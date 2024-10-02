# New Functionality: Comment System with Notifications

## Overview
We have added a comment system where users can leave comments and view a list of all comments. We have applied the **Observer Pattern** to notify administrators when new comments are added.

### Comment System
- Users can add comments using a form.
- All comments are displayed in reverse chronological order.

### Observer Pattern
We implemented a function `notify_admin_new_comment()` that simulates a notification system, alerting administrators when a new comment is added. This is the first step towards integrating a real notification system, such as email or push notifications.

#### Code Example
```python
def notify_admin_new_comment(comment):
    print(f'Nuevo comentario por {comment.user.username}: "{comment.content}"')
