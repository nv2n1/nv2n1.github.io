---
title: "sudo_logsrvd(8)"
name: "sudo_logsrvd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sudo_logsrvd/"
description: "sudo_logsrvd – sudo event and I/O log server"
---

<p>Sudo 1.9.9</p>
<h2>Name</h2>
<p><code>sudo_logsrvd</code> &#8211; sudo event and I/O log server</p>
<h2>Synopsis</h2>
<p><code>sudo_logsrvd</code> [-<code>hnV</code> ] [-<code>f </code><i>file</i> ] [-<code>R </code><i>percentage</i> ]</p>
<h2>Description</h2>
<p><code>sudo_logsrvd</code> is a high-performance log server that accepts event and I/O logs from <code>sudo</code> It can be used to implement centralized logging of <code>sudo</code> logs. The server has two modes of operation: local and relay. By default, <code>sudo_logsrvd</code> stores the logs locally but it can also be configured to relay them to another server that supports the sudo_logsrv.proto5 protocol. </p>
<p> When not relaying, event log entries may be logged either via <a href="/docs/linux/man/3-syslog/">syslog</a>(3) or to a local file. I/O Logs stored locally by <code>sudo_logsrvd</code> can be replayed via the <a href="/docs/linux/man/8-sudoreplay/">sudoreplay</a>(8) utility in the same way as logs generated directly by the <code>sudoers</code> plugin. </p>
<p> The server also supports restarting interrupted log transfers. To distinguish completed I/O logs from incomplete ones, the I/O log timing file is set to be read-only when the log is complete. </p>
<p> Configuration parameters for <code>sudo_logsrvd</code> may be specified in the sudo_logsrvd.conf5 file or the file specified via the &#8211;<code>f</code> option. </p>
<p> <code>sudo_logsrvd</code> rereads its configuration file when it receives SIGHUP and writes server state to the debug file (if one is configured) when it receives SIGUSR1. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-f </code><i>file , &#8211;</i><code>-file = </code><i>file</i></p>
<dd>Read configuration from <i>file</i> instead of the default, /etc/sudo_logsrvd.conf</p>
<dt><code>-h , -help</code></p>
<dd>Display a short help message to the standard output and exit.</p>
<dt><code>-n , -no-fork</code></p>
<dd>Run <code>sudo_logsrvd</code> in the foreground instead of detaching from the terminal and becoming a daemon.</p>
<dt><code>-R </code><i>percentage , &#8211;</i><code>-random-drop = </code><i>percentage</i></p>
<dd>For each message, there is a <i>percentage</i> chance that the server will drop the connection. This is only intended for debugging the ability of a client to restart a connection.</p>
<dt><code>-V , -version</code></p>
<dd>Print the <code>sudo_logsrvd</code> version and exit.</dl>
<h3>Securing server connections</h3>
<p>The I/O log data sent to <code>sudo_logsrvd</code> may contain sensitive information such as passwords and should be secured using Transport Layer Security (TLS). Doing so requires having a signed certificate on the server and, if <i>tls_checkpeer</i> is enabled in sudo_logsrvd.conf5, a signed certificate on the client as well. </p>
<p> The certificates can either be signed by a well-known Certificate Authority (CA), or a private CA can be used. Instructions for creating a private CA are included below in the Sx EXAMPLES section.</p>
<h3>Debugging sudo_logsrvd</h3>
<p><code>sudo_logsrvd</code> supports a flexible debugging framework that is configured via <code>Debug</code> lines in the sudo.conf5 file. </p>
<p> For more information on configuring sudo.conf5, please refer to its manual.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/sudo.conf </code></p>
<dd>Sudo front-end configuration</p>
<dt><code>/etc/sudo_logsrvd.conf </code></p>
<dd>Sudo log server configuration file</p>
<dt><code>/var/log/sudo_logsrvd/incoming </code></p>
<dd>Directory where new journals are stored when the <i>store_first relay</i> setting is enabled.</p>
<dt><code>/var/log/sudo_logsrvd/outgoing </code></p>
<dd>Directory where completed journals are stored when the <i>store_first relay</i> setting is enabled.</p>
<dt><code>/var/log/sudo-io </code></p>
<dd>Default I/O log file location</p>
<dt><code>/run/sudo/sudo_logsrvd.pid </code></p>
<dd>Process ID file for <code>sudo_logsrvd</code></dl>
<h2>Examples</h2>
<h3>Creating self-signed certificates</h3>
<p>Unless you are using certificates signed by a well-known Certificate Authority (or a local enterprise CA), you will need to create your own CA that can sign the certificates used by <code>sudo_logsrvd,</code> <code>sudo_sendlog</code> and the <code>sudoers</code> plugin. The following steps use the <a href="/docs/linux/man/1-openssl/">openssl</a>(1) command to create keys and certificates.</p>
<h3>Initial setup</h3>
<p>First, we need to create a directory structure to store the files for the CA. We&#8217;ll create a new directory hierarchy in /etc/ssl/sudo for this purpose. </p>
<blockquote>
<pre># mkdir /etc/ssl/sudo
# cd /etc/ssl/sudo
# mkdir certs csr newcerts private
# chmod 700 private
# touch index.txt
# echo 1000 &gt; serial</pre>
</blockquote>
<p> The serial and index.txt files are used to keep track of signed certificates. </p>
<p> Next, we need to make a copy of the openssl.conf file and customize it for our new CA. The path to openssl.cnf is system-dependent but /etc/ssl/openssl.cnf is the most common location. You will need to adjust the example below if it has a different location on your system. </p>
<blockquote>
<pre># cp /etc/ssl/openssl.cnf .</pre>
</blockquote>
<p> Now edit the openssl.cnf file in the current directory and make sure it contains &#8220;ca&#8221; and &#8220;CA_default&#8221; sections. Those sections should include the following settings: </p>
<blockquote>
<pre>[ ca ]
default_ca = CA_default
[ CA_default ]
dir = /etc/ssl/sudo
certs = $dir/certs
database = $dir/index.txt
certificate = $dir/cacert.pem
serial = $dir/serial</pre>
</blockquote>
<p> If your openssl.conf file already has a &#8220;CA_default&#8221; section, you may only need to modify the &#8220;dir&#8221; setting.</p>
<h3>Creating the CA key and certificate</h3>
<p>In order to create and sign our own certificates, we need to create a private key and a certificate for the root of the CA. First, create the private key and protect it with a pass phrase: </p>
<blockquote>
<pre># openssl genrsa -aes256 -out private/cakey.pem 4096
# chmod 400 private/cakey.pem</pre>
</blockquote>
<p> Next, generate the root certificate, using appropriate values for the site-specific fields: </p>
<blockquote>
<pre># openssl req -config openssl.cnf -key private/cakey.pem \
 -new -x509 -days 7300 -sha256 -extensions v3_ca \
 -out cacert.pem
Enter pass phrase for private/cakey.pem:
You are about to be asked to enter information that will be
incorporated into your certificate request.
What you are about to enter is what is called a Distinguished Name
or a DN.
There are quite a few fields but you can leave some blank.
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:Colorado
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:sudo
Organizational Unit Name (eg, section) []:sudo Certificate Authority
Common Name (e.g., server FQDN or YOUR name) []:sudo Root CA
Email Address []:
# chmod 444 cacert.pem</pre>
</blockquote>
<p> Finally, verify the root certificate: </p>
<blockquote>
<pre># openssl x509 -noout -text -in cacert.pem</pre>
</blockquote>
<h3>Creating and signing certificates</h3>
<p>The server and client certificates will be signed by the previously created root CA. Usually, the root CA is not used to sign server/client certificates directly. Instead, intermediate certificates are created and signed with the root CA and the intermediate certs are used to sign CSRs (Certificate Signing Request). In this example we&#8217;ll skip this part for simplicity&#8217;s sake and sign the CSRs with the root CA. </p>
<p> First, generate the private key without a pass phrase. </p>
<blockquote>
<pre># openssl genrsa -out private/logsrvd_key.pem 2048
# chmod 400 private/logsrvd_key.pem</pre>
</blockquote>
<p> Next, create a certificate signing request (CSR) for the server&#8217;s certificate. The organization name must match the name given in the root certificate. The common name should be either the server&#8217;s IP address or a fully qualified domain name. </p>
<blockquote>
<pre># openssl req -config openssl.cnf -key private/logsrvd_key.pem -new \
 -sha256 -out csr/logsrvd_csr.pem
Enter pass phrase for private/logsrvd_key.pem:
You are about to be asked to enter information that will be
incorporated into your certificate request.
What you are about to enter is what is called a Distinguished Name
or a DN.
There are quite a few fields but you can leave some blank.
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:Colorado
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:sudo
Organizational Unit Name (eg, section) []:sudo log server
Common Name (e.g., server FQDN or YOUR name) []:logserver.example.com
Email Address []:
Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:</pre>
</blockquote>
<p> Now sign the CSR that was just created: </p>
<blockquote>
<pre># openssl ca -config openssl.cnf -days 375 -notext -md sha256 \
 -in csr/logsrvd_csr.pem -out certs/logsrvd_cert.pem
Using configuration from openssl.cnf
Enter pass phrase for ./private/cakey.pem:
Check that the request matches the signature
Signature ok
Certificate Details:
 Serial Number: 4096 (0x1000)
 Validity
 Not Before: Nov 11 14:05:05 2019 GMT
 Not After : Nov 20 14:05:05 2020 GMT
 Subject:
 countryName = US
 stateOrProvinceName = Colorado
 organizationName = sudo
 organizationalUnitName = sudo log server
 commonName = logserve.example.com
 X509v3 extensions:
 X509v3 Basic Constraints:
 CA:FALSE
 Netscape Comment:
 OpenSSL Generated Certificate
 X509v3 Subject Key Identifier:
 4C:50:F9:D0:BE:1A:4C:B2:AC:90:76:56:C7:9E:16:AE:E6:9E:E5:B5
 X509v3 Authority Key Identifier:
 keyid:D7:91:24:16:B1:03:06:65:1A:7A:6E:CF:51:E9:5C:CB:7A:95:3E:0C
Certificate is to be certified until Nov 20 14:05:05 2020 GMT (375 days)
Sign the certificate? [y/n]:y
1 out of 1 certificate requests certified, commit? [y/n]y
Write out database with 1 new entries
Data Base Updated</pre>
</blockquote>
<p> Finally, verify the new certificate: </p>
<blockquote>
<pre># openssl verify -CAfile cacert.pem certs/logsrvd_cert.pem
certs/logsrvd_cert.pem: OK</pre>
</blockquote>
<p> The /etc/ssl/sudo/certs directory now contains a signed and verified certificate for use with <code>sudo_logsrvd</code> </p>
<p> To generate a client certificate, repeat the process above using a different file name.</p>
<h3>Configuring sudo_logsrvd to use TLS</h3>
<p>To use TLS for client/server communication, both <code>sudo_logsrvd</code> and the <code>sudoers</code> plugin need to be configured to use TLS. Configuring <code>sudo_logsrvd</code> for TLS requires the following settings, assuming the same path names used earlier: </p>
<blockquote>
<pre># Listen on port 30344 for TLS connections to any address.
listen_address = *:30344(tls)
# Path to the certificate authority bundle file in PEM format.
tls_cacert = /etc/ssl/sudo/cacert.pem
# Path to the server's certificate file in PEM format.
tls_cert = /etc/ssl/sudo/certs/logsrvd_cert.pem
# Path to the server's private key file in PEM format.
tls_key = /etc/ssl/sudo/private/logsrvd_key.pem</pre>
</blockquote>
<p> The root CA cert (cacert.pem ) must be installed on the system running <code>sudo_logsrvd.</code> If peer authentication is enabled on the client, a copy of cacert.pem must be present on the client system too.</p>
<h2>See Also</h2>
<p>sudo.conf5, sudo_logsrvd.conf5, <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5), <a href="/docs/linux/man/8-sudo/">sudo</a>(8), sudo_sendlog8, <a href="/docs/linux/man/8-sudoreplay/">sudoreplay</a>(8)</p>
<h2>Authors</h2>
<p>Many people have worked on <code>sudo</code> over the years; this version consists of code written primarily by: </p>
<blockquote><p> An Todd C. Miller </p></blockquote>
<p> See the CONTRIBUTORS file in the <code>sudo</code> distribution (<a rel="nofollow" href="https://www.sudo.ws/contributors.html)">https://www.sudo.ws/contributors.html)</a> for an exhaustive list of people who have contributed to <code>sudo</code></p>
<h2>Bugs</h2>
<p>If you feel you have found a bug in <code>sudo_logsrvd,</code> please submit a bug report at <a rel="nofollow" href="https://bugzilla.sudo.ws/">https://bugzilla.sudo.ws/</a></p>
<h2>Support</h2>
<p>Limited free support is available via the sudo-users mailing list, see <a rel="nofollow" href="https://www.sudo.ws/mailman/listinfo/sudo-users">https://www.sudo.ws/mailman/listinfo/sudo-users</a> to subscribe or search the archives.</p>
<h2>Disclaimer</h2>
<p><code>sudo_logsrvd</code> is provided &#8220;AS IS&#8221; and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. See the LICENSE file distributed with <code>sudo</code> or <a rel="nofollow" href="https://www.sudo.ws/license.html">https://www.sudo.ws/license.html</a> for complete details.</p>
