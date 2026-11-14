---
title: "genkey(1)"
name: "genkey"
section: "1"
letter: "g"
url: "/docs/linux/man/1-genkey/"
description: "genkey – generate SSL certificates and certificate requests"
---

<h2 class="name">NAME</h2>
<p> genkey &#8211; generate SSL certificates and certificate requests </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>genkey</code> [<code>&#8211;test</code>] [<code>&#8211;days&nbsp;<wbr></code><i>count</i>] [[<code>&#8211;genreq</code>] | [<code>&#8211;makeca</code>] | [<code>&#8211;nss</code>] | [<code>&#8211;renew</code>] | [<code>&#8211;cacert</code>]] {<i>hostname</i>}</dl>
<h2>DESCRIPTION</h2>
<p> <code>genkey</code></p>
<dd>is an interactive command-line tool which can be used to generate SSL certificates or Certificate Signing Requests (CSR). Generated certificates are stored in the directory /etc/pki/tls/certs/, and the corresponding private key in /etc/pki/tls/private/. </p>
<p> When using mod_nss the private key is stored in the nss database. Consult the nss.conf file in /etc/httpd/conf.d/ for the location of the database. </p>
<p> <code>genkey</code> will prompt for the size of key desired; whether or not to generate a CSR; whether or not an encrypted private key is desired; the certificate subject DN details. </p>
<p> <code>genkey</code> generates random data for the private key using the truerand library and also by prompting the user for entry of random text. </p>
<p> <code>nss</code> indicates that mod_nss database should be used to store keys and certificates.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;makeca</code></p>
<dl>
<dt>
<dd> Generate a Certificate Authority keypair and certificate.</dl>
<p> <code>&#8211;genreq</code></p>
<dl>
<dt>
<dd> Generate a Certificate Signing Request for an existing private key, which can be submitted to a CA (for example, for renewal).</dl>
<p> <code>&#8211;renew</code></p>
<dl>
<dt>
<dd> Used with &#8211;genreq to indicate a renewal, the existing keypair will be used. Certs and keys must reside in the nss database, therefore &#8211;nss is also required. Pem file based cert renewal is not currently supported.</dl>
<p> <code>&#8211;cacert</code></p>
<dl>
<dt>
<dd> The certificate renewal is for a CA, needed for openssl certs only.</dl>
<p> <code>&#8211;days</code> <i>count</i></p>
<dl>
<dt>
<dd> When generating a self-signed certificate, specify that the number of days for which the certificate is valid be <i>count</i> rather than the default value of 30.</dl>
<p> <code>&#8211;test</code></p>
<dl>
<dt>
<dd> For test purposes only; omit the slow process of generating random data.</dl>
<h2>EXAMPLES</h2>
<p> The following example will create a self-signed certificate and private key for the hostname <a rel="nofollow" href="http://www.example.com">www.example.com</a>: </p>
<dl>
<dt>
<dd>
<pre>
        # genkey --days 120 <a rel="nofollow" href="http://www.example.com">www.example.com</a>
      
</pre>
</dl>
<p> The following example will create a self-signed certificate and private key for the hostname <a rel="nofollow" href="http://www.nssexample.com">www.nssexample.com</a> which will be stored in cert and key in the nss database. If no nickname is given the tool will extract it from mod_nss&#8217;s nss configuration file. </p>
<dl>
<dt>
<dd>
<pre>
        # genkey --days --nss 120 <a rel="nofollow" href="http://www.nssexample.com">www.nssexample.com</a>
      
</pre>
</dl>
<p> The following example will generate a certificate signing request for a new mod_nss style cert specified by its nickname, Server-Cert: </p>
<dl>
<dt>
<dd>
<pre>
        # genkey --genreq --nss --days 120 Server-Cert
      
</pre>
</dl>
<p> The following example will generate a certificate signing request for the renewal of an existing mod_nss cert specified by its nickname, Server-Cert: </p>
<dl>
<dt>
<dd>
<pre><code>
#genkey-- genreq-- renew-- nss-- days 120 Server - Cert
</code></pre>
</dl>
<h2>FILES</h2>
<p> /etc/pki/tls/openssl.cnf</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-certwatch/">certwatch</a>(1), <a href="/docs/linux/man/1-keyrand/">keyrand</a>(1) </p>
<h2>Index</h2>
