# Ng-Flask

A Docker appliance for deploying client/server web applications using Angular and Flask 
with a preexisting Traefik reverse proxy server.

## Getting Started

These instructions will get a project up and running on your local
machine for development and testing purposes. See deployment for notes on how to deploy
your project on a live system.

### Prerequisites

What things you need to install the software and how to install them:

- <a href="https://docs.docker.com/engine/installation/">Docker</a>
- <a href="https://docs.docker.com/compose/install/">Docker-Compose</a>

### Installing

1. Download the repository.

    ```
    git clone {this repo}
    cd {this repo}
    ```

1. Change the environment variables in the .env file.

    - CLIENT_FRONTEND = domain for frontend client application
    - CLIENT_PORT = port on which to serve backend client application
    - SERVER_FRONTEND = domain for frontend server application 
    - SERVER_PORT = port on which to serve backend server application
    - NETWORK = name of preexisting Traefik reverse proxy server

1. Run the appliance.

    ```
    docker-compose -f docker-compose.dev.yml up -d
    ```

1. Visit your Traefik dashboard to confirm that the new NgFlask application is up and running.

## Deployment
To deploy the container and application in a production environment:

```
docker-compose up -d
```

## Built With

* [Angular CLI] (https://cli.angular.io/) - the frontend web framework
* [Flask] (http://flask.pocoo.org/) - the backend framework
* [Docker] (https://www.docker.com/) - the containerization platform

## Authors

* **Patrick Ryan**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
