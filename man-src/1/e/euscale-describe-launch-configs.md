---
title: "euscale-describe-launch-configs(1)"
name: "euscale-describe-launch-configs"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euscale-describe-launch-configs/"
description: "euscale-describe-launch-configs – Describe auto-scaling instance launch configurations"
---

<h2>NAME</h2>
<p> euscale-describe-launch-configs &#8211; Describe auto-scaling instance launch configurations</p>
<h2>SYNOPSIS</h2>
<p> euscale-describe-launch-configs [&#8211;show-long] [&#8211;show-empty-fields]</p>
<dl>
<dt>[-U URL] [&#8211;region USER [at] REGION]</p>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [LAUNCHCONFIG [LAUNCHCONFIG &#8230;]]</dl>
<h2>DESCRIPTION</h2>
<p> Describe auto-scaling instance launch configurations</p>
<h3>positional arguments:</h3>
<dl>
<dt>LAUNCHCONFIG</p>
<dd> limit results to specific launch configurations</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;show-long</code></p>
<dd> show all of the launch configurations&#8217; info</p>
<dt><code>&#8211;show-empty-fields</code></p>
<dd> show empty values as &quot;(nil)&quot;</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> auto-scaling service endpoint URL</p>
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
