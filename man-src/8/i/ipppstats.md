---
title: "ipppstats(8)"
name: "ipppstats"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipppstats/"
description: "pppstats – print PPP statistics"
---

<p>pppstats &#8211; print PPP statistics</p>
<h2>Synopsis</h2>
<p><code>pppstats</code> [ <code>-v</code> ] [ <code>-r</code> ] [ <code>-c</code> ] [ <code>-i</code> <i>&lt;secs&gt;</i> ] [ <i>&lt;unit#&gt;</i> ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></p>
<h2>Description</h2>
<p><code>pppstats</code> prints PPP-related statistics. The <code>-v</code> flag causes <code>pppstats</code> to display additional statistics, such as the number of packets tossed (that is, which the VJ TCP header decompression code rejected). The <code>-r</code> flag causes <code>pppstats</code> to display the overall packet compression rate. The rate value is between 0 and 1, with 0 meaning that the data is incompressible. The <code>-c</code> flag is used to specify an alternate display mode that shows packet compression statistics: the number of packets and bytes uncompressed (that is, before compression or after decompression), compressed, and incompressible (packets which did not shrink on compression and were transmitted uncompressed), and the recent compression rate. This rate reflects the recent performance of the compression code rather than the overall rate achieved since compression was enabled. The <code>-i</code> flag is used to specify the interval between printouts. The default is 5 seconds. &lt;unit#&gt; specifies which interface to use for gathering statistics. </p>
