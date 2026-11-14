---
title: "pam_faildelay(8)"
name: "pam_faildelay"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_faildelay/"
description: "pam_faildelay – Change the delay on failure per-application"
---

<p>pam_faildelay &#8211; Change the delay on failure per-application</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_faildelay.so</code> [debug] [delay=<i>microseconds</i>]</dl>
<h2>Description</h2>
<dd>pam_faildelay is a PAM module that can be used to set the delay on failure per-application. </p>
<p> If no <code>delay</code> is given, pam_faildelay will use the value of FAIL_DELAY from /etc/login.defs.</p>
<h2>Options</h2>
<p><code>debug</code></p>
<dl>
<dd>Turns on debugging messages sent to syslog.</dl>
<p> <code>delay=</code><i>N</i></p>
<dl>
<dd>Set the delay on failure to N microseconds.</dl>
<h2>Module Types Provided</h2>
<p>Only the <code>auth</code> module type is provided.</p>
<h2>Return Values</h2>
<p>PAM_IGNORE</p>
<dl>
<dd>Delay was successful adjusted.</dl>
<p> PAM_SYSTEM_ERR</p>
<dl>
<dd>The specified delay was not valid.</dl>
<h2>Examples</h2>
<p>The following example will set the delay on failure to 10 seconds:</p>
<dl>
<dd>
<pre>auth optional pam_faildelay.so delay=10000000</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam_fail_delay/">pam_fail_delay</a></code>(3), <code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_faildelay was written by Darren Tucker &lt;dtucker [at] zip.com.au&gt;.</p>
