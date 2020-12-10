#!/bin/bash
curl -s -XPOST -d '{"type" : "latency", "attributes" : {"latency" : 3000}}' http://localhost:8474/proxies/recibo/toxics
