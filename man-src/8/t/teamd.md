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
<p><code>teamd</code> <code>-k</code> [<code>-p</code> <i>pid_file</i>] [<code>-g</code>]<br />
 <code>teamd</code> <code>-e</code> [<code>-p</code> <i>pid_file</i>] [<code>-g</code>]<br />
 <code>teamd</code> <code>-c</code><i> config_text</i> [<code>-p</code> <i>pid_file</i>] [<code>-gdrD</code>] [<code>-Z</code> <i>address</i>]<br />
 <code>teamd</code> <code>-f</code><i> config_file</i> [<code>-p</code> <i>pid_file</i>] [<code>-gdrD</code>] [<code>-Z</code> <i>address</i>]<br />
 <code>teamd</code> <code>-h</code>|<code>-V</code></p>
<h2>Description</h2>
<p>teamd is a daemon to control a given team network device, during runtime, as a puppeteer controls a puppet. It uses libteam to communicate with the kernel team device instance via Netlink sockets. The behaviour depends on the selected runner and its configuration. This daemon is part of the libteam project.</p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Print help text to console and exit.</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Print version information to console and exit.</p>
<dt><code>-d, &#8211;daemonize</code></p>
<dd>Daemonize after startup.</p>
<dt><code>-k, &#8211;kill</code></p>
<dd>Kill running daemon instance.</p>
<dt><code>-e, &#8211;check</code></p>
<dd>Return 0 if a daemon is already running.</p>
<dt><code>-f </code><i>filename</i><code>, &#8211;config-file </code><i>filename</i></p>
<dd>Load the specified configuration file.</p>
<dt><code>-c </code><i>text</i><code>, &#8211;config text</code></p>
<dd>Use given JSON format configuration string. If this option is present then -f option will be ignored.</p>
<dt><code>-p </code><i>filename</i><code>, &#8211;pid-file </code><i>filename</i></p>
<dd>Use the specified PID file.</p>
<dt><code>-g, &#8211;debug</code></p>
<dd>Turns on debugging messages. Repeating the option increases verbosity.</p>
<dt><code>-r, &#8211;force-recreate</code></p>
<dd>Force team device recreation in case it already exists.</p>
<dt><code>-o, &#8211;take-over</code></p>
<dd>Take over the device if it already exists.</p>
<dt><code>-N, &#8211;no-quit-destroy</code></p>
<dd>This option also ensures that the team device is not removed after teamd finishes.</p>
<dt><code>-t </code><i>devicename</i><code>, &#8211;team-dev </code><i>devicename</i></p>
<dd>Use the specified team device name (overrides &quot;device&quot; key in the configuration).</p>
<dt><code>-n, &#8211;no-ports</code></p>
<dd>Start without ports, even if they are listed in the configuration.</p>
<dt><code>-D, &#8211;dbus-enable</code></p>
<dd>Enable D-Bus interface.</p>
<dt><code>-Z </code><i>address</i><code>, &#8211;zmq-enable </code><i>address</i></p>
<dd>Enable ZMQ interface. Possible address formats are &quot;<a href="tcp://ip:port">tcp://ip:port</a>&quot;, &quot;<a href="ipc://path">ipc://path</a>&quot; and others. Detailed description of ZMQ library is in page <a rel="nofollow" href="http://zguide.zeromq.org/page:all.">http://zguide.zeromq.org/page:all.</a></p>
<dt><code>-U, &#8211;usock-enable</code></p>
<dd>Enable UNIX domain socket interface. This is enabled by default.</p>
<dt><code>-u, &#8211;usock-disable</code></p>
<dd>Disable UNIX domain socket interface.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-teamdctl/">teamdctl</a></code>(8), <code><a href="/docs/linux/man/5-teamd-conf/">teamd.conf</a></code>(5), <code><a href="/docs/linux/man/8-teamnl/">teamnl</a></code>(8), <code><a href="/docs/linux/man/1-bond2team/">bond2team</a></code>(1)</p>
<h2>Author</h2>
<p>Jiri Pirko is the original author and current maintainer of libteam.</p>
