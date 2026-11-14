---
title: "smcinit(8)"
name: "smcinit"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smcinit/"
description: "smcinit – initialize the SMSC IrDA controler on various laptops"
---

<p>smcinit &#8211; initialize the SMSC IrDA controler on various laptops</p>
<h2>Synopsis</h2>
<p>smcinit <code>[OPTIONS]</code></p>
<h2>Description</h2>
<p>Toshiba Satellite 1800, Satellite 5100, Tecra 9100 laptops and may be many other models are provided with a SMCS LPC47N227 SuperIO chip which is IrDA SIR/FIR capable. The IrDA subsystem of the SuperIO chip is supported by the <code>smc-ircc</code> Linux kernel module. Unfortunately the BIOS neither configurates the SuperIO chip IrDA subsystem (SIR port, FIR port, dma, irq, IrDA mode, power) nor sets the PCI-ISA bridge to decode any usable port. Linux kernel is thus prevented to detect the second UART making impossible to use it in SIR mode. For the same reason, the FIR mode <code>smc-ircc</code> is able to detect the SuperIO chip but, once found the IrDA subsystem unconfigured, fails to install. </p>
<p> While this problem will be fixed in Linux 2.6.x kernel series, the 2.4.x users are frustrated. Daniele Peri, Rob Miller and Paul Hampson mananged to build little utilities that initialize the LPC47N227 SuperIO allowing smc-ircc IrDA kernel driver to detect and use the SMSC chip. </p>
<p> My sole work was to put these utilities as one package, easy to install and use.</p>
<h2>Options</h2>
<dl>
<dt><code>-V, &#8211;version</code></p>
<dd>Show program version and exit</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Show a little help on options and exit</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Increase the details about actions performed</p>
<dt><code>-t, &#8211;tty=device</code></p>
<dd>If specified, the serial <code>device</code> will be unbound from the kernel stock serial driver. It is there to replace an external call to <code><a href="/docs/linux/man/1-setserial/">setserial</a>(1)</code> to unset the UART of the device. There is no default value.</p>
<dt><code>-s, &#8211;sirio=IO</code></p>
<dd>Set the SIR (serial infrared) I/O port address to <code>IO</code>. Default value is <i>0x3f8</i>.</p>
<dt><code>-f, &#8211;firio=IO</code></p>
<dd>Set the FIR (fast infrared) I/O port address to <code>IO</code>. Default value is <i>0x130</i>.</p>
<dt><code>-i, &#8211;firirq=IRQ</code></p>
<dd>Set the FIR (fast infrared) IRQ line to <code>IRQ</code>. Default value is <i>3</i>.</p>
<dt><code>-d, &#8211;firdma=DMA</code></p>
<dd>Set the FIR (fast infrared) DMA channel to <code>DMA</code>. Default value is <i>3</i>. </p>
</dl>
<h2>Configuration</h2>
<p>When system startup a script is run from <i>/etc/init.d</i> and which run appropriate SMC intialization utility. This is done before PCMCIA startup because on Tecra 9100 and other models the <code>orinoco_cs</code> wireless driver will block the I/O region used 47N227 SuperIO. </p>
<p> The only configuration file is <i>/etc/sysconfig/smcinit</i> and the variable SMCCONFIG can be set to &quot;1800&quot; or &quot;5100&quot;. By default &quot;5100&quot; value is used.</p>
<dl>
<dt><code>1800</code></p>
<dd>for Toshiba Satellite 1800</p>
<dt><code>5100</code></p>
<dd>for Toshiba Satellite 5100 and Toshiba Tecra 9100</dl>
<p> The next step is to configure the kernel IrDA stack package to attach the smc-ircc driver. This is Linux distribution specific. The main thing is that the device should be set to &quot;irda0&quot;. Run the following command: </p>
<pre>irattach irda0 -s</pre>
<p>Distribution specific configuration:</p>
<dl>
<dt><code>SuSE</code></p>
<dd>Edit the <i>/etc/sysconfig/irda</i> and set IRDA_PORT=irda0</p>
<dt><code>RedHat</code></p>
<dd>Edit the <i>/etc/sysconfig/irda</i> and set DEVICE=irda0</dl>
<h2>Notes</h2>
<p>The <code>smc-ircc</code> driver is preloaded in kernel. I tested the package only on Tecra 9100 without any additional step, but for Toshiba Satellite 1800 Daniele Peri sugest to put the following line in your <i>/etc/modules.conf</i> (on one line): </p>
<pre>options smc-ircc ircc_dma=3 ircc_irq=7 ircc_cfg=0x2e \
 ircc_sir=0x2e8 ircc_fir=0x2f8</pre>
<p>After that run the command: </p>
<pre>prompt# depmod -a</pre>
<p>If the laptop enter suspend mode, then resume operation the <code>smc-ircc</code> driver will stop working. You need to stop IrDA service, then SMCINIT, start SMCINIT, and finally start IrDA service. Simply put, the kernel driver must be unloaded, then reloaded.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sysconfig/smcinit</i></p>
<dd>Configuration file for SMCINIT startup script. It&#8217;s shell script.</dl>
<h2>Author</h2>
<p>This document is made by Claudiu Costin &lt;claudiuc [at] kde.org&gt; The utilities authors are Daniele Peri, Rob Miller and Paul Hampson. Thomas Pinz made improvements to <code>tosh-smcinit</code> (the former <code>tosh5100-smcinit</code>) to expand the number of Toshiba Satellite models supported.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-smcinit/">smcinit</a></code>(7),<br />
 <code><a href="/docs/linux/man/8-tosh1800-smcinit/">tosh1800-smcinit</a></code>(8),<br />
 <code><a href="/docs/linux/man/1-irattach/">irattach</a></code>(1),<br />
 <code><a href="/docs/linux/man/1-irdadump/">irdadump</a></code>(1),<br />
 <code><a rel="nofollow" href="http://irda.sourceforge.net/smcinit/">http://irda.sourceforge.net/smcinit/</a></code> the SMCINIT package home page. </p>
