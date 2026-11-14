---
title: "euscale-describe-scaling-activities(1)"
name: "euscale-describe-scaling-activities"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euscale-describe-scaling-activities/"
description: "euscale-describe-scaling-activities – Describe past and current auto-scaling activities"
---

<h2>NAME</h2>
<p> euscale-describe-scaling-activities &#8211; Describe past and current auto-scaling activities</p>
<h2>SYNOPSIS</h2>
<p> euscale-describe-scaling-activities [-g ASGROUP] [&#8211;show-long]</p>
<dl>
<dt>[&#8211;show-empty-fields] [-U URL]</p>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [ACTIVITY [ACTIVITY &#8230;]]</dl>
<h2>DESCRIPTION</h2>
<p> Describe past and current auto-scaling activities</p>
<h3>positional arguments:</h3>
<dl>
<dt>ACTIVITY</p>
<dd> limit results to specific auto-scaling activities</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-g</code> ASGROUP, <code>&#8211;auto-scaling-group</code> ASGROUP</p>
<dd> name of an Auto Scaling group by which to filter the request</p>
<dt><code>&#8211;show-long</code></p>
<dd> show all of the activities&#8217; info</p>
<dt><code>&#8211;show-empty-fields</code></p>
<dd> show empty values as &quot;(nil)&quot;</p>
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
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit </p>
</dl>
<h2>Index</h2>
