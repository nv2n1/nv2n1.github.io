---
title: "Importing Self-Signed Certificates into Chrome on Linux"
date: 2014-10-08 04:29:13 +0000
modified: 2026-04-11 16:22:11 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /making-chrome-accept-self-signed-certificates-on-linux/
---

Chrome on Linux uses NSS (Network Security Services) for certificate management. Install the `certutil` utility from your distribution:

**Debian/Ubuntu/Linux Mint:**

``` bash
sudo apt install libnss3-tools
```

**CentOS/Fedora/RHEL:**

``` bash
sudo dnf install nss-tools
```

**Arch Linux:**

``` bash
sudo pacman -S nss
```

## Extract and Import the Certificate

The most reliable approach is to extract the certificate directly from the server and import it into Chrome’s NSS database. This script handles both tasks:

``` bash
#!/bin/bash

if [ $# -lt 1 ]; then
    echo "Usage: $0 <hostname> [port]"
    exit 1
fi

hostname=$1
port=${2:-443}

echo "Fetching certificate from $hostname:$port..."

# Extract the certificate chain
echo Q | openssl s_client -servername "$hostname" -connect "$hostname:$port" -showcerts 2>/dev/null \
    | sed -ne '/BEGIN CERTIFICATE/,/END CERTIFICATE/p' \
    > "/tmp/cert-$hostname.pem"

if [ ! -s "/tmp/cert-$hostname.pem" ]; then
    echo "Error: Failed to retrieve certificate from $hostname"
    exit 1
fi

# Import into NSS database
certutil -d "sql:$HOME/.pki/nssdb" -A -t "P,," -n "$hostname" -i "/tmp/cert-$hostname.pem"

if [ $? -eq 0 ]; then
    echo "Certificate imported successfully for $hostname"
    certutil -d "sql:$HOME/.pki/nssdb" -L -n "$hostname"
else
    echo "Error: Failed to import certificate"
    exit 1
fi

# Cleanup
rm -f "/tmp/cert-$hostname.pem"
```

Save this as `add-cert.sh`, make it executable, and run it:

``` bash
chmod +x add-cert.sh
./add-cert.sh your.internal.site
```

For non-standard ports:

``` bash
./add-cert.sh your.internal.site 8443
```

## Verify the Import

List all imported certificates:

``` bash
certutil -d "sql:$HOME/.pki/nssdb" -L
```

View details for a specific certificate:

``` bash
certutil -d "sql:$HOME/.pki/nssdb" -L -n "your.internal.site"
```

The output shows the certificate’s trust flags. The `P` flag indicates it’s trusted for websites.

## Restart Chrome

Close all Chrome/Chromium instances, including background processes:

``` bash
killall chrome chromium chromium-browser google-chrome 2>/dev/null
```

Wait a moment for all processes to terminate, then reopen the browser. The certificate warning should no longer appear.

## Remove a Certificate

If you need to delete a certificate later:

``` bash
certutil -d "sql:$HOME/.pki/nssdb" -D -n "your.internal.site"
```

## Troubleshooting

**NSS database doesn’t exist**

The `~/.pki/nssdb` directory may not be present on fresh Linux installs. Create and initialize it:

``` bash
mkdir -p ~/.pki/nssdb
certutil -d "sql:$HOME/.pki/nssdb" -N --empty-password
```

**Certificate still shows warnings after import**

Ensure Chrome is completely closed. Background processes can persist in the system tray. Verify with `ps aux | grep chrome` and force-kill if necessary:

``` bash
killall -9 chrome chromium google-chrome 2>/dev/null
```

**Hostname mismatch errors**

Chrome validates the certificate’s Common Name (CN) or Subject Alternative Name (SAN) against the hostname. If they don’t match, the browser warns even after import. Check the certificate’s CN:

``` bash
echo Q | openssl s_client -servername "$hostname" -connect "$hostname:443" 2>/dev/null \
    | openssl x509 -text -noout | grep -A1 "Subject:"
```

If the CN doesn’t match your hostname, you need a certificate with the correct CN or SAN field, or access the site using the hostname in the certificate.

**Certificate chain issues**

If the server uses intermediate certificates, the extraction script captures the full chain. However, some servers don’t send the complete chain. You may need to import the CA certificate separately:

``` bash
# Save the CA cert to a file, then import it
certutil -d "sql:$HOME/.pki/nssdb" -A -t "CT,," -n "ca-cert-name" -i /path/to/ca.pem
```

Use `CT,,` trust flags for CA certificates instead of `P,,`.

## Chromium, Brave, and Other Chromium-Based Browsers

This process works identically for Chromium, Google Chrome, Brave, and Edge. All Chromium-based browsers share the same NSS database, so importing a certificate once makes it available to all of them.

To verify which browsers use your NSS database:

``` bash
certutil -d "sql:$HOME/.pki/nssdb" -L
```

If a certificate appears here, all installed Chromium-based browsers recognize it.
