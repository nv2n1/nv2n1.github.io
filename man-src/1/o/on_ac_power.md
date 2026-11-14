---
title: "on_ac_power(1)"
name: "on_ac_power"
section: "1"
letter: "o"
url: "/docs/linux/man/1-on_ac_power/"
description: "on_ac_power – test whether computer is running on AC power"
---

<h2 class="name">NAME</h2>
<p> on_ac_power &#8211; test whether computer is running on AC power </p>
<h2>SYNOPSIS</h2>
<p> <code>on_ac_power</code></p>
<h2>DESCRIPTION</h2>
<p> <code>on_ac_power</code> checks whether the system is running on abundant power (such as AC mains, an USB charger, etc), as opposed to battery power.</p>
<h2>OPTIONS</h2>
<p> None.</p>
<h2>EXIT STATUS</h2>
<pre>
<code>0</code> (true)        System is on mains power
<code>1</code> (false)       System is not on mains power
<code>255</code> (false)     Power status could not be determined
</pre>
<h2>CAVEATS</h2>
<p> The vast majority of desktops and servers have no power sensors, thus they return 255 &quot;unknown&quot;; for most purposes you&#8217;d want to consider this answer to imply mains power &#8212; note that 255 evaluates as false for the shell. </p>
<p> This program currently provides only information known to the kernel; it doesn&#8217;t (yet?) query userspace daemons such as nut which may provide further information.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Steve Dodd &lt;steved [at] loth.demon.co.uk&gt;, was updated by Thomas Hood then by Adam Borowski. </p>
<h2>Index</h2>
