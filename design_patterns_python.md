# Design Pattern: Factory Pattern in UserSection

## Problem
The original `signupAccount` view directly created instances of the `CustomUser` class to handle user registration. This made it difficult to extend the system to support different types of users, such as drivers or passengers, without adding significant complexity to the view.

## Solution
To address this, we implemented the **Factory Pattern**. The `UserFactory` class is responsible for creating users of different types (e.g., `CustomUser`, `Driver`, `Passenger`) without hardcoding the creation logic in the view. This makes the system more extensible and easier to maintain, as new user types can be added by modifying the factory without altering the core view logic.

### Code Implementation
We created a `UserFactory` class that determines the type of user to create based on input parameters. The view `signupAccount` now uses the factory to create users, making it easier to extend or change the creation logic in the future.

#### UserFactory Class
```python
class UserFactory:
    @staticmethod
    def create_user(user_type, user_data):
        if user_type == 'custom':
            user = CustomUser()
        elif user_type == 'driver':
            user = Driver()
        elif user_type == 'passenger':
            user = Passenger()
        else:
            raise ValueError(f"Unknown user type: {user_type}")
        
        user.save_user(user_data)
        return user
