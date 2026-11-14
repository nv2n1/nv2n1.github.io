---
title: "tor-gencert(1)"
name: "tor-gencert"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tor-gencert/"
description: "tor-gencert – Generate certs and keys for Tor directory authorities"
---

<h2 class="name">NAME</h2>
<p> tor-gencert &#8211; Generate certs and keys for Tor directory authorities </p>
<h2>SYNOPSIS</h2>
<p> <code>tor-gencert</code> [-h|&#8211;help] [-v] [-r|&#8211;reuse] [&#8211;create-identity-key] [-i <i>id_file</i>] [-c <i>cert_file</i>] [-m <i>num</i>] [-a <i>address</i>:<i>port</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>tor-gencert</code> generates certificates and private keys for use by Tor directory authorities running the v3 Tor directory protocol, as used by Tor 0.2.0 and later. If you are not running a directory authority, you don&#8217;t need to use tor-gencert. </p>
<p> Every directory authority has a long term authority <i>identity</i> <i>key</i> (which is distinct from the identity key it uses as a Tor server); this key should be kept offline in a secure location. It is used to certify shorter-lived <i>signing</i> <i>keys</i>, which are kept online and used by the directory authority to sign votes and consensus documents. </p>
<p> After you use this program to generate a signing key and a certificate, copy those files to the keys subdirectory of your Tor process, and send Tor a SIGHUP signal. DO NOT COPY THE IDENTITY KEY.</p>
<h2>OPTIONS</h2>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> Display verbose output.</dl>
<p> <code>-h</code> or <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<p> <code>-r</code> or <code>&#8211;reuse</code></p>
<dl>
<dt>
<dd> Generate a new certificate, but not a new signing key. This can be used to change the address or lifetime associated with a given key.</dl>
<p> <code>&#8211;create-identity-key</code></p>
<dl>
<dt>
<dd> Generate a new identity key. You should only use this option the first time you run tor-gencert; in the future, you should use the identity key that&#8217;s already there.</dl>
<p> <code>-i</code> <i>FILENAME</i></p>
<dl>
<dt>
<dd> Read the identity key from the specified file. If the file is not present and &#8211;create-identity-key is provided, create the identity key in the specified file. Default: &quot;./authority_identity_key&quot;</dl>
<p> <code>-s</code> <i>FILENAME</i></p>
<dl>
<dt>
<dd> Write the signing key to the specified file. Default: &quot;./authority_signing_key&quot;</dl>
<p> <code>-c</code> <i>FILENAME</i></p>
<dl>
<dt>
<dd> Write the certificate to the specified file. Default: &quot;./authority_certificate&quot;</dl>
<p> <code>-m</code> <i>NUM</i></p>
<dl>
<dt>
<dd> Number of months that the certificate should be valid. Default: 12.</dl>
<p> <code>&#8211;passphrase-fd</code> <i>FILEDES</i></p>
<dl>
<dt>
<dd> Filedescriptor to read the passphrase from. Ends at the first NUL or newline. Default: read from the terminal.</dl>
<p> <code>-a</code> <i>address</i>:<i>port</i></p>
<dl>
<dt>
<dd> If provided, advertise the address:port combination as this authority&#8217;s preferred directory port in its certificate. If the address is a hostname, the hostname is resolved to an IP before it&#8217;s published.</dl>
<h2>BUGS</h2>
<p> This probably doesn&#8217;t run on Windows. That&#8217;s not a big issue, since we don&#8217;t really want authorities to be running on Windows anyway.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tor/">tor</a></code>(1) </p>
<p> See also the &quot;dir-spec.txt&quot; file, distributed with Tor.</p>
<h2>AUTHORS</h2>
<dl>
<dt>
<dd>
<pre><code>
Roger Dingledine&lt;arma[at] mit.edu&gt;, Nick Mathewson&lt;nickm[at] alum.mit.edu&gt;.
</code></pre>
</dl>
<h2>AUTHOR</h2>
<p> <code>Nick Mathewson</code></p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
