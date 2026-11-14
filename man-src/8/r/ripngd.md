---
title: "ripngd(8)"
name: "ripngd"
section: "8"
letter: "r"
url: "/docs/linux/man/8-ripngd/"
description: "ripngd – a RIPNG routing engine for use with Quagga routing software."
---

<p>ripngd &#8211; a RIPNG routing engine for use with Quagga routing software.</p>
<h2>Synopsis</h2>
<p><code>ripngd</code> [ <code>-dhlrv</code> ] [ <code>-f</code> <i>config-file</i> ] [ <code>-i</code> <i>pid-file</i> ] [ <code>-P</code> <i>port-number</i> ] [ <code>-A</code> <i>vty-address</i> ] [ <code>-u</code> <i>user</i> ] [ <code>-g</code> <i>group</i> ]</p>
<h2>Description</h2>
<p><code>ripngd</code> is a routing component that works with the <code>Quagga</code> routing engine.</p>
<h2>Options</h2>
<p>Options available for the <code>ripngd</code> command:</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;daemon</code></p>
<dd>Runs in daemon mode, forking and exiting from tty.</p>
<dt><code>-f</code>, <code>&#8211;config-file </code><i>config-file</i></p>
<dd>Specifies the config file to use for startup. If not specified this option will likely default to <i>/usr/local/etc/ripngd.conf</i>.</p>
<dt><code>-g</code>, <code>&#8211;group </code><i>group</i></p>
<dd>Specify the group to run as. Default is <i>quagga</i>.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>A brief message.</p>
<dt><code>-i</code>, <code>&#8211;pid_file </code><i>pid-file</i></p>
<dd>When ripngd starts its process identifier is written to <i>pid-file</i>. The init system uses the recorded PID to stop or restart ripngd. The likely default is <i>/var/run/ripngd.pid</i>.</p>
<dt><code>-P</code>, <code>&#8211;vty_port </code><i>port-number</i></p>
<dd>Specify the port that the ripngd VTY will listen on. This defaults to 2603, as specified in <i>/etc/services</i>.</p>
<dt><code>-A</code>, <code>&#8211;vty_addr </code><i>vty-address</i></p>
<dd>Specify the address that the ripngd VTY will listen on. Default is all interfaces.</p>
<dt><code>-u</code>, <code>&#8211;user </code><i>user</i></p>
<dd>Specify the user to run as. Default is <i>quagga</i>.</p>
<dt><code>-r</code>, <code>&#8211;retain</code></p>
<dd>When the program terminates, retain routes added by <code>ripd</code>.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>Print the version and exit.</dl>
<h2>Files</h2>
<dl>
<dt><code>/usr/local/sbin/ripngd</code></p>
<dd>The default location of the <code>ripngd</code> binary.</p>
<dt><code>/usr/local/etc/ripngd.conf</code></p>
<dd>The default location of the <code>ripngd</code> config file.</p>
<dt><code>$(PWD)/ripngd.log</code></p>
<dd>If the <code>ripngd</code> process is config&#8217;d to output logs to a file, then you will find this file in the directory where you started <code>ripngd</code>.</dl>
<h2>Warning</h2>
<p>This man page is intended to be a quick reference for command line options. The definitive document is the Info file <code>Quagga</code>.</p>
<h2>Diagnostics</h2>
<p>The ripngd process may log to standard output, to a VTY, to a log file, or through syslog to the system logs. <code>ripngd</code> supports many debugging options, see the Info file, or the source for details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-bgpd/">bgpd</a></code>(8), <code><a href="/docs/linux/man/8-ripd/">ripd</a></code>(8), <code><a href="/docs/linux/man/8-ospfd/">ospfd</a></code>(8), <code><a href="/docs/linux/man/8-ospf6d/">ospf6d</a></code>(8), <code><a href="/docs/linux/man/8-isisd/">isisd</a></code>(8), <code><a href="/docs/linux/man/8-zebra/">zebra</a></code>(8), <code><a href="/docs/linux/man/1-vtysh/">vtysh</a></code>(1)</p>
<h2>Bugs</h2>
<p><code>ripngd</code> eats bugs for breakfast. If you have food for the maintainers try <code><a rel="nofollow" href="http://bugzilla.quagga.net">http://bugzilla.quagga.net</a></code></p>
<h2>Authors</h2>
<p>See <code><a rel="nofollow" href="http://www.zebra.org">http://www.zebra.org</a></code> and <code><a rel="nofollow" href="http://www.quagga.net">http://www.quagga.net</a></code> or the Info file for an accurate list of authors.</p>
