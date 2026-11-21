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
<dt>[&#8211;alarm-name-prefix PREFIX] [&#8211;show-long]</dt>
<dd> [&#8211;state-value {OK,ALARM,INSUFFICIENT_DATA}] [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [ALARM [ALARM &#8230;]]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Describe alarms</p>
<h3>positional arguments:</h3>
<dl>
<dt>ALARM</dt>
<dd> limit results to specific alarms</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;action-prefix</code> PREFIX</dt>
<dd> limit results to alarms whose actions&#8217; ARNs begin with a specific string</dd>
<dt><code>&#8211;alarm-name-prefix</code> PREFIX</dt>
<dd> limit results to alarms whose names begin with a specific string</dd>
<dt><code>&#8211;show-long</code></dt>
<dd> show all of the alarms&#8217; info</dd>
<dt><code>&#8211;state-value</code> {OK,ALARM,INSUFFICIENT_DATA}</dt>
<dd> limit results to alarms in a specific state</dd>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> instance monitoring service endpoint URL</dd>
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
