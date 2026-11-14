---
title: "euscale-resume-processes(1)"
name: "euscale-resume-processes"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euscale-resume-processes/"
description: "euscale-resume-processes – Resume an auto-scaling group’s auto-scaling processes"
---

<h2>NAME</h2>
<p> euscale-resume-processes &#8211; Resume an auto-scaling group&#8217;s auto-scaling processes</p>
<h2>SYNOPSIS</h2>
<p> euscale-resume-processes [&#8211;processes PROCESS1,PROCESS2,&#8230;] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</p>
<dd> [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ASGROUP</dl>
<h2>DESCRIPTION</h2>
<p> Resume an auto-scaling group&#8217;s auto-scaling processes</p>
<h3>positional arguments:</h3>
<dl>
<dt>ASGROUP</p>
<dd> name of the auto-scaling group to update (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;processes</code> PROCESS1,PROCESS2,&#8230;</p>
<dd> comma-separated list of auto-scaling processes to resume (default: all processes)</p>
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
