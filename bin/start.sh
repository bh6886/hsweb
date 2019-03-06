#!/bin/bash
sed -in "s/111.111.111.111/${ORACLE_ADDR}/g" /opt/skytest/hs/config.conf
sed -in "s/222.222.222.222/${HDC_ADDR}/g" /opt/skytest/hs/config.conf
nginx  
cd /opt/skytest/bin && ./restart.sh
