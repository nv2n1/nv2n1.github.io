---
title: "audit_request_signal_info(3)"
name: "audit_request_signal_info"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audit_request_signal_info/"
description: "audit_request_signal_info – Request signal info for the audit system"
---

<h2>NAME</h2>
<p> audit_request_signal_info &#8211; Request signal info for the audit system</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libaudit.h&gt;</code> </p>
<p> int audit_request_signal_info(int fd); </p>
<h2>DESCRIPTION</h2>
<p> audit_request_signal_info requests that the kernel send information about the sender of a signal to the audit daemon. The sinal info structure is as follows: </p>
<pre><code>
struct audit_sig_info {
    uid_t uid;
    pid_t pid;
    char ctx[0];
};
</code></pre>
<p> This function is likely to be used only by audit daemons and shouldn&#8217;t be called by any other kind of program. </p>
<h2>RETURN VALUE</h2>
<p> The return value is &lt;= 0 on error, otherwise it is the netlink sequence id number. This function can have any error that sendto would encounter. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-audit_open/">audit_open</a></code>(3), <code><a href="/docs/linux/man/3-audit_get_reply/">audit_get_reply</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
