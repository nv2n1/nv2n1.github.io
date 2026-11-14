---
title: "editrc(5)"
name: "editrc"
section: "5"
letter: "e"
url: "/docs/linux/man/5-editrc/"
description: "editrc – configuration file for editline library"
---

<p><code>editrc</code> &#8211; configuration file for editline library</p>
<h2>Synopsis</h2>
<h2>Description</h2>
<p>The file defines various settings to be used by the <a href="/docs/linux/man/3-editline/">editline</a>(3) library. </p>
<p> The format of each line is: </p>
<blockquote><p><tt>[prog:]command [arg ...]</tt></p></blockquote>
<p> <i>command</i> is one of the <a href="/docs/linux/man/3-editline/">editline</a>(3) builtin commands. Refer to Sx BUILTIN COMMANDS for more information. </p>
<p> <i>prog</i> is the program name string that a program defines when it calls el_init3 to set up <a href="/docs/linux/man/3-editline/">editline</a>(3), which is usually <i>argv[0]</i> <i>command</i> will be executed for any program which matches <i>prog</i> </p>
<p> <i>prog</i> may also be a <a href="/docs/linux/man/3-regex/">regex</a>(3) style regular expression, in which case <i>command</i> will be executed for any program that matches the regular expression. </p>
<p> If <i>prog</i> is absent, <i>command</i> is executed for all programs.</p>
<h2>Builtin Commands</h2>
<p>The <code>editline</code> library has some builtin commands, which affect the way that the line editing and history functions operate. These are based on similar named builtins present in the <a href="/docs/linux/man/1-tcsh/">tcsh</a>(1) shell. </p>
<p> The following builtin commands are available:</p>
<dl>
<dt><code>bind </code>[-<code>a </code>[-<code>e </code>[-<code>k </code>[-<code>l </code>[-<code>r </code>] ] ] ] ]</p>
<dd>Oo Fl s Oc Oo Fl v Oc Oo Ar key Oo Ar command Oc Oc Without options, list all bound keys, and the editor command to which each is bound. If <i>key</i> is supplied, show the bindings for <i>key</i> If <i>key command</i> is supplied, bind <i>command</i> to <i>key</i> Options include:</p>
<dl>
<dt><code>-a</code></p>
<dd>List or change key bindings in the <a href="/docs/linux/man/1-vi/">vi</a>(1) mode alternate (command mode) key map.</p>
<dt><code>-e</code></p>
<dd>Bind all keys to the standard GNU Emacs-like bindings.</p>
<dt><code>-k</code></p>
<dd><i>key</i> is interpreted as a symbolic arrow key name, which may be one of `up&#8217; `down&#8217; `left&#8217; or `right&#8217;</p>
<dt><code>-l</code></p>
<dd>List all editor commands and a short description of each.</p>
<dt><code>-r</code></p>
<dd>Remove a key&#8217;s binding.</p>
<dt><code>-s</code></p>
<dd><i>command</i> is taken as a literal string and treated as terminal input when <i>key</i> is typed. Bound keys in <i>command</i> are themselves reinterpreted, and this continues for ten levels of interpretation.</p>
<dt><code>-v</code></p>
<dd>Bind all keys to the standard <a href="/docs/linux/man/1-vi/">vi</a>(1)Ns-like bindings.</dl>
<p> <i>command</i> may be one of the commands documented in Sx EDITOR COMMANDS below, or another key. </p>
<p> <i>key</i> and <i>command</i> can contain control characters of the form `<code>^ </code><i>character</i> &#8216; Po e.g. `^A&#8217; Pc , and the following backslashed escape sequences: </p>
<dl>
<dt><code></code></p>
<dd>Bell</p>
<dt><code></code></p>
<dd>Backspace</p>
<dt><code></code></p>
<dd>Escape</p>
<dt><code></code></p>
<dd>Formfeed</p>
<dt><code>
</code></p>
<dd>Newline</p>
<dt><code></code></p>
<dd>Carriage return</p>
<dt><code>	</code></p>
<dd>Horizontal tab</p>
<dt><code></code></p>
<dd>Vertical tab</p>
<dt><code>\ </code><i>nnn</i></p>
<dd>The ASCII character corresponding to the octal number <i>nnn</i></dl>
<p> `\&#8217; nullifies the special meaning of the following character, if it has any, notably `\&#8217; and `^&#8217;</p>
<dt><code>echotc </code>[-<code>sv </code><i>arg &#8230;</i> ]</p>
<dd>Exercise terminal capabilities given in <i>arg &#8230;</i> If <i>arg</i> is `baud&#8217; `cols&#8217; `lines&#8217; `rows&#8217; `meta&#8217; or `tabs&#8217; the value of that capability is printed, with &#8220;yes&#8221; or &#8220;no&#8221; indicating that the terminal does or does not have that capability. </p>
<p> &#8211;<code>s</code> returns an empty string for non-existent capabilities, rather than causing an error. &#8211;<code>v</code> causes messages to be verbose.</p>
<dt><code>edit </code>[<code>on | off</code> ]</p>
<dd>Enable or disable the <code>editline</code> functionality in a program.</p>
<dt><code>history </code><i>list | size </i><code>n | </code><i>unique </i><code>n</code></p>
<dd>The <i>list</i> command lists all entries in the history. The <i>size</i> command sets the history size to <code>n</code> entries. The <i>unique</i> command controls if history should keep duplicate entries. If <code>n</code> is non zero, only keep unique history entries. If <code>n</code> is zero, then keep all entries (the default).</p>
<dt><code>settc </code><i>cap val</i></p>
<dd>Set the terminal capability <i>cap</i> to <i>val</i> as defined in <a href="/docs/linux/man/5-termcap/">termcap</a>(5). No sanity checking is done.</p>
<dt><code>setty </code>[-<code>a </code>[-<code>d </code>[-<code>q </code>[-<code>x </code>[<i>+mode </i>] ] ] ] ]</p>
<dd>Oo Ar -mode Oc Oo Ar mode Oc Oo Ar char=c Oc Control which tty modes that won&#8217;t allow the user to change. &#8211;<code>d</code> &#8211;<code>q</code> or &#8211;<code>x</code> tells <code>setty</code> to act on the `edit&#8217; `quote&#8217; or `execute&#8217; set of tty modes respectively; defaulting to &#8211;<code>x</code> </p>
<p> Without other arguments, <code>setty</code> lists the modes in the chosen set which are fixed on Po `+mode&#8217; Pc or off Po `-mode&#8217; Pc . &#8211;<code>a</code> lists all tty modes in the chosen set regardless of the setting. With <i>+mode</i> <i>-mode</i> or <i>mode</i> fixes <i>mode</i> on or off or removes control of <i>mode</i> in the chosen set. </p>
<p> <code>Setty</code> can also be used to set tty characters to particular values using <i>char=value</i> If <i>value</i> is empty then the character is set to <code>_POSIX_VDISABLE</code></p>
<dt><code>telltc</code></p>
<dd>List the values of all the terminal capabilities (see <a href="/docs/linux/man/5-termcap/">termcap</a>(5)).</dl>
<h2>Editor Commands</h2>
<p>The following editor commands are available for use in key bindings:</p>
<dl>
<dt><code>vi-paste-next</code></p>
<dd>Vi paste previous deletion to the right of the cursor.</p>
<dt><code>vi-paste-prev</code></p>
<dd>Vi paste previous deletion to the left of the cursor.</p>
<dt><code>vi-prev-big-word</code></p>
<dd>Vi move to the previous space delimited word.</p>
<dt><code>vi-prev-word</code></p>
<dd>Vi move to the previous word.</p>
<dt><code>vi-next-big-word</code></p>
<dd>Vi move to the next space delimited word.</p>
<dt><code>vi-next-word</code></p>
<dd>Vi move to the next word.</p>
<dt><code>vi-change-case</code></p>
<dd>Vi change case of character under the cursor and advance one character.</p>
<dt><code>vi-change-meta</code></p>
<dd>Vi change prefix command.</p>
<dt><code>vi-insert-at-bol</code></p>
<dd>Vi enter insert mode at the beginning of line.</p>
<dt><code>vi-replace-char</code></p>
<dd>Vi replace character under the cursor with the next character typed.</p>
<dt><code>vi-replace-mode</code></p>
<dd>Vi enter replace mode.</p>
<dt><code>vi-substitute-char</code></p>
<dd>Vi replace character under the cursor and enter insert mode.</p>
<dt><code>vi-substitute-line</code></p>
<dd>Vi substitute entire line.</p>
<dt><code>vi-change-to-eol</code></p>
<dd>Vi change to end of line.</p>
<dt><code>vi-insert</code></p>
<dd>Vi enter insert mode.</p>
<dt><code>vi-add</code></p>
<dd>Vi enter insert mode after the cursor.</p>
<dt><code>vi-add-at-eol</code></p>
<dd>Vi enter insert mode at end of line.</p>
<dt><code>vi-delete-meta</code></p>
<dd>Vi delete prefix command.</p>
<dt><code>vi-end-big-word</code></p>
<dd>Vi move to the end of the current space delimited word.</p>
<dt><code>vi-end-word</code></p>
<dd>Vi move to the end of the current word.</p>
<dt><code>vi-undo</code></p>
<dd>Vi undo last change.</p>
<dt><code>vi-command-mode</code></p>
<dd>Vi enter command mode (use alternative key bindings).</p>
<dt><code>vi-zero</code></p>
<dd>Vi move to the beginning of line.</p>
<dt><code>vi-delete-prev-char</code></p>
<dd>Vi move to previous character (backspace).</p>
<dt><code>vi-list-or-eof</code></p>
<dd>Vi list choices for completion or indicate end of file if empty line.</p>
<dt><code>vi-kill-line-prev</code></p>
<dd>Vi cut from beginning of line to cursor.</p>
<dt><code>vi-search-prev</code></p>
<dd>Vi search history previous.</p>
<dt><code>vi-search-next</code></p>
<dd>Vi search history next.</p>
<dt><code>vi-repeat-search-next</code></p>
<dd>Vi repeat current search in the same search direction.</p>
<dt><code>vi-repeat-search-prev</code></p>
<dd>Vi repeat current search in the opposite search direction.</p>
<dt><code>vi-next-char</code></p>
<dd>Vi move to the character specified next.</p>
<dt><code>vi-prev-char</code></p>
<dd>Vi move to the character specified previous.</p>
<dt><code>vi-to-next-char</code></p>
<dd>Vi move up to the character specified next.</p>
<dt><code>vi-to-prev-char</code></p>
<dd>Vi move up to the character specified previous.</p>
<dt><code>vi-repeat-next-char</code></p>
<dd>Vi repeat current character search in the same search direction.</p>
<dt><code>vi-repeat-prev-char</code></p>
<dd>Vi repeat current character search in the opposite search direction.</p>
<dt><code>vi-match</code></p>
<dd>Vi go to matching () {} or [].</p>
<dt><code>vi-undo-line</code></p>
<dd>Vi undo all changes to line.</p>
<dt><code>vi-to-column</code></p>
<dd>Vi go to specified column.</p>
<dt><code>vi-yank-end</code></p>
<dd>Vi yank to end of line.</p>
<dt><code>vi-yank</code></p>
<dd>Vi yank.</p>
<dt><code>vi-comment-out</code></p>
<dd>Vi comment out current command.</p>
<dt><code>vi-alias</code></p>
<dd>Vi include shell alias.</p>
<dt><code>vi-to-history-line</code></p>
<dd>Vi go to specified history file line..</p>
<dt><code>vi-histedit</code></p>
<dd>Vi edit history line with vi.</p>
<dt><code>vi-history-word</code></p>
<dd>Vi append word from previous input line.</p>
<dt><code>vi-redo</code></p>
<dd>Vi redo last non-motion command.</p>
<dt><code>em-delete-or-list</code></p>
<dd>Delete character under cursor or list completions if at end of line.</p>
<dt><code>em-delete-next-word</code></p>
<dd>Cut from cursor to end of current word.</p>
<dt><code>em-yank</code></p>
<dd>Paste cut buffer at cursor position.</p>
<dt><code>em-kill-line</code></p>
<dd>Cut the entire line and save in cut buffer.</p>
<dt><code>em-kill-region</code></p>
<dd>Cut area between mark and cursor and save in cut buffer.</p>
<dt><code>em-copy-region</code></p>
<dd>Copy area between mark and cursor to cut buffer.</p>
<dt><code>em-gosmacs-transpose</code></p>
<dd>Exchange the two characters before the cursor.</p>
<dt><code>em-next-word</code></p>
<dd>Move next to end of current word.</p>
<dt><code>em-upper-case</code></p>
<dd>Uppercase the characters from cursor to end of current word.</p>
<dt><code>em-capitol-case</code></p>
<dd>Capitalize the characters from cursor to end of current word.</p>
<dt><code>em-lower-case</code></p>
<dd>Lowercase the characters from cursor to end of current word.</p>
<dt><code>em-set-mark</code></p>
<dd>Set the mark at cursor.</p>
<dt><code>em-exchange-mark</code></p>
<dd>Exchange the cursor and mark.</p>
<dt><code>em-universal-argument</code></p>
<dd>Universal argument (argument times 4).</p>
<dt><code>em-meta-next</code></p>
<dd>Add 8th bit to next character typed.</p>
<dt><code>em-toggle-overwrite</code></p>
<dd>Switch from insert to overwrite mode or vice versa.</p>
<dt><code>em-copy-prev-word</code></p>
<dd>Copy current word to cursor.</p>
<dt><code>em-inc-search-next</code></p>
<dd>Emacs incremental next search.</p>
<dt><code>em-inc-search-prev</code></p>
<dd>Emacs incremental reverse search.</p>
<dt><code>ed-end-of-file</code></p>
<dd>Indicate end of file.</p>
<dt><code>ed-insert</code></p>
<dd>Add character to the line.</p>
<dt><code>ed-delete-prev-word</code></p>
<dd>Delete from beginning of current word to cursor.</p>
<dt><code>ed-delete-next-char</code></p>
<dd>Delete character under cursor.</p>
<dt><code>ed-kill-line</code></p>
<dd>Cut to the end of line.</p>
<dt><code>ed-move-to-end</code></p>
<dd>Move cursor to the end of line.</p>
<dt><code>ed-move-to-beg</code></p>
<dd>Move cursor to the beginning of line.</p>
<dt><code>ed-transpose-chars</code></p>
<dd>Exchange the character to the left of the cursor with the one under it.</p>
<dt><code>ed-next-char</code></p>
<dd>Move to the right one character.</p>
<dt><code>ed-prev-word</code></p>
<dd>Move to the beginning of the current word.</p>
<dt><code>ed-prev-char</code></p>
<dd>Move to the left one character.</p>
<dt><code>ed-quoted-insert</code></p>
<dd>Add the next character typed verbatim.</p>
<dt><code>ed-digit</code></p>
<dd>Adds to argument or enters a digit.</p>
<dt><code>ed-argument-digit</code></p>
<dd>Digit that starts argument.</p>
<dt><code>ed-unassigned</code></p>
<dd>Indicates unbound character.</p>
<dt><code>ed-tty-sigint</code></p>
<dd>Tty interrupt character.</p>
<dt><code>ed-tty-dsusp</code></p>
<dd>Tty delayed suspend character.</p>
<dt><code>ed-tty-flush-output</code></p>
<dd>Tty flush output characters.</p>
<dt><code>ed-tty-sigquit</code></p>
<dd>Tty quit character.</p>
<dt><code>ed-tty-sigtstp</code></p>
<dd>Tty suspend character.</p>
<dt><code>ed-tty-stop-output</code></p>
<dd>Tty disallow output characters.</p>
<dt><code>ed-tty-start-output</code></p>
<dd>Tty allow output characters.</p>
<dt><code>ed-newline</code></p>
<dd>Execute command.</p>
<dt><code>ed-delete-prev-char</code></p>
<dd>Delete the character to the left of the cursor.</p>
<dt><code>ed-clear-screen</code></p>
<dd>Clear screen leaving current line at the top.</p>
<dt><code>ed-redisplay</code></p>
<dd>Redisplay everything.</p>
<dt><code>ed-start-over</code></p>
<dd>Erase current line and start from scratch.</p>
<dt><code>ed-sequence-lead-in</code></p>
<dd>First character in a bound sequence.</p>
<dt><code>ed-prev-history</code></p>
<dd>Move to the previous history line.</p>
<dt><code>ed-next-history</code></p>
<dd>Move to the next history line.</p>
<dt><code>ed-search-prev-history</code></p>
<dd>Search previous in history for a line matching the current.</p>
<dt><code>ed-search-next-history</code></p>
<dd>Search next in history for a line matching the current.</p>
<dt><code>ed-prev-line</code></p>
<dd>Move up one line.</p>
<dt><code>ed-next-line</code></p>
<dd>Move down one line.</p>
<dt><code>ed-command</code></p>
<dd>Editline extended command.</dl>
<h2>Files</h2>
<dl>
<dt><code>~/.editrc </code></p>
<dd>User configuration file for the <a href="/docs/linux/man/3-editline/">editline</a>(3) library.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-editline/">editline</a>(3), <a href="/docs/linux/man/3-regex/">regex</a>(3), <a href="/docs/linux/man/5-termcap/">termcap</a>(5)</p>
<h2>Authors</h2>
<p>An -nosplit The <code>editline</code> library was written by An Christos Zoulas , and this manual was written by An Luke Mewburn , with some sections inspired by <a href="/docs/linux/man/1-tcsh/">tcsh</a>(1).</p>
