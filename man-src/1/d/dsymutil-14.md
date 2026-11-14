---
title: "dsymutil-14(1)"
name: "dsymutil-14"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dsymutil-14/"
description: "dsymutil – manipulate archived DWARF debug symbol files"
---

<h2 class="name">NAME</h2>
<p> dsymutil &#8211; manipulate archived DWARF debug symbol files </p>
<h2>SYNOPSIS</h2>
<pre>
<code>dsymutil</code> [<i>options</i>] <i>executable</i>
</pre>
<h2>DESCRIPTION</h2>
<p> <code>dsymutil</code> links the DWARF debug information found in the object files for an executable <i>executable</i> by using debug symbols information contained in its symbol table. By default, the linked debug information is placed in a <code>.dSYM</code> bundle with the same name as the executable.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;accelerator=&lt;accelerator type&gt;</code></p>
<dd> Specify the desired type of accelerator table. Valid options are ‘Apple’, ‘Dwarf’ and ‘Default’.</p>
<dt><code>&#8211;arch &lt;arch&gt;</code></p>
<dd> Link DWARF debug information only for specified CPU architecture types. Architectures may be specified by name. When using this option, an error will be returned if any architectures can not be properly linked. This option can be specified multiple times, once for each desired architecture. All CPU architectures will be linked by default and any architectures that can’t be properly linked will cause <code>dsymutil</code> to return an error.</p>
<dt><code>&#8211;dump-debug-map</code></p>
<dd> Dump the <i>executable</i>’s debug-map (the list of the object files containing the debug information) in YAML format and exit. No DWARF link will take place.</p>
<dt><code>&#8211;flat, -f</code></p>
<dd> Produce a flat dSYM file. A <code>.dwarf</code> extension will be appended to the executable name unless the output file is specified using the <code>-o</code> option.</p>
<dt><code>&#8211;gen-reproducer</code></p>
<dd> Generate a reproducer consisting of the input object files.</p>
<dt><code>&#8211;help, -h</code></p>
<dd> Print this help output.</p>
<dt><code>&#8211;keep-function-for-static</code></p>
<dd> Make a static variable keep the enclosing function even if it would have been omitted otherwise.</p>
<dt><code>&#8211;minimize, -z</code></p>
<dd> When used when creating a dSYM file, this option will suppress the emission of the .debug_inlines, .debug_pubnames, and .debug_pubtypes sections since dsymutil currently has better equivalents: .apple_names and .apple_types. When used in conjunction with <code>&#8211;update</code> option, this option will cause redundant accelerator tables to be removed.</p>
<dt><code>&#8211;no-odr</code></p>
<dd> Do not use ODR (One Definition Rule) for uniquing C++ types.</p>
<dt><code>&#8211;no-output</code></p>
<dd> Do the link in memory, but do not emit the result file.</p>
<dt><code>&#8211;no-swiftmodule-timestamp</code></p>
<dd> Don’t check the timestamp for swiftmodule files.</p>
<dt><code>&#8211;num-threads &lt;threads&gt;, -j &lt;threads&gt;</code></p>
<dd> Specifies the maximum number (<code>n</code>) of simultaneous threads to use when linking multiple architectures.</p>
<dt><code>&#8211;object-prefix-map &lt;prefix=remapped&gt;</code></p>
<dd> Remap object file paths (but no source paths) before processing. Use this for Clang objects where the module cache location was remapped using <code>-fdebug-prefix-map</code>; to help dsymutil find the Clang module cache.</p>
<dt><code>&#8211;oso-prepend-path &lt;path&gt;</code></p>
<dd> Specifies a <code>path</code> to prepend to all debug symbol object file paths.</p>
<dt><code>&#8211;out &lt;filename&gt;, -o &lt;filename&gt;</code></p>
<dd> Specifies an alternate <code>path</code> to place the dSYM bundle. The default dSYM bundle path is created by appending <code>.dSYM</code> to the executable name.</p>
<dt><code>&#8211;papertrail</code></p>
<dd> When running dsymutil as part of your build system, it can be desirable for warnings to be part of the end product, rather than just being emitted to the output stream. When enabled warnings are embedded in the linked DWARF debug information.</p>
<dt><code>&#8211;remarks-output-format &lt;format&gt;</code></p>
<dd> Specify the format to be used when serializing the linked remarks.</p>
<dt><code>&#8211;remarks-prepend-path &lt;path&gt;</code></p>
<dd> Specify a directory to prepend the paths of the external remark files.</p>
<dt><code>&#8211;statistics</code></p>
<dd> Print statistics about the contribution of each object file to the linked debug info. This prints a table after linking with the object file name, the size of the debug info in the object file (in bytes) and the size contributed (in bytes) to the linked dSYM. The table is sorted by the output size listing the object files with the largest contribution first.</p>
<dt><code>&#8211;symbol-map &lt;bcsymbolmap&gt;</code></p>
<dd> Update the existing dSYMs inplace using symbol map specified.</p>
<dt><code>-s, &#8211;symtab</code></p>
<dd> Dumps the symbol table found in <i>executable</i> or object file(s) and exits.</p>
<dt><code>-S</code></p>
<dd> Output textual assembly instead of a binary dSYM companion file.</p>
<dt><code>&#8211;toolchain &lt;toolchain&gt;</code></p>
<dd> Embed the toolchain in the dSYM bundle’s property list.</p>
<dt><code>-u, &#8211;update</code></p>
<dd> Update an existing dSYM file to contain the latest accelerator tables and other DWARF optimizations. This option will rebuild the ‘.apple_names’ and ‘.apple_types’ hashed accelerator tables.</p>
<dt><code>&#8211;use-reproducer &lt;path&gt;</code></p>
<dd> Use the object files from the given reproducer path.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Display verbose information when linking.</p>
<dt><code>&#8211;verify</code></p>
<dd> Run the DWARF verifier on the linked DWARF debug info.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Display the version of the tool.</p>
<dt><code>-y</code></p>
<dd> Treat <i>executable</i> as a YAML debug-map rather than an executable.</dl>
<h2>EXIT STATUS</h2>
<p> <code>dsymutil</code> returns 0 if the DWARF debug information was linked successfully. Otherwise, it returns 1.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-llvm-dwarfdump/">llvm-dwarfdump</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
