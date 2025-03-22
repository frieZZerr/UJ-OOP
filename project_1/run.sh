#!/bin/bash

APP="RandomSort"

docker pull kprzystalski/projobj-pascal

docker run --rm -it -v "$(pwd)":/home/student/projobj kprzystalski/projobj-pascal:latest fpc $APP.pas
echo
docker run --rm -it -v "$(pwd)":/home/student/projobj kprzystalski/projobj-pascal:latest  ./$APP
