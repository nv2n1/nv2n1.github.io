---
title: "groff_ms(7)"
name: "groff_ms"
section: "7"
letter: "g"
url: "/docs/linux/man/7-groff_ms/"
description: "groff_ms – GNU roff manuscript macro package for formatting documents"
---

<p>groff_ms &#8211; GNU roff manuscript macro package for formatting documents</p>
<h2>Synopsis</h2>
<p>[<i>option</i> &#8230;] [<i>input-file</i> &#8230;] [<i>option</i> &#8230;] [<i>input-file</i> &#8230;]</p>
<h2>Description</h2>
<p>This manual page describes the GNU version of the <i>ms</i> macros, part of the <i>groff</i> typesetting system. The <i>ms</i> macros are mostly compatible with the documented behavior of the 4.3 BSD Unix <i>ms</i> macros (see <i>Differences from troff ms</i> below for details). The <i>ms</i> macros are suitable for reports, letters, books, and technical documentation.</p>
<h2>Usage</h2>
<p>The <i>ms</i> macro package expects files to have a certain amount of structure. The simplest documents can begin with a paragraph macro and consist of text separated by paragraph macros or even blank lines. Longer documents have a structure as follows:</p>
<dl>
<dt><code>Document type</code></p>
<dd>If you use the <code>RP</code> (report) macro at the beginning of the document, <i>groff</i> prints the cover page information on its own page; otherwise it prints the information on the first page with your document text immediately following. Other document formats found in AT&amp;T <i>troff</i> are specific to AT&amp;T or Berkeley, and are not supported in <i>groff ms</i>.</p>
<dt><code>Format and layout</code></p>
<dd>By setting number registers, you can change your document&#8217;s margins, spacing, headers and footers, footnotes, and the base point size for the text. See <i>Document control registers</i> below for more details.</p>
<dt><code>Cover page</code></p>
<dd>A cover page consists of a title, and optionally the author&#8217;s name and institution, an abstract, and the date. See <i>Cover page macros</i> below for more details.</p>
<dt><code>Body</code></p>
<dd>Following the cover page is your document. It consists of paragraphs, headings, and lists.</p>
<dt><code>Table of contents</code></p>
<dd>Longer documents usually include a table of contents, which you can add by placing the <code>TC</code> macro at the end of your document.</dl>
<h3>Document control registers</h3>
<p>The following table lists the document control number registers. For the sake of consistency, set registers related to margins at the beginning of your document, or just after the <code>RP</code> macro. </p>
<p> <code>Margin settings</code></p>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>Reg.</code></td>
<td ALIGN=center><code>Definition</code></td>
<td ALIGN=center><code>Effective</code></td>
<td ALIGN=center><code>Default</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>PO</td>
<td>Page offset (left margin)</td>
<td>next page</td>
<td>1i
</td>
</tr>
<tr VALIGN=top>
<td>LL</td>
<td>Line length</td>
<td>next paragraph</td>
<td>6i
</td>
</tr>
<tr VALIGN=top>
<td>LT</td>
<td>Header/footer length</td>
<td>next paragraph</td>
<td>6i
</td>
</tr>
<tr VALIGN=top>
<td>HM</td>
<td>Top (header) margin</td>
<td>next page</td>
<td>1i
</td>
</tr>
<tr VALIGN=top>
<td>FM</td>
<td>Bottom (footer) margin</td>
<td>next page</td>
<td>1i
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
</table>
</dl>
<p> <code>Text settings</code></p>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>Reg.</code></td>
<td ALIGN=center><code>Definition</code></td>
<td ALIGN=center><code>Effective</code></td>
<td ALIGN=center><code>Default</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>PS</td>
<td> Point size </td>
<td>next paragraph</td>
<td>10p
</td>
</tr>
<tr VALIGN=top>
<td>VS</td>
<td> Line spacing (leading) </td>
<td>next paragraph</td>
<td>12p
</td>
</tr>
<tr VALIGN=top>
<td>PSINCR</td>
<td> Point size increment for section headings of increasing importance </td>
<td>next heading</td>
<td>1p
</td>
</tr>
<tr VALIGN=top>
<td>GROWPS</td>
<td> Heading level beyond which PSINCR is ignored </td>
<td>next heading</td>
<td>0
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
</table>
</dl>
<p> <code>Paragraph settings</code></p>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>Reg.</code></td>
<td ALIGN=center><code>Definition</code></td>
<td ALIGN=center><code>Effective</code></td>
<td ALIGN=center><code>Default</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>PI</td>
<td> Initial indent </td>
<td>next paragraph</td>
<td>5n
</td>
</tr>
<tr VALIGN=top>
<td>PD</td>
<td> Space between paragraphs </td>
<td>next paragraph</td>
<td>0.3v
</td>
</tr>
<tr VALIGN=top>
<td>QI</td>
<td> Quoted paragraph indent </td>
<td>next paragraph</td>
<td>5n
</td>
</tr>
<tr VALIGN=top>
<td>PORPHANS</td>
<td> Number of initial lines to be kept together </td>
<td>next paragraph</td>
<td>1
</td>
</tr>
<tr VALIGN=top>
<td>HORPHANS</td>
<td> Number of initial lines to be kept with heading </td>
<td>next heading</td>
<td>1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
</table>
</dl>
<p> <code>Footnote settings</code></p>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>Reg.</code></td>
<td ALIGN=center><code>Definition</code></td>
<td ALIGN=center><code>Effective</code></td>
<td ALIGN=center><code>Default</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>FL</td>
<td>Footnote length</td>
<td>next footnote</td>
<td>
[LL]*5/6
</td>
</tr>
<tr VALIGN=top>
<td>FI</td>
<td>Footnote indent</td>
<td>next footnote</td>
<td>2n
</td>
</tr>
<tr VALIGN=top>
<td>FF</td>
<td>Footnote format</td>
<td>next footnote</td>
<td>0
</td>
</tr>
<tr VALIGN=top>
<td>FPS</td>
<td>Point size</td>
<td>next footnote</td>
<td>
[PS]-2
</td>
</tr>
<tr VALIGN=top>
<td>FVS</td>
<td>Vert. spacing</td>
<td>next footnote</td>
<td>
[FPS]+2
</td>
</tr>
<tr VALIGN=top>
<td>FPD</td>
<td>Para. spacing</td>
<td>next footnote</td>
<td>
[PD]/2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
</table>
</dl>
<p> <code>Other settings</code></p>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>Reg.</code></td>
<td ALIGN=center><code>Definition</code></td>
<td ALIGN=center><code>Effective</code></td>
<td ALIGN=center><code>Default</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>DD</td>
<td>Display, table, eqn, pic spacing</td>
<td>next para.</td>
<td>0.5v
</td>
</tr>
<tr VALIGN=top>
<td>MINGW</td>
<td>Minimum width between columns</td>
<td>next page</td>
<td>2n
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
</table>
</dl>
<h3>Cover page macros</h3>
<p>Use the following macros to create a cover page for your document in the order shown.</p>
<dl>
<dt><code>.RP </code>[<code>no</code>]</p>
<dd>Specifies the report format for your document. The report format creates a separate cover page. With no <code>RP</code> macro, <i>groff</i> prints a subset of the cover page on page~1 of your document.</p>
<dd>If you use the optional <code>no</code> argument, <i>groff</i> prints a title page but does not repeat any of the title page information (title, author, abstract, etc.) on page~1 of the document.</p>
<dt><code>.P1</code></p>
<dd>(P-one) Prints the header on page~1. The default is to suppress the header.</p>
<dt><code>.DA</code></p>
<dd>[<i>xxx</i>] (optional) Print the current date, or the arguments to the macro if any, on the title page (if specified) and in the footers. This is the default for <i>nroff</i>.</p>
<dt><code>.ND</code></p>
<dd>[<i>xxx</i>] (optional) Print the current date, or the arguments to the macro if any, on the title page (if specified) but not in the footers. This is the default for <i>troff</i>.</p>
<dt><code>.TL</code></p>
<dd>Specifies the document title. <i>Groff</i> collects text following the <code>TL</code> macro into the title, until reaching the author name or abstract.</p>
<dt><code>.AU</code></p>
<dd>Specifies the author&#8217;s name. You can specify multiple authors by using an <code>AU</code> macro for each author.</p>
<dt><code>.AI</code></p>
<dd>Specifies the author&#8217;s institution. You can specify multiple institutions.</p>
<dt><code>.AB </code>[<code>no</code>]</p>
<dd>Begins the abstract. The default is to print the word <code>ABSTRACT</code>, centered and in italics, above the text of the abstract. The option <code>no</code> suppresses this heading.</p>
<dt><code>.AE</code></p>
<dd>End the abstract.</dl>
<h3>Paragraphs</h3>
<p>Use the <code>PP</code> macro to create indented paragraphs, and the <code>LP</code> macro to create paragraphs with no initial indent. </p>
<p> The <code>QP</code> macro indents all text at both left and right margins by the amount of the register <code>QI</code>. The effect is reminiscent of the HTML <code>&lt;BLOCKQUOTE&gt;</code> tag. The next paragraph or heading returns the margins to normal. <code>QP</code> inserts the vertical space specified in register <code>PD</code> as inter-paragraph spacing. </p>
<p> A paragraph bracketed between the macros <code>QS</code> and <code>QE</code> has the same appearance as a paragraph started with <code>QP</code> and a following paragraph started with <code>LP</code>. Both <code>QS</code> and <code>QE</code> insert the inter-paragraph spacing specified in <code>PD</code> and the text is indented on both sides by the amount of register <code>QI</code>. The text between <code>QS</code> and <code>QE</code> can be split into further paragraphs by using <code>.LP</code> or <code>.PP</code>. </p>
<p> The <code>XP</code> macro produces an &#8220;exdented&#8221; paragraph; that is, one with a hanging indent. The first line of the paragraph begins at the left margin, and subsequent lines are indented (the opposite of <code>PP</code>). </p>
<p> For each of the above paragraph types, and also for any list entry introduced by the <code>IP</code> macro (described later), the document control register <code>PORPHANS</code>, sets the <i>minimum</i> number of lines which must be printed, after the start of the paragraph, and before any page break occurs. If there is insufficient space remaining on the current page to accommodate this number of lines, then a page break is forced <i>before</i> the first line of the paragraph is printed. </p>
<p> Similarly, when a section heading (see subsection &#8220;Headings&#8221; below) precedes any of these paragraph types, the <code>HORPHANS</code> document control register specifies the <i>minimum</i> number of lines of the paragraph which must be kept on the same page as the heading. If insufficient space remains on the current page to accommodate the heading and this number of lines of paragraph text, then a page break is forced <i>before</i> the heading is printed.</p>
<h3>Headings</h3>
<p>Use headings to create a hierarchical structure for your document. By default, the <i>ms</i> macros print headings in <code>bold</code> using the same font family and point size as the body text. For output devices which support scalable fonts, this behaviour may be modified by defining the document control registers <code>GROWPS</code> and <code>PSINCR</code>. </p>
<p> The following heading macros are available:</p>
<dl>
<dt><code>.NH&nbsp;</code><i>xx</i></p>
<dd>Numbered heading. The argument <i>xx</i> is either a numeric argument to indicate the level of the heading, or <code>S~</code><i>xx~xx~</i>&#8230; to set the section number explicitly. If you specify heading levels out of sequence, such as invoking <code>.NH 3</code> after <code>.NH 1</code>, <i>groff</i> prints a warning on standard error.</p>
<dd>If the <code>GROWPS</code> register is set to a value greater than the level of the heading, then the point size of the heading will be increased by <code>PSINCR</code> units over the text size specified by the <code>PS</code> register, for each level by which the heading level is less than the value of <code>GROWPS</code>. For example, the sequence:</p>
<dl>
<dd>
<pre><dl><dt><dd>.nr PS 10
.nr GROWPS 3
.nr PSINCR 1.5p
.
.NH 1
Top Level Heading
.
.NH 2
Second Level Heading
.
.NH 3
Third Level Heading</pre>
</dl>
</dl>
<dd>will cause &#8220;<i>1. Top Level Heading</i>&#8221; to be printed in 13pt <code>bold</code> text, followed by &#8220;<i>1.1. Second Level Heading</i>&#8221; in 11.5pt <code>bold</code> text, while &#8220;<i>1.1.1. Third Level Heading</i>&#8221;, and all more deeply nested heading levels, will remain in the 10pt <code>bold</code> text which is specified by the <code>PS</code> register.</p>
<dd>Note that the value stored in <code>PSINCR</code> is interpreted in <i>groff</i> basic units; the <i>p</i> scaling factor should be employed when assigning a value specified in points.</p>
<dd>The style used to represent the section number, within a numbered heading, is controlled by the <code>SN-STYLE</code> string; this may be set to either the <code>SN-DOT</code> or the <code>SN-NO-DOT</code> style, (described below), by aliasing <code>SN-STYLE</code> accordingly. By default, <code>SN-STYLE</code> is initialised by defining the alias</p>
<dl>
<dd>
<pre><dl><dt><dd>.als SN-STYLE SN-DOT</pre>
</dl>
</dl>
<dd>it may be changed to the <code>SN-NO-DOT</code> style, if preferred, by defining the alternative alias</p>
<dl>
<dd>
<pre><dl><dt><dd>.als SN-STYLE SN-NO-DOT</pre>
</dl>
</dl>
<dd>Any such change becomes effective with the first use of <code>.NH</code>, <i>after</i> the new alias is defined.</p>
<dd>After invoking <code>.NH</code>, the assigned heading number is available in the strings <code>SN-DOT</code> (as it appears in the default formatting style for numbered headings, with a terminating period following the number), and <code>SN-NO-DOT</code> (with this terminating period omitted). The string <code>SN</code> is also defined, as an alias for <code>SN-DOT</code>; if preferred, the user may redefine it as an alias for <code>SN-NO-DOT</code>, by including the initialisation:</p>
<dl>
<dd>
<pre><dl><dt><dd>.als SN SN-NO-DOT</pre>
</dl>
</dl>
<dd>at any time; the change becomes effective with the next use of <code>.NH</code>, <i>after</i> the new alias is defined.</p>
<dt><code>.SH</code></p>
<dd>[<i>xx</i>] Unnumbered subheading. The use of the optional <i>xx</i> argument is a GNU extension, which adjusts the point size of the unnumbered subheading to match that of a numbered heading, introduced using <code>.NH&nbsp;</code><i>xx</i> with the same value of <i>xx</i>. For example, given the same settings for <code>PS</code>, <code>GROWPS</code> and <code>PSINCR</code>, as used in the preceding <code>.NH</code> example, the sequence:</p>
<dl>
<dd>
<pre><dl><dt><dd>.SH 2
An Unnumbered Subheading</pre>
</dl>
</dl>
<dd>will print &#8220;<i>An Unnumbered Subheading</i>&#8221; in 11.5pt <code>bold</code> text.</dl>
<h3>Highlighting</h3>
<p>The <i>ms</i> macros provide a variety of methods to highlight or emphasize text:</p>
<dl>
<dt><code>.B</code></p>
<dd>[<i>txt</i> [<i>post</i> [<i>pre</i>]]] Sets its first argument in <code>bold type</code>. If you specify a second argument, <i>groff</i> prints it in the previous font after the bold text, with no intervening space (this allows you to set punctuation after the highlighted text without highlighting the punctuation). Similarly, it prints the third argument (if any) in the previous font <code>before</code> the first argument. For example,</p>
<dl>
<dd>
<dl>
<dd>.B foo ) (</dl>
</dl>
<dd>prints &#8220;(<code>foo</code>)&#8221;.</p>
<dd>If you give this macro no arguments, <i>groff</i> prints all text following in bold until the next highlighting, paragraph, or heading macro.</p>
<dt><code>.R</code></p>
<dd>[<i>txt</i> [<i>post</i> [<i>pre</i>]]] Sets its first argument in roman (or regular) type. It operates similarly to the <code>B</code> macro otherwise.</p>
<dt><code>.I</code></p>
<dd>[<i>txt</i> [<i>post</i> [<i>pre</i>]]] Sets its first argument in <i>italic type</i>. It operates similarly to the <code>B</code> macro otherwise.</p>
<dt><code>.CW</code></p>
<dd>[<i>txt</i> [<i>post</i> [<i>pre</i>]]] Sets its first argument in a constant-width face. It operates similarly to the <code>B</code> macro otherwise.</p>
<dt><code>.BI</code></p>
<dd>[<i>txt</i> [<i>post</i> [<i>pre</i>]]] Sets its first argument in bold italic type. It operates similarly to the <code>B</code> macro otherwise.</p>
<dt><code>.BX</code></p>
<dd>[<i>txt</i>] Prints its argument and draws a box around it. If you want to box a string that contains spaces, use a digit-width space (
