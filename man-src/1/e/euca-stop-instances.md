---

title: "euca-stop-instances(1)"
name: "euca-stop-instances"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-stop-instances/"
description: "euca-stop-instances – Stop one or more running instances"
---

<p> euca-stop-instances &#8211; Stop one or more running instances</p>
<h2>SYNOPSIS</h2>
<p> euca-stop-instances [-f] [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</dt>
<dd> [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] INSTANCE [INSTANCE &#8230;]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Stop one or more running instances</p>
<h3>positional arguments:</h3>
<dl>
<dt>INSTANCE</dt>
<dd> ID(s) of the instance(s) to stop</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd> immediately stop the instance(s). Data may be lost</dd>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
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
