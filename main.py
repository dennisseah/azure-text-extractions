import json
import os

from az_text_extractions.hosting import container
from az_text_extractions.protocols.i_text_extraction_service import (
    ITextExtractionService,
)


def fetch_content():
    results = []
    for f in os.listdir("data"):
        if f.endswith(".txt"):
            with open(f"data/{f}") as file:
                results.append(file.read())
    return results


async def main():
    svc = container.resolve(ITextExtractionService)
    results = await svc.recognize_entities(
        [
            "Studies have shown that regular physical activity is "
            "associated with a longer lifespan, reducing the risk "
            "of premature death from all causes.",
            "Climate change refers to significant, long-term changes in "
            "the average temperature, weather patterns, and atmospheric "
            "conditions on Earth. Although climate change is a natural "
            "phenomenon, the current trend of rapid warming is largely "
            "attributed to human activities. Understanding the causes, "
            "effects, and potential solutions for climate change is "
            "critical for mitigating its impacts on the environment "
            "and human society.",
        ]
    )
    # results = await svc.recognize_entities(fetch_content())
    with open("results.json", "w") as file:
        json.dump([result.model_dump() for result in results], file, indent=4)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
