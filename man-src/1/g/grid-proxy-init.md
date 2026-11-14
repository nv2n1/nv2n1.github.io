---
title: "grid-proxy-init(1)"
name: "grid-proxy-init"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grid-proxy-init/"
description: "grid-proxy-init – Generate a new proxy certificate"
---

<h2 class="name">NAME</h2>
<p> grid-proxy-init &#8211; Generate a new proxy certificate </p>
<h2>SYNOPSIS</h2>
<p> <code>grid-proxy-init</code> -help | -usage | -version </p>
<p> <code>grid-proxy-init</code> [OPTIONS]</p>
<h2>DESCRIPTION</h2>
<p> The <code>grid-proxy-init</code> program generates X.509 proxy certificates derived from the currently available certificate files. By default, this command generates a &lt;ulink url=&quot;<a rel="nofollow" href="http://www.ietf.org/rfc/rfc3820.txt">http://www.ietf.org/rfc/rfc3820.txt</a>&quot;&gt;RFC 3820&lt;/ulink&gt; Proxy Certificate with a 1024 bit key, valid for 12 hours, in a file named /tmp/x509up_u&#8217;UID&#8217;. Command-line options and environment variables can modify the format, strength, lifetime, and location of the generated proxy certificate. </p>
<p> X.509 proxy certificates are short-lived certificates, signed usually by a user&#8217;s identity certificate or another proxy certificate. The key associated with a proxy certificate is unencrypted, so applications can authenticate using a proxy identity without providing a pass phrase. </p>
<p> Proxy certificates provide a convenient alternative to constantly entering passwords, but are also less secure than the user&#8217;s normal security credential. Therefore, they should always be user-readable only (this is enforced by the GSI libraries), and should be deleted after they are no longer needed. </p>
<p> This version of <code>grid-proxy-init</code> supports three different proxy formats: the old proxy format used in early releases of the Globus Toolkit up to version 2.4.x, an IETF draft version of X.509 Proxy Certificate profile used in Globus Toolkit 3.0.x and 3.2.x, and the RFC 3820 profile used in Globus Toolkit Version 4.0.x and 4.2.x. By default, this version of <code>grid-proxy-init</code> creates an RFC 3820 compliant proxy. To create a proxy compatible with older versions of the Globus Toolkit, use the <i>-old</i> or <i>-draft</i> command-line options.</p>
<h2>OPTIONS</h2>
<p> The full set of command-line options to <code>grid-proxy-init</code> are: </p>
<p> <code>-help, -usage</code></p>
<dl>
<dt>
<dd> Display the command-line options to <code>grid-proxy-init</code>.</dl>
<p> <code>-version</code></p>
<dl>
<dt>
<dd> Display the version number of the <code>grid-proxy-init</code> command.</dl>
<p> <code>-debug</code></p>
<dl>
<dt>
<dd> Display information about the path to the certificate and key used to generate the proxy certificate, the path to the trusted certificate directory, and verbose error messages.</dl>
<p> <code>-q</code></p>
<dl>
<dt>
<dd> Suppress all output from <code>grid-proxy-init</code> except for pass phrase prompts.</dl>
<p> <code>-verify</code></p>
<dl>
<dt>
<dd> Perform certificate chain validity checks on the generated proxy.</dl>
<p> <code>-valid </code><i>HOURS:MINUTES</i><code>, -hours </code><i>HOURS</i></p>
<dl>
<dt>
<dd> Create a certificate that is valid for <i>HOURS</i> hours and <i>MINUTES</i> minutes. If not specified, the default of twelve hours is used.</dl>
<p> <code>-cert </code><i>CERTFILE</i><code>, -key </code><i>KEYFILE</i></p>
<dl>
<dt>
<dd> Create a proxy certificate signed by the certificate located in <i>CERTFILE</i> using the key located in <i>KEYFILE</i>. If not specified the default certificate and key will be used. This overrides the values of environment variables described below.</dl>
<p> <code>-certdir </code><i>CERTDIR</i></p>
<dl>
<dt>
<dd> Search <i>CERTDIR</i> for trusted certificates if verifying the proxy certificate. If not specified, the default trusted certificate search path is used. This overrides the value of the X509_CERT_DIR environment variable.</dl>
<p> <code>-out </code><i>PROXYPATH</i></p>
<dl>
<dt>
<dd> Write the generated proxy certificate file to <i>PROXYPATH</i> instead of the default path of /tmp/x509up_u&#8217;UID&#8217;.</dl>
<p> <code>-bits </code><i>BITS</i></p>
<dl>
<dt>
<dd> When creating the proxy certificate, use a <i>BITS</i> bit key instead of the default 1024-bit keys.</dl>
<p> <code>-policy </code><i>POLICYFILE</i></p>
<dl>
<dt>
<dd> Add the certificate policy data described in <i>POLICYFILE</i> as the ProxyCertInfo X.509 extension to the generated proxy certificate.</dl>
<p> <code>-pl </code><i>POLICY-OID</i><code>, -policy-language </code><i>POLICY-OID</i></p>
<dl>
<dt>
<dd> Set the policy language identifier of the policy data specified by the <i>-policy</i> command-line option to the OID specified by the <i>POLICY-OID</i> string.</dl>
<p> <code>-path-length </code><i>MAXIMUM</i></p>
<dl>
<dt>
<dd> Set the maximum length of the chain of proxies that can be created by the generated proxy to <i>MAXIMUM</i>. If not set, the default of an unlimited proxy chain length is used.</dl>
<p> <code>-pwstdin</code></p>
<dl>
<dt>
<dd> Read the private key&#8217;s pass phrase from standard input instead of reading input from the controlling tty. This is useful when scripting <code>grid-proxy-init</code>.</dl>
<p> <code>-limited</code></p>
<dl>
<dt>
<dd> Create a limited proxy. Limited proxies are generally refused by process-creating services, but may be used to authorize with other services.</dl>
<p> <code>-independent</code></p>
<dl>
<dt>
<dd> Create an independent proxy. An independent proxy is not treated as an impersonation proxy but as a separate identity for authorization purposes.</dl>
<p> <code>-draft</code></p>
<dl>
<dt>
<dd> Create a IETF draft proxy instead of the default RFC 3280-compliant proxy. This type of proxy uses a non-standard proxy policy identifier. This might be useful for authenticating with older versions of the Globus Toolkit.</dl>
<p> <code>-old</code></p>
<dl>
<dt>
<dd> Create a legacy proxy instead of the default RFC 3280-compliant proxy. This type of proxy uses a non-standard method of indicating that the certificate is a proxy and whether it is limited. This might be useful for authenticating with older versions of the Globus Toolkit.</dl>
<p> <code>-rfc</code></p>
<dl>
<dt>
<dd> Create an RFC 3820-compliant proxy certificate. This is the default for this version of <code>grid-proxy-init</code>.</dl>
<h2>EXAMPLES</h2>
<p> To create a proxy with the default lifetime and format, run the <code>grid-proxy-init</code> program with no arguments. For example: </p>
<dl>
<dt>
<dd>
<pre>
% grid-proxy-init
Your identity: /DC=org/DC=example/CN=Joe User
Enter GRID pass phrase for this identity: XXXXXXX
Creating proxy .................................. Done
Your proxy is valid until: Thu Mar 18 03:48:05 2010
</pre>
</dl>
<p> To create a stronger proxy that lasts for only 8 hours, use the <i>-hours</i> and <i>-bits</i> command-line options to <code>grid-proxy-init</code>. For example: </p>
<dl>
<dt>
<dd>
<pre>
% grid-proxy-init -hours 8 -bits 4096
Your identity: /DC=org/DC=example/CN=Joe User
Enter GRID pass phrase for this identity: XXXXXXX
Creating proxy .................................. Done
Your proxy is valid until: Thu Mar 17 23:48:05 2010
</pre>
</dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variables affect the execution of <code>grid-proxy-init</code>: </p>
<p> <code>X509_USER_CERT</code></p>
<dl>
<dt>
<dd> Path to the certificate to use as issuer of the new proxy.</dl>
<p> <code>X509_USER_KEY</code></p>
<dl>
<dt>
<dd> Path to the key to use to sign the new proxy.</dl>
<p> <code>X509_CERT_DIR</code></p>
<dl>
<dt>
<dd> Path to the directory containing trusted certificates and signing policies.</dl>
<h2>FILES</h2>
<p> The following files affect the execution of <code>grid-proxy-init</code>: </p>
<p> <code>$HOME/.globus/usercert.pem</code></p>
<dl>
<dt>
<dd> Default path to the certificate to use as issuer of the new proxy.</dl>
<p> <code>$HOME/.globus/userkey.pem</code></p>
<dl>
<dt>
<dd> Default path to the key to use to sign the new proxy.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-grid-proxy-destroy/">grid-proxy-destroy</a>(1), <a href="/docs/linux/man/1-grid-proxy-info/">grid-proxy-info</a>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright &#169; 1999-2014 University of Chicago </p>
<h2>Index</h2>
