
Question 1: HTTP Methods and Python Requests
Difference Between GET and POST Requests
 * GET Request: Designed to retrieve or fetch data from a specified resource on a server. It is safe and idempotent, meaning making multiple identical requests leaves the server state unchanged. Parameters are appended directly to the URL string in query parameters (e.g., [https://example.com/api?id=1](https://example.com/api?id=1)), making them visible in the browser URL bar and context history, and subject to URL length limitations.
 * POST Request: Designed to send data to a server to create or update a resource (e.g., submitting a form, uploading a file). It is non-idempotent, as repeating the request can result in side effects like creating duplicate entries. Parameters and payload data are enclosed in the body of the HTTP request, which keeps them out of the URL string and avoids length constraints.
Making a POST Request Using Python requests
import requests

# Target API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Data payload to send in the request body (JSON format)
payload = {
    "title": "Python Requests Demo",
    "body": "Sending a POST request using the requests library.",
    "userId": 1,
}

# Standard headers specifying the data type
headers = {"Content-Type": "application/json; charset=UTF-8"}

# Execute the POST request
response = requests.post(url, json=payload, headers=headers)

# Process the response
print(f"Status Code: {response.status_code}")
print("Response JSON:")
print(response.json())

Question 2: SQLite Database Operations in Python
Connecting to and manipulating a SQLite database in Python requires specific foundational steps using the built-in sqlite3 module:
 * sqlite3.connect(database_name): Establishes a database connection object to the specified SQLite file (or creates it if it does not exist). It acts as the primary communication bridge between the Python program and the database engine. Passing ":memory:" creates a temporary database stored entirely in RAM.
 * Cursor Object (connection.cursor()): Acts as a control structure to execute SQL statements and retrieve results. The cursor maintains context across operations, executing queries via .execute() or .executemany() and fetching query results using methods such as .fetchone(), .fetchall(), or .fetchmany().
 * connection.commit(): Saves (commits) all transactions performed during the connection session to the persistent database file. Without calling .commit(), structural schema modifications or data insertions/updates/deletions made during the execution context remain temporary and are rolled back when the connection closes.
Question 3: List Comprehensions in Python
Purpose and Syntax
A list comprehension provides a concise, readable, and pythonic way to construct a new list by applying an expression to each item in an existing iterable, optionally filtering elements based on a condition.
Syntax:
[expression for item in iterable if condition]

 * expression: The value or operation to evaluate and include in the output list.
 * item: The variable representing elements drawn sequentially from the iterable.
 * iterable: Any Python sequence or iterable object (e.g., list, tuple, range).
 * if condition (optional): A boolean filter that includes the item only when it evaluates to True.
Code Implementation
# List comprehension generating odd numbers between 1 and 50 that are divisible by 3
odd_divisible_by_3 = [num for num in range(1, 51) if num % 2 != 0 and num % 3 == 0]

print(odd_divisible_by_3)
# Output: [3, 9, 15, 21, 27, 33, 39, 45]
Question 4: Memory-Efficient Custom File Reader Generator
When processing files that exceed available system memory (RAM), reading the entire dataset into memory at once causes memory errors. The implementation below uses a memory-efficient generator to process large text files in fixed byte chunks while handling line tearing seamlessly.
from typing import Generator

def chunked_file_reader(
    file_path: str, chunk_size_bytes: int = 1024 * 1024
) -> Generator[str, None, None]:
    """Reads a large text file in binary chunks, yielding complete, unbroken lines.

    Prevents line tearing and maintains a minimal memory footprint.
    """
    with open(file_path, "rb") as file:
        buffer = b""

        while True:
            # Read a fixed-size byte block from disk
            chunk = file.read(chunk_size_bytes)

            # End of file reached
            if not chunk:
                # Yield any remaining text left in the buffer as the final line
                if buffer:
                    yield buffer.decode("utf-8", errors="replace")
                break

            buffer += chunk
            lines = buffer.split(b"\n")

            # The last element in lines might be incomplete (line tear across chunk boundaries).
            # Retain it in the buffer for the next iteration.
            buffer = lines.pop()

            # Yield complete, unbroken lines processed so far
            for line in lines:
                yield line.decode("utf-8", errors="replace")

# --- Example Usage ---
# file_gen = chunked_file_reader("large_dataset.csv", chunk_size_bytes=1024 * 1024)
# for line in file_gen:
#     process_line(line)  class Car:

    def _init_(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def get_description(self) -> str:
        """Returns a formatted basic description of the car."""
        return f"{self.year} {self.make} {self.model}"


class ElectricCar(Car):

    def _init_(
        self,
        make: str,
        model: str,
        year: int,
        battery_size: int,
        estimated_range: int = 300,
        charging_time_hours: float = 8.0,
    ):
        # Initialize attributes from the base class
        super()._init_(make, model, year)
        # Introduce specific ElectricCar attributes
        self.battery_size = battery_size  # Battery capacity in kWh
        self.estimated_range = estimated_range  # Estimated range in miles/km
        self.charging_time_hours = charging_time_hours  # Charge time from 0-100%

    def get_description(self) -> str:
        """Overrides base method to include battery size information."""
        base_desc = super().get_description()
        return f"{base_desc} (Battery: {self.battery_size} kWh)"

    def get_battery_info(self) -> str:
        """Returns detailed specs regarding the electric battery features."""
        return (
            f"Battery Specifications:\n"
            f" - Capacity: {self.battery_size} kWh\n"
            f" - Estimated Range: {self.estimated_range} miles\n"
            f" - Full Charge Time: approx. {self.charging_time_hours} hours"
        )


# Demonstration
if _name_ == "_main_":
    standard_car = Car("Toyota", "Camry", 2022)
    print("Standard Car Description:")
    print(standard_car.get_description())

    print("\n" + "=" * 40 + "\n")

    ev = ElectricCar(
        make="Tesla",
        model="Model 3",
        year=2024,
        battery_size=75,
        estimated_range=341,
        charging_time_hours=6.5,
    )
    print("EV Description (Overridden Method):")
    print(ev.get_description())

    print("\nEV Detailed Battery Features:")
    print(ev.get_battery_info())
     print("EV Description (Overridden Method):")
    print(ev.get_description())

    print("\nEV Detailed Battery Features:")
    print(ev.get_battery_info())
