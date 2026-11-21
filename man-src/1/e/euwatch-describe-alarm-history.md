---

title: "euwatch-describe-alarm-history(1)"
name: "euwatch-describe-alarm-history"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euwatch-describe-alarm-history/"
description: "euwatch-describe-alarm-history – Retrieve history for one alarm or all alarms"
---

<p> euwatch-describe-alarm-history &#8211; Retrieve history for one alarm or all alarms</p>
<h2>SYNOPSIS</h2>
<p> euwatch-describe-alarm-history [&#8211;end-date DATE]</p>
<dl>
<dt>[&#8211;history-item-type {Action,ConfigurationUpdate,StateUpdate}]</dt>
<dd> [&#8211;show-long] [&#8211;start-date DATE] [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [ALARM]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Retrieve history for one alarm or all alarms</p>
<h3>positional arguments:</h3>
<dl>
<dt>ALARM</dt>
<dd> limit results to a specific alarm</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;end-date</code> DATE</dt>
<dd> limit results to history before a given point in time</dd>
<dt><code>&#8211;history-item-type</code> {Action,ConfigurationUpdate,StateUpdate}</dt>
<dd> limit results to specific history item types</dd>
<dt><code>&#8211;show-long</code></dt>
<dd> show detailed event data as machine-readable JSON</dd>
<dt><code>&#8211;start-date</code> DATE</dt>
<dd> limit results to history after a given point in time</dd>
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
