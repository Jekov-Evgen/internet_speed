import speedtest

def get_data_internet():
    st = speedtest.Speedtest()
    st.get_best_server()
    download = st.download() / 1000000
    upload = st.upload() / 1000000
    ping = st.results.ping
    
    return [round(download, 2), round(upload, 2), round(ping, 2)]