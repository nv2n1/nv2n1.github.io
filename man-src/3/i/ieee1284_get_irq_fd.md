---
title: "ieee1284_get_irq_fd(3)"
name: "ieee1284_get_irq_fd"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ieee1284_get_irq_fd/"
description: "ieee1284_get_irq_fd, ieee1284_clear_irq – interrupt notification"
---

<h2 class="name">NAME</h2>
<p> ieee1284_get_irq_fd, ieee1284_clear_irq &#8211; interrupt notification </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ieee1284.h&gt;
</code></pre>
<dl>
<dt> <code>int ieee1284_get_irq_fd(struct parport&nbsp;<wbr>*</code><i>port</i><code>);</code></p>
<dt> <code>int ieee1284_clear_irq(struct parport&nbsp;<wbr>*</code><i>port</i><code>, unsigned int&nbsp;<wbr>*</code><i>count</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>If the <i>port</i> has a configured interrupt line and the port type supports interrupt notification, it is possible to obtain a file descriptor that may be used for <code><a href="/docs/linux/man/2-select/">select</a></code>(2) or <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2). Any event (readable, writable or exception) means that an interrupt has been triggered. No operations other than <code>select</code> or <code>poll</code> may be performed on the file descriptor. </p>
<p> The port must be open in order to call <code>ieee1284_get_irq_fd</code>, and must be claimed when using <code>select</code> or <code>poll</code>. </p>
<p> The caller must not close the file descriptor, and may not use it at all when the port is not claimed. </p>
<p> When an interrupt has been detected, the caller must call <code>ieee1284_clear_irq</code> to clear the interrupt condition, at which point the number of interrupts raised can be obtained by supplying a non-<code>NULL</code><i>count</i>.</p>
<h2>RETURN VALUE</h2>
<p> For <code>ieee1284_get_irq_fd</code>: If the return value is negative then it is an error code listed below. Otherwise it is a valid file descriptor. </p>
<p> <code>E1284_NOTAVAIL</code></p>
<dl>
<dt>
<dd> No such file descriptor is available.</dl>
<p> <code>E1284_INVALIDPORT</code></p>
<dl>
<dt>
<dd> The <i>port</i> parameter is invalid (for instance, perhaps the <i>port</i> is not open).</dl>
<p> For <code>ieee1284_clear_irq</code>: </p>
<p> <code>E1284_OK</code></p>
<dl>
<dt>
<dd> The interrupt has been cleared. If <i>count</i> was not <code>NULL</code> the count of interrupts has been atomically stored to <i>count</i> and reset.</dl>
<p> <code>E1284_NOTAVAIL</code></p>
<dl>
<dt>
<dd> The <i>count</i> parameter was not <code>NULL</code> but interrupt counting is not supported on this type of port. The interrupt has been cleared.</dl>
<p> <code>E1284_SYS</code></p>
<dl>
<dt>
<dd> There was a problem clearing the interrupt.</dl>
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
