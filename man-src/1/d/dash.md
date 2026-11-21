---
title: "dash(1)"
name: "dash"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dash/"
description: "dash – command interpreter (shell)"
---
<h2 class="name">NAME</h2>
<p> <code>dash</code> - command interpreter (shell) </p>
<h2>SYNOPSIS</h2>
<p> <code>dash</code> [-<code>aCefnuvxIimqVEbp</code> ] [<code>+aCefnuvxIimqVEbp</code> ] [-<code>o </code><i>option_name</i> ] [<code>+o </code><i>option_name</i> ] [<i>command_file </i>[<i>argument ... </i>] ] <br />
<code>dash</code> -<code>c</code> [-<code>aCefnuvxIimqVEbp</code> ] [<code>+aCefnuvxIimqVEbp</code> ] [-<code>o </code><i>option_name</i> ] [<code>+o </code><i>option_name</i> ] <i>command_string</i> [<i>command_name </i>[<i>argument ... </i>] ] <br />
<code>dash</code> -<code>s</code> [-<code>aCefnuvxIimqVEbp</code> ] [<code>+aCefnuvxIimqVEbp</code> ] [-<code>o </code><i>option_name</i> ] [<code>+o </code><i>option_name</i> ] [<i>argument ...</i> ]  </p>
<h2>DESCRIPTION</h2>
<p> <code>dash</code> is the standard command interpreter for the system. The current version of <code>dash</code> is in the process of being changed to conform with the <code>POSIX</code> 1003.2 and 1003.2a specifications for the shell. This version has many features which make it appear similar in some respects to the Korn shell, but it is not a Korn shell clone (see ksh(1)). Only features designated by <code>POSIX</code> plus a few Berkeley extensions, are being incorporated into this shell. This man page is not intended to be a tutorial or a complete specification of the shell.  </p>
<h3>Overview</h3>
<p> The shell is a command that reads lines from either a file or the terminal, interprets them, and generally executes other commands. It is the program that is running when a user logs into the system (although a user can select a different shell with the <a href="/docs/linux/man/1-chsh/">chsh</a>(1) command). The shell implements a language that has flow control constructs, a macro facility that provides a variety of features in addition to data storage, along with built in history and line editing capabilities. It incorporates many features to aid interactive use and has the advantage that the interpretative language is common to both interactive and non-interactive use (shell scripts). That is, commands can be typed directly to the running shell or can be put into a file and the file can be executed directly by the shell.  </p>
<h3>Invocation</h3>
<p> If no args are present and if the standard input of the shell is connected to a terminal (or if the -<code>i</code> flag is set), and the -<code>c</code> option is not present, the shell is considered an interactive shell. An interactive shell generally prompts before each command and handles programming and command errors differently (as described below). When first starting, the shell inspects argument 0, and if it begins with a dash `-&#8216; the shell is also considered a login shell. This is normally done automatically by the system when the user first logs in. A login shell first reads commands from the files /etc/profile and .profile if they exist. If the environment variable <code>ENV</code> is set on entry to an interactive shell, or is set in the .profile of a login shell, the shell next reads commands from the file named in <code>ENV</code> Therefore, a user should place commands that are to be executed only at login time in the .profile file, and commands that are executed for every interactive shell inside the <code>ENV</code> file. To set the <code>ENV</code> variable to some file, place the following line in your .profile of your home directory </p>
<blockquote><p> <code>ENV=$HOME/.shinit; export ENV</code> </p>
</blockquote>
<p> substituting for ``.shinit&#8217;&#8216; any filename you wish. </p>
<p> If command line arguments besides the options have been specified, then the shell treats the first argument as the name of a file from which to read commands (a shell script), and the remaining arguments are set as the positional parameters of the shell ($1, $2, etc). Otherwise, the shell reads commands from its standard input.  </p>
<h3>Argument List Processing</h3>
<p> All of the single letter options that have a corresponding name can be used as an argument to the -<code>o</code> option. The set -<code>o</code> name is provided next to the single letter option in the description below. Specifying a dash ``-&#8216;&#8216; turns the option on, while using a plus ``+&#8216;&#8216; disables the option. The following options can be set from the command line or with the <code>set</code> builtin (described later). </p>
<dl>
<dt><code>-a </code><i>allexport</i></dt>
<dd> <p> Export all variables assigned to. </p>
 </dd>
<dt><code>-c</code></dt>
<dd> <p> Read commands from the <i>command_string</i> operand instead of from the standard input. Special parameter 0 will be set from the <i>command_name</i> operand and the positional parameters ($1, $2, etc.) set from the remaining argument operands. </p>
 </dd>
<dt><code>-C </code><i>noclobber</i></dt>
<dd> <p> Don&#8217;t overwrite existing files with ``&gt;&#8216;&#8216; </p>
 </dd>
<dt><code>-e </code><i>errexit</i></dt>
<dd> <p> If not interactive, exit immediately if any untested command fails. The exit status of a command is considered to be explicitly tested if the command is used to control an <code>if</code> <code>elif</code> <code>while</code> or <code>until</code> or if the command is the left hand operand of an ``&amp;&amp;&#8216;&#8216; or ``||&#8216;&#8216; operator. </p>
 </dd>
<dt><code>-f </code><i>noglob</i></dt>
<dd> <p> Disable pathname expansion. </p>
 </dd>
<dt><code>-n </code><i>noexec</i></dt>
<dd> <p> If not interactive, read commands but do not execute them. This is useful for checking the syntax of shell scripts. </p>
 </dd>
<dt><code>-u </code><i>nounset</i></dt>
<dd> <p> Write a message to standard error when attempting to expand a variable that is not set, and if the shell is not interactive, exit immediately. </p>
 </dd>
<dt><code>-v </code><i>verbose</i></dt>
<dd> <p> The shell writes its input to standard error as it is read. Useful for debugging. </p>
 </dd>
<dt><code>-x </code><i>xtrace</i></dt>
<dd> <p> Write each command to standard error (preceded by a `+&nbsp;&#8216; before it is executed. Useful for debugging. </p>
 </dd>
<dt><code>-I </code><i>ignoreeof</i></dt>
<dd> <p> Ignore EOF&#8217;s from input when interactive. </p>
 </dd>
<dt><code>-i </code><i>interactive</i></dt>
<dd> <p> Force the shell to behave interactively. </p>
 </dd>
<dt><code>-l</code></dt>
<dd> <p> Make dash act as if it had been invoked as a login shell. </p>
 </dd>
<dt><code>-m </code><i>monitor</i></dt>
<dd> <p> Turn on job control (set automatically when interactive). </p>
 </dd>
<dt><code>-s </code><i>stdin</i></dt>
<dd> <p> Read commands from standard input (set automatically if no file arguments are present). This option has no effect when set after the shell has already started running (i.e. with <code>set )</code> </p>
 </dd>
<dt><code>-V </code><i>vi</i></dt>
<dd> <p> Enable the built-in <a href="/docs/linux/man/1-vi/">vi</a>(1) command line editor (disables -<code>E</code> if it has been set). </p>
 </dd>
<dt><code>-E </code><i>emacs</i></dt>
<dd> <p> Enable the built-in <a href="/docs/linux/man/1-emacs/">emacs</a>(1) command line editor (disables -<code>V</code> if it has been set). </p>
 </dd>
<dt><code>-b </code><i>notify</i></dt>
<dd> <p> Enable asynchronous notification of background job completion. (UNIMPLEMENTED for 4.4alpha) </p>
 </dd>
<dt><code>-p </code><i>priviliged</i></dt>
<dd> <p> Do not attempt to reset effective uid if it does not match uid. This is not set by default to help avoid incorrect usage by setuid root programs via <a href="/docs/linux/man/3-system/">system</a>(3) or <a href="/docs/linux/man/3-popen/">popen</a>(3). </p>
 </dd></dl>
<h3>Lexical Structure</h3>
<p> The shell reads input in terms of lines from a file and breaks it up into words at whitespace (blanks and tabs), and at certain sequences of characters that are special to the shell called ``operators&#8217;&#8216; There are two types of operators: control operators and redirection operators (their meaning is discussed later). Following is a list of operators: </p>
<dl>
<dt><code>&quot;Control operators:&quot;</code></dt>
<dd> <blockquote><p> <code>&amp; &amp;&amp; ( ) ; ;; | || &lt;newline&gt;</code> </p>
</blockquote>
 </dd>
<dt><code>&quot;Redirection operators:&quot;</code></dt>
<dd> <blockquote><p> <code>&lt; &gt; &gt;| &lt;&lt; &gt;&gt; &lt;&amp; &gt;&amp; &lt;&lt;- &lt;&gt;</code> </p>
</blockquote>
 </dd></dl>
<h3>Quoting</h3>
<p> Quoting is used to remove the special meaning of certain characters or words to the shell, such as operators, whitespace, or keywords. There are three types of quoting: matched single quotes, matched double quotes, and backslash.  </p>
<h3>Backslash</h3>
<p> A backslash preserves the literal meaning of the following character, with the exception of Aq newline . A backslash preceding a Aq newline is treated as a line continuation.  </p>
<h3>Single Quotes</h3>
<p> Enclosing characters in single quotes preserves the literal meaning of all the characters (except single quotes, making it impossible to put single-quotes in a single-quoted string).  </p>
<h3>Double Quotes</h3>
<p> Enclosing characters within double quotes preserves the literal meaning of all characters except dollarsign ($) backquote (`) and backslash (\) The backslash inside double quotes is historically weird, and serves to quote only the following characters: </p>
<blockquote><p> <code>$ ` &quot; \ &lt;newline&gt;</code> </p>
</blockquote>
<p> Otherwise it remains literal.  </p>
<h3>Reserved Words</h3>
<p> Reserved words are words that have special meaning to the shell and are recognized at the beginning of a line and after a control operator. The following are reserved words: </p>
<dl>
<dt><code>! Ta </code>elif Ta fi Ta while Ta case </dt>
<dd>  </dd>
<dt><code>else Ta </code>for Ta then Ta { Ta } </dt>
<dd>  </dd>
<dt><code>do Ta </code>done Ta until Ta if Ta esac </dt>
<dd>  </dd></dl>
<p> Their meaning is discussed later.  </p>
<h3>Aliases</h3>
<p> An alias is a name and corresponding value set using the <a href="/docs/linux/man/1-alias/">alias</a>(1) builtin command. Whenever a reserved word may occur (see above), and after checking for reserved words, the shell checks the word to see if it matches an alias. If it does, it replaces it in the input stream with its value. For example, if there is an alias called ``lf&#8217;&#8216; with the value ``ls -F&#8217;&#8216; then the input: </p>
<blockquote><p> <code>lf foobar Aq </code>return </p>
</blockquote>
<p> would become </p>
<blockquote><p> <code>ls -F foobar Aq </code>return </p>
</blockquote>
<p> Aliases provide a convenient way for naive users to create shorthands for commands without having to learn how to create functions with arguments. They can also be used to create lexically obscure code. This use is discouraged.  </p>
<h3>Commands</h3>
<p> The shell interprets the words it reads according to a language, the specification of which is outside the scope of this man page (refer to the BNF in the <code>POSIX</code> 1003.2 document). Essentially though, a line is read and if the first word of the line (or after a control operator) is not a reserved word, then the shell has recognized a simple command. Otherwise, a complex command or some other special construct may have been recognized.  </p>
<h3>Simple Commands</h3>
<p> If a simple command has been recognized, the shell performs the following actions: </p>
<ol>
<li> <p> Leading words of the form ``name=value&#8217;&#8216; are stripped off and assigned to the environment of the simple command. Redirection operators and their arguments (as described below) are stripped off and saved for processing.  </li>
<li>  The remaining words are expanded as described in the section called ``Expansions&#8217;&#8216; and the first remaining word is considered the command name and the command is located. The remaining words are considered the arguments of the command. If no command name resulted, then the ``name=value&#8217;&#8216; variable assignments recognized in item 1 affect the current shell.  </li>
<li>  Redirections are performed as described in the next section.  </li>
</ol>
 </p>
<h3>Redirections</h3>
<p> Redirections are used to change where a command reads its input or sends its output. In general, redirections open, close, or duplicate an existing reference to a file. The overall format used for redirection is: </p>
<blockquote><p> <code>[n] </code><i>redir-op file</i> </p>
</blockquote>
<p> where <i>redir-op</i> is one of the redirection operators mentioned previously. Following is a list of the possible redirections. The Bq n is an optional number between 0 and 9, as in `3&#8217; (not `Bq 3 ) &#8216; that refers to a file descriptor. </p>
<dl>
<dt><code>[n] &gt; file</code></dt>
<dd> <p> Redirect standard output (or n) to file. </p>
 </dd>
<dt><code>[n] &gt;| file</code></dt>
<dd> <p> Same, but override the -<code>C</code> option. </p>
 </dd>
<dt><code>[n] &gt;&gt; file</code></dt>
<dd> <p> Append standard output (or n) to file. </p>
 </dd>
<dt><code>[n] &lt; file</code></dt>
<dd> <p> Redirect standard input (or n) from file. </p>
 </dd>
<dt><code>[n1] &lt;&amp; n2</code></dt>
<dd> <p> Copy file descriptor n2 as stdout (or fd n1). fd n2. </p>
 </dd>
<dt><code>[n] &lt;&amp;-</code></dt>
<dd> <p> Close standard input (or n). </p>
 </dd>
<dt><code>[n1] &gt;&amp; n2</code></dt>
<dd> <p> Copy file descriptor n2 as stdin (or fd n1). fd n2. </p>
 </dd>
<dt><code>[n] &gt;&amp;-</code></dt>
<dd> <p> Close standard output (or n). </p>
 </dd>
<dt><code>[n] &lt;&gt; file</code></dt>
<dd> <p> Open file for reading and writing on standard input (or n). </p>
 </dd></dl>
<p> The following redirection is often called a ``here-document&#8217;&#8216; </p>
<dl>
<dt><code>[n]&lt;&lt; delimiter</code></dt>
<dd> <blockquote><p> <code>here-doc-text ...</code> </p>
</blockquote>
<p> <code>delimiter</code> </p>
 </dd></dl>
<p> All the text on successive lines up to the delimiter is saved away and made available to the command on standard input, or file descriptor n if it is specified. If the delimiter as specified on the initial line is quoted, then the here-doc-text is treated literally, otherwise the text is subjected to parameter expansion, command substitution, and arithmetic expansion (as described in the section on ``Expansions )&#8216;&#8216; If the operator is ``&lt;&lt;-&#8216;&#8216; instead of ``&lt;&lt;&#8216;&#8216; then leading tabs in the here-doc-text are stripped.  </p>
<h3>Search and Execution</h3>
<p> There are three types of commands: shell functions, builtin commands, and normal programs - and the command is searched for (by name) in that order. They each are executed in a different way. </p>
<p> When a shell function is executed, all of the shell positional parameters (except $0, which remains unchanged) are set to the arguments of the shell function. The variables which are explicitly placed in the environment of the command (by placing assignments to them before the function name) are made local to the function and are set to the values given. Then the command given in the function definition is executed. The positional parameters are restored to their original values when the command completes. This all occurs within the current shell. </p>
<p> Shell builtins are executed internally to the shell, without spawning a new process. </p>
<p> Otherwise, if the command name doesn&#8217;t match a function or builtin, the command is searched for as a normal program in the file system (as described in the next section). When a normal program is executed, the shell runs the program, passing the arguments and the environment to the program. If the program is not a normal executable file (i.e., if it does not begin with the &quot;magic number&quot; whose <code>ASCII</code> representation is &quot;#!&quot;, so <a href="/docs/linux/man/2-execve/">execve</a>(2) returns Er ENOEXEC then) the shell will interpret the program in a subshell. The child shell will reinitialize itself in this case, so that the effect will be as if a new shell had been invoked to handle the ad-hoc shell script, except that the location of hashed commands located in the parent shell will be remembered by the child. </p>
<p> Note that previous versions of this document and the source code itself misleadingly and sporadically refer to a shell script without a magic number as a &quot;shell procedure&quot;.  </p>
<h3>Path Search</h3>
<p> When locating a command, the shell first looks to see if it has a shell function by that name. Then it looks for a builtin command by that name. If a builtin command is not found, one of two things happen: </p>
<ol>
<li> <p> Command names containing a slash are simply executed without performing any searches.  </li>
<li>  The shell searches each entry in <code>PATH</code> in turn for the command. The value of the <code>PATH</code> variable should be a series of entries separated by colons. Each entry consists of a directory name. The current directory may be indicated implicitly by an empty directory name, or explicitly by a single period.  </li>
</ol>
 </p>
<h3>Command Exit Status</h3>
<p> Each command has an exit status that can influence the behaviour of other shell commands. The paradigm is that a command exits with zero for normal or success, and non-zero for failure, error, or a false indication. The man page for each command should indicate the various exit codes and what they mean. Additionally, the builtin commands return exit codes, as does an executed shell function. </p>
<p> If a command consists entirely of variable assignments then the exit status of the command is that of the last command substitution if any, otherwise 0.  </p>
<h3>Complex Commands</h3>
<p> Complex commands are combinations of simple commands with control operators or reserved words, together creating a larger complex command. More generally, a command is one of the following: </p>
<ul>
<li> <p> simple command  </li>
<li>  pipeline  </li>
<li>  list or compound-list  </li>
<li>  compound command  </li>
<li>  function definition  </li>
</ul>
 </p>
<p> Unless otherwise stated, the exit status of a command is that of the last simple command executed by the command.  </p>
<h3>Pipelines</h3>
<p> A pipeline is a sequence of one or more commands separated by the control operator |. The standard output of all but the last command is connected to the standard input of the next command. The standard output of the last command is inherited from the shell, as usual. </p>
<p> The format for a pipeline is: </p>
<blockquote><p> <code>[!] command1 [ | command2 ...]</code> </p>
</blockquote>
<p> The standard output of command1 is connected to the standard input of command2. The standard input, standard output, or both of a command is considered to be assigned by the pipeline before any redirection specified by redirection operators that are part of the command. </p>
<p> If the pipeline is not in the background (discussed later), the shell waits for all commands to complete. </p>
<p> If the reserved word ! does not precede the pipeline, the exit status is the exit status of the last command specified in the pipeline. Otherwise, the exit status is the logical NOT of the exit status of the last command. That is, if the last command returns zero, the exit status is 1; if the last command returns greater than zero, the exit status is zero. </p>
<p> Because pipeline assignment of standard input or standard output or both takes place before redirection, it can be modified by redirection. For example: </p>
<blockquote><p> <code>$ command1 2&gt;&amp;1 | command2</code> </p>
</blockquote>
<p> sends both the standard output and standard error of command1 to the standard input of command2. </p>
<p> A ; or Aq newline terminator causes the preceding AND-OR-list (described next) to be executed sequentially; a &amp; causes asynchronous execution of the preceding AND-OR-list. </p>
<p> Note that unlike some other shells, each process in the pipeline is a child of the invoking shell (unless it is a shell builtin, in which case it executes in the current shell - but any effect it has on the environment is wiped).  </p>
<h3>Background Commands -</h3>
<p> If a command is terminated by the control operator ampersand (&amp;), the shell executes the command asynchronously - that is, the shell does not wait for the command to finish before executing the next command. </p>
<p> The format for running a command in background is: </p>
<blockquote><p> <code>command1 &amp; [command2 &amp; ...]</code> </p>
</blockquote>
<p> If the shell is not interactive, the standard input of an asynchronous command is set to /dev/null  </p>
<h3>Lists - Generally Speaking</h3>
<p> A list is a sequence of zero or more commands separated by newlines, semicolons, or ampersands, and optionally terminated by one of these three characters. The commands in a list are executed in the order they are written. If command is followed by an ampersand, the shell starts the command and immediately proceeds onto the next command; otherwise it waits for the command to terminate before proceeding to the next one.  </p>
<h3>Short-Circuit List Operators</h3>
<p> ``&amp;&amp;&#8216;&#8216; and ``||&#8216;&#8216; are AND-OR list operators. ``&amp;&amp;&#8216;&#8216; executes the first command, and then executes the second command if and only if the exit status of the first command is zero. ``||&#8216;&#8216; is similar, but executes the second command if and only if the exit status of the first command is nonzero. ``&amp;&amp;&#8216;&#8216; and ``||&#8216;&#8216; both have the same priority.  </p>
<h3>Flow-Control Constructs - if, while, for, case</h3>
<p> The syntax of the if command is </p>
<blockquote><pre><code>if list
then list
[ elif list
then list ] ...
[ else list ]
fi
</code></pre>
</blockquote>
<p> The syntax of the while command is </p>
<blockquote><pre><code>while list
do list
done
</code></pre>
</blockquote>
<p> The two lists are executed repeatedly while the exit status of the first list is zero. The until command is similar, but has the word until in place of while, which causes it to repeat until the exit status of the first list is zero. </p>
<p> The syntax of the for command is </p>
<blockquote><pre><code>for variable [ in [ word ... ] ]
do list
done
</code></pre>
</blockquote>
<p> The words following in are expanded, and then the list is executed repeatedly with the variable set to each word in turn. Omitting in word ... is equivalent to in &quot;$@&quot;. </p>
<p> The syntax of the break and continue command is </p>
<blockquote><pre><code>break [ num ]
continue [ num ]
</code></pre>
</blockquote>
<p> Break terminates the num innermost for or while loops. Continue continues with the next iteration of the innermost loop. These are implemented as builtin commands. </p>
<p> The syntax of the case command is </p>
<blockquote><pre><code>case word in
[(]pattern) list ;;
...
esac
</code></pre>
</blockquote>
<p> The pattern can actually be one or more patterns (see Sx Shell Patterns described later), separated by ``|&#8216;&#8216; characters. The Do ( Dc character before the pattern is optional.  </p>
<h3>Grouping Commands Together</h3>
<p> Commands may be grouped by writing either </p>
<blockquote><p> <code>(list)</code> </p>
</blockquote>
<p> or </p>
<blockquote><p> <code>{ list;</code> </p>
</blockquote>
<p> The first of these executes the commands in a subshell. Builtin commands grouped into a (list) will not affect the current shell. The second form does not fork another shell so is slightly more efficient. Grouping commands together this way allows you to redirect their output as though they were one program: </p>
<blockquote><pre><code>{ printf &quot; hello &quot; ; printf &quot; world\n&quot; ; } &gt; greeting
</code></pre>
</blockquote>
<p> Note that ``}&#8216;&#8216; must follow a control operator (here, ``;&#8216;&#8216; so that it is recognized as a reserved word and not as another command argument.  </p>
<h3>Functions</h3>
<p> The syntax of a function definition is </p>
<blockquote><p> <code>name ( ) command</code> </p>
</blockquote>
<p> A function definition is an executable statement; when executed it installs a function named name and returns an exit status of zero. The command is normally a list enclosed between ``{&#8216;&#8216; and ``}&#8216;&#8216; </p>
<p> Variables may be declared to be local to a function by using a local command. This should appear as the first statement of a function, and the syntax is </p>
<blockquote><p> <code>local [ variable | - ] ...</code> </p>
</blockquote>
<p> Local is implemented as a builtin command. </p>
<p> When a variable is made local, it inherits the initial value and exported and readonly flags from the variable with the same name in the surrounding scope, if there is one. Otherwise, the variable is initially unset. The shell uses dynamic scoping, so that if you make the variable x local to function f, which then calls function g, references to the variable x made inside g will refer to the variable x declared inside f, not to the global variable named x. </p>
<p> The only special parameter that can be made local is ``-&#8216;&#8216; Making ``-&#8216;&#8216; local any shell options that are changed via the set command inside the function to be restored to their original values when the function returns. </p>
<p> The syntax of the return command is </p>
<blockquote><p> <code>return [ exitstatus</code> </p>
</blockquote>
<p> It terminates the currently executing function. Return is implemented as a builtin command.  </p>
<h3>Variables and Parameters</h3>
<p> The shell maintains a set of parameters. A parameter denoted by a name is called a variable. When starting up, the shell turns all the environment variables into shell variables. New variables can be set using the form </p>
<blockquote><p> <code>name=value</code> </p>
</blockquote>
<p> Variables set by the user must have a name consisting solely of alphabetics, numerics, and underscores - the first of which must not be numeric. A parameter can also be denoted by a number or a special character as explained below.  </p>
<h3>Positional Parameters</h3>
<p> A positional parameter is a parameter denoted by a number (n &gt; 0). The shell sets these initially to the values of its command line arguments that follow the name of the shell script. The <code>set</code> builtin can also be used to set or reset them.  </p>
<h3>Special Parameters</h3>
<p> A special parameter is a parameter denoted by one of the following special characters. The value of the parameter is listed next to its character. </p>
<dl>
<dt><code>*</code></dt>
<dd> <p> Expands to the positional parameters, starting from one. When the expansion occurs within a double-quoted string it expands to a single field with the value of each parameter separated by the first character of the <code>IFS</code> variable, or by a Aq space if <code>IFS</code> is unset. </p>
 </dd>
<dt><code>@</code></dt>
<dd> <p> Expands to the positional parameters, starting from one. When the expansion occurs within double-quotes, each positional parameter expands as a separate argument. If there are no positional parameters, the expansion of @ generates zero arguments, even when @ is double-quoted. What this basically means, for example, is if $1 is ``abc&#8217;&#8216; and $2 is ``def ghi&#8217;&#8216; then Qq $@ expands to the two arguments: </p>
<blockquote><p> <code>&quot; abc &quot; &nbsp; &quot; def ghi &quot;</code> </p>
</blockquote>
 </dd>
<dt><code>#</code></dt>
<dd> <p> Expands to the number of positional parameters. </p>
 </dd>
<dt><code>?</code></dt>
<dd> <p> Expands to the exit status of the most recent pipeline. </p>
 </dd>
<dt><code>- (Hyphen.)</code></dt>
<dd> <p> Expands to the current option flags (the single-letter option names concatenated into a string) as specified on invocation, by the set builtin command, or implicitly by the shell. </p>
 </dd>
<dt><code>$</code></dt>
<dd> <p> Expands to the process ID of the invoked shell. A subshell retains the same value of $ as its parent. </p>
 </dd>
<dt><code>!</code></dt>
<dd> <p> Expands to the process ID of the most recent background command executed from the current shell. For a pipeline, the process ID is that of the last command in the pipeline. </p>
 </dd>
<dt><code>0 (Zero.)</code></dt>
<dd> <p> Expands to the name of the shell or shell script. </p>
 </dd></dl>
<h3>Word Expansions</h3>
<p> This clause describes the various expansions that are performed on words. Not all expansions are performed on every word, as explained later. </p>
<p> Tilde expansions, parameter expansions, command substitutions, arithmetic expansions, and quote removals that occur within a single word expand to a single field. It is only field splitting or pathname expansion that can create multiple fields from a single word. The single exception to this rule is the expansion of the special parameter @ within double-quotes, as was described above. </p>
<p> The order of word expansion is: </p>
<ol>
<li> <p> Tilde Expansion, Parameter Expansion, Command Substitution, Arithmetic Expansion (these all occur at the same time).  </li>
<li>  Field Splitting is performed on fields generated by step (1) unless the <code>IFS</code> variable is null.  </li>
<li>  Pathname Expansion (unless set -<code>f</code> is in effect).  </li>
<li>  Quote Removal.  </li>
</ol>
 </p>
<p> The $ character is used to introduce parameter expansion, command substitution, or arithmetic evaluation.  </p>
<h3>Tilde Expansion (substituting a user's home directory)</h3>
<p> A word beginning with an unquoted tilde character (~) is subjected to tilde expansion. All the characters up to a slash (/) or the end of the word are treated as a username and are replaced with the user&#8217;s home directory. If the username is missing (as in ~/foobar ) the tilde is replaced with the value of the <i>HOME</i> variable (the current user&#8217;s home directory).  </p>
<h3>Parameter Expansion</h3>
<p> The format for parameter expansion is as follows: </p>
<blockquote><p> <code>${expression}</code> </p>
</blockquote>
<p> where expression consists of all characters until the matching ``}&#8216;&#8216; Any ``}&#8216;&#8216; escaped by a backslash or within a quoted string, and characters in embedded arithmetic expansions, command substitutions, and variable expansions, are not examined in determining the matching ``}&#8216;&#8216; </p>
<p> The simplest form for parameter expansion is: </p>
<blockquote><p> <code>${parameter}</code> </p>
</blockquote>
<p> The value, if any, of parameter is substituted. </p>
<p> The parameter name or symbol can be enclosed in braces, which are optional except for positional parameters with more than one digit or when parameter is followed by a character that could be interpreted as part of the name. If a parameter expansion occurs inside double-quotes: </p>
<ol>
<li> <p> Pathname expansion is not performed on the results of the expansion.  </li>
<li>  Field splitting is not performed on the results of the expansion, with the exception of @.  </li>
</ol>
 </p>
<p> In addition, a parameter expansion can be modified by using one of the following formats. </p>
<dl>
<dt><code>${parameter:-word}</code></dt>
<dd> <p> Use Default Values. If parameter is unset or null, the expansion of word is substituted; otherwise, the value of parameter is substituted. </p>
 </dd>
<dt><code>${parameter:=word}</code></dt>
<dd> <p> Assign Default Values. If parameter is unset or null, the expansion of word is assigned to parameter. In all cases, the final value of parameter is substituted. Only variables, not positional parameters or special parameters, can be assigned in this way. </p>
 </dd>
<dt><code>${parameter:?[word]}</code></dt>
<dd> <p> Indicate Error if Null or Unset. If parameter is unset or null, the expansion of word (or a message indicating it is unset if word is omitted) is written to standard error and the shell exits with a nonzero exit status. Otherwise, the value of parameter is substituted. An interactive shell need not exit. </p>
 </dd>
<dt><code>${parameter:+word}</code></dt>
<dd> <p> Use Alternative Value. If parameter is unset or null, null is substituted; otherwise, the expansion of word is substituted. </p>
 </dd></dl>
<p> In the parameter expansions shown previously, use of the colon in the format results in a test for a parameter that is unset or null; omission of the colon results in a test for a parameter that is only unset. </p>
<dl>
<dt><code>${#parameter}</code></dt>
<dd> <p> String Length. The length in characters of the value of parameter. </p>
 </dd></dl>
<p> The following four varieties of parameter expansion provide for substring processing. In each case, pattern matching notation (see Sx Shell Patterns ) , rather than regular expression notation, is used to evaluate the patterns. If parameter is * or @, the result of the expansion is unspecified. Enclosing the full parameter expansion string in double-quotes does not cause the following four varieties of pattern characters to be quoted, whereas quoting characters within the braces has this effect. </p>
<dl>
<dt><code>${parameter%word}</code></dt>
<dd> <p> Remove Smallest Suffix Pattern. The word is expanded to produce a pattern. The parameter expansion then results in parameter, with the smallest portion of the suffix matched by the pattern deleted. </p>
 </dd>
<dt><code>${parameter%%word}</code></dt>
<dd> <p> Remove Largest Suffix Pattern. The word is expanded to produce a pattern. The parameter expansion then results in parameter, with the largest portion of the suffix matched by the pattern deleted. </p>
 </dd>
<dt><code>${parameter#word}</code></dt>
<dd> <p> Remove Smallest Prefix Pattern. The word is expanded to produce a pattern. The parameter expansion then results in parameter, with the smallest portion of the prefix matched by the pattern deleted. </p>
 </dd>
<dt><code>${parameter##word}</code></dt>
<dd> <p> Remove Largest Prefix Pattern. The word is expanded to produce a pattern. The parameter expansion then results in parameter, with the largest portion of the prefix matched by the pattern deleted. </p>
 </dd></dl>
<h3>Command Substitution</h3>
<p> Command substitution allows the output of a command to be substituted in place of the command name itself. Command substitution occurs when the command is enclosed as follows: </p>
<blockquote><p> <code>$(command)</code> </p>
</blockquote>
<p> or Po ``backquoted&#8217;&#8216; version Pc : </p>
<blockquote><p> <code>`command`</code> </p>
</blockquote>
<p> The shell expands the command substitution by executing command in a subshell environment and replacing the command substitution with the standard output of the command, removing sequences of one or more Ao newline Ac Ns s at the end of the substitution. (Embedded Ao newline Ac Ns s before the end of the output are not removed; however, during field splitting, they may be translated into Ao space Ac Ns s , depending on the value of <code>IFS</code> and quoting that is in effect.)  </p>
<h3>Arithmetic Expansion</h3>
<p> Arithmetic expansion provides a mechanism for evaluating an arithmetic expression and substituting its value. The format for arithmetic expansion is as follows: </p>
<blockquote><p> <code>$((expression))</code> </p>
</blockquote>
<p> The expression is treated as if it were in double-quotes, except that a double-quote inside the expression is not treated specially. The shell expands all tokens in the expression for parameter expansion, command substitution, and quote removal. </p>
<p> Next, the shell treats this as an arithmetic expression and substitutes the value of the expression.  </p>
<h3>White Space Splitting (Field Splitting)</h3>
<p> After parameter expansion, command substitution, and arithmetic expansion the shell scans the results of expansions and substitutions that did not occur in double-quotes for field splitting and multiple fields can result. </p>
<p> The shell treats each character of the <code>IFS</code> as a delimiter and uses the delimiters to split the results of parameter expansion and command substitution into fields.  </p>
<h3>Pathname Expansion (File Name Generation)</h3>
<p> Unless the -<code>f</code> flag is set, file name generation is performed after word splitting is complete. Each word is viewed as a series of patterns, separated by slashes. The process of expansion replaces the word with the names of all existing files whose names can be formed by replacing each pattern with a string that matches the specified pattern. There are two restrictions on this: first, a pattern cannot match a string containing a slash, and second, a pattern cannot match a string starting with a period unless the first character of the pattern is a period. The next section describes the patterns used for both Pathname Expansion and the <code>case</code> command.  </p>
<h3>Shell Patterns</h3>
<p> A pattern consists of normal characters, which match themselves, and meta-characters. The meta-characters are ``!&#8216;&#8216; ``*&#8216;&#8216; ``?&#8216;&#8216; and ``[&#8216;&#8216; These characters lose their special meanings if they are quoted. When command or variable substitution is performed and the dollar sign or back quotes are not double quoted, the value of the variable or the output of the command is scanned for these characters and they are turned into meta-characters. </p>
<p> An asterisk (``*&#8216;&#8216; ) matches any string of characters. A question mark matches any single character. A left bracket (``[&#8216;&#8216; ) introduces a character class. The end of the character class is indicated by a (``]&#8216;&#8216; ) if the ``]&#8216;&#8216; is missing then the ``[&#8216;&#8216; matches a ``[&#8216;&#8216; rather than introducing a character class. A character class matches any of the characters between the square brackets. A range of characters may be specified using a minus sign. The character class may be complemented by making an exclamation point the first character of the character class. </p>
<p> To include a ``]&#8216;&#8216; in a character class, make it the first character listed (after the ``!&#8216;&#8216; if any). To include a minus sign, make it the first or last character listed.  </p>
<h3>Builtins</h3>
<p> This section lists the builtin commands which are builtin because they need to perform some operation that can&#8217;t be performed by a separate process. In addition to these, there are several other commands that may be builtin for efficiency (e.g. <a href="/docs/linux/man/1-printf/">printf</a>(1), <a href="/docs/linux/man/1-echo/">echo</a>(1), <a href="/docs/linux/man/1-test/">test</a>(1), etc). </p>
<dl>
<dt><code>:</code></dt>
<dd>  </dd>
<dt><code>true</code></dt>
<dd> <p> A null command that returns a 0 (true) exit value. </p>
 </dd>
<dt><code>. file</code></dt>
<dd> <p> The commands in the specified file are read and executed by the shell. </p>
 </dd>
<dt><code>alias </code>[<i>name </i>[<i>=string ...</i> ] ] </dt>
<dd> <p> If <i>name=string</i> is specified, the shell defines the alias <i>name</i> with value <i>string</i> If just <i>name</i> is specified, the value of the alias <i>name</i> is printed. With no arguments, the <code>alias</code> builtin prints the names and values of all defined aliases (see <code>unalias )</code> </p>
 </dd>
<dt><code>bg [ </code><i>job ] ...</i></dt>
<dd> <p> Continue the specified jobs (or the current job if no jobs are given) in the background. </p>
 </dd>
<dt><code> command</code> [-<code>p</code> ] [-<code>v</code> ] [-<code>V</code> ] <i>command</i> [<i>arg ...</i> ] </dt>
<dd>  </dd>
<dd> <p> Execute the specified command but ignore shell functions when searching for it. (This is useful when you have a shell function with the same name as a builtin command.) </p>
 </dd>
<dl>
<dt><code>-p</code></dt>
<dd> <p> search for command using a <code>PATH</code> that guarantees to find all the standard utilities. </p>
 </dd>
<dt><code>-V</code></dt>
<dd> <p> Do not execute the command but search for the command and print the resolution of the command search. This is the same as the type builtin. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Do not execute the command but search for the command and print the absolute pathname of utilities, the name for builtins or the expansion of aliases. </p>
 </dd></dl>
<dt><code>cd </code><i>file ...</i></dt>
<dd>  </dd>
<dt><code> cd </code>[-<code>LP</code> ] [<i>directory</i> ] </dt>
<dd>  </dd>
<dd> <p> Switch to the specified directory (default <code>HOME )</code> If an entry for <code>CDPATH</code> appears in the environment of the <code>cd</code> command or the shell variable <code>CDPATH</code> is set and the directory name does not begin with a slash, then the directories listed in <code>CDPATH</code> will be searched for the specified directory. The format of <code>CDPATH</code> is the same as that of <code>PATH</code> If a single dash is specified as the argument, it will be replaced by the value of <code>OLDPWD</code> The <code>cd</code> command will print out the name of the directory that it actually switched to if this is different from the name that the user gave. These may be different either because the <code>CDPATH</code> mechanism was used or because the argument is a single dash. The -<code>P</code> option causes the physical directory structure to be used, that is, all symbolic links are resolved to their respective values. The -<code>L</code> option turns off the effect of any preceding -<code>P</code> options. </p>
 </dd>
<dt><code> echo </code>[-<code>n</code> ] <i>args...</i></dt>
<dd>  </dd>
<dd> <p> Print the arguments on the standard output, separated by spaces. Unless the -<code>n</code> option is present, a newline is output following the arguments. </p>
<p> If any of the following sequences of characters is encountered during output, the sequence is not output. Instead, the specified action is performed: </p>
 </dd>
<dl>
<dt><code>\b</code></dt>
<dd> <p> A backspace character is output. </p>
 </dd>
<dt><code>\c</code></dt>
<dd> <p> Subsequent output is suppressed. This is normally used at the end of the last argument to suppress the trailing newline that <code>echo</code> would otherwise output. </p>
 </dd>
<dt><code>\e</code></dt>
<dd> <p> Outputs an escape character (ESC). </p>
 </dd>
<dt><code>\f</code></dt>
<dd> <p> Output a form feed. </p>
 </dd>
<dt><code>\n</code></dt>
<dd> <p> Output a newline character. </p>
 </dd>
<dt><code>\r</code></dt>
<dd> <p> Output a carriage return. </p>
 </dd>
<dt><code>\t</code></dt>
<dd> <p> Output a (horizontal) tab character. </p>
 </dd>
<dt><code>\v</code></dt>
<dd> <p> Output a vertical tab. </p>
 </dd>
<dt><code>\0 </code><i>digits</i></dt>
<dd> <p> Output the character whose value is given by zero to three octal digits. If there are zero digits, a nul character is output. </p>
 </dd>
<dt><code>\\</code></dt>
<dd> <p> Output a backslash. </p>
 </dd></dl>
<p> All other backslash sequences elicit undefined behaviour. </p>
<dt><code>eval </code><i>string ...</i></dt>
<dd> <p> Concatenate all the arguments with spaces. Then re-parse and execute the command. </p>
 </dd>
<dt><code>exec </code>[<i>command arg ...</i> ] </dt>
<dd> <p> Unless command is omitted, the shell process is replaced with the specified program (which must be a real program, not a shell builtin or function). Any redirections on the <code>exec</code> command are marked as permanent, so that they are not undone when the <code>exec</code> command finishes. </p>
 </dd>
<dt><code>exit </code>[<i>exitstatus</i> ] </dt>
<dd> <p> Terminate the shell process. If <i>exitstatus</i> is given it is used as the exit status of the shell; otherwise the exit status of the preceding command is used. </p>
 </dd>
<dt><code>export </code><i>name ...</i></dt>
<dd>  </dd>
<dt><code>export -p</code></dt>
<dd> <p> The specified names are exported so that they will appear in the environment of subsequent commands. The only way to un-export a variable is to unset it. The shell allows the value of a variable to be set at the same time it is exported by writing </p>
<blockquote><p> <code>export name=value</code> </p>
</blockquote>
<p> With no arguments the export command lists the names of all exported variables. With the -<code>p</code> option specified the output will be formatted suitably for non-interactive use. </p>
 </dd>
<dt><code> fc </code>[-<code>e </code><i>editor</i> ] [<i>first </i>[<i>last</i> ] ] </dt>
<dd>  </dd>
<dt><code> fc -l</code> [-<code>nr</code> ] [<i>first </i>[<i>last</i> ] ] </dt>
<dd>  </dd>
<dt><code> fc -s </code>[<i>old=new</i> ] [<i>first</i> ] </dt>
<dd>  </dd>
<dd> <p> The <code>fc</code> builtin lists, or edits and re-executes, commands previously entered to an interactive shell. </p>
 </dd>
<dl>
<dt><code>-e editor</code></dt>
<dd> <p> Use the editor named by editor to edit the commands. The editor string is a command name, subject to search via the <code>PATH</code> variable. The value in the <code>FCEDIT</code> variable is used as a default when -<code>e</code> is not specified. If <code>FCEDIT</code> is null or unset, the value of the <code>EDITOR</code> variable is used. If <code>EDITOR</code> is null or unset, <a href="/docs/linux/man/1-ed/">ed</a>(1) is used as the editor. </p>
 </dd>
<dt><code>-l (ell)</code></dt>
<dd> <p> List the commands rather than invoking an editor on them. The commands are written in the sequence indicated by the first and last operands, as affected by -<code>r</code> with each command preceded by the command number. </p>
 </dd>
<dt><code>-n</code></dt>
<dd> <p> Suppress command numbers when listing with -l. </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> Reverse the order of the commands listed (with -<code>l</code> or edited (with neither -<code>l</code> nor -<code>s )</code> </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> Re-execute the command without invoking an editor. </p>
 </dd>
<dt><code>first</code></dt>
<dd>  </dd>
<dt><code>last</code></dt>
<dd> <p> Select the commands to list or edit. The number of previous commands that can be accessed are determined by the value of the <code>HISTSIZE</code> variable. The value of first or last or both are one of the following: </p>
 </dd>
<dl>
<dt><code>[+]number</code></dt>
<dd> <p> A positive number representing a command number; command numbers can be displayed with the -<code>l</code> option. </p>
 </dd>
<dt><code>-number</code></dt>
<dd> <p> A negative decimal number representing the command that was executed number of commands previously. For example, -1 is the immediately previous command. </p>
 </dd></dl>
<dt><code>string</code></dt>
<dd> <p> A string indicating the most recently entered command that begins with that string. If the old=new operand is not also specified with -<code>s</code> the string form of the first operand cannot contain an embedded equal sign. </p>
 </dd></dl>
<p> The following environment variables affect the execution of fc: </p>
<dl>
<dt><code>FCEDIT</code></dt>
<dd> <p> Name of the editor to use. </p>
 </dd>
<dt><code>HISTSIZE</code></dt>
<dd> <p> The number of previous commands that are accessible. </p>
 </dd></dl>
<dt><code>fg </code>[<i>job</i> ] </dt>
<dd> <p> Move the specified job or the current job to the foreground. </p>
 </dd>
<dt><code>getopts </code><i>optstring var</i></dt>
<dd> <p> The <code>POSIX</code> <code>getopts</code> command, not to be confused with the <i>Bell Labs</i> -derived <a href="/docs/linux/man/1-getopt/">getopt</a>(1). </p>
<p> The first argument should be a series of letters, each of which may be optionally followed by a colon to indicate that the option requires an argument. The variable specified is set to the parsed option. </p>
<p> The <code>getopts</code> command deprecates the older <a href="/docs/linux/man/1-getopt/">getopt</a>(1) utility due to its handling of arguments containing whitespace. </p>
<p> The <code>getopts</code> builtin may be used to obtain options and their arguments from a list of parameters. When invoked, <code>getopts</code> places the value of the next option from the option string in the list in the shell variable specified by <i>var</i> and its index in the shell variable <code>OPTIND</code> When the shell is invoked, <code>OPTIND</code> is initialized to 1. For each option that requires an argument, the <code>getopts</code> builtin will place it in the shell variable <code>OPTARG</code> If an option is not allowed for in the <i>optstring</i> then <code>OPTARG</code> will be unset. </p>
<p> <i>optstring</i> is a string of recognized option letters (see <a href="/docs/linux/man/3-getopt/">getopt</a>(3)). If a letter is followed by a colon, the option is expected to have an argument which may or may not be separated from it by white space. If an option character is not found where expected, <code>getopts</code> will set the variable <i>var</i> to a ``?&#8216;&#8216; <code>getopts</code> will then unset <code>OPTARG</code> and write output to standard error. By specifying a colon as the first character of <i>optstring</i> all errors will be ignored. </p>
<p> After the last option <code>getopts</code> will return a non-zero value and set <i>var</i> to ``?&#8216;&#8216; </p>
<p> The following code fragment shows how one might process the arguments for a command that can take the options [a] and [b] and the option [c] which requires an argument. </p>
<blockquote><pre><code>while getopts abc: f
do
        case $f in
        a | b) flag=$f;;
        c) carg=$OPTARG;;
        \?) echo $USAGE; exit 1;;
        esac
done
shift `expr $OPTIND - 1`
</code></pre>
</blockquote>
<p> This code will accept any of the following as equivalent: </p>
<blockquote><pre><code>cmd -acarg file file
cmd -a -c arg file file
cmd -carg -a file file
cmd -a -carg -- file file
</code></pre>
</blockquote>
 </dd>
<dt><code>hash -rv </code><i>command ...</i></dt>
<dd> <p> The shell maintains a hash table which remembers the locations of commands. With no arguments whatsoever, the <code>hash</code> command prints out the contents of this table. Entries which have not been looked at since the last <code>cd</code> command are marked with an asterisk; it is possible for these entries to be invalid. </p>
<p> With arguments, the <code>hash</code> command removes the specified commands from the hash table (unless they are functions) and then locates them. With the -<code>v</code> option, hash prints the locations of the commands as it finds them. The -<code>r</code> option causes the hash command to delete all the entries in the hash table except for functions. </p>
 </dd>
<dt><code>pwd </code>[-<code>LP</code> ] </dt>
<dd> <p> builtin command remembers what the current directory is rather than recomputing it each time. This makes it faster. However, if the current directory is renamed, the builtin version of <code>pwd</code> will continue to print the old name for the directory. The -<code>P</code> option causes the physical value of the current working directory to be shown, that is, all symbolic links are resolved to their respective values. The -<code>L</code> option turns off the effect of any preceding -<code>P</code> options. </p>
 </dd>
<dt><code> read </code>[-<code>p </code><i>prompt</i> ] [-<code>r</code> ] <i>variable</i> [<i>...</i> ] </dt>
<dd>  </dd>
<dd> <p> The prompt is printed if the -<code>p</code> option is specified and the standard input is a terminal. Then a line is read from the standard input. The trailing newline is deleted from the line and the line is split as described in the section on word splitting above, and the pieces are assigned to the variables in order. At least one variable must be specified. If there are more pieces than variables, the remaining pieces (along with the characters in <code>IFS</code> that separated them) are assigned to the last variable. If there are more variables than pieces, the remaining variables are assigned the null string. The <code>read</code> builtin will indicate success unless EOF is encountered on input, in which case failure is returned. </p>
<p> By default, unless the -<code>r</code> option is specified, the backslash ``\&#8216;&#8216; acts as an escape character, causing the following character to be treated literally. If a backslash is followed by a newline, the backslash and the newline will be deleted. </p>
 </dd>
<dt><code>readonly </code><i>name ...</i></dt>
<dd>  </dd>
<dt><code>readonly -p</code></dt>
<dd> <p> The specified names are marked as read only, so that they cannot be subsequently modified or unset. The shell allows the value of a variable to be set at the same time it is marked read only by writing </p>
<blockquote><p> <code>readonly name=value</code> </p>
</blockquote>
<p> With no arguments the readonly command lists the names of all read only variables. With the -<code>p</code> option specified the output will be formatted suitably for non-interactive use. </p>
 </dd>
<dt><code> printf </code><i>format</i> [<i>arguments ...</i> ] </dt>
<dd> <p> <code>printf</code> </p>
 </dd>
<dd> <p> formats and prints its arguments, after the first, under control of the <i>format </i> The <i>format</i> is a character string which contains three types of objects: plain characters, which are simply copied to standard output, character escape sequences which are converted and copied to the standard output, and format specifications, each of which causes printing of the next successive <i>argument </i> </p>
<p> The <i>arguments</i> after the first are treated as strings if the corresponding format is either <code>b</code> <code>c</code> or <code>s</code> otherwise it is evaluated as a C constant, with the following extensions: </p>
 </dd>
<ul>
<li> <p> A leading plus or minus sign is allowed.  </li>
<li>  If the leading character is a single or double quote, the value is the <code>ASCII</code> code of the next character.  </li>
</ul>
 </p>
<p> The format string is reused as often as necessary to satisfy the <i>arguments </i> Any extra format specifications are evaluated with zero or the null string. </p>
<p> Character escape sequences are in backslash notation as defined in St -ansiC . The characters and their meanings are as follows: </p>
<dl>
<dt><code>\a</code></dt>
<dd> <p> Write a &lt;bell&gt; character. </p>
 </dd>
<dt><code>\b</code></dt>
<dd> <p> Write a &lt;backspace&gt; character. </p>
 </dd>
<dt><code>\e</code></dt>
<dd> <p> Write an &lt;escape&gt; (ESC) character. </p>
 </dd>
<dt><code>\f</code></dt>
<dd> <p> Write a &lt;form-feed&gt; character. </p>
 </dd>
<dt><code>\n</code></dt>
<dd> <p> Write a &lt;new-line&gt; character. </p>
 </dd>
<dt><code>\r</code></dt>
<dd> <p> Write a &lt;carriage return&gt; character. </p>
 </dd>
<dt><code>\t</code></dt>
<dd> <p> Write a &lt;tab&gt; character. </p>
 </dd>
<dt><code>\v</code></dt>
<dd> <p> Write a &lt;vertical tab&gt; character. </p>
 </dd>
<dt><code>\\</code></dt>
<dd> <p> Write a backslash character. </p>
 </dd>
<dt><code>\ </code><i>num</i></dt>
<dd> <p> Write an 8-bit character whose <code>ASCII</code> value is the 1-, 2-, or 3-digit octal number <i>num</i> </p>
 </dd></dl>
<p> Each format specification is introduced by the percent character (``%&#8216;&#8216;). The remainder of the format specification includes, in the following order: </p>
<dl>
<dt><code>&quot;Zero or more of the following flags:&quot;</code></dt>
<dd>  </dd>
<dl>
<dt><code>#</code></dt>
<dd> <p> A `#&#8216; character specifying that the value should be printed in an ``alternative form&#8217;&#8216;. For <code>b</code> <code>c</code> <code>d</code> and <code>s</code> formats, this option has no effect. For the <code>o</code> format the precision of the number is increased to force the first character of the output string to a zero. For the <code>x</code> (<code>X</code> ) format, a non-zero result has the string <code>0x</code> (<code>0X</code> ) prepended to it. For <code>e </code> <code>E</code> <code>f </code> <code>g</code> and <code>G</code> formats, the result will always contain a decimal point, even if no digits follow the point (normally, a decimal point only appears in the results of those formats if a digit follows the decimal point). For <code>g</code> and <code>G</code> formats, trailing zeros are not removed from the result as they would otherwise be. </p>
 </dd>
<dt><code>-</code></dt>
<dd> <p> A minus sign `-&#8216; which specifies <i>left adjustment</i> of the output in the indicated field; </p>
 </dd>
<dt><code>+</code></dt>
<dd> <p> A `+&#8216; character specifying that there should always be a sign placed before the number when using signed formats. </p>
 </dd>
<dt><code>`&nbsp;&#8216; </code></dt>
<dd> <p> A space specifying that a blank should be left before a positive number for a signed format. A `+&#8216; overrides a space if both are used; </p>
 </dd>
<dt><code>0</code></dt>
<dd> <p> A zero `0&#8217; character indicating that zero-padding should be used rather than blank-padding. A `-&#8216; overrides a `0&#8217; if both are used; </p>
 </dd></dl>
<dt><code>&quot;Field Width:&quot;</code></dt>
<dd> <p> An optional digit string specifying a <i>field width</i> if the output string has fewer characters than the field width it will be blank-padded on the left (or right, if the left-adjustment indicator has been given) to make up the field width (note that a leading zero is a flag, but an embedded zero is part of a field width); </p>
 </dd>
<dt><code>Precision</code></dt>
<dd> <p> An optional period, `<code>.</code> &#8216; followed by an optional digit string giving a <i>precision</i> which specifies the number of digits to appear after the decimal point, for <code>e</code> and <code>f</code> formats, or the maximum number of bytes to be printed from a string ( <code>b</code> and <code>s</code> formats); if the digit string is missing, the precision is treated as zero; </p>
 </dd>
<dt><code>Format</code></dt>
<dd> <p> A character which indicates the type of format to use (one of <code>diouxXfwEgGbcs )</code> </p>
 </dd></dl>
<p> A field width or precision may be `<code>*</code> &#8216; instead of a digit string. In this case an <i>argument</i> supplies the field width or precision. </p>
<p> The format characters and their meanings are: </p>
<dl>
<dt><code>diouXx </code>The </dt>
<dd> <p> <i>argument</i> is printed as a signed decimal (d or i), unsigned octal, unsigned decimal, or unsigned hexadecimal (X or x), respectively. </p>
 </dd>
<dt><code>f</code></dt>
<dd> <p> The <i>argument</i> is printed in the style [-]ddd <code>. ddd</code> where the number of d&#8217;s after the decimal point is equal to the precision specification for the argument. If the precision is missing, 6 digits are given; if the precision is explicitly 0, no digits and no decimal point are printed. </p>
 </dd>
<dt><code>eE</code></dt>
<dd> <p> The <i>argument</i> is printed in the style [-]d <code>. ddd e &plusmn;dd</code> where there is one digit before the decimal point and the number after is equal to the precision specification for the argument; when the precision is missing, 6 digits are produced. An upper-case E is used for an `E&#8217; format. </p>
 </dd>
<dt><code>gG</code></dt>
<dd> <p> The <i>argument</i> is printed in style <code>f</code> or in style <code>e</code> (<code>E</code> ) whichever gives full precision in minimum space. </p>
 </dd>
<dt><code>b</code></dt>
<dd> <p> Characters from the string <i>argument</i> are printed with backslash-escape sequences expanded. <br />
 The following additional backslash-escape sequences are supported: </p>
 </dd>
<dl>
<dt><code>\c</code></dt>
<dd> <p> Causes <code>dash</code> to ignore any remaining characters in the string operand containing it, any remaining string operands, and any additional characters in the format operand. </p>
 </dd>
<dt><code>\0 </code><i>num</i></dt>
<dd> <p> Write an 8-bit character whose <code>ASCII</code> value is the 1-, 2-, or 3-digit octal number <i>num</i> </p>
 </dd></dl>
<dt><code>c</code></dt>
<dd> <p> The first character of <i>argument</i> is printed. </p>
 </dd>
<dt><code>s</code></dt>
<dd> <p> Characters from the string <i>argument</i> are printed until the end is reached or until the number of bytes indicated by the precision specification is reached; if the precision is omitted, all characters in the string are printed. </p>
 </dd>
<dt><code>%</code></dt>
<dd> <p> Print a `%&#8216;; no argument is used. </p>
 </dd></dl>
<p> In no case does a non-existent or small field width cause truncation of a field; padding takes place only if the specified field width exceeds the actual width. </p>
<dt><code> set</code> [{ -<code>options | +options | --</code><i>arg ...</i> ] </dt>
<dd>  </dd>
<dd> <p> The <code>set</code> command performs three different functions. </p>
<p> With no arguments, it lists the values of all shell variables. </p>
<p> If options are given, it sets the specified option flags, or clears them as described in the section called Sx Argument List Processing . As a special case, if the option is -o or +o and no argument is supplied, the shell prints the settings of all its options. If the option is -o, the settings are printed in a human-readable format; if the option is +o, the settings are printed in a format suitable for reinput to the shell to affect the same option settings. </p>
<p> The third use of the set command is to set the values of the shell&#8217;s positional parameters to the specified args. To change the positional parameters without changing any options, use ``--&#8216;&#8216; as the first argument to set. If no args are present, the set command will clear all the positional parameters (equivalent to executing ``shift $# .&#8216;&#8216; </p>
 </dd>
<dt><code>shift </code>[<i>n</i> ] </dt>
<dd> <p> Shift the positional parameters n times. A <code>shift</code> sets the value of <i>$1</i> to the value of <i>$2</i> the value of <i>$2</i> to the value of <i>$3</i> and so on, decreasing the value of <i>$#</i> by one. If n is greater than the number of positional parameters, <code>shift</code> will issue an error message, and exit with return status 2. </p>
 </dd>
<dt><code>test </code><i>expression</i></dt>
<dd>  </dd>
<dt><code>[ </code><i>expression </i><code>]</code></dt>
<dd> <p> The <code>test</code> utility evaluates the expression and, if it evaluates to true, returns a zero (true) exit status; otherwise it returns 1 (false). If there is no expression, test also returns 1 (false). </p>
<p> All operators and flags are separate arguments to the <code>test</code> utility. </p>
<p> The following primaries are used to construct expression: </p>
 </dd>
<dl>
<dt><code>-b </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and is a block special file. </p>
 </dd>
<dt><code>-c </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and is a character special file. </p>
 </dd>
<dt><code>-d </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and is a directory. </p>
 </dd>
<dt><code>-e </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists (regardless of type). </p>
 </dd>
<dt><code>-f </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and is a regular file. </p>
 </dd>
<dt><code>-g </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and its set group ID flag is set. </p>
 </dd>
<dt><code>-h </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and is a symbolic link. </p>
 </dd>
<dt><code>-k </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and its sticky bit is set. </p>
 </dd>
<dt><code>-n </code><i>string</i></dt>
<dd> <p> True if the length of <i>string</i> is nonzero. </p>
 </dd>
<dt><code>-p </code><i>file</i></dt>
<dd> <p> True if <i>file</i> is a named pipe Po Tn FIFO Pc . </p>
 </dd>
<dt><code>-r </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and is readable. </p>
 </dd>
<dt><code>-s </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and has a size greater than zero. </p>
 </dd>
<dt><code>-t </code><i>file_descriptor</i></dt>
<dd> <p> True if the file whose file descriptor number is <i>file_descriptor</i> is open and is associated with a terminal. </p>
 </dd>
<dt><code>-u </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and its set user ID flag is set. </p>
 </dd>
<dt><code>-w </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and is writable. True indicates only that the write flag is on. The file is not writable on a read-only file system even if this test indicates true. </p>
 </dd>
<dt><code>-x </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and is executable. True indicates only that the execute flag is on. If <i>file</i> is a directory, true indicates that <i>file</i> can be searched. </p>
 </dd>
<dt><code>-z </code><i>string</i></dt>
<dd> <p> True if the length of <i>string</i> is zero. </p>
 </dd>
<dt><code>-L </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and is a symbolic link. This operator is retained for compatibility with previous versions of this program. Do not rely on its existence; use -<code>h</code> instead. </p>
 </dd>
<dt><code>-O </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and its owner matches the effective user id of this process. </p>
 </dd>
<dt><code>-G </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and its group matches the effective group id of this process. </p>
 </dd>
<dt><code>-S </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and is a socket. </p>
 </dd>
<dt><i>file1 -</i><code>nt </code><i>file2</i></dt>
<dd> <p> True if <i>file1</i> and <i>file2</i> exist and <i>file1</i> is newer than <i>file2</i> </p>
 </dd>
<dt><i>file1 -</i><code>ot </code><i>file2</i></dt>
<dd> <p> True if <i>file1</i> and <i>file2</i> exist and <i>file1</i> is older than <i>file2</i> </p>
 </dd>
<dt><i>file1 -</i><code>ef </code><i>file2</i></dt>
<dd> <p> True if <i>file1</i> and <i>file2</i> exist and refer to the same file. </p>
 </dd>
<dt><i>string</i></dt>
<dd> <p> True if <i>string</i> is not the null string. </p>
 </dd>
<dt><i>s1 </i><code>= </code><i>s2</i></dt>
<dd> <p> True if the strings <i>s1</i> and <i>s2</i> are identical. </p>
 </dd>
<dt><i>s1 </i><code>!= </code><i>s2</i></dt>
<dd> <p> True if the strings <i>s1</i> and <i>s2</i> are not identical. </p>
 </dd>
<dt><i>s1 </i><code>&lt; </code><i>s2</i></dt>
<dd> <p> True if string <i>s1</i> comes before <i>s2</i> based on the ASCII value of their characters. </p>
 </dd>
<dt><i>s1 </i><code>&gt; </code><i>s2</i></dt>
<dd> <p> True if string <i>s1</i> comes after <i>s2</i> based on the ASCII value of their characters. </p>
 </dd>
<dt><i>n1 -</i><code>eq </code><i>n2</i></dt>
<dd> <p> True if the integers <i>n1</i> and <i>n2</i> are algebraically equal. </p>
 </dd>
<dt><i>n1 -</i><code>ne </code><i>n2</i></dt>
<dd> <p> True if the integers <i>n1</i> and <i>n2</i> are not algebraically equal. </p>
 </dd>
<dt><i>n1 -</i><code>gt </code><i>n2</i></dt>
<dd> <p> True if the integer <i>n1</i> is algebraically greater than the integer <i>n2</i> </p>
 </dd>
<dt><i>n1 -</i><code>ge </code><i>n2</i></dt>
<dd> <p> True if the integer <i>n1</i> is algebraically greater than or equal to the integer <i>n2</i> </p>
 </dd>
<dt><i>n1 -</i><code>lt </code><i>n2</i></dt>
<dd> <p> True if the integer <i>n1</i> is algebraically less than the integer <i>n2</i> </p>
 </dd>
<dt><i>n1 -</i><code>le </code><i>n2</i></dt>
<dd> <p> True if the integer <i>n1</i> is algebraically less than or equal to the integer <i>n2</i> </p>
 </dd></dl>
<p> These primaries can be combined with the following operators: </p>
<dl>
<dt><code>! </code><i>expression</i></dt>
<dd> <p> True if <i>expression</i> is false. </p>
 </dd>
<dt><i>expression1 -</i><code>a </code><i>expression2</i></dt>
<dd> <p> True if both <i>expression1</i> and <i>expression2</i> are true. </p>
 </dd>
<dt><i>expression1 -</i><code>o </code><i>expression2</i></dt>
<dd> <p> True if either <i>expression1</i> or <i>expression2</i> are true. </p>
 </dd>
<dt><code>( </code><i>expression </i><code>)</code></dt>
<dd> <p> True if expression is true. </p>
 </dd></dl>
<p> The -<code>a</code> operator has higher precedence than the -<code>o</code> operator. </p>
<dt><code>times</code></dt>
<dd> <p> Print the accumulated user and system times for the shell and for processes run from the shell. The return status is 0. </p>
 </dd>
<dt><code> trap</code> [<i>action signal ...</i> ] </dt>
<dd>  </dd>
<dd> <p> Cause the shell to parse and execute action when any of the specified signals are received. The signals are specified by signal number or as the name of the signal. If <i>signal</i> is <code>0</code> or <code>EXIT</code> the action is executed when the shell exits. <i>action</i> may be empty <code>( &#8216;&#8216; )</code> which causes the specified signals to be ignored. With <i>action</i> omitted or set to `-&#8216; the specified signals are set to their default action. When the shell forks off a subshell, it resets trapped (but not ignored) signals to the default action. The <code>trap</code> command has no effect on signals that were ignored on entry to the shell. <code>trap</code> without any arguments cause it to write a list of signals and their associated action to the standard output in a format that is suitable as an input to the shell that achieves the same trapping results. </p>
<p> Examples: </p>
<blockquote><p> <code>trap</code> </p>
</blockquote>
<p> List trapped signals and their corresponding action </p>
<blockquote><p> <code>trap &#8216;&#8216; INT QUIT tstp 30</code> </p>
</blockquote>
<p> Ignore signals INT QUIT TSTP USR1 </p>
<blockquote><p> <code>trap date INT</code> </p>
</blockquote>
<p> Print date upon receiving signal INT </p>
 </dd>
<dt><code>type </code>[<i>name ...</i> ] </dt>
<dd> <p> Interpret each name as a command and print the resolution of the command search. Possible resolutions are: shell keyword, alias, shell builtin, command, tracked alias and not found. For aliases the alias expansion is printed; for commands and tracked aliases the complete pathname of the command is printed. </p>
 </dd>
<dt><code>ulimit </code> [-<code>H | -S</code> ] [-<code>a | -tfdscmlpnv </code>[<i>value</i> ] ] </dt>
<dd>  </dd>
<dd> <p> Inquire about or set the hard or soft limits on processes or set new limits. The choice between hard limit (which no process is allowed to violate, and which may not be raised once it has been lowered) and soft limit (which causes processes to be signaled but not necessarily killed, and which may be raised) is made with these flags: </p>
 </dd>
<dl>
<dt><code>-H</code></dt>
<dd> <p> set or inquire about hard limits </p>
 </dd>
<dt><code>-S</code></dt>
<dd> <p> set or inquire about soft limits. If neither -<code>H</code> nor -<code>S</code> is specified, the soft limit is displayed or both limits are set. If both are specified, the last one wins. </p>
 </dd></dl>
<p> The limit to be interrogated or set, then, is chosen by specifying any one of these flags: </p>
<dl>
<dt><code>-a</code></dt>
<dd> <p> show all the current limits </p>
 </dd>
<dt><code>-t</code></dt>
<dd> <p> show or set the limit on CPU time (in seconds) </p>
 </dd>
<dt><code>-f</code></dt>
<dd> <p> show or set the limit on the largest file that can be created (in 512-byte blocks) </p>
 </dd>
<dt><code>-d</code></dt>
<dd> <p> show or set the limit on the data segment size of a process (in kilobytes) </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> show or set the limit on the stack size of a process (in kilobytes) </p>
 </dd>
<dt><code>-c</code></dt>
<dd> <p> show or set the limit on the largest core dump size that can be produced (in 512-byte blocks) </p>
 </dd>
<dt><code>-m</code></dt>
<dd> <p> show or set the limit on the total physical memory that can be in use by a process (in kilobytes) </p>
 </dd>
<dt><code>-l</code></dt>
<dd> <p> show or set the limit on how much memory a process can lock with <a href="/docs/linux/man/2-mlock/">mlock</a>(2) (in kilobytes) </p>
 </dd>
<dt><code>-p</code></dt>
<dd> <p> show or set the limit on the number of processes this user can have at one time </p>
 </dd>
<dt><code>-n</code></dt>
<dd> <p> show or set the limit on the number files a process can have open at once </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> show or set the limit on the total virtual memory that can be in use by a process (in kilobytes) </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> show or set the limit on the real-time scheduling priority of a process </p>
 </dd></dl>
<p> If none of these is specified, it is the limit on file size that is shown or set. If value is specified, the limit is set to that number; otherwise the current limit is displayed. </p>
<p> Limits of an arbitrary process can be displayed or set using the <a href="/docs/linux/man/8-sysctl/">sysctl</a>(8) utility. </p>
<dt><code>umask </code>[<i>mask</i> ] </dt>
<dd> <p> Set the value of umask (see <a href="/docs/linux/man/2-umask/">umask</a>(2)) to the specified octal value. If the argument is omitted, the umask value is printed. </p>
 </dd>
<dt><code>unalias </code> [-<code>a</code> ] [<i>name</i> ] </dt>
<dd>  </dd>
<dd> <p> If <i>name</i> is specified, the shell removes that alias. If -<code>a</code> is specified, all aliases are removed. </p>
 </dd>
<dt><code>unset </code> [-<code>fv</code> ] <i>name ...</i></dt>
<dd>  </dd>
<dd> <p> The specified variables and functions are unset and unexported. If -<code>f</code> or -<code>v</code> is specified, the corresponding function or variable is unset, respectively. If a given name corresponds to both a variable and a function, and no options are given, only the variable is unset. </p>
 </dd>
<dt><code>wait </code>[<i>job</i> ] </dt>
<dd> <p> Wait for the specified job to complete and return the exit status of the last process in the job. If the argument is omitted, wait for all jobs to complete and return an exit status of zero. </p>
 </dd></dl>
<h3>Command Line Editing</h3>
<p> When <code>dash</code> is being used interactively from a terminal, the current command and the command history (see <code>fc</code> in Sx Builtins ) can be edited using vi-mode command-line editing. This mode uses commands, described below, similar to a subset of those described in the vi man page. The command `set&#8217; -o vi enables vi-mode editing and places sh into vi insert mode. With vi-mode enabled, sh can be switched between insert mode and command mode. It is similar to vi: typing Aq ESC enters vi command mode. Hitting Aq return while in command mode will pass the line to the shell.  </p>
<h2>EXIT STATUS</h2>
<p> Errors that are detected by the shell, such as a syntax error, will cause the shell to exit with a non-zero exit status. If the shell is not an interactive shell, the execution of the shell file will be aborted. Otherwise the shell will return the exit status of the last command executed, or if the exit builtin is used with a numeric argument, it will return the argument.  </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>HOME</code></dt>
<dd> <p> Set automatically by <a href="/docs/linux/man/1-login/">login</a>(1) from the user&#8217;s login directory in the password file (passwd(4) ) This environment variable also functions as the default argument for the cd builtin. </p>
 </dd>
<dt><code>PATH</code></dt>
<dd> <p> The default search path for executables. See the above section Sx Path Search . </p>
 </dd>
<dt><code>CDPATH</code></dt>
<dd> <p> The search path used with the cd builtin. </p>
 </dd>
<dt><code>MAIL</code></dt>
<dd> <p> The name of a mail file, that will be checked for the arrival of new mail. Overridden by <code>MAILPATH</code> </p>
 </dd>
<dt><code>MAILCHECK</code></dt>
<dd> <p> The frequency in seconds that the shell checks for the arrival of mail in the files specified by the <code>MAILPATH</code> or the <code>MAIL</code> file. If set to 0, the check will occur at each prompt. </p>
 </dd>
<dt><code>MAILPATH</code></dt>
<dd> <p> A colon ``:&#8216;&#8216; separated list of file names, for the shell to check for incoming mail. This environment setting overrides the <code>MAIL</code> setting. There is a maximum of 10 mailboxes that can be monitored at once. </p>
 </dd>
<dt><code>PS1</code></dt>
<dd> <p> The primary prompt string, which defaults to ``$&nbsp;&#8216;&#8216; unless you are the superuser, in which case it defaults to ``#&nbsp;&#8216;&#8216; </p>
 </dd>
<dt><code>PS2</code></dt>
<dd> <p> The secondary prompt string, which defaults to ``&gt;&nbsp;&#8216;&#8216; </p>
 </dd>
<dt><code>PS4</code></dt>
<dd> <p> Output before each line when execution trace (set -x) is enabled, defaults to ``+&nbsp;&#8216;&#8216; </p>
 </dd>
<dt><code>IFS</code></dt>
<dd> <p> Input Field Separators. This is normally set to Aq space , Aq tab , and Aq newline . See the Sx White Space Splitting section for more details. </p>
 </dd>
<dt><code>TERM</code></dt>
<dd> <p> The default terminal setting for the shell. This is inherited by children of the shell, and is used in the history editing modes. </p>
 </dd>
<dt><code>HISTSIZE</code></dt>
<dd> <p> The number of lines in the history buffer for the shell. </p>
 </dd>
<dt><code>PWD</code></dt>
<dd> <p> The logical value of the current working directory. This is set by the <code>cd</code> command. </p>
 </dd>
<dt><code>OLDPWD</code></dt>
<dd> <p> The previous logical value of the current working directory. This is set by the <code>cd</code> command. </p>
 </dd>
<dt><code>PPID</code></dt>
<dd> <p> The process ID of the parent process of the shell. </p>
 </dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>$HOME/.profile </code></dt>
<dd>  </dd>
<dt><code>/etc/profile </code></dt>
<dd>  </dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-csh/">csh</a>(1), <a href="/docs/linux/man/1-echo/">echo</a>(1), <a href="/docs/linux/man/1-getopt/">getopt</a>(1), ksh(1), <a href="/docs/linux/man/1-login/">login</a>(1), <a href="/docs/linux/man/1-printf/">printf</a>(1), <a href="/docs/linux/man/1-test/">test</a>(1), <a href="/docs/linux/man/3-getopt/">getopt</a>(3), <a href="/docs/linux/man/5-passwd/">passwd</a>(5), <a href="/docs/linux/man/7-environ/">environ</a>(7), <a href="/docs/linux/man/8-sysctl/">sysctl</a>(8)  </p>
<h2>HISTORY</h2>
<p> <code>dash</code> is a POSIX-compliant implementation of /bin/sh that aims to be as small as possible. <code>dash</code> is a direct descendant of the NetBSD version of ash (the Almquist SHell), ported to Linux in early 1997. It was renamed to <code>dash</code> in 2002.  </p>
<h2>BUGS</h2>
<p> Setuid shell scripts should be avoided at all costs, as they are a significant security risk. </p>
<p> PS1, PS2, and PS4 should be subject to parameter expansion before being displayed. </p>
