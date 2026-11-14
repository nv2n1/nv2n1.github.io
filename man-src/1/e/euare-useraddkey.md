---
title: "euare-useraddkey(1)"
name: "euare-useraddkey"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-useraddkey/"
description: "euare-useraddkey – Create a new access key for a user"
---

<h2>NAME</h2>
<p> euare-useraddkey &#8211; Create a new access key for a user</p>
<h2>SYNOPSIS</h2>
<p> euare-useraddkey [-w] [-d DOMAIN] [-l] [&#8211;as-account ACCOUNT] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</p>
<dd> [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] USER</dl>
<h2>DESCRIPTION</h2>
<p> Create a new access key for a user</p>
<h3>positional arguments:</h3>
<dl>
<dt>USER</p>
<dd> user the new key will belong to (default: current user)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-w</code>, <code>&#8211;write-config</code></p>
<dd> output access keys and region information in the form of a <a href="/docs/linux/man/5-euca2ools-ini/">euca2ools.ini</a>(5) configuration file instead of by themselves</p>
<dt><code>-d</code> DOMAIN, <code>&#8211;domain</code> DOMAIN</p>
<dd> the DNS domain to use for region information in configuration file output (default: based on IAM URL)</p>
<dt><code>-l</code>, <code>&#8211;set-default-user</code></p>
<dd> set this user as the default user for the region in <a href="/docs/linux/man/5-euca2ools-ini/">euca2ools.ini</a>(5) configuration file output. This option is only useful when used with <code>-w</code>.</p>
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
