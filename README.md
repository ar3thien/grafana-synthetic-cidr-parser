# grafana-synthetic-cidr-parser

## Overview

This script is designed to fetch the CIDR ranges used by Grafana Cloud for synthetic monitoring. It retrieves the data from this endpoint https://allowlists.grafana.com/synthetics and processes it into individual text files for easy reference. Each file contains plain text representations of the CIDR ranges, with a timestamp indicating when the data was last fetched.

## Purpose

This script is designed for firewalls, such as OPNsense, which do not have native support for parsing JSON lists. By converting the Grafana Cloud CIDR ranges into plain text files, the script makes it easier for these firewalls to process and utilize the data.

## Schedule

This script is designed to run on an **hourly basis**. Each time it runs, it fetches the latest data from the endpoint and updates the generated text files with new content, ensuring that the output files are always up to date with the latest JSON data.

## Usage

To obtain the required CIDR range file, refer to the `output_files` folder. You can use the raw version of files directly for your firewall configurations.
For example:
https://raw.githubusercontent.com/ar3thien/grafana-synthetic-cidr-parser/main/output_files/all_ipv4.txt
