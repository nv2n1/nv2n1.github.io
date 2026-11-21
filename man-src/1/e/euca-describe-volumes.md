---

title: "euca-describe-volumes(1)"
name: "euca-describe-volumes"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-volumes/"
description: "euca-describe-volumes – Display information about volumes"
---

<p> euca-describe-volumes &#8211; Display information about volumes</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-volumes [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</dt>
<dd> [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [VOLUME [VOLUME &#8230;]]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Display information about volumes</p>
<h3>positional arguments:</h3>
<dl>
<dt>VOLUME</dt>
<dd> limit results to specific volumes</dd></dl>
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
<dt>attachment.attach-time</dt>
<dd> attachment start time</dd>
<dt>attachment.delete-on-termination</dt>
<dd> whether the volume will be deleted upon instance termination</dd>
<dt>attachment.device</dt>
<dd> device node exposed to the instance</dd>
<dt>attachment.instance-id</dt>
<dd> ID of the instance the volume is attached to</dd>
<dt>attachment.status</dt>
<dd> attachment state availability-zone create-time creation time size size in GiB snapshot-id snapshot from which the volume was created status tag-key key of a tag assigned to the volume tag-value value of a tag assigned to the volume tag:KEY specific tag key/value combination volume-id volume-type </dd>
</dl>
