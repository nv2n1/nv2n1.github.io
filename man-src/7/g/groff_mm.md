---
title: "groff_mm(7)"
name: "groff_mm"
section: "7"
letter: "g"
url: "/docs/linux/man/7-groff_mm/"
description: "groff_mm – memorandum macros for GNU roff"
---

<p>groff_mm &#8211; memorandum macros for GNU roff</p>
<h2>Synopsis</h2>
<p>[<i>option</i> &#8230;] [<i>file</i> &#8230;] [<i>option</i> &#8230;] [<i>file</i> &#8230;]</p>
<h2>Description</h2>
<p>The groff mm macros are intended to be compatible with the DWB mm macros with the following limitations:</p>
<dl>
<dt><code>&bull;</code></dt>
<dd>No Bell Labs localisms are implemented.</dd>
<dt><code>&bull;</code></dt>
<dd>The macros OK and PM are not implemented.</dd>
<dt><code>&bull;</code></dt>
<dd>groff mm does not support cut marks.</dd></dl>
<p> <code>mm</code> is intended to support easy localization. Use <code>mmse</code> as an example how to adapt the output format to a national standard. Localized strings are collected in the file <i>/usr/:share/:groff/:1.22.4/:tmac/</i>xx<i>.tmac</i>, where <i>xx</i> denotes the two-letter code for the <i>language</i>, as defined in the ISO 639 standard. For Swedish, this is &#8216;sv.tmac&#8217; &#8211; not &#8216;se&#8217;, which is the ISO 3166 two-letter code for the <i>country</i> (as used for the output format localization). </p>
<p> A file called <i>locale</i> or country<i>_locale</i> is read after the initialization of the global variables. It is therefore possible to localize the macros with a different company name and so on. </p>
<p> In this manual, square brackets are used to show optional arguments.</p>
<h3>Number registers and strings</h3>
<p>Many macros can be controlled by number registers and strings. A number register is assigned with the <code>nr</code> command:</p>
<dl>
<dd><code>.nr&nbsp;</code><i>XXX </i>[<code>&plusmn;</code>]n [i]</dd></dl>
<p> <i>XXX</i> is the name of the register, <i>n</i>~is the value to be assigned, and <i>i</i>~is the increment value for auto-increment. <i>n</i>~can have a plus or minus sign as a prefix if an increment or decrement of the current value is wanted. (Auto-increment or auto-decrement occurs if the number register is used with a plus or minus sign, <code>
+[</code><i>XXX</i><code>]</code> or <code>
-[</code><i>XXX</i><code>]</code>.) </p>
<p> Strings are defined with <code>ds</code>.</p>
<dl>
<dd><code>.ds</code> <i>YYY string</i></dd></dl>
<p> The string is assigned everything to the end of the line, even blanks. Initial blanks in <i>string</i> should be prefixed with a double-quote. (Strings are used in the text as <code>\*[</code><i>YYY</i><code>]</code>.)</p>
<h3>Special formatting of number registers</h3>
<p>A number register is printed with normal digits if no format has been given. Set the format with <code>af</code>:</p>
<dl>
<dd><code>.af&nbsp;</code><i>R c</i></dd></dl>
<p> <i>R</i>~is the name of the register, <i>c</i>~is the format.</p>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>Form</code></td>
<td><code>Sequence</code>
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td>0, 1, 2, 3, &#8230;
</td>
</tr>
<tr VALIGN=top>
<td>001</td>
<td>000, 001, 002, 003, &#8230;
</td>
</tr>
<tr VALIGN=top>
<td>i</td>
<td>0, i, ii, iii, iv, &#8230;
</td>
</tr>
<tr VALIGN=top>
<td>I</td>
<td>0, I, II, III, IV, &#8230;
</td>
</tr>
<tr VALIGN=top>
<td>a</td>
<td>0, a, b, c, &#8230;, z, aa, ab, &#8230;
</td>
</tr>
<tr VALIGN=top>
<td>A</td>
<td>0, A, B, C, &#8230;, Z, AA, AB, &#8230;
</td>
</tr>
</table>
</dd></dl>
<h3>Fonts</h3>
<p>In <code>mm</code>, the fonts (or rather, font styles) <code>R</code>~(normal), <code>I</code>~(italic), and <code>B</code>~(bold) are hardwired to font positions <code>1</code>, <code>2</code>, and~<code>3</code>, respectively. Internally, font positions are used for backwards compatibility. From a practical point of view it doesn&#8217;t make a big difference &#8211; a different font family can still be selected with a call to the <code>.fam</code> request or using <code>groff</code>&#8216;s <code>-f</code> command-line option. On the other hand, if you want to replace just, say, font <code>B</code>, you have to replace the font at position~2 (with a call to &#8216;.fp~2~&#8230;&#8217;).</p>
<h3>Macros</h3>
<dl>
<dt><code>)E&nbsp;</code><i>level text</i></dt>
<dd>Add heading text <i>text</i> to the table of contents with <i>level</i>, which is either~0 or in the range 1 to~7. See also <code>.H</code>. This macro is used for customized tables of contents.</dd>
<dt><code>1C&nbsp;</code>[<code>1</code>]</dt>
<dd>Begin one-column processing. A~<code>1</code> as an argument disables the page break. Use wide footnotes, small footnotes may be overprinted.</dd>
<dt><code>2C</code></dt>
<dd>Begin two-column processing. Splits the page in two columns. It is a special case of <code>MC</code>. See also <code>1C</code>.</dd>
<dt><code>AE</code></dt>
<dd>Abstract end, see <code>AS</code>.</dd>
<dt><code>AF&nbsp;</code>[<i>name-of-firm</i>]</dt>
<dd>Author&#8217;s firm, should be called before <code>AU</code>, see also <code>COVER</code>.</dd>
<dt><code>AL&nbsp;</code><i></i>[type&nbsp;[text-indent&nbsp;[1]]]</dt>
<dd>Start auto-increment list. Items are numbered beginning with one. The <i>type</i> argument controls the format of numbers.</dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>Arg</code></td>
<td><code>Description</code>
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td>Arabic (the default)
</td>
</tr>
<tr VALIGN=top>
<td>A</td>
<td>Upper-case letters (A-Z)
</td>
</tr>
<tr VALIGN=top>
<td>a</td>
<td>Lower-case letters (a-z)
</td>
</tr>
<tr VALIGN=top>
<td>I</td>
<td>Upper-case roman
</td>
</tr>
<tr VALIGN=top>
<td>i</td>
<td>Lower-case roman
</td>
</tr>
</table>
</dd></dl>
</dl>
<dd><i>text-indent</i> sets the indentation and overrides <code>Li</code>. A third argument prohibits printing of a blank line before each item.</dd>
<dt><code>APP&nbsp;</code><i>name text</i></dt>
<dd>Begin an appendix with name <i>name</i>. Automatic naming occurs if <i>name</i> is <code>&quot;&quot;</code>. The appendices start with~<code>A</code> if automatic naming is used. A new page is ejected, and a header is also produced if the number variable <code>Aph</code> is non-zero. This is the default. The appendix always appears in the &#8216;List of contents&#8217; with correct page numbers. The name &#8216;APPENDIX&#8217; can be changed by setting the string <code>App</code> to the desired text. The string <code>Apptxt</code> contains the current appendix text.</dd>
<dt><code>APPSK&nbsp;</code><i>name pages text</i></dt>
<dd>Same as <code>.APP</code>, but the page number is incremented with <i>pages</i>. This is used when diagrams or other non-formatted documents are included as appendices.</dd>
<dt><code>AS&nbsp;</code><i></i>[arg [indent]]</dt>
<dd>Abstract start. Indentation is specified in &#8216;ens&#8217;, but scaling is allowed. Argument <i>arg</i> controls where the abstract is printed.</dd>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code><code>Arg</code></code></td>
<td><code>Placement</code>
</td>
</tr>
<tr VALIGN=top>
<td>0</td>
<td> Abstract is printed on page~1 and on the cover sheet if used in the released-paper style (<code>MT 4</code>), otherwise it is printed on page~1 without a cover sheet.
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td>Abstract is only printed on the cover sheet (<code>MT 4</code> only).
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td> Abstract is printed only on the cover sheet (other than <code>MT 4</code> only). The cover sheet is printed without a need for <code>CS</code>.
</td>
</tr>
</table>
</dd></dl>
<dd>An abstract is not printed at all in external letters (<code>MT 5</code>). The <i>indent</i> parameter controls the indentation of both margins, otherwise normal text indentation is used.</dd>
<dt><code>AST&nbsp;</code><i></i>[title]</dt>
<dd>Abstract title. Default is &#8216;ABSTRACT&#8217;. Sets the text above the abstract text.</dd>
<dt><code>AT&nbsp;</code><i>title1 </i>[title2 [&#8230;]]</dt>
<dd>Author&#8217;s title. <code>AT</code> must appear just after each <code>AU</code>. The title shows up after the name in the signature block.</dd>
<dt><code>AU&nbsp;</code><i></i>[name [initials [loc [dept [ext [room [arg [arg [arg]]]]]]]]]</dt>
<dd>Author information. Specifies the author of the memo or paper, and is printed on the cover sheet and on other similar places. <code>AU</code> must not appear before <code>TL</code>. The author information can contain initials, location, department, telephone extension, room number or name and up to three extra arguments.</dd>
<dt><code>AV&nbsp;</code><i></i>[name&nbsp;[1]]</dt>
<dd>Approval signature. Generates an approval line with place for signature and date. The string &#8216;APPROVED:&#8217; can be changed with variable <code>Letapp</code>; it is replaced with an empty lin if there is a second argument. The string &#8216;Date&#8217; can be changed with variable <code>Letdate</code>.</dd>
<dt><code>AVL&nbsp;</code><i></i>[name]</dt>
<dd>Letter signature. Generates a line with place for signature.</dd>
<dt><code>B&nbsp;</code><i></i>[bold-text [prev-font-text [bold [&#8230;]]]]</dt>
<dd>Begin boldface. No limit on the number of arguments. All arguments are concatenated to one word; the first, third and so on is printed in boldface.</dd>
<dt><code>B1</code></dt>
<dd>Begin box (as the ms macro). Draws a box around the text. The text is indented one character, and the right margin is one character shorter.</dd>
<dt><code>B2</code></dt>
<dd>End box. Finishes the box started with <code>B1</code>.</dd>
<dt><code>BE</code></dt>
<dd>End bottom block, see <code>BS</code>.</dd>
<dt><code>BI&nbsp;</code><i></i>[bold-text [italic-text [bold-text [&#8230;]]]]</dt>
<dd>Bold-italic. No limit on the number of arguments, see~<code>B</code>.</dd>
<dt><code>BL&nbsp;</code><i></i>[text-indent&nbsp;[1]]</dt>
<dd>Start bullet list. Initializes a list with a bullet and a space in the beginning of each list item (see <code>LI</code>). <i>text-indent</i> overrides the default indentation of the list items set by number register <code>Pi</code>. A third argument prohibits printing of a blank line before each item.</dd>
<dt><code>BR&nbsp;</code><i></i>[bold-text [roman-text [bold-text [&#8230;]]]]</dt>
<dd>Bold-roman. No limit on the number of arguments.</dd>
<dt><code>BS</code></dt>
<dd>Bottom block start. Begins the definition of a text block which is printed at the bottom of each page. The block ends with <code>BE</code>.</dd>
<dt><code>BVL&nbsp;</code><i>text-indent </i>[mark-indent&nbsp;[1]]</dt>
<dd>Start of broken variable-item list. Broken variable-item list has no fixed mark, it assumes that every <code>LI</code> has a mark instead. The text always begins at the next line after the mark. <i>text-indent</i> sets the indentation to the text, and <i>mark-indent</i> the distance from the current indentation to the mark. A third argument prohibits printing of a blank line before each item.</dd>
<dt><code>COVER&nbsp;</code><i></i>[arg]</dt>
<dd>Begin a coversheet definition. It is important that <code>.COVER</code> appears before any normal text. This macro uses <i>arg</i> to build the filename <i>/usr/share/groff/1.22.4/tmac/mm/</i>arg<i>.cov</i>. Therefore it is possible to create unlimited types of cover sheets. <i>ms.cov</i> is supposed to look like the ms cover sheet. <code>.COVER</code> requires a <code>.COVEND</code> at the end of the cover definition. Always use this order of the cover macros:</dd>
<dl>
<dd>
</dd><dl>
<dd>
<pre>.COVER
.TL
.AF
.AU
.AT
.AS
.AE
.COVEND</pre>
</dd></dl>
</dl>
<dd>However, only <code>.TL</code> and <code>.AU</code> are required.</dd>
<dt><code>COVEND</code></dt>
<dd>Finish the cover description and print the cover page. It is defined in the cover file.</dd>
<dt><code>DE</code></dt>
<dd>Display end. Ends a block of text or display that begins with <code>DS</code> or <code>DF</code>.</dd>
<dt><code>DF&nbsp;</code><i></i>[format [fill [rindent]]]</dt>
<dd>Begin floating display (no nesting allowed). A floating display is saved in a queue and is printed in the order entered. <i>Format</i>, <i>fill</i>, and <i>rindent</i> are the same as in <code>DS</code>. Floating displays are controlled by the two number registers <code>De</code> and <code>Df</code>.</dd>
<dd><code>De register</code></dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td>0</td>
<td> Nothing special, this is the default.
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td> A page eject occurs after each printed display, giving only one display per page and no text following it.
</td>
</tr>
</table>
</dd></dl>
</dl>
<dd><code>Df register</code></dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td>0</td>
<td> Displays are printed at the end of each section (when section-page numbering is active) or at the end of the document.
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td> A new display is printed on the current page if there is enough space, otherwise it is printed at the end of the document.
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td> One display is printed at the top of each page or column (in multi-column mode).
</td>
</tr>
<tr VALIGN=top>
<td>3</td>
<td> Print one display if there is enough space for it, otherwise it is printed at the top of the next page or column.
</td>
</tr>
<tr VALIGN=top>
<td>4</td>
<td> Print as many displays as possible in a new page or column. A page break occurs between each display if <code>De</code> is not zero.
</td>
</tr>
<tr VALIGN=top>
<td>5</td>
<td> Fill the current page with displays and the rest beginning at a new page or column. (This is the default.) A page break occurs between each display if <code>De</code> is not zero.
</td>
</tr>
</table>
</dd></dl>
</dl>
<dt><code>DL&nbsp;</code><i></i>[text-indent&nbsp;[<code>1</code> [<code>1</code>]]]</dt>
<dd>Dash list start. Begins a list where each item is printed after a dash. <i>text-indent</i> changes the default indentation of the list items set by number register <code>Pi</code>. A second argument prevents an empty line between each list item. See <code>LI</code>. A third argument prohibits printing of a blank line before each item.</dd>
<dt><code>DS&nbsp;</code><i></i>[format [fill [rindent]]]</dt>
<dd>Static display start. Begins collection of text until <code>DE</code>. The text is printed together on the same page, unless it is longer than the height of the page. <code>DS</code> can be nested arbitrarily.</dd>
<dd><code>format</code></dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td>&quot;&quot;</td>
<td>No indentation.
</td>
</tr>
<tr VALIGN=top>
<td>none</td>
<td>No indentation.
</td>
</tr>
<tr VALIGN=top>
<td>L</td>
<td>No indentation.
</td>
</tr>
<tr VALIGN=top>
<td>I</td>
<td> Indent text with the value of number register <code>Si</code>.
</td>
</tr>
<tr VALIGN=top>
<td>C</td>
<td>Center each line.
</td>
</tr>
<tr VALIGN=top>
<td>CB</td>
<td>Center the whole display as a block.
</td>
</tr>
<tr VALIGN=top>
<td>R</td>
<td>Right-adjust the lines.
</td>
</tr>
<tr VALIGN=top>
<td>RB</td>
<td>Right-adjust the whole display as a block.
</td>
</tr>
</table>
</dd></dl>
</dl>
<dd>The values &#8216;L&#8217;, &#8216;I&#8217;, &#8216;C&#8217;, and &#8216;CB&#8217; can also be specified as &#8216;0&#8217;, &#8216;1&#8217;, &#8216;2&#8217;, and &#8216;3&#8217;, respectively, for compatibility reasons.</dd>
<dd><code>fill</code></dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td>&quot;&quot;</td>
<td>Line-filling turned off.
</td>
</tr>
<tr VALIGN=top>
<td>none</td>
<td>Line-filling turned off.
</td>
</tr>
<tr VALIGN=top>
<td>N</td>
<td>Line-filling turned off.
</td>
</tr>
<tr VALIGN=top>
<td>F</td>
<td>Line-filling turned on.
</td>
</tr>
</table>
</dd></dl>
</dl>
<dd>&#8216;N&#8217; and &#8216;F&#8217; can also be specified as &#8216;0&#8217; and &#8216;1&#8217;, respectively.</dd>
<dd>By default, an empty line is printed before and after the display. Setting number register <code>Ds</code> to~0 prevents this. <i>rindent</i> shortens the line length by that amount.</dd>
<dt><code>EC&nbsp;</code><i></i>[title [override [flag [refname]]]]</dt>
<dd>Equation title. Sets a title for an equation. The <i>override</i> argument changes the numbering.</dd>
<dd><code>flag</code></dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td>none</td>
<td> <i>override</i> is a prefix to the number.
</td>
</tr>
<tr VALIGN=top>
<td>0</td>
<td> <i>override</i> is a prefix to the number.
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td> <i>override</i> is a suffix to the number.
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td> <i>override</i> replaces the number.
</td>
</tr>
</table>
</dd></dl>
</dl>
<dd><code>EC</code> uses the number register <code>Ec</code> as a counter. It is possible to use <code>.af</code> to change the format of the number. If number register <code>Of</code> is~1, the format of title uses a dash instead of a dot after the number.</dd>
<dd>The string <code>Le</code> controls the title of the List of Equations; default is &#8216;LIST OF EQUATIONS&#8217;. The List of Equations is only printed if number register <code>Le</code> is~1. The default is~0. The string <code>Liec</code> contains the word &#8216;Equation&#8217;, which is printed before the number. If <i>refname</i> is used, then the equation number is saved with <code>.SETR</code>, and can be retrieved with &#8216;<code>.GETST</code> <i>refname</i>&#8216;.</dd>
<dd>Special handling of the title occurs if <code>EC</code> is used inside <code>DS</code>/<code>DE</code>; it is not affected by the format of <code>DS</code>.</dd>
<dt><code>EF&nbsp;</code><i></i>[arg]</dt>
<dd>Even-page footer, printed just above the normal page footer on even pages. See <code>PF</code>.</dd>
<dd>This macro defines string <code>EOPef</code>.</dd>
<dt><code>EH&nbsp;</code><i></i>[arg]</dt>
<dd>Even-page header, printed just below the normal page header on even pages. See <code>PH</code>.</dd>
<dd>This macro defines string <code>TPeh</code>.</dd>
<dt><code>EN</code></dt>
<dd>Equation end, see <code>EQ</code>.</dd>
<dt><code>EOP</code></dt>
<dd>End-of-page user-defined macro. This macro is called instead of the normal printing of the footer. The macro is executed in a separate environment, without any trap active. See <code>TP</code>.</dd>
<dd><code>Strings available to EOP</code></dd>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td>EOPf</td>
<td>argument of <code>PF</code>
</td>
</tr>
<tr VALIGN=top>
<td>EOPef</td>
<td>argument of <code>EF</code>
</td>
</tr>
<tr VALIGN=top>
<td>EOPof</td>
<td>argument of <code>OF</code>
</td>
</tr>
</table>
</dd></dl>
<dt><code>EPIC&nbsp;</code><i></i>[<code>-L</code>] width height [name]</dt>
<dd>Draw a box with the given <i>width</i> and <i>height</i>. It also prints the text <i>name</i> or a default string if <i>name</i> is not specified. This is used to include external pictures; just give the size of the picture. <code>-L</code> left-adjusts the picture; the default is to center. See <code>PIC</code>.</dd>
<dt><code>EQ&nbsp;</code><i></i>[label]</dt>
<dd>Equation start. <code>EQ</code>/<code>EN</code> are the delimiters for equations written for <code><a href="/docs/linux/man/1-eqn/">eqn</a></code>(1). <code>EQ</code>/<code>EN</code> must be inside of a <code>DS</code>/<code>DE</code> pair, except if <code>EQ</code> is used to set options for <code>eqn</code> only. The <i>label</i> argument appears at the right margin of the equation, centered vertically within the <code>DS</code>/<code>DE</code> block, unless number register <code>Eq</code> is~1. Then the label appears at the left margin.</dd>
<dd>If there are multiple <code>EQ</code>/<code>EN</code> blocks within a single <code>DS</code>/<code>DE</code> pair, only the last equation label (if any) is printed.</dd>
<dt><code>EX&nbsp;</code><i></i>[title [override [flag [refname]]]]</dt>
<dd>Exhibit title. The arguments are the same as for <code>EC</code>. <code>EX</code> uses the number register <code>Ex</code> as a counter. The string <code>Lx</code> controls the title of the List of Exhibits; default is &#8216;LIST OF EXHIBITS&#8217;. The List of Exhibits is only printed if number register <code>Lx</code> is~1, which is the default. The string <code>Liex</code> contains the word &#8216;Exhibit&#8217;, which is printed before the number. If <i>refname</i> is used, the exhibit number is saved with <code>.SETR</code>, and can be retrieved with &#8216;<code>.GETST</code> <i>refname</i>&#8216;.</dd>
<dd>Special handling of the title occurs if <code>EX</code> is used inside <code>DS</code>/<code>DE</code>; it is not affected by the format of <code>DS</code>.</dd>
<dt><code>FC&nbsp;</code><i></i>[closing]</dt>
<dd>Print &#8216;Yours~very~truly,&#8217; as a formal closing of a letter or memorandum. The argument replaces the default string. The default is stored in string variable <code>Letfc</code>.</dd>
<dt><code>FD&nbsp;</code><i></i>[arg&nbsp;[1]]</dt>
<dd>Footnote default format. Controls the hyphenation (hyphen), right margin justification (adjust), and indentation of footnote text (indent). It can also change the label justification (ljust).</dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>arg</code></td>
<td><code>hyphen</code></td>
<td><code>adjust</code></td>
<td><code>indent</code></td>
<td><code>ljust</code>
</td>
</tr>
<tr VALIGN=top>
<td>0</td>
<td>no</td>
<td>yes</td>
<td>yes</td>
<td>left
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td>yes</td>
<td>yes</td>
<td>yes</td>
<td>left
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td>no</td>
<td>no</td>
<td>yes</td>
<td>left
</td>
</tr>
<tr VALIGN=top>
<td>3</td>
<td>yes</td>
<td>no</td>
<td>yes</td>
<td>left
</td>
</tr>
<tr VALIGN=top>
<td>4</td>
<td>no</td>
<td>yes</td>
<td>no</td>
<td>left
</td>
</tr>
<tr VALIGN=top>
<td>5</td>
<td>yes</td>
<td>yes</td>
<td>no</td>
<td>left
</td>
</tr>
<tr VALIGN=top>
<td>6</td>
<td>no</td>
<td>no</td>
<td>no</td>
<td>left
</td>
</tr>
<tr VALIGN=top>
<td>7</td>
<td>yes</td>
<td>no</td>
<td>no</td>
<td>left
</td>
</tr>
<tr VALIGN=top>
<td>8</td>
<td>no</td>
<td>yes</td>
<td>yes</td>
<td>right
</td>
</tr>
<tr VALIGN=top>
<td>9</td>
<td>yes</td>
<td>yes</td>
<td>yes</td>
<td>right
</td>
</tr>
<tr VALIGN=top>
<td>10</td>
<td>no</td>
<td>no</td>
<td>yes</td>
<td>right
</td>
</tr>
<tr VALIGN=top>
<td>11</td>
<td>yes</td>
<td>no</td>
<td>yes</td>
<td>right
</td>
</tr>
</table>
</dd></dl>
</dl>
<dd>An argument greater than or equal to 11 is considered as value~0. Default for <code>mm</code> is 10.</dd>
<dt><code>FE</code></dt>
<dd>Footnote end.</dd>
<dt><code>FG&nbsp;</code><i></i>[title [override [flag [refname]]]]</dt>
<dd>Figure title. The arguments are the same as for <code>EC</code>. <code>FG</code> uses the number register <code>Fg</code> as a counter. The string <code>Lf</code> controls the title of the List of Figures; default is &#8216;LIST OF FIGURES&#8217;. The List of Figures is only printed if number register <code>Lf</code> is~1, which is the default. The string <code>Lifg</code> contains the word &#8216;Figure&#8217;, which is printed before the number. If <i>refname</i> is used, then the figure number is saved with <code>.SETR</code>, and can be retrieved with &#8216;<code>.GETST</code> <i>refname</i>&#8216;.</dd>
<dd>Special handling of the title occurs if <code>FG</code> is used inside <code>DS</code>/<code>DE</code>, it is not affected by the format of <code>DS</code>.</dd>
<dt><code>FS&nbsp;</code><i></i>[label]</dt>
<dd>Footnote start. The footnote is ended by <code>FE</code>. By default, footnotes are automatically numbered; the number is available in string~<code>F</code>. Just add <code>\*F</code> in the text. By adding <i>label</i>, it is possible to have other number or names on the footnotes. Footnotes in displays are now possible. An empty line separates footnotes; the height of the line is controlled by number register <code>Fs</code>, default value is~1.</dd>
<dt><code>GETHN&nbsp;</code><i>refname </i>[varname]</dt>
<dd>Include the header number where the corresponding &#8216;<code>SETR</code> <i>refname</i>&#8216; was placed. This is displayed as &#8216;X.X.X.&#8217; in pass~1. See <code>INITR</code>. If <i>varname</i> is used, <code>GETHN</code> sets the string variable <i>varname</i> to the header number.</dd>
<dt><code>GETPN&nbsp;</code><i>refname </i>[varname]</dt>
<dd>Include the page number where the corresponding &#8216;<code>SETR</code> <i>refname</i>&#8216; was placed. This is displayed as &#8216;9999&#8217; in pass~1. See <code>INITR</code>. If <i>varname</i> is used, <code>GETPN</code> sets the stringvariable <i>varname</i> to the page number.</dd>
<dt><code>GETR&nbsp;</code><i>refname</i></dt>
<dd>Combine <code>GETHN</code> and <code>GETPN</code> with the text &#8216;chapter&#8217; and &#8216;,~page&#8217;. The string <code>Qrf</code> contains the text for the cross reference:</dd>
<dl>
<dd>
</dd><dl>
<dd>.ds Qrf See chapter \*[Qrfh], page \*[Qrfp].</dd></dl>
</dl>
<dd><code>Qrf</code> may be changed to support other languages. Strings <code>Qrfh</code> and <code>Qrfp</code> are set by <code>GETR</code> and contain the page and header number, respectively.</dd>
<dt><code>GETST&nbsp;</code><i>refname </i>[varname]</dt>
<dd>Include the string saved with the second argument to <code>.SETR</code>. This is a dummy string in pass~1. If <i>varname</i> is used, <code>GETST</code> sets it to the saved string. See <code>INITR</code>.</dd>
<dt><code>H&nbsp;</code><i>level </i>[heading-text [heading-suffix]]</dt>
<dd>Numbered section heading. Section headers can have a level between 1 and 14; level~1 is the top level. The text is given in <i>heading-text</i>, and must be surrounded by double quotes if it contains spaces. <i>heading-suffix</i> is added to the header in the text but not in the table of contents. This is normally used for footnote marks and similar things. Don&#8217;t use <code>\*F</code> in <i>heading-suffix</i>, it doesn&#8217;t work. A manual label must be used, see <code>FS</code>. </dd>
<p> A call to the paragraph macro~<code>P</code> directly after~<code>H</code> is ignored. <code>H</code>~takes care of spacing and indentation.</p>
<dd><code>Page ejection before heading</code></dd>
<dl>
<dd>
</dd><dl>
<dd>Number register <code>Ej</code> controls page ejection before the heading. By default, a level-one heading gets two blank lines before it; higher levels only get one. A new page is ejected before each first-level heading if number register <code>Ej</code> is~1. All levels below or equal the value of <code>Ej</code> get a new page. Default value for <code>Ej</code> is~0.</dd></dl>
</dl>
<dd><code>Heading break level</code></dd>
<dl>
<dd>
</dd><dl>
<dd>A line break occurs after the heading if the heading level is less or equal to number register <code>Hb</code>. Default value is~2.</dd></dl>
</dl>
<dd><code>Heading space level</code></dd>
<dl>
<dd>
</dd><dl>
<dd>A blank line is inserted after the heading if the heading level is less or equal to number register <code>Hs</code>. Default value is~2.</dd>
<dd>Text follows the heading on the same line if the level is greater than both <code>Hb</code> and <code>Hs</code>.</dd></dl>
</dl>
<dd><code>Post-heading indent</code></dd>
<dl>
<dd>
</dd><dl>
<dd>Indentation of the text after the heading is controlled by number register <code>Hi</code>. Default value is~0.</dd>
<dd><code>Hi</code> </dd>
<table>
<tr VALIGN=top>
<td>0</td>
<td>The text is left-justified.
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td> Indentation of the text follows the value of number register <code>Pt ,</code> see <code>P</code>.
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td> The text is lined up with the first word of the heading.
</td>
</tr>
</table>
</dl>
</dl>
<dd><code>Centered section headings</code></dd>
<dl>
<dd>
</dd><dl>
<dd>All headings whose level is equal or below number register <code>Hc</code> and also less than or equal to <code>Hb</code> or <code>Hs</code> are centered.</dd></dl>
</dl>
<dd><code>Font control of the heading</code></dd>
<dl>
<dd>
</dd><dl>
<dd>The font of each heading level is controlled by string <code>HF</code>. It contains a font number or font name for each level. Default value is</dd>
<dl>
<dd>
</dd><dl>
<dd><code>2 2 2 2 2 2 2 2 2 2 2 2 2 2</code></dd></dl>
</dl>
<dd>(all headings in italic). This could also be written as</dd>
<dl>
<dd>
</dd><dl>
<dd><code>I I I I I I I I I I I I I I</code></dd></dl>
</dl>
<dd>Note that some other implementations use <code>3~3~2~2~2~2~2</code> as the default value. All omitted values are presumed to have value~1.</dd></dl>
</dl>
<dd><code>Point size control</code></dd>
<dl>
<dd>
</dd><dl>
<dd>String <code>HP</code> controls the point size of each heading, in the same way as <code>HF</code> controls the font. A value of~0 selects the default point size. Default value is</dd>
<dl>
<dd>
</dd><dl>
<dd><code>0 0 0 0 0 0 0 0 0 0 0 0 0 0</code></dd></dl>
</dl>
<dd>Beware that only the point size changes, not the vertical size. The latter can be controlled by the user-specified macros <code>HX</code> and/or <code>HZ</code>.</dd></dl>
</dl>
<dd><code>Heading counters</code></dd>
<dl>
<dd>
</dd><dl>
<dd>Fourteen number registers named <code>H1</code> up to <code>H14</code> contain the counter for each heading level. The values are printed using Arabic numerals; this can be changed with the macro <code>HM</code> (see below). All marks are concatenated before printing. To avoid this, set number register <code>Ht</code> to~1. This only prints the current heading counter at each heading.</dd></dl>
</dl>
<dd><code>Automatic table of contents</code></dd>
<dl>
<dd>
</dd><dl>
<dd>All headings whose level is equal or below number register <code>Cl</code> are saved to be printed in the table of contents. Default value is~2.</dd></dl>
</dl>
<dd><code>Special control of the heading, user-defined macros</code></dd>
<dl>
<dd>
</dd><dl>
<dd>The following macros can be defined by the user to get a finer control of vertical spacing, fonts, or other features. Argument <i>level</i> is the level-argument to~<code>H</code>, but~0 for unnumbered headings (see <code>HU</code>). Argument <i>rlevel</i> is the real level; it is set to number register <code>Hu</code> for unnumbered headings. Argument <i>heading-text</i> is the text argument to <code>H</code> and <code>HU</code>.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>HX&nbsp;</code><i>level rlevel heading-text</i></dt>
<dd>This macro is called just before the printing of the heading. The following registers are available for <code>HX</code>. Note that <code>HX</code> may alter <code>}0</code>, <code>}2</code>, and <code>;3</code>.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>}0&nbsp;</code>(string)</dt>
<dd>Contains the heading mark plus two spaces if <i>rlevel</i> is non-zero, otherwise empty.</dd>
<dt><code>;0&nbsp;</code>(register)</dt>
<dd>Contains the position of the text after the heading. 0~means that the text should follow the heading on the same line, 1~means that a line break should occur before the text, and 2~means that a blank line should separate the heading and the text.</dd>
<dt><code>}2&nbsp;</code>(string)</dt>
<dd>Contains two spaces if register <code>;0</code> is~0. It is used to separate the heading from the text. The string is empty if <code>;0</code> is non-zero.</dd>
<dt><code>;3&nbsp;</code>(register)</dt>
<dd>Contains the needed space in units after the heading. Default is 2v. Can be used to change things like numbering (<code>}0</code>), vertical spacing (<code>}2</code>), and the needed space after the heading.</dd></dl>
</dl>
<dt><code>HY&nbsp;</code><i>dlevel rlevel heading-text</i></dt>
<dd>This macro is called after size and font calculations and might be used to change indentation.</dd>
<dt><code>HZ&nbsp;</code><i>dlevel rlevel heading-text</i></dt>
<dd>This macro is called after the printing of the heading, just before <code>H</code> or <code>HU</code> exits. Can be used to change the page header according to the section heading.</dd></dl>
</dl>
</dl>
</dl>
<dt><code>HC&nbsp;</code><i></i>[hyphenation-character]</dt>
<dd>Set hyphenation character. Default value is &#8216;\%&#8217;. Resets to the default if called without argument. Hyphenation can be turned off by setting number register <code>Hy</code> to~0 at the beginning of the file.</dd>
<dt><code>HM&nbsp;</code><i></i>[arg1 [arg2 [&#8230; [arg14]]]]</dt>
<dd>Heading mark style. Controls the type of marking for printing of the heading counters. Default is~1 for all levels.</dd>
<dd><code>Argument</code> </dd>
<table>
<tr VALIGN=top>
<td>1</td>
<td>Arabic numerals.
</td>
</tr>
<tr VALIGN=top>
<td>0001</td>
<td>Arabic numerals with leading zeroes, one or more.
</td>
</tr>
<tr VALIGN=top>
<td>A</td>
<td>upper-case alphabetic
</td>
</tr>
<tr VALIGN=top>
<td>a</td>
<td>lower-case alphabetic
</td>
</tr>
<tr VALIGN=top>
<td>I</td>
<td>upper-case roman numerals
</td>
</tr>
<tr VALIGN=top>
<td>i</td>
<td>lower-case roman numerals
</td>
</tr>
<tr VALIGN=top>
<td>&quot;&quot;</td>
<td>Arabic numerals.
</td>
</tr>
</table>
<dt><code>HU&nbsp;</code><i>heading-text</i></dt>
<dd>Unnumbered section header. <code>HU</code> behaves like <code>H</code> at the level in number register <code>Hu</code>. See~<code>H</code>.</dd>
<dt><code>HX&nbsp;</code><i>dlevel rlevel heading-text</i></dt>
<dd>User-defined heading exit. Called just before printing the header. See~<code>H</code>.</dd>
<dt><code>HY&nbsp;</code><i>dlevel rlevel heading-text</i></dt>
<dd>User-defined heading exit. Called just before printing the header. See~<code>H</code>.</dd>
<dt><code>HZ&nbsp;</code><i>dlevel rlevel heading-text</i></dt>
<dd>User-defined heading exit. Called just after printing the header. See~<code>H</code>.</dd>
<dt><code>I&nbsp;</code><i></i>[italic-text [prev-font-text [italic-text [&#8230;]]]]</dt>
<dd>Italic. Changes the font to italic if called without arguments. With one argument it sets the word in italic. With two arguments it concatenates them and sets the first word in italic and the second in the previous font. There is no limit on the number of argument; all are concatenated.</dd>
<dt><code>IA&nbsp;</code><i></i>[addressee-name [title]]</dt>
<dd>Begin specification of the addressee and addressee&#8217;s address in letter style. Several names can be specified with empty <code>IA</code>/<code>IE</code>-pairs, but only one address. See <code>LT</code>.</dd>
<dt><code>IB&nbsp;</code><i></i>[italic-text [bold-text [italic-text [&#8230;]]]]</dt>
<dd>Italic-bold. Even arguments are printed in italic, odd in boldface. See~<code>I</code>.</dd>
<dt><code>IE</code></dt>
<dd>End the address specification after <code>IA</code>.</dd>
<dt><code>INITI&nbsp;</code><i>type filename </i>[macro]</dt>
<dd>Initialize the new index system and set the filename to collect index lines in with <code>IND</code>. Argument <i>type</i> selects the type of index: page number, header marks or both. The default is page numbers.</dd>
<dd>It is also possible to create a macro that is responsible for formatting each row; just add the name of the macro as a third argument. The macro is then called with the index as argument(s).</dd>
<dd><code>type</code></dd>
<dd>
<table>
<tr VALIGN=top>
<td>N</td>
<td>Page numbers
</td>
</tr>
<tr VALIGN=top>
<td>H</td>
<td>Header marks
</td>
</tr>
<tr VALIGN=top>
<td>B</td>
<td> Both page numbers and header marks, separated with a tab character.
</td>
</tr>
</table>
</dd><dt><code>INITR&nbsp;</code><i>filename</i></dt>
<dd>Initialize the cross reference macros. Cross references are written to stderr and are supposed to be redirected into file filename<i>.qrf</i>. Requires two passes with groff; this is handled by a separate program called <code><a href="/docs/linux/man/1-mmroff/">mmroff</a></code>(1). This program exists because <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) by default deactivates the unsafe operations that are required by <code>INITR</code>. The first pass looks for cross references, and the second one includes them. <code>INITR</code> can be used several times, but it is only the first occurrence of <code>INITR</code> that is active.</dd>
<dd>See also <code>SETR</code>, <code>GETPN</code>, and <code>GETHN</code>.</dd>
<dt><code>IND&nbsp;</code><i>arg1 </i>[arg2 [&#8230;]]</dt>
<dd>Write a line in the index file selected by <code>INITI</code> with all arguments and the page number or header mark separated by tabs.</dd>
<dl>
<dd>
</dd><dl>
<dd><code>Examples</code></dd>
<dd>arg1	page number<br/>
 arg1	arg2	page number<br/>
 arg1	header mark<br/>
 arg1	page number	header mark</dd></dl>
</dl>
<dt><code>INDP</code></dt>
<dd>Print the index by running the command specified by string variable <code>Indcmd</code>, which has &#8216;sort -t	&#8217; as the default value. <code>INDP</code> reads the output from the command to form the index, by default in two columns (this can be changed by defining <code>TYIND</code>). The index is printed with string variable <code>Index</code> as header, default is &#8216;INDEX&#8217;. One-column processing is reactivated after the list. <code>INDP</code> calls the user-defined macros <code>TXIND</code>, <code>TYIND</code>, and <code>TZIND</code> if defined. <code>TXIND</code> is called before printing the string &#8216;INDEX&#8217;, <code>TYIND</code> is called instead of printing &#8216;INDEX&#8217;, and <code>TZIND</code> is called after the printing and should take care of restoring to normal operation again.</dd>
<dt><code>ISODATE </code>[0]</dt>
<dd>Change the predefined date string in <code>DT</code> to ISO-format, this is, &#8216;YYYY-MM-DD&#8217;. This can also be done by adding <code>-rIso=1</code> on the command line. Reverts to old date format if argument is~<code>0</code>.</dd>
<dt><code>IR&nbsp;</code><i></i>[italic-text [roman-text [italic-text [&#8230;]]]]</dt>
<dd>Italic-roman. Even arguments are printed in italic, odd in roman. See~<code>I</code>.</dd>
<dt><code>LB&nbsp;</code><i>text-indent mark-indent pad type </i>[mark [LI-space [LB-space]]]</dt>
<dd>List-begin macro. This is the common macro used for all lists. <i>text-indent</i> is the number of spaces to indent the text from the current indentation.</dd>
<dd><i>pad</i> and <i>mark-indent</i> control where to put the mark. The mark is placed within the mark area, and <i>mark-indent</i> sets the number of spaces before this area. By default it is~0. The mark area ends where the text begins. The start of the text is still controlled by <i>text-indent</i>.</dd>
<dd>The mark is left-justified within the mark area if <i>pad</i> is~0. If <i>pad</i> is greater than~0, <i>mark-indent</i> is ignored, and the mark is placed <i>pad</i> spaces before the text. This right-justifies the mark.</dd>
<dd>If <i>type</i> is~0 the list either has a hanging indentation or, if argument <i>mark</i> is given, the string <i>mark</i> as a mark.</dd>
<dd>If <i>type</i> is greater than~0 automatic numbering occurs, using arabic numbers if <i>mark</i> is empty. <i>mark</i> can then be any of &#8216;1&#8217;, &#8216;A&#8217;, &#8216;a&#8217;, &#8216;I&#8217;, or &#8216;i&#8217;.</dd>
<dd><i>type</i> selects one of six possible ways to display the mark.</dd>
<dd><code>type</code></dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td>1</td>
<td>x.
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td>x)
</td>
</tr>
<tr VALIGN=top>
<td>3</td>
<td>(x)
</td>
</tr>
<tr VALIGN=top>
<td>4</td>
<td>[x]
</td>
</tr>
<tr VALIGN=top>
<td>5</td>
<td>&lt;x&gt;
</td>
</tr>
<tr VALIGN=top>
<td>6</td>
<td>{x}
</td>
</tr>
</table>
</dd></dl>
</dl>
<dd>Every item in the list gets <i>LI-space</i> number of blank lines before them. Default is~1.</dd>
<dd><code>LB</code> itself prints <i>LB-space</i> blank lines. Default is~0.</dd>
<dt><code>LC&nbsp;</code><i></i>[list-level]</dt>
<dd>List-status clear. Terminates all current active lists down to <i>list-level</i>, or~0 if no argument is given. This is used by~<code>H</code> to clear any active list.</dd>
<dt><code>LE </code>[1]</dt>
<dd>List end. Terminates the current list. <code>LE</code> outputs a blank line if an argument is given.</dd>
<dt><code>LI&nbsp;</code><i></i>[mark&nbsp;[1|2]]</dt>
<dd>List item preceding every item in a list. Without argument, <code>LI</code> prints the mark determined by the current list type. By giving <code>LI</code> one argument, it uses that as the mark instead. Two arguments to <code>LI</code> makes <i>mark</i> a prefix to the current mark. There is no separating space between the prefix and the mark if the second argument is &#8216;2&#8217; instead of &#8216;1&#8217;. This behaviour can also be achieved by setting number register <code>Limsp</code> to zero. A zero length <i>mark</i> makes a hanging indentation instead.</dd>
<dd>A blank line is printed before the list item by default. This behaviour can be controlled by number register <code>Ls</code>. Pre-spacing occurs for each list level less than or equal to <code>Ls</code>. Default value is 99. There is no nesting limit.</dd>
<dd>The indentation can be changed through number register <code>Li</code>. Default is~6.</dd>
<dd>All lists begin with a list initialization macro, <code>LB</code>. There are, however, seven predefined list types to make lists easier to use. They all call <code>LB</code> with different default values.</dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>AL</code></td>
<td>Automatically Incremented List
</td>
</tr>
<tr VALIGN=top>
<td><code>ML</code></td>
<td>Marked List
</td>
</tr>
<tr VALIGN=top>
<td><code>VL</code></td>
<td>Variable-Item List
</td>
</tr>
<tr VALIGN=top>
<td><code>BL</code></td>
<td>Bullet List
</td>
</tr>
<tr VALIGN=top>
<td><code>DL</code></td>
<td>Dash List
</td>
</tr>
<tr VALIGN=top>
<td><code>RL</code></td>
<td>Reference List
</td>
</tr>
<tr VALIGN=top>
<td><code>BVL</code></td>
<td>Broken Variable List.
</td>
</tr>
</table>
</dd></dl>
</dl>
<dd>These lists are described at other places in this manual. See also <code>LB</code>.</dd>
<dt><code>LT&nbsp;</code><i></i>[<i>arg/</i>]<i></i></dt>
<dd>Format a letter in one of four different styles depending on the argument. Also see section &#8220;Internals&#8221; below.</dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>Arg</code></td>
<td><code>Style</code>
</td>
</tr>
<tr VALIGN=top>
<td>BL</td>
<td> Blocked. Date line, return address, writer&#8217;s address and closing begins at the center of the line. All other lines begin at the left margin.
</td>
</tr>
<tr VALIGN=top>
<td>SB</td>
<td> Semi-blocked. Same as blocked, except that the first line in every paragraph is indented five spaces.
</td>
</tr>
<tr VALIGN=top>
<td>FB</td>
<td> Full-blocked. All lines begin at the left margin.
</td>
</tr>
<tr VALIGN=top>
<td>SP</td>
<td> Simplified. Almost the same as the full-blocked style. Subject and the writer&#8217;s identification are printed in all-capital.
</td>
</tr>
</table>
</dd></dl>
</dl>
<dt><code>LO&nbsp;</code><i>type </i>[arg]</dt>
<dd>Specify options in letter (see <code>.LT</code>). This is a list of the standard options:</dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td>CN</td>
<td> Confidential notation. Prints &#8216;CONFIDENTIAL&#8217; on the second line below the date line. Any argument replaces &#8216;CONFIDENTIAL&#8217;. See also string variable <code>LetCN</code>.
</td>
</tr>
<tr VALIGN=top>
<td>RN</td>
<td> Reference notation. Prints &#8216;In reference to:&#8217; and the argument two lines below the date line. See also string variable <code>LetRN</code>.
</td>
</tr>
<tr VALIGN=top>
<td>AT</td>
<td> Attention. Prints &#8216;ATTENTION:&#8217; and the argument below the inside address. See also string variable <code>LetAT</code>.
</td>
</tr>
<tr VALIGN=top>
<td>SA</td>
<td> Salutation. Prints &#8216;To Whom It May Concern:&#8217; or the argument if it was present. The salutation is printed two lines below the inside address. See also string variable <code>LetSA</code>.
</td>
</tr>
<tr VALIGN=top>
<td>SJ</td>
<td> Subject line. Prints the argument as subject prefixed with &#8216;SUBJECT:&#8217; two lines below the inside address, except in letter type &#8216;SP&#8217;, where the subject is printed in all-capital without any prefix. See also string variable <code>LetSJ</code>.
</td>
</tr>
</table>
</dd></dl>
</dl>
<dt><code>MC&nbsp;</code><i>column-size </i>[column-separation]</dt>
<dd>Begin multiple columns. Return to normal with <code>1C</code>. <code>MC</code> creates as many columns as the current line length permits. <i>column-size</i> is the width of each column, and <i>column-separation</i> is the space between two columns. Default separation is <i>column-size</i>/15. See also <code>1C</code>.</dd>
<dt><code>ML&nbsp;</code><i>mark </i>[text-indent&nbsp;[1]]</dt>
<dd>Marked list start. The <i>mark</i> argument is printed before each list item. <i>text-indent</i> sets the indent and overrides <code>Li</code>. A third argument prohibits printing of a blank line before each item.</dd>
<dt><code>MT&nbsp;</code><i></i>[arg [addressee]]</dt>
<dd>Memorandum type. The argument <i>arg</i> is part of a filename in <i>/usr/share/groff/1.22.4/tmac/mm/</i>*<i>.MT</i>. Memorandum types 0 to~5 are supported, including type &#8216;string&#8217; (which gets internally mapped to type~6). <i>addressee</i> just sets a variable, used in the AT&amp;T macros.</dd>
<dd><code>arg</code></dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td>0</td>
<td>Normal memorandum, no type printed.
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td>Memorandum with &#8216;MEMORANDUM FOR FILE&#8217; printed.
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td>Memorandum with &#8216;PROGRAMMER&#8217;S NOTES&#8217; printed.
</td>
</tr>
<tr VALIGN=top>
<td>3</td>
<td>Memorandum with &#8216;ENGINEER&#8217;S NOTES&#8217; printed.
</td>
</tr>
<tr VALIGN=top>
<td>4</td>
<td>Released paper style.
</td>
</tr>
<tr VALIGN=top>
<td>5</td>
<td>External letter style.
</td>
</tr>
</table>
</dd></dl>
</dl>
<dd>See also <code>COVER</code>/<code>COVEND</code>, a more flexible type of front page.</dd>
<dt><code>MOVE&nbsp;</code><i>y-pos </i>[x-pos [line-length]]</dt>
<dd>Move to a position, setting page offset to <i>x-pos</i>. If <i>line-length</i> is not given, the difference between current and new page offset is used. Use <code>PGFORM</code> without arguments to return to normal.</dd>
<dt><code>MULB&nbsp;</code><i>cw1 space1 </i>[cw2 space2 [cw3 &#8230;]]</dt>
<dd>Begin a special multi-column mode. All columns widths must be specified. The space between the columns must be specified also. The last column does not need any space definition. <code>MULB</code> starts a diversion, and <code>MULE</code> ends the diversion and prints the columns. The unit for the width and space arguments is &#8216;n&#8217;, but <code>MULB</code> accepts all normal unit specifications like &#8216;c&#8217; and &#8216;i&#8217;. <code>MULB</code> operates in a separate environment.</dd>
<dt><code>MULN</code></dt>
<dd>Begin the next column. This is the only way to switch the column.</dd>
<dt><code>MULE</code></dt>
<dd>End the multi-column mode and print the columns.</dd>
<dt><code>nP&nbsp;</code><i></i>[type]</dt>
<dd>Print numbered paragraph with header level two. See <code>.P</code>.</dd>
<dt><code>NCOL</code></dt>
<dd>Force printing to the next column. Don&#8217;t use this together with the <code>MUL*</code> macros, see <code>2C</code>.</dd>
<dt><code>NS&nbsp;</code><i></i>[arg&nbsp;[1]]</dt>
<dd>Print different types of notations. The argument selects between the predefined type of notations. If the second argument is available, then the argument becomes the entire notation. If the argument doesn&#8217;t select a predefined type, it is printed as &#8216;Copy (<i>arg/</i>) to&#8217;. It is possible to add more standard notations, see the string variables <code>Letns</code> and <code>Letnsdef</code>.</dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>Arg</code></td>
<td>Notation
</td>
</tr>
<tr VALIGN=top>
<td><i>none/</i></td>
<td>Copy To
</td>
</tr>
<tr VALIGN=top>
<td>&quot;&quot;</td>
<td>Copy To
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td>Copy To (with att.) to
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td>Copy To (without att.) to
</td>
</tr>
<tr VALIGN=top>
<td>3</td>
<td>Att.
</td>
</tr>
<tr VALIGN=top>
<td>4</td>
<td>Atts.
</td>
</tr>
<tr VALIGN=top>
<td>5</td>
<td>Enc.
</td>
</tr>
<tr VALIGN=top>
<td>6</td>
<td>Encs.
</td>
</tr>
<tr VALIGN=top>
<td>7</td>
<td>Under separate cover
</td>
</tr>
<tr VALIGN=top>
<td>8</td>
<td>Letter to
</td>
</tr>
<tr VALIGN=top>
<td>9</td>
<td>Memorandum to
</td>
</tr>
<tr VALIGN=top>
<td>10</td>
<td>Copy (with atts.) to
</td>
</tr>
<tr VALIGN=top>
<td>11</td>
<td>Copy (without atts.) to
</td>
</tr>
<tr VALIGN=top>
<td>12</td>
<td>Abstract Only to
</td>
</tr>
<tr VALIGN=top>
<td>13</td>
<td>Complete Memorandum to
</td>
</tr>
<tr VALIGN=top>
<td>14</td>
<td>CC
</td>
</tr>
</table>
</dd></dl>
</dl>
<dt><code>ND&nbsp;</code><i>new-date</i></dt>
<dd>New date. Overrides the current date. Date is not printed if <i>new-date</i> is an empty string.</dd>
<dt><code>OF&nbsp;</code><i></i>[arg]</dt>
<dd>Odd-page footer, a line printed just above the normal footer. See <code>EF</code> and <code>PF</code>.</dd>
<dd>This macro defines string <code>EOPof</code>.</dd>
<dt><code>OH&nbsp;</code><i></i>[arg]</dt>
<dd>Odd-page header, a line printed just below the normal header. See <code>EH</code> and <code>PH</code>.</dd>
<dd>This macro defines string <code>TPoh</code>.</dd>
<dt><code>OP</code></dt>
<dd>Make sure that the following text is printed at the top of an odd-numbered page. Does not output an empty page if currently at the top of an odd page.</dd>
<dt><code>P&nbsp;</code><i></i>[type]</dt>
<dd>Begin new paragraph. <code>P</code>~without argument produces left-justified text, even the first line of the paragraph. This is the same as setting <i>type</i> to~0. If the argument is~1, the first line of text following~<code>P</code> is indented by the number of spaces in number register <code>Pi</code>, by default~5.</dd>
<dd>Instead of giving an argument to~<code>P</code> it is possible to set the paragraph type in number register <code>Pt</code>. Using 0 and~1 is the same as adding that value to <code>P</code>. A value of~2 indents all paragraphs, except after headings, lists, and displays (this value can&#8217;t be used as an argument to <code>P</code> itself).</dd>
<dd>The space between two paragraphs is controlled by number register <code>Ps</code>, and is~1 by default (one blank line).</dd>
<dt><code>PGFORM&nbsp;</code><i></i>[linelength [pagelength [pageoffset&nbsp;[1]]]]</dt>
<dd>Set line length, page length, and/or page offset. This macro can be used for special formatting, like letter heads and other. It is normally the first command in a file, though it is not necessary. <code>PGFORM</code> can be used without arguments to reset everything after a <code>MOVE</code> call. A line break is done unless the fourth argument is given. This can be used to avoid the page number on the first page while setting new width and length. (It seems as if this macro sometimes doesn&#8217;t work too well. Use the command-line arguments to change line length, page length, and page offset instead.)</dd>
<dt><code>PGNH</code></dt>
<dd>No header is printed on the next page. Used to get rid of the header in letters or other special texts. This macro must be used before any text to inhibit the page header on the first page.</dd>
<dt><code>PIC </code>[-B] [-L] [-C] [-R] [-I&nbsp;<i>n</i>] filename [width [height]]</dt>
<dd>Include a PostScript file in the document. The macro depends on <code><a href="/docs/linux/man/1-mmroff/">mmroff</a></code>(1) and <code>INITR</code>. The arguments <code>-L</code>, <code>-C</code>, <code>-R</code>, and <code>-I&nbsp;</code><i>n</i> adjust the picture or indent it. With no flag the picture is adjusted to the left. Adding <code>-B</code> draws a box around the picture. The optional <i>width</i> and <i>height</i> can also be given to resize the picture.</dd>
<dt><code>PE</code></dt>
<dd>Picture end. Ends a picture for <code><a href="/docs/linux/man/1-pic/">pic</a></code>(1).</dd>
<dt><code>PF&nbsp;</code><i></i>[arg]</dt>
<dd>Page footer. <code>PF</code> sets the line to be printed at the bottom of each page. Empty by default. See <code>PH</code> for the argument specification.</dd>
<dd>This macro defines string <code>EOPf</code>.</dd>
<dt><code>PH&nbsp;</code><i></i>[arg]</dt>
<dd>Page header, a line printed at the top of each page. The argument should be specified as</dd>
<dl>
<dd>
</dd><dl>
<dd>&quot;&#8217;<i>left-part</i>&#8216;<i>center-part</i>&#8216;<i>right-part</i>&#8216;&quot;</dd></dl>
</dl>
<dd>where <i>left-part</i>, <i>center-part</i>, and <i>right-part</i> are printed left-justified, centered, and right justified, respectively. Within the argument to <code>PH</code>, the character &#8216;%&#8217; is changed to the current page number. The default argument is</dd>
<dl>
<dd>
</dd><dl>
<dd>&quot;&#8221;- % -&#8221;&quot;</dd></dl>
</dl>
<dd>which gives the page number between two dashes.</dd>
<dd>This macro defines string <code>TPh</code>.</dd>
<dt><code>PS</code></dt>
<dd>Picture start (from pic). Begins a picture for <code><a href="/docs/linux/man/1-pic/">pic</a></code>(1).</dd>
<dt><code>PX</code></dt>
<dd>Page header user-defined exit. This macro is called just after the printing of the page header in <i>no-space</i> mode.</dd>
<dt><code>R</code></dt>
<dd>Roman. Return to roman font, see also~<code>I</code>.</dd>
<dt><code>RB&nbsp;</code><i></i>[roman-text [bold-text [roman-text [&#8230;]]]]</dt>
<dd>Roman-bold. Even arguments are printed in roman, odd in boldface. See~<code>I</code>.</dd>
<dt><code>RD&nbsp;</code><i></i>[prompt [diversion [string]]]</dt>
<dd>Read from standard input to diversion and/or string. The text is saved in a diversion named <i>diversion</i>. Recall the text by writing the name of the diversion after a dot on an empty line. A string is also defined if <i>string</i> is given. <i>Diversion</i> and/or <i>prompt</i> can be empty (&quot;&quot;).</dd>
<dt><code>RF</code></dt>
<dd>Reference end. Ends a reference definition and returns to normal processing. See <code>RS</code>.</dd>
<dt><code>RI&nbsp;</code><i></i>[roman-text [italic-text [roman-text [&#8230;]]]]</dt>
<dd>Print even arguments in roman, odd in italic. See~<code>I</code>.</dd>
<dt><code>RL&nbsp;</code><i></i>[text-indent[1]]</dt>
<dd>Reference list start. Begins a list where each item is preceded with an automatically incremented number between square brackets. <i>text-indent</i> changes the default indentation.</dd>
<dt><code>RP&nbsp;</code><i></i>[arg1 [arg2]]</dt>
<dd>Produce reference page. This macro can be used if a reference page is wanted somewhere in the document. It is not needed if <code>TC</code> is used to produce a table of contents. The reference page is then printed automatically.</dd>
<dd>The reference counter is not reset if <i>arg1</i> is~1.</dd>
<dd><i>arg2</i> tells <code>RP</code> whether to eject a page or not.</dd>
<dd><code>arg2</code></dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td>0</td>
<td>The reference page is printed on a separate page.
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td>Do not eject page after the list.
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td>Do not eject page before the list.
</td>
</tr>
<tr VALIGN=top>
<td>3</td>
<td>Do not eject page before and after the list.
</td>
</tr>
</table>
</dd></dl>
</dl>
<dd>The reference items are separated by a blank line. Setting number register <code>Ls</code> to~0 suppresses the line.</dd>
<dd>The string <code>Rp</code> contains the reference page title and is set to &#8216;REFERENCES&#8217; by default. The number register <code>Rpe</code> holds the default value for the second argument of <code>RP</code>; it is initially set to~0.</dd>
<dt><code>RS&nbsp;</code><i></i>[string-name]</dt>
<dd>Begin an automatically numbered reference definition. Put the string <code>\*(Rf</code> where the reference mark should be and write the reference between <code>RS</code>/<code>RF</code> at next new line after the reference mark. The reference number is stored in number register <code>:R</code>. If <i>string-name</i> is given, a string with that name is defined and contains the current reference mark. The string can be referenced as <code>\*[</code><i>string-name</i><code>]</code> later in the text.</dd>
<dt><code>S&nbsp;</code><i></i>[size [spacing]]</dt>
<dd>Set point size and vertical spacing. If any argument is equal to &#8216;P&#8217;, the previous value is used. A &#8216;C&#8217; means current value, and &#8216;D&#8217; the default value. If &#8216;+&#8217; or &#8216;-&#8216; is used before the value, the current value is incremented or decremented, respectively.</dd>
<dt><code>SA&nbsp;</code><i></i>[arg]</dt>
<dd>Set right-margin justification. Justification is turned on by default. No argument or value &#8216;0&#8217; turns off justification, and &#8216;1&#8217; turns on justification.</dd>
<dt><code>SETR&nbsp;</code><i>refname </i>[string]</dt>
<dd>Remember the current header and page number as <i>refname</i>. Saves <i>string</i> if <i>string</i> is defined. <i>string</i> is retrieved with <code>.GETST</code>. See <code>INITR</code>.</dd>
<dt><code>SG&nbsp;</code><i></i>[arg&nbsp;[1]]</dt>
<dd>Signature line. Prints the authors name(s) after the formal closing. The argument is appended to the reference data, printed at either the first or last author. The reference data is the location, department, and initials specified with <code>.AU</code>. It is printed at the first author if the second argument is given, otherwise at the last. No reference data is printed if the author(s) is specified through <code>.WA</code>/<code>.WE</code>. See section &#8220;Internals&#8221; below.</dd>
<dt><code>SK&nbsp;</code><i></i>[pages]</dt>
<dd>Skip pages. If <i>pages</i> is~0 or omitted, a skip to the next page occurs unless it is already at the top of a page. Otherwise it skips <i>pages</i> pages.</dd>
<dt><code>SM&nbsp;</code><i>string1 </i>[string2 [string3]]</dt>
<dd>Make a string smaller. If <i>string2</i> is given, <i>string1</i> is made smaller and <i>string2</i> stays at normal size, concatenated with <i>string1</i>. With three arguments, everything is concatenated, but only <i>string2</i> is made smaller.</dd>
<dt><code>SP&nbsp;</code><i></i>[lines]</dt>
<dd>Space vertically. <i>lines</i> can have any scaling factor, like &#8216;3i&#8217; or &#8216;8v&#8217;. Several <code>SP</code> calls in a line only produces the maximum number of lines, not the sum. <code>SP</code> is ignored also until the first text line in a page. Add <code>\&amp;</code> before a call to <code>SP</code> to avoid this.</dd>
<dt><code>TAB</code></dt>
<dd>Reset tabs to every 5n. Normally used to reset any previous tab positions.</dd>
<dt><code>TB&nbsp;</code><i></i>[title [override [flag [refname]]]]</dt>
<dd>Table title. The arguments are the same as for <code>EC</code>. <code>TB</code> uses the number register <code>Tb</code> as a counter. The string <code>Lt</code> controls the title of the List of Tables; default value is &#8216;LIST OF TABLES&#8217;. The List of Tables is only printed if number register <code>Lt</code> is~1, which is the default. The string <code>Litb</code> contains the word &#8216;TABLE&#8217;, which is printed before the number.</dd>
<dd>Special handling of the title occurs if <code>TB</code> is used inside <code>DS</code>/<code>DE</code>, it is not affected by the format of <code>DS</code>.</dd>
<dt><code>TC&nbsp;</code><i></i>[slevel [spacing [tlevel [tab [h1 [h2 [h3 [h4 [h5]]]]]]]]]</dt>
<dd>Table of contents. This macro is normally used as the last line of the document. It generates a table of contents with headings up to the level controlled by number register <code>Cl</code>. Note that <code>Cl</code> controls the saving of headings, it has nothing to do with <code>TC</code>. Headings with a level less than or equal to <i>slevel</i> get <i>spacing</i> number of lines before them. Headings with a level less than or equal to <i>tlevel</i> have their page numbers right-justified with dots or spaces separating the text and the page number. Spaces are used if <i>tab</i> is greater than zero, dots otherwise. Other headings have the page number directly at the end of the heading text (<i>ragged-right</i>).</dd>
<dd>The rest of the arguments is printed, centered, before the table of contents.</dd>
<dd>The user-defined macros <code>TX</code> and <code>TY</code> are used if <code>TC</code> is called with at most four arguments. <code>TX</code> is called before the printing of the string &#8216;CONTENTS&#8217;, and <code>TY</code> is called instead of printing &#8216;CONTENTS&#8217;.</dd>
<dd>Equivalent macros can be defined for list of figures, tables, equations and exhibits by defining <code>TX</code><i>xx</i> or <code>TY</code><i>xx</i>, where <i>xx</i> is &#8216;Fg&#8217;, &#8216;TB&#8217;, &#8216;EC&#8217;, or &#8216;EX&#8217;, respectively.</dd>
<dd>String <code>Ci</code> can be set to control the indentations for each heading-level. It must be scaled, like</dd>
<dl>
<dd>
</dd><dl>
<dd>.ds Ci .25i .5i .75i 1i 1i</dd></dl>
</dl>
<dd>By default, the indentation is controlled by the maximum length of headings in each level.</dd>
<dd>The string variables <code>Lifg</code>, <code>Litb</code>, <code>Liex</code>, <code>Liec</code>, and <code>Licon</code> contain &#8216;Figure&#8217;, &#8216;TABLE&#8217;, &#8216;Exhibit&#8217;, &#8216;Equation&#8217;, and &#8216;CONTENTS&#8217;, respectively. These can be redefined to other languages.</dd>
<dt><code>TE</code></dt>
<dd>Table end. See <code>TS</code>.</dd>
<dt><code>TH </code>[N]</dt>
<dd>Table header. See <code>TS</code>. <code>TH</code> ends the header of the table. This header is printed again if a page break occurs. Argument &#8216;N&#8217; isn&#8217;t implemented yet.</dd>
<dt><code>TL&nbsp;</code><i></i>[charging-case-number [filing-case-number]]</dt>
<dd>Begin title of memorandum. All text up to the next <code>AU</code> is included in the title. <i>charging-case-number</i> and <i>filing-case-number</i> are saved for use in the front page processing.</dd>
<dt><code>TM&nbsp;</code><i></i>[num1 [num2 [&#8230;]]]</dt>
<dd>Technical memorandum numbers used in <code>.MT</code>. An unlimited number of arguments may be given.</dd>
<dt><code>TP</code></dt>
<dd>Top-of-page user-defined macro. This macro is called instead of the normal page header. It is possible to get complete control over the header. Note that the header and the footer are printed in a separate environment. Line length is preserved, though. See <code>EOP</code>.</dd>
<dd><code>strings available to TP</code></dd>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td>TPh</td>
<td>argument of <code>PH</code>
</td>
</tr>
<tr VALIGN=top>
<td>TPeh</td>
<td>argument of <code>EH</code>
</td>
</tr>
<tr VALIGN=top>
<td>TPoh</td>
<td>argument of <code>OH</code>
</td>
</tr>
</table>
</dd></dl>
<dt><code>TS </code>[H]</dt>
<dd>Table start. This is the start of a table specification to <code><a href="/docs/linux/man/1-tbl/">tbl</a></code>(1). <code>TS</code> ends with <code>TE</code>. Argument &#8216;H&#8217; tells <code>mm</code> that the table has a header. See <code>TH</code>.</dd>
<dt><code>TX</code></dt>
<dd>User-defined table of contents exit. This macro is called just before <code>TC</code> prints the word &#8216;CONTENTS&#8217;. See <code>TC</code>.</dd>
<dt><code>TY</code></dt>
<dd>User-defined table of contents exit. This macro is called instead of printing &#8216;CONTENTS&#8217;. See <code>TC</code>.</dd>
<dt><code>VERBON&nbsp;</code><i></i>[flag [point-size [font]]]</dt>
<dd>Begin verbatim output using Courier font. Usually for printing programs. All characters have equal width. The point size can be changed with the second argument. By specifying a third argument it is possible to use another font instead of Courier. <i>flag</i> controls several special features. Its value is the sum of all wanted features.</dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>Arg</code></td>
<td><code>Description</code>
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td> Disable the escape character (\). This is normally turned on during verbose output.
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td>Add an empty line before the verbose text.
</td>
</tr>
<tr VALIGN=top>
<td>4</td>
<td>Add an empty line after the verbose text.
</td>
</tr>
<tr VALIGN=top>
<td>8</td>
<td> Print the verbose text with numbered lines. This adds four digit-sized spaces in the beginning of each line. Finer control is available with the string variable <code>Verbnm</code>. It contains all arguments to the <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1) command <code>.nm</code>, normally &#8216;1&#8217;.
</td>
</tr>
<tr VALIGN=top>
<td>16</td>
<td> Indent the verbose text by &#8216;5n&#8217;. This is controlled by the number-variable <code>Verbin</code> (in units).
</td>
</tr>
</table>
</dd></dl>
</dl>
<dt><code>VERBOFF</code></dt>
<dd>End verbatim output.</dd>
<dt><code>VL&nbsp;</code><i>text-indent </i>[mark-indent&nbsp;[1]]</dt>
<dd>Variable-item list. It has no fixed mark, it assumes that every <code>LI</code> has a mark instead. <i>text-indent</i> sets the indent to the text, and <i>mark-indent</i> the distance from the current indentation to the mark. A third argument prohibits printing of a blank line before each item.</dd>
<dt><code>VM </code>[-T] [<i>top </i>[bottom]]</dt>
<dd>Vertical margin. Increase the top and bottom margin by <i>top</i> and <i>bottom</i>, respectively. If option <code>-T</code> is specified, set those margins to <i>top</i> and <i>bottom</i>. If no argument is given, reset the margin to zero, or to the default (&#8216;7v 5v&#8217;) if <code>-T</code> is used. It is highly recommended that macros <code>TP</code> and/or <code>EOP</code> are defined if using <code>-T</code> and setting top and/or bottom margin to less than the default.</dd>
<dt><code>WA&nbsp;</code><i></i>[writer-name [title]]</dt>
<dd>Begin specification of the writer and writer&#8217;s address. Several names can be specified with empty <code>WA</code>/<code>WE</code> pairs, but only one address.</dd>
<dt><code>WE</code></dt>
<dd>End the address specification after <code>.WA</code>.</dd>
<dt><code>WC&nbsp;</code><i></i>[format1] [format2] [&#8230;]</dt>
<dd>Footnote and display width control.</dd>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td>N</td>
<td> Set default mode which is equal to using the options <code>-WF</code>, <code>-FF</code>, <code>-WD</code>, and <code>FB</code>.
</td>
</tr>
<tr VALIGN=top>
<td>WF</td>
<td> Wide footnotes, wide also in two-column mode.
</td>
</tr>
<tr VALIGN=top>
<td>-WF</td>
<td>Normal footnote width, follow column mode.
</td>
</tr>
<tr VALIGN=top>
<td>FF</td>
<td> All footnotes gets the same width as the first footnote encountered.
</td>
</tr>
<tr VALIGN=top>
<td>-FF</td>
<td> Normal footnotes, width follows <code>WF</code> and <code>-WF</code>.
</td>
</tr>
<tr VALIGN=top>
<td>WD</td>
<td> Wide displays, wide also in two-column mode.
</td>
</tr>
<tr VALIGN=top>
<td>-WD</td>
<td> Normal display width, follow column mode.
</td>
</tr>
<tr VALIGN=top>
<td>FB</td>
<td> Floating displays generates a line break when printed on the current page.
</td>
</tr>
<tr VALIGN=top>
<td>-FB</td>
<td> Floating displays does not generate line break.
</td>
</tr>
</table>
</dd></dl>
</dl>
<h3>Strings used in mm</h3>
<dl>
<dt><code>App</code></dt>
<dd>A string containing the word &#8216;APPENDIX&#8217;.</dd>
<dt><code>Apptxt</code></dt>
<dd>The current appendix text.</dd>
<dt><code>EM</code></dt>
<dd>Em dash string</dd>
<dt><code>H1txt</code></dt>
<dd>Updated by <code>.H</code> and <code>.HU</code> to the current heading text. Also updated in table of contents &amp; friends.</dd>
<dt><code>HF</code></dt>
<dd>Font list for headings, &#8216;2 2 2 2 2 2 2&#8217; by default. Non-numeric font names may also be used.</dd>
<dt><code>HP</code></dt>
<dd>Point size list for headings. By default, this is &#8216;0 0 0 0 0 0 0&#8242; which is the same as &#8217;10 10 10 10 10 10 10&#8217;.</dd>
<dt><code>Index</code></dt>
<dd>Contains the string &#8216;INDEX&#8217;.</dd>
<dt><code>Indcmd</code></dt>
<dd>Contains the index command. Default value is &#8216;sort -t	&#8217;.</dd>
<dt><code>Lifg</code></dt>
<dd>String containing &#8216;Figure&#8217;.</dd>
<dt><code>Litb</code></dt>
<dd>String containing &#8216;TABLE&#8217;.</dd>
<dt><code>Liex</code></dt>
<dd>String containing &#8216;Exhibit&#8217;.</dd>
<dt><code>Liec</code></dt>
<dd>String containing &#8216;Equation&#8217;.</dd>
<dt><code>Licon</code></dt>
<dd>String containing &#8216;CONTENTS&#8217;.</dd>
<dt><code>Lf</code></dt>
<dd>Contains the string &#8216;LIST OF FIGURES&#8217;.</dd>
<dt><code>Lt</code></dt>
<dd>Contains the string &#8216;LIST OF TABLES&#8217;.</dd>
<dt><code>Lx</code></dt>
<dd>Contains the string &#8216;LIST OF EXHIBITS&#8217;.</dd>
<dt><code>Le</code></dt>
<dd>Contains the string &#8216;LIST OF EQUATIONS&#8217;.</dd>
<dt><code>Letfc</code></dt>
<dd>Contains the string &#8216;Yours very truly,&#8217;, used in <code>.FC</code>.</dd>
<dt><code>Letapp</code></dt>
<dd>Contains the string &#8216;APPROVED:&#8217;, used in <code>.AV</code>.</dd>
<dt><code>Letdate</code></dt>
<dd>Contains the string &#8216;Date&#8217;, used in <code>.AV</code>.</dd>
<dt><code>LetCN</code></dt>
<dd>Contains the string &#8216;CONFIDENTIAL&#8217;, used in <code>.LO CN</code>.</dd>
<dt><code>LetSA</code></dt>
<dd>Contains the string &#8216;To Whom It May Concern:&#8217;, used in <code>.LO SA</code>.</dd>
<dt><code>LetAT</code></dt>
<dd>Contains the string &#8216;ATTENTION:&#8217;, used in <code>.LO AT</code>.</dd>
<dt><code>LetSJ</code></dt>
<dd>Contains the string &#8216;SUBJECT:&#8217;, used in <code>.LO SJ</code>.</dd>
<dt><code>LetRN</code></dt>
<dd>Contains the string &#8216;In reference to:&#8217;, used in <code>.LO RN</code>.</dd>
<dt><code>Letns</code></dt>
<dd>is an array containing the different strings used in <code>.NS</code>. It is really a number of string variables prefixed with <code>Letns!</code>. If the argument doesn&#8217;t exist, it is included between <code>()</code> with <code>Letns!copy</code> as a prefix and <code>Letns!to</code> as a suffix. Observe the space after &#8216;Copy&#8217; and before &#8216;to&#8217;.</dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td>Letns!0</td>
<td>Copy to
</td>
</tr>
<tr VALIGN=top>
<td>Letns!1</td>
<td>Copy (with att.) to
</td>
</tr>
<tr VALIGN=top>
<td>Letns!2</td>
<td>Copy (without att.) to
</td>
</tr>
<tr VALIGN=top>
<td>Letns!3</td>
<td>Att.
</td>
</tr>
<tr VALIGN=top>
<td>Letns!4</td>
<td>Atts.
</td>
</tr>
<tr VALIGN=top>
<td>Letns!5</td>
<td>Enc.
</td>
</tr>
<tr VALIGN=top>
<td>Letns!6</td>
<td>Encs.
</td>
</tr>
<tr VALIGN=top>
<td>Letns!7</td>
<td>Under separate cover
</td>
</tr>
<tr VALIGN=top>
<td>Letns!8</td>
<td>Letter to
</td>
</tr>
<tr VALIGN=top>
<td>Letns!9</td>
<td>Memorandum to
</td>
</tr>
<tr VALIGN=top>
<td>Letns!10</td>
<td>Copy (with atts.) to
</td>
</tr>
<tr VALIGN=top>
<td>Letns!11</td>
<td>Copy (without atts.) to
</td>
</tr>
<tr VALIGN=top>
<td>Letns!12</td>
<td>Abstract Only to
</td>
</tr>
<tr VALIGN=top>
<td>Letns!13</td>
<td>Complete Memorandum to
</td>
</tr>
<tr VALIGN=top>
<td>Letns!14</td>
<td>CC
</td>
</tr>
<tr VALIGN=top>
<td>Letns!copy</td>
<td>Copy <i>(with trailing space)</i>
</td>
</tr>
<tr VALIGN=top>
<td>Letns!to</td>
<td> to <i>(note leading space)</i>
</td>
</tr>
</table>
</dd></dl>
</dl>
<dt><code>Letnsdef</code></dt>
<dd>Define the standard notation used when no argument is given to <code>.NS</code>. Default is~0.</dd>
<dt><code>MO1 &#8211; MO12</code></dt>
<dd>Strings containing the month names &#8216;January&#8217; through &#8216;December&#8217;.</dd>
<dt><code>Qrf</code></dt>
<dd>String containing &#8216;See chapter \*[Qrfh], page \n[Qrfp].&#8217;.</dd>
<dt><code>Rp</code></dt>
<dd>Contains the string &#8216;REFERENCES&#8217;.</dd>
<dt><code>Tcst</code></dt>
<dd>Contains the current status of the table of contents and list of figures, etc. Empty outside of <code>.TC</code>. Useful in user-defined macros like <code>.TP</code>.</dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>Value</code></td>
<td><code>Meaning</code>
</td>
</tr>
<tr VALIGN=top>
<td>co</td>
<td>Table of contents
</td>
</tr>
<tr VALIGN=top>
<td>fg</td>
<td>List of figures
</td>
</tr>
<tr VALIGN=top>
<td>tb</td>
<td>List of tables
</td>
</tr>
<tr VALIGN=top>
<td>ec</td>
<td>List of equations
</td>
</tr>
<tr VALIGN=top>
<td>ex</td>
<td>List of exhibits
</td>
</tr>
<tr VALIGN=top>
<td>ap</td>
<td>Appendix
</td>
</tr>
</table>
</dd></dl>
</dl>
<dt><code>Tm</code></dt>
<dd>Contains the string &#8216;\(tm&#8217;, the trade mark symbol.</dd>
<dt><code>Verbnm</code></dt>
<dd>Argument to <code>.nm</code> in the <code>.VERBON</code> command. Default is~1.</dd></dl>
<h3>Number variables used in mm</h3>
<dl>
<dt><code>Aph</code></dt>
<dd>Print an appendix page for every new appendix if this number variable is non-zero. No output occurs if <code>Aph</code> is zero, but there is always an appendix entry in the &#8216;List of contents&#8217;.</dd>
<dt><code>Cl</code></dt>
<dd>Contents level (in the range 0 to 14). The contents is saved if a heading level is lower than or equal to the value of <code>Cl</code>. Default is~2.</dd>
<dt><code>Cp</code></dt>
<dd>Eject page between list of table, list of figure, etc., if the value of <code>Cp</code> is zero. Default is~0.</dd>
<dt><code>D</code></dt>
<dd>Debug flag. Values greater than zero produce debug information of increasing verbosity. A value of~1 gives information about the progress of formatting. Default is~0.</dd>
<dt><code>De</code></dt>
<dd>If set to~1, eject after floating display is output. Default is~0.</dd>
<dt><code>Dsp</code></dt>
<dd>If defined, it controls the space output before and after static displays. Otherwise the value of <code>Lsp</code> is used.</dd>
<dt><code>Df</code></dt>
<dd>Control floating keep output. This is a number in the range 0 to 5, with a default value of~5. See <code>.DF</code>.</dd>
<dt><code>Ds</code></dt>
<dd>If set to~1, use the amount of space stored in register <code>Lsp</code> before and after display. Default is~1.</dd>
<dt><code>Ej</code></dt>
<dd>If set to~1, eject page before each first-level heading. Default is~0.</dd>
<dt><code>Eq</code></dt>
<dd>Equation labels are left-adjusted if set to~0 and right-adjusted if set to~1. Default is~0.</dd>
<dt><code>Fs</code></dt>
<dd>Footnote spacing. Default is~1.</dd>
<dt><code>H1 &#8211; H7</code></dt>
<dd>Heading counters</dd>
<dt><code>H1dot</code></dt>
<dd>Append a dot after the level-one heading number if value is greater than zero. Default is~1.</dd>
<dt><code>H1h</code></dt>
<dd>A copy of number register <code>H1</code>, but it is incremented just before the page break. Useful in user-defined header macros.</dd>
<dt><code>Hb</code></dt>
<dd>Heading break level. A number in the range 0 to 14, with a default value of~2. See~<code>.H</code>.</dd>
<dt><code>Hc</code></dt>
<dd>Heading centering level. A number in the range 0 to 14, with a default value value of~0. See~<code>.H</code>.</dd>
<dt><code>Hi</code></dt>
<dd>Heading temporary indent. A number in the range 0 to 2, with a default value of~1.</dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td>0</td>
<td>no indentation, left margin
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td> indent to the right, similar to &#8216;<code>.P 1</code>&#8216;
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td> indent to line up with text part of preceding heading
</td>
</tr>
</table>
</dd></dl>
</dl>
<dt><code>Hps</code></dt>
<dd>Heading pre-space level. If the heading level is less than or equal to <code>Hps</code>, two lines precede the section heading instead of one. Default is first level only. The real amount of lines is controlled by the variables <code>Hps1</code> and <code>Hps2</code>.</dd>
<dt><code>Hps1</code></dt>
<dd>Number of lines preceding <code>.H</code> if the heading level is greater than <code>Hps</code>. Value is in units, default is 0.5.</dd>
<dt><code>Hps2</code></dt>
<dd>Number of lines preceding <code>.H</code> if the heading level is less than or equal to <code>Hps</code>. Value is in units, default is~1.</dd>
<dt><code>Hs</code></dt>
<dd>Heading space level. A number in the range 0 to 14, with a default value of~2. See~<code>.H</code>.</dd>
<dt><code>Hss</code></dt>
<dd>Number of lines following <code>.H</code> if the heading level is less than or equal to <code>Hs</code>. Value is in units, default is~1.</dd>
<dt><code>Ht</code></dt>
<dd>Heading numbering type.</dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td>0</td>
<td>multiple levels (1.1.1, 1.1.2, etc.)
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td>single level
</td>
</tr>
</table>
</dd></dl>
</dl>
<dd>Default is~0.</dd>
<dt><code>Hu</code></dt>
<dd>Unnumbered heading level. Default is~2.</dd>
<dt><code>Hy</code></dt>
<dd>Hyphenation status of text body.</dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td>0</td>
<td>no hyphenation
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td>hyphenation on, set to value~6
</td>
</tr>
</table>
</dd></dl>
</dl>
<dd>Default is~0.</dd>
<dt><code>Iso</code></dt>
<dd>Set this variable to~1 on the command line to get an ISO-formatted date string (<code>-rIso=1</code>). Useless inside of a document.</dd>
<dt><code>L</code></dt>
<dd>Page length, only for command-line settings.</dd>
<dt><code>Letwam</code></dt>
<dd>Maximum lines in return-address, used in <code>.WA</code>/<code>.WE</code>. Default is~14.</dd>
<dt><code>Lf</code>,&nbsp;<code>Lt</code>,&nbsp;<code>Lx</code>,&nbsp;<code>Le</code></dt>
<dd>Enable (1) or disable (0) the printing of List of figures, List of tables, List of exhibits and List of equations, respectively. Default values are Lf=1, Lt=1, Lx=1, and Le=0.</dd>
<dt><code>Li</code></dt>
<dd>List indentation, used by <code>.AL</code>. Default is~6.</dd>
<dt><code>Limsp</code></dt>
<dd>A flag controlling the insertion of space between prefix and mark in automatic lists (<code>.AL</code>).</dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td>0</td>
<td>no space
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td>emit space
</td>
</tr>
</table>
</dd></dl>
</dl>
<dt><code>Ls</code></dt>
<dd>List space threshold. If current list level is greater than <code>Ls</code> no spacing occurs around lists. Default is~99.</dd>
<dt><code>Lsp</code></dt>
<dd>The vertical space used by an empty line. The default is 0.5v in troff mode and 1v in nroff mode.</dd>
<dt><code>N</code></dt>
<dd>Page numbering style.</dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td>0</td>
<td>normal header for all pages.
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td> header replaces footer on first page, header is empty.
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td>page header is removed on the first page.
</td>
</tr>
<tr VALIGN=top>
<td>3</td>
<td>&#8216;section-page&#8217; numbering style enabled.
</td>
</tr>
<tr VALIGN=top>
<td>4</td>
<td>page header is removed on the first page.
</td>
</tr>
<tr VALIGN=top>
<td>5</td>
<td> &#8216;section-page&#8217; and &#8216;section-figure&#8217; numbering style enabled.
</td>
</tr>
</table>
</dd></dl>
</dl>
<dd>Default is~0. See also the number registers <code>Sectf</code> and <code>Sectp</code>.</dd>
<dt><code>Np</code></dt>
<dd>A flag to control whether paragraphs are numbered.</dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td>0</td>
<td>not numbered
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td>numbered in first-level headings.
</td>
</tr>
</table>
</dd></dl>
</dl>
<dd>Default is~0.</dd>
<dt><code>O</code></dt>
<dd>Page offset, only for command-line settings.</dd>
<dt><code>Of</code></dt>
<dd>Format of figure, table, exhibit, and equation titles.</dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td>0</td>
<td>&quot;. &quot;
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td>&quot; &#8211; &quot;
</td>
</tr>
</table>
</dd></dl>
</dl>
<dd>Default is~0.</dd>
<dt><code>P</code></dt>
<dd>Current page-number, normally the same as &#8216;%&#8217; unless &#8216;section-page&#8217; numbering style is enabled.</dd>
<dt><code>Pi</code></dt>
<dd>Paragraph indentation. Default is~5.</dd>
<dt><code>Pgps</code></dt>
<dd>A flag to control whether header and footer point size should follow the current settings or just change when the header and footer are defined.</dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td>0</td>
<td> Point size only changes to the current setting when <code>.PH</code>, <code>.PF</code>, <code>.OH</code>, <code>.EH</code>, <code>.OF</code>, or <code>.OE</code> is executed.
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td> Point size changes after every <code>.S</code>. This is the default.
</td>
</tr>
</table>
</dd></dl>
</dl>
<dt><code>Ps</code></dt>
<dd>Paragraph spacing. Default is~1.</dd>
<dt><code>Pt</code></dt>
<dd>Paragraph type.</dd>
<dl>
<dd>
</dd><dl>
<dd>
<table>
<tr VALIGN=top>
<td>0</td>
<td>left-justified
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td>indented paragraphs
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td> indented paragraphs except after <code>.H</code>, <code>.DE</code>, or <code>.LE</code>.
</td>
</tr>
</table>
</dd></dl>
</dl>
<dd>Default is~0.</dd>
<dt><code>Rpe</code></dt>
<dd>Set default value for second argument of <code>.RP</code>. Default is~0.</dd>
<dt><code>Sectf</code></dt>
<dd>A flag controlling &#8216;section-figures&#8217; numbering style. A non-zero value enables this. See also register~<code>N</code>.</dd>
<dt><code>Sectp</code></dt>
<dd>A flag controlling &#8216;section-page&#8217; numbering style. A non-zero value enables this. See also register~<code>N</code>.</dd>
<dt><code>Si</code></dt>
<dd>Display indentation. Default is~5.</dd>
<dt><code>Verbin</code></dt>
<dd>Indentation for <code>.VERBON</code>. Default is 5n.</dd>
<dt><code>W</code></dt>
<dd>Line length, only for command-line settings.</dd>
<dt><code>.mgm</code></dt>
<dd>Always~1.</dd></dl>
<h2>Internals</h2>
<p>The letter macros are using different submacros depending on the letter type. The name of the submacro has the letter type as suffix. It is therefore possible to define other letter types, either in the national macro-file, or as local additions. <code>.LT</code> sets the number variables <code>Pt</code> and <code>Pi</code> to 0 and~5, respectively. The following strings and macros must be defined for a new letter type.</p>
<dl>
<dt><code>let [at] init_</code><i>type</i></dt>
<dd>This macro is called directly by <code>.LT</code>. It is supposed to initialize variables and other stuff.</dd>
<dt><code>let [at] head_</code><i>type</i></dt>
<dd>This macro prints the letter head, and is called instead of the normal page header. It is supposed to remove the alias <code>let [at] header</code>, otherwise it is called for all pages.</dd>
<dt><code>let@sg_</code><i>type name title n flag </i>[arg1 [arg2 [&#8230;]]]</dt>
<dd><code>.SG</code> is calling this macro only for letters; memorandums have its own processing. <i>name</i> and <i>title</i> are specified through <code>.WA</code>/<code>.WB</code>. <i>n</i>~is the counter, 1-max, and <i>flag</i> is true for the last name. Any other argument to <code>.SG</code> is appended.</dd>
<dt><code>let@fc_</code><i>type closing</i></dt>
<dd>This macro is called by <code>.FC</code>, and has the formal closing as the argument.</dd></dl>
<p> <code>.LO</code> is implemented as a general option-macro. It demands that a string named <code>Let</code><i>type</i> is defined, where <i>type</i> is the letter type. <code>.LO</code> then assigns the argument to the string variable <code>let*lo-</code><i>type</i>.</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/:share/:groff/:1.22.4/:tmac/m.tmac</i></dt>
<dd>
</dd><dt><i>/usr/share/groff/1.22.4/tmac/mm/</i>*<i>.cov</i></dt>
<dd>
</dd><dt><i>/usr/share/groff/1.22.4/tmac/mm/</i>*<i>.MT</i></dt>
<dd>
</dd><dt><i>/usr/share/groff/1.22.4/tmac/mm/locale</i></dt>
<dd></dd></dl>
<h2>Authors</h2>
<p>The GNU version of the <i>mm</i> macro package was written by J&ouml;rgen H&auml;gg of Lund, Sweden.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1), <code><a href="/docs/linux/man/1-tbl/">tbl</a></code>(1), <code><a href="/docs/linux/man/1-pic/">pic</a></code>(1), <code><a href="/docs/linux/man/1-eqn/">eqn</a></code>(1)<br/>
 <code><a href="/docs/linux/man/7-groff_mmse/">groff_mmse</a></code>(7) (only in Swedish locales) </p>
