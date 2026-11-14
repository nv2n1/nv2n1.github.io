---
title: "mdoc-samples(7)"
name: "mdoc-samples"
section: "7"
letter: "m"
url: "/docs/linux/man/7-mdoc-samples/"
description: "‘ macro is mandatory. If not specified, the headers, footers and page layout defaults will not be set and things will be rather unpleasant. The Sx NAME section consists of at least three items. The..."
---

<p><code>mdoc.samples</code> &#8211; tutorial sampler for writing BSD manuals with <code>-mdoc</code></p>
<h2>Synopsis</h2>
<p><code>man mdoc.samples</code></p>
<h2>Description</h2>
<p>A tutorial sampler for writing BSD manual pages with the <code>-mdoc</code> macro package, a <i>content </i><code>-based</code> and <i>domain </i><code>-based</code> formatting package for <a href="/docs/linux/man/1-troff/">troff</a>(1). Its predecessor, the -man7 package, addressed page layout, leaving the manipulation of fonts and other typesetting details to the individual author. In <code>-mdoc</code> page layout macros make up the <i>page structure domain</i> which consists of macros for titles, section headers, displays and lists. Essentially items which affect the physical position of text on a formatted page. In addition to the page structure domain, there are two more domains, the manual domain and the general text domain. The general text domain is defined as macros which perform tasks such as quoting or emphasizing pieces of text. The manual domain is defined as macros that are a subset of the day to day informal language used to describe commands, routines and related BSD files. Macros in the manual domain handle command names, command-line arguments and options, function names, function parameters, pathnames, variables, cross references to other manual pages, and so on. These domain items have value for both the author and the future user of the manual page. It is hoped the consistency gained across the manual set will provide easier translation to future documentation tools. </p>
<p> Throughout the UNIX manual pages, a manual entry is simply referred to as a man page, regardless of actual length and without sexist intention.</p>
<h2>Getting Started</h2>
<p>Since a tutorial document is normally read when a person desires to use the material immediately, the assumption has been made that the user of this document may be impatient. The material presented in the remained of this document is outlined as follows: </p>
<ol>
<li> <code>TROFF IDIOSYNCRASIES</code>
<dl>
<dt><code>&quot;Macro Usage&quot;</code></p>
<dd>
<dt><code>&quot;Passing Space Characters in an Argument&quot;</code></p>
<dd>
<dt><code>&quot;Trailing Blank Space Characters (a warning)&quot;</code></p>
<dd>
<dt><code>&quot;Escaping Special Characters&quot;</code></p>
<dd></dl>
<li> <code>THE ANATOMY OF A MAN PAGE</code>
<dl>
<dt><code>&quot;A manual page template&quot;</code></p>
<dd></dl>
<li> <code>TITLE MACROS</code>
<li> <code>INTRODUCTION OF MANUAL AND GENERAL TEXT DOMAINS</code>
<dl>
<dt><code>&quot;What&#8217;s in a name&#8230;&quot;</code></p>
<dd>
<dt><code>&quot;General Syntax&quot;</code></p>
<dd></dl>
<li> <code>MANUAL DOMAIN</code>
<dl>
<dt><code>&quot;Addresses&quot;</code></p>
<dd>
<dt><code>&quot;Author name&quot;</code></p>
<dd>
<dt><code>&quot;Arguments&quot;</code></p>
<dd>
<dt><code>&quot;Configuration Declarations (section four only)&quot;</code></p>
<dd>
<dt><code>&quot;Command Modifier&quot;</code></p>
<dd>
<dt><code>&quot;Defined Variables&quot;</code></p>
<dd>
<dt><code>&quot;Errno&#8217;s (Section two only)&quot;</code></p>
<dd>
<dt><code>&quot;Environment Variables&quot;</code></p>
<dd>
<dt><code>&quot;Function Argument&quot;</code></p>
<dd>
<dt><code>&quot;Function Declaration&quot;</code></p>
<dd>
<dt><code>&quot;Flags&quot;</code></p>
<dd>
<dt><code>&quot;Functions (library routines)&quot;</code></p>
<dd>
<dt><code>&quot;Function Types&quot;</code></p>
<dd>
<dt><code>&quot;Interactive Commands&quot;</code></p>
<dd>
<dt><code>&quot;Names&quot;</code></p>
<dd>
<dt><code>&quot;Options&quot;</code></p>
<dd>
<dt><code>&quot;Pathnames&quot;</code></p>
<dd>
<dt><code>&quot;Variables&quot;</code></p>
<dd>
<dt><code>&quot;Cross References&quot;</code></p>
<dd></dl>
<li> <code>GENERAL TEXT DOMAIN</code>
<dl>
<dt><code>&quot;AT&amp;T Macro&quot;</code></p>
<dd>
<dt><code>&quot;BSD Macro&quot;</code></p>
<dd>
<dt><code>&quot;FreeBSD Macro&quot;</code></p>
<dd>
<dt><code>&quot;UNIX Macro&quot;</code></p>
<dd>
<dt><code>&quot;Enclosure/Quoting Macros&quot;</code></p>
<dd>
<dl>
<dt><code>&quot;Angle Bracket Quote/Enclosure&quot;</code></p>
<dd>
<dt><code>&quot;Bracket Quotes/Enclosure&quot;</code></p>
<dd>
<dt><code>&quot;Double Quote macro/Enclosure&quot;</code></p>
<dd>
<dt><code>&quot;Parenthesis Quote/Enclosure&quot;</code></p>
<dd>
<dt><code>&quot;Single Quotes/Enclosure&quot;</code></p>
<dd>
<dt><code>&quot;Prefix Macro&quot;</code></p>
<dd></dl>
<dt><code>&quot;No-</code>[or Normal Text Macro]</p>
<dd>
<dt><code>&quot;Space Macro</code></p>
<dd>
<dt><code>&quot;Section Cross References&quot;</code></p>
<dd>
<dt><code>&quot;References and Citations&quot;</code></p>
<dd>
<dt><code>&quot;Return Values (sections two and three only)&quot;</code></p>
<dd>
<dt><code>&quot;Trade Names (Acronyms and Type Names)&quot;</code></p>
<dd>
<dt><code>&quot;Extended Arguments&quot;</code></p>
<dd></dl>
<li> <code>PAGE STRUCTURE DOMAIN</code>
<dl>
<dt><code>&quot;Section Headers&quot;</code></p>
<dd>
<dt><code>&quot;Paragraphs and Line Spacing&quot;</code></p>
<dd>
<dt><code>&quot;Keeps&quot;</code></p>
<dd>
<dt><code>&quot;Displays&quot;</code></p>
<dd>
<dt><code>&quot;Font Modes (Emphasis, Literal, and Symbolic)&quot;</code></p>
<dd>
<dt><code>&quot;Lists and Columns&quot;</code></p>
<dd></dl>
<li> <code>PREDEFINED STRINGS</code>
<li> <code>DIAGNOSTICS</code>
<li> <code>FORMATTING WITH GROFF, TROFF AND NROFF</code>
<li> <code>BUGS</code> </ol>
<h2>Troff Idiosyncrasies</h2>
<p>The <code>-mdoc</code> package attempts to simplify the process of writing a man page. Theoretically, one should not have to learn the dirty details of <a href="/docs/linux/man/1-troff/">troff</a>(1) to use <code>-mdoc</code> however, there are a few limitations which are unavoidable and best gotten out of the way. And, too, be forewarned, this package is <i>not</i> fast.</p>
<h3>Macro Usage</h3>
<p>As in <a href="/docs/linux/man/1-troff/">troff</a>(1), a macro is called by placing a `.&#8217; (dot character) at the beginning of a line followed by the two character name for the macro. Arguments may follow the macro separated by spaces. It is the dot character at the beginning of the line which causes <a href="/docs/linux/man/1-troff/">troff</a>(1) to interpret the next two characters as a macro name. To place a `.&#8217; (dot character) at the beginning of a line in some context other than a macro invocation, precede the `.&#8217; (dot) with the `\&amp;&#8217; escape sequence. The `\&amp;&#8217; translates literally to a zero width space, and is never displayed in the output. </p>
<p> In general, <a href="/docs/linux/man/1-troff/">troff</a>(1) macros accept up to nine arguments, any extra arguments are ignored. Most macros in <code>-mdoc</code> accept nine arguments and, in limited cases, arguments may be continued or extended on the next line (See Sx Extensions ) . A few macros handle quoted arguments (see Sx Passing Space Characters in an Argument below). </p>
<p> Most of the <code>-mdoc</code> general text domain and manual domain macros are special in that their argument lists are <i>parsed</i> for callable macro names. This means an argument on the argument list which matches a general text or manual domain macro name and is determined to be callable will be executed or called when it is processed. In this case, the argument, although the name of a macro, is not preceded by a `.&#8217; (dot). It is in this manner that many macros are nested; for example the option macro, `.[,] &#8216; may <i>call</i> the flag and argument macros, `- &#8216; and `<i>file &#8230;</i> &#8216; to specify an optional flag with an argument:</p>
<dl>
<dt>[-<code>s </code><i>bytes</i> ]</p>
<dd>is produced by <code>.</code>[-<code>s </code><i>bytes</i> ]</dl>
<p> To prevent a two character string from being interpreted as a macro name, precede the string with the escape sequence `\&amp;&#8217; :</p>
<dl>
<dt>[-<code>s </code><i>bytes</i> ]</p>
<dd>is produced by <code>.</code>[\&amp;-<code>s \&amp;</code><i>bytes</i> ]</dl>
<p> Here the strings `- &#8216; and `<i>file &#8230;</i> &#8216; are not interpreted as macros. Macros whose argument lists are parsed for callable arguments are referred to as parsed and macros which may be called from an argument list are referred to as callable throughout this document and in the companion quick reference manual <a href="/docs/linux/man/7-mdoc/">mdoc</a>(7). This is a technical <i>faux pas</i> as almost all of the macros in <code>-mdoc</code> are parsed, but as it was cumbersome to constantly refer to macros as being callable and being able to call other macros, the term parsed has been used.</p>
<h3>Passing Space Characters in an Argument</h3>
<p>Sometimes it is desirable to give as one argument a string containing one or more blank space characters. This may be necessary to defeat the nine argument limit or to specify arguments to macros which expect particular arrangement of items in the argument list. For example, the function macro `.Fn expects &#8216; the first argument to be the name of a function and any remaining arguments to be function parameters. As <code>ANSI C</code> stipulates the declaration of function parameters in the parenthesized parameter list, each parameter is guaranteed to be at minimum a two word string. For example, Fa int foo . </p>
<p> There are two possible ways to pass an argument which contains an embedded space. <i>Implementation note</i> Unfortunately, the most convenient way of passing spaces in between quotes by reassigning individual arguments before parsing was fairly expensive speed wise and space wise to implement in all the macros for <code>AT&amp;T</code> troff. It is not expensive for groff but for the sake of portability, has been limited to the following macros which need it the most: </p>
<dl>
<dt><code>Configuration declaration (section 4</code></p>
<dd>Sx SYNOPSIS )</p>
<dt><code></p>
<dl>
<p> </code></p>
<dd>Begin list (for the width specifier).</p>
<dt><i>Emphasized text.</i></p>
<dd>
<dt><code>Fn </code>Functions (sections two and four).</p>
<dd>
<dt><code></p>
<dt>List items.</code></p>
<dd>
<dd>
<dt><code>Literal text.</code></p>
<dd>
<dt><code>Symbolic text.</code></p>
<dd>
<dt><code>%B</code></p>
<dd>Book titles.</p>
<dt><code>%J</code></p>
<dd>Journal names.</p>
<dt><code>%O</code></p>
<dd>Optional notes for a reference.</p>
<dt><code>%R</code></p>
<dd>Report title (in a reference).</p>
<dt><code>%T</code></p>
<dd>Title of article in a book or journal.</dl>
<p> One way of passing a string containing blank spaces is to use the hard or unpaddable space character `\<br />
&nbsp;,&#8217; that is, a blank space preceded by the escape character `\&#8217; This method may be used with any macro but has the side effect of interfering with the adjustment of text over the length of a line. Troff sees the hard space as if it were any other printable character and cannot split the string into blank or newline separated pieces as one would expect. The method is useful for strings which are not expected to overlap a line boundary. For example:</p>
<dl>
<dt><code>Fn </code>fetch char&nbsp;*str</p>
<dd>is created by `.Fn fetch &#8216; char\ *str</p>
<dt><code>Fn </code>fetch char *str</p>
<dd>can also be created by `.Fn fetch &#8216; \*qchar *str\*q</dl>
<p> If the `\&#8217; or quotes were omitted, `.Fn would &#8216; see three arguments and the result would be: </p>
<blockquote><p><tt>Fn </tt>fetch char *str </p></blockquote>
<p> For an example of what happens when the parameter list overlaps a newline boundary, see the Sx BUGS section.</dl>
</dl>
<h3>Trailing Blank Space Characters</h3>
<p>Troff can be confused by blank space characters at the end of a line. It is a wise preventive measure to globally remove all blank spaces from &lt;blank-space&gt;&lt;end-of-line&gt; character sequences. Should the need arise to force a blank character at the end of a line, it may be forced with an unpaddable space and the `\&amp;&#8217; escape character. For example, `string\&amp; .&#8217;</p>
<h3>Escaping Special Characters</h3>
<p>Special characters like the newline character `
&#8217; , are handled by replacing the `\&#8217; with `&#8217; (e.g., `n&#8217; ) to preserve the backslash.</p>
<h2>The Anatomy Of A Man Page</h2>
<p>The body of a man page is easily constructed from a basic template found in the file /usr/share/misc/mdoc.template Several example man pages can also be found in /usr/share/examples/mdoc</p>
<h3>A manual page template</h3>
<blockquote>
<pre>.\&quot; The following requests are required for all man pages.
.Dd Month day, year
.Os OPERATING_SYSTEM [version/release]
.Dt DOCUMENT_TITLE [section number] [volume]
.Sh NAME
.Nm name
.Nd one line description of name
.Sh SYNOPSIS
.Sh DESCRIPTION
.\&quot; The following requests should be uncommented and
.\&quot; used where appropriate. This next request is
.\&quot; for sections 2 and 3 function return values only.
.\&quot; .Sh RETURN VALUE
.\&quot; This next request is for sections 1, 6, 7 &amp; 8 only
.\&quot; .Sh ENVIRONMENT
.\&quot; .Sh FILES
.\&quot; .Sh EXAMPLES
.\&quot; This next request is for sections 1, 6, 7 &amp; 8 only
.\&quot; (command return values (to shell) and
.\&quot; fprintf/stderr type diagnostics)
.\&quot; .Sh DIAGNOSTICS
.\&quot; The next request is for sections 2 and 3 error
.\&quot; and signal handling only.
.\&quot; .Sh ERRORS
.\&quot; .Sh SEE ALSO
.\&quot; .Sh CONFORMING TO
.\&quot; .Sh HISTORY
.\&quot; .Sh AUTHORS
.\&quot; .Sh BUGS</pre>
</blockquote>
<p> The first items in the template are the macros (<code>., ., . </code> ) the document date, the operating system the man page or subject source is developed or modified for, and the man page title (<i>in uppercase</i> ) along with the section of the manual the page belongs in. These macros identify the page, and are discussed below in Sx TITLE MACROS . </p>
<p> The remaining items in the template are section headers (<code>.</code></p>
<h2>;</h2>
<p>) of which Sx NAME , Sx SYNOPSIS and Sx DESCRIPTION are mandatory. The headers are discussed in Sx PAGE STRUCTURE DOMAIN , after presentation of Sx MANUAL DOMAIN . Several content macros are used to demonstrate page layout macros; reading about content macros before page layout macros is recommended.</p>
<h2>Title Macros</h2>
<p>The title macros are the first portion of the page structure domain, but are presented first and separate for someone who wishes to start writing a man page yesterday. Three header macros designate the document title or manual page title, the operating system, and the date of authorship. These macros are one called once at the very beginning of the document and are used to construct the headers and footers only.</p>
<dl>
<dt><code>. </code></p>
<dd>The document title is the subject of the man page and must be in <code>CAPITALS</code> due to troff limitations. The section number may be 1, &#8230;, 8, and if it is specified, the volume title may be omitted. A volume title may be arbitrary or one of the following: </p>
<dl>
<dt><code>AMD<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>UNIX Ancestral Manual Documents</code></p>
<dd>
<dt><code>SMM<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>UNIX System Manager&#8217;s Manual</code></p>
<dd>
<dt><code>URM<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>UNIX Reference Manual</code></p>
<dd>
<dt><code>PRMUNIX Programmer&#8217;s Manual</code></p>
<dd></dl>
<p> The default volume labeling is<br />
 <code>URM</code> for sections 1, 6, and 7; <code>SMM</code> for section 8; <code>PRM</code> for sections 2, 3, 4, and 5.</p>
<dt><code>.operating_system release# </code></p>
<dd>The name of the operating system should be the common acronym, for example, <code>BSD</code> or <code>FreeBSD</code> or <code>ATT</code> The release should be the standard release nomenclature for the system specified, for example, 4.3, 4.3+Tahoe, V.3, V.4. Unrecognized arguments are displayed as given in the page footer. For instance, a typical footer might be: </p>
<blockquote><p><tt>.4.3BSD </tt></p></blockquote>
<p> or </p>
<blockquote><p><tt>.FreeBSD 2.2 </tt></p></blockquote>
<p> or for a locally produced set </p>
<blockquote><p><tt>.CS Department </tt></p></blockquote>
<p> The Berkeley default, `.without &#8216; an argument, has been defined as <code>BSD</code> in the site-specific file /usr/share/tmac/mdoc/doc-common It really should default to <code>LOCAL</code> Note, if the `.macro &#8216; is not present, the bottom left corner of the page will be ugly.</p>
<dt><code>.month day, year </code></p>
<dd>The date should be written formally: </p>
<blockquote><p><tt>January 25, 1989</tt></p></blockquote>
</dl>
<h2>Introduction Of Manual And General Text Domains</h2>
<h3>What&#8217;s in a name&#8230;</h3>
<p>The manual domain macro names are derived from the day to day informal language used to describe commands, subroutines and related files. Slightly different variations of this language are used to describe the three different aspects of writing a man page. First, there is the description of <code>-mdoc</code> macro request usage. Second is the description of a UNIX command <i>with</i> <code>-mdoc</code> macros and third, the description of a command to a user in the verbal sense; that is, discussion of a command in the text of a man page. </p>
<p> In the first case, <a href="/docs/linux/man/1-troff/">troff</a>(1) macros are themselves a type of command; the general syntax for a troff command is: </p>
<blockquote><p> .Va argument1 argument2 &#8230; argument9 </p></blockquote>
<p> The `.<i>is</i> &#8216; a macro command or request, and anything following it is an argument to be processed. In the second case, the description of a UNIX command using the content macros is a bit more involved; a typical Sx SYNOPSIS command line might be displayed as: </p>
<blockquote><p> <code>filter</code> [-<code>flag</code> ] <i>infile outfile</i> </p></blockquote>
<p> Here, <code>filter</code> is the command name and the bracketed string &#8211;<code>flag</code> is a <i>flag</i> argument designated as optional by the option brackets. In <code>-mdoc</code> terms, <i>infile</i> and <i>outfile</i> are called <i>arguments</i> The macros which formatted the above example: </p>
<blockquote>
<pre>.Nm filter
.Op Fl flag
.Ar infile outfile</pre>
</blockquote>
<p> In the third case, discussion of commands and command syntax includes both examples above, but may add more detail. The arguments <i>infile</i> and <i>outfile</i> from the example above might be referred to as <i>operands</i> or <i>file arguments</i> Some command-line argument lists are quite long:</p>
<dl>
<dt><code>make</code></p>
<dd>[-<code>eiknqrstv</code> ] [-<code>D </code><i>variable</i> ] [-<code>d </code><i>flags</i> ] [-<code>f </code><i>makefile</i> ] -words [-<code>I </code><i>directory</i> ] [-<code>j </code><i>max_jobs</i> ] [<i>variable=value</i> ] -words [<i>target &#8230;</i> ]</dl>
<p> Here one might talk about the command <code>make</code> and qualify the argument <i>makefile</i> as an argument to the flag, &#8211;<code>f</code> or discuss the optional file operand <i>target</i> In the verbal context, such detail can prevent confusion, however the <code>-mdoc</code> package does not have a macro for an argument <i>to</i> a flag. Instead the `<i>file &#8230;</i> &#8216; argument macro is used for an operand or file argument like <i>target</i> as well as an argument to a flag like <i>variable</i> The make command line was produced from: </p>
<blockquote>
<pre>.Nm make
.Op Fl eiknqrstv
.Op Fl D Ar variable
.Op Fl d Ar flags
.Op Fl f Ar makefile
.Op Fl I Ar directory
.Op Fl j Ar max_jobs
.Op Ar variable=value
.Bk -words
.Op Ar target ...
.Ek</pre>
</blockquote>
<p> The `.and &#8216; `.macros &#8216; are explained in Sx Keeps .</p>
<h3>General Syntax</h3>
<p>The manual domain and general text domain macros share a similar syntax with a few minor deviations: `.<i>file &#8230;</i> &#8216; `.- &#8216; `.<code>man mdoc.samples</code> &#8216; and `.differ &#8216; only when called without arguments; `.Fn and &#8216; `.impose &#8216; an order on their argument lists and the `.[and] &#8216; `.Fn macros &#8216; have nesting limitations. All content macros are capable of recognizing and properly handling punctuation, provided each punctuation character is separated by a leading space. If a request is given: </p>
<blockquote><p><tt>.</tt><code>sptr, ptr),</code> </p></blockquote>
<p> The result is: </p>
<blockquote><p><tt></tt><code>sptr, ptr),</code> </p></blockquote>
<p> The punctuation is not recognized and all is output in the literal font. If the punctuation is separated by a leading white space: </p>
<blockquote><p><tt>.</tt><code>sptr , ptr ) ,</code> </p></blockquote>
<p> The result is: </p>
<blockquote><p><tt></tt><code>sptr , ptr</code> </p></blockquote>
<p> The punctuation is now recognized and is output in the default font distinguishing it from the strings in literal font. </p>
<p> To remove the special meaning from a punctuation character escape it with `\&amp;&#8217; Troff is limited as a macro language, and has difficulty when presented with a string containing a member of the mathematical, logical or quotation set: </p>
<blockquote>
<pre>{+,-,/,*,%,&lt;,&gt;,&lt;=,&gt;=,=,==,&amp;,`,',&quot;}</pre>
</blockquote>
<p> The problem is that troff may assume it is supposed to actually perform the operation or evaluation suggested by the characters. To prevent the accidental evaluation of these characters, escape them with `\&amp;&#8217; Typical syntax is shown in the first content macro displayed below, `.<i></i> &#8216;</p>
<h2>Manual Domain</h2>
<h3>Address Macro</h3>
<p>The address macro identifies an address construct of the form addr1[,addr2[,addr3]]. </p>
<blockquote><p><tt>Usage: .</tt><i>address &#8230; [ .,:;()[]?! ]</i> </p></blockquote>
<dl>
<dt><code>.</code><i>addr1</i></p>
<dd><i>addr1</i></p>
<dt><code>.</code><i>addr1</i></p>
<dd><i>addr1</i></p>
<dt><code>.</code><i>addr1 , file2</i></p>
<dd><i>addr1 , file2</i></p>
<dt><code>.</code><i>f1 , f2 , f3:</i></p>
<dd><i>f1 , f2 , f3</i></p>
<dt><code>.</code><i>addr&nbsp;)&nbsp;),</i></p>
<dd><i>addr ) )</i></dl>
<p> It is an error to call `.<i>without</i> &#8216; arguments. `.<i>is</i> &#8216; callable by other macros and is parsed.</p>
<h3>Author Name</h3>
<p>The `.An macro &#8216; is used to specify the name of the author of the item being documented, or the name of the author of the actual manual page. Any remaining arguments after the name information are assumed to be punctuation. </p>
<blockquote><p><tt>Usage: .An </tt>author_name [ .,:;()[]?! ] </p></blockquote>
<dl>
<dt><code>.An </code>Joe Author</p>
<dd>An Joe Author</p>
<dt><code>.An </code>Joe Author,</p>
<dd>An Joe Author ,</p>
<dt><code>.An </code>Joe Author Aq nobody [at] FreeBSD.ORG</p>
<dd>An Joe Author Aq nobody [at] FreeBSD.ORG</p>
<dt><code>.An </code>Joe Author&nbsp;)&nbsp;),</p>
<dd>An Joe Author ) ) ,</dl>
<p> The `.An macro &#8216; is parsed and is callable. It is an error to call `.An without &#8216; any arguments.</p>
<h3>Argument Macro</h3>
<p>The `.<i>file &#8230;</i> &#8216; argument macro may be used whenever a command-line argument is referenced. </p>
<blockquote><p><tt>Usage: .</tt><i>argument &#8230; [ .,:;()[]?! ]</i> </p></blockquote>
<dl>
<dt><code>.</code><i>file &#8230;</i></p>
<dd><i>file &#8230;</i></p>
<dt><code>.</code><i>file1</i></p>
<dd><i>file1</i></p>
<dt><code>.</code><i>file1</i></p>
<dd><i>file1</i></p>
<dt><code>.</code><i>file1 file2</i></p>
<dd><i>file1 file2</i></p>
<dt><code>.</code><i>f1 f2 f3:</i></p>
<dd><i>f1 f2 f3</i></p>
<dt><code>.</code><i>file&nbsp;)&nbsp;),</i></p>
<dd><i>file ) )</i></dl>
<p> If `.<i>file &#8230;</i> &#8216; is called without arguments, `<i>file &#8230;</i> &#8216; is assumed. The `.<i>file &#8230;</i> &#8216; macro is parsed and is callable.</p>
<h3>Configuration Declaration (section four only)</h3>
<p>The `.<code>macro</code> &#8216; is used to demonstrate a <a href="/docs/linux/man/8-config/">config</a>(8) declaration for a device interface in a section four manual. This macro accepts quoted arguments (double quotes only). </p>
<dl>
<dt><code>device le0 at scode?</code></p>
<dd>produced by: `.<code>device</code> &#8216; le0 at scode? .</dl>
<h3>Command Modifier</h3>
<p>The command modifier is identical to the `.- &#8216; (flag) command with the exception the `.<code>macro</code> &#8216; does not assert a dash in front of every argument. Traditionally flags are marked by the preceding dash, some commands or subsets of commands do not use them. Command modifiers may also be specified in conjunction with interactive commands such as editor commands. See Sx Flags .</p>
<h3>Defined Variables</h3>
<p>A variable which is defined in an include file is specified by the macro `. &#8216; </p>
<blockquote><p><tt>Usage: .</tt><code>defined_variable &#8230; [ .,:;()[]?! ]</code> </p></blockquote>
<dl>
<dt><code>.MAXHOSTNAMELEN</code></p>
<dd><code>MAXHOSTNAMELEN</code></p>
<dt><code>.TIOCGPGRP )</code></p>
<dd><code>TIOCGPGRP</code></dl>
<p> It is an error to call `.<code>without</code> &#8216; arguments. `.<code>is</code> &#8216; parsed and is callable.</p>
<h3>Errno&#8217;s (Section two only)</h3>
<p>The `.Er errno &#8216; macro specifies the error return value for section two library routines. The second example below shows `.Er used &#8216; with the `.Bq general &#8216; text domain macro, as it would be used in a section two manual page. </p>
<blockquote><p><tt>Usage: .Er </tt>ERRNOTYPE &#8230; [ .,:;()[]?! ] </p></blockquote>
<dl>
<dt><code>.Er </code>ENOENT</p>
<dd>Er ENOENT</p>
<dt><code>.Er </code>ENOENT&nbsp;);</p>
<dd>Er ENOENT ) ;</p>
<dt><code>.Bq </code>Er ENOTDIR</p>
<dd>Bq Er ENOTDIR</dl>
<p> It is an error to call `.Er without &#8216; arguments. The `.Er macro &#8216; is parsed and is callable.</p>
<h3>Environment Variables</h3>
<p>The `.<code>macro</code> &#8216; specifies an environment variable. </p>
<blockquote><p><tt>Usage: .</tt><code>argument &#8230; [ .,:;()[]?! ]</code> </p></blockquote>
<dl>
<dt><code>.DISPLAY</code></p>
<dd><code>DISPLAY</code></p>
<dt><code>.PATH</code></p>
<dd><code>PATH</code></p>
<dt><code>.PRINTER&nbsp;)&nbsp;),</code></p>
<dd><code>PRINTER ) )</code></dl>
<p> It is an error to call `.<code>without</code> &#8216; arguments. The `.<code>macro</code> &#8216; is parsed and is callable.</p>
<h3>Function Argument</h3>
<p>The `.Fa macro &#8216; is used to refer to function arguments (parameters) outside of the Sx SYNOPSIS section of the manual or inside the Sx SYNOPSIS section should a parameter list be too long for the `.Fn macro &#8216; and the enclosure macros `.Fo and &#8216; `.Fc must &#8216; be used. `.Fa may &#8216; also be used to refer to structure members. </p>
<blockquote><p><tt>Usage: .Fa </tt>function_argument &#8230; [ .,:;()[]?! ] </p></blockquote>
<dl>
<dt><code>.Fa </code>d_namlen&nbsp;)&nbsp;),</p>
<dd>Fa d_namlen ) ) ,</p>
<dt><code>.Fa </code>iov_len</p>
<dd>Fa iov_len</dl>
<p> It is an error to call `.Fa without &#8216; arguments. `.Fa is &#8216; parsed and is callable.</p>
<h3>Function Declaration</h3>
<p>The `.Fd macro &#8216; is used in the Sx SYNOPSIS section with section two or three functions. The `.Fd macro &#8216; does not call other macros and is not callable by other macros. </p>
<blockquote><p><tt>Usage: .Fd </tt>include_file (or defined variable) </p></blockquote>
<p> In the Sx SYNOPSIS section a `.Fd request &#8216; causes a line break if a function has already been presented and a break has not occurred. This leaves a nice vertical space in between the previous function call and the declaration for the next function.</p>
<h3>Flags</h3>
<p>The `.- &#8216; macro handles command-line flags. It prepends a dash, `-&#8216; , to the flag. For interactive command flags, which are not prepended with a dash, the `.<code>(command</code> &#8216; modifier) macro is identical, but without the dash. </p>
<blockquote><p><tt>Usage: .-</tt><code>argument &#8230; [ .,:;()[]?! ]</code> </p></blockquote>
<dl>
<dt><code>.- </code></p>
<dd>&#8211;</p>
<dt><code>.-cfv</code></p>
<dd>&#8211;<code>cfv</code></p>
<dt><code>.-cfv</code></p>
<dd>&#8211;<code>cfv</code></p>
<dt><code>.-s v t</code></p>
<dd>&#8211;<code>s v t</code></p>
<dt><code>.&#8211;,</code></p>
<dd>&#8211;<code>&#8211;</code></p>
<dt><code>.-xyz&nbsp;),</code></p>
<dd>&#8211;<code>xyz )</code></dl>
<p> The `.- &#8216; macro without any arguments results in a dash representing <i>stdin</i>/<i>stdout</i>. Note that giving `.- &#8216; a single dash, will result in two dashes. The `.- &#8216; macro is parsed and is callable.</p>
<h3>Functions (library routines)</h3>
<p>The .Fn macro is modeled on ANSI C conventions. </p>
<pre>Usage: .Fn [type] function [[type] parameters ... [ .,:;()[]?! ]]</pre>
<dl>
<dt><code>.Fn </code>getchar</p>
<dd>Fn getchar</p>
<dt><code>.Fn </code>strlen ) ,</p>
<dd>Fn strlen ) ,</p>
<dt><code>.Fn </code>\*qint align\*q \*qconst * char *sptrs\*q</p>
<dd>Fn int align const * char *sptrs ,</dl>
<p> It is an error to call `.Fn without &#8216; any arguments. The `.Fn macro &#8216; is parsed and is callable, note that any call to another macro signals the end of the `.Fn call &#8216; (it will close-parenthesis at that point). </p>
<p> For functions that have more than eight parameters (and this is rare), the macros `.Fo (function &#8216; open) and `.Fc (function &#8216; close) may be used with `.Fa (function &#8216; argument) to get around the limitation. For example: </p>
<blockquote>
<pre>.Fo &quot;int res_mkquery&quot;
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
<blockquote><p> Fo int res_mkquery Fa int op Fa char *dname Fa int class Fa int type Fa char *data Fa int datalen Fa struct rrec *newrr Fa char *buf Fa int buflen Fc </p></blockquote>
<p> The `.Fo and &#8216; `.Fc macros &#8216; are parsed and are callable. In the Sx SYNOPSIS section, the function will always begin at the beginning of line. If there is more than one function presented in the Sx SYNOPSIS section and a function type has not been given, a line break will occur, leaving a nice vertical space between the current function name and the one prior. At the moment, `.Fn does &#8216; not check its word boundaries against troff line lengths and may split across a newline ungracefully. This will be fixed in the near future.</p>
<h3>Function Type</h3>
<p>This macro is intended for the Sx SYNOPSIS section. It may be used anywhere else in the man page without problems, but its main purpose is to present the function type in kernel normal form for the Sx SYNOPSIS of sections two and three (it causes a line break allowing the function name to appear on the next line). </p>
<blockquote><p><tt>Usage: .Ft </tt>type &#8230; [ .,:;()[]?! ] </p></blockquote>
<dl>
<dt><code>.Ft </code>struct stat</p>
<dd>Ft struct stat</dl>
<p> The `.Ft request &#8216; is not callable by other macros.</p>
<h3>Interactive Commands</h3>
<p>The `.<code>macro</code> &#8216; designates an interactive or internal command. </p>
<blockquote><p><tt>Usage: .</tt><code>argument &#8230; [ .,:;()[]?! ]</code> </p></blockquote>
<dl>
<dt><code>.:wq</code></p>
<dd><code>:wq</code></p>
<dt><code>.do while {&#8230;}</code></p>
<dd><code>do while {&#8230;}</code></p>
<dt><code>.setenv , unsetenv</code></p>
<dd><code>setenv , unsetenv</code></dl>
<p> It is an error to call `.<code>without</code> &#8216; arguments. The `.<code>macro</code> &#8216; is parsed and is callable.</p>
<h3>Name Macro</h3>
<p>The `.<code>man mdoc.samples</code> &#8216; macro is used for the document title or subject name. It has the peculiarity of remembering the first argument it was called with, which should always be the subject name of the page. When called without arguments, `.<code>man mdoc.samples</code> &#8216; regurgitates this initial name for the sole purpose of making less work for the author. Note: a section two or three document function name is addressed with the `.<code>man mdoc.samples</code> &#8216; in the Sx NAME section, and with `.Fn in &#8216; the Sx SYNOPSIS and remaining sections. For interactive commands, such as the `while&#8217; command keyword in <a href="/docs/linux/man/1-csh/">csh</a>(1), the `.<code>macro</code> &#8216; should be used. While the `.<code>is</code> &#8216; nearly identical to `.<code>man mdoc.samples</code> &#8216; it can not recall the first argument it was invoked with. </p>
<blockquote><p><tt>Usage: .</tt><code>argument &#8230; [ .,:;()[]?! ]</code> </p></blockquote>
<dl>
<dt><code>.mdoc.sample</code></p>
<dd><code>mdoc.sample</code></p>
<dt><code>.\-mdoc</code></p>
<dd><code>-mdoc</code></p>
<dt><code>.foo&nbsp;)&nbsp;),</code></p>
<dd><code>foo ) )</code></p>
<dt><code>.man mdoc.samples</code></p>
<dd><code>man mdoc.samples</code></dl>
<p> The `.<code>man mdoc.samples</code> &#8216; macro is parsed and is callable.</p>
<h3>Options</h3>
<p>The `.[macro] &#8216; places option brackets around the any remaining arguments on the command line, and places any trailing punctuation outside the brackets. The macros `.] &#8216; and `.[may &#8216; be used across one or more lines. </p>
<blockquote><p><tt>Usage: .</tt>[options &#8230; [ .,:;()[]?! ]] </p></blockquote>
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
<dd>[word1 word2]</dl>
<p> The `.] &#8216; and `.[macros: &#8216; </p>
<blockquote>
<pre>.Oo
.Op Fl k Ar kilobytes
.Op Fl i Ar interval
.Op Fl c Ar count
.Oc</pre>
</blockquote>
<p> Produce: [[-<code>k </code><i>kilobytes</i> ] [-<code>i </code><i>interval</i> ] [-<code>c </code><i>count</i> ] ] </p>
<p> The macros `.[,] &#8216; `.] &#8216; and `.[are &#8216; parsed and are callable.</p>
<h3>Pathnames</h3>
<p>The `.macro &#8216; formats pathnames or filenames. </p>
<blockquote><p><tt>Usage: .pathname [ .,:;()[]?! ] </tt></p></blockquote>
<dl>
<dt><code>./usr/share </code></p>
<dd>/usr/share</p>
<dt><code>./tmp/fooXXXXX&nbsp;) </code></p>
<dd>/tmp/fooXXXXX )</dl>
<p> The `.macro &#8216; is parsed and is callable.</p>
<h3>Variables</h3>
<p>Generic variable reference: </p>
<blockquote><p><tt>Usage: .</tt><i>variable &#8230; [ .,:;()[]?! ]</i> </p></blockquote>
<dl>
<dt><code>.</code><i>count</i></p>
<dd><i>count</i></p>
<dt><code>.</code><i>settimer</i></p>
<dd><i>settimer</i></p>
<dt><code>.</code><i>int&nbsp;*prt&nbsp;):</i></p>
<dd><i>int&nbsp;*prt )</i></p>
<dt><code>.</code><i>char s&nbsp;]&nbsp;)&nbsp;),</i></p>
<dd><i>char s ] ) )</i></dl>
<p> It is an error to call `.<i>without</i> &#8216; any arguments. The `.<i>macro</i> &#8216; is parsed and is callable.</p>
<h3>Manual Page Cross References</h3>
<p>The `.macro &#8216; expects the first argument to be a manual page name, and the second argument, if it exists, to be either a section page number or punctuation. Any remaining arguments are assumed to be punctuation. </p>
<blockquote><p><tt>Usage: .man_page[1,...,8][ .,:;()[]?! ] </tt></p></blockquote>
<dl>
<dt><code>.mdoc </code></p>
<dd>mdoc</p>
<dt><code>.mdoc </code></p>
<dd>mdoc,</p>
<dt><code><a href="/docs/linux/man/7--mdoc/">.mdoc</a>(7) </code></p>
<dd><a href="/docs/linux/man/7-mdoc/">mdoc</a>(7)</p>
<dt><code><a href="/docs/linux/man/7--mdoc/">.mdoc</a>(7))) </code></p>
<dd><a href="/docs/linux/man/7-mdoc/">mdoc</a>(7))),</dl>
<p> The `.macro &#8216; is parsed and is callable. It is an error to call `.without &#8216; any arguments.</p>
<h2>General Text Domain</h2>
<h3>AT&amp;T Macro</h3>
<blockquote>
<pre>Usage: .At [v6 | v7 | 32v | V.1 | V.4] ... [ .,:;()[]?! ]</pre>
</blockquote>
<dl>
<dt><code>.At</code></p>
<dd>AT&amp;T System</p>
<dt><code>.AT&amp;T System v6 .</code></p>
<dd>AT&amp;T System v6 .</dl>
<p> The `.AT&amp;T System &#8216; macro is <i>not</i> parsed and <i>not</i> callable It accepts at most two arguments.</p>
<h3>BSD Macro</h3>
<blockquote><p><tt>Usage: .BSD [Version/release] ... [ .,:;()[]?! ] </tt></p></blockquote>
<dl>
<dt><code>.Bx</code></p>
<dd>BSD</p>
<dt><code>.BSD 4.3 . </code></p>
<dd>BSD 4.3</dl>
<p> The `.BSD macro &#8216; is parsed and is callable.</p>
<h3>FreeBSD Macro</h3>
<blockquote>
<pre>Usage: .Fx Version.release ... [ .,:;()[]?! ]</pre>
</blockquote>
<dl>
<dt><code>.Fx </code>2.2 .</p>
<dd>Fx 2.2 .</dl>
<p> The `.Fx macro &#8216; is <i>not</i> parsed and <i>not</i> callable It accepts at most two arguments.</p>
<h3>UNIX Macro</h3>
<blockquote><p><tt>Usage: .UNIX </tt></p></blockquote>
<dl>
<dt><code>.Ux</code></p>
<dd>UNIX</dl>
<p> The `.UNIX &#8216; macro is parsed and is callable.</p>
<h3>Enclosure and Quoting Macros</h3>
<p>The concept of enclosure is similar to quoting. The object being to enclose one or more strings between a pair of characters like quotes or parentheses. The terms quoting and enclosure are used interchangeably throughout this document. Most of the one line enclosure macros end in small letter `q&#8217; to give a hint of quoting, but there are a few irregularities. For each enclosure macro there is also a pair of open and close macros which end in small letters `o&#8217; and `c&#8217; respectively. These can be used across one or more lines of text and while they have nesting limitations, the one line quote macros can be used inside of them. </p>
<blockquote>
<dl>
<p> <i> Quote<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> Close<tt>&nbsp;<wbr>&nbsp;</tt> Open<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Function<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Result</i> .Aq<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>.Ac<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>.Ao<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Angle Bracket Enclosure&lt;string&gt;<br />
 .Bq<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>.Bc<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>.Bo<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Bracket Enclosure<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[string]<br />
 .Dq<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>.Dc<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>.Do<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Double Quote<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&#8220;string&#8221;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>.Ec<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>.Eo<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Enclose String (in XX)<tt>&nbsp;<wbr>&nbsp;</tt>XXstringXX<br />
 .Pq<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>.Pc<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>.Po<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Parenthesis Enclosure<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>(string)<br />
 .Ql<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Quoted Literal<tt>&nbsp;<wbr>&nbsp;</tt>`st&#8217; or string<br />
 .Qq<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>.Qc<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>.Qo<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Straight Double Quote<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&quot;string&quot;<br />
 .Sq<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>.Sc<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>.So<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Single Quote<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>`string&#8217;
</dl>
</blockquote>
<p> Except for the irregular macros noted below, all of the quoting macros are parsed and callable. All handle punctuation properly, as long as it is presented one character at a time and separated by spaces. The quoting macros examine opening and closing punctuation to determine whether it comes before or after the enclosing string This makes some nesting possible.</p>
<dl>
<dt><code>.Ec </code>, .Eo These macros expect the first argument to be the</p>
<dd>opening and closing strings respectively.</p>
<dt><code>.`The&#8217; </code></p>
<dd>quoted literal macro behaves differently for troff than nroff. If formatted with nroff, a quoted literal is always quoted. If formatted with troff, an item is quoted only if the width of the item is less than three constant width characters. This is to make short strings more visible where the font change to literal (constant width) is less noticeable.</p>
<dt><code>.The prefix macro is not callable, but it is parsed: </code></p>
<dd>
<dl>
<dt><code>.( Fa </code>name2</p>
<dd>becomes ( Fa name2</dl>
<p> The `.<code>(no</code> &#8216; space) macro performs the analogous suffix function.</dl>
<p> Examples of quoting:</p>
<dl>
<dt><code>.Aq </code>Aq</p>
<dt><code>.Aq </code><i>ctype.h&nbsp;),</i></p>
<dd>
<dd>Aq Ar ctype.h ) ,</p>
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
<dd>`string&#8217;</dl>
<p> For a good example of nested enclosure macros, see the `.[option] &#8216; macro. It was created from the same underlying enclosure macros as those presented in the list above. The `. &#8216; and `. &#8216; extended argument list macros were also built from the same underlying routines and are a good example of <code>-mdoc</code> macro usage at its worst.</p>
<h3>No-[or Normal Text Macro]</h3>
<p>The macro `.<code>is</code> &#8216; a hack for words in a macro command line which should <i>not</i> be formatted and follows the conventional syntax for content macros.</p>
<h3><code>Space Macro</code></h3>
<p>The `.<code>macro</code> &#8216; eliminates unwanted spaces in between macro requests. It is useful for old style argument lists where there is no space between the flag and argument:</p>
<dl>
<dt><code>.</code>[-<code>I </code><i>directory</i> ]</p>
<dd>produces [-<code>I </code><i>directory</i> ]</dl>
<p> Note: the `.<code>macro</code> &#8216; always invokes the `.<code>macro</code> &#8216; after eliminating the space unless another macro name follows it. The macro `.<code>is</code> &#8216; parsed and is callable.</p>
<h3>Section Cross References</h3>
<p>The `.Sx macro &#8216; designates a reference to a section header within the same document. It is parsed and is callable. </p>
<dl>
<dt><code>.Sx </code>FILES</p>
<dd>Sx FILES</dl>
<h3>References and Citations</h3>
<p>The following macros make a modest attempt to handle references. At best, the macros make it convenient to manually drop in a subset of refer style references. </p>
<dl>
<dt><code>.Rs</code></p>
<dd>Reference Start. Causes a line break and begins collection of reference information until the reference end macro is read.</p>
<dt><code>.Re</code></p>
<dd>Reference End. The reference is printed.</p>
<dt><code>.%A</code></p>
<dd>Reference author name, one name per invocation.</p>
<dt><code>.%B</code></p>
<dd>Book title.</p>
<dt><code>.%C</code></p>
<dd>City/place.</p>
<dt><code>.%D</code></p>
<dd>Date.</p>
<dt><code>.%J</code></p>
<dd>Journal name.</p>
<dt><code>.%N</code></p>
<dd>Issue number.</p>
<dt><code>.%O</code></p>
<dd>Optional information.</p>
<dt><code>.%P</code></p>
<dd>Page number.</p>
<dt><code>.%R</code></p>
<dd>Report name.</p>
<dt><code>.%T</code></p>
<dd>Title of article.</p>
<dt><code>.%V</code></p>
<dd>Volume(s).</dl>
<p> The macros beginning with `%&#8217; are not callable, and are parsed only for the trade name macro which returns to its caller. (And not very predictably at the moment either.) The purpose is to allow trade names to be pretty printed in troffNs/NsXrditroff output.</p>
<h3>Return Values</h3>
<p>The `.Rv macro &#8216; generates text for use in the Sx RETURN VALUE section. </p>
<blockquote><p><tt>Usage: .Rv </tt>[-std function] </p></blockquote>
<p> `.Rv -std &#8216; atexit will generate the following text: </p>
<p> Rv -std atexit </p>
<p> The &#8211;<code>std</code> option is valid only for manual page sections 2 and 3.</p>
<h3>Trade Names (or Acronyms and Type Names)</h3>
<p>The trade name macro is generally a small caps macro for all uppercase words longer than two characters. </p>
<blockquote><p><tt>Usage: .</tt><code>symbol &#8230; [ .,:;()[]?! ]</code> </p></blockquote>
<dl>
<dt><code>.DEC</code></p>
<dd><code>DEC</code></p>
<dt><code>.ASCII</code></p>
<dd><code>ASCII</code></dl>
<p> The `.<code>macro</code> &#8216; is parsed and is callable by other macros.</p>
<h3>Extended Arguments</h3>
<p>The `. &#8216; and `. &#8216; macros allow one to extend an argument list on a macro boundary. Argument lists cannot be extended within a macro which expects all of its arguments on one line such as `.[] &#8216; </p>
<p> Here is an example of `. &#8216; using the space mode macro to turn spacing off: </p>
<blockquote>
<pre>.Sm off
.It Xo Sy I Ar operation
.No n Ar count No n
.Xc
.Sm on</pre>
</blockquote>
<p> Produces </p>
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
<p> Produces </p>
<blockquote>
<dl>
<dt><code>S / </code><i>old_pattern </i> <code>/ </code><i>new_pattern</i> <code>/ </code>[<code>g</code> ]</p>
<dd></dl>
</blockquote>
<dd>Another example of `. &#8216; and using enclosure macros: Test the value of a variable. </p>
<blockquote>
<pre>.It Xo
.Ic .ifndef
.Oo \&amp;! Oc Ns Ar variable
.Op Ar operator variable ...
.Xc</pre>
</blockquote>
<p> Produces </p>
<blockquote>
<dl>
<dt> <code>.ifndef</code> [! <i>variable</i> ] [<i>operator variable &#8230;</i> ]</p>
<dd></dl>
</blockquote>
<dd>All of the above examples have used the `. &#8216; macro on the argument list of the `. &#8216; (list-item) macro. The extend macros are not used very often, and when they are it is usually to extend the list-item argument list. Unfortunately, this is also where the extend macros are the most finicky. In the first two examples, spacing was turned off; in the third, spacing was desired in part of the output but not all of it. To make these macros work in this situation make sure the `. &#8216; and `. &#8216; macros are placed as shown in the third example. If the `. &#8216; macro is not alone on the `. &#8216; argument list, spacing will be unpredictable. The `.<code>(no</code> &#8216; space macro) must not occur as the first or last macro on a line in this situation. Out of 900 manual pages (about 1500 actual pages) currently released with BSD only fifteen use the `. &#8216; macro.</p>
<h2>Page Structure Domain</h2>
<h3>Section Headers</h3>
<p>The first three `.</p>
<h2>section</h2>
<p>&#8216; header macros list below are required in every man page. The remaining section headers are recommended at the discretion of the author writing the manual page. The `.</p>
<h2>macro</h2>
<p>&#8216; can take up to nine arguments. It is parsed and but is not callable.</p>
<dl>
<dt><code>.</dl>
</dl>
<p> </code></p>
<h2>Name</h2>
<dd>The `.</p>
<h2>Name</h2>
<p>&#8216; macro is mandatory. If not specified, the headers, footers and page layout defaults will not be set and things will be rather unpleasant. The Sx NAME section consists of at least three items. The first is the `.<code>man mdoc.samples</code> &#8216; name macro naming the subject of the man page. The second is the Name Description macro, `. &#8211; , &#8216; which separates the subject name from the third item, which is the description. The description should be the most terse and lucid possible, as the space available is small. .Sh SYNOPSIS The Sx SYNOPSIS section describes the typical usage of the subject of a man page. The macros required are either `.Nm&#8217; , `.Cd&#8217; , `.Fn&#8217; , (and possibly `.Fo&#8217; , `.Fc&#8217; , `.Fd&#8217; , `.Ft&#8217; macros). The function name macro `.Fn&#8217; is required for manual page sections 2 and 3, the command and general name macro `.<code>man mdoc.samples</code> &#8216; is required for sections 1, 5, 6, 7, 8. Section 4 manuals require a `.Nm&#8217; , `.Fd&#8217; or a `.Cd&#8217; configuration device usage macro. Several other macros may be necessary to produce the synopsis line as shown below: </p>
<blockquote><p> <code>cat</code> [-<code>benstuv</code> ] [- ] <i>file &#8230;</i> </p></blockquote>
<p> The following macros were used: </p>
<blockquote><p><tt>.</tt><code>cat</code> </p></blockquote>
<blockquote><p><tt>.</tt>[-<code>benstuv</code> ] </p></blockquote>
<blockquote><p><tt>.</tt>[- ] </p></blockquote>
<blockquote><p><tt>.</tt><i>file &#8230;</i> </p></blockquote>
<p> <code>Note</code> The macros `.[,] &#8216; `.- &#8216; and `.<i>file &#8230;</i> &#8216; recognize the pipe bar character `|&#8217; so a command line such as: </p>
<blockquote><p><tt>&quot;.</tt>[-<code>a | -b</code> ] </p></blockquote>
<p> will not go orbital. Troff normally interprets a | as a special operator. See Sx PREDEFINED STRINGS for a usable | character in other situations.</p>
<dl>
<dt><code>.</dl>
</dl>
<p> </code></p>
<h2>Description</h2>
<dd>In most cases the first text in the Sx DESCRIPTION section is a brief paragraph on the command, function or file, followed by a lexical list of options and respective explanations. To create such a list, the `.</p>
<dl>
<p> &#8216; begin-list, `.</p>
<dt><code>list-item</code> &#8216;</p>
<dd>and `.</dl>
<p> &#8216; end-list macros are used (see Sx Lists and Columns below). </p>
<p> The following `.</p>
<h2>section</h2>
<p>&#8216; headers are part of the preferred manual page layout and must be used appropriately to maintain consistency. They are listed in the order in which they would be used.</p>
<dl>
<dt><code>.</dl>
</dl>
<p> </code></p>
<h2>Environment</h2>
<dd>The Sx ENVIRONMENT section should reveal any related environment variables and clues to their behavior and/or usage. .Sh EXAMPLES There are several ways to create examples. See the Sx EXAMPLES section below for details. .Sh FILES Files which are used or created by the man page subject should be listed via the `.macro &#8216; in the Sx FILES section. .Sh SEE ALSO References to other material on the man page topic and cross references to other relevant man pages should be placed in the Sx SEE ALSO section. Cross references are specified using the `.macro. &#8216; Cross references in the Sx SEE ALSO section should be sorted by section number, and then placed in alphabetical order and comma separated. For example: </p>
<p> <a href="/docs/linux/man/1-ls/">ls</a>(1), <a href="/docs/linux/man/1-ps/">ps</a>(1), <a href="/docs/linux/man/5-group/">group</a>(5), <a href="/docs/linux/man/5-passwd/">passwd</a>(5). </p>
<p> At this time <a href="/docs/linux/man/1-refer/">refer</a>(1) style references are not accommodated. .Sh CONFORMING TO If the command, library function or file adheres to a specific implementation such as St -p1003.2 or St -ansiC this should be noted here. If the command does not adhere to any standard, its history should be noted in the Sx HISTORY section. .Sh HISTORY Any command which does not adhere to any specific standards should be outlined historically in this section. .Sh AUTHORS Credits, if need be, should be placed here. .Sh DIAGNOSTICS Diagnostics from a command should be placed in this section. .Sh ERRORS Specific error handling, especially from library functions (man page sections 2 and 3) should go here. The `.Er macro &#8216; is used to specify an errno. .Sh BUGS Blatant problems with the topic go here&#8230; </p>
<p> User specified `.</p>
<h2>sections</h2>
<p>&#8216; may be added, for example, this section was set with: </p>
<pre>.Sh PAGE STRUCTURE DOMAIN</pre>
<h3>Paragraphs and Line Spacing.</h3>
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
<p> &#8216; macro. (The `.</p>
<dl>
<p> &#8216; macro asserts a vertical distance unless the -compact flag is given).</dl>
</dl>
</dl>
<h3>Keeps</h3>
<p>The only keep that is implemented at this time is for words. The macros are `.(begin-keep) &#8216; and `.(end-keep). &#8216; The only option that `.accepts &#8216; is &#8211;<code>words</code> and is useful for preventing line breaks in the middle of options. In the example for the make command-line arguments (see Sx What&#8217;s in a name ) , the keep prevented nroff from placing up the flag and the argument on separate lines. (Actually, the option macro used to prevent this from occurring, but was dropped when the decision (religious) was made to force right justified margins in troff as options in general look atrocious when spread across a sparse line. More work needs to be done with the keep macros, a &#8211;<code>line</code> option needs to be added.)</p>
<h3>Examples and Displays</h3>
<p>There are five types of displays, a quickie one line indented display `.D1&#8242; , a quickie one line literal display `. </p>
<blockquote><p><tt>,</tt></p></blockquote>
<p> &#8216; and a block literal, block filled and block ragged which use the `. &#8216; begin-display and `. &#8216; end-display macros. </p>
<dl>
<dt><code>.D1</code> (D-one) Display one line of indented text.</p>
<dd>This macro is parsed, but it is not callable. </p>
<blockquote><p><tt>-</tt><code>ldghfstru</code> </p></blockquote>
<p> The above was produced by: <code>. </p>
<blockquote><p></code><tt>-</tt><code>ldghfstru</code> </p></blockquote>
<dt><code>. </p>
<blockquote><p></code><tt>(D-ell)</tt></p></blockquote>
<dd>Display one line of indented <i>literal</i> text. The `. </p>
<blockquote><p><tt>example</tt></p></blockquote>
<p> &#8216; macro has been used throughout this file. It allows the indent (display) of one line of text. Its default font is set to constant width (literal) however it is parsed and will recognized other macros. It is not callable however. </p>
<blockquote><p><tt>% ls -ldg /usr/local/bin</tt></p></blockquote>
<p> The above was produced by <code>. </p>
<blockquote><p></code><tt>% ls -ldg /usr/local/bin</tt></p></blockquote>
<dt><code>. </code></p>
<dd>Begin-display. The `. &#8216; display must be ended with the `. &#8216; macro. Displays may be nested within displays and lists. `. &#8216; has the following syntax: </p>
<blockquote><p><tt>&quot;. </tt></p></blockquote>
<p> The display-type must be one of the following four types and may have an offset specifier for indentation: `. &#8216;</dl>
<dl>
<dt><code>-ragged</code></p>
<dd>Display a block of text as typed, right (and left) margin edges are left ragged.</p>
<dt><code>-filled</code></p>
<dd>Display a filled (formatted) block. The block of text is formatted (the edges are filled &#8211; not left unjustified).</p>
<dt><code>-literal</code></p>
<dd>Display a literal block, useful for source code or simple tabbed or spaced text.</p>
<dt><code>-file </code><i>file_name</i></p>
<dd>The filename following the &#8211;<code>file</code> flag is read and displayed. Literal mode is asserted and tabs are set at 8 constant width character intervals, however any troff/NsNm-mdoc commands in file will be processed.</p>
<dt><code>-offset </code><i>string</i></p>
<dd>If &#8211;<code>offset</code> is specified with one of the following strings, the string is interpreted to indicate the level of indentation for the forthcoming block of text: </p>
<dl>
<dt><i>left</i></p>
<dd>Align block on the current left margin, this is the default mode of `. &#8216;</p>
<dt><i>center</i></p>
<dd>Supposedly center the block. At this time unfortunately, the block merely gets left aligned about an imaginary center margin.</p>
<dt><i>indent</i></p>
<dd>Indents by one default indent value or tab. The default indent value is also used for the `.D1&#8242; display so one is guaranteed the two types of displays will line up. This indent is normally set to 6n or about two thirds of an inch (six constant width characters).</p>
<dt><i>indent-two</i></p>
<dd>Indents two times the default indent value.</p>
<dt><i>right</i></p>
<dd>This <i>left</i> aligns the block about two inches from the right side of the page. This macro needs work and perhaps may never do the right thing by troff.</dl>
<dt><code>&quot;.Ed&quot;</code></p>
<dd>End-display.</dl>
<h3>Font Modes</h3>
<p>There are five macros for changing the appearance of the manual page text:</p>
<dl>
<dt><code>.</code><i>Text may be stressed or emphasized with the</i> `.<i></p>
<dd>macro.</i> &#8216; The usual font for emphasis is italic. </p>
<blockquote><p><tt>Usage: .</tt><i>argument &#8230; [ .,:;()[]?! ]</i> </p></blockquote>
<dl>
<dt><code>.</code><i>does not</i> <i>does not</i></p>
<dt><code>.</code><i>exceed 1024 .</i> <i>exceed 1024</i></p>
<dt><code>.</code><i>vide infra ) ) ,</i> <i>vide infra ) )</i></dl>
<dd>The `.<i>macro</i> &#8216; is parsed and is callable. It is an error to call `.<i>without</i> &#8216; arguments.</p>
<dt><code>.The</code> `.<code></p>
<dd>literal</code> &#8216; macro may be used for special characters, variable constants, anything which should be displayed as it would be typed. </p>
<blockquote><p><tt>Usage: .</tt><code>argument &#8230; [ .,:;()[]?! ]</code> </p></blockquote>
<dl>
<dt><code>.n</code> <code>
</code></p>
<dt><code>.M1 M2 M3;</code> <code>M1 M2 M3</code></p>
<dt><code>.cntrl-D&nbsp;),</code> <code>cntrl-D )</code></p>
<dt><code>.1024 &#8230;</code> <code>1024 &#8230;</code></dl>
<dd>The `.<code>macro</code> &#8216; is parsed and is callable.</p>
<dt><code>.The symbolic emphasis macro is generally a boldface macro in</code></p>
<dd>either the symbolic sense or the traditional English usage. </p>
<blockquote><p><tt>Usage: .</tt><code>symbol &#8230; [ .,:;()[]?! ]</code> </p></blockquote>
<dl>
<dt><code>.Important Notice</code> <code>Important Notice</code> </p>
<dd>The `.<code>macro</code> &#8216; is parsed and is callable. Arguments to `.<code>may</code> &#8216; be quoted.</dl>
<dt><code>.Bf </code>Begin font mode.</p>
<dd>The `.Bf font &#8216; mode must be ended with the `.Ef macro. &#8216; Font modes may be nested within other font modes. `.Bf has &#8216; the following syntax: </p>
<blockquote><p><tt>&quot;.Bf </tt>font-mode </p></blockquote>
<p> The font-mode must be one of the following three types: `.Bf &#8216; </p>
<dl>
<dt><i>| &#8211;</i><code>emphasis</code></p>
<dd>Same as if the `.<i>macro</i> &#8216; was used for the entire block of text.</p>
<dt><code>| -literal</code></p>
<dd>Same as if the `.<code>macro</code> &#8216; was used for the entire block of text.</p>
<dt><code>| -symbolic</code></p>
<dd>Same as if the `.<code>macro</code> &#8216; was used for the entire block of text.</dl>
<dt><code>&quot;.Ef&quot;</code></p>
<dd>End font mode.</dl>
<h3>Tagged Lists and Columns</h3>
<p>There are several types of lists which may be initiated with the `.Bl&#8217; begin-list macro. Items within the list are specified with the `.It&#8217; item macro and each list must end with the `.El&#8217; macro. Lists may be nested within themselves and within displays. Columns may be used inside of lists, but lists are unproven inside of columns. </p>
<p> In addition, several list attributes may be specified such as the width of a tag, the list offset, and compactness (blank lines between items allowed or disallowed). Most of this document has been formatted with a tag style list (-<code>tag</code> ) For a change of pace, the list-type used to present the list-types is an over-hanging list (-<code>ohang</code> ) This type of list is quite popular with <code>TeX</code> users, but might look a bit funny after having read many pages of tagged lists. The following list types are accepted by `.Bl&#8217; : </p>
<dl>
<dt><code>-bullet</code></p>
<dt><code>-item</code></p>
<dt><code>-enum</code></p>
<dd>These three are the simplest types of lists. Once the `.Bl&#8217; macro has been given, items in the list are merely indicated by a line consisting solely of the `.It&#8217; macro. For example, the source text for a simple enumerated list would look like: </p>
<blockquote>
<pre>.Bl -enum -compact
.It
Item one goes here.
.It
And item two here.
.It
Lastly item three goes here.
.El</pre>
</blockquote>
</dl>
<p> The results: </p>
<ol>
<li> Item one goes here.
<li> And item two here.
<li> Lastly item three goes here. </ol>
<p> A simple bullet list construction: </p>
<blockquote>
<pre>.Bl -bullet -compact
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
<dl>
<dt><code>-tag</code></p>
<dt><code>-diag</code></p>
<dt><code>-hang</code></p>
<dt><code>-ohang</code></p>
<dt><code>-inset</code></p>
<dd>These list-types collect arguments specified with the `.</p>
<dt><code>macro</code> &#8216;</p>
<dd>and create a label which may be <i>inset</i> into the forthcoming text, <i>hanged</i> from the forthcoming text, <i>overhanged</i> from above and not indented or <i>tagged</i> This list was constructed with the `-<code>ohang</code> &#8216; list-type. The `.</p>
<dt><code>macro</code> &#8216;</p>
<dd>is parsed only for the inset, hang and tag list-types and is not callable. Here is an example of inset labels:</dl>
<dl>
<dt><i>Tag</i></p>
<dd>The tagged list (also called a tagged paragraph) is the most common type of list used in the Berkeley manuals.</p>
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
The tagged list (also called a tagged paragraph) is the
most common type of list used in the Berkeley manuals.
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
<p> Here is a hanged list with two items:</p>
<dl>
<dt><i>Hanged</i></p>
<dd>labels appear similar to tagged lists when the label is smaller than the label width.</p>
<dt><i>Longer hanged list labels</i></p>
<dd>blend in to the paragraph unlike tagged paragraph labels.</dl>
<p> And the unformatted text which created it: </p>
<blockquote>
<pre>.Bl -hang -offset indent
.It Em Hanged
labels appear similar to tagged lists when the
label is smaller than the label width.
.It Em Longer hanged list labels
blend in to the paragraph unlike
tagged paragraph labels.
.El</pre>
</blockquote>
<p> The tagged list which follows uses an optional width specifier to control the width of the tag. </p>
<dl>
<dt><code>SL</code></p>
<dd>sleep time of the process (seconds blocked)</p>
<dt><code>PAGEIN</code></p>
<dd>number of disk <code>I/O &#8216;s</code> resulting from references by the process to pages not loaded in core.</p>
<dt><code>UID</code></p>
<dd>numerical user-id of process owner</p>
<dt><code>PPID</code></p>
<dd>numerical ID of parent of process process priority (nonpositive when in noninterruptible wait)</dl>
<p> The raw text: </p>
<blockquote>
<pre>.Bl -tag -width &quot;PAGEIN&quot; -compact -offset indent
.It SL
sleep time of the process (seconds blocked)
.It PAGEIN
number of disk
.Tn I/O Ns 's
resulting from references
by the process to pages not loaded in core.
.It UID
numerical user ID of process owner
.It PPID
numerical ID of parent of process process priority
(nonpositive when in noninterruptible wait)
.El</pre>
</blockquote>
<p> Acceptable width specifiers:</p>
<dl>
<dt><code>-width </code><i>Fl</i></p>
<dd>sets the width to the default width for a flag. All callable macros have a default width value. The `.- &#8216; value is presently set to ten constant width characters or about five sixth of an inch.</p>
<dt><code>-width </code><i>24n</i></p>
<dd>sets the width to 24 constant width characters or about two inches. The `n&#8217; is absolutely necessary for the scaling to work correctly.</p>
<dt><code>-width </code><i>ENAMETOOLONG</i></p>
<dd>sets width to the constant width length of the string given.</p>
<dt><code>-width </code><i>\*qint mkfifo\*q</i></p>
<dd>again, the width is set to the constant width of the string given.</dl>
<p> If a width is not specified for the tag list type, the first time `. &#8216; is invoked, an attempt is made to determine an appropriate width. If the first argument to `.It&#8217; is a callable macro, the default width for that macro will be used as if the macro name had been supplied as the width. However, if another item in the list is given with a different callable macro name, a new and nested list is assumed.</p>
<h2>Predefined Strings</h2>
<p>The following strings are predefined as may be used by preceding with the troff string interpreting sequence `\*(xx&#8217; where <i>xx</i> is the name of the defined string or as `\*x&#8217; where <i>x</i> is the name of the string. The interpreting sequence may be used any where in the text. </p>
<dl>
<dt><code>String<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Nroff<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Troff</code></p>
<dt><code>&lt;= Ta </code>&lt;= Ta &lt;=</p>
<dt><code>&gt;= Ta </code>&gt;= Ta &#038;gt=;</p>
<dt><code>Rq Ta </code>&#8221; Ta &rdquo;</p>
<dt><code>Lq Ta </code>&#8220; Ta &ldquo;</p>
<dt><code>ua Ta </code>^ Ta ^</p>
<dt><code>aa Ta </code>&#8216; Ta &#8216;</p>
<dt><code>ga Ta </code>` Ta `</p>
<dt><code>q Ta </code> Ta &quot;</p>
<dt><code>Pi Ta </code>pi Ta Pi</p>
<dt><code>Ne Ta </code>!= Ta !=</p>
<dt><code>Le Ta </code>&lt;= Ta &lt;=</p>
<dt><code>Ge Ta </code>&gt;= Ta &#038;gt=;</p>
<dt><code>Lt Ta </code>&lt; Ta &gt;</p>
<dt><code>Gt Ta </code>&gt; Ta &lt;</p>
<dt><code>Pm Ta </code>+- Ta &plusmn;</p>
<dt><code>If Ta </code>infinity Ta &infin;</p>
<dt><code>Na Ta </code><i>NaN</i> Ta NaN</p>
<dt><code>Ba Ta </code>| Ta |</dl>
<p> <code>Note</code> </p>
<dd>The string named `q&#8217; should be written as `\*q&#8217; since it is only one char.</p>
<h2>Diagnostics</h2>
<p>The debugging facilities for <code>-mdoc</code> are limited, but can help detect subtle errors such as the collision of an argument name with an internal register or macro name. (A what?) A register is an arithmetic storage class for troff with a one or two character name. All registers internal to <code>-mdoc</code> for troff and ditroff are two characters and of the form &lt;upper_case&gt;&lt;lower_case&gt; such as `<i>file &#8230;</i> &#8216; &lt;lower_case&gt;&lt;upper_case&gt; as `aR&#8217; or &lt;upper or lower letter&gt;&lt;digit&gt; as `C1&#8242; And adding to the muddle, troff has its own internal registers all of which are either two lowercase characters or a dot plus a letter or metacharacter character. In one of the introduction examples, it was shown how to prevent the interpretation of a macro name with the escape sequence `\&amp;&#8217; This is sufficient for the internal register names also. </p>
<p> If a nonescaped register name is given in the argument list of a request, unpredictable behavior will occur. In general, any time huge portions of text do not appear where expected in the output, or small strings such as list tags disappear, chances are there is a misunderstanding about an argument type in the argument list. Your mother never intended for you to remember this evil stuff &#8211; so here is a way to find out whether or not your arguments are valid: The `.Db (debug) &#8216; macro displays the interpretation of the argument list for most macros. Macros such as the `.</p>
<p> &#8216; (paragraph) macro do not contain debugging information. All of the callable macros do, and it is strongly advised whenever in doubt, turn on the `.Db macro. &#8216; </p>
<blockquote><p><tt>Usage: .Db </tt>[on | off] </p></blockquote>
<p> An example of a portion of text with the debug macro placed above and below an artificially created problem (a flag argument `aC&#8217; which should be `\&amp;aC&#8217; in order to work): </p>
<blockquote>
<pre>.Db on
.Op Fl aC Ar file )
.Db off</pre>
</blockquote>
<p> The resulting output: </p>
<blockquote>
<pre>DEBUGGING ON
DEBUG(argv) MACRO: `.Op' Line #: 2
 Argc: 1 Argv: `Fl' Length: 2
 Space: `' Class: Executable
 Argc: 2 Argv: `aC' Length: 2
 Space: `' Class: Executable
 Argc: 3 Argv: `Ar' Length: 2
 Space: `' Class: Executable
 Argc: 4 Argv: `file' Length: 4
 Space: ` ' Class: String
 Argc: 5 Argv: `)' Length: 1
 Space: ` ' Class: Closing Punctuation or suffix
 MACRO REQUEST: .Op Fl aC Ar file )
DEBUGGING OFF</pre>
</blockquote>
<p> The first line of information tells the name of the calling macro, here `.[,] &#8216; and the line number it appears on. If one or more files are involved (especially if text from another file is included), the line number may be bogus. If there is only one file, it should be accurate. The second line gives the argument count, the argument (`- &#8216; ) and its length. If the length of an argument is two characters, the argument is tested to see if it is executable (unfortunately, any register which contains a nonzero value appears executable). The third line gives the space allotted for a class, and the class type. The problem here is the argument aC should not be executable. The four types of classes are string, executable, closing punctuation and opening punctuation. The last line shows the entire argument list as it was read. In this next example, the offending `aC&#8217; is escaped: </p>
<blockquote>
<pre>.Db on
.Em An escaped \&amp;aC
.Db off</pre>
</blockquote>
<blockquote>
<pre>DEBUGGING ON
DEBUG(fargv) MACRO: `.Em' Line #: 2
 Argc: 1 Argv: `An' Length: 2
 Space: ` ' Class: String
 Argc: 2 Argv: `escaped' Length: 7
 Space: ` ' Class: String
 Argc: 3 Argv: `aC' Length: 2
 Space: ` ' Class: String
 MACRO REQUEST: .Em An escaped &amp;aC
DEBUGGING OFF</pre>
</blockquote>
<p> The argument `\&amp;aC&#8217; shows up with the same length of 2 as the `\&amp;&#8217; sequence produces a zero width, but a register named `\&amp;aC&#8217; was not found and the type classified as string. </p>
<p> Other diagnostics consist of usage statements and are self explanatory.</p>
<h2>Groff, Troff And Nroff</h2>
<p>The <code>-mdoc</code> package does not need compatibility mode with groff. </p>
<p> The package inhibits page breaks, and the headers and footers which normally occur at those breaks with nroff, to make the manual more efficient for viewing on-line. At the moment, groff with &#8211;<code>T </code><i>ascii</i> does eject the imaginary remainder of the page at end of file. The inhibiting of the page breaks makes nroffNs&#8217;d files unsuitable for hardcopy. There is a register named `cR&#8217; which can be set to zero in the site dependent style file /usr/src/share/tmac/doc-nroff to restore the old style behavior.</p>
<h2>Files</h2>
<dl>
<dt><code>/usr/share/tmac/doc.tmac </code></p>
<dd>manual macro package</p>
<dt><code>/usr/share/misc/mdoc.template </code></p>
<dd>template for writing a man page</p>
<dt><code>/usr/share/examples/mdoc/* </code></p>
<dd>several example man pages</dl>
<h2>Bugs</h2>
<p>Undesirable hyphenation on the dash of a flag argument is not yet resolved, and causes occasional mishaps in the Sx DESCRIPTION section. (line break on the hyphen). </p>
<p> Predefined strings are not declared in documentation. </p>
<p> Section 3f has not been added to the header routines. </p>
<p> `.<code>man mdoc.samples</code> &#8216; font should be changed in Sx NAME section. </p>
<p> `.Fn needs &#8216; to have a check to prevent splitting up if the line length is too short. Occasionally it separates the last parenthesis, and sometimes looks ridiculous if a line is in fill mode. </p>
<p> The method used to prevent header and footer page breaks (other than the initial header and footer) when using nroff occasionally places an unsightly partially filled line (blank) at the would be bottom of the page. </p>
<p> The list and display macros to not do any keeps and certainly should be able to.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-man/">man</a>(1), <a href="/docs/linux/man/1-troff/">troff</a>(1), groff_mdoc7, <a href="/docs/linux/man/7-mdoc/">mdoc</a>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 4.15 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
