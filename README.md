# Zoo Food Service

This is the **Food API** for managing food-related data in the zoo management system. Built with **FastAPI**, it handles operations such as food records, storage unit records, food location units allowed, and which foods certain animals can eat. It is part of a larger microservices-based architecture for zoo management.

---

## Features

- CRUD operations for food.
- Management of storage units, and food location units, and which food animals can eat.
- Integration with a relational database (e.g., PostgreSQL).
- Role-based access control (RBAC) with JWT authentication.
- API documentation via Swagger UI and ReDoc.

---

## Requirements

Make sure you have the following installed:
- Python 3.13.1
- poetry (Python package manager)

---

## Installation

1. Clone the repository:
  ```bash
  git clone https://github.com/derekgygax/zoo-food-service.git
  cd zoo-animals-service
  ```

2. Install Dependencies
Make sure you have **Poetry** installed:
  ```sh
  poetry install
  ```

3. Set up environment variables:
  - Create a `.env` file in the root directory with the necessary configuration.
    Example:
    ```
    DATABASE_URL=postgresql://user:password@localhost:5432/zoo_food
    AUTH_SECRET=your_secret_key
    AUTH_ALGORITHM=your_algorithm
    ```

---

## Running the API

1. Start the development server:
   ```bash
   poetry run uvicorn app.main:app --reload --port 8101
   ```


2. Access the API documentation:
  - Swagger UI: [http://127.0.0.1:8101/docs](http://127.0.0.1:8101/docs)
  - ReDoc: [http://127.0.0.1:8101/redoc](http://127.0.0.1:8101/redoc)

---

## Project Structure

```
zoo-food-service/
├── app/
│   ├── models/        # Database models
│   ├── routers/        # API routes
│   ├── schemas/       # Pydantic schemas
│   ├── services/      # Business logic
│   ├── __init__.py    # Package initialization
├── main.py            # Entry point of the application
├── requirements.txt   # Dependency file
├── .env               # Environment variables
├── README.md          # Project documentation
```

---

## Testing

Run tests using your preferred testing framework (e.g., `pytest`):
```bash
poetry run pytest
```

---

## Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request for review.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Repository

The repository for this project is hosted at: [https://github.com/derekgygax/zoo-food-service.git](https://github.com/derekgygax/zoo-food-service.git)
```