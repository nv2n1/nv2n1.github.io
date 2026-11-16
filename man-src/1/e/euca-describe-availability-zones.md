---
title: "euca-describe-availability-zones(1)"
name: "euca-describe-availability-zones"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-availability-zones/"
description: "euca-describe-availability-zones – Display availability zones within the current region"
---

<h2>NAME</h2>
<p> euca-describe-availability-zones &#8211; Display availability zones within the current region</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-availability-zones [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID]</dt>
<dd> [-S KEY] [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [ZONE [ZONE &#8230;]]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Display availability zones within the current region</p>
<h3>positional arguments:</h3>
<dl>
<dt>ZONE</dt>
<dd> limit results to specific availability zones</dd></dl>
<h3>optional arguments:</h3>
<dl>
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
<dl>
<dt>message</dt>
<dd> message giving information about the availability zone</dd>
<dt>region-name</dt>
<dd> region the availability zone is in</dd>
<dt>state</dt>
<dd> state of the availability zone</dd>
<dt>zone-name</dt>
<dd> name of the availability zone </dd>
</dl>
<h2>Index</h2>
