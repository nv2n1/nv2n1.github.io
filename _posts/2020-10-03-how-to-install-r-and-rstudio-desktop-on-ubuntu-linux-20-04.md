---
title: "Installing R and RStudio on Ubuntu"
date: 2020-10-03 11:49:20 +0000
layout: post
canonical: https://www.systutorials.com/how-to-install-r-and-rstudio-desktop-on-ubuntu-linux-20-04/
---

Start by updating your package manager and installing R:

``` bash
sudo apt update
sudo apt install r-base
```

This installs the base R distribution from Ubuntu’s default repositories. For more details on R installation, see the dedicated R installation guide.

## Install RStudio Desktop

Once R is installed, you can add RStudio Desktop as your local IDE.

### Download RStudio Desktop

Check the <a href="https://posit.co/download/rstudio-desktop/" rel="nofollow noopener" target="_blank">official RStudio download page</a> for the latest version and Ubuntu architecture. RStudio currently provides builds for Ubuntu 18.04 through 24.04 (Jammy). Download the appropriate `.deb` file:

``` bash
wget https://download1.rstudio.org/desktop/jammy/amd64/rstudio-2025.02.0-daily+496-amd64.deb
```

Update the version number and filename to match what you download.

### Install the package

Install the downloaded `.deb` file:

``` bash
sudo apt install ./rstudio-2025.02.0-daily+496-amd64.deb
```

apt will resolve dependencies automatically. The installation will complete with output confirming the package setup and triggering desktop file updates.

### Alternative: Using RStudio’s package repository

For easier updates, add RStudio’s repository to your system:

``` bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E7F57070
sudo apt-add-repository "deb https://rstudio.r-project.org/ubuntu jammy main"
sudo apt update
sudo apt install rstudio-desktop
```

This approach allows you to update RStudio alongside other system packages using `sudo apt upgrade`.

## Verify installation

Launch RStudio Desktop either from your application menu or directly from the terminal:

``` bash
rstudio
```

The RStudio window will open with the Console panel ready. Test your R installation by running a demo:

``` r
demo(nlm)
```

Press Enter when prompted. The demo will execute and display plots in the Plots panel, confirming both R and RStudio are functioning correctly.

## Troubleshooting

If RStudio fails to start, verify R was installed correctly:

``` bash
R --version
```

If you encounter library dependency errors during installation, install missing packages:

``` bash
sudo apt install --fix-missing
```

For systems using newer Ubuntu versions (24.04+), ensure you download the correct architecture-specific build. Check your system architecture with:

``` bash
uname -m
```

This returns either `x86_64` (standard) or `aarch64` (ARM-based).

## Next steps

Once RStudio is running, consider installing additional R packages for your workflow using the package manager within RStudio or via the command line:

``` r
install.packages("package_name")
```

For reproducible environments, consider using `renv` to manage per-project dependencies, or use Docker if you need isolated R environments across multiple machines.

## Troubleshooting Common Issues

If you encounter problems during installation, check these common solutions:

- Ensure your system packages are up to date before installing new software
- Check for conflicting packages that might prevent installation
- Verify network connectivity if downloading packages from external repositories
- Review system logs in /var/log/ for detailed error messages

## Verification Steps

After installation, verify everything is working correctly by checking the installed version and running basic functionality tests. Most command-line tools respond to the –version or -v flag to display their version information.

## Keeping Your Installation Updated

Regularly update your system to receive security patches and bug fixes. On Fedora, use dnf update. On Ubuntu and Debian, use apt update followed by apt upgrade. For software installed via language-specific package managers like pip, npm, or gem, check their respective update commands.

## Related Linux Commands

These related commands are often used alongside the tools discussed in this article:

- man command-name – Read the manual page for any command
- which command-name – Find the location of an executable
- rpm -qa or dpkg -l – List installed packages
- journalctl -u service-name – Check service logs
- ss -tulpn – List listening ports and services

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.
