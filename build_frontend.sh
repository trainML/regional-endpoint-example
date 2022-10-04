#!/bin/bash

rm -rf webroot/*
cd simple-classifier-endpoint/front-end
sed -i 's/api_address:.*/api_address: '"'"''"'"',/g' src/config.js
sed -i 's/route_path:.*/route_path: '"'"'\/api\/predict'"'"',/g' src/config.js
npm install
npm run build
cd build
mv * ../../../webroot/
cd ..
git reset --hard

