---
title: "cgget(1)"
name: "cgget"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cgget/"
description: "cgget – print parameter(s) of given group(s)"
---

<h2>NAME</h2>
<p> cgget &#8211; print parameter(s) of given group(s) </p>
<h2>SYNOPSIS</h2>
<p> <code>cgget</code> [<code>-n</code>] [<code>-v</code>] [<code>-r</code> &lt;<i>name</i>&gt;] [<code>-g</code> &lt;<i>controller</i>&gt;] [<code>-a</code>] &lt;<code>path</code>&gt; &#8230;<br />
 <code>cgget</code> [<code>-n</code>] [<code>-v</code>] [<code>-r</code> &lt;<i>name</i>&gt;] <code>-g</code> &lt;<i>controller</i>&gt;:&lt;<code>path</code>&gt; &#8230; </p>
<h2>DESCRIPTION</h2>
<p> Prints the parameter(s) of input cgroup(s). If neither controller nor variable are specified, the values of all possible variables are displayed. </p>
<dl>
<dt><code>&lt;path&gt;</code></dt>
<dd> is the name of the cgroup which should be read. This parameter can be used multiple times. </dd>
<dt><code>-a, &#8211;all</code></dt>
<dd> print the variables for all controllers which consist in the given cgroup </dd>
<dt><code>-g &lt;controller&gt;</code></dt>
<dd> defines controllers whose values should be displayed. This option can be used multiple times. </dd>
<dt><code>-g &lt;controller&gt;:&lt;path&gt;</code></dt>
<dd> defines control groups whose values should be displayed. This option can be used multiple times. </dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> display help and exit </dd>
<dt><code>-n</code></dt>
<dd> do not print headers, i.e. names of groups. </dd>
<dt><code>-r, &#8211;variable &lt;name&gt;</code></dt>
<dd> defines parameter to display. This option can be used multiple times. </dd>
<dt><code>-v, &#8211;values-only</code></dt>
<dd> print only values, not parameter names. </dd>
</dl>
<h2>EXAMPLES</h2>
<pre>
$ cgget -r cpuset.cpus -r cpuset.mems first second
first:
cpuset.cpus=0-1
cpuset.mems=0
second:
cpuset.cpus=0
cpuset.mems=0
$ cgget -n -r cpuset.cpus -r cpuset.mems first second
cpuset.cpus=0-1
cpuset.mems=0
cpuset.cpus=0
cpuset.mems=0
$ cgget -nv -r cpuset.cpus -r cpuset.mems first second
0-1
0
0
0
$ cgget -n -g cpu /
cpu.rt_period_us=1000000
cpu.rt_runtime_us=950000
cpu.shares=1024
</pre>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>CGROUP_LOGLEVEL</code></dt>
<dd> controls verbosity of the tool. Allowed values are <code>DEBUG</code>, <code>INFO</code>, <code>WARNING</code> or <code>ERROR</code>. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> cgrules.conf (1), cgcreate (1), cgget (1) </p>
<h2>Index</h2>
