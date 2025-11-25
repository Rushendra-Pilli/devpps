terraform{
    required_providers{
        docker = {
      source = "kreuzwerker/docker"
      version = "~> 3.0"
    }
    }
}

provider "docker"{}

resource "docker_container" "student"{
    image = "python:3.9-slim"
    name = "student-app"
    command = ["sleep","3600"]
    ports{
        internal = 4000
        external = 4000
    }
}