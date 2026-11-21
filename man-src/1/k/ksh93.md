---
title: "ksh93(1)"
name: "ksh93"
section: "1"
letter: "k"
url: "/docs/linux/man/1-ksh93/"
description: "ksh, rksh, pfksh – KornShell, a standard/restricted command and programming language"
---
<h2>SYNOPSIS</h2>
<p> <code>ksh</code> [ <code>&plusmn;abcefhiknoprstuvxBCDP</code> ] [ <code>-R</code> file ] [ <code>&plusmn;o</code> option ] ... [ <code>-</code> ] [ arg ... ]  </p>
<h2>DESCRIPTION</h2>
<p> <i>Ksh</i> is a command and programming language that executes commands read from a terminal or a file. <i>Rksh</i> is a restricted version of the command interpreter <i>ksh</i>; it is used to set up login names and execution environments whose capabilities are more controlled than those of the standard shell. <i>Rpfksh</i> is a profile shell version of the command interpreter <i>ksh</i>; it is used to to execute commands with the attributes specified by the user&#8217;s profiles (see <i>pfexec</i>(1)). See <i>Invocation</i> below for the meaning of arguments to the shell.  </p>
<h3>Definitions.</h3>
<p> A <i>metacharacter</i> is one of the following characters: </p>
<dl>
<dd> <p> <code>; &amp; ( ) | &lt; &gt; new-line space tab</code> </p>
 </dd></dl>
<p> A <i>blank</i> is a <code>tab</code> or a <code>space</code>. An <i>identifier</i> is a sequence of letters, digits, or underscores starting with a letter or underscore. Identifiers are used as components of <i>variable</i> names. A <i>vname</i> is a sequence of one or more identifiers separated by a <font SIZE="+2"><code>.</code></font> and optionally preceded by a <font SIZE="+2"><code>.</code></font>. Vnames are used as function and variable names. A <i>word</i> is a sequence of <i>characters</i> from the character set defined by the current locale, excluding non-quoted <i>metacharacters</i>. </p>
<p> A <i>command</i> is a sequence of characters in the syntax of the shell language. The shell reads each command and carries out the desired action either directly or by invoking separate utilities. A built-in command is a command that is carried out by the shell itself without creating a separate process. Some commands are built-in purely for convenience and are not documented here. Built-ins that cause side effects in the shell environment and built-ins that are found before performing a path search (see <i>Execution</i> below) are documented here. For historical reasons, some of these built-ins behave differently than other built-ins and are called <i>special built-ins</i>.  </p>
<h3>Commands.</h3>
<p> A <i>simple-command</i> is a list of variable assignments (see <i>Variable Assignments</i> below) or a sequence of <i>blank</i> separated words which may be preceded by a list of variable assignments (see <i>Environment</i> below). The first word specifies the name of the command to be executed. Except as specified below, the remaining words are passed as arguments to the invoked command. The command name is passed as argument 0 (see <i>exec</i>(2)). The <i>value</i> of a simple-command is its exit status; 0-255 if it terminates normally; 256+<i>signum</i> if it terminates abnormally (the name of the signal corresponding to the exit status can be obtained via the <code>-l</code> option of the <code>kill</code> built-in utility). </p>
<p> A <i>pipeline</i> is a sequence of one or more <i>commands</i> separated by <code>|</code>. The standard output of each command but the last is connected by a <i><a href="/docs/linux/man/2-pipe/">pipe</a></i>(2) to the standard input of the next command. Each command, except possibly the last, is run as a separate process; the shell waits for the last command to terminate. The exit status of a pipeline is the exit status of the last command unless the <code>pipefail</code> option is enabled. Each pipeline can be preceded by the <i>reserved word</i> <code>!</code> which causes the exit status of the pipeline to become 0 if the exit status of the last command is non-zero, and 1 if the exit status of the last command is 0. </p>
<p> A <i>list</i> is a sequence of one or more pipelines separated by <code>;</code>, <code>&amp;</code>, <code>|&amp;</code>, <code>&amp;&amp;</code>, or <code>||</code>, and optionally terminated by <code>;</code>, <code>&amp;</code>, or <code>|&amp;</code>. Of these five symbols, <code>;</code>, <code>&amp;</code>, and <code>|&amp;</code> have equal precedence, which is lower than that of <code>&amp;&amp;</code> and <code>||</code>. The symbols <code>&amp;&amp;</code> and <code>||</code> also have equal precedence. A semicolon (<code>;</code>) causes sequential execution of the preceding pipeline; an ampersand (<code>&amp;</code>) causes asynchronous execution of the preceding pipeline (i.e., the shell does <i>not</i> wait for that pipeline to finish). The symbol <code>|&amp;</code> causes asynchronous execution of the preceding pipeline with a two-way pipe established to the parent shell; the standard input and output of the spawned pipeline can be written to and read from by the parent shell by applying the redirection operators <code>&lt;&amp;</code> and <code>&gt;&amp;</code> with arg <code>p</code> to commands and by using <code>-p</code> option of the built-in commands <code>read</code> and <code>print</code> described later. The symbol <code>&amp;&amp;</code> (<code>||</code>) causes the <i>list</i> following it to be executed only if the preceding pipeline returns a zero (non-zero) value. One or more new-lines may appear in a <i>list</i> instead of a semicolon, to delimit a command. The first <i>item </i> of the first <i>pipeline</i> of a <i>list</i> that is a simple command not beginning with a redirection, and not occurring within a <code>while</code>, <code>until</code>, or <code>if</code> <i>list</i>, can be preceded by a semicolon. This semicolon is ignored unless the <code>showme</code> option is enabled as described with the <code>set</code> built-in below. </p>
<p> A <i>command</i> is either a simple-command or one of the following. Unless otherwise stated, the value returned by a command is that of the last simple-command executed in the command. </p>
<dl>
<dt><code>for</code><i>vname</i><code>in</code><i>word</i> ... ] <code>;do</code><i>list</i><code>;done</code></dt>
<dd> <p> Each time a <code>for</code> command is executed, <i>vname</i> is set to the next <i>word</i> taken from the <code>in</code> <i>word</i> list. If <code>in</code><i> word</i> ... is omitted, then the <code>for</code> command executes the <code>do</code> <i>list</i> once for each positional parameter that is set starting from <code>1</code> (see <i>Parameter Expansion</i> below). Execution ends when there are no more words in the list. </p>
 </dd>
<dt><code>for ((</code><i>expr1</i>] <code>;</code><i>expr2</i>] <code>;</code><i>expr3</i>] <code>))</code><code>;do</code><i>list</i><code>;done</code></dt>
<dd> <p> The arithmetic expression <i>expr1</i> is evaluated first (see <i>Arithmetic evaluation</i> below). The arithmetic expression <i>expr2</i> is repeatedly evaluated until it evaluates to zero and when non-zero, <i>list</i> is executed and the arithmetic expression <i>expr3</i> evaluated. If any expression is omitted, then it behaves as if it evaluated to 1. </p>
 </dd>
<dt><code>select</code><i>vname</i><code>in</code><i>word</i> ... ] <code>;do</code><i>list</i><code>;done</code></dt>
<dd> <p> A <code>select</code> command prints on standard error (file descriptor 2) the set of <i>word</i>s, each preceded by a number. If <code>in</code><i> word</i> ... is omitted, then the positional parameters starting from <code>1</code> are used instead (see <i>Parameter Expansion</i> below). The <font SIZE="-1"><code>PS3</code> </font> prompt is printed and a line is read from the standard input. If this line consists of the number of one of the listed <i>word</i>s, then the value of the variable <i>vname</i> is set to the <i>word</i> corresponding to this number. If this line is empty, the selection list is printed again. Otherwise the value of the variable <i>vname</i> is set to <i>null</i>. The contents of the line read from standard input is saved in the variable <font SIZE="-1"><code>REPLY</code>. </font> The <i>list</i> is executed for each selection until a <code>break</code> or <i>end-of-file</i> is encountered. If the <font SIZE="-1"><code>REPLY</code> </font> variable is set to <i>null</i> by the execution of <i>list</i>, then the selection list is printed before displaying the <font SIZE="-1"><code>PS3</code> </font> prompt for the next selection. </p>
 </dd>
<dt><code>case</code><i>word</i><code>in</code><code>(</code>]<i>pattern</i> | <i>pattern</i> ] ... <code>)</code><i>list</i><code>;;</code> ] ... <code>esac</code></dt>
<dd> <p> A <code>case</code> command executes the <i>list</i> associated with the first <i>pattern</i> that matches <i>word</i>. The form of the patterns is the same as that used for file-name generation (see <i>File Name Generation</i> below). The <code>;;</code> operator causes execution of <code>case</code> to terminate. If <code>;&amp;</code> is used in place of <code>;;</code> the next subsequent list, if any, is executed. </p>
 </dd>
<dt><code>if</code><i>list</i><code>;then</code><i>list</i><code>;elif</code><i>list</i><code>;then</code><i>list</i> ] ... <code>;else</code><i>list</i> ] <code>;fi</code></dt>
<dd> <p> The <i>list</i> following <code>if</code> is executed and, if it returns a zero exit status, the <i>list</i> following the first <code>then</code> is executed. Otherwise, the <i>list</i> following <code>elif</code> is executed and, if its value is zero, the <i>list</i> following the next <code>then</code> is executed. Failing each successive <code>elif</code> <i>list</i>, the <code>else</code> <i>list</i> is executed. If the <code>if</code> <i>list</i> has non-zero exit status and there is no <code>else</code> <i>list</i>, then the <code>if</code> command returns a zero exit status. </p>
 </dd>
<dd> <p> <code>while</code> <i>list</i> <code>;do</code> <i>list</i> <code>;done</code> </p>
 </dd>
<dt><code>until</code><i>list</i><code>;do</code><i>list</i><code>;done</code></dt>
<dd> <p> A <code>while</code> command repeatedly executes the <code>while</code> <i>list</i> and, if the exit status of the last command in the list is zero, executes the <code>do</code> <i>list</i>; otherwise the loop terminates. If no commands in the <code>do</code> <i>list</i> are executed, then the <code>while</code> command returns a zero exit status; <code>until</code> may be used in place of <code>while</code> to negate the loop termination test. </p>
 </dd>
<dt><code>((</code><i>expression</i><code>))</code></dt>
<dd> <p> <br />
 The <i>expression</i> is evaluated using the rules for arithmetic evaluation described below. If the value of the arithmetic expression is non-zero, the exit status is 0, otherwise the exit status is 1. </p>
 </dd>
<dt><code>(</code><i>list</i><code>)</code></dt>
<dd> <p> <br />
 Execute <i>list</i> in a separate environment. Note, that if two adjacent open parentheses are needed for nesting, a space must be inserted to avoid evaluation as an arithmetic command as described above. </p>
 </dd>
<dt><code>{ </code><i>list</i><code>;}</code></dt>
<dd> <p> <br />
 <i>list</i> is simply executed. Note that unlike the metacharacters <code>(</code> and <code>)</code>, <code>{</code> and <code>}</code> are <i>reserved word</i>s and must occur at the beginning of a line or after a <code>;</code> in order to be recognized. </p>
 </dd>
<dt><code>[[</code><i> expression </i><code>]]</code></dt>
<dd> <p> <br />
 Evaluates <i>expression</i> and returns a zero exit status when <i>expression</i> is true. See <i>Conditional Expressions</i> below, for a description of <i>expression</i>. </p>
 </dd>
<dd> <p> <code>function</code> <i>varname</i> <code>{</code> <i>list</i> <code>;}</code> </p>
 </dd>
<dt><i>varname</i><code>() {</code><i>list</i><code>;}</code></dt>
<dd> <p> Define a function which is referenced by <i>varname</i>. A function whose <i>varname</i> contains a <font SIZE="+2"><code>.</code></font> is called a discipline function and the portion of the <i>varname</i> preceding the last <font SIZE="+2"><code>.</code></font> must refer to an existing variable. The body of the function is the <i>list</i> of commands between <code>{</code> and <code>}</code>. A function defined with the <code>function</code> <i>varname</i> syntax can also be used as an argument to the <code>.</code> special built-in command to get the equivalent behavior as if the <i>varname</i><code>()</code> syntax were used to define it. (See <i>Functions</i> below.) </p>
 </dd>
<dt><code>namespace</code><i>identifier</i><code>{</code><i>list</i><code>;}</code></dt>
<dd> <p> <br />
 Defines or uses the name space <i>identifier</i> and runs the commands in <i>list</i> in this name space. (See <i>Name Spaces</i> below.) </p>
 </dd>
<dt><code>&amp;</code><i>name</i><i>arg...</i> ] ]</dt>
<dd> <p> Causes subsequent <i>list</i> commands terminated by <code>&amp;</code> to be placed in the background job pool <i>name</i>. If <i>name</i> is omitted a default unnamed pool is used. Commands in a named background pool may be executed remotely. </p>
 </dd>
<dt><code>time</code><i>pipeline</i> ]</dt>
<dd> <p> <br />
 If <i>pipeline</i> is omitted the user and system time for the current shell and completed child processes is printed on standard error. Otherwise, <i>pipeline</i> is executed and the elapsed time as well as the user and system time are printed on standard error. The <font SIZE="-1"><code>TIMEFORMAT</code> </font> variable may be set to a format string that specifies how the timing information should be displayed. See <code>Shell Variables</code> below for a description of the <font SIZE="-1"><code>TIMEFORMAT</code> </font> variable. </p>
 </dd></dl>
<p> The following reserved words are recognized as reserved only when they are the first word of a command and are not quoted: </p>
<p> <code>if then else elif fi case esac for while until do done { } function select time [[ ]] ! </code>  </p>
<h3>Variable Assignments.</h3>
<p> One or more variable assignments can start a simple command or can be arguments to the <code>typeset</code>, <code>enum</code>, <code>export</code>, or <code>readonly</code> special built-in commands as well as to other declaration commands created as types. The syntax for an <i>assignment</i> is of the form: </p>
<dl>
<dd> <p> <i>varname</i><code>=</code><i>word</i> </p>
 </dd>
<dt><i>varname</i><code>[</code><i>word</i><code>]</code>=<i>word</i></dt>
<dd> <p> No space is permitted between <i>varname</i> and the <code>=</code> or between <code>=</code> and <i>word</i>. </p>
 </dd>
<dt><i>varname</i><code>=(</code><i>assign_list</i><code>)</code></dt>
<dd> <p> No space is permitted between <i>varname</i> and the <code>=</code>. The variable <i>varname</i> is unset before the assignment. An <i>assign_list</i> can be one of the following: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><i>word</i> ...</dt>
<dd> <p> Indexed array assignment. </p>
 </dd>
<dt><code>[</code><i>word</i><code>]=</code><i>word</i> ...</dt>
<dd> <p> Associative array assignment. If preceded by <code>typeset -a</code> this will create an indexed array instead. </p>
 </dd>
<dt><i>assignment</i> ...</dt>
<dd> <p> Compound variable assignment. This creates a compound variable <i>varname</i> with sub-variables of the form <i>varname</i><code>.</code><i>name</i>, where <i>name</i> is the name portion of <i>assignment</i>. The value of <i>varname</i> will contain all the assignment elements. Additional assignments made to sub-variables of <i>varname</i> will also be displayed as part of the value of <i>varname</i>. If no <i>assignment</i>s are specified, <i>varname</i> will be a compound variable allowing subsequence child elements to be defined. </p>
 </dd>
<dt><code>typeset</code><i>options</i>] <i>assignment</i> ...</dt>
<dd> <p> Nested variable assignment. Multiple assignments can be specified by separating each of them with a <code>;</code>. The previous value is unset before the assignment. Other declaration commands such as <code>readonly,</code> <code>enum</code>, and other declaration commands can be used in place of <code>typeset</code>. </p>
 </dd>
<dt><code>.</code><i>filename</i></dt>
<dd> <p> Include the assignment commands contained in <i>filename</i>. </p>
 </dd></dl>
</dl>
</dl>
<p> In addition, a <code>+=</code> can be used in place of the <code>=</code> to signify adding to or appending to the previous value. When <code>+=</code> is applied to an arithmetic type, <i>word</i> is evaluated as an arithmetic expression and added to the current value. When applied to a string variable, the value defined by <i>word</i> is appended to the value. For compound assignments, the previous value is not unset and the new values are appended to the current ones provided that the types are compatible. </p>
<p> The right hand side of a variable assignment undergoes all the expansion listed below except word splitting, brace expansion, and file name generation. When the left hand side is an assignment is a compound variable and the right hand is the name of a compound variable, the compound variable on the right will be copied or appended to the compound variable on the left.  </p>
<h3>Comments.</h3>
<p> A word beginning with <code>#</code> causes that word and all the following characters up to a new-line to be ignored.  </p>
<h3>Aliasing.</h3>
<p> The first word of each command is replaced by the text of an <code>alias</code> if an <code>alias</code> for this word has been defined. An <code>alias</code> name consists of any number of characters excluding metacharacters, quoting characters, file expansion characters, parameter expansion and command substitution characters, the characters <code>/</code> and <code>=</code>. The replacement string can contain any valid shell script including the metacharacters listed above. The first word of each command in the replaced text, other than any that are in the process of being replaced, will be tested for aliases. If the last character of the alias value is a <i>blank</i> then the word following the alias will also be checked for alias substitution. Aliases can be used to redefine built-in commands but cannot be used to redefine the reserved words listed above. Aliases can be created and listed with the <code>alias</code> command and can be removed with the <code>unalias</code> command. </p>
<p> <i>Aliasing</i> is performed when scripts are read, not while they are executed. Therefore, for an alias to take effect, the <code>alias</code> definition command has to be executed before the command which references the alias is read. </p>
<p> The following aliases are compiled into the shell but can be unset or redefined: </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>autoload=&#180;typeset -fu&#180;</code></dt>
<dd>  </dd>
<dt><code>command=&#180;command &#180;</code></dt>
<dd>  </dd>
<dt><code>compound=&#180;typeset -C&#180;</code></dt>
<dd>  </dd>
<dt><code>fc=hist</code></dt>
<dd>  </dd>
<dt><code>float=&#180;typeset -lE&#180;</code></dt>
<dd>  </dd>
<dt><code>functions=&#180;typeset -f&#180;</code></dt>
<dd>  </dd>
<dt><code>hash=&#180;alias -t --&#180;</code></dt>
<dd>  </dd>
<dt><code>history=&#180;hist -l&#180;</code></dt>
<dd>  </dd>
<dt><code>integer=&#180;typeset -li&#180;</code></dt>
<dd>  </dd>
<dt><code>nameref=&#180;typeset -n&#180;</code></dt>
<dd>  </dd>
<dt><code>nohup=&#180;nohup &#180;</code></dt>
<dd>  </dd>
<dt><code>r=&#180;hist -s&#180;</code></dt>
<dd>  </dd>
<dt><code>redirect=&#180;command exec&#180;</code></dt>
<dd>  </dd>
<dt><code>source=&#180;command </code><font SIZE="+2"><code>.</code></font><code>&#180;</code></dt>
<dd>  </dd>
<dt><code>stop=&#180;kill -s </code><font SIZE="-1"><code>STOP</code></font><code>&#180;</code></dt>
<dd>  </dd>
<dt><code>suspend=&#180;kill -s </code><font SIZE="-1"><code>STOP</code></font><code> $$&#180;</code></dt>
<dd>  </dd>
<dt><code>times=&#180;{ { time;} 2&gt;&amp;1;}&#180;</code></dt>
<dd>  </dd>
<dt><code>type=&#180;whence -v&#180;</code></dt>
<dd>  </dd></dl>
</dl>
<h3>Tilde Substitution.</h3>
<p> After alias substitution is performed, each word is checked to see if it begins with an unquoted <code>&asymp;</code>. For tilde substitution, <i>word</i> also refers to the <i>word</i> portion of parameter expansion (see <i>Parameter Expansion</i> below). If it does, then the word up to a <code>/</code> is checked to see if it matches a user name in the password database (See <i>getpwname</i>(3).) If a match is found, the <code>&asymp;</code> and the matched login name are replaced by the login directory of the matched user. If no match is found, the original text is left unchanged. A <code>&asymp;</code> by itself, or in front of a <code>/</code>, is replaced by <font SIZE="-1"><code>$HOME</code>. </font> A <code>&asymp;</code> followed by a <code>+</code> or <code>-</code> is replaced by the value of <font SIZE="-1"><code>$PWD</code></font> and <font SIZE="-1"><code>$OLDPWD</code></font> respectively. </p>
<p> In addition, when expanding a <i>variable assignment</i>, <i>tilde</i> substitution is attempted when the value of the assignment begins with a <code>&asymp;</code>, and when a <code>&asymp;</code> appears after a <code>:</code>. The <code>:</code> also terminates a <code>&asymp;</code> login name.  </p>
<h3>Command Substitution.</h3>
<p> The standard output from a command list enclosed in parentheses preceded by a dollar sign ( <code>$(</code><i>list</i><code>)</code> ), or in a brace group preceded by a dollar sign ( <code>${ </code><i>list</i><code>;}</code> ), or in a pair of grave accents (<code><font SIZE="+4">`</font><font SIZE="+4">`</font></code>) may be used as part or all of a word; trailing new-lines are removed. In the second case, the <code>{</code> and <code>}</code> are treated as a reserved words so that <code>{</code> must be followed by a <i>blank</i> and <code>}</code> must appear at the beginning of the line or follow a <code>;</code>. In the third (obsolete) form, the string between the quotes is processed for special quoting characters before the command is executed (see <i>Quoting</i> below). The command substitution <code>$(cat file)</code> can be replaced by the equivalent but faster <code>$(&lt;file)</code>. The command substitution <code>$(</code><i>n</i><code>&lt;#)</code> will expand to the current byte offset for file descriptor <i>n</i>. Except for the second form, the command list is run in a subshell so that no side effects are possible. For the second form, the final <code>}</code> will be recognized as a reserved word after any token.  </p>
<h3>Arithmetic Substitution.</h3>
<p> An arithmetic expression enclosed in double parentheses preceded by a dollar sign ( <code>$(())</code> ) is replaced by the value of the arithmetic expression within the double parentheses.  </p>
<h3>Process Substitution.</h3>
<p> Each command argument of the form <code>&lt;(</code><i>list</i><code>)</code> or <code>&gt;(</code><i>list</i><code>)</code> will run process <i>list</i> asynchronously connected to some file in <code>/dev/fd</code> if this directory exists, or else a fifo a temporary directory. The name of this file will become the argument to the command. If the form with <code>&gt;</code> is selected then writing on this file will provide input for <i>list</i>. If <code>&lt;</code> is used, then the file passed as an argument will contain the output of the <i>list</i> process. For example, </p>
<dl>
<dd> <p> <code>paste &lt;(cut -f1</code> <i>file1</i><code>) &lt;(cut -f3</code> <i>file2</i><code>) | tee &gt;(</code><i>process1</i><code>) &gt;(</code><i>process2</i><code>)</code> </p>
 </dd></dl>
<p> <i>cuts</i> fields 1 and 3 from the files <i>file1</i> and <i>file2</i> respectively, <i>pastes</i> the results together, and sends it to the processes <i>process1</i> and <i>process2</i>, as well as putting it onto the standard output. Note that the file, which is passed as an argument to the command, is a UNIX <i><a href="/docs/linux/man/2-pipe/">pipe</a></i>(2) so programs that expect to <i><a href="/docs/linux/man/2-lseek/">lseek</a></i>(2) on the file will not work. </p>
<p> Process substitution of the form <code>&lt;(</code><i>list</i><code>)</code> can also be used with the <code>&lt;</code> redirection operator which causes the output of <i>list</i> to be standard input or the input for whatever file descriptor is specified.  </p>
<h3>Parameter Expansion.</h3>
<p> A <i>parameter</i> is a <i>variable</i>, one or more digits, or any of the characters <code>*</code>, <code>@</code>, <code>#</code>, <code>?</code>, <code>-</code>, <code>$</code>, and <code>!\^</code>. A <i>variable</i> is denoted by a <i>vname</i>. To create a variable whose <i>vname</i> contains a <font SIZE="+2"><code>.</code></font>, a variable whose <i>vname</i> consists of everything before the last <font SIZE="+2"><code>.</code></font> must already exist. A <i>variable</i> has a <i>value</i> and zero or more <i>attributes</i>. <i>Variables</i> can be assigned <i>values</i> and <i>attributes</i> by using the <code>typeset</code> special built-in command. The attributes supported by the shell are described later with the <code>typeset</code> special built-in command. Exported variables pass values and attributes to the environment. </p>
<p> The shell supports both indexed and associative arrays. An element of an array variable is referenced by a <i>subscript</i>. A <i>subscript</i> for an indexed array is denoted by an <i>arithmetic expression</i> (see <i>Arithmetic evaluation</i> below) between a <code>[</code> and a <code>]</code>. To assign values to an indexed array, use <i>vname</i><code>=(</code><i>value</i> ...<code>)</code> or <code>set -A</code> <i>vname</i> <i>value</i> ... . The value of all non-negative subscripts must be in the range of 0 through 4,194,303. A negative subscript is treated as an offset from the maximum current index +1 so that -1 refers to the last element. Indexed arrays can be declared with the <code>-a</code> option to <code>typeset.</code> Indexed arrays need not be declared. Any reference to a variable with a valid subscript is legal and an array will be created if necessary. </p>
<p> An associative array is created with the <code>-A</code> option to <code>typeset.</code> A <i>subscript</i> for an associative array is denoted by a string enclosed between <code>[</code> and <code>]</code>. </p>
<p> Referencing any array without a subscript is equivalent to referencing the array with subscript 0. </p>
<p> The <i>value</i> of a <i>variable</i> may be assigned by writing: </p>
<dl>
<dd> <p> <i>vname</i><code>=</code><i>value</i> <i>vname</i><code>=</code><i>value</i> ] ... </p>
 </dd></dl>
<p> or </p>
<dl>
<dd> <p> <i>vname</i><code>[</code><i>subscript</i><code>]=</code><i>value</i> <i>vname</i><code>[</code><i>subscript</i><code>]=</code><i>value</i> ] ... </p>
 </dd></dl>
<p> Note that no space is allowed before or after the <code>=</code>. </p>
<p> Attributes assigned by the <i>typeset</i> special built-in command apply to all elements of the array. An array element can be a simple variable, a compound variable or an array variable. An element of an indexed array can be either an indexed array or an associative array. An element of an associative array can also be either. To refer to an array element that is part of an array element, concatenate the subscript in brackets. For example, to refer to the <i>foobar</i> element of an associative array that is defined as the third element of the indexed array, use <code>${</code><i>vname</i><code>[</code><i>3</i><code>][</code><i>foobar</i><code>]}</code> </p>
<p> A <i>nameref</i> is a variable that is a reference to another variable. A nameref is created with the <code>-n</code> attribute of <code>typeset</code>. The value of the variable at the time of the <code>typeset</code> command becomes the variable that will be referenced whenever the nameref variable is used. The name of a nameref cannot contain a <font SIZE="+2"><code>.</code></font>. When a variable or function name contains a <font SIZE="+2"><code>.</code></font>, and the portion of the name up to the first <font SIZE="+2"><code>.</code></font> matches the name of a nameref, the variable referred to is obtained by replacing the nameref portion with the name of the variable referenced by the nameref. If a nameref is used as the index of a <code>for</code> loop, a name reference is established for each item in the list. A nameref provides a convenient way to refer to the variable inside a function whose name is passed as an argument to a function. For example, if the name of a variable is passed as the first argument to a function, the command </p>
<dl>
<dd> <p> <code>typeset -n var=$1</code> </p>
 </dd></dl>
<p> inside the function causes references and assignments to <code>var</code> to be references and assignments to the variable whose name has been passed to the function. </p>
<p> If any of the floating point attributes, <code>-E</code>, <code>-F</code>, or <code>-X</code>, or the integer attribute, <code>-i</code>, is set for <i>vname</i>, then the <i>value</i> is subject to arithmetic evaluation as described below. </p>
<p> Positional parameters, parameters denoted by a number, may be assigned values with the <code>set</code> special built-in command. Parameter <code>$0</code> is set from argument zero when the shell is invoked. </p>
<p> The character <code>$</code> is used to introduce substitutable <i>parameters</i>. </p>
<dl>
<dt><code>${</code><i>parameter</i><code>}</code></dt>
<dd> <p> The shell reads all the characters from <code>${</code> to the matching <code>}</code> as part of the same word even if it contains braces or metacharacters. The value, if any, of the parameter is substituted. The braces are required when <i>parameter</i> is followed by a letter, digit, or underscore that is not to be interpreted as part of its name, when the variable name contains a <font SIZE="+2"><code>.</code></font>. The braces are also required when a variable is subscripted unless it is part of an Arithmetic Expression or a Conditional Expression. If <i>parameter</i> is one or more digits then it is a positional parameter. A positional parameter of more than one digit must be enclosed in braces. If <i>parameter</i> is <code>*</code> or <code>@</code>, then all the positional parameters, starting with <code>$1</code>, are substituted (separated by a field separator character). If an array <i>vname</i> with last subscript <code>*</code> <code>@</code>, or for index arrays of the form <i>sub1</i> <code>..</code> <i>sub2</i>. is used, then the value for each of the elements between <i>sub1</i> and <i>sub2</i> inclusive (or all elements for <code>*</code> and <code>@</code>) is substituted, separated by the first character of the value of <font SIZE="-1"><code>IFS</code>. </font> </p>
 </dd>
<dt><code>${#</code><i>parameter</i><code>}</code></dt>
<dd> <p> If <i>parameter</i> is <code>*</code> or <code>@</code>, the number of positional parameters is substituted. Otherwise, the length of the value of the <i>parameter</i> is substituted. </p>
 </dd>
<dd> <p> <code>${#</code><i>vname</i><code>[*]}</code> </p>
 </dd>
<dd> <p> <code>${#</code><i>vname</i><code>[@]}</code> The number of elements in the array <i>vname</i> is substituted. </p>
 </dd>
<dd> <p> <code>${@</code><i>vname</i><code>}</code> Expands to the type name (See <i>Type Variables</i> below) or attributes of the variable referred to by <i>vname</i>. </p>
 </dd>
<dt><code>${!</code><i>vname</i><code>}</code></dt>
<dd> <p> Expands to the name of the variable referred to by <i>vname</i>. This will be <i>vname</i> except when <i>vname</i> is a name reference. </p>
 </dd>
<dt><code>${!</code><i>vname</i><code>[</code><i>subscript</i><code>]}</code></dt>
<dd> <p> Expands to name of the subscript unless <i>subscript</i> is <code>*</code>, <code>@</code>. or of the form <i>sub1</i> <code>..</code> <i>sub2</i>. When <i>subscript</i> is <code>*</code>, the list of array subscripts for <i>vname</i> is generated. For a variable that is not an array, the value is 0 if the variable is set. Otherwise it is null. When <i>subscript</i> is <code>@</code>, same as above, except that when used in double quotes, each array subscript yields a separate argument. When <i>subscript</i> is of the form <i>sub1</i> <code>..</code> <i>sub2</i> it expands to the list of subscripts between <i>sub1</i> and <i>sub2</i> inclusive using the same quoting rules as <code>@</code>. </p>
 </dd>
<dt><code>${!</code><i>prefix</i><code>*}</code></dt>
<dd> <p> Expands to the names of the variables whose names begin with <i>prefix</i>. </p>
 </dd>
<dt><code>${</code><i>parameter</i><code>:-</code><i>word</i><code>}</code></dt>
<dd> <p> If <i>parameter</i> is set and is non-null then substitute its value; otherwise substitute <i>word</i>. </p>
 </dd>
<dt><code>${</code><i>parameter</i><code>:=</code><i>word</i><code>}</code></dt>
<dd> <p> If <i>parameter</i> is not set or is null then set it to <i>word</i>; the value of the parameter is then substituted. Positional parameters may not be assigned to in this way. </p>
 </dd>
<dt><code>${</code><i>parameter</i><code>:?</code><i>word</i><code>}</code></dt>
<dd> <p> If <i>parameter</i> is set and is non-null then substitute its value; otherwise, print <i>word</i> and exit from the shell (if not interactive). If <i>word</i> is omitted then a standard message is printed. </p>
 </dd>
<dt><code>${</code><i>parameter</i><code>:+</code><i>word</i><code>}</code></dt>
<dd> <p> If <i>parameter</i> is set and is non-null then substitute <i>word</i>; otherwise substitute nothing. </p>
 </dd></dl>
<p> In the above, <i>word</i> is not evaluated unless it is to be used as the substituted string, so that, in the following example, <code>pwd</code> is executed only if <code>d</code> is not set or is null: </p>
<dl>
<dd> <p> print ${d:-$(pwd)} </p>
 </dd></dl>
<p> If the colon ( <code>: )</code> is omitted from the above expressions, then the shell only checks whether <i>parameter</i> is set or not. </p>
<dl>
<dd> <p> <code>${</code><i>parameter</i><code>:</code><i>offset</i><code>:</code><i>length</i><code>}</code> </p>
 </dd>
<dt><code>${</code><i>parameter</i><code>:</code><i>offset</i><code>}</code></dt>
<dd> <p> Expands to the portion of the value of <i>parameter</i> starting at the character (counting from <code>0</code>) determined by expanding <i>offset</i> as an arithmetic expression and consisting of the number of characters determined by the arithmetic expression defined by <i>length.</i> In the second form, the remainder of the value is used. If A negative <i>offset</i> counts backwards from the end of <i>parameter</i>. Note that one or more <i>blank</i>s is required in front of a minus sign to prevent the shell from interpreting the operator as <code>:-</code>. If <i>parameter</i> is <code>*</code> or <code>@</code>, or is an array name indexed by <code>*</code> or <code>@</code>, then <i>offset</i> and <i>length</i> refer to the array index and number of elements respectively. A negative <i>offset</i> is taken relative to one greater than the highest subscript for indexed arrays. The order for associate arrays is unspecified. </p>
 </dd>
<dd> <p> <code>${</code><i>parameter</i><code>#</code><i>pattern</i><code>}</code> </p>
 </dd>
<dt><code>${</code><i>parameter</i><code>##</code><i>pattern</i><code>}</code></dt>
<dd> <p> If the shell <i>pattern</i> matches the beginning of the value of <i>parameter</i>, then the value of this expansion is the value of the <i>parameter</i> with the matched portion deleted; otherwise the value of this <i>parameter</i> is substituted. In the first form the smallest matching pattern is deleted and in the second form the largest matching pattern is deleted. When <i>parameter</i> is <code>@</code>, <code>*</code>, or an array variable with subscript <code>@</code> or <code>*</code>, the substring operation is applied to each element in turn. </p>
 </dd>
<dd> <p> <code>${</code><i>parameter</i><code>%</code><i>pattern</i><code>}</code> </p>
 </dd>
<dt><code>${</code><i>parameter</i><code>%%</code><i>pattern</i><code>}</code></dt>
<dd> <p> If the shell <i>pattern</i> matches the end of the value of <i>parameter</i>, then the value of this expansion is the value of the <i>parameter</i> with the matched part deleted; otherwise substitute the value of <i>parameter</i>. In the first form the smallest matching pattern is deleted and in the second form the largest matching pattern is deleted. When <i>parameter</i> is <code>@</code>, <code>*</code>, or an array variable with subscript <code>@</code> or <code>*</code>, the substring operation is applied to each element in turn. </p>
 </dd>
<dd> <p> <code>${</code><i>parameter</i><code>/</code><i>pattern</i><code>/</code><i>string</i><code>}</code> </p>
 </dd>
<dt><code>${</code><i>parameter</i><code>//</code><i>pattern</i><code>/</code><i>string</i><code>}</code></dt>
<dd>  </dd>
<dt><code>${</code><i>parameter</i><code>/#</code><i>pattern</i><code>/</code><i>string</i><code>}</code></dt>
<dd>  </dd>
<dt><code>${</code><i>parameter</i><code>/%</code><i>pattern</i><code>/</code><i>string</i><code>}</code></dt>
<dd> <p> Expands <i>parameter</i> and replaces the longest match of <i>pattern</i> with the given <i>string.</i> Each occurrence of <code>\</code><i>n</i> in <i>string</i> is replaced by the portion of <i>parameter</i> that matches the <i>n</i>-th sub-pattern. In the first form, only the first occurrence of <i>pattern</i> is replaced. In the second form, each match for <i>pattern</i> is replaced by the given <i>string.</i> The third form restricts the pattern match to the beginning of the string while the fourth form restricts the pattern match to the end of the string. When <i>string</i> is null, the <i>pattern</i> will be deleted and the <code>/</code> in front of <i>string</i> may be omitted. When <i>parameter</i> is <code>@</code>, <code>*</code>, or an array variable with subscript <code>@</code> or <code>*</code>, the substitution operation is applied to each element in turn. In this case, the <i>string</i> portion of <i>word</i> will be re-evaluated for each element. </p>
 </dd></dl>
<p> The following parameters are automatically set by the shell: </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>#</code></dt>
<dd> <p> The number of positional parameters in decimal. </p>
 </dd>
<dt><code>-</code></dt>
<dd> <p> Options supplied to the shell on invocation or by the <code>set</code> command. </p>
 </dd>
<dt><code>?</code></dt>
<dd> <p> The decimal value returned by the last executed command. </p>
 </dd>
<dt><code>$</code></dt>
<dd> <p> The process number of this shell. </p>
 </dd>
<dt><code>_</code></dt>
<dd> <p> Initially, the value of <code>_</code> is an absolute pathname of the shell or script being executed as passed in the <i>environment</i>. Subsequently it is assigned the last argument of the previous command. This parameter is not set for commands which are asynchronous. This parameter is also used to hold the name of the matching <font SIZE="-1"><code>MAIL</code></font> file when checking for mail. While defining a compound variable or a type, <code>_</code> is initialized as a reference to the compound variable or type. When a discipline function is invoked, <code>_</code> is initialized as a reference to the variable associated with the call to this function. Finally when <code>_</code> is used as the name of the first variable of a type definition, the new type is derived from the type of the first variable (See <i>Type Variables</i> below.). </p>
 </dd>
<dt><code>!</code></dt>
<dd> <p> The process id or the pool name and job number of the last background command invoked or the most recent job put in the background with the <code>bg</code> built-in command. Background jobs started in a named pool will be in the form <i>pool</i><code>.</code><i>number</i> where <i>pool</i> is the pool name and <i>number</i> is the job number within that pool. </p>
 </dd>
<dt><code>.sh.command</code></dt>
<dd> <p> When processing a <font SIZE="-1"><code>DEBUG</code> </font> trap, this variable contains the current command line that is about to run. </p>
 </dd>
<dt><code>.sh.edchar</code></dt>
<dd> <p> This variable contains the value of the keyboard character (or sequence of characters if the first character is an ESC, ascii <code>033</code>) that has been entered when processing a <font SIZE="-1"><code>KEYBD</code></font> trap (see <i>Key Bindings</i> below). If the value is changed as part of the trap action, then the new value replaces the key (or key sequence) that caused the trap. </p>
 </dd>
<dt><code>.sh.edcol</code></dt>
<dd> <p> The character position of the cursor at the time of the most recent <font SIZE="-1"><code>KEYBD</code></font> trap. </p>
 </dd>
<dt><code>.sh.edmode</code></dt>
<dd> <p> The value is set to ESC when processing a <font SIZE="-1"><code>KEYBD</code></font> trap while in <code>vi</code> insert mode. (See <i>Vi Editing Mode</i> below.) Otherwise, <code>.sh.edmode</code> is null when processing a <font SIZE="-1"><code>KEYBD</code></font> trap. </p>
 </dd>
<dt><code>.sh.edtext</code></dt>
<dd> <p> The characters in the input buffer at the time of the most recent <font SIZE="-1"><code>KEYBD</code></font> trap. The value is null when not processing a <font SIZE="-1"><code>KEYBD</code></font> trap. </p>
 </dd>
<dt><code>.sh.file</code></dt>
<dd> <p> The pathname of the file than contains the current command. </p>
 </dd>
<dt><code>.sh.fun</code></dt>
<dd> <p> The name of the current function that is being executed. </p>
 </dd>
<dt><code>.sh.level</code></dt>
<dd> <p> Set to the current function depth. This can be changed inside a DEBUG trap and will set the context to the specified level. </p>
 </dd>
<dt><code>.sh.lineno</code></dt>
<dd> <p> Set during a DEBUG trap to the line number for the caller of each function. </p>
 </dd>
<dt><code>.sh.match</code></dt>
<dd> <p> An indexed array which stores the most recent match and sub-pattern matches after conditional pattern matches that match and after variables expansions using the operators <code>#</code>, <code>%</code>, or <code>/</code>. The <code>0</code>-th element stores the complete match and the <i>i</i>-th. element stores the <i>i</i>-th submatch. The <code>.sh.match</code> variable becomes unset when the variable that has expanded is assigned a new value. </p>
 </dd>
<dt><code>.sh.math</code></dt>
<dd> <p> Used for defining arithmetic functions (see <i>Arithmetic evaluation</i> below). and stores the list of user defined arithmetic functions. </p>
 </dd>
<dt><code>.sh.name</code></dt>
<dd> <p> Set to the name of the variable at the time that a discipline function is invoked. </p>
 </dd>
<dt><code>.sh.subscript</code></dt>
<dd> <p> Set to the name subscript of the variable at the time that a discipline function is invoked. </p>
 </dd>
<dt><code>.sh.subshell</code></dt>
<dd> <p> The current depth for subshells and command substitution. </p>
 </dd>
<dt><code>.sh.value</code></dt>
<dd> <p> Set to the value of the variable at the time that the <code>set</code> or <code>append</code> discipline function is invoked. When a user defined arithmetic function is invoked, the value of <code>.sh.value</code> is saved and <code>.sh.value</code> is set to long double precision floating point. <code>.sh.value</code> is restored when the function returns. </p>
 </dd>
<dt><code>.sh.version</code></dt>
<dd> <p> Set to a value that identifies the version of this shell. </p>
 </dd>
<dt><font SIZE="-1"><code>KSH_VERSION</code></font></dt>
<dd> <p> A name reference to <code>.sh.version</code>. </p>
 </dd>
<dt><font SIZE="-1"><code>LINENO</code></font></dt>
<dd> <p> The current line number within the script or function being executed. </p>
 </dd>
<dt><font SIZE="-1"><code>OLDPWD</code></font></dt>
<dd> <p> The previous working directory set by the <code>cd</code> command. </p>
 </dd>
<dt><font SIZE="-1"><code>OPTARG</code></font></dt>
<dd> <p> The value of the last option argument processed by the <code>getopts</code> built-in command. </p>
 </dd>
<dt><font SIZE="-1"><code>OPTIND</code></font></dt>
<dd> <p> The index of the last option argument processed by the <code>getopts</code> built-in command. </p>
 </dd>
<dt><font SIZE="-1"><code>PPID</code></font></dt>
<dd> <p> The process number of the parent of the shell. </p>
 </dd>
<dt><font SIZE="-1"><code>PWD</code></font></dt>
<dd> <p> The present working directory set by the <code>cd</code> command. </p>
 </dd>
<dt><font SIZE="-1"><code>RANDOM</code></font></dt>
<dd> <p> Each time this variable is referenced, a random integer, uniformly distributed between 0 and 32767, is generated. The sequence of random numbers can be initialized by assigning a numeric value to <font SIZE="-1"><code>RANDOM</code>. </font> </p>
 </dd>
<dt><font SIZE="-1"><code>REPLY</code></font></dt>
<dd> <p> This variable is set by the <code>select</code> statement and by the <code>read</code> built-in command when no arguments are supplied. </p>
 </dd>
<dt><font SIZE="-1"><code>SECONDS</code></font></dt>
<dd> <p> Each time this variable is referenced, the number of seconds since shell invocation is returned. If this variable is assigned a value, then the value returned upon reference will be the value that was assigned plus the number of seconds since the assignment. </p>
 </dd>
<dt><font SIZE="-1"><code>SHLVL</code></font></dt>
<dd> <p> An integer variable the is incremented each time the shell is invoked and is exported. If <font SIZE="-1"><code>SHLVL</code> </font> is not in the environment when the shell is invoked, it is set to 1. </p>
 </dd></dl>
</dl>
<p> The following variables are used by the shell: </p>
<dl>
<dd>  </dd>
<dl>
<dt><font SIZE="-1"><code>CDPATH</code></font></dt>
<dd> <p> The search path for the <code>cd</code> command. </p>
 </dd>
<dt><font SIZE="-1"><code>COLUMNS</code></font></dt>
<dd> <p> If this variable is set, the value is used to define the width of the edit window for the shell edit modes and for printing <code>select</code> lists. </p>
 </dd>
<dt><font SIZE="-1"><code>EDITOR</code></font></dt>
<dd> <p> If the <font SIZE="-1"><code>VISUAL</code></font> variable is not set, the value of this variable will be checked for the patterns as described with <font SIZE="-1"><code>VISUAL</code></font> below and the corresponding editing option (see Special Command <code>set</code> below) will be turned on. </p>
 </dd>
<dt><font SIZE="-1"><code>ENV</code></font></dt>
<dd> <p> If this variable is set, then parameter expansion, command substitution, and arithmetic substitution are performed on the value to generate the pathname of the script that will be executed when the shell is invoked interactively (see <i>Invocation</i> below). This file is typically used for <code>alias</code> and <code>function</code> definitions. The default value is <code>$HOME/.kshrc</code>. On systems that support a system wide <code>/etc/ksh.kshrc</code> initialization file, if the filename generated by the expansion of <font SIZE="-1"><code>ENV</code> </font> begins with <code>/./</code> or <code>././</code> the system wide initialization file will not be executed. </p>
 </dd>
<dt><font SIZE="-1"><code>FCEDIT</code></font></dt>
<dd> <p> Obsolete name for the default editor name for the <code>hist</code> command. <font SIZE="-1"><code>FCEDIT</code></font> is not used when <font SIZE="-1"><code>HISTEDIT</code></font> is set. </p>
 </dd>
<dt><font SIZE="-1"><code>FIGNORE</code></font></dt>
<dd> <p> A pattern that defines the set of filenames that will be ignored when performing filename matching. </p>
 </dd>
<dt><font SIZE="-1"><code>FPATH</code></font></dt>
<dd> <p> The search path for function definitions. The directories in this path are searched for a file with the same name as the function or command when a function with the <code>-u</code> attribute is referenced and when a command is not found. If an executable file with the name of that command is found, then it is read and executed in the current environment. Unlike <font SIZE="-1"><code>PATH</code>, </font> the current directory must be represented explicitly by <code>.</code> rather than by adjacent <code>:</code> characters or a beginning or ending <code>:</code>. </p>
 </dd>
<dt><font SIZE="-1"><code>HISTCMD</code></font></dt>
<dd> <p> Number of the current command in the history file. </p>
 </dd>
<dt><font SIZE="-1"><code>HISTEDIT</code></font></dt>
<dd> <p> Name for the default editor name for the <code>hist</code> command. </p>
 </dd>
<dt><font SIZE="-1"><code>HISTFILE</code></font></dt>
<dd> <p> If this variable is set when the shell is invoked, then the value is the pathname of the file that will be used to store the command history (see <i>Command Re-entry</i> below). </p>
 </dd>
<dt><font SIZE="-1"><code>HISTSIZE</code></font></dt>
<dd> <p> If this variable is set when the shell is invoked, then the number of previously entered commands that are accessible by this shell will be greater than or equal to this number. The default is 512. </p>
 </dd>
<dt><font SIZE="-1"><code>HOME</code></font></dt>
<dd> <p> The default argument (home directory) for the <code>cd</code> command. </p>
 </dd>
<dt><font SIZE="-1"><code>IFS</code></font></dt>
<dd> <p> Internal field separators, normally <code>space</code>, <code>tab</code>, and <code>new-line</code> that are used to separate the results of command substitution or parameter expansion and to separate fields with the built-in command <code>read</code>. The first character of the <font SIZE="-1"><code>IFS</code> </font> variable is used to separate arguments for the <code>&quot;$*&quot;</code> substitution (see <i>Quoting</i> below). Each single occurrence of an <font SIZE="-1"><code>IFS</code> </font> character in the string to be split, that is not in the <i>isspace</i> character class, and any adjacent characters in <font SIZE="-1"><code>IFS</code> </font> that are in the <i>isspace</i> character class, delimit a field. One or more characters in <font SIZE="-1"><code>IFS</code> </font> that belong to the <i>isspace</i> character class, delimit a field. In addition, if the same <i>isspace</i> character appears consecutively inside <font SIZE="-1"><code>IFS</code>, </font> this character is treated as if it were not in the <i>isspace</i> class, so that if <font SIZE="-1"><code>IFS</code> </font> consists of two <code>tab</code> characters, then two adjacent <code>tab</code> characters delimit a null field. </p>
 </dd>
<dt><font SIZE="-1"><code>JOBMAX</code></font></dt>
<dd> <p> This variable defines the maximum number running background jobs that can run at a time. When this limit is reached, the shell will wait for a job to complete before staring a new job. </p>
 </dd>
<dt><font SIZE="-1"><code>LANG</code></font></dt>
<dd> <p> This variable determines the locale category for any category not specifically selected with a variable starting with <font SIZE="-1"><code>LC_</code></font> or <font SIZE="-1"><code>LANG</code>. </font> </p>
 </dd>
<dt><font SIZE="-1"><code>LC_ALL</code></font></dt>
<dd> <p> This variable overrides the value of the <font SIZE="-1"><code>LANG</code></font> variable and any other <font SIZE="-1"><code>LC_</code></font> variable. </p>
 </dd>
<dt><font SIZE="-1"><code>LC_COLLATE</code></font></dt>
<dd> <p> This variable determines the locale category for character collation information. </p>
 </dd>
<dt><font SIZE="-1"><code>LC_CTYPE</code></font></dt>
<dd> <p> This variable determines the locale category for character handling functions. It determines the character classes for pattern matching (see <i>File Name Generation</i> below). </p>
 </dd>
<dt><font SIZE="-1"><code>LC_NUMERIC</code></font></dt>
<dd> <p> This variable determines the locale category for the decimal point character. </p>
 </dd>
<dt><font SIZE="-1"><code>LINES</code></font></dt>
<dd> <p> If this variable is set, the value is used to determine the column length for printing <code>select</code> lists. Select lists will print vertically until about two-thirds of <font SIZE="-1"><code>LINES</code></font> lines are filled. </p>
 </dd>
<dt><font SIZE="-1"><code>MAIL</code></font></dt>
<dd> <p> If this variable is set to the name of a mail file <i>and</i> the <font SIZE="-1"><code>MAILPATH</code></font> variable is not set, then the shell informs the user of arrival of mail in the specified file. </p>
 </dd>
<dt><font SIZE="-1"><code>MAILCHECK</code></font></dt>
<dd> <p> This variable specifies how often (in seconds) the shell will check for changes in the modification time of any of the files specified by the <font SIZE="-1"><code>MAILPATH</code></font> or <font SIZE="-1"><code>MAIL</code></font> variables. The default value is 600 seconds. When the time has elapsed the shell will check before issuing the next prompt. </p>
 </dd>
<dt><font SIZE="-1"><code>MAILPATH</code></font></dt>
<dd> <p> A colon ( <code>:</code> ) separated list of file names. If this variable is set, then the shell informs the user of any modifications to the specified files that have occurred within the last <font SIZE="-1"><code>MAILCHECK</code></font> seconds. Each file name can be followed by a <code>?</code> and a message that will be printed. The message will undergo parameter expansion, command substitution, and arithmetic substitution with the variable <code>$_</code> defined as the name of the file that has changed. The default message is <i>you have mail in $_.</i> </p>
 </dd>
<dt><font SIZE="-1"><code>PATH</code></font></dt>
<dd> <p> The search path for commands (see <i>Execution</i> below). The user may not change <font SIZE="-1"><code>PATH</code></font> if executing under <code>rksh</code> (except in <code>.profile).</code> </p>
 </dd>
<dt><font SIZE="-1"><code>PS1</code></font></dt>
<dd> <p> The value of this variable is expanded for parameter expansion, command substitution, and arithmetic substitution to define the primary prompt string which by default is ``<code>$</code>&#8216;&#8216;. The character <code>!</code> in the primary prompt string is replaced by the <i>command</i> number (see <i>Command Re-entry</i> below). Two successive occurrences of <code>!</code> will produce a single <code>!</code> when the prompt string is printed. </p>
 </dd>
<dt><font SIZE="-1"><code>PS2</code></font></dt>
<dd> <p> Secondary prompt string, by default ``<code>&gt; </code>&#8216;&#8216;. </p>
 </dd>
<dt><font SIZE="-1"><code>PS3</code></font></dt>
<dd> <p> Selection prompt string used within a <code>select</code> loop, by default ``<code>#? </code>&#8216;&#8216;. </p>
 </dd>
<dt><font SIZE="-1"><code>PS4</code></font></dt>
<dd> <p> The value of this variable is expanded for parameter evaluation, command substitution, and arithmetic substitution and precedes each line of an execution trace. By default, <font SIZE="-1"><code>PS4</code> </font> is ``<code>+ </code>&#8216;&#8216;. In addition when <font SIZE="-1"><code>PS4</code> </font> is unset, the execution trace prompt is also ``<code>+ </code>&#8216;&#8216;. </p>
 </dd>
<dt><font SIZE="-1"><code>SHELL</code></font></dt>
<dd> <p> The pathname of the <i>shell</i> is kept in the environment. At invocation, if the basename of this variable is <code>rsh</code>, <code>rksh</code>, or <code>krsh</code>, then the shell becomes restricted. If it is <code>pfsh</code> or <code>pfksh</code>, then the shell becomes a profile shell (see <i>pfexec</i>(1)). </p>
 </dd>
<dt><font SIZE="-1"><code>TIMEFORMAT</code></font></dt>
<dd> <p> The value of this parameter is used as a format string specifying how the timing information for pipelines prefixed with the <code>time</code> reserved word should be displayed. The <code>%</code> character introduces a format sequence that is expanded to a time value or other information. The format sequences and their meanings are as follows. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>%%</code></dt>
<dd> <p> A literal <code>%</code>. </p>
 </dd>
<dt><code>%[</code><i>p</i>][l]R </dt>
<dd> <p> The elapsed time in seconds. </p>
 </dd>
<dt><code>%[</code><i>p</i>][l]U </dt>
<dd> <p> The number of CPU seconds spent in user mode. </p>
 </dd>
<dt><code>%[</code><i>p</i>][l]S </dt>
<dd> <p> The number of CPU seconds spent in system mode. </p>
 </dd>
<dt><code>%P</code></dt>
<dd> <p> The CPU percentage, computed as (U + S) / R. </p>
 </dd></dl>
</dl>
<dd> <p> The brackets denote optional portions. The optional <i>p</i> is a digit specifying the <i>precision</i>, the number of fractional digits after a decimal point. A value of 0 causes no decimal point or fraction to be output. At most three places after the decimal point can be displayed; values of <i>p</i> greater than 3 are treated as 3. If <i>p</i> is not specified, the value 3 is used. </p>
 </dd>
<dd> <p> The optional <code>l</code> specifies a longer format, including hours if greater than zero, minutes, and seconds of the form <i>HH</i>h <i>MM</i>m <i>SS</i>.<i>FF</i>s. The value of <i>p</i> determines whether or not the fraction is included. </p>
 </dd>
<dd> <p> All other characters are output without change and a trailing newline is added. If unset, the default value, <code>$&#8216;\nreal\t%2lR\nuser\t%2lU\nsys %2lS&#8217;</code>, is used. If the value is null, no timing information is displayed. </p>
 </dd>
<dt><font SIZE="-1"><code>TMOUT</code></font></dt>
<dd> <p> If set to a value greater than zero, <font SIZE="-1"><code>TMOUT</code></font> will be the default timeout value for the <code>read</code> built-in command. The <code>select</code> compound command terminates after <font SIZE="-1"><code>TMOUT</code></font> seconds when input is from a terminal. Otherwise, the shell will terminate if a line is not entered within the prescribed number of seconds while reading from a terminal. (Note that the shell can be compiled with a maximum bound for this value which cannot be exceeded.) </p>
 </dd>
<dt><font SIZE="-1"><code>VISUAL</code></font></dt>
<dd> <p> If the value of this variable matches the pattern <i>*[Vv][Ii]*</i>, then the <code>vi</code> option (see Special Command <code>set</code> below) is turned on. If the value matches the pattern <i>*gmacs* ,</i> the <code>gmacs</code> option is turned on. If the value matches the pattern <i>*macs*</i>, then the <code>emacs</code> option will be turned on. The value of <font SIZE="-1"><code>VISUAL</code></font> overrides the value of <font SIZE="-1"><code>EDITOR.</code></font> </p>
 </dd></dl>
</dl>
<p> The shell gives default values to <font SIZE="-1"><code>PATH</code></font>, <font SIZE="-1"><code>PS1</code></font>, <font SIZE="-1"><code>PS2</code></font>, <font SIZE="-1"><code>PS3</code></font>, <font SIZE="-1"><code>PS4</code></font>, <font SIZE="-1"><code>MAILCHECK</code></font>, <font SIZE="-1"><code>FCEDIT</code></font>, <font SIZE="-1"><code>TMOUT</code></font> and <font SIZE="-1"><code>IFS</code></font>, while <font SIZE="-1"><code>HOME</code>, </font> <font SIZE="-1"><code>SHELL</code>, </font> <font SIZE="-1"><code>ENV</code>, </font> and <font SIZE="-1"><code>MAIL</code> </font> are not set at all by the shell (although <font SIZE="-1"><code>HOME</code> </font> <i>is</i> set by <i><a href="/docs/linux/man/1-login/">login</a></i>(1)). On some systems <font SIZE="-1"><code>MAIL</code> </font> and <font SIZE="-1"><code>SHELL</code> </font> are also set by <i><a href="/docs/linux/man/1-login/">login</a></i>(1).  </p>
<h3>Field Splitting.</h3>
<p> After parameter expansion and command substitution, the results of substitutions are scanned for the field separator characters (those found in <font SIZE="-1"><code>IFS</code></font> ) and split into distinct fields where such characters are found. Explicit null fields (<code>&quot;&quot;</code> or <code>&#180;&#180;</code>) are retained. Implicit null fields (those resulting from <i>parameters</i> that have no values or command substitutions with no output) are removed. </p>
<p> If the <code>braceexpand</code> (<code>-B</code>) option is set then each of the fields resulting from <font SIZE="-1"><code>IFS</code> </font> are checked to see if they contain one or more of the brace patterns <code>{*,*}</code>, <code>{</code><i>l1</i><code>..</code><i>l2</i><code>}</code> , <code>{</code><i>n1</i><code>..</code><i>n2</i><code>}</code> , <code>{</code><i>n1</i><code>..</code><i>n2</i><code>%</code> <i>fmt</i><code>}</code> , <code>{</code><i>n1</i><code>..</code><i>n2</i> <code>..</code><i>n3</i><code>}</code> , or <code>{</code><i>n1</i><code>..</code><i>n2</i> <code>..</code><i>n3</i><code>%</code><i>fmt</i><code>}</code> , where <code>*</code> represents any character, <i>l1</i>,<i>l2</i> are letters and <i>n1</i>,<i>n2</i>,<i>n3</i> are signed numbers and <i>fmt</i> is a format specified as used by <code>printf</code>. In each case, fields are created by prepending the characters before the <code>{</code> and appending the characters after the <code>}</code> to each of the strings generated by the characters between the <code>{</code> and <code>}</code>. The resulting fields are checked to see if they have any brace patterns. </p>
<p> In the first form, a field is created for each string between <code>{</code> and <code>,</code>, between <code>,</code> and <code>,</code>, and between <code>,</code> and <code>}</code>. The string represented by <code>*</code> can contain embedded matching <code>{</code> and <code>}</code> without quoting. Otherwise, each <code>{</code> and <code>}</code> with <code>*</code> must be quoted. </p>
<p> In the seconds form, <i>l1</i> and <i>l2</i> must both be either upper case or both be lower case characters in the C locale. In this case a field is created for each character from <i>l1</i> thru <i>l2</i>. </p>
<p> In the remaining forms, a field is created for each number starting at <i>n1</i> and continuing until it reaches <i>n2</i> incrementing <i>n1</i> by <i>n3</i>. The cases where <i>n3</i> is not specified behave as if <i>n3</i> where <code>1</code> if <i>n1</i><code>&lt;=</code><i>n2</i> and <code>-1</code> otherwise. If forms which specify <code>%</code><i>fmt</i> any format flags, widths and precisions can be specified and <i>fmt</i> can end in any of the specifiers <code>cdiouxX</code>. For example, <code>{a,z}{1..5..3%02d}{b..c}x</code> expands to the 8 fields, <code>a01bx</code>, <code>a01cx</code>, <code>a04bx</code>, <code>a04cx</code>, <code>z01bx</code>, <code>z01cx</code>, <code>z04bx</code> and <code>z4cx</code>.  </p>
<h3>File Name Generation.</h3>
<p> Following splitting, each field is scanned for the characters <code>*</code>, <code>?</code>, <code>(</code>, and unless the <code>-f</code> option has been set. If one of these characters appears, then the word is regarded as a <i>pattern</i>. Each file name component that contains any pattern character is replaced with a lexicographically sorted set of names that matches the pattern from that directory. If no file name is found that matches the pattern, then that component of the filename is left unchanged unless the pattern is prefixed with <code>&asymp;(N)</code> in which case it is removed as described below. If <font SIZE="-1"><code>FIGNORE</code> </font> is set, then each file name component that matches the pattern defined by the value of <font SIZE="-1"><code>FIGNORE</code> </font> is ignored when generating the matching filenames. The names <code>.</code> and <code>..</code> are also ignored. If <font SIZE="-1"><code>FIGNORE</code> </font> is not set, the character <code>.</code> at the start of each file name component will be ignored unless the first character of the pattern corresponding to this component is the character <code>.</code> itself. Note, that for other uses of pattern matching the <code>/</code> and <code>.</code> are not treated specially. </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>*</code></dt>
<dd> <p> Matches any string, including the null string. When used for filename expansion, if the <code>globstar</code> option is on, two adjacent <code>*</code>&#8216;s by itself will match all files and zero or more directories and subdirectories. If followed by a <code>/</code> then only directories and subdirectories will match. </p>
 </dd>
<dt><code>?</code></dt>
<dd> <p> Matches any single character. </p>
 </dd>
<dt>...<code>]</code></dt>
<dd> <p> Matches any one of the enclosed characters. A pair of characters separated by <code>-</code> matches any character lexically between the pair, inclusive. If the first character following the opening is a <code>!</code> or <code>^</code> then any character not enclosed is matched. A <code>-</code> can be included in the character set by putting it as the first or last character. <br />
 Within and <code>]</code>, character classes can be specified with the syntax <code>[:</code><i>class</i><code>:]</code> where class is one of the following classes defined in the ANSI-C standard: (Note that <code>word</code> is equivalent to <code>alnum</code> plus the character <code>_</code>.) <br />
 <code>alnum alpha blank cntrl digit graph lower print punct space upper word xdigit </code> <br />
 Within and <code>]</code>, an equivalence class can be specified with the syntax <code>[=</code><i>c</i><code>=]</code> which matches all characters with the same primary collation weight (as defined by the current locale) as the character <i>c</i>. Within and <code>]</code>, <code>[.</code><i>symbol</i><code>.]</code> matches the collating symbol <i>symbol</i>. </p>
 </dd></dl>
</dl>
<p> A <i>pattern-list</i> is a list of one or more patterns separated from each other with a <code>&amp;</code> or <code>|</code>. A <code>&amp;</code> signifies that all patterns must be matched whereas <code>|</code> requires that only one pattern be matched. Composite patterns can be formed with one or more of the following sub-patterns: </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>?(</code><i>pattern-list</i><code>)</code></dt>
<dd> <p> Optionally matches any one of the given patterns. </p>
 </dd>
<dt><code>*(</code><i>pattern-list</i><code>)</code></dt>
<dd> <p> Matches zero or more occurrences of the given patterns. </p>
 </dd>
<dt><code>+(</code><i>pattern-list</i><code>)</code></dt>
<dd> <p> Matches one or more occurrences of the given patterns. </p>
 </dd>
<dt><code>{</code><i>n</i><code>}</code>(<i>pattern-list</i><code>)</code></dt>
<dd> <p> Matches <i>n</i> occurrences of the given patterns. </p>
 </dd>
<dt><code>{</code><i>m</i><code>,</code><i>n</i><code>}</code>(<i>pattern-list</i><code>)</code></dt>
<dd> <p> Matches from <i>m</i> to <i>n</i> occurrences of the given patterns. If <i>m</i> is omitted, <code>0</code> will be used. If <i>n</i> is omitted at least <i>m</i> occurrences will be matched. </p>
 </dd>
<dt><code>@(</code><i>pattern-list</i><code>)</code></dt>
<dd> <p> Matches exactly one of the given patterns. <br />
 </p>
 </dd>
<dt><code>!(</code><i>pattern-list</i><code>)</code></dt>
<dd> <p> Matches anything except one of the given patterns. </p>
 </dd></dl>
</dl>
<p> By default, each pattern, or sub-pattern will match the longest string possible consistent with generating the longest overall match. If more than one match is possible, the one starting closest to the beginning of the string will be chosen. However, for each of the above compound patterns a <code>-</code> can be inserted in front of the <code>(</code> to cause the shortest match to the specified <i>pattern-list</i> to be used. </p>
<p> When <i>pattern-list</i> is contained within parentheses, the backslash character <code>\</code> is treated specially even when inside a character class. All ANSI-C character escapes are recognized and match the specified character. In addition the following escape sequences are recognized: </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>\d</code></dt>
<dd> <p> Matches any character in the <code>digit</code> class. </p>
 </dd>
<dt><code>\D</code></dt>
<dd> <p> Matches any character not in the <code>digit</code> class. </p>
 </dd>
<dt><code>\s</code></dt>
<dd> <p> Matches any character in the <code>space</code> class. </p>
 </dd>
<dt><code>\S</code></dt>
<dd> <p> Matches any character not in the <code>space</code> class. </p>
 </dd>
<dt><code>\w</code></dt>
<dd> <p> Matches any character in the <code>word</code> class. </p>
 </dd>
<dt><code>\W</code></dt>
<dd> <p> Matches any character not in the <code>word</code> class. </p>
 </dd></dl>
</dl>
<p> A pattern of the form <code>%(</code><i>pattern-pair</i>(s)<code>)</code> is a sub-pattern that can be used to match nested character expressions. Each <i>pattern-pair</i> is a two character sequence which cannot contain <code>&amp;</code> or <code>|</code>. The first <i>pattern-pair</i> specifies the starting and ending characters for the match. Each subsequent <i>pattern-pair</i> represents the beginning and ending characters of a nested group that will be skipped over when counting starting and ending character matches. The behavior is unspecified when the first character of a <i>pattern-pair</i> is alpha-numeric except for the following: </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>D</code></dt>
<dd> <p> Causes the ending character to terminate the search for this pattern without finding a match. </p>
 </dd>
<dt><code>E</code></dt>
<dd> <p> Causes the ending character to be interpreted as an escape character. </p>
 </dd>
<dt><code>L</code></dt>
<dd> <p> Causes the ending character to be interpreted as a quote character causing all characters to be ignored when looking for a match. </p>
 </dd>
<dt><code>Q</code></dt>
<dd> <p> Causes the ending character to be interpreted as a quote character causing all characters other than any escape character to be ignored when looking for a match. </p>
 </dd></dl>
</dl>
<p> Thus, <code>%({}Q&quot;E\)</code>, matches characters starting at <code>{</code> until the matching <code>}</code> is found not counting any <code>{</code> or <code>}</code> that is inside a double quoted string or preceded by the escape character <code>\</code>. Without the <code>{}</code> this pattern matches any C language string. </p>
<p> Each sub-pattern in a composite pattern is numbered, starting at 1, by the location of the <code>(</code> within the pattern. The sequence <code>\</code><i>n</i>, where <i>n</i> is a single digit and <code>\</code><i>n</i> comes after the <i>n</i>-th. sub-pattern, matches the same string as the sub-pattern itself. </p>
<p> Finally a pattern can contain sub-patterns of the form <code>&asymp;(</code><i>options</i><code>:</code><i>pattern-list</i><code>)</code>, where either <i>options</i> or <code>:</code><i>pattern-list</i> can be omitted. Unlike the other compound patterns, these sub-patterns are not counted in the numbered sub-patterns. <code>:</code><i>pattern-list</i> must be omitted for options <code>F</code>, <code>G</code>, <code>N ,</code> and <code>V</code> below. If <i>options</i> is present, it can consist of one or more of the following: </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>+</code></dt>
<dd> <p> Enable the following options. This is the default. </p>
 </dd>
<dt><code>-</code></dt>
<dd> <p> Disable the following options. </p>
 </dd>
<dt><code>E</code></dt>
<dd> <p> The remainder of the pattern uses extended regular expression syntax like the <i><a href="/docs/linux/man/1-egrep/">egrep</a></i>(1) command. </p>
 </dd>
<dt><code>F</code></dt>
<dd> <p> The remainder of the pattern uses <i><a href="/docs/linux/man/1-fgrep/">fgrep</a></i>(1) expression syntax. </p>
 </dd>
<dt><code>G</code></dt>
<dd> <p> The remainder of the pattern uses basic regular expression syntax like the <i><a href="/docs/linux/man/1-grep/">grep</a></i>(1) command. </p>
 </dd>
<dt><code>K</code></dt>
<dd> <p> The remainder of the pattern uses shell pattern syntax. This is the default. </p>
 </dd>
<dt><code>N</code></dt>
<dd> <p> This is ignored. However, when it is the first letter and is used with file name generation, and no matches occur, the file pattern expands to the empty string. </p>
 </dd>
<dt><code>X</code></dt>
<dd> <p> The remainder of the pattern uses augmented regular expression syntax like the <i>xgrep</i>(1) command. </p>
 </dd>
<dt><code>P</code></dt>
<dd> <p> The remainder of the pattern uses <i><a href="/docs/linux/man/1-perl/">perl</a></i>(1) regular expression syntax. Not all perl regular expression syntax is currently implemented. </p>
 </dd>
<dt><code>V</code></dt>
<dd> <p> The remainder of the pattern uses System V regular expression syntax. </p>
 </dd>
<dt><code>i</code></dt>
<dd> <p> Treat the match as case insensitive. </p>
 </dd>
<dt><code>g</code></dt>
<dd> <p> File the longest match (greedy). This is the default. </p>
 </dd>
<dt><code>l</code></dt>
<dd> <p> Left anchor the pattern. This is the default for <code>K</code> style patterns. </p>
 </dd>
<dt><code>r</code></dt>
<dd> <p> Right anchor the pattern. This is the default for <code>K</code> style patterns. </p>
 </dd></dl>
</dl>
<p> If both <i>options</i> and <code>:</code><i>pattern-list</i> are specified, then the options apply only to <i>pattern-list</i>. Otherwise, these options remain in effect until they are disabled by a subsequent <code>&asymp;(</code><i>...</i><code>)</code> or at the end of the sub-pattern containing <code>&asymp;(</code><i>...</i><code>)</code>.  </p>
<h3>Quoting.</h3>
<p> Each of the <i>metacharacters</i> listed earlier (see <i>Definitions</i> above) has a special meaning to the shell and causes termination of a word unless quoted. A character may be <i>quoted</i> (i.e., made to stand for itself) by preceding it with a <code>\</code>. The pair <code>\new-line</code> is removed. All characters enclosed between a pair of single quote marks (<code>&#180;&#180;</code>) that is not preceded by a <code>$</code> are quoted. A single quote cannot appear within the single quotes. A single quoted string preceded by an unquoted <code>$</code> is processed as an ANSI-C string except for the following: </p>
<dl>
<dt><code>\0</code></dt>
<dd> <p> Causes the remainder of the string to be ignored. </p>
 </dd>
<dt><code>\E</code></dt>
<dd> <p> Equivalent to the escape character (ascii <code>033</code>), </p>
 </dd>
<dt><code>\e</code></dt>
<dd> <p> Equivalent to the escape character (ascii <code>033</code>), </p>
 </dd>
<dt><code>\c</code><i>x</i></dt>
<dd> <p> Expands to the character control-<i>x</i>. </p>
 </dd>
<dt><code>\C[.</code><i>name</i><code>.]</code></dt>
<dd> <p> Expands to the collating element <i>name</i>. </p>
 </dd></dl>
<p> Inside double quote marks (<code>&quot;&quot;</code>), parameter and command substitution occur and <code>\</code> quotes the characters <code>\</code>, <code><font SIZE="+4">`</font></code>, <code>&quot;</code>, and <code>$</code>. A <code>$</code> in front of a double quoted string will be ignored in the &quot;C&quot; or &quot;POSIX&quot; locale, and may cause the string to be replaced by a locale specific string otherwise. The meaning of <code>$*</code> and <code>$@</code> is identical when not quoted or when used as a variable assignment value or as a file name. However, when used as a command argument, <code>&quot;$*&quot;</code> is equivalent to <code>&quot;$1</code><i>d</i><code>$2</code><i>d</i>...<code>&quot;</code>, where <i>d</i> is the first character of the <font SIZE="-1"><code>IFS</code> </font> variable, whereas <code>&quot;$@&quot;</code> is equivalent to <code>&quot;$1&quot;</code> <code>&quot;$2&quot;</code> .... Inside grave quote marks (<code><font SIZE="+4">`</font><font SIZE="+4">`</font></code>), <code>\</code> quotes the characters <code>\</code>, <code><font SIZE="+4">`</font></code>, and <code>$</code>. If the grave quotes occur within double quotes, then <code>\</code> also quotes the character <code>&quot;</code>. </p>
<p> The special meaning of reserved words or aliases can be removed by quoting any character of the reserved word. The recognition of function names or built-in command names listed below cannot be altered by quoting them.  </p>
<h3>Arithmetic Evaluation.</h3>
<p> The shell performs arithmetic evaluation for arithmetic substitution, to evaluate an arithmetic command, to evaluate an indexed array subscript, and to evaluate arguments to the built-in commands <code>shift</code> and <code>let</code>. Evaluations are performed using double precision floating point arithmetic or long double precision floating point for systems that provide this data type. Floating point constants follow the ANSI-C programming language floating point conventions. The floating point constants <code>Nan</code> and <code>Inf</code> can be use to represent &quot;not a number&quot; and infinity respectively. Integer constants follow the ANSI-C programming language integer constant conventions although only single byte character constants are recognized and character casts are not recognized. In addition constants can be of the form <i>base</i><code>#</code>]<i>n</i> where <i>base</i> is a decimal number between two and sixty-four representing the arithmetic base and <i>n</i> is a number in that base. The digits above 9 are represented by the lower case letters, the upper case letters, <code>@</code>, and <code>_</code> respectively. For bases less than or equal to 36, upper and lower case characters can be used interchangeably. </p>
<p> An arithmetic expression uses the same syntax, precedence, and associativity of expression as the C language. All the C language operators that apply to floating point quantities can be used. In addition, the operator <code>**</code> can be used for exponentiation. It has higher precedence than multiplication and is left associative. In addition, when the value of an arithmetic variable or sub-expression can be represented as a long integer, all C language integer arithmetic operations can be performed. Variables can be referenced by name within an arithmetic expression without using the parameter expansion syntax. When a variable is referenced, its value is evaluated as an arithmetic expression. </p>
<p> Any of the following math library functions that are in the C math library can be used within an arithmetic expression: </p>
<p> <code>abs acos acosh asin asinh atan atan2 atanh cbrt ceil copysign cos cosh erf erfc exp exp2 expm1 fabs fpclassify fdim finite floor fma fmax fmin fmod hypot ilogb int isfinite sinf isnan isnormal issubnormal issubordered iszero j0 j1 jn lgamma log log10 log2 logb nearbyint nextafter nexttoward pow remainder rint round scanb signbit sin sinh sqrt tan tanh tgamma trunc y0 y1 yn </code> In addition, arithmetic functions can be define as shell functions with a variant of the <code>function</code> <i>name</i> syntax, </p>
<dl>
<dd> <p> <code>function .sh.math.</code><i>name ident</i> ... <code>{</code> <i>list</i> <code>;}</code> where <i>name</i> is the function name used in the arithmetic expression and each identifier, <i>ident</i> is a name reference to the long double precision floating point argument. The value of <code>.sh.value</code> when the function returns is the value of this function. User defined functions can take up to 3 arguments and override C math library functions. </p>
 </dd></dl>
<p> An internal representation of a <i>variable</i> as a double precision floating point can be specified with the <code>-E</code> <i>n</i>], <code>-F</code> <i>n</i>], or <code>-X</code> <i>n</i>] option of the <code>typeset</code> special built-in command. The <code>-E</code> option causes the expansion of the value to be represented using scientific notation when it is expanded. The optional option argument <i>n</i> defines the number of significant figures. The <code>-F</code> option causes the expansion to be represented as a floating decimal number when it is expanded. The <code>-X</code> option cause the expansion to be represented using the <code>%a</code> format defined by ISO C-99. The optional option argument <i>n</i> defines the number of places after the decimal (or radix) point in this case. </p>
<p> An internal integer representation of a <i>variable</i> can be specified with the <code>-i</code> <i>n</i>] option of the <code>typeset</code> special built-in command. The optional option argument <i>n</i> specifies an arithmetic base to be used when expanding the variable. If you do not specify an arithmetic base, base 10 will be used. </p>
<p> Arithmetic evaluation is performed on the value of each assignment to a variable with the <code>-E</code>, <code>-F</code>, <code>-X</code>, or <code>-i</code> attribute. Assigning a floating point number to a variable whose type is an integer causes the fractional part to be truncated. </p>
<h3>Prompting.</h3>
<p> When used interactively, the shell prompts with the value of <font SIZE="-1"><code>PS1</code> </font> after expanding it for parameter expansion, command substitution, and arithmetic substitution, before reading a command. In addition, each single <code>!</code> in the prompt is replaced by the command number. A <code>!!</code> is required to place <code>!</code> in the prompt. If at any time a new-line is typed and further input is needed to complete a command, then the secondary prompt (i.e., the value of <font SIZE="-1"><code>PS2</code></font>) is issued.  </p>
<h3>Conditional Expressions.</h3>
<p> A <i>conditional expression</i> is used with the <code>[[</code> compound command to test attributes of files and to compare strings. Field splitting and file name generation are not performed on the words between <code>[[</code> and <code>]]</code>. Each expression can be constructed from one or more of the following unary or binary expressions: </p>
<dl>
<dt><i>string</i></dt>
<dd> <p> True, if <i>string</i> is not null. </p>
 </dd>
<dt><code>-a</code><i>file</i></dt>
<dd> <p> Same as <code>-e</code> below. This is obsolete. </p>
 </dd>
<dt><code>-b</code><i>file</i></dt>
<dd> <p> True, if <i>file</i> exists and is a block special file. </p>
 </dd>
<dt><code>-c</code><i>file</i></dt>
<dd> <p> True, if <i>file</i> exists and is a character special file. </p>
 </dd>
<dt><code>-d</code><i>file</i></dt>
<dd> <p> True, if <i>file</i> exists and is a directory. </p>
 </dd>
<dt><code>-e</code><i>file</i></dt>
<dd> <p> True, if <i>file</i> exists. </p>
 </dd>
<dt><code>-f</code><i>file</i></dt>
<dd> <p> True, if <i>file</i> exists and is an ordinary file. </p>
 </dd>
<dt><code>-g</code><i>file</i></dt>
<dd> <p> True, if <i>file</i> exists and it has its setgid bit set. </p>
 </dd>
<dt><code>-k</code><i>file</i></dt>
<dd> <p> True, if <i>file</i> exists and it has its sticky bit set. </p>
 </dd>
<dt><code>-n</code><i>string</i></dt>
<dd> <p> True, if length of <i>string</i> is non-zero. </p>
 </dd>
<dt><code>-o</code><code>?</code><i>option</i></dt>
<dd> <p> True, if option named <i>option</i> is a valid option name. </p>
 </dd>
<dt><code>-o</code><i>option</i></dt>
<dd> <p> True, if option named <i>option</i> is on. </p>
 </dd>
<dt><code>-p</code><i>file</i></dt>
<dd> <p> True, if <i>file</i> exists and is a fifo special file or a pipe. </p>
 </dd>
<dt><code>-r</code><i>file</i></dt>
<dd> <p> True, if <i>file</i> exists and is readable by current process. </p>
 </dd>
<dt><code>-s</code><i>file</i></dt>
<dd> <p> True, if <i>file</i> exists and has size greater than zero. </p>
 </dd>
<dt><code>-t</code><i>fildes</i></dt>
<dd> <p> True, if file descriptor number <i>fildes</i> is open and associated with a terminal device. </p>
 </dd>
<dt><code>-u</code><i>file</i></dt>
<dd> <p> True, if <i>file</i> exists and it has its setuid bit set. </p>
 </dd>
<dt><code>-v</code><i>name</i></dt>
<dd> <p> True, if variable <i>name</i> is a valid variable name and is set. </p>
 </dd>
<dt><code>-w</code><i>file</i></dt>
<dd> <p> True, if <i>file</i> exists and is writable by current process. </p>
 </dd>
<dt><code>-x</code><i>file</i></dt>
<dd> <p> True, if <i>file</i> exists and is executable by current process. If <i>file</i> exists and is a directory, then true if the current process has permission to search in the directory. </p>
 </dd>
<dt><code>-z</code><i>string</i></dt>
<dd> <p> True, if length of <i>string</i> is zero. </p>
 </dd>
<dt><code>-L</code><i>file</i></dt>
<dd> <p> True, if <i>file</i> exists and is a symbolic link. </p>
 </dd>
<dt><code>-h</code><i>file</i></dt>
<dd> <p> True, if <i>file</i> exists and is a symbolic link. </p>
 </dd>
<dt><code>-N</code><i>file</i></dt>
<dd> <p> True, if <i>file</i> exists and the modification time is greater than the last access time. </p>
 </dd>
<dt><code>-O</code><i>file</i></dt>
<dd> <p> True, if <i>file</i> exists and is owned by the effective user id of this process. </p>
 </dd>
<dt><code>-G</code><i>file</i></dt>
<dd> <p> True, if <i>file</i> exists and its group matches the effective group id of this process. </p>
 </dd>
<dt><code>-R</code><i>name</i></dt>
<dd> <p> True if variable <i>name</i> is a name reference. </p>
 </dd>
<dt><code>-S</code><i>file</i></dt>
<dd> <p> True, if <i>file</i> exists and is a socket. </p>
 </dd>
<dt><i>file1</i><code>-nt</code><i>file2</i></dt>
<dd> <p> True, if <i>file1</i> exists and <i>file2</i> does not, or <i>file1</i> is newer than <i>file2</i>. </p>
 </dd>
<dt><i>file1</i><code>-ot</code><i>file2</i></dt>
<dd> <p> True, if <i>file2</i> exists and <i>file1</i> does not, or <i>file1</i> is older than <i>file2</i>. </p>
 </dd>
<dt><i>file1</i><code>-ef</code><i>file2</i></dt>
<dd> <p> True, if <i>file1</i> and <i>file2</i> exist and refer to the same file. </p>
 </dd>
<dt><i>string</i><code>==</code><i>pattern</i></dt>
<dd> <p> True, if <i>string</i> matches <i>pattern</i>. Any part of <i>pattern</i> can be quoted to cause it to be matched as a string. With a successful match to a pattern, the <code>.sh.match</code> array variable will contain the match and sub-pattern matches. </p>
 </dd>
<dt><i>string</i><code>=</code><i>pattern</i></dt>
<dd> <p> Same as <code>==</code> above, but is obsolete. </p>
 </dd>
<dt><i>string</i><code>!=</code><i>pattern</i></dt>
<dd> <p> True, if <i>string</i> does not match <i>pattern</i>. When the <i>string</i> matches the <i>pattern</i> the <code>.sh.match</code> array variable will contain the match and sub-pattern matches. </p>
 </dd>
<dt><i>string</i><code>=&asymp;</code><i>ere</i></dt>
<dd> <p> True if <i>string</i> matches the pattern <code>&asymp;(E)</code><i>ere</i> where <i>ere</i> is an extended regular expression. </p>
 </dd>
<dt><i>string1</i><code>&lt;</code><i>string2</i></dt>
<dd> <p> True, if <i>string1</i> comes before <i>string2</i> based on ASCII value of their characters. </p>
 </dd>
<dt><i>string1</i><code>&gt;</code><i>string2</i></dt>
<dd> <p> True, if <i>string1</i> comes after <i>string2</i> based on ASCII value of their characters. </p>
 </dd></dl>
<p> The following obsolete arithmetic comparisons are also permitted: </p>
<dl>
<dt><i>exp1</i><code>-eq</code><i>exp2</i></dt>
<dd> <p> True, if <i>exp1</i> is equal to <i>exp2</i>. </p>
 </dd>
<dt><i>exp1</i><code>-ne</code><i>exp2</i></dt>
<dd> <p> True, if <i>exp1</i> is not equal to <i>exp2</i>. </p>
 </dd>
<dt><i>exp1</i><code>-lt</code><i>exp2</i></dt>
<dd> <p> True, if <i>exp1</i> is less than <i>exp2</i>. </p>
 </dd>
<dt><i>exp1</i><code>-gt</code><i>exp2</i></dt>
<dd> <p> True, if <i>exp1</i> is greater than <i>exp2</i>. </p>
 </dd>
<dt><i>exp1</i><code>-le</code><i>exp2</i></dt>
<dd> <p> True, if <i>exp1</i> is less than or equal to <i>exp2</i>. </p>
 </dd>
<dt><i>exp1</i><code>-ge</code><i>exp2</i></dt>
<dd> <p> True, if <i>exp1</i> is greater than or equal to <i>exp2</i>. </p>
 </dd></dl>
<p> In each of the above expressions, if <i>file</i> is of the form <code>/dev/fd/</code><i>n</i>, where <i>n</i> is an integer, then the test is applied to the open file whose descriptor number is <i>n</i>. </p>
<p> A compound expression can be constructed from these primitives by using any of the following, listed in decreasing order of precedence. </p>
<dl>
<dt><code>(</code><i>expression</i><code>)</code></dt>
<dd> <p> True, if <i>expression</i> is true. Used to group expressions. </p>
 </dd>
<dt><code>!</code><i>expression</i></dt>
<dd> <p> True if <i>expression</i> is false. </p>
 </dd>
<dt><i>expression1</i><code>&amp;&amp;</code><i>expression2</i></dt>
<dd> <p> True, if <i>expression1</i> and <i>expression2</i> are both true. </p>
 </dd>
<dt><i>expression1</i><code>||</code><i>expression2</i></dt>
<dd> <p> True, if either <i>expression1</i> or <i>expression2</i> is true. </p>
 </dd></dl>
<h3>Input/Output.</h3>
<p> Before a command is executed, its input and output may be redirected using a special notation interpreted by the shell. The following may appear anywhere in a simple-command or may precede or follow a <i>command</i> and are <i>not</i> passed on to the invoked command. Command substitution, parameter expansion, and arithmetic substitution occur before <i>word</i> or <i>digit</i> is used except as noted below. File name generation occurs only if the shell is interactive and the pattern matches a single file. Field splitting is not performed. </p>
<p> In each of the following redirections, if <i>file</i> is of the form <code>/dev/sctp/</code><i>host</i><code>/</code><i>port</i>, <code>/dev/tcp/</code><i>host</i><code>/</code><i>port</i>, or <code>/dev/udp/</code><i>host</i><code>/</code><i>port</i>, where <i>host</i> is a hostname or host address, and <i>port</i> is a service given by name or an integer port number, then the redirection attempts to make a <code>tcp</code>, <code>sctp</code> or <code>udp</code> connection to the corresponding socket. </p>
<p> No intervening space is allowed between the characters of redirection operators. </p>
<dl>
<dt><code>&lt;</code><i>word</i></dt>
<dd> <p> Use file <i>word</i> as standard input (file descriptor 0). </p>
 </dd>
<dt><code>&gt;</code><i>word</i></dt>
<dd> <p> Use file <i>word</i> as standard output (file descriptor 1). If the file does not exist then it is created. If the file exists, and the <code>noclobber</code> option is on, this causes an error; otherwise, it is truncated to zero length. </p>
 </dd>
<dt><code>&gt;|</code><i>word</i></dt>
<dd> <p> Same as <code>&gt;</code>, except that it overrides the <code>noclobber</code> option. </p>
 </dd>
<dt><code>&gt;;</code><i>word</i></dt>
<dd> <p> Write output to a temporary file. If the command completes successfully rename it to <i>word</i>, otherwise, delete the temporary file. <code>&gt;;</code><i>word</i> cannot be used with the <i>exec</i>(2). built-in. </p>
 </dd>
<dt><code>&gt;&gt;</code><i>word</i></dt>
<dd> <p> Use file <i>word</i> as standard output. If the file exists, then output is appended to it (by first seeking to the end-of-file); otherwise, the file is created. </p>
 </dd>
<dt><code>&lt;&gt;</code><i>word</i></dt>
<dd> <p> Open file <i>word</i> for reading and writing as standard output. </p>
 </dd>
<dt><code>&lt;&gt;;</code><i>word</i></dt>
<dd> <p> The same as <code>&lt;&gt;</code><i>word</i> except that if the command completes successfully, <i>word</i> is truncated to the offset at command completion. <code>&lt;&gt;;</code><i>word</i> cannot be used with the <i>exec</i>(2). built-in. </p>
 </dd>
<dt><code>&lt;&lt;</code><code>-</code>]<i>word</i></dt>
<dd> <p> The shell input is read up to a line that is the same as <i>word</i> after any quoting has been removed, or to an end-of-file. No parameter substitution, command substitution, arithmetic substitution or file name generation is performed on <i>word</i>. The resulting document, called a <i>here-document</i>, becomes the standard input. If any character of <i>word</i> is quoted, then no interpretation is placed upon the characters of the document; otherwise, parameter expansion, command substitution, and arithmetic substitution occur, <code>\new-line</code> is ignored, and <code>\</code> must be used to quote the characters <code>\</code>, <code>$</code>, <code><font SIZE="+4">`</font></code>. If <code>-</code> is appended to <code>&lt;&lt;</code>, then all leading tabs are stripped from <i>word</i> and from the document. If <code>#</code> is appended to <code>&lt;&lt;</code>, then leading spaces and tabs will be stripped off the first line of the document and up to an equivalent indentation will be stripped from the remaining lines and from <i>word</i>. A tab stop is assumed to occur at every 8 columns for the purposes of determining the indentation. </p>
 </dd>
<dt><code>&lt;&lt;&lt;</code><i>word</i></dt>
<dd> <p> A short form of here document in which <i>word</i> becomes the contents of the here-document after any parameter expansion, command substitution, and arithmetic substitution occur. </p>
 </dd>
<dt><code>&lt;&amp;</code><i>digit</i></dt>
<dd> <p> The standard input is duplicated from file descriptor <i>digit</i> (see <i><a href="/docs/linux/man/2-dup/">dup</a></i>(2)). Similarly for the standard output using <code>&gt;&amp;</code><i>digit</i>. </p>
 </dd>
<dt><code>&lt;&amp;</code><i>digit</i><code>-</code></dt>
<dd> <p> The file descriptor given by <i>digit</i> is moved to standard input. Similarly for the standard output using <code>&gt;&amp;</code><i>digit</i><code>-</code>. </p>
 </dd>
<dt><code>&lt;&amp;-</code></dt>
<dd> <p> The standard input is closed. Similarly for the standard output using <code>&gt;&amp;-</code>. </p>
 </dd>
<dt><code>&lt;&amp;p</code></dt>
<dd> <p> The input from the co-process is moved to standard input. </p>
 </dd>
<dt><code>&gt;&amp;p</code></dt>
<dd> <p> The output to the co-process is moved to standard output. </p>
 </dd>
<dt><code>&lt;#</code><i></i><code>((</code><i>expr</i><code>))</code></dt>
<dd> <p> Evaluate arithmetic expression <i>expr</i> and position file descriptor 0 to the resulting value bytes from the start of the file. The variables <code>CUR</code> and <code>EOF</code> evaluate to the current offset and end-of-file offset respectively when evaluating <i>expr.</i> </p>
 </dd>
<dt><code>&gt;#</code><i></i><code>((</code><i>offset</i><code>))</code></dt>
<dd> <p> The same as <code>&lt;#</code> except applies to file descriptor 1. </p>
 </dd>
<dt><code>&lt;#</code><i>pattern</i></dt>
<dd> <p> Seeks forward to the beginning of the next line containing <i>pattern</i>. </p>
 </dd>
<dt><code>&lt;##</code><i>pattern</i></dt>
<dd> <p> The same as <code>&lt;#</code> except that the portion of the file that is skipped is copied to standard output. </p>
 </dd></dl>
<p> If one of the above is preceded by a digit, with no intervening space, then the file descriptor number referred to is that specified by the digit (instead of the default 0 or 1). If one of the above, other than <code>&gt;&amp;-</code> and the <code>&gt;#</code> and <code>&lt;#</code> forms, is preceded by <code>{</code><i>varname</i><code>}</code> with no intervening space, then a file descriptor number &gt; 10 will be selected by the shell and stored in the variable <i>varname</i>. If <code>&gt;&amp;-</code> or the any of the <code>&gt;#</code> and <code>&lt;#</code> forms is preceded by <code>{</code><i>varname</i><code>}</code> the value of <i>varname</i> defines the file descriptor to close or position. For example: </p>
<dl>
<dd> <p> <code>... 2&gt;&amp;1</code> </p>
 </dd></dl>
<p> means file descriptor 2 is to be opened for writing as a duplicate of file descriptor 1 and </p>
<dl>
<dd> <p> <code>exec {n}&lt;file</code> </p>
 </dd></dl>
<p> means open file named <code>file</code> for reading and store the file descriptor number in variable <code>n</code>. </p>
<p> The order in which redirections are specified is significant. The shell evaluates each redirection in terms of the (<i>file descriptor</i>, <i>file</i>) association at the time of evaluation. For example: </p>
<dl>
<dd> <p> <code>... 1&gt;</code><i>fname</i> 2&gt;&amp;1 </p>
 </dd></dl>
<p> first associates file descriptor 1 with file <i>fname</i>. It then associates file descriptor 2 with the file associated with file descriptor 1 (i.e. <i>fname</i>). If the order of redirections were reversed, file descriptor 2 would be associated with the terminal (assuming file descriptor 1 had been) and then file descriptor 1 would be associated with file <i>fname</i>. </p>
<p> If a command is followed by <code>&amp;</code> and job control is not active, then the default standard input for the command is the empty file <code>/dev/null</code>. Otherwise, the environment for the execution of a command contains the file descriptors of the invoking shell as modified by input/output specifications.  </p>
<h3>Environment.</h3>
<p> The <i>environment</i> (see <i><a href="/docs/linux/man/7-environ/">environ</a></i>(7)) is a list of name-value pairs that is passed to an executed program in the same way as a normal argument list. The names must be <i>identifiers</i> and the values are character strings. The shell interacts with the environment in several ways. On invocation, the shell scans the environment and creates a variable for each name found, giving it the corresponding value and attributes and marking it <i>export</i>. Executed commands inherit the environment. If the user modifies the values of these variables or creates new ones, using the <code>export</code> or <code>typeset -x</code> commands, they become part of the environment. The environment seen by any executed command is thus composed of any name-value pairs originally inherited by the shell, whose values may be modified by the current shell, plus any additions which must be noted in <code>export</code> or <code>typeset -x</code> commands. </p>
<p> The environment for any <i>simple-command</i> or function may be augmented by prefixing it with one or more variable assignments. A variable assignment argument is a word of the form <i>identifier=value</i>. Thus: </p>
<dl>
<dd> <p> <font SIZE="-1"><code>TERM</code></font><code>=450 cmd args</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>and<br />
 <br />
 <code>(export </code><font SIZE="-1"><code>TERM</code></font><code>; </code><font SIZE="-1"><code>TERM</code></font><code>=450; cmd args)</code> </p>
 </dd></dl>
<p> are equivalent (as far as the above execution of <i>cmd</i> is concerned except for special built-in commands listed below - those that are preceded with a dagger). </p>
<p> If the obsolete <code>-k</code> option is set, <i>all</i> variable assignment arguments are placed in the environment, even if they occur after the command name. The following first prints <code>a=b c</code> and then <code>c</code>: </p>
<dl>
<dd> <pre><code>
 echo a=b c
set -k
echo a=b c
 </code></pre>
 </dd></dl>
<p> This feature is intended for use with scripts written for early versions of the shell and its use in new scripts is strongly discouraged. It is likely to disappear someday.  </p>
<h3>Functions.</h3>
<p> For historical reasons, there are two ways to define functions, the <i>name</i><code>()</code> syntax and the <code>function</code> <i>name</i> syntax, described in the <i>Commands</i> section above. Shell functions are read in and stored internally. Alias names are resolved when the function is read. Functions are executed like commands with the arguments passed as positional parameters. (See <i>Execution</i> below.) </p>
<p> Functions defined by the <code>function</code> <i>name</i> syntax and called by name execute in the same process as the caller and share all files and present working directory with the caller. Traps caught by the caller are reset to their default action inside the function. A trap condition that is not caught or ignored by the function causes the function to terminate and the condition to be passed on to the caller. A trap on <font SIZE="-1"><code>EXIT</code> </font> set inside a function is executed in the environment of the caller after the function completes. Ordinarily, variables are shared between the calling program and the function. However, the <code>typeset</code> special built-in command used within a function defines local variables whose scope includes the current function. They can be passed to functions that they call in the variable assignment list that precedes the call or as arguments passed as name references. Errors within functions return control to the caller. </p>
<p> Functions defined with the <i>name</i><code>()</code> syntax and functions defined with the <code>function</code> <i>name</i> syntax that are invoked with the <font SIZE="+2"><code>.</code></font> special built-in are executed in the caller&#8217;s environment and share all variables and traps with the caller. Errors within these function executions cause the script that contains them to abort. </p>
<p> The special built-in command <code>return</code> is used to return from function calls. </p>
<p> Function names can be listed with the <code>-f</code> or <code>+f</code> option of the <code>typeset</code> special built-in command. The text of functions, when available, will also be listed with <code>-f</code>. Functions can be undefined with the <code>-f</code> option of the <code>unset</code> special built-in command. </p>
<p> Ordinarily, functions are unset when the shell executes a shell script. Functions that need to be defined across separate invocations of the shell should be placed in a directory and the <font SIZE="-1"><code>FPATH</code></font> variable should contain the name of this directory. They may also be specified in the <font SIZE="-1"><code>ENV</code></font> file.  </p>
<h3>Discipline Functions.</h3>
<p> Each variable can have zero or more discipline functions associated with it. The shell initially understands the discipline names <code>get</code>, <code>set</code>, <code>append</code>, and <code>unset</code> but can be added when defining new types. On most systems others can be added at run time via the C programming interface extension provided by the <code>builtin</code> built-in utility. If the <code>get</code> discipline is defined for a variable, it is invoked whenever the given variable is referenced. If the variable <code>.sh.value</code> is assigned a value inside the discipline function, the referenced variable will evaluate to this value instead. If the <code>set</code> discipline is defined for a variable, it is invoked whenever the given variable is assigned a value. If the <code>append</code> discipline is defined for a variable, it is invoked whenever a value is appended to the given variable. The variable <code>.sh.value</code> is given the value of the variable before invoking the discipline, and the variable will be assigned the value of <code>.sh.value</code> after the discipline completes. If <code>.sh.value</code> is unset inside the discipline, then that value is unchanged. If the <code>unset</code> discipline is defined for a variable, it is invoked whenever the given variable is unset. The variable will not be unset unless it is unset explicitly from within this discipline function. </p>
<p> The variable <code>.sh.name</code> contains the name of the variable for which the discipline function is called, <code>.sh.subscript</code> is the subscript of the variable, and <code>.sh.value</code> will contain the value being assigned inside the <code>set</code> discipline function. The variable <code>_</code> is a reference to the variable including the subscript if any. For the <code>set</code> discipline, changing <code>.sh.value</code> will change the value that gets assigned. Finally, the expansion <code>${</code><i>var</i><code>.</code><i>name</i><code>}</code>, when <i>name</i> is the name of a discipline, and there is no variable of this name, is equivalent to the command substitution <code>${ </code><i>var</i><code>.</code><i>name</i><code>;}</code>. </p>
<h3>Name Spaces.</h3>
<p> Commands and functions that are executed as part of the <i>list</i> of a <code>namespace</code> command that modify variables or create new ones, create a new variable whose name is the name of the name space as given by <i>identifier</i> preceded by <font SIZE="+2"><code>.</code></font>. When a variable whose name is <i>name</i> is referenced, it is first searched for using <font SIZE="+2"><code>.</code></font><i>identifier</i><font SIZE="+2"><code>.</code></font><i>name</i>. Similarly, a function defined by a command in the <code>namespace</code> <i>list</i> is created using the name space name preceded by a <font SIZE="+2"><code>.</code></font>. </p>
<p> When the <i>list</i> of a <code>namespace</code> command contains a <code>namespace</code> command, the names of variables and functions that are created consist of the variable or function name preceded by the list of <i>identifier</i>s each preceded by <font SIZE="+2"><code>.</code></font>. </p>
<p> Outside of a name space, a variable or function created inside a name space can be referenced by preceding it with the name space name. </p>
<p> By default, variables staring with <font SIZE="+2"><code>.</code></font><code>sh</code> are in the <code>sh</code> name space. </p>
<h3>Type Variables.</h3>
<p> Typed variables provide a way to create data structure and objects. A type can be defined either by a shared library, by the <code>enum</code> built-in command described below, or by using the new <code>-T</code> option of the <code>typeset</code> built-in command. With the <code>-T</code> option of <code>typeset</code>, the type name, specified as an option argument to <code>-T</code>, is set with a compound variable assignment that defines the type. Function definitions can appear inside the compound variable assignment and these become discipline functions for this type and can be invoked or redefined by each instance of the type. The function name <code>create</code> is treated specially. It is invoked for each instance of the type that is created but is not inherited and cannot be redefined for each instance. </p>
<p> When a type is defined a special built-in command of that name is added. These built-ins are declaration commands and follow the same expansion rules as all the special built-in commands defined below that are preceded by --. These commands can subsequently be used inside further type definitions. The man page for these commands can be generated by using the <code>--man</code> option or any of the other <code>--</code> options described with <code>getopts</code>. The <code>-r</code>, <code>-a</code>, <code>-A</code>, <code>-h</code>, and <code>-S</code> options of <code>typeset</code> are permitted with each of these new built-ins. </p>
<p> An instance of a type is created by invoking the type name followed by one or more instance names. Each instance of the type is initialized with a copy of the sub-variables except for sub-variables that are defined with the <code>-S</code> option. Variables defined with the <code>-S</code> are shared by all instances of the type. Each instance can change the value of any sub-variable and can also define new discipline functions of the same names as those defined by the type definition as well as any standard discipline names. No additional sub-variables can be defined for any instance. </p>
<p> When defining a type, if the value of a sub-variable is not set and the <code>-r</code> attribute is specified, it causes the sub-variable to be a required sub-variable. Whenever an instance of a type is created, all required sub-variables must be specified. These sub-variables become readonly in each instance. </p>
<p> When <code>unset</code> is invoked on a sub-variable within a type, and the <code>-r</code> attribute has not been specified for this field, the value is reset to the default value associative with the type. Invoking <code>unset</code> on a type instance not contained within another type deletes all sub-variables and the variable itself. </p>
<p> A type definition can be derived from another type definition by defining the first sub-variable name as <code>_</code> and defining its type as the base type. Any remaining definitions will be additions and modifications that apply to the new type. If the new type name is the same is that of the base type, the type will be replaced and the original type will no longer be accessible. </p>
<p> The <code>typeset</code> command with the <code>-T</code> and no option argument or operands will write all the type definitions to standard output in a form that that can be read in to create all they types.  </p>
<h3>Jobs.</h3>
<p> If the <code>monitor</code> option of the <code>set</code> command is turned on, an interactive shell associates a <i>job</i> with each pipeline. It keeps a table of current jobs, printed by the <code>jobs</code> command, and assigns them small integer numbers. When a job is started asynchronously with <code>&amp;</code>, the shell prints a line which looks like: </p>
<p> <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>[1] 1234<br />
 </p>
<p> indicating that the job which was started asynchronously was job number 1 and had one (top-level) process, whose process id was 1234. </p>
<p> This paragraph and the next require features that are not in all versions of UNIX and may not apply. If you are running a job and wish to do something else you may hit the key <code>^Z</code> (control-Z) which sends a STOP signal to the current job. The shell will then normally indicate that the job has been `Stopped&#8217;, and print another prompt. You can then manipulate the state of this job, putting it in the background with the <code>bg</code> command, or run some other commands and then eventually bring the job back into the foreground with the foreground command <code>fg</code>. A <code>^Z</code> takes effect immediately and is like an interrupt in that pending output and unread input are discarded when it is typed. </p>
<p> A job being run in the background will stop if it tries to read from the terminal. Background jobs are normally allowed to produce output, but this can be disabled by giving the command <code>stty tostop</code>. If you set this tty option, then background jobs will stop when they try to produce output like they do when they try to read input. </p>
<p> A job pool is a collection of jobs started with <i>list</i> <code>&amp;</code> associated with a name. </p>
<p> There are several ways to refer to jobs in the shell. A job can be referred to by the process id of any process of the job or by one of the following: </p>
<dl>
<dt><code>%</code><i>number</i></dt>
<dd> <p> The job with the given number. </p>
 </dd>
<dt><i>pool</i></dt>
<dd> <p> All the jobs in the job pool named by <i>pool</i>. </p>
 </dd>
<dt><i>pool</i><code>.</code><i>number</i></dt>
<dd> <p> The job number <i>number</i> in the job pool named by <i>pool</i>. </p>
 </dd>
<dt><code>%</code><i>string</i></dt>
<dd> <p> Any job whose command line begins with <i>string</i>. </p>
 </dd>
<dt><code>%?</code><i>string</i></dt>
<dd> <p> Any job whose command line contains <i>string</i>. </p>
 </dd>
<dt><code>%%</code></dt>
<dd> <p> Current job. </p>
 </dd>
<dt><code>%+</code></dt>
<dd> <p> Equivalent to <code>%%</code>. </p>
 </dd>
<dt><code>%-</code></dt>
<dd> <p> Previous job. In addition, unless noted otherwise, wherever a job can be specified, the name of a background job pool can be used to represent all the jobs in that pool. </p>
 </dd></dl>
<p> The shell learns immediately whenever a process changes state. It normally informs you whenever a job becomes blocked so that no further progress is possible, but only just before it prints a prompt. This is done so that it does not otherwise disturb your work. The <code>notify</code> option of the <code>set</code> command causes the shell to print these job change messages as soon as they occur. </p>
<p> When the <code>monitor</code> option is on, each background job that completes triggers any trap set for <code>CHLD</code>. </p>
<p> When you try to leave the shell while jobs are running or stopped, you will be warned that `You have stopped(running) jobs.&#8216; You may use the <code>jobs</code> command to see what they are. If you immediately try to exit again, the shell will not warn you a second time, and the stopped jobs will be terminated. When a login shell receives a HUP signal, it sends a HUP signal to each job that has not been disowned with the <code>disown</code> built-in command described below.  </p>
<h3>Signals.</h3>
<p> The <font SIZE="-1">INT</font> and <font SIZE="-1">QUIT</font> signals for an invoked command are ignored if the command is followed by <code>&amp;</code> and the <code>monitor</code> option is active. Otherwise, signals have the values inherited by the shell from its parent (but see also the <code>trap</code> built-in command below).  </p>
<h3>Execution.</h3>
<p> Each time a command is read, the above substitutions are carried out. If the command name matches one of the <i>Special Built-in Commands</i> listed below, it is executed within the current shell process. Next, the command name is checked to see if it matches a user defined function. If it does, the positional parameters are saved and then reset to the arguments of the <i>function</i> call. A function is also executed in the current shell process. When the <i>function</i> completes or issues a <code>return</code>, the positional parameter list is restored. For functions defined with the <code>function</code> <i>name</i> syntax, any trap set on <font SIZE="-1"><code>EXIT</code> </font> within the function is executed. The exit value of a <i>function</i> is the value of the last command executed. If a command name is not a <i>special built-in command</i> or a user defined <i>function</i>, but it is one of the built-in commands listed below, it is executed in the current shell process. </p>
<p> The shell variables <font SIZE="-1"><code>PATH</code></font> followed by the variable <font SIZE="-1"><code>FPATH</code></font> defines the list of directories to search for the command name. Alternative directory names are separated by a colon (<code>:</code>). The default path is equal to <code>getconf PATH</code> output. The current directory can be specified by two or more adjacent colons, or by a colon at the beginning or end of the path list. If the command name contains a <code>/</code>, then the search path is not used. Otherwise, each directory in the list of directories defined by <font SIZE="-1"><code>PATH</code></font> and <font SIZE="-1"><code>FPATH</code></font> is checked in order. If the directory being searched is contained in <font SIZE="-1"><code>FPATH</code></font> and contains a file whose name matches the command being searched, then this file is loaded into the current shell environment as if it were the argument to the <code>.</code> command except that only preset aliases are expanded, and a function of the given name is executed as described above. </p>
<p> If this directory is not in <font SIZE="-1"><code>FPATH</code></font> the shell first determines whether there is a built-in version of a command corresponding to a given pathname and if so it is invoked in the current process. If no built-in is found, the shell checks for a file named <code>.paths</code> in this directory. If found and there is a line of the form <code>FPATH=</code><i>path</i> where <i>path</i> names an existing directory then that directory is searched after immediately after the current directory as if it were found in the <font SIZE="-1"><code>FPATH</code></font> variable. If <i>path</i> does not begin with /, it is checked for relative to the directory being searched. </p>
<p> The <code>.paths</code> file is then checked for a line of the form <code>PLUGIN_LIB=</code><i>libname</i> <code>:</code> <i>libname</i> ] ... . Each library named by <i>libname</i> will be searched for as if it were an option argument to <code>builtin -f</code>, and if it contains a built-in of the specified name this will be executed instead of a command by this name. Any built-in loaded from a library found this way will be associated with the directory containing the <code>.paths</code> file so it will only execute if not found in an earlier directory. </p>
<p> Finally, the directory will be checked for a file of the given name. If the file has execute permission but is not an <code>a.out</code> file, it is assumed to be a file containing shell commands. A separate shell is spawned to read it. All non-exported variables are removed in this case. If the shell command file doesn&#8217;t have read permission, or if the <i>setuid</i> and/or <i>setgid</i> bits are set on the file, then the shell executes an agent whose job it is to set up the permissions and execute the shell with the shell command file passed down as an open file. If the <code>.paths</code> contains a line of the form <i>name</i><code>=</code><i>value</i> in the first or second line, then the environment variable <i>name</i> is modified by prepending the directory specified by <i>value</i> to the directory list. If <i>value</i> is not an absolute directory, then it specifies a directory relative to the directory that the executable was found. If the environment variable <i>name</i> does not already exist it will be added to the environment list for the specified command. A parenthesized command is executed in a sub-shell without removing non-exported variables.  </p>
<h3>Command Re-entry.</h3>
<p> The text of the last <font SIZE="-1"><code>HISTSIZE</code></font> (default 512) commands entered from a terminal device is saved in a <i>history</i> file. The file <font SIZE="-1"><code>$HOME</code></font><code>/.sh_history</code> is used if the <font SIZE="-1"><code>HISTFILE</code></font> variable is not set or if the file it names is not writable. A shell can access the commands of all <i>interactive</i> shells which use the same named <font SIZE="-1"><code>HISTFILE</code>. </font> The built-in command <code>hist</code> is used to list or edit a portion of this file. The portion of the file to be edited or listed can be selected by number or by giving the first character or characters of the command. A single command or range of commands can be specified. If you do not specify an editor program as an argument to <code>hist</code> then the value of the variable <font SIZE="-1"><code>HISTEDIT</code> </font> is used. If <font SIZE="-1"><code>HISTEDIT</code> </font> is unset, the obsolete variable <font SIZE="-1"><code>FCEDIT</code> </font> is used. If <font SIZE="-1"><code>FCEDIT</code> </font> is not defined, then <code>/bin/ed</code> is used. The edited command(s) is printed and re-executed upon leaving the editor unless you quit without writing. The <code>-s</code> option (and in obsolete versions, the editor name <code>-</code>) is used to skip the editing phase and to re-execute the command. In this case a substitution parameter of the form <i>old</i><code>=</code><i>new</i> can be used to modify the command before execution. For example, with the preset alias <code>r</code>, which is aliased to <code>&#180;hist -s&#180;</code>, typing `<code>r bad=good c</code>&#8216; will re-execute the most recent command which starts with the letter <code>c</code>, replacing the first occurrence of the string <code>bad</code> with the string <code>good</code>.  </p>
<h3>In-line Editing Options.</h3>
<p> Normally, each command line entered from a terminal device is simply typed followed by a <code>new-line</code> (`RETURN&#8217; or `LINE FEED&#8217;). If either the <code>emacs</code>, <code>gmacs</code>, or <code>vi</code> option is active, the user can edit the command line. To be in either of these edit modes <code>set</code> the corresponding option. An editing option is automatically selected each time the <font SIZE="-1"><code>VISUAL</code> </font> or <font SIZE="-1"><code>EDITOR</code> </font> variable is assigned a value ending in either of these option names. </p>
<p> The editing features require that the user&#8217;s terminal accept `RETURN&#8217; as carriage return without line feed and that a space (`&nbsp;<wbr>&#8216;) must overwrite the current character on the screen. </p>
<p> Unless the <code>multiline</code> option is on, the editing modes implement a concept where the user is looking through a window at the current line. The window width is the value of <font SIZE="-1"><code>COLUMNS</code> </font> if it is defined, otherwise 80. If the window width is too small to display the prompt and leave at least 8 columns to enter input, the prompt is truncated from the left. If the line is longer than the window width minus two, a mark is displayed at the end of the window to notify the user. As the cursor moves and reaches the window boundaries the window will be centered about the cursor. The mark is a <code>&gt;</code> (&lt;<code>,</code> <code>*</code>) if the line extends on the right (left, both) side(s) of the window. </p>
<p> The search commands in each edit mode provide access to the history file. Only strings are matched, not patterns, although a leading <code>^</code> in the string restricts the match to begin at the first character in the line. </p>
<p> Each of the edit modes has an operation to list the files or commands that match a partially entered word. When applied to the first word on the line, or the first word after a <code>;</code>, <code>|</code>, <code>&amp;</code>, or <code>(</code>, and the word does not begin with <code>&asymp;</code> or contain a <code>/</code>, the list of aliases, functions, and executable commands defined by the <font SIZE="-1"><code>PATH</code></font> variable that could match the partial word is displayed. Otherwise, the list of files that match the given word is displayed. If the partially entered word does not contain any file expansion characters, a <code>*</code> is appended before generating these lists. After displaying the generated list, the input line is redrawn. These operations are called command name listing and file name listing, respectively. There are additional operations, referred to as command name completion and file name completion, which compute the list of matching commands or files, but instead of printing the list, replace the current word with a complete or partial match. For file name completion, if the match is unique, a <code>/</code> is appended if the file is a directory and a space is appended if the file is not a directory. Otherwise, the longest common prefix for all the matching files replaces the word. For command name completion, only the portion of the file names after the last <code>/</code> are used to find the longest command prefix. If only a single name matches this prefix, then the word is replaced with the command name followed by a space. When using a <i>tab</i> for completion that does not yield a unique match, a subsequent <i>tab</i> will provide a numbered list of matching alternatives. A specific selection can be made by entering the selection number followed by a <i>tab</i>.  </p>
<h3>Key Bindings.</h3>
<p> The <font SIZE="-1"><code>KEYBD</code></font> trap can be used to intercept keys as they are typed and change the characters that are actually seen by the shell. This trap is executed after each character (or sequence of characters when the first character is ESC) is entered while reading from a terminal. The variable <code>.sh.edchar</code> contains the character or character sequence which generated the trap. Changing the value of <code>.sh.edchar</code> in the trap action causes the shell to behave as if the new value were entered from the keyboard rather than the original value. </p>
<p> The variable <code>.sh.edcol</code> is set to the input column number of the cursor at the time of the input. The variable <code>.sh.edmode</code> is set to ESC when in <code>vi</code> insert mode (see below) and is null otherwise. By prepending <code>${.sh.editmode}</code> to a value assigned to <code>.sh.edchar</code> it will cause the shell to change to control mode if it is not already in this mode. </p>
<p> This trap is not invoked for characters entered as arguments to editing directives, or while reading input for a character search.  </p>
<h3>Emacs Editing Mode.</h3>
<p> This mode is entered by enabling either the <code>emacs</code> or <code>gmacs</code> option. The only difference between these two modes is the way they handle <code>^T</code>. To edit, the user moves the cursor to the point needing correction and then inserts or deletes characters or words as needed. All the editing commands are control characters or escape sequences. The notation for control characters is caret (<code>^</code>) followed by the character. For example, <code>^F</code> is the notation for control <code>F</code>. This is entered by depressing `f&#8217; while holding down the `CTRL&#8217; (control) key. The `SHIFT&#8217; key is <i>not</i> depressed. (The notation <code>^?</code> indicates the DEL (delete) key.) </p>
<p> The notation for escape sequences is <code>M-</code> followed by a character. For example, <code>M-f</code> (pronounced Meta f) is entered by depressing ESC (ascii <code>033</code>) followed by `f&#8217;. (<code>M-F</code> would be the notation for ESC followed by `SHIFT&#8217; (capital) `F&#8217;.) </p>
<p> All edit commands operate from any place on the line (not just at the beginning). Neither the `RETURN&#8217; nor the `LINE FEED&#8217; key is entered after edit commands except when noted. </p>
<dl>
<dt><code>^F</code></dt>
<dd> <p> Move cursor forward (right) one character. </p>
 </dd></dl>
<dl>
<dt><code>M-[C</code></dt>
<dd> <p> Move cursor forward (right) one character. </p>
 </dd></dl>
<dl>
<dt><code>M-f</code></dt>
<dd> <p> Move cursor forward one word. (The <code>emacs</code> editor&#8217;s idea of a word is a string of characters consisting of only letters, digits and underscores.) </p>
 </dd></dl>
<dl>
<dt><code>^B</code></dt>
<dd> <p> Move cursor backward (left) one character. </p>
 </dd></dl>
<dl>
<dt><code>M-[D</code></dt>
<dd> <p> Move cursor backward (left) one character. </p>
 </dd></dl>
<dl>
<dt><code>M-b</code></dt>
<dd> <p> Move cursor backward one word. </p>
 </dd></dl>
<dl>
<dt><code>^A</code></dt>
<dd> <p> Move cursor to start of line. </p>
 </dd></dl>
<dl>
<dt><code>M-[H</code></dt>
<dd> <p> Move cursor to start of line. </p>
 </dd></dl>
<dl>
<dt><code>^E</code></dt>
<dd> <p> Move cursor to end of line. </p>
 </dd></dl>
<dl>
<dt><code>M-[Y</code></dt>
<dd> <p> Move cursor to end of line. </p>
 </dd></dl>
<dl>
<dt><code>^]</code><i>char</i></dt>
<dd> <p> Move cursor forward to character <i>char</i> on current line. </p>
 </dd></dl>
<dl>
<dt><code>M-^]</code><i>char</i></dt>
<dd> <p> Move cursor backward to character <i>char</i> on current line. </p>
 </dd></dl>
<dl>
<dt><code>^X^X</code></dt>
<dd> <p> Interchange the cursor and mark. </p>
 </dd></dl>
<dl>
<dt><i>erase</i></dt>
<dd> <p> (User defined erase character as defined by the <i><a href="/docs/linux/man/1-stty/">stty</a></i>(1) command, usually <code>^H</code> or <code>#</code>.) Delete previous character. </p>
 </dd></dl>
<dl>
<dt><i>lnext</i></dt>
<dd> <p> (User defined literal next character as defined by the <i><a href="/docs/linux/man/1-stty/">stty</a></i>(1) command, or <code>^V</code> if not defined.) Removes the next character&#8217;s editing features (if any). </p>
 </dd></dl>
<dl>
<dt><code>^D</code></dt>
<dd> <p> Delete current character. </p>
 </dd></dl>
<dl>
<dt><code>M-d</code></dt>
<dd> <p> Delete current word. </p>
 </dd></dl>
<dl>
<dt><code>M-^H</code></dt>
<dd> <p> (Meta-backspace) Delete previous word. </p>
 </dd></dl>
<dl>
<dt><code>M-h</code></dt>
<dd> <p> Delete previous word. </p>
 </dd></dl>
<dl>
<dt><code>M-^?</code></dt>
<dd> <p> (Meta-DEL) Delete previous word (if your interrupt character is <code>^?</code> (DEL, the default) then this command will not work). </p>
 </dd></dl>
<dl>
<dt><code>^T</code></dt>
<dd> <p> Transpose current character with previous character and advance the cursor in <i>emacs</i> mode. Transpose two previous characters in <i>gmacs</i> mode. </p>
 </dd></dl>
<dl>
<dt><code>^C</code></dt>
<dd> <p> Capitalize current character. </p>
 </dd></dl>
<dl>
<dt><code>M-c</code></dt>
<dd> <p> Capitalize current word. </p>
 </dd></dl>
<dl>
<dt><code>M-l</code></dt>
<dd> <p> Change the current word to lower case. </p>
 </dd></dl>
<dl>
<dt><code>^K</code></dt>
<dd> <p> Delete from the cursor to the end of the line. If preceded by a numerical parameter whose value is less than the current cursor position, then delete from given position up to the cursor. If preceded by a numerical parameter whose value is greater than the current cursor position, then delete from cursor up to given cursor position. </p>
 </dd></dl>
<dl>
<dt><code>^W</code></dt>
<dd> <p> Kill from the cursor to the mark. </p>
 </dd></dl>
<dl>
<dt><code>M-p</code></dt>
<dd> <p> Push the region from the cursor to the mark on the stack. </p>
 </dd></dl>
<dl>
<dt><i>kill</i></dt>
<dd> <p> (User defined kill character as defined by the stty command, usually <code>^G</code> or <code>@</code>.) Kill the entire current line. If two <i>kill</i> characters are entered in succession, all kill characters from then on cause a line feed (useful when using paper terminals). </p>
 </dd></dl>
<dl>
<dt><code>^Y</code></dt>
<dd> <p> Restore last item removed from line. (Yank item back to the line.) </p>
 </dd></dl>
<dl>
<dt><code>^L</code></dt>
<dd> <p> Line feed and print current line. </p>
 </dd></dl>
<dl>
<dt><code>M-^L</code></dt>
<dd> <p> Clear the screen. </p>
 </dd></dl>
<dl>
<dt><code>^@</code></dt>
<dd> <p> (Null character) Set mark. </p>
 </dd></dl>
<dl>
<dt><code>M-</code><i>space</i></dt>
<dd> <p> (Meta space) Set mark. </p>
 </dd></dl>
<dl>
<dt><code>^J</code></dt>
<dd> <p> (New line) Execute the current line. </p>
 </dd></dl>
<dl>
<dt><code>^M</code></dt>
<dd> <p> (Return) Execute the current line. </p>
 </dd></dl>
<dl>
<dt><i>eof</i></dt>
<dd> <p> End-of-file character, normally <code>^D</code>, is processed as an End-of-file only if the current line is null. </p>
 </dd></dl>
<dl>
<dt><code>^P</code></dt>
<dd> <p> Fetch previous command. Each time <code>^P</code> is entered the previous command back in time is accessed. Moves back one line when not on the first line of a multi-line command. </p>
 </dd></dl>
<dl>
<dt><code>M-[A</code></dt>
<dd> <p> If the cursor is at the end of the line, it is equivalent to <code>^R</code> with <i>string</i> set to the contents of the current line. Otherwise, it is equivalent to <code>^P.</code> </p>
 </dd></dl>
<dl>
<dt><code>M-&lt;</code></dt>
<dd> <p> Fetch the least recent (oldest) history line. </p>
 </dd></dl>
<dl>
<dt><code>M-&gt;</code></dt>
<dd> <p> Fetch the most recent (youngest) history line. </p>
 </dd></dl>
<dl>
<dt><code>^N</code></dt>
<dd> <p> Fetch next command line. Each time <code>^N</code> is entered the next command line forward in time is accessed. </p>
 </dd></dl>
<dl>
<dt><code>M-[B</code></dt>
<dd> <p> Equivalent to <code>^N.</code> </p>
 </dd></dl>
<dl>
<dt><code>^R</code><i>string</i></dt>
<dd> <p> Reverse search history for a previous command line containing <i>string</i>. If a parameter of zero is given, the search is forward. <i>String</i> is terminated by a `RETURN&#8217; or `NEW LINE&#8217;. If string is preceded by a <code>^</code>, the matched line must begin with <i>string</i>. If <i>string</i> is omitted, then the next command line containing the most recent <i>string</i> is accessed. In this case a parameter of zero reverses the direction of the search. </p>
 </dd></dl>
<dl>
<dt><code>^O</code></dt>
<dd> <p> Operate - Execute the current line and fetch the next line relative to current line from the history file. </p>
 </dd></dl>
<dl>
<dt><code>M-</code><i>digits</i></dt>
<dd> <p> (Escape) Define numeric parameter, the digits are taken as a parameter to the next command. The commands that accept a parameter are <code>^F</code>, <code>^B</code>, <i>erase</i>, <code>^C</code>, <code>^D</code>, <code>^K</code>, <code>^R</code>, <code>^P</code>, <code>^N</code>, <code>^]</code>, <code>M-.</code>, <code>M-^]</code>, <code>M-_</code>, <code>M-=</code>, <code>M-b</code>, <code>M-c</code>, <code>M-d</code>, <code>M-f</code>, <code>M-h</code>, <code>M-l</code> and <code>M-^H</code>. </p>
 </dd></dl>
<dl>
<dt><code>M-</code><i>letter</i></dt>
<dd> <p> Soft-key - Your alias list is searched for an alias by the name <code>_</code><i>letter</i> and if an alias of this name is defined, its value will be inserted on the input queue. The <i>letter</i> must not be one of the above meta-functions. </p>
 </dd></dl>
<dl>
<dt><code>M-[</code><i>letter</i></dt>
<dd> <p> Soft-key - Your alias list is searched for an alias by the name <code>__</code><i>letter</i> and if an alias of this name is defined, its value will be inserted on the input queue. This can be used to program function keys on many terminals. </p>
 </dd></dl>
<dl>
<dt><code>M-.</code></dt>
<dd> <p> The last word of the previous command is inserted on the line. If preceded by a numeric parameter, the value of this parameter determines which word to insert rather than the last word. </p>
 </dd></dl>
<dl>
<dt><code>M-_</code></dt>
<dd> <p> Same as <code>M-.</code>. </p>
 </dd></dl>
<dl>
<dt><code>M-*</code></dt>
<dd> <p> Attempt file name generation on the current word. An asterisk is appended if the word doesn&#8217;t match any file or contain any special pattern characters. </p>
 </dd></dl>
<dl>
<dt><code>M-ESC</code></dt>
<dd> <p> Command or file name completion as described above. </p>
 </dd></dl>
<dl>
<dt><code>^I</code><i> tab</i></dt>
<dd> <p> Attempts command or file name completion as described above. If a partial completion occurs, repeating this will behave as if <code>M-=</code> were entered. If no match is found or entered after <i>space</i>, a <i>tab</i> is inserted. </p>
 </dd></dl>
<dl>
<dt><code>M-=</code></dt>
<dd> <p> If not preceded by a numeric parameter, it generates the list of matching commands or file names as described above. Otherwise, the word under the cursor is replaced by the item corresponding to the value of the numeric parameter from the most recently generated command or file list. If the cursor is not on a word, it is inserted instead. </p>
 </dd></dl>
<dl>
<dt><code>^U</code></dt>
<dd> <p> Multiply parameter of next command by 4. </p>
 </dd></dl>
<dl>
<dt><code>\</code></dt>
<dd> <p> Escape next character. Editing characters, the user&#8217;s erase, kill and interrupt (normally <code>^?</code>) characters may be entered in a command line or in a search string if preceded by a <code>\</code>. The <code>\</code> removes the next character&#8217;s editing features (if any). </p>
 </dd></dl>
<dl>
<dt><code>M-^V</code></dt>
<dd> <p> Display version of the shell. </p>
 </dd></dl>
<dl>
<dt><code>M-#</code></dt>
<dd> <p> If the line does not begin with a <code>#</code>, a <code>#</code> is inserted at the beginning of the line and after each new-line, and the line is entered. This causes a comment to be inserted in the history file. If the line begins with a <code>#</code>, the <code>#</code> is deleted and one <code>#</code> after each new-line is also deleted. </p>
 </dd></dl>
<h3>Vi Editing Mode.</h3>
<p> There are two typing modes. Initially, when you enter a command you are in the <i>input</i> mode. To edit, the user enters <i>control</i> mode by typing ESC (<code>033</code>) and moves the cursor to the point needing correction and then inserts or deletes characters or words as needed. Most control commands accept an optional repeat <i>count</i> prior to the command. </p>
<p> When in <code>vi</code> mode on most systems, canonical processing is initially enabled and the command will be echoed again if the speed is 1200 baud or greater and it contains any control characters or less than one second has elapsed since the prompt was printed. The ESC character terminates canonical processing for the remainder of the command and the user can then modify the command line. This scheme has the advantages of canonical processing with the type-ahead echoing of raw mode. </p>
<p> If the option <code>viraw</code> is also set, the terminal will always have canonical processing disabled. This mode is implicit for systems that do not support two alternate end of line delimiters, and may be helpful for certain terminals.  </p>
<wbr><wbr><wbr><wbr><wbr><h3>Input Edit Commands</h3>
<dl>
<dd> <p> By default the editor is in input mode. </p>
 </dd>
<dl>
<dt><i>erase</i></dt>
<dd> <p> (User defined erase character as defined by the stty command, usually <code>^H</code> or <code>#</code>.) Delete previous character. </p>
 </dd>
<dt><code>^W</code></dt>
<dd> <p> Delete the previous blank separated word. On some systems the <code>viraw</code> option may be required for this to work. </p>
 </dd>
<dt><i>eof</i></dt>
<dd> <p> As the first character of the line causes the shell to terminate unless the <code>ignoreeof</code> option is set. Otherwise this character is ignored. </p>
 </dd>
<dt><i>lnext</i></dt>
<dd> <p> (User defined literal next character as defined by the <i><a href="/docs/linux/man/1-stty/">stty</a></i>(1) or <code>^V</code> if not defined.) Removes the next character&#8217;s editing features (if any). On some systems the <code>viraw</code> option may be required for this to work. </p>
 </dd>
<dt><code>\</code></dt>
<dd> <p> Escape the next <i>erase</i> or <i>kill</i> character. </p>
 </dd>
<dt><code>^I</code><i> tab</i></dt>
<dd> <p> Attempts command or file name completion as described above and returns to input mode. If a partial completion occurs, repeating this will behave as if <code>=</code> were entered from control mode. If no match is found or entered after <i>space</i>, a <i>tab</i> is inserted. </p>
 </dd></dl>
</dl>
<wbr><wbr><wbr><wbr><wbr><h3>Motion Edit Commands</h3>
<dl>
<dd> <p> These commands will move the cursor. </p>
 </dd>
<dl>
<dt>[<i>count</i>]<code>l</code></dt>
<dd> <p> Cursor forward (right) one character. </p>
 </dd>
<dt>[<i>count</i>]<code>[C</code></dt>
<dd> <p> Cursor forward (right) one character. </p>
 </dd>
<dt>[<i>count</i>]<code>w</code></dt>
<dd> <p> Cursor forward one alpha-numeric word. </p>
 </dd>
<dt>[<i>count</i>]<code>W</code></dt>
<dd> <p> Cursor to the beginning of the next word that follows a blank. </p>
 </dd>
<dt>[<i>count</i>]<code>e</code></dt>
<dd> <p> Cursor to end of word. </p>
 </dd>
<dt>[<i>count</i>]<code>E</code></dt>
<dd> <p> Cursor to end of the current blank delimited word. </p>
 </dd>
<dt>[<i>count</i>]<code>h</code></dt>
<dd> <p> Cursor backward (left) one character. </p>
 </dd>
<dt>[<i>count</i>]<code>[D</code></dt>
<dd> <p> Cursor backward (left) one character. </p>
 </dd>
<dt>[<i>count</i>]<code>b</code></dt>
<dd> <p> Cursor backward one word. </p>
 </dd>
<dt>[<i>count</i>]<code>B</code></dt>
<dd> <p> Cursor to preceding blank separated word. </p>
 </dd>
<dt>[<i>count</i>]<code>|</code></dt>
<dd> <p> Cursor to column <i>count</i>. </p>
 </dd>
<dt>[<i>count</i>]<code>f</code><i>c</i></dt>
<dd> <p> Find the next character <i>c</i> in the current line. </p>
 </dd>
<dt>[<i>count</i>]<code>F</code><i>c</i></dt>
<dd> <p> Find the previous character <i>c</i> in the current line. </p>
 </dd>
<dt>[<i>count</i>]<code>t</code><i>c</i></dt>
<dd> <p> Equivalent to <code>f</code> followed by <code>h</code>. </p>
 </dd>
<dt>[<i>count</i>]<code>T</code><i>c</i></dt>
<dd> <p> Equivalent to <code>F</code> followed by <code>l</code>. </p>
 </dd>
<dt>[<i>count</i>]<code>;</code></dt>
<dd> <p> Repeats <i>count</i> times, the last single character find command, <code>f</code>, <code>F</code>, <code>t</code>, or <code>T</code>. </p>
 </dd>
<dt>[<i>count</i>]<code>,</code></dt>
<dd> <p> Reverses the last single character find command <i>count</i> times. </p>
 </dd>
<dt><code>0</code></dt>
<dd> <p> Cursor to start of line. </p>
 </dd>
<dt><code>^</code></dt>
<dd> <p> Cursor to start of line. </p>
 </dd>
<dt><code>[H</code></dt>
<dd> <p> Cursor to first non-blank character in line. </p>
 </dd>
<dt><code>$</code></dt>
<dd> <p> Cursor to end of line. </p>
 </dd>
<dt><code>[Y</code></dt>
<dd> <p> Cursor to end of line. </p>
 </dd>
<dt><code>%</code></dt>
<dd> <p> Moves to balancing <code>(</code>, <code>)</code>, <code>{</code>, <code>}</code>, <code>[</code>, or <code>]</code>. If cursor is not on one of the above characters, the remainder of the line is searched for the first occurrence of one of the above characters first. </p>
 </dd></dl>
</dl>
<wbr><wbr><wbr><wbr><wbr><h3>Search Edit Commands</h3>
<dl>
<dd> <p> These commands access your command history. </p>
 </dd>
<dl>
<dt>[<i>count</i>]<code>k</code></dt>
<dd> <p> Fetch previous command. Each time <code>k</code> is entered the previous command back in time is accessed. </p>
 </dd>
<dt>[<i>count</i>]<code>-</code></dt>
<dd> <p> Equivalent to <code>k</code>. </p>
 </dd>
<dt>[<i>count</i>]<code>[A</code></dt>
<dd> <p> If cursor is at the end of the line it is equivalent to <code>/</code> with <i>string^set to the contents of the current line.</i> Otherwise, it is equivalent to <code>k</code>. </p>
 </dd>
<dt>[<i>count</i>]<code>j</code></dt>
<dd> <p> Fetch next command. Each time <code>j</code> is entered the next command forward in time is accessed. </p>
 </dd>
<dt>[<i>count</i>]<code>+</code></dt>
<dd> <p> Equivalent to <code>j</code>. </p>
 </dd>
<dt>[<i>count</i>]<code>[B</code></dt>
<dd> <p> Equivalent to <code>j</code>. </p>
 </dd>
<dt>[<i>count</i>]<code>G</code></dt>
<dd> <p> The command number <i>count</i> is fetched. The default is the least recent history command. </p>
 </dd>
<dt><code>/</code><i>string</i></dt>
<dd> <p> Search backward through history for a previous command containing <i>string</i>. <i>String</i> is terminated by a `RETURN&#8217; or `NEW LINE&#8217;. If string is preceded by a <code>^</code>, the matched line must begin with <i>string</i>. If <i>string</i> is null, the previous string will be used. </p>
 </dd>
<dt><code>?</code><i>string</i></dt>
<dd> <p> Same as <code>/</code> except that search will be in the forward direction. </p>
 </dd>
<dt><code>n</code></dt>
<dd> <p> Search for next match of the last pattern to <code>/</code> or <code>?</code> commands. </p>
 </dd>
<dt><code>N</code></dt>
<dd> <p> Search for next match of the last pattern to <code>/</code> or <code>?</code>, but in reverse direction. </p>
 </dd></dl>
</dl>
<wbr><wbr><wbr><wbr><wbr><h3>Text Modification Edit Commands</h3>
<dl>
<dd> <p> These commands will modify the line. </p>
 </dd>
<dl>
<dt><code>a</code></dt>
<dd> <p> Enter input mode and enter text after the current character. </p>
 </dd>
<dt><code>A</code></dt>
<dd> <p> Append text to the end of the line. Equivalent to <code>$a</code>. </p>
 </dd>
<dt>[<i>count</i>]<code>c</code><i>motion</i></dt>
<dd>  </dd>
<dt><code>c</code>[<i>count</i>]<i>motion</i></dt>
<dd> <p> Delete current character through the character that <i>motion</i> would move the cursor to and enter input mode. If <i>motion</i> is <code>c</code>, the entire line will be deleted and input mode entered. </p>
 </dd>
<dt><code>C</code></dt>
<dd> <p> Delete the current character through the end of line and enter input mode. Equivalent to <code>c$</code>. </p>
 </dd>
<dt><code>S</code></dt>
<dd> <p> Equivalent to <code>cc</code>. </p>
 </dd>
<dt>[<i>count</i>]<code>s</code></dt>
<dd> <p> Replace characters under the cursor in input mode. </p>
 </dd>
<dt><code>D</code></dt>
<dd> <p> Delete the current character through the end of line. Equivalent to <code>d$</code>. </p>
 </dd>
<dt>[<i>count</i>]<code>d</code><i>motion</i></dt>
<dd>  </dd>
<dt><code>d</code>[<i>count</i>]<i>motion</i></dt>
<dd> <p> Delete current character through the character that <i>motion</i> would move to. If <i>motion</i> is <code>d ,</code> the entire line will be deleted. </p>
 </dd>
<dt><code>i</code></dt>
<dd> <p> Enter input mode and insert text before the current character. </p>
 </dd>
<dt><code>I</code></dt>
<dd> <p> Insert text before the beginning of the line. Equivalent to <code>0i</code>. </p>
 </dd>
<dt>[<i>count</i>]<code>P</code></dt>
<dd> <p> Place the previous text modification before the cursor. </p>
 </dd>
<dt>[<i>count</i>]<code>p</code></dt>
<dd> <p> Place the previous text modification after the cursor. </p>
 </dd>
<dt><code>R</code></dt>
<dd> <p> Enter input mode and replace characters on the screen with characters you type overlay fashion. </p>
 </dd>
<dt>[<i>count</i>]<code>r</code><i>c</i></dt>
<dd> <p> Replace the <i>count</i> character(s) starting at the current cursor position with <i>c</i>, and advance the cursor. </p>
 </dd>
<dt>[<i>count</i>]<code>x</code></dt>
<dd> <p> Delete current character. </p>
 </dd>
<dt>[<i>count</i>]<code>X</code></dt>
<dd> <p> Delete preceding character. </p>
 </dd>
<dt>[<i>count</i>]<code>.</code></dt>
<dd> <p> Repeat the previous text modification command. </p>
 </dd>
<dt>[<i>count</i>]<code>&asymp;</code></dt>
<dd> <p> Invert the case of the <i>count</i> character(s) starting at the current cursor position and advance the cursor. </p>
 </dd>
<dt>[<i>count</i>]<code>_</code></dt>
<dd> <p> Causes the <i>count</i> word of the previous command to be appended and input mode entered. The last word is used if <i>count</i> is omitted. </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> Causes an <code>*</code> to be appended to the current word and file name generation attempted. If no match is found, it rings the bell. Otherwise, the word is replaced by the matching pattern and input mode is entered. </p>
 </dd>
<dt><code>\</code></dt>
<dd> <p> Command or file name completion as described above. </p>
 </dd></dl>
</dl>
<wbr><wbr><wbr><wbr><wbr><h3>Other Edit Commands</h3>
<dl>
<dd> <p> Miscellaneous commands. </p>
 </dd>
<dl>
<dt>[<i>count</i>]<code>y</code><i>motion</i></dt>
<dd>  </dd>
<dt><code>y</code>[<i>count</i>]<i>motion</i></dt>
<dd> <p> Yank current character through character that <i>motion</i> would move the cursor to and puts them into the delete buffer. The text and cursor are unchanged. </p>
 </dd>
<dt><code>yy</code></dt>
<dd> <p> Yanks the entire line. </p>
 </dd>
<dt><code>Y</code></dt>
<dd> <p> Yanks from current position to end of line. Equivalent to <code>y$</code>. </p>
 </dd>
<dt><code>u</code></dt>
<dd> <p> Undo the last text modifying command. </p>
 </dd>
<dt><code>U</code></dt>
<dd> <p> Undo all the text modifying commands performed on the line. </p>
 </dd>
<dt>[<i>count</i>]<code>v</code></dt>
<dd> <p> Returns the command <code>hist -e ${</code><font SIZE="-1"><code>VISUAL</code></font><code>:-${</code><font SIZE="-1"><code>EDITOR</code></font><code>:-vi}}</code><i> count</i> in the input buffer. If <i>count</i> is omitted, then the current line is used. </p>
 </dd>
<dt><code>^L</code></dt>
<dd> <p> Line feed and print current line. Has effect only in control mode. </p>
 </dd>
<dt><code>^J</code></dt>
<dd> <p> (New line) Execute the current line, regardless of mode. </p>
 </dd>
<dt><code>^M</code></dt>
<dd> <p> (Return) Execute the current line, regardless of mode. </p>
 </dd>
<dt><code>#</code></dt>
<dd> <p> If the first character of the command is a <code>#</code>, then this command deletes this <code>#</code> and each <code>#</code> that follows a newline. Otherwise, sends the line after inserting a <code>#</code> in front of each line in the command. Useful for causing the current line to be inserted in the history as a comment and uncommenting previously commented commands in the history file. </p>
 </dd>
<dt>[<i>count</i>]<code>=</code></dt>
<dd> <p> If <i>count</i> is not specified, it generates the list of matching commands or file names as described above. Otherwise, the word under the the cursor is replaced by the <i>count</i> item from the most recently generated command or file list. If the cursor is not on a word, it is inserted instead. </p>
 </dd>
<dt><code>@</code><i>letter</i></dt>
<dd> <p> Your alias list is searched for an alias by the name <code>_</code><i>letter</i> and if an alias of this name is defined, its value will be inserted on the input queue for processing. </p>
 </dd>
<dt><code>^V</code></dt>
<dd> <p> Display version of the shell. </p>
 </dd></dl>
</dl>
<h3>Built-in Commands.</h3>
<p> The following simple-commands are executed in the shell process. Input/Output redirection is permitted. Unless otherwise indicated, the output is written on file descriptor 1 and the exit status, when there is no syntax error, is zero. Except for <code>:</code>, <code>true</code>, <code>false</code>, <code>echo</code>, <code>newgrp</code>, and <code>login</code>, all built-in commands accept <code>--</code> to indicate end of options. They also interpret the option <code>--man</code> as a request to display the man page onto standard error and <code>-?</code> as a help request which prints a <i>usage</i> message on standard error. Commands that are preceded by one or two - symbols are special built-in commands and are treated specially in the following ways: </p>
<dl>
<dt>1.</dt>
<dd> <p> Variable assignment lists preceding the command remain in effect when the command completes. </p>
 </dd>
<dt>2.</dt>
<dd> <p> I/O redirections are processed after variable assignments. </p>
 </dd>
<dt>3.</dt>
<dd> <p> Errors cause a script that contains them to abort. </p>
 </dd>
<dt>4.</dt>
<dd> <p> They are not valid function names. </p>
 </dd>
<dt>5.</dt>
<dd> <p> Words following a command preceded by -- that are in the format of a variable assignment are expanded with the same rules as a variable assignment. This means that tilde substitution is performed after the <code>=</code> sign and field splitting and file name generation are not performed. These are called <i>declaration</i> built-ins. </p>
 </dd>
<dt>- <code>:</code><i>arg</i> ... ]</dt>
<dd> <p> The command only expands parameters. <br />
 </p>
 </dd>
<dt>- <code>. </code><i>name</i><i>arg</i> ... ]</dt>
<dd> <p> If <i>name</i> is a function defined with the <code>function</code> <i>name</i> reserved word syntax, the function is executed in the current environment (as if it had been defined with the <i>name</i><code>()</code> syntax.) Otherwise if <i>name</i> refers to a file, the file is read in its entirety and the commands are executed in the current shell environment. The search path specified by <font SIZE="-1"><code>PATH</code></font> is used to find the directory containing the file. If any arguments <i>arg</i> are given, they become the positional parameters while processing the <code>.</code> command and the original positional parameters are restored upon completion. Otherwise the positional parameters are unchanged. The exit status is the exit status of the last command executed. </p>
 </dd>
<dt>-- <code>alias</code><code>-ptx</code> ] <i>name</i><code>=</code><i>value</i> ] ] ...</dt>
<dd> <p> <code>alias</code> with no arguments prints the list of aliases in the form <i>name=value</i> on standard output. The <code>-p</code> option causes the word <code>alias</code> to be inserted before each one. When one or more arguments are given, an <i>alias</i> is defined for each <i>name</i> whose <i>value</i> is given. A trailing space in <i>value</i> causes the next word to be checked for alias substitution. The obsolete <code>-t</code> option is used to set and list tracked aliases. The value of a tracked alias is the full pathname corresponding to the given <i>name</i>. The value becomes undefined when the value of <font SIZE="-1"><code>PATH</code> </font> is reset but the alias remains tracked. Without the <code>-t</code> option, for each <i>name</i> in the argument list for which no <i>value</i> is given, the name and value of the alias is printed. The obsolete <code>-x</code> option has no effect. The exit status is non-zero if a <i>name</i> is given, but no value, and no alias has been defined for the <i>name</i>. </p>
 </dd>
<dt><code>bg</code><i>job</i>... ]</dt>
<dd> <p> This command is only on systems that support job control. Puts each specified <i>job</i> into the background. The current job is put in the background if <i>job</i> is not specified. See <i>Jobs</i> for a description of the format of <i>job</i>. </p>
 </dd>
<dt>- <code>break</code><i>n</i> ]</dt>
<dd> <p> Exit from the enclosing <code>for</code>, <code>while</code>, <code>until</code>, or <code>select</code> loop, if any. If <i>n</i> is specified, then break <i>n</i> levels. </p>
 </dd>
<dt><code>builtin</code><code>-ds</code> ] <code>-f</code><i>file</i> ] <i>name</i> ... ]</dt>
<dd> <p> If <i>name</i> is not specified, and no <code>-f</code> option is specified, the built-ins are printed on standard output. The <code>-s</code> option prints only the special built-ins. Otherwise, each <i>name</i> represents the pathname whose basename is the name of the built-in. The entry point function name is determined by prepending <code>b_</code> to the built-in name. A built-in specified by a pathname will only be executed when that pathname would be found during the path search. Built-ins found in libraries loaded via the <code>.paths</code> file will be associate with the pathname of the directory containing the <code>.paths</code> file. </p>
 </dd></dl>
<p> The ISO C/C++ prototype is <code>b_</code><i>mycommand</i><code>(int</code> <i>argc</i>, <code>char *</code><i>argv</i><code>[]</code>, <code>void *</code><i>context</i><code>)</code> for the builtin command <i>mycommand</i> where <i>argv</i> is array an of <i>argc</i> elements and context is an optional pointer to a <code>Shell_t</code> structure as described in <code>&lt;ast/shell.h&gt;</code>. </p>
<p> Special built-ins cannot be bound to a pathname or deleted. The <code>-d</code> option deletes each of the given built-ins. On systems that support dynamic loading, the <code>-f</code> option names a shared library containing the code for built-ins. The shared library prefix and/or suffix, which depend on the system, can be omitted. Once a library is loaded, its symbols become available for subsequent invocations of <code>builtin</code>. Multiple libraries can be specified with separate invocations of the <code>builtin</code> command. Libraries are searched in the reverse order in which they are specified. When a library is loaded, it looks for a function in the library whose name is <code>lib_init()</code> and invokes this function with an argument of <code>0</code>. </p>
<dl>
<dd> <p> <code>cd</code> <code>-LP</code> ] <i>arg</i> ] </p>
 </dd>
<dt><code>cd</code><code>-LP</code> ] <i>old</i><i>new</i></dt>
<dd> <p> This command can be in either of two forms. In the first form it changes the current directory to <i>arg</i>. If <i>arg</i> is <code>-</code> the directory is changed to the previous directory. The shell variable <font SIZE="-1"><code>HOME</code></font> is the default <i>arg</i>. The variable <font SIZE="-1"><code>PWD</code> </font> is set to the current directory. The shell variable <font SIZE="-1"><code>CDPATH</code></font> defines the search path for the directory containing <i>arg</i>. Alternative directory names are separated by a colon (<code>:</code>). The default path is <code>&lt;null&gt;</code> (specifying the current directory). Note that the current directory is specified by a null path name, which can appear immediately after the equal sign or between the colon delimiters anywhere else in the path list. If <i>arg</i> begins with a <code>/</code> then the search path is not used. Otherwise, each directory in the path is searched for <i>arg</i>. </p>
<p> The second form of <code>cd</code> substitutes the string <i>new</i> for the string <i>old</i> in the current directory name, <font SIZE="-1"><code>PWD</code>, </font> and tries to change to this new directory. </p>
<p> By default, symbolic link names are treated literally when finding the directory name. This is equivalent to the <code>-L</code> option. The <code>-P</code> option causes symbolic links to be resolved when determining the directory. The last instance of <code>-L</code> or <code>-P</code> on the command line determines which method is used. </p>
<p> The <code>cd</code> command may not be executed by <code>rksh.</code> <code>rksh93.</code> </p>
 </dd>
<dt><code>command</code><code>-pvxV</code> ] <i>name</i><i>arg</i> ... ]</dt>
<dd> <p> Without the <code>-v</code> or <code>-V</code> options, <code>command</code> executes <i>name</i> with the arguments given by <i>arg</i>. The <code>-p</code> option causes a default path to be searched rather than the one defined by the value of <font SIZE="-1"><code>PATH</code>. </font> Functions will not be searched for when finding <i>name</i>. In addition, if <i>name</i> refers to a special built-in, none of the special properties associated with the leading daggers will be honored. (For example, the predefined alias <code>redirect=&#180;command exec&#180;</code> prevents a script from terminating when an invalid redirection is given.) With the <code>-x</code> option, if command execution would result in a failure because there are too many arguments, errno <font SIZE="-1"><code>E2BIG</code>, </font> the shell will invoke command <i>name</i> multiple times with a subset of the arguments on each invocation. Arguments that occur prior to the first word that expands to multiple arguments and after the last word that expands to multiple arguments will be passed on each invocation. The exit status will be the maximum invocation exit status. With the <code>-v</code> option, <code>command</code> is equivalent to the built-in <code>whence</code> command described below. The <code>-V</code> option causes <code>command</code> to act like <code>whence -v</code>. </p>
 </dd>
<dt>- <code>continue</code><i>n</i> ]</dt>
<dd> <p> Resume the next iteration of the enclosing <code>for</code>, <code>while</code>, <code>until</code>, or <code>select</code> loop. If <i>n</i> is specified, then resume at the <i>n</i>-th enclosing loop. </p>
 </dd>
<dt><code>disown</code><i>job</i>... ]</dt>
<dd> <p> Causes the shell not to send a HUP signal to each given <i>job</i>, or all active jobs if <i>job</i> is omitted, when a login shell terminates. </p>
 </dd>
<dt><code>echo</code><i>arg</i> ... ]</dt>
<dd> <p> When the first <i>arg</i> does not begin with a -, and none of the arguments contain a \, then <code>echo</code> prints each of its arguments separated by a space and terminated by a new-line. Otherwise, the behavior of <code>echo</code> is system dependent and <code>print</code> or <code>printf</code> described below should be used. See <i><a href="/docs/linux/man/1-echo/">echo</a></i>(1) for usage and description. </p>
 </dd>
<dt>-- <code>enum</code><code>-i</code> ] <i>type</i>=(<i>value</i> ...) ]</dt>
<dd> <p> Creates a declaration command named <i>type</i> that is an integer type that allows one of the specified <i>value</i>s as enumeration names. If <code>=(</code><i>value ...</i><code>)</code> is omitted, then <i>type</i> must be an indexed array variable with at least two elements and the values are taken from this array variable. If <code>-i</code> is specified the values are case insensitive. </p>
 </dd>
<dt>- <code>eval</code><i>arg</i> ... ]</dt>
<dd> <p> The arguments are read as input to the shell and the resulting command(s) executed. </p>
 </dd>
<dt>- <code>exec</code><code>-c</code> ] <code>-a</code><i>name</i> ] <i>arg</i> ... ]</dt>
<dd> <p> If <i>arg</i> is given, the command specified by the arguments is executed in place of this shell without creating a new process. The <code>-c</code> option causes the environment to be cleared before applying variable assignments associated with the <code>exec</code> invocation. The <code>-a</code> option causes <i>name</i> rather than the first <i>arg</i>, to become <code>argv[0]</code> for the new process. Input/output arguments may appear and affect the current process. If <i>arg</i> is not given, the effect of this command is to modify file descriptors as prescribed by the input/output redirection list. In this case, any file descriptor numbers greater than 2 that are opened with this mechanism are closed when invoking another program. </p>
 </dd>
<dt>- <code>exit</code><i>n</i> ]</dt>
<dd> <p> Causes the shell to exit with the exit status specified by <i>n</i>. The value will be the least significant 8 bits of the specified status. If <i>n</i> is omitted, then the exit status is that of the last command executed. An end-of-file will also cause the shell to exit except for a shell which has the <code>ignoreeof</code> option (see <code>set</code> below) turned on. </p>
 </dd>
<dt>-- <code>export</code><code>-p</code> ] <i>name</i><code>=</code><i>value</i>] ] ...</dt>
<dd> <p> If <i>name</i> is not given, the names and values of each variable with the export attribute are printed with the values quoted in a manner that allows them to be re-input. The <code>export</code> command is the same as <code>typeset -x</code> except that if you use <code>export</code> within a function, no local variable is created. The <code>-p</code> option causes the word <code>export</code> to be inserted before each one. Otherwise, the given <i>name</i>s are marked for automatic export to the <i>environment</i> of subsequently-executed commands. </p>
 </dd>
<dt><code>false</code></dt>
<dd> <p> Does nothing, and exits 1. Used with <code>until</code> for infinite loops. </p>
 </dd>
<dt><code>fg</code><i>job</i>... ]</dt>
<dd> <p> This command is only on systems that support job control. Each <i>job</i> specified is brought to the foreground and waited for in the specified order. Otherwise, the current job is brought into the foreground. See <i>Jobs</i> for a description of the format of <i>job</i>. </p>
 </dd>
<dt><code>getconf</code><i>name</i><i>pathname</i> ] ]</dt>
<dd> <p> Prints the current value of the configuration parameter given by <i>name</i>. The configuration parameters are defined by the IEEE POSIX 1003.1 and IEEE POSIX 1003.2 standards. (See <i>pathconf</i>(2) and <i>sysconf</i>(2).) The <i>pathname</i> argument is required for parameters whose value depends on the location in the file system. If no arguments are given, <code>getconf</code> prints the names and values of the current configuration parameters. The pathname <code>/</code> is used for each of the parameters that requires <i>pathname</i>. </p>
 </dd>
<dt><code>getopts</code><code>&nbsp;<wbr>-a</code><i>name</i> ] <i>optstring vname</i><i>arg</i> ... ]</dt>
<dd> <p> Checks <i>arg</i> for legal options. If <i>arg</i> is omitted, the positional parameters are used. An option argument begins with a <code>+</code> or a <code>-</code>. An option not beginning with <code>+</code> or <code>-</code> or the argument <code>--</code> ends the options. Options beginning with <code>+</code> are only recognized when <i>optstring</i> begins with a <code>+</code>. <i>optstring</i> contains the letters that <code>getopts</code> recognizes. If a letter is followed by a <code>:</code>, that option is expected to have an argument. The options can be separated from the argument by blanks. The option <code>-?</code> causes <code>getopts</code> to generate a usage message on standard error. The <code>-a</code> argument can be used to specify the name to use for the usage message, which defaults to <code>$0</code>. </p>
<p> <code>getopts</code> places the next option letter it finds inside variable <i>vname</i> each time it is invoked. The option letter will be prepended with a <code>+</code> when <i>arg</i> begins with a <code>+</code>. The index of the next <i>arg</i> is stored in <font SIZE="-1"><code>OPTIND</code>. </font> The option argument, if any, gets stored in <font SIZE="-1"><code>OPTARG</code>. </font> </p>
<p> A leading <code>:</code> in <i>optstring</i> causes <code>getopts</code> to store the letter of an invalid option in <font SIZE="-1"><code>OPTARG</code>, </font> and to set <i>vname</i> to <code>?</code> for an unknown option and to <code>:</code> when a required option argument is missing. Otherwise, <code>getopts</code> prints an error message. The exit status is non-zero when there are no more options. </p>
<p> There is no way to specify any of the options <code>:</code>, <code>+</code>, <code>-</code>, <code>?</code>, <code>[</code>, and <code>]</code>. The option <code>#</code> can only be specified as the first option. </p>
 </dd>
<dd> <p> <code>hist</code> <code>-e</code> <i>ename</i> &nbsp;<wbr>] <code>-nlr</code> ] <i>first</i> <i>last</i> ] ] </p>
 </dd>
<dt><code>hist -s </code><i>old</i><code>=</code><i>new</i> ] <i>command</i> ]</dt>
<dd> <p> In the first form, a range of commands from <i>first</i> to <i>last</i> is selected from the last <font SIZE="-1"><code>HISTSIZE</code> </font> commands that were typed at the terminal. The arguments <i>first</i> and <i>last</i> may be specified as a number or as a string. A string is used to locate the most recent command starting with the given string. A negative number is used as an offset to the current command number. If the <code>-l</code> option is selected, the commands are listed on standard output. Otherwise, the editor program <i>ename</i> is invoked on a file containing these keyboard commands. If <i>ename</i> is not supplied, then the value of the variable <font SIZE="-1"><code>HISTEDIT</code> </font> is used. If <font SIZE="-1"><code>HISTEDIT</code> </font> is not set, then <font SIZE="-1"><code>FCEDIT</code> </font> (default <code>/bin/ed</code>) is used as the editor. When editing is complete, the edited command(s) is executed if the changes have been saved. If <i>last</i> is not specified, then it will be set to <i>first</i>. If <i>first</i> is not specified, the default is the previous command for editing and -16 for listing. The option <code>-r</code> reverses the order of the commands and the option <code>-n</code> suppresses command numbers when listing. In the second form, <i>command</i> is interpreted as <i>first</i> described above and defaults to the last command executed. The resulting command is executed after the optional substitution <i>old</i><code>=</code><i>new</i> is performed. </p>
 </dd>
<dt><code>jobs</code><code>-lnp</code> ] <i>job</i> ... ]</dt>
<dd> <p> Lists information about each given job; or all active jobs if <i>job</i> is omitted. The <code>-l</code> option lists process ids in addition to the normal information. The <code>-n</code> option only displays jobs that have stopped or exited since last notified. The <code>-p</code> option causes only the process group to be listed. See <i>Jobs</i> for a description of the format of <i>job</i>. </p>
 </dd>
<dd> <p> <code>kill</code> <code>-s</code> <i>signame</i> ] <i>job</i> ... </p>
 </dd>
<dd> <p> <code>kill</code> <code>-n</code> <i>signum</i> ] <i>job</i> ... </p>
 </dd>
<dt><code>kill</code><code>-Ll</code><i>sig</i> ... ]</dt>
<dd> <p> Sends either the TERM (terminate) signal or the specified signal to the specified jobs or processes. Signals are either given by number with the <code>-n</code> option or by name with the <code>-s</code> option (as given in <code>&lt;signal.h&gt;</code>, stripped of the prefix ``SIG&#8217;&#8216; with the exception that SIGCLD is named CHLD). For backward compatibility, the <code>n</code> and <code>s</code> can be omitted and the number or name placed immediately after the <code>-</code>. If the signal being sent is TERM (terminate) or HUP (hangup), then the job or process will be sent a CONT (continue) signal if it is stopped. The argument <i>job</i> can be the process id of a process that is not a member of one of the active jobs. See <i>Jobs</i> for a description of the format of <i>job</i>. In the third form, <code>kill -l</code>, or <code>kill -L</code>, if <i>sig</i> is not specified, the signal names are listed. The <code>-l</code> option list only the signal names. <code>-L</code> options lists each signal name and corresponding number. Otherwise, for each <i>sig</i> that is a name, the corresponding signal number is listed. For each <i>sig</i> that is a number, the signal name corresponding to the least significant 8 bits of <i>sig</i> is listed. </p>
 </dd>
<dt><code>let</code><i>arg</i> ...</dt>
<dd> <p> Each <i>arg</i> is a separate <i>arithmetic expression</i> to be evaluated. <code>let</code> only recognizes octal constants starting with <code>0</code> when the <code>set</code> option <code>letoctal</code> is on. See <i>Arithmetic Evaluation</i> above, for a description of arithmetic expression evaluation. </p>
<p> The exit status is 0 if the value of the last expression is non-zero, and 1 otherwise. </p>
 </dd>
<dt>- <code>newgrp</code><i>arg</i> ... ]</dt>
<dd> <p> Equivalent to <code>exec /bin/newgrp</code><i> arg</i> .... </p>
 </dd>
<dt><code>print</code><code>-CRenprsv</code> ] <code>-u</code><i>unit</i>] <code>-f</code><i>format</i> ] <i>arg</i> ... ]</dt>
<dd> <p> With no options or with option <code>-</code> or <code>--</code>, each <i>arg</i> is printed on standard output. The <code>-f</code> option causes the arguments to be printed as described by <code>printf</code>. In this case, any <code>e</code>, <code>n</code>, <code>r</code>, <code>R</code> options are ignored. Otherwise, unless the <code>-C</code>, <code>-R</code>, <code>-r</code>, or <code>-v</code> are specified, the following escape conventions will be applied: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>\a</code></dt>
<dd> <p> The alert character (ascii <code>07</code>). </p>
 </dd>
<dt><code>\b</code></dt>
<dd> <p> The backspace character (ascii <code>010</code>). </p>
 </dd>
<dt><code>\c</code></dt>
<dd> <p> Causes <code>print</code> to end without processing more arguments and not adding a new-line. </p>
 </dd>
<dt><code>\f</code></dt>
<dd> <p> The formfeed character (ascii <code>014</code>). </p>
 </dd>
<dt><code>\n</code></dt>
<dd> <p> The new-line character (ascii <code>012</code>). </p>
 </dd>
<dt><code>\r</code></dt>
<dd> <p> The carriage return character (ascii <code>015</code>). </p>
 </dd>
<dt><code>\t</code></dt>
<dd> <p> The tab character (ascii <code>011</code>). </p>
 </dd>
<dt><code>\v</code></dt>
<dd> <p> The vertical tab character (ascii <code>013</code>). </p>
 </dd>
<dt><code>\E</code></dt>
<dd> <p> The escape character (ascii <code>033</code>). </p>
 </dd>
<dt><code>\\</code></dt>
<dd> <p> The backslash character \. </p>
 </dd>
<dt><code>\0</code><i>x</i></dt>
<dd> <p> The character defined by the 1, 2, or 3-digit octal string given by <i>x</i>. </p>
 </dd></dl>
<p> The <code>-R</code> option will print all subsequent arguments and options other than <code>-n</code>. The <code>-e</code> causes the above escape conventions to be applied. This is the default behavior. It reverses the effect of an earlier <code>-r</code>. The <code>-p</code> option causes the arguments to be written onto the pipe of the process spawned with <code>|&amp;</code> instead of standard output. The <code>-v</code> option treats each <i>arg</i> as a variable name and writes the value in the <code>printf</code> <code>%B</code> format. The <code>-C</code> option treats each <i>arg</i> as a variable name and writes the value in the <code>printf</code> <code>%#B</code> format. The <code>-s</code> option causes the arguments to be written onto the history file instead of standard output. The <code>-u</code> option can be used to specify a one digit file descriptor unit number <i>unit</i> on which the output will be placed. The default is 1. If the option <code>-n</code> is used, no <code>new-line</code> is added to the output. </dl>
 </p>
<dt><code>printf</code><i>format</i><i>arg</i> ... ]</dt>
<dd> <p> The arguments <i>arg</i> are printed on standard output in accordance with the ANSI-C formatting rules associated with the format string <i>format</i>. If the number of arguments exceeds the number of format specifications, the <code>format</code> string is reused to format remaining arguments. The following extensions can also be used: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>%b</code></dt>
<dd> <p> A <code>%b</code> format can be used instead of <code>%s</code> to cause escape sequences in the corresponding <i>arg</i> to be expanded as described in <code>print.</code> </p>
 </dd>
<dt><code>%B</code></dt>
<dd> <p> A <code>%B</code> option causes each of the arguments to be treated as variable names and the binary value of variable will be printed. The alternate flag <code>#</code> causes a compound variable to be output on a single line. This is most useful for compound variables and variables whose attribute is <code>-b</code>. </p>
 </dd>
<dt><code>%H</code></dt>
<dd> <p> A <code>%H</code> format can be used instead of <code>%s</code> to cause characters in <i>arg</i> that are special in HTML and XML to be output as their entity name. The alternate flag <code>#</code> formats the output for use as a URI. </p>
 </dd>
<dt><code>%P</code></dt>
<dd> <p> A <code>%P</code> format can be used instead of <code>%s</code> to cause <i>arg</i> to be interpreted as an extended regular expression and be printed as a shell pattern. </p>
 </dd>
<dt><code>%R</code></dt>
<dd> <p> A <code>%R</code> format can be used instead of <code>%s</code> to cause <i>arg</i> to be interpreted as a shell pattern and to be printed as an extended regular expression. </p>
 </dd>
<dt><code>%q</code></dt>
<dd> <p> A <code>%q</code> format can be used instead of <code>%s</code> to cause the resulting string to be quoted in a manner than can be reinput to the shell. When <code>q</code> is preceded by the alternative format specifier, <code>#</code>, the string is quoted in manner suitable as a field in a <code>.csv</code> format file. </p>
 </dd>
<dt><code>%(</code><i>date-format</i><code>)T</code></dt>
<dd> <p> A <code>%(</code><i>date-format</i><code>)T</code> format can be use to treat an argument as a date/time string and to format the date/time according to the <i>date-format</i> as defined for the <code><a href="/docs/linux/man/1-date/">date</a></code>(1) command. </p>
 </dd>
<dt><code>%Z</code></dt>
<dd> <p> A <code>%Z</code> format will output a byte whose value is 0. </p>
 </dd>
<dt><code>%d</code></dt>
<dd> <p> The precision field of the <code>%d</code> format can be followed by a <code>.</code> and the output base. In this case, the <code>#</code> flag character causes <i>base</i><code>#</code> to be prepended. </p>
 </dd>
<dt><code>#</code></dt>
<dd> <p> The <code>#</code> flag, when used with the <code>%d</code> format without an output base, displays the output in powers of 1000 indicated by one of the following suffixes: <code>k M G T P E</code>, and when used with the <code>%i</code> format displays the output in powers of 1024 indicated by one of the following suffixes: <code>Ki Mi Gi Ti Pi Ei</code>. </p>
 </dd>
<dt><code>=</code></dt>
<dd> <p> The <code>=</code> flag centers the output within the specified field width. </p>
 </dd>
<dt><code>L</code></dt>
<dd> <p> The <code>L</code> flag, when used with the <code>%c</code> or <code>%s</code> formats, treats precision as character width instead of byte count. </p>
 </dd>
<dt><code>,</code></dt>
<dd> <p> The <code>,</code> flag, when used with the <code>%d</code> or <code>%f</code> formats, separates groups of digits with the grouping delimiter (<code>,</code> on groups of 3 in the C locale.) </p>
 </dd></dl>
<dt><code>pwd</code><code>-LP</code> ]</dt>
<dd> <p> Outputs the value of the current working directory. The <code>-L</code> option is the default; it prints the logical name of the current directory. If the <code>-P</code> option is given, all symbolic links are resolved from the name. The last instance of <code>-L</code> or <code>-P</code> on the command line determines which method is used. </p>
 </dd>
<dt><code>read</code><code>-ACSprsv</code> ] <code>-d</code><i>delim</i>] <code>-n</code><i>n</i>] <code>-N</code><i>n</i>] <code>-t</code><i>timeout</i>] <code>-u</code><i>unit</i>] <i>vname</i><code>?</code><i>prompt</i> ] <i>vname</i> ... ]</dt>
<dd> <p> The shell input mechanism. One line is read and is broken up into fields using the characters in <font SIZE="-1"><code>IFS</code></font> as separators. The escape character, <code>\</code>, is used to remove any special meaning for the next character and for line continuation. The <code>-d</code> option causes the read to continue to the first character of <i>delim</i> rather than new-line. The <code>-n</code> option causes at most <i>n</i> bytes to read rather a full line but will return when reading from a slow device as soon as any characters have been read. The <code>-N</code> option causes exactly <i>n</i> to be read unless an end-of-file has been encountered or the read times out because of the <code>-t</code> option. In raw mode, <code>-r,</code> the <code>\</code> character is not treated specially. The first field is assigned to the first <i>vname</i>, the second field to the second <i>vname</i>, etc., with leftover fields assigned to the last <i>vname</i>. When <i>vname</i> has the binary attribute and <code>-n</code> or <code>-N</code> is specified, the bytes that are read are stored directly into the variable. If the <code>-v</code> is specified, then the value of the first <i>vname</i> will be used as a default value when reading from a terminal device. The <code>-A</code> option causes the variable <i>vname</i> to be unset and each field that is read to be stored in successive elements of the indexed array <i>vname.</i> The <code>-C</code> option causes the variable <i>vname</i> to be read as a compound variable. Blanks will be ignored when finding the beginning open parenthesis. The -S option causes the line to be treated like a record in a <code>.csv</code> format file so that double quotes can be used to allow the delimiter character and the new-line character to appear within a field. The <code>-p</code> option causes the input line to be taken from the input pipe of a process spawned by the shell using <code>|&amp;</code>. If the <code>-s</code> option is present, the input will be saved as a command in the history file. The option <code>-u</code> can be used to specify a one digit file descriptor unit <i>unit</i> to read from. The file descriptor can be opened with the <code>exec</code> special built-in command. The default value of unit <i>n</i> is 0. The option <code>-t</code> is used to specify a timeout in seconds when reading from a terminal or pipe. If <i>vname</i> is omitted, then <font SIZE="-1"><code>REPLY</code> </font> is used as the default <i>vname</i>. An end-of-file with the <code>-p</code> option causes cleanup for this process so that another can be spawned. If the first argument contains a <code>?</code>, the remainder of this word is used as a <i>prompt</i> on standard error when the shell is interactive. The exit status is 0 unless an end-of-file is encountered or <code>read</code> has timed out. </p>
 </dd>
<dt>-- <code>readonly</code><code>-p</code> ] <i>vname</i><code>=</code><i>value</i>] ] ...</dt>
<dd> <p> If <i>vname</i> is not given, the names and values of each variable with the readonly attribute is printed with the values quoted in a manner that allows them to be re-inputted. The <code>-p</code> option causes the word <code>readonly</code> to be inserted before each one. Otherwise, the given <i>vname</i>s are marked readonly and these names cannot be changed by subsequent assignment. When defining a type, if the value of a readonly sub-variable is not defined the value is required when creating each instance. </p>
 </dd>
<dt>- <code>return</code><i>n</i> ]</dt>
<dd> <p> Causes a shell <i>function</i> or <code>.</code> script to return to the invoking script with the exit status specified by <i>n</i>. The value will be the least significant 8 bits of the specified status. If <i>n</i> is omitted, then the return status is that of the last command executed. If <code>return</code> is invoked while not in a <i>function</i> or a <code>.</code> script, then it behaves the same as <code>exit</code>. </p>
 </dd>
<dt>- <code>set</code><code>&plusmn;BCGabefhkmnoprstuvx</code> ] <code>&plusmn;o</code><i>option</i> ] ] ... <code>&plusmn;A</code><i>vname</i> ] <i>arg</i> ... ]</dt>
<dd> <p> The options for this command have meaning as follows: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>-A</code></dt>
<dd> <p> Array assignment. Unset the variable <i>vname</i> and assign values sequentially from the <i>arg</i> list. If <code>+A</code> is used, the variable <i>vname</i> is not unset first. </p>
 </dd>
<dt><code>-B</code></dt>
<dd> <p> Enable brace pattern field generation. This is the default behavior. </p>
 </dd>
<dt><code>-B</code></dt>
<dd> <p> Enable brace group expansion. On by default. </p>
 </dd>
<dt><code>-C</code></dt>
<dd> <p> Prevents redirection <code>&gt;</code> from truncating existing files. Files that are created are opened with the O_EXCL mode. Requires <code>&gt;|</code> to truncate a file when turned on. </p>
 </dd>
<dt><code>-G</code></dt>
<dd> <p> Causes the pattern <code>**</code> by itself to match files and zero or more directories and sub-directories when used for file name generation. If followed by a <code>/</code> only directories and sub-directories are matched. </p>
 </dd>
<dt><code>-a</code></dt>
<dd> <p> All subsequent variables that are defined are automatically exported. </p>
 </dd>
<dt><code>-b</code></dt>
<dd> <p> Prints job completion messages as soon as a background job changes state rather than waiting for the next prompt. </p>
 </dd>
<dt><code>-e</code></dt>
<dd> <p> Unless contained in a <code>||</code> or <code>&amp;&amp;</code> command, or the command following an <code>if</code> <code>while</code> or <code>until</code> command or in the pipeline following <code>!</code>, if a command has a non-zero exit status, execute the <font SIZE="-1"><code>ERR</code> </font> trap, if set, and exit. This mode is disabled while reading profiles. </p>
 </dd>
<dt><code>-f</code></dt>
<dd> <p> Disables file name generation. </p>
 </dd>
<dt><code>-h</code></dt>
<dd> <p> Each command becomes a tracked alias when first encountered. </p>
 </dd>
<dt><code>-k</code></dt>
<dd> <p> (Obsolete). All variable assignment arguments are placed in the environment for a command, not just those that precede the command name. </p>
 </dd>
<dt><code>-m</code></dt>
<dd> <p> Background jobs will run in a separate process group and a line will print upon completion. The exit status of background jobs is reported in a completion message. On systems with job control, this option is turned on automatically for interactive shells. </p>
 </dd>
<dt><code>-n</code></dt>
<dd> <p> Read commands and check them for syntax errors, but do not execute them. Ignored for interactive shells. </p>
 </dd>
<dt><code>-o</code></dt>
<dd> <p> The following argument can be one of the following option names: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>allexport</code></dt>
<dd> <p> Same as <code>-a</code>. </p>
 </dd>
<dt><code>errexit</code></dt>
<dd> <p> Same as <code>-e</code>. </p>
 </dd>
<dt><code>bgnice</code></dt>
<dd> <p> All background jobs are run at a lower priority. This is the default mode. </p>
 </dd>
<dt><code>braceexpand</code></dt>
<dd> <p> Same as <code>-B</code>. </p>
 </dd>
<dt><code>emacs</code></dt>
<dd> <p> Puts you in an <i>emacs</i> style in-line editor for command entry. </p>
 </dd>
<dt><code>globstar</code></dt>
<dd> <p> Same as <code>-G</code>. </p>
 </dd>
<dt><code>gmacs</code></dt>
<dd> <p> Puts you in a <i>gmacs</i> style in-line editor for command entry. </p>
 </dd>
<dt><code>ignoreeof</code></dt>
<dd> <p> The shell will not exit on end-of-file. The command <code>exit</code> must be used. </p>
 </dd>
<dt><code>keyword</code></dt>
<dd> <p> Same as <code>-k</code>. </p>
 </dd>
<dt><code>letoctal</code></dt>
<dd> <p> The <code>let</code> command allows octal constants starting with <code>0</code>. </p>
 </dd>
<dt><code>markdirs</code></dt>
<dd> <p> All directory names resulting from file name generation have a trailing <code>/</code> appended. </p>
 </dd>
<dt><code>monitor</code></dt>
<dd> <p> Same as <code>-m</code>. </p>
 </dd>
<dt><code>multiline</code></dt>
<dd> <p> The built-in editors will use multiple lines on the screen for lines that are longer than the width of the screen. This may not work for all terminals. </p>
 </dd>
<dt><code>noclobber</code></dt>
<dd> <p> Same as <code>-C</code>. </p>
 </dd>
<dt><code>noexec</code></dt>
<dd> <p> Same as <code>-n</code>. </p>
 </dd>
<dt><code>noglob</code></dt>
<dd> <p> Same as <code>-f</code>. </p>
 </dd>
<dt><code>nolog</code></dt>
<dd> <p> Do not save function definitions in the history file. </p>
 </dd>
<dt><code>notify</code></dt>
<dd> <p> Same as <code>-b</code>. </p>
 </dd>
<dt><code>nounset</code></dt>
<dd> <p> Same as <code>-u</code>. </p>
 </dd>
<dt><code>pipefail</code></dt>
<dd> <p> A pipeline will not complete until all components of the pipeline have completed, and the return value will be the value of the last non-zero command to fail or zero if no command has failed. </p>
 </dd>
<dt><code>showme</code></dt>
<dd> <p> When enabled, simple commands or pipelines preceded by a semicolon (<code>;</code>) will be displayed as if the <code>xtrace</code> option were enabled but will not be executed. Otherwise, the leading <code>;</code> will be ignored. </p>
 </dd>
<dt><code>privileged</code></dt>
<dd> <p> Same as <code>-p</code>. </p>
 </dd>
<dt><code>verbose</code></dt>
<dd> <p> Same as <code>-v</code>. </p>
 </dd>
<dt><code>trackall</code></dt>
<dd> <p> Same as <code>-h</code>. </p>
 </dd>
<dt><code>vi</code></dt>
<dd> <p> Puts you in insert mode of a <i>vi</i> style in-line editor until you hit the escape character <code>033</code>. This puts you in control mode. A return sends the line. </p>
 </dd>
<dt><code>viraw</code></dt>
<dd> <p> Each character is processed as it is typed in <i>vi</i> mode. </p>
 </dd>
<dt><code>xtrace</code></dt>
<dd> <p> Same as <code>-x</code>. </p>
 </dd></dl>
<p> If no option name is supplied, then the current option settings are printed. </dl>
 </p>
<dt><code>-p</code></dt>
<dd> <p> Disables processing of the <font SIZE="-1"><code>$HOME</code></font><code>/.profile</code> file and uses the file <code>/etc/suid_profile</code> instead of the <font SIZE="-1"><code>ENV</code> </font> file. This mode is on whenever the effective uid (gid) is not equal to the real uid (gid). Turning this off causes the effective uid and gid to be set to the real uid and gid. </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> Enables the restricted shell. This option cannot be unset once set. </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> Sort the positional parameters lexicographically. </p>
 </dd>
<dt><code>-t</code></dt>
<dd> <p> (Obsolete). Exit after reading and executing one command. </p>
 </dd>
<dt><code>-u</code></dt>
<dd> <p> Treat unset parameters as an error when substituting. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Print shell input lines as they are read. </p>
 </dd>
<dt><code>-x</code></dt>
<dd> <p> Print commands and their arguments as they are executed. </p>
 </dd>
<dt><code>--</code></dt>
<dd> <p> Do not change any of the options; useful in setting <code>$1</code> to a value beginning with <code>-</code>. If no arguments follow this option then the positional parameters are unset. </p>
 </dd></dl>
<p> As an obsolete feature, if the first <i>arg</i> is <code>-</code> then the <code>-x</code> and <code>-v</code> options are turned off and the next <i>arg</i> is treated as the first argument. Using <code>+</code> rather than <code>-</code> causes these options to be turned off. These options can also be used upon invocation of the shell. The current set of options may be found in <code>$-</code>. Unless <code>-A</code> is specified, the remaining arguments are positional parameters and are assigned, in order, to <code>$1</code> <code>$2</code> .... If no arguments are given, then the names and values of all variables are printed on the standard output. </dl>
 </p>
<dt>- <code>shift</code><i>n</i> ]</dt>
<dd> <p> <br />
 The positional parameters from <code>$</code><i>n</i><code>+1</code> ... are renamed <code>$1</code> ... , default <i>n</i> is 1. The parameter <i>n</i> can be any arithmetic expression that evaluates to a non-negative number less than or equal to <code>$#</code>. </p>
 </dd>
<dt><code>sleep</code><i>seconds</i></dt>
<dd> <p> Suspends execution for the number of decimal seconds or fractions of a second given by <i>seconds</i>. </p>
 </dd>
<dt>- <code>trap</code><code>-p</code> ] <i>action</i> ] <i>sig</i> ] ...</dt>
<dd> <p> The <code>-p</code> option causes the trap action associated with each trap as specified by the arguments to be printed with appropriate quoting. Otherwise, <i>action</i> will be processed as if it were an argument to <code>eval</code> when the shell receives signal(s) <i>sig</i>. Each <i>sig</i> can be given as a number or as the name of the signal. Trap commands are executed in order of signal number. Any attempt to set a trap on a signal that was ignored on entry to the current shell is ineffective. If <i>action</i> is omitted and the first <i>sig</i> is a number, or if <i>action</i> is <code>-</code>, then the trap(s) for each <i>sig</i> are reset to their original values. If <i>action</i> is the null string then this signal is ignored by the shell and by the commands it invokes. If <i>sig</i> is <font SIZE="-1"><code>ERR</code> </font> then <i>action</i> will be executed whenever a command has a non-zero exit status. If <i>sig</i> is <font SIZE="-1"><code>DEBUG</code> </font> then <i>action</i> will be executed before each command. The variable <code>.sh.command</code> will contain the contents of the current command line when <i>action</i> is running. If the exit status of the trap is <code>2</code> the command will not be executed. If the exit status of the trap is <code>255</code> and inside a function or a dot script, the function or dot script will return. If <i>sig</i> is <code>0</code> or <font SIZE="-1"><code>EXIT</code> </font> and the <code>trap</code> statement is executed inside the body of a function defined with the <code>function</code> <i>name</i> syntax, then the command <i>action</i> is executed after the function completes. If <i>sig</i> is <code>0</code> or <font SIZE="-1"><code>EXIT</code> </font> for a <code>trap</code> set outside any function then the command <i>action</i> is executed on exit from the shell. If <i>sig</i> is <font SIZE="-1"><code>KEYBD</code>, </font> then <i>action</i> will be executed whenever a key is read while in <code>emacs</code>, <code>gmacs</code>, or <code>vi</code> mode. The <code>trap</code> command with no arguments prints a list of commands associated with each signal number. </p>
 </dd></dl>
<p> An <code>exit</code> or <code>return</code> without an argument in a trap action will preserve the exit status of the command that invoked the trap. </p>
<dl>
<dt><code>true</code></dt>
<dd> <p> Does nothing, and exits 0. Used with <code>while</code> for infinite loops. </p>
 </dd>
<dt>-- <code>typeset</code><code>&plusmn;ACHSfblmnprtux</code> ] <code>&plusmn;EFLRXZi</code><i>n</i>] ] <code>+-M </code><i>mapname</i> ] ] <code>-T </code><i>tname</i>=(<i>assign_list</i>) ] ] <code>-h </code><i>str</i> ] <code>-a</code><i>type</i>] ] <i>vname</i><code>=</code><i>value</i> ] ] ...</dt>
<dd> <p> Sets attributes and values for shell variables and functions. When invoked inside a function defined with the <code>function</code> <i>name</i> syntax, a new instance of the variable <i>vname</i> is created, and the variable&#8217;s value and type are restored when the function completes. The following list of attributes may be specified: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>-A</code></dt>
<dd> <p> Declares <i>vname</i> to be an associative array. Subscripts are strings rather than arithmetic expressions. </p>
 </dd>
<dt><code>-C</code></dt>
<dd> <p> causes each <i>vname</i> to be a compound variable. <i>value</i> names a compound variable it is copied into <i>vname</i>. Otherwise, it unsets each <i>vname</i>. </p>
 </dd>
<dt><code>-a</code></dt>
<dd> <p> Declares <i>vname</i> to be an indexed array. If <i>type</i> is specified, it must be the name of an enumeration type created with the <code>enum</code> command and it allows enumeration constants to be used as subscripts. </p>
 </dd>
<dt><code>-E</code></dt>
<dd> <p> Declares <i>vname</i> to be a double precision floating point number. If <i>n</i> is non-zero, it defines the number of significant figures that are used when expanding <i>vname</i>. Otherwise, ten significant figures will be used. </p>
 </dd>
<dt><code>-F</code></dt>
<dd> <p> Declares <i>vname</i> to be a double precision floating point number. If <i>n</i> is non-zero, it defines the number of places after the decimal point that are used when expanding <i>vname</i>. Otherwise ten places after the decimal point will be used. </p>
 </dd>
<dt><code>-H</code></dt>
<dd> <p> This option provides UNIX to host-name file mapping on non-UNIX machines. </p>
 </dd>
<dt><code>-L</code></dt>
<dd> <p> Left justify and remove leading blanks from <i>value</i>. If <i>n</i> is non-zero, it defines the width of the field, otherwise it is determined by the width of the value of first assignment. When the variable is assigned to, it is filled on the right with blanks or truncated, if necessary, to fit into the field. The <code>-R</code> option is turned off. </p>
 </dd>
<dt><code>-M</code></dt>
<dd> <p> Use the character mapping <i>mapping</i> defined by <i><a href="/docs/linux/man/3-wctrans/">wctrans</a></i>(3). such as <code>tolower</code> and <code>toupper</code> when assigning a value to each of the specified operands. When <i>mapping</i> is specified and there are not operands, all variables that use this mapping are written to standard output. When <i>mapping</i> is omitted and there are no operands, all mapped variables are written to standard output. </p>
 </dd>
<dt><code>-R</code></dt>
<dd> <p> Right justify and fill with leading blanks. If <i>n</i> is non-zero, it defines the width of the field, otherwise it is determined by the width of the value of first assignment. The field is left filled with blanks or truncated from the end if the variable is reassigned. The <code>-L</code> option is turned off. </p>
 </dd>
<dt><code>-S</code></dt>
<dd> <p> When used within the <i>assign_list</i> of a type definition, it causes the specified sub-variable to be shared by all instances of the type. When used inside a function defined with the <code>function</code> reserved word, the specified variables will have <i>function static</i> scope. Otherwise, the variable is unset prior to processing the assignment list. </p>
 </dd>
<dt><code>-T</code></dt>
<dd> <p> If followed by <i>tname</i>, it creates a type named by <i>tname</i> using the compound assignment <i>assign_list</i> to <i>tname</i>. Otherwise, it writes all the type definitions to standard output. </p>
 </dd>
<dt><code>-X</code></dt>
<dd> <p> Declares <i>vname</i> to be a double precision floating point number and expands using the <code>%a</code> format of ISO-C99. If <i>n</i> is non-zero, it defines the number of hex digits after the radix point that is used when expanding <i>vname</i>. The default is 10. </p>
 </dd>
<dt><code>-Z</code></dt>
<dd> <p> Right justify and fill with leading zeros if the first non-blank character is a digit and the <code>-L</code> option has not been set. Remove leading zeros if the <code>-L</code> option is also set. If <i>n</i> is non-zero, it defines the width of the field, otherwise it is determined by the width of the value of first assignment. </p>
 </dd>
<dt><code>-f</code></dt>
<dd> <p> The names refer to function names rather than variable names. No assignments can be made and the only other valid options are <code>-S</code>, <code>-t</code>, <code>-u</code> and <code>-x</code>. The -S can be used with discipline functions defined in a type to indicate that the function is static. For a static function, the same method will be used by all instances of that type no matter which instance references it. In addition, it can only use value of variables from the original type definition. These discipline functions cannot be redefined in any type instance. The <code>-t</code> option turns on execution tracing for this function. The <code>-u</code> option causes this function to be marked undefined. The <font SIZE="-1"><code>FPATH</code> </font> variable will be searched to find the function definition when the function is referenced. If no options other than <code>-f</code> is specified, then the function definition will be displayed on standard output. If <code>+f</code> is specified, then a line containing the function name followed by a shell comment containing the line number and path name of the file where this function was defined, if any, is displayed. The exit status can be used to determine whether the function is defined so that <code>typeset -f .sh.math.</code><i>name</i> will return 0 when math function <i>name</i> is defined and non-zero otherwise. </p>
 </dd>
<dt><code>-b</code></dt>
<dd> <p> The variable can hold any number of bytes of data. The data can be text or binary. The value is represented by the base64 encoding of the data. If <code>-Z</code> is also specified, the size in bytes of the data in the buffer will be determined by the size associated with the <code>-Z</code>. If the base64 string assigned results in more data, it will be truncated. Otherwise, it will be filled with bytes whose value is zero. The <code>printf</code> format <code>%B</code> can be used to output the actual data in this buffer instead of the base64 encoding of the data. </p>
 </dd>
<dt><code>-h</code></dt>
<dd> <p> Used within type definitions to add information when generating information about the sub-variable on the man page. It is ignored when used outside of a type definition. When used with <code>-f</code> the information is associated with the corresponding discipline function. </p>
 </dd>
<dt><code>-i</code></dt>
<dd> <p> Declares <i>vname</i> to be represented internally as integer. The right hand side of an assignment is evaluated as an arithmetic expression when assigning to an integer. If <i>n</i> is non-zero, it defines the output arithmetic base, otherwise the output base will be ten. </p>
 </dd>
<dt><code>-l</code></dt>
<dd> <p> Used with <code>-i</code>, <code>-E</code> or <code>-F</code>, to indicate long integer, or long float. Otherwise, all upper-case characters are converted to lower-case. The upper-case option, <code>-u</code>, is turned off. Equivalent to <code>-M tolower .</code> </p>
 </dd>
<dt><code>-m</code></dt>
<dd> <p> moves or renames the variable. The value is the name of a variable whose value will be moved to <i>vname</i>. The original variable will be unset. Cannot be used with any other options. </p>
 </dd>
<dt><code>-n</code></dt>
<dd> <p> Declares <i>vname</i> to be a reference to the variable whose name is defined by the value of variable <i>vname</i>. This is usually used to reference a variable inside a function whose name has been passed as an argument. Cannot be used with any other options. </p>
 </dd>
<dt><code>-p</code></dt>
<dd> <p> The name, attributes and values for the given <i>vname</i>s are written on standard output in a form that can be used as shell input. If <code>+p</code> is specified, then the values are not displayed. </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> The given <i>vname</i>s are marked readonly and these names cannot be changed by subsequent assignment. </p>
 </dd>
<dt><code>-t</code></dt>
<dd> <p> Tags the variables. Tags are user definable and have no special meaning to the shell. </p>
 </dd>
<dt><code>-u</code></dt>
<dd> <p> When given along with <code>-i</code>, specifies unsigned integer. Otherwise, all lower-case characters are converted to upper-case. The lower-case option, <code>-l</code>, is turned off. Equivalent to <code>-M toupper .</code> </p>
 </dd>
<dt><code>-x</code></dt>
<dd> <p> The given <i>vname</i>s are marked for automatic export to the <i>environment</i> of subsequently-executed commands. Variables whose names contain a <font SIZE="+2"><code>.</code></font> cannot be exported. </p>
 </dd></dl>
<p> The <code>-i</code> attribute cannot be specified along with <code>-R</code>, <code>-L</code>, <code>-Z</code>, or <code>-f</code>. </p>
<p> Using <code>+</code> rather than <code>-</code> causes these options to be turned off. If no <i>vname</i> arguments are given, a list of <i>vnames</i> (and optionally the <i>values</i>) of the <i>variables</i> is printed. (Using <code>+</code> rather than <code>-</code> keeps the values from being printed.) The <code>-p</code> option causes <code>typeset</code> followed by the option letters to be printed before each name rather than the names of the options. If any option other than <code>-p</code> is given, only those variables which have all of the given options are printed. Otherwise, the <i>vname</i>s and <i>attributes</i> of all <i>variables</i> that have attributes are printed. </dl>
 </p>
<dt><code>ulimit</code><code>-HSacdfmnpstv</code> ] <i>limit</i> ]</dt>
<dd> <p> Set or display a resource limit. The available resource limits are listed below. Many systems do not support one or more of these limits. The limit for a specified resource is set when <i>limit</i> is specified. The value of <i>limit</i> can be a number in the unit specified below with each resource, or the value <code>unlimited</code>. The <code>-H</code> and <code>-S</code> options specify whether the hard limit or the soft limit for the given resource is set. A hard limit cannot be increased once it is set. A soft limit can be increased up to the value of the hard limit. If neither the <code>H</code> nor <code>S</code> option is specified, the limit applies to both. The current resource limit is printed when <i>limit</i> is omitted. In this case, the soft limit is printed unless <code>H</code> is specified. When more than one resource is specified, then the limit name and unit is printed before the value. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>-a</code></dt>
<dd> <p> Lists all of the current resource limits. </p>
 </dd>
<dt><code>-c</code></dt>
<dd> <p> The number of 512-byte blocks on the size of core dumps. </p>
 </dd>
<dt><code>-d</code></dt>
<dd> <p> The number of K-bytes on the size of the data area. </p>
 </dd>
<dt><code>-f</code></dt>
<dd> <p> The number of 512-byte blocks on files that can be written by the current process or by child processes (files of any size may be read). </p>
 </dd>
<dt><code>-m</code></dt>
<dd> <p> The number of K-bytes on the size of physical memory. </p>
 </dd>
<dt><code>-n</code></dt>
<dd> <p> The number of file descriptors plus 1. </p>
 </dd>
<dt><code>-p</code></dt>
<dd> <p> The number of 512-byte blocks for pipe buffering. </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> The number of K-bytes on the size of the stack area. </p>
 </dd>
<dt><code>-t</code></dt>
<dd> <p> The number of CPU seconds to be used by each process. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> The number of K-bytes for virtual memory. </p>
 </dd></dl>
<p> If no option is given, <code>-f</code> is assumed. </dl>
 </p>
<dt><code>umask</code><code>-S</code> ] <i>mask</i> ]</dt>
<dd> <p> The user file-creation mask is set to <i>mask</i> (see <i><a href="/docs/linux/man/2-umask/">umask</a></i>(2)). <i>mask</i> can either be an octal number or a symbolic value as described in <i><a href="/docs/linux/man/1-chmod/">chmod</a></i>(1). If a symbolic value is given, the new umask value is the complement of the result of applying <i>mask</i> to the complement of the previous umask value. If <i>mask</i> is omitted, the current value of the mask is printed. The <code>-S</code> option causes the mode to be printed as a symbolic value. Otherwise, the mask is printed in octal. </p>
 </dd>
<dt>- <code>unalias</code><code>-a</code> ] <i>name</i> ...</dt>
<dd> <p> The aliases given by the list of <i>name</i>s are removed from the alias list. The <code>-a</code> option causes all the aliases to be unset. </p>
 </dd>
<dt>-<code>unset</code><code>-fnv</code> ] <i>vname</i> ...</dt>
<dd> <p> The variables given by the list of <i>vname</i>s are unassigned, i.e., except for sub-variables within a type, their values and attributes are erased. For sub-variables of a type, the values are reset to the default value from the type definition. Readonly variables cannot be unset. If the <code>-f</code> option is set, then the names refer to <i>function</i> names. If the <code>-v</code> option is set, then the names refer to <i>variable</i> names. The <code>-f</code> option overrides <code>-v</code>. If <code>-n</code> is set and <i>name</i> is a name reference, then <i>name</i> will be unset rather than the variable that it references. The default is equivalent to <code>-v</code>. Unsetting <font SIZE="-1"><code>LINENO</code>, </font> <font SIZE="-1"><code>MAILCHECK</code>, </font> <font SIZE="-1"><code>OPTARG</code>, </font> <font SIZE="-1"><code>OPTIND</code>, </font> <font SIZE="-1"><code>RANDOM</code>, </font> <font SIZE="-1"><code>SECONDS</code>, </font> <font SIZE="-1"><code>TMOUT</code>, </font> and <font SIZE="-1"><code>_</code> </font> removes their special meaning even if they are subsequently assigned to. </p>
 </dd>
<dt><code>wait</code><i>job</i> ... ]</dt>
<dd> <p> Wait for the specified <i>job</i> and report its termination status. If <i>job</i> is not given, then all currently active child processes are waited for. The exit status from this command is that of the last process waited for if <i>job</i> is specified; otherwise it is zero. See <i>Jobs</i> for a description of the format of <i>job</i>. </p>
 </dd>
<dt><code>whence</code><code>-afpv</code> ] <i>name</i> ...</dt>
<dd> <p> For each <i>name</i>, indicate how it would be interpreted if used as a command name. </p>
<p> The <code>-v</code> option produces a more verbose report. The <code>-f</code> option skips the search for functions. The <code>-p</code> option does a path search for <i>name</i> even if name is an alias, a function, or a reserved word. The <code>-p</code> option turns off the <code>-v</code> option. The <code>-a</code> option is similar to the <code>-v</code> option but causes all interpretations of the given name to be reported. </p>
 </dd></dl>
<h3>Invocation.</h3>
<p> If the shell is invoked by <i>exec</i>(2), and the first character of argument zero (<code>$0</code>) is <code>-</code>, then the shell is assumed to be a <i>login</i> shell and commands are read from <code>/etc/profile</code> and then from either <code>.profile</code> in the current directory or <font SIZE="-1"><code>$HOME</code></font><code>/.profile</code>, if either file exists. Next, for interactive shells, commands are read from the file named by performing parameter expansion, command substitution, and arithmetic substitution on the value of the environment variable <font SIZE="-1"><code>ENV</code> </font> if the file exists. If the <code>-s</code> option is not present and <i>arg</i> and a file by the name of <i>arg</i> exists, then it reads and executes this script. Otherwise, if the first <i>arg</i> does not contain a <code>/</code>, a path search is performed on the first <i>arg</i> to determine the name of the script to execute. The script <i>arg</i> must have execute permission and any <i>setuid</i> and <i>setgid</i> settings will be ignored. If the script is not found on the path, <i>arg</i> is processed as if it named a built-in command or function. Commands are then read as described below; the following options are interpreted by the shell when it is invoked: </p>
<dl>
<dt><code>-D</code></dt>
<dd> <p> Do not execute the script, but output the set of double quoted strings preceded by a <code>$</code>. These strings are needed for localization of the script to different locales. </p>
 </dd>
<dt><code>-E</code></dt>
<dd> <p> Reads the file named by the <code>ENV</code> variable or by <font SIZE="-1">$HOME</font>/<code>.</code>kshrc if not defined after the profiles. </p>
 </dd>
<dt><code>-c</code></dt>
<dd> <p> If the <code>-c</code> option is present, then commands are read from the first <i>arg</i>. Any remaining arguments become positional parameters starting at <code>0</code>. </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> If the <code>-s</code> option is present or if no arguments remain, then commands are read from the standard input. Shell output, except for the output of the <i>Special Commands</i> listed above, is written to file descriptor 2. </p>
 </dd>
<dt><code>-i</code></dt>
<dd> <p> If the <code>-i</code> option is present or if the shell input and error output are attached to a terminal (as told by <i>tcgetattr</i>(2)), then this shell is <i>interactive</i>. In this case <font SIZE="-1">TERM</font> is ignored (so that <code>kill 0</code> does not kill an interactive shell) and <font SIZE="-1">INTR</font> is caught and ignored (so that <code>wait</code> is ). In all cases, <font SIZE="-1">QUIT</font> is ignored by the shell. </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> If the <code>-r</code> option is present, the shell is a restricted shell. </p>
 </dd>
<dt><code>-D</code></dt>
<dd> <p> A list of all double quoted strings that are preceded by a <code>$</code> will be printed on standard output and the shell will exit. This set of strings will be subject to language translation when the locale is not C or POSIX. No commands will be executed. </p>
 </dd>
<dt><code>-P</code></dt>
<dd> <p> If <code>-P</code> or <code>-o profile</code> is present, the shell is a profile shell (see <i>pfexec</i>(1)). </p>
 </dd>
<dt><code>-R</code><i> filename</i></dt>
<dd> <p> The <code>-R</code> <i>filename</i> option is used to generate a cross reference database that can be used by a separate utility to find definitions and references for variables and commands. The filename argument specifies the generated database. A script file must be provided on the command line as well. </p>
 </dd></dl>
<p> The remaining options and arguments are described under the <code>set</code> command above. An optional <code>-</code> as the first argument is ignored. .SS Rksh Only. <i>Rksh</i> is used to set up login names and execution environments whose capabilities are more controlled than those of the standard shell. The actions of <code>rksh</code> are identical to those of <code>ksh</code>, except that the following are disallowed: </p>
<dl>
<dd> <p> Unsetting the restricted option. <br />
 changing directory (see <i><a href="/docs/linux/man/1-cd/">cd</a></i>(1)), <br />
 setting or unsetting the value or attributes of <font SIZE="-1"><code>SHELL</code>, </font> <font SIZE="-1"><code>ENV</code>, </font> <font SIZE="-1"><code>FPATH</code>, </font> or <font SIZE="-1"><code>PATH,</code> </font> <br />
 specifying path or command names containing <code>/</code>, <br />
 redirecting output (<code>&gt;</code>, <code>&gt;|</code>, <code>&lt;&gt;</code>, and <code>&gt;&gt;</code>). <br />
 adding or deleting built-in commands. <br />
 using <code>command -p</code> to invoke a command. </p>
 </dd></dl>
<p> The restrictions above are enforced after <code>.profile</code> and the <font SIZE="-1"><code>ENV</code> </font> files are interpreted. </p>
<p> When a command to be executed is found to be a shell procedure, .B rksh invokes <i>ksh</i> to execute it. Thus, it is possible to provide to the end-user shell procedures that have access to the full power of the standard shell, while imposing a limited menu of commands; this scheme assumes that the end-user does not have write and execute permissions in the same directory. </p>
<p> The net effect of these rules is that the writer of the <code>.profile</code> has complete control over user actions, by performing guaranteed setup actions and leaving the user in an appropriate directory (probably <i>not</i> the login directory). </p>
<p> The system administrator often sets up a directory of commands (e.g., <code>/usr/rbin</code>) that can be safely invoked by <code>rksh</code>.  </p>
<h2>EXIT STATUS</h2>
<p> Errors detected by the shell, such as syntax errors, cause the shell to return a non-zero exit status. If the shell is being used non-interactively, then execution of the shell file is abandoned unless the error occurs inside a subshell in which case the subshell is abandoned. Otherwise, the shell returns the exit status of the last command executed (see also the <code>exit</code> command above). Run time errors detected by the shell are reported by printing the command or function name and the error condition. If the line number that the error occurred on is greater than one, then the line number is also printed in square brackets (<code>[]</code>) after the command or function name.  </p>
<h2>FILES</h2>
<dl>
<dt><code>/etc/profile</code></dt>
<dd> <p> The system wide initialization file, executed for login shells. </p>
 </dd>
<dt><font SIZE="-1"><code>$HOME</code></font><code>/.</code>profile </dt>
<dd> <p> The personal initialization file, executed for login shells after /etc/profile. </p>
 </dd>
<dt><font SIZE="-1">$HOME</font>/<code>.</code>.kshrc</dt>
<dd> <p> Default personal initialization file, executed for interactive shells when <font SIZE="-1"><code>ENV</code> </font> is not set. </p>
 </dd>
<dt><code>/etc/suid_profile</code></dt>
<dd> <p> Alternative initialization file, executed instead of the personal initialization file when the real and effective user or group id do not match. </p>
 </dd>
<dt><code>/dev/null</code></dt>
<dd> <p> NULL device </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cat/">cat</a>(1), <a href="/docs/linux/man/1-cd/">cd</a>(1), <a href="/docs/linux/man/1-chmod/">chmod</a>(1), <a href="/docs/linux/man/1-cut/">cut</a>(1), <a href="/docs/linux/man/1-egrep/">egrep</a>(1), <a href="/docs/linux/man/1-echo/">echo</a>(1), <a href="/docs/linux/man/1-emacs/">emacs</a>(1), <a href="/docs/linux/man/1-env/">env</a>(1), <a href="/docs/linux/man/1-fgrep/">fgrep</a>(1), gmacs(1), <a href="/docs/linux/man/1-grep/">grep</a>(1), <a href="/docs/linux/man/1-newgrp/">newgrp</a>(1), pfexec(1), <a href="/docs/linux/man/1-stty/">stty</a>(1), <a href="/docs/linux/man/1-test/">test</a>(1), <a href="/docs/linux/man/1-umask/">umask</a>(1), <a href="/docs/linux/man/1-vi/">vi</a>(1), <a href="/docs/linux/man/2-dup/">dup</a>(2), exec(2), <a href="/docs/linux/man/2-fork/">fork</a>(2), <a href="/docs/linux/man/3-getpwnam/">getpwnam</a>(3), <a href="/docs/linux/man/2-ioctl/">ioctl</a>(2), <a href="/docs/linux/man/2-lseek/">lseek</a>(2), <a href="/docs/linux/man/1-paste/">paste</a>(1), pathconf(2), <a href="/docs/linux/man/2-pipe/">pipe</a>(2), sysconf(2), <a href="/docs/linux/man/2-umask/">umask</a>(2), ulimit(2), <a href="/docs/linux/man/2-wait/">wait</a>(2), <a href="/docs/linux/man/3-wctrans/">wctrans</a>(3), <a href="/docs/linux/man/3-rand/">rand</a>(3), a.out(5), profile(5), <a href="/docs/linux/man/7-environ/">environ</a>(7). </p>
<p> Morris I. Bolsky and David G. Korn, <i>The New KornShell Command and Programming Language</i>, Prentice Hall, 1995. </p>
<p> <i>POSIX - Part 2: Shell and Utilities,</i> IEEE Std 1003.2-1992, ISO/IEC 9945-2, IEEE, 1993.  </p>
<h2>CAVEATS</h2>
<p> If a command is executed, and then a command with the same name is installed in a directory in the search path before the directory where the original command was found, the shell will continue to <i>exec</i> the original command. Use the <code>-t</code> option of the <code>alias</code> command to correct this situation. </p>
<p> Some very old shell scripts contain a <code>^</code> as a synonym for the pipe character <code>|</code>. </p>
<p> Using the <code>hist</code> built-in command within a compound command will cause the whole command to disappear from the history file. </p>
<p> The built-in command <code>.</code> <i>file</i> reads the whole file before any commands are executed. Therefore, <code>alias</code> and <code>unalias</code> commands in the file will not apply to any commands defined in the file. </p>
<p> Traps are not processed while a job is waiting for a foreground process. Thus, a trap on <code>CHLD</code> won&#8217;t be executed until the foreground job terminates. </p>
<p> It is a good idea to leave a space after the comma operator in arithmetic expressions to prevent the comma from being interpreted as the decimal point character in certain locales. </p>
