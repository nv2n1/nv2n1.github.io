---
title: "iecset(1)"
name: "iecset"
section: "1"
letter: "i"
url: "/docs/linux/man/1-iecset/"
description: "iecset – Set or dump IEC958 status bits"
---

<h2 class="name">NAME</h2>
<p> iecset &#8211; Set or dump IEC958 status bits</p>
<h2>SYNOPSIS</h2>
<p> <code>iecset</code> [<i>options</i>] [<i>cmd</i> <i>arg</i>&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <code>iecset</code> is a small utility to set or dump the IEC958 (or so-called &quot;S/PDIF&quot;) status bits of the specified sound card via ALSA control API. </p>
<p> When <code>iecset</code> is started without arguments except for options, it will show the current IEC958 status in a human-readable form. When the commands are given in the arguments, they are parsed and the IEC958 status bits are updated. The resultant status is shown as well. </p>
<p> The commands consist of the command directive and the argument. As the boolean argument, <i>yes</i>, <i>no</i>, <i>true</i>, <i>false</i>, or a digit number is allowed. </p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>iecset -Dhw:1</code></p>
<dd> Displays the current IEC958 status bits on the second card. This is equivalent with <i>-c 1</i>.</p>
<dt><code>iecset -x</code></p>
<dd> Displays the current IEC958 status bits in a style of the arguments for the PCM stream. The output string can be passed to the <i>iec958</i> (or <i>spdif</i>) PCM type as the optional argument.</p>
<dt><code>iecset pro off audio off</code></p>
<dd> Sets the current status to the consumer-mode and turns on the non-audio bit. The modified status will be shown, too. </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><i>-D</i> device</p>
<dd> Specifies the device name of the control to open</p>
<dt><i>-c</i> card</p>
<dd> Specifies the card index to open. Equivalent with <i>-Dhw:x</i>.</p>
<dt><i>-n</i> index</p>
<dd> Specifies the IEC958 control element index, in case you have multiple IEC958 devices and need to choose one of them.</p>
<dt><i>-x</i></p>
<dd> Dumps the status in the form of AESx bytes.</p>
<dt><i>-i</i></p>
<dd> Reads the command sequences from stdin. Each line has single command. </p>
</dl>
<h2>COMMANDS</h2>
<dl>
<dt><i>professional</i> &lt;bool&gt;</p>
<dd> The professional mode (true) or consumer mode (false). </p>
<dt><i>audio</i> &lt;bool&gt;</p>
<dd> The audio mode (true) or non-audio mode (false). </p>
<dt><i>rate</i> &lt;int&gt;</p>
<dd> The sample rate in Hz. </p>
<dt><i>emphasis</i> &lt;int&gt;</p>
<dd> The emphasis: 0 = none, 1 = 50/15us, 2 = CCITT. </p>
<dt><i>lock</i> &lt;bool&gt;</p>
<dd> Rate lock: locked (true), unlocked (false). This command is for the professional mode only. </p>
<dt><i>sbits</i> &lt;int&gt;</p>
<dd> Sample bits: 2 = 20bit, 4 = 24bit, 6 = undefined. This command is for the professional mode only. </p>
<dt><i>wordlength</i> &lt;int&gt;</p>
<dd> Wordlength: 0 = No, 2 = 22-18 bit, 4 = 23-19 bit, 5 = 24-20 bit, 6 = 20-16 bit. This command is for the professional mode only. </p>
<dt><i>category</i> &lt;int&gt;</p>
<dd> Category: the value is from 0 to 0x7f. This command is for the consumer mode only. </p>
<dt><i>copyright</i> &lt;bool&gt;</p>
<dd> Copyright: copyrighted (true), non-copyrighted (false). This command is for the consumer mode only. </p>
<dt><i>original</i> &lt;boo&gt;</p>
<dd> Original flag: original (true), 1st generation (false). This command is for the consumer mode only. </p>
</dl>
<h2>AUTHOR</h2>
<p> Takashi Iwai &lt;tiwai [at] suse.de&gt; </p>
<h2>Index</h2>
