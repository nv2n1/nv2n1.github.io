---

title: "euare-usergetpolicy(1)"
name: "euare-usergetpolicy"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-usergetpolicy/"
description: "euare-usergetpolicy – Display a user’s policy"
---

<h2>NAME</h2>
<p> euare-usergetpolicy &#8211; Display a user&#8217;s policy</p>
<p> euare-usergetpolicy <code>-p</code> POLICY [&#8211;pretty-print] [&#8211;as-account ACCOUNT]</p>
<dl>
<dt>[-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID]</dt>
<dd> [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] USER</dd></dl>
<p> Display a user&#8217;s policy</p>
<h3>positional arguments:</h3>
<dl>
<dt>USER</dt>
<dd> user the poilcy is attached to (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-p</code> POLICY, <code>&#8211;policy-name</code> POLICY</dt>
<dd> name of the policy to show (required)</dd>
<dt><code>&#8211;pretty-print</code></dt>
<dd> reformat the policy for easier reading</dd>
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
