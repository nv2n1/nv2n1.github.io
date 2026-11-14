---
title: "euca-describe-bundle-tasks(1)"
name: "euca-describe-bundle-tasks"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-bundle-tasks/"
description: "euca-describe-bundle-tasks – Describe current instance-bundling tasks"
---

<h2>NAME</h2>
<p> euca-describe-bundle-tasks &#8211; Describe current instance-bundling tasks</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-bundle-tasks [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</p>
<dd> [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [BUNDLE [BUNDLE &#8230;]]</dl>
<h2>DESCRIPTION</h2>
<p> Describe current instance-bundling tasks</p>
<h3>positional arguments:</h3>
<dl>
<dt>BUNDLE</p>
<dd> limit results to specific bundle tasks</dl>
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
<dt>bundle-id</p>
<dd> bundle task ID</p>
<dt>error-code</p>
<dd> if the task failed, the error code returned</p>
<dt>error-message</p>
<dd> if the task failed, the error message returned</p>
<dt>instance-id</p>
<dd> ID of the bundled instance</p>
<dt>progress</p>
<dd> level of task completion, in percent</p>
<dt>s3-bucket</p>
<dd> bucket where the image will be stored</p>
<dt>s3-prefix</p>
<dd> beginning of the bundle name</p>
<dt>start-time</p>
<dd> task start time</p>
<dt>state</p>
<dd> task state</p>
<dt>update-time</p>
<dd> most recent task update time </p>
</dl>
<h2>Index</h2>
