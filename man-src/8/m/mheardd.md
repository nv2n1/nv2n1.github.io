---
title: "mheardd(8)"
name: "mheardd"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mheardd/"
description: "mheardd – collect information about packet activity"
---

<p>mheardd &#8211; collect information about packet activity</p>
<h2>Synopsis</h2>
<p><code>mheardd [-f] [-l] [-n number] [-p [!]port1[,port2,..]] [-v]</code></p>
<h2>Description</h2>
<p><code>Mheardd</code> is a daemon that collects the statistics about the activity on all the AX.25 channels that are configured. The list generated is available for viewing by the <code><a href="/docs/linux/man/1-mheard/">mheard</a></code>(1) program. The information collected is a superset of the information normally collected by similar mheard programs and this is reflected in the options available for the viewing program. Logging to the system log file may be enabled which will enable monitoring of pathalogical conditions, for example invalid frame types and invalid/unknown protocol IDs.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></p>
<dd>Deletes the existing mheard logging file at program startup, this is not the default.</p>
<dt><code>-l</code></p>
<dd>Enables logging to the system log file. The default is off.</p>
<dt><code>-n number</code></p>
<dd>Sets the number of entries in the activity list file, the default is 100. The minimum value allowed is 10 and the maximum is 1000.</p>
<dt><code>-p [!]port1[,port2,..]</code></p>
<dd>With -p, you instruct mheardd to only listen on specified ax25 ports. You may give more ports, seperated by &#8216;,&#8217;. If you introduce the port(s) by a leading &#8216;!&#8217;, then mheardd will listen on all ports except those you specified.</p>
<dt><code>-v</code></p>
<dd>Display the version.</dl>
<h2>Files</h2>
<p>/var/ax25/mheard/mheard.dat<br />
 /etc/ax25/axports</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-mheard/">mheard</a></code>(1), <code><a href="/docs/linux/man/4-ax25/">ax25</a></code>(4).</p>
<h2>Author</h2>
<p>Jonathan Naylor G4KLX &lt;g4klx [at] g4klx.demon.co.uk&gt;</p>
