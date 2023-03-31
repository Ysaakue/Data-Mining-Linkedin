# Requirements
 - Python3
 - [linkedin-api python module](https://github.com/tomquirk/linkedin-api)

# Getting Started
First you will need to create a folder `.local` and file `credentials.json` inside that folder:
```
.
├── .local
│   └── credentials.json
└── linkedin_data_mining.py
```
In `credentials.json` write your linkedin credentials as below:
```
{
  "username": "your_username",
  "password": "your_password"
}
```
In `linkedin_data_mining.py` you can change the `search_profiles` list with a list of public ids of profiles that you want to get posts of. You can get the public id from the link of the profile user page.
```text
 __________________________ _____________
|         base path        |  public id  |
https://www.linkedin.com/in/isaac-geraldo/
```
After fill the list of profiles public ids you can run `linkedin_data_mining.py` and use your output.