---
title: "llvm-symbolizer-14(1)"
name: "llvm-symbolizer-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-symbolizer-14/"
description: "llvm-symbolizer – convert addresses into source code locations"
---

<h2 class="name">NAME</h2>
<p> llvm-symbolizer &#8211; convert addresses into source code locations </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-symbolizer</code> [<i>options</i>] [<i>addresses…</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>llvm-symbolizer</code> reads object file names and addresses from the command-line and prints corresponding source code locations to standard output. </p>
<p> If no address is specified on the command-line, it reads the addresses from standard input. If no object file is specified on the command-line, but addresses are, or if at any time an input value is not recognized, the input is simply echoed to the output. </p>
<p> A positional argument or standard input value can be preceded by “DATA” or “CODE” to indicate that the address should be symbolized as data or executable code respectively. If neither is specified, “CODE” is assumed. DATA is symbolized as address and symbol size rather than line number. </p>
<p> Object files can be specified together with the addresses either on standard input or as positional arguments on the command-line, following any “DATA” or “CODE” prefix. </p>
<p> <code>llvm-symbolizer</code> parses options from the environment variable <code>LLVM_SYMBOLIZER_OPTS</code> after parsing options from the command line. <code>LLVM_SYMBOLIZER_OPTS</code> is primarily useful for supplementing the command-line options when <code>llvm-symbolizer</code> is invoked by another program or runtime.</p>
<h2>EXAMPLES</h2>
<p> All of the following examples use the following two source files as input. They use a mixture of C-style and C++-style linkage to illustrate how these names are printed differently (see <i>&#8211;demangle</i>). </p>
<pre><code>
// test.h
extern "C" inline int foz()
{
    return 1234;
}
</code></pre>
<p>// test.cpp<br />
#include &#8220;test.h&#8221;<br />
int bar = 42;<br />
int foo()<br />
{<br />
    return bar;<br />
}<br />
int baz()<br />
{<br />
    volatile int k = 42;<br />
    return foz() + k;<br />
}<br />
int main()<br />
{<br />
    return foo() + baz();<br />
}</p>
<p> These files are built as follows: </p>
<pre>
$ clang -g test.cpp -o test.elf
$ clang -g -O2 test.cpp -o inlined.elf
</pre>
<p> Example 1 &#8211; addresses and object on command-line: </p>
<pre>
$ llvm-symbolizer --obj=test.elf 0x4004d0 0x400490
foz
/tmp/test.h:1:0
baz()
/tmp/test.cpp:11:0
</pre>
<p> Example 2 &#8211; addresses on standard input: </p>
<pre>
$ cat addr.txt
0x4004a0
0x400490
0x4004d0
$ llvm-symbolizer --obj=test.elf &lt; addr.txt
main
/tmp/test.cpp:15:0
baz()
/tmp/test.cpp:11:0
foz
/tmp/./test.h:1:0
</pre>
<p> Example 3 &#8211; object specified with address: </p>
<pre>
$ llvm-symbolizer &quot;test.elf 0x400490&quot; &quot;inlined.elf 0x400480&quot;
baz()
/tmp/test.cpp:11:0
foo()
/tmp/test.cpp:8:10
$ cat addr2.txt
test.elf 0x4004a0
inlined.elf 0x400480
$ llvm-symbolizer &lt; addr2.txt
main
/tmp/test.cpp:15:0
foo()
/tmp/test.cpp:8:10
</pre>
<p> Example 4 &#8211; CODE and DATA prefixes: </p>
<pre>
$ llvm-symbolizer --obj=test.elf &quot;CODE 0x400490&quot; &quot;DATA 0x601028&quot;
baz()
/tmp/test.cpp:11:0
bar
6295592 4
$ cat addr3.txt
CODE test.elf 0x4004a0
DATA inlined.elf 0x601028
$ llvm-symbolizer &lt; addr3.txt
main
/tmp/test.cpp:15:0
bar
6295592 4
</pre>
<p> Example 5 &#8211; path-style options: </p>
<p> This example uses the same source file as above, but the source file’s full path is /tmp/foo/test.cpp and is compiled as follows. The first case shows the default absolute path, the second –basenames, and the third shows –relativenames. </p>
<p>$ pwd / tmp<br />
            $ clang &#8211;<br />
    g foo / test.cpp &#8211; o test.elf $ llvm &#8211; symbolizer&#8211; obj = test.elf 0x4004a0 main / tmp / foo / test.cpp : 15 : 0 $ llvm &#8211; symbolizer&#8211; obj = test.elf 0x4004a0 &#8211;basenames<br />
                                                                                                                                                     main<br />
                                                                                                                                                         test.cpp : 15 : 0 $ llvm &#8211;<br />
                                                                                                                                                 symbolizer&#8211; obj = test.elf 0x4004a0 &#8211;relativenames<br />
                                                                                                                                                                        main<br />
                                                                                                                                                                            foo /<br />
                                                                                                                                                                    test.cpp : 15 : 0</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;adjust-vma &lt;offset&gt;</code></p>
<dd> Add the specified offset to object file addresses when performing lookups. This can be used to perform lookups as if the object were relocated by the offset.</p>
<dt><code>&#8211;basenames, -s</code></p>
<dd> Print just the file’s name without any directories, instead of the absolute path.</p>
<dt><code>&#8211;demangle, -C</code></p>
<dd> Print demangled function names, if the names are mangled (e.g. the mangled name <i>_Z3bazv</i> becomes <i>baz()</i>, whilst the non-mangled name <i>foz</i> is printed as is). Defaults to true.</p>
<dt><code>&#8211;dwp &lt;path&gt;</code></p>
<dd> Use the specified DWP file at <code>&lt;path&gt;</code> for any CUs that have split DWARF debug data.</p>
<dt><code>&#8211;fallback-debug-path &lt;path&gt;</code></p>
<dd> When a separate file contains debug data, and is referenced by a GNU debug link section, use the specified path as a basis for locating the debug data if it cannot be found relative to the object.</p>
<dt><code>&#8211;functions [=&lt;none|short|linkage&gt;], -f</code></p>
<dd> Specify the way function names are printed (omit function name, print short function name, or print full linkage name, respectively). Defaults to <code>linkage</code>.</p>
<dt><code>&#8211;help, -h</code></p>
<dd> Show help and usage for this command.</p>
<dt><code>&#8211;inlining, &#8211;inlines, -i</code></p>
<dd> If a source code location is in an inlined function, prints all the inlined frames. This is the default.</p>
<dt><code>&#8211;no-inlines</code></p>
<dd> Don’t print inlined frames.</p>
<dt><code>&#8211;no-demangle</code></p>
<dd> Don’t print demangled function names.</p>
<dt><code>&#8211;obj &lt;path&gt;, &#8211;exe, -e</code></p>
<dd> Path to object file to be symbolized. If <code>&#8211;</code> is specified, read the object directly from the standard input stream.</p>
<dt><code>&#8211;output-style &lt;LLVM|GNU|JSON&gt;</code></p>
<dd> Specify the preferred output style. Defaults to <code>LLVM</code>. When the output style is set to <code>GNU</code>, the tool follows the style of GNU’s <code>addr2line</code>. The differences from the <code>LLVM</code> style are:</p>
<dt>&bull;</p>
<dd> Does not print the column of a source code location.</p>
<dt>&bull;</p>
<dd> Does not add an empty line after the report for an address.</p>
<dt>&bull;</p>
<dd> Does not replace the name of an inlined function with the name of the topmost caller when inlined frames are not shown.</p>
<dt>&bull;</p>
<dd> Prints an address’s debug-data discriminator when it is non-zero. One way to produce discriminators is to compile with clang’s -fdebug-info-for-profiling.</p>
<dt><code>JSON</code> style provides a machine readable output in JSON. If addresses are</p>
<dd> supplied via stdin, the output JSON will be a series of individual objects. Otherwise, all results will be contained in a single array. </p>
<p>$ llvm-symbolizer &#8211;obj=inlined.elf 0x4004be 0x400486 -p<br />
baz() at /tmp/test.cpp:11:18<br />
 (inlined by) main at /tmp/test.cpp:15:0<br />
foo() at /tmp/test.cpp:6:3<br />
$ llvm-symbolizer &#8211;output-style=LLVM &#8211;obj=inlined.elf 0x4004be 0x400486 -p &#8211;no-inlines<br />
main at /tmp/test.cpp:11:18<br />
foo() at /tmp/test.cpp:6:3<br />
$ llvm-symbolizer &#8211;output-style=GNU &#8211;obj=inlined.elf 0x4004be 0x400486 -p &#8211;no-inlines<br />
baz() at /tmp/test.cpp:11<br />
foo() at /tmp/test.cpp:6<br />
$ clang -g -fdebug-info-for-profiling test.cpp -o profiling.elf<br />
$ llvm-symbolizer &#8211;output-style=GNU &#8211;obj=profiling.elf 0x401167 -p &#8211;no-inlines<br />
main at /tmp/test.cpp:15 (discriminator 2)<br />
$ llvm-symbolizer &#8211;output-style=JSON &#8211;obj=inlined.elf 0x4004be 0x400486 -p<br />
[<br />
  {<br />
    &#8220;Address&#8221;: &#8220;0x4004be&#8221;,<br />
    &#8220;ModuleName&#8221;: &#8220;inlined.elf&#8221;,<br />
    &#8220;Symbol&#8221;: [<br />
      {<br />
        &#8220;Column&#8221;: 18,<br />
        &#8220;Discriminator&#8221;: 0,<br />
        &#8220;FileName&#8221;: &#8220;/tmp/test.cpp&#8221;,<br />
        &#8220;FunctionName&#8221;: &#8220;baz()&#8221;,<br />
        &#8220;Line&#8221;: 11,<br />
        &#8220;StartAddress&#8221;: &#8220;0x4004be&#8221;,<br />
        &#8220;StartFileName&#8221;: &#8220;/tmp/test.cpp&#8221;,<br />
        &#8220;StartLine&#8221;: 9<br />
      },<br />
      {<br />
        &#8220;Column&#8221;: 0,<br />
        &#8220;Discriminator&#8221;: 0,<br />
        &#8220;FileName&#8221;: &#8220;/tmp/test.cpp&#8221;,<br />
        &#8220;FunctionName&#8221;: &#8220;main&#8221;,<br />
        &#8220;Line&#8221;: 15,<br />
        &#8220;StartAddress&#8221;: &#8220;0x4004be&#8221;,<br />
        &#8220;StartFileName&#8221;: &#8220;/tmp/test.cpp&#8221;,<br />
        &#8220;StartLine&#8221;: 14<br />
      }<br />
    ]<br />
  },<br />
  {<br />
    &#8220;Address&#8221;: &#8220;0x400486&#8221;,<br />
    &#8220;ModuleName&#8221;: &#8220;inlined.elf&#8221;,<br />
    &#8220;Symbol&#8221;: [<br />
      {<br />
        &#8220;Column&#8221;: 3,<br />
        &#8220;Discriminator&#8221;: 0,<br />
        &#8220;FileName&#8221;: &#8220;/tmp/test.cpp&#8221;,<br />
        &#8220;FunctionName&#8221;: &#8220;foo()&#8221;,<br />
        &#8220;Line&#8221;: 6,<br />
        &#8220;StartAddress&#8221;: &#8220;0x400486&#8221;,<br />
        &#8220;StartFileName&#8221;: &#8220;/tmp/test.cpp&#8221;,<br />
        &#8220;StartLine&#8221;: 5<br />
      }<br />
    ]<br />
  }<br />
]</p>
<dt><code>&#8211;pretty-print, -p</code></p>
<dd> Print human readable output. If <i>&#8211;inlining</i> is specified, the enclosing scope is prefixed by (inlined by). For JSON output, the option will cause JSON to be indented and split over new lines. Otherwise, the JSON output will be printed in a compact form. </p>
<pre>
$ llvm-symbolizer --obj=inlined.elf 0x4004be --inlining --pretty-print
baz() at /tmp/test.cpp:11:18
 (inlined by) main at /tmp/test.cpp:15:0
</pre>
<dt><code>&#8211;print-address, &#8211;addresses, -a</code></p>
<dd> Print address before the source code location. Defaults to false. </p>
<p>$ llvm &#8211; symbolizer&#8211; obj = inlined.elf&#8211; print &#8211; address 0x4004be 0x4004be baz() / tmp / test.cpp : 11 : 18 main / tmp / test.cpp : 15 : 0 $ llvm &#8211; symbolizer&#8211; obj = inlined.elf 0x4004be &#8211;pretty &#8211; print&#8211; print &#8211; address 0x4004be : baz() at / tmp / test.cpp : 11 : 18(inlined by)main at / tmp / test.cpp : 15 : 0</p>
<dt><code>&#8211;print-source-context-lines &lt;N&gt;</code></p>
<dd> Print <code>N</code> lines of source context for each symbolized address. </p>
<pre><code>
$ llvm - symbolizer-- obj = test.elf 0x400490 --print - source - context - lines = 3 baz() / tmp / test.cpp : 11 : 0 10 : volatile int k = 42;
11 &gt; : return foz() + k;
12:
}
</code></pre>
<dt><code>&#8211;relativenames</code></p>
<dd> Print the file’s path relative to the compilation directory, instead of the absolute path. If the command-line to the compiler included the full path, this will be the same as the default.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Print verbose address, line and column information. </p>
<pre>
$ llvm-symbolizer --obj=inlined.elf --verbose 0x4004be
baz()
  Filename: /tmp/test.cpp
  Function start filename: /tmp/test.cpp
  Function start line: 9
  Function start address: 0x4004b6
  Line: 11
  Column: 18
main
  Filename: /tmp/test.cpp
  Function start filename: /tmp/test.cpp
  Function start line: 14
  Function start address: 0x4004b0
  Line: 15
  Column: 18
</pre>
<dt><code>&#8211;version, -v</code></p>
<dd> Print version information for the tool.</p>
<dt><code>@&lt;FILE&gt;</code></p>
<dd> Read command-line options from response file <i>&lt;FILE&gt;</i>.</dl>
<h2>WINDOWS/PDB SPECIFIC OPTIONS</h2>
<dl>
<dt><code>&#8211;dia</code></p>
<dd> Use the Windows DIA SDK for symbolization. If the DIA SDK is not found, llvm-symbolizer will fall back to the native implementation.</dl>
<h2>MACH-O SPECIFIC OPTIONS</h2>
<dl>
<dt><code>&#8211;default-arch &lt;arch&gt;</code></p>
<dd> If a binary contains object files for multiple architectures (e.g. it is a Mach-O universal binary), symbolize the object file for a given architecture. You can also specify the architecture by writing <code>binary_name:arch_name</code> in the input (see example below). If the architecture is not specified in either way, the address will not be symbolized. Defaults to empty string. </p>
<pre>
$ cat addr.txt
/tmp/mach_universal_binary:i386 0x1f84
/tmp/mach_universal_binary:x86_64 0x100000f24
$ llvm-symbolizer &lt; addr.txt
_main
/tmp/source_i386.cc:8
_main
/tmp/source_x86_64.cc:8
</pre>
<dt><code>&#8211;dsym-hint &lt;path/to/file.dSYM&gt;</code></p>
<dd> If the debug info for a binary isn’t present in the default location, look for the debug info at the .dSYM path provided via this option. This flag can be used multiple times.</dl>
<h2>EXIT STATUS</h2>
<p> <code>llvm-symbolizer</code> returns 0. Other exit codes imply an internal program error.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-llvm-addr2line/">llvm-addr2line</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
