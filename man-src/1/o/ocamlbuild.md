---
title: "ocamlbuild(1)"
name: "ocamlbuild"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ocamlbuild/"
description: "ocamlbuild – The OCaml project compilation tool"
---

<h2 class="name">NAME</h2>
<p> ocamlbuild &#8211; The OCaml project compilation tool </p>
<h2>SYNOPSIS</h2>
<p> <code>ocamlbuild</code> [ <code>-Is &nbsp;<wbr>dir1,&#8230;</code> ] [ <code>-libs</code><i>&nbsp;<wbr>lib1,&#8230;</i> ] [ <code>-lflags</code><i>&nbsp;<wbr>flag1,&#8230;</i> ] [ <code>-pp</code><i>&nbsp;<wbr>flags</i> ] [ <code>-tags</code><i>&nbsp;<wbr>tag1,&#8230;</i> ] [ <code>-j &nbsp;<wbr>parallel-jobs</code> ] <i>target.native</i> [ <code>&#8212; arg1 arg2 &#8230;</code> ] </p>
<p> <i>(same options)</i> </p>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-ocamlbuild/">ocamlbuild</a></code>(1) orchestrates the compilation process of your OCaml project. It is similar in function to <code><a href="/docs/linux/man/1-make/">make</a></code>(1) except that it is tailor-made to automatically compile most OCaml projects with very little user input. </p>
<p> <code>ocamlbuild</code> should be invoked in the root of a clean project tree (e.g., with no leftover compilation files). Given one or more targets to compile, it scans the required subdirectories to gather information about the various files present, running tools such as <code><a href="/docs/linux/man/1-ocamldep/">ocamldep</a></code>(1) to extract dependency information, and gathering optional files that fine-tune its behaviour. Target names are very significant. </p>
<h2>TARGET NAMES</h2>
<p> <code>ocamlbuild</code> uses a set of target naming conventions to select the kind of objects to produce. Target names are of the form <code>base.extension</code> where <code>base</code> is usually the name of the underlying OCaml module and <code>extension</code> denotes the kind of object to produce from that file &#8212; a byte code executable, a native executable, documentation&#8230; Of course extensions such as <code>.cmo,</code> <code>.cma,</code> <code>.cmi&#8230;</code> map to their usual counterparts. Here is a list of the most important <code>ocamlbuild</code>-specific extensions: </p>
<dl>
<dt><code>.native</code></p>
<dd> Native code executable </p>
<dt><code>.byte</code></p>
<dd> Byte code executable </p>
<dt><code>.inferred.mli</code></p>
<dd> Interface inferred with <code>ocamlc</code>-i </p>
<dt><code>.docdir/index.html</code></p>
<dd> HTML documentation generated with <code>ocamldoc</code> </p>
</dl>
<h2>OPTIONS</h2>
<p> The following command-line options are recognized by <code><a href="/docs/linux/man/1-ocamlbuild/">ocamlbuild</a></code>(1). </p>
<dl>
<dt><code>-version</code></p>
<dd> Display the version</p>
<dt><code>-quiet</code></p>
<dd> Make as quiet as possible</p>
<dt><code>-verbose</code> &lt;level&gt;</p>
<dd> Set the verbose level</p>
<dt><code>-documentation</code></p>
<dd> Show rules and flags</p>
<dt><code>-log</code> &lt;file&gt;</p>
<dd> Set log file</p>
<dt><code>-no-log</code></p>
<dd> No log file</p>
<dt><code>-clean</code></p>
<dd> Remove build directory and other files, then exit</p>
<dt><code>-I</code> &lt;path&gt;</p>
<dd> Add to include directories</p>
<dt><code>-Is</code> &lt;path,&#8230;&gt;</p>
<dd> (same as above, but accepts a comma-separated list)</p>
<dt><code>-X</code> &lt;path&gt;</p>
<dd> Directory to ignore</p>
<dt><code>-Xs</code> &lt;path,&#8230;&gt;</p>
<dd> (idem)</p>
<dt><code>-lib</code> &lt;flag&gt;</p>
<dd> Link to this ocaml library</p>
<dt><code>-libs</code> &lt;flag,&#8230;&gt;</p>
<dd> (idem)</p>
<dt><code>-lflag</code> &lt;flag&gt;</p>
<dd> Add to ocamlc link flags</p>
<dt><code>-lflags</code> &lt;flag,&#8230;&gt;</p>
<dd> (idem)</p>
<dt><code>-cflag</code> &lt;flag&gt;</p>
<dd> Add to ocamlc compile flags</p>
<dt><code>-cflags</code> &lt;flag,&#8230;&gt;</p>
<dd> (idem)</p>
<dt><code>-yaccflag</code> &lt;flag&gt;</p>
<dd> Add to ocamlyacc flags</p>
<dt><code>-yaccflags</code> &lt;flag,&#8230;&gt;</p>
<dd> (idem)</p>
<dt><code>-lexflag</code> &lt;flag&gt;</p>
<dd> Add to ocamllex flags</p>
<dt><code>-lexflags</code> &lt;flag,&#8230;&gt;</p>
<dd> (idem)</p>
<dt><code>-ppflag</code> &lt;flag&gt;</p>
<dd> Add to ocaml preprocessing flags</p>
<dt><code>-pp</code> &lt;flag,&#8230;&gt;</p>
<dd> (idem)</p>
<dt><code>-tag</code> &lt;tag&gt;</p>
<dd> Add to default tags</p>
<dt><code>-tags</code> &lt;tag,&#8230;&gt;</p>
<dd> (idem)</p>
<dt><code>-ignore</code> &lt;module,&#8230;&gt;</p>
<dd> Don&#8217;t try to build these modules</p>
<dt><code>-no-links</code></p>
<dd> Don&#8217;t make links of produced final targets</p>
<dt><code>-no-skip</code></p>
<dd> Don&#8217;t skip modules that are requested by ocamldep but cannot be built</p>
<dt><code>-no-hygiene</code></p>
<dd> Don&#8217;t apply sanity-check rules</p>
<dt><code>-no-plugin</code></p>
<dd> Don&#8217;t build myocamlbuild.ml</p>
<dt><code>-no-stdlib</code></p>
<dd> Don&#8217;t ignore stdlib modules</p>
<dt><code>-just-plugin</code></p>
<dd> Just build myocamlbuild.ml</p>
<dt><code>-byte-plugin</code></p>
<dd> Don&#8217;t use a native plugin but bytecode</p>
<dt><code>-no-sanitize</code></p>
<dd> Do not enforce sanity-check rules</p>
<dt><code>-nothing-should-be-rebuilt</code></p>
<dd> Fail if something needs to be rebuilt</p>
<dt><code>-classic-display</code></p>
<dd> Display executed commands the old-fashioned way</p>
<dt><code>-j</code> &lt;N&gt;</p>
<dd> Allow N jobs at once (0 for unlimited)</p>
<dt><code>-build-dir</code> &lt;path&gt;</p>
<dd> Set build directory</p>
<dt><code>-install-dir</code> &lt;path&gt;</p>
<dd> Set the install directory</p>
<dt><code>-where</code></p>
<dd> Display the install directory</p>
<dt><code>-ocamlc</code> &lt;command&gt;</p>
<dd> Set the OCaml bytecode compiler</p>
<dt><code>-ocamlopt</code> &lt;command&gt;</p>
<dd> Set the OCaml native compiler</p>
<dt><code>-ocamldep</code> &lt;command&gt;</p>
<dd> Set the OCaml dependency tool</p>
<dt><code>-ocamlyacc</code> &lt;command&gt;</p>
<dd> Set the ocamlyacc tool</p>
<dt><code>-ocamllex</code> &lt;command&gt;</p>
<dd> Set the ocamllex tool</p>
<dt><code>-ocamlrun</code> &lt;command&gt;</p>
<dd> Set the ocamlrun tool</p>
<dt><code>&#8212;</code></p>
<dd> Stop argument processing, remaining arguments are given to the user program</p>
<dt><code>-help</code></p>
<dd> Display the list of options</p>
<dt><code>&#8211;help</code></p>
<dd> Display the list of options</dl>
<h2>SEE ALSO</h2>
<p> The <code>ocamlbuild</code> manual, <code><a href="/docs/linux/man/1-ocaml/">ocaml</a></code>(1), <code><a href="/docs/linux/man/1-make/">make</a></code>(1).<br />
 <i>The OCaml user&#8217;s manual, chapter Batch compilation.</i> </p>
<h2>Index</h2>
