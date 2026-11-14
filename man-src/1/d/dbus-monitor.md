---
title: "dbus-monitor(1)"
name: "dbus-monitor"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbus-monitor/"
description: "dbus-monitor – debug probe to print message bus messages"
---

<h2 class="name">NAME</h2>
<p> dbus-monitor &#8211; debug probe to print message bus messages </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>dbus-monitor</code> [&#8211;system | &#8211;session | &#8211;address&nbsp;<i>ADDRESS</i>] [&#8211;profile | &#8211;monitor | &#8211;pcap | &#8211;binary] [<i>watch</i>&nbsp;<i>expressions</i>]</p>
<dd>
</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dbus-monitor</code> command is used to monitor messages going through a D-Bus message bus. See m[blue]<code><a rel="nofollow" href="http://www.freedesktop.org/software/dbus/">http://www.freedesktop.org/software/dbus/</a></code>m[] for more information about the big picture. </p>
<p> There are two well-known message buses: the systemwide message bus (installed on many systems as the &quot;messagebus&quot; service) and the per-user-login-session message bus (started each time a user logs in). The &#8211;system and &#8211;session options direct <code>dbus-monitor</code> to monitor the system or session buses respectively. If neither is specified, <code>dbus-monitor</code> monitors the session bus. </p>
<p> <code>dbus-monitor</code> has two different text output modes: the &#8216;classic&#8217;-style monitoring mode, and profiling mode. The profiling format is a compact format with a single line per message and microsecond-resolution timing information. The &#8211;profile and &#8211;monitor options select the profiling and monitoring output format respectively. </p>
<p> <code>dbus-monitor</code> also has two binary output modes. The binary mode, selected by &#8211;binary, outputs the entire binary message stream (without the initial authentication handshake). The PCAP mode, selected by &#8211;pcap, adds a PCAP file header to the beginning of the output, and prepends a PCAP message header to each message; this produces a binary file that can be read by, for instance, Wireshark. </p>
<p> If no mode is specified, <code>dbus-monitor</code> uses the monitoring output format. </p>
<p> In order to get <code>dbus-monitor</code> to see the messages you are interested in, you should specify a set of watch expressions as you would expect to be passed to the <i>dbus_bus_add_match</i> function. </p>
<p> The message bus configuration may keep <code>dbus-monitor</code> from seeing all messages, especially if you run the monitor as a non-root user.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Monitor the system message bus.</dl>
<p> <code>&#8211;session</code></p>
<dl>
<dt>
<dd> Monitor the session message bus. (This is the default.)</dl>
<p> <code>&#8211;address ADDRESS</code></p>
<dl>
<dt>
<dd> Monitor an arbitrary message bus given at ADDRESS.</dl>
<p> <code>&#8211;profile</code></p>
<dl>
<dt>
<dd> Use the profiling output format.</dl>
<p> <code>&#8211;monitor</code></p>
<dl>
<dt>
<dd> Use the monitoring output format. (This is the default.)</dl>
<h2>EXAMPLE</h2>
<p> Here is an example of using dbus-monitor to watch for the gnome typing monitor to say things </p>
<dl>
<dt>
<dd>
<pre>
  dbus-monitor &quot;type='signal',sender='org.gnome.TypingMonitor',interface='org.gnome.TypingMonitor'&quot;
</pre>
</dl>
<h2>AUTHOR</h2>
<p> dbus-monitor was written by Philip Blundell. The profiling output mode was added by Olli Salli.</p>
<h2>BUGS</h2>
<p> Please send bug reports to the D-Bus mailing list or bug tracker, see m[blue]<code><a rel="nofollow" href="http://www.freedesktop.org/software/dbus/">http://www.freedesktop.org/software/dbus/</a></code>m[] </p>
<h2>Index</h2>
