---
title: "pulse-client-conf(5)"
name: "pulse-client-conf"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pulse-client-conf/"
description: "pulse-client.conf – PulseAudio client configuration file"
---

<p>pulse-client.conf &#8211; PulseAudio client configuration file</p>
<h2>Synopsis</h2>
<p><i>~/.config/pulse/client.conf</i><code> </p>
<p> </code><i>~/.config/pulse/client.conf.d/*.conf</i><code> </p>
<p> </code><i>/etc/pulse/client.conf</i><code> </p>
<p> </code><i>/etc/pulse/client.conf.d/*.conf</i></p>
<h2>Description</h2>
<p>The PulseAudio client library reads configuration directives from a configuration file on startup. If the per-user file <i>~/.config/pulse/client.conf</i> exists, it is used, otherwise the system configuration file <i>/etc/pulse/client.conf</i> is used. In addition to those main files, configuration directives can also be put in files under directories <i>~/.config/pulse/client.conf.d/</i> and <i>/etc/pulse/client.conf.d/</i>. Those files have to have the .conf file name extension, but otherwise the file names can be chosen freely. The files under client.conf.d are processed in alphabetical order. In case the same option is set in multiple files, the last file to set an option overrides earlier files. The main client.conf file is processed first, so options set in files under client.conf.d override the main file. </p>
<p> The configuration file is a simple collection of variable declarations. If the configuration file parser encounters either ; or # it ignores the rest of the line until its end. </p>
<p> For the settings that take a boolean argument the values <code>true</code>, <code>yes</code>, <code>on</code> and <code>1</code> are equivalent, resp. <code>false</code>, <code>no</code>, <code>off</code>, <code>0</code>.</p>
<h2>Directives</h2>
<dl>
<dt><code>default-sink=</code> The default sink to connect to. If specified overwrites the setting in the daemon. The environment variable <code>$PULSE_SINK</code> however takes precedence.</p>
<dd>
<dt><code>default-source=</code> The default source to connect to. If specified overwrites the setting in the daemon. The environment variable <code>$PULSE_SOURCE</code> however takes precedence.</p>
<dd>
<dt><code>default-server=</code> The default server to connect to. The environment variable <code>$PULSE_SERVER</code> takes precedence.</p>
<dd>
<dt><code>autospawn=</code> Autospawn a PulseAudio daemon when needed. Takes a boolean value, defaults to <code>yes</code>. Note that setting this to &quot;no&quot; doesn&#8217;t disable the systemd service. The autospawn option is only meant to be used on systems without systemd. If you use systemd to start PulseAudio, use &quot;systemctl &#8211;user stop pulseaudio.service pulseaudio.socket&quot; to stop the daemon temporarily, or &quot;systemctl &#8211;user mask pulseaudio.service pulseaudio.socket&quot; to permanently disable the units (the &quot;disable&quot; command of systemctl probably won&#8217;t work, because the pulseaudio.socket unit is often installed to /usr/lib/systemd/user/sockets.target.wants/, which makes it impossible to disable the unit with the &quot;disable&quot; command).</p>
<dd>
<dt><code>daemon-binary=</code> Path to the PulseAudio daemon to run when autospawning. Defaults to a path configured at compile time.</p>
<dd>
<dt><code>extra-arguments=</code> Extra arguments to pass to the PulseAudio daemon when autospawning. Defaults to <code>&#8211;log-target=syslog</code></p>
<dd>
<dt><code>cookie-file=</code> Specify the path to the PulseAudio authentication cookie. Defaults to <i>~/.config/pulse/cookie</i>.</p>
<dd>
<dt><code>enable-shm=</code> Enable data transfer via POSIX or memfd shared memory. Takes a boolean argument, defaults to <code>yes</code>. If set to <code>no</code>, communication with the server will be exclusively done through data-copy over sockets.</p>
<dd>
<dt><code>enable-memfd=</code>. Enable data transfer via memfd shared memory. Takes a boolean argument, defaults to <code>yes</code>.</p>
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
