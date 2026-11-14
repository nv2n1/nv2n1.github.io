---
title: "groff(7)"
name: "groff"
section: "7"
letter: "g"
url: "/docs/linux/man/7-groff/"
description: "groff – a short reference for the GNU roff language"
---

<p>groff &#8211; a short reference for the GNU roff language</p>
<h2>Description</h2>
<p>The name <i>groff</i> stands for <i>GNU roff</i> and is the free implementation of the roff type-setting system. See <code><a href="/docs/linux/man/7-roff/">roff</a></code>(7) for a survey and the background of the groff system. This document provides only short descriptions of roff language elements. <i>Groff: The GNU Implementation of troff</i>, by Trent A. Fisher and Werner Lemberg, is the primary <i>groff</i> manual, and is written in Texinfo. You can browse it interactively with &#8220;info groff&#8221;. Historically, the <i>roff language</i> was called <i>troff</i>. <i>groff</i> is compatible with the classical system and provides proper extensions. So in GNU, the terms <i>roff</i>, <i>troff</i>, and <i>groff language</i> could be used as synonyms. However <i>troff</i> slightly tends to refer more to the classical aspects, whereas <i>groff</i> emphasizes the GNU extensions, and <i>roff</i> is the general term for the language. The general syntax for writing groff documents is relatively easy, but writing extensions to the roff language can be a bit harder. The roff language is line-oriented. There are only two kinds of lines, control lines and text lines. The control lines start with a control character, by default a period or a single quote all other lines are text lines. <code>Control lines</code> represent commands, optionally with arguments. They have the following syntax. The leading control character can be followed by a command name; arguments, if any, are separated by spaces (but not tab characters) from the command name and among themselves, for example,</p>
<dl>
<dd> For indentation, any number of space or tab characters can be inserted between the leading control character and the command name, but the control character must be on the first position of the line. <code>Text lines</code> represent the parts that is printed. They can be modified by escape sequences, which are recognized by a leading backslash These are in-line or even in-word formatting elements or functions. Some of these take arguments separated by single quotes others are regulated by a length encoding introduced by an open parenthesis or enclosed in brackets and The roff language provides flexible instruments for writing language extension, such as macros. When interpreting macro definitions, the roff system enters a special operating mode, called the <code>copy mode</code>. The copy mode behaviour can be quite tricky, but there are some rules that ensure a safe usage.</p>
<dl>
<dt>1.</p>
<dd>Printable backslashes must be denoted as <code></code>. To be more precise, <code></code> represents the current escape character. To get a backslash glyph, use <code>\(rs</code> or <code>\[rs]</code>.</p>
<dt>2.</p>
<dd>Double all backslashes.</p>
<dt>3.</p>
<dd>Begin all text lines with the special non-spacing character <code>\&amp;</code>.</dl>
<p> This does not produce the most efficient code, but it should work as a first measure. For better strategies, see the <i>groff</i> Texinfo manual and <code><a href="/docs/linux/man/5-groff_tmac/">groff_tmac</a></code>(5). Reading roff source files is easier, just reduce all double backslashes to a single one in all macro definitions.</p>
<h2>Groff Elements</h2>
<p>The roff language elements add formatting information to a text file. The fundamental elements are predefined commands and variables that make roff a full-blown programming language. </p>
<p> There are two kinds of roff commands, possibly with arguments. <code>Requests</code> are written on a line of their own starting with a dot or a whereas <code>Escape sequences</code> are in-line functions and in-word formatting elements starting with a backslash </p>
<p> The user can define her own formatting commands using the <code>de</code> request. These commands are called <code>macros</code>, but they are used exactly like requests. Macro packages are pre-defined sets of macros written in the groff language. A user&#8217;s possibilities to create escape sequences herself is very limited, only special characters can be mapped. </p>
<p> The groff language provides several kinds of variables with different interfaces. There are pre-defined variables, but the user can define her own variables as well. </p>
<p> <code>String</code> variables store character sequences. They are set with the <code>ds</code> request and retrieved by the <code>\*</code> escape sequences. Strings can have variables. </p>
<p> <code>Register</code> variables can store numerical values, numbers with a scale unit, and occasionally string-like objects. They are set with the <code>nr</code> request and retrieved by the <code>
</code> escape sequences. </p>
<p> <code>Environments</code> allow the user to temporarily store global formatting parameters like line length, font size, etc. for later reuse. This is done by the <code>ev</code> request. </p>
<p> <code>Fonts</code> are identified either by a name or by an internal number. The current font is chosen by the <code>ft</code> request or by the <code></code> escape sequences. Each device has special fonts, but the following fonts are available for all devices. <code>R</code> is the standard font Roman. <code>B</code> is its <code>bold</code> counterpart. The <i>italic</i> font is called <code>I</code> and is available everywhere, but on text devices it is displayed as an underlined Roman font. For the graphical output devices, there exist constant-width pendants of these fonts, <code>CR</code>, <code>CI</code>, and <code>CB</code>. On text devices, all glyphs have a constant width anyway. </p>
<p> <code>Glyphs</code> are visual representation forms of <code>characters</code>. In groff, the distinction between those two elements is not always obvious (and a full discussion is beyond the scope of this man page). A first approximation is that glyphs have a specific size and colour and are taken from a specific font; they can&#8217;t be modified any more &#8211; characters are the input, and glyphs are the output. As soon as an output line has been generated, it no longer contains characters but glyphs. In this man page, we use either &#8216;glyph&#8217; or &#8216;character&#8217;, whatever is more appropriate. </p>
<p> Moreover, there are some advanced roff elements. A <code>diversion</code> stores (formatted) information into a macro for later usage. See <code><a href="/docs/linux/man/5-groff_tmac/">groff_tmac</a></code>(5) for more details. A <code>trap</code> is a positional condition like a certain number of lines from page top or in a diversion or in the input. Some action can be prescribed to be run automatically when the condition is met. </p>
<p> More detailed information and examples can be found in the <i>groff</i> Texinfo manual.</p>
<h2>Control Characters</h2>
<p>There is a small set of characters that have a special controlling task in certain conditions.</p>
<dl>
<dt>.</p>
<dd>A dot is only special at the beginning of a line or after the condition in the requests <code>if</code> , <code>ie</code> , <code>el</code> , and <code>while</code> . There it is the control character that introduces a request (or macro). By using the <code>cc</code> request, the control character can be set to a different character, making the dot a non-special character.</p>
<dd>In all other positions, it just means a dot character. In text paragraphs, it is advantageous to start each sentence at a line of its own.</p>
<dt>&#8216;</p>
<dd>The single quote has two controlling tasks. At the beginning of a line and in the conditional requests it is the non-breaking control character. That means that it introduces a request like the dot, but with the additional property that this request doesn&#8217;t cause a linebreak. By using the <code>c2</code> request, the non-break control character can be set to a different character.</p>
<dd>As a second task, it is the most commonly used argument separator in some functional escape sequences (but any pair of characters not part of the argument do work). In all other positions, it denotes the single quote or apostrophe character. Groff provides a printable representation with the <code>\(cq</code> escape sequence.</p>
<dt>&quot;</p>
<dd>The double quote is used to enclose arguments in macros (but not in requests and strings). In the <code>ds</code> and <code>as</code> requests, a leading double quote in the argument is stripped off, making everything else afterwards the string to be defined (enabling leading whitespace). The escaped double quote <code>\&quot;</code> introduces a comment. Otherwise, it is not special. Groff provides a printable representation with the <code>\(dq</code> escape sequence.</p>
<dt>\</p>
<dd>The backslash usually introduces an escape sequence (this can be changed with the <code>ec</code> request). A printed version of the escape character is the <code></code> escape; a backslash glyph can be obtained by <code>\(rs</code>.</p>
<dt>(</p>
<dd>The open parenthesis is only special in escape sequences when introducing an escape name or argument consisting of exactly two characters. In groff, this behaviour can be replaced by the [] construct.</p>
<dt>[</p>
<dd>The opening bracket is only special in groff escape sequences; there it is used to introduce a long escape name or long escape argument. Otherwise, it is non-special, e.g. in macro calls.</p>
<dt>]</p>
<dd>The closing bracket is only special in groff escape sequences; there it terminates a long escape name or long escape argument. Otherwise, it is non-special.</p>
<dt>space</p>
<dd>Space characters are only functional characters. They separate the arguments in requests, macros, and strings, and the words in text lines. They are subject to groff&#8217;s horizontal spacing calculations. To get a defined space width, escape sequences like (this is the escape character followed by a space), <code>\|</code>, <code>\^</code>, or <code>\h</code> should be used.</p>
<dt>newline</p>
<dd>In text paragraphs, newlines mostly behave like space characters. Continuation lines can be specified by an escaped newline, i.e., by specifying a backslash as the last character of a line.</p>
<dt>tab</p>
<dd>If a tab character occurs during text the interpreter makes a horizontal jump to the next pre-defined tab position. There is a sophisticated interface for handling tab positions.</dl>
<h2>Numerical Expressions</h2>
<p>A <code>numerical value</code> is a signed or unsigned integer or float with or without an appended scaling indicator. A <code>scaling indicator</code> is a one-character abbreviation for a unit of measurement. A number followed by a scaling indicator signifies a size value. By default, numerical values do not have a scaling indicator, i.e., they are normal numbers. </p>
<p> The <i>roff</i> language defines the following scaling indicators. </p>
<dl>
<dd>
<dl>
<dt> <code>c</code></p>
<dd>centimeter</p>
<dt> <code>i</code></p>
<dd>inch</p>
<dt> <code>P</code></p>
<dd>pica&nbsp;=&nbsp;1/6 inch</p>
<dt> <code>p</code></p>
<dd>point&nbsp;=&nbsp;1/72 inch</p>
<dt> <code>m</code></p>
<dd>em&nbsp;=&nbsp;the font size in points (approx. width of letter &#8216;m&#8217;)</p>
<dt> <code>M</code></p>
<dd>100th of an em</p>
<dt> <code>n</code></p>
<dd>en&nbsp;=&nbsp;em/2</p>
<dt> <code>u</code></p>
<dd>Basic unit for actual output device</p>
<dt> <code>v</code></p>
<dd>Vertical line space in basic units</p>
<dt> <code>s</code></p>
<dd>scaled point&nbsp;=&nbsp;1/sizescale of a point (defined in font DESC file)</p>
<dt> <code>f</code></p>
<dd>Scale by 65536.</dl>
</dl>
<p> <code>Numerical expressions</code> are combinations of the numerical values defined above with the following arithmetical operators already defined in classical troff. </p>
<dl>
<dd>
<dl>
<dt> <code>+</code></p>
<dd>Addition</p>
<dt> <code>&#8211;</code></p>
<dd>Subtraction</p>
<dt> <code>*</code></p>
<dd>Multiplication</p>
<dt> <code>/</code></p>
<dd>Division</p>
<dt> <code>%</code></p>
<dd>Modulo</p>
<dt> <code>=</code></p>
<dd>Equals</p>
<dt> <code>==</code></p>
<dd>Equals</p>
<dt> <code>&lt;</code></p>
<dd>Less than</p>
<dt> <code>&gt;</code></p>
<dd>Greater than</p>
<dt> <code>&lt;=</code></p>
<dd>Less or equal</p>
<dt> <code>&gt;=</code></p>
<dd>Greater or equal</p>
<dt> <code>&amp;</code></p>
<dd>Logical and</p>
<dt> <code>:</code></p>
<dd>Logical or</p>
<dt> <code>!</code></p>
<dd>Logical not</p>
<dt> <code>(</code></p>
<dd>Grouping of expressions</p>
<dt> <code>)</code></p>
<dd>Close current grouping</dl>
</dl>
<p> Moreover, <i>groff</i> added the following operators for numerical expressions: </p>
<dl>
<dd>
<dl>
<dt> e1/&gt;?,e2</p>
<dd>The maximum of <i>e1</i> and <i>e2</i>.</p>
<dt> e1/&lt;?,e2</p>
<dd>The minimum of <i>e1</i> and <i>e2</i>.</p>
<dt> (,c/;,e/)</p>
<dd>Evaluate <i>e</i> using <i>c</i> as the default scaling indicator.</dl>
</dl>
<p> For details see the <i>groff</i> Texinfo manual.</p>
<h2>Conditions</h2>
<p><code>Conditions</code> occur in tests raised by the <code>if</code> , <code>ie</code> , and the <code>while</code> requests. The following table characterizes the different types of conditions. </p>
<dl>
<dd>
<dl>
<dt> <i>N</i></p>
<dd>A numerical expression <i>N</i> yields true if its value is greater than~0.</p>
<dt> <code>!</code><i>N</i></p>
<dd>True if the value of <i>N</i> is~0 (see below).</p>
<dt> <code>&#8216;</code><i>s1</i><code>&#8216;</code><i>s2</i><code>&#8216;</code></p>
<dd>True if string~<i>s1</i> is identical to string~<i>s2</i>.</p>
<dt> <code>!&#8217;</code><i>s1</i><code>&#8216;</code><i>s2</i><code>&#8216;</code></p>
<dd>True if string~<i>s1</i> is not identical to string~<i>s2</i> (see below).</p>
<dt> <code>c</code><i>ch</i></p>
<dd>True if there is a glyph~<i>ch</i> available.</p>
<dt> <code>d</code><i>name</i></p>
<dd>True if there is a string, macro, diversion, or request called <i>name</i>.</p>
<dt> <code>e</code></p>
<dd>Current page number is even.</p>
<dt> <code>o</code></p>
<dd>Current page number is odd.</p>
<dt> <code>m</code><i>name</i></p>
<dd>True if there is a color called <i>name</i>.</p>
<dt> <code>n</code></p>
<dd>Formatter is <code>nroff</code>.</p>
<dt> <code>r</code><i>reg</i></p>
<dd>True if there is a register named <i>reg</i>.</p>
<dt> <code>t</code></p>
<dd>Formatter is <code>troff</code>.</p>
<dt> <code>F</code><i>font</i></p>
<dd>True if there exists a font named <i>font</i>.</p>
<dt> <code>S</code><i>style</i></p>
<dd>True if a style named <i>style</i> has been registered.</dl>
</dl>
<p> Note that the <code>!</code> operator may only appear at the beginning of an expression, and negates the entire expression. This maintains bug-compatibility with AT&amp;T <i>troff</i>.</p>
<h2>Requests</h2>
<p>This section provides a short reference for the predefined requests. In groff, request, macro, and string names can be arbitrarily long. No bracketing or marking of long names is needed. </p>
<p> Most requests take one or more arguments. The arguments are separated by space characters (no tabs!); there is no inherent limit for their length or number. </p>
<p> Some requests have optional arguments with a different behaviour. Not all of these details are outlined here. Refer to the <i>groff</i> Texinfo manual and <code><a href="/docs/linux/man/7-groff_diff/">groff_diff</a></code>(7) for all details. </p>
<p> In the following request specifications, most argument names were chosen to be descriptive. Only the following denotations need clarification. </p>
<dl>
<dd>
<dl>
<dt> <i>c</i></p>
<dd>denotes a single character.</p>
<dt> <i>font</i></p>
<dd>a font either specified as a font name or a font number.</p>
<dt> <i>anything</i></p>
<dd>all characters up to the end of the line or within <code>\{</code> and <code>\}</code>.</p>
<dt> <i>n</i></p>
<dd>is a numerical expression that evaluates to an integer value.</p>
<dt> <i>N</i></p>
<dd>is an arbitrary numerical expression, signed or unsigned.</p>
<dt> <i>&plusmn;N</i></p>
<dd>has three meanings depending on its sign, described below.</dl>
</dl>
<p> If an expression defined as <i>&plusmn;N</i> starts with a sign the resulting value of the expression is added to an already existing value inherent to the related request, e.g. adding to a number register. If the expression starts with a the value of the expression is subtracted from the request value. </p>
<p> Without a sign, <i>N</i> replaces the existing value directly. To assign a negative number either prepend~0 or enclose the negative number in parentheses.</p>
<h3>Request Short Reference</h3>
<dl>
<dd>Empty line, ignored. Useful for structuring documents.</p>
<dd>Complete line is a comment.</p>
<dd>Print <i>string</i> on standard error, exit program.</p>
<dd>Begin line adjustment for output lines in current adjust mode.</p>
<dd>Start line adjustment in mode <i>c</i> (c/=l,r,c,b,n).</p>
<dd>Assign format <i>c</i> to <i>register</i> (c/=l,i,I,a,A).</p>
<dd>Create alias name for <i>register</i>.</p>
<dd>Create alias name for request, string, macro, or diversion <i>object</i>.</p>
<dd>Append to <i>macro</i> until <code>..</code> is encountered.</p>
<dd>Append to <i>macro</i> until <code>.</code><i>end</i> is called.</p>
<dd>Same as <code>.am</code> but with compatibility mode switched off during macro expansion.</p>
<dd>Same as <code>.am</code> but with compatibility mode switched off during macro expansion.</p>
<dd>Append to a macro whose name is contained in the string register <i>macro</i> until <code>..</code> is encountered.</p>
<dd>Append to a macro indirectly. <i>macro</i> and <i>end</i> are string registers whose contents are interpolated for the macro name and the end macro, respectively.</p>
<dd>Same as <code>.ami</code> but with compatibility mode switched off during macro expansion.</p>
<dd>Same as <code>.ami</code> but with compatibility mode switched off during macro expansion.</p>
<dd>Append <i>anything</i> to <i>stringvar</i>.</p>
<dd>Same as <code>.as</code> but with compatibility mode switched off during string expansion.</p>
<dd>Unformat ASCII characters, spaces, and some escape sequences in <i>diversion</i>.</p>
<dd>Print a backtrace of the input on stderr.</p>
<dd>Embolden <i>font</i> by <i>N</i>-1 units.</p>
<dd>Embolden Special Font <i>S</i> when current font is <i>font</i>.</p>
<dd>Unset the blank line macro.</p>
<dd>Set the blank line macro to <i>macro</i>.</p>
<dd>End current diversion.</p>
<dd>Divert to <i>macro</i>, omitting a partially filled line.</p>
<dd>End current diversion.</p>
<dd>Divert and append to <i>macro</i>, omitting a partially filled line.</p>
<dd>Eject current page and begin new page.</p>
<dd>Eject current page; next page number <i>&plusmn;N</i>.</p>
<dd>Line break.</p>
<dd>Break output line; adjust if applicable.</p>
<dd>Break out of a while loop.</p>
<dd>Reset no-break control character to</p>
<dd>Set no-break control character to <i>c</i>.</p>
<dd>Reset control character to</p>
<dd>Set control character to <i>c</i>.</p>
<dd>Center the next input line.</p>
<dd>Center following <i>N</i> input lines.</p>
<dd>Copy contents of file <i>filename</i> unprocessed to stdout or to the diversion.</p>
<dd>Treat characters <i>c1</i>, <i>c2</i>, &#8230; according to <i>mode</i> number.</p>
<dd>Change <i>trap</i> location to <i>N</i>.</p>
<dd>Define entity <i>c</i> as string <i>anything</i>.</p>
<dd>Chop the last character off macro, string, or diversion <i>object</i>.</p>
<dd>Assign a set of characters, character ranges, or classes <i>c1</i>, <i>c2</i>, &#8230; to <i>name</i>.</p>
<dd>Close the <i>stream</i>.</p>
<dd>Enable colors.</p>
<dd>If <i>N</i> is zero disable colors, otherwise enable them.</p>
<dd>Map glyph name <i>from</i> to glyph name <i>to</i> while constructing a composite glyph name.</p>
<dd>Finish the current iteration of a while loop.</p>
<dd>Enable compatibility mode.</p>
<dd>If <i>N</i> is zero disable compatibility mode, otherwise enable it.</p>
<dd>Set constant character width mode for <i>font</i> to <i>N</i>/36 ems with em <i>M</i>.</p>
<dd>Continuous underline in nroff, like <code>.ul</code> in troff.</p>
<dd>End current diversion.</p>
<dd>Divert and append to <i>macro</i>.</p>
<dd>Define or redefine <i>macro</i> until <code>..</code> is encountered.</p>
<dd>Define or redefine <i>macro</i> until <code>.</code><i>end</i> is called.</p>
<dd>Same as <code>.de</code> but with compatibility mode switched off during macro expansion.</p>
<dd>Same as <code>.de</code> but with compatibility mode switched off during macro expansion.</p>
<dd>Define or redefine a color with name <i>color</i>. <i>scheme</i> can be <code>rgb</code>, <code>cym</code>, <code>cymk</code>, <code>gray</code>, or <code>grey</code>. <i>component</i> can be single components specified as fractions in the range 0 to 1 (default scaling indicator~ as a string of two-digit hexadecimal color components with a leading <code>#</code>, or as a string of four-digit hexadecimal components with two leading <code>#</code>. The color <code>default</code> can&#8217;t be redefined.</p>
<dd>Define or redefine a macro whose name is contained in the string register <i>macro</i> until <code>..</code> is encountered.</p>
<dd>Define or redefine a macro indirectly. <i>macro</i> and <i>end</i> are string registers whose contents are interpolated for the macro name and the end macro, respectively.</p>
<dd>Same as <code>.dei</code> but with compatibility mode switched off during macro expansion.</p>
<dd>Same as <code>.dei</code> but with compatibility mode switched off during macro expansion.</p>
<dd>Write <i>anything</i> to the intermediate output as a device control function.</p>
<dd>Write contents of macro or string <i>name</i> uninterpreted to the intermediate output as a device control function.</p>
<dd>End current diversion.</p>
<dd>Divert to <i>macro</i>. See <code><a href="/docs/linux/man/5-groff_tmac/">groff_tmac</a></code>(5) for more details.</p>
<dd>Interpret <code>.</code><i>name</i> with compatibility mode disabled.</p>
<dd>Set <i>stringvar</i> to <i>anything</i>.</p>
<dd>Same as <code>.ds</code> but with compatibility mode switched off during string expansion.</p>
<dd>Set diversion trap to position <i>N</i> (default scaling indicator~</p>
<dd>Reset escape character to</p>
<dd>Set escape character to <i>c</i>.</p>
<dd>Restore escape character saved with <code>.ecs</code> .</p>
<dd>Save current escape character.</p>
<dd>Else part for if-else (<code>.ie</code> ) request.</p>
<dd>The <i>macro</i> is run after the end of input.</p>
<dd>Turn off escape character mechanism.</p>
<dd>Switch to previous environment and pop it off the stack.</p>
<dd>Push down environment number or name <i>env</i> to the stack and switch to it.</p>
<dd>Copy the contents of environment <i>env</i> to the current environment. No pushing or popping.</p>
<dd>Exit from roff processing.</p>
<dd>Return to previous font family.</p>
<dd>Set the current font family to <i>name</i>.</p>
<dd>Disable field mechanism.</p>
<dd>Set field delimiter to~<i>a</i> and pad glyph to space.</p>
<dd>Set field delimiter to~<i>a</i> and pad glyph to~<i>b</i>.</p>
<dd>Define fallback character (or glyph) <i>c</i> as string <i>anything</i>.</p>
<dd>Set fill color to previous fill color.</p>
<dd>Set fill color to <i>c</i>.</p>
<dd>Fill output lines.</p>
<dd>Flush output buffer.</p>
<dd>Mount <i>font</i> on position <i>n</i>.</p>
<dd>Mount font with long <i>external</i> name to short <i>internal</i> name on position <i>n</i>.</p>
<dd>Define fallback character (or glyph) <i>c</i> for font <i>f</i> as string <i>anything</i>.</p>
<dd>Reset list of special fonts for <i>font</i> to be empty.</p>
<dd>When the current font is <i>font</i>, then the fonts <i>s1</i>, <i>s2</i>, &#8230; are special.</p>
<dd>Return to previous font. Same as <code>\</code> or <code>\</code> .</p>
<dd>Change to font name or number <i>font</i>; same as escape sequence.</p>
<dd>Translate <i>font1</i> to <i>font2</i>.</p>
<dd>Don&#8217;t magnify <i>font</i>.</p>
<dd>Set zoom factor for <i>font</i> (in multiples of 1/1000th).</p>
<dd>Set glyph color to previous glyph color.</p>
<dd>Set glyph color to <i>c</i>.</p>
<dd>Remove additional hyphenation indicator character.</p>
<dd>Set up additional hyphenation indicator character~<i>c</i>.</p>
<dd>Set the hyphenation code of character <i>c1</i> to <i>code1</i>, that of <i>c2</i> to <i>code2</i>, etc.</p>
<dd>Set the current hyphenation language to <i>lang</i>.</p>
<dd>Set the maximum number of consecutive hyphenated lines to <i>n</i>.</p>
<dd>Read hyphenation patterns from <i>file</i>.</p>
<dd>Append hyphenation patterns from <i>file</i>.</p>
<dd>Set input mapping for <code>.hpf</code> .</p>
<dd>List of <i>words</i> with exceptional hyphenation.</p>
<dd>Switch to hyphenation mode <i>N</i>.</p>
<dd>Set the hyphenation margin to <i>n</i> (default scaling indicator~</p>
<dd>Set the hyphenation space to <i>n</i>.</p>
<dd>If <i>cond</i> then <i>anything</i> else goto <code>.el</code> .</p>
<dd>If <i>cond</i> then <i>anything</i>; otherwise do nothing.</p>
<dd>Ignore text until <code>..</code> is encountered.</p>
<dd>Ignore text until <code>.</code><i>end</i> is called.</p>
<dd>Change to previous indentation value.</p>
<dd>Change indentation according to <i>&plusmn;N</i> (default scaling indicator~</p>
<dd>Set an input-line count trap for the next <i>N</i> lines.</p>
<dd>Same as <code>.it</code> but don&#8217;t count lines interrupted with <code>
