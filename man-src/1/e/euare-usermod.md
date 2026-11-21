---

title: "euare-usermod(1)"
name: "euare-usermod"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-usermod/"
description: "euare-usermod – Change the name and/or path of a user"
---

<p> euare-usermod &#8211; Change the name and/or path of a user</p>
<h2>SYNOPSIS</h2>
<p> euare-usermod [-n USER] [-p PATH] [&#8211;enabled {true,false}]</p>
<dl>
<dt>[&#8211;pwd-expires YYYY-MM-DDThh:mm:ssZ]</dt>
<dd> [&#8211;reg-status {REGISTERED,APPROVED,CONFIRMED}] [&#8211;as-account ACCOUNT] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] USER</dd></dl>
<h2>DESCRIPTION</h2>
<p> Change the name and/or path of a user</p>
<h3>positional arguments:</h3>
<dl>
<dt>USER</dt>
<dd> name of the user to update</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-n</code> USER, <code>&#8211;new-user-name</code> USER</dt>
<dd> new name for the user</dd>
<dt><code>-p</code> PATH, <code>&#8211;new-path</code> PATH</dt>
<dd> new path for the user</dd>
<dt><code>&#8211;enabled</code> {true,false}</dt>
<dd> [Eucalyptus only] &#8216;true&#8217; to enable the user, or &#8216;false&#8217; to disable the user</dd>
<dt><code>&#8211;pwd-expires</code> YYYY-MM-DDThh:mm:ssZ</dt>
<dd> [Eucalyptus only] New password expiration date, in ISO8601 format</dd>
<dt><code>&#8211;reg-status</code> {REGISTERED,APPROVED,CONFIRMED}</dt>
<dd> [Eucalyptus &lt; 4.2 only] new registration status. Only CONFIRMED users may access the system.</dd>
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
