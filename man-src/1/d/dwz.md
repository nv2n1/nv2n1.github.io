---
title: "dwz(1)"
name: "dwz"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dwz/"
description: "dwz – DWARF optimization and duplicate removal tool"
---

<h2 class="name">NAME</h2>
<p> dwz &#8211; DWARF optimization and duplicate removal tool </p>
<h2>SYNOPSIS</h2>
<p> dwz [OPTION&#8230;]&nbsp;[FILES]</p>
<h2>DESCRIPTION</h2>
<p> <code>dwz</code> is a program that attempts to optimize DWARF debugging information contained in ELF shared libraries and ELF executables for size, by replacing DWARF information representation with equivalent smaller representation where possible and by reducing the amount of duplication using techniques from DWARF standard appendix E &#8211; creating <i>DW_TAG_partial_unit</i> compilation units (CUs) for duplicated information and using <i>DW_TAG_imported_unit</i> to import it into each CU that needs it. </p>
<p> The tool handles DWARF 32-bit format debugging sections of versions 2, 3 and 4 and GNU extensions on top of those, though using DWARF 4 or worst case DWARF 3 is strongly recommended. </p>
<p> The tool has two main modes of operation, without the <i>-m</i> option it attempts to optimize DWARF debugging information in each given object (executable or shared library) individually, with the <i>-m</i> option it afterwards attempts to optimize even more by moving DWARF debugging information entries (DIEs), strings and macro descriptions duplicated in more than one object into a newly created ELF ET_REL object whose filename is given as <i>-m</i> option argument. The debug sections in the executables and shared libraries specified on the command line are then modified again, referring to the entities in the newly created object.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-m FILE &#8211;multifile FILE</code></p>
<dd> Multifile mode. After processing all named executables and shared libraries, attempt to create ELF object <i>FILE</i> and put debugging information duplicated in more than one object there, afterwards optimize each named executable or shared library even further if possible.</p>
<dt><code>-h &#8211;hardlink</code></p>
<dd> Look for executables or shared libraries hardlinked together, instead of rewriting them individually rewrite just one of them and hardlink the rest to the first one again.</p>
<dt><code>-M NAME &#8211;multifile-name NAME</code></p>
<dd> Specify the name of the common file that should be put into the <i>.gnu_debugaltlink</i> section alongside with its build ID. By default <code>dwz</code> puts there the argument of the <code>-m</code> option.</p>
<dt><code>-r &#8211;relative</code></p>
<dd> Specify that the name of the common file to be put into the <i>.gnu_debugaltlink</i> section is supposed to be relative path from the directory containing the executable or shared library to the file named in the argument of the <code>-m</code> option. Either <code>-M</code> or <code>-r</code> option can be specified, but not both.</p>
<dt><code>-q &#8211;quiet</code></p>
<dd> Silence up some of the most common messages.</p>
<dt><code>-o FILE &#8211;output FILE</code></p>
<dd> This option instructs <code>dwz</code> not to overwrite the specified file, but instead store the new content into <code>FILE</code>. Nothing is written if <code>dwz</code> exits with non-zero exit code. Can be used only with a single executable or shared library (if there are no arguments at all, <i>a.out</i> is assumed).</p>
<dt><code>-l &lt;COUNT|none&gt; &#8211;low-mem-die-limit &lt;COUNT|none&gt;</code></p>
<dd> Handle executables or shared libraries containing more than <i>COUNT</i> debugging information entries in their <i>.debug_info</i> section using a slower and more memory usage friendly mode and don&#8217;t attempt to optimize that object in multifile mode. The default is 10 million DIEs. There is a risk that for very large amounts of debugging information in a single shared library or executable there might not be enough memory (especially when <code>dwz</code> tool is 32-bit binary, it might run out of available virtual address space even sooner). Specifying none as argument disables the limit.</p>
<dt><code>-L &lt;COUNT|none&gt; &#8211;max-die-limit &lt;COUNT|none&gt;</code></p>
<dd> Don&#8217;t attempt to optimize executables or shared libraries containing more than <i>COUNT</i> DIEs at all. The default is 50 million DIEs. Specifying none as argument disables the limit.</p>
<dt><code>-? &#8211;help</code></p>
<dd> Print short help and exit.</p>
<dt><code>-v &#8211;version</code></p>
<dd> Print version number and short licensing notice and exit.</dl>
<h2>ARGUMENTS</h2>
<p> Command-line arguments should be the executables, shared libraries or their stripped to file separate debug information objects.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> $ dwz -m .dwz/foobar-1.2.debug -rh \<br />
&nbsp;<wbr>&nbsp;bin/foo.debug bin/foo2.debug foo/lib/libbar.so.debug</dl>
<p> will attempt to optimize debugging information in <i>bin/foo.debug</i>, <i>bin/foo2.debug</i> and <i>lib/libbar.so.debug</i> (by modifying the files in place) and when beneficial also will create <i>.dwz/foobar-1.2.debug</i> file. <i>.gnu_debugaltlink</i> section in the first two files will refer to <i>../.dwz/foobar-1.2.debug</i> and in the last file to <i>../../.dwz/foobar-1.2.debug</i>. If e.g. <i>bin/foo.debug</i> and <i>bin/foo2.debug</i> were hardlinked together initially, they will be hardlinked again and for multifile optimizations considered just as a single file rather than two.</p>
<dl>
<dt>
<dd> $ dwz -o foo.dwz foo</dl>
<p> will not modify <i>foo</i> but instead store the ELF object with optimized debugging information if successful into <i>foo.dwz</i> file it creates.</p>
<dl>
<dt>
<dd> $ dwz *.debug foo/*.debug</dl>
<p> will attempt to optimize debugging information in *.debug and foo/*.debug files, optimizing each file individually in place.</p>
<dl>
<dt>
<dd> $ dwz</dl>
<p> is equivalent to <i>dwz a.out</i> command.</p>
<h2>SEE ALSO</h2>
<p> <code><a rel="nofollow" href="http://dwarfstd.org/doc/DWARF4.pdf">http://dwarfstd.org/doc/DWARF4.pdf</a></code> , <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1).</p>
<h2>AUTHORS</h2>
<p> Jakub Jelinek &lt;jakub [at] redhat.com&gt;. </p>
<h2>Index</h2>
