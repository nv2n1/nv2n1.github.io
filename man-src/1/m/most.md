---
title: "most(1)"
name: "most"
section: "1"
letter: "m"
url: "/docs/linux/man/1-most/"
description: "most – browse or page through a text file"
---

<h2>NAME</h2>
<p> most &#8211; browse or page through a text file</p>
<h2>SYNOPSIS</h2>
<p> <code>most</code> [<code>-1bCcdMstuvwz</code>] [<code>+</code><i>lineno</i>] [<code>+c</code>] [<code>+d</code>] [<code>+s</code>] [<code>+u</code>] [<code>+/</code><i>string</i>] [<i>filename</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <i>most</i> is a paging program that displays, one windowful at a time, the contents of a file on a terminal. It pauses after each windowful and prints on the window status line the screen the file name, current line number, and the percentage of the file so far displayed. </p>
<p> Unlike other paging programs, <i>most</i> is capable of displaying an arbitrary number of windows as long as each window occupies at least two screen lines. Each window may contain the same file or a different file. In addition, each window has its own mode. For example, one window may display a file with its lines wrapped while another may be truncating the lines. Windows may be `locked&#8217; together in the sense that if one of the locked windows scrolls, all locked windows will scroll. <i>most</i> is also capable of ignoring lines that are indented beyond a user specified value. This is useful when viewing computer programs to pick out gross features of the code. See the `<code>:o</code>&#8216; command for a description of this feature. </p>
<p> In addition to displaying ordinary text files, <i>most</i> can also display binary files as well as files with arbitrary ascii characters. When a file is read into a buffer, <i>most</i> examines the first 32 bytes of the file to determine if the file is a binary file and then switches to the appropriate mode. However, this feature may be disabled with the <code>-k</code> option. See the description of the <code>-b</code>, <code>-k</code>, <code>-v</code>, and <code>-t</code> options for further details. </p>
<p> Text files may contain combinations of underscore and backspace characters causing a printer to underline or overstrike. When <i>most</i> recognizes this, it inserts the appropriate escape sequences to achieve the desired effect. In addition, some files cause the printer to overstrike some characters by embedding carriage return characters in the middle of a line. When this occurs, <i>most</i> displays the overstruck character with a bold attribute. This feature facilitates the reading of <font SIZE="-1">UNIX</font> man pages or a document produced by <i>runoff</i>. In particular, viewing this document with <i>most</i> should illustrate this behavior provided that the underline characters have not been stripped. This may be turned off with the <code>-v</code> option. </p>
<p> By default, lines with more characters than the terminal width are not wrapped but are instead truncated. When truncation occurs, this is indicated by a `$&#8217; in the far right column of the terminal screen. The RIGHT and LEFT arrow keys may be used to view lines which extend past the margins of the screen. The <code>-w</code> option may be used to override this feature. When a window is wrapped, the character `\&#8217; will appear at the right edge of the window. </p>
<p> Commands are listed below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-1</code></p>
<dd> VT100 mode. This is meaningful only on VMS systems. This option should be used if the terminal is strictly a VT100. This implies that the terminal does not have the ability to delete and insert multiple lines. VT102s and above have this ability.</p>
<dt><code>-b</code></p>
<dd> Binary mode. Use this switch when you want to view files containing 8 bit characters. <i>most</i> will display the file 16 bytes per line in hexadecimal notation. A typical line looks like:</p>
<dt>
<dd>
<pre>
01000000 40001575 9C23A020 4000168D     ....@..u.#. @...
</pre>
<dt>
<dd> When used with the <code>-v</code> option, the same line looks like:</p>
<dt>
<dd>
<pre>
^A^@^@^@  @^@^U u 9C #A0    @^@^V8D     ....@..u.#. @...
</pre>
<dt><code>-C</code></p>
<dd> Disable color support.</p>
<dt><code>-d</code></p>
<dd> Omit the backslash mark used to denote a wrapped line.</p>
<dt><code>-M</code></p>
<dd> Disable the use of mmap.</p>
<dt><code>-s</code></p>
<dd> Squeeze. Replace multiple blank lines with a single blank line.</p>
<dt><code>-z</code></p>
<dd> option turns off gunzip-on-the-fly.</p>
<dt><code>-v</code></p>
<dd> Display control characters as in `^A&#8217; for control A. Normally <i>most</i> does not interpret control characters.</p>
<dt><code>-t</code></p>
<dd> Display tabs as `^I&#8217;. This option is meaningful only when used with the <code>-v</code> option.</p>
<dt><code>+</code><i>lineno</i></p>
<dd> Start up at <i>lineno</i>.</p>
<dt><code>-c</code></p>
<dd> Make searches case sensitive. By default, they are not.</p>
<dt><code>-u</code></p>
<dd> Disable UTF-8 mode even if the locale dictates it.</p>
<dt><code>+u</code></p>
<dd> Force UTF-8 mode. By default most will use the current locale to determine if UTF-8 mode shoul be used. The <code>+u</code> and <code>-u</code> switches allow the behavior to be overridden.</p>
<dt><code>+d</code></p>
<dd> This switch should only be used if you want the option to delete a file while viewing it. This makes it easier to clean unwanted files out of a directory. The file is deleted with the interactive key sequence `<code>:D</code>&#8216; and then confirming with `<code>y</code>&#8216;.</p>
<dt><code>+/</code><i>string</i></p>
<dd> Start up at the line containing the first occurrence of <i>string</i>.</dl>
<h2>COMMAND USAGE</h2>
<p> The commands take effect immediately; it is not necessary to type a carriage return. </p>
<p> In the following commands, <i>i</i> is a numerical argument (1 by default).</p>
<dl>
<dt><code>SPACE</code>, <code>CTRL-D</code>, <code>NEXT_SCREEN</code></p>
<dd> Display another windowful, or jump <i>i</i> windowfuls if <i>i</i> is specified.</p>
<dt><code>RETURN</code>, <code>DOWN_ARROW</code>, <code>V</code>, <code>CTRL-N</code></p>
<dd> Display another line, or <i>i</i> more lines, if specified.</p>
<dt><code>UP_ARROW</code>, <code>^</code>, <code>CTRL-P</code></p>
<dd> Display previous line, or <i>i</i> previous lines, if specified.</p>
<dt><code>T</code>, <code>ESCAPE</code>&lt;</p>
<dd> Move to top of buffer.</p>
<dt><code>B</code>, <code>ESCAPE</code>&gt;</p>
<dd> Move to bottom of buffer.</p>
<dt><code>RIGHT_ARROW</code>, <code>TAB</code>, <code>&gt;</code></p>
<dd> Scroll window left 60<i>i</i> columns to view lines that are beyond the right margin of the window.</p>
<dt><code>LEFT_ARROW</code>, <code>CTRL-B</code>, <code>&lt;</code></p>
<dd> Scroll window right 60<i>i</i> columns to view lines that are beyond the left margin of the window.</p>
<dt><code>U</code>, <code>CTRL-U</code>, <code>DELETE</code>, <code>PREV_SCREEN</code></p>
<dd> Skip back <i>i</i> windowfuls and then print a windowful.</p>
<dt><code>R</code>, <code>CTRL-R</code></p>
<dd> Redraw the window.</p>
<dt><code>J</code>, <code>G</code></p>
<dd> If <i>i</i> is not specified, then prompt for a line number then jump to that line otherwise just jump to line <i>i</i>.</p>
<dt><code>%</code></p>
<dd> If <i>i</i> is not specified, then prompt for a percent number then jump to that percent of the file otherwise just jump to <i>i</i> percent of the file.</p>
<dt><code>W</code>, <code>w</code></p>
<dd> If the current screen width is 80, make it 132 and vice-versa. For other values, this command is ignored.</p>
<dt><code>Q</code>, <code>CTRL-X CTRL-C</code>, <code>CTRL-K E</code></p>
<dd> Exit from <i>most</i>. On VMS, ^Z also exits.</p>
<dt><code>h</code>, <code>CTRL-H</code>, <code>HELP</code>, <code>PF2</code></p>
<dd> Help. Give a description of all the <i>most</i> commands. The <i>most</i> environment variable <code>MOST_HELP</code> must be set for this to be meaningful.</p>
<dt><code>f</code>, <code>/</code>, <code>CTRL-F</code>, <code>FIND</code>, <code>GOLD PF3</code></p>
<dd> Prompt for a string and search forward from the current line for <i>i</i>th distinct line containing the string. <code>CTRL-G</code> aborts.</p>
<dt><code>?</code></p>
<dd> Prompt for a string and search backward for the <i>i</i>th distinct line containing the string. <code>CTRL-G</code> aborts.</p>
<dt><code>n</code></p>
<dd> Search for the next <i>i</i> lines containing an occurrence of the last search string in the direction of the previous search.</dl>
<p> <code>m</code>, <code>SELECT</code>, <code>CTRL-@</code>, <code>CTRL-K M</code>, <code>PERIOD</code></p>
<dl>
<dt>
<dd> Set a mark on the current line for later reference.</p>
<dt><code>INSERT_HERE, CTRL-X CTRL-X, COMMA, CTRL-K RETURN, GOLD PERIOD</code></p>
<dd> Set a mark on the current line but return to previous mark. This allows the user to toggle back and forth between two positions in the file.</p>
<dt><code>l</code>, <code>L</code></p>
<dd> Toggle locking for this window. The window is locked if there is a `*&#8217; at the left edge of the status line. Windows locked together, scroll together.</p>
<dt><code>CTRL-X 2</code>, <code>CTRL-W 2</code>, <code>GOLD X</code></p>
<dd> Split this window in half.</p>
<dt><code>CTRL-X o</code>, <code>CTRL-W o</code>, <code>o</code>, <code>GOLD</code>UP<code>, </code>GOLD<code>DOWN</code></p>
<dd> Move to other window.</p>
<dt><code>CTRL-X 0</code>, <code>CTRL-W 0</code>, <code>GOLD V</code></p>
<dd> Delete this window.</p>
<dt><code>CTRL-X 1</code>, <code>CTRL-W 1</code>, <code>GOLD O</code></p>
<dd> Delete all other windows, leaving only one window.</p>
<dt><code>E</code>, <code>e</code></p>
<dd> Edit this file.</p>
<dt><code>$</code>, <code>ESC $</code></p>
<dd> This is system dependent. On VMS, this causes <i>most</i> to spawn a subprocess. When the user exits the process, <i>most</i> is resumed. On <font SIZE="-1">UNIX</font> systems, <i>most</i> simply suspends itself.</p>
<dt><code>:n</code></p>
<dd> Skip to the next filename given in the command line. Use the arrow keys to scroll forward or backward through the file list. `<code>Q</code>&#8216; quits <i>most</i> and any other key selects the given file.</p>
<dt><code>:c</code></p>
<dd> Toggle case sensitive search.</p>
<dt><code>:D</code></p>
<dd> Delete current file. This command is only meaningful with the <code>+d</code> switch.</p>
<dt><code>:o</code>, <code>:O</code></p>
<dd> Toggle various options. With this key sequence, <i>most</i> displays a prompt asking the user to hit one of: <code>bdtvw</code>. The `<code>b</code>&#8216;, `<code>t</code>&#8216;, `<code>v</code>&#8216;, and `<code>w</code>&#8216; options have the same meaning as the command line switches. For example, the `<code>w</code>&#8216; option will toggle wrapping on and off for the current window.</p>
<dt>
<dd> The `<code>d</code>&#8216; option must be used with a prefix integer <i>i</i>. All lines indented beyond <i>i</i> columns will not be displayed. For example, consider the fragment:</p>
<dt>
<dd>
<pre><code>
int main(int argc, char **argv)
{
    int i;
    for (i = 0; i &lt; argc, i++) {
        fprintf(stdout, "%i: %s
", i, argv[i]);
    }
    return 0;
}
</code></pre>
<dt>
<dd> The key sequence `<code>1:od</code>&#8216; will cause <i>most</i> to display the file ignoring all lines indented beyond the first column. So for the example above, <i>most</i> would display:</p>
<dt>
<dd>
int main(int argc, char **argv)&#8230;<br />
}</p>
<dt>
<dd> where the `&#8230;&#8217; indicates lines follow are not displayed.</dl>
<h2>HINTS</h2>
<p> <code>CTRL-G</code> aborts the commands requiring the user to type something in at a prompt. The backquote key has a special meaning here. It is used to quote certain characters. This is useful when search for the occurrence of a string with a control character or a string at the beginning of a line. In the latter case, to find the occurrence of `The&#8217; at the beginning of a line, enter <code>`^JThe</code> where <code>`</code> quotes the <code>CTRL-J</code>.</p>
<h2>ENVIRONMENT</h2>
<p> <i>most</i> uses the following environment variables:</p>
<dl>
<dt><code>MOST_SWITCHES</code></p>
<dd> This variable sets commonly used switches. For example, some people prefer to use <i>most</i> with the <code>-s</code> option so that excess blank lines are not displayed. On VMS this is normally done done in the login.com through the line:</p>
<dt>
<dd>
<pre>
$ define MOST_SWITCHES &quot;-s&quot;
</pre>
<dt><code>MOST_EDITOR</code>, <code>SLANG_EDITOR</code></p>
<dd> Either of these environment variables specify an editor for <i>most</i> to invoke to edit a file. The value can contain %s and %d formatting descriptors that represent the file name and line number, respectively. For example, if JED is your editor, then set <code>MOST_EDITOR </code> to &#8216;jed %s -g %d&#8217;.</p>
<dt><code>MOST_HELP</code></p>
<dd> This variable may be used to specify an alternate help file.</p>
<dt><code>MOST_INITFILE</code></p>
<dd> Set this variable to specify the initialization file to load during startup. The default action is to load the system configuration file and then a personal configuration file called <i>.mostrc</i> on Unix, and <i>most.rc</i> on other systems.</dl>
<h2>CONFIGURATION FILE SYNTAX</h2>
<p> When most starts up, it tries to read a system configuration file and then a personal configuration file. These files may be used to specify keybindings and colors. </p>
<p> To bind a key to a particular function use the syntax: </p>
<p> <code>setkey function-name key-sequence</code> </p>
<p> The <i>setkey</i> command requires two arguments. The <i>function-name</i> argument specifies the function that is to be executed as a response to the keys specified by the <i>key-sequence </i> argument are pressed. For example, </p>
<p>setkey&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;up&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;^P&quot; </p>
<p> indicates that when <i>Ctrl-P</i> is pressed then the function <i>up</i> is to be executed. </p>
<p> Sometimes, it is necessary to first unbind a key-sequence before rebinding it in order via the <i>unsetkey</i> function: </p>
<p>&nbsp;<wbr>unsetkey&nbsp;<wbr>&quot;^F&quot; </p>
<p> Colors may be defined through the use of the <i>color</i> keyword in the the configuration file using the syntax: </p>
<p> <code>color OBJECT-NAME FOREGROUND-COLOR BACKGROUND-COLOR</code> </p>
<p> Here, OBJECT-NAME can be any one of the following items: </p>
<pre><code>
status-- the status line
    underline-- underlined text
        overstrike-- overstriked text
            normal-- anything else
</code></pre>
<p> See the sample configuration files for more information.</p>
<h2>BUGS</h2>
<p> Almost all of the known bugs or limitations of <i>most</i> are due to a desire to read and interpret control characters in files. One problem concerns the use of backspace characters to underscore or overstrike other characters. <i>most</i> makes an attempt to use terminal escape sequences to simulate this behavior. One side effect is the one does not always get what one expects when scrolling right and left through a file. When in doubt, use the <code>-v</code> and <code>-b</code> options of <i>most</i>. </p>
<h2>AUTHOR</h2>
<p> John E. Davis<br />
 davis [at] space.mit.edu</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> I would like to thank the users of <i>most</i> for valuable comments and criticisms. I would especially like to thank those individuals who have contributed code to <i>most.</i> </p>
<p> Mats Akerberg, Henk D. Davids, Rex O. Livingston, and Mark Pizzolato contributed to the early VMS versions of <i>most.</i> In particular, Mark worked on it to get it ready for DECUS. </p>
<p> Foteos Macrides &lt;MACRIDES [at] SCI.WFEB.EDU&gt; adapted <i>most</i> for use in <i>cswing</i> and <i>gopher.</i> A few features of the present version of <i>most</i> was inspired from his work. </p>
<p> I am grateful to Robert Mills &lt;robert [at] jna.com.au&gt; for re-writing the search routines to use regular expressions. </p>
<p> Sven Oliver Moll &lt;smol0075 [at] rz.uni-hildesheim.de&gt; came up with the idea of automatic detection of zipped files. </p>
<p> I would also like to thank Shinichi Hama for his valuable criticisms of <i>most.</i> </p>
<p> Javier Kohen was instrumental in the support for UTF-8. </p>
<p> Thanks to David W. Sanderson (dws [at] cs.wisc.edu) for adapting the documentation to nroff man page source format. </p>
<h2>Index</h2>
