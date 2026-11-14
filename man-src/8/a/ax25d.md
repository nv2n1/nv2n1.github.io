---
title: "ax25d(8)"
name: "ax25d"
section: "8"
letter: "a"
url: "/docs/linux/man/8-ax25d/"
description: "ax25d – General purpose AX.25, NET/ROM and Rose daemon"
---

<p>ax25d &#8211; General purpose AX.25, NET/ROM and Rose daemon</p>
<h2>Synopsis</h2>
<p><code>ax25d [-v] [-c altconffile] [-l]</code></p>
<h2>Description</h2>
<p><code>Ax25d</code> is a general purpose server daemon that listens on a number of AX.25, NET/ROM and Rose ports and offers different services depending upon port, callsign and other parameters. <code>Ax25d</code> is driven by a complex configuration file, a full description of which may be found in another manual page. </p>
<p> <code>AX25d</code> has the facility to log information about incoming connections to the system log file. By default no logging is done. When <code>ax25d</code> is running, and a change in the configuration file is made, <code>ax25d</code> can be forced to re-read its configuration file by sending it a SIGHUP.</p>
<h2>Options</h2>
<dl>
<dt><code>-c altconffile</code></p>
<dd>Specifies an alternate configuration file name.</p>
<dt><code>-l</code></p>
<dd>Specifies that messages should be logged into the system log file. By default no messages are logged.</p>
<dt><code>-v</code></p>
<dd>Display the version.</dl>
<h2>Files</h2>
<p>/etc/ax25/ax25d.conf</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-kill/">kill</a></code>(1), <code><a href="/docs/linux/man/4-ax25/">ax25</a></code>(4), <code><a href="/docs/linux/man/4-netrom/">netrom</a></code>(4), <code><a href="/docs/linux/man/4-rose/">rose</a></code>(4), <code><a href="/docs/linux/man/5-ax25d-conf/">ax25d.conf</a></code>(5).</p>
<h2>Author</h2>
<p>Darryl Miles G7LED &lt;dlm [at] frink.demon.co.uk&gt;<br />
 Jonathan Naylor G4KLX &lt;g4klx [at] g4klx.demon.co.uk&gt;</p>
