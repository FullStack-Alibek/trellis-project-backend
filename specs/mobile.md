# Mobile Application Specification

## Purpose

Cross-platform mobile application for Android, iOS and RuStore.

## User Roles

### User
- Upload images
- Generate 3D models
- View generation history
- Download generated models
- Manage profile and balance

### Admin
- View users
- Monitor generations
- Manage system settings

## Main Features

### Authentication
- Registration
- Login
- Password recovery
- JWT authentication

### Profile
- Edit profile
- View balance
- View subscription

### Image Upload
- Camera upload
- Gallery upload
- Preview image

### 3D Generation
- Submit generation task
- Track progress
- View status

### History
- List generations
- Search generations
- Download generated files

### Notifications
- Generation completed
- System notifications

## Screens

### Splash Screen

### Login Screen

### Registration Screen

### Home Screen

### Upload Screen

### Generation Screen

### History Screen

### Profile Screen

### Settings Screen

## API Integration

- POST /upload-image
- POST /generate-3d
- GET /job/{id}
- GET /download/{filename}

## Non Functional Requirements

- Android support
- iOS support
- RuStore support
- Offline cache
- Push notifications