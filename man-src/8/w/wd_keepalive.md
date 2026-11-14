---
title: "wd_keepalive(8)"
name: "wd_keepalive"
section: "8"
letter: "w"
url: "/docs/linux/man/8-wd_keepalive/"
description: "wd_keepalive – a simplified software watchdog daemon"
---

<p>wd_keepalive &#8211; a simplified software watchdog daemon</p>
<h2>Synopsis</h2>
<p><code>wd_keepalive</code> [<code>-c</code> <i>filename</i>|<code>&#8211;config-file</code> <i>filename</i>]</p>
<h2>Description</h2>
<p>This is a simplified version of the watchdog daemon. If configured so it only opens<br />
&nbsp;<wbr>.IR&nbsp;<wbr>/dev/watchdog ,&nbsp;<wbr> and keeps writing to it often enough to keep the kernel from resetting, at least once per minute. Each write delays the reboot time another minute. After a minute of inactivity the watchdog hardware will cause a reset. In the case of the software watchdog the ability to reboot will depend on the state of the machines and interrupts. </p>
<p> The wd_keepalive daemon can be stopped without causing a reboot if the device <i>/dev/watchdog</i> is closed correctly, unless your kernel is compiled with the <i>CONFIG_WATCHDOG_NOWAYOUT</i> option enabled. </p>
<p> Under high system load <code>wd_keepalive</code> might be swapped out of memory and may fail to make it back in in time. Under these circumstances the Linux kernel will reset the machine. To make sure you won&#8217;t get unnecessary reboots make sure you have the variable <i>realtime</i> set to <i>yes</i> in the configuration file <i>watchdog.conf</i>. This adds real time support to <code>wd_keepalive</code>: it will lock itself into memory and there should be no problem even under the highest of loads. </p>
<p> On system running out of memory the kernel will try to free enough memory by killing process. The <code>wd_keepalive</code> daemon itself is exempted from this so-called out-of-memory killer.</p>
<h2>Options</h2>
<p>Available command line options are the following:</p>
<dl>
<dt><code>-c</code> <i>config-file</i>, <code>&#8211;config-file</code> <i>config-file</i></p>
<dd>Use <i>config-file</i> as the configuration file instead of the default <i>/etc/watchdog.conf</i>.</dl>
<h2>Files</h2>
<dl>
<dt><i>/dev/watchdog </i></p>
<dd>The watchdog device.</p>
<dt><i>/var/run/wd_keepalive.pid </i></p>
<dd>The pid file of the running <code>wd_keepalive</code>.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-watchdog-conf/">watchdog.conf</a></code>(5)</p>
<dl>
<dt><code><a href="/docs/linux/man/8-watchdog/">watchdog</a></code>(8)</p>
<dd>
