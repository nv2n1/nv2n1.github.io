---
title: "llvm-lipo-14(1)"
name: "llvm-lipo-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-lipo-14/"
description: "llvm-lipo – LLVM tool for manipulating universal binaries"
---

<h2 class="name">NAME</h2>
<p> llvm-lipo &#8211; LLVM tool for manipulating universal binaries </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-lipo</code> [<i>filenames…</i>] [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>llvm-lipo</code> can create universal binaries from Mach-O files, extract regular object files from universal binaries, and display architecture information about both universal and regular files.</p>
<h2>COMMANDS</h2>
<p> <code>llvm-lipo</code> supports the following mutually exclusive commands:</p>
<dl>
<dt><code>-help, -h</code></p>
<dd> Display usage information and exit.</p>
<dt><code>-version</code></p>
<dd> Display the version of this program.</p>
<dt><code>-verify_arch &lt;architecture 1&gt; [&lt;architecture 2&gt; &#8230;]</code></p>
<dd> Take a single input file and verify the specified architectures are present in the file. If so then exit with a status of 0 else exit with a status of 1.</p>
<dt><code>-archs</code></p>
<dd> Take a single input file and display the architectures present in the file. Each architecture is separated by a single whitespace. Unknown architectures are displayed as unknown(CPUtype,CPUsubtype).</p>
<dt><code>-info</code></p>
<dd> Take at least one input file and display the descriptions of each file. The descriptions include the filename and architecture types separated by whitespace. Universal binaries are grouped together first, followed by thin files. Architectures in the fat file: &lt;filename&gt; are: &lt;architectures&gt; Non-fat file: &lt;filename&gt; is architecture: &lt;architecture&gt;</p>
<dt><code>-thin</code></p>
<dd> Take a single universal binary input file and the thin flag followed by an architecture type. Require the output flag to be specified, and output a thin binary of the specified architecture.</p>
<dt><code>-create</code></p>
<dd> Take at least one input file and require the output flag to be specified. Output a universal binary combining the input files.</p>
<dt><code>-replace</code></p>
<dd> Take a single universal binary input file and require the output flag to be specified. The replace flag is followed by an architecture type, and a thin input file. Output a universal binary with the specified architecture slice in the universal binary input replaced with the contents of the thin input file.</p>
<dt><code>-segalign</code></p>
<dd> Additional flag that can be specified with create and replace. The segalign flag is followed by an architecture type, and an alignment. The alignment is a hexadecimal number that is a power of 2. Output a file in which the slice with the specified architecture has the specified alignment.</dl>
<h2>BUGS</h2>
<p> To report bugs, please visit &lt;<i><a rel="nofollow" href="https://github.com/llvm/llvm-project/issues/">https://github.com/llvm/llvm-project/issues/</a></i>&gt;.</p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
