# 📖 API Reference

Complete API documentation for all 8 MissionControlMCP tools.

---

## 1. PDF Reader

### `read_pdf(file_path: str) -> Dict[str, Any]`

Extract text and metadata from PDF files.

**Parameters:**
- `file_path` (str): Absolute path to PDF file

**Returns:**
```python
{
    "text": str,           # Full text content from all pages
    "pages": int,          # Number of pages
    "metadata": {          # Document metadata
        "author": str,
        "creator": str,
        "producer": str,
        "subject": str,
        "title": str,
        "creation_date": str,
        "modification_date": str
    }
}
```

**Example:**
```python
from tools.pdf_reader import read_pdf

result = read_pdf("C:/docs/report.pdf")
print(f"Pages: {result['pages']}")
print(f"Author: {result['metadata']['author']}")
print(result['text'][:500])  # First 500 chars
```

**Errors:**
- `FileNotFoundError`: PDF file not found
- `ImportError`: PyPDF2 not installed
- `Exception`: Invalid or corrupted PDF

---

### `get_pdf_info(file_path: str) -> Dict[str, Any]`

Get basic PDF information without extracting text.

**Parameters:**
- `file_path` (str): Path to PDF file

**Returns:**
```python
{
    "page_count": int,
    "is_encrypted": bool,
    "file_size_bytes": int,
    "file_name": str
}
```

---

## 2. Text Extractor

### `extract_text(text: str, operation: str, **kwargs) -> Dict[str, Any]`

Process and extract information from text.

**Parameters:**
- `text` (str): Input text to process
- `operation` (str): Operation type
  - `"clean"` - Remove extra whitespace
  - `"summarize"` - Create summary
  - `"chunk"` - Split into chunks
  - `"keywords"` - Extract keywords
- `**kwargs`: Operation-specific parameters

**Operation: clean**
```python
extract_text(text, operation="clean")
# Returns: {"result": str, "word_count": int}
```

**Operation: summarize**
```python
extract_text(text, operation="summarize", max_length=500)
# max_length: Maximum summary length (default: 500)
# Returns: {"result": str, "word_count": int, "original_length": int}
```

**Operation: chunk**
```python
extract_text(text, operation="chunk", chunk_size=100, overlap=20)
# chunk_size: Characters per chunk (default: 100)
# overlap: Overlapping characters (default: 20)
# Returns: {"chunks": List[str], "chunk_count": int}
```

**Operation: keywords**
```python
extract_text(text, operation="keywords", top_n=10)
# top_n: Number of keywords (default: 10)
# Returns: {"result": str, "keywords": List[str]}
```

**Example:**
```python
from tools.text_extractor import extract_text

# Get keywords
result = extract_text("Your text here...", operation="keywords")
print(result['result'])  # "keyword1, keyword2, keyword3"

# Summarize
summary = extract_text("Long text...", operation="summarize", max_length=200)
print(summary['result'])
```

---

## 3. Web Fetcher

### `fetch_web_content(url: str, timeout: int = 30) -> Dict[str, Any]`

Fetch and parse web page content.

**Parameters:**
- `url` (str): Website URL
- `timeout` (int): Request timeout in seconds (default: 30)

**Returns:**
```python
{
    "url": str,
    "title": str,
    "content": str,         # Clean text content
    "html": str,            # Raw HTML
    "links": List[str],     # All URLs found
    "status_code": int,     # HTTP status
    "timestamp": str
}
```

**Example:**
```python
from tools.web_fetcher import fetch_web_content

result = fetch_web_content("https://example.com")
print(f"Title: {result['title']}")
print(f"Content: {result['content'][:200]}")
print(f"Links found: {len(result['links'])}")
```

**Errors:**
- `requests.exceptions.Timeout`: Request timed out
- `requests.exceptions.RequestException`: Network error
- `Exception`: Invalid URL or parsing error

---

## 4. RAG Search

### `search_documents(query: str, documents: List[str], top_k: int = 3) -> Dict[str, Any]`

Semantic search using vector embeddings and FAISS.

**Parameters:**
- `query` (str): Search query
- `documents` (List[str]): List of documents to search
- `top_k` (int): Number of results to return (default: 3)

**Returns:**
```python
{
    "query": str,
    "total_documents": int,
    "returned_results": int,
    "results": [
        {
            "rank": int,
            "document": str,
            "score": float,      # 0.0 to 1.0 (higher = more relevant)
            "distance": float    # L2 distance
        }
    ]
}
```

**Example:**
```python
from tools.rag_search import search_documents

docs = [
    "Machine learning is a subset of AI",
    "Python is a programming language",
    "Data science uses statistics"
]

result = search_documents("artificial intelligence", docs, top_k=2)

for item in result['results']:
    print(f"Score: {item['score']:.4f} - {item['document']}")
```

**Features:**
- Semantic matching (understands meaning, not just keywords)
- Uses sentence-transformers (all-MiniLM-L6-v2)
- FAISS for fast vector search

---

### `multi_query_search(queries: List[str], documents: List[str], top_k: int = 3) -> Dict[str, Any]`

Search multiple queries at once.

**Returns:**
```python
{
    "queries": List[str],
    "results": {
        "query1": [results],
        "query2": [results]
    }
}
```

---

## 5. Data Visualizer

### `visualize_data(data: str, chart_type: str, x_column: str = None, y_column: str = None, title: str = "Data Visualization") -> Dict[str, Any]`

Create charts from CSV or JSON data.

**Parameters:**
- `data` (str): CSV or JSON string
- `chart_type` (str): Chart type
  - `"bar"` - Bar chart
  - `"line"` - Line chart
  - `"pie"` - Pie chart
  - `"scatter"` - Scatter plot
- `x_column` (str): X-axis column name
- `y_column` (str): Y-axis column name
- `title` (str): Chart title

**Returns:**
```python
{
    "image_base64": str,     # Base64-encoded PNG image
    "dimensions": {
        "width": int,
        "height": int
    },
    "chart_type": str,
    "title": str,
    "columns_used": {
        "x": str,
        "y": str
    }
}
```

**Example:**
```python
from tools.data_visualizer import visualize_data
import base64

csv_data = """month,revenue
Jan,5000000
Feb,5200000
Mar,5400000"""

result = visualize_data(
    data=csv_data,
    chart_type="line",
    x_column="month",
    y_column="revenue",
    title="Revenue Trends"
)

# Save chart
with open("chart.png", "wb") as f:
    f.write(base64.b64decode(result['image_base64']))
```

---

## 6. File Converter

### `convert_file(input_path: str, output_path: str, conversion_type: str) -> Dict[str, Any]`

Convert between PDF, TXT, and CSV formats.

**Parameters:**
- `input_path` (str): Input file path
- `output_path` (str): Output file path
- `conversion_type` (str): Conversion type
  - `"pdf_to_txt"` - PDF → Text
  - `"txt_to_pdf"` - Text → PDF
  - `"csv_to_txt"` - CSV → Text
  - `"txt_to_csv"` - Text → CSV

**Returns:**
```python
{
    "success": bool,
    "input_file": str,
    "output_file": str,
    "conversion_type": str,
    "file_size_bytes": int
}
```

**Example:**
```python
from tools.file_converter import convert_file

result = convert_file(
    input_path="document.pdf",
    output_path="document.txt",
    conversion_type="pdf_to_txt"
)

print(f"Converted: {result['success']}")
print(f"Output: {result['output_file']}")
```

---

## 7. Email Intent Classifier

### `classify_email_intent(email_text: str) -> Dict[str, Any]`

Classify email intent using NLP pattern matching.

**Parameters:**
- `email_text` (str): Email content (subject + body)

**Returns:**
```python
{
    "intent": str,          # Primary intent
    "confidence": float,    # 0.0 to 1.0
    "secondary_intents": [
        {
            "intent": str,
            "confidence": float
        }
    ],
    "explanation": str
}
```

**Intent Types:**
- `complaint` - Customer complaints
- `inquiry` - Information requests
- `request` - Action requests
- `feedback` - Suggestions/reviews
- `order` - Purchase-related
- `meeting` - Meeting scheduling
- `urgent` - High priority issues
- `application` - Job applications
- `sales` - Sales pitches
- `other` - Unclassified

**Example:**
```python
from tools.email_intent_classifier import classify_email_intent

email = """
Subject: Order Issue
My order #12345 hasn't arrived yet. Can you help?
"""

result = classify_email_intent(email)
print(f"Intent: {result['intent']}")          # "complaint"
print(f"Confidence: {result['confidence']}")  # 0.85
```

---

### `classify_batch(emails: List[str]) -> Dict[str, Any]`

Classify multiple emails at once.

**Returns:**
```python
{
    "results": [
        {"email_index": int, "intent": str, "confidence": float},
        ...
    ],
    "total_processed": int
}
```

---

## 8. KPI Generator

### `generate_kpis(data: str, metrics: List[str] = None) -> Dict[str, Any]`

Calculate business KPIs from financial data.

**Parameters:**
- `data` (str): JSON string with business data
- `metrics` (List[str]): Metric categories (optional)
  - `"revenue"` - Revenue-related KPIs
  - `"growth"` - Growth rates
  - `"efficiency"` - Efficiency metrics
  - `"customer"` - Customer metrics
  - `"operational"` - Operational metrics

**Input Data Format:**
```json
{
    "revenue": 5000000,
    "costs": 3000000,
    "customers": 2500,
    "current_revenue": 5000000,
    "previous_revenue": 4500000,
    "current_customers": 2500,
    "previous_customers": 2300,
    "employees": 50,
    "marketing_spend": 500000,
    "sales": 5000000,
    "cogs": 2000000
}
```

**Returns:**
```python
{
    "kpis": {
        "total_revenue": float,
        "profit": float,
        "profit_margin_percent": float,
        "revenue_growth": float,
        "revenue_per_customer": float,
        "revenue_per_employee": float,
        "customer_growth_rate": float,
        ...
    },
    "summary": str,              # Executive summary
    "trends": List[str],         # Identified trends
    "metrics_analyzed": List[str],
    "data_points": int
}
```

**Example:**
```python
from tools.kpi_generator import generate_kpis
import json

data = {
    "revenue": 5000000,
    "costs": 3000000,
    "customers": 2500,
    "employees": 50
}

result = generate_kpis(json.dumps(data), metrics=["revenue", "efficiency"])

print(f"Profit: ${result['kpis']['profit']:,.0f}")
print(f"Margin: {result['kpis']['profit_margin_percent']:.1f}%")
print(f"\nSummary: {result['summary']}")
```

---

## Error Handling

All tools follow consistent error handling:

```python
try:
    result = tool_function(params)
except FileNotFoundError as e:
    print(f"File not found: {e}")
except ValueError as e:
    print(f"Invalid input: {e}")
except ImportError as e:
    print(f"Missing dependency: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

## Type Hints

All functions use Python type hints:

```python
from typing import Dict, Any, List

def function_name(param: str) -> Dict[str, Any]:
    ...
```

---

## Logging

All tools use Python logging:

```python
import logging
logger = logging.getLogger(__name__)

logger.info("Operation completed")
logger.warning("Warning message")
logger.error("Error occurred")
```

---

## Dependencies

See `requirements.txt` for all dependencies:

```txt
mcp>=1.0.0
pypdf2>=3.0.0
requests>=2.31.0
beautifulsoup4>=4.12.0
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
scikit-learn>=1.3.0
nltk>=3.8.0
pydantic>=2.0.0
faiss-cpu>=1.7.4
sentence-transformers>=2.2.0
```

---

## MCP Integration

All tools are registered in `mcp_server.py`:

```python
server.register_tool(
    name="pdf_reader",
    description="Extract text and metadata from PDF files",
    input_schema={
        "type": "object",
        "properties": {
            "file_path": {"type": "string"}
        },
        "required": ["file_path"]
    }
)
```

---

## Version Information

- **API Version:** 1.0.0
- **Python:** 3.8+
- **MCP Protocol:** 1.0.0

---

## Support

For issues or questions:
- GitHub: AlBaraa-1/CleanEye-Hackathon
- Documentation: README.md
- Examples: EXAMPLES.md
- Testing: TESTING.md

**Complete API reference for MissionControlMCP!** 🚀
