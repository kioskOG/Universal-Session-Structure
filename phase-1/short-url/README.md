# Python-Project-Url-Shortner

## Overview

Python-Project-Url-Shortner is a web application that provides URL shortening functionality along with user interface, authentication, reporting, and URL shortening services.

## Services

### UI Service

- **Description**: This service provides the user interface for the URL shortener application.
- **Path**: `/`
- **Docker Service Name**: `flask-uiapp`
- **Port**: 5000

### AUTH Service

- **Description**: This service handles user authentication and interacts with the database for user information.
- **Paths**:
  - `/api/v1/auth/register`
  - `/api/v1/auth/login`
- **Docker Service Name**: `flask-authapp`
- **Port**: 5000

### REPORT Service

- **Description**: This service generates reports showing URLs visited by users.
- **Path**: `/report`
- **Docker Service Name**: `flask-reportapp`
- **Port**: 5000

### URL-SHORT Service

- **Description**: This service shortens long URLs and redirects users to the original URL.
- **Paths**:
  - `/api/url`
  - `/r/<short_url>` --> "<short_url>" this is a short url which can be used to visit the long url
  - `/allurls`
- **Docker Service Name**: `flask-shorturlapp`
- **Port**: 5000

## Usage

To access the various services, use the appropriate paths mentioned above in combination with the base URL of your Docker cluster.

For example:
- To access the UI Service: `http://<cluster-ip>/`
- To register a new user: `http://<cluster-ip>/api/v1/auth/register`
- To shorten a URL: `http://<cluster-ip>/api/url`

## Installation

1. Clone the repository.
2. Deploy the services to your Docker cluster using the provided Docker configuration files.

## Dependencies

- Python 3.x
- Flask
- Docker

![Jhon Wick](<undefined - Imgur.gif>)
