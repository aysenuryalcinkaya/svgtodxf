import requests
import json

# set the input and output formats
input_format = "svg"
output_format = "dxf"

# set the input file name and path
input_file = "new.svg"
input_path = r"C:\Users\ASUS\Desktop\me, myself and I\svgtodxf\new.svg"


# set the output file name and path
output_file = "new.dxf"
output_path =  r"C:\Users\ASUS\Desktop\me, myself and I\svgtodxf\new.dxf"

# create the request payload
payload = {
    "input_format": input_format,
    "output_format": output_format,
    "file": input_file
}

# send the request to the API endpoint
response = requests.post("https://vectorexpress.io/api/v2/convert", data=payload, files={"file": open(input_path, "rb")})

# check the status code of the response
if response.status_code == 200:
    # get the response data as JSON
    data = response.json()

    # get the download URL of the output file
    download_url = data["download_url"]

    # download the output file and save it to the output path
    output_response = requests.get(download_url)
    with open(output_path, "wb") as f:
        f.write(output_response.content)

    # print a success message
    print(f"Successfully converted {input_file} to {output_file}")
else:
    # print an error message
    print(f"An error occurred: {response.text}")
