---
title: "infocmp(1)"
name: "infocmp"
section: "1"
letter: "i"
url: "/docs/linux/man/1-infocmp/"
description: "infocmp – compare or print out terminfo descriptions"
---

<h2 class="name">NAME</h2>
<p> <code>infocmp</code> &#8211; compare or print out <i>terminfo</i> descriptions </p>
<h2>SYNOPSIS</h2>
<p> <code>infocmp</code> [<code>-1CDEFGIKLTUVWcdegilnpqrtux</code>] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-v</code>&nbsp;<i>n</i>]&nbsp;[<code>-s d</code>|&nbsp;<code>i</code>|&nbsp;<code>l</code>|&nbsp;<code>c</code>]&nbsp;[<code>-Q</code>&nbsp;<i>n</i>]&nbsp;[<code>-R&nbsp;</code><code>subset</code>] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-w</code>&nbsp;<i>width</i>]&nbsp;[<code>-A</code>&nbsp;<i>directory</i>]&nbsp;[<code>-B</code>&nbsp;<i>directory</i>] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<i>termname</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>infocmp</code> can be used to compare a binary <code>terminfo</code> entry with other terminfo entries, rewrite a <code>terminfo</code> description to take advantage of the <code>use=</code> terminfo field, or print out a <code>terminfo</code> description from the binary file (<code>term</code>) in a variety of formats. In all cases, the boolean fields will be printed first, followed by the numeric fields, followed by the string fields.</p>
<h3>Default Options</h3>
<p> If no options are specified and zero or one <i>termnames</i> are specified, the <code>-I</code> option will be assumed. If more than one <i>termname</i> is specified, the <code>-d</code> option will be assumed.</p>
<h3>Comparison Options [-d] [-c] [-n]</h3>
<p> <code>infocmp</code> compares the <code>terminfo</code> description of the first terminal <i>termname</i> with each of the descriptions given by the entries for the other terminal&#8217;s <i>termnames</i>. If a capability is defined for only one of the terminals, the value returned depends on the type of the capability:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>F</code> for missing boolean variables<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>NULL</code> for missing integer or string variables </p>
<p> Use the <code>-q</code> option to show the distinction between <i>absent</i> and <i>cancelled</i> capabilities. </p>
<p> These options produce a list which you can use to compare two or more terminal descriptions:</p>
<dl>
<dt><code>-d</code></p>
<dd> produces a list of each capability that is <i>different</i> between two entries. Each item in the list shows &#8220;:&#8221; after the capability name, followed by the capability values, separated by a comma.</p>
<dt><code>-c</code></p>
<dd> produces a list of each capability that is <i>common</i> between two or more entries. Missing capabilities are ignored. Each item in the list shows &#8220;=&#8221; after the capability name, followed by the capability value.</p>
<dt>
<dd> The <code>-u</code> option provides a related output, showing the first terminal description rewritten to use the second as a building block via the &#8220;use=&#8221; clause.</p>
<dt><code>-n</code></p>
<dd> produces a list of each capability that is in <i>none</i> of the given entries. Each item in the list shows &#8220;!&#8221; before the capability name.</p>
<dt>
<dd> Normally only the conventional capabilities are shown. Use the <code>-x</code> option to add the BSD-compatibility capabilities (names prefixed with &#8220;OT&#8221;).</p>
<dt>
<dd> If no <i>termnames</i> are given, <code>infocmp</code> uses the environment variable <code>TERM</code> for each of the <i>termnames</i>.</dl>
<h3>Source Listing Options [-I] [-L] [-C] [-r]</h3>
<p> The <code>-I</code>, <code>-L</code>, and <code>-C</code> options will produce a source listing for each terminal named. <center></p>
<table>
<tr VALIGN=top>
<td><code>-I</code></td>
<td>use the <code>terminfo</code> names
</td>
</tr>
<tr VALIGN=top>
<td><code>-L</code></td>
<td>use the long C variable name listed in &lt;<code>term.h</code>&gt;
</td>
</tr>
<tr VALIGN=top>
<td><code>-C</code></td>
<td>use the <code>termcap</code> names
</td>
</tr>
<tr VALIGN=top>
<td><code>-r</code></td>
<td>when using <code>-C</code>, put out all capabilities in <code>termcap</code> form
</td>
</tr>
<tr VALIGN=top>
<td><code>-K</code></td>
<td>modifies the <code>-C</code> option, improving BSD-compatibility.
</td>
</tr>
</table>
<p></center> </p>
<p> If no <i>termnames</i> are given, the environment variable <code>TERM</code> will be used for the terminal name. </p>
<p> The source produced by the <code>-C</code> option may be used directly as a <code>termcap</code> entry, but not all parameterized strings can be changed to the <code>termcap</code> format. <code>infocmp</code> will attempt to convert most of the parameterized information, and anything not converted will be plainly marked in the output and commented out. These should be edited by hand. </p>
<p> For best results when converting to <code>termcap</code> format, you should use both <code>-C</code> and <code>-r</code>. Normally a termcap description is limited to 1023 bytes. <code>infocmp</code> trims away less essential parts to make it fit. If you are converting to one of the (rare) termcap implementations which accept an unlimited size of termcap, you may want to add the <code>-T</code> option. More often however, you must help the termcap implementation, and trim excess whitespace (use the <code>-0</code> option for that). </p>
<p> All padding information for strings will be collected together and placed at the beginning of the string where <code>termcap</code> expects it. Mandatory padding (padding information with a trailing &#8220;/&#8221;) will become optional. </p>
<p> All <code>termcap</code> variables no longer supported by <code>terminfo</code>, but which are derivable from other <code>terminfo</code> variables, will be output. Not all <code>terminfo</code> capabilities will be translated; only those variables which were part of <code>termcap</code> will normally be output. Specifying the <code>-r</code> option will take off this restriction, allowing all capabilities to be output in <i>termcap</i> form. Normally you would use both the <code>-C</code> and <code>-r</code> options. The actual format used incorporates some improvements for escaped characters from terminfo format. For a stricter BSD-compatible translation, use the <code>-K</code> option rather than <code>-C</code>. </p>
<p> Note that because padding is collected to the beginning of the capability, not all capabilities are output. Mandatory padding is not supported. Because <code>termcap</code> strings are not as flexible, it is not always possible to convert a <code>terminfo</code> string capability into an equivalent <code>termcap</code> format. A subsequent conversion of the <code>termcap</code> file back into <code>terminfo</code> format will not necessarily reproduce the original <code>terminfo</code> source. </p>
<p> Some common <code>terminfo</code> parameter sequences, their <code>termcap</code> equivalents, and some terminal types which commonly have such sequences, are: <center></p>
<table>
<tr VALIGN=top>
<td><code>terminfo</code></td>
<td ALIGN=center>termcap</td>
<td>Representative Terminals
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>%p1%c</code></td>
<td>%.</td>
<td>adm
</td>
</tr>
<tr VALIGN=top>
<td><code>%p1%d</code></td>
<td>%d</td>
<td>hp, ANSI standard, vt100
</td>
</tr>
<tr VALIGN=top>
<td><code>%p1%&#8217;x&#8217;%+%c</code></td>
<td>%+x</td>
<td>concept
</td>
</tr>
<tr VALIGN=top>
<td><code>%i</code></td>
<td>%iq</td>
<td>ANSI standard, vt100
</td>
</tr>
<tr VALIGN=top>
<td><code>%p1%?%&#8217;x&#8217;%&gt;%t%p1%&#8217;y&#8217;%+%;</code></td>
<td>%&gt;xy</td>
<td>concept
</td>
</tr>
<tr VALIGN=top>
<td><code>%p2</code> is printed before <code>%p1</code></td>
<td>%r</td>
<td>hp
</td>
</tr>
</table>
<p></center></p>
<h3>Use= Option [-u]</h3>
<p> The <code>-u</code> option produces a <code>terminfo</code> source description of the first terminal <i>termname</i> which is relative to the sum of the descriptions given by the entries for the other terminals <i>termnames</i>. It does this by analyzing the differences between the first <i>termname</i> and the other <i>termnames</i> and producing a description with <code>use=</code> fields for the other terminals. In this manner, it is possible to retrofit generic terminfo entries into a terminal&#8217;s description. Or, if two similar terminals exist, but were coded at different times or by different people so that each description is a full description, using <code>infocmp</code> will show what can be done to change one description to be relative to the other. </p>
<p> A capability will be printed with an at-sign (@) if it no longer exists in the first <i>termname</i>, but one of the other <i>termname</i> entries contains a value for it. A capability&#8217;s value will be printed if the value in the first <i>termname</i> is not found in any of the other <i>termname</i> entries, or if the first of the other <i>termname</i> entries that has this capability gives a different value for the capability than that in the first <i>termname</i>. </p>
<p> The order of the other <i>termname</i> entries is significant. Since the terminfo compiler <code>tic</code> does a left-to-right scan of the capabilities, specifying two <code>use=</code> entries that contain differing entries for the same capabilities will produce different results depending on the order that the entries are given in. <code>infocmp</code> will flag any such inconsistencies between the other <i>termname</i> entries as they are found. </p>
<p> Alternatively, specifying a capability <i>after</i> a <code>use=</code> entry that contains that capability will cause the second specification to be ignored. Using <code>infocmp</code> to recreate a description can be a useful check to make sure that everything was specified correctly in the original source description. </p>
<p> Another error that does not cause incorrect compiled files, but will slow down the compilation time, is specifying extra <code>use=</code> fields that are superfluous. <code>infocmp</code> will flag any other <i>termname use=</i> fields that were not needed.</p>
<h3>Changing Databases [-A <i>directory</i>] [-B <i>directory</i>]</h3>
<p> Like other <code>ncurses</code> utilities, <code>infocmp</code> looks for the terminal descriptions in several places. You can use the <code>TERMINFO</code> and <code>TERMINFO_DIRS</code> environment variables to override the compiled-in default list of places to search (see <code><a href="//www.systutorials.com/docs/linux/man/3X-curses/">curses</a></code>(3X) for details). </p>
<p> You can also use the options <code>-A</code> and <code>-B</code> to override the list of places to search when comparing terminal descriptions:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The <code>-A</code> option sets the location for the first <i>termname</i><br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The <code>-B</code> option sets the location for the other <i>termnames</i>. </p>
<p> Using these options, it is possible to compare descriptions for a terminal with the same name located in two different databases. For instance, you can use this feature for comparing descriptions for the same terminal created by different people.</p>
<h3>Other Options</h3>
<dl>
<dt><code>-0</code></p>
<dd> causes the fields to be printed on one line, without wrapping.</p>
<dt><code>-1</code></p>
<dd> causes the fields to be printed out one to a line. Otherwise, the fields will be printed several to a line to a maximum width of 60 characters.</p>
<dt><code>-a</code></p>
<dd> tells <code>infocmp</code> to retain commented-out capabilities rather than discarding them. Capabilities are commented by prefixing them with a period.</p>
<dt><code>-D</code></p>
<dd> tells <code>infocmp</code> to print the database locations that it knows about, and exit.</p>
<dt><code>-E</code></p>
<dd> Dump the capabilities of the given terminal as tables, needed in the C initializer for a TERMTYPE structure (the terminal capability structure in the <code>&lt;term.h&gt;</code>). This option is useful for preparing versions of the curses library hardwired for a given terminal type. The tables are all declared static, and are named according to the type and the name of the corresponding terminal entry. </p>
<p> Before ncurses 5.0, the split between the <code>-e</code> and <code>-E</code> options was not needed; but support for extended names required making the arrays of terminal capabilities separate from the TERMTYPE structure.</p>
<dt><code>-e</code></p>
<dd> Dump the capabilities of the given terminal as a C initializer for a TERMTYPE structure (the terminal capability structure in the <code>&lt;term.h&gt;</code>). This option is useful for preparing versions of the curses library hardwired for a given terminal type.</p>
<dt><code>-F</code></p>
<dd> compare terminfo files. This assumes that two following arguments are filenames. The files are searched for pairwise matches between entries, with two entries considered to match if any of their names do. The report printed to standard output lists entries with no matches in the other file, and entries with more than one match. For entries with exactly one match it includes a difference report. Normally, to reduce the volume of the report, use references are not resolved before looking for differences, but resolution can be forced by also specifying <code>-r</code>.</p>
<dt><code>-f</code></p>
<dd> Display complex terminfo strings which contain if/then/else/endif expressions indented for readability.</p>
<dt><code>-G</code></p>
<dd> Display constant literals in decimal form rather than their character equivalents.</p>
<dt><code>-g</code></p>
<dd> Display constant character literals in quoted form rather than their decimal equivalents.</p>
<dt><code>-i</code></p>
<dd> Analyze the initialization (<code>is1</code>, <code>is2</code>, <code>is3</code>), and reset (<code>rs1</code>, <code>rs2</code>, <code>rs3</code>), strings in the entry, as well as those used for starting/stopping cursor-positioning mode (<code>smcup</code>, <code>rmcup</code>) as well as starting/stopping keymap mode (<code>smkx</code>, <code>rmkx</code>).</p>
<dt>
<dd> For each string, the code tries to analyze it into actions in terms of the other capabilities in the entry, certain X3.64/ISO 6429/ECMA-48 capabilities, and certain DEC VT-series private modes (the set of recognized special sequences has been selected for completeness over the existing terminfo database). Each report line consists of the capability name, followed by a colon and space, followed by a printable expansion of the capability string with sections matching recognized actions translated into {}-bracketed descriptions.</p>
<dt>
<dd> Here is a list of the DEC/ANSI special sequences recognized: <center></p>
<table>
<tr VALIGN=top>
<td>Action</td>
<td>Meaning
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>RIS</td>
<td>full reset
</td>
</tr>
<tr VALIGN=top>
<td>SC</td>
<td>save cursor
</td>
</tr>
<tr VALIGN=top>
<td>RC</td>
<td>restore cursor
</td>
</tr>
<tr VALIGN=top>
<td>LL</td>
<td>home-down
</td>
</tr>
<tr VALIGN=top>
<td>RSR</td>
<td>reset scroll region
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>DECSTR</td>
<td>soft reset (VT320)
</td>
</tr>
<tr VALIGN=top>
<td>S7C1T</td>
<td>7-bit controls (VT220)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>ISO DEC G0</td>
<td>enable DEC graphics for G0
</td>
</tr>
<tr VALIGN=top>
<td>ISO UK G0</td>
<td>enable UK chars for G0
</td>
</tr>
<tr VALIGN=top>
<td>ISO US G0</td>
<td>enable US chars for G0
</td>
</tr>
<tr VALIGN=top>
<td>ISO DEC G1</td>
<td>enable DEC graphics for G1
</td>
</tr>
<tr VALIGN=top>
<td>ISO UK G1</td>
<td>enable UK chars for G1
</td>
</tr>
<tr VALIGN=top>
<td>ISO US G1</td>
<td>enable US chars for G1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>DECPAM</td>
<td>application keypad mode
</td>
</tr>
<tr VALIGN=top>
<td>DECPNM</td>
<td>normal keypad mode
</td>
</tr>
<tr VALIGN=top>
<td>DECANSI</td>
<td>enter ANSI mode
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>ECMA[+-]AM</td>
<td>keyboard action mode
</td>
</tr>
<tr VALIGN=top>
<td>ECMA[+-]IRM</td>
<td>insert replace mode
</td>
</tr>
<tr VALIGN=top>
<td>ECMA[+-]SRM</td>
<td>send receive mode
</td>
</tr>
<tr VALIGN=top>
<td>ECMA[+-]LNM</td>
<td>linefeed mode
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>DEC[+-]CKM</td>
<td>application cursor keys
</td>
</tr>
<tr VALIGN=top>
<td>DEC[+-]ANM</td>
<td>set VT52 mode
</td>
</tr>
<tr VALIGN=top>
<td>DEC[+-]COLM</td>
<td>132-column mode
</td>
</tr>
<tr VALIGN=top>
<td>DEC[+-]SCLM</td>
<td>smooth scroll
</td>
</tr>
<tr VALIGN=top>
<td>DEC[+-]SCNM</td>
<td>reverse video mode
</td>
</tr>
<tr VALIGN=top>
<td>DEC[+-]OM</td>
<td>origin mode
</td>
</tr>
<tr VALIGN=top>
<td>DEC[+-]AWM</td>
<td>wraparound mode
</td>
</tr>
<tr VALIGN=top>
<td>DEC[+-]ARM</td>
<td>auto-repeat mode
</td>
</tr>
</table>
<p></center> </p>
<p> It also recognizes a SGR action corresponding to ANSI/ISO 6429/ECMA Set Graphics Rendition, with the values NORMAL, BOLD, UNDERLINE, BLINK, and REVERSE. All but NORMAL may be prefixed with</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 &#8220;+&#8221; (turn on) or<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 &#8220;-&#8221; (turn off).</dl>
<dt>
<dd> An SGR0 designates an empty highlight sequence (equivalent to {SGR:NORMAL}).</p>
<dt><code>-l</code></p>
<dd> Set output format to terminfo.</p>
<dt><code>-p</code></p>
<dd> Ignore padding specifications when comparing strings.</p>
<dt><code>-Q</code> <i>n</i></p>
<dd> Rather than show source in terminfo (text) format, print the compiled (binary) format in hexadecimal or base64 form, depending on the option&#8217;s value:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1</p>
<dd> hexadecimal</p>
<dt>2</p>
<dd> base64</p>
<dt>3</p>
<dd> hexadecimal and base64</dl>
</dl>
<dt>
<dd> For example, this prints the compiled terminfo value as a string which could be assigned to the <code>TERMINFO</code> environment variable:<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
infocmp -0 -q -Q2
</pre>
<p>&nbsp;.in -4</p>
<dt><code>-q</code></p>
<dd> This makes the output a little shorter:</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Make the comparison listing shorter by omitting subheadings, and using &#8220;-&#8221; for absent capabilities, &#8220;@&#8221; for canceled rather than &#8220;NULL&#8221;.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 However, show differences between absent and cancelled capabilities.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Omit the &#8220;Reconstructed from&#8221; comment for source listings.</dl>
<dt><code>-R</code><i>subset</i></p>
<dd> Restrict output to a given subset. This option is for use with archaic versions of terminfo like those on SVr1, Ultrix, or HP-UX that do not support the full set of SVR4/XSI Curses terminfo; and variants such as AIX that have their own extensions incompatible with SVr4/XSI.</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Available terminfo subsets are &#8220;SVr1&#8221;, &#8220;Ultrix&#8221;, &#8220;HP&#8221;, and &#8220;AIX&#8221;; see <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5) for details.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 You can also choose the subset &#8220;BSD&#8221; which selects only capabilities with termcap equivalents recognized by 4.4BSD. The <code>-C</code> option sets the &#8220;BSD&#8221; subset as a side-effect.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If you select any other value for <code>-R</code>, it is the same as no subset, i.e., all capabilities are used. The <code>-I</code> option likewise selects no subset as a side-effect.</dl>
<dt><code>-s </code><i>[d|i|l|c]</i></p>
<dd> The <code>-s</code> option sorts the fields within each type according to the argument below: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>d</code></p>
<dd> leave fields in the order that they are stored in the <i>terminfo</i> database.</p>
<dt><code>i</code></p>
<dd> sort by <i>terminfo</i> name.</p>
<dt><code>l</code></p>
<dd> sort by the long C variable name.</p>
<dt><code>c</code></p>
<dd> sort by the <i>termcap</i> name.</dl>
</dl>
<dt>
<dd> If the <code>-s</code> option is not given, the fields printed out will be sorted alphabetically by the <code>terminfo</code> name within each type, except in the case of the <code>-C</code> or the <code>-L</code> options, which cause the sorting to be done by the <code>termcap</code> name or the long C variable name, respectively.</p>
<dt><code>-T</code></p>
<dd> eliminates size-restrictions on the generated text. This is mainly useful for testing and analysis, since the compiled descriptions are limited (e.g., 1023 for termcap, 4096 for terminfo).</p>
<dt><code>-t</code></p>
<dd> tells <code>tic</code> to discard commented-out capabilities. Normally when translating from terminfo to termcap, untranslatable capabilities are commented-out.</p>
<dt><code>-U</code></p>
<dd> tells <code>infocmp</code> to not post-process the data after parsing the source file. This feature helps when comparing the actual contents of two source files, since it excludes the inferences that <code>infocmp</code> makes to fill in missing data.</p>
<dt><code>-V</code></p>
<dd> reports the version of ncurses which was used in this program, and exits.</p>
<dt><code>-v</code> <i>n</i></p>
<dd> prints out tracing information on standard error as the program runs.</p>
<dt>
<dd> The optional parameter <i>n</i> is a number from 1 to 10, inclusive, indicating the desired level of detail of information. If ncurses is built without tracing support, the optional parameter is ignored.</p>
<dt><code>-W</code></p>
<dd> By itself, the <code>-w</code> option will not force long strings to be wrapped. Use the <code>-W</code> option to do this.</p>
<dt><code>-w</code> <i>width</i></p>
<dd> changes the output to <i>width</i> characters.</p>
<dt><code>-x</code></p>
<dd> print information for user-defined capabilities (see <code><a href="/docs/linux/man/5-user_caps/">user_caps</a>(5)</code>. These are extensions to the terminfo repertoire which can be loaded using the <code>-x</code> option of <code>tic</code>.</dl>
<h2>FILES</h2>
<dl>
<dt>/etc/terminfo</p>
<dd> Compiled terminal description database.</dl>
<h2>HISTORY</h2>
<p> Although System V Release 2 provided a terminfo library, it had no documented tool for decompiling the terminal descriptions. Tony Hansen (AT&amp;T) wrote the first <code>infocmp</code> in early 1984, for System V Release 3. </p>
<p> Eric Raymond used the AT&amp;T documentation in 1995 to provide an equivalent <code>infocmp</code> for ncurses. In addition, he added a few new features such as:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 the <code>-e</code> option, to support <i>fallback</i> (compiled-in) terminal descriptions<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 the <code>-i</code> option, to help with analysis </p>
<p> Later, Thomas Dickey added the <code>-x</code> (user-defined capabilities) option, and the <code>-E</code> option to support fallback entries with user-defined capabilities. </p>
<p> For a complete list, see the <i>EXTENSIONS</i> section. </p>
<p> In 2010, Roy Marples provided an <code>infocmp</code> program for NetBSD. It is less capable than the SVr4 or ncurses versions (e.g., it lacks the sorting options documented in X/Open), but does include the <code>-x</code> option adapted from ncurses.</p>
<h2>PORTABILITY</h2>
<p> X/Open Curses, Issue 7 (2009) provides a description of <code>infocmp</code>. It does not mention the options used for converting to termcap format.</p>
<h2>EXTENSIONS</h2>
<p> The <code>-0</code>, <code>-1</code>, <code>-E</code>, <code>-F</code>, <code>-G</code>, <code>-Q</code>, <code>-R</code>, <code>-T</code>, <code>-V</code>, <code>-a</code>, <code>-e</code>, <code>-f</code>, <code>-g</code>, <code>-i</code>, <code>-l</code>, <code>-p</code>, <code>-q</code> and <code>-t</code> options are not supported in SVr4 curses. </p>
<p> SVr4 infocmp does not distinguish between absent and cancelled capabilities. Also, it shows missing integer capabilities as <code>-1</code> (the internal value used to represent missing integers). This implementation shows those as &#8220;NULL&#8221;, for consistency with missing strings. </p>
<p> The <code>-r</code> option&#8217;s notion of &#8220;termcap&#8221; capabilities is System V Release 4&#8217;s. Actual BSD curses versions will have a more restricted set. To see only the 4.4BSD set, use <code>-r</code> <code>-RBSD</code>.</p>
<h2>BUGS</h2>
<p> The <code>-F</code> option of <code><a href="/docs/linux/man/1-infocmp/">infocmp</a></code>(1) should be a <code><a href="/docs/linux/man/1-toe/">toe</a></code>(1) mode.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-captoinfo/">captoinfo</a></code>(1), <code><a href="/docs/linux/man/1-infotocap/">infotocap</a></code>(1), <code><a href="/docs/linux/man/1-tic/">tic</a></code>(1), <code><a href="/docs/linux/man/1-toe/">toe</a></code>(1), <code>ncurses</code>(3NCURSES), <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5). <code><a href="/docs/linux/man/5-user_caps/">user_caps</a></code>(5). </p>
<p> <a rel="nofollow" href="https://invisible-island.net/ncurses/tctest.html">https://invisible-island.net/ncurses/tctest.html</a> </p>
<p> This describes <code>ncurses</code> version 6.3 (patch 20211021).</p>
<h2>AUTHOR</h2>
<p> Eric S. Raymond &lt;esr [at] snark.thyrsus.com&gt; and<br />
 Thomas E. Dickey &lt;dickey [at] invisible-island.net&gt; </p>
<h2>Index</h2>
<dt><a href="#lbAK">FILES</a></p>
<dd>
<dt><a href="#lbAL">HISTORY</a></p>
<dd>
<dt><a href="#lbAM">PORTABILITY</a></p>
<dd>
<dt><a href="#lbAN">EXTENSIONS</a></p>
<dd>
<dt><a href="#lbAO">BUGS</a></p>
<dd>
<dt><a href="#lbAP">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAQ">AUTHOR</a></p>
<dd></dl>
