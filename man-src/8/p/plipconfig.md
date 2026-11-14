---
title: "plipconfig(8)"
name: "plipconfig"
section: "8"
letter: "p"
url: "/docs/linux/man/8-plipconfig/"
description: "plipconfig – fine tune PLIP device parameters"
---

<p>plipconfig &#8211; fine tune PLIP device parameters</p>
<h2>Synopsis</h2>
<p><code>plipconfig interface</code> [<code>nibble</code> <i>NN</i>] [<code>trigger</code> <i>NN</i>]<br />
 <code>plipconfig</code> [<code>-V</code>] [<code>&#8211;version</code>] [<code>-h</code>] [<code>&#8211;help</code>]</p>
<h2>Description</h2>
<p><code>Plipconfig</code> is used to (hopefully) improve PLIP performance by changing the default timing parameters used by the PLIP protocol. Results are dependent on the parallel port hardware, cable, and the CPU speed of each machine on each end of the PLIP link. </p>
<p> If the single <code>interface</code> argument is given, <code>plipconfig</code> displays the status of the given interface only. Otherwise, it will try to set the options.</p>
<h2>Options</h2>
<dl>
<dt><code>nibble NN</code></p>
<dd>Sets the nibble wait value in microseconds. Default is 3000.</p>
<dt><code>trigger NN</code></p>
<dd>Sets the trigger wait value in microseconds. Default is 500.</dl>
<p> PLIP speed can in some cases be improved by lowering the default values. Values which are too low may cause excess use of CPU, poor interrupt response time resulting in serial ports dropping characters, or in dropping of PLIP packets. Changing the plip MTU can also affect PLIP speed.</p>
<h2>Note</h2>
<p>If you get no response it is far more likely the irq is wrong and needs setting with ifconfig. The few cases where the default parameters will be too fast are those using very long cables. Something you should never do as the parallel port is not specified or designed for driving long cable runs.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ifconfig/">ifconfig</a>(8)</i></p>
<h2>Bugs</h2>
<p>Non.</p>
<h2>Author</h2>
<p>John Paul Morrison, &lt;jmorriso [at] bogomips.ee.ubc.ca&gt;, &lt;ve7jpm [at] ve7jpm.ampr.org&gt;</p>
