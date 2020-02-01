## Getting Started

In the root directory of the project...

1. Install node modules `yarn install` or `npm install`.
2. Install Python dependencies `yarn install-requirements` or `npm install-requirements`
2. Start development server `yarn start` or `npm start`.


## File Structure

The front-end is based on [Vue](https://vuejs.org/).

The back-end is based on [Flask](https://github.com/pallets/flask).

The database is based on [MongoDB](https://www.mongodb.com/)

The front-end is served on http://localhost:3000/ and the back-end on http://localhost:3001/.

```
.
├── server/ - Flask server that provides API routes and serves front-end
│ ├── DB/                   - Default images js & css library
│ ├── constants.py          - Defines the constants for the endpoints and port
│ └── server.py             - Configures Port and HTTP Server and provides API routes

├── client - Vue front-end
│   ├── assets/             - Default images js & css library
│   ├── components/         - Common Vue components shared between different views
│   ├── router/             - Vue routes
│   ├── views/              - The main pages displayed
│   ├── constants.js        - Contains constants for error messages and endpoints
│   ├── App.vue             - Base Vue template
│   └── main.js             - Root Vue Component
└── README.md
```

## Additional Documentation


- Vue - https://vuejs.org/v2/guide/
- Tailwind CSS - https://tailwindcss.com/

- Flask - http://flask.pocoo.org/
- PyMongo - https://api.mongodb.com/python/current/

