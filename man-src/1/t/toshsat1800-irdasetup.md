---
title: "toshsat1800-irdasetup(1)"
name: "toshsat1800-irdasetup"
section: "1"
letter: "t"
url: "/docs/linux/man/1-toshsat1800-irdasetup/"
description: "toshsat1800-irdasetup – IrDA setup utility for Toshiba Satellite 1800"
---

<h2 class="name">NAME</h2>
<p> toshsat1800-irdasetup &#8211; IrDA setup utility for Toshiba Satellite 1800 </p>
<h2>SYNOPSIS</h2>
<p> <code>toshsat1800-irdasetup</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> IrDA configurator for laptops with ALI1533 bridge (LPC47N227 SuperIO), smc-ircc and not initializing BIOS (tested on Toshiba Satellite 1800-514) to be used with Linux kernel.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;skip-decoding-cfg</code> skip ISA bridge decoding configuration</p>
<dd>
<dt><code>-b</code>, <code>&#8211;skip-smc-ircc-cfg</code> skip SMC-IRCC configuration</p>
<dd>
<dt><code>-v</code>, <code>&#8211;vendor</code>=<i>VALUE</i> look for the specified ISA bridge PCI vendor id</p>
<dd>
<dt><code>-x</code>, <code>&#8211;device</code>=<i>VALUE</i> look for the specified ISA bridge PCI device id</p>
<dd>
<dt><code>-c</code>, <code>&#8211;cfgbase</code>=<i>VALUE</i> set SMC-IRCC IO cfgbase address</p>
<dd>
<dt><code>-s</code>, <code>&#8211;sirbase</code>=<i>VALUE</i> set SMC-IRCC IO sirbase address</p>
<dd>
<dt><code>-f</code>, <code>&#8211;firbase</code>=<i>VALUE</i> set SMC-IRCC IO firbase address</p>
<dd>
<dt><code>-m</code>, <code>&#8211;dma</code>=<i>VALUE</i> set SMC-IRCC DMA channel</p>
<dd>
<dt><code>-i</code>, <code>&#8211;irq</code>=<i>VALUE</i> set SMC-IRCC IRQ</p>
<dd>
<dt><code>-p</code>, <code>&#8211;print</code> print ISA bridge configuration</p>
<dd>
<dt><code>-h</code>, <code>&#8211;help</code> show this help</p>
<dd></dl>
<h2>SEE ALSO</h2>
<p> More detailed information in /usr/share/doc/toshset/README.IrDA or online at <a rel="nofollow" href="http://www.csai.unipa.it/peri/toshsat1800-irdasetup/">http://www.csai.unipa.it/peri/toshsat1800-irdasetup/</a></p>
<h2>AUTHOR</h2>
<p> toshsat1800-irdasetup was written by Daniele Peri &lt;peri [at] csai.unipa.it&gt;. </p>
<p> This manual page was written by Roberto C. Sanchez &lt;roberto [at] connexer.com&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
