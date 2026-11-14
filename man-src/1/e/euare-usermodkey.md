---
title: "euare-usermodkey(1)"
name: "euare-usermodkey"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-usermodkey/"
description: "euare-usermodkey – Change the status of an access key from Active to Inactive, or vice versa"
---

<h2>NAME</h2>
<p> euare-usermodkey &#8211; Change the status of an access key from Active to Inactive, or vice versa</p>
<h2>SYNOPSIS</h2>
<p> euare-usermodkey <code>-s</code> {Active,Inactive} [-u USER] [&#8211;as-account ACCOUNT]</p>
<dl>
<dt>[-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</p>
<dd> [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] KEY_ID</dl>
<h2>DESCRIPTION</h2>
<p> Change the status of an access key from Active to Inactive, or vice versa</p>
<h3>positional arguments:</h3>
<dl>
<dt>KEY_ID</p>
<dd> ID of the access key to update (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-s</code> {Active,Inactive}, <code>&#8211;status</code> {Active,Inactive}</p>
<dd> status to assign to the access key (required)</p>
<dt><code>-u</code> USER, <code>&#8211;user-name</code> USER</p>
<dd> user owning the access key to update (default: current user)</p>
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
