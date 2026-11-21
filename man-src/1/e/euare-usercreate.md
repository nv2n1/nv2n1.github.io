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
<p> euare-usercreate [-p PATH] [-g GROUP_NAME] [&#8211;verify] [-k] [-v | <code>-w]</code></p>
<dl>
<dt>[-d DOMAIN] [-l] [&#8211;as-account ACCOUNT] [-U URL]</dt>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] USER</dd></dl>
<p> Create a new user</p>
<h3>positional arguments:</h3>
<dl>
<dt>USER</dt>
<dd> name of the new user (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-p</code> PATH, <code>&#8211;path</code> PATH</dt>
<dd> path for the new user (default: &quot;/&quot;)</dd>
<dt><code>-g</code> GROUP_NAME, <code>&#8211;group-name</code> GROUP_NAME</dt>
<dd> also add the new user to a group</dd>
<dt><code>&#8211;verify</code></dt>
<dd> ensure the group given with <code>-g</code> exists before doing anything</dd>
<dt><code>-k</code>, <code>&#8211;create-accesskey</code></dt>
<dd> also create an access key for the new user and show it</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> show the new user&#8217;s ARN and GUID</dd>
<dt><code>-w</code>, <code>&#8211;write-config</code></dt>
<dd> output access keys and region information in the form of a euca2ools.ini(5) configuration file instead of by themselves (implies <code>-k</code>)</dd>
<dt><code>-d</code> DOMAIN, <code>&#8211;domain</code> DOMAIN</dt>
<dd> the DNS domain to use for region information in configuration file output (default: based on IAM URL)</dd>
<dt><code>-l</code>, <code>&#8211;set-default-user</code></dt>
<dd> set this user as the default user for the region in euca2ools.ini(5) configuration file output. This option is only useful when used with <code>-w</code>.</dd>
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
