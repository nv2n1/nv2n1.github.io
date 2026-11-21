---
title: "jupp(1)"
name: "jupp"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jupp/"
description: "joe – Joe’s Own Editor"
---
<p> joe - Joe&#8217;s Own Editor  </p>
<h2>Syntax</h2>
<p> <code>joe [global-options] [ [local-options] filename ]...</code> </p>
<p> <code>jstar [global-options] [ [local-options] filename ]...</code> </p>
<p> <code>jmacs [global-options] [ [local-options] filename ]...</code> </p>
<p> <code>rjoe [global-options] [ [local-options] filename ]...</code> </p>
<p> <code>jpico [global-options] [ [local-options] filename ]...</code> </p>
<p> <code>jupp [global-options] [ [local-options] filename ]...</code>  </p>
<h2>Description</h2>
<p> JOE is a powerful ASCII-text screen editor. It has a &quot;mode-less&quot; user interface which is similar to many user-friendly PC editors. Users of Micro-Pro&#8217;s WordStar or Borland&#8217;s &quot;Turbo&quot; languages will feel at home. JOE is a full featured UNIX screen-editor though, and has many features for editing programs and text. </p>
<p>JOE also emulates several other editors. JSTAR is a close imitation of WordStar with many &quot;JOE&quot; extensions. JPICO is a close imitation of the Pine mailing system&#8217;s PICO editor, but with many extensions and improvements. JMACS is a GNU-EMACS imitation. RJOE is a restricted version of JOE, which allows you to edit only the files specified on the command line. </p>
<p>Although JOE is actually six different editors, it still requires only one executable, but one with six different names. The name of the editor with an &quot;rc&quot; appended gives the name of JOE&#8217;s initialisation file, which determines the personality of the editor. </p>
<p>JUPP is free software; you can distribute it and/or modify it under the terms of the GNU General Public License, Version 1, as published by the Free Software Foundation. (main.c contains more detailed exceptions.) I have no plans for turning JOE into a commercial or share-ware product. See the source code for exact authorship and licencing information. JOE is available over the Internet from <code><a rel="nofollow" href="http://joe-editor.sf.net/">http://joe-editor.sf.net/</a></code>. JUPP is available at <code><a rel="nofollow" href="http://mirbsd.de/jupp">http://mirbsd.de/jupp</a></code>. </p>
<h2>Usage</h2>
<p>To start the editor, type <code>joe</code> followed by zero or more names of files you want to edit. Each file name may be preceded by a local option setting (see the local options table which follows). Other global options, which apply to the editor as a whole, may also be placed on the command line (see the global options table which follows). If you are editing a new file, you can either give the name of the new file when you invoke the editor, or in the editor when you save the new file. A modified syntax for file names is provided to allow you to edit program output, standard input/output, or sections of files or devices. See the section <code>Filenames</code> below for details. </p>
<p>On cygwin32 systems, the special option <code>-CYGhack</code> is replaced by anything that comes past it (and separating whitespace) on the command line as <i>one</i> option (to work around a Cygwin bug as it cannot correctly be passed a UNC pathname with spaces as one argument from Explorer <i>at all</i>). </p>
<p>Once you are in the editor, you can type in text and use special control-character sequences to perform other editing tasks. To find out what the control-character sequences are, read the rest of this man page or type <code>^K H</code> for help in the editor. </p>
<p>Now for some obscure computer-lore: </p>
<p>The <code>^</code> means that you hold down the <code>Control</code> key while pressing the following key (the same way the <code>Shift</code> key works for uppercase letters). A number of control-key sequences are duplicated on other keys, so that you don&#8217;t need to press the control key: <code>ESC</code> will work in place of <code>^[</code>, <code>Del</code> will work in place of <code>^?</code>, <code>Backspace</code> will work in place of <code>^H</code>, <code>Tab</code> will work in place of <code>^I</code>, <code>Return</code> or <code>Enter</code> will work in place of <code>^M</code> and <code>Linefeed</code> will work in place of <code>^J</code>. Some keyboards may give you trouble with some control keys. <code>^_</code>, <code>^^</code> and <code>^@</code> can usually be entered without pressing shift (I.E., try <code>^-</code>, <code>^6</code> and <code>^2</code>). Other keyboards may reassign these to other keys. Try: <code>^.</code>, <code>^,</code> and <code>^/</code>. <code>^SPACE</code> can usually be used in place of <code>^@</code>. <code>^\</code> and <code>^]</code> are interpreted by many communication programs, including telnet and kermit. Usually you just hit the key twice to get it to pass through the communication program. </p>
<p>Once you have typed <code>^K H</code>, the first help window appears at the top of the screen. You can continue to enter and edit text while the help window is on. To page through other topics, hit ^[, and ^[. (that is, ESC , and ESC .). Use <code>^K H</code> to dismiss the help window. </p>
<p>You can customise the keyboard layout, the help screens and a number of behavior defaults by copying JOE&#8217;s initialisation file (usually <code>/etc/jupp/joe/joerc</code>) to <code>.joerc</code> in your home directory and then by modifying it. See the section <code>joerc</code> below. The filename is actually <code>.</code><i>name</i><code>rc</code> where <i>name</i> is the <code>argv[0]</code> the editor is called with. </p>
<p>Custom syntax files are loaded from <code>.jupp/syntax/</code><i>name</i><code>.jsf</code> in your home directory and <code>.jupp/charmaps/</code><i>name</i> holds custom charmaps (<i>name</i> here is the name of the syntax or charmap). </p>
<p>To have JOE used as your default editor for e-mail and News, you need to set the <code>EDITOR</code> and <code>VISUAL</code> environment variables in your shell initialisation file (<code>.cshrc</code> or <code>.profile</code>) to refer to JOE (the joe binary usually resides as <code>/usr/bin/joe</code>). </p>
<p>There are a number of other obscure invocation parameters which may have to be set, particularly if your terminal screen is not updating as you think it should. See the section <code>Environment variables</code> below. </p>
<h2>Command Line Options</h2>
<p>The following global options may be specified on the command line: </p>
<dl>
<dt>-asis</dt>
<dd> <p> Characters with codes above 127 will be sent to the terminal as-is, instead of as inverse of the corresponding character below 128. If this does not work, check your terminal server. </p>
 </dd>
<dt>-backpath path</dt>
<dd> <p> If this option is given, backup files will be stored in the specified directory instead of in each file&#8217;s original directory. </p>
 </dd>
<dt>-baud nnn</dt>
<dd> <p> Set the baud rate for the purposes of terminal screen optimisation. Joe inserts delays for baud rates below 19200, which bypasses tty buffering so that typeahead will interrupt the screen output. Scrolling commands will not be used for 38400 baud. This is useful for X-terms and other console ttys which really aren&#8217;t going over a serial line. </p>
 </dd>
<dt>-beep</dt>
<dd> <p> Joe will beep on command errors and when the cursor goes past extremes. </p>
 </dd>
<dt>-columns nnn</dt>
<dd> <p> Sets the number of screen columns. </p>
 </dd>
<dt>-csmode</dt>
<dd> <p> Continued search mode: a search immediately following a search will repeat the previous search instead of prompting for new string. This is useful for the the ^[S and ^[R commands and for when joe is trying to be emacs. </p>
 </dd>
<dt>-dopadding</dt>
<dd> <p> Joe usually assumes that there is some kind of flow control between it and the tty. If there isn&#8217;t, this option will make joe output extra ^@s to the tty as specified by the termcap entry. The extra ^@s allow the terminal to catch up after long terminal commands. </p>
 </dd>
<dt>-exask</dt>
<dd> <p> This option makes ^KX verify the file name that it&#8217;s about to write. </p>
 </dd>
<dt>-force</dt>
<dd> <p> This option makes sure that the last line of the file has a line-feed which it&#8217;s saved. </p>
 </dd>
<dt>-help</dt>
<dd> <p> The editor will start with the help screen on if this option is given. </p>
 </dd>
<dt>-keepup</dt>
<dd> <p> Normally the column number and control-key prefix fields of the status lines are on a one second delay to reduce CPU consumption, but with this option they are updated after each key-stroke. </p>
 </dd>
<dt>-lightoff</dt>
<dd> <p> The block highlighting will go away after any block command if this option is given. </p>
 </dd>
<dt>-lines nnn</dt>
<dd> <p> Sets the number of screen lines. </p>
 </dd>
<dt>-marking</dt>
<dd> <p> Text between ^KB and the cursor is highlighted (use with -lightoff and a modified joerc file to have drop-anchor style block selection). </p>
 </dd>
<dt>-mid</dt>
<dd> <p> If this option is set and the cursor moves off the window, the window will be scrolled so that the cursor is in the center. This option is forced on slow terminals which don&#8217;t have scrolling commands. </p>
 </dd>
<dt>-nobackups</dt>
<dd> <p> This option prevents backup files. </p>
 </dd>
<dt>-nonotice</dt>
<dd> <p> This option prevent the copyright notice from being displayed when the editor starts. </p>
 </dd>
<dt>-nosta</dt>
<dd> <p> This option eliminates the top-most status line. It&#8217;s nice for when you only want to see your text on the screen or if you&#8217;re using a vt52. </p>
 </dd>
<dt>-noxon</dt>
<dd> <p> Attempt to turn off ^S/^Q processing. This is useful for when joe is trying to be WordStar or EMACS. </p>
 </dd>
<dt>-orphan</dt>
<dd> <p> When this option is active, extra files on the command line will be placed in orphaned buffers instead of in extra windows. This is useful for when joe is trying to be emacs. </p>
 </dd>
<dt>-pg nnn</dt>
<dd> <p> This specifies the number of lines to keep after PgUp/PgDn (^U/^V). If -1 is given, half the window is kept. </p>
 </dd>
<dt>-skiptop nnn</dt>
<dd> <p> Don&#8217;t use the top nnn lines of the screen. Useful for when joe is used as a BBS editor. </p>
 </dd></dl>
<p>Each of these options may be specified in the joerc file as well. In addition, the NOXON, BAUD, LINES, COLUMNS and DOPADDING options may be specified with environment variables. See the section <code>Environment variables</code> below. </p>
<p>The following options may be specified before each filename on the command line: </p>
<dl>
<dt>+nnn</dt>
<dd> <p> The cursor starts on the specified line. </p>
 </dd>
<dt>-crlf</dt>
<dd> <p> Joe uses CR-LF as the end of line sequence instead of just LF. This is for editing MS-DOS or VMS files. </p>
 </dd>
<dt>-hex</dt>
<dd> <p> Sets the buffer to hex edit mode. </p>
 </dd>
<dt>-wordwrap</dt>
<dd> <p> Joe wraps the previous word when you type past the right margin. </p>
 </dd>
<dt>-autoindent</dt>
<dd> <p> When you hit Return on an indented line, the indentation is duplicated onto the new line. </p>
 </dd>
<dt>-overwrite</dt>
<dd> <p> Typing overwrites existing characters instead of inserting before them. </p>
 </dd>
<dt>-lmargin nnn</dt>
<dd> <p> Sets the left margin. </p>
 </dd>
<dt>-rmargin nnn</dt>
<dd> <p> Sets the right margin. </p>
 </dd>
<dt>-tab nnn</dt>
<dd> <p> Sets the tab width. </p>
 </dd>
<dt>-indentc nnn</dt>
<dd> <p> Sets the indentation character for ^K, and ^K. (32 for SPACE, 9 for TAB). </p>
 </dd>
<dt>-istep nnn</dt>
<dd> <p> Sets the indentation step for ^K, and ^K.. </p>
 </dd>
<dt>-linums</dt>
<dd> <p> Line numbers are displayed before each line. </p>
 </dd>
<dt>-rdonly</dt>
<dd> <p> The file is read only. </p>
 </dd>
<dt>-keymap name</dt>
<dd> <p> Use an alternate section of the joerc file for the key sequence bindings. For example, <code>joe, jstar, rjoe</code> and <code>jupp</code> support <code>-keymap cua</code> to make ^Z, ^X, ^C and ^V do the same thing as in contemporary GUI editors. </p>
 </dd></dl>
<p>These options can also be specified in the joerc file. They can be set depending on the file-name extension. Programs (.c, .h or .p extension) usually have autoindent enabled. Wordwrap is enabled on other files, but rc files have it disabled. </p>
<h2>Editing Tasks</h2>
<h3>Basic Editing</h3>
<p>When you type characters into the editor, they are normally inserted into the file being edited (or appended to the file if the cursor is at the end of the file). This is the normal operating mode of the editor. If you want to replace some existing text, you have to delete the old text before or after you type in the replacement text. The <code>Backspace</code> key can be used for deleting text: move the cursor to right after the text you want to delete and hit <code>Backspace</code> a number of times. </p>
<p>Hit the <code>Enter</code> or <code>Return</code> key to insert a line-break. For example, if the cursor was in the middle of a line and you hit <code>Return</code>, the line would be split into two lines with the cursor appearing at the beginning of the second line. Hit <code>Backspace</code> at the beginning of a line to eliminate a line-break. </p>
<p>Use the arrow keys to move around the file. If your keyboard doesn&#8217;t have arrow keys (or if they don&#8217;t work for some reason), use <code>^F</code> to move forwards (right), <code>^B</code> to move backwards (left), <code>^P</code> to move to the previous line (up), and <code>^N</code> to move to the next line (down). The right and left arrow keys simply move forwards or backwards one character at a time through the text: if you&#8217;re at the beginning of a line and you press left-arrow, you will end up at the end of the previous line. The up and down arrow keys move forwards and backwards by enough characters so that the cursor appears in the same column that it was in on the original line. </p>
<p>If you want to indent the text you enter, you can use the <code>TAB</code> key. This inserts a special control character which makes the characters which follow it begin at the next TAB STOP. TAB STOPS normally occur every 8 columns, but this can be changed with the <code>^T D</code> command. PASCAL and C programmers often set TAB STOPS on every 4 columns. </p>
<p>If for some reason your terminal screen gets messed up (for example, if you receive a mail notice from biff), you can have the editor refresh the screen by hitting <code>^R</code>. </p>
<p>There are many other keys for deleting text and moving around the file. For example, hit <code>^D</code> to delete the character the cursor is on instead of deleting backwards like <code>Backspace</code>. <code>^D</code> will also delete a line-break if the cursor is at the end of a line. Type <code>^Y</code> to delete the entire line the cursor is on or <code>^J</code> to delete just from the cursor to the end of the line. </p>
<p>Hit <code>^A</code> to move the cursor to the beginning of the line it&#8217;s on. Hit <code>^E</code> to move the cursor to the end of the line. Hit <code>^U</code> or <code>^V</code> for scrolling the cursor up or down 1/2 a screen&#8217;s worth. &quot;Scrolling&quot; means that the text on the screen moves, but the cursor stays at the same place relative to the screen. Hit <code>^K U</code> or <code>^K V</code> to move the cursor to the beginning or the end of the file. Look at the help screens in the editor to find even more delete and movement commands. </p>
<p>If you make a mistake, you can hit <code>^_</code> to &quot;undo&quot; it. On most keyboards you hit just <code>^-</code> to get <code>^_</code>, but on some you might have to hold both the <code>Shift</code> and <code>Control</code> keys down at the same time to get it. If you &quot;undo&quot; too much, you can &quot;redo&quot; the changes back into existence by hitting <code>^^</code> (type this with just <code>^6</code> on most keyboards). </p>
<p>If you were editing in one place within the file, and you then temporarily had to look or edit some other place within the file, you can get back to the original place by hitting <code>^K -</code>. This command actually returns you to the last place you made a change in the file. You can step through a history of places with <code>^K -</code> and <code>^K =</code>, in the same way you can step through the history of changes with the &quot;undo&quot; and &quot;redo&quot; commands. </p>
<p>When you are done editing the file, hit <code>^K X</code> to exit the editor. You will be prompted for a file name if you hadn&#8217;t already named the file you were editing. </p>
<p>When you edit a file, you actually edit only a copy of the file. So if you decide that you don&#8217;t want the changes you made to a file during a particular edit session, you can hit <code>^C</code> to exit the editor without saving them. </p>
<p>If you edit a file and save the changes, a &quot;backup&quot; copy of that file is created in the current directory, with a ~ appended to the name, which contains the original version of the file. </p>
<h3>Word wrap and formatting</h3>
<p>If you type past the right edge of the screen in a C language or PASCAL file, the screen will scroll to the right to follow the cursor. If you type past the right edge of the screen in a normal file (one whose name doesn&#8217;t end in .c, .h or .p), JOE will automatically wrap the last word onto the next line so that you don&#8217;t have to hit <code>Return</code>. This is called word-wrap mode. Word-wrap can be turned on or off with the <code>^T W</code> command. JOE&#8217;s initialisation file is usually set up so that this mode is automatically turned on for all non-program files. See the section below on the <code>joerc</code> file to change this and other defaults. </p>
<p>Aside for Word-wrap mode, JOE does not automatically keep paragraphs formatted like some word-processors. Instead, if you need a paragraph to be reformatted, hit <code>^K J</code>. This command &quot;fills in&quot; the paragraph that the cursor is in, fitting as many words in a line as is possible. A paragraph, in this case, is a block of text separated above and below by a blank line. </p>
<p>The margins which JOE uses for paragraph formatting and word-wrap can be set with the <code>^T L</code> and <code>^T R</code> commands. If the left margin is set to a value other than 1, then when you start typing at the beginning of a line, the cursor will immediately jump to the left margin. </p>
<p>If you want to center a line within the margins, use the <code>^K A</code> command. </p>
<h3>Over-type mode</h3>
<p>Sometimes it&#8217;s tiresome to have to delete old text before or after you insert new text. This happens, for example, when you are changing a table and you want to maintain the column position of the right side of the table. When this occurs, you can put the editor in over-type mode with <code>^T T</code>. When the editor is in this mode, the characters you type in replace existing characters, in the way an idealised typewriter would. Also, <code>Backspace</code> simply moves left instead of deleting the character to the left, when it&#8217;s not at the end or beginning of a line. Over-type mode is not the natural way of dealing with text electronically, so you should go back to insert-mode as soon as possible by typing <code>^T T</code> again. </p>
<p>If you need to insert while you&#8217;re in over-type mode, hit <code>^@</code>. This inserts a single SPACE into the text. </p>
<h3>Control and Meta characters</h3>
<p>Each character is represented by a number. For example, the number for &#8216;A&#8217; is 65 and the number for &#8216;1&#8217; is 49. All of the characters which you normally see have numbers in the range of 32 &#8211; 126 (this particular arbitrary assignment between characters and numbers is called the ASCII character set). The numbers outside of this range, from 0 to 255, aren&#8217;t usually displayed, but sometimes have other special meanings. The number 10, for example, is used for the line-breaks. You can enter these special, non-displayed <code>control characters</code> by first hitting <code>`</code> and then hitting a character in the range <code>@ A B C ... X Y Z [ ^ ] \ _</code> to get the number 0 - 31, and ? to get 127. For example, if you hit <code>` J</code>, you&#8217;ll insert a line-break character, or if you hit <code>` I</code>, you&#8217;ll insert a TAB character (which does the same thing the TAB key does). A useful control character to enter is 12 (<code>` L</code>), which causes most printers to advance to the top of the page. You&#8217;ll notice that JOE displays this character as an underlined L. You can enter the characters above 127, the <code>meta characters</code>, by first hitting <code>^\</code>. This adds 128 to the next (possibly control) character entered. JOE displays characters above 128 in inverse-video. Some foreign languages, which have more letters than English, use the meta characters for the rest of their alphabet. You have to put the editor in <code>ASIS</code> mode (described later) to have these passed untranslated to the terminal. </p>
<h3>Prompts</h3>
<p> If you hit <code>TAB</code> at any file name prompt, joe will attempt to complete the name you entered as much as possible. If it couldn&#8217;t complete the entire name, because there are more than one possible completions, joe beeps. If you hit <code>TAB</code> again, joe list the completions. You can use the arrow keys to move around this directory menu and press RETURN or SPACE to select an item. If you press the first letter of one of the directory entries, it will be selected, or if more than one entry has the same first letter, the cursor will jump between those entries. If you select a subdirectory or .., the directory name is appended to the prompt and the new directory is loaded into the menu. You can hit Backspace to go back to the previous directory. </p>
<p>Most prompts record a history of the responses you give them. You can hit up and down arrow to step through these histories. </p>
<p>Prompts are actually single line windows with no status line, so you can use any editing command that you normally use on text within the prompts. The prompt history is actually just other lines of the same &quot;prompt file&quot;. Thus you can can search backwards though the prompt history with the normal <code>^K F</code> command if you want. </p>
<p>Since prompts are windows, you can also switch out of them with <code>^K P</code> and <code>^K N</code>. </p>
<h3>Where am I?</h3>
<p>Hit <code>^K SPACE</code> to have JOE report the line number, column number, and byte number on the last line of the screen. The number associated with the character the cursor is on (its ASCII code) is also shown. You can have the line number and/or column number always displayed on the status line by setting placing the appropriate escape sequences in the status line setup strings. Edit the joerc file for details. </p>
<h3>File operations</h3>
<p>You can hit <code>^K D</code> to save the current file (possibly under a different name from what the file was called originally). After the file is saved, you can hit <code>^K E</code> to edit a different file. </p>
<p>If you want to save only a selected section of the file, see the section on <code>Blocks</code> below. </p>
<p>If you want to include another file in the file you&#8217;re editing, use <code>^K R</code> to insert it. </p>
<h3>Temporarily suspending the editor</h3>
<p>If you need to temporarily stop the editor and go back to the shell, hit <code>^K Z</code>. You might want to do this to stop whatever you&#8217;re editing and answer an e-mail message or read this man page, for example. You have to type <code>fg</code> or <code>exit</code> (you&#8217;ll be told which when you hit <code>^K Z</code>) to return to the editor. </p>
<h3>Searching for text</h3>
<p>Hit <code>^K F</code> to have the editor search forwards or backwards for a text fragment (<code>string</code>) for you. You will be prompted for the text to search for. After you hit <code>Return</code>, you are prompted to enter options. You can just hit <code>Return</code> again to have the editor immediately search forwards for the text, or you can enter one or more of these options: </p>
<dl>
<dt><code>b</dt>
<dd> <p> Search backwards instead of forwards. </p>
 </dd>
<dt>i</dt>
<dd> <p> Treat uppercase and lower case letters as the same when searching. Normally uppercase and lowercase letters are considered to be different. </p>
 </dd>
<dt>nnn</dt>
<dd> <p> (where nnn</code> is a number) If you enter a number, JOE searches for the Nth occurrence of the text. This is useful for going to specific places in files structured in some regular manner. </p>
 </dd>
<dt><code>r</dt>
<dd> <p> Replace text. If you enter the r</code> option, then you will be further prompted for replacement text. Each time the editor finds the search text, you will be prompted as to whether you want to replace the found search text with the replacement text. You hit: <code>y</code> to replace the text and then find the next occurrence, <code>n</code> to not replace this text, but to then find the next occurrence, <code>l</code> to replace the text and then stop searching, <code>r</code> to replace all of the remaining occurrences of the search text in the remainder of the file without asking for confirmation (subject to the <code>nnn</code> option above), or <code>^C</code> to stop searching and replacing. </p>
 </dd></dl>
<p>You can hit <code>^L</code> to repeat the previous search. </p>
<h3>Regular Expressions</h3>
<p>A number of special character sequences may be entered as search text: </p>
<dl>
<dt><code>\*</dt>
<dd> <p> This finds zero or more characters. For example, if you give A\*B</code> as the search text, JOE will try to find an A followed by any number of characters and then a B. </p>
 </dd>
<dt><code>\?</dt>
<dd> <p> This finds exactly one character. For example, if you give A\?B</code> as the search text, JOE will find AXB, but not AB or AXXB. </p>
 </dd>
<dt><code>\^&nbsp;<wbr>\$</dt>
<dd> <p> These match the beginning and end of a line. For example, if you give \^test\$</code>, then JOE with find <code>test</code> on a line by itself. </p>
 </dd>
<dt><code>\&lt;&nbsp;<wbr>\&gt;</dt>
<dd> <p> These match the beginning and end of a word. For example, if you give \&lt;\*is\*\&gt;</code>, then joe will find whole words which have the sub-string <code>is</code> within them. </p>
 </dd>
<dt><code>\[...]</dt>
<dd> <p> This matches any single character which appears within the brackets. For example, if \[Tt]his</code> is entered as the search string, then JOE finds both <code>This</code> and <code>this</code>. Ranges of characters can be entered within the brackets. For example, <code>\[A-Z]</code> finds any uppercase letter. If the first character given in the brackets is <code>^</code>, then JOE tries to find any character not given in the the brackets. </p>
 </dd>
<dt><code>\c</dt>
<dd> <p> This works like \*</code>, but matches a balanced C-language expression. For example, if you search for <code>malloc(\c)</code>, then JOE will find all function calls to <code>malloc</code>, even if there was a <code>)</code> within the parenthesis. </p>
 </dd>
<dt><code>\+</dt>
<dd> <p> This finds zero or more of the character which immediately follows the \+</code>. For example, if you give <code>\[ ]\+\[ ]</code>, where the characters within the brackets are both SPACE and TAB, then JOE will find whitespace. </p>
 </dd>
<dt><code>\\</dt>
<dd> <p> Matches a single \. </p>
 </dd>
<dt>\n</dt>
<dd> <p> This finds the special end-of-line or line-break character. </p>
 </dd></dl>
<p>A number of special character sequences may also be given in the replacement string: </p>
<dl>
<dt>\&amp;</dt>
<dd> <p> This gets replaced by the text which matched the search string. For example, if the search string was \&lt;\*\&gt;</code>, which matches words, and you give <code>&quot;\&amp;&quot;</code>, then joe will put quote marks around words. </p>
 </dd>
<dt><code>\0 -&nbsp;<wbr>\9</dt>
<dd> <p> These get replaced with the text which matched the Nth \*</code>, <code>\?</code>, <code>\+</code>, <code>\c</code>, <code>\+</code>, or <code>\[...]</code> in the search string. </p>
 </dd>
<dt><code>\\</dt>
<dd> <p> Use this if you need to put a \</code> in the replacement string. </p>
 </dd>
<dt><code>\n</dt>
<dd> <p> Use this if you need to put a line-break in the replacement string. </p>
 </dd></dl>
<p>Some examples: </p>
<p>Suppose you have a list of addresses, each on a separate line, which starts with &quot;Address:&quot; and has each element separated by commas. Like so: </p>
<p>Address: S. Holmes, 221b Baker St., London, England </p>
<p>If you wanted to rearrange the list, to get the country first, then the city, then the person&#8217;s name, and then the address, you could do this: </p>
<p>Type ^K F</code> to start the search, and type: </p>
<p> <code>Address:\*,\*,\*,\*\$</code> </p>
<p>to match &quot;Address:&quot;, the four comma-separated elements, and then the end of the line. When asked for options, you would type <code>r</code> to replace the string, and then type: </p>
<p> <code>Address:\3,\2,\0,\1</code> </p>
<p>To shuffle the information the way you want it. After hitting return, the search would begin, and the sample line would be changed to: </p>
<p>Address: England, London, S. Holmes, 221b Baker St. </p>
<h3>Blocks</h3>
<p>If you want to move, copy, save or delete a specific section of text, you can do it with highlighted blocks. First, move the cursor to the start of the section of text you want to work on, and press <code>^K B</code>. Then move the cursor to the character just after the end of the text you want to affect and press <code>^K K</code>. The text between the <code>^K B</code> and <code>^K K</code> should become highlighted. Now you can move your cursor to someplace else in your document and press <code>^K M</code> to move the highlighted text there. You can press <code>^K C</code> to make a copy of the highlighted text and insert it to where the cursor is positioned. <code>^K Y</code> to deletes the highlighted text. <code>^K W</code>, writes the highlighted text to a file. </p>
<p>A very useful command is <code>^K /</code>, which filters a block of text through a unix command. For example, if you select a list of words with <code>^K B</code> and <code>^K K</code>, and then type <code>^K / sort</code>, the list of words will be sorted. Another useful unix command for <code>^K /</code>, is <code>tr</code>. If you type <code>^K / tr a-z A-Z</code>, then all of the letters in the highlighted block will be converted to uppercase. </p>
<p>After you are finished with some block operations, you can just leave the highlighting on if you don&#8217;t mind it (of course, if you accidentally hit <code>^K Y</code> without noticing...). If it really bothers you, however, just hit <code>^K B ^K K</code>, to turn the highlighting off. </p>
<h3>Indenting program blocks</h3>
<p> Auto-indent mode toggled with the <code>^T I</code> command. The <code>joerc</code> is normally set up so that files with names ending with .p, .c or .h have auto-indent mode enabled. When auto-indent mode is enabled and you hit <code>Return</code>, the cursor will be placed in the same column that the first non-SPACE/TAB character was in on the original line. </p>
<p>You can use the <code>^K ,</code> and <code>^K .</code> commands to shift a block of text to the left or right. If no highlighting is set when you give these commands, the program block the cursor is located in will be selected, and will be moved by subsequent <code>^K ,</code> and <code>^K .</code> commands. The number of columns these commands shift by can be set through a <code>^T</code> option. </p>
<h3>Windows</h3>
<p> You can edit more than one file at the same time or edit two or more different places of the same file. To do this, hit <code>^K O</code>, to split the screen into two windows. Use <code>^K P</code> or <code>^K N</code> to move the cursor into the top window or the lower window. Use <code>^K E</code> to edit a new file in one of the windows. A window will go away when you save the file with <code>^K X</code> or abort the file with <code>^C</code>. If you abort a file which exists in two windows, one of the window goes away, not the file. </p>
<p>You can hit <code>^K O</code> within a window to create even more windows. If you have too many windows on the screen, but you don&#8217;t want to eliminate them, you can hit <code>^K I</code>. This will show only the window the cursor is in, or if there was only one window on the screen to begin with, try to fit all hidden windows on the screen. If there are more windows than can fit on the screen, you can hit <code>^K N</code> on the bottom-most window or <code>^K P</code> on the top-most window to get to them. </p>
<p>If you gave more than one file name to JOE on the command line, each file will be placed in a different window. </p>
<p>You can change the height of the windows with the <code>^K G</code> and <code>^K T</code> commands. </p>
<h3>Keyboard macros</h3>
<p>Macros allow you to record a series of keystrokes and replay them with the press of two keys. This is useful to automate repetitive tasks. To start a macro recording, hit <code>^K [</code> followed by a number from 0 to 9. The status line will display (Macro n recording...). Now, type in the series of keystrokes that you want to be able to repeat. The commands you type will have their usual effect. Hit <code>^K ]</code> to stop recording the macro. Hit <code>^K</code> followed by the number you recorded the macro in to execute one iteration of the key-strokes. </p>
<p>For example, if you want to put &quot;**&quot; in front of a number of lines, you can type: </p>
<p> <code>^K [ ^A ** </code>&lt;down arrow&gt; <code>^K ]</code> </p>
<p>Which starts the macro recording, moves the cursor to the beginning of the line, inserts &quot;**&quot;, moves the cursor down one line, and then ends the recording. Since we included the key-strokes needed to position the cursor on the next line, we can repeatedly use this macro without having to move the cursor ourselves, something you should always keep in mind when recording a macro. </p>
<p>If you find that the macro you are recording itself has a repeated set of key-strokes in it, you can record a macro within the macro, as long as you use a different macro number. Also you can execute previously recorded macros from within new macros. </p>
<h3>Repeat</h3>
<p> You can use the repeat command, <code>^K \</code>, to repeat a macro, or any other edit command or even a normal character, a specified number of times. Hit <code>^K \</code>, type in the number of times you want the command repeated and press <code>Return</code>. The next edit command you now give will be repeated that many times. </p>
<p>For example, to delete the next 20 lines of text, type: </p>
<p> <code>^K &nbsp;<wbr>20</code>&lt;return&gt;<code>^Y</code> </p>
<h3>Rectangle mode</h3>
<p> Type <code>^T X</code> to have <code>^K B</code> and <code>^K K</code> select rectangular blocks instead of stream-of-text blocks. This mode is useful for moving, copying, deleting or saving columns of text. You can also filter columns of text with the <code>^K /</code> command- if you want to sort a column, for example. The insert file command, <code>^K R</code> is also effected. </p>
<p>When rectangle mode is selected, over-type mode is also useful (<code>^T T</code>). When over-type mode is selected, rectangles will replace existing text instead of getting inserted before it. Also the delete block command (<code>^K Y</code>) will clear the selected rectangle with SPACEs and TABs instead of deleting it. Over-type mode is especially useful for the filter block command (<code>^K /</code>), since it will maintain the original width of the selected column. </p>
<h3>Tag search</h3>
<p> If you are editing a large C program with many source files, you can use the <code>ctags</code> program to generate a <code>tags</code> file. This file contains a list of program symbols and the files and positions where the symbols are defined. The <code>^K ;</code> command can be used to lookup a symbol (functions, defined constants, etc.), load the file where the symbol is defined into the current window and position the cursor to where the symbol is defined. <code>^K ;</code> prompts you for the symbol you want, but uses the symbol the cursor was on as a default. Since <code>^K ;</code> loads the definition file into the current window, you probably want to split the window first with <code>^K O</code>, to have both the original file and the definition file loaded. </p>
<h3>Shell windows</h3>
<p> Hit <code>^K &#8216;</code> to run a command shell in one of JOE&#8217;s windows. When the cursor is at the end of a shell window (use <code>^K V</code> if it&#8217;s not), whatever you type is passed to the shell instead of the window. Any output from the shell or from commands executed in the shell is appended to the shell window (the cursor will follow this output if it&#8217;s at the end of the shell window). This command is useful for recording the results of shell commands- for example the output of <code>make</code>, the result of <code>grep</code>ping a set of files for a string, or directory listings from <code>FTP</code> sessions. Besides typeable characters, the keys ^C, Backspace, DEL, Return and ^D are passed to the shell. Type the shell <code>exit</code> command to stop recording shell output. If you press <code>^C</code> in a shell window, when the cursor is not at the end of the window, the shell is <code>kill</code>ed. </p>
<h2>Environment variables</h2>
<p>For JOE to operate correctly, a number of other environment settings must be correct. The throughput (baud rate) of the connection between the computer and your terminal must be set correctly for JOE to update the screen smoothly and allow typeahead to defer the screen update. Use the stty nnn</code> command to set this. You want to set it as close as possible to actual throughput of the connection. For example, if you are connected via a 1200 baud modem, you want to use this value for <code>stty</code>. If you are connected via 14.4k modem, but the terminal server you are connected to connects to the computer a 9600 baud, you want to set your speed as 9600 baud. The special baud rate of 38400 or <code>extb</code> is used to indicate that you have a very-high speed connection, such as a memory mapped console or an X-window terminal emulator. If you can&#8217;t use <code>stty</code> to set the actual throughput (perhaps because of a modem communicating with the computer at a different rate than it&#8217;s communicating over the phone line), you can put a numeric value in the <code>BAUD</code> environment variable instead (use <code>setenv BAUD 9600</code> for csh or <code>BAUD=9600; export BAUD</code> for sh). </p>
<p>The <code>SHELL</code> or <code>EXECSHELL</code> environment variable must be set to the full pathname of a shell executable that accepts the -i (interactive) and -c (run a command) arguments of the Korn Shell; otherwise, <code>/bin/sh</code> is used. </p>
<p>The <code>TERM</code> environment variable must be set to the type of terminal you&#8217;re using. If the size (number of lines/columns) of your terminal is different from what is reported in the TERMCAP or TERMINFO entry, you can set this with the <code>stty rows nn cols nn</code> command, or by setting the <code>LINES</code> and <code>COLUMNS</code> environment variables. </p>
<p>The <code>xterm-xfree86</code> terminal allows automatic entering and leaving of the bracketed paste mode. </p>
<p>The <code>JOETERM</code> environment variable may be set to override the regular <code>TERM</code> environment variable for specifying your terminal type. </p>
<p>JOE uses two character maps for its operation: the terminal I/O character map, which determines how characters are sent to the terminal and whether the %a/%A message specifiers use Unicode, and the file encoding, which can be specified per file using the <code>-encoding</code> option and changed with the <code>^T E</code> command, and which defaults to the terminal I/O character map, which, in turn, is determined from the current locale, if the system supports such, otherwise the <code>LC_ALL</code>, <code>LC_CTYPE</code> and <code>LANG</code> environment variables (if they contain a period, only the part after it and before an optional &quot;at sign&quot; is used); on cygwin32 before 1.7.2, the codepage is used instead if the POSIX locale environment variables are empty; the environment variable <code>JOECHARMAP</code> can be used to manually force one overriding all methods described above, and can be used together with <code>-encoding</code> to specify a different default file character map. </p>
<p>JOE normally expects that flow control between the computer and your terminal to use ^S/^Q handshaking (I.E., if the computer is sending characters too fast for your terminal, your terminal sends ^S to stop the output and ^Q to restart it). If the flow control uses out-of-band or hardware handshaking or if your terminal is fast enough to always keep up with the computer output and you wish to map ^S/^Q to edit commands, you can set the environment variable <code>NOXON</code> to have JOE attempt to turn off ^S/^Q handshaking. If the connection between the computer and your terminal uses no handshaking and your terminal is not fast enough to keep up with the output of the computer, you can set the environment variable <code>DOPADDING</code> to have <code>JOE</code> slow down the output by interspersing PAD characters between the terminal screen update sequences. </p>
<h2>Filenames</h2>
<p> Wherever JOE expects you to enter a file name, whether on the command line or in prompts within the editor, you may also type: </p>
<dl>
<dt><code>!command</dt>
<dd> <p> Read or write data to or from a shell command. For example, use joe &#8216;!ls&#8217;</code> to get a copy of your directory listing to edit or from within the editor use <code>^K D !mail jhallen [at] world.std.com</code> to send the file being edited to me. </p>
 </dd>
<dt><code>&gt;&gt;filename</dt>
<dd> <p> Use this to have JOE append the edited text to the end of the file &quot;filename.&quot; </p>
 </dd>
<dt>filename,START,SIZE</dt>
<dd> <p> Use this to access a fixed section of a file or device. START</code> and <code>SIZE</code> may be entered in decimal (ex.: 123) octal (ex.: 0777) or hexadecimal (ex.: 0xFF). For example, use <code>joe /dev/fd0,508,2</code> to edit bytes 508 and 509 of the first floppy drive in Linux. </p>
 </dd>
<dt><code>-</dt>
<dd> <p> Use this to get input from the standard input or to write output to the standard output. For example, you can put joe in a pipe of commands: quota -v | joe - | mail root</code>, if you want to complain about your low quota. </p>
 </dd></dl>
<h2>The joerc file</h2>
<p> <code>^T</code> options, the help screens and the key-sequence to editor command bindings are all defined in JOE&#8217;s initialisation file. If you make a copy of this file (which normally resides in <code>/etc/jupp/joe/joerc</code>) to <code>$HOME/.joerc</code>, you can customise these settings to your liking. The syntax of the initialisation file should be fairly obvious, and there are further instruction in it. </p>
<h2>Acknowledgments</h2>
<p> JOE was written by Joseph H. Allen. If you have bug reports or questions, e-mail them to jhallen [at] world.std.com. Larry Foard (entropy [at] world.std.com) and Gary Gray (ggray [at] world.std.com) also helped with the creation of JOE. Thorsten &quot;mirabilos&quot; Glaser (tg [at] mirbsd.org) created JUPP, and the 16-bit MS-DOS version of JUPP 2.8 was compiled by Andreas Totlis (atotlis [at] t-online.de). </p>
<h2>Bugs</h2>
<p> This manual page describes only the JOE flavour; documentation for JUPP is especially missing. </p>
