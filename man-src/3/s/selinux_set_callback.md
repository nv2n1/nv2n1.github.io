---
title: "selinux_set_callback(3)"
name: "selinux_set_callback"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selinux_set_callback/"
description: "selinux_set_callback – userspace SELinux callback facilities"
---

<p>selinux_set_callback &#8211; userspace SELinux callback facilities</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;
void selinux_set_callback(int type, union selinux_callback callback);</code></pre>
<h2>Description</h2>
<p><code>selinux_set_callback</code>() sets the callback indicated by <i>type</i> to the value of <i>callback</i>, which should be passed as a function pointer cast to type <code>union</code> <code>selinux_callback</code>. </p>
<p> All callback functions should return a negative value with <i>errno</i> set appropriately on error. </p>
<p> The available values for <i>type</i> are:</p>
<dl>
<dt><code>SELINUX_CB_LOG</code></p>
<dd><code>int (*</code><i>func_log</i><code>) (int </code><i>type</i><code>, const char *</code><i>fmt</i><code>, &#8230;);</code> </p>
<p> This callback is used for logging and should process the <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) style <i>fmt</i> string and arguments as appropriate. The <i>type</i> argument indicates the type of message and will be set to one of the following: </p>
<p> <code>SELINUX_ERROR</code> </p>
<p> <code>SELINUX_WARNING</code> </p>
<p> <code>SELINUX_INFO</code> </p>
<p> <code>SELINUX_AVC</code></p>
<dt><code>SELINUX_CB_AUDIT</code></p>
<dd><code>int (*</code><i>func_audit</i><code>) (void *</code><i>auditdata</i><code>, security_class_t </code><i>cls</i><code>,</code> <code>char *</code><i>msgbuf</i><code>, size_t </code><i>msgbufsize</i><code>);</code> </p>
<p> This callback is used for supplemental auditing in AVC messages. The <i>auditdata</i> and <i>cls</i> arguments are the values passed to <code><a href="/docs/linux/man/3-avc_has_perm/">avc_has_perm</a></code>(3). A human-readable interpretation should be printed to <i>msgbuf</i> using no more than <i>msgbufsize</i> characters.</p>
<dt><code>SELINUX_CB_VALIDATE</code></p>
<dd><code>int (*</code><i>func_validate</i><code>) (char **</code><i>ctx</i><code>);</code> </p>
<p> This callback is used for context validation. The callback may optionally modify the input context by setting the target of the <i>ctx</i> pointer to a new context. In this case, the old value should be freed with <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3). The value of <i>errno</i> should be set to <code>EINVAL</code> to indicate an invalid context.</p>
<dt><code>SELINUX_CB_SETENFORCE</code></p>
<dd><code>int (*</code><i>func_setenforce</i><code>) (int </code><i>enforcing</i><code>);</code> </p>
<p> This callback is invoked when the system enforcing state changes. The <i>enforcing</i> argument indicates the new value and is set to <i>1</i> for enforcing mode, and <i>0</i> for permissive mode.</p>
<dt><code>SELINUX_CB_POLICYLOAD</code></p>
<dd><code>int (*</code><i>func_policyload</i><code>) (int </code><i>seqno</i><code>);</code> </p>
<p> This callback is invoked when the system security policy is reloaded. The <i>seqno</i> argument is the current sequential number of the policy generation in the system.</dl>
<h2>Return Value</h2>
<p>None.</p>
<h2>Errors</h2>
<p>None.</p>
<h2>Author</h2>
<p>Eamon Walsh &lt;ewalsh [at] tycho.nsa.gov&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-selabel_open/">selabel_open</a></code>(3), <code><a href="/docs/linux/man/3-avc_init/">avc_init</a></code>(3), <code><a href="/docs/linux/man/3-avc_netlink_open/">avc_netlink_open</a></code>(3), <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
