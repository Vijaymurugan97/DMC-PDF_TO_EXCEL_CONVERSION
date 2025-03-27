# PDF Data Extractor

A Python application for extracting structured data from PDF documents. This application provides a graphical user interface for processing PDF files and exporting the extracted data to Excel format.

## Features

- GUI-based PDF processing
- Extract structured data from PDF documents
- Edit extracted data through an interactive interface
- Export data to Excel format
- Persistent storage using SQLite database

## Installation

1. Create and activate a virtual environment (recommended):

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Directory Structure

```
sono_package/
├── src/               # Source code
│   ├── extractor.py  # Main application
│   └── db_handler.py # Database operations
├── data/             # Data directory
│   ├── input/        # Place PDF files here
│   └── output/       # Exported Excel files
└── requirements.txt  # Python dependencies
```

## Usage

1. Place your PDF files in the `data/input` directory.

2. Run the application:

```bash
python src/extractor.py
```

3. Using the application:
   - Click "Browse" to select a PDF file
   - Click "Process PDF" to extract data
   - Double-click on cells to edit values if needed
   - Click "Export to Excel" to save the data

## Data Storage

The application uses a SQLite database (`data/pdf_data.db`) to store processed data. This ensures data persistence between sessions and enables quick access to previously processed information.

## Support

For any issues or questions, please check the source code documentation or create an issue in the repository.
