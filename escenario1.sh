#!/bin/bash
curl -s -XPOST -d '{"type" : "timeout", "attributes" : {"timeout" : 5000}}' http://localhost:8474/proxies/banco/toxics
