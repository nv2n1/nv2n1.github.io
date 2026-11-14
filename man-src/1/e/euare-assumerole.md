---
title: "euare-assumerole(1)"
name: "euare-assumerole"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-assumerole/"
description: "euare-assumerole – Assume an IAM role"
---

<h2>NAME</h2>
<p> euare-assumerole &#8211; Assume an IAM role</p>
<h2>SYNOPSIS</h2>
<p> euare-assumerole [-d SECONDS] [&#8211;session-name PATH] [-c | <code>-s]</code></p>
<dl>
<dt>[&#8211;policy-content POLICY_CONTENT | <code>&#8211;policy-document</code> FILE]</p>
<dd> [&#8211;external-id STR] [&#8211;mfa-serial MFA] [&#8211;mfa-code CODE] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ROLE</dl>
<h2>DESCRIPTION</h2>
<p> Assume an IAM role</p>
<h2>DESCRIPTION</h2>
<p> The euare-assumerole utility obtains credentials for an IAM role and outputs them in the form of shellcode that sets environment variables that allow euca2ools commands to use them. Use it inside an eval command to make this process seamless:</p>
<h2>DESCRIPTION</h2>
<p> $ eval `euare-assumerole myrole`</p>
<h2>DESCRIPTION</h2>
<p> To stop using the role, use <a href="/docs/linux/man/1-euare-releaserole/">euare-releaserole</a>(1).</p>
<h3>positional arguments:</h3>
<dl>
<dt>ROLE</p>
<dd> the role to assume</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-d</code> SECONDS, <code>&#8211;duration</code> SECONDS</p>
<dd> number of seconds the credentials should be valid for (900-3600) (default: 900)</p>
<dt><code>&#8211;session-name</code> PATH</p>
<dd> role session identifier to include in the assumed role user ID (default: automatic)</p>
<dt><code>-c</code></p>
<dd> generate C-shell commands on stdout (default if SHELL looks like a csh-style shell</p>
<dt><code>-s</code></p>
<dd> generate Bourne shell commands on stdout (default if SHELL does not look like a csh-style shell</p>
<dt><code>&#8211;policy-content</code> POLICY_CONTENT</p>
<dd> an IAM policy further restricting what the credentials will be allowed to do. This cannot grant additional permissions.</p>
<dt><code>&#8211;policy-document</code> FILE</p>
<dd> file containing an IAM policy further restricting what the credentials will be allowed to do. This cannot grant additional permissions.</p>
<dt><code>&#8211;external-id</code> STR</p>
<dd> external ID to use for comparison with policies</p>
<dt><code>&#8211;mfa-serial</code> MFA</p>
<dd> MFA token serial number</p>
<dt><code>&#8211;mfa-code</code> CODE</p>
<dd> MFA token code</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> token service endpoint URL</p>
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
