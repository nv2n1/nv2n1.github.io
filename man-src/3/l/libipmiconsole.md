---
title: "libipmiconsole(3)"
name: "libipmiconsole"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libipmiconsole/"
description: "libipmiconsole – IPMI SOL library"
---

<h2>NAME</h2>
<p> libipmiconsole &#8211; IPMI SOL library</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;ipmiconsole.h&gt;</code> </p>
<p> <code>int ipmiconsole_engine_init(unsigned int thread_count, unsigned int debug_flags);</code> </p>
<p> <code>int ipmiconsole_engine_submit(ipmiconsole_ctx_t c, Ipmiconsole_callback callback, void *callback_arg);</code> </p>
<p> <code>int ipmiconsole_engine_submit_block(ipmiconsole_ctx_t c);</code> </p>
<p> <code>void ipmiconsole_engine_teardown(int cleanup_sol_sessions);</code> </p>
<p> <code>ipmiconsole_ctx_t ipmiconsole_ctx_create(char *hostname, struct ipmiconsole_ipmi_config *ipmi_config, struct ipmiconsole_protocol_config *protocol_config);</code> </p>
<p> <code>int ipmiconsole_ctx_errnum(ipmiconsole_ctx_t c);</code> </p>
<p> <code>char *ipmiconsole_ctx_strerror(int errnum);</code> </p>
<p> <code>ipmiconsole_ctx_status_t ipmiconsole_ctx_status(ipmiconsole_ctx_t c);</code> </p>
<p> <code>int ipmiconsole_ctx_fd(ipmiconsole_ctx_t c);</code> </p>
<p> <code>int ipmiconsole_ctx_generate_break(ipmiconsole_ctx_t c);</code> </p>
<p> <code>int ipmiconsole_ctx_destroy(ipmiconsole_ctx_t c);</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>Libipmiconsole</code> implements a high level serial-over-lan (SOL) API for remote console access. It can be used to establish and manage multiple IPMI 2.0 SOL sessions. The goal of this library is to abstract away all of the underlying IPMI/SOL details away from the user into a relatively simple file descriptor interface.</p>
<h2>FILES</h2>
<p> /usr/include/ipmiconsole.h</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2007-2012 Lawrence Livermore National Security, LLC.<br />
 Copyright (C) 2006-2007 The Regents of the University of California. </p>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-ipmiconsole/">ipmiconsole</a>(8) </p>
<p> <a rel="nofollow" href="http://www.gnu.org/software/freeipmi/">http://www.gnu.org/software/freeipmi/</a> </p>
<h2>Index</h2>
