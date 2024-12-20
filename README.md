# azure-text-extractions
Using Azure Text Analytics Client to extract texts.

The results contains the confidence scores and reference to the original statement in the text.



## Deployment of Azure Services

see [infra/README.md](infra/README.md)

## Setup

1. Clone the repository
2. `cd azure-text-extractions` (root directory of this git repository)
3. `python -m venv .venv`
4. `poetry install` (install the dependencies)
5. code . (open the project in vscode)
6. install the recommended extensions (cmd + shift + p -> `Extensions: Show Recommended Extensions`)
7. `pre-commit install` (install the pre-commit hooks)
8. copy the `.env.sample` file to `.env` and fill in the values

## Unit Test Coverage

```sh
python -m pytest -p no:warnings --cov-report term-missing --cov=az_text_extractions tests
```

## Text Extraction

text are in data folder

```sh
python -m main
```
