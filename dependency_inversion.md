# Dependency Inversion in UserSection

## Problem
Originally, the `signupAccount` view in `UserSection` directly depended on the concrete implementations of the models `CustomUser` and `Vehicle`. This created tight coupling between the view and the data layer, making it difficult to extend or modify in the future.

## Solution
To reduce this coupling, we introduced two abstract base classes: `AbstractUser` and `AbstractVehicle`. These serve as interfaces, defining methods for saving user and vehicle data without tying the view to any specific implementation. The view now depends on these abstract classes, and the models `CustomUser` and `Vehicle` implement them.

This allows for better flexibility in the future, as we can easily swap out the concrete implementations for different ones, such as if we introduce a different type of user or vehicle model.

## Code Changes
### Abstract Classes
```python
from abc import ABC, abstractmethod

class AbstractUser(ABC):
    @abstractmethod
    def save_user(self, user_data):
        pass

class AbstractVehicle(ABC):
    @abstractmethod
    def save_vehicle(self, vehicle_data):
        pass
