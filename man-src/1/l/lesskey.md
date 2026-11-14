---
title: "lesskey(1)"
name: "lesskey"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lesskey/"
description: "lesskey – specify key bindings for less"
---

<h2 class="name">NAME</h2>
<p> lesskey &#8211; specify key bindings for less </p>
<h2>SYNOPSIS (deprecated)</h2>
<p> <code>lesskey [-o output] [&#8211;] [input]</code><br />
 <code>lesskey [&#8211;output=output] [&#8211;] [input]</code><br />
 <code>lesskey -V</code><br />
 <code>lesskey &#8211;version</code></p>
<h2>SCOPE</h2>
<p> This document describes the format of the <i>lesskey</i> source file, which is used by <i>less</i> version 582 and later. In previous versions of <i>less</i>, a separate program called <i>lesskey</i> was used to compile the <i>lesskey </i> source file into a format understood by <i>less</i>. This compilation step is no longer required and the <i>lesskey</i> program is therefore deprecated although the file format remains supported by <i>less</i> itself. </p>
<h2>FILE FORMAT</h2>
<p> The input file consists of one or more <i>sections.</i> Each section starts with a line that identifies the type of section. Possible sections are:</p>
<dl>
<dt>#command</p>
<dd> Defines new command keys.</p>
<dt>#line-edit</p>
<dd> Defines new line-editing keys.</p>
<dt>#env</p>
<dd> Defines environment variables.</dl>
<p> Blank lines and lines which start with a pound sign (#) are ignored, except for the special section header lines.</p>
<h2>COMMAND SECTION</h2>
<p> The command section begins with the line </p>
<p> #command </p>
<p> If the command section is the first section in the file, this line may be omitted. The command section consists of lines of the form: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>string</i> &lt;whitespace&gt; <i>action</i> [extra-string] &lt;newline&gt;</p>
<p> Whitespace is any sequence of one or more spaces and/or tabs. The <i>string</i> is the command key(s) which invoke the action. The <i>string</i> may be a single command key, or a sequence of up to 15 keys. The <i>action</i> is the name of the less action, from the list below. The characters in the <i>string</i> may appear literally, or be prefixed by a caret to indicate a control key. A backslash followed by one to three octal digits may be used to specify a character by its octal value. A backslash followed by certain characters specifies input characters as follows:</p>
<dl>
<dt></p>
<dd> BACKSPACE</p>
<dt></p>
<dd> ESCAPE</p>
<dt>
</p>
<dd> NEWLINE</p>
<dt></p>
<dd> RETURN</p>
<dt>	</p>
<dd> TAB</p>
<dt>\ku</p>
<dd> UP ARROW</p>
<dt>\kd</p>
<dd> DOWN ARROW</p>
<dt>\kr</p>
<dd> RIGHT ARROW</p>
<dt>\kl</p>
<dd> LEFT ARROW</p>
<dt>\kU</p>
<dd> PAGE UP</p>
<dt>\kD</p>
<dd> PAGE DOWN</p>
<dt>\kh</p>
<dd> HOME</p>
<dt>\ke</p>
<dd> END</p>
<dt>\kx</p>
<dd> DELETE</dl>
<p> A backslash followed by any other character indicates that character is to be taken literally. Characters which must be preceded by backslash include caret, space, tab and the backslash itself. </p>
<p> An action may be followed by an &quot;extra&quot; string. When such a command is entered while running <i>less</i>, the action is performed, and then the extra string is parsed, just as if it were typed in to <i>less</i>. This feature can be used in certain cases to extend the functionality of a command. For example, see the &quot;{&quot; and &quot;:t&quot; commands in the example below. The extra string has a special meaning for the &quot;quit&quot; action: when <i>less</i> quits, the first character of the extra string is used as its exit status.</p>
<h2>EXAMPLE</h2>
<p> The following input file describes the set of default command keys used by less: </p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td>#command</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>forw-line
</td>
</tr>
<tr VALIGN=top>
<td>
</td>
<td>forw-line
</td>
</tr>
<tr VALIGN=top>
<td>e</td>
<td>forw-line
</td>
</tr>
<tr VALIGN=top>
<td>j</td>
<td>forw-line
</td>
</tr>
<tr VALIGN=top>
<td>\kd</td>
<td>forw-line
</td>
</tr>
<tr VALIGN=top>
<td>^E</td>
<td>forw-line
</td>
</tr>
<tr VALIGN=top>
<td>^N</td>
<td>forw-line
</td>
</tr>
<tr VALIGN=top>
<td>k</td>
<td>back-line
</td>
</tr>
<tr VALIGN=top>
<td>y</td>
<td>back-line
</td>
</tr>
<tr VALIGN=top>
<td>^Y</td>
<td>back-line
</td>
</tr>
<tr VALIGN=top>
<td>^K</td>
<td>back-line
</td>
</tr>
<tr VALIGN=top>
<td>^P</td>
<td>back-line
</td>
</tr>
<tr VALIGN=top>
<td>J</td>
<td>forw-line-force
</td>
</tr>
<tr VALIGN=top>
<td>K</td>
<td>back-line-force
</td>
</tr>
<tr VALIGN=top>
<td>Y</td>
<td>back-line-force
</td>
</tr>
<tr VALIGN=top>
<td>d</td>
<td>forw-scroll
</td>
</tr>
<tr VALIGN=top>
<td>^D</td>
<td>forw-scroll
</td>
</tr>
<tr VALIGN=top>
<td>u</td>
<td>back-scroll
</td>
</tr>
<tr VALIGN=top>
<td>^U</td>
<td>back-scroll
</td>
</tr>
<tr VALIGN=top>
<td>\40</td>
<td>forw-screen
</td>
</tr>
<tr VALIGN=top>
<td>f</td>
<td>forw-screen
</td>
</tr>
<tr VALIGN=top>
<td>^F</td>
<td>forw-screen
</td>
</tr>
<tr VALIGN=top>
<td>^V</td>
<td>forw-screen
</td>
</tr>
<tr VALIGN=top>
<td>\kD</td>
<td>forw-screen
</td>
</tr>
<tr VALIGN=top>
<td>b</td>
<td>back-screen
</td>
</tr>
<tr VALIGN=top>
<td>^B</td>
<td>back-screen
</td>
</tr>
<tr VALIGN=top>
<td>v</td>
<td>back-screen
</td>
</tr>
<tr VALIGN=top>
<td>\kU</td>
<td>back-screen
</td>
</tr>
<tr VALIGN=top>
<td>z</td>
<td>forw-window
</td>
</tr>
<tr VALIGN=top>
<td>w</td>
<td>back-window
</td>
</tr>
<tr VALIGN=top>
<td>\40</td>
<td>forw-screen-force
</td>
</tr>
<tr VALIGN=top>
<td>F</td>
<td>forw-forever
</td>
</tr>
<tr VALIGN=top>
<td>F</td>
<td>forw-until-hilite
</td>
</tr>
<tr VALIGN=top>
<td>R</td>
<td>repaint-flush
</td>
</tr>
<tr VALIGN=top>
<td>r</td>
<td>repaint
</td>
</tr>
<tr VALIGN=top>
<td>^R</td>
<td>repaint
</td>
</tr>
<tr VALIGN=top>
<td>^L</td>
<td>repaint
</td>
</tr>
<tr VALIGN=top>
<td>u</td>
<td>undo-hilite
</td>
</tr>
<tr VALIGN=top>
<td>U</td>
<td>clear-search
</td>
</tr>
<tr VALIGN=top>
<td>g</td>
<td>goto-line
</td>
</tr>
<tr VALIGN=top>
<td>\kh</td>
<td>goto-line
</td>
</tr>
<tr VALIGN=top>
<td>&lt;</td>
<td>goto-line
</td>
</tr>
<tr VALIGN=top>
<td>&lt;</td>
<td>goto-line
</td>
</tr>
<tr VALIGN=top>
<td>p</td>
<td>percent
</td>
</tr>
<tr VALIGN=top>
<td>%</td>
<td>percent
</td>
</tr>
<tr VALIGN=top>
<td>[</td>
<td>left-scroll
</td>
</tr>
<tr VALIGN=top>
<td>]</td>
<td>right-scroll
</td>
</tr>
<tr VALIGN=top>
<td>(</td>
<td>left-scroll
</td>
</tr>
<tr VALIGN=top>
<td>)</td>
<td>right-scroll
</td>
</tr>
<tr VALIGN=top>
<td>\kl</td>
<td>left-scroll
</td>
</tr>
<tr VALIGN=top>
<td>\kr</td>
<td>right-scroll
</td>
</tr>
<tr VALIGN=top>
<td>{</td>
<td>no-scroll
</td>
</tr>
<tr VALIGN=top>
<td>}</td>
<td>end-scroll
</td>
</tr>
<tr VALIGN=top>
<td>{</td>
<td>forw-bracket {}
</td>
</tr>
<tr VALIGN=top>
<td>}</td>
<td>back-bracket {}
</td>
</tr>
<tr VALIGN=top>
<td>(</td>
<td>forw-bracket ()
</td>
</tr>
<tr VALIGN=top>
<td>)</td>
<td>back-bracket ()
</td>
</tr>
<tr VALIGN=top>
<td>[</td>
<td>forw-bracket []
</td>
</tr>
<tr VALIGN=top>
<td>]</td>
<td>back-bracket []
</td>
</tr>
<tr VALIGN=top>
<td>^F</td>
<td>forw-bracket
</td>
</tr>
<tr VALIGN=top>
<td>^B</td>
<td>back-bracket
</td>
</tr>
<tr VALIGN=top>
<td>G</td>
<td>goto-end
</td>
</tr>
<tr VALIGN=top>
<td>&gt;</td>
<td>goto-end
</td>
</tr>
<tr VALIGN=top>
<td>&gt;</td>
<td>goto-end
</td>
</tr>
<tr VALIGN=top>
<td>\ke</td>
<td>goto-end
</td>
</tr>
<tr VALIGN=top>
<td>G</td>
<td>goto-end-buffered
</td>
</tr>
<tr VALIGN=top>
<td>=</td>
<td>status
</td>
</tr>
<tr VALIGN=top>
<td>^G</td>
<td>status
</td>
</tr>
<tr VALIGN=top>
<td>:f</td>
<td>status
</td>
</tr>
<tr VALIGN=top>
<td>/</td>
<td>forw-search
</td>
</tr>
<tr VALIGN=top>
<td>?</td>
<td>back-search
</td>
</tr>
<tr VALIGN=top>
<td>/</td>
<td>forw-search *
</td>
</tr>
<tr VALIGN=top>
<td>?</td>
<td>back-search *
</td>
</tr>
<tr VALIGN=top>
<td>n</td>
<td>repeat-search
</td>
</tr>
<tr VALIGN=top>
<td>n</td>
<td>repeat-search-all
</td>
</tr>
<tr VALIGN=top>
<td>N</td>
<td>reverse-search
</td>
</tr>
<tr VALIGN=top>
<td>N</td>
<td>reverse-search-all
</td>
</tr>
<tr VALIGN=top>
<td>&amp;</td>
<td>filter
</td>
</tr>
<tr VALIGN=top>
<td>m</td>
<td>set-mark
</td>
</tr>
<tr VALIGN=top>
<td>M</td>
<td>set-mark-bottom
</td>
</tr>
<tr VALIGN=top>
<td>m</td>
<td>clear-mark
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>goto-mark
</td>
</tr>
<tr VALIGN=top>
<td>^X^X</td>
<td>goto-mark
</td>
</tr>
<tr VALIGN=top>
<td>E</td>
<td>examine
</td>
</tr>
<tr VALIGN=top>
<td>:e</td>
<td>examine
</td>
</tr>
<tr VALIGN=top>
<td>^X^V</td>
<td>examine
</td>
</tr>
<tr VALIGN=top>
<td>:n</td>
<td>next-file
</td>
</tr>
<tr VALIGN=top>
<td>:p</td>
<td>prev-file
</td>
</tr>
<tr VALIGN=top>
<td>t</td>
<td>next-tag
</td>
</tr>
<tr VALIGN=top>
<td>T</td>
<td>prev-tag
</td>
</tr>
<tr VALIGN=top>
<td>:x</td>
<td>index-file
</td>
</tr>
<tr VALIGN=top>
<td>:d</td>
<td>remove-file
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;</td>
<td>toggle-option
</td>
</tr>
<tr VALIGN=top>
<td>:t</td>
<td>toggle-option t
</td>
</tr>
<tr VALIGN=top>
<td>s</td>
<td>toggle-option o
</td>
</tr>
<tr VALIGN=top>
<td>_</td>
<td>display-option
</td>
</tr>
<tr VALIGN=top>
<td>|</td>
<td>pipe
</td>
</tr>
<tr VALIGN=top>
<td>v</td>
<td>visual
</td>
</tr>
<tr VALIGN=top>
<td>!</td>
<td>shell
</td>
</tr>
<tr VALIGN=top>
<td>+</td>
<td>firstcmd
</td>
</tr>
<tr VALIGN=top>
<td>H</td>
<td>help
</td>
</tr>
<tr VALIGN=top>
<td>h</td>
<td>help
</td>
</tr>
<tr VALIGN=top>
<td>V</td>
<td>version
</td>
</tr>
<tr VALIGN=top>
<td>0</td>
<td>digit
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td>digit
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td>digit
</td>
</tr>
<tr VALIGN=top>
<td>3</td>
<td>digit
</td>
</tr>
<tr VALIGN=top>
<td>4</td>
<td>digit
</td>
</tr>
<tr VALIGN=top>
<td>5</td>
<td>digit
</td>
</tr>
<tr VALIGN=top>
<td>6</td>
<td>digit
</td>
</tr>
<tr VALIGN=top>
<td>7</td>
<td>digit
</td>
</tr>
<tr VALIGN=top>
<td>8</td>
<td>digit
</td>
</tr>
<tr VALIGN=top>
<td>9</td>
<td>digit
</td>
</tr>
<tr VALIGN=top>
<td>q</td>
<td>quit
</td>
</tr>
<tr VALIGN=top>
<td>Q</td>
<td>quit
</td>
</tr>
<tr VALIGN=top>
<td>:q</td>
<td>quit
</td>
</tr>
<tr VALIGN=top>
<td>:Q</td>
<td>quit
</td>
</tr>
<tr VALIGN=top>
<td>ZZ</td>
<td>quit
</td>
</tr>
</table>
</dl>
<h2>PRECEDENCE</h2>
<p> Commands specified by <i>lesskey</i> take precedence over the default commands. A default command key may be disabled by including it in the input file with the action &quot;invalid&quot;. Alternatively, a key may be defined to do nothing by using the action &quot;noaction&quot;. &quot;noaction&quot; is similar to &quot;invalid&quot;, but <i>less</i> will give an error beep for an &quot;invalid&quot; command, but not for a &quot;noaction&quot; command. In addition, ALL default commands may be disabled by adding this control line to the input file: </p>
<p> #stop </p>
<p> This will cause all default commands to be ignored. The #stop line should be the last line in that section of the file. </p>
<p> Be aware that #stop can be dangerous. Since all default commands are disabled, you must provide sufficient commands before the #stop line to enable all necessary actions. For example, failure to provide a &quot;quit&quot; command can lead to frustration.</p>
<h2>LINE EDITING SECTION</h2>
<p> The line-editing section begins with the line: </p>
<p> #line-edit </p>
<p> This section specifies new key bindings for the line editing commands, in a manner similar to the way key bindings for ordinary commands are specified in the #command section. The line-editing section consists of a list of keys and actions, one per line as in the example below.</p>
<h2>EXAMPLE</h2>
<p> The following input file describes the set of default line-editing keys used by less: </p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td>#line-edit</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>	</td>
<td>forw-complete
</td>
</tr>
<tr VALIGN=top>
<td>\17</td>
<td>back-complete
</td>
</tr>
<tr VALIGN=top>
<td>	</td>
<td>back-complete
</td>
</tr>
<tr VALIGN=top>
<td>^L</td>
<td>expand
</td>
</tr>
<tr VALIGN=top>
<td>^V</td>
<td>literal
</td>
</tr>
<tr VALIGN=top>
<td>^A</td>
<td>literal
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>right
</td>
</tr>
<tr VALIGN=top>
<td>\kr</td>
<td>right
</td>
</tr>
<tr VALIGN=top>
<td>h</td>
<td>left
</td>
</tr>
<tr VALIGN=top>
<td>\kl</td>
<td>left
</td>
</tr>
<tr VALIGN=top>
<td>b</td>
<td>word-left
</td>
</tr>
<tr VALIGN=top>
<td>\kl</td>
<td>word-left
</td>
</tr>
<tr VALIGN=top>
<td>w</td>
<td>word-right
</td>
</tr>
<tr VALIGN=top>
<td>\kr</td>
<td>word-right
</td>
</tr>
<tr VALIGN=top>
<td>i</td>
<td>insert
</td>
</tr>
<tr VALIGN=top>
<td>x</td>
<td>delete
</td>
</tr>
<tr VALIGN=top>
<td>\kx</td>
<td>delete
</td>
</tr>
<tr VALIGN=top>
<td>X</td>
<td>word-delete
</td>
</tr>
<tr VALIGN=top>
<td>kx</td>
<td>word-delete
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>word-backspace
</td>
</tr>
<tr VALIGN=top>
<td>0</td>
<td>home
</td>
</tr>
<tr VALIGN=top>
<td>\kh</td>
<td>home
</td>
</tr>
<tr VALIGN=top>
<td>$</td>
<td>end
</td>
</tr>
<tr VALIGN=top>
<td>\ke</td>
<td>end
</td>
</tr>
<tr VALIGN=top>
<td>k</td>
<td>up
</td>
</tr>
<tr VALIGN=top>
<td>\ku</td>
<td>up
</td>
</tr>
<tr VALIGN=top>
<td>j</td>
<td>down
</td>
</tr>
<tr VALIGN=top>
<td>^G</td>
<td>abort
</td>
</tr>
</table>
</dl>
<h2>LESS ENVIRONMENT VARIABLES</h2>
<p> The environment variable section begins with the line </p>
<p> #env </p>
<p> Following this line is a list of environment variable assignments. Each line consists of an environment variable name, an equals sign (=) and the value to be assigned to the environment variable. White space before and after the equals sign is ignored. Variables assigned in this way are visible only to <i>less</i>. If a variable is specified in the system environment and also in a lesskey file, the value in the lesskey file takes precedence. Although the lesskey file can be used to override variables set in the environment, the main purpose of assigning variables in the lesskey file is simply to have all <i>less</i> configuration information stored in one file.</p>
<h2>EXAMPLE</h2>
<p> The following input file sets the -i option whenever <i>less</i> is run, and specifies the character set to be &quot;latin1&quot;: </p>
<pre>
        #env
        LESS = -i
        LESSCHARSET = latin1
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-less/">less</a></code>(1)</p>
<h2>WARNINGS</h2>
<p> On MS-DOS and OS/2 systems, certain keys send a sequence of characters which start with a NUL character (0). This NUL character should be represented as \340 in a lesskey file.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1984-2021 Mark Nudelman </p>
<p> less is part of the GNU project and is free software. You can redistribute it and/or modify it under the terms of either (1) the GNU General Public License as published by the Free Software Foundation; or (2) the Less License. See the file README in the less distribution for more details regarding redistribution. You should have received a copy of the GNU General Public License along with the source for less; see the file COPYING. If not, write to the Free Software Foundation, 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA. You should also have received a copy of the Less License; see the file LICENSE. </p>
<p> less is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.</p>
<h2>AUTHOR</h2>
<p> Mark Nudelman<br />
 Report bugs at <a rel="nofollow" href="https://github.com/gwsw/less/issues.">https://github.com/gwsw/less/issues.</a> </p>
<h2>Index</h2>
