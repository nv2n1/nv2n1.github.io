---
title: "aptd(1)"
name: "aptd"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aptd/"
description: "aptd – package managing daemon proving a D-Bus interface"
---

<h2 class="name">NAME</h2>
<p> aptd &#8211; package managing daemon proving a D-Bus interface </p>
<h2>SYNOPSIS</h2>
<p> <code>aptd</code> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>aptd</code> allows to perform package management tasks, e.g. installing or removing software, using a D-Bus interface. The privileges are handled by PolicyKit so the client application doesn&#8217;t need to run as root. Furthermore aptd is started by D-Bus activation only when an user calls a method.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-d, &#8211;debug</p>
<dd> Show additional information on the command line.</p>
<dt>-h, &#8211;help</p>
<dd> Show information about the usage of the command.</p>
<dt>-r, &#8211;replace</p>
<dd> Replace another aptd instance if it is running.</p>
<dt>-p PROFILE_FILE</p>
<dd> Write profiling data to <i>PROFILE_FILE</i> using Python&#8217;s profiler. This is only of use to developers.</p>
<dt>-t, &#8211;disable-timeout</p>
<dd> Do not shutdown the daemon after an idle time.</p>
<dt>&#8211;dummy</p>
<dd> Instead of applying the changes to the system only show a progress. This option is only usable for developers to locate problems in client applications.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/apt/apt.conf.d/20dbus</i></p>
<dd> Adds a small post update hook which will emit the org.debian.apt.CacheChanged signal on the system D-Bus to indicate that the cache has been changed and a possible running aptd instance should reloade its internal cache.</p>
<dt><i>/usr/share/polkit-1/actions/org.debian.apt.policy</i></p>
<dd> The PolicyKit definitions of the privileges used by aptdaemon, e.g. to install packages. To change the privileges please have a look at <code><a href="/docs/linux/man/1-policykit-conf/">PolicyKit.conf</a></code>(1).</p>
<dt><i>/etc/dbus-1/system.d/org.debian.apt.conf</i></p>
<dd> The D-Bus configuration of the org.debian.apt name space.</dl>
<h2>DIAGNOSTICS</h2>
<p> By default aptdaemon logs to the syslog facility AptDaemon. Furthermore you can use the -d option to get additional information on the command line.</p>
<h2>HOMEPAGE</h2>
<p> <a rel="nofollow" href="https://launchpad.net/aptdaemon">https://launchpad.net/aptdaemon</a></p>
<h2>BUGS</h2>
<p> You can report bugs at the Launchpad site of aptdaemon: <a rel="nofollow" href="https://bugs.launchpad.net/aptdaemon/+filebug">https://bugs.launchpad.net/aptdaemon/+filebug</a></p>
<h2>AUTHOR</h2>
<p> Sebastian Heinlein &lt;devel at glatzor dot de&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-aptdcon/">aptdcon</a></code>(1), <code><a href="/docs/linux/man/7-org-debian-apt/">org.debian.apt</a></code>(7), <code><a href="/docs/linux/man/7-org-debian-apt-transaction/">org.debian.apt.transaction</a></code>(7), <code><a href="/docs/linux/man/7-policykit-conf/">PolicyKit.conf</a></code>(7) </p>
<h2>Index</h2>
