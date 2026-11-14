---
title: "latencytop(8)"
name: "latencytop"
section: "8"
letter: "l"
url: "/docs/linux/man/8-latencytop/"
description: "latencytop – a tool for developers to visualize system latencies"
---

<p>latencytop &#8211; a tool for developers to visualize system latencies</p>
<h2>Synopsis</h2>
<p><code>latencytop</code> [<i>&#8211;unknown</i>]<i> </i>[<i>processes</i>&#8230;<i>]</i></p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>latencytop</code> command. <code>latencytop</code> is a Linux* tool for software developers (both kernel and userspace), aimed at identifying where in the system latency is happening, and what kind of operation/action is causing the latency to happen so that the code can be changed to avoid the worst latency hiccups. <code>LatencyTOP</code> focuses on the cases where the applications want to run and execute useful code, but there&#8217;s some resource that&#8217;s not currently available (and the kernel then blocks the process). This is done both on a system level and on a per process level, so that you can see what&#8217;s happening to the system, and which process is suffering and/or causing the delays. You can walk the processes by using the cursor keys. If you press <code>s</code> followed by a letter, then only active processes starting with that lettter are displayed and walked. If you press <code>s</code> followed by <code>0</code> then that filter is reset. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-powertop/">powertop</a></code>(1)<br />
 The program is more fully described at <a rel="nofollow" href="http://www.latencytop.org">http://www.latencytop.org</a></p>
<h2>Author</h2>
<p>latencytop was written by Arjan van de Ven &lt;arjan [at] linux.intel.com&gt;. </p>
<p> This manual page was written by Giacomo Catenazzi &lt;cate [at] debian.org&gt;, for the Debian project (but may be used by others).</p>
