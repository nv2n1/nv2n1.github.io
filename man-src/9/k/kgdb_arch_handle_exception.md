---
title: "kgdb_arch_handle_exception(9)"
name: "kgdb_arch_handle_exception"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kgdb_arch_handle_exception/"
description: "kgdb_arch_handle_exception – Handle architecture specific GDB packets."
---

<p>kgdb_arch_handle_exception &#8211; Handle architecture specific GDB packets.</p>
<h2>Synopsis</h2>
<pre><code>int kgdb_arch_handle_exception(int vector, int signo, int err_code, char *remcom_in_buffer, char *remcom_out_buffer, struct pt_regs *regs);</code></pre>
<h2>Arguments</h2>
<p><i>vector</i></p>
<dl>
<dd>
<dd>The error vector of the exception that happened.</dl>
<p> <i>signo</i></p>
<dl>
<dd>The signal number of the exception that happened.</dl>
<p> <i>err_code</i></p>
<dl>
<dd>The error code of the exception that happened.</dl>
<p> <i>remcom_in_buffer</i></p>
<dl>
<dd>The buffer of the packet we have read.</dl>
<p> <i>remcom_out_buffer</i></p>
<dl>
<dd>The buffer of <code>BUFMAX</code> bytes to write a packet into.</dl>
<p> <i>regs</i></p>
<dl>
<dd>The struct pt_regs of the current process.</dl>
<h2>Description</h2>
<p>This function MUST handle the &#8216;c&#8217; and &#8216;s&#8217; command packets, as well packets to set / remove a hardware breakpoint, if used. If there are additional packets which the hardware needs to handle, they are handled here. The code should return -1 if it wants to process more packets, and a <code>0</code> or <code>1</code> if it wants to exit from the kgdb callback.</p>
<h2>Author</h2>
<p><code>Jason Wessel</code> &lt;jason.wessel [at] windriver.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
