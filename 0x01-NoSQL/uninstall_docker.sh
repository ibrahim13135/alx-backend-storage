#!/bin/bash

# Function to stop Docker service
stop_docker_service() {
    echo "Stopping Docker service..."
    sudo service docker stop
}

# Function to purge Docker and related packages
purge_docker() {
    echo "Purging Docker and related packages..."
    sudo apt-get purge -y docker-ce docker-ce-cli containerd.io
    sudo apt-get purge -y docker docker-engine docker.io
    sudo apt-get autoremove -y
}

# Function to remove Docker directories
remove_docker_directories() {
    echo "Removing Docker directories..."
    sudo rm -rf /var/lib/docker
    sudo rm -rf /etc/docker
    sudo rm -rf /var/run/docker
    sudo rm -rf /var/run/docker.sock
    sudo rm -rf /usr/libexec/docker
    sudo rm -rf /var/lib/containerd
    sudo rm -rf /var/lib/dockershim
}

# Function to remove Docker configuration files
remove_docker_configs() {
    echo "Removing Docker configuration files..."
    sudo rm -f /etc/systemd/system/docker.service
    sudo rm -f /etc/systemd/system/docker.socket
    sudo rm -f /lib/systemd/system/docker.service
    sudo rm -f /lib/systemd/system/docker.socket
    sudo rm -f /etc/default/docker
    sudo rm -f /etc/docker/daemon.json
}

# Function to clean up remaining dependencies and cache
clean_up() {
    echo "Cleaning up remaining dependencies and cache..."
    sudo apt-get autoremove -y
    sudo apt-get autoclean
}

# Main script execution
stop_docker_service
purge_docker
remove_docker_directories
remove_docker_configs
clean_up

echo "Docker and all associated files have been removed from the system."
