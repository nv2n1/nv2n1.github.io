---
title: "avmcapictrl(8)"
name: "avmcapictrl"
section: "8"
letter: "a"
url: "/docs/linux/man/8-avmcapictrl/"
description: "avmcapictrl – Add, reset or remove active AVM cards and load firmware"
---

<p>avmcapictrl &#8211; Add, reset or remove active AVM cards and load firmware</p>
<h2>Synopsis</h2>
<p>avmcapictrl add &lt;portbase&gt; &lt;irq&gt; &lt;type&gt;<br />
 avmcapictrl load &lt;bootcode&gt; [&lt;contrnr&gt; [&lt;protocol&gt; </p>
<p>&nbsp;<wbr>[P2P |&nbsp;<wbr>&lt;dn1&gt;:&lt;spid1&gt;&nbsp;<wbr>[&lt;dn2&gt;:&lt;spid2&gt;]]]]<br />
 avmcapictrl reset [contrnr]<br />
 avmcapictrl remove [contrnr]<br />
 avmcapictrl trace [contrnr] [off|short|on|full|shortnodata|nodata]<br />
 avmcapictrl addcard &lt;driver&gt; &lt;portbase&gt; &lt;irq&gt; [ &lt;membase&gt; [ &lt;cardnr&gt; ] ]</p>
<h2>Description</h2>
<p><i>avmcapictrl</i> is used to register active AVM ISA cards kernelcapi system and therewith to the isdn system. You need it also to upload the firmware to any active AVM card. If an error occurred please also check the kernel error messages by using the command <a href="/docs/linux/man/8-dmesg/">dmesg</a>(8). </p>
<h2>Commands</h2>
<dl>
<dt><code>add &lt;portbase&gt; &lt;irq&gt; &lt;type&gt;</code></p>
<dd>is used to add a ISA card to the kernel-capi2.0 system. The <i>portbase</i> can have the values 0x150, 0x250, 0x300 and 0x340 for the B1 ISA cards, look at the jumper on the card. For a T1-ISA (HEMA) card you can select an wide range of ports.<br />
 <i>irq</i> can be selected from the following values:<br />
 3, 4, 5, 6, 7, 9, 10, 11, 12 and 15.<br />
 <i>type</i> can be B1 or T1.</dl>
<dl>
<dt><code>load &lt;bootcode&gt; [&lt;contrnr&gt; [&lt;protocol&gt;</code></p>
<dd><code>[P2P | &lt;dn1&gt;:&lt;spid1&gt; [&lt;dn2&gt;:&lt;spid2&gt;]]]]</code> is used to load the firmware to a card <i>bootcode</i> is a t4-file. The actual versions of the t4-files for the different d-channel protocols can be found at <a href="ftp://ftp.avm.de/cardware/b1/linux/firmware.">ftp://ftp.avm.de/cardware/b1/linux/firmware.</a><br />
 You need different t4-files for different d channel protocols: b1-1tr6.t4 for 1TR6, b1.t4 for DSS1 and<br />
 b1-usa.t4 for 5ESS and NI1 (DSS1 is also supported).<br />
 For M1/M2 PCMCIA cards you need m1-s10.t4 or m1-s4.t4 depending on the handy type used.<br />
 <i>contrnr</i> is the number of the controller (card) starting from 1.<br />
 <i>protocol</i> can be DSS1, CT1, VN3, AUSTEL, 5ESS or NI1.<br />
 <i>P2P</i> point to point<br />
 <i>DN1:SPID1 DN2:SPID2</i> is for the North American 5ESS and NI1 protocols.</dl>
<dl>
<dt><code>reset [contrnr]</code></p>
<dd>is used to reset a card if loading has failed. This function only make sense if card is not successfully loaded.<br />
 <i>contrnr</i> is the number of the controller (card) starting from 1.</dl>
<dl>
<dt><code>remove [contrnr]</code></p>
<dd>is used to remove a card previous added. You can also remove automatic added cards (for example a B1-PCI card).<br />
 <i>contrnr</i> is the number of the controller (card) starting from 1.</dl>
<dl>
<dt><code>trace [contrnr] [off|short|on|full|shortnodata|nodata]</code></p>
<dd>is used to trace CAPI2.0 messages. The trace will be done as kernel messages, see <a href="/docs/linux/man/8-dmesg/">dmesg</a>(8).<br />
 <i>contrnr</i> is the number of the controller (card) starting from 1.<br />
 <i>off</i> switch tracing off<br />
 <i>short</i> switch one line per CAPI2.0 message tracing on<br />
 <i>on | full</i> switch on full decode tracing<br />
 <i>shortnodata</i> switch on line per CAPI2.0 message tracing on, but exclude DATA_B3_IND and DATA_B3_REQ messages.<br />
 <i>on | full</i> switch on full decode tracing, but exclude DATA_B3_IND and DATA_B3_REQ messages.</dl>
<dl>
<dt><code>addcard &lt;driver&gt; &lt;portbase&gt; &lt;irq&gt; [ &lt;membase&gt; [ &lt;cardnr&gt; ] ]</code></p>
<dd>is used to add a card, this is more generic than <i>add.</i><br />
 <i>driver</i> currently b1isa or t1isa<br />
 <i>portbase</i> can have the values 0x150, 0x250, 0x300 and 0x340 for the b1isa driver, look at the jumper on the card. For t1isa driver you can select an wide range of ports.<br />
 <i>irq</i> can be selected from the following values: 3, 4, 5, 6, 7, 9, 10, 11, 12 and 15.<br />
 <i>membase</i> memory address if needed by driver<br />
 <i>cardnr</i> only useful with driver t1isa </p>
</dl>
<h2>Author</h2>
<p>Carsten Paeth &lt;calle [at] calle.in-berlin.de&gt;</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/4-ttyi/">ttyI</a></i>(4), <i><a href="/docs/linux/man/8-isdnctrl/">isdnctrl</a></i>(8), <i><a href="/docs/linux/man/4-isdninfo/">isdninfo</a></i>(4). <i><a href="/docs/linux/man/8-dmesg/">dmesg</a></i>(8). <i><a href="/docs/linux/man/8-syslogd/">syslogd</a></i>(8). </p>
