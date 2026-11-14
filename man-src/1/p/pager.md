---
title: "pager(1)"
name: "pager"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pager/"
description: "less – opposite of more"
---

<h2 class="name">NAME</h2>
<p> less &#8211; opposite of more </p>
<h2>SYNOPSIS</h2>
<p> <code>less -?</code><br />
 <code>less &#8211;help</code><br />
 <code>less -V</code><br />
 <code>less &#8211;version</code><br />
 <code>less [-[+]aABcCdeEfFgGiIJKLmMnNqQrRsSuUVwWX~]</code><br />
 <code> [-b </code><i>space/</i>] [-h <i>lines/</i>] [-j <i>line/</i>] [-k <i>keyfile/</i>]<br />
 <code> [-{oO} </code><i>logfile/</i>] [-p <i>pattern/</i>] [-P <i>prompt/</i>] [-t <i>tag/</i>]<br />
 <code> [-T </code><i>tagsfile/</i>] [-x <i>tab/</i>,&#8230;] [-y <i>lines/</i>] [-[z] <i>lines/</i>]<br />
 <code> [-# </code><i>shift/</i>] [+[+]<i>cmd/</i>] [&#8211;] [<i>filename/</i>]&#8230;<br />
 (See the OPTIONS section for alternate option syntax with long option names.)</p>
<h2>DESCRIPTION</h2>
<p> <i>Less</i> is a program similar to <i><a href="/docs/linux/man/1-more/">more</a></i>(1), but it has many more features. <i>Less</i> does not have to read the entire input file before starting, so with large input files it starts up faster than text editors like <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1). <i>Less</i> uses termcap (or terminfo on some systems), so it can run on a variety of terminals. There is even limited support for hardcopy terminals. (On a hardcopy terminal, lines which should be printed at the top of the screen are prefixed with a caret.) </p>
<p> Commands are based on both <i>more</i> and <i>vi</i>. Commands may be preceded by a decimal number, called N in the descriptions below. The number is used by some commands, as indicated.</p>
<h2>COMMANDS</h2>
<p> In the following descriptions, ^X means control-X. ESC stands for the ESCAPE key; for example ESC-v means the two character sequence &quot;ESCAPE&quot;, then &quot;v&quot;.</p>
<dl>
<dt>h or H</p>
<dd> Help: display a summary of these commands. If you forget all the other commands, remember this one.</p>
<dt>SPACE or ^V or f or ^F</p>
<dd> Scroll forward N lines, default one window (see option -z below). If N is more than the screen size, only the final screenful is displayed. Warning: some systems use ^V as a special literalization character.</p>
<dt>z</p>
<dd> Like SPACE, but if N is specified, it becomes the new window size.</p>
<dt>ESC-SPACE</p>
<dd> Like SPACE, but scrolls a full screenful, even if it reaches end-of-file in the process.</p>
<dt>ENTER or RETURN or ^N or e or ^E or j or ^J</p>
<dd> Scroll forward N lines, default 1. The entire N lines are displayed, even if N is more than the screen size.</p>
<dt>d or ^D</p>
<dd> Scroll forward N lines, default one half of the screen size. If N is specified, it becomes the new default for subsequent d and u commands.</p>
<dt>b or ^B or ESC-v</p>
<dd> Scroll backward N lines, default one window (see option -z below). If N is more than the screen size, only the final screenful is displayed.</p>
<dt>w</p>
<dd> Like ESC-v, but if N is specified, it becomes the new window size.</p>
<dt>y or ^Y or ^P or k or ^K</p>
<dd> Scroll backward N lines, default 1. The entire N lines are displayed, even if N is more than the screen size. Warning: some systems use ^Y as a special job control character.</p>
<dt>u or ^U</p>
<dd> Scroll backward N lines, default one half of the screen size. If N is specified, it becomes the new default for subsequent d and u commands.</p>
<dt>J</p>
<dd> Like j, but continues to scroll beyond the end of the file.</p>
<dt>K or Y</p>
<dd> Like k, but continues to scroll beyond the beginning of the file.</p>
<dt>ESC-) or RIGHTARROW</p>
<dd> Scroll horizontally right N characters, default half the screen width (see the -# option). If a number N is specified, it becomes the default for future RIGHTARROW and LEFTARROW commands. While the text is scrolled, it acts as though the -S option (chop lines) were in effect.</p>
<dt>ESC-( or LEFTARROW</p>
<dd> Scroll horizontally left N characters, default half the screen width (see the -# option). If a number N is specified, it becomes the default for future RIGHTARROW and LEFTARROW commands.</p>
<dt>ESC-} or ^RIGHTARROW</p>
<dd> Scroll horizontally right to show the end of the longest displayed line.</p>
<dt>ESC-{ or ^LEFTARROW</p>
<dd> Scroll horizontally left back to the first column.</p>
<dt>r or ^R or ^L</p>
<dd> Repaint the screen.</p>
<dt>R</p>
<dd> Repaint the screen, discarding any buffered input. That is, reload the current file. Useful if the file is changing while it is being viewed.</p>
<dt>F</p>
<dd> Scroll forward, and keep trying to read when the end of file is reached. Normally this command would be used when already at the end of the file. It is a way to monitor the tail of a file which is growing while it is being viewed. (The behavior is similar to the &quot;tail -f&quot; command.) To stop waiting for more data, enter the interrupt character (usually ^C). On some systems you can also use ^X.</p>
<dt>ESC-F</p>
<dd> Like F, but as soon as a line is found which matches the last search pattern, the terminal bell is rung and forward scrolling stops.</p>
<dt>g or &lt; or ESC-&lt;</p>
<dd> Go to line N in the file, default 1 (beginning of file). (Warning: this may be slow if N is large.)</p>
<dt>G or &gt; or ESC-&gt;</p>
<dd> Go to line N in the file, default the end of the file. (Warning: this may be slow if N is large, or if N is not specified and standard input, rather than a file, is being read.)</p>
<dt>ESC-G</p>
<dd> Same as G, except if no number N is specified and the input is standard input, goes to the last line which is currently buffered.</p>
<dt>p or %</p>
<dd> Go to a position N percent into the file. N should be between 0 and 100, and may contain a decimal point.</p>
<dt>P</p>
<dd> Go to the line containing byte offset N in the file.</p>
<dt>{</p>
<dd> If a left curly bracket appears in the top line displayed on the screen, the { command will go to the matching right curly bracket. The matching right curly bracket is positioned on the bottom line of the screen. If there is more than one left curly bracket on the top line, a number N may be used to specify the N-th bracket on the line.</p>
<dt>}</p>
<dd> If a right curly bracket appears in the bottom line displayed on the screen, the } command will go to the matching left curly bracket. The matching left curly bracket is positioned on the top line of the screen. If there is more than one right curly bracket on the top line, a number N may be used to specify the N-th bracket on the line.</p>
<dt>(</p>
<dd> Like {, but applies to parentheses rather than curly brackets.</p>
<dt>)</p>
<dd> Like }, but applies to parentheses rather than curly brackets.</p>
<dt>[</p>
<dd> Like {, but applies to square brackets rather than curly brackets.</p>
<dt>]</p>
<dd> Like }, but applies to square brackets rather than curly brackets.</p>
<dt>ESC-^F</p>
<dd> Followed by two characters, acts like {, but uses the two characters as open and close brackets, respectively. For example, &quot;ESC ^F &lt; &gt;&quot; could be used to go forward to the &gt; which matches the &lt; in the top displayed line.</p>
<dt>ESC-^B</p>
<dd> Followed by two characters, acts like }, but uses the two characters as open and close brackets, respectively. For example, &quot;ESC ^B &lt; &gt;&quot; could be used to go backward to the &lt; which matches the &gt; in the bottom displayed line.</p>
<dt>m</p>
<dd> Followed by any lowercase or uppercase letter, marks the first displayed line with that letter. If the status column is enabled via the -J option, the status column shows the marked line.</p>
<dt>M</p>
<dd> Acts like m, except the last displayed line is marked rather than the first displayed line.</p>
<dt>&#8216;</p>
<dd> (Single quote.) Followed by any lowercase or uppercase letter, returns to the position which was previously marked with that letter. Followed by another single quote, returns to the position at which the last &quot;large&quot; movement command was executed. Followed by a ^ or $, jumps to the beginning or end of the file respectively. Marks are preserved when a new file is examined, so the &#8216; command can be used to switch between input files.</p>
<dt>^X^X</p>
<dd> Same as single quote.</p>
<dt>ESC-m</p>
<dd> Followed by any lowercase or uppercase letter, clears the mark identified by that letter.</p>
<dt>/pattern</p>
<dd> Search forward in the file for the N-th line containing the pattern. N defaults to 1. The pattern is a regular expression, as recognized by the regular expression library supplied by your system. The search starts at the first line displayed (but see the -a and -j options, which change this). </p>
<p> Certain characters are special if entered at the beginning of the pattern; they modify the type of search rather than become part of the pattern:</p>
<dl>
<dt>
<dd>
<dl>
<dt>^N or !</p>
<dd> Search for lines which do NOT match the pattern.</p>
<dt>^E or *</p>
<dd> Search multiple files. That is, if the search reaches the END of the current file without finding a match, the search continues in the next file in the command line list.</p>
<dt>^F or @</p>
<dd> Begin the search at the first line of the FIRST file in the command line list, regardless of what is currently displayed on the screen or the settings of the -a or -j options.</p>
<dt>^K</p>
<dd> Highlight any text which matches the pattern on the current screen, but don&#8217;t move to the first match (KEEP current position).</p>
<dt>^R</p>
<dd> Don&#8217;t interpret regular expression metacharacters; that is, do a simple textual comparison.</p>
<dt>^W</p>
<dd> WRAP around the current file. That is, if the search reaches the end of the current file without finding a match, the search continues from the first line of the current file up to the line where it started.</dl>
</dl>
<dt>?pattern</p>
<dd> Search backward in the file for the N-th line containing the pattern. The search starts at the last line displayed (but see the -a and -j options, which change this). </p>
<p> Certain characters are special as in the / command:</p>
<dl>
<dt>
<dd>
<dl>
<dt>^N or !</p>
<dd> Search for lines which do NOT match the pattern.</p>
<dt>^E or *</p>
<dd> Search multiple files. That is, if the search reaches the beginning of the current file without finding a match, the search continues in the previous file in the command line list.</p>
<dt>^F or @</p>
<dd> Begin the search at the last line of the last file in the command line list, regardless of what is currently displayed on the screen or the settings of the -a or -j options.</p>
<dt>^K</p>
<dd> As in forward searches.</p>
<dt>^R</p>
<dd> As in forward searches.</p>
<dt>^W</p>
<dd> WRAP around the current file. That is, if the search reaches the beginning of the current file without finding a match, the search continues from the last line of the current file up to the line where it started.</dl>
</dl>
<dt>ESC-/pattern</p>
<dd> Same as &quot;/*&quot;.</p>
<dt>ESC-?pattern</p>
<dd> Same as &quot;?*&quot;.</p>
<dt>n</p>
<dd> Repeat previous search, for N-th line containing the last pattern. If the previous search was modified by ^N, the search is made for the N-th line NOT containing the pattern. If the previous search was modified by ^E, the search continues in the next (or previous) file if not satisfied in the current file. If the previous search was modified by ^R, the search is done without using regular expressions. There is no effect if the previous search was modified by ^F or ^K.</p>
<dt>N</p>
<dd> Repeat previous search, but in the reverse direction.</p>
<dt>ESC-n</p>
<dd> Repeat previous search, but crossing file boundaries. The effect is as if the previous search were modified by *.</p>
<dt>ESC-N</p>
<dd> Repeat previous search, but in the reverse direction and crossing file boundaries.</p>
<dt>ESC-u</p>
<dd> Undo search highlighting. Turn off highlighting of strings matching the current search pattern. If highlighting is already off because of a previous ESC-u command, turn highlighting back on. Any search command will also turn highlighting back on. (Highlighting can also be disabled by toggling the -G option; in that case search commands do not turn highlighting back on.)</p>
<dt>ESC-U</p>
<dd> Like ESC-u but also clears the saved search pattern. If the status column is enabled via the -J option, this clears all search matches marked in the status column.</p>
<dt>&amp;pattern</p>
<dd> Display only lines which match the pattern; lines which do not match the pattern are not displayed. If pattern is empty (if you type &amp; immediately followed by ENTER), any filtering is turned off, and all lines are displayed. While filtering is in effect, an ampersand is displayed at the beginning of the prompt, as a reminder that some lines in the file may be hidden. Multiple &amp; commands may be entered, in which case only lines which match all of the patterns will be displayed. </p>
<p> Certain characters are special as in the / command:</p>
<dl>
<dt>
<dd>
<dl>
<dt>^N or !</p>
<dd> Display only lines which do NOT match the pattern.</p>
<dt>^R</p>
<dd> Don&#8217;t interpret regular expression metacharacters; that is, do a simple textual comparison.</dl>
</dl>
<dt>:e [filename]</p>
<dd> Examine a new file. If the filename is missing, the &quot;current&quot; file (see the :n and :p commands below) from the list of files in the command line is re-examined. A percent sign (%) in the filename is replaced by the name of the current file. A pound sign (#) is replaced by the name of the previously examined file. However, two consecutive percent signs are simply replaced with a single percent sign. This allows you to enter a filename that contains a percent sign in the name. Similarly, two consecutive pound signs are replaced with a single pound sign. The filename is inserted into the command line list of files so that it can be seen by subsequent :n and :p commands. If the filename consists of several files, they are all inserted into the list of files and the first one is examined. If the filename contains one or more spaces, the entire filename should be enclosed in double quotes (also see the -&quot; option).</p>
<dt>^X^V or E</p>
<dd> Same as :e. Warning: some systems use ^V as a special literalization character. On such systems, you may not be able to use ^V.</p>
<dt>:n</p>
<dd> Examine the next file (from the list of files given in the command line). If a number N is specified, the N-th next file is examined.</p>
<dt>:p</p>
<dd> Examine the previous file in the command line list. If a number N is specified, the N-th previous file is examined.</p>
<dt>:x</p>
<dd> Examine the first file in the command line list. If a number N is specified, the N-th file in the list is examined.</p>
<dt>:d</p>
<dd> Remove the current file from the list of files.</p>
<dt>t</p>
<dd> Go to the next tag, if there were more than one matches for the current tag. See the -t option for more details about tags.</p>
<dt>T</p>
<dd> Go to the previous tag, if there were more than one matches for the current tag.</p>
<dt>= or ^G or :f</p>
<dd> Prints some information about the file being viewed, including its name and the line number and byte offset of the bottom line being displayed. If possible, it also prints the length of the file, the number of lines in the file and the percent of the file above the last displayed line.</p>
<dt>&#8211;</p>
<dd> Followed by one of the command line option letters (see OPTIONS below), this will change the setting of that option and print a message describing the new setting. If a ^P (CONTROL-P) is entered immediately after the dash, the setting of the option is changed but no message is printed. If the option letter has a numeric value (such as -b or -h), or a string value (such as -P or -t), a new value may be entered after the option letter. If no new value is entered, a message describing the current setting is printed and nothing is changed.</p>
<dt>&#8212;</p>
<dd> Like the &#8211; command, but takes a long option name (see OPTIONS below) rather than a single option letter. You must press ENTER or RETURN after typing the option name. A ^P immediately after the second dash suppresses printing of a message describing the new setting, as in the &#8211; command.</p>
<dt>-+</p>
<dd> Followed by one of the command line option letters this will reset the option to its default setting and print a message describing the new setting. (The &quot;-+<i>X</i>&quot; command does the same thing as &quot;-+<i>X</i>&quot; on the command line.) This does not work for string-valued options.</p>
<dt>&#8211;+</p>
<dd> Like the -+ command, but takes a long option name rather than a single option letter.</p>
<dt>-!</p>
<dd> Followed by one of the command line option letters, this will reset the option to the &quot;opposite&quot; of its default setting and print a message describing the new setting. This does not work for numeric or string-valued options.</p>
<dt>&#8211;!</p>
<dd> Like the -! command, but takes a long option name rather than a single option letter.</p>
<dt>_</p>
<dd> (Underscore.) Followed by one of the command line option letters, this will print a message describing the current setting of that option. The setting of the option is not changed.</p>
<dt>__</p>
<dd> (Double underscore.) Like the _ (underscore) command, but takes a long option name rather than a single option letter. You must press ENTER or RETURN after typing the option name.</p>
<dt>+cmd</p>
<dd> Causes the specified cmd to be executed each time a new file is examined. For example, +G causes <i>less</i> to initially display each file starting at the end rather than the beginning.</p>
<dt>V</p>
<dd> Prints the version number of <i>less</i> being run.</p>
<dt>q or Q or :q or :Q or ZZ</p>
<dd> Exits <i>less</i>.</dl>
<p> The following four commands may or may not be valid, depending on your particular installation.</p>
<dl>
<dt>v</p>
<dd> Invokes an editor to edit the current file being viewed. The editor is taken from the environment variable VISUAL if defined, or EDITOR if VISUAL is not defined, or defaults to &quot;vi&quot; if neither VISUAL nor EDITOR is defined. See also the discussion of LESSEDIT under the section on PROMPTS below.</p>
<dt>! shell-command</p>
<dd> Invokes a shell to run the shell-command given. A percent sign (%) in the command is replaced by the name of the current file. A pound sign (#) is replaced by the name of the previously examined file. &quot;!!&quot; repeats the last shell command. &quot;!&quot; with no shell command simply invokes a shell. On Unix systems, the shell is taken from the environment variable SHELL, or defaults to &quot;sh&quot;. On MS-DOS and OS/2 systems, the shell is the normal command processor.</p>
<dt>| &lt;m&gt; shell-command</p>
<dd> &lt;m&gt; represents any mark letter. Pipes a section of the input file to the given shell command. The section of the file to be piped is between the position marked by the letter and the current screen. The entire current screen is included, regardless of whether the marked position is before or after the current screen. &lt;m&gt; may also be ^ or $ to indicate beginning or end of file respectively. If &lt;m&gt; is . or newline, the current screen is piped.</p>
<dt>s filename</p>
<dd> Save the input to a file. This only works if the input is a pipe, not an ordinary file.</dl>
<h2>OPTIONS</h2>
<p> Command line options are described below. Most options may be changed while <i>less</i> is running, via the &quot;-&quot; command. </p>
<p> Most options may be given in one of two forms: either a dash followed by a single letter, or two dashes followed by a long option name. A long option name may be abbreviated as long as the abbreviation is unambiguous. For example, &#8211;quit-at-eof may be abbreviated &#8211;quit, but not &#8211;qui, since both &#8211;quit-at-eof and &#8211;quiet begin with &#8211;qui. Some long option names are in uppercase, such as &#8211;QUIT-AT-EOF, as distinct from &#8211;quit-at-eof. Such option names need only have their first letter capitalized; the remainder of the name may be in either case. For example, &#8211;Quit-at-eof is equivalent to &#8211;QUIT-AT-EOF. </p>
<p> Options are also taken from the environment variable &quot;LESS&quot;. For example, to avoid typing &quot;less -options &#8230;&quot; each time <i>less</i> is invoked, you might tell <i>csh</i>: </p>
<p> setenv LESS &quot;-options&quot; </p>
<p> or if you use <i>sh</i>: </p>
<p> LESS=&quot;-options&quot;; export LESS </p>
<p> On MS-DOS, you don&#8217;t need the quotes, but you should replace any percent signs in the options string by double percent signs. </p>
<p> The environment variable is parsed before the command line, so command line options override the LESS environment variable. If an option appears in the LESS variable, it can be reset to its default value on the command line by beginning the command line option with &quot;-+&quot;. </p>
<p> Some options like -k or -D require a string to follow the option letter. The string for that option is considered to end when a dollar sign ($) is found. For example, you can set two -D options on MS-DOS like this: </p>
<p> LESS=&quot;Dn9.1$Ds4.1&quot; </p>
<p> If the &#8211;use-backslash option appears earlier in the options, then a dollar sign or backslash may be included literally in an option string by preceding it with a backslash. If the &#8211;use-backslash option is not in effect, then backslashes are not treated specially, and there is no way to include a dollar sign in the option string.</p>
<dl>
<dt>-? or &#8211;help</p>
<dd> This option displays a summary of the commands accepted by <i>less</i> (the same as the h command). (Depending on how your shell interprets the question mark, it may be necessary to quote the question mark, thus: &quot;-\?&quot;.)</p>
<dt>-a or &#8211;search-skip-screen</p>
<dd> By default, forward searches start at the top of the displayed screen and backwards searches start at the bottom of the displayed screen (except for repeated searches invoked by the n or N commands, which start after or before the &quot;target&quot; line respectively; see the -j option for more about the target line). The -a option causes forward searches to instead start at the bottom of the screen and backward searches to start at the top of the screen, thus skipping all lines displayed on the screen.</p>
<dt>-A or &#8211;SEARCH-SKIP-SCREEN</p>
<dd> Causes all forward searches (not just non-repeated searches) to start just after the target line, and all backward searches to start just before the target line. Thus, forward searches will skip part of the displayed screen (from the first line up to and including the target line). Similarly backwards searches will skip the displayed screen from the last line up to and including the target line. This was the default behavior in less versions prior to 441.</p>
<dt>-b<i>n</i> or &#8211;buffers=<i>n</i></p>
<dd> Specifies the amount of buffer space <i>less</i> will use for each file, in units of kilobytes (1024 bytes). By default 64 KB of buffer space is used for each file (unless the file is a pipe; see the -B option). The -b option specifies instead that <i>n</i> kilobytes of buffer space should be used for each file. If <i>n</i> is -1, buffer space is unlimited; that is, the entire file can be read into memory.</p>
<dt>-B or &#8211;auto-buffers</p>
<dd> By default, when data is read from a pipe, buffers are allocated automatically as needed. If a large amount of data is read from the pipe, this can cause a large amount of memory to be allocated. The -B option disables this automatic allocation of buffers for pipes, so that only 64 KB (or the amount of space specified by the -b option) is used for the pipe. Warning: use of -B can result in erroneous display, since only the most recently viewed part of the piped data is kept in memory; any earlier data is lost.</p>
<dt>-c or &#8211;clear-screen</p>
<dd> Causes full screen repaints to be painted from the top line down. By default, full screen repaints are done by scrolling from the bottom of the screen.</p>
<dt>-C or &#8211;CLEAR-SCREEN</p>
<dd> Same as -c, for compatibility with older versions of <i>less</i>.</p>
<dt>-d or &#8211;dumb</p>
<dd> The -d option suppresses the error message normally displayed if the terminal is dumb; that is, lacks some important capability, such as the ability to clear the screen or scroll backward. The -d option does not otherwise change the behavior of <i>less</i> on a dumb terminal.</p>
<dt>-D<code>x</code><i>color</i> or &#8211;color=<code>x</code><i>color</i></p>
<dd> Changes the color of different parts of the displayed text. <code>x</code> is a single character which selects the type of text whose color is being set:</p>
<dl>
<dt>
<dd>
<dl>
<dt>B</p>
<dd> Binary characters.</p>
<dt>C</p>
<dd> Control characters.</p>
<dt>E</p>
<dd> Errors and informational messages.</p>
<dt>M</p>
<dd> Mark letters in the status column.</p>
<dt>N</p>
<dd> Line numbers enabled via the -N option.</p>
<dt>P</p>
<dd> Prompts.</p>
<dt>R</p>
<dd> The rscroll character.</p>
<dt>S</p>
<dd> Search results.</p>
<dt>W</p>
<dd> The highlight enabled via the -w option.</p>
<dt>d</p>
<dd> Bold text.</p>
<dt>k</p>
<dd> Blinking text.</p>
<dt>s</p>
<dd> Standout text.</p>
<dt>u</p>
<dd> Underlined text.</dl>
</dl>
<p>&nbsp;</p>
<dl>
<dt>
<dd> The uppercase letters can be used only when the &#8211;use-color option is enabled. When text color is specified by both an uppercase letter and a lowercase letter, the uppercase letter takes precedence. For example, error messages are normally displayed as standout text. So if both &quot;s&quot; and &quot;E&quot; are given a color, the &quot;E&quot; color applies to error messages, and the &quot;s&quot; color applies to other standout text. The &quot;d&quot; and &quot;u&quot; letters refer to bold and underline text formed by overstriking with backspaces (see the -u option), not to text using ANSI escape sequences with the -R option. </p>
<p> A lowercase letter may be followed by a + to indicate that both the normal format change and the specified color should both be used. For example, -Dug displays underlined text as green without underlining; the green color has replaced the usual underline formatting. But -Du+g displays underlined text as both green and in underlined format. </p>
<p> <i>color</i> is either a 4-bit color string or an 8-bit color string: </p>
<p> A 4-bit color string is zero, one or two characters, where the first character specifies the foreground color and the second specifies the background color as follows:</p>
<dl>
<dt>b</p>
<dd> Blue</p>
<dt>c</p>
<dd> Cyan</p>
<dt>g</p>
<dd> Green</p>
<dt>k</p>
<dd> Black</p>
<dt>m</p>
<dd> Magenta</p>
<dt>r</p>
<dd> Red</p>
<dt>w</p>
<dd> White</p>
<dt>y</p>
<dd> Yellow</dl>
<p> The corresponding upper-case letter denotes a brighter shade of the color. For example, -DNGk displays line numbers as bright green text on a black background, and -DEbR displays error messages as blue text on a bright red background. If either character is a &quot;-&quot; or is omitted, the corresponding color is set to that of normal text. </p>
<p> An 8-bit color string is one or two decimal integers separated by a dot, where the first integer specifies the foreground color and the second specifies the background color. Each integer is a value between 0 and 255 inclusive which selects a &quot;CSI 38;5&quot; color value (see<br />
 <a rel="nofollow" href="https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_parameters)">https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_parameters)</a> If either integer is a &quot;-&quot; or is omitted, the corresponding color is set to that of normal text. On MS-DOS versions of <i>less</i>, 8-bit color is not supported; instead, decimal values are interpreted as 4-bit CHAR_INFO.Attributes values (see<br />
 <a rel="nofollow" href="https://docs.microsoft.com/en-us/windows/console/char-info-str">https://docs.microsoft.com/en-us/windows/console/char-info-str</a>).</dl>
<dt>-e or &#8211;quit-at-eof</p>
<dd> Causes <i>less</i> to automatically exit the second time it reaches end-of-file. By default, the only way to exit <i>less</i> is via the &quot;q&quot; command.</p>
<dt>-E or &#8211;QUIT-AT-EOF</p>
<dd> Causes <i>less</i> to automatically exit the first time it reaches end-of-file.</p>
<dt>-f or &#8211;force</p>
<dd> Forces non-regular files to be opened. (A non-regular file is a directory or a device special file.) Also suppresses the warning message when a binary file is opened. By default, <i>less</i> will refuse to open non-regular files. Note that some operating systems will not allow directories to be read, even if -f is set.</p>
<dt>-F or &#8211;quit-if-one-screen</p>
<dd> Causes <i>less</i> to automatically exit if the entire file can be displayed on the first screen.</p>
<dt>-g or &#8211;hilite-search</p>
<dd> Normally, <i>less</i> will highlight ALL strings which match the last search command. The -g option changes this behavior to highlight only the particular string which was found by the last search command. This can cause <i>less</i> to run somewhat faster than the default.</p>
<dt>-G or &#8211;HILITE-SEARCH</p>
<dd> The -G option suppresses all highlighting of strings found by search commands.</p>
<dt>-h<i>n</i> or &#8211;max-back-scroll=<i>n</i></p>
<dd> Specifies a maximum number of lines to scroll backward. If it is necessary to scroll backward more than <i>n</i> lines, the screen is repainted in a forward direction instead. (If the terminal does not have the ability to scroll backward, -h0 is implied.)</p>
<dt>-i or &#8211;ignore-case</p>
<dd> Causes searches to ignore case; that is, uppercase and lowercase are considered identical. This option is ignored if any uppercase letters appear in the search pattern; in other words, if a pattern contains uppercase letters, then that search does not ignore case.</p>
<dt>-I or &#8211;IGNORE-CASE</p>
<dd> Like -i, but searches ignore case even if the pattern contains uppercase letters.</p>
<dt>-j<i>n</i> or &#8211;jump-target=<i>n</i></p>
<dd> Specifies a line on the screen where the &quot;target&quot; line is to be positioned. The target line is the line specified by any command to search for a pattern, jump to a line number, jump to a file percentage or jump to a tag. The screen line may be specified by a number: the top line on the screen is 1, the next is 2, and so on. The number may be negative to specify a line relative to the bottom of the screen: the bottom line on the screen is -1, the second to the bottom is -2, and so on. Alternately, the screen line may be specified as a fraction of the height of the screen, starting with a decimal point: .5 is in the middle of the screen, .3 is three tenths down from the first line, and so on. If the line is specified as a fraction, the actual line number is recalculated if the terminal window is resized, so that the target line remains at the specified fraction of the screen height. If any form of the -j option is used, repeated forward searches (invoked with &quot;n&quot; or &quot;N&quot;) begin at the line immediately after the target line, and repeated backward searches begin at the target line, unless changed by -a or -A. For example, if &quot;-j4&quot; is used, the target line is the fourth line on the screen, so forward searches begin at the fifth line on the screen. However nonrepeated searches (invoked with &quot;/&quot; or &quot;?&quot;) always begin at the start or end of the current screen respectively.</p>
<dt>-J or &#8211;status-column</p>
<dd> Displays a status column at the left edge of the screen. The status column shows the lines that matched the current search, and any lines that are marked (via the m or M command).</p>
<dt>-k<i>filename</i> or &#8211;lesskey-file=<i>filename</i></p>
<dd> Causes <i>less</i> to open and interpret the named file as a <i><a href="/docs/linux/man/1-lesskey/">lesskey</a></i>(1) binary file. Multiple -k options may be specified. If the LESSKEY or LESSKEY_SYSTEM environment variable is set, or if a lesskey file is found in a standard place (see KEY BINDINGS), it is also used as a <i>lesskey</i> file.</p>
<dt>&#8211;lesskey-src=<i>filename</i></p>
<dd> Causes <i>less</i> to open and interpret the named file as a <i><a href="/docs/linux/man/1-lesskey/">lesskey</a></i>(1) source file. If the LESSKEYIN or LESSKEYIN_SYSTEM environment variable is set, or if a lesskey source file is found in a standard place (see KEY BINDINGS), it is also used as a <i>lesskey source</i> file. Prior to version 582, the <i>lesskey</i> program needed to be run to convert a <i>lesskey source</i> file to a <i>lesskey binary</i> file for <i>less</i> to use. Newer versions of <i>less</i> read the <i>lesskey source</i> file directly and ignore the binary file if the source file exists.</p>
<dt>-K or &#8211;quit-on-intr</p>
<dd> Causes <i>less</i> to exit immediately (with status 2) when an interrupt character (usually ^C) is typed. Normally, an interrupt character causes <i>less</i> to stop whatever it is doing and return to its command prompt. Note that use of this option makes it impossible to return to the command prompt from the &quot;F&quot; command.</p>
<dt>-L or &#8211;no-lessopen</p>
<dd> Ignore the LESSOPEN environment variable (see the INPUT PREPROCESSOR section below). This option can be set from within <i>less</i>, but it will apply only to files opened subsequently, not to the file which is currently open.</p>
<dt>-m or &#8211;long-prompt</p>
<dd> Causes <i>less</i> to prompt verbosely (like <i>more</i>), with the percent into the file. By default, <i>less</i> prompts with a colon.</p>
<dt>-M or &#8211;LONG-PROMPT</p>
<dd> Causes <i>less</i> to prompt even more verbosely than <i>more</i>.</p>
<dt>-n or &#8211;line-numbers</p>
<dd> Suppresses line numbers. The default (to use line numbers) may cause <i>less</i> to run more slowly in some cases, especially with a very large input file. Suppressing line numbers with the -n option will avoid this problem. Using line numbers means: the line number will be displayed in the verbose prompt and in the = command, and the v command will pass the current line number to the editor (see also the discussion of LESSEDIT in PROMPTS below).</p>
<dt>-N or &#8211;LINE-NUMBERS</p>
<dd> Causes a line number to be displayed at the beginning of each line in the display.</p>
<dt>-o<i>filename</i> or &#8211;log-file=<i>filename</i></p>
<dd> Causes <i>less</i> to copy its input to the named file as it is being viewed. This applies only when the input file is a pipe, not an ordinary file. If the file already exists, <i>less</i> will ask for confirmation before overwriting it.</p>
<dt>-O<i>filename</i> or &#8211;LOG-FILE=<i>filename</i></p>
<dd> The -O option is like -o, but it will overwrite an existing file without asking for confirmation. </p>
<p> If no log file has been specified, the -o and -O options can be used from within <i>less</i> to specify a log file. Without a file name, they will simply report the name of the log file. The &quot;s&quot; command is equivalent to specifying -o from within <i>less</i>.</p>
<dt>-p<i>pattern</i> or &#8211;pattern=<i>pattern</i></p>
<dd> The -p option on the command line is equivalent to specifying +/<i>pattern</i>; that is, it tells <i>less</i> to start at the first occurrence of <i>pattern</i> in the file.</p>
<dt>-P<i>prompt</i> or &#8211;prompt=<i>prompt</i></p>
<dd> Provides a way to tailor the three prompt styles to your own preference. This option would normally be put in the LESS environment variable, rather than being typed in with each <i>less</i> command. Such an option must either be the last option in the LESS variable, or be terminated by a dollar sign.<br />
&nbsp;-Ps followed by a string changes the default&nbsp;(short)&nbsp;prompt to that string.<br />
&nbsp;-Pm changes the medium&nbsp;(-m)&nbsp;prompt.<br />
&nbsp;-PM changes the long&nbsp;(-M)&nbsp;prompt.<br />
&nbsp;-Ph changes the prompt for the help screen.<br />
&nbsp;-P=&nbsp;changes the message printed by the&nbsp;=&nbsp;command.<br />
&nbsp;-Pw changes the message printed while waiting for data&nbsp;(in the F command). </p>
<p> All prompt strings consist of a sequence of letters and special escape sequences. See the section on PROMPTS for more details.</p>
<dt>-q or &#8211;quiet or &#8211;silent</p>
<dd> Causes moderately &quot;quiet&quot; operation: the terminal bell is not rung if an attempt is made to scroll past the end of the file or before the beginning of the file. If the terminal has a &quot;visual bell&quot;, it is used instead. The bell will be rung on certain other errors, such as typing an invalid character. The default is to ring the terminal bell in all such cases.</p>
<dt>-Q or &#8211;QUIET or &#8211;SILENT</p>
<dd> Causes totally &quot;quiet&quot; operation: the terminal bell is never rung. If the terminal has a &quot;visual bell&quot;, it is used in all cases where the terminal bell would have been rung.</p>
<dt>-r or &#8211;raw-control-chars</p>
<dd> Causes &quot;raw&quot; control characters to be displayed. The default is to display control characters using the caret notation; for example, a control-A (octal 001) is displayed as &quot;^A&quot;. Warning: when the -r option is used, <i>less</i> cannot keep track of the actual appearance of the screen (since this depends on how the screen responds to each type of control character). Thus, various display problems may result, such as long lines being split in the wrong place. </p>
<p> USE OF THE -r OPTION IS NOT RECOMMENDED.</p>
<dt>-R or &#8211;RAW-CONTROL-CHARS</p>
<dd> Like -r, but only ANSI &quot;color&quot; escape sequences and OSC 8 hyperlink sequences are output in &quot;raw&quot; form. Unlike -r, the screen appearance is maintained correctly, provided that there are no escape sequences in the file other than these types of escape sequences. Color escape sequences are only supported when the color is changed within one line, not across lines. In other words, the beginning of each line is assumed to be normal (non-colored), regardless of any escape sequences in previous lines. For the purpose of keeping track of screen appearance, these escape sequences are assumed to not move the cursor. </p>
<p> OSC 8 hyperlinks are sequences of the form: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>ESC ] 8 ; &#8230; \7</p>
<p> The terminating sequence may be either a BEL character (\7) or the two-character sequence &quot;ESC \&quot;. </p>
<p> ANSI color escape sequences are sequences of the form: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>ESC [ &#8230; m</p>
<p> where the &quot;&#8230;&quot; is zero or more color specification characters. You can make <i>less</i> think that characters other than &quot;m&quot; can end ANSI color escape sequences by setting the environment variable LESSANSIENDCHARS to the list of characters which can end a color escape sequence. And you can make <i>less</i> think that characters other than the standard ones may appear between the ESC and the m by setting the environment variable LESSANSIMIDCHARS to the list of characters which can appear.</p>
<dt>-s or &#8211;squeeze-blank-lines</p>
<dd> Causes consecutive blank lines to be squeezed into a single blank line. This is useful when viewing <i>nroff</i> output.</p>
<dt>-S or &#8211;chop-long-lines</p>
<dd> Causes lines longer than the screen width to be chopped (truncated) rather than wrapped. That is, the portion of a long line that does not fit in the screen width is not displayed until you press RIGHT-ARROW. The default is to wrap long lines; that is, display the remainder on the next line.</p>
<dt>-t<i>tag</i> or &#8211;tag=<i>tag</i></p>
<dd> The -t option, followed immediately by a TAG, will edit the file containing that tag. For this to work, tag information must be available; for example, there may be a file in the current directory called &quot;tags&quot;, which was previously built by <i><a href="/docs/linux/man/1-ctags/">ctags</a></i>(1) or an equivalent command. If the environment variable LESSGLOBALTAGS is set, it is taken to be the name of a command compatible with <i><a href="/docs/linux/man/1-global/">global</a></i>(1), and that command is executed to find the tag. (See <a rel="nofollow" href="http://www.gnu.org/software/global/global.html">http://www.gnu.org/software/global/global.html</a>). The -t option may also be specified from within <i>less</i> (using the &#8211; command) as a way of examining a new file. The command &quot;:t&quot; is equivalent to specifying -t from within <i>less</i>.</p>
<dt>-T<i>tagsfile</i> or &#8211;tag-file=<i>tagsfile</i></p>
<dd> Specifies a tags file to be used instead of &quot;tags&quot;.</p>
<dt>-u or &#8211;underline-special</p>
<dd> Causes backspaces and carriage returns to be treated as printable characters; that is, they are sent to the terminal when they appear in the input.</p>
<dt>-U or &#8211;UNDERLINE-SPECIAL</p>
<dd> Causes backspaces, tabs, carriage returns and &quot;formatting characters&quot; (as defined by Unicode) to be treated as control characters; that is, they are handled as specified by the -r option. </p>
<p> By default, if neither -u nor -U is given, backspaces which appear adjacent to an underscore character are treated specially: the underlined text is displayed using the terminal&#8217;s hardware underlining capability. Also, backspaces which appear between two identical characters are treated specially: the overstruck text is printed using the terminal&#8217;s hardware boldface capability. Other backspaces are deleted, along with the preceding character. Carriage returns immediately followed by a newline are deleted. Other carriage returns are handled as specified by the -r option. Unicode formatting characters, such as the Byte Order Mark, are sent to the terminal. Text which is overstruck or underlined can be searched for if neither -u nor -U is in effect.</p>
<dt>-V or &#8211;version</p>
<dd> Displays the version number of <i>less</i>.</p>
<dt>-w or &#8211;hilite-unread</p>
<dd> Temporarily highlights the first &quot;new&quot; line after a forward movement of a full page. The first &quot;new&quot; line is the line immediately following the line previously at the bottom of the screen. Also highlights the target line after a g or p command. The highlight is removed at the next command which causes movement. The entire line is highlighted, unless the -J option is in effect, in which case only the status column is highlighted.</p>
<dt>-W or &#8211;HILITE-UNREAD</p>
<dd> Like -w, but temporarily highlights the first new line after any forward movement command larger than one line.</p>
<dt>-x<i>n</i>,&#8230; or &#8211;tabs=<i>n</i>,&#8230;</p>
<dd> Sets tab stops. If only one <i>n</i> is specified, tab stops are set at multiples of <i>n</i>. If multiple values separated by commas are specified, tab stops are set at those positions, and then continue with the same spacing as the last two. For example, <i>-x9,17</i> will set tabs at positions 9, 17, 25, 33, etc. The default for <i>n</i> is 8.</p>
<dt>-X or &#8211;no-init</p>
<dd> Disables sending the termcap initialization and deinitialization strings to the terminal. This is sometimes desirable if the deinitialization string does something unnecessary, like clearing the screen.</p>
<dt>-y<i>n</i> or &#8211;max-forw-scroll=<i>n</i></p>
<dd> Specifies a maximum number of lines to scroll forward. If it is necessary to scroll forward more than <i>n</i> lines, the screen is repainted instead. The -c or -C option may be used to repaint from the top of the screen if desired. By default, any forward movement causes scrolling.</p>
<dt>-z<i>n</i> or &#8211;window=<i>n</i> or &#8211;<i>n</i></p>
<dd> Changes the default scrolling window size to <i>n</i> lines. The default is one screenful. The z and w commands can also be used to change the window size. The &quot;z&quot; may be omitted for compatibility with some versions of <i>more</i>. If the number <i>n</i> is negative, it indicates <i>n</i> lines less than the current screen size. For example, if the screen is 24 lines, <i>-z-4</i> sets the scrolling window to 20 lines. If the screen is resized to 40 lines, the scrolling window automatically changes to 36 lines.</p>
<dt>-&quot;<i>cc</i>&nbsp;or &#8211;quotes=<i>cc</i></p>
<dd> Changes the filename quoting character. This may be necessary if you are trying to name a file which contains both spaces and quote characters. Followed by a single character, this changes the quote character to that character. Filenames containing a space should then be surrounded by that character rather than by double quotes. Followed by two characters, changes the open quote to the first character, and the close quote to the second character. Filenames containing a space should then be preceded by the open quote character and followed by the close quote character. Note that even after the quote characters are changed, this option remains -&quot; (a dash followed by a double quote).</p>
<dt>-~ or &#8211;tilde</p>
<dd> Normally lines after end of file are displayed as a single tilde (~). This option causes lines after end of file to be displayed as blank lines.</p>
<dt>-# or &#8211;shift</p>
<dd> Specifies the default number of positions to scroll horizontally in the RIGHTARROW and LEFTARROW commands. If the number specified is zero, it sets the default number of positions to one half of the screen width. Alternately, the number may be specified as a fraction of the width of the screen, starting with a decimal point: .5 is half of the screen width, .3 is three tenths of the screen width, and so on. If the number is specified as a fraction, the actual number of scroll positions is recalculated if the terminal window is resized, so that the actual scroll remains at the specified fraction of the screen width.</p>
<dt>&#8211;file-size</p>
<dd> If &#8211;file-size is specified, <i>less</i> will determine the size of the file immediately after opening the file. Normally this is not done, because it can be slow if the input file is large.</p>
<dt>&#8211;follow-name</p>
<dd> Normally, if the input file is renamed while an F command is executing, <i>less</i> will continue to display the contents of the original file despite its name change. If &#8211;follow-name is specified, during an F command <i>less</i> will periodically attempt to reopen the file by name. If the reopen succeeds and the file is a different file from the original (which means that a new file has been created with the same name as the original (now renamed) file), <i>less</i> will display the contents of that new file.</p>
<dt>&#8211;incsearch</p>
<dd> Subsequent search commands will be &quot;incremental&quot;; that is, <i>less</i> will advance to the next line containing the search pattern as each character of the pattern is typed in.</p>
<dt>&#8211;line-num-width</p>
<dd> Sets the minimum width of the line number field when the -N option is in effect. The default is 7 characters.</p>
<dt>&#8211;mouse</p>
<dd> Enables mouse input: scrolling the mouse wheel down moves forward in the file, scrolling the mouse wheel up moves backwards in the file, and clicking the mouse sets the &quot;#&quot; mark to the line where the mouse is clicked. The number of lines to scroll when the wheel is moved can be set by the &#8211;wheel-lines option. Mouse input works only on terminals which support X11 mouse reporting, and on the Windows version of <i>less</i>.</p>
<dt>&#8211;MOUSE</p>
<dd> Like &#8211;mouse, except the direction scrolled on mouse wheel movement is reversed.</p>
<dt>&#8211;no-keypad</p>
<dd> Disables sending the keypad initialization and deinitialization strings to the terminal. This is sometimes useful if the keypad strings make the numeric keypad behave in an undesirable manner.</p>
<dt>&#8211;no-histdups</p>
<dd> This option changes the behavior so that if a search string or file name is typed in, and the same string is already in the history list, the existing copy is removed from the history list before the new one is added. Thus, a given string will appear only once in the history list. Normally, a string may appear multiple times.</p>
<dt>&#8211;rscroll</p>
<dd> This option changes the character used to mark truncated lines. It may begin with a two-character attribute indicator like LESSBINFMT does. If there is no attribute indicator, standout is used. If set to &quot;-&quot;, truncated lines are not marked.</p>
<dt>&#8211;save-marks</p>
<dd> Save marks in the history file, so marks are retained across different invocations of <i>less</i>.</p>
<dt>&#8211;status-col-width</p>
<dd> Sets the width of the status column when the -J option is in effect. The default is 2 characters.</p>
<dt>&#8211;use-backslash</p>
<dd> This option changes the interpretations of options which follow this one. After the &#8211;use-backslash option, any backslash in an option string is removed and the following character is taken literally. This allows a dollar sign to be included in option strings.</p>
<dt>&#8211;use-color</p>
<dd> Enables the colored text in various places. The -D option can be used to change the colors. Colored text works only if the terminal supports ANSI color escape sequences (as defined in ECMA-48 SGR; see<br />
 <a rel="nofollow" href="https://www.ecma-international.org/publications-and-standards/standards/ecma-48">https://www.ecma-international.org/publications-and-standards/standards/ecma-48</a>).</p>
<dt>&#8211;wheel-lines=<i>n</i></p>
<dd> Set the number of lines to scroll when the mouse wheel is scrolled and the &#8211;mouse or &#8211;MOUSE option is in effect. The default is 1 line.</p>
<dt>&#8212;</p>
<dd> A command line argument of &quot;&#8211;&quot; marks the end of option arguments. Any arguments following this are interpreted as filenames. This can be useful when viewing a file whose name begins with a &quot;-&quot; or &quot;+&quot;.</p>
<dt>+</p>
<dd> If a command line option begins with <code>+</code>, the remainder of that option is taken to be an initial command to <i>less</i>. For example, +G tells <i>less</i> to start at the end of the file rather than the beginning, and +/xyz tells it to start at the first occurrence of &quot;xyz&quot; in the file. As a special case, +&lt;number&gt; acts like +&lt;number&gt;g; that is, it starts the display at the specified line number (however, see the caveat under the &quot;g&quot; command above). If the option starts with ++, the initial command applies to every file being viewed, not just the first one. The + command described previously may also be used to set (or change) an initial command for every file.</dl>
<h2>LINE EDITING</h2>
<p> When entering a command line at the bottom of the screen (for example, a filename for the :e command, or the pattern for a search command), certain keys can be used to manipulate the command line. Most commands have an alternate form in [ brackets ] which can be used if a key does not exist on a particular keyboard. (Note that the forms beginning with ESC do not work in some MS-DOS and Windows systems because ESC is the line erase character.) Any of these special keys may be entered literally by preceding it with the &quot;literal&quot; character, either ^V or ^A. A backslash itself may also be entered literally by entering two backslashes.</p>
<dl>
<dt>LEFTARROW [ ESC-h ]</p>
<dd> Move the cursor one space to the left.</p>
<dt>RIGHTARROW [ ESC-l ]</p>
<dd> Move the cursor one space to the right.</p>
<dt>^LEFTARROW [ ESC-b or ESC-LEFTARROW ]</p>
<dd> (That is, CONTROL and LEFTARROW simultaneously.) Move the cursor one word to the left.</p>
<dt>^RIGHTARROW [ ESC-w or ESC-RIGHTARROW ]</p>
<dd> (That is, CONTROL and RIGHTARROW simultaneously.) Move the cursor one word to the right.</p>
<dt>HOME [ ESC-0 ]</p>
<dd> Move the cursor to the beginning of the line.</p>
<dt>END [ ESC-$ ]</p>
<dd> Move the cursor to the end of the line.</p>
<dt>BACKSPACE</p>
<dd> Delete the character to the left of the cursor, or cancel the command if the command line is empty.</p>
<dt>DELETE or [ ESC-x ]</p>
<dd> Delete the character under the cursor.</p>
<dt>^BACKSPACE [ ESC-BACKSPACE ]</p>
<dd> (That is, CONTROL and BACKSPACE simultaneously.) Delete the word to the left of the cursor.</p>
<dt>^DELETE [ ESC-X or ESC-DELETE ]</p>
<dd> (That is, CONTROL and DELETE simultaneously.) Delete the word under the cursor.</p>
<dt>UPARROW [ ESC-k ]</p>
<dd> Retrieve the previous command line. If you first enter some text and then press UPARROW, it will retrieve the previous command which begins with that text.</p>
<dt>DOWNARROW [ ESC-j ]</p>
<dd> Retrieve the next command line. If you first enter some text and then press DOWNARROW, it will retrieve the next command which begins with that text.</p>
<dt>TAB</p>
<dd> Complete the partial filename to the left of the cursor. If it matches more than one filename, the first match is entered into the command line. Repeated TABs will cycle thru the other matching filenames. If the completed filename is a directory, a &quot;/&quot; is appended to the filename. (On MS-DOS systems, a &quot;\&quot; is appended.) The environment variable LESSSEPARATOR can be used to specify a different character to append to a directory name.</p>
<dt>BACKTAB [ ESC-TAB ]</p>
<dd> Like, TAB, but cycles in the reverse direction thru the matching filenames.</p>
<dt>^L</p>
<dd> Complete the partial filename to the left of the cursor. If it matches more than one filename, all matches are entered into the command line (if they fit).</p>
<dt>^U (Unix and OS/2) or ESC (MS-DOS)</p>
<dd> Delete the entire command line, or cancel the command if the command line is empty. If you have changed your line-kill character in Unix to something other than ^U, that character is used instead of ^U.</p>
<dt>^G</p>
<dd> Delete the entire command line and return to the main prompt.</dl>
<h2>KEY BINDINGS</h2>
<p> You may define your own <i>less</i> commands by creating a lesskey source file. This file specifies a set of command keys and an action associated with each key. You may also change the line-editing keys (see LINE EDITING), and to set environment variables. If the environment variable LESSKEYIN is set, <i>less</i> uses that as the name of the lesskey source file. Otherwise, <i>less</i> looks in a standard place for the lesskey source file: On Unix systems, <i>less</i> looks for a lesskey file called &quot;$XDG_CONFIG_HOME/lesskey&quot; or &quot;$HOME/.lesskey&quot;. On MS-DOS and Windows systems, <i>less</i> looks for a lesskey file called &quot;$HOME/_lesskey&quot;, and if it is not found there, then looks for a lesskey file called &quot;_lesskey&quot; in any directory specified in the PATH environment variable. On OS/2 systems, <i>less</i> looks for a lesskey file called &quot;$HOME/lesskey.ini&quot;, and if it is not found, then looks for a lesskey file called &quot;lesskey.ini&quot; in any directory specified in the INIT environment variable, and if it not found there, then looks for a lesskey file called &quot;lesskey.ini&quot; in any directory specified in the PATH environment variable. See the <i>lesskey</i> manual page for more details. </p>
<p> A system-wide lesskey source file may also be set up to provide key bindings. If a key is defined in both a local lesskey file and in the system-wide file, key bindings in the local file take precedence over those in the system-wide file. If the environment variable LESSKEYIN_SYSTEM is set, <i>less</i> uses that as the name of the system-wide lesskey file. Otherwise, <i>less</i> looks in a standard place for the system-wide lesskey file: On Unix systems, the system-wide lesskey file is /usr/local/etc/syslesskey. (However, if <i>less</i> was built with a different sysconf directory than /usr/local/etc, that directory is where the sysless file is found.) On MS-DOS and Windows systems, the system-wide lesskey file is c:\_syslesskey. On OS/2 systems, the system-wide lesskey file is c:\syslesskey.ini. </p>
<p> Previous versions of <i>less</i> (before v582) used lesskey files with a binary format, produced by the <i>lesskey</i> program. It is no longer necessary to use the <i>lesskey</i> program.</p>
<h2>INPUT PREPROCESSOR</h2>
<p> You may define an &quot;input preprocessor&quot; for <i>less</i>. Before <i>less</i> opens a file, it first gives your input preprocessor a chance to modify the way the contents of the file are displayed. An input preprocessor is simply an executable program (or shell script), which writes the contents of the file to a different file, called the replacement file. The contents of the replacement file are then displayed in place of the contents of the original file. However, it will appear to the user as if the original file is opened; that is, <i>less</i> will display the original filename as the name of the current file. </p>
<p> An input preprocessor receives one command line argument, the original filename, as entered by the user. It should create the replacement file, and when finished, print the name of the replacement file to its standard output. If the input preprocessor does not output a replacement filename, <i>less</i> uses the original file, as normal. The input preprocessor is not called when viewing standard input. To set up an input preprocessor, set the LESSOPEN environment variable to a command line which will invoke your input preprocessor. This command line should include one occurrence of the string &quot;%s&quot;, which will be replaced by the filename when the input preprocessor command is invoked. </p>
<p> When <i>less</i> closes a file opened in such a way, it will call another program, called the input postprocessor, which may perform any desired clean-up action (such as deleting the replacement file created by LESSOPEN). This program receives two command line arguments, the original filename as entered by the user, and the name of the replacement file. To set up an input postprocessor, set the LESSCLOSE environment variable to a command line which will invoke your input postprocessor. It may include two occurrences of the string &quot;%s&quot;; the first is replaced with the original name of the file and the second with the name of the replacement file, which was output by LESSOPEN. </p>
<p> For example, on many Unix systems, these two scripts will allow you to keep files in compressed format, but still let <i>less</i> view them directly: </p>
<p> lessopen.sh:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>#! /bin/sh</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>case &quot;$1&quot; in</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>*.Z)<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>TEMPFILE=$(mktemp)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>uncompress -c $1 &gt;$TEMPFILE 2&gt;/dev/null</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>if [ -s $TEMPFILE ]; then</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>echo $TEMPFILE</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>else</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>rm -f $TEMPFILE</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>fi</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>;;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>esac</p>
<p> lessclose.sh:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>#! /bin/sh</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>rm $2</p>
<p> To use these scripts, put them both where they can be executed and set LESSOPEN=&quot;lessopen.sh&nbsp;%s&quot;, and LESSCLOSE=&quot;lessclose.sh&nbsp;%s&nbsp;%s&quot;. More complex LESSOPEN and LESSCLOSE scripts may be written to accept other types of compressed files, and so on. </p>
<p> It is also possible to set up an input preprocessor to pipe the file data directly to <i>less</i>, rather than putting the data into a replacement file. This avoids the need to decompress the entire file before starting to view it. An input preprocessor that works this way is called an input pipe. An input pipe, instead of writing the name of a replacement file on its standard output, writes the entire contents of the replacement file on its standard output. If the input pipe does not write any characters on its standard output, then there is no replacement file and <i>less</i> uses the original file, as normal. To use an input pipe, make the first character in the LESSOPEN environment variable a vertical bar (|) to signify that the input preprocessor is an input pipe. As with non-pipe input preprocessors, the command string must contain one occurrence of %s, which is replaced with the filename of the input file. </p>
<p> For example, on many Unix systems, this script will work like the previous example scripts: </p>
<p> lesspipe.sh:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>#! /bin/sh</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>case &quot;$1&quot; in</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>*.Z)<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>uncompress -c $1 2&gt;/dev/null</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>;;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>*)<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>exit 1</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>;;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>esac</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>exit $?</p>
<p> To use this script, put it where it can be executed and set LESSOPEN=&quot;|lesspipe.sh %s&quot;. </p>
<p> Note that a preprocessor cannot output an empty file, since that is interpreted as meaning there is no replacement, and the original file is used. To avoid this, if LESSOPEN starts with two vertical bars, the exit status of the script becomes meaningful. If the exit status is zero, the output is considered to be replacement text, even if it is empty. If the exit status is nonzero, any output is ignored and the original file is used. For compatibility with previous versions of <i>less</i>, if LESSOPEN starts with only one vertical bar, the exit status of the preprocessor is ignored. </p>
<p> When an input pipe is used, a LESSCLOSE postprocessor can be used, but it is usually not necessary since there is no replacement file to clean up. In this case, the replacement file name passed to the LESSCLOSE postprocessor is &quot;-&quot;. </p>
<p> For compatibility with previous versions of <i>less</i>, the input preprocessor or pipe is not used if <i>less</i> is viewing standard input. However, if the first character of LESSOPEN is a dash (-), the input preprocessor is used on standard input as well as other files. In this case, the dash is not considered to be part of the preprocessor command. If standard input is being viewed, the input preprocessor is passed a file name consisting of a single dash. Similarly, if the first two characters of LESSOPEN are vertical bar and dash (|-) or two vertical bars and a dash (||-), the input pipe is used on standard input as well as other files. Again, in this case the dash is not considered to be part of the input pipe command.</p>
<h2>NATIONAL CHARACTER SETS</h2>
<p> There are three types of characters in the input file:</p>
<dl>
<dt>normal characters</p>
<dd> can be displayed directly to the screen.</p>
<dt>control characters</p>
<dd> should not be displayed directly, but are expected to be found in ordinary text files (such as backspace and tab).</p>
<dt>binary characters</p>
<dd> should not be displayed directly and are not expected to be found in text files.</dl>
<p> A &quot;character set&quot; is simply a description of which characters are to be considered normal, control, and binary. The LESSCHARSET environment variable may be used to select a character set. Possible values for LESSCHARSET are:</p>
<dl>
<dt>ascii</p>
<dd> BS, TAB, NL, CR, and formfeed are control characters, all chars with values between 32 and 126 are normal, and all others are binary.</p>
<dt>iso8859</p>
<dd> Selects an ISO 8859 character set. This is the same as ASCII, except characters between 160 and 255 are treated as normal characters.</p>
<dt>latin1</p>
<dd> Same as iso8859.</p>
<dt>latin9</p>
<dd> Same as iso8859.</p>
<dt>dos</p>
<dd> Selects a character set appropriate for MS-DOS.</p>
<dt>ebcdic</p>
<dd> Selects an EBCDIC character set.</p>
<dt>IBM-1047</p>
<dd> Selects an EBCDIC character set used by OS/390 Unix Services. This is the EBCDIC analogue of latin1. You get similar results by setting either LESSCHARSET=IBM-1047 or LC_CTYPE=en_US in your environment.</p>
<dt>koi8-r</p>
<dd> Selects a Russian character set.</p>
<dt>next</p>
<dd> Selects a character set appropriate for NeXT computers.</p>
<dt>utf-8</p>
<dd> Selects the UTF-8 encoding of the ISO 10646 character set. UTF-8 is special in that it supports multi-byte characters in the input file. It is the only character set that supports multi-byte characters.</p>
<dt>windows</p>
<dd> Selects a character set appropriate for Microsoft Windows (cp 1251).</dl>
<p> In rare cases, it may be desired to tailor <i>less</i> to use a character set other than the ones definable by LESSCHARSET. In this case, the environment variable LESSCHARDEF can be used to define a character set. It should be set to a string where each character in the string represents one character in the character set. The character &quot;.&quot; is used for a normal character, &quot;c&quot; for control, and &quot;b&quot; for binary. A decimal number may be used for repetition. For example, &quot;bccc4b.&quot; would mean character 0 is binary, 1, 2 and 3 are control, 4, 5, 6 and 7 are binary, and 8 is normal. All characters after the last are taken to be the same as the last, so characters 9 through 255 would be normal. (This is an example, and does not necessarily represent any real character set.) </p>
<p> This table shows the value of LESSCHARDEF which is equivalent to each of the possible values for LESSCHARSET:</p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td>ascii</td>
<td>8bcccbcc18b95.b
</td>
</tr>
<tr VALIGN=top>
<td>dos</td>
<td>8bcccbcc12bc5b95.b.
</td>
</tr>
<tr VALIGN=top>
<td>ebcdic</td>
<td>5bc6bcc7bcc41b.9b7.9b5.b..8b6.10b6.b9.7b
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>9.8b8.17b3.3b9.7b9.8b8.6b10.b.b.b.
</td>
</tr>
<tr VALIGN=top>
<td>IBM-1047</td>
<td>4cbcbc3b9cbccbccbb4c6bcc5b3cbbc4bc4bccbc
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>191.b
</td>
</tr>
<tr VALIGN=top>
<td>iso8859</td>
<td>8bcccbcc18b95.33b.
</td>
</tr>
<tr VALIGN=top>
<td>koi8-r</td>
<td>8bcccbcc18b95.b128.
</td>
</tr>
<tr VALIGN=top>
<td>latin1</td>
<td>8bcccbcc18b95.33b.
</td>
</tr>
<tr VALIGN=top>
<td>next</td>
<td>8bcccbcc18b95.bb125.bb
</td>
</tr>
</table>
</dl>
<p> If neither LESSCHARSET nor LESSCHARDEF is set, but any of the strings &quot;UTF-8&quot;, &quot;UTF8&quot;, &quot;utf-8&quot; or &quot;utf8&quot; is found in the LC_ALL, LC_CTYPE or LANG environment variables, then the default character set is utf-8. </p>
<p> If that string is not found, but your system supports the <i>setlocale</i> interface, <i>less</i> will use setlocale to determine the character set. setlocale is controlled by setting the LANG or LC_CTYPE environment variables. </p>
<p> Finally, if the <i>setlocale</i> interface is also not available, the default character set is latin1. </p>
<p> Control and binary characters are displayed in standout (reverse video). Each such character is displayed in caret notation if possible (e.g. ^A for control-A). Caret notation is used only if inverting the 0100 bit results in a normal printable character. Otherwise, the character is displayed as a hex number in angle brackets. This format can be changed by setting the LESSBINFMT environment variable. LESSBINFMT may begin with a &quot;*&quot; and one character to select the display attribute: &quot;*k&quot; is blinking, &quot;*d&quot; is bold, &quot;*u&quot; is underlined, &quot;*s&quot; is standout, and &quot;*n&quot; is normal. If LESSBINFMT does not begin with a &quot;*&quot;, normal attribute is assumed. The remainder of LESSBINFMT is a string which may include one printf-style escape sequence (a % followed by x, X, o, d, etc.). For example, if LESSBINFMT is &quot;*u[%x]&quot;, binary characters are displayed in underlined hexadecimal surrounded by brackets. The default if no LESSBINFMT is specified is &quot;*s&lt;%02X&gt;&quot;. Warning: the result of expanding the character via LESSBINFMT must be less than 31 characters. </p>
<p> When the character set is utf-8, the LESSUTFBINFMT environment variable acts similarly to LESSBINFMT but it applies to Unicode code points that were successfully decoded but are unsuitable for display (e.g., unassigned code points). Its default value is &quot;&lt;U+%04lX&gt;&quot;. Note that LESSUTFBINFMT and LESSBINFMT share their display attribute setting (&quot;*x&quot;) so specifying one will affect both; LESSUTFBINFMT is read after LESSBINFMT so its setting, if any, will have priority. Problematic octets in a UTF-8 file (octets of a truncated sequence, octets of a complete but non-shortest form sequence, invalid octets, and stray trailing octets) are displayed individually using LESSBINFMT so as to facilitate diagnostic of how the UTF-8 file is ill-formed.</p>
<h2>PROMPTS</h2>
<p> The -P option allows you to tailor the prompt to your preference. The string given to the -P option replaces the specified prompt string. Certain characters in the string are interpreted specially. The prompt mechanism is rather complicated to provide flexibility, but the ordinary user need not understand the details of constructing personalized prompt strings. </p>
<p> A percent sign followed by a single character is expanded according to what the following character is:</p>
<dl>
<dt>%b<i>X</i></p>
<dd> Replaced by the byte offset into the current input file. The b is followed by a single character (shown as <i>X</i> above) which specifies the line whose byte offset is to be used. If the character is a &quot;t&quot;, the byte offset of the top line in the display is used, an &quot;m&quot; means use the middle line, a &quot;b&quot; means use the bottom line, a &quot;B&quot; means use the line just after the bottom line, and a &quot;j&quot; means use the &quot;target&quot; line, as specified by the -j option.</p>
<dt>%B</p>
<dd> Replaced by the size of the current input file.</p>
<dt>%c</p>
<dd> Replaced by the column number of the text appearing in the first column of the screen.</p>
<dt>%d<i>X</i></p>
<dd> Replaced by the page number of a line in the input file. The line to be used is determined by the <i>X</i>, as with the %b option.</p>
<dt>%D</p>
<dd> Replaced by the number of pages in the input file, or equivalently, the page number of the last line in the input file.</p>
<dt>%E</p>
<dd> Replaced by the name of the editor (from the VISUAL environment variable, or the EDITOR environment variable if VISUAL is not defined). See the discussion of the LESSEDIT feature below.</p>
<dt>%f</p>
<dd> Replaced by the name of the current input file.</p>
<dt>%F</p>
<dd> Replaced by the last component of the name of the current input file.</p>
<dt>%g</p>
<dd> Replaced by the shell-escaped name of the current input file. This is useful when the expanded string will be used in a shell command, such as in LESSEDIT.</p>
<dt>%i</p>
<dd> Replaced by the index of the current file in the list of input files.</p>
<dt>%l<i>X</i></p>
<dd> Replaced by the line number of a line in the input file. The line to be used is determined by the <i>X</i>, as with the %b option.</p>
<dt>%L</p>
<dd> Replaced by the line number of the last line in the input file.</p>
<dt>%m</p>
<dd> Replaced by the total number of input files.</p>
<dt>%p<i>X</i></p>
<dd> Replaced by the percent into the current input file, based on byte offsets. The line used is determined by the <i>X</i> as with the %b option.</p>
<dt>%P<i>X</i></p>
<dd> Replaced by the percent into the current input file, based on line numbers. The line used is determined by the <i>X</i> as with the %b option.</p>
<dt>%s</p>
<dd> Same as %B.</p>
<dt>%t</p>
<dd> Causes any trailing spaces to be removed. Usually used at the end of the string, but may appear anywhere.</p>
<dt>%T</p>
<dd> Normally expands to the word &quot;file&quot;. However if viewing files via a tags list using the -t option, it expands to the word &quot;tag&quot;.</p>
<dt>%x</p>
<dd> Replaced by the name of the next input file in the list.</dl>
<p> If any item is unknown (for example, the file size if input is a pipe), a question mark is printed instead. </p>
<p> The format of the prompt string can be changed depending on certain conditions. A question mark followed by a single character acts like an &quot;IF&quot;: depending on the following character, a condition is evaluated. If the condition is true, any characters following the question mark and condition character, up to a period, are included in the prompt. If the condition is false, such characters are not included. A colon appearing between the question mark and the period can be used to establish an &quot;ELSE&quot;: any characters between the colon and the period are included in the string if and only if the IF condition is false. Condition characters (which follow a question mark) may be:</p>
<dl>
<dt>?a</p>
<dd> True if any characters have been included in the prompt so far.</p>
<dt>?b<i>X</i></p>
<dd> True if the byte offset of the specified line is known.</p>
<dt>?B</p>
<dd> True if the size of current input file is known.</p>
<dt>?c</p>
<dd> True if the text is horizontally shifted (%c is not zero).</p>
<dt>?d<i>X</i></p>
<dd> True if the page number of the specified line is known.</p>
<dt>?e</p>
<dd> True if at end-of-file.</p>
<dt>?f</p>
<dd> True if there is an input filename (that is, if input is not a pipe).</p>
<dt>?l<i>X</i></p>
<dd> True if the line number of the specified line is known.</p>
<dt>?L</p>
<dd> True if the line number of the last line in the file is known.</p>
<dt>?m</p>
<dd> True if there is more than one input file.</p>
<dt>?n</p>
<dd> True if this is the first prompt in a new input file.</p>
<dt>?p<i>X</i></p>
<dd> True if the percent into the current input file, based on byte offsets, of the specified line is known.</p>
<dt>?P<i>X</i></p>
<dd> True if the percent into the current input file, based on line numbers, of the specified line is known.</p>
<dt>?s</p>
<dd> Same as &quot;?B&quot;.</p>
<dt>?x</p>
<dd> True if there is a next input file (that is, if the current input file is not the last one).</dl>
<p> Any characters other than the special ones (question mark, colon, period, percent, and backslash) become literally part of the prompt. Any of the special characters may be included in the prompt literally by preceding it with a backslash. </p>
<p> Some examples: </p>
<p> ?f%f:Standard input. </p>
<p> This prompt prints the filename, if known; otherwise the string &quot;Standard input&quot;. </p>
<p> ?f%f .?ltLine %lt:?pt%pt\%:?btByte %bt:-&#8230; </p>
<p> This prompt would print the filename, if known. The filename is followed by the line number, if known, otherwise the percent if known, otherwise the byte offset if known. Otherwise, a dash is printed. Notice how each question mark has a matching period, and how the % after the %pt is included literally by escaping it with a backslash. </p>
<p> ?n?f%f .?m(%T %i of %m)&nbsp;..?e(END)&nbsp;?x- Next\:&nbsp;%x..%t&quot;; </p>
<p> This prints the filename if this is the first prompt in a file, followed by the &quot;file N of N&quot; message if there is more than one input file. Then, if we are at end-of-file, the string &quot;(END)&quot; is printed followed by the name of the next file, if there is one. Finally, any trailing spaces are truncated. This is the default prompt. For reference, here are the defaults for the other two prompts (-m and -M respectively). Each is broken into two lines here for readability only. </p>
<pre><code>
? n ? f % f.? m(% T &amp; nbsp; % i of &amp; nbsp; % m) &amp; nbsp;
..          ? e(END) &amp; nbsp;
          ? x - Next\: &amp;nbsp;
% x. :
              ? pB % pB\%
              : byte &amp;nbsp;
% bB ? s / % s... % t
              ? f % f.
              ? n
              ? m(% T &amp; nbsp; % i of &amp; nbsp; % m) &amp; nbsp;
..? ltlines &amp;nbsp;
% lt - % lb ? L / % L. : byte &amp;nbsp;
% bB ? s / % s..? e(END) &amp; nbsp;
          ? x - Next\: &amp;nbsp;
% x. :     ? pB % pB\%..% t
</code></pre>
<p> And here is the default message produced by the = command: </p>
<pre><code>
? f % f.    ? m(% T &amp; nbsp; % i of &amp; nbsp; % m) &amp; nbsp;
.           ? ltlines &amp;nbsp;
% lt - % lb ? L / % L..byte &amp;nbsp;
% bB        ? s / % s.&amp;nbsp;
? e(END) &amp; nbsp;:?pB%pB\%..%t
</code></pre>
<p> The prompt expansion features are also used for another purpose: if an environment variable LESSEDIT is defined, it is used as the command to be executed when the v command is invoked. The LESSEDIT string is expanded in the same way as the prompt strings. The default value for LESSEDIT is: </p>
<pre>
        %E&nbsp;?lm+%lm.&nbsp;%g
</pre>
<p> Note that this expands to the editor name, followed by a + and the line number, followed by the shell-escaped file name. If your editor does not accept the &quot;+linenumber&quot; syntax, or has other differences in invocation syntax, the LESSEDIT variable can be changed to modify this default.</p>
<h2>SECURITY</h2>
<p> When the environment variable LESSSECURE is set to 1, <i>less</i> runs in a &quot;secure&quot; mode. This means these features are disabled:</p>
<dl>
<dt>
<dd>
<dl>
<dt>!</p>
<dd> the shell command</p>
<dt>|</p>
<dd> the pipe command</p>
<dt>:e</p>
<dd> the examine command.</p>
<dt>v</p>
<dd> the editing command</p>
<dt>s -o</p>
<dd> log files</p>
<dt>-k</p>
<dd> use of lesskey files</p>
<dt>-t</p>
<dd> use of tags files</p>
<dt>
<dd> metacharacters in filenames, such as *</p>
<dt>
<dd> filename completion (TAB, ^L)</dl>
</dl>
<p> Less can also be compiled to be permanently in &quot;secure&quot; mode.</p>
<h2>COMPATIBILITY WITH MORE</h2>
<p> If the environment variable LESS_IS_MORE is set to 1, or if the program is invoked via a file link named &quot;more&quot;, <i>less</i> behaves (mostly) in conformance with the POSIX &quot;more&quot; command specification. In this mode, less behaves differently in these ways: </p>
<p> The -e option works differently. If the -e option is not set, <i>less</i> behaves as if the -e option were set. If the -e option is set, <i>less</i> behaves as if the -E option were set. </p>
<p> The -m option works differently. If the -m option is not set, the medium prompt is used, and it is prefixed with the string &quot;&#8211;More&#8211;&quot;. If the -m option is set, the short prompt is used. </p>
<p> The -n option acts like the -z option. The normal behavior of the -n option is unavailable in this mode. </p>
<p> The parameter to the -p option is taken to be a <i>less</i> command rather than a search pattern. </p>
<p> The LESS environment variable is ignored, and the MORE environment variable is used in its place.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> Environment variables may be specified either in the system environment as usual, or in a <i><a href="/docs/linux/man/1-lesskey/">lesskey</a></i>(1) file. If environment variables are defined in more than one place, variables defined in a local lesskey file take precedence over variables defined in the system environment, which take precedence over variables defined in the system-wide lesskey file.</p>
<dl>
<dt>COLUMNS</p>
<dd> Sets the number of columns on the screen. Takes precedence over the number of columns specified by the TERM variable. (But if you have a windowing system which supports TIOCGWINSZ or WIOCGETD, the window system&#8217;s idea of the screen size takes precedence over the LINES and COLUMNS environment variables.)</p>
<dt>EDITOR</p>
<dd> The name of the editor (used for the v command).</p>
<dt>HOME</p>
<dd> Name of the user&#8217;s home directory (used to find a lesskey file on Unix and OS/2 systems).</p>
<dt>HOMEDRIVE, HOMEPATH</p>
<dd> Concatenation of the HOMEDRIVE and HOMEPATH environment variables is the name of the user&#8217;s home directory if the HOME variable is not set (only in the Windows version).</p>
<dt>INIT</p>
<dd> Name of the user&#8217;s init directory (used to find a lesskey file on OS/2 systems).</p>
<dt>LANG</p>
<dd> Language for determining the character set.</p>
<dt>LC_CTYPE</p>
<dd> Language for determining the character set.</p>
<dt>LESS</p>
<dd> Options which are passed to <i>less</i> automatically.</p>
<dt>LESSANSIENDCHARS</p>
<dd> Characters which may end an ANSI color escape sequence (default &quot;m&quot;).</p>
<dt>LESSANSIMIDCHARS</p>
<dd> Characters which may appear between the ESC character and the end character in an ANSI color escape sequence (default &quot;0123456789:;[?!&quot;&#8217;#%()*+&nbsp;&quot;.</p>
<dt>LESSBINFMT</p>
<dd> Format for displaying non-printable, non-control characters.</p>
<dt>LESSCHARDEF</p>
<dd> Defines a character set.</p>
<dt>LESSCHARSET</p>
<dd> Selects a predefined character set.</p>
<dt>LESSCLOSE</p>
<dd> Command line to invoke the (optional) input-postprocessor.</p>
<dt>LESSECHO</p>
<dd> Name of the lessecho program (default &quot;lessecho&quot;). The lessecho program is needed to expand metacharacters, such as * and ?, in filenames on Unix systems.</p>
<dt>LESSEDIT</p>
<dd> Editor prototype string (used for the v command). See discussion under PROMPTS.</p>
<dt>LESSGLOBALTAGS</p>
<dd> Name of the command used by the -t option to find global tags. Normally should be set to &quot;global&quot; if your system has the <i><a href="/docs/linux/man/1-global/">global</a></i>(1) command. If not set, global tags are not used.</p>
<dt>LESSHISTFILE</p>
<dd> Name of the history file used to remember search commands and shell commands between invocations of <i>less</i>. If set to &quot;-&quot; or &quot;/dev/null&quot;, a history file is not used. The default is &quot;$XDG_DATA_HOME/lesshst&quot; or &quot;$HOME/.lesshst&quot; on Unix systems, &quot;$HOME/_lesshst&quot; on DOS and Windows systems, or &quot;$HOME/lesshst.ini&quot; or &quot;$INIT/lesshst.ini&quot; on OS/2 systems.</p>
<dt>LESSHISTSIZE</p>
<dd> The maximum number of commands to save in the history file. The default is 100.</p>
<dt>LESSKEYIN</p>
<dd> Name of the default <i>lesskey source</i> file.</p>
<dt>LESSKEY</p>
<dd> Name of the default <i>lesskey binary</i> file. (Not used if &quot;$LESSKEYIN&quot; exists.)</p>
<dt>LESSKEYIN_SYSTEM</p>
<dd> Name of the default system-wide <i>lesskey source</i> file.</p>
<dt>LESSKEY_SYSTEM</p>
<dd> Name of the default system-wide <i>lesskey binary</i> file. (Not used if &quot;$LESSKEYIN_SYSTEM&quot; exists.)</p>
<dt>LESSMETACHARS</p>
<dd> List of characters which are considered &quot;metacharacters&quot; by the shell.</p>
<dt>LESSMETAESCAPE</p>
<dd> Prefix which less will add before each metacharacter in a command sent to the shell. If LESSMETAESCAPE is an empty string, commands containing metacharacters will not be passed to the shell.</p>
<dt>LESSOPEN</p>
<dd> Command line to invoke the (optional) input-preprocessor.</p>
<dt>LESSSECURE</p>
<dd> Runs less in &quot;secure&quot; mode. See discussion under SECURITY.</p>
<dt>LESSSEPARATOR</p>
<dd> String to be appended to a directory name in filename completion.</p>
<dt>LESSUTFBINFMT</p>
<dd> Format for displaying non-printable Unicode code points.</p>
<dt>LESS_IS_MORE</p>
<dd> Emulate the <i><a href="/docs/linux/man/1-more/">more</a></i>(1) command.</p>
<dt>LINES</p>
<dd> Sets the number of lines on the screen. Takes precedence over the number of lines specified by the TERM variable. (But if you have a windowing system which supports TIOCGWINSZ or WIOCGETD, the window system&#8217;s idea of the screen size takes precedence over the LINES and COLUMNS environment variables.)</p>
<dt>MORE</p>
<dd> Options which are passed to <i>less</i> automatically when running in <i>more</i> compatible mode.</p>
<dt>PATH</p>
<dd> User&#8217;s search path (used to find a lesskey file on MS-DOS and OS/2 systems).</p>
<dt>SHELL</p>
<dd> The shell used to execute the ! command, as well as to expand filenames.</p>
<dt>TERM</p>
<dd> The type of terminal on which <i>less</i> is being run.</p>
<dt>VISUAL</p>
<dd> The name of the editor (used for the v command).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lesskey/">lesskey</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1984-2021 Mark Nudelman </p>
<p> less is part of the GNU project and is free software. You can redistribute it and/or modify it under the terms of either (1) the GNU General Public License as published by the Free Software Foundation; or (2) the Less License. See the file README in the less distribution for more details regarding redistribution. You should have received a copy of the GNU General Public License along with the source for less; see the file COPYING. If not, write to the Free Software Foundation, 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA. You should also have received a copy of the Less License; see the file LICENSE. </p>
<p> less is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.</p>
<h2>AUTHOR</h2>
<p> Mark Nudelman<br />
 Report bugs at <a rel="nofollow" href="https://github.com/gwsw/less/issues.">https://github.com/gwsw/less/issues.</a><br />
 For more information, see the less homepage at<br />
 <a rel="nofollow" href="https://greenwoodsoftware.com/less">https://greenwoodsoftware.com/less</a> </p>
<h2>Index</h2>
