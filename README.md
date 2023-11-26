# Writes description of the given image

## Setup instructions

1. **Create new Conda environment**:
    ```bash
    conda create -n ai-note python=3.10
    ```

2. **Activate Conda environment**:
    ```bash
    conda activate ai-note
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Add API Keys**:\
    Create *.env* file and assign your api key to OPENAI_API_KEY variable. Example:
    ```txt
    OPENAI_API_KEY="your_api_key"
    ```

5. **Add notes**:\
    Create folder for your notes and fill it with notes (currently .txt files)

6. **Run the program**:
    ```bash
    python main.py
    ```