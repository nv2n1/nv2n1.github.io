---
title: "groff_man(7)"
name: "groff_man"
section: "7"
letter: "g"
url: "/docs/linux/man/7-groff_man/"
description: "groff_man – GNU roff macro package for formatting man pages"
---

<p>groff_man &#8211; GNU roff macro package for formatting man pages</p>
<h2>Synopsis</h2>
<p>[<i>option</i> &#8230;] [<i>input-file</i> &#8230;] [<i>option</i> &#8230;] [<i>input-file</i> &#8230;]</p>
<h2>Description</h2>
<p>The <i>man</i> macro package for <i>groff</i> is used to produce manual pages (&#8220;man~pages&#8221;) like the one you are reading. GNU <i>roff</i>&#8216;s implementation was written by James Clark. This document presents the macros thematically to aid learners; for those needing only a quick reference, the following table lists them alphabetically, with cross-references to appropriate subsections below. </p>
<table>
<tr VALIGN=top>
<td>Macro</td>
<td>Meaning</td>
<td>Subsection
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>.B</code></td>
<td>Bold</td>
<td>Font style macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.BI</code></td>
<td>Bold, italic alternating</td>
<td>Font style macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.BR</code></td>
<td>Bold, roman alternating</td>
<td>Font style macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.EE</code></td>
<td>Example end</td>
<td>Document structure macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.EX</code></td>
<td>Example begin</td>
<td>Document structure macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.I</code></td>
<td>Italic</td>
<td>Font style macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.IB</code></td>
<td>Italic, bold alternating</td>
<td>Font style macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.IP</code></td>
<td>Indented paragraph</td>
<td>Paragraph macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.IR</code></td>
<td>Italic, roman alternating</td>
<td>Font style macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.LP</code></td>
<td>(Left) paragraph</td>
<td>Paragraph macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.ME</code></td>
<td>Mail-to end</td>
<td>Hyperlink and email macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.MT</code></td>
<td>Mail-to start</td>
<td>Hyperlink and email macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.OP</code></td>
<td>(Command-line) option</td>
<td>Command synopsis macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.P</code></td>
<td>Paragraph</td>
<td>Paragraph macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.PP</code></td>
<td>Paragraph</td>
<td>Paragraph macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.RB</code></td>
<td>Roman, bold alternating</td>
<td>Font style macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.RE</code></td>
<td>Relative-indent end</td>
<td>Document structure macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.RI</code></td>
<td>Roman, italic alternating</td>
<td>Font style macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.RS</code></td>
<td>Relative-indent start</td>
<td>Document structure macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.SB</code></td>
<td>Small bold</td>
<td>Font style macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.SH</code></td>
<td>Section heading</td>
<td>Document structure macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.SM</code></td>
<td>Small</td>
<td>Font style macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.SS</code></td>
<td>Subection heading</td>
<td>Document structure macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.SY</code></td>
<td>Synopsis start</td>
<td>Command synopsis macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.TH</code></td>
<td>Title heading</td>
<td>Document structure macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.TP</code></td>
<td>Tagged paragraph</td>
<td>Paragraph macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.TQ</code></td>
<td>Tagged paragraph continuation</td>
<td>Paragraph macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.UE</code></td>
<td>URL end</td>
<td>Hyperlink and email macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.UR</code></td>
<td>URL start</td>
<td>Hyperlink and email macros
</td>
</tr>
<tr VALIGN=top>
<td><code>.YS</code></td>
<td>Synopsis end</td>
<td>Command synopsis macros
</td>
</tr>
</table>
<p> Macros whose use we discourage (<code>.AT</code>, <code>.BT</code>, <code>.DT</code>, <code>.HP</code>, <code>.PD</code>, <code>.PT</code>, and <code>.UC</code>) are described in subsection &#8220;Deprecated features&#8221;, below.</p>
<h3>Macro reference preliminaries</h3>
<p>Each macro is described in a tagged paragraph. Closely related macros, such as <code>.EX</code> and <code>.EE</code>, are grouped together. Optional macro arguments are indicated by surrounding them with square brackets. If a macro accepts multiple arguments, arguments containing whitespace must be double-quoted (&quot;one two&quot;), to be interpreted correctly. Most macro arguments are strings that will be output as text; exceptions are noted. Bear in mind that <i>groff</i> is fundamentally a programming system for typesetting. Consequently, the verb &#8220;to set&#8221; is frequently used below in the sense &#8220;to typeset&#8221;.</p>
<h3>Document structure macros</h3>
<p>The highest level of organization of a man page is determined by this group of macros. <code>.TH</code> (title heading) identifies the document as a man page and defines information enabling its indexing by <i><a href="/docs/linux/man/8-mandb/">mandb</a></i>(8) or a similar tool. Sections (<code>.SH</code>), one of which is mandatory and many of which are standardized, facilitate quick location of relevant material by the reader and aid the man page writer to discuss all essential aspects of the topic. Subsections (<code>.SS</code>) are optional and permit sections that grow long to develop in a controlled way. Many technical discussions require examples; lengthy ones, especially those reflecting multiple lines of input to or output from the system, are usefully bracketed by <code>.EX</code> and <code>.EE</code>. When none of the foregoing meets a structural demand, a section of the discussion can be manually indented within <code>.RS</code> and <code>.RE</code> macros.</p>
<dl>
<dt><code>.TH</code><i> title section</i></dt>
<dd>[<i>footer-middle</i>] [<i>footer-outside</i>] [<i>header-middle</i>] Define the title of the man page as <i>title</i> and the section as <i>section</i>. See <i><a href="/docs/linux/man/1-man/">man</a></i>(1) for details on the section numbers and suffixes applicable to your system. <i>title</i> and <i>section</i> are positioned together at the left and right in the header line (with <i>section</i> in parentheses immediately appended to <i>title</i>). <i>footer-middle</i> is centered in the footer line. <i>footer-outside</i> is positioned at the left in the footer line (or at the left on even pages and at the right on odd pages if double-sided printing is active). <i>header-middle</i> is centered in the header line. If <i>section</i> is a simple integer between 1 and~9 (inclusive), or is exactly &#8220;3p&#8221;, there is no need to specify <i>header-middle</i>; the macro package will supply text for it.</dd>
<dd>For HTML output, headers and footers are completely suppressed.</dd>
<dd>Additionally, this macro starts a new page; the page number is reset to~1 (unless the <code>-rC1</code> option is given on the command line). This feature is intended only for formatting multiple man pages.</dd>
<dd>A man page should contain exactly one <code>.TH</code> call at or near the beginning of the file, prior to any other macro calls.</dd>
<dd>By convention, <i>footer-middle</i> is the most recent modification date of the man page source document, and <i>footer-outside</i> is the name and version or release of the project providing it.</dd>
<dt><code>.SH</code> [</dt>
<dd><i>heading-text</i>] Set <i>heading-text</i> as a section heading flush left. The text following <code>.SH</code> up to the end of the line, or the text on the next input line if <code>.SH</code> is given no arguments, is set in bold (or the font specified by the string register <code>HF</code>) slightly larger than the base font size. Additionally, the left margin and indentation affecting subsequent text are reset to their default values. Text on input lines after <i>heading-text</i> is set as a normal paragraph (<code>.PP</code>).</dd>
<dd>The content of <i>heading-text</i> and ordering of sections has been standardized by common practice, as has much of the layout of material within sections. For example, a section called &#8220;Name&#8221; or &#8220;NAME&#8221; must exist, must be the first section after the <code>.TH</code> call, and must contain only a line of the form</dd>
<dl>
<dd>&quot; Invisibly move left margin to current .IP indent.</dd>
<dl>
<dd>&quot; Now indent further, visibly. <i>page-topic</i>[<code>,</code> &#8230;] <code>\-&nbsp;</code><i>summary-description</i></dd></dl>
<p> for a man page to be properly indexed. See <i><a href="/docs/linux/man/7-man/">man</a></i>(7) for the conventions prevailing on your system.</dl>
<dt><code>.SS</code> [</dt>
<dd><i>subheading-text</i>] Set <i>subheading-text</i> as a subsection heading indented (by default) partway between a section heading and a normally-indented paragraph (<code>.PP</code>). The text following <code>.SS</code> up to the end of the line, or the text on the next input line if <code>.SS</code> is given no arguments, is set in bold (or the font specified by the string register <code>HF</code>) at the base font size. Additionally, the left margin and indentation affecting subsequent text are reset to their default values. Text on input lines after <i>subheading-text</i> is set as a normal paragraph (<code>.PP</code>).</dd>
<dt><code>.EX</code></dt>
<dd><code>.EE</code> Begin and end example. After <code>.EX</code>, filling and hyphenation are disabled and a constant-width (monospaced) font is selected. Calling <code>.EE</code> enables filling and restores the previous hyphenation setting and font.</dd>
<dd>Example regions are useful for formatting code, shell sessions, and text file contents.</dd>
<dd>These macros are defined on many (but not all) legacy Unix systems running classic <i>troff</i>. To be certain your page will be portable to those systems, copy their definitions from the <i>an-ext.tmac</i> file of a <i>groff</i> installation.</dd>
<dt><code>.RS</code> [</dt>
<dd><i>indent</i>] Move the left margin to the right by the value <i>indent</i>, if specified, and by a default amount otherwise; see subsection &#8220;Horizontal and vertical spacing&#8221; below. Calls to <code>.RS</code> can be nested; each call increments by~1 the indentation level used by <code>.RE</code>. The indentation level prior to any <code>.RS</code> calls is~1.</dd>
<dt><code>.RE</code> [</dt>
<dd><i>level</i>] Move the left margin back to that corresponding to indentation level <i>level</i>. If no argument is given, move the left margin one level back.</dd></dl>
<h3>Paragraph macros</h3>
<p>A typical paragraph (<code>.PP</code>) is set at the current left margin, which by default is indented from the left margin of the output device. In man pages and other technical literature, definition lists are frequently encountered; these can be set as &#8220;tagged paragraphs&#8221; (<code>.TP</code> and <code>.TQ</code>), which have one or more leading tags followed by a paragraph that has an additional left indent. The indented paragraph (<code>.IP</code>) macro is useful to continue the indented content of a narrative started with <code>.TP</code>, or to present an itemized or ordered list.</p>
<dl>
<dt><code>.LP</code></dt>
<dd><code>.PP</code> <code>.P</code> Begin a new paragraph; these macros are synonymous. They break the output line at the current position, followed by a vertical space downward by a default amount (which can be changed by the deprecated <code>.PD</code> macro). The font size and style are reset to defaults; see subsection &#8220;Font style macros&#8221; below. Finally, the left margin and indentation are reset to default values.</dd>
<dt><code>.TP</code> [</dt>
<dd><i>indent</i>] Set a tagged, indented paragraph. The input line following this macro, known as the <i>tag</i>, is printed at the current left margin. Subsequent text is indented by <i>indent</i>, if specified, and by a default amount otherwise; see subsection &#8220;Horizontal and vertical spacing&#8221; below.</dd>
<dd>If the tag is not as wide as the indentation, the paragraph starts on the same line as the tag, at the applicable indentation, and continues on the following lines. Otherwise, the descriptive part of the paragraph begins on the line following the tag, entirely indented. The line containing the tag can include a macro call, for instance to set the tag in bold with <code>.B</code>.</dd>
<dd><code>.TP</code> was used to write the first paragraph of this description of <code>.TP</code>, and <code>.IP</code> the subsequent ones.</dd>
<dt><code>.TQ</code></dt>
<dd>Set an additional tag for a paragraph tagged with <code>.TP</code>. The pending output line is broken. The tag on the input line following this macro and subsequent lines are handled as with <code>.TP</code>.</dd>
<dd>This macro is not defined on legacy Unix systems running classic <i>troff</i>. To be certain your page will be portable to those systems, copy its definition from the <i>an-ext.tmac</i> file of a <i>groff</i> installation.</dd>
<dd>The descriptions of <code>.LP</code>, <code>.PP</code>, and <code>.P</code> above were written using <code>.TP</code> and <code>.TQ</code>.</dd>
<dt><code>.IP</code> [</dt>
<dd><i>tag</i>] [<i>indent</i>] Set an indented paragraph with an optional tag. The <i>tag</i> and <i>indent</i> arguments, if present, are handled as with <code>.TP</code>, with the exception that the <i>tag</i> argument to <code>.IP</code> cannot include a macro call.</dd>
<dd>Two convenient use cases for <code>.IP</code> are</dd>
<dl>
<dd>&quot; Invisibly move left margin to current .IP indent.</dd>
<dl>
<dd>&quot; Now indent further, visibly.</dd>
<dl>
<dt>(1)</dt>
<dd>to start a new paragraph with the same indentation as the previous <code>.IP</code> or <code>.TP</code> paragraph, if no <i>indent</i> argument is given; and</dd>
<dt>(2)</dt>
<dd>to set a paragraph with a short <i>tag</i> that is not semantically important, such as a bullet (&bull;)&#8212;obtained with the &#8216;\(bu&#8217; character escape&#8212;or list enumerator, as seen in this very paragraph.</dd></dl>
</dl>
</dl>
</dl>
<h3>Command synopsis macros</h3>
<p>Command synopses are a staple of section~1 and~8 man pages. These macros aid you to construct one that has the classical Unix appearance. Furthermore, some tools are able to interpret these macros semantically and treat them appropriately for localization and/or presentation. A command synopsis is wrapped in <code>.SY</code>/<code>.YS</code> calls, with command-line options of some formats indicated by <code>.OP</code>. These macros are not defined on legacy Unix systems running classic <i>troff</i>. To be certain your page will be portable to those systems, copy their definitions from the <i>an-ext.tmac</i> file of a <i>groff</i> installation.</p>
<dl>
<dt><code>.SY</code><i> command</i></dt>
<dd>Begin synopsis. Hyphenation is turned off. The <i>command</i> argument is set in bold. The output line is filled as normal, but if a break is required, subsequent output lines are indented by the width of <i>command</i> plus a space.</dd>
<dt><code>.OP</code><i> option-name/</i></dt>
<dd>[<i>option-argument</i>] Indicate an optional command parameter called <i>option-name</i>, which is set in bold. If the option takes an argument, specify <i>option-argument</i> using a noun, abbreviation, or hyphenated noun phrase. If present, <i>option-argument</i> is preceded by a space and set in italics. Square brackets (in roman) surround both arguments.</dd>
<dt><code>.YS</code></dt>
<dd>End synopsis. Restore indentation and hyphenation to previous values.</dd></dl>
<p> Multiple <code>.SY/.YS</code> blocks can be specified, for instance to distinguish differing modes of operation of a complex command like <i><a href="/docs/linux/man/1-tar/">tar</a></i>(1); each will be separated by a paragraph space. <code>.SY</code> can also be repeated multiple times before a closing <code>.YS</code>, which is useful to indicate synonymous ways of invoking a particular mode of operation. For example,</p>
<dl>
<dd>.SY groff .OP \-abcegiklpstzCEGNRSUVXZ .OP \-d cs .OP \-f fam .OP \-F dir .OP \-I dir .OP \-K arg .OP \-L arg .OP \-m name .OP \-M dir .OP \-n num .OP \-o list .OP \-P arg .OP \-r cn .OP \-T dev .OP \-w name .OP \-W name .RI [ file \&amp;.\|.\|.\&amp;] .YS . .SY groff .B \-h .SY groff .B \-\-help .YS</dd>
<dd> produces the following output.</dd>
<dl>
<dd>[ <code>-abcegiklpstzCEGNRSUVXZ</code> ] [ <code>-d </code><i>cs</i> ] [ <code>-f </code><i>fam</i> ] [ <code>-F </code><i>dir</i> ] [ <code>-I </code><i>dir</i> ] [ <code>-K </code><i>arg</i> ] [ <code>-L </code><i>arg</i> ] [ <code>-m </code><i>name</i> ] [ <code>-M </code><i>dir</i> ] [ <code>-n </code><i>num</i> ] [ <code>-o </code><i>list</i> ] [ <code>-P </code><i>arg</i> ] [ <code>-r </code><i>cn</i> ] [ <code>-T </code><i>dev</i> ] [ <code>-w </code><i>name</i> ] [ <code>-W </code><i>name</i> ] [<i>file</i> &#8230;] <code>-h</code> <code>&#8211;help</code></dd></dl>
<p> Several features of the above example are of note.</p>
<dl>
<dt>&bull;</dt>
<dd>The empty request (.), which does nothing, is used for vertical spacing in the input file for readability by the document maintainer. Do not put empty lines in a <i>roff</i> source document.</dd>
<dt>&bull;</dt>
<dd>The command and option names are presented in <code>bold</code> to cue the user that they should be input literally.</dd>
<dt>&bull;</dt>
<dd>Option dashes are specified with the &#8216;\-&#8216; escape sequence; this is an important practice to make them clearly visible and to facilitate cut-and-paste from the rendered man page to a shell prompt or text file.</dd>
<dt>&bull;</dt>
<dd>Option arguments and command operands are presented in <i>italics</i> (underlined on some output devices, such as terminals and emulators), to cue the user that they must be replaced with appropriate text.</dd>
<dt>&bull;</dt>
<dd>Symbols that are neither to be typed literally nor simply replaced appear in the roman style; brackets surround optional arguments, and an ellipsis indicates that the previous syntactical element may be repeated arbitrarily.</dd>
<dd>Some man pages use a brace-and-pipe notation such as &#8220;{<code>&#8211;diff</code>|<code>&#8211;compare</code>}&#8221; to indicate that one and only one of the &#8216;|&#8217;-separated items within the braces must be input. If this braced construct is furthermore surrounded by square brackets, it means that at most one of the items is accepted.</dd>
<dd>Authors of man pages should note the use of the zero-width space escape sequence &#8216;\&amp;&#8217; on both sides of the ellipsis; this is a good practice to avoid surprises in the event the ellipsis gets refilled in your text editor. See &#8220;Portability&#8221;, below. The morbidly curious may consult <i><a href="/docs/linux/man/7-groff/">groff</a></i>(7) regarding the narrow-space escape sequence &#8216;\|&#8217;.</dd></dl>
<h3>Hyperlink and email macros</h3>
<p>Email addresses are bracketed with <code>.MT</code>/<code>.ME</code> and URL hyperlinks with <code>.UR</code>/<code>.UE</code>. These macros are not defined on legacy Unix systems running classic <i>troff</i>. To be certain your page will be portable to those systems, copy their definitions from the <i>an-ext.tmac</i> file of a <i>groff</i> installation.</p>
<dl>
<dt><code>.MT</code><i> address</i></dt>
<dd><code>.ME</code> [<i>punctuation</i>] Identify <i>address</i> as an RFC 6068 <i>addr-spec</i> for a &#8220;mailto:&#8221; URI with the text between the two macro calls as the link text. A <i>punctuation</i> argument to <code>.ME</code> is placed at the end of the link text without intervening space. Note that <i>address</i> may not be visible in the output text, particularly if the man page is being viewed as HTML. On a device that is not a browser, <i>address</i> is set in angle brackets after the link text and before <i>punctuation</i>.</dd>
<dd>When rendered by <i>groff</i> to a TTY or PostScript output device,</dd>
<dl>
<dd>
</dd><dl>
<dd>Contact .MT fred.foonly@\:fubar.net Fred Foonly .ME for more information.</dd></dl>
</dl>
<dd>displays as: &#8220;Contact Fred Foonly &lt;fred.foonly@:fubar.net&gt; for more information.&#8221;.</dd>
<dd>The use of &#8216;\:&#8217; to insert hyphenless discretionary breaks is a <i>groff</i> extension and can be omitted.</dd>
<dt><code>.UR</code><i> URL</i></dt>
<dd><code>.UE</code> [<i>punctuation</i>] Identify <i>URL</i> as an RFC 3986 URI hyperlink with the text between the two macro calls as the link text. A <i>punctuation</i> argument to <code>.UE</code> is placed at the end of the link text without intervening space. Note that <i>URL</i> may not be visible in the output text, particularly if the man page is being viewed as HTML. On a device that is not a browser, <i>URL</i> is set in angle brackets after the link text and before <i>punctuation</i>.</dd>
<dd>When rendered by <i>groff</i> to a TTY or PostScript output device,</dd>
<dl>
<dd>
</dd><dl>
<dd>The GNU Project of the Free Software Foundation hosts the .UR <a rel="nofollow" href="https://\:www.gnu.org/\:software/\:groff/">https://\:www.gnu.org/\:software/\:groff/</a> Groff home page .UE .</dd></dl>
</dl>
<dd>displays as: &#8220;The GNU Project of the Free Software Foundation hosts the Groff home page &lt;<a rel="nofollow" href="https://:www.gnu.org/:software/:groff/">https://:www.gnu.org/:software/:groff/</a>&gt;.&#8221;.</dd>
<dd>The use of &#8216;\:&#8217; to insert hyphenless discretionary breaks is a <i>groff</i> extension and can be omitted.</dd></dl>
<h3>Font style macros</h3>
<p>The <i>man</i> macro package is limited in its font styling options, offering only <code>bold</code>~(<code>.B</code>), <i>italic</i>~(<code>.I</code>), and roman (the default). Italic text is usually set underscored instead on terminals and other classical <i>nroff</i>-style output devices. The <code>.SM</code> and <code>.SB</code> macros set text in roman or bold, respectively, at a smaller point size; these differ visually from regular-sized roman or bold text only on <i>troff</i>-style output devices. The foregoing macros cause word breaks before and after their arguments, but it is often necessary to set text in different styles without intervening whitespace. The macros <code>.BI</code>, <code>.BR</code>, <code>.IB</code>, <code>.IR</code>, <code>.RB</code>, and <code>.RI</code>, where &#8216;B&#8217;, &#8216;I&#8217;, and &#8216;R&#8217; indicate bold, italic, and roman, respectively, set their odd- and even-numbered arguments in alternating styles, with no whitespace separating them. Because font styles are presentational rather than semantic, conflicting traditions have arisen regarding which font styles should be used to mark file or path names, environment variables, in-line literals, and even man page cross-references. The default font size and family (for <i>troff</i> output devices) is 10-point Times. The default style is roman.</p>
<dl>
<dt><code>.B</code>~[</dt>
<dd><i>text</i>] Set <i>text</i> in bold. If the macro is given no arguments, the text of the next input line is set in bold.</dd>
<dd>Use bold for literal portions of syntax synopses, for command-line options in running text, and for literals that are major topics of the subject under discussion; for example, this page uses bold for macro and register names. In <code>.EX</code>/<code>.EE</code> examples of interactive I/O (such as a shell session), set only the user-typed input in bold.</dd>
<dt><code>.I</code>~[</dt>
<dd><i>text</i>] Set <i>text</i> in italics. If the macro is given no arguments, the text of the next input line is set in italics.</dd>
<dd>Use italics for file and path names, for environment variables, for enumeration or preprocessor constants in C, for variable (user-determined) portions of syntax synopses, for the first occurrence only of a technical concept being introduced, for names of works of software (including commands and functions, but excluding names of operating systems or their kernels), and anywhere a parameter requiring replacement by the user is encountered. An exception involves variable text in a context that is already marked up in italics, such as file or path names with variable components; in such cases, follow the convention of mathematical typography: set the file or path name in italics as usual (see <code>.IR</code> below), but use roman for the variable part, and italics again in running roman text when referring to the variable material.</dd>
<dt><code>.SM</code>~[</dt>
<dd><i>text</i>] Set <i>text</i> one point size smaller than the default size. If the macro is given no arguments, the text of the next input line is set smaller.</dd>
<dd><i>Note</i>: <i>nroff</i>-style output devices, such as terminals, will render <i>text</i> at the normal font size instead. Do not rely upon <code>.SM</code> to communicate semantic information distinct from using roman style at the normal size; it will be hidden from readers using such devices.</dd>
<dt><code>.SB</code>~[</dt>
<dd><i>text</i>] Set <i>text</i> in bold, one point size smaller than the default size. If the macro is given no arguments, the text of the next input line is set smaller and in bold.</dd>
<dd><i>Note</i>: <i>nroff</i>-style output devices, such as terminals, will render <i>text</i> in bold at the normal font size instead. Do not rely upon <code>.SB</code> to communicate semantic information distinct from using bold style at the normal size; it will be hidden from readers using such devices.</dd></dl>
<p> Note what is <i>not</i> prescribed for setting in bold or italics above: elements of &#8220;synopsis language&#8221; such as ellipses and brackets around options; proper names and adjectives; titles of anything other than works of literature or software; identifiers for standards documents or technical reports such as CSTR~#54, RFC~1918, Unicode~11.0, or POSIX.1-2017; acronyms; and occurrences after the first of a technical term or piece of jargon. Again, the names of operating systems and their kernels are, by practically universal convention, set in roman. Be frugal with the use of italics for emphasis, and particularly with the use of bold. Brief runs of literal text, such as references to individual characters or short strings, including section and subsection headings of man pages, are suitable objects for quotation; see the &#8216;\(lq&#8217;, &#8216;\(rq&#8217;, &#8216;\(oq&#8217;, and &#8216;\(cq&#8217; escapes in subsection &#8220;Portability&#8221; below. Unlike the above font style macros, the font alternation macros below accept only arguments on the same line as the macro call. If whitespace is required within one of the arguments, first consider whether the same result could be achieved with as much clarity by using the single-style macros on separate input lines. When it cannot, double-quote an argument with one or more embedded space characters. Setting all three different styles within one whitespace-delimited word presents challenges; it is possible with the &#8216;\c&#8217; and/or &#8216;\f&#8217; escapes, but see subsection "Portability" below for caveats. </p>
<dl>
<dt><code>.BI</code><i> bold-text italic-text</i></dt>
<dd> <p> ~... Set each argument in bold and italics, alternately. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> .BI \-r name = n </p>
 </dd></dl>
</dl>
<dt><code>.BR</code><i> bold-text roman-text</i></dt>
<dd> <p> ~... Set each argument in bold and roman, alternately. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> Any such change becomes effective with the first use of .BR .NH , .I after the new alias is defined. </p>
 </dd></dl>
</dl>
<dt><code>.IB</code><i> italic-text bold-text</i></dt>
<dd> <p> ~... Set each argument in italics and bold, alternately. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> All macro package files must be named .IB name .tmac to fully use the .I tmac mechanism. </p>
 </dd></dl>
</dl>
<dt><code>.IR</code><i> italic-text roman-text</i></dt>
<dd> <p> ~... Set each argument in italics and roman, alternately. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> This is the first command of the .IR prologue . </p>
 </dd></dl>
</dl>
<dt><code>.RB</code><i> roman-text bold-text</i></dt>
<dd> <p> ~... Set each argument in roman and bold, alternately. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> Also, the statement .RB \(oq &quot;delim on&quot; \(cq is not handled specially. </p>
 </dd></dl>
</dl>
<dt><code>.RI</code><i> roman-text italic-text</i></dt>
<dd> <p> ~... Set each argument in roman and italics, alternately. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> .RI [ file \&amp;.\|.\|.\&amp;] </p>
 </dd></dl>
</dl>
</dl>
<h3>Horizontal and vertical spacing</h3>
<p> The <i>indent</i> argument accepted by <code>.RS</code>, <code>.IP</code>, <code>.TP</code>, and the deprecated <code>.HP</code> is a number plus an optional scaling indicator. If no scaling indicator is given, the <i>man</i> package assumes &#8216;n&#8217;; that is, the width of a letter "n" in the font current when the macro is called. See section "Numerical Expressions" in <i><a href="/docs/linux/man/7-groff/">groff</a></i>(7) for further details. An indent specified in a call to <code>.IP</code>, <code>.TP</code>, or the deprecated <code>.HP</code> persists until (1) another of these macros is called with an explicit indent argument, or (2) <code>.SH</code>, <code>.SS</code>, or <code>.PP</code> or its synonyms is called; these clear the indent entirely. </p>
<p> Indents set by <code>.RS</code> move the left margin and persist until <code>.RS</code>, <code>.RE</code>, <code>.SH</code>, or <code>.SS</code> is called. The default indentation, exhibited by ordinary <code>.PP</code> paragraphs not within an <code>.RS</code>/<code>.RE</code> relative indent, is 7.2n in <i>troff</i> mode and 7n in <i>nroff</i> mode. The HTML output device is an exception; it ignores indentation completely. This same indentation is used again (additively) for the defaults of <code>.IP</code>, <code>.TP</code>, <code>.RS</code>, and the deprecated <code>.HP</code>. Section headings (<code>.SH</code>) are set flush with the left margin of the output device, and subsection headings (<code>.SS</code>) are indented 3n. </p>
<p> Resist the temptation to mock up tabular or multi-column output with ASCII tab characters or the indentation arguments to <code>.IP</code>, <code>.TP</code>, <code>.RS</code>, or the deprecated <code>.HP</code>; the result may not render comprehensibly on an output device you fail to check, or which is developed in the future. The table preprocessor <i><a href="/docs/linux/man/1-tbl/">tbl</a></i>(1) can likely meet your needs. </p>
<p> The following macros cause a line break with the insertion of vertical space: <code>.SH</code>, <code>.SS</code>, <code>.TP</code>, <code>.TQ</code>, <code>.PP</code> (and its synonyms), <code>.IP</code>, and the deprecated <code>.HP</code>. The default inter-section and inter-paragraph spacing is 1~line in <i>nroff</i> mode, and 0.4v in <i>troff</i> mode. (The deprecated macro <code>.PD</code> can change this vertical spacing, but its use is discouraged.) The macros <code>.RS</code>, <code>.RE</code>, <code>.EX</code>, and <code>.EE</code> also cause a break but no insertion of vertical space.  </p>
<h3>Number registers</h3>
<p> Number registers are described in section "Options" below.  </p>
<h3>String registers</h3>
<p> The following strings are defined. </p>
<dl>
<dt><code>\*R</code></dt>
<dd> <p> expands to the character escape for the "registered sign" glyph, &#8216;\(rg&#8217;, if available, and "(Reg.)" otherwise. </p>
 </dd>
<dt><code>\*S</code></dt>
<dd> <p> expands to an escape setting the font size to the document default. </p>
 </dd>
<dt><code>\*(HF</code></dt>
<dd> <p> expands to the font identifier used to print headings and subheadings. The default is &#8216;B&#8217;. </p>
 </dd>
<dt><code>\*(lq</code></dt>
<dd> <p> <code>\*(rq</code> expand to the character escapes for left and right double-quotation marks, &#8216;\(lq&#8217; and &#8216;\(rq&#8217;, respectively. </p>
 </dd>
<dt><code>\*(Tm</code></dt>
<dd> <p> expands to the character escape for the "trade mark sign" glyph, &#8216;\(tm&#8217;, if available, and "(TM)" otherwise. </p>
 </dd></dl>
<h3>Interaction with preprocessors</h3>
<p> When a preprocessor like <i>tbl</i> or <i>eqn</i> is needed, a hint can be given to the man page formatter by making the first line of a man page look like this: </p>
<dl>
<dd> <p> <code>&#8216;\&quot; </code><i>word</i> </p>
 </dd></dl>
<p> Note that the line starts with an apostrophe (&#8216;), not a dot, and that a single space character follows the double quote. The <i>word</i> consists of one letter for each needed preprocessor: &#8216;e&#8217; for <i>eqn</i>, &#8216;r&#8217; for <i>refer</i>, and &#8216;t&#8217; for <i>tbl</i>. Modern implementations of the <i>man</i> program interpret this first line and automatically call the right preprocessor(s). </p>
<p> The usual <i>tbl</i> and <i>eqn</i> macros for table and equation inclusion, <code>.TS</code>, <code>.T&amp;</code>, <code>.TE</code>, <code>.EQ</code>, and <code>.EN</code>, may be used freely. Note that <i>nroff</i> output devices are extremely limited in presentation of mathematical equations.  </p>
<h3>Portability</h3>
<p> The two major syntactical categories of <i>roff</i> languages are requests and escapes. Since the <i>man</i> macros are implemented in terms of <i>groff</i> requests and escapes, one can, in principle, supplement the functionality of <i>man</i> with these lower-level elements where necessary. </p>
<p> Note, however, that using raw <i>groff</i> requests is likely to make your page render poorly on the class of viewers that transform it to HTML. Some requests make implicit assumptions about things like character and page sizes that may not hold in an HTML environment; also, many of these viewers don&#8217;t interpret the full <i>groff</i> vocabulary, a problem that can lead to portions of your text being silently dropped. </p>
<p> For portability to modern viewers, it is best to write your page entirely with the macros described in this page (except for the ones identified as deprecated, which should be avoided). The macros we have described as extensions (<code>.EX</code>/<code>.EE</code>, <code>.SY</code>/<code>.OP</code>/<code>.YS</code>, <code>.UR</code>/<code>.UE</code>, and <code>.MT</code>/<code>.ME</code>) should be used with caution, as they may not yet be built in to some viewer that is important to your audience. If in doubt, copy the implementation into your page---after the <code>.TH</code> call and the "Name" section, to accommodate timid <i>mandb</i> implementations. </p>
<p> Similar caveats apply to escapes. Some escape sequences are however required for correct typesetting even in man pages and usually do not cause portability problems: </p>
<dl>
<dt><code>\&quot;</code></dt>
<dd> <p> Comment. Everything after the double-quote to the end of the input line is ignored. Whole-line comments are frequently placed immediately after the empty request &#8216;.&#8216;. </p>
 </dd>
<dt><code>\</code><i>newline</i></dt>
<dd> <p> Join the next input line to the current one. Except for the update of the input line counter (used for diagnostic messages and related purposes), a series of lines ending in backslash-newline is transparent to <i>groff</i>. Use this escape to break excessively input long lines for document maintenance. </p>
 </dd>
<dt><code>\~</code></dt>
<dd> <p> Adjustable, non-breaking space character. Use this escape to prevent a break inside a short phrase or between a numerical quantity and its corresponding unit(s). </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> Before starting the motor, set the output speed to\~1. There are 1,024\~bytes in 1\~kiB. CSTR\~#8 documents the B language. </p>
 </dd></dl>
</dl>
<dt><code>\&amp;</code></dt>
<dd> <p> Zero-width space. Append to an input line to prevent an end-of-sentence punctuation sequence from being recognized as such, or insert at the beginning of an input line to prevent a dot or apostrophe from being interpreted as the beginning of a <i>roff</i> request. </p>
 </dd>
<dt><code>\(aq</code></dt>
<dd> <p> ASCII apostrophe. Use for syntax elements of programming languages because some output devices might replace unescaped apostrophes with right single quotation marks. </p>
 </dd>
<dt><code>\(oq</code></dt>
<dd> <p> Opening single quotation mark. <code>\(cq</code> Closing single quotation mark. </p>
 </dd>
<dd> <p> Use these for paired directional single quotes, &#8216;like this&#8217;. </p>
 </dd>
<dt><code>\(dq</code></dt>
<dd> <p> ASCII double-quote. Sometimes needed after macro calls to prevent the interpretation of the ASCII quotation mark character &#8216;&quot;&#8216; as the beginning or end of a macro argument. </p>
 </dd>
<dt><code>\(lq</code></dt>
<dd> <p> Left double quotation mark. <code>\(rq</code> Right double quotation mark. </p>
 </dd>
<dd> <p> Use these for paired directional double quotes, "like this". </p>
 </dd>
<dt><code>\(em</code></dt>
<dd> <p> Em-dash. Use for an interruption in a sentence---such as this one. </p>
 </dd>
<dt><code>\(en</code></dt>
<dd> <p> En-dash. Use to separate the two ends of a range, in particular between numbers, for example: the digits 1-9. </p>
 </dd>
<dt><code>\(ga</code></dt>
<dd> <p> ASCII grave accent. Use for syntax elements of programming languages, for example shell command substitutions, because some output devices might replace unescaped grave accents with left single quotation marks. </p>
 </dd>
<dt><code>\(ha</code></dt>
<dd> <p> ASCII circumflex accent. Use for syntax elements of programming languages because some output devices might replace unescaped circumflex accents with non-ASCII glyphs like the Unicode U+02C6 modifier letter circumflex. </p>
 </dd>
<dt><code>\(ti</code></dt>
<dd> <p> ASCII tilde. Use for syntax elements of programming languages because some output devices might replace unescaped tildes with non-ASCII glyphs like the Unicode U+02DC small tilde. </p>
 </dd>
<dt><code>\-</code></dt>
<dd> <p> Minus sign. Also use this to display syntax elements that require the ASCII hyphen-minus character, for example command-line options and C language operators. The unescaped &#8216;-&#8216; input character is not appropriate for these cases because it may render as a hyphen on some output devices. </p>
 </dd>
<dt><code>\c</code></dt>
<dd> <p> If this escape sequence occurs at the end of an input line, no white space is inserted between the last glyph on it and the first glyph resulting from the next input line. This is occasionally useful when three different fonts are needed in a single word. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> Normally, the final output file should be named .IB file .pdf\c \&amp;. </p>
 </dd></dl>
</dl>
<dd> <p> Note that when using this trick with the <code>.BI</code> or <code>.RI</code> macros, you will need to manually add an italic correction escape &#8216;\/&#8216; before the &#8216;\c&#8217; due to way macros expand their arguments. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> Files processed with .B groff \-mom (or .BI &quot;\-m &quot; mom\/\c ) produce PostScript output by default. </p>
 </dd></dl>
</dl>
<dd> <p> Alternatively, and perhaps with better portability, the &#8216;\f&#8217; font escape sequence can be used; see below. Using &#8216;\c&#8217; to include the output from more than one input line into the next-line argument of a <code>.TP</code> macro will render incorrectly with <i>groff</i> 1.22.3, <i>mandoc</i> 1.14.1, older versions of these programs, and perhaps with some other formatters. </p>
 </dd>
<dt><code>\e</code></dt>
<dd> <p> Widely used in man pages to represent a backslash output glyph. It works reliably as long as the <code>.ec</code> request is not used, which should never happen in man pages, and it is slightly more portable than the more exact &#8216;\(rs&#8217; ("reverse solidus") escape sequence. </p>
 </dd>
<dt><code>\fB</code>,&nbsp;<code>\fI</code>,&nbsp;<code>\fR</code>,&nbsp;<code>\fP</code></dt>
<dd> <p> Switch to bold, italic, roman, or back to the previous font, respectively. Either these or &#8216;\c&#8217; is needed when three different fonts are required in a single whitespace-delimited word. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> .RB [ \-\-reference\-dictionary=\fI\,name\/\fP ] </p>
 </dd>
<dd> <p> .RB [ \-\-reference\-dictionary=\c .IR name ] </p>
 </dd></dl>
</dl>
<dd> <p> Font escapes may be more portable than &#8216;\c&#8217;. As shown above, it is up to you to account for italic corrections with &#8216;\/&#8216; and &#8216;\,&#8216;, which are themselves <i>groff</i> extensions, if desired and if supported by your implementation. </p>
 </dd>
<dd> <p> Note that &#8216;\fP&#8217; reliably returns to the style in use immediately preceding the previous &#8216;\f&#8217; escape only if no sectioning, paragraph, or font face macro calls have intervened. </p>
 </dd>
<dd> <p> As long as only two fonts are needed in any single whitespace-delimited word, font alternation macros like <code>.BI</code> usually result in more readable source code than &#8216;\f&#8217; escapes do. </p>
 </dd></dl>
<p> For maximum portability, escape sequences and special characters not listed above are better avoided in man pages.  </p>
<h3>Deprecated features</h3>
<p> Use of the following is discouraged. </p>
<dl>
<dt><code>.AT</code> [</dt>
<dd> <p> <i>system</i> [<i>release</i>]] Alter the footer for use with AT&amp;T man pages, overriding any definition of the <i>footer-outside</i> argument to <code>.TH</code>. This macro exists only for compatibility; don&#8217;t use it. </p>
 </dd>
<dd> <p> The first argument <i>system</i> can be: </p>
 </dd>
<dl>
<dd> <p> &quot; Invisibly move left margin to current .IP indent. </p>
 </dd>
<dl>
<dd> <p> &quot; Now indent further, visibly. </p>
 </dd>
<dl>
<dt>3</dt>
<dd> <p> 7th edition <i>(default)</i> </p>
 </dd>
<dt>4</dt>
<dd> <p> System III </p>
 </dd>
<dt>5</dt>
<dd> <p> System V </p>
 </dd></dl>
</dl>
</dl>
<dd> <p> The optional second argument <i>release</i> specifies the release number, such as in "System V Release 3". </p>
 </dd>
<dt><code>.BT</code></dt>
<dd> <p> Set the page footer. Redefine this macro to get control of the footer. </p>
 </dd>
<dt><code>.DT</code></dt>
<dd> <p> Set tabs every 0.5~inches. Since this macro is always called during a <code>.TH</code> macro, it makes sense to call it only if the tab positions have been changed. </p>
 </dd>
<dd> <p> Use of this presentation-level macro is deprecated. It translates poorly to HTML, under which exact whitespace control and tabbing are not readily available. Thus, information or distinctions that you use <code>.DT</code> to express are likely to be lost. If you feel tempted to use it, you should probably be composing a table using <i><a href="/docs/linux/man/1-tbl/">tbl</a></i>(1) markup instead. </p>
 </dd>
<dt><code>.HP</code> [</dt>
<dd> <p> <i>indent</i>] Set up a paragraph with a hanging left indentation. The <i>indent</i> argument, if present, is handled as with <code>.TP</code>. </p>
 </dd>
<dd> <p> Use of this presentation-level macro is deprecated. While it is universally portable to legacy Unix systems, a hanging indentation cannot be expressed naturally under HTML, and many HTML-based manual viewers simply interpret it as a starter for a normal paragraph. Thus, any information or distinction you tried to express with the indentation may be lost. </p>
 </dd>
<dt><code>.PD</code> [</dt>
<dd> <p> <i>vertical-space</i>] Define the vertical space between paragraphs or (sub)sections. The optional argument <i>vertical-space</i> specifies the amount of space; the default scaling is &#8216;v&#8217;). Without an argument, the spacing is reset to its default value; see "Horizontal and vertical spacing" above. </p>
 </dd>
<dd> <p> Use of this presentation-level macro is deprecated. It translates poorly to HTML, under which exact control of inter-paragraph spacing is not readily available. Thus, information or distinctions that you use <code>.PD</code> to express are likely to be lost. </p>
 </dd>
<dt><code>.PT</code></dt>
<dd> <p> Set the page header. Redefine this macro to get control of the header. </p>
 </dd>
<dt><code>.UC</code> [</dt>
<dd> <p> <i>version</i>] Alter the footer for use with BSD man pages, overriding any definition of the <i>footer-outside</i> argument to <code>.TH</code>. This macro exists only for compatibility; don&#8217;t use it. </p>
 </dd>
<dd> <p> The argument <i>version</i> can be: </p>
 </dd>
<dl>
<dd> <p> &quot; Invisibly move left margin to current .IP indent. </p>
 </dd>
<dl>
<dd> <p> &quot; Now indent further, visibly. </p>
 </dd>
<dl>
<dt>3</dt>
<dd> <p> 3rd Berkeley Distribution <i>(default)</i> </p>
 </dd>
<dt>4</dt>
<dd> <p> 4th Berkeley Distribution </p>
 </dd>
<dt>5</dt>
<dd> <p> 4.2 Berkeley Distribution </p>
 </dd>
<dt>6</dt>
<dd> <p> 4.3 Berkeley Distribution </p>
 </dd>
<dt>7</dt>
<dd> <p> 4.4 Berkeley Distribution </p>
 </dd></dl>
</dl>
</dl>
</dl>
<h3>History</h3>
<p> According to its own <i><a href="/docs/linux/man/7-man/">man</a></i>(7) page, Version 7 Unix (1979) supported all of the macros described in this page not listed as GNU extensions, except <code>.P</code>, <code>.SB</code>, <code>.SS</code>, and the deprecated <code>.AT</code>, <code>.BT</code>, <code>.PT</code>, and <code>.UC</code>. The only string registers defined were <code>R</code> and <code>S</code>; no number registers were documented.  </p>
<h2>OPTIONS</h2>
<p> The following <i>groff</i> options set number registers recognized and used by the <i>man</i> macro package. </p>
<dl>
<dt><code>-rcR=1</code></dt>
<dd> <p> Continuous rendering. Create a single, very long page instead of multiple pages. This is the default in <i>nroff</i> mode. Use <code>-rcR=0</code> to disable it. </p>
 </dd>
<dt><code>-rC1</code></dt>
<dd> <p> Number pages continuously. If more than one man page is given on the command line, number the pages continuously, rather than starting each at~1. </p>
 </dd>
<dt><code>-rD1</code></dt>
<dd> <p> Enable double-sided printing. Footers for even and odd pages are formatted differently; see the description of <code>.TH</code> in "Document structure macros", above. </p>
 </dd>
<dt><code>-rFT=</code><i>footer-distance</i></dt>
<dd> <p> Set distance of the footer, relative to the bottom of the page if negative or relative to the top if positive, to <i>footer-distance</i>. The default is -0.5i. </p>
 </dd>
<dt><code>-rHY=</code><i>flags</i></dt>
<dd> <p> Set hyphenation flags. Permissible values of <i>flags</i> are documented in section "Hyphenation" of <i><a href="/docs/linux/man/7-groff/">groff</a></i>(7). The default is~4 if continuous rendering is enabled (<code>-rcR=1</code> above), and~6 otherwise. </p>
 </dd>
<dt><code>-rIN=</code><i>indent</i></dt>
<dd> <p> Set the body text indentation (for normal paragraphs) to <i>indent</i>. See "Horizontal and vertical spacing" above for the default indentation value. For <i>nroff</i>, <i>indent</i> should always be an integer multiple of unit &#8216;n&#8217; to get consistent indentation. </p>
 </dd>
<dt><code>-rLL=</code><i>line-length</i></dt>
<dd> <p> Set line length. If this option is not given, the line length is set to respect any value set by a prior ".ll" request (which <i>must</i> be in effect when the <code>.TH</code> macro is invoked), if this differs from the built-in default for the formatter; otherwise it defaults to 78n in <i>nroff</i> mode and 6.5i in <i>troff</i> mode. </p>
 </dd>
<dd> <p> Note that the use of a ".ll" request to initialize the line length is supported for backward compatibility with some versions of the <i>man</i> program; direct initialization of the <code>LL</code> register should <i>always</i> be preferred to the use of such a request. In particular, note that a ".ll~65n" request does <i>not</i> preserve the normal <i>nroff</i> default line length (the <i>man</i> default initialization to 78n prevails), whereas the <code>-rLL=65n</code> option, or an equivalent ".nr~LL~65n" request preceding the use of the <code>.TH</code> macro, <i>does</i> set a line length of 65n. </p>
 </dd>
<dt><code>-rLT=</code><i>title-length</i></dt>
<dd> <p> Set title length. If this option is not given, the title length defaults to the line length. </p>
 </dd>
<dt><code>-rP</code><i>n</i></dt>
<dd> <p> Start enumeration of pages at <i>n</i> rather than~1. </p>
 </dd>
<dt><code>-rS</code><i>point-size</i></dt>
<dd> <p> Use <i>point-size</i> as the base document font size. Acceptable values are 10, 11, or 12. See subsection "Font style macros" above for the default. </p>
 </dd>
<dt><code>-rSN=</code><i>subsection-indent</i></dt>
<dd> <p> Set subsection indentation to <i>subsection-indent</i>. See "Horizontal and vertical spacing" above for the default indentation value. </p>
 </dd>
<dt><code>-rX</code><i>p</i></dt>
<dd> <p> After page <i> p</i>, number pages as <i>p</i>a, <i>p</i>b, <i>p</i>c, and so forth. For example, the option <code>-rX2</code> produces the following page numbers: 1, 2, 2a, 2b, 2c, and so on. </p>
 </dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/:share/:groff/:1.22.4/:tmac/:man.tmac</i></dt>
<dd> <p> <i>/usr/:share/:groff/:1.22.4/:tmac/:an.tmac</i> These are wrapper files to call <i>andoc.tmac</i>. </p>
 </dd>
<dt><i>/usr/:share/:groff/:1.22.4/:tmac/:andoc.tmac</i></dt>
<dd> <p> This brief <i>groff</i> program detects whether the <i>man</i> or <i>mdoc</i> macro package is being used by a document and loads the correct macro definitions, taking advantage of the fact that pages using them must call <code>.TH</code> or <code>.Dd</code>, respectively, as their first macro. Because the wrappers above load this file, a <i>man</i> program or user typing, for example, "groff -man page.1", need not know which package the file <i>page.1</i> uses. Multiple man pages, in either format, can be handled. </p>
 </dd>
<dt><i>/usr/:share/:groff/:1.22.4/:tmac/:an-old.tmac</i></dt>
<dd> <p> Most <i>man</i> macros are contained in this file. It also loads the GNU extensions from <i>an-ext.tmac</i> (see below). </p>
 </dd>
<dt><i>/usr/:share/:groff/:1.22.4/:tmac/:an-ext.tmac</i></dt>
<dd> <p> The extension macro definitions for <code>.SY</code>, <code>.OP</code>, <code>.YS</code>, <code>.TQ</code>, <code>.EX</code>/<code>.EE</code>, <code>.UR</code>/<code>.UE</code>, and <code>.MT</code>/<code>.ME</code> are contained in this file, which is written in classic <i>troff</i> and permissively licensed---not copylefted. Man page authors concerned about portability to legacy Unix systems are encouraged to copy these definitions into their pages, and maintainers of <i>troff</i> implementations or work-alike systems that format man pages are encouraged to re-use them. </p>
 </dd>
<dd> <p> Note that the definitions for these macros are read after the call of <code>.TH</code>, so they will replace any macros of the same names preceding it in your file. If you use your own implementations of these macros, they must be defined after calling <code>.TH</code> to have any effect. </p>
 </dd>
<dt><i>/usr/:share/:groff/:site-tmac/:man.local</i></dt>
<dd> <p> Local changes and customizations should be put into this file. </p>
 </dd></dl>
<h2>NOTES</h2>
<p> Some tips on troubleshooting your man pages follow. </p>
<dl>
<dt>&bull;<code> .RS</code> doesn&#8217;t indent relative to my indented paragraph </dt>
<dd> <p> The <code>.RS</code> macro sets the indentation relative to the amount of a <i>normal</i> paragraph (<code>.PP</code> and its synonyms). The same default indentation amount is used for <code>.RS</code>, <code>.IP</code>, <code>.TP</code>, and the deprecated <code>.HP</code>. If you need to start an indent relative to an indented paragraph, call <code>.RS</code> repeatedly until an acceptable indentation is achieved, or give <code>.RS</code> an indentation argument that is at least as much as the paragraph&#8217;s indentation amount relative to an adjacent <code>.PP</code> paragraph. See "Horizontal and vertical spacing" above for the values. </p>
 </dd>
<dt>&bull;<code> .RE</code> doesn&#8217;t reset the indent to the expected level </dt>
<dd> <p> &bull; warning: scale indicator invalid in this context &bull; warning: number register &#8216;an-saved-margin <i>n</i>&#8216; not defined &bull; warning: number register &#8216;an-saved-prevailing-indent <i>n</i>&#8216; not defined The <code>.RS</code> macro takes an indentation <i>amount</i> as an argument; the <code>.RE</code> macro&#8217;s argument is a specific indentation <i>level</i>. <code>.RE~1</code> goes to the level before any <code>.RS</code> macros were called, <code>.RE~2</code> goes to the level of the first <code>.RS</code> call you made, and so forth. If you desire symmetry in your macro calls, simply issue one <code>.RE</code> without an argument for each <code>.RS</code> that precedes it. </p>
 </dd>
<dd> <p> After calls to the <code>.SH</code> and <code>.SS</code> sectioning macros, all relative indents are cleared and calls to <code>.RE</code> have no effect. </p>
 </dd></dl>
<h2>AUTHORS</h2>
<p> The GNU version of the <i>man</i> macro package was written by James Clark and contributors. The extension macros were written by Werner Lemberg and Eric S. Raymond </p>
<p> This document was originally written for the Debian GNU/Linux system by Susan G. Kleinmann It was corrected and updated by Werner Lemberg and G. Branden Robinson. The extension macros were documented by Eric S. Raymond; he also originated the portability section, to which Ingo Schwarze contributed most of the material on escape sequences.  </p>
<h2>SEE ALSO</h2>
<p> <i>Groff: The GNU Implementation of troff</i>, by Trent A. Fisher and Werner Lemberg, is the main <i>groff</i> documentation. You can browse it interactively with "info groff". </p>
<p> <i><a href="/docs/linux/man/1-tbl/">tbl</a></i>(1), <i><a href="/docs/linux/man/1-eqn/">eqn</a></i>(1), and <i><a href="/docs/linux/man/1-refer/">refer</a></i>(1) are preprocessors used with man pages. </p>
<p> <i><a href="/docs/linux/man/1-man/">man</a></i>(1) describes the man page formatter on your system. </p>
<p> <i><a href="/docs/linux/man/7-groff_mdoc/">groff_mdoc</a></i>(7) describes the <i>groff</i> version of the BSD-originated alternative macro package for man pages. </p>
<p> <i><a href="/docs/linux/man/7-groff/">groff</a></i>(7), <i><a href="/docs/linux/man/7-groff_char/">groff_char</a></i>(7), <i><a href="/docs/linux/man/7-man/">man</a></i>(7) </p>
