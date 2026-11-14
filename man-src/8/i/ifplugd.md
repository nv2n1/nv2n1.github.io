---
title: "ifplugd(8)"
name: "ifplugd"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ifplugd/"
description: "ifplugd – A link detection daemon for ethernet devices"
---

<p>ifplugd &#8211; A link detection daemon for ethernet devices</p>
<h2>Synopsis</h2>
<p><code>ifplugd [</code><i>options</i><code>] </code></p>
<h2>Description</h2>
<p>ifplugd is a daemon which will automatically configure your ethernet device when a cable is plugged in and automatically unconfigure it if the cable is pulled. This is useful on laptops with on-board network adapters, since it will only configure the interface when a cable is really connected. </p>
<p> It uses your distribution&#8217;s native ifup/ifdown programs, but can be configured to do anything you wish when the state of the interface changes. It may ignore short unplugged whiles (<code>-d</code> option) or plugged whiles (<code>-u</code> option). </p>
<p> ifplugd may be used in &quot;compatibility mode&quot; by specifying -F on the command line. Than ifplugd will treat network drivers which do not support link beat querying as always online.</p>
<h2>Options</h2>
<dl>
<dt><code>-a | &#8211;no-auto</code></p>
<dd>Do not enable interface automatically (default: off)</p>
<dt><code>-n | &#8211;no-daemon</code></p>
<dd>Do not daemonize (for debugging) (default: off)</p>
<dt><code>-s | &#8211;no-syslog</code></p>
<dd>Do not use syslog, use stdout instead (for debugging) (default: off).</p>
<dt><code>-b | &#8211;no-beep</code></p>
<dd>Do not beep (off)</p>
<dt><code>-f | &#8211;ignore-fail</code></p>
<dd>Ignore detection failure, retry instead. Failure is treated as &quot;no link&quot;. (default: off)</p>
<dt><code>-F | &#8211;ignore-fail-positive</code></p>
<dd>Ignore detection failure, retry instead. Failure is treated as &quot;link detected&quot;. (default: off)</p>
<dt><code>-i | &#8211;iface=</code> <i>IFACE</i></p>
<dd>Specify ethernet interface (default: eth0)</p>
<dt><code>-r | &#8211;run=</code> <i>EXEC</i></p>
<dd>Specify program to execute when link status changes (default: <i>/etc/ifplugd/ifplugd.action</i>)</p>
<dt><code>-I | &#8211;ignore-retval</code></p>
<dd>Don&#8217;t exit on nonzero return value of program executed on link change. (default: off)</p>
<dt><code>-t | &#8211;poll-time=</code> <i>SECS</i></p>
<dd>Specify poll time in seconds (default: 1)</p>
<dt><code>-u | &#8211;delay-up=</code> <i>SECS</i></p>
<dd>Specify delay for configuring interface (default: 0)</p>
<dt><code>-d | &#8211;delay-down=</code> <i>SECS</i></p>
<dd>Specify delay for deconfiguring interface (default: 5)</p>
<dt><code>-m | &#8211;api-mode=</code> <i>MODE</i></p>
<dd>Force a specific link beat detection ioctl() API. Possible values are auto, iff, wlan, ethtool, mii, and priv for automatic detection, interface flag (IFF_RUNNING), wireless extension, SIOCETHTOOL, SIOCGMIIREG resp. SIOCPRIV. Only the first character of the argument is relevant, case insensitive. (default: auto)</p>
<dt><code>-p | &#8211;no-startup</code></p>
<dd>Don&#8217;t call the script to bring up network on deamon start (default: off)</p>
<dt><code>-q | &#8211;no-shutdown</code></p>
<dd>Don&#8217;t call the script for network shutdown on deamon quit (default: off)</p>
<dt><code>-w | &#8211;wait-on-fork</code></p>
<dd>When daemonizing, wait until the background process finished with the initial link beat detection. When this is enabled, the parent process will return the link status on exit. 1 means link beat detected, 2 stands for link beat not detected, everything else is an error.</p>
<dt><code>-W | &#8211;wait-on-kill</code></p>
<dd>When killing a running daemon (with -k) wait until the daemon died.</p>
<dt><code>-x | &#8211;extra-arg=</code> <i>ARG</i></p>
<dd>Specify an extra argument to be passed to the action script.</p>
<dt><code>-M | &#8211;monitor</code></p>
<dd>Don&#8217;t fail when the network interface is not available, instead use NETLINK to monitor device avaibility. The is useful for PCMCIA devices and similar.</p>
<dt><code>-h | &#8211;help</code></p>
<dd>Show help</p>
<dt><code>-k | &#8211;kill</code></p>
<dd>Kill a running daemon (Specify -i to select the daemon instance to kill)</p>
<dt><code>-c | &#8211;check-running</code></p>
<dd>Check if a daemon is running for a given network interface. Sets the return value to 0 if a daemon is already running or to 255 if not.</p>
<dt><code>-v | &#8211;version</code></p>
<dd>Show version</p>
<dt><code>-S | &#8211;supend</code></p>
<dd>Suspend a running daemon. The daemon will no longer check the link status until it is resumed (-R) again. (Specify -i to select the daemon instance to suspend.)</p>
<dt><code>-R | &#8211;resume</code></p>
<dd>Resume a suspended daemon. (Specify -i to select the daemon instance to resume.)</p>
<dt><code>-z | &#8211;info</code></p>
<dd>Request that a running daemon shall write its status information to syslog. (Specify -i to select the daemon instance to send the request to.)</dl>
<h2>Files</h2>
<p><i>/etc/ifplugd/ifplugd.conf</i>: this file is sourced by the init script <i>/etc/init.d/ifplugd</i> and contains the interface to be monitored and the options to be used. </p>
<p> <i>/etc/ifplugd/ifplugd.action</i>: this is the script which will be called by the daemon whenever the state of the interface changes. It takes two areguments: the first is the interface name (eg. eth0), the second either &quot;up&quot; or &quot;down&quot;. </p>
<p> <i>/var/run/ifplugd.&lt;iface&gt;.pid</i>: the pid file for ifplugd.</p>
<h2>Environment</h2>
<p>The action script will be called with two environment variables set: </p>
<p> <i>IFPLUGD_PREVIOUS</i> The previous link status. Either &quot;up&quot;, &quot;down&quot;, &quot;error&quot; or &quot;disabled&quot;. The former values should be obvious, the latter is set on daemon startup. </p>
<p> <i>IFPLUGD_CURRENT</i> The current link status. See above for possible values.</p>
<h2>Signals</h2>
<p><i>SIGINT, SIGTERM</i> ifplugd will quit, possibly running the shutdown script. This is issued by passing -k to ifplugd. </p>
<p> <i>SIGQUIT</i> ifplugd will quit, the shutdown script is never run. </p>
<p> <i>SIGHUP</i> ifplugd will write its status information to syslog. This is issued by -z. </p>
<p> <i>SIGUSR1</i> ifplugd will go to suspend mode. (-S) </p>
<p> <i>SIGUSR2</i> ifplugd will resume from suspend mode. (-R)</p>
<h2>Author</h2>
<p>ifplugd was written by Lennart Poettering &lt;mzvscyhtq (at) 0pointer (dot) de&gt;. ifplugd is available at <code><a rel="nofollow" href="http://0pointer.de/lennart/projects/ifplugd/">http://0pointer.de/lennart/projects/ifplugd/</a></code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-ifplugd-conf/">ifplugd.conf</a>(5)</code>, <code><a href="/docs/linux/man/8-ifup/">ifup</a>(8)</code>, <code><a href="/docs/linux/man/5-interfaces/">interfaces</a>(5)</code>, <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a>(8)</code>, <code><a href="/docs/linux/man/8-ifplugstatus/">ifplugstatus</a>(8)</code></p>
<h2>Comments</h2>
<p>This man page was written using <code><a href="/docs/linux/man/1-xmltoman/">xmltoman</a>(1)</code> by Oliver Kurth.</p>
