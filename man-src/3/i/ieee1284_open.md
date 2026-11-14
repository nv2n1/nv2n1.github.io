---
title: "ieee1284_open(3)"
name: "ieee1284_open"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ieee1284_open/"
description: "ieee1284_open – open a port"
---

<h2 class="name">NAME</h2>
<p> ieee1284_open &#8211; open a port </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ieee1284.h&gt;
</code></pre>
<dl>
<dt> <code>int ieee1284_open(struct parport&nbsp;<wbr>*</code><i>port</i><code>, int&nbsp;<wbr></code><i>flags</i><code>, int&nbsp;<wbr>*</code><i>capabilities</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>In order to begin using a port it must be opened. Any initial set-up of the port is done at this stage. When an open port is no longer needed it should be closed with <code><a href="/docs/linux/man/3-ieee1284_close/">ieee1284_close</a></code>(3). </p>
<p> The possible <i>flags</i> are: </p>
<p> <code>F1284_EXCL</code></p>
<dl>
<dt>
<dd> This device cannot share the port with any other device. If this is the case it must be declared at this stage, so that other drivers trying to access the port know not to bother; otherwise they will wait until this driver releases the port, i.e. never. </p>
<p> The iopl/dev-port access methods don&#8217;t support this yet, but the ppdev ones do.</dl>
<p> If <i>capabilities</i> is not <code>NULL</code> it must point to storage for an <code>int</code>, which will be treated as a set of flags, one per bit, which the library sets or clears as appropriate. If a capability is present it will be used when asked for. They are: </p>
<p> <code>CAP1284_RAW</code></p>
<dl>
<dt>
<dd> Pin-level access is available. If this capability is present then the following functions are effective: <code>ieee1284_write_data</code>, <code>ieee1284_read_status</code>, <code>ieee1284_wait_status</code>, <code>ieee1284_write_control</code>, <code>ieee1284_read_control</code>, <code>ieee1284_frob_control</code>.</dl>
<p> <code>CAP1284_NIBBLE</code></p>
<dl>
<dt>
<dd> There is an implementation of nibble mode for this port.</dl>
<p> <code>CAP1284_BYTE</code></p>
<dl>
<dt>
<dd> There is an implementation of byte mode for this port.</dl>
<p> <code>CAP1284_COMPAT</code></p>
<dl>
<dt>
<dd> There is an implementation of compatibility mode for this port.</dl>
<p> <code>CAP1284_ECP</code></p>
<dl>
<dt>
<dd> There is a hardware implementation of ECP mode for this port.</dl>
<p> <code>CAP1284_ECPRLE</code></p>
<dl>
<dt>
<dd> There is an RLE-aware implementation of ECP mode for this port (the <code>F1284_RLE</code> flag is recognised by the ECP transfer functions).</dl>
<p> <code>CAP1284_ECPSWE</code></p>
<dl>
<dt>
<dd> There is a software implementation of ECP mode for this port.</dl>
<p> <code>CAP1284_BECP</code></p>
<dl>
<dt>
<dd> There is an implementation of bounded ECP mode for this port.</dl>
<p> <code>CAP1284_EPP</code></p>
<dl>
<dt>
<dd> There is a hardware implementation of EPP mode for this port.</dl>
<p> <code>CAP1284_EPPSWE</code></p>
<dl>
<dt>
<dd> There is a software implementation of EPP mode for this port.</dl>
<p> <code>CAP1284_IRQ</code></p>
<dl>
<dt>
<dd> An interrupt line is configured for this port and interrupt notifications can be received using <code><a href="/docs/linux/man/3-ieee1284_get_irq_fd/">ieee1284_get_irq_fd</a></code>(3).</dl>
<p> <code>CAP1284_DMA</code></p>
<dl>
<dt>
<dd> A DMA channel is configured for this port.</dl>
<h2>RETURN VALUE</h2>
<p> <code>E1284_OK</code></p>
<dl>
<dt>
<dd> The port is now opened.</dl>
<p> <code>E1284_INIT</code></p>
<dl>
<dt>
<dd> There was a problem during port initialization. This could be because another driver has opened the port exclusively, or some other reason.</dl>
<p> <code>E1284_NOMEM</code></p>
<dl>
<dt>
<dd> There is not enough memory.</dl>
<p> <code>E1284_NOTAVAIL</code></p>
<dl>
<dt>
<dd> One or more of the supplied flags is not supported by this type of port.</dl>
<p> <code>E1284_INVALIDPORT</code></p>
<dl>
<dt>
<dd> The <i>port</i> parameter is invalid (for instance, the <i>port</i> may already be open).</dl>
<p> <code>E1284_SYS</code></p>
<dl>
<dt>
<dd> There was a problem at the operating system level. The global variable <i>errno</i> has been set appropriately.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ieee1284_close/">ieee1284_close</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2003 Tim Waugh </p>
<h2>Index</h2>
