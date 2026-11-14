---
title: "lssubsys(1)"
name: "lssubsys"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lssubsys/"
description: "lssubsys – list hierarchies containing given subsystem"
---

<h2>NAME</h2>
<p> lssubsys &#8211; list hierarchies containing given subsystem </p>
<h2>SYNOPSIS</h2>
<p> <code>lssubsys</code> [<code>-m|&#8211;mount-points</code>] [<code>-M|&#8211;all-mount-points</code>] [<i>controller</i>] [&#8230;]<br />
 <code>lssubsys</code> [<code>-m|&#8211;mount-points</code>] [<code>-M|&#8211;all-mount-points</code>] [<code>-i|&#8211;hierarchies</code>] [<code>-a|&#8211;all</code>]<br />
 <code>lssubsys</code> [<code>-h|&#8211;help</code>] </p>
<h2>DESCRIPTION</h2>
<p> <code>lssubsys</code> list the hierarchies containing the given subsystem(s). If no subsystem is defined, it displays all mounted hierarchies. </p>
<dl>
<dt><code>controller</code></p>
<dd> defines the subsystem whose hierarchy is shown. If this parameter is not used, the command will list all mounted subsystems. </p>
<dt><code>-m, &#8211;mount-points</code></p>
<dd> Display mount points. Only the first mount points of shown hierarchies are displayed. </p>
<dt><code>-M, &#8211;all-mount-points</code></p>
<dd> Display mount points. All mount points of shown hierarchies are displayed, each on separate line. </p>
<dt><code>-a, &#8211;all</code></p>
<dd> Display all subsystems (including unmounted ones). </p>
<dt><code>-i, &#8211;hierarchies</code></p>
<dd> Display the attached hierarchy number if the subsystem is in a hierarchy. If the option <code>-m</code> is also used, the hierarchy number is shown only for unmounted hierarchies. </p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display help and exit. </p>
</dl>
<h2>EXAMPLE</h2>
<p> The command <code>lssubsys -am</code> lists all subsystems which are present in the system, mounted ones will be shown with their mount point:</p>
<dl>
<dt>
<dd>
<pre>
$ lssubsys -am
ns
cpuset
cpu,devices
cpuacct /cgroup/cpuacct
memory /cgroup/memory
freezer /cgroup/freezer
net_cls /cgroup/net_cls
</pre>
</dl>
<p> The command <code>lssubsys -ami</code> lists all subsystems which are present in the system, mounted subsystems are listed with their mount points, unmounted ones which are in a hierarchy are listed with their hierarchy number:</p>
<dl>
<dt>
<dd>
<pre>
$ lssubsys -ami
ns
cpuset 5
cpu,devices 6
cpuacct /cgroup/cpuacct
memory /cgroup/memory
freezer /cgroup/freezer
net_cls /cgroup/net_cls
</pre>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>CGROUP_LOGLEVEL</code></p>
<dd> controls verbosity of the tool. Allowed values are <code>DEBUG</code>, <code>INFO</code>, <code>WARNING</code> or <code>ERROR</code>. </p>
</dl>
<h2>SEE ALSO</h2>
<p> lscgroup (1), cgcreate (1), cgdelete (1), cgconfig.conf (5) </p>
<h2>Index</h2>
