---

title: "euare-groupcreate(1)"
name: "euare-groupcreate"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-groupcreate/"
description: "euare-groupcreate – Create a new group"
---

<p> euare-groupcreate &#8211; Create a new group</p>
<h2>SYNOPSIS</h2>
<p> euare-groupcreate [-p PATH] [-v] [&#8211;as-account ACCOUNT] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</dt>
<dd> [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] GROUP</dd></dl>
<h2>DESCRIPTION</h2>
<p> Create a new group</p>
<h3>positional arguments:</h3>
<dl>
<dt>GROUP</dt>
<dd> name of the new group (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-p</code> PATH, <code>&#8211;path</code> PATH</dt>
<dd> path for the new group (default: &quot;/&quot;)</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> print the new group&#8217;s ARN and GUID</dd>
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
