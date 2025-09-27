import streamlit as st
import pickle
import numpy as np
import time

# Set page configuration
st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown('''
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
    }
    .prediction-card {
        background-color: #F5F7FA;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }
    .section-header {
        font-size: 1.2rem;
        color: #3949AB;
        margin-top: 15px;
        margin-bottom: 10px;
    }
    .stButton button {
        background-color: #1E88E5;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        margin-top: 20px;
    }
    .stButton button:hover {
        background-color: #1565C0;
    }
    .metric-card {
        background-color: #E3F2FD;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: bold;
        color: #0D47A1;
    }
    .metric-label {
        font-size: 0.9rem;
        color: #546E7A;
    }
    .feature-card {
        background-color: #F5F7FA;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 10px;
    }
    .feature-title {
        font-size: 1rem;
        color: #3949AB;
        margin-bottom: 5px;
    }
    .feature-value {
        font-size: 1.1rem;
        color: #37474F;
        font-weight: 500;
    }
</style>
''', unsafe_allow_html=True)

# Load the model and data
@st.cache_resource
def load_model():
    pipe_rand = pickle.load(open('pipe_rand.pkl', 'rb'))
    df = pickle.load(open('df.pkl', 'rb'))
    return pipe_rand, df

pipe_rand, df = load_model()

# Header section
st.markdown("<h1 class='main-header'>💻 Laptop Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #546E7A;'>Configure your ideal laptop and get an instant price estimate</p>", unsafe_allow_html=True)

# Create columns for layout
col1, col2 = st.columns([1, 1])

# Basic Information Section
with col1:
    st.markdown("<div class='section-header'>Basic Information</div>", unsafe_allow_html=True)
    company = st.selectbox('Brand', df['Company'].unique(), help="Select the laptop manufacturer")
    laptop_type = st.selectbox('Type', df['TypeName'].unique(), help="Choose the laptop category")
    weight = st.number_input('Weight (kg)', min_value=0.5, max_value=5.0, value=1.5, step=0.1, help="Enter the laptop weight in kilograms")

# Memory Section
with col2:
    st.markdown("<div class='section-header'>Memory & Storage</div>", unsafe_allow_html=True)
    ram = st.selectbox('RAM (GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64], help="Select RAM capacity")
    hdd = st.selectbox('HDD (GB)', [0, 128, 256, 512, 1024, 2048], help="Select HDD capacity (0 if no HDD)")
    ssd = st.selectbox('SSD (GB)', [0, 8, 128, 256, 512, 1024], help="Select SSD capacity (0 if no SSD)")

# Display Section
st.markdown("<div class='section-header'>Display Specifications</div>", unsafe_allow_html=True)
col3, col4, col5 = st.columns([1, 1, 1])

with col3:
    touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'], help="Does the laptop have a touchscreen?")
with col4:
    ips = st.selectbox('IPS Display', ['No', 'Yes'], help="Does the laptop have an IPS display?")
with col5:
    screen_size = st.slider('Screen Size (inches)', 10.0, 18.0, 13.0, step=0.1, help="Select the screen size")

resolution = st.selectbox('Screen Resolution', 
                         ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', 
                          '2880x1800', '2560x1600', '2560x1440', '2304x1440'],
                         help="Select the display resolution")

# Performance Section
st.markdown("<div class='section-header'>Performance Components</div>", unsafe_allow_html=True)
col6, col7 = st.columns([1, 1])

with col6:
    cpu = st.selectbox('CPU Brand', df['Cpu brand'].unique(), help="Select the processor brand")
with col7:
    gpu = st.selectbox('GPU Brand', df['Gpu brand'].unique(), help="Select the graphics card brand")

# Operating System Section
os = st.selectbox('Operating System', df['os'].unique(), help="Select the pre-installed operating system")

# Prediction button
st.markdown("---")
predict_button = st.button('Predict Price', help="Click to get the price prediction")

# Prediction logic
if predict_button:
    with st.spinner('Calculating price...'):
        # Process inputs
        touchscreen_val = 1 if touchscreen == 'Yes' else 0
        ips_val = 1 if ips == 'Yes' else 0
        
        # Extract X_res and Y_res from resolution
        X_res = int(resolution.split('x')[0])
        Y_res = int(resolution.split('x')[1])
        
        # Calculate PPI
        ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size
        
        # Create the query array with all 15 features
        query = np.array([company, laptop_type, screen_size, ram, weight, touchscreen_val, ips_val, 
                          X_res, Y_res, ppi, cpu, hdd, ssd, gpu, os])
        
        # Reshape the array
        query = query.reshape(1, 15)
        
        # Make the prediction
        predicted_price = int(np.exp(pipe_rand.predict(query)[0]))
        
        # Display results
        st.markdown("<div class='prediction-card'>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #1E88E5;'>Price Prediction</h3>", unsafe_allow_html=True)
        
        # Create metrics
        col8, col9, col10 = st.columns([1, 1, 1])
        
        with col8:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-value">₹{:,}</div>
                <div class="metric-label">Estimated Price</div>
            </div>
            """.format(predicted_price), unsafe_allow_html=True)
        
        with col9:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-value">{:.1f}"</div>
                <div class="metric-label">Screen Size</div>
            </div>
            """.format(screen_size), unsafe_allow_html=True)
        
        with col10:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-value">{} GB</div>
                <div class="metric-label">RAM</div>
            </div>
            """.format(ram), unsafe_allow_html=True)
        
        # Configuration Summary
        st.markdown("<h4 style='color: #3949AB; margin-top: 20px;'>Configuration Summary</h4>", unsafe_allow_html=True)
        
        # Create feature cards
        features = [
            ("Brand", company),
            ("Type", laptop_type),
            ("CPU", cpu),
            ("GPU", gpu),
            ("Storage", f"SSD: {ssd}GB, HDD: {hdd}GB"),
            ("Display", f"{screen_size}\" {resolution} {'Touchscreen' if touchscreen_val else ''} {'IPS' if ips_val else ''}"),
            ("OS", os),
            ("Weight", f"{weight} kg")
        ]
        
        # Create two columns for features
        col11, col12 = st.columns([1, 1])
        
        with col11:
            for title, value in features[:4]:
                st.markdown(f"""
                <div class="feature-card">
                    <div class="feature-title">{title}</div>
                    <div class="feature-value">{value}</div>
                </div>
                """, unsafe_allow_html=True)
        
        with col12:
            for title, value in features[4:]:
                st.markdown(f"""
                <div class="feature-card">
                    <div class="feature-title">{title}</div>
                    <div class="feature-value">{value}</div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Add a success message
        st.success("Prediction completed successfully!")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #78909C;'>Made with ❤️ using Streamlit | Laptop Price Predictor</p>", unsafe_allow_html=True) 
