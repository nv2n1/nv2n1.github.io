---
title: "ieee1284_ecp_fwd_to_rev(3)"
name: "ieee1284_ecp_fwd_to_rev"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ieee1284_ecp_fwd_to_rev/"
description: "ieee1284_ecp_fwd_to_rev, ieee1284_ecp_rev_to_fwd – ECP direction switching"
---

<h2 class="name">NAME</h2>
<p> ieee1284_ecp_fwd_to_rev, ieee1284_ecp_rev_to_fwd &#8211; ECP direction switching </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>int ieee1284_ecp_fwd_to_rev(struct parport&nbsp;<wbr>*</code><i>port</i><code>);</code></p>
<dt> <code>int ieee1284_ecp_rev_to_fwd(struct parport&nbsp;<wbr>*</code><i>port</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>These functions are used to switch directions when in ECP mode. On negotiation to ECP mode the direction is forward (in other words, host-to-peripheral). Use <code>ieee1284_ecp_fwd_to_rev</code> to switch from forward to reverse, and <code>ieee1284_ecp_rev_to_fwd</code> to switch from reverse to forward. </p>
<p> They act on the parallel port associated with <i>port</i>, which must be claimed.</p>
<h2>RETURN VALUE</h2>
<p> <code>E1284_OK</code></p>
<dl>
<dt>
<dd> Direction switched successfully.</dl>
<p> <code>E1284_NOTIMPL</code></p>
<dl>
<dt>
<dd> The <i>port</i> lacks the required capability. This could be due to a limitation of this version of libieee1284, or a hardware limitation.</dl>
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
