---
title: "euscale-put-notification-configuration(1)"
name: "euscale-put-notification-configuration"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euscale-put-notification-configuration/"
description: "euscale-put-notification-configuration – Create or replace an auto-scaling group’s notification configuration"
---

<h2>NAME</h2>
<p> euscale-put-notification-configuration &#8211; Create or replace an auto-scaling group&#8217;s notification configuration</p>
<h2>SYNOPSIS</h2>
<p> euscale-put-notification-configuration <code>-n</code> TYPE1,TYPE2,&#8230; <code>-t</code> TOPIC</p>
<dl>
<dt>[-U URL] [&#8211;region USER [at] REGION]</dt>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ASGROUP</dd></dl>
<h2>DESCRIPTION</h2>
<p> Create or replace an auto-scaling group&#8217;s notification configuration</p>
<h3>positional arguments:</h3>
<dl>
<dt>ASGROUP</dt>
<dd> name of the auto-scaling group to update (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-n</code> TYPE1,TYPE2,&#8230;, <code>&#8211;notification-types</code> TYPE1,TYPE2,&#8230;</dt>
<dd> comma-separated list of event types that will trigger notification (required)</dd>
<dt><code>-t</code> TOPIC, <code>&#8211;topic-arn</code> TOPIC</dt>
<dd> ARN of the SNS topic to publish notifications to (required)</dd>
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
