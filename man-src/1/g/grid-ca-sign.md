---

title: "grid-ca-sign(1)"
name: "grid-ca-sign"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grid-ca-sign/"
description: "grid-ca-sign – Sign a certificate with a SimpleCA for use on a grid"
---

<p> <code>grid-ca-sign</code> -in <i>REQUEST</i> -out <i>CERTIFICATE</i> [OPTIONS] </p>
<p> <code>grid-ca-sign</code> [ -help | -h | -usage | -version | -versions ]</p>
<p> The <code>grid-ca-sign</code> program signs a certificate based on a request file with a CA certificate created by <code>grid-ca-create</code>. The new certificate is written to a file. If the CA has already signed a certificate with the same subject name as contained in the certificate request, it will refuse to sign the new request unless the <i>-force</i> option is provided on the command-line. </p>
<p> If run as a privileged user, <code>grid-ca-sign</code> uses the CA certificate and sign the certificate. For a non-privileged user, <code>grid-ca-sign</code> uses the CA certificate and configuration located in $HOME/.globus/simpleCA. The <code>grid-ca-sign</code> program an use a different CA configuration and certificate by using the <i>-dir</i> option.</p>
<h2>OPTIONS</h2>
<p> The full set of command-line options to <code>grid-ca-sign</code> follows. In addition to these, unknown options will be passed to the <code>openssl</code> command when creating the self-signed certificate. </p>
<p> <code>-help, -h, -usage</code></p>
<dl>
<dt>
</dt><dd> Display the command-line options to <code>grid-ca-sign</code> and exit.</dd></dl>
<p> <code>-version, -versions</code></p>
<dl>
<dt>
</dt><dd> Display the version number of the <code>grid-ca-sign</code> command. The second form includes details about the package containing <code>grid-ca-sign</code>.</dd></dl>
<p> <code>-in </code><i>REQUEST</i></p>
<dl>
<dt>
</dt><dd> Sign the request contained in the <i>REQUEST</i> file.</dd></dl>
<p> <code>-out </code><i>CERTIFICATE</i></p>
<dl>
<dt>
</dt><dd> Write the signed request to the <i>CERTIFICATE</i> file.</dd></dl>
<p> <code>-force</code></p>
<dl>
<dt>
</dt><dd> Revoke any previously issued certificate with the same subject name as in the certificate request and issue a new certificate. Otherwise, <code>grid-ca-sign</code> will refuse to sign the request.</dd></dl>
<p> <code>-dir </code><i>DIRECTORY</i></p>
<dl>
<dt>
</dt><dd> Sign the certificate using the Simple CA certificate and configuration located in <i>DIRECTORY</i> instead of the default.</dd></dl>
<p> <code>-openssl-help</code></p>
<dl>
<dt>
</dt><dd> Print the command-line options available for the <code>openssl ca</code> command.</dd></dl>
<h2>EXAMPLES</h2>
<p> Sign a certificate request using the simple CA in $HOME/SimpleCA&#8217; </p>
<dl>
<dt>
</dt><dd>
<pre>
% *grid-ca-sign* \
    -in usercert_request.pem \
    -out usercert.pem \
    -dir $HOME/SimpleCA
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
To sign the request please enter the password for the CA key:
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
The new signed certificate is at: /home/juser/.globus/simpleCA/newcerts/01.pem
</pre>
</dd></dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variables affect the execution of <code>grid-ca-sign</code>: </p>
<p> GLOBUS_LOCATION</p>
<dl>
<dt>
</dt><dd> Non-standard installation path of the Globus Toolkit.</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-grid-cert-request/">grid-cert-request</a>(1), <a href="/docs/linux/man/1-grid-ca-create/">grid-ca-create</a>(1), grid-default-ca(1), <a href="/docs/linux/man/1-grid-ca-package/">grid-ca-package</a>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright &#169; 1999-2014 University of Chicago </p>
