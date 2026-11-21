---

title: "euscale-describe-scheduled-actions(1)"
name: "euscale-describe-scheduled-actions"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euscale-describe-scheduled-actions/"
description: "euscale-describe-scheduled-actions – Describe scheduled auto-scaling group actions"
---

<h2>NAME</h2>
<p> euscale-describe-scheduled-actions &#8211; Describe scheduled auto-scaling group actions</p>
<p> euscale-describe-scheduled-actions [-g ASGROUP]</p>
<dl>
<dt>[&#8211;start-time YYYY-MM-DDThh:mm:ssZ]</dt>
<dd> [&#8211;end-time YYYY-MM-DDThh:mm:ssZ] [&#8211;show-long] [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [ACTION [ACTION &#8230;]]</dd></dl>
<p> Describe scheduled auto-scaling group actions</p>
<h3>positional arguments:</h3>
<dl>
<dt>ACTION</dt>
<dd> limit results to specific actions</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt> <code>-g</code> ASGROUP, <code>&#8211;group</code> ASGROUP</dt>
<dt><code>&#8211;start-time</code> YYYY-MM-DDThh:mm:ssZ</dt>
<dd>
</dd><dd>earliest start time to return scheduled actions for. This is ignored when specific action names are provided.</dd>
<dt><code>&#8211;end-time</code> YYYY-MM-DDThh:mm:ssZ</dt>
<dd> latest start time to return scheduled actions for. This is ignored when specific action names are provided.</dd>
<dt><code>&#8211;show-long</code></dt>
<dd> show all of the scheduled actions&#8217; info</dd>
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
