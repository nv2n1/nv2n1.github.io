---
title: "networkd-dispatcher(8)"
name: "networkd-dispatcher"
section: "8"
letter: "n"
url: "/docs/linux/man/8-networkd-dispatcher/"
description: "networkd-dispatcher – Dispatcher service for systemd-networkd connection status changes"
---

<p>networkd-dispatcher &#8211; Dispatcher service for systemd-networkd connection status changes</p>
<h2>Synopsis</h2>
<p><code>networkd-dispatcher</code> [-h] [-S <i>SCRIPT_DIR</i>] [-T] [-v] [-q]</p>
<h2>Description</h2>
<p>Dispatcher daemon for systemd-networkd connection status changes. This daemon is similar to NetworkManager-dispatcher, but is much more limited in the types of events it supports due to the limited nature of <i><a href="/docs/linux/man/8-systemd-networkd/">systemd-networkd</a>(8)</i>. </p>
<p> Desired actions (scripts) are placed into directories that reflect systemd-networkd operational states under <i>SCRIPT_DIR</i> and are executed when the daemon receives the relevant event from systemd-networkd. </p>
<p> The daemon listens for signals from systemd-networkd over dbus, so it should be very light on resources (e.g. no polling). It is meant to be run as a system-wide daemon (as root). This allows it to be used for tasks such as starting a VPN after a connection is established.</p>
<h2>Options</h2>
<p><code>-h, &#8211;help</code></p>
<dl>
<dd>Print command-line syntax and program options to stdout.</dl>
<p> <code>-S, &#8211;script-dir=</code><i>SCRIPT_DIR</i></p>
<dl>
<dd>Location under which to look for scripts. Like the <i>PATH</i> environment variable, this may contain multiple directories separated by : and in case multiple directories have scripts with the same name, the earliest directory wins. Defaults to /etc/networkd-dispatcher:/usr/lib/networkd-dispatcher.</dl>
<p> <code>-T, &#8211;run-startup-triggers</code></p>
<dl>
<dd>Generate events reflecting preexisting state and behavior on startup. This can be used to ensure that triggers are belatedly run even if networkd-dispatcher is invoked after systemd-networkd has already started an interface.</dl>
<p> <code>-v, &#8211;verbose</code></p>
<dl>
<dd>Increase verbosity by one level. The default level is <i>WARNING</i>. Each use of <i>-v</i> will increment the log level (towards <i>INFO</i> or <i>DEBUG</i>), and each use of <i>-q</i> will decrement it (towards <i>ERROR</i> or <i>CRITICAL</i>).</dl>
<p> <code>-q, &#8211;quiet</code></p>
<dl>
<dd>Decrease verbosity by one level.</dl>
<h2>Configuration Files</h2>
<p>The systemd service reads <i>/etc/default/networkd-dispatcher</i> as an environment file for additional daemon arguments. </p>
<p> The scripts to be run on network changes are in subdirectories <i>routable.d/</i>, <i>dormant.d/</i>, <i>no-carrier.d/</i>, <i>off.d/</i>, <i>carrier.d/</i>, <i>degraded.d/</i>, <i>configured.d</i>, <i>configuring.d/</i> inside <i>SCRIPT_DIR</i>. The default value for <i>SCRIPT_DIR</i> is <i>/etc/networkd-dispatcher:/usr/lib/networkd-dispatcher</i>. </p>
<p> For information about the network operational states exposed by systemd, see <a href="/docs/linux/man/1-networkctl/">networkctl</a>(1).</p>
<h2>Resources</h2>
<p>GitHub: <a rel="nofollow" href="https://github.com/craftyguy/networkd-dispatcher">https://github.com/craftyguy/networkd-dispatcher</a></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-systemd-networkd/">systemd-networkd</a>(8), <a href="/docs/linux/man/1-networkctl/">networkctl</a>(1) </p>
