FROM docker.n8n.io/n8nio/n8n:latest

# We don't need to copy the JSON file into the image because 
# the easiest way for you to manage it is to import it via the UI once deployed.
# This Dockerfile simply tells Render to use the official n8n image.
