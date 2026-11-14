---
title: "intuitively(8)"
name: "intuitively"
section: "8"
letter: "i"
url: "/docs/linux/man/8-intuitively/"
description: "intuitively – Automagic configuration of network parameters"
---

<p>intuitively &#8211; Automagic configuration of network parameters</p>
<h2>Synopsis</h2>
<p><code>intuitively</code> [ <code> [ -V ] </code> ] [ <code> [ -f ] </code> ] [ <code> [ -v ] [ -q ] </code><i>&#8230;</i> ] [ <code> [ -l </code><i>location</i><code> ] </code> ] [ <code> [ -i </code><i>interface</i><code> ] </code> ] [ <code> [ -c </code><i>config_file</i><code> ] </code> ] [ <code> [ -r </code><i>location_file</i><code> ] </code> ] [ <code> [ -S ] </code> ]</p>
<h2>Description</h2>
<p>Sends out ARP (address resolution protocol) requests and, depending on who answers, it configures the network interface and default route. It also links the files in /etc/intuitively/NETWORK into your root hierarchy</p>
<h2>Options</h2>
<p><code>-f</code>, <code>&#8211;force</code> </p>
<p> force overwriting of non-symlinks when linking the files from /etc/intuitively into the &quot;real hierarchy&quot; <code>-V</code>, <code>&#8211;version</code> </p>
<p> display version and quit <code>-v</code>, <code>&#8211;verbose</code> </p>
<p> be more verbose (may be repeated) <code>-q</code>, <code>&#8211;quiet</code> </p>
<p> be more quiet (may be repeated) <code>-l </code><i>location</i>, <code>&#8211;location=</code><i>location</i> </p>
<p> force selection of location. Useful if, for some reason intuitively fails to detect your location <code>-i </code><i>interface</i>, <code>&#8211;interface=</code><i>interface</i> </p>
<p> force selection of interface. Useful if, for some reason libnet (or intuitively)) fails to detect which interface to use, or if you have more than one interface. <code>-c </code><i>config_file</i>, <code>&#8211;config=</code><i>config_file</i> </p>
<p> use alternate configuration file. <code>-r </code><i>location_file</i>, <code>&#8211;locationfile=</code><i>location_file</i> </p>
<p> write the location found into that file. <code>-S</code>, <code>&#8211;no-scripts</code> </p>
<p> don&#8217;t run the script specified in intuitively.conf. Nice for debugging.</p>
<h2>Exit Status</h2>
<p>intuitively returns a zero exit status if the everything went ok. If something went wrong, it prints an error message and exits with a non-zero exit value. Use one or more <code>-v</code> to try to debug what is going on and send bug reports.</p>
<h2>Author</h2>
<p>Intuitively was originally based on divine, though almost all of the code has been rewritten multiple times. divine is written by Felix von Leitner &lt;&lt;felix [at] fefe.de&gt;&gt;. Intuitively is written by Tollef Fog Heen &lt;&lt;tollef [at] add.no&gt;&gt;</p>
<h2>Bugs</h2>
<p>It is impossible to have netmask = 32, but who wants that anyway? If you find a bug, please report by email to me .&lt;tollef [at] add.no&gt; </p>
