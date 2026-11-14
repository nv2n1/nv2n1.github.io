---
title: "euwatch-describe-alarms-for-metric(1)"
name: "euwatch-describe-alarms-for-metric"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euwatch-describe-alarms-for-metric/"
description: "euwatch-describe-alarms-for-metric – Describe alarms for a single metric."
---

<h2>NAME</h2>
<p> euwatch-describe-alarms-for-metric &#8211; Describe alarms for a single metric.</p>
<h2>SYNOPSIS</h2>
<p> euwatch-describe-alarms-for-metric <code>&#8211;metric-name</code> METRIC <code>&#8211;namespace</code></p>
<dl>
<dt>NAMESPACE</p>
<dd> [&#8211;dimensions KEY1=VALUE1,KEY2=VALUE2,&#8230;] [&#8211;period SECONDS] [&#8211;show-long] [&#8211;statistic {Average,Maximum,Minimum,SampleCount,Sum}] [&#8211;unit UNIT] [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dl>
<h2>DESCRIPTION</h2>
<p> Describe alarms for a single metric.</p>
<h2>DESCRIPTION</h2>
<p> Note that all of an alarm&#8217;s metrics must match exactly to obtain any results.</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;metric-name</code> METRIC</p>
<dd> name of the metric (required)</p>
<dt><code>&#8211;namespace</code> NAMESPACE</p>
<dd> namespace of the metric (required)</p>
<dt><code>&#8211;dimensions</code> KEY1=VALUE1,KEY2=VALUE2,&#8230;</p>
<dd> dimensions of the metric</p>
<dt><code>&#8211;period</code> SECONDS</p>
<dd> period over which statistics are applied</p>
<dt><code>&#8211;show-long</code></p>
<dd> show all of the alarms&#8217; info</p>
<dt><code>&#8211;statistic</code> {Average,Maximum,Minimum,SampleCount,Sum}</p>
<dd> statistic of the metric on which to trigger alarms</p>
<dt><code>&#8211;unit</code> UNIT</p>
<dd> unit of measurement for statistics</p>
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
