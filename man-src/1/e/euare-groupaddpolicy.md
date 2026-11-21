---

title: "euare-groupaddpolicy(1)"
name: "euare-groupaddpolicy"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-groupaddpolicy/"
description: "euare-groupaddpolicy – Add a new policy to a group. To add more complex policies than this tool supports, see euare-groupuploadpolicy(1)."
---

<p> euare-groupaddpolicy &#8211; Add a new policy to a group. To add more complex policies than this tool supports, see <a href="/docs/linux/man/1-euare-groupuploadpolicy/">euare-groupuploadpolicy</a>(1).</p>
<h2>SYNOPSIS</h2>
<p> euare-groupaddpolicy <code>-p</code> POLICY <code>-e</code> {Allow,Deny} <code>-a</code> ACTIONS <code>-r</code> RESOURCES</p>
<dl>
<dt>[-o] [&#8211;as-account ACCOUNT] [-U URL]</dt>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] GROUP</dd></dl>
<h2>DESCRIPTION</h2>
<p> Add a new policy to a group. To add more complex policies than this tool supports, see <a href="/docs/linux/man/1-euare-groupuploadpolicy/">euare-groupuploadpolicy</a>(1).</p>
<h3>positional arguments:</h3>
<dl>
<dt>GROUP</dt>
<dd> group to attach the policy to (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-p</code> POLICY, <code>&#8211;policy-name</code> POLICY</dt>
<dd> name of the new policy (required)</dd>
<dt><code>-e</code> {Allow,Deny}, <code>&#8211;effect</code> {Allow,Deny}</dt>
<dd> whether the new policy should Allow or Deny (required)</dd>
<dt><code>-a</code> ACTIONS, <code>&#8211;action</code> ACTIONS</dt>
<dd> action(s) the policy should apply to (at least one required)</dd>
<dt><code>-r</code> RESOURCES, <code>&#8211;resource</code> RESOURCES</dt>
<dd> resource(s) the policy should apply to (at least one required)</dd>
<dt><code>-o</code>, <code>&#8211;output</code></dt>
<dd> display the newly-created policy</dd>
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
