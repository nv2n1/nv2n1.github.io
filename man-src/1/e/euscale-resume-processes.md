---

title: "euscale-resume-processes(1)"
name: "euscale-resume-processes"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euscale-resume-processes/"
description: "euscale-resume-processes – Resume an auto-scaling group’s auto-scaling processes"
---

<p> euscale-resume-processes &#8211; Resume an auto-scaling group&#8217;s auto-scaling processes</p>
<h2>SYNOPSIS</h2>
<p> euscale-resume-processes [&#8211;processes PROCESS1,PROCESS2,&#8230;] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</dt>
<dd> [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ASGROUP</dd></dl>
<h2>DESCRIPTION</h2>
<p> Resume an auto-scaling group&#8217;s auto-scaling processes</p>
<h3>positional arguments:</h3>
<dl>
<dt>ASGROUP</dt>
<dd> name of the auto-scaling group to update (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;processes</code> PROCESS1,PROCESS2,&#8230;</dt>
<dd> comma-separated list of auto-scaling processes to resume (default: all processes)</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> auto-scaling service endpoint URL</dd>
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
