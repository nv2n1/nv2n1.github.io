---

title: "ocamlbuild(1)"
name: "ocamlbuild"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ocamlbuild/"
description: "ocamlbuild – The OCaml project compilation tool"
---

<p> <code>ocamlbuild</code> [ <code>-Is &nbsp;<wbr>dir1,&#8230;</code> ] [ <code>-libs</code><i>&nbsp;<wbr>lib1,&#8230;</i> ] [ <code>-lflags</code><i>&nbsp;<wbr>flag1,&#8230;</i> ] [ <code>-pp</code><i>&nbsp;<wbr>flags</i> ] [ <code>-tags</code><i>&nbsp;<wbr>tag1,&#8230;</i> ] [ <code>-j &nbsp;<wbr>parallel-jobs</code> ] <i>target.native</i> [ <code>&#8212; arg1 arg2 &#8230;</code> ] </p>
<p> <i>(same options)</i> </p>
<p> <code><a href="/docs/linux/man/1-ocamlbuild/">ocamlbuild</a></code>(1) orchestrates the compilation process of your OCaml project. It is similar in function to <code><a href="/docs/linux/man/1-make/">make</a></code>(1) except that it is tailor-made to automatically compile most OCaml projects with very little user input. </p>
<p> <code>ocamlbuild</code> should be invoked in the root of a clean project tree (e.g., with no leftover compilation files). Given one or more targets to compile, it scans the required subdirectories to gather information about the various files present, running tools such as <code><a href="/docs/linux/man/1-ocamldep/">ocamldep</a></code>(1) to extract dependency information, and gathering optional files that fine-tune its behaviour. Target names are very significant. </p>
<h2>TARGET NAMES</h2>
<p> <code>ocamlbuild</code> uses a set of target naming conventions to select the kind of objects to produce. Target names are of the form <code>base.extension</code> where <code>base</code> is usually the name of the underlying OCaml module and <code>extension</code> denotes the kind of object to produce from that file &#8212; a byte code executable, a native executable, documentation&#8230; Of course extensions such as <code>.cmo,</code> <code>.cma,</code> <code>.cmi&#8230;</code> map to their usual counterparts. Here is a list of the most important <code>ocamlbuild</code>-specific extensions: </p>
<dl>
<dt><code>.native</code></dt>
<dd> Native code executable </dd>
<dt><code>.byte</code></dt>
<dd> Byte code executable </dd>
<dt><code>.inferred.mli</code></dt>
<dd> Interface inferred with <code>ocamlc</code>-i </dd>
<dt><code>.docdir/index.html</code></dt>
<dd> HTML documentation generated with <code>ocamldoc</code> </dd>
</dl>
<h2>OPTIONS</h2>
<p> The following command-line options are recognized by <code><a href="/docs/linux/man/1-ocamlbuild/">ocamlbuild</a></code>(1). </p>
<dl>
<dt><code>-version</code></dt>
<dd> Display the version</dd>
<dt><code>-quiet</code></dt>
<dd> Make as quiet as possible</dd>
<dt><code>-verbose</code> &lt;level&gt;</dt>
<dd> Set the verbose level</dd>
<dt><code>-documentation</code></dt>
<dd> Show rules and flags</dd>
<dt><code>-log</code> &lt;file&gt;</dt>
<dd> Set log file</dd>
<dt><code>-no-log</code></dt>
<dd> No log file</dd>
<dt><code>-clean</code></dt>
<dd> Remove build directory and other files, then exit</dd>
<dt><code>-I</code> &lt;path&gt;</dt>
<dd> Add to include directories</dd>
<dt><code>-Is</code> &lt;path,&#8230;&gt;</dt>
<dd> (same as above, but accepts a comma-separated list)</dd>
<dt><code>-X</code> &lt;path&gt;</dt>
<dd> Directory to ignore</dd>
<dt><code>-Xs</code> &lt;path,&#8230;&gt;</dt>
<dd> (idem)</dd>
<dt><code>-lib</code> &lt;flag&gt;</dt>
<dd> Link to this ocaml library</dd>
<dt><code>-libs</code> &lt;flag,&#8230;&gt;</dt>
<dd> (idem)</dd>
<dt><code>-lflag</code> &lt;flag&gt;</dt>
<dd> Add to ocamlc link flags</dd>
<dt><code>-lflags</code> &lt;flag,&#8230;&gt;</dt>
<dd> (idem)</dd>
<dt><code>-cflag</code> &lt;flag&gt;</dt>
<dd> Add to ocamlc compile flags</dd>
<dt><code>-cflags</code> &lt;flag,&#8230;&gt;</dt>
<dd> (idem)</dd>
<dt><code>-yaccflag</code> &lt;flag&gt;</dt>
<dd> Add to ocamlyacc flags</dd>
<dt><code>-yaccflags</code> &lt;flag,&#8230;&gt;</dt>
<dd> (idem)</dd>
<dt><code>-lexflag</code> &lt;flag&gt;</dt>
<dd> Add to ocamllex flags</dd>
<dt><code>-lexflags</code> &lt;flag,&#8230;&gt;</dt>
<dd> (idem)</dd>
<dt><code>-ppflag</code> &lt;flag&gt;</dt>
<dd> Add to ocaml preprocessing flags</dd>
<dt><code>-pp</code> &lt;flag,&#8230;&gt;</dt>
<dd> (idem)</dd>
<dt><code>-tag</code> &lt;tag&gt;</dt>
<dd> Add to default tags</dd>
<dt><code>-tags</code> &lt;tag,&#8230;&gt;</dt>
<dd> (idem)</dd>
<dt><code>-ignore</code> &lt;module,&#8230;&gt;</dt>
<dd> Don&#8217;t try to build these modules</dd>
<dt><code>-no-links</code></dt>
<dd> Don&#8217;t make links of produced final targets</dd>
<dt><code>-no-skip</code></dt>
<dd> Don&#8217;t skip modules that are requested by ocamldep but cannot be built</dd>
<dt><code>-no-hygiene</code></dt>
<dd> Don&#8217;t apply sanity-check rules</dd>
<dt><code>-no-plugin</code></dt>
<dd> Don&#8217;t build myocamlbuild.ml</dd>
<dt><code>-no-stdlib</code></dt>
<dd> Don&#8217;t ignore stdlib modules</dd>
<dt><code>-just-plugin</code></dt>
<dd> Just build myocamlbuild.ml</dd>
<dt><code>-byte-plugin</code></dt>
<dd> Don&#8217;t use a native plugin but bytecode</dd>
<dt><code>-no-sanitize</code></dt>
<dd> Do not enforce sanity-check rules</dd>
<dt><code>-nothing-should-be-rebuilt</code></dt>
<dd> Fail if something needs to be rebuilt</dd>
<dt><code>-classic-display</code></dt>
<dd> Display executed commands the old-fashioned way</dd>
<dt><code>-j</code> &lt;N&gt;</dt>
<dd> Allow N jobs at once (0 for unlimited)</dd>
<dt><code>-build-dir</code> &lt;path&gt;</dt>
<dd> Set build directory</dd>
<dt><code>-install-dir</code> &lt;path&gt;</dt>
<dd> Set the install directory</dd>
<dt><code>-where</code></dt>
<dd> Display the install directory</dd>
<dt><code>-ocamlc</code> &lt;command&gt;</dt>
<dd> Set the OCaml bytecode compiler</dd>
<dt><code>-ocamlopt</code> &lt;command&gt;</dt>
<dd> Set the OCaml native compiler</dd>
<dt><code>-ocamldep</code> &lt;command&gt;</dt>
<dd> Set the OCaml dependency tool</dd>
<dt><code>-ocamlyacc</code> &lt;command&gt;</dt>
<dd> Set the ocamlyacc tool</dd>
<dt><code>-ocamllex</code> &lt;command&gt;</dt>
<dd> Set the ocamllex tool</dd>
<dt><code>-ocamlrun</code> &lt;command&gt;</dt>
<dd> Set the ocamlrun tool</dd>
<dt><code>&#8212;</code></dt>
<dd> Stop argument processing, remaining arguments are given to the user program</dd>
<dt><code>-help</code></dt>
<dd> Display the list of options</dd>
<dt><code>&#8211;help</code></dt>
<dd> Display the list of options</dd></dl>
<h2>SEE ALSO</h2>
<p> The <code>ocamlbuild</code> manual, <code><a href="/docs/linux/man/1-ocaml/">ocaml</a></code>(1), <code><a href="/docs/linux/man/1-make/">make</a></code>(1).<br />
 <i>The OCaml user&#8217;s manual, chapter Batch compilation.</i> </p>
