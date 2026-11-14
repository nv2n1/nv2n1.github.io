---
title: "mg(1)"
name: "mg"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mg/"
description: "mg – emacs-like text editor"
---

<h2>NAME</h2>
<p> <code>mg</code> &#8211; emacs-like text editor</p>
<h2>SYNOPSIS</h2>
<p> <code>mg</code> [-<code>n</code> ] [-<code>f </code><i>mode</i> ] [+ <i>number</i> ] [<i>file &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>mg</code> is intended to be a small, fast, and portable editor for people who can&#8217;t (or don&#8217;t want to) run emacs for one reason or another, or are not familiar with the <a href="/docs/linux/man/1-vi/">vi</a>(1) editor. It is compatible with emacs because there shouldn&#8217;t be any reason to learn more editor types than emacs or <a href="/docs/linux/man/1-vi/">vi</a>(1). </p>
<p> The options are as follows:</p>
<dl>
<dt><code>+ </code><i>number</i></p>
<dd> Go to the line specified by number (do not insert a space between the `+&#8217; sign and the number). If a negative number is specified, the line number counts backwards from the end of the file i.e. +-1 will be the last line of the file, +-2 will be second last, and so on.</p>
<dt><code>-f </code><i>mode</i></p>
<dd> Run the mode command for all buffers created from arguments on the command line, including the scratch buffer and all files.</p>
<dt><code>-n</code></p>
<dd> Turn off backup file generation.</dl>
<h2>WINDOWS AND BUFFERS</h2>
<p> When a file is loaded into <code>,</code> it is stored in a <i>buffer</i> This buffer may be displayed on the screen in more than one window. At present, windows may only be split horizontally, so each window is delineated by a modeline at the bottom. If changes are made to a buffer, it will be reflected in all open windows. </p>
<p> If a file is changed outside <code>mg</code> and its buffer is about to be changed, <code>mg</code> prompts if the change should go ahead (y), not go ahead (n) or if the buffer should be reverted (r) to the latest file on disk. </p>
<p> If a buffer name begins and ends with an asterisk, the buffer is considered throwaway; i.e. the user will not be prompted to save changes when the buffer is killed.</p>
<h2>POINT AND MARK</h2>
<p> The current cursor location in <code>mg</code> is called the <i>point</i> (or <i>dot )</i> It is possible to define a window-specific region of text by setting a second location, called the <i>mark</i> The <i>region</i> is the text between point and mark inclusive. Deleting the character at the mark position leaves the mark at the point of deletion. </p>
<p> Note: The point and mark are window-specific in <code>,</code> not buffer-specific, as in other emacs flavours.</p>
<h2>BACKUP FILES</h2>
<p> Backup files have a `~&#8217; character appended to the file name and are created in the current working directory by default. Whether to create backup files or not can be toggled with the make-backup-file command. The backup file location can either be in the current working directory, or all backups can be moved to a ~/.mg.d directory where files retain their path name to retain uniqueness. Use the backup-to-home-directory to alternate between these two locations. Further, if any application creates backup files in the <code>TMPDIR</code> these can be left with the leave-tmpdir-backups command.</p>
<h2>TAGS</h2>
<p> <code>mg</code> supports tag files created by <a href="/docs/linux/man/1-ctags/">ctags</a>(1), allowing the user to quickly locate various object definitions. Note though that emacs uses etags, not ctags.</p>
<h2>CSCOPE</h2>
<p> <code>mg</code> supports navigating source code using cscope. However, <code>mg</code> requires cscope and cscope-indexer executables to be present in <code>PATH</code> for it to work.</p>
<h2>DEFAULT KEY BINDINGS</h2>
<p> Normal editing commands are very similar to GNU Emacs. In the following examples, C-x means Control-x, and M-x means Meta-x, where the Meta key may be either a special key on the keyboard or the ALT key; otherwise ESC followed by the key X works as well. </p>
<dl>
<dt><code>C-SPC</code></p>
<dd> set-mark-command</p>
<dt><code>C-a</code></p>
<dd> beginning-of-line</p>
<dt><code>C-b</code></p>
<dd> backward-char</p>
<dt><code>C-c s c</code></p>
<dd> cscope-find-functions-calling-this-function</p>
<dt><code>C-c s d</code></p>
<dd> cscope-find-global-definition</p>
<dt><code>C-c s e</code></p>
<dd> cscope-find-egrep-pattern</p>
<dt><code>C-c s f</code></p>
<dd> cscope-find-this-file</p>
<dt><code>C-c s i</code></p>
<dd> cscope-find-files-including-file</p>
<dt><code>C-c s n</code></p>
<dd> cscope-next-symbol</p>
<dt><code>C-c s p</code></p>
<dd> cscope-prev-symbol</p>
<dt><code>C-c s s</code></p>
<dd> cscope-find-this-symbol</p>
<dt><code>C-c s t</code></p>
<dd> cscope-find-this-text-string</p>
<dt><code>C-d</code></p>
<dd> delete-char</p>
<dt><code>C-e</code></p>
<dd> end-of-line</p>
<dt><code>C-f</code></p>
<dd> forward-char</p>
<dt><code>C-g</code></p>
<dd> keyboard-quit</p>
<dt><code>C-h C-h</code></p>
<dd> help-help</p>
<dt><code>C-h a</code></p>
<dd> apropos</p>
<dt><code>C-h b</code></p>
<dd> describe-bindings</p>
<dt><code>C-h c</code></p>
<dd> describe-key-briefly</p>
<dt><code>C-j</code></p>
<dd> newline-and-indent</p>
<dt><code>C-k</code></p>
<dd> kill-line</p>
<dt><code>C-l</code></p>
<dd> recenter</p>
<dt><code>RET</code></p>
<dd> newline</p>
<dt><code>C-n</code></p>
<dd> next-line</p>
<dt><code>C-o</code></p>
<dd> open-line</p>
<dt><code>C-p</code></p>
<dd> previous-line</p>
<dt><code>C-q</code></p>
<dd> quoted-insert</p>
<dt><code>C-r</code></p>
<dd> isearch-backward</p>
<dt><code>C-s</code></p>
<dd> isearch-forward</p>
<dt><code>C-t</code></p>
<dd> transpose-chars</p>
<dt><code>C-u</code></p>
<dd> universal-argument</p>
<dt><code>C-v</code></p>
<dd> scroll-up</p>
<dt><code>C-w</code></p>
<dd> kill-region</p>
<dt><code>C-x C-b</code></p>
<dd> list-buffers</p>
<dt><code>C-x C-c</code></p>
<dd> save-buffers-kill-emacs</p>
<dt><code>C-x C-f</code></p>
<dd> find-file</p>
<dt><code>C-x C-g</code></p>
<dd> keyboard-quit</p>
<dt><code>C-x C-l</code></p>
<dd> downcase-region</p>
<dt><code>C-x C-o</code></p>
<dd> delete-blank-lines</p>
<dt><code>C-x C-q</code></p>
<dd> toggle-read-only</p>
<dt><code>C-x C-r</code></p>
<dd> find-file-read-only</p>
<dt><code>C-x C-s</code></p>
<dd> save-buffer</p>
<dt><code>C-x C-u</code></p>
<dd> upcase-region</p>
<dt><code>C-x C-v</code></p>
<dd> find-alternate-file</p>
<dt><code>C-x C-w</code></p>
<dd> write-file</p>
<dt><code>C-x C-x</code></p>
<dd> exchange-point-and-mark</p>
<dt><code>C-x</code></p>
<dd> start-kbd-macro</p>
<dt><code>C-x )</code></p>
<dd> end-kbd-macro</p>
<dt><code>C-x 0</code></p>
<dd> delete-window</p>
<dt><code>C-x 1</code></p>
<dd> delete-other-windows</p>
<dt><code>C-x 2</code></p>
<dd> split-window-vertically</p>
<dt><code>C-x 4 C-f</code></p>
<dd> find-file-other-window</p>
<dt><code>C-x 4 C-g</code></p>
<dd> keyboard-quit</p>
<dt><code>C-x 4 b</code></p>
<dd> switch-to-buffer-other-window</p>
<dt><code>C-x 4 f</code></p>
<dd> find-file-other-window</p>
<dt><code>C-x</code></p>
<dd> what-cursor-position</p>
<dt><code>C-x</code></p>
<dd> enlarge-window</p>
<dt><code>C-x</code></p>
<dd> next-error</p>
<dt><code>C-x b</code></p>
<dd> switch-to-buffer</p>
<dt><code>C-x d</code></p>
<dd> dired</p>
<dt><code>C-x e</code></p>
<dd> call-last-kbd-macro</p>
<dt><code>C-x f</code></p>
<dd> set-fill-column</p>
<dt><code>C-x g</code></p>
<dd> goto-line</p>
<dt><code>C-x h</code></p>
<dd> mark-whole-buffer</p>
<dt><code>C-x i</code></p>
<dd> insert-file</p>
<dt><code>C-x k</code></p>
<dd> kill-buffer</p>
<dt><code>C-x n</code></p>
<dd> other-window</p>
<dt><code>C-x o</code></p>
<dd> other-window</p>
<dt><code>C-x p</code></p>
<dd> previous-window</p>
<dt><code>C-x s</code></p>
<dd> save-some-buffers</p>
<dt><code>C-x u</code></p>
<dd> undo</p>
<dt><code>C-y</code></p>
<dd> yank</p>
<dt><code>C-z</code></p>
<dd> suspend-emacs</p>
<dt><code>M-C-v</code></p>
<dd> scroll-other-window</p>
<dt><code>M-SPC</code></p>
<dd> just-one-space</p>
<dt><code>M-!</code></p>
<dd> shell-command</p>
<dt><code>M-.</code></p>
<dd> find-tag</p>
<dt><code>M-*</code></p>
<dd> pop-tag-mark</p>
<dt><code>M-%</code></p>
<dd> query-replace</p>
<dt><code>M-&lt;</code></p>
<dd> beginning-of-buffer</p>
<dt><code>M-&gt;</code></p>
<dd> end-of-buffer</p>
<dt><code>M-\</code></p>
<dd> delete-horizontal-space</p>
<dt><code>M-^</code></p>
<dd> join-line</p>
<dt><code>M-b</code></p>
<dd> backward-word</p>
<dt><code>M-c</code></p>
<dd> capitalize-word</p>
<dt><code>M-d</code></p>
<dd> kill-word</p>
<dt><code>M-f</code></p>
<dd> forward-word</p>
<dt><code>M-l</code></p>
<dd> downcase-word</p>
<dt><code>M-m</code></p>
<dd> back-to-indentation</p>
<dt><code>M-q</code></p>
<dd> fill-paragraph</p>
<dt><code>M-r</code></p>
<dd> search-backward</p>
<dt><code>M-s</code></p>
<dd> search-forward</p>
<dt><code>M-u</code></p>
<dd> upcase-word</p>
<dt><code>M-v</code></p>
<dd> scroll-down</p>
<dt><code>M-w</code></p>
<dd> copy-region-as-kill</p>
<dt><code>M-x</code></p>
<dd> execute-extended-command</p>
<dt><code>M-{</code></p>
<dd> backward-paragraph</p>
<dt><code>M-|</code></p>
<dd> shell-command-on-region</p>
<dt><code>M-}</code></p>
<dd> forward-paragraph</p>
<dt><code>M-~</code></p>
<dd> not-modified</p>
<dt><code>M-DEL</code></p>
<dd> backward-kill-word</p>
<dt><code>C-_</code></p>
<dd> undo</p>
<dt><code>)</code></p>
<dd> blink-and-insert</p>
<dt><code>DEL</code></p>
<dd> delete-backward-char</dl>
<p> For a complete description of <code>mg</code> commands, see Sx MG COMMANDS . To see the active keybindings at any time, type &#8220;M-x describe-bindings&#8221;</p>
<h2>MG COMMANDS</h2>
<p> Commands are invoked by &#8220;M-x&#8221; or by binding to a key. Many commands take an optional numerical parameter, <i>n</i> This parameter is set either by M-&lt;n&gt; (where <i>n</i> is the numerical argument) before the command, or by one or more invocations of the universal argument, usually bound to C-u. When invoked in this manner, the value of the numeric parameter to be passed is displayed in the minibuffer before the M-x. One common use of the parameter is in mode toggles (e.g. make-backup-files). If no parameter is supplied, the mode is toggled to its alternate state. If a positive parameter is supplied, the mode is forced to on. Otherwise, it is forced to off.</p>
<dl>
<dt><code>apropos</code></p>
<dd> Help Apropos. Prompt the user for a string, open the *help* buffer, and list all <code>mg</code> commands that contain that string.</p>
<dt><code>audible-bell</code></p>
<dd> Toggle the audible system bell.</p>
<dt><code>auto-execute</code></p>
<dd> Register an auto-execute hook; that is, specify a filename pattern (conforming to the shell&#8217;s filename globbing rules) and an associated function to execute when a file matching the specified pattern is read into a buffer.</p>
<dt><code>auto-fill-mode</code></p>
<dd> Toggle auto-fill mode (sometimes called mail-mode), where text inserted past the fill column is automatically wrapped to a new line.</p>
<dt><code>auto-indent-mode</code></p>
<dd> Toggle indent mode, where indentation is preserved after a newline.</p>
<dt><code>back-to-indentation</code></p>
<dd> Move the dot to the first non-whitespace character on the current line.</p>
<dt><code>backup-to-home-directory</code></p>
<dd> Save backup copies to a ~/.mg.d directory instead of working directory. Requires make-backup-files to be on.</p>
<dt><code>backward-char</code></p>
<dd> Move cursor backwards one character.</p>
<dt><code>backward-kill-word</code></p>
<dd> Kill text backwards by <i>n</i> words.</p>
<dt><code>backward-paragraph</code></p>
<dd> Move cursor backwards <i>n</i> paragraphs. Paragraphs are delimited by &lt;NL&gt;&lt;NL&gt; or &lt;NL&gt;&lt;TAB&gt; or &lt;NL&gt;&lt;SPACE&gt;.</p>
<dt><code>backward-word</code></p>
<dd> Move cursor backwards by the specified number of words.</p>
<dt><code>beginning-of-buffer</code></p>
<dd> Move cursor to the top of the buffer.</p>
<dt><code>beginning-of-line</code></p>
<dd> Move cursor to the beginning of the line.</p>
<dt><code>blink-and-insert</code></p>
<dd> Self-insert a character, then search backwards and blink its matching delimiter. For delimiters other than parenthesis, brackets, and braces, the character itself is used as its own match.</p>
<dt><code>bsmap-mode</code></p>
<dd> Toggle bsmap mode, where DEL and C-h are swapped.</p>
<dt><code>c-mode</code></p>
<dd> Toggle a KNF-compliant mode for editing C program files.</p>
<dt><code>call-last-kbd-macro</code></p>
<dd> Invoke the keyboard macro.</p>
<dt><code>capitalize-word</code></p>
<dd> Capitalize <i>n</i> words; i.e. convert the first character of the word to upper case, and subsequent letters to lower case.</p>
<dt><code>cd</code></p>
<dd> Change the global working directory. See also global-wd-mode.</p>
<dt><code>column-number-mode</code></p>
<dd> Toggle whether the column number is displayed in the modeline.</p>
<dt><code>copy-region-as-kill</code></p>
<dd> Copy all of the characters in the region to the kill buffer, clearing the mark afterwards. This is a bit like a kill-region followed by a yank.</p>
<dt><code>count-matches</code></p>
<dd> Count the number of lines matching the supplied regular expression.</p>
<dt><code>count-non-matches</code></p>
<dd> Count the number of lines not matching the supplied regular expression.</p>
<dt><code>cscope-find-this-symbol</code></p>
<dd> List the matches for the given symbol.</p>
<dt><code>cscope-find-global-definition</code></p>
<dd> List global definitions for the given literal.</p>
<dt><code>cscope-find-called-functions</code></p>
<dd> List functions called from the given function.</p>
<dt><code>cscope-find-functions-calling-this-function</code></p>
<dd> List functions calling the given function.</p>
<dt><code>cscope-find-this-text-string</code></p>
<dd> List locations matching the given text string.</p>
<dt><code>cscope-find-egrep-pattern</code></p>
<dd> List locations matching the given extended regular expression pattern.</p>
<dt><code>cscope-find-this-file</code></p>
<dd> List filenames matching the given filename.</p>
<dt><code>cscope-find-files-including-file</code></p>
<dd> List files that #include the given filename.</p>
<dt><code>cscope-next-symbol</code></p>
<dd> Navigate to the next match.</p>
<dt><code>cscope-prev-symbol</code></p>
<dd> Navigate to the previous match.</p>
<dt><code>cscope-next-file</code></p>
<dd> Navigate to the next file.</p>
<dt><code>cscope-prev-file</code></p>
<dd> Navigate to the previous file.</p>
<dt><code>cscope-create-list-of-files-to-index</code></p>
<dd> Create cscope&#8217;s List and Index in the given directory.</p>
<dt><code>define-key</code></p>
<dd> Prompts the user for a named keymap (mode), a key, and an <code>mg</code> command, then creates a keybinding in the appropriate map.</p>
<dt><code>delete-backward-char</code></p>
<dd> Delete backwards <i>n</i> characters. Like delete-char, this actually does a kill if presented with an argument.</p>
<dt><code>delete-blank-lines</code></p>
<dd> Delete blank lines around dot. If dot is sitting on a blank line, this command deletes all the blank lines above and below the current line. Otherwise, it deletes all of the blank lines after the current line.</p>
<dt><code>delete-char</code></p>
<dd> Delete <i>n</i> characters forward. If any argument is present, it kills rather than deletes, saving the result in the kill buffer.</p>
<dt><code>delete-horizontal-space</code></p>
<dd> Delete any whitespace around the dot.</p>
<dt><code>delete-leading-space</code></p>
<dd> Delete leading whitespace on the current line.</p>
<dt><code>delete-trailing-space</code></p>
<dd> Delete trailing whitespace on the current line.</p>
<dt><code>delete-matching-lines</code></p>
<dd> Delete all lines after dot that contain a string matching the supplied regular expression.</p>
<dt><code>delete-non-matching-lines</code></p>
<dd> Delete all lines after dot that contain a string matching the supplied regular expression.</p>
<dt><code>delete-other-windows</code></p>
<dd> Make the current window the only window visible on the screen.</p>
<dt><code>delete-window</code></p>
<dd> Delete current window.</p>
<dt><code>describe-bindings</code></p>
<dd> List all global and local keybindings, putting the result in the *help* buffer.</p>
<dt><code>describe-key-briefly</code></p>
<dd> Read a key from the keyboard, and look it up in the keymap. Display the name of the function currently bound to the key.</p>
<dt><code>diff-buffer-with-file</code></p>
<dd> View the differences between buffer and its associated file.</p>
<dt><code>digit-argument</code></p>
<dd> Process a numerical argument for keyboard-invoked functions.</p>
<dt><code>downcase-region</code></p>
<dd> Set all characters in the region to lower case.</p>
<dt><code>downcase-word</code></p>
<dd> Set characters to lower case, starting at the dot, and ending <i>n</i> words away.</p>
<dt><code>emacs-version</code></p>
<dd> Return an <code>mg</code> version string.</p>
<dt><code>end-kbd-macro</code></p>
<dd> Stop defining a keyboard macro.</p>
<dt><code>end-of-buffer</code></p>
<dd> Move cursor to the end of the buffer.</p>
<dt><code>end-of-line</code></p>
<dd> Move cursor to the end of the line.</p>
<dt><code>enlarge-window</code></p>
<dd> Enlarge the current window by shrinking either the window above or below it.</p>
<dt><code>eval-current-buffer</code></p>
<dd> Evaluate the current buffer as a series of <code>mg</code> commands. Useful for testing <code>mg</code> startup files.</p>
<dt><code>eval-expression</code></p>
<dd> Get one line from the user, and run it. Useful for testing expressions in <code>mg</code> startup files.</p>
<dt><code>exchange-point-and-mark</code></p>
<dd> Swap the values of &quot;dot&quot; and &quot;mark&quot; in the current window. Return an error if no mark is set.</p>
<dt><code>execute-extended-command</code></p>
<dd> Invoke an extended command; i.e. M-x. Call the message line routine to read in the command name and apply autocompletion to it. When it comes back, look the name up in the symbol table and run the command if it is found, passing arguments as necessary. Print an error if there is anything wrong.</p>
<dt><code>fill-paragraph</code></p>
<dd> Justify a paragraph, wrapping text at the current fill column.</p>
<dt><code>find-file</code></p>
<dd> Select a file for editing. First check if the file can be found in another buffer; if it is there, just switch to that buffer. If the file cannot be found, create a new buffer, read in the file from disk, and switch to the new buffer.</p>
<dt><code>find-file-read-only</code></p>
<dd> Same as find-file, except the new buffer is set to read-only.</p>
<dt><code>find-alternate-file</code></p>
<dd> Replace the current file with an alternate one. Semantics for finding the replacement file are the same as find-file, except the current buffer is killed before the switch. If the kill fails, or is aborted, revert to the original file.</p>
<dt><code>find-file-other-window</code></p>
<dd> Opens the specified file in a second buffer. Splits the current window if necessary.</p>
<dt><code>find-tag</code></p>
<dd> Jump to definition of tag at dot.</p>
<dt><code>forward-char</code></p>
<dd> Move cursor forwards (or backwards, if <i>n</i> is negative) <i>n</i> characters. Returns an error if the end of buffer is reached.</p>
<dt><code>forward-paragraph</code></p>
<dd> Move forward <i>n</i> paragraphs. Paragraphs are delimited by &lt;NL&gt;&lt;NL&gt; or &lt;NL&gt;&lt;TAB&gt; or &lt;NL&gt;&lt;SPACE&gt;.</p>
<dt><code>forward-word</code></p>
<dd> Move the cursor forward by the specified number of words.</p>
<dt><code>global-set-key</code></p>
<dd> Bind a key in the global (fundamental) key map.</p>
<dt><code>global-unset-key</code></p>
<dd> Unbind a key from the global (fundamental) key map; i.e. set it to &#8216;rescan&#8217;.</p>
<dt><code>global-wd-mode</code></p>
<dd> Toggle global working-directory mode. When enabled, <code>mg</code> defaults to opening files (and executing commands like compile and grep) relative to the global working directory. When disabled, a working directory is set for each buffer.</p>
<dt><code>goto-line</code></p>
<dd> Go to a specific line. If an argument is present, then it is the line number, else prompt for a line number to use.</p>
<dt><code>help-help</code></p>
<dd> Prompts for one of (a)propos, (b)indings, des(c)ribe key briefly.</p>
<dt><code>insert</code></p>
<dd> Insert a string, mainly for use from macros.</p>
<dt><code>insert-buffer</code></p>
<dd> Insert the contents of another buffer at dot.</p>
<dt><code>insert-file</code></p>
<dd> Insert a file into the current buffer at dot.</p>
<dt><code>insert-with-wrap</code></p>
<dd> Insert the bound character with word wrap. Check to see if we&#8217;re past the fill column, and if so, justify this line.</p>
<dt><code>isearch-backward</code></p>
<dd> Use incremental searching, initially in the reverse direction. isearch ignores any explicit arguments. If invoked during macro definition or evaluation, the non-incremental search-backward is invoked instead.</p>
<dt><code>isearch-forward</code></p>
<dd> Use incremental searching, initially in the forward direction. isearch ignores any explicit arguments. If invoked during macro definition or evaluation, the non-incremental search-forward is invoked instead.</p>
<dt><code>join-line</code></p>
<dd> Join the current line to the previous. If called with an argument, join the next line to the current one.</p>
<dt><code>just-one-space</code></p>
<dd> Delete any whitespace around dot, then insert a space.</p>
<dt><code>keyboard-quit</code></p>
<dd> Abort the current action.</p>
<dt><code>kill-buffer</code></p>
<dd> Dispose of a buffer, by name. If the buffer name does not start and end with an asterisk, prompt the user if the buffer has been changed.</p>
<dt><code>kill-line</code></p>
<dd> Kill line. If called without an argument, it kills from dot to the end of the line, unless it is at the end of the line, when it kills the newline. If called with an argument of 0, it kills from the start of the line to dot. If called with a positive argument, it kills from dot forward over that number of newlines. If called with a negative argument it kills any text before dot on the current line, then it kills back <a href="/docs/linux/man/n-abs/">abs</a>(n) lines.</p>
<dt><code>kill-paragraph</code></p>
<dd> Delete <i>n</i> paragraphs starting with the current one.</p>
<dt><code>kill-region</code></p>
<dd> Kill the currently defined region.</p>
<dt><code>kill-word</code></p>
<dd> Delete forward <i>n</i> words.</p>
<dt><code>leave-tmpdir-backups</code></p>
<dd> Modifies the behaviour of backup-to-home-directory. Backup files that would normally reside in the system <code>TMPDIR</code> are left there and not moved to the ~/.mg.d directory.</p>
<dt><code>line-number-mode</code></p>
<dd> Toggle whether the line number is displayed in the modeline.</p>
<dt><code>list-buffers</code></p>
<dd> Display the list of available buffers.</p>
<dt><code>load</code></p>
<dd> Prompt the user for a filename, and then execute commands from that file.</p>
<dt><code>local-set-key</code></p>
<dd> Bind a key mapping in the local (topmost) mode.</p>
<dt><code>local-unset-key</code></p>
<dd> Unbind a key mapping in the local (topmost) mode.</p>
<dt><code>make-backup-files</code></p>
<dd> Toggle generation of backup files.</p>
<dt><code>make-directory</code></p>
<dd> Prompt the user for a path or directory name which is then created.</p>
<dt><code>mark-whole-buffer</code></p>
<dd> Marks whole buffer as a region by putting dot at the beginning and mark at the end of buffer.</p>
<dt><code>meta-key-mode</code></p>
<dd> When disabled, the meta key can be used to insert extended-ascii (8-bit) characters. When enabled, the meta key acts as usual.</p>
<dt><code>negative-argument</code></p>
<dd> Process a negative argument for keyboard-invoked functions.</p>
<dt><code>newline</code></p>
<dd> Insert a newline into the current buffer.</p>
<dt><code>newline-and-indent</code></p>
<dd> Insert a newline, then enough tabs and spaces to duplicate the indentation of the previous line. Assumes tabs are every eight characters.</p>
<dt><code>next-line</code></p>
<dd> Move forward <i>n</i> lines.</p>
<dt><code>no-tab-mode</code></p>
<dd> Toggle notab mode. In this mode, spaces are inserted rather than tabs.</p>
<dt><code>not-modified</code></p>
<dd> Turn off the modified flag in the current buffer.</p>
<dt><code>open-line</code></p>
<dd> Open up some blank space. Essentially, insert <i>n</i> newlines, then back up over them.</p>
<dt><code>other-window</code></p>
<dd> The command to make the next (down the screen) window the current window. There are no real errors, although the command does nothing if there is only 1 window on the screen.</p>
<dt><code>overwrite-mode</code></p>
<dd> Toggle overwrite mode, where typing in a buffer overwrites existing characters rather than inserting them.</p>
<dt><code>prefix-region</code></p>
<dd> Inserts a prefix string before each line of a region. The prefix string is settable by using &#8216;set-prefix-string&#8217;.</p>
<dt><code>previous-line</code></p>
<dd> Move backwards <i>n</i> lines.</p>
<dt><code>previous-window</code></p>
<dd> This command makes the previous (up the screen) window the current window. There are no errors, although the command does not do a lot if there is only 1 window.</p>
<dt><code>pop-tag-mark</code></p>
<dd> Return to position where find-tag was previously invoked.</p>
<dt><code>push-shell</code></p>
<dd> Suspend <code>mg</code> and switch to alternate screen, if available.</p>
<dt><code>pwd</code></p>
<dd> Display current (global) working directory in the status area.</p>
<dt><code>query-replace</code></p>
<dd> Query Replace. Search and replace strings selectively, prompting after each match.</p>
<dt><code>replace-string</code></p>
<dd> Replace string globally without individual prompting.</p>
<dt><code>query-replace-regexp</code></p>
<dd> Replace strings selectively. Does a search and replace operation using regular expressions for both patterns.</p>
<dt><code>quoted-insert</code></p>
<dd> Insert the next character verbatim into the current buffer; i.e. ignore any function bound to that key.</p>
<dt><code>re-search-again</code></p>
<dd> Perform a regular expression search again, using the same search string and direction as the last search command.</p>
<dt><code>re-search-backward</code></p>
<dd> Search backwards using a regular expression. Get a search string from the user, and search, starting at dot and proceeding toward the front of the buffer. If found, dot is left pointing at the first character of the pattern [the last character that was matched].</p>
<dt><code>re-search-forward</code></p>
<dd> Search forward using a regular expression. Get a search string from the user and search for it starting at dot. If found, move dot to just after the matched characters. display does all the hard stuff. If not found, it just prints a message.</p>
<dt><code>recenter</code></p>
<dd> Reposition dot in the current window. By default, the dot is centered. If given a positive argument (n), the display is repositioned to line n. If <i>n</i> is negative, it is that line from the bottom.</p>
<dt><code>redraw-display</code></p>
<dd> Refresh the display. Recomputes all window sizes in case something has changed.</p>
<dt><code>revert-buffer</code></p>
<dd> Revert the current buffer to the latest file on disk.</p>
<dt><code>save-buffer</code></p>
<dd> Save the contents of the current buffer if it has been changed, optionally creating a backup copy.</p>
<dt><code>save-buffers-kill-emacs</code></p>
<dd> Offer to save modified buffers and quit <code>.</code></p>
<dt><code>save-some-buffers</code></p>
<dd> Look through the list of buffers, offering to save any buffer that has been changed. Buffers that are not associated with files (such as *scratch*, *grep*, *compile*) are ignored.</p>
<dt><code>scroll-down</code></p>
<dd> Scroll backwards <i>n</i> pages. A two-line overlap between pages is assumed. If given a repeat argument, scrolls back lines, not pages.</p>
<dt><code>scroll-one-line-down</code></p>
<dd> Scroll the display down <i>n</i> lines without changing the cursor position.</p>
<dt><code>scroll-one-line-up</code></p>
<dd> Scroll the display <i>n</i> lines up without moving the cursor position.</p>
<dt><code>scroll-other-window</code></p>
<dd> Scroll the next window in the window list window forward <i>n</i> pages.</p>
<dt><code>scroll-up</code></p>
<dd> Scroll forward one page. A two-line overlap between pages is assumed. If given a repeat argument, scrolls back lines, not pages.</p>
<dt><code>search-again</code></p>
<dd> Search again, using the same search string and direction as the last search command.</p>
<dt><code>search-backward</code></p>
<dd> Reverse search. Get a search string from the user, and search, starting at dot and proceeding toward the front of the buffer. If found, dot is left pointing at the first character of the pattern (the last character that was matched).</p>
<dt><code>search-forward</code></p>
<dd> Search forward. Get a search string from the user, and search for it starting at dot. If found, dot gets moved to just after the matched characters, if not found, print a message.</p>
<dt><code>self-insert-command</code></p>
<dd> Insert a character.</p>
<dt><code>set-case-fold-search</code></p>
<dd> Set case-fold searching, causing case not to matter in regular expression searches. This is the default.</p>
<dt><code>set-default-mode</code></p>
<dd> Append the supplied mode to the list of default modes used by subsequent buffer creation. Built in modes include: fill, indent, overwrite, and notab.</p>
<dt><code>set-fill-column</code></p>
<dd> Prompt the user for a fill column. Used by auto-fill-mode.</p>
<dt><code>set-mark-command</code></p>
<dd> Sets the mark in the current window to the current dot location.</p>
<dt><code>set-prefix-string</code></p>
<dd> Sets the prefix string to be used by the &#8216;prefix-region&#8217; command.</p>
<dt><code>shell-command</code></p>
<dd> Execute external command from mini-buffer.</p>
<dt><code>shell-command-on-region</code></p>
<dd> Provide the text in region to the shell command as input.</p>
<dt><code>shrink-window</code></p>
<dd> Shrink current window by one line. The window immediately below is expanded to pick up the slack. If only one window is present, this command has no effect.</p>
<dt><code>space-to-tabstop</code></p>
<dd> Insert enough spaces to reach the next tab-stop position. By default, tab-stops occur every 8 characters.</p>
<dt><code>split-window-vertically</code></p>
<dd> Split the current window. A window smaller than 3 lines cannot be split.</p>
<dt><code>start-kbd-macro</code></p>
<dd> Start defining a keyboard macro. Macro definition is ended by invoking end-kbd-macro.</p>
<dt><code>suspend-emacs</code></p>
<dd> Suspend <code>mg</code> and switch back to alternate screen, if in use.</p>
<dt><code>switch-to-buffer</code></p>
<dd> Prompt and switch to a new buffer in the current window.</p>
<dt><code>switch-to-buffer-other-window</code></p>
<dd> Switch to buffer in another window.</p>
<dt><code>toggle-read-only</code></p>
<dd> Toggle the read-only flag on the current buffer.</p>
<dt><code>transpose-chars</code></p>
<dd> Transpose the two characters in front of and under dot, then move forward one character. Treat newline characters the same as any other.</p>
<dt><code>undo</code></p>
<dd> Undo the most recent action. If invoked again without an intervening command, move the undo pointer to the previous action and undo it.</p>
<dt><code>undo-boundary</code></p>
<dd> Add an undo boundary. This is not usually done interactively.</p>
<dt><code>undo-boundary-toggle</code></p>
<dd> Toggle whether undo boundaries are generated. Undo boundaries are often disabled before operations that should be considered atomically undoable.</p>
<dt><code>undo-enable</code></p>
<dd> Toggle whether undo information is kept.</p>
<dt><code>undo-list</code></p>
<dd> Show the undo records for the current buffer in a new buffer.</p>
<dt><code>universal-argument</code></p>
<dd> Repeat the next command 4 times. Usually bound to C-u. This command may be stacked; e.g. C-u C-u C-f moves the cursor forward 16 characters.</p>
<dt><code>upcase-region</code></p>
<dd> Upper case region. Change all of the lower case characters in the region to upper case.</p>
<dt><code>upcase-word</code></p>
<dd> Move the cursor forward by the specified number of words. As it moves, convert any characters to upper case.</p>
<dt><code>visible-bell</code></p>
<dd> Toggle the visible bell. If this toggle is on, the modeline will flash.</p>
<dt><code>visit-tags-table</code></p>
<dd> Record name of the tags file to be used for subsequent find-tag.</p>
<dt><code>what-cursor-position</code></p>
<dd> Display a bunch of useful information about the current location of dot. The character under the cursor (in octal), the current line, row, and column, and approximate position of the cursor in the file (as a percentage) is displayed. The column position assumes an infinite position display; it does not truncate just because the screen does.</p>
<dt><code>write-file</code></p>
<dd> Ask for a file name and write the contents of the current buffer to that file. Update the remembered file name and clear the buffer changed flag.</p>
<dt><code>yank</code></p>
<dd> Yank text from kill-buffer. Unlike emacs, the <code>mg</code> kill buffer consists only of the most recent kill. It is not a ring.</dl>
<h2>MG DIRED KEY BINDINGS</h2>
<p> Specific key bindings are available in dired mode. </p>
<dl>
<dt><code>DEL</code></p>
<dd> dired-unmark-backward</p>
<dt><code>SPC</code></p>
<dd> dired-next-line</p>
<dt><code>!</code></p>
<dd> dired-shell-command</p>
<dt><code>+</code></p>
<dd> dired-create-directory</p>
<dt><code>c</code></p>
<dd> dired-do-copy</p>
<dt><code>d and C-d</code></p>
<dd> dired-flag-file-deletion</p>
<dt><code>e, f and C-m</code></p>
<dd> dired-find-file</p>
<dt><code>g</code></p>
<dd> dired-revert</p>
<dt><code>n</code></p>
<dd> dired-next-line</p>
<dt><code>o</code></p>
<dd> dired-find-file-other-window</p>
<dt><code>p</code></p>
<dd> dired-previous-line</p>
<dt><code>q</code></p>
<dd> quit-window</p>
<dt><code>r</code></p>
<dd> dired-do-rename</p>
<dt><code>u</code></p>
<dd> dired-unmark</p>
<dt><code>x</code></p>
<dd> dired-do-flagged-delete</p>
<dt><code>C-v</code></p>
<dd> dired-scroll-down</p>
<dt><code>M-v</code></p>
<dd> dired-scroll-up</dl>
<h2>MG DIRED COMMANDS</h2>
<p> The following are a list of the commands specific to dired mode:</p>
<dl>
<dt><code>dired-create-directory</code></p>
<dd> Create a directory.</p>
<dt><code>dired-do-copy</code></p>
<dd> Copy the file listed on the current line of the dired buffer.</p>
<dt><code>dired-do-flagged-delete</code></p>
<dd> Delete the files that have been flagged for deletion.</p>
<dt><code>dired-do-rename</code></p>
<dd> Rename the file listed on the current line of the dired buffer.</p>
<dt><code>dired-find-file</code></p>
<dd> Open the file on the current line of the dired buffer. If the cursor is on a directory it will be opened in dired mode.</p>
<dt><code>dired-flag-file-deletion</code></p>
<dd> Flag the file listed on the current line for deletion. This is indicated in the buffer by putting a D at the left margin. No files are actually deleted until the function dired-do-deletions is executed.</p>
<dt><code>dired-find-file-other-window</code></p>
<dd> Open the file on the current line of the dired buffer in a different window.</p>
<dt><code>dired-next-line</code></p>
<dd> Move the cursor to the next line.</p>
<dt><code>dired-other-window</code></p>
<dd> This function works just like dired, except that it puts the dired buffer in another window.</p>
<dt><code>dired-previous-line</code></p>
<dd> Move the cursor to the previous line.</p>
<dt><code>dired-revert</code></p>
<dd> Refresh the dired buffer.</p>
<dt><code>dired-scroll-down</code></p>
<dd> Scroll down the dired buffer.</p>
<dt><code>dired-scroll-up</code></p>
<dd> Scroll up the dired buffer.</p>
<dt><code>dired-unmark</code></p>
<dd> Remove the deletion flag for the file on the current line.</p>
<dt><code>dired-unmark-backward</code></p>
<dd> Remove the deletion flag from the file listed on the previous line of the dired buffer, then move up to that line.</p>
<dt><code>quit-window</code></p>
<dd> Close the current dired buffer.</dl>
<h2>CONFIGURATION FILES</h2>
<p> There are two configuration files, .mg and .mg-TERM Here, <code>TERM</code> represents the name of the terminal type; e.g. if the terminal type is set to &#8220;vt100&#8221; <code>mg</code> will use .mg-vt100 as a startup file. The terminal type startup file is used first. </p>
<p> The startup file format is a list of commands, one per line, as used for interactive evaluation. Strings that are normally entered by the user at any subsequent prompts may be specified after the command name; e.g.: </p>
<blockquote>
<pre>
global-set-key &quot;)&quot; self-insert-command
global-set-key &quot;\^x\^f&quot; find-file
global-set-key &quot;[Z&quot; backward-char
set-default-mode fill
set-fill-column 72
auto-execute *.c c-mode
</pre>
</blockquote>
<p> Comments can be added to the startup files by placing &#8220;;&#8221; or &#8220;#&#8221; as the first character of a line.</p>
<h2>FILES</h2>
<dl>
<dt><code>~/.mg </code></p>
<dd> normal startup file</p>
<dt><code>~/.mg-TERM </code></p>
<dd> terminal-specific startup file</p>
<dt><code>~/.mg.d </code></p>
<dd> alternative backup file location</p>
<dt><code>/usr/share/doc/mg/tutorial </code></p>
<dd> concise tutorial</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ctags/">ctags</a>(1), <a href="/docs/linux/man/1-vi/">vi</a>(1)</p>
<h2>CAVEATS</h2>
<p> Since it is written completely in C, there is currently no language in which extensions can be written; however, keys can be rebound and certain parameters can be changed in startup files. </p>
<p> In order to use 8-bit characters (such as German umlauts), the Meta key needs to be disabled via the &#8220;meta-key-mode&#8221; command. </p>
<p> Multi-byte character sets, such as UTF-8, are not supported. </p>
<h2>Index</h2>
