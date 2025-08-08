The administrator credentials is
username: root
password: root

*******API URLs*******

to view static HTML content:
http://127.0.0.1:8000/api/

to register a new user:
[POST] http://127.0.0.1:8000/auth/users/

to generate a user Token:
[POST] http://127.0.0.1:8000/api/api-token-auth/

to view menu list:
[GET] http://127.0.0.1:8000/api/menu_item/

to add menu item (!!Auth Token Required!!):
[POST] http://127.0.0.1:8000/api/create_menu_item/

to get,edit,delete menu item (!!Auth Token Required!!):
[POST] http://127.0.0.1:8000/api/menu_item/{Item_id}

to view booking list (!!Auth Token Required!!):
[GET] http://127.0.0.1:8000/api/booking/

to get,edit,delete booking (!!Auth Token Required!!):
[POST] http://127.0.0.1:8000/api/booking/{Book_id}

to add new booking:
[POST] http://127.0.0.1:8000/api/create_booking/ 