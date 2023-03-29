# Chat with the Glucose Goddess 🧜‍♀️

A simple chatbot application that allows users to chat with the Glucose Goddess using Gradio for the interface and GPTSimpleVectorIndex for similarity search.

## Prerequisites

- Python 3.6 or later
- A virtual environment is recommended to manage dependencies

## Installation

1. Clone the repository:
git clone https://github.com/Fritskee/epubGPT.git

2. Change to the project directory:
cd epubGPT

3. Create and activate a virtual environment:
python -m venv venv
- Linux/Mac:
`source venv/bin/activate`
- Windows:
`venv\Scripts\activate`

4. Install the required dependencies:
`pip install -r requirements.txt`


## Usage

1. Set up the `.env` file with the following content:
`OPENAI_API_KEY=your_openai_api_key`

Replace `your_openai_api_key` with your actual API key.

2. Update the `book` variable in `main.py` to point to the path of the book file you want to use.

3. Run the application:
`python main.py`

4. Open the Gradio interface in your web browser using the URL provided in the terminal.

5. Type your query into the text input field and press "Submit" to get a response from the chatbot.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
