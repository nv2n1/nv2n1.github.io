---
title: "euare-userenablemfadevice(1)"
name: "euare-userenablemfadevice"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-userenablemfadevice/"
description: "euare-userenablemfadevice – Enable an MFA device"
---

<h2>NAME</h2>
<p> euare-userenablemfadevice &#8211; Enable an MFA device</p>
<h2>SYNOPSIS</h2>
<p> euare-userenablemfadevice <code>-s</code> SERIAL <code>-c1</code> CODE <code>-c2</code> CODE</p>
<dl>
<dt>[&#8211;as-account ACCOUNT] [-U URL]</p>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] USER</dl>
<h2>DESCRIPTION</h2>
<p> Enable an MFA device</p>
<h3>positional arguments:</h3>
<dl>
<dt>USER</p>
<dd> user to enable the MFA device for (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-s</code> SERIAL, <code>&#8211;serial-number</code> SERIAL</p>
<dd> serial number of the MFA device to activate (required)</p>
<dt><code>-c1</code> CODE</p>
<dd> an authentication code emitted by the MFA device (required)</p>
<dt><code>-c2</code> CODE</p>
<dd> a subsequent authentication code emitted by the MFA device (required)</p>
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
