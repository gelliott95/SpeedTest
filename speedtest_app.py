import streamlit as st
import speedtest

def run_speed_test():
    st.info("Running the speed test... This may take a few seconds.")
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        ping = st.results.ping
        
        st.success("Speed Test Completed!")
        st.metric("Download Speed", f"{download_speed:.2f} Mbps")
        st.metric("Upload Speed", f"{upload_speed:.2f} Mbps")
        st.metric("Ping", f"{ping:.2f} ms")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Streamlit App UI
st.title("Internet Speed Test")
st.write("This app tests your internet download and upload speeds.")

if st.button("Run Speed Test"):
    run_speed_test()
