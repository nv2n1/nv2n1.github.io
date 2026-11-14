---
title: "cgexec(1)"
name: "cgexec"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cgexec/"
description: "cgexec – run the task in given control groups"
---

<h2>NAME</h2>
<p> cgexec &#8211; run the task in given control groups </p>
<h2>SYNOPSIS</h2>
<p> <code>cgexec</code> [<code>-h</code>] [<code>-g</code> &lt;<i>controllers&gt;:&lt;path</i>&gt;] [&#8211;sticky] <code>command</code> [<i>arguments</i>] </p>
<h2>DESCRIPTION</h2>
<p> The <code>cgexec</code> program executes the task <code>command</code> with arguments <code>arguments</code> in the given control groups. </p>
<dl>
<dt><code>-g &lt;controllers&gt;:&lt;path&gt;</code></p>
<dd> defines the control groups in which the task will be run. <code>controllers</code> is a list of controllers and <code>path</code> is the relative path to control groups in the given controllers list. </p>
<p> This flag can be used multiple times to define multiple pairs of lists of controllers and relative paths. Instead of the list of all mounted controllers, the wildcard <code>b&quot;*b&quot;</code> can be used. </p>
<p> If this option is not used, <code>cgexec</code> will automatically place the task in the right cgroup based on <code>/etc/cgrules.conf</code>. </p>
<p> If <code>/etc/cgrules.conf</code> configuration file is used, there can be used template names. Then the control group name contains a template in destination tag (see <code>cgrules.conf</code> (5)) and if the cgroup does not exist in execution time, it is created, based on <code>/etc/cgconfig.conf</code> specification. If the specifications are not present the group is created with the default kernel values. </p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display this help and exit. </p>
<dt><code>&#8211;sticky</code></p>
<dd> If running the task <code>command</code> with this option, the daemon of service cgred (cgrulesengd process) does not change both the task of the <code>command</code> and the child tasks. Without this option, the daemon does not change the task of the <code>command</code> but it changes the child tasks to the right cgroup based on <code>/etc/cgrules.conf</code> automatically. </p>
</dl>
<h2>EXAMPLES</h2>
<pre>
<code>cgexec -g *:test1 ls
</code></pre>
<p> runs command <code>ls</code> in control group test1 in all mounted controllers. </p>
<pre>
<code>cgexec -g cpu,memory:test1 ls -l
</code></pre>
<p> runs command <code>ls -l</code> in control group test1 in controllers cpu and memory. </p>
<pre>
<code>cgexec -g cpu,memory:test1 -g swap:test2 ls -l
</code></pre>
<p> runs command <code>ls -l</code> in control group test1 in controllers cpu and memory and control group test2 in controller swap. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>CGROUP_LOGLEVEL</code></p>
<dd> controls verbosity of the tool. Allowed values are <code>DEBUG</code>, <code>INFO</code>, <code>WARNING</code> or <code>ERROR</code>. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/cgrules.conf</code></p>
<dd> default libcgroup configuration file </p>
</dl>
<h2>SEE ALSO</h2>
<p> cgrules.conf (5) </p>
<h2>Index</h2>
