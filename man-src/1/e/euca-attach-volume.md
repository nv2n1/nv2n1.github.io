---
title: "euca-attach-volume(1)"
name: "euca-attach-volume"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-attach-volume/"
description: "euca-attach-volume – Attach an EBS volume to an instance"
---

<h2>NAME</h2>
<p> euca-attach-volume &#8211; Attach an EBS volume to an instance</p>
<h2>SYNOPSIS</h2>
<p> euca-attach-volume <code>-i</code> INSTANCE <code>-d</code> DEVICE [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</p>
<dd> [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] VOLUME</dl>
<h2>DESCRIPTION</h2>
<p> Attach an EBS volume to an instance</p>
<h3>positional arguments:</h3>
<dl>
<dt>VOLUME</p>
<dd> ID of the volume to attach (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-i</code> INSTANCE, <code>&#8211;instance</code> INSTANCE</p>
<dd> instance to attach the volume to (required)</p>
<dt><code>-d</code> DEVICE, <code>&#8211;device</code> DEVICE</p>
<dd> device name exposed to the instance (required)</p>
<dt><code>&#8211;show-empty-fields</code></p>
<dd> show empty values as &quot;(nil)&quot;</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> compute service endpoint URL</p>
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
