import requests
import webbrowser

while True:
    breed = input("Enter a breed of dog (ex: boxer) or enter 1 to end program: ").lower()
    if breed == '1':
        print("Thank you, goodbye.")
        break

    api_url = f"https://dog.ceo/api/breed/{breed}/images/random"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            image_url = data['message']
            print(f"Here is a picture of a {breed}:")
            webbrowser.open_new_tab(image_url)
        else:
            print(f"Couldn't find a picture for the breed: {breed}")
    else:
        print("Error fetching data from the API. Please try again.")
        

