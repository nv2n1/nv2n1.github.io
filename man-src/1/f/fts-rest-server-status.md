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
<dt><code>-H/&#8211;host</code></dt>
<dd> Limit the output to a given host</dd>
<dl>
</dl>
<dt><code>&#8211;is-active</code></dt>
<dd> The tool will return &lt; 0 on error, 0 if nothing is active, 1 if there are active transfers, 2 if there are active staging, 3 if there are both</dd>
<dl>
</dl>
</dl>
<h2>AUTHORS</h2>
<p> fts-devel [at] cern.ch. </p>
