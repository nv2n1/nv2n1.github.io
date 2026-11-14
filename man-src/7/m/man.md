---
title: "man(7)"
name: "man"
section: "7"
letter: "m"
url: "/docs/linux/man/7-man/"
description: "man – macros to format man pages"
---

<p>man &#8211; macros to format man pages</p>
<h2>Synopsis</h2>
<p><code>groff -Tascii -man</code> <i>file</i> &#8230; </p>
<p> <code>groff -Tps -man</code> <i>file</i> &#8230; </p>
<p> <code>man</code> [<i>section</i>] <i>title</i></p>
<h2>Description</h2>
<p>This manual page explains the <code>groff an.tmac</code> macro package (often called the <code>man</code> macro package). This macro package should be used by developers when writing or porting man pages for Linux. It is fairly compatible with other versions of this macro package, so porting man pages should not be a major problem (exceptions include the NET-2 BSD release, which uses a totally different macro package called mdoc; see <code><a href="/docs/linux/man/7-mdoc/">mdoc</a></code>(7)). </p>
<p> Note that NET-2 BSD mdoc man pages can be used with <code>groff</code> simply by specifying the <code>-mdoc</code> option instead of the <code>-man</code> option. Using the <code>-mandoc</code> option is, however, recommended, since this will automatically detect which macro package is in use. </p>
<p> For conventions that should be employed when writing man pages for the Linux <i>man-pages</i> package, see <code><a href="/docs/linux/man/7-man-pages/">man-pages</a></code>(7).</p>
<h3>Title line</h3>
<p>The first command in a man page (after comment lines, that is, lines that start with <code>.\&quot;</code>) should be </p>
<dl>
<dd><code>.TH</code> <i>title section date source manual</i></dl>
<p> For details of the arguments that should be supplied to the <code>TH</code> command, see <code><a href="/docs/linux/man/7-man-pages/">man-pages</a></code>(7). </p>
<p> Note that BSD mdoc-formatted pages begin with the <code>Dd</code> command, not the <code>TH</code> command.</p>
<h3>Sections</h3>
<p>Sections are started with <code>.SH</code> followed by the heading name. </p>
<p> The only mandatory heading is NAME, which should be the first section and be followed on the next line by a one-line description of the program: </p>
<dl>
<dd>.SH NAME<br />
 item \- description</dl>
<p> It is extremely important that this format is followed, and that there is a backslash before the single dash which follows the item name. This syntax is used by the <code><a href="/docs/linux/man/8-mandb/">mandb</a></code>(8) program to create a database of short descriptions for the <code><a href="/docs/linux/man/1-whatis/">whatis</a></code>(1) and <code><a href="/docs/linux/man/1-apropos/">apropos</a></code>(1) commands. (See <code><a href="/docs/linux/man/1-lexgrog/">lexgrog</a></code>(1) for further details on the syntax of the NAME section.) </p>
<p> For a list of other sections that might appear in a manual page, see <code><a href="/docs/linux/man/7-man-pages/">man-pages</a></code>(7).</p>
<h3>Fonts</h3>
<p>The commands to select the type face are:</p>
<dl>
<dt><code>.B</code></p>
<dd>Bold</p>
<dt><code>.BI</code></p>
<dd>Bold alternating with italics (especially useful for function specifications)</p>
<dt><code>.BR</code></p>
<dd>Bold alternating with Roman (especially useful for referring to other manual pages)</p>
<dt><code>.I</code></p>
<dd>Italics</p>
<dt><code>.IB</code></p>
<dd>Italics alternating with bold</p>
<dt><code>.IR</code></p>
<dd>Italics alternating with Roman</p>
<dt><code>.RB</code></p>
<dd>Roman alternating with bold</p>
<dt><code>.RI</code></p>
<dd>Roman alternating with italics</p>
<dt><code>.SB</code></p>
<dd>Small alternating with bold</p>
<dt><code>.SM</code></p>
<dd>Small (useful for acronyms)</dl>
<p> Traditionally, each command can have up to six arguments, but the GNU implementation removes this limitation (you might still want to limit yourself to 6 arguments for portability&#8217;s sake). Arguments are delimited by spaces. Double quotes can be used to specify an argument which contains spaces. For the macros that produce alternating type faces, the arguments will be printed next to each other without intervening spaces, so that the <code>.BR</code> command can be used to specify a word in bold followed by a mark of punctuation in Roman. If no arguments are given, the command is applied to the following line of text.</p>
<h3>Other macros and strings</h3>
<p>Below are other relevant macros and predefined strings. Unless noted otherwise, all macros cause a break (end the current line of text). Many of these macros set or use the &quot;prevailing indent.&quot; The &quot;prevailing indent&quot; value is set by any macro with the parameter <i>i</i> below; macros may omit <i>i</i> in which case the current prevailing indent will be used. As a result, successive indented paragraphs can use the same indent without respecifying the indent value. A normal (nonindented) paragraph resets the prevailing indent value to its default value (0.5 inches). By default, a given indent is measured in ens; try to use ens or ems as units for indents, since these will automatically adjust to font size changes. The other key macro definitions are:</p>
<h3>Normal paragraphs</h3>
<dl>
<dt><code>.LP</code></p>
<dd>Same as <code>.PP</code> (begin a new paragraph).</p>
<dt><code>.P</code></p>
<dd>Same as <code>.PP</code> (begin a new paragraph).</p>
<dt><code>.PP</code></p>
<dd>Begin a new paragraph and reset prevailing indent.</dl>
<h3>Relative margin indent</h3>
<dl>
<dt><code>.RS</code><i> i</i></p>
<dd>Start relative margin indent: moves the left margin <i>i</i> to the right (if <i>i</i> is omitted, the prevailing indent value is used). A new prevailing indent is set to 0.5 inches. As a result, all following paragraph(s) will be indented until the corresponding <code>.RE</code>.</p>
<dt><code>.RE</code></p>
<dd>End relative margin indent and restores the previous value of the prevailing indent.</dl>
<h3>Indented paragraph macros</h3>
<dl>
<dt><code>.HP</code><i> i</i></p>
<dd>Begin paragraph with a hanging indent (the first line of the paragraph is at the left margin of normal paragraphs, and the rest of the paragraph&#8217;s lines are indented).</p>
<dt><code>.IP</code><i> x i</i></p>
<dd>Indented paragraph with optional hanging tag. If the tag <i>x</i> is omitted, the entire following paragraph is indented by <i>i</i>. If the tag <i>x</i> is provided, it is hung at the left margin before the following indented paragraph (this is just like <code>.TP</code> except the tag is included with the command instead of being on the following line). If the tag is too long, the text after the tag will be moved down to the next line (text will not be lost or garbled). For bulleted lists, use this macro with \(bu (bullet) or \(em (em dash) as the tag, and for numbered lists, use the number or letter followed by a period as the tag; this simplifies translation to other formats.</p>
<dt><code>.TP</code><i> i</i></p>
<dd>Begin paragraph with hanging tag. The tag is given on the next line, but its results are like those of the <code>.IP</code> command.</dl>
<h3>Hypertext link macros</h3>
<dl>
<dt><code>.UR</code><i> url</i></p>
<dd>Insert a hypertext link to the URI (URL) <i>url</i>, with all text up to the following <code>.UE</code> macro as the link text.</p>
<dt><code>.UE </code></p>
<dd>[<i>trailer</i>] Terminate the link text of the preceding <code>.UR</code> macro, with the optional <i>trailer</i> (if present, usually a closing parenthesis and/or end-of-sentence punctuation) immediately following. For non-HTML output devices (e.g., <code>man -Tutf8</code>), the link text is followed by the URL in angle brackets; if there is no link text, the URL is printed as its own link text, surrounded by angle brackets. (Angle brackets may not be available on all output devices.) For the HTML output device, the link text is hyperlinked to the URL; if there is no link text, the URL is printed as its own link text.</dl>
<p> These macros have been supported since GNU Troff 1.20 (2009-01-05) and Heirloom Doctools Troff since 160217 (2016-02-17).</p>
<h3>Miscellaneous macros</h3>
<dl>
<dt><code>.DT</code></p>
<dd>Reset tabs to default tab values (every 0.5 inches); does not cause a break.</p>
<dt><code>.PD</code><i> d</i></p>
<dd>Set inter-paragraph vertical distance to d (if omitted, d=0.4v); does not cause a break.</p>
<dt><code>.SS</code><i> t</i></p>
<dd>Subheading <i>t</i> (like <code>.SH</code>, but used for a subsection inside a section).</dl>
<h3>Predefined strings</h3>
<p>The <code>man</code> package has the following predefined strings:</p>
<dl>
<dt>\*R</p>
<dd>Registration Symbol: &#174;</p>
<dt>\*S</p>
<dd>Change to default font size</p>
<dt>\*(Tm</p>
<dd>Trademark Symbol:</p>
<dt>\*(lq</p>
<dd>Left angled double quote: &#8220;</p>
<dt>\*(rq</p>
<dd>Right angled double quote: &#8221;</dl>
<h3>Safe subset</h3>
<p>Although technically <code>man</code> is a troff macro package, in reality a large number of other tools process man page files that don&#8217;t implement all of troff&#8217;s abilities. Thus, it&#8217;s best to avoid some of troff&#8217;s more exotic abilities where possible to permit these other tools to work correctly. Avoid using the various troff preprocessors (if you must, go ahead and use <code><a href="/docs/linux/man/1-tbl/">tbl</a></code>(1), but try to use the <code>IP</code> and <code>TP</code> commands instead for two-column tables). Avoid using computations; most other tools can&#8217;t process them. Use simple commands that are easy to translate to other formats. The following troff macros are believed to be safe (though in many cases they will be ignored by translators): <code>\ ,</code> <code>.</code>, <code>ad</code>, <code>bp</code>, <code>br</code>, <code>ce</code>, <code>de</code>, <code>ds</code>, <code>el</code>, <code>ie</code>, <code>if</code>, <code>fi</code>, <code>ft</code>, <code>hy</code>, <code>ig</code>, <code>in</code>, <code>na</code>, <code>ne</code>, <code>nf</code>, <code>nh</code>, <code>ps</code>, <code>so</code>, <code>sp</code>, <code>ti</code>, <code>tr</code>. </p>
<p> You may also use many troff escape sequences (those sequences beginning with \). When you need to include the backslash character as normal text, use . Other sequences you may use, where x or xx are any characters and N is any digit, include: <code>\&#8217;</code>, <code>\`</code>, <code>\-</code>, <code>\.</code>, <code>\ ,</code> <code>\%</code>, <code>\*x</code>, <code>\*(xx</code>, <code>\(xx</code>, <code>\$N</code>, <code>
x</code>, <code>
(xx</code>, <code>x</code>, and <code>(xx</code>. Avoid using the escape sequences for drawing graphics. </p>
<p> Do not use the optional parameter for <code>bp</code> (break page). Use only positive values for <code>sp</code> (vertical space). Don&#8217;t define a macro (<code>de</code>) with the same name as a macro in this or the mdoc macro package with a different meaning; it&#8217;s likely that such redefinitions will be ignored. Every positive indent (<code>in</code>) should be paired with a matching negative indent (although you should be using the <code>RS</code> and <code>RE</code> macros instead). The condition test (<code>if,ie</code>) should only have &#8216;t&#8217; or &#8216;n&#8217; as the condition. Only translations (<code>tr</code>) that can be ignored should be used. Font changes (<code>ft</code> and the <code></code> escape sequence) should only have the values 1, 2, 3, 4, R, I, B, P, or CW (the ft command may also have no parameters). </p>
<p> If you use capabilities beyond these, check the results carefully on several tools. Once you&#8217;ve confirmed that the additional capability is safe, let the maintainer of this document know about the safe command or sequence that should be added to this list.</p>
<h2>Files</h2>
<p><i>/usr/share/groff/</i>[*/]<i>tmac/an.tmac</i><br />
 <i>/usr/man/whatis</i></p>
<h2>Notes</h2>
<p>By all means include full URLs (or URIs) in the text itself; some tools such as <code><a href="/docs/linux/man/1-man2html/">man2html</a></code>(1) can automatically turn them into hypertext links. You can also use the <code>UR</code> and <code>UE</code> macros to identify links to related information. If you include URLs, use the full URL (e.g., to ensure that tools can automatically find the URLs. </p>
<p> Tools processing these files should open the file and examine the first nonwhitespace character. A period (.) or single quote (&#8216;) at the beginning of a line indicates a troff-based file (such as man or mdoc). A left angle bracket (&lt;) indicates an SGML/XML-based file (such as HTML or Docbook). Anything else suggests simple ASCII text (e.g., a &quot;catman&quot; result). </p>
<p> Many man pages begin with <code>&#8216;\&quot;</code> followed by a space and a list of characters, indicating how the page is to be preprocessed. For portability&#8217;s sake to non-troff translators we recommend that you avoid using anything other than <code><a href="/docs/linux/man/1-tbl/">tbl</a></code>(1), and Linux can detect that automatically. However, you might want to include this information so your man page can be handled by other (less capable) systems. Here are the definitions of the preprocessors invoked by these characters:</p>
<dl>
<dt><code>e</code></p>
<dd><a href="/docs/linux/man/1-eqn/">eqn</a>(1)</p>
<dt><code>g</code></p>
<dd><a href="/docs/linux/man/1-grap/">grap</a>(1)</p>
<dt><code>p</code></p>
<dd><a href="/docs/linux/man/1-pic/">pic</a>(1)</p>
<dt><code>r</code></p>
<dd><a href="/docs/linux/man/1-refer/">refer</a>(1)</p>
<dt><code>t</code></p>
<dd><a href="/docs/linux/man/1-tbl/">tbl</a>(1)</p>
<dt><code>v</code></p>
<dd><a href="/docs/linux/man/1-vgrind/">vgrind</a>(1)</dl>
<h2>Bugs</h2>
<p>Most of the macros describe formatting (e.g., font type and spacing) instead of marking semantic content (e.g., this text is a reference to another page), compared to formats like mdoc and DocBook (even HTML has more semantic markings). This situation makes it harder to vary the <code>man</code> format for different media, to make the formatting consistent for a given media, and to automatically insert cross-references. By sticking to the safe subset described above, it should be easier to automate transitioning to a different reference page format in the future. </p>
<p> The Sun macro <code>TX</code> is not implemented.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-apropos/">apropos</a></code>(1), <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-lexgrog/">lexgrog</a></code>(1), <code><a href="/docs/linux/man/1-man/">man</a></code>(1), <code><a href="/docs/linux/man/1-man2html/">man2html</a></code>(1), <code><a href="/docs/linux/man/7-groff_mdoc/">groff_mdoc</a></code>(7), <code><a href="/docs/linux/man/1-whatis/">whatis</a></code>(1), <code><a href="/docs/linux/man/7-groff_man/">groff_man</a></code>(7), <code><a href="/docs/linux/man/7-groff_www/">groff_www</a></code>(7), <code><a href="/docs/linux/man/7-man-pages/">man-pages</a></code>(7), <code><a href="/docs/linux/man/7-mdoc/">mdoc</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
