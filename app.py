# Copyrights @ Muhammad Ahmad Sultan
# Text2Graph : Transforming Text into Insightful Knowledge Graphs

# Import necessary modules
import streamlit as st
import streamlit.components.v1 as components  # For embedding custom HTML
from generate_knowledge_graph import generate_knowledge_graph

# Set up Streamlit page configuration
st.set_page_config(
    page_title="Text2Graph - Knowledge Graph Generator",
    page_icon="🧠",
    layout="wide",  # Use wide layout for better graph display
    initial_sidebar_state="expanded",
    menu_items=None
)

# Custom CSS for styling
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    /* Main app styling */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    
    /* Header styling */
    .header-container {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem 0;
        margin: -1rem -1rem 2rem -1rem;
        border-radius: 0 0 20px 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .header-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 100" fill="rgba(255,255,255,0.1)"><polygon points="0,0 1000,0 1000,100 0,80"/></svg>');
        background-size: cover;
    }
    
    .header-content {
        position: relative;
        z-index: 1;
    }
    
    .app-title {
        font-family: 'Poppins', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        color: #ffffff;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    .app-tagline {
        font-family: 'Poppins', sans-serif;
        font-size: 1.2rem;
        font-weight: 300;
        color: #e8f4f8;
        margin-top: 0.5rem;
        opacity: 0.9;
    }
    
    @keyframes glow {
        from { text-shadow: 2px 2px 4px rgba(0,0,0,0.3), 0 0 10px rgba(255,255,255,0.2); }
        to { text-shadow: 2px 2px 4px rgba(0,0,0,0.3), 0 0 20px rgba(255,255,255,0.4); }
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #2c3e50 0%, #34495e 100%);
    }
    
    .css-1d391kg .css-1v0mbdj {
        background: linear-gradient(180deg, #2c3e50 0%, #34495e 100%);
    }
    
    /* Section headers */
    .section-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    /* Content containers */
    .content-container {
        background: rgba(255,255,255,0.95);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    
    /* Success message styling */
    .success-message {
        background: linear-gradient(135deg, #00b894 0%, #00cec9 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-family: 'Poppins', sans-serif;
        font-weight: 500;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    /* Footer styling */
    .footer {
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
        color: #bdc3c7;
        text-align: center;
        padding: 2rem;
        margin: 3rem -1rem -1rem -1rem;
        border-radius: 20px 20px 0 0;
        font-family: 'Poppins', sans-serif;
        font-size: 0.9rem;
        box-shadow: 0 -4px 20px rgba(0,0,0,0.1);
    }
    
    /* Icon styling */
    .icon {
        font-size: 1.5rem;
        margin-right: 0.5rem;
        vertical-align: middle;
    }
    
    /* Divider styling */
    .divider {
        height: 2px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        margin: 2rem 0;
        border-radius: 1px;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
<div class="header-container">
    <div class="header-content">
        <h1 class="app-title">🧠 Text2Graph</h1>
        <p class="app-tagline">Transforming Text into Insightful Knowledge Graphs</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Main content area
col1, col2 = st.columns([1, 2])

with col1:
    # Input Section
    st.markdown("""
    <div class="section-header">
        <span class="icon">✍️</span> Input Document
    </div>
    """, unsafe_allow_html=True)
    
    # Input method selection
    input_method = st.radio(
        "Choose an input method:",
        ["📄 Upload txt file", "✏️ Input text manually"],
        help="Select how you want to provide your text data"
    )
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    # Case 1: User chooses to upload a .txt file
    if input_method == "📄 Upload txt file":
        st.markdown("**📁 File Upload**")
        uploaded_file = st.file_uploader(
            label="Choose a .txt file",
            type=["txt"],
            help="Upload a text file to generate knowledge graph"
        )
        
        if uploaded_file is not None:
            # Read the uploaded file content and decode it as UTF-8 text
            text = uploaded_file.read().decode("utf-8")
            
            # Show file details
            st.success(f"✅ File uploaded: {uploaded_file.name}")
            st.info(f"📊 File size: {len(text)} characters")
            
            # Show preview of text
            with st.expander("👀 Preview uploaded text"):
                st.text_area("File content preview:", text[:500] + "..." if len(text) > 500 else text, height=100, disabled=True)
            
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
            
            # Button to generate the knowledge graph
            if st.button("🚀 Generate Knowledge Graph", key="upload_generate"):
                with st.spinner("⚙️ Generating knowledge graph..."):
                    # Call the function to generate the graph from the text
                    net = generate_knowledge_graph(text)
                    
                    # Save the graph to an HTML file
                    output_file = "knowledge_graph.html"
                    net.save_graph(output_file)
                    
                    st.session_state.graph_generated = True
                    st.session_state.output_file = output_file
    
    # Case 2: User chooses to directly input text
    else:
        st.markdown("**✏️ Manual Text Input**")
        text = st.text_area(
            "Enter your text here:",
            height=300,
            placeholder="Paste or type your text here to generate a knowledge graph...",
            help="Enter the text you want to convert into a knowledge graph"
        )
        
        if text:
            st.info(f"📊 Text length: {len(text)} characters")
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
            
            # Button to generate the knowledge graph
            if st.button("🚀 Generate Knowledge Graph", key="text_generate"):
                with st.spinner("⚙️ Generating knowledge graph..."):
                    # Call the function to generate the graph from the input text
                    net = generate_knowledge_graph(text)
                    
                    # Save the graph to an HTML file
                    output_file = "knowledge_graph.html"
                    net.save_graph(output_file)
                    
                    st.session_state.graph_generated = True
                    st.session_state.output_file = output_file

with col2:
    # Visualization Section
    st.markdown("""
    <div class="section-header">
        <span class="icon">📊</span> Knowledge Graph Visualization
    </div>
    """, unsafe_allow_html=True)
    
    # Check if graph has been generated
    if hasattr(st.session_state, 'graph_generated') and st.session_state.graph_generated:
        st.markdown("""
        <div class="success-message">
            🎉 Knowledge graph generated successfully!
        </div>
        """, unsafe_allow_html=True)
        
        # Display the graph
        try:
            HtmlFile = open(st.session_state.output_file, 'r', encoding='utf-8')
            components.html(HtmlFile.read(), height=1000, scrolling=True)
        except FileNotFoundError:
            st.error("❌ Graph file not found. Please regenerate the knowledge graph.")
    else:
        # Placeholder content when no graph is generated
        st.markdown("""
        <div class="content-container">
            <div style="text-align: center; padding: 3rem;">
                <h3 style="color: #666; font-family: 'Poppins', sans-serif;">🧠 Your Knowledge Graph Will Appear Here</h3>
                <p style="color: #888; font-family: 'Poppins', sans-serif; margin-top: 1rem;">
                    Upload a text file or enter text manually, then click "Generate Knowledge Graph" to visualize your data as an interactive network.
                </p>
                <div style="font-size: 4rem; margin: 2rem 0; opacity: 0.8;">🕸️</div>
                <p style="color: #666; font-size: 0.9rem; font-family: 'Poppins', sans-serif;">
                    <strong>Features:</strong><br>
                    🔍 Interactive node exploration<br>
                    🎨 Dynamic graph visualization<br>
                    📈 Entity relationship mapping
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>© 2025 | Developed by <strong>Muhammad Ahmad Sultan</strong></p>
    <p style="font-size: 0.8rem; margin-top: 0.5rem; opacity: 0.8;">
        Powered by Streamlit & NetworkX | 🧠 AI-Driven Knowledge Graph Generation
    </p>
</div>
""", unsafe_allow_html=True)