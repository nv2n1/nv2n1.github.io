---
title: "zshall(1)"
name: "zshall"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zshall/"
description: "zshall – the Z shell meta-man page"
---

<h2 class="name">NAME</h2>
<p> zshall &#8211; the Z shell meta-man page </p>
<h2>OVERVIEW</h2>
<p> Because zsh contains many features, the zsh manual has been split into a number of sections. This manual page includes all the separate manual pages in the following order: </p>
<dl>
<dt><i>zsh</i> Zsh overview</p>
<dd>
<dt><i>zshroadmap</i> Informal introduction to the manual</p>
<dd>
<dt><i>zshmisc</i> Anything not fitting into the other sections</p>
<dd>
<dt><i>zshexpn</i> Zsh command and parameter expansion</p>
<dd>
<dt><i>zshparam</i> Zsh parameters</p>
<dd>
<dt><i>zshoptions</i> Zsh options</p>
<dd>
<dt><i>zshbuiltins</i> Zsh built-in functions</p>
<dd>
<dt><i>zshzle</i> Zsh command line editing</p>
<dd>
<dt><i>zshcompwid</i> Zsh completion widgets</p>
<dd>
<dt><i>zshcompsys</i> Zsh completion system</p>
<dd>
<dt><i>zshcompctl</i> Zsh completion control</p>
<dd>
<dt><i>zshmodules</i> Zsh loadable modules</p>
<dd>
<dt><i>zshcalsys</i> Zsh built-in calendar functions</p>
<dd>
<dt><i>zshtcpsys</i> Zsh built-in TCP functions</p>
<dd>
<dt><i>zshzftpsys</i> Zsh built-in FTP client</p>
<dd>
<dt><i>zshcontrib</i> Additional zsh functions and utilities</p>
<dd></dl>
<h2>DESCRIPTION</h2>
<p> Zsh is a UNIX command interpreter (shell) usable as an interactive login shell and as a shell script command processor. Of the standard shells, zsh most closely resembles <code>ksh</code> but includes many enhancements. It does not provide compatibility with POSIX or other shells in its default operating mode: see the section Compatibility below. </p>
<p> Zsh has command line editing, builtin spelling correction, programmable command completion, shell functions (with autoloading), a history mechanism, and a host of other features.</p>
<h2>AUTHOR</h2>
<p> Zsh was originally written by Paul Falstad <code>&lt;pf [at] zsh.org&gt;</code>. Zsh is now maintained by the members of the zsh-workers mailing list <code>&lt;zsh-workers [at] zsh.org&gt;</code>. The development is currently coordinated by Peter Stephenson <code>&lt;pws [at] zsh.org&gt;</code>. The coordinator can be contacted at <code>&lt;coordinator [at] zsh.org&gt;</code>, but matters relating to the code should generally go to the mailing list.</p>
<h2>AVAILABILITY</h2>
<p> Zsh is available from the following HTTP and anonymous FTP site. </p>
<pre>
<code><a href="ftp://ftp.zsh.org/pub/">ftp://ftp.zsh.org/pub/</a></code>
<code><a rel="nofollow" href="https://www.zsh.org/pub/">https://www.zsh.org/pub/</a></code>
</pre>
<p> ) </p>
<p> The up-to-date source code is available via Git from Sourceforge. See <code><a rel="nofollow" href="https://sourceforge.net/projects/zsh/">https://sourceforge.net/projects/zsh/</a></code> for details. A summary of instructions for the archive can be found at <code><a rel="nofollow" href="http://zsh.sourceforge.net/">http://zsh.sourceforge.net/</a></code>. </p>
<h2>MAILING LISTS</h2>
<p> Zsh has 3 mailing lists: </p>
<dl>
<dt>
<dd> <code>&lt;zsh-announce [at] zsh.org&gt;</code> Announcements about releases, major changes in the shell and the monthly posting of the Zsh FAQ. (moderated)</p>
<dt><code>&lt;zsh-users [at] zsh.org&gt;</code></p>
<dd> User discussions.</p>
<dt><code>&lt;zsh-workers [at] zsh.org&gt;</code></p>
<dd> Hacking, development, bug reports and patches.</dl>
<p> To subscribe or unsubscribe, send mail to the associated administrative address for the mailing list. </p>
<dl>
<dt><code>&lt;zsh-announce-subscribe [at] zsh.org&gt;</code></p>
<dd>
<dt><code>&lt;zsh-users-subscribe [at] zsh.org&gt;</code></p>
<dd>
<dt><code>&lt;zsh-workers-subscribe [at] zsh.org&gt;</code></p>
<dd></dl>
<dl>
<dt><code>&lt;zsh-announce-unsubscribe [at] zsh.org&gt;</code></p>
<dd>
<dt><code>&lt;zsh-users-unsubscribe [at] zsh.org&gt;</code></p>
<dd>
<dt><code>&lt;zsh-workers-unsubscribe [at] zsh.org&gt;</code></p>
<dd></dl>
<p> YOU ONLY NEED TO JOIN ONE OF THE MAILING LISTS AS THEY ARE NESTED. All submissions to <code>zsh-announce</code> are automatically forwarded to <code>zsh-users</code>. All submissions to <code>zsh-users</code> are automatically forwarded to <code>zsh-workers</code>. </p>
<p> If you have problems subscribing/unsubscribing to any of the mailing lists, send mail to <code>&lt;listmaster [at] zsh.org&gt;</code>. The mailing lists are maintained by Karsten Thygesen <code>&lt;karthy [at] kom.auc.dk&gt;</code>. </p>
<p> The mailing lists are archived; the archives can be accessed via the administrative addresses listed above. There is also a hypertext archive, maintained by Geoff Wing <code>&lt;gcw [at] zsh.org&gt;</code>, available at <code><a rel="nofollow" href="https://www.zsh.org/mla/">https://www.zsh.org/mla/</a></code>.</p>
<h2>THE ZSH FAQ</h2>
<p> Zsh has a list of Frequently Asked Questions (FAQ), maintained by Peter Stephenson <code>&lt;pws [at] zsh.org&gt;</code>. It is regularly posted to the newsgroup <code>comp.unix.shell</code> and the <code>zsh-announce</code> mailing list. The latest version can be found at any of the Zsh FTP sites, or at <code><a rel="nofollow" href="http://www.zsh.org/FAQ/">http://www.zsh.org/FAQ/</a></code>. The contact address for FAQ-related matters is <code>&lt;faqmaster [at] zsh.org&gt;</code>.</p>
<h2>THE ZSH WEB PAGE</h2>
<p> Zsh has a web page which is located at <code><a rel="nofollow" href="https://www.zsh.org/">https://www.zsh.org/</a></code>. This is maintained by Karsten Thygesen <code>&lt;karthy [at] zsh.org&gt;</code>, of SunSITE Denmark. The contact address for web-related matters is <code>&lt;webmaster [at] zsh.org&gt;</code>.</p>
<h2>THE ZSH USERGUIDE</h2>
<p> A userguide is currently in preparation. It is intended to complement the manual, with explanations and hints on issues where the manual can be cabbalistic, hierographic, or downright mystifying (for example, the word `hierographic&#8217; does not exist). It can be viewed in its current state at <code><a rel="nofollow" href="http://zsh.sourceforge.net/Guide/">http://zsh.sourceforge.net/Guide/</a></code>. At the time of writing, chapters dealing with startup files and their contents and the new completion system were essentially complete.</p>
<h2>INVOCATION</h2>
<p> The following flags are interpreted by the shell when invoked to determine where the shell will read commands from: </p>
<dl>
<dt>
<dd> <code>-c</code> Take the first argument as a command to execute, rather than reading commands from a script or standard input. If any further arguments are given, the first one is assigned to <code>$0</code>, rather than being used as a positional parameter.</p>
<dt><code>-i</code></p>
<dd> Force shell to be interactive. It is still possible to specify a script to execute.</p>
<dt><code>-s</code></p>
<dd> Force shell to read commands from the standard input. If the <code>-s</code> flag is not present and an argument is given, the first argument is taken to be the pathname of a script to execute.</dl>
<p> If there are any remaining arguments after option processing, and neither of the options <code>-c</code> or <code>-s</code> was supplied, the first argument is taken as the file name of a script containing shell commands to be executed. If the option <code>PATH_SCRIPT</code> is set, and the file name does not contain a directory path (i.e. there is no `<code>/</code>&#8216; in the name), first the current directory and then the command path given by the variable <code>PATH</code> are searched for the script. If the option is not set or the file name contains a `<code>/</code>&#8216; it is used directly. </p>
<p> After the first one or two arguments have been appropriated as described above, the remaining arguments are assigned to the positional parameters. </p>
<p> For further options, which are common to invocation and the <code>set</code> builtin, see <i><a href="/docs/linux/man/1-zshoptions/">zshoptions</a></i>(1). </p>
<p> The long option `<code>&#8211;</code><code>-emulate</code>&#8216; followed (in a separate word) by an emulation mode may be passed to the shell. The emulation modes are those described for the <code>emulate</code> builtin, see <i><a href="/docs/linux/man/1-zshbuiltins/">zshbuiltins</a></i>(1). The `<code>&#8211;</code><code>-emulate</code>&#8216; option must precede any other options (which might otherwise be overridden), but following options are honoured, so may be used to modify the requested emulation mode. Note that certain extra steps are taken to ensure a smooth emulation when this option is used compared with the <code>emulate</code> command within the shell: for example, variables that conflict with POSIX usage such as <code>path</code> are not defined within the shell. </p>
<p> Options may be specified by name using the <code>-o</code> option. <code>-o</code> acts like a single-letter option, but takes a following string as the option name. For example, </p>
<dl>
<dt>
<dd>
<pre>
<code>zsh -x -o shwordsplit scr</code>
</pre>
</dl>
<p> runs the script <code>scr</code>, setting the <code>XTRACE</code> option by the corresponding letter `<code>-x</code>&#8216; and the <code>SH_WORD_SPLIT</code> option by name. Options may be turned <i>off</i> by name by using <code>+o</code> instead of <code>-o</code>. <code>-o</code> can be stacked up with preceding single-letter options, so for example `<code>-xo shwordsplit</code>&#8216; or `<code>-xoshwordsplit</code>&#8216; is equivalent to `<code>-x -o shwordsplit</code>&#8216;. </p>
<p> Options may also be specified by name in GNU long option style, `<code>&#8211;</code><code>&#8211;</code><i>option-name</i>&#8216;. When this is done, `<code>&#8211;</code>&#8216; characters in the option name are permitted: they are translated into `<code>_</code>&#8216;, and thus ignored. So, for example, `<code>zsh &#8211;</code><code>-sh-word-split</code>&#8216; invokes zsh with the <code>SH_WORD_SPLIT</code> option turned on. Like other option syntaxes, options can be turned off by replacing the initial `<code>&#8211;</code>&#8216; with a `<code>+</code>&#8216;; thus `<code>+-sh-word-split</code>&#8216; is equivalent to `<code>&#8211;</code><code>-no-sh-word-split</code>&#8216;. Unlike other option syntaxes, GNU-style long options cannot be stacked with any other options, so for example `<code>-x-shwordsplit</code>&#8216; is an error, rather than being treated like `<code>-x &#8211;</code><code>-shwordsplit</code>&#8216;. </p>
<p> The special GNU-style option `<code>&#8211;</code><code>-version</code>&#8216; is handled; it sends to standard output the shell&#8217;s version information, then exits successfully. `<code>&#8211;</code><code>-help</code>&#8216; is also handled; it sends to standard output a list of options that can be used when invoking the shell, then exits successfully. </p>
<p> Option processing may be finished, allowing following arguments that start with `<code>&#8211;</code>&#8216; or `<code>+</code>&#8216; to be treated as normal arguments, in two ways. Firstly, a lone `<code>&#8211;</code>&#8216; (or `<code>+</code>&#8216;) as an argument by itself ends option processing. Secondly, a special option `<code>&#8211;</code><code>&#8211;</code>&#8216; (or `<code>+-</code>&#8216;), which may be specified on its own (which is the standard POSIX usage) or may be stacked with preceding options (so `<code>-x-</code>&#8216; is equivalent to `<code>-x &#8211;</code><code>&#8211;</code>&#8216;). Options are not permitted to be stacked after `<code>&#8211;</code><code>&#8211;</code>&#8216; (so `<code>-x-f</code>&#8216; is an error), but note the GNU-style option form discussed above, where `<code>&#8211;</code><code>-shwordsplit</code>&#8216; is permitted and does not end option processing. </p>
<p> Except when the <code>sh</code>/<code>ksh</code> emulation single-letter options are in effect, the option `<code>-b</code>&#8216; (or `<code>+b</code>&#8216;) ends option processing. `<code>-b</code>&#8216; is like `<code>&#8211;</code><code>&#8211;</code>&#8216;, except that further single-letter options can be stacked after the `<code>-b</code>&#8216; and will take effect as normal. </p>
<h2>COMPATIBILITY</h2>
<p> Zsh tries to emulate <code>sh</code> or <code>ksh</code> when it is invoked as <code>sh</code> or <code>ksh</code> respectively; more precisely, it looks at the first letter of the name by which it was invoked, excluding any initial `<code>r</code>&#8216; (assumed to stand for `restricted&#8217;), and if that is `<code>b</code>&#8216;, `<code>s</code>&#8216; or `<code>k</code>&#8216; it will emulate <code>sh</code> or <code>ksh</code>. Furthermore, if invoked as <code>su</code> (which happens on certain systems when the shell is executed by the <code>su</code> command), the shell will try to find an alternative name from the <code>SHELL</code> environment variable and perform emulation based on that. </p>
<p> In <code>sh</code> and <code>ksh</code> compatibility modes the following parameters are not special and not initialized by the shell: <code>ARGC</code>, <code>argv</code>, <code>cdpath</code>, <code>fignore</code>, <code>fpath</code>, <code>HISTCHARS</code>, <code>mailpath</code>, <code>MANPATH</code>, <code>manpath</code>, <code>path</code>, <code>prompt</code>, <code>PROMPT</code>, <code>PROMPT2</code>, <code>PROMPT3</code>, <code>PROMPT4</code>, <code>psvar</code>, <code>status</code>, <code>watch</code>. </p>
<p> The usual zsh startup/shutdown scripts are not executed. Login shells source <code>/etc/profile</code> followed by <code>$HOME/.profile</code>. If the <code>ENV</code> environment variable is set on invocation, <code>$ENV</code> is sourced after the profile scripts. The value of <code>ENV</code> is subjected to parameter expansion, command substitution, and arithmetic expansion before being interpreted as a pathname. Note that the <code>PRIVILEGED</code> option also affects the execution of startup files. </p>
<p> The following options are set if the shell is invoked as <code>sh</code> or <code>ksh</code>: <code>NO_BAD_PATTERN</code>, <code>NO_BANG_HIST</code>, <code>NO_BG_NICE</code>, <code>NO_EQUALS</code>, <code>NO_FUNCTION_ARGZERO</code>, <code>GLOB_SUBST</code>, <code>NO_GLOBAL_EXPORT</code>, <code>NO_HUP</code>, <code>INTERACTIVE_COMMENTS</code>, <code>KSH_ARRAYS</code>, <code>NO_MULTIOS</code>, <code>NO_NOMATCH</code>, <code>NO_NOTIFY</code>, <code>POSIX_BUILTINS</code>, <code>NO_PROMPT_PERCENT</code>, <code>RM_STAR_SILENT</code>, <code>SH_FILE_EXPANSION</code>, <code>SH_GLOB</code>, <code>SH_OPTION_LETTERS</code>, <code>SH_WORD_SPLIT</code>. Additionally the <code>BSD_ECHO</code> and <code>IGNORE_BRACES</code> options are set if zsh is invoked as <code>sh</code>. Also, the <code>KSH_OPTION_PRINT</code>, <code>LOCAL_OPTIONS</code>, <code>PROMPT_BANG</code>, <code>PROMPT_SUBST</code> and <code>SINGLE_LINE_ZLE</code> options are set if zsh is invoked as <code>ksh</code>.</p>
<h2>RESTRICTED SHELL</h2>
<p> When the basename of the command used to invoke zsh starts with the letter `<code>r</code>&#8216; or the `<code>-r</code>&#8216; command line option is supplied at invocation, the shell becomes restricted. Emulation mode is determined after stripping the letter `<code>r</code>&#8216; from the invocation name. The following are disabled in restricted mode: </p>
<dl>
<dt>
<dd> &bull; changing directories with the <code>cd</code> builtin</p>
<dt>&bull;</p>
<dd> changing or unsetting the <code>EGID</code>, <code>EUID</code>, <code>GID</code>, <code>HISTFILE</code>, <code>HISTSIZE</code>, <code>IFS</code>, <code>LD_AOUT_LIBRARY_PATH</code>, <code>LD_AOUT_PRELOAD</code>, <code>LD_LIBRARY_PATH</code>, <code>LD_PRELOAD</code>, <code>MODULE_PATH</code>, <code>module_path</code>, <code>PATH</code>, <code>path</code>, <code>SHELL</code>, <code>UID</code> and <code>USERNAME</code> parameters</p>
<dt>&bull;</p>
<dd> specifying command names containing <code>/</code></p>
<dt>&bull;</p>
<dd> specifying command pathnames using <code>hash</code></p>
<dt>&bull;</p>
<dd> redirecting output to files</p>
<dt>&bull;</p>
<dd> using the <code>exec</code> builtin command to replace the shell with another command</p>
<dt>&bull;</p>
<dd> using <code>jobs -Z</code> to overwrite the shell process&#8217; argument and environment space</p>
<dt>&bull;</p>
<dd> using the <code>ARGV0</code> parameter to override <code>argv[0]</code> for external commands</p>
<dt>&bull;</p>
<dd> turning off restricted mode with <code>set +r</code> or <code>unsetopt RESTRICTED</code></dl>
<p> These restrictions are enforced after processing the startup files. The startup files should set up <code>PATH</code> to point to a directory of commands which can be safely invoked in the restricted environment. They may also add further restrictions by disabling selected builtins. </p>
<p> Restricted mode can also be activated any time by setting the <code>RESTRICTED</code> option. This immediately enables all the restrictions described above even if the shell still has not processed all startup files. </p>
<p> A shell <i>Restricted Mode</i> is an outdated way to restrict what users may do: modern systems have better, safer and more reliable ways to confine user actions, such as <i>chroot jails</i>, <i>containers</i> and <i>zones</i>. </p>
<p> A restricted shell is very difficult to implement safely. The feature may be removed in a future version of zsh. </p>
<p> It is important to realise that the restrictions only apply to the shell, not to the commands it runs (except for some shell builtins). While a restricted shell can only run the restricted list of commands accessible via the predefined `<code>PATH</code>&#8216; variable, it does not prevent those commands from running any other command. </p>
<p> As an example, if `<code>env</code>&#8216; is among the list of <i>allowed</i> commands, then it allows the user to run any command as `<code>env</code>&#8216; is not a shell builtin command and can run arbitrary executables. </p>
<p> So when implementing a restricted shell framework it is important to be fully aware of what actions each of the <i>allowed</i> commands or features (which may be regarded as <i>modules</i>) can perform. </p>
<p> Many commands can have their behaviour affected by environment variables. Except for the few listed above, zsh does not restrict the setting of environment variables. </p>
<p> If a `<code>perl</code>&#8216;, `<code>python</code>&#8216;, `<code>bash</code>&#8216;, or other general purpose interpreted script it treated as a restricted command, the user can work around the restriction by setting specially crafted `<code>PERL5LIB</code>&#8216;, `<code>PYTHONPATH</code>&#8216;, `<code>BASHENV</code>&#8216; (etc.) environment variables. On GNU systems, any command can be made to run arbitrary code when performing character set conversion (including zsh itself) by setting a `<code>GCONV_PATH</code>&#8216; environment variable. Those are only a few examples. </p>
<p> Bear in mind that, contrary to some other shells, `<code>readonly</code>&#8216; is not a security feature in zsh as it can be undone and so cannot be used to mitigate the above. </p>
<p> A restricted shell only works if the allowed commands are few and carefully written so as not to grant more access to users than intended. It is also important to restrict what zsh module the user may load as some of them, such as `<code>zsh/system</code>&#8216;, `<code>zsh/mapfile</code>&#8216; and `<code>zsh/files</code>&#8216;, allow bypassing most of the restrictions.</p>
<h2>STARTUP/SHUTDOWN FILES</h2>
<p> Commands are first read from <code>/etc/zsh/zshenv</code>; this cannot be overridden. Subsequent behaviour is modified by the <code>RCS</code> and <code>GLOBAL_RCS</code> options; the former affects all startup files, while the second only affects global startup files (those shown here with an path starting with a <code>/</code>). If one of the options is unset at any point, any subsequent startup file(s) of the corresponding type will not be read. It is also possible for a file in <code>$ZDOTDIR</code> to re-enable <code>GLOBAL_RCS</code>. Both <code>RCS</code> and <code>GLOBAL_RCS</code> are set by default. </p>
<p> Commands are then read from <code>$ZDOTDIR/.zshenv</code>. If the shell is a login shell, commands are read from <code>/etc/zsh/zprofile</code> and then <code>$ZDOTDIR/.zprofile</code>. Then, if the shell is interactive, commands are read from <code>/etc/zsh/zshrc</code> and then <code>$ZDOTDIR/.zshrc</code>. Finally, if the shell is a login shell, <code>/etc/zsh/zlogin</code> and <code>$ZDOTDIR/.zlogin</code> are read. </p>
<p> When a login shell exits, the files <code>$ZDOTDIR/.zlogout</code> and then <code>/etc/zsh/zlogout</code> are read. This happens with either an explicit exit via the <code>exit</code> or <code>logout</code> commands, or an implicit exit by reading end-of-file from the terminal. However, if the shell terminates due to <code>exec</code>&#8216;ing another process, the logout files are not read. These are also affected by the <code>RCS</code> and <code>GLOBAL_RCS</code> options. Note also that the <code>RCS</code> option affects the saving of history files, i.e. if <code>RCS</code> is unset when the shell exits, no history file will be saved. </p>
<p> If <code>ZDOTDIR</code> is unset, <code>HOME</code> is used instead. Files listed above as being in <code>/etc</code> may be in another directory, depending on the installation. </p>
<p> As <code>/etc/zsh/zshenv</code> is run for all instances of zsh, it is important that it be kept as small as possible. In particular, it is a good idea to put code that does not need to be run for every single shell behind a test of the form `<code>if [[ -o rcs ]]; then &#8230;</code>&#8216; so that it will not be executed when zsh is invoked with the `<code>-f</code>&#8216; option. </p>
<p> Any of these files may be pre-compiled with the <code>zcompile</code> builtin command (see <i><a href="/docs/linux/man/1-zshbuiltins/">zshbuiltins</a></i>(1)). If a compiled file exists (named for the original file plus the <code>.zwc</code> extension) and it is newer than the original file, the compiled file will be used instead.</p>
<h2>FILES</h2>
<dl>
<dt><code>$ZDOTDIR/.zshenv</code></p>
<dd>
<dt><code>$ZDOTDIR/.zprofile</code></p>
<dd>
<dt><code>$ZDOTDIR/.zshrc</code></p>
<dd>
<dt><code>$ZDOTDIR/.zlogin</code></p>
<dd>
<dt><code>$ZDOTDIR/.zlogout</code></p>
<dd>
<dt><code>${TMPPREFIX}*</code> (default is /tmp/zsh*)</p>
<dd>
<dt><code>/etc/zsh/zshenv</code></p>
<dd>
<dt><code>/etc/zsh/zprofile</code></p>
<dd>
<dt><code>/etc/zsh/zshrc</code></p>
<dd>
<dt><code>/etc/zsh/zlogin</code></p>
<dd>
<dt><code>/etc/zsh/zlogout</code> (installation-specific &#8211; <code>/etc</code> is the default)</p>
<dd></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1), <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1), <i><a href="/docs/linux/man/1-tcsh/">tcsh</a></i>(1), <i><a href="/docs/linux/man/1-rc/">rc</a></i>(1), <i><a href="/docs/linux/man/1-bash/">bash</a></i>(1), <i><a href="/docs/linux/man/1-ksh/">ksh</a></i>(1) </p>
<p> <code>IEEE Standard for information Technology &#8211; Portable Operating System Interface (POSIX) &#8211; Part 2: Shell and Utilities</code>, IEEE Inc, 1993, ISBN 1-55937-255-9. </p>
<h2>Index</h2>
