---
title: "tcsh(1)"
name: "tcsh"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcsh/"
description: "tcsh – C shell with file name completion and command line editing"
---

<h2>NAME</h2>
<p> tcsh &#8211; C shell with file name completion and command line editing</p>
<h2>SYNOPSIS</h2>
<p> <code>tcsh </code>[<code>-bcdefFimnqstvVxX</code>] [<code>-Dname</code>[<code>=value</code>]] [arg &#8230;]<br />
 <code>tcsh -l</code></p>
<h2>DESCRIPTION</h2>
<p> <i>tcsh</i> is an enhanced but completely compatible version of the Berkeley UNIX C shell, <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1). It is a command language interpreter usable both as an interactive login shell and a shell script command processor. It includes a command-line editor (see <code>The command-line editor</code>), programmable word completion (see <code>Completion and listing</code>), spelling correction (see <code>Spelling correction</code>), a history mechanism (see <code>History substitution</code>), job control (see <code>Jobs</code>) and a C-like syntax. The <code>NEW FEATURES</code> section describes major enhancements of <i>tcsh</i> over <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1). Throughout this manual, features of <i>tcsh</i> not found in most <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1) implementations (specifically, the 4.4BSD <i>csh</i>) are labeled with `(+)&#8217;, and features which are present in <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1) but not usually documented are labeled with `(u)&#8217;.</p>
<h3>Argument list processing</h3>
<p> If the first argument (argument 0) to the shell is `-&#8216; then it is a login shell. A login shell can be also specified by invoking the shell with the <code>-l</code> flag as the only argument. </p>
<p> The rest of the flag arguments are interpreted as follows:</p>
<dl>
<dt><code>-b</code></p>
<dd> Forces a &#8220;break&#8221; from option processing, causing any further shell arguments to be treated as non-option arguments. The remaining arguments will not be interpreted as shell options. This may be used to pass options to a shell script without confusion or possible subterfuge. The shell will not run a set-user ID script without this option.</p>
<dt><code>-c</code></p>
<dd> Commands are read from the following argument (which must be present, and must be a single argument), stored in the <code>command</code> shell variable for reference, and executed. Any remaining arguments are placed in the <code>argv</code> shell variable.</p>
<dt><code>-d</code></p>
<dd> The shell loads the directory stack from <i>~/.cshdirs</i> as described under <code>Startup and shutdown</code>, whether or not it is a login shell. (+)</p>
<dt><code>-D</code><i>name</i>[=<i>value</i>]</p>
<dd> Sets the environment variable <i>name</i> to <i>value</i>. (Domain/OS only) (+)</p>
<dt><code>-e</code></p>
<dd> The shell exits if any invoked command terminates abnormally or yields a non-zero exit status.</p>
<dt><code>-f</code></p>
<dd> The shell does not load any resource or startup files, or perform any command hashing, and thus starts faster.</p>
<dt><code>-F</code></p>
<dd> The shell uses <i><a href="/docs/linux/man/2-fork/">fork</a></i>(2) instead of <i><a href="/docs/linux/man/2-vfork/">vfork</a></i>(2) to spawn processes. (+)</p>
<dt><code>-i</code></p>
<dd> The shell is interactive and prompts for its top-level input, even if it appears to not be a terminal. Shells are interactive without this option if their inputs and outputs are terminals.</p>
<dt><code>-l</code></p>
<dd> The shell is a login shell. Applicable only if <code>-l</code> is the only flag specified.</p>
<dt><code>-m</code></p>
<dd> The shell loads <i>~/.tcshrc</i> even if it does not belong to the effective user. Newer versions of <i><a href="/docs/linux/man/1-su/">su</a></i>(1) can pass <code>-m</code> to the shell. (+)</p>
<dt><code>-n</code></p>
<dd> The shell parses commands but does not execute them. This aids in debugging shell scripts.</p>
<dt><code>-q</code></p>
<dd> The shell accepts SIGQUIT (see <code>Signal handling</code>) and behaves when it is used under a debugger. Job control is disabled. (u)</p>
<dt><code>-s</code></p>
<dd> Command input is taken from the standard input.</p>
<dt><code>-t</code></p>
<dd> The shell reads and executes a single line of input. A `\&#8217; may be used to escape the newline at the end of this line and continue onto another line.</p>
<dt><code>-v</code></p>
<dd> Sets the <code>verbose</code> shell variable, so that command input is echoed after history substitution.</p>
<dt><code>-x</code></p>
<dd> Sets the <code>echo</code> shell variable, so that commands are echoed immediately before execution.</p>
<dt><code>-V</code></p>
<dd> Sets the <code>verbose</code> shell variable even before executing <i>~/.tcshrc</i>.</p>
<dt><code>-X</code></p>
<dd> Is to <code>-x</code> as <code>-V</code> is to <code>-v</code>.</p>
<dt><code>&#8211;help</code></p>
<dd> Print a help message on the standard output and exit. (+)</p>
<dt><code>&#8211;version</code></p>
<dd> Print the version/platform/compilation options on the standard output and exit. This information is also contained in the <code>version</code> shell variable. (+)</dl>
<p> After processing of flag arguments, if arguments remain but none of the <code>-c</code>, <code>-i</code>, <code>-s</code>, or <code>-t</code> options were given, the first argument is taken as the name of a file of commands, or &#8220;script&#8221;, to be executed. The shell opens this file and saves its name for possible resubstitution by `$0&#8242;. Because many systems use either the standard version 6 or version 7 shells whose shell scripts are not compatible with this shell, the shell uses such a `standard&#8217; shell to execute a script whose first character is not a `#&#8217;, i.e., that does not start with a comment. </p>
<p> Remaining arguments are placed in the <code>argv</code> shell variable.</p>
<h3>Startup and shutdown</h3>
<p> A login shell begins by executing commands from the system files <i>/etc/csh.cshrc</i> and <i>/etc/csh.login</i>. It then executes commands from files in the user&#8217;s <code>home</code> directory: first <i>~/.tcshrc</i> (+) or, if <i>~/.tcshrc</i> is not found, <i>~/.cshrc</i>, then <i>~/.history</i> (or the value of the <code>histfile</code> shell variable), then <i>~/.login</i>, and finally <i>~/.cshdirs</i> (or the value of the <code>dirsfile</code> shell variable) (+). The shell may read <i>/etc/csh.login</i> before instead of after <i>/etc/csh.cshrc</i>, and <i>~/.login</i> before instead of after <i>~/.tcshrc</i> or <i>~/.cshrc</i> and <i>~/.history</i>, if so compiled; see the <code>version</code> shell variable. (+) </p>
<p> Non-login shells read only <i>/etc/csh.cshrc</i> and <i>~/.tcshrc</i> or <i>~/.cshrc</i> on startup. </p>
<p> For examples of startup files, please consult <i><a rel="nofollow" href="http://tcshrc.sourceforge.net">http://tcshrc.sourceforge.net</a></i>. </p>
<p> Commands like <i><a href="/docs/linux/man/1-stty/">stty</a></i>(1) and <i><a href="/docs/linux/man/1-tset/">tset</a></i>(1), which need be run only once per login, usually go in one&#8217;s <i>~/.login</i> file. Users who need to use the same set of files with both <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1) and <i>tcsh</i> can have only a <i>~/.cshrc</i> which checks for the existence of the <code>tcsh</code> shell variable (q.v.) before using <i>tcsh</i>-specific commands, or can have both a <i>~/.cshrc</i> and a <i>~/.tcshrc</i> which <i>source</i>s (see the builtin command) <i>~/.cshrc</i>. The rest of this manual uses `<i>~/.tcshrc</i>&#8216; to mean `<i>~/.tcshrc</i> or, if <i>~/.tcshrc</i> is not found, <i>~/.cshrc</i>&#8216;. </p>
<p> In the normal case, the shell begins reading commands from the terminal, prompting with `&gt; &#8216;. (Processing of arguments and the use of the shell to process files containing command scripts are described later.) The shell repeatedly reads a line of command input, breaks it into words, places it on the command history list, parses it and executes each command in the line. </p>
<p> One can log out by typing `^D&#8217; on an empty line, `logout&#8217; or `login&#8217; or via the shell&#8217;s autologout mechanism (see the <code>autologout</code> shell variable). When a login shell terminates it sets the <code>logout</code> shell variable to `normal&#8217; or `automatic&#8217; as appropriate, then executes commands from the files <i>/etc/csh.logout</i> and <i>~/.logout</i>. The shell may drop DTR on logout if so compiled; see the <code>version</code> shell variable. </p>
<p> The names of the system login and logout files vary from system to system for compatibility with different <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1) variants; see <code>FILES</code>.</p>
<h3>Editing</h3>
<p> We first describe <code>The command-line editor</code>. The <code>Completion and listing</code> and <code>Spelling correction</code> sections describe two sets of functionality that are implemented as editor commands but which deserve their own treatment. Finally, <code>Editor commands</code> lists and describes the editor commands specific to the shell and their default bindings.</p>
<h3>The command-line editor (+)</h3>
<p> Command-line input can be edited using key sequences much like those used in GNU Emacs or <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1). The editor is active only when the <code>edit</code> shell variable is set, which it is by default in interactive shells. The <i>bindkey</i> builtin can display and change key bindings. Emacs-style key bindings are used by default (unless the shell was compiled otherwise; see the <code>version</code> shell variable), but <i>bindkey</i> can change the key bindings to <i>vi</i>-style bindings en masse. </p>
<p> The shell always binds the arrow keys (as defined in the <code>TERMCAP</code> environment variable) to </p>
<dl>
<dt>
<dd>
<dl>
<dt>down</p>
<dd> <i>down-history</i></p>
<dt>up</p>
<dd> <i>up-history</i></p>
<dt>left</p>
<dd> <i>backward-char</i></p>
<dt>right</p>
<dd> <i>forward-char</i></dl>
</dl>
<p> unless doing so would alter another single-character binding. One can set the arrow key escape sequences to the empty string with <i>settc</i> to prevent these bindings. The ANSI/VT100 sequences for arrow keys are always bound. </p>
<p> Other key bindings are, for the most part, what Emacs and <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) users would expect and can easily be displayed by <i>bindkey</i>, so there is no need to list them here. Likewise, <i>bindkey</i> can list the editor commands with a short description of each. </p>
<p> Note that editor commands do not have the same notion of a &#8220;word&#8221; as does the shell. The editor delimits words with any non-alphanumeric characters not in the shell variable <code>wordchars</code>, while the shell recognizes only whitespace and some of the characters with special meanings to it, listed under <code>Lexical structure</code>.</p>
<h3>Completion and listing (+)</h3>
<p> The shell is often able to complete words when given a unique abbreviation. Type part of a word (for example `ls /usr/lost&#8217;) and hit the tab key to run the <i>complete-word</i> editor command. The shell completes the filename `/usr/lost&#8217; to `/usr/lost+found/&#8217;, replacing the incomplete word with the complete word in the input buffer. (Note the terminal `/&#8217;; completion adds a `/&#8217; to the end of completed directories and a space to the end of other completed words, to speed typing and provide a visual indicator of successful completion. The <code>addsuffix</code> shell variable can be unset to prevent this.) If no match is found (perhaps `/usr/lost+found&#8217; doesn&#8217;t exist), the terminal bell rings. If the word is already complete (perhaps there is a `/usr/lost&#8217; on your system, or perhaps you were thinking too far ahead and typed the whole thing) a `/&#8217; or space is added to the end if it isn&#8217;t already there. </p>
<p> Completion works anywhere in the line, not at just the end; completed text pushes the rest of the line to the right. Completion in the middle of a word often results in leftover characters to the right of the cursor that need to be deleted. </p>
<p> Commands and variables can be completed in much the same way. For example, typing `em[tab]&#8217; would complete `em&#8217; to `emacs&#8217; if <i>emacs</i> were the only command on your system beginning with `em&#8217;. Completion can find a command in any directory in <code>path</code> or if given a full pathname. Typing `echo $ar[tab]&#8217; would complete `$ar&#8217; to `$argv&#8217; if no other variable began with `ar&#8217;. </p>
<p> The shell parses the input buffer to determine whether the word you want to complete should be completed as a filename, command or variable. The first word in the buffer and the first word following `;&#8217;, `|&#8217;, `|&amp;&#8217;, `&amp;&amp;&#8217; or `||&#8217; is considered to be a command. A word beginning with `$&#8217; is considered to be a variable. Anything else is a filename. An empty line is `completed&#8217; as a filename. </p>
<p> You can list the possible completions of a word at any time by typing `^D&#8217; to run the <i>delete-char-or-list-or-eof</i> editor command. The shell lists the possible completions using the <i>ls-F</i> builtin (q.v.) and reprints the prompt and unfinished command line, for example:</p>
<dl>
<dt>
<dd> &gt; ls /usr/l[^D]<br />
 lbin/ lib/ local/ lost+found/<br />
 &gt; ls /usr/l</dl>
<p> If the <code>autolist</code> shell variable is set, the shell lists the remaining choices (if any) whenever completion fails:</p>
<dl>
<dt>
<dd> &gt; set autolist<br />
 &gt; nm /usr/lib/libt[tab]<br />
 libtermcap.a@ libtermlib.a@<br />
 &gt; nm /usr/lib/libterm</dl>
<p> If <code>autolist</code> is set to `ambiguous&#8217;, choices are listed only when completion fails and adds no new characters to the word being completed. </p>
<p> A filename to be completed can contain variables, your own or others&#8217; home directories abbreviated with `~&#8217; (see <code>Filename substitution</code>) and directory stack entries abbreviated with `=&#8217; (see <code>Directory stack substitution</code>). For example,</p>
<dl>
<dt>
<dd> &gt; ls ~k[^D]<br />
 kahn kas kellogg<br />
 &gt; ls ~ke[tab]<br />
 &gt; ls ~kellogg/</dl>
<p> or</p>
<dl>
<dt>
<dd> &gt; set local = /usr/local<br />
 &gt; ls $lo[tab]<br />
 &gt; ls $local/[^D]<br />
 bin/ etc/ lib/ man/ src/<br />
 &gt; ls $local/</dl>
<p> Note that variables can also be expanded explicitly with the <i>expand-variables</i> editor command. </p>
<p> <i>delete-char-or-list-or-eof</i> lists at only the end of the line; in the middle of a line it deletes the character under the cursor and on an empty line it logs one out or, if <code>ignoreeof</code> is set, does nothing. `M-^D&#8217;, bound to the editor command <i>list-choices</i>, lists completion possibilities anywhere on a line, and <i>list-choices</i> (or any one of the related editor commands that do or don&#8217;t delete, list and/or log out, listed under <i>delete-char-or-list-or-eof</i>) can be bound to `^D&#8217; with the <i>bindkey</i> builtin command if so desired. </p>
<p> The <i>complete-word-fwd</i> and <i>complete-word-back</i> editor commands (not bound to any keys by default) can be used to cycle up and down through the list of possible completions, replacing the current word with the next or previous word in the list. </p>
<p> The shell variable <code>fignore</code> can be set to a list of suffixes to be ignored by completion. Consider the following:</p>
<dl>
<dt>
<dd> &gt; ls<br />
 Makefile condiments.h~ main.o side.c<br />
 README main.c meal side.o<br />
 condiments.h main.c~<br />
 &gt; set fignore = (.o \~)<br />
 &gt; emacs ma[^D]<br />
 main.c main.c~ main.o<br />
 &gt; emacs ma[tab]<br />
 &gt; emacs main.c</dl>
<p> `main.c~&#8217; and `main.o&#8217; are ignored by completion (but not listing), because they end in suffixes in <code>fignore</code>. Note that a `\&#8217; was needed in front of `~&#8217; to prevent it from being expanded to <code>home</code> as described under <code>Filename substitution</code>. <code>fignore</code> is ignored if only one completion is possible. </p>
<p> If the <code>complete</code> shell variable is set to `enhance&#8217;, completion 1) ignores case and 2) considers periods, hyphens and underscores (`.&#8217;, `-&#8216; and `_&#8217;) to be word separators and hyphens and underscores to be equivalent. If you had the following files</p>
<dl>
<dt>
<dd> comp.lang.c comp.lang.perl comp.std.c++<br />
 comp.lang.c++ comp.std.c</dl>
<p> and typed `mail -f c.l.c[tab]&#8217;, it would be completed to `mail -f comp.lang.c&#8217;, and ^D would list `comp.lang.c&#8217; and `comp.lang.c++&#8217;. `mail -f c..c++[^D]&#8217; would list `comp.lang.c++&#8217; and `comp.std.c++&#8217;. Typing `rm a&#8211;file[^D]&#8217; in the following directory</p>
<dl>
<dt>
<dd> A_silly_file a-hyphenated-file another_silly_file</dl>
<p> would list all three files, because case is ignored and hyphens and underscores are equivalent. Periods, however, are not equivalent to hyphens or underscores. </p>
<p> If the <code>complete</code> shell variable is set to `Enhance&#8217;, completion ignores case and differences between a hyphen and an underscore word separator only when the user types a lowercase character or a hyphen. Entering an uppercase character or an underscore will not match the corresponding lowercase character or hyphen word separator. Typing `rm a&#8211;file[^D]&#8217; in the directory of the previous example would still list all three files, but typing `rm A&#8211;file&#8217; would match only `A_silly_file&#8217; and typing `rm a__file[^D]&#8217; would match just `A_silly_file&#8217; and `another_silly_file&#8217; because the user explicitly used an uppercase or an underscore character. </p>
<p> Completion and listing are affected by several other shell variables: <code>recexact</code> can be set to complete on the shortest possible unique match, even if more typing might result in a longer match:</p>
<dl>
<dt>
<dd> &gt; ls<br />
 fodder foo food foonly<br />
 &gt; set recexact<br />
 &gt; rm fo[tab]</dl>
<p> just beeps, because `fo&#8217; could expand to `fod&#8217; or `foo&#8217;, but if we type another `o&#8217;,</p>
<dl>
<dt>
<dd> &gt; rm foo[tab]<br />
 &gt; rm foo</dl>
<p> the completion completes on `foo&#8217;, even though `food&#8217; and `foonly&#8217; also match. <code>autoexpand</code> can be set to run the <i>expand-history</i> editor command before each completion attempt, <code>autocorrect</code> can be set to spelling-correct the word to be completed (see <code>Spelling correction</code>) before each completion attempt and <code>correct</code> can be set to complete commands automatically after one hits `return&#8217;. <code>matchbeep</code> can be set to make completion beep or not beep in a variety of situations, and <code>nobeep</code> can be set to never beep at all. <code>nostat</code> can be set to a list of directories and/or patterns that match directories to prevent the completion mechanism from <i><a href="/docs/linux/man/2-stat/">stat</a></i>(2)ing those directories. <code>listmax</code> and <code>listmaxrows</code> can be set to limit the number of items and rows (respectively) that are listed without asking first. <code>recognize_only_executables</code> can be set to make the shell list only executables when listing commands, but it is quite slow. </p>
<p> Finally, the <i>complete</i> builtin command can be used to tell the shell how to complete words other than filenames, commands and variables. Completion and listing do not work on glob-patterns (see <code>Filename substitution</code>), but the <i>list-glob</i> and <i>expand-glob</i> editor commands perform equivalent functions for glob-patterns.</p>
<h3>Spelling correction (+)</h3>
<p> The shell can sometimes correct the spelling of filenames, commands and variable names as well as completing and listing them. </p>
<p> Individual words can be spelling-corrected with the <i>spell-word</i> editor command (usually bound to M-s and M-S) and the entire input buffer with <i>spell-line</i> (usually bound to M-$). The <code>correct</code> shell variable can be set to `cmd&#8217; to correct the command name or `all&#8217; to correct the entire line each time return is typed, and <code>autocorrect</code> can be set to correct the word to be completed before each completion attempt. </p>
<p> When spelling correction is invoked in any of these ways and the shell thinks that any part of the command line is misspelled, it prompts with the corrected line:</p>
<dl>
<dt>
<dd> &gt; set correct = cmd<br />
 &gt; lz /usr/bin<br />
 CORRECT&gt;ls /usr/bin (y|n|e|a)?</dl>
<p> One can answer `y&#8217; or space to execute the corrected line, `e&#8217; to leave the uncorrected command in the input buffer, `a&#8217; to abort the command as if `^C&#8217; had been hit, and anything else to execute the original line unchanged. </p>
<p> Spelling correction recognizes user-defined completions (see the <i>complete</i> builtin command). If an input word in a position for which a completion is defined resembles a word in the completion list, spelling correction registers a misspelling and suggests the latter word as a correction. However, if the input word does not match any of the possible completions for that position, spelling correction does not register a misspelling. </p>
<p> Like completion, spelling correction works anywhere in the line, pushing the rest of the line to the right and possibly leaving extra characters to the right of the cursor. </p>
<p> Beware: spelling correction is not guaranteed to work the way one intends, and is provided mostly as an experimental feature. Suggestions and improvements are welcome.</p>
<h3>Editor commands (+)</h3>
<p> `bindkey&#8217; lists key bindings and `bindkey -l&#8217; lists and briefly describes editor commands. Only new or especially interesting editor commands are described here. See <i><a href="/docs/linux/man/1-emacs/">emacs</a></i>(1) and <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) for descriptions of each editor&#8217;s key bindings. </p>
<p> The character or characters to which each command is bound by default is given in parentheses. `^<i>character</i>&#8216; means a control character and `M-<i>character</i>&#8216; a meta character, typed as escape-<i>character</i> on terminals without a meta key. Case counts, but commands that are bound to letters by default are bound to both lower- and uppercase letters for convenience.</p>
<dl>
<dt><code>complete-word </code>(tab)</p>
<dd> Completes a word as described under <code>Completion and listing</code>.</p>
<dt><code>complete-word-back </code>(not bound)</p>
<dd> Like <i>complete-word-fwd</i>, but steps up from the end of the list.</p>
<dt><code>complete-word-fwd </code>(not bound)</p>
<dd> Replaces the current word with the first word in the list of possible completions. May be repeated to step down through the list. At the end of the list, beeps and reverts to the incomplete word.</p>
<dt><code>complete-word-raw </code>(^X-tab)</p>
<dd> Like <i>complete-word</i>, but ignores user-defined completions.</p>
<dt><code>copy-prev-word </code>(M-^_)</p>
<dd> Copies the previous word in the current line into the input buffer. See also <i>insert-last-word</i>.</p>
<dt><code>dabbrev-expand </code>(M-/)</p>
<dd> Expands the current word to the most recent preceding one for which the current is a leading substring, wrapping around the history list (once) if necessary. Repeating <i>dabbrev-expand</i> without any intervening typing changes to the next previous word etc., skipping identical matches much like <i>history-search-backward</i> does.</p>
<dt><code>delete-char </code>(not bound)</p>
<dd> Deletes the character under the cursor. See also <i>delete-char-or-list-or-eof</i>.</p>
<dt><code>delete-char-or-eof </code>(not bound)</p>
<dd> Does <i>delete-char</i> if there is a character under the cursor or <i>end-of-file</i> on an empty line. See also <i>delete-char-or-list-or-eof</i>.</p>
<dt><code>delete-char-or-list </code>(not bound)</p>
<dd> Does <i>delete-char</i> if there is a character under the cursor or <i>list-choices</i> at the end of the line. See also <i>delete-char-or-list-or-eof</i>.</p>
<dt><code>delete-char-or-list-or-eof </code>(^D)</p>
<dd> Does <i>delete-char</i> if there is a character under the cursor, <i>list-choices</i> at the end of the line or <i>end-of-file</i> on an empty line. See also those three commands, each of which does only a single action, and <i>delete-char-or-eof</i>, <i>delete-char-or-list</i> and <i>list-or-eof</i>, each of which does a different two out of the three.</p>
<dt><code>down-history </code>(down-arrow, ^N)</p>
<dd> Like <i>up-history</i>, but steps down, stopping at the original input line.</p>
<dt><code>end-of-file </code>(not bound)</p>
<dd> Signals an end of file, causing the shell to exit unless the <code>ignoreeof</code> shell variable (q.v.) is set to prevent this. See also <i>delete-char-or-list-or-eof</i>.</p>
<dt><code>expand-history </code>(M-space)</p>
<dd> Expands history substitutions in the current word. See <code>History substitution</code>. See also <i>magic-space</i>, <i>toggle-literal-history</i> and the <code>autoexpand</code> shell variable.</p>
<dt><code>expand-glob </code>(^X-*)</p>
<dd> Expands the glob-pattern to the left of the cursor. See <code>Filename substitution</code>.</p>
<dt><code>expand-line </code>(not bound)</p>
<dd> Like <i>expand-history</i>, but expands history substitutions in each word in the input buffer.</p>
<dt><code>expand-variables </code>(^X-$)</p>
<dd> Expands the variable to the left of the cursor. See <code>Variable substitution</code>.</p>
<dt><code>history-search-backward </code>(M-p, M-P)</p>
<dd> Searches backwards through the history list for a command beginning with the current contents of the input buffer up to the cursor and copies it into the input buffer. The search string may be a glob-pattern (see <code>Filename substitution</code>) containing `*&#8217;, `?&#8217;, `[]&#8217; or `{}&#8217;. <i>up-history</i> and <i>down-history</i> will proceed from the appropriate point in the history list. Emacs mode only. See also <i>history-search-forward</i> and <i>i-search-back</i>.</p>
<dt><code>history-search-forward </code>(M-n, M-N)</p>
<dd> Like <i>history-search-backward</i>, but searches forward.</p>
<dt><code>i-search-back </code>(not bound)</p>
<dd> Searches backward like <i>history-search-backward</i>, copies the first match into the input buffer with the cursor positioned at the end of the pattern, and prompts with `bck: &#8216; and the first match. Additional characters may be typed to extend the search, <i>i-search-back</i> may be typed to continue searching with the same pattern, wrapping around the history list if necessary, (<i>i-search-back</i> must be bound to a single character for this to work) or one of the following special characters may be typed:</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>^W</p>
<dd> Appends the rest of the word under the cursor to the search pattern.</p>
<dt>delete (or any character bound to <i>backward-delete-char</i>)</p>
<dd> Undoes the effect of the last character typed and deletes a character from the search pattern if appropriate.</p>
<dt>^G</p>
<dd> If the previous search was successful, aborts the entire search. If not, goes back to the last successful search.</p>
<dt>escape</p>
<dd> Ends the search, leaving the current line in the input buffer.</dl>
</dl>
<p> Any other character not bound to <i>self-insert-command</i> terminates the search, leaving the current line in the input buffer, and is then interpreted as normal input. In particular, a carriage return causes the current line to be executed. Emacs mode only. See also <i>i-search-fwd</i> and <i>history-search-backward</i>.</dl>
<dl>
<dt><code>i-search-fwd </code>(not bound)</p>
<dd> Like <i>i-search-back</i>, but searches forward.</p>
<dt><code>insert-last-word </code>(M-_)</p>
<dd> Inserts the last word of the previous input line (`!$&#8217;) into the input buffer. See also <i>copy-prev-word</i>.</p>
<dt><code>list-choices </code>(M-^D)</p>
<dd> Lists completion possibilities as described under <code>Completion and listing</code>. See also <i>delete-char-or-list-or-eof</i> and <i>list-choices-raw</i>.</p>
<dt><code>list-choices-raw </code>(^X-^D)</p>
<dd> Like <i>list-choices</i>, but ignores user-defined completions.</p>
<dt><code>list-glob </code>(^X-g, ^X-G)</p>
<dd> Lists (via the <i>ls-F</i> builtin) matches to the glob-pattern (see <code>Filename substitution</code>) to the left of the cursor.</p>
<dt><code>list-or-eof </code>(not bound)</p>
<dd> Does <i>list-choices</i> or <i>end-of-file</i> on an empty line. See also <i>delete-char-or-list-or-eof</i>.</p>
<dt><code>magic-space </code>(not bound)</p>
<dd> Expands history substitutions in the current line, like <i>expand-history</i>, and inserts a space. <i>magic-space</i> is designed to be bound to the space bar, but is not bound by default.</p>
<dt><code>normalize-command </code>(^X-?)</p>
<dd> Searches for the current word in PATH and, if it is found, replaces it with the full path to the executable. Special characters are quoted. Aliases are expanded and quoted but commands within aliases are not. This command is useful with commands that take commands as arguments, e.g., `dbx&#8217; and `sh -x&#8217;.</p>
<dt><code>normalize-path </code>(^X-n, ^X-N)</p>
<dd> Expands the current word as described under the `expand&#8217; setting of the <code>symlinks</code> shell variable.</p>
<dt><code>overwrite-mode </code>(unbound)</p>
<dd> Toggles between input and overwrite modes.</p>
<dt><code>run-fg-editor </code>(M-^Z)</p>
<dd> Saves the current input line and looks for a stopped job with a name equal to the last component of the file name part of the <code>EDITOR</code> or <code>VISUAL</code> environment variables, or, if neither is set, `ed&#8217; or `vi&#8217;. If such a job is found, it is restarted as if `fg %<i>job</i>&#8216; had been typed. This is used to toggle back and forth between an editor and the shell easily. Some people bind this command to `^Z&#8217; so they can do this even more easily.</p>
<dt><code>run-help </code>(M-h, M-H)</p>
<dd> Searches for documentation on the current command, using the same notion of `current command&#8217; as the completion routines, and prints it. There is no way to use a pager; <i>run-help</i> is designed for short help files. If the special alias <code>helpcommand</code> is defined, it is run with the command name as a sole argument. Else, documentation should be in a file named <i>command</i>.help, <i>command</i>.1, <i>command</i>.6, <i>command</i>.8 or <i>command</i>, which should be in one of the directories listed in the <code>HPATH</code> environment variable. If there is more than one help file only the first is printed.</p>
<dt><code>self-insert-command </code>(text characters)</p>
<dd> In insert mode (the default), inserts the typed character into the input line after the character under the cursor. In overwrite mode, replaces the character under the cursor with the typed character. The input mode is normally preserved between lines, but the <code>inputmode</code> shell variable can be set to `insert&#8217; or `overwrite&#8217; to put the editor in that mode at the beginning of each line. See also <i>overwrite-mode</i>.</p>
<dt><code>sequence-lead-in </code>(arrow prefix, meta prefix, ^X)</p>
<dd> Indicates that the following characters are part of a multi-key sequence. Binding a command to a multi-key sequence really creates two bindings: the first character to <i>sequence-lead-in</i> and the whole sequence to the command. All sequences beginning with a character bound to <i>sequence-lead-in</i> are effectively bound to <i>undefined-key</i> unless bound to another command.</p>
<dt><code>spell-line </code>(M-$)</p>
<dd> Attempts to correct the spelling of each word in the input buffer, like <i>spell-word</i>, but ignores words whose first character is one of `-&#8216;, `!&#8217;, `^&#8217; or `%&#8217;, or which contain `\&#8217;, `*&#8217; or `?&#8217;, to avoid problems with switches, substitutions and the like. See <code>Spelling correction</code>.</p>
<dt><code>spell-word </code>(M-s, M-S)</p>
<dd> Attempts to correct the spelling of the current word as described under <code>Spelling correction</code>. Checks each component of a word which appears to be a pathname.</p>
<dt><code>toggle-literal-history </code>(M-r, M-R)</p>
<dd> Expands or `unexpands&#8217; history substitutions in the input buffer. See also <i>expand-history</i> and the <code>autoexpand</code> shell variable.</p>
<dt><code>undefined-key </code>(any unbound key)</p>
<dd> Beeps.</p>
<dt><code>up-history </code>(up-arrow, ^P)</p>
<dd> Copies the previous entry in the history list into the input buffer. If <code>histlit</code> is set, uses the literal form of the entry. May be repeated to step up through the history list, stopping at the top.</p>
<dt><code>vi-search-back </code>(?)</p>
<dd> Prompts with `?&#8217; for a search string (which may be a glob-pattern, as with <i>history-search-backward</i>), searches for it and copies it into the input buffer. The bell rings if no match is found. Hitting return ends the search and leaves the last match in the input buffer. Hitting escape ends the search and executes the match. <i>vi</i> mode only.</p>
<dt><code>vi-search-fwd </code>(/)</p>
<dd> Like <i>vi-search-back</i>, but searches forward.</p>
<dt><code>which-command </code>(M-?)</p>
<dd> Does a <i>which</i> (see the description of the builtin command) on the first word of the input buffer.</p>
<dt><code>yank-pop </code>(M-y)</p>
<dd> When executed immediately after a <i>yank</i> or another <i>yank-pop</i>, replaces the yanked string with the next previous string from the killring. This also has the effect of rotating the killring, such that this string will be considered the most recently killed by a later <i>yank</i> command. Repeating <i>yank-pop</i> will cycle through the killring any number of times.</dl>
<h3>Lexical structure</h3>
<p> The shell splits input lines into words at blanks and tabs. The special characters `&amp;&#8217;, `|&#8217;, `;&#8217;, `&lt;&#8216;, `&gt;&#8217;, `(&#8216;, and `)&#8217; and the doubled characters `&amp;&amp;&#8217;, `||&#8217;, `&lt;&lt;&#8216; and `&gt;&gt;&#8217; are always separate words, whether or not they are surrounded by whitespace. </p>
<p> When the shell&#8217;s input is not a terminal, the character `#&#8217; is taken to begin a comment. Each `#&#8217; and the rest of the input line on which it appears is discarded before further parsing. </p>
<p> A special character (including a blank or tab) may be prevented from having its special meaning, and possibly made part of another word, by preceding it with a backslash (`\&#8217;) or enclosing it in single (`&#8221;), double (`&quot;&#8217;) or backward (&#8220;&#8217;) quotes. When not otherwise quoted a newline preceded by a `\&#8217; is equivalent to a blank, but inside quotes this sequence results in a newline. </p>
<p> Furthermore, all <code>Substitutions</code> (see below) except <code>History substitution</code> can be prevented by enclosing the strings (or parts of strings) in which they appear with single quotes or by quoting the crucial character(s) (e.g., `$&#8217; or &#8220;&#8217; for <code>Variable substitution</code> or <code>Command substitution</code> respectively) with `\&#8217;. (<code>Alias substitution</code> is no exception: quoting in any way any character of a word for which an <i>alias</i> has been defined prevents substitution of the alias. The usual way of quoting an alias is to precede it with a backslash.) <code>History substitution</code> is prevented by backslashes but not by single quotes. Strings quoted with double or backward quotes undergo <code>Variable substitution</code> and <code>Command substitution</code>, but other substitutions are prevented. </p>
<p> Text inside single or double quotes becomes a single word (or part of one). Metacharacters in these strings, including blanks and tabs, do not form separate words. Only in one special case (see <code>Command substitution</code> below) can a double-quoted string yield parts of more than one word; single-quoted strings never do. Backward quotes are special: they signal <code>Command substitution</code> (q.v.), which may result in more than one word. </p>
<p> Quoting complex strings, particularly strings which themselves contain quoting characters, can be confusing. Remember that quotes need not be used as they are in human writing! It may be easier to quote not an entire string, but only those parts of the string which need quoting, using different types of quoting to do so if appropriate. </p>
<p> The <code>backslash_quote</code> shell variable (q.v.) can be set to make backslashes always quote `\&#8217;, `&#8221;, and `&quot;&#8217;. (+) This may make complex quoting tasks easier, but it can cause syntax errors in <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1) scripts.</p>
<h3>Substitutions</h3>
<p> We now describe the various transformations the shell performs on the input in the order in which they occur. We note in passing the data structures involved and the commands and variables which affect them. Remember that substitutions can be prevented by quoting as described under <code>Lexical structure</code>.</p>
<h3>History substitution</h3>
<p> Each command, or &#8220;event&#8221;, input from the terminal is saved in the history list. The previous command is always saved, and the <code>history</code> shell variable can be set to a number to save that many commands. The <code>histdup</code> shell variable can be set to not save duplicate events or consecutive duplicate events. </p>
<p> Saved commands are numbered sequentially from 1 and stamped with the time. It is not usually necessary to use event numbers, but the current event number can be made part of the prompt by placing an `!&#8217; in the <code>prompt</code> shell variable. </p>
<p> The shell actually saves history in expanded and literal (unexpanded) forms. If the <code>histlit</code> shell variable is set, commands that display and store history use the literal form. </p>
<p> The <i>history</i> builtin command can print, store in a file, restore and clear the history list at any time, and the <code>savehist</code> and <code>histfile</code> shell variables can be set to store the history list automatically on logout and restore it on login. </p>
<p> History substitutions introduce words from the history list into the input stream, making it easy to repeat commands, repeat arguments of a previous command in the current command, or fix spelling mistakes in the previous command with little typing and a high degree of confidence. </p>
<p> History substitutions begin with the character `!&#8217;. They may begin anywhere in the input stream, but they do not nest. The `!&#8217; may be preceded by a `\&#8217; to prevent its special meaning; for convenience, a `!&#8217; is passed unchanged when it is followed by a blank, tab, newline, `=&#8217; or `(&#8216;. History substitutions also occur when an input line begins with `^&#8217;. This special abbreviation will be described later. The characters used to signal history substitution (`!&#8217; and `^&#8217;) can be changed by setting the <code>histchars</code> shell variable. Any input line which contains a history substitution is printed before it is executed. </p>
<p> A history substitution may have an &#8220;event specification&#8221;, which indicates the event from which words are to be taken, a &#8220;word designator&#8221;, which selects particular words from the chosen event, and/or a &#8220;modifier&#8221;, which manipulates the selected words. </p>
<p> An event specification can be </p>
<dl>
<dt>
<dd>
<dl>
<dt><i>n</i></p>
<dd> A number, referring to a particular event</p>
<dt>&#8211;<i>n</i></p>
<dd> An offset, referring to the event <i>n</i> before the current event</p>
<dt>#</p>
<dd> The current event. This should be used carefully in <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1), where there is no check for recursion. <i>tcsh</i> allows 10 levels of recursion. (+)</p>
<dt>!</p>
<dd> The previous event (equivalent to `-1&#8242;)</p>
<dt><i>s</i></p>
<dd> The most recent event whose first word begins with the string <i>s</i></p>
<dt>?<i>s</i>?</p>
<dd> The most recent event which contains the string <i>s</i>. The second `?&#8217; can be omitted if it is immediately followed by a newline.</dl>
</dl>
<p> For example, consider this bit of someone&#8217;s history list:</p>
<dl>
<dt>
<dd> &nbsp;<wbr>9 8:30 nroff -man wumpus.man<br />
 10 8:31 cp wumpus.man wumpus.man.old<br />
 11 8:36 vi wumpus.man<br />
 12 8:37 diff wumpus.man.old wumpus.man</dl>
<p> The commands are shown with their event numbers and time stamps. The current event, which we haven&#8217;t typed in yet, is event 13. `!11&#8242; and `!-2&#8242; refer to event 11. `!!&#8217; refers to the previous event, 12. `!!&#8217; can be abbreviated `!&#8217; if it is followed by `:&#8217; (`:&#8217; is described below). `!n&#8217; refers to event 9, which begins with `n&#8217;. `!?old?&#8217; also refers to event 12, which contains `old&#8217;. Without word designators or modifiers history references simply expand to the entire event, so we might type `!cp&#8217; to redo the copy command or `!!|more&#8217; if the `diff&#8217; output scrolled off the top of the screen. </p>
<p> History references may be insulated from the surrounding text with braces if necessary. For example, `!vdoc&#8217; would look for a command beginning with `vdoc&#8217;, and, in this example, not find one, but `!{v}doc&#8217; would expand unambiguously to `vi wumpus.mandoc&#8217;. Even in braces, history substitutions do not nest. </p>
<p> (+) While <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1) expands, for example, `!3d&#8217; to event 3 with the letter `d&#8217; appended to it, <i>tcsh</i> expands it to the last event beginning with `3d&#8217;; only completely numeric arguments are treated as event numbers. This makes it possible to recall events beginning with numbers. To expand `!3d&#8217; as in <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1) say `!{3}d&#8217;. </p>
<p> To select words from an event we can follow the event specification by a `:&#8217; and a designator for the desired words. The words of an input line are numbered from 0, the first (usually command) word being 0, the second word (first argument) being 1, etc. The basic word designators are: </p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> The first (command) word</p>
<dt><i>n</i></p>
<dd> The <i>n</i>th argument</p>
<dt>^</p>
<dd> The first argument, equivalent to `1&#8242;</p>
<dt>$</p>
<dd> The last argument</p>
<dt>%</p>
<dd> The word matched by an ?<i>s</i>? search</p>
<dt><i>x-y</i></p>
<dd> A range of words</p>
<dt><i>-y</i></p>
<dd> Equivalent to <i>`0-y&#8217;</i></p>
<dt>*</p>
<dd> Equivalent to `^-$&#8217;, but returns nothing if the event contains only 1 word</p>
<dt><i>x*</i></p>
<dd> Equivalent to <i>`x-$&#8217;</i></p>
<dt><i>x-</i></p>
<dd> Equivalent to <i>`x*&#8217;</i>, but omitting the last word (`$&#8217;)</dl>
</dl>
<p> Selected words are inserted into the command line separated by single blanks. For example, the `diff&#8217; command in the previous example might have been typed as `diff !!:1.old !!:1&#8242; (using `:1&#8242; to select the first argument from the previous event) or `diff !-2:2 !-2:1&#8242; to select and swap the arguments from the `cp&#8217; command. If we didn&#8217;t care about the order of the `diff&#8217; we might have said `diff !-2:1-2&#8242; or simply `diff !-2:*&#8217;. The `cp&#8217; command might have been written `cp wumpus.man !#:1.old&#8217;, using `#&#8217; to refer to the current event. `!n:- hurkle.man&#8217; would reuse the first two words from the `nroff&#8217; command to say `nroff -man hurkle.man&#8217;. </p>
<p> The `:&#8217; separating the event specification from the word designator can be omitted if the argument selector begins with a `^&#8217;, `$&#8217;, `*&#8217;, `%&#8217; or `-&#8216;. For example, our `diff&#8217; command might have been `diff !!^.old !!^&#8217; or, equivalently, `diff !!$.old !!$&#8217;. However, if `!!&#8217; is abbreviated `!&#8217;, an argument selector beginning with `-&#8216; will be interpreted as an event specification. </p>
<p> A history reference may have a word designator but no event specification. It then references the previous command. Continuing our `diff&#8217; example, we could have said simply `diff !^.old !^&#8217; or, to get the arguments in the opposite order, just `diff !*&#8217;. </p>
<p> The word or words in a history reference can be edited, or &#8220;modified&#8221;, by following it with one or more modifiers, each preceded by a `:&#8217;: </p>
<dl>
<dt>
<dd>
<dl>
<dt>h</p>
<dd> Remove a trailing pathname component, leaving the head.</p>
<dt>t</p>
<dd> Remove all leading pathname components, leaving the tail.</p>
<dt>r</p>
<dd> Remove a filename extension `.xxx&#8217;, leaving the root name.</p>
<dt>e</p>
<dd> Remove all but the extension.</p>
<dt>u</p>
<dd> Uppercase the first lowercase letter.</p>
<dt>l</p>
<dd> Lowercase the first uppercase letter.</p>
<dt>s<i>/l/r/</i></p>
<dd> Substitute <i>l</i> for <i>r</i>. <i>l</i> is simply a string like <i>r</i>, not a regular expression as in the eponymous <i><a href="/docs/linux/man/1-ed/">ed</a></i>(1) command. Any character may be used as the delimiter in place of `/&#8217;; a `\&#8217; can be used to quote the delimiter expect `(&#8216;, `)&#8217;, `|&#8217; and `&gt;&#8217; inside <i>l</i> and <i>r</i>. The character `&amp;&#8217; in the <i>r</i> is replaced by <i>l</i>; `\&#8217; also quotes `&amp;&#8217;. If <i>l</i> is empty (&#8220;&#8221;), the <i>l</i> from a previous substitution or the <i>s</i> from a previous search or event number in event specification is used. The trailing delimiter may be omitted if it is immediately followed by a newline.</p>
<dt>&amp;</p>
<dd> Repeat the previous substitution.</p>
<dt>g</p>
<dd> Apply the following modifier once to each word.</p>
<dt>a (+)</p>
<dd> Apply the following modifier as many times as possible to a single word. `a&#8217; and `g&#8217; can be used together to apply a modifier globally. With the `s&#8217; modifier, only the patterns contained in the original word are substituted, not patterns that contain any substitution result.</p>
<dt>p</p>
<dd> Print the new command line but do not execute it.</p>
<dt>q</p>
<dd> Quote the substituted words, preventing further substitutions.</p>
<dt>x</p>
<dd> Like q, but break into words at blanks, tabs and newlines.</dl>
</dl>
<p> Modifiers are applied to only the first modifiable word (unless `g&#8217; is used). It is an error for no word to be modifiable. </p>
<p> For example, the `diff&#8217; command might have been written as `diff wumpus.man.old !#^:r&#8217;, using `:r&#8217; to remove `.old&#8217; from the first argument on the same line (`!#^&#8217;). We could say `echo hello out there&#8217;, then `echo !*:u&#8217; to capitalize `hello&#8217;, `echo !*:au&#8217; to say it out loud, or `echo !*:agu&#8217; to really shout. We might follow `mail -s &quot;I forgot my password&quot; rot&#8217; with `!:s/rot/root&#8217; to correct the spelling of `root&#8217; (but see <code>Spelling correction</code> for a different approach). </p>
<p> There is a special abbreviation for substitutions. `^&#8217;, when it is the first character on an input line, is equivalent to `!:s^&#8217;. Thus we might have said `^rot^root&#8217; to make the spelling correction in the previous example. This is the only history substitution which does not explicitly begin with `!&#8217;. </p>
<p> (+) In <i>csh</i> as such, only one modifier may be applied to each history or variable expansion. In <i>tcsh</i>, more than one may be used, for example</p>
<dl>
<dt>
<dd> % mv wumpus.man /usr/man/man1/wumpus.1<br />
 % man !$:t:r<br />
 man wumpus</dl>
<p> In <i>csh</i>, the result would be `wumpus.1:r&#8217;. A substitution followed by a colon may need to be insulated from it with braces:</p>
<dl>
<dt>
<dd> &gt; mv a.out /usr/games/wumpus<br />
 &gt; setenv PATH !$:h:$PATH<br />
 Bad ! modifier: $.<br />
 &gt; setenv PATH !{-2$:h}:$PATH<br />
 setenv PATH /usr/games:/bin:/usr/bin:.</dl>
<p> The first attempt would succeed in <i>csh</i> but fails in <i>tcsh</i>, because <i>tcsh</i> expects another modifier after the second colon rather than `$&#8217;. </p>
<p> Finally, history can be accessed through the editor as well as through the substitutions just described. The <i>up-</i> and <i>down-history</i>, <i>history-search-backward</i> and <i>-forward</i>, <i>i-search-back</i> and <i>-fwd</i>, <i>vi-search-back</i> and <i>-fwd</i>, <i>copy-prev-word</i> and <i>insert-last-word</i> editor commands search for events in the history list and copy them into the input buffer. The <i>toggle-literal-history</i> editor command switches between the expanded and literal forms of history lines in the input buffer. <i>expand-history</i> and <i>expand-line</i> expand history substitutions in the current word and in the entire input buffer respectively.</p>
<h3>Alias substitution</h3>
<p> The shell maintains a list of aliases which can be set, unset and printed by the <i>alias</i> and <i>unalias</i> commands. After a command line is parsed into simple commands (see <code>Commands</code>) the first word of each command, left-to-right, is checked to see if it has an alias. If so, the first word is replaced by the alias. If the alias contains a history reference, it undergoes <code>History substitution</code> (q.v.) as though the original command were the previous input line. If the alias does not contain a history reference, the argument list is left untouched. </p>
<p> Thus if the alias for `ls&#8217; were `ls -l&#8217; the command `ls /usr&#8217; would become `ls -l /usr&#8217;, the argument list here being undisturbed. If the alias for `lookup&#8217; were `grep !^ /etc/passwd&#8217; then `lookup bill&#8217; would become `grep bill /etc/passwd&#8217;. Aliases can be used to introduce parser metasyntax. For example, `alias print &#8216;pr \!* | lpr&#8221; defines a &#8220;command&#8221; (`print&#8217;) which <i><a href="/docs/linux/man/1-pr/">pr</a></i>(1)s its arguments to the line printer. </p>
<p> Alias substitution is repeated until the first word of the command has no alias. If an alias substitution does not change the first word (as in the previous example) it is flagged to prevent a loop. Other loops are detected and cause an error. </p>
<p> Some aliases are referred to by the shell; see <code>Special aliases</code>.</p>
<h3>Variable substitution</h3>
<p> The shell maintains a list of variables, each of which has as value a list of zero or more words. The values of shell variables can be displayed and changed with the <i>set</i> and <i>unset</i> commands. The system maintains its own list of &#8220;environment&#8221; variables. These can be displayed and changed with <i>printenv</i>, <i>setenv</i> and <i>unsetenv</i>. </p>
<p> (+) Variables may be made read-only with `set -r&#8217; (q.v.). Read-only variables may not be modified or unset; attempting to do so will cause an error. Once made read-only, a variable cannot be made writable, so `set -r&#8217; should be used with caution. Environment variables cannot be made read-only. </p>
<p> Some variables are set by the shell or referred to by it. For instance, the <code>argv</code> variable is an image of the shell&#8217;s argument list, and words of this variable&#8217;s value are referred to in special ways. Some of the variables referred to by the shell are toggles; the shell does not care what their value is, only whether they are set or not. For instance, the <code>verbose</code> variable is a toggle which causes command input to be echoed. The <code>-v</code> command line option sets this variable. <code>Special shell variables</code> lists all variables which are referred to by the shell. </p>
<p> Other operations treat variables numerically. The `@&#8217; command permits numeric calculations to be performed and the result assigned to a variable. Variable values are, however, always represented as (zero or more) strings. For the purposes of numeric operations, the null string is considered to be zero, and the second and subsequent words of multi-word values are ignored. </p>
<p> After the input line is aliased and parsed, and before each command is executed, variable substitution is performed keyed by `$&#8217; characters. This expansion can be prevented by preceding the `$&#8217; with a `\&#8217; except within `&quot;&#8217;s where it <i>always</i> occurs, and within `&#8221;s where it <i>never</i> occurs. Strings quoted by &#8220;&#8217; are interpreted later (see <code>Command substitution</code> below) so `$&#8217; substitution does not occur there until later, if at all. A `$&#8217; is passed unchanged if followed by a blank, tab, or end-of-line. </p>
<p> Input/output redirections are recognized before variable expansion, and are variable expanded separately. Otherwise, the command name and entire argument list are expanded together. It is thus possible for the first (command) word (to this point) to generate more than one word, the first of which becomes the command name, and the rest of which become arguments. </p>
<p> Unless enclosed in `&quot;&#8217; or given the `:q&#8217; modifier the results of variable substitution may eventually be command and filename substituted. Within `&quot;&#8217;, a variable whose value consists of multiple words expands to a (portion of a) single word, with the words of the variable&#8217;s value separated by blanks. When the `:q&#8217; modifier is applied to a substitution the variable will expand to multiple words with each word separated by a blank and quoted to prevent later command or filename substitution. </p>
<p> The following metasequences are provided for introducing variable values into the shell input. Except as noted, it is an error to reference a variable which is not set. </p>
<p> $<i>name</i></p>
<dl>
<dt>${<i>name</i>}</p>
<dd> Substitutes the words of the value of variable <i>name</i>, each separated by a blank. Braces insulate <i>name</i> from following characters which would otherwise be part of it. Shell variables have names consisting of letters and digits starting with a letter. The underscore character is considered a letter. If <i>name</i> is not a shell variable, but is set in the environment, then that value is returned (but some of the other forms given below are not available in this case).</dl>
<p> $<i>name</i>[<i>selector</i>]</p>
<dl>
<dt>${<i>name</i>[<i>selector</i>]}</p>
<dd> Substitutes only the selected words from the value of <i>name</i>. The <i>selector</i> is subjected to `$&#8217; substitution and may consist of a single number or two numbers separated by a `-&#8216;. The first word of a variable&#8217;s value is numbered `1&#8242;. If the first number of a range is omitted it defaults to `1&#8217;. If the last member of a range is omitted it defaults to `$#<i>name</i>&#8216;. The <i>selector</i> `*&#8217; selects all words. It is not an error for a range to be empty if the second argument is omitted or in range.</p>
<dt>$0</p>
<dd> Substitutes the name of the file from which command input is being read. An error occurs if the name is not known.</dl>
<p> $<i>number</i></p>
<dl>
<dt>${<i>number</i>}</p>
<dd> Equivalent to `$argv[<i>number</i>]&#8217;.</p>
<dt>$*</p>
<dd> Equivalent to `$argv&#8217;, which is equivalent to `$argv[*]&#8217;.</dl>
<p> The `:&#8217; modifiers described under <code>History substitution</code>, except for `:p&#8217;, can be applied to the substitutions above. More than one may be used. (+) Braces may be needed to insulate a variable substitution from a literal colon just as with <code>History substitution</code> (q.v.); any modifiers must appear within the braces. </p>
<p> The following substitutions can not be modified with `:&#8217; modifiers. </p>
<p> $?<i>name</i></p>
<dl>
<dt>${?<i>name</i>}</p>
<dd> Substitutes the string `1&#8242; if <i>name</i> is set, `0&#8242; if it is not.</p>
<dt>$?0</p>
<dd> Substitutes `1&#8242; if the current input filename is known, `0&#8242; if it is not. Always `0&#8242; in interactive shells.</dl>
<p> $#<i>name</i></p>
<dl>
<dt>${#<i>name</i>}</p>
<dd> Substitutes the number of words in <i>name</i>.</p>
<dt>$#</p>
<dd> Equivalent to `$#argv&#8217;. (+)</dl>
<p> $%<i>name</i></p>
<dl>
<dt>${%<i>name</i>}</p>
<dd> Substitutes the number of characters in <i>name</i>. (+)</dl>
<p> $%<i>number</i></p>
<dl>
<dt>${%<i>number</i>}</p>
<dd> Substitutes the number of characters in $argv[<i>number</i>]. (+)</p>
<dt>$?</p>
<dd> Equivalent to `$status&#8217;. (+)</p>
<dt>$$</p>
<dd> Substitutes the (decimal) process number of the (parent) shell.</p>
<dt>$!</p>
<dd> Substitutes the (decimal) process number of the last background process started by this shell. (+)</p>
<dt>$_</p>
<dd> Substitutes the command line of the last command executed. (+)</p>
<dt>$&lt;</p>
<dd> Substitutes a line from the standard input, with no further interpretation thereafter. It can be used to read from the keyboard in a shell script. (+) While <i>csh</i> always quotes $&lt;, as if it were equivalent to `$&lt;:q&#8217;, <i>tcsh</i> does not. Furthermore, when <i>tcsh</i> is waiting for a line to be typed the user may type an interrupt to interrupt the sequence into which the line is to be substituted, but <i>csh</i> does not allow this.</dl>
<p> The editor command <i>expand-variables</i>, normally bound to `^X-$&#8217;, can be used to interactively expand individual variables.</p>
<h3>Command, filename and directory stack substitution</h3>
<p> The remaining substitutions are applied selectively to the arguments of builtin commands. This means that portions of expressions which are not evaluated are not subjected to these expansions. For commands which are not internal to the shell, the command name is substituted separately from the argument list. This occurs very late, after input-output redirection is performed, and in a child of the main shell.</p>
<h3>Command substitution</h3>
<p> Command substitution is indicated by a command enclosed in &#8220;&#8217;. The output from such a command is broken into separate words at blanks, tabs and newlines, and null words are discarded. The output is variable and command substituted and put in place of the original string. </p>
<p> Command substitutions inside double quotes (`&quot;&#8217;) retain blanks and tabs; only newlines force new words. The single final newline does not force a new word in any case. It is thus possible for a command substitution to yield only part of a word, even if the command outputs a complete line. </p>
<p> By default, the shell since version 6.12 replaces all newline and carriage return characters in the command by spaces. If this is switched off by unsetting <code>csubstnonl</code>, newlines separate commands as usual.</p>
<h3>Filename substitution</h3>
<p> If a word contains any of the characters `*&#8217;, `?&#8217;, `[&#8216; or `{&#8216; or begins with the character `~&#8217; it is a candidate for filename substitution, also known as &#8220;globbing&#8221;. This word is then regarded as a pattern (&#8220;glob-pattern&#8221;), and replaced with an alphabetically sorted list of file names which match the pattern. </p>
<p> In matching filenames, the character `.&#8217; at the beginning of a filename or immediately following a `/&#8217;, as well as the character `/&#8217; must be matched explicitly (unless either <code>globdot</code> or <code>globstar</code> or both are set(+)). The character `*&#8217; matches any string of characters, including the null string. The character `?&#8217; matches any single character. The sequence `[&#8230;]&#8217; matches any one of the characters enclosed. Within `[&#8230;]&#8217;, a pair of characters separated by `-&#8216; matches any character lexically between the two. </p>
<p> (+) Some glob-patterns can be negated: The sequence `[^&#8230;]&#8217; matches any single character <i>not</i> specified by the characters and/or ranges of characters in the braces. </p>
<p> An entire glob-pattern can also be negated with `^&#8217;:</p>
<dl>
<dt>
<dd> &gt; echo *<br />
 bang crash crunch ouch<br />
 &gt; echo ^cr*<br />
 bang ouch</dl>
<p> Glob-patterns which do not use `?&#8217;, `*&#8217;, or `[]&#8217; or which use `{}&#8217; or `~&#8217; (below) are not negated correctly. </p>
<p> The metanotation `a{b,c,d}e&#8217; is a shorthand for `abe ace ade&#8217;. Left-to-right order is preserved: `/usr/source/s1/{oldls,ls}.c&#8217; expands to `/usr/source/s1/oldls.c /usr/source/s1/ls.c&#8217;. The results of matches are sorted separately at a low level to preserve this order: `../{memo,*box}&#8217; might expand to `../memo ../box ../mbox&#8217;. (Note that `memo&#8217; was not sorted with the results of matching `*box&#8217;.) It is not an error when this construct expands to files which do not exist, but it is possible to get an error from a command to which the expanded list is passed. This construct may be nested. As a special case the words `{&#8216;, `}&#8217; and `{}&#8217; are passed undisturbed. </p>
<p> The character `~&#8217; at the beginning of a filename refers to home directories. Standing alone, i.e., `~&#8217;, it expands to the invoker&#8217;s home directory as reflected in the value of the <code>home</code> shell variable. When followed by a name consisting of letters, digits and `-&#8216; characters the shell searches for a user with that name and substitutes their home directory; thus `~ken&#8217; might expand to `/usr/ken&#8217; and `~ken/chmach&#8217; to `/usr/ken/chmach&#8217;. If the character `~&#8217; is followed by a character other than a letter or `/&#8217; or appears elsewhere than at the beginning of a word, it is left undisturbed. A command like `setenv MANPATH /usr/man:/usr/local/man:~/lib/man&#8217; does not, therefore, do home directory substitution as one might hope. </p>
<p> It is an error for a glob-pattern containing `*&#8217;, `?&#8217;, `[&#8216; or `~&#8217;, with or without `^&#8217;, not to match any files. However, only one pattern in a list of glob-patterns must match a file (so that, e.g., `rm *.a *.c *.o&#8217; would fail only if there were no files in the current directory ending in `.a&#8217;, `.c&#8217;, or `.o&#8217;), and if the <code>nonomatch</code> shell variable is set a pattern (or list of patterns) which matches nothing is left unchanged rather than causing an error. </p>
<p> The <code>globstar</code> shell variable can be set to allow `**&#8217; or `***&#8217; as a file glob pattern that matches any string of characters including `/&#8217;, recursively traversing any existing sub-directories. For example, `ls **.c&#8217; will list all the .c files in the current directory tree. If used by itself, it will match zero or more sub-directories (e.g. `ls /usr/include/**/time.h&#8217; will list any file named `time.h&#8217; in the /usr/include directory tree; `ls /usr/include/**time.h&#8217; will match any file in the /usr/include directory tree ending in `time.h&#8217;; and `ls /usr/include/**time**.h&#8217; will match any .h file with `time&#8217; either in a subdirectory name or in the filename itself). To prevent problems with recursion, the `**&#8217; glob-pattern will not descend into a symbolic link containing a directory. To override this, use `***&#8217; (+) </p>
<p> The <code>noglob</code> shell variable can be set to prevent filename substitution, and the <i>expand-glob</i> editor command, normally bound to `^X-*&#8217;, can be used to interactively expand individual filename substitutions.</p>
<h3>Directory stack substitution (+)</h3>
<p> The directory stack is a list of directories, numbered from zero, used by the <i>pushd</i>, <i>popd</i> and <i>dirs</i> builtin commands (q.v.). <i>dirs</i> can print, store in a file, restore and clear the directory stack at any time, and the <code>savedirs</code> and <code>dirsfile</code> shell variables can be set to store the directory stack automatically on logout and restore it on login. The <code>dirstack</code> shell variable can be examined to see the directory stack and set to put arbitrary directories into the directory stack. </p>
<p> The character `=&#8217; followed by one or more digits expands to an entry in the directory stack. The special case `=-&#8216; expands to the last directory in the stack. For example,</p>
<dl>
<dt>
<dd> &gt; dirs -v<br />
 0 /usr/bin<br />
 1 /usr/spool/uucp<br />
 2 /usr/accts/sys<br />
 &gt; echo =1<br />
 /usr/spool/uucp<br />
 &gt; echo =0/calendar<br />
 /usr/bin/calendar<br />
 &gt; echo =-<br />
 /usr/accts/sys</dl>
<p> The <code>noglob</code> and <code>nonomatch</code> shell variables and the <i>expand-glob</i> editor command apply to directory stack as well as filename substitutions.</p>
<h3>Other substitutions (+)</h3>
<p> There are several more transformations involving filenames, not strictly related to the above but mentioned here for completeness. <i>Any</i> filename may be expanded to a full path when the <code>symlinks</code> variable (q.v.) is set to `expand&#8217;. Quoting prevents this expansion, and the <i>normalize-path</i> editor command does it on demand. The <i>normalize-command</i> editor command expands commands in PATH into full paths on demand. Finally, <i>cd</i> and <i>pushd</i> interpret `-&#8216; as the old working directory (equivalent to the shell variable <code>owd</code>). This is not a substitution at all, but an abbreviation recognized by only those commands. Nonetheless, it too can be prevented by quoting.</p>
<h3>Commands</h3>
<p> The next three sections describe how the shell executes commands and deals with their input and output.</p>
<h3>Simple commands, pipelines and sequences</h3>
<p> A simple command is a sequence of words, the first of which specifies the command to be executed. A series of simple commands joined by `|&#8217; characters forms a pipeline. The output of each command in a pipeline is connected to the input of the next. </p>
<p> Simple commands and pipelines may be joined into sequences with `;&#8217;, and will be executed sequentially. Commands and pipelines can also be joined into sequences with `||&#8217; or `&amp;&amp;&#8217;, indicating, as in the C language, that the second is to be executed only if the first fails or succeeds respectively. </p>
<p> A simple command, pipeline or sequence may be placed in parentheses, `()&#8217;, to form a simple command, which may in turn be a component of a pipeline or sequence. A command, pipeline or sequence can be executed without waiting for it to terminate by following it with an `&amp;&#8217;.</p>
<h3>Builtin and non-builtin command execution</h3>
<p> Builtin commands are executed within the shell. If any component of a pipeline except the last is a builtin command, the pipeline is executed in a subshell. </p>
<p> Parenthesized commands are always executed in a subshell.</p>
<dl>
<dt>
<dd> (cd; pwd); pwd</dl>
<p> thus prints the <code>home</code> directory, leaving you where you were (printing this after the home directory), while</p>
<dl>
<dt>
<dd> cd; pwd</dl>
<p> leaves you in the <code>home</code> directory. Parenthesized commands are most often used to prevent <i>cd</i> from affecting the current shell. </p>
<p> When a command to be executed is found not to be a builtin command the shell attempts to execute the command via <i><a href="/docs/linux/man/2-execve/">execve</a></i>(2). Each word in the variable <code>path</code> names a directory in which the shell will look for the command. If the shell is not given a <code>-f</code> option, the shell hashes the names in these directories into an internal table so that it will try an <i><a href="/docs/linux/man/2-execve/">execve</a></i>(2) in only a directory where there is a possibility that the command resides there. This greatly speeds command location when a large number of directories are present in the search path. This hashing mechanism is not used:</p>
<dl>
<dt><code>1.</code></p>
<dd> If hashing is turned explicitly off via <i>unhash</i>.</p>
<dt><code>2.</code></p>
<dd> If the shell was given a <code>-f</code> argument.</p>
<dt><code>3.</code></p>
<dd> For each directory component of <code>path</code> which does not begin with a `/&#8217;.</p>
<dt><code>4.</code></p>
<dd> If the command contains a `/&#8217;.</dl>
<p> In the above four cases the shell concatenates each component of the path vector with the given command name to form a path name of a file which it then attempts to execute it. If execution is successful, the search stops. </p>
<p> If the file has execute permissions but is not an executable to the system (i.e., it is neither an executable binary nor a script that specifies its interpreter), then it is assumed to be a file containing shell commands and a new shell is spawned to read it. The <i>shell</i> special alias may be set to specify an interpreter other than the shell itself. </p>
<p> On systems which do not understand the `#!&#8217; script interpreter convention the shell may be compiled to emulate it; see the <code>version</code> shell variable. If so, the shell checks the first line of the file to see if it is of the form `#!<i>interpreter</i> <i>arg</i> &#8230;&#8217;. If it is, the shell starts <i>interpreter</i> with the given <i>arg</i>s and feeds the file to it on standard input.</p>
<h3>Input/output</h3>
<p> The standard input and standard output of a command may be redirected with the following syntax: </p>
<dl>
<dt>&lt; <i>name</p>
<dd> Open file name</i> (which is first variable, command and filename expanded) as the standard input.</p>
<dt>&lt;&lt; <i>word</p>
<dd> Read the shell input up to a line which is identical to word</i>. <i>word</i> is not subjected to variable, filename or command substitution, and each input line is compared to <i>word</i> before any substitutions are done on this input line. Unless a quoting `\&#8217;, `&quot;&#8217;, `&#8217; or &#8220;&#8217; appears in <i>word</i> variable and command substitution is performed on the intervening lines, allowing `\&#8217; to quote `$&#8217;, `\&#8217; and &#8220;&#8217;. Commands which are substituted have all blanks, tabs, and newlines preserved, except for the final newline which is dropped. The resultant text is placed in an anonymous temporary file which is given to the command as standard input.</dl>
<p> &gt; <i>name<br />
 &gt;! name<br />
 &gt;&amp; name</p>
<dl>
<dt>&gt;&amp;! name</p>
<dd> The file name</i> is used as standard output. If the file does not exist then it is created; if the file exists, it is truncated, its previous contents being lost.</p>
<dl>
<dt>
<dd>
<p> If the shell variable <code>noclobber</code> is set, then the file must not exist or be a character special file (e.g., a terminal or `/dev/null&#8217;) or an error results. This helps prevent accidental destruction of files. In this case the `!&#8217; forms can be used to suppress this check. </p>
<p> The forms involving `&amp;&#8217; route the diagnostic output into the specified file as well as the standard output. <i>name</i> is expanded in the same way as `&lt;&#8216; input filenames are.</dl>
</dl>
<p> &gt;&gt; <i>name<br />
 &gt;&gt;&amp; name<br />
 &gt;&gt;! name</p>
<dl>
<dt>&gt;&gt;&amp;! name</p>
<dd> Like `&gt;&#8217;, but appends output to the end of name</i>. If the shell variable <code>noclobber</code> is set, then it is an error for the file <i>not</i> to exist, unless one of the `!&#8217; forms is given.</dl>
<p> A command receives the environment in which the shell was invoked as modified by the input-output parameters and the presence of the command in a pipeline. Thus, unlike some previous shells, commands run from a file of shell commands have no access to the text of the commands by default; rather they receive the original standard input of the shell. The `&lt;&lt;&#8216; mechanism should be used to present inline data. This permits shell command scripts to function as components of pipelines and allows the shell to block read its input. Note that the default standard input for a command run detached is <i>not</i> the empty file <i>/dev/null</i>, but the original standard input of the shell. If this is a terminal and if the process attempts to read from the terminal, then the process will block and the user will be notified (see <code>Jobs</code>). </p>
<p> Diagnostic output may be directed through a pipe with the standard output. Simply use the form `|&amp;&#8217; rather than just `|&#8217;. </p>
<p> The shell cannot presently redirect diagnostic output without also redirecting standard output, but `(<i>command</i> &gt; <i>output-file</i>) &gt;&amp; <i>error-file</i>&#8216; is often an acceptable workaround. Either <i>output-file</i> or <i>error-file</i> may be `/dev/tty&#8217; to send output to the terminal.</p>
<h3>Features</h3>
<p> Having described how the shell accepts, parses and executes command lines, we now turn to a variety of its useful features.</p>
<h3>Control flow</h3>
<p> The shell contains a number of commands which can be used to regulate the flow of control in command files (shell scripts) and (in limited but useful ways) from terminal input. These commands all operate by forcing the shell to reread or skip in its input and, due to the implementation, restrict the placement of some of the commands. </p>
<p> The <i>foreach</i>, <i>switch</i>, and <i>while</i> statements, as well as the <i>if-then-else</i> form of the <i>if</i> statement, require that the major keywords appear in a single simple command on an input line as shown below. </p>
<p> If the shell&#8217;s input is not seekable, the shell buffers up input whenever a loop is being read and performs seeks in this internal buffer to accomplish the rereading implied by the loop. (To the extent that this allows, backward <i>goto</i>s will succeed on non-seekable inputs.)</p>
<h3>Expressions</h3>
<p> The <i>if</i>, <i>while</i> and <i>exit</i> builtin commands use expressions with a common syntax. The expressions can include any of the operators described in the next three sections. Note that the <i>@</i> builtin command (q.v.) has its own separate syntax.</p>
<h3>Logical, arithmetical and comparison operators</h3>
<p> These operators are similar to those of C and have the same precedence. They include</p>
<dl>
<dt>
<dd> || &amp;&amp; | ^ &amp; == != =~ !~ &lt;= &gt;=<br />
 &lt; &gt; &lt;&lt; &gt;&gt; + &#8211; * / % ! ~ ( )</dl>
<p> Here the precedence increases to the right, `==&#8217; `!=&#8217; `=~&#8217; and `!~&#8217;, `&lt;=&#8217; `&gt;=&#8217; `&lt;&#8216; and `&gt;&#8217;, `&lt;&lt;&#8216; and `&gt;&gt;&#8217;, `+&#8217; and `-&#8216;, `*&#8217; `/&#8217; and `%&#8217; being, in groups, at the same level. When multiple operators which have same precedence are used in one expression, calculation must be done from operator of right side. The `==&#8217; `!=&#8217; `=~&#8217; and `!~&#8217; operators compare their arguments as strings; all others operate on numbers. The operators `=~&#8217; and `!~&#8217; are like `!=&#8217; and `==&#8217; except that the right hand side is a glob-pattern (see <code>Filename substitution</code>) against which the left hand operand is matched. This reduces the need for use of the <i>switch</i> builtin command in shell scripts when all that is really needed is pattern matching. </p>
<p> Null or missing arguments are considered `0&#8242;. The results of all expressions are strings, which represent decimal numbers. It is important to note that no two components of an expression can appear in the same word; except when adjacent to components of expressions which are syntactically significant to the parser (`&amp;&#8217; `|&#8217; `&lt;&#8216; `&gt;&#8217; `(&#8216; `)&#8217;) they should be surrounded by spaces.</p>
<h3>Command exit status</h3>
<p> Commands can be executed in expressions and their exit status returned by enclosing them in braces (`{}&#8217;). Remember that the braces should be separated from the words of the command by spaces. Command executions succeed, returning true, i.e., `1&#8242;, if the command exits with status 0, otherwise they fail, returning false, i.e., `0&#8242;. If more detailed status information is required then the command should be executed outside of an expression and the <code>status</code> shell variable examined.</p>
<h3>File inquiry operators</h3>
<p> Some of these operators perform true/false tests on files and related objects. They are of the form <code>&#8211;</code><i>op file</i>, where <i>op</i> is one of </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>r</code></p>
<dd> Read access</p>
<dt><code>w</code></p>
<dd> Write access</p>
<dt><code>x</code></p>
<dd> Execute access</p>
<dt><code>X</code></p>
<dd> Executable in the path or shell builtin, e.g., `-X ls&#8217; and `-X ls-F&#8217; are generally true, but `-X /bin/ls&#8217; is not (+)</p>
<dt><code>e</code></p>
<dd> Existence</p>
<dt><code>o</code></p>
<dd> Ownership</p>
<dt><code>z</code></p>
<dd> Zero size</p>
<dt><code>s</code></p>
<dd> Non-zero size (+)</p>
<dt><code>f</code></p>
<dd> Plain file</p>
<dt><code>d</code></p>
<dd> Directory</p>
<dt><code>l</code></p>
<dd> Symbolic link (+) *</p>
<dt><code>b</code></p>
<dd> Block special file (+)</p>
<dt><code>c</code></p>
<dd> Character special file (+)</p>
<dt><code>p</code></p>
<dd> Named pipe (fifo) (+) *</p>
<dt><code>S</code></p>
<dd> Socket special file (+) *</p>
<dt><code>u</code></p>
<dd> Set-user-ID bit is set (+)</p>
<dt><code>g</code></p>
<dd> Set-group-ID bit is set (+)</p>
<dt><code>k</code></p>
<dd> Sticky bit is set (+)</p>
<dt><code>t</code></p>
<dd> <i>file</i> (which must be a digit) is an open file descriptor for a terminal device (+)</p>
<dt><code>R</code></p>
<dd> Has been migrated (Convex only) (+)</p>
<dt><code>L</code></p>
<dd> Applies subsequent operators in a multiple-operator test to a symbolic link rather than to the file to which the link points (+) *</dl>
</dl>
<p> <i>file</i> is command and filename expanded and then tested to see if it has the specified relationship to the real user. If <i>file</i> does not exist or is inaccessible or, for the operators indicated by `*&#8217;, if the specified file type does not exist on the current system, then all inquiries return false, i.e., `0&#8242;. </p>
<p> These operators may be combined for conciseness: `-<i>xy file</i>&#8216; is equivalent to `-<i>x file</i> &amp;&amp; &#8211;<i>y file</i>&#8216;. (+) For example, `-fx&#8217; is true (returns `1&#8242;) for plain executable files, but not for directories. </p>
<p> <code>L</code> may be used in a multiple-operator test to apply subsequent operators to a symbolic link rather than to the file to which the link points. For example, `-lLo&#8217; is true for links owned by the invoking user. <code>Lr</code>, <code>Lw</code> and <code>Lx</code> are always true for links and false for non-links. <code>L</code> has a different meaning when it is the last operator in a multiple-operator test; see below. </p>
<p> It is possible but not useful, and sometimes misleading, to combine operators which expect <i>file</i> to be a file with operators which do not (e.g., <code>X</code> and <code>t</code>). Following <code>L</code> with a non-file operator can lead to particularly strange results. </p>
<p> Other operators return other information, i.e., not just `0&#8242; or `1&#8242;. (+) They have the same format as before; <i>op</i> may be one of </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>A</code></p>
<dd> Last file access time, as the number of seconds since the epoch</p>
<dt><code>A:</code></p>
<dd> Like <code>A</code>, but in timestamp format, e.g., `Fri May 14 16:36:10 1993&#8242;</p>
<dt><code>M</code></p>
<dd> Last file modification time</p>
<dt><code>M:</code></p>
<dd> Like <code>M</code>, but in timestamp format</p>
<dt><code>C</code></p>
<dd> Last inode modification time</p>
<dt><code>C:</code></p>
<dd> Like <code>C</code>, but in timestamp format</p>
<dt><code>D</code></p>
<dd> Device number</p>
<dt><code>I</code></p>
<dd> Inode number</p>
<dt><code>F</code></p>
<dd> Composite <code>f</code>ile identifier, in the form <i>device</i>:<i>inode</i></p>
<dt><code>L</code></p>
<dd> The name of the file pointed to by a symbolic link</p>
<dt><code>N</code></p>
<dd> Number of (hard) links</p>
<dt><code>P</code></p>
<dd> Permissions, in octal, without leading zero</p>
<dt><code>P:</code></p>
<dd> Like <code>P</code>, with leading zero</p>
<dt><code>P</code><i>mode</i></p>
<dd> Equivalent to `-P <i>file</i> &amp; <i>mode</i>&#8216;, e.g., `-P22 <i>file</i>&#8216; returns `22&#8217; if <i>file</i> is writable by group and other, `20&#8242; if by group only, and `0&#8242; if by neither</p>
<dt><code>P</code><i>mode</i><code>:</code></p>
<dd> Like <code>P</code><i>mode</i>, with leading zero</p>
<dt><code>U</code></p>
<dd> Numeric userid</p>
<dt><code>U:</code></p>
<dd> Username, or the numeric userid if the username is unknown</p>
<dt><code>G</code></p>
<dd> Numeric groupid</p>
<dt><code>G:</code></p>
<dd> Groupname, or the numeric groupid if the groupname is unknown</p>
<dt><code>Z</code></p>
<dd> Size, in bytes</dl>
</dl>
<p> Only one of these operators may appear in a multiple-operator test, and it must be the last. Note that <code>L</code> has a different meaning at the end of and elsewhere in a multiple-operator test. Because `0&#8242; is a valid return value for many of these operators, they do not return `0&#8242; when they fail: most return `-1&#8242;, and <code>F</code> returns `:&#8217;. </p>
<p> If the shell is compiled with POSIX defined (see the <code>version</code> shell variable), the result of a file inquiry is based on the permission bits of the file and not on the result of the <i><a href="/docs/linux/man/2-access/">access</a></i>(2) system call. For example, if one tests a file with <code>-w</code> whose permissions would ordinarily allow writing but which is on a file system mounted read-only, the test will succeed in a POSIX shell but fail in a non-POSIX shell. </p>
<p> File inquiry operators can also be evaluated with the <i>filetest</i> builtin command (q.v.) (+).</p>
<h3>Jobs</h3>
<p> The shell associates a <i>job</i> with each pipeline. It keeps a table of current jobs, printed by the <i>jobs</i> command, and assigns them small integer numbers. When a job is started asynchronously with `&amp;&#8217;, the shell prints a line which looks like</p>
<dl>
<dt>
<dd> [1] 1234</dl>
<p> indicating that the job which was started asynchronously was job number 1 and had one (top-level) process, whose process id was 1234. </p>
<p> If you are running a job and wish to do something else you may hit the suspend key (usually `^Z&#8217;), which sends a STOP signal to the current job. The shell will then normally indicate that the job has been `Suspended&#8217; and print another prompt. If the <code>listjobs</code> shell variable is set, all jobs will be listed like the <i>jobs</i> builtin command; if it is set to `long&#8217; the listing will be in long format, like `jobs -l&#8217;. You can then manipulate the state of the suspended job. You can put it in the &#8220;background&#8221; with the <i>bg</i> command or run some other commands and eventually bring the job back into the &#8220;foreground&#8221; with <i>fg</i>. (See also the <i>run-fg-editor</i> editor command.) A `^Z&#8217; takes effect immediately and is like an interrupt in that pending output and unread input are discarded when it is typed. The <i>wait</i> builtin command causes the shell to wait for all background jobs to complete. </p>
<p> The `^]&#8217; key sends a delayed suspend signal, which does not generate a STOP signal until a program attempts to <i><a href="/docs/linux/man/2-read/">read</a></i>(2) it, to the current job. This can usefully be typed ahead when you have prepared some commands for a job which you wish to stop after it has read them. The `^Y&#8217; key performs this function in <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1); in <i>tcsh</i>, `^Y&#8217; is an editing command. (+) </p>
<p> A job being run in the background stops if it tries to read from the terminal. Background jobs are normally allowed to produce output, but this can be disabled by giving the command `stty tostop&#8217;. If you set this tty option, then background jobs will stop when they try to produce output like they do when they try to read input. </p>
<p> There are several ways to refer to jobs in the shell. The character `%&#8217; introduces a job name. If you wish to refer to job number 1, you can name it as `%1&#8242;. Just naming a job brings it to the foreground; thus `%1&#8242; is a synonym for `fg %1&#8242;, bringing job 1 back into the foreground. Similarly, saying `%1 &amp;&#8217; resumes job 1 in the background, just like `bg %1&#8242;. A job can also be named by an unambiguous prefix of the string typed in to start it: `%ex&#8217; would normally restart a suspended <i><a href="/docs/linux/man/1-ex/">ex</a></i>(1) job, if there were only one suspended job whose name began with the string `ex&#8217;. It is also possible to say `%?<i>string</i>&#8216; to specify a job whose text contains <i>string</i>, if there is only one such job. </p>
<p> The shell maintains a notion of the current and previous jobs. In output pertaining to jobs, the current job is marked with a `+&#8217; and the previous job with a `-&#8216;. The abbreviations `%+&#8217;, `%&#8217;, and (by analogy with the syntax of the <i>history</i> mechanism) `%%&#8217; all refer to the current job, and `%-&#8216; refers to the previous job. </p>
<p> The job control mechanism requires that the <i><a href="/docs/linux/man/1-stty/">stty</a></i>(1) option `new&#8217; be set on some systems. It is an artifact from a `new&#8217; implementation of the tty driver which allows generation of interrupt characters from the keyboard to tell jobs to stop. See <i><a href="/docs/linux/man/1-stty/">stty</a></i>(1) and the <i>setty</i> builtin command for details on setting options in the new tty driver.</p>
<h3>Status reporting</h3>
<p> The shell learns immediately whenever a process changes state. It normally informs you whenever a job becomes blocked so that no further progress is possible, but only right before it prints a prompt. This is done so that it does not otherwise disturb your work. If, however, you set the shell variable <code>notify</code>, the shell will notify you immediately of changes of status in background jobs. There is also a shell command <i>notify</i> which marks a single process so that its status changes will be immediately reported. By default <i>notify</i> marks the current process; simply say `notify&#8217; after starting a background job to mark it. </p>
<p> When you try to leave the shell while jobs are stopped, you will be warned that `There are suspended jobs.&#8217; You may use the <i>jobs</i> command to see what they are. If you do this or immediately try to exit again, the shell will not warn you a second time, and the suspended jobs will be terminated.</p>
<h3>Automatic, periodic and timed events (+)</h3>
<p> There are various ways to run commands and take other actions automatically at various times in the &#8220;life cycle&#8221; of the shell. They are summarized here, and described in detail under the appropriate <code>Builtin commands</code>, <code>Special shell variables</code> and <code>Special aliases</code>. </p>
<p> The <i>sched</i> builtin command puts commands in a scheduled-event list, to be executed by the shell at a given time. </p>
<p> The <i>beepcmd</i>, <i>cwdcmd</i>, <i>periodic</i>, <i>precmd</i>, <i>postcmd</i>, and <i>jobcmd</i> <code>Special aliases</code> can be set, respectively, to execute commands when the shell wants to ring the bell, when the working directory changes, every <code>tperiod</code> minutes, before each prompt, before each command gets executed, after each command gets executed, and when a job is started or is brought into the foreground. </p>
<p> The <code>autologout</code> shell variable can be set to log out or lock the shell after a given number of minutes of inactivity. </p>
<p> The <code>mail</code> shell variable can be set to check for new mail periodically. </p>
<p> The <code>printexitvalue</code> shell variable can be set to print the exit status of commands which exit with a status other than zero. </p>
<p> The <code>rmstar</code> shell variable can be set to ask the user, when `rm *&#8217; is typed, if that is really what was meant. </p>
<p> The <code>time</code> shell variable can be set to execute the <i>time</i> builtin command after the completion of any process that takes more than a given number of CPU seconds. </p>
<p> The <code>watch</code> and <code>who</code> shell variables can be set to report when selected users log in or out, and the <i>log</i> builtin command reports on those users at any time.</p>
<h3>Native Language System support (+)</h3>
<p> The shell is eight bit clean (if so compiled; see the <code>version</code> shell variable) and thus supports character sets needing this capability. NLS support differs depending on whether or not the shell was compiled to use the system&#8217;s NLS (again, see <code>version</code>). In either case, 7-bit ASCII is the default character code (e.g., the classification of which characters are printable) and sorting, and changing the <code>LANG</code> or <code>LC_CTYPE</code> environment variables causes a check for possible changes in these respects. </p>
<p> When using the system&#8217;s NLS, the <i><a href="/docs/linux/man/3-setlocale/">setlocale</a></i>(3) function is called to determine appropriate character code/classification and sorting (e.g., a &#8216;en_CA.UTF-8&#8217; would yield &quot;UTF-8&quot; as a character code). This function typically examines the <code>LANG</code> and <code>LC_CTYPE</code> environment variables; refer to the system documentation for further details. When not using the system&#8217;s NLS, the shell simulates it by assuming that the ISO 8859-1 character set is used whenever either of the <code>LANG</code> and <code>LC_CTYPE</code> variables are set, regardless of their values. Sorting is not affected for the simulated NLS. </p>
<p> In addition, with both real and simulated NLS, all printable characters in the range \200-\377, i.e., those that have M-<i>char</i> bindings, are automatically rebound to <i>self-insert-command</i>. The corresponding binding for the escape-<i>char</i> sequence, if any, is left alone. These characters are not rebound if the <code>NOREBIND</code> environment variable is set. This may be useful for the simulated NLS or a primitive real NLS which assumes full ISO 8859-1. Otherwise, all M-<i>char</i> bindings in the range \240-\377 are effectively undone. Explicitly rebinding the relevant keys with <i>bindkey</i> is of course still possible. </p>
<p> Unknown characters (i.e., those that are neither printable nor control characters) are printed in the format 
nn. If the tty is not in 8 bit mode, other 8 bit characters are printed by converting them to ASCII and using standout mode. The shell never changes the 7/8 bit mode of the tty and tracks user-initiated changes of 7/8 bit mode. NLS users (or, for that matter, those who want to use a meta key) may need to explicitly set the tty in 8 bit mode through the appropriate <i><a href="/docs/linux/man/1-stty/">stty</a></i>(1) command in, e.g., the <i>~/.login</i> file.</p>
<h3>OS variant support (+)</h3>
<p> A number of new builtin commands are provided to support features in particular operating systems. All are described in detail in the <code>Builtin commands</code> section. </p>
<p> On systems that support TCF (aix-ibm370, aix-ps2), <i>getspath</i> and <i>setspath</i> get and set the system execution path, <i>getxvers</i> and <i>setxvers</i> get and set the experimental version prefix and <i>migrate</i> migrates processes between sites. The <i>jobs</i> builtin prints the site on which each job is executing. </p>
<p> Under BS2000, <i>bs2cmd</i> executes commands of the underlying BS2000/OSD operating system. </p>
<p> Under Domain/OS, <i>inlib</i> adds shared libraries to the current environment, <i>rootnode</i> changes the rootnode and <i>ver</i> changes the systype. </p>
<p> Under Mach, <i>setpath</i> is equivalent to Mach&#8217;s <i><a href="/docs/linux/man/1-setpath/">setpath</a></i>(1). </p>
<p> Under Masscomp/RTU and Harris CX/UX, <i>universe</i> sets the universe. </p>
<p> Under Harris CX/UX, <i>ucb</i> or <i>att</i> runs a command under the specified universe. </p>
<p> Under Convex/OS, <i>warp</i> prints or sets the universe. </p>
<p> The <code>VENDOR</code>, <code>OSTYPE</code> and <code>MACHTYPE</code> environment variables indicate respectively the vendor, operating system and machine type (microprocessor class or machine model) of the system on which the shell thinks it is running. These are particularly useful when sharing one&#8217;s home directory between several types of machines; one can, for example,</p>
<dl>
<dt>
<dd> set path = (~/bin.$MACHTYPE /usr/ucb /bin /usr/bin .)</dl>
<p> in one&#8217;s <i>~/.login</i> and put executables compiled for each machine in the appropriate directory. </p>
<p> The <code>version</code> shell variable indicates what options were chosen when the shell was compiled. </p>
<p> Note also the <i>newgrp</i> builtin, the <code>afsuser</code> and <code>echo_style</code> shell variables and the system-dependent locations of the shell&#8217;s input files (see <code>FILES</code>).</p>
<h3>Signal handling</h3>
<p> Login shells ignore interrupts when reading the file <i>~/.logout</i>. The shell ignores quit signals unless started with <code>-q</code>. Login shells catch the terminate signal, but non-login shells inherit the terminate behavior from their parents. Other signals have the values which the shell inherited from its parent. </p>
<p> In shell scripts, the shell&#8217;s handling of interrupt and terminate signals can be controlled with <i>onintr</i>, and its handling of hangups can be controlled with <i>hup</i> and <i>nohup</i>. </p>
<p> The shell exits on a hangup (see also the <code>logout</code> shell variable). By default, the shell&#8217;s children do too, but the shell does not send them a hangup when it exits. <i>hup</i> arranges for the shell to send a hangup to a child when it exits, and <i>nohup</i> sets a child to ignore hangups.</p>
<h3>Terminal management (+)</h3>
<p> The shell uses three different sets of terminal (&#8220;tty&#8221;) modes: `edit&#8217;, used when editing, `quote&#8217;, used when quoting literal characters, and `execute&#8217;, used when executing commands. The shell holds some settings in each mode constant, so commands which leave the tty in a confused state do not interfere with the shell. The shell also matches changes in the speed and padding of the tty. The list of tty modes that are kept constant can be examined and modified with the <i>setty</i> builtin. Note that although the editor uses CBREAK mode (or its equivalent), it takes typed-ahead characters anyway. </p>
<p> The <i>echotc</i>, <i>settc</i> and <i>telltc</i> commands can be used to manipulate and debug terminal capabilities from the command line. </p>
<p> On systems that support SIGWINCH or SIGWINDOW, the shell adapts to window resizing automatically and adjusts the environment variables <code>LINES</code> and <code>COLUMNS</code> if set. If the environment variable <code>TERMCAP</code> contains li# and co# fields, the shell adjusts them to reflect the new window size.</p>
<h2>REFERENCE</h2>
<p> The next sections of this manual describe all of the available <code>Builtin commands</code>, <code>Special aliases</code> and <code>Special shell variables</code>.</p>
<h3>Builtin commands</h3>
<dl>
<dt><code>%</code><i>job</i></p>
<dd> A synonym for the <i>fg</i> builtin command.</p>
<dt><code>%</code><i>job </i><code>&amp;</code></p>
<dd> A synonym for the <i>bg</i> builtin command.</p>
<dt><code>:</code></p>
<dd> Does nothing, successfully.</dl>
<p> <code>@</code><br />
 <code>@ </code><i>name</i><code> = </code><i>expr</i><br />
 <code>@ </code><i>name</i>[<i>index</i>]<code> = </code><i>expr</i><br />
 <code>@ </code><i>name</i><code>++</code>|<code>&#8212;</code></p>
<dl>
<dt><code>@ </code><i>name</i>[<i>index</i>]<code>++</code>|<code>&#8212;</code></p>
<dd> The first form prints the values of all shell variables.</p>
<dl>
<dt>
<dd>
<p> The second form assigns the value of <i>expr</i> to <i>name</i>. The third form assigns the value of <i>expr</i> to the <i>index</i>&#8216;th component of <i>name</i>; both <i>name</i> and its <i>index</i>&#8216;th component must already exist. </p>
<p> <i>expr</i> may contain the operators `*&#8217;, `+&#8217;, etc., as in C. If <i>expr</i> contains `&lt;&#8216;, `&gt;&#8217;, `&amp;&#8217; or `&#8217; then at least that part of <i>expr</i> must be placed within `()&#8217;. Note that the syntax of <i>expr</i> has nothing to do with that described under <code>Expressions</code>. </p>
<p> The fourth and fifth forms increment (`++&#8217;) or decrement (`&#8211;&#8216;) <i>name</i> or its <i>index</i>&#8216;th component. </p>
<p> The space between `@&#8217; and <i>name</i> is required. The spaces between <i>name</i> and `=&#8217; and between `=&#8217; and <i>expr</i> are optional. Components of <i>expr</i> must be separated by spaces.</dl>
<dt><code>alias </code>[<i>name </i>[<i>wordlist</i>]]</p>
<dd> Without arguments, prints all aliases. With <i>name</i>, prints the alias for name. With <i>name</i> and <i>wordlist</i>, assigns <i>wordlist</i> as the alias of <i>name</i>. <i>wordlist</i> is command and filename substituted. <i>name</i> may not be `alias&#8217; or `unalias&#8217;. See also the <i>unalias</i> builtin command.</p>
<dt><code>alloc</code></p>
<dd> Shows the amount of dynamic memory acquired, broken down into used and free memory. With an argument shows the number of free and used blocks in each size category. The categories start at size 8 and double at each step. This command&#8217;s output may vary across system types, because systems other than the VAX may use a different memory allocator.</p>
<dt><code>bg </code>[<code>%</code><i>job</i> &#8230;]</p>
<dd> Puts the specified jobs (or, without arguments, the current job) into the background, continuing each if it is stopped. <i>job</i> may be a number, a string, `&#8217;, `%&#8217;, `+&#8217; or `-&#8216; as described under <code>Jobs</code>.</dl>
<p> <code>bindkey </code>[<code>-l</code>|<code>-d</code>|<code>-e</code>|<code>-v</code>|<code>-u</code>] (+)<br />
 <code>bindkey </code>[<code>-a</code>] [<code>-b</code>] [<code>-k</code>] [<code>-r</code>] [<code>&#8212;</code>] <i>key </i>(+)</p>
<dl>
<dt><code>bindkey </code>[<code>-a</code>] [<code>-b</code>] [<code>-k</code>] [<code>-c</code>|<code>-s</code>] [<code>&#8212;</code>] <i>key command </i>(+)</p>
<dd> Without options, the first form lists all bound keys and the editor command to which each is bound, the second form lists the editor command to which <i>key</i> is bound and the third form binds the editor command <i>command</i> to <i>key</i>. Options include:</dl>
<dl>
<dt>
<dd>
<dl>
<dt><code>-l</code></p>
<dd> Lists all editor commands and a short description of each.</p>
<dt><code>-d</code></p>
<dd> Binds all keys to the standard bindings for the default editor.</p>
<dt><code>-e</code></p>
<dd> Binds all keys to the standard GNU Emacs-like bindings.</p>
<dt><code>-v</code></p>
<dd> Binds all keys to the standard <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1)-like bindings.</p>
<dt><code>-a</code></p>
<dd> Lists or changes key-bindings in the alternative key map. This is the key map used in <i>vi</i> command mode.</p>
<dt><code>-b</code></p>
<dd> <i>key</i> is interpreted as a control character written ^<i>character</i> (e.g., `^A&#8217;) or C-<i>character</i> (e.g., `C-A&#8217;), a meta character written M-<i>character</i> (e.g., `M-A&#8217;), a function key written F-<i>string</i> (e.g., `F-string&#8217;), or an extended prefix key written X-<i>character</i> (e.g., `X-A&#8217;).</p>
<dt><code>-k</code></p>
<dd> <i>key</i> is interpreted as a symbolic arrow key name, which may be one of `down&#8217;, `up&#8217;, `left&#8217; or `right&#8217;.</p>
<dt><code>-r</code></p>
<dd> Removes <i>key</i>&#8216;s binding. Be careful: `bindkey -r&#8217; does <i>not</i> bind <i>key</i> to <i>self-insert-command</i> (q.v.), it unbinds <i>key</i> completely.</p>
<dt><code>-c</code></p>
<dd> <i>command</i> is interpreted as a builtin or external command instead of an editor command.</p>
<dt><code>-s</code></p>
<dd> <i>command</i> is taken as a literal string and treated as terminal input when <i>key</i> is typed. Bound keys in <i>command</i> are themselves reinterpreted, and this continues for ten levels of interpretation.</p>
<dt><code>&#8212;</code></p>
<dd> Forces a break from option processing, so the next word is taken as <i>key</i> even if it begins with &#8216;-&#8216;.</p>
<dt><code>-u </code>(or any invalid option)</p>
<dd> Prints a usage message.</dl>
<p> <i>key</i> may be a single character or a string. If a command is bound to a string, the first character of the string is bound to <i>sequence-lead-in</i> and the entire string is bound to the command. </p>
<p> Control characters in <i>key</i> can be literal (they can be typed by preceding them with the editor command <i>quoted-insert</i>, normally bound to `^V&#8217;) or written caret-character style, e.g., `^A&#8217;. Delete is written `^?&#8217; (caret-question mark). <i>key</i> and <i>command</i> can contain backslashed escape sequences (in the style of System V <i><a href="/docs/linux/man/1-echo/">echo</a></i>(1)) as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code></code> Bell</p>
<dt><code></code></p>
<dd> Backspace</p>
<dt><code></code></p>
<dd> Escape</p>
<dt><code></code></p>
<dd> Form feed</p>
<dt><code>
</code></p>
<dd> Newline</p>
<dt><code></code></p>
<dd> Carriage return</p>
<dt><code>	</code></p>
<dd> Horizontal tab</p>
<dt><code></code></p>
<dd> Vertical tab</p>
<dt><code>\</code><i>nnn</i></p>
<dd> The ASCII character corresponding to the octal number <i>nnn</i></dl>
</dl>
<p> `\&#8217; nullifies the special meaning of the following character, if it has any, notably `\&#8217; and `^&#8217;.</dl>
<dl>
<dt><code>bs2cmd </code><i>bs2000-command</i> (+)</p>
<dd> Passes <i>bs2000-command</i> to the BS2000 command interpreter for execution. Only non-interactive commands can be executed, and it is not possible to execute any command that would overlay the image of the current process, like /EXECUTE or /CALL-PROCEDURE. (BS2000 only)</p>
<dt><code>break</code></p>
<dd> Causes execution to resume after the <i>end</i> of the nearest enclosing <i>foreach</i> or <i>while</i>. The remaining commands on the current line are executed. Multi-level breaks are thus possible by writing them all on one line.</p>
<dt><code>breaksw</code></p>
<dd> Causes a break from a <i>switch</i>, resuming after the <i>endsw</i>.</p>
<dt><code>builtins </code>(+)</p>
<dd> Prints the names of all builtin commands.</p>
<dt><code>bye </code>(+)</p>
<dd> A synonym for the <i>logout</i> builtin command. Available only if the shell was so compiled; see the <code>version</code> shell variable.</p>
<dt><code>case </code><i>label</i><code>:</code></p>
<dd> A label in a <i>switch</i> statement as discussed below.</p>
<dt><code>cd </code>[<code>-p</code>] [<code>-l</code>] [<code>-n</code>|<code>-v</code>] [I&#8211;] [<i>name</i>]</p>
<dd> If a directory <i>name</i> is given, changes the shell&#8217;s working directory to <i>name</i>. If not, changes to <code>home</code>. If <i>name</i> is `-&#8216; it is interpreted as the previous working directory (see <code>Other substitutions</code>). (+) If <i>name</i> is not a subdirectory of the current directory (and does not begin with `/&#8217;, `./&#8217; or `../&#8217;), each component of the variable <code>cdpath</code> is checked to see if it has a subdirectory <i>name</i>. Finally, if all else fails but <i>name</i> is a shell variable whose value begins with `/&#8217;, then this is tried to see if it is a directory.</p>
<dl>
<dt>
<dd>
<p> With <code>-p</code>, prints the final directory stack, just like <i>dirs</i>. The <code>-l</code>, <code>-n</code> and <code>-v</code> flags have the same effect on <i>cd</i> as on <i>dirs</i>, and they imply <code>-p</code>. (+) Using <code>&#8212;</code> forces a break from option processing so the next word is taken as the directory <i>name</i> even if it begins with &#8216;-&#8216;. (+) </p>
<p> See also the <code>implicitcd</code> shell variable.</dl>
<dt><code>chdir</code></p>
<dd> A synonym for the <i>cd</i> builtin command.</p>
<dt><code>complete </code>[<i>command</i> [<i>word</i><code>/</code><i>pattern</i><code>/</code><i>list</i>[<code>:</code><i>select</i>]<code>/</code>[[<i>suffix</i>]<code>/</code>] &#8230;]] (+)</p>
<dd> Without arguments, lists all completions. With <i>command</i>, lists completions for <i>command</i>. With <i>command</i> and <i>word</i> etc., defines completions.</p>
<dl>
<dt>
<dd>
<p> <i>command</i> may be a full command name or a glob-pattern (see <code>Filename substitution</code>). It can begin with `-&#8216; to indicate that completion should be used only when <i>command</i> is ambiguous. </p>
<p> <i>word</i> specifies which word relative to the current word is to be completed, and may be one of the following: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>c</code></p>
<dd> Current-word completion. <i>pattern</i> is a glob-pattern which must match the beginning of the current word on the command line. <i>pattern</i> is ignored when completing the current word.</p>
<dt><code>C</code></p>
<dd> Like <code>c</code>, but includes <i>pattern</i> when completing the current word.</p>
<dt><code>n</code></p>
<dd> Next-word completion. <i>pattern</i> is a glob-pattern which must match the beginning of the previous word on the command line.</p>
<dt><code>N</code></p>
<dd> Like <code>n</code>, but must match the beginning of the word two before the current word.</p>
<dt><code>p</code></p>
<dd> Position-dependent completion. <i>pattern</i> is a numeric range, with the same syntax used to index shell variables, which must include the current word.</dl>
</dl>
<p> <i>list</i>, the list of possible completions, may be one of the following: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>a</code></p>
<dd> Aliases</p>
<dt><code>b</code></p>
<dd> Bindings (editor commands)</p>
<dt><code>c</code></p>
<dd> Commands (builtin or external commands)</p>
<dt><code>C</code></p>
<dd> External commands which begin with the supplied path prefix</p>
<dt><code>d</code></p>
<dd> Directories</p>
<dt><code>D</code></p>
<dd> Directories which begin with the supplied path prefix</p>
<dt><code>e</code></p>
<dd> Environment variables</p>
<dt><code>f</code></p>
<dd> Filenames</p>
<dt><code>F</code></p>
<dd> Filenames which begin with the supplied path prefix</p>
<dt><code>g</code></p>
<dd> Groupnames</p>
<dt><code>j</code></p>
<dd> Jobs</p>
<dt><code>l</code></p>
<dd> Limits</p>
<dt><code>n</code></p>
<dd> Nothing</p>
<dt><code>s</code></p>
<dd> Shell variables</p>
<dt><code>S</code></p>
<dd> Signals</p>
<dt><code>t</code></p>
<dd> Plain (&#8220;text&#8221;) files</p>
<dt><code>T</code></p>
<dd> Plain (&#8220;text&#8221;) files which begin with the supplied path prefix</p>
<dt><code>v</code></p>
<dd> Any variables</p>
<dt><code>u</code></p>
<dd> Usernames</p>
<dt><code>x</code></p>
<dd> Like <code>n</code>, but prints <i>select</i> when <i>list-choices</i> is used.</p>
<dt><code>X</code></p>
<dd> Completions</p>
<dt>$<i>var</i></p>
<dd> Words from the variable <i>var</i></p>
<dt>(&#8230;)</p>
<dd> Words from the given list</p>
<dt>`&#8230;`</p>
<dd> Words from the output of command</dl>
</dl>
<p> <i>select</i> is an optional glob-pattern. If given, words from only <i>list</i> that match <i>select</i> are considered and the <code>fignore</code> shell variable is ignored. The last three types of completion may not have a <i>select</i> pattern, and <code>x</code> uses <i>select</i> as an explanatory message when the <i>list-choices</i> editor command is used. </p>
<p> <i>suffix</i> is a single character to be appended to a successful completion. If null, no character is appended. If omitted (in which case the fourth delimiter can also be omitted), a slash is appended to directories and a space to other words. </p>
<p> <i>command</i> invoked from `&#8230;` version has additional environment variable set, the variable name is <code>COMMAND_LINE</code> and contains (as its name indicates) contents of the current (already typed in) command line. One can examine and use contents of the <code>COMMAND_LINE</code> variable in her custom script to build more sophisticated completions (see completion for <a href="/docs/linux/man/1-svn/">svn</a>(1) included in this package). </p>
<p> Now for some examples. Some commands take only directories as arguments, so there&#8217;s no point completing plain files.</p>
<dl>
<dt>
<dd> &gt; complete cd &#8216;p/1/d/&#8217;</dl>
<p> completes only the first word following `cd&#8217; (`p/1&#8242;) with a directory. <code>p</code>-type completion can also be used to narrow down command completion:</p>
<dl>
<dt>
<dd> &gt; co[^D]<br />
 complete compress<br />
 &gt; complete -co* &#8216;p/0/(compress)/&#8217;<br />
 &gt; co[^D]<br />
 &gt; compress</dl>
<p> This completion completes commands (words in position 0, `p/0&#8242;) which begin with `co&#8217; (thus matching `co*&#8217;) to `compress&#8217; (the only word in the list). The leading `-&#8216; indicates that this completion is to be used with only ambiguous commands.</p>
<dl>
<dt>
<dd> &gt; complete find &#8216;n/-user/u/&#8217;</dl>
<p> is an example of <code>n</code>-type completion. Any word following `find&#8217; and immediately following `-user&#8217; is completed from the list of users.</p>
<dl>
<dt>
<dd> &gt; complete cc &#8216;c/-I/d/&#8217;</dl>
<p> demonstrates <code>c</code>-type completion. Any word following `cc&#8217; and beginning with `-I&#8217; is completed as a directory. `-I&#8217; is not taken as part of the directory because we used lowercase <code>c</code>. </p>
<p> Different <i>list</i>s are useful with different commands.</p>
<dl>
<dt>
<dd> &gt; complete alias &#8216;p/1/a/&#8217;<br />
 &gt; complete man &#8216;p/*/c/&#8217;<br />
 &gt; complete set &#8216;p/1/s/&#8217;<br />
 &gt; complete true &#8216;p/1/x:Truth has no options./&#8217;</dl>
<p> These complete words following `alias&#8217; with aliases, `man&#8217; with commands, and `set&#8217; with shell variables. `true&#8217; doesn&#8217;t have any options, so <code>x</code> does nothing when completion is attempted and prints `Truth has no options.&#8217; when completion choices are listed. </p>
<p> Note that the <i>man</i> example, and several other examples below, could just as well have used &#8216;c/*&#8217; or &#8216;n/*&#8217; as &#8216;p/*&#8217;. </p>
<p> Words can be completed from a variable evaluated at completion time,</p>
<dl>
<dt>
<dd> &gt; complete ftp &#8216;p/1/$hostnames/&#8217;<br />
 &gt; set hostnames = (rtfm.mit.edu tesla.ee.cornell.edu)<br />
 &gt; ftp [^D]<br />
 rtfm.mit.edu tesla.ee.cornell.edu<br />
 &gt; ftp [^C]<br />
 &gt; set hostnames = (rtfm.mit.edu tesla.ee.cornell.edu uunet.uu.net)<br />
 &gt; ftp [^D]<br />
 rtfm.mit.edu tesla.ee.cornell.edu uunet.uu.net</dl>
<p> or from a command run at completion time:</p>
<dl>
<dt>
<dd> &gt; complete kill &#8216;p/*/`ps | awk \{print\ \$1\}`/&#8217;<br />
 &gt; kill -9 [^D]<br />
 23113 23377 23380 23406 23429 23529 23530 PID</dl>
<p> Note that the <i>complete</i> command does not itself quote its arguments, so the braces, space and `$&#8217; in `{print $1}&#8217; must be quoted explicitly. </p>
<p> One command can have multiple completions:</p>
<dl>
<dt>
<dd> &gt; complete dbx &#8216;p/2/(core)/&#8217; &#8216;p/*/c/&#8217;</dl>
<p> completes the second argument to `dbx&#8217; with the word `core&#8217; and all other arguments with commands. Note that the positional completion is specified before the next-word completion. Because completions are evaluated from left to right, if the next-word completion were specified first it would always match and the positional completion would never be executed. This is a common mistake when defining a completion. </p>
<p> The <i>select</i> pattern is useful when a command takes files with only particular forms as arguments. For example,</p>
<dl>
<dt>
<dd> &gt; complete cc &#8216;p/*/f:*.[cao]/&#8217;</dl>
<p> completes `cc&#8217; arguments to files ending in only `.c&#8217;, `.a&#8217;, or `.o&#8217;. <i>select</i> can also exclude files, using negation of a glob-pattern as described under <code>Filename substitution</code>. One might use</p>
<dl>
<dt>
<dd> &gt; complete rm &#8216;p/*/f:^*.{c,h,cc,C,tex,1,man,l,y}/&#8217;</dl>
<p> to exclude precious source code from `rm&#8217; completion. Of course, one could still type excluded names manually or override the completion mechanism using the <i>complete-word-raw</i> or <i>list-choices-raw</i> editor commands (q.v.). </p>
<p> The `C&#8217;, `D&#8217;, `F&#8217; and `T&#8217; <i>list</i>s are like `c&#8217;, `d&#8217;, `f&#8217; and `t&#8217; respectively, but they use the <i>select</i> argument in a different way: to restrict completion to files beginning with a particular path prefix. For example, the Elm mail program uses `=&#8217; as an abbreviation for one&#8217;s mail directory. One might use</p>
<dl>
<dt>
<dd> &gt; complete elm c@=@F:$HOME/Mail/@</dl>
<p> to complete `elm -f =&#8217; as if it were `elm -f ~/Mail/&#8217;. Note that we used `@&#8217; instead of `/&#8217; to avoid confusion with the <i>select</i> argument, and we used `$HOME&#8217; instead of `~&#8217; because home directory substitution works at only the beginning of a word. </p>
<p> <i>suffix</i> is used to add a nonstandard suffix (not space or `/&#8217; for directories) to completed words.</p>
<dl>
<dt>
<dd> &gt; complete finger &#8216;c/*@/$hostnames/&#8217; &#8216;p/1/u/@&#8217;</dl>
<p> completes arguments to `finger&#8217; from the list of users, appends an `@&#8217;, and then completes after the `@&#8217; from the `hostnames&#8217; variable. Note again the order in which the completions are specified. </p>
<p> Finally, here&#8217;s a complex example for inspiration:</p>
<dl>
<dt>
<dd> &gt; complete find \<br />
 &#8216;n/-name/f/&#8217; &#8216;n/-newer/f/&#8217; &#8216;n/-{,n}cpio/f/&#8217; \<br />
 &#8216;n/-exec/c/&#8217; &#8216;n/-ok/c/&#8217; &#8216;n/-user/u/&#8217; \<br />
 &#8216;n/-group/g/&#8217; &#8216;n/-fstype/(nfs 4.2)/&#8217; \<br />
 &#8216;n/-type/(b c d f l p s)/&#8217; \<br />
 &#8216;c/-/(name newer cpio ncpio exec ok user \<br />
 group fstype type atime ctime depth inum \<br />
 ls mtime nogroup nouser perm print prune \<br />
 size xdev)/&#8217; \<br />
 &#8216;p/*/d/&#8217;</dl>
<p> This completes words following `-name&#8217;, `-newer&#8217;, `-cpio&#8217; or `ncpio&#8217; (note the pattern which matches both) to files, words following `-exec&#8217; or `-ok&#8217; to commands, words following `user&#8217; and `group&#8217; to users and groups respectively and words following `-fstype&#8217; or `-type&#8217; to members of the given lists. It also completes the switches themselves from the given list (note the use of <code>c</code>-type completion) and completes anything not otherwise completed to a directory. Whew. </p>
<p> Remember that programmed completions are ignored if the word being completed is a tilde substitution (beginning with `~&#8217;) or a variable (beginning with `$&#8217;). <i>complete</i> is an experimental feature, and the syntax may change in future versions of the shell. See also the <i>uncomplete</i> builtin command.</dl>
<dt><code>continue</code></p>
<dd> Continues execution of the nearest enclosing <i>while</i> or <i>foreach</i>. The rest of the commands on the current line are executed.</p>
<dt><code>default:</code></p>
<dd> Labels the default case in a <i>switch</i> statement. It should come after all <i>case</i> labels.</dl>
<p> <code>dirs </code>[<code>-l</code>] [<code>-n</code>|<code>-v</code>]<br />
 <code>dirs -S</code>|<code>-L </code>[<i>filename</i>] (+)</p>
<dl>
<dt><code>dirs -c </code>(+)</p>
<dd> The first form prints the directory stack. The top of the stack is at the left and the first directory in the stack is the current directory. With <code>-l</code>, `~&#8217; or `~<i>name</i>&#8216; in the output is expanded explicitly to <code>home</code> or the pathname of the home directory for user <i>name</i>. (+) With <code>-n</code>, entries are wrapped before they reach the edge of the screen. (+) With <code>-v</code>, entries are printed one per line, preceded by their stack positions. (+) If more than one of <code>-n</code> or <code>-v</code> is given, <code>-v</code> takes precedence. <code>-p</code> is accepted but does nothing.</p>
<dl>
<dt>
<dd>
<p> With <code>-S</code>, the second form saves the directory stack to <i>filename</i> as a series of <i>cd</i> and <i>pushd</i> commands. With <code>-L</code>, the shell sources <i>filename</i>, which is presumably a directory stack file saved by the <code>-S</code> option or the <code>savedirs</code> mechanism. In either case, <code>dirsfile</code> is used if <i>filename</i> is not given and <i>~/.cshdirs</i> is used if <code>dirsfile</code> is unset. </p>
<p> Note that login shells do the equivalent of `dirs -L&#8217; on startup and, if <code>savedirs</code> is set, `dirs -S&#8217; before exiting. Because only <i>~/.tcshrc</i> is normally sourced before <i>~/.cshdirs</i>, <code>dirsfile</code> should be set in <i>~/.tcshrc</i> rather than <i>~/.login</i>. </p>
<p> The last form clears the directory stack.</dl>
<dt><code>echo </code>[<code>-n</code>] <i>word</i> &#8230;</p>
<dd> Writes each <i>word</i> to the shell&#8217;s standard output, separated by spaces and terminated with a newline. The <code>echo_style</code> shell variable may be set to emulate (or not) the flags and escape sequences of the BSD and/or System V versions of <i>echo</i>; see <i><a href="/docs/linux/man/1-echo/">echo</a></i>(1).</p>
<dt><code>echotc </code>[<code>-sv</code>] <i>arg</i> &#8230; (+)</p>
<dd> Exercises the terminal capabilities (see <i><a href="/docs/linux/man/5-termcap/">termcap</a></i>(5)) in <i>args</i>. For example, &#8216;echotc home&#8217; sends the cursor to the home position, &#8216;echotc cm 3 10&#8217; sends it to column 3 and row 10, and &#8216;echotc ts 0; echo &quot;This is a test.&quot;; echotc fs&#8217; prints &quot;This is a test.&quot; in the status line.</p>
<dl>
<dt>
<dd>
<p> If <i>arg</i> is &#8216;baud&#8217;, &#8216;cols&#8217;, &#8216;lines&#8217;, &#8216;meta&#8217; or &#8216;tabs&#8217;, prints the value of that capability (&quot;yes&quot; or &quot;no&quot; indicating that the terminal does or does not have that capability). One might use this to make the output from a shell script less verbose on slow terminals, or limit command output to the number of lines on the screen:</p>
<dl>
<dt>
<dd> &gt; set history=`echotc lines`<br />
 &gt; @ history&#8211;</dl>
<p> Termcap strings may contain wildcards which will not echo correctly. One should use double quotes when setting a shell variable to a terminal capability string, as in the following example that places the date in the status line:</p>
<dl>
<dt>
<dd> &gt; set tosl=&quot;`echotc ts 0`&quot;<br />
 &gt; set frsl=&quot;`echotc fs`&quot;<br />
 &gt; echo -n &quot;$tosl&quot;;date; echo -n &quot;$frsl&quot;</dl>
<p> With <code>-s</code>, nonexistent capabilities return the empty string rather than causing an error. With <code>-v</code>, messages are verbose.</dl>
</dl>
<p> <code>else</code><br />
 <code>end</code><br />
 <code>endif</code></p>
<dl>
<dt><code>endsw</code></p>
<dd> See the description of the <i>foreach</i>, <i>if</i>, <i>switch</i>, and <i>while</i> statements below.</p>
<dt><code>eval </code><i>arg</i> &#8230;</p>
<dd> Treats the arguments as input to the shell and executes the resulting command(s) in the context of the current shell. This is usually used to execute commands generated as the result of command or variable substitution, because parsing occurs before these substitutions. See <i><a href="/docs/linux/man/1-tset/">tset</a></i>(1) for a sample use of <i>eval</i>.</p>
<dt><code>exec </code><i>command</i></p>
<dd> Executes the specified command in place of the current shell.</p>
<dt><code>exit </code>[<i>expr</i>]</p>
<dd> The shell exits either with the value of the specified <i>expr</i> (an expression, as described under <code>Expressions</code>) or, without <i>expr</i>, with the value 0.</p>
<dt><code>fg </code>[<code>%</code><i>job</i> &#8230;]</p>
<dd> Brings the specified jobs (or, without arguments, the current job) into the foreground, continuing each if it is stopped. <i>job</i> may be a number, a string, `&#8217;, `%&#8217;, `+&#8217; or `-&#8216; as described under <code>Jobs</code>. See also the <i>run-fg-editor</i> editor command.</p>
<dt><code>filetest &#8211;</code><i>op file</i> &#8230; (+)</p>
<dd> Applies <i>op</i> (which is a file inquiry operator as described under <code>File inquiry operators</code>) to each <i>file</i> and returns the results as a space-separated list.</dl>
<p> <code>foreach </code><i>name </i><code>(</code><i>wordlist</i><code>)</code><br />
 &#8230;</p>
<dl>
<dt><code>end</code></p>
<dd> Successively sets the variable <i>name</i> to each member of <i>wordlist</i> and executes the sequence of commands between this command and the matching <i>end</i>. (Both <i>foreach</i> and <i>end</i> must appear alone on separate lines.) The builtin command <i>continue</i> may be used to continue the loop prematurely and the builtin command <i>break</i> to terminate it prematurely. When this command is read from the terminal, the loop is read once prompting with `foreach? &#8216; (or <code>prompt2</code>) before any statements in the loop are executed. If you make a mistake typing in a loop at the terminal you can rub it out.</p>
<dt><code>getspath </code>(+)</p>
<dd> Prints the system execution path. (TCF only)</p>
<dt><code>getxvers </code>(+)</p>
<dd> Prints the experimental version prefix. (TCF only)</p>
<dt><code>glob </code><i>wordlist</i></p>
<dd> Like <i>echo</i>, but the `-n&#8217; parameter is not recognized and words are delimited by null characters in the output. Useful for programs which wish to use the shell to filename expand a list of words.</p>
<dt><code>goto </code><i>word</i></p>
<dd> <i>word</i> is filename and command-substituted to yield a string of the form `label&#8217;. The shell rewinds its input as much as possible, searches for a line of the form `label:&#8217;, possibly preceded by blanks or tabs, and continues execution after that line.</p>
<dt><code>hashstat</code></p>
<dd> Prints a statistics line indicating how effective the internal hash table has been at locating commands (and avoiding <i>exec</i>&#8216;s). An <i>exec</i> is attempted for each component of the <code>path</code> where the hash function indicates a possible hit, and in each component which does not begin with a `/&#8217;.</p>
<dt>
<dd> On machines without <i><a href="/docs/linux/man/2-vfork/">vfork</a></i>(2), prints only the number and size of hash buckets.</dl>
<p> <code>history </code>[<code>-hTr</code>] [<i>n</i>]<br />
 <code>history -S</code>|<code>-L|-M </code>[<i>filename</i>] (+)</p>
<dl>
<dt><code>history -c </code>(+)</p>
<dd> The first form prints the history event list. If <i>n</i> is given only the <i>n</i> most recent events are printed or saved. With <code>-h</code>, the history list is printed without leading numbers. If <code>-T</code> is specified, timestamps are printed also in comment form. (This can be used to produce files suitable for loading with &#8216;history -L&#8217; or &#8216;source -h&#8217;.) With <code>-r</code>, the order of printing is most recent first rather than oldest first.</p>
<dl>
<dt>
<dd>
<p> With <code>-S</code>, the second form saves the history list to <i>filename</i>. If the first word of the <code>savehist</code> shell variable is set to a number, at most that many lines are saved. If the second word of <code>savehist</code> is set to `merge&#8217;, the history list is merged with the existing history file instead of replacing it (if there is one) and sorted by time stamp. (+) Merging is intended for an environment like the X Window System with several shells in simultaneous use. Currently it succeeds only when the shells quit nicely one after another. </p>
<p> With <code>-L</code>, the shell appends <i>filename</i>, which is presumably a history list saved by the <code>-S</code> option or the <code>savehist</code> mechanism, to the history list. <code>-M</code> is like <code>-L</code>, but the contents of <i>filename</i> are merged into the history list and sorted by timestamp. In either case, <code>histfile</code> is used if <i>filename</i> is not given and <i>~/.history</i> is used if <code>histfile</code> is unset. `history -L&#8217; is exactly like &#8216;source -h&#8217; except that it does not require a filename. </p>
<p> Note that login shells do the equivalent of `history -L&#8217; on startup and, if <code>savehist</code> is set, `history -S&#8217; before exiting. Because only <i>~/.tcshrc</i> is normally sourced before <i>~/.history</i>, <code>histfile</code> should be set in <i>~/.tcshrc</i> rather than <i>~/.login</i>. </p>
<p> If <code>histlit</code> is set, the first and second forms print and save the literal (unexpanded) form of the history list. </p>
<p> The last form clears the history list.</dl>
<dt><code>hup </code>[<i>command</i>] (+)</p>
<dd> With <i>command</i>, runs <i>command</i> such that it will exit on a hangup signal and arranges for the shell to send it a hangup signal when the shell exits. Note that commands may set their own response to hangups, overriding <i>hup</i>. Without an argument, causes the non-interactive shell only to exit on a hangup for the remainder of the script. See also <code>Signal handling</code> and the <i>nohup</i> builtin command.</p>
<dt><code>if (</code><i>expr</i><code>) </code><i>command</i></p>
<dd> If <i>expr</i> (an expression, as described under <code>Expressions</code>) evaluates true, then <i>command</i> is executed. Variable substitution on <i>command</i> happens early, at the same time it does for the rest of the <i>if</i> command. <i>command</i> must be a simple command, not an alias, a pipeline, a command list or a parenthesized command list, but it may have arguments. Input/output redirection occurs even if <i>expr</i> is false and <i>command</i> is thus <i>not</i> executed; this is a bug.</dl>
<p> <code>if (</code><i>expr</i><code>) then</code><br />
 &#8230;<br />
 <code>else if (</code><i>expr2</i><code>) then</code><br />
 &#8230;<br />
 <code>else</code><br />
 &#8230;</p>
<dl>
<dt><code>endif</code></p>
<dd> If the specified <i>expr</i> is true then the commands to the first <i>else</i> are executed; otherwise if <i>expr2</i> is true then the commands to the second <i>else</i> are executed, etc. Any number of <i>else-if</i> pairs are possible; only one <i>endif</i> is needed. The <i>else</i> part is likewise optional. (The words <i>else</i> and <i>endif</i> must appear at the beginning of input lines; the <i>if</i> must appear alone on its input line or after an <i>else</i>.)</p>
<dt><code>inlib </code><i>shared-library</i> &#8230; (+)</p>
<dd> Adds each <i>shared-library</i> to the current environment. There is no way to remove a shared library. (Domain/OS only)</p>
<dt><code>jobs </code>[<code>-l</code>]</p>
<dd> Lists the active jobs. With <code>-l</code>, lists process IDs in addition to the normal information. On TCF systems, prints the site on which each job is executing.</dl>
<dl>
<dt><code>kill </code>[<code>-s </code><i>signal</i>] <code>%</code><i>job</i>|<i>pid</i> &#8230;</p>
<dd>
<dt><code>kill -l</code></p>
<dd> The first and second forms sends the specified <i>signal</i> (or, if none is given, the TERM (terminate) signal) to the specified jobs or processes. <i>job</i> may be a number, a string, `&#8217;, `%&#8217;, `+&#8217; or `-&#8216; as described under <code>Jobs</code>. Signals are either given by number or by name (as given in <i>/usr/include/signal.h</i>, stripped of the prefix `SIG&#8217;). There is no default <i>job</i>; saying just `kill&#8217; does not send a signal to the current job. If the signal being sent is TERM (terminate) or HUP (hangup), then the job or process is sent a CONT (continue) signal as well. The third form lists the signal names.</p>
<dt><code>limit </code>[<code>-h</code>] [<i>resource</i> [<i>maximum-use</i>]]</p>
<dd> Limits the consumption by the current process and each process it creates to not individually exceed <i>maximum-use</i> on the specified <i>resource</i>. If no <i>maximum-use</i> is given, then the current limit is printed; if no <i>resource</i> is given, then all limitations are given. If the <code>-h</code> flag is given, the hard limits are used instead of the current limits. The hard limits impose a ceiling on the values of the current limits. Only the super-user may raise the hard limits, but a user may lower or raise the current limits within the legal range.</p>
<dl>
<dt>
<dd>
<p> Controllable resources currently include (if supported by the OS):</p>
<dl>
<dt><i>cputime</i></p>
<dd> the maximum number of cpu-seconds to be used by each process</p>
<dt><i>filesize</i></p>
<dd> the largest single file which can be created</p>
<dt><i>datasize</i></p>
<dd> the maximum growth of the data+stack region via <a href="/docs/linux/man/2-sbrk/">sbrk</a>(2) beyond the end of the program text</p>
<dt><i>stacksize</i></p>
<dd> the maximum size of the automatically-extended stack region</p>
<dt><i>coredumpsize</i></p>
<dd> the size of the largest core dump that will be created</p>
<dt><i>memoryuse</i></p>
<dd> the maximum amount of physical memory a process may have allocated to it at a given time (this is not implemented in the 2.6+ kernel, so there is no effect introduced by changing this value)</p>
<dt><i>vmemoryuse</i></p>
<dd> the maximum amount of virtual memory a process may have allocated to it at a given time (address space)</p>
<dt><i>vmemoryuse</i></p>
<dd> the maximum amount of virtual memory a process may have allocated to it at a given time</p>
<dt><i>heapsize</i></p>
<dd> the maximum amount of memory a process may allocate per <i>brk()</i> system call</p>
<dt><i>descriptors</i> or <i>openfiles</i></p>
<dd> the maximum number of open files for this process</p>
<dt><i>concurrency</i></p>
<dd> the maximum number of threads for this process</p>
<dt><i>memorylocked</i></p>
<dd> the maximum size which a process may lock into memory using <a href="/docs/linux/man/2-mlock/">mlock</a>(2)</p>
<dt><i>maxproc</i></p>
<dd> the maximum number of simultaneous processes for this user id</p>
<dt><i>sbsize</i></p>
<dd> the maximum size of socket buffer usage for this user</p>
<dt><i>swapsize</i></p>
<dd> the maximum amount of swap space reserved or used for this user</p>
<dt><i>maxlocks</i></p>
<dd> the maximum number of locks for this user</p>
<dt><i>maxsignal</i></p>
<dd> the maximum number of pending signals for this user</p>
<dt><i>maxmessage</i></p>
<dd> the maximum number of bytes in POSIX mqueues for this user</p>
<dt><i>maxnice</i></p>
<dd> the maximum nice priority the user is allowed to raise mapped from [19&#8230;-20] to [0&#8230;39] for this user</p>
<dt><i>maxrtprio</i></p>
<dd> the maximum realtime priority for this user <i>maxrttime</i> the timeout for RT tasks in microseconds for this user.</dl>
<p> <i>maximum-use</i> may be given as a (floating point or integer) number followed by a scale factor. For all limits other than <i>cputime</i> the default scale is `k&#8217; or `kilobytes&#8217; (1024 bytes); a scale factor of `m&#8217; or `megabytes&#8217; or `g&#8217; or `gigabytes&#8217; may also be used. For <i>cputime</i> the default scaling is `seconds&#8217;, while `m&#8217; for minutes or `h&#8217; for hours, or a time of the form `mm:ss&#8217; giving minutes and seconds may be used. </p>
<p> If <i>maximum-use</i> is `unlimited&#8217;, then the limitation on the specified <i>resource</i> is removed (this is equivalent to the <i>unlimit</i> builtin command). </p>
<p> For both <i>resource</i> names and scale factors, unambiguous prefixes of the names suffice.</dl>
<dt><code>log </code>(+)</p>
<dd> Prints the <code>watch</code> shell variable and reports on each user indicated in <code>watch</code> who is logged in, regardless of when they last logged in. See also <i>watchlog</i>.</p>
<dt><code>login</code></p>
<dd> Terminates a login shell, replacing it with an instance of <i>/bin/login</i>. This is one way to log off, included for compatibility with <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1).</p>
<dt><code>logout</code></p>
<dd> Terminates a login shell. Especially useful if <code>ignoreeof</code> is set.</p>
<dt><code>ls-F </code>[-<i>switch</i> &#8230;] [<i>file</i> &#8230;] (+)</p>
<dd> Lists files like `ls -F&#8217;, but much faster. It identifies each type of special file in the listing with a special character:</dl>
<dl>
<dt>
<dd>
<dl>
<dt>/</p>
<dd> Directory</p>
<dt>*</p>
<dd> Executable</p>
<dt>#</p>
<dd> Block device</p>
<dt>%</p>
<dd> Character device</p>
<dt>|</p>
<dd> Named pipe (systems with named pipes only)</p>
<dt>=</p>
<dd> Socket (systems with sockets only)</p>
<dt>@</p>
<dd> Symbolic link (systems with symbolic links only)</p>
<dt>+</p>
<dd> Hidden directory (AIX only) or context dependent (HP/UX only)</p>
<dt>:</p>
<dd> Network special (HP/UX only)</dl>
<p> If the <code>listlinks</code> shell variable is set, symbolic links are identified in more detail (on only systems that have them, of course): </p>
<dl>
<dt>@</p>
<dd> Symbolic link to a non-directory</p>
<dt>&gt;</p>
<dd> Symbolic link to a directory</p>
<dt>&amp;</p>
<dd> Symbolic link to nowhere</dl>
<p> <code>listlinks</code> also slows down <i>ls-F</i> and causes partitions holding files pointed to by symbolic links to be mounted. </p>
<p> If the <code>listflags</code> shell variable is set to `x&#8217;, `a&#8217; or `A&#8217;, or any combination thereof (e.g., `xA&#8217;), they are used as flags to <i>ls-F</i>, making it act like `ls -xF&#8217;, `ls -Fa&#8217;, `ls -FA&#8217; or a combination (e.g., `ls -FxA&#8217;). On machines where `ls -C&#8217; is not the default, <i>ls-F</i> acts like `ls -CF&#8217;, unless <code>listflags</code> contains an `x&#8217;, in which case it acts like `ls -xF&#8217;. <i>ls-F</i> passes its arguments to <i><a href="/docs/linux/man/1-ls/">ls</a></i>(1) if it is given any switches, so `alias ls ls-F&#8217; generally does the right thing. </p>
<p> The <code>ls-F</code> builtin can list files using different colors depending on the filetype or extension. See the <code>color</code> shell variable and the <code>LS_COLORS</code> environment variable.</dl>
<p> <code>migrate </code>[<code>&#8211;</code><i>site</i>] <i>pid</i>|<code>%</code><i>jobid</i> &#8230; (+)</p>
<dl>
<dt><code>migrate &#8211;</code><i>site</i> (+)</p>
<dd> The first form migrates the process or job to the site specified or the default site determined by the system path. The second form is equivalent to `migrate &#8211;<i>site</i> $$&#8217;: it migrates the current process to the specified site. Migrating the shell itself can cause unexpected behavior, because the shell does not like to lose its tty. (TCF only)</p>
<dt><code>newgrp </code>[<code>&#8211;</code>] <i>[group]</i> (+)</p>
<dd> Equivalent to `exec newgrp&#8217;; see <i><a href="/docs/linux/man/1-newgrp/">newgrp</a></i>(1). Available only if the shell was so compiled; see the <code>version</code> shell variable.</p>
<dt><code>nice </code>[<code>+</code><i>number</i>] [<i>command</i>]</p>
<dd> Sets the scheduling priority for the shell to <i>number</i>, or, without <i>number</i>, to 4. With <i>command</i>, runs <i>command</i> at the appropriate priority. The greater the <i>number</i>, the less cpu the process gets. The super-user may specify negative priority by using `nice -number &#8230;&#8217;. Command is always executed in a sub-shell, and the restrictions placed on commands in simple <i>if</i> statements apply.</p>
<dt><code>nohup </code>[<i>command</i>]</p>
<dd> With <i>command</i>, runs <i>command</i> such that it will ignore hangup signals. Note that commands may set their own response to hangups, overriding <i>nohup</i>. Without an argument, causes the non-interactive shell only to ignore hangups for the remainder of the script. See also <code>Signal handling</code> and the <i>hup</i> builtin command.</p>
<dt><code>notify </code>[<code>%</code><i>job</i> &#8230;]</p>
<dd> Causes the shell to notify the user asynchronously when the status of any of the specified jobs (or, without %<i>job</i>, the current job) changes, instead of waiting until the next prompt as is usual. <i>job</i> may be a number, a string, `&#8217;, `%&#8217;, `+&#8217; or `-&#8216; as described under <code>Jobs</code>. See also the <code>notify</code> shell variable.</p>
<dt><code>onintr </code>[<code>&#8211;</code>|<i>label</i>]</p>
<dd> Controls the action of the shell on interrupts. Without arguments, restores the default action of the shell on interrupts, which is to terminate shell scripts or to return to the terminal command input level. With `-&#8216;, causes all interrupts to be ignored. With <i>label</i>, causes the shell to execute a `goto <i>label</i>&#8216; when an interrupt is received or a child process terminates because it was interrupted.</p>
<dt>
<dd> <i>onintr</i> is ignored if the shell is running detached and in system startup files (see <code>FILES</code>), where interrupts are disabled anyway.</p>
<dt><code>popd </code>[<code>-p</code>] [<code>-l</code>] [<code>-n</code>|<code>-v</code>] [<code>+</code><i>n</i>]</p>
<dd> Without arguments, pops the directory stack and returns to the new top directory. With a number `+<i>n</i>&#8216;, discards the <i>n</i>&#8216;th entry in the stack.</p>
<dt>
<dd> Finally, all forms of <i>popd</i> print the final directory stack, just like <i>dirs</i>. The <code>pushdsilent</code> shell variable can be set to prevent this and the <code>-p</code> flag can be given to override <code>pushdsilent</code>. The <code>-l</code>, <code>-n</code> and <code>-v</code> flags have the same effect on <i>popd</i> as on <i>dirs</i>. (+)</p>
<dt><code>printenv </code>[<i>name</i>] (+)</p>
<dd> Prints the names and values of all environment variables or, with <i>name</i>, the value of the environment variable <i>name</i>.</p>
<dt><code>pushd </code>[<code>-p</code>] [<code>-l</code>] [<code>-n</code>|<code>-v</code>] [<i>name</i>|<code>+</code><i>n</i>]</p>
<dd> Without arguments, exchanges the top two elements of the directory stack. If <code>pushdtohome</code> is set, <i>pushd</i> without arguments does `pushd ~&#8217;, like <i>cd</i>. (+) With <i>name</i>, pushes the current working directory onto the directory stack and changes to <i>name</i>. If <i>name</i> is `-&#8216; it is interpreted as the previous working directory (see <code>Filename substitution</code>). (+) If <code>dunique</code> is set, <i>pushd</i> removes any instances of <i>name</i> from the stack before pushing it onto the stack. (+) With a number `+<i>n</i>&#8216;, rotates the <i>n</i>th element of the directory stack around to be the top element and changes to it. If <code>dextract</code> is set, however, `pushd +<i>n</i>&#8216; extracts the <i>n</i>th directory, pushes it onto the top of the stack and changes to it. (+)</p>
<dt>
<dd> Finally, all forms of <i>pushd</i> print the final directory stack, just like <i>dirs</i>. The <code>pushdsilent</code> shell variable can be set to prevent this and the <code>-p</code> flag can be given to override <code>pushdsilent</code>. The <code>-l</code>, <code>-n</code> and <code>-v</code> flags have the same effect on <i>pushd</i> as on <i>dirs</i>. (+)</p>
<dt><code>rehash</code></p>
<dd> Causes the internal hash table of the contents of the directories in the <code>path</code> variable to be recomputed. This is needed if the <code>autorehash</code> shell variable is not set and new commands are added to directories in <code>path</code> while you are logged in. With <code>autorehash</code>, a new command will be found automatically, except in the special case where another command of the same name which is located in a different directory already exists in the hash table. Also flushes the cache of home directories built by tilde expansion.</p>
<dt><code>repeat </code><i>count command</i></p>
<dd> The specified <i>command</i>, which is subject to the same restrictions as the <i>command</i> in the one line <i>if</i> statement above, is executed <i>count</i> times. I/O redirections occur exactly once, even if <i>count</i> is 0.</p>
<dt><code>rootnode //</code><i>nodename </i>(+)</p>
<dd> Changes the rootnode to //<i>nodename</i>, so that `/&#8217; will be interpreted as `//<i>nodename</i>&#8216;. (Domain/OS only)</dl>
<p> <code>sched </code>(+)<br />
 <code>sched </code>[<code>+</code>]<i>hh:mm command</i> (+)</p>
<dl>
<dt><code>sched &#8211;</code><i>n</i> (+)</p>
<dd> The first form prints the scheduled-event list. The <code>sched</code> shell variable may be set to define the format in which the scheduled-event list is printed. The second form adds <i>command</i> to the scheduled-event list. For example,</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &gt; sched 11:00 echo It\&#8217;s eleven o\&#8217;clock.</dl>
<p> causes the shell to echo `It&#8217;s eleven o&#8217;clock.&#8217; at 11 AM. The time may be in 12-hour AM/PM format</p>
<dl>
<dt>
<dd> &gt; sched 5pm set prompt='[%h] It\&#8217;s after 5; go home: &gt;&#8217;</dl>
<p> or may be relative to the current time:</p>
<dl>
<dt>
<dd> &gt; sched +2:15 /usr/lib/uucp/uucico -r1 -sother</dl>
<p> A relative time specification may not use AM/PM format. The third form removes item <i>n</i> from the event list:</p>
<dl>
<dt>
<dd> &gt; sched </p>
<p>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>Wed Apr&nbsp;<wbr>&nbsp;<wbr>4 15:42&nbsp;<wbr>&nbsp;<wbr>/usr/lib/uucp/uucico -r1 -sother </p>
<p>&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>Wed Apr&nbsp;<wbr>&nbsp;<wbr>4 17:00&nbsp;<wbr>&nbsp;<wbr>set prompt=[%h]&nbsp;<wbr>It&#8217;s after 5;&nbsp;<wbr>go home:&nbsp;<wbr>&gt;<br />
 &gt; sched -2<br />
 &gt; sched </p>
<p>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>Wed Apr&nbsp;<wbr>&nbsp;<wbr>4 15:42&nbsp;<wbr>&nbsp;<wbr>/usr/lib/uucp/uucico -r1 -sother</dl>
<p> A command in the scheduled-event list is executed just before the first prompt is printed after the time when the command is scheduled. It is possible to miss the exact time when the command is to be run, but an overdue command will execute at the next prompt. A command which comes due while the shell is waiting for user input is executed immediately. However, normal operation of an already-running command will not be interrupted so that a scheduled-event list element may be run. </p>
<p> This mechanism is similar to, but not the same as, the <i><a href="/docs/linux/man/1-at/">at</a></i>(1) command on some Unix systems. Its major disadvantage is that it may not run a command at exactly the specified time. Its major advantage is that because <i>sched</i> runs directly from the shell, it has access to shell variables and other structures. This provides a mechanism for changing one&#8217;s working environment based on the time of day.</dl>
</dl>
<p> <code>set</code><br />
 <code>set </code><i>name</i> &#8230;<br />
 <code>set </code><i>name</i><code>=</code><i>word</i> &#8230;<br />
 <code>set [-r] [-f|-l] </code><i>name</i><code>=(</code><i>wordlist</i><code>)</code> &#8230; (+)<br />
 <code>set </code><i>name[index]</i><code>=</code><i>word</i> &#8230;<br />
 <code>set -r </code>(+)<br />
 <code>set -r </code><i>name</i> &#8230; (+)</p>
<dl>
<dt><code>set -r </code><i>name</i><code>=</code><i>word</i> &#8230; (+)</p>
<dd> The first form of the command prints the value of all shell variables. Variables which contain more than a single word print as a parenthesized word list. The second form sets <i>name</i> to the null string. The third form sets <i>name</i> to the single <i>word</i>. The fourth form sets <i>name</i> to the list of words in <i>wordlist</i>. In all cases the value is command and filename expanded. If <code>-r</code> is specified, the value is set read-only. If <code>-f</code> or <code>-l</code> are specified, set only unique words keeping their order. <code>-f</code> prefers the first occurrence of a word, and <code>-l</code> the last. The fifth form sets the <i>index</i>&#8216;th component of <i>name</i> to <i>word</i>; this component must already exist. The sixth form lists only the names of all shell variables that are read-only. The seventh form makes <i>name</i> read-only, whether or not it has a value. The eighth form is the same as the third form, but make <i>name</i> read-only at the same time.</p>
<dt>
<dd> These arguments can be repeated to set and/or make read-only multiple variables in a single set command. Note, however, that variable expansion happens for all arguments before any setting occurs. Note also that `=&#8217; can be adjacent to both <i>name</i> and <i>word</i> or separated from both by whitespace, but cannot be adjacent to only one or the other. See also the <i>unset</i> builtin command.</p>
<dt><code>setenv </code>[<i>name </i>[<i>value</i>]]</p>
<dd> Without arguments, prints the names and values of all environment variables. Given <i>name</i>, sets the environment variable <i>name</i> to <i>value</i> or, without <i>value</i>, to the null string.</p>
<dt><code>setpath </code><i>path </i>(+)</p>
<dd> Equivalent to <i><a href="/docs/linux/man/1-setpath/">setpath</a></i>(1). (Mach only)</p>
<dt><code>setspath</code> LOCAL|<i>site</i>|<i>cpu</i> &#8230; (+)</p>
<dd> Sets the system execution path. (TCF only)</p>
<dt><code>settc </code><i>cap value </i>(+)</p>
<dd> Tells the shell to believe that the terminal capability <i>cap</i> (as defined in <i><a href="/docs/linux/man/5-termcap/">termcap</a></i>(5)) has the value <i>value</i>. No sanity checking is done. Concept terminal users may have to `settc xn no&#8217; to get proper wrapping at the rightmost column.</p>
<dt><code>setty </code>[<code>-d</code>|<code>-q</code>|<code>-x</code>] [<code>-a</code>] [[<code>+</code>|<code>&#8211;</code>]<i>mode</i>] (+)</p>
<dd> Controls which tty modes (see <code>Terminal management</code>) the shell does not allow to change. <code>-d</code>, <code>-q</code> or <code>-x</code> tells <i>setty</i> to act on the `edit&#8217;, `quote&#8217; or `execute&#8217; set of tty modes respectively; without <code>-d</code>, <code>-q</code> or <code>-x</code>, `execute&#8217; is used.</p>
<dt>
<dd> Without other arguments, <i>setty</i> lists the modes in the chosen set which are fixed on (`+mode&#8217;) or off (`-mode&#8217;). The available modes, and thus the display, vary from system to system. With <code>-a</code>, lists all tty modes in the chosen set whether or not they are fixed. With <code>+</code><i>mode</i>, <code>&#8211;</code><i>mode</i> or <i>mode</i>, fixes <i>mode</i> on or off or removes control from <i>mode</i> in the chosen set. For example, `setty +echok echoe&#8217; fixes `echok&#8217; mode on and allows commands to turn `echoe&#8217; mode on or off, both when the shell is executing commands.</p>
<dt><code>setxvers</code> [<i>string</i>] (+)</p>
<dd> Set the experimental version prefix to <i>string</i>, or removes it if <i>string</i> is omitted. (TCF only)</p>
<dt><code>shift </code>[<i>variable</i>]</p>
<dd> Without arguments, discards <code>argv</code>[1] and shifts the members of <code>argv</code> to the left. It is an error for <code>argv</code> not to be set or to have less than one word as value. With <i>variable</i>, performs the same function on <i>variable</i>.</p>
<dt><code>source </code>[<code>-h</code>] <i>name</i> [<i>args</i> &#8230;]</p>
<dd> The shell reads and executes commands from <i>name</i>. The commands are not placed on the history list. If any <i>args</i> are given, they are placed in <code>argv</code>. (+) <i>source</i> commands may be nested; if they are nested too deeply the shell may run out of file descriptors. An error in a <i>source</i> at any level terminates all nested <i>source</i> commands. With <code>-h</code>, commands are placed on the history list instead of being executed, much like `history -L&#8217;.</p>
<dt><code>stop %</code><i>job</i>|<i>pid</i> &#8230;</p>
<dd> Stops the specified jobs or processes which are executing in the background. <i>job</i> may be a number, a string, `&#8217;, `%&#8217;, `+&#8217; or `-&#8216; as described under <code>Jobs</code>. There is no default <i>job</i>; saying just `stop&#8217; does not stop the current job.</p>
<dt><code>suspend</code></p>
<dd> Causes the shell to stop in its tracks, much as if it had been sent a stop signal with <code>^Z</code>. This is most often used to stop shells started by <i><a href="/docs/linux/man/1-su/">su</a></i>(1).</dl>
<p> <code>switch (</code><i>string</i><code>)</code><br />
 <code>case </code><i>str1</i><code>:</code></p>
<dl>
<dt>
<dd> &#8230;<br />
 <code>breaksw</code></dl>
<p> &#8230; </p>
<p> <code>default:</code></p>
<dl>
<dt>
<dd> &#8230;<br />
 <code>breaksw</code></p>
<dt><code>endsw</code></p>
<dd> Each case label is successively matched, against the specified <i>string</i> which is first command and filename expanded. The file metacharacters `*&#8217;, `?&#8217; and `[&#8230;]&#8217; may be used in the case labels, which are variable expanded. If none of the labels match before a `default&#8217; label is found, then the execution begins after the default label. Each case label and the default label must appear at the beginning of a line. The command <i>breaksw</i> causes execution to continue after the <i>endsw</i>. Otherwise control may fall through case labels and default labels as in C. If no label matches and there is no default, execution continues after the <i>endsw</i>.</p>
<dt><code>telltc </code>(+)</p>
<dd> Lists the values of all terminal capabilities (see <i><a href="/docs/linux/man/5-termcap/">termcap</a></i>(5)).</p>
<dt><code>termname </code>[<i>terminal type</i>] (+)</p>
<dd> Tests if <i>terminal type</i> (or the current value of <code>TERM</code> if no <i>terminal type</i> is given) has an entry in the hosts <a href="/docs/linux/man/5-termcap/">termcap</a>(5) or <a href="/docs/linux/man/5-terminfo/">terminfo</a>(5) database. Prints the terminal type to stdout and returns 0 if an entry is present otherwise returns 1.</p>
<dt><code>time </code>[<i>command</i>]</p>
<dd> Executes <i>command</i> (which must be a simple command, not an alias, a pipeline, a command list or a parenthesized command list) and prints a time summary as described under the <code>time</code> variable. If necessary, an extra shell is created to print the time statistic when the command completes. Without <i>command</i>, prints a time summary for the current shell and its children.</p>
<dt><code>umask </code>[<i>value</i>]</p>
<dd> Sets the file creation mask to <i>value</i>, which is given in octal. Common values for the mask are 002, giving all access to the group and read and execute access to others, and 022, giving read and execute access to the group and others. Without <i>value</i>, prints the current file creation mask.</p>
<dt><code>unalias </code><i>pattern</i></p>
<dd>
 Removes all aliases whose names match <i>pattern</i>. `unalias *&#8217; thus removes all aliases. It is not an error for nothing to be <i>unalias</i>ed.</p>
<dt><code>uncomplete </code><i>pattern</i> (+)</p>
<dd> Removes all completions whose names match <i>pattern</i>. `uncomplete *&#8217; thus removes all completions. It is not an error for nothing to be <i>uncomplete</i>d.</p>
<dt><code>unhash</code></p>
<dd> Disables use of the internal hash table to speed location of executed programs.</p>
<dt><code>universe </code><i>universe</i> (+)</p>
<dd> Sets the universe to <i>universe</i>. (Masscomp/RTU only)</p>
<dt><code>unlimit </code>[<code>-hf</code>] [<i>resource</i>]</p>
<dd> Removes the limitation on <i>resource</i> or, if no <i>resource</i> is specified, all <i>resource</i> limitations. With <code>-h</code>, the corresponding hard limits are removed. Only the super-user may do this. Note that <code>unlimit</code> may not exit successful, since most systems do not allow <i>descriptors</i> to be unlimited. With <code>-f</code> errors are ignored.</p>
<dt><code>unset </code><i>pattern</i></p>
<dd> Removes all variables whose names match <i>pattern</i>, unless they are read-only. `unset *&#8217; thus removes all variables unless they are read-only; this is a bad idea. It is not an error for nothing to be <i>unset</i>.</p>
<dt><code>unsetenv </code><i>pattern</i></p>
<dd> Removes all environment variables whose names match <i>pattern</i>. `unsetenv *&#8217; thus removes all environment variables; this is a bad idea. It is not an error for nothing to be <i>unsetenv</i>ed.</p>
<dt><code>ver </code>[<i>systype</i> [<i>command</i>]] (+)</p>
<dd> Without arguments, prints <code>SYSTYPE</code>. With <i>systype</i>, sets <code>SYSTYPE</code> to <i>systype</i>. With <i>systype</i> and <i>command</i>, executes <i>command</i> under <i>systype</i>. <i>systype</i> may be `bsd4.3&#8242; or `sys5.3&#8242;. (Domain/OS only)</p>
<dt><code>wait</code></p>
<dd> The shell waits for all background jobs. If the shell is interactive, an interrupt will disrupt the wait and cause the shell to print the names and job numbers of all outstanding jobs.</p>
<dt><code>warp </code><i>universe</i> (+)</p>
<dd> Sets the universe to <i>universe</i>. (Convex/OS only)</p>
<dt><code>watchlog </code>(+)</p>
<dd> An alternate name for the <i>log</i> builtin command (q.v.). Available only if the shell was so compiled; see the <code>version</code> shell variable.</p>
<dt><code>where </code><i>command</i> (+)</p>
<dd> Reports all known instances of <i>command</i>, including aliases, builtins and executables in <code>path</code>.</p>
<dt><code>which</code> <i>command</i> (+)</p>
<dd> Displays the command that will be executed by the shell after substitutions, <code>path</code> searching, etc. The builtin command is just like <i><a href="/docs/linux/man/1-which/">which</a></i>(1), but it correctly reports <i>tcsh</i> aliases and builtins and is 10 to 100 times faster. See also the <i>which-command</i> editor command.</dl>
<p> <code>while (</code><i>expr</i><code>)</code><br />
 &#8230;</p>
<dl>
<dt><code>end</code></p>
<dd> Executes the commands between the <i>while</i> and the matching <i>end</i> while <i>expr</i> (an expression, as described under <code>Expressions</code>) evaluates non-zero. <i>while</i> and <i>end</i> must appear alone on their input lines. <i>break</i> and <i>continue</i> may be used to terminate or continue the loop prematurely. If the input is a terminal, the user is prompted the first time through the loop as with <i>foreach</i>.</dl>
<h3>Special aliases (+)</h3>
<p> If set, each of these aliases executes automatically at the indicated time. They are all initially undefined.</p>
<dl>
<dt><code>beepcmd</code></p>
<dd> Runs when the shell wants to ring the terminal bell.</p>
<dt><code>cwdcmd</code></p>
<dd> Runs after every change of working directory. For example, if the user is working on an X window system using <i><a href="/docs/linux/man/1-xterm/">xterm</a></i>(1) and a re-parenting window manager that supports title bars such as <i><a href="/docs/linux/man/1-twm/">twm</a></i>(1) and does</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &gt; alias cwdcmd &#8216;echo -n &quot;^[]2;${HOST}:$cwd ^G&quot;&#8217;</dl>
<p> then the shell will change the title of the running <i><a href="/docs/linux/man/1-xterm/">xterm</a></i>(1) to be the name of the host, a colon, and the full current working directory. A fancier way to do that is</p>
<dl>
<dt>
<dd> &gt; alias cwdcmd &#8216;echo -n &quot;^[]2;${HOST}:$cwd^G^[]1;${HOST}^G&quot;&#8217;</dl>
<p> This will put the hostname and working directory on the title bar but only the hostname in the icon manager menu. </p>
<p> Note that putting a <i>cd</i>, <i>pushd</i> or <i>popd</i> in <i>cwdcmd</i> may cause an infinite loop. It is the author&#8217;s opinion that anyone doing so will get what they deserve.</dl>
<dt><code>jobcmd</code></p>
<dd> Runs before each command gets executed, or when the command changes state. This is similar to <i>postcmd</i>, but it does not print builtins.</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &gt; alias jobcmd &#8216;echo -n &quot;^[]2\;\!#:q^G&quot;&#8217;</dl>
<p> then executing <i>vi foo.c</i> will put the command string in the xterm title bar.</dl>
<dt><code>helpcommand</code></p>
<dd> Invoked by the <code>run-help</code> editor command. The command name for which help is sought is passed as sole argument. For example, if one does</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &gt; alias helpcommand &#8216;\!:1 &#8211;help&#8217;</dl>
<p> then the help display of the command itself will be invoked, using the GNU help calling convention. Currently there is no easy way to account for various calling conventions (e.g., the customary Unix `-h&#8217;), except by using a table of many commands.</dl>
<dt><code>periodic</code></p>
<dd> Runs every <code>tperiod</code> minutes. This provides a convenient means for checking on common but infrequent changes such as new mail. For example, if one does</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &gt; set tperiod = 30<br />
 &gt; alias periodic checknews</dl>
<p> then the <i><a href="/docs/linux/man/1-checknews/">checknews</a></i>(1) program runs every 30 minutes. If <i>periodic</i> is set but <code>tperiod</code> is unset or set to 0, <i>periodic</i> behaves like <i>precmd</i>.</dl>
<dt><code>precmd</code></p>
<dd> Runs just before each prompt is printed. For example, if one does</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &gt; alias precmd date</dl>
<p> then <i><a href="/docs/linux/man/1-date/">date</a></i>(1) runs just before the shell prompts for each command. There are no limits on what <i>precmd</i> can be set to do, but discretion should be used.</dl>
<dt><code>postcmd</code></p>
<dd> Runs before each command gets executed.</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &gt; alias postcmd &#8216;echo -n &quot;^[]2\;\!#:q^G&quot;&#8217;</dl>
<p> then executing <i>vi foo.c</i> will put the command string in the xterm title bar.</dl>
<dt><code>shell</code></p>
<dd> Specifies the interpreter for executable scripts which do not themselves specify an interpreter. The first word should be a full path name to the desired interpreter (e.g., `/bin/csh&#8217; or `/usr/local/bin/tcsh&#8217;).</dl>
<h3>Special shell variables</h3>
<p> The variables described in this section have special meaning to the shell. </p>
<p> The shell sets <code>addsuffix</code>, <code>argv</code>, <code>autologout</code>, <code>csubstnonl</code>, <code>command</code>, <code>echo_style</code>, <code>edit</code>, <code>gid</code>, <code>group</code>, <code>home</code>, <code>loginsh</code>, <code>oid</code>, <code>path</code>, <code>prompt</code>, <code>prompt2</code>, <code>prompt3</code>, <code>shell</code>, <code>shlvl</code>, <code>tcsh</code>, <code>term</code>, <code>tty</code>, <code>uid</code>, <code>user</code> and <code>version</code> at startup; they do not change thereafter unless changed by the user. The shell updates <code>cwd</code>, <code>dirstack</code>, <code>owd</code> and <code>status</code> when necessary, and sets <code>logout</code> on logout. </p>
<p> The shell synchronizes <code>group</code>, <code>home</code>, <code>path</code>, <code>shlvl</code>, <code>term</code> and <code>user</code> with the environment variables of the same names: whenever the environment variable changes the shell changes the corresponding shell variable to match (unless the shell variable is read-only) and vice versa. Note that although <code>cwd</code> and <code>PWD</code> have identical meanings, they are not synchronized in this manner, and that the shell automatically converts between the different formats of <code>path</code> and <code>PATH</code>.</p>
<dl>
<dt><code>addsuffix </code>(+)</p>
<dd> If set, filename completion adds `/&#8217; to the end of directories and a space to the end of normal files when they are matched exactly. Set by default.</p>
<dt><code>afsuser </code>(+)</p>
<dd> If set, <code>autologout</code>&#8216;s autolock feature uses its value instead of the local username for kerberos authentication.</p>
<dt><code>ampm </code>(+)</p>
<dd> If set, all times are shown in 12-hour AM/PM format.</p>
<dt><code>argv</code></p>
<dd> The arguments to the shell. Positional parameters are taken from <code>argv</code>, i.e., `$1&#8242; is replaced by `$argv[1]&#8217;, etc. Set by default, but usually empty in interactive shells.</p>
<dt><code>autocorrect </code>(+)</p>
<dd> If set, the <i>spell-word</i> editor command is invoked automatically before each completion attempt.</p>
<dt><code>autoexpand </code>(+)</p>
<dd> If set, the <i>expand-history</i> editor command is invoked automatically before each completion attempt. If this is set to <i>onlyhistory</i>, then only history will be expanded and a second completion will expand filenames.</p>
<dt><code>autolist </code>(+)</p>
<dd> If set, possibilities are listed after an ambiguous completion. If set to `ambiguous&#8217;, possibilities are listed only when no new characters are added by completion.</p>
<dt><code>autologout </code>(+)</p>
<dd> The first word is the number of minutes of inactivity before automatic logout. The optional second word is the number of minutes of inactivity before automatic locking. When the shell automatically logs out, it prints `auto-logout&#8217;, sets the variable <code>logout</code> to `automatic&#8217; and exits. When the shell automatically locks, the user is required to enter his password to continue working. Five incorrect attempts result in automatic logout. Set to `60&#8242; (automatic logout after 60 minutes, and no locking) by default in login and superuser shells, but not if the shell thinks it is running under a window system (i.e., the <code>DISPLAY</code> environment variable is set), the tty is a pseudo-tty (pty) or the shell was not so compiled (see the <code>version</code> shell variable). See also the <code>afsuser</code> and <code>logout</code> shell variables.</p>
<dt><code>autorehash </code>(+)</p>
<dd> If set, the internal hash table of the contents of the directories in the <code>path</code> variable will be recomputed if a command is not found in the hash table. In addition, the list of available commands will be rebuilt for each command completion or spelling correction attempt if set to `complete&#8217; or `correct&#8217; respectively; if set to `always&#8217;, this will be done for both cases.</p>
<dt><code>backslash_quote </code>(+)</p>
<dd> If set, backslashes (`\&#8217;) always quote `\&#8217;, `&#8221;, and `&quot;&#8217;. This may make complex quoting tasks easier, but it can cause syntax errors in <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1) scripts.</p>
<dt><code>catalog</code></p>
<dd> The file name of the message catalog. If set, tcsh use `tcsh.${catalog}&#8217; as a message catalog instead of default `tcsh&#8217;.</p>
<dt><code>cdpath</code></p>
<dd> A list of directories in which <i>cd</i> should search for subdirectories if they aren&#8217;t found in the current directory.</p>
<dt><code>color</code></p>
<dd> If set, it enables color display for the builtin <code>ls-F</code> and it passes <code>&#8211;color=auto</code> to <code>ls</code>. Alternatively, it can be set to only <code>ls-F</code> or only <code>ls</code> to enable color to only one command. Setting it to nothing is equivalent to setting it to <code>(ls-F ls)</code>.</p>
<dt><code>colorcat</code></p>
<dd> If set, it enables color escape sequence for NLS message files. And display colorful NLS messages.</p>
<dt><code>command </code>(+)</p>
<dd> If set, the command which was passed to the shell with the <code>-c</code> flag (q.v.).</p>
<dt><code>compat_expr </code>(+)</p>
<dd> If set, the shell will evaluate expressions right to left, like the original <i>csh</i>.</p>
<dt><code>complete </code>(+)</p>
<dd> If set to `igncase&#8217;, the completion becomes case insensitive. If set to `enhance&#8217;, completion ignores case and considers hyphens and underscores to be equivalent; it will also treat periods, hyphens and underscores (`.&#8217;, `-&#8216; and `_&#8217;) as word separators. If set to `Enhance&#8217;, completion matches uppercase and underscore characters explicitly and matches lowercase and hyphens in a case-insensivite manner; it will treat periods, hypens and underscores as word separators.</p>
<dt><code>continue </code>(+)</p>
<dd> If set to a list of commands, the shell will continue the listed commands, instead of starting a new one.</p>
<dt><code>continue_args </code>(+)</p>
<dd> Same as continue, but the shell will execute:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> echo `pwd` $argv &gt; ~/.&lt;cmd&gt;_pause; %&lt;cmd&gt;</dl>
</dl>
<dt><code>correct </code>(+)</p>
<dd> If set to `cmd&#8217;, commands are automatically spelling-corrected. If set to `complete&#8217;, commands are automatically completed. If set to `all&#8217;, the entire command line is corrected.</p>
<dt><code>csubstnonl </code>(+)</p>
<dd> If set, newlines and carriage returns in command substitution are replaced by spaces. Set by default.</p>
<dt><code>cwd</code></p>
<dd> The full pathname of the current directory. See also the <code>dirstack</code> and <code>owd</code> shell variables.</p>
<dt><code>dextract </code>(+)</p>
<dd> If set, `pushd +<i>n</i>&#8216; extracts the <i>n</i>th directory from the directory stack rather than rotating it to the top.</p>
<dt><code>dirsfile </code>(+)</p>
<dd> The default location in which `dirs -S&#8217; and `dirs -L&#8217; look for a history file. If unset, <i>~/.cshdirs</i> is used. Because only <i>~/.tcshrc</i> is normally sourced before <i>~/.cshdirs</i>, <code>dirsfile</code> should be set in <i>~/.tcshrc</i> rather than <i>~/.login</i>.</p>
<dt><code>dirstack </code>(+)</p>
<dd> An array of all the directories on the directory stack. `$dirstack[1]&#8217; is the current working directory, `$dirstack[2]&#8217; the first directory on the stack, etc. Note that the current working directory is `$dirstack[1]&#8217; but `=0&#8242; in directory stack substitutions, etc. One can change the stack arbitrarily by setting <code>dirstack</code>, but the first element (the current working directory) is always correct. See also the <code>cwd</code> and <code>owd</code> shell variables.</p>
<dt><code>dspmbyte </code>(+)</p>
<dd> Has an effect iff &#8216;dspm&#8217; is listed as part of the <code>version</code> shell variable. If set to `euc&#8217;, it enables display and editing EUC-kanji(Japanese) code. If set to `sjis&#8217;, it enables display and editing Shift-JIS(Japanese) code. If set to `big5&#8242;, it enables display and editing Big5(Chinese) code. If set to `utf8&#8242;, it enables display and editing Utf8(Unicode) code. If set to the following format, it enables display and editing of original multi-byte code format:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &gt; set dspmbyte = 0000&#8230;.(256 bytes)&#8230;.0000</dl>
<p> The table requires <code>just</code> 256 bytes. Each character of 256 characters corresponds (from left to right) to the ASCII codes 0x00, 0x01, &#8230; 0xff. Each character is set to number 0,1,2 and 3. Each number has the following meaning: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>0 &#8230; not used for multi-byte characters. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>1 &#8230; used for the first byte of a multi-byte character. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>2 &#8230; used for the second byte of a multi-byte character. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>3 &#8230; used for both the first byte and second byte of a multi-byte character. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Example:<br />
 If set to `001322&#8242;, the first character (means 0x00 of the ASCII code) and second character (means 0x01 of ASCII code) are set to `0&#8242;. Then, it is not used for multi-byte characters. The 3rd character (0x02) is set to &#8216;1&#8217;, indicating that it is used for the first byte of a multi-byte character. The 4th character(0x03) is set &#8216;3&#8217;. It is used for both the first byte and the second byte of a multi-byte character. The 5th and 6th characters (0x04,0x05) are set to &#8216;2&#8217;, indicating that they are used for the second byte of a multi-byte character. </p>
<p> The GNU fileutils version of ls cannot display multi-byte filenames without the -N ( &#8211;literal ) option. If you are using this version, set the second word of dspmbyte to &quot;ls&quot;. If not, for example, &quot;ls-F -l&quot; cannot display multi-byte filenames. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Note:<br />
 This variable can only be used if KANJI and DSPMBYTE has been defined at compile time.</dl>
<dt><code>dunique </code>(+)</p>
<dd> If set, <i>pushd</i> removes any instances of <i>name</i> from the stack before pushing it onto the stack.</p>
<dt><code>echo</code></p>
<dd> If set, each command with its arguments is echoed just before it is executed. For non-builtin commands all expansions occur before echoing. Builtin commands are echoed before command and filename substitution, because these substitutions are then done selectively. Set by the <code>-x</code> command line option.</p>
<dt><code>echo_style </code>(+)</p>
<dd> The style of the <i>echo</i> builtin. May be set to</dl>
<dl>
<dt>
<dd>
<dl>
<dt>bsd</p>
<dd> Don&#8217;t echo a newline if the first argument is `-n&#8217;.</p>
<dt>sysv</p>
<dd> Recognize backslashed escape sequences in echo strings.</p>
<dt>both</p>
<dd> Recognize both the `-n&#8217; flag and backslashed escape sequences; the default.</p>
<dt>none</p>
<dd> Recognize neither.</dl>
<p> Set by default to the local system default. The BSD and System V options are described in the <i><a href="/docs/linux/man/1-echo/">echo</a></i>(1) man pages on the appropriate systems.</dl>
<dl>
<dt><code>edit </code>(+)</p>
<dd> If set, the command-line editor is used. Set by default in interactive shells.</p>
<dt><code>ellipsis </code>(+)</p>
<dd> If set, the `%c&#8217;/`%.&#8217; and `%C&#8217; prompt sequences (see the <code>prompt</code> shell variable) indicate skipped directories with an ellipsis (`&#8230;&#8217;) instead of `/&lt;skipped&gt;&#8217;.</p>
<dt><code>euid </code>(+)</p>
<dd> The user&#8217;s effective user ID.</p>
<dt><code>euser </code>(+)</p>
<dd> The first matching passwd entry name corresponding to the effective user ID.</p>
<dt><code>fignore </code>(+)</p>
<dd> Lists file name suffixes to be ignored by completion.</p>
<dt><code>filec</code></p>
<dd> In <i>tcsh</i>, completion is always used and this variable is ignored by default. If <code>edit</code> is unset, then the traditional <i>csh</i> completion is used. If set in <i>csh</i>, filename completion is used.</p>
<dt><code>gid </code>(+)</p>
<dd> The user&#8217;s real group ID.</p>
<dt><code>globdot </code>(+)</p>
<dd> If set, wild-card glob patterns will match files and directories beginning with `.&#8217; except for `.&#8217; and `..&#8217;</p>
<dt><code>globstar </code>(+)</p>
<dd> If set, the `**&#8217; and `***&#8217; file glob patterns will match any string of characters including `/&#8217; traversing any existing sub-directories. (e.g. `ls **.c&#8217; will list all the .c files in the current directory tree). If used by itself, it will match zero or more sub-directories (e.g. `ls /usr/include/**/time.h&#8217; will list any file named `time.h&#8217; in the /usr/include directory tree; whereas `ls /usr/include/**time.h&#8217; will match any file in the /usr/include directory tree ending in `time.h&#8217;). To prevent problems with recursion, the `**&#8217; glob-pattern will not descend into a symbolic link containing a directory. To override this, use `***&#8217;</p>
<dt><code>group </code>(+)</p>
<dd> The user&#8217;s group name.</p>
<dt><code>highlight</code></p>
<dd> If set, the incremental search match (in <i>i-search-back</i> and <i>i-search-fwd</i>) and the region between the mark and the cursor are highlighted in reverse video.</p>
<dt>
<dd> Highlighting requires more frequent terminal writes, which introduces extra overhead. If you care about terminal performance, you may want to leave this unset.</p>
<dt><code>histchars</code></p>
<dd> A string value determining the characters used in <code>History substitution</code> (q.v.). The first character of its value is used as the history substitution character, replacing the default character `!&#8217;. The second character of its value replaces the character `^&#8217; in quick substitutions.</p>
<dt><code>histdup </code>(+)</p>
<dd> Controls handling of duplicate entries in the history list. If set to `all&#8217; only unique history events are entered in the history list. If set to `prev&#8217; and the last history event is the same as the current command, then the current command is not entered in the history. If set to `erase&#8217; and the same event is found in the history list, that old event gets erased and the current one gets inserted. Note that the `prev&#8217; and `all&#8217; options renumber history events so there are no gaps.</p>
<dt><code>histfile </code>(+)</p>
<dd> The default location in which `history -S&#8217; and `history -L&#8217; look for a history file. If unset, <i>~/.history</i> is used. <code>histfile</code> is useful when sharing the same home directory between different machines, or when saving separate histories on different terminals. Because only <i>~/.tcshrc</i> is normally sourced before <i>~/.history</i>, <code>histfile</code> should be set in <i>~/.tcshrc</i> rather than <i>~/.login</i>.</p>
<dt><code>histlit </code>(+)</p>
<dd> If set, builtin and editor commands and the <code>savehist</code> mechanism use the literal (unexpanded) form of lines in the history list. See also the <i>toggle-literal-history</i> editor command.</p>
<dt><code>history</code></p>
<dd> The first word indicates the number of history events to save. The optional second word (+) indicates the format in which history is printed; if not given, `%h	%T	%R
&#8217; is used. The format sequences are described below under <code>prompt</code>; note the variable meaning of `%R&#8217;. Set to `100&#8242; by default.</p>
<dt><code>home</code></p>
<dd> Initialized to the home directory of the invoker. The filename expansion of `<i>~</i>&#8216; refers to this variable.</p>
<dt><code>ignoreeof</code></p>
<dd> If set to the empty string or `0&#8242; and the input device is a terminal, the <i>end-of-file</i> command (usually generated by the user by typing `^D&#8217; on an empty line) causes the shell to print `Use &quot;exit&quot; to leave tcsh.&#8217; instead of exiting. This prevents the shell from accidentally being killed. Historically this setting exited after 26 successive EOF&#8217;s to avoid infinite loops. If set to a number <i>n</i>, the shell ignores <i>n &#8211; 1</i> consecutive <i>end-of-file</i>s and exits on the <i>n</i>th. (+) If unset, `1&#8242; is used, i.e., the shell exits on a single `^D&#8217;.</p>
<dt><code>implicitcd </code>(+)</p>
<dd> If set, the shell treats a directory name typed as a command as though it were a request to change to that directory. If set to <i>verbose</i>, the change of directory is echoed to the standard output. This behavior is inhibited in non-interactive shell scripts, or for command strings with more than one word. Changing directory takes precedence over executing a like-named command, but it is done after alias substitutions. Tilde and variable expansions work as expected.</p>
<dt><code>inputmode </code>(+)</p>
<dd> If set to `insert&#8217; or `overwrite&#8217;, puts the editor into that input mode at the beginning of each line.</p>
<dt><code>killdup </code>(+)</p>
<dd> Controls handling of duplicate entries in the kill ring. If set to `all&#8217; only unique strings are entered in the kill ring. If set to `prev&#8217; and the last killed string is the same as the current killed string, then the current string is not entered in the ring. If set to `erase&#8217; and the same string is found in the kill ring, the old string is erased and the current one is inserted.</p>
<dt><code>killring </code>(+)</p>
<dd> Indicates the number of killed strings to keep in memory. Set to `30&#8242; by default. If unset or set to less than `2&#8242;, the shell will only keep the most recently killed string. Strings are put in the killring by the editor commands that delete (kill) strings of text, e.g. <i>backward-delete-word</i>, <i>kill-line</i>, etc, as well as the <i>copy-region-as-kill</i> command. The <i>yank</i> editor command will yank the most recently killed string into the command-line, while <i>yank-pop</i> (see <code>Editor commands</code>) can be used to yank earlier killed strings.</p>
<dt><code>listflags </code>(+)</p>
<dd> If set to `x&#8217;, `a&#8217; or `A&#8217;, or any combination thereof (e.g., `xA&#8217;), they are used as flags to <i>ls-F</i>, making it act like `ls -xF&#8217;, `ls -Fa&#8217;, `ls -FA&#8217; or a combination (e.g., `ls -FxA&#8217;): `a&#8217; shows all files (even if they start with a `.&#8217;), `A&#8217; shows all files but `.&#8217; and `..&#8217;, and `x&#8217; sorts across instead of down. If the second word of <code>listflags</code> is set, it is used as the path to `<a href="/docs/linux/man/1-ls/">ls</a>(1)&#8217;.</p>
<dt><code>listjobs </code>(+)</p>
<dd> If set, all jobs are listed when a job is suspended. If set to `long&#8217;, the listing is in long format.</p>
<dt><code>listlinks </code>(+)</p>
<dd> If set, the <i>ls-F</i> builtin command shows the type of file to which each symbolic link points.</p>
<dt><code>listmax </code>(+)</p>
<dd> The maximum number of items which the <i>list-choices</i> editor command will list without asking first.</p>
<dt><code>listmaxrows </code>(+)</p>
<dd> The maximum number of rows of items which the <i>list-choices</i> editor command will list without asking first.</p>
<dt><code>loginsh </code>(+)</p>
<dd> Set by the shell if it is a login shell. Setting or unsetting it within a shell has no effect. See also <code>shlvl</code>.</p>
<dt><code>logout </code>(+)</p>
<dd> Set by the shell to `normal&#8217; before a normal logout, `automatic&#8217; before an automatic logout, and `hangup&#8217; if the shell was killed by a hangup signal (see <code>Signal handling</code>). See also the <code>autologout</code> shell variable.</p>
<dt><code>mail</code></p>
<dd> A list of files and directories to check for incoming mail, optionally preceded by a numeric word. Before each prompt, if 10 minutes have passed since the last check, the shell checks each file and says `You have new mail.&#8217; (or, if <code>mail</code> contains multiple files, `You have new mail in <i>name</i>.&#8217;) if the filesize is greater than zero in size and has a modification time greater than its access time.</dl>
<dl>
<dt>
<dd>
<p> If you are in a login shell, then no mail file is reported unless it has been modified after the time the shell has started up, to prevent redundant notifications. Most login programs will tell you whether or not you have mail when you log in. </p>
<p> If a file specified in <code>mail</code> is a directory, the shell will count each file within that directory as a separate message, and will report `You have <i>n</i> mails.&#8217; or `You have <i>n</i> mails in <i>name</i>.&#8217; as appropriate. This functionality is provided primarily for those systems which store mail in this manner, such as the Andrew Mail System. </p>
<p> If the first word of <code>mail</code> is numeric it is taken as a different mail checking interval, in seconds. </p>
<p> Under very rare circumstances, the shell may report `You have mail.&#8217; instead of `You have new mail.&#8217;</dl>
<dl>
<dt><code>matchbeep </code>(+)</p>
<dd> If set to `never&#8217;, completion never beeps. If set to `nomatch&#8217;, it beeps only when there is no match. If set to `ambiguous&#8217;, it beeps when there are multiple matches. If set to `notunique&#8217;, it beeps when there is one exact and other longer matches. If unset, `ambiguous&#8217; is used.</p>
<dt><code>nobeep </code>(+)</p>
<dd> If set, beeping is completely disabled. See also <code>visiblebell</code>.</p>
<dt><code>noclobber</code></p>
<dd> If set, restrictions are placed on output redirection to insure that files are not accidentally destroyed and that `&gt;&gt;&#8217; redirections refer to existing files, as described in the <code>Input/output</code> section.</p>
<dt><code>noding</code></p>
<dd> If set, disable the printing of `DING!&#8217; in the <code>prompt</code> time specifiers at the change of hour.</p>
<dt><code>noglob</code></p>
<dd> If set, <code>Filename substitution</code> and <code>Directory stack substitution</code> (q.v.) are inhibited. This is most useful in shell scripts which do not deal with filenames, or after a list of filenames has been obtained and further expansions are not desirable.</p>
<dt><code>nokanji </code>(+)</p>
<dd> If set and the shell supports Kanji (see the <code>version</code> shell variable), it is disabled so that the meta key can be used.</p>
<dt><code>nonomatch</code></p>
<dd> If set, a <code>Filename substitution</code> or <code>Directory stack substitution</code> (q.v.) which does not match any existing files is left untouched rather than causing an error. It is still an error for the substitution to be malformed, e.g., `echo [&#8216; still gives an error.</p>
<dt><code>nostat </code>(+)</p>
<dd> A list of directories (or glob-patterns which match directories; see <code>Filename substitution</code>) that should not be <i><a href="/docs/linux/man/2-stat/">stat</a></i>(2)ed during a completion operation. This is usually used to exclude directories which take too much time to <i><a href="/docs/linux/man/2-stat/">stat</a></i>(2), for example <i>/afs</i>.</p>
<dt><code>notify</code></p>
<dd> If set, the shell announces job completions asynchronously. The default is to present job completions just before printing a prompt.</p>
<dt><code>oid </code>(+)</p>
<dd> The user&#8217;s real organization ID. (Domain/OS only)</p>
<dt><code>owd </code>(+)</p>
<dd> The old working directory, equivalent to the `-&#8216; used by <i>cd</i> and <i>pushd</i>. See also the <code>cwd</code> and <code>dirstack</code> shell variables.</p>
<dt><code>padhour</code></p>
<dd> If set, enable the printing of padding &#8216;0&#8217; for hours, in 24 and 12 hour formats. E.G.: 07:45:42 vs. 7:45:42.</p>
<dt><code>parseoctal</code></p>
<dd> To retain compatibily with older versions numeric variables starting with 0 are not interpreted as octal. Setting this variable enables proper octal parsing.</p>
<dt><code>path</code></p>
<dd> A list of directories in which to look for executable commands. A null word specifies the current directory. If there is no <code>path</code> variable then only full path names will execute. <code>path</code> is set by the shell at startup from the <code>PATH</code> environment variable or, if <code>PATH</code> does not exist, to a system-dependent default something like `(/usr/local/bin /usr/bsd /bin /usr/bin .)&#8217;. The shell may put `.&#8217; first or last in <code>path</code> or omit it entirely depending on how it was compiled; see the <code>version</code> shell variable. A shell which is given neither the <code>-c</code> nor the <code>-t</code> option hashes the contents of the directories in <code>path</code> after reading <i>~/.tcshrc</i> and each time <code>path</code> is reset. If one adds a new command to a directory in <code>path</code> while the shell is active, one may need to do a <i>rehash</i> for the shell to find it.</p>
<dt><code>printexitvalue </code>(+)</p>
<dd> If set and an interactive program exits with a non-zero status, the shell prints `Exit <code>status</code>&#8216;.</p>
<dt><code>prompt</code></p>
<dd> The string which is printed before reading each command from the terminal. <code>prompt</code> may include any of the following formatting sequences (+), which are replaced by the given information:</dl>
<dl>
<dt>
<dd>
<dl>
<dt>%/</p>
<dd> The current working directory.</p>
<dt>%~</p>
<dd> The current working directory, but with one&#8217;s home directory represented by `~&#8217; and other users&#8217; home directories represented by `~user&#8217; as per <code>Filename substitution</code>. `~user&#8217; substitution happens only if the shell has already used `~<i>user</i>&#8216; in a pathname in the current session.</p>
<dt>%c[[0]<i>n</i>], %.[[0]<i>n</i>]</p>
<dd> The trailing component of the current working directory, or <i>n</i> trailing components if a digit <i>n</i> is given. If <i>n</i> begins with `0&#8242;, the number of skipped components precede the trailing component(s) in the format `/&lt;<i>skipped</i>&gt;trailing&#8217;. If the <code>ellipsis</code> shell variable is set, skipped components are represented by an ellipsis so the whole becomes `&#8230;trailing&#8217;. `~&#8217; substitution is done as in `%~&#8217; above, but the `~&#8217; component is ignored when counting trailing components.</p>
<dt>%C</p>
<dd> Like %c, but without `~&#8217; substitution.</p>
<dt>%h, %!, !</p>
<dd> The current history event number.</p>
<dt>%M</p>
<dd> The full hostname.</p>
<dt>%m</p>
<dd> The hostname up to the first `.&#8217;.</p>
<dt>%S (%s)</p>
<dd> Start (stop) standout mode.</p>
<dt>%B (%b)</p>
<dd> Start (stop) boldfacing mode.</p>
<dt>%U (%u)</p>
<dd> Start (stop) underline mode.</p>
<dt>%t, %@</p>
<dd> The time of day in 12-hour AM/PM format.</p>
<dt>%T</p>
<dd> Like `%t&#8217;, but in 24-hour format (but see the <code>ampm</code> shell variable).</p>
<dt>%p</p>
<dd> The `precise&#8217; time of day in 12-hour AM/PM format, with seconds.</p>
<dt>%P</p>
<dd> Like `%p&#8217;, but in 24-hour format (but see the <code>ampm</code> shell variable).</p>
<dt>\<i>c</i></p>
<dd> <i>c</i> is parsed as in <i>bindkey</i>.</p>
<dt>^<i>c</i></p>
<dd> <i>c</i> is parsed as in <i>bindkey</i>.</p>
<dt>%%</p>
<dd> A single `%&#8217;.</p>
<dt>%n</p>
<dd> The user name.</p>
<dt>%N</p>
<dd> The effective user name.</p>
<dt>%j</p>
<dd> The number of jobs.</p>
<dt>%d</p>
<dd> The weekday in `Day&#8217; format.</p>
<dt>%D</p>
<dd> The day in `dd&#8217; format.</p>
<dt>%w</p>
<dd> The month in `Mon&#8217; format.</p>
<dt>%W</p>
<dd> The month in `mm&#8217; format.</p>
<dt>%y</p>
<dd> The year in `yy&#8217; format.</p>
<dt>%Y</p>
<dd> The year in `yyyy&#8217; format.</p>
<dt>%l</p>
<dd> The shell&#8217;s tty.</p>
<dt>%L</p>
<dd> Clears from the end of the prompt to end of the display or the end of the line.</p>
<dt>%$</p>
<dd> Expands the shell or environment variable name immediately after the `$&#8217;.</p>
<dt>%#</p>
<dd> `&gt;&#8217; (or the first character of the <code>promptchars</code> shell variable) for normal users, `#&#8217; (or the second character of <code>promptchars</code>) for the superuser.</p>
<dt>%{<i>string</i>%}</p>
<dd> Includes <i>string</i> as a literal escape sequence. It should be used only to change terminal attributes and should not move the cursor location. This cannot be the last sequence in <code>prompt</code>.</p>
<dt>%?</p>
<dd> The return code of the command executed just before the prompt.</p>
<dt>%R</p>
<dd> In <code>prompt2</code>, the status of the parser. In <code>prompt3</code>, the corrected string. In <code>history</code>, the history string.</dl>
<p> `%B&#8217;, `%S&#8217;, `%U&#8217; and `%{<i>string</i>%}&#8217; are available in only eight-bit-clean shells; see the <code>version</code> shell variable. </p>
<p> The bold, standout and underline sequences are often used to distinguish a superuser shell. For example,</p>
<dl>
<dt>
<dd> &gt; set prompt = &quot;%m [%h] %B[%@]%b [%/] you rang? &quot;<br />
 tut [37] <code>[2:54pm]</code> [/usr/accts/sys] you rang? _</dl>
<p> If `%t&#8217;, `%@&#8217;, `%T&#8217;, `%p&#8217;, or `%P&#8217; is used, and <code>noding</code> is not set, then print `DING!&#8217; on the change of hour (i.e, `:00&#8242; minutes) instead of the actual time. </p>
<p> Set by default to `%# &#8216; in interactive shells.</dl>
<dl>
<dt><code>prompt2 </code>(+)</p>
<dd> The string with which to prompt in <i>while</i> and <i>foreach</i> loops and after lines ending in `\&#8217;. The same format sequences may be used as in <code>prompt</code> (q.v.); note the variable meaning of `%R&#8217;. Set by default to `%R? &#8216; in interactive shells.</p>
<dt><code>prompt3 </code>(+)</p>
<dd> The string with which to prompt when confirming automatic spelling correction. The same format sequences may be used as in <code>prompt</code> (q.v.); note the variable meaning of `%R&#8217;. Set by default to `CORRECT&gt;%R (y|n|e|a)? &#8216; in interactive shells.</p>
<dt><code>promptchars </code>(+)</p>
<dd> If set (to a two-character string), the `%#&#8217; formatting sequence in the <code>prompt</code> shell variable is replaced with the first character for normal users and the second character for the superuser.</p>
<dt><code>pushdtohome </code>(+)</p>
<dd> If set, <i>pushd</i> without arguments does `pushd ~&#8217;, like <i>cd</i>.</p>
<dt><code>pushdsilent </code>(+)</p>
<dd> If set, <i>pushd</i> and <i>popd</i> do not print the directory stack.</p>
<dt><code>recexact </code>(+)</p>
<dd> If set, completion completes on an exact match even if a longer match is possible.</p>
<dt><code>recognize_only_executables </code>(+)</p>
<dd> If set, command listing displays only files in the path that are executable. Slow.</p>
<dt><code>rmstar </code>(+)</p>
<dd> If set, the user is prompted before `rm *&#8217; is executed.</p>
<dt><code>rprompt </code>(+)</p>
<dd> The string to print on the right-hand side of the screen (after the command input) when the prompt is being displayed on the left. It recognizes the same formatting characters as <code>prompt</code>. It will automatically disappear and reappear as necessary, to ensure that command input isn&#8217;t obscured, and will appear only if the prompt, command input, and itself will fit together on the first line. If <code>edit</code> isn&#8217;t set, then <code>rprompt</code> will be printed after the prompt and before the command input.</p>
<dt><code>savedirs </code>(+)</p>
<dd> If set, the shell does `dirs -S&#8217; before exiting. If the first word is set to a number, at most that many directory stack entries are saved.</p>
<dt><code>savehist</code></p>
<dd> If set, the shell does `history -S&#8217; before exiting. If the first word is set to a number, at most that many lines are saved. (The number must be less than or equal to <code>history</code>.) If the second word is set to `merge&#8217;, the history list is merged with the existing history file instead of replacing it (if there is one) and sorted by time stamp and the most recent events are retained. (+)</p>
<dt><code>sched </code>(+)</p>
<dd> The format in which the <i>sched</i> builtin command prints scheduled events; if not given, `%h	%T	%R
&#8217; is used. The format sequences are described above under <code>prompt</code>; note the variable meaning of `%R&#8217;.</p>
<dt><code>shell</code></p>
<dd> The file in which the shell resides. This is used in forking shells to interpret files which have execute bits set, but which are not executable by the system. (See the description of <code>Builtin and non-builtin command execution</code>.) Initialized to the (system-dependent) home of the shell.</p>
<dt><code>shlvl </code>(+)</p>
<dd> The number of nested shells. Reset to 1 in login shells. See also <code>loginsh</code>.</p>
<dt><code>status</code></p>
<dd> The exit status from the last command or backquote expansion, or any command in a pipeline is propagated to <code>status</code>. (This is also the default <code>csh</code> behavior.) This default does not match what POSIX mandates (to return the status of the last command only). To match the POSIX behavior, you need to unset <code>anyerror</code>.</p>
<dl>
<dt>
<dd>
<p> If the <code>anyerror</code> variable is unset, the exit status of a pipeline is determined only from the last command in the pipeline, and the exit status of a backquote expansion is <i>not</i> propagated to <code>status</code>. </p>
<p> If a command terminated abnormally, then 0200 is added to the status. Builtin commands which fail return exit status `1&#8242;, all other builtin commands return status `0&#8242;.</dl>
<dt><code>symlinks </code>(+)</p>
<dd> Can be set to several different values to control symbolic link (`symlink&#8217;) resolution:</p>
<dl>
<dt>
<dd>
<p> If set to `chase&#8217;, whenever the current directory changes to a directory containing a symbolic link, it is expanded to the real name of the directory to which the link points. This does not work for the user&#8217;s home directory; this is a bug. </p>
<p> If set to `ignore&#8217;, the shell tries to construct a current directory relative to the current directory before the link was crossed. This means that <i>cd</i>ing through a symbolic link and then `cd ..&#8217;ing returns one to the original directory. This affects only builtin commands and filename completion. </p>
<p> If set to `expand&#8217;, the shell tries to fix symbolic links by actually expanding arguments which look like path names. This affects any command, not just builtins. Unfortunately, this does not work for hard-to-recognize filenames, such as those embedded in command options. Expansion may be prevented by quoting. While this setting is usually the most convenient, it is sometimes misleading and sometimes confusing when it fails to recognize an argument which should be expanded. A compromise is to use `ignore&#8217; and use the editor command <i>normalize-path</i> (bound by default to ^X-n) when necessary. </p>
<p> Some examples are in order. First, let&#8217;s set up some play directories:</p>
<dl>
<dt>
<dd> &gt; cd /tmp<br />
 &gt; mkdir from from/src to<br />
 &gt; ln -s from/src to/dst</dl>
<p> Here&#8217;s the behavior with <code>symlinks</code> unset,</p>
<dl>
<dt>
<dd> &gt; cd /tmp/to/dst; echo $cwd<br />
 /tmp/to/dst<br />
 &gt; cd ..; echo $cwd<br />
 /tmp/from</dl>
<p> here&#8217;s the behavior with <code>symlinks</code> set to `chase&#8217;,</p>
<dl>
<dt>
<dd> &gt; cd /tmp/to/dst; echo $cwd<br />
 /tmp/from/src<br />
 &gt; cd ..; echo $cwd<br />
 /tmp/from</dl>
<p> here&#8217;s the behavior with <code>symlinks</code> set to `ignore&#8217;,</p>
<dl>
<dt>
<dd> &gt; cd /tmp/to/dst; echo $cwd<br />
 /tmp/to/dst<br />
 &gt; cd ..; echo $cwd<br />
 /tmp/to</dl>
<p> and here&#8217;s the behavior with <code>symlinks</code> set to `expand&#8217;.</p>
<dl>
<dt>
<dd> &gt; cd /tmp/to/dst; echo $cwd<br />
 /tmp/to/dst<br />
 &gt; cd ..; echo $cwd<br />
 /tmp/to<br />
 &gt; cd /tmp/to/dst; echo $cwd<br />
 /tmp/to/dst<br />
 &gt; cd &quot;..&quot;; echo $cwd<br />
 /tmp/from<br />
 &gt; /bin/echo ..<br />
 /tmp/to<br />
 &gt; /bin/echo &quot;..&quot;<br />
 ..</dl>
<p> Note that `expand&#8217; expansion 1) works just like `ignore&#8217; for builtins like <i>cd</i>, 2) is prevented by quoting, and 3) happens before filenames are passed to non-builtin commands.</dl>
<dt><code>tcsh </code>(+)</p>
<dd> The version number of the shell in the format `R.VV.PP&#8217;, where `R&#8217; is the major release number, `VV&#8217; the current version and `PP&#8217; the patchlevel.</p>
<dt><code>term</code></p>
<dd> The terminal type. Usually set in <i>~/.login</i> as described under <code>Startup and shutdown</code>.</p>
<dt><code>time</code></p>
<dd> If set to a number, then the <i>time</i> builtin (q.v.) executes automatically after each command which takes more than that many CPU seconds. If there is a second word, it is used as a format string for the output of the <i>time</i> builtin. (u) The following sequences may be used in the format string:</dl>
<dl>
<dt>
<dd>
<dl>
<dt>%U</p>
<dd> The time the process spent in user mode in cpu seconds.</p>
<dt>%S</p>
<dd> The time the process spent in kernel mode in cpu seconds.</p>
<dt>%E</p>
<dd> The elapsed (wall clock) time in seconds.</p>
<dt>%P</p>
<dd> The CPU percentage computed as (%U + %S) / %E.</p>
<dt>%W</p>
<dd> Number of times the process was swapped.</p>
<dt>%X</p>
<dd> The average amount in (shared) text space used in Kbytes.</p>
<dt>%D</p>
<dd> The average amount in (unshared) data/stack space used in Kbytes.</p>
<dt>%K</p>
<dd> The total space used (%X + %D) in Kbytes.</p>
<dt>%M</p>
<dd> The maximum memory the process had in use at any time in Kbytes.</p>
<dt>%F</p>
<dd> The number of major page faults (page needed to be brought from disk).</p>
<dt>%R</p>
<dd> The number of minor page faults.</p>
<dt>%I</p>
<dd> The number of input operations.</p>
<dt>%O</p>
<dd> The number of output operations.</p>
<dt>%r</p>
<dd> The number of socket messages received.</p>
<dt>%s</p>
<dd> The number of socket messages sent.</p>
<dt>%k</p>
<dd> The number of signals received.</p>
<dt>%w</p>
<dd> The number of voluntary context switches (waits).</p>
<dt>%c</p>
<dd> The number of involuntary context switches.</dl>
<p> Only the first four sequences are supported on systems without BSD resource limit functions. The default time format is `%Uu %Ss %E %P %X+%Dk %I+%Oio %Fpf+%Ww&#8217; for systems that support resource usage reporting and `%Uu %Ss %E %P&#8217; for systems that do not. </p>
<p> Under Sequent&#8217;s DYNIX/ptx, %X, %D, %K, %r and %s are not available, but the following additional sequences are: </p>
<dl>
<dt>%Y</p>
<dd> The number of system calls performed.</p>
<dt>%Z</p>
<dd> The number of pages which are zero-filled on demand.</p>
<dt>%i</p>
<dd> The number of times a process&#8217;s resident set size was increased by the kernel.</p>
<dt>%d</p>
<dd> The number of times a process&#8217;s resident set size was decreased by the kernel.</p>
<dt>%l</p>
<dd> The number of read system calls performed.</p>
<dt>%m</p>
<dd> The number of write system calls performed.</p>
<dt>%p</p>
<dd> The number of reads from raw disk devices.</p>
<dt>%q</p>
<dd> The number of writes to raw disk devices.</dl>
<p> and the default time format is `%Uu %Ss %E %P %I+%Oio %Fpf+%Ww&#8217;. Note that the CPU percentage can be higher than 100% on multi-processors.</dl>
<dl>
<dt><code>tperiod </code>(+)</p>
<dd> The period, in minutes, between executions of the <i>periodic</i> special alias.</p>
<dt><code>tty </code>(+)</p>
<dd> The name of the tty, or empty if not attached to one.</p>
<dt><code>uid </code>(+)</p>
<dd> The user&#8217;s real user ID.</p>
<dt><code>user</code></p>
<dd> The user&#8217;s login name.</p>
<dt><code>verbose</code></p>
<dd> If set, causes the words of each command to be printed, after history substitution (if any). Set by the <code>-v</code> command line option.</p>
<dt><code>version </code>(+)</p>
<dd> The version ID stamp. It contains the shell&#8217;s version number (see <code>tcsh</code>), origin, release date, vendor, operating system and machine (see <code>VENDOR</code>, <code>OSTYPE</code> and <code>MACHTYPE</code>) and a comma-separated list of options which were set at compile time. Options which are set by default in the distribution are noted.</dl>
<dl>
<dt>
<dd>
<dl>
<dt>8b</p>
<dd> The shell is eight bit clean; default</p>
<dt>7b</p>
<dd> The shell is not eight bit clean</p>
<dt>wide</p>
<dd> The shell is multibyte encoding clean (like UTF-8)</p>
<dt>nls</p>
<dd> The system&#8217;s NLS is used; default for systems with NLS</p>
<dt>lf</p>
<dd> Login shells execute <i>/etc/csh.login</i> before instead of after <i>/etc/csh.cshrc</i> and <i>~/.login</i> before instead of after <i>~/.tcshrc</i> and <i>~/.history</i>.</p>
<dt>dl</p>
<dd> `.&#8217; is put last in <code>path</code> for security; default</p>
<dt>nd</p>
<dd> `.&#8217; is omitted from <code>path</code> for security</p>
<dt>vi</p>
<dd> <i>vi</i>-style editing is the default rather than <i>emacs</i></p>
<dt>dtr</p>
<dd> Login shells drop DTR when exiting</p>
<dt>bye</p>
<dd> <i>bye</i> is a synonym for <i>logout</i> and <i>log</i> is an alternate name for <i>watchlog</i></p>
<dt>al</p>
<dd> <code>autologout</code> is enabled; default</p>
<dt>kan</p>
<dd> Kanji is used if appropriate according to locale settings, unless the <code>nokanji</code> shell variable is set</p>
<dt>sm</p>
<dd> The system&#8217;s <i><a href="/docs/linux/man/3-malloc/">malloc</a></i>(3) is used</p>
<dt>hb</p>
<dd> The `#!&lt;program&gt; &lt;args&gt;&#8217; convention is emulated when executing shell scripts</p>
<dt>ng</p>
<dd> The <i>newgrp</i> builtin is available</p>
<dt>rh</p>
<dd> The shell attempts to set the <code>REMOTEHOST</code> environment variable</p>
<dt>afs</p>
<dd> The shell verifies your password with the kerberos server if local authentication fails. The <code>afsuser</code> shell variable or the <code>AFSUSER</code> environment variable override your local username if set.</dl>
<p> An administrator may enter additional strings to indicate differences in the local version.</dl>
<dl>
<dt><code>visiblebell </code>(+)</p>
<dd> If set, a screen flash is used rather than the audible bell. See also <code>nobeep</code>.</p>
<dt><code>watch </code>(+)</p>
<dd> A list of user/terminal pairs to watch for logins and logouts. If either the user is `any&#8217; all terminals are watched for the given user and vice versa. Setting <code>watch</code> to `(any any)&#8217; watches all users and terminals. For example,</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> set watch = (george ttyd1 any console $user any)</dl>
<p> reports activity of the user `george&#8217; on ttyd1, any user on the console, and oneself (or a trespasser) on any terminal. </p>
<p> Logins and logouts are checked every 10 minutes by default, but the first word of <code>watch</code> can be set to a number to check every so many minutes. For example,</p>
<dl>
<dt>
<dd> set watch = (1 any any)</dl>
<p> reports any login/logout once every minute. For the impatient, the <i>log</i> builtin command triggers a <code>watch</code> report at any time. All current logins are reported (as with the <i>log</i> builtin) when <code>watch</code> is first set. </p>
<p> The <code>who</code> shell variable controls the format of <code>watch</code> reports.</dl>
<dt><code>who </code>(+)</p>
<dd> The format string for <code>watch</code> messages. The following sequences are replaced by the given information:</dl>
<dl>
<dt>
<dd>
<dl>
<dt>%n</p>
<dd> The name of the user who logged in/out.</p>
<dt>%a</p>
<dd> The observed action, i.e., `logged on&#8217;, `logged off&#8217; or `replaced <i>olduser</i> on&#8217;.</p>
<dt>%l</p>
<dd> The terminal (tty) on which the user logged in/out.</p>
<dt>%M</p>
<dd> The full hostname of the remote host, or `local&#8217; if the login/logout was from the local host.</p>
<dt>%m</p>
<dd> The hostname of the remote host up to the first `.&#8217;. The full name is printed if it is an IP address or an X Window System display.</dl>
<p> %M and %m are available on only systems that store the remote hostname in <i>/etc/utmp</i>. If unset, `%n has %a %l from %m.&#8217; is used, or `%n has %a %l.&#8217; on systems which don&#8217;t store the remote hostname.</dl>
<dl>
<dt><code>wordchars </code>(+)</p>
<dd> A list of non-alphanumeric characters to be considered part of a word by the <i>forward-word</i>, <i>backward-word</i> etc., editor commands. If unset, `*?_-.[]~=&#8217; is used.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>AFSUSER </code>(+)</p>
<dd> Equivalent to the <code>afsuser</code> shell variable.</p>
<dt><code>COLUMNS</code></p>
<dd> The number of columns in the terminal. See <code>Terminal management</code>.</p>
<dt><code>DISPLAY</code></p>
<dd> Used by X Window System (see <i><a href="/docs/linux/man/1-x/">X</a></i>(1)). If set, the shell does not set <code>autologout</code> (q.v.).</p>
<dt><code>EDITOR</code></p>
<dd> The pathname to a default editor. See also the <code>VISUAL</code> environment variable and the <i>run-fg-editor</i> editor command.</p>
<dt><code>GROUP </code>(+)</p>
<dd> Equivalent to the <code>group</code> shell variable.</p>
<dt><code>HOME</code></p>
<dd> Equivalent to the <code>home</code> shell variable.</p>
<dt><code>HOST </code>(+)</p>
<dd> Initialized to the name of the machine on which the shell is running, as determined by the <i><a href="/docs/linux/man/2-gethostname/">gethostname</a></i>(2) system call.</p>
<dt><code>HOSTTYPE </code>(+)</p>
<dd> Initialized to the type of machine on which the shell is running, as determined at compile time. This variable is obsolete and will be removed in a future version.</p>
<dt><code>HPATH </code>(+)</p>
<dd> A colon-separated list of directories in which the <i>run-help</i> editor command looks for command documentation.</p>
<dt><code>LANG</code></p>
<dd> Gives the preferred character environment. See <code>Native Language System support</code>.</p>
<dt><code>LC_CTYPE</code></p>
<dd> If set, only ctype character handling is changed. See <code>Native Language System support</code>.</p>
<dt><code>LINES</code></p>
<dd> The number of lines in the terminal. See <code>Terminal management</code>.</p>
<dt><code>LS_COLORS</code></p>
<dd> The format of this variable is reminiscent of the <code><a href="/docs/linux/man/5-termcap/">termcap</a>(5)</code> file format; a colon-separated list of expressions of the form &quot;<i>xx=string</i>&quot;, where &quot;<i>xx</i>&quot; is a two-character variable name. The variables with their associated defaults are:</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>no<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0</p>
<dd> Normal (non-filename) text</p>
<dt>fi<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0</p>
<dd> Regular file</p>
<dt>di<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>01;34</p>
<dd> Directory</p>
<dt>ln<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>01;36</p>
<dd> Symbolic link</p>
<dt>pi<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>33</p>
<dd> Named pipe (FIFO)</p>
<dt>so<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>01;35</p>
<dd> Socket</p>
<dt>do<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>01;35</p>
<dd> Door</p>
<dt>bd<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>01;33</p>
<dd> Block device</p>
<dt>cd<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>01;32</p>
<dd> Character device</p>
<dt>ex<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>01;32</p>
<dd> Executable file</p>
<dt>mi<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>(none)</p>
<dd> Missing file (defaults to fi)</p>
<dt>or<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>(none)</p>
<dd> Orphaned symbolic link (defaults to ln)</p>
<dt>lc<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>^[[</p>
<dd> Left code</p>
<dt>rc<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>m</p>
<dd> Right code</p>
<dt>ec<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>(none)</p>
<dd> End code (replaces lc+no+rc)
</dl>
</dl>
<p> You need to include only the variables you want to change from the default. </p>
<p> File names can also be colorized based on filename extension. This is specified in the <code>LS_COLORS</code> variable using the syntax <code>&quot;*ext=string&quot;</code>. For example, using ISO 6429 codes, to color all C-language source files blue you would specify <code>&quot;*.c=34&quot;</code>. This would color all files ending in <code>.c</code> in blue (34) color. </p>
<p> Control characters can be written either in C-style-escaped notation, or in stty-like ^-notation. The C-style notation adds <code>^[</code> for Escape, <code>_</code> for a normal space character, and <code>?</code> for Delete. In addition, the <code>^[</code> escape character can be used to override the default interpretation of <code>^[</code>, <code>^</code>, <code>:</code> and <code>=</code>. </p>
<p> Each file will be written as <code>&lt;lc&gt;</code> <code>&lt;color-code&gt;</code> <code>&lt;rc&gt;</code> <code>&lt;filename&gt;</code> <code>&lt;ec&gt;</code>. If the <code>&lt;ec&gt;</code> code is undefined, the sequence <code>&lt;lc&gt;</code> <code>&lt;no&gt; &lt;rc&gt;</code> will be used instead. This is generally more convenient to use, but less general. The left, right and end codes are provided so you don&#8217;t have to type common parts over and over again and to support weird terminals; you will generally not need to change them at all unless your terminal does not use ISO 6429 color sequences but a different system. </p>
<p> If your terminal does use ISO 6429 color codes, you can compose the type codes (i.e., all except the <code>lc</code>, <code>rc</code>, and <code>ec</code> codes) from numerical commands separated by semicolons. The most common commands are: </p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> to restore default color</p>
<dt>1</p>
<dd> for brighter colors</p>
<dt>4</p>
<dd> for underlined text</p>
<dt>5</p>
<dd> for flashing text</p>
<dt>30</p>
<dd> for black foreground</p>
<dt>31</p>
<dd> for red foreground</p>
<dt>32</p>
<dd> for green foreground</p>
<dt>33</p>
<dd> for yellow (or brown) foreground</p>
<dt>34</p>
<dd> for blue foreground</p>
<dt>35</p>
<dd> for purple foreground</p>
<dt>36</p>
<dd> for cyan foreground</p>
<dt>37</p>
<dd> for white (or gray) foreground</p>
<dt>40</p>
<dd> for black background</p>
<dt>41</p>
<dd> for red background</p>
<dt>42</p>
<dd> for green background</p>
<dt>43</p>
<dd> for yellow (or brown) background</p>
<dt>44</p>
<dd> for blue background</p>
<dt>45</p>
<dd> for purple background</p>
<dt>46</p>
<dd> for cyan background</p>
<dt>47</p>
<dd> for white (or gray) background</dl>
</dl>
<p> Not all commands will work on all systems or display devices. </p>
<p> A few terminal programs do not recognize the default end code properly. If all text gets colorized after you do a directory listing, try changing the <code>no</code> and <code>fi</code> codes from 0 to the numerical codes for your standard fore- and background colors.</dl>
<dl>
<dt><code>MACHTYPE </code>(+)</p>
<dd> The machine type (microprocessor class or machine model), as determined at compile time.</p>
<dt><code>NOREBIND </code>(+)</p>
<dd> If set, printable characters are not rebound to <i>self-insert-command</i>. See <code>Native Language System support</code>.</p>
<dt><code>OSTYPE </code>(+)</p>
<dd> The operating system, as determined at compile time.</p>
<dt><code>PATH</code></p>
<dd> A colon-separated list of directories in which to look for executables. Equivalent to the <code>path</code> shell variable, but in a different format.</p>
<dt><code>PWD </code>(+)</p>
<dd> Equivalent to the <code>cwd</code> shell variable, but not synchronized to it; updated only after an actual directory change.</p>
<dt><code>REMOTEHOST </code>(+)</p>
<dd> The host from which the user has logged in remotely, if this is the case and the shell is able to determine it. Set only if the shell was so compiled; see the <code>version</code> shell variable.</p>
<dt><code>SHLVL </code>(+)</p>
<dd> Equivalent to the <code>shlvl</code> shell variable.</p>
<dt><code>SYSTYPE </code>(+)</p>
<dd> The current system type. (Domain/OS only)</p>
<dt><code>TERM</code></p>
<dd> Equivalent to the <code>term</code> shell variable.</p>
<dt><code>TERMCAP</code></p>
<dd> The terminal capability string. See <code>Terminal management</code>.</p>
<dt><code>USER</code></p>
<dd> Equivalent to the <code>user</code> shell variable.</p>
<dt><code>VENDOR </code>(+)</p>
<dd> The vendor, as determined at compile time.</p>
<dt><code>VISUAL</code></p>
<dd> The pathname to a default full-screen editor. See also the <code>EDITOR</code> environment variable and the <i>run-fg-editor</i> editor command.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/csh.cshrc</i></p>
<dd> Read first by every shell. ConvexOS, Stellix and Intel use <i>/etc/cshrc</i> and NeXTs use <i>/etc/cshrc.std</i>. A/UX, AMIX, Cray and IRIX have no equivalent in <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1), but read this file in <i>tcsh</i> anyway. Solaris 2.x does not have it either, but <i>tcsh</i> reads <i>/etc/.cshrc</i>. (+)</p>
<dt><i>/etc/csh.login</i></p>
<dd> Read by login shells after <i>/etc/csh.cshrc</i>. ConvexOS, Stellix and Intel use <i>/etc/login</i>, NeXTs use <i>/etc/login.std</i>, Solaris 2.x uses <i>/etc/.login</i> and A/UX, AMIX, Cray and IRIX use <i>/etc/cshrc</i>.</p>
<dt><i>~/.tcshrc </i>(+)</p>
<dd> Read by every shell after <i>/etc/csh.cshrc</i> or its equivalent.</p>
<dt><i>~/.cshrc</i></p>
<dd> Read by every shell, if <i>~/.tcshrc</i> doesn&#8217;t exist, after <i>/etc/csh.cshrc</i> or its equivalent. This manual uses `<i>~/.tcshrc</i>&#8216; to mean `<i>~/.tcshrc</i> or, if <i>~/.tcshrc</i> is not found, <i>~/.cshrc</i>&#8216;.</p>
<dt><i>~/.history</i></p>
<dd> Read by login shells after <i>~/.tcshrc</i> if <code>savehist</code> is set, but see also <code>histfile</code>.</p>
<dt><i>~/.login</i></p>
<dd> Read by login shells after <i>~/.tcshrc</i> or <i>~/.history</i>. The shell may be compiled to read <i>~/.login</i> before instead of after <i>~/.tcshrc</i> and <i>~/.history</i>; see the <code>version</code> shell variable.</p>
<dt><i>~/.cshdirs </i>(+)</p>
<dd> Read by login shells after <i>~/.login</i> if <code>savedirs</code> is set, but see also <code>dirsfile</code>.</p>
<dt><i>/etc/csh.logout</i></p>
<dd> Read by login shells at logout. ConvexOS, Stellix and Intel use <i>/etc/logout</i> and NeXTs use <i>/etc/logout.std</i>. A/UX, AMIX, Cray and IRIX have no equivalent in <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1), but read this file in <i>tcsh</i> anyway. Solaris 2.x does not have it either, but <i>tcsh</i> reads <i>/etc/.logout</i>. (+)</p>
<dt><i>~/.logout</i></p>
<dd> Read by login shells at logout after <i>/etc/csh.logout</i> or its equivalent.</p>
<dt><i>/bin/sh</i></p>
<dd> Used to interpret shell scripts not starting with a `#&#8217;.</p>
<dt><i>/tmp/sh*</i></p>
<dd> Temporary file for `&lt;&lt;&#8216;.</p>
<dt><i>/etc/passwd</i></p>
<dd> Source of home directories for `~name&#8217; substitutions.</dl>
<p> The order in which startup files are read may differ if the shell was so compiled; see <code>Startup and shutdown</code> and the <code>version</code> shell variable.</p>
<h2>NEW FEATURES (+)</h2>
<p> This manual describes <i>tcsh</i> as a single entity, but experienced <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1) users will want to pay special attention to <i>tcsh</i>&#8216;s new features. </p>
<p> A command-line editor, which supports GNU Emacs or <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1)-style key bindings. See <code>The command-line editor</code> and <code>Editor commands</code>. </p>
<p> Programmable, interactive word completion and listing. See <code>Completion and listing</code> and the <i>complete</i> and <i>uncomplete</i> builtin commands. </p>
<p> <code>Spelling correction</code> (q.v.) of filenames, commands and variables. </p>
<p> <code>Editor commands</code> (q.v.) which perform other useful functions in the middle of typed commands, including documentation lookup (<i>run-help</i>), quick editor restarting (<i>run-fg-editor</i>) and command resolution (<i>which-command</i>). </p>
<p> An enhanced history mechanism. Events in the history list are time-stamped. See also the <i>history</i> command and its associated shell variables, the previously undocumented `#&#8217; event specifier and new modifiers under <code>History substitution</code>, the <i>*-history</i>, <i>history-search-*</i>, <i>i-search-*</i>, <i>vi-search-*</i> and <i>toggle-literal-history</i> editor commands and the <code>histlit</code> shell variable. </p>
<p> Enhanced directory parsing and directory stack handling. See the <i>cd</i>, <i>pushd</i>, <i>popd</i> and <i>dirs</i> commands and their associated shell variables, the description of <code>Directory stack substitution</code>, the <code>dirstack</code>, <code>owd</code> and <code>symlinks</code> shell variables and the <i>normalize-command</i> and <i>normalize-path</i> editor commands. </p>
<p> Negation in glob-patterns. See <code>Filename substitution</code>. </p>
<p> New <code>File inquiry operators</code> (q.v.) and a <i>filetest</i> builtin which uses them. </p>
<p> A variety of <code>Automatic, periodic and timed events</code> (q.v.) including scheduled events, special aliases, automatic logout and terminal locking, command timing and watching for logins and logouts. </p>
<p> Support for the Native Language System (see <code>Native Language System support</code>), OS variant features (see <code>OS variant support</code> and the <code>echo_style</code> shell variable) and system-dependent file locations (see <code>FILES</code>). </p>
<p> Extensive terminal-management capabilities. See <code>Terminal management</code>. </p>
<p> New builtin commands including <i>builtins</i>, <i>hup</i>, <i>ls-F</i>, <i>newgrp</i>, <i>printenv</i>, <i>which</i> and <i>where</i> (q.v.). </p>
<p> New variables that make useful information easily available to the shell. See the <code>gid</code>, <code>loginsh</code>, <code>oid</code>, <code>shlvl</code>, <code>tcsh</code>, <code>tty</code>, <code>uid</code> and <code>version</code> shell variables and the <code>HOST</code>, <code>REMOTEHOST</code>, <code>VENDOR</code>, <code>OSTYPE</code> and <code>MACHTYPE</code> environment variables. </p>
<p> A new syntax for including useful information in the prompt string (see <code>prompt</code>), and special prompts for loops and spelling correction (see <code>prompt2</code> and <code>prompt3</code>). </p>
<p> Read-only variables. See <code>Variable substitution</code>.</p>
<h2>BUGS</h2>
<p> When a suspended command is restarted, the shell prints the directory it started in if this is different from the current directory. This can be misleading (i.e., wrong) as the job may have changed directories internally. </p>
<p> Shell builtin functions are not stoppable/restartable. Command sequences of the form `a ; b ; c&#8217; are also not handled gracefully when stopping is attempted. If you suspend `b&#8217;, the shell will then immediately execute `c&#8217;. This is especially noticeable if this expansion results from an <i>alias</i>. It suffices to place the sequence of commands in ()&#8217;s to force it to a subshell, i.e., `( a ; b ; c )&#8217;. </p>
<p> Control over tty output after processes are started is primitive; perhaps this will inspire someone to work on a good virtual terminal interface. In a virtual terminal interface much more interesting things could be done with output control. </p>
<p> Alias substitution is most often used to clumsily simulate shell procedures; shell procedures should be provided rather than aliases. </p>
<p> Control structures should be parsed rather than being recognized as built-in commands. This would allow control commands to be placed anywhere, to be combined with `|&#8217;, and to be used with `&amp;&#8217; and `;&#8217; metasyntax. </p>
<p> <i>foreach</i> doesn&#8217;t ignore here documents when looking for its <i>end</i>. </p>
<p> It should be possible to use the `:&#8217; modifiers on the output of command substitutions. </p>
<p> The screen update for lines longer than the screen width is very poor if the terminal cannot move the cursor up (i.e., terminal type `dumb&#8217;). </p>
<p> <code>HPATH</code> and <code>NOREBIND</code> don&#8217;t need to be environment variables. </p>
<p> Glob-patterns which do not use `?&#8217;, `*&#8217; or `[]&#8217; or which use `{}&#8217; or `~&#8217; are not negated correctly. </p>
<p> The single-command form of <i>if</i> does output redirection even if the expression is false and the command is not executed. </p>
<p> <i>ls-F</i> includes file identification characters when sorting filenames and does not handle control characters in filenames well. It cannot be interrupted. </p>
<p> Command substitution supports multiple commands and conditions, but not cycles or backward <i>goto</i>s. </p>
<p> Report bugs at <a rel="nofollow" href="http://bugs.gw.com/,">http://bugs.gw.com/,</a> preferably with fixes. If you want to help maintain and test tcsh, send mail to tcsh-request [at] mx.gw.com with the text `subscribe tcsh&#8217; on a line by itself in the body.</p>
<h2>THE T IN TCSH</h2>
<p> In 1964, DEC produced the PDP-6. The PDP-10 was a later re-implementation. It was re-christened the DECsystem-10 in 1970 or so when DEC brought out the second model, the KI10. </p>
<p> TENEX was created at Bolt, Beranek &amp; Newman (a Cambridge, Massachusetts think tank) in 1972 as an experiment in demand-paged virtual memory operating systems. They built a new pager for the DEC PDP-10 and created the OS to go with it. It was extremely successful in academia. </p>
<p> In 1975, DEC brought out a new model of the PDP-10, the KL10; they intended to have only a version of TENEX, which they had licensed from BBN, for the new box. They called their version TOPS-20 (their capitalization is trademarked). A lot of TOPS-10 users (`The OPerating System for PDP-10&#8242;) objected; thus DEC found themselves supporting two incompatible systems on the same hardware&#8211;but then there were 6 on the PDP-11! </p>
<p> TENEX, and TOPS-20 to version 3, had command completion via a user-code-level subroutine library called ULTCMD. With version 3, DEC moved all that capability and more into the monitor (`kernel&#8217; for you Unix types), accessed by the COMND% JSYS (`Jump to SYStem&#8217; instruction, the supervisor call mechanism [are my IBM roots also showing?]). </p>
<p> The creator of tcsh was impressed by this feature and several others of TENEX and TOPS-20, and created a version of csh which mimicked them.</p>
<h2>LIMITATIONS</h2>
<p> The system limits argument lists to ARG_MAX characters. </p>
<p> The number of arguments to a command which involves filename expansion is limited to 1/6th the number of characters allowed in an argument list. </p>
<p> Command substitutions may substitute no more characters than are allowed in an argument list. </p>
<p> To detect looping, the shell restricts the number of <i>alias</i> substitutions on a single line to 20.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-csh/">csh</a>(1), <a href="/docs/linux/man/1-emacs/">emacs</a>(1), <a href="/docs/linux/man/1-ls/">ls</a>(1), <a href="/docs/linux/man/1-newgrp/">newgrp</a>(1), <a href="/docs/linux/man/1-sh/">sh</a>(1), <a href="/docs/linux/man/1-setpath/">setpath</a>(1), <a href="/docs/linux/man/1-stty/">stty</a>(1), <a href="/docs/linux/man/1-su/">su</a>(1), <a href="/docs/linux/man/1-tset/">tset</a>(1), <a href="/docs/linux/man/1-vi/">vi</a>(1), <a href="/docs/linux/man/1-x/">x</a>(1), <a href="/docs/linux/man/2-access/">access</a>(2), <a href="/docs/linux/man/2-execve/">execve</a>(2), <a href="/docs/linux/man/2-fork/">fork</a>(2), <a href="/docs/linux/man/2-killpg/">killpg</a>(2), <a href="/docs/linux/man/2-pipe/">pipe</a>(2), <a href="/docs/linux/man/2-setrlimit/">setrlimit</a>(2), <a href="/docs/linux/man/2-sigvec/">sigvec</a>(2), <a href="/docs/linux/man/2-stat/">stat</a>(2), <a href="/docs/linux/man/2-umask/">umask</a>(2), <a href="/docs/linux/man/2-vfork/">vfork</a>(2), <a href="/docs/linux/man/2-wait/">wait</a>(2), <a href="/docs/linux/man/3-malloc/">malloc</a>(3), <a href="/docs/linux/man/3-setlocale/">setlocale</a>(3), <a href="/docs/linux/man/4-tty/">tty</a>(4), <a href="/docs/linux/man/5-a-out/">a.out</a>(5), <a href="/docs/linux/man/5-termcap/">termcap</a>(5), <a href="/docs/linux/man/7-environ/">environ</a>(7), <a href="/docs/linux/man/7-termio/">termio</a>(7), Introduction to the C Shell</p>
<h2>VERSION</h2>
<p> This manual documents tcsh 6.18.01 (Astron) 2012-02-14.</p>
<h2>AUTHORS</h2>
<dl>
<dt>William Joy</p>
<dd> Original author of <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1)</p>
<dt>J.E. Kulp, IIASA, Laxenburg, Austria</p>
<dd> Job control and directory stack features</p>
<dt>Ken Greer, HP Labs, 1981</p>
<dd> File name completion</p>
<dt>Mike Ellis, Fairchild, 1983</p>
<dd> Command name recognition/completion</p>
<dt>Paul Placeway, Ohio State CIS Dept., 1983-1993</p>
<dd> Command line editor, prompt routines, new glob syntax and numerous fixes and speedups</p>
<dt>Karl Kleinpaste, CCI 1983-4</p>
<dd> Special aliases, directory stack extraction stuff, login/logout watch, scheduled events, and the idea of the new prompt format</p>
<dt>Rayan Zachariassen, University of Toronto, 1984</p>
<dd> <i>ls-F</i> and <i>which</i> builtins and numerous bug fixes, modifications and speedups</p>
<dt>Chris Kingsley, Caltech</p>
<dd> Fast storage allocator routines</p>
<dt>Chris Grevstad, TRW, 1987</p>
<dd> Incorporated 4.3BSD <i>csh</i> into <i>tcsh</i></p>
<dt>Christos S. Zoulas, Cornell U. EE Dept., 1987-94</p>
<dd> Ports to HPUX, SVR2 and SVR3, a SysV version of getwd.c, SHORT_STRINGS support and a new version of sh.glob.c</p>
<dt>James J Dempsey, BBN, and Paul Placeway, OSU, 1988</p>
<dd> A/UX port</p>
<dt>Daniel Long, NNSC, 1988</p>
<dd> <code>wordchars</code></p>
<dt>Patrick Wolfe, Kuck and Associates, Inc., 1988</p>
<dd> <i>vi</i> mode cleanup</p>
<dt>David C Lawrence, Rensselaer Polytechnic Institute, 1989</p>
<dd> <code>autolist</code> and ambiguous completion listing</p>
<dt>Alec Wolman, DEC, 1989</p>
<dd> Newlines in the prompt</p>
<dt>Matt Landau, BBN, 1989</p>
<dd> <i>~/.tcshrc</i></p>
<dt>Ray Moody, Purdue Physics, 1989</p>
<dd> Magic space bar history expansion</p>
<dt>Mordechai ????, Intel, 1989</p>
<dd> printprompt() fixes and additions</p>
<dt>Kazuhiro Honda, Dept. of Computer Science, Keio University, 1989</p>
<dd> Automatic spelling correction and <code>prompt3</code></p>
<dt>Per Hedeland, Ellemtel, Sweden, 1990-</p>
<dd> Various bugfixes, improvements and manual updates</p>
<dt>Hans J. Albertsson (Sun Sweden)</p>
<dd> <code>ampm</code>, <i>settc</i> and <i>telltc</i></p>
<dt>Michael Bloom</p>
<dd> Interrupt handling fixes</p>
<dt>Michael Fine, Digital Equipment Corp</p>
<dd> Extended key support</p>
<dt>Eric Schnoebelen, Convex, 1990</p>
<dd> Convex support, lots of <i>csh</i> bug fixes, save and restore of directory stack</p>
<dt>Ron Flax, Apple, 1990</p>
<dd> A/UX 2.0 (re)port</p>
<dt>Dan Oscarsson, LTH Sweden, 1990</p>
<dd> NLS support and simulated NLS support for non NLS sites, fixes</p>
<dt>Johan Widen, SICS Sweden, 1990</p>
<dd> <code>shlvl</code>, Mach support, <i>correct-line</i>, 8-bit printing</p>
<dt>Matt Day, Sanyo Icon, 1990</p>
<dd> POSIX termio support, SysV limit fixes</p>
<dt>Jaap Vermeulen, Sequent, 1990-91</p>
<dd> Vi mode fixes, expand-line, window change fixes, Symmetry port</p>
<dt>Martin Boyer, Institut de recherche d&#8217;Hydro-Quebec, 1991</p>
<dd> <code>autolist</code> beeping options, modified the history search to search for the whole string from the beginning of the line to the cursor.</p>
<dt>Scott Krotz, Motorola, 1991</p>
<dd> Minix port</p>
<dt>David Dawes, Sydney U. Australia, Physics Dept., 1991</p>
<dd> SVR4 job control fixes</p>
<dt>Jose Sousa, Interactive Systems Corp., 1991</p>
<dd> Extended <i>vi</i> fixes and <i>vi</i> delete command</p>
<dt>Marc Horowitz, MIT, 1991</p>
<dd> ANSIfication fixes, new exec hashing code, imake fixes, <i>where</i></p>
<dt>Bruce Sterling Woodcock, sterling [at] netcom.com, 1991-1995</p>
<dd> ETA and Pyramid port, Makefile and lint fixes, <code>ignoreeof</code>=n addition, and various other portability changes and bug fixes</p>
<dt>Jeff Fink, 1992</p>
<dd> <i>complete-word-fwd</i> and <i>complete-word-back</i></p>
<dt>Harry C. Pulley, 1992</p>
<dd> Coherent port</p>
<dt>Andy Phillips, Mullard Space Science Lab U.K., 1992</p>
<dd> VMS-POSIX port</p>
<dt>Beto Appleton, IBM Corp., 1992</p>
<dd> Walking process group fixes, <i>csh</i> bug fixes, POSIX file tests, POSIX SIGHUP</p>
<dt>Scott Bolte, Cray Computer Corp., 1992</p>
<dd> CSOS port</p>
<dt>Kaveh R. Ghazi, Rutgers University, 1992</p>
<dd> Tek, m88k, Titan and Masscomp ports and fixes. Added autoconf support.</p>
<dt>Mark Linderman, Cornell University, 1992</p>
<dd> OS/2 port</p>
<dt>Mika Liljeberg, liljeber [at] kruuna.Helsinki.FI, 1992</p>
<dd> Linux port</p>
<dt>Tim P. Starrin, NASA Langley Research Center Operations, 1993</p>
<dd> Read-only variables</p>
<dt>Dave Schweisguth, Yale University, 1993-4</p>
<dd> New man page and tcsh.man2html</p>
<dt>Larry Schwimmer, Stanford University, 1993</p>
<dd> AFS and HESIOD patches</p>
<dt>Luke Mewburn, RMIT University, 1994-6</p>
<dd> Enhanced directory printing in prompt, added <code>ellipsis</code> and <code>rprompt</code>.</p>
<dt>Edward Hutchins, Silicon Graphics Inc., 1996</p>
<dd> Added implicit cd.</p>
<dt>Martin Kraemer, 1997</p>
<dd> Ported to Siemens Nixdorf EBCDIC machine</p>
<dt>Amol Deshpande, Microsoft, 1997</p>
<dd> Ported to WIN32 (Windows/95 and Windows/NT); wrote all the missing library and message catalog code to interface to Windows.</p>
<dt>Taga Nayuta, 1998</p>
<dd> Color ls additions.</dl>
<h2>THANKS TO</h2>
<p> Bryan Dunlap, Clayton Elwell, Karl Kleinpaste, Bob Manson, Steve Romig, Diana Smetters, Bob Sutterfield, Mark Verber, Elizabeth Zwicky and all the other people at Ohio State for suggestions and encouragement </p>
<p> All the people on the net, for putting up with, reporting bugs in, and suggesting new additions to each and every version </p>
<p> Richard M. Alderson III, for writing the `T in tcsh&#8217; section </p>
<h2>Index</h2>
