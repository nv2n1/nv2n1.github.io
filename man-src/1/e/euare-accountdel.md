---

title: "euare-accountdel(1)"
name: "euare-accountdel"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-accountdel/"
description: "euare-accountdel – [Eucalyptus cloud admin only] Delete an account"
---

<p> euare-accountdel &#8211; [Eucalyptus cloud admin only] Delete an account</p>
<h2>SYNOPSIS</h2>
<p> euare-accountdel [-r] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID]</p>
<dl>
<dt>[-S KEY] [&#8211;security-token TOKEN] [&#8211;debug]</dt>
<dd> [&#8211;debugger] [&#8211;version] [-h] ACCOUNT</dd></dl>
<h2>DESCRIPTION</h2>
<p> [Eucalyptus cloud admin only] Delete an account</p>
<h3>positional arguments:</h3>
<dl>
<dt>ACCOUNT</dt>
<dd> name or ID of the account to delete (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-r</code>, <code>&#8211;recursive</code></dt>
<dd> delete all users, groups, and policies associated with the account as well</dd>
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
