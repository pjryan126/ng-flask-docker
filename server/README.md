# Flask-Docker

A Docker container for developing and deploying Flask applications.

## Getting Started

These instructions will get you a copy of the project up and running on your local
machine for development and testing purposes. See deployment for notes on how to deploy
the project on a live system.

### Prerequisites

What things you need to install the software and how to install them:

- <a href="https://docs.docker.com/engine/installation/">Docker</a>
- <a href="https://docs.docker.com/compose/install/">Docker-Compose</a>

### Installing

1. Download the repository.

    ```
    git clone https://github.com/pjryan126/flask-docker.git
    cd flask-docker
    ```

1. Change the environment variables in the .env file.

    - PORT = port on which the Flask application will run

1. Run the container.  

    ```
    docker-compose -f docker-compose.dev.yml up -d
    ```

## Deployment
To deploy the container and application in a production environment, use the docker-compose.prod.yml file.  

```
docker-compose up -d
```

## Built With

* [Flask] (http://flask.pocoo.org/) - the backend framework
* [Docker] (https://www.docker.com/) - the containerization platform

## Authors

* **Patrick Ryan**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
