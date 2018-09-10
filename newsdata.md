# Log Analysis

Building an informative summary from logs is a real task that comes up very often in software engineering. This program collects logs to help us measure the most popular articles and authors and percent of error requests. We use SQL query to calculate the results from the database.

This documentation tells you how to run this news data log analysis application.
Before downloading, make sure you have installed python2 in your computer. If not, please download from this site: https://www.python.org/downloads/

## Step 1: Download
* Download the **newsdata.zip** file
* Extract all the files into a new foler called newsdata
* Download and installvirtual machine from this site: https://www.virtualbox.org/
* Download and install vagrant from this site: https://www.vagrantup.com/downloads.html

## Step 2: Run the virtual box
* Open the terminal and use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm
* Go the vagrant directory
* Run the **vagrant up** and this will take a while
* Then run the **vagrant ssh** and you will see this:
```
vagrant@vagrant:~$
```
## Step 3: Run the python program
* Make sure you put the newsdata folder into the vagrant folder
* On the vagrant virtual box run **cd /vagrant** to access the shared files
* Then cd into the newsdata folder
* Then run the newsdata.py file
```
python newsdata.py
```
You will see a newsdata.txt file in the newsdata folder. That's all. You can see the analysis result of the news!
