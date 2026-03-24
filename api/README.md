# API Service

A high-performance RESTful API service built with Node.js and Express.

## Features

- RESTful endpoints for CRUD operations
- JWT-based authentication
- Rate limiting
- Request validation
- Logging middleware
- Docker support

## Prerequisites

- Node.js 18+
- npm 9+
- Docker (optional)

## Installation

```bash
npm install
```

## Configuration

Copy `.env.example` to `.env` and update the values:

```bash
cp .env.example .env
```

## Running the Service

Start in development mode:

```bash
npm run dev
```

Start in production mode:

```bash
npm start
```

Build and run with Docker:

```bash
docker build -t api-service .
docker run -p 3000:3000 api-service
```

## Testing

Run unit tests:

```bash
npm test
```

Run integration tests:

```bash
npm run test:integration
```

## API Documentation

See the [API Documentation](docs/api.md) for detailed endpoint specifications.

## License

MIT