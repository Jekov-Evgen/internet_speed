import speedtest

def get_data_internet():
    st = speedtest.Speedtest()
    download = st.download() / 1000000
    upload = st.upload() / 1000000
    ping = st.results.ping
    
    return [download, upload, ping]