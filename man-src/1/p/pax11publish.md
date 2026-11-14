---
title: "pax11publish(1)"
name: "pax11publish"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pax11publish/"
description: "pax11publish – PulseAudio X11 Credential Utility"
---

<h2 class="name">NAME</h2>
<p> pax11publish &#8211; PulseAudio X11 Credential Utility </p>
<h2>SYNOPSIS</h2>
<p> <code>pax11publish -h </p>
<p> pax11publish [</code><i>options</i><code>] [-d] </p>
<p> pax11publish [</code><i>options</i><code>] -e </p>
<p> pax11publish [</code><i>options</i><code>] -i </p>
<p> pax11publish [</code><i>options</i><code>] -r </code></p>
<h2>DESCRIPTION</h2>
<p> The <i>pax11publish</i> utility can be used to dump or manipulate the PulseAudio server credentials that can be stored as properties on the X11 root window. </p>
<p> Please note that the loadable module <i>module-x11-publish</i> exports the same information directly from the PulseAudio sound server, and should in most cases be used in preference over this tool. </p>
<p> Use the following command to dump the raw PulseAudio-specific data that is stored in your X11 root window: </p>
<p> xprop -root | grep ^PULSE_</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Show help.</p>
<dt><code>-d</code></p>
<dd> Read the PulseAudio server credentials currently set on the X11 root window and dump them in a human readable form. This reads the PULSE_SERVER, PULSE_SINK, PULSE_SOURCE and PULSE_COOKIE properties.</p>
<dt><code>-i</code></p>
<dd> Similar to <code>-d</code>, however dumps them in a Bourne shell compatible format so they may be used together with the <i>eval</i> shell command to set the $PULSE_SERVER, $PULSE_SINK, $PULSE_SOURCE environment variables. Also reads the authentication cookie from the root window and stores it in <i>~/.config/pulse/cookie</i>.</p>
<dt><code>-e</code></p>
<dd> Export the currently locally used sound server, sink, source configuration to the X11 root window. This takes the data from the $PULSE_SERVER, $PULSE_SINK, $PULSE_SOURCE environment variables and combines them with the data from <i>~/.config/pulse/client.conf</i> (or <i>/etc/pulse/client.conf</i> if that file does not exist). If specific options are passed on the command line (<code>-S</code>, <code>-O</code>, <code>-I</code>, <code>-c</code>, see below), they take precedence. Also uploads the local authentication cookie <i>~/.config/pulse/cookie</i> to the X11 server.</p>
<dt><code>-r</code></p>
<dd> Removes the configured PulseAudio configuration from the X11 root window.</p>
<dt><code>-D</code> <i>DISPLAY</i></p>
<dd> Connect to the specified X11 display, instead of the default one configured in $DISPLAY.</p>
<dt><code>-S</code> <i>SERVER</i></p>
<dd> Only valid for <code>-e</code>: export the specified PulseAudio server as default to the X11 display instead of the one configured via local configuration.</p>
<dt><code>-O</code> <i>SINK</i></p>
<dd> Only valid for <code>-e</code>: export the specified sink as default sink to the X11 display instead of the one configured via local configuration.</p>
<dt><code>-I</code> <i>SOURCE</i></p>
<dd> Only valid for <code>-e</code>: export the specified source as default to the X11 display instead of the one configured via local configuration.</p>
<dt><code>-c</code> <i>FILE</i></p>
<dd> Only valid for <code>-e</code>: export the PulseAudio authentication cookie stored in the specified file to the X11 display instead of the one stored in <i>~/.config/pulse/cookie</i>.</dl>
<h2>AUTHORS</h2>
<p> The PulseAudio Developers &lt;pulseaudio-discuss (at) lists (dot) freedesktop (dot) org&gt;; PulseAudio is available from <code><a rel="nofollow" href="http://pulseaudio.org/">http://pulseaudio.org/</a></code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pulseaudio/">pulseaudio</a>(1)</code>, <code><a href="/docs/linux/man/1-xprop/">xprop</a>(1)</code> </p>
<h2>Index</h2>
