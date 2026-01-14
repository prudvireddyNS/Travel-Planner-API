# Travel Planner API

A comprehensive REST API for planning and managing travel itineraries, destinations, and activities. This API provides a robust backend solution for travel planning applications.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [API Endpoints](#api-endpoints)
- [Usage Examples](#usage-examples)
- [Authentication](#authentication)
- [Database Schema](#database-schema)
- [Error Handling](#error-handling)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Travel Planner API is designed to simplify travel planning by providing endpoints to manage trips, destinations, accommodations, activities, and itineraries. It serves as the backend for travel planning applications and can be integrated with various frontend frameworks.

## Features

- **Trip Management**: Create, read, update, and delete trips
- **Destination Management**: Browse and manage travel destinations
- **Activity Planning**: Add and schedule activities within trips
- **Accommodation Management**: Search and book accommodations
- **Itinerary Building**: Create detailed day-by-day itineraries
- **User Profiles**: Manage user preferences and travel history
- **Search & Filter**: Advanced search capabilities for destinations and activities
- **Reviews & Ratings**: Rate and review destinations and accommodations
- **Collaborative Planning**: Share trips and collaborate with other users
- **Weather Integration**: Get weather information for destinations
- **Cost Tracking**: Monitor and manage trip budgets

## Tech Stack

- **Runtime**: Node.js
- **Framework**: Express.js
- **Database**: MongoDB / PostgreSQL (configurable)
- **Authentication**: JWT (JSON Web Tokens)
- **API Documentation**: Swagger/OpenAPI
- **Testing**: Jest, Mocha, Chai
- **Deployment**: Docker, Kubernetes

## Installation

### Prerequisites

- Node.js (v14.0 or higher)
- npm or yarn
- MongoDB or PostgreSQL
- Git

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/prudvireddyNS/Travel-Planner-API.git
   cd Travel-Planner-API
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Create environment file**
   ```bash
   cp .env.example .env
   ```

4. **Configure your database**
   Update the `.env` file with your database connection string and credentials.

5. **Run database migrations**
   ```bash
   npm run db:migrate
   ```

6. **Start the server**
   ```bash
   npm start
   ```

The API will be available at `http://localhost:3000` by default.

## Configuration

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Server Configuration
NODE_ENV=development
PORT=3000
HOST=localhost

# Database Configuration
DB_HOST=localhost
DB_PORT=27017
DB_NAME=travel_planner
DB_USER=your_username
DB_PASSWORD=your_password

# JWT Configuration
JWT_SECRET=your_secret_key
JWT_EXPIRATION=7d

# API Keys (External Services)
WEATHER_API_KEY=your_weather_api_key
GOOGLE_MAPS_API_KEY=your_google_maps_key

# Email Configuration
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password

# File Upload
MAX_FILE_SIZE=5mb
UPLOAD_DIR=./uploads

# CORS Configuration
CORS_ORIGIN=http://localhost:3000

# Logging
LOG_LEVEL=info
```

## API Endpoints

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register` | Register a new user |
| POST | `/api/auth/login` | User login |
| POST | `/api/auth/logout` | User logout |
| POST | `/api/auth/refresh` | Refresh JWT token |
| POST | `/api/auth/forgot-password` | Request password reset |
| POST | `/api/auth/reset-password` | Reset password with token |

### User Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/users/profile` | Get user profile |
| PUT | `/api/users/profile` | Update user profile |
| GET | `/api/users/{id}` | Get user by ID |
| DELETE | `/api/users/{id}` | Delete user account |
| GET | `/api/users/{id}/trips` | Get user's trips |

### Trip Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/trips` | Get all trips |
| POST | `/api/trips` | Create new trip |
| GET | `/api/trips/{id}` | Get trip details |
| PUT | `/api/trips/{id}` | Update trip |
| DELETE | `/api/trips/{id}` | Delete trip |
| GET | `/api/trips/{id}/itinerary` | Get trip itinerary |
| POST | `/api/trips/{id}/collaborators` | Add trip collaborator |

### Destination Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/destinations` | Get all destinations |
| POST | `/api/destinations` | Create destination |
| GET | `/api/destinations/{id}` | Get destination details |
| PUT | `/api/destinations/{id}` | Update destination |
| DELETE | `/api/destinations/{id}` | Delete destination |
| GET | `/api/destinations/{id}/reviews` | Get destination reviews |

### Activity Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/activities` | Get all activities |
| POST | `/api/activities` | Create activity |
| GET | `/api/activities/{id}` | Get activity details |
| PUT | `/api/activities/{id}` | Update activity |
| DELETE | `/api/activities/{id}` | Delete activity |

### Accommodation Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/accommodations` | Get all accommodations |
| POST | `/api/accommodations` | Create accommodation |
| GET | `/api/accommodations/{id}` | Get accommodation details |
| PUT | `/api/accommodations/{id}` | Update accommodation |
| DELETE | `/api/accommodations/{id}` | Delete accommodation |
| POST | `/api/accommodations/{id}/book` | Book accommodation |

### Itinerary Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/itineraries` | Get all itineraries |
| POST | `/api/itineraries` | Create itinerary |
| GET | `/api/itineraries/{id}` | Get itinerary details |
| PUT | `/api/itineraries/{id}` | Update itinerary |
| DELETE | `/api/itineraries/{id}` | Delete itinerary |

## Usage Examples

### Register a New User

```bash
curl -X POST http://localhost:3000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "securepassword",
    "firstName": "John",
    "lastName": "Doe"
  }'
```

### Create a New Trip

```bash
curl -X POST http://localhost:3000/api/trips \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Summer Vacation in Europe",
    "description": "A 2-week trip across Europe",
    "startDate": "2026-06-01",
    "endDate": "2026-06-15",
    "destinations": ["Paris", "Rome", "Barcelona"],
    "budget": 5000
  }'
```

### Get Trip Details

```bash
curl -X GET http://localhost:3000/api/trips/trip_id \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

### Add Activity to Trip

```bash
curl -X POST http://localhost:3000/api/activities \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "tripId": "trip_id",
    "title": "Visit Eiffel Tower",
    "destination": "Paris",
    "date": "2026-06-05",
    "startTime": "10:00",
    "endTime": "12:00",
    "category": "sightseeing",
    "cost": 15
  }'
```

### Search Destinations

```bash
curl -X GET "http://localhost:3000/api/destinations?country=France&rating=4.5&limit=10" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

## Authentication

The API uses JWT (JSON Web Tokens) for authentication. Include the token in the Authorization header:

```bash
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### Token Refresh

Tokens expire after the period specified in your `.env` file. Use the refresh endpoint to get a new token:

```bash
curl -X POST http://localhost:3000/api/auth/refresh \
  -H "Content-Type: application/json" \
  -d '{
    "refreshToken": "your_refresh_token"
  }'
```

## Database Schema

### Users Collection

```javascript
{
  _id: ObjectId,
  email: String (unique),
  password: String (hashed),
  firstName: String,
  lastName: String,
  avatar: String,
  bio: String,
  country: String,
  preferences: {
    notifications: Boolean,
    theme: String,
    language: String
  },
  createdAt: Date,
  updatedAt: Date
}
```

### Trips Collection

```javascript
{
  _id: ObjectId,
  userId: ObjectId (ref: User),
  title: String,
  description: String,
  startDate: Date,
  endDate: Date,
  destinations: [String],
  budget: Number,
  estimatedCost: Number,
  actualCost: Number,
  status: String (enum: planning, ongoing, completed),
  collaborators: [ObjectId] (ref: User),
  createdAt: Date,
  updatedAt: Date
}
```

### Activities Collection

```javascript
{
  _id: ObjectId,
  tripId: ObjectId (ref: Trip),
  title: String,
  description: String,
  destination: String,
  category: String,
  date: Date,
  startTime: String,
  endTime: String,
  cost: Number,
  rating: Number,
  location: {
    latitude: Number,
    longitude: Number,
    address: String
  },
  createdAt: Date,
  updatedAt: Date
}
```

## Error Handling

The API returns standard HTTP status codes and error messages:

### Response Format

```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "User-friendly error message",
    "details": {}
  }
}
```

### Common Error Codes

| Code | HTTP Status | Description |
|------|------------|-------------|
| INVALID_CREDENTIALS | 401 | Invalid email or password |
| TOKEN_EXPIRED | 401 | JWT token has expired |
| UNAUTHORIZED | 401 | User not authenticated |
| FORBIDDEN | 403 | User lacks permissions |
| NOT_FOUND | 404 | Resource not found |
| CONFLICT | 409 | Resource already exists |
| VALIDATION_ERROR | 422 | Input validation failed |
| INTERNAL_ERROR | 500 | Server error |

## Testing

### Run All Tests

```bash
npm test
```

### Run Tests with Coverage

```bash
npm run test:coverage
```

### Run Specific Test Suite

```bash
npm test -- tests/api/trips.test.js
```

### Test Files Location

Tests are located in the `/tests` directory, organized by feature:

```
tests/
├── api/
│   ├── auth.test.js
│   ├── trips.test.js
│   ├── activities.test.js
│   └── ...
├── models/
├── middleware/
└── utils/
```

## Deployment

### Docker Deployment

1. **Build the Docker image**
   ```bash
   docker build -t travel-planner-api .
   ```

2. **Run the container**
   ```bash
   docker run -p 3000:3000 --env-file .env travel-planner-api
   ```

### Docker Compose

```bash
docker-compose up -d
```

### Kubernetes Deployment

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### Environment-specific Deployment

```bash
# Development
npm run deploy:dev

# Staging
npm run deploy:staging

# Production
npm run deploy:prod
```

## API Documentation

Interactive API documentation is available via Swagger UI:

- **Local**: `http://localhost:3000/api-docs`
- **Production**: `https://api.travelplanner.com/api-docs`

## Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit your changes**
   ```bash
   git commit -am 'Add some feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Create a Pull Request**

### Code Style

- Use ESLint for code linting: `npm run lint`
- Use Prettier for code formatting: `npm run format`
- Follow the existing code structure and naming conventions

### Commit Message Guidelines

- Use clear and descriptive commit messages
- Format: `[Type] Description`
- Types: feat, fix, docs, style, refactor, test, chore

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For issues, feature requests, or support:

- **Issues**: [GitHub Issues](https://github.com/prudvireddyNS/Travel-Planner-API/issues)
- **Email**: support@travelplanner.com
- **Documentation**: [Full Documentation](https://docs.travelplanner.com)

## Acknowledgments

- Special thanks to all contributors
- Inspiration from travel and tourism APIs
- Community feedback and suggestions

---

**Last Updated**: 2026-01-14
**Maintained by**: prudvireddyNS
