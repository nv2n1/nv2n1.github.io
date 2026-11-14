---
title: "sh-distrib(1)"
name: "sh-distrib"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sh-distrib/"
description: "dash – command interpreter (shell)"
---

<p><code>dash</code> &#8211; command interpreter (shell) </p>
<h2>Synopsis</h2>
<p>-words [-<code>aCefnuvxIimqVEbp</code> ] [<code>+aCefnuvxIimqVEbp</code> ] -words [-<code>o </code><i>option_name</i> ] [<code>+o </code><i>option_name</i> ] -words [<i>command_file </i>[<i>argument &#8230; </i>] ]<br />
 &#8211;<code>c</code> -words [-<code>aCefnuvxIimqVEbp</code> ] [<code>+aCefnuvxIimqVEbp</code> ] -words [-<code>o </code><i>option_name</i> ] [<code>+o </code><i>option_name</i> ] -words <i>command_string</i> [<i>command_name </i>[<i>argument &#8230; </i>] ]<br />
 &#8211;<code>s</code> -words [-<code>aCefnuvxIimqVEbp</code> ] [<code>+aCefnuvxIimqVEbp</code> ] -words [-<code>o </code><i>option_name</i> ] [<code>+o </code><i>option_name</i> ] -words [<i>argument &#8230;</i> ]</p>
<h2>Description</h2>
<p>is the standard command interpreter for the system. The current version of is in the process of being changed to conform with the <code>POSIX</code> 1003.2 and 1003.2a specifications for the shell. This version has many features which make it appear similar in some respects to the Korn shell, but it is not a Korn shell clone (see <a href="/docs/linux/man/1-ksh/">ksh</a>(1)). Only features designated by <code>POSIX</code> plus a few Berkeley extensions, are being incorporated into this shell. This man page is not intended to be a tutorial or a complete specification of the shell.</p>
<h3>Overview</h3>
<p>The shell is a command that reads lines from either a file or the terminal, interprets them, and generally executes other commands. It is the program that is running when a user logs into the system (although a user can select a different shell with the <a href="/docs/linux/man/1-chsh/">chsh</a>(1) command). The shell implements a language that has flow control constructs, a macro facility that provides a variety of features in addition to data storage, along with built in history and line editing capabilities. It incorporates many features to aid interactive use and has the advantage that the interpretative language is common to both interactive and non-interactive use (shell scripts). That is, commands can be typed directly to the running shell or can be put into a file and the file can be executed directly by the shell.</p>
<h3>Invocation</h3>
<p>If no args are present and if the standard input of the shell is connected to a terminal (or if the &#8211;<code>i</code> flag is set), and the &#8211;<code>c</code> option is not present, the shell is considered an interactive shell. An interactive shell generally prompts before each command and handles programming and command errors differently (as described below). When first starting, the shell inspects argument 0, and if it begins with a dash `-&#8216; the shell is also considered a login shell. This is normally done automatically by the system when the user first logs in. A login shell first reads commands from the files /etc/profile and .profile if they exist. If the environment variable <code>ENV</code> is set on entry to an interactive shell, or is set in the .profile of a login shell, the shell next reads commands from the file named in <code>ENV</code> Therefore, a user should place commands that are to be executed only at login time in the .profile file, and commands that are executed for every interactive shell inside the <code>ENV</code> file. To set the <code>ENV</code> variable to some file, place the following line in your .profile of your home directory </p>
<blockquote><p><tt>ENV=$HOME/.shinit; export ENV</tt></p></blockquote>
<p> substituting for &#8220;.shinit&#8221; any filename you wish. </p>
<p> If command line arguments besides the options have been specified, then the shell treats the first argument as the name of a file from which to read commands (a shell script), and the remaining arguments are set as the positional parameters of the shell ($1, $2, etc). Otherwise, the shell reads commands from its standard input.</p>
<h3>Argument List Processing</h3>
<p>All of the single letter options that have a corresponding name can be used as an argument to the &#8211;<code>o</code> option. The set &#8211;<code>o</code> name is provided next to the single letter option in the description below. Specifying a dash &#8220;-&#8221; turns the option on, while using a plus &#8220;+&#8221; disables the option. The following options can be set from the command line or with the <code>set</code> builtin (described later).</p>
<dl COMPACT>
<dt><code>-a </code><i>allexport</i></p>
<dd>Export all variables assigned to.</p>
<dt><code>-c</code></p>
<dd>Read commands from the <i>command_string</i> operand instead of from the standard input. Special parameter 0 will be set from the <i>command_name</i> operand and the positional parameters ($1, $2, etc.) set from the remaining argument operands.</p>
<dt><code>-C </code><i>noclobber</i></p>
<dd>Don&#8217;t overwrite existing files with &#8220;&gt;&#8221;</p>
<dt><code>-e </code><i>errexit</i></p>
<dd>If not interactive, exit immediately if any untested command fails. The exit status of a command is considered to be explicitly tested if the command is used to control an <code>if</code> <code>elif</code> <code>while</code> or <code>until</code> or if the command is the left hand operand of an &#8220;&amp;&amp;&#8221; or &#8220;||&#8221; operator.</p>
<dt><code>-f </code><i>noglob</i></p>
<dd>Disable pathname expansion.</p>
<dt><code>-n </code><i>noexec</i></p>
<dd>If not interactive, read commands but do not execute them. This is useful for checking the syntax of shell scripts.</p>
<dt><code>-u </code><i>nounset</i></p>
<dd>Write a message to standard error when attempting to expand a variable that is not set, and if the shell is not interactive, exit immediately.</p>
<dt><code>-v </code><i>verbose</i></p>
<dd>The shell writes its input to standard error as it is read. Useful for debugging.</p>
<dt><code>-x </code><i>xtrace</i></p>
<dd>Write each command to standard error (preceded by a `+&nbsp;&#8216; before it is executed. Useful for debugging.</p>
<dt><code>-I </code><i>ignoreeof</i></p>
<dd>Ignore EOF&#8217;s from input when interactive.</p>
<dt><code>-i </code><i>interactive</i></p>
<dd>Force the shell to behave interactively.</p>
<dt><code>-l</code></p>
<dd>Make dash act as if it had been invoked as a login shell.</p>
<dt><code>-m </code><i>monitor</i></p>
<dd>Turn on job control (set automatically when interactive).</p>
<dt><code>-s </code><i>stdin</i></p>
<dd>Read commands from standard input (set automatically if no file arguments are present). This option has no effect when set after the shell has already started running (i.e. with <code>set )</code></p>
<dt><code>-V </code><i>vi</i></p>
<dd>Enable the built-in <a href="/docs/linux/man/1-vi/">vi</a>(1) command line editor (disables &#8211;<code>E</code> if it has been set).</p>
<dt><code>-E </code><i>emacs</i></p>
<dd>Enable the built-in <a href="/docs/linux/man/1-emacs/">emacs</a>(1) command line editor (disables &#8211;<code>V</code> if it has been set).</p>
<dt><code>-b </code><i>notify</i></p>
<dd>Enable asynchronous notification of background job completion. (UNIMPLEMENTED for 4.4alpha)</p>
<dt><code>-p </code><i>priv</i></p>
<dd>Do not attempt to reset effective uid if it does not match uid. This is not set by default to help avoid incorrect usage by setuid root programs via <a href="/docs/linux/man/3-system/">system</a>(3) or <a href="/docs/linux/man/3-popen/">popen</a>(3).</dl>
<h3>Lexical Structure</h3>
<p>The shell reads input in terms of lines from a file and breaks it up into words at whitespace (blanks and tabs), and at certain sequences of characters that are special to the shell called &#8220;operators&#8221; There are two types of operators: control operators and redirection operators (their meaning is discussed later). Following is a list of operators:</p>
<dl COMPACT>
<dt><code>&quot;Control operators:&quot;</code></p>
<dd>
<blockquote><p><tt>&amp; &amp;&amp; ( ) ; ;; | || &lt;newline&gt;</tt></p></blockquote>
<dt><code>&quot;Redirection operators:&quot;</code></p>
<dd>
<blockquote><p><tt>&lt; &gt; &gt;| &lt;&lt; &gt;&gt; &lt;&amp; &gt;&amp; &lt;&lt;- &lt;&gt;</tt></p></blockquote>
</dl>
<h3>Quoting</h3>
<p>Quoting is used to remove the special meaning of certain characters or words to the shell, such as operators, whitespace, or keywords. There are three types of quoting: matched single quotes, matched double quotes, and backslash.</p>
<h3>Backslash</h3>
<p>A backslash preserves the literal meaning of the following character, with the exception of Aq newline . A backslash preceding a Aq newline is treated as a line continuation.</p>
<h3>Single Quotes</h3>
<p>Enclosing characters in single quotes preserves the literal meaning of all the characters (except single quotes, making it impossible to put single-quotes in a single-quoted string).</p>
<h3>Double Quotes</h3>
<p>Enclosing characters within double quotes preserves the literal meaning of all characters except dollarsign ($) backquote (`) and backslash (\) The backslash inside double quotes is historically weird, and serves to quote only the following characters: </p>
<blockquote><p><tt>$ ` &quot; \ &lt;newline&gt;</tt></p></blockquote>
<p> Otherwise it remains literal.</p>
<h3>Reserved Words</h3>
<p>Reserved words are words that have special meaning to the shell and are recognized at the beginning of a line and after a control operator. The following are reserved words:</p>
<dl COMPACT>
<dt><code>! Ta </code>elif Ta fi Ta while Ta case</p>
<dd>
<dt><code>else Ta </code>for Ta then Ta { Ta }</p>
<dd>
<dt><code>do Ta </code>done Ta until Ta if Ta esac</p>
<dd></dl>
<p> Their meaning is discussed later.</p>
<h3>Aliases</h3>
<p>An alias is a name and corresponding value set using the <a href="/docs/linux/man/1-alias/">alias</a>(1) builtin command. Whenever a reserved word may occur (see above), and after checking for reserved words, the shell checks the word to see if it matches an alias. If it does, it replaces it in the input stream with its value. For example, if there is an alias called &#8220;lf&#8221; with the value &#8220;ls -F&#8221; then the input: </p>
<blockquote><p><tt>lf foobar Aq </tt>return </p></blockquote>
<p> would become </p>
<blockquote><p><tt>ls -F foobar Aq </tt>return </p></blockquote>
<p> Aliases provide a convenient way for naive users to create shorthands for commands without having to learn how to create functions with arguments. They can also be used to create lexically obscure code. This use is discouraged.</p>
<h3>Commands</h3>
<p>The shell interprets the words it reads according to a language, the specification of which is outside the scope of this man page (refer to the BNF in the <code>POSIX</code> 1003.2 document). Essentially though, a line is read and if the first word of the line (or after a control operator) is not a reserved word, then the shell has recognized a simple command. Otherwise, a complex command or some other special construct may have been recognized.</p>
<h3>Simple Commands</h3>
<p>If a simple command has been recognized, the shell performs the following actions: </p>
<ol>
<li> Leading words of the form &#8220;name=value&#8221; are stripped off and assigned to the environment of the simple command. Redirection operators and their arguments (as described below) are stripped off and saved for processing.
<li> The remaining words are expanded as described in the section called &#8220;Expansions&#8221; and the first remaining word is considered the command name and the command is located. The remaining words are considered the arguments of the command. If no command name resulted, then the &#8220;name=value&#8221; variable assignments recognized in item 1 affect the current shell.
<li> Redirections are performed as described in the next section. </ol>
<h3>Redirections</h3>
<p>Redirections are used to change where a command reads its input or sends its output. In general, redirections open, close, or duplicate an existing reference to a file. The overall format used for redirection is: </p>
<blockquote><p><tt>[n] </tt><i>redir-op file</i> </p></blockquote>
<p> where <i>redir-op</i> is one of the redirection operators mentioned previously. Following is a list of the possible redirections. The Bq n is an optional number between 0 and 9, as in `3&#8242; (not `Bq 3 ) &#8216; that refers to a file descriptor.</p>
<dl COMPACT>
<dt><code>[n] &gt; file</code></p>
<dd>Redirect standard output (or n) to file.</p>
<dt><code>[n] &gt;| file</code></p>
<dd>Same, but override the &#8211;<code>C</code> option.</p>
<dt><code>[n] &gt;&gt; file</code></p>
<dd>Append standard output (or n) to file.</p>
<dt><code>[n] &lt; file</code></p>
<dd>Redirect standard input (or n) from file.</p>
<dt><code>[n1] &lt;&amp; n2</code></p>
<dd>Copy file descriptor n2 as stdout (or fd n1). fd n2.</p>
<dt><code>[n] &lt;&amp;-</code></p>
<dd>Close standard input (or n).</p>
<dt><code>[n1] &gt;&amp; n2</code></p>
<dd>Copy file descriptor n2 as stdin (or fd n1). fd n2.</p>
<dt><code>[n] &gt;&amp;-</code></p>
<dd>Close standard output (or n).</p>
<dt><code>[n] &lt;&gt; file</code></p>
<dd>Open file for reading and writing on standard input (or n).</dl>
<p> The following redirection is often called a &#8220;here-document&#8221;</p>
<dl COMPACT>
<dt><code>[n]&lt;&lt; delimiter</code></p>
<dd>
<blockquote><p><tt>here-doc-text ...</tt></p></blockquote>
<p> <code>delimiter</code></dl>
<p> All the text on successive lines up to the delimiter is saved away and made available to the command on standard input, or file descriptor n if it is specified. If the delimiter as specified on the initial line is quoted, then the here-doc-text is treated literally, otherwise the text is subjected to parameter expansion, command substitution, and arithmetic expansion (as described in the section on &#8220;Expansions )&#8221; If the operator is &#8220;&lt;&lt;-&#8221; instead of &#8220;&lt;&lt;&#8221; then leading tabs in the here-doc-text are stripped.</p>
<h3>Search and Execution</h3>
<p>There are three types of commands: shell functions, builtin commands, and normal programs &#8212; and the command is searched for (by name) in that order. They each are executed in a different way. </p>
<p> When a shell function is executed, all of the shell positional parameters (except $0, which remains unchanged) are set to the arguments of the shell function. The variables which are explicitly placed in the environment of the command (by placing assignments to them before the function name) are made local to the function and are set to the values given. Then the command given in the function definition is executed. The positional parameters are restored to their original values when the command completes. This all occurs within the current shell. </p>
<p> Shell builtins are executed internally to the shell, without spawning a new process. </p>
<p> Otherwise, if the command name doesn&#8217;t match a function or builtin, the command is searched for as a normal program in the file system (as described in the next section). When a normal program is executed, the shell runs the program, passing the arguments and the environment to the program. If the program is not a normal executable file (i.e., if it does not begin with the &quot;magic number&quot; whose <code>ASCII</code> representation is &quot;#!&quot;, so <a href="/docs/linux/man/2-execve/">execve</a>(2) returns Er ENOEXEC then) the shell will interpret the program in a subshell. The child shell will reinitialize itself in this case, so that the effect will be as if a new shell had been invoked to handle the ad-hoc shell script, except that the location of hashed commands located in the parent shell will be remembered by the child. </p>
<p> Note that previous versions of this document and the source code itself misleadingly and sporadically refer to a shell script without a magic number as a &quot;shell procedure&quot;.</p>
<h3>Path Search</h3>
<p>When locating a command, the shell first looks to see if it has a shell function by that name. Then it looks for a builtin command by that name. If a builtin command is not found, one of two things happen: </p>
<ol>
<li> Command names containing a slash are simply executed without performing any searches.
<li> The shell searches each entry in <code>PATH</code> in turn for the command. The value of the <code>PATH</code> variable should be a series of entries separated by colons. Each entry consists of a directory name. The current directory may be indicated implicitly by an empty directory name, or explicitly by a single period. </ol>
<h3>Command Exit Status</h3>
<p>Each command has an exit status that can influence the behaviour of other shell commands. The paradigm is that a command exits with zero for normal or success, and non-zero for failure, error, or a false indication. The man page for each command should indicate the various exit codes and what they mean. Additionally, the builtin commands return exit codes, as does an executed shell function. </p>
<p> If a command consists entirely of variable assignments then the exit status of the command is that of the last command substitution if any, otherwise 0.</p>
<h3>Complex Commands</h3>
<p>Complex commands are combinations of simple commands with control operators or reserved words, together creating a larger complex command. More generally, a command is one of the following: </p>
<ul>
<li> simple command
<li> pipeline
<li> list or compound-list
<li> compound command
<li> function definition </ul>
<p> Unless otherwise stated, the exit status of a command is that of the last simple command executed by the command.</p>
<h3>Pipelines</h3>
<p>A pipeline is a sequence of one or more commands separated by the control operator |. The standard output of all but the last command is connected to the standard input of the next command. The standard output of the last command is inherited from the shell, as usual. </p>
<p> The format for a pipeline is: </p>
<blockquote><p><tt>[!] command1 [ | command2 ...]</tt></p></blockquote>
<p> The standard output of command1 is connected to the standard input of command2. The standard input, standard output, or both of a command is considered to be assigned by the pipeline before any redirection specified by redirection operators that are part of the command. </p>
<p> If the pipeline is not in the background (discussed later), the shell waits for all commands to complete. </p>
<p> If the reserved word ! does not precede the pipeline, the exit status is the exit status of the last command specified in the pipeline. Otherwise, the exit status is the logical NOT of the exit status of the last command. That is, if the last command returns zero, the exit status is 1; if the last command returns greater than zero, the exit status is zero. </p>
<p> Because pipeline assignment of standard input or standard output or both takes place before redirection, it can be modified by redirection. For example: </p>
<blockquote><p><tt>$ command1 2&gt;&amp;1 | command2</tt></p></blockquote>
<p> sends both the standard output and standard error of command1 to the standard input of command2. </p>
<p> A ; or Aq newline terminator causes the preceding AND-OR-list (described next) to be executed sequentially; a &amp; causes asynchronous execution of the preceding AND-OR-list. </p>
<p> Note that unlike some other shells, each process in the pipeline is a child of the invoking shell (unless it is a shell builtin, in which case it executes in the current shell &#8212; but any effect it has on the environment is wiped).</p>
<h3>Background Commands &#8212;</h3>
<p>If a command is terminated by the control operator ampersand (&amp;), the shell executes the command asynchronously &#8212; that is, the shell does not wait for the command to finish before executing the next command. </p>
<p> The format for running a command in background is: </p>
<blockquote><p><tt>command1 &amp; [command2 &amp; ...]</tt></p></blockquote>
<p> If the shell is not interactive, the standard input of an asynchronous command is set to /dev/null</p>
<h3>Lists &#8212; Generally Speaking</h3>
<p>A list is a sequence of zero or more commands separated by newlines, semicolons, or ampersands, and optionally terminated by one of these three characters. The commands in a list are executed in the order they are written. If command is followed by an ampersand, the shell starts the command and immediately proceeds onto the next command; otherwise it waits for the command to terminate before proceeding to the next one.</p>
<h3>Short-Circuit List Operators</h3>
<p>&#8220;&amp;&amp;&#8221; and &#8220;||&#8221; are AND-OR list operators. &#8220;&amp;&amp;&#8221; executes the first command, and then executes the second command if and only if the exit status of the first command is zero. &#8220;||&#8221; is similar, but executes the second command if and only if the exit status of the first command is nonzero. &#8220;&amp;&amp;&#8221; and &#8220;||&#8221; both have the same priority.</p>
<h3>Flow-Control Constructs &#8212; if, while, for, case</h3>
<p>The syntax of the if command is </p>
<blockquote>
<pre>if list
then list
[ elif list
then list ] ...
[ else list ]
fi</pre>
</blockquote>
<p> The syntax of the while command is </p>
<blockquote>
<pre>while list
do list
done</pre>
</blockquote>
<p> The two lists are executed repeatedly while the exit status of the first list is zero. The until command is similar, but has the word until in place of while, which causes it to repeat until the exit status of the first list is zero. </p>
<p> The syntax of the for command is </p>
<blockquote>
<pre>for variable [ in [ word ... ] ]
do list
done</pre>
</blockquote>
<p> The words following in are expanded, and then the list is executed repeatedly with the variable set to each word in turn. Omitting in word &#8230; is equivalent to in &quot;$@&quot;. </p>
<p> The syntax of the break and continue command is </p>
<blockquote>
<pre>break [ num ]
continue [ num ]</pre>
</blockquote>
<p> Break terminates the num innermost for or while loops. Continue continues with the next iteration of the innermost loop. These are implemented as builtin commands. </p>
<p> The syntax of the case command is </p>
<blockquote>
<pre>case word in
[(]pattern) list ;;
...
esac</pre>
</blockquote>
<p> The pattern can actually be one or more patterns (see Sx Shell Patterns described later), separated by &#8220;|&#8221; characters. The Do ( Dc character before the pattern is optional.</p>
<h3>Grouping Commands Together</h3>
<p>Commands may be grouped by writing either </p>
<blockquote><p><tt>(list)</tt></p></blockquote>
<p> or </p>
<blockquote><p><tt>{ list;</tt></p></blockquote>
<p> The first of these executes the commands in a subshell. Builtin commands grouped into a (list) will not affect the current shell. The second form does not fork another shell so is slightly more efficient. Grouping commands together this way allows you to redirect their output as though they were one program: </p>
<blockquote>
<pre>{ printf &quot; hello &quot; ; printf &quot; world
&quot; ; } &gt; greeting</pre>
</blockquote>
<p> Note that &#8220;}&#8221; must follow a control operator (here, &#8220;;&#8221; so that it is recognized as a reserved word and not as another command argument.</p>
<h3>Functions</h3>
<p>The syntax of a function definition is </p>
<blockquote><p><tt>name ( ) command</tt></p></blockquote>
<p> A function definition is an executable statement; when executed it installs a function named name and returns an exit status of zero. The command is normally a list enclosed between &#8220;{&#8221; and &#8220;}&#8221; </p>
<p> Variables may be declared to be local to a function by using a local command. This should appear as the first statement of a function, and the syntax is </p>
<blockquote><p><tt>local [ variable | - ] ...</tt></p></blockquote>
<p> Local is implemented as a builtin command. </p>
<p> When a variable is made local, it inherits the initial value and exported and readonly flags from the variable with the same name in the surrounding scope, if there is one. Otherwise, the variable is initially unset. The shell uses dynamic scoping, so that if you make the variable x local to function f, which then calls function g, references to the variable x made inside g will refer to the variable x declared inside f, not to the global variable named x. </p>
<p> The only special parameter that can be made local is &#8220;-&#8221; Making &#8220;-&#8221; local any shell options that are changed via the set command inside the function to be restored to their original values when the function returns. </p>
<p> The syntax of the return command is </p>
<blockquote><p><tt>return [ exitstatus</tt></p></blockquote>
<p> It terminates the currently executing function. Return is implemented as a builtin command.</p>
<h3>Variables and Parameters</h3>
<p>The shell maintains a set of parameters. A parameter denoted by a name is called a variable. When starting up, the shell turns all the environment variables into shell variables. New variables can be set using the form </p>
<blockquote><p><tt>name=value</tt></p></blockquote>
<p> Variables set by the user must have a name consisting solely of alphabetics, numerics, and underscores &#8211; the first of which must not be numeric. A parameter can also be denoted by a number or a special character as explained below.</p>
<h3>Positional Parameters</h3>
<p>A positional parameter is a parameter denoted by a number (n &gt; 0). The shell sets these initially to the values of its command line arguments that follow the name of the shell script. The <code>set</code> builtin can also be used to set or reset them.</p>
<h3>Special Parameters</h3>
<p>A special parameter is a parameter denoted by one of the following special characters. The value of the parameter is listed next to its character.</p>
<dl COMPACT>
<dt><code>*</code></p>
<dd>Expands to the positional parameters, starting from one. When the expansion occurs within a double-quoted string it expands to a single field with the value of each parameter separated by the first character of the <code>IFS</code> variable, or by a Aq space if <code>IFS</code> is unset.</p>
<dt><code>@</code></p>
<dd>Expands to the positional parameters, starting from one. When the expansion occurs within double-quotes, each positional parameter expands as a separate argument. If there are no positional parameters, the expansion of @ generates zero arguments, even when @ is double-quoted. What this basically means, for example, is if $1 is &#8220;abc&#8221; and $2 is &#8220;def ghi&#8221; then Qq $@ expands to the two arguments: </p>
<blockquote><p><tt>&quot; abc &quot; &nbsp; &quot; def ghi &quot;</tt></p></blockquote>
<dt><code>#</code></p>
<dd>Expands to the number of positional parameters.</p>
<dt><code>?</code></p>
<dd>Expands to the exit status of the most recent pipeline.</p>
<dt><code>&#8211; (Hyphen.)</code></p>
<dd>Expands to the current option flags (the single-letter option names concatenated into a string) as specified on invocation, by the set builtin command, or implicitly by the shell.</p>
<dt><code>$</code></p>
<dd>Expands to the process ID of the invoked shell. A subshell retains the same value of $ as its parent.</p>
<dt><code>!</code></p>
<dd>Expands to the process ID of the most recent background command executed from the current shell. For a pipeline, the process ID is that of the last command in the pipeline.</p>
<dt><code>0 (Zero.)</code></p>
<dd>Expands to the name of the shell or shell script.</dl>
<h3>Word Expansions</h3>
<p>This clause describes the various expansions that are performed on words. Not all expansions are performed on every word, as explained later. </p>
<p> Tilde expansions, parameter expansions, command substitutions, arithmetic expansions, and quote removals that occur within a single word expand to a single field. It is only field splitting or pathname expansion that can create multiple fields from a single word. The single exception to this rule is the expansion of the special parameter @ within double-quotes, as was described above. </p>
<p> The order of word expansion is: </p>
<ol>
<li> Tilde Expansion, Parameter Expansion, Command Substitution, Arithmetic Expansion (these all occur at the same time).
<li> Field Splitting is performed on fields generated by step (1) unless the <code>IFS</code> variable is null.
<li> Pathname Expansion (unless set &#8211;<code>f</code> is in effect).
<li> Quote Removal. </ol>
<p> The $ character is used to introduce parameter expansion, command substitution, or arithmetic evaluation.</p>
<h3>Tilde Expansion (substituting a user&#8217;s home directory)</h3>
<p>A word beginning with an unquoted tilde character (~) is subjected to tilde expansion. All the characters up to a slash (/) or the end of the word are treated as a username and are replaced with the user&#8217;s home directory. If the username is missing (as in ~/foobar ) the tilde is replaced with the value of the <i>HOME</i> variable (the current user&#8217;s home directory).</p>
<h3>Parameter Expansion</h3>
<p>The format for parameter expansion is as follows: </p>
<blockquote><p><tt>${expression}</tt></p></blockquote>
<p> where expression consists of all characters until the matching &#8220;}&#8221; Any &#8220;}&#8221; escaped by a backslash or within a quoted string, and characters in embedded arithmetic expansions, command substitutions, and variable expansions, are not examined in determining the matching &#8220;}&#8221; </p>
<p> The simplest form for parameter expansion is: </p>
<blockquote><p><tt>${parameter}</tt></p></blockquote>
<p> The value, if any, of parameter is substituted. </p>
<p> The parameter name or symbol can be enclosed in braces, which are optional except for positional parameters with more than one digit or when parameter is followed by a character that could be interpreted as part of the name. If a parameter expansion occurs inside double-quotes: </p>
<ol>
<li> Pathname expansion is not performed on the results of the expansion.
<li> Field splitting is not performed on the results of the expansion, with the exception of @. </ol>
<p> In addition, a parameter expansion can be modified by using one of the following formats.</p>
<dl COMPACT>
<dt><code>${parameter:-word}</code></p>
<dd>Use Default Values. If parameter is unset or null, the expansion of word is substituted; otherwise, the value of parameter is substituted.</p>
<dt><code>${parameter:=word}</code></p>
<dd>Assign Default Values. If parameter is unset or null, the expansion of word is assigned to parameter. In all cases, the final value of parameter is substituted. Only variables, not positional parameters or special parameters, can be assigned in this way.</p>
<dt><code>${parameter:?[word]}</code></p>
<dd>Indicate Error if Null or Unset. If parameter is unset or null, the expansion of word (or a message indicating it is unset if word is omitted) is written to standard error and the shell exits with a nonzero exit status. Otherwise, the value of parameter is substituted. An interactive shell need not exit.</p>
<dt><code>${parameter:+word}</code></p>
<dd>Use Alternative Value. If parameter is unset or null, null is substituted; otherwise, the expansion of word is substituted.</dl>
<p> In the parameter expansions shown previously, use of the colon in the format results in a test for a parameter that is unset or null; omission of the colon results in a test for a parameter that is only unset.</p>
<dl COMPACT>
<dt><code>${#parameter}</code></p>
<dd>String Length. The length in characters of the value of parameter.</dl>
<p> The following four varieties of parameter expansion provide for substring processing. In each case, pattern matching notation (see Sx Shell Patterns ) , rather than regular expression notation, is used to evaluate the patterns. If parameter is * or @, the result of the expansion is unspecified. Enclosing the full parameter expansion string in double-quotes does not cause the following four varieties of pattern characters to be quoted, whereas quoting characters within the braces has this effect.</p>
<dl COMPACT>
<dt><code>${parameter%word}</code></p>
<dd>Remove Smallest Suffix Pattern. The word is expanded to produce a pattern. The parameter expansion then results in parameter, with the smallest portion of the suffix matched by the pattern deleted.</p>
<dt><code>${parameter%%word}</code></p>
<dd>Remove Largest Suffix Pattern. The word is expanded to produce a pattern. The parameter expansion then results in parameter, with the largest portion of the suffix matched by the pattern deleted.</p>
<dt><code>${parameter#word}</code></p>
<dd>Remove Smallest Prefix Pattern. The word is expanded to produce a pattern. The parameter expansion then results in parameter, with the smallest portion of the prefix matched by the pattern deleted.</p>
<dt><code>${parameter##word}</code></p>
<dd>Remove Largest Prefix Pattern. The word is expanded to produce a pattern. The parameter expansion then results in parameter, with the largest portion of the prefix matched by the pattern deleted.</dl>
<h3>Command Substitution</h3>
<p>Command substitution allows the output of a command to be substituted in place of the command name itself. Command substitution occurs when the command is enclosed as follows: </p>
<blockquote><p><tt>$(command)</tt></p></blockquote>
<p> or Po &#8220;backquoted&#8221; version Pc : </p>
<blockquote><p><tt>`command`</tt></p></blockquote>
<p> The shell expands the command substitution by executing command in a subshell environment and replacing the command substitution with the standard output of the command, removing sequences of one or more Ao newline Ac Ns s at the end of the substitution. (Embedded Ao newline Ac Ns s before the end of the output are not removed; however, during field splitting, they may be translated into Ao space Ac Ns s , depending on the value of <code>IFS</code> and quoting that is in effect.)</p>
<h3>Arithmetic Expansion</h3>
<p>Arithmetic expansion provides a mechanism for evaluating an arithmetic expression and substituting its value. The format for arithmetic expansion is as follows: </p>
<blockquote><p><tt>$((expression))</tt></p></blockquote>
<p> The expression is treated as if it were in double-quotes, except that a double-quote inside the expression is not treated specially. The shell expands all tokens in the expression for parameter expansion, command substitution, and quote removal. </p>
<p> Next, the shell treats this as an arithmetic expression and substitutes the value of the expression.</p>
<h3>White Space Splitting (Field Splitting)</h3>
<p>After parameter expansion, command substitution, and arithmetic expansion the shell scans the results of expansions and substitutions that did not occur in double-quotes for field splitting and multiple fields can result. </p>
<p> The shell treats each character of the <code>IFS</code> as a delimiter and uses the delimiters to split the results of parameter expansion and command substitution into fields.</p>
<h3>Pathname Expansion (File Name Generation)</h3>
<p>Unless the &#8211;<code>f</code> flag is set, file name generation is performed after word splitting is complete. Each word is viewed as a series of patterns, separated by slashes. The process of expansion replaces the word with the names of all existing files whose names can be formed by replacing each pattern with a string that matches the specified pattern. There are two restrictions on this: first, a pattern cannot match a string containing a slash, and second, a pattern cannot match a string starting with a period unless the first character of the pattern is a period. The next section describes the patterns used for both Pathname Expansion and the <code>case</code> command.</p>
<h3>Shell Patterns</h3>
<p>A pattern consists of normal characters, which match themselves, and meta-characters. The meta-characters are &#8220;!&#8221; &#8220;*&#8221; &#8220;?&#8221; and &#8220;[&#8221; These characters lose their special meanings if they are quoted. When command or variable substitution is performed and the dollar sign or back quotes are not double quoted, the value of the variable or the output of the command is scanned for these characters and they are turned into meta-characters. </p>
<p> An asterisk (&#8220;*&#8221; ) matches any string of characters. A question mark matches any single character. A left bracket (&#8220;[&#8221; ) introduces a character class. The end of the character class is indicated by a (&#8220;]&#8221; ) if the &#8220;]&#8221; is missing then the &#8220;[&#8221; matches a &#8220;[&#8221; rather than introducing a character class. A character class matches any of the characters between the square brackets. A range of characters may be specified using a minus sign. The character class may be complemented by making an exclamation point the first character of the character class. </p>
<p> To include a &#8220;]&#8221; in a character class, make it the first character listed (after the &#8220;!&#8221; if any). To include a minus sign, make it the first or last character listed.</p>
<h3>Builtins</h3>
<p>This section lists the builtin commands which are builtin because they need to perform some operation that can&#8217;t be performed by a separate process. In addition to these, there are several other commands that may be builtin for efficiency (e.g. <a href="/docs/linux/man/1-printf/">printf</a>(1), <a href="/docs/linux/man/1-echo/">echo</a>(1), <a href="/docs/linux/man/1-test/">test</a>(1), etc).</p>
<dl COMPACT>
<dt><code>:</code></p>
<dd>
<dt><code>true</code></p>
<dd>A null command that returns a 0 (true) exit value.</p>
<dt><code>. file</code></p>
<dd>The commands in the specified file are read and executed by the shell.</p>
<dt><code>alias </code>[<i>name </i>[<i>=string &#8230;</i> ] ]</p>
<dd>If <i>name=string</i> is specified, the shell defines the alias <i>name</i> with value <i>string</i> If just <i>name</i> is specified, the value of the alias <i>name</i> is printed. With no arguments, the <code>alias</code> builtin prints the names and values of all defined aliases (see <code>unalias )</code></p>
<dt><code>bg [ </code><i>job ] &#8230;</i></p>
<dd>Continue the specified jobs (or the current job if no jobs are given) in the background.</p>
<dt><code> command</code> [-<code>p</code> ] [-<code>v</code> ] [-<code>V</code> ] <i>command</i> [<i>arg &#8230;</i> ]</p>
<dd>
<dd>Execute the specified command but ignore shell functions when searching for it. (This is useful when you have a shell function with the same name as a builtin command.)</p>
<dl COMPACT>
<dt><code>-p</code></p>
<dd>search for command using a <code>PATH</code> that guarantees to find all the standard utilities.</p>
<dt><code>-V</code></p>
<dd>Do not execute the command but search for the command and print the resolution of the command search. This is the same as the type builtin.</p>
<dt><code>-v</code></p>
<dd>Do not execute the command but search for the command and print the absolute pathname of utilities, the name for builtins or the expansion of aliases.</dl>
<dt><code>cd </code><i>file &#8230;</i></p>
<dd>
<dt><code> cd </code>[-<code>LP</code> ] [<i>directory</i> ]</p>
<dd>
<dd>Switch to the specified directory (default <code>HOME )</code> If an entry for <code>CDPATH</code> appears in the environment of the <code>cd</code> command or the shell variable <code>CDPATH</code> is set and the directory name does not begin with a slash, then the directories listed in <code>CDPATH</code> will be searched for the specified directory. The format of <code>CDPATH</code> is the same as that of <code>PATH</code> If a single dash is specified as the argument, it will be replaced by the value of <code>OLDPWD</code> The <code>cd</code> command will print out the name of the directory that it actually switched to if this is different from the name that the user gave. These may be different either because the <code>CDPATH</code> mechanism was used or because the argument is a single dash. The &#8211;<code>P</code> option causes the physical directory structure to be used, that is, all symbolic links are resolved to their respective values. The &#8211;<code>L</code> option turns off the effect of any preceding &#8211;<code>P</code> options.</p>
<dt><code> echo </code>[-<code>n</code> ] <i>args&#8230; </i></p>
<dd>
<dd>Print the arguments on the standard output, separated by spaces. Unless the &#8211;<code>n</code> option is present, a newline is output following the arguments. </p>
<p> If any of the following sequences of characters is encountered during output, the sequence is not output. Instead, the specified action is performed:</p>
<dl COMPACT>
<dt><code></code></p>
<dd>A backspace character is output.</p>
<dt><code>
