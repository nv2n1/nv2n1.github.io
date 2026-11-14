---
title: "ksh93(1)"
name: "ksh93"
section: "1"
letter: "k"
url: "/docs/linux/man/1-ksh93/"
description: "ksh, rksh, pfksh – KornShell, a standard/restricted command and programming language"
---

<h2 class="name">NAME</h2>
<p> ksh, rksh, pfksh &#8211; KornShell, a standard/restricted command and programming language </p>
<h2>SYNOPSIS</h2>
<p> <code>ksh</code> [ <code>&plusmn;abcefhiknoprstuvxBCDP</code> ] [ <code>-R</code> file ] [ <code>&plusmn;o</code> option ] &#8230; [ <code>&#8211;</code> ] [ arg &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Ksh</i> is a command and programming language that executes commands read from a terminal or a file. <i>Rksh</i> is a restricted version of the command interpreter <i>ksh</i>; it is used to set up login names and execution environments whose capabilities are more controlled than those of the standard shell. <i>Rpfksh</i> is a profile shell version of the command interpreter <i>ksh</i>; it is used to to execute commands with the attributes specified by the user&#8217;s profiles (see <i><a href="/docs/linux/man/1-pfexec/">pfexec</a></i>(1)). See <i>Invocation</i> below for the meaning of arguments to the shell.</p>
<h3>Definitions.</h3>
<p> A <i>metacharacter</i> is one of the following characters: </p>
<dl>
<dt>
<dd> <code>; &amp; ( ) | &lt; &gt; new-line space tab</code></dl>
<p> A <i>blank</i> is a <code>tab</code> or a <code>space</code>. An <i>identifier</i> is a sequence of letters, digits, or underscores starting with a letter or underscore. Identifiers are used as components of <i>variable</i> names. A <i>vname</i> is a sequence of one or more identifiers separated by a <font SIZE="+2"><code>.</code></font> and optionally preceded by a <font SIZE="+2"><code>.</code></font>. Vnames are used as function and variable names. A <i>word</i> is a sequence of <i>characters</i> from the character set defined by the current locale, excluding non-quoted <i>metacharacters</i>. </p>
<p> A <i>command</i> is a sequence of characters in the syntax of the shell language. The shell reads each command and carries out the desired action either directly or by invoking separate utilities. A built-in command is a command that is carried out by the shell itself without creating a separate process. Some commands are built-in purely for convenience and are not documented here. Built-ins that cause side effects in the shell environment and built-ins that are found before performing a path search (see <i>Execution</i> below) are documented here. For historical reasons, some of these built-ins behave differently than other built-ins and are called <i>special built-ins</i>.</p>
<h3>Commands.</h3>
<p> A <i>simple-command</i> is a list of variable assignments (see <i>Variable Assignments</i> below) or a sequence of <i>blank</i> separated words which may be preceded by a list of variable assignments (see <i>Environment</i> below). The first word specifies the name of the command to be executed. Except as specified below, the remaining words are passed as arguments to the invoked command. The command name is passed as argument 0 (see <i><a href="/docs/linux/man/2-exec/">exec</a></i>(2)). The <i>value</i> of a simple-command is its exit status; 0-255 if it terminates normally; 256+<i>signum</i> if it terminates abnormally (the name of the signal corresponding to the exit status can be obtained via the <code>-l</code> option of the <code>kill</code> built-in utility). </p>
<p> A <i>pipeline</i> is a sequence of one or more <i>commands</i> separated by <code>|</code>. The standard output of each command but the last is connected by a <i><a href="/docs/linux/man/2-pipe/">pipe</a></i>(2) to the standard input of the next command. Each command, except possibly the last, is run as a separate process; the shell waits for the last command to terminate. The exit status of a pipeline is the exit status of the last command unless the <code>pipefail</code> option is enabled. Each pipeline can be preceded by the <i>reserved word</i> <code>!</code> which causes the exit status of the pipeline to become 0 if the exit status of the last command is non-zero, and 1 if the exit status of the last command is 0. </p>
<p> A <i>list</i> is a sequence of one or more pipelines separated by <code>;</code>, <code>&amp;</code>, <code>|&amp;</code>, <code>&amp;&amp;</code>, or <code>||</code>, and optionally terminated by <code>;</code>, <code>&amp;</code>, or <code>|&amp;</code>. Of these five symbols, <code>;</code>, <code>&amp;</code>, and <code>|&amp;</code> have equal precedence, which is lower than that of <code>&amp;&amp;</code> and <code>||</code>. The symbols <code>&amp;&amp;</code> and <code>||</code> also have equal precedence. A semicolon (<code>;</code>) causes sequential execution of the preceding pipeline; an ampersand (<code>&amp;</code>) causes asynchronous execution of the preceding pipeline (i.e., the shell does <i>not</i> wait for that pipeline to finish). The symbol <code>|&amp;</code> causes asynchronous execution of the preceding pipeline with a two-way pipe established to the parent shell; the standard input and output of the spawned pipeline can be written to and read from by the parent shell by applying the redirection operators <code>&lt;&amp;</code> and <code>&gt;&amp;</code> with arg <code>p</code> to commands and by using <code>-p</code> option of the built-in commands <code>read</code> and <code>print</code> described later. The symbol <code>&amp;&amp;</code> (<code>||</code>) causes the <i>list</i> following it to be executed only if the preceding pipeline returns a zero (non-zero) value. One or more new-lines may appear in a <i>list</i> instead of a semicolon, to delimit a command. The first <i>item </i> of the first <i>pipeline</i> of a <i>list</i> that is a simple command not beginning with a redirection, and not occurring within a <code>while</code>, <code>until</code>, or <code>if</code> <i>list</i>, can be preceded by a semicolon. This semicolon is ignored unless the <code>showme</code> option is enabled as described with the <code>set</code> built-in below. </p>
<p> A <i>command</i> is either a simple-command or one of the following. Unless otherwise stated, the value returned by a command is that of the last simple-command executed in the command.</p>
<dl>
<dt><code>for</code> <i>vname</i> <code>in</code> <i>word</i> &#8230; ] <code>;do</code> <i>list</i> <code>;done</code></p>
<dd> Each time a <code>for</code> command is executed, <i>vname</i> is set to the next <i>word</i> taken from the <code>in</code> <i>word</i> list. If <code>in</code><i> word</i> &#8230; is omitted, then the <code>for</code> command executes the <code>do</code> <i>list</i> once for each positional parameter that is set starting from <code>1</code> (see <i>Parameter Expansion</i> below). Execution ends when there are no more words in the list.</p>
<dt><code>for ((</code> <i>expr1</i>] <code>;</code> <i>expr2</i>] <code>;</code> <i>expr3</i>] <code>))</code> <code>;do</code> <i>list</i> <code>;done</code></p>
<dd> The arithmetic expression <i>expr1</i> is evaluated first (see <i>Arithmetic evaluation</i> below). The arithmetic expression <i>expr2</i> is repeatedly evaluated until it evaluates to zero and when non-zero, <i>list</i> is executed and the arithmetic expression <i>expr3</i> evaluated. If any expression is omitted, then it behaves as if it evaluated to 1.</p>
<dt><code>select</code> <i>vname</i> <code>in</code> <i>word</i> &#8230; ] <code>;do</code> <i>list</i> <code>;done</code></p>
<dd> A <code>select</code> command prints on standard error (file descriptor 2) the set of <i>word</i>s, each preceded by a number. If <code>in</code><i> word</i> &#8230; is omitted, then the positional parameters starting from <code>1</code> are used instead (see <i>Parameter Expansion</i> below). The <font SIZE="-1"><code>PS3</code> </font> prompt is printed and a line is read from the standard input. If this line consists of the number of one of the listed <i>word</i>s, then the value of the variable <i>vname</i> is set to the <i>word</i> corresponding to this number. If this line is empty, the selection list is printed again. Otherwise the value of the variable <i>vname</i> is set to <i>null</i>. The contents of the line read from standard input is saved in the variable <font SIZE="-1"><code>REPLY</code>. </font> The <i>list</i> is executed for each selection until a <code>break</code> or <i>end-of-file</i> is encountered. If the <font SIZE="-1"><code>REPLY</code> </font> variable is set to <i>null</i> by the execution of <i>list</i>, then the selection list is printed before displaying the <font SIZE="-1"><code>PS3</code> </font> prompt for the next selection.</p>
<dt><code>case</code> <i>word</i> <code>in</code> <code>(</code>]<i>pattern</i> | <i>pattern</i> ] &#8230; <code>)</code> <i>list</i> <code>;;</code> ] &#8230; <code>esac</code></p>
<dd> A <code>case</code> command executes the <i>list</i> associated with the first <i>pattern</i> that matches <i>word</i>. The form of the patterns is the same as that used for file-name generation (see <i>File Name Generation</i> below). The <code>;;</code> operator causes execution of <code>case</code> to terminate. If <code>;&amp;</code> is used in place of <code>;;</code> the next subsequent list, if any, is executed.</p>
<dt><code>if</code> <i>list</i> <code>;then</code> <i>list</i> <code>;elif</code> <i>list</i> <code>;then</code> <i>list</i> ] &#8230; <code>;else</code> <i>list</i> ] <code>;fi</code></p>
<dd> The <i>list</i> following <code>if</code> is executed and, if it returns a zero exit status, the <i>list</i> following the first <code>then</code> is executed. Otherwise, the <i>list</i> following <code>elif</code> is executed and, if its value is zero, the <i>list</i> following the next <code>then</code> is executed. Failing each successive <code>elif</code> <i>list</i>, the <code>else</code> <i>list</i> is executed. If the <code>if</code> <i>list</i> has non-zero exit status and there is no <code>else</code> <i>list</i>, then the <code>if</code> command returns a zero exit status.</p>
<dt>
<dd> <code>while</code> <i>list</i> <code>;do</code> <i>list</i> <code>;done</code></p>
<dt><code>until</code> <i>list</i> <code>;do</code> <i>list</i> <code>;done</code></p>
<dd> A <code>while</code> command repeatedly executes the <code>while</code> <i>list</i> and, if the exit status of the last command in the list is zero, executes the <code>do</code> <i>list</i>; otherwise the loop terminates. If no commands in the <code>do</code> <i>list</i> are executed, then the <code>while</code> command returns a zero exit status; <code>until</code> may be used in place of <code>while</code> to negate the loop termination test.</p>
<dt><code>((</code><i>expression</i><code>))</code></p>
<dd>
 The <i>expression</i> is evaluated using the rules for arithmetic evaluation described below. If the value of the arithmetic expression is non-zero, the exit status is 0, otherwise the exit status is 1.</p>
<dt><code>(</code><i>list</i><code>)</code></p>
<dd>
 Execute <i>list</i> in a separate environment. Note, that if two adjacent open parentheses are needed for nesting, a space must be inserted to avoid evaluation as an arithmetic command as described above.</p>
<dt><code>{ </code><i>list</i><code>;}</code></p>
<dd>
 <i>list</i> is simply executed. Note that unlike the metacharacters <code>(</code> and <code>)</code>, <code>{</code> and <code>}</code> are <i>reserved word</i>s and must occur at the beginning of a line or after a <code>;</code> in order to be recognized.</p>
<dt><code>[[</code><i> expression </i><code>]]</code></p>
<dd>
 Evaluates <i>expression</i> and returns a zero exit status when <i>expression</i> is true. See <i>Conditional Expressions</i> below, for a description of <i>expression</i>.</p>
<dt>
<dd> <code>function</code> <i>varname</i> <code>{</code> <i>list</i> <code>;}</code></p>
<dt><i>varname</i> <code>() {</code> <i>list</i> <code>;}</code></p>
<dd> Define a function which is referenced by <i>varname</i>. A function whose <i>varname</i> contains a <font SIZE="+2"><code>.</code></font> is called a discipline function and the portion of the <i>varname</i> preceding the last <font SIZE="+2"><code>.</code></font> must refer to an existing variable. The body of the function is the <i>list</i> of commands between <code>{</code> and <code>}</code>. A function defined with the <code>function</code> <i>varname</i> syntax can also be used as an argument to the <code>.</code> special built-in command to get the equivalent behavior as if the <i>varname</i><code>()</code> syntax were used to define it. (See <i>Functions</i> below.)</p>
<dt><code>namespace</code> <i>identifier</i> <code>{</code> <i>list</i> <code>;}</code></p>
<dd>
 Defines or uses the name space <i>identifier</i> and runs the commands in <i>list</i> in this name space. (See <i>Name Spaces</i> below.)</p>
<dt><code>&amp;</code> <i>name</i> <i>arg&#8230;</i> ] ]</p>
<dd> Causes subsequent <i>list</i> commands terminated by <code>&amp;</code> to be placed in the background job pool <i>name</i>. If <i>name</i> is omitted a default unnamed pool is used. Commands in a named background pool may be executed remotely.</p>
<dt><code>time</code> <i>pipeline</i> ]</p>
<dd>
 If <i>pipeline</i> is omitted the user and system time for the current shell and completed child processes is printed on standard error. Otherwise, <i>pipeline</i> is executed and the elapsed time as well as the user and system time are printed on standard error. The <font SIZE="-1"><code>TIMEFORMAT</code> </font> variable may be set to a format string that specifies how the timing information should be displayed. See <code>Shell Variables</code> below for a description of the <font SIZE="-1"><code>TIMEFORMAT</code> </font> variable.</dl>
<p> The following reserved words are recognized as reserved only when they are the first word of a command and are not quoted: </p>
<p> <code>if then else elif fi case esac for while until do done { } function select time [[ ]] ! </code></p>
<h3>Variable Assignments.</h3>
<p> One or more variable assignments can start a simple command or can be arguments to the <code>typeset</code>, <code>enum</code>, <code>export</code>, or <code>readonly</code> special built-in commands as well as to other declaration commands created as types. The syntax for an <i>assignment</i> is of the form:</p>
<dl>
<dt>
<dd> <i>varname</i><code>=</code><i>word</i></p>
<dt><i>varname</i><code>[</code><i>word</i><code>]</code>=<i>word</i></p>
<dd> No space is permitted between <i>varname</i> and the <code>=</code> or between <code>=</code> and <i>word</i>.</p>
<dt><i>varname</i><code>=(</code><i>assign_list</i><code>)</code></p>
<dd> No space is permitted between <i>varname</i> and the <code>=</code>. The variable <i>varname</i> is unset before the assignment. An <i>assign_list</i> can be one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>word</i> &#8230;</p>
<dd> Indexed array assignment.</p>
<dt><code>[</code><i>word</i><code>]=</code><i>word</i> &#8230;</p>
<dd> Associative array assignment. If preceded by <code>typeset -a</code> this will create an indexed array instead.</p>
<dt><i>assignment</i> &#8230;</p>
<dd> Compound variable assignment. This creates a compound variable <i>varname</i> with sub-variables of the form <i>varname</i><code>.</code><i>name</i>, where <i>name</i> is the name portion of <i>assignment</i>. The value of <i>varname</i> will contain all the assignment elements. Additional assignments made to sub-variables of <i>varname</i> will also be displayed as part of the value of <i>varname</i>. If no <i>assignment</i>s are specified, <i>varname</i> will be a compound variable allowing subsequence child elements to be defined.</p>
<dt><code>typeset</code> <i>options</i>] <i>assignment</i> &#8230;</p>
<dd> Nested variable assignment. Multiple assignments can be specified by separating each of them with a <code>;</code>. The previous value is unset before the assignment. Other declaration commands such as <code>readonly,</code> <code>enum</code>, and other declaration commands can be used in place of <code>typeset</code>.</p>
<dt><code>.</code> <i>filename</i></p>
<dd> Include the assignment commands contained in <i>filename</i>.</dl>
</dl>
</dl>
<p> In addition, a <code>+=</code> can be used in place of the <code>=</code> to signify adding to or appending to the previous value. When <code>+=</code> is applied to an arithmetic type, <i>word</i> is evaluated as an arithmetic expression and added to the current value. When applied to a string variable, the value defined by <i>word</i> is appended to the value. For compound assignments, the previous value is not unset and the new values are appended to the current ones provided that the types are compatible. </p>
<p> The right hand side of a variable assignment undergoes all the expansion listed below except word splitting, brace expansion, and file name generation. When the left hand side is an assignment is a compound variable and the right hand is the name of a compound variable, the compound variable on the right will be copied or appended to the compound variable on the left.</p>
<h3>Comments.</h3>
<p> A word beginning with <code>#</code> causes that word and all the following characters up to a new-line to be ignored.</p>
<h3>Aliasing.</h3>
<p> The first word of each command is replaced by the text of an <code>alias</code> if an <code>alias</code> for this word has been defined. An <code>alias</code> name consists of any number of characters excluding metacharacters, quoting characters, file expansion characters, parameter expansion and command substitution characters, the characters <code>/</code> and <code>=</code>. The replacement string can contain any valid shell script including the metacharacters listed above. The first word of each command in the replaced text, other than any that are in the process of being replaced, will be tested for aliases. If the last character of the alias value is a <i>blank</i> then the word following the alias will also be checked for alias substitution. Aliases can be used to redefine built-in commands but cannot be used to redefine the reserved words listed above. Aliases can be created and listed with the <code>alias</code> command and can be removed with the <code>unalias</code> command. </p>
<p> <i>Aliasing</i> is performed when scripts are read, not while they are executed. Therefore, for an alias to take effect, the <code>alias</code> definition command has to be executed before the command which references the alias is read. </p>
<p> The following aliases are compiled into the shell but can be unset or redefined:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>autoload=&#180;typeset -fu&#180;</code></p>
<dd>
<dt><code>command=&#180;command &#180;</code></p>
<dd>
<dt><code>compound=&#180;typeset -C&#180;</code></p>
<dd>
<dt><code>fc=hist</code></p>
<dd>
<dt><code>float=&#180;typeset -lE&#180;</code></p>
<dd>
<dt><code>functions=&#180;typeset -f&#180;</code></p>
<dd>
<dt><code>hash=&#180;alias -t &#8211;&#180;</code></p>
<dd>
<dt><code>history=&#180;hist -l&#180;</code></p>
<dd>
<dt><code>integer=&#180;typeset -li&#180;</code></p>
<dd>
<dt><code>nameref=&#180;typeset -n&#180;</code></p>
<dd>
<dt><code>nohup=&#180;nohup &#180;</code></p>
<dd>
<dt><code>r=&#180;hist -s&#180;</code></p>
<dd>
<dt><code>redirect=&#180;command exec&#180;</code></p>
<dd>
<dt><code>source=&#180;command </code><font SIZE="+2"><code>.</code></font><code>&#180;</code></p>
<dd>
<dt><code>stop=&#180;kill -s </code><font SIZE="-1"><code>STOP</code></font><code>&#180;</code></p>
<dd>
<dt><code>suspend=&#180;kill -s </code><font SIZE="-1"><code>STOP</code></font><code> $$&#180;</code></p>
<dd>
<dt><code>times=&#180;{ { time;} 2&gt;&amp;1;}&#180;</code></p>
<dd>
<dt><code>type=&#180;whence -v&#180;</code></p>
<dd></dl>
</dl>
<h3>Tilde Substitution.</h3>
<p> After alias substitution is performed, each word is checked to see if it begins with an unquoted <code>&asymp;</code>. For tilde substitution, <i>word</i> also refers to the <i>word</i> portion of parameter expansion (see <i>Parameter Expansion</i> below). If it does, then the word up to a <code>/</code> is checked to see if it matches a user name in the password database (See <i><a href="/docs/linux/man/3-getpwname/">getpwname</a></i>(3).) If a match is found, the <code>&asymp;</code> and the matched login name are replaced by the login directory of the matched user. If no match is found, the original text is left unchanged. A <code>&asymp;</code> by itself, or in front of a <code>/</code>, is replaced by <font SIZE="-1"><code>$HOME</code>. </font> A <code>&asymp;</code> followed by a <code>+</code> or <code>&#8211;</code> is replaced by the value of <font SIZE="-1"><code>$PWD</code></font> and <font SIZE="-1"><code>$OLDPWD</code></font> respectively. </p>
<p> In addition, when expanding a <i>variable assignment</i>, <i>tilde</i> substitution is attempted when the value of the assignment begins with a <code>&asymp;</code>, and when a <code>&asymp;</code> appears after a <code>:</code>. The <code>:</code> also terminates a <code>&asymp;</code> login name.</p>
<h3>Command Substitution.</h3>
<p> The standard output from a command list enclosed in parentheses preceded by a dollar sign ( <code>$(</code><i>list</i><code>)</code> ), or in a brace group preceded by a dollar sign ( <code>${ </code><i>list</i><code>;}</code> ), or in a pair of grave accents (<code><font SIZE="+4">`</font><font SIZE="+4">`</font></code>) may be used as part or all of a word; trailing new-lines are removed. In the second case, the <code>{</code> and <code>}</code> are treated as a reserved words so that <code>{</code> must be followed by a <i>blank</i> and <code>}</code> must appear at the beginning of the line or follow a <code>;</code>. In the third (obsolete) form, the string between the quotes is processed for special quoting characters before the command is executed (see <i>Quoting</i> below). The command substitution <code>$(cat file)</code> can be replaced by the equivalent but faster <code>$(&lt;file)</code>. The command substitution <code>$(</code><i>n</i><code>&lt;#)</code> will expand to the current byte offset for file descriptor <i>n</i>. Except for the second form, the command list is run in a subshell so that no side effects are possible. For the second form, the final <code>}</code> will be recognized as a reserved word after any token.</p>
<h3>Arithmetic Substitution.</h3>
<p> An arithmetic expression enclosed in double parentheses preceded by a dollar sign ( <code>$(())</code> ) is replaced by the value of the arithmetic expression within the double parentheses.</p>
<h3>Process Substitution.</h3>
<p> Each command argument of the form <code>&lt;(</code><i>list</i><code>)</code> or <code>&gt;(</code><i>list</i><code>)</code> will run process <i>list</i> asynchronously connected to some file in <code>/dev/fd</code> if this directory exists, or else a fifo a temporary directory. The name of this file will become the argument to the command. If the form with <code>&gt;</code> is selected then writing on this file will provide input for <i>list</i>. If <code>&lt;</code> is used, then the file passed as an argument will contain the output of the <i>list</i> process. For example, </p>
<dl>
<dt>
<dd> <code>paste &lt;(cut -f1</code> <i>file1</i><code>) &lt;(cut -f3</code> <i>file2</i><code>) | tee &gt;(</code><i>process1</i><code>) &gt;(</code><i>process2</i><code>)</code></dl>
<p> <i>cuts</i> fields 1 and 3 from the files <i>file1</i> and <i>file2</i> respectively, <i>pastes</i> the results together, and sends it to the processes <i>process1</i> and <i>process2</i>, as well as putting it onto the standard output. Note that the file, which is passed as an argument to the command, is a UNIX <i><a href="/docs/linux/man/2-pipe/">pipe</a></i>(2) so programs that expect to <i><a href="/docs/linux/man/2-lseek/">lseek</a></i>(2) on the file will not work. </p>
<p> Process substitution of the form <code>&lt;(</code><i>list</i><code>)</code> can also be used with the <code>&lt;</code> redirection operator which causes the output of <i>list</i> to be standard input or the input for whatever file descriptor is specified.</p>
<h3>Parameter Expansion.</h3>
<p> A <i>parameter</i> is a <i>variable</i>, one or more digits, or any of the characters <code>*</code>, <code>@</code>, <code>#</code>, <code>?</code>, <code>&#8211;</code>, <code>$</code>, and <code>!\^</code>. A <i>variable</i> is denoted by a <i>vname</i>. To create a variable whose <i>vname</i> contains a <font SIZE="+2"><code>.</code></font>, a variable whose <i>vname</i> consists of everything before the last <font SIZE="+2"><code>.</code></font> must already exist. A <i>variable</i> has a <i>value</i> and zero or more <i>attributes</i>. <i>Variables</i> can be assigned <i>values</i> and <i>attributes</i> by using the <code>typeset</code> special built-in command. The attributes supported by the shell are described later with the <code>typeset</code> special built-in command. Exported variables pass values and attributes to the environment. </p>
<p> The shell supports both indexed and associative arrays. An element of an array variable is referenced by a <i>subscript</i>. A <i>subscript</i> for an indexed array is denoted by an <i>arithmetic expression</i> (see <i>Arithmetic evaluation</i> below) between a <code>[</code> and a <code>]</code>. To assign values to an indexed array, use <i>vname</i><code>=(</code><i>value</i> &#8230;<code>)</code> or <code>set -A</code> <i>vname</i> <i>value</i> &#8230; . The value of all non-negative subscripts must be in the range of 0 through 4,194,303. A negative subscript is treated as an offset from the maximum current index +1 so that -1 refers to the last element. Indexed arrays can be declared with the <code>-a</code> option to <code>typeset.</code> Indexed arrays need not be declared. Any reference to a variable with a valid subscript is legal and an array will be created if necessary. </p>
<p> An associative array is created with the <code>-A</code> option to <code>typeset.</code> A <i>subscript</i> for an associative array is denoted by a string enclosed between <code>[</code> and <code>]</code>. </p>
<p> Referencing any array without a subscript is equivalent to referencing the array with subscript 0. </p>
<p> The <i>value</i> of a <i>variable</i> may be assigned by writing: </p>
<dl>
<dt>
<dd> <i>vname</i><code>=</code><i>value</i> <i>vname</i><code>=</code><i>value</i> ] &#8230;</dl>
<p> or </p>
<dl>
<dt>
<dd> <i>vname</i><code>[</code><i>subscript</i><code>]=</code><i>value</i> <i>vname</i><code>[</code><i>subscript</i><code>]=</code><i>value</i> ] &#8230; </p>
</dl>
<p> Note that no space is allowed before or after the <code>=</code>. </p>
<p> Attributes assigned by the <i>typeset</i> special built-in command apply to all elements of the array. An array element can be a simple variable, a compound variable or an array variable. An element of an indexed array can be either an indexed array or an associative array. An element of an associative array can also be either. To refer to an array element that is part of an array element, concatenate the subscript in brackets. For example, to refer to the <i>foobar</i> element of an associative array that is defined as the third element of the indexed array, use <code>${</code><i>vname</i><code>[</code><i>3</i><code>][</code><i>foobar</i><code>]}</code> </p>
<p> A <i>nameref</i> is a variable that is a reference to another variable. A nameref is created with the <code>-n</code> attribute of <code>typeset</code>. The value of the variable at the time of the <code>typeset</code> command becomes the variable that will be referenced whenever the nameref variable is used. The name of a nameref cannot contain a <font SIZE="+2"><code>.</code></font>. When a variable or function name contains a <font SIZE="+2"><code>.</code></font>, and the portion of the name up to the first <font SIZE="+2"><code>.</code></font> matches the name of a nameref, the variable referred to is obtained by replacing the nameref portion with the name of the variable referenced by the nameref. If a nameref is used as the index of a <code>for</code> loop, a name reference is established for each item in the list. A nameref provides a convenient way to refer to the variable inside a function whose name is passed as an argument to a function. For example, if the name of a variable is passed as the first argument to a function, the command </p>
<dl>
<dt>
<dd> <code>typeset -n var=$1</code></dl>
<p> inside the function causes references and assignments to <code>var</code> to be references and assignments to the variable whose name has been passed to the function. </p>
<p> If any of the floating point attributes, <code>-E</code>, <code>-F</code>, or <code>-X</code>, or the integer attribute, <code>-i</code>, is set for <i>vname</i>, then the <i>value</i> is subject to arithmetic evaluation as described below. </p>
<p> Positional parameters, parameters denoted by a number, may be assigned values with the <code>set</code> special built-in command. Parameter <code>$0</code> is set from argument zero when the shell is invoked. </p>
<p> The character <code>$</code> is used to introduce substitutable <i>parameters</i>.</p>
<dl>
<dt><code>${</code><i>parameter</i><code>}</code></p>
<dd> The shell reads all the characters from <code>${</code> to the matching <code>}</code> as part of the same word even if it contains braces or metacharacters. The value, if any, of the parameter is substituted. The braces are required when <i>parameter</i> is followed by a letter, digit, or underscore that is not to be interpreted as part of its name, when the variable name contains a <font SIZE="+2"><code>.</code></font>. The braces are also required when a variable is subscripted unless it is part of an Arithmetic Expression or a Conditional Expression. If <i>parameter</i> is one or more digits then it is a positional parameter. A positional parameter of more than one digit must be enclosed in braces. If <i>parameter</i> is <code>*</code> or <code>@</code>, then all the positional parameters, starting with <code>$1</code>, are substituted (separated by a field separator character). If an array <i>vname</i> with last subscript <code>*</code> <code>@</code>, or for index arrays of the form <i>sub1</i> <code>..</code> <i>sub2</i>. is used, then the value for each of the elements between <i>sub1</i> and <i>sub2</i> inclusive (or all elements for <code>*</code> and <code>@</code>) is substituted, separated by the first character of the value of <font SIZE="-1"><code>IFS</code>. </font></p>
<dt><code>${#</code><i>parameter</i><code>}</code></p>
<dd> If <i>parameter</i> is <code>*</code> or <code>@</code>, the number of positional parameters is substituted. Otherwise, the length of the value of the <i>parameter</i> is substituted.</p>
<dt>
<dd> <code>${#</code><i>vname</i><code>[*]}</code></p>
<dt>
<dd> <code>${#</code><i>vname</i><code>[@]}</code> The number of elements in the array <i>vname</i> is substituted.</p>
<dt>
<dd> <code>${@</code><i>vname</i><code>}</code> Expands to the type name (See <i>Type Variables</i> below) or attributes of the variable referred to by <i>vname</i>.</p>
<dt><code>${!</code><i>vname</i><code>}</code></p>
<dd> Expands to the name of the variable referred to by <i>vname</i>. This will be <i>vname</i> except when <i>vname</i> is a name reference.</p>
<dt><code>${!</code><i>vname</i><code>[</code><i>subscript</i><code>]}</code></p>
<dd> Expands to name of the subscript unless <i>subscript</i> is <code>*</code>, <code>@</code>. or of the form <i>sub1</i> <code>..</code> <i>sub2</i>. When <i>subscript</i> is <code>*</code>, the list of array subscripts for <i>vname</i> is generated. For a variable that is not an array, the value is 0 if the variable is set. Otherwise it is null. When <i>subscript</i> is <code>@</code>, same as above, except that when used in double quotes, each array subscript yields a separate argument. When <i>subscript</i> is of the form <i>sub1</i> <code>..</code> <i>sub2</i> it expands to the list of subscripts between <i>sub1</i> and <i>sub2</i> inclusive using the same quoting rules as <code>@</code>.</p>
<dt><code>${!</code><i>prefix</i><code>*}</code></p>
<dd> Expands to the names of the variables whose names begin with <i>prefix</i>.</p>
<dt><code>${</code><i>parameter</i><code>:-</code><i>word</i><code>}</code></p>
<dd> If <i>parameter</i> is set and is non-null then substitute its value; otherwise substitute <i>word</i>.</p>
<dt><code>${</code><i>parameter</i><code>:=</code><i>word</i><code>}</code></p>
<dd> If <i>parameter</i> is not set or is null then set it to <i>word</i>; the value of the parameter is then substituted. Positional parameters may not be assigned to in this way.</p>
<dt><code>${</code><i>parameter</i><code>:?</code><i>word</i><code>}</code></p>
<dd> If <i>parameter</i> is set and is non-null then substitute its value; otherwise, print <i>word</i> and exit from the shell (if not interactive). If <i>word</i> is omitted then a standard message is printed.</p>
<dt><code>${</code><i>parameter</i><code>:+</code><i>word</i><code>}</code></p>
<dd> If <i>parameter</i> is set and is non-null then substitute <i>word</i>; otherwise substitute nothing.</dl>
<p> In the above, <i>word</i> is not evaluated unless it is to be used as the substituted string, so that, in the following example, <code>pwd</code> is executed only if <code>d</code> is not set or is null: </p>
<dl>
<dt>
<dd> print ${d:-$(pwd)}</dl>
<p> If the colon ( <code>: )</code> is omitted from the above expressions, then the shell only checks whether <i>parameter</i> is set or not.</p>
<dl>
<dt>
<dd> <code>${</code><i>parameter</i><code>:</code><i>offset</i><code>:</code><i>length</i><code>}</code></p>
<dt><code>${</code><i>parameter</i><code>:</code><i>offset</i><code>}</code></p>
<dd> Expands to the portion of the value of <i>parameter</i> starting at the character (counting from <code>0</code>) determined by expanding <i>offset</i> as an arithmetic expression and consisting of the number of characters determined by the arithmetic expression defined by <i>length.</i> In the second form, the remainder of the value is used. If A negative <i>offset</i> counts backwards from the end of <i>parameter</i>. Note that one or more <i>blank</i>s is required in front of a minus sign to prevent the shell from interpreting the operator as <code>:-</code>. If <i>parameter</i> is <code>*</code> or <code>@</code>, or is an array name indexed by <code>*</code> or <code>@</code>, then <i>offset</i> and <i>length</i> refer to the array index and number of elements respectively. A negative <i>offset</i> is taken relative to one greater than the highest subscript for indexed arrays. The order for associate arrays is unspecified.</p>
<dt>
<dd> <code>${</code><i>parameter</i><code>#</code><i>pattern</i><code>}</code></p>
<dt><code>${</code><i>parameter</i><code>##</code><i>pattern</i><code>}</code></p>
<dd> If the shell <i>pattern</i> matches the beginning of the value of <i>parameter</i>, then the value of this expansion is the value of the <i>parameter</i> with the matched portion deleted; otherwise the value of this <i>parameter</i> is substituted. In the first form the smallest matching pattern is deleted and in the second form the largest matching pattern is deleted. When <i>parameter</i> is <code>@</code>, <code>*</code>, or an array variable with subscript <code>@</code> or <code>*</code>, the substring operation is applied to each element in turn.</p>
<dt>
<dd> <code>${</code><i>parameter</i><code>%</code><i>pattern</i><code>}</code></p>
<dt><code>${</code><i>parameter</i><code>%%</code><i>pattern</i><code>}</code></p>
<dd> If the shell <i>pattern</i> matches the end of the value of <i>parameter</i>, then the value of this expansion is the value of the <i>parameter</i> with the matched part deleted; otherwise substitute the value of <i>parameter</i>. In the first form the smallest matching pattern is deleted and in the second form the largest matching pattern is deleted. When <i>parameter</i> is <code>@</code>, <code>*</code>, or an array variable with subscript <code>@</code> or <code>*</code>, the substring operation is applied to each element in turn.</p>
<dt>
<dd> <code>${</code><i>parameter</i><code>/</code><i>pattern</i><code>/</code><i>string</i><code>}</code></p>
<dt><code>${</code><i>parameter</i><code>//</code><i>pattern</i><code>/</code><i>string</i><code>}</code></p>
<dd>
<dt><code>${</code><i>parameter</i><code>/#</code><i>pattern</i><code>/</code><i>string</i><code>}</code></p>
<dd>
<dt><code>${</code><i>parameter</i><code>/%</code><i>pattern</i><code>/</code><i>string</i><code>}</code></p>
<dd> Expands <i>parameter</i> and replaces the longest match of <i>pattern</i> with the given <i>string.</i> Each occurrence of <code>\</code><i>n</i> in <i>string</i> is replaced by the portion of <i>parameter</i> that matches the <i>n</i>-th sub-pattern. In the first form, only the first occurrence of <i>pattern</i> is replaced. In the second form, each match for <i>pattern</i> is replaced by the given <i>string.</i> The third form restricts the pattern match to the beginning of the string while the fourth form restricts the pattern match to the end of the string. When <i>string</i> is null, the <i>pattern</i> will be deleted and the <code>/</code> in front of <i>string</i> may be omitted. When <i>parameter</i> is <code>@</code>, <code>*</code>, or an array variable with subscript <code>@</code> or <code>*</code>, the substitution operation is applied to each element in turn. In this case, the <i>string</i> portion of <i>word</i> will be re-evaluated for each element.</dl>
<p> The following parameters are automatically set by the shell:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>#</code></p>
<dd> The number of positional parameters in decimal.</p>
<dt><code>&#8211;</code></p>
<dd> Options supplied to the shell on invocation or by the <code>set</code> command.</p>
<dt><code>?</code></p>
<dd> The decimal value returned by the last executed command.</p>
<dt><code>$</code></p>
<dd> The process number of this shell.</p>
<dt><code>_</code></p>
<dd> Initially, the value of <code>_</code> is an absolute pathname of the shell or script being executed as passed in the <i>environment</i>. Subsequently it is assigned the last argument of the previous command. This parameter is not set for commands which are asynchronous. This parameter is also used to hold the name of the matching <font SIZE="-1"><code>MAIL</code></font> file when checking for mail. While defining a compound variable or a type, <code>_</code> is initialized as a reference to the compound variable or type. When a discipline function is invoked, <code>_</code> is initialized as a reference to the variable associated with the call to this function. Finally when <code>_</code> is used as the name of the first variable of a type definition, the new type is derived from the type of the first variable (See <i>Type Variables</i> below.).</p>
<dt><code>!</code></p>
<dd> The process id or the pool name and job number of the last background command invoked or the most recent job put in the background with the <code>bg</code> built-in command. Background jobs started in a named pool will be in the form <i>pool</i><code>.</code><i>number</i> where <i>pool</i> is the pool name and <i>number</i> is the job number within that pool.</p>
<dt><code>.sh.command</code></p>
<dd> When processing a <font SIZE="-1"><code>DEBUG</code> </font> trap, this variable contains the current command line that is about to run.</p>
<dt><code>.sh.edchar</code></p>
<dd> This variable contains the value of the keyboard character (or sequence of characters if the first character is an ESC, ascii <code>033</code>) that has been entered when processing a <font SIZE="-1"><code>KEYBD</code></font> trap (see <i>Key Bindings</i> below). If the value is changed as part of the trap action, then the new value replaces the key (or key sequence) that caused the trap.</p>
<dt><code>.sh.edcol</code></p>
<dd> The character position of the cursor at the time of the most recent <font SIZE="-1"><code>KEYBD</code></font> trap.</p>
<dt><code>.sh.edmode</code></p>
<dd> The value is set to ESC when processing a <font SIZE="-1"><code>KEYBD</code></font> trap while in <code>vi</code> insert mode. (See <i>Vi Editing Mode</i> below.) Otherwise, <code>.sh.edmode</code> is null when processing a <font SIZE="-1"><code>KEYBD</code></font> trap.</p>
<dt><code>.sh.edtext</code></p>
<dd> The characters in the input buffer at the time of the most recent <font SIZE="-1"><code>KEYBD</code></font> trap. The value is null when not processing a <font SIZE="-1"><code>KEYBD</code></font> trap.</p>
<dt><code>.sh.file</code></p>
<dd> The pathname of the file than contains the current command.</p>
<dt><code>.sh.fun</code></p>
<dd> The name of the current function that is being executed.</p>
<dt><code>.sh.level</code></p>
<dd> Set to the current function depth. This can be changed inside a DEBUG trap and will set the context to the specified level.</p>
<dt><code>.sh.lineno</code></p>
<dd> Set during a DEBUG trap to the line number for the caller of each function.</p>
<dt><code>.sh.match</code></p>
<dd> An indexed array which stores the most recent match and sub-pattern matches after conditional pattern matches that match and after variables expansions using the operators <code>#</code>, <code>%</code>, or <code>/</code>. The <code>0</code>-th element stores the complete match and the <i>i</i>-th. element stores the <i>i</i>-th submatch. The <code>.sh.match</code> variable becomes unset when the variable that has expanded is assigned a new value.</p>
<dt><code>.sh.math</code></p>
<dd> Used for defining arithmetic functions (see <i>Arithmetic evaluation</i> below). and stores the list of user defined arithmetic functions.</p>
<dt><code>.sh.name</code></p>
<dd> Set to the name of the variable at the time that a discipline function is invoked.</p>
<dt><code>.sh.subscript</code></p>
<dd> Set to the name subscript of the variable at the time that a discipline function is invoked.</p>
<dt><code>.sh.subshell</code></p>
<dd> The current depth for subshells and command substitution.</p>
<dt><code>.sh.value</code></p>
<dd> Set to the value of the variable at the time that the <code>set</code> or <code>append</code> discipline function is invoked. When a user defined arithmetic function is invoked, the value of <code>.sh.value</code> is saved and <code>.sh.value</code> is set to long double precision floating point. <code>.sh.value</code> is restored when the function returns.</p>
<dt><code>.sh.version</code></p>
<dd> Set to a value that identifies the version of this shell.</p>
<dt><font SIZE="-1"><code>KSH_VERSION</code></font></p>
<dd> A name reference to <code>.sh.version</code>.</p>
<dt><font SIZE="-1"><code>LINENO</code></font></p>
<dd> The current line number within the script or function being executed.</p>
<dt><font SIZE="-1"><code>OLDPWD</code></font></p>
<dd> The previous working directory set by the <code>cd</code> command.</p>
<dt><font SIZE="-1"><code>OPTARG</code></font></p>
<dd> The value of the last option argument processed by the <code>getopts</code> built-in command.</p>
<dt><font SIZE="-1"><code>OPTIND</code></font></p>
<dd> The index of the last option argument processed by the <code>getopts</code> built-in command.</p>
<dt><font SIZE="-1"><code>PPID</code></font></p>
<dd> The process number of the parent of the shell.</p>
<dt><font SIZE="-1"><code>PWD</code></font></p>
<dd> The present working directory set by the <code>cd</code> command.</p>
<dt><font SIZE="-1"><code>RANDOM</code></font></p>
<dd> Each time this variable is referenced, a random integer, uniformly distributed between 0 and 32767, is generated. The sequence of random numbers can be initialized by assigning a numeric value to <font SIZE="-1"><code>RANDOM</code>. </font></p>
<dt><font SIZE="-1"><code>REPLY</code></font></p>
<dd> This variable is set by the <code>select</code> statement and by the <code>read</code> built-in command when no arguments are supplied.</p>
<dt><font SIZE="-1"><code>SECONDS</code></font></p>
<dd> Each time this variable is referenced, the number of seconds since shell invocation is returned. If this variable is assigned a value, then the value returned upon reference will be the value that was assigned plus the number of seconds since the assignment.</p>
<dt><font SIZE="-1"><code>SHLVL</code> </font></p>
<dd> An integer variable the is incremented each time the shell is invoked and is exported. If <font SIZE="-1"><code>SHLVL</code> </font> is not in the environment when the shell is invoked, it is set to 1.</dl>
</dl>
<p> The following variables are used by the shell:</p>
<dl>
<dt>
<dd>
<dl>
<dt><font SIZE="-1"><code>CDPATH</code></font></p>
<dd> The search path for the <code>cd</code> command.</p>
<dt><font SIZE="-1"><code>COLUMNS</code></font></p>
<dd> If this variable is set, the value is used to define the width of the edit window for the shell edit modes and for printing <code>select</code> lists.</p>
<dt><font SIZE="-1"><code>EDITOR</code></font></p>
<dd> If the <font SIZE="-1"><code>VISUAL</code></font> variable is not set, the value of this variable will be checked for the patterns as described with <font SIZE="-1"><code>VISUAL</code></font> below and the corresponding editing option (see Special Command <code>set</code> below) will be turned on.</p>
<dt><font SIZE="-1"><code>ENV</code> </font></p>
<dd> If this variable is set, then parameter expansion, command substitution, and arithmetic substitution are performed on the value to generate the pathname of the script that will be executed when the shell is invoked interactively (see <i>Invocation</i> below). This file is typically used for <code>alias</code> and <code>function</code> definitions. The default value is <code>$HOME/.kshrc</code>. On systems that support a system wide <code>/etc/ksh.kshrc</code> initialization file, if the filename generated by the expansion of <font SIZE="-1"><code>ENV</code> </font> begins with <code>/./</code> or <code>././</code> the system wide initialization file will not be executed.</p>
<dt><font SIZE="-1"><code>FCEDIT</code></font></p>
<dd> Obsolete name for the default editor name for the <code>hist</code> command. <font SIZE="-1"><code>FCEDIT</code></font> is not used when <font SIZE="-1"><code>HISTEDIT</code></font> is set.</p>
<dt><font SIZE="-1"><code>FIGNORE</code> </font></p>
<dd> A pattern that defines the set of filenames that will be ignored when performing filename matching.</p>
<dt><font SIZE="-1"><code>FPATH</code> </font></p>
<dd> The search path for function definitions. The directories in this path are searched for a file with the same name as the function or command when a function with the <code>-u</code> attribute is referenced and when a command is not found. If an executable file with the name of that command is found, then it is read and executed in the current environment. Unlike <font SIZE="-1"><code>PATH</code>, </font> the current directory must be represented explicitly by <code>.</code> rather than by adjacent <code>:</code> characters or a beginning or ending <code>:</code>.</p>
<dt><font SIZE="-1"><code>HISTCMD</code></font></p>
<dd> Number of the current command in the history file.</p>
<dt><font SIZE="-1"><code>HISTEDIT</code></font></p>
<dd> Name for the default editor name for the <code>hist</code> command.</p>
<dt><font SIZE="-1"><code>HISTFILE</code> </font></p>
<dd> If this variable is set when the shell is invoked, then the value is the pathname of the file that will be used to store the command history (see <i>Command Re-entry</i> below).</p>
<dt><font SIZE="-1"><code>HISTSIZE</code> </font></p>
<dd> If this variable is set when the shell is invoked, then the number of previously entered commands that are accessible by this shell will be greater than or equal to this number. The default is 512.</p>
<dt><font SIZE="-1"><code>HOME</code></font></p>
<dd> The default argument (home directory) for the <code>cd</code> command.</p>
<dt><font SIZE="-1"><code>IFS</code> </font></p>
<dd> Internal field separators, normally <code>space</code>, <code>tab</code>, and <code>new-line</code> that are used to separate the results of command substitution or parameter expansion and to separate fields with the built-in command <code>read</code>. The first character of the <font SIZE="-1"><code>IFS</code> </font> variable is used to separate arguments for the <code>&quot;$*&quot;</code> substitution (see <i>Quoting</i> below). Each single occurrence of an <font SIZE="-1"><code>IFS</code> </font> character in the string to be split, that is not in the <i>isspace</i> character class, and any adjacent characters in <font SIZE="-1"><code>IFS</code> </font> that are in the <i>isspace</i> character class, delimit a field. One or more characters in <font SIZE="-1"><code>IFS</code> </font> that belong to the <i>isspace</i> character class, delimit a field. In addition, if the same <i>isspace</i> character appears consecutively inside <font SIZE="-1"><code>IFS</code>, </font> this character is treated as if it were not in the <i>isspace</i> class, so that if <font SIZE="-1"><code>IFS</code> </font> consists of two <code>tab</code> characters, then two adjacent <code>tab</code> characters delimit a null field.</p>
<dt><font SIZE="-1"><code>JOBMAX</code></font></p>
<dd> This variable defines the maximum number running background jobs that can run at a time. When this limit is reached, the shell will wait for a job to complete before staring a new job.</p>
<dt><font SIZE="-1"><code>LANG</code></font></p>
<dd> This variable determines the locale category for any category not specifically selected with a variable starting with <font SIZE="-1"><code>LC_</code></font> or <font SIZE="-1"><code>LANG</code>. </font></p>
<dt><font SIZE="-1"><code>LC_ALL</code></font></p>
<dd> This variable overrides the value of the <font SIZE="-1"><code>LANG</code></font> variable and any other <font SIZE="-1"><code>LC_</code></font> variable.</p>
<dt><font SIZE="-1"><code>LC_COLLATE</code></font></p>
<dd> This variable determines the locale category for character collation information.</p>
<dt><font SIZE="-1"><code>LC_CTYPE</code></font></p>
<dd> This variable determines the locale category for character handling functions. It determines the character classes for pattern matching (see <i>File Name Generation</i> below).</p>
<dt><font SIZE="-1"><code>LC_NUMERIC</code></font></p>
<dd> This variable determines the locale category for the decimal point character.</p>
<dt><font SIZE="-1"><code>LINES</code></font></p>
<dd> If this variable is set, the value is used to determine the column length for printing <code>select</code> lists. Select lists will print vertically until about two-thirds of <font SIZE="-1"><code>LINES</code></font> lines are filled.</p>
<dt><font SIZE="-1"><code>MAIL</code></font></p>
<dd> If this variable is set to the name of a mail file <i>and</i> the <font SIZE="-1"><code>MAILPATH</code></font> variable is not set, then the shell informs the user of arrival of mail in the specified file.</p>
<dt><font SIZE="-1"><code>MAILCHECK</code></font></p>
<dd> This variable specifies how often (in seconds) the shell will check for changes in the modification time of any of the files specified by the <font SIZE="-1"><code>MAILPATH</code></font> or <font SIZE="-1"><code>MAIL</code></font> variables. The default value is 600 seconds. When the time has elapsed the shell will check before issuing the next prompt.</p>
<dt><font SIZE="-1"><code>MAILPATH</code></font></p>
<dd> A colon ( <code>:</code> ) separated list of file names. If this variable is set, then the shell informs the user of any modifications to the specified files that have occurred within the last <font SIZE="-1"><code>MAILCHECK</code></font> seconds. Each file name can be followed by a <code>?</code> and a message that will be printed. The message will undergo parameter expansion, command substitution, and arithmetic substitution with the variable <code>$_</code> defined as the name of the file that has changed. The default message is <i>you have mail in $_.</i></p>
<dt><font SIZE="-1"><code>PATH</code></font></p>
<dd> The search path for commands (see <i>Execution</i> below). The user may not change <font SIZE="-1"><code>PATH</code></font> if executing under <code>rksh</code> (except in <code>.profile).</code></p>
<dt><font SIZE="-1"><code>PS1</code> </font></p>
<dd> The value of this variable is expanded for parameter expansion, command substitution, and arithmetic substitution to define the primary prompt string which by default is &#8220;<code>$</code>&#8221;. The character <code>!</code> in the primary prompt string is replaced by the <i>command</i> number (see <i>Command Re-entry</i> below). Two successive occurrences of <code>!</code> will produce a single <code>!</code> when the prompt string is printed.</p>
<dt><font SIZE="-1"><code>PS2</code> </font></p>
<dd> Secondary prompt string, by default &#8220;<code>&gt; </code>&#8221;.</p>
<dt><font SIZE="-1"><code>PS3</code> </font></p>
<dd> Selection prompt string used within a <code>select</code> loop, by default &#8220;<code>#? </code>&#8221;.</p>
<dt><font SIZE="-1"><code>PS4</code> </font></p>
<dd> The value of this variable is expanded for parameter evaluation, command substitution, and arithmetic substitution and precedes each line of an execution trace. By default, <font SIZE="-1"><code>PS4</code> </font> is &#8220;<code>+ </code>&#8221;. In addition when <font SIZE="-1"><code>PS4</code> </font> is unset, the execution trace prompt is also &#8220;<code>+ </code>&#8221;.</p>
<dt><font SIZE="-1"><code>SHELL</code> </font></p>
<dd> The pathname of the <i>shell</i> is kept in the environment. At invocation, if the basename of this variable is <code>rsh</code>, <code>rksh</code>, or <code>krsh</code>, then the shell becomes restricted. If it is <code>pfsh</code> or <code>pfksh</code>, then the shell becomes a profile shell (see <i><a href="/docs/linux/man/1-pfexec/">pfexec</a></i>(1)).</p>
<dt><font SIZE="-1"><code>TIMEFORMAT</code> </font></p>
<dd> The value of this parameter is used as a format string specifying how the timing information for pipelines prefixed with the <code>time</code> reserved word should be displayed. The <code>%</code> character introduces a format sequence that is expanded to a time value or other information. The format sequences and their meanings are as follows. </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>%%</code></p>
<dd> A literal <code>%</code>.</p>
<dt><code>%[</code><i>p</i>][l]R</p>
<dd> The elapsed time in seconds.</p>
<dt><code>%[</code><i>p</i>][l]U</p>
<dd> The number of CPU seconds spent in user mode.</p>
<dt><code>%[</code><i>p</i>][l]S</p>
<dd> The number of CPU seconds spent in system mode.</p>
<dt><code>%P</code></p>
<dd> The CPU percentage, computed as (U + S) / R.</dl>
</dl>
<dt>
<dd> The brackets denote optional portions. The optional <i>p</i> is a digit specifying the <i>precision</i>, the number of fractional digits after a decimal point. A value of 0 causes no decimal point or fraction to be output. At most three places after the decimal point can be displayed; values of <i>p</i> greater than 3 are treated as 3. If <i>p</i> is not specified, the value 3 is used.</p>
<dt>
<dd> The optional <code>l</code> specifies a longer format, including hours if greater than zero, minutes, and seconds of the form <i>HH</i>h<i>MM</i>m<i>SS</i>.<i>FF</i>s. The value of <i>p</i> determines whether or not the fraction is included.</p>
<dt>
<dd> All other characters are output without change and a trailing newline is added. If unset, the default value, <code>$&#8217;
real	%2lR
user	%2lU
sys %2lS&#8217;</code>, is used. If the value is null, no timing information is displayed.</p>
<dt><font SIZE="-1"><code>TMOUT</code></font></p>
<dd> If set to a value greater than zero, <font SIZE="-1"><code>TMOUT</code></font> will be the default timeout value for the <code>read</code> built-in command. The <code>select</code> compound command terminates after <font SIZE="-1"><code>TMOUT</code></font> seconds when input is from a terminal. Otherwise, the shell will terminate if a line is not entered within the prescribed number of seconds while reading from a terminal. (Note that the shell can be compiled with a maximum bound for this value which cannot be exceeded.)</p>
<dt><font SIZE="-1"><code>VISUAL</code></font></p>
<dd> If the value of this variable matches the pattern <i>*[Vv][Ii]*</i>, then the <code>vi</code> option (see Special Command <code>set</code> below) is turned on. If the value matches the pattern <i>*gmacs* ,</i> the <code>gmacs</code> option is turned on. If the value matches the pattern <i>*macs*</i>, then the <code>emacs</code> option will be turned on. The value of <font SIZE="-1"><code>VISUAL</code></font> overrides the value of <font SIZE="-1"><code>EDITOR.</code></font></dl>
</dl>
<p> The shell gives default values to <font SIZE="-1"><code>PATH</code></font>, <font SIZE="-1"><code>PS1</code></font>, <font SIZE="-1"><code>PS2</code></font>, <font SIZE="-1"><code>PS3</code></font>, <font SIZE="-1"><code>PS4</code></font>, <font SIZE="-1"><code>MAILCHECK</code></font>, <font SIZE="-1"><code>FCEDIT</code></font>, <font SIZE="-1"><code>TMOUT</code></font> and <font SIZE="-1"><code>IFS</code></font>, while <font SIZE="-1"><code>HOME</code>, </font> <font SIZE="-1"><code>SHELL</code>, </font> <font SIZE="-1"><code>ENV</code>, </font> and <font SIZE="-1"><code>MAIL</code> </font> are not set at all by the shell (although <font SIZE="-1"><code>HOME</code> </font> <i>is</i> set by <i><a href="/docs/linux/man/1-login/">login</a></i>(1)). On some systems <font SIZE="-1"><code>MAIL</code> </font> and <font SIZE="-1"><code>SHELL</code> </font> are also set by <i><a href="/docs/linux/man/1-login/">login</a></i>(1).</p>
<h3>Field Splitting.</h3>
<p> After parameter expansion and command substitution, the results of substitutions are scanned for the field separator characters (those found in <font SIZE="-1"><code>IFS</code></font> ) and split into distinct fields where such characters are found. Explicit null fields (<code>&quot;&quot;</code> or <code>&#180;&#180;</code>) are retained. Implicit null fields (those resulting from <i>parameters</i> that have no values or command substitutions with no output) are removed. </p>
<p> If the <code>braceexpand</code> (<code>-B</code>) option is set then each of the fields resulting from <font SIZE="-1"><code>IFS</code> </font> are checked to see if they contain one or more of the brace patterns <code>{*,*}</code>, <code>{</code><i>l1</i><code>..</code><i>l2</i><code>}</code> , <code>{</code><i>n1</i><code>..</code><i>n2</i><code>}</code> , <code>{</code><i>n1</i><code>..</code><i>n2</i><code>%</code> <i>fmt</i><code>}</code> , <code>{</code><i>n1</i><code>..</code><i>n2</i> <code>..</code><i>n3</i><code>}</code> , or <code>{</code><i>n1</i><code>..</code><i>n2</i> <code>..</code><i>n3</i><code>%</code><i>fmt</i><code>}</code> , where <code>*</code> represents any character, <i>l1</i>,<i>l2</i> are letters and <i>n1</i>,<i>n2</i>,<i>n3</i> are signed numbers and <i>fmt</i> is a format specified as used by <code>printf</code>. In each case, fields are created by prepending the characters before the <code>{</code> and appending the characters after the <code>}</code> to each of the strings generated by the characters between the <code>{</code> and <code>}</code>. The resulting fields are checked to see if they have any brace patterns. </p>
<p> In the first form, a field is created for each string between <code>{</code> and <code>,</code>, between <code>,</code> and <code>,</code>, and between <code>,</code> and <code>}</code>. The string represented by <code>*</code> can contain embedded matching <code>{</code> and <code>}</code> without quoting. Otherwise, each <code>{</code> and <code>}</code> with <code>*</code> must be quoted. </p>
<p> In the seconds form, <i>l1</i> and <i>l2</i> must both be either upper case or both be lower case characters in the C locale. In this case a field is created for each character from <i>l1</i> thru <i>l2</i>. </p>
<p> In the remaining forms, a field is created for each number starting at <i>n1</i> and continuing until it reaches <i>n2</i> incrementing <i>n1</i> by <i>n3</i>. The cases where <i>n3</i> is not specified behave as if <i>n3</i> where <code>1</code> if <i>n1</i><code>&lt;=</code><i>n2</i> and <code>-1</code> otherwise. If forms which specify <code>%</code><i>fmt</i> any format flags, widths and precisions can be specified and <i>fmt</i> can end in any of the specifiers <code>cdiouxX</code>. For example, <code>{a,z}{1..5..3%02d}{b..c}x</code> expands to the 8 fields, <code>a01bx</code>, <code>a01cx</code>, <code>a04bx</code>, <code>a04cx</code>, <code>z01bx</code>, <code>z01cx</code>, <code>z04bx</code> and <code>z4cx</code>.</p>
<h3>File Name Generation.</h3>
<p> Following splitting, each field is scanned for the characters <code>*</code>, <code>?</code>, <code>(</code>, and unless the <code>-f</code> option has been set. If one of these characters appears, then the word is regarded as a <i>pattern</i>. Each file name component that contains any pattern character is replaced with a lexicographically sorted set of names that matches the pattern from that directory. If no file name is found that matches the pattern, then that component of the filename is left unchanged unless the pattern is prefixed with <code>&asymp;(N)</code> in which case it is removed as described below. If <font SIZE="-1"><code>FIGNORE</code> </font> is set, then each file name component that matches the pattern defined by the value of <font SIZE="-1"><code>FIGNORE</code> </font> is ignored when generating the matching filenames. The names <code>.</code> and <code>..</code> are also ignored. If <font SIZE="-1"><code>FIGNORE</code> </font> is not set, the character <code>.</code> at the start of each file name component will be ignored unless the first character of the pattern corresponding to this component is the character <code>.</code> itself. Note, that for other uses of pattern matching the <code>/</code> and <code>.</code> are not treated specially. </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>*</code></p>
<dd> Matches any string, including the null string. When used for filename expansion, if the <code>globstar</code> option is on, two adjacent <code>*</code>&#8216;s by itself will match all files and zero or more directories and subdirectories. If followed by a <code>/</code> then only directories and subdirectories will match.</p>
<dt><code>?</code></p>
<dd> Matches any single character.</p>
<dt>&#8230;<code>]</code></p>
<dd> Matches any one of the enclosed characters. A pair of characters separated by <code>&#8211;</code> matches any character lexically between the pair, inclusive. If the first character following the opening is a <code>!</code> or <code>^</code> then any character not enclosed is matched. A <code>&#8211;</code> can be included in the character set by putting it as the first or last character.<br />
 Within and <code>]</code>, character classes can be specified with the syntax <code>[:</code><i>class</i><code>:]</code> where class is one of the following classes defined in the ANSI-C standard: (Note that <code>word</code> is equivalent to <code>alnum</code> plus the character <code>_</code>.)<br />
 <code>alnum alpha blank cntrl digit graph lower print punct space upper word xdigit </code><br />
 Within and <code>]</code>, an equivalence class can be specified with the syntax <code>[=</code><i>c</i><code>=]</code> which matches all characters with the same primary collation weight (as defined by the current locale) as the character <i>c</i>. Within and <code>]</code>, <code>[.</code><i>symbol</i><code>.]</code> matches the collating symbol <i>symbol</i>.</dl>
</dl>
<p> A <i>pattern-list</i> is a list of one or more patterns separated from each other with a <code>&amp;</code> or <code>|</code>. A <code>&amp;</code> signifies that all patterns must be matched whereas <code>|</code> requires that only one pattern be matched. Composite patterns can be formed with one or more of the following sub-patterns:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>?(</code><i>pattern-list</i><code>)</code></p>
<dd> Optionally matches any one of the given patterns.</p>
<dt><code>*(</code><i>pattern-list</i><code>)</code></p>
<dd> Matches zero or more occurrences of the given patterns.</p>
<dt><code>+(</code><i>pattern-list</i><code>)</code></p>
<dd> Matches one or more occurrences of the given patterns.</p>
<dt><code>{</code><i>n</i><code>}</code>(<i>pattern-list</i><code>)</code></p>
<dd> Matches <i>n</i> occurrences of the given patterns.</p>
<dt><code>{</code><i>m</i><code>,</code><i>n</i><code>}</code>(<i>pattern-list</i><code>)</code></p>
<dd> Matches from <i>m</i> to <i>n</i> occurrences of the given patterns. If <i>m</i> is omitted, <code>0</code> will be used. If <i>n</i> is omitted at least <i>m</i> occurrences will be matched.</p>
<dt><code>@(</code><i>pattern-list</i><code>)</code></p>
<dd> Matches exactly one of the given patterns. </p>
<dt><code>!(</code><i>pattern-list</i><code>)</code></p>
<dd> Matches anything except one of the given patterns.</dl>
</dl>
<p> By default, each pattern, or sub-pattern will match the longest string possible consistent with generating the longest overall match. If more than one match is possible, the one starting closest to the beginning of the string will be chosen. However, for each of the above compound patterns a <code>&#8211;</code> can be inserted in front of the <code>(</code> to cause the shortest match to the specified <i>pattern-list</i> to be used. </p>
<p> When <i>pattern-list</i> is contained within parentheses, the backslash character <code>\</code> is treated specially even when inside a character class. All ANSI-C character escapes are recognized and match the specified character. In addition the following escape sequences are recognized:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>\d</code></p>
<dd> Matches any character in the <code>digit</code> class.</p>
<dt><code>\D</code></p>
<dd> Matches any character not in the <code>digit</code> class.</p>
<dt><code>\s</code></p>
<dd> Matches any character in the <code>space</code> class.</p>
<dt><code>\S</code></p>
<dd> Matches any character not in the <code>space</code> class.</p>
<dt><code>\w</code></p>
<dd> Matches any character in the <code>word</code> class.</p>
<dt><code>\W</code></p>
<dd> Matches any character not in the <code>word</code> class.</dl>
</dl>
<p> A pattern of the form <code>%(</code><i>pattern-pair</i>(s)<code>)</code> is a sub-pattern that can be used to match nested character expressions. Each <i>pattern-pair</i> is a two character sequence which cannot contain <code>&amp;</code> or <code>|</code>. The first <i>pattern-pair</i> specifies the starting and ending characters for the match. Each subsequent <i>pattern-pair</i> represents the beginning and ending characters of a nested group that will be skipped over when counting starting and ending character matches. The behavior is unspecified when the first character of a <i>pattern-pair</i> is alpha-numeric except for the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>D</code></p>
<dd> Causes the ending character to terminate the search for this pattern without finding a match.</p>
<dt><code>E</code></p>
<dd> Causes the ending character to be interpreted as an escape character.</p>
<dt><code>L</code></p>
<dd> Causes the ending character to be interpreted as a quote character causing all characters to be ignored when looking for a match.</p>
<dt><code>Q</code></p>
<dd> Causes the ending character to be interpreted as a quote character causing all characters other than any escape character to be ignored when looking for a match.</dl>
</dl>
<p> Thus, <code>%({}Q&quot;E\)</code>, matches characters starting at <code>{</code> until the matching <code>}</code> is found not counting any <code>{</code> or <code>}</code> that is inside a double quoted string or preceded by the escape character <code>\</code>. Without the <code>{}</code> this pattern matches any C language string. </p>
<p> Each sub-pattern in a composite pattern is numbered, starting at 1, by the location of the <code>(</code> within the pattern. The sequence <code>\</code><i>n</i>, where <i>n</i> is a single digit and <code>\</code><i>n</i> comes after the <i>n</i>-th. sub-pattern, matches the same string as the sub-pattern itself. </p>
<p> Finally a pattern can contain sub-patterns of the form <code>&asymp;(</code><i>options</i><code>:</code><i>pattern-list</i><code>)</code>, where either <i>options</i> or <code>:</code><i>pattern-list</i> can be omitted. Unlike the other compound patterns, these sub-patterns are not counted in the numbered sub-patterns. <code>:</code><i>pattern-list</i> must be omitted for options <code>F</code>, <code>G</code>, <code>N ,</code> and <code>V</code> below. If <i>options</i> is present, it can consist of one or more of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>+</code></p>
<dd> Enable the following options. This is the default.</p>
<dt><code>&#8211;</code></p>
<dd> Disable the following options.</p>
<dt><code>E</code></p>
<dd> The remainder of the pattern uses extended regular expression syntax like the <i><a href="/docs/linux/man/1-egrep/">egrep</a></i>(1) command.</p>
<dt><code>F</code></p>
<dd> The remainder of the pattern uses <i><a href="/docs/linux/man/1-fgrep/">fgrep</a></i>(1) expression syntax.</p>
<dt><code>G</code></p>
<dd> The remainder of the pattern uses basic regular expression syntax like the <i><a href="/docs/linux/man/1-grep/">grep</a></i>(1) command.</p>
<dt><code>K</code></p>
<dd> The remainder of the pattern uses shell pattern syntax. This is the default.</p>
<dt><code>N</code></p>
<dd> This is ignored. However, when it is the first letter and is used with file name generation, and no matches occur, the file pattern expands to the empty string.</p>
<dt><code>X</code></p>
<dd> The remainder of the pattern uses augmented regular expression syntax like the <i><a href="/docs/linux/man/1-xgrep/">xgrep</a></i>(1) command.</p>
<dt><code>P</code></p>
<dd> The remainder of the pattern uses <i><a href="/docs/linux/man/1-perl/">perl</a></i>(1) regular expression syntax. Not all perl regular expression syntax is currently implemented.</p>
<dt><code>V</code></p>
<dd> The remainder of the pattern uses System V regular expression syntax.</p>
<dt><code>i</code></p>
<dd> Treat the match as case insensitive.</p>
<dt><code>g</code></p>
<dd> File the longest match (greedy). This is the default.</p>
<dt><code>l</code></p>
<dd> Left anchor the pattern. This is the default for <code>K</code> style patterns.</p>
<dt><code>r</code></p>
<dd> Right anchor the pattern. This is the default for <code>K</code> style patterns.</dl>
</dl>
<p> If both <i>options</i> and <code>:</code><i>pattern-list</i> are specified, then the options apply only to <i>pattern-list</i>. Otherwise, these options remain in effect until they are disabled by a subsequent <code>&asymp;(</code><i>&#8230;</i><code>)</code> or at the end of the sub-pattern containing <code>&asymp;(</code><i>&#8230;</i><code>)</code>.</p>
<h3>Quoting.</h3>
<p> Each of the <i>metacharacters</i> listed earlier (see <i>Definitions</i> above) has a special meaning to the shell and causes termination of a word unless quoted. A character may be <i>quoted</i> (i.e., made to stand for itself) by preceding it with a <code>\</code>. The pair <code>
ew-line</code> is removed. All characters enclosed between a pair of single quote marks (<code>&#180;&#180;</code>) that is not preceded by a <code>$</code> are quoted. A single quote cannot appear within the single quotes. A single quoted string preceded by an unquoted <code>$</code> is processed as an ANSI-C string except for the following:</p>
<dl>
<dt><code>
