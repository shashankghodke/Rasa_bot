
# Rasa Bot

This repository contains a Rasa bot that can be run locally or using Docker.

## Prerequisites

- Python 3.6 or later
- pip
- (Optional) Docker and Docker Compose

## Setup

### 1. Clone the Repository

```sh
git clone <repository_url>
cd <repository_name>
```

### 2. Install Dependencies

```sh
pip install rasa
```

## Running the Bot

### 1. Initialize the Project

```sh
rasa init
```

### 2. Train the Model

```sh
rasa train
```

### 3. Run the Action Server (if you have custom actions)

```sh
rasa run actions
```

### 4. Run the Rasa Bot

```sh
rasa run
```

### 5. Interact with Your Bot

```sh
rasa shell
```

## Project Structure

- **data/nlu.yml**: Contains training examples for NLU.
- **data/stories.yml**: Contains example conversations.
- **domain.yml**: Defines the intents, entities, slots, responses, and actions.
- **actions/actions.py**: Contains custom actions (if any).

## Custom Actions Example (actions/actions.py)

```python
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHelloWorld(Action):
    def name(self) -> str:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        dispatcher.utter_message(text="Hello World!")
        return []
```

## Configuration Example (config.yml)

```yaml
recipe: default.v1
language: en
pipeline:
  - name: SpacyNLP
    model: "en_core_web_md"
  - name: SpacyTokenizer
  - name: SpacyFeaturizer
  - name: RegexFeaturizer
  - name: LexicalSyntacticFeaturizer
  - name: CountVectorsFeaturizer
  - name: CountVectorsFeaturizer
    analyzer: char_wb
    min_ngram: 1
    max_ngram: 4
  - name: DIETClassifier
    epochs: 100
  - name: EntitySynonymMapper
  - name: ResponseSelector
    epochs: 100

policies:
  - name: MemoizationPolicy
  - name: TEDPolicy
    max_history: 5
    epochs: 100
  - name: RulePolicy
```

## Running the Bot with Docker

If you prefer Docker, create a `docker-compose.yml` file:

```yaml
version: '3.0'

services:
  rasa:
    image: rasa/rasa:latest
    ports:
      - "5005:5005"
    volumes:
      - ./:/app
    command: ["run", "--enable-api"]

  action-server:
    image: rasa/rasa-sdk:latest
    ports:
      - "5055:5055"
    volumes:
      - ./actions:/app/actions
```

Then run:

```sh
docker-compose up
```

This will start both the Rasa server and the action server.

## License

This project is licensed under the MIT License.
