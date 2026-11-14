---
title: "swapcontext(2)"
name: "swapcontext"
section: "2"
letter: "s"
url: "/docs/linux/man/2-swapcontext/"
description: "swapcontext – Swap out old context with new context"
---

<h2>NAME</h2>
<p> swapcontext &#8211; Swap out old context with new context</p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>int&nbsp;<wbr><code>sys_swapcontext</code>&nbsp;<wbr>(struct ucontext&nbsp;<wbr><i>*old_ctx</i>, struct ucontext&nbsp;<wbr><i>*new_ctx</i>, int&nbsp;<wbr><i>r5</i>, int&nbsp;<wbr><i>r6</i>, int&nbsp;<wbr><i>r7</i>, int&nbsp;<wbr><i>r8</i>, struct pt_regs&nbsp;<wbr><i>*regs</i>); </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>swapcontext</code> swaps out context <i>old_ctx</i> with new context <i>new_ctx</i>. The <i>int r#</i> values have no place in the system call functionality. The <i>regs</i> value indicates the current user register values from the user stack. </p>
<h2>RETURN VALUE</h2>
<p> <code>swapcontext</code> returns 0 on success; otherwise, <code>swapcontext</code> returns one of the errors listed in the &quot;Errors&quot; section. </p>
<h2>ERRORS</h2>
<dl>
<dt>-EFAULT</p>
<dd> <i>swapcontext</i> could not verify that the memory area pointed to by <i>old_ctx</i> or <i>new_ctx</i> was accessible for the operation. </p>
<dt>-SIGSEGV</p>
<dd> A fault occurred when the context was being copied into the kernel&#8217;s image of the user&#8217;s registers. The should only occur in an out-of-memory situation. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-getcontext/">getcontext</a>(2),</code> <code><a href="/docs/linux/man/2-sigaction/">sigaction</a>(2),</code> <code><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a>(2),</code> <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a>(2)</code> </p>
<h2>AUTHOR</h2>
<p> Niki Rahimi </p>
<h2>Index</h2>
