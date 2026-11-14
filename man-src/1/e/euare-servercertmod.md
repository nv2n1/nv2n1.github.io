---
title: "euare-servercertmod(1)"
name: "euare-servercertmod"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-servercertmod/"
description: "euare-servercertmod – Change the name and/or path of a server certificate"
---

<h2>NAME</h2>
<p> euare-servercertmod &#8211; Change the name and/or path of a server certificate</p>
<h2>SYNOPSIS</h2>
<p> euare-servercertmod [-n CERT] [-p PATH] [&#8211;as-account ACCOUNT] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</p>
<dd> [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] CERT</dl>
<h2>DESCRIPTION</h2>
<p> Change the name and/or path of a server certificate</p>
<h3>positional arguments:</h3>
<dl>
<dt>CERT</p>
<dd> name of the server certificate to update</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-n</code> CERT, <code>&#8211;new-server-certificate-name</code> CERT</p>
<dd> new name for the server certificate</p>
<dt><code>-p</code> PATH, <code>&#8211;new-path</code> PATH</p>
<dd> new path for the server certificate</p>
<dt><code>&#8211;as-account</code> ACCOUNT</p>
<dd> [Eucalyptus cloud admin only] run this command as the administrator of another account</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> identity service endpoint URL</p>
<dt><code>&#8211;region</code> USER [at] REGION</p>
<dd> region and/or user names to search when looking up config file data</p>
<dt> <code>-I</code> KEY_ID, <code>&#8211;access-key-id</code> KEY_ID</p>
<dt> <code>-S</code> KEY, <code>&#8211;secret-key</code> KEY</p>
<dt> <code>&#8211;security-token</code> TOKEN</p>
<dt><code>&#8211;debug</code></p>
<dd>
<dd>show debugging output</p>
<dt><code>&#8211;debugger</code></p>
<dd> launch interactive debugger on error</p>
<dt><code>&#8211;version</code></p>
<dd> show the program&#8217;s version and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit </p>
</dl>
<h2>Index</h2>
