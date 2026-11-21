---

title: "euca-describe-bundle-tasks(1)"
name: "euca-describe-bundle-tasks"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-bundle-tasks/"
description: "euca-describe-bundle-tasks – Describe current instance-bundling tasks"
---

<p> euca-describe-bundle-tasks &#8211; Describe current instance-bundling tasks</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-bundle-tasks [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</dt>
<dd> [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [BUNDLE [BUNDLE &#8230;]]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Describe current instance-bundling tasks</p>
<h3>positional arguments:</h3>
<dl>
<dt>BUNDLE</dt>
<dd> limit results to specific bundle tasks</dd></dl>
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
<dt>bundle-id</dt>
<dd> bundle task ID</dd>
<dt>error-code</dt>
<dd> if the task failed, the error code returned</dd>
<dt>error-message</dt>
<dd> if the task failed, the error message returned</dd>
<dt>instance-id</dt>
<dd> ID of the bundled instance</dd>
<dt>progress</dt>
<dd> level of task completion, in percent</dd>
<dt>s3-bucket</dt>
<dd> bucket where the image will be stored</dd>
<dt>s3-prefix</dt>
<dd> beginning of the bundle name</dd>
<dt>start-time</dt>
<dd> task start time</dd>
<dt>state</dt>
<dd> task state</dd>
<dt>update-time</dt>
<dd> most recent task update time </dd>
</dl>
