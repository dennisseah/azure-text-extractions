import logging
from dataclasses import dataclass

import nltk
from azure.ai.textanalytics._models import RecognizeEntitiesResult
from azure.ai.textanalytics.aio import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from azure.identity import DefaultAzureCredential
from lagom.environment import Env

from az_text_extractions.models.recognized_entities import (
    RecognizedEntities,
    RecognizedEntity,
)
from az_text_extractions.models.sentence import Sentence
from az_text_extractions.protocols.i_text_extraction_service import (
    ITextExtractionService,
)

nltk.download("punkt_tab")


class TextExtractionServiceEnv(Env):
    azure_text_analytics_endpoint: str
    azure_text_analytics_key: str | None = None


@dataclass
class TextExtractionService(ITextExtractionService):
    env: TextExtractionServiceEnv

    logger: logging.Logger

    def get_client(self) -> TextAnalyticsClient:
        if self.env.azure_text_analytics_key is None:
            self.logger.info(
                "TextExtractionService: using Azure Default Credential to authenticate"
            )
            client = TextAnalyticsClient(
                endpoint=self.env.azure_text_analytics_endpoint,
                credential=DefaultAzureCredential(),  # type: ignore
            )
            self.logger.info("TextExtractionService: authenticated successfully")
            return client

        self.logger.info("TextExtractionService: using Azure API Key to authenticate")
        client = TextAnalyticsClient(
            endpoint=self.env.azure_text_analytics_endpoint,
            credential=AzureKeyCredential(self.env.azure_text_analytics_key),
        )
        self.logger.info("TextExtractionService: authenticated successfully")
        return client

    def generate_sentences(self, content: str) -> list[Sentence]:
        sentences = nltk.sent_tokenize(content)
        return [
            Sentence(content=sentence, start=content.index(sentence))
            for sentence in sentences
        ]

    def mapToRecognizedEntity(
        self, result: RecognizeEntitiesResult, statements: list[list[Sentence]]
    ) -> RecognizedEntities:
        entities = [
            RecognizedEntity(
                text=entity.text,
                category=entity.category,
                subcategory=entity.subcategory,
                confidence_score=entity.confidence_score,
                offset=entity.offset,
                length=entity.length,
                sentence=Sentence.includes(statements[int(result.id)], entity.offset),
            )
            for entity in result.entities
        ]

        return RecognizedEntities(id=result.id, entities=entities)

    async def recognize_entities(self, content: list[str]) -> list[RecognizedEntities]:
        if len(content) == 0:
            return []

        client = self.get_client()
        statements = [self.generate_sentences(c) for c in content]

        async with client:
            results = await client.recognize_entities(content)
            return [
                self.mapToRecognizedEntity(result, statements)
                for result in results
                if isinstance(result, RecognizeEntitiesResult)
            ]
