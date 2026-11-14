---
title: "hwclock(5)"
name: "hwclock"
section: "5"
letter: "h"
url: "/docs/linux/man/5-hwclock/"
description: "hwclock – settings that affect the behaviour of the hwclock init script"
---

<p>hwclock &#8211; settings that affect the behaviour of the hwclock init script</p>
<h2>Description</h2>
<p>The <i>/etc/default/hwclock</i> file contains settings in POSIX format:</p>
<dl>
<dd>VAR=VAL</dl>
<p> Only one assignment is allowed per line. Comments (starting with &#8216;#&#8217;) are also allowed. </p>
<h2>Settings</h2>
<p>The following settings can be set. </p>
<dl>
<dt><code>HCTOSYS_DEVICE</code></p>
<dd>The hardware clock device you want to use. Defaults to <code>rtc0</code>. It should probably match the CONFIG_RTC_HCTOSYS_DEVICE kernel config option. </p>
<p> If you change this, you also need to install a custom udev rule, mirroring <code>/usr/lib/udev/rules.d/85-hwclock.rules</code>. Otherwise, the hardware clock device will be ignored during boot. </p>
<p> On almost all systems, this should not be changed. </p>
</dl>
<h2>Notes</h2>
<p>On systems using systemd as init, the hwclock init script is ignored. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8), <code><a href="/docs/linux/man/8-systemd-timesyncd-service/">systemd-timesyncd.service</a></code>(8) </p>
