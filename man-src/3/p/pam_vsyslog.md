---
title: "pam_vsyslog(3)"
name: "pam_vsyslog"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_vsyslog/"
description: "pam_syslog, pam_vsyslog – send messages to the system logger"
---

<p>pam_syslog, pam_vsyslog &#8211; send messages to the system logger</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_ext.h&gt;
#include &lt;syslog.h&gt;

void pam_syslog(pam_handle_t *pamh, int priority, const char *fmt, ...);

void pam_vsyslog(pam_handle_t *pamh, int priority, const char *fmt, va_list args);</code></pre>
<h2>Description</h2>
<dd>The <code>pam_syslog</code> function logs messages using <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) and is intended for internal use by Linux-PAM and PAM service modules. The <i>priority</i> argument is formed by ORing the facility and the level values as documented in the <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) manual page. </p>
<p> The <code>pam_vsyslog</code> function performs the same task as <code>pam_syslog()</code> with the difference that it takes a set of arguments which have been obtained using the <code><a href="/docs/linux/man/3-stdarg/">stdarg</a></code>(3) variable argument list macros.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam/">pam</a></code>(8)</p>
<h2>Standards</h2>
<p>The <code>pam_syslog</code> and <code>pam_vsyslog</code> functions are Linux-PAM extensions.</p>
