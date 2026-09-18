#!/bin/bash
# Sends a GET request to a URL with a specific header variable
curl -sG -H "X-HolbertonSchool-User-Id: 98" "$1"
