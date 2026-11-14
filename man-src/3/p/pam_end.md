---
title: "pam_end(3)"
name: "pam_end"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_end/"
description: "pam_end – termination of PAM transaction"
---

<p>pam_end &#8211; termination of PAM transaction</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_appl.h&gt;

int pam_end(pam_handle_t *pamh, int pam_status);</code></pre>
<h2>Description</h2>
<dd>The <code>pam_end</code> function terminates the PAM transaction and is the last function an application should call in the PAM context. Upon return the handle <i>pamh</i> is no longer valid and all memory associated with it will be invalid. </p>
<p> The <i>pam_status</i> argument should be set to the value returned to the application by the last PAM library call. </p>
<p> The value taken by <i>pam_status</i> is used as an argument to the module specific callback function, <code>cleanup()</code> (See <code><a href="/docs/linux/man/3-pam_set_data/">pam_set_data</a></code>(3) and <code><a href="/docs/linux/man/3-pam_get_data/">pam_get_data</a></code>(3)). In this way the module can be given notification of the pass/fail nature of the tear-down process, and perform any last minute tasks that are appropriate to the module before it is unlinked. This argument can be logically OR&#8217;d with <i>PAM_DATA_SILENT</i> to indicate to indicate that the module should not treat the call too seriously. It is generally used to indicate that the current closing of the library is in a <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2)ed process, and that the parent will take care of cleaning up things that exist outside of the current process space (files etc.). </p>
<p> This function <i>free</i>&#8216;s all memory for items associated with the <code><a href="/docs/linux/man/3-pam_set_item/">pam_set_item</a></code>(3) and <code><a href="/docs/linux/man/3-pam_get_item/">pam_get_item</a></code>(3) functions. Pointers associated with such objects are not valid anymore after <code>pam_end</code> was called.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>Transaction was successful terminated.</dl>
<p> PAM_SYSTEM_ERR</p>
<dl>
<dd>System error, for example a NULL pointer was submitted as PAM handle or the function was called by a module.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam_get_data/">pam_get_data</a></code>(3), <code><a href="/docs/linux/man/3-pam_set_data/">pam_set_data</a></code>(3), <code><a href="/docs/linux/man/3-pam_start/">pam_start</a></code>(3), <code><a href="/docs/linux/man/3-pam_strerror/">pam_strerror</a></code>(3) </p>
