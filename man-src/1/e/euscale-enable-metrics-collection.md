---

title: "euscale-enable-metrics-collection(1)"
name: "euscale-enable-metrics-collection"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euscale-enable-metrics-collection/"
description: "euscale-enable-metrics-collection – Enable monitoring of an auto-scaling group’s group metrics"
---

<h2>NAME</h2>
<p> euscale-enable-metrics-collection &#8211; Enable monitoring of an auto-scaling group&#8217;s group metrics</p>
<p> euscale-enable-metrics-collection <code>-g</code> GRANULARITY</p>
<dl>
<dt>[-m METRIC1,METRIC2,&#8230;] [-U URL]</dt>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ASGROUP</dd></dl>
<p> Enable monitoring of an auto-scaling group&#8217;s group metrics</p>
<h3>positional arguments:</h3>
<dl>
<dt>ASGROUP</dt>
<dd> name of the auto-scaling group to update (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-g</code> GRANULARITY, <code>&#8211;granularity</code> GRANULARITY</dt>
<dd> granularity at which to collect metrics (e.g., &#8216;1Minute&#8217;) (required)</dd>
<dt><code>-m</code> METRIC1,METRIC2,&#8230;, <code>&#8211;metrics</code> METRIC1,METRIC2,&#8230;</dt>
<dd> list of metrics to collect (default: all metrics)</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> auto-scaling service endpoint URL</dd>
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
