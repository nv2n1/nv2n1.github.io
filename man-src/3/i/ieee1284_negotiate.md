---
title: "ieee1284_negotiate(3)"
name: "ieee1284_negotiate"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ieee1284_negotiate/"
description: "ieee1284_negotiate, ieee1284_terminate – IEEE 1284 negotiation"
---

<h2 class="name">NAME</h2>
<p> ieee1284_negotiate, ieee1284_terminate &#8211; IEEE 1284 negotiation </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ieee1284.h&gt;
</code></pre>
<dl>
<dt> <code>int ieee1284_negotiate(struct parport&nbsp;<wbr>*</code><i>port</i><code>, int&nbsp;<wbr></code><i>mode</i><code>);</code></p>
<dt> <code>void ieee1284_terminate(struct parport&nbsp;<wbr>*</code><i>port</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>These functions are for negotiating to and terminating from IEEE 1284 data transfer modes. The default mode is called compatibility mode, or in other words normal printer protocol. It is a host-to-peripheral mode only. There are special modes that allow peripheral-to-host transfer as well, which may be negotiated to using <code>ieee1284_negotiate</code>. IEEE 1284 negotiation is a process by which the host requests a transfer mode and the peripheral accepts or rejects it. An IEEE 1284-compliant device will require a successful negotiation to a particular mode before it is used for data transfer (but simpler devices may not if they only speak one transfer mode). </p>
<p> To terminate the special mode and go back to compatilibity mode use <code>ieee1284_terminate</code>. </p>
<p> These functions act on the parallel port associated with <i>port</i>, which must be claimed. </p>
<p> With a device strictly complying to IEEE 1284 you will need to call <code>ieee1284_terminate</code> in between any two calls to <code>ieee1284_negotiate</code> for modes other than <code>M1284_COMPAT</code>.</p>
<h2>AVAILABLE MODES</h2>
<h3>Uni-directional modes</h3>
<dl>
<dt>
<dd> &bull; <code>M1284_COMPAT</code>: Compatibility mode. Normal printer protocol. This is not a negotiated mode, but is the default mode in absence of negotiation. <code>ieee1284_negotiate(port, M1284_COMPAT)</code> is equivalent to <code>ieee1284_terminate(port)</code>. This host-to-peripheral mode is used for sending data to printers, and is historically the mode that has been used for that before IEEE 1284.</dl>
<dl>
<dt>
<dd> &bull; <code>M1284_NIBBLE</code>: Nibble mode. This peripheral-to-host mode uses the status lines to read data from the peripheral four bits at a time.</dl>
<dl>
<dt>
<dd> &bull; <code>M1284_BYTE</code>: Byte mode. This peripheral-to-host mode uses the data lines in reverse mode to read data from the peripheral a byte at a time.</dl>
<h3>Bi-directional modes</h3>
<dl>
<dt>
<dd> &bull; <code>M1284_ECP</code>: ECP mode. On entry to ECP mode it is a host-to-peripheral (i.e. forward) mode, but it may be set to reverse mode using <code><a href="/docs/linux/man/3-ieee1284_ecp_fwd_to_rev/">ieee1284_ecp_fwd_to_rev</a></code>(3). It is common for PC hardware to provide assistance with this mode by the use of a FIFO which the host (or, in reverse mode, the peripheral) may fill, so that the hardware can do the handshaking itself.</dl>
<dl>
<dt>
<dd> &bull; <code>M1284_EPP</code>: EPP mode. In this bi-directional mode the direction of data transfer is signalled at each byte.</dl>
<h3>Mode variations</h3>
<dl>
<dt>
<dd> &bull; <code>M1284_FLAG_DEVICEID</code>: Device ID retrieval. This flag may be combined with a nibble, byte, or ECP mode to notify the device that it should send its IEEE 1284 Device ID when asked for data.</dl>
<dl>
<dt>
<dd> &bull; <code>M1284_BECP</code>: Bounded ECP is a modification to ECP that makes it more robust at the point that the direction is changed. (Unfortunately it is not yet implemented in the Linux kernel driver.)</dl>
<dl>
<dt>
<dd> &bull; <code>M1284_ECPRLE</code>: ECP with run length encoding. In this mode, consecutive data bytes of the same value may be transferred in only a few cycles.</dl>
<h2>RETURN VALUE</h2>
<p> <code>E1284_OK</code></p>
<dl>
<dt>
<dd> The negotiation was successful.</dl>
<p> <code>E1284_NOTAVAIL</code></p>
<dl>
<dt>
<dd> Negotiation is not available with this port type.</dl>
<p> <code>E1284_REJECTED</code></p>
<dl>
<dt>
<dd> Negotiation was rejected by the peripheral.</dl>
<p> <code>E1284_NEGFAILED</code></p>
<dl>
<dt>
<dd> Negotiation failed for some reason. Perhaps the device is not IEEE 1284 compliant.</dl>
<p> <code>E1284_SYS</code></p>
<dl>
<dt>
<dd> A system error occured during negotiation.</dl>
<p> <code>E1284_INVALIDPORT</code></p>
<dl>
<dt>
<dd> The <i>port</i> parameter is invalid (for instance, perhaps the <i>port</i> is not claimed).</dl>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2003 Tim Waugh </p>
<h2>Index</h2>
