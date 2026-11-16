---
title: "rustdoc(1)"
name: "rustdoc"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rustdoc/"
description: "rustdoc – generate documentation from Rust source code"
---

<h2>NAME</h2>
<p> rustdoc &#8211; generate documentation from Rust source code</p>
<h2>SYNOPSIS</h2>
<p> <code>rustdoc</code> [<i>OPTIONS</i>] <i>INPUT</i> </p>
<h2>DESCRIPTION</h2>
<p> This tool generates API reference documentation by extracting comments from source code written in the Rust language, available at &lt;<code><a rel="nofollow" href="https://www.rust-lang.org">https://www.rust-lang.org</a></code>&gt;. It accepts several input formats and provides several output formats for the generated documentation. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r</code>, <code>&#8211;input-format</code> <i>FORMAT</i></dt>
<dd> html or json (default: inferred)</dd>
<dt><code>-w</code>, <code>&#8211;output-format</code> <i>FORMAT</i></dt>
<dd> html or json (default: html)</dd>
<dt><code>-o</code>, <code>&#8211;output</code> <i>OUTPUT</i></dt>
<dd> where to place the output (default: <i>doc/</i> for html, <i>doc.json</i> for json)</dd>
<dt><code>&#8211;passes</code> <i>LIST</i></dt>
<dd> space-separated list of passes to run (default: &#8221;)</dd>
<dt><code>&#8211;no-defaults</code></dt>
<dd> don&#8217;t run the default passes</dd>
<dt><code>&#8211;plugins</code> <i>LIST</i></dt>
<dd> space-separated list of plugins to run (default: &#8221;)</dd>
<dt><code>&#8211;plugin-path</code> <i>DIR</i></dt>
<dd> directory to load plugins from (default: <i>/tmp/rustdoc_ng/plugins</i>)</dd>
<dt><code>&#8211;target</code> <i>TRIPLE</i></dt>
<dd> target triple to document</dd>
<dt><code>&#8211;crate-name</code> <i>NAME</i></dt>
<dd> specify the name of this crate</dd>
<dt><code>-L</code>, <code>&#8211;library-path</code> <i>DIR</i></dt>
<dd> directory to add to crate search path</dd>
<dt><code>&#8211;cfg</code> <i>SPEC</i></dt>
<dd> pass a <i>&#8211;cfg</i> to rustc</dd>
<dt><code>&#8211;extern</code> <i>VAL</i></dt>
<dd> pass an <i>&#8211;extern</i> to rustc</dd>
<dt><code>&#8211;test</code></dt>
<dd> run code examples as tests</dd>
<dt><code>&#8211;test-args</code> <i>ARGS</i></dt>
<dd> pass arguments to the test runner</dd>
<dt><code>&#8211;html-in-header</code> <i>FILE</i></dt>
<dd> file to add to &lt;head&gt;</dd>
<dt><code>&#8211;html-before-content</code> <i>FILE</i></dt>
<dd> file to add in &lt;body&gt;, before content</dd>
<dt><code>&#8211;html-after-content</code> <i>FILE</i></dt>
<dd> file to add in &lt;body&gt;, after content</dd>
<dt><code>&#8211;markdown-css</code> <i>FILE</i></dt>
<dd> CSS files to include via &lt;link&gt; in a rendered Markdown file</dd>
<dt><code>&#8211;markdown-playground-url</code> <i>URL</i></dt>
<dd> URL to send code snippets to</dd>
<dt><code>&#8211;markdown-no-toc</code></dt>
<dd> don&#8217;t include table of contents</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Print help</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Print rustdoc&#8217;s version </dd>
</dl>
<h2>OUTPUT FORMATS</h2>
<p> The rustdoc tool can generate output in either an HTML or JSON format. </p>
<p> If using an HTML format, then the specified output destination will be the root directory of an HTML structure for all the documentation. Pages will be placed into this directory, and source files will also possibly be rendered into it as well. </p>
<p> If using a JSON format, then the specified output destination will have the rustdoc output serialized as JSON into it. This output format exists to pre-compile documentation for crates, and for usage in non-rustdoc tools. The JSON output is the following hash: </p>
<p>&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;schema&quot;: VERSION,<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;crate&quot;: &#8230;,<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;plugins&quot;: &#8230;,<br />
&nbsp;<wbr>} </p>
<p> The schema version indicates what the structure of crate/plugins will look like. Within a schema version the structure will remain the same. The <i>crate</i> field will contain all relevant documentation for the source being documented, and the <i>plugins</i> field will contain the output of the plugins run over the crate. </p>
<h2>EXAMPLES</h2>
<p> To generate documentation for the source in the current directory:<br />
&nbsp;<wbr>$&nbsp;<wbr>rustdoc hello.rs </p>
<p> List all available passes that rustdoc has, along with default passes:<br />
&nbsp;<wbr>$&nbsp;<wbr>rustdoc &#8211;passes list </p>
<p> To precompile the documentation for a crate, and then use it to render html at a later date:<br />
&nbsp;<wbr>$&nbsp;<wbr>rustdoc -w json hello.rs<br />
&nbsp;<wbr>$&nbsp;<wbr>rustdoc doc.json </p>
<p> The generated HTML can be viewed with any standard web browser. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rustc/">rustc</a></code>(1) </p>
<h2>BUGS</h2>
<p> See &lt;<code><a rel="nofollow" href="https://github.com/rust-lang/rust/issues">https://github.com/rust-lang/rust/issues</a></code>&gt; for issues. </p>
<h2>AUTHOR</h2>
<p> See <i>AUTHORS.txt</i> in the Rust source distribution. </p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See <i>COPYRIGHT</i> file in the rust source distribution. </p>
<h2>Index</h2>
