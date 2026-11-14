---
title: "stdsig_atomic_t(3)"
name: "stdsig_atomic_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsig_atomic_t/"
---

std::sig_atomic_t - std::sig_atomic_t

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;csignal&gt;

typedef /* unspecified */ sig_atomic_t;</code></pre> 
An integer type which can be accessed as an atomic entity even in the presence of asynchronous interrupts made by signals. 

<h2>Notes</h2>

Until C++11, which introduced std::atomic and std::atomic_signal_fence, about the only thing a strictly conforming program could do in a signal handler was to assign a value to a volatile static std::sig_atomic_t variable and promptly return. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets a signal handler for particular signal 
signal <i>(function)</i> 
atomic_signal_fence fence between a thread and a signal handler executed in the same thread 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
