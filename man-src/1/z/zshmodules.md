---
title: "zshmodules(1)"
name: "zshmodules"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zshmodules/"
description: "zshmodules – zsh loadable modules"
---

<h2 class="name">NAME</h2>
<p> zshmodules &#8211; zsh loadable modules </p>
<h2>DESCRIPTION</h2>
<p> Some optional parts of zsh are in modules, separate from the core of the shell. Each of these modules may be linked in to the shell at build time, or can be dynamically linked while the shell is running if the installation supports this feature. Modules are linked at runtime with the <code>zmodload</code> command, see <i><a href="/docs/linux/man/1-zshbuiltins/">zshbuiltins</a></i>(1). </p>
<p> The modules that are bundled with the zsh distribution are: </p>
<dl>
<dt>
<dd> <code>zsh/attr</code> Builtins for manipulating extended attributes (xattr).</p>
<dt><code>zsh/cap</code></p>
<dd> Builtins for manipulating POSIX.1e (POSIX.6) capability (privilege) sets.</p>
<dt><code>zsh/clone</code></p>
<dd> A builtin that can clone a running shell onto another terminal.</p>
<dt><code>zsh/compctl</code></p>
<dd> The <code>compctl</code> builtin for controlling completion.</p>
<dt><code>zsh/complete</code></p>
<dd> The basic completion code.</p>
<dt><code>zsh/complist</code></p>
<dd> Completion listing extensions.</p>
<dt><code>zsh/computil</code></p>
<dd> A module with utility builtins needed for the shell function based completion system.</p>
<dt><code>zsh/curses</code></p>
<dd> curses windowing commands</p>
<dt><code>zsh/datetime</code></p>
<dd> Some date/time commands and parameters.</p>
<dt><code>zsh/db/gdbm</code></p>
<dd> Builtins for managing associative array parameters tied to GDBM databases.</p>
<dt><code>zsh/deltochar</code></p>
<dd> A ZLE function duplicating EMACS&#8217; <code>zap-to-char</code>.</p>
<dt><code>zsh/example</code></p>
<dd> An example of how to write a module.</p>
<dt><code>zsh/files</code></p>
<dd> Some basic file manipulation commands as builtins.</p>
<dt><code>zsh/langinfo</code></p>
<dd> Interface to locale information.</p>
<dt><code>zsh/mapfile</code></p>
<dd> Access to external files via a special associative array.</p>
<dt><code>zsh/mathfunc</code></p>
<dd> Standard scientific functions for use in mathematical evaluations.</p>
<dt><code>zsh/nearcolor</code></p>
<dd> Map colours to the nearest colour in the available palette.</p>
<dt><code>zsh/newuser</code></p>
<dd> Arrange for files for new users to be installed.</p>
<dt><code>zsh/parameter</code></p>
<dd> Access to internal hash tables via special associative arrays.</p>
<dt><code>zsh/pcre</code></p>
<dd> Interface to the PCRE library.</p>
<dt><code>zsh/param/private</code></p>
<dd> Builtins for managing private-scoped parameters in function context.</p>
<dt><code>zsh/regex</code></p>
<dd> Interface to the POSIX regex library.</p>
<dt><code>zsh/sched</code></p>
<dd> A builtin that provides a timed execution facility within the shell.</p>
<dt><code>zsh/net/socket</code></p>
<dd> Manipulation of Unix domain sockets</p>
<dt><code>zsh/stat</code></p>
<dd> A builtin command interface to the <code>stat</code> system call.</p>
<dt><code>zsh/system</code></p>
<dd> A builtin interface to various low-level system features.</p>
<dt><code>zsh/net/tcp</code></p>
<dd> Manipulation of TCP sockets</p>
<dt><code>zsh/termcap</code></p>
<dd> Interface to the termcap database.</p>
<dt><code>zsh/terminfo</code></p>
<dd> Interface to the terminfo database.</p>
<dt><code>zsh/zftp</code></p>
<dd> A builtin FTP client.</p>
<dt><code>zsh/zle</code></p>
<dd> The Zsh Line Editor, including the <code>bindkey</code> and <code>vared</code> builtins.</p>
<dt><code>zsh/zleparameter</code></p>
<dd> Access to internals of the Zsh Line Editor via parameters.</p>
<dt><code>zsh/zprof</code></p>
<dd> A module allowing profiling for shell functions.</p>
<dt><code>zsh/zpty</code></p>
<dd> A builtin for starting a command in a pseudo-terminal.</p>
<dt><code>zsh/zselect</code></p>
<dd> Block and return when file descriptors are ready.</p>
<dt><code>zsh/zutil</code></p>
<dd> Some utility builtins, e.g. the one for supporting configuration via styles.</dl>
<h2>THE ZSH/ATTR MODULE</h2>
<p> The <code>zsh/attr</code> module is used for manipulating extended attributes. The <code>-h</code> option causes all commands to operate on symbolic links instead of their targets. The builtins in this module are: </p>
<dl>
<dt>
<dd> <code>zgetattr</code> [ <code>-h</code> ] <i>filename</i> <i>attribute</i> [ <i>parameter</i> ] Get the extended attribute <i>attribute</i> from the specified <i>filename</i>. If the optional argument <i>parameter</i> is given, the attribute is set on that parameter instead of being printed to stdout.</p>
<dt><code>zsetattr</code> [ <code>-h</code> ] <i>filename</i> <i>attribute</i> <i>value</i></p>
<dd> Set the extended attribute <i>attribute</i> on the specified <i>filename</i> to <i>value</i>.</p>
<dt><code>zdelattr</code> [ <code>-h</code> ] <i>filename</i> <i>attribute</i></p>
<dd> Remove the extended attribute <i>attribute</i> from the specified <i>filename</i>.</p>
<dt><code>zlistattr</code> [ <code>-h</code> ] <i>filename</i> [ <i>parameter</i> ]</p>
<dd> List the extended attributes currently set on the specified <i>filename</i>. If the optional argument <i>parameter</i> is given, the list of attributes is set on that parameter instead of being printed to stdout.</dl>
<p> <code>zgetattr</code> and <code>zlistattr</code> allocate memory dynamically. If the attribute or list of attributes grows between the allocation and the call to get them, they return 2. On all other errors, 1 is returned. This allows the calling function to check for this case and retry.</p>
<h2>THE ZSH/CAP MODULE</h2>
<p> The <code>zsh/cap</code> module is used for manipulating POSIX.1e (POSIX.6) capability sets. If the operating system does not support this interface, the builtins defined by this module will do nothing. The builtins in this module are: </p>
<dl>
<dt>
<dd> <code>cap</code> [ <i>capabilities</i> ] Change the shell&#8217;s process capability sets to the specified <i>capabilities</i>, otherwise display the shell&#8217;s current capabilities.</p>
<dt><code>getcap</code> <i>filename</i> &#8230;</p>
<dd> This is a built-in implementation of the POSIX standard utility. It displays the capability sets on each specified <i>filename</i>.</p>
<dt><code>setcap</code> <i>capabilities</i> <i>filename</i> &#8230;</p>
<dd> This is a built-in implementation of the POSIX standard utility. It sets the capability sets on each specified <i>filename</i> to the specified <i>capabilities</i>.</dl>
<h2>THE ZSH/CLONE MODULE</h2>
<p> The <code>zsh/clone</code> module makes available one builtin command: </p>
<dl>
<dt>
<dd> <code>clone</code> <i>tty</i> Creates a forked instance of the current shell, attached to the specified <i>tty</i>. In the new shell, the <code>PID</code>, <code>PPID</code> and <code>TTY</code> special parameters are changed appropriately. <code>$!</code> is set to zero in the new shell, and to the new shell&#8217;s PID in the original shell.</p>
<dl>
<dt>
<dd>
<p> The return status of the builtin is zero in both shells if successful, and non-zero on error. </p>
<p> The target of <code>clone</code> should be an unused terminal, such as an unused virtual console or a virtual terminal created by </p>
<dl>
<dt>
<dd>
<pre><code>
xterm - e sh - c 'trap : INT QUIT TSTP; tty; while:;
do
    sleep 100000000;
done'
</code></pre>
</dl>
<p> Some words of explanation are warranted about this long xterm command line: when doing clone on a pseudo-terminal, some other session (&quot;session&quot; meant as a unix session group, or SID) is already owning the terminal. Hence the cloned zsh cannot acquire the pseudo-terminal as a controlling tty. That means two things: </p>
<dl>
<dt>
<dd> &bull; the job control signals will go to the sh-started-by-xterm process group (that&#8217;s why we disable INT QUIT and TSTP with trap; otherwise the while loop could get suspended or killed)</p>
<dt>&bull;</p>
<dd> the cloned shell will have job control disabled, and the job control keys (control-C, control-\ and control-Z) will not work.</dl>
<p> This does not apply when cloning to an <i>unused</i> vc. </p>
<p> Cloning to a used (and unprepared) terminal will result in two processes reading simultaneously from the same terminal, with input bytes going randomly to either process. </p>
<p> <code>clone</code> is mostly useful as a shell built-in replacement for openvt.</dl>
</dl>
<h2>THE ZSH/COMPCTL MODULE</h2>
<p> The <code>zsh/compctl</code> module makes available two builtin commands. <code>compctl</code>, is the old, deprecated way to control completions for ZLE. See <i><a href="/docs/linux/man/1-zshcompctl/">zshcompctl</a></i>(1). The other builtin command, <code>compcall</code> can be used in user-defined completion widgets, see <i><a href="/docs/linux/man/1-zshcompwid/">zshcompwid</a></i>(1).</p>
<h2>THE ZSH/COMPLETE MODULE</h2>
<p> The <code>zsh/complete</code> module makes available several builtin commands which can be used in user-defined completion widgets, see <i><a href="/docs/linux/man/1-zshcompwid/">zshcompwid</a></i>(1).</p>
<h2>THE ZSH/COMPLIST MODULE</h2>
<p> The <code>zsh/complist</code> module offers three extensions to completion listings: the ability to highlight matches in such a list, the ability to scroll through long lists and a different style of menu completion. </p>
<h3>Colored completion listings</h3>
<p> Whenever one of the parameters <code>ZLS_COLORS</code> or <code>ZLS_COLOURS</code> is set and the <code>zsh/complist</code> module is loaded or linked into the shell, completion lists will be colored. Note, however, that <code>complist</code> will not automatically be loaded if it is not linked in: on systems with dynamic loading, `<code>zmodload zsh/complist</code>&#8216; is required. </p>
<p> The parameters <code>ZLS_COLORS</code> and <code>ZLS_COLOURS</code> describe how matches are highlighted. To turn on highlighting an empty value suffices, in which case all the default values given below will be used. The format of the value of these parameters is the same as used by the GNU version of the <code>ls</code> command: a colon-separated list of specifications of the form `<i>name</i><code>=</code><i>value</i>&#8216;. The <i>name</i> may be one of the following strings, most of which specify file types for which the <i>value</i> will be used. The strings and their default values are: </p>
<dl>
<dt>
<dd> <code>no 0</code> for normal text (i.e. when displaying something other than a matched file)</p>
<dt><code>fi 0</code></p>
<dd> for regular files</p>
<dt><code>di 32</code></p>
<dd> for directories</p>
<dt><code>ln 36</code></p>
<dd> for symbolic links. If this has the special value <code>target</code>, symbolic links are dereferenced and the target file used to determine the display format.</p>
<dt><code>pi 31</code></p>
<dd> for named pipes (FIFOs)</p>
<dt><code>so 33</code></p>
<dd> for sockets</p>
<dt><code>bd 44;37</code></p>
<dd> for block devices</p>
<dt><code>cd 44;37</code></p>
<dd> for character devices</p>
<dt><code>or</code> <i>none</i></p>
<dd> for a symlink to nonexistent file (default is the value defined for <code>ln</code>)</p>
<dt><code>mi</code> <i>none</i></p>
<dd> for a non-existent file (default is the value defined for <code>fi</code>); this code is currently not used</p>
<dt><code>su 37;41</code></p>
<dd> for files with setuid bit set</p>
<dt><code>sg 30;43</code></p>
<dd> for files with setgid bit set</p>
<dt><code>tw 30;42</code></p>
<dd> for world writable directories with sticky bit set</p>
<dt><code>ow 34;43</code></p>
<dd> for world writable directories without sticky bit set</p>
<dt><code>sa</code> <i>none</i></p>
<dd> for files with an associated suffix alias; this is only tested after specific suffixes, as described below</p>
<dt><code>st 37;44</code></p>
<dd> for directories with sticky bit set but not world writable</p>
<dt><code>ex 35</code></p>
<dd> for executable files</p>
<dt><code>lc [</code></p>
<dd> for the left code (see below)</p>
<dt><code>rc m</code></p>
<dd> for the right code</p>
<dt><code>tc 0</code></p>
<dd> for the character indicating the file type printed after filenames if the <code>LIST_TYPES</code> option is set</p>
<dt><code>sp 0</code></p>
<dd> for the spaces printed after matches to align the next column</p>
<dt><code>ec</code> <i>none</i></p>
<dd> for the end code</dl>
<p> Apart from these strings, the <i>name</i> may also be an asterisk (`<code>*</code>&#8216;) followed by any string. The <i>value</i> given for such a string will be used for all files whose name ends with the string. The <i>name</i> may also be an equals sign (`<code>=</code>&#8216;) followed by a pattern; the <code>EXTENDED_GLOB</code> option will be turned on for evaluation of the pattern. The <i>value</i> given for this pattern will be used for all matches (not just filenames) whose display string are matched by the pattern. Definitions for the form with the leading equal sign take precedence over the values defined for file types, which in turn take precedence over the form with the leading asterisk (file extensions). </p>
<p> The leading-equals form also allows different parts of the displayed strings to be colored differently. For this, the pattern has to use the `<code>(#b)</code>&#8216; globbing flag and pairs of parentheses surrounding the parts of the strings that are to be colored differently. In this case the <i>value</i> may consist of more than one color code separated by equal signs. The first code will be used for all parts for which no explicit code is specified and the following codes will be used for the parts matched by the sub-patterns in parentheses. For example, the specification `<code>=(#b)(?)*(?)=0=3=7</code>&#8216; will be used for all matches which are at least two characters long and will use the code `<code>3</code>&#8216; for the first character, `<code>7</code>&#8216; for the last character and `<code>0</code>&#8216; for the rest. </p>
<p> All three forms of <i>name</i> may be preceded by a pattern in parentheses. If this is given, the <i>value</i> will be used only for matches in groups whose names are matched by the pattern given in the parentheses. For example, `<code>(g*)m*=43</code>&#8216; highlights all matches beginning with `<code>m</code>&#8216; in groups whose names begin with `<code>g</code>&#8216; using the color code `<code>43</code>&#8216;. In case of the `<code>lc</code>&#8216;, `<code>rc</code>&#8216;, and `<code>ec</code>&#8216; codes, the group pattern is ignored. </p>
<p> Note also that all patterns are tried in the order in which they appear in the parameter value until the first one matches which is then used. Patterns may be matched against completions, descriptions (possibly with spaces appended for padding), or lines consisting of a completion followed by a description. For consistent coloring it may be necessary to use more than one pattern or a pattern with backreferences. </p>
<p> When printing a match, the code prints the value of <code>lc</code>, the value for the file-type or the last matching specification with a `<code>*</code>&#8216;, the value of <code>rc</code>, the string to display for the match itself, and then the value of <code>ec</code> if that is defined or the values of <code>lc</code>, <code>no</code>, and <code>rc</code> if <code>ec</code> is not defined. </p>
<p> The default values are ISO 6429 (ANSI) compliant and can be used on vt100 compatible terminals such as <code>xterm</code>s. On monochrome terminals the default values will have no visible effect. The <code>colors</code> function from the contribution can be used to get associative arrays containing the codes for ANSI terminals (see the section `Other Functions&#8217; in <i><a href="/docs/linux/man/1-zshcontrib/">zshcontrib</a></i>(1)). For example, after loading <code>colors</code>, one could use `<code>$color[red]</code>&#8216; to get the code for foreground color red and `<code>$color[bg-green]</code>&#8216; for the code for background color green. </p>
<p> If the completion system invoked by compinit is used, these parameters should not be set directly because the system controls them itself. Instead, the <code>list-colors</code> style should be used (see the section `Completion System Configuration&#8217; in <i><a href="/docs/linux/man/1-zshcompsys/">zshcompsys</a></i>(1)). </p>
<h3>Scrolling in completion listings</h3>
<p> To enable scrolling through a completion list, the <code>LISTPROMPT</code> parameter must be set. Its value will be used as the prompt; if it is the empty string, a default prompt will be used. The value may contain escapes of the form `<code>%x</code>&#8216;. It supports the escapes `<code>%B</code>&#8216;, `<code>%b</code>&#8216;, `<code>%S</code>&#8216;, `<code>%s</code>&#8216;, `<code>%U</code>&#8216;, `<code>%u</code>&#8216;, `<code>%F</code>&#8216;, `<code>%f</code>&#8216;, `<code>%K</code>&#8216;, `<code>%k</code>&#8216; and `<code>%{</code><i>&#8230;</i><code>%}</code>&#8216; used also in shell prompts as well as three pairs of additional sequences: a `<code>%l</code>&#8216; or `<code>%L</code>&#8216; is replaced by the number of the last line shown and the total number of lines in the form `<i>number</i><code>/</code><i>total</i>&#8216;; a `<code>%m</code>&#8216; or `<code>%M</code>&#8216; is replaced with the number of the last match shown and the total number of matches; and `<code>%p</code>&#8216; or `<code>%P</code>&#8216; is replaced with `<code>Top</code>&#8216;, `<code>Bottom</code>&#8216; or the position of the first line shown in percent of the total number of lines, respectively. In each of these cases the form with the uppercase letter will be replaced with a string of fixed width, padded to the right with spaces, while the lowercase form will not be padded. </p>
<p> If the parameter <code>LISTPROMPT</code> is set, the completion code will not ask if the list should be shown. Instead it immediately starts displaying the list, stopping after the first screenful, showing the prompt at the bottom, waiting for a keypress after temporarily switching to the <code>listscroll</code> keymap. Some of the zle functions have a special meaning while scrolling lists: </p>
<dl>
<dt>
<dd> <code>send-break</code> stops listing discarding the key pressed</p>
<dt>
<dd> <code>accept-line</code>, <code>down-history</code>, <code>down-line-or-history</code></p>
<dt>
<dd> <code>down-line-or-search</code>, <code>vi-down-line-or-history</code> scrolls forward one line</p>
<dt>
<dd> <code>complete-word</code>, <code>menu-complete</code>, <code>expand-or-complete</code></p>
<dt>
<dd> <code>expand-or-complete-prefix</code>, <code>menu-complete-or-expand</code> scrolls forward one screenful</p>
<dt><code>accept-search</code></p>
<dd> stop listing but take no other action</dl>
<p> Every other character stops listing and immediately processes the key as usual. Any key that is not bound in the <code>listscroll</code> keymap or that is bound to <code>undefined-key</code> is looked up in the keymap currently selected. </p>
<p> As for the <code>ZLS_COLORS</code> and <code>ZLS_COLOURS</code> parameters, <code>LISTPROMPT</code> should not be set directly when using the shell function based completion system. Instead, the <code>list-prompt</code> style should be used. </p>
<h3>Menu selection</h3>
<p> The <code>zsh/complist</code> module also offers an alternative style of selecting matches from a list, called menu selection, which can be used if the shell is set up to return to the last prompt after showing a completion list (see the <code>ALWAYS_LAST_PROMPT</code> option in <i><a href="/docs/linux/man/1-zshoptions/">zshoptions</a></i>(1)). </p>
<p> Menu selection can be invoked directly by the widget <code>menu-select</code> defined by this module. This is a standard ZLE widget that can be bound to a key in the usual way as described in <i><a href="/docs/linux/man/1-zshzle/">zshzle</a></i>(1). </p>
<p> Alternatively, the parameter <code>MENUSELECT</code> can be set to an integer, which gives the minimum number of matches that must be present before menu selection is automatically turned on. This second method requires that menu completion be started, either directly from a widget such as <code>menu-complete</code>, or due to one of the options <code>MENU_COMPLETE</code> or <code>AUTO_MENU</code> being set. If <code>MENUSELECT</code> is set, but is 0, 1 or empty, menu selection will always be started during an ambiguous menu completion. </p>
<p> When using the completion system based on shell functions, the <code>MENUSELECT</code> parameter should not be used (like the <code>ZLS_COLORS</code> and <code>ZLS_COLOURS</code> parameters described above). Instead, the <code>menu</code> style should be used with the <code>select=</code><i>&#8230;</i> keyword. </p>
<p> After menu selection is started, the matches will be listed. If there are more matches than fit on the screen, only the first screenful is shown. The matches to insert into the command line can be selected from this list. In the list one match is highlighted using the value for <code>ma</code> from the <code>ZLS_COLORS</code> or <code>ZLS_COLOURS</code> parameter. The default value for this is `<code>7</code>&#8216; which forces the selected match to be highlighted using standout mode on a vt100-compatible terminal. If neither <code>ZLS_COLORS</code> nor <code>ZLS_COLOURS</code> is set, the same terminal control sequence as for the `<code>%S</code>&#8216; escape in prompts is used. </p>
<p> If there are more matches than fit on the screen and the parameter <code>MENUPROMPT</code> is set, its value will be shown below the matches. It supports the same escape sequences as <code>LISTPROMPT</code>, but the number of the match or line shown will be that of the one where the mark is placed. If its value is the empty string, a default prompt will be used. </p>
<p> The <code>MENUSCROLL</code> parameter can be used to specify how the list is scrolled. If the parameter is unset, this is done line by line, if it is set to `<code>0</code>&#8216; (zero), the list will scroll half the number of lines of the screen. If the value is positive, it gives the number of lines to scroll and if it is negative, the list will be scrolled the number of lines of the screen minus the (absolute) value. </p>
<p> As for the <code>ZLS_COLORS</code>, <code>ZLS_COLOURS</code> and <code>LISTPROMPT</code> parameters, neither <code>MENUPROMPT</code> nor <code>MENUSCROLL</code> should be set directly when using the shell function based completion system. Instead, the <code>select-prompt</code> and <code>select-scroll</code> styles should be used. </p>
<p> The completion code sometimes decides not to show all of the matches in the list. These hidden matches are either matches for which the completion function which added them explicitly requested that they not appear in the list (using the <code>-n</code> option of the <code>compadd</code> builtin command) or they are matches which duplicate a string already in the list (because they differ only in things like prefixes or suffixes that are not displayed). In the list used for menu selection, however, even these matches are shown so that it is possible to select them. To highlight such matches the <code>hi</code> and <code>du</code> capabilities in the <code>ZLS_COLORS</code> and <code>ZLS_COLOURS</code> parameters are supported for hidden matches of the first and second kind, respectively. </p>
<p> Selecting matches is done by moving the mark around using the zle movement functions. When not all matches can be shown on the screen at the same time, the list will scroll up and down when crossing the top or bottom line. The following zle functions have special meaning during menu selection. Note that the following always perform the same task within the menu selection map and cannot be replaced by user defined widgets, nor can the set of functions be extended: </p>
<dl>
<dt>
<dd> <code>accept-line</code>, <code>accept-search</code> accept the current match and leave menu selection (but do not cause the command line to be accepted)</p>
<dt><code>send-break</code></p>
<dd> leaves menu selection and restores the previous contents of the command line</p>
<dt><code>redisplay</code>, <code>clear-screen</code></p>
<dd> execute their normal function without leaving menu selection</p>
<dt><code>accept-and-hold</code>, <code>accept-and-menu-complete</code></p>
<dd> accept the currently inserted match and continue selection allowing to select the next match to insert into the line</p>
<dt><code>accept-and-infer-next-history</code></p>
<dd> accepts the current match and then tries completion with menu selection again; in the case of files this allows one to select a directory and immediately attempt to complete files in it; if there are no matches, a message is shown and one can use <code>undo</code> to go back to completion on the previous level, every other key leaves menu selection (including the other zle functions which are otherwise special during menu selection)</p>
<dt><code>undo</code></p>
<dd> removes matches inserted during the menu selection by one of the three functions before</p>
<dt>
<dd> <code>down-history</code>, <code>down-line-or-history</code></p>
<dt>
<dd> <code>vi-down-line-or-history</code>, <code>down-line-or-search</code> moves the mark one line down</p>
<dt>
<dd> <code>up-history</code>, <code>up-line-or-history</code></p>
<dt>
<dd> <code>vi-up-line-or-history</code>, <code>up-line-or-search</code> moves the mark one line up</p>
<dt><code>forward-char</code>, <code>vi-forward-char</code></p>
<dd> moves the mark one column right</p>
<dt><code>backward-char</code>, <code>vi-backward-char</code></p>
<dd> moves the mark one column left</p>
<dt>
<dd> <code>forward-word</code>, <code>vi-forward-word</code></p>
<dt>
<dd> <code>vi-forward-word-end</code>, <code>emacs-forward-word</code> moves the mark one screenful down</p>
<dt><code>backward-word</code>, <code>vi-backward-word</code>, <code>emacs-backward-word</code></p>
<dd> moves the mark one screenful up</p>
<dt><code>vi-forward-blank-word</code>, <code>vi-forward-blank-word-end</code></p>
<dd> moves the mark to the first line of the next group of matches</p>
<dt><code>vi-backward-blank-word</code></p>
<dd> moves the mark to the last line of the previous group of matches</p>
<dt><code>beginning-of-history</code></p>
<dd> moves the mark to the first line</p>
<dt><code>end-of-history</code></p>
<dd> moves the mark to the last line</p>
<dt>
<dd> <code>beginning-of-buffer-or-history</code>, <code>beginning-of-line</code></p>
<dt>
<dd> <code>beginning-of-line-hist</code>, <code>vi-beginning-of-line</code> moves the mark to the leftmost column</p>
<dt>
<dd> <code>end-of-buffer-or-history</code>, <code>end-of-line</code></p>
<dt>
<dd> <code>end-of-line-hist</code>, <code>vi-end-of-line</code> moves the mark to the rightmost column</p>
<dt>
<dd> <code>complete-word</code>, <code>menu-complete</code>, <code>expand-or-complete</code></p>
<dt>
<dd> <code>expand-or-complete-prefix</code>, <code>menu-expand-or-complete</code> moves the mark to the next match</p>
<dt><code>reverse-menu-complete</code></p>
<dd> moves the mark to the previous match</p>
<dt><code>vi-insert</code></p>
<dd> this toggles between normal and interactive mode; in interactive mode the keys bound to <code>self-insert</code> and <code>self-insert-unmeta</code> insert into the command line as in normal editing mode but without leaving menu selection; after each character completion is tried again and the list changes to contain only the new matches; the completion widgets make the longest unambiguous string be inserted in the command line and <code>undo</code> and <code>backward-delete-char</code> go back to the previous set of matches</p>
<dt>
<dd> <code>history-incremental-search-forward</code></p>
<dt>
<dd> <code>history-incremental-search-backward</code> this starts incremental searches in the list of completions displayed; in this mode, <code>accept-line</code> only leaves incremental search, going back to the normal menu selection mode</dl>
<p> All movement functions wrap around at the edges; any other zle function not listed leaves menu selection and executes that function. It is possible to make widgets in the above list do the same by using the form of the widget with a `<code>.</code>&#8216; in front. For example, the widget `<code>.accept-line</code>&#8216; has the effect of leaving menu selection and accepting the entire command line. </p>
<p> During this selection the widget uses the keymap <code>menuselect</code>. Any key that is not defined in this keymap or that is bound to <code>undefined-key</code> is looked up in the keymap currently selected. This is used to ensure that the most important keys used during selection (namely the cursor keys, return, and TAB) have sensible defaults. However, keys in the <code>menuselect</code> keymap can be modified directly using the <code>bindkey</code> builtin command (see <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1)). For example, to make the return key leave menu selection without accepting the match currently selected one could call </p>
<dl>
<dt>
<dd>
<pre>
<code>bindkey -M menuselect '^M' send-break</code>
</pre>
</dl>
<p> after loading the <code>zsh/complist</code> module.</p>
<h2>THE ZSH/COMPUTIL MODULE</h2>
<p> The <code>zsh/computil</code> module adds several builtin commands that are used by some of the completion functions in the completion system based on shell functions (see <i><a href="/docs/linux/man/1-zshcompsys/">zshcompsys</a></i>(1) ). Except for <code>compquote</code> these builtin commands are very specialised and thus not very interesting when writing your own completion functions. In summary, these builtin commands are: </p>
<dl>
<dt>
<dd> <code>comparguments</code> This is used by the <code>_arguments</code> function to do the argument and command line parsing. Like <code>compdescribe</code> it has an option <code>-i</code> to do the parsing and initialize some internal state and various options to access the state information to decide what should be completed.</p>
<dt><code>compdescribe</code></p>
<dd> This is used by the <code>_describe</code> function to build the displays for the matches and to get the strings to add as matches with their options. On the first call one of the options <code>-i</code> or <code>-I</code> should be supplied as the first argument. In the first case, display strings without the descriptions will be generated, in the second case, the string used to separate the matches from their descriptions must be given as the second argument and the descriptions (if any) will be shown. All other arguments are like the definition arguments to <code>_describe</code> itself.</p>
<dl>
<dt>
<dd>
<p> Once <code>compdescribe</code> has been called with either the <code>-i</code> or the <code>-I</code> option, it can be repeatedly called with the <code>-g</code> option and the names of four parameters as its arguments. This will step through the different sets of matches and store the value of <code>compstate[list]</code> in the first scalar, the options for <code>compadd</code> in the second array, the matches in the third array, and the strings to be displayed in the completion listing in the fourth array. The arrays may then be directly given to <code>compadd</code> to register the matches with the completion code.</dl>
<dt><code>compfiles</code></p>
<dd> Used by the <code>_path_files</code> function to optimize complex recursive filename generation (globbing). It does three things. With the <code>-p</code> and <code>-P</code> options it builds the glob patterns to use, including the paths already handled and trying to optimize the patterns with respect to the prefix and suffix from the line and the match specification currently used. The <code>-i</code> option does the directory tests for the <code>ignore-parents</code> style and the <code>-r</code> option tests if a component for some of the matches are equal to the string on the line and removes all other matches if that is true.</p>
<dt><code>compgroups</code></p>
<dd> Used by the <code>_tags</code> function to implement the internals of the <code>group-order</code> style. This only takes its arguments as names of completion groups and creates the groups for it (all six types: sorted and unsorted, both without removing duplicates, with removing all duplicates and with removing consecutive duplicates).</p>
<dt><code>compquote</code> [ <code>-p</code> ] <i>names</i> &#8230;</p>
<dd> There may be reasons to write completion functions that have to add the matches using the <code>-Q</code> option to <code>compadd</code> and perform quoting themselves. Instead of interpreting the first character of the <code>all_quotes</code> key of the <code>compstate</code> special association and using the <code>q</code> flag for parameter expansions, one can use this builtin command. The arguments are the names of scalar or array parameters and the values of these parameters are quoted as needed for the innermost quoting level. If the <code>-p</code> option is given, quoting is done as if there is some prefix before the values of the parameters, so that a leading equal sign will not be quoted.</p>
<dl>
<dt>
<dd>
<p> The return status is non-zero in case of an error and zero otherwise.</dl>
<dt>
<dd> <code>comptags</code></p>
<dt>
<dd> <code>comptry</code> These implement the internals of the tags mechanism.</p>
<dt><code>compvalues</code></p>
<dd> Like <code>comparguments</code>, but for the <code>_values</code> function.</dl>
<h2>THE ZSH/CURSES MODULE</h2>
<p> The <code>zsh/curses</code> module makes available one builtin command and various parameters. </p>
<h3>Builtin</h3>
<dl>
<dt>
<dd> <code>zcurses</code> <code>init</code></p>
<dt>
<dd> <code>zcurses</code> <code>end</code></p>
<dt>
<dd> <code>zcurses</code> <code>addwin</code> <i>targetwin</i> <i>nlines</i> <i>ncols</i> <i>begin_y</i> <i>begin_x</i> [ <i>parentwin</i> ]</p>
<dt>
<dd> <code>zcurses</code> <code>delwin</code> <i>targetwin</i></p>
<dt>
<dd> <code>zcurses</code> <code>refresh</code> [ <i>targetwin</i> &#8230; ]</p>
<dt>
<dd> <code>zcurses</code> <code>touch</code> <i>targetwin</i> &#8230;</p>
<dt>
<dd> <code>zcurses</code> <code>move</code> <i>targetwin</i> <i>new_y</i> <i>new_x</i></p>
<dt>
<dd> <code>zcurses</code> <code>clear</code> <i>targetwin</i> [ <code>redraw</code> | <code>eol</code> | <code>bot</code> ]</p>
<dt>
<dd> <code>zcurses</code> <code>position</code> <i>targetwin</i> <i>array</i></p>
<dt>
<dd> <code>zcurses</code> <code>char</code> <i>targetwin</i> <i>character</i></p>
<dt>
<dd> <code>zcurses</code> <code>string</code> <i>targetwin</i> <i>string</i></p>
<dt>
<dd> <code>zcurses</code> <code>border</code> <i>targetwin</i> <i>border</i></p>
<dt>
<dd> <code>zcurses</code> <code>attr</code> <i>targetwin</i> [ [<code>+</code>|<code>&#8211;</code>]<i>attribute</i> | <i>fg_col</i><code>/</code><i>bg_col</i> ] [&#8230;]</p>
<dt>
<dd> <code>zcurses</code> <code>bg</code> <i>targetwin</i> [ [<code>+</code>|<code>&#8211;</code>]<i>attribute</i> | <i>fg_col</i><code>/</code><i>bg_col</i> | <code>@</code><i>char</i> ] [&#8230;]</p>
<dt>
<dd> <code>zcurses</code> <code>scroll</code> <i>targetwin</i> [ <code>on</code> | <code>off</code> | [<code>+</code>|<code>&#8211;</code>]<i>lines</i> ]</p>
<dt>
<dd> <code>zcurses</code> <code>input</code> <i>targetwin</i> [ <i>param</i> [ <i>kparam</i> [ <i>mparam</i> ] ] ]</p>
<dt>
<dd> <code>zcurses</code> <code>mouse</code> [ <code>delay</code> <i>num</i> | [<code>+</code>|<code>&#8211;</code>]<code>motion</code> ]</p>
<dt>
<dd> <code>zcurses</code> <code>timeout</code> <i>targetwin</i> <i>intval</i></p>
<dt>
<dd> <code>zcurses</code> <code>querychar</code> <i>targetwin</i> [ <i>param</i> ]</p>
<dt>
<dd> <code>zcurses</code> <code>resize</code> <i>height</i> <i>width</i> [ <code>endwin</code> | <code>nosave</code> | <code>endwin_nosave</code> ] Manipulate curses windows. All uses of this command should be bracketed by `<code>zcurses init</code>&#8216; to initialise use of curses, and `<code>zcurses end</code>&#8216; to end it; omitting `<code>zcurses end</code>&#8216; can cause the terminal to be in an unwanted state.</p>
<dl>
<dt>
<dd>
<p> The subcommand <code>addwin</code> creates a window with <i>nlines</i> lines and <i>ncols</i> columns. Its upper left corner will be placed at row <i>begin_y</i> and column <i>begin_x</i> of the screen. <i>targetwin</i> is a string and refers to the name of a window that is not currently assigned. Note in particular the curses convention that vertical values appear before horizontal values. </p>
<p> If <code>addwin</code> is given an existing window as the final argument, the new window is created as a subwindow of <i>parentwin</i>. This differs from an ordinary new window in that the memory of the window contents is shared with the parent&#8217;s memory. Subwindows must be deleted before their parent. Note that the coordinates of subwindows are relative to the screen, not the parent, as with other windows. </p>
<p> Use the subcommand <code>delwin</code> to delete a window created with <code>addwin</code>. Note that <code>end</code> does <i>not</i> implicitly delete windows, and that <code>delwin</code> does not erase the screen image of the window. </p>
<p> The window corresponding to the full visible screen is called <code>stdscr</code>; it always exists after `<code>zcurses init</code>&#8216; and cannot be delete with <code>delwin</code>. </p>
<p> The subcommand <code>refresh</code> will refresh window <i>targetwin</i>; this is necessary to make any pending changes (such as characters you have prepared for output with <code>char</code>) visible on the screen. <code>refresh</code> without an argument causes the screen to be cleared and redrawn. If multiple windows are given, the screen is updated once at the end. </p>
<p> The subcommand <code>touch</code> marks the <i>targetwin</i>s listed as changed. This is necessary before <code>refresh</code>ing windows if a window that was in front of another window (which may be <code>stdscr</code>) is deleted. </p>
<p> The subcommand <code>move</code> moves the cursor position in <i>targetwin</i> to new coordinates <i>new_y</i> and <i>new_x</i>. Note that the subcommand <code>string</code> (but not the subcommand <code>char</code>) advances the cursor position over the characters added. </p>
<p> The subcommand <code>clear</code> erases the contents of <i>targetwin</i>. One (and no more than one) of three options may be specified. With the option <code>redraw</code>, in addition the next <code>refresh</code> of <i>targetwin</i> will cause the screen to be cleared and repainted. With the option <code>eol</code>, <i>targetwin</i> is only cleared to the end of the current cursor line. With the option <code>bot</code>, <i>targetwin</i> is cleared to the end of the window, i.e everything to the right and below the cursor is cleared. </p>
<p> The subcommand <code>position</code> writes various positions associated with <i>targetwin</i> into the array named <i>array</i>. These are, in order:</p>
<dl>
<dt>&#8211;</p>
<dd> The y and x coordinates of the cursor relative to the top left of <i>targetwin</i></p>
<dt>&#8211;</p>
<dd> The y and x coordinates of the top left of <i>targetwin</i> on the screen</p>
<dt>&#8211;</p>
<dd> The size of <i>targetwin</i> in y and x dimensions.</dl>
<p> Outputting characters and strings are achieved by <code>char</code> and <code>string</code> respectively. </p>
<p> To draw a border around window <i>targetwin</i>, use <code>border</code>. Note that the border is not subsequently handled specially: in other words, the border is simply a set of characters output at the edge of the window. Hence it can be overwritten, can scroll off the window, etc. </p>
<p> The subcommand <code>attr</code> will set <i>targetwin</i>&#8216;s attributes or foreground/background color pair for any successive character output. Each <i>attribute</i> given on the line may be prepended by a <code>+</code> to set or a <code>&#8211;</code> to unset that attribute; <code>+</code> is assumed if absent. The attributes supported are <code>blink</code>, <code>bold</code>, <code>dim</code>, <code>reverse</code>, <code>standout</code>, and <code>underline</code>. </p>
<p> Each <i>fg_col</i><code>/</code><i>bg_col</i> attribute (to be read as `<i>fg_col</i> on <i>bg_col</i>&#8216;) sets the foreground and background color for character output. The color <code>default</code> is sometimes available (in particular if the library is ncurses), specifying the foreground or background color with which the terminal started. The color pair <code>default/default</code> is always available. To use more than the 8 named colors (red, green, etc.) construct the <i>fg_col</i><code>/</code><i>bg_col</i> pairs where <i>fg_col</i> and <i>bg_col</i> are decimal integers, e.g <code>128/200</code>. The maximum color value is 254 if the terminal supports 256 colors. </p>
<p> <code>bg</code> overrides the color and other attributes of all characters in the window. Its usual use is to set the background initially, but it will overwrite the attributes of any characters at the time when it is called. In addition to the arguments allowed with <code>attr</code>, an argument <code>@</code><i>char</i> specifies a character to be shown in otherwise blank areas of the window. Owing to limitations of curses this cannot be a multibyte character (use of ASCII characters only is recommended). As the specified set of attributes override the existing background, turning attributes off in the arguments is not useful, though this does not cause an error. </p>
<p> The subcommand <code>scroll</code> can be used with <code>on</code> or <code>off</code> to enabled or disable scrolling of a window when the cursor would otherwise move below the window due to typing or output. It can also be used with a positive or negative integer to scroll the window up or down the given number of lines without changing the current cursor position (which therefore appears to move in the opposite direction relative to the window). In the second case, if scrolling is <code>off</code> it is temporarily turned <code>on</code> to allow the window to be scrolled. </p>
<p> The subcommand <code>input</code> reads a single character from the window without echoing it back. If <i>param</i> is supplied the character is assigned to the parameter <i>param</i>, else it is assigned to the parameter <code>REPLY</code>. </p>
<p> If both <i>param</i> and <i>kparam</i> are supplied, the key is read in `keypad&#8217; mode. In this mode special keys such as function keys and arrow keys return the name of the key in the parameter <i>kparam</i>. The key names are the macros defined in the <code>curses.h</code> or <code>ncurses.h</code> with the prefix `<code>KEY_</code>&#8216; removed; see also the description of the parameter <code>zcurses_keycodes</code> below. Other keys cause a value to be set in <i>param</i> as before. On a successful return only one of <i>param</i> or <i>kparam</i> contains a non-empty string; the other is set to an empty string. </p>
<p> If <i>mparam</i> is also supplied, <code>input</code> attempts to handle mouse input. This is only available with the ncurses library; mouse handling can be detected by checking for the exit status of `<code>zcurses mouse</code>&#8216; with no arguments. If a mouse button is clicked (or double- or triple-clicked, or pressed or released with a configurable delay from being clicked) then <code>kparam</code> is set to the string <code>MOUSE</code>, and <i>mparam</i> is set to an array consisting of the following elements:</p>
<dl>
<dt>&#8211;</p>
<dd> An identifier to discriminate different input devices; this is only rarely useful.</p>
<dt>&#8211;</p>
<dd> The x, y and z coordinates of the mouse click relative to the full screen, as three elements in that order (i.e. the y coordinate is, unusually, after the x coordinate). The z coordinate is only available for a few unusual input devices and is otherwise set to zero.</p>
<dt>&#8211;</p>
<dd> Any events that occurred as separate items; usually there will be just one. An event consists of <code>PRESSED</code>, <code>RELEASED</code>, <code>CLICKED</code>, <code>DOUBLE_CLICKED</code> or <code>TRIPLE_CLICKED</code> followed immediately (in the same element) by the number of the button.</p>
<dt>&#8211;</p>
<dd> If the shift key was pressed, the string <code>SHIFT</code>.</p>
<dt>&#8211;</p>
<dd> If the control key was pressed, the string <code>CTRL</code>.</p>
<dt>&#8211;</p>
<dd> If the alt key was pressed, the string <code>ALT</code>.</dl>
<p> Not all mouse events may be passed through to the terminal window; most terminal emulators handle some mouse events themselves. Note that the ncurses manual implies that using input both with and without mouse handling may cause the mouse cursor to appear and disappear. </p>
<p> The subcommand <code>mouse</code> can be used to configure the use of the mouse. There is no window argument; mouse options are global. `<code>zcurses mouse</code>&#8216; with no arguments returns status 0 if mouse handling is possible, else status 1. Otherwise, the possible arguments (which may be combined on the same command line) are as follows. <code>delay</code> <i>num</i> sets the maximum delay in milliseconds between press and release events to be considered as a click; the value 0 disables click resolution, and the default is one sixth of a second. <code>motion</code> proceeded by an optional `<code>+</code>&#8216; (the default) or <code>&#8211;</code> turns on or off reporting of mouse motion in addition to clicks, presses and releases, which are always reported. However, it appears reports for mouse motion are not currently implemented. </p>
<p> The subcommand <code>timeout</code> specifies a timeout value for input from <i>targetwin</i>. If <i>intval</i> is negative, `<code>zcurses input</code>&#8216; waits indefinitely for a character to be typed; this is the default. If <i>intval</i> is zero, `<code>zcurses input</code>&#8216; returns immediately; if there is typeahead it is returned, else no input is done and status 1 is returned. If <i>intval</i> is positive, `<code>zcurses input</code>&#8216; waits <i>intval</i> milliseconds for input and if there is none at the end of that period returns status 1. </p>
<p> The subcommand <code>querychar</code> queries the character at the current cursor position. The return values are stored in the array named <i>param</i> if supplied, else in the array <code>reply</code>. The first value is the character (which may be a multibyte character if the system supports them); the second is the color pair in the usual <i>fg_col</i><code>/</code><i>bg_col</i> notation, or <code>0</code> if color is not supported. Any attributes other than color that apply to the character, as set with the subcommand <code>attr</code>, appear as additional elements. </p>
<p> The subcommand <code>resize</code> resizes <code>stdscr</code> and all windows to given dimensions (windows that stick out from the new dimensions are resized down). The underlying curses extension (<code>resize_term call</code>) can be unavailable. To verify, zeroes can be used for <i>height</i> and <i>width</i>. If the result of the subcommand is <code>0</code>, resize_term is available (<code>2</code> otherwise). Tests show that resizing can be normally accomplished by calling <code>zcurses end</code> and <code>zcurses refresh</code>. The <code>resize</code> subcommand is provided for versatility. Multiple system configurations have been checked and <code>zcurses end</code> and <code>zcurses refresh</code> are still needed for correct terminal state after resize. To invoke them with <code>resize</code>, use <i>endwin</i> argument. Using <i>nosave</i> argument will cause new terminal state to not be saved internally by <code>zcurses</code>. This is also provided for versatility and should normally be not needed.</dl>
</dl>
<h3>Parameters</h3>
<dl>
<dt>
<dd> <code>ZCURSES_COLORS</code> Readonly integer. The maximum number of colors the terminal supports. This value is initialised by the curses library and is not available until the first time <code>zcurses init</code> is run.</p>
<dt><code>ZCURSES_COLOR_PAIRS</code></p>
<dd> Readonly integer. The maximum number of color pairs <i>fg_col</i><code>/</code><i>bg_col</i> that may be defined in `<code>zcurses attr</code>&#8216; commands; note this limit applies to all color pairs that have been used whether or not they are currently active. This value is initialised by the curses library and is not available until the first time <code>zcurses init</code> is run.</p>
<dt><code>zcurses_attrs</code></p>
<dd> Readonly array. The attributes supported by <code>zsh/curses</code>; available as soon as the module is loaded.</p>
<dt><code>zcurses_colors</code></p>
<dd> Readonly array. The colors supported by <code>zsh/curses</code>; available as soon as the module is loaded.</p>
<dt><code>zcurses_keycodes</code></p>
<dd> Readonly array. The values that may be returned in the second parameter supplied to `<code>zcurses input</code>&#8216; in the order in which they are defined internally by curses. Not all function keys are listed, only <code>F0</code>; curses reserves space for <code>F0</code> up to <code>F63</code>.</p>
<dt><code>zcurses_windows</code></p>
<dd> Readonly array. The current list of windows, i.e. all windows that have been created with `<code>zcurses addwin</code>&#8216; and not removed with `<code>zcurses delwin</code>&#8216;.</dl>
<h2>THE ZSH/DATETIME MODULE</h2>
<p> The <code>zsh/datetime</code> module makes available one builtin command: </p>
<dl>
<dt>
<dd> <code>strftime</code> [ <code>-s</code> <i>scalar</i> ] <i>format</i> [ <i>epochtime</i> [ <i>nanoseconds</i> ] ]</p>
<dt>
<dd> <code>strftime</code> <code>-r</code> [ <code>-q</code> ] [ <code>-s</code> <i>scalar</i> ] <i>format</i> <i>timestring</i> Output the date in the <i>format</i> specified. With no <i>epochtime</i>, the current system date/time is used; optionally, <i>epochtime</i> may be used to specify the number of seconds since the epoch, and <i>nanoseconds</i> may additionally be used to specify the number of nanoseconds past the second (otherwise that number is assumed to be 0). See <i><a href="/docs/linux/man/3-strftime/">strftime</a></i>(3) for details. The zsh extensions described in the section EXPANSION OF PROMPT SEQUENCES in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1) are also available.</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>-q</code> Run quietly; suppress printing of all error messages described below. Errors for invalid <i>epochtime</i> values are always printed.</p>
<dt><code>-r</code></p>
<dd> With the option <code>-r</code> (reverse), use <i>format</i> to parse the input string <i>timestring</i> and output the number of seconds since the epoch at which the time occurred. The parsing is implemented by the system function <code>strptime</code>; see <i><a href="/docs/linux/man/3-strptime/">strptime</a></i>(3). This means that zsh format extensions are not available, but for reverse lookup they are not required.</p>
<dl>
<dt>
<dd>
<p> In most implementations of <code>strftime</code> any timezone in the <i>timestring</i> is ignored and the local timezone declared by the <code>TZ</code> environment variable is used; other parameters are set to zero if not present. </p>
<p> If <i>timestring</i> does not match <i>format</i> the command returns status 1 and prints an error message. If <i>timestring</i> matches <i>format</i> but not all characters in <i>timestring</i> were used, the conversion succeeds but also prints an error message. </p>
<p> If either of the system functions <code>strptime</code> or <code>mktime</code> is not available, status 2 is returned and an error message is printed.</dl>
<dt><code>-s</code> <i>scalar</i></p>
<dd> Assign the date string (or epoch time in seconds if <code>-r</code> is given) to <i>scalar</i> instead of printing it.</dl>
<p> Note that depending on the system&#8217;s declared integral time type, <code>strftime</code> may produce incorrect results for epoch times greater than 2147483647 which corresponds to 2038-01-19 03:14:07 +0000.</dl>
</dl>
<p> The <code>zsh/datetime</code> module makes available several parameters; all are readonly: </p>
<dl>
<dt>
<dd> <code>EPOCHREALTIME</code> A floating point value representing the number of seconds since the epoch. The notional accuracy is to nanoseconds if the <code>clock_gettime</code> call is available and to microseconds otherwise, but in practice the range of double precision floating point and shell scheduling latencies may be significant effects.</p>
<dt><code>EPOCHSECONDS</code></p>
<dd> An integer value representing the number of seconds since the epoch.</p>
<dt><code>epochtime</code></p>
<dd> An array value containing the number of seconds since the epoch in the first element and the remainder of the time since the epoch in nanoseconds in the second element. To ensure the two elements are consistent the array should be copied or otherwise referenced as a single substitution before the values are used. The following idiom may be used:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>for secs nsecs in $epochtime; do
  ...
done</code>
</pre>
</dl>
</dl>
</dl>
<h2>THE ZSH/DB/GDBM MODULE</h2>
<p> The <code>zsh/db/gdbm</code> module is used to create &quot;tied&quot; associative arrays that interface to database files. If the GDBM interface is not available, the builtins defined by this module will report an error. This module is also intended as a prototype for creating additional database interfaces, so the <code>ztie</code> builtin may move to a more generic module in the future. </p>
<p> The builtins in this module are: </p>
<dl>
<dt>
<dd> <code>ztie -d db/gdbm -f</code> <i>filename</i> [ <code>-r</code> ] <i>arrayname</i> Open the GDBM database identified by <i>filename</i> and, if successful, create the associative array <i>arrayname</i> linked to the file. To create a local tied array, the parameter must first be declared, so commands similar to the following would be executed inside a function scope:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>local -A sampledb
ztie -d db/gdbm -f sample.gdbm sampledb</code>
</pre>
</dl>
<p> The <code>-r</code> option opens the database file for reading only, creating a parameter with the readonly attribute. Without this option, using `<code>ztie</code>&#8216; on a file for which the user does not have write permission is an error. If writable, the database is opened synchronously so fields changed in <i>arrayname</i> are immediately written to <i>filename</i>. </p>
<p> Changes to the file modes <i>filename</i> after it has been opened do not alter the state of <i>arrayname</i>, but `<code>typeset -r</code> <i>arrayname</i>&#8216; works as expected.</dl>
<dt><code>zuntie</code> [ <code>-u</code> ] <i>arrayname</i> &#8230;</p>
<dd> Close the GDBM database associated with each <i>arrayname</i> and then unset the parameter. The <code>-u</code> option forces an unset of parameters made readonly with `<code>ztie -r</code>&#8216;.</p>
<dl>
<dt>
<dd>
<p> This happens automatically if the parameter is explicitly unset or its local scope (function) ends. Note that a readonly parameter may not be explicitly unset, so the only way to unset a global parameter created with `<code>ztie -r</code>&#8216; is to use `<code>zuntie -u</code>&#8216;.</dl>
<dt><code>zgdbmpath</code> <i>parametername</i></p>
<dd> Put path to database file assigned to <i>parametername</i> into <code>REPLY</code> scalar.</p>
<dt><code>zgdbm_tied</code></p>
<dd> Array holding names of all tied parameters.</dl>
<p> The fields of an associative array tied to GDBM are neither cached nor otherwise stored in memory, they are read from or written to the database on each reference. Thus, for example, the values in a readonly array may be changed by a second writer of the same database file.</p>
<h2>THE ZSH/DELTOCHAR MODULE</h2>
<p> The <code>zsh/deltochar</code> module makes available two ZLE functions: </p>
<dl>
<dt>
<dd> <code>delete-to-char</code> Read a character from the keyboard, and delete from the cursor position up to and including the next (or, with repeat count <i>n</i>, the <i>n</i>th) instance of that character. Negative repeat counts mean delete backwards.</p>
<dt><code>zap-to-char</code></p>
<dd> This behaves like <code>delete-to-char</code>, except that the final occurrence of the character itself is not deleted.</dl>
<h2>THE ZSH/EXAMPLE MODULE</h2>
<p> The <code>zsh/example</code> module makes available one builtin command: </p>
<dl>
<dt>
<dd> <code>example</code> [ <code>-flags</code> ] [ <i>args</i> &#8230; ] Displays the flags and arguments it is invoked with.</dl>
<p> The purpose of the module is to serve as an example of how to write a module.</p>
<h2>THE ZSH/FILES MODULE</h2>
<p> The <code>zsh/files</code> module makes available some common commands for file manipulation as builtins; these commands are probably not needed for many normal situations but can be useful in emergency recovery situations with constrained resources. The commands do not implement all features now required by relevant standards committees. </p>
<p> For all commands, a variant beginning <code>zf_</code> is also available and loaded automatically. Using the features capability of zmodload will let you load only those names you want. Note that it&#8217;s possible to load only the builtins with zsh-specific names using the following command: </p>
<dl>
<dt>
<dd>
<pre>
<code>zmodload -m -F zsh/files b:zf_\*</code>
</pre>
</dl>
<p> The commands loaded by default are: </p>
<dl>
<dt>
<dd> <code>chgrp</code> [ <code>-hRs</code> ] <i>group</i> <i>filename</i> &#8230; Changes group of files specified. This is equivalent to <code>chown</code> with a <i>user-spec</i> argument of `<code>:</code><i>group</i>&#8216;.</p>
<dt><code>chmod</code> [ <code>-Rs</code> ] <i>mode</i> <i>filename</i> &#8230;</p>
<dd> Changes mode of files specified.</p>
<dl>
<dt>
<dd>
<p> The specified <i>mode</i> must be in octal. </p>
<p> The <code>-R</code> option causes <code>chmod</code> to recursively descend into directories, changing the mode of all files in the directory after changing the mode of the directory itself. </p>
<p> The <code>-s</code> option is a zsh extension to <code>chmod</code> functionality. It enables paranoid behaviour, intended to avoid security problems involving a <code>chmod</code> being tricked into affecting files other than the ones intended. It will refuse to follow symbolic links, so that (for example) &#8220;<code>chmod 600 /tmp/foo/passwd</code>&#8221; can&#8217;t accidentally chmod <code>/etc/passwd</code> if <code>/tmp/foo</code> happens to be a link to <code>/etc</code>. It will also check where it is after leaving directories, so that a recursive chmod of a deep directory tree can&#8217;t end up recursively chmoding <code>/usr</code> as a result of directories being moved up the tree.</dl>
<dt><code>chown</code> [ <code>-hRs</code> ] <i>user-spec</i> <i>filename</i> &#8230;</p>
<dd> Changes ownership and group of files specified.</p>
<dl>
<dt>
<dd>
<p> The <i>user-spec</i> can be in four forms: </p>
<dl>
<dt><i>user</i></p>
<dd> change owner to <i>user</i>; do not change group</p>
<dt><i>user</i><code>::</code></p>
<dd> change owner to <i>user</i>; do not change group</p>
<dt><i>user</i><code>:</code></p>
<dd> change owner to <i>user</i>; change group to <i>user</i>&#8216;s primary group</p>
<dt><i>user</i><code>:</code><i>group</i></p>
<dd> change owner to <i>user</i>; change group to <i>group</i></p>
<dt><code>:</code><i>group</i></p>
<dd> do not change owner; change group to <i>group</i></dl>
<p> In each case, the `<code>:</code>&#8216; may instead be a `<code>.</code>&#8216;. The rule is that if there is a `<code>:</code>&#8216; then the separator is `<code>:</code>&#8216;, otherwise if there is a `<code>.</code>&#8216; then the separator is `<code>.</code>&#8216;, otherwise there is no separator. </p>
<p> Each of <i>user</i> and <i>group</i> may be either a username (or group name, as appropriate) or a decimal user ID (group ID). Interpretation as a name takes precedence, if there is an all-numeric username (or group name). </p>
<p> If the target is a symbolic link, the <code>-h</code> option causes <code>chown</code> to set the ownership of the link instead of its target. </p>
<p> The <code>-R</code> option causes <code>chown</code> to recursively descend into directories, changing the ownership of all files in the directory after changing the ownership of the directory itself. </p>
<p> The <code>-s</code> option is a zsh extension to <code>chown</code> functionality. It enables paranoid behaviour, intended to avoid security problems involving a <code>chown</code> being tricked into affecting files other than the ones intended. It will refuse to follow symbolic links, so that (for example) &#8220;<code>chown luser /tmp/foo/passwd</code>&#8221; can&#8217;t accidentally chown <code>/etc/passwd</code> if <code>/tmp/foo</code> happens to be a link to <code>/etc</code>. It will also check where it is after leaving directories, so that a recursive chown of a deep directory tree can&#8217;t end up recursively chowning <code>/usr</code> as a result of directories being moved up the tree.</dl>
<dt>
<dd> <code>ln</code> [ <code>-dfhins</code> ] <i>filename</i> <i>dest</i></p>
<dt>
<dd> <code>ln</code> [ <code>-dfhins</code> ] <i>filename</i> &#8230; <i>dir</i> Creates hard (or, with <code>-s</code>, symbolic) links. In the first form, the specified <i>dest</i>ination is created, as a link to the specified <i>filename</i>. In the second form, each of the <i>filename</i>s is taken in turn, and linked to a pathname in the specified <i>dir</i>ectory that has the same last pathname component.</p>
<dl>
<dt>
<dd>
<p> Normally, <code>ln</code> will not attempt to create hard links to directories. This check can be overridden using the <code>-d</code> option. Typically only the super-user can actually succeed in creating hard links to directories. This does not apply to symbolic links in any case. </p>
<p> By default, existing files cannot be replaced by links. The <code>-i</code> option causes the user to be queried about replacing existing files. The <code>-f</code> option causes existing files to be silently deleted, without querying. <code>-f</code> takes precedence. </p>
<p> The <code>-h</code> and <code>-n</code> options are identical and both exist for compatibility; either one indicates that if the target is a symlink then it should not be dereferenced. Typically this is used in combination with <code>-sf</code> so that if an existing link points to a directory then it will be removed, instead of followed. If this option is used with multiple filenames and the target is a symbolic link pointing to a directory then the result is an error.</dl>
<dt><code>mkdir</code> [ <code>-p</code> ] [ <code>-m</code> <i>mode</i> ] <i>dir</i> &#8230;</p>
<dd> Creates directories. With the <code>-p</code> option, non-existing parent directories are first created if necessary, and there will be no complaint if the directory already exists. The <code>-m</code> option can be used to specify (in octal) a set of file permissions for the created directories, otherwise mode 777 modified by the current <code>umask</code> (see <i><a href="/docs/linux/man/2-umask/">umask</a></i>(2)) is used.</p>
<dt>
<dd> <code>mv</code> [ <code>-fi</code> ] <i>filename</i> <i>dest</i></p>
<dt>
<dd> <code>mv</code> [ <code>-fi</code> ] <i>filename</i> &#8230; <i>dir</i> Moves files. In the first form, the specified <i>filename</i> is moved to the specified <i>dest</i>ination. In the second form, each of the <i>filename</i>s is taken in turn, and moved to a pathname in the specified <i>dir</i>ectory that has the same last pathname component.</p>
<dl>
<dt>
<dd>
<p> By default, the user will be queried before replacing any file that the user cannot write to, but writable files will be silently removed. The <code>-i</code> option causes the user to be queried about replacing any existing files. The <code>-f</code> option causes any existing files to be silently deleted, without querying. <code>-f</code> takes precedence. </p>
<p> Note that this <code>mv</code> will not move files across devices. Historical versions of <code>mv</code>, when actual renaming is impossible, fall back on copying and removing files; if this behaviour is desired, use <code>cp</code> and <code>rm</code> manually. This may change in a future version.</dl>
<dt><code>rm</code> [ <code>-dfiRrs</code> ] <i>filename</i> &#8230;</p>
<dd> Removes files and directories specified.</p>
<dl>
<dt>
<dd>
<p> Normally, <code>rm</code> will not remove directories (except with the <code>-R</code> or <code>-r</code> options). The <code>-d</code> option causes <code>rm</code> to try removing directories with <code>unlink</code> (see <i><a href="/docs/linux/man/2-unlink/">unlink</a></i>(2)), the same method used for files. Typically only the super-user can actually succeed in unlinking directories in this way. <code>-d</code> takes precedence over <code>-R</code> and <code>-r</code>. </p>
<p> By default, the user will be queried before removing any file that the user cannot write to, but writable files will be silently removed. The <code>-i</code> option causes the user to be queried about removing any files. The <code>-f</code> option causes files to be silently deleted, without querying, and suppresses all error indications. <code>-f</code> takes precedence. </p>
<p> The <code>-R</code> and <code>-r</code> options cause <code>rm</code> to recursively descend into directories, deleting all files in the directory before removing the directory with the <code>rmdir</code> system call (see <i><a href="/docs/linux/man/2-rmdir/">rmdir</a></i>(2)). </p>
<p> The <code>-s</code> option is a zsh extension to <code>rm</code> functionality. It enables paranoid behaviour, intended to avoid common security problems involving a root-run <code>rm</code> being tricked into removing files other than the ones intended. It will refuse to follow symbolic links, so that (for example) &#8220;<code>rm /tmp/foo/passwd</code>&#8221; can&#8217;t accidentally remove <code>/etc/passwd</code> if <code>/tmp/foo</code> happens to be a link to <code>/etc</code>. It will also check where it is after leaving directories, so that a recursive removal of a deep directory tree can&#8217;t end up recursively removing <code>/usr</code> as a result of directories being moved up the tree.</dl>
<dt><code>rmdir</code> <i>dir</i> &#8230;</p>
<dd> Removes empty directories specified.</p>
<dt><code>sync</code></p>
<dd> Calls the system call of the same name (see <i><a href="/docs/linux/man/2-sync/">sync</a></i>(2)), which flushes dirty buffers to disk. It might return before the I/O has actually been completed.</dl>
<h2>THE ZSH/LANGINFO MODULE</h2>
<p> The <code>zsh/langinfo</code> module makes available one parameter: </p>
<dl>
<dt>
<dd> <code>langinfo</code> An associative array that maps langinfo elements to their values.</p>
<dl>
<dt>
<dd>
<p> Your implementation may support a number of the following keys: </p>
<p> <code>CODESET</code>, <code>D_T_FMT</code>, <code>D_FMT</code>, <code>T_FMT</code>, <code>RADIXCHAR</code>, <code>THOUSEP</code>, <code>YESEXPR</code>, <code>NOEXPR</code>, <code>CRNCYSTR</code>, <code>ABDAY_{1..7}</code>, <code>DAY_{1..7}</code>, <code>ABMON_{1..12}</code>, <code>MON_{1..12}</code>, <code>T_FMT_AMPM</code>, <code>AM_STR</code>, <code>PM_STR</code>, <code>ERA</code>, <code>ERA_D_FMT</code>, <code>ERA_D_T_FMT</code>, <code>ERA_T_FMT</code>, <code>ALT_DIGITS</code> </p>
</dl>
</dl>
<h2>THE ZSH/MAPFILE MODULE</h2>
<p> The <code>zsh/mapfile</code> module provides one special associative array parameter of the same name. </p>
<dl>
<dt>
<dd> <code>mapfile</code> This associative array takes as keys the names of files; the resulting value is the content of the file. The value is treated identically to any other text coming from a parameter. The value may also be assigned to, in which case the file in question is written (whether or not it originally existed); or an element may be unset, which will delete the file in question. For example, `<code>vared mapfile[myfile]</code>&#8216; works as expected, editing the file `<code>myfile</code>&#8216;.</p>
<dl>
<dt>
<dd>
<p> When the array is accessed as a whole, the keys are the names of files in the current directory, and the values are empty (to save a huge overhead in memory). Thus <code>${(k)mapfile}</code> has the same effect as the glob operator <code>*(D)</code>, since files beginning with a dot are not special. Care must be taken with expressions such as <code>rm ${(k)mapfile}</code>, which will delete every file in the current directory without the usual `<code>rm *</code>&#8216; test. </p>
<p> The parameter <code>mapfile</code> may be made read-only; in that case, files referenced may not be written or deleted. </p>
<p> A file may conveniently be read into an array as one line per element with the form `<i>array</i><code>=(&quot;${(f@)mapfile[</code><i>filename</i><code>]}&quot;)</code>&#8216;. The double quotes and the `<code>@</code>&#8216; are necessary to prevent empty lines from being removed. Note that if the file ends with a newline, the shell will split on the final newline, generating an additional empty field; this can be suppressed by using `<i>array</i><code>=(&quot;${(f@)${mapfile[</code><i>filename</i><code>]%$&#8217;
&#8217;}}&quot;)</code>&#8216;.</dl>
</dl>
<h3>Limitations</h3>
<p> Although reading and writing of the file in question is efficiently handled, zsh&#8217;s internal memory management may be arbitrarily baroque; however, <code>mapfile</code> is usually very much more efficient than anything involving a loop. Note in particular that the whole contents of the file will always reside physically in memory when accessed (possibly multiple times, due to standard parameter substitution operations). In particular, this means handling of sufficiently long files (greater than the machine&#8217;s swap space, or than the range of the pointer type) will be incorrect. </p>
<p> No errors are printed or flagged for non-existent, unreadable, or unwritable files, as the parameter mechanism is too low in the shell execution hierarchy to make this convenient. </p>
<p> It is unfortunate that the mechanism for loading modules does not yet allow the user to specify the name of the shell parameter to be given the special behaviour.</p>
<h2>THE ZSH/MATHFUNC MODULE</h2>
<p> The <code>zsh/mathfunc</code> module provides standard mathematical functions for use when evaluating mathematical formulae. The syntax agrees with normal C and FORTRAN conventions, for example, </p>
<dl>
<dt>
<dd>
<pre>
<code>(( f = sin(0.3) ))</code>
</pre>
</dl>
<p> assigns the sine of 0.3 to the parameter f. </p>
<p> Most functions take floating point arguments and return a floating point value. However, any necessary conversions from or to integer type will be performed automatically by the shell. Apart from <code>atan</code> with a second argument and the <code>abs</code>, <code>int</code> and <code>float</code> functions, all functions behave as noted in the manual page for the corresponding C function, except that any arguments out of range for the function in question will be detected by the shell and an error reported. </p>
<p> The following functions take a single floating point argument: <code>acos</code>, <code>acosh</code>, <code>asin</code>, <code>asinh</code>, <code>atan</code>, <code>atanh</code>, <code>cbrt</code>, <code>ceil</code>, <code>cos</code>, <code>cosh</code>, <code>erf</code>, <code>erfc</code>, <code>exp</code>, <code>expm1</code>, <code>fabs</code>, <code>floor</code>, <code>gamma</code>, <code>j0</code>, <code>j1</code>, <code>lgamma</code>, <code>log</code>, <code>log10</code>, <code>log1p</code>, <code>log2</code>, <code>logb</code>, <code>sin</code>, <code>sinh</code>, <code>sqrt</code>, <code>tan</code>, <code>tanh</code>, <code>y0</code>, <code>y1</code>. The <code>atan</code> function can optionally take a second argument, in which case it behaves like the C function <code>atan2</code>. The <code>ilogb</code> function takes a single floating point argument, but returns an integer. </p>
<p> The function <code>signgam</code> takes no arguments, and returns an integer, which is the C variable of the same name, as described in <i><a href="/docs/linux/man/3-gamma/">gamma</a></i>(3). Note that it is therefore only useful immediately after a call to <code>gamma</code> or <code>lgamma</code>. Note also that `<code>signgam()</code>&#8216; and `<code>signgam</code>&#8216; are distinct expressions. </p>
<p> The functions <code>min</code>, <code>max</code>, and <code>sum</code> are defined not in this module but in the <code>zmathfunc</code> autoloadable function, described in the section `Mathematical Functions&#8217; in <i><a href="/docs/linux/man/1-zshcontrib/">zshcontrib</a></i>(1). </p>
<p> The following functions take two floating point arguments: <code>copysign</code>, <code>fmod</code>, <code>hypot</code>, <code>nextafter</code>. </p>
<p> The following take an integer first argument and a floating point second argument: <code>jn</code>, <code>yn</code>. </p>
<p> The following take a floating point first argument and an integer second argument: <code>ldexp</code>, <code>scalb</code>. </p>
<p> The function <code>abs</code> does not convert the type of its single argument; it returns the absolute value of either a floating point number or an integer. The functions <code>float</code> and <code>int</code> convert their arguments into a floating point or integer value (by truncation) respectively. </p>
<p> Note that the C <code>pow</code> function is available in ordinary math evaluation as the `<code>**</code>&#8216; operator and is not provided here. </p>
<p> The function <code>rand48</code> is available if your system&#8217;s mathematical library has the function <code><a href="/docs/linux/man/3-erand48/">erand48</a>(3)</code>. It returns a pseudo-random floating point number between 0 and 1. It takes a single string optional argument. </p>
<p> If the argument is not present, the random number seed is initialised by three calls to the <code><a href="/docs/linux/man/3-rand/">rand</a>(3)</code> function &#8212; this produces the same random numbers as the next three values of <code>$RANDOM</code>. </p>
<p> If the argument is present, it gives the name of a scalar parameter where the current random number seed will be stored. On the first call, the value must contain at least twelve hexadecimal digits (the remainder of the string is ignored), or the seed will be initialised in the same manner as for a call to <code>rand48</code> with no argument. Subsequent calls to <code>rand48</code>(<i>param</i>) will then maintain the seed in the parameter <i>param</i> as a string of twelve hexadecimal digits, with no base signifier. The random number sequences for different parameters are completely independent, and are also independent from that used by calls to <code>rand48</code> with no argument. </p>
<p> For example, consider </p>
<dl>
<dt>
<dd>
<pre>
<code>print $(( rand48(seed) ))
print $(( rand48() ))
print $(( rand48(seed) ))</code>
</pre>
</dl>
<p> Assuming <code>$seed</code> does not exist, it will be initialised by the first call. In the second call, the default seed is initialised; note, however, that because of the properties of <code>rand()</code> there is a correlation between the seeds used for the two initialisations, so for more secure uses, you should generate your own 12-byte seed. The third call returns to the same sequence of random numbers used in the first call, unaffected by the intervening <code>rand48()</code>.</p>
<h2>THE ZSH/NEARCOLOR MODULE</h2>
<p> The <code>zsh/nearcolor</code> module replaces colours specified as hex triplets with the nearest colour in the 88 or 256 colour palettes that are widely used by terminal emulators. By default, 24-bit true colour escape codes are generated when colours are specified using hex triplets. These are not supported by all terminals. The purpose of this module is to make it easier to define colour preferences in a form that can work across a range of terminal emulators. </p>
<p> Aside from the default colour, the ANSI standard for terminal escape codes provides for eight colours. The bright attribute brings this to sixteen. These basic colours are commonly used in terminal applications due to being widely supported. Expanded 88 and 256 colour palettes are also common and, while the first sixteen colours vary somewhat between terminals and configurations, these add a generally consistent and predictable set of colours. </p>
<p> In order to use the <code>zsh/nearcolor</code> module, it only needs to be loaded. Thereafter, whenever a colour is specified using a hex triplet, it will be compared against each of the available colours and the closest will be selected. The first sixteen colours are never matched in this process due to being unpredictable. </p>
<p> It isn&#8217;t possible to reliably detect support for true colour in the terminal emulator. It is therefore recommended to be selective in loading the <code>zsh/nearcolor</code> module. For example, the following checks the <code>COLORTERM</code> environment variable: </p>
<dl>
<dt>
<dd>
[[$COLORTERM = *(24bit | truecolor) * ]] || zmodload zsh / nearcolor
</dl>
<p> Note that some terminals accept the true color escape codes but map them internally to a more limited palette in a similar manner to the <code>zsh/nearcolor</code> module.</p>
<h2>THE ZSH/NEWUSER MODULE</h2>
<p> The <code>zsh/newuser</code> module is loaded at boot if it is available, the <code>RCS</code> option is set, and the <code>PRIVILEGED</code> option is not set (all three are true by default). This takes place immediately after commands in the global <code>zshenv</code> file (typically <code>/etc/zsh/zshenv</code>), if any, have been executed. If the module is not available it is silently ignored by the shell; the module may safely be removed from <code>$MODULE_PATH</code> by the administrator if it is not required. </p>
<p> On loading, the module tests if any of the start-up files <code>.zshenv</code>, <code>.zprofile</code>, <code>.zshrc</code> or <code>.zlogin</code> exist in the directory given by the environment variable <code>ZDOTDIR</code>, or the user&#8217;s home directory if that is not set. The test is not performed and the module halts processing if the shell was in an emulation mode (i.e. had been invoked as some other shell than zsh). </p>
<p> If none of the start-up files were found, the module then looks for the file <code>newuser</code> first in a sitewide directory, usually the parent directory of the <code>site-functions</code> directory, and if that is not found the module searches in a version-specific directory, usually the parent of the <code>functions</code> directory containing version-specific functions. (These directories can be configured when zsh is built using the <code>&#8211;enable-site-scriptdir=</code><i>dir</i> and <code>&#8211;enable-scriptdir=</code><i>dir</i> flags to <code>configure</code>, respectively; the defaults are <i>prefix</i><code>/share/zsh</code> and <i>prefix</i><code>/share/zsh/$ZSH_VERSION</code> where the default <i>prefix</i> is <code>/usr/local</code>.) </p>
<p> If the file <code>newuser</code> is found, it is then sourced in the same manner as a start-up file. The file is expected to contain code to install start-up files for the user, however any valid shell code will be executed. </p>
<p> The <code>zsh/newuser</code> module is then unconditionally unloaded. </p>
<p> Note that it is possible to achieve exactly the same effect as the <code>zsh/newuser</code> module by adding code to <code>/etc/zsh/zshenv</code>. The module exists simply to allow the shell to make arrangements for new users without the need for intervention by package maintainers and system administrators. </p>
<p> The script supplied with the module invokes the shell function <code>zsh-newuser-install</code>. This may be invoked directly by the user even if the <code>zsh/newuser</code> module is disabled. Note, however, that if the module is not installed the function will not be installed either. The function is documented in the section User Configuration Functions in <i><a href="/docs/linux/man/1-zshcontrib/">zshcontrib</a></i>(1).</p>
<h2>THE ZSH/PARAMETER MODULE</h2>
<p> The <code>zsh/parameter</code> module gives access to some of the internal hash tables used by the shell by defining some special parameters. </p>
<dl>
<dt>
<dd> <code>options</code> The keys for this associative array are the names of the options that can be set and unset using the <code>setopt</code> and <code>unsetopt</code> builtins. The value of each key is either the string <code>on</code> if the option is currently set, or the string <code>off</code> if the option is unset. Setting a key to one of these strings is like setting or unsetting the option, respectively. Unsetting a key in this array is like setting it to the value <code>off</code>.</p>
<dt><code>commands</code></p>
<dd> This array gives access to the command hash table. The keys are the names of external commands, the values are the pathnames of the files that would be executed when the command would be invoked. Setting a key in this array defines a new entry in this table in the same way as with the <code>hash</code> builtin. Unsetting a key as in `<code>unset &quot;commands[foo]&quot;</code>&#8216; removes the entry for the given key from the command hash table.</p>
<dt><code>functions</code></p>
<dd> This associative array maps names of enabled functions to their definitions. Setting a key in it is like defining a function with the name given by the key and the body given by the value. Unsetting a key removes the definition for the function named by the key.</p>
<dt><code>dis_functions</code></p>
<dd> Like <code>functions</code> but for disabled functions.</p>
<dt><code>functions_source</code></p>
<dd> This readonly associative array maps names of enabled functions to the name of the file containing the source of the function.</p>
<dl>
<dt>
<dd>
<p> For an autoloaded function that has already been loaded, or marked for autoload with an absolute path, or that has had its path resolved with `<code>functions -r</code>&#8216;, this is the file found for autoloading, resolved to an absolute path. </p>
<p> For a function defined within the body of a script or sourced file, this is the name of that file. In this case, this is the exact path originally used to that file, which may be a relative path. </p>
<p> For any other function, including any defined at an interactive prompt or an autoload function whose path has not yet been resolved, this is the empty string. However, the hash element is reported as defined just so long as the function is present: the keys to this hash are the same as those to <code>$functions</code>.</dl>
<dt><code>dis_functions_source</code></p>
<dd> Like <code>functions_source</code> but for disabled functions.</p>
<dt><code>builtins</code></p>
<dd> This associative array gives information about the builtin commands currently enabled. The keys are the names of the builtin commands and the values are either `<code>undefined</code>&#8216; for builtin commands that will automatically be loaded from a module if invoked or `<code>defined</code>&#8216; for builtin commands that are already loaded.</p>
<dt><code>dis_builtins</code></p>
<dd> Like <code>builtins</code> but for disabled builtin commands.</p>
<dt><code>reswords</code></p>
<dd> This array contains the enabled reserved words.</p>
<dt><code>dis_reswords</code></p>
<dd> Like <code>reswords</code> but for disabled reserved words.</p>
<dt><code>patchars</code></p>
<dd> This array contains the enabled pattern characters.</p>
<dt><code>dis_patchars</code></p>
<dd> Like <code>patchars</code> but for disabled pattern characters.</p>
<dt><code>aliases</code></p>
<dd> This maps the names of the regular aliases currently enabled to their expansions.</p>
<dt><code>dis_aliases</code></p>
<dd> Like <code>aliases</code> but for disabled regular aliases.</p>
<dt><code>galiases</code></p>
<dd> Like <code>aliases</code>, but for global aliases.</p>
<dt><code>dis_galiases</code></p>
<dd> Like <code>galiases</code> but for disabled global aliases.</p>
<dt><code>saliases</code></p>
<dd> Like <code>raliases</code>, but for suffix aliases.</p>
<dt><code>dis_saliases</code></p>
<dd> Like <code>saliases</code> but for disabled suffix aliases.</p>
<dt><code>parameters</code></p>
<dd> The keys in this associative array are the names of the parameters currently defined. The values are strings describing the type of the parameter, in the same format used by the <code>t</code> parameter flag, see <i><a href="/docs/linux/man/1-zshexpn/">zshexpn</a></i>(1) . Setting or unsetting keys in this array is not possible.</p>
<dt><code>modules</code></p>
<dd> An associative array giving information about modules. The keys are the names of the modules loaded, registered to be autoloaded, or aliased. The value says which state the named module is in and is one of the strings `<code>loaded</code>&#8216;, `<code>autoloaded</code>&#8216;, or `<code>alias:</code><i>name</i>&#8216;, where <i>name</i> is the name the module is aliased to.</p>
<dl>
<dt>
<dd>
<p> Setting or unsetting keys in this array is not possible.</dl>
<dt><code>dirstack</code></p>
<dd> A normal array holding the elements of the directory stack. Note that the output of the <code>dirs</code> builtin command includes one more directory, the current working directory.</p>
<dt><code>history</code></p>
<dd> This associative array maps history event numbers to the full history lines. Although it is presented as an associative array, the array of all values (<code>${history[@]}</code>) is guaranteed to be returned in order from most recent to oldest history event, that is, by decreasing history event number.</p>
<dt><code>historywords</code></p>
<dd> A special array containing the words stored in the history. These also appear in most to least recent order.</p>
<dt><code>jobdirs</code></p>
<dd> This associative array maps job numbers to the directories from which the job was started (which may not be the current directory of the job).</p>
<dl>
<dt>
<dd>
<p> The keys of the associative arrays are usually valid job numbers, and these are the values output with, for example, <code>${(k)jobdirs}</code>. Non-numeric job references may be used when looking up a value; for example, <code>${jobdirs[%+]}</code> refers to the current job.</dl>
<dt><code>jobtexts</code></p>
<dd> This associative array maps job numbers to the texts of the command lines that were used to start the jobs.</p>
<dl>
<dt>
<dd>
<p> Handling of the keys of the associative array is as described for <code>jobdirs</code> above.</dl>
<dt><code>jobstates</code></p>
<dd> This associative array gives information about the states of the jobs currently known. The keys are the job numbers and the values are strings of the form `<i>job-state</i><code>:</code><i>mark</i><code>:</code><i>pid</i><code>=</code><i>state</i>&#8230;&#8217;. The <i>job-state</i> gives the state the whole job is currently in, one of `<code>running</code>&#8216;, `<code>suspended</code>&#8216;, or `<code>done</code>&#8216;. The <i>mark</i> is `<code>+</code>&#8216; for the current job, `<code>&#8211;</code>&#8216; for the previous job and empty otherwise. This is followed by one `<code>:</code><i>pid</i><code>=</code><i>state</i>&#8216; for every process in the job. The <i>pid</i>s are, of course, the process IDs and the <i>state</i> describes the state of that process.</p>
<dl>
<dt>
<dd>
<p> Handling of the keys of the associative array is as described for <code>jobdirs</code> above.</dl>
<dt><code>nameddirs</code></p>
<dd> This associative array maps the names of named directories to the pathnames they stand for.</p>
<dt><code>userdirs</code></p>
<dd> This associative array maps user names to the pathnames of their home directories.</p>
<dt><code>usergroups</code></p>
<dd> This associative array maps names of system groups of which the current user is a member to the corresponding group identifiers. The contents are the same as the groups output by the <code>id</code> command.</p>
<dt><code>funcfiletrace</code></p>
<dd> This array contains the absolute line numbers and corresponding file names for the point where the current function, sourced file, or (if <code>EVAL_LINENO</code> is set) <code>eval</code> command was called. The array is of the same length as <code>funcsourcetrace</code> and <code>functrace</code>, but differs from <code>funcsourcetrace</code> in that the line and file are the point of call, not the point of definition, and differs from <code>functrace</code> in that all values are absolute line numbers in files, rather than relative to the start of a function, if any.</p>
<dt><code>funcsourcetrace</code></p>
<dd> This array contains the file names and line numbers of the points where the functions, sourced files, and (if <code>EVAL_LINENO</code> is set) <code>eval</code> commands currently being executed were defined. The line number is the line where the `<code>function</code> <i>name</i>&#8216; or `<i>name</i> <code>()</code>&#8216; started. In the case of an autoloaded function the line number is reported as zero. The format of each element is <i>filename</i><code>:</code><i>lineno</i>.</p>
<dl>
<dt>
<dd>
<p> For functions autoloaded from a file in native zsh format, where only the body of the function occurs in the file, or for files that have been executed by the <code>source</code> or `<code>.</code>&#8216; builtins, the trace information is shown as <i>filename</i><code>:</code><i>0</i>, since the entire file is the definition. The source file name is resolved to an absolute path when the function is loaded or the path to it otherwise resolved. </p>
<p> Most users will be interested in the information in the <code>funcfiletrace</code> array instead.</dl>
<dt><code>funcstack</code></p>
<dd> This array contains the names of the functions, sourced files, and (if <code>EVAL_LINENO</code> is set) <code>eval</code> commands. currently being executed. The first element is the name of the function using the parameter.</p>
<dl>
<dt>
<dd>
<p> The standard shell array <code>zsh_eval_context</code> can be used to determine the type of shell construct being executed at each depth: note, however, that is in the opposite order, with the most recent item last, and it is more detailed, for example including an entry for <code>toplevel</code>, the main shell code being executed either interactively or from a script, which is not present in <code>$funcstack</code>.</dl>
<dt><code>functrace</code></p>
<dd> This array contains the names and line numbers of the callers corresponding to the functions currently being executed. The format of each element is <i>name</i><code>:</code><i>lineno</i>. Callers are also shown for sourced files; the caller is the point where the <code>source</code> or `<code>.</code>&#8216; command was executed.</dl>
<h2>THE ZSH/PCRE MODULE</h2>
<p> The <code>zsh/pcre</code> module makes some commands available as builtins: </p>
<dl>
<dt>
<dd> <code>pcre_compile</code> [ <code>-aimxs</code> ] <i>PCRE</i> Compiles a perl-compatible regular expression.</p>
<dl>
<dt>
<dd>
<p> Option <code>-a</code> will force the pattern to be anchored. Option <code>-i</code> will compile a case-insensitive pattern. Option <code>-m</code> will compile a multi-line pattern; that is, <code>^</code> and <code>$</code> will match newlines within the pattern. Option <code>-x</code> will compile an extended pattern, wherein whitespace and <code>#</code> comments are ignored. Option <code>-s</code> makes the dot metacharacter match all characters, including those that indicate newline.</dl>
<dt><code>pcre_study</code></p>
<dd> Studies the previously-compiled PCRE which may result in faster matching.</p>
<dt><code>pcre_match</code> [ <code>-v</code> <i>var</i> ] [ <code>-a</code> <i>arr</i> ] [ <code>-n</code> <i>offset</i> ] [ <code>-b</code> ] <i>string</i></p>
<dd> Returns successfully if <code>string</code> matches the previously-compiled PCRE.</p>
<dl>
<dt>
<dd>
<p> Upon successful match, if the expression captures substrings within parentheses, <code>pcre_match</code> will set the array <code>match</code> to those substrings, unless the <code>-a</code> option is given, in which case it will set the array <i>arr</i>. Similarly, the variable <code>MATCH</code> will be set to the entire matched portion of the string, unless the <code>-v</code> option is given, in which case the variable <i>var</i> will be set. No variables are altered if there is no successful match. A <code>-n</code> option starts searching for a match from the byte <i>offset</i> position in <i>string</i>. If the <code>-b</code> option is given, the variable <code>ZPCRE_OP</code> will be set to an offset pair string, representing the byte offset positions of the entire matched portion within the <i>string</i>. For example, a <code>ZPCRE_OP</code> set to &quot;32 45&quot; indicates that the matched portion began on byte offset 32 and ended on byte offset 44. Here, byte offset position 45 is the position directly after the matched portion. Keep in mind that the byte position isn&#8217;t necessarily the same as the character position when UTF-8 characters are involved. Consequently, the byte offset positions are only to be relied on in the context of using them for subsequent searches on <i>string</i>, using an offset position as an argument to the <code>-n</code> option. This is mostly used to implement the &quot;find all non-overlapping matches&quot; functionality. </p>
<p> A simple example of &quot;find all non-overlapping matches&quot;: </p>
<dl>
<dt>
<dd>
string=&#8221;The following zip codes: 78884 90210 99513&#8243;<br />
pcre_compile -m &#8220;\d{5}&#8221;<br />
accum=()<br />
pcre_match -b &#8212; $string<br />
while [[ $? -eq 0 ]] do<br />
    b=($=ZPCRE_OP)<br />
    accum+=$MATCH<br />
    pcre_match -b -n $b[2] &#8212; $string<br />
done<br />
print -l $accum
</dl>
</dl>
</dl>
<p> The <code>zsh/pcre</code> module makes available the following test condition: </p>
<dl>
<dt>
<dd> <i>expr</i> <code>-pcre-match</code> <i>pcre</i> Matches a string against a perl-compatible regular expression.</p>
<dl>
<dt>
<dd>
<p> For example, </p>
<dl>
<dt>
<dd>
[[&#8220;$text&#8221; &#8211; pcre &#8211; match ^ d + $]] &amp;&amp;<br />
    print text variable contains only &#8220;d&#8217;s&#8221;.
</dl>
<p> If the <code>REMATCH_PCRE</code> option is set, the <code>=~</code> operator is equivalent to <code>-pcre-match</code>, and the <code>NO_CASE_MATCH</code> option may be used. Note that <code>NO_CASE_MATCH</code> never applies to the <code>pcre_match</code> builtin, instead use the <code>-i</code> switch of <code>pcre_compile</code>.</dl>
</dl>
<h2>THE ZSH/PARAM/PRIVATE MODULE</h2>
<p> The <code>zsh/param/private</code> module is used to create parameters whose scope is limited to the current function body, and <i>not</i> to other functions called by the current function. </p>
<p> This module provides a single autoloaded builtin: </p>
<dl>
<dt>
<dd> <code>private</code> [ {<code>+</code>|<code>&#8211;</code>}<code>AHUahlprtux</code> ] [ {<code>+</code>|<code>&#8211;</code>}<code>EFLRZi</code> [ <i>n</i> ] ] [ <i>name</i>[<code>=</code><i>value</i>] &#8230; ] The <code>private</code> builtin accepts all the same options and arguments as <code>local</code> (<i><a href="/docs/linux/man/1-zshbuiltins/">zshbuiltins</a></i>(1)) except for the `<code>&#8211;</code><code>T</code>&#8216; option. Tied parameters may not be made private.</p>
<dl>
<dt>
<dd>
<p> If used at the top level (outside a function scope), <code>private</code> creates a normal parameter in the same manner as <code>declare</code> or <code>typeset</code>. A warning about this is printed if <code>WARN_CREATE_GLOBAL</code> is set (<i><a href="/docs/linux/man/1-zshoptions/">zshoptions</a></i>(1)). Used inside a function scope, <code>private</code> creates a local parameter similar to one declared with <code>local</code>, except having special properties noted below. </p>
<p> Special parameters which expose or manipulate internal shell state, such as <code>ARGC</code>, <code>argv</code>, <code>COLUMNS</code>, <code>LINES</code>, <code>UID</code>, <code>EUID</code>, <code>IFS</code>, <code>PROMPT</code>, <code>RANDOM</code>, <code>SECONDS</code>, etc., cannot be made private unless the `<code>&#8211;</code><code>h</code>&#8216; option is used to hide the special meaning of the parameter. This may change in the future.</dl>
</dl>
<p> As with other <code>typeset</code> equivalents, <code>private</code> is both a builtin and a reserved word, so arrays may be assigned with parenthesized word list <i>name</i><code>=(</code><i>value</i>&#8230;<code>)</code> syntax. However, the reserved word `<code>private</code>&#8216; is not available until <code>zsh/param/private</code> is loaded, so care must be taken with order of execution and parsing for function definitions which use <code>private</code>. To compensate for this, the module also adds the option `<code>-P</code>&#8216; to the `<code>local</code>&#8216; builtin to declare private parameters. </p>
<p> For example, this construction fails if <code>zsh/param/private</code> has not yet been loaded when `<code>bad_declaration</code>&#8216; is defined:</p>
<dl>
<dt>
<dd>
<pre>
<code>bad_declaration() {
  zmodload zsh/param/private
  private array=( one two three )
}</code>
</pre>
</dl>
<p> This construction works because <code>local</code> is already a keyword, and the module is loaded before the statement is executed:</p>
<dl>
<dt>
<dd>
<pre>
<code>good_declaration() {
  zmodload zsh/param/private
  local -P array=( one two three )
}</code>
</pre>
</dl>
<p> The following is usable in scripts but may have trouble with <code>autoload</code>:</p>
<dl>
<dt>
<dd>
<pre>
<code>zmodload zsh/param/private
iffy_declaration() {
  private array=( one two three )
}</code>
</pre>
</dl>
<p> The <code>private</code> builtin may always be used with scalar assignments and for declarations without assignments. </p>
<p> Parameters declared with <code>private</code> have the following properties: </p>
<dl>
<dt>
<dd> &bull; Within the function body where it is declared, the parameter behaves as a local, except as noted above for tied or special parameters.</p>
<dt>&bull;</p>
<dd> The type of a parameter declared private cannot be changed in the scope where it was declared, even if the parameter is unset. Thus an array cannot be assigned to a private scalar, etc.</p>
<dt>&bull;</p>
<dd> Within any other function called by the declaring function, the private parameter does <i>NOT</i> hide other parameters of the same name, so for example a global parameter of the same name is visible and may be assigned or unset. This includes calls to anonymous functions, although that may also change in the future.</p>
<dt>&bull;</p>
<dd> An exported private remains in the environment of inner scopes but appears unset for the current shell in those scopes. Generally, exporting private parameters should be avoided.</dl>
<p> Note that this differs from the static scope defined by compiled languages derived from C, in that the a new call to the same function creates a new scope, i.e., the parameter is still associated with the call stack rather than with the function definition. It differs from ksh `<code>typeset -S</code>&#8216; because the syntax used to define the function has no bearing on whether the parameter scope is respected.</p>
<h2>THE ZSH/REGEX MODULE</h2>
<p> The <code>zsh/regex</code> module makes available the following test condition: </p>
<dl>
<dt>
<dd> <i>expr</i> <code>-regex-match</code> <i>regex</i> Matches a string against a POSIX extended regular expression. On successful match, matched portion of the string will normally be placed in the <code>MATCH</code> variable. If there are any capturing parentheses within the regex, then the <code>match</code> array variable will contain those. If the match is not successful, then the variables will not be altered.</p>
<dl>
<dt>
<dd>
<p> For example, </p>
<dl>
<dt>
<dd>
[[alphabetical &#8211; regex &#8211; match ^ a([^a] +) a([^a] +) a]] &amp;&amp;<br />
    print &#8211; l $MATCH X $match
</dl>
<p> If the option <code>REMATCH_PCRE</code> is not set, then the <code>=~</code> operator will automatically load this module as needed and will invoke the <code>-regex-match</code> operator. </p>
<p> If <code>BASH_REMATCH</code> is set, then the array <code>BASH_REMATCH</code> will be set instead of <code>MATCH</code> and <code>match</code>.</dl>
</dl>
<h2>THE ZSH/SCHED MODULE</h2>
<p> The <code>zsh/sched</code> module makes available one builtin command and one parameter. </p>
<dl>
<dt>
<dd> <code>sched</code> [<code>-o</code>] [<code>+</code>]<i>hh</i><code>:</code><i>mm</i>[<code>:</code><i>ss</i>] <i>command</i> &#8230;</p>
<dt>
<dd> <code>sched</code> [<code>-o</code>] [<code>+</code>]<i>seconds</i> <i>command</i> &#8230;</p>
<dt>
<dd> <code>sched</code> [ <code>&#8211;</code><i>item</i> ] Make an entry in the scheduled list of commands to execute. The time may be specified in either absolute or relative time, and either as hours, minutes and (optionally) seconds separated by a colon, or seconds alone. An absolute number of seconds indicates the time since the epoch (1970/01/01 00:00); this is useful in combination with the features in the <code>zsh/datetime</code> module, see the zsh/datetime module entry in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1).</p>
<dl>
<dt>
<dd>
<p> With no arguments, prints the list of scheduled commands. If the scheduled command has the <code>-o</code> flag set, this is shown at the start of the command. </p>
<p> With the argument `<code>&#8211;</code><i>item</i>&#8216;, removes the given item from the list. The numbering of the list is continuous and entries are in time order, so the numbering can change when entries are added or deleted. </p>
<p> Commands are executed either immediately before a prompt, or while the shell&#8217;s line editor is waiting for input. In the latter case it is useful to be able to produce output that does not interfere with the line being edited. Providing the option <code>-o</code> causes the shell to clear the command line before the event and redraw it afterwards. This should be used with any scheduled event that produces visible output to the terminal; it is not needed, for example, with output that updates a terminal emulator&#8217;s title bar. </p>
<p> To effect changes to the editor buffer when an event executes, use the `<code>zle</code>&#8216; command with no arguments to test whether the editor is active, and if it is, then use `<code>zle </code><i>widget</i>&#8216; to access the editor via the named <i>widget</i>. </p>
<p> The <code>sched</code> builtin is not made available by default when the shell starts in a mode emulating another shell. It can be made available with the command `<code>zmodload -F zsh/sched b:sched</code>&#8216;.</dl>
</dl>
<dl>
<dt>
<dd> <code>zsh_scheduled_events</code> A readonly array corresponding to the events scheduled by the <code>sched</code> builtin. The indices of the array correspond to the numbers shown when <code>sched</code> is run with no arguments (provided that the <code>KSH_ARRAYS</code> option is not set). The value of the array consists of the scheduled time in seconds since the epoch (see the section `The zsh/datetime Module&#8217; for facilities for using this number), followed by a colon, followed by any options (which may be empty but will be preceded by a `<code>&#8211;</code>&#8216; otherwise), followed by a colon, followed by the command to be executed.</p>
<dl>
<dt>
<dd>
<p> The <code>sched</code> builtin should be used for manipulating the events. Note that this will have an immediate effect on the contents of the array, so that indices may become invalid.</dl>
</dl>
<h2>THE ZSH/NET/SOCKET MODULE</h2>
<p> The <code>zsh/net/socket</code> module makes available one builtin command: </p>
<dl>
<dt>
<dd> <code>zsocket</code> [ <code>-altv</code> ] [ <code>-d</code> <i>fd</i> ] [ <i>args</i> ] <code>zsocket</code> is implemented as a builtin to allow full use of shell command line editing, file I/O, and job control mechanisms.</dl>
<h3>Outbound Connections</h3>
<dl>
<dt>
<dd> <code>zsocket</code> [ <code>-v</code> ] [ <code>-d</code> <i>fd</i> ] <i>filename</i> Open a new Unix domain connection to <i>filename</i>. The shell parameter <code>REPLY</code> will be set to the file descriptor associated with that connection. Currently, only stream connections are supported.</p>
<dl>
<dt>
<dd>
<p> If <code>-d</code> is specified, its argument will be taken as the target file descriptor for the connection. </p>
<p> In order to elicit more verbose output, use <code>-v</code>. </p>
<p> File descriptors can be closed with normal shell syntax when no longer needed, for example: </p>
<dl>
<dt>
<dd>
<pre>
<code>exec {REPLY}&gt;&amp;-</code>
</pre>
</dl>
</dl>
</dl>
<h3>Inbound Connections</h3>
<dl>
<dt>
<dd> <code>zsocket</code> <code>-l</code> [ <code>-v</code> ] [ <code>-d</code> <i>fd</i> ] <i>filename</i> <code>zsocket -l</code> will open a socket listening on <i>filename</i>. The shell parameter <code>REPLY</code> will be set to the file descriptor associated with that listener. The file descriptor remains open in subshells and forked external executables.</p>
<dl>
<dt>
<dd>
<p> If <code>-d</code> is specified, its argument will be taken as the target file descriptor for the connection. </p>
<p> In order to elicit more verbose output, use <code>-v</code>.</dl>
<dt><code>zsocket</code> <code>-a</code> [ <code>-tv</code> ] [ <code>-d</code> <i>targetfd</i> ] <i>listenfd</i></p>
<dd> <code>zsocket -a</code> will accept an incoming connection to the socket associated with <i>listenfd</i>. The shell parameter <code>REPLY</code> will be set to the file descriptor associated with the inbound connection. The file descriptor remains open in subshells and forked external executables.</p>
<dl>
<dt>
<dd>
<p> If <code>-d</code> is specified, its argument will be taken as the target file descriptor for the connection. </p>
<p> If <code>-t</code> is specified, <code>zsocket</code> will return if no incoming connection is pending. Otherwise it will wait for one. </p>
<p> In order to elicit more verbose output, use <code>-v</code>.</dl>
</dl>
<h2>THE ZSH/STAT MODULE</h2>
<p> The <code>zsh/stat</code> module makes available one builtin command under two possible names: </p>
<dl>
<dt>
<dd> <code>zstat </code>[ <code>-gnNolLtTrs</code> ] [ <code>-f</code> <i>fd</i> ] [ <code>-H</code> <i>hash</i> ] [ <code>-A</code> <i>array</i> ] [ <code>-F</code> <i>fmt</i> ]</p>
<dt>
<dd> [ <code>+</code><i>element</i> ] [ <i>file</i> &#8230; ]</p>
<dt>
<dd> <code>stat</code> <i>&#8230;</i> The command acts as a front end to the <code>stat</code> system call (see <i><a href="/docs/linux/man/2-stat/">stat</a></i>(2)). The same command is provided with two names; as the name <code>stat</code> is often used by an external command it is recommended that only the <code>zstat</code> form of the command is used. This can be arranged by loading the module with the command `<code>zmodload -F zsh/stat b:zstat</code>&#8216;.</p>
<dl>
<dt>
<dd>
<p> If the <code>stat</code> call fails, the appropriate system error message printed and status 1 is returned. The fields of <code>struct stat</code> give information about the files provided as arguments to the command. In addition to those available from the <code>stat</code> call, an extra element `<code>link</code>&#8216; is provided. These elements are: </p>
<dl>
<dt>
<dd> <code>device</code> The number of the device on which the file resides.</p>
<dt><code>inode</code></p>
<dd> The unique number of the file on this device (`<i>inode</i>&#8216; number).</p>
<dt><code>mode</code></p>
<dd> The mode of the file; that is, the file&#8217;s type and access permissions. With the <code>-s</code> option, this will be returned as a string corresponding to the first column in the display of the <code>ls -l</code> command.</p>
<dt><code>nlink</code></p>
<dd> The number of hard links to the file.</p>
<dt><code>uid</code></p>
<dd> The user ID of the owner of the file. With the <code>-s</code> option, this is displayed as a user name.</p>
<dt><code>gid</code></p>
<dd> The group ID of the file. With the <code>-s</code> option, this is displayed as a group name.</p>
<dt><code>rdev</code></p>
<dd> The raw device number. This is only useful for special devices.</p>
<dt><code>size</code></p>
<dd> The size of the file in bytes.</p>
<dt>
<dd> <code>atime</code></p>
<dt>
<dd> <code>mtime</code></p>
<dt>
<dd> <code>ctime</code> The last access, modification and inode change times of the file, respectively, as the number of seconds since midnight GMT on 1st January, 1970. With the <code>-s</code> option, these are printed as strings for the local time zone; the format can be altered with the <code>-F</code> option, and with the <code>-g</code> option the times are in GMT.</p>
<dt><code>blksize</code></p>
<dd> The number of bytes in one allocation block on the device on which the file resides.</p>
<dt><code>block</code></p>
<dd> The number of disk blocks used by the file.</p>
<dt><code>link</code></p>
<dd> If the file is a link and the <code>-L</code> option is in effect, this contains the name of the file linked to, otherwise it is empty. Note that if this element is selected (&#8220;<code>zstat +link</code>&#8221;) then the <code>-L</code> option is automatically used.</dl>
<p> A particular element may be selected by including its name preceded by a `<code>+</code>&#8216; in the option list; only one element is allowed. The element may be shortened to any unique set of leading characters. Otherwise, all elements will be shown for all files. </p>
<p> Options: </p>
<dl>
<dt>
<dd> <code>-A</code> <i>array</i> Instead of displaying the results on standard output, assign them to an <i>array</i>, one <code>struct stat</code> element per array element for each file in order. In this case neither the name of the element nor the name of the files appears in <i>array</i> unless the <code>-t</code> or <code>-n</code> options were given, respectively. If <code>-t</code> is given, the element name appears as a prefix to the appropriate array element; if <code>-n</code> is given, the file name appears as a separate array element preceding all the others. Other formatting options are respected.</p>
<dt><code>-H</code> <i>hash</i></p>
<dd> Similar to <code>-A</code>, but instead assign the values to <i>hash</i>. The keys are the elements listed above. If the <code>-n</code> option is provided then the name of the file is included in the hash with key <code>name</code>.</p>
<dt><code>-f</code> <i>fd</i></p>
<dd> Use the file on file descriptor <i>fd</i> instead of named files; no list of file names is allowed in this case.</p>
<dt><code>-F</code> <i>fmt</i></p>
<dd> Supplies a <code>strftime</code> (see <i><a href="/docs/linux/man/3-strftime/">strftime</a></i>(3)) string for the formatting of the time elements. The format string supports all of the zsh extensions described in the section EXPANSION OF PROMPT SEQUENCES in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1). The <code>-s</code> option is implied.</p>
<dt><code>-g</code></p>
<dd> Show the time elements in the GMT time zone. The <code>-s</code> option is implied.</p>
<dt><code>-l</code></p>
<dd> List the names of the type elements (to standard output or an array as appropriate) and return immediately; arguments, and options other than <code>-A</code>, are ignored.</p>
<dt><code>-L</code></p>
<dd> Perform an <code>lstat</code> (see <i><a href="/docs/linux/man/2-lstat/">lstat</a></i>(2)) rather than a <code>stat</code> system call. In this case, if the file is a link, information about the link itself rather than the target file is returned. This option is required to make the <code>link</code> element useful. It&#8217;s important to note that this is the exact opposite from <i><a href="/docs/linux/man/1-ls/">ls</a></i>(1), etc.</p>
<dt><code>-n</code></p>
<dd> Always show the names of files. Usually these are only shown when output is to standard output and there is more than one file in the list.</p>
<dt><code>-N</code></p>
<dd> Never show the names of files.</p>
<dt><code>-o</code></p>
<dd> If a raw file mode is printed, show it in octal, which is more useful for human consumption than the default of decimal. A leading zero will be printed in this case. Note that this does not affect whether a raw or formatted file mode is shown, which is controlled by the <code>-r</code> and <code>-s</code> options, nor whether a mode is shown at all.</p>
<dt><code>-r</code></p>
<dd> Print raw data (the default format) alongside string data (the <code>-s</code> format); the string data appears in parentheses after the raw data.</p>
<dt><code>-s</code></p>
<dd> Print <code>mode</code>, <code>uid</code>, <code>gid</code> and the three time elements as strings instead of numbers. In each case the format is like that of <code>ls -l</code>.</p>
<dt><code>-t</code></p>
<dd> Always show the type names for the elements of <code>struct stat</code>. Usually these are only shown when output is to standard output and no individual element has been selected.</p>
<dt><code>-T</code></p>
<dd> Never show the type names of the <code>struct stat</code> elements.</dl>
</dl>
</dl>
<h2>THE ZSH/SYSTEM MODULE</h2>
<p> The <code>zsh/system</code> module makes available various builtin commands and parameters. </p>
<h3>Builtins</h3>
<dl>
<dt>
<dd> <code>syserror</code> [ <code>-e</code> <i>errvar</i> ] [ <code>-p</code> <i>prefix</i> ] [ <i>errno</i> | <i>errname</i> ] This command prints out the error message associated with <i>errno</i>, a system error number, followed by a newline to standard error.</p>
<dl>
<dt>
<dd>
<p> Instead of the error number, a name <i>errname</i>, for example <code>ENOENT</code>, may be used. The set of names is the same as the contents of the array <code>errnos</code>, see below. </p>
<p> If the string <i>prefix</i> is given, it is printed in front of the error message, with no intervening space. </p>
<p> If <i>errvar</i> is supplied, the entire message, without a newline, is assigned to the parameter names <i>errvar</i> and nothing is output. </p>
<p> A return status of 0 indicates the message was successfully printed (although it may not be useful if the error number was out of the system&#8217;s range), a return status of 1 indicates an error in the parameters, and a return status of 2 indicates the error name was not recognised (no message is printed for this).</dl>
<dt>
<dd> <code>sysopen</code> [ <code>-arw</code> ] [ <code>-m</code> <i>permissions</i> ] [ <code>-o</code> <i>options</i> ]</p>
<dt>
<dd> <code>-u</code> <i>fd</i> <i>file</i> This command opens a file. The <code>-r</code>, <code>-w</code> and <code>-a</code> flags indicate whether the file should be opened for reading, writing and appending, respectively. The <code>-m</code> option allows the initial permissions to use when creating a file to be specified in octal form. The file descriptor is specified with <code>-u</code>. Either an explicit file descriptor in the range 0 to 9 can be specified or a variable name can be given to which the file descriptor number will be assigned.</p>
<dl>
<dt>
<dd>
<p> The <code>-o</code> option allows various system specific options to be specified as a comma-separated list. The following is a list of possible options. Note that, depending on the system, some may not be available.</p>
<dl>
<dt>
<dd> <code>cloexec</code> mark file to be closed when other programs are executed (else the file descriptor remains open in subshells and forked external executables)</p>
<dt>
<dd> <code>create</code></p>
<dt>
<dd> <code>creat</code> create file if it does not exist</p>
<dt><code>excl</code></p>
<dd> create file, error if it already exists</p>
<dt><code>noatime</code></p>
<dd> suppress updating of the file atime</p>
<dt><code>nofollow</code></p>
<dd> fail if <i>file</i> is a symbolic link</p>
<dt><code>sync</code></p>
<dd> request that writes wait until data has been physically written</p>
<dt>
<dd> <code>truncate</code></p>
<dt>
<dd> <code>trunc</code> truncate file to size 0</dl>
<p> To close the file, use one of the following: </p>
<dl>
<dt>
<dd>
exec{fd}&lt;&amp;-exec{fd}&gt; &amp; &#8211;
</dl>
</dl>
<dt>
<dd> <code>sysread </code>[ <code>-c</code> <i>countvar</i> ] [ <code>-i</code> <i>infd</i> ] [ <code>-o</code> <i>outfd</i> ]</p>
<dt>
<dd> [ <code>-s</code> <i>bufsize</i> ] [ <code>-t</code> <i>timeout</i> ] [ <i>param</i> ] Perform a single system read from file descriptor <i>infd</i>, or zero if that is not given. The result of the read is stored in <i>param</i> or <code>REPLY</code> if that is not given. If <i>countvar</i> is given, the number of bytes read is assigned to the parameter named by <i>countvar</i>.</p>
<dl>
<dt>
<dd>
<p> The maximum number of bytes read is <i>bufsize</i> or 8192 if that is not given, however the command returns as soon as any number of bytes was successfully read. </p>
<p> If <i>timeout</i> is given, it specifies a timeout in seconds, which may be zero to poll the file descriptor. This is handled by the <code>poll</code> system call if available, otherwise the <code>select</code> system call if available. </p>
<p> If <i>outfd</i> is given, an attempt is made to write all the bytes just read to the file descriptor <i>outfd</i>. If this fails, because of a system error other than <code>EINTR</code> or because of an internal zsh error during an interrupt, the bytes read but not written are stored in the parameter named by <i>param</i> if supplied (no default is used in this case), and the number of bytes read but not written is stored in the parameter named by <i>countvar</i> if that is supplied. If it was successful, <i>countvar</i> contains the full number of bytes transferred, as usual, and <i>param</i> is not set. </p>
<p> The error <code>EINTR</code> (interrupted system call) is handled internally so that shell interrupts are transparent to the caller. Any other error causes a return. </p>
<p> The possible return statuses are</p>
<dl>
<dt>
<dd> 0 At least one byte of data was successfully read and, if appropriate, written.</p>
<dt>1</p>
<dd> There was an error in the parameters to the command. This is the only error for which a message is printed to standard error.</p>
<dt>2</p>
<dd> There was an error on the read, or on polling the input file descriptor for a timeout. The parameter <code>ERRNO</code> gives the error.</p>
<dt>3</p>
<dd> Data were successfully read, but there was an error writing them to <i>outfd</i>. The parameter <code>ERRNO</code> gives the error.</p>
<dt>4</p>
<dd> The attempt to read timed out. Note this does not set <code>ERRNO</code> as this is not a system error.</p>
<dt>5</p>
<dd> No system error occurred, but zero bytes were read. This usually indicates end of file. The parameters are set according to the usual rules; no write to <i>outfd</i> is attempted.</dl>
</dl>
<dt><code>sysseek</code> [ <code>-u</code> <i>fd</i> ] [ <code>-w</code> <code>start</code>|<code>end</code>|<code>current</code> ] <i>offset</i></p>
<dd> The current file position at which future reads and writes will take place is adjusted to the specified byte offset. The <i>offset</i> is evaluated as a math expression. The <code>-u</code> option allows the file descriptor to be specified. By default the offset is specified relative to the start or the file but, with the <code>-w</code> option, it is possible to specify that the offset should be relative to the current position or the end of the file.</p>
<dt><code>syswrite</code> [ <code>-c</code> <i>countvar</i> ] [ <code>-o</code> <i>outfd</i> ] <i>data</i></p>
<dd> The data (a single string of bytes) are written to the file descriptor <i>outfd</i>, or 1 if that is not given, using the <code>write</code> system call. Multiple write operations may be used if the first does not write all the data.</p>
<dl>
<dt>
<dd>
<p> If <i>countvar</i> is given, the number of byte written is stored in the parameter named by <i>countvar</i>; this may not be the full length of <i>data</i> if an error occurred. </p>
<p> The error <code>EINTR</code> (interrupted system call) is handled internally by retrying; otherwise an error causes the command to return. For example, if the file descriptor is set to non-blocking output, an error <code>EAGAIN</code> (on some systems, <code>EWOULDBLOCK</code>) may result in the command returning early. </p>
<p> The return status may be 0 for success, 1 for an error in the parameters to the command, or 2 for an error on the write; no error message is printed in the last case, but the parameter <code>ERRNO</code> will reflect the error that occurred.</dl>
<dt>
<dd> <code>zsystem flock</code> [ <code>-t</code> <i>timeout</i> ] [ <code>-f</code> <i>var</i> ] [<code>-er</code>] <i>file</i></p>
<dt>
<dd> <code>zsystem flock -u</code> <i>fd_expr</i> The builtin <code>zsystem</code>&#8216;s subcommand <code>flock</code> performs advisory file locking (via the <i><a href="/docs/linux/man/2-fcntl/">fcntl</a></i>(2) system call) over the entire contents of the given file. This form of locking requires the processes accessing the file to cooperate; its most obvious use is between two instances of the shell itself.</p>
<dl>
<dt>
<dd>
<p> In the first form the named <i>file</i>, which must already exist, is locked by opening a file descriptor to the file and applying a lock to the file descriptor. The lock terminates when the shell process that created the lock exits; it is therefore often convenient to create file locks within subshells, since the lock is automatically released when the subshell exits. Note that use of the <code>print</code> builtin with the <code>-u</code> option will, as a side effect, release the lock, as will redirection to the file in the shell holding the lock. To work around this use a subshell, e.g. `<code>(print message) &gt;&gt; </code><i>file</i>&#8216;. Status 0 is returned if the lock succeeds, else status 1. </p>
<p> In the second form the file descriptor given by the arithmetic expression <i>fd_expr</i> is closed, releasing a lock. The file descriptor can be queried by using the `<code>-f</code> <i>var</i>&#8216; form during the lock; on a successful lock, the shell variable <i>var</i> is set to the file descriptor used for locking. The lock will be released if the file descriptor is closed by any other means, for example using `<code>exec {</code><i>var</i><code>}&gt;&amp;-</code>&#8216;; however, the form described here performs a safety check that the file descriptor is in use for file locking. </p>
<p> By default the shell waits indefinitely for the lock to succeed. The option <code>-t</code> <i>timeout</i> specifies a timeout for the lock in seconds; currently this must be an integer. The shell will attempt to lock the file once a second during this period. If the attempt times out, status 2 is returned. </p>
<p> If the option <code>-e</code> is given, the file descriptor for the lock is preserved when the shell uses <code>exec</code> to start a new process; otherwise it is closed at that point and the lock released. </p>
<p> If the option <code>-r</code> is given, the lock is only for reading, otherwise it is for reading and writing. The file descriptor is opened accordingly.</dl>
<dt><code>zsystem supports</code> <i>subcommand</i></p>
<dd> The builtin <code>zsystem</code>&#8216;s subcommand <code>supports</code> tests whether a given subcommand is supported. It returns status 0 if so, else status 1. It operates silently unless there was a syntax error (i.e. the wrong number of arguments), in which case status 255 is returned. Status 1 can indicate one of two things: <i>subcommand</i> is known but not supported by the current operating system, or <i>subcommand</i> is not known (possibly because this is an older version of the shell before it was implemented).</dl>
<h3>Math Functions</h3>
<dl>
<dt>
<dd> <code>systell(</code><i>fd</i>) The systell math function returns the current file position for the file descriptor passed as an argument.</dl>
<h3>Parameters</h3>
<dl>
<dt>
<dd> <code>errnos</code> A readonly array of the names of errors defined on the system. These are typically macros defined in C by including the system header file <code>errno.h</code>. The index of each name (assuming the option <code>KSH_ARRAYS</code> is unset) corresponds to the error number. Error numbers <i>num</i> before the last known error which have no name are given the name <code>E</code><i>num</i> in the array.</p>
<dl>
<dt>
<dd>
<p> Note that aliases for errors are not handled; only the canonical name is used.</dl>
<dt><code>sysparams</code></p>
<dd> A readonly associative array. The keys are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>pid</code> Returns the process ID of the current process, even in subshells. Compare <code>$$</code>, which returns the process ID of the main shell process.</p>
<dt><code>ppid</code></p>
<dd> Returns the process ID of the parent of the current process, even in subshells. Compare <code>$PPID</code>, which returns the process ID of the parent of the main shell process.</p>
<dt><code>procsubstpid</code></p>
<dd> Returns the process ID of the last process started for process substitution, i.e. the <code>&lt;(</code><i>&#8230;</i><code>)</code> and <code>&gt;(</code><i>&#8230;</i><code>)</code> expansions.</dl>
</dl>
</dl>
<h2>THE ZSH/NET/TCP MODULE</h2>
<p> The <code>zsh/net/tcp</code> module makes available one builtin command: </p>
<dl>
<dt>
<dd> <code>ztcp</code> [ <code>-acflLtv</code> ] [ <code>-d</code> <i>fd</i> ] [ <i>args</i> ] <code>ztcp</code> is implemented as a builtin to allow full use of shell command line editing, file I/O, and job control mechanisms.</p>
<dl>
<dt>
<dd>
<p> If <code>ztcp</code> is run with no options, it will output the contents of its session table. </p>
<p> If it is run with only the option <code>-L</code>, it will output the contents of the session table in a format suitable for automatic parsing. The option is ignored if given with a command to open or close a session. The output consists of a set of lines, one per session, each containing the following elements separated by spaces: </p>
<dl>
<dt>
<dd> File descriptor The file descriptor in use for the connection. For normal inbound (<code>I</code>) and outbound (<code>O</code>) connections this may be read and written by the usual shell mechanisms. However, it should only be close with `<code>ztcp -c</code>&#8216;.</p>
<dt>Connection type</p>
<dd> A letter indicating how the session was created:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>Z</code> A session created with the <code>zftp</code> command.</p>
<dt><code>L</code></p>
<dd> A connection opened for listening with `<code>ztcp -l</code>&#8216;.</p>
<dt><code>I</code></p>
<dd> An inbound connection accepted with `<code>ztcp -a</code>&#8216;.</p>
<dt><code>O</code></p>
<dd> An outbound connection created with `<code>ztcp</code> <i>host</i> <i>&#8230;</i>&#8216;.</dl>
</dl>
<dt>The local host</p>
<dd> This is usually set to an all-zero IP address as the address of the localhost is irrelevant.</p>
<dt>The local port</p>
<dd> This is likely to be zero unless the connection is for listening.</p>
<dt>The remote host</p>
<dd> This is the fully qualified domain name of the peer, if available, else an IP address. It is an all-zero IP address for a session opened for listening.</p>
<dt>The remote port</p>
<dd> This is zero for a connection opened for listening.</dl>
</dl>
</dl>
<h3>Outbound Connections</h3>
<dl>
<dt>
<dd> <code>ztcp</code> [ <code>-v</code> ] [ <code>-d</code> <i>fd</i> ] <i>host</i> [ <i>port</i> ] Open a new TCP connection to <i>host</i>. If the <i>port</i> is omitted, it will default to port 23. The connection will be added to the session table and the shell parameter <code>REPLY</code> will be set to the file descriptor associated with that connection.</p>
<dl>
<dt>
<dd>
<p> If <code>-d</code> is specified, its argument will be taken as the target file descriptor for the connection. </p>
<p> In order to elicit more verbose output, use <code>-v</code>.</dl>
</dl>
<h3>Inbound Connections</h3>
<dl>
<dt>
<dd> <code>ztcp</code> <code>-l</code> [ <code>-v</code> ] [ <code>-d</code> <i>fd</i> ] <i>port</i> <code>ztcp -l</code> will open a socket listening on TCP <i>port</i>. The socket will be added to the session table and the shell parameter <code>REPLY</code> will be set to the file descriptor associated with that listener.</p>
<dl>
<dt>
<dd>
<p> If <code>-d</code> is specified, its argument will be taken as the target file descriptor for the connection. </p>
<p> In order to elicit more verbose output, use <code>-v</code>.</dl>
<dt><code>ztcp</code> <code>-a</code> [ <code>-tv</code> ] [ <code>-d</code> <i>targetfd</i> ] <i>listenfd</i></p>
<dd> <code>ztcp -a</code> will accept an incoming connection to the port associated with <i>listenfd</i>. The connection will be added to the session table and the shell parameter <code>REPLY</code> will be set to the file descriptor associated with the inbound connection.</p>
<dl>
<dt>
<dd>
<p> If <code>-d</code> is specified, its argument will be taken as the target file descriptor for the connection. </p>
<p> If <code>-t</code> is specified, <code>ztcp</code> will return if no incoming connection is pending. Otherwise it will wait for one. </p>
<p> In order to elicit more verbose output, use <code>-v</code>.</dl>
</dl>
<h3>Closing Connections</h3>
<dl>
<dt>
<dd> <code>ztcp</code> <code>-cf</code> [ <code>-v</code> ] [ <i>fd</i> ]</p>
<dt>
<dd> <code>ztcp</code> <code>-c</code> [ <code>-v</code> ] [ <i>fd</i> ] <code>ztcp -c</code> will close the socket associated with <i>fd</i>. The socket will be removed from the session table. If <i>fd</i> is not specified, <code>ztcp</code> will close everything in the session table.</p>
<dl>
<dt>
<dd>
<p> Normally, sockets registered by zftp (see <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1) ) cannot be closed this way. In order to force such a socket closed, use <code>-f</code>. </p>
<p> In order to elicit more verbose output, use <code>-v</code>.</dl>
</dl>
<h3>Example</h3>
<p> Here is how to create a TCP connection between two instances of zsh. We need to pick an unassigned port; here we use the randomly chosen 5123. </p>
<p> On <code>host1</code>,</p>
<dl>
<dt>
<dd>
<pre>
<code>zmodload zsh/net/tcp
ztcp -l 5123
listenfd=$REPLY
ztcp -a $listenfd
fd=$REPLY</code>
</pre>
</dl>
<p> The second from last command blocks until there is an incoming connection. </p>
<p> Now create a connection from <code>host2</code> (which may, of course, be the same machine):</p>
<dl>
<dt>
<dd>
<pre>
<code>zmodload zsh/net/tcp
ztcp host1 5123
fd=$REPLY</code>
</pre>
</dl>
<p> Now on each host, <code>$fd</code> contains a file descriptor for talking to the other. For example, on <code>host1</code>:</p>
<dl>
<dt>
<dd>
<pre>
<code>print This is a message &gt;&amp;$fd</code>
</pre>
</dl>
<p> and on <code>host2</code>:</p>
<dl>
<dt>
<dd>
<pre>
<code>read -r line &lt;&amp;$fd; print -r - $line</code>
</pre>
</dl>
<p> prints `<code>This is a message</code>&#8216;. </p>
<p> To tidy up, on <code>host1</code>:</p>
<dl>
<dt>
<dd>
<pre>
<code>ztcp -c $listenfd
ztcp -c $fd</code>
</pre>
</dl>
<p> and on <code>host2</code></p>
<dl>
<dt>
<dd>
<pre>
<code>ztcp -c $fd</code>
</pre>
</dl>
<h2>THE ZSH/TERMCAP MODULE</h2>
<p> The <code>zsh/termcap</code> module makes available one builtin command: </p>
<dl>
<dt>
<dd> <code>echotc</code> <i>cap</i> [ <i>arg</i> &#8230; ] Output the termcap value corresponding to the capability <i>cap</i>, with optional arguments.</dl>
<p> The <code>zsh/termcap</code> module makes available one parameter: </p>
<dl>
<dt>
<dd> <code>termcap</code> An associative array that maps termcap capability codes to their values.</dl>
<h2>THE ZSH/TERMINFO MODULE</h2>
<p> The <code>zsh/terminfo</code> module makes available one builtin command: </p>
<dl>
<dt>
<dd> <code>echoti</code> <i>cap</i> [ <i>arg</i> ] Output the terminfo value corresponding to the capability <i>cap</i>, instantiated with <i>arg</i> if applicable.</dl>
<p> The <code>zsh/terminfo</code> module makes available one parameter: </p>
<dl>
<dt>
<dd> <code>terminfo</code> An associative array that maps terminfo capability names to their values.</dl>
<h2>THE ZSH/ZFTP MODULE</h2>
<p> The <code>zsh/zftp</code> module makes available one builtin command: </p>
<dl>
<dt>
<dd> <code>zftp</code> <i>subcommand</i> [ <i>args</i> ] The <code>zsh/zftp</code> module is a client for FTP (file transfer protocol). It is implemented as a builtin to allow full use of shell command line editing, file I/O, and job control mechanisms. Often, users will access it via shell functions providing a more powerful interface; a set is provided with the <code>zsh</code> distribution and is described in <i><a href="/docs/linux/man/1-zshzftpsys/">zshzftpsys</a></i>(1). However, the <code>zftp</code> command is entirely usable in its own right.</p>
<dl>
<dt>
<dd>
<p> All commands consist of the command name <code>zftp</code> followed by the name of a subcommand. These are listed below. The return status of each subcommand is supposed to reflect the success or failure of the remote operation. See a description of the variable <code>ZFTP_VERBOSE</code> for more information on how responses from the server may be printed.</dl>
</dl>
<h3>Subcommands</h3>
<dl>
<dt>
<dd> <code>open</code> <i>host</i>[<code>:</code><i>port</i>] [ <i>user</i> [ <i>password</i> [ <i>account</i> ] ] ] Open a new FTP session to <i>host</i>, which may be the name of a TCP/IP connected host or an IP number in the standard dot notation. If the argument is in the form <i>host</i><code>:</code><i>port</i>, open a connection to TCP port <i>port</i> instead of the standard FTP port 21. This may be the name of a TCP service or a number: see the description of <code>ZFTP_PORT</code> below for more information.</p>
<dl>
<dt>
<dd>
<p> If IPv6 addresses in colon format are used, the <i>host</i> should be surrounded by quoted square brackets to distinguish it from the <i>port</i>, for example <code>&#8216;[fe80::203:baff:fe02:8b56]&#8217;</code>. For consistency this is allowed with all forms of <i>host</i>. </p>
<p> Remaining arguments are passed to the <code>login</code> subcommand. Note that if no arguments beyond <i>host</i> are supplied, <code>open</code> will <i>not</i> automatically call <code>login</code>. If no arguments at all are supplied, <code>open</code> will use the parameters set by the <code>params</code> subcommand. </p>
<p> After a successful open, the shell variables <code>ZFTP_HOST</code>, <code>ZFTP_PORT</code>, <code>ZFTP_IP</code> and <code>ZFTP_SYSTEM</code> are available; see `Variables&#8217; below.</dl>
<dt>
<dd> <code>login</code> [ <i>name</i> [ <i>password</i> [ <i>account</i> ] ] ]</p>
<dt>
<dd> <code>user</code> [ <i>name</i> [ <i>password</i> [ <i>account</i> ] ] ] Login the user <i>name</i> with parameters <i>password</i> and <i>account</i>. Any of the parameters can be omitted, and will be read from standard input if needed (<i>name</i> is always needed). If standard input is a terminal, a prompt for each one will be printed on standard error and <i>password</i> will not be echoed. If any of the parameters are not used, a warning message is printed.</p>
<dl>
<dt>
<dd>
<p> After a successful login, the shell variables <code>ZFTP_USER</code>, <code>ZFTP_ACCOUNT</code> and <code>ZFTP_PWD</code> are available; see `Variables&#8217; below. </p>
<p> This command may be re-issued when a user is already logged in, and the server will first be reinitialized for a new user.</dl>
<dt>
<dd> <code>params</code> [ <i>host</i> [ <i>user</i> [ <i>password</i> [ <i>account</i> ] ] ] ]</p>
<dt>
<dd> <code>params</code> <code>&#8211;</code> Store the given parameters for a later <code>open</code> command with no arguments. Only those given on the command line will be remembered. If no arguments are given, the parameters currently set are printed, although the password will appear as a line of stars; the return status is one if no parameters were set, zero otherwise.</p>
<dl>
<dt>
<dd>
<p> Any of the parameters may be specified as a `<code>?</code>&#8216;, which may need to be quoted to protect it from shell expansion. In this case, the appropriate parameter will be read from stdin as with the <code>login</code> subcommand, including special handling of <i>password</i>. If the `<code>?</code>&#8216; is followed by a string, that is used as the prompt for reading the parameter instead of the default message (any necessary punctuation and whitespace should be included at the end of the prompt). The first letter of the parameter (only) may be quoted with a `<code>\</code>&#8216;; hence an argument <code>&quot;\$word&quot;</code> guarantees that the string from the shell parameter <code>$word</code> will be treated literally, whether or not it begins with a `<code>?</code>&#8216;. </p>
<p> If instead a single `<code>&#8211;</code>&#8216; is given, the existing parameters, if any, are deleted. In that case, calling <code>open</code> with no arguments will cause an error. </p>
<p> The list of parameters is not deleted after a <code>close</code>, however it will be deleted if the <code>zsh/zftp</code> module is unloaded. </p>
<p> For example, </p>
<dl>
<dt>
<dd>
<pre>
<code>zftp params <a href="ftp://ftp.elsewhere.xx">ftp.elsewhere.xx</a> juser '?Password for juser: '</code>
</pre>
</dl>
<p> will store the host <code><a href="ftp://ftp.elsewhere.xx">ftp.elsewhere.xx</a></code> and the user <code>juser</code> and then prompt the user for the corresponding password with the given prompt.</dl>
<dt><code>test</code></p>
<dd> Test the connection; if the server has reported that it has closed the connection (maybe due to a timeout), return status 2; if no connection was open anyway, return status 1; else return status 0. The <code>test</code> subcommand is silent, apart from messages printed by the <code>$ZFTP_VERBOSE</code> mechanism, or error messages if the connection closes. There is no network overhead for this test.</p>
<dl>
<dt>
<dd>
<p> The test is only supported on systems with either the <code><a href="/docs/linux/man/2-select/">select</a>(2)</code> or <code><a href="/docs/linux/man/2-poll/">poll</a>(2)</code> system calls; otherwise the message `<code>not supported on this system</code>&#8216; is printed instead. </p>
<p> The <code>test</code> subcommand will automatically be called at the start of any other subcommand for the current session when a connection is open.</dl>
<dt><code>cd</code> <i>directory</i></p>
<dd> Change the remote directory to <i>directory</i>. Also alters the shell variable <code>ZFTP_PWD</code>.</p>
<dt><code>cdup</code></p>
<dd> Change the remote directory to the one higher in the directory tree. Note that <code>cd ..</code> will also work correctly on non-UNIX systems.</p>
<dt><code>dir</code> [ <i>arg</i> &#8230; ]</p>
<dd> Give a (verbose) listing of the remote directory. The <i>arg</i>s are passed directly to the server. The command&#8217;s behaviour is implementation dependent, but a UNIX server will typically interpret <i>arg</i>s as arguments to the <code>ls</code> command and with no arguments return the result of `<code>ls -l</code>&#8216;. The directory is listed to standard output.</p>
<dt><code>ls</code> [ <i>arg</i> &#8230; ]</p>
<dd> Give a (short) listing of the remote directory. With no <i>arg</i>, produces a raw list of the files in the directory, one per line. Otherwise, up to vagaries of the server implementation, behaves similar to <code>dir</code>.</p>
<dt><code>type</code> [ <i>type</i> ]</p>
<dd> Change the type for the transfer to <i>type</i>, or print the current type if <i>type</i> is absent. The allowed values are `<code>A</code>&#8216; (ASCII), `<code>I</code>&#8216; (Image, i.e. binary), or `<code>B</code>&#8216; (a synonym for `<code>I</code>&#8216;).</p>
<dl>
<dt>
<dd>
<p> The FTP default for a transfer is ASCII. However, if <code>zftp</code> finds that the remote host is a UNIX machine with 8-bit byes, it will automatically switch to using binary for file transfers upon <code>open</code>. This can subsequently be overridden. </p>
<p> The transfer type is only passed to the remote host when a data connection is established; this command involves no network overhead.</dl>
<dt><code>ascii</code></p>
<dd> The same as <code>type A</code>.</p>
<dt><code>binary</code></p>
<dd> The same as <code>type I</code>.</p>
<dt><code>mode</code> [ <code>S</code> | <code>B</code> ]</p>
<dd> Set the mode type to stream (<code>S</code>) or block (<code>B</code>). Stream mode is the default; block mode is not widely supported.</p>
<dt>
<dd> <code>remote</code> <i>file</i> &#8230;</p>
<dt>
<dd> <code>local</code> [ <i>file</i> &#8230; ] Print the size and last modification time of the remote or local files. If there is more than one item on the list, the name of the file is printed first. The first number is the file size, the second is the last modification time of the file in the format <code>CCYYMMDDhhmmSS</code> consisting of year, month, date, hour, minutes and seconds in GMT. Note that this format, including the length, is guaranteed, so that time strings can be directly compared via the <code>[[</code> builtin&#8217;s <code>&lt;</code> and <code>&gt;</code> operators, even if they are too long to be represented as integers.</p>
<dl>
<dt>
<dd>
<p> Not all servers support the commands for retrieving this information. In that case, the <code>remote</code> command will print nothing and return status 2, compared with status 1 for a file not found. </p>
<p> The <code>local</code> command (but not <code>remote</code>) may be used with no arguments, in which case the information comes from examining file descriptor zero. This is the same file as seen by a <code>put</code> command with no further redirection.</dl>
<dt><code>get</code> <i>file</i> &#8230;</p>
<dd> Retrieve all <i>file</i>s from the server, concatenating them and sending them to standard output.</p>
<dt><code>put</code> <i>file</i> &#8230;</p>
<dd> For each <i>file</i>, read a file from standard input and send that to the remote host with the given name.</p>
<dt><code>append</code> <i>file</i> &#8230;</p>
<dd> As <code>put</code>, but if the remote <i>file</i> already exists, data is appended to it instead of overwriting it.</p>
<dt>
<dd> <code>getat</code> <i>file</i> <i>point</i></p>
<dt>
<dd> <code>putat</code> <i>file</i> <i>point</i></p>
<dt>
<dd> <code>appendat</code> <i>file</i> <i>point</i> Versions of <code>get</code>, <code>put</code> and <code>append</code> which will start the transfer at the given <i>point</i> in the remote <i>file</i>. This is useful for appending to an incomplete local file. However, note that this ability is not universally supported by servers (and is not quite the behaviour specified by the standard).</p>
<dt><code>delete</code> <i>file</i> &#8230;</p>
<dd> Delete the list of files on the server.</p>
<dt><code>mkdir</code> <i>directory</i></p>
<dd> Create a new directory <i>directory</i> on the server.</p>
<dt><code>rmdir</code> <i>directory</i></p>
<dd> Delete the directory <i>directory</i> on the server.</p>
<dt><code>rename</code> <i>old-name</i> <i>new-name</i></p>
<dd> Rename file <i>old-name</i> to <i>new-name</i> on the server.</p>
<dt><code>site</code> <i>arg</i> &#8230;</p>
<dd> Send a host-specific command to the server. You will probably only need this if instructed by the server to use it.</p>
<dt><code>quote</code> <i>arg</i> &#8230;</p>
<dd> Send the raw FTP command sequence to the server. You should be familiar with the FTP command set as defined in RFC959 before doing this. Useful commands may include <code>STAT</code> and <code>HELP</code>. Note also the mechanism for returning messages as described for the variable <code>ZFTP_VERBOSE</code> below, in particular that all messages from the control connection are sent to standard error.</p>
<dt>
<dd> <code>close</code></p>
<dt>
<dd> <code>quit</code> Close the current data connection. This unsets the shell parameters <code>ZFTP_HOST</code>, <code>ZFTP_PORT</code>, <code>ZFTP_IP</code>, <code>ZFTP_SYSTEM</code>, <code>ZFTP_USER</code>, <code>ZFTP_ACCOUNT</code>, <code>ZFTP_PWD</code>, <code>ZFTP_TYPE</code> and <code>ZFTP_MODE</code>.</p>
<dt><code>session</code> [ <i>sessname</i> ]</p>
<dd> Allows multiple FTP sessions to be used at once. The name of the session is an arbitrary string of characters; the default session is called `<code>default</code>&#8216;. If this command is called without an argument, it will list all the current sessions; with an argument, it will either switch to the existing session called <i>sessname</i>, or create a new session of that name.</p>
<dl>
<dt>
<dd>
<p> Each session remembers the status of the connection, the set of connection-specific shell parameters (the same set as are unset when a connection closes, as given in the description of <code>close</code>), and any user parameters specified with the <code>params</code> subcommand. Changing to a previous session restores those values; changing to a new session initialises them in the same way as if <code>zftp</code> had just been loaded. The name of the current session is given by the parameter <code>ZFTP_SESSION</code>.</dl>
<dt><code>rmsession</code> [ <i>sessname</i> ]</p>
<dd> Delete a session; if a name is not given, the current session is deleted. If the current session is deleted, the earliest existing session becomes the new current session, otherwise the current session is not changed. If the session being deleted is the only one, a new session called `<code>default</code>&#8216; is created and becomes the current session; note that this is a new session even if the session being deleted is also called `<code>default</code>&#8216;. It is recommended that sessions not be deleted while background commands which use <code>zftp</code> are still active.</dl>
<h3>Parameters</h3>
<p> The following shell parameters are used by <code>zftp</code>. Currently none of them are special. </p>
<dl>
<dt>
<dd> <code>ZFTP_TMOUT</code> Integer. The time in seconds to wait for a network operation to complete before returning an error. If this is not set when the module is loaded, it will be given the default value 60. A value of zero turns off timeouts. If a timeout occurs on the control connection it will be closed. Use a larger value if this occurs too frequently.</p>
<dt><code>ZFTP_IP</code></p>
<dd> Readonly. The IP address of the current connection in dot notation.</p>
<dt><code>ZFTP_HOST</code></p>
<dd> Readonly. The hostname of the current remote server. If the host was opened as an IP number, <code>ZFTP_HOST</code> contains that instead; this saves the overhead for a name lookup, as IP numbers are most commonly used when a nameserver is unavailable.</p>
<dt><code>ZFTP_PORT</code></p>
<dd> Readonly. The number of the remote TCP port to which the connection is open (even if the port was originally specified as a named service). Usually this is the standard FTP port, 21.</p>
<dl>
<dt>
<dd>
<p> In the unlikely event that your system does not have the appropriate conversion functions, this appears in network byte order. If your system is little-endian, the port then consists of two swapped bytes and the standard port will be reported as 5376. In that case, numeric ports passed to <code>zftp open</code> will also need to be in this format.</dl>
<dt><code>ZFTP_SYSTEM</code></p>
<dd> Readonly. The system type string returned by the server in response to an FTP <code>SYST</code> request. The most interesting case is a string beginning <code>&quot;UNIX Type: L8&quot;</code>, which ensures maximum compatibility with a local UNIX host.</p>
<dt><code>ZFTP_TYPE</code></p>
<dd> Readonly. The type to be used for data transfers , either `<code>A</code>&#8216; or `<code>I</code>&#8216;. Use the <code>type</code> subcommand to change this.</p>
<dt><code>ZFTP_USER</code></p>
<dd> Readonly. The username currently logged in, if any.</p>
<dt><code>ZFTP_ACCOUNT</code></p>
<dd> Readonly. The account name of the current user, if any. Most servers do not require an account name.</p>
<dt><code>ZFTP_PWD</code></p>
<dd> Readonly. The current directory on the server.</p>
<dt><code>ZFTP_CODE</code></p>
<dd> Readonly. The three digit code of the last FTP reply from the server as a string. This can still be read after the connection is closed, and is not changed when the current session changes.</p>
<dt><code>ZFTP_REPLY</code></p>
<dd> Readonly. The last line of the last reply sent by the server. This can still be read after the connection is closed, and is not changed when the current session changes.</p>
<dt><code>ZFTP_SESSION</code></p>
<dd> Readonly. The name of the current FTP session; see the description of the <code>session</code> subcommand.</p>
<dt><code>ZFTP_PREFS</code></p>
<dd> A string of preferences for altering aspects of <code>zftp</code>&#8216;s behaviour. Each preference is a single character. The following are defined:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>P</code> Passive: attempt to make the remote server initiate data transfers. This is slightly more efficient than sendport mode. If the letter <code>S</code> occurs later in the string, <code>zftp</code> will use sendport mode if passive mode is not available.</p>
<dt><code>S</code></p>
<dd> Sendport: initiate transfers by the FTP <code>PORT</code> command. If this occurs before any <code>P</code> in the string, passive mode will never be attempted.</p>
<dt><code>D</code></p>
<dd> Dumb: use only the bare minimum of FTP commands. This prevents the variables <code>ZFTP_SYSTEM</code> and <code>ZFTP_PWD</code> from being set, and will mean all connections default to ASCII type. It may prevent <code>ZFTP_SIZE</code> from being set during a transfer if the server does not send it anyway (many servers do).</dl>
<p> If <code>ZFTP_PREFS</code> is not set when <code>zftp</code> is loaded, it will be set to a default of `<code>PS</code>&#8216;, i.e. use passive mode if available, otherwise fall back to sendport mode.</dl>
<dt><code>ZFTP_VERBOSE</code></p>
<dd> A string of digits between 0 and 5 inclusive, specifying which responses from the server should be printed. All responses go to standard error. If any of the numbers 1 to 5 appear in the string, raw responses from the server with reply codes beginning with that digit will be printed to standard error. The first digit of the three digit reply code is defined by RFC959 to correspond to:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 1. A positive preliminary reply.</p>
<dt>2.</p>
<dd> A positive completion reply.</p>
<dt>3.</p>
<dd> A positive intermediate reply.</p>
<dt>4.</p>
<dd> A transient negative completion reply.</p>
<dt>5.</p>
<dd> A permanent negative completion reply.</dl>
<p> It should be noted that, for unknown reasons, the reply `Service not available&#8217;, which forces termination of a connection, is classified as 421, i.e. `transient negative&#8217;, an interesting interpretation of the word `transient&#8217;. </p>
<p> The code 0 is special: it indicates that all but the last line of multiline replies read from the server will be printed to standard error in a processed format. By convention, servers use this mechanism for sending information for the user to read. The appropriate reply code, if it matches the same response, takes priority. </p>
<p> If <code>ZFTP_VERBOSE</code> is not set when <code>zftp</code> is loaded, it will be set to the default value <code>450</code>, i.e., messages destined for the user and all errors will be printed. A null string is valid and specifies that no messages should be printed.</dl>
</dl>
<h3>Functions</h3>
<dl>
<dt>
<dd> <code>zftp_chpwd</code> If this function is set by the user, it is called every time the directory changes on the server, including when a user is logged in, or when a connection is closed. In the last case, <code>$ZFTP_PWD</code> will be unset; otherwise it will reflect the new directory.</p>
<dt><code>zftp_progress</code></p>
<dd> If this function is set by the user, it will be called during a <code>get</code>, <code>put</code> or <code>append</code> operation each time sufficient data has been received from the host. During a <code>get</code>, the data is sent to standard output, so it is vital that this function should write to standard error or directly to the terminal, <i>not</i> to standard output.</p>
<dl>
<dt>
<dd>
<p> When it is called with a transfer in progress, the following additional shell parameters are set: </p>
<dl>
<dt>
<dd> <code>ZFTP_FILE</code> The name of the remote file being transferred from or to.</p>
<dt><code>ZFTP_TRANSFER</code></p>
<dd> A <code>G</code> for a <code>get</code> operation and a <code>P</code> for a <code>put</code> operation.</p>
<dt><code>ZFTP_SIZE</code></p>
<dd> The total size of the complete file being transferred: the same as the first value provided by the <code>remote</code> and <code>local</code> subcommands for a particular file. If the server cannot supply this value for a remote file being retrieved, it will not be set. If input is from a pipe the value may be incorrect and correspond simply to a full pipe buffer.</p>
<dt><code>ZFTP_COUNT</code></p>
<dd> The amount of data so far transferred; a number between zero and <code>$ZFTP_SIZE</code>, if that is set. This number is always available.</dl>
<p> The function is initially called with <code>ZFTP_TRANSFER</code> set appropriately and <code>ZFTP_COUNT</code> set to zero. After the transfer is finished, the function will be called one more time with <code>ZFTP_TRANSFER</code> set to <code>GF</code> or <code>PF</code>, in case it wishes to tidy up. It is otherwise never called twice with the same value of <code>ZFTP_COUNT</code>. </p>
<p> Sometimes the progress meter may cause disruption. It is up to the user to decide whether the function should be defined and to use <code>unfunction</code> when necessary.</dl>
</dl>
<h3>Problems</h3>
<p> A connection may not be opened in the left hand side of a pipe as this occurs in a subshell and the file information is not updated in the main shell. In the case of type or mode changes or closing the connection in a subshell, the information is returned but variables are not updated until the next call to <code>zftp</code>. Other status changes in subshells will not be reflected by changes to the variables (but should be otherwise harmless). </p>
<p> Deleting sessions while a <code>zftp</code> command is active in the background can have unexpected effects, even if it does not use the session being deleted. This is because all shell subprocesses share information on the state of all connections, and deleting a session changes the ordering of that information. </p>
<p> On some operating systems, the control connection is not valid after a fork(), so that operations in subshells, on the left hand side of a pipeline, or in the background are not possible, as they should be. This is presumably a bug in the operating system.</p>
<h2>THE ZSH/ZLE MODULE</h2>
<p> The <code>zsh/zle</code> module contains the Zsh Line Editor. See <i><a href="/docs/linux/man/1-zshzle/">zshzle</a></i>(1).</p>
<h2>THE ZSH/ZLEPARAMETER MODULE</h2>
<p> The <code>zsh/zleparameter</code> module defines two special parameters that can be used to access internal information of the Zsh Line Editor (see <i><a href="/docs/linux/man/1-zshzle/">zshzle</a></i>(1)). </p>
<dl>
<dt>
<dd> <code>keymaps</code> This array contains the names of the keymaps currently defined.</p>
<dt><code>widgets</code></p>
<dd> This associative array contains one entry per widget. The name of the widget is the key and the value gives information about the widget. It is either<br />
&nbsp;<wbr>&nbsp;the string&nbsp;`<code>builtin</code>&#8216;&nbsp;for builtin widgets,<br />
&nbsp;<wbr>&nbsp;a string of the form&nbsp;`<code>user:</code><i>name</i>&#8216;&nbsp;for user-defined widgets,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;where&nbsp;<i>name</i>&nbsp;is the name of the shell function implementing the widget,<br />
&nbsp;<wbr>&nbsp;a string of the form&nbsp;`<code>completion:</code><i>type</i><code>:</code><i>name</i>&#8216;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for completion widgets,<br />
&nbsp;<wbr>&nbsp;or a null value if the widget is not yet fully defined. In the penultimate case, <i>type</i> is the name of the builtin widget the completion widget imitates in its behavior and <i>name</i> is the name of the shell function implementing the completion widget.</dl>
<h2>THE ZSH/ZPROF MODULE</h2>
<p> When loaded, the <code>zsh/zprof</code> causes shell functions to be profiled. The profiling results can be obtained with the <code>zprof</code> builtin command made available by this module. There is no way to turn profiling off other than unloading the module. </p>
<dl>
<dt>
<dd> <code>zprof</code> [ <code>-c</code> ] Without the <code>-c</code> option, <code>zprof</code> lists profiling results to standard output. The format is comparable to that of commands like <code>gprof</code>.</p>
<dl>
<dt>
<dd>
<p> At the top there is a summary listing all functions that were called at least once. This summary is sorted in decreasing order of the amount of time spent in each. The lines contain the number of the function in order, which is used in other parts of the list in suffixes of the form `<code>[</code><i>num</i><code>]</code>&#8216;, then the number of calls made to the function. The next three columns list the time in milliseconds spent in the function and its descendants, the average time in milliseconds spent in the function and its descendants per call and the percentage of time spent in all shell functions used in this function and its descendants. The following three columns give the same information, but counting only the time spent in the function itself. The final column shows the name of the function. </p>
<p> After the summary, detailed information about every function that was invoked is listed, sorted in decreasing order of the amount of time spent in each function and its descendants. Each of these entries consists of descriptions for the functions that called the function described, the function itself, and the functions that were called from it. The description for the function itself has the same format as in the summary (and shows the same information). The other lines don&#8217;t show the number of the function at the beginning and have their function named indented to make it easier to distinguish the line showing the function described in the section from the surrounding lines. </p>
<p> The information shown in this case is almost the same as in the summary, but only refers to the call hierarchy being displayed. For example, for a calling function the column showing the total running time lists the time spent in the described function and its descendants only for the times when it was called from that particular calling function. Likewise, for a called function, this columns lists the total time spent in the called function and its descendants only for the times when it was called from the function described. </p>
<p> Also in this case, the column showing the number of calls to a function also shows a slash and then the total number of invocations made to the called function. </p>
<p> As long as the <code>zsh/zprof</code> module is loaded, profiling will be done and multiple invocations of the <code>zprof</code> builtin command will show the times and numbers of calls since the module was loaded. With the <code>-c</code> option, the <code>zprof</code> builtin command will reset its internal counters and will not show the listing.</dl>
</dl>
<h2>THE ZSH/ZPTY MODULE</h2>
<p> The <code>zsh/zpty</code> module offers one builtin: </p>
<dl>
<dt>
<dd> <code>zpty</code> [ <code>-e</code> ] [ <code>-b</code> ] <i>name</i> [ <i>arg</i> &#8230; ] The arguments following <i>name</i> are concatenated with spaces between, then executed as a command, as if passed to the <code>eval</code> builtin. The command runs under a newly assigned pseudo-terminal; this is useful for running commands non-interactively which expect an interactive environment. The <i>name</i> is not part of the command, but is used to refer to this command in later calls to <code>zpty</code>.</p>
<dl>
<dt>
<dd>
<p> With the <code>-e</code> option, the pseudo-terminal is set up so that input characters are echoed. </p>
<p> With the <code>-b</code> option, input to and output from the pseudo-terminal are made non-blocking. </p>
<p> The shell parameter <code>REPLY</code> is set to the file descriptor assigned to the master side of the pseudo-terminal. This allows the terminal to be monitored with ZLE descriptor handlers (see <i><a href="/docs/linux/man/1-zshzle/">zshzle</a></i>(1)) or manipulated with <code>sysread</code> and <code>syswrite</code> (see THE ZSH/SYSTEM MODULE in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1)). <i>Warning</i>: Use of <code>sysread</code> and <code>syswrite</code> is <i>not</i> recommended; use <code>zpty -r</code> and <code>zpty -w</code> unless you know exactly what you are doing.</dl>
<dt><code>zpty</code> <code>-d</code> [ <i>name</i> &#8230; ]</p>
<dd> The second form, with the <code>-d</code> option, is used to delete commands previously started, by supplying a list of their <i>name</i>s. If no <i>name</i> is given, all commands are deleted. Deleting a command causes the HUP signal to be sent to the corresponding process.</p>
<dt><code>zpty</code> <code>-w</code> [ <code>-n</code> ] <i>name</i> [ <i>string</i> &#8230; ]</p>
<dd> The <code>-w</code> option can be used to send the to command <i>name</i> the given <i>string</i>s as input (separated by spaces). If the <code>-n</code> option is <i>not</i> given, a newline is added at the end.</p>
<dl>
<dt>
<dd>
<p> If no <i>string</i> is provided, the standard input is copied to the pseudo-terminal; this may stop before copying the full input if the pseudo-terminal is non-blocking. The exact input is always copied: the <code>-n</code> option is not applied. </p>
<p> Note that the command under the pseudo-terminal sees this input as if it were typed, so beware when sending special tty driver characters such as word-erase, line-kill, and end-of-file.</dl>
<dt><code>zpty</code> <code>-r</code> [ <code>-mt</code> ] <i>name</i> [ <i>param</i> [ <i>pattern</i> ] ]</p>
<dd> The <code>-r</code> option can be used to read the output of the command <i>name</i>. With only a <i>name</i> argument, the output read is copied to the standard output. Unless the pseudo-terminal is non-blocking, copying continues until the command under the pseudo-terminal exits; when non-blocking, only as much output as is immediately available is copied. The return status is zero if any output is copied.</p>
<dl>
<dt>
<dd>
<p> When also given a <i>param</i> argument, at most one line is read and stored in the parameter named <i>param</i>. Less than a full line may be read if the pseudo-terminal is non-blocking. The return status is zero if at least one character is stored in <i>param</i>. </p>
<p> If a <i>pattern</i> is given as well, output is read until the whole string read matches the <i>pattern</i>, even in the non-blocking case. The return status is zero if the string read matches the pattern, or if the command has exited but at least one character could still be read. If the option <code>-m</code> is present, the return status is zero only if the pattern matches. As of this writing, a maximum of one megabyte of output can be consumed this way; if a full megabyte is read without matching the pattern, the return status is non-zero. </p>
<p> In all cases, the return status is non-zero if nothing could be read, and is <code>2</code> if this is because the command has finished. </p>
<p> If the <code>-r</code> option is combined with the <code>-t</code> option, <code>zpty</code> tests whether output is available before trying to read. If no output is available, <code>zpty</code> immediately returns the status <code>1</code>. When used with a <i>pattern</i>, the behaviour on a failed poll is similar to when the command has exited: the return value is zero if at least one character could still be read even if the pattern failed to match.</dl>
<dt><code>zpty</code> <code>-t</code> <i>name</i></p>
<dd> The <code>-t</code> option without the <code>-r</code> option can be used to test whether the command <i>name</i> is still running. It returns a zero status if the command is running and a non-zero value otherwise.</p>
<dt><code>zpty</code> [ <code>-L</code> ]</p>
<dd> The last form, without any arguments, is used to list the commands currently defined. If the <code>-L</code> option is given, this is done in the form of calls to the <code>zpty</code> builtin.</dl>
<h2>THE ZSH/ZSELECT MODULE</h2>
<p> The <code>zsh/zselect</code> module makes available one builtin command: </p>
<dl>
<dt>
<dd> <code>zselect</code> [ <code>-rwe</code> ] [ <code>-t</code> <i>timeout</i> ] [ <code>-a</code> <i>array</i> ] [ <code>-A</code> <i>assoc</i> ] [ <i>fd</i> &#8230; ] The <code>zselect</code> builtin is a front-end to the `select&#8217; system call, which blocks until a file descriptor is ready for reading or writing, or has an error condition, with an optional timeout. If this is not available on your system, the command prints an error message and returns status 2 (normal errors return status 1). For more information, see your systems documentation for <i><a href="/docs/linux/man/3-select/">select</a></i>(3). Note there is no connection with the shell builtin of the same name.</p>
<dl>
<dt>
<dd>
<p> Arguments and options may be intermingled in any order. Non-option arguments are file descriptors, which must be decimal integers. By default, file descriptors are to be tested for reading, i.e. <code>zselect</code> will return when data is available to be read from the file descriptor, or more precisely, when a read operation from the file descriptor will not block. After a <code>-r</code>, <code>-w</code> and <code>-e</code>, the given file descriptors are to be tested for reading, writing, or error conditions. These options and an arbitrary list of file descriptors may be given in any order. </p>
<p> (The presence of an `error condition&#8217; is not well defined in the documentation for many implementations of the select system call. According to recent versions of the POSIX specification, it is really an <i>exception</i> condition, of which the only standard example is out-of-band data received on a socket. So zsh users are unlikely to find the <code>-e</code> option useful.) </p>
<p> The option `<code>-t</code> <i>timeout</i>&#8216; specifies a timeout in hundredths of a second. This may be zero, in which case the file descriptors will simply be polled and <code>zselect</code> will return immediately. It is possible to call zselect with no file descriptors and a non-zero timeout for use as a finer-grained replacement for `sleep&#8217;; note, however, the return status is always 1 for a timeout. </p>
<p> The option `<code>-a</code> <i>array</i>&#8216; indicates that <i>array</i> should be set to indicate the file descriptor(s) which are ready. If the option is not given, the array <code>reply</code> will be used for this purpose. The array will contain a string similar to the arguments for <code>zselect</code>. For example, </p>
<dl>
<dt>
<dd>
<pre>
<code>zselect -t 0 -r 0 -w 1</code>
</pre>
</dl>
<p> might return immediately with status 0 and <code>$reply</code> containing `<code>-r 0 -w 1</code>&#8216; to show that both file descriptors are ready for the requested operations. </p>
<p> The option `<code>-A</code> <i>assoc</i>&#8216; indicates that the associative array <i>assoc</i> should be set to indicate the file descriptor(s) which are ready. This option overrides the option <code>-a</code>, nor will <code>reply</code> be modified. The keys of <code>assoc</code> are the file descriptors, and the corresponding values are any of the characters `<code>rwe</code>&#8216; to indicate the condition. </p>
<p> The command returns status 0 if some file descriptors are ready for reading. If the operation timed out, or a timeout of 0 was given and no file descriptors were ready, or there was an error, it returns status 1 and the array will not be set (nor modified in any way). If there was an error in the select operation the appropriate error message is printed.</dl>
</dl>
<h2>THE ZSH/ZUTIL MODULE</h2>
<p> The <code>zsh/zutil</code> module only adds some builtins: </p>
<dl>
<dt>
<dd> <code>zstyle</code> [ <code>-L</code> [ <i>metapattern</i> [ <i>style</i> ] ] ]</p>
<dt>
<dd> <code>zstyle</code> [ <code>-e</code> | <code>&#8211;</code> | <code>&#8211;</code><code>&#8211;</code> ] <i>pattern</i> <i>style</i> <i>string</i> &#8230;</p>
<dt>
<dd> <code>zstyle -d</code> [ <i>pattern</i> [ <i>style</i> &#8230; ] ]</p>
<dt>
<dd> <code>zstyle -g</code> <i>name</i> [ <i>pattern</i> [ <i>style</i> ] ]</p>
<dt>
<dd> <code>zstyle &#8211;</code>{<code>a</code>|<code>b</code>|<code>s</code>} <i>context</i> <i>style</i> <i>name</i> [ <i>sep</i> ]</p>
<dt>
<dd> <code>zstyle &#8211;</code>{<code>T</code>|<code>t</code>} <i>context</i> <i>style</i> [ <i>string</i> &#8230; ]</p>
<dt>
<dd> <code>zstyle -m</code> <i>context</i> <i>style</i> <i>pattern</i> This builtin command is used to define and lookup styles. Styles are pairs of names and values, where the values consist of any number of strings. They are stored together with patterns and lookup is done by giving a string, called the `<i>context</i>&#8216;, which is matched against the patterns. The definition stored for the most specific pattern that matches will be returned.</p>
<dl>
<dt>
<dd>
<p> A pattern is considered to be more specific than another if it contains more components (substrings separated by colons) or if the patterns for the components are more specific, where simple strings are considered to be more specific than patterns and complex patterns are considered to be more specific than the pattern `<code>*</code>&#8216;. A `<code>*</code>&#8216; in the pattern will match zero or more characters in the context; colons are not treated specially in this regard. If two patterns are equally specific, the tie is broken in favour of the pattern that was defined first. </p>
<p> <i>Example</i> </p>
<p> For example, to define your preferred form of precipitation depending on which city you&#8217;re in, you might set the following in your <code>zshrc</code>: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':weather:europe:*' preferred-precipitation rain
zstyle ':weather:europe:germany:* preferred-precipitation none
zstyle ':weather:europe:germany:*:munich' preferred-precipitation snow</code>
</pre>
</dl>
<p> Then, the fictional `<code>weather</code>&#8216; plugin might run under the hood a command such as </p>
<dl>
<dt>
<dd>
<pre><code>
zstyle - s ":weather:${continent}:${country}:${county}:${city}" preferred - precipitation REPLY
</code></pre>
</dl>
<p> in order to retrieve your preference into the scalar variable <code>$REPLY</code>. </p>
<p> <i>Usage</i> </p>
<p> The forms that operate on patterns are the following. </p>
<dl>
<dt>
<dd> <code>zstyle</code> [ <code>-L</code> [ <i>metapattern</i> [ <i>style</i> ] ] ] Without arguments, lists style definitions. Styles are shown in alphabetic order and patterns are shown in the order <code>zstyle</code> will test them.</p>
<dl>
<dt>
<dd>
<p> If the <code>-L</code> option is given, listing is done in the form of calls to <code>zstyle</code>. The optional first argument, <i>metapattern</i>, is a pattern which will be matched against the string supplied as <i>pattern</i> when the style was defined. Note: this means, for example, `<code>zstyle -L &quot;:completion:*&quot;</code>&#8216; will match any supplied pattern beginning `<code>:completion:</code>&#8216;, not just <code>&quot;:completion:*&quot;</code>: use <code>&#8216;:completion:\*&#8217;</code> to match that. The optional second argument limits the output to a specific <i>style</i> (not a pattern). <code>-L</code> is not compatible with any other options.</dl>
<dt><code>zstyle</code> [ <code>&#8211;</code> | <code>&#8211;</code><code>&#8211;</code> | <code>-e</code> ] <i>pattern</i> <i>style</i> <i>string</i> &#8230;</p>
<dd> Defines the given <i>style</i> for the <i>pattern</i> with the <i>string</i>s as the value. If the <code>-e</code> option is given, the <i>string</i>s will be concatenated (separated by spaces) and the resulting string will be evaluated (in the same way as it is done by the <code>eval</code> builtin command) when the style is looked up. In this case the parameter `<code>reply</code>&#8216; must be assigned to set the strings returned after the evaluation. Before evaluating the value, <code>reply</code> is unset, and if it is still unset after the evaluation, the style is treated as if it were not set.</p>
<dt><code>zstyle -d</code> [ <i>pattern</i> [ <i>style</i> &#8230; ] ]</p>
<dd> Delete style definitions. Without arguments all definitions are deleted, with a <i>pattern</i> all definitions for that pattern are deleted and if any <i>style</i>s are given, then only those styles are deleted for the <i>pattern</i>.</p>
<dt><code>zstyle -g</code> <i>name</i> [ <i>pattern</i> [ <i>style</i> ] ]</p>
<dd> Retrieve a style definition. The <i>name</i> is used as the name of an array in which the results are stored. Without any further arguments, all patterns defined are returned. With a <i>pattern</i> the styles defined for that pattern are returned and with both a <i>pattern</i> and a <i>style</i>, the value strings of that combination is returned.</dl>
<p> The other forms can be used to look up or test styles for a given context. </p>
<dl>
<dt>
<dd> <code>zstyle -s</code> <i>context</i> <i>style</i> <i>name</i> [ <i>sep</i> ] The parameter <i>name</i> is set to the value of the style interpreted as a string. If the value contains several strings they are concatenated with spaces (or with the <i>sep</i> string if that is given) between them.</p>
<dl>
<dt>
<dd>
<p> Return <code>0</code> if the style is set, <code>1</code> otherwise.</dl>
<dt><code>zstyle -b</code> <i>context</i> <i>style</i> <i>name</i></p>
<dd> The value is stored in <i>name</i> as a boolean, i.e. as the string `<code>yes</code>&#8216; if the value has only one string and that string is equal to one of `<code>yes</code>&#8216;, `<code>true</code>&#8216;, `<code>on</code>&#8216;, or `<code>1</code>&#8216;. If the value is any other string or has more than one string, the parameter is set to `<code>no</code>&#8216;.</p>
<dl>
<dt>
<dd>
<p> Return <code>0</code> if <i>name</i> is set to `<code>yes</code>&#8216;, <code>1</code> otherwise.</dl>
<dt><code>zstyle -a</code> <i>context</i> <i>style</i> <i>name</i></p>
<dd> The value is stored in <i>name</i> as an array. If <i>name</i> is declared as an associative array, the first, third, etc. strings are used as the keys and the other strings are used as the values.</p>
<dl>
<dt>
<dd>
<p> Return <code>0</code> if the style is set, <code>1</code> otherwise.</dl>
<dt>
<dd> <code>zstyle -t</code> <i>context</i> <i>style</i> [ <i>string</i> &#8230; ]</p>
<dt>
<dd> <code>zstyle -T</code> <i>context</i> <i>style</i> [ <i>string</i> &#8230; ] Test the value of a style, i.e. the <code>-t</code> option only returns a status (sets <code>$?</code>). Without any <i>string</i> the return status is zero if the style is defined for at least one matching pattern, has only one string in its value, and that is equal to one of `<code>true</code>&#8216;, `<code>yes</code>&#8216;, `<code>on</code>&#8216; or `<code>1</code>&#8216;. If any <i>string</i>s are given the status is zero if and only if at least one of the <i>string</i>s is equal to at least one of the strings in the value. If the style is defined but doesn&#8217;t match, the return status is <code>1</code>. If the style is not defined, the status is <code>2</code>.</p>
<dl>
<dt>
<dd>
<p> The <code>-T</code> option tests the values of the style like <code>-t</code>, but it returns status zero (rather than <code>2</code>) if the style is not defined for any matching pattern.</dl>
<dt><code>zstyle -m</code> <i>context</i> <i>style</i> <i>pattern</i></p>
<dd> Match a value. Returns status zero if the <i>pattern</i> matches at least one of the strings in the value.</dl>
</dl>
<dt>
<dd> <code>zformat -f</code> <i>param</i> <i>format</i> <i>spec</i> &#8230;</p>
<dt>
<dd> <code>zformat -a</code> <i>array</i> <i>sep</i> <i>spec</i> &#8230; This builtin provides two different forms of formatting. The first form is selected with the <code>-f</code> option. In this case the <i>format</i> string will be modified by replacing sequences starting with a percent sign in it with strings from the <i>spec</i>s. Each <i>spec</i> should be of the form `<i>char</i><code>:</code><i>string</i>&#8216; which will cause every appearance of the sequence `<code>%</code><i>char</i>&#8216; in <i>format</i> to be replaced by the <i>string</i>. The `<code>%</code>&#8216; sequence may also contain optional minimum and maximum field width specifications between the `<code>%</code>&#8216; and the `<i>char</i>&#8216; in the form `<code>%</code><i>min</i><code>.</code><i>max</i><code>c</code>&#8216;, i.e. the minimum field width is given first and if the maximum field width is used, it has to be preceded by a dot. Specifying a minimum field width makes the result be padded with spaces to the right if the <i>string</i> is shorter than the requested width. Padding to the left can be achieved by giving a negative minimum field width. If a maximum field width is specified, the <i>string</i> will be truncated after that many characters. After all `<code>%</code>&#8216; sequences for the given <i>spec</i>s have been processed, the resulting string is stored in the parameter <i>param</i>.</p>
<dl>
<dt>
<dd>
<p> The <code>%</code>-escapes also understand ternary expressions in the form used by prompts. The <code>%</code> is followed by a `<code>(</code>&#8216; and then an ordinary format specifier character as described above. There may be a set of digits either before or after the `<code>(</code>&#8216;; these specify a test number, which defaults to zero. Negative numbers are also allowed. An arbitrary delimiter character follows the format specifier, which is followed by a piece of `true&#8217; text, the delimiter character again, a piece of `false&#8217; text, and a closing parenthesis. The complete expression (without the digits) thus looks like `<code>%(</code><i>X</i><code>.</code><i>text1</i><code>.</code><i>text2</i><code>)</code>&#8216;, except that the `<code>.</code>&#8216; character is arbitrary. The value given for the format specifier in the <i>char</i><code>:</code><i>string</i> expressions is evaluated as a mathematical expression, and compared with the test number. If they are the same, <i>text1</i> is output, else <i>text2</i> is output. A parenthesis may be escaped in <i>text2</i> as <code>%)</code>. Either of <i>text1</i> or <i>text2</i> may contain nested <code>%</code>-escapes. </p>
<p> For example: </p>
<dl>
<dt>
<dd>
<pre>
<code>zformat -f REPLY &quot;The answer is '%3(c.yes.no)'.&quot; c:3</code>
</pre>
</dl>
<p> outputs &quot;The answer is &#8216;yes&#8217;.&quot; to <code>REPLY</code> since the value for the format specifier <code>c</code> is 3, agreeing with the digit argument to the ternary expression. </p>
<p> The second form, using the <code>-a</code> option, can be used for aligning strings. Here, the <i>spec</i>s are of the form `<i>left</i><code>:</code><i>right</i>&#8216; where `<i>left</i>&#8216; and `<i>right</i>&#8216; are arbitrary strings. These strings are modified by replacing the colons by the <i>sep</i> string and padding the <i>left</i> strings with spaces to the right so that the <i>sep</i> strings in the result (and hence the <i>right</i> strings after them) are all aligned if the strings are printed below each other. All strings without a colon are left unchanged and all strings with an empty <i>right</i> string have the trailing colon removed. In both cases the lengths of the strings are not used to determine how the other strings are to be aligned. A colon in the <i>left</i> string can be escaped with a backslash. The resulting strings are stored in the <i>array</i>.</dl>
<dt><code>zregexparse</code></p>
<dd> This implements some internals of the <code>_regex_arguments</code> function.</p>
<dt><code>zparseopts</code> [ <code>-D</code> <code>-E</code> <code>-F</code> <code>-K</code> <code>-M</code> ] [ <code>-a</code> <i>array</i> ] [ <code>-A</code> <i>assoc</i> ] [ <code>&#8211;</code> ] <i>spec</i> &#8230;</p>
<dd> This builtin simplifies the parsing of options in positional parameters, i.e. the set of arguments given by <code>$*</code>. Each <i>spec</i> describes one option and must be of the form `<i>opt</i>[<code>=</code><i>array</i>]&#8217;. If an option described by <i>opt</i> is found in the positional parameters it is copied into the <i>array</i> specified with the <code>-a</code> option; if the optional `<code>=</code><i>array</i>&#8216; is given, it is instead copied into that array, which should be declared as a normal array and never as an associative array.</p>
<dl>
<dt>
<dd>
<p> Note that it is an error to give any <i>spec</i> without an `<code>=</code><i>array</i>&#8216; unless one of the <code>-a</code> or <code>-A</code> options is used. </p>
<p> Unless the <code>-E</code> option is given, parsing stops at the first string that isn&#8217;t described by one of the <i>spec</i>s. Even with <code>-E</code>, parsing always stops at a positional parameter equal to `<code>&#8211;</code>&#8216; or `<code>&#8211;</code><code>&#8211;</code>&#8216;. See also <code>-F</code>. </p>
<p> The <i>opt</i> description must be one of the following. Any of the special characters can appear in the option name provided it is preceded by a backslash. </p>
<dl>
<dt>
<dd> <i>name</i></p>
<dt>
<dd> <i>name</i><code>+</code> The <i>name</i> is the name of the option without the leading `<code>&#8211;</code>&#8216;. To specify a GNU-style long option, one of the usual two leading `<code>&#8211;</code>&#8216; must be included in <i>name</i>; for example, a `<code>&#8211;</code><code>-file</code>&#8216; option is represented by a <i>name</i> of `<code>-file</code>&#8216;.</p>
<dl>
<dt>
<dd>
<p> If a `<code>+</code>&#8216; appears after <i>name</i>, the option is appended to <i>array</i> each time it is found in the positional parameters; without the `<code>+</code>&#8216; only the <i>last</i> occurrence of the option is preserved. </p>
<p> If one of these forms is used, the option takes no argument, so parsing stops if the next positional parameter does not also begin with `<code>&#8211;</code>&#8216; (unless the <code>-E</code> option is used).</dl>
<dt>
<dd> <i>name</i><code>:</code></p>
<dt>
<dd> <i>name</i><code>:-</code></p>
<dt>
<dd> <i>name</i><code>::</code> If one or two colons are given, the option takes an argument; with one colon, the argument is mandatory and with two colons it is optional. The argument is appended to the <i>array</i> after the option itself.</p>
<dl>
<dt>
<dd>
<p> An optional argument is put into the same array element as the option name (note that this makes empty strings as arguments indistinguishable). A mandatory argument is added as a separate element unless the `<code>:-</code>&#8216; form is used, in which case the argument is put into the same element. </p>
<p> A `<code>+</code>&#8216; as described above may appear between the <i>name</i> and the first colon.</dl>
</dl>
<p> In all cases, option-arguments must appear either immediately following the option in the same positional parameter or in the next one. Even an optional argument may appear in the next parameter, unless it begins with a `<code>&#8211;</code>&#8216;. There is no special handling of `<code>=</code>&#8216; as with GNU-style argument parsers; given the <i>spec</i> `<code>-foo:</code>&#8216;, the positional parameter `<code>&#8211;</code><code>-foo=bar</code>&#8216; is parsed as `<code>&#8211;</code><code>-foo</code>&#8216; with an argument of `<code>=bar</code>&#8216;. </p>
<p> When the names of two options that take no arguments overlap, the longest one wins, so that parsing for the <i>spec</i>s `<code>-foo -foobar</code>&#8216; (for example) is unambiguous. However, due to the aforementioned handling of option-arguments, ambiguities may arise when at least one overlapping <i>spec</i> takes an argument, as in `<code>-foo: -foobar</code>&#8216;. In that case, the last matching <i>spec</i> wins. </p>
<p> The options of <code>zparseopts</code> itself cannot be stacked because, for example, the stack `<code>-DEK</code>&#8216; is indistinguishable from a <i>spec</i> for the GNU-style long option `<code>&#8211;</code><code>-DEK</code>&#8216;. The options of <code>zparseopts</code> itself are: </p>
<dl>
<dt>
<dd> <code>-a</code> <i>array</i> As described above, this names the default array in which to store the recognised options.</p>
<dt><code>-A</code> <i>assoc</i></p>
<dd> If this is given, the options and their values are also put into an associative array with the option names as keys and the arguments (if any) as the values.</p>
<dt><code>-D</code></p>
<dd> If this option is given, all options found are removed from the positional parameters of the calling shell or shell function, up to but not including any not described by the <i>spec</i>s. If the first such parameter is `<code>&#8211;</code>&#8216; or `<code>&#8211;</code><code>&#8211;</code>&#8216;, it is removed as well. This is similar to using the <code>shift</code> builtin.</p>
<dt><code>-E</code></p>
<dd> This changes the parsing rules to <i>not</i> stop at the first string that isn&#8217;t described by one of the <i>spec</i>s. It can be used to test for or (if used together with <code>-D</code>) extract options and their arguments, ignoring all other options and arguments that may be in the positional parameters. As indicated above, parsing still stops at the first `<code>&#8211;</code>&#8216; or `<code>&#8211;</code><code>&#8211;</code>&#8216; not described by a <i>spec</i>, but it is not removed when used with <code>-D</code>.</p>
<dt><code>-F</code></p>
<dd> If this option is given, <code>zparseopts</code> immediately stops at the first option-like parameter not described by one of the <i>spec</i>s, prints an error message, and returns status 1. Removal (<code>-D</code>) and extraction (<code>-E</code>) are not performed, and option arrays are not updated. This provides basic validation for the given options.</p>
<dl>
<dt>
<dd>
<p> Note that the appearance in the positional parameters of an option without its required argument always aborts parsing and returns an error as described above regardless of whether this option is used.</dl>
<dt><code>-K</code></p>
<dd> With this option, the arrays specified with the <code>-a</code> option and with the `<code>=</code><i>array</i>&#8216; forms are kept unchanged when none of the <i>spec</i>s for them is used. Otherwise the entire array is replaced when any of the <i>spec</i>s is used. Individual elements of associative arrays specified with the <code>-A</code> option are preserved by <code>-K</code>. This allows assignment of default values to arrays before calling <code>zparseopts</code>.</p>
<dt><code>-M</code></p>
<dd> This changes the assignment rules to implement a map among equivalent option names. If any <i>spec</i> uses the `<code>=</code><i>array</i>&#8216; form, the string <i>array</i> is interpreted as the name of another <i>spec</i>, which is used to choose where to store the values. If no other <i>spec</i> is found, the values are stored as usual. This changes only the way the values are stored, not the way <code>$*</code> is parsed, so results may be unpredictable if the `<i>name</i><code>+</code>&#8216; specifier is used inconsistently.</dl>
<p> For example, </p>
<dl>
<dt>
<dd>
<pre>
<code>set -- -a -bx -c y -cz baz -cend
zparseopts a=foo b:=bar c+:=bar</code>
</pre>
</dl>
<p> will have the effect of </p>
<dl>
<dt>
<dd>
<pre>
<code>foo=(-a)
bar=(-b x -c y -c z)</code>
</pre>
</dl>
<p> The arguments from `<code>baz</code>&#8216; on will not be used. </p>
<p> As an example for the <code>-E</code> option, consider: </p>
<dl>
<dt>
<dd>
<pre>
<code>set -- -a x -b y -c z arg1 arg2
zparseopts -E -D b:=bar</code>
</pre>
</dl>
<p> will have the effect of </p>
<dl>
<dt>
<dd>
<pre>
<code>bar=(-b y)
set -- -a x -c z arg1 arg2</code>
</pre>
</dl>
<p> I.e., the option <code>-b</code> and its arguments are taken from the positional parameters and put into the array <code>bar</code>. </p>
<p> The <code>-M</code> option can be used like this: </p>
<dl>
<dt>
<dd>
<pre>
<code>set -- -a -bx -c y -cz baz -cend
zparseopts -A bar -M a=foo b+: c:=b</code>
</pre>
</dl>
<p> to have the effect of </p>
<dl>
<dt>
<dd>
<pre>
<code>foo=(-a)
bar=(-a '' -b xyz)</code>
</pre>
</dl>
</dl>
</dl>
<h2>Index</h2>
