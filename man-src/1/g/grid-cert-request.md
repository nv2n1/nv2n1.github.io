---
title: "grid-cert-request(1)"
name: "grid-cert-request"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grid-cert-request/"
description: "grid-cert-request – Generate a X.509 certificate request and corresponding private key"
---

<h2 class="name">NAME</h2>
<p> grid-cert-request &#8211; Generate a X.509 certificate request and corresponding private key </p>
<h2>SYNOPSIS</h2>
<p> <code>grid-cert-request</code> -help | -h | -? | -usage | -version-versions </p>
<p> <code>grid-cert-request</code> [OPTIONS]</p>
<h2>DESCRIPTION</h2>
<p> The <code>grid-cert-request</code> program generates an X.509 Certificate Request and corresponding private key for the specified name, host, or service. It is intended to be used with a CA implemented using the <code>globus_simple_ca</code> package. </p>
<p> The default behavior of <code>grid-cert-request</code> is to generate a certificate request and private key for the user running the command. The subject name is derived from the gecos information in the local system&#8217;s password database, unless the <i>-commonname</i>, <i>-cn</i>, or <i>-host</i> command-line options are used. </p>
<p> By default, <code>grid-cert-request</code> writes user certificate requests and keys to the $HOME/.globus directory, and host and service certificate requests and keys to /etc/grid-security. This can be overridden by using the <i>-dir</i> command-line option.</p>
<h2>OPTIONS</h2>
<p> The full set of command-line options to <code>grid-cert-request</code> are: </p>
<p> <code>-help, -h, -?, -usage</code></p>
<dl>
<dt>
<dd> Display the command-line options to <code>grid-cert-request</code> and exit.</dl>
<p> <code>-version, -versions</code></p>
<dl>
<dt>
<dd> Display the version number of the <code>grid-cert-request</code> command. The second form includes more details.</dl>
<p> <code>-cn </code><i>NAME</i><code>, -commonname </code><i>NAME</i></p>
<dl>
<dt>
<dd> Create a certificate request with the common name component of the subject set to <i>NAME</i>. This is used to create user identity certificates.</dl>
<p> <code>-dir </code><i>DIRECTORY</i></p>
<dl>
<dt>
<dd> Write the certificate request and key to files in the directory specified by <i>DIRECTORY</i>.</dl>
<p> <code>-prefix </code><i>PREFIX</i></p>
<dl>
<dt>
<dd> Use the string <i>PREFIX</i> as the base name of the certificate, certificate_request, and key files instead of the default. For a user certificate request, this would mean creating files $HOME/.globus/&#8217;PREFIX&#8217;cert_request.pem, $HOME/.globus/&#8217;PREFIX&#8217;cert.pem, and $HOME/.globus/&#8217;PREFIX&#8217;key.pem.</dl>
<p> <code>-ca </code><i>CA-HASH</i></p>
<dl>
<dt>
<dd> Use the certificate request configuration for the CA with the name hash <i>CA-HASH</i> instead of the default CA chosen by running <code>grid-default-ca</code>.</dl>
<p> <code>-verbose</code></p>
<dl>
<dt>
<dd> Keep the output from the OpenSSL certificate request command visible after it completes, instead of clearing the screen.</dl>
<p> <code>-interactive, -int</code></p>
<dl>
<dt>
<dd> Prompt for each component of the subject name of the request, instead of generating the common name from other command-line options. Note that CAs may not sign certificates for subject names that don&#8217;t match their signing policies.</dl>
<p> <code>-force</code></p>
<dl>
<dt>
<dd> Overwrite any existing certificate request and private key with a new one.</dl>
<p> <code>-nopw, -nodes, -nopassphrase</code></p>
<dl>
<dt>
<dd> Create an unencrypted private key for the certificate instead of prompting for a passphrase. This is the default behavior for host or service certificates, but not recommended for user certificates.</dl>
<p> <code>-host </code><i>FQDN</i></p>
<dl>
<dt>
<dd> Create a certificate request for use on a particular host. This option also causes the private key associated with the certificate request to be unencrypted. The <i>FQDN</i> argument to this option should be the fully qualified domain name of the host that will use this certificate. The subject name of the certificate will be derived from the <i>FQDN</i> and the service option if specified by the <i>-service</i> command-line option. If the host for the certificate has multiple names, then use either the <i>-dns</i> or <i>-ip</i> command-line options to add alternate names or addresses to the certificates.</dl>
<p> <code>-service </code><i>SERVICE</i></p>
<dl>
<dt>
<dd> Create a certificate request for a particular service on a host. The subject name of the certificate will be derived from the <i>FQDN</i> passed as the argument to the <i>-host</i> command-line option and the <i>SERVICE</i> string.</dl>
<p> <code>-dns </code><i>FQDN,&#8230;</i></p>
<dl>
<dt>
<dd> Create a certificate request containing a subjectAltName extension containing one or more host names. This is used when a certificate may be used by multiple virtual servers or if a host has different names when contacted within or outside a private network. Multiple DNS names can be included in the extension by separating then with a comma.</dl>
<p> <code>-ip </code><i>IP-ADDRESS,&#8230;</i></p>
<dl>
<dt>
<dd> Create a certificate request containing a subjectAltName extension containing the IP addresses named by the <i>IP-ADDRESS</i> strings. This is used when a certificate may be used by services listening on multiple networks. Multiple IP addresses can be included in the extension by separating then with a comma.</dl>
<h2>EXAMPLES</h2>
<p> Create a user certificate request: % <code>grid-cert-request</code> A certificate request and private key is being created. You will be asked to enter a PEM pass phrase. This pass phrase is akin to your account password, and is used to protect your key file. If you forget your pass phrase, you will need to obtain a new certificate. A private key and a certificate request has been generated with the subject: </p>
<dl>
<dt>
<dd>
<pre>
/O=org/OU=example/OU=grid/CN=Joe User
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
If the CN=Joe User is not appropriate, rerun this
script with the -force -cn &quot;Common Name&quot; options.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Your private key is stored in /home/juser/.globus/userkey.pem
Your request is stored in /home/juser/.globus/usercert_request.pem
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Please e-mail the request to the Example CA ca [at] grid.example.org
You may use a command similar to the following:
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
cat /home/juser/.globus/usercert_request.pem | mail ca [at] grid.example.org
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Only use the above if this machine can send AND receive e-mail. if not, please
mail using some other method.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
    Your certificate will be mailed to you within two working days.
If you receive no response, contact Example CA at ca [at] grid.example.org
</pre>
</dl>
<p> Create a host certificate for a host with two names. </p>
<dl>
<dt>
<dd>
<pre>
% *grid-cert-request -host grid.example.org -dns grid.example.org,grid-internal.example.org*
A private host key and a certificate request has been generated
with the subject:
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
/O=org/OU=example/OU=grid/CN=host/grid.example.org
</pre>
</dl>
<dl>
<dt>
<dd>
<pre><code>
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
</code></pre>
</dl>
<dl>
<dt>
<dd>
<pre>
The private key is stored in /etc/grid-security/hostkey.pem
The request is stored in /etc/grid-security/hostcert_request.pem
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Please e-mail the request to the Example CA ca [at] grid.example.org
You may use a command similar to the following:
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
cat /etc/grid-security/hostcert_request.pem | mail ca [at] grid.example.org
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Only use the above if this machine can send AND receive e-mail. if not, please
mail using some other method.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Your certificate will be mailed to you within two working days.
If you receive no response, contact Example CA at
ca [at] grid.example.org
</pre>
</dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variables affect the execution of <code>grid-cert-request</code>: </p>
<p> <code>X509_CERT_DIR</code></p>
<dl>
<dt>
<dd> Path to the directory containing SSL configuration files for generating certificate requests.</dl>
<p> <code>GRID_SECURITY_DIR</code></p>
<dl>
<dt>
<dd> Path to the directory containing SSL configuration files for generating certificate requests. This value is used if X509_CERT_DIR is not set.</dl>
<p> <code>GLOBUS_LOCATION</code></p>
<dl>
<dt>
<dd> Path to the directory containing the Globus Toolkit. This is searched if neither the X509_CERT_DIR nor the GRID_SECURITY_DIR environment variables are set.</dl>
<h2>FILES</h2>
<p> <code>$HOME/.globus/usercert_request.pem</code></p>
<dl>
<dt>
<dd> Default path to write a user certificate request.</dl>
<p> <code>$HOME/.globus/usercert.pem</code></p>
<dl>
<dt>
<dd> Default path to write a user certificate.</dl>
<p> <code>$HOME/.globus/userkey.pem</code></p>
<dl>
<dt>
<dd> Default path to write a user private key.</dl>
<p> <code>/etc/grid-security/hostcert_request.pem</code></p>
<dl>
<dt>
<dd> Default path to write a host certificate request.</dl>
<p> <code>/etc/grid-security/hostcert.pem</code></p>
<dl>
<dt>
<dd> Default path to write a host certificate.</dl>
<p> <code>/etc/grid-security/hostkey.pem</code></p>
<dl>
<dt>
<dd> Default path to write a host private key.</dl>
<p> <i>TRUSTED-CERT-DIR</i><code>/globus-user-ssl.conf, </code><i>TRUSTED-CERT-DIR</i><code>/globus-user-ssl.conf.</code><i>CA-HASH</i></p>
<dl>
<dt>
<dd> SSL configuration file for requesting a user certificate. The first form is the default location, the second form is used when the <i>-ca</i> command-line option is specified.</dl>
<p> <i>TRUSTED-CERT-DIR</i><code>/globus-host-ssl.conf, </code><i>TRUSTED-CERT-DIR</i><code>/globus-host-ssl.conf.</code><i>CA-HASH</i></p>
<dl>
<dt>
<dd> SSL configuration file for requesting a host or service certificate. The first form is the default location, the second form is used when the <i>-ca</i> command-line option is specified.</dl>
<h2>AUTHOR</h2>
<p> Copyright &#169; 1999-2014 University of Chicago </p>
<h2>Index</h2>
