---
title: "call_usermodehelper_setup(9)"
name: "call_usermodehelper_setup"
section: "9"
letter: "c"
url: "/docs/linux/man/9-call_usermodehelper_setup/"
description: "call_usermodehelper_setup – prepare to call a usermode helper"
---

<p>call_usermodehelper_setup &#8211; prepare to call a usermode helper</p>
<h2>Synopsis</h2>
<pre><code>struct subprocess_info *call_usermodehelper_setup(char *path, char **argv, char **envp, gfp_t gfp_mask, int (*init)(struct subprocess_info *info, struct cred *new), void (*cleanup)(struct subprocess_info *info), void *data);</code></pre>
<h2>Arguments</h2>
<p><i>path</i></p>
<dl>
<dd>
<dd>path to usermode executable</dl>
<p> <i>argv</i></p>
<dl>
<dd>arg vector for process</dl>
<p> <i>envp</i></p>
<dl>
<dd>environment for process</dl>
<p> <i>gfp_mask</i></p>
<dl>
<dd>gfp mask for memory allocation</dl>
<p> <i>init</i></p>
<dl>
<dd>an init function</dl>
<p> <i>cleanup</i></p>
<dl>
<dd>a cleanup function</dl>
<p> <i>data</i></p>
<dl>
<dd>arbitrary context sensitive data</dl>
<h2>Description</h2>
<p>Returns either <code>NULL</code> on allocation failure, or a subprocess_info structure. This should be passed to call_usermodehelper_exec to exec the process and free the structure. </p>
<p> The init function is used to customize the helper process prior to exec. A non-zero return code causes the process to error out, exit, and return the failure to the calling process </p>
<p> The cleanup function is just before ethe subprocess_info is about to be freed. This can be used for freeing the argv and envp. The Function must be runnable in either a process context or the context in which call_usermodehelper_exec is called.</p>
<h2>Copyright</h2>
