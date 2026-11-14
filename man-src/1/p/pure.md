---
title: "pure(1)"
name: "pure"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pure/"
description: "pure – the Pure interpreter"
---

<h2>NAME</h2>
<p> pure &#8211; the Pure interpreter</p>
<h2>SYNOPSIS</h2>
<p> <code>pure</code> [<i>options</i> &#8230;] [<i>script</i> &#8230;] [&#8211; <i>args</i> &#8230;]<br />
 <code>pure</code> [<i>options</i> &#8230;] -x <i>script</i> [<i>args</i> &#8230;]</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Batch compilation.</p>
<dt><code>&#8211;ctags</code>, <code>&#8211;etags</code></p>
<dd> Create a tags file in ctags (vi) or etags (emacs) format.</p>
<dt><code>&#8211;eager-jit</code></p>
<dd> Enable eager JIT compilation. This requires LLVM 2.7 or later, otherwise this flag will be ignored.</p>
<dt><code>-fPIC</code>, <code>-fpic</code></p>
<dd> Create position-independent code (batch compilation).</p>
<dt><code>-g</code></p>
<dd> Enable symbolic debugging.</p>
<dt><code>&#8211;help</code>, <code>-h</code></p>
<dd> Print help message and exit.</p>
<dt><code>-i</code></p>
<dd> Force interactive mode (read commands from stdin).</p>
<dt><code>-I</code><i>directory</i></p>
<dd> Add a directory to be searched for included source scripts.</p>
<dt><code>-L</code><i>directory</i></p>
<dd> Add a directory to be searched for dynamic libraries.</p>
<dt><code>-l</code><i>libname</i></p>
<dd> Library to be linked in batch compilation.</p>
<dt><code>&#8211;noediting</code></p>
<dd> Disable command-line editing.</p>
<dt><code>&#8211;noprelude</code>, <code>-n</code></p>
<dd> Do not load the prelude.</p>
<dt><code>&#8211;norc</code></p>
<dd> Do not run the interactive startup files.</p>
<dt><code>-o</code><i>filename</i></p>
<dd> Output filename for batch compilation.</p>
<dt><code>-q</code></p>
<dd> Quiet startup (suppresses sign-on message in interactive mode).</p>
<dt><code>-T</code><i>filename</i></p>
<dd> Tags file to be written by &#8211;ctags or &#8211;etags.</p>
<dt><code>-u</code></p>
<dd> Do not strip unused functions in batch compilation.</p>
<dt><code>-v</code>[<i>level</i>]</p>
<dd> Set verbosity level.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version information and exit.</p>
<dt><code>-w</code></p>
<dd> Enable compiler warnings about various dubious constructs and backward compatibility issues.</p>
<dt><code>-x</code></p>
<dd> Execute script with given command line arguments.</p>
<dt><code>&#8212;</code></p>
<dd> Stop option processing and pass the remaining command line arguments in the <code>argv</code> variable.</dl>
<h2>DESCRIPTION</h2>
<p> Pure is a modern-style functional programming language based on term rewriting. Pure programs are basically collections of equational rules used to evaluate expressions in a symbolic fashion by reducing them to normal form. </p>
<p> <code>pure</code> is the Pure interpreter. The interpreter has an LLVM backend which JIT-compiles Pure programs to machine code, hence programs run blazingly fast and interfacing to C modules is easy, while the interpreter still provides a convenient, fully interactive environment for running Pure scripts and evaluating expressions. </p>
<p> Basically, to run a Pure script with the interpreter, just specifiy the filename of the script on the command line. You can also invoke the interpreter without arguments, in which case it starts up in interactive mode. Or you can compile a script to a native executable (as well as a number of other recognized LLVM and native code formats) with the <code>-c</code> option (use <code>-o</code> to specify the output filename); this requires that you have some parts of the LLVM toolchain (llc, opt) as well as gcc installed. Last but not least, you can create a tags file for use with <code><a href="/docs/linux/man/1-emacs/">emacs</a></code>(1) or <code><a href="/docs/linux/man/1-vi/">vi</a></code>(1) with the <code>&#8211;etags</code> and <code>&#8211;ctags</code> options. </p>
<p> The full version of this manual can be read inside the interpreter, by typing <code>help</code> on the interpreter&#8217;s command line. This requires <code><a href="/docs/linux/man/1-w3m/">w3m</a></code>(1) to work. (You can also set the name of another html browser to use with the <code>PURE_HELP</code> or the <code>BROWSER</code> environment variable.)</p>
<h2>FILES</h2>
<dl>
<dt><code>a.out</code></p>
<dd> Default output filename for batch compilation (-c).</p>
<dt><code>~/.pure_history</code></p>
<dd> Interactive command history.</p>
<dt><code>~/.purerc</code>, <code>.purerc</code>, <code>.pure</code></p>
<dd> Interactive startup files. The latter is usually a dump from a previous interactive session.</p>
<dt><code>prelude.pure</code></p>
<dd> Standard prelude. If available, this script is loaded before any other definitions, unless <code>-n</code> was specified.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>BROWSER</code></p>
<dd> If the <code>PURE_HELP</code> variable is not set (see below), this specifies a colon-separated list of browsers to try for reading the online documentation. See <i><a rel="nofollow" href="http://www.catb.org/~esr/BROWSER/">http://www.catb.org/~esr/BROWSER/</a></i>.</p>
<dt><code>PURELIB</code></p>
<dd> Directory to search for library scripts, including the prelude. If <code>PURELIB</code> is not set, it defaults to some location specified at installation time.</p>
<dt><code>PURE_EAGER_JIT</code></p>
<dd> Enable eager JIT compilation (same as <code>&#8211;eager-jit</code>).</p>
<dt><code>PURE_HELP</code></p>
<dd> Browser to use to read online documentation in the interpreter. By default, <code><a href="/docs/linux/man/1-w3m/">w3m</a></code>(1) is used.</p>
<dt><code>PURE_INCLUDE</code></p>
<dd> Additional directories (in colon-separated format) to be searched for included scripts.</p>
<dt><code>PURE_LIBRARY</code></p>
<dd> Additional directories (in colon-separated format) to be searched for dynamic libraries.</p>
<dt><code>PURE_MORE</code></p>
<dd> Shell command to be used for paging through output of the <code>show</code> command, when the interpreter runs in interactive mode.</p>
<dt><code>PURE_PS</code></p>
<dd> Command prompt used in the interactive command loop (&quot;&gt;&nbsp;<wbr>&quot; by default).</p>
<dt><code>PURE_STACK</code></p>
<dd> Maximum stack size in kilobytes (default: 0 = unlimited).</dl>
<h2>LICENSE</h2>
<p> LGPL V3 or later. See the accompanying COPYING file for details.</p>
<h2>AUTHOR</h2>
<p> Albert Graef &lt;Dr.Graef [at] t-online.de&gt;, Dept. of Computer Music, Johannes Gutenberg University of Mainz, Germany.</p>
<h2>SEE ALSO</h2>
<p> You can find the latest releases and the mailing list at the Pure website, <i><a rel="nofollow" href="http://pure-lang.googlecode.com">http://pure-lang.googlecode.com</a></i>. </p>
<h2>Index</h2>
