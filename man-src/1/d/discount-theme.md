---

title: "discount-theme(1)"
name: "discount-theme"
section: "1"
letter: "d"
url: "/docs/linux/man/1-discount-theme/"
description: "theme – create a web page from a template file"
---

<p> <code>theme</code> &#8211; create a web page from a template file </p>
<p> [-<code>C option-flags </code> ] [-<code>c options </code> ] [-<code>d root </code> ] [-<code>E</code> ] [-<code>f</code> ] [-<code>o file </code> ] [-<code>p pagename </code> ] [-<code>t template </code> ] [-<code>V</code> ] [textfile ]</p>
<p> The utility takes a <a href="/docs/linux/man/7-markdown/">markdown</a>(7)Ns-formatted textfile (or stdin if not specified,) compiles it, and combines it with a <i>template</i> Po page.theme by default Pc to produce a web page. If a path to the template is not specified, looks for page.theme in the current directory, then each parent directory up to the document root Po set with &#8211;<code>d</code> or, if unset, the <i>root directory</i> of the system. Pc If page.theme is found, copies it to the output, looking for <i>&lt;?theme action?&gt;</i> html tags and processing the embedded <i>action </i> as appropriate. </p>
<p> processes the following actions:</p>
<dl>
<dt><i>author</i></dt>
<dd> Prints the author name(s) from the mkd_doc_author3 function.</dd>
<dt><i>body</i></dt>
<dd> Prints the formatted <a href="/docs/linux/man/7-markdown/">markdown</a>(7) input file.</dd>
<dt><i>date</i></dt>
<dd> Prints the date returned by mkd_doc_date3 or, if none, the date the input file was last modified.</dd>
<dt><i>dir</i></dt>
<dd> Prints the directory part of the pagename</dd>
<dt><i>include </i><code>(file ) </code></dt>
<dd> Prints the contents of file <a href="/docs/linux/man/7-markdown/">Markdown</a>(7) translation will <i>NOT</i> be done on this file.</dd>
<dt><i>source</i></dt>
<dd> The filename part of the pagename.</dd>
<dt><i>style</i></dt>
<dd> Print any stylesheets (see mkd-extensions7 ) found in the input file.</dd>
<dt><i>title</i></dt>
<dd> Print the title returned by mkd_doc_title3, or, if that does not exist, the source filename.</dd>
<dt><i>version</i></dt>
<dd> Print the version of discount(7) that this copy of theme was compiled with.</dd></dl>
<p> If input is coming from a file and the output was not set with the &#8211;<code>o</code> option, <code>writes the output to</code> file-sans-text.html (if ) <i>file</i> has a .text suffix, that will be stripped off and replaced with .html otherwise a .html will be appended to the end of the filename.) </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-d root </code></dt>
<dd> Set the <i>document root</i> to <i>root</i></dd>
<dt><code>-E</code></dt>
<dd> Normally theme will not expand &lt;?theme body?&gt; or &lt;?theme toc?&gt; in the &lt;head&gt; section, or &lt;?theme style?&gt; in the &lt;body&gt; section, but the &#8211;<code>E</code> option overrides this and allows expansions everywhere.</dd>
<dt><code>-f</code></dt>
<dd> Forcibly overwrite existing html files.</dd>
<dt><code>-o filename </code></dt>
<dd> Write the output to <i>filename</i></dd>
<dt><code>-p </code><i>path</i></dt>
<dd> Set the pagename to <i>path</i></dd>
<dt><code>-t </code><i>filename</i></dt>
<dd> Use <i>filename</i> as the template file.</dd></dl>
<h2>RETURN VALUES</h2>
<p> The utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-markdown/">markdown</a>(1), markdown(3), <a href="/docs/linux/man/7-markdown/">markdown</a>(7), mkd-extensions7.</p>
<h2>AUTHOR</h2>
<p> An David Parsons (<code>orc [at] pell.portland.or.us</code> ) </p>
