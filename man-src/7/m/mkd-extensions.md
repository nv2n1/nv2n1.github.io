---
title: "mkd-extensions(7)"
name: "mkd-extensions"
section: "7"
letter: "m"
url: "/docs/linux/man/7-mkd-extensions/"
description: "mkd-extensions – Extensions to the Markdown text formatting syntax"
---

<p><code>mkd-extensions</code> &#8211; Extensions to the Markdown text formatting syntax</p>
<h2>Description</h2>
<p>This version of markdown has been extended in a few ways by extending existing markup, creating new markup from scratch, and borrowing markup from other markup languages.</p>
<h3>Image dimensions</h3>
<p>Markdown embedded images have been extended to allow specifying the dimensions of the image by adding a new argument <i>=/height/x/width/</i> to the link description. </p>
<p> The new image syntax is </p>
<pre> ![alt text](image =/height/x/width/ &quot;title&quot;)</pre>
<h3>pseudo-protocols</h3>
<p>Five pseudo-protocols have been added to links</p>
<dl>
<dt><i>id:</i></p>
<dd>The <i>alt text</i> is marked up and written to the output, wrapped with <i>&lt;a id=id&gt;</i> and <i>&lt;/a&gt;</i></p>
<dt><i>class:</i></p>
<dd>The <i>alt text</i> is marked up and written to the output, wrapped with <i>&lt;span class=class&gt;</i> and <i>&lt;/span&gt;</i></p>
<dt><i>raw:</i></p>
<dd>The <i>title</i> is written <i>&#8212; with no further processing &#8212;</i> to the output. The <i>alt text</i> is discarded.</p>
<dt><i>abbr:</i></p>
<dd>The <i>alt text</i> is marked up and written to the output, wrapped with <i>&lt;abbr title=abbr&gt;</i> and <i>&lt;/abbr&gt;</i></p>
<dt><i>lang:</i></p>
<dd>The <i>alt text</i> s marked up and written to the output, wrapped with <i>&lt;span lang=lang&gt;</i> and <i>&lt;/span&gt;</i></dl>
<h3>Pandoc headers</h3>
<p>The markdown source document can have a 3-line Pandoc header in the format of </p>
<pre> % title
 % author(s)
 % date</pre>
<p>which will be made available to the Fn mkd_doc_title , Fn mkd_doc_author , and Fn mkd_doc_date functions.</p>
<h3>Definition lists</h3>
<p>A definition list item is defined as </p>
<pre>=tag=
 description</pre>
<p>(that is a <i>=</i> followed by text, another <i>=</i> a newline, 4 spaces of intent, and then more text.) </p>
<p> Alternatively, definition list items are defined as </p>
<pre>tag
: description</pre>
<p>(This is the format that <i>PHP Markdown Extra</i> uses.)</p>
<h3>embedded stylesheets</h3>
<p>Stylesheets may be defined and modified in a <i>&lt;style&gt;</i> block. A style block is parsed like any other block level html; <i>&lt;style&gt;</i> starting on column 1, raw html (or, in this case, css) following it, and either ending with a <i>&lt;/style&gt;</i> at the end of the line or a <i>&lt;/style&gt;</i> at the beginning of a subsequent line. </p>
<p> Be warned that style blocks work like footnote links &#8212; no matter where you define them they are valid for the entire document.</p>
<h3>relaxed emphasis</h3>
<p>The rules for emphasis are changed so that a single <i>_</i> will <i>not</i> count as a emphasis character if it&#8217;s in the middle of a word. This is primarily for documenting code, if you don&#8217;t wish to have to backquote all code references.</p>
<h3>alpha lists</h3>
<p>Alphabetic lists (like regular numeric lists, but with alphabetic items) are supported. So: </p>
<pre> a. this
 b. is
 c. an alphabetic
 d. list</pre>
<p>will produce: </p>
<pre> &lt;ol type=a&gt;
 &lt;li&gt;this&lt;/li&gt;
 &lt;li&gt;is&lt;/li&gt;
 &lt;li&gt;an alphabetic&lt;/li&gt;
 &lt;li&gt;list&lt;/li&gt;
 &lt;/ol&gt;</pre>
<h3>tables</h3>
<p><i>PHP Markdown Extra</i> tables are supported; input of the form </p>
<pre> header|header
 ------|------
 text | text</pre>
<p>will produce: </p>
<pre> &lt;table&gt;
 &lt;thead&gt;
 &lt;tr&gt;
 &lt;th&gt;header&lt;/th&gt;
 &lt;th&gt;header&lt;/th&gt;
 &lt;/tr&gt;
 &lt;/thead&gt;
 &lt;tbody&gt;
 &lt;tr&gt;
 &lt;td&gt;text&lt;/td&gt;
 &lt;td&gt;text&lt;/td&gt;
 &lt;/tr&gt;
 &lt;/tbody&gt;
 &lt;/table&gt;</pre>
<p>The dashed line can also contain <i>:</i> characters for formatting; if a <i>:</i> is at the start of a column, it tells <code>discount</code> to align the cell contents to the left; if it&#8217;s at the end, it aligns right, and if there&#8217;s one at the start and at the end, it centers.</p>
<h3>strikethrough</h3>
<p>A strikethrough syntax is supported in much the same way that <i>`</i> is used to define a section of code. If you enclose text with two or more tildes, such as <i>~~erased text~~</i> it will be written as <i>&lt;del&gt;erased text&lt;/del&gt;</i> Like code sections, you may use as many <i>~</i> as you want, but there must be as many starting tildes as closing tildes.</p>
<h3>markdown extra-style footnotes</h3>
<p><i>PHP Markdown Extra</i> footnotes are supported. If a footnote link begins with a <i>^</i> the first use of that footnote will generate a link down to the bottom of the rendered document, which will contain a numbered footnote with a link back to where the footnote was called.</p>
<h2>Author</h2>
<p>David Parsons <i><a rel="nofollow" href="http://www.pell.portland.or.us/~orc/">http://www.pell.portland.or.us/~orc/</a></i></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-markdown/">markdown</a>(1), <a href="/docs/linux/man/3-markdown/">markdown</a>(3), mkd-callbacks3, mkd-functions3, mkd-line3. <i><a rel="nofollow" href="http://daringfireball.net/projects/markdown">http://daringfireball.net/projects/markdown</a></i> <i><a rel="nofollow" href="http://michelf.com/projects/php-markdown">http://michelf.com/projects/php-markdown</a></i> </p>
