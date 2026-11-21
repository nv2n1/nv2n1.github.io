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
<dt>[-n NAMESPACE] [&#8211;show-empty-fields] [-U URL]</dt>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Show a list of monitoring metrics</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-d</code> KEY1=VALUE1,KEY2=VALUE2,&#8230;, <code>&#8211;dimensions</code> KEY1=VALUE1,KEY2=VALUE2,&#8230;</dt>
<dd> limit results to metrics with specific dimensions</dd>
<dt><code>-m</code> METRIC, <code>&#8211;metric-name</code> METRIC</dt>
<dd> limit results to a specific metric</dd>
<dt><code>-n</code> NAMESPACE, <code>&#8211;namespace</code> NAMESPACE</dt>
<dd> limit results to metrics in a specific namespace</dd>
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
