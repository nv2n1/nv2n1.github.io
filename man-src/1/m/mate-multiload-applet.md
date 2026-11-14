---
title: "mate-multiload-applet(1)"
name: "mate-multiload-applet"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mate-multiload-applet/"
description: "mate-multiload-applet – Multiload (cpu, load average, memory, net, swap) applet for the MATE panel."
---

<h2>NAME</h2>
<p> mate-multiload-applet &#8211; Multiload (cpu, load average, memory, net, swap) applet for the MATE panel.</p>
<h2>SYNOPSIS</h2>
<p> <code>mate-multiload-applet</code> [ <code>&#8211;activate-goad-server</code><i>[=GOAD_ID]</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>mate-multiload-applet</code> Contains 5 applets. </p>
<p> CPU Load Applet. To add this applet to a Panel, right-click on the Panel and choose Applets-&gt;Monitors-&gt;CPULoad </p>
<p> Load Average Applet. To add this applet to a Panel, right-click on the Panel and choose Applets-&gt;Monitors-&gt;Load Average </p>
<p> Memory Applet. To add this applet to a Panel, right-click on the Panel and choose Applets-&gt;Monitors-&gt;MemLoad </p>
<p> Net Applet. To add this applet to a Panel, right-click on the Panel and choose Applets-&gt;Monitors-&gt;NetLoad </p>
<p> Swap Applet. To add this applet to a Panel, right-click on the Panel and choose Applets-&gt;Monitors-&gt;SwapLoad</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;activate-goad-server</code></p>
<dd> (Internal use only) GOAD server ID to activate </p>
<p> GOAD_ID may be: </p>
<p> <code>multiload_cpuload_applet </code>start the cpu applet. </p>
<p> <code>multiload_loadavg_applet </code>start the load average applet. </p>
<p> <code>multiload_memload_applet </code>start the memory applet. </p>
<p> <code>multiload_netload_applet </code>start the net applet. </p>
<p> <code>multiload_swapload_applet </code>start the swap applet.</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Christian Marillat &lt;marillat [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
