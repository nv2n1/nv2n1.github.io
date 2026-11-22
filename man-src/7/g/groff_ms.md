---

title: "groff_ms(7)"
name: "groff_ms"
section: "7"
letter: "g"
url: "/docs/linux/man/7-groff_ms/"
description: "groff_ms – GNU roff manuscript macro package for formatting documents"
---

<p>groff_ms &#8211; GNU roff manuscript macro package for formatting documents </p>

<p> [<i>option</i> ...] [<i>input-file</i> ...] [<i>option</i> ...] [<i>input-file</i> ...]  </p>
<h2>DESCRIPTION</h2>
<p> This manual page describes the GNU version of the <i>ms</i> macros, part of the <i>groff</i> typesetting system. The <i>ms</i> macros are mostly compatible with the documented behavior of the 4.3 BSD Unix <i>ms</i> macros (see <i>Differences from troff ms</i> below for details). The <i>ms</i> macros are suitable for reports, letters, books, and technical documentation.  </p>
<h2>USAGE</h2>
<p> The <i>ms</i> macro package expects files to have a certain amount of structure. The simplest documents can begin with a paragraph macro and consist of text separated by paragraph macros or even blank lines. Longer documents have a structure as follows: </p>
<dl>
<dt><code>Document type</code></dt>
<dd> <p> If you use the <code>RP</code> (report) macro at the beginning of the document, <i>groff</i> prints the cover page information on its own page; otherwise it prints the information on the first page with your document text immediately following. Other document formats found in AT&amp;T <i>troff</i> are specific to AT&amp;T or Berkeley, and are not supported in <i>groff ms</i>. </p>
 </dd>
<dt><code>Format and layout</code></dt>
<dd> <p> By setting number registers, you can change your document&#8217;s margins, spacing, headers and footers, footnotes, and the base point size for the text. See <i>Document control registers</i> below for more details. </p>
 </dd>
<dt><code>Cover page</code></dt>
<dd> <p> A cover page consists of a title, and optionally the author&#8217;s name and institution, an abstract, and the date. See <i>Cover page macros</i> below for more details. </p>
 </dd>
<dt><code>Body</code></dt>
<dd> <p> Following the cover page is your document. It consists of paragraphs, headings, and lists. </p>
 </dd>
<dt><code>Table of contents</code></dt>
<dd> <p> Longer documents usually include a table of contents, which you can add by placing the <code>TC</code> macro at the end of your document. </p>
 </dd></dl>
<h3>Document control registers</h3>
<p> The following table lists the document control number registers. For the sake of consistency, set registers related to margins at the beginning of your document, or just after the <code>RP</code> macro. </p>
<p> <code>Margin settings</code> </p>
<dl>
<dd> <table>
<tr VALIGN=top>
<td><code>Reg.</code></td>
<td><code>Definition</code></td>
<td><code>Effective</code></td>
<td><code>Default</code>
</td>
</tr>
<tr VALIGN=top>
<td><hr />
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
<td><hr />
</td>
</tr>
</table>
 </dd></dl>
<p> <code>Text settings</code> </p>
<dl>
<dd> <table>
<tr VALIGN=top>
<td><code>Reg.</code></td>
<td><code>Definition</code></td>
<td><code>Effective</code></td>
<td><code>Default</code>
</td>
</tr>
<tr VALIGN=top>
<td><hr />
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
<td><hr />
</td>
</tr>
</table>
 </dd></dl>
<p> <code>Paragraph settings</code> </p>
<dl>
<dd> <table>
<tr VALIGN=top>
<td><code>Reg.</code></td>
<td><code>Definition</code></td>
<td><code>Effective</code></td>
<td><code>Default</code>
</td>
</tr>
<tr VALIGN=top>
<td><hr />
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
<td><hr />
</td>
</tr>
</table>
 </dd></dl>
<p> <code>Footnote settings</code> </p>
<dl>
<dd> <table>
<tr VALIGN=top>
<td><code>Reg.</code></td>
<td><code>Definition</code></td>
<td><code>Effective</code></td>
<td><code>Default</code>
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>FL</td>
<td>Footnote length</td>
<td>next footnote</td>
<td>\n[LL]*5/6
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
<td>\n[PS]-2
</td>
</tr>
<tr VALIGN=top>
<td>FVS</td>
<td>Vert. spacing</td>
<td>next footnote</td>
<td>\n[FPS]+2
</td>
</tr>
<tr VALIGN=top>
<td>FPD</td>
<td>Para. spacing</td>
<td>next footnote</td>
<td>\n[PD]/2
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
</table>
 </dd></dl>
<p> <code>Other settings</code> </p>
<dl>
<dd> <table>
<tr VALIGN=top>
<td><code>Reg.</code></td>
<td><code>Definition</code></td>
<td><code>Effective</code></td>
<td><code>Default</code>
</td>
</tr>
<tr VALIGN=top>
<td><hr />
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
<td><hr />
</td>
</tr>
</table>
 </dd></dl>
<h3>Cover page macros</h3>
<p> Use the following macros to create a cover page for your document in the order shown. </p>
<dl>
<dt><code>.RP </code>[<code>no</code>] </dt>
<dd> <p> Specifies the report format for your document. The report format creates a separate cover page. With no <code>RP</code> macro, <i>groff</i> prints a subset of the cover page on page~1 of your document. </p>
 </dd>
<dd> <p> If you use the optional <code>no</code> argument, <i>groff</i> prints a title page but does not repeat any of the title page information (title, author, abstract, etc.) on page~1 of the document. </p>
 </dd>
<dt><code>.P1</code></dt>
<dd> <p> (P-one) Prints the header on page~1. The default is to suppress the header. </p>
 </dd>
<dt><code>.DA</code></dt>
<dd> <p> [<i>xxx</i>] (optional) Print the current date, or the arguments to the macro if any, on the title page (if specified) and in the footers. This is the default for <i>nroff</i>. </p>
 </dd>
<dt><code>.ND</code></dt>
<dd> <p> [<i>xxx</i>] (optional) Print the current date, or the arguments to the macro if any, on the title page (if specified) but not in the footers. This is the default for <i>troff</i>. </p>
 </dd>
<dt><code>.TL</code></dt>
<dd> <p> Specifies the document title. <i>Groff</i> collects text following the <code>TL</code> macro into the title, until reaching the author name or abstract. </p>
 </dd>
<dt><code>.AU</code></dt>
<dd> <p> Specifies the author&#8217;s name. You can specify multiple authors by using an <code>AU</code> macro for each author. </p>
 </dd>
<dt><code>.AI</code></dt>
<dd> <p> Specifies the author&#8217;s institution. You can specify multiple institutions. </p>
 </dd>
<dt><code>.AB </code>[<code>no</code>] </dt>
<dd> <p> Begins the abstract. The default is to print the word <code>ABSTRACT</code>, centered and in italics, above the text of the abstract. The option <code>no</code> suppresses this heading. </p>
 </dd>
<dt><code>.AE</code></dt>
<dd> <p> End the abstract. </p>
 </dd></dl>
<h3>Paragraphs</h3>
<p> Use the <code>PP</code> macro to create indented paragraphs, and the <code>LP</code> macro to create paragraphs with no initial indent. </p>
<p>The <code>QP</code> macro indents all text at both left and right margins by the amount of the register <code>QI</code>. The effect is reminiscent of the HTML <code>&lt;BLOCKQUOTE&gt;</code> tag. The next paragraph or heading returns the margins to normal. <code>QP</code> inserts the vertical space specified in register <code>PD</code> as inter-paragraph spacing. </p>
<p>A paragraph bracketed between the macros <code>QS</code> and <code>QE</code> has the same appearance as a paragraph started with <code>QP</code> and a following paragraph started with <code>LP</code>. Both <code>QS</code> and <code>QE</code> insert the inter-paragraph spacing specified in <code>PD</code> and the text is indented on both sides by the amount of register <code>QI</code>. The text between <code>QS</code> and <code>QE</code> can be split into further paragraphs by using <code>.LP</code> or <code>.PP</code>. </p>
<p>The <code>XP</code> macro produces an "exdented" paragraph; that is, one with a hanging indent. The first line of the paragraph begins at the left margin, and subsequent lines are indented (the opposite of <code>PP</code>). </p>
<p>For each of the above paragraph types, and also for any list entry introduced by the <code>IP</code> macro (described later), the document control register <code>PORPHANS</code>, sets the <i>minimum</i> number of lines which must be printed, after the start of the paragraph, and before any page break occurs. If there is insufficient space remaining on the current page to accommodate this number of lines, then a page break is forced <i>before</i> the first line of the paragraph is printed. </p>
<p>Similarly, when a section heading (see subsection "Headings" below) precedes any of these paragraph types, the <code>HORPHANS</code> document control register specifies the <i>minimum</i> number of lines of the paragraph which must be kept on the same page as the heading. If insufficient space remains on the current page to accommodate the heading and this number of lines of paragraph text, then a page break is forced <i>before</i> the heading is printed.  </p>
<h3>Headings</h3>
<p> Use headings to create a hierarchical structure for your document. By default, the <i>ms</i> macros print headings in <code>bold</code> using the same font family and point size as the body text. For output devices which support scalable fonts, this behaviour may be modified by defining the document control registers <code>GROWPS</code> and <code>PSINCR</code>. </p>
<p>The following heading macros are available: </p>
<dl>
<dt><code>.NH&nbsp;</code><i>xx</i></dt>
<dd> <p> Numbered heading. The argument <i>xx</i> is either a numeric argument to indicate the level of the heading, or <code>S~</code><i>xx~xx~</i>... to set the section number explicitly. If you specify heading levels out of sequence, such as invoking <code>.NH 3</code> after <code>.NH 1</code>, <i>groff</i> prints a warning on standard error. </p>
 </dd>
<dd> <p> If the <code>GROWPS</code> register is set to a value greater than the level of the heading, then the point size of the heading will be increased by <code>PSINCR</code> units over the text size specified by the <code>PS</code> register, for each level by which the heading level is less than the value of <code>GROWPS</code>. For example, the sequence: </p>
 </dd>
<dl>
<dd> <pre><code>
 </dd>
<dl>

<dd> .nr PS 10
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
Third Level Heading
</code></pre>
 </dd></dl>
</dl>
<dd> <p> will cause ``<i>1. Top Level Heading</i>&#8216;&#8216; to be printed in 13pt <code>bold</code> text, followed by ``<i>1.1. Second Level Heading</i>&#8216;&#8216; in 11.5pt <code>bold</code> text, while ``<i>1.1.1. Third Level Heading</i>&#8216;&#8216;, and all more deeply nested heading levels, will remain in the 10pt <code>bold</code> text which is specified by the <code>PS</code> register. </p>
 </dd>
<dd> <p> Note that the value stored in <code>PSINCR</code> is interpreted in <i>groff</i> basic units; the <i>p</i> scaling factor should be employed when assigning a value specified in points. </p>
 </dd>
<dd> <p> The style used to represent the section number, within a numbered heading, is controlled by the <code>SN-STYLE</code> string; this may be set to either the <code>SN-DOT</code> or the <code>SN-NO-DOT</code> style, (described below), by aliasing <code>SN-STYLE</code> accordingly. By default, <code>SN-STYLE</code> is initialised by defining the alias </p>
 </dd>
<dl>
<dd> <pre><code>
 </dd>
<dl>

<dd> .als SN-STYLE SN-DOT
</code></pre>
 </dd></dl>
</dl>
<dd> <p> it may be changed to the <code>SN-NO-DOT</code> style, if preferred, by defining the alternative alias </p>
 </dd>
<dl>
<dd> <pre><code>
 </dd>
<dl>

<dd> .als SN-STYLE SN-NO-DOT
</code></pre>
 </dd></dl>
</dl>
<dd> <p> Any such change becomes effective with the first use of <code>.NH</code>, <i>after</i> the new alias is defined. </p>
 </dd>
<dd> <p> After invoking <code>.NH</code>, the assigned heading number is available in the strings <code>SN-DOT</code> (as it appears in the default formatting style for numbered headings, with a terminating period following the number), and <code>SN-NO-DOT</code> (with this terminating period omitted). The string <code>SN</code> is also defined, as an alias for <code>SN-DOT</code>; if preferred, the user may redefine it as an alias for <code>SN-NO-DOT</code>, by including the initialisation: </p>
 </dd>
<dl>
<dd> <pre><code>
 </dd>
<dl>

<dd> .als SN SN-NO-DOT
</code></pre>
 </dd></dl>
</dl>
<dd> <p> at any time; the change becomes effective with the next use of <code>.NH</code>, <i>after</i> the new alias is defined. </p>
 </dd>
<dt><code>.SH</code></dt>
<dd> <p> [<i>xx</i>] Unnumbered subheading. The use of the optional <i>xx</i> argument is a GNU extension, which adjusts the point size of the unnumbered subheading to match that of a numbered heading, introduced using <code>.NH&nbsp;</code><i>xx</i> with the same value of <i>xx</i>. For example, given the same settings for <code>PS</code>, <code>GROWPS</code> and <code>PSINCR</code>, as used in the preceding <code>.NH</code> example, the sequence: </p>
 </dd>
<dl>
<dd> <pre><code>
 </dd>
<dl>

<dd> .SH 2
An Unnumbered Subheading
</code></pre>
 </dd></dl>
</dl>
<dd> <p> will print ``<i>An Unnumbered Subheading</i>&#8216;&#8216; in 11.5pt <code>bold</code> text. </p>
 </dd></dl>
<h3>Highlighting</h3>
<p> The <i>ms</i> macros provide a variety of methods to highlight or emphasize text: </p>
<dl>
<dt><code>.B</code></dt>
<dd> <p> [<i>txt</i> [<i>post</i> [<i>pre</i>]]] Sets its first argument in <code>bold type</code>. If you specify a second argument, <i>groff</i> prints it in the previous font after the bold text, with no intervening space (this allows you to set punctuation after the highlighted text without highlighting the punctuation). Similarly, it prints the third argument (if any) in the previous font <code>before</code> the first argument. For example, </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> .B foo ) ( </p>
 </dd></dl>
</dl>
<dd> <p> prints "(<code>foo</code>)". </p>
 </dd>
<dd> <p> If you give this macro no arguments, <i>groff</i> prints all text following in bold until the next highlighting, paragraph, or heading macro. </p>
 </dd>
<dt><code>.R</code></dt>
<dd> <p> [<i>txt</i> [<i>post</i> [<i>pre</i>]]] Sets its first argument in roman (or regular) type. It operates similarly to the <code>B</code> macro otherwise. </p>
 </dd>
<dt><code>.I</code></dt>
<dd> <p> [<i>txt</i> [<i>post</i> [<i>pre</i>]]] Sets its first argument in <i>italic type</i>. It operates similarly to the <code>B</code> macro otherwise. </p>
 </dd>
<dt><code>.CW</code></dt>
<dd> <p> [<i>txt</i> [<i>post</i> [<i>pre</i>]]] Sets its first argument in a constant-width face. It operates similarly to the <code>B</code> macro otherwise. </p>
 </dd>
<dt><code>.BI</code></dt>
<dd> <p> [<i>txt</i> [<i>post</i> [<i>pre</i>]]] Sets its first argument in bold italic type. It operates similarly to the <code>B</code> macro otherwise. </p>
 </dd>
<dt><code>.BX</code></dt>
<dd> <p> [<i>txt</i>] Prints its argument and draws a box around it. If you want to box a string that contains spaces, use a digit-width space (\0). </p>
 </dd>
<dt><code>.UL</code></dt>
<dd> <p> [<i>txt</i> [<i>post</i>]] Prints its first argument with an underline. If you specify a second argument, <i>groff</i> prints it in the previous font after the underlined text, with no intervening space. </p>
 </dd>
<dt><code>.LG</code></dt>
<dd> <p> Prints all text following in larger type (2~points larger than the current point size) until the next font size, highlighting, paragraph, or heading macro. You can specify this macro multiple times to enlarge the point size as needed. </p>
 </dd>
<dt><code>.SM</code></dt>
<dd> <p> Prints all text following in smaller type (2~points smaller than the current point size) until the next type size, highlighting, paragraph, or heading macro. You can specify this macro multiple times to reduce the point size as needed. </p>
 </dd>
<dt><code>.NL</code></dt>
<dd> <p> Prints all text following in the normal point size (that is, the value of the <code>PS</code> register). </p>
 </dd>
<dt><code>\*{</code><i>text</i><code>\*}</code></dt>
<dd> <p> Print the enclosed <i>text</i> as a superscript. </p>
 </dd></dl>
<h3>Indents</h3>
<p> You may need to indent sections of text. A typical use for indents is to create nested lists and sublists. </p>
<p>Use the <code>RS</code> and <code>RE</code> macros to start and end a section of indented text, respectively. The <code>PI</code> register controls the amount of indent. </p>
<p>You can nest indented sections as deeply as needed by using multiple, nested pairs of <code>RS</code> and <code>RE</code>.  </p>
<h3>Lists</h3>
<p> The <code>IP</code> macro handles duties for all lists. Its syntax is as follows: </p>
<dl>
<dt><code>.IP</code></dt>
<dd> <p> [<i>marker</i> [<i>width</i>]] The <i>marker</i> is usually a bullet character <code>\(bu</code> for unordered lists, a number (or auto-incrementing number register) for numbered lists, or a word or phrase for indented (glossary-style) lists. </p>
 </dd>
<dd> <p> The <i>width</i> specifies the indent for the body of each list item. Once specified, the indent remains the same for all list items in the document until specified again. <br/>
 </p>
 </dd></dl>
<h3>Tab stops</h3>
<p> Use the <code>ta</code> request to set tab stops as needed. Use the <code>TA</code> macro to reset tabs to the default (every 5n). You can redefine the <code>TA</code> macro to create a different set of default tab stops.  </p>
<h3>Displays and keeps</h3>
<p> Use displays to show text-based examples or figures (such as code listings). Displays turn off filling, so lines of code can be displayed as-is without inserting <code>br</code> requests in between each line. Displays can be <i>kept</i> on a single page, or allowed to break across pages. The following table shows the display types available. </p>
<dl>
<dd> <table>
<tr VALIGN=top>
<td><code>Display macro</code></td>
<td><code>Type of display</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>With keep</code></td>
<td><code>No keep</code></td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>.DS L</td>
<td>.LD</td>
<td>Left-justified.
</td>
</tr>
<tr VALIGN=top>
<td>.DS I [,<i>indent/</i>]</td>
<td>.ID</td>
<td> Indented (default indent in the <code>DI</code> register). 
</td>
</tr>
<tr VALIGN=top>
<td>.DS B</td>
<td>.BD</td>
<td> Block-centered (left-justified, longest line centered). 
</td>
</tr>
<tr VALIGN=top>
<td>.DS C</td>
<td>.CD</td>
<td>Centered.
</td>
</tr>
<tr VALIGN=top>
<td>.DS R</td>
<td>.RD</td>
<td>Right-justified.
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
</table>
 </dd></dl>
<p>Use the <code>DE</code> macro to end any display type. The macros <code>Ds</code> and <code>De</code> were formerly provided as aliases for <code>DS</code> and <code>DE</code>, respectively, but they have been removed, and should no longer be used. X11 documents which actually use <code>Ds</code> and <code>De</code> always load a specific macro file from the X11 distribution (<i>macros.t</i>) which provides proper definitions for the two macros. </p>
<p>To <i>keep</i> text together on a page, such as a paragraph that refers to a table (or list, or other item) immediately following, use the <code>KS</code> and <code>KE</code> macros. The <code>KS</code> macro begins a block of text to be kept on a single page, and the <code>KE</code> macro ends the block. </p>
<p>You can specify a <i>floating keep</i> using the <code>KF</code> and <code>KE</code> macros. If the keep cannot fit on the current page, <i>groff</i> holds the contents of the keep and allows text following the keep (in the source file) to fill in the remainder of the current page. When the page breaks, whether by an explicit <code>bp</code> request or by reaching the end of the page, <i>groff</i> prints the floating keep at the top of the new page. This is useful for printing large graphics or tables that do not need to appear exactly where specified. </p>
<p>The macros <code>B1</code> and <code>B2</code> can be used to enclose a text within a box; <code>.B1</code> begins the box, and <code>.B2</code> ends it. Text in the box is automatically placed in a diversion (keep).  </p>
<h3>Tables, figures, equations, and references</h3>
<p> The <i>ms</i> macros support the standard <i>groff</i> preprocessors: <i>tbl</i>, <i>pic</i>, <i>eqn</i>, and <i>refer</i>. Mark text meant for preprocessors by enclosing it in pairs of tags as follows: </p>
<dl>
<dt><code>.TS</code> [<code>H</code>] and <code>.TE</code></dt>
<dd> <p> Denote a table to be processed by the <i>tbl</i> preprocessor. The optional <code>H</code>~argument instructs <i>groff</i> to create a running header with the information up to the <code>TH</code> macro. <i>Groff</i> prints the header at the beginning of the table; if the table runs onto another page, <i>groff</i> prints the header on the next page as well. </p>
 </dd>
<dt><code>.PS</code> and <code>.PE</code></dt>
<dd> <p> Denote a graphic to be processed by the <i>pic</i> preprocessor. You can create a <i>pic</i> file by hand, using the AT&amp;T <i>pic</i> manual available on the Web as a reference, or by using a graphics program such as <i>xfig</i>. </p>
 </dd>
<dt><code>.EQ</code></dt>
<dd> <p> [<i>align</i>] and <code>.EN</code> Denote an equation to be processed by the <i>eqn</i> preprocessor. The optional <i>align</i> argument can be <code>C</code>, <code>L</code>, or~<code>I</code> to center (the default), left-justify, or indent the equation, respectively. </p>
 </dd>
<dt><code>.[</code> and <code>.]</code></dt>
<dd> <p> Denote a reference to be processed by the <i>refer</i> preprocessor. The GNU <i><a href="/docs/linux/man/1-refer/">refer</a></i>(1) manual page provides a comprehensive reference to the preprocessor and the format of the bibliographic database. </p>
 </dd></dl>
<h3>Footnotes</h3>
<p> The <i>ms</i> macros provide a flexible footnote system. You can specify a numbered footnote by using the <code>\**</code> escape, followed by the text of the footnote enclosed by <code>FS</code> and <code>FE</code> macros. </p>
<p>You can specify symbolic footnotes by placing the mark character (such as <code>\(dg</code> for the dagger character) in the body text, followed by the text of the footnote enclosed by <code>FS&nbsp;\(dg</code> and <code>FE</code> macros. </p>
<p>You can control how <i>groff</i> prints footnote numbers by changing the value of the <code>FF</code> register as follows: </p>
<dl>
<dd>  </dd>
<dl>
<dt>0</dt>
<dd> <p> Prints the footnote number as a superscript; indents the footnote (default). </p>
 </dd>
<dt>1</dt>
<dd> <p> Prints the number followed by a period (that is,~"1.") and indents the footnote. </p>
 </dd>
<dt>2</dt>
<dd> <p> Like~1, without an indent. </p>
 </dd>
<dt>3</dt>
<dd> <p> Like~1, but prints the footnote number as a paragraph with a hanging indent. </p>
 </dd></dl>
</dl>
<p>You can use footnotes safely within keeps and displays, but avoid using numbered footnotes within floating keeps. You can set a second <code>\**</code> between a <code>\**</code> and its corresponding <code>.FS</code>; as long as each <code>.FS</code> occurs <i>after</i> the corresponding <code>\**</code> and the occurrences of <code>.FS</code> are in the same order as the corresponding occurrences of <code>\**</code>.  </p>
<h3>Headers and footers</h3>
<p> There are three ways to define headers and footers: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Use the strings <code>LH</code>, <code>CH</code>, and <code>RH</code> to set the left, center, and right headers. Use <code>LF</code>, <code>CF</code>, and <code>RF</code> to set the left, center, and right footers. The string-setting approach works best for documents that do not distinguish between odd and even pages. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Use the <code>OH</code> and <code>EH</code> macros to define headers for the odd and even pages, and <code>OF</code> and <code>EF</code> macros to define footers for the odd and even pages. This is more flexible than defining the individual strings. The syntax for these macros is as follows: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <code>.</code><i>XX</i><code> &#8216;</code><i>left</i><code>&#8216;</code><i>center</i><code>&#8216;</code><i>right</i><code>&#8216;</code> </p>
 </dd></dl>
</dl>
<dd> <p> where <i>XX</i> is one of the foregoing four macros and each of <i>left</i>, <i>center</i>, and <i>right</i> is text of your choice. You can replace the quote (&#8216;) marks with any character not appearing in the header or footer text. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> You can redefine the <code>PT</code> and <code>BT</code> macros to change the behavior of the header and footer, respectively. The header process also calls the (undefined) <code>HD</code> macro after <code>PT</code>; you can define this macro if you need additional processing after printing the header (for example, to draw a line below the header). </p>
 </dd></dl>
<h3>Margins</h3>
<p> You control margins using a set of number registers. The following table lists the register names and defaults: </p>
<dl>
<dd> <table>
<tr VALIGN=top>
<td><code>Reg.</code></td>
<td><code>Definition</code></td>
<td><code>Effective</code></td>
<td><code>Default</code>
</td>
</tr>
<tr VALIGN=top>
<td><hr />
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
<td><hr />
</td>
</tr>
</table>
 </dd></dl>
<p>Note that there is no right margin setting. The combination of page offset and line length provide the information necessary to derive the right margin.  </p>
<h3>Multiple columns</h3>
<p> The <i>ms</i> macros can set text in as many columns as will reasonably fit on the page. The following macros are available. All of them force a page break if a multi-column mode is already set. However, if the current mode is single-column, starting a multi-column mode does <i>not</i> force a page break. </p>
<dl>
<dt><code>.1C</code></dt>
<dd> <p> Single-column mode. </p>
 </dd>
<dt><code>.2C</code></dt>
<dd> <p> Two-column mode. </p>
 </dd>
<dt><code>.MC</code></dt>
<dd> <p> [<i>column-width</i> [<i>gutter-width</i>]] Multi-column mode. If you specify no arguments, it is equivalent to the <code>2C</code> macro. Otherwise, <i>column-width</i> is the width of each column and <i>gutter-width</i> is the space between columns. The <code>MINGW</code> number register is the default gutter width. </p>
 </dd></dl>
<h3>Creating a table of contents</h3>
<p> Wrap text that you want to appear in the table of contents in <code>XS</code> and <code>XE</code> macros. Use the <code>TC</code> macro to print the table of contents at the end of the document, resetting the page number to~<code>i</code> (Roman numeral~1). </p>
<p>You can manually create a table of contents by specifying a page number as the first argument to <code>XS</code>. Add subsequent entries using the <code>XA</code> macro. For example: </p>
<dl>
<dd> <pre><code>.XS 1
Introduction
.XA 2
A Brief History of the Universe
.XA 729
Details of Galactic Formation
...
.XE
</code></pre>
 </dd></dl>
<p>Use the <code>PX</code> macro to print a manually-generated table of contents without resetting the page number. </p>
<p>If you give the argument <code>no</code> to either <code>PX</code> or <code>TC</code>, <i>groff</i> suppresses printing the title specified by the <code>\*[TOC]</code> string.  </p>
<h3>Fractional point sizes</h3>
<p> Traditionally, the <i>ms</i> macros only support integer values for the document&#8217;s font size and vertical spacing. To overcome this restriction, values larger than or equal to 1000 are taken as fractional values, multiplied by 1000. For example, &#8216;.nr~PS~10250&#8217; sets the font size to 10.25 points. </p>
<p>The following four registers accept fractional point sizes: <code>PS</code>, <code>VS</code>, <code>FPS</code>, and <code>FVS</code>. </p>
<p>Due to backwards compatibility, the value of <code>VS</code> must be smaller than 40000 (this is 40.0 points).  </p>
<h2>DIFFERENCES FROM troff ms</h2>
<p> The <i>groff ms</i> macros are a complete re-implementation, using no original AT&amp;T code. Since they take advantage of the extended features in <i>groff</i>, they cannot be used with AT&amp;T <i>troff</i>. Other differences include: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The internals of <i>groff ms</i> differ from the internals of Unix <i>ms</i>. Documents that depend upon implementation details of Unix <i>ms</i> may not format properly with <i>groff ms</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The error-handling policy of <i>groff ms</i> is to detect and report errors, rather than silently to ignore them. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some Bell Labs localisms are not implemented by default. However, if you call the otherwise undocumented <code>SC</code> section-header macro, you will enable implementations of three other archaic Bell Labs macros: <code>UC</code>, <code>P1</code>, and <code>P2</code>. These are not enabled by default because (a)~they were not documented, in the original <i>ms manual</i>, and (b)~the <code>P1</code> and <code>UC</code> macros both collide with different macros in the Berkeley version of <i>ms</i>. </p>
 </dd>
<dd> <p> These emulations are sufficient to give back the 1976 Kernighan~&amp; Cherry paper <i>Typesetting Mathematics - User&#8217;s Guide</i> its section headings, and restore some text that had gone missing as arguments of undefined macros. No warranty express or implied is given as to how well the typographic details these produce match the original Bell Labs macros. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Berkeley localisms, in particular the <code>TM</code> and <code>CT</code> macros, are not implemented. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>Groff ms</i> does not work in compatibility mode (e.g., with the <code>-C</code> option). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> There is no support for typewriter-like devices. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>Groff ms</i> does not provide cut marks. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Multiple line spacing is not supported (use a larger vertical spacing instead). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some Unix <i>ms</i> documentation says that the <code>CW</code> and <code>GW</code> number registers can be used to control the column width and gutter width, respectively. These number registers are not used in <i>groff ms</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Macros that cause a reset (paragraphs, headings, etc.) may change the indent. Macros that change the indent do not increment or decrement the indent, but rather set it absolutely. This can cause problems for documents that define additional macros of their own. The solution is to use not the <code>in</code> request but instead the <code>RS</code> and <code>RE</code> macros. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The number register <code>GS</code> is set to~1 by the <i>groff ms</i> macros, but is not used by the Unix <i>ms</i> macros. Documents that need to determine whether they are being formatted with Unix <i>ms</i> or <i>groff ms</i> should use this number register. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> To make <i>groff ms</i> use the default page offset (which also specifies the left margin), the <code>PO</code> number register must stay undefined until the first <code>ms</code> macro is evaluated. This implies that <code>PO</code> should not be used early in the document, unless it is changed also: remember that accessing an undefined register automatically defines it. <br/>
 </p>
 </dd></dl>
<h3>Strings</h3>
<p> You can redefine the following strings to adapt the <i>groff ms</i> macros to languages other than English: </p>
<dl>
<dd> <table>
<tr VALIGN=top>
<td><code>String</code></td>
<td><code>Default Value</code>
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>REFERENCES</td>
<td>References
</td>
</tr>
<tr VALIGN=top>
<td>ABSTRACT</td>
<td>ABSTRACT
</td>
</tr>
<tr VALIGN=top>
<td>TOC</td>
<td>Table of Contents
</td>
</tr>
<tr VALIGN=top>
<td>MONTH1</td>
<td>January
</td>
</tr>
<tr VALIGN=top>
<td>MONTH2</td>
<td>February
</td>
</tr>
<tr VALIGN=top>
<td>MONTH3</td>
<td>March
</td>
</tr>
<tr VALIGN=top>
<td>MONTH4</td>
<td>April
</td>
</tr>
<tr VALIGN=top>
<td>MONTH5</td>
<td>May
</td>
</tr>
<tr VALIGN=top>
<td>MONTH6</td>
<td>June
</td>
</tr>
<tr VALIGN=top>
<td>MONTH7</td>
<td>July
</td>
</tr>
<tr VALIGN=top>
<td>MONTH8</td>
<td>August
</td>
</tr>
<tr VALIGN=top>
<td>MONTH9</td>
<td>September
</td>
</tr>
<tr VALIGN=top>
<td>MONTH10</td>
<td>October
</td>
</tr>
<tr VALIGN=top>
<td>MONTH11</td>
<td>November
</td>
</tr>
<tr VALIGN=top>
<td>MONTH12</td>
<td>December
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
</table>
 </dd></dl>
<p>The <code>\*-</code> string produces an em dash---like this. </p>
<p>Use <code>\*Q</code> and <code>\*U</code> to get a left and right typographer&#8217;s quote, respectively, in <i>troff</i> (and plain quotes in <i>nroff</i>).  </p>
<h3>Text Settings</h3>
<p> The <code>FAM</code> string sets the default font family. If this string is undefined at initialization, it is set to Times. </p>
<p>The point size, vertical spacing, and inter-paragraph spacing for footnotes are controlled by the number registers <code>FPS</code>, <code>FVS</code>, and <code>FPD</code>; at initialization these are set to <code>\n(PS-2</code>, <code>\n[FPS]+2</code>, and <code>\n(PD/2</code>, respectively. If any of these registers are defined before initialization, the initialization macro does not change them. </p>
<p>The hyphenation flags (as set by the <code>hy</code> request) are set from the <code>HY</code> register; the default is~6. </p>
<p>Improved accent marks (as originally defined in Berkeley&#8217;s <i>ms</i> version) are available by specifying the <code>AM</code> macro at the beginning of your document. You can place an accent over most characters by specifying the string defining the accent directly after the character. For example, <code>n\*~</code> produces an n with a tilde over it.  </p>
<h2>NAMING CONVENTIONS</h2>
<p> The following conventions are used for names of macros, strings, and number registers. External names available to documents that use the <i>groff ms</i> macros contain only uppercase letters and digits. </p>
<p>Internally the macros are divided into modules; naming conventions are as follows: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Names used only within one module are of the form <i>module</i><code>*</code><i>name</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Names used outside the module in which they are defined are of the form <i>module</i><code>@</code><i>name</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Names associated with a particular environment are of the form <i>environment</i><code>:</code><i>name</i>; these are used only within the <code>par</code> module. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>name</i> does not have a module prefix. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Constructed names used to implement arrays are of the form <i>array</i><code>!</code><i>index</i>. </p>
 </dd></dl>
<p>Thus the groff ms macros reserve the following names: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Names containing the characters <code>*</code>, <code>@</code>, and~<code>:</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Names containing only uppercase letters and digits. </p>
 </dd></dl>
<h2>FILES</h2>
<p> <i>/usr/:share/:groff/:1.22.4/:tmac/ms.tmac</i> (a wrapper file for <i>s.tmac</i>) <br/>
 <i>/usr/:share/:groff/:1.22.4/:tmac/s.tmac</i>  </p>
<h2>AUTHORS</h2>
<p> The GNU version of the <i>ms</i> macro package was written by James Clark and contributors. This document was (re-)written by Larry Kollar  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1), <code><a href="/docs/linux/man/1-tbl/">tbl</a></code>(1), <code><a href="/docs/linux/man/1-pic/">pic</a></code>(1), <code><a href="/docs/linux/man/1-eqn/">eqn</a></code>(1), <code><a href="/docs/linux/man/1-refer/">refer</a></code>(1) </p>
<p> <i>Groff: The GNU Implementation of troff</i>, by Trent A. Fisher and Werner Lemberg </p>
