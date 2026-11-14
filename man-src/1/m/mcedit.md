---
title: "mcedit(1)"
name: "mcedit"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mcedit/"
description: "mcedit – Internal file editor of GNU Midnight Commander."
---

<h2>NAME</h2>
<p> mcedit &#8211; Internal file editor of GNU Midnight Commander.</p>
<h2>USAGE</h2>
<p> <code>mcedit</code> [-bcCdfhstVx?] [+lineno] [file1] [file2] &#8230; </p>
<p> <code>mcedit</code> [-bcCdfhstVx?] file1:lineno[:] file2:lineno[:] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> mcedit is a link to <code>mc</code>, the main GNU Midnight Commander executable. Executing GNU Midnight Commander under this name runs the internal editor and opens files specified on the command line. The editor is based on the terminal version of <code>cooledit</code> &#8211; standalone editor for X Window System.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>+lineno</i></p>
<dd> Go to the line specified by number (do not put a space between the <i>+</i> sign and the number). Several line numbers are allowed but only the last one will be used, and it will be applied to the first file only.</p>
<dt><i>-b</i></p>
<dd> Force black and white display.</p>
<dt><i>-c</i></p>
<dd> Force ANSI color mode on terminals that don&#8217;t seem to have color support.</p>
<dt><i>-C &lt;keyword&gt;=&lt;fgcolor&gt;,&lt;bgcolor&gt;,&lt;attributes&gt;:&lt;keyword&gt;= &#8230;</i></p>
<dd> Specify a different color set. See the <code>Colors</code> section in <a href="/docs/linux/man/1-mc/">mc</a>(1) for more information.</p>
<dt><i>-d</i></p>
<dd> Disable mouse support.</p>
<dt><i>-f</i></p>
<dd> Display the compiled-in search path for GNU Midnight Commander data files.</p>
<dt><i>-t</i></p>
<dd> Force using termcap database instead of terminfo. This option is only applicable if GNU Midnight Commander was compiled with S-Lang library with terminfo support.</p>
<dt><i>-V</i></p>
<dd> Display the version of the program.</p>
<dt><i>-x</i></p>
<dd> Force xterm mode. Used when running on xterm-capable terminals (two screen modes, and able to send mouse escape sequences).</dl>
<h2>FEATURES</h2>
<p> The internal file editor is a full-featured windowed editor. It can edit several files at the same time. Maximim size of each file is 64 megabytes. It is possible to edit binary files. The features it presently supports are: block copy, move, delete, cut, paste; key for key undo; pull-down menus; file insertion; macro commands; regular expression search and replace; shift-arrow text highlighting (if supported by the terminal); insert-overwrite toggle; autoindent; tunable tab size; syntax highlighting for various file types; and an option to pipe text blocks through shell commands like indent and ispell. </p>
<p> Each file is opened in its own window in full-screen mode. Window control in mcedit is similar to the window control in other multi-window program: double click on window title maximizes the window to full-screen or restores window size and position; left-click on window title and mouse drag moves the window in editor area; left-click on low-right frame corner and mouse drag resizes the window. These actions can be made using &quot;Window&quot; menu.</p>
<h2>KEYS</h2>
<p> The editor is easy to use and can be used without learning. The pull-down menu is invoked by pressing F9. You can learn other keys from the menu and from the button bar labels. </p>
<p> In addition to that, Shift combined with arrows does text highlighting (if supported by the terminal): <code>Ctrl-Ins</code> copies to the file <code>~/.cache/mc/mcedit/mcedit.clip</code>, <code>Shift-Ins</code> pastes from <code>~/.cache/mc/mcedit/mcedit.clip</code>, <code>Shift-Del</code> cuts to <code>~/.cache/mc/mcedit/mcedit.clip</code>, and <code>Ctrl-Del</code> deletes highlighted text. Mouse highlighting also works on some terminals. To use the standard mouse support provided by your terminal, hold the Shift key. Please note that the mouse support in the terminal doesn&#8217;t share the clipboard with <code>mcedit</code>. </p>
<p> The completion key (usually <code>Meta-Tab</code> or <code>Escape Tab</code>) completes the word under the cursor using the words used in the file.</p>
<h2>MACRO</h2>
<p> To define a macro, press <code>Ctrl-R</code> and then type out the keys you want to be executed. Press <code>Ctrl-R</code> again when finished. The macro can be assigned to any key by pressing that key. The macro is executed when you press the assigned key. </p>
<p> The macro commands are stored in section <code>[editor]</code> it the file <code>~/.local/share/mc/mc.macros</code>. </p>
<p> External scripts (filters) can be assigned into the any hotkey by edit <code>mc.macros</code> like following: </p>
<pre>
[editor]
ctrl-W=ExecuteScript:25;
</pre>
<p> This means that ctrl-W hotkey initiates the <i>ExecuteScript(25)</i> action, then editor handler translates this into execution of <code>~/.local/share/mc/mcedit/macros.d/macro.25.sh</code> shell script. </p>
<p> External scripts are stored in <code>~/.local/share/mc/mcedit/macros.d/</code> directory and must be named as <code>macro.XXXX.sh</code> where <code>XXXX</code> is the number from 0 to 9999. See <code>Menu File Edit</code> for more detail about format of the script. </p>
<p> Following macro definition and directives can be used:</p>
<dl>
<dt><i>#silent</i></p>
<dd> If this directive is set, then script starts without interactive subshell.</p>
<dt><i>%c</i></p>
<dd> The cursor column position number.</p>
<dt><i>%i</i></p>
<dd> The indent of blank space, equal the cursor column.</p>
<dt><i>%y</i></p>
<dd> The syntax type of current file.</p>
<dt><i>%b</i></p>
<dd> The block file name.</p>
<dt><i>%f</i></p>
<dd> The current file name.</p>
<dt><i>%n</i></p>
<dd> Only the current file name without extension.</p>
<dt><i>%x</i></p>
<dd> The extension of current file name.</p>
<dt><i>%d</i></p>
<dd> The current directory name.</p>
<dt><i>%F</i></p>
<dd> The current file in the unselected panel.</p>
<dt><i>%D</i></p>
<dd> The directory name of the unselected panel.</p>
<dt><i>%t</i></p>
<dd> The currently tagged files.</p>
<dt><i>%T</i></p>
<dd> The tagged files in the unselected panel.</p>
<dt><i>%u</i> and <i>%U</i></p>
<dd> Similar to the <i>%t</i> and <i>%T</i> macros, but in addition the files are untagged. You can use this macro only once per menu file entry or extension file entry, because next time there will be no tagged files.</p>
<dt><i>%s</i> and <i>%S</i></p>
<dd> The selected files: The tagged files if there are any. Otherwise the current file.</dl>
<p> Feel free to edit this files, if you need. Here is a sample external script: </p>
<pre><code>
l comment selection
    TMPFILE =`mktemp ${MC_TMPDIR : - / tmp} / up.XXXXXX` || exit 1 echo #if 0 &gt; $TMPFILE
                                                                                        cat %
                                                                                    b &gt;&gt;
                                                                $TMPFILE
                                                                    echo #endif &gt;&gt;
                                                                $TMPFILE
                                                                    cat $TMPFILE &gt; % b
                                                                                               rm -
                                                                                       f $TMPFILE
</code></pre>
<p> If some keys don&#8217;t work, you can use <code>Learn Keys</code> in the <code>Options</code> menu.</p>
<h2>CODE NAVIGATION</h2>
<p> <code>mcedit</code> can be used for navigation through code with tags files created by etags or ctags commands. If there is no TAGS file code navigation will not work. For example, in case of exuberant-ctags for C language command will be: </p>
<p> ctags -e &#8211;language-force=C -R ./ </p>
<p> <code>Meta-Enter</code> shows list box to select item under cursor (cursor should stand at the end of the word). </p>
<p> <code>Meta-Minus</code> where minus is symbol &quot;-&quot; goes to previous function in navigation list (like browser&#8217;s Back button). </p>
<p> <code>Meta-Equal</code> where equal is symbol &quot;=&quot; goes to next function in navigation list (like browser&#8217;s Forward button). </p>
<h2>SYNTAX HIGHLIGHTING</h2>
<p> <code>mcedit</code> supports syntax highlighting. This means that keywords and contexts (like C comments, string constants, etc) are highlighted in different colors. The following section explains the format of the file <code>~/.config/mc/mcedit/Syntax</code>. If this file is missing, system-wide <code>/usr/share/mc/syntax/Syntax</code> is used. The file <code>~/.config/mc/mcedit/Syntax</code> is rescanned on opening of every new editor file. The file contains rules for highlighting, each of which is given on a separate line, and define which keywords will be highlighted with what color. </p>
<p> The file is divided into sections, each beginning with a line with the <code>file</code> command. The sections are normally put into separate files using the <code>include</code> command. </p>
<p> The <code>file</code> command has three arguments. The first argument is a regular expression that is applied to the file name to determine if the following section applies to the file. The second argument is the description of the file type. It is used in <code>cooledit</code>; future versions of <code>mcedit</code> may use it as well. The third optional argument is a regular expression to match the first line of text of the file. The rules in the following section apply if either the file name or the first line of text matches. </p>
<p> A section ends with the start of another section. Each section is divided into contexts, and each context contains rules. A context is a scope within the text that a particular set of rules belongs to. For instance, the text within a C style comment (i.e. between <code>/*</code> and <code>*/</code>) has its own color. This is a context, although it has no further rules inside it because there is probably nothing that we want highlighted within a C comment. </p>
<p> A trivial C programming section might look like this: </p>
<p>file .\*\.c C\sProgram\sFile (#include|/\\*)<br />
wholechars abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_<br />
#default colors<br />
define  comment   brown<br />
context default<br />
  keyword  whole  if       yellow<br />
  keyword  whole  else     yellow<br />
  keyword  whole  for      yellow<br />
  keyword  whole  while    yellow<br />
  keyword  whole  do       yellow<br />
  keyword  whole  switch   yellow<br />
  keyword  whole  case     yellow<br />
  keyword  whole  static   yellow<br />
  keyword  whole  extern   yellow<br />
  keyword         {        brightcyan<br />
  keyword         }        brightcyan<br />
  keyword         &#8216;*&#8217;      green<br />
#C comments<br />
context /\* \*/ comment<br />
#C preprocessor directives<br />
context linestart # 
 red<br />
  keyword  \
  brightred<br />
#C string constants<br />
context &#8221; &#8221; green<br />
  keyword  %d    brightgreen<br />
  keyword  %s    brightgreen<br />
  keyword  %c    brightgreen<br />
  keyword  \&#8221;   brightgreen</p>
<p> Each context starts with a line of the form: </p>
<p> <code>context</code> [<code>exclusive</code>] [<code>whole</code>|<code>wholeright</code>|<code>wholeleft</code>] [<code>linestart</code>] <i>delim</i> [<code>linestart</code>] <i>delim</i> [<i>foreground</i>] [<i>background</i>] [<i>attributes</i>] </p>
<p> The first context is an exception. It must start with the command </p>
<p> <code>context default</code> [<i>foreground</i>] [<i>background</i>] [<i>attributes</i>] </p>
<p> otherwise <code>mcedit</code> will report an error. The <code>linestart</code> option specifies that <i>delim</i> must start at the beginning of a line. The <code>whole</code> option tells that <i>delim</i> must be a whole word. To specify that a word must begin on the word boundary only on the left side, you can use the <code>wholeleft</code> option, and similarly a word that must end on the word boundary is specified by <code>wholeright</code>. </p>
<p> The set of characters that constitute a whole word can be changed at any point in the file with the <code>wholechars</code> command. The left and right set of characters can be set separately with </p>
<p> <code>wholechars</code> [<code>left</code>|<code>right</code>] <i>characters</i> </p>
<p> The <code>exclusive</code> option causes the text between the delimiters to be highlighted, but not the delimiters themselves. </p>
<p> Each rule is a line of the form: </p>
<p> <code>keyword</code> [<code>whole</code>|<code>wholeright</code>|<code>wholeleft</code>] [<code>linestart</code>] <i>string foreground</i> [<i>background</i>] [<i>attributes</i>] </p>
<p> Context or keyword strings are interpreted, so that you can include tabs and spaces with the sequences 	 and \s. Newlines and backslashes are specified with 
 and \ respectively. Since whitespace is used as a separator, it may not be used as is. Also, \* must be used to specify an asterisk. The * itself is a wildcard that matches any length of characters. For example, </p>
<pre>
  keyword         '*'      green
</pre>
<p> colors all C single character constants green. You also could use </p>
<pre>
  keyword         &quot;*&quot;      green
</pre>
<p> to color string constants, but the matched string would not be allowed to span across multiple newlines. The wildcard may be used within context delimiters as well, but you cannot have a wildcard as the last or first character. </p>
<p> Important to note is the line </p>
<pre>
  keyword  \
  brightgreen
</pre>
<p> This line defines a keyword containing the backslash and newline characters. Since the keywords are matched before the context delimiters, this keyword prevents the context from ending at the end of the lines that end in a backslash, thus allowing C preprocessor directive to continue across multiple lines. </p>
<p> The possible colors are: black, gray, red, brightred, green, brightgreen, brown, yellow, blue, brightblue, magenta, brightmagenta, cyan, brightcyan, lightgray and white. The special keyword &quot;default&quot; means the terminal&#8217;s default. Another special keyword &quot;base&quot; means mc&#8217;s main colors, it is useful as a placeholder if you want to specify attributes without modifying the background color. When 256 colors are available, they can be specified either as color16 to color255, or as rgb000 to rgb555 and gray0 to gray23. </p>
<p> If the syntax file is shared with <code>cooledit</code>, it is possible to specify different colors for <code>mcedit</code> and <code>cooledit</code> by separating them with a slash, e.g. </p>
<pre><code>
keyword #include red / Orange
</code></pre>
<p> <code>mcedit</code> uses the color before the slash. See <a href="/docs/linux/man/1-cooledit/">cooledit</a>(1) for supported <code>cooledit</code> colors. </p>
<p> Attributes can be any of bold, underline, reverse and blink, appended by a plus sign if more than one are desired. </p>
<p> Comments may be put on a separate line starting with the hash sign (#). </p>
<p> If you are describing case insensitive language you need to use <code>caseinsensitive</code> directive. It should be specified at the beginning of syntax file. </p>
<p> Because of the simplicity of the implementation, there are a few intricacies that will not be dealt with correctly but these are a minor irritation. On the whole, a broad spectrum of quite complicated situations are handled with these simple rules. It is a good idea to take a look at the syntax file to see some of the nifty tricks you can do with a little imagination. If you cannot get by with the rules I have coded, and you think you have a rule that would be useful, please email me with your request. However, do not ask for regular expression support, because this is flatly impossible. </p>
<p> A useful hint is to work with as much as possible with the things you can do rather than try to do things that this implementation cannot deal with. Also remember that the aim of syntax highlighting is to make programming less prone to error, not to make code look pretty. </p>
<p> The syntax highlighting can be toggled using Ctrl-s shortcut.</p>
<h2>COLORS</h2>
<p> The default colors may be changed by appending to the <code>MC_COLOR_TABLE</code> environment variable. Foreground and background colors pairs may be specified for example with: </p>
<pre>
MC_COLOR_TABLE=&quot;$MC_COLOR_TABLE:\
editnormal=lightgray,black:\
editbold=yellow,black:\
editmarked=black,cyan&quot;
</pre>
<h2>OPTIONS</h2>
<p> Most options can be set from Options dialog box. See the <code>Options</code> menu. The following options are defined in <code>~/.config/mc/ini</code> and have obvious counterparts in the dialog box. You can modify them to change the editor behavior, by editing the file. Unless specified, a 1 sets the option to on, and a 0 sets it to off, as usual.</p>
<dl>
<dt><i>use_internal_edit</i></p>
<dd> This option is ignored when invoking <code>mcedit</code>.</p>
<dt><i>editor_tab_spacing</i></p>
<dd> Interpret the tab character as being of this length. Default is 8. You should avoid using other than 8 since most other editors and text viewers assume a tab spacing of 8. Use <code>editor_fake_half_tabs</code> to simulate a smaller tab spacing.</p>
<dt><i>editor_fill_tabs_with_spaces</i></p>
<dd> Never insert a tab character. Rather insert spaces (ascii 32) to fill to the desired tab size.</p>
<dt><i>editor_return_does_auto_indent</i></p>
<dd> Pressing return will tab across to match the indentation of the first line above that has text on it.</p>
<dt><i>editor_backspace_through_tabs</i></p>
<dd> Make a single backspace delete all the space to the left margin if there is no text between the cursor and the left margin.</p>
<dt><i>editor_fake_half_tabs</i></p>
<dd> This will emulate a half tab for those who want to program with a tab spacing of 4, but do not want the tab size changed from 8 (so that the code will be formatted the same when displayed by other programs). When editing between text and the left margin, moving and tabbing will be as though a tab space were 4, while actually using spaces and normal tabs for an optimal fill. When editing anywhere else, a normal tab is inserted.</p>
<dt><i>editor_option_save_mode</i></p>
<dd> Possible values 0, 1 and 2. The save mode (see the options menu also) allows you to change the method of saving a file. Quick save (0) saves the file immediately, truncating the disk file to zero length (i.e. erasing it) and then writing the editor contents to the file. This method is fast, but dangerous, since a system error during a file save will leave the file only partially written, possibly rendering the data irretrievable. When saving, the safe save (1) option enables creation of a temporary file into which the file contents are first written. In the event of a problem, the original file is untouched. When the temporary file is successfully written, it is renamed to the name of the original file, thus replacing it. The safest method is create backups (2): a backup file is created before any changes are made. You can specify your own backup file extension in the dialog. Note that saving twice will replace your backup as well as your original file.</p>
<dt><i>editor_word_wrap_line_length</i></p>
<dd> Line length to wrap at. Default is 72.</p>
<dt><i>editor_backup_extension</i></p>
<dd> Symbol to add to name of backup files. Default is &quot;~&quot;.</p>
<dt><i>editor_line_state</i></p>
<dd> Show state line of editor. Currently it shows current line number (in the future it might show things like folding, breakpoints, etc.). M-n toggles this option.</p>
<dt><i>editor_visible_spaces</i></p>
<dd> Toggle &quot;show visible trailing spaces&quot;. If editor_visible_spaces=1, they are shown as &#8216;.&#8217;</p>
<dt><i>editor_visible_tabs</i></p>
<dd> Toggle &quot;show visible tabs&quot;. If editor_visible_tabs=1, tabs are shown as &#8216;&lt;&#8212;-&gt;&#8217;</p>
<dt><i>editor_persistent_selections</i></p>
<dd> Do not remove block selection after cursor movement.</p>
<dt><i>editor_cursor_beyond_eol</i></p>
<dd> Allow moving cursor beyond the end of line.</p>
<dt><i>editor_cursor_after_inserted_block</i></p>
<dd> Allow moving cursor after inserted block.</p>
<dt><i>editor_syntax_highlighting</i></p>
<dd> enable syntax highlighting.</p>
<dt><i>editor_edit_confirm_save</i></p>
<dd> Show confirmation dialog on save.</p>
<dt><i>editor_option_typewriter_wrap</i></p>
<dd> to be described</p>
<dt><i>editor_option_auto_para_formatting</i></p>
<dd> to be described</p>
<dt><i>editor_option_save_position</i></p>
<dd> save file position on exit.</p>
<dt><i>source_codepage</i></p>
<dd> symbol representation of codepage name for file (i.e. CP1251, ~ &#8211; default).</p>
<dt><i>editor_group_undo</i></p>
<dd> do UNDO for several of the same type of action (inserting/overwriting, deleting, navigating, typing)</p>
<dt><i>editor_wordcompletion_collect_entire_file</i></p>
<dd> Search autocomplete candidates in entire of file or just from begin of file to cursor position (0)</p>
<dt><i>spell_language</i></p>
<dd> Spelling language (en, en-variant_0, ru, etc) installed with aspell package (a full list can be get using &#8216;aspell&#8217; utility). Use <code>spell_language = NONE</code> to disable aspell support. Default value is &#8216;en&#8217;. Option must located in the [Misc] section.</dl>
<h2>MISCELLANEOUS</h2>
<p> You can use scanf search and replace to search and replace a C format string. First take a look at the <code>sscanf</code> and <code>sprintf</code> man pages to see what a format string is and how it works. Here&#8217;s an example: suppose that you want to replace all occurrences of an open bracket, three comma separated numbers, and a close bracket, with the word <i>apples</i>, the third number, the word <i>oranges</i> and then the second number. You would fill in the Replace dialog box as follows: </p>
<pre>
<code>Enter search string</code>
(%d,%d,%d)
<code>Enter replace string</code>
apples %d oranges %d
<code>Enter replacement argument order</code>
3,2
</pre>
<p> The last line specifies that the third and then the second number are to be used in place of the first and second. </p>
<p> It is advisable to use this feature with Prompt On Replace on, because a match is thought to be found whenever the number of arguments found matches the number given, which is not always a real match. Scanf also treats whitespace as being elastic. Note that the scanf format %[ is very useful for scanning strings, and whitespace. </p>
<p> The editor also displays non-us characters (160+). When editing binary files, you should set <code>display bits</code> to 7 bits in the Midnight Commander options menu to keep the spacing clean.</p>
<h2>FILES</h2>
<p> <i>/usr/share/mc/mc.hlp</i></p>
<dl>
<dt>
<dd> The help file for the program.</dl>
<p> <i>/usr/share/mc/mc.ini</i></p>
<dl>
<dt>
<dd> The default system-wide setup for GNU Midnight Commander, used only if the user&#8217;s own ~/.config/mc/ini file is missing.</dl>
<p> <i>/usr/share/mc/mc.lib</i></p>
<dl>
<dt>
<dd> Global settings for the Midnight Commander. Settings in this file affect all users, whether they have ~/.config/mc/ini or not.</dl>
<p> <i>/usr/share/mc/syntax/*</i></p>
<dl>
<dt>
<dd> The default system-wide syntax files for mcedit, used only if the corresponding user&#8217;s own ~/.local/share/mc/mcedit/ file is missing.</dl>
<p> <i>~/.config/mc/ini</i></p>
<dl>
<dt>
<dd> User&#8217;s own setup. If this file is present then the setup is loaded from here instead of the system-wide setup file.</dl>
<p> <i>~/.local/share/mc/mcedit/</i></p>
<dl>
<dt>
<dd> User&#8217;s own directory where block commands are processed and saved and user&#8217;s own syntax files are located.</dl>
<h2>LICENSE</h2>
<p> This program is distributed under the terms of the GNU General Public License as published by the Free Software Foundation. See the built-in help of the Midnight Commander for details on the License and the lack of warranty.</p>
<h2>AVAILABILITY</h2>
<p> The latest version of this program can be found at <a rel="nofollow" href="http://midnight-commander.org/.">http://midnight-commander.org/.</a></p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cooledit/">cooledit</a>(1), <a href="/docs/linux/man/1-mc/">mc</a>(1), <a href="/docs/linux/man/1-gpm/">gpm</a>(1), <a href="/docs/linux/man/1-terminfo/">terminfo</a>(1), <a href="/docs/linux/man/3-scanf/">scanf</a>(3).</p>
<h2>AUTHORS</h2>
<p> Paul Sheer (psheer [at] obsidian.co.za) is the original author of the Midnight Commander&#8217;s internal editor.</p>
<h2>BUGS</h2>
<p> Bugs should be reported to mc-devel [at] gnome.org </p>
<h2>Index</h2>
