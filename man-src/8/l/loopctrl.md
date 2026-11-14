---
title: "loopctrl(8)"
name: "loopctrl"
section: "8"
letter: "l"
url: "/docs/linux/man/8-loopctrl/"
description: "loopctrl – configure isdnloop ISDN driver"
---

<p>loopctrl &#8211; configure isdnloop ISDN driver</p>
<h2>Synopsis</h2>
<p><code>loopctrl [-d</code> <i>Driver-Id</i><code>]</code> <i>action options</i> <code>&#8230;</code></p>
<h2>Description</h2>
<p><code>loopctrl</code> is used to setup the isdnloop <font SIZE="-1">ISDN</font> driver. </p>
<h2>Options</h2>
<dl>
<dt><code>-d </code><i>Driver-Id</i></p>
<dd>selects the virtual S0 interface named by <i>Driver-Id</i>. Driver-Ids are defined during driver initialisation. See <code><a href="/docs/linux/man/4-isdnloop/">isdnloop</a></code>(4) for a description of the syntax to be used for modularised and monolithic driver versions. This option <code>must</code> be used to identify the virtual S0 interface if more than one S0 interface is existent. If a single virtual S0 interface is used, it may be omitted. If using more than one virtual card, support for the other cards is enabled with the <code>add</code> action of loopctrl. Ids may <code>not</code> start with <code>digits</code> or small <code>x</code>, because these values are misinterpreted as numeric parameters by <code>insmod</code>. For loading the module, always the newest <code>modutils</code> package should be used to avoid problems during load.</dl>
<p> The following <i>actions</i> may be given to <code>loopctrl</code>.</p>
<dl>
<dt><code>add [</code><i>id</i><code>]</code></p>
<dd>enables support for an additional virtual card in the driver. If <i>id</i> is missing, adds a card with an id given by the system. with <i>id</i> given, adds a card with an Id given by the user. Ids are checked against conflicts, and if a conflict happens, replaced by the system in the same manner as if no Id was supplied.</p>
<dt><code>leased on|off</code></p>
<dd>switches between normal (dialup) and leased-line mode. Leased-line mode is intended for usage with S64K-lines or &#8211; if both channels are used &#8211; for S02. These lines do not have a D-channel. When leased-line mode is enabled, the driver simulates incoming calls using special &quot;phone-numbers&quot; for calling and called address which are generated as follows:</p>
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
<dt><code>start </code><i>protocol</i><i>phone1</i><code> [</code><i>phone2 phone3</i><code>]</code></p>
<dd>starts the driver with the given D-channel protocol. If <i>protocol</i> is <code>1tr6</code>, only<i> phone1</i> has to be given. It is meant to be the base number of the virtual S0 interface to which the EAZ is appended. If <i>protocol</i> is <code>dss1</code>, <i>phone1, phone2 </i>and<i> phone3</i> have to be given and represent the three MSNs of the virtual S0 interface.</p>
<dt><code>dump</code></p>
<dd>is available if the program is configured using the <code>&#8211;enable-dump</code> option only. The contents of internal driver variables is dumped on stdout.</dl>
<h2>Bugs</h2>
<p>This program and the isdnloop driver are <code>ALPHA</code> code. The main intention for this driver is for testing the link level and applications.</p>
<h2>Author</h2>
<p>&#169; 1997 by Fritz Elfert &lt;fritz [at] isdn4linux.de&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-isdnctrl/">isdnctrl</a></code>(8), <code><a href="/docs/linux/man/4-isdnloop/">isdnloop</a></code>(4), <code><a href="/docs/linux/man/4-isdninfo/">isdninfo</a></code>(4), <code><a href="/docs/linux/man/4-isdnctrl/">isdnctrl</a></code>(4), <code><a href="/docs/linux/man/4-ttyi/">ttyI</a></code>(4). </p>
