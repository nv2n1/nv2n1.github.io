---

title: "llvm-libtool-darwin-14(1)"
name: "llvm-libtool-darwin-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-libtool-darwin-14/"
description: "llvm-libtool-darwin – LLVM tool for creating libraries for Darwin"
---

<p> <code>llvm-libtool-darwin</code> [<i>options</i>] <i>&lt;input files&gt;</i></p>
<p> <code>llvm-libtool-darwin</code> is a tool for creating static and dynamic libraries for Darwin. </p>
<p> For most scenarios, it works as a drop-in replacement for cctools’ <code>libtool</code>.</p>
<h2>OPTIONS</h2>
<p> <code>llvm-libtool-darwin</code> supports the following options:</p>
<dl>
<dt><code>-arch_only &lt;architecture&gt;</code></dt>
<dd> Build a static library only for the specified <i>&lt;architecture&gt;</i> and ignore all other architectures in the files.</dd>
<dt><code>-color</code></dt>
<dd> Use colors in output.</dd>
<dt><code>-D</code></dt>
<dd> Use zero for timestamps and UIDs/GIDs. This is set by default.</dd>
<dt><code>-filelist &lt;listfile[,dirname]&gt;</code></dt>
<dd> Read input file names from <i>&lt;listfile&gt;</i>. File names are specified in <i>&lt;listfile&gt;</i> one per line, separated only by newlines. Whitespace on a line is assumed to be part of the filename. If the directory name, <i>dirname</i>, is also specified then it is prepended to each file name in the <i>&lt;listfile&gt;</i>.</dd>
<dt><code>-h, -help</code></dt>
<dd> Show help and usage for this command.</dd>
<dt><code>-help-list</code></dt>
<dd> Show help and usage for this command without grouping the options into categories.</dd>
<dt><code>-l &lt;x&gt;</code></dt>
<dd> Searches for the library libx.a in the library search path. If the string <i>&lt;x&gt;</i> ends with ‘.o’, then the library ‘x’ is searched for without prepending ‘lib’ or appending ‘.a’. If the library is found, it is added to the list of input files. Otherwise, an error is raised.</dd>
<dt><code>-L &lt;dir&gt;</code></dt>
<dd> Adds <i>&lt;dir&gt;</i> to the list of directories in which to search for libraries. The directories are searched in the order in which they are specified with <i>-L</i> and before the default search path. The default search path includes directories <i>/lib</i>, <i>/usr/lib</i> and <i>/usr/local/lib</i>.</dd>
<dt><code>-no_warning_for_no_symbols</code></dt>
<dd> Do not warn about files that have no symbols.</dd>
<dt><code>-o &lt;filename&gt;</code></dt>
<dd> Specify the output file name. Must be specified exactly once.</dd>
<dt><code>-static</code></dt>
<dd> Produces a static library from the input files.</dd>
<dt><code>-U</code></dt>
<dd> Use actual timestamps and UIDs/GIDs.</dd>
<dt><code>-V</code></dt>
<dd> Display the version of this program and perform any operation specified.</dd>
<dt><code>-version</code></dt>
<dd> Display the version of this program and exit immediately.</dd></dl>
<h2>EXIT STATUS</h2>
<p> <code>llvm-libtool-darwin</code> exits with a non-zero exit code if there is an error. Otherwise, it exits with code 0.</p>
<h2>BUGS</h2>
<p> To report bugs, please visit &lt;<i><a rel="nofollow" href="https://github.com/llvm/llvm-project/issues/">https://github.com/llvm/llvm-project/issues/</a></i>&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-llvm-ar/">llvm-ar</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
