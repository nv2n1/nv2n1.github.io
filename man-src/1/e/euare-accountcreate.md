---
title: "euare-accountcreate(1)"
name: "euare-accountcreate"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-accountcreate/"
description: "euare-accountcreate – [Eucalyptus cloud admin only] Create a new account"
---

<h2>NAME</h2>
<p> euare-accountcreate &#8211; [Eucalyptus cloud admin only] Create a new account</p>
<h2>SYNOPSIS</h2>
<p> euare-accountcreate [-k] [-w] [-d DOMAIN] [-l] [&#8211;show-empty-fields]</p>
<dl>
<dt>[-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID]</p>
<dd> [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [ACCOUNT]</dl>
<h2>DESCRIPTION</h2>
<p> [Eucalyptus cloud admin only] Create a new account</p>
<h3>positional arguments:</h3>
<dl>
<dt>ACCOUNT</p>
<dd> also add an alias (name) to the new account (required on eucalyptus &lt; 4.2)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-k</code>, <code>&#8211;create-accesskey</code></p>
<dd> also create an access key for the new account&#8217;s administrator and show it</p>
<dt><code>-w</code>, <code>&#8211;write-config</code></p>
<dd> output access keys and region information in the form of a <a href="/docs/linux/man/5-euca2ools-ini/">euca2ools.ini</a>(5) configuration file instead of by themselves (implies <code>-k</code>)</p>
<dt><code>-d</code> DOMAIN, <code>&#8211;domain</code> DOMAIN</p>
<dd> the DNS domain to use for region information in configuration file output (default: based on IAM URL)</p>
<dt><code>-l</code>, <code>&#8211;set-default-user</code></p>
<dd> set this user as the default user for the region in <a href="/docs/linux/man/5-euca2ools-ini/">euca2ools.ini</a>(5) configuration file output. This option is only useful when used with <code>-w</code>.</p>
<dt><code>&#8211;show-empty-fields</code></p>
<dd> show empty values as &quot;(nil)&quot;</p>
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
