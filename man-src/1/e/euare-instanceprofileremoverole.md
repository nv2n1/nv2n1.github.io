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
<p> euare-instanceprofileremoverole <code>-r</code> ROLE [&#8211;as-account ACCOUNT] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID]</dt>
<dd> [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] IPROFILE</dd></dl>
<p> Remove a role from an instance profile</p>
<h3>positional arguments:</h3>
<dl>
<dt>IPROFILE</dt>
<dd> instance profile to remove the role from (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-r</code> ROLE, <code>&#8211;role-name</code> ROLE</dt>
<dd> the role to remove (required)</dd>
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
