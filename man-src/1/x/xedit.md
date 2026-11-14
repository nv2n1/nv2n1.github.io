---
title: "xedit(1)"
name: "xedit"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xedit/"
description: "xedit – simple text editor for X"
---

<h2 class="name">NAME</h2>
<p> xedit &#8211; simple text editor for X </p>
<h2>SYNTAX</h2>
<p> <code>xedit</code> [ <i>-toolkitoption</i> &#8230; ] [ <i>filename</i> &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Xedit</i> provides a window consisting of the following four areas:</p>
<dl>
<dt>Commands Section</p>
<dd> A set of commands that allow you to exit <i>xedit</i>, save the file, or load a new file into the edit window.</p>
<dt>Message Window</p>
<dd> Displays <i>xedit</i> messages. In addition, this window can be also used as a scratch pad.</p>
<dt>Filename Display</p>
<dd> Displays the name of the file currently being edited, and whether this file is <i>Read-Write</i> or <i>Read Only</i>.</p>
<dt>Edit Window</p>
<dd> Displays the text of the file that you are editing or creating.</dl>
<h2>OPTIONS</h2>
<p> <i>Xedit</i> accepts all of the standard X Toolkit command line options (see <i><a href="/docs/linux/man/7-x/">X</a></i>(7)). The order of the command line options is not important.</p>
<dl>
<dt><i>filename</i></p>
<dd> Specifies the file(s) that are to be loaded during start-up. This is the file which will be edited. If a file is not specified, <i>xedit</i> lets you load files or create new files after it has started up.</dl>
<h2>EDITING</h2>
<p> The Athena Text widget is used for the three sections of this application that allow text input. The characters typed will go to the Text widget that has the input focus, or the Text widget that the pointer cursor is currently over. </p>
<p> The following keystroke combinations are defined: </p>
<table>
<tr VALIGN=top>
<td>Ctrl-a</td>
<td>Beginning Of Line
</td>
</tr>
<tr VALIGN=top>
<td>Meta-b</td>
<td>Backward Word
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-b</td>
<td>Backward Character
</td>
</tr>
<tr VALIGN=top>
<td>Meta-f</td>
<td>Forward Word
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-d</td>
<td>Delete Next Character
</td>
</tr>
<tr VALIGN=top>
<td>Meta-i</td>
<td>Insert File
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-e</td>
<td>End Of Line
</td>
</tr>
<tr VALIGN=top>
<td>Meta-k</td>
<td>Kill To End Of Paragraph
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-f</td>
<td>Forward Character
</td>
</tr>
<tr VALIGN=top>
<td>Meta-q</td>
<td>Form Paragraph
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-g</td>
<td>Keyboard Reset
</td>
</tr>
<tr VALIGN=top>
<td>Meta-v</td>
<td>Previous Page
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-h</td>
<td>Delete Previous Character
</td>
</tr>
<tr VALIGN=top>
<td>Meta-y</td>
<td>Insert Current Selection
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-j</td>
<td>Newline And Indent
</td>
</tr>
<tr VALIGN=top>
<td>Meta-z</td>
<td>Scroll One Line Down
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-k</td>
<td>Kill To End Of Line
</td>
</tr>
<tr VALIGN=top>
<td>Meta-d</td>
<td>Delete Next Word
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-l</td>
<td>Redraw Display
</td>
</tr>
<tr VALIGN=top>
<td>Meta-D</td>
<td>Kill Word
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-m</td>
<td>Newline
</td>
</tr>
<tr VALIGN=top>
<td>Meta-h</td>
<td>Delete Previous Word
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-n</td>
<td>Next Line
</td>
</tr>
<tr VALIGN=top>
<td>Meta-H</td>
<td>Backward Kill Word
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-o</td>
<td>Newline And Backup
</td>
</tr>
<tr VALIGN=top>
<td>Meta-&lt;</td>
<td>Beginning Of File
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-p</td>
<td>Previous Line
</td>
</tr>
<tr VALIGN=top>
<td>Meta-&gt;</td>
<td>End Of File
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-r</td>
<td>Search/Replace Backward
</td>
</tr>
<tr VALIGN=top>
<td>Meta-]</td>
<td>Forward Paragraph
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-s</td>
<td>Search/Replace Forward
</td>
</tr>
<tr VALIGN=top>
<td>Meta-[</td>
<td>Backward Paragraph
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-t</td>
<td>Transpose Characters
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-u [<i>number</i>]</td>
<td>Multiply by 4 or <i>number</i>
</td>
</tr>
<tr VALIGN=top>
<td>Meta-Delete</td>
<td>Delete Previous Word
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-v</td>
<td>Next Page
</td>
</tr>
<tr VALIGN=top>
<td>Meta-Shift Delete</td>
<td>Kill Previous Word
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-w</td>
<td>Kill Selection
</td>
</tr>
<tr VALIGN=top>
<td>Meta-Backspace</td>
<td>Delete Previous Word
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-y</td>
<td>Unkill
</td>
</tr>
<tr VALIGN=top>
<td>Meta-Shift Backspace</td>
<td>Kill Previous Word
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-z</td>
<td>Scroll One Line Up
</td>
</tr>
<tr VALIGN=top>
<td>Meta-z</td>
<td>Scroll One Line Down
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-_</td>
<td>Undo
</td>
</tr>
<tr VALIGN=top>
<td>Escape</td>
<td>Line Edit Mode
</td>
</tr>
</table>
<p> In addition, the pointer may be used to cut and paste text: </p>
<table>
<tr VALIGN=top>
<td>Button 1 Down</td>
<td>Start Selection
</td>
</tr>
<tr VALIGN=top>
<td>Button 1 Motion</td>
<td>Adjust Selection
</td>
</tr>
<tr VALIGN=top>
<td>Button 1 Up</td>
<td>End Selection (cut)
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Button 2 Down</td>
<td>Insert Current Selection (paste)
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Button 3 Down</td>
<td>Extend Current Selection
</td>
</tr>
<tr VALIGN=top>
<td>Button 3 Motion</td>
<td>Adjust Selection
</td>
</tr>
<tr VALIGN=top>
<td>Button 3 Up</td>
<td>End Selection (cut)
</td>
</tr>
</table>
<h2>LINE EDIT MODE</h2>
<p> <i>Line edit mode</i> enables several shortcut commands for searching and replacing text in a xedit buffer. <i>Line edit mode</i> commands have the format: </p>
<pre><code>
[line - number[, line - number]] command[parameters]
</code></pre>
<p> <i>Line number</i> may be specified as:</p>
<dl>
<dt>.</p>
<dd> The current text line.</p>
<dt>$</p>
<dd> The last line of the file.</p>
<dt>number</p>
<dd> The literal line <i>number</i>.</p>
<dt>&#8211; or ^</p>
<dd> The previous line. Equivalent to <i>-1</i>.</p>
<dt>-number or ^number</p>
<dd> The current line minus <i>number</i>.</p>
<dt>+</p>
<dd> The next line. Equivalent to <i>+1</i>.</p>
<dt>+number</p>
<dd> The current line plus <i>number</i>.</p>
<dt>, or %</p>
<dd> From the first to the last line. Equivalent to <i>1,$</i>.</p>
<dt>;</p>
<dd> From the current to the last line. Equivalent to <i>.,$</i>. </p>
</dl>
<p> <i>Command</i> may be specified as:</p>
<dl>
<dt>s</p>
<dd> Substitute text in the specified lines.</p>
<dt>/re/</p>
<dd> Search forward for the regular expression pattern <i>re</i>.</p>
<dt>?re?</p>
<dd> Search backward for the regular expression pattern <i>re</i>. </p>
</dl>
<p> <i>Parameters</i> may be specified as:</p>
<dl>
<dt>/re/</p>
<dd> Works as a parameter to <i>i</i> or as a command.</p>
<dt>/re/text/</p>
<dd> Search forward for <i>re</i> and substitute by <i>text</i>. </p>
</dl>
<p> <i>Options</i> may follow or be parameters, known values are:</p>
<dl>
<dt>i</p>
<dd> Case insensitive search.</p>
<dt>g</p>
<dd> <i>Global</i> match when replacing text. Unless specified, only the nth, that defaults to 1, match will be replaced.</p>
<dt>c</p>
<dd> <i>Confirm</i> before replacing text.</p>
<dt>number</p>
<dd> Replace only the occurrence referenced by <i>number</i>.</dl>
<p> Commands accept some variations, examples: </p>
<pre>
        /pattern/i
        i/pattern/
        i/pattern
</pre>
<p> Search forward for <i>pattern</i>. </p>
<pre>
        ,sc/pattern/text
        ,sc/pattern/text/
        ,s/pattern/text/c
</pre>
<p> Search the entire buffer and ask confirmation to replace <i>pattern</i> with <i>text</i>. </p>
<pre>
        ,s/pattern/text/number
</pre>
<p> Replace the match <i>number</i> in the text line. If not specified, defaults to the first occurrence. </p>
<p> When searching for text, type &lt;Return&gt; to go to the next match. When interactively replacing text, type <i>y</i> or <i>Y</i> to accept the change, and <i>n</i> or <i>N</i> to ignore it and go to the next match. </p>
<h2>COMMANDS</h2>
<dl>
<dt>Quit</p>
<dd> Quits the current editing session. If any changes have not been saved, <i>xedit</i> displays a warning message, allowing the user to save them.</p>
<dt>Save</p>
<dd> If file backups are enabled (see RESOURCES, below) <i>xedit</i> stores a copy of the original, unedited file in &lt;prefix&gt;<i>file</i>&lt;suffix&gt;, then overwrites the <i>file</i> with the contents of the edit window. The filename is retrieved from the Text widget directly to the right of the <i>Load</i> button.</p>
<dt>Load</p>
<dd> Loads the file named in the text widget immediately to the right of the this button and displays it in the Edit window.</dl>
<h2>RESOURCES</h2>
<p> For <i>xedit</i> the available resources are:</p>
<dl>
<dt><code>tagsName (</code>Class<code> TagsName)</code></p>
<dd> Specifies the name of the tags file to search when loading a new file. Default value is <i>tags</i>.</p>
<dt><code>loadTags (</code>Class<code> LoadTags)</code></p>
<dd> Boolean value to enable or disabling searching for tags files. Default is <i>True</i>.</p>
<dt><code>enableBackups (</code>Class<code> EnableBackups)</code></p>
<dd> Specifies that, when edits made to an existing file are saved, <i>xedit</i> is to copy the original version of that file to &lt;prefix&gt;<i>file</i>&lt;suffix&gt; before it saves the changes. The default value for this resource is &#8220;on,&#8221; stating that backups should be created.</p>
<dt><code>backupNamePrefix (</code>Class<code> BackupNamePrefix)</code></p>
<dd> Specifies a string that is to be prepended to the backup filename. The default is that no string shall be prepended.</p>
<dt><code>backupNameSuffix (</code>Class<code> BackupNameSuffix)</code></p>
<dd> Specifies a string that is to be appended to the backup filename. The default is to use &#8220;~&#8221; as the suffix.</p>
<dt><code>positionFormat (</code>Class<code> Format)</code></p>
<dd> Specifies a format string used to display the cursor position. This string uses <a href="/docs/linux/man/3-printf/">printf</a>(3) like notation, where <code>%l</code> prints the line number, <code>%c</code> prints the column number, <code>%p</code> prints the insert position offset, and <code>%s</code> prints the current file size. It is also allowed to specify field sizes, with the notation <code>%-?[0-9]+</code> . The default format string is &#8220;L%l&#8221;, which shows the character &#8220;L&#8221; followed by the line number.</p>
<dt><code>hints (</code>Class<code> Hints)</code></p>
<dd> Specifies a list of strings, separated by new lines, that will be displayed in the bc_label window.</p>
<dt><code>hintsInterval (</code>Class <code>Interval)</code></p>
<dd> Specifies the interval in seconds, which the hint string in the bc_label window will be changed.</p>
<dt><code>changedBitmap (</code>Class <code>Bitmap)</code></p>
<dd> Specifies the name of the Bitmap that will be displayed in the fileMenu, when the file being edited is changed.</p>
<dt><code>autoReplace (</code>Class <code>Replace)</code></p>
<dd> This resource is useful to automatically correct common misspelling errors, but can also be used to create simple macros. The format is <i>{non-blanks}{blanks}[{string}]</i>. Fields are separated by newlines. Example of use: </p>
<pre>
nto       not
\
/macro some long string with \
 newlines \

</pre>
<p> Will automatically replace the word <i>nto</i> by <i>not</i>, and <i>/macro</i> by <i>some long string with<br />
&nbsp;newlines </i> when you type that words.</p>
<dt><code>ispell.dictionaries (</code>Class <code>ispell.Dictionary)</code></p>
<dd> Specifies a list of dictionary names, separated by spaces, available to the ispell program. The default value is <i>&quot;american americamed+ english&quot;</i>.</p>
<dt><code>ispell.dictionary (</code>Class <code>ispell.Dictionary)</code></p>
<dd> Specifies the default dictionary to use.</p>
<dt><code>ispell*&lt;DICTIONARY&gt;.wordChars (</code>Class <code>ispell*Chars)</code></p>
<dd> Specifies a set of characters that can be part of a legal word. The <i>&lt;DICTIONARY&gt;</i> field is one of the dictionaries specified in the <i>dictionaries</i> resource.</p>
<dt><code>ispell.ispellCommand (</code>Class <code>ispell.CommandLine)</code></p>
<dd> The path to the ispell program, and possibly, additional arguments. You don&#8217;t need to specify the &#8220;-w&#8221; option, neither the &#8220;-a&#8221; option. Refer to the <i><a href="/docs/linux/man/1-ispell/">ispell</a></i>(1) manpage for more information on ispell options.</p>
<dt><code>ispell.formatting (</code>Class ispell.TextFormat)</p>
<dd> Specifies which text formatting to use while spell checking the file. The available formats are <i>text</i> and <i>html</i>.</p>
<dt><code>ispell*text.skipLines (</code>Class <code>ispell*text.Skip)</code></p>
<dd> Lines starting with one of the characters in this string will not be spell checked. This resource is only used in <i>text</i> mode.</p>
<dt><code>ispell.terseMode (</code>Class <code>ispell.Terse)</code></p>
<dd> When enabled, runs ispell in terse mode, not asking user interaction for words generated through compound formation (when using the ispell &#8220;-C&#8221; option), or words generated through affix removal. The default value is False.</p>
<dt><code>ispell.lookCommand (</code>Class <code>ispell.CommandLine)</code></p>
<dd> The path to the program to search for alternate words, and possibly, additional arguments. The default program used is <i>/usr/bin/egrep</i>.</p>
<dt><code>ispell.wordsFile (</code>Class <code>ispell.Words)</code></p>
<dd> The path to the file[s] to search for alternate words. The default file is <i>/usr/share/dict/words</i>.</p>
<dt><code>ispell.guessLabel (</code>Class <code>ispell.Status)</code></p>
<dd> String displayed in the ispell status bar when ispell returns a guess list of one or more words. The default value is <i>Guess</i>.</p>
<dt><code>ispell.missLabel (</code>Class <code>ispell.Status)</code></p>
<dd> String displayed in the ispell status bar when ispell returns a list of one or more words to match a misspelled one. The default value is <i>Miss</i>.</p>
<dt><code>ispell.rootLabel (</code>Class <code>ispell.Status)</code></p>
<dd> String displayed in the ispell status bar when the word is not in the dictionary, but it can be formed through a root one. The default value is <i>Root:</i>, and is followed by a space and the root word.</p>
<dt><code>ispell.noneLabel (</code>Class <code>ispell.Status)</code></p>
<dd> String displayed in the ispell status bar when there is no near misses. The default value is <i>None</i>.</p>
<dt><code>ispell.compoundLabel (</code>Class <code>ispell.Status)</code></p>
<dd> String displayed in the ispell status bar when the word being checked is formed by concatenation of two words. The default value is <i>Compound</i>.</p>
<dt><code>ispell.okLabel (</code>Class <code>ispell.Status)</code></p>
<dd> String displayed in the ispell status bar when the checked word is in the dictionary. This string is only displayed when using the <i>check</i> button in the xedit ispell interface. The default value is <i>Ok</i>.</p>
<dt><code>ispell.eofLabel (</code>Class <code>ispell.Status)</code></p>
<dd> The string displayed in the ispell status bar when the end of the file is reached. The default value is <i>End Of File</i>.</p>
<dt><code>ispell.repeatLabel (</code>Class <code>ispell.Status)</code></p>
<dd> The string displayed in the ispell status bar when two identical words are found together in the file. The default value is <i>Repeat</i>.</p>
<dt><code>ispell.lookLabel (</code>Class <code>ispell.Status)</code></p>
<dd> The string displayed in the ispell status bar after displaying the results of the <i>Look</i> command. If no results are found, the value of the <i>ispell.noneLabel</i> resource is shown.</p>
<dt><code>ispell.workingLabel (</code>Class <code>ispell.Status)</code></p>
<dd> The string displayed in the ispell status bar while xedit is communicating with ispell. The default value is <i>&#8230;</i>.</dl>
<h2>WIDGETS</h2>
<p> In order to specify resources, it is useful to know the hierarchy of the widgets which compose <i>xedit</i>. In the notation below, indentation indicates hierarchical structure. The widget class name is given first, followed by the widget instance name. </p>
<pre>
Xedit  xedit
        Paned  paned
                Paned  buttons
                        Command  quit
                        Command  save
                        Command  load
                        Text     filename
                Label  bc_label
                Text   messageWindow
                Label  labelWindow
                Text   editWindow
</pre>
<h2>ENVIRONMENT</h2>
<dl>
<dt><i>DISPLAY</i></p>
<dd> to get the default host and display number.</p>
<dt><i>XENVIRONMENT</i></p>
<dd> to get the name of a resource file that overrides the global resources stored in the RESOURCE_MANAGER property.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/X11/app-defaults/Xedit</i></p>
<dd> specifies required resources</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-x/">X</a></i>(7), <i><a href="/docs/linux/man/1-xrdb/">xrdb</a></i>(1), <i>Athena Widget Set</i></p>
<h2>RESTRICTIONS</h2>
<p> Xedit is not a replacement to Emacs.</p>
<h2>COPYRIGHT</h2>
<p> Copyright 1988, Digital Equipment Corporation.<br />
 Copyright 1989, X Consortium<br />
 Copyright 1998, The XFree86 Project<br />
 See <i><a href="/docs/linux/man/7-x/">X</a></i>(7) for a full statement of rights and permissions.</p>
<h2>AUTHORS</h2>
<p> Chris D. Peterson, MIT X Consortium<br />
 Paulo Cesar Pereira de Andrade, The XFree86 Project </p>
<h2>Index</h2>
