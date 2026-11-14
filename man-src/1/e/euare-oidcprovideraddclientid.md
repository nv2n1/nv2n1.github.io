---
title: "euare-oidcprovideraddclientid(1)"
name: "euare-oidcprovideraddclientid"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-oidcprovideraddclientid/"
description: "euare-oidcprovideraddclientid – Add a client ID to an OpenID Connect provider"
---

<h2>NAME</h2>
<p> euare-oidcprovideraddclientid &#8211; Add a client ID to an OpenID Connect provider</p>
<h2>SYNOPSIS</h2>
<p> euare-oidcprovideraddclientid <code>-c</code> CLIENT [&#8211;as-account ACCOUNT] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID]</p>
<dd> [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] OIDC</dl>
<h2>DESCRIPTION</h2>
<p> Add a client ID to an OpenID Connect provider</p>
<h3>positional arguments:</h3>
<dl>
<dt>OIDC</p>
<dd> the ARN of the provider to update (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-c</code> CLIENT, <code>&#8211;client-id</code> CLIENT</p>
<dd> the client ID to add to the provider (required)</p>
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
