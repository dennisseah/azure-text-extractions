from typing import Protocol

from az_text_extractions.models.recognized_entities import (
    RecognizedEntities,
)


class ITextExtractionService(Protocol):
    async def recognize_entities(
        self, content: list[str]
    ) -> list[RecognizedEntities]: ...
