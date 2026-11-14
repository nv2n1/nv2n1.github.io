---
title: "stdjmp_buf(3)"
name: "stdjmp_buf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdjmp_buf/"
---

std::jmp_buf - std::jmp_buf

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;csetjmp&gt;

typedef /* unspecified */ jmp_buf;</code></pre> 
The std::jmp_buf type is an array type suitable for storing information to restore a calling environment. The stored information is sufficient to restore execution at the correct block of the program and invocation of that block. The state of floating-point status flags, or open files, or any other data is not stored in an object of type jmp_buf. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;saves the context 
setjmp <i>(function macro)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;jumps to specified location 
longjmp <i>(function)</i> 
