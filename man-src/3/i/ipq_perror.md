---
title: "ipq_perror(3)"
name: "ipq_perror"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ipq_perror/"
description: "ipq_errstr, ipq_perror — libipq error handling routines"
---

<h2 class="name">NAME</h2>
<p> ipq_errstr, ipq_perror &#8212; libipq error handling routines </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/linux/netfilter.h">linux/netfilter.h</a>&gt;</code><br />
 <code>#include &lt;<a href="file:/usr/include/libipq.h">libipq.h</a>&gt;</code> </p>
<p> <code>char *ipq_errstr(</code><i>void</i><code>);</code><br />
 <code>void ipq_perror(const char *</code><i>s</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>ipq_errstr</code> function returns a descriptive error message based on the current value of the internal <code>ipq_errno</code> variable. All libipq API functions set this internal variable upon failure. </p>
<p> The <code>ipq_perror</code> function prints an error message to stderr corresponding to the current value of the internal <code>ipq_error</code> variable, and the global <code>errno</code> variable (if set). The error message is prefixed with the string <i>s</i> as supplied by the application. If <i>s</i> is NULL, the error message is prefixed with the string &quot;ERROR&quot;.</p>
<h2>RETURN VALUE</h2>
<p> <code>ipq_errstr</code> returns an error message as outlined above.</p>
<h2>BUGS</h2>
<p> None known.</p>
<h2>AUTHOR</h2>
<p> James Morris &lt;jmorris [at] intercode.com.au&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2001 Netfilter Core Team. </p>
<p> Distributed under the GNU General Public License.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8), <code><a href="/docs/linux/man/3-libipq/">libipq</a></code>(3). </p>
<h2>Index</h2>
