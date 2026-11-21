---

title: "dahdi_scan(8)"
name: "dahdi_scan"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dahdi_scan/"
description: "dahdi_scan — Print Configuration of DAHDI Spans"
---

<p> dahdi_scan --- Print Configuration of DAHDI Spans  </p>

<p> <code>dahdi_scan</code> <i>[spans]</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>dahdi_scan</code> prints information about DAHDI spans in the system. For analog spans it also provides a list of channels. </p>
<p>By default it prints information about all the spans in the system. However if parameters are provided, they will be considered to be a list of span numbers and information will be printed for them. </p>
<p>Output is printed to the standard output. The format is that of an Asterisk configuration file (similar to a &quot;ini&quot; configuration file), where the name of the section is the number of the span. Note that the specifically for analog spans some keys may appear more than once, and hence you can not use a parser for an &quot;ini&quot; format and assume you have a dictionary. </p>
<h2>EXAMPLES</h2>
<p> Printing information for spans 1, 2 and 4: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>dahdi_scan 1 2 4 </p>
<p>And to print all the spans: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>dahdi_scan </p>
<p>Information about a certain analog span: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>[5] <br />
&nbsp;<wbr>&nbsp;<wbr>active=yes <br />
&nbsp;<wbr>&nbsp;<wbr>alarms=OK <br />
&nbsp;<wbr>&nbsp;<wbr>description=Xorcom XPD&nbsp;<wbr>#00/10: FXS <br />
&nbsp;<wbr>&nbsp;<wbr>name=XBUS-00/XPD-10 <br />
&nbsp;<wbr>&nbsp;<wbr>manufacturer=Xorcom Inc. <br />
&nbsp;<wbr>&nbsp;<wbr>devicetype=Astribank: Unit 1 Subunit 0: FXS <br />
&nbsp;<wbr>&nbsp;<wbr>location=usb-0000:00:03.3-4 <br />
&nbsp;<wbr>&nbsp;<wbr>basechan=125 <br />
&nbsp;<wbr>&nbsp;<wbr>totchans=8 <br />
&nbsp;<wbr>&nbsp;<wbr>irq=0 <br />
&nbsp;<wbr>&nbsp;<wbr>type=analog <br />
&nbsp;<wbr>&nbsp;<wbr>port=125,FXS <br />
&nbsp;<wbr>&nbsp;<wbr>port=126,FXS <br />
&nbsp;<wbr>&nbsp;<wbr>port=127,FXS <br />
&nbsp;<wbr>&nbsp;<wbr>port=128,FXS <br />
&nbsp;<wbr>&nbsp;<wbr>port=129,FXS <br />
&nbsp;<wbr>&nbsp;<wbr>port=130,FXS <br />
&nbsp;<wbr>&nbsp;<wbr>port=131,FXS <br />
&nbsp;<wbr>&nbsp;<wbr>port=132,FXS </p>
<p>And an example of a digital span: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>[1] <br />
&nbsp;<wbr>&nbsp;<wbr>active=yes <br />
&nbsp;<wbr>&nbsp;<wbr>alarms=RED <br />
&nbsp;<wbr>&nbsp;<wbr>description=T2XXP&nbsp;<wbr>(PCI)&nbsp;<wbr>Card 0 Span 1 <br />
&nbsp;<wbr>&nbsp;<wbr>name=TE2/0/1 <br />
&nbsp;<wbr>&nbsp;<wbr>manufacturer=Digium <br />
&nbsp;<wbr>&nbsp;<wbr>devicetype=Wildcard TE205P&nbsp;<wbr>(4th Gen) <br />
&nbsp;<wbr>&nbsp;<wbr>location=Board ID Switch 0 <br />
&nbsp;<wbr>&nbsp;<wbr>basechan=1 <br />
&nbsp;<wbr>&nbsp;<wbr>totchans=24 <br />
&nbsp;<wbr>&nbsp;<wbr>irq=193 <br />
&nbsp;<wbr>&nbsp;<wbr>type=digital-T1 <br />
&nbsp;<wbr>&nbsp;<wbr>syncsrc=0 <br />
&nbsp;<wbr>&nbsp;<wbr>lbo=0 db&nbsp;<wbr>(CSU)/0-133 feet&nbsp;<wbr>(DSX-1) <br />
&nbsp;<wbr>&nbsp;<wbr>coding_opts=B8ZS,AMI <br />
&nbsp;<wbr>&nbsp;<wbr>framing_opts=ESF,D4 <br />
&nbsp;<wbr>&nbsp;<wbr>coding=B8ZS <br />
&nbsp;<wbr>&nbsp;<wbr>framing=ESF </p>
<p>The &quot;type&quot; field may contain: &quot;analog&quot;, &quot;digital-T1&quot;, &quot;digital-E1&quot;, &quot;digital-J1&quot; or &quot;digital-BRI&quot;. </p>
<h2>FILES</h2>
<p> Requires read access to /dev/zap/ctl . </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-dahdi_cfg/">dahdi_cfg</a>(8), <a href="/docs/linux/man/8-asterisk/">asterisk</a>(8). </p>
<h2>BUGS</h2>
<p> The program still does not do everything described in the man page. </p>
<p>It also assumes that spans don&#8217;t skip channel numbers, and that their channel numbers are &quot;running&quot;. This is anyway almost always the case. And always the case in a normal boot process. </p>
<h2>AUTHOR</h2>
<p>This manual page was written by Tzafrir Cohen &lt;tzafrir.cohen [at] xorcom.com&gt; Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation. <br />
&nbsp;<wbr> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
