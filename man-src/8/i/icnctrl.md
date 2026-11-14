---
title: "icnctrl(8)"
name: "icnctrl"
section: "8"
letter: "i"
url: "/docs/linux/man/8-icnctrl/"
description: "icnctrl – configure ICN ISDN adaptor"
---

<p>icnctrl &#8211; configure ICN ISDN adaptor</p>
<h2>Synopsis</h2>
<p><code>icnctrl [-d</code> <i>Driver-Id</i><code>]</code> <i>action options</i> <code>&#8230;</code></p>
<h2>Description</h2>
<p><code>icnctrl</code> is used to setup the ICN <font SIZE="-1">ISDN</font> device driver and for downloading the firmware into the <font SIZE="-1">ISDN</font> card. The use of <i>icnctrl</i> makes sense, if you are using an ICN card only. </p>
<h2>Options</h2>
<dl>
<dt><code>-d </code><i>Driver-Id</i></p>
<dd>selects the S0 interface named by <i>Driver-Id</i>. Driver-Ids are defined during driver initialisation. See <code><a href="/docs/linux/man/4-icn/">icn</a></code>(4) for a description of the syntax to be used for modularised and monolithic driver versions. This option <code>must</code> be used to identify the S0 interface if more than one S0 interface is existent. If a single ICN-2B is used, it may be omitted. If using more than one card, support for the other cards is enabled with the <code>add</code> action of icnctrl. Ids may <code>not</code> start with <code>digits</code> or small <code>x</code>, because these values are misinterpreted as numeric parameters by <code>insmod</code>. For loading the module, always the newest <code>modutils</code> package should be used to avoid problems during load.</dl>
<p> The following <i>actions</i> may be given to <code>icnctrl</code>.</p>
<dl>
<dt><code>add port [</code><i>id1</i><code> [</code><i>id2</i><code>]]</code></p>
<dd>enables support for an additional card in the driver. If <i>id1</i> and <i>id2</i> are missing, adds an ICN-2B with an id given by the system. with <i>id2</i> missing, adds an ICN-2B with an Id given by the user. With both Ids given, adds an ICN-4B with both Ids given by the user. There is <code>no checking</code> against port-conflicts. Ports are checked later during first activation while downloading the firmware and can be changed at runtime. Ids are checked against conflicts, and if a conflict happens, replaced by the system in the same manner as if no Id was supplied. It is <code>not allowed,</code> to add cards, <code>after</code> a <code>load</code> was done.</p>
<dt><code>io [</code><i>base-address port</i><code>]</code></p>
<dd>sets the address of the memory-mapped IO-region and the port-base. After loading the icn-module into kernel-space, this command should be used as the very first setup, if the hardware settings are different from the default settings below. If both parameters are omitted, prints out current settings. The default memory address is <i>0xD0000</i>, the default port-base is <i>0x320</i>. An ICN card uses 4 port-addresses. The memory address is globally used for all cards (cards are mapped on demand), while each card has its own port range. Memory range is <i>16k</i>.</p>
<dt><code>leased on|1|2|off</code></p>
<dd>switches between normal (dialup) and leased-line mode. Leased-line mode is intended for usage with S64K-lines or &#8211; if both channels are used &#8211; for S02. If the second parameter is <code>1</code> , only one channel is enabled. If the second parameter is <code>2</code> or <code>on</code> both channels are enabled. Leased lines do not have a D-channel. When leased-line mode is enabled, the driver simulates incoming calls using special &quot;phone-numbers&quot; for calling and called address which are generated as follows:</p>
<dl>
<dd>Calling number:</p>
<dl>
<dd><code>LEASED</code><i>x</i></p>
<dl>
<dd>where <i>x</i> is the internal slot-number of the S0 interface. This number starts with <i>0</i> for the first S0 interface and is incremented by one for every S0 interface configured using the <code>add</code> action.</dl>
</dl>
<p> Called number:</p>
<dl>
<dd><i>x</i></p>
<dl>
<dd>where <i>x</i> is equal to the channel number of the calling S0 interface starting with <i>1</i>.</dl>
</dl>
</dl>
<dt><code>load </code><i>boot-code</i><i>firmware</i><code> [</code><i>firmware2</i><code>]</code></p>
<dd>downloads the firmware into the card and starts operation. Using this command, after loading the icn-module into kernel-space the first real access to the hardware is done. Therefore the <code>io</code> action above, should be used before, if the hardware settings are different from the default settings. Usually the images are located in <i>@DATADIR@</i>. The boot-code is named <i>loadpg.bin</i>. The firmware depends on the D-channel protocol of the <font SIZE="-1">ISDN</font> line. For German 1TR6-lines, the firmware is named <i>pc_1t_ca.bin</i>. For Euro-ISDN-lines, it is named <i>pc_eu_ca.bin</i>. When loading an ICN-4B, <code>two</code> firmware parameters have to be supplied. The first firmware is used for the upper S0 connector, the second firmware is used for the lower S0 connector (towards the card&#8217;s slot connector).</p>
<dt><code>dump</code></p>
<dd>is available if the program is configured using the <code>&#8211;enable-dump</code> option only. The contents of internal driver variables is dumped on stdout.</dl>
<h2>Files</h2>
<dl>
<dt><i>@DATADIR@/loadpg.bin</i></p>
<dd>This is the image of the bootstrap loader, which is loaded first, then loads the firmware into the card&#8217;s memory and starts execution.</p>
<dt><i>@DATADIR@/pc_1t_ca.bin</i></p>
<dd>This is the image of the firmware designed for the German 1TR6 protocol.</p>
<dt><i>@DATADIR@/pc_eu_ca.bin</i></p>
<dd>This is the image of the firmware, designed for Euro ISDN.</dl>
<h2>Diagnostics</h2>
<p>The following diagnostics may be issued on stderr:</p>
<dl>
<dt>Read error on <i>boot-code</i></p>
<dd>The file supplied as <i>boot-code</i> has less than 4096 bytes length or could not be read.</p>
<dt>Read error on <i>firmware</i></p>
<dd>The file supplied as <i>firmware</i> has less than 65536 bytes length or could not be read.</dl>
<h2>Bugs</h2>
<p>No bugs so far.</p>
<h2>Author</h2>
<p>&#169; 1997 by Fritz Elfert &lt;fritz [at] isdn4linux.de&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-isdnctrl/">isdnctrl</a></code>(8), <code><a href="/docs/linux/man/4-icn/">icn</a></code>(4), <code><a href="/docs/linux/man/4-isdnctrl/">isdnctrl</a></code>(4), <code><a href="/docs/linux/man/4-ttyi/">ttyI</a></code>(4). </p>
