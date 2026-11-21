---

title: "euare-assumerole(1)"
name: "euare-assumerole"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-assumerole/"
description: "euare-assumerole – Assume an IAM role"
---

<p> euare-assumerole &#8211; Assume an IAM role</p>
<h2>SYNOPSIS</h2>
<p> euare-assumerole [-d SECONDS] [&#8211;session-name PATH] [-c | <code>-s]</code></p>
<dl>
<dt>[&#8211;policy-content POLICY_CONTENT | <code>&#8211;policy-document</code> FILE]</dt>
<dd> [&#8211;external-id STR] [&#8211;mfa-serial MFA] [&#8211;mfa-code CODE] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ROLE</dd></dl>
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
<dt>ROLE</dt>
<dd> the role to assume</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-d</code> SECONDS, <code>&#8211;duration</code> SECONDS</dt>
<dd> number of seconds the credentials should be valid for (900-3600) (default: 900)</dd>
<dt><code>&#8211;session-name</code> PATH</dt>
<dd> role session identifier to include in the assumed role user ID (default: automatic)</dd>
<dt><code>-c</code></dt>
<dd> generate C-shell commands on stdout (default if SHELL looks like a csh-style shell</dd>
<dt><code>-s</code></dt>
<dd> generate Bourne shell commands on stdout (default if SHELL does not look like a csh-style shell</dd>
<dt><code>&#8211;policy-content</code> POLICY_CONTENT</dt>
<dd> an IAM policy further restricting what the credentials will be allowed to do. This cannot grant additional permissions.</dd>
<dt><code>&#8211;policy-document</code> FILE</dt>
<dd> file containing an IAM policy further restricting what the credentials will be allowed to do. This cannot grant additional permissions.</dd>
<dt><code>&#8211;external-id</code> STR</dt>
<dd> external ID to use for comparison with policies</dd>
<dt><code>&#8211;mfa-serial</code> MFA</dt>
<dd> MFA token serial number</dd>
<dt><code>&#8211;mfa-code</code> CODE</dt>
<dd> MFA token code</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> token service endpoint URL</dd>
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
