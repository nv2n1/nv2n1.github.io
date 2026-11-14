---
title: "sanlk-reset(8)"
name: "sanlk-reset"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sanlk-reset/"
description: "sanlk-reset – host reset program"
---

<p>sanlk-reset &#8211; host reset program</p>
<h2>Synopsis</h2>
<p><code>sanlk-reset</code> [OPTIONS] <i>action</i> <i>lockspace_name</i> &#8230; </p>
<h2>Description</h2>
<p>The sanlk-reset program sets events in specified sanlock lockspaces. Events are defined to cause sanlk-resetd on another host to:<br />
 &#8211; use wdmd/watchdog to reset the host<br />
 &#8211; use /proc/sysrq-trigger to reboot the host Both hosts must be operational and have continued access to a common lockspace for the reset request to succeed. After setting the event, the sanlk-reset program monitors the host status in the sanlock lockspace until the target host is dead. The sanlk-reset program can also be run on the same host as sanlk-resetd to update which lockspaces the local sanlk-resetd is watching for events. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;version, -V</code></p>
<dd>Print version. </p>
<dt><code>&#8211;help, -h</code></p>
<dd>Print usage. </p>
</dl>
<h3>Reset another host</h3>
<p>The event is set in each lockspace specified. The target host may have a different host id in each lockspace. </p>
<p> <code>sanlk-reset reset</code> <i>lockspace_name:host_id</i> &#8230; </p>
<dl>
<dt><code>&#8211;host-id, -i </code><i>num</i></p>
<dd>Host id to reset. (Use only with single lockspace name.) </p>
<dt><code>&#8211;generation, -g </code><i>num</i></p>
<dd>Generation of host. (Use only with single lockspace name.) </p>
<dt><code>&#8211;sysrq-reboot, -b 0|1</code></p>
<dd>Enable/Disable (1/0) use of /proc/sysrq-trigger to reboot. </p>
<dt><code>&#8211;resource-mode, -R 0|1</code></p>
<dd>Resource leases are used (1) or not used (0) to protect storage. </p>
<dt><code>&#8211;native-timeout, -t num</code></p>
<dd>Disable native timeout by setting to 0. </p>
</dl>
<h3>Update the local sanlk-resetd</h3>
<p>to watch new lockspaces for reset events: </p>
<p> <code>sanlk-reset reg</code> <i>lockspace_name</i> &#8230; </p>
<p> to not watch lockspaces for reset events: </p>
<p> <code>sanlk-reset end</code> <i>lockspace_name</i> &#8230; </p>
<p> to clear all lockspaces being watched: </p>
<p> <code>sanlk-reset clear all</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sanlk-resetd/">sanlk-resetd</a></code>(8) <code><a href="/docs/linux/man/8-sanlock/">sanlock</a></code>(8) <code><a href="/docs/linux/man/8-wdmd/">wdmd</a></code>(8) </p>
