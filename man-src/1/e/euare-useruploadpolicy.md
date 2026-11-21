---
title: "euare-useruploadpolicy(1)"
name: "euare-useruploadpolicy"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-useruploadpolicy/"
description: "euare-useruploadpolicy – Attach a policy to a user"
---

<h2>NAME</h2>
<p> euare-useruploadpolicy &#8211; Attach a policy to a user</p>
<h2>SYNOPSIS</h2>
<p> euare-useruploadpolicy <code>-p</code> POLICY (<code>-o</code> POLICY_CONTENT | <code>-f</code> FILE)</p>
<dl>
<dt>[&#8211;as-account ACCOUNT] [-U URL]</dt>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] USER</dd></dl>
<h2>DESCRIPTION</h2>
<p> Attach a policy to a user</p>
<h3>positional arguments:</h3>
<dl>
<dt>USER</dt>
<dd> user to attach the policy to (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-p</code> POLICY, <code>&#8211;policy-name</code> POLICY</dt>
<dd> name of the policy (required)</dd>
<dt><code>-o</code> POLICY_CONTENT, <code>&#8211;policy-content</code> POLICY_CONTENT</dt>
<dd> the policy to attach</dd>
<dt><code>-f</code> FILE, <code>&#8211;policy-document</code> FILE</dt>
<dd> file containing the policy to attach</dd>
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
