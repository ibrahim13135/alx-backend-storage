#!/bin/bash

# Function to check Docker daemon logs
check_docker_logs() {
    echo "Checking Docker daemon logs..."
    sudo journalctl -u docker | tail -n 50
}

# Function to purge Docker
purge_docker() {
    echo "Purging Docker..."
    sudo apt-get purge -y docker-ce docker-ce-cli containerd.io
    sudo apt-get autoremove -y
}

# Function to install Docker
install_docker() {
    echo "Installing Docker..."
    sudo apt-get update
    sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    sudo apt-get update
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io
}

# Function to start Docker service
start_docker() {
    echo "Starting Docker service..."
    sudo service docker start
}

# Function to check Docker service status
check_docker_status() {
    echo "Checking Docker service status..."
    sudo service docker status
}

# Function to ensure necessary kernel modules are loaded
load_kernel_modules() {
    echo "Loading necessary kernel modules..."
    sudo modprobe overlay
    sudo modprobe br_netfilter
}

# Function to check Docker configuration file
check_docker_config() {
    echo "Checking Docker configuration file..."
    if [ -f /etc/docker/daemon.json ]; then
        cat /etc/docker/daemon.json
    else
        echo "/etc/docker/daemon.json does not exist."
    fi
}

# Function to run Docker inside Docker container (DinD)
run_dind_container() {
    echo "Running Docker inside a Docker container (DinD)..."
    sudo docker run --privileged --name dind -d docker:stable-dind
}

# Function to use Docker's debug script
use_docker_debug_script() {
    echo "Using Docker's debug script..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh --debug
}

# Main script execution
check_docker_logs
purge_docker
install_docker
start_docker
check_docker_status
load_kernel_modules
check_docker_config
use_docker_debug_script

# Uncomment the following line if you want to run Docker inside a Docker container (DinD)
# run_dind_container
