---
title: "groff(7)"
name: "groff"
section: "7"
letter: "g"
url: "/docs/linux/man/7-groff/"
description: "groff – a short reference for the GNU roff language"
---
<p>groff &#8211; a short reference for the GNU roff language </p>
<h2>DESCRIPTION</h2>
<p>The name <i>groff</i> stands for <i>GNU roff</i> and is the free implementation of the roff type-setting system. See <code><a href="/docs/linux/man/7-roff/">roff</a></code>(7) for a survey and the background of the groff system. </p>
<p>This document provides only short descriptions of roff language elements. <i>Groff: The GNU Implementation of troff</i>, by Trent A. Fisher and Werner Lemberg, is the primary <i>groff</i> manual, and is written in Texinfo. You can browse it interactively with "info groff". </p>
<p>Historically, the <i>roff language</i> was called <i>troff</i>. <i>groff</i> is compatible with the classical system and provides proper extensions. So in GNU, the terms <i>roff</i>, <i>troff</i>, and <i>groff language</i> could be used as synonyms. However <i>troff</i> slightly tends to refer more to the classical aspects, whereas <i>groff</i> emphasizes the GNU extensions, and <i>roff</i> is the general term for the language. </p>
<p>The general syntax for writing groff documents is relatively easy, but writing extensions to the roff language can be a bit harder. </p>
<p>The roff language is line-oriented. There are only two kinds of lines, control lines and text lines. The control lines start with a control character, by default a period or a single quote all other lines are text lines. </p>
<p> <code>Control lines</code> represent commands, optionally with arguments. They have the following syntax. The leading control character can be followed by a command name; arguments, if any, are separated by spaces (but not tab characters) from the command name and among themselves, for example, </p>
<dl>
<dd>  </dd></dl>
<p>For indentation, any number of space or tab characters can be inserted between the leading control character and the command name, but the control character must be on the first position of the line. </p>
<p> <code>Text lines</code> represent the parts that is printed. They can be modified by escape sequences, which are recognized by a leading backslash These are in-line or even in-word formatting elements or functions. Some of these take arguments separated by single quotes others are regulated by a length encoding introduced by an open parenthesis or enclosed in brackets and </p>
<p>The roff language provides flexible instruments for writing language extension, such as macros. When interpreting macro definitions, the roff system enters a special operating mode, called the <code>copy mode</code>. </p>
<p>The copy mode behaviour can be quite tricky, but there are some rules that ensure a safe usage. </p>
<dl>
<dt>1.</dt>
<dd> <p> Printable backslashes must be denoted as <code>\e</code>. To be more precise, <code>\e</code> represents the current escape character. To get a backslash glyph, use <code>\(rs</code> or <code>\[rs]</code>. </p>
 </dd>
<dt>2.</dt>
<dd> <p> Double all backslashes. </p>
 </dd>
<dt>3.</dt>
<dd> <p> Begin all text lines with the special non-spacing character <code>\&amp;</code>. </p>
 </dd></dl>
<p>This does not produce the most efficient code, but it should work as a first measure. For better strategies, see the <i>groff</i> Texinfo manual and <code><a href="/docs/linux/man/5-groff_tmac/">groff_tmac</a></code>(5). </p>
<p>Reading roff source files is easier, just reduce all double backslashes to a single one in all macro definitions.  </p>
<h2>GROFF ELEMENTS</h2>
<p> The roff language elements add formatting information to a text file. The fundamental elements are predefined commands and variables that make roff a full-blown programming language. </p>
<p>There are two kinds of roff commands, possibly with arguments. <code>Requests</code> are written on a line of their own starting with a dot or a whereas <code>Escape sequences</code> are in-line functions and in-word formatting elements starting with a backslash </p>
<p>The user can define her own formatting commands using the <code>de</code> request. These commands are called <code>macros</code>, but they are used exactly like requests. Macro packages are pre-defined sets of macros written in the groff language. A user&#8217;s possibilities to create escape sequences herself is very limited, only special characters can be mapped. </p>
<p>The groff language provides several kinds of variables with different interfaces. There are pre-defined variables, but the user can define her own variables as well. </p>
<p> <code>String</code> variables store character sequences. They are set with the <code>ds</code> request and retrieved by the <code>\*</code> escape sequences. Strings can have variables. </p>
<p> <code>Register</code> variables can store numerical values, numbers with a scale unit, and occasionally string-like objects. They are set with the <code>nr</code> request and retrieved by the <code>\n</code> escape sequences. </p>
<p> <code>Environments</code> allow the user to temporarily store global formatting parameters like line length, font size, etc. for later reuse. This is done by the <code>ev</code> request. </p>
<p> <code>Fonts</code> are identified either by a name or by an internal number. The current font is chosen by the <code>ft</code> request or by the <code>\f</code> escape sequences. Each device has special fonts, but the following fonts are available for all devices. <code>R</code> is the standard font Roman. <code>B</code> is its <code>bold</code> counterpart. The <i>italic</i> font is called <code>I</code> and is available everywhere, but on text devices it is displayed as an underlined Roman font. For the graphical output devices, there exist constant-width pendants of these fonts, <code>CR</code>, <code>CI</code>, and <code>CB</code>. On text devices, all glyphs have a constant width anyway. </p>
<p> <code>Glyphs</code> are visual representation forms of <code>characters</code>. In groff, the distinction between those two elements is not always obvious (and a full discussion is beyond the scope of this man page). A first approximation is that glyphs have a specific size and colour and are taken from a specific font; they can&#8217;t be modified any more - characters are the input, and glyphs are the output. As soon as an output line has been generated, it no longer contains characters but glyphs. In this man page, we use either &#8216;glyph&#8217; or &#8216;character&#8217;, whatever is more appropriate. </p>
<p>Moreover, there are some advanced roff elements. A <code>diversion</code> stores (formatted) information into a macro for later usage. See <code><a href="/docs/linux/man/5-groff_tmac/">groff_tmac</a></code>(5) for more details. A <code>trap</code> is a positional condition like a certain number of lines from page top or in a diversion or in the input. Some action can be prescribed to be run automatically when the condition is met. </p>
<p>More detailed information and examples can be found in the <i>groff</i> Texinfo manual.  </p>
<h2>CONTROL CHARACTERS</h2>
<p> There is a small set of characters that have a special controlling task in certain conditions. </p>
<dl>
<dt>.</dt>
<dd> <p> A dot is only special at the beginning of a line or after the condition in the requests <code>if</code> , <code>ie</code> , <code>el</code> , and <code>while</code> . There it is the control character that introduces a request (or macro). By using the <code>cc</code> request, the control character can be set to a different character, making the dot a non-special character. </p>
 </dd>
<dd> <p> In all other positions, it just means a dot character. In text paragraphs, it is advantageous to start each sentence at a line of its own. </p>
 </dd>
<dt>&#8216;</dt>
<dd> <p> The single quote has two controlling tasks. At the beginning of a line and in the conditional requests it is the non-breaking control character. That means that it introduces a request like the dot, but with the additional property that this request doesn&#8217;t cause a linebreak. By using the <code>c2</code> request, the non-break control character can be set to a different character. </p>
 </dd>
<dd> <p> As a second task, it is the most commonly used argument separator in some functional escape sequences (but any pair of characters not part of the argument do work). In all other positions, it denotes the single quote or apostrophe character. Groff provides a printable representation with the <code>\(cq</code> escape sequence. </p>
 </dd>
<dt>&quot;</dt>
<dd> <p> The double quote is used to enclose arguments in macros (but not in requests and strings). In the <code>ds</code> and <code>as</code> requests, a leading double quote in the argument is stripped off, making everything else afterwards the string to be defined (enabling leading whitespace). The escaped double quote <code>\&quot;</code> introduces a comment. Otherwise, it is not special. Groff provides a printable representation with the <code>\(dq</code> escape sequence. </p>
 </dd>
<dt>\</dt>
<dd> <p> The backslash usually introduces an escape sequence (this can be changed with the <code>ec</code> request). A printed version of the escape character is the <code>\e</code> escape; a backslash glyph can be obtained by <code>\(rs</code>. </p>
 </dd>
<dt>(</dt>
<dd> <p> The open parenthesis is only special in escape sequences when introducing an escape name or argument consisting of exactly two characters. In groff, this behaviour can be replaced by the [] construct. </p>
 </dd>
<dt>[</dt>
<dd> <p> The opening bracket is only special in groff escape sequences; there it is used to introduce a long escape name or long escape argument. Otherwise, it is non-special, e.g. in macro calls. </p>
 </dd>
<dt>]</dt>
<dd> <p> The closing bracket is only special in groff escape sequences; there it terminates a long escape name or long escape argument. Otherwise, it is non-special. </p>
 </dd>
<dt>space</dt>
<dd> <p> Space characters are only functional characters. They separate the arguments in requests, macros, and strings, and the words in text lines. They are subject to groff&#8217;s horizontal spacing calculations. To get a defined space width, escape sequences like (this is the escape character followed by a space), <code>\|</code>, <code>\^</code>, or <code>\h</code> should be used. </p>
 </dd>
<dt>newline</dt>
<dd> <p> In text paragraphs, newlines mostly behave like space characters. Continuation lines can be specified by an escaped newline, i.e., by specifying a backslash as the last character of a line. </p>
 </dd>
<dt>tab</dt>
<dd> <p> If a tab character occurs during text the interpreter makes a horizontal jump to the next pre-defined tab position. There is a sophisticated interface for handling tab positions. </p>
 </dd></dl>
<h2>NUMERICAL EXPRESSIONS</h2>
<p> A <code>numerical value</code> is a signed or unsigned integer or float with or without an appended scaling indicator. A <code>scaling indicator</code> is a one-character abbreviation for a unit of measurement. A number followed by a scaling indicator signifies a size value. By default, numerical values do not have a scaling indicator, i.e., they are normal numbers. </p>
<p>The <i>roff</i> language defines the following scaling indicators. </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>c</code></dt>
<dd> <p> centimeter </p>
 </dd>
<dt><code>i</code></dt>
<dd> <p> inch </p>
 </dd>
<dt><code>P</code></dt>
<dd> <p> pica&nbsp;=&nbsp;1/6 inch </p>
 </dd>
<dt><code>p</code></dt>
<dd> <p> point&nbsp;=&nbsp;1/72 inch </p>
 </dd>
<dt><code>m</code></dt>
<dd> <p> em&nbsp;=&nbsp;the font size in points (approx. width of letter &#8216;m&#8217;) </p>
 </dd>
<dt><code>M</code></dt>
<dd> <p> 100th of an em </p>
 </dd>
<dt><code>n</code></dt>
<dd> <p> en&nbsp;=&nbsp;em/2 </p>
 </dd>
<dt><code>u</code></dt>
<dd> <p> Basic unit for actual output device </p>
 </dd>
<dt><code>v</code></dt>
<dd> <p> Vertical line space in basic units </p>
 </dd>
<dt><code>s</code></dt>
<dd> <p> scaled point&nbsp;=&nbsp;1/sizescale of a point (defined in font DESC file) </p>
 </dd>
<dt><code>f</code></dt>
<dd> <p> Scale by 65536. </p>
 </dd></dl>
</dl>
<p> <code>Numerical expressions</code> are combinations of the numerical values defined above with the following arithmetical operators already defined in classical troff. </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>+</code></dt>
<dd> <p> Addition </p>
 </dd>
<dt><code>-</code></dt>
<dd> <p> Subtraction </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> Multiplication </p>
 </dd>
<dt><code>/</code></dt>
<dd> <p> Division </p>
 </dd>
<dt><code>%</code></dt>
<dd> <p> Modulo </p>
 </dd>
<dt><code>=</code></dt>
<dd> <p> Equals </p>
 </dd>
<dt><code>==</code></dt>
<dd> <p> Equals </p>
 </dd>
<dt><code>&lt;</code></dt>
<dd> <p> Less than </p>
 </dd>
<dt><code>&gt;</code></dt>
<dd> <p> Greater than </p>
 </dd>
<dt><code>&lt;=</code></dt>
<dd> <p> Less or equal </p>
 </dd>
<dt><code>&gt;=</code></dt>
<dd> <p> Greater or equal </p>
 </dd>
<dt><code>&amp;</code></dt>
<dd> <p> Logical and </p>
 </dd>
<dt><code>:</code></dt>
<dd> <p> Logical or </p>
 </dd>
<dt><code>!</code></dt>
<dd> <p> Logical not </p>
 </dd>
<dt><code>(</code></dt>
<dd> <p> Grouping of expressions </p>
 </dd>
<dt><code>)</code></dt>
<dd> <p> Close current grouping </p>
 </dd></dl>
</dl>
<p>Moreover, <i>groff</i> added the following operators for numerical expressions: </p>
<dl>
<dd>  </dd>
<dl>
<dt> e1/&gt;?,e2 </dt>
<dd> <p> The maximum of <i>e1</i> and <i>e2</i>. </p>
 </dd>
<dt> e1/&lt;?,e2 </dt>
<dd> <p> The minimum of <i>e1</i> and <i>e2</i>. </p>
 </dd>
<dt> (,c/;,e/) </dt>
<dd> <p> Evaluate <i>e</i> using <i>c</i> as the default scaling indicator. </p>
 </dd></dl>
</dl>
<p>For details see the <i>groff</i> Texinfo manual.  </p>
<h2>CONDITIONS</h2>
<p> <code>Conditions</code> occur in tests raised by the <code>if</code> , <code>ie</code> , and the <code>while</code> requests. The following table characterizes the different types of conditions. </p>
<dl>
<dd>  </dd>
<dl>
<dt><i>N</i></dt>
<dd> <p> A numerical expression <i>N</i> yields true if its value is greater than~0. </p>
 </dd>
<dt><code>!</code><i>N</i></dt>
<dd> <p> True if the value of <i>N</i> is~0 (see below). </p>
 </dd>
<dt><code>&#8216;</code><i>s1</i><code>&#8216;</code><i>s2</i><code>&#8216;</code></dt>
<dd> <p> True if string~<i>s1</i> is identical to string~<i>s2</i>. </p>
 </dd>
<dt><code>!&#8216;</code><i>s1</i><code>&#8216;</code><i>s2</i><code>&#8216;</code></dt>
<dd> <p> True if string~<i>s1</i> is not identical to string~<i>s2</i> (see below). </p>
 </dd>
<dt><code>c</code><i>ch</i></dt>
<dd> <p> True if there is a glyph~<i>ch</i> available. </p>
 </dd>
<dt><code>d</code><i>name</i></dt>
<dd> <p> True if there is a string, macro, diversion, or request called <i>name</i>. </p>
 </dd>
<dt><code>e</code></dt>
<dd> <p> Current page number is even. </p>
 </dd>
<dt><code>o</code></dt>
<dd> <p> Current page number is odd. </p>
 </dd>
<dt><code>m</code><i>name</i></dt>
<dd> <p> True if there is a color called <i>name</i>. </p>
 </dd>
<dt><code>n</code></dt>
<dd> <p> Formatter is <code>nroff</code>. </p>
 </dd>
<dt><code>r</code><i>reg</i></dt>
<dd> <p> True if there is a register named <i>reg</i>. </p>
 </dd>
<dt><code>t</code></dt>
<dd> <p> Formatter is <code>troff</code>. </p>
 </dd>
<dt><code>F</code><i>font</i></dt>
<dd> <p> True if there exists a font named <i>font</i>. </p>
 </dd>
<dt><code>S</code><i>style</i></dt>
<dd> <p> True if a style named <i>style</i> has been registered. </p>
 </dd></dl>
</dl>
<p>Note that the <code>!</code> operator may only appear at the beginning of an expression, and negates the entire expression. This maintains bug-compatibility with AT&amp;T <i>troff</i>.  </p>
<h2>REQUESTS</h2>
<p> This section provides a short reference for the predefined requests. In groff, request, macro, and string names can be arbitrarily long. No bracketing or marking of long names is needed. </p>
<p>Most requests take one or more arguments. The arguments are separated by space characters (no tabs!); there is no inherent limit for their length or number. </p>
<p>Some requests have optional arguments with a different behaviour. Not all of these details are outlined here. Refer to the <i>groff</i> Texinfo manual and <code><a href="/docs/linux/man/7-groff_diff/">groff_diff</a></code>(7) for all details. </p>
<p>In the following request specifications, most argument names were chosen to be descriptive. Only the following denotations need clarification. </p>
<dl>
<dd>  </dd>
<dl>
<dt><i>c</i></dt>
<dd> <p> denotes a single character. </p>
 </dd>
<dt><i>font</i></dt>
<dd> <p> a font either specified as a font name or a font number. </p>
 </dd>
<dt><i>anything</i></dt>
<dd> <p> all characters up to the end of the line or within <code>\{</code> and <code>\}</code>. </p>
 </dd>
<dt><i>n</i></dt>
<dd> <p> is a numerical expression that evaluates to an integer value. </p>
 </dd>
<dt><i>N</i></dt>
<dd> <p> is an arbitrary numerical expression, signed or unsigned. </p>
 </dd>
<dt><i>&plusmn;N</i></dt>
<dd> <p> has three meanings depending on its sign, described below. </p>
 </dd></dl>
</dl>
<p>If an expression defined as <i>&plusmn;N</i> starts with a sign the resulting value of the expression is added to an already existing value inherent to the related request, e.g. adding to a number register. If the expression starts with a the value of the expression is subtracted from the request value. </p>
<p>Without a sign, <i>N</i> replaces the existing value directly. To assign a negative number either prepend~0 or enclose the negative number in parentheses.  </p>
<h3>Request Short Reference</h3>
<dl>
<dd> <p> Empty line, ignored. Useful for structuring documents. </p>
 </dd>
<dd> <p> Complete line is a comment. </p>
 </dd>
<dd> <p> Print <i>string</i> on standard error, exit program. </p>
 </dd>
<dd> <p> Begin line adjustment for output lines in current adjust mode. </p>
 </dd>
<dd> <p> Start line adjustment in mode <i>c</i> (c/=l,r,c,b,n). </p>
 </dd>
<dd> <p> Assign format <i>c</i> to <i>register</i> (c/=l,i,I,a,A). </p>
 </dd>
<dd> <p> Create alias name for <i>register</i>. </p>
 </dd>
<dd> <p> Create alias name for request, string, macro, or diversion <i>object</i>. </p>
 </dd>
<dd> <p> Append to <i>macro</i> until <code>..</code> is encountered. </p>
 </dd>
<dd> <p> Append to <i>macro</i> until <code>.</code><i>end</i> is called. </p>
 </dd>
<dd> <p> Same as <code>.am</code> but with compatibility mode switched off during macro expansion. </p>
 </dd>
<dd> <p> Same as <code>.am</code> but with compatibility mode switched off during macro expansion. </p>
 </dd>
<dd> <p> Append to a macro whose name is contained in the string register <i>macro</i> until <code>..</code> is encountered. </p>
 </dd>
<dd> <p> Append to a macro indirectly. <i>macro</i> and <i>end</i> are string registers whose contents are interpolated for the macro name and the end macro, respectively. </p>
 </dd>
<dd> <p> Same as <code>.ami</code> but with compatibility mode switched off during macro expansion. </p>
 </dd>
<dd> <p> Same as <code>.ami</code> but with compatibility mode switched off during macro expansion. </p>
 </dd>
<dd> <p> Append <i>anything</i> to <i>stringvar</i>. </p>
 </dd>
<dd> <p> Same as <code>.as</code> but with compatibility mode switched off during string expansion. </p>
 </dd>
<dd> <p> Unformat ASCII characters, spaces, and some escape sequences in <i>diversion</i>. </p>
 </dd>
<dd> <p> Print a backtrace of the input on stderr. </p>
 </dd>
<dd> <p> Embolden <i>font</i> by <i>N</i>-1 units. </p>
 </dd>
<dd> <p> Embolden Special Font <i>S</i> when current font is <i>font</i>. </p>
 </dd>
<dd> <p> Unset the blank line macro. </p>
 </dd>
<dd> <p> Set the blank line macro to <i>macro</i>. </p>
 </dd>
<dd> <p> End current diversion. </p>
 </dd>
<dd> <p> Divert to <i>macro</i>, omitting a partially filled line. </p>
 </dd>
<dd> <p> End current diversion. </p>
 </dd>
<dd> <p> Divert and append to <i>macro</i>, omitting a partially filled line. </p>
 </dd>
<dd> <p> Eject current page and begin new page. </p>
 </dd>
<dd> <p> Eject current page; next page number <i>&plusmn;N</i>. </p>
 </dd>
<dd> <p> Line break. </p>
 </dd>
<dd> <p> Break output line; adjust if applicable. </p>
 </dd>
<dd> <p> Break out of a while loop. </p>
 </dd>
<dd> <p> Reset no-break control character to </p>
 </dd>
<dd> <p> Set no-break control character to <i>c</i>. </p>
 </dd>
<dd> <p> Reset control character to </p>
 </dd>
<dd> <p> Set control character to <i>c</i>. </p>
 </dd>
<dd> <p> Center the next input line. </p>
 </dd>
<dd> <p> Center following <i>N</i> input lines. </p>
 </dd>
<dd> <p> Copy contents of file <i>filename</i> unprocessed to stdout or to the diversion. </p>
 </dd>
<dd> <p> Treat characters <i>c1</i>, <i>c2</i>, ... according to <i>mode</i> number. </p>
 </dd>
<dd> <p> Change <i>trap</i> location to <i>N</i>. </p>
 </dd>
<dd> <p> Define entity <i>c</i> as string <i>anything</i>. </p>
 </dd>
<dd> <p> Chop the last character off macro, string, or diversion <i>object</i>. </p>
 </dd>
<dd> <p> Assign a set of characters, character ranges, or classes <i>c1</i>, <i>c2</i>, ... to <i>name</i>. </p>
 </dd>
<dd> <p> Close the <i>stream</i>. </p>
 </dd>
<dd> <p> Enable colors. </p>
 </dd>
<dd> <p> If <i>N</i> is zero disable colors, otherwise enable them. </p>
 </dd>
<dd> <p> Map glyph name <i>from</i> to glyph name <i>to</i> while constructing a composite glyph name. </p>
 </dd>
<dd> <p> Finish the current iteration of a while loop. </p>
 </dd>
<dd> <p> Enable compatibility mode. </p>
 </dd>
<dd> <p> If <i>N</i> is zero disable compatibility mode, otherwise enable it. </p>
 </dd>
<dd> <p> Set constant character width mode for <i>font</i> to <i>N</i>/36 ems with em <i>M</i>. </p>
 </dd>
<dd> <p> Continuous underline in nroff, like <code>.ul</code> in troff. </p>
 </dd>
<dd> <p> End current diversion. </p>
 </dd>
<dd> <p> Divert and append to <i>macro</i>. </p>
 </dd>
<dd> <p> Define or redefine <i>macro</i> until <code>..</code> is encountered. </p>
 </dd>
<dd> <p> Define or redefine <i>macro</i> until <code>.</code><i>end</i> is called. </p>
 </dd>
<dd> <p> Same as <code>.de</code> but with compatibility mode switched off during macro expansion. </p>
 </dd>
<dd> <p> Same as <code>.de</code> but with compatibility mode switched off during macro expansion. </p>
 </dd>
<dd> <p> Define or redefine a color with name <i>color</i>. <i>scheme</i> can be <code>rgb</code>, <code>cym</code>, <code>cymk</code>, <code>gray</code>, or <code>grey</code>. <i>component</i> can be single components specified as fractions in the range 0 to 1 (default scaling indicator~ as a string of two-digit hexadecimal color components with a leading <code>#</code>, or as a string of four-digit hexadecimal components with two leading <code>#</code>. The color <code>default</code> can&#8217;t be redefined. </p>
 </dd>
<dd> <p> Define or redefine a macro whose name is contained in the string register <i>macro</i> until <code>..</code> is encountered. </p>
 </dd>
<dd> <p> Define or redefine a macro indirectly. <i>macro</i> and <i>end</i> are string registers whose contents are interpolated for the macro name and the end macro, respectively. </p>
 </dd>
<dd> <p> Same as <code>.dei</code> but with compatibility mode switched off during macro expansion. </p>
 </dd>
<dd> <p> Same as <code>.dei</code> but with compatibility mode switched off during macro expansion. </p>
 </dd>
<dd> <p> Write <i>anything</i> to the intermediate output as a device control function. </p>
 </dd>
<dd> <p> Write contents of macro or string <i>name</i> uninterpreted to the intermediate output as a device control function. </p>
 </dd>
<dd> <p> End current diversion. </p>
 </dd>
<dd> <p> Divert to <i>macro</i>. See <code><a href="/docs/linux/man/5-groff_tmac/">groff_tmac</a></code>(5) for more details. </p>
 </dd>
<dd> <p> Interpret <code>.</code><i>name</i> with compatibility mode disabled. </p>
 </dd>
<dd> <p> Set <i>stringvar</i> to <i>anything</i>. </p>
 </dd>
<dd> <p> Same as <code>.ds</code> but with compatibility mode switched off during string expansion. </p>
 </dd>
<dd> <p> Set diversion trap to position <i>N</i> (default scaling indicator~ </p>
 </dd>
<dd> <p> Reset escape character to </p>
 </dd>
<dd> <p> Set escape character to <i>c</i>. </p>
 </dd>
<dd> <p> Restore escape character saved with <code>.ecs</code> . </p>
 </dd>
<dd> <p> Save current escape character. </p>
 </dd>
<dd> <p> Else part for if-else (<code>.ie</code> ) request. </p>
 </dd>
<dd> <p> The <i>macro</i> is run after the end of input. </p>
 </dd>
<dd> <p> Turn off escape character mechanism. </p>
 </dd>
<dd> <p> Switch to previous environment and pop it off the stack. </p>
 </dd>
<dd> <p> Push down environment number or name <i>env</i> to the stack and switch to it. </p>
 </dd>
<dd> <p> Copy the contents of environment <i>env</i> to the current environment. No pushing or popping. </p>
 </dd>
<dd> <p> Exit from roff processing. </p>
 </dd>
<dd> <p> Return to previous font family. </p>
 </dd>
<dd> <p> Set the current font family to <i>name</i>. </p>
 </dd>
<dd> <p> Disable field mechanism. </p>
 </dd>
<dd> <p> Set field delimiter to~<i>a</i> and pad glyph to space. </p>
 </dd>
<dd> <p> Set field delimiter to~<i>a</i> and pad glyph to~<i>b</i>. </p>
 </dd>
<dd> <p> Define fallback character (or glyph) <i>c</i> as string <i>anything</i>. </p>
 </dd>
<dd> <p> Set fill color to previous fill color. </p>
 </dd>
<dd> <p> Set fill color to <i>c</i>. </p>
 </dd>
<dd> <p> Fill output lines. </p>
 </dd>
<dd> <p> Flush output buffer. </p>
 </dd>
<dd> <p> Mount <i>font</i> on position <i>n</i>. </p>
 </dd>
<dd> <p> Mount font with long <i>external</i> name to short <i>internal</i> name on position <i>n</i>. </p>
 </dd>
<dd> <p> Define fallback character (or glyph) <i>c</i> for font <i>f</i> as string <i>anything</i>. </p>
 </dd>
<dd> <p> Reset list of special fonts for <i>font</i> to be empty. </p>
 </dd>
<dd> <p> When the current font is <i>font</i>, then the fonts <i>s1</i>, <i>s2</i>, ... are special. </p>
 </dd>
<dd> <p> Return to previous font. Same as <code>\</code> or <code>\</code> . </p>
 </dd>
<dd> <p> Change to font name or number <i>font</i>; same as escape sequence. </p>
 </dd>
<dd> <p> Translate <i>font1</i> to <i>font2</i>. </p>
 </dd>
<dd> <p> Don&#8217;t magnify <i>font</i>. </p>
 </dd>
<dd> <p> Set zoom factor for <i>font</i> (in multiples of 1/1000th). </p>
 </dd>
<dd> <p> Set glyph color to previous glyph color. </p>
 </dd>
<dd> <p> Set glyph color to <i>c</i>. </p>
 </dd>
<dd> <p> Remove additional hyphenation indicator character. </p>
 </dd>
<dd> <p> Set up additional hyphenation indicator character~<i>c</i>. </p>
 </dd>
<dd> <p> Set the hyphenation code of character <i>c1</i> to <i>code1</i>, that of <i>c2</i> to <i>code2</i>, etc. </p>
 </dd>
<dd> <p> Set the current hyphenation language to <i>lang</i>. </p>
 </dd>
<dd> <p> Set the maximum number of consecutive hyphenated lines to <i>n</i>. </p>
 </dd>
<dd> <p> Read hyphenation patterns from <i>file</i>. </p>
 </dd>
<dd> <p> Append hyphenation patterns from <i>file</i>. </p>
 </dd>
<dd> <p> Set input mapping for <code>.hpf</code> . </p>
 </dd>
<dd> <p> List of <i>words</i> with exceptional hyphenation. </p>
 </dd>
<dd> <p> Switch to hyphenation mode <i>N</i>. </p>
 </dd>
<dd> <p> Set the hyphenation margin to <i>n</i> (default scaling indicator~ </p>
 </dd>
<dd> <p> Set the hyphenation space to <i>n</i>. </p>
 </dd>
<dd> <p> If <i>cond</i> then <i>anything</i> else goto <code>.el</code> . </p>
 </dd>
<dd> <p> If <i>cond</i> then <i>anything</i>; otherwise do nothing. </p>
 </dd>
<dd> <p> Ignore text until <code>..</code> is encountered. </p>
 </dd>
<dd> <p> Ignore text until <code>.</code><i>end</i> is called. </p>
 </dd>
<dd> <p> Change to previous indentation value. </p>
 </dd>
<dd> <p> Change indentation according to <i>&plusmn;N</i> (default scaling indicator~ </p>
 </dd>
<dd> <p> Set an input-line count trap for the next <i>N</i> lines. </p>
 </dd>
<dd> <p> Same as <code>.it</code> but don&#8217;t count lines interrupted with <code>\c</code>. </p>
 </dd>
<dd> <p> Enable pairwise kerning. </p>
 </dd>
<dd> <p> If <i>n</i> is zero, disable pairwise kerning, otherwise enable it. </p>
 </dd>
<dd> <p> Remove leader repetition glyph. </p>
 </dd>
<dd> <p> Set leader repetition glyph to~<i>c</i>. </p>
 </dd>
<dd> <p> Write the length of the string <i>anything</i> to <i>register</i>. </p>
 </dd>
<dd> <p> Enable line-tabs mode (i.e., calculate tab positions relative to output line). </p>
 </dd>
<dd> <p> If <i>n</i> is zero, disable line-tabs mode, otherwise enable it. </p>
 </dd>
<dd> <p> Set input line number to <i>N</i>. </p>
 </dd>
<dd> <p> Set input line number to <i>N</i> and filename to <i>file</i>. </p>
 </dd>
<dd> <p> Ligature mode on if <i>N</i>&gt;0. </p>
 </dd>
<dd> <p> Change to previous line length. </p>
 </dd>
<dd> <p> Set line length according to <i>&plusmn;N</i> (default length default scaling indicator~ </p>
 </dd>
<dd> <p> Unset the leading spaces macro. </p>
 </dd>
<dd> <p> Set the leading spaces macro to <i>macro</i>. </p>
 </dd>
<dd> <p> Change to the previous value of additional intra-line skip. </p>
 </dd>
<dd> <p> Set additional intra-line skip value to <i>N</i>, i.e., <i>N</i>-1 blank lines are inserted after each text output line. </p>
 </dd>
<dd> <p> Length of title (default scaling indicator~ </p>
 </dd>
<dd> <p> Margin glyph off. </p>
 </dd>
<dd> <p> Print glyph~<i>c</i> after each text line at actual distance from right margin. </p>
 </dd>
<dd> <p> Set margin glyph to~<i>c</i> and distance to~<i>N</i> from right margin (default scaling indicator~ </p>
 </dd>
<dd> <p> Mark current vertical position in <i>register</i>, or in an internal register used by <code>.rt</code> if no argument. </p>
 </dd>
<dd> <p> The same as <code>.so</code> except that <i>file</i> is searched in the tmac directories. </p>
 </dd>
<dd> <p> No output-line adjusting. </p>
 </dd>
<dd> <p> Need a one-line vertical space. </p>
 </dd>
<dd> <p> Need <i>N</i> vertical space (default scaling indicator~ </p>
 </dd>
<dd> <p> No filling or adjusting of output lines. </p>
 </dd>
<dd> <p> No hyphenation. </p>
 </dd>
<dd> <p> Number mode off. </p>
 </dd>
<dd> <p> In line number mode, set number, multiple, spacing, and indentation. </p>
 </dd>
<dd> <p> Do not number next line. </p>
 </dd>
<dd> <p> Do not number next <i>N</i> lines. </p>
 </dd>
<dd> <p> Always process <i>anything</i>. </p>
 </dd>
<dd> <p> Define or modify <i>register</i> using <i>&plusmn;N</i> with auto-increment <i>M</i>. </p>
 </dd>
<dd> <p> Make the built-in conditions <code>n</code> true and <code>t</code> false. </p>
 </dd>
<dd> <p> Turn on no-space mode. </p>
 </dd>
<dd> <p> Immediately jump to end of current file. </p>
 </dd>
<dd> <p> Immediately continue processing with file <i>file</i>. </p>
 </dd>
<dd> <p> Open <i>filename</i> for writing and associate the stream named <i>stream</i> with it. </p>
 </dd>
<dd> <p> Like <code>.open</code> but append to it. </p>
 </dd>
<dd> <p> Output vertical distance that was saved by the <code>sv</code> request. </p>
 </dd>
<dd> <p> Emit <i>string</i> directly to intermediate output, allowing leading whitespace if <i>string</i> starts with &quot; (which is stripped off). </p>
 </dd>
<dd> <p> Reset page number character to~ </p>
 </dd>
<dd> <p> Page number character. </p>
 </dd>
<dd> <p> Print the current environment and each defined environment state to stderr. </p>
 </dd>
<dd> <p> Pipe output to <i>program</i> (nroff only). </p>
 </dd>
<dd> <p> Set page length to default The current page length is stored in <code>.p</code> . </p>
 </dd>
<dd> <p> Change page length to <i>&plusmn;N</i> (default scaling indicator~ </p>
 </dd>
<dd> <p> Print macro names and sizes (number of blocks of 128 bytes). </p>
 </dd>
<dd> <p> Print only total of sizes of macros (number of 128 bytes blocks). </p>
 </dd>
<dd> <p> Next page number <i>N</i>. </p>
 </dd>
<dd> <p> Print the names and contents of all currently defined number registers on stderr. </p>
 </dd>
<dd> <p> Change to previous page offset. The current page offset is available in <code>.o</code> . </p>
 </dd>
<dd> <p> Page offset <i>N</i>. </p>
 </dd>
<dd> <p> Return to previous point size. </p>
 </dd>
<dd> <p> Point size; same as </p>
 </dd>
<dd> <p> Get the bounding box of a PostScript image <i>filename</i>. </p>
 </dd>
<dd> <p> This behaves like the <code>so</code> request except that input comes from the standard output of <i>command</i>. </p>
 </dd>
<dd> <p> Print the names and positions of all traps (not including input line traps and diversion traps) on stderr. </p>
 </dd>
<dd> <p> Change to previous post-vertical line spacing. </p>
 </dd>
<dd> <p> Change post-vertical line spacing according to <i>&plusmn;N</i> (default scaling indicator~ </p>
 </dd>
<dd> <p> Remove the definitions of entities <i>c1</i>, <i>c2</i>, ... </p>
 </dd>
<dd> <p> Read insertion. </p>
 </dd>
<dd> <p> Return from a macro. </p>
 </dd>
<dd> <p> Return twice, namely from the macro at the current level and from the macro one level higher. </p>
 </dd>
<dd> <p> Remove the definitions of entities <i>c1</i>, <i>c2</i>, ... for font <i>f</i>. </p>
 </dd>
<dd> <p> Right justify the next <i>n</i> input lines. </p>
 </dd>
<dd> <p> Remove request, macro, diversion, or string <i>name</i>. </p>
 </dd>
<dd> <p> Rename request, macro, diversion, or string <i>old</i> to <i>new</i>. </p>
 </dd>
<dd> <p> Rename register <i>reg1</i> to <i>reg2</i>. </p>
 </dd>
<dd> <p> Remove <i>register</i>. </p>
 </dd>
<dd> <p> Restore spacing; turn no-space mode off. </p>
 </dd>
<dd> <p> Return <i>(upward only)</i> to vertical position marked by <code>.mk</code> on the current page. </p>
 </dd>
<dd> <p> Return <i>(upward only)</i> to specified distance from the top of the page (default scaling indicator~ </p>
 </dd>
<dd> <p> Define global fallback character (or glyph)~<i>c</i> as string <i>anything</i>. </p>
 </dd>
<dd> <p> Reset soft hyphen glyph to <code>\(hy</code>. </p>
 </dd>
<dd> <p> Set the soft hyphen glyph to~<i>c</i>. </p>
 </dd>
<dd> <p> In a macro, shift the arguments by <i>n</i>~positions. </p>
 </dd>
<dd> <p> Set available font sizes similar to the <code>sizes</code> command in a <i>DESC</i> file. </p>
 </dd>
<dd> <p> Include source file. </p>
 </dd>
<dd> <p> Skip one line vertically. </p>
 </dd>
<dd> <p> Space vertical distance <i>N</i> up or down according to sign of <i>N</i> (default scaling indicator~ </p>
 </dd>
<dd> <p> Reset global list of special fonts to be empty. </p>
 </dd>
<dd> <p> Fonts <i>s1</i>, <i>s2</i>, etc. are special and are searched for glyphs not in the current font. </p>
 </dd>
<dd> <p> Toggle the spread warning on and off without changing its value. </p>
 </dd>
<dd> <p> Emit a warning if each space in an output line is widened by <i>limit</i> or more (default scaling indicator~ </p>
 </dd>
<dd> <p> Set space glyph size to <i>N</i>/12 of the space width in the current font. </p>
 </dd>
<dd> <p> Set space glyph size to <i>N</i>/12 and sentence space size set to <i>M</i>/12 of the space width in the current font. </p>
 </dd>
<dd> <p> Associate <i>style</i> with font position <i>n</i>. </p>
 </dd>
<dd> <p> Replace the string named <i>xx</i> with the substring defined by the indices <i>n1</i> and <i>n2</i>. </p>
 </dd>
<dd> <p> Save of vertical space. </p>
 </dd>
<dd> <p> Save the vertical distance <i>N</i> for later output with <code>os</code> request (default scaling indicator~ </p>
 </dd>
<dd> <p> Execute program <i>command-line</i>. </p>
 </dd>
<dd> <p> Set tabs after every position that is a multiple of <i>N</i> (default scaling indicator~ </p>
 </dd>
<dd> <p> Set tabs at positions <i>n1</i>, <i>n2</i>, ..., <i>n</i>n, then set tabs at <i>n</i>n+<i>m</i>mu <i>r</i>n+<i>r1</i> through <i>n</i>n+<i>m</i>mu <i>r</i>n+<i>r</i>n, where <i>m</i> increments from 0, 1, 2, ... to infinity. </p>
 </dd>
<dd> <p> Remove tab repetition glyph. </p>
 </dd>
<dd> <p> Set tab repetition glyph to~<i>c</i>. </p>
 </dd>
<dd> <p> Temporary indent next line (default scaling indicator~ </p>
 </dd>
<dd> <p> Enable track kerning for <i>font</i>. </p>
 </dd>
<dd> <p> Three-part title. </p>
 </dd>
<dd> <p> Print <i>anything</i> on stderr. </p>
 </dd>
<dd> <p> Print <i>anything</i> on stderr, allowing leading whitespace if <i>anything</i> starts with &quot; (which is stripped off). </p>
 </dd>
<dd> <p> Similar to <code>.tm1</code> without emitting a final newline. </p>
 </dd>
<dd> <p> Translate <i>a</i> to <i>b</i>, <i>c</i> to <i>d</i>, etc. on output. </p>
 </dd>
<dd> <p> Transparently output the contents of file <i>filename</i>. </p>
 </dd>
<dd> <p> This is the same as the <code>tr</code> request except that the <code>asciify</code> request uses the character code (if any) before the character translation. </p>
 </dd>
<dd> <p> This is the same as the <code>tr</code> request except that the translations do not apply to text that is transparently throughput into a diversion with <code>\!</code>. </p>
 </dd>
<dd> <p> Make the built-in conditions <code>t</code> true and <code>n</code> false. </p>
 </dd>
<dd> <p> Set underline font to <i>font</i> (to be switched to by <code>.ul</code> ). </p>
 </dd>
<dd> <p> Underline (italicize in troff) <i>N</i> input lines. </p>
 </dd>
<dd> <p> Unformat space characters and tabs in <i>diversion</i>, preserving font information. </p>
 </dd>
<dd> <p> Enable vertical position traps if <i>n</i> is non-zero, disable them otherwise. </p>
 </dd>
<dd> <p> Change to previous vertical base line spacing. </p>
 </dd>
<dd> <p> Set vertical base line spacing to <i>&plusmn;N</i> (default scaling indicator~ </p>
 </dd>
<dd> <p> Set warnings code to <i>n</i>. </p>
 </dd>
<dd> <p> Set scaling indicator used in warnings to <i>si</i>. </p>
 </dd>
<dd> <p> Remove (first) trap at position <i>N</i>. </p>
 </dd>
<dd> <p> Set location trap; negative means from page bottom. </p>
 </dd>
<dd> <p> While condition <i>cond</i> is true, accept <i>anything</i> as input. </p>
 </dd>
<dd> <p> Write <i>anything</i> to the stream named <i>stream</i>. </p>
 </dd>
<dd> <p> Similar to <code>.write</code> without emitting a final newline. </p>
 </dd>
<dd> <p> Write contents of macro or string <i>xx</i> to the stream named <i>stream</i>. </p>
 </dd></dl>
<p>Besides these standard groff requests, there might be further macro calls. They can originate from a macro package (see <code><a href="/docs/linux/man/7-roff/">roff</a></code>(7) for an overview) or from a preprocessor. </p>
<p>Preprocessor macros are easy to recognize. They enclose their code between a pair of characteristic macros. </p>
<p> <center> </p>
<table BORDER>
<tr>
<td><table>
 <tr VALIGN=top>
<td>preprocessor</td>
<td>start macro</td>
<td> end macro
</td>
</tr>
<tr VALIGN=top>
<td><hr />
<hr />
</td>
</tr>
<tr VALIGN=top>
<td>chem</td>
<td>.cstart</td>
<td>.cend
</td>
</tr>
<tr VALIGN=top>
<td>eqn</td>
<td>.EQ</td>
<td>.EN
</td>
</tr>
<tr VALIGN=top>
<td>grap</td>
<td>.G1</td>
<td>.G2
</td>
</tr>
<tr VALIGN=top>
<td>grn</td>
<td>.GS</td>
<td>.GE
</td>
</tr>
<tr VALIGN=top>
<td>ideal</td>
<td>.IS</td>
<td>.IE
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>.IF
</td>
</tr>
<tr VALIGN=top>
<td>pic</td>
<td>.PS</td>
<td>.PE
</td>
</tr>
<tr VALIGN=top>
<td>refer</td>
<td>.R1</td>
<td>.R2
</td>
</tr>
<tr VALIGN=top>
<td>soelim</td>
<td>none</td>
<td>none
</td>
</tr>
<tr VALIGN=top>
<td>tbl</td>
<td>.TS</td>
<td>.TE
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>glilypond</td>
<td>.lilypond start</td>
<td>.lilypond stop
</td>
</tr>
<tr VALIGN=top>
<td>gperl</td>
<td>.Perl start</td>
<td>.Perl stop
</td>
</tr>
<tr VALIGN=top>
<td>gpinyin</td>
<td>.pinyin start</td>
<td>.pinyin stop
</td>
</tr>
</table>
</table>
<p> </center> </p>
<p>Note that the &#8216;ideal&#8217; preprocessor is not available in groff yet.  </p>
<h2>ESCAPE SEQUENCES</h2>
<p> Escape sequences are in-line language elements usually introduced by a backslash and followed by an escape name and sometimes by a required argument. Input processing is continued directly after the escaped character or the argument (without an intervening separation character). So there must be a way to determine the end of the escape name and the end of the argument. </p>
<p>This is done by enclosing names (escape name and arguments consisting of a variable name) by a pair of brackets <code>[</code><i>name</i><code>]</code> and constant arguments (number expressions and characters) by apostrophes (ASCII 0x27) like <code>&#8216;</code><i>constant</i><code>&#8216;</code><i></i>. </p>
<p>There are abbreviations for short names. Two-character escape names can be specified by an opening parenthesis like <code>\(</code>xy or <code>\*(</code>xy without a closing counterpart. And all one-character names different from the special characters and can even be specified without a marker, for example <code>\n</code>c or <code>\$</code>c. </p>
<p>Constant arguments of length~1 can omit the marker apostrophes, too, but there is no two-character analogue. </p>
<p>While one-character escape sequences are mainly used for in-line functions and system-related tasks, the two-letter names following the <code>\(</code> construct are glyphs predefined by the roff system; these are called &#8216;Special Characters&#8217; in the classical documentation. Escapes sequences of the form denote glyphs too.  </p>
<h3>Single-Character Escapes</h3>
<dl>
<dd> <p> Start of a comment. Everything up to the end of the line is ignored. </p>
 </dd>
<dd> <p> Everything up to and including the next newline is ignored. This is interpreted in copy mode. This is like <code>\&quot;</code> except that the terminating newline is ignored as well. </p>
 </dd>
<dd> <p> The string stored in the string variable with one-character name~<i>s</i>. </p>
 </dd>
<dd> <p> The string stored in the string variable with two-character name <i>st</i>. </p>
 </dd>
<dd> <p> The string stored in the string variable with name <i>string</i> (with arbitrary length). </p>
 </dd>
<dd> <p> The string stored in the string variable with arbitrarily long name <i>stringvar</i>, taking <i>arg1</i>, <i>arg2</i>, ... as arguments. </p>
 </dd>
<dd> <p> The name by which the current macro was invoked. The <code>als</code> request can make a macro have more than one name. </p>
 </dd>
<dd> <p> Macro or string argument with one-digit number~<i>x</i> in the range 1 to~9. </p>
 </dd>
<dd> <p> Macro or string argument with two-digit number <i>xy</i> (larger than zero). </p>
 </dd>
<dd> <p> Macro or string argument with number <i>nexp</i>, where <i>nexp</i> is a numerical expression evaluating to an integer &ge;1. </p>
 </dd>
<dd> <p> In a macro or string, the concatenation of all the arguments separated by spaces. </p>
 </dd>
<dd> <p> In a macro or string, the concatenation of all the arguments with each surrounded by double quotes, and separated by spaces. </p>
 </dd>
<dd> <p> In a macro, the representation of all parameters as if they were an argument to the <code>ds</code> request. </p>
 </dd>
<dd> <p> reduces to a single backslash; useful to delay its interpretation as escape character in copy mode. For a printable backslash, use <code>\e</code>, or even better <code>\[rs]</code>, to be independent from the current escape character. </p>
 </dd>
<dd> <p> The acute accent &acute;; same as <code>\(aa</code>. Unescaped: apostrophe, right quotation mark, single quote (ASCII 0x27). </p>
 </dd>
<dd> <p> The grave accent `; same as <code>\(ga</code>. Unescaped: left quote, backquote (ASCII 0x60). </p>
 </dd>
<dd> <p> The - (minus) sign in the current font. </p>
 </dd>
<dd> <p> The same as <code>\(ul</code>, the underline character. </p>
 </dd>
<dd> <p> The same as a dot (&#8216;.&#8216;). Necessary in nested macro definitions so that &#8216;\\..&#8216; expands to &#8216;..&#8216;. </p>
 </dd>
<dd> <p> Default optional hyphenation character. </p>
 </dd>
<dd> <p> Transparent line indicator. </p>
 </dd>
<dd> <p> In a diversion, this transparently embeds <i>anything</i> in the diversion. <i>anything</i> is read in copy mode. See also the escape sequences <code>\!</code> and <code>\?</code>. </p>
 </dd>
<dd> <p> Unpaddable space size space glyph (no line break). </p>
 </dd>
<dd> <p> Digit-width space. </p>
 </dd>
<dd> <p> 1/6 em narrow space glyph; zero width in nroff. </p>
 </dd>
<dd> <p> 1/12 em half-narrow space glyph; zero width in nroff. </p>
 </dd>
<dd> <p> Non-printable, zero-width glyph. </p>
 </dd>
<dd> <p> Like <code>\&amp;</code> except that it behaves like a glyph declared with the <code>cflags</code> request to be transparent for the purposes of end-of-sentence recognition. </p>
 </dd>
<dd> <p> Increases the width of the preceding glyph so that the spacing between that glyph and the following glyph is correct if the following glyph is a roman glyph. </p>
 </dd>
<dd> <p> Modifies the spacing of the following glyph so that the spacing between that glyph and the preceding glyph is correct if the preceding glyph is a roman glyph. </p>
 </dd>
<dd> <p> Unbreakable space that stretches like a normal inter-word space when a line is adjusted. </p>
 </dd>
<dd> <p> Inserts a zero-width break point (similar to <code>\%</code> but without a soft hyphen character). </p>
 </dd>
<dd> <p> Ignored newline, for continuation lines. </p>
 </dd>
<dd> <p> Begin conditional input. </p>
 </dd>
<dd> <p> End conditional input. </p>
 </dd>
<dd> <p> A glyph with two-character name <i>sc</i>; see section "Special Characters" below. </p>
 </dd>
<dd> <p> A glyph with name <i>name</i> (of arbitrary length). </p>
 </dd>
<dd> <p> A composite glyph with components <i>comp1</i>, <i>comp2</i>, ... </p>
 </dd>
<dd> <p> Non-interpreted leader character. </p>
 </dd>
<dd> <p> If <i>anything</i> is acceptable as a name of a string, macro, diversion, register, environment or font it expands to~1, and to~0 otherwise. </p>
 </dd>
<dd> <p> Bracket building function. </p>
 </dd>
<dd> <p> If <i>anything</i> is acceptable as a valid numeric expression it expands to~1, and to~0 otherwise. </p>
 </dd>
<dd> <p> Continue output line at next input line. Anything after this escape on the same line is ignored except (which works as usual). Anything before on the same line is appended to the current partial output line. The next non-command line after a line interrupted with counts as a new input line. </p>
 </dd>
<dd> <p> The glyph called <i>glyph</i>; same as but compatible to other roff versions. </p>
 </dd>
<dd> <p> Forward (down) 1/2 em (1/2 line in nroff). </p>
 </dd>
<dd> <p> Draw a graphical element defined by the characters in <i>charseq</i>; see the <i>groff</i> Texinfo manual for details. </p>
 </dd>
<dd> <p> Printable version of the current escape character. </p>
 </dd>
<dd> <p> Equivalent to an escape character, but is not interpreted in copy mode. </p>
 </dd>
<dd> <p> Change to font with one-character name or one-digit number~<i>F</i>. </p>
 </dd>
<dd> <p> Switch back to previous font. </p>
 </dd>
<dd> <p> Change to font with two-character name or two-digit number <i>fo</i>. </p>
 </dd>
<dd> <p> Change to font with arbitrarily long name or number expression <i>font</i>. </p>
 </dd>
<dd> <p> Switch back to previous font. </p>
 </dd>
<dd> <p> Change to font family with one-character name~<i>f</i>. </p>
 </dd>
<dd> <p> Change to font family with two-character name <i>fm</i>. </p>
 </dd>
<dd> <p> Change to font family with arbitrarily long name <i>fam</i>. </p>
 </dd>
<dd> <p> Switch back to previous font family. </p>
 </dd>
<dd> <p> Return format of register with one-character name~<i>r</i> suitable for <code>af</code> request. </p>
 </dd>
<dd> <p> Return format of register with two-character name <i>rg</i> suitable for <code>af</code> request. </p>
 </dd>
<dd> <p> Return format of register with arbitrarily long name <i>reg</i> suitable for <code>af</code> request. </p>
 </dd>
<dd> <p> Local horizontal motion; move right <i>N</i> (left if negative). </p>
 </dd>
<dd> <p> Set height of current font to <i>N</i>. </p>
 </dd>
<dd> <p> Mark horizontal input place in one-character register~<i>r</i>. </p>
 </dd>
<dd> <p> Mark horizontal input place in two-character register <i>rg</i>. </p>
 </dd>
<dd> <p> Mark horizontal input place in register with arbitrarily long name <i>reg</i>. </p>
 </dd>
<dd> <p> Horizontal line drawing function (optionally using character <i>c</i>). </p>
 </dd>
<dd> <p> Vertical line drawing function (optionally using character <i>c</i>). </p>
 </dd>
<dd> <p> Change to color with one-character name~<i>c</i>. </p>
 </dd>
<dd> <p> Change to color with two-character name <i>cl</i>. </p>
 </dd>
<dd> <p> Change to color with arbitrarily long name <i>color</i>. </p>
 </dd>
<dd> <p> Switch back to previous color. </p>
 </dd>
<dd> <p> Change filling color for closed drawn objects to color with one-character name~<i>c</i>. </p>
 </dd>
<dd> <p> Change filling color for closed drawn objects to color with two-character name <i>cl</i>. </p>
 </dd>
<dd> <p> Change filling color for closed drawn objects to color with arbitrarily long name <i>color</i>. </p>
 </dd>
<dd> <p> Switch to previous fill color. </p>
 </dd>
<dd> <p> The numerical value stored in the register variable with the one-character name~<i>r</i>. </p>
 </dd>
<dd> <p> The numerical value stored in the register variable with the two-character name <i>re</i>. </p>
 </dd>
<dd> <p> The numerical value stored in the register variable with arbitrarily long name <i>reg</i>. </p>
 </dd>
<dd> <p> Typeset the glyph with index~<i>n</i> in the current font. No special fonts are searched. Useful for adding (named) entities to a document using the <code>char</code> request and friends. </p>
 </dd>
<dd> <p> Overstrike glyphs <i>a</i>, <i>b</i>, <i>c</i>, etc. </p>
 </dd>
<dd> <p> Disable glyph output. Mainly for internal use. </p>
 </dd>
<dd> <p> Enable glyph output. Mainly for internal use. </p>
 </dd>
<dd> <p> Break output line at next word boundary; adjust if applicable. </p>
 </dd>
<dd> <p> Reverse 1 em vertical motion (reverse line in nroff). </p>
 </dd>
<dd> <p> The same as <code>.nr</code> <i>name</i> <i>&plusmn;n</i>. </p>
 </dd>
<dd> <p> Set/increase/decrease the point size to/by <i>N</i> scaled points; <i>N</i> is a one-digit number in the range 1 to~9. Same as <code>ps</code> request. </p>
 </dd>
<dd> <p> Set/increase/decrease the point size to/by <i>N</i> scaled points; <i>N</i> is a two-digit number &ge;1. Same as <code>ps</code> request. </p>
 </dd>
<dd> <p> Set/increase/decrease the point size to/by <i>N</i> scaled points. Same as <code>ps</code> request. </p>
 </dd>
<dd> <p> Slant output by <i>N</i> degrees. </p>
 </dd>
<dd> <p> Non-interpreted horizontal tab. </p>
 </dd>
<dd> <p> Reverse (up) 1/2 em vertical motion (1/2 line in nroff). </p>
 </dd>
<dd> <p> Local vertical motion; move down <i>N</i> (up if negative). </p>
 </dd>
<dd> <p> The contents of the environment variable with one-character name~<i>e</i>. </p>
 </dd>
<dd> <p> The contents of the environment variable with two-character name <i>ev</i>. </p>
 </dd>
<dd> <p> The contents of the environment variable with arbitrarily long name <i>env</i>. </p>
 </dd>
<dd> <p> The width of the glyph sequence <i>string</i>. </p>
 </dd>
<dd> <p> Extra line-space function (negative before, positive after). </p>
 </dd>
<dd> <p> Output <i>string</i> as device control function. </p>
 </dd>
<dd> <p> Output string variable or macro with one-character name~<i>n</i> uninterpreted as device control function. </p>
 </dd>
<dd> <p> Output string variable or macro with two-character name <i>nm</i> uninterpreted as device control function. </p>
 </dd>
<dd> <p> Output string variable or macro with arbitrarily long name <i>name</i> uninterpreted as device control function. </p>
 </dd>
<dd> <p> Print <i>c</i> with zero width (without spacing). </p>
 </dd>
<dd> <p> Print <i>anything</i> and then restore the horizontal and vertical position; <i>anything</i> may not contain tabs or leaders. </p>
 </dd></dl>
<p>The escape sequences <code>\e</code>, <code>\.</code>, <code>\&quot;</code>, <code>\$</code>, <code>\*</code>, <code>\a</code>, <code>\n</code>, <code>\t</code>, <code>\g</code>, and are interpreted in copy mode. </p>
<p>Escape sequences starting with <code>\(</code> or <code>\[</code> do not represent single character escape sequences, but introduce escape names with two or more characters. </p>
<p>If a backslash is followed by a character that does not constitute a defined escape sequence, the backslash is silently ignored and the character maps to itself.  </p>
<h3>Special Characters</h3>
<p> [Note: &#8216;Special Characters&#8217; is a misnomer; those entities are (output) glyphs, not (input) characters.] </p>
<p>Common special characters are predefined by escape sequences of the form <code>\(</code><i>xy</i> with characters <i>x</i> and <i>y</i>. In <i>groff</i>, it is also possible to use the writing <code>\[</code><i>xy</i><code>]</code> as well. </p>
<p>Some of these special characters exist in the usual font while most of them are only available in the special font. Below you can see a small selection of the most important glyphs; a complete list can be found in <code><a href="/docs/linux/man/7-groff_char/">groff_char</a></code>(7). </p>
<dl>
<dd>  </dd>
<dl>
<dd> <p> Dollar <code>$</code> </p>
 </dd>
<dd> <p> Euro <code>&euro;</code> </p>
 </dd>
<dd> <p> British pound sterling <code>&pound;</code> </p>
 </dd>
<dd> <p> Apostrophe quote <code>&#8216;</code> </p>
 </dd>
<dd> <p> Bullet sign <code>&bull;</code> </p>
 </dd>
<dd> <p> Copyright <code>&#169;</code> </p>
 </dd>
<dd> <p> Single closing quote (right) <code>&#8216;</code> </p>
 </dd>
<dd> <p> Cent <code>&#162;</code> </p>
 </dd>
<dd> <p> Double dagger <code>=</code> </p>
 </dd>
<dd> <p> Degree <code>&#176;</code> </p>
 </dd>
<dd> <p> Dagger <code>-</code> </p>
 </dd>
<dd> <p> Double quote (ASCII 34) <code>&quot;</code> </p>
 </dd>
<dd> <p> Em-dash <code>---</code> </p>
 </dd>
<dd> <p> En-dash <code>-</code> </p>
 </dd>
<dd> <p> Hyphen <code>-</code> </p>
 </dd>
<dd> <p> Double quote left <code>"</code> </p>
 </dd>
<dd> <p> Single opening quote (left) <code>&#8216;</code> </p>
 </dd>
<dd> <p> Registered sign <code>&#174;</code> </p>
 </dd>
<dd> <p> Double quote right <code>"</code> </p>
 </dd>
<dd> <p> Printable backslash character <code>\</code> </p>
 </dd>
<dd> <p> Section sign <code>&#167;</code> </p>
 </dd>
<dd> <p> Trademark symbol <code>&trade;</code> </p>
 </dd>
<dd> <p> Underline character <code>_</code> </p>
 </dd>
<dd> <p> Identical <code>&equiv;</code> </p>
 </dd>
<dd> <p> Larger or equal <code>&ge;</code> </p>
 </dd>
<dd> <p> Less or equal <code>&le;</code> </p>
 </dd>
<dd> <p> Not equal <code>&ne;</code> </p>
 </dd>
<dd> <p> Right arrow <code>&rarr;</code> </p>
 </dd>
<dd> <p> Left arrow <code>&larr;</code> </p>
 </dd>
<dd> <p> Plus-minus sign <code>&plusmn;</code> </p>
 </dd></dl>
</dl>
<h3>Unicode Characters</h3>
<p> The extended escape <code>u</code> allows the inclusion of all available Unicode characters into a <i>roff</i> file. </p>
<dl>
<dt><code>\[u</code><i>xxxx</i><code>]</code></dt>
<dd> <p> <code>u</code> is the escape name. <i>xxxx</i> is a hexadecimal number of four hex digits, such as <code>0041</code> for the letter <code>A</code>, thus <code>\[u0041]</code>. </p>
 </dd>
<dt><code>\[u</code><i>yyyyy</i><code>]</code></dt>
<dd> <p> <code>u</code> is the escape name. <i>yyyyy</i> is a hexadecimal number of five hex digits, such as <code>2FA1A</code> for a Chinese-looking character from the Unicode block <i>CJK Compatibility Ideographs Supplement</i>, thus <code>\[u2FA1A]</code>. </p>
 </dd></dl>
<p>The hexadecimal value indicates the corresponding Unicode code point for a character. </p>
<dl>
<dt><code>\[u</code><i>hex1</i><code>_</code><i>hex2</i><code>]</code></dt>
<dd> <p> <code>\[u</code><i>hex1</i><code>_</code><i>hex2</i><code>_</code><i>hex3</i><code>]</code> <i>hex1</i>, <i>hex2</i>, and <i>hex3</i> are all Unicode hexadecimal codes (4 or 5 hex digits) that are used for overstriking, e.g. <code>\[u0041_0301]</code> is <i>A acute</i>, which can also be specified as <code>&Aacute;</code>; see <code><a href="/docs/linux/man/7-groff_char/">groff_char</a></code>(7). </p>
 </dd></dl>
<p>The availability of the Unicode characters depends on the font used. For text mode, the device <code>-Tutf8</code> is quite complete; for <i>troff</i> modes it might happen that some or many characters will not be displayed. Please check your fonts.  </p>
<h3>Strings</h3>
<p> Strings are defined by the <code>ds</code> request and can be retrieved by the <code>\*</code> escape sequence. </p>
<p>Strings share their name space with macros. So strings and macros without arguments are roughly equivalent; it is possible to call a string like a macro and vice versa, but this often leads to unpredictable results. The following string is the only one predefined in groff. </p>
<dl>
<dd> <p> The name of the current output device as specified by the command-line option. </p>
 </dd></dl>
<h2>REGISTERS</h2>
<p> Registers are variables that store a value. In groff, most registers store numerical values (see section "Numerical Expressions" above), but some can also hold a string value. </p>
<p>Each register is given a name. Arbitrary registers can be defined and set with the <code>nr</code> request. </p>
<p>The value stored in a register can be retrieved by the escape sequences introduced by <code>\n</code>. </p>
<p>Most useful are predefined registers. In the following the notation <i>name</i> is used to refer to <code>name</code> to make clear that we speak about registers. Please keep in mind that the decoration is not part of the register name.  </p>
<h3>Read-only Registers</h3>
<p> The following registers have predefined values that should not be modified by the user (usually, registers starting with a dot are read-only). Mostly, they provide information on the current settings or store results from request calls. </p>
<dl>
<dd> <p> The process ID of <code>troff</code>. </p>
 </dd>
<dd> <p> Number of arguments in the current macro or string. </p>
 </dd>
<dd> <p> Post-line extra line-space most recently utilized using <code>\x</code>. </p>
 </dd>
<dd> <p> Set to~1 in <code>troff</code> if option is used; always~1 in <code>nroff</code>. </p>
 </dd>
<dd> <p> The emboldening offset while <code>.bd</code> is active. </p>
 </dd>
<dd> <p> Within a macro, set to~1 if macro called with the &#8216;normal&#8217; control character, and to~0 otherwise. </p>
 </dd>
<dd> <p> Current input line number. </p>
 </dd>
<dd> <p> 1~if compatibility mode is in effect, 0~otherwise. </p>
 </dd>
<dd> <p> The depth of the last glyph added to the current environment. It is positive if the glyph extends below the baseline. </p>
 </dd>
<dd> <p> The number of lines remaining to be centered, as set by the <code>ce</code> request. </p>
 </dd>
<dd> <p> The height of the last glyph added to the current environment. It is positive if the glyph extends above the baseline. </p>
 </dd>
<dd> <p> 1~if colors are enabled, 0~otherwise. </p>
 </dd>
<dd> <p> The skew of the last glyph added to the current environment. The skew of a glyph is how far to the right of the center of a glyph the center of an accent over that glyph should be placed. </p>
 </dd>
<dd> <p> Current vertical place in current diversion; equal to <code>nl</code> . </p>
 </dd>
<dd> <p> The name or number of the current environment (string-valued). </p>
 </dd>
<dd> <p> Current font number. </p>
 </dd>
<dd> <p> The name of the current input file (string-valued). </p>
 </dd>
<dd> <p> The current font family (string-valued). </p>
 </dd>
<dd> <p> The current (internal) real font name (string-valued). </p>
 </dd>
<dd> <p> The number of the next free font position. </p>
 </dd>
<dd> <p> Always 1 in GNU troff. Macros should use it to test if running under groff. </p>
 </dd>
<dd> <p> Text base-line high-water mark on current page or diversion. </p>
 </dd>
<dd> <p> Number of basic units per horizontal unit of output device resolution. </p>
 </dd>
<dd> <p> The current font height as set with <code>\H</code> . </p>
 </dd>
<dd> <p> The current hyphenation language as set by the <code>hla</code> request. </p>
 </dd>
<dd> <p> The number of immediately preceding consecutive hyphenated lines. </p>
 </dd>
<dd> <p> The maximum allowed number of consecutive hyphenated lines, as set by the <code>hlm</code> request. </p>
 </dd>
<dd> <p> The current hyphenation flags (as set by the <code>hy</code> request). </p>
 </dd>
<dd> <p> The current hyphenation margin (as set by the <code>hym</code> request). </p>
 </dd>
<dd> <p> The current hyphenation space (as set by the <code>hys</code> request). </p>
 </dd>
<dd> <p> Current indentation. </p>
 </dd>
<dd> <p> The indentation that applies to the current output line. </p>
 </dd>
<dd> <p> Positive if last output line contains <code>\c</code>. </p>
 </dd>
<dd> <p> The current adjustment mode. It can be stored and used to set adjustment. (n&nbsp;=&nbsp;1, b&nbsp;=&nbsp;1, l&nbsp;=&nbsp;0, r&nbsp;=&nbsp;5, c&nbsp;=&nbsp;3). </p>
 </dd>
<dd> <p> The current horizontal output position (relative to the current indentation). </p>
 </dd>
<dd> <p> 1~if pairwise kerning is enabled, 0~otherwise. </p>
 </dd>
<dd> <p> Current line length. </p>
 </dd>
<dd> <p> The current line spacing setting as set by <code>.ls</code> . </p>
 </dd>
<dd> <p> The current ligature mode (as set by the <code>lg</code> request). </p>
 </dd>
<dd> <p> The current line-tabs mode (as set by the <code>linetabs</code> request). </p>
 </dd>
<dd> <p> The line length that applies to the current output line. </p>
 </dd>
<dd> <p> The title length (as set by the <code>lt</code> request). </p>
 </dd>
<dd> <p> The current drawing color (string-valued). </p>
 </dd>
<dd> <p> The current background color (string-valued). </p>
 </dd>
<dd> <p> Length of text portion on previous output line. </p>
 </dd>
<dd> <p> The amount of space that was needed in the last <code>ne</code> request that caused a trap to be sprung. Useful in conjunction with <code>.trunc</code> . </p>
 </dd>
<dd> <p> 1~if in no-space mode, 0~otherwise. </p>
 </dd>
<dd> <p> Current page offset. </p>
 </dd>
<dd> <p> The suppression nesting level (see <code>\O</code>). </p>
 </dd>
<dd> <p> Current page length. </p>
 </dd>
<dd> <p> 1~if the current page is being printed, 0~otherwise (as determined by the command-line option). </p>
 </dd>
<dd> <p> 1~during page ejection, 0~otherwise. </p>
 </dd>
<dd> <p> The number of the next page: either the value set by a <code>pn</code> request, or the number of the current page plus 1. </p>
 </dd>
<dd> <p> The current point size in scaled points. </p>
 </dd>
<dd> <p> The last-requested point size in scaled points. </p>
 </dd>
<dd> <p> The current post-vertical line spacing. </p>
 </dd>
<dd> <p> The number of unused number registers. Always 10000 in GNU troff. </p>
 </dd>
<dd> <p> The number of lines to be right-justified as set by the <code>rj</code> request. </p>
 </dd>
<dd> <p> Current point size as a decimal fraction. </p>
 </dd>
<dd> <p> The slant of the current font as set with <code>\S</code> . </p>
 </dd>
<dd> <p> The last requested point size in points as a decimal fraction (string-valued). </p>
 </dd>
<dd> <p> The value of the parameters set by the first argument of the <code>ss</code> request. </p>
 </dd>
<dd> <p> The value of the parameters set by the second argument of the <code>ss</code> request. </p>
 </dd>
<dd> <p> The current font style (string-valued). </p>
 </dd>
<dd> <p> Vertical distance to the next trap. </p>
 </dd>
<dd> <p> Set to~1 if option is used. </p>
 </dd>
<dd> <p> A string representation of the current tab settings suitable for use as an argument to the <code>ta</code> request. </p>
 </dd>
<dd> <p> The amount of vertical space truncated by the most recently sprung vertical position trap, or, if the trap was sprung by an <code>ne</code> request, minus the amount of vertical motion produced by <code>.ne</code> . Useful in conjunction with the <code>.ne</code> . </p>
 </dd>
<dd> <p> Equal to 1 in fill mode and 0 in no-fill mode. </p>
 </dd>
<dd> <p> Equal to 1 in safer mode and 0 in unsafe mode. </p>
 </dd>
<dd> <p> Current vertical line spacing. </p>
 </dd>
<dd> <p> Number of basic units per vertical unit of output device resolution. </p>
 </dd>
<dd> <p> 1~if vertical position traps are enabled, 0~otherwise. </p>
 </dd>
<dd> <p> Width of previous glyph. </p>
 </dd>
<dd> <p> The sum of the number codes of the currently enabled warnings. </p>
 </dd>
<dd> <p> The major version number. </p>
 </dd>
<dd> <p> The minor version number. </p>
 </dd>
<dd> <p> The revision number of groff. </p>
 </dd>
<dd> <p> Name of current diversion. </p>
 </dd>
<dd> <p> Zoom factor for current font (in multiples of 1/1000th; zero if no magnification). </p>
 </dd></dl>
<h3>Writable Registers</h3>
<p> The following registers can be read and written by the user. They have predefined default values, but these can be modified for customizing a document. </p>
<dl>
<dd> <p> Current page number. </p>
 </dd>
<dt> Current input line number. </dt>
<dt> Character type (set by width function <code>\w</code>). </dt>
<dt> Maximal width of last completed diversion. </dt>
<dt> Height of last completed diversion. </dt>
<dt> Current day of week (1-7). </dt>
<dt> Current day of month (1-31). </dt>
<dt> The number of hours past midnight. Initialized at start-up. </dt>
<dt> Current horizontal position at input line. </dt>
<dt> Lower left x-coordinate (in PostScript units) of a given PostScript image (set by <code>.psbb</code> ). </dt>
<dt> Lower left y-coordinate (in PostScript units) of a given PostScript image (set by <code>.psbb</code> ). </dt>
<dt> Output line number. </dt>
<dt> The number of leading spaces of an input line. </dt>
<dt> The horizontal space corresponding to the leading spaces of an input line. </dt>
<dt> The number of minutes after the hour. Initialized at start-up. </dt>
<dt> Current month (1-12). </dt>
<dt> Vertical position of last printed text base-line. </dt>
<dt> These four registers mark the top left and bottom right hand corners of a box which encompasses all written glyphs. They are reset to -1 by or </dt>
<dt> Like <code>sb</code> , but takes account of the heights and depths of glyphs. </dt>
<dt> Like <code>st</code> , but takes account of the heights and depths of glyphs. </dt>
<dt> Depth of string below base line (generated by width function <code>\w</code>). </dt>
<dt> The number of seconds after the minute. Initialized at start-up. </dt>
<dt> Right skip width from the center of the last glyph in the <code>\w</code> argument. </dt>
<dt> If greater than 0, the maximum number of objects on the input stack. If &le;0 there is no limit, i.e., recursion can continue until virtual memory is exhausted. </dt>
<dt> The amount of horizontal space (possibly negative) that should be added to the last glyph before a subscript (generated by width function <code>\w</code>). </dt>
<dt> Height of string above base line (generated by width function <code>\w</code>). </dt>
<dt> The return value of the <i>system()</i> function executed by the last <code>sy</code> request. </dt>
<dt> Upper right x-coordinate (in PostScript units) of a given PostScript image (set by <code>.psbb</code> ). </dt>
<dt> Upper right y-coordinate (in PostScript units) of a given PostScript image (set by <code>.psbb</code> ). </dt>
<dt> The current year (year 2000 compliant). </dt>
<dt> Current year minus 1900. For Y2K compliance use <code>year</code> instead. </dt>
</dl>
<h2>HYPHENATION</h2>
<p> The request, given an integer argument, controls when hyphenation applies. The default value is <code>1</code>, which enables hyphenation almost everywhere (see below). Macro packages often override this default. </p>
<dl>
<dt><code>1</code></dt>
<dd> <p> disables hyphenation only after the first and before the last character of a word. </p>
 </dd>
<dt><code>2</code></dt>
<dd> <p> disables hyphenation only of the last word on a page or column. </p>
 </dd>
<dt><code>4</code></dt>
<dd> <p> disables hyphenation only before the last two characters of a word. </p>
 </dd>
<dt><code>8</code></dt>
<dd> <p> disables hyphenation only after the first two characters of a word. </p>
 </dd>
<dt><code>16</code></dt>
<dd> <p> enables hyphenation before the last character of a word. </p>
 </dd>
<dt><code>32</code></dt>
<dd> <p> enables hyphenation after the first character of a word. </p>
 </dd></dl>
<p>The values are additive. Some values cannot be used together because they contradict; for instance, 4 and~16; 8 and~32.  </p>
<h2>UNDERLINING</h2>
<p> In the <i>RUNOFF</i> language, the underlining was quite easy. But in <i>roff</i> this is much more difficult.  </p>
<h3>Underlining with .ul</h3>
<p> There exists a <i>groff</i> request <code>.ul</code> (see above) that can underline the next or further source lines in <code>nroff</code>, but in <code>troff</code> it produces only a font change into <i>italic</i>. So this request is not really useful.  </p>
<h3>Underlining with .UL from ms</h3>
<p> In the &#8216;ms&#8217; macro package in tmac/s.tmac <code><a href="/docs/linux/man/7-groff_ms/">groff_ms</a></code>(7), there is the macro <code>.UL</code>. But this works only in <code>troff</code>, not in <code>nroff</code>.  </p>
<h3>Underlining macro definitions</h3>
<p> So one can use the <i>italic</i> <code>nroff</code> idea from <code>.ul</code> and the <code>troff</code> definition in <i>ms</i> for writing a useful new macro, something like </p>
<dl>
<dd> <p> .de UNDERLINE . ie n \\$1\f[I]\\$2\f[P]\\$3 . el \\$1\Z&#8217;\\$2&#8217;\v&#8217;.25m&#8217;\D&#8217;l \w&#8217;\\$2&#8217;u 0&#8217;\v&#8217;-.25m&#8217;\\$3 .. </p>
 </dd></dl>
<p> If <code>doclifter</code>(1) makes trouble, change the macro name <code>UNDERLINE</code> into some 2-letter word, like <code>Ul</code>. Moreover change the font writing from <code>\f[P]</code> to <code>\fP</code>.  </p>
<h3>Underlining without macro definitions</h3>
<p> If one does not want to use macro definitions, e.g., when <code>doclifter</code> gets lost, use the following: </p>
<dl>
<dd> <p> .ds u1 before .ds u2 in .ds u3 after .ie n \*[u1]\f[I]\*[u2]\f[P]\*[u3] .el \*[u1]\Z&#8217;\*[u2]&#8216;\v&#8217;.25m&#8217;\D&#8217;l \w&#8217;\*[u2]&#8216;u 0&#8217;\v&#8217;-.25m&#8217;\*[u3] </p>
 </dd></dl>
<p> Due to <code>doclifter</code>, it might be necessary to change the variable writing <code>\[xy]</code> and <code>\*[xy]</code> into the strange ancient writing <code>\*(xy</code> and <code>\(xy</code>, and so on. </p>
<p>Then these lines could look like </p>
<dl>
<dd> <p> .ds u1 before .ds u2 in .ds u3 after .ie n \*[u1]\fI\*(u2\fP\*(u3 .el \*(u1\Z&#8217;\*(u2&#8217;\v&#8217;.25m&#8217;\D&#8217;l \w&#8217;\*(u2&#8217;u 0&#8217;\v&#8217;-.25m&#8217;\*(u3 </p>
 </dd></dl>
<p>The result looks like </p>
<dl>
<dd> <p> before _i_n after </p>
 </dd></dl>
<h3>Underlining with Overstriking \z and \(ul</h3>
<p> There is another possibility for underlining by using overstriking with <code>\z</code><i>c</i> (print <i>c</i> with zero width without spacing) and <code>\(ul</code> (underline character). This produces the underlining of 1 character, both in <code>nroff</code> and in <code>troff</code>. </p>
<p>For example the underlining of a character say <code>t</code> looks like <code>\z\[ul]t</code> or <code>\z\(ult</code> </p>
<p>Longer words look then a bit strange, but a useful mode is to write each character into a whole own line. To underlines the 3 character part &quot;tar&quot; of the word &quot;start&quot;: </p>
<dl>
<dd> <p> <br />
 before s\ \z\[ul]t\ \z\[ul]a\ \z\[ul]r\ t after </p>
 </dd></dl>
<p> or </p>
<dl>
<dd> <p> <br />
 before s\ \z\(ult\ \z\(ula\ \z\(ulr\ t after </p>
 </dd></dl>
<p>The result looks like </p>
<dl>
<dd> <p> before s_t_a_rt after </p>
 </dd></dl>
<h2>COMPATIBILITY</h2>
<p> The differences between the groff language and classical troff as defined by [CSTR~#54] are documented in <code><a href="/docs/linux/man/7-groff_diff/">groff_diff</a></code>(7). </p>
<p>The groff system provides a compatibility mode, see <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) on how to invoke this.  </p>
<h2>AUTHORS</h2>
<p> This document was written by Bernd Warken  </p>
<h2>SEE ALSO</h2>
<p> <i>Groff: The GNU Implementation of troff</i>, by Trent A. Fisher and Werner Lemberg, is the primary <i>groff</i> manual. You can browse it interactively with "info groff". Besides the gory details, it contains many examples. </p>
<dl>
<dt><code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) </dt>
<dd> <p> the usage of the groff program and pointers to the documentation and availability of the groff system. </p>
 </dd>
<dt><code><a href="/docs/linux/man/7-groff_diff/">groff_diff</a></code>(7) </dt>
<dd> <p> describes the differences between the groff language and classical troff. </p>
 </dd>
<dd> <p> This is the authoritative document for the predefined language elements that are specific to groff. </p>
 </dd>
<dt><code><a href="/docs/linux/man/7-groff_char/">groff_char</a></code>(7) </dt>
<dd> <p> the predefined groff special characters (glyphs). </p>
 </dd>
<dt><code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5) </dt>
<dd> <p> the specification of fonts and the DESC file. </p>
 </dd>
<dt><code><a href="/docs/linux/man/5-groff_tmac/">groff_tmac</a></code>(5) </dt>
<dd> <p> contains an overview of available groff macro packages, instructions on how to interface them with a document, guidance on writing macro packages and using diversions, and historical information on macro package naming conventions. </p>
 </dd>
<dt><code><a href="/docs/linux/man/7-roff/">roff</a></code>(7) </dt>
<dd> <p> the history of roff, the common parts shared by all roff systems, and pointers to further documentation. </p>
 </dd>
<dt>[CSTR~#54]</dt>
<dd> <p> Nroff/:Troff User&#8217;s Manual by Ossanna &amp; Kernighan --- the bible for classical troff. </p>
 </dd>
<dt><i>Wikipedia</i></dt>
<dd> <p> article about <i>groff</i> </p>
 </dd>
<dt><i>Tutorial about groff</i></dt>
<dd> <p> Manas Laha - An Introduction to the GNU Groff Text Processing System </p>
 </dd>
<dt><i>troff.org</i></dt>
<dd> <p> This is a collection of internet sites with classical <i>roff</i> documentations and other information. </p>
 </dd></dl>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">GROFF ELEMENTS</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">CONTROL CHARACTERS</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">NUMERICAL EXPRESSIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">CONDITIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">REQUESTS</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAI">Request Short Reference</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAJ">ESCAPE SEQUENCES</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAK">Single-Character Escapes</a></dt>
<dd>  </dd>
<dt><a href="#lbAL">Special Characters</a></dt>
<dd>  </dd>
<dt><a href="#lbAM">Unicode Characters</a></dt>
<dd>  </dd>
<dt><a href="#lbAN">Strings</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAO">REGISTERS</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAP">Read-only Registers</a></dt>
<dd>  </dd>
<dt><a href="#lbAQ">Writable Registers</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAR">HYPHENATION</a></dt>
<dd>  </dd>
<dt><a href="#lbAS">UNDERLINING</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAT">Underlining with .ul</a></dt>
<dd>  </dd>
<dt><a href="#lbAU">Underlining with .UL from ms</a></dt>
<dd>  </dd>
<dt><a href="#lbAV">Underlining macro definitions</a></dt>
<dd>  </dd>
<dt><a href="#lbAW">Underlining without macro definitions</a></dt>
<dd>  </dd>
<dt><a href="#lbAX">Underlining with Overstriking \z and \(ul</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAY">COMPATIBILITY</a></dt>
<dd>  </dd>
<dt><a href="#lbAZ">AUTHORS</a></dt>
<dd>  </dd>
<dt><a href="#lbBA">SEE ALSO</a></dt>
<dd>  </dd></dl>
