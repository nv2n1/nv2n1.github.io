---
title: "fts-rest-server-status(1)"
name: "fts-rest-server-status"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fts-rest-server-status/"
description: "fts-rest-server-status"
---

<h2>NAME</h2>
<p> fts-rest-server-status</p>
<h2>SYNOPIS</h2>
<p> Usage: fts-rest-server-status [options]</p>
<h2>DESCRIPTION</h2>
<p> Use this command to check on the service status.</p>
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
<dt><code>-H/&#8211;host</code></p>
<dd> Limit the output to a given host</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;is-active</code></p>
<dd> The tool will return &lt; 0 on error, 0 if nothing is active, 1 if there are active transfers, 2 if there are active staging, 3 if there are both</p>
<dl>
<dt>
<dd></dl>
</dl>
<h2>AUTHORS</h2>
<p> fts-devel [at] cern.ch. </p>
<h2>Index</h2>
