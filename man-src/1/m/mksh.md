---
title: "mksh(1)"
name: "mksh"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mksh/"
description: "mksh sh – MirBSD Korn shell"
---

<h2 class="name">NAME</h2>
<p> <code>mksh</code> <code>sh</code> &#8211; MirBSD Korn shell </p>
<h2>SYNOPSIS</h2>
<p> -words [-<code>+abCefhiklmnprUuvXx </code>[-<code>T </code><i>/dev/ttyCn </i>| &#8211; ] ] [-<code>+o </code><i>option</i> ] [-<code>c </code><i>string |</i> &#8211;<code>s |</code> <i>file</i> [<i>argument &#8230;</i> ] ]<br />
<code>builtin-name</code> [<i>argument &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> is a command interpreter intended for both interactive and shell script use. Its command language is a superset of the shC shell language and largely compatible to the original Korn shell.</p>
<h3>I&#8217;m an Android user, so what&#8217;s mksh?</h3>
<p> <code>mksh</code> is a UNIX shell / command interpreter, similar to <code>COMMAND.COM</code> or <code>CMD.EXE</code> which has been included with <code>Android Open Source Project</code> for a while now. Basically, it&#8217;s a program that runs in a terminal (console window), takes user input and runs commands or scripts, which it can also be asked to do by other programs, even in the background. Any privilege pop-ups you might be encountering are thus not <code>mksh</code> issues but questions by some other program utilising it.</p>
<h3>Invocation</h3>
<p> Most builtins can be called directly, for example if a link points from its name to the shell; not all make sense, have been tested or work at all though. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-c </code><i>string</i></p>
<dd> will execute the command(s) contained in <i>string</i></p>
<dt><code>-i</code></p>
<dd> Interactive shell. A shell is &#8220;interactive&#8221; if this option is used or if both standard input and standard error are attached to a <a href="/docs/linux/man/4-tty/">tty</a>(4). An interactive shell has job control enabled, ignores the <code>SIGINT</code> <code>SIGQUIT</code> and <code>SIGTERM</code> signals, and prints prompts before reading input (see the <code>PS1</code> and <code>PS2</code> parameters). It also processes the <code>ENV</code> parameter or the mkshrc file (see below). For non-interactive shells, the <code>trackall</code> option is on by default (see the <code>set</code> command below).</p>
<dt><code>-l</code></p>
<dd> Login shell. If the basename the shell is called with (i.e. argv[0]) starts with `-&#8216; or if this option is used, the shell is assumed to be a login shell; see Sx Startup files below.</p>
<dt><code>-p</code></p>
<dd> Privileged shell. A shell is &#8220;privileged&#8221; if this option is used or if the real user ID or group ID does not match the effective user ID or group ID (see <a href="/docs/linux/man/2-getuid/">getuid</a>(2) and <a href="/docs/linux/man/2-getgid/">getgid</a>(2)). Clearing the privileged option causes the shell to set its effective user ID (group ID) to its real user ID (group ID). For further implications, see Sx Startup files .</p>
<dt><code>-r</code></p>
<dd> Restricted shell. A shell is &#8220;restricted&#8221; if this option is used. The following restrictions come into effect after the shell processes any profile and <code>ENV</code> files: </p>
<ul>
<li> The <code>cd</code> Po and Ic chdir Pc command is disabled.
<li> The <code>SHELL</code> <code>ENV</code> and <code>PATH</code> parameters cannot be changed.
<li> Command names can&#8217;t be specified with absolute or relative paths.
<li> The &#8211;<code>p</code> option of the built-in command <code>command</code> can&#8217;t be used.
<li> Redirections that create files can&#8217;t be used (i.e. `&gt;&#8217; `&gt;|&#8217; `&gt;&gt;&#8217; `&lt;&gt;&#8217; </ul>
<dt><code>-s</code></p>
<dd> The shell reads commands from standard input; all non-option arguments are positional parameters.</p>
<dt><code>-T </code><i>tty</i></p>
<dd> Spawn on the <a href="/docs/linux/man/4-tty/">tty</a>(4) device given. Superuser only. If <i>tty</i> is a dash, detach from controlling terminal (daemonise) instead.</dl>
<p> In addition to the above, the options described in the <code>set</code> built-in command can also be used on the command line: both [-<code>+abCefhkmnuvXx </code>and ] [-<code>+o </code><i>option</i> ] can be used for single letter or long options, respectively. </p>
<p> If neither the &#8211;<code>c</code> nor the &#8211;<code>s</code> option is specified, the first non-option argument specifies the name of a file the shell reads commands from. If there are no non-option arguments, the shell reads commands from the standard input. The name of the shell (i.e. the contents of $0) is determined as follows: if the &#8211;<code>c</code> option is used and there is a non-option argument, it is used as the name; if commands are being read from a file, the file is used as the name; otherwise, the basename the shell was called with (i.e. argv[0]) is used. </p>
<p> The exit status of the shell is 127 if the command file specified on the command line could not be opened, or non-zero if a fatal syntax error occurred during the execution of a script. In the absence of fatal errors, the exit status is that of the last command executed, or zero, if no command is executed.</p>
<h3>Startup files</h3>
<p> For the actual location of these files, see Sx FILES . A login shell processes the system profile first. A privileged shell then processes the suid profile. A non-privileged login shell processes the user profile next. A non-privileged interactive shell checks the value of the <code>ENV</code> parameter after subjecting it to parameter, command, arithmetic and tilde (`~&#8217; ) substitution; if unset or empty, the user mkshrc profile is processed; otherwise, if a file whose name is the substitution result exists, it is processed; non-existence is silently ignored.</p>
<h3>Command syntax</h3>
<p> The shell begins parsing its input by removing any backslash-newline combinations, then breaking it into <i>words</i> Words (which are sequences of characters) are delimited by unquoted whitespace characters (space, tab, and newline) or meta-characters Po `&lt;&#8216; `&gt;&#8217; `|&#8217; `;&#8217; , `(&#8216; , `)&#8217; , and `&amp;&#8217; Pc . Aside from delimiting words, spaces and tabs are ignored, while newlines usually delimit commands. The meta-characters are used in building the following <i>tokens</i> `&lt;&#8216; `&lt;&amp;&#8217; , `&lt;&lt;&#8216; `&lt;&lt;&lt;&#8216; `&gt;&#8217; `&gt;&amp;&#8217; , `&gt;&gt;&#8217; `&amp;&gt;&#8217; etc. are used to specify redirections (see Sx Input/output redirection below); `|&#8217; is used to create pipelines; `|&amp;&#8217; is used to create co-processes (see Sx Co-processes below); `;&#8217; is used to separate commands; `&amp;&#8217; is used to create asynchronous pipelines; `&amp;&amp;&#8217; and `||&#8217; are used to specify conditional execution; `;;&#8217; , `;&amp;&#8217; and `;|&#8217; are used in <code>case</code> statements; `((&#8216; is used in arithmetic expressions; and lastly, `(&#8216; is used to create subshells. </p>
<p> Whitespace and meta-characters can be quoted individually using a backslash (`\&#8217; ) or in groups using double (`&#8217; ) or single (`&#8221; ) quotes. Note that the following characters are also treated specially by the shell and must be quoted if they are to represent themselves: `\&#8217; , `&#8217; , `&#8221; , `#&#8217; , `$&#8217; , &#8220;&#8217; , `~&#8217; , `{&#8216; , `}&#8217; , `*&#8217; , `?&#8217; , and `[&#8216; The first three of these are the above mentioned quoting characters (see Sx Quoting below); `#&#8217; , if used at the beginning of a word, introduces a comment &#8212; everything after the `#&#8217; up to the nearest newline is ignored; `$&#8217; is used to introduce parameter, command, and arithmetic substitutions (see Sx Substitution below); &#8220;&#8217; introduces an old-style command substitution (see Sx Substitution below); `~&#8217; begins a directory expansion (see Sx Tilde expansion below); `{&#8216; and `}&#8217; delimit <a href="/docs/linux/man/1-csh/">csh</a>(1)Ns-style alterations (see Sx Brace expansion below); and finally, `*&#8217; , `?&#8217; , and `[&#8216; are used in file name generation (see Sx File name patterns below). </p>
<p> As words and tokens are parsed, the shell builds commands, of which there are two basic types: <i>simple-commands</i> typically programmes that are executed, and <i>compound-commands</i> such as <code>for</code> and <code>if</code> statements, grouping constructs, and function definitions. </p>
<p> A simple-command consists of some combination of parameter assignments (see Sx Parameters below), input/output redirections (see Sx Input/output redirections below), and command words; the only restriction is that parameter assignments come before any command words. The command words, if any, define the command that is to be executed and its arguments. The command may be a shell built-in command, a function, or an external command (i.e. a separate executable file that is located using the <code>PATH</code> parameter; see Sx Command execution below). Note that all command constructs have an exit status: for external commands, this is related to the status returned by <a href="/docs/linux/man/2-wait/">wait</a>(2) (if the command could not be found, the exit status is 127; if it could not be executed, the exit status is 126); the exit status of other command constructs (built-in commands, functions, compound-commands, pipelines, lists, etc.) are all well-defined and are described where the construct is described. The exit status of a command consisting only of parameter assignments is that of the last command substitution performed during the parameter assignment or 0 if there were no command substitutions. </p>
<p> Commands can be chained together using the `|&#8217; token to form pipelines, in which the standard output of each command but the last is piped (see <a href="/docs/linux/man/2-pipe/">pipe</a>(2)) to the standard input of the following command. The exit status of a pipeline is that of its last command, unless the <code>pipefail</code> option is set (see there). All commands of a pipeline are executed in separate subshells; this is allowed by POSIX but differs from both variants of AT&amp;T System <code>ksh</code> where all but the last command were executed in subshells; see the <code>read</code> builtin&#8217;s description for implications and workarounds. A pipeline may be prefixed by the `!&#8217; reserved word which causes the exit status of the pipeline to be logically complemented: if the original status was 0, the complemented status will be 1; if the original status was not 0, the complemented status will be 0. </p>
<p> <i>Lists</i> of commands can be created by separating pipelines by any of the following tokens: `&amp;&amp;&#8217; , `||&#8217; `&amp;&#8217; , `|&amp;&#8217; , and `;&#8217; The first two are for conditional execution: &#8220;<i>cmd1 </i><code>&amp;&amp; </code><i>cmd2</i> &#8221; executes <i>cmd2</i> only if the exit status of <i>cmd1</i> is zero; `||&#8217; is the opposite &#8212; <i>cmd2</i> is executed only if the exit status of <i>cmd1</i> is non-zero. `&amp;&amp;&#8217; and `||&#8217; have equal precedence which is higher than that of `&amp;&#8217; , `|&amp;&#8217; , and `;&#8217; , which also have equal precedence. Note that the `&amp;&amp;&#8217; and `||&#8217; operators are Qq left-associative . For example, both of these commands will print only Qq bar : </p>
<blockquote>
<pre><code>
$ false &amp;&amp; echo foo || echo bar $ true || echo foo &amp;&amp;echo bar
</code></pre>
</blockquote>
<p> The `&amp;&#8217; token causes the preceding command to be executed asynchronously; that is, the shell starts the command but does not wait for it to complete (the shell does keep track of the status of asynchronous commands; see Sx Job control below). When an asynchronous command is started when job control is disabled (i.e. in most scripts), the command is started with signals <code>SIGINT</code> and <code>SIGQUIT</code> ignored and with input redirected from /dev/null (however, redirections specified in the asynchronous command have precedence). The `|&amp;&#8217; operator starts a co-process which is a special kind of asynchronous process (see Sx Co-processes below). Note that a command must follow the `&amp;&amp;&#8217; and `||&#8217; operators, while it need not follow `&amp;&#8217; , `|&amp;&#8217; , or `;&#8217; The exit status of a list is that of the last command executed, with the exception of asynchronous lists, for which the exit status is 0. </p>
<p> Compound commands are created using the following reserved words. These words are only recognised if they are unquoted and if they are used as the first word of a command (i.e. they can&#8217;t be preceded by parameter assignments or redirections): </p>
<blockquote><p>
case     else     function     then      !       (<br />
do       esac     if           time      [[      ((<br />
done     fi       in           until     {<br />
elif     for      select       while     }
 </p></blockquote>
<p> In the following compound command descriptions, command lists (denoted as <i>list</i> that are followed by reserved words must end with a semicolon, a newline, or a (syntactically correct) reserved word. For example, the following are all valid: </p>
<blockquote><p>
$<br />
{<br />
    echo foo;<br />
    echo bar;<br />
}<br />
$<br />
{<br />
    echo foo;<br />
    echo bar&lt;newline&gt;<br />
}<br />
$<br />
{<br />
    {<br />
        echo foo;<br />
        echo bar;<br />
    }<br />
}
 </p></blockquote>
<p> This is not valid: </p>
<blockquote><p><tt>$ { echo foo; echo bar</tt></p></blockquote>
<dl>
<dt><code>(</code><i>list</i> )</p>
<dd> Execute <i>list</i> in a subshell. There is no implicit way to pass environment changes from a subshell back to its parent.</p>
<dt><code>{ </code><i>list ; </i><code>}</code></p>
<dd> Compound construct; <i>list</i> is executed, but not in a subshell. Note that `{&#8216; and `}&#8217; are reserved words, not meta-characters.</p>
<dt><code> case </code><i>word </i><code>in</code> [[(] <i>pattern</i> [| <i>pat</i> ] <code>&#8230; )</code> <i>list</i> [;; | ;&amp; | ;|&nbsp;<wbr>] &#8230; esac]</p>
<dd>
<dd>The <code>case</code> statement attempts to match <i>word</i> against a specified <i>pattern</i> the <i>list</i> associated with the first successfully matched pattern is executed. Patterns used in <code>case</code> statements are the same as those used for file name patterns except that the restrictions regarding `.&#8217; and `/&#8217; are dropped. Note that any unquoted space before and after a pattern is stripped; any space within a pattern must be quoted. Both the word and the patterns are subject to parameter, command, and arithmetic substitution, as well as tilde substitution. </p>
<p> For historical reasons, open and close braces may be used instead of <code>in</code> and <code>esac</code> e.g. <code>case $foo { *) echo bar;; }</code> </p>
<p> The list terminators are:</p>
<dl>
<dt><code>`;;&#8217; </code></p>
<dd> Terminate after the list.</p>
<dt><code>`;&amp;&#8217; </code></p>
<dd> Fall through into the next list.</p>
<dt><code>`;|&#8217; </code></p>
<dd> Evaluate the remaining pattern-list tuples.</dl>
<p> The exit status of a <code>case</code> statement is that of the executed <i>list</i> if no <i>list</i> is executed, the exit status is zero.</p>
<dt><code> for </code><i>name</i> [in <i>word </i><code>&#8230; </code>] <code>do </code><i>list ; </i><code>done</code></p>
<dd>
<dd>For each <i>word</i> in the specified word list, the parameter <i>name</i> is set to the word and <i>list</i> is executed. If <code>in</code> is not used to specify a word list, the positional parameters ($1, $2, etc.) are used instead. For historical reasons, open and close braces may be used instead of <code>do</code> and <code>done</code> e.g. <code>for i; { echo $i; }</code> The exit status of a <code>for</code> statement is the last exit status of <i>list</i> if <i>list</i> is never executed, the exit status is zero.</p>
<dt><code> if </code><i>list</i> <code>then </code><i>list</i> [elif <i>list</i> <code>then </code><i>list ; </i>] <code>&#8230;</code> [else <i>list ; </i>] <code>fi</code></p>
<dd>
<dd>If the exit status of the first <i>list</i> is zero, the second <i>list</i> is executed; otherwise, the <i>list</i> following the <code>elif</code> if any, is executed with similar consequences. If all the lists following the <code>if</code> and <code>elif s</code> fail (i.e. exit with non-zero status), the <i>list</i> following the <code>else</code> is executed. The exit status of an <code>if</code> statement is that of non-conditional <i>list</i> that is executed; if no non-conditional <i>list</i> is executed, the exit status is zero.</p>
<dt><code> select </code><i>name</i> [in <i>word </i><code>&#8230; </code>] <code>do </code><i>list ; </i><code>done</code></p>
<dd>
<dd>The <code>select</code> statement provides an automatic method of presenting the user with a menu and selecting from it. An enumerated list of the specified <i>word </i><code>(s)</code> is printed on standard error, followed by a prompt Po <code>PS3: normally</code> `#?&nbsp;<wbr>&#8216; Pc . A number corresponding to one of the enumerated words is then read from standard input, <i>name</i> is set to the selected word (or unset if the selection is not valid), <code>REPLY</code> is set to what was read (leading/trailing space is stripped), and <i>list</i> is executed. If a blank line (i.e. zero or more <code>IFS</code> octets) is entered, the menu is reprinted without executing <i>list</i> </p>
<p> When <i>list</i> completes, the enumerated list is printed if <code>REPLY</code> is <code>NULL</code> the prompt is printed, and so on. This process continues until an end-of-file is read, an interrupt is received, or a <code>break</code> statement is executed inside the loop. If &#8220;in word &#8230;&#8221; is omitted, the positional parameters are used (i.e. $1, $2, etc.). For historical reasons, open and close braces may be used instead of <code>do</code> and <code>done</code> e.g. <code>select i; { echo $i; }</code> The exit status of a <code>select</code> statement is zero if a <code>break</code> statement is used to exit the loop, non-zero otherwise.</p>
<dt><code> until </code><i>list</i> <code>do </code><i>list</i> <code>done</code></p>
<dd>
<dd>This works like <code>while</code> except that the body is executed only while the exit status of the first <i>list</i> is non-zero.</p>
<dt><code> while </code><i>list</i> <code>do </code><i>list</i> <code>done</code></p>
<dd>
<dd>A <code>while</code> is a pre-checked loop. Its body is executed as often as the exit status of the first <i>list</i> is zero. The exit status of a <code>while</code> statement is the last exit status of the <i>list</i> in the body of the loop; if the body is not executed, the exit status is zero.</p>
<dt><code> function </code><i>name</i> <code>{ </code><i>list ; </i><code>}</code></p>
<dd>
<dd>Defines the function <i>name</i> (see Sx Functions below). Note that redirections specified after a function definition are performed whenever the function is executed, not when the function definition is executed.</p>
<dt><i>name </i><code>() </code><i>command</i></p>
<dd> Mostly the same as <code>function</code> (see Sx Functions below). Whitespace (space or tab) after <i>name</i> will be ignored most of the time.</p>
<dt><code> function </code><i>name </i><code>()</code> <code>{ </code><i>list ; </i><code>}</code></p>
<dd>
<dd>The same as <i>name </i><code>()</code> (<code>bash ism</code> ) The <code>function</code> keyword is ignored.</p>
<dt><code> time </code>[-<code>p</code> ] [<i>pipeline</i> ]</p>
<dd>
<dd>The Sx Command execution section describes the <code>time</code> reserved word.</p>
<dt><code>(( </code><i>expression </i><code>))</code></p>
<dd> The arithmetic expression <i>expression</i> is evaluated; equivalent to &#8220;let expression&#8221; (see Sx Arithmetic expressions and the <code>let</code> command, below).</p>
<dt><code>Bq </code>Bq <i>&nbsp;<wbr>expression&nbsp;<wbr></i></p>
<dd> Similar to the <code>test</code> and <code>[ &#8230; ]</code> commands (described later), with the following exceptions: </p>
<ul>
<li> Field splitting and file name generation are not performed on arguments.
<li> The &#8211;<code>a</code> (AND) and &#8211;<code>o</code> (OR) operators are replaced with `&amp;&amp;&#8217; and `||&#8217; respectively.
<li> Operators (e.g. `-<code>f</code> &#8216; `=&#8217; `!&#8217; must be unquoted.
<li> Parameter, command, and arithmetic substitutions are performed as expressions are evaluated and lazy expression evaluation is used for the `&amp;&amp;&#8217; and `||&#8217; operators. This means that in the following statement, <code>$(&lt;foo)</code> is evaluated if and only if the file foo exists and is readable:<br />
<blockquote><p>
$[[-r foo &amp;&amp; $(&lt; foo) = b * r]]
 </p></blockquote>
<li> The second operand of the `!=&#8217; and `=&#8217; expressions are patterns (e.g. the comparison <code>[[ foobar = f*r ]]</code> succeeds). This even works indirectly:<br />
<blockquote><p>
$ bar = foobar;<br />
baz = &#8216;f*r&#8217; $ [[$bar = $baz]];<br />
echo $ ? $ [[$bar = &#8220;$baz&#8221;]];<br />
echo $ ?
 </p></blockquote>
<p> Perhaps surprisingly, the first comparison succeeds, whereas the second doesn&#8217;t. </ul>
</dl>
<h3>Quoting</h3>
<p> Quoting is used to prevent the shell from treating characters or words specially. There are three methods of quoting. First, `\&#8217; quotes the following character, unless it is at the end of a line, in which case both the `\&#8217; and the newline are stripped. Second, a single quote (`&#8221; ) quotes everything up to the next single quote (this may span lines). Third, a double quote (`&#8217; ) quotes all characters, except `$&#8217; , &#8220;&#8217; and `\&#8217; , up to the next unquoted double quote. `$&#8217; and &#8220;&#8217; inside double quotes have their usual meaning (i.e. parameter, command, or arithmetic substitution) except no field splitting is carried out on the results of double-quoted substitutions. If a `\&#8217; inside a double-quoted string is followed by `\&#8217; , `$&#8217; , &#8220;&#8217; , or `&#8217; , it is replaced by the second character; if it is followed by a newline, both the `\&#8217; and the newline are stripped; otherwise, both the `\&#8217; and the character following are unchanged. </p>
<p> If a single-quoted string is preceded by an unquoted `$&#8217; , C style backslash expansion (see below) is applied (even single quote characters inside can be escaped and do not terminate the string then); the expanded result is treated as any other single-quoted string. If a double-quoted string is preceded by an unquoted `$&#8217; , the latter is ignored.</p>
<h3>Backslash expansion</h3>
<p> In places where backslashes are expanded, certain C and AT&amp;T System <code>ksh</code> or GNU <code>bash</code> style escapes are translated. These include `&#8217; , `&#8217; , `&#8217; , `
&#8217; , `&#8217; , `	&#8217; , `
