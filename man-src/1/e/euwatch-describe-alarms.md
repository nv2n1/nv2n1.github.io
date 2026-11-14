---
title: "euwatch-describe-alarms(1)"
name: "euwatch-describe-alarms"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euwatch-describe-alarms/"
description: "euwatch-describe-alarms – Describe alarms"
---

<h2>NAME</h2>
<p> euwatch-describe-alarms &#8211; Describe alarms</p>
<h2>SYNOPSIS</h2>
<p> euwatch-describe-alarms [&#8211;action-prefix PREFIX]</p>
<dl>
<dt>[&#8211;alarm-name-prefix PREFIX] [&#8211;show-long]</p>
<dd> [&#8211;state-value {OK,ALARM,INSUFFICIENT_DATA}] [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [ALARM [ALARM &#8230;]]</dl>
<h2>DESCRIPTION</h2>
<p> Describe alarms</p>
<h3>positional arguments:</h3>
<dl>
<dt>ALARM</p>
<dd> limit results to specific alarms</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;action-prefix</code> PREFIX</p>
<dd> limit results to alarms whose actions&#8217; ARNs begin with a specific string</p>
<dt><code>&#8211;alarm-name-prefix</code> PREFIX</p>
<dd> limit results to alarms whose names begin with a specific string</p>
<dt><code>&#8211;show-long</code></p>
<dd> show all of the alarms&#8217; info</p>
<dt><code>&#8211;state-value</code> {OK,ALARM,INSUFFICIENT_DATA}</p>
<dd> limit results to alarms in a specific state</p>
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
