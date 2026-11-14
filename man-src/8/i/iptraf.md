---
title: "iptraf(8)"
name: "iptraf"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iptraf/"
description: "iptraf – Interactive Colorful IP LAN Monitor"
---

<p>iptraf &#8211; Interactive Colorful IP LAN Monitor</p>
<h2>Synopsis</h2>
<p><code>iptraf</code> { [ <code>-f</code> ] [ <code>-q</code> ] [ { <code>-i</code> <i>iface</i> | <code>-g</code> | <code>-d</code> <i>iface</i> | <code>-s</code> <i>iface</i> | <code>-z</code> <i>iface</i> | <code>-l</code> <i>iface</i> } [ <code>-t</code> <i>timeout</i> ] [ <code>-B</code> [ <code>-L</code> <i>logfile</i> ] ] ] | [ <code>-h</code> ] }</p>
<h2>Description</h2>
<p><code>iptraf</code> is an ncurses-based IP LAN monitor that generates various network statistics including TCP info, UDP counts, ICMP and OSPF information, Ethernet load info, node stats, IP checksum errors, and others. If the command is issued without any command-line options, the program comes up in interactive mode, with the various facilities accessed through the main menu. </p>
<h2>Options</h2>
<p>These options can also be supplied to the command:</p>
<dl>
<dt><code>-i </code><i>iface</i></p>
<dd>immediately start the IP traffic monitor on the specified interface, or all interfaces if &quot;-i all&quot; is specified</p>
<dt><code>-g</code></p>
<dd>immediately start the general interface statistics</p>
<dt><code>-d </code><i>iface</i></p>
<dd>allows you to immediately start the detailed on the indicated interface (iface)</p>
<dt><code>-s </code><i>iface</i></p>
<dd>allows you to immediately monitor TCP and UDP traffic on the specified interface (iface)</p>
<dt><code>-z </code><i>iface</i></p>
<dd>shows packet counts by size on the specified interface</p>
<dt><code>-l </code><i>iface</i></p>
<dd>start the LAN station monitor on the specified interface, or all LAN interfaces if &quot;-l all&quot; is specified</p>
<dt><code>-t </code><i>timeout</i></p>
<dd>tells IPTraf to run the specified facility for only <i>timeout</i> minutes. This option is used only with one of the above parameters.</p>
<dt><code>-B</code></p>
<dd>redirect standard output to /dev/null, closes standard input, and forks the program into the background. Can be used only with one of the facility invocation parameters above. Send the backgrounded process a USR2 signal to terminate.</p>
<dt><code>-L logfile</code></p>
<dd>allows you to specify an alternate log file name. The default log file name is based on either the interface selected (detailed interface statistics, TCP/UDP service statistics, packet size breakdown), or the instance of the facility (IP traffic monitor, LAN station monitor). If a path is not specified, the log file is placed in <code>/var/log/iptraf</code></p>
<dt><code>-f</code></p>
<dd>clears all locks and counters, causing this instance of IPTraf to think it&#8217;s the first one running. This should only be used to recover from an abnormal termination or system crash.</p>
<dt><code>-q</code></p>
<dd>no longer needed, maintained only for compatibility.</p>
<dt><code>-h</code></p>
<dd>shows a command summary</dl>
<h2>Signals</h2>
<p>&nbsp;<wbr>SIGUSR1 &#8211; rotates log files while program is running<br />
&nbsp;<wbr>SIGUSR2 &#8211; terminates an IPTraf process running in the background.</p>
<h2>Files</h2>
<p>&nbsp;<wbr>/var/log/iptraf/*.log &#8211; log file<br />
&nbsp;<wbr>/var/lib/iptraf/*&nbsp;<wbr>&#8211; important IPTraf data files</p>
<h2>See Also</h2>
<p>&nbsp;<wbr>Documentation/*&nbsp;<wbr>&#8211; complete documentation written by the author </p>
<h2>Author</h2>
<p>Gerard Paul Java (riker [at] mozcom.com)</p>
<h2>Manual Author</h2>
<p>Frederic Peters (fpeters [at] debian.org), using iptraf &#8211;help General manual page modifications by Gerard Paul Java (riker [at] mozcom.com)</p>
