---
title: "tosh1800-smcinit(8)"
name: "tosh1800-smcinit"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tosh1800-smcinit/"
description: "tosh1800-smcinit – initialize the IrDA controler on Toshiba laptops"
---

<p>tosh1800-smcinit &#8211; initialize the IrDA controler on Toshiba laptops</p>
<h2>Synopsis</h2>
<p><code>tosh1800-smcinit </code> [<i>OPTION</i>]</p>
<h2>Description</h2>
<p>IrDA configurator for laptops with ALI1533 bridge (LPC47N227 SuperIO), smc-ircc and not initializing BIOS (tested on Toshiba Satellite 1800-514, Toshiba Satellite 5100 and Toshiba Tecra 9100) to be used with Linux kernel. </p>
<p> Toshiba Satellite 1800 laptops are provided with a SMCS LPC47N227 SuperIO chip which is IrDA SIR/FIR capable. The chip is connected through an ALI1533 PCI-ISA bridge. The IrDA subsystem of the SuperIO chip is supported by the <code>smc-ircc</code> Linux kernel module. Unfortunately the BIOS neither configurates the SuperIO chip IrDA subsystem (SIR port, FIR port, dma, irq, IrDA mode, power) nor sets the PCI-ISA bridge to decode any usable port. Linux kernel is thus prevented to detect the second UART making impossible to use it in SIR mode. For the same reason, the FIR mode <code>smc-ircc</code> is able to detect the SuperIO chip but, once found the IrDA subsystem unconfigured, fails to install. </p>
<p> <code>tosh1800-smcinit</code> sets SIR and FIR ioport addresses, DMA and IRQ of the SuperIO chip IrDA subsystem then powers on the second UART. It also configures the PCI-ISA bridge to decode SIR and FIR ports. All this configuration work should be rather done into the kernel but it was more practical and safe to make a small testing tool of it. It can be probably extended to include configuration kludges for other similar SuperIO and ISA bridge combination. </p>
<p> Testing was carried on a Toshiba Satellite 1800-514 with Linux kernel 2.4.17. I hope this work could be helpful, it was quite funny to do it however.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;skip-decoding-cfg</code></p>
<dd>Skip ISA bridge decoding configuration.</p>
<dt><code>-b</code>, <code>&#8211;skip-smc-ircc-cfg</code></p>
<dd>Skip SMC-IRCC configuration.</p>
<dt><code>-v</code>, <code>&#8211;vendor</code>=<i>VALUE</i></p>
<dd>Look for the specified ISA bridge PCI vendor ID</p>
<dt><code>-x</code>, <code>&#8211;device</code>=<i>VALUE</i></p>
<dd>Look for the specified ISA bridge PCI device ID</p>
<dt><code>-c</code>, <code>&#8211;cfgbase</code>=<i>VALUE</i></p>
<dd>Set SMC-IRCC IO cfgbase address. Usual value can be 0x2e.</p>
<dt><code>-s</code>, <code>&#8211;sirbase</code>=<i>VALUE</i></p>
<dd>Set SMC-IRCC IO sirbase address. Usual value can be 0x2e8.</p>
<dt><code>-f</code>, <code>&#8211;firbase</code>=<i>VALUE</i></p>
<dd>Set SMC-IRCC IO firbase address. Usual value can be 0x2f8.</p>
<dt><code>-m</code>, <code>&#8211;dma</code>=<i>VALUE</i></p>
<dd>Set SMC-IRCC DMA channel. Usual value can be 3.</p>
<dt><code>-i</code>, <code>&#8211;irq</code>=<i>VALUE</i></p>
<dd>Set SMC-IRCC IRQ. Usual value can be 7.</p>
<dt><code>-p</code>, <code>&#8211;print</code></p>
<dd>Print ISA bridge configuration.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Show program version.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Show program options.</dl>
<h2>Author</h2>
<p>This program was made by Daniele Peri &lt;peri [at] csai.unipa.it&gt;</p>
<h2>Credits</h2>
<p>SMSC for the downloadable datasheets </p>
<p> Paul Hampson for its Linux IrDA mailing list messages. </p>
<p> Manual page written by Claudiu Costin &lt;claudiuc [at] kde.org&gt;. Documentation based on original README by Daniele Peri.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-irattach/">irattach</a></code>(1),<br />
 <code><a href="/docs/linux/man/1-irdadump/">irdadump</a></code>(1),<br />
 <code><a rel="nofollow" href="http://lancelot.csai.unipa.it/~peri/">http://lancelot.csai.unipa.it/~peri/</a></code> Daniele Peri&#8217;s home page,<br />
 <code><a rel="nofollow" href="http://irda.sourceforge.net/smcinit/">http://irda.sourceforge.net/smcinit/</a></code> the SMCINIT package home page. </p>
