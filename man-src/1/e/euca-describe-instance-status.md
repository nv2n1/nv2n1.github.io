---
title: "euca-describe-instance-status(1)"
name: "euca-describe-instance-status"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-instance-status/"
description: "euca-describe-instance-status – Show information about instance status and scheduled events"
---

<h2>NAME</h2>
<p> euca-describe-instance-status &#8211; Show information about instance status and scheduled events</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-instance-status [&#8211;hide-healthy]</p>
<dl>
<dt>[&#8211;include-all-instances]</dt>
<dd> [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [INSTANCE [INSTANCE &#8230;]]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Show information about instance status and scheduled events</p>
<h3>positional arguments:</h3>
<dl>
<dt>INSTANCE</dt>
<dd> limit results to specific instances</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;hide-healthy</code></dt>
<dd> hide instances where all status checks pass</dd>
<dt><code>&#8211;include-all-instances</code></dt>
<dd> show all instances, not just those that are running</dd>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> compute service endpoint URL</dd>
<dt><code>&#8211;region</code> USER [at] REGION</dt>
<dd> region and/or user names to search when looking up config file data</dd>
<dt> <code>-I</code> KEY_ID, <code>&#8211;access-key-id</code> KEY_ID</dt>
<dt> <code>-S</code> KEY, <code>&#8211;secret-key</code> KEY</dt>
<dt> <code>&#8211;security-token</code> TOKEN</dt>
<dt><code>&#8211;filter</code> NAME=VALUE</dt>
<dd>
</dd><dd>restrict results to those that meet criteria</dd>
<dt><code>&#8211;debug</code></dt>
<dd> show debugging output</dd>
<dt><code>&#8211;debugger</code></dt>
<dd> launch interactive debugger on error</dd>
<dt><code>&#8211;version</code></dt>
<dd> show the program&#8217;s version and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit</dd></dl>
<h3>allowed filter names:</h3>
<p> availability-zone event.code the code identifying the type of event event.description an event&#8217;s description event.not-after an event&#8217;s latest possible end time event.not-before an event&#8217;s earliest possible start time instance-state-code numeric code identifying instance state instance-state-name instance state instance-status.status instance&#8217;s status</p>
<dl>
<dt>instance-status.reachability</dt>
<dd> instance&#8217;s reachability status</dd>
<dt>system-status.status</dt>
<dd> instance&#8217;s system status</dd>
<dt>system-status.reachability</dt>
<dd> instance&#8217;s system reachability status </dd>
</dl>
<h2>Index</h2>
