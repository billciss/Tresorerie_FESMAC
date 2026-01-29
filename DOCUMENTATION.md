# Treasury Management Application Documentation

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/billciss/Tresorerie_FESMAC.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Tresorerie_FESMAC
   ```

3. **Install dependencies:**
   ```bash
   npm install
   # or
   pip install -r requirements.txt
   ```

## Configuration

- **Environment Variables:**
  - Create a `.env` file in the root of the project and set the following variables:
    ```
    DATABASE_URL=your_database_url
    SECRET_KEY=your_secret_key
    ```

- **Example configuration:**
  ```
  DATABASE_URL=postgres://user:password@localhost:5432/dbname
  SECRET_KEY=mysecretkey
  ```

## Usage

- **Starting the Application:**
  ```bash
  npm start
  # or
  python app.py
  ```

- **Access the Application:**
  - Open your browser and navigate to `http://localhost:3000`

## API Endpoints

### 1. Authentication
- **Login**
  - **Endpoint:** `/api/auth/login`
  - **Method:** POST
  - **Request Body:**
    ```json
    {
      "username": "string",
      "password": "string"
    }
    ```

### 2. Treasuries
- **Get All Treasuries**
  - **Endpoint:** `/api/treasuries`
  - **Method:** GET

- **Create Treasury**
  - **Endpoint:** `/api/treasuries`
  - **Method:** POST
  - **Request Body:**
    ```json
    {
      "name": "string",
      "amount": number
    }
    ```

### 3. Transactions
- **Get All Transactions**
  - **Endpoint:** `/api/transactions`
  - **Method:** GET

- **Create Transaction**
  - **Endpoint:** `/api/transactions`
  - **Method:** POST
  - **Request Body:**
    ```json
    {
      "treasury_id": "string",
      "amount": number,
      "type": "income|expense"
    }
    ```
