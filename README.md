# Chatbot

This is a basic chatbot implemented in Python that allows users to interact in both user and trainer modes. In user mode, the chatbot responds to user queries, and in trainer mode, it learns from trainers by allowing them to input new responses for user queries.

## Getting Started

### Prerequisites

- Python 2.x (Note: The code uses `raw_input`, which is specific to Python 2. For Python 3, you should replace it with `input`.)
- [trainer.py](trainer.py) - Module for the trainer mode functions
- [user.py](user.py) - Module for the user mode functions

### Usage

1. Run the main script:

    ```bash
    python main.py
    ```

2. Choose between entering "trainer" mode or "user" mode when prompted.

### User Mode

In user mode, the chatbot responds to user inputs based on pre-defined responses stored in a JSON file.

### Trainer Mode

In trainer mode, the chatbot allows the trainer to input new responses for user queries. If a query doesn't have a predefined response, the trainer can add one.

## Code Structure

- [main.py](main.py): Main entry point, presents the option to enter trainer or user mode.
- [user.py](user.py): Contains functions for user mode, including reading the JSON file and generating responses.
- [trainer.py](trainer.py): Functions for trainer mode, including checking for matches, adding new responses, and finding best matches.

## Contributing

Feel free to contribute by adding new features, improving existing code, or fixing issues. Please follow the existing code style and open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

