---
title: "makeglossaries(1)"
name: "makeglossaries"
section: "1"
letter: "m"
url: "/docs/linux/man/1-makeglossaries/"
description: "makeglossaries – Calls makeindex/xindy for LaTeX documents using glossaries package"
---

<h2 class="name">NAME</h2>
<p> makeglossaries &#8211; Calls makeindex/xindy for LaTeX documents using glossaries package </p>
<h2>SYNOPSIS</h2>
<p> <code>makeglossaries</code> [<code>-o</code> <i>file</i>] [<code>-q</code>] [<code>-Q</code>] [<code>-k</code>] [<code>-n</code>] [<code>-s</code> <i>file</i>] [<code>-t</code> <i>file</i>] [<code>-L</code> <i>language</i>] [<code>-c</code>] [<code>-g</code>] [<code>-l</code>] [<code>-p</code> <i>num</i>] [<code>-r</code>] [<code>-d</code> <i>aux dir</i>] [<code>-m</code> <i>file</i>] [<code>-x</code> <i>file</i>] [<code>&#8211;version</code>] [<code>&#8211;help</code>] <i>basename</i></p>
<h2>DESCRIPTION</h2>
<p> <code>makeglossaries</code> is designed for use with LaTeX documents that use the glossaries package. The mandatory argument <i>basename</i> should be the name of the LaTeX document without the .tex extension. <code>makeglossaries</code> will read the auxiliary file to determine whether <code>makeindex</code> or <code>xindy</code> should be called. All the information required to be passed to the relevant indexing application should also be contained in the auxiliary file, but may be overridden by the option arguments to <code>makeglossaries</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-q</code></dt>
<dd> Quiet mode. Reduces chatter to standard output.</dd>
<dt><code>-Q</code></dt>
<dd> Silences warning about being unable to fork.</dd>
<dt><code>-k</code></dt>
<dd> Don&#8217;t try forking with piped redirection. (Lessens the effect of -q)</dd>
<dt><code>-n</code></dt>
<dd> Print the commands that would normally be executed but don&#8217;t run them.</dd>
<dt><code>-o</code> <i>file</i></dt>
<dd> Use <i>file</i> as the output file. (Only suitable for documents containing a single glossary, otherwise each glossary will be overridden.)</dd>
<dt><code>-s</code> <i>file</i></dt>
<dd> Use <i>file</i> as the style file. Note that if you use this option, you need to know whether <code>makeindex</code> or <code>xindy</code> will be called, as they have different style files.</dd>
<dt><code>-t</code> <i>file</i></dt>
<dd> Use <i>file</i> as the transcript file.</dd>
<dt><code>-l</code></dt>
<dd> Letter ordering.</dd>
<dt><code>-L</code> <i>language</i></dt>
<dd> This option only has an effect if <code>xindy</code> is called. Sets the language. See <code>xindy</code> documentation for further details.</dd>
<dt><code>-c</code></dt>
<dd> Compress intermediate blanks (<code>makeindex</code> only).</dd>
<dt><code>-g</code></dt>
<dd> Employ German word ordering (<code>makeindex</code> only).</dd>
<dt><code>-p</code> <i>num</i></dt>
<dd> Sets the starting page number to be <i>num</i> (<code>makeindex</code> only).</dd>
<dt><code>-r</code></dt>
<dd> Disable implicit page range formation (<code>makeindex</code> only).</dd>
<dt><code>-d</code> <i>aux dir</i></dt>
<dd> Specify the directory the .aux, .glo etc files are located. Defaults to the parent directory of the base file <i>filename</i>.</dd>
<dt><code>-m</code> <i>file</i></dt>
<dd> Specify the full path name for <code>makeindex</code> to <i>file</i> in the event that <code>makeindex</code> isn&#8217;t on the operating system&#8217;s path.</dd>
<dt><code>-x</code> <i>file</i></dt>
<dd> Specify the full path name for <code>xindy</code> to <i>file</i> in the event that <code>xindy</code> isn&#8217;t on the operating system&#8217;s path.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Prints version number and exits.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Prints help message and exits.</dd></dl>
<h2>REQUIRES</h2>
<p> Perl, Getopt::Std, and makeindex or xindy (depending on glossaries package options).</p>
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
