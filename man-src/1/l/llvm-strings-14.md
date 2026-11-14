---
title: "llvm-strings-14(1)"
name: "llvm-strings-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-strings-14/"
description: "llvm-strings – print strings"
---

<h2 class="name">NAME</h2>
<p> llvm-strings &#8211; print strings </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-strings</code> [<i>options</i>] [<i>input…</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>llvm-strings</code> is a tool intended as a drop-in replacement for GNU’s <code>strings</code>, which looks for printable strings in files and writes them to the standard output stream. A printable string is any sequence of four (by default) or more printable ASCII characters. The end of the file, or any other byte, terminates the current sequence. </p>
<p> <code>llvm-strings</code> looks for strings in each <code>input</code> file specified. Unlike GNU <code>strings</code> it looks in the entire input file, regardless of file format, rather than restricting the search to certain sections of object files. If “<code>&#8211;</code>” is specified as an <code>input</code>, or no <code>input</code> is specified, the program reads from the standard input stream.</p>
<h2>EXAMPLE</h2>
<pre>
$ cat input.txt
bars
foo
wibble blob
$ llvm-strings input.txt
bars
wibble blob
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;all, -a</code></p>
<dd> Silently ignored. Present for GNU <code>strings</code> compatibility.</p>
<dt><code>&#8211;bytes=&lt;length&gt;, -n</code></p>
<dd> Set the minimum number of printable ASCII characters required for a sequence of bytes to be considered a string. The default value is 4.</p>
<dt><code>&#8211;help, -h</code></p>
<dd> Display a summary of command line options.</p>
<dt><code>&#8211;print-file-name, -f</code></p>
<dd> Display the name of the containing file before each string. </p>
<p> Example: </p>
<pre>
$ llvm-strings --print-file-name test.o test.elf
test.o: _Z5hellov
test.o: some_bss
test.o: test.cpp
test.o: main
test.elf: test.cpp
test.elf: test2.cpp
test.elf: _Z5hellov
test.elf: main
test.elf: some_bss
</pre>
<dt><code>&#8211;radix=&lt;radix&gt;, -t</code></p>
<dd> Display the offset within the file of each string, before the string and using the specified radix. Valid <code>&lt;radix&gt;</code> values are <code>o</code>, <code>d</code> and <code>x</code> for octal, decimal and hexadecimal respectively. </p>
<p> Example: </p>
<pre>
$ llvm-strings --radix=o test.o
    1054 _Z5hellov
    1066 .rela.text
    1101 .comment
    1112 some_bss
    1123 .bss
    1130 test.cpp
    1141 main
$ llvm-strings --radix=d test.o
    556 _Z5hellov
    566 .rela.text
    577 .comment
    586 some_bss
    595 .bss
    600 test.cpp
    609 main
$ llvm-strings -t x test.o
    22c _Z5hellov
    236 .rela.text
    241 .comment
    24a some_bss
    253 .bss
    258 test.cpp
    261 main
</pre>
<dt><code>&#8211;version</code></p>
<dd> Display the version of the <code>llvm-strings</code> executable.</p>
<dt><code>@&lt;FILE&gt;</code></p>
<dd> Read command-line options from response file <code>&lt;FILE&gt;</code>.</dl>
<h2>EXIT STATUS</h2>
<p> <code>llvm-strings</code> exits with a non-zero exit code if there is an error. Otherwise, it exits with code 0.</p>
<h2>BUGS</h2>
<p> To report bugs, please visit &lt;<i><a rel="nofollow" href="https://github.com/llvm/llvm-project/labels/tools:llvm-strings/">https://github.com/llvm/llvm-project/labels/tools:llvm-strings/</a></i>&gt;.</p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
