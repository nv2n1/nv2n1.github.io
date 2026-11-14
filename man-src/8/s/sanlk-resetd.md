---
title: "sanlk-resetd(8)"
name: "sanlk-resetd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sanlk-resetd/"
description: "sanlk-resetd – host reset daemon"
---

<p>sanlk-resetd &#8211; host reset daemon</p>
<h2>Synopsis</h2>
<p><code>sanlk-resetd</code> [OPTIONS] <i>lockspace_name</i> &#8230; </p>
<h2>Description</h2>
<p>The sanlk-resetd daemon gets events from specified sanlock lockspaces. Events are defined to cause sanlk-resetd to:<br />
 &#8211; use wdmd/watchdog to reset the host<br />
 &#8211; use /proc/sysrq-trigger to reboot the host The sanlk-reset program can be run on another host to request that sanlk-resetd reset the host it is running on. Both hosts must be operational and have continued access to a common lockspace for the reset request to succeed. After setting the event, the sanlk-reset program monitors the host status in the sanlock lockspace until the target host is dead. The sanlk-reset program can also be run on the same host as sanlk-resetd to update which lockspaces the local sanlk-resetd is watching for events. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;version, -V</code></p>
<dd>Print version. </p>
<dt><code>&#8211;help, -h</code></p>
<dd>Print usage. </p>
<dt><code>&#8211;foreground, -f</code></p>
<dd>Don&#8217;t fork. </p>
<dt><code>&#8211;daemon-debug, -D</code></p>
<dd>Enable debugging to stderr and don&#8217;t fork. </p>
<dt><code>&#8211;sysrq-reboot, -b 0|1</code></p>
<dd>Enable/Disable (1/0) use of /proc/sysrq-trigger to reboot. </p>
<dt><code>&#8211;sysrq-delay, -d </code><i>sec</i></p>
<dd>Delay this many seconds before using /proc/sysrq-trigger. </p>
<dt><code>&#8211;resource-mode, -R 0|1</code></p>
<dd>Resource leases are used (1) or not used (0) to protect storage. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sanlk-reset/">sanlk-reset</a></code>(8) <code><a href="/docs/linux/man/8-sanlock/">sanlock</a></code>(8) <code><a href="/docs/linux/man/8-wdmd/">wdmd</a></code>(8) </p>
