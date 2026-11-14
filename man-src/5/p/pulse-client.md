---
title: "pulse-client(5)"
name: "pulse-client"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pulse-client/"
description: "pulse-client.conf – PulseAudio client configuration file"
---

<p>pulse-client.conf &#8211; PulseAudio client configuration file</p>
<h2>Synopsis</h2>
<p><i>~/.config/pulse/client.conf</i><code> </p>
<p> </code><i>/etc/pulse/client.conf</i></p>
<h2>Description</h2>
<p>The PulseAudio client library reads configuration directives from a file <i>~/.config/pulse/client.conf</i> on startup and when that file doesn&#8217;t exist from <i>/etc/pulse/client.conf</i>. </p>
<p> The configuration file is a simple collection of variable declarations. If the configuration file parser encounters either ; or # it ignores the rest of the line until its end. </p>
<p> For the settings that take a boolean argument the values <code>true</code>, <code>yes</code>, <code>on</code> and <code>1</code> are equivalent, resp. <code>false</code>, <code>no</code>, <code>off</code>, <code>0</code>.</p>
<h2>Directives</h2>
<dl>
<dt><code>default-sink=</code> The default sink to connect to. If specified overwrites the setting in the daemon. The environment variable <code>$PULSE_SINK</code> however takes precedence.</p>
<dd>
<dt><code>default-source=</code> The default source to connect to. If specified overwrites the setting in the daemon. The environment variable <code>$PULSE_SOURCE</code> however takes precedence.</p>
<dd>
<dt><code>default-server=</code> The default sever to connect to. The environment variable <code>$PULSE_SERVER</code> takes precedence.</p>
<dd>
<dt><code>autospawn=</code> Autospawn a PulseAudio daemon when needed. Takes a boolean value, defaults to <code>yes</code>.</p>
<dd>
<dt><code>daemon-binary=</code> Path to the PulseAudio daemon to run when autospawning. Defaults to a path configured at compile time.</p>
<dd>
<dt><code>extra-arguments=</code> Extra arguments to pass to the PulseAudio daemon when autospawning. Defaults to <code>&#8211;log-target=syslog</code></p>
<dd>
<dt><code>cookie-file=</code> Specify the path to the PulseAudio authentication cookie. Defaults to <i>~/.config/pulse/cookie</i>.</p>
<dd>
<dt><code>enable-shm=</code> Enable data transfer via POSIX shared memory. Takes a boolean argument, defaults to <code>yes</code>.</p>
<dd>
<dt><code>shm-size-bytes=</code> Sets the shared memory segment size for clients, in bytes. If left unspecified or is set to 0 it will default to some system-specific default, usually 64 MiB. Please note that usually there is no need to change this value, unless you are running an OS kernel that does not do memory overcommit.</p>
<dd>
<dt><code>auto-connect-localhost=</code> Automatically try to connect to localhost via IP. Enabling this is a potential security hole since connections are only authenticated one-way and a rogue server might hence fool a client into sending it its private (e.g. VoIP call) data. This was enabled by default on PulseAudio version 0.9.21 and older. Defaults to <code>no</code>.</p>
<dd>
<dt><code>auto-connect-display=</code> Automatically try to connect to the host X11&#8217;s $DISPLAY variable is set to. The same security issues apply as to <code>auto-connect-localhost=</code>. Defaults to <code>no</code>.</p>
<dd></dl>
<h2>Authors</h2>
<p>The PulseAudio Developers &lt;pulseaudio-discuss (at) lists (dot) freedesktop (dot) org&gt;; PulseAudio is available from <code><a rel="nofollow" href="http://pulseaudio.org/">http://pulseaudio.org/</a></code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pulse-daemon-conf/">pulse-daemon.conf</a>(5)</code>, <code><a href="/docs/linux/man/1-pulseaudio/">pulseaudio</a>(1)</code> </p>
