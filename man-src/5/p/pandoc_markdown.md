---
title: "pandoc_markdown(5)"
name: "pandoc_markdown"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pandoc_markdown/"
description: "pandoc_markdown – markdown syntax for pandoc(1)"
---

<p>pandoc_markdown &#8211; markdown syntax for <a href="/docs/linux/man/1-pandoc/">pandoc</a>(1)</p>
<h2>Description</h2>
<p>Pandoc understands an extended and slightly revised version of John Gruber&#8217;s markdown syntax. This document explains the syntax, noting differences from standard markdown. Except where noted, these differences can be suppressed by using the markdown_strict format instead of markdown. An extensions can be enabled by adding +EXTENSION to the format name and disabled by adding -EXTENSION. For example, markdown_strict+footnotes is strict markdown with footnotes enabled, while markdown-footnotes-pipe_tables is pandoc&#8217;s markdown without footnotes or pipe tables.</p>
<h2>Philosophy</h2>
<p>Markdown is designed to be easy to write, and, even more importantly, easy to read:</p>
<dl>
<dd>A Markdown-formatted document should be publishable as-is, as plain text, without looking like it&#8217;s been marked up with tags or formatting instructions. &#8212; John Gruber</dl>
<p> This principle has guided pandoc&#8217;s decisions in finding syntax for tables, footnotes, and other extensions. </p>
<p> There is, however, one respect in which pandoc&#8217;s aims are different from the original aims of markdown. Whereas markdown was originally designed with HTML generation in mind, pandoc is designed for multiple output formats. Thus, while pandoc allows the embedding of raw HTML, it discourages it, and provides other, non-HTMLish ways of representing important document elements like definition lists, tables, mathematics, and footnotes.</p>
<h2>Paragraphs</h2>
<p>A paragraph is one or more lines of text followed by one or more blank line. Newlines are treated as spaces, so you can reflow your paragraphs as you like. If you need a hard line break, put two or more spaces at the end of a line. </p>
<p> Extension: escaped_line_breaks </p>
<p> A backslash followed by a newline is also a hard line break. Note: in multiline and grid table cells, this is the only way to create a hard line break, since trailing spaces in the cells are ignored.</p>
<h2>Headers</h2>
<p>There are two kinds of headers, Setext and atx.</p>
<h3>Setext-style headers</h3>
<p>A setext-style header is a line of text &quot;underlined&quot; with a row of = signs (for a level one header) or &#8211; signs (for a level two header):</p>
<dl>
<dd>
<pre>A level-one header
==================
A level-two header
------------------</pre>
</dl>
<p> The header text can contain inline formatting, such as emphasis (see Inline formatting, below).</p>
<h3>Atx-style headers</h3>
<p>An Atx-style header consists of one to six # signs and a line of text, optionally followed by any number of # signs. The number of # signs at the beginning of the line is the header level:</p>
<dl>
<dd>
<pre>##&nbsp;<wbr>A level-two header
###&nbsp;<wbr>A level-three header&nbsp;<wbr>###</pre>
</dl>
<p> As with setext-style headers, the header text can contain formatting:</p>
<dl>
<dd>
<pre>#&nbsp;<wbr>A level-one header with a&nbsp;<wbr>[link](/url)&nbsp;<wbr>and&nbsp;<wbr>*emphasis*</pre>
</dl>
<p> Extension: blank_before_header </p>
<p> Standard markdown syntax does not require a blank line before a header. Pandoc does require this (except, of course, at the beginning of the document). The reason for the requirement is that it is all too easy for a # to end up at the beginning of a line by accident (perhaps through line wrapping). Consider, for example:</p>
<dl>
<dd>
<pre>I like several of their flavors of ice cream:
#22, for example, and&nbsp;<wbr>#5.</pre>
</dl>
<h3>Header identifiers in HTML, LaTeX, and ConTeXt</h3>
<p>Extension: header_attributes </p>
<p> Headers can be assigned attributes using this syntax at the end of the line containing the header text:</p>
<dl>
<dd>
<pre>{#identifier .class .class key=value key=value}</pre>
</dl>
<p> Although this syntax allows assignment of classes and key/value attributes, only identifiers currently have any affect in the writers (and only in some writers: HTML, LaTeX, ConTeXt, Textile, AsciiDoc). Thus, for example, the following headers will all be assigned the identifier foo:</p>
<dl>
<dd>
<pre>#&nbsp;<wbr>My header&nbsp;<wbr>{#foo}
##&nbsp;<wbr>My header&nbsp;<wbr>##&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>{#foo}
My other header&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>{#foo}
---------------</pre>
</dl>
<p> (This syntax is compatible with PHP Markdown Extra.) </p>
<p> Headers with the class unnumbered will not be numbered, even if &#8211;number-sections is specified. A single hyphen (-) in an attribute context is equivalent to .unnumbered, and preferable in non-English documents. So,</p>
<dl>
<dd>
<pre>#&nbsp;<wbr>My header&nbsp;<wbr>{-}</pre>
</dl>
<p> is just the same as</p>
<dl>
<dd>
<pre>#&nbsp;<wbr>My header&nbsp;<wbr>{.unnumbered}</pre>
</dl>
<p> Extension: auto_identifiers </p>
<p> A header without an explicitly specified identifier will be automatically assigned a unique identifier based on the header text. To derive the identifier from the header text,</p>
<dl>
<dt>&bull;</p>
<dd>Remove all formatting, links, etc.</p>
<dt>&bull;</p>
<dd>Remove all footnotes.</p>
<dt>&bull;</p>
<dd>Remove all punctuation, except underscores, hyphens, and periods.</p>
<dt>&bull;</p>
<dd>Replace all spaces and newlines with hyphens.</p>
<dt>&bull;</p>
<dd>Convert all alphabetic characters to lowercase.</p>
<dt>&bull;</p>
<dd>Remove everything up to the first letter (identifiers may not begin with a number or punctuation mark).</p>
<dt>&bull;</p>
<dd>If nothing is left after this, use the identifier section.</dl>
<p> Thus, for example, </p>
<table>
<tr VALIGN=top>
<td> Header </td>
<td> Identifier
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Header identifiers in HTML </td>
<td> header-identifiers-in-html
</td>
</tr>
<tr VALIGN=top>
<td> Dogs?&#8211;in my house? </td>
<td> dogs&#8211;in-my-house
</td>
</tr>
<tr VALIGN=top>
<td> HTML, S5, or RTF? </td>
<td> html-s5-or-rtf
</td>
</tr>
<tr VALIGN=top>
<td> 3. Applications </td>
<td> applications
</td>
</tr>
<tr VALIGN=top>
<td> 33 </td>
<td> section
</td>
</tr>
</table>
<p> These rules should, in most cases, allow one to determine the identifier from the header text. The exception is when several headers have the same text; in this case, the first will get an identifier as described above; the second will get the same identifier with -1 appended; the third with -2; and so on. </p>
<p> These identifiers are used to provide link targets in the table of contents generated by the &#8211;toc|&#8211;table-of-contents option. They also make it easy to provide links from one section of a document to another. A link to this section, for example, might look like this:</p>
<dl>
<dd>
<pre>See the section on
[header identifiers](#header-identifiers-in-html-latex-and-context).</pre>
</dl>
<p> Note, however, that this method of providing links to sections works only in HTML, LaTeX, and ConTeXt formats. </p>
<p> If the &#8211;section-divs option is specified, then each section will be wrapped in a div (or a section, if &#8211;html5 was specified), and the identifier will be attached to the enclosing &lt;div&gt; (or &lt;section&gt;) tag rather than the header itself. This allows entire sections to be manipulated using javascript or treated differently in CSS. </p>
<p> Extension: implicit_header_references </p>
<p> Pandoc behaves as if reference links have been defined for each header. So, instead of</p>
<dl>
<dd>
<pre>[header identifiers](#header-identifiers-in-html)</pre>
</dl>
<p> you can simply write</p>
<dl>
<dd>
<pre>[header identifiers]</pre>
</dl>
<p> or</p>
<dl>
<dd>
<pre>[header identifiers][]</pre>
</dl>
<p> or</p>
<dl>
<dd>
<pre>[the section on header identifiers][header identifiers]</pre>
</dl>
<p> If there are multiple headers with identical text, the corresponding reference will link to the first one only, and you will need to use explicit links to link to the others, as described above. </p>
<p> Unlike regular reference links, these references are case-sensitive. </p>
<p> Note: if you have defined an explicit identifier for a header, then implicit references to it will not work.</p>
<h2>Block Quotations</h2>
<p>Markdown uses email conventions for quoting blocks of text. A block quotation is one or more paragraphs or other block elements (such as lists or headers), with each line preceded by a &gt; character and a space. (The &gt; need not start at the left margin, but it should not be indented more than three spaces.)</p>
<dl>
<dd>
<pre>&gt;&nbsp;<wbr>This is a block quote. This
&gt;&nbsp;<wbr>paragraph has two lines.
&gt;
&gt;&nbsp;<wbr>1. This is a list inside a block quote.
&gt;&nbsp;<wbr>2. Second item.</pre>
</dl>
<p> A &quot;lazy&quot; form, which requires the &gt; character only on the first line of each block, is also allowed:</p>
<dl>
<dd>
<pre>&gt;&nbsp;<wbr>This is a block quote. This
paragraph has two lines.
&gt;&nbsp;<wbr>1. This is a list inside a block quote.
2. Second item.</pre>
</dl>
<p> Among the block elements that can be contained in a block quote are other block quotes. That is, block quotes can be nested:</p>
<dl>
<dd>
<pre>&gt;&nbsp;<wbr>This is a block quote.
&gt;
&gt;&nbsp;<wbr>&gt;&nbsp;<wbr>A block quote within a block quote.</pre>
</dl>
<p> Extension: blank_before_blockquote </p>
<p> Standard markdown syntax does not require a blank line before a block quote. Pandoc does require this (except, of course, at the beginning of the document). The reason for the requirement is that it is all too easy for a &gt; to end up at the beginning of a line by accident (perhaps through line wrapping). So, unless the markdown_strict format is used, the following does not produce a nested block quote in pandoc:</p>
<dl>
<dd>
<pre>&gt;&nbsp;<wbr>This is a block quote.
&gt;&gt;&nbsp;<wbr>Nested.</pre>
</dl>
<h2>Verbatim (Code) Blocks</h2>
<h3>Indented code blocks</h3>
<p>A block of text indented four spaces (or one tab) is treated as verbatim text: that is, special characters do not trigger special formatting, and all spaces and line breaks are preserved. For example,</p>
<dl>
<dd>
<pre>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>if&nbsp;<wbr>(a&nbsp;<wbr>&gt;&nbsp;<wbr>3)&nbsp;<wbr>{
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>moveShip(5&nbsp;<wbr>*&nbsp;<wbr>gravity, DOWN);
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>}</pre>
</dl>
<p> The initial (four space or one tab) indentation is not considered part of the verbatim text, and is removed in the output. </p>
<p> Note: blank lines in the verbatim text need not begin with four spaces.</p>
<h3>Fenced code blocks</h3>
<p>Extension: fenced_code_blocks </p>
<p> In addition to standard indented code blocks, Pandoc supports fenced code blocks. These begin with a row of three or more tildes (~) or backticks (`) and end with a row of tildes or backticks that must be at least as long as the starting row. Everything between these lines is treated as code. No indentation is necessary:</p>
<dl>
<dd>
<pre>~~~~~~~
if&nbsp;<wbr>(a&nbsp;<wbr>&gt;&nbsp;<wbr>3)&nbsp;<wbr>{
&nbsp;<wbr>&nbsp;<wbr>moveShip(5&nbsp;<wbr>*&nbsp;<wbr>gravity, DOWN);
}
~~~~~~~</pre>
</dl>
<p> Like regular code blocks, fenced code blocks must be separated from surrounding text by blank lines. </p>
<p> If the code itself contains a row of tildes or backticks, just use a longer row of tildes or backticks at the start and end:</p>
<dl>
<dd>
<pre>~~~~~~~~~~~~~~~~
~~~~~~~~~~
code including tildes
~~~~~~~~~~
~~~~~~~~~~~~~~~~</pre>
</dl>
<p> Optionally, you may attach attributes to the code block using this syntax:</p>
<dl>
<dd>
<pre>~~~~&nbsp;<wbr>{#mycode .haskell .numberLines startFrom=&quot;100&quot;}
qsort&nbsp;<wbr>[]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>[]
qsort&nbsp;<wbr>(x:xs)&nbsp;<wbr>=&nbsp;<wbr>qsort&nbsp;<wbr>(filter&nbsp;<wbr>(&lt;&nbsp;<wbr>x)&nbsp;<wbr>xs)&nbsp;<wbr>++&nbsp;<wbr>[x]&nbsp;<wbr>++
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>qsort&nbsp;<wbr>(filter&nbsp;<wbr>(&gt;=&nbsp;<wbr>x)&nbsp;<wbr>xs)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</pre>
</dl>
<p> Here mycode is an identifier, haskell and numberLines are classes, and startFrom is an attribute with value 100. Some output formats can use this information to do syntax highlighting. Currently, the only output formats that uses this information are HTML and LaTeX. If highlighting is supported for your output format and language, then the code block above will appear highlighted, with numbered lines. (To see which languages are supported, do pandoc &#8211;version.) Otherwise, the code block above will appear as follows:</p>
<dl>
<dd>
<pre>&lt;pre id=&quot;mycode&quot;&nbsp;<wbr>class=&quot;haskell numberLines&quot;&nbsp;<wbr>startFrom=&quot;100&quot;&gt;
&nbsp;<wbr>&nbsp;<wbr>&lt;code&gt;
&nbsp;<wbr>&nbsp;<wbr>...
&nbsp;<wbr>&nbsp;<wbr>&lt;/code&gt;
&lt;/pre&gt;</pre>
</dl>
<p> A shortcut form can also be used for specifying the language of the code block:</p>
<dl>
<dd>
<pre>```haskell
qsort&nbsp;<wbr>[]&nbsp;<wbr>=&nbsp;<wbr>[]
```</pre>
</dl>
<p> This is equivalent to:</p>
<dl>
<dd>
<pre>```&nbsp;<wbr>{.haskell}
qsort&nbsp;<wbr>[]&nbsp;<wbr>=&nbsp;<wbr>[]
```</pre>
</dl>
<p> To prevent all highlighting, use the &#8211;no-highlight flag. To set the highlighting style, use &#8211;highlight-style.</p>
<h2>Line Blocks</h2>
<p>Extension: line_blocks </p>
<p> A line block is a sequence of lines beginning with a vertical bar (|) followed by a space. The division into lines will be preserved in the output, as will any leading spaces; otherwise, the lines will be formatted as markdown. This is useful for verse and addresses:</p>
<dl>
<dd>
<pre>| The limerick packs laughs anatomical
| In space that is quite economical.
|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>But the good ones I've seen
|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>So seldom are clean
| And the clean ones so seldom are comical
| 200 Main St.
| Berkeley, CA 94718</pre>
</dl>
<p> The lines can be hard-wrapped if needed, but the continuation line must begin with a space.</p>
<dl>
<dd>
<pre>| The Right Honorable Most Venerable and Righteous Samuel L.
&nbsp;<wbr>&nbsp;<wbr>Constable, Jr.
| 200 Main St.
| Berkeley, CA 94718</pre>
</dl>
<p> This syntax is borrowed from reStructuredText.</p>
<h2>Lists</h2>
<h3>Bullet lists</h3>
<p>A bullet list is a list of bulleted list items. A bulleted list item begins with a bullet (*, +, or -). Here is a simple example:</p>
<dl>
<dd>
<pre>*&nbsp;<wbr>one
*&nbsp;<wbr>two
*&nbsp;<wbr>three</pre>
</dl>
<p> This will produce a &quot;compact&quot; list. If you want a &quot;loose&quot; list, in which each item is formatted as a paragraph, put spaces between the items:</p>
<dl>
<dd>
<pre>*&nbsp;<wbr>one
*&nbsp;<wbr>two
*&nbsp;<wbr>three</pre>
</dl>
<p> The bullets need not be flush with the left margin; they may be indented one, two, or three spaces. The bullet must be followed by whitespace. </p>
<p> List items look best if subsequent lines are flush with the first line (after the bullet):</p>
<dl>
<dd>
<pre>*&nbsp;<wbr>here is my first
&nbsp;<wbr>&nbsp;<wbr>list item.
*&nbsp;<wbr>and my second.</pre>
</dl>
<p> But markdown also allows a &quot;lazy&quot; format:</p>
<dl>
<dd>
<pre>*&nbsp;<wbr>here is my first
list item.
*&nbsp;<wbr>and my second.</pre>
</dl>
<h3>The four-space rule</h3>
<p>A list item may contain multiple paragraphs and other block-level content. However, subsequent paragraphs must be preceded by a blank line and indented four spaces or a tab. The list will look better if the first paragraph is aligned with the rest:</p>
<dl>
<dd>
<pre>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>First paragraph.
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Continued.
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Second paragraph. With a code block, which must be indented
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>eight spaces:
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>{&nbsp;<wbr>code&nbsp;<wbr>}</pre>
</dl>
<p> List items may include other lists. In this case the preceding blank line is optional. The nested list must be indented four spaces or one tab:</p>
<dl>
<dd>
<pre>*&nbsp;<wbr>fruits
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&nbsp;<wbr>apples
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- macintosh
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- red delicious
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&nbsp;<wbr>pears
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&nbsp;<wbr>peaches
*&nbsp;<wbr>vegetables
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&nbsp;<wbr>broccoli
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&nbsp;<wbr>chard</pre>
</dl>
<p> As noted above, markdown allows you to write list items &quot;lazily,&quot; instead of indenting continuation lines. However, if there are multiple paragraphs or other blocks in a list item, the first line of each must be indented.</p>
<dl>
<dd>
<pre>+&nbsp;<wbr>A lazy, lazy, list
item.
+&nbsp;<wbr>Another one;&nbsp;<wbr>this looks
bad but is legal.
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Second paragraph of second
list item.</pre>
</dl>
<p> Note: Although the four-space rule for continuation paragraphs comes from the official markdown syntax guide, the reference implementation, Markdown.pl, does not follow it. So pandoc will give different results than Markdown.pl when authors have indented continuation paragraphs fewer than four spaces. </p>
<p> The markdown syntax guide is not explicit whether the four-space rule applies to all block-level content in a list item; it only mentions paragraphs and code blocks. But it implies that the rule applies to all block-level content (including nested lists), and pandoc interprets it that way.</p>
<h3>Ordered lists</h3>
<p>Ordered lists work just like bulleted lists, except that the items begin with enumerators rather than bullets. </p>
<p> In standard markdown, enumerators are decimal numbers followed by a period and a space. The numbers themselves are ignored, so there is no difference between this list:</p>
<dl>
<dd>
<pre>1.&nbsp;<wbr>&nbsp;<wbr>one
2.&nbsp;<wbr>&nbsp;<wbr>two
3.&nbsp;<wbr>&nbsp;<wbr>three</pre>
</dl>
<p> and this one:</p>
<dl>
<dd>
<pre>5.&nbsp;<wbr>&nbsp;<wbr>one
7.&nbsp;<wbr>&nbsp;<wbr>two
1.&nbsp;<wbr>&nbsp;<wbr>three</pre>
</dl>
<p> Extension: fancy_lists </p>
<p> Unlike standard markdown, Pandoc allows ordered list items to be marked with uppercase and lowercase letters and roman numerals, in addition to arabic numerals. List markers may be enclosed in parentheses or followed by a single right-parentheses or period. They must be separated from the text that follows by at least one space, and, if the list marker is a capital letter with a period, by at least two spaces.[1] </p>
<p> The fancy_lists extension also allows &#8216;#&#8217; to be used as an ordered list marker in place of a numeral:</p>
<dl>
<dd>
<pre>#. one
#. two</pre>
</dl>
<p> Extension: startnum </p>
<p> Pandoc also pays attention to the type of list marker used, and to the starting number, and both of these are preserved where possible in the output format. Thus, the following yields a list with numbers followed by a single parenthesis, starting with 9, and a sublist with lowercase roman numerals:</p>
<dl>
<dd>
<pre>&nbsp;<wbr>9)&nbsp;<wbr>&nbsp;<wbr>Ninth
10)&nbsp;<wbr>&nbsp;<wbr>Tenth
11)&nbsp;<wbr>&nbsp;<wbr>Eleventh
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>i. subone
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ii. subtwo
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>iii. subthree</pre>
</dl>
<p> Pandoc will start a new list each time a different type of list marker is used. So, the following will create three lists:</p>
<dl>
<dd>
<pre>(2)&nbsp;<wbr>Two
(5)&nbsp;<wbr>Three
1.&nbsp;<wbr>&nbsp;<wbr>Four
*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Five</pre>
</dl>
<p> If default list markers are desired, use #.:</p>
<dl>
<dd>
<pre>#.&nbsp;<wbr>&nbsp;<wbr>one
#.&nbsp;<wbr>&nbsp;<wbr>two
#.&nbsp;<wbr>&nbsp;<wbr>three</pre>
</dl>
<h3>Definition lists</h3>
<p>Extension: definition_lists </p>
<p> Pandoc supports definition lists, using a syntax inspired by PHP Markdown Extra and reStructuredText:[2]</p>
<dl>
<dd>
<pre>Term 1
:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Definition 1
Term 2 with&nbsp;<wbr>*inline markup*
:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Definition 2
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>{&nbsp;<wbr>some code, part of Definition 2&nbsp;<wbr>}
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Third paragraph of definition 2.</pre>
</dl>
<p> Each term must fit on one line, which may optionally be followed by a blank line, and must be followed by one or more definitions. A definition begins with a colon or tilde, which may be indented one or two spaces. The body of the definition (including the first line, aside from the colon or tilde) should be indented four spaces. A term may have multiple definitions, and each definition may consist of one or more block elements (paragraph, code block, list, etc.), each indented four spaces or one tab stop. </p>
<p> If you leave space after the definition (as in the example above), the blocks of the definitions will be considered paragraphs. In some output formats, this will mean greater spacing between term/definition pairs. For a compact definition list, do not leave space between the definition and the next term:</p>
<dl>
<dd>
<pre>Term 1
&nbsp;<wbr>&nbsp;<wbr>~&nbsp;<wbr>Definition 1
Term 2
&nbsp;<wbr>&nbsp;<wbr>~&nbsp;<wbr>Definition 2a
&nbsp;<wbr>&nbsp;<wbr>~&nbsp;<wbr>Definition 2b</pre>
</dl>
<h3>Numbered example lists</h3>
<p>Extension: example_lists </p>
<p> The special list marker @ can be used for sequentially numbered examples. The first list item with a @ marker will be numbered &#8216;1&#8217;, the next &#8216;2&#8217;, and so on, throughout the document. The numbered examples need not occur in a single list; each new list using @ will take up where the last stopped. So, for example:</p>
<dl>
<dd>
<pre>(@)&nbsp;<wbr>&nbsp;<wbr>My first example will be numbered&nbsp;<wbr>(1).
(@)&nbsp;<wbr>&nbsp;<wbr>My second example will be numbered&nbsp;<wbr>(2).
Explanation of examples.
(@)&nbsp;<wbr>&nbsp;<wbr>My third example will be numbered&nbsp;<wbr>(3).</pre>
</dl>
<p> Numbered examples can be labeled and referred to elsewhere in the document:</p>
<dl>
<dd>
<pre>(@good)&nbsp;<wbr>&nbsp;<wbr>This is a good example.
As&nbsp;<wbr>(@good)&nbsp;<wbr>illustrates, ...</pre>
</dl>
<p> The label can be any string of alphanumeric characters, underscores, or hyphens.</p>
<h3>Compact and loose lists</h3>
<p>Pandoc behaves differently from Markdown.pl on some &quot;edge cases&quot; involving lists. Consider this source:</p>
<dl>
<dd>
<pre>+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>First
+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Second:
	-&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Fee
	-&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Fie
	-&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Foe
+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Third</pre>
</dl>
<p> Pandoc transforms this into a &quot;compact list&quot; (with no &lt;p&gt; tags around &quot;First&quot;, &quot;Second&quot;, or &quot;Third&quot;), while markdown puts &lt;p&gt; tags around &quot;Second&quot; and &quot;Third&quot; (but not &quot;First&quot;), because of the blank space around &quot;Third&quot;. Pandoc follows a simple rule: if the text is followed by a blank line, it is treated as a paragraph. Since &quot;Second&quot; is followed by a list, and not a blank line, it isn&#8217;t treated as a paragraph. The fact that the list is followed by a blank line is irrelevant. (Note: Pandoc works this way even when the markdown_strict format is specified. This behavior is consistent with the official markdown syntax description, even though it is different from that of Markdown.pl.)</p>
<h3>Ending a list</h3>
<p>What if you want to put an indented code block after a list?</p>
<dl>
<dd>
<pre>-&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>item one
-&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>item two
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>{&nbsp;<wbr>my code block&nbsp;<wbr>}</pre>
</dl>
<p> Trouble! Here pandoc (like other markdown implementations) will treat {&nbsp;<wbr>my code block&nbsp;<wbr>} as the second paragraph of item two, and not as a code block. </p>
<p> To &quot;cut off&quot; the list after item two, you can insert some non-indented content, like an HTML comment, which won&#8217;t produce visible output in any format:</p>
<dl>
<dd>
<pre>-&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>item one
-&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>item two
&lt;!-- end of list --&gt;
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>{&nbsp;<wbr>my code block&nbsp;<wbr>}</pre>
</dl>
<p> You can use the same trick if you want two consecutive lists instead of one big list:</p>
<dl>
<dd>
<pre>1.&nbsp;<wbr>&nbsp;<wbr>one
2.&nbsp;<wbr>&nbsp;<wbr>two
3.&nbsp;<wbr>&nbsp;<wbr>three
&lt;!-- --&gt;
1.&nbsp;<wbr>&nbsp;<wbr>uno
2.&nbsp;<wbr>&nbsp;<wbr>dos
3.&nbsp;<wbr>&nbsp;<wbr>tres</pre>
</dl>
<h2>Horizontal Rules</h2>
<p>A line containing a row of three or more *, -, or _ characters (optionally separated by spaces) produces a horizontal rule:</p>
<dl>
<dd>
<pre>*&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>&nbsp;<wbr>*
---------------</pre>
</dl>
<h2>Tables</h2>
<p>Four kinds of tables may be used. The first three kinds presuppose the use of a fixed-width font, such as Courier. The fourth kind can be used with proportionally spaced fonts, as it does not require lining up columns.</p>
<h3>Simple tables</h3>
<p>Extension: simple_tables, table_captions </p>
<p> Simple tables look like this:</p>
<dl>
<dd>
<pre>&nbsp;<wbr>&nbsp;<wbr>Right&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Left&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Center&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Default
-------&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>------ ----------&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-------
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>123&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>123&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>123&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>123
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1
Table:&nbsp;<wbr>&nbsp;<wbr>Demonstration of simple table syntax.</pre>
</dl>
<p> The headers and table rows must each fit on one line. Column alignments are determined by the position of the header text relative to the dashed line below it:[3]</p>
<dl>
<dt>&bull;</p>
<dd>If the dashed line is flush with the header text on the right side but extends beyond it on the left, the column is right-aligned.</p>
<dt>&bull;</p>
<dd>If the dashed line is flush with the header text on the left side but extends beyond it on the right, the column is left-aligned.</p>
<dt>&bull;</p>
<dd>If the dashed line extends beyond the header text on both sides, the column is centered.</p>
<dt>&bull;</p>
<dd>If the dashed line is flush with the header text on both sides, the default alignment is used (in most cases, this will be left).</dl>
<p> The table must end with a blank line, or a line of dashes followed by a blank line. A caption may optionally be provided (as illustrated in the example above). A caption is a paragraph beginning with the string Table: (or just :), which will be stripped off. It may appear either before or after the table. </p>
<p> The column headers may be omitted, provided a dashed line is used to end the table. For example:</p>
<dl>
<dd>
<pre>-------&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>------ ----------&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-------
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>123&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>123&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>123&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>123
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1
-------&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>------ ----------&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-------</pre>
</dl>
<p> When headers are omitted, column alignments are determined on the basis of the first line of the table body. So, in the tables above, the columns would be right, left, center, and right aligned, respectively.</p>
<h3>Multiline tables</h3>
<p>Extension: multiline_tables, table_captions </p>
<p> Multiline tables allow headers and table rows to span multiple lines of text (but cells that span multiple columns or rows of the table are not supported). Here is an example:</p>
<dl>
<dd>
<pre>-------------------------------------------------------------
&nbsp;<wbr>Centered&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Default&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Right Left
&nbsp;<wbr>&nbsp;<wbr>Header&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Aligned&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Aligned Aligned
----------- ------- --------------- -------------------------
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>First&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>row&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12.0 Example of a row that
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>spans multiple lines.
&nbsp;<wbr>&nbsp;<wbr>Second&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>row&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>5.0 Here's another one. Note
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the blank line between
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rows.
-------------------------------------------------------------
Table: Here's the caption. It, too, may span
multiple lines.</pre>
</dl>
<p> These work like simple tables, but with the following differences:</p>
<dl>
<dt>&bull;</p>
<dd>They must begin with a row of dashes, before the header text (unless the headers are omitted).</p>
<dt>&bull;</p>
<dd>They must end with a row of dashes, then a blank line.</p>
<dt>&bull;</p>
<dd>The rows must be separated by blank lines.</dl>
<p> In multiline tables, the table parser pays attention to the widths of the columns, and the writers try to reproduce these relative widths in the output. So, if you find that one of the columns is too narrow in the output, try widening it in the markdown source. </p>
<p> Headers may be omitted in multiline tables as well as simple tables:</p>
<dl>
<dd>
<pre>----------- ------- --------------- -------------------------
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>First&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>row&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12.0 Example of a row that
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>spans multiple lines.
&nbsp;<wbr>&nbsp;<wbr>Second&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>row&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>5.0 Here's another one. Note
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the blank line between
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rows.
----------- ------- --------------- -------------------------
: Here's a multiline table without headers.</pre>
</dl>
<p> It is possible for a multiline table to have just one row, but the row should be followed by a blank line (and then the row of dashes that ends the table), or the table may be interpreted as a simple table.</p>
<h3>Grid tables</h3>
<p>Extension: grid_tables, table_captions </p>
<p> Grid tables look like this:</p>
<dl>
<dd>
<pre>: Sample grid table.
+---------------+---------------+--------------------+
| Fruit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| Price&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| Advantages&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|
+===============+===============+====================+
| Bananas&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>$1.34&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| - built-in wrapper |
|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| - bright color&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|
+---------------+---------------+--------------------+
| Oranges&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>$2.10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| - cures scurvy&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|
|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| - tasty&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|
+---------------+---------------+--------------------+</pre>
</dl>
<p> The row of =s separates the header from the table body, and can be omitted for a headerless table. The cells of grid tables may contain arbitrary block elements (multiple paragraphs, code blocks, lists, etc.). Alignments are not supported, nor are cells that span multiple columns or rows. Grid tables can be created easily using Emacs table mode.</p>
<h3>Pipe tables</h3>
<p>Extension: pipe_tables, table_captions </p>
<p> Pipe tables look like this:</p>
<dl>
<dd>
<pre>| Right | Left | Default | Center |
|------:|:-----|---------|:------:|
|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>12&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12&nbsp;<wbr>&nbsp;<wbr>|
|&nbsp;<wbr>&nbsp;<wbr>123&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>123 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>123&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>123&nbsp;<wbr>&nbsp;<wbr>|
|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1 |&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>|
&nbsp;<wbr>&nbsp;<wbr>: Demonstration of simple table syntax.</pre>
</dl>
<p> The syntax is the same as in PHP markdown extra. The beginning and ending pipe characters are optional, but pipes are required between all columns. The colons indicate column alignment as shown. The header can be omitted, but the horizontal line must still be included, as it defines column alignments. </p>
<p> Since the pipes indicate column boundaries, columns need not be vertically aligned, as they are in the above example. So, this is a perfectly legal (though ugly) pipe table:</p>
<dl>
<dd>
<pre>fruit| price
-----|-----:
apple|2.05
pear|1.37
orange|3.09</pre>
</dl>
<p> The cells of pipe tables cannot contain block elements like paragraphs and lists, and cannot span multiple lines. </p>
<p> Note: Pandoc also recognizes pipe tables of the following form, as can produced by Emacs&#8217; orgtbl-mode:</p>
<dl>
<dd>
<pre>| One | Two&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|
|-----+-------|
| my&nbsp;<wbr>&nbsp;<wbr>| table |
| is&nbsp;<wbr>&nbsp;<wbr>| nice&nbsp;<wbr>&nbsp;<wbr>|</pre>
</dl>
<p> The difference is that + is used instead of |. Other orgtbl features are not supported. In particular, to get non-default column alignment, you&#8217;ll need to add colons as above.</p>
<h2>Title Block</h2>
<p>Extension: pandoc_title_block </p>
<p> If the file begins with a title block</p>
<dl>
<dd>
<pre>%&nbsp;<wbr>title
%&nbsp;<wbr>author(s)&nbsp;<wbr>(separated by semicolons)
%&nbsp;<wbr>date</pre>
</dl>
<p> it will be parsed as bibliographic information, not regular text. (It will be used, for example, in the title of standalone LaTeX or HTML output.) The block may contain just a title, a title and an author, or all three elements. If you want to include an author but no title, or a title and a date but no author, you need a blank line:</p>
<dl>
<dd>
<pre>%
%&nbsp;<wbr>Author
%&nbsp;<wbr>My title
%
%&nbsp;<wbr>June 15, 2006</pre>
</dl>
<p> The title may occupy multiple lines, but continuation lines must begin with leading space, thus:</p>
<dl>
<dd>
<pre>%&nbsp;<wbr>My title
&nbsp;<wbr>&nbsp;<wbr>on multiple lines</pre>
</dl>
<p> If a document has multiple authors, the authors may be put on separate lines with leading space, or separated by semicolons, or both. So, all of the following are equivalent:</p>
<dl>
<dd>
<pre>%&nbsp;<wbr>Author One
&nbsp;<wbr>&nbsp;<wbr>Author Two
%&nbsp;<wbr>Author One;&nbsp;<wbr>Author Two
%&nbsp;<wbr>Author One;
&nbsp;<wbr>&nbsp;<wbr>Author Two</pre>
</dl>
<p> The date must fit on one line. </p>
<p> All three metadata fields may contain standard inline formatting (italics, links, footnotes, etc.). </p>
<p> Title blocks will always be parsed, but they will affect the output only when the &#8211;standalone (-s) option is chosen. In HTML output, titles will appear twice: once in the document head &#8212; this is the title that will appear at the top of the window in a browser &#8212; and once at the beginning of the document body. The title in the document head can have an optional prefix attached (&#8211;title-prefix or -T option). The title in the body appears as an H1 element with class &quot;title&quot;, so it can be suppressed or reformatted with CSS. If a title prefix is specified with -T and no title block appears in the document, the title prefix will be used by itself as the HTML title. </p>
<p> The man page writer extracts a title, man page section number, and other header and footer information from the title line. The title is assumed to be the first word on the title line, which may optionally end with a (single-digit) section number in parentheses. (There should be no space between the title and the parentheses.) Anything after this is assumed to be additional footer and header text. A single pipe character (|) should be used to separate the footer text from the header text. Thus,</p>
<dl>
<dd>
<pre>%&nbsp;<wbr><a href="//www.systutorials.com/docs/linux/man/1-PANDOC/">PANDOC</a>(1)</pre>
</dl>
<p> will yield a man page with the title PANDOC and section 1.</p>
<dl>
<dd>
<pre>%&nbsp;<wbr><a href="//www.systutorials.com/docs/linux/man/1-PANDOC/">PANDOC</a>(1)&nbsp;<wbr>Pandoc User Manuals</pre>
</dl>
<p> will also have &quot;Pandoc User Manuals&quot; in the footer.</p>
<dl>
<dd>
<pre>%&nbsp;<wbr><a href="//www.systutorials.com/docs/linux/man/1-PANDOC/">PANDOC</a>(1)&nbsp;<wbr>Pandoc User Manuals | Version 4.0</pre>
</dl>
<p> will also have &quot;Version 4.0&quot; in the header.</p>
<h2>Yaml Metadata Block</h2>
<p>Extension: yaml_metadata_block </p>
<p> A YAML metadata block is a valid YAML object, delimited by a line of three hyphens (&#8212;) at the top and a line of three hyphens (&#8212;) or three dots (&#8230;) at the bottom. A YAML metadata block may occur anywhere in the document, but if it is not at the beginning, it must be preceded by a blank line. </p>
<p> Metadata will be taken from the fields of the YAML object and added to any existing document metadata. Metadata can contain lists and objects (nested arbitrarily), but all string scalars will be interpreted as markdown. Fields with names ending in an underscore will be ignored by pandoc. (They may be given a role by external processors.) </p>
<p> A document may contain multiple metadata blocks. The metadata fields will be combined through a left-biased union: if two metadata blocks attempt to set the same field, the value from the first block will be taken. </p>
<p> Note that YAML escaping rules must be followed. Thus, for example, if a title contains a colon, it must be quoted. The pipe character (|) can be used to begin an indented block that will be interpreted literally, without need for escaping. This form is necessary when the field contains blank lines:</p>
<dl>
<dd>
<pre>---
title:&nbsp;<wbr>&nbsp;<wbr>'This is the title: it contains a colon'
author:
- name: Author One
&nbsp;<wbr>&nbsp;<wbr>affiliation: University of Somewhere
- name: Author Two
&nbsp;<wbr>&nbsp;<wbr>affiliation: University of Nowhere
tags:&nbsp;<wbr>[nothing, nothingness]
abstract: |
&nbsp;<wbr>&nbsp;<wbr>This is the abstract.
&nbsp;<wbr>&nbsp;<wbr>It consists of two paragraphs.
...</pre>
</dl>
<p> Template variables will be set automatically from the metadata. Thus, for example, in writing HTML, the variable abstract will be set to the HTML equivalent of the markdown in the abstract field:</p>
<dl>
<dd>
<pre>&lt;p&gt;This is the abstract.&lt;/p&gt;
&lt;p&gt;It consists of two paragraphs.&lt;/p&gt;</pre>
</dl>
<p> Note: The author variable in the default templates expects a simple list or string. To use the structured authors in the example, you would need a custom template. For example:</p>
<dl>
<dd>
<pre>$for(author)$
$if(author.name)$
$author.name$$if(author.affiliation)$&nbsp;<wbr>($author.affiliation$)$endif$
$else$
$author$
$endif$
$endfor$</pre>
</dl>
<h2>Backslash Escapes</h2>
<p>Extension: all_symbols_escapable </p>
<p> Except inside a code block or inline code, any punctuation or space character preceded by a backslash will be treated literally, even if it would normally indicate formatting. Thus, for example, if one writes</p>
<dl>
<dd>
<pre>*\*hello\**</pre>
</dl>
<p> one will get</p>
<dl>
<dd>
<pre>&lt;em&gt;*hello*&lt;/em&gt;</pre>
</dl>
<p> instead of</p>
<dl>
<dd>
<pre>&lt;strong&gt;hello&lt;/strong&gt;</pre>
</dl>
<p> This rule is easier to remember than standard markdown&#8217;s rule, which allows only the following characters to be backslash-escaped:</p>
<dl>
<dd>
<pre>\`*_{}[]()&gt;#+-.!</pre>
</dl>
<p> (However, if the markdown_strict format is used, the standard markdown rule will be used.) </p>
<p> A backslash-escaped space is parsed as a nonbreaking space. It will appear in TeX output as ~ and in HTML and XML as \&amp;#160; or \&amp;nbsp;. </p>
<p> A backslash-escaped newline (i.e. a backslash occurring at the end of a line) is parsed as a hard line break. It will appear in TeX output as \ and in HTML as &lt;br&nbsp;<wbr>/&gt;. This is a nice alternative to markdown&#8217;s &quot;invisible&quot; way of indicating hard line breaks using two trailing spaces on a line. </p>
<p> Backslash escapes do not work in verbatim contexts.</p>
<h2>Smart Punctuation</h2>
<p>Extension </p>
<p> If the &#8211;smart option is specified, pandoc will produce typographically correct output, converting straight quotes to curly quotes, &#8212; to em-dashes, &#8212; to en-dashes, and &#8230; to ellipses. Nonbreaking spaces are inserted after certain abbreviations, such as &quot;Mr.&quot; </p>
<p> Note: if your LaTeX template uses the csquotes package, pandoc will detect automatically this and use nquote{&#8230;} for quoted text.</p>
<h2>Inline Formatting</h2>
<h3>Emphasis</h3>
<p>To emphasize some text, surround it with *s or _, like this:</p>
<dl>
<dd>
<pre>This text is&nbsp;<wbr>_emphasized with underscores_, and this
is&nbsp;<wbr>*emphasized with asterisks*.</pre>
</dl>
<p> Double * or _ produces strong emphasis:</p>
<dl>
<dd>
<pre>This is&nbsp;<wbr>**strong emphasis**&nbsp;<wbr>and&nbsp;<wbr>__with underscores__.</pre>
</dl>
<p> A * or _ character surrounded by spaces, or backslash-escaped, will not trigger emphasis:</p>
<dl>
<dd>
<pre>This is&nbsp;<wbr>*&nbsp;<wbr>not emphasized&nbsp;<wbr>*, and&nbsp;<wbr>\*neither is this\*.</pre>
</dl>
<p> Extension: intraword_underscores </p>
<p> Because _ is sometimes used inside words and identifiers, pandoc does not interpret a _ surrounded by alphanumeric characters as an emphasis marker. If you want to emphasize just part of a word, use *:</p>
<dl>
<dd>
<pre>feas*ible*, not feas*able*.</pre>
</dl>
<h3>Strikeout</h3>
<p>Extension: strikeout </p>
<p> To strikeout a section of text with a horizontal line, begin and end it with ~~. Thus, for example,</p>
<dl>
<dd>
<pre>This&nbsp;<wbr>~~is deleted text.~~</pre>
</dl>
<h3>Superscripts and subscripts</h3>
<p>Extension: superscript, subscript </p>
<p> Superscripts may be written by surrounding the superscripted text by ^ characters; subscripts may be written by surrounding the subscripted text by ~ characters. Thus, for example,</p>
<dl>
<dd>
<pre>H~2~O is a liquid.&nbsp;<wbr>&nbsp;<wbr>2^10^&nbsp;<wbr>is 1024.</pre>
</dl>
<p> If the superscripted or subscripted text contains spaces, these spaces must be escaped with backslashes. (This is to prevent accidental superscripting and subscripting through the ordinary use of ~ and ^.) Thus, if you want the letter P with &#8216;a cat&#8217; in subscripts, use P~a\&nbsp;<wbr>cat~, not P~a cat~.</p>
<h3>Verbatim</h3>
<p>To make a short span of text verbatim, put it inside backticks:</p>
<dl>
<dd>
<pre>What is the difference between&nbsp;<wbr>`&gt;&gt;=`&nbsp;<wbr>and&nbsp;<wbr>`&gt;&gt;`?</pre>
</dl>
<p> If the verbatim text includes a backtick, use double backticks:</p>
<dl>
<dd>
<pre>Here is a literal backtick&nbsp;<wbr>``&nbsp;<wbr>`&nbsp;<wbr>``.</pre>
</dl>
<p> (The spaces after the opening backticks and before the closing backticks will be ignored.) </p>
<p> The general rule is that a verbatim span starts with a string of consecutive backticks (optionally followed by a space) and ends with a string of the same number of backticks (optionally preceded by a space). </p>
<p> Note that backslash-escapes (and other markdown constructs) do not work in verbatim contexts:</p>
<dl>
<dd>
<pre>This is a backslash followed by an asterisk:&nbsp;<wbr>`\*`.</pre>
</dl>
<p> Extension: inline_code_attributes </p>
<p> Attributes can be attached to verbatim text, just as with fenced code blocks:</p>
<dl>
<dd>
<pre>`&lt;$&gt;`{.haskell}</pre>
</dl>
<h2>Math</h2>
<p>Extension: tex_math_dollars </p>
<p> Anything between two $ characters will be treated as TeX math. The opening $ must have a character immediately to its right, while the closing $ must have a character immediately to its left. Thus, $20,000 and&nbsp;<wbr>$30,000 won&#8217;t parse as math. If for some reason you need to enclose text in literal $ characters, backslash-escape them and they won&#8217;t be treated as math delimiters. </p>
<p> TeX math will be printed in all output formats. How it is rendered depends on the output format:</p>
<dl>
<dt><code>Markdown, LaTeX, Org-Mode, ConTeXt</code></p>
<dd>It will appear verbatim between $ characters.</p>
<dl>
<dd></dl>
<dt><code>reStructuredText</code></p>
<dd>It will be rendered using an interpreted text role :math:, as described here.</p>
<dl>
<dd></dl>
<dt><code>AsciiDoc</code></p>
<dd>It will be rendered as latexmath:[&#8230;].</p>
<dl>
<dd></dl>
<dt><code>Texinfo</code></p>
<dd>It will be rendered inside a @math command.</p>
<dl>
<dd></dl>
<dt><code>groff man</code></p>
<dd>It will be rendered verbatim without $&#8217;s.</p>
<dl>
<dd></dl>
<dt><code>MediaWiki</code></p>
<dd>It will be rendered inside &lt;math&gt; tags.</p>
<dl>
<dd></dl>
<dt><code>Textile</code></p>
<dd>It will be rendered inside &lt;span class=&quot;math&quot;&gt; tags.</p>
<dl>
<dd></dl>
<dt><code>RTF, OpenDocument, ODT</code></p>
<dd>It will be rendered, if possible, using unicode characters, and will otherwise appear verbatim.</p>
<dl>
<dd></dl>
<dt><code>Docbook</code></p>
<dd>If the &#8211;mathml flag is used, it will be rendered using mathml in an inlineequation or informalequation tag. Otherwise it will be rendered, if possible, using unicode characters.</p>
<dl>
<dd></dl>
<dt><code>Docx</code></p>
<dd>It will be rendered using OMML math markup.</p>
<dl>
<dd></dl>
<dt><code>FictionBook2</code></p>
<dd>If the &#8211;webtex option is used, formulas are rendered as images using Google Charts or other compatible web service, downloaded and embedded in the e-book. Otherwise, they will appear verbatim.</p>
<dl>
<dd></dl>
<dt><code>HTML, Slidy, DZSlides, S5, EPUB</code></p>
<dd>The way math is rendered in HTML will depend on the command-line options selected:</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>The default is to render TeX math as far as possible using unicode characters, as with RTF, DocBook, and OpenDocument output. Formulas are put inside a span with class=&quot;math&quot;, so that they may be styled differently from the surrounding text if needed.</p>
<dt>2.</p>
<dd>If the &#8211;latexmathml option is used, TeX math will be displayed between $ or $$ characters and put in &lt;span&gt; tags with class LaTeX. The LaTeXMathML script will be used to render it as formulas. (This trick does not work in all browsers, but it works in Firefox. In browsers that do not support LaTeXMathML, TeX math will appear verbatim between $ characters.)</p>
<dt>3.</p>
<dd>If the &#8211;jsmath option is used, TeX math will be put inside &lt;span&gt; tags (for inline math) or &lt;div&gt; tags (for display math) with class math. The jsMath script will be used to render it.</p>
<dt>4.</p>
<dd>If the &#8211;mimetex option is used, the mimeTeX CGI script will be called to generate images for each TeX formula. This should work in all browsers. The &#8211;mimetex option takes an optional URL as argument. If no URL is specified, it will be assumed that the mimeTeX CGI script is at /cgi-bin/mimetex.cgi.</p>
<dt>5.</p>
<dd>If the &#8211;gladtex option is used, TeX formulas will be enclosed in &lt;eq&gt; tags in the HTML output. The resulting htex file may then be processed by gladTeX, which will produce image files for each formula and an html file with links to these images. So, the procedure is:</p>
<dl>
<dd>
<dl>
<dd>
<pre>pandoc -s --gladtex myfile.txt -o myfile.htex
gladtex -d myfile-images myfile.htex
#&nbsp;<wbr>produces myfile.html and images in myfile-images</pre>
</dl>
</dl>
<dt>6.</p>
<dd>If the &#8211;webtex option is used, TeX formulas will be converted to &lt;img&gt; tags that link to an external script that converts formulas to images. The formula will be URL-encoded and concatenated with the URL provided. If no URL is specified, the Google Chart API will be used (<a rel="nofollow" href="http://chart.apis.google.com/chart?cht=tx">http://chart.apis.google.com/chart?cht=tx</a>&amp;chl=).</p>
<dt>7.</p>
<dd>If the &#8211;mathjax option is used, TeX math will be displayed between \(&#8230;\) (for inline math) or \[&#8230;\] (for display math) and put in &lt;span&gt; tags with class math. The MathJax script will be used to render it as formulas.</dl>
</dl>
</dl>
<h2>Raw Html</h2>
<p>Extension: raw_html </p>
<p> Markdown allows you to insert raw HTML (or DocBook) anywhere in a document (except verbatim contexts, where &lt;, &gt;, and &amp; are interpreted literally). (Technically this is not an extension, since standard markdown allows it, but it has been made an extension so that it can be disabled if desired.) </p>
<p> The raw HTML is passed through unchanged in HTML, S5, Slidy, Slideous, DZSlides, EPUB, Markdown, and Textile output, and suppressed in other formats. </p>
<p> Extension: markdown_in_html_blocks </p>
<p> Standard markdown allows you to include HTML &quot;blocks&quot;: blocks of HTML between balanced tags that are separated from the surrounding text with blank lines, and start and end at the left margin. Within these blocks, everything is interpreted as HTML, not markdown; so (for example), * does not signify emphasis. </p>
<p> Pandoc behaves this way when the markdown_strict format is used; but by default, pandoc interprets material between HTML block tags as markdown. Thus, for example, Pandoc will turn</p>
<dl>
<dd>
<pre>&lt;table&gt;
	&lt;tr&gt;
		&lt;td&gt;*one*&lt;/td&gt;
		&lt;td&gt;[a link](<a rel="nofollow" href="http://google.com)">http://google.com)</a>&lt;/td&gt;
	&lt;/tr&gt;
&lt;/table&gt;</pre>
</dl>
<p> into</p>
<dl>
<dd>
<pre>&lt;table&gt;
	&lt;tr&gt;
		&lt;td&gt;&lt;em&gt;one&lt;/em&gt;&lt;/td&gt;
		&lt;td&gt;&lt;a href=&quot;<a rel="nofollow" href="http://google.com">http://google.com</a>&quot;&gt;a link&lt;/a&gt;&lt;/td&gt;
	&lt;/tr&gt;
&lt;/table&gt;</pre>
</dl>
<p> whereas Markdown.pl will preserve it as is. </p>
<p> There is one exception to this rule: text between &lt;script&gt; and &lt;style&gt; tags is not interpreted as markdown. </p>
<p> This departure from standard markdown should make it easier to mix markdown with HTML block elements. For example, one can surround a block of markdown text with &lt;div&gt; tags without preventing it from being interpreted as markdown.</p>
<h2>Raw Tex</h2>
<p>Extension: raw_tex </p>
<p> In addition to raw HTML, pandoc allows raw LaTeX, TeX, and ConTeXt to be included in a document. Inline TeX commands will be preserved and passed unchanged to the LaTeX and ConTeXt writers. Thus, for example, you can use LaTeX to include BibTeX citations:</p>
<dl>
<dd>
<pre>This result was proved in&nbsp;<wbr>
