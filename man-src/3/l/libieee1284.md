---
title: "libieee1284(3)"
name: "libieee1284"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libieee1284/"
description: "libieee1284 – IEEE1284 communications library"
---

<h2 class="name">NAME</h2>
<p> libieee1284 &#8211; IEEE1284 communications library </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ieee1284.h&gt;
cc files... - lieee1284
</code></pre>
<h2>OVERVIEW</h2>
<p> The libieee1284 library is a library for accessing parallel port devices. </p>
<p> The model presented to the user is fairly abstract: a list of parallel ports with arbitrary names, with functions to access them in various ways ranging from bit operations to block data transfer in one of the IEEE 1284 sanctioned protocols. </p>
<p> Although the library resides in user space the speed penalty may not be as bad as you initially think, since the operating system may well provide assistance with block data transfer operations; in fact, the operating system may even use hardware assistance to get the job done. So, using libieee1284, ECP transfers using DMA are possible. </p>
<p> The normal sequence of events will be that the application </p>
<dl>
<dt>
<dd> 1. calls <code>ieee1284_find_ports</code> to get a list of available ports</dl>
<dl>
<dt>
<dd> 2. then <code>ieee1284_get_deviceid</code> to look for a device on each port that it is interested in</dl>
<dl>
<dt>
<dd> 3. and then <code>ieee1284_open</code> to open each port it finds a device it can control on.</dl>
<dl>
<dt>
<dd> 4. The list of ports returned from <code>ieee1284_find_ports</code> can now be disposed of using <code>ieee1284_free_ports</code>.</dl>
<dl>
<dt>
<dd> 5. Then when it wants to control the device, it will call <code>ieee1284_claim</code> to prevent other drivers from using the port</dl>
<dl>
<dt>
<dd> 6. then perhaps do some data transfers</dl>
<dl>
<dt>
<dd> 7. and then <code>ieee1284_release</code> when it is finished that that particular command. This claim-control-release sequence will be repeated each time it wants to tell the device to do something.</dl>
<dl>
<dt>
<dd> 8. Finally when the application is finished with the device it will call <code>ieee1284_close</code>.</dl>
<p> Usually a port needs to be claimed before it can be used. This is to prevent multiple drivers from trampling on each other if they both want to use the same port. The exception to this rule is the collection of IEEE 1284 Device IDs, which has an implicit open-claim-release-close sequence. The reason for this is that it may be possible to collect a Device ID from the operating system, without bothering the device with it.</p>
<h2>CONFIGURATION</h2>
<p> When <code>ieee1284_find_ports</code> is first called, the library will look for a configuration file, /etc/ieee1284.conf. </p>
<p> Comments begin with a &#8216;#&#8217; character and extend to the end of the line. Everything else is freely-formatted tokens. A non-quoted (or double-quoted) backslash character &#8216;\&#8217; preserves the literal value of the next character, and single and double quotes may be used for preserving white-space. Braces and equals signs are recognised as tokens, unless quoted or escaped. </p>
<p> The only configuration instruction that is currently recognised is &#8220;disallow method ppdev&#8221;, for preventing the use of the Linux ppdev driver.</p>
<h2>ENVIRONMENT</h2>
<p> You can enable debugging output from the library by setting the environment variable <code>LIBIEEE1284_DEBUG</code> to any value.</p>
<h2>FILES</h2>
<p> /etc/ieee1284.conf</p>
<dl>
<dt>
<dd> Configuration file.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-parport/">parport</a>(3), <a href="/docs/linux/man/3-parport_list/">parport_list</a>(3), <a href="/docs/linux/man/3-ieee1284_find_ports/">ieee1284_find_ports</a>(3), <a href="/docs/linux/man/3-ieee1284_free_ports/">ieee1284_free_ports</a>(3), <a href="/docs/linux/man/3-ieee1284_get_deviceid/">ieee1284_get_deviceid</a>(3), <a href="/docs/linux/man/3-ieee1284_open/">ieee1284_open</a>(3), <a href="/docs/linux/man/3-ieee1284_close/">ieee1284_close</a>(3), <a href="/docs/linux/man/3-ieee1284_claim/">ieee1284_claim</a>(3), <a href="/docs/linux/man/3-ieee1284_release/">ieee1284_release</a>(3), <a href="/docs/linux/man/3-ieee1284_data/">ieee1284_data</a>(3), <a href="/docs/linux/man/3-ieee1284_status/">ieee1284_status</a>(3), <a href="/docs/linux/man/3-ieee1284_control/">ieee1284_control</a>(3), <a href="/docs/linux/man/3-ieee1284_negotiation/">ieee1284_negotiation</a>(3), <a href="/docs/linux/man/3-ieee1284_ecp_fwd_to_rev/">ieee1284_ecp_fwd_to_rev</a>(3), <a href="/docs/linux/man/3-ieee1284_transfer/">ieee1284_transfer</a>(3), <a href="/docs/linux/man/3-ieee1284_get_irq_fd/">ieee1284_get_irq_fd</a>(3), <a href="/docs/linux/man/3-ieee1284_set_timeout/">ieee1284_set_timeout</a>(3)</p>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2003 Tim Waugh </p>
<h2>Index</h2>
