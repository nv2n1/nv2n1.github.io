---
title: "bash(1)"
name: "bash"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bash/"
description: "bash – GNU Bourne-Again SHell"
---

<h2 class="name">NAME</h2>
<p> bash &#8211; GNU Bourne-Again SHell </p>
<h2>SYNOPSIS</h2>
<p> <code>bash</code> [options] [command_string | file]</p>
<h2>COPYRIGHT</h2>
<p> Bash is Copyright (C) 1989-2020 by the Free Software Foundation, Inc.</p>
<h2>DESCRIPTION</h2>
<p> <code>Bash</code> is an <code>sh</code>-compatible command language interpreter that executes commands read from the standard input or from a file. <code>Bash</code> also incorporates useful features from the <i>Korn</i> and <i>C</i> shells (<code>ksh</code> and <code>csh</code>). </p>
<p> <code>Bash</code> is intended to be a conformant implementation of the Shell and Utilities portion of the IEEE POSIX specification (IEEE Standard 1003.1). <code>Bash</code> can be configured to be POSIX-conformant by default.</p>
<h2>OPTIONS</h2>
<p> All of the single-character shell options documented in the description of the <code>set</code> builtin command, including <code>-o</code>, can be used as options when the shell is invoked. In addition, <code>bash</code> interprets the following options when it is invoked: </p>
<dl>
<dt><code>-c</code></p>
<dd> If the <code>-c</code> option is present, then commands are read from the first non-option argument <i>command_string</i>. If there are arguments after the <i>command_string</i>, the first argument is assigned to <code>$0</code> and any remaining arguments are assigned to the positional parameters. The assignment to <code>$0</code> sets the name of the shell, which is used in warning and error messages.</p>
<dt><code>-i</code></p>
<dd> If the <code>-i</code> option is present, the shell is <i>interactive</i>.</p>
<dt><code>-l</code></p>
<dd> Make <code>bash</code> act as if it had been invoked as a login shell (see <font SIZE="-1"><code>INVOCATION</code> </font> below).</p>
<dt><code>-r</code></p>
<dd> If the <code>-r</code> option is present, the shell becomes <i>restricted</i> (see <font SIZE="-1"><code>RESTRICTED SHELL</code> </font> below).</p>
<dt><code>-s</code></p>
<dd> If the <code>-s</code> option is present, or if no arguments remain after option processing, then commands are read from the standard input. This option allows the positional parameters to be set when invoking an interactive shell or when reading input through a pipe.</p>
<dt><code>-v</code></p>
<dd> Print shell input lines as they are read.</p>
<dt><code>-x</code></p>
<dd> Print commands and their arguments as they are executed.</p>
<dt><code>-D</code></p>
<dd> A list of all double-quoted strings preceded by <code>$</code> is printed on the standard output. These are the strings that are subject to language translation when the current locale is not <code>C</code> or <code>POSIX</code>. This implies the <code>-n</code> option; no commands will be executed.</p>
<dt><code>[-+]O [</code><i>shopt_option</i>]</p>
<dd> <i>shopt_option</i> is one of the shell options accepted by the <code>shopt</code> builtin (see <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below). If <i>shopt_option</i> is present, <code>-O</code> sets the value of that option; <code>+O</code> unsets it. If <i>shopt_option</i> is not supplied, the names and values of the shell options accepted by <code>shopt</code> are printed on the standard output. If the invocation option is <code>+O</code>, the output is displayed in a format that may be reused as input.</p>
<dt><code>&#8212;</code></p>
<dd> A <code>&#8212;</code> signals the end of options and disables further option processing. Any arguments after the <code>&#8212;</code> are treated as filenames and arguments. An argument of <code>&#8211;</code> is equivalent to <code>&#8212;</code>.</dl>
<p> <code>Bash</code> also interprets a number of multi-character options. These options must appear on the command line before the single-character options to be recognized. </p>
<dl>
<dt><code>&#8211;debugger</code></p>
<dd> Arrange for the debugger profile to be executed before the shell starts. Turns on extended debugging mode (see the description of the <code>extdebug</code> option to the <code>shopt</code> builtin below).</p>
<dt><code>&#8211;dump-po-strings</code></p>
<dd> Equivalent to <code>-D</code>, but the output is in the GNU <i>gettext</i> <code>po</code> (portable object) file format.</p>
<dt><code>&#8211;dump-strings</code></p>
<dd> Equivalent to <code>-D</code>.</p>
<dt><code>&#8211;help</code></p>
<dd> Display a usage message on standard output and exit successfully.</p>
<dt><code>&#8211;init-file</code> <i>file</i></p>
<dd>
<dt><code>&#8211;rcfile</code> <i>file</i></p>
<dd> Execute commands from <i>file</i> instead of the system wide initialization file <i>/etc/bash.bashrc</i> and the standard personal initialization file <i>~/.bashrc</i> if the shell is interactive (see <font SIZE="-1"><code>INVOCATION</code> </font> below).</p>
<dt><code>&#8211;login</code></p>
<dd> Equivalent to <code>-l</code>.</p>
<dt><code>&#8211;noediting</code></p>
<dd> Do not use the GNU <code>readline</code> library to read command lines when the shell is interactive.</p>
<dt><code>&#8211;noprofile</code></p>
<dd> Do not read either the system-wide startup file <i>/etc/profile</i> or any of the personal initialization files <i>~/.bash_profile</i>, <i>~/.bash_login</i>, or <i>~/.profile</i>. By default, <code>bash</code> reads these files when it is invoked as a login shell (see <font SIZE="-1"><code>INVOCATION</code> </font> below).</p>
<dt><code>&#8211;norc</code></p>
<dd> Do not read and execute the system wide initialization file <i>/etc/bash.bashrc</i> and the personal initialization file <i>~/.bashrc</i> if the shell is interactive. This option is on by default if the shell is invoked as <code>sh</code>.</p>
<dt><code>&#8211;posix</code></p>
<dd> Change the behavior of <code>bash</code> where the default operation differs from the POSIX standard to match the standard (<i>posix mode</i>). See <font SIZE="-1"><code>SEE ALSO</code> </font> below for a reference to a document that details how posix mode affects bash&#8217;s behavior.</p>
<dt><code>&#8211;restricted</code></p>
<dd> The shell becomes restricted (see <font SIZE="-1"><code>RESTRICTED SHELL</code> </font> below).</p>
<dt><code>&#8211;verbose</code></p>
<dd> Equivalent to <code>-v</code>.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version information for this instance of <code>bash</code> on the standard output and exit successfully.</dl>
<h2>ARGUMENTS</h2>
<p> If arguments remain after option processing, and neither the <code>-c</code> nor the <code>-s</code> option has been supplied, the first argument is assumed to be the name of a file containing shell commands. If <code>bash</code> is invoked in this fashion, <code>$0</code> is set to the name of the file, and the positional parameters are set to the remaining arguments. <code>Bash</code> reads and executes commands from this file, then exits. <code>Bash</code>&#8216;s exit status is the exit status of the last command executed in the script. If no commands are executed, the exit status is 0. An attempt is first made to open the file in the current directory, and, if no file is found, then the shell searches the directories in <font SIZE="-1"><code>PATH</code> </font> for the script.</p>
<h2>INVOCATION</h2>
<p> A <i>login shell</i> is one whose first character of argument zero is a <code>&#8211;</code>, or one started with the <code>&#8211;login</code> option. </p>
<p> An <i>interactive</i> shell is one started without non-option arguments (unless <code>-s</code> is specified) and without the <code>-c</code> option whose standard input and error are both connected to terminals (as determined by <i><a href="/docs/linux/man/3-isatty/">isatty</a></i>(3)), or one started with the <code>-i</code> option. <font SIZE="-1"><code>PS1</code> </font> is set and <code>$-</code> includes <code>i</code> if <code>bash</code> is interactive, allowing a shell script or a startup file to test this state. </p>
<p> The following paragraphs describe how <code>bash</code> executes its startup files. If any of the files exist but cannot be read, <code>bash</code> reports an error. Tildes are expanded in filenames as described below under <code>Tilde Expansion</code> in the <font SIZE="-1"><code>EXPANSION</code> </font> section. </p>
<p> When <code>bash</code> is invoked as an interactive login shell, or as a non-interactive shell with the <code>&#8211;login</code> option, it first reads and executes commands from the file <i>/etc/profile</i>, if that file exists. After reading that file, it looks for <i>~/.bash_profile</i>, <i>~/.bash_login</i>, and <i>~/.profile</i>, in that order, and reads and executes commands from the first one that exists and is readable. The <code>&#8211;noprofile</code> option may be used when the shell is started to inhibit this behavior. </p>
<p> When an interactive login shell exits, or a non-interactive login shell executes the <code>exit</code> builtin command, <code>bash</code> reads and executes commands from the file <i>~/.bash_logout</i>, if it exists. </p>
<p> When an interactive shell that is not a login shell is started, <code>bash</code> reads and executes commands from <i>/etc/bash.bashrc</i> and <i>~/.bashrc</i>, if these files exist. This may be inhibited by using the <code>&#8211;norc</code> option. The <code>&#8211;rcfile</code> <i>file</i> option will force <code>bash</code> to read and execute commands from <i>file</i> instead of <i>/etc/bash.bashrc</i> and <i>~/.bashrc</i>. </p>
<p> When <code>bash</code> is started non-interactively, to run a shell script, for example, it looks for the variable <font SIZE="-1"><code>BASH_ENV</code> </font> in the environment, expands its value if it appears there, and uses the expanded value as the name of a file to read and execute. <code>Bash</code> behaves as if the following command were executed: </p>
<dl>
<dt>
<dd> if [ -n &quot;$BASH_ENV&quot; ]; then . &quot;$BASH_ENV&quot;; fi</dl>
<p> but the value of the <font SIZE="-1"><code>PATH</code> </font> variable is not used to search for the filename. </p>
<p> If <code>bash</code> is invoked with the name <code>sh</code>, it tries to mimic the startup behavior of historical versions of <code>sh</code> as closely as possible, while conforming to the POSIX standard as well. When invoked as an interactive login shell, or a non-interactive shell with the <code>&#8211;login</code> option, it first attempts to read and execute commands from <i>/etc/profile</i> and <i>~/.profile</i>, in that order. The <code>&#8211;noprofile</code> option may be used to inhibit this behavior. When invoked as an interactive shell with the name <code>sh</code>, <code>bash</code> looks for the variable <font SIZE="-1"><code>ENV</code>, </font> expands its value if it is defined, and uses the expanded value as the name of a file to read and execute. Since a shell invoked as <code>sh</code> does not attempt to read and execute commands from any other startup files, the <code>&#8211;rcfile</code> option has no effect. A non-interactive shell invoked with the name <code>sh</code> does not attempt to read any other startup files. When invoked as <code>sh</code>, <code>bash</code> enters <i>posix</i> mode after the startup files are read. </p>
<p> When <code>bash</code> is started in <i>posix</i> mode, as with the <code>&#8211;posix</code> command line option, it follows the POSIX standard for startup files. In this mode, interactive shells expand the <font SIZE="-1"><code>ENV</code> </font> variable and commands are read and executed from the file whose name is the expanded value. No other startup files are read. </p>
<p> <code>Bash</code> attempts to determine when it is being run with its standard input connected to a network connection, as when executed by the remote shell daemon, usually <i>rshd</i>, or the secure shell daemon <i>sshd</i>. If <code>bash</code> determines it is being run in this fashion, it reads and executes commands from <i>~/.bashrc</i> and <i>~/.bashrc</i>, if these files exist and are readable. It will not do this if invoked as <code>sh</code>. The <code>&#8211;norc</code> option may be used to inhibit this behavior, and the <code>&#8211;rcfile</code> option may be used to force another file to be read, but neither <i>rshd</i> nor <i>sshd</i> generally invoke the shell with those options or allow them to be specified. </p>
<p> If the shell is started with the effective user (group) id not equal to the real user (group) id, and the <code>-p</code> option is not supplied, no startup files are read, shell functions are not inherited from the environment, the <font SIZE="-1"><code>SHELLOPTS</code>, </font> <font SIZE="-1"><code>BASHOPTS</code>, </font> <font SIZE="-1"><code>CDPATH</code>, </font> and <font SIZE="-1"><code>GLOBIGNORE</code> </font> variables, if they appear in the environment, are ignored, and the effective user id is set to the real user id. If the <code>-p</code> option is supplied at invocation, the startup behavior is the same, but the effective user id is not reset.</p>
<h2>DEFINITIONS</h2>
<p> The following definitions are used throughout the rest of this document.</p>
<dl>
<dt><code>blank</code></p>
<dd> A space or tab.</p>
<dt><code>word</code></p>
<dd> A sequence of characters considered as a single unit by the shell. Also known as a <code>token</code>.</p>
<dt><code>name</code></p>
<dd> A <i>word</i> consisting only of alphanumeric characters and underscores, and beginning with an alphabetic character or an underscore. Also referred to as an <code>identifier</code>.</p>
<dt><code>metacharacter</code></p>
<dd> A character that, when unquoted, separates words. One of the following: </p>
<dl>
<dt>
<dd>
<p> <code>| &amp; ; ( ) &lt; &gt; space tab newline</code></dl>
<dt><code>control operator</code></p>
<dd> A <i>token</i> that performs a control function. It is one of the following symbols:</p>
<dl>
<dt>
<dd>
<p> <code>|| &amp; &amp;&amp; ; ;; ;&amp; ;;&amp; ( ) | |&amp; &lt;newline&gt;</code></dl>
</dl>
<h2>RESERVED WORDS</h2>
<p> <i>Reserved words</i> are words that have a special meaning to the shell. The following words are recognized as reserved when unquoted and either the first word of a command (see <font SIZE="-1"><code>SHELL GRAMMAR</code> </font> below), the third word of a <code>case</code> or <code>select</code> command (only <code>in</code> is valid), or the third word of a <code>for</code> command (only <code>in</code> and <code>do</code> are valid): </p>
<p> <code>! case coproc do done elif else esac fi for function if in select then until while { } time [[ ]] </code></p>
<h2>SHELL GRAMMAR</h2>
<h3>Simple Commands</h3>
<p> A <i>simple command</i> is a sequence of optional variable assignments followed by <code>blank</code>-separated words and redirections, and terminated by a <i>control operator</i>. The first word specifies the command to be executed, and is passed as argument zero. The remaining words are passed as arguments to the invoked command. </p>
<p> The return value of a <i>simple command</i> is its exit status, or 128+<i>n</i> if the command is terminated by signal <i>n</i>.</p>
<h3>Pipelines</h3>
<p> A <i>pipeline</i> is a sequence of one or more commands separated by one of the control operators <code>|</code> or <code>|&amp;</code>. The format for a pipeline is:</p>
<dl>
<dt>
<dd>
<p> [<code>time</code> [<code>-p</code>]] [ ! ] <i>command</i> [ [<code>|</code>|<code>|&amp;</code>] <i>command2</i> &#8230; ]</dl>
<p> The standard output of <i>command</i> is connected via a pipe to the standard input of <i>command2</i>. This connection is performed before any redirections specified by the command (see <font SIZE="-1"><code>REDIRECTION</code> </font> below). If <code>|&amp;</code> is used, <i>command</i>&#8216;s standard error, in addition to its standard output, is connected to <i>command2</i>&#8216;s standard input through the pipe; it is shorthand for <code>2&gt;&amp;1 |</code>. This implicit redirection of the standard error to the standard output is performed after any redirections specified by the command. </p>
<p> The return status of a pipeline is the exit status of the last command, unless the <code>pipefail</code> option is enabled. If <code>pipefail</code> is enabled, the pipeline&#8217;s return status is the value of the last (rightmost) command to exit with a non-zero status, or zero if all commands exit successfully. If the reserved word <code>!</code> precedes a pipeline, the exit status of that pipeline is the logical negation of the exit status as described above. The shell waits for all commands in the pipeline to terminate before returning a value. </p>
<p> If the <code>time</code> reserved word precedes a pipeline, the elapsed as well as user and system time consumed by its execution are reported when the pipeline terminates. The <code>-p</code> option changes the output format to that specified by POSIX. When the shell is in <i>posix mode</i>, it does not recognize <code>time</code> as a reserved word if the next token begins with a `-&#8216;. The <font SIZE="-1"><code>TIMEFORMAT</code> </font> variable may be set to a format string that specifies how the timing information should be displayed; see the description of <font SIZE="-1"><code>TIMEFORMAT</code> </font> under <code>Shell Variables</code> below. </p>
<p> When the shell is in <i>posix mode</i>, <code>time</code> may be followed by a newline. In this case, the shell displays the total user and system time consumed by the shell and its children. The <font SIZE="-1"><code>TIMEFORMAT</code> </font> variable may be used to specify the format of the time information. </p>
<p> Each command in a pipeline is executed as a separate process (i.e., in a subshell). See <font SIZE="-1"><code>COMMAND EXECUTION ENVIRONMENT</code></font> for a description of a subshell environment. If the <code>lastpipe</code> option is enabled using the <code>shopt</code> builtin (see the description of <code>shopt</code> below), the last element of a pipeline may be run by the shell process.</p>
<h3>Lists</h3>
<p> A <i>list</i> is a sequence of one or more pipelines separated by one of the operators <code>;</code>, <code>&amp;</code>, <code>&amp;&amp;</code>, or <code>||</code>, and optionally terminated by one of <code>;</code>, <code>&amp;</code>, or <code>&lt;newline&gt;</code>. </p>
<p> Of these list operators, <code>&amp;&amp;</code> and <code>||</code> have equal precedence, followed by <code>;</code> and <code>&amp;</code>, which have equal precedence. </p>
<p> A sequence of one or more newlines may appear in a <i>list</i> instead of a semicolon to delimit commands. </p>
<p> If a command is terminated by the control operator <code>&amp;</code>, the shell executes the command in the <i>background</i> in a subshell. The shell does not wait for the command to finish, and the return status is 0. These are referred to as <i>asynchronous</i> commands. Commands separated by a <code>;</code> are executed sequentially; the shell waits for each command to terminate in turn. The return status is the exit status of the last command executed. </p>
<p> AND and OR lists are sequences of one or more pipelines separated by the <code>&amp;&amp;</code> and <code>||</code> control operators, respectively. AND and OR lists are executed with left associativity. An AND list has the form</p>
<dl>
<dt>
<dd>
<p> <i>command1</i> <code>&amp;&amp;</code> <i>command2</i></dl>
<p> <i>command2</i> is executed if, and only if, <i>command1</i> returns an exit status of zero (success). </p>
<p> An OR list has the form</p>
<dl>
<dt>
<dd>
<p> <i>command1</i> <code>||</code> <i>command2</i></dl>
<p> <i>command2</i> is executed if, and only if, <i>command1</i> returns a non-zero exit status. The return status of AND and OR lists is the exit status of the last command executed in the list.</p>
<h3>Compound Commands</h3>
<p> A <i>compound command</i> is one of the following. In most cases a <i>list</i> in a command&#8217;s description may be separated from the rest of the command by one or more newlines, and may be followed by a newline in place of a semicolon.</p>
<dl>
<dt>(<i>list</i>)</p>
<dd> <i>list</i> is executed in a subshell environment (see <font SIZE="-1"><code>COMMAND EXECUTION ENVIRONMENT</code></font> below). Variable assignments and builtin commands that affect the shell&#8217;s environment do not remain in effect after the command completes. The return status is the exit status of <i>list</i>.</p>
<dt>{ <i>list</i>; }</p>
<dd> <i>list</i> is simply executed in the current shell environment. <i>list</i> must be terminated with a newline or semicolon. This is known as a <i>group command</i>. The return status is the exit status of <i>list</i>. Note that unlike the metacharacters <code>(</code> and <code>)</code>, <code>{</code> and <code>}</code> are <i>reserved words</i> and must occur where a reserved word is permitted to be recognized. Since they do not cause a word break, they must be separated from <i>list</i> by whitespace or another shell metacharacter.</p>
<dt>((<i>expression</i>))</p>
<dd> The <i>expression</i> is evaluated according to the rules described below under <font SIZE="-1"><code>ARITHMETIC</code>EVALUATION<code>.</code> </font> If the value of the expression is non-zero, the return status is 0; otherwise the return status is 1. This is exactly equivalent to <code>let &quot;</code><i>expression</i>&quot;.</p>
<dt><code>[[</code> <i>expression</i> <code>]]</code></p>
<dd> Return a status of 0 or 1 depending on the evaluation of the conditional expression <i>expression</i>. Expressions are composed of the primaries described below under <font SIZE="-1"><code>CONDITIONAL</code>EXPRESSIONS<code>.</code> </font> Word splitting and pathname expansion are not performed on the words between the <code>[[</code> and <code>]]</code>; tilde expansion, parameter and variable expansion, arithmetic expansion, command substitution, process substitution, and quote removal are performed. Conditional operators such as <code>-f</code> must be unquoted to be recognized as primaries. </p>
<p> When used with <code>[[</code>, the <code>&lt;</code> and <code>&gt;</code> operators sort lexicographically using the current locale.</dl>
<p> See the description of the <i>test</i> builtin command (section SHELL BUILTIN COMMANDS below) for the handling of parameters (i.e. missing parameters). </p>
<p> When the <code>==</code> and <code>!=</code> operators are used, the string to the right of the operator is considered a pattern and matched according to the rules described below under <code>Pattern Matching</code>, as if the <code>extglob</code> shell option were enabled. The <code>=</code> operator is equivalent to <code>==</code>. If the <code>nocasematch</code> shell option is enabled, the match is performed without regard to the case of alphabetic characters. The return value is 0 if the string matches (<code>==</code>) or does not match (<code>!=</code>) the pattern, and 1 otherwise. Any part of the pattern may be quoted to force the quoted portion to be matched as a string. </p>
<p> An additional binary operator, <code>=~</code>, is available, with the same precedence as <code>==</code> and <code>!=</code>. When it is used, the string to the right of the operator is considered a POSIX extended regular expression and matched accordingly (using the POSIX <i>regcomp</i> and <i>regexec</i> interfaces usually described in <i><a href="/docs/linux/man/3-regex/">regex</a></i>(3)). The return value is 0 if the string matches the pattern, and 1 otherwise. If the regular expression is syntactically incorrect, the conditional expression&#8217;s return value is 2. If the <code>nocasematch</code> shell option is enabled, the match is performed without regard to the case of alphabetic characters. Any part of the pattern may be quoted to force the quoted portion to be matched as a string. Bracket expressions in regular expressions must be treated carefully, since normal quoting characters lose their meanings between brackets. If the pattern is stored in a shell variable, quoting the variable expansion forces the entire pattern to be matched as a string. </p>
<p> The pattern will match if it matches any part of the string. Anchor the pattern using the <code>^</code> and <code>$</code> regular expression operators to force it to match the entire string. The array variable <font SIZE="-1"><code>BASH_REMATCH</code> </font> records which parts of the string matched the pattern. The element of <font SIZE="-1"><code>BASH_REMATCH</code> </font> with index 0 contains the portion of the string matching the entire regular expression. Substrings matched by parenthesized subexpressions within the regular expression are saved in the remaining <font SIZE="-1"><code>BASH_REMATCH</code> </font> indices. The element of <font SIZE="-1"><code>BASH_REMATCH</code> </font> with index <i>n</i> is the portion of the string matching the <i>n</i>th parenthesized subexpression. </p>
<p> Expressions may be combined using the following operators, listed in decreasing order of precedence: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>( </code><i>expression</i> )</p>
<dd> Returns the value of <i>expression</i>. This may be used to override the normal precedence of operators.</p>
<dt><code>! </code><i>expression</i></p>
<dd> True if <i>expression</i> is false.</p>
<dt><i>expression1</i> <code>&amp;&amp;</code> <i>expression2</i></p>
<dd> True if both <i>expression1</i> and <i>expression2</i> are true.</p>
<dt><i>expression1</i> <code>||</code> <i>expression2</i></p>
<dd> True if either <i>expression1</i> or <i>expression2</i> is true.</dl>
<p> The <code>&amp;&amp;</code> and <code>||</code> operators do not evaluate <i>expression2</i> if the value of <i>expression1</i> is sufficient to determine the return value of the entire conditional expression.</dl>
<dl>
<dt><code>for</code> <i>name</i> [ [ <code>in</code> [ <i>word &#8230;</i> ] ] ; ] <code>do</code> <i>list</i> ; <code>done</code></p>
<dd> The list of words following <code>in</code> is expanded, generating a list of items. The variable <i>name</i> is set to each element of this list in turn, and <i>list</i> is executed each time. If the <code>in</code> <i>word</i> is omitted, the <code>for</code> command executes <i>list</i> once for each positional parameter that is set (see <font SIZE="-1"><code>PARAMETERS</code> </font> below). The return status is the exit status of the last command that executes. If the expansion of the items following <code>in</code> results in an empty list, no commands are executed, and the return status is 0.</p>
<dt><code>for</code> (( <i>expr1</i> ; <i>expr2</i> ; <i>expr3</i> )) ; <code>do</code> <i>list</i> ; <code>done</code></p>
<dd> First, the arithmetic expression <i>expr1</i> is evaluated according to the rules described below under <font SIZE="-1"><code>ARITHMETIC</code>EVALUATION<code>.</code> </font> The arithmetic expression <i>expr2</i> is then evaluated repeatedly until it evaluates to zero. Each time <i>expr2</i> evaluates to a non-zero value, <i>list</i> is executed and the arithmetic expression <i>expr3</i> is evaluated. If any expression is omitted, it behaves as if it evaluates to 1. The return value is the exit status of the last command in <i>list</i> that is executed, or false if any of the expressions is invalid.</p>
<dt><code>select</code> <i>name</i> [ <code>in</code> <i>word</i> ] ; <code>do</code> <i>list</i> ; <code>done</code></p>
<dd> The list of words following <code>in</code> is expanded, generating a list of items. The set of expanded words is printed on the standard error, each preceded by a number. If the <code>in</code> <i>word</i> is omitted, the positional parameters are printed (see <font SIZE="-1"><code>PARAMETERS</code> </font> below). The <font SIZE="-1"><code>PS3</code> </font> prompt is then displayed and a line read from the standard input. If the line consists of a number corresponding to one of the displayed words, then the value of <i>name</i> is set to that word. If the line is empty, the words and prompt are displayed again. If EOF is read, the command completes. Any other value read causes <i>name</i> to be set to null. The line read is saved in the variable <font SIZE="-1"><code>REPLY</code>. </font> The <i>list</i> is executed after each selection until a <code>break</code> command is executed. The exit status of <code>select</code> is the exit status of the last command executed in <i>list</i>, or zero if no commands were executed.</p>
<dt><code>case</code> <i>word</i> <code>in</code> [ [(] <i>pattern</i> [ <code>|</code> <i>pattern</i> ]</p>
<dd> A <code>case</code> command first expands <i>word</i>, and tries to match it against each <i>pattern</i> in turn, using the matching rules described under <code>Pattern Matching</code> below. The <i>word</i> is expanded using tilde expansion, parameter and variable expansion, arithmetic expansion, command substitution, process substitution and quote removal. Each <i>pattern</i> examined is expanded using tilde expansion, parameter and variable expansion, arithmetic expansion, command substitution, and process substitution. If the <code>nocasematch</code> shell option is enabled, the match is performed without regard to the case of alphabetic characters. When a match is found, the corresponding <i>list</i> is executed. If the <code>;;</code> operator is used, no subsequent matches are attempted after the first pattern match. Using <code>;&amp;</code> in place of <code>;;</code> causes execution to continue with the <i>list</i> associated with the next set of patterns. Using <code>;;&amp;</code> in place of <code>;;</code> causes the shell to test the next pattern list in the statement, if any, and execute any associated <i>list</i> on a successful match, continuing the case statement execution as if the pattern list had not matched. The exit status is zero if no pattern matches. Otherwise, it is the exit status of the last command executed in <i>list</i>.</p>
<dt><code>if</code> <i>list</i>; <code>then</code> <i>list</i>; [ <code>elif</code> <i>list</i>; <code>then</code> <i>list</i>; ] &#8230; [ <code>else</code> <i>list</i>; ] <code>fi</code></p>
<dd> The <code>if</code> <i>list</i> is executed. If its exit status is zero, the <code>then</code> <i>list</i> is executed. Otherwise, each <code>elif</code> <i>list</i> is executed in turn, and if its exit status is zero, the corresponding <code>then</code> <i>list</i> is executed and the command completes. Otherwise, the <code>else</code> <i>list</i> is executed, if present. The exit status is the exit status of the last command executed, or zero if no condition tested true.</p>
<dt><code>while</code> <i>list-1</i>; <code>do</code> <i>list-2</i>; <code>done</code></p>
<dd>
<dt><code>until</code> <i>list-1</i>; <code>do</code> <i>list-2</i>; <code>done</code></p>
<dd> The <code>while</code> command continuously executes the list <i>list-2</i> as long as the last command in the list <i>list-1</i> returns an exit status of zero. The <code>until</code> command is identical to the <code>while</code> command, except that the test is negated: <i>list-2</i> is executed as long as the last command in <i>list-1</i> returns a non-zero exit status. The exit status of the <code>while</code> and <code>until</code> commands is the exit status of the last command executed in <i>list-2</i>, or zero if none was executed.</dl>
<h3>Coprocesses</h3>
<p> A <i>coprocess</i> is a shell command preceded by the <code>coproc</code> reserved word. A coprocess is executed asynchronously in a subshell, as if the command had been terminated with the <code>&amp;</code> control operator, with a two-way pipe established between the executing shell and the coprocess. </p>
<p> The format for a coprocess is:</p>
<dl>
<dt>
<dd>
<p> <code>coproc</code> [<i>NAME</i>] <i>command</i> [<i>redirections</i>]</dl>
<p> This creates a coprocess named <i>NAME</i>. If <i>NAME</i> is not supplied, the default name is <code>COPROC</code>. <i>NAME</i> must not be supplied if <i>command</i> is a <i>simple command</i> (see above); otherwise, it is interpreted as the first word of the simple command. When the coprocess is executed, the shell creates an array variable (see <code>Arrays</code> below) named <i>NAME</i> in the context of the executing shell. The standard output of <i>command</i> is connected via a pipe to a file descriptor in the executing shell, and that file descriptor is assigned to <i>NAME</i>[0]. The standard input of <i>command</i> is connected via a pipe to a file descriptor in the executing shell, and that file descriptor is assigned to <i>NAME</i>[1]. This pipe is established before any redirections specified by the command (see <font SIZE="-1"><code>REDIRECTION</code> </font> below). The file descriptors can be utilized as arguments to shell commands and redirections using standard word expansions. Other than those created to execute command and process substitutions, the file descriptors are not available in subshells. The process ID of the shell spawned to execute the coprocess is available as the value of the variable <i>NAME</i>_PID. The <code>wait</code> builtin command may be used to wait for the coprocess to terminate. </p>
<p> Since the coprocess is created as an asynchronous command, the <code>coproc</code> command always returns success. The return status of a coprocess is the exit status of <i>command</i>.</p>
<h3>Shell Function Definitions</h3>
<p> A shell function is an object that is called like a simple command and executes a compound command with a new set of positional parameters. Shell functions are declared as follows:</p>
<dl>
<dt><i>fname</i> () <i>compound-command</i> [<i>redirection</i>]</p>
<dd>
<dt><code>function</code> <i>fname</i> [()] <i>compound-command</i> [<i>redirection</i>]</p>
<dd> This defines a function named <i>fname</i>. The reserved word <code>function</code> is optional. If the <code>function</code> reserved word is supplied, the parentheses are optional. The <i>body</i> of the function is the compound command <i>compound-command</i> (see <code>Compound Commands</code> above). That command is usually a <i>list</i> of commands between { and }, but may be any command listed under <code>Compound Commands</code> above, with one exception: If the <code>function</code> reserved word is used, but the parentheses are not supplied, the braces are required. <i>compound-command</i> is executed whenever <i>fname</i> is specified as the name of a simple command. When in <i>posix mode</i>, <i>fname</i> must be a valid shell <i>name</i> and may not be the name of one of the POSIX <i>special builtins</i>. In default mode, a function name can be any unquoted shell word that does not contain <code>$</code>. Any redirections (see <font SIZE="-1"><code>REDIRECTION</code> </font> below) specified when a function is defined are performed when the function is executed. The exit status of a function definition is zero unless a syntax error occurs or a readonly function with the same name already exists. When executed, the exit status of a function is the exit status of the last command executed in the body. (See <font SIZE="-1"><code>FUNCTIONS</code> </font> below.)</dl>
<h2>COMMENTS</h2>
<p> In a non-interactive shell, or an interactive shell in which the <code>interactive_comments</code> option to the <code>shopt</code> builtin is enabled (see <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below), a word beginning with <code>#</code> causes that word and all remaining characters on that line to be ignored. An interactive shell without the <code>interactive_comments</code> option enabled does not allow comments. The <code>interactive_comments</code> option is on by default in interactive shells.</p>
<h2>QUOTING</h2>
<p> <i>Quoting</i> is used to remove the special meaning of certain characters or words to the shell. Quoting can be used to disable special treatment for special characters, to prevent reserved words from being recognized as such, and to prevent parameter expansion. </p>
<p> Each of the <i>metacharacters</i> listed above under <font SIZE="-1"><code>DEFINITIONS</code> </font> has special meaning to the shell and must be quoted if it is to represent itself. </p>
<p> When the command history expansion facilities are being used (see <font SIZE="-1"><code>HISTORY EXPANSION</code> </font> below), the <i>history expansion</i> character, usually <code>!</code>, must be quoted to prevent history expansion. </p>
<p> There are three quoting mechanisms: the <i>escape character</i>, single quotes, and double quotes. </p>
<p> A non-quoted backslash (<code>\</code>) is the <i>escape character</i>. It preserves the literal value of the next character that follows, with the exception of &lt;newline&gt;. If a <code>\</code>&lt;newline&gt; pair appears, and the backslash is not itself quoted, the <code>\</code>&lt;newline&gt; is treated as a line continuation (that is, it is removed from the input stream and effectively ignored). </p>
<p> Enclosing characters in single quotes preserves the literal value of each character within the quotes. A single quote may not occur between single quotes, even when preceded by a backslash. </p>
<p> Enclosing characters in double quotes preserves the literal value of all characters within the quotes, with the exception of <code>$</code>, <code>`</code>, <code>\</code>, and, when history expansion is enabled, <code>!</code>. When the shell is in <i>posix mode</i>, the <code>!</code> has no special meaning within double quotes, even when history expansion is enabled. The characters <code>$</code> and <code>`</code> retain their special meaning within double quotes. The backslash retains its special meaning only when followed by one of the following characters: <code>$</code>, <code>`</code>, <code>&quot;</code>, <code>\</code>, or <code>&lt;newline&gt;</code>. A double quote may be quoted within double quotes by preceding it with a backslash. If enabled, history expansion will be performed unless an <code>!</code> appearing in double quotes is escaped using a backslash. The backslash preceding the <code>!</code> is not removed. </p>
<p> The special parameters <code>*</code> and <code>@</code> have special meaning when in double quotes (see <font SIZE="-1"><code>PARAMETERS</code> </font> below). </p>
<p> Words of the form <code>$</code>&#8216;<i>string</i>&#8216; are treated specially. The word expands to <i>string</i>, with backslash-escaped characters replaced as specified by the ANSI C standard. Backslash escape sequences, if present, are decoded as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code></code></p>
<dd> alert (bell)</p>
<dt><code></code></p>
<dd> backspace</p>
<dt><code></code></p>
<dd>
<dt><code>\E</code></p>
<dd> an escape character</p>
<dt><code></code></p>
<dd> form feed</p>
<dt><code>
</code></p>
<dd> new line</p>
<dt><code></code></p>
<dd> carriage return</p>
<dt><code>	</code></p>
<dd> horizontal tab</p>
<dt><code></code></p>
<dd> vertical tab</p>
<dt><code>\</code></p>
<dd> backslash</p>
<dt><code>\&#8217;</code></p>
<dd> single quote</p>
<dt><code>\&quot;</code></p>
<dd> double quote</p>
<dt><code>\?</code></p>
<dd> question mark</p>
<dt><code>\</code><i>nnn</i></p>
<dd> the eight-bit character whose value is the octal value <i>nnn</i> (one to three octal digits)</p>
<dt><code>
