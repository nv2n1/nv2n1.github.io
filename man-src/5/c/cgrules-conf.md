---
title: "cgrules-conf(5)"
name: "cgrules-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cgrules-conf/"
description: "cgrules.conf – libcgroup configuration file"
---

<p>cgrules.conf &#8211; libcgroup configuration file</p>
<h2>Description</h2>
<p><code>cgrules.conf</code> configuration file is used by <code>libcgroups</code> to define control groups to which a process belongs. The file contains a list of rules which assign to a defined group/user a control group in a subsystem (or control groups in subsystems). Rules have two formats: </p>
<pre>&lt;user&gt; &lt;controllers&gt; &lt;destination&gt;</pre>
<pre>&lt;user&gt;:&lt;process name&gt; &lt;controllers&gt; &lt;destination&gt;</pre>
<p>Where: <i>user</i> can be: </p>
<pre> - a user name
 - a group name with @group syntax
 - the wildcard '*', for any user or group
 - '%', which is equivalent to &quot;ditto&quot; (useful for 
 multi-line rules where different cgroups need to be 
 specified for various hierarchies for a single user)</pre>
<p><i>process name</i> is optional and it can be: </p>
<pre> - a process name
 - a full command path of a process</pre>
<p><i>controllers</i> can be: </p>
<pre> - comma separated controller names (no spaces) or 
 - * (for all mounted controllers)</pre>
<p><i>destination</i> can be: </p>
<pre> - path relative to the controller hierarchy (ex. pgrp1/gid1/uid1)
 - following strings called &quot;<code>templates</code>&quot; and will get expanded
 %u username, uid if name resolving fails
 %U uid
 %g group name, gid if name resolving fails
 %G gid
 %p process name, pid if name not available
 %P pid
 '\' can be used to escape '%'</pre>
<p>First rule which matches the criteria will be executed. Any text starting with &#8216;#&#8217; is considered as a start of comment line and is ignored. If the <i>destination</i> contains <code>template</code> string, the control group can be created on-fly. In time when some process wants to use the template rule which leads to control group (see <code>cgexec</code> (1)) and the control group does not exist, the group is created. The template control group parameters can be specified in <code>cgconfig.conf</code> configuration file. See (<code>cgconfig.conf</code> (5)). If the template definition is not found there created group have default kernel setting. </p>
<h2>Examples</h2>
<pre>student devices /usergroup/students</pre>
<p>Student&#8217;s processes in the &#8216;devices&#8217; subsystem belong to the control group /usergroup/students. </p>
<pre>student:cp devices /usergroup/students/cp</pre>
<p>When student executes &#8216;cp&#8217; command, the processes in the &#8216;devices&#8217; subsystem belong to the control group /usergroup/students/cp. </p>
<pre>@admin * admingroup/</pre>
<p>Processes started by anybody from admin group no matter in what subsystem belong to the control group admingroup/. </p>
<pre>peter cpu test1/
% memory test2/</pre>
<p>The first line says Peter&#8217;s task for cpu controller belongs to test1 control group. The second one says Peter&#8217;s tasks for memory controller belong to test2/ control group. </p>
<pre>* * default/ </pre>
<p>All processes in any subsystem belong to the control group default/. Since the earliest matched rule is applied, it makes sense to have this line at the end of the list. It will put a task which was not mentioned in the previous rules to default/ control group. </p>
<pre>@students cpu,cpuacct students/%u</pre>
<p>Processes in cpu and cpuacct subsystems started by anybody from students group belong to group students/name. Where &quot;name&quot; is user name of owner of the process. </p>
<h2>Files</h2>
<dl>
<dt><code>/etc/cgrules.conf</code></p>
<dd>
<dt>default libcgroup configuration file</p>
<dd></dl>
<h2>See Also</h2>
<p>cgconfig.conf (5), cgclassify (1), cgred.conf (5) </p>
<h2>Bugs</h2>
