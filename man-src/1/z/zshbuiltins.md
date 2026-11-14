---
title: "zshbuiltins(1)"
name: "zshbuiltins"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zshbuiltins/"
description: "zshbuiltins – zsh built-in commands"
---

<h2 class="name">NAME</h2>
<p> zshbuiltins &#8211; zsh built-in commands </p>
<h2>SHELL BUILTIN COMMANDS</h2>
<p> Some shell builtin commands take options as described in individual entries; these are often referred to in the list below as `<code>flags</code>&#8216; to avoid confusion with shell options, which may also have an effect on the behaviour of builtin commands. In this introductory section, `<code>option</code>&#8216; always has the meaning of an option to a command that should be familiar to most command line users. </p>
<p> Typically, options are single letters preceded by a hyphen (<code>&#8211;</code>). Options that take an argument accept it either immediately following the option letter or after white space, for example `<code>print -C3 {1..9}</code>&#8216; or `<code>print -C 3 {1..9}</code>&#8216; are equivalent. Arguments to options are not the same as arguments to the command; the documentation indicates which is which. Options that do not take an argument may be combined in a single word, for example `<code>print -rca &#8212; *</code>&#8216; and `<code>print -r -c -a &#8212; *</code>&#8216; are equivalent. </p>
<p> Some shell builtin commands also take options that begin with `<code>+</code>&#8216; instead of `<code>&#8211;</code>&#8216;. The list below makes clear which commands these are. </p>
<p> Options (together with their individual arguments, if any) must appear in a group before any non-option arguments; once the first non-option argument has been found, option processing is terminated. </p>
<p> All builtin commands other than `<code>echo</code>&#8216; and precommand modifiers, even those that have no options, can be given the argument `<code>&#8211;</code><code>&#8211;</code>&#8216; to terminate option processing. This indicates that the following words are non-option arguments, but is otherwise ignored. This is useful in cases where arguments to the command may begin with `<code>&#8211;</code>&#8216;. For historical reasons, most builtin commands (including `<code>echo</code>&#8216;) also recognize a single `<code>&#8211;</code>&#8216; in a separate word for this purpose; note that this is less standard and use of `<code>&#8211;</code><code>&#8211;</code>&#8216; is recommended. </p>
<dl>
<dt>
<dd> <code>&#8211;</code> <i>simple command</i> See the section `Precommand Modifiers&#8217; in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1).</p>
<dt><code>.</code> <i>file</i> [ <i>arg</i> &#8230; ]</p>
<dd> Read commands from <i>file</i> and execute them in the current shell environment.</p>
<dl>
<dt>
<dd>
<p> If <i>file</i> does not contain a slash, or if <code>PATH_DIRS</code> is set, the shell looks in the components of <code>$path</code> to find the directory containing <i>file</i>. Files in the current directory are not read unless `<code>.</code>&#8216; appears somewhere in <code>$path</code>. If a file named `<i>file</i><code>.zwc</code>&#8216; is found, is newer than <i>file</i>, and is the compiled form (created with the <code>zcompile</code> builtin) of <i>file</i>, then commands are read from that file instead of <i>file</i>. </p>
<p> If any arguments <i>arg</i> are given, they become the positional parameters; the old positional parameters are restored when the <i>file</i> is done executing. However, if no arguments are given, the positional parameters remain those of the calling context, and no restoring is done. </p>
<p> If <i>file</i> was not found the return status is 127; if <i>file</i> was found but contained a syntax error the return status is 126; else the return status is the exit status of the last command executed.</dl>
<dt><code>:</code> [ <i>arg</i> &#8230; ]</p>
<dd> This command does nothing, although normal argument expansions is performed which may have effects on shell parameters. A zero exit status is returned.</p>
<dt><code>alias</code> [ {<code>+</code>|<code>&#8211;</code>}<code>gmrsL</code> ] [ <i>name</i>[<code>=</code><i>value</i>] &#8230; ]</p>
<dd> For each <i>name</i> with a corresponding <i>value</i>, define an alias with that value. A trailing space in <i>value</i> causes the next word to be checked for alias expansion. If the <code>-g</code> flag is present, define a global alias; global aliases are expanded even if they do not occur in command position.</p>
<dl>
<dt>
<dd>
<p> If the <code>-s</code> flag is present, define a suffix alias: if the command word on a command line is in the form `<i>text</i><code>.</code><i>name</i>&#8216;, where <i>text</i> is any non-empty string, it is replaced by the text `<i>value</i> <i>text</i><code>.</code><i>name</i>&#8216;. Note that <i>name</i> is treated as a literal string, not a pattern. A trailing space in <i>value</i> is not special in this case. For example, </p>
<dl>
<dt>
<dd>
<pre>
<code>alias -s ps='gv --'</code>
</pre>
</dl>
<p> will cause the command `<code>*.ps</code>&#8216; to be expanded to `<code>gv &#8212; *.ps</code>&#8216;. As alias expansion is carried out earlier than globbing, the `<code>*.ps</code>&#8216; will then be expanded. Suffix aliases constitute a different name space from other aliases (so in the above example it is still possible to create an alias for the command <code>ps</code>) and the two sets are never listed together. </p>
<p> For each <i>name</i> with no <i>value</i>, print the value of <i>name</i>, if any. With no arguments, print all currently defined aliases other than suffix aliases. If the <code>-m</code> flag is given the arguments are taken as patterns (they should be quoted to preserve them from being interpreted as glob patterns), and the aliases matching these patterns are printed. When printing aliases and one of the <code>-g</code>, <code>-r</code> or <code>-s</code> flags is present, restrict the printing to global, regular or suffix aliases, respectively; a regular alias is one which is neither a global nor a suffix alias. Using `<code>+</code>&#8216; instead of `<code>&#8211;</code>&#8216;, or ending the option list with a single `<code>+</code>&#8216;, prevents the values of the aliases from being printed. </p>
<p> If the <code>-L</code> flag is present, then print each alias in a manner suitable for putting in a startup script. The exit status is nonzero if a <i>name</i> (with no <i>value</i>) is given for which no alias has been defined. </p>
<p> For more on aliases, include common problems, see the section ALIASING in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1).</dl>
<dt><code>autoload</code> [ {<code>+</code>|<code>&#8211;</code>}<code>RTUXdkmrtWz</code> ] [ <code>-w</code> ] [ <i>name</i> &#8230; ]</p>
<dd> See the section `Autoloading Functions&#8217; in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1) for full details. The <code>fpath</code> parameter will be searched to find the function definition when the function is first referenced.</p>
<dl>
<dt>
<dd>
<p> If <i>name</i> consists of an absolute path, the function is defined to load from the file given (searching as usual for dump files in the given location). The name of the function is the basename (non-directory part) of the file. It is normally an error if the function is not found in the given location; however, if the option <code>-d</code> is given, searching for the function defaults to <code>$fpath</code>. If a function is loaded by absolute path, any functions loaded from it that are marked for <code>autoload</code> without an absolute path have the load path of the parent function temporarily prepended to <code>$fpath</code>. </p>
<p> If the option <code>-r</code> or <code>-R</code> is given, the function is searched for immediately and the location is recorded internally for use when the function is executed; a relative path is expanded using the value of <code>$PWD</code>. This protects against a change to <code>$fpath</code> after the call to <code>autoload</code>. With <code>-r</code>, if the function is not found, it is silently left unresolved until execution; with <code>-R</code>, an error message is printed and command processing aborted immediately the search fails, i.e. at the <code>autoload</code> command rather than at function execution.. </p>
<p> The flag <code>-X</code> may be used only inside a shell function. It causes the calling function to be marked for autoloading and then immediately loaded and executed, with the current array of positional parameters as arguments. This replaces the previous definition of the function. If no function definition is found, an error is printed and the function remains undefined and marked for autoloading. If an argument is given, it is used as a directory (i.e. it does not include the name of the function) in which the function is to be found; this may be combined with the <code>-d</code> option to allow the function search to default to <code>$fpath</code> if it is not in the given location. </p>
<p> The flag <code>+X</code> attempts to load each <i>name</i> as an autoloaded function, but does <i>not</i> execute it. The exit status is zero (success) if the function was not previously defined <i>and</i> a definition for it was found. This does <i>not</i> replace any existing definition of the function. The exit status is nonzero (failure) if the function was already defined or when no definition was found. In the latter case the function remains undefined and marked for autoloading. If ksh-style autoloading is enabled, the function created will contain the contents of the file plus a call to the function itself appended to it, thus giving normal ksh autoloading behaviour on the first call to the function. If the <code>-m</code> flag is also given each <i>name</i> is treated as a pattern and all functions already marked for autoload that match the pattern are loaded. </p>
<p> With the <code>-t</code> flag, turn on execution tracing; with <code>-T</code>, turn on execution tracing only for the current function, turning it off on entry to any called functions that do not also have tracing enabled. </p>
<p> With the <code>-U</code> flag, alias expansion is suppressed when the function is loaded. </p>
<p> With the <code>-w</code> flag, the <i>name</i>s are taken as names of files compiled with the <code>zcompile</code> builtin, and all functions defined in them are marked for autoloading. </p>
<p> The flags <code>-z</code> and <code>-k</code> mark the function to be autoloaded using the zsh or ksh style, as if the option <code>KSH_AUTOLOAD</code> were unset or were set, respectively. The flags override the setting of the option at the time the function is loaded. </p>
<p> Note that the <code>autoload</code> command makes no attempt to ensure the shell options set during the loading or execution of the file have any particular value. For this, the <code>emulate</code> command can be used: </p>
<dl>
<dt>
<dd>
<pre>
<code>emulate zsh -c 'autoload -Uz </code><i>func</i>'
</pre>
</dl>
<p> arranges that when <i>func</i> is loaded the shell is in native <code>zsh</code> emulation, and this emulation is also applied when <i>func</i> is run. </p>
<p> Some of the functions of <code>autoload</code> are also provided by <code>functions -u</code> or <code>functions -U</code>, but <code>autoload</code> is a more comprehensive interface.</dl>
<dt>
<dd> <code>bg</code> [ <i>job</i> &#8230; ]</p>
<dt>
<dd> <i>job</i> &#8230; <code>&amp;</code> Put each specified <i>job</i> in the background, or the current job if none is specified.</p>
<dt><code>bindkey</code></p>
<dd> See the section `Zle Builtins&#8217; in <i><a href="/docs/linux/man/1-zshzle/">zshzle</a></i>(1).</p>
<dt><code>break</code> [ <i>n</i> ]</p>
<dd> Exit from an enclosing <code>for</code>, <code>while</code>, <code>until</code>, <code>select</code> or <code>repeat</code> loop. If an arithmetic expression <i>n</i> is specified, then break <i>n</i> levels instead of just one.</p>
<dt><code>builtin</code> <i>name</i> [ <i>args</i> &#8230; ]</p>
<dd> Executes the builtin <i>name</i>, with the given <i>args</i>.</p>
<dt><code>bye</code></p>
<dd> Same as <code>exit</code>.</p>
<dt><code>cap</code></p>
<dd> See the section `The zsh/cap Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1).</p>
<dt>
<dd> <code>cd</code> [ <code>-qsLP</code> ] [ <i>arg</i> ]</p>
<dt>
<dd> <code>cd</code> [ <code>-qsLP</code> ] <i>old</i> <i>new</i></p>
<dt>
<dd> <code>cd</code> [ <code>-qsLP</code> ] {<code>+</code>|<code>&#8211;</code>}<i>n</i> Change the current directory. In the first form, change the current directory to <i>arg</i>, or to the value of <code>$HOME</code> if <i>arg</i> is not specified. If <i>arg</i> is `<code>&#8211;</code>&#8216;, change to the previous directory.</p>
<dl>
<dt>
<dd>
<p> Otherwise, if <i>arg</i> begins with a slash, attempt to change to the directory given by <i>arg</i>. </p>
<p> If <i>arg</i> does not begin with a slash, the behaviour depends on whether the current directory `<code>.</code>&#8216; occurs in the list of directories contained in the shell parameter <code>cdpath</code>. If it does not, first attempt to change to the directory <i>arg</i> under the current directory, and if that fails but <code>cdpath</code> is set and contains at least one element attempt to change to the directory <i>arg</i> under each component of <code>cdpath</code> in turn until successful. If `<code>.</code>&#8216; occurs in <code>cdpath</code>, then <code>cdpath</code> is searched strictly in order so that `<code>.</code>&#8216; is only tried at the appropriate point. </p>
<p> The order of testing <code>cdpath</code> is modified if the option <code>POSIX_CD</code> is set, as described in the documentation for the option. </p>
<p> If no directory is found, the option <code>CDABLE_VARS</code> is set, and a parameter named <i>arg</i> exists whose value begins with a slash, treat its value as the directory. In that case, the parameter is added to the named directory hash table. </p>
<p> The second form of <code>cd</code> substitutes the string <i>new</i> for the string <i>old</i> in the name of the current directory, and tries to change to this new directory. </p>
<p> The third form of <code>cd</code> extracts an entry from the directory stack, and changes to that directory. An argument of the form `<code>+</code><i>n</i>&#8216; identifies a stack entry by counting from the left of the list shown by the <code>dirs</code> command, starting with zero. An argument of the form `<code>&#8211;</code><i>n</i>&#8216; counts from the right. If the <code>PUSHD_MINUS</code> option is set, the meanings of `<code>+</code>&#8216; and `<code>&#8211;</code>&#8216; in this context are swapped. If the <code>POSIX_CD</code> option is set, this form of <code>cd</code> is not recognised and will be interpreted as the first form. </p>
<p> If the <code>-q</code> (quiet) option is specified, the hook function <code>chpwd</code> and the functions in the array <code>chpwd_functions</code> are not called. This is useful for calls to <code>cd</code> that do not change the environment seen by an interactive user. </p>
<p> If the <code>-s</code> option is specified, <code>cd</code> refuses to change the current directory if the given pathname contains symlinks. If the <code>-P</code> option is given or the <code>CHASE_LINKS</code> option is set, symbolic links are resolved to their true values. If the <code>-L</code> option is given symbolic links are retained in the directory (and not resolved) regardless of the state of the <code>CHASE_LINKS</code> option.</dl>
<dt><code>chdir</code></p>
<dd> Same as <code>cd</code>.</p>
<dt><code>clone</code></p>
<dd> See the section `The zsh/clone Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1).</p>
<dt><code>command</code> [ <code>-pvV</code> ] <i>simple command</i></p>
<dd> The simple command argument is taken as an external command instead of a function or builtin and is executed. If the <code>POSIX_BUILTINS</code> option is set, builtins will also be executed but certain special properties of them are suppressed. The <code>-p</code> flag causes a default path to be searched instead of that in <code>$path</code>. With the <code>-v</code> flag, <code>command</code> is similar to <code>whence</code> and with <code>-V</code>, it is equivalent to <code>whence -v</code>.</p>
<dl>
<dt>
<dd>
<p> See also the section `Precommand Modifiers&#8217; in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1).</dl>
<dt><code>comparguments</code></p>
<dd> See the section `The zsh/computil Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1).</p>
<dt><code>compcall</code></p>
<dd> See the section `The zsh/compctl Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1).</p>
<dt><code>compctl</code></p>
<dd> See the section `The zsh/compctl Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1).</p>
<dt><code>compdescribe</code></p>
<dd> See the section `The zsh/computil Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1).</p>
<dt><code>compfiles</code></p>
<dd> See the section `The zsh/computil Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1).</p>
<dt><code>compgroups</code></p>
<dd> See the section `The zsh/computil Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1).</p>
<dt><code>compquote</code></p>
<dd> See the section `The zsh/computil Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1).</p>
<dt><code>comptags</code></p>
<dd> See the section `The zsh/computil Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1).</p>
<dt><code>comptry</code></p>
<dd> See the section `The zsh/computil Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1).</p>
<dt><code>compvalues</code></p>
<dd> See the section `The zsh/computil Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1).</p>
<dt><code>continue</code> [ <i>n</i> ]</p>
<dd> Resume the next iteration of the enclosing <code>for</code>, <code>while</code>, <code>until</code>, <code>select</code> or <code>repeat</code> loop. If an arithmetic expression <i>n</i> is specified, break out of <i>n</i>-1 loops and resume at the <i>n</i>th enclosing loop.</p>
<dt><code>declare</code></p>
<dd> Same as <code>typeset</code>.</p>
<dt>
<dd> <code>dirs</code> [ <code>-c</code> ] [ <i>arg</i> &#8230; ]</p>
<dt>
<dd> <code>dirs</code> [ <code>-lpv</code> ] With no arguments, print the contents of the directory stack. Directories are added to this stack with the <code>pushd</code> command, and removed with the <code>cd</code> or <code>popd</code> commands. If arguments are specified, load them onto the directory stack, replacing anything that was there, and push the current directory onto the stack.</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>-c</code> clear the directory stack.</p>
<dt><code>-l</code></p>
<dd> print directory names in full instead of using of using <code>~</code> expressions (see <i>Dynamic</i> and <i>Static named directories</i> in <i><a href="/docs/linux/man/1-zshexpn/">zshexpn</a></i>(1)).</p>
<dt><code>-p</code></p>
<dd> print directory entries one per line.</p>
<dt><code>-v</code></p>
<dd> number the directories in the stack when printing.</dl>
</dl>
<dt><code>disable</code> [ <code>-afmprs</code> ] <i>name</i> &#8230;</p>
<dd> Temporarily disable the <i>name</i>d hash table elements or patterns. The default is to disable builtin commands. This allows you to use an external command with the same name as a builtin command. The <code>-a</code> option causes <code>disable</code> to act on regular or global aliases. The <code>-s</code> option causes <code>disable</code> to act on suffix aliases. The <code>-f</code> option causes <code>disable</code> to act on shell functions. The <code>-r</code> options causes <code>disable</code> to act on reserved words. Without arguments all disabled hash table elements from the corresponding hash table are printed. With the <code>-m</code> flag the arguments are taken as patterns (which should be quoted to prevent them from undergoing filename expansion), and all hash table elements from the corresponding hash table matching these patterns are disabled. Disabled objects can be enabled with the <code>enable</code> command.</p>
<dl>
<dt>
<dd>
<p> With the option <code>-p</code>, <i>name</i> &#8230; refer to elements of the shell&#8217;s pattern syntax as described in the section `Filename Generation&#8217;. Certain elements can be disabled separately, as given below. </p>
<p> Note that patterns not allowed by the current settings for the options <code>EXTENDED_GLOB</code>, <code>KSH_GLOB</code> and <code>SH_GLOB</code> are never enabled, regardless of the setting here. For example, if <code>EXTENDED_GLOB</code> is not active, the pattern <code>^</code> is ineffective even if `<code>disable -p &quot;^&quot;</code>&#8216; has not been issued. The list below indicates any option settings that restrict the use of the pattern. It should be noted that setting <code>SH_GLOB</code> has a wider effect than merely disabling patterns as certain expressions, in particular those involving parentheses, are parsed differently. </p>
<p> The following patterns may be disabled; all the strings need quoting on the command line to prevent them from being interpreted immediately as patterns and the patterns are shown below in single quotes as a reminder. </p>
<dl>
<dt>
<dd> <code>&#8216;?&#8217;</code> The pattern character <code>?</code> wherever it occurs, including when preceding a parenthesis with <code>KSH_GLOB</code>.</p>
<dt><code>&#8216;*&#8217;</code></p>
<dd> The pattern character <code>*</code> wherever it occurs, including recursive globbing and when preceding a parenthesis with <code>KSH_GLOB</code>.</p>
<dt><code>&#8216;[&#8216;</code></p>
<dd> Character classes.</p>
<dt><code>&#8216;&lt;&#8216;</code> (<code>NO_SH_GLOB</code>)</p>
<dd> Numeric ranges.</p>
<dt><code>&#8216;|&#8217;</code> (<code>NO_SH_GLOB</code>)</p>
<dd> Alternation in grouped patterns, case statements, or KSH_GLOB parenthesised expressions.</p>
<dt><code>&#8216;(&#8216;</code> (<code>NO_SH_GLOB</code>)</p>
<dd> Grouping using single parentheses. Disabling this does not disable the use of parentheses for <code>KSH_GLOB</code> where they are introduced by a special character, nor for glob qualifiers (use `<code>setopt NO_BARE_GLOB_QUAL</code>&#8216; to disable glob qualifiers that use parentheses only).</p>
<dt><code>&#8216;~&#8217;</code> (<code>EXTENDED_GLOB</code>)</p>
<dd> Exclusion in the form <i>A</i><code>~</code><i>B</i>.</p>
<dt><code>&#8216;^&#8217;</code> (<code>EXTENDED_GLOB</code>)</p>
<dd> Exclusion in the form <i>A</i><code>^</code><i>B</i>.</p>
<dt><code>&#8216;#&#8217;</code> (<code>EXTENDED_GLOB</code>)</p>
<dd> The pattern character <code>#</code> wherever it occurs, both for repetition of a previous pattern and for indicating globbing flags.</p>
<dt><code>&#8216;?(&#8216;</code> (<code>KSH_GLOB</code>)</p>
<dd> The grouping form <code>?(</code><i>&#8230;</i><code>)</code>. Note this is also disabled if <code>&#8216;?&#8217;</code> is disabled.</p>
<dt><code>&#8216;*(&#8216;</code> (<code>KSH_GLOB</code>)</p>
<dd> The grouping form <code>*(</code><i>&#8230;</i><code>)</code>. Note this is also disabled if <code>&#8216;*&#8217;</code> is disabled.</p>
<dt><code>&#8216;+(&#8216;</code> (<code>KSH_GLOB</code>)</p>
<dd> The grouping form <code>+(</code><i>&#8230;</i><code>)</code>.</p>
<dt><code>&#8216;!(&#8216;</code> (<code>KSH_GLOB</code>)</p>
<dd> The grouping form <code>!(</code><i>&#8230;</i><code>)</code>.</p>
<dt><code>&#8216;@(&#8216;</code> (<code>KSH_GLOB</code>)</p>
<dd> The grouping form <code>@(</code><i>&#8230;</i><code>)</code>.</dl>
</dl>
<dt>
<dd> <code>disown</code> [ <i>job</i> &#8230; ]</p>
<dt>
<dd> <i>job</i> &#8230; <code>&amp;|</code></p>
<dt>
<dd> <i>job</i> &#8230; <code>&amp;!</code> Remove the specified <i>job</i>s from the job table; the shell will no longer report their status, and will not complain if you try to exit an interactive shell with them running or stopped. If no <i>job</i> is specified, disown the current job.</p>
<dl>
<dt>
<dd>
<p> If the <i>job</i>s are currently stopped and the <code>AUTO_CONTINUE</code> option is not set, a warning is printed containing information about how to make them running after they have been disowned. If one of the latter two forms is used, the <i>job</i>s will automatically be made running, independent of the setting of the <code>AUTO_CONTINUE</code> option.</dl>
<dt><code>echo</code> [ <code>-neE</code> ] [ <i>arg</i> &#8230; ]</p>
<dd> Write each <i>arg</i> on the standard output, with a space separating each one. If the <code>-n</code> flag is not present, print a newline at the end. <code>echo</code> recognizes the following escape sequences:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code></code></p>
<dd> bell character</p>
<dt><code></code></p>
<dd> backspace</p>
<dt><code>
