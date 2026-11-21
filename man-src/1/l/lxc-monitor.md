---

title: "lxc-monitor(1)"
name: "lxc-monitor"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxc-monitor/"
description: "lxc-monitor – monitor the container state"
---

<h2>NAME</h2>
<p> lxc-monitor &#8211; monitor the container state</p>
<p> <code>lxc-monitor</code> [-n <i>name</i>] [-Q <i>name</i>]</p>
<p> <code>lxc-monitor</code> monitors the state of containers. The <i>name</i> argument may be used to specify which containers to monitor. It is a regular expression, conforming with posix2, so it is possible to monitor all the containers, several of them or just one. If not specified, <i>name</i> will default to &#8216;.*&#8217; which will monitor all containers in <code>lxcpath</code>. </p>
<p> The <code>-P, &#8211;lxcpath</code>=PATH option may be specified multiple times to monitor more than one container path. Note however that containers with the same name in multiple paths will be indistinguishable in the output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-Q, &#8211;quit</code></dt>
<dd> Ask the lxc-monitord daemon on each given <code>lxcpath</code> to quit. After receiving this command, lxc-monitord will exit immediately as soon as it has no clients instead of waiting the normal 30 seconds for new clients. This is useful if you need to unmount the filesystem <code>lxcpath</code> is on.</dd></dl>
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
<dt>lxc-monitor -n foo</dt>
<dd> will monitor the different states for container foo.</dd>
<dt>lxc-monitor -n &#8216;foo|bar&#8217;</dt>
<dd> will monitor the different states for container foo and bar.</dd>
<dt>lxc-monitor -n &#8216;[f|b].*&#8217;</dt>
<dd> will monitor the different states for container with the name beginning with letter &#8216;f&#8217; or &#8216;b&#8217;.</dd>
<dt>lxc-monitor -n &#8216;.*&#8217;</dt>
<dd> will monitor the different states for all containers.</dd></dl>
<h2>DIAGNOSTIC</h2>
<dl>
<dt>The container was not found</dt>
<dd> The specified container was not created before with the <code>lxc-create</code> command.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7),</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-lxc/">lxc</a></code>(7), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-attach/">lxc-attach</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Daniel Lezcano &lt;daniel.lezcano [at] free.fr&gt; </p>
