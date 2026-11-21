---

title: "mousetweaks(1)"
name: "mousetweaks"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mousetweaks/"
description: "mousetweaks – Accessibility enhancements for pointing devices"
---

<p> mousetweaks &#8211; Accessibility enhancements for pointing devices </p>
<h2>SYNOPSIS</h2>
<p> <code>mousetweaks</code> [&#8211;dwell] [&#8211;ssc] [&#8211;dwell-time=FLOAT] [&#8211;ssc-time=FLOAT] [-m|&#8211;dwell-mode=STRING] [-c|&#8211;show-ctw] [-t|&#8211;threshold=INT] [-g|&#8211;geometry] [-s|&#8211;shutdown] [&#8211;daemonize] [-?|&#8211;help]</p>
<h2>DESCRIPTION</h2>
<p> <code>mousetweaks</code> is a collection of accessibility enhancements for pointing devices. This manual page describes the mousetweaks daemon.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;dwell</code></dt>
<dd> Automatically perform mouse clicks without using a physical button.</dd>
<dt><code>&#8211;ssc</code></dt>
<dd> Trigger the secondary mouse button when the primary mouse button is held down for a specified amount of time.</dd>
<dt><code>&#8211;dwell-time=FLOAT</code></dt>
<dd> Time to keep the pointer motionless before a dwell click is performed. Range: 0.2 &#8211; 3.0 seconds.</dd>
<dt><code>&#8211;ssc-time=FLOAT</code></dt>
<dd> Time to hold the primary mouse button before a simulated secondary click is performed. Range: 0.5 &#8211; 3.0 seconds.</dd>
<dt><code>-m, &#8211;dwell-mode=STRING</code></dt>
<dd> Select a dwell mode. Available options: <code>window</code> &#8211; Select the click type from a window or a panel applet. <code>gesture</code> &#8211; Perform different clicks by moving in different directions.</dd>
<dt><code>-c, &#8211;show-ctw</code></dt>
<dd> Show the click-type window. Only useful in combination with &#8211;dwell-mode=window.</dd>
<dt><code>-t, &#8211;threshold=INT</code></dt>
<dd> Ignore small pointer movements. Range: 0 &#8211; 30 pixels.</dd>
<dt><code>-g, &#8211;geometry</code></dt>
<dd> Size and position of the click-type window. Expects a standard X Window System geometry string. ie. WIDTHxHEIGHT+X+Y</dd>
<dt><code>-s, &#8211;shutdown</code></dt>
<dd> Stop the mousetweaks daemon.</dd>
<dt><code>&#8211;daemonize</code></dt>
<dd> Start mousetweaks in the background, ie. spawn a child process.</dd>
<dt><code>&#8211;login</code></dt>
<dd> Start mousetweaks in login mode. Login mode enables workarounds specific to GDM. Currently unused.</dd></dl>
<h2>FILES</h2>
<p> <i>mousetweaks.pid</i></p>
<dl>
<dt>
</dt><dd> The daemon creates a lock file in the $XDG_RUNTIME_DIR directory to keep track of its state. On systems with no user runtime directory, the $XDG_CACHE_HOME directory is used.</dd></dl>
<h2>BUGS</h2>
<p> Report bugs to &lt;<a rel="nofollow" href="http://bugzilla.gnome.org/">http://bugzilla.gnome.org/</a>&gt;</p>
<h2>AUTHORS</h2>
<p> This manual page was written by Francesco Fumanti.</p>
<h2>LICENSE</h2>
<p> Licenced under the GNU General Public License v3 or later. </p>
