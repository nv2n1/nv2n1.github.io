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
<p> This command exists for convenience. It can be used to check, as the name suggests, who are we for the server.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h/&#8211;help</code></dt>
<dd> Show this help message and exit</dd>
<dl>
</dl>
<dt><code>-v/&#8211;verbose</code></dt>
<dd> Verbose output.</dd>
<dl>
</dl>
<dt><code>-s/&#8211;endpoint</code></dt>
<dd> Fts3 rest endpoint.</dd>
<dl>
</dl>
<dt><code>-j/&#8211;json</code></dt>
<dd> Print the output in json format.</dd>
<dl>
</dl>
<dt><code>&#8211;key</code></dt>
<dd> The user certificate private key.</dd>
<dl>
</dl>
<dt><code>&#8211;cert</code></dt>
<dd> The user certificate.</dd>
<dl>
</dl>
<dt><code>&#8211;capath</code></dt>
<dd> Use the specified directory to verify the peer</dd>
<dl>
</dl>
<dt><code>&#8211;insecure</code></dt>
<dd> Do not validate the server certificate</dd>
<dl>
</dl>
<dt><code>&#8211;access-token</code></dt>
<dd> Oauth2 access token (supported only by some endpoints, takes precedence)</dd>
<dl>
</dl>
</dl>
<h2>EXAMPLE</h2>
<dl>
<dt>
</dt><dd>
<pre>
$&nbsp;<wbr>fts-rest-whoami -s&nbsp;<wbr><a rel="nofollow" href="https://fts3-pilot.cern.ch:8446">https://fts3-pilot.cern.ch:8446</a>
User DN:&nbsp;<wbr>/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=saketag/CN=678984/CN=Alejandro Alvarez Ayllon
VO: dteam
VO: dteam/cern
Delegation id: 9a4257f435fa2010
</pre>
</dd></dl>
<h2>AUTHORS</h2>
<p> fts-devel [at] cern.ch. </p>
