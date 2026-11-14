---
title: "cgdelete(1)"
name: "cgdelete"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cgdelete/"
description: "cgdelete – remove control group(s)"
---

<h2>NAME</h2>
<p> cgdelete &#8211; remove control group(s) </p>
<h2>SYNOPSIS</h2>
<p> <code>cgdelete</code> [<code>-h</code>] [<code>-r</code>] [[<code>-g</code>] &lt;<i>controllers</i>&gt;:<i>&lt;path</i>&gt;] &#8230; </p>
<h2>DESCRIPTION</h2>
<p> The <code>cgdelete</code> program removes all specified control groups. </p>
<dl>
<dt><code>[-g] &lt;controllers&gt;:&lt;path&gt;</code></p>
<dd> Defines the control group to delete. Multiple control groups may be specified. <code>-g</code> is optional. </p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display this help and exit. </p>
<dt><code>-r, &#8211;recursive</code></p>
<dd> Recursively remove all subgroups. </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>CGROUP_LOGLEVEL</code></p>
<dd> controls verbosity of the tool. Allowed values are <code>DEBUG</code>, <code>INFO</code>, <code>WARNING</code> or <code>ERROR</code>. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>cgdelete -g cpu,devices:/test</code></p>
<dd> remove control group test from hierarchies containing cpu and device controllers </p>
</dl>
<h2>SEE ALSO</h2>
<p> cgcreate (1), lscgroup (1), cgclear (1) </p>
<h2>Index</h2>
