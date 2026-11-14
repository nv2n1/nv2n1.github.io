---
title: "ieee1284_data_dir(3)"
name: "ieee1284_data_dir"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ieee1284_data_dir/"
description: "ieee1284_read_data, ieee1284_write_data, ieee1284_data_dir, ieee1284_wait_data – control the data lines"
---

<h2 class="name">NAME</h2>
<p> ieee1284_read_data, ieee1284_write_data, ieee1284_data_dir, ieee1284_wait_data &#8211; control the data lines </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ieee1284.h&gt;
</code></pre>
<dl>
<dt> <code>int ieee1284_read_data(struct parport&nbsp;<wbr>*</code><i>port</i><code>);</code></p>
<dt> <code>void ieee1284_write_data(struct parport&nbsp;<wbr>*</code><i>port</i><code>, unsigned char&nbsp;<wbr></code><i>dt</i><code>);</code></p>
<dt> <code>int ieee1284_data_dir(struct parport&nbsp;<wbr>*</code><i>port</i><code>, int&nbsp;<wbr></code><i>reverse</i><code>);</code></p>
<dt> <code>int ieee1284_wait_data(struct parport&nbsp;<wbr>*</code><i>port</i><code>, unsigned char&nbsp;<wbr></code><i>mask</i><code>, unsigned char&nbsp;<wbr></code><i>val</i><code>, struct timeval&nbsp;<wbr>*</code><i>timeout</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>These functions manipulate the data lines of the parallel port associated with <i>port</i> (which must have been claimed using <code><a href="/docs/linux/man/3-ieee1284_claim/">ieee1284_claim</a></code>(3)). The lines are represented by an 8-bit number (one line per bit) and a direction. The data lines are driven as a group; they may be all host-driven (forward direction) or not (reverse direction). When the peripheral is driving them the host must not. </p>
<p> For <code>ieee1284_data_dir</code> the <i>reverse</i> parameter should be zero to turn the data line drivers on and non-zero to turn them off. Some port types may be unable to switch off the data line drivers. </p>
<p> Setting the data lines may have side effects on some port types (for example, some Amiga ports pulse nStrobe). </p>
<p> <code>ieee1284_wait_data</code> waits, up until the <i>timeout</i>, for the data bits specified in <i>mask</i> to have the corresponding values in <i>val</i>.</p>
<h2>RETURN VALUE</h2>
<p> <code>ieee1284_read_data</code> returns the 8-bit number representing the data lines unless it is not possible to return such a value with this port type, in which case it returns an error code. Possible error codes: </p>
<p> <code>E1284_NOTAVAIL</code></p>
<dl>
<dt>
<dd> Bi-directional data lines are not available on this system.</dl>
<p> <code>E1284_INVALIDPORT</code></p>
<dl>
<dt>
<dd> The <i>port</i> parameter is invalid (perhaps it has not been claimed, for instance).</dl>
<p> <code>E1284_SYS</code></p>
<dl>
<dt>
<dd> There was an error at the operating system level, and <i>errno</i> has been set accordingly.</dl>
<p> <code>E1284_TIMEDOUT</code></p>
<dl>
<dt>
<dd> The <i>timeout</i> has elapsed.</dl>
<p> Whereas <code>ieee1284_read_data</code> may return <code>E1284_NOTAVAIL</code> on its first invocation on the port, if it does not do so then it cannot until <code>ieee1284_close</code> is called for that port.</p>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2003 Tim Waugh </p>
<h2>Index</h2>
