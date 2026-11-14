---
title: "ibstatus(8)"
name: "ibstatus"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ibstatus/"
description: "IBSTATUS –"
---

<p>IBSTATUS &#8211;</p>
<h2>Query Basic Status Of Infiniband Device(S)</h2>
<h3>Synopsis</h3>
<p>ibstatus [-h] [devname[:port]]&#8230;</p>
<h3>Description</h3>
<p>ibstatus is a script which displays basic information obtained from the local IB driver. Output includes LID, SMLID, port state, link width active, and port physical state.</p>
<h3>Options</h3>
<p><code>-h, &#8211;help</code> show the usage message</p>
<dl>
<dt><code>devname</code></p>
<dd>InfiniBand device name</p>
<dt><code>portnum</code></p>
<dd>port number of InfiniBand device</dl>
<h3>Examples</h3>
<dl>
<dt><code>::</code></p>
<dd>ibstatus # display status of all IB ports ibstatus mthca1 # status of mthca1 ports ibstatus mthca1:1 mthca0:2 # show status of specified ports</dl>
<h3>See Also</h3>
<p><code>ibstat (8)</code></p>
<h3>Author</h3>
<dl>
<dt><code>Hal Rosenstock</code></p>
<dd>&lt; <i>halr [at] voltaire.com</i> &gt; </p>
</dl>
