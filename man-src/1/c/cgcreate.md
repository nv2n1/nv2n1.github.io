---
title: "cgcreate(1)"
name: "cgcreate"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cgcreate/"
description: "cgcreate – create new cgroup(s)"
---

<h2>NAME</h2>
<p> cgcreate &#8211; create new cgroup(s) </p>
<h2>SYNOPSIS</h2>
<p> <code>cgcreate</code> [<code>-h</code>] [<code>-t</code> &lt;<i>tuid&gt;:&lt;tgid</i>&gt;] [<code>-a</code> &lt;<i>agid&gt;:&lt;auid</i>&gt;] [<code>-f</code> mode] [<code>-d</code> mode] [<code>-s</code> mode] <code>-g</code> &lt;<i>controllers&gt;:&lt;path</i>&gt; [<code>-g</code> &#8230;] </p>
<h2>DESCRIPTION</h2>
<p> The command creates new cgroup(s) defined by the options <code>-g</code>. </p>
<dl>
<dt><code>-a &lt;agid&gt;:&lt;auid&gt;</code></p>
<dd> defines the name of the user and the group which own the rest of the defined control group’s files. These users are allowed to set subsystem parameters and create subgroups. The default value is the same as has the parent cgroup. </p>
<dt><code>-d, &#8211;dperm=mode</code></p>
<dd> sets the permissions of a control groups directory. The permissions needs to be specified as octal numbers e.g. <code>-d 775</code>. </p>
<dt><code>-f, &#8211;fperm=mode</code></p>
<dd> sets the permissions of the control groups parameters. The permissions needs to be specified as octal numbers e.g. <code>-f 775</code>. The value is not used as given because the current owner&#8217;s permissions are used as an umask (so 777 will set group and others permissions to the owners permissions). </p>
<dt><code>-g &lt;controllers&gt;:&lt;path&gt;</code></p>
<dd> defines control groups to be added. <code>controllers</code> is a list of controllers. Character &quot;*&quot; can be used as a shortcut for &quot;all mounted controllers&quot;. <code>path</code> is the relative path to control groups in the given controllers list. This option can be specified multiple times. </p>
<dt><code>-h, &#8211;help</code></p>
<dd> display this help and exit </p>
<dt><code>-s, &#8211;tperm=mode</code></p>
<dd> sets the permissions of the control group tasks file. The permissions needs to be specified as octal numbers e.g. <code>-s 775</code>. The value is not used as given because the current owner&#8217;s permissions are used as an umask (so 777 will set group and others permissions to the owners permissions). </p>
<dt><code>-t &lt;tuid&gt;:&lt;tgid&gt;</code></p>
<dd> defines the name of the user and the group, which owns tasks file of the defined control group. I.e. this user and members of this group have write access to the file. The default value is the same as has the parent cgroup. </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>CGROUP_LOGLEVEL</code></p>
<dd> controls verbosity of the tool. Allowed values are <code>DEBUG</code>, <code>INFO</code>, <code>WARNING</code> or <code>ERROR</code>. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>cgcreate -g *:student -g devices:teacher</code></p>
<dd> create control group student in all mounted hierarchies and create control group teacher in hierarchy containing controller devices. </p>
</dl>
<h2>SEE ALSO</h2>
<p> cgrules.conf (5) cgexec (1) cgclassify (1) </p>
<h2>Index</h2>
