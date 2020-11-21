# ENCODE DECODE APP
**It's a web-app which encrypts and decrypts the message**\
\
You can view its live demo [here](http://encode-decode-app.herokuapp.com/)


## About the project
This was my very first web app with Django. I have converted a script to a web app.\
It is a text-encoding and decoding app. 
I have written my algorithm which converts text to encrypted text and the encrypted text to readable text.

**How does my algorithm work?** \
My algorithm assigns 4 random integers which randomly add even and odd characters to the string. The first two number decides how many numbers to add and last two number decided the range of the string.


**Top Features of my App:**
- My algorithm can convert one string to many encrypted strings.
- It does not require DB.


## Installation
*After cloning the repo*\
\
Install all the dependencies.

```bash
pip3 install -r requirements.txt
```
> Note: You will need to generate a SECRET KEY and then past it [here](https://github.com/Riken-Shah/Encode-Decode-App/blob/master/mysite/settings.py)

Run the project locally
```bash
python3 manage.py runserver
```


## Contributing
Pull requests are welcome. \
If you have any ideas or suggestions or issues please **open an issue** first to discuss.
