---
title: "euca-modify-instance-type(1)"
name: "euca-modify-instance-type"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-modify-instance-type/"
description: "euca-modify-instance-type – [Eucalyptus cloud admin only] Modify an instance type"
---

<h2>NAME</h2>
<p> euca-modify-instance-type &#8211; [Eucalyptus cloud admin only] Modify an instance type</p>
<h2>SYNOPSIS</h2>
<p> euca-modify-instance-type [-c COUNT] [-d GiB] [-m MiB] [-i COUNT]</p>
<dl>
<dt>[&#8211;reset] [&#8211;show-empty-fields] [-U URL]</p>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] INSTANCETYPE</dl>
<h2>DESCRIPTION</h2>
<p> [Eucalyptus cloud admin only] Modify an instance type</p>
<h3>positional arguments:</h3>
<dl>
<dt>INSTANCETYPE</p>
<dd> name of the instance type to modify (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-c</code> COUNT, <code>&#8211;cpus</code> COUNT</p>
<dd> number of virtual CPUs to allocate to each instance</p>
<dt><code>-d</code> GiB, <code>&#8211;disk</code> GiB</p>
<dd> amount of instance storage to allow each instance</p>
<dt><code>-m</code> MiB, <code>&#8211;memory</code> MiB</p>
<dd> amount of RAM to allocate to each instance</p>
<dt><code>-i</code> COUNT, <code>&#8211;network-interfaces</code> COUNT</p>
<dd> maximum network interfaces for each instance (VPC)</p>
<dt><code>&#8211;reset</code></p>
<dd> reset the instance type to its default configuration</p>
<dt><code>&#8211;show-empty-fields</code></p>
<dd> show empty values as &quot;(nil)&quot;</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> compute service endpoint URL</p>
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
