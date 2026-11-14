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
<dt><code>.TH</code><i> title section</i></p>
<dd>[<i>footer-middle</i>] [<i>footer-outside</i>] [<i>header-middle</i>] Define the title of the man page as <i>title</i> and the section as <i>section</i>. See <i><a href="/docs/linux/man/1-man/">man</a></i>(1) for details on the section numbers and suffixes applicable to your system. <i>title</i> and <i>section</i> are positioned together at the left and right in the header line (with <i>section</i> in parentheses immediately appended to <i>title</i>). <i>footer-middle</i> is centered in the footer line. <i>footer-outside</i> is positioned at the left in the footer line (or at the left on even pages and at the right on odd pages if double-sided printing is active). <i>header-middle</i> is centered in the header line. If <i>section</i> is a simple integer between 1 and~9 (inclusive), or is exactly &#8220;3p&#8221;, there is no need to specify <i>header-middle</i>; the macro package will supply text for it.</p>
<dd>For HTML output, headers and footers are completely suppressed.</p>
<dd>Additionally, this macro starts a new page; the page number is reset to~1 (unless the <code>-rC1</code> option is given on the command line). This feature is intended only for formatting multiple man pages.</p>
<dd>A man page should contain exactly one <code>.TH</code> call at or near the beginning of the file, prior to any other macro calls.</p>
<dd>By convention, <i>footer-middle</i> is the most recent modification date of the man page source document, and <i>footer-outside</i> is the name and version or release of the project providing it.</p>
<dt><code>.SH</code> [</p>
<dd><i>heading-text</i>] Set <i>heading-text</i> as a section heading flush left. The text following <code>.SH</code> up to the end of the line, or the text on the next input line if <code>.SH</code> is given no arguments, is set in bold (or the font specified by the string register <code>HF</code>) slightly larger than the base font size. Additionally, the left margin and indentation affecting subsequent text are reset to their default values. Text on input lines after <i>heading-text</i> is set as a normal paragraph (<code>.PP</code>).</p>
<dd>The content of <i>heading-text</i> and ordering of sections has been standardized by common practice, as has much of the layout of material within sections. For example, a section called &#8220;Name&#8221; or &#8220;NAME&#8221; must exist, must be the first section after the <code>.TH</code> call, and must contain only a line of the form</p>
<dl>
<dd>&quot; Invisibly move left margin to current .IP indent.</p>
<dl>
<dd>&quot; Now indent further, visibly. <i>page-topic</i>[<code>,</code> &#8230;] <code>\-&nbsp;</code><i>summary-description</i></dl>
<p> for a man page to be properly indexed. See <i><a href="/docs/linux/man/7-man/">man</a></i>(7) for the conventions prevailing on your system.</dl>
<dt><code>.SS</code> [</p>
<dd><i>subheading-text</i>] Set <i>subheading-text</i> as a subsection heading indented (by default) partway between a section heading and a normally-indented paragraph (<code>.PP</code>). The text following <code>.SS</code> up to the end of the line, or the text on the next input line if <code>.SS</code> is given no arguments, is set in bold (or the font specified by the string register <code>HF</code>) at the base font size. Additionally, the left margin and indentation affecting subsequent text are reset to their default values. Text on input lines after <i>subheading-text</i> is set as a normal paragraph (<code>.PP</code>).</p>
<dt><code>.EX</code></p>
<dd><code>.EE</code> Begin and end example. After <code>.EX</code>, filling and hyphenation are disabled and a constant-width (monospaced) font is selected. Calling <code>.EE</code> enables filling and restores the previous hyphenation setting and font.</p>
<dd>Example regions are useful for formatting code, shell sessions, and text file contents.</p>
<dd>These macros are defined on many (but not all) legacy Unix systems running classic <i>troff</i>. To be certain your page will be portable to those systems, copy their definitions from the <i>an-ext.tmac</i> file of a <i>groff</i> installation.</p>
<dt><code>.RS</code> [</p>
<dd><i>indent</i>] Move the left margin to the right by the value <i>indent</i>, if specified, and by a default amount otherwise; see subsection &#8220;Horizontal and vertical spacing&#8221; below. Calls to <code>.RS</code> can be nested; each call increments by~1 the indentation level used by <code>.RE</code>. The indentation level prior to any <code>.RS</code> calls is~1.</p>
<dt><code>.RE</code> [</p>
<dd><i>level</i>] Move the left margin back to that corresponding to indentation level <i>level</i>. If no argument is given, move the left margin one level back.</dl>
<h3>Paragraph macros</h3>
<p>A typical paragraph (<code>.PP</code>) is set at the current left margin, which by default is indented from the left margin of the output device. In man pages and other technical literature, definition lists are frequently encountered; these can be set as &#8220;tagged paragraphs&#8221; (<code>.TP</code> and <code>.TQ</code>), which have one or more leading tags followed by a paragraph that has an additional left indent. The indented paragraph (<code>.IP</code>) macro is useful to continue the indented content of a narrative started with <code>.TP</code>, or to present an itemized or ordered list.</p>
<dl>
<dt><code>.LP</code></p>
<dd><code>.PP</code> <code>.P</code> Begin a new paragraph; these macros are synonymous. They break the output line at the current position, followed by a vertical space downward by a default amount (which can be changed by the deprecated <code>.PD</code> macro). The font size and style are reset to defaults; see subsection &#8220;Font style macros&#8221; below. Finally, the left margin and indentation are reset to default values.</p>
<dt><code>.TP</code> [</p>
<dd><i>indent</i>] Set a tagged, indented paragraph. The input line following this macro, known as the <i>tag</i>, is printed at the current left margin. Subsequent text is indented by <i>indent</i>, if specified, and by a default amount otherwise; see subsection &#8220;Horizontal and vertical spacing&#8221; below.</p>
<dd>If the tag is not as wide as the indentation, the paragraph starts on the same line as the tag, at the applicable indentation, and continues on the following lines. Otherwise, the descriptive part of the paragraph begins on the line following the tag, entirely indented. The line containing the tag can include a macro call, for instance to set the tag in bold with <code>.B</code>.</p>
<dd><code>.TP</code> was used to write the first paragraph of this description of <code>.TP</code>, and <code>.IP</code> the subsequent ones.</p>
<dt><code>.TQ</code></p>
<dd>Set an additional tag for a paragraph tagged with <code>.TP</code>. The pending output line is broken. The tag on the input line following this macro and subsequent lines are handled as with <code>.TP</code>.</p>
<dd>This macro is not defined on legacy Unix systems running classic <i>troff</i>. To be certain your page will be portable to those systems, copy its definition from the <i>an-ext.tmac</i> file of a <i>groff</i> installation.</p>
<dd>The descriptions of <code>.LP</code>, <code>.PP</code>, and <code>.P</code> above were written using <code>.TP</code> and <code>.TQ</code>.</p>
<dt><code>.IP</code> [</p>
<dd><i>tag</i>] [<i>indent</i>] Set an indented paragraph with an optional tag. The <i>tag</i> and <i>indent</i> arguments, if present, are handled as with <code>.TP</code>, with the exception that the <i>tag</i> argument to <code>.IP</code> cannot include a macro call.</p>
<dd>Two convenient use cases for <code>.IP</code> are</p>
<dl>
<dd>&quot; Invisibly move left margin to current .IP indent.</p>
<dl>
<dd>&quot; Now indent further, visibly.</p>
<dl>
<dt>(1)</p>
<dd>to start a new paragraph with the same indentation as the previous <code>.IP</code> or <code>.TP</code> paragraph, if no <i>indent</i> argument is given; and</p>
<dt>(2)</p>
<dd>to set a paragraph with a short <i>tag</i> that is not semantically important, such as a bullet (&bull;)&#8212;obtained with the &#8216;\(bu&#8217; character escape&#8212;or list enumerator, as seen in this very paragraph.</dl>
</dl>
</dl>
</dl>
<h3>Command synopsis macros</h3>
<p>Command synopses are a staple of section~1 and~8 man pages. These macros aid you to construct one that has the classical Unix appearance. Furthermore, some tools are able to interpret these macros semantically and treat them appropriately for localization and/or presentation. A command synopsis is wrapped in <code>.SY</code>/<code>.YS</code> calls, with command-line options of some formats indicated by <code>.OP</code>. These macros are not defined on legacy Unix systems running classic <i>troff</i>. To be certain your page will be portable to those systems, copy their definitions from the <i>an-ext.tmac</i> file of a <i>groff</i> installation.</p>
<dl>
<dt><code>.SY</code><i> command</i></p>
<dd>Begin synopsis. Hyphenation is turned off. The <i>command</i> argument is set in bold. The output line is filled as normal, but if a break is required, subsequent output lines are indented by the width of <i>command</i> plus a space.</p>
<dt><code>.OP</code><i> option-name/</i></p>
<dd>[<i>option-argument</i>] Indicate an optional command parameter called <i>option-name</i>, which is set in bold. If the option takes an argument, specify <i>option-argument</i> using a noun, abbreviation, or hyphenated noun phrase. If present, <i>option-argument</i> is preceded by a space and set in italics. Square brackets (in roman) surround both arguments.</p>
<dt><code>.YS</code></p>
<dd>End synopsis. Restore indentation and hyphenation to previous values.</dl>
<p> Multiple <code>.SY/.YS</code> blocks can be specified, for instance to distinguish differing modes of operation of a complex command like <i><a href="/docs/linux/man/1-tar/">tar</a></i>(1); each will be separated by a paragraph space. <code>.SY</code> can also be repeated multiple times before a closing <code>.YS</code>, which is useful to indicate synonymous ways of invoking a particular mode of operation. For example,</p>
<dl>
<dd>.SY groff .OP \-abcegiklpstzCEGNRSUVXZ .OP \-d cs .OP \-f fam .OP \-F dir .OP \-I dir .OP \-K arg .OP \-L arg .OP \-m name .OP \-M dir .OP \-n num .OP \-o list .OP \-P arg .OP \-r cn .OP \-T dev .OP \-w name .OP \-W name .RI [ file \&amp;.\|.\|.\&amp;] .YS . .SY groff .B \-h .SY groff .B \-\-help .YS</p>
<dd> produces the following output.</p>
<dl>
<dd>[ <code>-abcegiklpstzCEGNRSUVXZ</code> ] [ <code>-d </code><i>cs</i> ] [ <code>-f </code><i>fam</i> ] [ <code>-F </code><i>dir</i> ] [ <code>-I </code><i>dir</i> ] [ <code>-K </code><i>arg</i> ] [ <code>-L </code><i>arg</i> ] [ <code>-m </code><i>name</i> ] [ <code>-M </code><i>dir</i> ] [ <code>-n </code><i>num</i> ] [ <code>-o </code><i>list</i> ] [ <code>-P </code><i>arg</i> ] [ <code>-r </code><i>cn</i> ] [ <code>-T </code><i>dev</i> ] [ <code>-w </code><i>name</i> ] [ <code>-W </code><i>name</i> ] [<i>file</i> &#8230;] <code>-h</code> <code>&#8211;help</code></dl>
<p> Several features of the above example are of note.</p>
<dl>
<dt>&bull;</p>
<dd>The empty request (.), which does nothing, is used for vertical spacing in the input file for readability by the document maintainer. Do not put empty lines in a <i>roff</i> source document.</p>
<dt>&bull;</p>
<dd>The command and option names are presented in <code>bold</code> to cue the user that they should be input literally.</p>
<dt>&bull;</p>
<dd>Option dashes are specified with the &#8216;\-&#8216; escape sequence; this is an important practice to make them clearly visible and to facilitate cut-and-paste from the rendered man page to a shell prompt or text file.</p>
<dt>&bull;</p>
<dd>Option arguments and command operands are presented in <i>italics</i> (underlined on some output devices, such as terminals and emulators), to cue the user that they must be replaced with appropriate text.</p>
<dt>&bull;</p>
<dd>Symbols that are neither to be typed literally nor simply replaced appear in the roman style; brackets surround optional arguments, and an ellipsis indicates that the previous syntactical element may be repeated arbitrarily.</p>
<dd>Some man pages use a brace-and-pipe notation such as &#8220;{<code>&#8211;diff</code>|<code>&#8211;compare</code>}&#8221; to indicate that one and only one of the &#8216;|&#8217;-separated items within the braces must be input. If this braced construct is furthermore surrounded by square brackets, it means that at most one of the items is accepted.</p>
<dd>Authors of man pages should note the use of the zero-width space escape sequence &#8216;\&amp;&#8217; on both sides of the ellipsis; this is a good practice to avoid surprises in the event the ellipsis gets refilled in your text editor. See &#8220;Portability&#8221;, below. The morbidly curious may consult <i><a href="/docs/linux/man/7-groff/">groff</a></i>(7) regarding the narrow-space escape sequence &#8216;\|&#8217;.</dl>
<h3>Hyperlink and email macros</h3>
<p>Email addresses are bracketed with <code>.MT</code>/<code>.ME</code> and URL hyperlinks with <code>.UR</code>/<code>.UE</code>. These macros are not defined on legacy Unix systems running classic <i>troff</i>. To be certain your page will be portable to those systems, copy their definitions from the <i>an-ext.tmac</i> file of a <i>groff</i> installation.</p>
<dl>
<dt><code>.MT</code><i> address</i></p>
<dd><code>.ME</code> [<i>punctuation</i>] Identify <i>address</i> as an RFC 6068 <i>addr-spec</i> for a &#8220;mailto:&#8221; URI with the text between the two macro calls as the link text. A <i>punctuation</i> argument to <code>.ME</code> is placed at the end of the link text without intervening space. Note that <i>address</i> may not be visible in the output text, particularly if the man page is being viewed as HTML. On a device that is not a browser, <i>address</i> is set in angle brackets after the link text and before <i>punctuation</i>.</p>
<dd>When rendered by <i>groff</i> to a TTY or PostScript output device,</p>
<dl>
<dd>
<dl>
<dd>Contact .MT fred.foonly@\:fubar.net Fred Foonly .ME for more information.</dl>
</dl>
<dd>displays as: &#8220;Contact Fred Foonly &lt;fred.foonly@:fubar.net&gt; for more information.&#8221;.</p>
<dd>The use of &#8216;\:&#8217; to insert hyphenless discretionary breaks is a <i>groff</i> extension and can be omitted.</p>
<dt><code>.UR</code><i> URL</i></p>
<dd><code>.UE</code> [<i>punctuation</i>] Identify <i>URL</i> as an RFC 3986 URI hyperlink with the text between the two macro calls as the link text. A <i>punctuation</i> argument to <code>.UE</code> is placed at the end of the link text without intervening space. Note that <i>URL</i> may not be visible in the output text, particularly if the man page is being viewed as HTML. On a device that is not a browser, <i>URL</i> is set in angle brackets after the link text and before <i>punctuation</i>.</p>
<dd>When rendered by <i>groff</i> to a TTY or PostScript output device,</p>
<dl>
<dd>
<dl>
<dd>The GNU Project of the Free Software Foundation hosts the .UR <a rel="nofollow" href="https://\:www.gnu.org/\:software/\:groff/">https://\:www.gnu.org/\:software/\:groff/</a> Groff home page .UE .</dl>
</dl>
<dd>displays as: &#8220;The GNU Project of the Free Software Foundation hosts the Groff home page &lt;<a rel="nofollow" href="https://:www.gnu.org/:software/:groff/">https://:www.gnu.org/:software/:groff/</a>&gt;.&#8221;.</p>
<dd>The use of &#8216;\:&#8217; to insert hyphenless discretionary breaks is a <i>groff</i> extension and can be omitted.</dl>
<h3>Font style macros</h3>
<p>The <i>man</i> macro package is limited in its font styling options, offering only <code>bold</code>~(<code>.B</code>), <i>italic</i>~(<code>.I</code>), and roman (the default). Italic text is usually set underscored instead on terminals and other classical <i>nroff</i>-style output devices. The <code>.SM</code> and <code>.SB</code> macros set text in roman or bold, respectively, at a smaller point size; these differ visually from regular-sized roman or bold text only on <i>troff</i>-style output devices. The foregoing macros cause word breaks before and after their arguments, but it is often necessary to set text in different styles without intervening whitespace. The macros <code>.BI</code>, <code>.BR</code>, <code>.IB</code>, <code>.IR</code>, <code>.RB</code>, and <code>.RI</code>, where &#8216;B&#8217;, &#8216;I&#8217;, and &#8216;R&#8217; indicate bold, italic, and roman, respectively, set their odd- and even-numbered arguments in alternating styles, with no whitespace separating them. Because font styles are presentational rather than semantic, conflicting traditions have arisen regarding which font styles should be used to mark file or path names, environment variables, in-line literals, and even man page cross-references. The default font size and family (for <i>troff</i> output devices) is 10-point Times. The default style is roman.</p>
<dl>
<dt><code>.B</code>~[</p>
<dd><i>text</i>] Set <i>text</i> in bold. If the macro is given no arguments, the text of the next input line is set in bold.</p>
<dd>Use bold for literal portions of syntax synopses, for command-line options in running text, and for literals that are major topics of the subject under discussion; for example, this page uses bold for macro and register names. In <code>.EX</code>/<code>.EE</code> examples of interactive I/O (such as a shell session), set only the user-typed input in bold.</p>
<dt><code>.I</code>~[</p>
<dd><i>text</i>] Set <i>text</i> in italics. If the macro is given no arguments, the text of the next input line is set in italics.</p>
<dd>Use italics for file and path names, for environment variables, for enumeration or preprocessor constants in C, for variable (user-determined) portions of syntax synopses, for the first occurrence only of a technical concept being introduced, for names of works of software (including commands and functions, but excluding names of operating systems or their kernels), and anywhere a parameter requiring replacement by the user is encountered. An exception involves variable text in a context that is already marked up in italics, such as file or path names with variable components; in such cases, follow the convention of mathematical typography: set the file or path name in italics as usual (see <code>.IR</code> below), but use roman for the variable part, and italics again in running roman text when referring to the variable material.</p>
<dt><code>.SM</code>~[</p>
<dd><i>text</i>] Set <i>text</i> one point size smaller than the default size. If the macro is given no arguments, the text of the next input line is set smaller.</p>
<dd><i>Note</i>: <i>nroff</i>-style output devices, such as terminals, will render <i>text</i> at the normal font size instead. Do not rely upon <code>.SM</code> to communicate semantic information distinct from using roman style at the normal size; it will be hidden from readers using such devices.</p>
<dt><code>.SB</code>~[</p>
<dd><i>text</i>] Set <i>text</i> in bold, one point size smaller than the default size. If the macro is given no arguments, the text of the next input line is set smaller and in bold.</p>
<dd><i>Note</i>: <i>nroff</i>-style output devices, such as terminals, will render <i>text</i> in bold at the normal font size instead. Do not rely upon <code>.SB</code> to communicate semantic information distinct from using bold style at the normal size; it will be hidden from readers using such devices.</dl>
<p> Note what is <i>not</i> prescribed for setting in bold or italics above: elements of &#8220;synopsis language&#8221; such as ellipses and brackets around options; proper names and adjectives; titles of anything other than works of literature or software; identifiers for standards documents or technical reports such as CSTR~#54, RFC~1918, Unicode~11.0, or POSIX.1-2017; acronyms; and occurrences after the first of a technical term or piece of jargon. Again, the names of operating systems and their kernels are, by practically universal convention, set in roman. Be frugal with the use of italics for emphasis, and particularly with the use of bold. Brief runs of literal text, such as references to individual characters or short strings, including section and subsection headings of man pages, are suitable objects for quotation; see the &#8216;\(lq&#8217;, &#8216;\(rq&#8217;, &#8216;\(oq&#8217;, and &#8216;\(cq&#8217; escapes in subsection &#8220;Portability&#8221; below. Unlike the above font style macros, the font alternation macros below accept only arguments on the same line as the macro call. If whitespace is required within one of the arguments, first consider whether the same result could be achieved with as much clarity by using the single-style macros on separate input lines. When it cannot, double-quote an argument with one or more embedded space characters. Setting all three different styles within one whitespace-delimited word presents challenges; it is possible with the &#8216;
