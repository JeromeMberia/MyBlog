# MyBlog

Its an application that allows you as the user can comment and post in MyBlog.

#### By [Jerome Mberia](https://github.com/JeromeMberia)

## [LINK TO SITE](https://my--blog2.herokuapp.com/)

## Description

As user you

## Installation

On linux:

#### If you dont python in your computer

* Install  python
  
    ```

    $ sudo add-apt-repository ppa:jonathonf/python-3.8
    $ sudo apt-get update
    $ sudo apt-get install python3.8
    ```

* Confirm Installation

    ```

    $ python3

    Python 3.8.2 (default, Apr 27 2020, 15:53:34)
    [GCC 9.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```

* To exit the interface type *exit()* in interface

    ```

    jerome@jerome-HP-EliteBook-840-G3:~$ python3
    Python 3.8.2 (default, Apr 27 2020, 15:53:34) 
    [GCC 9.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>exit()
    ```

* Install  python

    ```

    $ sudo apt-get install python3-pip
    ```

#### If you do have python in your computer

* Clone this repository

    ```

    $ git clone https://github.com/JeromeMberia/MyBlog.git
    ```

* Creating a virtual environment

    ```

    $ sudo apt-get install python3-venv
    $ python3 -m venv virtual
    ```

* Activating the virtual environment

    ```

    $ . virtual/bin/activate
    ```

To install all dependencies

    ```

    (virtual)$ pip install -r requirements.txt
    ```

## SetUp

* Create a file named start.sh
  
* In that file type the code below:

    ```

    export SECRET_KEY=<the secret key thing of it like your password for this application >
    export MAIL_USERNAME=<the senders email >
    export EMAIL_PASS=<the password for MAIL_USERNAME >

    python3.8 manage.py server
    ```

* Then you go to your terminal and type this to run this application

    ```

    $ chmod a+x start.py
    $ ./start.py
    ```

## Known Bugs

* I removed the comment funtion.
* Disable on the request function for the quotes.

## Technologies Used

* HTML & CSS
* Bootstrap-4
* Python
* Flask

## Support and contact details

For ways on how to improve the app contact me via jeromemberia@gmail.com.

### License

[MIT Licence](https://github.com/JeromeMberia/MyBlog/blob/master/LICENSE)

Copyright (c) 2020 [Jerome Mberia](https://github.com/JeromeMberia)
