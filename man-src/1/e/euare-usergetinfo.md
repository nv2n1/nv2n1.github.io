---
title: "euare-usergetinfo(1)"
name: "euare-usergetinfo"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-usergetinfo/"
description: "euare-usergetinfo – [Eucalyptus only] Display information about a user"
---

<h2>NAME</h2>
<p> euare-usergetinfo &#8211; [Eucalyptus only] Display information about a user</p>
<h2>SYNOPSIS</h2>
<p> euare-usergetinfo [-k INFOKEY] [&#8211;as-account ACCOUNT]</p>
<dl>
<dt>[&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION]</dt>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [USER]</dd></dl>
<h2>DESCRIPTION</h2>
<p> [Eucalyptus only] Display information about a user</p>
<h3>positional arguments:</h3>
<dl>
<dt>USER</dt>
<dd> name of the user to describe (default: current user)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-k</code> INFOKEY, <code>&#8211;info-key</code> INFOKEY</dt>
<dd> name of the piece of user info to show</dd>
<dt><code>&#8211;as-account</code> ACCOUNT</dt>
<dd> [Eucalyptus cloud admin only] run this command as the administrator of another account</dd>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
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
<h2>Index</h2>
