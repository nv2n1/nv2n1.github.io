---
title: "htproxydestroy(1)"
name: "htproxydestroy"
section: "1"
letter: "h"
url: "/docs/linux/man/1-htproxydestroy/"
description: "htproxyput, htproxydestroy, htproxytime, htproxyunixtime, htproxyrenew – GSI proxy delegations and querying, using GridSite/gLite delegation API"
---

<h2>NAME</h2>
<p> <code>htproxyput, htproxydestroy, htproxytime, htproxyunixtime, htproxyrenew</code> &#8211; GSI proxy delegations and querying, using GridSite/gLite delegation API</p>
<h2>SYNOPSIS</h2>
<p> <code>htproxyput, htproxydestroy, htproxytime, htproxyunixtime, htproxyrenew</code> [options] Service-URL </p>
<p> <code>htproxyinfo</code> [options] </p>
<h2>DESCRIPTION</h2>
<p> <code>htproxyput</code> is a client to perform GSI proxy delegations using the GridSite/gLite delegation Web Service portType. The <a href="/docs/linux/man/8-gridsite-delegation/">gridsite-delegation</a>(8) CGI program is the complementary server-side implementation. </p>
<p> <code>htproxyinfo</code> examines a local copy of a GSI proxy, and outputs a summary of its X.509 and VOMS contents. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-v/&#8211;verbose</p>
<dd> Turn on debugging information. </p>
<dt>&#8211;delegation-id &lt;ID&gt;</p>
<dd> Explicitly specify the Delegation ID to use. </p>
<dt>&#8211;destroy</p>
<dd> Instead of delegating a proxy, delete the proxy from the service&#8217;s proxy cache. Calling the program as htproxydestroy has the same effect. </p>
<dt>&#8211;time</p>
<dd> Instead of delegating a proxy, report the expiration time of the proxy, in the local time of the client. Calling the program as htproxytime has the same effect. </p>
<dt>&#8211;unixtime</p>
<dd> Instead of delegating a proxy, report the expiration time of the proxy, as the number of seconds since 00:00:00 1970-01-01 UTC. Calling the program as htproxyunixtime has the same effect. </p>
<dt>&#8211;renew</p>
<dd> Delegate an updated version of an existing proxy. The Delegation ID <code>must</code> be given when using this option. Calling the program as htproxyrenew has the same effect. </p>
<dt>&#8211;info</p>
<dd> Examine a local proxy file, and output a summary of the X.509 certificates and VOMS attributes it contains. Calling the program as htproxyinfo has the same effect. </p>
<dt>&#8211;cert &lt;X.509 cert path&gt; and &#8211;key &lt;X.509 key path&gt;</p>
<dd> Path to the PEM-encoded X.509 or GSI Proxy user certificate and key to use for HTTPS connections, instead of &quot;anonymous mode.&quot; If only one of &#8211;key or &#8211;cert is given, then that will be tried for both. If neither is given, then the following order of precedence is used: the file name held by the variable X509_USER_PROXY; the file /tmp/x509up_uID (with Unix UID equal to ID); the file names held by X509_USER_CERT / X509_USER_KEY; the files ~/.globus/usercert.pem and ~/.globus/userkey.pem (where ~/ is the home directory of the user.) </p>
<dt>&#8211;capath &lt;X.509 CA root certs directory or file&gt;</p>
<dd> Path to the PEM-encoded CA root certificates to use when verifying remote servers&#8217; host certificates in HTTPS connections. Ideally this should be a directory of hash.0 files as described in the OpenSSL <a href="/docs/linux/man/1-verify/">verify</a>(1) man page, but a file may be used instead. If &#8211;capath is not given, the value of the environment variable X509_CERT_DIR will be tried. If this is not valid, then /etc/grid-security/certificates will be used. </p>
<dt>&#8211;no-verify</p>
<dd> Do not use CA root certificates to verify remote servers&#8217; host certificates. This is useful for testing sites before their certificate is set up properly, but leaves you vulnerable to &quot;man in the middle&quot; attacks by hostile servers masquerading as your target. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt>/tmp/x509up_uID</p>
<dd> Default GSI Proxy file for Unix UID equal to ID. </p>
<dt>/etc/grid-security/certificates</p>
<dd> Default location for trusted Certification Authority root certificates to use when checking server certificates. </p>
<dt>/tmp/.ca-roots-XXXXXX</p>
<dd> Prior to 7.9.8, the underlying curl library did not support the CA root certificates directory. If built with an old version of libcurl, htproxyput will concatenate the certificates in the CA roots directory into a unique temporary file and use that. </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>X509_CERT_DIR</p>
<dd> Holds directory to search for Certification Authority root certificates when verifying server certificates. (Tried if &#8211;capath is not given on the command line.) </p>
<dt>X509_USER_PROXY</p>
<dd> Holds file name of a GSI Proxy to use as user certificate. (Tried if &#8211;cert or &#8211;key are not given on the command line.) </p>
<dt>X509_USER_CERT and X509_USER_KEY</p>
<dd> Holds file name of X.509 user certificate and key. (Tried if X509_USER_PROXY is not valid.) </p>
</dl>
<h2>EXIT CODES</h2>
<p> 0 is returned on complete success, and non-zero on error. </p>
<h2>TO DO</h2>
<p> Better error recovery. </p>
<h2>AUTHOR</h2>
<p> Andrew McNab &lt;Andrew.McNab [at] manchester.ac.uk&gt; </p>
<p> htproxyput is part of GridSite: <a rel="nofollow" href="http://www.gridsite.org/">http://www.gridsite.org/</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-htcp/">htcp</a>(1),</code> <code><a href="/docs/linux/man/8-gridsite-delegation/">gridsite-delegation</a>(8)</code> </p>
<h2>Index</h2>
