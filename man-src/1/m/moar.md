---
title: "moar(1)"
name: "moar"
section: "1"
letter: "m"
url: "/docs/linux/man/1-moar/"
---

<h2 class="name">NAME</h2>
 

 moar - a runtime for Perl 6 

<h2>SYNOPSIS</h2>

 <pre><code>
moar-- version
    moar[--dump][--crash][--libpath = ...][--full - cleanup] inputfile
</code></pre>

<h2>DESCRIPTION</h2>

 <tt>&quot;moar&quot;</tt> is the binary of MoarVM, (short for Metamodel On A Runtime Virtual Machine). It can be used to execute <tt>&quot;.moarvm&quot;</tt> bytecode files.

<h2>ENVIRONMENT VARIABLES</h2>

 moar respects the following environment variables:
<dl>
<dt><font SIZE="-1">MVM_JIT_DISABLE</font>
<dd> Disables the just-in-time compiler (<font SIZE="-1">JIT</font>). This is ignored if MoarVM was built without <font SIZE="-1">JIT</font> support.
<dt><font SIZE="-1">MVM_SPESH_DISABLE</font>
<dd> Disables the runtime bytecode specializer / optimizer.
<dt><font SIZE="-1">MVM_SPESH_INLINE_DISABLE</font>
<dd> Disables inlining of call frames inside the bytecode specializer.
<dt><font SIZE="-1">MVM_SPESH_OSR_DISABLE</font>
<dd> Disables the on-stack replacement feature of the bytecode specializer.
<dt><font SIZE="-1">MVM_CROSS_THREAD_WRITE_LOG</font>
<dd> Tells MoarVM to insert instrumentation to detect when a thread does a write to an object it didn't allocate and doesn't have a lock for.
<dt><font SIZE="-1">MVM_CROSS_THREAD_WRITE_LOG_INCLUDE_LOCKED</font>
<dd> Same as <font SIZE="-1">MVM_CROSS_THREAD_WRITE_LOG,</font> except objects that are locked are included as well.</dl>

<h2>REPORTING BUGS</h2>

 Please use the issue tracker at &lt;<a rel="nofollow" HREF="https://github.com/moarvm/moarvm/issues">https://github.com/moarvm/moarvm/issues</a>&gt; to report bugs.

<h2>COPYRIGHT</h2>

 Copyright (C) 2012-2014 by the MoarVM contributors. See the <i></i><font SIZE="-1"><i>CREDITS</i></font><i></i> file for a list of contributors. 

 License: Artistic License 2.0. See the file <i>Artistic2.txt</i> for more information. 

<h2>Index</h2>


