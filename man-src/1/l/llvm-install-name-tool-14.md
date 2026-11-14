---
title: "llvm-install-name-tool-14(1)"
name: "llvm-install-name-tool-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-install-name-tool-14/"
description: "llvm-install-name-tool – LLVM tool for manipulating install-names and rpaths"
---

<h2 class="name">NAME</h2>
<p> llvm-install-name-tool &#8211; LLVM tool for manipulating install-names and rpaths </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-install-name-tool</code> [<i>options</i>] <i>input</i></p>
<h2>DESCRIPTION</h2>
<p> <code>llvm-install-name-tool</code> is a tool to manipulate dynamic shared library install names and rpaths listed in a Mach-O binary. </p>
<p> For most scenarios, it works as a drop-in replacement for Apple’s <code>install_name_tool</code>.</p>
<h2>OPTIONS</h2>
<p> At least one of the following options are required, and some options can be combined with other options. Options <i>-add_rpath</i>, <i>-delete_rpath</i>, and <i>-rpath</i> can be combined in an invocation only if they do not share the same <i>&lt;rpath&gt;</i> value.</p>
<dl>
<dt><code>-add_rpath &lt;rpath&gt;</code></p>
<dd> Add an rpath named <code>&lt;rpath&gt;</code> to the specified binary. Can be specified multiple times to add multiple rpaths. Throws an error if <code>&lt;rpath&gt;</code> is already listed in the binary.</p>
<dt><code>-change &lt;old_install_name&gt; &lt;new_install_name&gt;</code></p>
<dd> Change an install name <code>&lt;old_install_name&gt;</code> to <code>&lt;new_install_name&gt;</code> in the specified binary. Can be specified multiple times to change multiple dependent shared library install names. Option is ignored if <code>&lt;old_install_name&gt;</code> is not listed in the specified binary.</p>
<dt><code>-delete_rpath &lt;rpath&gt;</code></p>
<dd> Delete an rpath named <code>&lt;rpath&gt;</code> from the specified binary. Can be specified multiple times to delete multiple rpaths. Throws an error if <code>&lt;rpath&gt;</code> is not listed in the binary.</p>
<dt><code>-delete_all_rpaths</code></p>
<dd> Deletes all rpaths from the binary.</p>
<dt><code>&#8211;help, -h</code></p>
<dd> Print a summary of command line options.</p>
<dt><code>-id &lt;name&gt;</code></p>
<dd> Change shared library’s identification name under LC_ID_DYLIB to <code>&lt;name&gt;</code> in the specified binary. If specified multiple times, only the last <i>-id</i> option is selected. Option is ignored if the specified Mach-O binary is not a dynamic shared library.</p>
<dt><code>-rpath &lt;old_rpath&gt; &lt;new_rpath&gt;</code></p>
<dd> Change an rpath named <code>&lt;old_rpath&gt;</code> to <code>&lt;new_rpath&gt;</code> in the specified binary. Can be specified multiple times to change multiple rpaths. Throws an error if <code>&lt;old_rpath&gt;</code> is not listed in the binary or <code>&lt;new_rpath&gt;</code> is already listed in the binary.</p>
<dt><code>&#8211;version, -V</code></p>
<dd> Display the version of the <code>llvm-install-name-tool</code> executable.</dl>
<h2>EXIT STATUS</h2>
<p> <code>llvm-install-name-tool</code> exits with a non-zero exit code if there is an error. Otherwise, it exits with code 0.</p>
<h2>BUGS</h2>
<p> To report bugs, please visit &lt;<i><a rel="nofollow" href="https://github.com/llvm/llvm-project/labels/tools:llvm-objcopy/strip/">https://github.com/llvm/llvm-project/labels/tools:llvm-objcopy/strip/</a></i>&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-llvm-objcopy/">llvm-objcopy</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
