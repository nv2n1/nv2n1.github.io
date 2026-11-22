---

title: "zshbuiltins(1)"
name: "zshbuiltins"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zshbuiltins/"
description: "zshbuiltins – zsh built-in commands"
---

<p> zshbuiltins - zsh built-in commands </p>
<h2>SHELL BUILTIN COMMANDS</h2>
<p> Some shell builtin commands take options as described in individual entries; these are often referred to in the list below as `<code>flags</code>&#8216; to avoid confusion with shell options, which may also have an effect on the behaviour of builtin commands. In this introductory section, `<code>option</code>&#8216; always has the meaning of an option to a command that should be familiar to most command line users. </p>
<p> Typically, options are single letters preceded by a hyphen (<code>-</code>). Options that take an argument accept it either immediately following the option letter or after white space, for example `<code>print -C3 {1..9}</code>&#8216; or `<code>print -C 3 {1..9}</code>&#8216; are equivalent. Arguments to options are not the same as arguments to the command; the documentation indicates which is which. Options that do not take an argument may be combined in a single word, for example `<code>print -rca -- *</code>&#8216; and `<code>print -r -c -a -- *</code>&#8216; are equivalent. </p>
<p> Some shell builtin commands also take options that begin with `<code>+</code>&#8216; instead of `<code>-</code>&#8216;. The list below makes clear which commands these are. </p>
<p> Options (together with their individual arguments, if any) must appear in a group before any non-option arguments; once the first non-option argument has been found, option processing is terminated. </p>
<p> All builtin commands other than `<code>echo</code>&#8216; and precommand modifiers, even those that have no options, can be given the argument `<code>-</code><code>-</code>&#8216; to terminate option processing. This indicates that the following words are non-option arguments, but is otherwise ignored. This is useful in cases where arguments to the command may begin with `<code>-</code>&#8216;. For historical reasons, most builtin commands (including `<code>echo</code>&#8216;) also recognize a single `<code>-</code>&#8216; in a separate word for this purpose; note that this is less standard and use of `<code>-</code><code>-</code>&#8216; is recommended. </p>
<dl>
<dd> <p> <code>-</code> <i>simple command</i> See the section `Precommand Modifiers&#8217; in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1). </p>
 </dd>
<dt><code>.</code><i>file</i> [ <i>arg</i> ... ]</dt>
<dd> <p> Read commands from <i>file</i> and execute them in the current shell environment. </p>
 </dd>
<dl>
<dd> <p> If <i>file</i> does not contain a slash, or if <code>PATH_DIRS</code> is set, the shell looks in the components of <code>$path</code> to find the directory containing <i>file</i>. Files in the current directory are not read unless `<code>.</code>&#8216; appears somewhere in <code>$path</code>. If a file named `<i>file</i><code>.zwc</code>&#8216; is found, is newer than <i>file</i>, and is the compiled form (created with the <code>zcompile</code> builtin) of <i>file</i>, then commands are read from that file instead of <i>file</i>. </p>
<p> If any arguments <i>arg</i> are given, they become the positional parameters; the old positional parameters are restored when the <i>file</i> is done executing. However, if no arguments are given, the positional parameters remain those of the calling context, and no restoring is done. </p>
<p> If <i>file</i> was not found the return status is 127; if <i>file</i> was found but contained a syntax error the return status is 126; else the return status is the exit status of the last command executed. </p>
 </dd></dl>
<dt><code>:</code> [ <i>arg</i> ... ]</dt>
<dd> <p> This command does nothing, although normal argument expansions is performed which may have effects on shell parameters. A zero exit status is returned. </p>
 </dd>
<dt><code>alias</code> [ {<code>+</code>|<code>-</code>}<code>gmrsL</code> ] [ <i>name</i>[<code>=</code><i>value</i>] ... ]</dt>
<dd> <p> For each <i>name</i> with a corresponding <i>value</i>, define an alias with that value. A trailing space in <i>value</i> causes the next word to be checked for alias expansion. If the <code>-g</code> flag is present, define a global alias; global aliases are expanded even if they do not occur in command position. </p>
 </dd>
<dl>
<dd> <p> If the <code>-s</code> flag is present, define a suffix alias: if the command word on a command line is in the form `<i>text</i><code>.</code><i>name</i>&#8216;, where <i>text</i> is any non-empty string, it is replaced by the text `<i>value</i> <i>text</i><code>.</code><i>name</i>&#8216;. Note that <i>name</i> is treated as a literal string, not a pattern. A trailing space in <i>value</i> is not special in this case. For example, </p>
 </dd>
<dl>
<dd> <pre><code>
 alias -s ps='gv --' 
</code></pre>
 </dd></dl>
<p> will cause the command `<code>*.ps</code>&#8216; to be expanded to `<code>gv -- *.ps</code>&#8216;. As alias expansion is carried out earlier than globbing, the `<code>*.ps</code>&#8216; will then be expanded. Suffix aliases constitute a different name space from other aliases (so in the above example it is still possible to create an alias for the command <code>ps</code>) and the two sets are never listed together. </p>
<p> For each <i>name</i> with no <i>value</i>, print the value of <i>name</i>, if any. With no arguments, print all currently defined aliases other than suffix aliases. If the <code>-m</code> flag is given the arguments are taken as patterns (they should be quoted to preserve them from being interpreted as glob patterns), and the aliases matching these patterns are printed. When printing aliases and one of the <code>-g</code>, <code>-r</code> or <code>-s</code> flags is present, restrict the printing to global, regular or suffix aliases, respectively; a regular alias is one which is neither a global nor a suffix alias. Using `<code>+</code>&#8216; instead of `<code>-</code>&#8216;, or ending the option list with a single `<code>+</code>&#8216;, prevents the values of the aliases from being printed. </p>
<p> If the <code>-L</code> flag is present, then print each alias in a manner suitable for putting in a startup script. The exit status is nonzero if a <i>name</i> (with no <i>value</i>) is given for which no alias has been defined. </p>
<p> For more on aliases, include common problems, see the section ALIASING in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1). </dl>
 </p>
<dt><code>autoload</code> [ {<code>+</code>|<code>-</code>}<code>RTUXdkmrtWz</code> ] [ <code>-w</code> ] [ <i>name</i> ... ]</dt>
<dd> <p> See the section `Autoloading Functions&#8217; in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1) for full details. The <code>fpath</code> parameter will be searched to find the function definition when the function is first referenced. </p>
 </dd>
<dl>
<dd> <p> If <i>name</i> consists of an absolute path, the function is defined to load from the file given (searching as usual for dump files in the given location). The name of the function is the basename (non-directory part) of the file. It is normally an error if the function is not found in the given location; however, if the option <code>-d</code> is given, searching for the function defaults to <code>$fpath</code>. If a function is loaded by absolute path, any functions loaded from it that are marked for <code>autoload</code> without an absolute path have the load path of the parent function temporarily prepended to <code>$fpath</code>. </p>
<p> If the option <code>-r</code> or <code>-R</code> is given, the function is searched for immediately and the location is recorded internally for use when the function is executed; a relative path is expanded using the value of <code>$PWD</code>. This protects against a change to <code>$fpath</code> after the call to <code>autoload</code>. With <code>-r</code>, if the function is not found, it is silently left unresolved until execution; with <code>-R</code>, an error message is printed and command processing aborted immediately the search fails, i.e. at the <code>autoload</code> command rather than at function execution.. </p>
<p> The flag <code>-X</code> may be used only inside a shell function. It causes the calling function to be marked for autoloading and then immediately loaded and executed, with the current array of positional parameters as arguments. This replaces the previous definition of the function. If no function definition is found, an error is printed and the function remains undefined and marked for autoloading. If an argument is given, it is used as a directory (i.e. it does not include the name of the function) in which the function is to be found; this may be combined with the <code>-d</code> option to allow the function search to default to <code>$fpath</code> if it is not in the given location. </p>
<p> The flag <code>+X</code> attempts to load each <i>name</i> as an autoloaded function, but does <i>not</i> execute it. The exit status is zero (success) if the function was not previously defined <i>and</i> a definition for it was found. This does <i>not</i> replace any existing definition of the function. The exit status is nonzero (failure) if the function was already defined or when no definition was found. In the latter case the function remains undefined and marked for autoloading. If ksh-style autoloading is enabled, the function created will contain the contents of the file plus a call to the function itself appended to it, thus giving normal ksh autoloading behaviour on the first call to the function. If the <code>-m</code> flag is also given each <i>name</i> is treated as a pattern and all functions already marked for autoload that match the pattern are loaded. </p>
<p> With the <code>-t</code> flag, turn on execution tracing; with <code>-T</code>, turn on execution tracing only for the current function, turning it off on entry to any called functions that do not also have tracing enabled. </p>
<p> With the <code>-U</code> flag, alias expansion is suppressed when the function is loaded. </p>
<p> With the <code>-w</code> flag, the <i>name</i>s are taken as names of files compiled with the <code>zcompile</code> builtin, and all functions defined in them are marked for autoloading. </p>
<p> The flags <code>-z</code> and <code>-k</code> mark the function to be autoloaded using the zsh or ksh style, as if the option <code>KSH_AUTOLOAD</code> were unset or were set, respectively. The flags override the setting of the option at the time the function is loaded. </p>
<p> Note that the <code>autoload</code> command makes no attempt to ensure the shell options set during the loading or execution of the file have any particular value. For this, the <code>emulate</code> command can be used: </p>
 </dd>
<dl>
<dd> <pre><code>
 emulate zsh -c 'autoload -Uz  func '
</code></pre>
 </dd></dl>
<p> arranges that when <i>func</i> is loaded the shell is in native <code>zsh</code> emulation, and this emulation is also applied when <i>func</i> is run. </p>
<p> Some of the functions of <code>autoload</code> are also provided by <code>functions -u</code> or <code>functions -U</code>, but <code>autoload</code> is a more comprehensive interface. </dl>
 </p>
<dd> <p> <code>bg</code> [ <i>job</i> ... ] </p>
 </dd>
<dd> <p> <i>job</i> ... <code>&amp;</code> Put each specified <i>job</i> in the background, or the current job if none is specified. </p>
 </dd>
<dt><code>bindkey</code></dt>
<dd> <p> See the section `Zle Builtins&#8217; in <i><a href="/docs/linux/man/1-zshzle/">zshzle</a></i>(1). </p>
 </dd>
<dt><code>break</code> [ <i>n</i> ]</dt>
<dd> <p> Exit from an enclosing <code>for</code>, <code>while</code>, <code>until</code>, <code>select</code> or <code>repeat</code> loop. If an arithmetic expression <i>n</i> is specified, then break <i>n</i> levels instead of just one. </p>
 </dd>
<dt><code>builtin</code><i>name</i> [ <i>args</i> ... ]</dt>
<dd> <p> Executes the builtin <i>name</i>, with the given <i>args</i>. </p>
 </dd>
<dt><code>bye</code></dt>
<dd> <p> Same as <code>exit</code>. </p>
 </dd>
<dt><code>cap</code></dt>
<dd> <p> See the section `The zsh/cap Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dd> <p> <code>cd</code> [ <code>-qsLP</code> ] [ <i>arg</i> ] </p>
 </dd>
<dd> <p> <code>cd</code> [ <code>-qsLP</code> ] <i>old</i> <i>new</i> </p>
 </dd>
<dd> <p> <code>cd</code> [ <code>-qsLP</code> ] {<code>+</code>|<code>-</code>}<i>n</i> Change the current directory. In the first form, change the current directory to <i>arg</i>, or to the value of <code>$HOME</code> if <i>arg</i> is not specified. If <i>arg</i> is `<code>-</code>&#8216;, change to the previous directory. </p>
 </dd>
<dl>
<dd> <p> Otherwise, if <i>arg</i> begins with a slash, attempt to change to the directory given by <i>arg</i>. </p>
<p> If <i>arg</i> does not begin with a slash, the behaviour depends on whether the current directory `<code>.</code>&#8216; occurs in the list of directories contained in the shell parameter <code>cdpath</code>. If it does not, first attempt to change to the directory <i>arg</i> under the current directory, and if that fails but <code>cdpath</code> is set and contains at least one element attempt to change to the directory <i>arg</i> under each component of <code>cdpath</code> in turn until successful. If `<code>.</code>&#8216; occurs in <code>cdpath</code>, then <code>cdpath</code> is searched strictly in order so that `<code>.</code>&#8216; is only tried at the appropriate point. </p>
<p> The order of testing <code>cdpath</code> is modified if the option <code>POSIX_CD</code> is set, as described in the documentation for the option. </p>
<p> If no directory is found, the option <code>CDABLE_VARS</code> is set, and a parameter named <i>arg</i> exists whose value begins with a slash, treat its value as the directory. In that case, the parameter is added to the named directory hash table. </p>
<p> The second form of <code>cd</code> substitutes the string <i>new</i> for the string <i>old</i> in the name of the current directory, and tries to change to this new directory. </p>
<p> The third form of <code>cd</code> extracts an entry from the directory stack, and changes to that directory. An argument of the form `<code>+</code><i>n</i>&#8216; identifies a stack entry by counting from the left of the list shown by the <code>dirs</code> command, starting with zero. An argument of the form `<code>-</code><i>n</i>&#8216; counts from the right. If the <code>PUSHD_MINUS</code> option is set, the meanings of `<code>+</code>&#8216; and `<code>-</code>&#8216; in this context are swapped. If the <code>POSIX_CD</code> option is set, this form of <code>cd</code> is not recognised and will be interpreted as the first form. </p>
<p> If the <code>-q</code> (quiet) option is specified, the hook function <code>chpwd</code> and the functions in the array <code>chpwd_functions</code> are not called. This is useful for calls to <code>cd</code> that do not change the environment seen by an interactive user. </p>
<p> If the <code>-s</code> option is specified, <code>cd</code> refuses to change the current directory if the given pathname contains symlinks. If the <code>-P</code> option is given or the <code>CHASE_LINKS</code> option is set, symbolic links are resolved to their true values. If the <code>-L</code> option is given symbolic links are retained in the directory (and not resolved) regardless of the state of the <code>CHASE_LINKS</code> option. </p>
 </dd></dl>
<dt><code>chdir</code></dt>
<dd> <p> Same as <code>cd</code>. </p>
 </dd>
<dt><code>clone</code></dt>
<dd> <p> See the section `The zsh/clone Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dt><code>command</code> [ <code>-pvV</code> ] <i>simple command</i></dt>
<dd> <p> The simple command argument is taken as an external command instead of a function or builtin and is executed. If the <code>POSIX_BUILTINS</code> option is set, builtins will also be executed but certain special properties of them are suppressed. The <code>-p</code> flag causes a default path to be searched instead of that in <code>$path</code>. With the <code>-v</code> flag, <code>command</code> is similar to <code>whence</code> and with <code>-V</code>, it is equivalent to <code>whence -v</code>. </p>
 </dd>
<dl>
<dd> <p> See also the section `Precommand Modifiers&#8217; in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1). </p>
 </dd></dl>
<dt><code>comparguments</code></dt>
<dd> <p> See the section `The zsh/computil Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dt><code>compcall</code></dt>
<dd> <p> See the section `The zsh/compctl Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dt><code>compctl</code></dt>
<dd> <p> See the section `The zsh/compctl Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dt><code>compdescribe</code></dt>
<dd> <p> See the section `The zsh/computil Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dt><code>compfiles</code></dt>
<dd> <p> See the section `The zsh/computil Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dt><code>compgroups</code></dt>
<dd> <p> See the section `The zsh/computil Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dt><code>compquote</code></dt>
<dd> <p> See the section `The zsh/computil Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dt><code>comptags</code></dt>
<dd> <p> See the section `The zsh/computil Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dt><code>comptry</code></dt>
<dd> <p> See the section `The zsh/computil Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dt><code>compvalues</code></dt>
<dd> <p> See the section `The zsh/computil Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dt><code>continue</code> [ <i>n</i> ]</dt>
<dd> <p> Resume the next iteration of the enclosing <code>for</code>, <code>while</code>, <code>until</code>, <code>select</code> or <code>repeat</code> loop. If an arithmetic expression <i>n</i> is specified, break out of <i>n</i>-1 loops and resume at the <i>n</i>th enclosing loop. </p>
 </dd>
<dt><code>declare</code></dt>
<dd> <p> Same as <code>typeset</code>. </p>
 </dd>
<dd> <p> <code>dirs</code> [ <code>-c</code> ] [ <i>arg</i> ... ] </p>
 </dd>
<dd> <p> <code>dirs</code> [ <code>-lpv</code> ] With no arguments, print the contents of the directory stack. Directories are added to this stack with the <code>pushd</code> command, and removed with the <code>cd</code> or <code>popd</code> commands. If arguments are specified, load them onto the directory stack, replacing anything that was there, and push the current directory onto the stack. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <code>-c</code> clear the directory stack. </p>
 </dd>
<dt><code>-l</code></dt>
<dd> <p> print directory names in full instead of using of using <code>~</code> expressions (see <i>Dynamic</i> and <i>Static named directories</i> in <i><a href="/docs/linux/man/1-zshexpn/">zshexpn</a></i>(1)). </p>
 </dd>
<dt><code>-p</code></dt>
<dd> <p> print directory entries one per line. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> number the directories in the stack when printing. </p>
 </dd></dl>
<dt><code>disable</code> [ <code>-afmprs</code> ] <i>name</i> ...</dt>
<dd> <p> Temporarily disable the <i>name</i>d hash table elements or patterns. The default is to disable builtin commands. This allows you to use an external command with the same name as a builtin command. The <code>-a</code> option causes <code>disable</code> to act on regular or global aliases. The <code>-s</code> option causes <code>disable</code> to act on suffix aliases. The <code>-f</code> option causes <code>disable</code> to act on shell functions. The <code>-r</code> options causes <code>disable</code> to act on reserved words. Without arguments all disabled hash table elements from the corresponding hash table are printed. With the <code>-m</code> flag the arguments are taken as patterns (which should be quoted to prevent them from undergoing filename expansion), and all hash table elements from the corresponding hash table matching these patterns are disabled. Disabled objects can be enabled with the <code>enable</code> command. </p>
 </dd>
<dl>
<dd> <p> With the option <code>-p</code>, <i>name</i> ... refer to elements of the shell&#8217;s pattern syntax as described in the section `Filename Generation&#8217;. Certain elements can be disabled separately, as given below. </p>
<p> Note that patterns not allowed by the current settings for the options <code>EXTENDED_GLOB</code>, <code>KSH_GLOB</code> and <code>SH_GLOB</code> are never enabled, regardless of the setting here. For example, if <code>EXTENDED_GLOB</code> is not active, the pattern <code>^</code> is ineffective even if `<code>disable -p &quot;^&quot;</code>&#8216; has not been issued. The list below indicates any option settings that restrict the use of the pattern. It should be noted that setting <code>SH_GLOB</code> has a wider effect than merely disabling patterns as certain expressions, in particular those involving parentheses, are parsed differently. </p>
<p> The following patterns may be disabled; all the strings need quoting on the command line to prevent them from being interpreted immediately as patterns and the patterns are shown below in single quotes as a reminder. </p>
 </dd>
<dl>
<dd> <p> <code>&#8216;?&#8216;</code> The pattern character <code>?</code> wherever it occurs, including when preceding a parenthesis with <code>KSH_GLOB</code>. </p>
 </dd>
<dt><code>&#8216;*&#8216;</code></dt>
<dd> <p> The pattern character <code>*</code> wherever it occurs, including recursive globbing and when preceding a parenthesis with <code>KSH_GLOB</code>. </p>
 </dd>
<dt><code>&#8216;[&#8216;</code></dt>
<dd> <p> Character classes. </p>
 </dd>
<dt><code>&#8216;&lt;&#8216;</code> (<code>NO_SH_GLOB</code>)</dt>
<dd> <p> Numeric ranges. </p>
 </dd>
<dt><code>&#8216;|&#8216;</code> (<code>NO_SH_GLOB</code>)</dt>
<dd> <p> Alternation in grouped patterns, case statements, or KSH_GLOB parenthesised expressions. </p>
 </dd>
<dt><code>&#8216;(&#8216;</code> (<code>NO_SH_GLOB</code>)</dt>
<dd> <p> Grouping using single parentheses. Disabling this does not disable the use of parentheses for <code>KSH_GLOB</code> where they are introduced by a special character, nor for glob qualifiers (use `<code>setopt NO_BARE_GLOB_QUAL</code>&#8216; to disable glob qualifiers that use parentheses only). </p>
 </dd>
<dt><code>&#8216;~&#8216;</code> (<code>EXTENDED_GLOB</code>)</dt>
<dd> <p> Exclusion in the form <i>A</i><code>~</code><i>B</i>. </p>
 </dd>
<dt><code>&#8216;^&#8216;</code> (<code>EXTENDED_GLOB</code>)</dt>
<dd> <p> Exclusion in the form <i>A</i><code>^</code><i>B</i>. </p>
 </dd>
<dt><code>&#8216;#&#8216;</code> (<code>EXTENDED_GLOB</code>)</dt>
<dd> <p> The pattern character <code>#</code> wherever it occurs, both for repetition of a previous pattern and for indicating globbing flags. </p>
 </dd>
<dt><code>&#8216;?(&#8216;</code> (<code>KSH_GLOB</code>)</dt>
<dd> <p> The grouping form <code>?(</code><i>...</i><code>)</code>. Note this is also disabled if <code>&#8216;?&#8216;</code> is disabled. </p>
 </dd>
<dt><code>&#8216;*(&#8216;</code> (<code>KSH_GLOB</code>)</dt>
<dd> <p> The grouping form <code>*(</code><i>...</i><code>)</code>. Note this is also disabled if <code>&#8216;*&#8216;</code> is disabled. </p>
 </dd>
<dt><code>&#8216;+(&#8216;</code> (<code>KSH_GLOB</code>)</dt>
<dd> <p> The grouping form <code>+(</code><i>...</i><code>)</code>. </p>
 </dd>
<dt><code>&#8216;!(&#8216;</code> (<code>KSH_GLOB</code>)</dt>
<dd> <p> The grouping form <code>!(</code><i>...</i><code>)</code>. </p>
 </dd>
<dt><code>&#8216;@(&#8216;</code> (<code>KSH_GLOB</code>)</dt>
<dd> <p> The grouping form <code>@(</code><i>...</i><code>)</code>. </p>
 </dd></dl>
</dl>
<dd> <p> <code>disown</code> [ <i>job</i> ... ] </p>
 </dd>
<dd> <p> <i>job</i> ... <code>&amp;|</code> </p>
 </dd>
<dd> <p> <i>job</i> ... <code>&amp;!</code> Remove the specified <i>job</i>s from the job table; the shell will no longer report their status, and will not complain if you try to exit an interactive shell with them running or stopped. If no <i>job</i> is specified, disown the current job. </p>
 </dd>
<dl>
<dd> <p> If the <i>job</i>s are currently stopped and the <code>AUTO_CONTINUE</code> option is not set, a warning is printed containing information about how to make them running after they have been disowned. If one of the latter two forms is used, the <i>job</i>s will automatically be made running, independent of the setting of the <code>AUTO_CONTINUE</code> option. </p>
 </dd></dl>
<dt><code>echo</code> [ <code>-neE</code> ] [ <i>arg</i> ... ]</dt>
<dd> <p> Write each <i>arg</i> on the standard output, with a space separating each one. If the <code>-n</code> flag is not present, print a newline at the end. <code>echo</code> recognizes the following escape sequences: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>\a</code></dt>
<dd> <p> bell character </p>
 </dd>
<dt><code>\b</code></dt>
<dd> <p> backspace </p>
 </dd>
<dt><code>\c</code></dt>
<dd> <p> suppress subsequent characters and final newline </p>
 </dd>
<dt><code>\e</code></dt>
<dd> <p> escape </p>
 </dd>
<dt><code>\f</code></dt>
<dd> <p> form feed </p>
 </dd>
<dt><code>\n</code></dt>
<dd> <p> linefeed (newline) </p>
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
<dt><code>\\</code></dt>
<dd> <p> backslash </p>
 </dd>
<dt><code>\0</code><i>NNN</i></dt>
<dd> <p> character code in octal </p>
 </dd>
<dt><code>\x</code><i>NN</i></dt>
<dd> <p> character code in hexadecimal </p>
 </dd>
<dt><code>\u</code><i>NNNN</i></dt>
<dd> <p> unicode character code in hexadecimal </p>
 </dd>
<dt><code>\U</code><i>NNNNNNNN</i></dt>
<dd> <p> unicode character code in hexadecimal </p>
 </dd></dl>
<p> The <code>-E</code> flag, or the <code>BSD_ECHO</code> option, can be used to disable these escape sequences. In the latter case, <code>-e</code> flag can be used to enable them. </p>
<p> Note that for standards compliance a double dash does not terminate option processing; instead, it is printed directly. However, a single dash does terminate option processing, so the first dash, possibly following options, is not printed, but everything following it is printed as an argument. The single dash behaviour is different from other shells. For a more portable way of printing text, see <code>printf</code>, and for a more controllable way of printing text within zsh, see <code>print</code>. </dl>
 </p>
<dt><code>echotc</code></dt>
<dd> <p> See the section `The zsh/termcap Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dt><code>echoti</code></dt>
<dd> <p> See the section `The zsh/terminfo Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dt><code>emulate</code> [ <code>-lLR</code> ] [ {<code>zsh</code>|<code>sh</code>|<code>ksh</code>|<code>csh</code>} [ <i>flags</i> ... ] ]</dt>
<dd> <p> Without any argument print current emulation mode. </p>
 </dd>
<dl>
<dd> <p> With single argument set up zsh options to emulate the specified shell as much as possible. <code>csh</code> will never be fully emulated. If the argument is not one of the shells listed above, <code>zsh</code> will be used as a default; more precisely, the tests performed on the argument are the same as those used to determine the emulation at startup based on the shell name, see the section COMPATIBILITY in <i><a href="/docs/linux/man/1-zsh/">zsh</a></i>(1) . In addition to setting shell options, the command also restores the pristine state of pattern enables, as if all patterns had been enabled using <code>enable -p</code>. </p>
<p> If the <code>emulate</code> command occurs inside a function that has been marked for execution tracing with <code>functions -t</code> then the <code>xtrace</code> option will be turned on regardless of emulation mode or other options. Note that code executed inside the function by the <code>.</code>, <code>source</code>, or <code>eval</code> commands is not considered to be running directly from the function, hence does not provoke this behaviour. </p>
<p> If the <code>-R</code> switch is given, all settable options are reset to their default value corresponding to the specified emulation mode, except for certain options describing the interactive environment; otherwise, only those options likely to cause portability problems in scripts and functions are altered. If the <code>-L</code> switch is given, the options <code>LOCAL_OPTIONS</code>, <code>LOCAL_PATTERNS</code> and <code>LOCAL_TRAPS</code> will be set as well, causing the effects of the <code>emulate</code> command and any <code>setopt</code>, <code>disable -p</code> or <code>enable -p</code>, and <code>trap</code> commands to be local to the immediately surrounding shell function, if any; normally these options are turned off in all emulation modes except <code>ksh</code>. The <code>-L</code> switch is mutually exclusive with the use of <code>-c</code> in <i>flags</i>. </p>
<p> If there is a single argument and the <code>-l</code> switch is given, the options that would be set or unset (the latter indicated with the prefix `<code>no</code>&#8216;) are listed. <code>-l</code> can be combined with <code>-L</code> or <code>-R</code> and the list will be modified in the appropriate way. Note the list does not depend on the current setting of options, i.e. it includes all options that may in principle change, not just those that would actually change. </p>
<p> The <i>flags</i> may be any of the invocation-time flags described in the section INVOCATION in <i><a href="/docs/linux/man/1-zsh/">zsh</a></i>(1), except that `<code>-o EMACS</code>&#8216; and `<code>-o VI</code>&#8216; may not be used. Flags such as `<code>+r</code>&#8216;/`<code>+o RESTRICTED</code>&#8216; may be prohibited in some circumstances. </p>
<p> If <code>-c</code> <i>arg</i> appears in <i>flags</i>, <i>arg</i> is evaluated while the requested emulation is temporarily in effect. In this case the emulation mode and all options are restored to their previous values before <code>emulate</code> returns. The <code>-R</code> switch may precede the name of the shell to emulate; note this has a meaning distinct from including <code>-R</code> in <i>flags</i>. </p>
<p> Use of <code>-c</code> enables `sticky&#8217; emulation mode for functions defined within the evaluated expression: the emulation mode is associated thereafter with the function so that whenever the function is executed the emulation (respecting the <code>-R</code> switch, if present) and all options are set (and pattern disables cleared) before entry to the function, and the state is restored after exit. If the function is called when the sticky emulation is already in effect, either within an `<code>emulate</code> <i>shell</i> <code>-c</code>&#8216; expression or within another function with the same sticky emulation, entry and exit from the function do not cause options to be altered (except due to standard processing such as the <code>LOCAL_OPTIONS</code> option). This also applies to functions marked for autoload within the sticky emulation; the appropriate set of options will be applied at the point the function is loaded as well as when it is run. </p>
<p> For example: </p>
 </dd>
<dl>
<dd> <pre><code>
 emulate sh -c 'fni() { setopt cshnullglob; }
fno() { fni; }'
fno 
</code></pre>
 </dd></dl>
<p> The two functions <code>fni</code> and <code>fno</code> are defined with sticky <code>sh</code> emulation. <code>fno</code> is then executed, causing options associated with emulations to be set to their values in <code>sh</code>. <code>fno</code> then calls <code>fni</code>; because <code>fni</code> is also marked for sticky <code>sh</code> emulation, no option changes take place on entry to or exit from it. Hence the option <code>cshnullglob</code>, turned off by <code>sh</code> emulation, will be turned on within <code>fni</code> and remain on return to <code>fno</code>. On exit from <code>fno</code>, the emulation mode and all options will be restored to the state they were in before entry to the temporary emulation. </p>
<p> The documentation above is typically sufficient for the intended purpose of executing code designed for other shells in a suitable environment. More detailed rules follow. </p>
<dl>
<dt>1.</dt>
<dd> <p> The sticky emulation environment provided by `<code>emulate</code> <i>shell</i> <code>-c</code>&#8216; is identical to that provided by entry to a function marked for sticky emulation as a consequence of being defined in such an environment. Hence, for example, the sticky emulation is inherited by subfunctions defined within functions with sticky emulation. </p>
 </dd>
<dt>2.</dt>
<dd> <p> No change of options takes place on entry to or exit from functions that are not marked for sticky emulation, other than those that would normally take place, even if those functions are called within sticky emulation. </p>
 </dd>
<dt>3.</dt>
<dd> <p> No special handling is provided for functions marked for <code>autoload</code> nor for functions present in wordcode created by the <code>zcompile</code> command. </p>
 </dd>
<dt>4.</dt>
<dd> <p> The presence or absence of the <code>-R</code> switch to <code>emulate</code> corresponds to different sticky emulation modes, so for example `<code>emulate sh -c</code>&#8216;, `<code>emulate -R sh -c</code>&#8216; and `<code>emulate csh -c</code>&#8216; are treated as three distinct sticky emulations. </p>
 </dd>
<dt>5.</dt>
<dd> <p> Difference in shell options supplied in addition to the basic emulation also mean the sticky emulations are different, so for example `<code>emulate zsh -c</code>&#8216; and `<code>emulate zsh -o cbases -c</code>&#8216; are treated as distinct sticky emulations. </p>
 </dd></dl>
</dl>
<dt><code>enable</code> [ <code>-afmprs</code> ] <i>name</i> ...</dt>
<dd> <p> Enable the <i>name</i>d hash table elements, presumably disabled earlier with <code>disable</code>. The default is to enable builtin commands. The <code>-a</code> option causes <code>enable</code> to act on regular or global aliases. The <code>-s</code> option causes <code>enable</code> to act on suffix aliases. The <code>-f</code> option causes <code>enable</code> to act on shell functions. The <code>-r</code> option causes <code>enable</code> to act on reserved words. Without arguments all enabled hash table elements from the corresponding hash table are printed. With the <code>-m</code> flag the arguments are taken as patterns (should be quoted) and all hash table elements from the corresponding hash table matching these patterns are enabled. Enabled objects can be disabled with the <code>disable</code> builtin command. </p>
 </dd>
<dl>
<dd> <p> <code>enable -p</code> reenables patterns disabled with <code>disable -p</code>. Note that it does not override globbing options; for example, `<code>enable -p &quot;~&quot;</code>&#8216; does not cause the pattern character <code>~</code> to be active unless the <code>EXTENDED_GLOB</code> option is also set. To enable all possible patterns (so that they may be individually disabled with <code>disable -p</code>), use `<code>setopt EXTENDED_GLOB KSH_GLOB NO_SH_GLOB</code>&#8216;. </p>
 </dd></dl>
<dt><code>eval</code> [ <i>arg</i> ... ]</dt>
<dd> <p> Read the arguments as input to the shell and execute the resulting command(s) in the current shell process. The return status is the same as if the commands had been executed directly by the shell; if there are no <i>args</i> or they contain no commands (i.e. are an empty string or whitespace) the return status is zero. </p>
 </dd>
<dt><code>exec</code> [ <code>-cl</code> ] [ <code>-a</code><i>argv0</i> ] [ <i>command</i> [ <i>arg</i> ... ] ]</dt>
<dd> <p> Replace the current shell with <i>command</i> rather than forking. If <i>command</i> is a shell builtin command or a shell function, the shell executes it, and exits when the command is complete. </p>
 </dd>
<dl>
<dd> <p> With <code>-c</code> clear the environment; with <code>-l</code> prepend <code>-</code> to the <code>argv[0]</code> string of the command executed (to simulate a login shell); with <code>-a</code> <i>argv0</i> set the <code>argv[0]</code> string of the command executed. See the section `Precommand Modifiers&#8217; in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1). </p>
<p> If the option <code>POSIX_BUILTINS</code> is set, <i>command</i> is never interpreted as a shell builtin command or shell function. This means further precommand modifiers such as <code>builtin</code> and <code>noglob</code> are also not interpreted within the shell. Hence <i>command</i> is always found by searching the command path. </p>
<p> If <i>command</i> is omitted but any redirections are specified, then the redirections will take effect in the current shell. </p>
 </dd></dl>
<dt><code>exit</code> [ <i>n</i> ]</dt>
<dd> <p> Exit the shell with the exit status specified by an arithmetic expression <i>n</i>; if none is specified, use the exit status from the last command executed. An EOF condition will also cause the shell to exit, unless the <code>IGNORE_EOF</code> option is set. </p>
 </dd>
<dl>
<dd> <p> See notes at the end of the section JOBS in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1) for some possibly unexpected interactions of the <code>exit</code> command with jobs. </p>
 </dd></dl>
<dt><code>export</code> [ <i>name</i>[<code>=</code><i>value</i>] ... ]</dt>
<dd> <p> The specified <i>name</i>s are marked for automatic export to the environment of subsequently executed commands. Equivalent to <code>typeset -gx</code>. If a parameter specified does not already exist, it is created in the global scope. </p>
 </dd>
<dt><code>false</code> [ <i>arg</i> ... ]</dt>
<dd> <p> Do nothing and return an exit status of 1. </p>
 </dd>
<dd> <p> <code>fc</code> [ <code>-e</code> <i>ename</i> ] [ <code>-LI</code> ] [ <code>-m</code> <i>match</i> ] [ <i>old</i><code>=</code><i>new</i> ... ] [ <i>first</i> [ <i>last</i> ] ] </p>
 </dd>
<dd> <p> <code>fc -l </code>[ <code>-LI</code> ] [ <code>-nrdfEiD</code> ] [ <code>-t</code> <i>timefmt</i> ] [ <code>-m</code> <i>match</i> ] </p>
 </dd>
<dd> <p> [ <i>old</i><code>=</code><i>new</i> ... ] [ <i>first</i> [ <i>last</i> ] ] </p>
 </dd>
<dd> <p> <code>fc -p </code>[ <code>-a</code> ] [ <i>filename</i> [ <i>histsize</i> [ <i>savehistsize</i> ] ] ] </p>
 </dd>
<dd> <p> <code>fc</code> <code>-P</code> </p>
 </dd>
<dd> <p> <code>fc</code> <code>-ARWI</code> [ <i>filename</i> ] The <code>fc</code> command controls the interactive history mechanism. Note that reading and writing of history options is only performed if the shell is interactive. Usually this is detected automatically, but it can be forced by setting the <code>interactive</code> option when starting the shell. </p>
 </dd>
<dl>
<dd> <p> The first two forms of this command select a range of events from <i>first</i> to <i>last</i> from the history list. The arguments <i>first</i> and <i>last</i> may be specified as a number or as a string. A negative number is used as an offset to the current history event number. A string specifies the most recent event beginning with the given string. All substitutions <i>old</i><code>=</code><i>new</i>, if any, are then performed on the text of the events. </p>
<p> In addition to the number range, </p>
 </dd>
<dl>
<dt><code>-I</code></dt>
<dd> <p> restricts to only internal events (not from <code>$HISTFILE</code>) </p>
 </dd>
<dt><code>-L</code></dt>
<dd> <p> restricts to only local events (not from other shells, see <code>SHARE_HISTORY</code> in <i><a href="/docs/linux/man/1-zshoptions/">zshoptions</a></i>(1) -- note that <code>$HISTFILE</code> is considered local when read at startup) </p>
 </dd>
<dt><code>-m</code></dt>
<dd> <p> takes the first argument as a pattern (should be quoted) and only the history events matching this pattern are considered </p>
 </dd></dl>
<p> If <i>first</i> is not specified, it will be set to -1 (the most recent event), or to -16 if the <code>-l</code> flag is given. If <i>last</i> is not specified, it will be set to <i>first</i>, or to -1 if the <code>-l</code> flag is given. However, if the current event has added entries to the history with `<code>print -s</code>&#8216; or `<code>fc -R</code>&#8216;, then the default <i>last</i> for <code>-l</code> includes all new history entries since the current event began. </p>
<p> When the <code>-l</code> flag is given, the resulting events are listed on standard output. Otherwise the editor program specified by <code>-e</code> <i>ename</i> is invoked on a file containing these history events. If <code>-e</code> is not given, the value of the parameter <code>FCEDIT</code> is used; if that is not set the value of the parameter <code>EDITOR</code> is used; if that is not set a builtin default, usually `<code>vi</code>&#8216; is used. If <i>ename</i> is `<code>-</code>&#8216;, no editor is invoked. When editing is complete, the edited command is executed. </p>
<p> The flag <code>-r</code> reverses the order of the events and the flag <code>-n</code> suppresses event numbers when listing. </p>
<p> Also when listing, </p>
<dl>
<dt><code>-d</code></dt>
<dd> <p> prints timestamps for each event </p>
 </dd>
<dt><code>-f</code></dt>
<dd> <p> prints full time-date stamps in the US `<i>MM</i><code>/</code><i>DD</i><code>/</code><i>YY</i> <i>hh</i><code>:</code><i>mm</i>&#8216; format </p>
 </dd>
<dt><code>-E</code></dt>
<dd> <p> prints full time-date stamps in the European `<i>dd</i><code>.</code><i>mm</i><code>.</code><i>yyyy</i> <i>hh</i><code>:</code><i>mm</i>&#8216; format </p>
 </dd>
<dt><code>-i</code></dt>
<dd> <p> prints full time-date stamps in ISO8601 `<i>yyyy</i><code>-</code><i>mm</i><code>-</code><i>dd</i> <i>hh</i><code>:</code><i>mm</i>&#8216; format </p>
 </dd>
<dt><code>-t</code><i>fmt</i></dt>
<dd> <p> prints time and date stamps in the given format; <i>fmt</i> is formatted with the strftime function with the zsh extensions described for the <code>%D{</code><i>string</i><code>}</code> prompt format in the section EXPANSION OF PROMPT SEQUENCES in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1). The resulting formatted string must be no more than 256 characters or will not be printed </p>
 </dd></dl>
<dl>
<dt><code>-D</code></dt>
<dd> <p> prints elapsed times; may be combined with one of the options above </p>
 </dd></dl>
<p> `<code>fc -p</code>&#8216; pushes the current history list onto a stack and switches to a new history list. If the <code>-a</code> option is also specified, this history list will be automatically popped when the current function scope is exited, which is a much better solution than creating a trap function to call `<code>fc -P</code>&#8216; manually. If no arguments are specified, the history list is left empty, <code>$HISTFILE</code> is unset, and <code>$HISTSIZE</code> &amp; <code>$SAVEHIST</code> are set to their default values. If one argument is given, <code>$HISTFILE</code> is set to that filename, <code>$HISTSIZE</code> &amp; <code>$SAVEHIST</code> are left unchanged, and the history file is read in (if it exists) to initialize the new list. If a second argument is specified, <code>$HISTSIZE</code> &amp; <code>$SAVEHIST</code> are instead set to the single specified numeric value. Finally, if a third argument is specified, <code>$SAVEHIST</code> is set to a separate value from <code>$HISTSIZE</code>. You are free to change these environment values for the new history list however you desire in order to manipulate the new history list. </p>
<p> `<code>fc -P</code>&#8216; pops the history list back to an older list saved by `<code>fc -p</code>&#8216;. The current list is saved to its <code>$HISTFILE</code> before it is destroyed (assuming that <code>$HISTFILE</code> and <code>$SAVEHIST</code> are set appropriately, of course). The values of <code>$HISTFILE</code>, <code>$HISTSIZE</code>, and <code>$SAVEHIST</code> are restored to the values they had when `<code>fc -p</code>&#8216; was called. Note that this restoration can conflict with making these variables &quot;local&quot;, so your best bet is to avoid local declarations for these variables in functions that use `<code>fc -p</code>&#8216;. The one other guaranteed-safe combination is declaring these variables to be local at the top of your function and using the automatic option (<code>-a</code>) with `<code>fc -p</code>&#8216;. Finally, note that it is legal to manually pop a push marked for automatic popping if you need to do so before the function exits. </p>
<p> `<code>fc -R</code>&#8216; reads the history from the given file, `<code>fc -W</code>&#8216; writes the history out to the given file, and `<code>fc -A</code>&#8216; appends the history out to the given file. If no filename is specified, the <code>$HISTFILE</code> is assumed. If the <code>-I</code> option is added to <code>-R</code>, only those events that are not already contained within the internal history list are added. If the <code>-I</code> option is added to <code>-A</code> or <code>-W</code>, only those events that are new since last incremental append/write to the history file are appended/written. In any case, the created file will have no more than <code>$SAVEHIST</code> entries. </dl>
 </p>
<dd> <p> <code>fg</code> [ <i>job</i> ... ] </p>
 </dd>
<dd> <p> <i>job</i> ... Bring each specified <i>job</i> in turn to the foreground. If no <i>job</i> is specified, resume the current job. </p>
 </dd>
<dt><code>float</code> [ {<code>+</code>|<code>-</code>}<code>Hghlprtux</code> ] [ {<code>+</code>|<code>-</code>}<code>EFLRZ</code> [ <i>n</i> ] ] [ <i>name</i>[<code>=</code><i>value</i>] ... ]</dt>
<dd> <p> Equivalent to <code>typeset -E</code>, except that options irrelevant to floating point numbers are not permitted. </p>
 </dd>
<dd> <p> <code>functions</code> [ {<code>+</code>|<code>-</code>}<code>UkmtTuWz</code> ] [ <code>-x</code> <i>num</i> ] [ <i>name</i> ... ] </p>
 </dd>
<dd> <p> <code>functions -c</code> <i>oldfn</i> <i>newfn</i> </p>
 </dd>
<dd> <p> <code>functions -M</code> [<code>-s</code>] <i>mathfn</i> [ <i>min</i> [ <i>max</i> [ <i>shellfn</i> ] ] ] </p>
 </dd>
<dd> <p> <code>functions -M</code> [ <code>-m</code> <i>pattern</i> ... ] </p>
 </dd>
<dd> <p> <code>functions +M</code> [ <code>-m</code> ] <i>mathfn</i> ... Equivalent to <code>typeset -f</code>, with the exception of the <code>-c</code>, <code>-x</code>, <code>-M</code> and <code>-W</code> options. For <code>functions -u</code> and <code>functions -U</code>, see <code>autoload</code>, which provides additional options. </p>
 </dd>
<dl>
<dd> <p> The <code>-x</code> option indicates that any functions output will have each leading tab for indentation, added by the shell to show syntactic structure, expanded to the given number <i>num</i> of spaces. <i>num</i> can also be 0 to suppress all indentation. </p>
<p> The <code>-W</code> option turns on the option <code>WARN_NESTED_VAR</code> for the named function or functions only. The option is turned off at the start of nested functions (apart from anonoymous functions) unless the called function also has the <code>-W</code> attribute. </p>
<p> The <code>-c</code> option causes <i>oldfn</i> to be copied to <i>newfn</i>. The copy is efficiently handled internally by reference counting. If <i>oldfn</i> was marked for autoload it is first loaded and if this fails the copy fails. Either function may subsequently be redefined without affecting the other. A typical idiom is that <i>oldfn</i> is the name of a library shell function which is then redefined to call <code>newfn</code>, thereby installing a modified version of the function. </p>
<p> Use of the <code>-M</code> option may not be combined with any of the options handled by <code>typeset -f</code>. </p>
<p> <code>functions -M</code> <i>mathfn</i> defines <i>mathfn</i> as the name of a mathematical function recognised in all forms of arithmetical expressions; see the section `Arithmetic Evaluation&#8217; in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1). By default <i>mathfn</i> may take any number of comma-separated arguments. If <i>min</i> is given, it must have exactly <i>min</i> args; if <i>min</i> and <i>max</i> are both given, it must have at least <i>min</i> and at most <i>max</i> args. <i>max</i> may be -1 to indicate that there is no upper limit. </p>
<p> By default the function is implemented by a shell function of the same name; if <i>shellfn</i> is specified it gives the name of the corresponding shell function while <i>mathfn</i> remains the name used in arithmetical expressions. The name of the function in <code>$0</code> is <i>mathfn</i> (not <i>shellfn</i> as would usually be the case), provided the option <code>FUNCTION_ARGZERO</code> is in effect. The positional parameters in the shell function correspond to the arguments of the mathematical function call. The result of the last arithmetical expression evaluated inside the shell function (even if it is a form that normally only returns a status) gives the result of the mathematical function. </p>
<p> If the additional option <code>-s</code> is given to <code>functions -M</code>, the argument to the function is a single string: anything between the opening and matching closing parenthesis is passed to the function as a single argument, even if it includes commas or white space. The minimum and maximum argument specifiers must therefore be 1 if given. An empty argument list is passed as a zero-length string. </p>
<p> <code>functions -M</code> with no arguments lists all such user-defined functions in the same form as a definition. With the additional option <code>-m</code> and a list of arguments, all functions whose <i>mathfn</i> matches one of the pattern arguments are listed. </p>
<p> <code>function +M</code> removes the list of mathematical functions; with the additional option <code>-m</code> the arguments are treated as patterns and all functions whose <i>mathfn</i> matches the pattern are removed. Note that the shell function implementing the behaviour is not removed (regardless of whether its name coincides with <i>mathfn</i>). </p>
<p> For example, the following prints the cube of 3: </p>
 </dd>
<dl>
<dd> <pre><code>
 zmath_cube() { (( $1 * $1 * $1 )) }
functions -M cube 1 1 zmath_cube
print $((cube(3) )) 
</code></pre>
 </dd></dl>
<p> The following string function takes a single argument, including the commas, so prints 11: </p>
<dl>
<dd> <pre><code>
 stringfn() { (( $#1 )) }
functions -Ms stringfn
print $(( stringfn(foo,bar,rod) )) 
</code></pre>
 </dd></dl>
</dl>
<dt><code>getcap</code></dt>
<dd> <p> See the section `The zsh/cap Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dt><code>getln</code> [ <code>-AclneE</code> ] <i>name</i> ...</dt>
<dd> <p> Read the top value from the buffer stack and put it in the shell parameter <i>name</i>. Equivalent to <code>read -zr</code>. </p>
 </dd>
<dt><code>getopts</code><i>optstring</i><i>name</i> [ <i>arg</i> ... ]</dt>
<dd> <p> Checks the <i>arg</i>s for legal options. If the <i>arg</i>s are omitted, use the positional parameters. A valid option argument begins with a `<code>+</code>&#8216; or a `<code>-</code>&#8216;. An argument not beginning with a `<code>+</code>&#8216; or a `<code>-</code>&#8216;, or the argument `<code>-</code><code>-</code>&#8216;, ends the options. Note that a single `<code>-</code>&#8216; is not considered a valid option argument. <i>optstring</i> contains the letters that <code>getopts</code> recognizes. If a letter is followed by a `<code>:</code>&#8216;, that option requires an argument. The options can be separated from the argument by blanks. </p>
 </dd>
<dl>
<dd> <p> Each time it is invoked, <code>getopts</code> places the option letter it finds in the shell parameter <i>name</i>, prepended with a `<code>+</code>&#8216; when <i>arg</i> begins with a `<code>+</code>&#8216;. The index of the next <i>arg</i> is stored in <code>OPTIND</code>. The option argument, if any, is stored in <code>OPTARG</code>. </p>
<p> The first option to be examined may be changed by explicitly assigning to <code>OPTIND</code>. <code>OPTIND</code> has an initial value of <code>1</code>, and is normally set to <code>1</code> upon entry to a shell function and restored upon exit (this is disabled by the <code>POSIX_BUILTINS</code> option). <code>OPTARG</code> is not reset and retains its value from the most recent call to <code>getopts</code>. If either of <code>OPTIND</code> or <code>OPTARG</code> is explicitly unset, it remains unset, and the index or option argument is not stored. The option itself is still stored in <i>name</i> in this case. </p>
<p> A leading `<code>:</code>&#8216; in <i>optstring</i> causes <code>getopts</code> to store the letter of any invalid option in <code>OPTARG</code>, and to set <i>name</i> to `<code>?</code>&#8216; for an unknown option and to `<code>:</code>&#8216; when a required argument is missing. Otherwise, <code>getopts</code> sets <i>name</i> to `<code>?</code>&#8216; and prints an error message when an option is invalid. The exit status is nonzero when there are no more options. </p>
 </dd></dl>
<dt><code>hash</code> [ <code>-Ldfmrv</code> ] [ <i>name</i>[<code>=</code><i>value</i>] ] ...</dt>
<dd> <p> <code>hash</code> can be used to directly modify the contents of the command hash table, and the named directory hash table. Normally one would modify these tables by modifying one&#8217;s <code>PATH</code> (for the command hash table) or by creating appropriate shell parameters (for the named directory hash table). The choice of hash table to work on is determined by the <code>-d</code> option; without the option the command hash table is used, and with the option the named directory hash table is used. </p>
 </dd>
<dl>
<dd> <p> A command <i>name</i> starting with a <code>/</code> is never hashed, whether by explicit use of the <code>hash</code> command or otherwise. Such a command is always found by direct look up in the file system. </p>
<p> Given no arguments, and neither the <code>-r</code> or <code>-f</code> options, the selected hash table will be listed in full. </p>
<p> The <code>-r</code> option causes the selected hash table to be emptied. It will be subsequently rebuilt in the normal fashion. The <code>-f</code> option causes the selected hash table to be fully rebuilt immediately. For the command hash table this hashes all the absolute directories in the <code>PATH</code>, and for the named directory hash table this adds all users&#8217; home directories. These two options cannot be used with any arguments. </p>
<p> The <code>-m</code> option causes the arguments to be taken as patterns (which should be quoted) and the elements of the hash table matching those patterns are printed. This is the only way to display a limited selection of hash table elements. </p>
<p> For each <i>name</i> with a corresponding <i>value</i>, put `<i>name</i>&#8216; in the selected hash table, associating it with the pathname `<i>value</i>&#8216;. In the command hash table, this means that whenever `<i>name</i>&#8216; is used as a command argument, the shell will try to execute the file given by `<i>value</i>&#8216;. In the named directory hash table, this means that `<i>value</i>&#8216; may be referred to as `<code>~</code><i>name</i>&#8216;. </p>
<p> For each <i>name</i> with no corresponding <i>value</i>, attempt to add <i>name</i> to the hash table, checking what the appropriate <code>value</code> is in the normal manner for that hash table. If an appropriate <code>value</code> can&#8217;t be found, then the hash table will be unchanged. </p>
<p> The <code>-v</code> option causes hash table entries to be listed as they are added by explicit specification. If has no effect if used with <code>-f</code>. </p>
<p> If the <code>-L</code> flag is present, then each hash table entry is printed in the form of a call to hash. </p>
 </dd></dl>
<dt><code>history</code></dt>
<dd> <p> Same as <code>fc -l</code>. </p>
 </dd>
<dt><code>integer</code> [ {<code>+</code>|<code>-</code>}<code>Hghlprtux</code> ] [ {<code>+</code>|<code>-</code>}<code>LRZi</code> [ <i>n</i> ] ] [ <i>name</i>[<code>=</code><i>value</i>] ... ]</dt>
<dd> <p> Equivalent to <code>typeset -i</code>, except that options irrelevant to integers are not permitted. </p>
 </dd>
<dd> <p> <code>jobs</code> [ <code>-dlprs</code> ] [ <i>job</i> ... ] </p>
 </dd>
<dd> <p> <code>jobs -Z</code> <i>string</i> Lists information about each given job, or all jobs if <i>job</i> is omitted. The <code>-l</code> flag lists process IDs, and the <code>-p</code> flag lists process groups. If the <code>-r</code> flag is specified only running jobs will be listed and if the <code>-s</code> flag is given only stopped jobs are shown. If the <code>-d</code> flag is given, the directory from which the job was started (which may not be the current directory of the job) will also be shown. </p>
 </dd>
<dl>
<dd> <p> The <code>-Z</code> option replaces the shell&#8217;s argument and environment space with the given string, truncated if necessary to fit. This will normally be visible in <code>ps</code> (<i><a href="/docs/linux/man/1-ps/">ps</a></i>(1)) listings. This feature is typically used by daemons, to indicate their state. </p>
 </dd></dl>
<dd> <p> <code>kill</code> [ <code>-s</code> <i>signal_name</i> | <code>-n</code> <i>signal_number</i> | <code>-</code><i>sig</i> ] <i>job</i> ... </p>
 </dd>
<dd> <p> <code>kill</code> <code>-l</code> [ <i>sig</i> ... ] Sends either <code>SIGTERM</code> or the specified signal to the given jobs or processes. Signals are given by number or by names, with or without the `<code>SIG</code>&#8216; prefix. If the signal being sent is not `<code>KILL</code>&#8216; or `<code>CONT</code>&#8216;, then the job will be sent a `<code>CONT</code>&#8216; signal if it is stopped. The argument <i>job</i> can be the process ID of a job not in the job list. In the second form, <code>kill -l</code>, if <i>sig</i> is not specified the signal names are listed. Otherwise, for each <i>sig</i> that is a name, the corresponding signal number is listed. For each <i>sig</i> that is a signal number or a number representing the exit status of a process which was terminated or stopped by a signal the name of the signal is printed. </p>
 </dd>
<dl>
<dd> <p> On some systems, alternative signal names are allowed for a few signals. Typical examples are <code>SIGCHLD</code> and <code>SIGCLD</code> or <code>SIGPOLL</code> and <code>SIGIO</code>, assuming they correspond to the same signal number. <code>kill -l</code> will only list the preferred form, however <code>kill -l</code> <i>alt</i> will show if the alternative form corresponds to a signal number. For example, under Linux <code>kill -l IO</code> and <code>kill -l POLL</code> both output 29, hence <code>kill -IO</code> and <code>kill -POLL</code> have the same effect. </p>
<p> Many systems will allow process IDs to be negative to kill a process group or zero to kill the current process group. </p>
 </dd></dl>
<dt><code>let</code><i>arg</i> ...</dt>
<dd> <p> Evaluate each <i>arg</i> as an arithmetic expression. See the section `Arithmetic Evaluation&#8217; in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1) for a description of arithmetic expressions. The exit status is 0 if the value of the last expression is nonzero, 1 if it is zero, and 2 if an error occurred. </p>
 </dd>
<dt><code>limit</code> [ <code>-hs</code> ] [ <i>resource</i> [ <i>limit</i> ] ] ...</dt>
<dd> <p> Set or display resource limits. Unless the <code>-s</code> flag is given, the limit applies only the children of the shell. If <code>-s</code> is given without other arguments, the resource limits of the current shell is set to the previously set resource limits of the children. </p>
 </dd>
<dl>
<dd> <p> If <i>limit</i> is not specified, print the current limit placed on <i>resource</i>, otherwise set the limit to the specified value. If the <code>-h</code> flag is given, use hard limits instead of soft limits. If no <i>resource</i> is given, print all limits. </p>
<p> When looping over multiple resources, the shell will abort immediately if it detects a badly formed argument. However, if it fails to set a limit for some other reason it will continue trying to set the remaining limits. </p>
<p> <i>resource</i> can be one of: </p>
 </dd>
<dl>
<dt><code>addressspace</code></dt>
<dd> <p> Maximum amount of address space used. </p>
 </dd>
<dt><code>aiomemorylocked</code></dt>
<dd> <p> Maximum amount of memory locked in RAM for AIO operations. </p>
 </dd>
<dt><code>aiooperations</code></dt>
<dd> <p> Maximum number of AIO operations. </p>
 </dd>
<dt><code>cachedthreads</code></dt>
<dd> <p> Maximum number of cached threads. </p>
 </dd>
<dt><code>coredumpsize</code></dt>
<dd> <p> Maximum size of a core dump. </p>
 </dd>
<dt><code>cputime</code></dt>
<dd> <p> Maximum CPU seconds per process. </p>
 </dd>
<dt><code>datasize</code></dt>
<dd> <p> Maximum data size (including stack) for each process. </p>
 </dd>
<dt><code>descriptors</code></dt>
<dd> <p> Maximum value for a file descriptor. </p>
 </dd>
<dt><code>filesize</code></dt>
<dd> <p> Largest single file allowed. </p>
 </dd>
<dt><code>kqueues</code></dt>
<dd> <p> Maximum number of kqueues allocated. </p>
 </dd>
<dt><code>maxproc</code></dt>
<dd> <p> Maximum number of processes. </p>
 </dd>
<dt><code>maxpthreads</code></dt>
<dd> <p> Maximum number of threads per process. </p>
 </dd>
<dt><code>memorylocked</code></dt>
<dd> <p> Maximum amount of memory locked in RAM. </p>
 </dd>
<dt><code>memoryuse</code></dt>
<dd> <p> Maximum resident set size. </p>
 </dd>
<dt><code>msgqueue</code></dt>
<dd> <p> Maximum number of bytes in POSIX message queues. </p>
 </dd>
<dt><code>posixlocks</code></dt>
<dd> <p> Maximum number of POSIX locks per user. </p>
 </dd>
<dt><code>pseudoterminals</code></dt>
<dd> <p> Maximum number of pseudo-terminals. </p>
 </dd>
<dt><code>resident</code></dt>
<dd> <p> Maximum resident set size. </p>
 </dd>
<dt><code>sigpending</code></dt>
<dd> <p> Maximum number of pending signals. </p>
 </dd>
<dt><code>sockbufsize</code></dt>
<dd> <p> Maximum size of all socket buffers. </p>
 </dd>
<dt><code>stacksize</code></dt>
<dd> <p> Maximum stack size for each process. </p>
 </dd>
<dt><code>swapsize</code></dt>
<dd> <p> Maximum amount of swap used. </p>
 </dd>
<dt><code>vmemorysize</code></dt>
<dd> <p> Maximum amount of virtual memory. </p>
 </dd></dl>
<p> Which of these resource limits are available depends on the system. <i>resource</i> can be abbreviated to any unambiguous prefix. It can also be an integer, which corresponds to the integer defined for the resource by the operating system. </p>
<p> If argument corresponds to a number which is out of the range of the resources configured into the shell, the shell will try to read or write the limit anyway, and will report an error if this fails. As the shell does not store such resources internally, an attempt to set the limit will fail unless the <code>-s</code> option is present. </p>
<p> <i>limit</i> is a number, with an optional scaling factor, as follows: </p>
<dl>
<dt><i>n</i><code>h</code></dt>
<dd> <p> hours </p>
 </dd>
<dt><i>n</i><code>k</code></dt>
<dd> <p> kilobytes (default) </p>
 </dd>
<dt><i>n</i><code>m</code></dt>
<dd> <p> megabytes or minutes </p>
 </dd>
<dt><i>n</i><code>g</code></dt>
<dd> <p> gigabytes </p>
 </dd>
<dt>[<i>mm</i><code>:</code>]<i>ss</i></dt>
<dd> <p> minutes and seconds </p>
 </dd></dl>
<p> The <code>limit</code> command is not made available by default when the shell starts in a mode emulating another shell. It can be made available with the command `<code>zmodload -F zsh/rlimits b:limit</code>&#8216;. </dl>
 </p>
<dt><code>local</code> [ {<code>+</code>|<code>-</code>}<code>AHUahlprtux</code> ] [ {<code>+</code>|<code>-</code>}<code>EFLRZi</code> [ <i>n</i> ] ] [ <i>name</i>[<code>=</code><i>value</i>] ... ]</dt>
<dd> <p> Same as <code>typeset</code>, except that the options <code>-g</code>, and <code>-f</code> are not permitted. In this case the <code>-x</code> option does not force the use of <code>-g</code>, i.e. exported variables will be local to functions. </p>
 </dd>
<dt><code>log</code></dt>
<dd> <p> List all users currently logged in who are affected by the current setting of the <code>watch</code> parameter. </p>
 </dd>
<dt><code>logout</code> [ <i>n</i> ]</dt>
<dd> <p> Same as <code>exit</code>, except that it only works in a login shell. </p>
 </dd>
<dt><code>noglob</code><i>simple command</i></dt>
<dd> <p> See the section `Precommand Modifiers&#8217; in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1). </p>
 </dd>
<dt><code>popd</code> [ <code>-q</code> ] [ {<code>+</code>|<code>-</code>}<i>n</i> ]</dt>
<dd> <p> Remove an entry from the directory stack, and perform a <code>cd</code> to the new top directory. With no argument, the current top entry is removed. An argument of the form `<code>+</code><i>n</i>&#8216; identifies a stack entry by counting from the left of the list shown by the <code>dirs</code> command, starting with zero. An argument of the form <code>-</code><i>n</i> counts from the right. If the <code>PUSHD_MINUS</code> option is set, the meanings of `<code>+</code>&#8216; and `<code>-</code>&#8216; in this context are swapped. </p>
 </dd>
<dl>
<dd> <p> If the <code>-q</code> (quiet) option is specified, the hook function <code>chpwd</code> and the functions in the array <code>$chpwd_functions</code> are not called, and the new directory stack is not printed. This is useful for calls to <code>popd</code> that do not change the environment seen by an interactive user. </p>
 </dd></dl>
<dd> <p> <code>print </code>[ <code>-abcDilmnNoOpPrsSz</code> ] [ <code>-u</code> <i>n</i> ] [ <code>-f</code> <i>format</i> ] [ <code>-C</code> <i>cols</i> ] </p>
 </dd>
<dd> <p> [ <code>-v</code> <i>name</i> ] [ <code>-xX</code> <i>tabstop</i> ] [ <code>-R</code> [ <code>-en</code> ]] [ <i>arg</i> ... ] With the `<code>-f</code>&#8216; option the arguments are printed as described by <code>printf</code>. With no flags or with the flag `<code>-</code>&#8216;, the arguments are printed on the standard output as described by <code>echo</code>, with the following differences: the escape sequence `<code>\M-</code><i>x</i>&#8216; (or `<code>\M</code><i>x</i>&#8216;) metafies the character <i>x</i> (sets the highest bit), `<code>\C-</code><i>x</i>&#8216; (or `<code>\C</code><i>x</i>&#8216;) produces a control character (`<code>\C-@</code>&#8216; and `<code>\C-?</code>&#8216; give the characters NULL and delete), a character code in octal is represented by `<code>\</code><i>NNN</i>&#8216; (instead of `<code>\0</code><i>NNN</i>&#8216;), and `<code>\E</code>&#8216; is a synonym for `<code>\e</code>&#8216;. Finally, if not in an escape sequence, `<code>\</code>&#8216; escapes the following character and is not printed. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <code>-a</code> Print arguments with the column incrementing first. Only useful with the <code>-c</code> and <code>-C</code> options. </p>
 </dd>
<dt><code>-b</code></dt>
<dd> <p> Recognize all the escape sequences defined for the <code>bindkey</code> command, see the section `Zle Builtins&#8217; in <i><a href="/docs/linux/man/1-zshzle/">zshzle</a></i>(1). </p>
 </dd>
<dt><code>-c</code></dt>
<dd> <p> Print the arguments in columns. Unless <code>-a</code> is also given, arguments are printed with the row incrementing first. </p>
 </dd>
<dt><code>-C</code><i>cols</i></dt>
<dd> <p> Print the arguments in <i>cols</i> columns. Unless <code>-a</code> is also given, arguments are printed with the row incrementing first. </p>
 </dd>
<dt><code>-D</code></dt>
<dd> <p> Treat the arguments as paths, replacing directory prefixes with <code>~</code> expressions corresponding to directory names, as appropriate. </p>
 </dd>
<dt><code>-i</code></dt>
<dd> <p> If given together with <code>-o</code> or <code>-O</code>, sorting is performed case-independently. </p>
 </dd>
<dt><code>-l</code></dt>
<dd> <p> Print the arguments separated by newlines instead of spaces. Note: if the list of arguments is empty, <code>print -l</code> will still output one empty line. To print a possibly-empty list of arguments one per line, use <code>print -C1</code>, as in `<code>print -rC1 -- &quot;$list[@]&quot;</code>&#8216;. </p>
 </dd>
<dt><code>-m</code></dt>
<dd> <p> Take the first argument as a pattern (should be quoted), and remove it from the argument list together with subsequent arguments that do not match this pattern. </p>
 </dd>
<dt><code>-n</code></dt>
<dd> <p> Do not add a newline to the output. </p>
 </dd>
<dt><code>-N</code></dt>
<dd> <p> Print the arguments separated and terminated by nulls. Again, <code>print -rNC1 -- &quot;$list[@]&quot;</code> is a canonical way to print an arbitrary list as null-delimited records. </p>
 </dd>
<dt><code>-o</code></dt>
<dd> <p> Print the arguments sorted in ascending order. </p>
 </dd>
<dt><code>-O</code></dt>
<dd> <p> Print the arguments sorted in descending order. </p>
 </dd>
<dt><code>-p</code></dt>
<dd> <p> Print the arguments to the input of the coprocess. </p>
 </dd>
<dt><code>-P</code></dt>
<dd> <p> Perform prompt expansion (see EXPANSION OF PROMPT SEQUENCES in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1)). In combination with `<code>-f</code>&#8216;, prompt escape sequences are parsed only within interpolated arguments, not within the format string. </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> Ignore the escape conventions of <code>echo</code>. </p>
 </dd>
<dt><code>-R</code></dt>
<dd> <p> Emulate the BSD <code>echo</code> command, which does not process escape sequences unless the <code>-e</code> flag is given. The <code>-n</code> flag suppresses the trailing newline. Only the <code>-e</code> and <code>-n</code> flags are recognized after <code>-R</code>; all other arguments and options are printed. </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> Place the results in the history list instead of on the standard output. Each argument to the <code>print</code> command is treated as a single word in the history, regardless of its content. </p>
 </dd>
<dt><code>-S</code></dt>
<dd> <p> Place the results in the history list instead of on the standard output. In this case only a single argument is allowed; it will be split into words as if it were a full shell command line. The effect is similar to reading the line from a history file with the <code>HIST_LEX_WORDS</code> option active. </p>
 </dd>
<dt><code>-u</code><i>n</i></dt>
<dd> <p> Print the arguments to file descriptor <i>n</i>. </p>
 </dd>
<dt><code>-v</code><i>name</i></dt>
<dd> <p> Store the printed arguments as the value of the parameter <i>name</i>. </p>
 </dd>
<dt><code>-x</code><i>tab-stop</i></dt>
<dd> <p> Expand leading tabs on each line of output in the printed string assuming a tab stop every <i>tab-stop</i> characters. This is appropriate for formatting code that may be indented with tabs. Note that leading tabs of any argument to print, not just the first, are expanded, even if <code>print</code> is using spaces to separate arguments (the column count is maintained across arguments but may be incorrect on output owing to previous unexpanded tabs). </p>
 </dd>
<dl>
<dd> <p> The start of the output of each print command is assumed to be aligned with a tab stop. Widths of multibyte characters are handled if the option <code>MULTIBYTE</code> is in effect. This option is ignored if other formatting options are in effect, namely column alignment or <code>printf</code> style, or if output is to a special location such as shell history or the command line editor. </p>
 </dd></dl>
<dt><code>-X</code><i>tab-stop</i></dt>
<dd> <p> This is similar to <code>-x</code>, except that all tabs in the printed string are expanded. This is appropriate if tabs in the arguments are being used to produce a table format. </p>
 </dd>
<dt><code>-z</code></dt>
<dd> <p> Push the arguments onto the editing buffer stack, separated by spaces. </p>
 </dd></dl>
<p> If any of `<code>-m</code>&#8216;, `<code>-o</code>&#8216; or `<code>-O</code>&#8216; are used in combination with `<code>-f</code>&#8216; and there are no arguments (after the removal process in the case of `<code>-m</code>&#8216;) then nothing is printed. </dl>
 </p>
<dt><code>printf</code> [ <code>-v</code><i>name</i> ] <i>format</i> [ <i>arg</i> ... ]</dt>
<dd> <p> Print the arguments according to the format specification. Formatting rules are the same as used in C. The same escape sequences as for <code>echo</code> are recognised in the format. All C conversion specifications ending in one of <code>csdiouxXeEfgGn</code> are handled. In addition to this, `<code>%b</code>&#8216; can be used instead of `<code>%s</code>&#8216; to cause escape sequences in the argument to be recognised and `<code>%q</code>&#8216; can be used to quote the argument in such a way that allows it to be reused as shell input. With the numeric format specifiers, if the corresponding argument starts with a quote character, the numeric value of the following character is used as the number to print; otherwise the argument is evaluated as an arithmetic expression. See the section `Arithmetic Evaluation&#8217; in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1) for a description of arithmetic expressions. With `<code>%n</code>&#8216;, the corresponding argument is taken as an identifier which is created as an integer parameter. </p>
 </dd>
<dl>
<dd> <p> Normally, conversion specifications are applied to each argument in order but they can explicitly specify the <i>n</i>th argument is to be used by replacing `<code>%</code>&#8216; by `<code>%</code><i>n</i><code>$</code>&#8216; and `<code>*</code>&#8216; by `<code>*</code><i>n</i><code>$</code>&#8216;. It is recommended that you do not mix references of this explicit style with the normal style and the handling of such mixed styles may be subject to future change. </p>
<p> If arguments remain unused after formatting, the format string is reused until all arguments have been consumed. With the <code>print</code> builtin, this can be suppressed by using the <code>-r</code> option. If more arguments are required by the format than have been specified, the behaviour is as if zero or an empty string had been specified as the argument. </p>
<p> The <code>-v</code> option causes the output to be stored as the value of the parameter <i>name</i>, instead of printed. If <i>name</i> is an array and the format string is reused when consuming arguments then one array element will be used for each use of the format string. </p>
 </dd></dl>
<dd> <p> <code>pushd</code> [ <code>-qsLP</code> ] [ <i>arg</i> ] </p>
 </dd>
<dd> <p> <code>pushd</code> [ <code>-qsLP</code> ] <i>old</i> <i>new</i> </p>
 </dd>
<dd> <p> <code>pushd</code> [ <code>-qsLP</code> ] {<code>+</code>|<code>-</code>}<i>n</i> Change the current directory, and push the old current directory onto the directory stack. In the first form, change the current directory to <i>arg</i>. If <i>arg</i> is not specified, change to the second directory on the stack (that is, exchange the top two entries), or change to <code>$HOME</code> if the <code>PUSHD_TO_HOME</code> option is set or if there is only one entry on the stack. Otherwise, <i>arg</i> is interpreted as it would be by <code>cd</code>. The meaning of <i>old</i> and <i>new</i> in the second form is also the same as for <code>cd</code>. </p>
 </dd>
<dl>
<dd> <p> The third form of <code>pushd</code> changes directory by rotating the directory list. An argument of the form `<code>+</code><i>n</i>&#8216; identifies a stack entry by counting from the left of the list shown by the <code>dirs</code> command, starting with zero. An argument of the form `<code>-</code><i>n</i>&#8216; counts from the right. If the <code>PUSHD_MINUS</code> option is set, the meanings of `<code>+</code>&#8216; and `<code>-</code>&#8216; in this context are swapped. </p>
<p> If the <code>-q</code> (quiet) option is specified, the hook function <code>chpwd</code> and the functions in the array <code>$chpwd_functions</code> are not called, and the new directory stack is not printed. This is useful for calls to <code>pushd</code> that do not change the environment seen by an interactive user. </p>
<p> If the option <code>-q</code> is not specified and the shell option <code>PUSHD_SILENT</code> is not set, the directory stack will be printed after a <code>pushd</code> is performed. </p>
<p> The options <code>-s</code>, <code>-L</code> and <code>-P</code> have the same meanings as for the <code>cd</code> builtin. </p>
 </dd></dl>
<dt><code>pushln</code> [ <i>arg</i> ... ]</dt>
<dd> <p> Equivalent to <code>print -nz</code>. </p>
 </dd>
<dt><code>pwd</code> [ <code>-rLP</code> ]</dt>
<dd> <p> Print the absolute pathname of the current working directory. If the <code>-r</code> or the <code>-P</code> flag is specified, or the <code>CHASE_LINKS</code> option is set and the <code>-L</code> flag is not given, the printed path will not contain symbolic links. </p>
 </dd>
<dt><code>r</code></dt>
<dd> <p> Same as <code>fc -e -</code>. </p>
 </dd>
<dd> <p> <code>read </code>[ <code>-rszpqAclneE</code> ] [ <code>-t</code> [ <i>num</i> ] ] [ <code>-k</code> [ <i>num</i> ] ] [ <code>-d</code> <i>delim</i> ] </p>
 </dd>
<dd> <p> [ <code>-u</code> <i>n</i> ] [ <i>name</i>[<code>?</code><i>prompt</i>] ] [ <i>name</i> ... ] Read one line and break it into fields using the characters in <code>$IFS</code> as separators, except as noted below. The first field is assigned to the first <i>name</i>, the second field to the second <i>name</i>, etc., with leftover fields assigned to the last <i>name</i>. If <i>name</i> is omitted then <code>REPLY</code> is used for scalars and <code>reply</code> for arrays. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <code>-r</code> Raw mode: a `<code>\</code>&#8216; at the end of a line does not signify line continuation and backslashes in the line don&#8217;t quote the following character and are not removed. </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> Don&#8217;t echo back characters if reading from the terminal. </p>
 </dd>
<dt><code>-q</code></dt>
<dd> <p> Read only one character from the terminal and set <i>name</i> to `<code>y</code>&#8216; if this character was `<code>y</code>&#8216; or `<code>Y</code>&#8216; and to `<code>n</code>&#8216; otherwise. With this flag set the return status is zero only if the character was `<code>y</code>&#8216; or `<code>Y</code>&#8216;. This option may be used with a timeout (see <code>-t</code>); if the read times out, or encounters end of file, status 2 is returned. Input is read from the terminal unless one of <code>-u</code> or <code>-p</code> is present. This option may also be used within zle widgets. </p>
 </dd>
<dt><code>-k</code> [ <i>num</i> ]</dt>
<dd> <p> Read only one (or <i>num</i>) characters. All are assigned to the first <i>name</i>, without word splitting. This flag is ignored when <code>-q</code> is present. Input is read from the terminal unless one of <code>-u</code> or <code>-p</code> is present. This option may also be used within zle widgets. </p>
 </dd>
<dl>
<dd> <p> Note that despite the mnemonic `key&#8217; this option does read full characters, which may consist of multiple bytes if the option <code>MULTIBYTE</code> is set. </p>
 </dd></dl>
<dt><code>-z</code></dt>
<dd> <p> Read one entry from the editor buffer stack and assign it to the first <i>name</i>, without word splitting. Text is pushed onto the stack with `<code>print -z</code>&#8216; or with <code>push-line</code> from the line editor (see <i><a href="/docs/linux/man/1-zshzle/">zshzle</a></i>(1)). This flag is ignored when the <code>-k</code> or <code>-q</code> flags are present. </p>
 </dd>
<dd> <p> <code>-e</code> </p>
 </dd>
<dd> <p> <code>-E</code> The input read is printed (echoed) to the standard output. If the <code>-e</code> flag is used, no input is assigned to the parameters. </p>
 </dd>
<dt><code>-A</code></dt>
<dd> <p> The first <i>name</i> is taken as the name of an array and all words are assigned to it. </p>
 </dd>
<dd> <p> <code>-c</code> </p>
 </dd>
<dd> <p> <code>-l</code> These flags are allowed only if called inside a function used for completion (specified with the <code>-K</code> flag to <code>compctl</code>). If the <code>-c</code> flag is given, the words of the current command are read. If the <code>-l</code> flag is given, the whole line is assigned as a scalar. If both flags are present, <code>-l</code> is used and <code>-c</code> is ignored. </p>
 </dd>
<dt><code>-n</code></dt>
<dd> <p> Together with <code>-c</code>, the number of the word the cursor is on is read. With <code>-l</code>, the index of the character the cursor is on is read. Note that the command name is word number 1, not word 0, and that when the cursor is at the end of the line, its character index is the length of the line plus one. </p>
 </dd>
<dt><code>-u</code><i>n</i></dt>
<dd> <p> Input is read from file descriptor <i>n</i>. </p>
 </dd>
<dt><code>-p</code></dt>
<dd> <p> Input is read from the coprocess. </p>
 </dd>
<dt><code>-d</code><i>delim</i></dt>
<dd> <p> Input is terminated by the first character of <i>delim</i> instead of by newline. </p>
 </dd>
<dt><code>-t</code> [ <i>num</i> ]</dt>
<dd> <p> Test if input is available before attempting to read. If <i>num</i> is present, it must begin with a digit and will be evaluated to give a number of seconds, which may be a floating point number; in this case the read times out if input is not available within this time. If <i>num</i> is not present, it is taken to be zero, so that <code>read</code> returns immediately if no input is available. If no input is available, return status 1 and do not set any variables. <br/>
&nbsp; This option is not available when reading from the editor buffer with <code>-z</code>, when called from within completion with <code>-c</code> or <code>-l</code>, with <code>-q</code> which clears the input queue before reading, or within zle where other mechanisms should be used to test for input. <br/>
&nbsp; Note that read does not attempt to alter the input processing mode. The default mode is canonical input, in which an entire line is read at a time, so usually `<code>read -t</code>&#8216; will not read anything until an entire line has been typed. However, when reading from the terminal with <code>-k</code> input is processed one key at a time; in this case, only availability of the first character is tested, so that e.g. `<code>read -t -k 2</code>&#8216; can still block on the second character. Use two instances of `<code>read -t -k</code>&#8216; if this is not what is wanted. </p>
 </dd></dl>
<p> If the first argument contains a `<code>?</code>&#8216;, the remainder of this word is used as a <i>prompt</i> on standard error when the shell is interactive. </p>
<p> The value (exit status) of <code>read</code> is 1 when an end-of-file is encountered, or when <code>-c</code> or <code>-l</code> is present and the command is not called from a <code>compctl</code> function, or as described for <code>-q</code>. Otherwise the value is 0. </p>
<p> The behavior of some combinations of the <code>-k</code>, <code>-p</code>, <code>-q</code>, <code>-u</code> and <code>-z</code> flags is undefined. Presently <code>-q</code> cancels all the others, <code>-p</code> cancels <code>-u</code>, <code>-k</code> cancels <code>-z</code>, and otherwise <code>-z</code> cancels both <code>-p</code> and <code>-u</code>. </p>
<p> The <code>-c</code> or <code>-l</code> flags cancel any and all of <code>-kpquz</code>. </dl>
 </p>
<dt><code>readonly</code></dt>
<dd> <p> Same as <code>typeset -r</code>. With the <code>POSIX_BUILTINS</code> option set, same as <code>typeset -gr</code>. </p>
 </dd>
<dt><code>rehash</code></dt>
<dd> <p> Same as <code>hash -r</code>. </p>
 </dd>
<dt><code>return</code> [ <i>n</i> ]</dt>
<dd> <p> Causes a shell function or `<code>.</code>&#8216; script to return to the invoking script with the return status specified by an arithmetic expression <i>n</i>. If <i>n</i> is omitted, the return status is that of the last command executed. </p>
 </dd>
<dl>
<dd> <p> If <code>return</code> was executed from a trap in a <code>TRAP</code><i>NAL</i> function, the effect is different for zero and non-zero return status. With zero status (or after an implicit return at the end of the trap), the shell will return to whatever it was previously processing; with a non-zero status, the shell will behave as interrupted except that the return status of the trap is retained. Note that the numeric value of the signal which caused the trap is passed as the first argument, so the statement `<code>return $((128+$1))</code>&#8216; will return the same status as if the signal had not been trapped. </p>
 </dd></dl>
<dt><code>sched</code></dt>
<dd> <p> See the section `The zsh/sched Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dd> <p> <code>set </code>[ {<code>+</code>|<code>-</code>}<i>options</i> | {<code>+</code>|<code>-</code>}<code>o</code> [ <i>option_name</i> ] ] ... [ {<code>+</code>|<code>-</code>}<code>A</code> [ <i>name</i> ] ] </p>
 </dd>
<dd> <p> [ <i>arg</i> ... ] Set the options for the shell and/or set the positional parameters, or declare and set an array. If the <code>-s</code> option is given, it causes the specified arguments to be sorted before assigning them to the positional parameters (or to the array <i>name</i> if <code>-A</code> is used). With <code>+s</code> sort arguments in descending order. For the meaning of the other flags, see <i><a href="/docs/linux/man/1-zshoptions/">zshoptions</a></i>(1). Flags may be specified by name using the <code>-o</code> option. If no option name is supplied with <code>-o</code>, the current option states are printed: see the description of <code>setopt</code> below for more information on the format. With <code>+o</code> they are printed in a form that can be used as input to the shell. </p>
 </dd>
<dl>
<dd> <p> If the <code>-A</code> flag is specified, <i>name</i> is set to an array containing the given <i>arg</i>s; if no <i>name</i> is specified, all arrays are printed together with their values. </p>
<p> If <code>+A</code> is used and <i>name</i> is an array, the given arguments will replace the initial elements of that array; if no <i>name</i> is specified, all arrays are printed without their values. </p>
<p> The behaviour of arguments after <code>-A</code> <i>name</i> or <code>+A</code> <i>name</i> depends on whether the option <code>KSH_ARRAYS</code> is set. If it is not set, all arguments following <i>name</i> are treated as values for the array, regardless of their form. If the option is set, normal option processing continues at that point; only regular arguments are treated as values for the array. This means that </p>
 </dd>
<dl>
<dd> <pre><code>
 set -A array -x -- foo 
</code></pre>
 </dd></dl>
<p> sets <code>array</code> to `<code>-x -</code><code>- foo</code>&#8216; if <code>KSH_ARRAYS</code> is not set, but sets the array to <code>foo</code> and turns on the option `<code>-x</code>&#8216; if it is set. </p>
<p> If the <code>-A</code> flag is not present, but there are arguments beyond the options, the positional parameters are set. If the option list (if any) is terminated by `<code>-</code><code>-</code>&#8216;, and there are no further arguments, the positional parameters will be unset. </p>
<p> If no arguments and no `<code>-</code><code>-</code>&#8216; are given, then the names and values of all parameters are printed on the standard output. If the only argument is `<code>+</code>&#8216;, the names of all parameters are printed. </p>
<p> For historical reasons, `<code>set -</code>&#8216; is treated as `<code>set +xv</code>&#8216; and `<code>set -</code> <i>args</i>&#8216; as `<code>set +xv --</code> <i>args</i>&#8216; when in any other emulation mode than zsh&#8217;s native mode. </dl>
 </p>
<dt><code>setcap</code></dt>
<dd> <p> See the section `The zsh/cap Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dt><code>setopt</code> [ {<code>+</code>|<code>-</code>}<i>options</i> | {<code>+</code>|<code>-</code>}<code>o</code><i>option_name</i> ] [ <code>-m</code> ] [ <i>name</i> ... ]</dt>
<dd> <p> Set the options for the shell. All options specified either with flags or by name are set. </p>
 </dd>
<dl>
<dd> <p> If no arguments are supplied, the names of all options currently set are printed. The form is chosen so as to minimize the differences from the default options for the current emulation (the default emulation being native <code>zsh</code>, shown as <code>&lt;Z&gt;</code> in <i><a href="/docs/linux/man/1-zshoptions/">zshoptions</a></i>(1)). Options that are on by default for the emulation are shown with the prefix <code>no</code> only if they are off, while other options are shown without the prefix <code>no</code> and only if they are on. In addition to options changed from the default state by the user, any options activated automatically by the shell (for example, <code>SHIN_STDIN</code> or <code>INTERACTIVE</code>) will be shown in the list. The format is further modified by the option <code>KSH_OPTION_PRINT</code>, however the rationale for choosing options with or without the <code>no</code> prefix remains the same in this case. </p>
<p> If the <code>-m</code> flag is given the arguments are taken as patterns (which should be quoted to protect them from filename expansion), and all options with names matching these patterns are set. </p>
<p> Note that a bad option name does not cause execution of subsequent shell code to be aborted; this is behaviour is different from that of `<code>set -o</code>&#8216;. This is because <code>set</code> is regarded as a special builtin by the POSIX standard, but <code>setopt</code> is not. </p>
 </dd></dl>
<dt><code>shift</code> [ <code>-p</code> ] [ <i>n</i> ] [ <i>name</i> ... ]</dt>
<dd> <p> The positional parameters <code>${</code><i>n</i>+1 <code>}</code> ... are renamed to <code>$1</code> ..., where <i>n</i> is an arithmetic expression that defaults to 1. If any <i>name</i>s are given then the arrays with these names are shifted instead of the positional parameters. </p>
 </dd>
<dl>
<dd> <p> If the option <code>-p</code> is given arguments are instead removed (popped) from the end rather than the start of the array. </p>
 </dd></dl>
<dt><code>source</code><i>file</i> [ <i>arg</i> ... ]</dt>
<dd> <p> Same as `<code>.</code>&#8216;, except that the current directory is always searched and is always searched first, before directories in <code>$path</code>. </p>
 </dd>
<dt><code>stat</code></dt>
<dd> <p> See the section `The zsh/stat Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dt><code>suspend</code> [ <code>-f</code> ]</dt>
<dd> <p> Suspend the execution of the shell (send it a <code>SIGTSTP</code>) until it receives a <code>SIGCONT</code>. Unless the <code>-f</code> option is given, this will refuse to suspend a login shell. </p>
 </dd>
<dd> <p> <code>test</code> [ <i>arg</i> ... ] </p>
 </dd>
<dd> <p> <code>[</code> [ <i>arg</i> ... ] <code>]</code> Like the system version of <code>test</code>. Added for compatibility; use conditional expressions instead (see the section `Conditional Expressions&#8217;). The main differences between the conditional expression syntax and the <code>test</code> and <code>[</code> builtins are: these commands are not handled syntactically, so for example an empty variable expansion may cause an argument to be omitted; syntax errors cause status 2 to be returned instead of a shell error; and arithmetic operators expect integer arguments rather than arithmetic expressions. </p>
 </dd>
<dl>
<dd> <p> The command attempts to implement POSIX and its extensions where these are specified. Unfortunately there are intrinsic ambiguities in the syntax; in particular there is no distinction between test operators and strings that resemble them. The standard attempts to resolve these for small numbers of arguments (up to four); for five or more arguments compatibility cannot be relied on. Users are urged wherever possible to use the `<code>[[</code>&#8216; test syntax which does not have these ambiguities. </p>
 </dd></dl>
<dt><code>times</code></dt>
<dd> <p> Print the accumulated user and system times for the shell and for processes run from the shell. </p>
 </dd>
<dt><code>trap</code> [ <i>arg</i> ] [ <i>sig</i> ... ]</dt>
<dd> <p> <i>arg</i> is a series of commands (usually quoted to protect it from immediate evaluation by the shell) to be read and executed when the shell receives any of the signals specified by one or more <i>sig</i> args. Each <i>sig</i> can be given as a number, or as the name of a signal either with or without the string <code>SIG</code> in front (e.g. 1, HUP, and SIGHUP are all the same signal). </p>
 </dd>
<dl>
<dd> <p> If <i>arg</i> is `<code>-</code>&#8216;, then the specified signals are reset to their defaults, or, if no <i>sig</i> args are present, all traps are reset. </p>
<p> If <i>arg</i> is an empty string, then the specified signals are ignored by the shell (and by the commands it invokes). </p>
<p> If <i>arg</i> is omitted but one or more <i>sig</i> args are provided (i.e. the first argument is a valid signal number or name), the effect is the same as if <i>arg</i> had been specified as `<code>-</code>&#8216;. </p>
<p> The <code>trap</code> command with no arguments prints a list of commands associated with each signal. </p>
<p> If <i>sig</i> is <code>ZERR</code> then <i>arg</i> will be executed after each command with a nonzero exit status. <code>ERR</code> is an alias for <code>ZERR</code> on systems that have no <code>SIGERR</code> signal (this is the usual case). </p>
<p> If <i>sig</i> is <code>DEBUG</code> then <i>arg</i> will be executed before each command if the option <code>DEBUG_BEFORE_CMD</code> is set (as it is by default), else after each command. Here, a `command&#8217; is what is described as a `sublist&#8217; in the shell grammar, see the section SIMPLE COMMANDS &amp; PIPELINES in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1). If <code>DEBUG_BEFORE_CMD</code> is set various additional features are available. First, it is possible to skip the next command by setting the option <code>ERR_EXIT</code>; see the description of the <code>ERR_EXIT</code> option in <i><a href="/docs/linux/man/1-zshoptions/">zshoptions</a></i>(1). Also, the shell parameter <code>ZSH_DEBUG_CMD</code> is set to the string corresponding to the command to be executed following the trap. Note that this string is reconstructed from the internal format and may not be formatted the same way as the original text. The parameter is unset after the trap is executed. </p>
<p> If <i>sig</i> is <code>0</code> or <code>EXIT</code> and the <code>trap</code> statement is executed inside the body of a function, then the command <i>arg</i> is executed after the function completes. The value of <code>$?</code> at the start of execution is the exit status of the shell or the return status of the function exiting. If <i>sig</i> is <code>0</code> or <code>EXIT</code> and the <code>trap</code> statement is not executed inside the body of a function, then the command <i>arg</i> is executed when the shell terminates; the trap runs before any <code>zshexit</code> hook functions. </p>
<p> <code>ZERR</code>, <code>DEBUG</code>, and <code>EXIT</code> traps are not executed inside other traps. <code>ZERR</code> and <code>DEBUG</code> traps are kept within subshells, while other traps are reset. </p>
<p> Note that traps defined with the <code>trap</code> builtin are slightly different from those defined as `<code>TRAP</code><i>NAL</i> () { ... }&#8216;, as the latter have their own function environment (line numbers, local variables, etc.) while the former use the environment of the command in which they were called. For example, </p>
 </dd>
<dl>
<dd> <pre><code>
 trap 'print $LINENO' DEBUG 
</code></pre>
 </dd></dl>
<p> will print the line number of a command executed after it has run, while </p>
<dl>
<dd> <pre><code>
 TRAPDEBUG() { print $LINENO; } 
</code></pre>
 </dd></dl>
<p> will always print the number zero. </p>
<p> Alternative signal names are allowed as described under <code>kill</code> above. Defining a trap under either name causes any trap under an alternative name to be removed. However, it is recommended that for consistency users stick exclusively to one name or another. </dl>
 </p>
<dt><code>true</code> [ <i>arg</i> ... ]</dt>
<dd> <p> Do nothing and return an exit status of 0. </p>
 </dd>
<dt><code>ttyctl</code> [ <code>-fu</code> ]</dt>
<dd> <p> The <code>-f</code> option freezes the tty (i.e. terminal or terminal emulator), and <code>-u</code> unfreezes it. When the tty is frozen, no changes made to the tty settings by external programs will be honored by the shell, except for changes in the size of the screen; the shell will simply reset the settings to their previous values as soon as each command exits or is suspended. Thus, <code>stty</code> and similar programs have no effect when the tty is frozen. Freezing the tty does not cause the current state to be remembered: instead, it causes future changes to the state to be blocked. </p>
 </dd>
<dl>
<dd> <p> Without options it reports whether the terminal is frozen or not. </p>
<p> Note that, regardless of whether the tty is frozen or not, the shell needs to change the settings when the line editor starts, so unfreezing the tty does not guarantee settings made on the command line are preserved. Strings of commands run between editing the command line will see a consistent tty state. See also the shell variable <code>STTY</code> for a means of initialising the tty before running external commands. </p>
 </dd></dl>
<dt><code>type</code> [ <code>-wfpamsS</code> ] <i>name</i> ...</dt>
<dd> <p> Equivalent to <code>whence -v</code>. </p>
 </dd>
<dd> <p> <code>typeset </code>[ {<code>+</code>|<code>-</code>}<code>AHUaghlmrtux</code> ] [ {<code>+</code>|<code>-</code>}<code>EFLRZip</code> [ <i>n</i> ] ] </p>
 </dd>
<dd> <p> [ <code>+</code> ] [ <i>name</i>[<code>=</code><i>value</i>] ... ] </p>
 </dd>
<dd> <p> <code>typeset </code><code>-T</code> [ {<code>+</code>|<code>-</code>}<code>Uglrux</code> ] [ {<code>+</code>|<code>-</code>}<code>LRZp</code> [ <i>n</i> ] ] </p>
 </dd>
<dd> <p> [ <code>+</code> | <i>SCALAR</i>[<code>=</code><i>value</i>] <i>array</i>[<code>=(</code><i>value</i> ...<code>)</code>] [ <i>sep</i> ] ] </p>
 </dd>
<dd> <p> <code>typeset</code> <code>-f</code> [ {<code>+</code>|<code>-</code>}<code>TUkmtuz</code> ] [ <code>+</code> ] [ <i>name</i> ... ] Set or display attributes and values for shell parameters. </p>
 </dd>
<dl>
<dd> <p> Except as noted below for control flags that change the behavior, a parameter is created for each <i>name</i> that does not already refer to one. When inside a function, a new parameter is created for every <i>name</i> (even those that already exist), and is unset again when the function completes. See `Local Parameters&#8217; in <i><a href="/docs/linux/man/1-zshparam/">zshparam</a></i>(1). The same rules apply to special shell parameters, which retain their special attributes when made local. </p>
<p> For each <i>name</i><code>=</code><i>value</i> assignment, the parameter <i>name</i> is set to <i>value</i>. </p>
<p> If the shell option <code>TYPESET_SILENT</code> is not set, for each remaining <i>name</i> that refers to a parameter that is already set, the name and value of the parameter are printed in the form of an assignment. Nothing is printed for newly-created parameters, or when any attribute flags listed below are given along with the <i>name</i>. Using `<code>+</code>&#8216; instead of minus to introduce an attribute turns it off. </p>
<p> If no <i>name</i> is present, the names and values of all parameters are printed. In this case the attribute flags restrict the display to only those parameters that have the specified attributes, and using `<code>+</code>&#8216; rather than `<code>-</code>&#8216; to introduce the flag suppresses printing of the values of parameters when there is no parameter name. </p>
<p> All forms of the command handle scalar assignment. Array assignment is possible if any of the reserved words <code>declare</code>, <code>export</code>, <code>float</code>, <code>integer</code>, <code>local</code>, <code>readonly</code> or <code>typeset</code> is matched when the line is parsed (N.B. not when it is executed). In this case the arguments are parsed as assignments, except that the `<code>+=</code>&#8216; syntax and the <code>GLOB_ASSIGN</code> option are not supported, and scalar values after <code>=</code> are <i>not</i> split further into words, even if expanded (regardless of the setting of the <code>KSH_TYPESET</code> option; this option is obsolete). </p>
<p> Examples of the differences between command and reserved word parsing: </p>
 </dd>
<dl>
<dd> <pre><code>
 # Reserved word parsing
typeset svar=$(echo one word) avar=(several words) 
</code></pre>
 </dd></dl>
<p> The above creates a scalar parameter <code>svar</code> and an array parameter <code>avar</code> as if the assignments had been </p>
<dl>
<dd> <pre><code>
 svar=&quot;one word&quot;
avar=(several words) 
</code></pre>
 </dd></dl>
<p> On the other hand: </p>
<dl>
<dd> <pre><code>
 # Normal builtin interface
builtin typeset svar=$(echo two words) 
</code></pre>
 </dd></dl>
<p> The <code>builtin</code> keyword causes the above to use the standard builtin interface to <code>typeset</code> in which argument parsing is performed in the same way as for other commands. This example creates a scalar <code>svar</code> containing the value <code>two</code> and another scalar parameter <code>words</code> with no value. An array value in this case would either cause an error or be treated as an obscure set of glob qualifiers. </p>
<p> Arbitrary arguments are allowed if they take the form of assignments after command line expansion; however, these only perform scalar assignment: </p>
<dl>
<dd> <pre><code>
 var='svar=val'
typeset $var 
</code></pre>
 </dd></dl>
<p> The above sets the scalar parameter <code>svar</code> to the value <code>val</code>. Parentheses around the value within <code>var</code> would not cause array assignment as they will be treated as ordinary characters when <code>$var</code> is substituted. Any non-trivial expansion in the name part of the assignment causes the argument to be treated in this fashion: </p>
<dl>
<dd> <pre><code>
 typeset {var1,var2,var3}=name 
</code></pre>
 </dd></dl>
<p> The above syntax is valid, and has the expected effect of setting the three parameters to the same value, but the command line is parsed as a set of three normal command line arguments to <code>typeset</code> after expansion. Hence it is not possible to assign to multiple arrays by this means. </p>
<p> Note that each interface to any of the commands my be disabled separately. For example, `<code>disable -r typeset</code>&#8216; disables the reserved word interface to <code>typeset</code>, exposing the builtin interface, while `<code>disable typeset</code>&#8216; disables the builtin. Note that disabling the reserved word interface for <code>typeset</code> may cause problems with the output of `<code>typeset -p</code>&#8216;, which assumes the reserved word interface is available in order to restore array and associative array values. </p>
<p> Unlike parameter assignment statements, <code>typeset</code>&#8216;s exit status on an assignment that involves a command substitution does not reflect the exit status of the command substitution. Therefore, to test for an error in a command substitution, separate the declaration of the parameter from its initialization: </p>
<dl>
<dd> <pre><code>
 # WRONG
typeset var1=$(exit 1) || echo &quot;Trouble with var1&quot;
# RIGHT
typeset var1 &amp;&amp; var1=$(exit 1) || echo &quot;Trouble with var1&quot; 
</code></pre>
 </dd></dl>
<p> To initialize a parameter <i>param</i> to a command output and mark it readonly, use <code>typeset -r </code><i>param</i> or <code>readonly </code><i>param</i> after the parameter assignment statement. </p>
<p> If no attribute flags are given, and either no <i>name</i> arguments are present or the flag <code>+m</code> is used, then each parameter name printed is preceded by a list of the attributes of that parameter (<code>array</code>, <code>association</code>, <code>exported</code>, <code>float</code>, <code>integer</code>, <code>readonly</code>, or <code>undefined</code> for autoloaded parameters not yet loaded). If <code>+m</code> is used with attribute flags, and all those flags are introduced with <code>+</code>, the matching parameter names are printed but their values are not. </p>
<p> The following control flags change the behavior of <code>typeset</code>: </p>
<dl>
<dd> <p> <code>+</code> If `<code>+</code>&#8216; appears by itself in a separate word as the last option, then the names of all parameters (functions with <code>-f</code>) are printed, but the values (function bodies) are not. No <i>name</i> arguments may appear, and it is an error for any other options to follow `<code>+</code>&#8216;. The effect of `<code>+</code>&#8216; is as if all attribute flags which precede it were given with a `<code>+</code>&#8216; prefix. For example, `<code>typeset -U +</code>&#8216; is equivalent to `<code>typeset +U</code>&#8216; and displays the names of all arrays having the uniqueness attribute, whereas `<code>typeset -f -U +</code>&#8216; displays the names of all autoloadable functions. If <code>+</code> is the only option, then type information (array, readonly, etc.) is also printed for each parameter, in the same manner as `<code>typeset +m &quot;*&quot;</code>&#8216;. </p>
 </dd>
<dt><code>-g</code></dt>
<dd> <p> The <code>-g</code> (global) means that any resulting parameter will not be restricted to local scope. Note that this does not necessarily mean that the parameter will be global, as the flag will apply to any existing parameter (even if unset) from an enclosing function. This flag does not affect the parameter after creation, hence it has no effect when listing existing parameters, nor does the flag <code>+g</code> have any effect except in combination with <code>-m</code> (see below). </p>
 </dd>
<dt><code>-m</code></dt>
<dd> <p> If the <code>-m</code> flag is given the <i>name</i> arguments are taken as patterns (use quoting to prevent these from being interpreted as file patterns). With no attribute flags, all parameters (or functions with the <code>-f</code> flag) with matching names are printed (the shell option <code>TYPESET_SILENT</code> is not used in this case). </p>
 </dd>
<dl>
<dd> <p> If the <code>+g</code> flag is combined with <code>-m</code>, a new local parameter is created for every matching parameter that is not already local. Otherwise <code>-m</code> applies all other flags or assignments to the existing parameters. </p>
<p> Except when assignments are made with <i>name</i><code>=</code><i>value</i>, using <code>+m</code> forces the matching parameters and their attributes to be printed, even inside a function. Note that <code>-m</code> is ignored if no patterns are given, so `<code>typeset -m</code>&#8216; displays attributes but `<code>typeset -a +m</code>&#8216; does not. </p>
 </dd></dl>
<dt><code>-p</code> [ <i>n</i> ]</dt>
<dd> <p> If the <code>-p</code> option is given, parameters and values are printed in the form of a typeset command with an assignment, regardless of other flags and options. Note that the <code>-H</code> flag on parameters is respected; no value will be shown for these parameters. </p>
 </dd>
<dl>
<dd> <p> <code>-p</code> may be followed by an optional integer argument. Currently only the value <code>1</code> is supported. In this case arrays and associative arrays are printed with newlines between indented elements for readability. </p>
 </dd></dl>
<dt><code>-T</code> [ <i>scalar</i>[<code>=</code><i>value</i>] <i>array</i>[<code>=(</code><i>value</i> ...<code>)</code>] [ <i>sep</i> ] ]</dt>
<dd> <p> This flag has a different meaning when used with <code>-f</code>; see below. Otherwise the <code>-T</code> option requires zero, two, or three arguments to be present. With no arguments, the list of parameters created in this fashion is shown. With two or three arguments, the first two are the name of a scalar and of an array parameter (in that order) that will be tied together in the manner of <code>$PATH</code> and <code>$path</code>. The optional third argument is a single-character separator which will be used to join the elements of the array to form the scalar; if absent, a colon is used, as with <code>$PATH</code>. Only the first character of the separator is significant; any remaining characters are ignored. Multibyte characters are not yet supported. </p>
 </dd>
<dl>
<dd> <p> Only one of the scalar and array parameters may be assigned an initial value (the restrictions on assignment forms described above also apply). </p>
<p> Both the scalar and the array may be manipulated as normal. If one is unset, the other will automatically be unset too. There is no way of untying the variables without unsetting them, nor of converting the type of one of them with another <code>typeset</code> command; <code>+T</code> does not work, assigning an array to <i>scalar</i> is an error, and assigning a scalar to <i>array</i> sets it to be a single-element array. </p>
<p> Note that both `<code>typeset -xT ...</code>&#8216; and `<code>export -T ...</code>&#8216; work, but only the scalar will be marked for export. Setting the value using the scalar version causes a split on all separators (which cannot be quoted). It is possible to apply <code>-T</code> to two previously tied variables but with a different separator character, in which case the variables remain joined as before but the separator is changed. </p>
<p> When an existing scalar is tied to a new array, the value of the scalar is preserved but no attribute other than export will be preserved. </p>
 </dd></dl>
</dl>
<p> Attribute flags that transform the final value (<code>-L</code>, <code>-R</code>, <code>-Z</code>, <code>-l</code>, <code>-u</code>) are only applied to the expanded value at the point of a parameter expansion expression using `<code>$</code>&#8216;. They are not applied when a parameter is retrieved internally by the shell for any purpose. </p>
<p> The following attribute flags may be specified: </p>
<dl>
<dd> <p> <code>-A</code> The names refer to associative array parameters; see `Array Parameters&#8217; in <i><a href="/docs/linux/man/1-zshparam/">zshparam</a></i>(1). </p>
 </dd>
<dt><code>-L</code> [ <i>n</i> ]</dt>
<dd> <p> Left justify and remove leading blanks from the value when the parameter is expanded. If <i>n</i> is nonzero, it defines the width of the field. If <i>n</i> is zero, the width is determined by the width of the value of the first assignment. In the case of numeric parameters, the length of the complete value assigned to the parameter is used to determine the width, not the value that would be output. </p>
 </dd>
<dl>
<dd> <p> The width is the count of characters, which may be multibyte characters if the <code>MULTIBYTE</code> option is in effect. Note that the screen width of the character is not taken into account; if this is required, use padding with parameter expansion flags <code>${(ml</code><i>...</i><code>)</code><i>...</i><code>}</code> as described in `Parameter Expansion Flags&#8217; in <i><a href="/docs/linux/man/1-zshexpn/">zshexpn</a></i>(1). </p>
<p> When the parameter is expanded, it is filled on the right with blanks or truncated if necessary to fit the field. Note truncation can lead to unexpected results with numeric parameters. Leading zeros are removed if the <code>-Z</code> flag is also set. </p>
 </dd></dl>
<dt><code>-R</code> [ <i>n</i> ]</dt>
<dd> <p> Similar to <code>-L</code>, except that right justification is used; when the parameter is expanded, the field is left filled with blanks or truncated from the end. May not be combined with the <code>-Z</code> flag. </p>
 </dd>
<dt><code>-U</code></dt>
<dd> <p> For arrays (but not for associative arrays), keep only the first occurrence of each duplicated value. This may also be set for tied parameters (see <code>-T</code>) or colon-separated special parameters like <code>PATH</code> or <code>FIGNORE</code>, etc. Note the flag takes effect on assignment, and the type of the variable being assigned to is determinative; for variables with shared values it is therefore recommended to set the flag for all interfaces, e.g. `<code>typeset -U PATH path</code>&#8216;. </p>
 </dd>
<dl>
<dd> <p> This flag has a different meaning when used with <code>-f</code>; see below. </p>
 </dd></dl>
<dt><code>-Z</code> [ <i>n</i> ]</dt>
<dd> <p> Specially handled if set along with the <code>-L</code> flag. Otherwise, similar to <code>-R</code>, except that leading zeros are used for padding instead of blanks if the first non-blank character is a digit. Numeric parameters are specially handled: they are always eligible for padding with zeroes, and the zeroes are inserted at an appropriate place in the output. </p>
 </dd>
<dt><code>-a</code></dt>
<dd> <p> The names refer to array parameters. An array parameter may be created this way, but it may be assigned to in the <code>typeset</code> statement only if the reserved word form of <code>typeset</code> is enabled (as it is by default). When displaying, both normal and associative arrays are shown. </p>
 </dd>
<dt><code>-f</code></dt>
<dd> <p> The names refer to functions rather than parameters. No assignments can be made, and the only other valid flags are <code>-t</code>, <code>-T</code>, <code>-k</code>, <code>-u</code>, <code>-U</code> and <code>-z</code>. The flag <code>-t</code> turns on execution tracing for this function; the flag <code>-T</code> does the same, but turns off tracing for any named (not anonymous) function called from the present one, unless that function also has the <code>-t</code> or <code>-T</code> flag. The <code>-u</code> and <code>-U</code> flags cause the function to be marked for autoloading; <code>-U</code> also causes alias expansion to be suppressed when the function is loaded. See the description of the `<code>autoload</code>&#8216; builtin for details. </p>
 </dd>
<dl>
<dd> <p> Note that the builtin <code>functions</code> provides the same basic capabilities as <code>typeset -f</code> but gives access to a few extra options; <code>autoload</code> gives further additional options for the case <code>typeset -fu</code> and <code>typeset -fU</code>. </p>
 </dd></dl>
<dt><code>-h</code></dt>
<dd> <p> Hide: only useful for special parameters (those marked `&lt;S&gt;&#8216; in the table in <i><a href="/docs/linux/man/1-zshparam/">zshparam</a></i>(1)), and for local parameters with the same name as a special parameter, though harmless for others. A special parameter with this attribute will not retain its special effect when made local. Thus after `<code>typeset -h PATH</code>&#8216;, a function containing `<code>typeset PATH</code>&#8216; will create an ordinary local parameter without the usual behaviour of <code>PATH</code>. Alternatively, the local parameter may itself be given this attribute; hence inside a function `<code>typeset -h PATH</code>&#8216; creates an ordinary local parameter and the special <code>PATH</code> parameter is not altered in any way. It is also possible to create a local parameter using `<code>typeset +h </code><i>special</i>&#8216;, where the local copy of <i>special</i> will retain its special properties regardless of having the <code>-h</code> attribute. Global special parameters loaded from shell modules (currently those in <code>zsh/mapfile</code> and <code>zsh/parameter</code>) are automatically given the <code>-h</code> attribute to avoid name clashes. </p>
 </dd>
<dt><code>-H</code></dt>
<dd> <p> Hide value: specifies that <code>typeset</code> will not display the value of the parameter when listing parameters; the display for such parameters is always as if the `<code>+</code>&#8216; flag had been given. Use of the parameter is in other respects normal, and the option does not apply if the parameter is specified by name, or by pattern with the <code>-m</code> option. This is on by default for the parameters in the <code>zsh/parameter</code> and <code>zsh/mapfile</code> modules. Note, however, that unlike the <code>-h</code> flag this is also useful for non-special parameters. </p>
 </dd>
<dt><code>-i</code> [ <i>n</i> ]</dt>
<dd> <p> Use an internal integer representation. If <i>n</i> is nonzero it defines the output arithmetic base, otherwise it is determined by the first assignment. Bases from 2 to 36 inclusive are allowed. </p>
 </dd>
<dt><code>-E</code> [ <i>n</i> ]</dt>
<dd> <p> Use an internal double-precision floating point representation. On output the variable will be converted to scientific notation. If <i>n</i> is nonzero it defines the number of significant figures to display; the default is ten. </p>
 </dd>
<dt><code>-F</code> [ <i>n</i> ]</dt>
<dd> <p> Use an internal double-precision floating point representation. On output the variable will be converted to fixed-point decimal notation. If <i>n</i> is nonzero it defines the number of digits to display after the decimal point; the default is ten. </p>
 </dd>
<dt><code>-l</code></dt>
<dd> <p> Convert the result to lower case whenever the parameter is expanded. The value is <i>not</i> converted when assigned. </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> The given <i>name</i>s are marked readonly. Note that if <i>name</i> is a special parameter, the readonly attribute can be turned on, but cannot then be turned off. </p>
 </dd>
<dl>
<dd> <p> If the <code>POSIX_BUILTINS</code> option is set, the readonly attribute is more restrictive: unset variables can be marked readonly and cannot then be set; furthermore, the readonly attribute cannot be removed from any variable. </p>
<p> It is still possible to change other attributes of the variable though, some of which like <code>-U</code> or <code>-Z</code> would affect the value. More generally, the readonly attribute should not be relied on as a security mechanism. </p>
<p> Note that in zsh (like in pdksh but unlike most other shells) it is still possible to create a local variable of the same name as this is considered a different variable (though this variable, too, can be marked readonly). Special variables that have been made readonly retain their value and readonly attribute when made local. </p>
 </dd></dl>
<dt><code>-t</code></dt>
<dd> <p> Tags the named parameters. Tags have no special meaning to the shell. This flag has a different meaning when used with <code>-f</code>; see above. </p>
 </dd>
<dt><code>-u</code></dt>
<dd> <p> Convert the result to upper case whenever the parameter is expanded. The value is <i>not</i> converted when assigned. This flag has a different meaning when used with <code>-f</code>; see above. </p>
 </dd>
<dt><code>-x</code></dt>
<dd> <p> Mark for automatic export to the environment of subsequently executed commands. If the option <code>GLOBAL_EXPORT</code> is set, this implies the option <code>-g</code>, unless <code>+g</code> is also explicitly given; in other words the parameter is not made local to the enclosing function. This is for compatibility with previous versions of zsh. </p>
 </dd></dl>
</dl>
<dt><code>ulimit</code> [ <code>-HSa</code> ] [ { <code>-bcdfiklmnpqrsTtvwx</code> | <code>-N</code><i>resource</i> } [ <i>limit</i> ] ... ]</dt>
<dd> <p> Set or display resource limits of the shell and the processes started by the shell. The value of <i>limit</i> can be a number in the unit specified below or one of the values `<code>unlimited</code>&#8216;, which removes the limit on the resource, or `<code>hard</code>&#8216;, which uses the current value of the hard limit on the resource. </p>
 </dd>
<dl>
<dd> <p> By default, only soft limits are manipulated. If the <code>-H</code> flag is given use hard limits instead of soft limits. If the <code>-S</code> flag is given together with the <code>-H</code> flag set both hard and soft limits. </p>
<p> If no options are used, the file size limit (<code>-f</code>) is assumed. </p>
<p> If <i>limit</i> is omitted the current value of the specified resources are printed. When more than one resource value is printed, the limit name and unit is printed before each value. </p>
<p> When looping over multiple resources, the shell will abort immediately if it detects a badly formed argument. However, if it fails to set a limit for some other reason it will continue trying to set the remaining limits. </p>
<p> Not all the following resources are supported on all systems. Running <code>ulimit -a</code> will show which are supported. </p>
 </dd>
<dl>
<dt><code>-a</code></dt>
<dd> <p> Lists all of the current resource limits. </p>
 </dd>
<dt><code>-b</code></dt>
<dd> <p> Socket buffer size in bytes (N.B. not kilobytes) </p>
 </dd>
<dt><code>-c</code></dt>
<dd> <p> 512-byte blocks on the size of core dumps. </p>
 </dd>
<dt><code>-d</code></dt>
<dd> <p> Kilobytes on the size of the data segment. </p>
 </dd>
<dt><code>-f</code></dt>
<dd> <p> 512-byte blocks on the size of files written. </p>
 </dd>
<dt><code>-i</code></dt>
<dd> <p> The number of pending signals. </p>
 </dd>
<dt><code>-k</code></dt>
<dd> <p> The number of kqueues allocated. </p>
 </dd>
<dt><code>-l</code></dt>
<dd> <p> Kilobytes on the size of locked-in memory. </p>
 </dd>
<dt><code>-m</code></dt>
<dd> <p> Kilobytes on the size of physical memory. </p>
 </dd>
<dt><code>-n</code></dt>
<dd> <p> open file descriptors. </p>
 </dd>
<dt><code>-p</code></dt>
<dd> <p> The number of pseudo-terminals. </p>
 </dd>
<dt><code>-q</code></dt>
<dd> <p> Bytes in POSIX message queues. </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> Maximum real time priority. On some systems where this is not available, such as NetBSD, this has the same effect as <code>-T</code> for compatibility with <code>sh</code>. </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> Kilobytes on the size of the stack. </p>
 </dd>
<dt><code>-T</code></dt>
<dd> <p> The number of simultaneous threads available to the user. </p>
 </dd>
<dt><code>-t</code></dt>
<dd> <p> CPU seconds to be used. </p>
 </dd>
<dt><code>-u</code></dt>
<dd> <p> The number of processes available to the user. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Kilobytes on the size of virtual memory. On some systems this refers to the limit called `address space&#8217;. </p>
 </dd>
<dt><code>-w</code></dt>
<dd> <p> Kilobytes on the size of swapped out memory. </p>
 </dd>
<dt><code>-x</code></dt>
<dd> <p> The number of locks on files. </p>
 </dd></dl>
<p> A resource may also be specified by integer in the form `<code>-N</code> <i>resource</i>&#8216;, where <i>resource</i> corresponds to the integer defined for the resource by the operating system. This may be used to set the limits for resources known to the shell which do not correspond to option letters. Such limits will be shown by number in the output of `<code>ulimit -a</code>&#8216;. </p>
<p> The number may alternatively be out of the range of limits compiled into the shell. The shell will try to read or write the limit anyway, and will report an error if this fails. </dl>
 </p>
<dt><code>umask</code> [ <code>-S</code> ] [ <i>mask</i> ]</dt>
<dd> <p> The umask is set to <i>mask</i>. <i>mask</i> can be either an octal number or a symbolic value as described in <i><a href="/docs/linux/man/1-chmod/">chmod</a></i>(1). If <i>mask</i> is omitted, the current value is printed. The <code>-S</code> option causes the mask to be printed as a symbolic value. Otherwise, the mask is printed as an octal number. Note that in the symbolic form the permissions you specify are those which are to be allowed (not denied) to the users specified. </p>
 </dd>
<dt><code>unalias</code> [ <code>-ams</code> ] <i>name</i> ...</dt>
<dd> <p> Removes aliases. This command works the same as <code>unhash -a</code>, except that the <code>-a</code> option removes all regular or global aliases, or with <code>-s</code> all suffix aliases: in this case no <i>name</i> arguments may appear. The options <code>-m</code> (remove by pattern) and <code>-s</code> without <code>-a</code> (remove listed suffix aliases) behave as for <code>unhash -a</code>. Note that the meaning of <code>-a</code> is different between <code>unalias</code> and <code>unhash</code>. </p>
 </dd>
<dt><code>unfunction</code></dt>
<dd> <p> Same as <code>unhash -f</code>. </p>
 </dd>
<dt><code>unhash</code> [ <code>-adfms</code> ] <i>name</i> ...</dt>
<dd> <p> Remove the element named <i>name</i> from an internal hash table. The default is remove elements from the command hash table. The <code>-a</code> option causes <code>unhash</code> to remove regular or global aliases; note when removing a global aliases that the argument must be quoted to prevent it from being expanded before being passed to the command. The <code>-s</code> option causes <code>unhash</code> to remove suffix aliases. The <code>-f</code> option causes <code>unhash</code> to remove shell functions. The <code>-d</code> options causes <code>unhash</code> to remove named directories. If the <code>-m</code> flag is given the arguments are taken as patterns (should be quoted) and all elements of the corresponding hash table with matching names will be removed. </p>
 </dd>
<dt><code>unlimit</code> [ <code>-hs</code> ] <i>resource</i> ...</dt>
<dd> <p> The resource limit for each <i>resource</i> is set to the hard limit. If the <code>-h</code> flag is given and the shell has appropriate privileges, the hard resource limit for each <i>resource</i> is removed. The resources of the shell process are only changed if the <code>-s</code> flag is given. </p>
 </dd>
<dl>
<dd> <p> The <code>unlimit</code> command is not made available by default when the shell starts in a mode emulating another shell. It can be made available with the command `<code>zmodload -F zsh/rlimits b:unlimit</code>&#8216;. </p>
 </dd></dl>
<dt><code>unset</code> [ <code>-fmv</code> ] <i>name</i> ...</dt>
<dd> <p> Each named parameter is unset. Local parameters remain local even if unset; they appear unset within scope, but the previous value will still reappear when the scope ends. </p>
 </dd>
<dl>
<dd> <p> Individual elements of associative array parameters may be unset by using subscript syntax on <i>name</i>, which should be quoted (or the entire command prefixed with <code>noglob</code>) to protect the subscript from filename generation. </p>
<p> If the <code>-m</code> flag is specified the arguments are taken as patterns (should be quoted) and all parameters with matching names are unset. Note that this cannot be used when unsetting associative array elements, as the subscript will be treated as part of the pattern. </p>
<p> The <code>-v</code> flag specifies that <i>name</i> refers to parameters. This is the default behaviour. </p>
<p> <code>unset -f</code> is equivalent to <code>unfunction</code>. </p>
 </dd></dl>
<dt><code>unsetopt</code> [ {<code>+</code>|<code>-</code>}<i>options</i> | {<code>+</code>|<code>-</code>}<code>o</code><i>option_name</i> ] [ <i>name</i> ... ]</dt>
<dd> <p> Unset the options for the shell. All options specified either with flags or by name are unset. If no arguments are supplied, the names of all options currently unset are printed. If the <code>-m</code> flag is given the arguments are taken as patterns (which should be quoted to preserve them from being interpreted as glob patterns), and all options with names matching these patterns are unset. </p>
 </dd>
<dt><code>vared</code></dt>
<dd> <p> See the section `Zle Builtins&#8217; in <i><a href="/docs/linux/man/1-zshzle/">zshzle</a></i>(1). </p>
 </dd>
<dt><code>wait</code> [ <i>job</i> ... ]</dt>
<dd> <p> Wait for the specified jobs or processes. If <i>job</i> is not given then all currently active child processes are waited for. Each <i>job</i> can be either a job specification or the process ID of a job in the job table. The exit status from this command is that of the job waited for. If <i>job</i> represents an unknown job or process ID, a warning is printed (unless the <code>POSIX_BUILTINS</code> option is set) and the exit status is 127. </p>
 </dd>
<dl>
<dd> <p> It is possible to wait for recent processes (specified by process ID, not by job) that were running in the background even if the process has exited. Typically the process ID will be recorded by capturing the value of the variable <code>$!</code> immediately after the process has been started. There is a limit on the number of process IDs remembered by the shell; this is given by the value of the system configuration parameter <code>CHILD_MAX</code>. When this limit is reached, older process IDs are discarded, least recently started processes first. </p>
<p> Note there is no protection against the process ID wrapping, i.e. if the wait is not executed soon enough there is a chance the process waited for is the wrong one. A conflict implies both process IDs have been generated by the shell, as other processes are not recorded, and that the user is potentially interested in both, so this problem is intrinsic to process IDs. </p>
 </dd></dl>
<dt><code>whence</code> [ <code>-vcwfpamsS</code> ] [ <code>-x</code><i>num</i> ] <i>name</i> ...</dt>
<dd> <p> For each <i>name</i>, indicate how it would be interpreted if used as a command name. </p>
 </dd>
<dl>
<dd> <p> If <i>name</i> is not an alias, built-in command, external command, shell function, hashed command, or a reserved word, the exit status shall be non-zero, and -- if <code>-v</code>, <code>-c</code>, or <code>-w</code> was passed -- a message will be written to standard output. (This is different from other shells that write that message to standard error.) </p>
<p> <code>whence</code> is most useful when <i>name</i> is only the last path component of a command, i.e. does not include a `<code>/</code>&#8216;; in particular, pattern matching only succeeds if just the non-directory component of the command is passed. </p>
 </dd>
<dl>
<dd> <p> <code>-v</code> Produce a more verbose report. </p>
 </dd>
<dt><code>-c</code></dt>
<dd> <p> Print the results in a <code>csh</code>-like format. This takes precedence over <code>-v</code>. </p>
 </dd>
<dt><code>-w</code></dt>
<dd> <p> For each <i>name</i>, print `<i>name</i><code>:</code> <i>word</i>&#8216; where <i>word</i> is one of <code>alias</code>, <code>builtin</code>, <code>command</code>, <code>function</code>, <code>hashed</code>, <code>reserved</code> or <code>none</code>, according as <i>name</i> corresponds to an alias, a built-in command, an external command, a shell function, a command defined with the <code>hash</code> builtin, a reserved word, or is not recognised. This takes precedence over <code>-v</code> and <code>-c</code>. </p>
 </dd>
<dt><code>-f</code></dt>
<dd> <p> Causes the contents of a shell function to be displayed, which would otherwise not happen unless the <code>-c</code> flag were used. </p>
 </dd>
<dt><code>-p</code></dt>
<dd> <p> Do a path search for <i>name</i> even if it is an alias, reserved word, shell function or builtin. </p>
 </dd>
<dt><code>-a</code></dt>
<dd> <p> Do a search for all occurrences of <i>name</i> throughout the command path. Normally only the first occurrence is printed. </p>
 </dd>
<dt><code>-m</code></dt>
<dd> <p> The arguments are taken as patterns (pattern characters should be quoted), and the information is displayed for each command matching one of these patterns. </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> If a pathname contains symlinks, print the symlink-free pathname as well. </p>
 </dd>
<dt><code>-S</code></dt>
<dd> <p> As <code>-s</code>, but if the pathname had to be resolved by following multiple symlinks, the intermediate steps are printed, too. The symlink resolved at each step might be anywhere in the path. </p>
 </dd>
<dt><code>-x</code><i>num</i></dt>
<dd> <p> Expand tabs when outputting shell functions using the <code>-c</code> option. This has the same effect as the <code>-x</code> option to the <code>functions</code> builtin. </p>
 </dd></dl>
</dl>
<dt><code>where</code> [ <code>-wpmsS</code> ] [ <code>-x</code><i>num</i> ] <i>name</i> ...</dt>
<dd> <p> Equivalent to <code>whence -ca</code>. </p>
 </dd>
<dt><code>which</code> [ <code>-wpamsS</code> ] [ <code>-x</code><i>num</i> ] <i>name</i> ...</dt>
<dd> <p> Equivalent to <code>whence -c</code>. </p>
 </dd>
<dd> <p> <code>zcompile</code> [ <code>-U</code> ] [ <code>-z</code> | <code>-k</code> ] [ <code>-R</code> | <code>-M</code> ] <i>file</i> [ <i>name</i> ... ] </p>
 </dd>
<dd> <p> <code>zcompile</code> <code>-ca</code> [ <code>-m</code> ] [ <code>-R</code> | <code>-M</code> ] <i>file</i> [ <i>name</i> ... ] </p>
 </dd>
<dd> <p> <code>zcompile -t</code> <i>file</i> [ <i>name</i> ... ] This builtin command can be used to compile functions or scripts, storing the compiled form in a file, and to examine files containing the compiled form. This allows faster autoloading of functions and sourcing of scripts by avoiding parsing of the text when the files are read. </p>
 </dd>
<dl>
<dd> <p> The first form (without the <code>-c</code>, <code>-a</code> or <code>-t</code> options) creates a compiled file. If only the <i>file</i> argument is given, the output file has the name `<i>file</i><code>.zwc</code>&#8216; and will be placed in the same directory as the <i>file</i>. The shell will load the compiled file instead of the normal function file when the function is autoloaded; see the section `Autoloading Functions&#8217; in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1) for a description of how autoloaded functions are searched. The extension <code>.zwc</code> stands for `zsh word code&#8217;. </p>
<p> If there is at least one <i>name</i> argument, all the named files are compiled into the output <i>file</i> given as the first argument. If <i>file</i> does not end in <code>.zwc</code>, this extension is automatically appended. Files containing multiple compiled functions are called `digest&#8217; files, and are intended to be used as elements of the <code>FPATH</code>/<code>fpath</code> special array. </p>
<p> The second form, with the <code>-c</code> or <code>-a</code> options, writes the compiled definitions for all the named functions into <i>file</i>. For <code>-c</code>, the names must be functions currently defined in the shell, not those marked for autoloading. Undefined functions that are marked for autoloading may be written by using the <code>-a</code> option, in which case the <code>fpath</code> is searched and the contents of the definition files for those functions, if found, are compiled into <i>file</i>. If both <code>-c</code> and <code>-a</code> are given, names of both defined functions and functions marked for autoloading may be given. In either case, the functions in files written with the <code>-c</code> or <code>-a</code> option will be autoloaded as if the <code>KSH_AUTOLOAD</code> option were unset. </p>
<p> The reason for handling loaded and not-yet-loaded functions with different options is that some definition files for autoloading define multiple functions, including the function with the same name as the file, and, at the end, call that function. In such cases the output of `<code>zcompile -c</code>&#8216; does not include the additional functions defined in the file, and any other initialization code in the file is lost. Using `<code>zcompile -a</code>&#8216; captures all this extra information. </p>
<p> If the <code>-m</code> option is combined with <code>-c</code> or <code>-a</code>, the <i>name</i>s are used as patterns and all functions whose names match one of these patterns will be written. If no <i>name</i> is given, the definitions of all functions currently defined or marked as autoloaded will be written. </p>
<p> Note the second form cannot be used for compiling functions that include redirections as part of the definition rather than within the body of the function; for example </p>
 </dd>
<dl>
<dd> <pre><code>
 fn1() { { ... } &gt;~/logfile } 
</code></pre>
 </dd></dl>
<p> can be compiled but </p>
<dl>
<dd> <pre><code>
 fn1() { ... } &gt;~/logfile 
</code></pre>
 </dd></dl>
<p> cannot. It is possible to use the first form of <code>zcompile</code> to compile autoloadable functions that include the full function definition instead of just the body of the function. </p>
<p> The third form, with the <code>-t</code> option, examines an existing compiled file. Without further arguments, the names of the original files compiled into it are listed. The first line of output shows the version of the shell which compiled the file and how the file will be used (i.e. by reading it directly or by mapping it into memory). With arguments, nothing is output and the return status is set to zero if definitions for <i>all</i> <i>name</i>s were found in the compiled file, and non-zero if the definition for at least one <i>name</i> was not found. </p>
<p> Other options: </p>
<dl>
<dd> <p> <code>-U</code> Aliases are not expanded when compiling the <i>name</i>d files. </p>
 </dd>
<dt><code>-R</code></dt>
<dd> <p> When the compiled file is read, its contents are copied into the shell&#8217;s memory, rather than memory-mapped (see <code>-M</code>). This happens automatically on systems that do not support memory mapping. </p>
 </dd>
<dl>
<dd> <p> When compiling scripts instead of autoloadable functions, it is often desirable to use this option; otherwise the whole file, including the code to define functions which have already been defined, will remain mapped, consequently wasting memory. </p>
 </dd></dl>
<dt><code>-M</code></dt>
<dd> <p> The compiled file is mapped into the shell&#8217;s memory when read. This is done in such a way that multiple instances of the shell running on the same host will share this mapped file. If neither <code>-R</code> nor <code>-M</code> is given, the <code>zcompile</code> builtin decides what to do based on the size of the compiled file. </p>
 </dd>
<dd> <p> <code>-k</code> </p>
 </dd>
<dd> <p> <code>-z</code> These options are used when the compiled file contains functions which are to be autoloaded. If <code>-z</code> is given, the function will be autoloaded as if the <code>KSH_AUTOLOAD</code> option is <i>not</i> set, even if it is set at the time the compiled file is read, while if the <code>-k</code> is given, the function will be loaded as if <code>KSH_AUTOLOAD</code> <i>is</i> set. These options also take precedence over any <code>-k</code> or <code>-z</code> options specified to the <code>autoload</code> builtin. If neither of these options is given, the function will be loaded as determined by the setting of the <code>KSH_AUTOLOAD</code> option at the time the compiled file is read. <br/>
&nbsp; These options may also appear as many times as necessary between the listed <i>name</i>s to specify the loading style of all following functions, up to the next <code>-k</code> or <code>-z</code>. </p>
<p> The created file always contains two versions of the compiled format, one for big-endian machines and one for small-endian machines. The upshot of this is that the compiled file is machine independent and if it is read or mapped, only one half of the file is actually used (and mapped). </p>
 </dd></dl>
</dl>
<dt><code>zformat</code></dt>
<dd> <p> See the section `The zsh/zutil Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dt><code>zftp</code></dt>
<dd> <p> See the section `The zsh/zftp Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dt><code>zle</code></dt>
<dd> <p> See the section `Zle Builtins&#8217; in <i><a href="/docs/linux/man/1-zshzle/">zshzle</a></i>(1). </p>
 </dd>
<dd> <p> <code>zmodload</code> [ <code>-dL</code> ] [ <code>-s</code> ] [ ... ] </p>
 </dd>
<dd> <p> <code>zmodload -F</code> [ <code>-alLme</code> <code>-P</code> <i>param</i> ] <i>module</i> [ [<code>+-</code>]<i>feature</i> ... ] </p>
 </dd>
<dd> <p> <code>zmodload -e</code> [ <code>-A</code> ] [ ... ] </p>
 </dd>
<dd> <p> <code>zmodload</code> [ <code>-a</code> [ <code>-bcpf</code> [ <code>-I</code> ] ] ] [ <code>-iL</code> ] ... </p>
 </dd>
<dd> <p> <code>zmodload</code> <code>-u</code> [ <code>-abcdpf</code> [ <code>-I</code> ] ] [ <code>-iL</code> ] ... </p>
 </dd>
<dd> <p> <code>zmodload</code> <code>-A</code> [ <code>-L</code> ] [ <i>modalias</i>[<code>=</code><i>module</i>] ... ] </p>
 </dd>
<dd> <p> <code>zmodload</code> <code>-R</code> <i>modalias</i> ... Performs operations relating to zsh&#8217;s loadable modules. Loading of modules while the shell is running (`dynamical loading&#8217;) is not available on all operating systems, or on all installations on a particular operating system, although the <code>zmodload</code> command itself is always available and can be used to manipulate modules built into versions of the shell executable without dynamical loading. </p>
 </dd>
<dl>
<dd> <p> Without arguments the names of all currently loaded binary modules are printed. The <code>-L</code> option causes this list to be in the form of a series of <code>zmodload</code> commands. Forms with arguments are: </p>
 </dd>
<dl>
<dd> <p> <code>zmodload</code> [ <code>-is</code> ] <i>name</i> ... </p>
 </dd>
<dd> <p> <code>zmodload</code> <code>-u</code> [ <code>-i</code> ] <i>name</i> ... In the simplest case, <code>zmodload</code> loads a binary module. The module must be in a file with a name consisting of the specified <i>name</i> followed by a standard suffix, usually `<code>.so</code>&#8216; (`<code>.sl</code>&#8216; on HPUX). If the module to be loaded is already loaded the duplicate module is ignored. If <code>zmodload</code> detects an inconsistency, such as an invalid module name or circular dependency list, the current code block is aborted. If it is available, the module is loaded if necessary, while if it is not available, non-zero status is silently returned. The option <code>-i</code> is accepted for compatibility but has no effect. </p>
 </dd>
<dl>
<dd> <p> The <i>name</i>d module is searched for in the same way a command is, using <code>$module_path</code> instead of <code>$path</code>. However, the path search is performed even when the module name contains a `<code>/</code>&#8216;, which it usually does. There is no way to prevent the path search. </p>
<p> If the module supports features (see below), <code>zmodload</code> tries to enable all features when loading a module. If the module was successfully loaded but not all features could be enabled, <code>zmodload</code> returns status 2. </p>
<p> If the option <code>-s</code> is given, no error is printed if the module was not available (though other errors indicating a problem with the module are printed). The return status indicates if the module was loaded. This is appropriate if the caller considers the module optional. </p>
<p> With <code>-u</code>, <code>zmodload</code> unloads modules. The same <i>name</i> must be given that was given when the module was loaded, but it is not necessary for the module to exist in the file system. The <code>-i</code> option suppresses the error if the module is already unloaded (or was never loaded). </p>
<p> Each module has a boot and a cleanup function. The module will not be loaded if its boot function fails. Similarly a module can only be unloaded if its cleanup function runs successfully. </p>
 </dd></dl>
<dt><code>zmodload -F</code> [ <code>-almLe</code><code>-P</code><i>param</i> ] <i>module</i> [ [<code>+-</code>]<i>feature</i> ... ]</dt>
<dd> <p> <code>zmodload -F</code> allows more selective control over the features provided by modules. With no options apart from <code>-F</code>, the module named <i>module</i> is loaded, if it was not already loaded, and the list of <i>feature</i>s is set to the required state. If no <i>feature</i>s are specified, the module is loaded, if it was not already loaded, but the state of features is unchanged. Each feature may be preceded by a <code>+</code> to turn the feature on, or <code>-</code> to turn it off; the <code>+</code> is assumed if neither character is present. Any feature not explicitly mentioned is left in its current state; if the module was not previously loaded this means any such features will remain disabled. The return status is zero if all features were set, 1 if the module failed to load, and 2 if some features could not be set (for example, a parameter couldn&#8217;t be added because there was a different parameter of the same name) but the module was loaded. </p>
 </dd>
<dl>
<dd> <p> The standard features are builtins, conditions, parameters and math functions; these are indicated by the prefix `<code>b:</code>&#8216;, `<code>c:</code>&#8216; (`<code>C:</code>&#8216; for an infix condition), `<code>p:</code>&#8216; and `<code>f:</code>&#8216;, respectively, followed by the name that the corresponding feature would have in the shell. For example, `<code>b:strftime</code>&#8216; indicates a builtin named <code>strftime</code> and <code>p:EPOCHSECONDS</code> indicates a parameter named <code>EPOCHSECONDS</code>. The module may provide other (`abstract&#8217;) features of its own as indicated by its documentation; these have no prefix. </p>
<p> With <code>-l</code> or <code>-L</code>, features provided by the module are listed. With <code>-l</code> alone, a list of features together with their states is shown, one feature per line. With <code>-L</code> alone, a <code>zmodload -F</code> command that would cause enabled features of the module to be turned on is shown. With <code>-lL</code>, a <code>zmodload -F</code> command that would cause all the features to be set to their current state is shown. If one of these combinations is given with the option <code>-P</code> <i>param</i> then the parameter <i>param</i> is set to an array of features, either features together with their state or (if <code>-L</code> alone is given) enabled features. </p>
<p> With the option <code>-L</code> the module name may be omitted; then a list of all enabled features for all modules providing features is printed in the form of <code>zmodload -F</code> commands. If <code>-l</code> is also given, the state of both enabled and disabled features is output in that form. </p>
<p> A set of features may be provided together with <code>-l</code> or <code>-L</code> and a module name; in that case only the state of those features is considered. Each feature may be preceded by <code>+</code> or <code>-</code> but the character has no effect. If no set of features is provided, all features are considered. </p>
<p> With <code>-e</code>, the command first tests that the module is loaded; if it is not, status 1 is returned. If the module is loaded, the list of features given as an argument is examined. Any feature given with no prefix is simply tested to see if the module provides it; any feature given with a prefix <code>+</code> or <code>-</code> is tested to see if is provided and in the given state. If the tests on all features in the list succeed, status 0 is returned, else status 1. </p>
<p> With <code>-m</code>, each entry in the given list of features is taken as a pattern to be matched against the list of features provided by the module. An initial <code>+</code> or <code>-</code> must be given explicitly. This may not be combined with the <code>-a</code> option as autoloads must be specified explicitly. </p>
<p> With <code>-a</code>, the given list of features is marked for autoload from the specified module, which may not yet be loaded. An optional <code>+</code> may appear before the feature name. If the feature is prefixed with <code>-</code>, any existing autoload is removed. The options <code>-l</code> and <code>-L</code> may be used to list autoloads. Autoloading is specific to individual features; when the module is loaded only the requested feature is enabled. Autoload requests are preserved if the module is subsequently unloaded until an explicit `<code>zmodload -Fa</code> <i>module</i> <code>-</code><i>feature</i>&#8216; is issued. It is not an error to request an autoload for a feature of a module that is already loaded. </p>
<p> When the module is loaded each autoload is checked against the features actually provided by the module; if the feature is not provided the autoload request is deleted. A warning message is output; if the module is being loaded to provide a different feature, and that autoload is successful, there is no effect on the status of the current command. If the module is already loaded at the time when <code>zmodload -Fa</code> is run, an error message is printed and status 1 returned. </p>
<p> <code>zmodload -Fa</code> can be used with the <code>-l</code>, <code>-L</code>, <code>-e</code> and <code>-P</code> options for listing and testing the existence of autoloadable features. In this case <code>-l</code> is ignored if <code>-L</code> is specified. <code>zmodload -FaL</code> with no module name lists autoloads for all modules. </p>
<p> Note that only standard features as described above can be autoloaded; other features require the module to be loaded before enabling. </p>
 </dd></dl>
<dd> <p> <code>zmodload</code> <code>-d</code> [ <code>-L</code> ] [ <i>name</i> ] </p>
 </dd>
<dd> <p> <code>zmodload</code> <code>-d</code> <i>name</i> <i>dep</i> ... </p>
 </dd>
<dd> <p> <code>zmodload</code> <code>-ud</code> <i>name</i> [ <i>dep</i> ... ] The <code>-d</code> option can be used to specify module dependencies. The modules named in the second and subsequent arguments will be loaded before the module named in the first argument. </p>
 </dd>
<dl>
<dd> <p> With <code>-d</code> and one argument, all dependencies for that module are listed. With <code>-d</code> and no arguments, all module dependencies are listed. This listing is by default in a Makefile-like format. The <code>-L</code> option changes this format to a list of <code>zmodload -d</code> commands. </p>
<p> If <code>-d</code> and <code>-u</code> are both used, dependencies are removed. If only one argument is given, all dependencies for that module are removed. </p>
 </dd></dl>
<dd> <p> <code>zmodload</code> <code>-ab</code> [ <code>-L</code> ] </p>
 </dd>
<dd> <p> <code>zmodload</code> <code>-ab</code> [ <code>-i</code> ] <i>name</i> [ <i>builtin</i> ... ] </p>
 </dd>
<dd> <p> <code>zmodload</code> <code>-ub</code> [ <code>-i</code> ] <i>builtin</i> ... The <code>-ab</code> option defines autoloaded builtins. It defines the specified <i>builtin</i>s. When any of those builtins is called, the module specified in the first argument is loaded and all its features are enabled (for selective control of features use `<code>zmodload -F -a</code>&#8216; as described above). If only the <i>name</i> is given, one builtin is defined, with the same name as the module. <code>-i</code> suppresses the error if the builtin is already defined or autoloaded, but not if another builtin of the same name is already defined. </p>
 </dd>
<dl>
<dd> <p> With <code>-ab</code> and no arguments, all autoloaded builtins are listed, with the module name (if different) shown in parentheses after the builtin name. The <code>-L</code> option changes this format to a list of <code>zmodload -a</code> commands. </p>
<p> If <code>-b</code> is used together with the <code>-u</code> option, it removes builtins previously defined with <code>-ab</code>. This is only possible if the builtin is not yet loaded. <code>-i</code> suppresses the error if the builtin is already removed (or never existed). </p>
<p> Autoload requests are retained if the module is subsequently unloaded until an explicit `<code>zmodload -ub</code> <i>builtin</i>&#8216; is issued. </p>
 </dd></dl>
<dd> <p> <code>zmodload</code> <code>-ac</code> [ <code>-IL</code> ] </p>
 </dd>
<dd> <p> <code>zmodload</code> <code>-ac</code> [ <code>-iI</code> ] <i>name</i> [ <i>cond</i> ... ] </p>
 </dd>
<dd> <p> <code>zmodload</code> <code>-uc</code> [ <code>-iI</code> ] <i>cond</i> ... The <code>-ac</code> option is used to define autoloaded condition codes. The <i>cond</i> strings give the names of the conditions defined by the module. The optional <code>-I</code> option is used to define infix condition names. Without this option prefix condition names are defined. </p>
 </dd>
<dl>
<dd> <p> If given no condition names, all defined names are listed (as a series of <code>zmodload</code> commands if the <code>-L</code> option is given). </p>
<p> The <code>-uc</code> option removes definitions for autoloaded conditions. </p>
 </dd></dl>
<dd> <p> <code>zmodload</code> <code>-ap</code> [ <code>-L</code> ] </p>
 </dd>
<dd> <p> <code>zmodload</code> <code>-ap</code> [ <code>-i</code> ] <i>name</i> [ <i>parameter</i> ... ] </p>
 </dd>
<dd> <p> <code>zmodload</code> <code>-up</code> [ <code>-i</code> ] <i>parameter</i> ... The <code>-p</code> option is like the <code>-b</code> and <code>-c</code> options, but makes <code>zmodload</code> work on autoloaded parameters instead. </p>
 </dd>
<dd> <p> <code>zmodload</code> <code>-af</code> [ <code>-L</code> ] </p>
 </dd>
<dd> <p> <code>zmodload</code> <code>-af</code> [ <code>-i</code> ] <i>name</i> [ <i>function</i> ... ] </p>
 </dd>
<dd> <p> <code>zmodload</code> <code>-uf</code> [ <code>-i</code> ] <i>function</i> ... The <code>-f</code> option is like the <code>-b</code>, <code>-p</code>, and <code>-c</code> options, but makes <code>zmodload</code> work on autoloaded math functions instead. </p>
 </dd>
<dd> <p> <code>zmodload</code> <code>-a</code> [ <code>-L</code> ] </p>
 </dd>
<dd> <p> <code>zmodload</code> <code>-a</code> [ <code>-i</code> ] <i>name</i> [ <i>builtin</i> ... ] </p>
 </dd>
<dd> <p> <code>zmodload</code> <code>-ua</code> [ <code>-i</code> ] <i>builtin</i> ... Equivalent to <code>-ab</code> and <code>-ub</code>. </p>
 </dd>
<dt><code>zmodload -e</code> [ <code>-A</code> ] [ <i>string</i> ... ]</dt>
<dd> <p> The <code>-e</code> option without arguments lists all loaded modules; if the <code>-A</code> option is also given, module aliases corresponding to loaded modules are also shown. If arguments are provided, nothing is printed; the return status is set to zero if all <i>string</i>s given as arguments are names of loaded modules and to one if at least on <i>string</i> is not the name of a loaded module. This can be used to test for the availability of things implemented by modules. In this case, any aliases are automatically resolved and the <code>-A</code> flag is not used. </p>
 </dd>
<dt><code>zmodload</code><code>-A</code> [ <code>-L</code> ] [ <i>modalias</i>[<code>=</code><i>module</i>] ... ]</dt>
<dd> <p> For each argument, if both <i>modalias</i> and <i>module</i> are given, define <i>modalias</i> to be an alias for the module <i>module</i>. If the module <i>modalias</i> is ever subsequently requested, either via a call to <code>zmodload</code> or implicitly, the shell will attempt to load <i>module</i> instead. If <i>module</i> is not given, show the definition of <i>modalias</i>. If no arguments are given, list all defined module aliases. When listing, if the <code>-L</code> flag was also given, list the definition as a <code>zmodload</code> command to recreate the alias. </p>
 </dd>
<dl>
<dd> <p> The existence of aliases for modules is completely independent of whether the name resolved is actually loaded as a module: while the alias exists, loading and unloading the module under any alias has exactly the same effect as using the resolved name, and does not affect the connection between the alias and the resolved name which can be removed either by <code>zmodload -R</code> or by redefining the alias. Chains of aliases (i.e. where the first resolved name is itself an alias) are valid so long as these are not circular. As the aliases take the same format as module names, they may include path separators: in this case, there is no requirement for any part of the path named to exist as the alias will be resolved first. For example, `<code>any/old/alias</code>&#8216; is always a valid alias. </p>
<p> Dependencies added to aliased modules are actually added to the resolved module; these remain if the alias is removed. It is valid to create an alias whose name is one of the standard shell modules and which resolves to a different module. However, if a module has dependencies, it will not be possible to use the module name as an alias as the module will already be marked as a loadable module in its own right. </p>
<p> Apart from the above, aliases can be used in the <code>zmodload</code> command anywhere module names are required. However, aliases will not be shown in lists of loaded modules with a bare `<code>zmodload</code>&#8216;. </p>
 </dd></dl>
<dt><code>zmodload</code><code>-R</code><i>modalias</i> ... </dt>
<dd> <p> For each <i>modalias</i> argument that was previously defined as a module alias via <code>zmodload -A</code>, delete the alias. If any was not defined, an error is caused and the remainder of the line is ignored. </p>
 </dd></dl>
<p> Note that <code>zsh</code> makes no distinction between modules that were linked into the shell and modules that are loaded dynamically. In both cases this builtin command has to be used to make available the builtins and other things defined by modules (unless the module is autoloaded on these definitions). This is true even for systems that don&#8217;t support dynamic loading of modules. </dl>
 </p>
<dt><code>zparseopts</code></dt>
<dd> <p> See the section `The zsh/zutil Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dt><code>zprof</code></dt>
<dd> <p> See the section `The zsh/zprof Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dt><code>zpty</code></dt>
<dd> <p> See the section `The zsh/zpty Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dt><code>zregexparse</code></dt>
<dd> <p> See the section `The zsh/zutil Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dt><code>zsocket</code></dt>
<dd> <p> See the section `The zsh/net/socket Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dt><code>zstyle</code></dt>
<dd> <p> See the section `The zsh/zutil Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd>
<dt><code>ztcp</code></dt>
<dd> <p> See the section `The zsh/net/tcp Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
 </dd></dl>
