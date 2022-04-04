# Secretary: A web app Password Manager

<img src="./images/icon.png" alt="icon">

*my something-awesome-project for COMP6441*

## Ideas

- A simple password manager python script is not enough for me
- But I haven't completely learned html and css yet
- So I searched some open sources projects and found the most suitable one that inspired me: https://www.youtube.com/watch?v=z87LjWauDvI

## Changes I made

- Improve the algorithm and methods for the password security
  
  - Implemented the **RSA algorithm** in the **rsa.py** inside the **secretary** folder and
    - import them to the backend, <img src="./images/import.png" alt="">
    - encrypt the passwrod and email, <img src="./images/encrypt.png" alt="">
    - decrypt them when saving them into the DataBase, <img src="./images/decrypt.png" alt="">
    - succeed output: <img src="./images/succeed_output.png" alt="">

- Wrote automation tests to test the api of the password manager

- For the frontend:
  
  - Use my own design for the UI
  - Update the main.js to fix bugs that:
    - When switching modals from one to another, the modal that was open before is not closed:
    - <img title="" src="./images/bug1.png" alt="logo" width="237">

## What to achieve:

- [ ] A web app password manager that can be used on any device
  
  - Implemented by the deployment on a server

- [ ] People are able to interact with it through the ui
  
  - Implemented in frontend

- [ ] The password manager should be secure
  
  - Implemented in the backend
  - Improved the algorithm and methods for the password security

- [ ] The web app should has following functions:
  
  - [x] Login
    - [x] Return msg when username or password is incorrect
    - [x] Use OTP (HOST is outlook) to send confirmation email
      - [x] Return msg when verifitation failed
      - [x] Return msg when verification succeeded
  - [x] Register
    - [x] Return msg when duplicated username
    - [x] Return msg when passwords do not match
    - [x] Return msg when duplicated email
    - [x] Welome msg when register successfully
  - [x] Logout
    - [x] Return msg when loggout
  - [x] Add a new password
    - [ ] Use **RSA** algorithm to encrypt and decrypt the email and password
    - [ ] Return msg when Add password succeed
  - [ ] Delete a password
  - [ ] Update a password
  - [ ] View all passwords

## Requirements

See requirements.txt