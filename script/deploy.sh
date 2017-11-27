#!/bin/sh

# Não faz deploy com Pull Requests. As envs criptografadas não estão disponíveis.
if [ "${TRAVIS_PULL_REQUEST}" = false ]; then
  
  # O deploy só é executado em tags e vira o latest
  PLONEGOVBR_VERSION="${SOURCE_BRANCH}";

  docker build --build-arg PLONEGOVBR_VERSION=$PLONEGOVBR_VERSION -t plonegovbr/plonegovbr:$PLONEGOVBR_VERSION -t plonegovbr/plonegovbr:latest docker/
  docker login -u "$DOCKER_LOGIN" -p "$DOCKER_PASS"
  docker push plonegovbr/plonegovbr:$PLONEGOVBR_VERSION
  docker push plonegovbr/plonegovbr:latest
fi
