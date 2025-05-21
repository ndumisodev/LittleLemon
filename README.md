# LittleLemon Restaurant API

This is the backend API for the LittleLemon Restaurant application, built with Django and Django REST Framework (DRF).

## Setup & Running the Project

1.  **Clone the repository:**
    ```bash
    git clone [your_repository_url_here]
    cd littlelemon
    ```
2.  **Install Pipenv (if you don't have it):**
    ```bash
    pip install pipenv
    ```
3.  **Install dependencies and create/activate the virtual environment using Pipenv:**
    ```bash
    pipenv install
    pipenv shell
    ```
    *This command reads your `Pipfile` and `Pipfile.lock` to install the correct dependencies and then activates the project's virtual environment.*

4.  **Database Migrations:**
    ```bash
    python manage.py makemigrations restaurant
    python manage.py migrate
    ```
5.  **Create a Superuser (if you don't have one):**
    ```bash
    python manage.py createsuperuser
    ```
6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The API will be available at `http://127.0.0.1:8000/`.

---

## API Endpoints for Testing

Here are the key API endpoints you can test using tools like **Insomnia**, **Postman**, or `curl`.

### 1. User Management & Authentication

#### Create a New User

* **Endpoint:** `/auth/users/`
* **Method:** `POST`
* **Authentication:** Not required.
* **Body (JSON):**
    ```json
    {
        "username": "newuser",
        "password": "strongpassword123",
        "email": "newuser@example.com"
    }
    ```
* **Response:** The details of the newly created user (often including `id`, `username`, `email`).

#### Obtain Authentication Token (Login)

You have two options to obtain an authentication token:

**Option 1: Using Django REST Framework's `authtoken` view**

* **Endpoint:** `/api-token-auth/`
* **Method:** `POST`
* **Body (JSON):**
    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```
* **Response:** A JSON object containing the authentication `token`.
    ```json
    {
        "token": "your_generated_token_string"
    }
    ```

**Option 2: Using Djoser's login view**

* **Endpoint:** `/auth/token/login/`
* **Method:** `POST`
* **Body (JSON):**
    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```
* **Response:** A JSON object containing the authentication `auth_token`.
    ```json
    {
        "auth_token": "your_generated_token_string"
    }
    ```
    *Note the key name `auth_token` instead of `token`.*

* **Important Note for both options:** Use the obtained token in the `Authorization: Bearer <token>` header for all subsequent authenticated requests. In Insomnia, navigate to the **Auth tab**, select **Bearer Token**, and paste the token string (e.g., `your_generated_token_string`).

---

### 2. Menu API (`restaurant/menu/`)

This API allows CRUD operations on menu items. It does **not** require authentication by default.

#### Get All Menu Items (READ)

* **Endpoint:** `/restaurant/menu/`
* **Method:** `GET`
* **Authentication:** Not required.
* **Response:** List of menu items.

#### Create a New Menu Item (CREATE)

* **Endpoint:** `/restaurant/menu/`
* **Method:** `POST`
* **Authentication:** Not required.
* **Body (JSON):**
    ```json
    {
        "title": "New Dish Name",
        "price": 15.99,
        "inventory": 50
    }
    ```
* **Response:** The created menu item with its ID.

#### Get a Single Menu Item (READ)

* **Endpoint:** `/restaurant/menu/{id}/` (e.g., `/restaurant/menu/1/`)
* **Method:** `GET`
* **Authentication:** Not required.
* **Response:** Details of the specific menu item.

#### Update a Menu Item (UPDATE)

* **Endpoint:** `/restaurant/menu/{id}/`
* **Method:** `PUT`
* **Authentication:** Not required.
* **Body (JSON - send all fields):**
    ```json
    {
        "title": "Updated Dish Name",
        "price": 18.50,
        "inventory": 40
    }
    ```
* **Response:** The updated menu item.

#### Delete a Menu Item (DELETE)

* **Endpoint:** `/restaurant/menu/{id}/`
* **Method:** `DELETE`
* **Authentication:** Not required.
* **Response:** `204 No Content` on success.

---

### 3. Booking API (`restaurant/booking/tables/`)

This API allows CRUD operations on table bookings. It **requires authentication**.

#### Get All Bookings (READ)

* **Endpoint:** `/restaurant/booking/tables/`
* **Method:** `GET`
* **Authentication:** **REQUIRED** (use `Bearer Token` from `/api-token-auth/`).
* **Response:** List of booking entries.

#### Create a New Booking (CREATE)

* **Endpoint:** `/restaurant/booking/tables/`
* **Method:** `POST`
* **Authentication:** **REQUIRED**.
* **Body (JSON):**
    ```json
    {
        "name": "Customer Name",
        "no_of_guests": 4,
        "booking_date": "YYYY-MM-DDTHH:MM:SSZ"
    }
    ```
    (Example `booking_date`: "2025-05-25T19:00:00Z")
* **Response:** The created booking entry.

#### Get a Single Booking (READ)

* **Endpoint:** `/restaurant/booking/tables/{id}/`
* **Method:** `GET`
* **Authentication:** **REQUIRED**.
* **Response:** Details of the specific booking.

#### Update a Booking (UPDATE)

* **Endpoint:** `/restaurant/booking/tables/{id}/`
* **Method:** `PUT`
* **Authentication:** **REQUIRED**.
* **Body (JSON - send all fields):**
    ```json
    {
        "name": "Updated Customer Name",
        "no_of_guests": 6,
        "booking_date": "YYYY-MM-DDTHH:MM:SSZ"
    }
    ```
* **Response:** The updated booking entry.

#### Delete a Booking (DELETE)

* **Endpoint:** `/restaurant/booking/tables/{id}/`
* **Method:** `DELETE`
* **Authentication:** **REQUIRED**.
* **Response:** `204 No Content` on success.

---
This `README.md` provides a clear guide for anyone looking to test your API! Make sure to replace `[your_repository_url_here]` with the actual URL of your Git repository.