---
title: "wd_identify(8)"
name: "wd_identify"
section: "8"
letter: "w"
url: "/docs/linux/man/8-wd_identify/"
description: "wd_identify – a simplified software watchdog daemon"
---

<p>wd_identify &#8211; a simplified software watchdog daemon</p>
<h2>Synopsis</h2>
<p><code>wd_identify</code> [<code>-c</code> <i>filename</i>|<code>&#8211;config-file</code> <i>filename</i>]</p>
<h2>Description</h2>
<p>This utility opens <i>/dev/watchdog</i> and gets the identification string from the watchdog which then is printed. The device is closed afterwards. </p>
<p> The wd_identify tool can only be used without causing a reboot if your kernel is compiled with the <i>CONFIG_WATCHDOG_NOWAYOUT</i> option enabled. </p>
<p> Watchdog and/or wd_keepalive may have to be stopped to make sure that wd_identify can access the watchdog device.</p>
<h2>Options</h2>
<p>Available command line options are the following:</p>
<dl>
<dt><code>-c</code> <i>config-file</i>, <code>&#8211;config-file</code> <i>config-file</i></p>
<dd>Use <i>config-file</i> as the configuration file instead of the default <i>/etc/watchdog.conf</i>.</dl>
<h2>Files</h2>
<dl>
<dt><i>/dev/watchdog </i></p>
<dd>The watchdog device.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-watchdog-conf/">watchdog.conf</a></code>(5)</p>
<dl>
<dt><code><a href="/docs/linux/man/8-watchdog/">watchdog</a></code>(8)</p>
<dd>
