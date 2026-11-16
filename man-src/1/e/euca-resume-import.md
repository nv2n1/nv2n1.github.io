---
title: "euca-resume-import(1)"
name: "euca-resume-import"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-resume-import/"
description: "euca-resume-import – Perform the upload step of an import task"
---

<h2>NAME</h2>
<p> euca-resume-import &#8211; Perform the upload step of an import task</p>
<h2>SYNOPSIS</h2>
<p> euca-resume-import <code>-t</code> TASK [-x DAYS] [&#8211;show-empty-fields]</p>
<dl>
<dt>[&#8211;s3-url URL] [-o KEY_ID] [-w KEY]</dt>
<dd> [&#8211;progress | <code>&#8211;no-progress]</code> [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] FILE</dd></dl>
<h2>DESCRIPTION</h2>
<p> Perform the upload step of an import task</p>
<h3>positional arguments:</h3>
<dl>
<dt>FILE</dt>
<dd> file containing the disk image to import (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-t</code> TASK, <code>&#8211;task</code> TASK</dt>
<dd> the ID of the import task to resume (required)</dd>
<dt><code>-x</code> DAYS, <code>&#8211;expires</code> DAYS</dt>
<dd> how long the import manifest should remain valid, in days (default: 30 days)</dd>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
<dt><code>&#8211;s3-url</code> URL</dt>
<dd> object storage service endpoint URL</dd>
<dt><code>-o</code> KEY_ID, <code>&#8211;owner-akid</code> KEY_ID</dt>
<dd> access key to use for the object storage service (default: same as that for the compute service)</dd>
<dt><code>-w</code> KEY, <code>&#8211;owner-sak</code> KEY</dt>
<dd> secret key to use for the object storage service (default: same as that for the compute service)</dd>
<dt><code>&#8211;progress</code></dt>
<dd> show progress (the default when run interactively)</dd>
<dt><code>&#8211;no-progress</code></dt>
<dd> do not show progress (the default when run noninteractively)</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> compute service endpoint URL</dd>
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
<h2>Index</h2>
