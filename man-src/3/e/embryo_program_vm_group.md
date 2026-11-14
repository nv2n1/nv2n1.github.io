---
title: "embryo_program_vm_group(3)"
name: "embryo_program_vm_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-embryo_program_vm_group/"
description: "Virtual Machine Functions – Functions that deal with creating and destroying virtual machine sessions for a given program."
---

<p>Virtual Machine Functions &#8211; Functions that deal with creating and destroying virtual machine sessions for a given program. </p>
<h3>Functions</h3>
<p>EAPI void <code>embryo_program_vm_reset</code> (Embryo_Program *ep)<br />
 <i>Resets the current virtual machine session of the given program. </i><br />
 EAPI void <code>embryo_program_vm_push</code> (Embryo_Program *ep)<br />
 <i>Starts a new virtual machine session for the given program. </i><br />
 EAPI void <code>embryo_program_vm_pop</code> (Embryo_Program *ep)<br />
 <i>Frees the current virtual machine session associated with the given program. </i></p>
<h2>Detailed Description</h2>
<p>Functions that deal with creating and destroying virtual machine sessions for a given program. </p>
<p> A given embryo program can have multiple virtual machine sessions running. This is useful when you have a native call that in turn calls a function in the embryo program. The native call can start a new virtual machine session to run the function it needs. Once completed, the session can be popped off the program&#8217;s stack, and the native call can return its value to the old session. </p>
<p> A new virtual machine session is created by pushing a new virtual machine onto the session stack of a program using <code>embryo_program_vm_push</code>. The current virtual machine session can be destroyed by calling <code>embryo_program_vm_pop</code>.</p>
<h2>Function Documentation</h2>
<h3>EAPI void embryo_program_vm_pop (Embryo_Program * ep)</h3>
<p>Frees the current virtual machine session associated with the given program. </p>
<p> See <code>Virtual Machine Functions</code> for more information about how this works. Note that you will need to retrieve any return data or data on the stack before you pop. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The given program.</dl>
<h3>EAPI void embryo_program_vm_push (Embryo_Program * ep)</h3>
<p>Starts a new virtual machine session for the given program. </p>
<p> See <code>Virtual Machine Functions</code> for more information about how this works. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The given program.</dl>
<p> References embryo_program_vm_reset().</p>
<h3>EAPI void embryo_program_vm_reset (Embryo_Program * ep)</h3>
<p>Resets the current virtual machine session of the given program. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The given program.</dl>
<p> Referenced by embryo_program_vm_push().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Embryo from the source code.</p>
