# TRACKMEDAPP

Track me is a Django REST API that allows users to track their to-do lists. It has the following features:

  - CRUD functions for task entity
  - Marking task as completed
  - Single page application
  - Rest framework

# Technical Stack
  - Python 3.6
  - Django 2.2.2
  - Postges
  - HTML 5
  - CSS 3
  - heroku

# Set-up

  - Install Python 3.6

  * Then, Git clone this repo to your PC

  ```bash
    $ git clone https://github.com/EnockOMONDI/TRACK-ME
  ```

  ```bash
  $ pip install virtualenv
   ```

  - Install Django with command: `pip install Django`
  - Open the project in an IDE (visual studio recommended here)
  - There should be some data available in the database since I have uploaded my DB. If you would like to use your own data,
    please read the next step
  - Set up database:
       - Run command: `python3 manage.py makemigrations`
       - Run command: `python3 manage.py migrate` 
  - "Edit Configurations"
  - Runserver
  - Check the port that the server is running on, normally it is 8000
  - Open the browser and enter `127.0.0.1:8000`
  - Enjoy!


# APIs
| URL | Method | Response (JSON format) |
| ------ | ------ | ------ |
| /api/v1/items | GET | Get all task in the database |
| /api/v1/items | POST | Create a new task |
| /api/v1/items/:id | PUT | Edit an existing task |
| /api/v1/items/:id | DELETE | Delete an task |

# Test
Alternatively, you can test APIs through [Postman](https://www.getpostman.com/), 

# Tips
  - Title length should be 1-50 characters
  - Description length should be 1-500 characters
  - While inputing dates, please follow the parttern "yyyy-MM-dd" (will improve later!)
  - Start date should be ealier than the end date 
  - Start date should be today or later
  - Since the end date is the estimated date, it is allowed that items is not completed even after the end date. In this circumstance, the font color of the end date will turn red and be appended with "(Over Due)"
  - All items, completed items or not complted items can be shown respectively according to user selection
  - The background color of the "status" cells of completed items will turn green, otherwise it will be red

# To Be Improved
  - UI enhancement (e.g. calendar)
  - User registration and permissions
  - Write test cases

