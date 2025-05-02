while True:
	try:
		pincode=input("Enter Pincode: ")
		url=f'https://api.postalpincode.in/pincode/{pincode}'
		import requests
		postoffice_list=[]
		response = requests.get(url)
		data=response.json()
		postoffice=data[0]['PostOffice']
		i=0
		for i in range(len(postoffice)):
			postoffice_list.append(postoffice[i]['Name'])

		postoffice_dict={
			"postoffice_names":postoffice_list,
			"postoffice_district":postoffice[0]['District'],
			"postoffice_state":postoffice[0]['State'],
		"postoffice_country":postoffice[0]['Country']
		}

		print(f"Post Office: {postoffice_dict["postoffice_names"]}\n")
		print(f"District: {postoffice_dict["postoffice_district"]}\n")
		print(f"State: {postoffice_dict["postoffice_state"]}\n")
		print(f"Country: {postoffice_dict["postoffice_country"]}\n")

	except (TypeError, KeyError):
		print("\nWrong Pincode! Please Try Again! :)\n")

	except KeyboardInterrupt:
		print("\nExiting the program...\n")
		exit()
