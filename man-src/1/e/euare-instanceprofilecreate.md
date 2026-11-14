---
title: "euare-instanceprofilecreate(1)"
name: "euare-instanceprofilecreate"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-instanceprofilecreate/"
description: "euare-instanceprofilecreate – Create a new instance profile"
---

<h2>NAME</h2>
<p> euare-instanceprofilecreate &#8211; Create a new instance profile</p>
<h2>SYNOPSIS</h2>
<p> euare-instanceprofilecreate [-p PATH] [-r ROLE | <code>&#8211;create-role]</code> [-v]</p>
<dl>
<dt>[&#8211;as-account ACCOUNT] [-U URL]</p>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] IPROFILE</dl>
<h2>DESCRIPTION</h2>
<p> Create a new instance profile</p>
<h3>positional arguments:</h3>
<dl>
<dt>IPROFILE</p>
<dd> name of the new instance profile (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-p</code> PATH, <code>&#8211;path</code> PATH</p>
<dd> path for the new instance profile (default: &quot;/&quot;)</p>
<dt><code>-r</code> ROLE, <code>&#8211;add-role</code> ROLE</p>
<dd> also add a role to the new instance profile</p>
<dt><code>&#8211;create-role</code></p>
<dd> also create a role with the same name and path and add it to the instance profile</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> print the new instance profile&#8217;s ARN and GUID</p>
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
