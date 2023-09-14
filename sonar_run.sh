#!/bin/bash

sonar-scanner \
  -Dsonar.projectKey=zangotasks \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=sqp_56e161b1f2a5a0483a1cf79da1658aabe6cc73fd \
  -Dsonar.python.coverage.reportPaths=coverage.xml \
  -Dsonar.exclusions=**/migrations/** \
