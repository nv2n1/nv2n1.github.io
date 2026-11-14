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
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID]</p>
<dd> [-S KEY] [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [ZONE [ZONE &#8230;]]</dl>
<h2>DESCRIPTION</h2>
<p> Display availability zones within the current region</p>
<h3>positional arguments:</h3>
<dl>
<dt>ZONE</p>
<dd> limit results to specific availability zones</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;show-empty-fields</code></p>
<dd> show empty values as &quot;(nil)&quot;</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> compute service endpoint URL</p>
<dt><code>&#8211;region</code> USER [at] REGION</p>
<dd> region and/or user names to search when looking up config file data</p>
<dt> <code>-I</code> KEY_ID, <code>&#8211;access-key-id</code> KEY_ID</p>
<dt> <code>-S</code> KEY, <code>&#8211;secret-key</code> KEY</p>
<dt> <code>&#8211;security-token</code> TOKEN</p>
<dt><code>&#8211;filter</code> NAME=VALUE</p>
<dd>
<dd>restrict results to those that meet criteria</p>
<dt><code>&#8211;debug</code></p>
<dd> show debugging output</p>
<dt><code>&#8211;debugger</code></p>
<dd> launch interactive debugger on error</p>
<dt><code>&#8211;version</code></p>
<dd> show the program&#8217;s version and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit</dl>
<h3>allowed filter names:</h3>
<dl>
<dt>message</p>
<dd> message giving information about the availability zone</p>
<dt>region-name</p>
<dd> region the availability zone is in</p>
<dt>state</p>
<dd> state of the availability zone</p>
<dt>zone-name</p>
<dd> name of the availability zone </p>
</dl>
<h2>Index</h2>
