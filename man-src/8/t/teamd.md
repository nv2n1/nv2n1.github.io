---
title: "teamd(8)"
name: "teamd"
section: "8"
letter: "t"
url: "/docs/linux/man/8-teamd/"
description: "teamd — team network device control daemon"
---

<p>teamd &#8212; team network device control daemon</p>
<h2>Synopsis</h2>
<p><code>teamd</code> <code>-k</code> [<code>-p</code> <i>pid_file</i>] [<code>-g</code>]<br/>
 <code>teamd</code> <code>-e</code> [<code>-p</code> <i>pid_file</i>] [<code>-g</code>]<br/>
 <code>teamd</code> <code>-c</code><i> config_text</i> [<code>-p</code> <i>pid_file</i>] [<code>-gdrD</code>] [<code>-Z</code> <i>address</i>]<br/>
 <code>teamd</code> <code>-f</code><i> config_file</i> [<code>-p</code> <i>pid_file</i>] [<code>-gdrD</code>] [<code>-Z</code> <i>address</i>]<br/>
 <code>teamd</code> <code>-h</code>|<code>-V</code></p>
<h2>Description</h2>
<p>teamd is a daemon to control a given team network device, during runtime, as a puppeteer controls a puppet. It uses libteam to communicate with the kernel team device instance via Netlink sockets. The behaviour depends on the selected runner and its configuration. This daemon is part of the libteam project.</p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd>Print help text to console and exit.</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd>Print version information to console and exit.</dd>
<dt><code>-d, &#8211;daemonize</code></dt>
<dd>Daemonize after startup.</dd>
<dt><code>-k, &#8211;kill</code></dt>
<dd>Kill running daemon instance.</dd>
<dt><code>-e, &#8211;check</code></dt>
<dd>Return 0 if a daemon is already running.</dd>
<dt><code>-f </code><i>filename</i><code>, &#8211;config-file </code><i>filename</i></dt>
<dd>Load the specified configuration file.</dd>
<dt><code>-c </code><i>text</i><code>, &#8211;config text</code></dt>
<dd>Use given JSON format configuration string. If this option is present then -f option will be ignored.</dd>
<dt><code>-p </code><i>filename</i><code>, &#8211;pid-file </code><i>filename</i></dt>
<dd>Use the specified PID file.</dd>
<dt><code>-g, &#8211;debug</code></dt>
<dd>Turns on debugging messages. Repeating the option increases verbosity.</dd>
<dt><code>-r, &#8211;force-recreate</code></dt>
<dd>Force team device recreation in case it already exists.</dd>
<dt><code>-o, &#8211;take-over</code></dt>
<dd>Take over the device if it already exists.</dd>
<dt><code>-N, &#8211;no-quit-destroy</code></dt>
<dd>This option also ensures that the team device is not removed after teamd finishes.</dd>
<dt><code>-t </code><i>devicename</i><code>, &#8211;team-dev </code><i>devicename</i></dt>
<dd>Use the specified team device name (overrides &quot;device&quot; key in the configuration).</dd>
<dt><code>-n, &#8211;no-ports</code></dt>
<dd>Start without ports, even if they are listed in the configuration.</dd>
<dt><code>-D, &#8211;dbus-enable</code></dt>
<dd>Enable D-Bus interface.</dd>
<dt><code>-Z </code><i>address</i><code>, &#8211;zmq-enable </code><i>address</i></dt>
<dd>Enable ZMQ interface. Possible address formats are &quot;<a href="tcp://ip:port">tcp://ip:port</a>&quot;, &quot;<a href="ipc://path">ipc://path</a>&quot; and others. Detailed description of ZMQ library is in page <a rel="nofollow" href="http://zguide.zeromq.org/page:all.">http://zguide.zeromq.org/page:all.</a></dd>
<dt><code>-U, &#8211;usock-enable</code></dt>
<dd>Enable UNIX domain socket interface. This is enabled by default.</dd>
<dt><code>-u, &#8211;usock-disable</code></dt>
<dd>Disable UNIX domain socket interface.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-teamdctl/">teamdctl</a></code>(8), <code><a href="/docs/linux/man/5-teamd-conf/">teamd.conf</a></code>(5), <code><a href="/docs/linux/man/8-teamnl/">teamnl</a></code>(8), <code><a href="/docs/linux/man/1-bond2team/">bond2team</a></code>(1)</p>
<h2>Author</h2>
<p>Jiri Pirko is the original author and current maintainer of libteam.</p>
