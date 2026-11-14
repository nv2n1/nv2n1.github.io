---
title: "euare-rolecreate(1)"
name: "euare-rolecreate"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-rolecreate/"
description: "euare-rolecreate – Create a new role"
---

<h2>NAME</h2>
<p> euare-rolecreate &#8211; Create a new role</p>
<h2>SYNOPSIS</h2>
<p> euare-rolecreate [-p PATH] (<code>-f</code> FILE | <code>-s</code> SERVICE) [-v]</p>
<dl>
<dt>[&#8211;as-account ACCOUNT] [-U URL] [&#8211;region USER [at] REGION]</p>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ROLE</dl>
<h2>DESCRIPTION</h2>
<p> Create a new role</p>
<h3>positional arguments:</h3>
<dl>
<dt>ROLE</p>
<dd> name of the new role (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-p</code> PATH, <code>&#8211;path</code> PATH</p>
<dd> path for the new role (default: &quot;/&quot;)</p>
<dt><code>-f</code> FILE, <code>&#8211;trust-policy</code> FILE</p>
<dd> file containing the trust policy for the new role</p>
<dt><code>-s</code> SERVICE, <code>&#8211;service</code> SERVICE</p>
<dd> service to allow access to the role (e.g. ec2.amazonaws.com)</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> print the new role&#8217;s ARN, GUID, and policy</p>
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
