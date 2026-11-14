---
title: "zebra(8)"
name: "zebra"
section: "8"
letter: "z"
url: "/docs/linux/man/8-zebra/"
description: "zebra – a routing manager for use with associated Quagga components."
---

<p>zebra &#8211; a routing manager for use with associated Quagga components.</p>
<h2>Synopsis</h2>
<p><code>zebra</code> [ <code>-bdhklrv</code> ] [ <code>-f</code> <i>config-file</i> ] [ <code>-i</code> <i>pid-file</i> ] [ <code>-P</code> <i>port-number</i> ] [ <code>-A</code> <i>vty-address</i> ] [ <code>-u</code> <i>user</i> ] [ <code>-g</code> <i>group</i> ]</p>
<h2>Description</h2>
<p><code>zebra </code> is a routing manager that implements the <code>zebra</code> route engine. <code>zebra </code> supports RIPv1, RIPv2, RIPng, OSPF, OSPF6, IS-IS, BGP4+, and BGP4-.</p>
<h2>Options</h2>
<p>Options available for the <code>zebra</code> command:</p>
<dl>
<dt><code>-b</code>, <code>&#8211;batch</code></p>
<dd>Runs in batch mode, <code>zebra</code> parses its config and exits.</p>
<dt><code>-d</code>, <code>&#8211;daemon</code></p>
<dd>Runs in daemon mode, forking and exiting from tty.</p>
<dt><code>-f</code>, <code>&#8211;config-file </code><i>config-file</i></p>
<dd>Specifies the config file to use for startup. If not specified this option will likely default to <i>/usr/local/etc/zebra.conf</i>.</p>
<dt><code>-g</code>, <code>&#8211;group </code><i>group</i></p>
<dd>Specify the group to run as. Default is <i>quagga</i>.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>A brief message.</p>
<dt><code>-i</code>, <code>&#8211;pid_file </code><i>pid-file</i></p>
<dd>When zebra starts its process identifier is written to <i>pid-file</i>. The init system uses the recorded PID to stop or restart zebra. The likely default is <i>/var/run/zebra.pid</i>.</p>
<dt><code>-k</code>, <code>&#8211;keep_kernel</code></p>
<dd>On startup, don&#8217;t delete self inserted routes.</p>
<dt><code>-P</code>, <code>&#8211;vty_port </code><i>port-number</i></p>
<dd>Specify the port that the zebra VTY will listen on. This defaults to 2601, as specified in <i>/etc/services</i>.</p>
<dt><code>-A</code>, <code>&#8211;vty_addr </code><i>vty-address</i></p>
<dd>Specify the address that the zebra VTY will listen on. Default is all interfaces.</p>
<dt><code>-u</code>, <code>&#8211;user </code><i>user</i></p>
<dd>Specify the user to run as. Default is <i>quagga</i>.</p>
<dt><code>-r</code>, <code>&#8211;retain</code></p>
<dd>When the program terminates, retain routes added by <code>zebra</code>.</p>
<dt><code>-s</code>, <code>&#8211;nl-bufsize </code><i>netlink-buffer-size</i></p>
<dd>Set netlink receive buffer size. There are cases where zebra daemon can&#8217;t handle flood of netlink messages from kernel. If you ever see &quot;recvmsg overrun&quot; messages in zebra log, you are in trouble. </p>
<p> Solution is to increase receive buffer of netlink socket. Note that kernel doesn&#8217;t allow to increase it over maximum value defined in <i>/proc/sys/net/core/rmem_max</i>. If you want to do it, you have to increase maximum before starting zebra. </p>
<p> Note that this affects Linux only.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>Print the version and exit.</dl>
<h2>Files</h2>
<dl>
<dt><code>/usr/local/sbin/zebra</code></p>
<dd>The default location of the <code>zebra</code> binary.</p>
<dt><code>/usr/local/etc/zebra.conf</code></p>
<dd>The default location of the <code>zebra</code> config file.</p>
<dt><code>$(PWD)/zebra.log</code></p>
<dd>If the <code>zebra</code> process is config&#8217;d to output logs to a file, then you will find this file in the directory where you started <code>zebra</code>.</dl>
<h2>Warning</h2>
<p>This man page is intended to be a quick reference for command line options. The definitive document is the Info file <code>Quagga</code>.</p>
<h2>Diagnostics</h2>
<p>The zebra process may log to standard output, to a VTY, to a log file, or through syslog to the system logs. <code>zebra</code> supports many debugging options, see the Info file, or the source for details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-bgpd/">bgpd</a></code>(8), <code><a href="/docs/linux/man/8-ripd/">ripd</a></code>(8), <code><a href="/docs/linux/man/8-ripngd/">ripngd</a></code>(8), <code><a href="/docs/linux/man/8-ospfd/">ospfd</a></code>(8), <code><a href="/docs/linux/man/8-ospf6d/">ospf6d</a></code>(8), <code><a href="/docs/linux/man/8-isisd/">isisd</a></code>(8), <code><a href="/docs/linux/man/1-vtysh/">vtysh</a></code>(1)</p>
<h2>Bugs</h2>
<p><code>zebra</code> eats bugs for breakfast. If you have food for the maintainers try <code><a rel="nofollow" href="http://bugzilla.quagga.net">http://bugzilla.quagga.net</a></code></p>
<h2>Authors</h2>
<p>See <code><a rel="nofollow" href="http://www.zebra.org">http://www.zebra.org</a></code> and <code><a rel="nofollow" href="http://www.quagga.net">http://www.quagga.net</a></code> or the Info file for an accurate list of authors.</p>
