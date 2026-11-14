---
title: "clang-format(1)"
name: "clang-format"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clang-format/"
description: "clang-format – manual page for clang-format 10"
---

<h2 class="name">NAME</h2>
<p> clang-format &#8211; manual page for clang-format 10 </p>
<h2>DESCRIPTION</h2>
<p> OVERVIEW: A tool to format C/C++/Java/JavaScript/Objective-C/Protobuf/C# code. </p>
<p> If no arguments are specified, it formats the code from standard input and writes the result to the standard output. If &lt;file&gt;s are given, it reformats the files. If <code>-i</code> is specified together with &lt;file&gt;s, the files are edited in-place. Otherwise, the result is written to the standard output. </p>
<p> USAGE: clang-format [options] [&lt;file&gt; &#8230;] </p>
<p> OPTIONS: </p>
<p> Clang-format options:</p>
<dl>
<dt> <code>&#8211;Werror</code> &#8211; If set, changes formatting warnings to errors</p>
<dt><code>&#8211;assume-filename=</code>&lt;string&gt; &#8211; Override filename used to determine the language.</p>
<dd>
<dd>When reading from stdin, clang-format assumes this filename to determine the language.</p>
<dt><code>&#8211;cursor=</code>&lt;uint&gt; &#8211; The position of the cursor when invoking</p>
<dd> clang-format from an editor integration</p>
<dt> <code>&#8211;dry-run</code> &#8211; If set, do not actually make the formatting changes</p>
<dt><code>&#8211;dump-config</code> &#8211; Dump configuration options to stdout and exit.</p>
<dd>
<dd>Can be used with <code>-style</code> option.</p>
<dt><code>&#8211;fallback-style=</code>&lt;string&gt; &#8211; The name of the predefined style used as a</p>
<dd> fallback in case clang-format is invoked with <code>-style</code>=<i>,file/</i>, but can not find the .clang-format file to use. Use <code>-fallback-style</code>=<i>,none/</i> to skip formatting.</p>
<dt> <code>&#8211;ferror-limit=</code>&lt;uint&gt; &#8211; Set the maximum number of clang-format errors to emit before stopping (0 = no limit). Used only with <code>&#8211;dry-run</code> or <code>-n</code></p>
<dt> <code>-i</code> &#8211; Inplace edit &lt;file&gt;s, if specified.</p>
<dt><code>&#8211;length=</code>&lt;uint&gt; &#8211; Format a range of this length (in bytes).</p>
<dd>
<dd>Multiple ranges can be formatted by specifying several <code>-offset</code> and <code>-length</code> pairs. When only a single <code>-offset</code> is specified without <code>-length</code>, clang-format will format up to the end of the file. Can only be used with one input file.</p>
<dt><code>&#8211;lines=</code>&lt;string&gt; &#8211; &lt;start line&gt;:&lt;end line&gt; &#8211; format a range of</p>
<dd> lines (both 1-based). Multiple ranges can be formatted by specifying several <code>-lines</code> arguments. Can&#8217;t be used with <code>-offset</code> and <code>-length</code>. Can only be used with one input file.</p>
<dt> <code>-n</code> &#8211; Alias for <code>&#8211;dry-run</code></p>
<dt><code>&#8211;offset=</code>&lt;uint&gt; &#8211; Format a range starting at this byte offset.</p>
<dd>
<dd>Multiple ranges can be formatted by specifying several <code>-offset</code> and <code>-length</code> pairs. Can only be used with one input file.</p>
<dt> <code>&#8211;output-replacements-xml</code> &#8211; Output replacements as XML.</p>
<dt> <code>&#8211;sort-includes</code> &#8211; If set, overrides the include sorting behavior determined by the SortIncludes style flag</p>
<dt><code>&#8211;style=</code>&lt;string&gt; &#8211; Coding style, currently supports:</p>
<dd>
<dd>LLVM, Google, Chromium, Mozilla, WebKit.</p>
<dt>Use <code>-style</code>=<i>,file/</i> to load style configuration from</p>
<dd> .clang-format file located in one of the parent directories of the source file (or current directory for stdin). Use <code>-style=</code>&quot;{key: value, &#8230;}&quot; to set specific parameters, e.g.:</p>
<dt>
<dd> <code>-style=</code>&quot;{BasedOnStyle: llvm, IndentWidth: 8}&quot;</p>
<dt> <code>&#8211;verbose</code> &#8211; If set, shows the list of processed files</dl>
<dd>Generic Options:</p>
<dl>
<dt> <code>&#8211;help</code> &#8211; Display available options (<code>&#8211;help-hidden</code> for more)</p>
<dt> <code>&#8211;help-list</code> &#8211; Display list of available options (<code>&#8211;help-list-hidden</code> for more)</p>
<dt> <code>&#8211;version</code> &#8211; Display the version of this program </p>
</dl>
<h2>Index</h2>
