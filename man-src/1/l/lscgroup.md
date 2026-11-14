---
title: "lscgroup(1)"
name: "lscgroup"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lscgroup/"
description: "lscgroup – list all cgroups"
---

<h2>NAME</h2>
<p> lscgroup &#8211; list all cgroups </p>
<h2>SYNOPSIS</h2>
<p> <code>lscgroup</code> [[<code>-g</code>] &lt;<i>controllers&gt;:&lt;path</i>&gt;] [&#8230;]<br />
 <code>lscgroup</code> [<code>-h|&#8211;help</code>] </p>
<h2>DESCRIPTION</h2>
<p> List all/chosen cgroups. </p>
<dl>
<dt><code>&lt;controllers&gt;:&lt;path&gt;</code></p>
<dd> defines the control groups whose subgroups will be shown. If this parameter is not used, the command will list all existing cgroups. </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>CGROUP_LOGLEVEL</code></p>
<dd> controls verbosity of the tool. Allowed values are <code>DEBUG</code>, <code>INFO</code>, <code>WARNING</code> or <code>ERROR</code>. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>lscgroup -g cpu:/</code></p>
<dd> list all cgroups which are in hierarchy containing cpu controller </p>
<dt><code>lscgroup -g cpu:/student</code></p>
<dd> list all cgroups which are in hierarchy containing cpu controller in subgroup student </p>
<dt><code>lscgroup</code></p>
<dd> list all cgroups which in all hierarchies </p>
</dl>
<h2>SEE ALSO</h2>
<p> lssubsys (1), cgcreate (1), cgdelete (1), cgconfig.conf (5) </p>
<h2>Index</h2>
