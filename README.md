Author: Niko Hienonen
Mailto: niko.hienonen@tuni.fi
Version: 1.1
Date: 2019/5/29

A simple demo REST-api made with Django that shows and allows the modification of a list of 
volleyball players. Just to note, the app is still in development-mode, so it is not deployed,
has its secret-key still intact and is not in that way optimized in security.

Stack: Django
DB: Heroku-postgresql

To use the api, follow the simple steps below. (Python needs to be installed.)

1. Download the zip or fork the repo
2. Navigate to $ root/
3. Run $ python manage.py runserver
4. The expected outcome is something similar to below, if not, contact the author
  ```
  System check identified no issues (0 silenced).
  May 29, 2019 - 11:53:43
  Django version 2.2.1, using settings 'api.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CTRL-BREAK.
  ```
5. After seeing the above, choose your method of making http-requests to the api and fire away
  (The author personally uses Postman for testing http: https://www.getpostman.com/)
6. Please contact me if you have any trouble or feedback about the app!

Thank you for reading!
Niko Hienonen
