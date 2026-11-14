---
title: "execstack(8)"
name: "execstack"
section: "8"
letter: "e"
url: "/docs/linux/man/8-execstack/"
description: "execstack – tool to set, clear, or query executable stack flag of ELF binaries and shared libraries"
---

<p>execstack &#8211; tool to set, clear, or query executable stack flag of ELF binaries and shared libraries</p>
<h2>Synopsis</h2>
<p>execstack [OPTION&#8230;]&nbsp;<wbr>[FILES]</p>
<h2>Description</h2>
<p><code>execstack</code> is a program which sets, clears, or queries executable stack flag of ELF binaries and shared libraries. Linux has in the past allowed execution of instructions on the stack and there are lots of binaries and shared libraries assuming this behaviour. Furthermore, GCC trampoline code for e.g. nested functions requires executable stack on many architectures. To avoid breaking binaries and shared libraries which need executable stack, ELF binaries and shared libraries now can be marked as requiring executable stack or not requiring it. This marking is done through the p_flags field in the PT_GNU_STACK program header entry. If the marking is missing, kernel or dynamic linker need to assume it might need executable stack. The marking is done automatically by recent GCC versions (objects using trampolines on the stack are marked as requiring executable stack, all other newly built objects are marked as not requiring it) and linker collects these markings into marking of the whole binary or shared library. The user can override this at assembly time (through <code>&#8211;execstack</code> or <code>&#8211;noexecstack</code> assembler options), at link time (through <code>-z execstack</code> or <code>-z noexecstack</code> linker options) and using the <code>execstack</code> tool also on an already linker binary or shared library. This tool is especially useful for third party shared libraries where it is known that they don&#8217;t need executable stack or testing proves it.</p>
<h2>Options</h2>
<dl>
<dt><code>-s &#8211;set-execstack</code></p>
<dd>Mark binary or shared library as requiring executable stack.</p>
<dt><code>-c &#8211;clear-execstack</code></p>
<dd>Mark binary or shared library as not requiring executable stack.</p>
<dt><code>-q &#8211;query</code></p>
<dd>Query executable stack marking of binaries and shared libraries. For each file it prints either <code>&#8211;</code> when executable stack is not required, <code>X</code> when executable stack is required or <code>?</code> when it is unknown whether the object requires or doesn&#8217;t require executable stack (the marking is missing).</p>
<dt><code>-V</code></p>
<dd>Print <code>execstack</code> version and exit.</p>
<dt><code>-? &#8211;help</code></p>
<dd>Print help message.</p>
<dt><code>&#8211;usage</code></p>
<dd>Print a short usage message.</dl>
<h2>Arguments</h2>
<p>Command line arguments should be names of ELF binaries and shared libraries which should be modified or queried.</p>
<h2>Examples</h2>
<dl>
<dd># execstack -s ~/lib/libfoo.so.1</dl>
<p> will mark ~/lib/libfoo.so.1 as requiring executable stack.</p>
<dl>
<dd># execstack -c ~/bin/bar</dl>
<p> will mark ~/bin/bar as not requiring executable stack.</p>
<dl>
<dd># execstack -q ~/lib/libfoo.so.1 ~/bin/bar</dl>
<p> will query executable stack marking of the given files.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8).</p>
<h2>Bugs</h2>
<p><code>execstack</code> doesn&#8217;t support yet marking of executables if they do not have PT_GNU_STACK program header entry nor they have room for program segment header table growth.</p>
<h2>Authors</h2>
<p>Jakub Jelinek &lt;jakub [at] redhat.com&gt;.</p>
