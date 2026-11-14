---
title: "euare-usercreatecert(1)"
name: "euare-usercreatecert"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-usercreatecert/"
description: "euare-usercreatecert – [Eucalyptus only] Create a new signing certificate"
---

<h2>NAME</h2>
<p> euare-usercreatecert &#8211; [Eucalyptus only] Create a new signing certificate</p>
<h2>SYNOPSIS</h2>
<p> euare-usercreatecert [&#8211;out FILE] [&#8211;keyout FILE]</p>
<dl>
<dt>[&#8211;as-account ACCOUNT] [-U URL]</p>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [USER]</dl>
<h2>DESCRIPTION</h2>
<p> [Eucalyptus only] Create a new signing certificate</p>
<h3>positional arguments:</h3>
<dl>
<dt>USER</p>
<dd> user to create the signing certificate for (default: current user)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;out</code> FILE</p>
<dd> file to write the certificate to (default: stdout)</p>
<dt><code>&#8211;keyout</code> FILE</p>
<dd> file to write the private key to (default: stdout)</p>
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
