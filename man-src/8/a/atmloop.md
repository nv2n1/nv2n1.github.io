---
title: "atmloop(8)"
name: "atmloop"
section: "8"
letter: "a"
url: "/docs/linux/man/8-atmloop/"
description: "atmloop – get/set loopback mode of ATM interfaces"
---

<p>atmloop &#8211; get/set loopback mode of ATM interfaces</p>
<h2>Synopsis</h2>
<p><code>atmloop</code> <code>-s</code> [<code>-l&nbsp;<wbr></code><i>level</i>] [<code>-r&nbsp;<wbr></code><i>level</i>] [<i>itf</i>]<br />
 <code>atmloop</code> [<i>itf</i>]<br />
 <code>atmloop</code> <code>-q</code> [<i>itf</i>]<br />
 <code>atmloop</code> <code>-V</code></p>
<h2>Description</h2>
<p><code>atmloop</code> sets or shows the current loopback settings of an ATM interface, and allows to query the loopback modes supported by the interface. </p>
<p> Some ATM cards can be configured to echo data back to the driver (local loopback) or to the network (remote loopback). The echoing may be done at several different levels:</p>
<dl>
<dt><code>aal</code></p>
<dd>AAL PDUs</p>
<dt><code>atm</code></p>
<dd>ATM cells</p>
<dt><code>digital</code></p>
<dd>bits sent to or received from the line interface</p>
<dt><code>analog</code></p>
<dd>the analog signal</dl>
<p> The levels supported by an interface can be queried with the <code>-q</code> option. If invoked without options, <code>atmloop</code> displays the current loopback settings.</p>
<h2>Options</h2>
<dl>
<dt><code>-s</code></p>
<dd>set loopback mode. Followed by either <code>-l</code> or <code>-r</code>, both options to set local and remote loopback at the same time (if supported by the driver), or none of them to turn off any loopback.</p>
<dt><code>-l&nbsp;<wbr></code><i>level</i></p>
<dd>enable local loopback.</p>
<dt><code>-r&nbsp;<wbr></code><i>level</i></p>
<dd>enable remote loopback.</p>
<dt><code>-q&nbsp;<wbr></code><i>level</i></p>
<dd>query loopback levels supported by the interface.</p>
<dt><code>-V</code></p>
<dd>print version number of <code>atmloop</code> on standard output and exit.</dl>
<h2>Author</h2>
<p>Werner Almesberger, EPFL ICA &lt;Werner.Almesberger [at] epfl.ch&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-atmdiag/">atmdiag</a>(8), <a href="/docs/linux/man/8-sonetdiag/">sonetdiag</a>(8) </p>
