"""
🚀 MissionControlMCP - Interactive Demo
Try all 8 tools with real examples!

Run: python demo.py
"""

import sys
import os
import json
import base64
from pathlib import Path

# Setup paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(SCRIPT_DIR)
EXAMPLES_DIR = os.path.join(SCRIPT_DIR, "examples")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "demo_output")

# Create output directory
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Import tools
from tools.pdf_reader import read_pdf
from tools.text_extractor import extract_text
from tools.web_fetcher import fetch_web_content
from tools.rag_search import search_documents
from tools.data_visualizer import visualize_data
from tools.file_converter import convert_file
from tools.email_intent_classifier import classify_email_intent
from tools.kpi_generator import generate_kpis


def print_header(title):
    """Print a nice header"""
    print("\n" + "="*80)
    print(f"  {title}")
    print("="*80)


def print_section(title):
    """Print a section header"""
    print(f"\n{'─'*80}")
    print(f"📌 {title}")
    print(f"{'─'*80}")


def pause(message="Press Enter to continue..."):
    """Pause and wait for user input"""
    input(f"\n{message}")


def save_chart(image_base64, filename):
    """Save base64 chart to file"""
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "wb") as f:
        f.write(base64.b64decode(image_base64))
    print(f"💾 Chart saved: {filepath}")
    return filepath


# ============================================================================
# TOOL 1: PDF READER
# ============================================================================

def demo_pdf_reader():
    """Demo: PDF Reader - Extract text from PDFs"""
    print_header("TOOL 1: PDF READER 📄")
    
    print("\n📖 What it does:")
    print("  • Extracts all text from PDF files")
    print("  • Gets metadata (author, title, pages)")
    print("  • Perfect for reading reports, contracts, invoices")
    
    print("\n💡 Real-world uses:")
    print("  • Extract data from invoices")
    print("  • Read research papers")
    print("  • Process legal contracts")
    print("  • Analyze business reports")
    
    pause("\nReady to see it in action? Press Enter...")
    
    # Check if user has their own PDF
    print("\n" + "─"*80)
    custom_pdf = input("Enter PDF file path (or press Enter to skip): ").strip()
    
    if custom_pdf and os.path.exists(custom_pdf):
        print(f"\n📄 Reading your PDF: {custom_pdf}")
        try:
            result = read_pdf(custom_pdf)
            print(f"\n✅ Successfully extracted:")
            print(f"  • Pages: {result['pages']}")
            print(f"  • Characters: {len(result['text']):,}")
            print(f"  • Author: {result['metadata'].get('author', 'N/A')}")
            print(f"\n📝 First 300 characters:")
            print(result['text'][:300] + "...")
            
            # Extract keywords from PDF
            print("\n🔑 Extracting keywords from PDF...")
            keywords = extract_text(result['text'], operation="keywords")
            print(f"Keywords: {keywords['result']}")
            
        except Exception as e:
            print(f"❌ Error: {e}")
    else:
        print("\n📝 Example: How it works")
        print("```python")
        print("result = read_pdf('document.pdf')")
        print("print(f'Pages: {result[\"pages\"]}')")
        print("print(result['text'][:500])  # First 500 chars")
        print("```")
        print("\n💬 Output:")
        print("  Pages: 16")
        print("  Text: College Of Engineering - System Analysis Project...")
    
    pause()


# ============================================================================
# TOOL 2: TEXT EXTRACTOR
# ============================================================================

def demo_text_extractor():
    """Demo: Text Extractor - Process and analyze text"""
    print_header("TOOL 2: TEXT EXTRACTOR 📝")
    
    print("\n📖 What it does:")
    print("  • Extract keywords from any text")
    print("  • Generate summaries (any length)")
    print("  • Clean messy text")
    print("  • Split text into chunks")
    
    print("\n💡 Real-world uses:")
    print("  • Summarize long documents")
    print("  • Find main topics in articles")
    print("  • Clean data before analysis")
    print("  • Prepare text for processing")
    
    pause("\nReady to try it? Press Enter...")
    
    # Load sample report
    print_section("Using sample business report")
    sample_file = os.path.join(EXAMPLES_DIR, "sample_report.txt")
    
    try:
        with open(sample_file, "r", encoding="utf-8") as f:
            text = f.read()
        
        print(f"📄 Loaded text: {len(text)} characters")
        print(f"\nPreview: {text[:200]}...")
        
        pause("\nPress Enter to extract keywords...")
        
        # Operation 1: Keywords
        print_section("Operation 1: Extract Keywords")
        keywords = extract_text(text, operation="keywords")
        print(f"🔑 Keywords: {keywords['result']}")
        
        pause("\nPress Enter to generate summary...")
        
        # Operation 2: Summarize
        print_section("Operation 2: Generate Summary")
        summary = extract_text(text, operation="summarize", max_length=300)
        print(f"📝 Summary ({len(summary['result'])} chars):")
        print(summary['result'])
        
        pause("\nPress Enter to clean text...")
        
        # Operation 3: Clean
        print_section("Operation 3: Clean Text")
        messy_text = "  This   has   extra    spaces\n\n\nand  newlines  "
        cleaned = extract_text(messy_text, operation="clean")
        print(f"Before: '{messy_text}'")
        print(f"After:  '{cleaned['result']}'")
        
        # Operation 4: Chunk
        print_section("Operation 4: Split into Chunks")
        chunks = extract_text(text[:500], operation="chunk", max_length=100)
        chunk_list = chunks['result'].split("\n\n---CHUNK---\n\n")
        print(f"✂️ Split into {len(chunk_list)} chunks (100 chars each)")
        print(f"Chunk 1: {chunk_list[0][:80]}...")
        
        # Try custom text
        print("\n" + "─"*80)
        custom_text = input("\n✏️ Want to try your own text? Enter it (or press Enter to skip): ").strip()
        if custom_text:
            print("\n🔑 Keywords from your text:")
            result = extract_text(custom_text, operation="keywords")
            print(result['result'])
            
            print("\n📝 Summary of your text:")
            result = extract_text(custom_text, operation="summarize", max_length=300)
            if result['result']:
                print(result['result'])
            else:
                # If summary is empty, show first 300 chars as fallback
                print(custom_text[:300] + ("..." if len(custom_text) > 300 else ""))
        
    except Exception as e:
        print(f"❌ Error: {e}")
    
    pause()


# ============================================================================
# TOOL 3: WEB FETCHER
# ============================================================================

def demo_web_fetcher():
    """Demo: Web Fetcher - Scrape web content"""
    print_header("TOOL 3: WEB FETCHER 🌐")
    
    print("\n📖 What it does:")
    print("  • Fetches content from any website")
    print("  • Extracts clean text (no HTML tags)")
    print("  • Finds all links on the page")
    print("  • Gets page title and metadata")
    
    print("\n💡 Real-world uses:")
    print("  • Monitor competitor websites")
    print("  • Collect research data")
    print("  • Track price changes")
    print("  • Gather news articles")
    
    pause("\nReady to fetch a website? Press Enter...")
    
    # Allow retry loop
    while True:
        # Get URL from user
        print("\n" + "─"*80)
        url = input("Enter URL to fetch (or press Enter for example.com): ").strip()
        if not url:
            url = "https://example.com"
        
        print(f"\n🌐 Fetching: {url}")
        print("⏳ Please wait...")
        
        success = False
        try:
            result = fetch_web_content(url)
            
            print(f"\n✅ Success!")
            print(f"  • Status: {result['status_code']}")
            print(f"  • Title: {result.get('title', 'N/A')}")
            print(f"  • Content length: {len(result['content']):,} characters")
            print(f"  • Links found: {len(result.get('links', []))}")
            
            # Check if content is available
            if result['status_code'] == 999:
                print(f"\n⚠️  Status 999 detected - Website is blocking automated requests")
                print("   This is common for LinkedIn, Facebook, and other sites with bot protection")
                print("   Try a different website!")
            elif not result['content'].strip():
                print(f"\n⚠️  No content extracted - the page might be dynamic (JavaScript-based)")
            else:
                success = True
                print(f"\n📄 Content preview (first 500 chars):")
                print(result['content'][:500] + "...")
                
                if result.get('links'):
                    print(f"\n🔗 First 5 links:")
                    for link in result['links'][:5]:
                        print(f"  • {link[:80]}")  # Truncate long URLs
                
                # Extract keywords from webpage
                if len(result['content']) > 50:
                    pause("\nPress Enter to extract keywords from this page...")
                    keywords = extract_text(result['content'], operation="keywords")
                    print(f"\n🔑 Keywords from webpage:")
                    print(f"  {keywords['result']}")
            
        except Exception as e:
            print(f"❌ Error fetching URL: {e}")
            print("Tip: Make sure the URL is valid and accessible!")
        
        # Ask if user wants to try another URL
        print("\n" + "─"*80)
        retry = input("Try another URL? (y/n): ").strip().lower()
        if retry != 'y':
            break
    
    pause()


# ============================================================================
# TOOL 4: RAG SEARCH
# ============================================================================

def demo_rag_search():
    """Demo: RAG Search - Semantic document search"""
    print_header("TOOL 4: RAG SEARCH 🔍")
    
    print("\n📖 What it does:")
    print("  • Semantic search (understands meaning, not just keywords)")
    print("  • Finds relevant documents even with different words")
    print("  • Uses AI embeddings (sentence transformers)")
    print("  • Powered by FAISS vector database")
    
    print("\n💡 Real-world uses:")
    print("  • Search company knowledge base")
    print("  • Find similar documents")
    print("  • Answer questions from docs")
    print("  • Build smart FAQ systems")
    
    pause("\nReady to see semantic search in action? Press Enter...")
    
    # Load sample documents
    print_section("Loading sample documents")
    docs_file = os.path.join(EXAMPLES_DIR, "sample_documents.txt")
    
    try:
        with open(docs_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        documents = [doc.strip() for doc in content.split("##") if doc.strip()]
        print(f"📚 Loaded {len(documents)} documents about:")
        topics = ["AI & Machine Learning", "Climate Change", "Web Development", 
                  "Digital Marketing", "Financial Technology"]
        for i, topic in enumerate(topics, 1):
            print(f"  {i}. {topic}")
        
        pause("\nPress Enter to search...")
        
        # Example searches
        queries = [
            ("What is machine learning?", "Testing: Does it find AI doc?"),
            ("How to reduce carbon emissions?", "Testing: Does it find climate doc?"),
            ("What are modern web frameworks?", "Testing: Does it find web dev doc?"),
        ]
        
        for query, description in queries:
            print_section(description)
            print(f"🔍 Query: '{query}'")
            print("⏳ Searching...")
            
            result = search_documents(query, documents, top_k=2)
            
            print(f"\n✅ Found {len(result['results'])} relevant results:")
            for i, res in enumerate(result['results'], 1):
                preview = res['document'][:120].replace('\n', ' ')
                print(f"\n  {i}. Relevance Score: {res['score']:.4f}")
                print(f"     {preview}...")
            
            pause()
        
        # Custom search
        print("\n" + "─"*80)
        custom_query = input("\n✏️ Try your own search query (or press Enter to skip): ").strip()
        if custom_query:
            print(f"\n🔍 Searching for: '{custom_query}'")
            result = search_documents(custom_query, documents, top_k=3)
            print(f"\n📊 Top {len(result['results'])} results:")
            for i, res in enumerate(result['results'], 1):
                preview = res['document'][:100].replace('\n', ' ')
                print(f"\n  {i}. Score: {res['score']:.4f}")
                print(f"     {preview}...")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    
    pause()


# ============================================================================
# TOOL 5: DATA VISUALIZER
# ============================================================================

def demo_data_visualizer():
    """Demo: Data Visualizer - Create charts"""
    print_header("TOOL 5: DATA VISUALIZER 📊")
    
    print("\n📖 What it does:")
    print("  • Creates beautiful charts from data")
    print("  • Supports: Bar, Line, Pie, Scatter plots")
    print("  • Accepts CSV or JSON data")
    print("  • Exports as PNG images")
    
    print("\n💡 Real-world uses:")
    print("  • Visualize sales trends")
    print("  • Create financial reports")
    print("  • Compare performance metrics")
    print("  • Present data insights")
    
    pause("\nReady to create charts? Press Enter...")
    
    # Load sample data
    print_section("Loading business data")
    csv_file = os.path.join(EXAMPLES_DIR, "business_data.csv")
    
    try:
        with open(csv_file, "r") as f:
            csv_data = f.read()
        
        print("📁 Sample data (12 months):")
        print(csv_data[:200] + "...")
        
        pause("\nPress Enter to create LINE CHART (Revenue Trends)...")
        
        # Chart 1: Line chart
        print_section("Creating Chart 1: Revenue Line Chart")
        result1 = visualize_data(
            data=csv_data,
            chart_type="line",
            x_column="month",
            y_column="revenue",
            title="Monthly Revenue Trends 2024"
        )
        filepath1 = save_chart(result1['image_base64'], "revenue_trends.png")
        print(f"✅ Line chart created!")
        print(f"   Size: {len(result1['image_base64']):,} bytes (base64)")
        print(f"   Dimensions: {result1['dimensions']}")
        
        pause("\nPress Enter to create BAR CHART (Monthly Costs)...")
        
        # Chart 2: Bar chart
        print_section("Creating Chart 2: Costs Bar Chart")
        result2 = visualize_data(
            data=csv_data,
            chart_type="bar",
            x_column="month",
            y_column="costs",
            title="Monthly Costs 2024"
        )
        filepath2 = save_chart(result2['image_base64'], "monthly_costs.png")
        print(f"✅ Bar chart created!")
        
        pause("\nPress Enter to create PIE CHART (Customer Distribution)...")
        
        # Chart 3: Pie chart
        print_section("Creating Chart 3: Customers Pie Chart")
        # Create sample pie data
        pie_data = """category,value
Q1,650
Q2,600
Q3,550
Q4,500"""
        result3 = visualize_data(
            data=pie_data,
            chart_type="pie",
            x_column="category",
            y_column="value",
            title="Customers by Quarter"
        )
        filepath3 = save_chart(result3['image_base64'], "customer_pie.png")
        print(f"✅ Pie chart created!")
        
        print(f"\n📊 All charts saved in: {OUTPUT_DIR}")
        print(f"  • {os.path.basename(filepath1)}")
        print(f"  • {os.path.basename(filepath2)}")
        print(f"  • {os.path.basename(filepath3)}")
        
        print("\n💡 You can open these PNG files to view the charts!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    
    pause()


# ============================================================================
# TOOL 6: FILE CONVERTER
# ============================================================================

def demo_file_converter():
    """Demo: File Converter - Convert between formats"""
    print_header("TOOL 6: FILE CONVERTER 🔄")
    
    print("\n📖 What it does:")
    print("  • Convert PDF ↔ TXT")
    print("  • Convert TXT ↔ CSV")
    print("  • Batch file processing")
    print("  • Preserves data integrity")
    
    print("\n💡 Real-world uses:")
    print("  • Extract text from PDFs")
    print("  • Convert reports to CSV for analysis")
    print("  • Prepare data for databases")
    print("  • Archive documents in different formats")
    
    print("\n🔧 Available conversions:")
    print("  • pdf_to_txt - Extract text from PDF")
    print("  • txt_to_pdf - Create PDF from text")
    print("  • csv_to_txt - Convert CSV to plain text")
    print("  • txt_to_csv - Structure text as CSV")
    
    pause("\nReady to see file conversions? Press Enter...")
    
    try:
        # Demo 1: CSV to TXT
        print_section("Demo 1: CSV → TXT Conversion")
        csv_file = os.path.join(EXAMPLES_DIR, "business_data.csv")
        txt_output = os.path.join(OUTPUT_DIR, "business_data.txt")
        
        print(f"📂 Converting: business_data.csv → business_data.txt")
        print("⏳ Processing...")
        
        result1 = convert_file(
            input_path=csv_file,
            output_path=txt_output,
            conversion_type="csv_to_txt"
        )
        
        if result1['success']:
            print(f"✅ Conversion successful!")
            print(f"   Output: {result1['output_file']}")
            
            # Show preview
            with open(txt_output, 'r', encoding='utf-8') as f:
                preview = f.read()[:300]
            print(f"\n📄 Preview of converted file:")
            print(preview + "...")
        
        pause("\nPress Enter for next conversion...")
        
        # Demo 2: TXT to CSV
        print_section("Demo 2: TXT → CSV Conversion")
        txt_input = os.path.join(EXAMPLES_DIR, "sample_report.txt")
        csv_output = os.path.join(OUTPUT_DIR, "sample_report.csv")
        
        print(f"📂 Converting: sample_report.txt → sample_report.csv")
        print("⏳ Processing...")
        
        result2 = convert_file(
            input_path=txt_input,
            output_path=csv_output,
            conversion_type="txt_to_csv"
        )
        
        if result2['success']:
            print(f"✅ Conversion successful!")
            print(f"   Output: {result2['output_file']}")
            
            # Show preview
            with open(csv_output, 'r', encoding='utf-8') as f:
                lines = f.readlines()[:5]
            print(f"\n📄 First 5 lines of CSV:")
            for line in lines:
                print(f"   {line.strip()}")
        
        print(f"\n� Converted files saved in: {OUTPUT_DIR}")
        print(f"  • business_data.txt")
        print(f"  • sample_report.csv")
        
        # Offer custom conversion
        print("\n" + "─"*80)
        print("\n🔧 Want to convert your own file?")
        print("Supported conversions: pdf_to_txt, txt_to_pdf, csv_to_txt, txt_to_csv")
        
        custom_input = input("\nEnter input file path (or press Enter to skip): ").strip()
        if custom_input and os.path.exists(custom_input):
            custom_output = input("Enter output file path: ").strip()
            conversion_type = input("Enter conversion type (e.g., pdf_to_txt): ").strip()
            
            if custom_output and conversion_type:
                print(f"\n🔄 Converting {os.path.basename(custom_input)}...")
                try:
                    result = convert_file(custom_input, custom_output, conversion_type)
                    if result['success']:
                        print(f"✅ Success! File saved: {result['output_file']}")
                except Exception as e:
                    print(f"❌ Conversion failed: {e}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    
    pause()


# ============================================================================
# TOOL 7: EMAIL INTENT CLASSIFIER
# ============================================================================

def demo_email_classifier():
    """Demo: Email Intent Classifier - Understand email purpose"""
    print_header("TOOL 7: EMAIL INTENT CLASSIFIER 📧")
    
    print("\n📖 What it does:")
    print("  • Automatically classifies email intent")
    print("  • Detects 10 different types")
    print("  • Gives confidence scores")
    print("  • Finds secondary intents too")
    
    print("\n📬 Detects these intents:")
    intents = [
        "complaint", "inquiry", "request", "feedback", "order",
        "meeting", "urgent", "application", "sales", "other"
    ]
    for i, intent in enumerate(intents, 1):
        print(f"  {i:2d}. {intent.title()}")
    
    print("\n💡 Real-world uses:")
    print("  • Auto-route customer emails")
    print("  • Prioritize urgent messages")
    print("  • Organize inbox automatically")
    print("  • Track complaint patterns")
    
    pause("\nReady to classify emails? Press Enter...")
    
    # Test with sample emails
    email_files = [
        ("sample_email_complaint.txt", "Customer Complaint"),
        ("sample_email_inquiry.txt", "Sales Inquiry"),
        ("sample_email_urgent.txt", "Urgent Issue"),
    ]
    
    for filename, label in email_files:
        print_section(f"Email: {label}")
        filepath = os.path.join(EXAMPLES_DIR, filename)
        
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                email_text = f.read()
            
            print(f"📧 Email content:")
            print(email_text[:200] + "...\n")
            
            result = classify_email_intent(email_text)
            
            print(f"🎯 Classification Results:")
            print(f"  Primary Intent: {result['intent'].upper()}")
            print(f"  Confidence: {result['confidence']:.2%}")
            
            if result['secondary_intents']:
                print(f"\n  Secondary Intents:")
                for intent in result['secondary_intents'][:3]:
                    print(f"    • {intent['intent']}: {intent['confidence']:.2%}")
            
            print(f"\n💬 {result['explanation']}")
            
            pause()
            
        except Exception as e:
            print(f"❌ Error: {e}")
    
    # Custom email
    print("\n" + "─"*80)
    print("\n✏️ Want to try your own email?")
    custom_email = input("Paste email text (or press Enter to skip): ").strip()
    
    if custom_email:
        print("\n🔍 Analyzing your email...")
        result = classify_email_intent(custom_email)
        print(f"\n🎯 Intent: {result['intent'].upper()}")
        print(f"   Confidence: {result['confidence']:.2%}")
        if result['secondary_intents']:
            print(f"   Also detected: {result['secondary_intents'][0]['intent']}")
    
    pause()


# ============================================================================
# TOOL 8: KPI GENERATOR
# ============================================================================

def demo_kpi_generator():
    """Demo: KPI Generator - Calculate business metrics"""
    print_header("TOOL 8: KPI GENERATOR 📈")
    
    print("\n📖 What it does:")
    print("  • Calculates business KPIs automatically")
    print("  • Analyzes 5 metric categories")
    print("  • Identifies trends and insights")
    print("  • Generates executive summaries")
    
    print("\n📊 Metric categories:")
    print("  1. Revenue - Total revenue, profit, margins")
    print("  2. Growth - Growth rates, trends over time")
    print("  3. Efficiency - Revenue per employee/customer")
    print("  4. Customer - Customer acquisition, retention")
    print("  5. Operational - Operational efficiency metrics")
    
    print("\n💡 Real-world uses:")
    print("  • Monthly performance reports")
    print("  • Executive dashboards")
    print("  • Investor presentations")
    print("  • Business health monitoring")
    
    pause("\nReady to generate KPIs? Press Enter...")
    
    # Sample business data
    print_section("Sample Business Data")
    business_data = {
        "revenue": 5500000,
        "costs": 3400000,
        "customers": 2700,
        "current_revenue": 5500000,
        "previous_revenue": 5400000,
        "current_customers": 2700,
        "previous_customers": 2650,
        "employees": 50,
        "marketing_spend": 500000,
        "sales": 5500000,
        "cogs": 2000000
    }
    
    print("📊 Input data:")
    for key, value in business_data.items():
        if 'revenue' in key or 'cost' in key or 'spend' in key or 'sales' in key or 'cogs' in key:
            print(f"  • {key}: ${value:,}")
        else:
            print(f"  • {key}: {value:,}")
    
    pause("\nPress Enter to calculate KPIs...")
    
    try:
        # Generate KPIs
        print_section("Calculating KPIs")
        print("⏳ Analyzing data...")
        
        result = generate_kpis(
            json.dumps(business_data),
            metrics=["revenue", "growth", "efficiency"]
        )
        
        print(f"\n✅ Generated {len(result['kpis'])} KPIs:")
        print("\n📈 Key Metrics:")
        
        # Display KPIs nicely
        kpi_items = list(result['kpis'].items())
        for i, (name, value) in enumerate(kpi_items[:10], 1):  # Show top 10
            # Format based on metric type
            if 'percent' in name or 'rate' in name or 'margin' in name:
                formatted = f"{value:.1f}%"
            elif 'revenue' in name or 'profit' in name or 'cost' in name:
                formatted = f"${value:,.0f}"
            else:
                formatted = f"{value:,.2f}"
            
            # Clean name
            display_name = name.replace('_', ' ').title()
            print(f"  {i:2d}. {display_name}: {formatted}")
        
        if len(kpi_items) > 10:
            print(f"  ... and {len(kpi_items) - 10} more")
        
        pause("\nPress Enter to see executive summary...")
        
        # Summary
        print_section("Executive Summary")
        print(result['summary'])
        
        # Trends
        if result.get('trends'):
            print("\n📊 Key Trends Identified:")
            for i, trend in enumerate(result['trends'], 1):
                print(f"  {i}. {trend}")
        
        # Try custom data
        print("\n" + "─"*80)
        print("\n✏️ Want to calculate KPIs for your own data?")
        print("Enter JSON data (or press Enter to skip):")
        print("Example: {\"revenue\": 1000000, \"costs\": 600000, \"customers\": 500}")
        
        custom_data = input("\nYour data: ").strip()
        if custom_data:
            try:
                # Validate JSON
                json.loads(custom_data)
                result = generate_kpis(custom_data, metrics=["revenue"])
                print(f"\n✅ Your KPIs:")
                for name, value in list(result['kpis'].items())[:5]:
                    print(f"  • {name}: {value}")
            except json.JSONDecodeError:
                print("❌ Invalid JSON format!")
            except Exception as e:
                print(f"❌ Error: {e}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    
    pause()


# ============================================================================
# MAIN MENU
# ============================================================================

def show_menu():
    """Display main menu"""
    print("\n" + "╔" + "═"*78 + "╗")
    print("║" + " "*20 + "🚀 MissionControlMCP Demo" + " "*33 + "║")
    print("║" + " "*25 + "Try All 8 Tools!" + " "*36 + "║")
    print("╚" + "═"*78 + "╝")
    
    print("\n📋 MENU - Choose a tool to try:")
    print("\n  [1] 📄 PDF Reader           - Extract text from PDFs")
    print("  [2] 📝 Text Extractor       - Keywords, summaries, cleaning")
    print("  [3] 🌐 Web Fetcher          - Scrape website content")
    print("  [4] 🔍 RAG Search           - Semantic document search")
    print("  [5] 📊 Data Visualizer      - Create beautiful charts")
    print("  [6] 🔄 File Converter       - Convert file formats")
    print("  [7] 📧 Email Classifier     - Detect email intent")
    print("  [8] 📈 KPI Generator        - Business metrics & insights")
    
    print("\n  [9] 🎯 Run ALL Tools        - Full demo (recommended!)")
    print("  [0] 🚪 Exit")
    
    print("\n" + "─"*80)


def run_all_tools():
    """Run all tool demos in sequence"""
    print_header("🎯 RUNNING ALL TOOLS - COMPLETE DEMO")
    print("\nThis will walk you through all 8 tools with examples.")
    print("You can pause, try your own data, and explore each tool.")
    
    pause("\nReady to start? Press Enter...")
    
    tools = [
        demo_pdf_reader,
        demo_text_extractor,
        demo_web_fetcher,
        demo_rag_search,
        demo_data_visualizer,
        demo_file_converter,
        demo_email_classifier,
        demo_kpi_generator
    ]
    
    for i, tool_func in enumerate(tools, 1):
        print(f"\n\n{'='*80}")
        print(f"  TOOL {i} OF {len(tools)}")
        print(f"{'='*80}")
        tool_func()
    
    print_header("🎉 DEMO COMPLETE!")
    print("\n✅ You've explored all 8 MissionControlMCP tools!")
    print(f"\n📁 Generated files saved in: {OUTPUT_DIR}")
    print("\n💡 Next steps:")
    print("  • Try the tools with your own data")
    print("  • Integrate with Claude Desktop")
    print("  • Build custom workflows")
    print("  • Check out the documentation (README.md)")
    print("\n🚀 Happy automating!")


def main():
    """Main program loop"""
    
    print("\n" + "╔" + "═"*78 + "╗")
    print("║" + " "*15 + "Welcome to MissionControlMCP Demo!" + " "*29 + "║")
    print("╚" + "═"*78 + "╝")
    
    print("\n👋 This interactive demo lets you:")
    print("  ✅ Try all 8 enterprise automation tools")
    print("  ✅ See real examples with sample data")
    print("  ✅ Test with your own data")
    print("  ✅ Understand what each tool does")
    
    pause("\nPress Enter to continue...")
    
    while True:
        show_menu()
        
        choice = input("\n👉 Enter your choice (0-9): ").strip()
        
        if choice == "1":
            demo_pdf_reader()
        elif choice == "2":
            demo_text_extractor()
        elif choice == "3":
            demo_web_fetcher()
        elif choice == "4":
            demo_rag_search()
        elif choice == "5":
            demo_data_visualizer()
        elif choice == "6":
            demo_file_converter()
        elif choice == "7":
            demo_email_classifier()
        elif choice == "8":
            demo_kpi_generator()
        elif choice == "9":
            run_all_tools()
        elif choice == "0":
            print("\n👋 Thanks for trying MissionControlMCP!")
            print("🚀 Check out the docs for more: README.md")
            break
        else:
            print("\n❌ Invalid choice! Please enter 0-9")
        
        # Ask if user wants to continue
        if choice != "9":  # Don't ask after running all tools
            print("\n" + "─"*80)
            continue_choice = input("Return to menu? (y/n): ").strip().lower()
            if continue_choice != 'y':
                print("\n👋 Thanks for trying MissionControlMCP!")
                break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Demo interrupted. See you next time!")
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
