---

title: "euscale-describe-scaling-activities(1)"
name: "euscale-describe-scaling-activities"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euscale-describe-scaling-activities/"
description: "euscale-describe-scaling-activities – Describe past and current auto-scaling activities"
---

<h2>NAME</h2>
<p> euscale-describe-scaling-activities &#8211; Describe past and current auto-scaling activities</p>
<p> euscale-describe-scaling-activities [-g ASGROUP] [&#8211;show-long]</p>
<dl>
<dt>[&#8211;show-empty-fields] [-U URL]</dt>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [ACTIVITY [ACTIVITY &#8230;]]</dd></dl>
<p> Describe past and current auto-scaling activities</p>
<h3>positional arguments:</h3>
<dl>
<dt>ACTIVITY</dt>
<dd> limit results to specific auto-scaling activities</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-g</code> ASGROUP, <code>&#8211;auto-scaling-group</code> ASGROUP</dt>
<dd> name of an Auto Scaling group by which to filter the request</dd>
<dt><code>&#8211;show-long</code></dt>
<dd> show all of the activities&#8217; info</dd>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
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
