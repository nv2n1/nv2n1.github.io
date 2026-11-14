---
title: "ifstat(1)"
name: "ifstat"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ifstat/"
description: "ifstat – Report InterFace STATistics"
---

<h2>NAME</h2>
<p> ifstat &#8211; Report InterFace STATistics</p>
<h2>SYNOPSIS</h2>
<p> <code>ifstat</code> [<code>-a</code>] [<code>-l</code>] [<code>-z</code>] [<code>-n</code>] [<code>-v</code>] [<code>-h</code>] [<code>-t</code>] [<code>-i</code> if0,if1,&#8230;] [<code>-d</code> drv[:opt]] [<code>-s</code> [comm@][#]host[/nn]] [<code>-T</code>] [<code>-A</code>] [<code>-w</code>] [<code>-W</code>] [<code>-S</code>] [<code>-b</code>] [<code>-q</code>] [delay[/delay] [count]]</p>
<h2>DESCRIPTION</h2>
<p> Ifstat is a little tool to report interface activity, just like iostat/vmstat do for other system statistics.</p>
<h2>OPTIONS</h2>
<p> <code>ifstat</code> accepts the following options:</p>
<dl>
<dt><code>-l</code></p>
<dd> Enables monitoring of loopback interfaces for which statistics are available. By default, ifstat monitors all non-loopback interfaces that are up.</p>
<dt><code>-a</code></p>
<dd> Enables monitoring of all interfaces found for which statistics are available.</p>
<dt><code>-z</code></p>
<dd> Hides interface which counters are null, eg interfaces that are up but not used.</p>
<dt><code>-i</code></p>
<dd> Specifies the list of interfaces to monitor, separated by commas (if an interface name has a comma, it can be escaped with &#8216;\&#8217;). Multiple instances of the options are added together.</p>
<dt><code>-s</code></p>
<dd> Equivalent to <code>-d snmp:[comm@][#]host[/nn]]</code> to poll a remote host through <font SIZE="-1">SNMP</font>. See below for details.</p>
<dt><code>-h</code></p>
<dd> Displays a short help message.</p>
<dt><code>-n</code></p>
<dd> Turns off displaying the header periodically.</p>
<dt><code>-t</code></p>
<dd> Adds a timestamp at the beginning of each line.</p>
<dt><code>-T</code></p>
<dd> Reports total bandwith for all monitored interfaces.</p>
<dt><code>-A</code></p>
<dd> Disables use of interface indexes: by default, when polling mechanism is index based (snmp, ifmib), ifstat remembers indexes of monitored interfaces to poll only them. However, if interfaces indexes change often (new interfaces added, etc), you might loose some stats, hence this flag. Note that if you ask ifstat to monitor a non existent interface, it will poll all interfaces until it finds the requested one (regardless of this flag) so you can poll for an interface that goes up and down.</p>
<dt><code>-w</code></p>
<dd> Uses fixed width columns, instead of enlarging them if needed for interfaces names to fit.</p>
<dt><code>-W</code></p>
<dd> Wrap lines that are larger than the terminal width (implies -w). Wrapped lines are prefixed with a cycling letter to ease reading.</p>
<dt><code>-S</code></p>
<dd> Keep stats updated on the same line if possible (no scrolling nor wrapping).</p>
<dt><code>-b</code></p>
<dd> Reports bandwith in kbits/sec instead of kbytes/sec.</p>
<dt><code>-q</code></p>
<dd> Quiet mode, warnings are not printed.</p>
<dt><code>-v</code></p>
<dd> Displays version and the compiled-in drivers.</p>
<dt><code>-d</code></p>
<dd> Specifies a driver to use to gather stats and an eventual option for this driver separated of the driver name by a colon. If this is not specified, ifstat uses the first driver compiled in, with no options. </p>
<p> The following drivers are available (depending on the operating system and compile-time options, not all of them might be present):</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>proc</code></p>
<dd> This driver gets statistics from Linux&#8217;s /proc/net/dev file. An alternate file name to get stats from can be passed as the option.</p>
<dt><code>ifmib</code></p>
<dd> This driver gets statistics from FreeBSD&#8217;s ifmib sysctl. It doesn&#8217;t accept any options.</p>
<dt><code>kstat</code></p>
<dd> This driver gets statistics from Solaris kstat interface. It doesn&#8217;t accept any options.</p>
<dt><code>ifdata</code></p>
<dd> This driver gets statistics using <font SIZE="-1">SIOCGIFDATA</font> ioctl under <font SIZE="-1">IRIX</font> and OpenBSD (different semantics). It doesn&#8217;t accept any options.</p>
<dt><code>route</code></p>
<dd> This driver gets statistics using routing sysctl on <font SIZE="-1">BSD</font> based systems. It doesn&#8217;t accept any options.</p>
<dt><code>kvm</code></p>
<dd> This driver gets statistics by reading the kernel live structures. It accepts an option specifying which files/devices to use in the following format : [execfile][,[corefile][,swapfile]] (see <i><a href="/docs/linux/man/3-kvm_open/">kvm_open</a></i>(3) for details on those fields). If a null string is passed for a parameter, the system default will be used for it. </p>
<p> Note that for this driver to work, ifstat needs to have read access to the system memory device. This is usually done by running it as root, or by installing setgid mem or kmem. ifstat will <font SIZE="-1">NOT</font> install setgid by default; It is up to you to decide if you trust it.</p>
<dt><code>dlpi</code></p>
<dd> This driver gets statistics using the <font SIZE="-1">DLPI</font> streams interface available on <font SIZE="-1">HP-UX</font>. An alternate device to query statistics from can be passed as the option (default is /dev/dlpi).</p>
<dt><code>win32</code></p>
<dd> This driver gets statistics using the GetIfTable interface available on Win32 systems. It doesn&#8217;t accept any options.</p>
<dt><code>snmp</code></p>
<dd> This driver gets statistics through <font SIZE="-1">SNMP</font>. The option, in the form [comm@][#]host[/nn]], specifies the host and eventual community to poll. Default community is public, but can be changed by prepending &#8220;comm@&#8221; to the hostname. If host starts by a #, interface names are generated from their index as `ifNN&#8217; (this is a workaround for some equipments that give all interfaces the same description). Default host is localhost, and this will be used by default if snmp is the only available driver. </p>
<p> The driver will try to poll several interfaces at once by grouping requests in <font SIZE="-1">SNMP</font> packets. By default interfaces will be polled by group of 8. If this doesn&#8217;t work well with your equipments, you can lower that number by suffixing the hostname with /nn, where nn is the number of interfaces to poll at once. You can also increase the number if you want to poll a large number of interfaces efficiently and if your server supports it.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>delay</code></p>
<dd> <code>delay</code> is the delay between updates in seconds, which defaults to 1. A decimal number can be specified for intervals shorter than a second. (minimum 0.1) </p>
<p> A second delay can also be specified (separated from the first one by a &#8216;/&#8217;). In that case the first delay will be used for the first poll after start and the second one will be used for all following polls (This can be used to have a &#8220;fast&#8221; start when running for a long while with a big delay).</p>
<dt><code>count</code></p>
<dd> <code>count</code> is the number of updates before stopping. If not specified, it is unlimited.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-vmstat/">vmstat</a></i>(1), <i><a href="/docs/linux/man/1-iostat/">iostat</a></i>(1)</p>
<h2>AUTHOR</h2>
<p> Gaël Roualland, &lt;gael.roualland [at] dial.oleane.com&gt; </p>
<h2>Index</h2>
