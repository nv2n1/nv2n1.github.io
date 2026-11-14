---
title: "atmaddr(8)"
name: "atmaddr"
section: "8"
letter: "a"
url: "/docs/linux/man/8-atmaddr/"
description: "atmaddr – list and maintain local ATM addresses"
---

<p>atmaddr &#8211; list and maintain local ATM addresses</p>
<h2>Synopsis</h2>
<p><code>atmaddr</code> [<code>-n</code>]&nbsp;<wbr>[<i>itf</i>]<br />
 <code>atmaddr</code> <code>-r</code> [<i>itf</i>]<br />
 <code>atmaddr</code> <code>-a</code> [<i>itf</i>]&nbsp;<wbr><i>atm_addr</i><br />
 <code>atmaddr</code> <code>-d</code> [<i>itf</i>]&nbsp;<wbr><i>atm_addr</i><br />
 <code>atmaddr</code> <code>-V</code></p>
<h2>Description</h2>
<p><code>atmaddr</code> is used to list the local addresses configured for ATM interfaces and to manually change the list of addresses. If the interface number <i>itf</i> is omitted, interface 0 is used by default. The ATM address <i>atm_addr</i> can be any valid ATM SVC address, e.g. an E.164 address or an ATM Forum NSAP address. </p>
<p> If invoked without options, <code>atmaddr</code> lists the addresses that are currently configured on the specified interface. </p>
<p> Note that local ATM addresses are normally automatically maintained by the ILMI demon.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>append the specified address at the end of the list.</p>
<dt><code>-d</code></p>
<dd>delete the specified address from the list.</p>
<dt><code>-n</code></p>
<dd>numeric address output only. No address to name translation is attempted.</p>
<dt><code>-r</code></p>
<dd>reset (clear) the local address list of the specified interface.</p>
<dt><code>-V</code></p>
<dd>print the version number of <code>atmaddr</code> on standard output and exit.</dl>
<h2>Author</h2>
<p>Werner Almesberger, EPFL ICA &lt;Werner.Almesberger [at] epfl.ch&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ilmid/">ilmid</a>(8) </p>
