---
title: "systemd-rc-local-generator(8)"
name: "systemd-rc-local-generator"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-rc-local-generator/"
description: "systemd-rc-local-generator, rc-local.service – Compatibility generator and service to start /etc/rc.local during boot"
---

<p>systemd-rc-local-generator, rc-local.service &#8211; Compatibility generator and service to start /etc/rc.local during boot</p>
<h2>Synopsis</h2>
<p>/lib/systemd/system-generators/systemd-rc-local-generator </p>
<p> rc-local.service</p>
<h2>Description</h2>
<p><code>systemd-rc-local-generator</code> is a generator that checks whether /etc/rc.local exists and is executable, and if it is, pulls the rc-local.service unit into the boot process. This unit is responsible for running this script during late boot. The script is run after network.target, but in parallel with most other regular system services. </p>
<p> Note that rc-local.service runs with slightly different semantics than the original System V version, which was executed &quot;last&quot; in the boot process, which is a concept that does not translate to systemd. </p>
<p> Also note that rc-local.service is ordered after network.target, which does not mean that the network is functional, see <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7). If the script requires a configured network connection, it may be desirable to pull in and order it after network-online.target with a drop-in: </p>
<dl>
<dd>
<pre># /etc/systemd/system/rc-local.service.d/network.conf
[Unit]
Wants=network-online.target
After=network-online.target</pre>
</dl>
<p> Support for /etc/rc.local is provided for compatibility with specific System V systems only. However, it is strongly recommended to avoid making use of this script today, and instead provide proper unit files with appropriate dependencies for any scripts to run during the boot process. Note that the path to the script is set at compile time and varies between distributions. </p>
<p> systemd-rc-local-generator implements <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) </p>
