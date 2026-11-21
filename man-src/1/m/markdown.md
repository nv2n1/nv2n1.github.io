---

title: "markdown(1)"
name: "markdown"
section: "1"
letter: "m"
url: "/docs/linux/man/1-markdown/"
description: "markdown – text to html conversion tool"
---

<p> <code>markdown</code> &#8211; text to html conversion tool </p>
<p> [-<code>d</code> ] [-<code>T</code> ] [-<code>V</code> ] [-<code>b </code><i>url-base</i> ] [-<code>C </code><i>prefix</i> ] [-<code>F bitmap </code> ] [-<code>f </code><i>flags</i> ] [-<code>n</code> ] [-<code>o file </code> ] [-<code>S</code> ] [-<code>s text </code> ] [-<code>t text </code> ] [textfile ]</p>
<p> The utility reads the <a href="/docs/linux/man/7-markdown/">markdown</a>(7)Ns-formatted textfile (or stdin if not specified,) compiles it, and writes the html output to stdout. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-b </code><i>url-base</i></dt>
<dd> Links in source beginning with / will be prefixed with <i>url-base</i> in the output.</dd>
<dt><code>-C</code></dt>
<dd> When processing markdown extra-style footnotes, use the given prefix instead of the default of <i>fn</i></dd>
<dt><code>-d</code></dt>
<dd> Instead of writing the html file, dump a parse tree to stdout.</dd>
<dt><code>-f </code><i>flags</i></dt>
<dd> Set or clear various translation flags. The flags are in a comma-delimited list, with an optional <i>+</i> (enable), <i>&#8211;</i> (disable), or <i>no</i> (disable) lprefix on each flag.</dd>
<dl>
<dt><i>links</i></dt>
<dd> Allow links.</dd>
<dt><i>image</i></dt>
<dd> Allow images.</dd>
<dt><i>smarty</i></dt>
<dd> Enable smartypants.</dd>
<dt><i>pants</i></dt>
<dd> Enable smartypants.</dd>
<dt><i>html</i></dt>
<dd> Allow raw html.</dd>
<dt><i>strict</i></dt>
<dd> Disable superscript, strikethrough &amp; relaxed emphasis.</dd>
<dt><i>ext</i></dt>
<dd> Enable pseudo-protocols.</dd>
<dt><i>cdata</i></dt>
<dd> Generate code for xml <i>![CDATA[&#8230;]]</i></dd>
<dt><i>superscript</i></dt>
<dd> Enable superscript processing.</dd>
<dt><i>emphasis</i></dt>
<dd> Emphasis happens <i>everywhere</i></dd>
<dt><i>tables</i></dt>
<dd> Don&#8217;t process PHP Markdown Extra tables.</dd>
<dt><i>del</i></dt>
<dd> Enable <i>~~strikethrough~~</i></dd>
<dt><i>strikethrough</i></dt>
<dd> Enable <i>~~strikethrough~~</i></dd>
<dt><i>toc</i></dt>
<dd> Enable table-of-contents processing.</dd>
<dt><i>1.0</i></dt>
<dd> Compatibility with MarkdownTest_1.0</dd>
<dt><i>autolink</i></dt>
<dd> Make <a rel="nofollow" href="http://foo.com">http://foo.com</a> a link even without <i>&lt;&gt;</i></dd>
<dt><i>safelink</i></dt>
<dd> Paranoid check for link protocol.</dd>
<dt><i>header</i></dt>
<dd> Process pandoc-style header blocks.</dd>
<dt><i>tabstop</i></dt>
<dd> Expand tabs to 4 spaces.</dd>
<dt><i>divquote</i></dt>
<dd> Allow &gt;%class% blocks.</dd>
<dt><i>alphalist</i></dt>
<dd> Allow alphabetic lists.</dd>
<dt><i>definitionlist</i></dt>
<dd> Allow definition lists.</dd>
<dt><i>footnote</i></dt>
<dd> Allow markdown extra-style footnotes.</dd>
<dt><i>styles</i></dt>
<dd> Extract &lt;style&gt; blocks from the output.</dd></dl>
<p> As an example, the option &#8211;<code>f </code><i>nolinks,smarty</i> tells to not allow &lt;a tags, and to do smarty pants processing.</p>
<dt><code>-F </code><i>bitmap</i></dt>
<dd> Set translation flags. <i>Bitmap</i> is a bit map of the various configuration options described in markdown(3) (the flag values are defined in mkdio.h</dd>
<dt><code>-n</code></dt>
<dd> Don&#8217;t write generated html.</dd>
<dt><code>-o file </code></dt>
<dd> Write the generated html to file</dd>
<dt><code>-S</code></dt>
<dd> output &lt;style&gt; blocks.</dd>
<dt><code>-V</code></dt>
<dd> Show the version# and compile-time configuration data. </dd>
<p> If the version includes the string <i>DEBUG</i> was configured with memory allocation debugging. </p>
<p> If the version includes the string <i>TAB</i> was configured to use the specified tabstop.</p>
<dt><code>-VV</code></dt>
<dd> Show the version#, the compile-time configuration, and the run-time configuration.</dd>
<dt><code>-t </code><i>text</i></dt>
<dd> Use mkd_text3 to format <i>text</i> instead of processing stdin with the markdown(3) function.</dd>
<dt><code>-T</code></dt>
<dd> If run with the table-of-content flag on, dump the table of contents before the formatted text.</dd>
<dt><code>-s </code><i>text</i></dt>
<dd> Use the markdown(3) function to format <i>text</i></dd></dl>
<h2>RETURN VALUES</h2>
<p> The utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>SEE ALSO</h2>
<p> markdown(3), <a href="/docs/linux/man/7-markdown/">markdown</a>(7), mkd-extensions7.</p>
<h2>AUTHOR</h2>
<p> An David Parsons (<code>orc [at] pell.portland.or.us</code> ) </p>
