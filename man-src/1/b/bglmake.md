---

title: "bglmake(1)"
name: "bglmake"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bglmake/"
description: "bglmake – create or update Bigloo makefiles"
---

<p> <code>bglmake</code> [ options ] [ sourcefile ] </p>
<p> <code>bglmake</code> reads <i>sourcefile</i>, computes the transitive closure of the import relationship and generates a <i>makefile</i> file that can be used by the <code>glmake(1)</code> program to compile the application or the library. If no <i>sourcefile</i> is provided, then bglmake display the template file for generating Makefile. </p>
<h2>OPTIONS</h2>
<dl>
<dt>
</dt><dt><code>-v</code></dt>
<dd>
</dd><dd> Verbose mode </dd>
<dt><code>-q</code></dt>
<dd> Prevent loading the <i>~/.bglmakerc</i> user configuration file. </dd>
<dt><code>-suffix &lt;suf&gt;</code></dt>
<dd> Adds <i>suf</i> to the <code>bglmake</code> source file suffixes list. Default suffixes are &quot;scm&quot;, &quot;sch&quot; and &quot;bgl&quot;. </dd>
<dt><code>file</code></dt>
<dd> is the name of the &quot;main&quot; file for an application of the name of the &quot;heap&quot; file for a library. </dd>
<dt><code>-I&lt;path&gt;</code></dt>
<dd> Add <i>path</i> to the directory list read for searching Bigloo source files. </dd>
<dt><code>-X&lt;path&gt;</code></dt>
<dd> Exclude <i>path</i> from the directory list read for searching Bigloo source files. </dd>
<dt><code>-o &lt;makefile&gt;</code></dt>
<dd> The name of the <i>makefile</i> file to be updated </dd>
<dt><code>-p &lt;name&gt;</code></dt>
<dd> The <i>name</i> of the project. This name is used in backup and versionning entries. </dd>
<dt><code>-t &lt;name&gt;</code></dt>
<dd> The <i>name</i> of the target binary file or the name of the library. </dd>
<dt><code>-f&lt;template&gt;</code></dt>
<dd> Set an alternative template file. </dd>
<dt><code>-object &lt;obj&gt;</code></dt>
<dd> Update the makefile for adding <i>obj</i> to the object list. </dd>
<dt><code>-source &lt;src&gt;</code></dt>
<dd> Update the makefile for adding <i>src</i> to the source file list. </dd>
<dt><code>-main &lt;file&gt;</code></dt>
<dd> Set the initial main file and tells bglmake that the project is an &quot;application&quot; (by opposition to libraries). This <i>File</i> is the starting point of the transitive closure of the imported modules. </dd>
<dt><code>-heap &lt;file&gt;</code></dt>
<dd> Set the initial heap file and tells bglmake that the project is an &quot;library&quot; (by opposition to applications). This <i>File</i> is the starting point of the transitive closure of the imported modules. </dd>
</dl>
<h2>TEMPLATES</h2>
<p> When bglmake generates a <i>makefile</i>, it uses templates. Theses templates may be specified with some option or they be printed out. For that it is enough to call bglmake without any parameter. Template files uses some extra &quot;macro&quot;. They are: </p>
<dl>
<dt>
</dt><dt>$[PROJECT]</dt>
<dd>
</dd><dd> this macro is replaced with the project name (option -p). If no <i>-p</i> option is used the default project name is the name of the current directory that contains the <i>sourcefile</i>. </dd>
<dt>$[TARGET_NAME]</dt>
<dd> this macro is replaced with the target name (option -t). If no <i>-t</i> option is used the default target name is the name of the current directory that contains the <i>sourcefile</i>. </dd>
<dt>$[MAKEFILE]</dt>
<dd> this macro is replaced with the <i>makefile</i> name (-o option). </dd>
</dl>
<h2>EXAMPLE</h2>
<p> A Makefile is created by &#8220;bglmake foo.scm -o Makefile&#8221;. Then it may be updated with &#8220;make updatemakefile&#8221;. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-bigloo/">bigloo</a>(1), <a href="/docs/linux/man/1-bglafile/">bglafile</a>(1), <a href="/docs/linux/man/1-bgldepend/">bgldepend</a>(1), <a href="/docs/linux/man/1-bgltags/">bgltags</a>(1), <a href="/docs/linux/man/1-make/">make</a>(1), <a href="/docs/linux/man/1-bglmco/">bglmco</a>(1) </p>
<h2>AUTHOR</h2>
<p> Manuel SERRANO, Manuel.Serrano [at] inria.fr </p>
