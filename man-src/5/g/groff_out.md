---
title: "groff_out(5)"
name: "groff_out"
section: "5"
letter: "g"
url: "/docs/linux/man/5-groff_out/"
description: "groff_out – groff intermediate output format"
---

<p>groff_out &#8211; groff intermediate output format</p>
<h2>Description</h2>
<p>This manual page describes the <i>intermediate output</i> format of the GNU <code><a href="/docs/linux/man/7-roff/">roff</a></code>(7) text processing system <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1). This output is produced by a run of the GNU <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1) program. It contains already all device-specific information, but it is not yet fed into a device postprocessor program. </p>
<p> As the GNU <i>roff</i> processor <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) is a wrapper program around <code>troff</code> that automatically calls a postprocessor, this output does not show up normally. This is why it is called <i>intermediate</i> within the <i>groff</i> <i>system</i>. The <code>groff</code> program provides the option <code>-Z</code> to inhibit postprocessing, such that the produced <i>intermediate output</i> is sent to standard output just like calling <code>troff</code> manually. </p>
<p> In this document, the term <i>troff output</i> describes what is output by the GNU <code>troff</code> program, while <i>intermediate output</i> refers to the language that is accepted by the parser that prepares this output for the postprocessors. This parser is smarter on whitespace and implements obsolete elements for compatibility, otherwise both formats are the same. Both formats can be viewed directly with <code><a href="/docs/linux/man/1-gxditview/">gxditview</a></code>(1). </p>
<p> The main purpose of the <i>intermediate output</i> concept is to facilitate the development of postprocessors by providing a common programming interface for all devices. It has a language of its own that is completely different from the <code><a href="/docs/linux/man/7-groff/">groff</a></code>(7) language. While the <i>groff</i> language is a high-level programming language for text processing, the <i>intermediate output</i> language is a kind of low-level assembler language by specifying all positions on the page for writing and drawing. </p>
<p> The pre-<i>groff</i> <i>roff</i> versions are denoted as <i>classical</i> <i>troff</i>. The <i>intermediate output</i> produced by <code>groff</code> is fairly readable, while <i>classical troff</i> output was hard to understand because of strange habits that are still supported, but not used any longer by <i>GNU</i> <i>troff</i>.</p>
<h2>Language Concepts</h2>
<p>During the run of <code>troff</code>, the <i>roff</i> input is cracked down to the information on what has to be printed at what position on the intended device. So the language of the <i>intermediate output</i> format can be quite small. Its only elements are commands with or without arguments. In this document, the term &#8220;command&#8221; always refers to the <i>intermediate output</i> language, never to the <i>roff</i> language used for document formatting. There are commands for positioning and text writing, for drawing, and for device controlling.</p>
<h3>Separation</h3>
<p><i>Classical troff output</i> had strange requirements on whitespace. The <code>groff</code> output parser, however, is smart about whitespace by making it maximally optional. The whitespace characters, i.e., the <i>tab</i>, <i>space</i>, and <i>newline</i> characters, always have a syntactical meaning. They are never printable because spacing within the output is always done by positioning commands. </p>
<p> Any sequence of <i>space</i> or <i>tab</i> characters is treated as a single <i>syntactical</i> <i>space</i>. It separates commands and arguments, but is only required when there would occur a clashing between the command code and the arguments without the space. Most often, this happens when variable length command names, arguments, argument lists, or command clusters meet. Commands and arguments with a known, fixed length need not be separated by <i>syntactical</i> <i>space</i>. </p>
<p> A line break is a syntactical element, too. Every command argument can be followed by whitespace, a comment, or a newline character. Thus a <i>syntactical line break</i> is defined to consist of optional <i>syntactical space</i> that is optionally followed by a comment, and a newline character. </p>
<p> The normal commands, those for positioning and text, consist of a single letter taking a fixed number of arguments. For historical reasons, the parser allows stacking of such commands on the same line, but fortunately, in <i>groff intermediate</i> <i>output</i>, every command with at least one argument is followed by a line break, thus providing excellent readability. </p>
<p> The other commands &#8212; those for drawing and device controlling &#8212; have a more complicated structure; some recognize long command names, and some take a variable number of arguments. So all <code>D</code> and <code>x</code> commands were designed to request a <i>syntactical line break</i> after their last argument. Only one command, &#8216;<code>x X</code>&#8216; has an argument that can stretch over several lines, all other commands must have all of their arguments on the same line as the command, i.e., the arguments may not be split by a line break. </p>
<p> Empty lines, i.e., lines containing only space and/or a comment, can occur everywhere. They are just ignored.</p>
<h3>Argument Units</h3>
<p>Some commands take integer arguments that are assumed to represent values in a measurement unit, but the letter for the corresponding <i>scale indicator</i> is not written with the output command arguments; see <code><a href="/docs/linux/man/7-groff/">groff</a></code>(7) and <i>Groff: The GNU Implementation of troff</i>, the <i>groff</i> Texinfo manual, for more on this topic. Most commands assume the scale indicator~<code>u</code>, the basic unit of the device, some use~<code>z</code>, the <i>scaled point unit</i> of the device, while others, such as the color commands expect plain integers. Note that these scale indicators are relative to the chosen device. They are defined by the parameters specified in the device&#8217;s <i>DESC</i> file; see <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5). </p>
<p> Note that single characters can have the eighth bit set, as can the names of fonts and special characters (this is, glyphs). The names of glyphs and fonts can be of arbitrary length. A glyph that is to be printed will always be in the current font. </p>
<p> A string argument is always terminated by the next whitespace character (space, tab, or newline); an embedded <code>#</code> character is regarded as part of the argument, not as the beginning of a comment command. An integer argument is already terminated by the next non-digit character, which then is regarded as the first character of the next argument or command.</p>
<h3>Document Parts</h3>
<p>A correct <i>intermediate output</i> document consists of two parts, the <i>prologue</i> and the <i>body</i>. </p>
<p> The task of the <i>prologue</i> is to set the general device parameters using three exactly specified commands. The <i>groff prologue</i> is guaranteed to consist of the following three lines (in that order):</p>
<dl>
<dd><code>x T</code> <i>device</i><br />
 <code>x res</code> <i>n h v</i><br />
 <code>x init</code></dl>
<p> with the arguments set as outlined in subsection &#8220;Device Control Commands&#8221; below. However, the parser for the <i>intermediate output</i> format is able to swallow additional whitespace and comments as well. </p>
<p> The <i>body</i> is the main section for processing the document data. Syntactically, it is a sequence of any commands different from the ones used in the <i>prologue</i>. Processing is terminated as soon as the first <code>x stop</code> command is encountered; the last line of any <i>groff intermediate output</i> always contains such a command. </p>
<p> Semantically, the <i>body</i> is page oriented. A new page is started by a <code>p</code>~command. Positioning, writing, and drawing commands are always done within the current page, so they cannot occur before the first <code>p</code>~command. Absolute positioning (by the <code>H</code> and <code>V</code>~commands) is done relative to the current page, all other positioning is done relative to the current location within this page.</p>
<h2>Command Reference</h2>
<p>This section describes all <i>intermediate output</i> commands, the classical commands as well as the <i>groff</i> extensions.</p>
<h3>Comment Command</h3>
<dl>
<dt><code>#</code><i>anything</i><code>&lt;end-of-line&gt;</code></p>
<dd>A comment. Ignore any characters from the <code>#</code>~character up to the next newline character.</dl>
<p> This command is the only possibility for commenting in the <i>intermediate</i> <i>output</i>. Each comment can be preceded by arbitrary <i>syntactical</i> <i>space</i>; every command can be terminated by a comment.</p>
<h3>Simple Commands</h3>
<p>The commands in this subsection have a command code consisting of a single character, taking a fixed number of arguments. Most of them are commands for positioning and text writing. These commands are smart about whitespace. Optionally, <i>syntactical space</i> can be inserted before, after, and between the command letter and its arguments. All of these commands are stackable, i.e., they can be preceded by other simple commands or followed by arbitrary other commands on the same line. A separating <i>syntactical space</i> is only necessary when two integer arguments would clash or if the preceding argument ends with a string argument.</p>
<dl>
<dt> <code>C</code>&nbsp;<i>,xxx/</i>&lt;white-space&gt;</p>
<dd>Print a glyph (special character) named <i>xxx</i>. The trailing <i>syntactical space</i> or <i>line break</i> is necessary to allow glyph names of arbitrary length. The glyph is printed at the current print position; the glyph&#8217;s size is read from the font file. The print position is not changed.</p>
<dt> <code>c</code>&nbsp;<i>,c/</i></p>
<dd>Print glyph with single-letter name~<i>c</i> at the current print position; the glyph&#8217;s size is read from the font file. The print position is not changed.</p>
<dt> <code>f</code>&nbsp;<i>,n/</i></p>
<dd>Set font to font number~<i>n</i> (a non-negative integer).</p>
<dt> <code>H</code>&nbsp;<i>,n/</i></p>
<dd>Move right to the absolute vertical position~<i>n</i> (a non-negative integer in basic units~<code>u</code>) relative to left edge of current page.</p>
<dt> <code>h</code>&nbsp;<i>,n/</i></p>
<dd>Move <i>n</i> (a non-negative integer) basic units~<code>u</code> horizontally to the right. [CSTR~#54] allows negative values for <i>n</i> also, but <i>groff</i> doesn&#8217;t use this.</p>
<dt> <code>m</code>&nbsp;<i>,color-scheme [component &#8230;]/</i></p>
<dd>Set the color for text (glyphs), line drawing, and the outline of graphic objects using different color schemes; the analogous command for the filling color of graphic objects is <code>DF</code>. The color components are specified as integer arguments between 0 and @maxcolor]. The number of color components and their meaning vary for the different color schemes. These commands are generated by the <i>groff</i> escape sequence <code>m</code>. No position changing. These commands are a <i>groff</i> extension.</p>
<dl>
<dd>
<dl>
<dt> <code>mc</code>&nbsp;<i>,cyan magenta yellow/</i></p>
<dd>Set color using the CMY color scheme, having the 3~color components cyan, magenta, and yellow.</p>
<dt> <code>md</code>&nbsp;<i>,/</i></p>
<dd>Set color to the default color value (black in most cases). No component arguments.</p>
<dt> <code>mg</code>&nbsp;<i>,gray/</i></p>
<dd>Set color to the shade of gray given by the argument, an integer between 0 (black) and @maxcolor] (white).</p>
<dt> <code>mk</code>&nbsp;<i>,cyan magenta yellow black/</i></p>
<dd>Set color using the CMYK color scheme, having the 4~color components cyan, magenta, yellow, and black.</p>
<dt> <code>mr</code>&nbsp;<i>,red green blue/</i></p>
<dd>Set color using the RGB color scheme, having the 3~color components red, green, and blue.</dl>
</dl>
<dt> <code>N</code>&nbsp;<i>,n/</i></p>
<dd>Print glyph with index~<i>n</i> (an integer, normally non-negative) of the current font. The print position is not changed. If <code>-T~html</code> or <code>-T~xhtml</code> is used, negative values are emitted also to indicate an unbreakable space with given width. For example, <code>N~-193</code> represents an unbreakable space which has a width of 193u. This command is a <i>groff</i> extension.</p>
<dt> <code>n</code>&nbsp;<i>,b a/</i></p>
<dd>Inform the device about a line break, but no positioning is done by this command. In <i>classical</i> <i>troff</i>, the integer arguments <i>b</i> and~<i>a</i> informed about the space before and after the current line to make the <i>intermediate output</i> more human readable without performing any action. In <i>groff</i>, they are just ignored, but they must be provided for compatibility reasons.</p>
<dt> <code>p</code>&nbsp;<i>,n/</i></p>
<dd>Begin a new page in the outprint. The page number is set to~<i>n</i>. This page is completely independent of pages formerly processed even if those have the same page number. The vertical position on the outprint is automatically set to~0. All positioning, writing, and drawing is always done relative to a page, so a <code>p</code>~command must be issued before any of these commands.</p>
<dt> <code>s</code>&nbsp;<i>,n/</i></p>
<dd>Set point size to <i>n</i> scaled points (this is unit~<code>z</code> in GNU <code>troff</code>). <i>Classical troff</i> used the unit <i>points</i> (<code>p</code>) instead; see section &#8220;Compatibility&#8221; below.</p>
<dt> <code>t</code>&nbsp;<i>,xyz&#8230;/</i>&lt;white-space&gt;</p>
<dd><code>t</code>&nbsp;<i>,xyz&#8230; dummy-arg/</i>&lt;white-space&gt; Print a word, i.e., a sequence of glyphs with single-letter names <i>x</i>, <i>y</i>, <i>z</i>, etc., terminated by a space character or a line break; an optional second integer argument is ignored (this allows the formatter to generate an even number of arguments). The first glyph should be printed at the current position, the current horizontal position should then be increased by the width of the first glyph, and so on for each glyph. The widths of the glyph are read from the font file, scaled for the current point size, and rounded to a multiple of the horizontal resolution. Special characters (glyphs with names longer than a single letter) cannot be printed using this command; use the <code>C</code> command for those glyphs. This command is a <i>groff</i> extension; it is only used for devices whose <i>DESC</i> file contains the <code>tcommand</code> keyword; see <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5).</p>
<dt> <code>u</code>&nbsp;<i>,n xyz&#8230;/</i>&lt;white-space&gt;</p>
<dd>Print word with track kerning. This is the same as the <code>t</code> command except that after printing each glyph, the current horizontal position is increased by the sum of the width of that glyph and~<i>n</i> (an integer in basic units~<code>u</code>). This command is a <i>groff</i> extension; it is only used for devices whose <i>DESC</i> file contains the <code>tcommand</code> keyword; see <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5).</p>
<dt> <code>V</code>&nbsp;<i>,n/</i></p>
<dd>Move down to the absolute vertical position~<i>n</i> (a non-negative integer in basic units~<code>u</code>) relative to upper edge of current page.</p>
<dt> <code>v</code>&nbsp;<i>,n/</i></p>
<dd>Move <i>n</i> basic units~<code>u</code> down (<i>n</i> is a non-negative integer). [CSTR~#54] allows negative values for <i>n</i> also, but <i>groff</i> doesn&#8217;t use this.</p>
<dt> <code>w</code>&nbsp;<i>,/</i></p>
<dd>Informs about a paddable whitespace to increase readability. The spacing itself must be performed explicitly by a move command.</dl>
<h3>Graphics Commands</h3>
<p>Each graphics or drawing command in the <i>intermediate output</i> starts with the letter~<code>D</code> followed by one or two characters that specify a subcommand; this is followed by a fixed or variable number of integer arguments that are separated by a single space character. A <code>D</code>~command may not be followed by another command on the same line (apart from a comment), so each <code>D</code>~command is terminated by a <i>syntactical line</i> <i>break</i>. </p>
<p> <code>troff</code> output follows the classical spacing rules (no space between command and subcommand, all arguments are preceded by a single space character), but the parser allows optional space between the command letters and makes the space before the first argument optional. As usual, each space can be any sequence of tab and space characters. </p>
<p> Some graphics commands can take a variable number of arguments. In this case, they are integers representing a size measured in basic units~<code>u</code>. The <i>h</i> arguments stand for horizontal distances where positive means right, negative left. The <i>v</i> arguments stand for vertical distances where positive means down, negative up. All these distances are offsets relative to the current location. </p>
<p> Unless indicated otherwise, each graphics command directly corresponds to a similar <i>groff</i> <code>D</code> escape sequence; see <code><a href="/docs/linux/man/7-groff/">groff</a></code>(7). </p>
<p> Unknown <code>D</code>~commands are assumed to be device-specific. Its arguments are parsed as strings; the whole information is then sent to the postprocessor. </p>
<p> In the following command reference, the syntax element <i>&lt;line-break&gt;</i> means a <i>syntactical line break</i> as defined in subsection &#8220;Separation&#8221; above.</p>
<dl>
<dt> <code>D~</code>&nbsp; &#8230;</p>
<dd>Draw B-spline from current position to offset (<i>,<i>h/</i><font SIZE="-3">1</font>/</i>,&nbsp;<i>,<i>v/</i><font SIZE="-3">1</font>/</i>), then to offset (<i>,<i>h/</i><font SIZE="-3">2</font>/</i>,&nbsp;<i>,<i>v/</i><font SIZE="-3">2</font>/</i>) if given, etc., up to (<i>,<i>h/</i><font SIZE="-3">n</font>/</i>,&nbsp;<i>,<i>v/</i><font SIZE="-3">n</font>/</i>). This command takes a variable number of argument pairs; the current position is moved to the terminal point of the drawn curve.</p>
<dt> <code>Da</code>&nbsp;</p>
<dd>Draw arc from current position to (<i>,<i>h/</i><font SIZE="-3">1</font>/</i>,&nbsp;<i>,<i>v/</i><font SIZE="-3">1</font>/</i>)+ (<i>,<i>h/</i><font SIZE="-3">2</font>/</i>,&nbsp;<i>,<i>v/</i><font SIZE="-3">2</font>/</i>) with center at (<i>,<i>h/</i><font SIZE="-3">1</font>/</i>,&nbsp;<i>,<i>v/</i><font SIZE="-3">1</font>/</i>); then move the current position to the final point of the arc.</p>
<dt> <code>DC</code>&nbsp;<i>,d/</i></p>
<dd><code>DC</code>&nbsp;<i>,d dummy-arg/</i> Draw a solid circle using the current fill color with diameter~<i>d</i> (integer in basic units~<code>u</code>) with leftmost point at the current position; then move the current position to the rightmost point of the circle. An optional second integer argument is ignored (this allows the formatter to generate an even number of arguments). This command is a <i>groff</i> extension.</p>
<dt> <code>Dc</code>&nbsp;<i>,d/</i></p>
<dd>Draw circle line with diameter~<i>d</i> (integer in basic units~<code>u</code>) with leftmost point at the current position; then move the current position to the rightmost point of the circle.</p>
<dt> <code>DE</code>&nbsp;<i>,h v/</i></p>
<dd>Draw a solid ellipse in the current fill color with a horizontal diameter of~<i>h</i> and a vertical diameter of~<i>v</i> (both integers in basic units~<code>u</code>) with the leftmost point at the current position; then move to the rightmost point of the ellipse. This command is a <i>groff</i> extension.</p>
<dt> <code>De</code>&nbsp;<i>,h v/</i></p>
<dd>Draw an outlined ellipse with a horizontal diameter of~<i>h</i> and a vertical diameter of~<i>v</i> (both integers in basic units~<code>u</code>) with the leftmost point at current position; then move to the rightmost point of the ellipse.</p>
<dt> <code>DF</code>&nbsp;<i>,color-scheme [component &#8230;]/</i></p>
<dd>Set fill color for solid drawing objects using different color schemes; the analogous command for setting the color of text, line graphics, and the outline of graphic objects is <code>m</code>. The color components are specified as integer arguments between 0 and @maxcolor]. The number of color components and their meaning vary for the different color schemes. These commands are generated by the <i>groff</i> escape sequences <code>D&#8217;F&nbsp;</code>&#8230;<code>&#8216;</code> and <code>M</code> (with no other corresponding graphics commands). No position changing. This command is a <i>groff</i> extension.</p>
<dl>
<dd>
<dl>
<dt> <code>DFc</code>&nbsp;<i>,cyan magenta yellow/</i></p>
<dd>Set fill color for solid drawing objects using the CMY color scheme, having the 3~color components cyan, magenta, and yellow.</p>
<dt> <code>DFd</code>&nbsp;<i>,/</i></p>
<dd>Set fill color for solid drawing objects to the default fill color value (black in most cases). No component arguments.</p>
<dt> <code>DFg</code>&nbsp;<i>,gray/</i></p>
<dd>Set fill color for solid drawing objects to the shade of gray given by the argument, an integer between 0 (black) and @maxcolor] (white).</p>
<dt> <code>DFk</code>&nbsp;<i>,cyan magenta yellow black/</i></p>
<dd>Set fill color for solid drawing objects using the CMYK color scheme, having the 4~color components cyan, magenta, yellow, and black.</p>
<dt> <code>DFr</code>&nbsp;<i>,red green blue/</i></p>
<dd>Set fill color for solid drawing objects using the RGB color scheme, having the 3~color components red, green, and blue.</dl>
</dl>
<dt> <code>Df</code>&nbsp;<i>,n/</i></p>
<dd>The argument <i>n</i> must be an integer in the range -32767 to 32767.</p>
<dl>
<dd>
<dl>
<dt>0&le;<i>n</i>&le;1000</p>
<dd>Set the color for filling solid drawing objects to a shade of gray, where 0 corresponds to solid white, 1000 (the default) to solid black, and values in between to intermediate shades of gray; this is obsoleted by command <code>DFg</code>.</p>
<dt><i>n</i>&lt;0 or <i>n</i>&gt;1000</p>
<dd>Set the filling color to the color that is currently being used for the text and the outline, see command <code>m</code>. For example, the command sequence</p>
<dl>
<dd>
<dl>
<dd>mg 0 0 @maxcolor] Df -1</dl>
</dl>
<dd>sets all colors to blue.</dl>
<p> No position changing. This command is a <i>groff</i> extension.</dl>
<dt> <code>Dl</code>&nbsp;<i>,h v/</i></p>
<dd>Draw line from current position to offset (<i>,h/</i>,&nbsp;<i>,v/</i>) (integers in basic units~<code>u</code>); then set current position to the end of the drawn line.</p>
<dt> <code>Dp</code>&nbsp; &#8230;</p>
<dd>Draw a polygon line from current position to offset (<i>,<i>h/</i><font SIZE="-3">1</font>/</i>,&nbsp;<i>,<i>v/</i><font SIZE="-3">1</font>/</i>), from there to offset (<i>,<i>h/</i><font SIZE="-3">2</font>/</i>,&nbsp;<i>,<i>v/</i><font SIZE="-3">2</font>/</i>), etc., up to offset (<i>,<i>h/</i><font SIZE="-3">n</font>/</i>,&nbsp;<i>,<i>v/</i><font SIZE="-3">n</font>/</i>), and from there back to the starting position. As the polygon is closed, the end of drawing is the starting point, so the position doesn&#8217;t change. This command is a <i>groff</i> extension.</p>
<dt> <code>DP</code>&nbsp; &#8230;</p>
<dd>The same macro as the corresponding <code>Dp</code> command with the same arguments, but draws a solid polygon in the current fill color rather than an outlined polygon. No position changing. This command is a <i>groff</i> extension.</p>
<dt> <code>Dt</code>&nbsp;<i>,n/</i></p>
<dd>Set the current line thickness to~<i>n</i> (an integer in basic units~<code>u</code>) if <i>n</i>&gt;0; if <i>n</i>=0 select the smallest available line thickness; if <i>n</i>&lt;0 set the line thickness proportional to the point size (this is the default before the first <code>Dt</code> command was specified). No position changing. This command is a <i>groff</i> extension.</dl>
<h3>Device Control Commands</h3>
<p>Each device control command starts with the letter <code>x</code> followed by a space character (optional or arbitrary space/:tab in <i>groff</i>) and a subcommand letter or word; each argument (if any) must be preceded by a <i>syntactical</i> <i>space</i>. All <code>x</code> commands are terminated by a <i>syntactical line break</i>; no device control command can be followed by another command on the same line (except a comment). </p>
<p> The subcommand is basically a single letter, but to increase readability, it can be written as a word, i.e., an arbitrary sequence of characters terminated by the next tab, space, or newline character. All characters of the subcommand word but the first are simply ignored. For example, <code>troff</code> outputs the initialization command <code>x i</code> as <code>x init</code> and the resolution command <code>x r</code> as <code>x res</code>. But writings like <code>x i_like_groff</code> and <code>x roff_is_groff</code> are accepted as well to mean the same commands. </p>
<p> In the following, the syntax element <i>&lt;line-break&gt;</i> means a <i>syntactical line break</i> as defined in subsection &#8220;Separation&#8221; above.</p>
<dl>
<dt> <code>xF</code>&nbsp;<i>name</i></p>
<dd>(<i>Filename</i> control command)<br />
 Use <i>name</i> as the intended name for the current file in error reports. This is useful for remembering the original file name when <code>groff</code> uses an internal piping mechanism. The input file is not changed by this command. This command is a <i>groff</i> extension.</p>
<dt> <code>xf</code>&nbsp;<i>n s</i></p>
<dd>(<i>font</i> control command)<br />
 Mount font position~<i>n</i> (a non-negative integer) with font named~<i>s</i> (a text word); see <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5).</p>
<dt> <code>xH</code>&nbsp;<i>n</i></p>
<dd>(<i>Height</i> control command)<br />
 Set character height to~<i>n</i> (a positive integer in scaled points~<code>z</code>). <i>Classical troff</i> used the unit points (<code>p</code>) instead; see section &#8220;Compatibility&#8221; below.</p>
<dt> <code>xi</code>&nbsp;<i></i></p>
<dd>(<i>init</i> control command)<br />
 Initialize device. This is the third command of the <i>prologue</i>.</p>
<dt> <code>xp</code>&nbsp;<i></i></p>
<dd>(<i>pause</i> control command)<br />
 Parsed but ignored. The classical documentation reads <i>pause device, can be</i> <i>restarted</i>.</p>
<dt> <code>xr</code>&nbsp;<i>n h v</i></p>
<dd>(<i>resolution</i> control command)<br />
 Resolution is~<i>n</i>, while <i>h</i> is the minimal horizontal motion, and <i>v</i> the minimal vertical motion possible with this device; all arguments are positive integers in basic units~<code>u</code> per inch. This is the second command of the <i>prologue</i>.</p>
<dt> <code>xS</code>&nbsp;<i>n</i></p>
<dd>(<i>Slant</i> control command)<br />
 Set slant to~<i>n</i> degrees (an integer in basic units~<code>u</code>).</p>
<dt> <code>xs</code>&nbsp;<i></i></p>
<dd>(<i>stop</i> control command)<br />
 Terminates the processing of the current file; issued as the last command of any <i>intermediate troff</i> <i>output</i>.</p>
<dt> <code>xt</code>&nbsp;<i></i></p>
<dd>(<i>trailer</i> control command)<br />
 Generate trailer information, if any. In <code>groff</code>, this is actually just ignored.</p>
<dt> <code>xT</code>&nbsp;<i>xxx</i></p>
<dd>(<i>Typesetter</i> control command)<br />
 Set name of device to word <i>xxx</i>, a sequence of characters ended by the next whitespace character. The possible device names coincide with those from the groff <code>-T</code> option. This is the first command of the <i>prologue</i>.</p>
<dt> <code>xu</code>&nbsp;<i>n</i></p>
<dd>(<i>underline</i> control command)<br />
 Configure underlining of spaces. If <i>n</i> is~1, start underlining of spaces; if <i>n</i> is~0, stop underlining of spaces. This is needed for the <code>cu</code> request in <code>nroff</code> mode and is ignored otherwise. This command is a <i>groff</i> extension.</p>
<dt> <code>xX</code>&nbsp;<i>anything</i></p>
<dd>(<i>X-escape</i> control command)<br />
 Send string <i>anything</i> uninterpreted to the device. If the line following this command starts with a <code>+</code> character this line is interpreted as a continuation line in the following sense. The <code>+</code> is ignored, but a newline character is sent instead to the device, the rest of the line is sent uninterpreted. The same applies to all following lines until the first character of a line is not a <code>+</code> character. This command is generated by the <i>groff</i> escape sequence <code>X</code>. The line-continuing feature is a <i>groff</i> extension.</dl>
<h3>Obsolete Command</h3>
<p>In <i>classical troff</i> output, emitting a single glyph was mostly done by a very strange command that combined a horizontal move and the printing of a glyph. It didn&#8217;t have a command code, but is represented by a 3-character argument consisting of exactly 2~digits and a character.</p>
<dl>
<dt><i>ddc</i></p>
<dd>Move right <i>dd</i> (exactly two decimal digits) basic units~<code>u</code>, then print glyph with single-letter name~<i>c</i>.</p>
<dl>
<dd>In <i>groff</i>, arbitrary <i>syntactical space</i> around and within this command is allowed to be added. Only when a preceding command on the same line ends with an argument of variable length a separating space is obligatory. In <i>classical</i> <i>troff</i>, large clusters of these and other commands were used, mostly without spaces; this made such output almost unreadable.</dl>
</dl>
<p> For modern high-resolution devices, this command does not make sense because the width of the glyphs can become much larger than two decimal digits. In <code>groff</code>, this is only used for the devices <code>X75</code>, <code>X75-12</code>, <code>X100</code>, and <code>X100-12</code>. For other devices, the commands <code>t</code> and~<code>u</code> provide a better functionality.</p>
<h2>Postprocessing</h2>
<p>The <i>roff</i> postprocessors are programs that have the task to translate the <i>intermediate output</i> into actions that are sent to a device. A device can be some piece of hardware such as a printer, or a software file format suitable for graphical or text processing. The <i>groff</i> system provides powerful means that make the programming of such postprocessors an easy task. </p>
<p> There is a library function that parses the <i>intermediate output</i> and sends the information obtained to the device via methods of a class with a common interface for each device. So a <i>groff</i> postprocessor must only redefine the methods of this class. For details, see the reference in section &#8220;Files&#8221; below.</p>
<h2>Examples</h2>
<p>This section presents the <i>intermediate output</i> generated from the same input for three different devices. The input is the sentence <i>hell world</i> fed into <code>groff</code> on the command line.</p>
<dl>
<dt>&bull;</p>
<dd>High-resolution device <i>ps</i></p>
<dl>
<dd><code>shell&gt;</code> echo &quot;hell world&quot; | groff -Z -T ps </p>
<pre>x T ps
x res 72000 1 1
x init
p1
x font 5 TR
f5
s10000
V12000
H72000
thell
wh2500
tw
H96620
torld
n12000 0
x trailer
V792000
x stop</pre>
</dl>
</dl>
<p> This output can be fed into the postprocessor <code><a href="/docs/linux/man/1-grops/">grops</a></code>(1) to get its representation as a PostScript file, or <code><a href="/docs/linux/man/1-gropdf/">gropdf</a></code>(1) to output directly to PDF.</p>
<dl>
<dt>&bull;</p>
<dd>Low-resolution device <i>latin1</i></p>
<dl>
<dd>This is similar to the high-resolution device except that the positioning is done at a minor scale. Some comments (lines starting with <i>#</i>) were added for clarification; they were not generated by the formatter. </p>
<p> <code>shell&gt;</code> &quot;hell world&quot; | groff -Z -T latin1 </p>
<pre><i># prologue</i>
x T latin1
x res 240 24 40
x init
<i># begin a new page</i>
p1
<i># font setup</i>
x font 1 R
f1
s10
<i># initial positioning on the page</i>
V40
H0
<i># write text 'hell'</i>
thell
<i># inform about a space, and do it by a horizontal jump</i>
wh24
<i># write text 'world'</i>
tworld
<i># announce line break, but do nothing because ...</i>
n40 0
<i># ... the end of the document has been reached</i>
x trailer
V2640
x stop</pre>
</dl>
</dl>
<p> This output can be fed into the postprocessor <code><a href="/docs/linux/man/1-grotty/">grotty</a></code>(1) to get a formatted text document.</p>
<dl>
<dt>&bull;</p>
<dd>Classical style output</p>
<dl>
<dd>As a computer monitor has a very low resolution compared to modern printers the <i>intermediate output</i> for the X~devices can use the jump-and-write command with its 2-digit displacements. </p>
<p> <code>shell&gt;</code> &quot;hell world&quot; | groff -Z -T X100 </p>
<pre>x T X100
x res 100 1 1
x init
p1
x font 5 TR
f5
s10
V16
H100
<i># write text with old-style jump-and-write command</i>
ch07e07l03lw06w11o07r05l03dh7
n16 0
x trailer
V1100
x stop</pre>
</dl>
</dl>
<p> This output can be fed into the postprocessor <code><a href="//www.systutorials.com/docs/linux/man/1x-xditview/">xditview</a></code>(1x) or <code><a href="/docs/linux/man/1-gxditview/">gxditview</a></code>(1) for displaying in~X. </p>
<p> Due to the obsolete jump-and-write command, the text clusters in the classical output are almost unreadable.</p>
<h2>Compatibility</h2>
<p>The <i>intermediate output</i> language of the <i>classical troff</i> was first documented in [CSTR~#97] . The <i>groff intermediate output</i> format is compatible with this specification except for the following features.</p>
<dl>
<dt>&bull;</p>
<dd>The classical quasi device independence is not yet implemented.</p>
<dt>&bull;</p>
<dd>The old hardware was very different from what we use today. So the <i>groff</i> devices are also fundamentally different from the ones in <i>classical</i> <i>troff</i>. For example, the classical PostScript device was called <i>post</i> and had a resolution of 720 units per inch, while <i>groff</i>&#8216;s <i>ps</i> device has a resolution of 72000 units per inch. Maybe, by implementing some rescaling mechanism similar to the classical quasi device independence, these could be integrated into modern <i>groff</i>.</p>
<dt>&bull;</p>
<dd>The B-spline command <code>D~</code> is correctly handled by the <i>intermediate output</i> parser, but the drawing routines aren&#8217;t implemented in some of the postprocessor programs.</p>
<dt>&bull;</p>
<dd>The argument of the commands <code>s</code> and <code>x H</code> has the implicit unit scaled point~<code>z</code> in <i>groff</i>, while <i>classical troff</i> had point (<code>p</code>). This isn&#8217;t an incompatibility, but a compatible extension, for both units coincide for all devices without a <i>sizescale</i> parameter, including all classical and the <i>groff</i> text devices. The few <i>groff</i> devices with a sizescale parameter either did not exist, had a different name, or seem to have had a different resolution. So conflicts with classical devices are very unlikely.</p>
<dt>&bull;</p>
<dd>Temporarily, there existed some confusion on the positioning after the <code>D</code> commands that are <i>groff</i> extensions. This has been clarified by establishing the classical rule for all groff drawing commands:</p>
<dl>
<dd><i> The position after a graphic object has been drawn is at its end; for circles and ellipses, the &quot;end&quot; is at the right side. </i></dl>
</dl>
<p> From this, the positionings specified for the drawing commands above follow quite naturally. </p>
<p> The differences between <i>groff</i> and <i>classical troff</i> are documented in <code><a href="/docs/linux/man/7-groff_diff/">groff_diff</a></code>(7).</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/:share/:groff/:1.22.4/:font/dev</i>name<i>/DESC</i></p>
<dd>Device description file for device <i>name</i>.</p>
<dt><i>src/libs/libdriver/input.cpp</i></p>
<dd>Defines the parser and postprocessor for the <i>intermediate</i> <i>output</i>. It is located relative to the top directory of the <i>groff</i> source tree. This parser is the definitive specification of the <i>groff intermediate output</i> format.</dl>
<h2>Authors</h2>
<p>James Clark wrote an early version of this document, which described only the differences between <code><a href="/docs/linux/man/7-ditroff/">ditroff</a></code>(7)&#8217;s output format and that of GNU <i>roff</i>. The present version was completely rewritten in 2001 by Bernd Warken</p>
<h2>See Also</h2>
<p>A reference like <code><a href="/docs/linux/man/7-groff/">groff</a></code>(7) refers to a manual page; here <code>groff</code> in section~<i>7</i> of the man page documentation system. To read the example, look up section~7 in your desktop help system or call from the shell prompt</p>
<dl>
<dd><code>shell&gt;</code> man 7 groff</dl>
<p> For more details, see <code><a href="/docs/linux/man/1-man/">man</a></code>(1).</p>
<dl>
<dt><code><a href="/docs/linux/man/1-groff/">groff</a></code>(1)</p>
<dd>option <code>-Z</code> and further readings on groff.</p>
<dt><code><a href="/docs/linux/man/7-groff/">groff</a></code>(7)</p>
<dd>for details of the <i>groff</i> language such as numerical units and escape sequences.</p>
<dt><code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5)</p>
<dd>for details on the device scaling parameters of the <i>DESC</i> file.</p>
<dt><code><a href="/docs/linux/man/1-troff/">troff</a></code>(1)</p>
<dd>generates the device-independent intermediate output.</p>
<dt><code><a href="/docs/linux/man/7-roff/">roff</a></code>(7)</p>
<dd>for historical aspects and the general structure of roff systems.</p>
<dt><code><a href="/docs/linux/man/7-groff_diff/">groff_diff</a></code>(7)</p>
<dd>The differences between the intermediate output in groff and classical troff.</p>
<dt><code><a href="/docs/linux/man/1-gxditview/">gxditview</a></code>(1)</p>
<dd>Viewer for the <i>intermediate</i> <i>output</i>.</dl>
<p> <code><a href="/docs/linux/man/1-grodvi/">grodvi</a></code>(1), <code><a href="/docs/linux/man/1-grohtml/">grohtml</a></code>(1), <code><a href="/docs/linux/man/1-grolbp/">grolbp</a></code>(1), <code><a href="/docs/linux/man/1-grolj4/">grolj4</a></code>(1), <code><a href="/docs/linux/man/1-grops/">grops</a></code>(1), <code><a href="/docs/linux/man/1-grotty/">grotty</a></code>(1) </p>
<dl>
<dd>the groff postprocessor programs.</dl>
<p> <i>Groff: The GNU Implementation of troff</i>, by Trent A. Fisher and Werner Lemberg, is the primary <i>groff</i> manual. You can browse it interactively with &#8220;info groff&#8221;. The <i>classical troff output language</i> is described in two AT&amp;T Bell Labs CSTR documents available on-line at Bell Labs CSTR site</p>
<dl>
<dt>[CSTR #97]</p>
<dd><i>A Typesetter-independent TROFF</i> by <i>Brian Kernighan</i> is the original and most comprehensive documentation on the output language; see CSTR~#97</p>
<dt>[CSTR~#54]</p>
<dd>The 1992 revision of the <i>Nroff/:Troff User&#8217;s Manual</i> by <i>J. F. Ossanna</i> and <i>Brian Kernighan</i> isn&#8217;t as comprehensive as [CSTR~#97] regarding the output language; see CSTR~#54 </p>
