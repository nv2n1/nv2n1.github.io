---
title: "euwatch-get-stats(1)"
name: "euwatch-get-stats"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euwatch-get-stats/"
description: "euwatch-get-stats – Show a metric’s statistics"
---

<h2>NAME</h2>
<p> euwatch-get-stats &#8211; Show a metric&#8217;s statistics</p>
<h2>SYNOPSIS</h2>
<p> euwatch-get-stats <code>-n</code> NAMESPACE <code>-s</code> STAT1,STAT2,&#8230;</p>
<dl>
<dt>[&#8211;dimensions KEY1=VALUE1,KEY2=VALUE2,&#8230;]</p>
<dd> [&#8211;start-time YYYY-MM-DDThh:mm:ssZ] [&#8211;end-time YYYY-MM-DDThh:mm:ssZ] [&#8211;period SECONDS] [&#8211;unit UNIT] [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] METRIC</dl>
<h2>DESCRIPTION</h2>
<p> Show a metric&#8217;s statistics</p>
<h3>positional arguments:</h3>
<dl>
<dt>METRIC</p>
<dd> name of the metric to get statistics for (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-n</code> NAMESPACE, <code>&#8211;namespace</code> NAMESPACE</p>
<dd> the metric&#8217;s namespace (required)</p>
<dt><code>-s</code> STAT1,STAT2,&#8230;, <code>&#8211;statistics</code> STAT1,STAT2,&#8230;</p>
<dd> the metric statistics to show (at least 1 required)</p>
<dt><code>&#8211;dimensions</code> KEY1=VALUE1,KEY2=VALUE2,&#8230;</p>
<dd> the dimensions of the metric to show</p>
<dt><code>&#8211;start-time</code> YYYY-MM-DDThh:mm:ssZ</p>
<dd> earliest time to retrieve data points for (default: one hour ago)</p>
<dt><code>&#8211;end-time</code> YYYY-MM-DDThh:mm:ssZ</p>
<dd> latest time to retrieve data points for (default: now)</p>
<dt><code>&#8211;period</code> SECONDS</p>
<dd> granularity of the returned data points (must be a multiple of 60) (default: 60)</p>
<dt><code>&#8211;unit</code> UNIT</p>
<dd> unit the metric is reported in</p>
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
