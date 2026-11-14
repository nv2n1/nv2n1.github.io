---
title: "pppstats(8)"
name: "pppstats"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pppstats/"
description: "pppstats – print PPP statistics"
---

<p>pppstats &#8211; print PPP statistics</p>
<h2>Synopsis</h2>
<p><code>pppstats</code> [ <code>-a</code> ] [ <code>-d</code> ] [ <code>-v</code> ] [ <code>-r</code> ] [ <code>-z</code> ] [ <code>-c</code> <i>&lt;count&gt;</i> ] [ <code>-w</code> <i>&lt;secs&gt;</i> ] [ <i>interface</i> ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<h2>Description</h2>
<p>The <code>pppstats</code> utility reports PPP-related statistics at regular intervals for the specified PPP interface. If the interface is unspecified, it will default to ppp0. The display is split horizontally into input and output sections containing columns of statistics describing the properties and volume of packets received and transmitted by the interface. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-a</code></p>
<dd>Display absolute values rather than deltas. With this option, all reports show statistics for the time since the link was initiated. Without this option, the second and subsequent reports show statistics for the time since the last report.</p>
<dt><code>-d</code></p>
<dd>Show data rate (kB/s) instead of bytes.</p>
<dt><code>-c </code><i>count</i></p>
<dd>Repeat the display <i>count</i> times. If this option is not specified, the default repeat count is 1 if the <code>-w</code> option is not specified, otherwise infinity.</p>
<dt><code>-r</code></p>
<dd>Display additional statistics summarizing the compression ratio achieved by the packet compression algorithm in use.</p>
<dt><code>-v</code></p>
<dd>Display additional statistics relating to the performance of the Van Jacobson TCP header compression algorithm.</p>
<dt><code>-w </code><i>wait</i></p>
<dd>Pause <i>wait</i> seconds between each display. If this option is not specified, the default interval is 5 seconds.</p>
<dt><code>-z</code></p>
<dd>Instead of the standard display, show statistics indicating the performance of the packet compression algorithm in use.</dl>
<p> The following fields are printed on the input side when the <code>-z</code> option is not used:</p>
<dl>
<dt><code>IN</code></p>
<dd>The total number of bytes received by this interface.</p>
<dt><code>PACK</code></p>
<dd>The total number of packets received by this interface.</p>
<dt><code>VJCOMP</code></p>
<dd>The number of header-compressed TCP packets received by this interface.</p>
<dt><code>VJUNC</code></p>
<dd>The number of header-uncompressed TCP packets received by this interface. Not reported when the <code>-r</code> option is specified.</p>
<dt><code>VJERR</code></p>
<dd>The number of corrupted or bogus header-compressed TCP packets received by this interface. Not reported when the <code>-r</code> option is specified.</p>
<dt><code>VJTOSS</code></p>
<dd>The number of VJ header-compressed TCP packets dropped on reception by this interface because of preceding errors. Only reported when the <code>-v</code> option is specified.</p>
<dt><code>NON-VJ</code></p>
<dd>The total number of non-TCP packets received by this interface. Only reported when the <code>-v</code> option is specified.</p>
<dt><code>RATIO</code></p>
<dd>The compression ratio achieved for received packets by the packet compression scheme in use, defined as the uncompressed size divided by the compressed size. Only reported when the <code>-r</code> option is specified.</p>
<dt><code>UBYTE</code></p>
<dd>The total number of bytes received, after decompression of compressed packets. Only reported when the <code>-r</code> option is specified.</dl>
<p> The following fields are printed on the output side:</p>
<dl>
<dt><code>OUT</code></p>
<dd>The total number of bytes transmitted from this interface.</p>
<dt><code>PACK</code></p>
<dd>The total number of packets transmitted from this interface.</p>
<dt><code>VJCOMP</code></p>
<dd>The number of TCP packets transmitted from this interface with VJ-compressed TCP headers.</p>
<dt><code>VJUNC</code></p>
<dd>The number of TCP packets transmitted from this interface with VJ-uncompressed TCP headers. Not reported when the <code>-r</code> option is specified.</p>
<dt><code>NON-VJ</code></p>
<dd>The total number of non-TCP packets transmitted from this interface. Not reported when the <code>-r</code> option is specified.</p>
<dt><code>VJSRCH</code></p>
<dd>The number of searches for the cached header entry for a VJ header compressed TCP packet. Only reported when the <code>-v</code> option is specified.</p>
<dt><code>VJMISS</code></p>
<dd>The number of failed searches for the cached header entry for a VJ header compressed TCP packet. Only reported when the <code>-v</code> option is specified.</p>
<dt><code>RATIO</code></p>
<dd>The compression ratio achieved for transmitted packets by the packet compression scheme in use, defined as the size before compression divided by the compressed size. Only reported when the <code>-r</code> option is specified.</p>
<dt><code>UBYTE</code></p>
<dd>The total number of bytes to be transmitted, before packet compression is applied. Only reported when the <code>-r</code> option is specified.</dl>
<p> When the <code>-z</code> option is specified, <code>pppstats</code> instead displays the following fields, relating to the packet compression algorithm currently in use. If packet compression is not in use, these fields will all display zeroes. The fields displayed on the input side are:</p>
<dl>
<dt><code>COMPRESSED BYTE</code></p>
<dd>The number of bytes of compressed packets received.</p>
<dt><code>COMPRESSED PACK</code></p>
<dd>The number of compressed packets received.</p>
<dt><code>INCOMPRESSIBLE BYTE</code></p>
<dd>The number of bytes of incompressible packets (that is, those which were transmitted in uncompressed form) received.</p>
<dt><code>INCOMPRESSIBLE PACK</code></p>
<dd>The number of incompressible packets received.</p>
<dt><code>COMP RATIO</code></p>
<dd>The recent compression ratio for incoming packets, defined as the uncompressed size divided by the compressed size (including both compressible and incompressible packets).</dl>
<p> The fields displayed on the output side are:</p>
<dl>
<dt><code>COMPRESSED BYTE</code></p>
<dd>The number of bytes of compressed packets transmitted.</p>
<dt><code>COMPRESSED PACK</code></p>
<dd>The number of compressed packets transmitted.</p>
<dt><code>INCOMPRESSIBLE BYTE</code></p>
<dd>The number of bytes of incompressible packets transmitted (that is, those which were transmitted in uncompressed form).</p>
<dt><code>INCOMPRESSIBLE PACK</code></p>
<dd>The number of incompressible packets transmitted.</p>
<dt><code>COMP RATIO</code></p>
<dd>The recent compression ratio for outgoing packets.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-pppd/">pppd</a>(8) </p>
