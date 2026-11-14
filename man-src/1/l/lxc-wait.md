---
title: "lxc-wait(1)"
name: "lxc-wait"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxc-wait/"
description: "lxc-wait – wait for a specific container state"
---

<h2>NAME</h2>
<p> lxc-wait &#8211; wait for a specific container state</p>
<h2>SYNOPSIS</h2>
<p> <code>lxc-wait</code> {-n <i>name</i>} {-s <i>states</i>}</p>
<h2>DESCRIPTION</h2>
<p> <code>lxc-wait</code> waits for a specific container state before exiting, this is useful for scripting.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s </code><i>states</i></p>
<dd> Specify the container state(s) to wait for. The container states can be ORed to specify several states.</p>
<dt><code>-t </code><i>timeout</i></p>
<dd> Wait timeout seconds for desired state to be reached.</dl>
<h2>COMMON OPTIONS</h2>
<p> These options are common to most of lxc commands.</p>
<dl>
<dt><code>-?, -h, &#8211;help</code></p>
<dd> Print a longer usage message than normal.</p>
<dt><code>&#8211;usage</code></p>
<dd> Give the usage message</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> mute on</p>
<dt><code>-P, &#8211;lxcpath=</code><i>PATH</i></p>
<dd> Use an alternate container path. The default is /var/lib/lxc.</p>
<dt><code>-o, &#8211;logfile=</code><i>FILE</i></p>
<dd> Output to an alternate log <i>FILE</i>. The default is no log.</p>
<dt><code>-l, &#8211;logpriority=</code><i>LEVEL</i></p>
<dd> Set log priority to <i>LEVEL</i>. The default log priority is ERROR. Possible values are : FATAL, CRIT, WARN, ERROR, NOTICE, INFO, DEBUG. </p>
<p> Note that this option is setting the priority of the events log in the alternate log file. It do not have effect on the ERROR events log on stderr.</p>
<dt><code>-n, &#8211;name=</code><i>NAME</i></p>
<dd> Use container identifier <i>NAME</i>. The container identifier format is an alphanumeric string.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version number.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>lxc-wait -n foo -s RUNNING</p>
<dd> exits when &#8216;RUNNING&#8217; is reached.</p>
<dt>lxc-wait -n foo -s &#8216;RUNNING|STOPPED&#8217;</p>
<dd> exits when &#8216;RUNNING&#8217; or &#8216;STOPPED&#8217; state is reached.</dl>
<h2>DIAGNOSTIC</h2>
<dl>
<dt>The container was not found</p>
<dd> The specified container was not created before with the <code>lxc-create</code> command.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-lxc/">lxc</a></code>(7), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-attach/">lxc-attach</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Daniel Lezcano &lt;daniel.lezcano [at] free.fr&gt; </p>
<h2>Index</h2>
