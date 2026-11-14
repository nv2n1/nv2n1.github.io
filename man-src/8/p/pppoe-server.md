---
title: "pppoe-server(8)"
name: "pppoe-server"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pppoe-server/"
description: "pppoe-server – user-space PPPoE server"
---

<p>pppoe-server &#8211; user-space PPPoE server</p>
<h2>Synopsis</h2>
<p><code>pppoe-server </code>[<i>options</i>] </p>
<h2>Description</h2>
<p><code>pppoe-server</code> is a user-space server for PPPoE (Point-to-Point Protocol over Ethernet) for Linux and other UNIX systems. <code>pppoe-server</code> works in concert with the <code>pppoe</code> client to respond to PPPoE discovery packets and set up PPPoE sessions. </p>
<h2>Options</h2>
<dl>
<dt><code>-F</code></p>
<dd>The <code>-F</code> option causes <code>pppoe-server</code> not to fork and become a daemon. The default is to fork and become a daemon. </p>
<dt><code>-I </code><i>interface</i></p>
<dd>The <code>-I</code> option specifies the Ethernet interface to use. Under Linux, it is typically <i>eth0</i> or <i>eth1</i>. The interface should be &quot;up&quot; before you start <code>pppoe-server</code>, but need not have an IP address. You can supply multiple <code>-I</code> options if you want the server to respond on more than one interface. </p>
<dt><code>-X </code><i>pidfile</i></p>
<dd>This option causes <code>pppoe-server</code> to write its process ID to <i>pidfile</i>. Additionally, it keeps the file locked so that only a single process may be started for a given <i>pidfile</i>. </p>
<dt><code>-q </code><i>/path/to/pppd</i></p>
<dd>Specifies the full path to the <code>pppd</code> program. The default is determined at compile time. One use of this option is to supply a wrapper program that modifies the arguments passed to pppd. This lets you do things not directly supported by the server (for example, specify IPv6 addresses.) </p>
<dt><code>-Q </code><i>/path/to/pppoe</i></p>
<dd>Specifies the full path to the <code>pppoe</code> program. The default is determined at compile time. This option is only relevant if you are <i>not</i> using kernel-mode PPPoE. </p>
<dt><code>-T </code><i>timeout</i></p>
<dd>This option is passed directly to <code>pppoe</code>; see <code><a href="/docs/linux/man/8-pppoe/">pppoe</a></code>(8) for details. If you are using kernel-mode PPPoE, this option has <i>no effect</i>. </p>
<dt><code>-C </code><i>ac_name</i></p>
<dd>Specifies which name to report as the access concentrator name. If not supplied, the host name is used. </p>
<dt><code>-S </code><i>name</i></p>
<dd>Offer a service named <i>name</i>. Multiple <code>-S</code> options may be specified; each one causes the named service to be advertised in a Service-Name tag in the PADO frame. The first <code>-S</code> option specifies the default service, and is used if the PPPoE client requests a Service-Name of length zero. </p>
<dt><code>-m </code><i>MSS</i></p>
<dd>This option is passed directly to <code>pppoe</code>; see <code><a href="/docs/linux/man/8-pppoe/">pppoe</a></code>(8) for details. If you are using kernel-mode PPPoE, this option has <i>no effect</i>. </p>
<dt><code>-x </code><i>n</i></p>
<dd>Limit the number of sessions per peer MAC address to <i>n</i>. If a given MAC address attempts to create more than <i>n</i> sessions, then its PADI and PADR packets are ignored. If you set <i>n</i> to 0 (the default), then no limit is imposed on the number of sessions per peer MAC address. </p>
<dt><code>-s</code></p>
<dd>This option is passed directly to <code>pppoe</code>; see <code><a href="/docs/linux/man/8-pppoe/">pppoe</a></code>(8) for details. In addition, it causes <code>pppd</code> to be invoked with the <i>sync</i> option. </p>
<dt><code>-L </code><i>ip</i></p>
<dd>Sets the local IP address. This is passed to spawned <code>pppd</code> processes. If not specified, the default is 10.0.0.1. </p>
<dt><code>-R </code><i>ip</i></p>
<dd>Sets the starting remote IP address. As sessions are established, IP addresses are assigned starting from <i>ip</i>. <code>pppoe-server</code> automatically keeps track of the pool of addresses and passes a valid remote IP address to <code>pppd</code>. If not specified, a starting address of 10.67.15.1 is used. </p>
<dt><code>-D</code></p>
<dd>Delegate the allocation of IP addresses to <code>pppd</code>. If specified, no local and remote addresses passed to pppd. </p>
<dt><code>-N </code><i>num</i></p>
<dd>Allows at most <i>num</i> concurrent PPPoE sessions. If not specified, the default is 64. </p>
<dt><code>-O </code><i>fname</i></p>
<dd>This option causes <code>pppoe-server</code> to tell <code>pppd</code> to use the option file <i>fname</i> instead of the default <i>/etc/ppp/pppoe-server-options</i>. </p>
<dt><code>-p </code><i>fname</i></p>
<dd>Reads the specified file <i>fname</i> which is a text file consisting of one IP address per line. These IP addresses will be assigned to clients. The number of sessions allowed will equal the number of addresses found in the file. The <code>-p</code> option overrides both <code>-R</code> and <code>-N</code>. </p>
<p> In addition to containing IP addresses, the pool file can contain lines of the form: </p>
<pre> a.b.c.d-e</pre>
<p>which includes all IP addresses from a.b.c.d to a.b.c.e. For example, the line: </p>
<pre> 1.2.3.4-7</pre>
<p>is equivalent to: </p>
<pre> 1.2.3.4
 1.2.3.5
 1.2.3.6
 1.2.3.7</pre>
<dt><code>-r</code></p>
<dd>Tells the PPPoE server to randomly permute session numbers. Instead of handing out sessions in order, the session numbers are assigned in an unpredictable order. </p>
<dt><code>-u</code></p>
<dd>Tells the server to invoke <code>pppd</code> with the <i>unit</i> option. Note that this option only works for <code>pppd</code> version 2.4.0 or newer. </p>
<dt><code>-o </code><i>offset</i></p>
<dd>Instead of numbering PPPoE sessions starting at 1, they will be numbered starting at <i>offset</i>+1. This allows you to run multiple servers on a given machine; just make sure that their session numbers do not overlap. </p>
<dt><code>-f disc:sess</code></p>
<dd>The <code>-f</code> option sets the Ethernet frame types for PPPoE discovery and session frames. The types are specified as hexadecimal numbers separated by a colon. Standard PPPoE uses frame types 8863:8864. <i>You should not use this option</i> unless you are absolutely sure the peer you are dealing with uses non-standard frame types. </p>
<dt><code>-k</code></p>
<dd>The <code>-k</code> option tells the server to use kernel-mode PPPoE on Linux. This option is available only on Linux kernels 2.4.0 and later, and only if the server was built with kernel-mode support. </p>
<dt><code>-i</code></p>
<dd>The <code>-i</code> option tells the server to completely ignore PADI frames if there are no free session slots. </p>
<dt><code>-h</code></p>
<dd>The <code>-h</code> option prints a brief usage message and exits. </p>
</dl>
<h2>Operation</h2>
<p><code>pppoe-server</code> listens for incoming PPPoE discovery packets. When a session is established, it spawns a <code>pppd</code> process. The following options are passed to <code>pppd</code>: </p>
<pre>nodetach noaccomp nobsdcom nodeflate nopcomp novj novjccomp
default-asyncmap</pre>
<p>In addition, the local and remote IP address are set based on the <code>-L</code> and <code>-R</code> options. The <code>pty</code> option is supplied along with a <code>pppoe</code> command to initiate the PPPoE session. Finally, additional <code>pppd</code> options can be placed in the file <code>/etc/ppp/pppoe-server-options</code> (which must exist, even if it is just empty!) </p>
<p> Note that <code>pppoe-server</code> is meant mainly for testing PPPoE clients. It is <i>not</i> a high-performance server meant for production use.</p>
<h2>Authors</h2>
<p><code>pppoe-server</code> was written by David F. Skoll &lt;dfs [at] roaringpenguin.com&gt;. </p>
<p> The <code>pppoe</code> home page is <i><a rel="nofollow" href="http://www.roaringpenguin.com/pppoe/">http://www.roaringpenguin.com/pppoe/</a></i>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-pppoe-start/">pppoe-start</a>(8), <a href="/docs/linux/man/8-pppoe-stop/">pppoe-stop</a>(8), <a href="/docs/linux/man/8-pppoe-connect/">pppoe-connect</a>(8), <a href="/docs/linux/man/8-pppd/">pppd</a>(8), <a href="/docs/linux/man/5-pppoe-conf/">pppoe.conf</a>(5), <a href="/docs/linux/man/8-pppoe/">pppoe</a>(8), <a href="/docs/linux/man/8-pppoe-setup/">pppoe-setup</a>(8), <a href="/docs/linux/man/8-pppoe-status/">pppoe-status</a>(8), <a href="/docs/linux/man/8-pppoe-sniff/">pppoe-sniff</a>(8), <a href="/docs/linux/man/8-pppoe-relay/">pppoe-relay</a>(8) </p>
