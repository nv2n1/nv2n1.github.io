---
title: "hostapd_cli(1)"
name: "hostapd_cli"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hostapd_cli/"
description: "hostapd_cli – hostapd command-line interface"
---

<h2>NAME</h2>
<p> hostapd_cli &#8211; hostapd command-line interface</p>
<h2>SYNOPSIS</h2>
<p> <code>hostapd_cli</code> [-p&lt;path&gt;] [-i&lt;ifname&gt;] [-a&lt;path&gt;] [-hvB] [command..]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>hostapd_cli</code> utility. </p>
<p> <code>hostapd_cli</code> is a command-line interface for the <code>hostapd</code> daemon. </p>
<p> <code>hostapd</code> is a user space daemon for access point and authentication servers. It implements IEEE 802.11 access point management, IEEE 802.1X/WPA/WPA2/EAP Authenticators and RADIUS authentication server. For more information about <code>hostapd</code> refer to the <code><a href="/docs/linux/man/8-hostapd/">hostapd</a></code>(8) man page.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below. For a complete description, run <code>hostapd_cli</code> from the command line.</p>
<dl>
<dt><code>-p&lt;path&gt;</code></p>
<dd> Path to find control sockets. </p>
<p> Default: /var/run/hostapd</p>
<dt><code>-i&lt;ifname&gt;</code></p>
<dd> Interface to listen on. </p>
<p> Default: first interface found in socket path.</p>
<dt><code>-a&lt;path&gt;</code></p>
<dd> Run in daemon mode executing the action file based on events from hostapd.</p>
<dt><code>-B</code></p>
<dd> Run a daemon in the background.</p>
<dt><code>-h</code></p>
<dd> Show usage.</p>
<dt><code>-v</code></p>
<dd> Show hostapd_cli version.</dl>
<h2>COMMANDS</h2>
<p> A summary of commands is included below. For a complete description, run <code>hostapd_cli</code> from the command line.</p>
<dl>
<dt><code>mib</code></p>
<dd> Get MIB variables (dot1x, dot11, radius).</p>
<dt><code>sta &lt;addr&gt;</code></p>
<dd> Get MIB variables for one station.</p>
<dt><code>all_sta</code></p>
<dd> Get MIB variables for all stations.</p>
<dt><code>help</code></p>
<dd> Get usage help.</p>
<dt><code>interface [ifname] </code></p>
<dd> Show interfaces/select interface.</p>
<dt><code>level &lt;debug level&gt;</code></p>
<dd> Change debug level.</p>
<dt><code>license</code></p>
<dd> Show full <code>hostapd_cli</code> license.</p>
<dt><code>quit</code></p>
<dd> Exit hostapd_cli.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-hostapd/">hostapd</a></code>(8).</p>
<h2>AUTHOR</h2>
<p> hostapd_cli was written by Jouni Malinen &lt;j@w1.fi&gt;. </p>
<p> This manual page was written by Faidon Liambotis &lt;faidon [at] cube.gr&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
