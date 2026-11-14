---
title: "euare-instanceprofileremoverole(1)"
name: "euare-instanceprofileremoverole"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-instanceprofileremoverole/"
description: "euare-instanceprofileremoverole – Remove a role from an instance profile"
---

<h2>NAME</h2>
<p> euare-instanceprofileremoverole &#8211; Remove a role from an instance profile</p>
<h2>SYNOPSIS</h2>
<p> euare-instanceprofileremoverole <code>-r</code> ROLE [&#8211;as-account ACCOUNT] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID]</p>
<dd> [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] IPROFILE</dl>
<h2>DESCRIPTION</h2>
<p> Remove a role from an instance profile</p>
<h3>positional arguments:</h3>
<dl>
<dt>IPROFILE</p>
<dd> instance profile to remove the role from (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-r</code> ROLE, <code>&#8211;role-name</code> ROLE</p>
<dd> the role to remove (required)</p>
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
