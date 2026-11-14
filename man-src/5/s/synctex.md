---
title: "synctex(5)"
name: "synctex"
section: "5"
letter: "s"
url: "/docs/linux/man/5-synctex/"
description: "synctex – Synchronize TeXnology help file"
---

<p>Independent</p>
<h2>Name</h2>
<p><code>synctex</code> &#8211; Synchronize TeXnology help file</p>
<h2>Description</h2>
<p>Synchronize TeXnology help file (synctexs) are text files that help input/output synchronization during document preparation with the TeX typesetting system.</p>
<h2>Basics</h2>
<p>The structure of this file should not be considered public, in the sense that no one should need to parse its contents, except the synctex command line utility, and the synctex_parser library which are both publicly available. Unless it is absolutely not avoidable, access to the contents of the synctex file should only be made through requests made to the synctex command line utility.</p>
<h2>Structure</h2>
<p>The element structure of a synctex file is a list of text line records as follows. `*&#8217; `+&#8217; and `?&#8217; have their usual EBNF meanings: `*&#8217; means zero or more, `+&#8217; means one or more, and `?&#8217; means zero or one (i.e., optional) </p>
<dl>
<dt><code>&lt;SyncTeX&gt; ::=</code></p>
<dd>(The whole contents in 4 sections)</p>
<dl>
<dt><code>&lt;Preamble&gt;</code></p>
<dd>
<dt><code>&lt;Content&gt;</code></p>
<dd>
<dt><code>&lt;Postamble&gt;</code></p>
<dd>
<dt><code>&lt;Post Scriptum&gt;</code></p>
<dd></dl>
</dl>
<p> Each section starts with the first occurrence of a sectioning line, and ends with the next section, if any. In the following definitions, we do not mention the section ending condition.</p>
<h2>The preamble</h2>
<dl>
<dt><code>&lt;Preamble&gt; ::=</code></p>
<dd>
<dl>
<dt><code>Qq </code>SyncTeX Version:</p>
<dd>&lt;Version Number&gt; &lt;EOL&gt;</p>
<dt><code>&lt;Input Line&gt;*</code></p>
<dd>
<dt><code>Qq </code>Magnification:</p>
<dd>&lt;TeX magnification&gt; &lt;EOL&gt;</p>
<dt><code>Qq </code>Unit:</p>
<dd>&lt;unit in scaled point&gt; &lt;EOL&gt;</p>
<dt><code>Qq </code>X Offset:</p>
<dd>&lt;horizontal offset in scaled point&gt; &lt;EOL&gt;</p>
<dt><code>Qq </code>Y Offset:</p>
<dd>&lt;vertical offset in scaled point&gt; &lt;EOL&gt;</dl>
<dt><code>&lt;Input Line&gt; ::= </code></p>
<dd>Qq Input: &lt;tag&gt; Qq : &lt;File Name&gt; &lt;EOL&gt;</dl>
<h2>The content</h2>
<dl>
<dt><code>&lt;Content&gt; ::=</code></p>
<dd>
<dl>
<dt><code>&lt;byte offset record&gt;</code></p>
<dd>
<dt><code>Qq </code>Content:</p>
<dd>&lt;EOL&gt;</p>
<dt><code>(&lt;Form(k)&gt;|&lt;Input Line&gt;)*</code></p>
<dd>
<dt><code>&lt;<a href="/docs/linux/man/1-sheet/">sheet</a>(1)&gt;</code></p>
<dd>
<dt><code>(&lt;Form(k)&gt;|&lt;Input Line&gt;)*</code></p>
<dd>
<dt><code>&lt;<a href="/docs/linux/man/2-sheet/">sheet</a>(2)&gt;</code></p>
<dd>
<dt><code>(&lt;Form(k)&gt;|&lt;Input Line&gt;)*</code></p>
<dd>
<dt><code>&#8230;</code></p>
<dd>
<dt><code>&lt;sheet(N)&gt;</code></p>
<dd>
<dt><code>(&lt;Form(k)&gt;|&lt;Input Line&gt;)*</code></p>
<dd></dl>
<dt><code>&lt;byte offset record&gt; ::=</code></p>
<dd>Qq ! &lt;byte offset&gt; &lt;end of record&gt; </p>
</dl>
<dl>
<dt><code>&lt;<a href="/docs/linux/man/n-sheet/">sheet</a>(n)&gt; ::=</code></p>
<dd>
<dl>
<dt><code>&lt;byte offset record&gt;</code></p>
<dd>
<dt><code>Qq </code>{</p>
<dd>&lt;the integer n&gt; &lt;end of record&gt;</p>
<dt><code>&lt;vbox section&gt;|&lt;hbox section&gt;</code></p>
<dd>
<dt><code>&lt;byte offset record&gt;</code></p>
<dd>
<dt><code>Qq </code>}</p>
<dd>&lt;the integer n&gt; &lt;end of record&gt;</dl>
<dt><code>&lt;Form&gt; ::=</code></p>
<dd>
<dl>
<dt><code>&lt;byte offset record&gt;</code></p>
<dd>
<dt><code>Qq </code>&lt;</p>
<dd>&lt;form tag&gt; &lt;end of record&gt;</p>
<dt><code>&lt;vbox section&gt;|&lt;hbox section&gt;</code></p>
<dd>
<dt><code>&lt;byte offset record&gt;</code></p>
<dd>
<dt><code>Qq </code>&gt;</p>
<dd>&lt;end of record&gt;</dl>
<dt><code>&lt;form tag&gt; ::= &lt;integer&gt;</code></p>
<dd></dl>
<p> Forms are available with pdfTeX. All the numbers are integers encoded using the decimal representation with &quot;C&quot; locale. The &lt;box content&gt; describes what is inside a box. It is either a vertical or horizontal box, with some records related to glue, kern or math nodes.</p>
<dl>
<dt><code>&lt;box content&gt; ::=</code></p>
<dd>
<dl>
<dt><code>&lt;vbox section&gt;|&lt;hbox section&gt;</code></p>
<dd>
<dt><code>|&lt;void vbox record&gt;|&lt;void hbox record&gt;</code></p>
<dd>
<dt><code>|&lt;current record&gt;|&lt;glue record&gt;|&lt;kern record&gt;</code></p>
<dd>
<dt><code>|&lt;math record&gt;|&lt;form ref record&gt;|&lt;Form&gt;</code></p>
<dd></dl>
<dt><code>&lt;vbox section&gt; ::=</code></p>
<dd>
<dl>
<dt><code>Qq </code>[</p>
<dd>&lt;link&gt; Qq : &lt;point&gt; Qq : &lt;size&gt; &lt;end of record&gt;</p>
<dt><code>&lt;box content&gt;*</code></p>
<dd>
<dt><code>Qq </code>]</p>
<dd>&lt;end of record&gt;</dl>
<dt><code>&lt;hbox section&gt; ::=</code></p>
<dd>
<dl>
<dt><code>(</code></p>
<dd>&lt;link&gt; Qq : &lt;point&gt; Qq : &lt;size&gt; &lt;end of record&gt;</p>
<dt><code>&lt;box content&gt;*</code></p>
<dd>
<dt><code>Qq </code>)</p>
<dd>&lt;end of record&gt;</dl>
</dl>
<p> Void boxes:</p>
<dl>
<dt><code>&lt;void vbox record&gt; ::=</code></p>
<dd>Qq v &lt;link&gt; Qq : &lt;point&gt; Qq : &lt;size&gt; &lt;end of record&gt;</p>
<dt><code>&lt;void hbox record&gt; ::=</code></p>
<dd>Qq h &lt;link&gt; Qq : &lt;point&gt; Qq : &lt;size&gt; &lt;end of record&gt;</p>
<dt><code>&lt;link&gt; ::= &lt;tag&gt;</code></p>
<dd>Qq , &lt;line&gt;( Qq , &lt;column&gt;)?</p>
<dt><code>&lt;point&gt; ::= &lt;full point&gt;|&lt;compressed point&gt;</code></p>
<dd>
<dt><code>&lt;full point&gt; ::=</code></p>
<dd>&lt;integer&gt; Qq , &lt;integer&gt;</p>
<dt><code>&lt;compressed point&gt; ::=</code></p>
<dd>&lt;integer&gt; Qq ,=</p>
<dt><code>&lt;line&gt; ::= &lt;integer&gt;</code></p>
<dd>
<dt><code>&lt;column&gt; ::= &lt;integer&gt;</code></p>
<dd>
<dt><code>&lt;size&gt; ::= &lt;Width&gt;</code></p>
<dd>Qq , &lt;Height&gt; Qq , &lt;Depth&gt;</p>
<dt><code>&lt;Width&gt; ::= &lt;integer&gt;</code></p>
<dd>
<dt><code>&lt;Height&gt; ::= &lt;integer&gt;</code></p>
<dd>
<dt><code>&lt;Depth&gt; ::= &lt;integer&gt;</code></p>
<dd></dl>
<p> The forthcoming records are basic one liners.</p>
<dl>
<dt><code>&lt;current record&gt; ::=</code></p>
<dd>Qq x &lt;link&gt; Qq : &lt;point&gt; &lt;end of record&gt;</p>
<dt><code>&lt;kern record&gt; ::=</code></p>
<dd>Qq k &lt;link&gt; Qq : &lt;point&gt; Qq : &lt;Width&gt; &lt;end of record&gt;</p>
<dt><code>&lt;glue record&gt; ::=</code></p>
<dd>Qq g &lt;link&gt; Qq : &lt;point&gt; &lt;end of record&gt;</p>
<dt><code>&lt;math record&gt; ::=</code></p>
<dd>Qq $ &lt;link&gt; Qq : &lt;point&gt; &lt;end of record&gt;</p>
<dt><code>&lt;form ref record&gt; ::=</code></p>
<dd>Qq f &lt;form tag&gt; Qq : &lt;point&gt; &lt;end of record&gt;</dl>
<h2>The postamble</h2>
<p>The postamble closes the file If there is no postamble, it means that the typesetting process did not end correctly.</p>
<dl>
<dt><code>&lt;Postamble&gt;::=</code></p>
<dd>
<dl>
<dt><code>&lt;byte offset record&gt;</code></p>
<dd>
<dt><code>Qq </code>Count:</p>
<dd>&lt;Number of records&gt; &lt;EOL&gt;</dl>
</dl>
<h2>The post scriptum</h2>
<p>The post scriptum contains material possibly added by 3rd parties. It allows to append some transformation (shift and magnify). Typically, one applies a dvi to pdf filter with offset options and magnification, then he appends the same options to the synctex file, for example </p>
<blockquote>
<pre>synctex update -o foo.pdf -m 0.486 -x 9472573sp -y 13.3dd source.dvi</pre>
</blockquote>
<dl>
<dt><code>&lt;Post Scriptum&gt;::=</code></p>
<dd>
<dl>
<dt><code>&lt;byte offset record&gt;</code></p>
<dd>
<dt><code>Qq </code>Post Scriptum:</p>
<dd>&lt;EOL&gt;</p>
<dt><code>Qq </code>Magnification:</p>
<dd>&lt;number&gt; &lt;EOL&gt; (Set additional magnification)</p>
<dt><code>Qq </code>X Offset:</p>
<dd>&lt;dimension&gt; &lt;EOL&gt; (Set horizontal offset)</p>
<dt><code>Qq </code>Y Offset:</p>
<dd>&lt;dimension&gt; &lt;EOL&gt; (Set vertical offset)</dl>
</dl>
<p> This second information will override the offset and magnification previously available in the preamble section. All the numbers are encoded using the decimal representation with &quot;C&quot; locale.</p>
<h2>Usage</h2>
<p>The &lt;current record&gt; is used to compute the visible size of hbox&#8217;s. The byte offset is an implicit anchor to navigate the synctex file from sheet to sheet. The second coordinate of a compressed point has been replaced by a Qq = character which means that it is the second coordinate of the last full point available above.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-synctex/">synctex</a>(1) <a href="/docs/linux/man/1-tex/">tex</a>(1)</p>
<h2>Author</h2>
<p>The Synchronize TeXnology is essentially due to Jerome Laurens, with useful suggestions by some well known actors of the TeX world.</p>
<h2>HISTORY This document has been updated on Sat Apr 22 09:57:20 UTC 2017 to include \pdfxform support.</h2>
