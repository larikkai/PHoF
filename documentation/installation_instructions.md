# Padel Hall of Fame - Installation instructions 

The instructions assume git is installed. If git is not installed, follow the installation instructions at:

https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

## Installing the application on your own machine

### Git clone with ssh

Open commandline, make directory where you want to clone repository by typing mkdir < directory name >

```
$ mkdir example
 ```

Move into created directry by typing cd < directory name >
```
$ cd example
```
On GitHub, navigate to the main page of the repository.
Under repository name, click __Clone or download__. Copy ssh-key from dropdown menu:

![alt text](https://raw.githubusercontent.com/larikkai/PHoF/master/documentation/git_clone.PNG "navbarinfo")

Run following command to clone repository to directory by typing git clone and paste url you copied.
```
$ git clone git@github.com:larikkai/PHoF.git
```
Your local clone will be created.
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `Spoon-Knife`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

### Download repository
On GitHub, navigate to the main page of the repository.
Under repository name, click __Clone or download__. From dropdown menu click __Download ZIP__.

![alt text](https://raw.githubusercontent.com/larikkai/PHoF/master/documentation/git_clone.PNG "navbarinfo")

Extract the downloaded file to the directory of your choice.

## Running the app locally

1. Requirements
     * Git
     * Pyhon - versio 3.5 or higher
     * Python pip
     * Sqlite3

2. Python virtual environment

   More details at https://docs.python.org/3/tutorial/venv.html

    __On Unix or MacOS__

    Install virtual enviroment by runnin command python3 -m venv venv
    ```
    $ python3 -m venv venv 
    ```
    Activate virtual enviroment, run: source venv/bin/activate
    ```
    $ source tutorial-env/bin/activate
    ```
    _Sign of activate virtual enviroment (venv)_
    __On Windows__

    Install virtual enviroment by runnin command python3 -m venv venv
    ```
    C:\Users\user\example\PHoF> python3 -m venv venv 
    ```
    Activate virtual enviroment, run: venv\Scripts\activate.bat
    ```
    C:\Users\user\example\PHoF venv\Scripts\activate.bat
    ```

    _Sign of activate virtual enviroment (venv)_


3. Applying for dependencies
   
    Upgrade pip, run command pip install --upgrrade pip
    ```
    $ pip install --upgrade pip
    ```
    Install Flask, run command pip install Flask
    ```
    $ pip install Flask
    ```
    Download dependecies, run command pip install -r requirements.txt
    ```
    $ pip install -r requirements.txt
    ```

4. Starting app

   Run command python3 run.py to start app
    ```
    $ python3 run.py
    ```
    By default, the application starts at http://localhost:5000/ or http://127.0.0.1:5000/ 