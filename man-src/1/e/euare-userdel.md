---
title: "euare-userdel(1)"
name: "euare-userdel"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-userdel/"
description: "euare-userdel – Delete a user"
---

<h2>NAME</h2>
<p> euare-userdel &#8211; Delete a user</p>
<h2>SYNOPSIS</h2>
<p> euare-userdel [-r] [-p] [&#8211;as-account ACCOUNT] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</p>
<dd> [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] USER</dl>
<h2>DESCRIPTION</h2>
<p> Delete a user</p>
<h3>positional arguments:</h3>
<dl>
<dt>USER</p>
<dd> name of the user to delete (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-r</code>, <code>&#8211;recursive</code></p>
<dd> remove all IAM resources associated with the user first</p>
<dt><code>-p</code>, <code>&#8211;pretend</code></p>
<dd> list the resources that would be deleted instead of actually deleting them. Implies <code>-r</code>.</p>
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
