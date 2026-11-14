---
title: "nut(5)"
name: "nut"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nut/"
description: "nut.conf – UPS definitions for Network UPS Tools"
---

<p>nut.conf &#8211; UPS definitions for Network UPS Tools </p>
<h2>Description</h2>
<p>This file attempts to standardize the various files being found in different installations, like /etc/default/nut on Debian based systems and /etc/sysconfig/nut on RedHat based systems. Distribution&#8217;s init script should source this file in order to determine which component(s) has to be started. Blank lines are ignored. Lines with a hash (&#8216;#&#8217;) character at the 1st position of the line are ignored too. They can be used to add comments. </p>
<h2>Directives</h2>
<dl>
<dt>MODE</p>
<dd>Required. Recognized values are none, standalone, netserver and netclient. Defaults to none. </p>
<p> none: Indicates that NUT should not get started automatically, possibly because it is not configured or that an Integrated Power Management or some external system, is used to startup the NUT components. </p>
<p> standalone: Addresses a local only configuration, with 1 UPS protecting the local system. This implies to start the 3 NUT layers (driver, upsd and upsmon), with the related configuration files. This mode can also address UPS redundancy. </p>
<p> netserver: Like the standalone configuration, but also need some more ACLs and possibly a specific LISTEN directive in upsd.conf. Since this MODE is open to the network, a special care should be applied to security concerns. </p>
<p> netclient: When only upsmon is required, possibly because there are other hosts that are more closely attached to the UPS, the MODE should be set to netclient. </p>
<dt>UPSD_OPTIONS</p>
<dd>Optional. Set upsd specific options. See <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) for more details. It is ignored when MODE above indicates that no upsd should be running. </p>
<dt>UPSMON_OPTIONS</p>
<dd>Optional. Set upsmon specific options. See <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8) for more details. It is ignored when MODE above indicates that no upsmon should be running. </p>
<dt>POWEROFF_WAIT</p>
<dd>Optional. At the end of an emergency system halt, the upsmon master will signal the UPS to switch off. This may fail for a number of reasons. Most notably is the case that mains power returns during the shutdown process. See the section &quot;Power races&quot; in /usr/share/doc/nut/docs/shutdown.txt.gz. The system will wait this long for the UPS to cut power, and then reboot. It should be long enough to exhaust the batteries, in case line power continues to be unavailable. On the other hand, it should not be so long that the system remains offline for an unreasonable amount of time if line power has returned. See <code><a href="/docs/linux/man/1-sleep/">sleep</a></code>(1) for compatible time syntax. If you specify the time in seconds, use the &quot;s&quot; suffix. </p>
<p> WARNING: this workaround might be dangerous under some circumstances. Please read <a rel="nofollow" href="http://bugs.debian.org/358696">http://bugs.debian.org/358696</a> for more details. </p>
</dl>
<h2>Example</h2>
<p># /etc/nut/nut.conf. See <a href="/docs/linux/man/5-nut-conf/">nut.conf</a>(5) MODE = none </p>
<pre><code>UPSD_OPTIONS = &quot;&quot;
UPSMON_OPTIONS = &quot;&quot;</code></pre>
<p> # POWEROFF_WAIT = 15m </p>
<h2>Integration</h2>
<p>An init script, such as /etc/init.d/nut, is expected to source this file in order to determine which component(s) has to be started.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5), <code><a href="/docs/linux/man/5-upsd-conf/">upsd.conf</a></code>(5), <code><a href="/docs/linux/man/5-upsd-users/">upsd.users</a></code>(5), <code><a href="/docs/linux/man/5-upsmon-conf/">upsmon.conf</a></code>(5)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
