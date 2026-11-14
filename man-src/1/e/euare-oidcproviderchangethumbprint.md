---
title: "euare-oidcproviderchangethumbprint(1)"
name: "euare-oidcproviderchangethumbprint"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-oidcproviderchangethumbprint/"
description: "euare-oidcproviderchangethumbprint – Replace an OpenID Connect provider’s list of thumbprints"
---

<h2>NAME</h2>
<p> euare-oidcproviderchangethumbprint &#8211; Replace an OpenID Connect provider&#8217;s list of thumbprints</p>
<h2>SYNOPSIS</h2>
<p> euare-oidcproviderchangethumbprint [-t HEX] [&#8211;as-account ACCOUNT]</p>
<dl>
<dt>[-U URL] [&#8211;region USER [at] REGION]</p>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] OIDC</dl>
<h2>DESCRIPTION</h2>
<p> Replace an OpenID Connect provider&#8217;s list of thumbprints</p>
<h3>positional arguments:</h3>
<dl>
<dt>OIDC</p>
<dd> the ARN of the provider to update (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-t</code> HEX, <code>&#8211;thumbprint</code> HEX</p>
<dd> the new SHA-1 thumbprint of the OpenID Connect provider&#8217;s certificate. This option may be specified more than once to allow multiple certificates to be accepted. If one is not supplied this command will attempt to determine it automatically.</p>
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
