---
title: "markdown(1)"
name: "markdown"
section: "1"
letter: "m"
url: "/docs/linux/man/1-markdown/"
description: "markdown – text to html conversion tool"
---

<h2 class="name">NAME</h2>
<p> <code>markdown</code> &#8211; text to html conversion tool </p>
<h2>SYNOPSIS</h2>
<p> [-<code>d</code> ] [-<code>T</code> ] [-<code>V</code> ] [-<code>b </code><i>url-base</i> ] [-<code>C </code><i>prefix</i> ] [-<code>F bitmap </code> ] [-<code>f </code><i>flags</i> ] [-<code>n</code> ] [-<code>o file </code> ] [-<code>S</code> ] [-<code>s text </code> ] [-<code>t text </code> ] [textfile ]</p>
<h2>DESCRIPTION</h2>
<p> The utility reads the <a href="/docs/linux/man/7-markdown/">markdown</a>(7)Ns-formatted textfile (or stdin if not specified,) compiles it, and writes the html output to stdout. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-b </code><i>url-base</i></p>
<dd> Links in source beginning with / will be prefixed with <i>url-base</i> in the output.</p>
<dt><code>-C</code></p>
<dd> When processing markdown extra-style footnotes, use the given prefix instead of the default of <i>fn</i></p>
<dt><code>-d</code></p>
<dd> Instead of writing the html file, dump a parse tree to stdout.</p>
<dt><code>-f </code><i>flags</i></p>
<dd> Set or clear various translation flags. The flags are in a comma-delimited list, with an optional <i>+</i> (enable), <i>&#8211;</i> (disable), or <i>no</i> (disable) lprefix on each flag.</p>
<dl>
<dt><i>links</i></p>
<dd> Allow links.</p>
<dt><i>image</i></p>
<dd> Allow images.</p>
<dt><i>smarty</i></p>
<dd> Enable smartypants.</p>
<dt><i>pants</i></p>
<dd> Enable smartypants.</p>
<dt><i>html</i></p>
<dd> Allow raw html.</p>
<dt><i>strict</i></p>
<dd> Disable superscript, strikethrough &amp; relaxed emphasis.</p>
<dt><i>ext</i></p>
<dd> Enable pseudo-protocols.</p>
<dt><i>cdata</i></p>
<dd> Generate code for xml <i>![CDATA[&#8230;]]</i></p>
<dt><i>superscript</i></p>
<dd> Enable superscript processing.</p>
<dt><i>emphasis</i></p>
<dd> Emphasis happens <i>everywhere</i></p>
<dt><i>tables</i></p>
<dd> Don&#8217;t process PHP Markdown Extra tables.</p>
<dt><i>del</i></p>
<dd> Enable <i>~~strikethrough~~</i></p>
<dt><i>strikethrough</i></p>
<dd> Enable <i>~~strikethrough~~</i></p>
<dt><i>toc</i></p>
<dd> Enable table-of-contents processing.</p>
<dt><i>1.0</i></p>
<dd> Compatibility with MarkdownTest_1.0</p>
<dt><i>autolink</i></p>
<dd> Make <a rel="nofollow" href="http://foo.com">http://foo.com</a> a link even without <i>&lt;&gt;</i></p>
<dt><i>safelink</i></p>
<dd> Paranoid check for link protocol.</p>
<dt><i>header</i></p>
<dd> Process pandoc-style header blocks.</p>
<dt><i>tabstop</i></p>
<dd> Expand tabs to 4 spaces.</p>
<dt><i>divquote</i></p>
<dd> Allow &gt;%class% blocks.</p>
<dt><i>alphalist</i></p>
<dd> Allow alphabetic lists.</p>
<dt><i>definitionlist</i></p>
<dd> Allow definition lists.</p>
<dt><i>footnote</i></p>
<dd> Allow markdown extra-style footnotes.</p>
<dt><i>styles</i></p>
<dd> Extract &lt;style&gt; blocks from the output.</dl>
<p> As an example, the option &#8211;<code>f </code><i>nolinks,smarty</i> tells to not allow &lt;a tags, and to do smarty pants processing.</p>
<dt><code>-F </code><i>bitmap</i></p>
<dd> Set translation flags. <i>Bitmap</i> is a bit map of the various configuration options described in <a href="/docs/linux/man/3-markdown/">markdown</a>(3) (the flag values are defined in mkdio.h</p>
<dt><code>-n</code></p>
<dd> Don&#8217;t write generated html.</p>
<dt><code>-o file </code></p>
<dd> Write the generated html to file</p>
<dt><code>-S</code></p>
<dd> output &lt;style&gt; blocks.</p>
<dt><code>-V</code></p>
<dd> Show the version# and compile-time configuration data. </p>
<p> If the version includes the string <i>DEBUG</i> was configured with memory allocation debugging. </p>
<p> If the version includes the string <i>TAB</i> was configured to use the specified tabstop.</p>
<dt><code>-VV</code></p>
<dd> Show the version#, the compile-time configuration, and the run-time configuration.</p>
<dt><code>-t </code><i>text</i></p>
<dd> Use mkd_text3 to format <i>text</i> instead of processing stdin with the <a href="/docs/linux/man/3-markdown/">markdown</a>(3) function.</p>
<dt><code>-T</code></p>
<dd> If run with the table-of-content flag on, dump the table of contents before the formatted text.</p>
<dt><code>-s </code><i>text</i></p>
<dd> Use the <a href="/docs/linux/man/3-markdown/">markdown</a>(3) function to format <i>text</i></dl>
<h2>RETURN VALUES</h2>
<p> The utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-markdown/">markdown</a>(3), <a href="/docs/linux/man/7-markdown/">markdown</a>(7), mkd-extensions7.</p>
<h2>AUTHOR</h2>
<p> An David Parsons (<code>orc [at] pell.portland.or.us</code> ) </p>
<h2>Index</h2>
