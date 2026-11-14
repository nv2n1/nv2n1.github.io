---
title: "makeglossaries-lite(1)"
name: "makeglossaries-lite"
section: "1"
letter: "m"
url: "/docs/linux/man/1-makeglossaries-lite/"
description: "makeglossaries-lite – Calls makeindex/xindy for LaTeX documents using glossaries package"
---

<h2 class="name">NAME</h2>
<p> makeglossaries-lite &#8211; Calls makeindex/xindy for LaTeX documents using glossaries package </p>
<h2>SYNOPSIS</h2>
<p> <code>makeglossaries</code> [<code>-o</code> <i>file</i>] [<code>-q</code>] [<code>-n</code>] [<code>-s</code> <i>file</i>] [<code>-t</code> <i>file</i>] [<code>-L</code> <i>language</i>] [<code>-c</code>] [<code>-g</code>] [<code>-l</code>] [<code>-p</code> <i>num</i>] [<code>-r</code>] [<code>-m</code> <i>file</i>] [<code>-x</code> <i>file</i>] [<code>&#8211;version</code>] [<code>&#8211;help</code>] <i>basename</i></p>
<h2>DESCRIPTION</h2>
<p> <code>makeglossaries-lite</code> is cut-down Lua alternative to the <code>makeglossaries</code> Perl script. It&#8217;s designed for use with LaTeX documents that use the glossaries package. Some options that are available to <code>makeglossaries</code> aren&#8217;t available with <code>makeglossaries-lite</code>. The mandatory argument <i>basename</i> should be the name of the LaTeX document without the .tex extension. <code>makeglossaries-lite</code> will read the auxiliary file to determine whether <code>makeindex</code> or <code>xindy</code> should be called. All the information required to be passed to the relevant indexing application should also be contained in the auxiliary file, but may be overridden by the option arguments to <code>makeglossaries-lite</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-q</code></p>
<dd> Quiet mode. Reduces chatter to standard output.</p>
<dt><code>-n</code></p>
<dd> Print the commands that would normally be executed but don&#8217;t run them.</p>
<dt><code>-o</code> <i>file</i></p>
<dd> Use <i>file</i> as the output file. (Only suitable for documents containing a single glossary, otherwise each glossary will be overridden.)</p>
<dt><code>-s</code> <i>file</i></p>
<dd> Use <i>file</i> as the style file. Note that if you use this option, you need to know whether <code>makeindex</code> or <code>xindy</code> will be called, as they have different style files.</p>
<dt><code>-t</code> <i>file</i></p>
<dd> Use <i>file</i> as the transcript file.</p>
<dt><code>-l</code></p>
<dd> Letter ordering.</p>
<dt><code>-L</code> <i>language</i></p>
<dd> This option only has an effect if <code>xindy</code> is called. Sets the language. See <code>xindy</code> documentation for further details.</p>
<dt><code>-c</code></p>
<dd> Compress intermediate blanks (<code>makeindex</code> only).</p>
<dt><code>-g</code></p>
<dd> Employ German word ordering (<code>makeindex</code> only).</p>
<dt><code>-p</code> <i>num</i></p>
<dd> Sets the starting page number to be <i>num</i> (<code>makeindex</code> only).</p>
<dt><code>-r</code></p>
<dd> Disable implicit page range formation (<code>makeindex</code> only).</p>
<dt><code>-m</code> <i>file</i></p>
<dd> Specify the full path name for <code>makeindex</code> to <i>file</i> in the event that <code>makeindex</code> isn&#8217;t on the operating system&#8217;s path.</p>
<dt><code>-x</code> <i>file</i></p>
<dd> Specify the full path name for <code>xindy</code> to <i>file</i> in the event that <code>xindy</code> isn&#8217;t on the operating system&#8217;s path.</p>
<dt><code>&#8211;version</code></p>
<dd> Prints version number and exits.</p>
<dt><code>&#8211;help</code></p>
<dd> Prints help message and exits.</dl>
<h2>REQUIRES</h2>
<p> texlua and makeindex or xindy (depending on glossaries package options).</p>
<h2>LICENSE</h2>
<p> This is free software distributed under the LaTeX Project Public License. There is <font SIZE="-1">NO WARRANTY.</font> See &lt;<a rel="nofollow" href="http://www.latex-project.org/lppl.txt">http://www.latex-project.org/lppl.txt</a>&gt; for details.</p>
<h2>AUTHOR</h2>
<p> Nicola L. C. Talbot, &lt;<a rel="nofollow" href="http://www.dickimaw-books.com/">http://www.dickimaw-books.com/</a>&gt;</p>
<h2>RECOMMENDED READING</h2>
<p> The glossaries manual: </p>
<pre>
        texdoc glossaries
</pre>
<h2>Index</h2>
