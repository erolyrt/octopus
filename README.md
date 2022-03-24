# Octopus Energy
OE Technical Challenge Project

Python based script to detect the related flow reference D0010

#### Dependencies

Python version 3.6 or later.

All other libraries are listed in `requirements.txt` file which could be used by `pip` to be installed:

```bash
pip install -r requirements.txt
```

#### How to work with script

To visualize the related flows, following steps need to be performed:
1) Run the ```python manage.py makemigrations``` and ```python manage.py migrate``` on your local machine to create the tables
2) Choose the csv file which is exported oln the Electralink website 
3) Push the confirm button and the list of products will be viewed
4) Click on D0010 link to review the products related to D0010
