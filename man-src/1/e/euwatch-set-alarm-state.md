---
title: "euwatch-set-alarm-state(1)"
name: "euwatch-set-alarm-state"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euwatch-set-alarm-state/"
description: "euwatch-set-alarm-state – Temporarily set the state of an alarm"
---

<h2>NAME</h2>
<p> euwatch-set-alarm-state &#8211; Temporarily set the state of an alarm</p>
<h2>SYNOPSIS</h2>
<p> euwatch-set-alarm-state <code>&#8211;state-value</code> {ALARM,INSUFFICIENT_DATA,OK}</p>
<dl>
<dt><code>&#8211;state-reason</code> REASON</p>
<dd> [&#8211;state-reason-data JSON] [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ALARM</dl>
<h2>DESCRIPTION</h2>
<p> Temporarily set the state of an alarm</p>
<h3>positional arguments:</h3>
<dl>
<dt>ALARM</p>
<dd> name of the alarm to update (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;state-value</code> {ALARM,INSUFFICIENT_DATA,OK}</p>
<dd> state to set the alarm to (required)</p>
<dt><code>&#8211;state-reason</code> REASON</p>
<dd> human-readable reason why the alarm was set to this state (required)</p>
<dt><code>&#8211;state-reason-data</code> JSON</p>
<dd> JSON-formatted reason why the alarm was set to this state</p>
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
