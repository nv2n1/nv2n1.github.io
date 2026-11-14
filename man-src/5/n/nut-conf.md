---
title: "nut-conf(5)"
name: "nut-conf"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nut-conf/"
description: "nut.conf – UPS definitions for Network UPS Tools"
---

<p>nut.conf &#8211; UPS definitions for Network UPS Tools</p>
<h2>Description</h2>
<p>This file attempts to standardize the various files being found in different installations, like /etc/default/nut on Debian based systems and /etc/sysconfig/ups on RedHat based systems. </p>
<p> Distribution&#8217;s init script should source this file in order to determine which components have to be started. </p>
<p> Blank lines are ignored. Lines with a hash (<i>#</i>) character at the 1st position of the line are ignored, too. They can be used to add comments.</p>
<h2>Important Note</h2>
<p>This file is intended to be sourced by shell scripts. You MUST NOT use spaces around the equal sign! </p>
<p> Refer to the EXAMPLE section for illustrations.</p>
<h2>Directives</h2>
<p><code>MODE</code></p>
<dl>
<dd>Required. Recognized values are <i>none</i>, <i>standalone</i>, <i>netserver</i> and <i>netclient</i>. Defaults to <i>none</i>. </p>
<p> none</p>
<dl>
<dd>Indicates that NUT should not get started automatically, possibly because it is not configured or that an Integrated Power Management or some external system, is used to startup the NUT components.</dl>
<p> standalone</p>
<dl>
<dd>Addresses a local only configuration, with 1 UPS protecting the local system. This implies to start the 3 NUT layers (driver, upsd and upsmon), with the related configuration files. This mode can also address UPS redundancy.</dl>
<p> netserver</p>
<dl>
<dd>Like the standalone configuration, but also possibly need one or more specific LISTEN directive(s) in upsd.conf. Since this MODE is open to the network, a special care should be applied to security concerns.</dl>
<p> netclient</p>
<dl>
<dd>When only upsmon is required, possibly because there are other hosts that are more closely attached to the UPS, the MODE should be set to netclient.</dl>
</dl>
<p> <code>UPSD_OPTIONS</code></p>
<dl>
<dd>Optional. Set upsd specific options. See <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) for more details. It is ignored when <i>MODE</i> above indicates that no upsd should be running.</dl>
<p> <code>UPSMON_OPTIONS</code></p>
<dl>
<dd>Optional. Set upsmon specific options. See <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8) for more details. It is ignored when <i>MODE</i> above indicates that no upsmon should be running.</dl>
<p> <code>POWEROFF_WAIT</code></p>
<dl>
<dd>Optional. At the end of an emergency system halt, the upsmon master will signal the UPS to switch off. This may fail for a number of reasons. Most notably is the case that mains power returns during the shutdown process. See the section &quot;Power races&quot; in /usr/share/doc/nut/docs/shutdown.txt.gz. The system will wait this long for the UPS to cut power, and then reboot. It should be long enough to exhaust the batteries, in case line power continues to be unavailable. On the other hand, it should not be so long that the system remains offline for an unreasonable amount of time if line power has returned. See <a href="/docs/linux/man/1-sleep/">sleep</a>(1) for compatible time syntax. If you specify the time in seconds, use the &quot;s&quot; suffix.</dl>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font> </p>
<p> this workaround might be dangerous under some circumstances. Please read <a rel="nofollow" href="http://bugs.debian.org/358696">http://bugs.debian.org/358696</a> for more details. </p>
</dl>
<h2>Example</h2>
<dl>
<dd>
<pre># /etc/nut/nut.conf. See <a href="//www.systutorials.com/docs/linux/man/5-nut.conf/">nut.conf</a>(5)</pre>
</dl>
<dl>
<dd>
<pre>MODE=none</pre>
</dl>
<pre><code>UPSD_OPTIONS=&quot;&quot;
UPSMON_OPTIONS=&quot;&quot;</code></pre>
<dl>
<dd>
<pre># POWEROFF_WAIT=15m</pre>
</dl>
<h2>Integration</h2>
<p>An init script, such as /etc/init.d/nut, is expected to source this file in order to determine which component(s) has to be started.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5), <code><a href="/docs/linux/man/5-upsd-conf/">upsd.conf</a></code>(5), <code><a href="/docs/linux/man/5-upsd-users/">upsd.users</a></code>(5), <code><a href="/docs/linux/man/5-upsmon-conf/">upsmon.conf</a></code>(5)</p>
<h2>Internet Resources</h2>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a></p>
