# Analytics Service

This project is a simple Django web application for managing events. The app allows users to create events, store event data in a database, and view event details.

## Tech Stack

- Python 3.x
- Django 4.x
- Celery (for asynchronous tasks)
- Redis (as a task broker for Celery)
- PostgreSQL (for data storage)
- Docker (for containerization)

## Features

1. **User Registration and Authentication**

   - Users can register and log in.
   - Sessions are used for authentication.

2. **Event Creation**

   - Users can create events through a form.
   - Event data is stored in the database and processed asynchronously.

3. **Event List View**

   - Users can view a list of all events.

4. **Event Detail View**

   - Users can view detailed information about a specific event, including formatted data.

5. **Event Processing in the Background**
   - After creating an event, its data is processed in a background task and converted into a text format.

## Setup

1. Clone the repository:
   git clone https://github.com/yourusername/event-analytics.git
