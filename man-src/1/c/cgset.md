---
title: "cgset(1)"
name: "cgset"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cgset/"
description: "cgset – set the parameters of given cgroup(s)"
---

<h2>NAME</h2>
<p> cgset &#8211; set the parameters of given cgroup(s) </p>
<h2>SYNOPSIS</h2>
<p> <code>cgset</code> [<code>-r</code> &lt;<i>name=value</i>&gt;] &lt;<code>cgroup_path</code>&gt; &#8230;<br />
 <code>cgset</code> <code>&#8211;copy-from</code> &lt;<i>source_cgroup_path</i>&gt; &lt;<code>cgroup_path</code>&gt; &#8230; </p>
<h2>DESCRIPTION</h2>
<p> Set the parameters of input cgroups. </p>
<dl>
<dt><code>&lt;path&gt;</code></p>
<dd> is the name of the cgroup which should be changed. This parameter can be used multiple times. </p>
<dt><code>-r &lt;name=value&gt;</code></p>
<dd> defines the name of the file to set and the value which should be written to that file. This parameter can be used multiple times. </p>
<dt><code>&#8211;copy-from &lt;source_cgroup_path&gt;</code></p>
<dd> defines the name of the cgroup whose parameters will be copied to the input cgroup. </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>CGROUP_LOGLEVEL</code></p>
<dd> controls verbosity of the tool. Allowed values are <code>DEBUG</code>, <code>INFO</code>, <code>WARNING</code> or <code>ERROR</code>. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>cgset -r cpuset.cpus=0-1 student</code></p>
<dd> set variable cpus in control group student (controller cpuset) to 0-1 </p>
<dt><code>cgset &#8211;copy-from group1/ group2/</code></p>
<dd> copy all parameters of group group1 to group group2 (for all path where both cgroups are defined) </p>
</dl>
<h2>SEE ALSO</h2>
<p> cgrules.conf (1), cgcreate (1), cgget (1) </p>
<h2>Index</h2>
