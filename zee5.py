
import time
import requests
import json
import streamlit as st
import time
import requests
css = """
<style>
.gradient-text {
display: flex;
    justify-content: center;
    align-items: center;
    height: 36px; /* Adjust height as needed */
    background: linear-gradient(to right, #00c6ff, #0072ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 36px;
    font-weight: bold;
    padding: 20px;
    padding-top:0px;
    margin:0px;
    padding-bottom: 0px;
    border-radius: 10px;

}
.gradient-button {
    background: linear-gradient(to right, #00c6ff, #0072ff);
    color: white;
    border: none;
    padding: 10px 20px;
    font-size: 18px;
    font-weight: bold;
    border-radius: 5px;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.gradient-button:hover {
    opacity: 0.9;
    transform: translateY(-1px);
    box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
}
</style>
"""
def serverrequest(data):


    url = "https://oms-co.zee5.com/order-bff/v3/promotions?coupon_code="+data+"&country_code=IN"

    payload = {}
    files = {}
    headers = {
        'Authorization': 'bearer eyJraWQiOiJlNmxfbGYweHpwYVk4VzBNcFQzWlBzN2hyOEZ4Y0trbDhDV0JaekVKT2lBIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI4ODEwQTY2MC0wQjcwLTQ4QUMtOTVFNy1ERjEzMTQ3ODNDMkQiLCJkZXZpY2VfaWQiOiIyMjc0MDRiMy0xYTQ1LTRhMjAtOGVhNC1jNDMzOTdhMTFlZWQiLCJhbXIiOlsiZGVsZWdhdGlvbiJdLCJpc3MiOiJodHRwczovL3VzZXJhcGkuemVlNS5jb20iLCJ2ZXJzaW9uIjo2LCJjbGllbnRfaWQiOiJyZWZyZXNoX3Rva2VuIiwiYXVkIjpbInVzZXJhcGkiLCJzdWJzY3JpcHRpb25hcGkiLCJwcm9maWxlYXBpIiwiZ2FtZS1wbGF5Il0sInVzZXJfdHlwZSI6IlJlZ2lzdGVyZWQiLCJuYmYiOjE3MTg3ODg4ODEsInVzZXJfaWQiOiI4ODEwYTY2MC0wYjcwLTQ4YWMtOTVlNy1kZjEzMTQ3ODNjMmQiLCJzY29wZSI6WyJ1c2VyYXBpIiwic3Vic2NyaXB0aW9uYXBpIiwicHJvZmlsZWFwaSJdLCJzZXNzaW9uX3R5cGUiOiJHRU5FUkFMIiwiZXhwIjoxNzIxNDE4ODgxLCJpYXQiOjE3MTg3ODg4ODEsImp0aSI6IjgzM2EyNWU4LWQ4YWMtNDFjMy05NDM4LTBhZjk5MzFhM2Q3MiJ9.qLpJ1fgUa9P-tAnzyhoBo-XUBqvBahIya5XsfjBIFzrHMjt8sNTKzcdFXwzetx_cJvwxHEe_RjFL2db6dk9QhuMnwpQaFYiy3-Pim_qM1MC340gK89b3oXBvfBBm3B3tvfubfPW9fk0uFPnREG9vvHIIoi6WRUAfY-tkQQoQkpvmh8WKmWUfyKOdlNKL6rAooyfilQWPWb0RAXKzlpfsQC6KhjWSBIczKTdIKhjpei2FoRzxTJw9NZD3tXgsaNfMLn9QNGieIVN3haAboAH7LnYvpTRQ13cU8Ne8ejyYacuGRYzCTfd8DFY10-iobpmVkSumhqWsxtaoSrWf7VL2fQ',
        'X-Access-Token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwbGF0Zm9ybV9jb2RlIjoiV2ViQCQhdDM4NzEyIiwiaXNzdWVkQXQiOiIyMDI0LTA2LTE5VDA1OjA2OjEzLjQ5MVoiLCJwcm9kdWN0X2NvZGUiOiJ6ZWU1QDk3NSIsInR0bCI6ODY0MDAwMDAsImlhdCI6MTcxODc3MzU3M30.Ctk4CuU6Noqw3bOtARBtf45rI2JXXkrol-3Z7raksUg'
    }

    response = requests.request("GET", url, headers=headers, data=payload, files=files)

    print(response.text)

    return response.text



def checkcode(codes_array):
    check_response=[]
    for code in codes_array:
        time.sleep(1)
        response=json.loads(serverrequest(code))
        message=response["message"]
        check_response.append(message)
    return check_response
st.markdown("""
<style>
          h1{  text-align: center;
            color: #fff;
            /* Change the color to white to match the gradient */
            margin: auto
            margin-top: 20px;
            margin-bottom: 20px;
            font-weight: bold;
            text-transform: capitalize;
            /* Add animation styles */
            background-image: linear-gradient(-225deg, #231557 0%, #44107a 29%, #ff1361 67%, #fff800 100%);
            background-size: auto auto;
            background-clip: border-box;
            background-size: 200% auto;
            
            background-clip: text;
            -webkit-background-clip: text;
            text-fill-color: transparent;
            -webkit-text-fill-color: transparent;
            animation: textclip 2s linear infinite;
            text-transform: uppercase;
            font-size: 20px;
            margin :0px;
            padding-bottom :0px
            }
            </style>

            """,unsafe_allow_html=True)
# Display the styled heading
st.markdown(css, unsafe_allow_html=True)
st.markdown('<p class="gradient-text">OTT CONNECT</p>', unsafe_allow_html=True)

st.markdown("<h1> ZEE5 CHECKER </h1>", unsafe_allow_html=True)
st.markdown(css, unsafe_allow_html=True)


codes_txt = st.text_area("",height=180)

st.markdown(css, unsafe_allow_html=True)
if st.button('Submit', key='submit_button', help='Click to submit', on_click=None):
   codes_array = codes_txt.splitlines()
   print(codes_array)
   data =checkcode(codes_array)
   i=0
   for code in data:

       if code == "Coupon code applied successfully":
           st.markdown(
               '<p style="background-color: green; color:white;padding: 10px; border-radius: 5px;">'+codes_array[i]+"                        "+code+'</p>',
               unsafe_allow_html=True)
       else:
           st.markdown(
               '<p style="background-color: red; padding: 10px;color:white; border-radius: 5px;">' + codes_array[
                   i] + "                        " + code + '</p>',
               unsafe_allow_html=True)

       i+=1