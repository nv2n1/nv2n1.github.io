---
title: "joe(1)"
name: "joe"
section: "1"
letter: "j"
url: "/docs/linux/man/1-joe/"
description: "joe – Joe’s Own Editor"
---

<h2>Name</h2>
<p> joe &#8211; Joe&#8217;s Own Editor</p>
<h2>Syntax</h2>
<p> <code>joe [global-options] [ [local-options] filename ]&#8230;</code> </p>
<p> <code>jstar [global-options] [ [local-options] filename ]&#8230;</code> </p>
<p> <code>jmacs [global-options] [ [local-options] filename ]&#8230;</code> </p>
<p> <code>rjoe [global-options] [ [local-options] filename ]&#8230;</code> </p>
<p> <code>jpico [global-options] [ [local-options] filename ]&#8230;</code></p>
<h2>Description</h2>
<p> JOE is a powerful ASCII-text screen editor. It has a &quot;mode-less&quot; user interface which is similar to many user-friendly PC editors. Users of Micro-Pro&#8217;s WordStar or Borland&#8217;s &quot;Turbo&quot; languages will feel at home. JOE is a full featured UNIX screen-editor though, and has many features for editing programs and text. </p>
<p> JOE also emulates several other editors. JSTAR is a close imitation of WordStar with many &quot;JOE&quot; extensions. JPICO is a close imitation of the Pine mailing system&#8217;s PICO editor, but with many extensions and improvements. JMACS is a GNU-EMACS imitation. RJOE is a restricted version of JOE, which allows you to edit only the files specified on the command line. </p>
<p> Although JOE is actually five different editors, it still requires only one executable, but one with five different names. The name of the editor with an &quot;rc&quot; appended gives the name of JOE&#8217;s initialization file, which determines the personality of the editor. </p>
<p> JOE is free software; you can distribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation. I have no plans for turning JOE into a commercial or share-ware product. JOE is available over the Internet from <code><a rel="nofollow" href="http://www.sourceforge.net">www.sourceforge.net</a>/projects/joe-editor</code>. </p>
<h2>Usage</h2>
<p> To start the editor, type <code>joe</code> followed by zero or more names of files you want to edit. Each file name may be preceded by a local option setting (see the local options table which follows). Other global options, which apply to the editor as a whole, may also be placed on the command line (see the global options table which follows). If you are editing a new file, you can either give the name of the new file when you invoke the editor, or in the editor when you save the new file. A modified syntax for file names is provided to allow you to edit program output, standard input/output, or sections of files or devices. See the section <code>Filenames</code> below for details. </p>
<p> Once you are in the editor, you can type in text and use special control-character sequences to perform other editing tasks. To find out what the control-character sequences are, read the rest of this man page or type <code>^K H</code> for help in the editor. </p>
<p> Now for some obscure computer-lore: </p>
<p> The <code>^</code> means that you hold down the <code>Control</code> key while pressing the following key (the same way the <code>Shift</code> key works for uppercase letters). A number of control-key sequences are duplicated on other keys, so that you don&#8217;t need to press the control key: <code>ESC</code> will work in place of <code>^[</code>, <code>Del</code> will work in place of <code>^?</code>, <code>Backspace</code> will work in place of <code>^H</code>, <code>Tab</code> will work in place of <code>^I</code>, <code>Return</code> or <code>Enter</code> will work in place of <code>^M</code> and <code>Linefeed</code> will work in place of <code>^J</code>. Some keyboards may give you trouble with some control keys. <code>^_</code>, <code>^^</code> and <code>^@</code> can usually be entered without pressing shift (I.E., try <code>^-</code>, <code>^6</code> and <code>^2</code>). Other keyboards may reassign these to other keys. Try: <code>^.</code>, <code>^,</code> and <code>^/</code>. <code>^SPACE</code> can usually be used in place of <code>^@</code>. <code>^\</code> and <code>^]</code> are interpreted by many communication programs, including telnet and kermit. Usually you just hit the key twice to get it to pass through the communication program. </p>
<p> Once you have typed <code>^K H</code>, the first help window appears at the top of the screen. You can continue to enter and edit text while the help window is on. To page through other topics, hit ^[, and ^[. (that is, ESC , and ESC .). Use <code>^K H</code> to dismiss the help window. </p>
<p> You can customize the keyboard layout, the help screens and a number of behavior defaults by copying JOE&#8217;s initialization file (usually <code>/etc/joe/joerc</code>) to <code>.joerc</code> in your home directory and then by modifying it. See the section <code>joerc</code> below. </p>
<p> To have JOE used as your default editor for e-mail and News, you need to set the <code>EDITOR</code> and <code>VISUAL</code> environment variables in your shell initialization file (<code>.cshrc</code> or <code>.profile</code>) to refer to JOE (joe usually resides as <code>/usr/bin/joe</code>). </p>
<p> There are a number of other obscure invocation parameters which may have to be set, particularly if your terminal screen is not updating as you think it should. See the section <code>Environment variables</code> below. </p>
<h2>Command Line Options</h2>
<p> The following global options may be specified on the command line: </p>
<dl>
<dt>-asis</p>
<dd> Characters with codes above 127 will be sent to the terminal as-is, instead of as inverse of the corresponding character below 128. If this does not work, check your terminal server. </p>
<dt>-backpath path</p>
<dd> If this option is given, backup files will be stored in the specified directory instead of in each file&#8217;s original directory. </p>
<dt>-baud nnn</p>
<dd> Set the baud rate for the purposes of terminal screen optimization. Joe inserts delays for baud rates below 19200, which bypasses tty buffering so that typeahead will interrupt the screen output. Scrolling commands will not be used for 38400 baud. This is useful for X-terms and other console ttys which really aren&#8217;t going over a serial line. </p>
<dt>-beep</p>
<dd> Joe will beep on command errors and when the cursor goes past extremes. </p>
<dt>-columns nnn</p>
<dd> Sets the number of screen columns. </p>
<dt>-csmode</p>
<dd> Continued search mode: a search immediately following a search will repeat the previous search instead of prompting for new string. This is useful for the the ^[S and ^[R commands and for when joe is trying to be emacs. </p>
<dt>-dopadding</p>
<dd> Joe usually assumes that there is some kind of flow control between it and the tty. If there isn&#8217;t, this option will make joe output extra ^@s to the tty as specified by the termcap entry. The extra ^@s allow the terminal to catch up after long terminal commands. </p>
<dt>-exask</p>
<dd> This option makes ^KX verify the file name that it&#8217;s about to write. </p>
<dt>-force</p>
<dd> This option makes sure that the last line of the file has a line-feed which it&#8217;s saved. </p>
<dt>-help</p>
<dd> The editor will start with the help screen on if this option is given. </p>
<dt>-keepup</p>
<dd> Normally the column number and control-key prefix fields of the status lines are on a one second delay to reduce CPU consumption, but with this option they are updated after each key-stroke. </p>
<dt>-lightoff</p>
<dd> The block highlighting will go away after any block command if this option is given. </p>
<dt>-lines nnn</p>
<dd> Sets the number of screen lines. </p>
<dt>-marking</p>
<dd> Text between ^KB and the cursor is highlighted (use with -lightoff and a modified joerc file to have drop-anchor style block selection). </p>
<dt>-mid</p>
<dd> If this option is set and the cursor moves off the window, the window will be scrolled so that the cursor is in the center. This option is forced on slow terminals which don&#8217;t have scrolling commands. </p>
<dt>-nobackups</p>
<dd> This option prevents backup files. </p>
<dt>-nonotice</p>
<dd> This option prevent the copyright notice from being displayed when the editor starts. </p>
<dt>-nosta</p>
<dd> This option eliminates the top-most status line. It&#8217;s nice for when you only want to see your text on the screen or if you&#8217;re using a vt52. </p>
<dt>-noxon</p>
<dd> Attempt to turn off ^S/^Q processing. This is useful for when joe is trying to be WordStar or EMACS. </p>
<dt>-orphan</p>
<dd> When this option is active, extra files on the command line will be placed in orphaned buffers instead of in extra windows. This is useful for when joe is trying to be emacs. </p>
<dt>-pg nnn</p>
<dd> This specifies the number of lines to keep after PgUp/PgDn (^U/^V). If -1 is given, half the window is kept. </p>
<dt>-skiptop nnn</p>
<dd> Don&#8217;t use the top nnn lines of the screen. Useful for when joe is used as a BBS editor. </p>
</dl>
<p> Each of these options may be specified in the joerc file as well. In addition, the NOXON, BAUD, LINES, COLUMNS and DOPADDING options may be specified with environment variables. </p>
<p> The JOETERM environment variable may be set to override the regular TERM environment variable for specifying your terminal type. </p>
<p> The following options may be specified before each filename on the command line: </p>
<dl>
<dt>+nnn</p>
<dd> The cursor starts on the specified line. </p>
<dt>-crlf</p>
<dd> Joe uses CR-LF as the end of line sequence instead of just LF. This is for editing MS-DOS or VMS files. </p>
<dt>-wordwrap</p>
<dd> Joe wraps the previous word when you type past the right margin. </p>
<dt>-autoindent</p>
<dd> When you hit Return on an indented line, the indentation is duplicated onto the new line. </p>
<dt>-overwrite</p>
<dd> Typing overwrites existing characters instead of inserting before them. </p>
<dt>-lmargin nnn</p>
<dd> Sets the left margin. </p>
<dt>-rmargin nnn</p>
<dd> Sets the right margin. </p>
<dt>-tab nnn</p>
<dd> Sets the tab width. </p>
<dt>-indentc nnn</p>
<dd> Sets the indentation character for ^K, and ^K. (32 for SPACE, 9 for TAB). </p>
<dt>-istep nnn</p>
<dd> Sets the indentation step for ^K, and ^K.. </p>
<dt>-linums</p>
<dd> Line numbers are displayed before each line. </p>
<dt>-rdonly</p>
<dd> The file is read only. </p>
<dt>-keymap name</p>
<dd> Use an alternate section of the joerc file for the key sequence bindings. </p>
</dl>
<p> These options can also be specified in the joerc file. They can be set depending on the file-name extension. Programs (.c, .h or .p extension) usually have autoindent enabled. Wordwrap is enabled on other files, but rc files have it disabled. </p>
<h2>Editing Tasks</h2>
<h3>Basic Editing</h3>
<p> When you type characters into the editor, they are normally inserted into the file being edited (or appended to the file if the cursor is at the end of the file). This is the normal operating mode of the editor. If you want to replace some existing text, you have to delete the old text before or after you type in the replacement text. The <code>Backspace</code> key can be used for deleting text: move the cursor to right after the text you want to delete and hit <code>Backspace</code> a number of times. </p>
<p> Hit the <code>Enter</code> or <code>Return</code> key to insert a line-break. For example, if the cursor was in the middle of a line and you hit <code>Return</code>, the line would be split into two lines with the cursor appearing at the beginning of the second line. Hit <code>Backspace</code> at the beginning of a line to eliminate a line-break. </p>
<p> Use the arrow keys to move around the file. If your keyboard doesn&#8217;t have arrow keys (or if they don&#8217;t work for some reason), use <code>^F</code> to move forwards (right), <code>^B</code> to move backwards (left), <code>^P</code> to move to the previous line (up), and <code>^N</code> to move to the next line (down). The right and left arrow keys simply move forwards or backwards one character at a time through the text: if you&#8217;re at the beginning of a line and you press left-arrow, you will end up at the end of the previous line. The up and down arrow keys move forwards and backwards by enough characters so that the cursor appears in the same column that it was in on the original line. </p>
<p> If you want to indent the text you enter, you can use the <code>TAB</code> key. This inserts a special control character which makes the characters which follow it begin at the next TAB STOP. TAB STOPS normally occur every 8 columns, but this can be changed with the <code>^T D</code> command. PASCAL and C programmers often set TAB STOPS on every 4 columns. </p>
<p> If for some reason your terminal screen gets messed up (for example, if you receive a mail notice from biff), you can have the editor refresh the screen by hitting <code>^R</code>. </p>
<p> There are many other keys for deleting text and moving around the file. For example, hit <code>^D</code> to delete the character the cursor is on instead of deleting backwards like <code>Backspace</code>. <code>^D</code> will also delete a line-break if the cursor is at the end of a line. Type <code>^Y</code> to delete the entire line the cursor is on or <code>^J</code> to delete just from the cursor to the end of the line. </p>
<p> Hit <code>^A</code> to move the cursor to the beginning of the line it&#8217;s on. Hit <code>^E</code> to move the cursor to the end of the line. Hit <code>^U</code> or <code>^V</code> for scrolling the cursor up or down 1/2 a screen&#8217;s worth. &quot;Scrolling&quot; means that the text on the screen moves, but the cursor stays at the same place relative to the screen. Hit <code>^K U</code> or <code>^K V</code> to move the cursor to the beginning or the end of the file. Look at the help screens in the editor to find even more delete and movement commands. </p>
<p> If you make a mistake, you can hit <code>^_</code> to &quot;undo&quot; it. On most keyboards you hit just <code>^-</code> to get <code>^_</code>, but on some you might have to hold both the <code>Shift</code> and <code>Control</code> keys down at the same time to get it. If you &quot;undo&quot; too much, you can &quot;redo&quot; the changes back into existence by hitting <code>^^</code> (type this with just <code>^6</code> on most keyboards). </p>
<p> If you were editing in one place within the file, and you then temporarily had to look or edit some other place within the file, you can get back to the original place by hitting <code>^K &#8211;</code>. This command actually returns you to the last place you made a change in the file. You can step through a history of places with <code>^K &#8211;</code> and <code>^K =</code>, in the same way you can step through the history of changes with the &quot;undo&quot; and &quot;redo&quot; commands. </p>
<p> When you are done editing the file, hit <code>^K X</code> to exit the editor. You will be prompted for a file name if you hadn&#8217;t already named the file you were editing. </p>
<p> When you edit a file, you actually edit only a copy of the file. So if you decide that you don&#8217;t want the changes you made to a file during a particular edit session, you can hit <code>^C</code> to exit the editor without saving them. </p>
<p> If you edit a file and save the changes, a &quot;backup&quot; copy of that file is created in the current directory, with a ~ appended to the name, which contains the original version of the file. </p>
<h3>Word wrap and formatting</h3>
<p> If you type past the right edge of the screen in a C language or PASCAL file, the screen will scroll to the right to follow the cursor. If you type past the right edge of the screen in a normal file (one whose name doesn&#8217;t end in .c, .h or .p), JOE will automatically wrap the last word onto the next line so that you don&#8217;t have to hit <code>Return</code>. This is called word-wrap mode. Word-wrap can be turned on or off with the <code>^T W</code> command. JOE&#8217;s initialization file is usually set up so that this mode is automatically turned on for all non-program files. See the section below on the <code>joerc</code> file to change this and other defaults. </p>
<p> Aside for Word-wrap mode, JOE does not automatically keep paragraphs formatted like some word-processors. Instead, if you need a paragraph to be reformatted, hit <code>^K J</code>. This command &quot;fills in&quot; the paragraph that the cursor is in, fitting as many words in a line as is possible. A paragraph, in this case, is a block of text separated above and below by a blank line. </p>
<p> The margins which JOE uses for paragraph formatting and word-wrap can be set with the <code>^T L</code> and <code>^T R</code> commands. If the left margin is set to a value other than 1, then when you start typing at the beginning of a line, the cursor will immediately jump to the left margin. </p>
<p> If you want to center a line within the margins, use the <code>^K A</code> command. </p>
<h3>Over-type mode</h3>
<p> Sometimes it&#8217;s tiresome to have to delete old text before or after you insert new text. This happens, for example, when you are changing a table and you want to maintain the column position of the right side of the table. When this occurs, you can put the editor in over-type mode with <code>^T T</code>. When the editor is in this mode, the characters you type in replace existing characters, in the way an idealized typewriter would. Also, <code>Backspace</code> simply moves left instead of deleting the character to the left, when it&#8217;s not at the end or beginning of a line. Over-type mode is not the natural way of dealing with text electronically, so you should go back to insert-mode as soon as possible by typing <code>^T T</code> again. </p>
<p> If you need to insert while you&#8217;re in over-type mode, hit <code>^@</code>. This inserts a single SPACE into the text. </p>
<h3>Control and Meta characters</h3>
<p> Each character is represented by a number. For example, the number for &#8216;A&#8217; is 65 and the number for &#8216;1&#8217; is 49. All of the characters which you normally see have numbers in the range of 32 &#8211; 126 (this particular arbitrary assignment between characters and numbers is called the ASCII character set). The numbers outside of this range, from 0 to 255, aren&#8217;t usually displayed, but sometimes have other special meanings. The number 10, for example, is used for the line-breaks. You can enter these special, non-displayed <code>control characters</code> by first hitting <code>`</code> and then hitting a character in the range <code>@ A B C &#8230; X Y Z [ ^ ] \ _</code> to get the number 0 &#8211; 31, and ? to get 127. For example, if you hit <code>` J</code>, you&#8217;ll insert a line-break character, or if you hit <code>` I</code>, you&#8217;ll insert a TAB character (which does the same thing the TAB key does). A useful control character to enter is 12 (<code>` L</code>), which causes most printers to advance to the top of the page. You&#8217;ll notice that JOE displays this character as an underlined L. You can enter the characters above 127, the <code>meta characters</code>, by first hitting <code>^\</code>. This adds 128 to the next (possibly control) character entered. JOE displays characters above 128 in inverse-video. Some foreign languages, which have more letters than English, use the meta characters for the rest of their alphabet. You have to put the editor in <code>ASIS</code> mode (described later) to have these passed untranslated to the terminal. </p>
<h3>Prompts</h3>
<p> If you hit <code>TAB</code> at any file name prompt, joe will attempt to complete the name you entered as much as possible. If it couldn&#8217;t complete the entire name, because there are more than one possible completions, joe beeps. If you hit <code>TAB</code> again, joe list the completions. You can use the arrow keys to move around this directory menu and press RETURN or SPACE to select an item. If you press the first letter of one of the directory entries, it will be selected, or if more than one entry has the same first letter, the cursor will jump between those entries. If you select a subdirectory or .., the directory name is appended to the prompt and the new directory is loaded into the menu. You can hit Backspace to go back to the previous directory. </p>
<p> Most prompts record a history of the responses you give them. You can hit up and down arrow to step through these histories. </p>
<p> Prompts are actually single line windows with no status line, so you can use any editing command that you normally use on text within the prompts. The prompt history is actually just other lines of the same &quot;prompt file&quot;. Thus you can can search backwards though the prompt history with the normal <code>^K F</code> command if you want. </p>
<p> Since prompts are windows, you can also switch out of them with <code>^K P</code> and <code>^K N</code>. </p>
<h3>Where am I?</h3>
<p> Hit <code>^K SPACE</code> to have JOE report the line number, column number, and byte number on the last line of the screen. The number associated with the character the cursor is on (its ASCII code) is also shown. You can have the line number and/or column number always displayed on the status line by setting placing the appropriate escape sequences in the status line setup strings. Edit the joerc file for details. </p>
<h3>File operations</h3>
<p> You can hit <code>^K D</code> to save the current file (possibly under a different name from what the file was called originally). After the file is saved, you can hit <code>^K E</code> to edit a different file. </p>
<p> If you want to save only a selected section of the file, see the section on <code>Blocks</code> below. </p>
<p> If you want to include another file in the file you&#8217;re editing, use <code>^K R</code> to insert it. </p>
<h3>Temporarily suspending the editor</h3>
<p> If you need to temporarily stop the editor and go back to the shell, hit <code>^K Z</code>. You might want to do this to stop whatever you&#8217;re editing and answer an e-mail message or read this man page, for example. You have to type <code>fg</code> or <code>exit</code> (you&#8217;ll be told which when you hit <code>^K Z</code>) to return to the editor. </p>
<h3>Searching for text</h3>
<p> Hit <code>^K F</code> to have the editor search forwards or backwards for a text fragment (<code>string</code>) for you. You will be prompted for the text to search for. After you hit <code>Return</code>, you are prompted to enter options. You can just hit <code>Return</code> again to have the editor immediately search forwards for the text, or you can enter one or more of these options: </p>
<dl>
<dt><code>b</p>
<dd> Search backwards instead of forwards. </p>
<dt>i</p>
<dd> Treat uppercase and lower case letters as the same when searching. Normally uppercase and lowercase letters are considered to be different. </p>
<dt>nnn</p>
<dd> (where nnn</code> is a number) If you enter a number, JOE searches for the Nth occurrence of the text. This is useful for going to specific places in files structured in some regular manner. </p>
<dt><code>r</p>
<dd> Replace text. If you enter the r</code> option, then you will be further prompted for replacement text. Each time the editor finds the search text, you will be prompted as to whether you want to replace the found search text with the replacement text. You hit: <code>y</code> to replace the text and then find the next occurrence, <code>n</code> to not replace this text, but to then find the next occurrence, <code>r</code> to replace all of the remaining occurrences of the search text in the remainder of the file without asking for confirmation (subject to the <code>nnn</code> option above), or <code>^C</code> to stop searching and replacing. </p>
</dl>
<p> You can hit <code>^L</code> to repeat the previous search. </p>
<h3>Regular Expressions</h3>
<p> A number of special character sequences may be entered as search text: </p>
<dl>
<dt><code>\*</p>
<dd> This finds zero or more characters. For example, if you give A\*B</code> as the search text, JOE will try to find an A followed by any number of characters and then a B. </p>
<dt><code>\?</p>
<dd> This finds exactly one character. For example, if you give A\?B</code> as the search text, JOE will find AXB, but not AB or AXXB. </p>
<dt><code>\^&nbsp;<wbr>\$</p>
<dd> These match the beginning and end of a line. For example, if you give \^test\$</code>, then JOE with find <code>test</code> on a line by itself. </p>
<dt><code>\&lt;&nbsp;<wbr>\&gt;</p>
<dd> These match the beginning and end of a word. For example, if you give \&lt;\*is\*\&gt;</code>, then joe will find whole words which have the sub-string <code>is</code> within them. </p>
<dt><code>\[&#8230;]</p>
<dd> This matches any single character which appears within the brackets. For example, if \[Tt]his</code> is entered as the search string, then JOE finds both <code>This</code> and <code>this</code>. Ranges of characters can be entered within the brackets. For example, <code>\[A-Z]</code> finds any uppercase letter. If the first character given in the brackets is <code>^</code>, then JOE tries to find any character not given in the the brackets. </p>
<dt><code>
