---
title: "euwatch-list-metrics(1)"
name: "euwatch-list-metrics"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euwatch-list-metrics/"
description: "euwatch-list-metrics – Show a list of monitoring metrics"
---

<h2>NAME</h2>
<p> euwatch-list-metrics &#8211; Show a list of monitoring metrics</p>
<h2>SYNOPSIS</h2>
<p> euwatch-list-metrics [-d KEY1=VALUE1,KEY2=VALUE2,&#8230;] [-m METRIC]</p>
<dl>
<dt>[-n NAMESPACE] [&#8211;show-empty-fields] [-U URL]</p>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dl>
<h2>DESCRIPTION</h2>
<p> Show a list of monitoring metrics</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-d</code> KEY1=VALUE1,KEY2=VALUE2,&#8230;, <code>&#8211;dimensions</code> KEY1=VALUE1,KEY2=VALUE2,&#8230;</p>
<dd> limit results to metrics with specific dimensions</p>
<dt><code>-m</code> METRIC, <code>&#8211;metric-name</code> METRIC</p>
<dd> limit results to a specific metric</p>
<dt><code>-n</code> NAMESPACE, <code>&#8211;namespace</code> NAMESPACE</p>
<dd> limit results to metrics in a specific namespace</p>
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
