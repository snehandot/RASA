def crypto(currency):	
	import requests

	url = "https://e22d-35-237-183-232.ngrok-free.app"
	message=currency
	print("hi")

	response = requests.get(url, params={"message": message})

	if response.status_code == 200:
	    print("Request successful!")
	    print("Response content:")
	    print(response.text)
	else:
	    print("Request failed with status code:", response.status_code)
	return response.text
