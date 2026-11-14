---
title: "euscale-execute-policy(1)"
name: "euscale-execute-policy"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euscale-execute-policy/"
description: "euscale-execute-policy – Manually set an auto-scaling instance’s health status"
---

<h2>NAME</h2>
<p> euscale-execute-policy &#8211; Manually set an auto-scaling instance&#8217;s health status</p>
<h2>SYNOPSIS</h2>
<p> euscale-execute-policy [-g ASGROUP] [-h] [-H] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</p>
<dd> [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [&#8211;help] POLICY</dl>
<h2>DESCRIPTION</h2>
<p> Manually set an auto-scaling instance&#8217;s health status</p>
<h3>positional arguments:</h3>
<dl>
<dt>POLICY</p>
<dd> name or ARN of the policy to run (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-g</code> ASGROUP, <code>&#8211;auto-scaling-group</code> ASGROUP</p>
<dd> name or ARN of the auto-scaling group</p>
<dt><code>-h</code>, <code>&#8211;honor-cooldown</code></p>
<dd> reject the request if the group is in cooldown (default: override any cooldown period)</p>
<dt><code>-H</code>, <code>&#8211;no-honor-cooldown</code></p>
<dd> override any cooldown period (this is the default)</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> auto-scaling service endpoint URL</p>
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
<dt><code>&#8211;help</code></p>
<dd> show this help message and exit </p>
</dl>
<h2>Index</h2>
