---
title: "euca-describe-volumes(1)"
name: "euca-describe-volumes"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-volumes/"
description: "euca-describe-volumes – Display information about volumes"
---

<h2>NAME</h2>
<p> euca-describe-volumes &#8211; Display information about volumes</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-volumes [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</p>
<dd> [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [VOLUME [VOLUME &#8230;]]</dl>
<h2>DESCRIPTION</h2>
<p> Display information about volumes</p>
<h3>positional arguments:</h3>
<dl>
<dt>VOLUME</p>
<dd> limit results to specific volumes</dl>
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
<dt>attachment.attach-time</p>
<dd> attachment start time</p>
<dt>attachment.delete-on-termination</p>
<dd> whether the volume will be deleted upon instance termination</p>
<dt>attachment.device</p>
<dd> device node exposed to the instance</p>
<dt>attachment.instance-id</p>
<dd> ID of the instance the volume is attached to</p>
<dt>attachment.status</p>
<dd> attachment state availability-zone create-time creation time size size in GiB snapshot-id snapshot from which the volume was created status tag-key key of a tag assigned to the volume tag-value value of a tag assigned to the volume tag:KEY specific tag key/value combination volume-id volume-type </p>
</dl>
<h2>Index</h2>
