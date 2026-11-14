---
title: "euca-generate-environment-config(1)"
name: "euca-generate-environment-config"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-generate-environment-config/"
description: "euca-generate-environment-config – Read environment variables and euca2ools.ini(5) files to discover the service URLs and credentials for a region, then output shellcode with the corresponding envi..."
---

<h2>NAME</h2>
<p> euca-generate-environment-config &#8211; Read environment variables and <a href="/docs/linux/man/5-euca2ools-ini/">euca2ools.ini</a>(5) files to discover the service URLs and credentials for a region, then output shellcode with the corresponding environment variables for that information. This output will contain secret access keys and should be treated with care.</p>
<h2>SYNOPSIS</h2>
<p> euca-generate-environment-config [&#8211;simple] [-I KEY_ID] [-S KEY]</p>
<dl>
<dt>[&#8211;security-token TOKEN]</p>
<dd> [&#8211;region USER [at] REGION] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dl>
<h2>DESCRIPTION</h2>
<p> Read environment variables and <a href="/docs/linux/man/5-euca2ools-ini/">euca2ools.ini</a>(5) files to discover the service URLs and credentials for a region, then output shellcode with the corresponding environment variables for that information. This output will contain secret access keys and should be treated with care.</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;simple</code></p>
<dd> use a simpler output format intended for consumption by scripts</p>
<dt> <code>-I</code> KEY_ID, <code>&#8211;access-key-id</code> KEY_ID</p>
<dt> <code>-S</code> KEY, <code>&#8211;secret-key</code> KEY</p>
<dt> <code>&#8211;security-token</code> TOKEN</p>
<dt><code>&#8211;region</code> USER [at] REGION</p>
<dd>
<dd>region and/or user names to search when looking up config file data</p>
<dt><code>&#8211;debug</code></p>
<dd> show debugging output</p>
<dt><code>&#8211;debugger</code></p>
<dd> launch interactive debugger on error</p>
<dt><code>&#8211;version</code></p>
<dd> show the program&#8217;s version and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit </p>
</dl>
<h2>Index</h2>
