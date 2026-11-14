---
title: "discount-theme(1)"
name: "discount-theme"
section: "1"
letter: "d"
url: "/docs/linux/man/1-discount-theme/"
description: "theme – create a web page from a template file"
---

<h2 class="name">NAME</h2>
<p> <code>theme</code> &#8211; create a web page from a template file </p>
<h2>SYNOPSIS</h2>
<p> [-<code>C option-flags </code> ] [-<code>c options </code> ] [-<code>d root </code> ] [-<code>E</code> ] [-<code>f</code> ] [-<code>o file </code> ] [-<code>p pagename </code> ] [-<code>t template </code> ] [-<code>V</code> ] [textfile ]</p>
<h2>DESCRIPTION</h2>
<p> The utility takes a <a href="/docs/linux/man/7-markdown/">markdown</a>(7)Ns-formatted textfile (or stdin if not specified,) compiles it, and combines it with a <i>template</i> Po page.theme by default Pc to produce a web page. If a path to the template is not specified, looks for page.theme in the current directory, then each parent directory up to the document root Po set with &#8211;<code>d</code> or, if unset, the <i>root directory</i> of the system. Pc If page.theme is found, copies it to the output, looking for <i>&lt;?theme action?&gt;</i> html tags and processing the embedded <i>action </i> as appropriate. </p>
<p> processes the following actions:</p>
<dl>
<dt><i>author</i></p>
<dd> Prints the author name(s) from the mkd_doc_author3 function.</p>
<dt><i>body</i></p>
<dd> Prints the formatted <a href="/docs/linux/man/7-markdown/">markdown</a>(7) input file.</p>
<dt><i>date</i></p>
<dd> Prints the date returned by mkd_doc_date3 or, if none, the date the input file was last modified.</p>
<dt><i>dir</i></p>
<dd> Prints the directory part of the pagename</p>
<dt><i>include </i><code>(file ) </code></p>
<dd> Prints the contents of file <a href="/docs/linux/man/7-markdown/">Markdown</a>(7) translation will <i>NOT</i> be done on this file.</p>
<dt><i>source</i></p>
<dd> The filename part of the pagename.</p>
<dt><i>style</i></p>
<dd> Print any stylesheets (see mkd-extensions7 ) found in the input file.</p>
<dt><i>title</i></p>
<dd> Print the title returned by mkd_doc_title3, or, if that does not exist, the source filename.</p>
<dt><i>version</i></p>
<dd> Print the version of <a href="/docs/linux/man/7-discount/">discount</a>(7) that this copy of theme was compiled with.</dl>
<p> If input is coming from a file and the output was not set with the &#8211;<code>o</code> option, <code>writes the output to</code> file-sans-text.html (if ) <i>file</i> has a .text suffix, that will be stripped off and replaced with .html otherwise a .html will be appended to the end of the filename.) </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-d root </code></p>
<dd> Set the <i>document root</i> to <i>root</i></p>
<dt><code>-E</code></p>
<dd> Normally theme will not expand &lt;?theme body?&gt; or &lt;?theme toc?&gt; in the &lt;head&gt; section, or &lt;?theme style?&gt; in the &lt;body&gt; section, but the &#8211;<code>E</code> option overrides this and allows expansions everywhere.</p>
<dt><code>-f</code></p>
<dd> Forcibly overwrite existing html files.</p>
<dt><code>-o filename </code></p>
<dd> Write the output to <i>filename</i></p>
<dt><code>-p </code><i>path</i></p>
<dd> Set the pagename to <i>path</i></p>
<dt><code>-t </code><i>filename</i></p>
<dd> Use <i>filename</i> as the template file.</dl>
<h2>RETURN VALUES</h2>
<p> The utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-markdown/">markdown</a>(1), <a href="/docs/linux/man/3-markdown/">markdown</a>(3), <a href="/docs/linux/man/7-markdown/">markdown</a>(7), mkd-extensions7.</p>
<h2>AUTHOR</h2>
<p> An David Parsons (<code>orc [at] pell.portland.or.us</code> ) </p>
<h2>Index</h2>
