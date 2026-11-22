---

title: "moar(1)"
name: "moar"
section: "1"
letter: "m"
url: "/docs/linux/man/1-moar/"
---

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
<dt>MVM_JIT_DISABLE
</dt><dd> Disables the just-in-time compiler (JIT). This is ignored if MoarVM was built without JIT support.
</dd><dt>MVM_SPESH_DISABLE
</dt><dd> Disables the runtime bytecode specializer / optimizer.
</dd><dt>MVM_SPESH_INLINE_DISABLE
</dt><dd> Disables inlining of call frames inside the bytecode specializer.
</dd><dt>MVM_SPESH_OSR_DISABLE
</dt><dd> Disables the on-stack replacement feature of the bytecode specializer.
</dd><dt>MVM_CROSS_THREAD_WRITE_LOG
</dt><dd> Tells MoarVM to insert instrumentation to detect when a thread does a write to an object it didn't allocate and doesn't have a lock for.
</dd><dt>MVM_CROSS_THREAD_WRITE_LOG_INCLUDE_LOCKED
</dt><dd> Same as MVM_CROSS_THREAD_WRITE_LOG, except objects that are locked are included as well.</dd></dl>

<h2>REPORTING BUGS</h2>

 Please use the issue tracker at &lt;<a rel="nofollow" HREF="https://github.com/moarvm/moarvm/issues">https://github.com/moarvm/moarvm/issues</a>&gt; to report bugs.

<h2>COPYRIGHT</h2>

 Copyright (C) 2012-2014 by the MoarVM contributors. See the <i></i><i>CREDITS</i><i></i> file for a list of contributors. 

 License: Artistic License 2.0. See the file <i>Artistic2.txt</i> for more information.
