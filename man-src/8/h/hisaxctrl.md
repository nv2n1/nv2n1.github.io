---
title: "hisaxctrl(8)"
name: "hisaxctrl"
section: "8"
letter: "h"
url: "/docs/linux/man/8-hisaxctrl/"
description: "hisaxctrl – configure HiSax-Module"
---

<p>hisaxctrl &#8211; configure HiSax-Module</p>
<h2>Synopsis</h2>
<p><code>hisaxctrl</code> <i>DriverId command parameters</i></p>
<h2>Description</h2>
<p><code>hisaxctrl</code> is used to setup the HiSax-ISDN device driver. All logging-output is sent to the device /dev/isdnctrl. So you can show it by executing <code>cat /dev/isdnctrl</code>.<br />
 <code>NOTE:</code> for <i>devfs</i> systems, the program will automatically use /dev/isdn/isdnctrl if available. The use of <i>hisaxctrl</i> only makes sense if you are using the HiSax driver. </p>
<h2>Options</h2>
<dl>
<dt><i>DriverId</i></p>
<dd>is used to identify the card when using more than one passive card. While loading the hisax module with <i>insmod</i>, or <i>modprobe</i> the DriverId is set by appending <code>id=</code><i>idstring1</i><code>%</code><i>idstring2</i><code>%&#8230;</code> to the commandline.</dl>
<dl>
<dt><i>command</i></p>
<dd>is an integer selecting the setup category. The following values are defined for setting the logging-level of the HiSax-ISDN device driver:</dl>
<dl>
<dd><code> 0</code> reports card status infos.<br />
 <code> 1</code> selects generic debugging.<br />
 <code>11</code> selects layer 1 development debugging.<br />
 <code>13</code> selects layer 3 development debugging.
</dl>
<p> the following commands are used to enable special features during runtime of the HiSax-ISDN device driver. </p>
<dl>
<dd><code> 2</code> set B-channel ON delay to parameter (in ms)<br />
 <code> 5</code> set B-channel in leased mode<br />
 <code> 6</code> set B-channel in TESTLOOP mode<br />
 <code> 7</code> set/reset card in Point To Point mode<br />
 <code> 8</code> set card in FIXED TEI mode<br />
 <code> 9</code> load firmware for DSP cards<br />
 <code>10</code> set B-channel usage limit to 1 or 2 channels<br />
 <code>12</code> set echo logging mode (only for some cards)<br />
 B-channel usage limit needs to be 1 if enabled
</dl>
<dl>
<dt><i>parameter</i></p>
<dd>If the command is <code>9</code> then the parameter is the full pathname to the file containing the firmware. </p>
<p> For debug settings this is an integer representing a bitmask. Every bit in this mask switches a debug facility on or off. Depending on the selected category, the following values are defined:</dl>
<dl>
<dd>With<code> generic debugging </code>selected<br />
 (command <code>1</code>): </p>
<p> <code>0x001</code> Link-level &lt;&#8211;&gt; hardware-level communication<br />
 <code>0x002</code> Top state machine<br />
 <code>0x004</code> D-Channel Q.931 (call control messages)<br />
 <code>0x008</code> D-Channel Q.921<br />
 <code>0x010</code> B-Channel X.75<br />
 <code>0x020</code> D-Channel l2<br />
 <code>0x040</code> B-Channel l2<br />
 <code>0x080</code> D-Channel link state debugging<br />
 <code>0x100</code> B-Channel link state debugging<br />
 <code>0x200</code> TEI debug<br />
 <code>0x400</code> LOCK debug in callc.c<br />
 <code>0x800</code> More debug in callc.c (not for normal use) </p>
<p> With<code> layer 1 development debugging </code>selected<br />
 (command <code>11</code>): </p>
<p> <code>0x001</code> Warnings (default: on)<br />
 <code>0x002</code> IRQ status<br />
 <code>0x004</code> ISAC<br />
 <code>0x008</code> ISAC FIFO<br />
 <code>0x010</code> HSCX<br />
 <code>0x020</code> HSCX FIFO (attention: full B-Channel output!)<br />
 <code>0x040</code> D-Channel LAPD frame types </p>
<p> With<code> layer 3 development debugging </code>selected<br />
 (command <code>13</code>): </p>
<p> <code>0x001</code> Warnings (default: on)<br />
 <code>0x002</code> l3 protocol discriptor errors<br />
 <code>0x004</code> l3 state machine<br />
 <code>0x008</code> charge info debugging (1TR6)
</dl>
<h2>Example</h2>
<dl>
<dt><code>hisaxctrl</code><i> HiSax 1 0x3ff</i></p>
<dd>enables full generic debugging.</dl>
<h2>Author</h2>
<p>&#169; 2000 by Karsten Keil &lt;kkeil [at] suse.de&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-isdnctrl/">isdnctrl</a></code>(8), <code><a href="/docs/linux/man/7-isdn_cause/">isdn_cause</a></code>(7), <code><a href="/docs/linux/man/4-isdninfo/">isdninfo</a></code>(4). </p>
