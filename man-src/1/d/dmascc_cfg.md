---
title: "dmascc_cfg(1)"
name: "dmascc_cfg"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dmascc_cfg/"
description: "dmascc_cfg – Configure dmascc devices"
---

<h2>NAME</h2>
<p> dmascc_cfg &#8211; Configure dmascc devices</p>
<h2>SYNOPSIS</h2>
<p> <code>dmascc &lt;interface&gt; [&lt;options&gt;]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>dmascc_cfg</code> is used to configure dmascc devices such as PI2 and PackeTwin cards. The <code>&#8211;show</code> option can be used by any user, all other options must be used by root.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;speed </code><i>frequency</i></p>
<dd> Set frequency of baud rate generator to <i>frequency</i>. A value of 0 disables the baud rate generator and the digital PLL. Use the <code>&#8211;show</code> option to check whether the frequency you selected could be approximated with sufficient accuracy.</p>
<dt><code>&#8211;nrzi </code>[<i>0</i>|<i>1</i>]</p>
<dd> <i>0</i> selects NRZ mode, <i>1</i> selects NRZI mode.</p>
<dt><code>&#8211;clocks </code><i>integer</i></p>
<dd> Set the clock mode. You may <code>OR</code> together three choices (other values are not supported and may cause strange results).</dl>
<p> TX clock pin:</p>
<dl>
<dt>
<dd> 0x00 input<br />
 0x05 output TX clock *<br />
 0x06 output baud rate generator *<br />
 0x07 output digital PLL *</dl>
<p> TX clock source:</p>
<dl>
<dt>
<dd> 0x00 RX clock pin<br />
 0x08 TX clock pin #<br />
 0x10 baud rate generator<br />
 0x18 digital PLL +
</dl>
<p> RX clock source:</p>
<dl>
<dt>
<dd> 0x00 RX clock pin<br />
 0x20 TX clock pin<br />
 0x40 baud rate generator<br />
 0x60 digital PLL +
</dl>
<p> * Not allowed on PI2 Port A if J3 is installed. </p>
<p> # TX clock pin must be configured as input. </p>
<p> + Speed must be equal to 32 times the baud rate.</p>
<dl>
<dt><code>&#8211;txdelay </code><i>milliseconds</i></p>
<dd> Set transmit delay to <i>milliseconds</i>. Maximum is 2500 ms.</p>
<dt><code>&#8211;txtime </code><i>seconds</i></p>
<dd> Set maximum time the transmitter may be active to <i>seconds</i>.</p>
<dt><code>&#8211;sqdelay </code><i>milliseconds</i></p>
<dd> Set the squelch delay to <i>milliseconds</i>. Maximum delay is 2500 ms.</p>
<dt><code>&#8211;slottime </code><i>milliseconds</i></p>
<dd> Set the slot time to <i>milliseconds</i>. Maximum slottime is 2500 ms.</p>
<dt><code>&#8211;waittime </code><i>milliseconds</i></p>
<dd> Set the minimum time between the transmitter turning off to when it turns on to <i>milliseconds</i>. Maximum wait time is 2500 ms.</p>
<dt><code>&#8211;persist </code><i>f</i></p>
<dd> Set the persistance parameter to <i>f</i>. Must be between 0 and 255 (inclusive).</p>
<dt><code>&#8211;dma </code><i>channel</i></p>
<dd> Set the DMA channel to <i>channel</i>. Can be 1 or 3. Setting to 0 disables DMA.</dl>
<h2>BUGS</h2>
<p> <code>dmascc_cfg</code> does not check the parameters for validity. The driver or kernel may crash if you specify invalid values.</p>
<h2>AUTHORS</h2>
<pre>
Klaus Kudielka
<br>
This manual page written by Craig Small &lt;csmall [at] small.dropbear.id.au&gt;
</pre>
<h2>Index</h2>
