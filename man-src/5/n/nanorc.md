---
title: "nanorc(5)"
name: "nanorc"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nanorc/"
description: "nanorc – GNU nano’s configuration file"
---

<p>nanorc &#8211; GNU nano&#8217;s configuration file</p>
<h2>Description</h2>
<p>The <i>nanorc</i> files contain the default settings for <code>nano</code>, a small and friendly editor. During startup, if <code>&#8211;rcfile</code> is not given, <code>nano</code> will read two files: first the system-wide settings, from <i>/etc/nanorc</i> (the exact path might be different on your system), and then the user-specific settings, either from <i>~/.nanorc</i> or from <i>$XDG_CONFIG_HOME/nano/nanorc</i> or from <i>~/.config/nano/nanorc</i>, whichever is encountered first. If <code>&#8211;rcfile</code> is given, <code>nano</code> will read just the specified settings file. </p>
<h2>Notice</h2>
<p>Since version 4.0, <code>nano</code> by default: </p>
<dl>
<dd>&bull; does not automatically hard-wrap lines that become overlong,<br />
 &bull; includes the line below the title bar in the editing area,<br />
 &bull; does linewise (smooth) scrolling.</dl>
<p> To get the old, Pico behavior back, you can use <code>set breaklonglines</code>, <code>set emptyline</code>, and <code>set jumpyscrolling</code>.</p>
<h2>Options</h2>
<p>The configuration file accepts a series of <code>set</code> and <code>unset</code> commands, which can be used to configure nano on startup without using command-line options. Additionally, there are some commands to define syntax highlighting and to rebind keys &#8212; see the two separate sections on those. <code>nano</code> reads one command per line. All commands and keywords should be written in lowercase. </p>
<p> Options in <i>nanorc</i> files take precedence over nano&#8217;s defaults, and command-line options override <i>nanorc</i> settings. Also, options that do not take an argument are unset by default. So using the <code>unset</code> command is only needed when wanting to override a setting of the system&#8217;s <i>nanorc</i> file in your own <i>nanorc</i>. Options that take an argument cannot be unset. </p>
<p> Quotes inside the <i>characters</i> parameters below should not be escaped. The last double quote on the line will be seen as the closing quote. </p>
<p> The supported commands and arguments are:</p>
<dl>
<dt><code>set afterends</code></p>
<dd>Make Ctrl+Right and Ctrl+Delete stop at word ends instead of beginnings.</p>
<dt><code>set allow_insecure_backup</code></p>
<dd>When backing up files, allow the backup to succeed even if its permissions can&#8217;t be (re)set due to special OS considerations. You should NOT enable this option unless you are sure you need it.</p>
<dt><code>set atblanks</code></p>
<dd>When soft line wrapping is enabled, make it wrap lines at blank characters (tabs and spaces) instead of always at the edge of the screen.</p>
<dt><code>set autoindent</code></p>
<dd>Automatically indent a newly created line to the same number of tabs and/or spaces as the previous line (or as the next line if the previous line is the beginning of a paragraph).</p>
<dt><code>set backup</code></p>
<dd>When saving a file, create a backup file by adding a tilde (<code>~</code>) to the file&#8217;s name.</p>
<dt><code>set backupdir </code><i>directory</i></p>
<dd>Make and keep not just one backup file, but make and keep a uniquely numbered one every time a file is saved &#8212; when backups are enabled with <code>set backup</code> or <code>&#8211;backup</code> or <code>-B</code>. The uniquely numbered files are stored in the specified <i>directory</i>.</p>
<dt><code>set boldtext</code></p>
<dd>Use bold instead of reverse video for the title bar, status bar, key combos, function tags, line numbers, and selected text. This can be overridden by setting the options <code>titlecolor</code>, <code>statuscolor</code>, <code>keycolor</code>, <code>functioncolor</code>, <code>numbercolor</code>, and <code>selectedcolor</code>.</p>
<dt><code>set bookstyle</code></p>
<dd>When justifying, treat any line that starts with whitespace as the beginning of a paragraph (unless auto-indenting is on).</p>
<dt><code>set brackets &quot;</code><i>characters</i><code>&quot;</code></p>
<dd>Set the characters treated as closing brackets when justifying paragraphs. This may not include blank characters. Only closing punctuation (see <code>set punct</code>), optionally followed by the specified closing brackets, can end sentences. The default value is &quot;<code>&quot;&#8217;)&gt;]}</code>&quot;.</p>
<dt><code>set breaklonglines</code></p>
<dd>Automatically hard-wrap the current line when it becomes overlong.</p>
<dt><code>set casesensitive</code></p>
<dd>Do case-sensitive searches by default.</p>
<dt><code>set constantshow</code></p>
<dd>Constantly display the cursor position in the status bar. This overrides the option <code>quickblank</code>.</p>
<dt><code>set cutfromcursor</code></p>
<dd>Use cut-from-cursor-to-end-of-line by default, instead of cutting the whole line.</p>
<dt><code>set emptyline</code></p>
<dd>Do not use the line below the title bar, leaving it entirely blank.</p>
<dt><code>set errorcolor </code>[<code>bold,</code>][<code>italic,</code>]<i>fgcolor</i><code>,</code><i>bgcolor</i></p>
<dd>Use this color combination for the status bar when an error message is displayed. The default value is <code>bold,white,red</code>. See <code>set titlecolor</code> for valid color names.</p>
<dt><code>set fill </code><i>number</i></p>
<dd>Set the target width for justifying and automatic hard-wrapping at this <i>number</i> of columns. If the value is 0 or less, wrapping will occur at the width of the screen minus <i>number</i> columns, allowing the wrap point to vary along with the width of the screen if the screen is resized. The default value is <code>-8</code>.</p>
<dt><code>set functioncolor </code>[<code>bold,</code>][<code>italic,</code>]<i>fgcolor</i><code>,</code><i>bgcolor</i></p>
<dd>Use this color combination for the concise function descriptions in the two help lines at the bottom of the screen. See <code>set titlecolor</code> for more details.</p>
<dt><code>set guidestripe </code><i>number</i></p>
<dd>Draw a vertical stripe at the given column, to help judge the width of the text. (The color of the stripe can be changed with <code>set stripecolor</code>.)</p>
<dt><code>set historylog</code></p>
<dd>Save the last hundred search strings and replacement strings and executed commands, so they can be easily reused in later sessions.</p>
<dt><code>set indicator</code></p>
<dd>Display a &quot;scrollbar&quot; on the righthand side of the edit window. It shows the position of the viewport in the buffer and how much of the buffer is covered by the viewport.</p>
<dt><code>set jumpyscrolling</code></p>
<dd>Scroll the buffer contents per half-screen instead of per line.</p>
<dt><code>set keycolor </code>[<code>bold,</code>][<code>italic,</code>]<i>fgcolor</i><code>,</code><i>bgcolor</i></p>
<dd>Use this color combination for the shortcut key combos in the two help lines at the bottom of the screen. See <code>set titlecolor</code> for more details.</p>
<dt><code>set linenumbers</code></p>
<dd>Display line numbers to the left of the text area. (Any line with an anchor additionally gets a mark in the margin.)</p>
<dt><code>set locking</code></p>
<dd>Enable vim-style lock-files for when editing files.</p>
<dt><code>set magic</code></p>
<dd>When neither the file&#8217;s name nor its first line give a clue, try using libmagic to determine the applicable syntax. (Calling libmagic can be relatively time consuming. It is therefore not done by default.)</p>
<dt><code>set matchbrackets &quot;</code><i>characters</i><code>&quot;</code></p>
<dd>Specify the opening and closing brackets that can be found by bracket searches. This may not include blank characters. The opening set must come before the closing set, and the two sets must be in the same order. The default value is &quot;<code>(&lt;[{)&gt;]}</code>&quot;.</p>
<dt><code>set minibar</code></p>
<dd>Suppress the title bar and instead show information about the current buffer at the bottom of the screen, in the space for the status bar. In this &quot;minibar&quot; the filename is shown on the left, followed by an asterisk if the buffer has been modified. On the right are displayed the current line and column number, the code of the character under the cursor (in Unicode format: U+xxxx), the same flags as are shown by <code>set stateflags</code>, and a percentage that expresses how far the cursor is into the file (linewise). When a file is loaded or saved, and also when switching between buffers, the number of lines in the buffer is displayed after the filename. This number is cleared upon the next keystroke, or replaced with an [i/n] counter when multiple buffers are open. The line plus column numbers and the character code are displayed only when <code>set constantshow</code> is used, and can be toggled on and off with <code>M-C</code>. The state flags are displayed only when <code>set stateflags</code> is used.</p>
<dt><code>set minicolor </code>[<code>bold,</code>][<code>italic,</code>]<i>fgcolor</i><code>,</code><i>bgcolor</i></p>
<dd>Use this color combination for the minibar. (When this option is not specified, the colors of the title bar are used.) See <code>set titlecolor</code> for more details.</p>
<dt><code>set mouse</code></p>
<dd>Enable mouse support, if available for your system. When enabled, mouse clicks can be used to place the cursor, set the mark (with a double click), and execute shortcuts. The mouse will work in the X Window System, and on the console when gpm is running. Text can still be selected through dragging by holding down the Shift key.</p>
<dt><code>set multibuffer</code></p>
<dd>When reading in a file with <code>^R</code>, insert it into a new buffer by default.</p>
<dt><code>set noconvert</code></p>
<dd>Don&#8217;t convert files from DOS/Mac format.</p>
<dt><code>set nohelp</code></p>
<dd>Don&#8217;t display the two help lines at the bottom of the screen.</p>
<dt><code>set nonewlines</code></p>
<dd>Don&#8217;t automatically add a newline when a text does not end with one. (This can cause you to save non-POSIX text files.)</p>
<dt><code>set nowrap</code></p>
<dd>Deprecated option since it has become the default setting. When needed, use <code>unset breaklonglines</code> instead.</p>
<dt><code>set numbercolor </code>[<code>bold,</code>][<code>italic,</code>]<i>fgcolor</i><code>,</code><i>bgcolor</i></p>
<dd>Use this color combination for line numbers. See <code>set titlecolor</code> for more details.</p>
<dt><code>set operatingdir </code><i>directory</i></p>
<dd><code>nano</code> will only read and write files inside <i>directory</i> and its subdirectories. Also, the current directory is changed to here, so files are inserted from this directory. By default, the operating directory feature is turned off.</p>
<dt><code>set positionlog</code></p>
<dd>Save the cursor position of files between editing sessions. The cursor position is remembered for the 200 most-recently edited files.</p>
<dt><code>set preserve</code></p>
<dd>Preserve the XON and XOFF keys (<code>^Q</code> and <code>^S</code>).</p>
<dt><code>set promptcolor </code>[<code>bold,</code>][<code>italic,</code>]<i>fgcolor</i><code>,</code><i>bgcolor</i></p>
<dd>Use this color combination for the prompt bar. (When this option is not specified, the colors of the title bar are used.) See <code>set titlecolor</code> for more details.</p>
<dt><code>set punct &quot;</code><i>characters</i><code>&quot;</code></p>
<dd>Set the characters treated as closing punctuation when justifying paragraphs. This may not include blank characters. Only the specfified closing punctuation, optionally followed by closing brackets (see <code>brackets</code>), can end sentences. The default value is &quot;<code>!.?</code>&quot;.</p>
<dt><code>set quickblank</code></p>
<dd>Make status-bar messages disappear after 1 keystroke instead of after 20. Note that option <code>constantshow</code> overrides this. When option <code>minibar</code> or <code>zero</code> is in effect, <code>quickblank</code> makes a message disappear after 0.8 seconds instead of after the default 1.5 seconds.</p>
<dt><code>set quotestr &quot;</code><i>regex</i><code>&quot;</code></p>
<dd>Set the regular expression for matching the quoting part of a line. The default value is &quot;<code>^([&nbsp;	]*([!#%:;&gt;|}]|//))+</code>&quot;. (Note that <code>	</code> stands for an actual Tab character.) This makes it possible to rejustify blocks of quoted text when composing email, and to rewrap blocks of line comments when writing source code.</p>
<dt><code>set rawsequences</code></p>
<dd>Interpret escape sequences directly, instead of asking <code>ncurses</code> to translate them. (If you need this option to get some keys to work properly, it means that the terminfo terminal description that is used does not fully match the actual behavior of your terminal. This can happen when you ssh into a BSD machine, for example.) Using this option disables <code>nano</code>&#8216;s mouse support.</p>
<dt><code>set rebinddelete</code></p>
<dd>Interpret the Delete and Backspace keys differently so that both Backspace and Delete work properly. You should only use this option when on your system either Backspace acts like Delete or Delete acts like Backspace.</p>
<dt><code>set regexp</code></p>
<dd>Do regular-expression searches by default. Regular expressions in <code>nano</code> are of the extended type (ERE).</p>
<dt><code>set saveonexit</code></p>
<dd>Save a changed buffer automatically on exit (<code>^X</code>); don&#8217;t prompt. (The old form of this option, <code>set tempfile</code>, is deprecated.)</p>
<dt><code>set scrollercolor </code><i>fgcolor</i><code>,</code><i>bgcolor</i></p>
<dd>Use this color combination for the indicator alias &quot;scrollbar&quot;. (On terminal emulators that link to a libvte older than version 0.55, using a background color here does not work correctly.) See <code>set titlecolor</code> for more details.</p>
<dt><code>set selectedcolor </code>[<code>bold,</code>][<code>italic,</code>]<i>fgcolor</i><code>,</code><i>bgcolor</i></p>
<dd>Use this color combination for selected text. See <code>set titlecolor</code> for more details.</p>
<dt><code>set showcursor</code></p>
<dd>Put the cursor on the highlighted item in the file browser, and show the cursor in the help viewer, to aid braille users and people with poor vision.</p>
<dt><code>set smarthome</code></p>
<dd>Make the Home key smarter. When Home is pressed anywhere but at the very beginning of non-whitespace characters on a line, the cursor will jump to that beginning (either forwards or backwards). If the cursor is already at that position, it will jump to the true beginning of the line.</p>
<dt><code>set softwrap</code></p>
<dd>Display lines that exceed the screen&#8217;s width over multiple screen lines. (You can make this soft-wrapping occur at whitespace instead of rudely at the screen&#8217;s edge, by using also <code>set atblanks</code>.)</p>
<dt><code>set speller </code><i>program</i> [<i>argument </i>&#8230;]</p>
<dd>Use the given <i>program</i> to do spell checking and correcting, instead of using the built-in corrector that calls <code><a href="/docs/linux/man/1-hunspell/">hunspell</a></code>(1) or <code><a href="/docs/linux/man/1-spell/">spell</a></code>(1).</p>
<dt><code>set spotlightcolor </code>[<code>bold,</code>][<code>italic,</code>]<i>fgcolor</i><code>,</code><i>bgcolor</i></p>
<dd>Use this color combination for highlighting a search match. The default value is <code>black,lightyellow</code>. See <code>set titlecolor</code> for valid color names.</p>
<dt><code>set stateflags</code></p>
<dd>Use the top-right corner of the screen for showing some state flags: <code>I</code> when auto-indenting, <code>M</code> when the mark is on, <code>L</code> when hard-wrapping (breaking long lines), <code>R</code> when recording a macro, and <code>S</code> when soft-wrapping. When the buffer is modified, a star (<code>*</code>) is shown after the filename in the center of the title bar.</p>
<dt><code>set statuscolor </code>[<code>bold,</code>][<code>italic,</code>]<i>fgcolor</i><code>,</code><i>bgcolor</i></p>
<dd>Use this color combination for the status bar. See <code>set titlecolor</code> for more details.</p>
<dt><code>set stripecolor </code>[<code>bold,</code>][<code>italic,</code>]<i>fgcolor</i><code>,</code><i>bgcolor</i></p>
<dd>Use this color combination for the vertical guiding stripe. See <code>set titlecolor</code> for more details.</p>
<dt><code>set suspendable</code></p>
<dd>Obsolete option; ignored. Suspension is enabled by default, reachable via <code>^T^Z</code>. (If you want a plain <code>^Z</code> to suspend nano, add <code>bind ^Z suspend main</code> to your nanorc.)</p>
<dt><code>set tabsize </code><i>number</i></p>
<dd>Use a tab size of <i>number</i> columns. The value of <i>number</i> must be greater than 0. The default value is <code>8</code>.</p>
<dt><code>set tabstospaces</code></p>
<dd>Convert each typed tab to spaces &#8212; to the number of spaces that a tab at that position would take up.</p>
<dt><code>set titlecolor </code>[<code>bold,</code>][<code>italic,</code>]<i>fgcolor</i><code>,</code><i>bgcolor</i></p>
<dd>Use this color combination for the title bar. Valid names for the foreground and background colors are: <code>red</code>, <code>green</code>, <code>blue</code>, <code>magenta</code>, <code>yellow</code>, <code>cyan</code>, <code>white</code>, and <code>black</code>. Each of these eight names may be prefixed with the word <code>light</code> to get a brighter version of that color. The word <code>grey</code> or <code>gray</code> may be used as a synonym for <code>lightblack</code>. On terminal emulators that can do at least 256 colors, other valid (but unprefixable) color names are: <code>pink</code>, <code>purple</code>, <code>mauve</code>, <code>lagoon</code>, <code>mint</code>, <code>lime</code>, <code>peach</code>, <code>orange</code>, <code>latte</code>, <code>rosy</code>, <code>beet</code>, <code>plum</code>, <code>sea</code>, <code>sky</code>, <code>slate</code>, <code>teal</code>, <code>sage</code>, <code>brown</code>, <code>ocher</code>, <code>sand</code>, <code>tawny</code>, <code>brick</code>, <code>crimson</code>, and <code>normal</code> &#8212; where <code>normal</code> means the default foreground or background color. On such emulators, the color may also be specified as a three-digit hexadecimal number prefixed with <code>#</code>, with the digits representing the amounts of red, green, and blue, respectively. This tells <code>nano</code> to select from the available palette the color that approximates the given values. </p>
<p> Either &quot;<i>fgcolor</i>&quot; or &quot;<code>,</code><i>bgcolor</i>&quot; may be left out, and the pair may be preceded by <code>bold</code> and/or <code>italic</code> (separated by commas) to get a bold and/or slanting typeface, if your terminal can do those.</p>
<dt><code>set trimblanks</code></p>
<dd>Remove trailing whitespace from wrapped lines when automatic hard-wrapping occurs or when text is justified.</p>
<dt><code>set unix</code></p>
<dd>Save a file by default in Unix format. This overrides nano&#8217;s default behavior of saving a file in the format that it had. (This option has no effect when you also use <code>set noconvert</code>.)</p>
<dt><code>set whitespace &quot;</code><i>characters</i><code>&quot;</code></p>
<dd>Set the two characters used to indicate the presence of tabs and spaces. They must be single-column characters. The default pair for a UTF-8 locale is &quot;<code>&raquo;md</code>&quot;, and for other locales &quot;<code>&gt;.</code>&quot;.</p>
<dt><code>set wordbounds</code></p>
<dd>Detect word boundaries differently by treating punctuation characters as parts of words.</p>
<dt><code>set wordchars &quot;</code><i>characters</i><code>&quot;</code></p>
<dd>Specify which other characters (besides the normal alphanumeric ones) should be considered as parts of words. When using this option, you probably want to unset <code>wordbounds</code>.</p>
<dt><code>set zap</code></p>
<dd>Let an unmodified Backspace or Delete erase the marked region (instead of a single character, and without affecting the cutbuffer).</p>
<dt><code>set zero</code></p>
<dd>Hide all elements of the interface (title bar, status bar, and help lines) and use all rows of the terminal for showing the contents of the buffer. The status bar appears only when there is a significant message, and disappears after 1.5 seconds or upon the next keystroke. With <code>M-Z</code> the title bar plus status bar can be toggled. With <code>M-X</code> the help lines. </p>
</dl>
<h2>Syntax Highlighting</h2>
<p>Coloring the different syntactic elements of a file is done via regular expressions (see the <code>color</code> command below). This is inherently imperfect, because regular expressions are not powerful enough to fully parse a file. Nevertheless, regular expressions can do a lot and are easy to make, so they are a good fit for a small editor like <code>nano</code>. </p>
<p> All regular expressions in <code>nano</code> are POSIX extended regular expressions. This means that <code>.</code>, <code>?</code>, <code>*</code>, <code>+</code>, <code>^</code>, <code>$</code>, and several other characters are special. The period <code>.</code> matches any single character, <code>?</code> means the preceding item is optional, <code>*</code> means the preceding item may be matched zero or more times, <code>+</code> means the preceding item must be matched one or more times, <code>^</code> matches the beginning of a line, and <code>$</code> the end, <code>\&lt;</code> matches the start of a word, and <code>\&gt;</code> the end, and <code>\s</code> matches a blank. It also means that lookahead and lookbehind are not possible. A complete explanation can be found in the manual page of GNU grep: <code>man grep</code>. </p>
<p> For each kind of file a separate syntax can be defined via the following commands:</p>
<dl>
<dt><code>syntax</code><i> name </i>[<code>&quot;</code><i>fileregex</i><code>&quot; </code><i></i>&#8230;]</p>
<dd>Start the definition of a syntax with this <i>name</i>. All subsequent <code>color</code> and other such commands will be added to this syntax, until a new <code>syntax</code> command is encountered. </p>
<p> When <code>nano</code> is run, this syntax will be automatically activated if the current filename matches the extended regular expression <i>fileregex</i>. Or the syntax can be explicitly activated by using the <code>-Y</code> or <code>&#8211;syntax</code> command-line option followed by the <i>name</i>. </p>
<p> The syntax <code>default</code> is special: it takes no <i>fileregex</i>, and applies to files that don&#8217;t match any syntax&#8217;s regexes. The syntax <code>none</code> is reserved; specifying it on the command line is the same as not having a syntax at all.</p>
<dt><code>header &quot;</code><i>regex</i><code>&quot; </code>&#8230;</p>
<dd>If from all defined syntaxes no <i>fileregex</i> matched, then compare this <i>regex</i> (or regexes) against the first line of the current file, to determine whether this syntax should be used for it.</p>
<dt><code>magic &quot;</code><i>regex</i><code>&quot; </code>&#8230;</p>
<dd>If no <i>fileregex</i> matched and no <code>header</code> regex matched either, then compare this <i>regex</i> (or regexes) against the result of querying the <code>magic</code> database about the current file, to determine whether this syntax should be used for it. (This functionality only works when <code>libmagic</code> is installed on the system and will be silently ignored otherwise.)</p>
<dt><code>formatter</code><i> program </i>[<i>argument </i>&#8230;]</p>
<dd>Run the given <i>program</i> on the full contents of the current buffer. (The current buffer is written out to a temporary file, the program is run on it, and then the temporary file is read back in, replacing the contents of the buffer.)</p>
<dt><code>linter</code><i> program </i>[<i>argument </i>&#8230;]</p>
<dd>Use the given <i>program</i> to run a syntax check on the current buffer.</p>
<dt><code>comment &quot;</code><i>string</i><code>&quot;</code></p>
<dd>Use the given <i>string</i> for commenting and uncommenting lines. If the string contains a vertical bar or pipe character (<code>|</code>), this designates bracket-style comments; for example, &quot;<code>/*|*/</code>&quot; for CSS files. The characters before the pipe are prepended to the line and the characters after the pipe are appended at the end of the line. If no pipe character is present, the full string is prepended; for example, &quot;<code>#</code>&quot; for Python files. If empty double quotes are specified, the comment/uncomment function is disabled; for example, &quot;&quot; for JSON. The default value is &quot;<code>#</code>&quot;.</p>
<dt><code>tabgives &quot;</code><i>string</i><code>&quot;</code></p>
<dd>Make the &lt;Tab&gt; key produce the given <i>string</i>. Useful for languages like Python that want to see only spaces for indentation. This overrides the setting of the <code>tabstospaces</code> option.</p>
<dt><code>color </code>[<code>bold,</code>][<code>italic,</code>]<i>fgcolor</i><code>,</code><i>bgcolor</i><code> &quot;</code><i>regex</i><code>&quot; </code><i></i>&#8230;</p>
<dd>Paint all pieces of text that match the extended regular expression <i>regex</i> with the given foreground and background colors, at least one of which must be specified. Valid color names are: <code>red</code>, <code>green</code>, <code>blue</code>, <code>magenta</code>, <code>yellow</code>, <code>cyan</code>, <code>white</code>, and <code>black</code>. Each of these eight names may be prefixed with the word <code>light</code> to get a brighter version of that color. The word <code>grey</code> or <code>gray</code> may be used as a synonym for <code>lightblack</code>. On terminal emulators that can do at least 256 colors, other valid (but unprefixable) color names are: <code>pink</code>, <code>purple</code>, <code>mauve</code>, <code>lagoon</code>, <code>mint</code>, <code>lime</code>, <code>peach</code>, <code>orange</code>, <code>latte</code>, <code>rosy</code>, <code>beet</code>, <code>plum</code>, <code>sea</code>, <code>sky</code>, <code>slate</code>, <code>teal</code>, <code>sage</code>, <code>brown</code>, <code>ocher</code>, <code>sand</code>, <code>tawny</code>, <code>brick</code>, <code>crimson</code>, and <code>normal</code> &#8212; where <code>normal</code> means the default foreground or background color. On such emulators, the color may also be specified as a three-digit hexadecimal number prefixed with <code>#</code>, with the digits representing the amounts of red, green, and blue, respectively. This tells <code>nano</code> to select from the available palette the color that approximates the given values. </p>
<p> The color pair may be preceded by <code>bold</code> and/or <code>italic</code> (separated by commas) to get a bold and/or slanting typeface, if your terminal can do those. </p>
<p> All coloring commands are applied in the order in which they are specified, which means that later commands can recolor stuff that was colored earlier.</p>
<dt><code>icolor </code>[<code>bold,</code>][<code>italic,</code>]<i>fgcolor</i><code>,</code><i>bgcolor</i><code> &quot;</code><i>regex</i><code>&quot; </code><i></i>&#8230;</p>
<dd>Same as above, except that the matching is case insensitive.</p>
<dt><code>color </code>[<code>bold,</code>][<code>italic,</code>]<i>fgcolor</i><code>,</code><i>bgcolor</i><code> start=&quot;</code><i>fromrx</i><code>&quot; end=&quot;</code><i>torx</i><code>&quot;</code></p>
<dd>Paint all pieces of text whose start matches extended regular expression <i>fromrx</i> and whose end matches extended regular expression <i>torx</i> with the given foreground and background colors, at least one of which must be specified. This means that, after an initial instance of <i>fromrx</i>, all text until the first instance of <i>torx</i> will be colored. This allows syntax highlighting to span multiple lines.</p>
<dt><code>icolor </code>[<code>bold,</code>][<code>italic,</code>]<i>fgcolor</i><code>,</code><i>bgcolor</i><code> start=&quot;</code><i>fromrx</i><code>&quot; end=&quot;</code><i>torx</i><code>&quot;</code></p>
<dd>Same as above, except that the matching is case insensitive.</p>
<dt><code>include &quot;</code><i>syntaxfile</i><code>&quot;</code></p>
<dd>Read in self-contained color syntaxes from <i>syntaxfile</i>. Note that <i>syntaxfile</i> may contain only the above commands, from <code>syntax</code> to <code>icolor</code>.</p>
<dt><code>extendsyntax</code><i> name command argument </i>&#8230;</p>
<dd>Extend the syntax previously defined as <i>name</i> with another <i>command</i>. This allows adding a new <code>color</code>, <code>icolor</code>, <code>header</code>, <code>magic</code>, <code>formatter</code>, <code>linter</code>, <code>comment</code>, or <code>tabgives</code> command to an already defined syntax &#8212; useful when you want to slightly improve a syntax defined in one of the system-installed files (which normally are not writable). </p>
</dl>
<h2>Rebinding Keys</h2>
<p>Key bindings can be changed via the following three commands:</p>
<dl>
<dd>
<dl>
<dt><code>bind</code><i> key function menu</i></p>
<dd>Rebinds the given <i>key</i> to the given <i>function</i> in the given <i>menu</i> (or in all menus where the function exists when <code>all</code> is used).</p>
<dt><code>bind</code><i> key </i><code>&quot;</code><i>string</i><code>&quot;</code><i> menu</i></p>
<dd>Makes the given <i>key</i> produce the given <i>string</i> in the given <i>menu</i> (or in all menus where the key exists when <code>all</code> is used). The <i>string</i> can consist of text or commands or a mix of them. (To enter a command into the <i>string</i>, precede its keystroke with <code>M-V</code>.)</p>
<dt><code>unbind</code><i> key menu</i></p>
<dd>Unbinds the given <i>key</i> from the given <i>menu</i> (or from all menus where the key exists when <code>all</code> is used).</dl>
</dl>
<dl>
<dt>The format of <i>key</i> should be one of:</p>
<dd>
<dl>
<dd>
<dl>
<dt><code>^</code><i>X</i></p>
<dd>where <i>X</i> is a Latin letter, or one of several ASCII characters (@, ], \, ^, _), or the word &quot;Space&quot;. Example: ^C.</p>
<dt><code>M-</code><i>X</i></p>
<dd>where <i>X</i> is any ASCII character except [, or the word &quot;Space&quot;. Example: M-8.</p>
<dt><code>Sh-M-</code><i>X</i></p>
<dd>where <i>X</i> is a Latin letter. Example: Sh-M-U. By default, each Meta+letter keystroke does the same as the corresponding Shift+Meta+letter. But when any Shift+Meta bind is made, that will no longer be the case, for all letters.</p>
<dt><code>F</code><i>N</i></p>
<dd>where <i>N</i> is a numeric value from 1 to 24. Example: F10. (Often, <code>F13</code> to <code>F24</code> can be typed as <code>F1</code> to <code>F12</code> with Shift.)</p>
<dt><code>Ins</code> or <code>Del</code>.</p>
<dd></dl>
</dl>
<p> Rebinding <code>^M</code> (Enter) or <code>^I</code> (Tab) is probably not a good idea. Rebinding <code>^[</code> (Esc) is not possible, because its keycode is the starter byte of Meta keystrokes and escape sequences. Rebinding any of the dedicated cursor-moving keys (the arrows, Home, End, PageUp and PageDown) is not possible. On some terminals it&#8217;s not possible to rebind <code>^H</code> (unless <code>&#8211;raw</code> is used) because its keycode is identical to that of the Backspace key. </p>
<dt>Valid <i>function</i> names to be bound are:</p>
<dd>
<dl>
<dd>
<dl>
<dt><code>help</code></p>
<dd>Invokes the help viewer.</p>
<dt><code>cancel</code></p>
<dd>Cancels the current command.</p>
<dt><code>exit</code></p>
<dd>Exits from the program (or from the help viewer or file browser).</p>
<dt><code>writeout</code></p>
<dd>Writes the current buffer to disk, asking for a name.</p>
<dt><code>savefile</code></p>
<dd>Writes the current file to disk without prompting.</p>
<dt><code>insert</code></p>
<dd>Inserts a file into the current buffer (at the current cursor position), or into a new buffer when option <code>multibuffer</code> is set.</p>
<dt><code>whereis</code></p>
<dd>Starts a forward search for text in the current buffer &#8212; or for filenames matching a string in the current list in the file browser.</p>
<dt><code>wherewas</code></p>
<dd>Starts a backward search for text in the current buffer &#8212; or for filenames matching a string in the current list in the file browser.</p>
<dt><code>findprevious</code></p>
<dd>Searches the next occurrence in the backward direction.</p>
<dt><code>findnext</code></p>
<dd>Searches the next occurrence in the forward direction.</p>
<dt><code>replace</code></p>
<dd>Interactively replaces text within the current buffer.</p>
<dt><code>cut</code></p>
<dd>Cuts and stores the current line (or the marked region).</p>
<dt><code>copy</code></p>
<dd>Copies the current line (or the marked region) without deleting it.</p>
<dt><code>paste</code></p>
<dd>Pastes the currently stored text into the current buffer at the current cursor position.</p>
<dt><code>zap</code></p>
<dd>Throws away the current line (or the marked region). (This function is bound by default to &lt;Meta+Delete&gt;.)</p>
<dt><code>chopwordleft</code></p>
<dd>Deletes from the cursor position to the beginning of the preceding word. (This function is bound by default to &lt;Shift+Ctrl+Delete&gt;. If your terminal produces <code>^H</code> for &lt;Ctrl+Backspace&gt;, you can make &lt;Ctrl+Backspace&gt; delete the word to the left of the cursor by rebinding <code>^H</code> to this function.)</p>
<dt><code>chopwordright</code></p>
<dd>Deletes from the cursor position to the beginning of the next word. (This function is bound by default to &lt;Ctrl+Delete&gt;.)</p>
<dt><code>cutrestoffile</code></p>
<dd>Cuts all text from the cursor position till the end of the buffer.</p>
<dt><code>mark</code></p>
<dd>Sets the mark at the current position, to start selecting text. Or, when it is set, unsets the mark.</p>
<dt><code>location</code></p>
<dd>Reports the current position of the cursor in the buffer: the line, column, and character positions. (The old name of this function, &#8216;curpos&#8217;, is deprecated.)</p>
<dt><code>wordcount</code></p>
<dd>Counts and reports on the status bar the number of lines, words, and characters in the current buffer (or in the marked region).</p>
<dt><code>execute</code></p>
<dd>Prompts for a program to execute. The program&#8217;s output will be inserted into the current buffer (or into a new buffer when <code>M-F</code> is toggled).</p>
<dt><code>speller</code></p>
<dd>Invokes a spell-checking program, either the default <code><a href="/docs/linux/man/1-hunspell/">hunspell</a></code>(1) or GNU <code><a href="/docs/linux/man/1-spell/">spell</a></code>(1), or the one defined by <code>&#8211;speller</code> or <code>set speller</code>.</p>
<dt><code>formatter</code></p>
<dd>Invokes a full-buffer-processing program (if the active syntax defines one).</p>
<dt><code>linter</code></p>
<dd>Invokes a syntax-checking program (if the active syntax defines one).</p>
<dt><code>justify</code></p>
<dd>Justifies the current paragraph (or the marked region). A paragraph is a group of contiguous lines that, apart from possibly the first line, all have the same indentation. The beginning of a paragraph is detected by either this lone line with a differing indentation or by a preceding blank line.</p>
<dt><code>fulljustify</code></p>
<dd>Justifies the entire current buffer (or the marked region).</p>
<dt><code>indent</code></p>
<dd>Indents (shifts to the right) the current line or the marked lines.</p>
<dt><code>unindent</code></p>
<dd>Unindents (shifts to the left) the current line or the marked lines.</p>
<dt><code>comment</code></p>
<dd>Comments or uncomments the current line or the marked lines, using the comment style specified in the active syntax.</p>
<dt><code>complete</code></p>
<dd>Completes (when possible) the fragment before the cursor to a full word found elsewhere in the current buffer.</p>
<dt><code>left</code></p>
<dd>Goes left one position (in the editor or browser).</p>
<dt><code>right</code></p>
<dd>Goes right one position (in the editor or browser).</p>
<dt><code>up</code></p>
<dd>Goes one line up (in the editor or browser).</p>
<dt><code>down</code></p>
<dd>Goes one line down (in the editor or browser).</p>
<dt><code>scrollup</code></p>
<dd>Scrolls the viewport up one row (meaning that the text slides down) while keeping the cursor in the same text position, if possible. (This function is bound by default to &lt;Alt+Up&gt;. If &lt;Alt+Up&gt; does nothing on your Linux console, see the FAQ:</p>
<dt><code>scrolldown</code></p>
<dd>Scrolls the viewport down one row (meaning that the text slides up) while keeping the cursor in the same text position, if possible. (This function is bound by default to &lt;Alt+Down&gt;.)</p>
<dt><code>center</code></p>
<dd>Scrolls the line with the cursor to the middle of the screen.</p>
<dt><code>prevword</code></p>
<dd>Moves the cursor to the beginning of the previous word.</p>
<dt><code>nextword</code></p>
<dd>Moves the cursor to the beginning of the next word.</p>
<dt><code>home</code></p>
<dd>Moves the cursor to the beginning of the current line.</p>
<dt><code>end</code></p>
<dd>Moves the cursor to the end of the current line.</p>
<dt><code>beginpara</code></p>
<dd>Moves the cursor to the beginning of the current paragraph.</p>
<dt><code>endpara</code></p>
<dd>Moves the cursor to the end of the current paragraph.</p>
<dt><code>prevblock</code></p>
<dd>Moves the cursor to the beginning of the current or preceding block of text. (Blocks are separated by one or more blank lines.)</p>
<dt><code>nextblock</code></p>
<dd>Moves the cursor to the beginning of the next block of text.</p>
<dt><code>pageup</code></p>
<dd>Goes up one screenful.</p>
<dt><code>pagedown</code></p>
<dd>Goes down one screenful.</p>
<dt><code>firstline</code></p>
<dd>Goes to the first line of the file.</p>
<dt><code>lastline</code></p>
<dd>Goes to the last line of the file.</p>
<dt><code>gotoline</code></p>
<dd>Goes to a specific line (and column if specified). Negative numbers count from the end of the file (and end of the line).</p>
<dt><code>findbracket</code></p>
<dd>Moves the cursor to the bracket (or brace or parenthesis, etc.) that matches (pairs) with the one under the cursor. See <code>set matchbrackets</code>.</p>
<dt><code>anchor</code></p>
<dd>Places an anchor at the current line, or removes it when already present. (An anchor is visible when line numbers are activated.)</p>
<dt><code>prevanchor</code></p>
<dd>Goes to the first anchor before the current line.</p>
<dt><code>nextanchor</code></p>
<dd>Goes to the first anchor after the current line.</p>
<dt><code>prevbuf</code></p>
<dd>Switches to editing/viewing the previous buffer when multiple buffers are open.</p>
<dt><code>nextbuf</code></p>
<dd>Switches to editing/viewing the next buffer when multiple buffers are open.</p>
<dt><code>verbatim</code></p>
<dd>Inserts the next keystroke verbatim into the file.</p>
<dt><code>tab</code></p>
<dd>Inserts a tab at the current cursor location.</p>
<dt><code>enter</code></p>
<dd>Inserts a new line below the current one.</p>
<dt><code>delete</code></p>
<dd>Deletes the character under the cursor.</p>
<dt><code>backspace</code></p>
<dd>Deletes the character before the cursor.</p>
<dt><code>recordmacro</code></p>
<dd>Starts the recording of keystrokes &#8212; the keystrokes are stored as a macro. When already recording, the recording is stopped.</p>
<dt><code>runmacro</code></p>
<dd>Replays the keystrokes of the last recorded macro.</p>
<dt><code>undo</code></p>
<dd>Undoes the last performed text action (add text, delete text, etc).</p>
<dt><code>redo</code></p>
<dd>Redoes the last undone action (i.e., it undoes an undo).</p>
<dt><code>refresh</code></p>
<dd>Refreshes the screen.</p>
<dt><code>suspend</code></p>
<dd>Suspends the editor and returns control to the shell (until you tell the process to resume execution with <code>fg</code>).</p>
<dt><code>casesens</code></p>
<dd>Toggles whether searching/replacing ignores or respects the case of the given characters.</p>
<dt><code>regexp</code></p>
<dd>Toggles whether searching/replacing uses literal strings or regular expressions.</p>
<dt><code>backwards</code></p>
<dd>Toggles whether searching/replacing goes forward or backward.</p>
<dt><code>older</code></p>
<dd>Retrieves the previous (earlier) entry at a prompt.</p>
<dt><code>newer</code></p>
<dd>Retrieves the next (later) entry at a prompt.</p>
<dt><code>flipreplace</code></p>
<dd>Toggles between searching for something and replacing something.</p>
<dt><code>flipgoto</code></p>
<dd>Toggles between searching for text and targeting a line number.</p>
<dt><code>flipexecute</code></p>
<dd>Toggles between inserting a file and executing a command.</p>
<dt><code>flippipe</code></p>
<dd>When executing a command, toggles whether the current buffer (or marked region) is piped to the command.</p>
<dt><code>flipnewbuffer</code></p>
<dd>Toggles between inserting into the current buffer and into a new empty buffer.</p>
<dt><code>flipconvert</code></p>
<dd>When reading in a file, toggles between converting and not converting it from DOS/Mac format. Converting is the default.</p>
<dt><code>dosformat</code></p>
<dd>When writing a file, switches to writing a DOS format (CR/LF).</p>
<dt><code>macformat</code></p>
<dd>When writing a file, switches to writing a Mac format.</p>
<dt><code>append</code></p>
<dd>When writing a file, appends to the end instead of overwriting.</p>
<dt><code>prepend</code></p>
<dd>When writing a file, &#8216;prepends&#8217; (writes at the beginning) instead of overwriting.</p>
<dt><code>backup</code></p>
<dd>When writing a file, creates a backup of the current file.</p>
<dt><code>discardbuffer</code></p>
<dd>When about to write a file, discard the current buffer without saving. (This function is bound by default only when option <code>&#8211;saveonexit</code> is in effect.)</p>
<dt><code>browser</code></p>
<dd>Starts the file browser (in the Read File and Write Out menus), allowing to select a file from a list.</p>
<dt><code>gotodir</code></p>
<dd>Goes to a directory to be specified, allowing to browse anywhere in the filesystem.</p>
<dt><code>firstfile</code></p>
<dd>Goes to the first file in the list when using the file browser.</p>
<dt><code>lastfile</code></p>
<dd>Goes to the last file in the list when using the file browser.</p>
<dt><code>nohelp</code></p>
<dd>Toggles the presence of the two-line list of key bindings at the bottom of the screen. (This toggle is special: it is available in all menus except the help viewer and the linter. All further toggles are available in the main menu only.)</p>
<dt><code>zero</code></p>
<dd>Toggles the presence of title bar and status bar.</p>
<dt><code>constantshow</code></p>
<dd>Toggles the constant display of the current line, column, and character positions.</p>
<dt><code>softwrap</code></p>
<dd>Toggles the displaying of overlong lines on multiple screen lines.</p>
<dt><code>linenumbers</code></p>
<dd>Toggles the display of line numbers in front of the text.</p>
<dt><code>whitespacedisplay</code></p>
<dd>Toggles the showing of whitespace.</p>
<dt><code>nosyntax</code></p>
<dd>Toggles syntax highlighting.</p>
<dt><code>smarthome</code></p>
<dd>Toggles the smartness of the Home key.</p>
<dt><code>autoindent</code></p>
<dd>Toggles whether a newly created line will contain the same amount of leading whitespace as the preceding line &#8212; or as the next line if the preceding line is the beginning of a paragraph.</p>
<dt><code>cutfromcursor</code></p>
<dd>Toggles whether cutting text will cut the whole line or just from the current cursor position to the end of the line.</p>
<dt><code>breaklonglines</code></p>
<dd>Toggles whether long lines will be hard-wrapped to the next line. (The old name of this function, &#8216;nowrap&#8217;, is deprecated.)</p>
<dt><code>tabstospaces</code></p>
<dd>Toggles whether typed tabs will be converted to spaces.</p>
<dt><code>mouse</code></p>
<dd>Toggles mouse support.</dl>
</dl>
<dt>Valid <i>menu</i> sections are:</p>
<dd>
<dl>
<dd>
<dl>
<dt><code>main</code></p>
<dd>The main editor window where text is entered and edited.</p>
<dt><code>help</code></p>
<dd>The help-viewer menu.</p>
<dt><code>search</code></p>
<dd>The search menu (AKA whereis).</p>
<dt><code>replace</code></p>
<dd>The &#8216;search to replace&#8217; menu.</p>
<dt><code>replacewith</code></p>
<dd>The &#8216;replace with&#8217; menu, which comes up after &#8216;search to replace&#8217;.</p>
<dt><code>yesno</code></p>
<dd>The &#8216;yesno&#8217; menu, where the Yes/No/All/Cancel question is asked.</p>
<dt><code>gotoline</code></p>
<dd>The &#8216;goto line (and column)&#8217; menu.</p>
<dt><code>writeout</code></p>
<dd>The &#8216;write file&#8217; menu.</p>
<dt><code>insert</code></p>
<dd>The &#8216;insert file&#8217; menu.</p>
<dt><code>browser</code></p>
<dd>The &#8216;file browser&#8217; menu, for selecting a file to be opened or inserted or written to.</p>
<dt><code>whereisfile</code></p>
<dd>The &#8216;search for a file&#8217; menu in the file browser.</p>
<dt><code>gotodir</code></p>
<dd>The &#8216;go to directory&#8217; menu in the file browser.</p>
<dt><code>execute</code></p>
<dd>The menu for inserting the output from an external command, or for filtering the buffer (or the marked region) through an external command, or for executing one of several tools. (The old form of this menu name, &#8216;extcmd&#8217;, is deprecated.)</p>
<dt><code>spell</code></p>
<dd>The menu of the integrated spell checker where the user can edit a misspelled word.</p>
<dt><code>linter</code></p>
<dd>The linter menu, which allows jumping through the linting messages.</p>
<dt><code>all</code></p>
<dd>A special name that encompasses all menus. For <code>bind</code> it means all menus where the specified <i>function</i> exists; for <code>unbind</code> it means all menus where the specified <i>key</i> exists.</dl>
</dl>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/nanorc</i></p>
<dd>System-wide configuration file.</p>
<dt><i>~/.nanorc</i> or <i>$XDG_CONFIG_HOME/nano/nanorc</i> or <i>~/.config/nano/nanorc</i></p>
<dd>Per-user configuration file.</p>
<dt><i>/usr/share/nano/*</i></p>
<dd>Syntax definitions for the syntax coloring of common file types (and for less common file types in the <i>extra/</i> subdirectory). </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-nano/">nano</a></code>(1)</p>
<dl>
<dt><i><a rel="nofollow" href="https://nano-editor.org/cheatsheet.html">https://nano-editor.org/cheatsheet.html</a></i></p>
<dd>An overview of the default key bindings. </p>
