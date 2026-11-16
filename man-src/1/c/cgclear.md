---
title: "cgclear(1)"
name: "cgclear"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cgclear/"
description: "cgclear – unload the cgroup filesystem"
---

<h2>NAME</h2>
<p> cgclear &#8211; unload the cgroup filesystem </p>
<h2>SYNOPSIS</h2>
<p> <code>cgclear</code> [<code>-e</code>] [<code>-l</code> &lt;<i>filename</i>&gt;] [<code>-L</code> &lt;<i>directory</i>&gt;] [&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> Without parameters, this command moves all the tasks inside the various cgroups to the root cgroup, deletes all the cgroups and finally unmounts the cgroup filesystem from the system. </p>
<p> If one or more config files are specified, only groups defined in the config files are removed. The files are processed in reverse order, i.e. the last file on command line is processed first, so <code>cgclear</code> can have the same command line arguments as appropriate <code>cgconfigparser</code>. </p>
<dl>
<dt><code>-l, &#8211;load=&lt;filename&gt;</code></dt>
<dd> specifies the config file to read. This option can be used multiple times and can be mixed with <code>-L</code> option. </dd>
<dt><code>-L, &#8211;load-directory=&lt;directory&gt;</code></dt>
<dd> specifies the directory, which is searched for configuration files. All files in this directory will be processed in alphabetical order as they were specified by <code>-l</code> option. This option can be used multiple times and can be mixed with <code>-l</code> option. </dd>
<dt><code>-e</code></dt>
<dd> specifies that only empty groups should be removed. If a group defined in a config file has tasks inside or has a subgroup, it won&#8217;t be removed. This option works only with <code>-l</code> or <code>-L</code> options. </dd>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>CGROUP_LOGLEVEL</code></dt>
<dd> controls verbosity of the tool. Allowed values are <code>DEBUG</code>, <code>INFO</code>, <code>WARNING</code> or <code>ERROR</code>. </dd>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/cgconfig.conf</code></dt>
<dd> default templates file</dd>
<dt><code>/etc/cgconfig.d/</code></dt>
<dd> default templates files directory </dd>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>cgclear</code></dt>
<dd> unload the whole cgroup filesystem </dd>
<dt><code>cgclear -l /etc/cgconfig.conf</code></dt>
<dd> unload a subsystem of cgroup filesystem based on <code>/etc/cgconfig.conf</code> definition. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> cgconfigparser(1), <a href="/docs/linux/man/5-cgconfig-conf/">cgconfig.conf</a>(5) </p>
<h2>Index</h2>
