---
title: "readline(3)"
name: "readline"
section: "3"
letter: "r"
url: "/docs/linux/man/3-readline/"
description: "readline – get a line from a user with editing"
---
<p>readline &#8211; get a line from a user with editing </p>
<h2>SYNOPSIS</h2>
<pre><code>
 #include &lt;stdio.h&gt;
#include &lt;readline/readline.h&gt;
#include &lt;readline/history.h&gt;
 </code></pre>
<pre><code>
 char * 


 readline  ( const char *prompt );
</code></pre>
<h2>COPYRIGHT</h2>
<p> Readline is Copyright (C) 1989-2011 Free Software Foundation, Inc.  </p>
<h2>DESCRIPTION</h2>
<p> <code>readline</code> will read a line from the terminal and return it, using <code>prompt</code> as a prompt. If <code>prompt</code> is <code>NULL</code> or the empty string, no prompt is issued. The line returned is allocated with <i><a href="/docs/linux/man/3-malloc/">malloc</a></i>(3); the caller must free it when finished. The line returned has the final newline removed, so only the text of the line remains. </p>
<p> <code>readline</code> offers editing capabilities while the user is entering the line. By default, the line editing commands are similar to those of emacs. A vi-style line editing interface is also available. </p>
<p>This manual page describes only the most basic use of <code>readline</code>. Much more functionality is available; see <i>The GNU Readline Library</i> and <i>The GNU History Library</i> for additional information.  </p>
<h2>RETURN VALUE</h2>
<p> <code>readline</code> returns the text of the line read. A blank line returns the empty string. If <code>EOF</code> is encountered while reading a line, and the line is empty, <code>NULL</code> is returned. If an <code>EOF</code> is read with a non-empty line, it is treated as a newline.  </p>
<h2>NOTATION</h2>
<p>An Emacs-style notation is used to denote keystrokes. Control keys are denoted by C-<i>key</i>, e.g., C-n means Control-N. Similarly, <i>meta</i> keys are denoted by M-<i>key</i>, so M-x means Meta-X. (On keyboards without a <i>meta</i> key, M-<i>x</i> means ESC <i>x</i>, i.e., press the Escape key then the <i>x</i> key. This makes ESC the <i>meta prefix</i>. The combination M-C-<i>x</i> means ESC-Control-<i>x</i>, or press the Escape key then hold the Control key while pressing the <i>x</i> key.) </p>
<p>Readline commands may be given numeric <i>arguments</i>, which normally act as a repeat count. Sometimes, however, it is the sign of the argument that is significant. Passing a negative argument to a command that acts in the forward direction (e.g., <code>kill-line</code>) causes that command to act in a backward direction. Commands whose behavior with arguments deviates from this are noted. </p>
<p>When a command is described as <i>killing</i> text, the text deleted is saved for possible future retrieval (<i>yanking</i>). The killed text is saved in a <i>kill ring</i>. Consecutive kills cause the text to be accumulated into one unit, which can be yanked all at once. Commands which do not kill text separate the chunks of text on the kill ring.  </p>
<h2>INITIALIZATION FILE</h2>
<p>Readline is customized by putting commands in an initialization file (the <i>inputrc</i> file). The name of this file is taken from the value of the <code>INPUTRC</code> environment variable. If that variable is unset, the default is <i>~/.inputrc</i>. If that file does not exist or cannot be read, the ultimate default is <i>/etc/inputrc</i>. When a program which uses the readline library starts up, the init file is read, and the key bindings and variables are set. There are only a few basic constructs allowed in the readline init file. Blank lines are ignored. Lines beginning with a <code>#</code> are comments. Lines beginning with a <code>$</code> indicate conditional constructs. Other lines denote key bindings and variable settings. Each program using this library may add its own commands and bindings. </p>
<p>For example, placing </p>
<dl>
<dd> <p>M-Control-u: universal-argument </p>
 </dd></dl>
<p> or </p>
<dl>
<dd> <p> C-Meta-u: universal-argument </p>
 </dd></dl>
<p>into the <i>inputrc</i> would make M-C-u execute the readline command <i>universal-argument</i>. </p>
<p>The following symbolic character names are recognized while processing key bindings: <i>DEL</i>, <i>ESC</i>, <i>ESCAPE</i>, <i>LFD</i>, <i>NEWLINE</i>, <i>RET</i>, <i>RETURN</i>, <i>RUBOUT</i>, <i>SPACE</i>, <i>SPC</i>, and <i>TAB</i>. </p>
<p>In addition to command names, readline allows keys to be bound to a string that is inserted when the key is pressed (a <i>macro</i>). </p>
<h3>Key Bindings</h3>
<p>The syntax for controlling key bindings in the <i>inputrc</i> file is simple. All that is required is the name of the command or the text of a macro and a key sequence to which it should be bound. The name may be specified in one of two ways: as a symbolic key name, possibly with <i>Meta-</i> or <i>Control-</i> prefixes, or as a key sequence. The name and key sequence are separated by a colon. There can be no whitespace between the name and the colon. </p>
<p>When using the form <code>keyname</code>:<i>function-name</i> or <i>macro</i>, <i>keyname</i> is the name of a key spelled out in English. For example: </p>
<dl>
<dd> <p> Control-u: universal-argument <br />
 Meta-Rubout: backward-kill-word <br />
 Control-o: &quot;&gt; output&quot; </p>
 </dd></dl>
<p>In the above example, <i>C-u</i> is bound to the function <code>universal-argument</code>, <i>M-DEL</i> is bound to the function <code>backward-kill-word</code>, and <i>C-o</i> is bound to run the macro expressed on the right hand side (that is, to insert the text ``&gt; output&#8217;&#8216; into the line). </p>
<p>In the second form, <code>&quot;keyseq&quot;</code>:<i>function-name</i> or <i>macro</i>, <code>keyseq</code> differs from <code>keyname</code> above in that strings denoting an entire key sequence may be specified by placing the sequence within double quotes. Some GNU Emacs style key escapes can be used, as in the following example, but the symbolic character names are not recognized. </p>
<dl>
<dd> <p> &quot;\C-u&quot;: universal-argument <br />
 &quot;\C-x\C-r&quot;: re-read-init-file <br />
 &quot;\e[11~&quot;: &quot;Function Key 1&quot; </p>
 </dd></dl>
<p>In this example, <i>C-u</i> is again bound to the function <code>universal-argument</code>. <i>C-x C-r</i> is bound to the function <code>re-read-init-file</code>, and <i>ESC [ 1 1 ~</i> is bound to insert the text ``Function Key 1&#8217;&#8216;. </p>
<p>The full set of GNU Emacs style escape sequences available when specifying key sequences is </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>\C-</code></dt>
<dd> <p> control prefix </p>
 </dd>
<dt><code>\M-</code></dt>
<dd> <p> meta prefix </p>
 </dd>
<dt><code>\e</code></dt>
<dd> <p> an escape character </p>
 </dd>
<dt><code>\\</code></dt>
<dd> <p> backslash </p>
 </dd>
<dt><code>\</code></dt>
<dd> <p> literal &quot;, a double quote </p>
 </dd>
<dt><code>\&#8216;</code></dt>
<dd> <p> literal &#8216;, a single quote </p>
 </dd></dl>
</dl>
<p>In addition to the GNU Emacs style escape sequences, a second set of backslash escapes is available: </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>\a</code></dt>
<dd> <p> alert (bell) </p>
 </dd>
<dt><code>\b</code></dt>
<dd> <p> backspace </p>
 </dd>
<dt><code>\d</code></dt>
<dd> <p> delete </p>
 </dd>
<dt><code>\f</code></dt>
<dd> <p> form feed </p>
 </dd>
<dt><code>\n</code></dt>
<dd> <p> newline </p>
 </dd>
<dt><code>\r</code></dt>
<dd> <p> carriage return </p>
 </dd>
<dt><code>\t</code></dt>
<dd> <p> horizontal tab </p>
 </dd>
<dt><code>\v</code></dt>
<dd> <p> vertical tab </p>
 </dd>
<dt><code>\</code><i>nnn</i></dt>
<dd> <p> the eight-bit character whose value is the octal value <i>nnn</i> (one to three digits) </p>
 </dd>
<dt><code>\x</code><i>HH</i></dt>
<dd> <p> the eight-bit character whose value is the hexadecimal value <i>HH</i> (one or two hex digits) </p>
 </dd></dl>
</dl>
<p>When entering the text of a macro, single or double quotes should be used to indicate a macro definition. Unquoted text is assumed to be a function name. In the macro body, the backslash escapes described above are expanded. Backslash will quote any other character in the macro text, including &quot; and &#8216;. </p>
<p> <code>Bash</code> allows the current readline key bindings to be displayed or modified with the <code>bind</code> builtin command. The editing mode may be switched during interactive use by using the <code>-o</code> option to the <code>set</code> builtin command. Other programs using this library provide similar mechanisms. The <i>inputrc</i> file may be edited and re-read if a program does not provide any other means to incorporate new bindings.  </p>
<h3>Variables</h3>
<p>Readline has variables that can be used to further customize its behavior. A variable may be set in the <i>inputrc</i> file with a statement of the form </p>
<dl>
<dd> <p> <code>set</code> <i>variable-name</i> <i>value</i> </p>
 </dd></dl>
<p>Except where noted, readline variables can take the values <code>On</code> or <code>Off</code> (without regard to case). Unrecognized variable names are ignored. When a variable value is read, empty or null values, &quot;on&quot; (case-insensitive), and &quot;1&quot; are equivalent to <code>On</code>. All other values are equivalent to <code>Off</code>. The variables and their default values are: </p>
<dl>
<dt><code>bell-style (audible)</code></dt>
<dd> <p> Controls what happens when readline wants to ring the terminal bell. If set to <code>none</code>, readline never rings the bell. If set to <code>visible</code>, readline uses a visible bell if one is available. If set to <code>audible</code>, readline attempts to ring the terminal&#8217;s bell. </p>
 </dd>
<dt><code>bind-tty-special-chars (On)</code></dt>
<dd> <p> If set to <code>On</code>, readline attempts to bind the control characters treated specially by the kernel&#8217;s terminal driver to their readline equivalents. </p>
 </dd>
<dt><code>comment-begin (``#&#8216;&#8216;)</code></dt>
<dd> <p> The string that is inserted in <code>vi</code> mode when the <code>insert-comment</code> command is executed. This command is bound to <code>M-#</code> in emacs mode and to <code>#</code> in vi command mode. </p>
 </dd>
<dt><code>completion-display-width (-1)</code></dt>
<dd> <p> The number of screen columns used to display possible matches when performing completion. The value is ignored if it is less than 0 or greater than the terminal screen width. A value of 0 will cause matches to be displayed one per line. The default value is -1. </p>
 </dd>
<dt><code>completion-ignore-case (Off)</code></dt>
<dd> <p> If set to <code>On</code>, readline performs filename matching and completion in a case-insensitive fashion. </p>
 </dd>
<dt><code>completion-map-case (Off)</code></dt>
<dd> <p> If set to <code>On</code>, and <code>completion-ignore-case</code> is enabled, readline treats hyphens (<i>-</i>) and underscores (<i>_</i>) as equivalent when performing case-insensitive filename matching and completion. </p>
 </dd>
<dt><code>completion-prefix-display-length (0)</code></dt>
<dd> <p> The length in characters of the common prefix of a list of possible completions that is displayed without modification. When set to a value greater than zero, common prefixes longer than this value are replaced with an ellipsis when displaying possible completions. </p>
 </dd>
<dt><code>completion-query-items (100)</code></dt>
<dd> <p> This determines when the user is queried about viewing the number of possible completions generated by the <code>possible-completions</code> command. It may be set to any integer value greater than or equal to zero. If the number of possible completions is greater than or equal to the value of this variable, the user is asked whether or not he wishes to view them; otherwise they are simply listed on the terminal. A negative value causes readline to never ask. </p>
 </dd>
<dt><code>convert-meta (On)</code></dt>
<dd> <p> If set to <code>On</code>, readline will convert characters with the eighth bit set to an ASCII key sequence by stripping the eighth bit and prefixing it with an escape character (in effect, using escape as the <i>meta prefix</i>). </p>
 </dd>
<dt><code>disable-completion (Off)</code></dt>
<dd> <p> If set to <code>On</code>, readline will inhibit word completion. Completion characters will be inserted into the line as if they had been mapped to <code>self-insert</code>. </p>
 </dd>
<dt><code>editing-mode (emacs)</code></dt>
<dd> <p> Controls whether readline begins with a set of key bindings similar to <i>Emacs</i> or <i>vi</i>. <code>editing-mode</code> can be set to either <code>emacs</code> or <code>vi</code>. </p>
 </dd>
<dt><code>echo-control-characters (On)</code></dt>
<dd> <p> When set to <code>On</code>, on operating systems that indicate they support it, readline echoes a character corresponding to a signal generated from the keyboard. </p>
 </dd>
<dt><code>enable-keypad (Off)</code></dt>
<dd> <p> When set to <code>On</code>, readline will try to enable the application keypad when it is called. Some systems need this to enable the arrow keys. </p>
 </dd>
<dt><code>enable-meta-key (On)</code></dt>
<dd> <p> When set to <code>On</code>, readline will try to enable any meta modifier key the terminal claims to support when it is called. On many terminals, the meta key is used to send eight-bit characters. </p>
 </dd>
<dt><code>expand-tilde (Off)</code></dt>
<dd> <p> If set to <code>On</code>, tilde expansion is performed when readline attempts word completion. </p>
 </dd>
<dt><code>history-preserve-point (Off)</code></dt>
<dd> <p> If set to <code>On</code>, the history code attempts to place point at the same location on each history line retrieved with <code>previous-history</code> or <code>next-history</code>. </p>
 </dd>
<dt><code>history-size (0)</code></dt>
<dd> <p> Set the maximum number of history entries saved in the history list. If set to zero, the number of entries in the history list is not limited. </p>
 </dd>
<dt><code>horizontal-scroll-mode (Off)</code></dt>
<dd> <p> When set to <code>On</code>, makes readline use a single line for display, scrolling the input horizontally on a single screen line when it becomes longer than the screen width rather than wrapping to a new line. </p>
 </dd>
<dt><code>input-meta (Off)</code></dt>
<dd> <p> If set to <code>On</code>, readline will enable eight-bit input (that is, it will not clear the eighth bit in the characters it reads), regardless of what the terminal claims it can support. The name <code>meta-flag</code> is a synonym for this variable. </p>
 </dd>
<dt><code>isearch-terminators (``C-[ C-J&#8217;&#8216;)</code></dt>
<dd> <p> The string of characters that should terminate an incremental search without subsequently executing the character as a command. If this variable has not been given a value, the characters <i>ESC</i> and <i>C-J</i> will terminate an incremental search. </p>
 </dd>
<dt><code>keymap (emacs)</code></dt>
<dd> <p> Set the current readline keymap. The set of legal keymap names is <i>emacs, emacs-standard, emacs-meta, emacs-ctlx, vi, vi-move, vi-command</i>, and <i>vi-insert</i>. <i>vi</i> is equivalent to <i>vi-command</i>; <i>emacs</i> is equivalent to <i>emacs-standard</i>. The default value is <i>emacs</i>. The value of <code>editing-mode</code> also affects the default keymap. </p>
 </dd>
<dt><code>mark-directories (On)</code></dt>
<dd> <p> If set to <code>On</code>, completed directory names have a slash appended. </p>
 </dd>
<dt><code>mark-modified-lines (Off)</code></dt>
<dd> <p> If set to <code>On</code>, history lines that have been modified are displayed with a preceding asterisk (<code>*</code>). </p>
 </dd>
<dt><code>mark-symlinked-directories (Off)</code></dt>
<dd> <p> If set to <code>On</code>, completed names which are symbolic links to directories have a slash appended (subject to the value of <code>mark-directories</code>). </p>
 </dd>
<dt><code>match-hidden-files (On)</code></dt>
<dd> <p> This variable, when set to <code>On</code>, causes readline to match files whose names begin with a `.&#8216; (hidden files) when performing filename completion. If set to <code>Off</code>, the leading `.&#8216; must be supplied by the user in the filename to be completed. </p>
 </dd>
<dt><code>menu-complete-display-prefix (Off)</code></dt>
<dd> <p> If set to <code>On</code>, menu completion displays the common prefix of the list of possible completions (which may be empty) before cycling through the list. </p>
 </dd>
<dt><code>output-meta (Off)</code></dt>
<dd> <p> If set to <code>On</code>, readline will display characters with the eighth bit set directly rather than as a meta-prefixed escape sequence. </p>
 </dd>
<dt><code>page-completions (On)</code></dt>
<dd> <p> If set to <code>On</code>, readline uses an internal <i>more</i>-like pager to display a screenful of possible completions at a time. </p>
 </dd>
<dt><code>print-completions-horizontally (Off)</code></dt>
<dd> <p> If set to <code>On</code>, readline will display completions with matches sorted horizontally in alphabetical order, rather than down the screen. </p>
 </dd>
<dt><code>revert-all-at-newline (Off)</code></dt>
<dd> <p> If set to <code>On</code>, readline will undo all changes to history lines before returning when <code>accept-line</code> is executed. By default, history lines may be modified and retain individual undo lists across calls to <code>readline</code>. </p>
 </dd>
<dt><code>show-all-if-ambiguous (Off)</code></dt>
<dd> <p> This alters the default behavior of the completion functions. If set to <code>On</code>, words which have more than one possible completion cause the matches to be listed immediately instead of ringing the bell. </p>
 </dd>
<dt><code>show-all-if-unmodified (Off)</code></dt>
<dd> <p> This alters the default behavior of the completion functions in a fashion similar to <code>show-all-if-ambiguous</code>. If set to <code>On</code>, words which have more than one possible completion without any possible partial completion (the possible completions don&#8217;t share a common prefix) cause the matches to be listed immediately instead of ringing the bell. </p>
 </dd>
<dt><code>skip-completed-text (Off)</code></dt>
<dd> <p> If set to <code>On</code>, this alters the default completion behavior when inserting a single match into the line. It&#8217;s only active when performing completion in the middle of a word. If enabled, readline does not insert characters from the completion that match characters after point in the word being completed, so portions of the word following the cursor are not duplicated. </p>
 </dd>
<dt><code>visible-stats (Off)</code></dt>
<dd> <p> If set to <code>On</code>, a character denoting a file&#8217;s type as reported by <i><a href="/docs/linux/man/2-stat/">stat</a></i>(2) is appended to the filename when listing possible completions. </p>
 </dd></dl>
<h3>Conditional Constructs</h3>
<p>Readline implements a facility similar in spirit to the conditional compilation features of the C preprocessor which allows key bindings and variable settings to be performed as the result of tests. There are four parser directives used. </p>
<dl>
<dt><code>$if</code></dt>
<dd> <p> The <code>$if</code> construct allows bindings to be made based on the editing mode, the terminal being used, or the application using readline. The text of the test extends to the end of the line; no characters are required to isolate it. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>mode</code></dt>
<dd> <p> The <code>mode=</code> form of the <code>$if</code> directive is used to test whether readline is in emacs or vi mode. This may be used in conjunction with the <code>set keymap</code> command, for instance, to set bindings in the <i>emacs-standard</i> and <i>emacs-ctlx</i> keymaps only if readline is starting out in emacs mode. </p>
 </dd>
<dt><code>term</code></dt>
<dd> <p> The <code>term=</code> form may be used to include terminal-specific key bindings, perhaps to bind the key sequences output by the terminal&#8217;s function keys. The word on the right side of the <code>=</code> is tested against the full name of the terminal and the portion of the terminal name before the first <code>-</code>. This allows <i>sun</i> to match both <i>sun</i> and <i>sun-cmd</i>, for instance. </p>
 </dd>
<dt><code>application</code></dt>
<dd> <p> The <code>application</code> construct is used to include application-specific settings. Each program using the readline library sets the <i>application name</i>, and an initialization file can test for a particular value. This could be used to bind key sequences to functions useful for a specific program. For instance, the following command adds a key sequence that quotes the current or previous word in <code>bash</code>: </p>
 </dd>
<dl>
<dd> <pre><code>
 $if  Bash
# Quote the current or previous word
&quot;\C-xq&quot;: &quot;\eb\&quot;\ef\&quot;&quot;
 $endif 
</code></pre>
 </dd></dl>
</dl>
</dl>
<dt><code>$endif</code></dt>
<dd> <p> This command, as seen in the previous example, terminates an <code>$if</code> command. </p>
 </dd>
<dt><code>$else</code></dt>
<dd> <p> Commands in this branch of the <code>$if</code> directive are executed if the test fails. </p>
 </dd>
<dt><code>$include</code></dt>
<dd> <p> This directive takes a single filename as an argument and reads commands and bindings from that file. For example, the following directive would read <i>/etc/inputrc</i>: </p>
 </dd>
<dl>
<dd> <pre><code>
 $include  /etc/inputrc 
</code></pre>
 </dd></dl>
</dl>
<h2>SEARCHING</h2>
<p>Readline provides commands for searching through the command history for lines containing a specified string. There are two search modes: <i>incremental</i> and <i>non-incremental</i>. </p>
<p>Incremental searches begin before the user has finished typing the search string. As each character of the search string is typed, readline displays the next entry from the history matching the string typed so far. An incremental search requires only as many characters as needed to find the desired history entry. To search backward in the history for a particular string, type <code>C-r</code>. Typing <code>C-s</code> searches forward through the history. The characters present in the value of the <code>isearch-terminators</code> variable are used to terminate an incremental search. If that variable has not been assigned a value the <i>Escape</i> and <code>C-J</code> characters will terminate an incremental search. <code>C-G</code> will abort an incremental search and restore the original line. When the search is terminated, the history entry containing the search string becomes the current line. </p>
<p>To find other matching entries in the history list, type <code>C-s</code> or <code>C-r</code> as appropriate. This will search backward or forward in the history for the next line matching the search string typed so far. Any other key sequence bound to a readline command will terminate the search and execute that command. For instance, a newline will terminate the search and accept the line, thereby executing the command from the history list. A movement command will terminate the search, make the last line found the current line, and begin editing. </p>
<p>Non-incremental searches read the entire search string before starting to search for matching history lines. The search string may be typed by the user or be part of the contents of the current line.  </p>
<h2>EDITING COMMANDS</h2>
<p>The following is a list of the names of the commands and the default key sequences to which they are bound. Command names without an accompanying key sequence are unbound by default. </p>
<p>In the following descriptions, <i>point</i> refers to the current cursor position, and <i>mark</i> refers to a cursor position saved by the <code>set-mark</code> command. The text between the point and mark is referred to as the <i>region</i>.  </p>
<h3>Commands for Moving</h3>
<dl>
<dt><code>beginning-of-line (C-a)</code></dt>
<dd> <p> Move to the start of the current line. </p>
 </dd>
<dt><code>end-of-line (C-e)</code></dt>
<dd> <p> Move to the end of the line. </p>
 </dd>
<dt><code>forward-char (C-f)</code></dt>
<dd> <p> Move forward a character. </p>
 </dd>
<dt><code>backward-char (C-b)</code></dt>
<dd> <p> Move back a character. </p>
 </dd>
<dt><code>forward-word (M-f)</code></dt>
<dd> <p> Move forward to the end of the next word. Words are composed of alphanumeric characters (letters and digits). </p>
 </dd>
<dt><code>backward-word (M-b)</code></dt>
<dd> <p> Move back to the start of the current or previous word. Words are composed of alphanumeric characters (letters and digits). </p>
 </dd>
<dt><code>clear-screen (C-l)</code></dt>
<dd> <p> Clear the screen leaving the current line at the top of the screen. With an argument, refresh the current line without clearing the screen. </p>
 </dd>
<dt><code>redraw-current-line</code></dt>
<dd> <p> Refresh the current line. </p>
 </dd></dl>
<h3>Commands for Manipulating the History</h3>
<dl>
<dt><code>accept-line (Newline, Return)</code></dt>
<dd> <p> Accept the line regardless of where the cursor is. If this line is non-empty, it may be added to the history list for future recall with <code>add_history()</code>. If the line is a modified history line, the history line is restored to its original state. </p>
 </dd>
<dt><code>previous-history (C-p)</code></dt>
<dd> <p> Fetch the previous command from the history list, moving back in the list. </p>
 </dd>
<dt><code>next-history (C-n)</code></dt>
<dd> <p> Fetch the next command from the history list, moving forward in the list. </p>
 </dd>
<dt><code>beginning-of-history (M-&lt;)</code></dt>
<dd> <p> Move to the first line in the history. </p>
 </dd>
<dt><code>end-of-history (M-&gt;)</code></dt>
<dd> <p> Move to the end of the input history, i.e., the line currently being entered. </p>
 </dd>
<dt><code>reverse-search-history (C-r)</code></dt>
<dd> <p> Search backward starting at the current line and moving `up&#8217; through the history as necessary. This is an incremental search. </p>
 </dd>
<dt><code>forward-search-history (C-s)</code></dt>
<dd> <p> Search forward starting at the current line and moving `down&#8217; through the history as necessary. This is an incremental search. </p>
 </dd>
<dt><code>non-incremental-reverse-search-history (M-p)</code></dt>
<dd> <p> Search backward through the history starting at the current line using a non-incremental search for a string supplied by the user. </p>
 </dd>
<dt><code>non-incremental-forward-search-history (M-n)</code></dt>
<dd> <p> Search forward through the history using a non-incremental search for a string supplied by the user. </p>
 </dd>
<dt><code>history-search-forward</code></dt>
<dd> <p> Search forward through the history for the string of characters between the start of the current line and the current cursor position (the <i>point</i>). This is a non-incremental search. </p>
 </dd>
<dt><code>history-search-backward</code></dt>
<dd> <p> Search backward through the history for the string of characters between the start of the current line and the point. This is a non-incremental search. </p>
 </dd>
<dt><code>yank-nth-arg (M-C-y)</code></dt>
<dd> <p> Insert the first argument to the previous command (usually the second word on the previous line) at point. With an argument <i>n</i>, insert the <i>n</i>th word from the previous command (the words in the previous command begin with word 0). A negative argument inserts the <i>n</i>th word from the end of the previous command. Once the argument <i>n</i> is computed, the argument is extracted as if the &quot;!<i>n</i>&quot; history expansion had been specified. </p>
 </dd>
<dt><code>yank-last-arg (M-., M-_)</code></dt>
<dd> <p> Insert the last argument to the previous command (the last word of the previous history entry). With a numeric argument, behave exactly like <code>yank-nth-arg</code>. Successive calls to <code>yank-last-arg</code> move back through the history list, inserting the last word (or the word specified by the argument to the first call) of each line in turn. Any numeric argument supplied to these successive calls determines the direction to move through the history. A negative argument switches the direction through the history (back or forward). The history expansion facilities are used to extract the last argument, as if the &quot;!$&quot; history expansion had been specified. </p>
 </dd></dl>
<h3>Commands for Changing Text</h3>
<dl>
<dt><code>delete-char (C-d)</code></dt>
<dd> <p> Delete the character at point. If point is at the beginning of the line, there are no characters in the line, and the last character typed was not bound to <code>delete-char</code>, then return <font SIZE="-1"><code>EOF</code>. </font> </p>
 </dd>
<dt><code>backward-delete-char (Rubout)</code></dt>
<dd> <p> Delete the character behind the cursor. When given a numeric argument, save the deleted text on the kill ring. </p>
 </dd>
<dt><code>forward-backward-delete-char </code></dt>
<dd> <p> Delete the character under the cursor, unless the cursor is at the end of the line, in which case the character behind the cursor is deleted. </p>
 </dd>
<dt><code>quoted-insert (C-q, C-v)</code></dt>
<dd> <p> Add the next character that you type to the line verbatim. This is how to insert characters like <code>C-q</code>, for example. </p>
 </dd>
<dt><code>tab-insert (M-TAB)</code></dt>
<dd> <p> Insert a tab character. </p>
 </dd>
<dt><code>self-insert (a, b, A, 1,&nbsp;<wbr>!, ...)</code></dt>
<dd> <p> Insert the character typed. </p>
 </dd>
<dt><code>transpose-chars (C-t)</code></dt>
<dd> <p> Drag the character before point forward over the character at point, moving point forward as well. If point is at the end of the line, then this transposes the two characters before point. Negative arguments have no effect. </p>
 </dd>
<dt><code>transpose-words (M-t)</code></dt>
<dd> <p> Drag the word before point past the word after point, moving point over that word as well. If point is at the end of the line, this transposes the last two words on the line. </p>
 </dd>
<dt><code>upcase-word (M-u)</code></dt>
<dd> <p> Uppercase the current (or following) word. With a negative argument, uppercase the previous word, but do not move point. </p>
 </dd>
<dt><code>downcase-word (M-l)</code></dt>
<dd> <p> Lowercase the current (or following) word. With a negative argument, lowercase the previous word, but do not move point. </p>
 </dd>
<dt><code>capitalize-word (M-c)</code></dt>
<dd> <p> Capitalize the current (or following) word. With a negative argument, capitalize the previous word, but do not move point. </p>
 </dd>
<dt><code>overwrite-mode</code></dt>
<dd> <p> Toggle overwrite mode. With an explicit positive numeric argument, switches to overwrite mode. With an explicit non-positive numeric argument, switches to insert mode. This command affects only <code>emacs</code> mode; <code>vi</code> mode does overwrite differently. Each call to <i>readline()</i> starts in insert mode. In overwrite mode, characters bound to <code>self-insert</code> replace the text at point rather than pushing the text to the right. Characters bound to <code>backward-delete-char</code> replace the character before point with a space. By default, this command is unbound. </p>
 </dd></dl>
<h3>Killing and Yanking</h3>
<dl>
<dt><code>kill-line (C-k)</code></dt>
<dd> <p> Kill the text from point to the end of the line. </p>
 </dd>
<dt><code>backward-kill-line (C-x Rubout)</code></dt>
<dd> <p> Kill backward to the beginning of the line. </p>
 </dd>
<dt><code>unix-line-discard (C-u)</code></dt>
<dd> <p> Kill backward from point to the beginning of the line. The killed text is saved on the kill-ring. </p>
 </dd>
<dt><code>kill-whole-line</code></dt>
<dd> <p> Kill all characters on the current line, no matter where point is. </p>
 </dd>
<dt><code>kill-word (M-d)</code></dt>
<dd> <p> Kill from point the end of the current word, or if between words, to the end of the next word. Word boundaries are the same as those used by <code>forward-word</code>. </p>
 </dd>
<dt><code>backward-kill-word (M-Rubout)</code></dt>
<dd> <p> Kill the word behind point. Word boundaries are the same as those used by <code>backward-word</code>. </p>
 </dd>
<dt><code>unix-word-rubout (C-w)</code></dt>
<dd> <p> Kill the word behind point, using white space as a word boundary. The killed text is saved on the kill-ring. </p>
 </dd>
<dt><code>unix-filename-rubout</code></dt>
<dd> <p> Kill the word behind point, using white space and the slash character as the word boundaries. The killed text is saved on the kill-ring. </p>
 </dd>
<dt><code>delete-horizontal-space (M-\)</code></dt>
<dd> <p> Delete all spaces and tabs around point. </p>
 </dd>
<dt><code>kill-region</code></dt>
<dd> <p> Kill the text between the point and <i>mark</i> (saved cursor position). This text is referred to as the <i>region</i>. </p>
 </dd>
<dt><code>copy-region-as-kill</code></dt>
<dd> <p> Copy the text in the region to the kill buffer. </p>
 </dd>
<dt><code>copy-backward-word</code></dt>
<dd> <p> Copy the word before point to the kill buffer. The word boundaries are the same as <code>backward-word</code>. </p>
 </dd>
<dt><code>copy-forward-word</code></dt>
<dd> <p> Copy the word following point to the kill buffer. The word boundaries are the same as <code>forward-word</code>. </p>
 </dd>
<dt><code>yank (C-y)</code></dt>
<dd> <p> Yank the top of the kill ring into the buffer at point. </p>
 </dd>
<dt><code>yank-pop (M-y)</code></dt>
<dd> <p> Rotate the kill ring, and yank the new top. Only works following <code>yank</code> or <code>yank-pop</code>. </p>
 </dd></dl>
<h3>Numeric Arguments</h3>
<dl>
<dt><code>digit-argument (M-0, M-1, ..., M--)</code></dt>
<dd> <p> Add this digit to the argument already accumulating, or start a new argument. M-- starts a negative argument. </p>
 </dd>
<dt><code>universal-argument</code></dt>
<dd> <p> This is another way to specify an argument. If this command is followed by one or more digits, optionally with a leading minus sign, those digits define the argument. If the command is followed by digits, executing <code>universal-argument</code> again ends the numeric argument, but is otherwise ignored. As a special case, if this command is immediately followed by a character that is neither a digit or minus sign, the argument count for the next command is multiplied by four. The argument count is initially one, so executing this function the first time makes the argument count four, a second time makes the argument count sixteen, and so on. </p>
 </dd></dl>
<h3>Completing</h3>
<dl>
<dt><code>complete (TAB)</code></dt>
<dd> <p> Attempt to perform completion on the text before point. The actual completion performed is application-specific. <code>Bash</code>, for instance, attempts completion treating the text as a variable (if the text begins with <code>$</code>), username (if the text begins with <code>~</code>), hostname (if the text begins with <code>@</code>), or command (including aliases and functions) in turn. If none of these produces a match, filename completion is attempted. <code>Gdb</code>, on the other hand, allows completion of program functions and variables, and only attempts filename completion under certain circumstances. </p>
 </dd>
<dt><code>possible-completions (M-?)</code></dt>
<dd> <p> List the possible completions of the text before point. When displaying completions, readline sets the number of columns used for display to the value of <code>completion-display-width</code>, the value of the environment variable <font SIZE="-1"><code>COLUMNS</code>, </font> or the screen width, in that order. </p>
 </dd>
<dt><code>insert-completions (M-*)</code></dt>
<dd> <p> Insert all completions of the text before point that would have been generated by <code>possible-completions</code>. </p>
 </dd>
<dt><code>menu-complete</code></dt>
<dd> <p> Similar to <code>complete</code>, but replaces the word to be completed with a single match from the list of possible completions. Repeated execution of <code>menu-complete</code> steps through the list of possible completions, inserting each match in turn. At the end of the list of completions, the bell is rung (subject to the setting of <code>bell-style</code>) and the original text is restored. An argument of <i>n</i> moves <i>n</i> positions forward in the list of matches; a negative argument may be used to move backward through the list. This command is intended to be bound to <code>TAB</code>, but is unbound by default. </p>
 </dd>
<dt><code>menu-complete-backward</code></dt>
<dd> <p> Identical to <code>menu-complete</code>, but moves backward through the list of possible completions, as if <code>menu-complete</code> had been given a negative argument. This command is unbound by default. </p>
 </dd>
<dt><code>delete-char-or-list</code></dt>
<dd> <p> Deletes the character under the cursor if not at the beginning or end of the line (like <code>delete-char</code>). If at the end of the line, behaves identically to <code>possible-completions</code>. </p>
 </dd></dl>
<h3>Keyboard Macros</h3>
<dl>
<dt><code>start-kbd-macro (C-x ()</code></dt>
<dd> <p> Begin saving the characters typed into the current keyboard macro. </p>
 </dd>
<dt><code>end-kbd-macro (C-x ))</code></dt>
<dd> <p> Stop saving the characters typed into the current keyboard macro and store the definition. </p>
 </dd>
<dt><code>call-last-kbd-macro (C-x e)</code></dt>
<dd> <p> Re-execute the last keyboard macro defined, by making the characters in the macro appear as if typed at the keyboard. </p>
 </dd></dl>
<h3>Miscellaneous</h3>
<dl>
<dt><code>re-read-init-file (C-x C-r)</code></dt>
<dd> <p> Read in the contents of the <i>inputrc</i> file, and incorporate any bindings or variable assignments found there. </p>
 </dd>
<dt><code>abort (C-g)</code></dt>
<dd> <p> Abort the current editing command and ring the terminal&#8217;s bell (subject to the setting of <code>bell-style</code>). </p>
 </dd>
<dt><code>do-uppercase-version (M-a, M-b, M-</code><i>x</i>, ...) </dt>
<dd> <p> If the metafied character <i>x</i> is lowercase, run the command that is bound to the corresponding uppercase character. </p>
 </dd>
<dt><code>prefix-meta (ESC)</code></dt>
<dd> <p> Metafy the next character typed. <font SIZE="-1"><code>ESC</code> </font> <code>f</code> is equivalent to <code>Meta-f</code>. </p>
 </dd>
<dt><code>undo (C-_, C-x C-u)</code></dt>
<dd> <p> Incremental undo, separately remembered for each line. </p>
 </dd>
<dt><code>revert-line (M-r)</code></dt>
<dd> <p> Undo all changes made to this line. This is like executing the <code>undo</code> command enough times to return the line to its initial state. </p>
 </dd>
<dt><code>tilde-expand (M-&amp;)</code></dt>
<dd> <p> Perform tilde expansion on the current word. </p>
 </dd>
<dt><code>set-mark (C-@, M-&lt;space&gt;)</code></dt>
<dd> <p> Set the mark to the point. If a numeric argument is supplied, the mark is set to that position. </p>
 </dd>
<dt><code>exchange-point-and-mark (C-x C-x)</code></dt>
<dd> <p> Swap the point with the mark. The current cursor position is set to the saved position, and the old cursor position is saved as the mark. </p>
 </dd>
<dt><code>character-search (C-])</code></dt>
<dd> <p> A character is read and point is moved to the next occurrence of that character. A negative count searches for previous occurrences. </p>
 </dd>
<dt><code>character-search-backward (M-C-])</code></dt>
<dd> <p> A character is read and point is moved to the previous occurrence of that character. A negative count searches for subsequent occurrences. </p>
 </dd>
<dt><code>skip-csi-sequence</code></dt>
<dd> <p> Read enough characters to consume a multi-key sequence such as those defined for keys like Home and End. Such sequences begin with a Control Sequence Indicator (CSI), usually ESC-[. If this sequence is bound to &quot;\[&quot;, keys producing such sequences will have no effect unless explicitly bound to a readline command, instead of inserting stray characters into the editing buffer. This is unbound by default, but usually bound to ESC-[. </p>
 </dd>
<dt><code>insert-comment (M-#)</code></dt>
<dd> <p> Without a numeric argument, the value of the readline <code>comment-begin</code> variable is inserted at the beginning of the current line. If a numeric argument is supplied, this command acts as a toggle: if the characters at the beginning of the line do not match the value of <code>comment-begin</code>, the value is inserted, otherwise the characters in <code>comment-begin</code> are deleted from the beginning of the line. In either case, the line is accepted as if a newline had been typed. The default value of <code>comment-begin</code> makes the current line a shell comment. If a numeric argument causes the comment character to be removed, the line will be executed by the shell. </p>
 </dd>
<dt><code>dump-functions</code></dt>
<dd> <p> Print all of the functions and their key bindings to the readline output stream. If a numeric argument is supplied, the output is formatted in such a way that it can be made part of an <i>inputrc</i> file. </p>
 </dd>
<dt><code>dump-variables</code></dt>
<dd> <p> Print all of the settable variables and their values to the readline output stream. If a numeric argument is supplied, the output is formatted in such a way that it can be made part of an <i>inputrc</i> file. </p>
 </dd>
<dt><code>dump-macros</code></dt>
<dd> <p> Print all of the readline key sequences bound to macros and the strings they output. If a numeric argument is supplied, the output is formatted in such a way that it can be made part of an <i>inputrc</i> file. </p>
 </dd>
<dt><code>emacs-editing-mode (C-e)</code></dt>
<dd> <p> When in <code>vi</code> command mode, this causes a switch to <code>emacs</code> editing mode. </p>
 </dd>
<dt><code>vi-editing-mode (M-C-j)</code></dt>
<dd> <p> When in <code>emacs</code> editing mode, this causes a switch to <code>vi</code> editing mode. </p>
 </dd></dl>
<h2>DEFAULT KEY BINDINGS</h2>
<p>The following is a list of the default emacs and vi bindings. Characters with the eighth bit set are written as M-&lt;character&gt;, and are referred to as <i>metafied</i> characters. The printable ASCII characters not mentioned in the list of emacs standard bindings are bound to the <code>self-insert</code> function, which just inserts the given character into the input line. In vi insertion mode, all characters not specifically mentioned are bound to <code>self-insert</code>. Characters assigned to signal generation by <i><a href="/docs/linux/man/1-stty/">stty</a></i>(1) or the terminal driver, such as C-Z or C-C, retain that function. Upper and lower case metafied characters are bound to the same function in the emacs mode meta keymap. The remaining characters are unbound, which causes readline to ring the bell (subject to the setting of the <code>bell-style</code> variable).  </p>
<h3>Emacs Mode</h3>
<dl>
<dd> <pre><code>Emacs Standard bindings
&quot;C-@&quot; set-mark
&quot;C-A&quot; beginning-of-line
&quot;C-B&quot; backward-char
&quot;C-D&quot; delete-char
&quot;C-E&quot; end-of-line
&quot;C-F&quot; forward-char
&quot;C-G&quot; abort
&quot;C-H&quot; backward-delete-char
&quot;C-I&quot; complete
&quot;C-J&quot; accept-line
&quot;C-K&quot; kill-line
&quot;C-L&quot; clear-screen
&quot;C-M&quot; accept-line
&quot;C-N&quot; next-history
&quot;C-P&quot; previous-history
&quot;C-Q&quot; quoted-insert
&quot;C-R&quot; reverse-search-history
&quot;C-S&quot; forward-search-history
&quot;C-T&quot; transpose-chars
&quot;C-U&quot; unix-line-discard
&quot;C-V&quot; quoted-insert
&quot;C-W&quot; unix-word-rubout
&quot;C-Y&quot; yank
&quot;C-]&quot; character-search
&quot;C-_&quot; undo
&quot; &quot; to &quot;/&quot; self-insert
&quot;0&quot; to &quot;9&quot; self-insert
&quot;:&quot; to &quot;~&quot; self-insert
&quot;C-?&quot; backward-delete-char
Emacs Meta bindings
&quot;M-C-G&quot; abort
&quot;M-C-H&quot; backward-kill-word
&quot;M-C-I&quot; tab-insert
&quot;M-C-J&quot; vi-editing-mode
&quot;M-C-M&quot; vi-editing-mode
&quot;M-C-R&quot; revert-line
&quot;M-C-Y&quot; yank-nth-arg
&quot;M-C-[&quot; complete
&quot;M-C-]&quot; character-search-backward
&quot;M-space&quot; set-mark
&quot;M-#&quot; insert-comment
&quot;M-&amp;&quot; tilde-expand
&quot;M-*&quot; insert-completions
&quot;M--&quot; digit-argument
&quot;M-.&quot; yank-last-arg
&quot;M-0&quot; digit-argument
&quot;M-1&quot; digit-argument
&quot;M-2&quot; digit-argument
&quot;M-3&quot; digit-argument
&quot;M-4&quot; digit-argument
&quot;M-5&quot; digit-argument
&quot;M-6&quot; digit-argument
&quot;M-7&quot; digit-argument
&quot;M-8&quot; digit-argument
&quot;M-9&quot; digit-argument
&quot;M-&lt;&quot; beginning-of-history
&quot;M-=&quot; possible-completions
&quot;M-&gt;&quot; end-of-history
&quot;M-?&quot; possible-completions
&quot;M-B&quot; backward-word
&quot;M-C&quot; capitalize-word
&quot;M-D&quot; kill-word
&quot;M-F&quot; forward-word
&quot;M-L&quot; downcase-word
&quot;M-N&quot; non-incremental-forward-search-history
&quot;M-P&quot; non-incremental-reverse-search-history
&quot;M-R&quot; revert-line
&quot;M-T&quot; transpose-words
&quot;M-U&quot; upcase-word
&quot;M-Y&quot; yank-pop
&quot;M-\&quot; delete-horizontal-space
&quot;M-~&quot; tilde-expand
&quot;M-C-?&quot; backward-kill-word
&quot;M-_&quot; yank-last-arg
Emacs Control-X bindings
&quot;C-XC-G&quot; abort
&quot;C-XC-R&quot; re-read-init-file
&quot;C-XC-U&quot; undo
&quot;C-XC-X&quot; exchange-point-and-mark
&quot;C-X(&quot; start-kbd-macro
&quot;C-X)&quot; end-kbd-macro
&quot;C-XE&quot; call-last-kbd-macro
&quot;C-XC-?&quot; backward-kill-line
 </dd></dl>

</code></pre>
<h3>VI Mode bindings</h3>
<dl>
<dd> <pre><code>VI Insert Mode functions
&quot;C-D&quot; vi-eof-maybe
&quot;C-H&quot; backward-delete-char
&quot;C-I&quot; complete
&quot;C-J&quot; accept-line
&quot;C-M&quot; accept-line
&quot;C-R&quot; reverse-search-history
&quot;C-S&quot; forward-search-history
&quot;C-T&quot; transpose-chars
&quot;C-U&quot; unix-line-discard
&quot;C-V&quot; quoted-insert
&quot;C-W&quot; unix-word-rubout
&quot;C-Y&quot; yank
&quot;C-[&quot; vi-movement-mode
&quot;C-_&quot; undo
&quot; &quot; to &quot;~&quot; self-insert
&quot;C-?&quot; backward-delete-char
VI Command Mode functions
&quot;C-D&quot; vi-eof-maybe
&quot;C-E&quot; emacs-editing-mode
&quot;C-G&quot; abort
&quot;C-H&quot; backward-char
&quot;C-J&quot; accept-line
&quot;C-K&quot; kill-line
&quot;C-L&quot; clear-screen
&quot;C-M&quot; accept-line
&quot;C-N&quot; next-history
&quot;C-P&quot; previous-history
&quot;C-Q&quot; quoted-insert
&quot;C-R&quot; reverse-search-history
&quot;C-S&quot; forward-search-history
&quot;C-T&quot; transpose-chars
&quot;C-U&quot; unix-line-discard
&quot;C-V&quot; quoted-insert
&quot;C-W&quot; unix-word-rubout
&quot;C-Y&quot; yank
&quot;C-_&quot; vi-undo
&quot; &quot; forward-char
&quot;#&quot; insert-comment
&quot;$&quot; end-of-line
&quot;%&quot; vi-match
&quot;&amp;&quot; vi-tilde-expand
&quot;*&quot; vi-complete
&quot;+&quot; next-history
&quot;,&quot; vi-char-search
&quot;-&quot; previous-history
&quot;.&quot; vi-redo
&quot;/&quot; vi-search
&quot;0&quot; beginning-of-line
&quot;1&quot; to &quot;9&quot; vi-arg-digit
&quot;;&quot; vi-char-search
&quot;=&quot; vi-complete
&quot;?&quot; vi-search
&quot;A&quot; vi-append-eol
&quot;B&quot; vi-prev-word
&quot;C&quot; vi-change-to
&quot;D&quot; vi-delete-to
&quot;E&quot; vi-end-word
&quot;F&quot; vi-char-search
&quot;G&quot; vi-fetch-history
&quot;I&quot; vi-insert-beg
&quot;N&quot; vi-search-again
&quot;P&quot; vi-put
&quot;R&quot; vi-replace
&quot;S&quot; vi-subst
&quot;T&quot; vi-char-search
&quot;U&quot; revert-line
&quot;W&quot; vi-next-word
&quot;X&quot; backward-delete-char
&quot;Y&quot; vi-yank-to
&quot;\&quot; vi-complete
&quot;^&quot; vi-first-print
&quot;_&quot; vi-yank-arg
&quot;`&quot; vi-goto-mark
&quot;a&quot; vi-append-mode
&quot;b&quot; vi-prev-word
&quot;c&quot; vi-change-to
&quot;d&quot; vi-delete-to
&quot;e&quot; vi-end-word
&quot;f&quot; vi-char-search
&quot;h&quot; backward-char
&quot;i&quot; vi-insertion-mode
&quot;j&quot; next-history
&quot;k&quot; prev-history
&quot;l&quot; forward-char
&quot;m&quot; vi-set-mark
&quot;n&quot; vi-search-again
&quot;p&quot; vi-put
&quot;r&quot; vi-change-char
&quot;s&quot; vi-subst
&quot;t&quot; vi-char-search
&quot;u&quot; vi-undo
&quot;w&quot; vi-next-word
&quot;x&quot; vi-delete
&quot;y&quot; vi-yank-to
&quot;|&quot; vi-column
&quot;~&quot; vi-change-case
 </dd></dl>

</code></pre>
<h2>SEE ALSO</h2>
<dl>
<dt><i>The Gnu Readline Library</i>, Brian Fox and Chet Ramey</dt>
<dd>  </dd>
<dt><i>The Gnu History Library</i>, Brian Fox and Chet Ramey</dt>
<dd>  </dd>
<dt><i><a href="/docs/linux/man/1-bash/">bash</a></i>(1)</dt>
<dd>  </dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>~/.inputrc</i></dt>
<dd> <p> Individual <code>readline</code> initialization file </p>
 </dd></dl>
<h2>AUTHORS</h2>
<p> Brian Fox, Free Software Foundation <br />
 bfox [at] gnu.org </p>
<p>Chet Ramey, Case Western Reserve University <br />
 chet [at] ins.CWRU.Edu  </p>
<h2>BUG REPORTS</h2>
<p> If you find a bug in <code>readline,</code> you should report it. But first, you should make sure that it really is a bug, and that it appears in the latest version of the <code>readline</code> library that you have. </p>
<p>Once you have determined that a bug actually exists, mail a bug report to <i>bug-readline</i>@<i>gnu.org</i>. If you have a fix, you are welcome to mail that as well! Suggestions and `philosophical&#8217; bug reports may be mailed to bug-readline@<i>gnu.org</i> or posted to the Usenet newsgroup <code>gnu.bash.bug</code>. </p>
<p>Comments and bug reports concerning this manual page should be directed to <i>chet [at] ins.CWRU.Edu</i>.  </p>
<h2>BUGS</h2>
<p>It&#8217;s too big and too slow. </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">COPYRIGHT</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">RETURN VALUE</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">NOTATION</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">INITIALIZATION FILE</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAI">Key Bindings</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">Variables</a></dt>
<dd>  </dd>
<dt><a href="#lbAK">Conditional Constructs</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAL">SEARCHING</a></dt>
<dd>  </dd>
<dt><a href="#lbAM">EDITING COMMANDS</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAN">Commands for Moving</a></dt>
<dd>  </dd>
<dt><a href="#lbAO">Commands for Manipulating the History</a></dt>
<dd>  </dd>
<dt><a href="#lbAP">Commands for Changing Text</a></dt>
<dd>  </dd>
<dt><a href="#lbAQ">Killing and Yanking</a></dt>
<dd>  </dd>
<dt><a href="#lbAR">Numeric Arguments</a></dt>
<dd>  </dd>
<dt><a href="#lbAS">Completing</a></dt>
<dd>  </dd>
<dt><a href="#lbAT">Keyboard Macros</a></dt>
<dd>  </dd>
<dt><a href="#lbAU">Miscellaneous</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAV">DEFAULT KEY BINDINGS</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAW">Emacs Mode</a></dt>
<dd>  </dd>
<dt><a href="#lbAX">VI Mode bindings</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAY">SEE ALSO</a></dt>
<dd>  </dd>
<dt><a href="#lbAZ">FILES</a></dt>
<dd>  </dd>
<dt><a href="#lbBA">AUTHORS</a></dt>
<dd>  </dd>
<dt><a href="#lbBB">BUG REPORTS</a></dt>
<dd>  </dd>
<dt><a href="#lbBC">BUGS</a></dt>
<dd>  </dd></dl>
