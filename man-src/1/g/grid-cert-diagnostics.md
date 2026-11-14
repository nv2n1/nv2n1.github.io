---
title: "grid-cert-diagnostics(1)"
name: "grid-cert-diagnostics"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grid-cert-diagnostics/"
description: "grid-cert-diagnostics – Print diagnostic information about certificates and keys"
---

<h2 class="name">NAME</h2>
<p> grid-cert-diagnostics &#8211; Print diagnostic information about certificates and keys </p>
<h2>SYNOPSIS</h2>
<p> <code>grid-cert-diagnostics</code> [ -h | -help ] </p>
<p> <code>grid-cert-diagnostics</code> [ -p ] [ -n ] [ -c CERTIFICATE [-H HOSTNAME] [-m { STRICT_GT2 | HYBRID | STRICT_RFC2818 }]] </p>
<p> <code>grid-cert-diagnostics</code> [ -s HOST[:PORT] | -g HOST[:PORT] ] [-m { STRICT_GT2 | HYBRID | STRICT_RFC2818 }]</p>
<h2>DESCRIPTION</h2>
<p> The <code>grid-cert-diagnostics</code> program displays information about the current user&#8217;s security environment, including information about security-related environment variables, security directory search path, personal key and certificates, and trusted certificates. It is intended to provide information to help diagnose problems using GSIC. </p>
<p> By default, <code>grid-cert-diagnostics</code> prints out information regarding the environment and trusted certificate directory. If the <i>-p</i> command-line option is used, then additional information about the current user&#8217;s default certificate and key will be printed. </p>
<p> The <code>grid-cert-diagnostics</code> program can also attempt do diagnose problems connecting to remote GridFTP or SSL-based services.</p>
<h2>OPTIONS</h2>
<p> The full set of command-line options to <code>grid-cert-diagnostics</code> consists of: </p>
<p> <code>-h, -help</code></p>
<dl>
<dt>
<dd> Display a help message and exit.</dl>
<p> <code>-p</code></p>
<dl>
<dt>
<dd> Display information about the personal certificate and key that is the current user&#8217;s default credential.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> Check time synchronization with the ntpdate command.</dl>
<p> <code>-c </code><i>CERTIFICATE</i><code>, -c </code><i>&#8211;</i></p>
<dl>
<dt>
<dd> Check the validity of the certificate in the file named by <i>CERTIFICATE</i> or standard input if the parameter to <i>-c</i> is <i>&#8211;</i>.</dl>
<p> <code>-H </code><i>HOSTNAME</i></p>
<dl>
<dt>
<dd> When using the <code>-c</code> option above, check that the certificate&#8217;s identity matches HOSTNAME.</dl>
<p> <code>-m </code><i>STRICT_GT2 | HYBRID | STRICT_RFC2818</i></p>
<dl>
<dt>
<dd> Use the specified mode when comparing host certificate names.</dl>
<p> <code>-s </code><i>HOST[:PORT]</i></p>
<dl>
<dt>
<dd> Connect to the service listening on <i>HOST:PORT</i> and initiate the TLS protocol. Diagnostics will be printed containing the TLS / SSL protocol version and available cipher list. The certificate chain will be verified, and certificate subject name, issuer name, and subjectAltName extensions will be printed. If the <i>:PORT</i> is omitted, the default of <i>443</i> is used.</dl>
<p> <code>-g </code><i>HOST[:PORT]</i></p>
<dl>
<dt>
<dd> Similar to the <i>-s</i> option, but use the GridFTP protocol. The initial GridFTP banner response is included in the diagnostic output. If the <i>:PORT</i> is omitted, the default of <i>2811</i> is used.</dl>
<h2>EXAMPLES</h2>
<p> In this example, we see the default mode of checking the default security environment for the system, without processing the user&#8217;s key and certificate. Note the user receives a warning about a cog.properties and about an expired CA certificate. </p>
<dl>
<dt>
<dd>
<pre>
% grid-cert-diagnostics
</pre>
</dl>
<dl>
<dt>
<dd>
<pre><code>
Checking Environment Variables == == == == == == == == == == == == == == ==
    Checking if X509_CERT_DIR is set... no
        Checking if X509_USER_CERT is set... no
            Checking if X509_USER_KEY is set... no
                Checking if X509_USER_PROXY is set... no
</code></pre>
</dl>
<dl>
<dt>
<dd>
Checking Security Directories<br />
=======================<br />
Determining trusted cert path&#8230; /etc/grid-security/certificates<br />
Checking for cog.properties&#8230; found<br />
    WARNING: If the cog.properties file contains security properties,<br />
             Java apps will ignore the security paths described in the GSI<br />
             documentation
</dl>
<dl>
<dt>
<dd>
Checking trusted certificates&#8230;<br />
================================<br />
Getting trusted certificate list&#8230;<br />
Checking CA file /etc/grid-security/certificates/1c4f4c48.0&#8230; ok<br />
Verifying certificate chain for &#8220;/etc/grid-security/certificates/1c3f2ca8.0&#8243;&#8230; ok<br />
Checking CA file /etc/grid-security/certificates/9d8788eb.0&#8230; ok<br />
Verifying certificate chain for &#8220;/etc/grid-security/certificates/9d8753eb.0&#8243;&#8230; failed<br />
    globus_credential: Error verifying credential: Failed to verify credential<br />
    globus_gsi_callback_module: Could not verify credential<br />
    globus_gsi_callback_module: The certificate has expired:<br />
    Credential with subject: /DC=org/DC=example/OU=grid/CN=CA has expired.
</dl>
<p> In this example, we show a user with a mismatched private key and certificate: </p>
<dl>
<dt>
<dd>
<pre>
% grid-cert-diagnostics -p
</pre>
</dl>
<dl>
<dt>
<dd>
Checking Environment Variables == == == == == == == == == == == == == == ==<br />
    Checking if X509_CERT_DIR is set&#8230; no<br />
        Checking if X509_USER_CERT is set&#8230; no<br />
            Checking if X509_USER_KEY is set&#8230; no<br />
                Checking if X509_USER_PROXY is set&#8230; no
</dl>
<dl>
<dt>
<dd>
Checking Security Directories<br />
=======================<br />
Determining trusted cert path&#8230; /etc/grid-security/certificates<br />
Checking for cog.properties&#8230; not found
</dl>
<dl>
<dt>
<dd>
<pre><code>
Checking Default Credentials == == == == == == == == == == == == == == ==
    Determining certificate and key file names... ok
        Certificate Path : "/home/juser/.globus/usercert.pem" Key Path : "/home/juser/.globus/userkey.pem" Reading certificate... ok
                                                                             Reading private key... ok
                                                                                 Checking Certificate Subject... "/O=Grid/OU=Example/OU=User/CN=Joe User" Checking cert... ok
                                                                                     Checking key... ok
                                                                                         Checking that certificate contains an RSA key... ok
                                                                                             Checking that private key is an RSA key... ok
                                                                                                 Checking that public and private keys have the same modulus... failed
                                                                                                     Private key modulus : D294849E37F048C3B5ACEEF2CCDF97D88B679C361E29D5CB5 219C3E948F3E530CFC609489759E1D751F0ACFF0515A614276A0F4C11A57D92D7165B8 FA64E3140155DE448D45C182F4657DA13EDA288423F5B9D169DFF3822EFD81EB2E6403
                                                                                                                               CE3CB4CCF96B65284D92592BB1673A18354DA241B9AFD7F494E54F63A93E15DCAE2
                                                                                                                                   Public key modulus : C002C7B329B13BFA87BAF214EACE3DC3D490165ACEB791790 600708C544175D9193C9BAC5AED03B7CB49BB6AE6D29B7E635FAC751E9A6D1CEA98022 6F1B63002902D6623A319E4682E7BFB0968DCE962CF218AAD95FAAD6A0BA5C42AA9AAF 7FDD32B37C6E2B2FF0E311310AA55FFB9EAFDF5B995C7D9EEAD8D5D81F3531E0AE5 Certificate and and private key don't match
</code></pre>
</dl>
<h2>AUTHOR</h2>
<p> Copyright &#169; 1999-2015 University of Chicago </p>
<h2>Index</h2>
