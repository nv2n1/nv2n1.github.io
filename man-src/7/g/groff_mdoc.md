---
title: "groff_mdoc(7)"
name: "groff_mdoc"
section: "7"
letter: "g"
url: "/docs/linux/man/7-groff_mdoc/"
description: "‘ macro is mandatory. If not specified, headers, footers and page layout defaults will not be set and things will be rather unpleasant. The NAME section consists of at least three items. The first ..."
---

<p><code>groff_mdoc</code> &#8211; reference for groff&#8217;s mdoc implementation</p>
<h2>Synopsis</h2>
<p><code>groff -m doc </code><i>file &#8230;</i></p>
<h2>Description</h2>
<p>A complete reference for writing UNIX manual pages with the <code>-mdoc</code> macro package; a <i>content </i><code>-based</code> and <i>domain </i><code>-based</code> formatting package for <code>GNU</code> <a href="/docs/linux/man/1-troff/">troff</a>(1). Its predecessor, the -man7 package, addressed page layout leaving the manipulation of fonts and other typesetting details to the individual author. In <code>-mdoc</code> page layout macros make up the <i>page structure domain</i> which consists of macros for titles, section headers, displays and lists &#8211; essentially items which affect the physical position of text on a formatted page. In addition to the page structure domain, there are two more domains, the <i>manual</i> domain and the <i>general</i> text domain. The general text domain is defined as macros which perform tasks such as quoting or emphasizing pieces of text. The manual domain is defined as macros that are a subset of the day to day informal language used to describe commands, routines and related UNIX files. Macros in the manual domain handle command names, command-line arguments and options, function names, function parameters, pathnames, variables, cross references to other manual pages, and so on. These domain items have value for both the author and the future user of the manual page. Hopefully, the consistency gained across the manual set will provide easier translation to future documentation tools. </p>
<p> Throughout the UNIX manual pages, a manual entry is simply referred to as a man page, regardless of actual length and without sexist intention.</p>
<h2>Getting Started</h2>
<p>The material presented in the remainder of this document is outlined as follows: </p>
<ol>
<li> <code>TROFF IDIOSYNCRASIES</code>
<dl>
<dt><code>&quot;Macro Usage&quot;</code></p>
<dd>
<dt><code>&quot;Passing Space Characters in an Argument&quot;</code></p>
<dd>
<dt><code>&quot;Trailing Blank Space Characters&quot;</code></p>
<dd>
<dt><code>&quot;Escaping Special Characters&quot;</code></p>
<dd>
<dt><code>&quot;Other Possible Pitfalls&quot;</code></p>
<dd></dl>
<li> <code>A MANUAL PAGE TEMPLATE</code>
<li> <code>CONVENTIONS</code>
<li> <code>TITLE MACROS</code>
<li> <code>INTRODUCTION OF MANUAL AND GENERAL TEXT DOMAINS</code>
<dl>
<dt><code>&quot;What&#8217;s in a Name&quot; &#8230;</code></p>
<dd>
<dt><code>&quot;General Syntax&quot;</code></p>
<dd></dl>
<li> <code>MANUAL DOMAIN</code>
<dl>
<dt><code>&quot;Addresses&quot;</code></p>
<dd>
<dt><code>&quot;Author Name&quot;</code></p>
<dd>
<dt><code>&quot;Arguments&quot;</code></p>
<dd>
<dt><code>&quot;Configuration Declarations (Section Four Only)&quot;</code></p>
<dd>
<dt><code>&quot;Command Modifiers&quot;</code></p>
<dd>
<dt><code>&quot;Defined Variables&quot;</code></p>
<dd>
<dt><code>&quot;Errno&#8217;s&quot;</code></p>
<dd>
<dt><code>&quot;Environment Variables&quot;</code></p>
<dd>
<dt><code>&quot;Flags&quot;</code></p>
<dd>
<dt><code>&quot;Function Declarations&quot;</code></p>
<dd>
<dt><code>&quot;Function Types&quot;</code></p>
<dd>
<dt><code>&quot;Functions (Library Routines)&quot;</code></p>
<dd>
<dt><code>&quot;Function Arguments&quot;</code></p>
<dd>
<dt><code>&quot;Return Values&quot;</code></p>
<dd>
<dt><code>&quot;Exit Status&quot;</code></p>
<dd>
<dt><code>&quot;Interactive Commands&quot;</code></p>
<dd>
<dt><code>&quot;Library Names&quot;</code></p>
<dd>
<dt><code>&quot;Literals&quot;</code></p>
<dd>
<dt><code>&quot;Names&quot;</code></p>
<dd>
<dt><code>&quot;Options&quot;</code></p>
<dd>
<dt><code>&quot;Pathnames&quot;</code></p>
<dd>
<dt><code>&quot;Standards&quot;</code></p>
<dd>
<dt><code>&quot;Variable Types&quot;</code></p>
<dd>
<dt><code>&quot;Variables&quot;</code></p>
<dd>
<dt><code>&quot;Manual Page Cross References&quot;</code></p>
<dd></dl>
<li> <code>GENERAL TEXT DOMAIN</code>
<dl>
<dt><code>&quot;AT&amp;T Macro&quot;</code></p>
<dd>
<dt><code>&quot;BSD Macro&quot;</code></p>
<dd>
<dt><code>&quot;NetBSD Macro&quot;</code></p>
<dd>
<dt><code>&quot;FreeBSD Macro&quot;</code></p>
<dd>
<dt><code>&quot;DragonFly Macro&quot;</code></p>
<dd>
<dt><code>&quot;OpenBSD Macro&quot;</code></p>
<dd>
<dt><code>&quot;BSD/OS Macro&quot;</code></p>
<dd>
<dt><code>&quot;UNIX Macro&quot;</code></p>
<dd>
<dt><code>&quot;Emphasis Macro&quot;</code></p>
<dd>
<dt><code>&quot;Font Mode&quot;</code></p>
<dd>
<dt><code>&quot;Enclosure and Quoting Macros&quot;</code></p>
<dd>
<dt><code>&quot;No-</code>[or Normal Text Macro]</p>
<dd>
<dt><code>&quot;No-Space Macro&quot;</code></p>
<dd>
<dt><code>&quot;Section Cross References&quot;</code></p>
<dd>
<dt><code>&quot;Symbolics&quot;</code></p>
<dd>
<dt><code>&quot;Mathematical Symbols&quot;</code></p>
<dd>
<dt><code>&quot;References and Citations&quot;</code></p>
<dd>
<dt><code>&quot;Trade Names (or Acronyms and Type Names)&quot;</code></p>
<dd>
<dt><code>&quot;Extended Arguments&quot;</code></p>
<dd></dl>
<li> <code>PAGE STRUCTURE DOMAIN</code>
<dl>
<dt><code>&quot;Section Headers&quot;</code></p>
<dd>
<dt><code>&quot;Subsection Headers&quot;</code></p>
<dd>
<dt><code>&quot;Paragraphs and Line Spacing&quot;</code></p>
<dd>
<dt><code>&quot;Keeps&quot;</code></p>
<dd>
<dt><code>&quot;Examples and Displays&quot;</code></p>
<dd>
<dt><code>&quot;Lists and Columns&quot;</code></p>
<dd></dl>
<li> <code>MISCELLANEOUS MACROS</code>
<li> <code>PREDEFINED STRINGS</code>
<li> <code>DIAGNOSTICS</code>
<li> <code>FORMATTING WITH GROFF, TROFF, AND NROFF</code>
<li> <code>FILES</code>
<li> <code>SEE ALSO</code>
<li> <code>BUGS</code> </ol>
<h2>Troff Idiosyncrasies</h2>
<p>The <code>-mdoc</code> package attempts to simplify the process of writing a man page. Theoretically, one should not have to learn the tricky details of <code>GNU</code> <a href="/docs/linux/man/1-troff/">troff</a>(1) to use <code>-mdoc</code> however, there are a few limitations which are unavoidable and best gotten out of the way. And, too, be forewarned, this package is <i>not</i> fast.</p>
<h3>Macro Usage</h3>
<p>As in <code>GNU</code> <a href="/docs/linux/man/1-troff/">troff</a>(1), a macro is called by placing a `.&#8217; (dot character) at the beginning of a line followed by the two-character (or three-character) name for the macro. There can be space or tab characters between the dot and the macro name. Arguments may follow the macro separated by spaces (but <i>no</i> tabs). It is the dot character at the beginning of the line which causes <code>GNU</code> <a href="/docs/linux/man/1-troff/">troff</a>(1) to interpret the next two (or more) characters as a macro name. A single starting dot followed by nothing is ignored. To place a `.&#8217; (dot character) at the beginning of an input line in some context other than a macro invocation, precede the `.&#8217; (dot) with the `\&amp;&#8217; escape sequence which translates literally to a zero-width space, and is never displayed in the output. </p>
<p> In general, <code>GNU</code> <a href="/docs/linux/man/1-troff/">troff</a>(1) macros accept an unlimited number of arguments (contrary to other versions of troff which can&#8217;t handle more than nine arguments). In limited cases, arguments may be continued or extended on the next line (See Sx Extended Arguments below). Almost all macros handle quoted arguments (see Sx Passing Space Characters in an Argument below). </p>
<p> Most of the <code>-mdoc</code> general text domain and manual domain macros are special in that their argument lists are <i>parsed</i> for callable macro names. This means an argument on the argument list which matches a general text or manual domain macro name (and which is defined to be callable) will be executed or called when it is processed. In this case the argument, although the name of a macro, is not preceded by a `.&#8217; (dot). This makes it possible to nest macros; for example the option macro, `.[,] &#8216; may <i>call</i> the flag and argument macros, `- &#8216; and `<i>file &#8230;</i> &#8216; to specify an optional flag with an argument:</p>
<dl>
<dt>[-<code>s </code><i>bytes</i> ]</p>
<dd>is produced by `.[-<code>s</code> ] &#8216; Ar bytes</dl>
<p> To prevent a string from being interpreted as a macro name, precede the string with the escape sequence `\&amp;&#8217; :</p>
<dl>
<dt>[-<code>s </code><i>bytes</i> ]</p>
<dd>is produced by `.[\&amp;-<code>s</code> ] &#8216; \&amp;Ar bytes</dl>
<p> Here the strings `- &#8216; and `<i>file &#8230;</i> &#8216; are not interpreted as macros. Macros whose argument lists are parsed for callable arguments are referred to as <i>parsed</i> and macros which may be called from an argument list are referred to as <i>callable</i> throughout this document. This is a technical <i>faux pas</i> as almost all of the macros in <code>-mdoc</code> are parsed, but as it was cumbersome to constantly refer to macros as being callable and being able to call other macros, the term parsed has been used. </p>
<p> In the following, we call an <code>-mdoc</code> macro which starts a line (with a leading dot) a <i>command</i> if this distinction is necessary.</p>
<h3>Passing Space Characters in an Argument</h3>
<p>Sometimes it is desirable to give as an argument a string containing one or more blank space characters, say, to specify arguments to commands which expect particular arrangement of items in the argument list. Additionally, it makes <code>-mdoc</code> working faster. For example, the function command `.Fn expects &#8216; the first argument to be the name of a function and any remaining arguments to be function parameters. As <code>ANSI~C</code> stipulates the declaration of function parameters in the parenthesized parameter list, each parameter is guaranteed to be at minimum a two word string. For example, Fa int foo . </p>
<p> There are two possible ways to pass an argument which contains an embedded space. One way of passing a string containing blank spaces is to use the hard or unpaddable space character `\<br />
&nbsp;,&#8217; that is, a blank space preceded by the escape character `\&#8217; This method may be used with any macro but has the side effect of interfering with the adjustment of text over the length of a line. Troff sees the hard space as if it were any other printable character and cannot split the string into blank or newline separated pieces as one would expect. This method is useful for strings which are not expected to overlap a line boundary. An alternative is to use `\~&#8217; , a paddable (i.e. stretchable), unbreakable space (this is a <code>GNU</code> <a href="/docs/linux/man/1-troff/">troff</a>(1) extension). The second method is to enclose the string with double quotes. </p>
<p> For example:</p>
<dl>
<dt><code>Fn </code>fetch char&nbsp;*str</p>
<dd>is created by `.Fn fetch &#8216; char\ *str</p>
<dt><code>Fn </code>fetch char *str</p>
<dd>can also be created by `.Fn fetch &#8216; &quot;char *str&quot;</dl>
<p> If the `\&#8217; before the space in the first example or double quotes in the second example were omitted, `.Fn would &#8216; see three arguments, and the result would be: </p>
<blockquote><p><tt>Fn </tt>fetch char *str </p></blockquote>
<h3>Trailing Blank Space Characters</h3>
<p>Troff can be confused by blank space characters at the end of a line. It is a wise preventive measure to globally remove all blank spaces from Ao blank-space Ac Ns Ao end-of-line Ac character sequences. Should the need arise to use a blank character at the end of a line, it may be forced with an unpaddable space and the `\&amp;&#8217; escape character. For example, `string\&amp; .&#8217;</p>
<h3>Escaping Special Characters</h3>
<p>Special characters like the newline character `
&#8217; are handled by replacing the `\&#8217; with `&#8217; (e.g. `n&#8217; ) to preserve the backslash.</p>
<h3>Other Possible Pitfalls</h3>
<p>A warning is emitted when an empty input line is found outside of displays (see below). Use `.sp&#8217; instead. (Well, it is even better to use <code>-mdoc</code> macros to avoid the usage of low-level commands.) </p>
<p> Leading spaces will cause a break and are output directly. Avoid this behaviour if possible. Similarly, do not use more than one space character between words in an ordinary text line; contrary to other text formatters, they are <i>not</i> replaced with a single space. </p>
<p> You can&#8217;t pass `&quot;&#8217; directly as an argument. Use `\*[q]&#8217; (or `\*q&#8217; ) instead. </p>
<p> By default, <a href="/docs/linux/man/1-troff/">troff</a>(1) inserts two space characters after a punctuation mark closing a sentence; characters like `)&#8217; or `&#8221; are treated transparently, not influencing the sentence-ending behaviour. To change this, insert `\&amp;&#8217; before or after the dot: </p>
<blockquote>
<pre>The
.Ql .
character.
.Pp
The
.Ql \&amp;.
character.
.Pp
.No test .
test
.Pp
.No test.
test</pre>
</blockquote>
<p> gives </p>
<blockquote><p> The `.&#8217; character </p>
<p> The `.&#8217; character. </p>
<p> <code>test</code> test </p>
<p> <code>test.</code> test </p></blockquote>
<p> As can be seen in the first and third line, <code>-mdoc</code> handles punctuation characters specially in macro arguments. This will be explained in section Sx General Syntax below. In the same way, you have to protect trailing full stops of abbreviations with a trailing zero-width space: `e.g.\&amp;&#8217; </p>
<p> A comment in the source file of a man page can be either started with `.\&#8217; on a single line, `\&#8217; after some input, or `\#&#8217; anywhere (the latter is a <code>GNU</code> <a href="/docs/linux/man/1-troff/">troff</a>(1) extension); the rest of such a line is ignored.</p>
<h2>A Manual Page Template</h2>
<p>The body of a man page is easily constructed from a basic template: </p>
<blockquote>
<pre>.\&quot; The following commands are required for all man pages.
.Dd Month day, year
.Dt DOCUMENT_TITLE [section number] [architecture/volume]
.Os [OPERATING_SYSTEM] [version/release]
.Sh NAME
.Nm name
.Nd one line description of name
.\&quot; This next command is for sections 2 and 3 only.
.\&quot; .Sh LIBRARY
.Sh SYNOPSIS
.Sh DESCRIPTION
.\&quot; The following commands should be uncommented and
.\&quot; used where appropriate.
.\&quot; .Sh IMPLEMENTATION NOTES
.\&quot; This next command is for sections 2, 3, and 9 only
.\&quot; (function return values).
.\&quot; .Sh RETURN VALUES
.\&quot; This next command is for sections 1, 6, 7, and 8 only.
.\&quot; .Sh ENVIRONMENT
.\&quot; .Sh FILES
.\&quot; This next command is for sections 1, 6, and 8 only
.\&quot; (command return values to the shell).
.\&quot; .Sh EXIT STATUS
.\&quot; .Sh EXAMPLES
.\&quot; This next command is for sections 1, 4, 6, 7, 8, and 9 only
.\&quot; (fprintf/stderr type diagnostics).
.\&quot; .Sh DIAGNOSTICS
.\&quot; .Sh COMPATIBILITY
.\&quot; This next command is for sections 2, 3, 4, and 9 only
.\&quot; (settings of the errno variable).
.\&quot; .Sh ERRORS
.\&quot; .Sh SEE ALSO
.\&quot; .Sh STANDARDS
.\&quot; .Sh HISTORY
.\&quot; .Sh AUTHORS
.\&quot; .Sh CAVEATS
.\&quot; .Sh BUGS</pre>
</blockquote>
<p> The first items in the template are the commands `., &#8216; `. &#8216; and `.; &#8216; the document date, the operating system the man page or subject source is developed or modified for, and the man page title (in <i>upper case</i> along with the section of the manual the page belongs in. These commands identify the page and are discussed below in Sx TITLE MACROS . </p>
<p> The remaining items in the template are section headers ( <code>.</code></p>
<h2>)</h2>
<p>of which <i>NAME</i> <i>SYNOPSIS</i> and <i>DESCRIPTION</i> are mandatory. The headers are discussed in Sx PAGE STRUCTURE DOMAIN , after presentation of Sx MANUAL DOMAIN . Several content macros are used to demonstrate page layout macros; reading about content macros before page layout macros is recommended.</p>
<h2>Conventions</h2>
<p>In the description of all macros below, optional arguments are put into brackets. An ellipsis ( `&#8230;&#8217; represents zero or more additional arguments. Alternative values for a parameter are separated with `|&#8217; If there are alternative values for a mandatory parameter, braces are used (together with `|&#8217; ) to enclose the value set. Meta-variables are specified within angles. </p>
<p> Example:</p>
<dl>
<dt><code>.Xx </code> Aq foo Br q bar1 | bar2 [-test1 [-test2 | -test3] ] <code>&#8230;</code></p>
<dd></dl>
<dd>Except stated explicitly, all macros are parsed and callable. </p>
<p> Note that a macro takes effect up to the next nested macro. For example, `.<code>foo</code> &#8216; Aq bar doesn&#8217;t produce `<code>foo &lt;bar&gt;</code> &#8216; but `<code>foo Aq </code>bar &#8216; Consequently, a warning message is emitted for most commands if the first argument is a macro itself since it cancels the effect of the calling command completely. Another consequence is that quoting macros never insert literal quotes; `<code>foo &lt;bar&gt;</code> &#8216; has been produced by `.<code>&quot;foo</code> &#8216; &lt;bar&gt;&quot; . </p>
<p> Most macros have a default width value which can be used to specify a label width ( &#8211;<code>width</code> or offset ( &#8211;<code>offset</code> for the `.</p>
<dl>
<p> &#8216; and `. &#8216; macros. It is recommended not to use this rather obscure feature to avoid dependencies on local modifications of the <code>-mdoc</code> package.</dl>
</dl>
<h2>Title Macros</h2>
<p>The title macros are part of the page structure domain but are presented first and separately for someone who wishes to start writing a man page yesterday. Three header macros designate the document title or manual page title, the operating system, and the date of authorship. These macros are called once at the very beginning of the document and are used to construct headers and footers only.</p>
<dl>
<dt><code>. </code></p>
<dd>[Aq document title ] [Aq section number ] [Aq volume ] The document title is the subject of the man page and must be in <code>CAPITALS</code> due to troff limitations. If omitted, `<code>UNTITLED</code> &#8216; is used. The section number may be a number in the range <code>1,~ &#8230; ,~9</code> or `unass&#8217; , `draft&#8217; , or `paper&#8217; If it is specified, and no volume name is given, a default volume name is used. </p>
<p> Under the following sections are defined: </p>
<table>
<tr VALIGN=top>
<td>1</td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>3</td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>4</td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>5</td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>6</td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>7</td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>8</td>
<td> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>9</td>
<td> </td>
<td>
</td>
</tr>
</table>
<p> A volume name may be arbitrary or one of the following: </p>
<table>
<tr VALIGN=top>
<td>USD</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>PS1</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>AMD</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>SMM</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>URM</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>PRM</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>KM </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>IND</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>LOCAL</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>CON</td>
<td>
</td>
</tr>
</table>
<p> For compatibility, `MMI&#8217; can be used for `IND&#8217; , and `LOC&#8217; for `LOCAL&#8217; Values from the previous table will specify a new volume name. If the third parameter is a keyword designating a computer architecture, its value is prepended to the default volume name as specified by the second parameter. By default, the following architecture keywords are defined: # we use &#8216;No&#8217; to avoid hyphenation </p>
<blockquote><p> <code>acorn26 , acorn32 , algor , alpha , amd64 , amiga , amigappc</code> <code>arc , arm , arm26 , arm32 , armish , atari , aviion</code> <code>beagle , bebox , cats , cesfic , cobalt , dreamcast</code> <code>emips , evbarm , evbmips , evbppc , evbsh3 , ews4800mips</code> <code>hp300 , hp700 , hpcarm , hpcmips , hpcsh , hppa , hppa64</code> <code>i386 , ia64 , ibmnws , iyonix , landisk , loongson , luna68k , luna88k</code> <code>m68k , mac68k , macppc , mips , mips64 , mipsco , mmeye</code> <code>mvme68k , mvme88k , mvmeppc , netwinder , news68k , newsmips , next68k</code> <code>ofppc , palm , pc532 , playstation2 , pmax , pmppc , powerpc , prep</code> <code>rs6000 , sandpoint , sbmips , sgi , sgimips , sh3 , shark</code> <code>socppc , solbourne , sparc , sparc64 , sun2 , sun3</code> <code>tahoe , vax , x68k , x86_64 , xen , zaurus</code> </p></blockquote>
<p> If the section number is neither a numeric expression in the range 1 to~9 nor one of the above described keywords, the third parameter is used verbatim as the volume name. </p>
<p> In the following examples, the left (which is identical to the right) and the middle part of the manual page header strings are shown. Note how `\&amp;&#8217; prevents the digit~7 from being a valid numeric expression.</p>
<dl>
<dt><code>. </code></p>
<dd>`<a href="/docs/linux/man/7-foo/">FOO</a>(7)&#8217; `&#8217;</p>
<dt><code>. </code></p>
<dd>`<a href="/docs/linux/man/7-foo/">FOO</a>(7)&#8217; `&#8217;</p>
<dt><code>. </code></p>
<dd>`<a href="/docs/linux/man/7-foo/">FOO</a>(7)&#8217; `bar&#8217;</p>
<dt><code>. </code></p>
<dd>`<a href="/docs/linux/man/2-foo/">FOO</a>(2)&#8217; `/&#8217;</p>
<dt><code>. </code></p>
<dd>`FOO&#8217; `bar&#8217;</dl>
<p> Local, OS-specific additions might be found in the file mdoc.local look for strings named `volume-ds-XXX&#8217; (for the former type) and `volume-as-XXX&#8217; (for the latter type); `XXX&#8217; then denotes the keyword to be used with the `. &#8216; macro. </p>
<p> This macro is neither callable nor parsed.</p>
<dt><code>. </code> [Aq operating system ] [Aq release ]</p>
<dd>
<dd>If the first parameter is empty, the default ` &#8216; is used. This may be overridden in the local configuration file, mdoc.local In general, the name of the operating system should be the common acronym, e.g. <code>BSD</code> or <code>ATT</code> The release should be the standard release nomenclature for the system specified. In the following table, the possible second arguments for some predefined operating systems are listed. Similar to `. &#8216; local additions might be defined in mdoc.local look for strings named `operating-system-XXX-YYY&#8217; , where `XXX&#8217; is the acronym for the operating system and `YYY&#8217; the release ID.</p>
<dl>
<dt><code>ATT</code></p>
<dd>7th, 7, III, 3, V, V.2, V.3, V.4</p>
<dt><code>BSD</code></p>
<dd>3, 4, 4.1, 4.2, 4.3, 4.3t, 4.3T, 4.3r, 4.3R, 4.4</p>
<dt><code>NetBSD</code></p>
<dd>0.8, 0.8a, 0.9, 0.9a, 1.0, 1.0a, 1.1, 1.2, 1.2a, 1.2b, 1.2c, 1.2d, 1.2e, 1.3, 1.3a, 1.4, 1.4.1, 1.4.2, 1.4.3, 1.5, 1.5.1, 1.5.2, 1.5.3, 1.6, 1.6.1, 1.6.2, 1.6.3, 2.0, 2.0.1, 2.0.2, 2.0.3, 2.1, 3.0, 3.0.1, 3.0.2, 3.0.3, 3.1, 3.1.1, 4.0, 4.0.1, 5.0, 5.0.1, 5.0.2, 5.1, 5.1.2, 5.1.3, 5.1.4, 5.2, 5.2.1, 5.2.2, 6.0, 6.0.1, 6.0.2, 6.0.3, 6.0.4, 6.0.5, 6.0.6, 6.1, 6.1.1, 6.1.2, 6.1.3, 6.1.4, 6.1.5, 7.0, 7.0.1, 7.0.2, 7.1, 7.1.1, 7.1.2, 7.2, 8.0, 8.1</p>
<dt><code>FreeBSD</code></p>
<dd>1.0, 1.1, 1.1.5, 1.1.5.1, 2.0, 2.0.5, 2.1, 2.1.5, 2.1.6, 2.1.7, 2.2, 2.2.1, 2.2.2, 2.2.5, 2.2.6, 2.2.7, 2.2.8, 2.2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 4.0, 4.1, 4.1.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.6.2, 4.7, 4.8, 4.9, 4.10, 4.11, 5.0, 5.1, 5.2, 5.2.1, 5.3, 5.4, 5.5, 6.0, 6.1, 6.2, 6.3, 6.4, 7.0, 7.1, 7.2, 7.3, 7.4, 8.0, 8.1, 8.2, 8.3, 8.4, 9.0, 9.1, 9.2, 9.3, 10.0, 10.1, 10.2, 10.3, 10.4, 11.0, 11.1, 11.2, 11.3, 12.0, 12.1</p>
<dt><code>OpenBSD</code></p>
<dd>2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6</p>
<dt><code>DragonFly</code></p>
<dd>1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.8.1, 1.9, 1.10, 1.11, 1.12, 1.12.2, 1.13, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 2.9.1, 2.10, 2.10.1, 2.11, 2.12, 2.13, 3.0, 3.0.1, 3.0.2, 3.1, 3.2, 3.2.1, 3.2.2, 3.3, 3.4, 3.4.1, 3.4.2, 3.4.3, 3.5, 3.6, 3.6.1, 3.6.2, 3.7, 3.8, 3.8.1, 3.8.2, 4.0, 4.0.1, 4.0.2, 4.0.3, 4.0.4, 4.0.5, 4.0.6, 4.1, 4.2, 4.2.1, 4.2.2, 4.2.3, 4.2.4, 4.3, 4.4, 4.4.1, 4.4.2, 4.4.3, 4.5, 4.6, 4.6.1, 4.6.2, 4.7, 4.8, 4.8.1, 4.9, 5.0, 5.0.1, 5.0.2, 5.1, 5.2, 5.2.1, 5.2.2, 5.3, 5.4, 5.4.1, 5.4.2, 5.4.3, 5.5, 5.6, 5.6.1, 5.6.2</p>
<dt><code>Darwin</code></p>
<dd>8.0.0, 8.1.0, 8.2.0, 8.3.0, 8.4.0, 8.5.0, 8.6.0, 8.7.0, 8.8.0, 8.9.0, 8.10.0, 8.11.0, 9.0.0, 9.1.0, 9.2.0, 9.3.0, 9.4.0, 9.5.0, 9.6.0, 9.7.0, 9.8.0, 10.0.0, 10.1.0, 10.2.0, 10.3.0, 10.4.0, 10.5.0, 10.6.0, 10.7.0, 10.8.0, 11.0.0, 11.1.0, 11.2.0, 11.3.0, 11.4.0, 11.5.0, 12.0.0, 12.1.0, 12.2.0, 13.0.0, 13.1.0, 13.2.0, 13.3.0, 13.4.0, 14.0.0, 14.1.0, 14.2.0, 14.3.0, 14.4.0, 14.5.0, 15.0.0, 15.1.0, 15.2.0, 15.3.0, 15.4.0, 15.5.0, 15.6.0, 16.0.0, 16.1.0, 16.2.0, 16.3.0, 16.4.0, 16.5.0, 16.6.0, 17.0.0, 17.1.0, 17.2.0, 17.3.0, 17.4.0, 17.5.0, 17.6.0, 17.7.0, 18.0.0, 18.1.0, 18.2.0, 18.3.0, 18.4.0, 18.5.0, 18.6.0, 18.7.0, 19.0.0, 19.1.0, 19.2.0</dl>
<p> For <code>ATT</code> an unknown second parameter will be replaced with the string <code>UNIX</code> for the other predefined acronyms it will be ignored and a warning message emitted. Unrecognized arguments are displayed as given in the page footer. For instance, a typical footer might be: </p>
<blockquote><p><tt>.BSD 4.3 </tt></p></blockquote>
<p> giving `4.3~Berkeley&#8217; Distribution , or for a locally produced set </p>
<blockquote><p><tt>.CS Department </tt></p></blockquote>
<p> which will produce `CS~Department&#8217; </p>
<p> If the `.macro &#8216; is not present, the bottom left corner of the manual page will be ugly. </p>
<p> This macro is neither callable nor parsed.</p>
<dt><code>.</code>[Aq month</p>
<dd>Aq day , Aq year ] If `has &#8216; no arguments, `Epoch&#8217; is used for the date string. If it has exactly three arguments, they are concatenated, separated with unbreakable space: </p>
<blockquote><p><tt>.January 25, 2001 </tt></p></blockquote>
<p> The month&#8217;s name shall not be abbreviated. </p>
<p> With any other number of arguments, the current date is used, ignoring the parameters. </p>
<p> As a special exception, the format </p>
<blockquote><p> <code>.$Mdocdate: </code> Aq month Aq day Aq year <code>$</code> </p></blockquote>
<p> is also recognized. It is used in Ox manuals to automatically insert the current date when committing. </p>
<p> This macro is neither callable nor parsed.</dl>
<h2>Introduction Of Manual And General Text Domains</h2>
<h3>What&#8217;s in a Name <code>&#8230;</code></h3>
<p>The manual domain macro names are derived from the day to day informal language used to describe commands, subroutines and related files. Slightly different variations of this language are used to describe the three different aspects of writing a man page. First, there is the description of <code>-mdoc</code> macro command usage. Second is the description of a UNIX command <i>with</i> <code>-mdoc</code> macros, and third, the description of a command to a user in the verbal sense; that is, discussion of a command in the text of a man page. </p>
<p> In the first case, <a href="/docs/linux/man/1-troff/">troff</a>(1) macros are themselves a type of command; the general syntax for a troff command is: </p>
<blockquote><p> <code>.Xx </code>argument1 argument2 &#8230; </p></blockquote>
<p> `.Xx is &#8216; a macro command, and anything following it are arguments to be processed. In the second case, the description of a UNIX command using the content macros is a bit more involved; a typical Sx SYNOPSIS command line might be displayed as: </p>
<blockquote><p> <code>filter</code> [-<code>flag</code> ] Ao Ar infile Ac Ao Ar outfile Ac </p></blockquote>
<p> Here, <code>filter</code> is the command name and the bracketed string &#8211;<code>flag</code> is a <i>flag</i> argument designated as optional by the option brackets. In <code>-mdoc</code> terms, Ao Ar infile Ac and Ao Ar outfile Ac are called <i>meta arguments</i> in this example, the user has to replace the meta expressions given in angle brackets with real file names. Note that in this document meta arguments are used to describe <code>-mdoc</code> commands; in most man pages, meta variables are not specifically written with angle brackets. The macros which formatted the above example: </p>
<blockquote>
<pre>.Nm filter
.Op Fl flag
.Ao Ar infile Ac Ao Ar outfile Ac</pre>
</blockquote>
<p> In the third case, discussion of commands and command syntax includes both examples above, but may add more detail. The arguments Ao Ar infile Ac and Ao Ar outfile Ac from the example above might be referred to as <i>operands</i> or <i>file arguments</i> Some command-line argument lists are quite long:</p>
<dl>
<dt><code>make</code></p>
<dd>[-<code>eiknqrstv</code> ] [-<code>D </code><i>variable</i> ] [-<code>d </code><i>flags</i> ] [-<code>f </code><i>makefile</i> ] [-<code>I </code><i>directory</i> ] [-<code>j </code><i>max_jobs</i> ] [<i>variable </i><code>= </code><i>value</i> ] [<i>target &#8230;</i> ]</dl>
<p> Here one might talk about the command <code>make</code> and qualify the argument, <i>makefile</i> as an argument to the flag, &#8211;<code>f</code> or discuss the optional file operand <i>target</i> In the verbal context, such detail can prevent confusion, however the <code>-mdoc</code> package does not have a macro for an argument <i>to</i> a flag. Instead the `<i>file &#8230;</i> &#8216; argument macro is used for an operand or file argument like <i>target</i> as well as an argument to a flag like <i>variable</i> The make command line was produced from: </p>
<blockquote>
<pre>.Nm make
.Op Fl eiknqrstv
.Op Fl D Ar variable
.Op Fl d Ar flags
.Op Fl f Ar makefile
.Op Fl I Ar directory
.Op Fl j Ar max_jobs
.Op Ar variable Ns = Ns Ar value
.Bk
.Op Ar target ...
.Ek</pre>
</blockquote>
<p> The `.and &#8216; `.macros &#8216; are explained in Sx Keeps .</p>
<h3>General Syntax</h3>
<p>The manual domain and general text domain macros share a similar syntax with a few minor deviations; most notably, `.<i>file &#8230;</i> &#8216; `.- &#8216; `.<code>groff Fl m Ns Cm doc Ar</code> &#8216; and `.differ &#8216; only when called without arguments; and `.Fn and &#8216; `.impose &#8216; an order on their argument lists. All content macros are capable of recognizing and properly handling punctuation, provided each punctuation character is separated by a leading space. If a command is given: </p>
<blockquote><p><tt>.</tt><i>sptr, ptr),</i> </p></blockquote>
<p> The result is: </p>
<blockquote><p><tt></tt><i>sptr, ptr),</i> </p></blockquote>
<p> The punctuation is not recognized and all is output in the font used by `.<i>file &#8230;</i> &#8216; If the punctuation is separated by a leading white space: </p>
<blockquote><p><tt>.</tt><i>sptr , ptr ) ,</i> </p></blockquote>
<p> The result is: </p>
<blockquote><p><tt></tt><i>sptr , ptr</i> </p></blockquote>
<p> The punctuation is now recognized and output in the default font distinguishing it from the argument strings. To remove the special meaning from a punctuation character escape it with `\&amp;&#8217; </p>
<p> The following punctuation characters are recognized by <code>-mdoc</code></p>
<dl>
<dt><code>. Ta </code><code>, Ta </code><code>: Ta </code><code>; Ta </code><code>(</code></p>
<dd>
<dt><code>) Ta </code><code>[ Ta </code><code>] Ta </code><code>? Ta </code><code>!</code></p>
<dd></dl>
<p> Troff is limited as a macro language, and has difficulty when presented with a string containing a member of the mathematical, logical or quotation set: </p>
<blockquote>
<pre>{+,-,/,*,%,&lt;,&gt;,&lt;=,&gt;=,=,==,&amp;,`,',&quot;}</pre>
</blockquote>
<p> The problem is that troff may assume it is supposed to actually perform the operation or evaluation suggested by the characters. To prevent the accidental evaluation of these characters, escape them with `\&amp;&#8217; Typical syntax is shown in the first content macro displayed below, `.<i></i> &#8216;</p>
<h2>Manual Domain</h2>
<h3>Addresses</h3>
<p>The address macro identifies an address construct. </p>
<blockquote><p><tt>Usage: .</tt><i>Ao </i>address Ac &#8230; </p></blockquote>
<dl>
<dt><code>.</code><i>addr1</i></p>
<dd><i>addr1</i></p>
<dt><code>.</code><i>addr1 .</i></p>
<dd><i>addr1</i></p>
<dt><code>.</code><i>addr1 , file2</i></p>
<dd><i>addr1 , file2</i></p>
<dt><code>.</code><i>f1 , f2 , f3 :</i></p>
<dd><i>f1 , f2 , f3</i></p>
<dt><code>.</code><i>addr ) ) ,</i></p>
<dd><i>addr ) )</i></dl>
<p> The default width is 12n.</p>
<h3>Author Name</h3>
<p>The `.An macro &#8216; is used to specify the name of the author of the item being documented, or the name of the author of the actual manual page. </p>
<blockquote><p><tt>Usage: .An </tt>Ao author name Ac &#8230; </p></blockquote>
<dl>
<dt><code>.An </code>&quot;Joe Author&quot;</p>
<dd>An Joe Author</p>
<dt><code>.An </code>&quot;Joe Author&quot; ,</p>
<dd>An Joe Author ,</p>
<dt><code>.An </code>&quot;Joe Author&quot; Aq nobody [at] FreeBSD.org</p>
<dd>An Joe Author Aq nobody [at] FreeBSD.org</p>
<dt><code>.An </code>&quot;Joe Author&quot; ) ) ,</p>
<dd>An Joe Author ) ) ,</dl>
<p> The default width is 12n. </p>
<p> In the <i>AUTHORS</i> section, the `.An command &#8216; causes a line break allowing each new name to appear on its own line. If this is not desirable, </p>
<blockquote>
<pre>.An -nosplit</pre>
</blockquote>
<p> call will turn this off. To turn splitting back on, write </p>
<blockquote>
<pre>.An -split</pre>
</blockquote>
<h3>Arguments</h3>
<p>The <code>.</code><i>file &#8230;</i> argument macro may be used whenever an argument is referenced. If called without arguments, the `<i>file &#8230;</i> &#8216; string is output. </p>
<blockquote><p><tt>Usage: .</tt><i></i>[Ao argument Ac &#8230;] </p></blockquote>
<dl>
<dt><code>.</code><i>file &#8230;</i></p>
<dd><i>file &#8230;</i></p>
<dt><code>.</code><i>file1</i></p>
<dd><i>file1</i></p>
<dt><code>.</code><i>file1 .</i></p>
<dd><i>file1</i></p>
<dt><code>.</code><i>file1 file2</i></p>
<dd><i>file1 file2</i></p>
<dt><code>.</code><i>f1 f2 f3 :</i></p>
<dd><i>f1 f2 f3</i></p>
<dt><code>.</code><i>file ) ) ,</i></p>
<dd><i>file ) )</i></dl>
<p> The default width is 12n.</p>
<h3>Configuration Declaration (Section Four Only)</h3>
<p>The `.<code>macro</code> &#8216; is used to demonstrate a <a href="/docs/linux/man/8-config/">config</a>(8) declaration for a device interface in a section four manual. </p>
<blockquote><p><tt>Usage: .</tt><code>Ao </code>argument Ac &#8230; </p></blockquote>
<dl>
<dt><code>.&quot;device le0 at scode?&quot;</code></p>
<dd><code>device le0 at scode?</code></dl>
<p> In the Sx SYNOPSIS section a `.<code>command</code> &#8216; causes a line break before and after its arguments are printed. </p>
<p> The default width is 12n.</p>
<h3>Command Modifiers</h3>
<p>The command modifier is identical to the `.- &#8216; (flag) command with the exception that the `.<code>macro</code> &#8216; does not assert a dash in front of every argument. Traditionally flags are marked by the preceding dash, however, some commands or subsets of commands do not use them. Command modifiers may also be specified in conjunction with interactive commands such as editor commands. See Sx Flags . </p>
<p> The default width is 10n.</p>
<h3>Defined Variables</h3>
<p>A variable (or constant) which is defined in an include file is specified by the macro `. &#8216; </p>
<blockquote><p><tt>Usage: .</tt><code>Ao </code>defined variable Ac &#8230; </p></blockquote>
<dl>
<dt><code>.MAXHOSTNAMELEN</code></p>
<dd><code>MAXHOSTNAMELEN</code></p>
<dt><code>.TIOCGPGRP )</code></p>
<dd><code>TIOCGPGRP</code></dl>
<p> The default width is 12n.</p>
<h3>Errno&#8217;s</h3>
<p>The `.Er errno &#8216; macro specifies the error return value for section 2, 3, and~9 library routines. The second example below shows `.Er used &#8216; with the `.Bq general &#8216; text domain macro, as it would be used in a section two manual page. </p>
<blockquote><p><tt>Usage: .Er </tt>Ao errno type Ac &#8230; </p></blockquote>
<dl>
<dt><code>.Er </code>ENOENT</p>
<dd>Er ENOENT</p>
<dt><code>.Er </code>ENOENT ) ;</p>
<dd>Er ENOENT ) ;</p>
<dt><code>.Bq </code>Er ENOTDIR</p>
<dd>Bq Er ENOTDIR</dl>
<p> The default width is 17n.</p>
<h3>Environment Variables</h3>
<p>The `.<code>macro</code> &#8216; specifies an environment variable. </p>
<blockquote><p><tt>Usage: .</tt><code>Ao </code>argument Ac &#8230; </p></blockquote>
<dl>
<dt><code>.DISPLAY</code></p>
<dd><code>DISPLAY</code></p>
<dt><code>.PATH .</code></p>
<dd><code>PATH</code></p>
<dt><code>.PRINTER ) ) ,</code></p>
<dd><code>PRINTER ) )</code></dl>
<p> The default width is 15n.</p>
<h3>Flags</h3>
<p>The `.- &#8216; macro handles command-line flags. It prepends a dash, `-&#8216; , to the flag. For interactive command flags, which are not prepended with a dash, the `.<code>(command</code> &#8216; modifier) macro is identical, but without the dash. </p>
<blockquote><p><tt>Usage: .-</tt><code>Ao </code>argument Ac &#8230; </p></blockquote>
<dl>
<dt><code>.- </code></p>
<dd>&#8211;</p>
<dt><code>.-cfv</code></p>
<dd>&#8211;<code>cfv</code></p>
<dt><code>.-cfv .</code></p>
<dd>&#8211;<code>cfv</code></p>
<dt><code>.cfv .</code></p>
<dd><code>cfv</code></p>
<dt><code>.-s v t</code></p>
<dd>&#8211;<code>s v t</code></p>
<dt><code>.&#8211; ,</code></p>
<dd>&#8211;<code>&#8211;</code></p>
<dt><code>.-xyz ) ,</code></p>
<dd>&#8211;<code>xyz )</code></p>
<dt><code>.-|</code></p>
<dd>&#8211;<code>|</code></dl>
<p> The `.- &#8216; macro without any arguments results in a dash representing stdin/stdout. Note that giving `.- &#8216; a single dash will result in two dashes. </p>
<p> The default width is 12n.</p>
<h3>Function Declarations</h3>
<p>The `.Fd macro &#8216; is used in the Sx SYNOPSIS section with section two or three functions. It is neither callable nor parsed. </p>
<blockquote><p><tt>Usage: .Fd </tt>Ao argument Ac &#8230; </p></blockquote>
<dl>
<dt><code>.Fd </code>&quot;#include &lt;sys/types.h&gt;&quot;</p>
<dd>Fd #include &lt;sys/types.h&gt;</dl>
<p> In the Sx SYNOPSIS section a `.Fd command &#8216; causes a line break if a function has already been presented and a break has not occurred. This leaves a nice vertical space in between the previous function call and the declaration for the next function. </p>
<p> The `.In macro, &#8216; while in the Sx SYNOPSIS section, represents the <code>#include</code> statement, and is the short form of the above example. It specifies the C~header file as being included in a C~program. It also causes a line break. </p>
<p> While not in the Sx SYNOPSIS section, it represents the header file enclosed in angle brackets. </p>
<blockquote><p><tt>Usage: .In </tt>Ao header file Ac </p>
</blockquote>
<dl>
<dt><code>.In </code>stdio.h</p>
<dd>In stdio.h</p>
<dt><code>.In </code>stdio.h</p>
<dd>In stdio.h</dl>
<h3>Function Types</h3>
<p>This macro is intended for the Sx SYNOPSIS section. It may be used anywhere else in the man page without problems, but its main purpose is to present the function type in kernel normal form for the Sx SYNOPSIS of sections two and three (it causes a line break, allowing the function name to appear on the next line). </p>
<blockquote><p><tt>Usage: .Ft </tt>Ao type Ac &#8230; </p></blockquote>
<dl>
<dt><code>.Ft </code>struct stat</p>
<dd>Ft struct stat</dl>
<h3>Functions (Library Routines)</h3>
<p>The `.Fn macro &#8216; is modeled on <code>ANSI~C</code> conventions. </p>
<blockquote><p><tt>Usage: .Fn </tt>Ao function Ac [Ao parameter Ac &#8230;] </p></blockquote>
<dl>
<dt><code>.Fn </code>getchar</p>
<dd>Fn getchar</p>
<dt><code>.Fn </code>strlen ) ,</p>
<dd>Fn strlen ) ,</p>
<dt><code>.Fn </code>align &quot;char *ptr&quot; ,</p>
<dd>Fn align char *ptr ,</dl>
<p> Note that any call to another macro signals the end of the `.Fn call &#8216; (it will insert a closing parenthesis at that point). </p>
<p> For functions with many parameters (which is rare), the macros `.Fo (function &#8216; open) and `.Fc (function &#8216; close) may be used with `.Fa (function &#8216; argument). </p>
<p> Example: </p>
<blockquote>
<pre>.Ft int
.Fo res_mkquery
.Fa &quot;int op&quot;
.Fa &quot;char *dname&quot;
.Fa &quot;int class&quot;
.Fa &quot;int type&quot;
.Fa &quot;char *data&quot;
.Fa &quot;int datalen&quot;
.Fa &quot;struct rrec *newrr&quot;
.Fa &quot;char *buf&quot;
.Fa &quot;int buflen&quot;
.Fc</pre>
</blockquote>
<p> Produces: </p>
<blockquote><p> Ft int Fo res_mkquery Fa int op Fa char *dname Fa int class Fa int type Fa char *data Fa int datalen Fa struct rrec *newrr Fa char *buf Fa int buflen Fc </p></blockquote>
<p> In the Sx SYNOPSIS section, the function will always begin at the beginning of line. If there is more than one function presented in the Sx SYNOPSIS section and a function type has not been given, a line break will occur, leaving a nice vertical space between the current function name and the one prior. </p>
<p> The default width values of `.Fn and &#8216; `.Fo are &#8216; 12n and 16n, respectively.</p>
<h3>Function Arguments</h3>
<p>The `.Fa macro &#8216; is used to refer to function arguments (parameters) outside of the Sx SYNOPSIS section of the manual or inside the Sx SYNOPSIS section if the enclosure macros `.Fo and &#8216; `.Fc instead &#8216; of `.Fn are &#8216; used. `.Fa may &#8216; also be used to refer to structure members. </p>
<blockquote><p><tt>Usage: .Fa </tt>Ao function argument Ac &#8230; </p></blockquote>
<dl>
<dt><code>.Fa </code>d_namlen ) ) ,</p>
<dd>Fa d_namlen ) ) ,</p>
<dt><code>.Fa </code>iov_len</p>
<dd>Fa iov_len</dl>
<p> The default width is 12n.</p>
<h3>Return Values</h3>
<p>The `.Rv macro &#8216; generates text for use in the Sx RETURN VALUES section. </p>
<blockquote><p><tt>Usage: .Rv </tt>[-std [Ao function Ac &#8230; ] ] </p></blockquote>
<p> For example, `.Rv -std &#8216; atexit produces: </p>
<blockquote><p> # a small hack to suppress a warning message Rv -std atexit </p></blockquote>
<p> The &#8211;<code>std</code> option is valid only for manual page sections~2 and~3. Currently, this macro does nothing if used without the &#8211;<code>std</code> flag.</p>
<h3>Exit Status</h3>
<p>The `.Ex macro &#8216; generates text for use in the Sx DIAGNOSTICS section. </p>
<blockquote><p><tt>Usage: .Ex </tt>[-std [Ao utility Ac &#8230; ] ] </p></blockquote>
<p> For example, `.Ex -std &#8216; cat produces: </p>
<blockquote><p> # a small hack to suppress a warning message Ex -std cat </p></blockquote>
<p> The &#8211;<code>std</code> option is valid only for manual page sections 1, 6 and~8. Currently, this macro does nothing if used without the &#8211;<code>std</code> flag.</p>
<h3>Interactive Commands</h3>
<p>The `.<code>macro</code> &#8216; designates an interactive or internal command. </p>
<blockquote><p><tt>Usage: .</tt><code>Ao </code>argument Ac &#8230; </p></blockquote>
<dl>
<dt><code>.:wq</code></p>
<dd><code>:wq</code></p>
<dt><code>.&quot;do while {&#8230;}&quot;</code></p>
<dd><code>do while {&#8230;}</code></p>
<dt><code>.setenv , unsetenv</code></p>
<dd><code>setenv , unsetenv</code></dl>
<p> The default width is 12n.</p>
<h3>Library Names</h3>
<p>The `.Lb macro &#8216; is used to specify the library where a particular function is compiled in. </p>
<blockquote><p><tt>Usage: .Lb </tt>Ao argument Ac &#8230; </p></blockquote>
<p> Available arguments to `.Lb and &#8216; their results are: </p>
<dl>
<dt><code>libarchive</code></p>
<dd>Lb libarchive</p>
<dt><code>libarm</code></p>
<dd>Lb libarm</p>
<dt><code>libarm32</code></p>
<dd>Lb libarm32</p>
<dt><code>libbluetooth</code></p>
<dd>Lb libbluetooth</p>
<dt><code>libbsm</code></p>
<dd>Lb libbsm</p>
<dt><code>libc</code></p>
<dd>Lb libc</p>
<dt><code>libc_r</code></p>
<dd>Lb libc_r</p>
<dt><code>libcalendar</code></p>
<dd>Lb libcalendar</p>
<dt><code>libcam</code></p>
<dd>Lb libcam</p>
<dt><code>libcdk</code></p>
<dd>Lb libcdk</p>
<dt><code>libcipher</code></p>
<dd>Lb libcipher</p>
<dt><code>libcompat</code></p>
<dd>Lb libcompat</p>
<dt><code>libcrypt</code></p>
<dd>Lb libcrypt</p>
<dt><code>libcurses</code></p>
<dd>Lb libcurses</p>
<dt><code>libdevinfo</code></p>
<dd>Lb libdevinfo</p>
<dt><code>libdevstat</code></p>
<dd>Lb libdevstat</p>
<dt><code>libdisk</code></p>
<dd>Lb libdisk</p>
<dt><code>libdwarf</code></p>
<dd>Lb libdwarf</p>
<dt><code>libedit</code></p>
<dd>Lb libedit</p>
<dt><code>libelf</code></p>
<dd>Lb libelf</p>
<dt><code>libevent</code></p>
<dd>Lb libevent</p>
<dt><code>libfetch</code></p>
<dd>Lb libfetch</p>
<dt><code>libform</code></p>
<dd>Lb libform</p>
<dt><code>libgeom</code></p>
<dd>Lb libgeom</p>
<dt><code>libgpib</code></p>
<dd>Lb libgpib</p>
<dt><code>libi386</code></p>
<dd>Lb libi386</p>
<dt><code>libintl</code></p>
<dd>Lb libintl</p>
<dt><code>libipsec</code></p>
<dd>Lb libipsec</p>
<dt><code>libipx</code></p>
<dd>Lb libipx</p>
<dt><code>libiscsi</code></p>
<dd>Lb libiscsi</p>
<dt><code>libjail</code></p>
<dd>Lb libjail</p>
<dt><code>libkiconv</code></p>
<dd>Lb libkiconv</p>
<dt><code>libkse</code></p>
<dd>Lb libkse</p>
<dt><code>libkvm</code></p>
<dd>Lb libkvm</p>
<dt><code>libm</code></p>
<dd>Lb libm</p>
<dt><code>libm68k</code></p>
<dd>Lb libm68k</p>
<dt><code>libmagic</code></p>
<dd>Lb libmagic</p>
<dt><code>libmd</code></p>
<dd>Lb libmd</p>
<dt><code>libmemstat</code></p>
<dd>Lb libmemstat</p>
<dt><code>libmenu</code></p>
<dd>Lb libmenu</p>
<dt><code>libnetgraph</code></p>
<dd>Lb libnetgraph</p>
<dt><code>libnetpgp</code></p>
<dd>Lb libnetpgp</p>
<dt><code>libossaudio</code></p>
<dd>Lb libossaudio</p>
<dt><code>libpam</code></p>
<dd>Lb libpam</p>
<dt><code>libpcap</code></p>
<dd>Lb libpcap</p>
<dt><code>libpci</code></p>
<dd>Lb libpci</p>
<dt><code>libpmc</code></p>
<dd>Lb libpmc</p>
<dt><code>libposix</code></p>
<dd>Lb libposix</p>
<dt><code>libprop</code></p>
<dd>Lb libprop</p>
<dt><code>libpthread</code></p>
<dd>Lb libpthread</p>
<dt><code>libpuffs</code></p>
<dd>Lb libpuffs</p>
<dt><code>librefuse</code></p>
<dd>Lb librefuse</p>
<dt><code>libresolv</code></p>
<dd>Lb libresolv</p>
<dt><code>librpcsec_gss</code></p>
<dd>Lb librpcsec_gss</p>
<dt><code>librpcsvc</code></p>
<dd>Lb librpcsvc</p>
<dt><code>librt</code></p>
<dd>Lb librt</p>
<dt><code>libsdp</code></p>
<dd>Lb libsdp</p>
<dt><code>libssp</code></p>
<dd>Lb libssp</p>
<dt><code>libSystem</code></p>
<dd>Lb libSystem</p>
<dt><code>libtermcap</code></p>
<dd>Lb libtermcap</p>
<dt><code>libterminfo</code></p>
<dd>Lb libterminfo</p>
<dt><code>libthr</code></p>
<dd>Lb libthr</p>
<dt><code>libufs</code></p>
<dd>Lb libufs</p>
<dt><code>libugidfw</code></p>
<dd>Lb libugidfw</p>
<dt><code>libulog</code></p>
<dd>Lb libulog</p>
<dt><code>libusbhid</code></p>
<dd>Lb libusbhid</p>
<dt><code>libutil</code></p>
<dd>Lb libutil</p>
<dt><code>libvgl</code></p>
<dd>Lb libvgl</p>
<dt><code>libx86_64</code></p>
<dd>Lb libx86_64</p>
<dt><code>libz</code></p>
<dd>Lb libz</dl>
<p> Local, OS-specific additions might be found in the file mdoc.local look for strings named `str-Lb-XXX&#8217; `XXX&#8217; then denotes the keyword to be used with the `.Lb macro. &#8216; </p>
<p> In the <i>LIBRARY</i> section an `.Lb command &#8216; causes a line break before and after its arguments are printed.</p>
<h3>Literals</h3>
<p>The `.<code>literal</code> &#8216; macro may be used for special characters, variable constants, etc. &#8211; anything which should be displayed as it would be typed. </p>
<blockquote><p><tt>Usage: .</tt><code>Ao </code>argument Ac &#8230; </p></blockquote>
<dl>
<dt><code>.n</code></p>
<dd><code>
</code></p>
<dt><code>.M1 M2 M3 ;</code></p>
<dd><code>M1 M2 M3</code></p>
<dt><code>.cntrl-D ) ,</code></p>
<dd><code>cntrl-D )</code></p>
<dt><code>.1024 &#8230;</code></p>
<dd><code>1024 &#8230;</code></dl>
<p> The default width is 16n.</p>
<h3>Names</h3>
<p>The `.<code>groff Fl m Ns Cm doc Ar</code> &#8216; macro is used for the document title or subject name. It has the peculiarity of remembering the first argument it was called with, which should always be the subject name of the page. When called without arguments, `.<code>groff Fl m Ns Cm doc Ar</code> &#8216; regurgitates this initial name for the sole purpose of making less work for the author. `.<code>groff Fl m Ns Cm doc Ar</code> &#8216; causes a line break within the Sx SYNOPSIS section. </p>
<p> Note: A section two or three document function name is addressed with the `.<code>groff Fl m Ns Cm doc Ar</code> &#8216; in the <i>NAME</i> section, and with `.Fn in &#8216; the Sx SYNOPSIS and remaining sections. For interactive commands, such as the `while&#8217; command keyword in <a href="/docs/linux/man/1-csh/">csh</a>(1), the `.<code>macro</code> &#8216; should be used. While `.<code>is</code> &#8216; nearly identical to `.<code>groff Fl m Ns Cm doc Ar</code> &#8216; it can not recall the first argument it was invoked with. </p>
<blockquote><p><tt>Usage: .</tt>[Ao argument Ac &#8230;] </p></blockquote>
<dl>
<dt><code>.groff_mdoc</code></p>
<dd><code>groff_mdoc</code></p>
<dt><code>.\-mdoc</code></p>
<dd><code>-mdoc</code></p>
<dt><code>.foo ) ) ,</code></p>
<dd><code>foo ) )</code></p>
<dt><code>.:</code></p>
<dd><code>:</code></dl>
<p> The default width is 10n.</p>
<h3>Options</h3>
<p>The `.[macro] &#8216; places option brackets around any remaining arguments on the command line, and places any trailing punctuation outside the brackets. The macros `.[and &#8216; `.] &#8216; (which produce an opening and a closing option bracket respectively) may be used across one or more lines or to specify the exact position of the closing parenthesis. </p>
<blockquote><p><tt>Usage: .</tt>[[Ao option Ac &#8230;] ] </p></blockquote>
<dl>
<dt><code>.</code>[[</p>
<dt><code>.</code>[-<code>k</code> ]</p>
<dd>] ]</p>
<dd>[-<code>k</code> ]</p>
<dt><code>.</code>[-<code>k ) .</code> ]</p>
<dd>[-<code>k</code> ]</p>
<dt><code>.</code>[-<code>k </code><i>kookfile</i> ]</p>
<dd>[-<code>k </code><i>kookfile</i> ]</p>
<dt><code>.</code>[-<code>k </code><i>kookfile ,</i> ]</p>
<dd>[-<code>k </code><i>kookfile</i> ]</p>
<dt><code>.</code>[<i>objfil </i>[<i>corfil</i> ] ]</p>
<dd>[<i>objfil </i>[<i>corfil</i> ] ]</p>
<dt><code>.</code>[-<code>c </code><i>objfil </i>[<i>corfil ,</i> ] ]</p>
<dd>[-<code>c </code><i>objfil </i>[<i>corfil</i> ] ]</p>
<dt><code>.</code>[word1 word2]</p>
<dd>[word1 word2]</p>
<dt><code>..</code>[[Ao option Ac &#8230;] ]</p>
<dd><code>.</code>[[Ao option Ac &#8230;] ]</dl>
<p> Here a typical example of the `.[and &#8216; `.] &#8216; macros: </p>
<blockquote>
<pre>.Oo
.Op Fl k Ar kilobytes
.Op Fl i Ar interval
.Op Fl c Ar count
.Oc</pre>
</blockquote>
<p> Produces: </p>
<blockquote><p> [[-<code>k </code><i>kilobytes</i> ] [-<code>i </code><i>interval</i> ] [-<code>c </code><i>count</i> ] ] </p></blockquote>
<p> The default width values of `.[and] &#8216; `.[are &#8216; 14n and 10n, respectively.</p>
<h3>Pathnames</h3>
<p>The `.macro &#8216; formats path or file names. If called without arguments, the `string is output, which represents the current user&#8217;s home directory. &#8216; </p>
<blockquote><p><tt>Usage: .</tt>[Ao pathname Ac &#8230;] </p></blockquote>
<dl>
<dt><code>.</p>
<dt>./usr/share </code></p>
<dd>
<dd>/usr/share</p>
<dt><code>./tmp/fooXXXXX ) . </code></p>
<dd>/tmp/fooXXXXX )</dl>
<p> The default width is 32n.</p>
<h3>Standards</h3>
<p>The `.St macro &#8216; replaces standard abbreviations with their formal names. </p>
<blockquote><p><tt>Usage: .St </tt>Ao abbreviation Ac &#8230; </p></blockquote>
<p> Available pairs for &#8220;Abbreviation/Formal Name&#8221; are: </p>
<p> <code>ANSI/ISO C</code> </p>
<dl>
<dt><code>-ansiC</code></p>
<dd>St -ansiC</p>
<dt><code>-ansiC-89</code></p>
<dd>St -ansiC-89</p>
<dt><code>-isoC</code></p>
<dd>St -isoC</p>
<dt><code>-isoC-90</code></p>
<dd>St -isoC-90</p>
<dt><code>-isoC-99</code></p>
<dd>St -isoC-99</p>
<dt><code>-isoC-2011</code></p>
<dd>St -isoC-2011</dl>
<p> <code>POSIX</code> Part 1: System API </p>
<dl>
<dt><code>-iso9945-1-90</code></p>
<dd>St -iso9945-1-90</p>
<dt><code>-iso9945-1-96</code></p>
<dd>St -iso9945-1-96</p>
<dt><code>-p1003.1</code></p>
<dd>St -p1003.1</p>
<dt><code>-p1003.1-88</code></p>
<dd>St -p1003.1-88</p>
<dt><code>-p1003.1-90</code></p>
<dd>St -p1003.1-90</p>
<dt><code>-p1003.1-96</code></p>
<dd>St -p1003.1-96</p>
<dt><code>-p1003.1b-93</code></p>
<dd>St -p1003.1b-93</p>
<dt><code>-p1003.1c-95</code></p>
<dd>St -p1003.1c-95</p>
<dt><code>-p1003.1g-2000</code></p>
<dd>St -p1003.1g-2000</p>
<dt><code>-p1003.1i-95</code></p>
<dd>St -p1003.1i-95</p>
<dt><code>-p1003.1-2001</code></p>
<dd>St -p1003.1-2001</p>
<dt><code>-p1003.1-2004</code></p>
<dd>St -p1003.1-2004</p>
<dt><code>-p1003.1-2008</code></p>
<dd>St -p1003.1-2008</dl>
<p> <code>POSIX</code> Part 2: Shell and Utilities </p>
<dl>
<dt><code>-iso9945-2-93</code></p>
<dd>St -iso9945-2-93</p>
<dt><code>-p1003.2</code></p>
<dd>St -p1003.2</p>
<dt><code>-p1003.2-92</code></p>
<dd>St -p1003.2-92</p>
<dt><code>-p1003.2a-92</code></p>
<dd>St -p1003.2a-92</dl>
<p> X/Open </p>
<dl>
<dt><code>-susv2</code></p>
<dd>St -susv2</p>
<dt><code>-susv3</code></p>
<dd>St -susv3</p>
<dt><code>-svid4</code></p>
<dd>St -svid4</p>
<dt><code>-xbd5</code></p>
<dd>St -xbd5</p>
<dt><code>-xcu5</code></p>
<dd>St -xcu5</p>
<dt><code>-xcurses4.2</code></p>
<dd>St -xcurses4.2</p>
<dt><code>-xns5</code></p>
<dd>St -xns5</p>
<dt><code>-xns5.2</code></p>
<dd>St -xns5.2</p>
<dt><code>-xpg3</code></p>
<dd>St -xpg3</p>
<dt><code>-xpg4</code></p>
<dd>St -xpg4</p>
<dt><code>-xpg4.2</code></p>
<dd>St -xpg4.2</p>
<dt><code>-xsh5</code></p>
<dd>St -xsh5</dl>
<p> Miscellaneous </p>
<dl>
<dt><code>-ieee754</code></p>
<dd>St -ieee754</p>
<dt><code>-iso8601</code></p>
<dd>St -iso8601</p>
<dt><code>-iso8802-3</code></p>
<dd>St -iso8802-3</dl>
<h3>Variable Types</h3>
<p>The `.Vt macro &#8216; may be used whenever a type is referenced. In the Sx SYNOPSIS section, it causes a line break (useful for old style variable declarations). </p>
<blockquote><p><tt>Usage: .Vt </tt>Ao type Ac &#8230; </p></blockquote>
<dl>
<dt><code>.Vt </code>extern char *optarg ;</p>
<dd>Vt extern char *optarg ;</p>
<dt><code>.Vt </code>FILE *</p>
<dd>Vt FILE *</dl>
<h3>Variables</h3>
<p>Generic variable reference. </p>
<blockquote><p><tt>Usage: .</tt><i>Ao </i>variable Ac &#8230; </p></blockquote>
<dl>
<dt><code>.</code><i>count</i></p>
<dd><i>count</i></p>
<dt><code>.</code><i>settimer ,</i></p>
<dd><i>settimer</i></p>
<dt><code>.</code><i>&quot;int *prt&quot; ) :</i></p>
<dd><i>int *prt )</i></p>
<dt><code>.</code><i>&quot;char s&quot; ] ) ) ,</i></p>
<dd><i>char s ] ) )</i></dl>
<p> The default width is 12n.</p>
<h3>Manual Page Cross References</h3>
<p>The `.macro &#8216; expects the first argument to be a manual page name. The optional second argument, if a string (defining the manual section), is put into parentheses. </p>
<blockquote><p><tt>Usage: .AomanpagenameAcOoAosectionAcOc... </tt></p></blockquote>
<dl>
<dt><code>.mdoc </code></p>
<dd>mdoc</p>
<dt><code>.mdoc, </code></p>
<dd>mdoc,</p>
<dt><code><a href="/docs/linux/man/7--mdoc/">.mdoc</a>(7) </code></p>
<dd><a href="/docs/linux/man/7-mdoc/">mdoc</a>(7)</p>
<dt><code><a href="//www.systutorials.com/docs/linux/man/1x-.xinit/">.xinit</a>(1x); </code></p>
<dd><a href="//www.systutorials.com/docs/linux/man/1x-xinit/">xinit</a>(1x);</dl>
<p> The default width is 10n.</p>
<h2>General Text Domain</h2>
<h3>AT&amp;T Macro</h3>
<blockquote><p><tt>Usage: .AT&amp;T System </tt>[Ao version Ac &#8230;] </p></blockquote>
<dl>
<dt><code>.AT&amp;T System </code></p>
<dd>AT&amp;T System</p>
<dt><code>.AT&amp;T System v6 .</code></p>
<dd>AT&amp;T System v6 .</dl>
<p> The following values for Ao version Ac are possible: </p>
<blockquote><p><tt>32v, v1, v2, v3, v4, v5, v6, v7, III, V, V.1, V.2, V.3, V.4</tt></p></blockquote>
<h3>BSD Macro</h3>
<blockquote><p><tt>&quot;Usage: .Bx&quot; Bro -alpha | -beta | -devel Brc ...</tt></p></blockquote>
<blockquote><p><tt>&quot; .Bx&quot; </tt>[Ao version Ac [Ao release Ac &#8230;] ] </p></blockquote>
<dl>
<dt><code>.BSD BSD</p>
<dt>.BSD 4.3 . </code></p>
<dd>
<dd>BSD 4.3</p>
<dt><code>.BSD -devel </code></p>
<dd>BSD -devel</dl>
<p> Ao version Ac will be prepended to the string `BSD &#8216; The following values for Ao release Ac are possible: </p>
<blockquote><p><tt>Reno, reno, Tahoe, tahoe, Lite, lite, Lite2, lite2</tt></p></blockquote>
<h3>NetBSD Macro</h3>
<blockquote><p><tt>Usage: .Nx </tt>[Ao version Ac &#8230;] </p></blockquote>
<dl>
<dt><code>.Nx </code>Nx</p>
<dt><code>.Nx </code>1.4 .</p>
<dd>
<dd>Nx 1.4 .</dl>
<p> For possible values of Ao version Ac see the description of the `.command &#8216; above in section Sx TITLE MACROS .</p>
<h3>FreeBSD Macro</h3>
<blockquote><p><tt>Usage: .Fx </tt>[Ao version Ac &#8230;] </p></blockquote>
<dl>
<dt><code>.Fx </code>Fx</p>
<dt><code>.Fx </code>2.2 .</p>
<dd>
<dd>Fx 2.2 .</dl>
<p> For possible values of Ao version Ac see the description of the `.command &#8216; above in section Sx TITLE MACROS .</p>
<h3>DragonFly Macro</h3>
<blockquote><p><tt>Usage: .Dx </tt>[Ao version Ac &#8230;] </p></blockquote>
<dl>
<dt><code>.Dx </code>Dx</p>
<dt><code>.Dx </code>1.4 .</p>
<dd>
<dd>Dx 1.4 .</dl>
<p> For possible values of Ao version Ac see the description of the `.command &#8216; above in section Sx TITLE MACROS .</p>
<h3>OpenBSD Macro</h3>
<blockquote><p><tt>Usage: .Ox </tt>[Ao version Ac &#8230;] </p></blockquote>
<dl>
<dt><code>.Ox </code>1.0</p>
<dd>Ox 1.0</dl>
<h3>BSD/OS Macro</h3>
<blockquote><p><tt>Usage: .Bsx </tt>[Ao version Ac &#8230;] </p></blockquote>
<dl>
<dt><code>.Bsx 1.0</code></p>
<dd>Bs x 1.0</dl>
<h3>UNIX Macro</h3>
<blockquote><p><tt>Usage: .UNIX </tt></p></blockquote>
<dl>
<dt><code>.UNIX </code></p>
<dd>UNIX</dl>
<h3>Emphasis Macro</h3>
<p>Text may be stressed or emphasized with the `.<i>macro.</i> &#8216; The usual font for emphasis is italic. </p>
<blockquote><p><tt>Usage: .</tt><i>Ao </i>argument Ac &#8230; </p></blockquote>
<dl>
<dt><code>.</code><i>does not</i></p>
<dd><i>does not</i></p>
<dt><code>.</code><i>exceed 1024 .</i></p>
<dd><i>exceed 1024</i></p>
<dt><code>.</code><i>vide infra ) ) ,</i></p>
<dd><i>vide infra ) )</i></dl>
<p> The default width is 10n.</p>
<h3>Font Mode</h3>
<p>The `.Bf font &#8216; mode must be ended with the `.Ef macro &#8216; (the latter takes no arguments). Font modes may be nested within other font modes. </p>
<p> `.Bf has &#8216; the following syntax: </p>
<blockquote><p><tt>.Bf </tt>Ao font mode Ac </p>
</blockquote>
<p> Ao font mode Ac must be one of the following three types: </p>
<dl>
<dt><i>| &#8211;</i><code>emphasis</code></p>
<dd>Same as if the `.<i>macro</i> &#8216; was used for the entire block of text.</p>
<dt><code>| -literal</code></p>
<dd>Same as if the `.<code>macro</code> &#8216; was used for the entire block of text.</p>
<dt><code>| -symbolic</code></p>
<dd>Same as if the `.<code>macro</code> &#8216; was used for the entire block of text.</dl>
<p> Both macros are neither callable nor parsed.</p>
<h3>Enclosure and Quoting Macros</h3>
<p>The concept of enclosure is similar to quoting. The object being to enclose one or more strings between a pair of characters like quotes or parentheses. The terms quoting and enclosure are used interchangeably throughout this document. Most of the one-line enclosure macros end in small letter `q&#8217; to give a hint of quoting, but there are a few irregularities. For each enclosure macro there is also a pair of open and close macros which end in small letters `o&#8217; and `c&#8217; respectively. </p>
<p> # XXX </p>
<table>
<tr VALIGN=top>
<td><code>Quote</code></td>
<td><code>Open</code></td>
<td><code>Close</code></td>
<td><code>Function</code></td>
<td><code>Result</code>
</td>
</tr>
<tr VALIGN=top>
<td>.Aq</td>
<td>.Ao</td>
<td>.Ac</td>
<td>Angle Bracket Enclosure</td>
<td>&lt;string&gt;
</td>
</tr>
<tr VALIGN=top>
<td>.Bq</td>
<td>.Bo</td>
<td>.Bc</td>
<td>Bracket Enclosure</td>
<td>[string]
</td>
</tr>
<tr VALIGN=top>
<td>.Brq</td>
<td>.Bro</td>
<td>.Brc</td>
<td>Brace Enclosure</td>
<td>{string}
</td>
</tr>
<tr VALIGN=top>
<td>.Dq</td>
<td>.Do</td>
<td>.Dc</td>
<td>Double Quote</td>
<td>&quot;string&quot;
</td>
</tr>
<tr VALIGN=top>
<td>.Eq</td>
<td>.Eo</td>
<td>.Ec</td>
<td>Enclose String (in XX)</td>
<td>XXstring
</td>
</tr>
<tr VALIGN=top>
<td>.Pq</td>
<td>.Po</td>
<td>.Pc</td>
<td>Parenthesis Enclosure</td>
<td>(string)
</td>
</tr>
<tr VALIGN=top>
<td>.Ql</td>
<td></td>
<td></td>
<td>Quoted Literal</td>
<td>&ldquo;string&rdquo; or string
</td>
</tr>
<tr VALIGN=top>
<td>.Qq</td>
<td>.Qo</td>
<td>.Qc</td>
<td>Straight Double Quote</td>
<td>&quot;string&quot;
</td>
</tr>
<tr VALIGN=top>
<td>.Sq</td>
<td>.So</td>
<td>.Sc</td>
<td>Single Quote</td>
<td>&#8216;string&#8217;
</td>
</tr>
</table>
<p> All macros ending with `q&#8217; and `o&#8217; have a default width value of 12n.</p>
<dl>
<dt><code>.Eo </code>, .Ec These macros expect the first argument to be the opening and closing strings</p>
<dd>respectively.</p>
<dt><code>.Es </code>, .En Due to the nine-argument limit in the original troff program two other</p>
<dd>macros have been implemented which are now rather obsolete: `.Es takes &#8216; the first and second parameter as the left and right enclosure string, which are then used to enclose the arguments of `.En &#8216; The default width value is 12n for both macros.</p>
<dt><code>.Eq </code>The first and second arguments of this macro are the opening and</p>
<dd>closing strings respectively, followed by the arguments to be enclosed.</p>
<dt><code>.`The&#8217; </code></p>
<dd>quoted literal macro behaves differently in troff and nroff mode. If formatted with nroff, a quoted literal is always quoted. If formatted with troff, an item is only quoted if the width of the item is less than three constant width characters. This is to make short strings more visible where the font change to literal (constant width) is less noticeable. </p>
<p> The default width is 16n.</p>
<dt><code>.The prefix macro suppresses the whitespace between its first and second </code></p>
<dd>argument:</p>
<dl>
<dt><code>.( Fa </code>name2</p>
<dd>( Fa name2</dl>
<p> The default width is 12n. </p>
<p> The `.<code>macro</code> &#8216; (see below) performs the analogous suffix function.</p>
<dt><code>.Ap </code>The</p>
<dd>`.Ap macro &#8216; inserts an apostrophe and exits any special text modes, continuing in `.<code>mode.</code> &#8216;</dl>
<p> Examples of quoting: </p>
<dl>
<dt><code>.Aq </code>Aq</p>
<dt><code>.Aq </code>ctype.h ) ,</p>
<dd>
<dd>Aq Pa ctype.h ) ,</p>
<dt><code>.Bq </code>Bq</p>
<dt><code>.Bq </code><i>Greek , French .</i></p>
<dd>
<dd>Bq Em Greek , French .</p>
<dt><code>.&#8220;&#8220;</p>
<dt>.&#8220;string abc .&#8221; </code></p>
<dd>&#8221; &#8221;</p>
<dd>&#8220;string abc&#8221;</p>
<dt><code>.&#8220;&#8217;^[A-Z]&#8221;&#8217; </code></p>
<dd>&#8220;&#8217;^[A-Z]&#8221;&#8217;</p>
<dt><code>.`man&#8217; </code></p>
<dd>mdoc `man&#8217; mdoc</p>
<dt><code>.Qq </code>Qq</p>
<dt><code>.Qq </code>string ) ,</p>
<dd>
<dd>Qq string ) ,</p>
<dt><code>.Qq </code>string <code>),</code></p>
<dd>Qq string Ns ),</p>
<dt><code>.&#8220;</p>
<dt>.`string&#8217; </code></p>
<dd>&#8216; &#8216;</p>
<dd>`string&#8217;</p>
<dt><code>.</code><i>or Ap </i>ing</p>
<dd><i>or Ap </i>ing</dl>
<p> For a good example of nested enclosure macros, see the `.[option] &#8216; macro. It was created from the same underlying enclosure macros as those presented in the list above. The `. &#8216; and `. &#8216; extended argument list macros are discussed below.</p>
<h3>No-[or Normal Text Macro]</h3>
<p>The `.<code>macro</code> &#8216; can be used in a macro command line for parameters which should <i>not</i> be formatted. Be careful to add `\&amp;&#8217; to the word `<code>if</code> &#8216; you really want that English word (and not the macro) as a parameter. </p>
<blockquote><p><tt>Usage: .</tt><code>Ao </code>argument Ac &#8230; </p></blockquote>
<dl>
<dt><code>.test Ta </code>with Ta tabs</p>
<dd><code>test Ta </code>with Ta tabs</dl>
<p> The default width is 12n.</p>
<h3>No-Space Macro</h3>
<p>The `.<code>macro</code> &#8216; suppresses insertion of a space between the current position and its first parameter. For example, it is useful for old style argument lists where there is no space between the flag and argument: </p>
<blockquote><p><tt>&quot;Usage:&quot; ... Ao </tt>argument Ac [Ao argument Ac &#8230;] </p></blockquote>
<blockquote><p><tt>&quot; &quot; .</tt><code>Ao </code>argument Ac &#8230; </p></blockquote>
<dl>
<dt><code>.</code>[-<code>I </code><i>directory</i> ]</p>
<dd>[-<code>I </code><i>directory</i> ]</dl>
<p> Note: The `.<code>macro</code> &#8216; always invokes the `.<code>macro</code> &#8216; after eliminating the space unless another macro name follows it. If used as a command (i.e., the second form above in the `Usage&#8217; line), `.<code>is</code> &#8216; identical to `. &#8216;</p>
<h3>Section Cross References</h3>
<p>The `.Sx macro &#8216; designates a reference to a section header within the same document. </p>
<blockquote><p><tt>Usage: .Sx </tt>Ao section reference Ac &#8230; </p></blockquote>
<dl>
<dt><code>.Sx </code>FILES</p>
<dd>Sx FILES</dl>
<p> The default width is 16n.</p>
<h3>Symbolics</h3>
<p>The symbolic emphasis macro is generally a boldface macro in either the symbolic sense or the traditional English usage. </p>
<blockquote><p><tt>Usage: .</tt><code>Ao </code>symbol Ac &#8230; </p></blockquote>
<dl>
<dt><code>.Important Notice</code></p>
<dd><code>Important Notice</code></dl>
<p> The default width is 6n.</p>
<h3>Mathematical Symbols</h3>
<p>Use this macro for mathematical symbols and similar things. </p>
<blockquote><p><tt>Usage: .</tt><code>Ao </code>math symbol Ac &#8230; </p></blockquote>
<dl>
<dt><code>.sigma</code></p>
<dd><code>sigma</code></dl>
<p> The default width is 6n.</p>
<h3>References and Citations</h3>
<p>The following macros make a modest attempt to handle references. At best, the macros make it convenient to manually drop in a subset of <a href="/docs/linux/man/1-refer/">refer</a>(1) style references. </p>
<dl>
<dt><code>.</p>
<dl>
<dd></code></p>
<dd>Reference start (does not take arguments). Causes a line break in the Sx SEE ALSO section and begins collection of reference information until the reference end macro is read. Li .Re Reference end (does not take arguments). The reference is printed. Li .%A Reference author name; one name per invocation. Li .%B Book title. Li .%C City/place. Li .%D Date. Li .%I Issuer/publisher name. Li .%J Journal name. Li .%N Issue number. Li .%O Optional information. Li .%P Page number. Li .%Q Corporate or foreign author. Li .%R Report name. Li .%T Title of article. Li .%U Optional hypertext reference. Li .%V Volume. </p>
<p> Macros beginning with `%&#8217; are not callable but accept multiple arguments in the usual way. Only the `.<code>macro</code> &#8216; is handled properly as a parameter; other macros will cause strange output. `.%B&#8217; and `.%T&#8217; can be used outside of the `.Rs/.</dl>
</dl>
<p> &#8216; environment. </p>
<p> Example: </p>
<blockquote>
<pre>.Rs
.%A &quot;Matthew Bar&quot;
.%A &quot;John Foo&quot;
.%T &quot;Implementation Notes on <a href="//www.systutorials.com/docs/linux/man/1-foobar/">foobar</a>(1)&quot;
.%R &quot;Technical Report ABC-DE-12-345&quot;
.%Q &quot;Drofnats College&quot;
.%C &quot;Nowhere&quot;
.%D &quot;April 1991&quot;
.Re</pre>
</blockquote>
<p> produces </p>
<blockquote>
<dl>
<dd>&quot;Matthew Bar&quot; &quot;John Foo&quot; <i>&quot;Implementation Notes on <a href="/docs/linux/man/1-foobar/">foobar</a>(1)&quot;</i> <i>&quot;Technical Report ABC-DE-12-345&quot;</i> &quot;Drofnats College&quot; &quot;April 1991&quot;</dl>
</blockquote>
<h3>Trade Names (or Acronyms and Type Names)</h3>
<p>The trade name macro prints its arguments in a smaller font. Its intended use is to imitate a small caps fonts for uppercase acronyms. </p>
<blockquote><p><tt>Usage: .</tt><code>Ao </code>symbol Ac &#8230; </p></blockquote>
<dl>
<dt><code>.DEC</code></p>
<dd><code>DEC</code></p>
<dt><code>.ASCII</code></p>
<dd><code>ASCII</code></dl>
<p> The default width is 10n.</p>
<h3>Extended Arguments</h3>
<p>The <code>. </code> and <code>. </code> macros allow one to extend an argument list on a macro boundary for the `. &#8216; macro (see below). Note that <code>. </code> and <code>. </code> are implemented similarly to all other macros opening and closing an enclosure (without inserting characters, of course). This means that the following is true for those macros also. </p>
<p> Here is an example of `. &#8216; using the space mode macro to turn spacing off: </p>
<blockquote>
<pre>.Sm off
.It Xo Sy I Ar operation
.No n Ar count No n
.Xc
.Sm on</pre>
</blockquote>
<p> produces </p>
<blockquote>
<dl>
<dt><code> I </code><i>operation</i> <code>
 </code><i>count </i><code>
</code></p>
<dd></dl>
</blockquote>
<dd>Another one: </p>
<blockquote>
<pre>.Sm off
.It Cm S No / Ar old_pattern Xo
.No / Ar new_pattern
.No / Op Cm g
.Xc
.Sm on</pre>
</blockquote>
<p> produces </p>
<blockquote>
<dl>
<dt><code>S / </code><i>old_pattern </i> <code>/ </code><i>new_pattern</i> <code>/ </code>[<code>g</code> ]</p>
<dd></dl>
</blockquote>
<dd>Another example of `. &#8216; and enclosure macros: Test the value of a variable. </p>
<blockquote>
<pre>.It Xo
.Ic .ifndef
.Oo \&amp;! Oc Ns Ar variable Oo
.Ar operator variable ...
.Oc Xc</pre>
</blockquote>
<p> produces </p>
<blockquote>
<dl>
<dt> <code>.ifndef</code> [! <i>variable </i>[<i>operator variable &#8230;</i> ]</p>
<dd>]</dl>
</blockquote>
<h2>Page Structure Domain</h2>
<h3>Section Headers</h3>
<dd>The following `.</p>
<h2>section</h2>
<p>&#8216; header macros are required in every man page. The remaining section headers are recommended at the discretion of the author writing the manual page. The `.</p>
<h2>macro</h2>
<p>&#8216; is parsed but not generally callable. It can be used as an argument in a call to `.</p>
<h2>only;</h2>
<p>&#8216; it then reactivates the default font for `.</p>
<h2></h2>
<p>&#8216; </p>
<p> The default width is 8n.</p>
<dl>
<dt><code>.</dl>
</dl>
<p> </code></p>
<h2>Name</h2>
<dd>The `.</p>
<h2>Name</h2>
<p>&#8216; macro is mandatory. If not specified, headers, footers and page layout defaults will not be set and things will be rather unpleasant. The <i>NAME</i> section consists of at least three items. The first is the `.<code>groff Fl m Ns Cm doc Ar</code> &#8216; name macro naming the subject of the man page. The second is the name description macro, `. &#8211; , &#8216; which separates the subject name from the third item, which is the description. The description should be the most terse and lucid possible, as the space available is small. </p>
<p> `. &#8211; first &#8216; prints `-&#8216; , then all its arguments. Li &quot;.Sh LIBRARY&quot; This section is for section two and three function calls. It should consist of a single `.Lb macro &#8216; call; see Sx Library Names . Li &quot;.Sh SYNOPSIS&quot; The Sx SYNOPSIS section describes the typical usage of the subject of a man page. The macros required are either `.<code>groff Fl m Ns Cm doc Ar</code> &#8216; `.<code>,</code> &#8216; or `.Fn (and &#8216; possibly `.Fo , &#8216; `.Fc , &#8216; `.Fd , &#8216; and `.Ft ) &#8216; The function name macro `.Fn is &#8216; required for manual page sections~2 and~3; the command and general name macro `.<code>groff Fl m Ns Cm doc Ar</code> &#8216; is required for sections 1, 5, 6, 7, and~8. Section~4 manuals require a `.<code>groff Fl m Ns Cm doc Ar</code> &#8216; `.Fd or &#8216; a `.<code>configuration</code> &#8216; device usage macro. Several other macros may be necessary to produce the synopsis line as shown below: </p>
<blockquote><p> <code>cat</code> [-<code>benstuv</code> ] [- ] <i>file &#8230;</i> </p></blockquote>
<p> The following macros were used: </p>
<blockquote><p><tt>&quot;.</tt><code>cat</code> </p></blockquote>
<blockquote><p><tt>&quot;.</tt>[-<code>benstuv</code> ] </p></blockquote>
<blockquote><p><tt>&quot;.</tt>[Fl] </p></blockquote>
<blockquote><p><tt>.</tt><i>file &#8230;</i> </p></blockquote>
<p> Li &quot;.Sh DESCRIPTION&quot; In most cases the first text in the Sx DESCRIPTION section is a brief paragraph on the command, function or file, followed by a lexical list of options and respective explanations. To create such a list, the `.</p>
<dl>
<p> &#8216; (begin list), `.</p>
<dt><code>(list</code></p>
<dd>&#8216; item) and `.</dl>
<p> &#8216; (end list) macros are used (see Sx Lists and Columns below). Li &quot;.Sh IMPLEMENTATION NOTES&quot; Implementation specific information should be placed here. Li &quot;.Sh RETURN VALUES&quot; Sections 2, 3 and~9 function return values should go here. The `.Rv macro &#8216; may be used to generate text for use in the Sx RETURN VALUES section for most section 2 and 3 library functions; see Sx Return Values . </p>
<p> The following `.</p>
<h2>section</h2>
<p>&#8216; headers are part of the preferred manual page layout and must be used appropriately to maintain consistency. They are listed in the order in which they would be used.</p>
<dl>
<dt><code>.</dl>
</dl>
<p> </code></p>
<h2>Environment</h2>
<dd>The <i>ENVIRONMENT</i> section should reveal any related environment variables and clues to their behavior and/or usage. Li &quot;.Sh FILES&quot; Files which are used or created by the man page subject should be listed via the `.macro &#8216; in the Sx FILES section. Li &quot;.Sh EXAMPLES&quot; There are several ways to create examples. See the Sx Examples and Displays section below for details. Li &quot;.Sh DIAGNOSTICS&quot; Diagnostic messages from a command should be placed in this section. The `.Ex macro &#8216; may be used to generate text for use in the Sx DIAGNOSTICS section for most section 1, 6 and~8 commands; see Sx Exit Status . Li &quot;.Sh COMPATIBILITY&quot; Known compatibility issues (e.g. deprecated options or parameters) should be listed here. Li &quot;.Sh ERRORS&quot; Specific error handling, especially from library functions (man page sections 2, 3, and~9) should go here. The `.Er macro &#8216; is used to specify an error (errno). Li &quot;.Sh SEE ALSO&quot; References to other material on the man page topic and cross references to other relevant man pages should be placed in the Sx SEE ALSO section. Cross references are specified using the `.macro. &#8216; Currently <a href="/docs/linux/man/1-refer/">refer</a>(1) style references are not accommodated. </p>
<p> It is recommended that the cross references are sorted on the section number, then alphabetically on the names within a section, and placed in that order and comma separated. Example: </p>
<p> <a href="/docs/linux/man/1-ls/">ls</a>(1), <a href="/docs/linux/man/1-ps/">ps</a>(1), <a href="/docs/linux/man/5-group/">group</a>(5), <a href="/docs/linux/man/5-passwd/">passwd</a>(5) Li &quot;.Sh STANDARDS&quot; If the command, library function or file adheres to a specific implementation such as St -p1003.2 or St -ansiC this should be noted here. If the command does not adhere to any standard, its history should be noted in the <i>HISTORY</i> section. Li &quot;.Sh HISTORY&quot; Any command which does not adhere to any specific standards should be outlined historically in this section. Li &quot;.Sh AUTHORS&quot; Credits should be placed here. Use the `.An macro &#8216; for names and the `.Aq macro &#8216; for e-mail addresses within optional contact information. Explicitly indicate whether the person authored the initial manual page or the software or whatever the person is being credited for. Li &quot;.Sh BUGS&quot; Blatant problems with the topic go here. </p>
<p> User-specified `.</p>
<h2>sections</h2>
<p>&#8216; may be added; for example, this section was set with: </p>
<pre>.Sh &quot;PAGE STRUCTURE DOMAIN&quot;</pre>
<h3>Subsection Headers</h3>
<p>Subsection headers have exactly the same syntax as section headers: `.</p>
<h3>is</h3>
<p>&#8216; parsed but not generally callable. It can be used as an argument in a call to `.</p>
<h3>only;</h3>
<p>&#8216; it then reactivates the default font for `.</p>
<h3></h3>
<p>&#8216; </p>
<p> The default width is 8n.</p>
<h3>Paragraphs and Line Spacing</h3>
<dl>
<dt><code>.</p>
<p> </code></p>
<dd>The `.</p>
<p> &#8216; paragraph command may be used to specify a line space where necessary. The macro is not necessary after a `.</dl>
</dl>
<h2>or</h2>
<p>&#8216; `.</p>
<h3>macro</h3>
<p>&#8216; or before a `.</p>
<dl>
<p> &#8216; or `. &#8216; macro (which both assert a vertical distance unless the &#8211;<code>compact</code> flag is given). </p>
<p> The macro is neither callable nor parsed and takes no arguments; an alternative name is `.Lp &#8216;</dl>
<h3>Keeps</h3>
<p>The only keep that is implemented at this time is for words. The macros are `.(begin &#8216; keep) and `.(end &#8216; keep). The only option that `.accepts &#8216; currently is &#8211;<code>words</code> (this is also the default if no option is given) which is useful for preventing line breaks in the middle of options. In the example for the make command-line arguments (see Sx What&#8217;s in a Name ) , the keep prevented nroff from placing up the flag and the argument on separate lines. </p>
<p> Both macros are neither callable nor parsed. </p>
<p> More work needs to be done with the keep macros; specifically, a &#8211;<code>line</code> option should be added.</p>
<h3>Examples and Displays</h3>
<p>There are seven types of displays. </p>
<dl>
<dt><code>.D1</code></p>
<dd>(This is D-one.) Display one line of indented text. This macro is parsed but not callable. </p>
<p> The above was produced by: <code>.D1 -ldghfstru</code></p>
<dt><code>. </p>
<blockquote><p></code><tt>(This is D-ell.)</tt></p></blockquote>
<dd>Display one line of indented <i>literal</i> text. The `. </p>
<blockquote><p><tt>example</tt></p></blockquote>
<p> &#8216; macro has been used throughout this file. It allows the indentation (display) of one line of text. Its default font is set to constant width (literal). `. </p>
<blockquote><p><tt>is</tt></p></blockquote>
<p> &#8216; parsed but not callable. </p>
<blockquote><p><tt>% ls -ldg /usr/local/bin</tt></p></blockquote>
<p> The above was produced by: <code>. </p>
<blockquote><p></code><tt>% ls \-ldg /usr/local/bin</tt></p></blockquote>
<dt><code>. </code></p>
<dd>Begin display. The `. &#8216; display must be ended with the `. &#8216; macro. It has the following syntax: </p>
<dl>
<dt><code>. </code></p>
<dd>Br o -literal | -filled | -unfilled | -ragged | -centered Brc [-offset Ao string Ac [-file Ao file name Ac [-compact ] ] ]</dl>
<dl>
<dt><code>-ragged</code></p>
<dd>Fill, but do not adjust the right margin (only left-justify).</p>
<dt><code>-centered</code></p>
<dd>Center lines between the current left and right margin. Note that each single line is centered.</p>
<dt><code>-unfilled</code></p>
<dd>Do not fill; display a block of text as typed, using line breaks as specified by the user. This can produce overlong lines without warning messages.</p>
<dt><code>-filled</code></p>
<dd>Display a filled block. The block of text is formatted (i.e., the text is justified on both the left and right side).</p>
<dt><code>-literal</code></p>
<dd>Display block with literal font (usually fixed-width). Useful for source code or simple tabbed or spaced text.</p>
<dt><code>-file Ao </code><i>file name Ac </i>The file whose name follows the</p>
<dd>&#8211;<code>file</code> flag is read and displayed before any data enclosed with `. &#8216; and `. &#8216; using the selected display type. Any troff/NsNm-mdoc commands in the file will be processed.</p>
<dt><code>-offset Ao </code><i>string Ac </i>If &#8211;<code>offset</code></p>
<dd>is specified with one of the following strings, the string is interpreted to indicate the level of indentation for the forthcoming block of text: </p>
<dl>
<dt><i>left</i></p>
<dd>Align block on the current left margin; this is the default mode of `. &#8216;</p>
<dt><i>center</i></p>
<dd>Supposedly center the block. At this time unfortunately, the block merely gets left aligned about an imaginary center margin.</p>
<dt><i>indent</i></p>
<dd>Indent by one default indent value or tab. The default indent value is also used for the `.D1&#8242; and `. </p>
<blockquote><p><tt>macros,</tt></p></blockquote>
<p> &#8216; so one is guaranteed the two types of displays will line up. The indentation value is normally set to~6n or about two thirds of an inch (six constant width characters).</p>
<dt><i>indent-two</i></p>
<dd>Indent two times the default indent value.</p>
<dt><i>right</i></p>
<dd>This <i>left</i> aligns the block about two inches from the right side of the page. This macro needs work and perhaps may never do the right thing within troff.</dl>
<p> If Ao string Ac is a valid numeric expression instead ( <i>with a scale indicator other than</i> `<i>u</i> &#8216; use that value for indentation. The most useful scale indicators are `m&#8217; and `n&#8217; specifying the so-called <i>and</i> <i>En </i>square This is approximately the width of the letters `m&#8217; and `n&#8217; respectively of the current font (for nroff output, both scale indicators give the same values). If Ao string Ac isn&#8217;t a numeric expression, it is tested whether it is an <code>-mdoc</code> macro name, and the default offset value associated with this macro is used. Finally, if all tests fail, the width of Ao string Ac (typeset with a fixed-width font) is taken as the offset.</p>
<dt><code>-compact</code></p>
<dd>Suppress insertion of vertical space before begin of display.</dl>
<dt><code>. </code></p>
<dd>End display (takes no arguments).</dl>
<h3>Lists and Columns</h3>
<p>There are several types of lists which may be initiated with the `.</p>
<dl>
<p> &#8216; begin-list macro. Items within the list are specified with the `.</p>
<dt><code>item</code></p>
<dd>&#8216; macro, and each list must end with the `.</dl>
<p> &#8216; macro. Lists may be nested within themselves and within displays. The use of columns inside of lists or lists inside of columns is unproven. </p>
<p> In addition, several list attributes may be specified such as the width of a tag, the list offset, and compactness (blank lines between items allowed or disallowed). Most of this document has been formatted with a tag style list ( &#8211;<code>tag</code> </p>
<p> It has the following syntax forms: </p>
<dl>
<dt><code>.</p>
<dl>
<p> </code></p>
<dd>Br o -hang | -ohang | -tag | -diag | -inset Brc [-width Ao string Ac ] [-offset Ao string Ac [-compact ] ]</p>
<dt><code>.</p>
<dl>
<p> </code></p>
<dd><code>-column </code>[-offset Ao string Ac ] Ao string1 Ac Ao string2 Ac &#8230; Xc</p>
<dt><code>.</p>
<dl>
<p> </code></p>
<dd>Br o -item | -enum Oo -nested Oc | -bullet | -hyphen | -dash Brc [-offset Ao string Ac [-compact ] ]</dl>
<p> And now a detailed description of the list types. </p>
<dl>
<dt><code>-bullet</code></p>
<dd>A bullet list. </p>
<blockquote>
<pre>.Bl -bullet -offset indent -compact
.It
Bullet one goes here.
.It
Bullet two here.
.El</pre>
</blockquote>
<p> Produces: </p>
<ul>
<li> Bullet one goes here.
<li> Bullet two here. </ul>
<dt><code>-dash ( or -hyphen</code></p>
<dd>A dash list. </p>
<blockquote>
<pre>.Bl -dash -offset indent -compact
.It
Dash one goes here.
.It
Dash two here.
.El</pre>
</blockquote>
<p> Produces: </p>
<dl>
<dt><code>Dash one goes here.</code></p>
<dd>
<dt><code>Dash two here.</code></p>
<dd></dl>
<dt><code>-enum</code></p>
<dd>An enumerated list. </p>
<blockquote>
<pre>.Bl -enum -offset indent -compact
.It
Item one goes here.
.It
And item two here.
.El</pre>
</blockquote>
<p> The result: </p>
<ol>
<li> Item one goes here.
<li> And item two here. </ol>
<p> If you want to nest enumerated lists, use the &#8211;<code>nested</code> flag (starting with the second-level list): </p>
<blockquote>
<pre>.Bl -enum -offset indent -compact
.It
Item one goes here
.Bl -enum -nested -compact
.It
Item two goes here.
.It
And item three here.
.El
.It
And item four here.
.El</pre>
</blockquote>
<p> Result: </p>
<ol>
<li> Item one goes here.
<ol>
<li> Item two goes here.
<li> And item three here. </ol>
<li> And item four here. </ol>
<dt><code>-item</code></p>
<dd>A list of type &#8211;<code>item</code> without list markers. </p>
<blockquote>
<pre>.Bl -item -offset indent
.It
Item one goes here.
Item one goes here.
Item one goes here.
.It
Item two here.
Item two here.
Item two here.
.El</pre>
</blockquote>
<p> Produces: </p>
<dl>
<dt><code>Item one goes here.</code></p>
<dd>Item one goes here. Item one goes here.</p>
<dt><code>Item two here.</code></p>
<dd>Item two here. Item two here.</dl>
<dt><code>-tag</code></p>
<dd>A list with tags. Use &#8211;<code>width</code> to specify the tag width. </p>
<dl>
<dt><code>SL</code></p>
<dd>sleep time of the process (seconds blocked)</p>
<dt><code>PAGEIN</code></p>
<dd>number of disk <code>I/O &#8216;s</code> resulting from references by the process to pages not loaded in core.</p>
<dt><code>UID</code></p>
<dd>numerical user-id of process owner</p>
<dt><code>PPID</code></p>
<dd>numerical id of parent of process priority (non-positive when in non-interruptible wait)</dl>
<p> The raw text: </p>
<blockquote>
<pre>.Bl -tag -width &quot;PPID&quot; -compact -offset indent
.It SL
sleep time of the process (seconds blocked)
.It PAGEIN
number of disk
.Tn I/O Ns 's
resulting from references by the process
to pages not loaded in core.
.It UID
numerical user-id of process owner
.It PPID
numerical id of parent of process priority
(non-positive when in non-interruptible wait)
.El</pre>
</blockquote>
<dt><code>-diag</code></p>
<dd>Diag lists create section four diagnostic lists and are similar to inset lists except callable macros are ignored. The &#8211;<code>width</code> flag is not meaningful in this context. </p>
<p> Example: </p>
<blockquote>
<pre>.Bl -diag
.It You can't use Sy here.
The message says all.
.El</pre>
</blockquote>
<p> produces</p>
<dl>
<dt><code>You can&#8217;t use here.</code></p>
<dd>The message says all.</dl>
<dt><code>-hang</code></p>
<dd>A list with hanging tags.</p>
<dl>
<dt><i>Hanged</i></p>
<dd>labels appear similar to tagged lists when the label is smaller than the label width.</p>
<dt><i>Longer hanged list labels</i></p>
<dd>blend into the paragraph unlike tagged paragraph labels.</dl>
<p> And the unformatted text which created it: </p>
<blockquote>
<pre>.Bl -hang -offset indent
.It Em Hanged
labels appear similar to tagged lists when the
label is smaller than the label width.
.It Em Longer hanged list labels
blend into the paragraph unlike
tagged paragraph labels.
.El</pre>
</blockquote>
<dt><code>-ohang</code></p>
<dd>Lists with overhanging tags do not use indentation for the items; tags are written to a separate line. </p>
<dl>
<dt><code>SL</code></p>
<dd>sleep time of the process (seconds blocked)</p>
<dt><code>PAGEIN</code></p>
<dd>number of disk <code>I/O &#8216;s</code> resulting from references by the process to pages not loaded in core.</p>
<dt><code>UID</code></p>
<dd>numerical user-id of process owner</p>
<dt><code>PPID</code></p>
<dd>numerical id of parent of process priority (non-positive when in non-interruptible wait)</dl>
<p> The raw text: </p>
<blockquote>
<pre>.Bl -ohang -offset indent
.It Sy SL
sleep time of the process (seconds blocked)
.It Sy PAGEIN
number of disk
.Tn I/O Ns 's
resulting from references by the process
to pages not loaded in core.
.It Sy UID
numerical user-id of process owner
.It Sy PPID
numerical id of parent of process priority
(non-positive when in non-interruptible wait)
.El</pre>
</blockquote>
<dt><code>-inset</code></p>
<dd>Here is an example of inset labels:</p>
<dl>
<dt><i>Tag</i></p>
<dd>The tagged list (also called a tagged paragraph) is the most common type of list used in the Berkeley manuals. Use a &#8211;<code>width</code> attribute as described below.</p>
<dt><i>Diag</i></p>
<dd>Diag lists create section four diagnostic lists and are similar to inset lists except callable macros are ignored.</p>
<dt><i>Hang</i></p>
<dd>Hanged labels are a matter of taste.</p>
<dt><i>Ohang</i></p>
<dd>Overhanging labels are nice when space is constrained.</p>
<dt><i>Inset</i></p>
<dd>Inset labels are useful for controlling blocks of paragraphs and are valuable for converting <code>-mdoc</code> manuals to other formats.</dl>
<p> Here is the source text which produced the above example: </p>
<blockquote>
<pre>.Bl -inset -offset indent
.It Em Tag
The tagged list (also called a tagged paragraph)
is the most common type of list used in the
Berkeley manuals.
.It Em Diag
Diag lists create section four diagnostic lists
and are similar to inset lists except callable
macros are ignored.
.It Em Hang
Hanged labels are a matter of taste.
.It Em Ohang
Overhanging labels are nice when space is constrained.
.It Em Inset
Inset labels are useful for controlling blocks of
paragraphs and are valuable for converting
.Nm -mdoc
manuals to other formats.
.El</pre>
</blockquote>
<dt><code>-column</code></p>
<dd>This list type generates multiple columns. The number of columns and the width of each column is determined by the arguments to the &#8211;<code>column</code> list, Aq Ar string1 , Aq Ar string2 , etc. If Aq Ar stringN starts with a `.&#8217; (dot) immediately followed by a valid <code>-mdoc</code> macro name, interpret Aq Ar stringN and use the width of the result. Otherwise, the width of Aq Ar stringN (typeset with a fixed-width font) is taken as the <i>N </i><code>th</code> column width. </p>
<p> Each `.</p>
<dt><code>argument</code></p>
<dd>&#8216; is parsed to make a row, each column within the row is a separate argument separated by a tab or the `.Ta macro. &#8216; </p>
<p> The table:</p>
<dl>
<dt><code>String Ta </code><code>Nroff Ta </code><code>Troff</code></p>
<dd>
<dt><code>&lt;= Ta </code>&lt;= Ta &lt;=</p>
<dd>
<dt><code>&gt;= Ta </code>&gt;= Ta &#038;gt=;</p>
<dd></dl>
<p> was produced by: </p>
<pre>.Bl -column -offset indent &quot;.Sy String&quot; &quot;.Sy Nroff&quot; &quot;.Sy Troff&quot;
.It Sy String Ta Sy Nroff Ta Sy Troff
.It Li &lt;= Ta &lt;= Ta \*(&lt;=
.It Li &gt;= Ta &gt;= Ta \*(&gt;=
.El</pre>
<p>Don&#8217;t abuse this list type! For more complicated cases it might be far better and easier to use <a href="/docs/linux/man/1-tbl/">tbl</a>(1), the table preprocessor.</dl>
<p> Other keywords:</p>
<dl>
<dt><code>-width Ao </code><i>string Ac </i>If Aq <i>string</i></p>
<dd>starts with a `.&#8217; (dot) immediately followed by a valid <code>-mdoc</code> macro name, interpret Aq Ar string and use the width of the result. Almost all lists in this document use this option. </p>
<p> Example: </p>
<blockquote>
<pre>.Bl -tag -width &quot;.Fl test Ao Ar string Ac&quot;
.It Fl test Ao Ar string Ac
This is a longer sentence to show how the
.Fl width
flag works in combination with a tag list.
.El</pre>
</blockquote>
<p> gives:</p>
<dl>
<dt><code>-test Ao </code><i>string Ac </i>This is a longer sentence to show how the</p>
<dd>&#8211;<code>width</code> flag works in combination with a tag list.</dl>
<p> (Note that the current state of <code>-mdoc</code> is saved before Aq Ar string is interpreted; afterwards, all variables are restored again. However, boxes (used for enclosures) can&#8217;t be saved in <code>GNU</code> <a href="/docs/linux/man/1-troff/">troff</a>(1); as a consequence, arguments must always be <i>balanced</i> to avoid nasty errors. For example, do not write `.Ao <i>string</i> &#8216; but `.Ao <i>string</i> &#8216; Xc instead if you really need only an opening angle bracket.) </p>
<p> Otherwise, if Aq Ar string is a valid numeric expression <i>( with a scale indicator other than</i> `<i>u</i> &#8216; use that value for indentation. The most useful scale indicators are `m&#8217; and `n&#8217; specifying the so-called <i>and</i> <i>En </i>square This is approximately the width of the letters `m&#8217; and `n&#8217; respectively of the current font (for nroff output, both scale indicators give the same values). If Aq Ar string isn&#8217;t a numeric expression, it is tested whether it is an <code>-mdoc</code> macro name, and the default width value associated with this macro is used. Finally, if all tests fail, the width of Aq Ar string (typeset with a fixed-width font) is taken as the width. </p>
<p> If a width is not specified for the tag list type, `6n&#8217; is used.</p>
<dt><code>-offset Ao </code><i>string Ac </i>If Aq <i>string</i></p>
<dd>is <i>indent</i> a default indent value (normally set to~6n, similar to the value used in `. </p>
<blockquote><p><tt>or</tt></p></blockquote>
<p> &#8216; `. &#8216; is used. If Aq Ar string is a valid numeric expression instead ( <i>with a scale indicator other than</i> `<i>u</i> &#8216; use that value for indentation. The most useful scale indicators are `m&#8217; and `n&#8217; specifying the so-called <i>and</i> <i>En </i>square This is approximately the width of the letters `m&#8217; and `n&#8217; respectively of the current font (for nroff output, both scale indicators give the same values). If Aq Ar string isn&#8217;t a numeric expression, it is tested whether it is an <code>-mdoc</code> macro name, and the default offset value associated with this macro is used. Finally, if all tests fail, the width of Aq Ar string (typeset with a fixed-width font) is taken as the offset.</p>
<dt><code>-compact</code></p>
<dd>Suppress insertion of vertical space before the list and between list items.</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
<h2>Miscellaneous Macros</h2>
<p>Here a list of the remaining macros which do not fit well into one of the above sections. We couldn&#8217;t find real examples for the following macros: `.Me and &#8216; `.Ot &#8216; They are documented here for completeness &#8211; if you know how to use them properly please send a mail to Mt groff [at] gnu.org (including an example).</p>
<dl>
<dt><code>. is currently in beta test. </code></p>
<dd>prints </p>
<blockquote><p> is currently in beta test. </p></blockquote>
<p> It is neither callable nor parsed and takes no arguments.</p>
<dt><code>.</p>
<p> </code></p>
<dd>
<blockquote><p><tt>Usage: .</tt><code>Ao </code>function return value Ac &#8230; </p></blockquote>
<p> Don&#8217;t use this macro. It allows a break right before the return value (usually a single digit) which is bad typographical behaviour. Use `\~&#8217; to tie the return value to the previous word.</p>
<dt><code>.Hf </code>Use this macro to include a (header) file literally.</p>
<dd>It first prints `File:&#8217; followed by the file name, then the contents of Ao file Ac . </p>
<blockquote><p><tt>Usage: .Hf </tt>Ao file Ac </p>
</blockquote>
<p> It is neither callable nor parsed.</p>
<dt><code>.Lk </code>To be written.</p>
<dd>
<dt><code>.Me </code>Exact usage unknown.</p>
<dd>The documentation in the <code>-mdoc</code> source file describes it as a macro for &#8220;menu entries&#8221; </p>
<p> Its default width is 6n.</p>
<dt><code>.Mt </code>To be written.</p>
<dd>
<dt><code>.Ot </code>Exact usage unknown.</p>
<dd>The documentation in the <code>-mdoc</code> source file describes it as &#8220;old function type (fortran)&#8221;</p>
<dt><code>. </code></p>
<dd>Activate (toggle) space mode. </p>
<blockquote><p><tt>Usage: . </tt></p></blockquote>
<p> If space mode is off, no spaces between macro arguments are inserted. If called without a parameter (or if the next parameter is neither `on&#8217; nor `off&#8217; , `. &#8216; toggles space mode.</p>
<dt><code>.Ud </code>prints</p>
<dd>
<blockquote><p> Ud </p></blockquote>
<p> It is neither callable nor parsed and takes no arguments.</dl>
<h2>Predefined Strings</h2>
<p>The following strings are predefined: </p>
<table>
<tr VALIGN=top>
<td><code>String</code></td>
<td><code>Nroff</code></td>
<td><code>Troff</code></td>
<td><code>Meaning</code>
</td>
</tr>
<tr VALIGN=top>
<td>&lt;=</td>
<td>&lt;= </td>
<td>&lt;=</td>
<td>less equal
</td>
</tr>
<tr VALIGN=top>
<td>&gt;=</td>
<td>&gt;= </td>
<td>&#038;gt=;</td>
<td>greater equal
</td>
</tr>
<tr VALIGN=top>
<td>Rq</td>
<td>&#8221; </td>
<td>&rdquo;</td>
<td>right double quote
</td>
</tr>
<tr VALIGN=top>
<td>Lq</td>
<td>&#8220; </td>
<td>&ldquo;</td>
<td>left double quote
</td>
</tr>
<tr VALIGN=top>
<td>ua</td>
<td>^ </td>
<td>^</td>
<td>upwards arrow
</td>
</tr>
<tr VALIGN=top>
<td>aa</td>
<td>&#8216; </td>
<td>&#8216;</td>
<td>acute accent
</td>
</tr>
<tr VALIGN=top>
<td>ga</td>
<td>` </td>
<td>`</td>
<td>grave accent
</td>
</tr>
<tr VALIGN=top>
<td>q </td>
<td>&quot; </td>
<td>&quot; </td>
<td>straight double quote
</td>
</tr>
<tr VALIGN=top>
<td>Pi</td>
<td>pi </td>
<td>Pi</td>
<td>greek pi
</td>
</tr>
<tr VALIGN=top>
<td>Ne</td>
<td>!= </td>
<td>!=</td>
<td>not equal
</td>
</tr>
<tr VALIGN=top>
<td>Le</td>
<td>&lt;= </td>
<td>&lt;=</td>
<td>less equal
</td>
</tr>
<tr VALIGN=top>
<td>Ge</td>
<td>&gt;= </td>
<td>&#038;gt=;</td>
<td>greater equal
</td>
</tr>
<tr VALIGN=top>
<td>Lt</td>
<td>&lt; </td>
<td>&lt;</td>
<td>less than
</td>
</tr>
<tr VALIGN=top>
<td>Gt</td>
<td>&gt; </td>
<td>&gt;</td>
<td>greater than
</td>
</tr>
<tr VALIGN=top>
<td>Pm</td>
<td>+- </td>
<td>&plusmn;</td>
<td>plus minus
</td>
</tr>
<tr VALIGN=top>
<td>If</td>
<td>infinity</td>
<td>&infin;</td>
<td>infinity
</td>
</tr>
<tr VALIGN=top>
<td>Am</td>
<td>&amp;</td>
<td>&amp;</td>
<td>ampersand
</td>
</tr>
<tr VALIGN=top>
<td>Na</td>
<td>NaN</td>
<td>NaN</td>
<td>not a number
</td>
</tr>
<tr VALIGN=top>
<td>Ba</td>
<td>|</td>
<td>|</td>
<td>vertical bar
</td>
</tr>
</table>
<p> The names of the columns <code>Nroff</code> and <code>Troff</code> are a bit misleading; <code>Nroff</code> shows the <code>ASCII</code> representation, while <code>Troff</code> gives the best glyph form available. For example, a Unicode enabled <code>TTY &#8211; device will have proper glyph representations for all strings, whereas the</code> enhancement for a Latin1 <code>TTY &#8211; device is only the plus-minus sign.</code> </p>
<p> String names which consist of two characters can be written as `\*(xx&#8217; ; string names which consist of one character can be written as `\*x&#8217; A generic syntax for a string name of any length is `\*[xxx]&#8217; (this is a <code>GNU</code> <a href="/docs/linux/man/1-troff/">troff</a>(1) extension). # #===================================================================== #</p>
<h2>Diagnostics</h2>
<p>The debugging macro `.Db available &#8216; in previous versions of <code>-mdoc</code> has been removed since <code>GNU</code> <a href="/docs/linux/man/1-troff/">troff</a>(1) provides better facilities to check parameters; additionally, many error and warning messages have been added to this macro package, making it both more robust and verbose. </p>
<p> The only remaining debugging macro is `.Rd which &#8216; yields a register dump of all global registers and strings. A normal user will never need it.</p>
<h2>Formatting With Groff, Troff, And Nroff</h2>
<p>By default, the package inhibits page breaks, headers, and footers if displayed with a <code>TTY</code> device like `latin1&#8242; or `unicode&#8217; to make the manual more efficient for viewing on-line. This behaviour can be changed (e.g. to create a hardcopy of the <code>TTY</code> output) by setting the register `cR&#8217; to zero while calling <a href="/docs/linux/man/1-groff/">groff</a>(1), resulting in multiple pages instead of a single, very long page: </p>
<blockquote><p><tt>groff -Tlatin1 -rcR=0 -mdoc foo.man &gt; foo.txt</tt></p></blockquote>
<p> For double-sided printing, set register `D&#8217; to~1: </p>
<blockquote><p><tt>groff -Tps -rD1 -mdoc foo.man &gt; foo.ps</tt></p></blockquote>
<p> To change the document font size to 11pt or 12pt, set register `S&#8217; accordingly: </p>
<blockquote><p><tt>groff -Tdvi -rS11 -mdoc foo.man &gt; foo.dvi</tt></p></blockquote>
<p> Register `S&#8217; is ignored for <code>TTY</code> devices. </p>
<p> The line and title length can be changed by setting the registers `LL&#8217; and `LT&#8217; , respectively: </p>
<blockquote><p><tt>groff -Tutf8 -rLL=100n -rLT=100n -mdoc foo.man | less</tt></p></blockquote>
<p> If not set, both registers default to 78n for TTY devices and 6.5i otherwise.</p>
<h2>Files</h2>
<dl>
<dt><code>doc.tmac </code></p>
<dd>The main manual macro package.</p>
<dt><code>mdoc.tmac </code></p>
<dd>A wrapper file to call doc.tmac</p>
<dt><code>mdoc/doc-common </code></p>
<dd>Common strings, definitions, stuff related typographic output.</p>
<dt><code>mdoc/doc-nroff </code></p>
<dd>Definitions used for a <code>TTY</code> output device.</p>
<dt><code>mdoc/doc-ditroff </code></p>
<dd>Definitions used for all other devices.</p>
<dt><code>mdoc.local </code></p>
<dd>Local additions and customizations.</p>
<dt><code>andoc.tmac </code></p>
<dd>Use this file if you don&#8217;t know whether the <code>-mdoc</code> or the <code>-man</code> package should be used. Multiple man pages (in either format) can be handled.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-groff/">groff</a>(1), <a href="/docs/linux/man/1-man/">man</a>(1), <a href="/docs/linux/man/1-troff/">troff</a>(1), groff_man7</p>
<h2>Bugs</h2>
<p>Section 3f has not been added to the header routines. `.<code>groff Fl m Ns Cm doc Ar</code> &#8216; font should be changed in <i>NAME</i> section. `.Fn needs &#8216; to have a check to prevent splitting up if the line length is too short. Occasionally it separates the last parenthesis, and sometimes looks ridiculous if a line is in fill mode. The list and display macros do not do any keeps and certainly should be able to. </p>
