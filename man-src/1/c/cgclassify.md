---
title: "cgclassify(1)"
name: "cgclassify"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cgclassify/"
description: "cgclassify – move running task(s) to given cgroups"
---

<h2>NAME</h2>
<p> cgclassify &#8211; move running task(s) to given cgroups </p>
<h2>SYNOPSIS</h2>
<p> <code>cgclassify</code> [<code>-g</code> &lt;<i>controllers&gt;:&lt;path</i>&gt;] [&#8211;sticky | &#8211;cancel-sticky] &lt;<i>pidlist</i>&gt; </p>
<h2>DESCRIPTION</h2>
<p> this command moves processes defined by the list of processes (<code>pidlist</code>) to the given control groups. </p>
<p> The pids in the pidlist are separated by spaces </p>
<dl>
<dt><code>-g &lt;controllers&gt;:&lt;path&gt;</code></p>
<dd> defines the control groups where the task will be moved. <code>controllers</code> is a list of controllers and <code>path</code> is the relative path to control groups in the given controllers list. </p>
<p> This flag can be used multiple times to define multiple pairs of lists of controllers and relative paths. Instead of the list of all mounted controllers, the wildcard <code>*</code> can be used. </p>
<p> If this option is not used then <code>cgclassify</code> will automatically move the task to a control group based on <code>/etc/cgrules.conf</code>. </p>
<dt><code>&#8211;sticky</code></p>
<dd> If this option is used, the daemon of service cgred (cgrulesengd process) does not change both the specified <code>pidlist</code> and their children tasks. Without this option, the daemon does not change the specified <code>pidlist</code> but it automatically changes their child tasks to the right cgroup based on <code>/etc/cgrules.conf</code>. </p>
<dt><code>&#8211;cancel-sticky</code></p>
<dd> If this option is used, the daemon of service cgred (cgrulesengd process) can automatically change both the specified <code>pidlist</code> and their child tasks to the right cgroup based on <code>/etc/cgrules.conf</code>. </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>CGROUP_LOGLEVEL</code></p>
<dd> controls verbosity of the tool. Allowed values are <code>DEBUG</code>, <code>INFO</code>, <code>WARNING</code> or <code>ERROR</code>. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/cgrules.conf</code></p>
<dd> default libcgroup configuration file</p>
<dt><code>/etc/cgrules.d</code></p>
<dd> default libcgroup configuration files directory </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>cgclassify -g cpu:student 1234</code></p>
<dd> moves process with pid number 1234 to control group student in cpu hierarchy. </p>
<dt><code>cgclassify 1234</code></p>
<dd> moves process with pid number 1234 to control groups based on <code>/etc/cgrules.conf</code> configuration file. </p>
<dt><code>cgclassify &#8211;sticky -g cpu:/student 1234</code></p>
<dd> moves process with pid number 1234 to control group student in cpu hierarchy. The daemon of service cgred does not change cgroups of pid 1234 and its children (based on <code>/etc/cgrules.conf</code>). </p>
</dl>
<h2>SEE ALSO</h2>
<p> cgrules.conf (5), cgexec (1) </p>
<h2>Index</h2>
