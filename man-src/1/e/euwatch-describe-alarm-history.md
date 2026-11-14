---
title: "euwatch-describe-alarm-history(1)"
name: "euwatch-describe-alarm-history"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euwatch-describe-alarm-history/"
description: "euwatch-describe-alarm-history – Retrieve history for one alarm or all alarms"
---

<h2>NAME</h2>
<p> euwatch-describe-alarm-history &#8211; Retrieve history for one alarm or all alarms</p>
<h2>SYNOPSIS</h2>
<p> euwatch-describe-alarm-history [&#8211;end-date DATE]</p>
<dl>
<dt>[&#8211;history-item-type {Action,ConfigurationUpdate,StateUpdate}]</p>
<dd> [&#8211;show-long] [&#8211;start-date DATE] [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [ALARM]</dl>
<h2>DESCRIPTION</h2>
<p> Retrieve history for one alarm or all alarms</p>
<h3>positional arguments:</h3>
<dl>
<dt>ALARM</p>
<dd> limit results to a specific alarm</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;end-date</code> DATE</p>
<dd> limit results to history before a given point in time</p>
<dt><code>&#8211;history-item-type</code> {Action,ConfigurationUpdate,StateUpdate}</p>
<dd> limit results to specific history item types</p>
<dt><code>&#8211;show-long</code></p>
<dd> show detailed event data as machine-readable JSON</p>
<dt><code>&#8211;start-date</code> DATE</p>
<dd> limit results to history after a given point in time</p>
<dt><code>&#8211;show-empty-fields</code></p>
<dd> show empty values as &quot;(nil)&quot;</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> instance monitoring service endpoint URL</p>
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
