---

title: "euscale-delete-notification-configuration(1)"
name: "euscale-delete-notification-configuration"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euscale-delete-notification-configuration/"
description: "euscale-delete-notification-configuration – Delete an auto-scaling group’s notification configuration"
---

<h2>NAME</h2>
<p> euscale-delete-notification-configuration &#8211; Delete an auto-scaling group&#8217;s notification configuration</p>
<p> euscale-delete-notification-configuration <code>-t</code> TOPIC [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION]</dt>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ASGROUP</dd></dl>
<p> Delete an auto-scaling group&#8217;s notification configuration</p>
<h3>positional arguments:</h3>
<dl>
<dt>ASGROUP</dt>
<dd> name of the auto-scaling group to update (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-t</code> TOPIC, <code>&#8211;topic-arn</code> TOPIC</dt>
<dd> ARN of the SNS topic associated with the configuration to delete</dd>
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
