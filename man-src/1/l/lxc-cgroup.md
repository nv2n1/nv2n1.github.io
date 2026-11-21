---

title: "lxc-cgroup(1)"
name: "lxc-cgroup"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxc-cgroup/"
description: "lxc-cgroup – manage the control group associated with a container"
---

<p> lxc-cgroup &#8211; manage the control group associated with a container</p>
<h2>SYNOPSIS</h2>
<p> <code>lxc-cgroup</code> {-n <i>name</i>} {<i>state-object</i>} [value]</p>
<h2>DESCRIPTION</h2>
<p> <code>lxc-cgroup</code> gets or sets the value of a <i>state-object</i> (e.g., &#8216;cpuset.cpus&#8217;) in the container&#8217;s cgroup for the corresponding subsystem (e.g., &#8216;cpuset&#8217;). If no [value] is specified, the current value of the <i>state-object</i> is displayed; otherwise it is set. </p>
<p> Note that <code>lxc-cgroup</code> does not check that the <i>state-object</i> is valid for the running kernel, or that the corresponding subsystem is contained in any mounted cgroup hierarchy.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>state-object</i></dt>
<dd> Specify the state object name.</dd>
<dt><code>[value]</code></dt>
<dd> Specify the value to assign to the state object.</dd></dl>
<h2>COMMON OPTIONS</h2>
<p> These options are common to most of lxc commands.</p>
<dl>
<dt><code>-?, -h, &#8211;help</code></dt>
<dd> Print a longer usage message than normal.</dd>
<dt><code>&#8211;usage</code></dt>
<dd> Give the usage message</dd>
<dt><code>-q, &#8211;quiet</code></dt>
<dd> mute on</dd>
<dt><code>-P, &#8211;lxcpath=</code><i>PATH</i></dt>
<dd> Use an alternate container path. The default is /var/lib/lxc.</dd>
<dt><code>-o, &#8211;logfile=</code><i>FILE</i></dt>
<dd> Output to an alternate log <i>FILE</i>. The default is no log.</dd>
<dt><code>-l, &#8211;logpriority=</code><i>LEVEL</i></dt>
<dd> Set log priority to <i>LEVEL</i>. The default log priority is ERROR. Possible values are : FATAL, CRIT, WARN, ERROR, NOTICE, INFO, DEBUG. </dd>
<p> Note that this option is setting the priority of the events log in the alternate log file. It do not have effect on the ERROR events log on stderr.</p>
<dt><code>-n, &#8211;name=</code><i>NAME</i></dt>
<dd> Use container identifier <i>NAME</i>. The container identifier format is an alphanumeric string.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show the version number.</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>lxc-cgroup -n foo devices.list</dt>
<dd> display the allowed devices to be used.</dd>
<dt>lxc-cgroup -n foo cpuset.cpus &quot;0,3&quot;</dt>
<dd> assign the processors 0 and 3 to the container.</dd></dl>
<h2>DIAGNOSTIC</h2>
<dl>
<dt>The container was not found</dt>
<dd> The container is not running.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-lxc/">lxc</a></code>(7), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-attach/">lxc-attach</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Daniel Lezcano &lt;daniel.lezcano [at] free.fr&gt; </p>
