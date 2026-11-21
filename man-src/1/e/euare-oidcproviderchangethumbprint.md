---

title: "euare-oidcproviderchangethumbprint(1)"
name: "euare-oidcproviderchangethumbprint"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-oidcproviderchangethumbprint/"
description: "euare-oidcproviderchangethumbprint – Replace an OpenID Connect provider’s list of thumbprints"
---

<p> euare-oidcproviderchangethumbprint &#8211; Replace an OpenID Connect provider&#8217;s list of thumbprints</p>
<h2>SYNOPSIS</h2>
<p> euare-oidcproviderchangethumbprint [-t HEX] [&#8211;as-account ACCOUNT]</p>
<dl>
<dt>[-U URL] [&#8211;region USER [at] REGION]</dt>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] OIDC</dd></dl>
<h2>DESCRIPTION</h2>
<p> Replace an OpenID Connect provider&#8217;s list of thumbprints</p>
<h3>positional arguments:</h3>
<dl>
<dt>OIDC</dt>
<dd> the ARN of the provider to update (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-t</code> HEX, <code>&#8211;thumbprint</code> HEX</dt>
<dd> the new SHA-1 thumbprint of the OpenID Connect provider&#8217;s certificate. This option may be specified more than once to allow multiple certificates to be accepted. If one is not supplied this command will attempt to determine it automatically.</dd>
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
