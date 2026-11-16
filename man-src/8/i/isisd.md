---
title: "isisd(8)"
name: "isisd"
section: "8"
letter: "i"
url: "/docs/linux/man/8-isisd/"
description: "isisd – an IS-IS routing engine for use with Quagga routing software."
---

<p>isisd &#8211; an IS-IS routing engine for use with Quagga routing software.</p>
<h2>Synopsis</h2>
<p><code>isisd</code> [ <code>-dhv</code> ] [ <code>-f</code> <i>config-file</i> ] [ <code>-i</code> <i>pid-file</i> ] [ <code>-P</code> <i>port-number</i> ] [ <code>-A</code> <i>vty-address</i> ] [ <code>-u</code> <i>user</i> ] [ <code>-g</code> <i>group</i> ]</p>
<h2>Description</h2>
<p><code>isisd</code> is a routing component that works with the <code>Quagga</code> routing engine.</p>
<h2>Options</h2>
<p>Options available for the <code>isisd</code> command:</p>
<dl>
<dt><code>-d</code>, <code>&#8211;daemon</code></dt>
<dd>Runs in daemon mode, forking and exiting from tty.</dd>
<dt><code>-f</code>, <code>&#8211;config-file </code><i>config-file</i></dt>
<dd>Specifies the config file to use for startup. If not specified this option will likely default to <i>/usr/local/etc/isisd.conf</i>.</dd>
<dt><code>-g</code>, <code>&#8211;group </code><i>group</i></dt>
<dd>Specify the group to run as. Default is <i>quagga</i>.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>A brief message.</dd>
<dt><code>-i</code>, <code>&#8211;pid_file </code><i>pid-file</i></dt>
<dd>When isisd starts its process identifier is written to <i>pid-file</i>. The init system uses the recorded PID to stop or restart isisd. The likely default is <i>/var/run/isisd.pid</i>.</dd>
<dt><code>-P</code>, <code>&#8211;vty_port </code><i>port-number</i></dt>
<dd>Specify the port that the isisd VTY will listen on. This defaults to 2608, as specified in <i>/etc/services</i>.</dd>
<dt><code>-A</code>, <code>&#8211;vty_addr </code><i>vty-address</i></dt>
<dd>Specify the address that the isisd VTY will listen on. Default is all interfaces.</dd>
<dt><code>-u</code>, <code>&#8211;user </code><i>user</i></dt>
<dd>Specify the user to run as. Default is <i>quagga</i>.</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd>Print the version and exit.</dd></dl>
<h2>Files</h2>
<dl>
<dt><code>/usr/local/sbin/isisd</code></dt>
<dd>The default location of the <code>isisd</code> binary.</dd>
<dt><code>/usr/local/etc/isisd.conf</code></dt>
<dd>The default location of the <code>isisd</code> config file.</dd>
<dt><code>$(PWD)/isisd.log</code></dt>
<dd>If the <code>isisd</code> process is config&#8217;d to output logs to a file, then you will find this file in the directory where you started <code>isisd</code>.</dd></dl>
<h2>Warning</h2>
<p>This man page is intended to be a quick reference for command line options. The definitive document is the Info file <code>Quagga</code>.</p>
<h2>Diagnostics</h2>
<p>The isisd process may log to standard output, to a VTY, to a log file, or through syslog to the system logs. <code>isisd</code> supports many debugging options, see the Info file, or the source for details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-bgpd/">bgpd</a></code>(8), <code><a href="/docs/linux/man/8-ripd/">ripd</a></code>(8), <code><a href="/docs/linux/man/8-ripngd/">ripngd</a></code>(8), <code><a href="/docs/linux/man/8-ospfd/">ospfd</a></code>(8), <code><a href="/docs/linux/man/8-ospf6d/">ospf6d</a></code>(8), <code><a href="/docs/linux/man/8-zebra/">zebra</a></code>(8), <code><a href="/docs/linux/man/1-vtysh/">vtysh</a></code>(1)</p>
<h2>Bugs</h2>
<p><code>isisd</code> is ALPHA quality at the moment and hasn&#8217;t any way ready for production use. </p>
<p> <code>isisd</code> eats bugs for breakfast. If you have food for the maintainers try <code><a rel="nofollow" href="http://bugzilla.quagga.net">http://bugzilla.quagga.net</a></code></p>
<h2>Authors</h2>
<p>See <code><a rel="nofollow" href="http://isisd.sourceforge.net">http://isisd.sourceforge.net</a></code> or the Info file for an accurate list of authors.</p>
