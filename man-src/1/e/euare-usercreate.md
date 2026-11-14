---
title: "euare-usercreate(1)"
name: "euare-usercreate"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-usercreate/"
description: "euare-usercreate – Create a new user"
---

<h2>NAME</h2>
<p> euare-usercreate &#8211; Create a new user</p>
<h2>SYNOPSIS</h2>
<p> euare-usercreate [-p PATH] [-g GROUP_NAME] [&#8211;verify] [-k] [-v | <code>-w]</code></p>
<dl>
<dt>[-d DOMAIN] [-l] [&#8211;as-account ACCOUNT] [-U URL]</p>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] USER</dl>
<h2>DESCRIPTION</h2>
<p> Create a new user</p>
<h3>positional arguments:</h3>
<dl>
<dt>USER</p>
<dd> name of the new user (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-p</code> PATH, <code>&#8211;path</code> PATH</p>
<dd> path for the new user (default: &quot;/&quot;)</p>
<dt><code>-g</code> GROUP_NAME, <code>&#8211;group-name</code> GROUP_NAME</p>
<dd> also add the new user to a group</p>
<dt><code>&#8211;verify</code></p>
<dd> ensure the group given with <code>-g</code> exists before doing anything</p>
<dt><code>-k</code>, <code>&#8211;create-accesskey</code></p>
<dd> also create an access key for the new user and show it</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> show the new user&#8217;s ARN and GUID</p>
<dt><code>-w</code>, <code>&#8211;write-config</code></p>
<dd> output access keys and region information in the form of a <a href="/docs/linux/man/5-euca2ools-ini/">euca2ools.ini</a>(5) configuration file instead of by themselves (implies <code>-k</code>)</p>
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
