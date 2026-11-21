---

title: "euare-oidcprovidercreate(1)"
name: "euare-oidcprovidercreate"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-oidcprovidercreate/"
description: "euare-oidcprovidercreate – Create a new OpenID Connect provider"
---

<h2>NAME</h2>
<p> euare-oidcprovidercreate &#8211; Create a new OpenID Connect provider</p>
<p> euare-oidcprovidercreate [-c CLIENT] [-t HEX] [&#8211;as-account ACCOUNT]</p>
<dl>
<dt>[-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID]</dt>
<dd> [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] URL</dd></dl>
<p> Create a new OpenID Connect provider</p>
<h3>positional arguments:</h3>
<dl>
<dt>URL</dt>
<dd> the URL for the new provider (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-c</code> CLIENT, <code>&#8211;client-id</code> CLIENT</dt>
<dd> a client ID, or audience, for the new provider</dd>
<dt><code>-t</code> HEX, <code>&#8211;thumbprint</code> HEX</dt>
<dd> the SHA-1 thumbprint of the new OpenID Connect provider&#8217;s certificate. If one is not supplied this command will attempt to connect to the server to determine it automatically.</dd>
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
