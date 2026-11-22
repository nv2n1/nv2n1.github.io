---

title: "mksh(1)"
name: "mksh"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mksh/"
description: "mksh sh – MirBSD Korn shell"
---

<p> <code>mksh</code> <code>sh</code> - MirBSD Korn shell </p>
<h2>SYNOPSIS</h2>
<p> -words [-<code>+abCefhiklmnprUuvXx </code>[-<code>T </code><i>/dev/ttyCn </i>| - ] ] [-<code>+o </code><i>option</i> ] [-<code>c </code><i>string |</i> -<code>s |</code> <i>file</i> [<i>argument ...</i> ] ] <br/>
<code>builtin-name</code> [<i>argument ...</i> ]  </p>
<h2>DESCRIPTION</h2>
<p> is a command interpreter intended for both interactive and shell script use. Its command language is a superset of the shC shell language and largely compatible to the original Korn shell.  </p>
<h3>I'm an Android user, so what's mksh?</h3>
<p> <code>mksh</code> is a UNIX shell / command interpreter, similar to <code>COMMAND.COM</code> or <code>CMD.EXE</code> which has been included with <code>Android Open Source Project</code> for a while now. Basically, it&#8217;s a program that runs in a terminal (console window), takes user input and runs commands or scripts, which it can also be asked to do by other programs, even in the background. Any privilege pop-ups you might be encountering are thus not <code>mksh</code> issues but questions by some other program utilising it.  </p>
<h3>Invocation</h3>
<p> Most builtins can be called directly, for example if a link points from its name to the shell; not all make sense, have been tested or work at all though. </p>
<p> The options are as follows: </p>
<dl>
<dt><code>-c </code><i>string</i></dt>
<dd> <p> will execute the command(s) contained in <i>string</i> </p>
 </dd>
<dt><code>-i</code></dt>
<dd> <p> Interactive shell. A shell is ``interactive&#8217;&#8216; if this option is used or if both standard input and standard error are attached to a <a href="/docs/linux/man/4-tty/">tty</a>(4). An interactive shell has job control enabled, ignores the <code>SIGINT</code> <code>SIGQUIT</code> and <code>SIGTERM</code> signals, and prints prompts before reading input (see the <code>PS1</code> and <code>PS2</code> parameters). It also processes the <code>ENV</code> parameter or the mkshrc file (see below). For non-interactive shells, the <code>trackall</code> option is on by default (see the <code>set</code> command below). </p>
 </dd>
<dt><code>-l</code></dt>
<dd> <p> Login shell. If the basename the shell is called with (i.e. argv[0]) starts with `-&#8216; or if this option is used, the shell is assumed to be a login shell; see Sx Startup files below. </p>
 </dd>
<dt><code>-p</code></dt>
<dd> <p> Privileged shell. A shell is ``privileged&#8217;&#8216; if this option is used or if the real user ID or group ID does not match the effective user ID or group ID (see <a href="/docs/linux/man/2-getuid/">getuid</a>(2) and <a href="/docs/linux/man/2-getgid/">getgid</a>(2)). Clearing the privileged option causes the shell to set its effective user ID (group ID) to its real user ID (group ID). For further implications, see Sx Startup files . </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> Restricted shell. A shell is ``restricted&#8217;&#8216; if this option is used. The following restrictions come into effect after the shell processes any profile and <code>ENV</code> files: </p>
 </dd>
<ul>
<li> <p> The <code>cd</code> Po and Ic chdir Pc command is disabled.  </li>
<li>  The <code>SHELL</code> <code>ENV</code> and <code>PATH</code> parameters cannot be changed.  </li>
<li>  Command names can&#8217;t be specified with absolute or relative paths.  </li>
<li>  The -<code>p</code> option of the built-in command <code>command</code> can&#8217;t be used.  </li>
<li>  Redirections that create files can&#8217;t be used (i.e. `&gt;&#8216; `&gt;|&#8216; `&gt;&gt;&#8216; `&lt;&gt;&#8216;  </li>
</ul>
 </p>
<dt><code>-s</code></dt>
<dd> <p> The shell reads commands from standard input; all non-option arguments are positional parameters. </p>
 </dd>
<dt><code>-T </code><i>tty</i></dt>
<dd> <p> Spawn on the <a href="/docs/linux/man/4-tty/">tty</a>(4) device given. Superuser only. If <i>tty</i> is a dash, detach from controlling terminal (daemonise) instead. </p>
 </dd></dl>
<p> In addition to the above, the options described in the <code>set</code> built-in command can also be used on the command line: both [-<code>+abCefhkmnuvXx </code>and ] [-<code>+o </code><i>option</i> ] can be used for single letter or long options, respectively. </p>
<p> If neither the -<code>c</code> nor the -<code>s</code> option is specified, the first non-option argument specifies the name of a file the shell reads commands from. If there are no non-option arguments, the shell reads commands from the standard input. The name of the shell (i.e. the contents of $0) is determined as follows: if the -<code>c</code> option is used and there is a non-option argument, it is used as the name; if commands are being read from a file, the file is used as the name; otherwise, the basename the shell was called with (i.e. argv[0]) is used. </p>
<p> The exit status of the shell is 127 if the command file specified on the command line could not be opened, or non-zero if a fatal syntax error occurred during the execution of a script. In the absence of fatal errors, the exit status is that of the last command executed, or zero, if no command is executed.  </p>
<h3>Startup files</h3>
<p> For the actual location of these files, see Sx FILES . A login shell processes the system profile first. A privileged shell then processes the suid profile. A non-privileged login shell processes the user profile next. A non-privileged interactive shell checks the value of the <code>ENV</code> parameter after subjecting it to parameter, command, arithmetic and tilde (`~&#8216; ) substitution; if unset or empty, the user mkshrc profile is processed; otherwise, if a file whose name is the substitution result exists, it is processed; non-existence is silently ignored.  </p>
<h3>Command syntax</h3>
<p> The shell begins parsing its input by removing any backslash-newline combinations, then breaking it into <i>words</i> Words (which are sequences of characters) are delimited by unquoted whitespace characters (space, tab, and newline) or meta-characters Po `&lt;&#8216; `&gt;&#8216; `|&#8216; `;&#8216; , `(&#8216; , `)&#8216; , and `&amp;&#8216; Pc . Aside from delimiting words, spaces and tabs are ignored, while newlines usually delimit commands. The meta-characters are used in building the following <i>tokens</i> `&lt;&#8216; `&lt;&amp;&#8216; , `&lt;&lt;&#8216; `&lt;&lt;&lt;&#8216; `&gt;&#8216; `&gt;&amp;&#8216; , `&gt;&gt;&#8216; `&amp;&gt;&#8216; etc. are used to specify redirections (see Sx Input/output redirection below); `|&#8216; is used to create pipelines; `|&amp;&#8216; is used to create co-processes (see Sx Co-processes below); `;&#8216; is used to separate commands; `&amp;&#8216; is used to create asynchronous pipelines; `&amp;&amp;&#8216; and `||&#8216; are used to specify conditional execution; `;;&#8216; , `;&amp;&#8216; and `;|&#8216; are used in <code>case</code> statements; `((&#8216; is used in arithmetic expressions; and lastly, `(&#8216; is used to create subshells. </p>
<p> Whitespace and meta-characters can be quoted individually using a backslash (`\&#8216; ) or in groups using double (`&#8216; ) or single (`&#8216;&#8216; ) quotes. Note that the following characters are also treated specially by the shell and must be quoted if they are to represent themselves: `\&#8216; , `&#8216; , `&#8216;&#8216; , `#&#8216; , `$&#8216; , ``&#8216; , `~&#8216; , `{&#8216; , `}&#8216; , `*&#8216; , `?&#8216; , and `[&#8216; The first three of these are the above mentioned quoting characters (see Sx Quoting below); `#&#8216; , if used at the beginning of a word, introduces a comment --- everything after the `#&#8216; up to the nearest newline is ignored; `$&#8216; is used to introduce parameter, command, and arithmetic substitutions (see Sx Substitution below); ``&#8216; introduces an old-style command substitution (see Sx Substitution below); `~&#8216; begins a directory expansion (see Sx Tilde expansion below); `{&#8216; and `}&#8216; delimit <a href="/docs/linux/man/1-csh/">csh</a>(1)Ns-style alterations (see Sx Brace expansion below); and finally, `*&#8216; , `?&#8216; , and `[&#8216; are used in file name generation (see Sx File name patterns below). </p>
<p> As words and tokens are parsed, the shell builds commands, of which there are two basic types: <i>simple-commands</i> typically programmes that are executed, and <i>compound-commands</i> such as <code>for</code> and <code>if</code> statements, grouping constructs, and function definitions. </p>
<p> A simple-command consists of some combination of parameter assignments (see Sx Parameters below), input/output redirections (see Sx Input/output redirections below), and command words; the only restriction is that parameter assignments come before any command words. The command words, if any, define the command that is to be executed and its arguments. The command may be a shell built-in command, a function, or an external command (i.e. a separate executable file that is located using the <code>PATH</code> parameter; see Sx Command execution below). Note that all command constructs have an exit status: for external commands, this is related to the status returned by <a href="/docs/linux/man/2-wait/">wait</a>(2) (if the command could not be found, the exit status is 127; if it could not be executed, the exit status is 126); the exit status of other command constructs (built-in commands, functions, compound-commands, pipelines, lists, etc.) are all well-defined and are described where the construct is described. The exit status of a command consisting only of parameter assignments is that of the last command substitution performed during the parameter assignment or 0 if there were no command substitutions. </p>
<p> Commands can be chained together using the `|&#8216; token to form pipelines, in which the standard output of each command but the last is piped (see <a href="/docs/linux/man/2-pipe/">pipe</a>(2)) to the standard input of the following command. The exit status of a pipeline is that of its last command, unless the <code>pipefail</code> option is set (see there). All commands of a pipeline are executed in separate subshells; this is allowed by POSIX but differs from both variants of AT&amp;T System <code>ksh</code> where all but the last command were executed in subshells; see the <code>read</code> builtin&#8217;s description for implications and workarounds. A pipeline may be prefixed by the `!&#8216; reserved word which causes the exit status of the pipeline to be logically complemented: if the original status was 0, the complemented status will be 1; if the original status was not 0, the complemented status will be 0. </p>
<p> <i>Lists</i> of commands can be created by separating pipelines by any of the following tokens: `&amp;&amp;&#8216; , `||&#8216; `&amp;&#8216; , `|&amp;&#8216; , and `;&#8216; The first two are for conditional execution: ``<i>cmd1 </i><code>&amp;&amp; </code><i>cmd2</i> &#8216;&#8216; executes <i>cmd2</i> only if the exit status of <i>cmd1</i> is zero; `||&#8216; is the opposite --- <i>cmd2</i> is executed only if the exit status of <i>cmd1</i> is non-zero. `&amp;&amp;&#8216; and `||&#8216; have equal precedence which is higher than that of `&amp;&#8216; , `|&amp;&#8216; , and `;&#8216; , which also have equal precedence. Note that the `&amp;&amp;&#8216; and `||&#8216; operators are Qq left-associative . For example, both of these commands will print only Qq bar : </p>
<blockquote><pre><code>$ false &amp;&amp; echo foo || echo bar
$ true || echo foo &amp;&amp; echo bar
</code></pre>
</blockquote>
<p> The `&amp;&#8216; token causes the preceding command to be executed asynchronously; that is, the shell starts the command but does not wait for it to complete (the shell does keep track of the status of asynchronous commands; see Sx Job control below). When an asynchronous command is started when job control is disabled (i.e. in most scripts), the command is started with signals <code>SIGINT</code> and <code>SIGQUIT</code> ignored and with input redirected from /dev/null (however, redirections specified in the asynchronous command have precedence). The `|&amp;&#8216; operator starts a co-process which is a special kind of asynchronous process (see Sx Co-processes below). Note that a command must follow the `&amp;&amp;&#8216; and `||&#8216; operators, while it need not follow `&amp;&#8216; , `|&amp;&#8216; , or `;&#8216; The exit status of a list is that of the last command executed, with the exception of asynchronous lists, for which the exit status is 0. </p>
<p> Compound commands are created using the following reserved words. These words are only recognised if they are unquoted and if they are used as the first word of a command (i.e. they can&#8217;t be preceded by parameter assignments or redirections): </p>
<blockquote><pre><code>case else function then ! (
do esac if time [[ ((
done fi in until {
elif for select while }
</code></pre>
</blockquote>
<p> In the following compound command descriptions, command lists (denoted as <i>list</i> that are followed by reserved words must end with a semicolon, a newline, or a (syntactically correct) reserved word. For example, the following are all valid: </p>
<blockquote><pre><code>$ { echo foo; echo bar; }
$ { echo foo; echo bar&lt;newline&gt;}
$ { { echo foo; echo bar; } }
</code></pre>
</blockquote>
<p> This is not valid: </p>
<blockquote><p> <code>$ { echo foo; echo bar</code> </p>
</blockquote>
<dl>
<dt><code>(</code><i>list</i> ) </dt>
<dd> <p> Execute <i>list</i> in a subshell. There is no implicit way to pass environment changes from a subshell back to its parent. </p>
 </dd>
<dt><code>{ </code><i>list ; </i><code>}</code></dt>
<dd> <p> Compound construct; <i>list</i> is executed, but not in a subshell. Note that `{&#8216; and `}&#8216; are reserved words, not meta-characters. </p>
 </dd>
<dt><code> case </code><i>word </i><code>in</code> [[(] <i>pattern</i> [| <i>pat</i> ] <code>... )</code><i>list</i> [;; | ;&amp; | ;|&nbsp;<wbr>] ... esac] </dt>
<dd>  </dd>
<dd> <p> The <code>case</code> statement attempts to match <i>word</i> against a specified <i>pattern</i> the <i>list</i> associated with the first successfully matched pattern is executed. Patterns used in <code>case</code> statements are the same as those used for file name patterns except that the restrictions regarding `.&#8216; and `/&#8216; are dropped. Note that any unquoted space before and after a pattern is stripped; any space within a pattern must be quoted. Both the word and the patterns are subject to parameter, command, and arithmetic substitution, as well as tilde substitution. </p>
<p> For historical reasons, open and close braces may be used instead of <code>in</code> and <code>esac</code> e.g. <code>case $foo { *) echo bar;; }</code> </p>
<p> The list terminators are: </p>
 </dd>
<dl>
<dt><code>`;;&#8216; </code></dt>
<dd> <p> Terminate after the list. </p>
 </dd>
<dt><code>`;&amp;&#8216; </code></dt>
<dd> <p> Fall through into the next list. </p>
 </dd>
<dt><code>`;|&#8216; </code></dt>
<dd> <p> Evaluate the remaining pattern-list tuples. </p>
 </dd></dl>
<p> The exit status of a <code>case</code> statement is that of the executed <i>list</i> if no <i>list</i> is executed, the exit status is zero. </p>
<dt><code> for </code><i>name</i> [in <i>word </i><code>... </code>] <code>do </code><i>list ; </i><code>done</code></dt>
<dd>  </dd>
<dd> <p> For each <i>word</i> in the specified word list, the parameter <i>name</i> is set to the word and <i>list</i> is executed. If <code>in</code> is not used to specify a word list, the positional parameters ($1, $2, etc.) are used instead. For historical reasons, open and close braces may be used instead of <code>do</code> and <code>done</code> e.g. <code>for i; { echo $i; }</code> The exit status of a <code>for</code> statement is the last exit status of <i>list</i> if <i>list</i> is never executed, the exit status is zero. </p>
 </dd>
<dt><code> if </code><i>list</i><code>then </code><i>list</i> [elif <i>list</i><code>then </code><i>list ; </i>] <code>...</code> [else <i>list ; </i>] <code>fi</code></dt>
<dd>  </dd>
<dd> <p> If the exit status of the first <i>list</i> is zero, the second <i>list</i> is executed; otherwise, the <i>list</i> following the <code>elif</code> if any, is executed with similar consequences. If all the lists following the <code>if</code> and <code>elif s</code> fail (i.e. exit with non-zero status), the <i>list</i> following the <code>else</code> is executed. The exit status of an <code>if</code> statement is that of non-conditional <i>list</i> that is executed; if no non-conditional <i>list</i> is executed, the exit status is zero. </p>
 </dd>
<dt><code> select </code><i>name</i> [in <i>word </i><code>... </code>] <code>do </code><i>list ; </i><code>done</code></dt>
<dd>  </dd>
<dd> <p> The <code>select</code> statement provides an automatic method of presenting the user with a menu and selecting from it. An enumerated list of the specified <i>word </i><code>(s)</code> is printed on standard error, followed by a prompt Po <code>PS3: normally</code> `#?&nbsp;<wbr>&#8216; Pc . A number corresponding to one of the enumerated words is then read from standard input, <i>name</i> is set to the selected word (or unset if the selection is not valid), <code>REPLY</code> is set to what was read (leading/trailing space is stripped), and <i>list</i> is executed. If a blank line (i.e. zero or more <code>IFS</code> octets) is entered, the menu is reprinted without executing <i>list</i> </p>
<p> When <i>list</i> completes, the enumerated list is printed if <code>REPLY</code> is <code>NULL</code> the prompt is printed, and so on. This process continues until an end-of-file is read, an interrupt is received, or a <code>break</code> statement is executed inside the loop. If ``in word ...&#8216;&#8216; is omitted, the positional parameters are used (i.e. $1, $2, etc.). For historical reasons, open and close braces may be used instead of <code>do</code> and <code>done</code> e.g. <code>select i; { echo $i; }</code> The exit status of a <code>select</code> statement is zero if a <code>break</code> statement is used to exit the loop, non-zero otherwise. </p>
 </dd>
<dt><code> until </code><i>list</i><code>do </code><i>list</i><code>done</code></dt>
<dd>  </dd>
<dd> <p> This works like <code>while</code> except that the body is executed only while the exit status of the first <i>list</i> is non-zero. </p>
 </dd>
<dt><code> while </code><i>list</i><code>do </code><i>list</i><code>done</code></dt>
<dd>  </dd>
<dd> <p> A <code>while</code> is a pre-checked loop. Its body is executed as often as the exit status of the first <i>list</i> is zero. The exit status of a <code>while</code> statement is the last exit status of the <i>list</i> in the body of the loop; if the body is not executed, the exit status is zero. </p>
 </dd>
<dt><code> function </code><i>name</i><code>{ </code><i>list ; </i><code>}</code></dt>
<dd>  </dd>
<dd> <p> Defines the function <i>name</i> (see Sx Functions below). Note that redirections specified after a function definition are performed whenever the function is executed, not when the function definition is executed. </p>
 </dd>
<dt><i>name </i><code>() </code><i>command</i></dt>
<dd> <p> Mostly the same as <code>function</code> (see Sx Functions below). Whitespace (space or tab) after <i>name</i> will be ignored most of the time. </p>
 </dd>
<dt><code> function </code><i>name </i><code>()</code><code>{ </code><i>list ; </i><code>}</code></dt>
<dd>  </dd>
<dd> <p> The same as <i>name </i><code>()</code> (<code>bash ism</code> ) The <code>function</code> keyword is ignored. </p>
 </dd>
<dt><code> time </code>[-<code>p</code> ] [<i>pipeline</i> ] </dt>
<dd>  </dd>
<dd> <p> The Sx Command execution section describes the <code>time</code> reserved word. </p>
 </dd>
<dt><code>(( </code><i>expression </i><code>))</code></dt>
<dd> <p> The arithmetic expression <i>expression</i> is evaluated; equivalent to ``let expression&#8217;&#8216; (see Sx Arithmetic expressions and the <code>let</code> command, below). </p>
 </dd>
<dt><code>Bq </code>Bq <i>&nbsp;<wbr>expression&nbsp;<wbr></i></dt>
<dd> <p> Similar to the <code>test</code> and <code>[ ... ]</code> commands (described later), with the following exceptions: </p>
 </dd>
<ul>
<li> <p> Field splitting and file name generation are not performed on arguments.  </li>
<li>  The -<code>a</code> (AND) and -<code>o</code> (OR) operators are replaced with `&amp;&amp;&#8216; and `||&#8216; respectively.  </li>
<li>  Operators (e.g. `-<code>f</code> &#8216; `=&#8216; `!&#8216; must be unquoted.  </li>
<li>  Parameter, command, and arithmetic substitutions are performed as expressions are evaluated and lazy expression evaluation is used for the `&amp;&amp;&#8216; and `||&#8216; operators. This means that in the following statement, <code>$(&lt;foo)</code> is evaluated if and only if the file foo exists and is readable: </p>
<blockquote><pre><code>$ [[ -r foo &amp;&amp; $(&lt;foo) = b*r ]]
</code></pre>
</blockquote>
 </li>
<li> <p> The second operand of the `!=&#8216; and `=&#8216; expressions are patterns (e.g. the comparison <code>[[ foobar = f*r ]]</code> succeeds). This even works indirectly: </p>
<blockquote><pre><code>$ bar=foobar; baz='f*r'
$ [[ $bar = $baz ]]; echo $?
$ [[ $bar = &quot;$baz&quot; ]]; echo $?
</code></pre>
</blockquote>
<p> Perhaps surprisingly, the first comparison succeeds, whereas the second doesn&#8217;t.  </li>
</ul>
 </p>
<h3>Quoting</h3>
<p> Quoting is used to prevent the shell from treating characters or words specially. There are three methods of quoting. First, `\&#8216; quotes the following character, unless it is at the end of a line, in which case both the `\&#8216; and the newline are stripped. Second, a single quote (`&#8216;&#8216; ) quotes everything up to the next single quote (this may span lines). Third, a double quote (`&#8216; ) quotes all characters, except `$&#8216; , ``&#8216; and `\&#8216; , up to the next unquoted double quote. `$&#8216; and ``&#8216; inside double quotes have their usual meaning (i.e. parameter, command, or arithmetic substitution) except no field splitting is carried out on the results of double-quoted substitutions. If a `\&#8216; inside a double-quoted string is followed by `\&#8216; , `$&#8216; , ``&#8216; , or `&#8216; , it is replaced by the second character; if it is followed by a newline, both the `\&#8216; and the newline are stripped; otherwise, both the `\&#8216; and the character following are unchanged. </p>
<p> If a single-quoted string is preceded by an unquoted `$&#8216; , C style backslash expansion (see below) is applied (even single quote characters inside can be escaped and do not terminate the string then); the expanded result is treated as any other single-quoted string. If a double-quoted string is preceded by an unquoted `$&#8216; , the latter is ignored.  </p>
<h3>Backslash expansion</h3>
<p> In places where backslashes are expanded, certain C and AT&amp;T System <code>ksh</code> or GNU <code>bash</code> style escapes are translated. These include `\a&#8217; , `\b&#8217; , `\f&#8217; , `\n&#8217; , `\r&#8217; , `\t&#8217; , `\U########&#8216; , `\u####&#8216; , and `\v&#8217; For `\U########&#8216; and `\u####&#8216; , ``#&#8216;&#8216; means a hexadecimal digit, of thich there may be none up to four or eight; these escapes translate a Unicode codepoint to UTF-8. Furthermore, `\E&#8217; and `\e&#8217; expand to the escape character. </p>
<p> In the <code>print</code> builtin mode, `\&#8216; , `\&#8216;&#8216; , and `\?&#8216; are explicitly excluded; octal sequences must have the none up to three octal digits ``#&#8216;&#8216; prefixed with the digit zero (`\0###&#8216; ) hexadecimal sequences `\x##&#8216; are limited to none up to two hexadecimal digits ``#&#8216;&#8216; both octal and hexadecimal sequences convert to raw octets; `\#&#8216; , where # is none of the above, translates to \# (backslashes are retained). </p>
<p> Backslash expansion in the C style mode slightly differs: octal sequences `\###&#8216; must have no digit zero prefixing the one up to three octal digits ``#&#8216;&#8216; and yield raw octets; hexadecimal sequences `\x#*&#8216; greedily eat up as many hexadecimal digits ``#&#8216;&#8216; as they can and terminate with the first non-hexadecimal digit; these translate a Unicode codepoint to UTF-8. The sequence `\c#&#8216; , where ``#&#8216;&#8216; is any octet, translates to Ctrl-# (which basically means, `\c?&#8216; becomes DEL, everything else is bitwise ANDed with 0x1F). Finally, `\#&#8216; , where # is none of the above, translates to # (has the backslash trimmed), even if it is a newline.  </p>
<h3>Aliases</h3>
<p> There are two types of aliases: normal command aliases and tracked aliases. Command aliases are normally used as a short hand for a long or often used command. The shell expands command aliases (i.e. substitutes the alias name for its value) when it reads the first word of a command. An expanded alias is re-processed to check for more aliases. If a command alias ends in a space or tab, the following word is also checked for alias expansion. The alias expansion process stops when a word that is not an alias is found, when a quoted word is found, or when an alias word that is currently being expanded is found. Aliases are specifically an interactive feature: while they do happen to work in scripts and on the command line in some cases, aliases are expanded during lexing, so their use must be in a separate command tree from their definition; otherwise, the alias will not be found. Noticeably, command lists (separated by semicolon, in command substitutions also by newline) may be one same parse tree. </p>
<p> The following command aliases are defined automatically by the shell: </p>
<blockquote><pre><code>autoload='typeset -fu'
functions='typeset -f'
hash='alias -t'
history='fc -l'
integer='typeset -i'
local='typeset'
login='exec login'
nameref='typeset -n'
nohup='nohup '
r='fc -e -'
stop='kill -STOP'
suspend='kill -STOP $$'
type='whence -v'
</code></pre>
</blockquote>
<p> Tracked aliases allow the shell to remember where it found a particular command. The first time the shell does a path search for a command that is marked as a tracked alias, it saves the full path of the command. The next time the command is executed, the shell checks the saved path to see that it is still valid, and if so, avoids repeating the path search. Tracked aliases can be listed and created using <code>alias -t</code> Note that changing the <code>PATH</code> parameter clears the saved paths for all tracked aliases. If the <code>trackall</code> option is set (i.e. <code>set -o trackall</code> or <code>set -h )</code> the shell tracks all commands. This option is set automatically for non-interactive shells. For interactive shells, only the following commands are automatically tracked: <a href="/docs/linux/man/1-cat/">cat</a>(1), <a href="/docs/linux/man/1-cc/">cc</a>(1), <a href="/docs/linux/man/1-chmod/">chmod</a>(1), <a href="/docs/linux/man/1-cp/">cp</a>(1), <a href="/docs/linux/man/1-date/">date</a>(1), <a href="/docs/linux/man/1-ed/">ed</a>(1), <a href="/docs/linux/man/1-emacs/">emacs</a>(1), <a href="/docs/linux/man/1-grep/">grep</a>(1), <a href="/docs/linux/man/1-ls/">ls</a>(1), <a href="/docs/linux/man/1-make/">make</a>(1), <a href="/docs/linux/man/1-mv/">mv</a>(1), <a href="/docs/linux/man/1-pr/">pr</a>(1), <a href="/docs/linux/man/1-rm/">rm</a>(1), <a href="/docs/linux/man/1-sed/">sed</a>(1), <a href="/docs/linux/man/1-sh/">sh</a>(1), <a href="/docs/linux/man/1-vi/">vi</a>(1), and <a href="/docs/linux/man/1-who/">who</a>(1).  </p>
<h3>Substitution</h3>
<p> The first step the shell takes in executing a simple-command is to perform substitutions on the words of the command. There are three kinds of substitution: parameter, command, and arithmetic. Parameter substitutions, which are described in detail in the next section, take the form $ <i>name</i> or ${ <i>... </i><code>}</code> command substitutions take the form $( <i>command </i><code>)</code> or (deprecated) ` <i>command </i><code>`</code> or (executed in the current environment) ${&nbsp;<wbr> <i>command </i><code>;}</code> and strip trailing newlines; and arithmetic substitutions take the form $(( <i>expression </i><code>))</code> Parsing the current-environment command substitution requires a space, tab or newline after the opening brace and that the closing brace be recognised as a keyword (i.e. is preceded by a newline or semicolon). They are also called funsubs (function substitutions) and behave like functions in that <code>local</code> and <code>return</code> work, and in that <code>exit</code> terminates the parent shell. </p>
<p> Another variant of substitution are the valsubs (value substitutions) ${| <i>command </i><code>;}</code> which are also executed in the current environment, like funsubs, but share their I/O with the parent; instead, they evaluate to whatever the, initially empty, expression-local variable <code>REPLY</code> is set to within the <i>command </i><code>s</code> </p>
<p> If a substitution appears outside of double quotes, the results of the substitution are generally subject to word or field splitting according to the current value of the <code>IFS</code> parameter. The <code>IFS</code> parameter specifies a list of octets which are used to break a string up into several words; any octets from the set space, tab, and newline that appear in the <code>IFS</code> octets are called ``IFS whitespace&#8217;&#8216; Sequences of one or more <code>IFS</code> whitespace octets, in combination with zero or one non- <code>IFS</code> whitespace octets, delimit a field. As a special case, leading and trailing <code>IFS</code> whitespace and trailing <code>IFS</code> non-whitespace are stripped (i.e. no leading or trailing empty field is created by it); leading non- <code>IFS</code> whitespace does create an empty field. </p>
<p> Example: If <code>IFS</code> is set to ``&lt;space&gt;:&#8216;&#8216; and VAR is set to ``&lt;space&gt;A&lt;space&gt;:&lt;space&gt;&lt;space&gt;B::D&#8217;&#8216; the substitution for $VAR results in four fields: `A&#8217; `B&#8217; `(an empty field),&#8216; and `D&#8217; Note that if the <code>IFS</code> parameter is set to the <code>NULL</code> string, no field splitting is done; if the parameter is unset, the default value of space, tab, and newline is used. </p>
<p> Also, note that the field splitting applies only to the immediate result of the substitution. Using the previous example, the substitution for $VAR:E results in the fields: `A&#8217; `B&#8217; `,&#8216; and `D:E&#8217; not `A&#8217; `B&#8217; `,&#8216; `D&#8217; and `E&#8217; This behavior is POSIX compliant, but incompatible with some other shell implementations which do field splitting on the word which contained the substitution or use <code>IFS</code> as a general whitespace delimiter. </p>
<p> The results of substitution are, unless otherwise specified, also subject to brace expansion and file name expansion (see the relevant sections below). </p>
<p> A command substitution is replaced by the output generated by the specified command which is run in a subshell. For $( <i>command </i><code>)</code> and ${&nbsp;<wbr> <i>command </i><code>;}</code> substitutions, normal quoting rules are used when <i>command</i> is parsed; however, for the deprecated ` <i>command </i><code>`</code> form, a `\&#8216; followed by any of `$&#8216; , ``&#8216; , or `\&#8216; is stripped (a `\&#8216; followed by any other character is unchanged). As a special case in command substitutions, a command of the form &lt; <i>file</i> is interpreted to mean substitute the contents of <i>file</i> Note that <code>$(&lt;foo)</code> has the same effect as <code>$(cat foo)</code> </p>
<p> Note that some shells do not use a recursive parser for command substitutions, leading to failure for certain constructs; to be portable, use as workaround `x=$(cat)&#8216; &lt;&lt;EOF (or the newline-keeping `x=&lt;&lt;EOF&#8217; extension) instead to merely slurp the string. St -p1003.1 recommends to use case statements of the form `x=$(case&#8217; $foo in (bar) echo $bar ;; (*) echo $baz ;; esac) instead, which would work but not serve as example for this portability issue. </p>
<blockquote><pre><code>x=$(case $foo in bar) echo $bar ;; *) echo $baz ;; esac)
# above fails to parse on old shells; below is the workaround
x=$(eval $(cat)) &lt;&lt;&quot;EOF&quot;
case $foo in bar) echo $bar ;; *) echo $baz ;; esac
EOF
</code></pre>
</blockquote>
<p> Arithmetic substitutions are replaced by the value of the specified expression. For example, the command <code>print $((2+3*4))</code> displays 14. See Sx Arithmetic expressions for a description of an expression.  </p>
<h3>Parameters</h3>
<p> Parameters are shell variables; they can be assigned values and their values can be accessed using a parameter substitution. A parameter name is either one of the special single punctuation or digit character parameters described below, or a letter followed by zero or more letters or digits Po `_&#8216; counts as a letter Pc . The latter form can be treated as arrays by appending an array index of the form [<i>expr</i> ] where <i>expr</i> is an arithmetic expression. Array indices in are limited to the range 0 through 4294967295, inclusive. That is, they are a 32-bit unsigned integer. </p>
<p> Parameter substitutions take the form $ <i>name</i> ${ <i>name </i><code>}</code> or ${ <i>name </i>[<i>expr </i>] where <i>name</i> is a parameter name. Substitution of all array elements with ${ <i>name </i><code>[*]}</code> and ${ <i>name </i><code>[@]}</code> works equivalent to $* and $@ for positional parameters. If substitution is performed on a parameter (or an array parameter element) that is not set, a null string is substituted unless the <code>nounset</code> option Po <code>set -o nounset</code> or <code>set -u</code> Pc is set, in which case an error occurs. </p>
<p> Parameters can be assigned values in a number of ways. First, the shell implicitly sets some parameters like `#&#8216; , `PWD&#8217; , and `$&#8216; ; this is the only way the special single character parameters are set. Second, parameters are imported from the shell&#8217;s environment at startup. Third, parameters can be assigned values on the command line: for example, <code>FOO=bar</code> sets the parameter ``FOO&#8217;&#8216; to ``bar&#8217;&#8216; multiple parameter assignments can be given on a single command line and they can be followed by a simple-command, in which case the assignments are in effect only for the duration of the command (such assignments are also exported; see below for the implications of this). Note that both the parameter name and the `=&#8216; must be unquoted for the shell to recognise a parameter assignment. The construct <code>FOO+=baz</code> is also recognised; the old and new values are immediately concatenated. The fourth way of setting a parameter is with the <code>export</code> <code>global</code> <code>readonly</code> and <code>typeset</code> commands; see their descriptions in the Sx Command execution section. Fifth, <code>for</code> and <code>select</code> loops set parameters as well as the <code>getopts</code> <code>read</code> and <code>set -A</code> commands. Lastly, parameters can be assigned values using assignment operators inside arithmetic expressions (see Sx Arithmetic expressions below) or using the ${ <i>name </i><code>= </code><i>value </i><code>}</code> form of the parameter substitution (see below). </p>
<p> Parameters with the export attribute (set using the <code>export</code> or <code>typeset -x</code> commands, or by parameter assignments followed by simple commands) are put in the environment (see <a href="/docs/linux/man/7-environ/">environ</a>(7)) of commands run by the shell as <i>name </i><code>= </code><i>value</i> pairs. The order in which parameters appear in the environment of a command is unspecified. When the shell starts up, it extracts parameters and their values from its environment and automatically sets the export attribute for those parameters. </p>
<p> Modifiers can be applied to the ${ <i>name </i><code>}</code> form of parameter substitution: </p>
<dl>
<dt><code>${ </code><i>name </i><code>:- </code><i>word </i><code>}</code></dt>
<dd> <p> If <i>name</i> is set and not <code>NULL</code> it is substituted; otherwise, <i>word</i> is substituted. </p>
 </dd>
<dt><code>${ </code><i>name </i><code>:+ </code><i>word </i><code>}</code></dt>
<dd> <p> If <i>name</i> is set and not <code>NULL</code> <i>word</i> is substituted; otherwise, nothing is substituted. </p>
 </dd>
<dt><code>${ </code><i>name </i><code>:= </code><i>word </i><code>}</code></dt>
<dd> <p> If <i>name</i> is set and not <code>NULL</code> it is substituted; otherwise, it is assigned <i>word</i> and the resulting value of <i>name</i> is substituted. </p>
 </dd>
<dt><code>${ </code><i>name </i><code>:? </code><i>word </i><code>}</code></dt>
<dd> <p> If <i>name</i> is set and not <code>NULL</code> it is substituted; otherwise, <i>word</i> is printed on standard error (preceded by <i>name :</i> and an error occurs (normally causing termination of a shell script, function, or script sourced using the `.&#8216; built-in). If <i>word</i> is omitted, the string ``parameter null or not set&#8217;&#8216; is used instead. Currently a bug, if <i>word</i> is a variable which expands to the null string, the error message is also printed. </p>
 </dd></dl>
<p> Note that, for all of the above, <i>word</i> is actually considered quoted, and special parsing rules apply. The parsing rules also differ on whether the expression is double-quoted: <i>word</i> then uses double-quoting rules, except for the double quote itself (`&#8216; ) and the closing brace, which, if backslash escaped, gets quote removal applied. </p>
<p> In the above modifiers, the `:&#8216; can be omitted, in which case the conditions only depend on <i>name</i> being set (as opposed to set and not <code>NULL )</code> If <i>word</i> is needed, parameter, command, arithmetic, and tilde substitution are performed on it; if <i>word</i> is not needed, it is not evaluated. </p>
<p> The following forms of parameter substitution can also be used (if <i>name</i> is an array, its element #0 will be substituted in a scalar context): </p>
<dl>
<dt><code>${# </code><i>name </i><code>}</code></dt>
<dd> <p> The number of positional parameters if <i>name</i> is `*&#8216; , `@&#8216; , or not specified; otherwise the length (in characters) of the string value of parameter <i>name</i> </p>
 </dd>
<dt><code>${# </code><i>name </i><code>[*]}</code></dt>
<dd>  </dd>
<dt><code>${# </code><i>name </i><code>[@]}</code></dt>
<dd> <p> The number of elements in the array <i>name</i> </p>
 </dd>
<dt><code>${% </code><i>name </i><code>}</code></dt>
<dd> <p> The width (in screen columns) of the string value of parameter <i>name</i> or -1 if ${ <i>name </i><code>}</code> contains a control character. </p>
 </dd>
<dt><code>${! </code><i>name </i><code>}</code></dt>
<dd> <p> The name of the variable referred to by <i>name</i> This will be <i>name</i> except when <i>name</i> is a name reference (bound variable), created by the <code>nameref</code> command (which is an alias for <code>typeset -n</code> </p>
 </dd>
<dt><code>${! </code><i>name </i><code>[*]}</code></dt>
<dd>  </dd>
<dt><code>${! </code><i>name </i><code>[@]}</code></dt>
<dd> <p> The names of indices (keys) in the array <i>name</i> </p>
 </dd>
<dt> ${ <i>name</i> # <i>pattern </i><code>}</code></dt>
<dd>  </dd>
<dt> ${ <i>name</i> ## <i>pattern </i><code>}</code></dt>
<dd>  </dd>
<dd> <p> If <i>pattern</i> matches the beginning of the value of parameter <i>name</i> the matched text is deleted from the result of substitution. A single `#&#8216; results in the shortest match, and two of them result in the longest match. Cannot be applied to a vector (${*} or ${@} or ${array[*]} or ${array[@]}) </p>
 </dd>
<dt> ${ <i>name</i> % <i>pattern </i><code>}</code></dt>
<dd>  </dd>
<dt> ${ <i>name</i> %% <i>pattern </i><code>}</code></dt>
<dd>  </dd>
<dd> <p> Like ${..#..} substitution, but it deletes from the end of the value. Cannot be applied to a vector. </p>
 </dd>
<dt> ${ <i>name</i> / <i>pattern / string </i><code>}</code></dt>
<dd>  </dd>
<dt> ${ <i>name</i> // <i>pattern / string </i><code>}</code></dt>
<dd>  </dd>
<dd> <p> Like ${..#..} substitution, but it replaces the longest match of <i>pattern</i> anchored anywhere in the value, with <i>string</i> If <i>pattern</i> begins with `#&#8216; , it is anchored at the beginning of the value; if it begins with `%&#8216; , it is anchored at the end. Patterns that are empty or consist only of wildcards are invalid. A single `/&#8216; replaces the first occurence of the search <i>pattern</i> and two of them replace all occurences. If / <i>string</i> is omitted, the <i>pattern</i> is replaced by the empty string, i.e. deleted. Cannot be applied to a vector. Inefficiently implemented, may be slow. </p>
 </dd>
<dt> ${ <i>name : </i><i>pos</i> : <i>len </i><code>}</code></dt>
<dd>  </dd>
<dd> <p> The first <i>len</i> characters of <i>name</i> starting at position <i>pos</i> are substituted. Both <i>pos</i> and : <i>len</i> are optional. If <i>pos</i> is negative, counting starts at the end of the string; if it is omitted, it defaults to 0. If <i>len</i> is omitted or greater than the length of the remaining string, all of it is substituted. Both <i>pos</i> and <i>len</i> are evaluated as arithmetic expressions. Currently, <i>pos</i> must start with a space, opening parenthesis or digit to be recognised. Cannot be applied to a vector. </p>
 </dd>
<dt> ${ <i>name</i> @# [<i>seed </i><code>}</code> ] </dt>
<dd>  </dd>
<dd> <p> The internal hash of the expansion of <i>name</i> with an optional (defaulting to zero) [<i>seed</i> ] At the moment, this is NZAAT (a 32-bit hash based on Bob Jenkins&#8217; one-at-a-time hash), but this is not set. This is the hash the shell uses internally for its associative arrays. </p>
 </dd>
<dt><code>${ </code><i>name </i><code>@Q}</code></dt>
<dd> <p> A quoted expression safe for re-entry, whose value is the value of the <i>name</i> parameter, is substituted. </p>
 </dd></dl>
<p> Note that <i>pattern</i> may need extended globbing pattern (@(...)) single (&#8216;...&#8216;) or double (...) quote escaping unless -<code>o sh</code> is set. </p>
<p> The following special parameters are implicitly set by the shell and cannot be set directly using assignments: </p>
<dl>
<dt><code>!</code></dt>
<dd> <p> Process ID of the last background process started. If no background processes have been started, the parameter is not set. </p>
 </dd>
<dt><code>#</code></dt>
<dd> <p> The number of positional parameters ($1, $2, etc.). </p>
 </dd>
<dt><code>$</code></dt>
<dd> <p> The PID of the shell, or the PID of the original shell if it is a subshell. Do <i>NOT</i> use this mechanism for generating temporary file names; see <a href="/docs/linux/man/1-mktemp/">mktemp</a>(1) instead. </p>
 </dd>
<dt><code>-</code></dt>
<dd> <p> The concatenation of the current single letter options (see the <code>set</code> command below for a list of options). </p>
 </dd>
<dt><code>?</code></dt>
<dd> <p> The exit status of the last non-asynchronous command executed. If the last command was killed by a signal, <code>$?</code> is set to 128 plus the signal number. </p>
 </dd>
<dt><code>0</code></dt>
<dd> <p> The name of the shell, determined as follows: the first argument to if it was invoked with the -<code>c</code> option and arguments were given; otherwise the <i>file</i> argument, if it was supplied; or else the basename the shell was invoked with (i.e. <code>argv[0] )</code> <code>$0</code> is also set to the name of the current script or the name of the current function, if it was defined with the <code>function</code> keyword (i.e. a Korn shell style function). </p>
 </dd>
<dt><code>1 .. 9</code></dt>
<dd> <p> The first nine positional parameters that were supplied to the shell, function, or script sourced using the `.&#8216; built-in. Further positional parameters may be accessed using ${ <i>number </i><code>}</code> </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> All positional parameters (except 0), i.e. $1, $2, $3, ... <br/>
 If used outside of double quotes, parameters are separate words (which are subjected to word splitting); if used within double quotes, parameters are separated by the first character of the <code>IFS</code> parameter (or the empty string if <code>IFS</code> is <code>NULL )</code> </p>
 </dd>
<dt><code>@</code></dt>
<dd> <p> Same as <code>$*</code> unless it is used inside double quotes, in which case a separate word is generated for each positional parameter. If there are no positional parameters, no word is generated. <code>$@</code> can be used to access arguments, verbatim, without losing <code>NULL</code> arguments or splitting arguments with spaces. </p>
 </dd></dl>
<p> The following parameters are set and/or used by the shell: </p>
<dl>
<dt><code>_</code></dt>
<dd> <p> (underscore) When an external command is executed by the shell, this parameter is set in the environment of the new process to the path of the executed command. In interactive use, this parameter is also set in the parent shell to the last word of the previous command. </p>
 </dd>
<dt><code>BASHPID</code></dt>
<dd> <p> The PID of the shell or subshell. </p>
 </dd>
<dt><code>CDPATH</code></dt>
<dd> <p> Search path for the <code>cd</code> built-in command. It works the same way as <code>PATH</code> for those directories not beginning with `/&#8216; in <code>cd</code> commands. Note that if <code>CDPATH</code> is set and does not contain `.&#8216; or contains an empty path, the current directory is not searched. Also, the <code>cd</code> built-in command will display the resulting directory when a match is found in any search path other than the empty path. </p>
 </dd>
<dt><code>COLUMNS</code></dt>
<dd> <p> Set to the number of columns on the terminal or window. Always set, defaults to 80, unless the value as reported by <a href="/docs/linux/man/1-stty/">stty</a>(1) is non-zero and sane enough (minimum is 12x3); similar for <code>LINES</code> This parameter is used by the interactive line editing modes, and by the <code>select</code> <code>set -o</code> and <code>kill -l</code> commands to format information columns. Importing from the environment or unsetting this parameter removes the binding to the actual terminal size in favour of the provided value. </p>
 </dd>
<dt><code>ENV</code></dt>
<dd> <p> If this parameter is found to be set after any profile files are executed, the expanded value is used as a shell startup file. It typically contains function and alias definitions. </p>
 </dd>
<dt><code>ERRNO</code></dt>
<dd> <p> Integer value of the shell&#8217;s <i>errno</i> variable. It indicates the reason the last system call failed. Not yet implemented. </p>
 </dd>
<dt><code>EXECSHELL</code></dt>
<dd> <p> If set, this parameter is assumed to contain the shell that is to be used to execute commands that <a href="/docs/linux/man/2-execve/">execve</a>(2) fails to execute and which do not start with a ``#! <i>shell</i> &#8216;&#8216; sequence. </p>
 </dd>
<dt><code>FCEDIT</code></dt>
<dd> <p> The editor used by the <code>fc</code> command (see below). </p>
 </dd>
<dt><code>FPATH</code></dt>
<dd> <p> Like <code>PATH</code> but used when an undefined function is executed to locate the file defining the function. It is also searched when a command can&#8217;t be found using <code>PATH</code> See Sx Functions below for more information. </p>
 </dd>
<dt><code>HISTFILE</code></dt>
<dd> <p> The name of the file used to store command history. When assigned to, history is loaded from the specified file. Also, several invocations of the shell will share history if their <code>HISTFILE</code> parameters all point to the same file. </p>
<p> <code>Note</code> If <code>HISTFILE</code> isn&#8217;t set, no history file is used. This is different from AT&amp;T System <code>ksh</code> </p>
 </dd>
<dt><code>HISTSIZE</code></dt>
<dd> <p> The number of commands normally stored for history. The default is 2047. </p>
 </dd>
<dt><code>HOME</code></dt>
<dd> <p> The default directory for the <code>cd</code> command and the value substituted for an unqualified <code>~</code> (see Sx Tilde expansion below). </p>
 </dd>
<dt><code>IFS</code></dt>
<dd> <p> Internal field separator, used during substitution and by the <code>read</code> command, to split values into distinct arguments; normally set to space, tab, and newline. See Sx Substitution above for details. </p>
<p> <code>Note</code> This parameter is not imported from the environment when the shell is started. </p>
 </dd>
<dt><code>KSHEGID</code></dt>
<dd> <p> The effective group id of the shell. </p>
 </dd>
<dt><code>KSHGID</code></dt>
<dd> <p> The real group id of the shell. </p>
 </dd>
<dt><code>KSHUID</code></dt>
<dd> <p> The real user id of the shell. </p>
 </dd>
<dt><code>KSH_VERSION</code></dt>
<dd> <p> The name and version of the shell (read-only). See also the version commands in Sx Emacs editing mode and Sx Vi editing mode sections, below. </p>
 </dd>
<dt><code>LINENO</code></dt>
<dd> <p> The line number of the function or shell script that is currently being executed. </p>
 </dd>
<dt><code>LINES</code></dt>
<dd> <p> Set to the number of lines on the terminal or window. Always set, defaults to 24. See <code>COLUMNS</code> </p>
 </dd>
<dt><code>EPOCHREALTIME</code></dt>
<dd> <p> Time since the epoch, as returned by <a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a>(2), formatted as decimal <i>tv_sec</i> followed by a dot (`.&#8216; ) and <i>tv_usec</i> padded to exactly six decimal digits. </p>
 </dd>
<dt><code>OLDPWD</code></dt>
<dd> <p> The previous working directory. Unset if <code>cd</code> has not successfully changed directories since the shell started, or if the shell doesn&#8217;t know where it is. </p>
 </dd>
<dt><code>OPTARG</code></dt>
<dd> <p> When using <code>getopts</code> it contains the argument for a parsed option, if it requires one. </p>
 </dd>
<dt><code>OPTIND</code></dt>
<dd> <p> The index of the next argument to be processed when using <code>getopts</code> Assigning 1 to this parameter causes <code>getopts</code> to process arguments from the beginning the next time it is invoked. </p>
 </dd>
<dt><code>PATH</code></dt>
<dd> <p> A colon separated list of directories that are searched when looking for commands and files sourced using the `.&#8216; command (see below). An empty string resulting from a leading or trailing colon, or two adjacent colons, is treated as a `.&#8216; (the current directory). </p>
 </dd>
<dt><code>PGRP</code></dt>
<dd> <p> The process ID of the shell&#8217;s process group leader. </p>
 </dd>
<dt><code>PIPESTATUS</code></dt>
<dd> <p> An array containing the errorlevel (exit status) codes, one by one, of the last pipeline run in the foreground. </p>
 </dd>
<dt><code>PPID</code></dt>
<dd> <p> The process ID of the shell&#8217;s parent. </p>
 </dd>
<dt><code>PS1</code></dt>
<dd> <p> The primary prompt for interactive shells. Parameter, command, and arithmetic substitutions are performed, and `!&#8216; is replaced with the current command number (see the <code>fc</code> command below). A literal `!&#8216; can be put in the prompt by placing `!!&#8216; in <code>PS1</code> </p>
<p> The default prompt is `$&nbsp;<wbr>&#8216; for non-root users, `#&nbsp;<wbr>&#8216; for root. If is invoked by root and <code>PS1</code> does not contain a `#&#8216; character, the default value will be used even if <code>PS1</code> already exists in the environment. </p>
<p> The distribution comes with a sample dot.mkshrc containing a sophisticated example, but you might like the following one (note that ${HOSTNAME:=$(hostname)} and the root-vs-user distinguishing clause are (in this example) executed at <code>PS1</code> assignment time, while the $USER and $PWD are escaped and thus will be evaluated each time a prompt is displayed): </p>
<pre><code>PS1='${USER:=$(id -un)}'&quot;@${HOSTNAME:=$(hostname)}:\$PWD $(
        if (( USER_ID )); then print \$; else print \#; fi) &quot;
</code></pre>
<p> Note that since the command-line editors try to figure out how long the prompt is (so they know how far it is to the edge of the screen), escape codes in the prompt tend to mess things up. You can tell the shell not to count certain sequences (such as escape codes) by prefixing your prompt with a character (such as Ctrl-A) followed by a carriage return and then delimiting the escape codes with this character. Any occurences of that character in the prompt are not printed. By the way, don&#8217;t blame me for this hack; it&#8217;s derived from the original ksh88(1), which did print the delimiter character so you were out of luck if you did not have any non-printing characters. </p>
<p> Since Backslashes and other special characters may be interpreted by the shell, to set <code>PS1</code> either escape the backslash itself, or use double quotes. The latter is more practical. This is a more complex example, avoiding to directly enter special characters (for example with <code>^V</code> in the emacs editing mode), which embeds the current working directory, in reverse video (colour would work, too) in the prompt string: </p>
<blockquote><pre><code>x=$(print \\001)
PS1=&quot;$x$(print \\r)$x$(tput smso)$x\$PWD$x$(tput rmso)$x&gt; &quot;
</code></pre>
</blockquote>
<p> Due to a strong suggestion from David G. Korn, now also supports the following form: </p>
<blockquote><pre><code>PS1=$'\1\r\1\e[7m\1$PWD\1\e[0m\1&gt; '
</code></pre>
</blockquote>
 </dd>
<dt><code>PS2</code></dt>
<dd> <p> Secondary prompt string, by default `&gt;&nbsp;<wbr>&#8216; used when more input is needed to complete a command. </p>
 </dd>
<dt><code>PS3</code></dt>
<dd> <p> Prompt used by the <code>select</code> statement when reading a menu selection. The default is `#?&nbsp;<wbr>&#8216; </p>
 </dd>
<dt><code>PS4</code></dt>
<dd> <p> Used to prefix commands that are printed during execution tracing (see the <code>set -x</code> command below). Parameter, command, and arithmetic substitutions are performed before it is printed. The default is `+&nbsp;<wbr>&#8216; You may want to set it to `[$EPOCHREALTIME]&nbsp;<wbr>&#8216; instead, to include timestamps. </p>
 </dd>
<dt><code>PWD</code></dt>
<dd> <p> The current working directory. May be unset or <code>NULL</code> if the shell doesn&#8217;t know where it is. </p>
 </dd>
<dt><code>RANDOM</code></dt>
<dd> <p> Each time <code>RANDOM</code> is referenced, it is assigned a number between 0 and 32767 from a Linear Congruential PRNG first. </p>
 </dd>
<dt><code>REPLY</code></dt>
<dd> <p> Default parameter for the <code>read</code> command if no names are given. Also used in <code>select</code> loops to store the value that is read from standard input. </p>
 </dd>
<dt><code>SECONDS</code></dt>
<dd> <p> The number of seconds since the shell started or, if the parameter has been assigned an integer value, the number of seconds since the assignment plus the value that was assigned. </p>
 </dd>
<dt><code>TMOUT</code></dt>
<dd> <p> If set to a positive integer in an interactive shell, it specifies the maximum number of seconds the shell will wait for input after printing the primary prompt (<code>PS1</code> ) If the time is exceeded, the shell exits. </p>
 </dd>
<dt><code>TMPDIR</code></dt>
<dd> <p> The directory temporary shell files are created in. If this parameter is not set, or does not contain the absolute path of a writable directory, temporary files are created in /tmp </p>
 </dd>
<dt><code>USER_ID</code></dt>
<dd> <p> The effective user id of the shell. </p>
 </dd></dl>
<h3>Tilde expansion</h3>
<p> Tilde expansion which is done in parallel with parameter substitution, is done on words starting with an unquoted `~&#8216; The characters following the tilde, up to the first `/&#8216; , if any, are assumed to be a login name. If the login name is empty, `+&#8216; , or `-&#8216; , the value of the <code>HOME</code> <code>PWD</code> or <code>OLDPWD</code> parameter is substituted, respectively. Otherwise, the password file is searched for the login name, and the tilde expression is substituted with the user&#8217;s home directory. If the login name is not found in the password file or if any quoting or parameter substitution occurs in the login name, no substitution is performed. </p>
<p> In parameter assignments (such as those preceding a simple-command or those occurring in the arguments of <code>alias</code> <code>export</code> <code>global</code> <code>readonly</code> and <code>typeset )</code> tilde expansion is done after any assignment (i.e. after the equals sign) or after an unquoted colon (`:&#8216; ) login names are also delimited by colons. </p>
<p> The home directory of previously expanded login names are cached and re-used. The <code>alias -d</code> command may be used to list, change, and add to this cache (e.g. <code>alias -d fac=/usr/local/facilities; cd ~fac/bin )</code>  </p>
<h3>Brace expansion (alteration)</h3>
<p> Brace expressions take the following form: </p>
<blockquote><pre><code>
 prefix  {  str1  ,..., 
 strN  }  suffix 
</code></pre>
</blockquote>
<p> The expressions are expanded to <i>N</i> words, each of which is the concatenation of <i>prefix</i> <i>str </i><code>i</code> and <i>suffix</i> (e.g. ``a{c,b{X,Y},d}e&#8217;&#8216; expands to four words: ``ace&#8217;&#8216; ``abXe , &#8216;&#8216; ``abYe , &#8216;&#8216; and ``ade )&#8216;&#8216; As noted in the example, brace expressions can be nested and the resulting words are not sorted. Brace expressions must contain an unquoted comma (`,&#8216; ) for expansion to occur (e.g. <code>{}</code> and <code>{foo}</code> are not expanded). Brace expansion is carried out after parameter substitution and before file name generation.  </p>
<h3>File name patterns</h3>
<p> A file name pattern is a word containing one or more unquoted `?&#8216; , `*&#8216; , `+&#8216; , `@&#8216; , or `!&#8216; characters or ``[..]&#8216;&#8216; sequences. Once brace expansion has been performed, the shell replaces file name patterns with the sorted names of all the files that match the pattern (if no files match, the word is left unchanged). The pattern elements have the following meaning: </p>
<dl>
<dt><code>?</code></dt>
<dd> <p> Matches any single character. </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> Matches any sequence of octets. </p>
 </dd>
<dt><code>[..]</code></dt>
<dd> <p> Matches any of the octets inside the brackets. Ranges of octets can be specified by separating two octets by a `-&#8216; (e.g. ``[a0-9]&#8216;&#8216; matches the letter `a&#8217; or any digit). In order to represent itself, a `-&#8216; must either be quoted or the first or last octet in the octet list. Similarly, a `]&#8216; must be quoted or the first octet in the list if it is to represent itself instead of the end of the list. Also, a `!&#8216; appearing at the start of the list has special meaning (see below), so to represent itself it must be quoted or appear later in the list. </p>
 </dd>
<dt><code>[!..]</code></dt>
<dd> <p> Like [..], except it matches any octet not inside the brackets. </p>
 </dd>
<dt><code>*( </code><i>pattern| </i><code>...| </code><i>pattern</i></dt>
<dd> <p> Matches any string of octets that matches zero or more occurrences of the specified patterns. Example: The pattern <code>*(foo|bar)</code> matches the strings ``,&#8216;&#8216; ``foo&#8217;&#8216; ``bar&#8217;&#8216; ``foobarfoo&#8217;&#8216; etc. </p>
 </dd>
<dt><code>+( </code><i>pattern| </i><code>...| </code><i>pattern</i></dt>
<dd> <p> Matches any string of octets that matches one or more occurrences of the specified patterns. Example: The pattern <code>+(foo|bar)</code> matches the strings ``foo&#8217;&#8216; ``bar&#8217;&#8216; ``foobar&#8217;&#8216; etc. </p>
 </dd>
<dt><code>?( </code><i>pattern| </i><code>...| </code><i>pattern</i></dt>
<dd> <p> Matches the empty string or a string that matches one of the specified patterns. Example: The pattern <code>?(foo|bar)</code> only matches the strings ``,&#8216;&#8216; ``foo&#8217;&#8216; and ``bar&#8217;&#8216; </p>
 </dd>
<dt><code>@( </code><i>pattern| </i><code>...| </code><i>pattern</i></dt>
<dd> <p> Matches a string that matches one of the specified patterns. Example: The pattern <code>@(foo|bar)</code> only matches the strings ``foo&#8217;&#8216; and ``bar&#8217;&#8216; </p>
 </dd>
<dt><code>!( </code><i>pattern| </i><code>...| </code><i>pattern</i></dt>
<dd> <p> Matches any string that does not match one of the specified patterns. Examples: The pattern <code>!(foo|bar)</code> matches all strings except ``foo&#8217;&#8216; and ``bar&#8217;&#8216; the pattern <code>!(*)</code> matches no strings; the pattern <code>!(?)*</code> matches all strings (think about it). </p>
 </dd></dl>
<p> Note that complicated globbing, especially with alternatives, is slow; using separate comparisons may (or may not) be faster. </p>
<p> Note that <code>mksh</code> Po and Nm pdksh Pc never matches `.&#8216; and `..&#8216; but AT&amp;T System <code>ksh</code> Bourne <code>sh</code> and GNU <code>bash</code> do. </p>
<p> Note that none of the above pattern elements match either a period (`.&#8216; ) at the start of a file name or a slash (`/&#8216; ) even if they are explicitly used in a [..] sequence; also, the names `.&#8216; and `..&#8216; are never matched, even by the pattern `.*&#8216; </p>
<p> If the <code>markdirs</code> option is set, any directories that result from file name generation are marked with a trailing `/&#8216;  </p>
<h3>Input/output redirection</h3>
<p> When a command is executed, its standard input, standard output, and standard error (file descriptors 0, 1, and 2, respectively) are normally inherited from the shell. Three exceptions to this are commands in pipelines, for which standard input and/or standard output are those set up by the pipeline, asynchronous commands created when job control is disabled, for which standard input is initially set to be from /dev/null and commands for which any of the following redirections have been specified: </p>
<dl>
<dt><code>&gt; </code><i>file</i></dt>
<dd> <p> Standard output is redirected to <i>file</i> If <i>file</i> does not exist, it is created; if it does exist, is a regular file, and the <code>noclobber</code> option is set, an error occurs; otherwise, the file is truncated. Note that this means the command <code>cmd &lt;foo &gt;foo</code> will open <i>foo</i> for reading and then truncate it when it opens it for writing, before <i>cmd</i> gets a chance to actually read <i>foo</i> </p>
 </dd>
<dt><code>&gt;| </code><i>file</i></dt>
<dd> <p> Same as <code>&gt;</code> except the file is truncated, even if the <code>noclobber</code> option is set. </p>
 </dd>
<dt><code>&gt;&gt; </code><i>file</i></dt>
<dd> <p> Same as <code>&gt;</code> except if <i>file</i> exists it is appended to instead of being truncated. Also, the file is opened in append mode, so writes always go to the end of the file (see <a href="/docs/linux/man/2-open/">open</a>(2)). </p>
 </dd>
<dt><code>&lt; </code><i>file</i></dt>
<dd> <p> Standard input is redirected from <i>file</i> which is opened for reading. </p>
 </dd>
<dt><code>&lt;&gt; </code><i>file</i></dt>
<dd> <p> Same as <code>&lt;</code> except the file is opened for reading and writing. </p>
 </dd>
<dt><code>&lt;&lt; </code><i>marker</i></dt>
<dd> <p> After reading the command line containing this kind of redirection (called a ``here document )&#8216;&#8216; the shell copies lines from the command source into a temporary file until a line matching <i>marker</i> is read. When the command is executed, standard input is redirected from the temporary file. If <i>marker</i> contains no quoted characters, the contents of the temporary file are processed as if enclosed in double quotes each time the command is executed, so parameter, command, and arithmetic substitutions are performed, along with backslash (`\&#8216; ) escapes for `$&#8216; , ``&#8216; , `\&#8216; , and `\newline&#8217; , but not for `&#8216; If multiple here documents are used on the same command line, they are saved in order. </p>
<p> If no <i>marker</i> is given, the here document ends at the next <code>&lt;&lt;</code> and substitution will be performed. If <i>marker</i> is only a set of either single ``&#8216;&#8216;&#8216;&#8216; or double `&#8216; quotes with nothing in between, the here document ends at the next empty line and substitution will not be performed. </p>
 </dd>
<dt><code>&lt;&lt;- </code><i>marker</i></dt>
<dd> <p> Same as <code>&lt;&lt;</code> except leading tabs are stripped from lines in the here document. </p>
 </dd>
<dt><code>&lt;&lt;&lt; </code><i>word</i></dt>
<dd> <p> Same as <code>&lt;&lt;</code> except that <i>word</i> <i>is</i> the here document. This is called a here string. </p>
 </dd>
<dt><code>&lt;&amp; </code><i>fd</i></dt>
<dd> <p> Standard input is duplicated from file descriptor <i>fd</i> <i>fd</i> can be a number, indicating the number of an existing file descriptor; the letter `p&#8217; , indicating the file descriptor associated with the output of the current co-process; or the character `-&#8216; , indicating standard input is to be closed. Note that <i>fd</i> is limited to a single digit in most shell implementations. </p>
 </dd>
<dt><code>&gt;&amp; </code><i>fd</i></dt>
<dd> <p> Same as <code>&lt;&amp;</code> except the operation is done on standard output. </p>
 </dd>
<dt><code>&amp;&gt; </code><i>file</i></dt>
<dd> <p> Same as <code>&gt; </code><i>file 2&gt;&amp;1</i> This is a GNU <code>bash</code> extension supported by which also supports the preceding explicit fd number, for example, <code>3&amp;&gt; </code><i>file</i> is the same as <code>3&gt; </code><i>file 2&gt;&amp;3</i> in but a syntax error in GNU <code>bash</code> Setting the -<code>o </code><i>posix</i> or -<code>o </code><i>sh</i> shell options disable parsing of this redirection; it&#8217;s a compatibility feature to legacy scripts, to not be used when writing new shell code. </p>
 </dd>
<dt><code>&amp;&gt;| </code><i>file</i><code>&amp;&gt;&gt; </code><i>file</i><code>&amp;&gt;&amp; </code><i>fd</i></dt>
<dd>  </dd>
<dd> <p> Same as <code>&gt;| </code><i>file</i> <code>&gt;&gt; </code><i>file</i> or <code>&gt;&amp; </code><i>fd</i> followed by <code>2&gt;&amp;1</code> as above. These are extensions. </p>
 </dd></dl>
<p> In any of the above redirections, the file descriptor that is redirected (i.e. standard input or standard output) can be explicitly given by preceding the redirection with a number (portably, only a single digit). Parameter, command, and arithmetic substitutions, tilde substitutions, and (if the shell is interactive) file name generation are all performed on the <i>file</i> <i>marker</i> and <i>fd</i> arguments of redirections. Note, however, that the results of any file name generation are only used if a single file is matched; if multiple files match, the word with the expanded file name generation characters is used. Note that in restricted shells, redirections which can create files cannot be used. </p>
<p> For simple-commands, redirections may appear anywhere in the command; for compound-commands Po <code>if</code> statements, etc. Pc , any redirections must appear at the end. Redirections are processed after pipelines are created and in the order they are given, so the following will print an error with a line number prepended to it: </p>
<p> File descriptors created by input/output redirections are private to the Korn shell, but passed to sub-processes if -<code>o posix</code> or -<code>o sh</code> is set.  </p>
<h3>Arithmetic expressions</h3>
<p> Integer arithmetic expressions can be used with the <code>let</code> command, inside $((..)) expressions, inside array references (e.g. <i>name </i><code>Bq </code><i>expr</i> as numeric arguments to the <code>test</code> command, and as the value of an assignment to an integer parameter. </p>
<p> Expressions are calculated using signed arithmetic and the Vt mksh_ari_t type (a 32-bit signed integer), unless they begin with a sole `#&#8216; character, in which case they use Vt mksh_uari_t Po a 32-bit unsigned integer Pc . </p>
<p> Expressions may contain alpha-numeric parameter identifiers, array references, and integer constants and may be combined with the following C operators (listed and grouped in increasing order of precedence): </p>
<p> Unary operators: </p>
<blockquote><pre><code>+ - ! ~ ++ --
</code></pre>
</blockquote>
<p> Binary operators: </p>
<blockquote><pre><code>,
= += -= *= /= %= &lt;&lt;&lt;= &gt;&gt;&gt;= &lt;&lt;= &gt;&gt;= &amp;= ^= |=
||
&amp;&amp;
|
^
&amp;
== !=
&lt; &lt;= &gt; &gt;=
&lt;&lt;&lt; &gt;&gt;&gt; &lt;&lt; &gt;&gt;
+ -
* / %
</code></pre>
</blockquote>
<p> Ternary operators: </p>
<blockquote><pre><code>?: (precedence is immediately higher than assignment)
</code></pre>
</blockquote>
<p> Grouping operators: </p>
<blockquote><pre><code>( )
</code></pre>
</blockquote>
<p> Integer constants and expressions are calculated using an exactly 32-bit wide, signed or unsigned, type with silent wraparound on integer overflow. Integer constants may be specified with arbitrary bases using the notation <i>base </i><code># </code><i>number</i> where <i>base</i> is a decimal integer specifying the base, and <i>number</i> is a number in the specified base. Additionally, base-16 integers may be specified by prefixing them with `0x&#8217; (case-insensitive) in all forms of arithmetic expressions, except as numeric arguments to the <code>test</code> built-in command. Prefixing numbers with a sole digit zero (`0&#8217; ) leads to the shell interpreting it as base-8 integer in <code>posix</code> mode <i>only</i> historically, (pd)ksh has never done so either anyway, and it&#8217;s unsafe to do that, but POSIX demands it nowadays. As a special <code>mksh</code> extension, numbers to the base of one are treated as either (8-bit transparent) ASCII or Unicode codepoints, depending on the shell&#8217;s <code>utf8-mode</code> flag (current setting). The AT&amp;T System <code>ksh93</code> syntax of ``&#8216;x&#8217;&#8216;&#8216; instead of ``1#x&#8217;&#8216; is also supported. Note that NUL bytes (integral value of zero) cannot be used. An unset or empty parameter evaluates to 0 in integer context. In Unicode mode, raw octets are mapped into the range EF80..EFFF as in OPTU-8, which is in the PUA and has been assigned by CSUR for this use. If more than one octet in ASCII mode, or a sequence of more than one octet not forming a valid and minimal CESU-8 sequence is passed, the behaviour is undefined (usually, the shell aborts with a parse error, but rarely, it succeeds, e.g. on the sequence C2 20). That&#8217;s why you should always use ASCII mode unless you know that the input is well-formed UTF-8 in the range of 0000..FFFD. </p>
<p> The operators are evaluated as follows: </p>
<dl>
<dt><code>unary</code></dt>
<dd> <p> Result is the argument (included for completeness). </p>
 </dd>
<dt><code>unary -</code></dt>
<dd> <p> Negation. </p>
 </dd>
<dt><code>!</code></dt>
<dd> <p> Logical NOT; the result is 1 if argument is zero, 0 if not. </p>
 </dd>
<dt><code>~</code></dt>
<dd> <p> Arithmetic (bit-wise) NOT. </p>
 </dd>
<dt><code>++</code></dt>
<dd> <p> Increment; must be applied to a parameter (not a literal or other expression). The parameter is incremented by 1. When used as a prefix operator, the result is the incremented value of the parameter; when used as a postfix operator, the result is the original value of the parameter. </p>
 </dd>
<dt><code>--</code></dt>
<dd> <p> Similar to <code>++</code> except the parameter is decremented by 1. </p>
 </dd>
<dt><code>,</code></dt>
<dd> <p> Separates two arithmetic expressions; the left-hand side is evaluated first, then the right. The result is the value of the expression on the right-hand side. </p>
 </dd>
<dt><code>=</code></dt>
<dd> <p> Assignment; the variable on the left is set to the value on the right. </p>
 </dd>
<dt><code>+= -= *= /= %= &lt;&lt;&lt;= &gt;&gt;&gt;=</code><code>&lt;&lt;= &gt;&gt;= &amp;= ^= |=</code></dt>
<dd>  </dd>
<dd> <p> Assignment operators. Ao Ar var Ac Xo Aq Ar op <code>= Aq </code><i>expr</i> is the same as Ao Ar var Ac Xo <code>= Aq </code><i>var</i> Aq Ar op Aq Ar expr , with any operator precedence in Aq Ar expr preserved. For example, ``var1 *= 5 + 3&#8217;&#8216; is the same as specifying ``var1 = var1 * (5 + 3)&#8216;&#8216; </p>
 </dd>
<dt><code>||</code></dt>
<dd> <p> Logical OR; the result is 1 if either argument is non-zero, 0 if not. The right argument is evaluated only if the left argument is zero. </p>
 </dd>
<dt><code>&amp;&amp;</code></dt>
<dd> <p> Logical AND; the result is 1 if both arguments are non-zero, 0 if not. The right argument is evaluated only if the left argument is non-zero. </p>
 </dd>
<dt><code>|</code></dt>
<dd> <p> Arithmetic (bit-wise) OR. </p>
 </dd>
<dt><code>^</code></dt>
<dd> <p> Arithmetic (bit-wise) XOR (exclusive-OR). </p>
 </dd>
<dt><code>&amp;</code></dt>
<dd> <p> Arithmetic (bit-wise) AND. </p>
 </dd>
<dt><code>==</code></dt>
<dd> <p> Equal; the result is 1 if both arguments are equal, 0 if not. </p>
 </dd>
<dt><code>!=</code></dt>
<dd> <p> Not equal; the result is 0 if both arguments are equal, 1 if not. </p>
 </dd>
<dt><code>&lt;</code></dt>
<dd> <p> Less than; the result is 1 if the left argument is less than the right, 0 if not. </p>
 </dd>
<dt><code>&lt;= &gt; &gt;=</code></dt>
<dd> <p> Less than or equal, greater than or equal, greater than. See <code>&lt;</code> </p>
 </dd>
<dt><code>&lt;&lt;&lt; &gt;&gt;&gt;</code></dt>
<dd> <p> Rotate left (right); the result is similar to shift (see <code>&lt;&lt;</code> except that the bits shifted out at one end are shifted in at the other end, instead of zero or sign bits. </p>
 </dd>
<dt><code>&lt;&lt; &gt;&gt;</code></dt>
<dd> <p> Shift left (right); the result is the left argument with its bits shifted left (right) by the amount given in the right argument. </p>
 </dd>
<dt><code>+ - *</code></dt>
<dd> <p> Addition, subtraction, multiplication, and division. </p>
 </dd>
<dt><code>%</code></dt>
<dd> <p> Remainder; the result is the remainder of the division of the left argument by the right. </p>
 </dd>
<dt> Aq Ar arg1 ? Aq Ar arg2 : Aq Ar arg3 </dt>
<dd>  </dd>
<dd> <p> If Aq Ar arg1 is non-zero, the result is Aq Ar arg2 ; otherwise the result is Aq Ar arg3 . The non-result argument is not evaluated. </p>
 </dd></dl>
<h3>Co-processes</h3>
<p> A co-process (which is a pipeline created with the `|&amp;&#8216; operator) is an asynchronous process that the shell can both write to (using <code>print -p</code> and read from (using <code>read -p )</code> The input and output of the co-process can also be manipulated using <code>&gt;&amp;p</code> and <code>&lt;&amp;p</code> redirections, respectively. Once a co-process has been started, another can&#8217;t be started until the co-process exits, or until the co-process&#8217;s input has been redirected using an <code>exec </code><i>n </i><code>&gt;&amp;p</code> redirection. If a co-process&#8217;s input is redirected in this way, the next co-process to be started will share the output with the first co-process, unless the output of the initial co-process has been redirected using an <code>exec </code><i>n </i><code>&lt;&amp;p</code> redirection. </p>
<p> Some notes concerning co-processes: </p>
<ul>
<li> <p> The only way to close the co-process&#8217;s input (so the co-process reads an end-of-file) is to redirect the input to a numbered file descriptor and then close that file descriptor: <code>exec 3&gt;&amp;p; exec 3&gt;&amp;-</code>  </li>
<li>  In order for co-processes to share a common output, the shell must keep the write portion of the output pipe open. This means that end-of-file will not be detected until all co-processes sharing the co-process&#8217;s output have exited (when they all exit, the shell closes its copy of the pipe). This can be avoided by redirecting the output to a numbered file descriptor (as this also causes the shell to close its copy). Note that this behaviour is slightly different from the original Korn shell which closes its copy of the write portion of the co-process output when the most recently started co-process (instead of when all sharing co-processes) exits.  </li>
<li>  <code>print -p</code> will ignore <code>SIGPIPE</code> signals during writes if the signal is not being trapped or ignored; the same is true if the co-process input has been duplicated to another file descriptor and <code>print -u </code><i>n</i> is used.  </li>
</ul>
 </p>
<h3>Functions</h3>
<p> Functions are defined using either Korn shell <code>function </code><i>function-name</i> syntax or the Bourne/POSIX shell <i>function-name </i><code>()</code> syntax (see below for the difference between the two forms). Functions are like <code>.-scripts</code> (i.e. scripts sourced using the `.&#8216; built-in) in that they are executed in the current environment. However, unlike <code>.-scripts</code> shell arguments (i.e. positional parameters $1, $2, etc.) are never visible inside them. When the shell is determining the location of a command, functions are searched after special built-in commands, before builtins and the <code>PATH</code> is searched. </p>
<p> An existing function may be deleted using <code>unset -f </code><i>function-name</i> A list of functions can be obtained using <code>typeset +f</code> and the function definitions can be listed using <code>typeset -f</code> The <code>autoload</code> command (which is an alias for <code>typeset -fu</code> may be used to create undefined functions: when an undefined function is executed, the shell searches the path specified in the <code>FPATH</code> parameter for a file with the same name as the function which, if found, is read and executed. If after executing the file the named function is found to be defined, the function is executed; otherwise, the normal command search is continued (i.e. the shell searches the regular built-in command table and <code>PATH )</code> Note that if a command is not found using <code>PATH</code> an attempt is made to autoload a function using <code>FPATH</code> (this is an undocumented feature of the original Korn shell). </p>
<p> Functions can have two attributes, ``trace&#8217;&#8216; and ``export&#8217;&#8216; which can be set with <code>typeset -ft</code> and <code>typeset -fx</code> respectively. When a traced function is executed, the shell&#8217;s <code>xtrace</code> option is turned on for the function&#8217;s duration. The ``export&#8217;&#8216; attribute of functions is currently not used. In the original Korn shell, exported functions are visible to shell scripts that are executed. </p>
<p> Since functions are executed in the current shell environment, parameter assignments made inside functions are visible after the function completes. If this is not the desired effect, the <code>typeset</code> command can be used inside a function to create a local parameter. Note that AT&amp;T System <code>ksh93</code> uses static scoping (one global scope, one local scope per function) and allows local variables only on Korn style functions, whereas <code>mksh</code> uses dynamic scoping (nested scopes of varying locality). Note that special parameters (e.g. <code>$$ , $!</code> can&#8217;t be scoped in this way. </p>
<p> The exit status of a function is that of the last command executed in the function. A function can be made to finish immediately using the <code>return</code> command; this may also be used to explicitly specify the exit status. </p>
<p> Functions defined with the <code>function</code> reserved word are treated differently in the following ways from functions defined with the <code>()</code> notation: </p>
<ul>
<li> <p> The $0 parameter is set to the name of the function (Bourne-style functions leave $0 untouched).  </li>
<li>  Parameter assignments preceding function calls are not kept in the shell environment (executing Bourne-style functions will keep assignments).  </li>
<li>  <code>OPTIND</code> is saved/reset and restored on entry and exit from the function so <code>getopts</code> can be used properly both inside and outside the function (Bourne-style functions leave <code>OPTIND</code> untouched, so using <code>getopts</code> inside a function interferes with using <code>getopts</code> outside the function).  </li>
<li>  Bourne-style function definitions take precedence over alias dereferences and remove alias definitions upon encounter, while aliases take precedence over Korn-style functions.  </li>
</ul>
 </p>
<p> In the future, the following differences may also be added: </p>
<ul>
<li> <p> A separate trap/signal environment will be used during the execution of functions. This will mean that traps set inside a function will not affect the shell&#8217;s traps and signals that are not ignored in the shell (but may be trapped) will have their default effect in a function.  </li>
<li>  The EXIT trap, if set in a function, will be executed after the function returns.  </li>
</ul>
 </p>
<h3>Command execution</h3>
<p> After evaluation of command-line arguments, redirections, and parameter assignments, the type of command is determined: a special built-in command, a function, a normal builtin, or the name of a file to execute found using the <code>PATH</code> parameter. The checks are made in the above order. Special built-in commands differ from other commands in that the <code>PATH</code> parameter is not used to find them, an error during their execution can cause a non-interactive shell to exit, and parameter assignments that are specified before the command are kept after the command completes. Regular built-in commands are different only in that the <code>PATH</code> parameter is not used to find them. </p>
<p> The original <code>ksh</code> and POSIX differ somewhat in which commands are considered special or regular. </p>
<p> POSIX special built-in utilities: </p>
<p> <code>. , : , break , continue</code> <code>eval , exec , exit , export</code> <code>readonly , return , set , shift</code> <code>times , trap , unset</code> </p>
<p> Additional commands keeping assignments: </p>
<p> <code>builtin , global , typeset , wait</code> </p>
<p> Builtins that are not special: </p>
<p> <code>[ , alias , bg , bind</code> <code>cat , cd , command , echo</code> <code>false , fc , fg , getopts</code> <code>jobs , kill , let , mknod</code> <code>print , pwd , read , realpath</code> <code>rename , sleep , test , true</code> <code>ulimit , umask , unalias , whence</code> </p>
<p> Once the type of command has been determined, any command-line parameter assignments are performed and exported for the duration of the command. </p>
<p> The following describes the special and regular built-in commands: </p>
<dl>
<dt><code>. </code><i>file </i>[<i>arg ...</i> ] </dt>
<dd> <p> This is called the ``dot&#8217;&#8216; command. Execute the commands in <i>file</i> in the current environment. The file is searched for in the directories of <code>PATH</code> If arguments are given, the positional parameters may be used to access them while <i>file</i> is being executed. If no arguments are given, the positional parameters are those of the environment the command is used in. </p>
 </dd>
<dt><code>: </code>[<i>...</i> ] </dt>
<dd> <p> The null command. Exit status is set to zero. </p>
 </dd>
<dt><code>[ </code><i>expression </i><code>]</code></dt>
<dd> <p> See <code>test</code> </p>
 </dd>
<dt><code> alias</code> [-<code>d | t </code>[-<code>r |</code>] <code>+-x </code>] [-<code>p</code> ] [<code>+</code> ] [<i>name</i> [<code>= </code><i>value</i> ] <i>... </i>] </dt>
<dd>  </dd>
<dd> <p> Without arguments, <code>alias</code> lists all aliases. For any name without a value, the existing alias is listed. Any name with a value defines an alias (see Sx Aliases above). </p>
<p> When listing aliases, one of two formats is used. Normally, aliases are listed as <i>name </i><code>= </code><i>value</i> where <i>value</i> is quoted. If options were preceded with `+&#8216; , or a lone `+&#8216; is given on the command line, only <i>name</i> is printed. </p>
<p> The -<code>d</code> option causes directory aliases which are used in tilde expansion to be listed or set (see Sx Tilde expansion above). </p>
<p> If the -<code>p</code> option is used, each alias is prefixed with the string ``alias&nbsp;<wbr>&#8216;&#8216; </p>
<p> The -<code>t</code> option indicates that tracked aliases are to be listed/set (values specified on the command line are ignored for tracked aliases). The -<code>r</code> option indicates that all tracked aliases are to be reset. </p>
<p> The -<code>x</code> option sets (<code>+x clears</code> ) the export attribute of an alias, or, if no names are given, lists the aliases with the export attribute (exporting an alias has no effect). </p>
 </dd>
<dt><code>bg </code>[<i>job ...</i> ] </dt>
<dd> <p> Resume the specified stopped job(s) in the background. If no jobs are specified, <code>%+</code> is assumed. See Sx Job control below for more information. </p>
 </dd>
<dt><code>bind </code>[-<code>l</code> ] </dt>
<dd> <p> The current bindings are listed. If the -<code>l</code> flag is given, <code>bind</code> instead lists the names of the functions to which keys may be bound. See Sx Emacs editing mode for more information. </p>
 </dd>
<dt><code> bind </code>[-<code>m</code> ] <i>string </i><code>= </code>[<i>substitute</i> ] <i>...</i></dt>
<dd>  </dd>
<dt><code> bind</code><i>string </i><code>= </code>[<i>editing-command</i> ] <i>...</i></dt>
<dd>  </dd>
<dd> <p> The specified editing command is bound to the given <i>string</i> which should consist of a control character optionally preceded by one of the two prefix characters and optionally succeded by a tilde character. Future input of the <i>string</i> will cause the editing command to be immediately invoked. If the -<code>m</code> flag is given, the specified input <i>string</i> will afterwards be immediately replaced by the given <i>substitute</i> string which may contain editing commands but not other macros. If a tilde postfix is given, a tilde trailing the one or two prefices and the control character is ignored, any other trailing character will be processed afterwards. </p>
<p> Control characters may be written using caret notation i.e. ^X represents Ctrl-X. Note that although only two prefix characters (usually ESC and ^X) are supported, some multi-character sequences can be supported. </p>
<p> The following default bindings show how the arrow keys, the home, end and delete key on a BSD wsvt25, xterm-xfree86 or GNU screen terminal are bound (of course some escape sequences won&#8217;t work out quite this nicely): </p>
<blockquote><pre><code>bind '^X'=prefix-2
bind '^[['=prefix-2
bind '^XA'=up-history
bind '^XB'=down-history
bind '^XC'=forward-char
bind '^XD'=backward-char
bind '^X1~'=beginning-of-line
bind '^X7~'=beginning-of-line
bind '^XH'=beginning-of-line
bind '^X4~'=end-of-line
bind '^X8~'=end-of-line
bind '^XF'=end-of-line
bind '^X3~'=delete-char-forward
</code></pre>
</blockquote>
 </dd>
<dt><code>break </code>[<i>level</i> ] </dt>
<dd> <p> Exit the <i>level </i><code>th</code> inner-most <code>for</code> <code>select</code> <code>until</code> or <code>while</code> loop. <i>level</i> defaults to 1. </p>
 </dd>
<dt><code>builtin</code> [-<code>-</code> ] <i>command </i>[<i>arg ...</i> ] </dt>
<dd>  </dd>
<dd> <p> Execute the built-in command <i>command</i> </p>
 </dd>
<dt><code>cat</code> [-<code>u</code> ] [<i>file ...</i> ] </dt>
<dd>  </dd>
<dd> <p> Read files sequentially, in command line order, and write them to standard output. If a <i>file</i> is a single dash (`-&#8216; ) or absent, read from standard input. Unless compiled with <code>MKSH_NO_EXTERNAL_CAT</code> if any options are given, an external <a href="/docs/linux/man/1-cat/">cat</a>(1) utility is invoked instead if called from the shell. For direct builtin calls, the <code>POSIX</code> -<code>u</code> option is supported as a no-op. </p>
 </dd>
<dt><code>cd</code> [-<code>L</code> ] [<i>dir</i> ] </dt>
<dd>  </dd>
<dt><code>cd</code> -<code>P </code>[-<code>e</code> ] [<i>dir</i> ] </dt>
<dd>  </dd>
<dt><code>chdir</code> [-<code>eLP</code> ] [<i>dir</i> ] </dt>
<dd>  </dd>
<dd> <p> Set the working directory to <i>dir</i> If the parameter <code>CDPATH</code> is set, it lists the search path for the directory containing <i>dir</i> A <code>NULL</code> path means the current directory. If <i>dir</i> is found in any component of the <code>CDPATH</code> search path other than the <code>NULL</code> path, the name of the new working directory will be written to standard output. If <i>dir</i> is missing, the home directory <code>HOME</code> is used. If <i>dir</i> is `-&#8216; , the previous working directory is used (see the <code>OLDPWD</code> parameter). </p>
<p> If the -<code>L</code> option (logical path) is used or if the <code>physical</code> option isn&#8217;t set (see the <code>set</code> command below), references to `..&#8216; in <i>dir</i> are relative to the path used to get to the directory. If the -<code>P</code> option (physical path) is used or if the <code>physical</code> option is set, `..&#8216; is relative to the filesystem directory tree. The <code>PWD</code> and <code>OLDPWD</code> parameters are updated to reflect the current and old working directory, respectively. If the -<code>e</code> option is set for physical filesystem traversal, and <code>PWD</code> could not be set, the exit code is 1; greater than 1 if an error occurred, 0 otherwise. </p>
 </dd>
<dt><code>cd</code> [-<code>eLP</code> ] <i>old new</i></dt>
<dd>  </dd>
<dt><code>chdir</code> [-<code>eLP</code> ] <i>old new</i></dt>
<dd>  </dd>
<dd> <p> The string <i>new</i> is substituted for <i>old</i> in the current directory, and the shell attempts to change to the new directory. </p>
 </dd>
<dt><code>command</code> [-<code>pVv </code><i>cmd</i> ] [<i>arg ...</i> ] </dt>
<dd>  </dd>
<dd> <p> If neither the -<code>v</code> nor -<code>V</code> option is given, <i>cmd</i> is executed exactly as if <code>command</code> had not been specified, with two exceptions: firstly, <i>cmd</i> cannot be a shell function; and secondly, special built-in commands lose their specialness (i.e. redirection and utility errors do not cause the shell to exit, and command assignments are not permanent). </p>
<p> If the -<code>p</code> option is given, a default search path is used instead of the current value of <code>PATH</code> the actual value of which is system dependent. </p>
<p> If the -<code>v</code> option is given, instead of executing <i>cmd</i> information about what would be executed is given (and the same is done for <i>arg ... )</i> For special and regular built-in commands and functions, their names are simply printed; for aliases, a command that defines them is printed; and for commands found by searching the <code>PATH</code> parameter, the full path of the command is printed. If no command is found (i.e. the path search fails), nothing is printed and <code>command</code> exits with a non-zero status. The -<code>V</code> option is like the -<code>v</code> option, except it is more verbose. </p>
 </dd>
<dt><code>continue </code>[<i>level</i> ] </dt>
<dd> <p> Jumps to the beginning of the <i>level </i><code>th</code> inner-most <code>for</code> <code>select</code> <code>until</code> or <code>while</code> loop. <i>level</i> defaults to 1. </p>
 </dd>
<dt><code>echo</code> [-<code>Een</code> ] [<i>arg ...</i> ] </dt>
<dd> <p> <i>Warning:</i> </p>
 </dd>
<dd> <p> this utility is not portable; use the Korn shell builtin <code>print</code> instead. </p>
<p> Prints its arguments (separated by spaces) followed by a newline, to the standard output. The newline is suppressed if any of the arguments contain the backslash sequence `\c&#8217; See the <code>print</code> command below for a list of other backslash sequences that are recognised. </p>
<p> The options are provided for compatibility with BSD shell scripts. The -<code>n</code> option suppresses the trailing newline, -<code>e</code> enables backslash interpretation (a no-op, since this is normally done), and -<code>E</code> suppresses backslash interpretation. </p>
<p> If the <code>posix</code> or <code>sh</code> option is set or this is a direct builtin call, only the first argument is treated as an option, and only if it is exactly ``-<code>n</code> &#8216;&#8216; Backslash interpretation is disabled. </p>
 </dd>
<dt><code>eval </code><i>command ...</i></dt>
<dd> <p> The arguments are concatenated (with spaces between them) to form a single string which the shell then parses and executes in the current environment. </p>
 </dd>
<dt><code>exec</code> [<i>command </i>[<i>arg ...</i> ] ] </dt>
<dd>  </dd>
<dd> <p> The command is executed without forking, replacing the shell process. </p>
<p> If no command is given except for I/O redirection, the I/O redirection is permanent and the shell is not replaced. Any file descriptors greater than 2 which are opened or <a href="/docs/linux/man/2-dup/">dup</a>(2)Ns&#8217;d in this way are not made available to other executed commands (i.e. commands that are not built-in to the shell). Note that the Bourne shell differs here; it does pass these file descriptors on. </p>
 </dd>
<dt><code>exit </code>[<i>status</i> ] </dt>
<dd> <p> The shell exits with the specified exit status. If <i>status</i> is not specified, the exit status is the current value of the <code>$?</code> parameter. </p>
 </dd>
<dt><code>export</code> [-<code>p</code> ] [<i>parameter </i>[= <i>value</i> ] ] </dt>
<dd>  </dd>
<dd> <p> Sets the export attribute of the named parameters. Exported parameters are passed in the environment to executed commands. If values are specified, the named parameters are also assigned. </p>
<p> If no parameters are specified, all parameters with the export attribute set are printed one per line; either their names, or, if a `-&#8216; with no option letter is specified, name=value pairs, or, with -<code>p</code> <code>export</code> commands suitable for re-entry. </p>
 </dd>
<dt><code>false</code></dt>
<dd> <p> A command that exits with a non-zero status. </p>
 </dd>
<dt><code>fc</code> [-<code>e </code><i>editor |</i> -<code>l </code>[-<code>n </code>] ] [-<code>r</code> ] [<i>first </i>[<i>last</i> ] ] </dt>
<dd> <p> <i>first</i> </p>
 </dd>
<dd> <p> and <i>last</i> select commands from the history. Commands can be selected by history number or a string specifying the most recent command starting with that string. The -<code>l</code> option lists the command on standard output, and -<code>n</code> inhibits the default command numbers. The -<code>r</code> option reverses the order of the list. Without -<code>l</code> the selected commands are edited by the editor specified with the -<code>e</code> option, or if no -<code>e</code> is specified, the editor specified by the <code>FCEDIT</code> parameter (if this parameter is not set, /bin/ed is used), and then executed by the shell. </p>
 </dd>
<dt><code>fc</code><code>-e - | -s</code> [-<code>g</code> ] [<i>old </i><code>= </code><i>new</i> ] [<i>prefix</i> ] </dt>
<dd>  </dd>
<dd> <p> Re-execute the selected command (the previous command by default) after performing the optional substitution of <i>old</i> with <i>new</i> If -<code>g</code> is specified, all occurrences of <i>old</i> are replaced with <i>new</i> The meaning of <code>-e -</code> and -<code>s</code> is identical: re-execute the selected command without invoking an editor. This command is usually accessed with the predefined: <code>alias r=&#8216;fc -e -&#8216;</code> </p>
 </dd>
<dt><code>fg </code>[<i>job ...</i> ] </dt>
<dd> <p> Resume the specified job(s) in the foreground. If no jobs are specified, <code>%+</code> is assumed. See Sx Job control below for more information. </p>
 </dd>
<dt><code>getopts</code><i>optstring name</i> [<i>arg ...</i> ] </dt>
<dd>  </dd>
<dd> <p> Used by shell procedures to parse the specified arguments (or positional parameters, if no arguments are given) and to check for legal options. <i>optstring</i> contains the option letters that <code>getopts</code> is to recognise. If a letter is followed by a colon, the option is expected to have an argument. Options that do not take arguments may be grouped in a single argument. If an option takes an argument and the option character is not the last character of the argument it is found in, the remainder of the argument is taken to be the option&#8217;s argument; otherwise, the next argument is the option&#8217;s argument. </p>
<p> Each time <code>getopts</code> is invoked, it places the next option in the shell parameter <i>name</i> and the index of the argument to be processed by the next call to <code>getopts</code> in the shell parameter <code>OPTIND</code> If the option was introduced with a `+&#8216; , the option placed in <i>name</i> is prefixed with a `+&#8216; When an option requires an argument, <code>getopts</code> places it in the shell parameter <code>OPTARG</code> </p>
<p> When an illegal option or a missing option argument is encountered, a question mark or a colon is placed in <i>name</i> (indicating an illegal option or missing argument, respectively) and <code>OPTARG</code> is set to the option character that caused the problem. Furthermore, if <i>optstring</i> does not begin with a colon, a question mark is placed in <i>name</i> <code>OPTARG</code> is unset, and an error message is printed to standard error. </p>
<p> When the end of the options is encountered, <code>getopts</code> exits with a non-zero exit status. Options end at the first (non-option argument) argument that does not start with a `-&#8216; , or when a `--&#8216; argument is encountered. </p>
<p> Option parsing can be reset by setting <code>OPTIND</code> to 1 (this is done automatically whenever the shell or a shell procedure is invoked). </p>
<p> Warning: Changing the value of the shell parameter <code>OPTIND</code> to a value other than 1, or parsing different sets of arguments without resetting <code>OPTIND</code> may lead to unexpected results. </p>
 </dd>
<dt><code>global </code><i>...</i></dt>
<dd> <p> See <code>typeset</code> </p>
 </dd>
<dt><code>hash</code> [-<code>r</code> ] [<i>name ...</i> ] </dt>
<dd>  </dd>
<dd> <p> Without arguments, any hashed executable command pathnames are listed. The -<code>r</code> option causes all hashed commands to be removed from the hash table. Each <i>name</i> is searched as if it were a command name and added to the hash table if it is an executable command. </p>
 </dd>
<dt><code>jobs</code> [-<code>lnp</code> ] [<i>job ...</i> ] </dt>
<dd>  </dd>
<dd> <p> Display information about the specified job(s); if no jobs are specified, all jobs are displayed. The -<code>n</code> option causes information to be displayed only for jobs that have changed state since the last notification. If the -<code>l</code> option is used, the process ID of each process in a job is also listed. The -<code>p</code> option causes only the process group of each job to be printed. See Sx Job control below for the format of <i>job</i> and the displayed job. </p>
 </dd>
<dt><code>kill</code> [-<code>s </code><i>signame |</i><code>- </code><i>signum |</i><code>- </code><i>signame </i>] <code>{ </code><i>job | pid | pgrp </i><code>}</code><i>...</i></dt>
<dd>  </dd>
<dd> <p> Send the specified signal to the specified jobs, process IDs, or process groups. If no signal is specified, the <code>TERM</code> signal is sent. If a job is specified, the signal is sent to the job&#8217;s process group. See Sx Job control below for the format of <i>job</i> </p>
 </dd>
<dt><code>kill</code> -<code>l</code> [<i>exit-status ...</i> ] </dt>
<dd>  </dd>
<dd> <p> Print the signal name corresponding to <i>exit-status</i> If no arguments are specified, a list of all the signals, their numbers, and a short description of them are printed. </p>
 </dd>
<dt><code>let </code>[<i>expression ...</i> ] </dt>
<dd> <p> Each expression is evaluated (see Sx Arithmetic expressions above). If all expressions are successfully evaluated, the exit status is 0 (1) if the last expression evaluated to non-zero (zero). If an error occurs during the parsing or evaluation of an expression, the exit status is greater than 1. Since expressions may need to be quoted, <code>(( </code><i>expr </i><code>))</code> is syntactic sugar for <code>let </code><i>expr </i> </p>
 </dd>
<dt><code>let]</code></dt>
<dd> <p> Internally used alias for <code>let</code> </p>
 </dd>
<dt><code>mknod</code> [-<code>m </code><i>mode</i> ] <i>name</i><code>b|c</code><i>major minor</i></dt>
<dd>  </dd>
<dt><code>mknod</code> [-<code>m </code><i>mode</i> ] <i>name</i><code>p</code></dt>
<dd>  </dd>
<dd> <p> Create a device special file. The file type may be <code>b</code> (block type device), <code>c</code> (character type device), or <code>p</code> (named pipe , <code>FIFO</code> ) The file created may be modified according to its <i>mode</i> (via the -<code>m</code> option), <i>major</i> (major device number), and <i>minor</i> (minor device number). </p>
<p> See mknod(8) for further information. </p>
 </dd>
<dt><code>print</code> [-<code>nprsu </code>[<i>n |</i>] -<code>R </code>[-<code>en </code>] ] [<i>argument ...</i> ] </dt>
<dd> <p> <code>print</code> </p>
 </dd>
<dd> <p> prints its arguments on the standard output, separated by spaces and terminated with a newline. The -<code>n</code> option suppresses the newline. By default, certain C escapes are translated. These include these mentioned in Sx Backslash expansion above, as well as `\c&#8217; , which is equivalent to using the -<code>n</code> option. Backslash expansion may be inhibited with the -<code>r</code> option. The -<code>s</code> option prints to the history file instead of standard output; the -<code>u</code> option prints to file descriptor <i>n</i> Po <i>n</i> defaults to 1 if omitted Pc ; and the -<code>p</code> option prints to the co-process (see Sx Co-processes above). </p>
<p> The -<code>R</code> option is used to emulate, to some degree, the BSD <a href="/docs/linux/man/1-echo/">echo</a>(1) command which does not process `\&#8216; sequences unless the -<code>e</code> option is given. As above, the -<code>n</code> option suppresses the trailing newline. </p>
 </dd>
<dt><code>printf </code><i>format </i>[<i>arguments ...</i> ] </dt>
<dd> <p> Formatted output. Approximately the same as the <a href="/docs/linux/man/1-printf/">printf</a>(1), utility, except it uses the same Sx Backslash expansion and I/O code and does hot handle floating point as the rest of <code>mksh</code> This is not normally part of <code>mksh</code> however, distributors may have added this as builtin as a speed hack. Do not use in new code. </p>
 </dd>
<dt><code>pwd </code>[-<code>LP</code> ] </dt>
<dd> <p> Print the present working directory. If the -<code>L</code> option is used or if the <code>physical</code> option isn&#8217;t set (see the <code>set</code> command below), the logical path is printed (i.e. the path used to <code>cd</code> to the current directory). If the -<code>P</code> option (physical path) is used or if the <code>physical</code> option is set, the path determined from the filesystem (by following `..&#8216; directories to the root directory) is printed. </p>
 </dd>
<dt><code>read</code> [-<code>A | -a</code> ] [-<code>d </code><i>x</i> ] [-<code>N </code><i>z |</i> -<code>n </code><i>z </i>] [-<code>p |</code> -<code>u </code>[<i>n</i> ] [-<code>t </code><i>n</i> ] ] [-<code>rs</code> ] [<i>p ...</i> ] </dt>
<dd>  </dd>
<dd> <p> Reads a line of input, separates the input into fields using the <code>IFS</code> parameter (see Sx Substitution above), and assigns each field to the specified parameters <i>p</i> If no parameters are specified, the <code>REPLY</code> parameter is used to store the result. With the -<code>A</code> and -<code>a</code> options, only no or one parameter is accepted. If there are more parameters than fields, the extra parameters are set to the empty string or 0; if there are more fields than parameters, the last parameter is assigned the remaining fields (including the word separators). </p>
<p> The options are as follows: </p>
 </dd>
<dl>
<dt><code>-A</code></dt>
<dd> <p> Store the result into the parameter <i>p</i> (or <code>REPLY</code> as array of words. </p>
 </dd>
<dt><code>-a</code></dt>
<dd> <p> Store the result without word splitting into the parameter <i>p</i> (or <code>REPLY</code> as array of characters (wide characters if the <code>utf8-mode</code> option is enacted, octets otherwise). </p>
 </dd>
<dt><code>-d </code><i>x</i></dt>
<dd> <p> Use the first byte of <i>x</i> <code>NUL</code> if empty, instead of the ASCII newline character as input line delimiter. </p>
 </dd>
<dt><code>-N </code><i>z</i></dt>
<dd> <p> Instead of reading till end-of-line, read exactly <i>z</i> bytes; less if EOF or a timeout occurs. </p>
 </dd>
<dt><code>-n </code><i>z</i></dt>
<dd> <p> Instead of reading till end-of-line, read up to <i>z</i> bytes but return as soon as any bytes are read, e.g. from a slow terminal device, or if EOF or a timeout occurs. </p>
 </dd>
<dt><code>-p</code></dt>
<dd> <p> Read from the currently active co-process, see Sx Co-processes above for details on this. </p>
 </dd>
<dt><code>-u </code>[<i>n</i> ] </dt>
<dd> <p> Read from the file descriptor <i>n</i> (defaults to 0, i.e. standard input). The argument must immediately follow the option character. </p>
 </dd>
<dt><code>-t </code><i>n</i></dt>
<dd> <p> Interrupt reading after <i>n</i> seconds (specified as positive decimal value with an optional fractional part). </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> Normally, the ASCII backslash character escapes the special meaning of the following character and is stripped from the input; <code>read</code> does not stop when encountering a backslash-newline sequence and does not store that newline in the result. This option enables raw mode, in which backslashes are not processed. </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> The input line is saved to the history. </p>
 </dd></dl>
<p> If the input is a terminal, both the -<code>N</code> and -<code>n</code> options set it into raw mode; they read an entire file if -1 is passed as <i>z</i> argument. </p>
<p> The first parameter may have a question mark and a string appended to it, in which case the string is used as a prompt (printed to standard error before any input is read) if the input is a <a href="/docs/linux/man/4-tty/">tty</a>(4) (e.g. <code>read nfoo?&#8216;number of foos: &#8216; )</code> </p>
<p> If no input is read or a timeout occurred, <code>read</code> exits with a non-zero status. </p>
<p> Another handy set of tricks: If <code>read</code> is run in a loop such as <code>while read foo; do ...; done</code> then leading whitespace will be removed (IFS) and backslashes processed. You might want to use <code>while IFS= read -r foo; do ...; done</code> for pristine I/O. Similarily, when using the -<code>a</code> option, use of the -<code>r</code> option might be prudent; the same applies for: </p>
<blockquote><pre><code>find . -type f -print0 | \
    while IFS= read -d '' -r filename; do
        print -r -- &quot;found &lt;${filename#./}&gt;&quot;
done
</code></pre>
</blockquote>
<p> The inner loop will be executed in a subshell and variable changes cannot be propagated if executed in a pipeline: </p>
<blockquote><pre><code>bar | baz | while read foo; do ...; done
</code></pre>
</blockquote>
<p> Use co-processes instead: </p>
<blockquote><pre><code>bar | baz |&amp;
while read -p foo; do ...; done
exec 3&gt;&amp;p; exec 3&gt;&amp;-
</code></pre>
</blockquote>
<dt><code>readonly</code> [-<code>p</code> ] [<i>parameter</i> [<code>= </code><i>value</i> ] <i>... </i>] </dt>
<dd>  </dd>
<dd> <p> Sets the read-only attribute of the named parameters. If values are given, parameters are set to them before setting the attribute. Once a parameter is made read-only, it cannot be unset and its value cannot be changed. </p>
<p> If no parameters are specified, the names of all parameters with the read-only attribute are printed one per line, unless the -<code>p</code> option is used, in which case <code>readonly</code> commands defining all read-only parameters, including their values, are printed. </p>
 </dd>
<dt><code>realpath</code> [-<code>-</code> ] <i>name</i></dt>
<dd>  </dd>
<dd> <p> Prints the resolved absolute pathname corresponding to <i>name</i> If <i>name</i> ends with a slash (`/&#8216; ) it&#8217;s also checked for existence and whether it is a directory; otherwise, <code>realpath</code> returns 0 if the pathname either exists or can be created immediately, i.e. all but the last component exist and are directories. </p>
 </dd>
<dt><code>rename</code> [-<code>-</code> ] <i>from to</i></dt>
<dd>  </dd>
<dd> <p> Renames the file <i>from</i> to <i>to</i> Both must be complete pathnames and on the same device. This builtin is intended for emergency situations where /bin/mv becomes unusable, and directly calls <a href="/docs/linux/man/2-rename/">rename</a>(2). </p>
 </dd>
<dt><code>return </code>[<i>status</i> ] </dt>
<dd> <p> Returns from a function or <code>.</code> script, with exit status <i>status</i> If no <i>status</i> is given, the exit status of the last executed command is used. If used outside of a function or <code>.</code> script, it has the same effect as <code>exit</code> Note that treats both profile and <code>ENV</code> files as <code>.</code> scripts, while the original Korn shell only treats profiles as <code>.</code> scripts. </p>
 </dd>
<dt><code>set </code>[<code>+-abCefhiklmnprsUuvXx </code>[<code>+-o </code><i>option</i> ] ] [<code>+-A </code><i>name</i> ] [-<code>-</code> ] [<i>arg ...</i> ] </dt>
<dd>  </dd>
<dd> <p> The <code>set</code> command can be used to set (<code>-</code> ) or clear (<code>+</code> ) shell options, set the positional parameters, or set an array parameter. Options can be changed using the <code>+-o </code><i>option</i> syntax, where <i>option</i> is the long name of an option, or using the <code>+- </code><i>letter</i> syntax, where <i>letter</i> is the option&#8217;s single letter name (not all options have a single letter name). The following table lists both option letters (if they exist) and long names along with a description of what the option does: </p>
 </dd>
<dl>
<dt><code>-A </code><i>name</i></dt>
<dd> <p> Sets the elements of the array parameter <i>name</i> to <i>arg ...</i> If -<code>A</code> is used, the array is reset (i.e. emptied) first; if <code>+A</code> is used, the first N elements are set (where N is the number of arguments); the rest are left untouched. </p>
<p> An alternative syntax for the command <code>set -A foo -- a b c</code> which is compatible to <code>GNU</code> <code>bash</code> and also supported by AT&amp;T System <code>ksh93</code> is: <code>foo=(a b c); foo+=(d e)</code> </p>
<p> Another AT&amp;T System <code>ksh93</code> and <code>GNU</code> <code>bash</code> extension allows specifying the indices used for <i>arg ...</i> (from the above example, <code>a b c</code> ) like this: <code>set -A foo -- [0]=a [1]=b [2]=c</code> or <code>foo=([0]=a [1]=b [2]=c)</code> which can also be written <code>foo=([0]=a b c)</code> because indices are incremented automatically. </p>
 </dd>
<dt><code>-a | -o allexport</code></dt>
<dd> <p> All new parameters are created with the export attribute. </p>
 </dd>
<dt><code>-b | -o notify</code></dt>
<dd> <p> Print job notification messages asynchronously, instead of just before the prompt. Only used if job control is enabled (-<code>m</code> ) </p>
 </dd>
<dt><code>-C | -o noclobber</code></dt>
<dd> <p> Prevent &gt; redirection from overwriting existing files. Instead, &gt;| must be used to force an overwrite. </p>
 </dd>
<dt><code>-e | -o errexit</code></dt>
<dd> <p> Exit (after executing the <code>ERR</code> trap) as soon as an error occurs or a command fails (i.e. exits with a non-zero status). This does not apply to commands whose exit status is explicitly tested by a shell construct such as <code>if</code> <code>until</code> <code>while</code> <code>&amp;&amp;</code> <code>||</code> or <code>!</code> statements. </p>
 </dd>
<dt><code>-f | -o noglob</code></dt>
<dd> <p> Do not expand file name patterns. </p>
 </dd>
<dt><code>-h | -o trackall</code></dt>
<dd> <p> Create tracked aliases for all executed commands (see Sx Aliases above). Enabled by default for non-interactive shells. </p>
 </dd>
<dt><code>-i | -o interactive</code></dt>
<dd> <p> The shell is an interactive shell. This option can only be used when the shell is invoked. See above for a description of what this means. </p>
 </dd>
<dt><code>-k | -o keyword</code></dt>
<dd> <p> Parameter assignments are recognised anywhere in a command. </p>
 </dd>
<dt><code>-l | -o login</code></dt>
<dd> <p> The shell is a login shell. This option can only be used when the shell is invoked. See above for a description of what this means. </p>
 </dd>
<dt><code>-m | -o monitor</code></dt>
<dd> <p> Enable job control (default for interactive shells). </p>
 </dd>
<dt><code>-n | -o noexec</code></dt>
<dd> <p> Do not execute any commands. Useful for checking the syntax of scripts (ignored if interactive). </p>
 </dd>
<dt><code>-p | -o privileged</code></dt>
<dd> <p> The shell is a privileged shell. It is set automatically if, when the shell starts, the real UID or GID does not match the effective UID (EUID) or GID (EGID), respectively. See above for a description of what this means. </p>
 </dd>
<dt><code>-r | -o restricted</code></dt>
<dd> <p> The shell is a restricted shell. This option can only be used when the shell is invoked. See above for a description of what this means. </p>
 </dd>
<dt><code>-s | -o stdin</code></dt>
<dd> <p> If used when the shell is invoked, commands are read from standard input. Set automatically if the shell is invoked with no arguments. </p>
<p> When -<code>s</code> is used with the <code>set</code> command it causes the specified arguments to be sorted before assigning them to the positional parameters (or to array <i>name</i> if -<code>A</code> is used). </p>
 </dd>
<dt><code>-U | -o utf8-mode</code></dt>
<dd> <p> Enable UTF-8 support in the Sx Emacs editing mode and internal string handling functions. This flag is disabled by default, but can be enabled by setting it on the shell command line; is enabled automatically for interactive shells if requested at compile time, your system supports Fn setlocale LC_CTYPE and optionally Fn nl_langinfo CODESET , or the <code>LC_ALL</code> <code>LC_CTYPE</code> or <code>LANG</code> environment variables, and at least one of these returns something that matches ``UTF-8&#8217;&#8216; or ``utf8&#8217;&#8216; case-insensitively; for direct builtin calls depending on the aforementioned environment variables; or for stdin or scripts, if the input begins with a UTF-8 Byte Order Mark. </p>
 </dd>
<dt><code>-u | -o nounset</code></dt>
<dd> <p> Referencing of an unset parameter, other than ``$@&#8216;&#8216; or ``$*&#8216;&#8216; is treated as an error, unless one of the `-&#8216; , `+&#8216; , or `=&#8216; modifiers is used. </p>
 </dd>
<dt><code>-v | -o verbose</code></dt>
<dd> <p> Write shell input to standard error as it is read. </p>
 </dd>
<dt><code>-X | -o markdirs</code></dt>
<dd> <p> Mark directories with a trailing `/&#8216; during file name generation. </p>
 </dd>
<dt><code>-x | -o xtrace</code></dt>
<dd> <p> Print command trees when they are executed, preceded by the value of <code>PS4</code> </p>
 </dd>
<dt><code>-o bgnice</code></dt>
<dd> <p> Background jobs are run with lower priority. </p>
 </dd>
<dt><code>-o braceexpand</code></dt>
<dd> <p> Enable brace expansion (a.k.a. alternation). This is enabled by default. If disabled, tilde expansion after an equals sign is disabled as a side effect. </p>
 </dd>
<dt><code>-o emacs</code></dt>
<dd> <p> Enable BRL emacs-like command-line editing (interactive shells only); see Sx Emacs editing mode . </p>
 </dd>
<dt><code>-o gmacs</code></dt>
<dd> <p> Enable gmacs-like command-line editing (interactive shells only). Currently identical to emacs editing except that transpose-chars (^T) acts slightly differently. </p>
 </dd>
<dt><code>-o ignoreeof</code></dt>
<dd> <p> The shell will not (easily) exit when end-of-file is read; <code>exit</code> must be used. To avoid infinite loops, the shell will exit if <code>EOF</code> is read 13 times in a row. </p>
 </dd>
<dt><code>-o nohup</code></dt>
<dd> <p> Do not kill running jobs with a <code>SIGHUP</code> signal when a login shell exits. Currently set by default, but this may change in the future to be compatible with AT&amp;T System <code>ksh</code> which doesn&#8217;t have this option, but does send the <code>SIGHUP</code> signal. </p>
 </dd>
<dt><code>-o nolog</code></dt>
<dd> <p> No effect. In the original Korn shell, this prevents function definitions from being stored in the history file. </p>
 </dd>
<dt><code>-o physical</code></dt>
<dd> <p> Causes the <code>cd</code> and <code>pwd</code> commands to use ``physical&#8217;&#8216; (i.e. the filesystem&#8217;s) `..&#8216; directories instead of ``logical&#8217;&#8216; directories (i.e. the shell handles `..&#8216; which allows the user to be oblivious of symbolic links to directories). Clear by default. Note that setting this option does not affect the current value of the <code>PWD</code> parameter; only the <code>cd</code> command changes <code>PWD</code> See the <code>cd</code> and <code>pwd</code> commands above for more details. </p>
 </dd>
<dt><code>-o pipefail</code></dt>
<dd> <p> Make the exit status of a pipeline (before logically complementing) the rightmost non-zero errorlevel, or zero if all commands exited with zero. </p>
 </dd>
<dt><code>-o posix</code></dt>
<dd> <p> Enable a somewhat more Px ish mode. As a side effect, setting this flag turns off <code>braceexpand</code> mode, which can be turned back on manually, and <code>sh</code> mode. </p>
 </dd>
<dt><code>-o sh</code></dt>
<dd> <p> Enable /bin/sh (kludge) mode. Automatically enabled if the basename of the shell invocation begins with ``sh&#8217;&#8216; and this autodetection feature is compiled in (not in MirBSD) As a side effect, setting this flag turns off <code>braceexpand</code> mode, which can be turned back on manually, and <code>posix</code> mode. </p>
 </dd>
<dt><code>-o vi</code></dt>
<dd> <p> Enable <a href="/docs/linux/man/1-vi/">vi</a>(1)Ns-like command-line editing (interactive shells only). </p>
 </dd>
<dt><code>-o vi-esccomplete</code></dt>
<dd> <p> In vi command-line editing, do command and file name completion when escape (^[) is entered in command mode. </p>
 </dd>
<dt><code>-o vi-tabcomplete</code></dt>
<dd> <p> In vi command-line editing, do command and file name completion when tab (^I) is entered in insert mode. This is the default. </p>
 </dd>
<dt><code>-o viraw</code></dt>
<dd> <p> No effect. In the original Korn shell, unless <code>viraw</code> was set, the vi command-line mode would let the <a href="/docs/linux/man/4-tty/">tty</a>(4) driver do the work until ESC (^[) was entered. is always in viraw mode. </p>
 </dd></dl>
<p> These options can also be used upon invocation of the shell. The current set of options (with single letter names) can be found in the parameter `$-&#8216; <code>set -o</code> with no option name will list all the options and whether each is on or off; <code>set +o</code> will print the long names of all options that are currently on. </p>
<p> Remaining arguments, if any, are positional parameters and are assigned, in order, to the positional parameters (i.e. $1, $2, etc.). If options end with `--&#8216; and there are no remaining arguments, all positional parameters are cleared. If no options or arguments are given, the values of all names are printed. For unknown historical reasons, a lone `-&#8216; option is treated specially --- it clears both the -<code>v</code> and -<code>x</code> options. </p>
<dt><code>shift </code>[<i>number</i> ] </dt>
<dd> <p> The positional parameters <i>number </i><code>+1</code> <i>number </i><code>+2</code> etc. are renamed to `1&#8217; `2&#8217; etc. <i>number</i> defaults to 1. </p>
 </dd>
<dt><code>sleep </code><i>seconds</i></dt>
<dd> <p> Suspends execution for a minimum of the <i>seconds</i> specified as positive decimal value with an optional fractional part. Signal delivery may continue execution earlier. </p>
 </dd>
<dt><code>source </code><i>file </i>[<i>arg ...</i> ] </dt>
<dd> <p> Like <code>. Po </code>Do dot Dc Pc , except that the current working directory is appended to the <code>PATH</code> in GNU <code>bash</code> and <code>mksh</code> In <code>ksh93</code> and <code>mksh</code> this is implemented as a shell alias instead of a builtin. </p>
 </dd>
<dt><code>test </code><i>expression</i></dt>
<dd>  </dd>
<dt><code>[ </code><i>expression </i><code>]</code></dt>
<dd> <p> <code>test</code> evaluates the <i>expression</i> and returns zero status if true, 1 if false, or greater than 1 if there was an error. It is normally used as the condition command of <code>if</code> and <code>while</code> statements. Symbolic links are followed for all <i>file</i> expressions except -<code>h</code> and -<code>L</code> </p>
<p> The following basic expressions are available: </p>
 </dd>
<dl>
<dt><code>-a </code><i>file</i></dt>
<dd> <p> <i>file</i> exists. </p>
 </dd>
<dt><code>-b </code><i>file</i></dt>
<dd> <p> <i>file</i> is a block special device. </p>
 </dd>
<dt><code>-c </code><i>file</i></dt>
<dd> <p> <i>file</i> is a character special device. </p>
 </dd>
<dt><code>-d </code><i>file</i></dt>
<dd> <p> <i>file</i> is a directory. </p>
 </dd>
<dt><code>-e </code><i>file</i></dt>
<dd> <p> <i>file</i> exists. </p>
 </dd>
<dt><code>-f </code><i>file</i></dt>
<dd> <p> <i>file</i> is a regular file. </p>
 </dd>
<dt><code>-G </code><i>file</i></dt>
<dd> <p> <i>file </i><code>&#8216;s</code> group is the shell&#8217;s effective group ID. </p>
 </dd>
<dt><code>-g </code><i>file</i></dt>
<dd> <p> <i>file </i><code>&#8216;s</code> mode has the setgid bit set. </p>
 </dd>
<dt><code>-H </code><i>file</i></dt>
<dd> <p> <i>file</i> is a context dependent directory (only useful on HP-UX). </p>
 </dd>
<dt><code>-h </code><i>file</i></dt>
<dd> <p> <i>file</i> is a symbolic link. </p>
 </dd>
<dt><code>-k </code><i>file</i></dt>
<dd> <p> <i>file </i><code>&#8216;s</code> mode has the sticky(8) bit set. </p>
 </dd>
<dt><code>-L </code><i>file</i></dt>
<dd> <p> <i>file</i> is a symbolic link. </p>
 </dd>
<dt><code>-O </code><i>file</i></dt>
<dd> <p> <i>file </i><code>&#8216;s</code> owner is the shell&#8217;s effective user ID. </p>
 </dd>
<dt><code>-o </code><i>option</i></dt>
<dd> <p> Shell <i>option</i> is set (see the <code>set</code> command above for a list of options). As a non-standard extension, if the option starts with a `!&#8216; , the test is negated; the test always fails if <i>option</i> doesn&#8217;t exist (so [ -o foo -o -o !foo ] returns true if and only if option <i>foo</i> exists). The same can be achieved with [ -o ?foo ] like in AT&amp;T System <code>ksh93</code> <i>option</i> can also be the short flag led by either `-&#8216; or `+&#8216; (no logical negation) for example `-x&#8217; or `+x&#8217; instead of `xtrace&#8217; </p>
 </dd>
<dt><code>-p </code><i>file</i></dt>
<dd> <p> <i>file</i> is a named pipe (<code>FIFO</code> ) </p>
 </dd>
<dt><code>-r </code><i>file</i></dt>
<dd> <p> <i>file</i> exists and is readable. </p>
 </dd>
<dt><code>-S </code><i>file</i></dt>
<dd> <p> <i>file</i> is a unix(4)Ns-domain socket. </p>
 </dd>
<dt><code>-s </code><i>file</i></dt>
<dd> <p> <i>file</i> is not empty. </p>
 </dd>
<dt><code>-t </code><i>fd</i></dt>
<dd> <p> File descriptor <i>fd</i> is a <a href="/docs/linux/man/4-tty/">tty</a>(4) device. </p>
 </dd>
<dt><code>-u </code><i>file</i></dt>
<dd> <p> <i>file </i><code>&#8216;s</code> mode has the setuid bit set. </p>
 </dd>
<dt><code>-w </code><i>file</i></dt>
<dd> <p> <i>file</i> exists and is writable. </p>
 </dd>
<dt><code>-x </code><i>file</i></dt>
<dd> <p> <i>file</i> exists and is executable. </p>
 </dd>
<dt><i>file1 -</i><code>nt </code><i>file2</i></dt>
<dd> <p> <i>file1</i> is newer than <i>file2</i> or <i>file1</i> exists and <i>file2</i> does not. </p>
 </dd>
<dt><i>file1 -</i><code>ot </code><i>file2</i></dt>
<dd> <p> <i>file1</i> is older than <i>file2</i> or <i>file2</i> exists and <i>file1</i> does not. </p>
 </dd>
<dt><i>file1 -</i><code>ef </code><i>file2</i></dt>
<dd> <p> <i>file1</i> is the same file as <i>file2</i> </p>
 </dd>
<dt><i>string</i></dt>
<dd> <p> <i>string</i> has non-zero length. </p>
 </dd>
<dt><code>-n </code><i>string</i></dt>
<dd> <p> <i>string</i> is not empty. </p>
 </dd>
<dt><code>-z </code><i>string</i></dt>
<dd> <p> <i>string</i> is empty. </p>
 </dd>
<dt><i>string </i><code>= </code><i>string</i></dt>
<dd> <p> Strings are equal. </p>
 </dd>
<dt><i>string </i><code>== </code><i>string</i></dt>
<dd> <p> Strings are equal. </p>
 </dd>
<dt><i>string </i><code>&gt; </code><i>string</i></dt>
<dd> <p> First string operand is greater than second string operand. </p>
 </dd>
<dt><i>string </i><code>&lt; </code><i>string</i></dt>
<dd> <p> First string operand is less than second string operand. </p>
 </dd>
<dt><i>string </i><code>!= </code><i>string</i></dt>
<dd> <p> Strings are not equal. </p>
 </dd>
<dt><i>number -</i><code>eq </code><i>number</i></dt>
<dd> <p> Numbers compare equal. </p>
 </dd>
<dt><i>number -</i><code>ne </code><i>number</i></dt>
<dd> <p> Numbers compare not equal. </p>
 </dd>
<dt><i>number -</i><code>ge </code><i>number</i></dt>
<dd> <p> Numbers compare greater than or equal. </p>
 </dd>
<dt><i>number -</i><code>gt </code><i>number</i></dt>
<dd> <p> Numbers compare greater than. </p>
 </dd>
<dt><i>number -</i><code>le </code><i>number</i></dt>
<dd> <p> Numbers compare less than or equal. </p>
 </dd>
<dt><i>number -</i><code>lt </code><i>number</i></dt>
<dd> <p> Numbers compare less than. </p>
 </dd></dl>
<p> The above basic expressions, in which unary operators have precedence over binary operators, may be combined with the following operators (listed in increasing order of precedence): </p>
<blockquote><pre><code>expr -o expr Logical OR.
expr -a expr Logical AND.
! expr Logical NOT.
( expr ) Grouping.
</code></pre>
</blockquote>
<p> Note that a number actually may be an arithmetic expression, such as a mathematical term or the name of an integer variable: </p>
<blockquote><pre><code>x=1; [ &quot;x&quot; -eq 1 ] evaluates to true
</code></pre>
</blockquote>
<p> Note that some special rules are applied (courtesy of Px ) if the number of arguments to <code>test</code> or inside the brackets <code>[ ... ]</code> is less than five: if leading `!&#8216; arguments can be stripped such that only one to three arguments remain, then the lowered comparison is executed; (thanks to XSI) parentheses <code>\( ... \)</code> lower four- and three-argument forms to two- and one-argument forms, respectively; three-argument forms ultimately prefer binary operations, followed by negation and parenthesis lowering; two- and four-argument forms prefer negation followed by parenthesis; the one-argument form always implies -<code>n</code> </p>
<p> <code>Note</code> A common mistake is to use ``if [ $foo = bar ]&#8216;&#8216; which fails if parameter ``foo&#8217;&#8216; is <code>NULL</code> or unset, if it has embedded spaces (i.e. <code>IFS</code> octets), or if it is a unary operator like `!&#8216; or `-<code>n</code> &#8216; Use tests like ``if [ x$foo = xbar ]&#8216;&#8216; instead, or the double-bracket operator ``if [[ $foo = bar ]]&#8216;&#8216; or, to avoid pattern matching (see <code>[[</code> above): ``if [[ $foo = $bar ]]&#8216;&#8216; </p>
<p> The <code>[[ ... ]]</code> construct is not only more secure to use but also often faster. </p>
<dt><code>time</code> [-<code>p</code> ] [<i>pipeline</i> ] </dt>
<dd>  </dd>
<dd> <p> If a <i>pipeline</i> is given, the times used to execute the pipeline are reported. If no pipeline is given, then the user and system time used by the shell itself, and all the commands it has run since it was started, are reported. The times reported are the real time (elapsed time from start to finish), the user CPU time (time spent running in user mode), and the system CPU time (time spent running in kernel mode). Times are reported to standard error; the format of the output is: </p>
<blockquote><p> <code>&quot;0m0.00s real 0m0.00s user 0m0.00s system&quot;</code> </p>
</blockquote>
<p> If the -<code>p</code> option is given the output is slightly longer: </p>
<blockquote><pre><code>real 0.00
user 0.00
sys 0.00
</code></pre>
</blockquote>
<p> It is an error to specify the -<code>p</code> option unless <i>pipeline</i> is a simple command. </p>
<p> Simple redirections of standard error do not affect the output of the <code>time</code> command: </p>
<blockquote><p> <code>$ time sleep 1 2&gt;afile</code> </p>
</blockquote>
<blockquote><p> <code>$ { time sleep 1; } 2&gt;afile</code> </p>
</blockquote>
<p> Times for the first command do not go to ``afile&#8217;&#8216; but those of the second command do. </p>
 </dd>
<dt><code>times</code></dt>
<dd> <p> Print the accumulated user and system times used both by the shell and by processes that the shell started which have exited. The format of the output is: </p>
<blockquote><pre><code>0m0.00s 0m0.00s
0m0.00s 0m0.00s
</code></pre>
</blockquote>
 </dd>
<dt><code>trap </code>[<i>handler signal ...</i> ] </dt>
<dd> <p> Sets a trap handler that is to be executed when any of the specified signals are received. <i>handler</i> is either a <code>NULL</code> string, indicating the signals are to be ignored, a minus sign (`-&#8216; ) indicating that the default action is to be taken for the signals (see signal(3)), or a string containing shell commands to be evaluated and executed at the first opportunity (i.e. when the current command completes, or before printing the next <code>PS1</code> prompt) after receipt of one of the signals. <i>signal</i> is the name of a signal (e.g. <code>PIPE</code> or <code>ALRM</code> or the number of the signal (see the <code>kill -l</code> command above). </p>
<p> There are two special signals: <code>EXIT</code> (also known as 0) which is executed when the shell is about to exit, and <code>ERR</code> which is executed after an error occurs (an error is something that would cause the shell to exit if the -<code>e</code> or <code>errexit</code> option were set --- see the <code>set</code> command above). <code>EXIT</code> handlers are executed in the environment of the last executed command. Note that for non-interactive shells, the trap handler cannot be changed for signals that were ignored when the shell started. </p>
<p> With no arguments, <code>trap</code> lists, as a series of <code>trap</code> commands, the current state of the traps that have been set since the shell started. Note that the output of <code>trap</code> cannot be usefully piped to another process (an artifact of the fact that traps are cleared when subprocesses are created). </p>
<p> The original Korn shell&#8217;s <code>DEBUG</code> trap and the handling of <code>ERR</code> and <code>EXIT</code> traps in functions are not yet implemented. </p>
 </dd>
<dt><code>true</code></dt>
<dd> <p> A command that exits with a zero value. </p>
 </dd>
<dt><code>global</code> [[<code>+-alpnrtUux</code> ] [-<code>L </code>[<i>n</i> ] ] [-<code>R </code>[<i>n</i> ] ] [-<code>Z </code>[<i>n</i> ] ] [-<code>i </code>[<i>n</i> ] ] <code>| -f </code>[-<code>tux </code>] ] [<i>name</i> [<code>= </code><i>value</i> ] <i>... </i>] </dt>
<dd>  </dd>
<dt><code>typeset</code> [[<code>+-alpnrtUux</code> ] [-<code>LRZ </code>[<i>n</i> ] ] [-<code>i </code>[<i>n</i> ] ] <code>| -f </code>[-<code>tux </code>] ] [<i>name</i> [<code>= </code><i>value</i> ] <i>... </i>] </dt>
<dd>  </dd>
<dd> <p> Display or set parameter attributes. With no <i>name</i> arguments, parameter attributes are displayed; if no options are used, the current attributes of all parameters are printed as <code>typeset</code> commands; if an option is given (or `-&#8216; with no option letter), all parameters and their values with the specified attributes are printed; if options are introduced with `+&#8216; , parameter values are not printed. </p>
<p> If <i>name</i> arguments are given, the attributes of the named parameters are set (<code>-</code> ) or cleared (<code>+</code> ) Values for parameters may optionally be specified. For <i>name </i><code>[*]</code> the change affects the entire array, and no value may be specified. </p>
<p> If <code>typeset</code> is used inside a function, any parameters specified are localised. This is not done by the otherwise identical <code>global</code> <i>Note</i> This means that <code>&#8216;s global</code> command is <i>not</i> equivalent to other programming languages&#8217; as it does not allow a function called from another function to access a parameter at truly global scope, but only prevents putting an accessed one into local scope. </p>
<p> When -<code>f</code> is used, <code>typeset</code> operates on the attributes of functions. As with parameters, if no <i>name</i> arguments are given, functions are listed with their values (i.e. definitions) unless options are introduced with `+&#8216; , in which case only the function names are reported. </p>
 </dd>
<dl>
<dt><code>-a</code></dt>
<dd> <p> Indexed array attribute. </p>
 </dd>
<dt><code>-f</code></dt>
<dd> <p> Function mode. Display or set functions and their attributes, instead of parameters. </p>
 </dd>
<dt><code>-i </code>[<i>n</i> ] </dt>
<dd> <p> Integer attribute. <i>n</i> specifies the base to use when displaying the integer (if not specified, the base given in the first assignment is used). Parameters with this attribute may be assigned values containing arithmetic expressions. </p>
 </dd>
<dt><code>-L </code>[<i>n</i> ] </dt>
<dd> <p> Left justify attribute. <i>n</i> specifies the field width. If <i>n</i> is not specified, the current width of a parameter (or the width of its first assigned value) is used. Leading whitespace (and zeros, if used with the -<code>Z</code> option) is stripped. If necessary, values are either truncated or space padded to fit the field width. </p>
 </dd>
<dt><code>-l</code></dt>
<dd> <p> Lower case attribute. All upper case characters in values are converted to lower case. (In the original Korn shell, this parameter meant ``long integer&#8217;&#8216; when used with the -<code>i</code> option.) </p>
 </dd>
<dt><code>-n</code></dt>
<dd> <p> Create a bound variable (name reference): any access to the variable <i>name</i> will access the variable <i>value</i> in the current scope (this is different from AT&amp;T System <code>ksh93 !</code> instead. Also different from AT&amp;T System <code>ksh93</code> is that <i>value</i> is lazily evaluated at the time <i>name</i> is accessed. This can be used by functions to access variables whose names are passed as parametres, instead of using <code>eval</code> </p>
 </dd>
<dt><code>-p</code></dt>
<dd> <p> Print complete <code>typeset</code> commands that can be used to re-create the attributes and values of parameters. </p>
 </dd>
<dt><code>-R </code>[<i>n</i> ] </dt>
<dd> <p> Right justify attribute. <i>n</i> specifies the field width. If <i>n</i> is not specified, the current width of a parameter (or the width of its first assigned value) is used. Trailing whitespace is stripped. If necessary, values are either stripped of leading characters or space padded to make them fit the field width. </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> Read-only attribute. Parameters with this attribute may not be assigned to or unset. Once this attribute is set, it cannot be turned off. </p>
 </dd>
<dt><code>-t</code></dt>
<dd> <p> Tag attribute. Has no meaning to the shell; provided for application use. </p>
<p> For functions, -<code>t</code> is the trace attribute. When functions with the trace attribute are executed, the <code>xtrace</code> (-<code>x</code> ) shell option is temporarily turned on. </p>
 </dd>
<dt><code>-U</code></dt>
<dd> <p> Unsigned integer attribute. Integers are printed as unsigned values (combine with the -<code>i</code> option). This option is not in the original Korn shell. </p>
 </dd>
<dt><code>-u</code></dt>
<dd> <p> Upper case attribute. All lower case characters in values are converted to upper case. (In the original Korn shell, this parameter meant ``unsigned integer&#8217;&#8216; when used with the -<code>i</code> option which meant upper case letters would never be used for bases greater than 10. See the -<code>U</code> option.) </p>
<p> For functions, -<code>u</code> is the undefined attribute. See Sx Functions above for the implications of this. </p>
 </dd>
<dt><code>-x</code></dt>
<dd> <p> Export attribute. Parameters (or functions) are placed in the environment of any executed commands. Exported functions are not yet implemented. </p>
 </dd>
<dt><code>-Z </code>[<i>n</i> ] </dt>
<dd> <p> Zero fill attribute. If not combined with -<code>L</code> this is the same as -<code>R</code> except zero padding is used instead of space padding. For integers, the number instead of the base is padded. </p>
 </dd></dl>
<p> If any of the -<code>i</code> -<code>L</code> -<code>l</code> -<code>R</code> -<code>U</code> -<code>u</code> or -<code>Z</code> options are changed, all others from this set are cleared, unless they are also given on the same command line. </p>
<dt><code>ulimit</code> [-<code>aBCcdefHiLlMmnOPpqrSsTtVvw</code> ] [<i>value</i> ] </dt>
<dd>  </dd>
<dd> <p> Display or set process limits. If no options are used, the file size limit (-<code>f</code> ) is assumed. <i>value</i> if specified, may be either an arithmetic expression or the word ``unlimited&#8217;&#8216; The limits affect the shell and any processes created by the shell after a limit is imposed. Note that some systems may not allow limits to be increased once they are set. Also note that the types of limits available are system dependent --- some systems have only the -<code>f</code> limit. </p>
 </dd>
<dl>
<dt><code>-a</code></dt>
<dd> <p> Display all limits; unless -<code>H</code> is used, soft limits are displayed. </p>
 </dd>
<dt><code>-B </code><i>n</i></dt>
<dd> <p> Set the socket buffer size to <i>n</i> kibibytes. </p>
 </dd>
<dt><code>-C </code><i>n</i></dt>
<dd> <p> Set the number of cached threads to <i>n</i> </p>
 </dd>
<dt><code>-c </code><i>n</i></dt>
<dd> <p> Impose a size limit of <i>n</i> blocks on the size of core dumps. </p>
 </dd>
<dt><code>-d </code><i>n</i></dt>
<dd> <p> Impose a size limit of <i>n</i> kibibytes on the size of the data area. </p>
 </dd>
<dt><code>-e </code><i>n</i></dt>
<dd> <p> Set the maximum niceness to <i>n</i> </p>
 </dd>
<dt><code>-f </code><i>n</i></dt>
<dd> <p> Impose a size limit of <i>n</i> blocks on files written by the shell and its child processes (files of any size may be read). </p>
 </dd>
<dt><code>-H</code></dt>
<dd> <p> Set the hard limit only (the default is to set both hard and soft limits). </p>
 </dd>
<dt><code>-i </code><i>n</i></dt>
<dd> <p> Set the number of pending signals to <i>n</i> </p>
 </dd>
<dt><code>-L </code><i>n</i></dt>
<dd> <p> Control flocks; documentation is missing. </p>
 </dd>
<dt><code>-l </code><i>n</i></dt>
<dd> <p> Impose a limit of <i>n</i> kibibytes on the amount of locked (wired) physical memory. </p>
 </dd>
<dt><code>-M </code><i>n</i></dt>
<dd> <p> Set the AIO locked memory to <i>n</i> kibibytes. </p>
 </dd>
<dt><code>-m </code><i>n</i></dt>
<dd> <p> Impose a limit of <i>n</i> kibibytes on the amount of physical memory used. </p>
 </dd>
<dt><code>-n </code><i>n</i></dt>
<dd> <p> Impose a limit of <i>n</i> file descriptors that can be open at once. </p>
 </dd>
<dt><code>-O </code><i>n</i></dt>
<dd> <p> Set the number of AIO operations to <i>n</i> </p>
 </dd>
<dt><code>-P </code><i>n</i></dt>
<dd> <p> Limit the number of threads per process to <i>n</i> </p>
 </dd>
<dt><code>-p </code><i>n</i></dt>
<dd> <p> Impose a limit of <i>n</i> processes that can be run by the user at any one time. </p>
 </dd>
<dt><code>-q </code><i>n</i></dt>
<dd> <p> Limit the size of <code>POSIX</code> message queues to <i>n</i> bytes. </p>
 </dd>
<dt><code>-r </code><i>n</i></dt>
<dd> <p> Set the maximum real-time priority to <i>n</i> </p>
 </dd>
<dt><code>-S</code></dt>
<dd> <p> Set the soft limit only (the default is to set both hard and soft limits). </p>
 </dd>
<dt><code>-s </code><i>n</i></dt>
<dd> <p> Impose a size limit of <i>n</i> kibibytes on the size of the stack area. </p>
 </dd>
<dt><code>-T </code><i>n</i></dt>
<dd> <p> Impose a time limit of <i>n</i> real seconds to be used by each process. </p>
 </dd>
<dt><code>-t </code><i>n</i></dt>
<dd> <p> Impose a time limit of <i>n</i> CPU seconds spent in user mode to be used by each process. </p>
 </dd>
<dt><code>-V </code><i>n</i></dt>
<dd> <p> Set the number of vnode monitors on Haiku to <i>n</i> </p>
 </dd>
<dt><code>-v </code><i>n</i></dt>
<dd> <p> Impose a limit of <i>n</i> kibibytes on the amount of virtual memory (address space) used. </p>
 </dd>
<dt><code>-w </code><i>n</i></dt>
<dd> <p> Impose a limit of <i>n</i> kibibytes on the amount of swap space used. </p>
 </dd></dl>
<p> As far as <code>ulimit</code> is concerned, a block is 512 bytes. </p>
<dt><code>umask</code> [-<code>S</code> ] [<i>mask</i> ] </dt>
<dd>  </dd>
<dd> <p> Display or set the file permission creation mask, or umask (see <a href="/docs/linux/man/2-umask/">umask</a>(2)). If the -<code>S</code> option is used, the mask displayed or set is symbolic; otherwise, it is an octal number. </p>
<p> Symbolic masks are like those used by <a href="/docs/linux/man/1-chmod/">chmod</a>(1). When used, they describe what permissions may be made available (as opposed to octal masks in which a set bit means the corresponding bit is to be cleared). For example, ``ug=rwx,o=&#8216;&#8216; sets the mask so files will not be readable, writable, or executable by ``others&#8217;&#8216; and is equivalent (on most systems) to the octal mask ``007&#8217;&#8216; </p>
 </dd>
<dt><code>unalias</code> [-<code>adt</code> ] [<i>name ...</i> ] </dt>
<dd>  </dd>
<dd> <p> The aliases for the given names are removed. If the -<code>a</code> option is used, all aliases are removed. If the -<code>t</code> or -<code>d</code> options are used, the indicated operations are carried out on tracked or directory aliases, respectively. </p>
 </dd>
<dt><code>unset</code> [-<code>fv</code> ] <i>parameter ...</i></dt>
<dd>  </dd>
<dd> <p> Unset the named parameters Po -<code>v</code> the default Pc or functions (-<code>f</code> ) With <i>parameter </i><code>[*]</code> attributes are kept, only values are unset. </p>
<p> The exit status is non-zero if any of the parameters have the read-only attribute set, zero otherwise. </p>
 </dd>
<dt><code>wait </code>[<i>job ...</i> ] </dt>
<dd> <p> Wait for the specified job(s) to finish. The exit status of <code>wait</code> is that of the last specified job; if the last job is killed by a signal, the exit status is 128 + the number of the signal (see <code>kill -l </code><i>exit-status</i> above); if the last specified job can&#8217;t be found (because it never existed, or had already finished), the exit status of <code>wait</code> is 127. See Sx Job control below for the format of <i>job</i> <code>wait</code> will return if a signal for which a trap has been set is received, or if a <code>SIGHUP</code> <code>SIGINT</code> or <code>SIGQUIT</code> signal is received. </p>
<p> If no jobs are specified, <code>wait</code> waits for all currently running jobs (if any) to finish and exits with a zero status. If job monitoring is enabled, the completion status of jobs is printed (this is not the case when jobs are explicitly specified). </p>
 </dd>
<dt><code>whence</code> [-<code>pv</code> ] [<i>name ...</i> ] </dt>
<dd>  </dd>
<dd> <p> For each <i>name</i> the type of command is listed (reserved word, built-in, alias, function, tracked alias, or executable). If the -<code>p</code> option is used, a path search is performed even if <i>name</i> is a reserved word, alias, etc. Without the -<code>v</code> option, <code>whence</code> is similar to <code>command -v</code> except that <code>whence</code> will find reserved words and won&#8217;t print aliases as alias commands. With the -<code>v</code> option, <code>whence</code> is the same as <code>command -V</code> Note that for <code>whence</code> the -<code>p</code> option does not affect the search path used, as it does for <code>command</code> If the type of one or more of the names could not be determined, the exit status is non-zero. </p>
 </dd></dl>
<h3>Job control</h3>
<p> Job control refers to the shell&#8217;s ability to monitor and control jobs which are processes or groups of processes created for commands or pipelines. At a minimum, the shell keeps track of the status of the background (i.e. asynchronous) jobs that currently exist; this information can be displayed using the <code>jobs</code> commands. If job control is fully enabled (using <code>set -m</code> or <code>set -o monitor )</code> as it is for interactive shells, the processes of a job are placed in their own process group. Foreground jobs can be stopped by typing the suspend character from the terminal (normally ^Z), jobs can be restarted in either the foreground or background using the <code>fg</code> and <code>bg</code> commands, and the state of the terminal is saved or restored when a foreground job is stopped or restarted, respectively. </p>
<p> Note that only commands that create processes (e.g. asynchronous commands, subshell commands, and non-built-in, non-function commands) can be stopped; commands like <code>read</code> cannot be. </p>
<p> When a job is created, it is assigned a job number. For interactive shells, this number is printed inside ``[..]&#8216;&#8216; followed by the process IDs of the processes in the job when an asynchronous command is run. A job may be referred to in the <code>bg</code> <code>fg</code> <code>jobs</code> <code>kill</code> and <code>wait</code> commands either by the process ID of the last process in the command pipeline (as stored in the <code>$!</code> parameter) or by prefixing the job number with a percent sign (`%&#8216; ) Other percent sequences can also be used to refer to jobs: </p>
<dl>
<dt><code>%+ | %% |</code></dt>
<dd> <p> The most recently stopped job, or, if there are no stopped jobs, the oldest running job. </p>
 </dd>
<dt><code>%-</code></dt>
<dd> <p> The job that would be the <code>%+</code> job if the latter did not exist. </p>
 </dd>
<dt><code>% </code><i>n</i></dt>
<dd> <p> The job with job number <i>n</i> </p>
 </dd>
<dt><code>%? </code><i>string</i></dt>
<dd> <p> The job with its command containing the string <i>string</i> (an error occurs if multiple jobs are matched). </p>
 </dd>
<dt><code>% </code><i>string</i></dt>
<dd> <p> The job with its command starting with the string <i>string</i> (an error occurs if multiple jobs are matched). </p>
 </dd></dl>
<p> When a job changes state (e.g. a background job finishes or foreground job is stopped), the shell prints the following status information: </p>
<p> where... </p>
<dl>
<dt><i>number</i></dt>
<dd> <p> is the job number of the job; </p>
 </dd>
<dt><i>flag</i></dt>
<dd> <p> is the `+&#8216; or `-&#8216; character if the job is the <code>%+</code> or <code>%-</code> job, respectively, or space if it is neither; </p>
 </dd>
<dt><i>status</i></dt>
<dd> <p> indicates the current state of the job and can be: </p>
 </dd>
<dl>
<dt><code>Done </code>[<i>number</i> ] </dt>
<dd> <p> The job exited. <i>number</i> is the exit status of the job which is omitted if the status is zero. </p>
 </dd>
<dt><code>Running</code></dt>
<dd> <p> The job has neither stopped nor exited (note that running does not necessarily mean consuming CPU time --- the process could be blocked waiting for some event). </p>
 </dd>
<dt><code>Stopped </code>[<i>signal</i> ] </dt>
<dd> <p> The job was stopped by the indicated <i>signal</i> (if no signal is given, the job was stopped by <code>SIGTSTP )</code> </p>
 </dd>
<dt><i>signal-description </i>[``core dumped&#8217;&#8216; ] </dt>
<dd> <p> The job was killed by a signal (e.g. memory fault, hangup); use <code>kill -l</code> for a list of signal descriptions. The ``core dumped&#8217;&#8216; message indicates the process created a core file. </p>
 </dd></dl>
<dt><i>command</i></dt>
<dd> <p> is the command that created the process. If there are multiple processes in the job, each process will have a line showing its <i>command</i> and possibly its <i>status</i> if it is different from the status of the previous process. </p>
 </dd></dl>
<p> When an attempt is made to exit the shell while there are jobs in the stopped state, the shell warns the user that there are stopped jobs and does not exit. If another attempt is immediately made to exit the shell, the stopped jobs are sent a <code>SIGHUP</code> signal and the shell exits. Similarly, if the <code>nohup</code> option is not set and there are running jobs when an attempt is made to exit a login shell, the shell warns the user and does not exit. If another attempt is immediately made to exit the shell, the running jobs are sent a <code>SIGHUP</code> signal and the shell exits.  </p>
<h3>Interactive input line editing</h3>
<p> The shell supports three modes of reading command lines from a <a href="/docs/linux/man/4-tty/">tty</a>(4) in an interactive session, controlled by the <code>emacs</code> <code>gmacs</code> and <code>vi</code> options (at most one of these can be set at once). The default is <code>emacs</code> Editing modes can be set explicitly using the <code>set</code> built-in. If none of these options are enabled, the shell simply reads lines using the normal <a href="/docs/linux/man/4-tty/">tty</a>(4) driver. If the <code>emacs</code> or <code>gmacs</code> option is set, the shell allows emacs-like editing of the command; similarly, if the <code>vi</code> option is set, the shell allows vi-like editing of the command. These modes are described in detail in the following sections. </p>
<p> In these editing modes, if a line is longer than the screen width (see the <code>COLUMNS</code> parameter), a `&gt;&#8216; `+&#8216; , or `&lt;&#8216; character is displayed in the last column indicating that there are more characters after, before and after, or before the current position, respectively. The line is scrolled horizontally as necessary. </p>
<p> Completed lines are pushed into the history, unless they begin with an IFS octet or IFS white space, or are the same as the previous line.  </p>
<h3>Emacs editing mode</h3>
<p> When the <code>emacs</code> option is set, interactive input line editing is enabled. Warning: This mode is slightly different from the emacs mode in the original Korn shell. In this mode, various editing commands (typically bound to one or more control characters) cause immediate actions without waiting for a newline. Several editing commands are bound to particular control characters when the shell is invoked; these bindings can be changed using the <code>bind</code> command. </p>
<p> The following is a list of available editing commands. Each description starts with the name of the command, suffixed with a colon; an [<i>n</i> ] (if the command can be prefixed with a count); and any keys the command is bound to by default, written using caret notation e.g. the ASCII ESC character is written as ^[. These control sequences are not case sensitive. A count prefix for a command is entered using the sequence ^[ <i>n</i> where <i>n</i> is a sequence of 1 or more digits. Unless otherwise specified, if a count is omitted, it defaults to 1. </p>
<p> Note that editing command names are used only with the <code>bind</code> command. Furthermore, many editing commands are useful only on terminals with a visible cursor. The default bindings were chosen to resemble corresponding Emacs key bindings. The user&#8217;s <a href="/docs/linux/man/4-tty/">tty</a>(4) characters (e.g. <code>ERASE</code> are bound to reasonable substitutes and override the default bindings. </p>
<dl>
<dt><code>abort: ^C, ^G</code></dt>
<dd> <p> Abort the current command, empty the line buffer and set the exit state to interrupted. </p>
 </dd>
<dt><code>auto-insert: </code>[<i>n</i> ] </dt>
<dd> <p> Simply causes the character to appear as literal input. Most ordinary characters are bound to this. </p>
 </dd>
<dt><code> backward-char:</code> [<i>n</i> ] <code>^B , ^XD , ANSI-CurLeft</code></dt>
<dd>  </dd>
<dd> <p> Moves the cursor backward <i>n</i> characters. </p>
 </dd>
<dt><code> backward-word:</code> [<i>n</i> ] <code>^[b , ANSI-Ctrl-CurLeft , ANSI-Alt-CurLeft</code></dt>
<dd>  </dd>
<dd> <p> Moves the cursor backward to the beginning of the word; words consist of alphanumerics, underscore (`_&#8216; ) and dollar sign (`$&#8216; ) characters. </p>
 </dd>
<dt><code>beginning-of-history: ^[&lt;</code></dt>
<dd> <p> Moves to the beginning of the history. </p>
 </dd>
<dt><code>beginning-of-line: ^A, ANSI-Home</code></dt>
<dd> <p> Moves the cursor to the beginning of the edited input line. </p>
 </dd>
<dt><code> capitalise-word:</code> [<i>n</i> ] <code>^[C , ^[c</code></dt>
<dd>  </dd>
<dd> <p> Uppercase the first character in the next <i>n</i> words, leaving the cursor past the end of the last word. </p>
 </dd>
<dt><code>clear-screen: ^[^L</code></dt>
<dd> <p> Prints a compile-time configurable sequence to clear the screen and home the cursor, redraws the entire prompt and the currently edited input line. The default sequence works for almost all standard terminals. </p>
 </dd>
<dt><code>comment: ^[#</code></dt>
<dd> <p> If the current line does not begin with a comment character, one is added at the beginning of the line and the line is entered (as if return had been pressed); otherwise, the existing comment characters are removed and the cursor is placed at the beginning of the line. </p>
 </dd>
<dt><code>complete: ^[^[</code></dt>
<dd> <p> Automatically completes as much as is unique of the command name or the file name containing the cursor. If the entire remaining command or file name is unique, a space is printed after its completion, unless it is a directory name in which case `/&#8216; is appended. If there is no command or file name with the current partial word as its prefix, a bell character is output (usually causing a beep to be sounded). </p>
 </dd>
<dt><code>complete-command: ^X^[</code></dt>
<dd> <p> Automatically completes as much as is unique of the command name having the partial word up to the cursor as its prefix, as in the <code>complete</code> command above. </p>
 </dd>
<dt><code>complete-file: ^[^X</code></dt>
<dd> <p> Automatically completes as much as is unique of the file name having the partial word up to the cursor as its prefix, as in the <code>complete</code> command described above. </p>
 </dd>
<dt><code>complete-list: ^I, ^[=</code></dt>
<dd> <p> Complete as much as is possible of the current word, and list the possible completions for it. If only one completion is possible, match as in the <code>complete</code> command above. Note that ^I is usually generated by the TAB (tabulator) key. </p>
 </dd>
<dt><code> delete-char-backward:</code> [<i>n</i> ] <code>ERASE , ^? , ^H</code></dt>
<dd>  </dd>
<dd> <p> Deletes <i>n</i> characters before the cursor. </p>
 </dd>
<dt><code> delete-char-forward:</code> [<i>n</i> ] <code>ANSI-Del</code></dt>
<dd>  </dd>
<dd> <p> Deletes <i>n</i> characters after the cursor. </p>
 </dd>
<dt><code> delete-word-backward:</code> [<i>n</i> ] <code>WERASE , ^[^? , ^[^H , ^[h</code></dt>
<dd>  </dd>
<dd> <p> Deletes <i>n</i> words before the cursor. </p>
 </dd>
<dt><code> delete-word-forward:</code> [<i>n</i> ] <code>^[d</code></dt>
<dd>  </dd>
<dd> <p> Deletes characters after the cursor up to the end of <i>n</i> words. </p>
 </dd>
<dt><code> down-history:</code> [<i>n</i> ] <code>^N , ^XB , ANSI-CurDown</code></dt>
<dd>  </dd>
<dd> <p> Scrolls the history buffer forward <i>n</i> lines (later). Each input line originally starts just after the last entry in the history buffer, so <code>down-history</code> is not useful until either <code>search-history</code> <code>search-history-up</code> or <code>up-history</code> has been performed. </p>
 </dd>
<dt><code> downcase-word:</code> [<i>n</i> ] <code>^[L , ^[l</code></dt>
<dd>  </dd>
<dd> <p> Lowercases the next <i>n</i> words. </p>
 </dd>
<dt><code> edit-line:</code> [<i>n</i> ] <code>^Xe </code></dt>
<dd>  </dd>
<dd> <p> Edit line <i>n</i> or the current line, if not specified, interactively. The actual command executed is <code>fc -e ${VISUAL:-${EDITOR:-vi}} </code><i>n</i> </p>
 </dd>
<dt><code>end-of-history: ^[&gt;</code></dt>
<dd> <p> Moves to the end of the history. </p>
 </dd>
<dt><code>end-of-line: ^E, ANSI-End</code></dt>
<dd> <p> Moves the cursor to the end of the input line. </p>
 </dd>
<dt><code>eot: ^_</code></dt>
<dd> <p> Acts as an end-of-file; this is useful because edit-mode input disables normal terminal input canonicalization. </p>
 </dd>
<dt><code> eot-or-delete:</code> [<i>n</i> ] <code>^D</code></dt>
<dd>  </dd>
<dd> <p> Acts as <code>eot</code> if alone on a line; otherwise acts as <code>delete-char-forward</code> </p>
 </dd>
<dt><code>error: (not bound)</code></dt>
<dd> <p> Error (ring the bell). </p>
 </dd>
<dt><code>exchange-point-and-mark: ^X^X</code></dt>
<dd> <p> Places the cursor where the mark is and sets the mark to where the cursor was. </p>
 </dd>
<dt><code>expand-file: ^[*</code></dt>
<dd> <p> Appends a `*&#8216; to the current word and replaces the word with the result of performing file globbing on the word. If no files match the pattern, the bell is rung. </p>
 </dd>
<dt><code> forward-char:</code> [<i>n</i> ] <code>^F , ^XC , ANSI-CurRight</code></dt>
<dd>  </dd>
<dd> <p> Moves the cursor forward <i>n</i> characters. </p>
 </dd>
<dt><code> forward-word:</code> [<i>n</i> ] <code>^[f , ANSI-Ctrl-CurRight , ANSI-Alt-CurRight</code></dt>
<dd>  </dd>
<dd> <p> Moves the cursor forward to the end of the <i>n </i><code>th</code> word. </p>
 </dd>
<dt><code> goto-history:</code> [<i>n</i> ] <code>^[g</code></dt>
<dd>  </dd>
<dd> <p> Goes to history number <i>n</i> </p>
 </dd>
<dt><code>kill-line: KILL</code></dt>
<dd> <p> Deletes the entire input line. </p>
 </dd>
<dt><code>kill-region: ^W</code></dt>
<dd> <p> Deletes the input between the cursor and the mark. </p>
 </dd>
<dt><code> kill-to-eol:</code> [<i>n</i> ] <code>^K</code></dt>
<dd>  </dd>
<dd> <p> Deletes the input from the cursor to the end of the line if <i>n</i> is not specified; otherwise deletes characters between the cursor and column <i>n</i> </p>
 </dd>
<dt><code>list: ^[?</code></dt>
<dd> <p> Prints a sorted, columnated list of command names or file names (if any) that can complete the partial word containing the cursor. Directory names have `/&#8216; appended to them. </p>
 </dd>
<dt><code>list-command: ^X?</code></dt>
<dd> <p> Prints a sorted, columnated list of command names (if any) that can complete the partial word containing the cursor. </p>
 </dd>
<dt><code>list-file: ^X^Y</code></dt>
<dd> <p> Prints a sorted, columnated list of file names (if any) that can complete the partial word containing the cursor. File type indicators are appended as described under <code>list</code> above. </p>
 </dd>
<dt><code>newline: ^J , ^M</code></dt>
<dd> <p> Causes the current input line to be processed by the shell. The current cursor position may be anywhere on the line. </p>
 </dd>
<dt><code>newline-and-next: ^O</code></dt>
<dd> <p> Causes the current input line to be processed by the shell, and the next line from history becomes the current line. This is only useful after an <code>up-history</code> <code>search-history</code> or <code>search-history-up</code> </p>
 </dd>
<dt><code>no-op: QUIT</code></dt>
<dd> <p> This does nothing. </p>
 </dd>
<dt><code>prefix-1: ^[</code></dt>
<dd> <p> Introduces a 2-character command sequence. </p>
 </dd>
<dt><code>prefix-2: ^X , ^[[ , ^[O</code></dt>
<dd> <p> Introduces a 2-character command sequence. </p>
 </dd>
<dt><code> prev-hist-word:</code> [<i>n</i> ] <code>^[. , ^[_</code></dt>
<dd>  </dd>
<dd> <p> The last word, or, if given, the <i>n </i><code>th</code> word (zero-based) of the previous (on repeated execution, second-last, third-last, etc.) command is inserted at the cursor. Use of this editing command trashes the mark. </p>
 </dd>
<dt><code>quote: ^^ , ^V</code></dt>
<dd> <p> The following character is taken literally rather than as an editing command. </p>
 </dd>
<dt><code>redraw: ^L</code></dt>
<dd> <p> Reprints the last line of the prompt string and the current input line on a new line. </p>
 </dd>
<dt><code> search-character-backward:</code> [<i>n</i> ] <code>^[^]</code></dt>
<dd>  </dd>
<dd> <p> Search backward in the current line for the <i>n </i><code>th</code> occurrence of the next character typed. </p>
 </dd>
<dt><code> search-character-forward:</code> [<i>n</i> ] <code>^]</code></dt>
<dd>  </dd>
<dd> <p> Search forward in the current line for the <i>n </i><code>th</code> occurrence of the next character typed. </p>
 </dd>
<dt><code>search-history: ^R</code></dt>
<dd> <p> Enter incremental search mode. The internal history list is searched backwards for commands matching the input. An initial `^&#8216; in the search string anchors the search. The escape key will leave search mode. Other commands, including sequences of escape as <code>prefix-1</code> followed by a <code>prefix-1</code> or <code>prefix-2</code> key will be executed after leaving search mode. The <code>abort (^G) </code> command will restore the input line before search started. Successive <code>search-history</code> commands continue searching backward to the next previous occurrence of the pattern. The history buffer retains only a finite number of lines; the oldest are discarded as necessary. </p>
 </dd>
<dt><code>search-history-up: ANSI-PgUp </code>Search backwards through the history buffer for commands whose beginning match </dt>
<dd> <p> the portion of the input line before the cursor. When used on an empty line, this has the same effect as <code>up-history</code> </p>
 </dd>
<dt><code>search-history-down: ANSI-PgDn </code>Search forwards through the history buffer for commands whose beginning match </dt>
<dd> <p> the portion of the input line before the cursor. When used on an empty line, this has the same effect as <code>down-history</code> This is only useful after an <code>up-history</code> <code>search-history</code> or <code>search-history-up</code> </p>
 </dd>
<dt><code>set-mark-command: ^[ Aq </code>space </dt>
<dd> <p> Set the mark at the cursor position. </p>
 </dd>
<dt><code>transpose-chars: ^T</code></dt>
<dd> <p> If at the end of line, or if the <code>gmacs</code> option is set, this exchanges the two previous characters; otherwise, it exchanges the previous and current characters and moves the cursor one character to the right. </p>
 </dd>
<dt><code> up-history:</code> [<i>n</i> ] <code>^P , ^XA , ANSI-CurUp </code></dt>
<dd>  </dd>
<dd> <p> Scrolls the history buffer backward <i>n</i> lines (earlier). </p>
 </dd>
<dt><code> upcase-word:</code> [<i>n</i> ] <code>^[U , ^[u</code></dt>
<dd>  </dd>
<dd> <p> Uppercase the next <i>n</i> words. </p>
 </dd>
<dt><code>version: ^[^V</code></dt>
<dd> <p> Display the version of <code>mksh</code> The current edit buffer is restored as soon as a key is pressed. The restoring keypress is processed, unless it is a space. </p>
 </dd>
<dt><code>yank: ^Y</code></dt>
<dd> <p> Inserts the most recently killed text string at the current cursor position. </p>
 </dd>
<dt><code>yank-pop: ^[y</code></dt>
<dd> <p> Immediately after a <code>yank</code> replaces the inserted text string with the next previously killed text string. </p>
 </dd></dl>
<h3>Vi editing mode</h3>
<p> <i>Note:</i> The vi command-line editing mode is orphaned, yet still functional. </p>
<p> The vi command-line editor in has basically the same commands as the <a href="/docs/linux/man/1-vi/">vi</a>(1) editor with the following exceptions: </p>
<ul>
<li> <p> You start out in insert mode.  </li>
<li>  There are file name and command completion commands: =, \, *, ^X, ^E, ^F, and, optionally, Aq tab and Aq esc .  </li>
<li>  The <code>_</code> command is different (in <code>mksh</code> it is the last argument command; in <a href="/docs/linux/man/1-vi/">vi</a>(1) it goes to the start of the current line).  </li>
<li>  The <code>/</code> and <code>G</code> commands move in the opposite direction to the <code>j</code> command.  </li>
<li>  Commands which don&#8217;t make sense in a single line editor are not available (e.g. screen movement commands and <a href="/docs/linux/man/1-ex/">ex</a>(1)Ns-style colon (<code>:</code> ) commands).  </li>
</ul>
 </p>
<p> Like <a href="/docs/linux/man/1-vi/">vi</a>(1), there are two modes: ``insert&#8217;&#8216; mode and ``command&#8217;&#8216; mode. In insert mode, most characters are simply put in the buffer at the current cursor position as they are typed; however, some characters are treated specially. In particular, the following characters are taken from current <a href="/docs/linux/man/4-tty/">tty</a>(4) settings (see <a href="/docs/linux/man/1-stty/">stty</a>(1)) and have their usual meaning (normal values are in parentheses): kill (^U), erase (^?), werase (^W), eof (^D), intr (^C), and quit (^\). In addition to the above, the following characters are also treated specially in insert mode: </p>
<dl>
<dt><code>^E</code></dt>
<dd> <p> Command and file name enumeration (see below). </p>
 </dd>
<dt><code>^F</code></dt>
<dd> <p> Command and file name completion (see below). If used twice in a row, the list of possible completions is displayed; if used a third time, the completion is undone. </p>
 </dd>
<dt><code>^H</code></dt>
<dd> <p> Erases previous character. </p>
 </dd>
<dt><code>^J | ^M</code></dt>
<dd> <p> End of line. The current line is read, parsed, and executed by the shell. </p>
 </dd>
<dt><code>^V</code></dt>
<dd> <p> Literal next. The next character typed is not treated specially (can be used to insert the characters being described here). </p>
 </dd>
<dt><code>^X</code></dt>
<dd> <p> Command and file name expansion (see below). </p>
 </dd>
<dt><code>Aq </code>esc </dt>
<dd> <p> Puts the editor in command mode (see below). </p>
 </dd>
<dt><code>Aq </code>tab </dt>
<dd> <p> Optional file name and command completion (see <code>^F</code> above), enabled with <code>set -o vi-tabcomplete</code> </p>
 </dd></dl>
<p> In command mode, each character is interpreted as a command. Characters that don&#8217;t correspond to commands, are illegal combinations of commands, or are commands that can&#8217;t be carried out, all cause beeps. In the following command descriptions, an [<i>n</i> ] indicates the command may be prefixed by a number (e.g. <code>10l</code> moves right 10 characters); if no number prefix is used, <i>n</i> is assumed to be 1 unless otherwise specified. The term ``current position&#8217;&#8216; refers to the position between the cursor and the character preceding the cursor. A ``word&#8217;&#8216; is a sequence of letters, digits, and underscore characters or a sequence of non-letter, non-digit, non-underscore, and non-whitespace characters (e.g. ``ab2*&amp;^&#8216;&#8216; contains two words) and a ``big-word&#8217;&#8216; is a sequence of non-whitespace characters. </p>
<p> Special vi commands: </p>
<p> The following commands are not in, or are different from, the normal vi file editor: </p>
<dl>
<dt> [<i>n </i><code>_</code> ] </dt>
<dd>  </dd>
<dd> <p> Insert a space followed by the <i>n </i><code>th</code> big-word from the last command in the history at the current position and enter insert mode; if <i>n</i> is not specified, the last word is inserted. </p>
 </dd>
<dt><code>#</code></dt>
<dd> <p> Insert the comment character (`#&#8216; ) at the start of the current line and return the line to the shell (equivalent to <code>I#^J )</code> </p>
 </dd>
<dt> [<i>n </i><code>g</code> ] </dt>
<dd>  </dd>
<dd> <p> Like <code>G</code> except if <i>n</i> is not specified, it goes to the most recent remembered line. </p>
 </dd>
<dt> [<i>n </i><code>v</code> ] </dt>
<dd>  </dd>
<dd> <p> Edit line <i>n</i> using the <a href="/docs/linux/man/1-vi/">vi</a>(1) editor; if <i>n</i> is not specified, the current line is edited. The actual command executed is <code>fc -e ${VISUAL:-${EDITOR:-vi}} </code><i>n</i> </p>
 </dd>
<dt><code>* and ^X</code></dt>
<dd> <p> Command or file name expansion is applied to the current big-word (with an appended `*&#8216; if the word contains no file globbing characters) --- the big-word is replaced with the resulting words. If the current big-word is the first on the line or follows one of the characters `;&#8216; , `|&#8216; `&amp;&#8216; , `(&#8216; , or `)&#8216; , and does not contain a slash (`/&#8216; ) then command expansion is done; otherwise file name expansion is done. Command expansion will match the big-word against all aliases, functions, and built-in commands as well as any executable files found by searching the directories in the <code>PATH</code> parameter. File name expansion matches the big-word against the files in the current directory. After expansion, the cursor is placed just past the last word and the editor is in insert mode. </p>
 </dd>
<dt> [<i>n </i><code>\</code> ] [<i>n </i><code>^F</code> ] [<i>n </i><code>Aq </code>tab ] <code>and</code> [<i>n </i><code>Aq </code>esc ] </dt>
<dd>  </dd>
<dd> <p> Command/file name completion. Replace the current big-word with the longest unique match obtained after performing command and file name expansion. Aq tab is only recognised if the <code>vi-tabcomplete</code> option is set, while Aq esc is only recognised if the <code>vi-esccomplete</code> option is set (see <code>set -o )</code> If <i>n</i> is specified, the <i>n </i><code>th</code> possible completion is selected (as reported by the command/file name enumeration command). </p>
 </dd>
<dt><code>= and ^E</code></dt>
<dd> <p> Command/file name enumeration. List all the commands or files that match the current big-word. </p>
 </dd>
<dt><code>^V</code></dt>
<dd> <p> Display the version of <code>mksh</code> The current edit buffer is restored as soon as a key is pressed. The restoring keypress is ignored. </p>
 </dd>
<dt><code>@ </code><i>c</i></dt>
<dd> <p> Macro expansion. Execute the commands found in the alias <i>c</i> </p>
 </dd></dl>
<p> Intra-line movement commands: </p>
<dl>
<dt> [<i>n </i><code>h and</code> ] [<i>n </i><code>^H</code> ] </dt>
<dd>  </dd>
<dd> <p> Move left <i>n</i> characters. </p>
 </dd>
<dt> [<i>n </i><code>l and</code> ] [<i>n </i><code>Aq </code>space ] </dt>
<dd>  </dd>
<dd> <p> Move right <i>n</i> characters. </p>
 </dd>
<dt><code>0</code></dt>
<dd> <p> Move to column 0. </p>
 </dd>
<dt><code>^</code></dt>
<dd> <p> Move to the first non-whitespace character. </p>
 </dd>
<dt> [<i>n </i><code>|</code> ] </dt>
<dd>  </dd>
<dd> <p> Move to column <i>n</i> </p>
 </dd>
<dt><code>$</code></dt>
<dd> <p> Move to the last character. </p>
 </dd>
<dt> [<i>n </i><code>b</code> ] </dt>
<dd>  </dd>
<dd> <p> Move back <i>n</i> words. </p>
 </dd>
<dt> [<i>n </i><code>B</code> ] </dt>
<dd>  </dd>
<dd> <p> Move back <i>n</i> big-words. </p>
 </dd>
<dt> [<i>n </i><code>e</code> ] </dt>
<dd>  </dd>
<dd> <p> Move forward to the end of the word, <i>n</i> times. </p>
 </dd>
<dt> [<i>n </i><code>E</code> ] </dt>
<dd>  </dd>
<dd> <p> Move forward to the end of the big-word, <i>n</i> times. </p>
 </dd>
<dt> [<i>n </i><code>w</code> ] </dt>
<dd>  </dd>
<dd> <p> Move forward <i>n</i> words. </p>
 </dd>
<dt> [<i>n </i><code>W</code> ] </dt>
<dd>  </dd>
<dd> <p> Move forward <i>n</i> big-words. </p>
 </dd>
<dt><code>%</code></dt>
<dd> <p> Find match. The editor looks forward for the nearest parenthesis, bracket, or brace and then moves the cursor to the matching parenthesis, bracket, or brace. </p>
 </dd>
<dt> [<i>n </i><code>f </code><i>c</i> ] </dt>
<dd>  </dd>
<dd> <p> Move forward to the <i>n </i><code>th</code> occurrence of the character <i>c</i> </p>
 </dd>
<dt> [<i>n </i><code>F </code><i>c</i> ] </dt>
<dd>  </dd>
<dd> <p> Move backward to the <i>n </i><code>th</code> occurrence of the character <i>c</i> </p>
 </dd>
<dt> [<i>n </i><code>t </code><i>c</i> ] </dt>
<dd>  </dd>
<dd> <p> Move forward to just before the <i>n </i><code>th</code> occurrence of the character <i>c</i> </p>
 </dd>
<dt> [<i>n </i><code>T </code><i>c</i> ] </dt>
<dd>  </dd>
<dd> <p> Move backward to just before the <i>n </i><code>th</code> occurrence of the character <i>c</i> </p>
 </dd>
<dt> [<i>n </i><code>;</code> ] </dt>
<dd>  </dd>
<dd> <p> Repeats the last <code>f , F , t</code> or <code>T</code> command. </p>
 </dd>
<dt> [<i>n </i><code>,</code> ] </dt>
<dd>  </dd>
<dd> <p> Repeats the last <code>f , F , t</code> or <code>T</code> command, but moves in the opposite direction. </p>
 </dd></dl>
<p> Inter-line movement commands: </p>
<dl>
<dt> [<i>n </i><code>j</code> ] [<i>n </i><code>+</code> ] <code>and</code> [<i>n </i><code>^N</code> ] </dt>
<dd>  </dd>
<dd> <p> Move to the <i>n </i><code>th</code> next line in the history. </p>
 </dd>
<dt> [<i>n </i><code>k</code> ] [<i>n </i><code>-</code> ] <code>and</code> [<i>n </i><code>^P</code> ] </dt>
<dd>  </dd>
<dd> <p> Move to the <i>n </i><code>th</code> previous line in the history. </p>
 </dd>
<dt> [<i>n </i><code>G</code> ] </dt>
<dd>  </dd>
<dd> <p> Move to line <i>n</i> in the history; if <i>n</i> is not specified, the number of the first remembered line is used. </p>
 </dd>
<dt> [<i>n </i><code>g</code> ] </dt>
<dd>  </dd>
<dd> <p> Like <code>G</code> except if <i>n</i> is not specified, it goes to the most recent remembered line. </p>
 </dd>
<dt> [<i>n </i><code>/ </code><i>string</i> ] </dt>
<dd>  </dd>
<dd> <p> Search backward through the history for the <i>n </i><code>th</code> line containing <i>string</i> if <i>string</i> starts with `^&#8216; , the remainder of the string must appear at the start of the history line for it to match. </p>
 </dd>
<dt> [<i>n </i><code>? </code><i>string</i> ] </dt>
<dd>  </dd>
<dd> <p> Same as <code>/</code> except it searches forward through the history. </p>
 </dd>
<dt> [<i>n </i><code>n</code> ] </dt>
<dd>  </dd>
<dd> <p> Search for the <i>n </i><code>th</code> occurrence of the last search string; the direction of the search is the same as the last search. </p>
 </dd>
<dt> [<i>n </i><code>N</code> ] </dt>
<dd>  </dd>
<dd> <p> Search for the <i>n </i><code>th</code> occurrence of the last search string; the direction of the search is the opposite of the last search. </p>
 </dd>
<dt><i>ANSI-CurUp </i>Take the characters from the beginning of the line to the current </dt>
<dd> <p> cursor position as search string and do a backwards history search for lines beginning with this string; keep the cursor position. This works only in insert mode and keeps it enabled. </p>
 </dd></dl>
<p> Edit commands </p>
<dl>
<dt> [<i>n </i><code>a</code> ] </dt>
<dd>  </dd>
<dd> <p> Append text <i>n</i> times; goes into insert mode just after the current position. The append is only replicated if command mode is re-entered i.e. Aq esc is used. </p>
 </dd>
<dt> [<i>n </i><code>A</code> ] </dt>
<dd>  </dd>
<dd> <p> Same as <code>a</code> except it appends at the end of the line. </p>
 </dd>
<dt> [<i>n </i><code>i</code> ] </dt>
<dd>  </dd>
<dd> <p> Insert text <i>n</i> times; goes into insert mode at the current position. The insertion is only replicated if command mode is re-entered i.e. Aq esc is used. </p>
 </dd>
<dt> [<i>n </i><code>I</code> ] </dt>
<dd>  </dd>
<dd> <p> Same as <code>i</code> except the insertion is done just before the first non-blank character. </p>
 </dd>
<dt> [<i>n </i><code>s</code> ] </dt>
<dd>  </dd>
<dd> <p> Substitute the next <i>n</i> characters (i.e. delete the characters and go into insert mode). </p>
 </dd>
<dt><code>S</code></dt>
<dd> <p> Substitute whole line. All characters from the first non-blank character to the end of the line are deleted and insert mode is entered. </p>
 </dd>
<dt> [<i>n </i><code>c </code><i>move-cmd</i> ] </dt>
<dd>  </dd>
<dd> <p> Change from the current position to the position resulting from <i>n move-cmd </i><code>s</code> (i.e. delete the indicated region and go into insert mode); if <i>move-cmd</i> is <code>c</code> the line starting from the first non-blank character is changed. </p>
 </dd>
<dt><code>C</code></dt>
<dd> <p> Change from the current position to the end of the line (i.e. delete to the end of the line and go into insert mode). </p>
 </dd>
<dt> [<i>n </i><code>x</code> ] </dt>
<dd>  </dd>
<dd> <p> Delete the next <i>n</i> characters. </p>
 </dd>
<dt> [<i>n </i><code>X</code> ] </dt>
<dd>  </dd>
<dd> <p> Delete the previous <i>n</i> characters. </p>
 </dd>
<dt><code>D</code></dt>
<dd> <p> Delete to the end of the line. </p>
 </dd>
<dt> [<i>n </i><code>d </code><i>move-cmd</i> ] </dt>
<dd>  </dd>
<dd> <p> Delete from the current position to the position resulting from <i>n move-cmd </i><code>s</code> <i>move-cmd</i> is a movement command (see above) or <code>d</code> in which case the current line is deleted. </p>
 </dd>
<dt> [<i>n </i><code>r </code><i>c</i> ] </dt>
<dd>  </dd>
<dd> <p> Replace the next <i>n</i> characters with the character <i>c</i> </p>
 </dd>
<dt> [<i>n </i><code>R</code> ] </dt>
<dd>  </dd>
<dd> <p> Replace. Enter insert mode but overwrite existing characters instead of inserting before existing characters. The replacement is repeated <i>n</i> times. </p>
 </dd>
<dt> [<i>n </i><code>~</code> ] </dt>
<dd>  </dd>
<dd> <p> Change the case of the next <i>n</i> characters. </p>
 </dd>
<dt> [<i>n </i><code>y </code><i>move-cmd</i> ] </dt>
<dd>  </dd>
<dd> <p> Yank from the current position to the position resulting from <i>n move-cmd </i><code>s</code> into the yank buffer; if <i>move-cmd</i> is <code>y</code> the whole line is yanked. </p>
 </dd>
<dt><code>Y</code></dt>
<dd> <p> Yank from the current position to the end of the line. </p>
 </dd>
<dt> [<i>n </i><code>p</code> ] </dt>
<dd>  </dd>
<dd> <p> Paste the contents of the yank buffer just after the current position, <i>n</i> times. </p>
 </dd>
<dt> [<i>n </i><code>P</code> ] </dt>
<dd>  </dd>
<dd> <p> Same as <code>p</code> except the buffer is pasted at the current position. </p>
 </dd></dl>
<p> Miscellaneous vi commands </p>
<dl>
<dt><code>^J and ^M</code></dt>
<dd> <p> The current line is read, parsed, and executed by the shell. </p>
 </dd>
<dt><code>^L and ^R</code></dt>
<dd> <p> Redraw the current line. </p>
 </dd>
<dt> [<i>n </i><code>.</code> ] </dt>
<dd>  </dd>
<dd> <p> Redo the last edit command <i>n</i> times. </p>
 </dd>
<dt><code>u</code></dt>
<dd> <p> Undo the last edit command. </p>
 </dd>
<dt><code>U</code></dt>
<dd> <p> Undo all changes that have been made to the current line. </p>
 </dd>
<dt><i>intr </i><code>and </code><i>quit</i></dt>
<dd> <p> The interrupt and quit terminal characters cause the current line to be deleted and a new prompt to be printed. </p>
 </dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.mkshrc </code></dt>
<dd> <p> User mkshrc profile (non-privileged interactive shells); see Sx Startup files. The location can be changed at compile time (for embedded systems); AOSP Android builds use /system/etc/mkshrc </p>
 </dd>
<dt><code>~/.profile </code></dt>
<dd> <p> User profile (non-privileged login shells); see Sx Startup files near the top of this manual. </p>
 </dd>
<dt><code>/etc/profile </code></dt>
<dd> <p> System profile (login shells); see Sx Startup files. </p>
 </dd>
<dt><code>/etc/shells </code></dt>
<dd> <p> Shell database. </p>
 </dd>
<dt><code>/etc/suid_profile </code></dt>
<dd> <p> Suid profile (privileged shells); see Sx Startup files. </p>
 </dd></dl>
<p> Note: On Android, /system/etc/ contains the system and suid profile.  </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-awk/">awk</a>(1), <a href="/docs/linux/man/1-cat/">cat</a>(1), <a href="/docs/linux/man/1-ed/">ed</a>(1), <a href="/docs/linux/man/1-getopt/">getopt</a>(1), <a href="/docs/linux/man/1-sed/">sed</a>(1), <a href="/docs/linux/man/1-sh/">sh</a>(1), <a href="/docs/linux/man/1-stty/">stty</a>(1), <a href="/docs/linux/man/2-dup/">dup</a>(2), <a href="/docs/linux/man/2-execve/">execve</a>(2), <a href="/docs/linux/man/2-getgid/">getgid</a>(2), <a href="/docs/linux/man/2-getuid/">getuid</a>(2), <a href="/docs/linux/man/2-mknod/">mknod</a>(2), mkfifo(2), <a href="/docs/linux/man/2-open/">open</a>(2), <a href="/docs/linux/man/2-pipe/">pipe</a>(2), <a href="/docs/linux/man/2-rename/">rename</a>(2), <a href="/docs/linux/man/2-wait/">wait</a>(2), <a href="/docs/linux/man/3-getopt/">getopt</a>(3), nl_langinfo3, <a href="/docs/linux/man/3-setlocale/">setlocale</a>(3), signal(3), <a href="/docs/linux/man/3-system/">system</a>(3), <a href="/docs/linux/man/4-tty/">tty</a>(4), <a href="/docs/linux/man/5-shells/">shells</a>(5), <a href="/docs/linux/man/7-environ/">environ</a>(7), script(7), utf-87, mknod(8) </p>
<p> <a rel="nofollow" href="http://docsrv.sco.com:507/en/man/html.C/sh.C.html">http://docsrv.sco.com:507/en/man/html.C/sh.C.html</a> </p>
<p> <a rel="nofollow" href="https://www.mirbsd.org/ksh-chan.htm">https://www.mirbsd.org/ksh-chan.htm</a> </p>
<dl>
<dd> <p> Morris Bolsky <i>&quot;The KornShell Command and Programming Language&quot;</i> 1989 &quot;xvi&nbsp;<wbr>+&nbsp;<wbr>356 pages&quot; &quot;ISBN 978-0-13-516972-8 (0-13-516972-0)&quot; </p>
 </dd></dl>
<dl>
<dd> <p> Morris I. Bolsky David G. Korn <i>&quot;The New KornShell Command and Programming Language (2nd Edition)&quot;</i> 1995 &quot;xvi&nbsp;<wbr>+&nbsp;<wbr>400 pages&quot; &quot;ISBN 978-0-13-182700-4 (0-13-182700-6)&quot; </p>
 </dd></dl>
<dl>
<dd> <p> Stephen G. Kochan Patrick H. Wood <i>&quot;\*(tNUNIX\*(sP Shell Programming&quot;</i> &quot;Revised Edition&quot; 1990 &quot;xi&nbsp;<wbr>+&nbsp;<wbr>490 pages&quot; &quot;ISBN 978-0-672-48448-3 (0-672-48448-X)&quot; </p>
 </dd></dl>
<dl>
<dd> <p> &quot;IEEE Inc.&quot; <i>&quot;\*(tNIEEE\*(sP Standard for Information Technology --- Portable Operating System Interface (POSIX)&quot;</i> &quot;Part 2: Shell and Utilities&quot; 1993 &quot;xvii&nbsp;<wbr>+&nbsp;<wbr>1195 pages&quot; &quot;ISBN 978-1-55937-255-8 (1-55937-255-9)&quot; </p>
 </dd></dl>
<dl>
<dd> <p> Bill Rosenblatt <i>&quot;Learning the Korn Shell&quot;</i> 1993 &quot;360 pages&quot; &quot;ISBN 978-1-56592-054-5 (1-56592-054-6)&quot; </p>
 </dd></dl>
<dl>
<dd> <p> Bill Rosenblatt Arnold Robbins <i>&quot;Learning the Korn Shell, Second Edition&quot;</i> 2002 &quot;432 pages&quot; &quot;ISBN 978-0-596-00195-7 (0-596-00195-9)&quot; </p>
 </dd></dl>
<dl>
<dd> <p> Barry Rosenberg <i>&quot;KornShell Programming Tutorial&quot;</i> 1991 &quot;xxi&nbsp;<wbr>+&nbsp;<wbr>324 pages&quot; &quot;ISBN 978-0-201-56324-5 (0-201-56324-X)&quot; </p>
 </dd></dl>
<h2>AUTHORS</h2>
<p> <code>The MirBSD Korn Shell</code> is developed by An Thorsten Glaser Aq tg [at] mirbsd.org and currently maintained as part of The MirOS Project. This shell is based upon the Public Domain Korn SHell. The developer of mksh recognises the efforts of the pdksh authors, who had dedicated their work into Public Domain, our users, and all contributors, such as the Debian and OpenBSD projects. See the documentation, CVS, and web site for details.  </p>
<h2>CAVEATS</h2>
<p> only supports the Unicode BMP (Basic Multilingual Plane). </p>
<p> has a different scope model from AT&amp;T System <code>ksh</code> which leads to subtile differences in semantics for identical builtins. This can cause issues with a <code>nameref</code> to suddenly point to a local variable by accident; fixing this is hard. </p>
<p> The parts of a pipeline, like below, are executed in subshells. Thus, variable assignments inside them fail. Use co-processes instead. </p>
<blockquote><pre><code>foo | bar | read baz # will not change $baz
foo | bar |&amp; read -p baz # will, however, do so
</code></pre>
</blockquote>
<p> <code>mksh</code> provides a consistent set of 32-bit integer arithmetics, both signed and unsigned, with defined wraparound and sign of the result of a modulo operation, even (defying POSIX) on 64-bit systems. If you require 64-bit integer arithmetics, use <code>lksh (legacy mksh) </code> instead, but be aware that, in POSIX, it&#8217;s legal for the OS to make <code>print $((2147483647 + 1))</code> delete all files on your system, as it&#8217;s Undefined Behaviour.  </p>
<h2>BUGS</h2>
<p> Suspending (using ^Z) pipelines like the one below will only suspend the currently running part of the pipeline; in this example, ``fubar&#8217;&#8216; is immediately printed on suspension (but not later after an <code>fg )</code> </p>
<blockquote><pre><code>$ /bin/sleep 666 &amp;&amp; echo fubar
</code></pre>
</blockquote>
<p> This document attempts to describe <code>mksh R46</code> and up, compiled without any options impacting functionality, such as <code>MKSH_SMALL</code> when not called as /bin/sh which, on some systems only, enables <code>set -o sh</code> automatically (whose behaviour differs across targets), for an operating environment supporting all of its advanced needs. Please report bugs in to the MirOS mailing list at Aq miros-mksh [at] mirbsd.org or in the <code>#!/bin/mksh</code> (or <code>#ksh</code> ) IRC channel at irc.freenode.net (Port 6697 SSL, 6667 unencrypted) or at: <a rel="nofollow" href="https://launchpad.net/mksh">https://launchpad.net/mksh</a> </p>
