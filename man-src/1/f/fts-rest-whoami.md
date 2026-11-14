---
title: "fts-rest-whoami(1)"
name: "fts-rest-whoami"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fts-rest-whoami/"
description: "fts-rest-whoami"
---

<h2>NAME</h2>
<p> fts-rest-whoami</p>
<h2>SYNOPIS</h2>
<p> Usage: fts-rest-whoami [options]</p>
<h2>DESCRIPTION</h2>
<p> This command exists for convenience. It can be used to check, as the name suggests, who are we for the server.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h/&#8211;help</code></p>
<dd> Show this help message and exit</p>
<dl>
<dt>
<dd></dl>
<dt><code>-v/&#8211;verbose</code></p>
<dd> Verbose output.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-s/&#8211;endpoint</code></p>
<dd> Fts3 rest endpoint.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-j/&#8211;json</code></p>
<dd> Print the output in json format.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;key</code></p>
<dd> The user certificate private key.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;cert</code></p>
<dd> The user certificate.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;capath</code></p>
<dd> Use the specified directory to verify the peer</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;insecure</code></p>
<dd> Do not validate the server certificate</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;access-token</code></p>
<dd> Oauth2 access token (supported only by some endpoints, takes precedence)</p>
<dl>
<dt>
<dd></dl>
</dl>
<h2>EXAMPLE</h2>
<dl>
<dt>
<dd>
<pre>
$&nbsp;<wbr>fts-rest-whoami -s&nbsp;<wbr><a rel="nofollow" href="https://fts3-pilot.cern.ch:8446">https://fts3-pilot.cern.ch:8446</a>
User DN:&nbsp;<wbr>/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=saketag/CN=678984/CN=Alejandro Alvarez Ayllon
VO: dteam
VO: dteam/cern
Delegation id: 9a4257f435fa2010
</pre>
</dl>
<h2>AUTHORS</h2>
<p> fts-devel [at] cern.ch. </p>
<h2>Index</h2>
