---
title: "cgconfigparser(8)"
name: "cgconfigparser"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cgconfigparser/"
description: "cgconfigparser – setup control group file system"
---

<p>cgconfigparser &#8211; setup control group file system </p>
<h2>Synopsis</h2>
<p><code>cgconfigparser</code> [<code>-h</code>] [<code>-l</code> <i>&lt;filename&gt;</i>] [<code>-L</code> <i>&lt;directory&gt;</i>] [&#8230;] </p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Displays help.</p>
<dt><code>-l, &#8211;load=FILE</code></p>
<dd>Parses the control groups configuration file Sets up the control group file system defined by the configuration file and mounts mount points defined by the configuration file. The format of the file is described in <code>cgconfig.conf</code>. This option can be used multiple times and can be mixed with <code>-L</code> option. </p>
<dt><code>-L, &#8211;load-directory=DIR</code></p>
<dd>Finds all files in given directory and parses them in alphabetical order like they were specified by <code>-l</code> option. This option can be used multiple times and can be mixed with <code>-l</code> option. </p>
<dt><code>-a &lt;agid&gt;:&lt;auid&gt;</code></p>
<dd>defines the default owner of the rest of the defined control group’s files. These users are allowed to set subsystem parameters and create subgroups. The default value is the same as has the parent cgroup. </p>
<dt><code>-d, &#8211;dperm=mode</code></p>
<dd>sets the default permissions of a control groups directory. The permissions needs to be specified as octal numbers e.g. <code>-d 775</code>. </p>
<dt><code>-f, &#8211;fperm=mode</code></p>
<dd>sets the default permissions of the control group files. The permissions needs to be specified as octal numbers e.g. <code>-f 775</code>. The value is not used as given because the current owner&#8217;s permissions are used as an umask (so 777 will set group and others permissions to the owners permissions). </p>
<dt><code>-s, &#8211;tperm=mode</code></p>
<dd>sets the default permissions of the control group tasks files. The permissions needs to be specified as octal numbers e.g. <code>-f 775</code>. The value is not used as given because the current owner&#8217;s permissions are used as an umask (so 777 will set group and others permissions to the owners permissions). </p>
<dt><code>-t &lt;tuid&gt;:&lt;tgid&gt;</code></p>
<dd>defines the default owner of tasks file of the defined control group. I.e. this user and members of this group have write access to the file. </p>
</dl>
<h2>Environment Variables</h2>
<dl>
<dt><code>CGROUP_LOGLEVEL</code></p>
<dd>controls verbosity of the tool. Allowed values are <code>DEBUG</code>, <code>INFO</code>, <code>WARNING</code> or <code>ERROR</code>. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/cgconfig.conf</code></p>
<dd>default libcgroup configuration file</p>
<dt><code>/etc/cgconfig.d/</code></p>
<dd>default libcgroup configuration files directory </p>
</dl>
<h2>Examples</h2>
<dl>
<dt><code>cgconfigparser -l /etc/cgconfig.conf</code></p>
<dd>setup control group file system based on <code>/etc/cgconfig.conf</code> configuration file </p>
<h2>See Also</h2>
<p>cgconfig.conf (5) </p>
