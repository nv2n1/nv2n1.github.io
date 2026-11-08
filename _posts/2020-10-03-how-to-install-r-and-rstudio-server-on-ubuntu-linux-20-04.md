---
title: "Setting Up R and RStudio Server on Ubuntu"
date: 2020-10-03 10:33:28 +0000
modified: 2026-04-11 17:11:34 +0000
author: "David Yang"
layout: post
categories: [web-development]
canonical: /how-to-install-r-and-rstudio-server-on-ubuntu-linux-20-04/
---

R is a language and environment for statistical computing and graphics. It’s free software under the GPL license and provides extensive statistical and graphical capabilities through numerous contributed packages.

The R environment package is available in Ubuntu’s standard repositories. Install it with:

``` bash
sudo apt update
sudo apt install r-base
```

This installs `r-base` along with recommended packages and build tools. The installation may take several minutes and will pull in dependencies like BLAS, LAPACK, and development libraries.

Once installed, verify the installation by starting the R REPL:

``` bash
R
```

You should see output like:

    R version 4.3.x (202x-xx-xx) -- "[Release Name]"
    Copyright (C) 202x The R Foundation for Statistical Computing
    Platform: x86_64-pc-linux-gnu (64-bit)

    R is free software and comes with ABSOLUTELY NO WARRANTY.
    ...
    Type 'q()' to quit R.

    >

Exit the REPL by typing `q()` at the prompt.

## Install RStudio Server on Ubuntu

RStudio Server is a browser-based IDE for R that runs on a remote server and is accessed through any web browser. This makes it ideal for shared computing environments or cloud deployments.

First, check the <a href="https://posit.co/download/rstudio-server/" rel="nofollow noopener" target="_blank">RStudio downloads page</a> to get the correct URL for your Ubuntu version. Then download and install the package:

``` bash
wget https://download2.rstudio.org/server/focal/amd64/rstudio-server-latest-amd64.deb
sudo apt install ./rstudio-server-latest-amd64.deb
```

The installation script will automatically create the `rstudio-server` system user and start the service. RStudio Server listens on port 8787 by default.

Verify that the service is running:

``` bash
sudo systemctl status rstudio-server
```

If the service isn’t running, start it with:

``` bash
sudo systemctl start rstudio-server
```

## Access RStudio Server

Open a web browser and navigate to:

    http://<server-ip-or-domain>:8787

For local access, use `http://localhost:8787`.

Log in with any valid Ubuntu system user account. The username and password must correspond to a real user on the system.

Once logged in, you’ll have access to the RStudio IDE with a console, script editor, package manager, and file browser.

## Useful RStudio Server Management Commands

Stop the server:

``` bash
sudo systemctl stop rstudio-server
```

Restart the server:

``` bash
sudo systemctl restart rstudio-server
```

View the service log:

``` bash
sudo journalctl -u rstudio-server -n 50
```

Check RStudio Server version:

``` bash
rstudio-server version
```

## Configure RStudio Server

RStudio Server configuration is stored in `/etc/rstudio/rserver.conf`. Common configurations include changing the default port:

    www-port=8787
    www-address=0.0.0.0

After editing the config file, restart the service:

``` bash
sudo systemctl restart rstudio-server
```

## Firewall Configuration

If your system uses a firewall (UFW on Ubuntu), allow access to port 8787:

``` bash
sudo ufw allow 8787/tcp
```

For cloud deployments (AWS, Azure, GCP), ensure the security group or network ACL permits inbound traffic on port 8787.

## Install R Packages in RStudio Server

From the RStudio console, install packages using `install.packages()`:

``` r
install.packages("ggplot2")
install.packages(c("dplyr", "tidyr", "ggplot2"))
```

Load packages with `library()`:

``` r
library(ggplot2)
```

## Performance Considerations

For production deployments, consider:

- Running RStudio Server behind a reverse proxy (nginx or Apache) for SSL/TLS termination
- Configuring resource limits in `rserver.conf` to prevent runaway processes from consuming system resources
- Using authentication providers like PAM or LDAP for larger organizations
- Running multiple sessions with appropriate memory and process limits
- Monitoring disk space, especially in `/home` where user libraries are installed

## Troubleshooting

If users cannot log in, check that their system account exists:

``` bash
id username
```

If RStudio Server won’t start, check the log:

``` bash
tail /var/log/rstudio/rstudio-server.log
```

For permission issues with package installation, ensure users have write access to their home directory and the R library path.
