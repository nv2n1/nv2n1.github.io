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
<p> <code>hostapd_cli</code> [-p&lt;path&gt;] [-i&lt;ifname&gt;] [-a&lt;path&gt;] [-hvB] [command..]</p>
<p> This manual page documents briefly the <code>hostapd_cli</code> utility. </p>
<p> <code>hostapd_cli</code> is a command-line interface for the <code>hostapd</code> daemon. </p>
<p> <code>hostapd</code> is a user space daemon for access point and authentication servers. It implements IEEE 802.11 access point management, IEEE 802.1X/WPA/WPA2/EAP Authenticators and RADIUS authentication server. For more information about <code>hostapd</code> refer to the <code><a href="/docs/linux/man/8-hostapd/">hostapd</a></code>(8) man page.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below. For a complete description, run <code>hostapd_cli</code> from the command line.</p>
<dl>
<dt><code>-p&lt;path&gt;</code></dt>
<dd> Path to find control sockets. </dd>
<p> Default: /var/run/hostapd</p>
<dt><code>-i&lt;ifname&gt;</code></dt>
<dd> Interface to listen on. </dd>
<p> Default: first interface found in socket path.</p>
<dt><code>-a&lt;path&gt;</code></dt>
<dd> Run in daemon mode executing the action file based on events from hostapd.</dd>
<dt><code>-B</code></dt>
<dd> Run a daemon in the background.</dd>
<dt><code>-h</code></dt>
<dd> Show usage.</dd>
<dt><code>-v</code></dt>
<dd> Show hostapd_cli version.</dd></dl>
<h2>COMMANDS</h2>
<p> A summary of commands is included below. For a complete description, run <code>hostapd_cli</code> from the command line.</p>
<dl>
<dt><code>mib</code></dt>
<dd> Get MIB variables (dot1x, dot11, radius).</dd>
<dt><code>sta &lt;addr&gt;</code></dt>
<dd> Get MIB variables for one station.</dd>
<dt><code>all_sta</code></dt>
<dd> Get MIB variables for all stations.</dd>
<dt><code>help</code></dt>
<dd> Get usage help.</dd>
<dt><code>interface [ifname] </code></dt>
<dd> Show interfaces/select interface.</dd>
<dt><code>level &lt;debug level&gt;</code></dt>
<dd> Change debug level.</dd>
<dt><code>license</code></dt>
<dd> Show full <code>hostapd_cli</code> license.</dd>
<dt><code>quit</code></dt>
<dd> Exit hostapd_cli.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-hostapd/">hostapd</a></code>(8).</p>
<h2>AUTHOR</h2>
<p> hostapd_cli was written by Jouni Malinen &lt;j@w1.fi&gt;. </p>
<p> This manual page was written by Faidon Liambotis &lt;faidon [at] cube.gr&gt;, for the Debian project (but may be used by others). </p>
