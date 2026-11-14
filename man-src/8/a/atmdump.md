---
title: "atmdump(8)"
name: "atmdump"
section: "8"
letter: "a"
url: "/docs/linux/man/8-atmdump/"
description: "atmdump – capture or generate ATM cells"
---

<p>atmdump &#8211; capture or generate ATM cells</p>
<h2>Synopsis</h2>
<p><code>atmdump</code> [<code>-i</code>] [ <code>-t&nbsp;<wbr></code><i>type</i> [<code>-g&nbsp;<wbr></code><i>gfc</i>] [<code>-c</code>] ] [<i>itf</i>.]<i>vpi</i>.<i>vci</i></p>
<h2>Description</h2>
<p><code>atmdump</code> captures or generates single ATM cells (&quot;AAL0&quot;). When capturing cells, a time stamp, the cell header contents, and a hex dump of the cell payload are shown. When sending cells, the payload type, the generic flow control (GFC), and the cell loss priority (CLP) can be set. </p>
<p> In both modes of operation, the interface number, the VPI, and the VCI have to be specified. </p>
<p> When sending, <code>atmdump</code> expects the cell payload on standard input. If only less than 48 bytes can be read, the remaining space is padded with zero bytes.</p>
<h2>Options</h2>
<dl>
<dt><code>-i</code></p>
<dd>displays timestamps as the interval since the last cell reception. By default, the absolute time is displayed. This options is ignored in transmit mode.</p>
<dt><code>-t&nbsp;<wbr></code><i>type</i></p>
<dd>selects transmit mode and specifies the payload type. A list of valid payload type numbers can be obtained by invoking <code>atmdump</code> without any arguments.</p>
<dt><code>-g&nbsp;<wbr></code><i>gfc</i></p>
<dd>specifies the value of the GFC field. <i>gfc</i> has to be in the range from 0 to 15, default is zero.</p>
<dt><code>-c</code></p>
<dd>sets the cell loss priority flag, indicating low priority. By default, CLP is not set.</dl>
<h2>Restrictions</h2>
<p>Some device drivers may not pass OAM cells transparently.</p>
<h2>Author</h2>
<p>Werner Almesberger, EPFL ICA &lt;Werner.Almesberger [at] epfl.ch&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-atmdiag/">atmdiag</a>(8), <a href="/docs/linux/man/8-clip/">clip</a>(8), <a href="/docs/linux/man/8-sonetdiag/">sonetdiag</a>(8) </p>
