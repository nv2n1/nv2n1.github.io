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
<dt>[&#8211;as-account ACCOUNT] [-U URL] [&#8211;region USER [at] REGION]</dt>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ROLE</dd></dl>
<h2>DESCRIPTION</h2>
<p> Create a new role</p>
<h3>positional arguments:</h3>
<dl>
<dt>ROLE</dt>
<dd> name of the new role (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-p</code> PATH, <code>&#8211;path</code> PATH</dt>
<dd> path for the new role (default: &quot;/&quot;)</dd>
<dt><code>-f</code> FILE, <code>&#8211;trust-policy</code> FILE</dt>
<dd> file containing the trust policy for the new role</dd>
<dt><code>-s</code> SERVICE, <code>&#8211;service</code> SERVICE</dt>
<dd> service to allow access to the role (e.g. ec2.amazonaws.com)</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> print the new role&#8217;s ARN, GUID, and policy</dd>
<dt><code>&#8211;as-account</code> ACCOUNT</dt>
<dd> [Eucalyptus cloud admin only] run this command as the administrator of another account</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> identity service endpoint URL</dd>
<dt><code>&#8211;region</code> USER [at] REGION</dt>
<dd> region and/or user names to search when looking up config file data</dd>
<dt> <code>-I</code> KEY_ID, <code>&#8211;access-key-id</code> KEY_ID</dt>
<dt> <code>-S</code> KEY, <code>&#8211;secret-key</code> KEY</dt>
<dt> <code>&#8211;security-token</code> TOKEN</dt>
<dt><code>&#8211;debug</code></dt>
<dd>
</dd><dd>show debugging output</dd>
<dt><code>&#8211;debugger</code></dt>
<dd> launch interactive debugger on error</dd>
<dt><code>&#8211;version</code></dt>
<dd> show the program&#8217;s version and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit </dd>
</dl>
