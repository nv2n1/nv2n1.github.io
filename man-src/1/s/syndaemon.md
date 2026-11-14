---
title: "syndaemon(1)"
name: "syndaemon"
section: "1"
letter: "s"
url: "/docs/linux/man/1-syndaemon/"
description: "syndaemon – a program that monitors keyboard activity and disables the touchpad when the keyboard is being used."
---

<h2 class="name">NAME</h2>
<p> syndaemon &#8211; a program that monitors keyboard activity and disables the touchpad when the keyboard is being used. </p>
<h2>SYNOPSIS</h2>
<p> syndaemon [<i>-i idle-time</i>] [<i>-m poll-inverval</i>] [<i>-d</i>] [<i>-p pid-file</i>] [<i>-t</i>] [<i>-k</i>] [<i>-K</i>] [<i>-R</i>]</p>
<h2>DESCRIPTION</h2>
<p> Disabling the touchpad while typing avoids unwanted movements of the pointer that could lead to giving focus to the wrong window.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code> &lt;<i>idle-time</i>&gt;</p>
<dd> How many seconds to wait after the last key press before enabling the touchpad. (default is 2.0s).</dl>
<dl>
<dt><code>-m</code> &lt;<i>poll-interval</i>&gt;</p>
<dd> How many milliseconds to wait between two polling intervals. If this value is too low, it will cause unnecessary wake-ups. If this value is too high, some key presses (press and release happen between two intervals) may not be noticed. This switch has no effect when running with <code>-R</code>. Default is 200ms.</dl>
<dl>
<dt><code>-d</code></p>
<dd> Start as a daemon, ie in the background.</dl>
<dl>
<dt><code>-p</code> &lt;<i>pid-file</i>&gt;</p>
<dd> Create a pid file with the specified filename. A pid file will only be created if the program is started in daemon mode.</dl>
<dl>
<dt><code>-t</code></p>
<dd> Only disable tapping and scrolling, not mouse movements, in response to keyboard activity.</dl>
<dl>
<dt><code>-k</code></p>
<dd> Ignore modifier keys when monitoring keyboard activity.</dl>
<dl>
<dt><code>-K</code></p>
<dd> Like -k but also ignore Modifier+Key combos.</dl>
<dl>
<dt><code>-R</code></p>
<dd> Use the XRecord extension for detecting keyboard activity instead of polling the keyboard state.</dl>
<dl>
<dt><code>-?</code></p>
<dd> Show the help message.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> Specifies the X server to contact.</dl>
<h2>EXIT CODES</h2>
<p> If syndaemon exists with a return code other than 0, the error encountered is as below. </p>
<dl>
<dt><code>Exit code 1</p>
<dd> Invalid commandline argument.</dl>
<dl>
<dt>Exit code 2</p>
<dd> The connection to the X sever could not be established or no touchpad device could be found.</dl>
<dl>
<dt>Exit code 3</p>
<dd> The fork into daemon mode failed or the pid file could not be created.</dl>
<dl>
<dt>Exit code 4</p>
<dd> XRECORD requested but not available or usable on the server.</dl>
<p> </code></p>
<h2>CAVEATS</h2>
<p> It doesn&#8217;t make much sense to connect to a remote X server, because the daemon will then monitor the remote server for keyboard activity, but will disable the touchpad on the local machine.</p>
<h2>AUTHORS</h2>
<p> Peter Osterlund &lt;petero2 [at] telia.com&gt;.</p>
<dl>
<dt>This man page was written by Mattia Dongili &lt;malattia [at] debian.org&gt;</p>
<dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/1-synclient/">synclient</a>(1), <a href="/docs/linux/man/4-synaptics/">synaptics</a>(4) </p>
<h2>Index</h2>
