---
title: "fts-rest-delegate(1)"
name: "fts-rest-delegate"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fts-rest-delegate/"
description: "fts-rest-delegate"
---

<h2>NAME</h2>
<p> fts-rest-delegate</p>
<h2>SYNOPIS</h2>
<p> Usage: fts-rest-delegate [options]</p>
<h2>DESCRIPTION</h2>
<p> This command can be used to (re)delegate your credentials to the FTS3 server</p>
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
<dt><code>-f/&#8211;force</code></dt>
<dd> Force the delegation</dd>
<dl>
</dl>
</dl>
<h2>EXAMPLE</h2>
<dl>
<dt>
</dt><dd>
<pre>
$&nbsp;<wbr>fts-rest-delegate -s&nbsp;<wbr><a rel="nofollow" href="https://fts3-devel.cern.ch:8446">https://fts3-devel.cern.ch:8446</a>
Delegation id: 9a4257f435fa2010&quot;
</pre>
</dd></dl>
<h2>AUTHORS</h2>
<p> fts-devel [at] cern.ch. </p>
<h2>Index</h2>
