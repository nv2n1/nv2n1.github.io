---
title: "dahdi_scan(8)"
name: "dahdi_scan"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dahdi_scan/"
description: "dahdi_scan — Print Configuration of DAHDI Spans"
---

<p>dahdi_scan &#8212; Print Configuration of DAHDI Spans</p>
<h2>Synopsis</h2>
<p><code>dahdi_scan</code> <i>[spans]</i> </p>
<h2>Description</h2>
<p><code>dahdi_scan</code> prints information about DAHDI spans in the system. For analog spans it also provides a list of channels. By default it prints information about all the spans in the system. However if parameters are provided, they will be considered to be a list of span numbers and information will be printed for them. Output is printed to the standard output. The format is that of an Asterisk configuration file (similar to a &quot;ini&quot; configuration file), where the name of the section is the number of the span. Note that the specifically for analog spans some keys may appear more than once, and hence you can not use a parser for an &quot;ini&quot; format and assume you have a dictionary. </p>
<h2>Examples</h2>
<p>Printing information for spans 1, 2 and 4:<br />
&nbsp;<wbr>&nbsp;<wbr>dahdi_scan 1 2 4 And to print all the spans:<br />
&nbsp;<wbr>&nbsp;<wbr>dahdi_scan Information about a certain analog span:  And an example of a digital span: </p>
<pre><code>[1]
active=yes
alarms=RED
description=T2XXP (PCI) Card 0 Span 1
name=TE2/0/1
manufacturer=Digium
devicetype=Wildcard TE205P (4th Gen)
location=Board ID Switch 0
basechan=1
totchans=24
irq=193
type=digital-T1
syncsrc=0
lbo=0 db (CSU)/0-133 feet (DSX-1)
coding_opts=B8ZS,AMI
framing_opts=ESF,D4
coding=B8ZS
framing=ESF</code></pre>
<p> The &quot;type&quot; field may contain: &quot;analog&quot;, &quot;digital-T1&quot;, &quot;digital-E1&quot;, &quot;digital-J1&quot; or &quot;digital-BRI&quot;. </p>
<h2>Files</h2>
<p>Requires read access to /dev/zap/ctl .</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dahdi_cfg/">dahdi_cfg</a>(8), <a href="/docs/linux/man/8-asterisk/">asterisk</a>(8). </p>
<h2>Bugs</h2>
<p>The program still does not do everything described in the man page. It also assumes that spans don&#8217;t skip channel numbers, and that their channel numbers are &quot;running&quot;. This is anyway almost always the case. And always the case in a normal boot process. </p>
<h2>Author</h2>
<p>This manual page was written by Tzafrir Cohen &lt;tzafrir.cohen [at] xorcom.com&gt; Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation.<br />
&nbsp;<wbr> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
