---
title: "editor(1)"
name: "editor"
section: "1"
letter: "e"
url: "/docs/linux/man/1-editor/"
description: "nano – Nano’s ANOther editor, inspired by Pico"
---

<h2 class="name">NAME</h2>
<p> nano &#8211; Nano&#8217;s ANOther editor, inspired by Pico</p>
<h2>SYNOPSIS</h2>
<p> <code>nano</code> [<i>options</i>] [[<code>+</code><i>line</i>[<code>,</code><i>column</i>]] <i>file</i>]&#8230; </p>
<p> <code>nano</code> [<i>options</i>] [[<code>+</code>[<code>crCR</code>](<code>/</code>|<code>?</code>)<i>string</i>] <i>file</i>]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>nano</code> is a small and friendly editor. It copies the look and feel of Pico, but is free software, and implements several features that Pico lacks, such as: opening multiple files, scrolling per line, undo/redo, syntax coloring, line numbering, and soft-wrapping overlong lines. </p>
<p> When giving a filename on the command line, the cursor can be put on a specific line by adding the line number with a plus sign (<code>+</code>) before the filename, and even in a specific column by adding it with a comma. (Negative numbers count from the end of the file or line.) The cursor can be put on the first or last occurrence of a specific string by specifying that string after <code>+/</code> or <code>+?</code> before the filename. The string can be made case sensitive and/or caused to be interpreted as a regular expression by inserting <code>c</code> and/or <code>r</code> after the <code>+</code> sign. These search modes can be explicitly disabled by using the uppercase variant of those letters: <code>C</code> and/or <code>R</code>. When the string contains spaces, it needs to be enclosed in quotes. To give an example: to open a file at the first occurrence of the word &quot;Foo&quot;, you would do: </p>
<dl>
<dt>
<dd> <code>nano +c/Foo </code><i>file</i></dl>
<p> As a special case: if instead of a filename a dash (<code>&#8211;</code>) is given, <code>nano</code> will read data from standard input. </p>
<h2>EDITING</h2>
<p> Entering text and moving around in a file is straightforward: typing the letters and using the normal cursor movement keys. Commands are entered by using the Control (^) and the Alt or Meta (M-) keys. Typing <code>^K</code> deletes the current line and puts it in the cutbuffer. Consecutive <code>^K</code>s will put all deleted lines together in the cutbuffer. Any cursor movement or executing any other command will cause the next <code>^K</code> to overwrite the cutbuffer. A <code>^U</code> will paste the current contents of the cutbuffer at the current cursor position. </p>
<p> When a more precise piece of text needs to be cut or copied, you can mark its start with <code>^6</code>, move the cursor to its end (the marked text will be highlighted), and then use <code>^K</code> to cut it, or <code>M-6</code> to copy it to the cutbuffer. You can also save the marked text to a file with <code>^O</code>, or spell check it with <code>^T^T</code>. </p>
<p> On some terminals, text can be selected also by holding down Shift while using the arrow keys. Holding down the Ctrl or Alt key too will increase the stride. Any cursor movement without Shift being held will cancel such a selection. </p>
<p> The two lines at the bottom of the screen show some important commands; the built-in help (<code>^G</code>) lists all the available ones. The default key bindings can be changed via a <i>nanorc</i> file &#8212; see <code><a href="/docs/linux/man/5-nanorc/">nanorc</a></code>(5). </p>
<h2>NOTICE</h2>
<p> Since version 4.0, <code>nano</code> by default: </p>
<dl>
<dt>
<dd> &bull; does not automatically hard-wrap lines that become overlong,<br />
 &bull; includes the line below the title bar in the editing area,<br />
 &bull; does linewise (smooth) scrolling.</dl>
<p> If you want the old, Pico behavior back, you can use <code>&#8211;breaklonglines</code>, <code>&#8211;emptyline</code>, and <code>&#8211;jumpyscrolling</code> (or <code>-bej</code> for short). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code>, <code>&#8211;smarthome</code></p>
<dd> Make the Home key smarter. When Home is pressed anywhere but at the very beginning of non-whitespace characters on a line, the cursor will jump to that beginning (either forwards or backwards). If the cursor is already at that position, it will jump to the true beginning of the line.</p>
<dt><code>-B</code>, <code>&#8211;backup</code></p>
<dd> When saving a file, back up the previous version of it, using the current filename suffixed with a tilde (<code>~</code>).</p>
<dt><code>-C&nbsp;</code><i>directory</i>, <code>&#8211;backupdir=</code><i>directory</i></p>
<dd> Make and keep not just one backup file, but make and keep a uniquely numbered one every time a file is saved &#8212; when backups are enabled (<code>-B</code>). The uniquely numbered files are stored in the specified <i>directory</i>.</p>
<dt><code>-D</code>, <code>&#8211;boldtext</code></p>
<dd> For the interface, use bold instead of reverse video. This will be overridden by setting the options <code>titlecolor</code>, <code>statuscolor</code>, <code>keycolor</code>, <code>functioncolor</code>, <code>numbercolor</code>, and/or <code>selectedcolor</code> in your nanorc file. See <code><a href="/docs/linux/man/5-nanorc/">nanorc</a></code>(5).</p>
<dt><code>-E</code>, <code>&#8211;tabstospaces</code></p>
<dd> Convert each typed tab to spaces &#8212; to the number of spaces that a tab at that position would take up.</p>
<dt><code>-F</code>, <code>&#8211;multibuffer</code></p>
<dd> Read a file into a new buffer by default.</p>
<dt><code>-G</code>, <code>&#8211;locking</code></p>
<dd> Use vim-style file locking when editing files.</p>
<dt><code>-H</code>, <code>&#8211;historylog</code></p>
<dd> Save the last hundred search strings and replacement strings and executed commands, so they can be easily reused in later sessions.</p>
<dt><code>-I</code>, <code>&#8211;ignorercfiles</code></p>
<dd> Don&#8217;t look at the system&#8217;s <i>nanorc</i> nor at the user&#8217;s <i>nanorc</i>.</p>
<dt><code>-J&nbsp;</code><i>number</i>, <code>&#8211;guidestripe=</code><i>number</i></p>
<dd> Draw a vertical stripe at the given column, to help judge the width of the text. (The color of the stripe can be changed with <code>set stripecolor</code> in your <i>nanorc</i> file.)</p>
<dt><code>-K</code>, <code>&#8211;rawsequences</code></p>
<dd> Interpret escape sequences directly, instead of asking <code>ncurses</code> to translate them. (If you need this option to get some keys to work properly, it means that the terminfo terminal description that is used does not fully match the actual behavior of your terminal. This can happen when you ssh into a BSD machine, for example.) Using this option disables <code>nano</code>&#8216;s mouse support.</p>
<dt><code>-L</code>, <code>&#8211;nonewlines</code></p>
<dd> Don&#8217;t automatically add a newline when a text does not end with one. (This can cause you to save non-POSIX text files.)</p>
<dt><code>-M</code>, <code>&#8211;trimblanks</code></p>
<dd> Snip trailing whitespace from the wrapped line when automatic hard-wrapping occurs or when text is justified.</p>
<dt><code>-N</code>, <code>&#8211;noconvert</code></p>
<dd> Disable automatic conversion of files from DOS/Mac format.</p>
<dt><code>-O</code>, <code>&#8211;bookstyle</code></p>
<dd> When justifying, treat any line that starts with whitespace as the beginning of a paragraph (unless auto-indenting is on).</p>
<dt><code>-P</code>, <code>&#8211;positionlog</code></p>
<dd> For the 200 most recent files, log the last position of the cursor, and place it at that position again upon reopening such a file.</p>
<dt><code>-Q &quot;</code><i>regex</i><code>&quot;</code>, <code>&#8211;quotestr=&quot;</code><i>regex</i><code>&quot;</code></p>
<dd> Set the regular expression for matching the quoting part of a line. The default value is &quot;<code>^([&nbsp;	]*([!#%:;&gt;|}]|//))+</code>&quot;. (Note that <code>	</code> stands for an actual Tab.) This makes it possible to rejustify blocks of quoted text when composing email, and to rewrap blocks of line comments when writing source code.</p>
<dt><code>-R</code>, <code>&#8211;restricted</code></p>
<dd> Restricted mode: don&#8217;t read or write to any file not specified on the command line. This means: don&#8217;t read or write history files; don&#8217;t allow suspending; don&#8217;t allow spell checking; don&#8217;t allow a file to be appended to, prepended to, or saved under a different name if it already has one; and don&#8217;t make backup files. Restricted mode can also be activated by invoking <code>nano</code> with any name beginning with &#8216;r&#8217; (e.g. &quot;rnano&quot;).</p>
<dt><code>-S</code>, <code>&#8211;softwrap</code></p>
<dd> Display over multiple screen rows lines that exceed the screen&#8217;s width. (You can make this soft-wrapping occur at whitespace instead of rudely at the screen&#8217;s edge, by using also <code>&#8211;atblanks</code>.) (The old short option, <code>-$</code>, is deprecated.)</p>
<dt><code>-T&nbsp;</code><i>number</i>, <code>&#8211;tabsize=</code><i>number</i></p>
<dd> Set the size (width) of a tab to <i>number</i> columns. The value of <i>number</i> must be greater than 0. The default value is <code>8</code>.</p>
<dt><code>-U</code>, <code>&#8211;quickblank</code></p>
<dd> Make status-bar messages disappear after 1 keystroke instead of after 20. Note that option <code>-c</code> (<code>&#8211;constantshow</code>) overrides this. When option <code>&#8211;minibar</code> or <code>&#8211;zero</code> is in effect, <code>&#8211;quickblank</code> makes a message disappear after 0.8 seconds instead of after the default 1.5 seconds.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Show the current version number and exit.</p>
<dt><code>-W</code>, <code>&#8211;wordbounds</code></p>
<dd> Detect word boundaries differently by treating punctuation characters as part of a word.</p>
<dt><code>-X &quot;</code><i>characters</i><code>&quot;</code>, <code>&#8211;wordchars=&quot;</code><i>characters</i><code>&quot;</code></p>
<dd> Specify which other characters (besides the normal alphanumeric ones) should be considered as part of a word. When using this option, you probably want to omit <code>-W</code> (<code>&#8211;wordbounds</code>).</p>
<dt><code>-Y&nbsp;</code><i>name</i>, <code>&#8211;syntax=</code><i>name</i></p>
<dd> Specify the name of the syntax highlighting to use from among the ones defined in the <i>nanorc</i> files.</p>
<dt><code>-Z</code>, <code>&#8211;zap</code></p>
<dd> Let an unmodified Backspace or Delete erase the marked region (instead of a single character, and without affecting the cutbuffer).</p>
<dt><code>-a</code>, <code>&#8211;atblanks</code></p>
<dd> When doing soft line wrapping, wrap lines at whitespace instead of always at the edge of the screen.</p>
<dt><code>-b</code>, <code>&#8211;breaklonglines</code></p>
<dd> Automatically hard-wrap the current line when it becomes overlong. (This option is the opposite of <code>-w</code> (<code>&#8211;nowrap</code>) &#8212; the last one given takes effect.)</p>
<dt><code>-c</code>, <code>&#8211;constantshow</code></p>
<dd> Constantly show the cursor position on the status bar. Note that this overrides option <code>-U</code> (<code>&#8211;quickblank</code>).</p>
<dt><code>-d</code>, <code>&#8211;rebinddelete</code></p>
<dd> Interpret the Delete and Backspace keys differently so that both Backspace and Delete work properly. You should only use this option when on your system either Backspace acts like Delete or Delete acts like Backspace.</p>
<dt><code>-e</code>, <code>&#8211;emptyline</code></p>
<dd> Do not use the line below the title bar, leaving it entirely blank.</p>
<dt><code>-f&nbsp;</code><i>file</i>, <code>&#8211;rcfile=</code><i>file</i></p>
<dd> Read only this <i>file</i> for setting nano&#8217;s options, instead of reading both the system-wide and the user&#8217;s nanorc files.</p>
<dt><code>-g</code>, <code>&#8211;showcursor</code></p>
<dd> Make the cursor visible in the file browser (putting it on the highlighted item) and in the help viewer. Useful for braille users and people with poor vision.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show a summary of the available command-line options and exit.</p>
<dt><code>-i</code>, <code>&#8211;autoindent</code></p>
<dd> Automatically indent a newly created line to the same number of tabs and/or spaces as the previous line (or as the next line if the previous line is the beginning of a paragraph).</p>
<dt><code>-j</code>, <code>&#8211;jumpyscrolling</code></p>
<dd> Scroll the buffer contents per half-screen instead of per line.</p>
<dt><code>-k</code>, <code>&#8211;cutfromcursor</code></p>
<dd> Make the &#8216;Cut Text&#8217; command (normally <code>^K</code>) cut from the current cursor position to the end of the line, instead of cutting the entire line.</p>
<dt><code>-l</code>, <code>&#8211;linenumbers</code></p>
<dd> Display line numbers to the left of the text area. (Any line with an anchor additionally gets a mark in the margin.)</p>
<dt><code>-m</code>, <code>&#8211;mouse</code></p>
<dd> Enable mouse support, if available for your system. When enabled, mouse clicks can be used to place the cursor, set the mark (with a double click), and execute shortcuts. The mouse will work in the X Window System, and on the console when gpm is running. Text can still be selected through dragging by holding down the Shift key.</p>
<dt><code>-n</code>, <code>&#8211;noread</code></p>
<dd> Treat any name given on the command line as a new file. This allows <code>nano</code> to write to named pipes: it will start with a blank buffer, and will write to the pipe when the user saves the &quot;file&quot;. This way <code>nano</code> can be used as an editor in combination with for instance <code>gpg</code> without having to write sensitive data to disk first.</p>
<dt><code>-o&nbsp;</code><i>directory</i>, <code>&#8211;operatingdir=</code><i>directory</i></p>
<dd> Set the operating directory. This makes <code>nano</code> set up something similar to a chroot.</p>
<dt><code>-p</code>, <code>&#8211;preserve</code></p>
<dd> Preserve the XON and XOFF sequences (<code>^Q</code> and <code>^S</code>) so they will be caught by the terminal.</p>
<dt><code>-q</code>, <code>&#8211;indicator</code></p>
<dd> Display a &quot;scrollbar&quot; on the righthand side of the edit window. It shows the position of the viewport in the buffer and how much of the buffer is covered by the viewport.</p>
<dt><code>-r&nbsp;</code><i>number</i>, <code>&#8211;fill=</code><i>number</i></p>
<dd> Set the target width for justifying and automatic hard-wrapping at this <i>number</i> of columns. If the value is 0 or less, wrapping will occur at the width of the screen minus <i>number</i> columns, allowing the wrap point to vary along with the width of the screen if the screen is resized. The default value is <code>-8</code>.</p>
<dt><code>-s </code><i>program</i> [<i>argument </i>&#8230;], <code>&#8211;speller=</code><i>program</i> [<i>argument </i>&#8230;]</p>
<dd> Use this command to perform spell checking and correcting, instead of using the built-in corrector that calls <code><a href="/docs/linux/man/1-hunspell/">hunspell</a></code>(1) or <code><a href="/docs/linux/man/1-spell/">spell</a></code>(1).</p>
<dt><code>-t</code>, <code>&#8211;saveonexit</code></p>
<dd> Save a changed buffer without prompting (when exiting with <code>^X</code>). (The old form of the long option, <code>&#8211;tempfile</code>, is deprecated.)</p>
<dt><code>-u</code>, <code>&#8211;unix</code></p>
<dd> Save a file by default in Unix format. This overrides nano&#8217;s default behavior of saving a file in the format that it had. (This option has no effect when you also use <code>&#8211;noconvert</code>.)</p>
<dt><code>-v</code>, <code>&#8211;view</code></p>
<dd> Just view the file and disallow editing: read-only mode. This mode allows the user to open also other files for viewing, unless <code>&#8211;restricted</code> is given too.</p>
<dt><code>-w</code>, <code>&#8211;nowrap</code></p>
<dd> Do not automatically hard-wrap the current line when it becomes overlong. This is the default. (This option is the opposite of <code>-b</code> (<code>&#8211;breaklonglines</code>) &#8212; the last one given takes effect.)</p>
<dt><code>-x</code>, <code>&#8211;nohelp</code></p>
<dd> Don&#8217;t show the two help lines at the bottom of the screen.</p>
<dt><code>-y</code>, <code>&#8211;afterends</code></p>
<dd> Make Ctrl+Right and Ctrl+Delete stop at word ends instead of beginnings.</p>
<dt><code>-z</code>, <code>&#8211;suspendable</code></p>
<dd> Obsolete option; ignored. Suspension is enabled by default, reachable via <code>^T^Z</code>. (If you want a plain <code>^Z</code> to suspend nano, add <code>bind ^Z suspend main</code> to your nanorc.)</p>
<dt><code>-%</code>, <code>&#8211;stateflags</code></p>
<dd> Use the top-right corner of the screen for showing some state flags: <code>I</code> when auto-indenting, <code>M</code> when the mark is on, <code>L</code> when hard-wrapping (breaking long lines), <code>R</code> when recording a macro, and <code>S</code> when soft-wrapping. When the buffer is modified, a star (<code>*</code>) is shown after the filename in the center of the title bar.</p>
<dt><code>-_</code>, <code>&#8211;minibar</code></p>
<dd> Suppress the title bar and instead show information about the current buffer at the bottom of the screen, in the space for the status bar. In this &quot;minibar&quot; the filename is shown on the left, followed by an asterisk if the buffer has been modified. On the right are displayed the current line and column number, the code of the character under the cursor (in Unicode format: U+xxxx), the same flags as are shown by <code>&#8211;stateflags</code>, and a percentage that expresses how far the cursor is into the file (linewise). When a file is loaded or saved, and also when switching between buffers, the number of lines in the buffer is displayed after the filename. This number is cleared upon the next keystroke, or replaced with an [i/n] counter when multiple buffers are open. The line plus column numbers and the character code are displayed only when <code>&#8211;constantshow</code> is used, and can be toggled on and off with <code>M-C</code>. The state flags are displayed only when <code>&#8211;stateflags</code> is used.</p>
<dt><code>-0</code>, <code>&#8211;zero</code></p>
<dd> Hide all elements of the interface (title bar, status bar, and help lines) and use all rows of the terminal for showing the contents of the buffer. The status bar appears only when there is a significant message, and disappears after 1.5 seconds or upon the next keystroke. With <code>M-Z</code> the title bar plus status bar can be toggled. With <code>M-X</code> the help lines.</p>
<dt><code>-!</code>, <code>&#8211;magic</code></p>
<dd> When neither the file&#8217;s name nor its first line give a clue, try using libmagic to determine the applicable syntax. </p>
</dl>
<h2>TOGGLES</h2>
<p> Several of the above options can be switched on and off also while <code>nano</code> is running. For example, <code>M-L</code> toggles the hard-wrapping of long lines, <code>M-S</code> toggles soft-wrapping, <code>M-N</code> toggles line numbers, <code>M-M</code> toggles the mouse, <code>M-I</code> auto-indentation, and <code>M-X</code> the help lines. See at the end of the <code>^G</code> help text for a complete list. </p>
<p> The <code>M-X</code> toggle is special: it works in all menus except the help viewer and the linter. All other toggles work in the main menu only. </p>
<h2>FILES</h2>
<p> When <code>&#8211;rcfile</code> is given, <code>nano</code> will read just the specified file for setting its options and syntaxes and key bindings. Without that option, <code>nano</code> will read two configuration files: first the system&#8217;s <i>nanorc</i> (if it exists), and then the user&#8217;s <i>nanorc</i> (if it exists), either <i>~/.nanorc</i> or <i>$XDG_CONFIG_HOME/nano/nanorc</i> or <i>~/.config/nano/nanorc</i>, whichever is encountered first. See <code><a href="/docs/linux/man/5-nanorc/">nanorc</a></code>(5) for more information on the possible contents of those files. </p>
<p> See <i>/usr/share/nano/</i> and <i>/usr/share/nano/extra/</i> for available syntax-coloring definitions. </p>
<h2>NOTES</h2>
<p> If no alternative spell checker command is specified on the command line nor in one of the <i>nanorc</i> files, <code>nano</code> will check the <code>SPELL</code> environment variable for one. </p>
<p> In some cases <code>nano</code> will try to dump the buffer into an emergency file. This will happen mainly if <code>nano</code> receives a SIGHUP or SIGTERM or runs out of memory. It will write the buffer into a file named <i>nano.save</i> if the buffer didn&#8217;t have a name already, or will add a &quot;.save&quot; suffix to the current filename. If an emergency file with that name already exists in the current directory, it will add &quot;.save&quot; plus a number (e.g. &quot;.save.1&quot;) to the current filename in order to make it unique. In multibuffer mode, <code>nano</code> will write all the open buffers to their respective emergency files. </p>
<h2>BUGS</h2>
<p> The recording and playback of keyboard macros works correctly only on a terminal emulator, not on a Linux console (VT), because the latter does not by default distinguish modified from unmodified arrow keys. </p>
<p> Please report any other bugs that you encounter via:<br />
 <i><a rel="nofollow" href="https://savannah.gnu.org/bugs/?group=nano">https://savannah.gnu.org/bugs/?group=nano</a></i>. </p>
<p> When nano crashes, it will save any modified buffers to emergency .save files. If you are able to reproduce the crash and you want to get a backtrace, define the environment variable <code>NANO_NOCATCH</code>. </p>
<h2>HOMEPAGE</h2>
<p> <i><a rel="nofollow" href="https://nano-editor.org/">https://nano-editor.org/</a></i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-nanorc/">nanorc</a></code>(5) </p>
<p> <i>/usr/share/doc/nano/</i> (or equivalent on your system) </p>
<h2>Index</h2>
