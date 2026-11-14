---
title: "racolor-conf(5)"
name: "racolor-conf"
section: "5"
letter: "r"
url: "/docs/linux/man/5-racolor-conf/"
description: "racolor.conf – racolor resource file."
---

<p><code>racolor.conf</code> &#8211; <code>racolor</code> resource file.</p>
<h2>Synopsis</h2>
<p><code>racolor.conf</code></p>
<h2>Description</h2>
<p>This configuration is a color configuration file for ratop.1. It is modeled after a <a href="/docs/linux/man/1-ralabel/">ralabel</a>(1) configuration file. This configuration would be referenced in a <code>ratop.1</code> <code>rarc.5</code> configuration file, using the RA_COLOR_CONFIG variable. The concept is to provide a number of painting strategies for any or all fields in an argus record. This allows the user to specify the order of the painting, hopefully to get a useful end result. The method used is flow filter based field painting, which uses the standard flow filter strategies to provide a general purpose coloring scheme. The concept is similar to racluster()&#8217;s fall through matching scheme. Fall through the list of filters, if it matches, use the color specification to paint specific fields in the record. If you want to continue through the list, once there is a match, add a &quot;cont&quot; to the end of the matching rule. </p>
<pre>The format is:
 filter=&quot;ra filter&quot; color=&quot;field[,field,...]:COLOR[+ATTRIBUTE]&quot; [cont]
 filter can be any working ra flow record filter, contained in double quotes
 color is composed of a comma separated list of fields, that will be painted
 using the ncurses supported COLOR(s) and an optional ATTRIBUTE(s).
 each line can be followed with an optional &quot;cont&quot;inue label, to indicate
 that it should not stop with this match, but keep going down the list.
A working example color specification is:
 filter=&quot;udp&quot; color=&quot;proto:VIOLET&quot; cont
 filter=&quot;tcp&quot; color=&quot;saddr,daddr,dir,sport,dport,proto:WHITE&quot; cont
 filter=&quot;tcp and dst port http&quot; color=&quot;dport:GREEN&quot; cont
 filter=&quot;tcp&quot; color=&quot;sport:BLUE+DIM&quot; cont
 filter=&quot;dst port domain&quot; color=&quot;dport:CYAN+DIM&quot; cont
 filter=&quot;dst port imaps&quot; color=&quot;dport:MAGENTA+DIM&quot; cont
 filter=&quot;src pkts gt 50&quot; color=&quot;spkts,dpkts,sbytes,dbytes:RED+BLINK&quot;
 filter=&quot;src co CN&quot; color=&quot;all:RED+BLINK&quot; </pre>
<h2>Copyright</h2>
<p>Copyright (c) 2000-2016 QoSient. All rights reserved.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ratop/">ratop</a></code>(1) </p>
