---

title: "bash(1)"
name: "bash"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bash/"
description: "bash – GNU Bourne-Again SHell"
---

<p> bash - GNU Bourne-Again SHell </p>
<h2>SYNOPSIS</h2>
<p> <code>bash</code> [options] [command_string | file]  </p>
<h2>COPYRIGHT</h2>
<p> Bash is Copyright (C) 1989-2020 by the Free Software Foundation, Inc.  </p>
<h2>DESCRIPTION</h2>
<p> <code>Bash</code> is an <code>sh</code>-compatible command language interpreter that executes commands read from the standard input or from a file. <code>Bash</code> also incorporates useful features from the <i>Korn</i> and <i>C</i> shells (<code>ksh</code> and <code>csh</code>). </p>
<p> <code>Bash</code> is intended to be a conformant implementation of the Shell and Utilities portion of the IEEE POSIX specification (IEEE Standard 1003.1). <code>Bash</code> can be configured to be POSIX-conformant by default.  </p>
<h2>OPTIONS</h2>
<p> All of the single-character shell options documented in the description of the <code>set</code> builtin command, including <code>-o</code>, can be used as options when the shell is invoked. In addition, <code>bash</code> interprets the following options when it is invoked: </p>
<dl>
<dt><code>-c</code></dt>
<dd> <p> If the <code>-c</code> option is present, then commands are read from the first non-option argument <i>command_string</i>. If there are arguments after the <i>command_string</i>, the first argument is assigned to <code>$0</code> and any remaining arguments are assigned to the positional parameters. The assignment to <code>$0</code> sets the name of the shell, which is used in warning and error messages. </p>
 </dd>
<dt><code>-i</code></dt>
<dd> <p> If the <code>-i</code> option is present, the shell is <i>interactive</i>. </p>
 </dd>
<dt><code>-l</code></dt>
<dd> <p> Make <code>bash</code> act as if it had been invoked as a login shell (see <font SIZE="-1"><code>INVOCATION</code> </font> below). </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> If the <code>-r</code> option is present, the shell becomes <i>restricted</i> (see <font SIZE="-1"><code>RESTRICTED SHELL</code> </font> below). </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> If the <code>-s</code> option is present, or if no arguments remain after option processing, then commands are read from the standard input. This option allows the positional parameters to be set when invoking an interactive shell or when reading input through a pipe. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Print shell input lines as they are read. </p>
 </dd>
<dt><code>-x</code></dt>
<dd> <p> Print commands and their arguments as they are executed. </p>
 </dd>
<dt><code>-D</code></dt>
<dd> <p> A list of all double-quoted strings preceded by <code>$</code> is printed on the standard output. These are the strings that are subject to language translation when the current locale is not <code>C</code> or <code>POSIX</code>. This implies the <code>-n</code> option; no commands will be executed. </p>
 </dd>
<dt><code>[-+]O [</code><i>shopt_option</i>] </dt>
<dd> <p> <i>shopt_option</i> is one of the shell options accepted by the <code>shopt</code> builtin (see <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below). If <i>shopt_option</i> is present, <code>-O</code> sets the value of that option; <code>+O</code> unsets it. If <i>shopt_option</i> is not supplied, the names and values of the shell options accepted by <code>shopt</code> are printed on the standard output. If the invocation option is <code>+O</code>, the output is displayed in a format that may be reused as input. </p>
 </dd>
<dt><code>--</code></dt>
<dd> <p> A <code>--</code> signals the end of options and disables further option processing. Any arguments after the <code>--</code> are treated as filenames and arguments. An argument of <code>-</code> is equivalent to <code>--</code>. </p>
 </dd></dl>
<p> <code>Bash</code> also interprets a number of multi-character options. These options must appear on the command line before the single-character options to be recognized. </p>
<dl>
<dt><code>--debugger</code></dt>
<dd> <p> Arrange for the debugger profile to be executed before the shell starts. Turns on extended debugging mode (see the description of the <code>extdebug</code> option to the <code>shopt</code> builtin below). </p>
 </dd>
<dt><code>--dump-po-strings</code></dt>
<dd> <p> Equivalent to <code>-D</code>, but the output is in the GNU <i>gettext</i> <code>po</code> (portable object) file format. </p>
 </dd>
<dt><code>--dump-strings</code></dt>
<dd> <p> Equivalent to <code>-D</code>. </p>
 </dd>
<dt><code>--help</code></dt>
<dd> <p> Display a usage message on standard output and exit successfully. </p>
 </dd>
<dt><code>--init-file</code><i>file</i></dt>
<dd>  </dd>
<dt><code>--rcfile</code><i>file</i></dt>
<dd> <p> Execute commands from <i>file</i> instead of the system wide initialization file <i>/etc/bash.bashrc</i> and the standard personal initialization file <i>~/.bashrc</i> if the shell is interactive (see <font SIZE="-1"><code>INVOCATION</code> </font> below). </p>
 </dd>
<dt><code>--login</code></dt>
<dd> <p> Equivalent to <code>-l</code>. </p>
 </dd>
<dt><code>--noediting</code></dt>
<dd> <p> Do not use the GNU <code>readline</code> library to read command lines when the shell is interactive. </p>
 </dd>
<dt><code>--noprofile</code></dt>
<dd> <p> Do not read either the system-wide startup file <i>/etc/profile</i> or any of the personal initialization files <i>~/.bash_profile</i>, <i>~/.bash_login</i>, or <i>~/.profile</i>. By default, <code>bash</code> reads these files when it is invoked as a login shell (see <font SIZE="-1"><code>INVOCATION</code> </font> below). </p>
 </dd>
<dt><code>--norc</code></dt>
<dd> <p> Do not read and execute the system wide initialization file <i>/etc/bash.bashrc</i> and the personal initialization file <i>~/.bashrc</i> if the shell is interactive. This option is on by default if the shell is invoked as <code>sh</code>. </p>
 </dd>
<dt><code>--posix</code></dt>
<dd> <p> Change the behavior of <code>bash</code> where the default operation differs from the POSIX standard to match the standard (<i>posix mode</i>). See <font SIZE="-1"><code>SEE ALSO</code> </font> below for a reference to a document that details how posix mode affects bash&#8217;s behavior. </p>
 </dd>
<dt><code>--restricted</code></dt>
<dd> <p> The shell becomes restricted (see <font SIZE="-1"><code>RESTRICTED SHELL</code> </font> below). </p>
 </dd>
<dt><code>--verbose</code></dt>
<dd> <p> Equivalent to <code>-v</code>. </p>
 </dd>
<dt><code>--version</code></dt>
<dd> <p> Show version information for this instance of <code>bash</code> on the standard output and exit successfully. </p>
 </dd></dl>
<h2>ARGUMENTS</h2>
<p> If arguments remain after option processing, and neither the <code>-c</code> nor the <code>-s</code> option has been supplied, the first argument is assumed to be the name of a file containing shell commands. If <code>bash</code> is invoked in this fashion, <code>$0</code> is set to the name of the file, and the positional parameters are set to the remaining arguments. <code>Bash</code> reads and executes commands from this file, then exits. <code>Bash</code>&#8216;s exit status is the exit status of the last command executed in the script. If no commands are executed, the exit status is 0. An attempt is first made to open the file in the current directory, and, if no file is found, then the shell searches the directories in <font SIZE="-1"><code>PATH</code> </font> for the script.  </p>
<h2>INVOCATION</h2>
<p> A <i>login shell</i> is one whose first character of argument zero is a <code>-</code>, or one started with the <code>--login</code> option. </p>
<p> An <i>interactive</i> shell is one started without non-option arguments (unless <code>-s</code> is specified) and without the <code>-c</code> option whose standard input and error are both connected to terminals (as determined by <i><a href="/docs/linux/man/3-isatty/">isatty</a></i>(3)), or one started with the <code>-i</code> option. <font SIZE="-1"><code>PS1</code> </font> is set and <code>$-</code> includes <code>i</code> if <code>bash</code> is interactive, allowing a shell script or a startup file to test this state. </p>
<p> The following paragraphs describe how <code>bash</code> executes its startup files. If any of the files exist but cannot be read, <code>bash</code> reports an error. Tildes are expanded in filenames as described below under <code>Tilde Expansion</code> in the <font SIZE="-1"><code>EXPANSION</code> </font> section. </p>
<p> When <code>bash</code> is invoked as an interactive login shell, or as a non-interactive shell with the <code>--login</code> option, it first reads and executes commands from the file <i>/etc/profile</i>, if that file exists. After reading that file, it looks for <i>~/.bash_profile</i>, <i>~/.bash_login</i>, and <i>~/.profile</i>, in that order, and reads and executes commands from the first one that exists and is readable. The <code>--noprofile</code> option may be used when the shell is started to inhibit this behavior. </p>
<p> When an interactive login shell exits, or a non-interactive login shell executes the <code>exit</code> builtin command, <code>bash</code> reads and executes commands from the file <i>~/.bash_logout</i>, if it exists. </p>
<p> When an interactive shell that is not a login shell is started, <code>bash</code> reads and executes commands from <i>/etc/bash.bashrc</i> and <i>~/.bashrc</i>, if these files exist. This may be inhibited by using the <code>--norc</code> option. The <code>--rcfile</code> <i>file</i> option will force <code>bash</code> to read and execute commands from <i>file</i> instead of <i>/etc/bash.bashrc</i> and <i>~/.bashrc</i>. </p>
<p> When <code>bash</code> is started non-interactively, to run a shell script, for example, it looks for the variable <font SIZE="-1"><code>BASH_ENV</code> </font> in the environment, expands its value if it appears there, and uses the expanded value as the name of a file to read and execute. <code>Bash</code> behaves as if the following command were executed: </p>
<dl>
<dd> <p> if [ -n &quot;$BASH_ENV&quot; ]; then . &quot;$BASH_ENV&quot;; fi </p>
 </dd></dl>
<p> but the value of the <font SIZE="-1"><code>PATH</code> </font> variable is not used to search for the filename. </p>
<p> If <code>bash</code> is invoked with the name <code>sh</code>, it tries to mimic the startup behavior of historical versions of <code>sh</code> as closely as possible, while conforming to the POSIX standard as well. When invoked as an interactive login shell, or a non-interactive shell with the <code>--login</code> option, it first attempts to read and execute commands from <i>/etc/profile</i> and <i>~/.profile</i>, in that order. The <code>--noprofile</code> option may be used to inhibit this behavior. When invoked as an interactive shell with the name <code>sh</code>, <code>bash</code> looks for the variable <font SIZE="-1"><code>ENV</code>, </font> expands its value if it is defined, and uses the expanded value as the name of a file to read and execute. Since a shell invoked as <code>sh</code> does not attempt to read and execute commands from any other startup files, the <code>--rcfile</code> option has no effect. A non-interactive shell invoked with the name <code>sh</code> does not attempt to read any other startup files. When invoked as <code>sh</code>, <code>bash</code> enters <i>posix</i> mode after the startup files are read. </p>
<p> When <code>bash</code> is started in <i>posix</i> mode, as with the <code>--posix</code> command line option, it follows the POSIX standard for startup files. In this mode, interactive shells expand the <font SIZE="-1"><code>ENV</code> </font> variable and commands are read and executed from the file whose name is the expanded value. No other startup files are read. </p>
<p> <code>Bash</code> attempts to determine when it is being run with its standard input connected to a network connection, as when executed by the remote shell daemon, usually <i>rshd</i>, or the secure shell daemon <i>sshd</i>. If <code>bash</code> determines it is being run in this fashion, it reads and executes commands from <i>~/.bashrc</i> and <i>~/.bashrc</i>, if these files exist and are readable. It will not do this if invoked as <code>sh</code>. The <code>--norc</code> option may be used to inhibit this behavior, and the <code>--rcfile</code> option may be used to force another file to be read, but neither <i>rshd</i> nor <i>sshd</i> generally invoke the shell with those options or allow them to be specified. </p>
<p> If the shell is started with the effective user (group) id not equal to the real user (group) id, and the <code>-p</code> option is not supplied, no startup files are read, shell functions are not inherited from the environment, the <font SIZE="-1"><code>SHELLOPTS</code>, </font> <font SIZE="-1"><code>BASHOPTS</code>, </font> <font SIZE="-1"><code>CDPATH</code>, </font> and <font SIZE="-1"><code>GLOBIGNORE</code> </font> variables, if they appear in the environment, are ignored, and the effective user id is set to the real user id. If the <code>-p</code> option is supplied at invocation, the startup behavior is the same, but the effective user id is not reset.  </p>
<h2>DEFINITIONS</h2>
<p> The following definitions are used throughout the rest of this document. </p>
<dl>
<dt><code>blank</code></dt>
<dd> <p> A space or tab. </p>
 </dd>
<dt><code>word</code></dt>
<dd> <p> A sequence of characters considered as a single unit by the shell. Also known as a <code>token</code>. </p>
 </dd>
<dt><code>name</code></dt>
<dd> <p> A <i>word</i> consisting only of alphanumeric characters and underscores, and beginning with an alphabetic character or an underscore. Also referred to as an <code>identifier</code>. </p>
 </dd>
<dt><code>metacharacter</code></dt>
<dd> <p> A character that, when unquoted, separates words. One of the following: <br />
 </p>
 </dd>
<dl>
<dd> <p> <code>| &amp; ; ( ) &lt; &gt; space tab newline</code> </p>
 </dd></dl>
<dt><code>control operator</code></dt>
<dd> <p> A <i>token</i> that performs a control function. It is one of the following symbols: </p>
 </dd>
<dl>
<dd> <p> <code>|| &amp; &amp;&amp; ; ;; ;&amp; ;;&amp; ( ) | |&amp; &lt;newline&gt;</code> </p>
 </dd></dl>
</dl>
<h2>RESERVED WORDS</h2>
<p> <i>Reserved words</i> are words that have a special meaning to the shell. The following words are recognized as reserved when unquoted and either the first word of a command (see <font SIZE="-1"><code>SHELL GRAMMAR</code> </font> below), the third word of a <code>case</code> or <code>select</code> command (only <code>in</code> is valid), or the third word of a <code>for</code> command (only <code>in</code> and <code>do</code> are valid): </p>
<p> <code>! case coproc do done elif else esac fi for function if in select then until while { } time [[ ]] </code>  </p>
<h2>SHELL GRAMMAR</h2>
<h3>Simple Commands</h3>
<p> A <i>simple command</i> is a sequence of optional variable assignments followed by <code>blank</code>-separated words and redirections, and terminated by a <i>control operator</i>. The first word specifies the command to be executed, and is passed as argument zero. The remaining words are passed as arguments to the invoked command. </p>
<p> The return value of a <i>simple command</i> is its exit status, or 128+<i>n</i> if the command is terminated by signal <i>n</i>.  </p>
<h3>Pipelines</h3>
<p> A <i>pipeline</i> is a sequence of one or more commands separated by one of the control operators <code>|</code> or <code>|&amp;</code>. The format for a pipeline is: </p>
<dl>
<dd> <p> [<code>time</code> [<code>-p</code>]] [ ! ] <i>command</i> [ [<code>|</code>|<code>|&amp;</code>] <i>command2</i> ... ] </p>
 </dd></dl>
<p> The standard output of <i>command</i> is connected via a pipe to the standard input of <i>command2</i>. This connection is performed before any redirections specified by the command (see <font SIZE="-1"><code>REDIRECTION</code> </font> below). If <code>|&amp;</code> is used, <i>command</i>&#8216;s standard error, in addition to its standard output, is connected to <i>command2</i>&#8216;s standard input through the pipe; it is shorthand for <code>2&gt;&amp;1 |</code>. This implicit redirection of the standard error to the standard output is performed after any redirections specified by the command. </p>
<p> The return status of a pipeline is the exit status of the last command, unless the <code>pipefail</code> option is enabled. If <code>pipefail</code> is enabled, the pipeline&#8217;s return status is the value of the last (rightmost) command to exit with a non-zero status, or zero if all commands exit successfully. If the reserved word <code>!</code> precedes a pipeline, the exit status of that pipeline is the logical negation of the exit status as described above. The shell waits for all commands in the pipeline to terminate before returning a value. </p>
<p> If the <code>time</code> reserved word precedes a pipeline, the elapsed as well as user and system time consumed by its execution are reported when the pipeline terminates. The <code>-p</code> option changes the output format to that specified by POSIX. When the shell is in <i>posix mode</i>, it does not recognize <code>time</code> as a reserved word if the next token begins with a `-&#8216;. The <font SIZE="-1"><code>TIMEFORMAT</code> </font> variable may be set to a format string that specifies how the timing information should be displayed; see the description of <font SIZE="-1"><code>TIMEFORMAT</code> </font> under <code>Shell Variables</code> below. </p>
<p> When the shell is in <i>posix mode</i>, <code>time</code> may be followed by a newline. In this case, the shell displays the total user and system time consumed by the shell and its children. The <font SIZE="-1"><code>TIMEFORMAT</code> </font> variable may be used to specify the format of the time information. </p>
<p> Each command in a pipeline is executed as a separate process (i.e., in a subshell). See <font SIZE="-1"><code>COMMAND EXECUTION ENVIRONMENT</code></font> for a description of a subshell environment. If the <code>lastpipe</code> option is enabled using the <code>shopt</code> builtin (see the description of <code>shopt</code> below), the last element of a pipeline may be run by the shell process.  </p>
<h3>Lists</h3>
<p> A <i>list</i> is a sequence of one or more pipelines separated by one of the operators <code>;</code>, <code>&amp;</code>, <code>&amp;&amp;</code>, or <code>||</code>, and optionally terminated by one of <code>;</code>, <code>&amp;</code>, or <code>&lt;newline&gt;</code>. </p>
<p> Of these list operators, <code>&amp;&amp;</code> and <code>||</code> have equal precedence, followed by <code>;</code> and <code>&amp;</code>, which have equal precedence. </p>
<p> A sequence of one or more newlines may appear in a <i>list</i> instead of a semicolon to delimit commands. </p>
<p> If a command is terminated by the control operator <code>&amp;</code>, the shell executes the command in the <i>background</i> in a subshell. The shell does not wait for the command to finish, and the return status is 0. These are referred to as <i>asynchronous</i> commands. Commands separated by a <code>;</code> are executed sequentially; the shell waits for each command to terminate in turn. The return status is the exit status of the last command executed. </p>
<p> AND and OR lists are sequences of one or more pipelines separated by the <code>&amp;&amp;</code> and <code>||</code> control operators, respectively. AND and OR lists are executed with left associativity. An AND list has the form </p>
<dl>
<dd> <p> <i>command1</i> <code>&amp;&amp;</code> <i>command2</i> </p>
 </dd></dl>
<p> <i>command2</i> is executed if, and only if, <i>command1</i> returns an exit status of zero (success). </p>
<p> An OR list has the form </p>
<dl>
<dd> <p> <i>command1</i> <code>||</code> <i>command2</i> </p>
 </dd></dl>
<p> <i>command2</i> is executed if, and only if, <i>command1</i> returns a non-zero exit status. The return status of AND and OR lists is the exit status of the last command executed in the list.  </p>
<h3>Compound Commands</h3>
<p> A <i>compound command</i> is one of the following. In most cases a <i>list</i> in a command&#8217;s description may be separated from the rest of the command by one or more newlines, and may be followed by a newline in place of a semicolon. </p>
<dl>
<dt>(<i>list</i>)</dt>
<dd> <p> <i>list</i> is executed in a subshell environment (see <font SIZE="-1"><code>COMMAND EXECUTION ENVIRONMENT</code></font> below). Variable assignments and builtin commands that affect the shell&#8217;s environment do not remain in effect after the command completes. The return status is the exit status of <i>list</i>. </p>
 </dd>
<dt>{ <i>list</i>; }</dt>
<dd> <p> <i>list</i> is simply executed in the current shell environment. <i>list</i> must be terminated with a newline or semicolon. This is known as a <i>group command</i>. The return status is the exit status of <i>list</i>. Note that unlike the metacharacters <code>(</code> and <code>)</code>, <code>{</code> and <code>}</code> are <i>reserved words</i> and must occur where a reserved word is permitted to be recognized. Since they do not cause a word break, they must be separated from <i>list</i> by whitespace or another shell metacharacter. </p>
 </dd>
<dt>((<i>expression</i>))</dt>
<dd> <p> The <i>expression</i> is evaluated according to the rules described below under <font SIZE="-1"><code>ARITHMETIC</code>EVALUATION <code>.</code> </font> If the value of the expression is non-zero, the return status is 0; otherwise the return status is 1. This is exactly equivalent to <code>let &quot;</code><i>expression</i>&quot;. </p>
 </dd>
<dt><code>[[</code><i>expression</i><code>]]</code></dt>
<dd> <p> Return a status of 0 or 1 depending on the evaluation of the conditional expression <i>expression</i>. Expressions are composed of the primaries described below under <font SIZE="-1"><code>CONDITIONAL</code>EXPRESSIONS <code>.</code> </font> Word splitting and pathname expansion are not performed on the words between the <code>[[</code> and <code>]]</code>; tilde expansion, parameter and variable expansion, arithmetic expansion, command substitution, process substitution, and quote removal are performed. Conditional operators such as <code>-f</code> must be unquoted to be recognized as primaries. </p>
<p> When used with <code>[[</code>, the <code>&lt;</code> and <code>&gt;</code> operators sort lexicographically using the current locale. </p>
 </dd></dl>
<p> See the description of the <i>test</i> builtin command (section SHELL BUILTIN COMMANDS below) for the handling of parameters (i.e. missing parameters). </p>
<p> When the <code>==</code> and <code>!=</code> operators are used, the string to the right of the operator is considered a pattern and matched according to the rules described below under <code>Pattern Matching</code>, as if the <code>extglob</code> shell option were enabled. The <code>=</code> operator is equivalent to <code>==</code>. If the <code>nocasematch</code> shell option is enabled, the match is performed without regard to the case of alphabetic characters. The return value is 0 if the string matches (<code>==</code>) or does not match (<code>!=</code>) the pattern, and 1 otherwise. Any part of the pattern may be quoted to force the quoted portion to be matched as a string. </p>
<p> An additional binary operator, <code>=~</code>, is available, with the same precedence as <code>==</code> and <code>!=</code>. When it is used, the string to the right of the operator is considered a POSIX extended regular expression and matched accordingly (using the POSIX <i>regcomp</i> and <i>regexec</i> interfaces usually described in <i><a href="/docs/linux/man/3-regex/">regex</a></i>(3)). The return value is 0 if the string matches the pattern, and 1 otherwise. If the regular expression is syntactically incorrect, the conditional expression&#8217;s return value is 2. If the <code>nocasematch</code> shell option is enabled, the match is performed without regard to the case of alphabetic characters. Any part of the pattern may be quoted to force the quoted portion to be matched as a string. Bracket expressions in regular expressions must be treated carefully, since normal quoting characters lose their meanings between brackets. If the pattern is stored in a shell variable, quoting the variable expansion forces the entire pattern to be matched as a string. </p>
<p> The pattern will match if it matches any part of the string. Anchor the pattern using the <code>^</code> and <code>$</code> regular expression operators to force it to match the entire string. The array variable <font SIZE="-1"><code>BASH_REMATCH</code> </font> records which parts of the string matched the pattern. The element of <font SIZE="-1"><code>BASH_REMATCH</code> </font> with index 0 contains the portion of the string matching the entire regular expression. Substrings matched by parenthesized subexpressions within the regular expression are saved in the remaining <font SIZE="-1"><code>BASH_REMATCH</code> </font> indices. The element of <font SIZE="-1"><code>BASH_REMATCH</code> </font> with index <i>n</i> is the portion of the string matching the <i>n</i>th parenthesized subexpression. </p>
<p> Expressions may be combined using the following operators, listed in decreasing order of precedence: </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>( </code><i>expression</i> ) </dt>
<dd> <p> Returns the value of <i>expression</i>. This may be used to override the normal precedence of operators. </p>
 </dd>
<dt><code>! </code><i>expression</i></dt>
<dd> <p> True if <i>expression</i> is false. </p>
 </dd>
<dt><i>expression1</i><code>&amp;&amp;</code><i>expression2</i></dt>
<dd> <p> True if both <i>expression1</i> and <i>expression2</i> are true. </p>
 </dd>
<dt><i>expression1</i><code>||</code><i>expression2</i></dt>
<dd> <p> True if either <i>expression1</i> or <i>expression2</i> is true. </p>
 </dd></dl>
<p> The <code>&amp;&amp;</code> and <code>||</code> operators do not evaluate <i>expression2</i> if the value of <i>expression1</i> is sufficient to determine the return value of the entire conditional expression. </dl>
 </p>
<dl>
<dt><code>for</code><i>name</i> [ [ <code>in</code> [ <i>word ...</i> ] ] ; ] <code>do</code><i>list</i> ; <code>done</code></dt>
<dd> <p> The list of words following <code>in</code> is expanded, generating a list of items. The variable <i>name</i> is set to each element of this list in turn, and <i>list</i> is executed each time. If the <code>in</code> <i>word</i> is omitted, the <code>for</code> command executes <i>list</i> once for each positional parameter that is set (see <font SIZE="-1"><code>PARAMETERS</code> </font> below). The return status is the exit status of the last command that executes. If the expansion of the items following <code>in</code> results in an empty list, no commands are executed, and the return status is 0. </p>
 </dd>
<dt><code>for</code> (( <i>expr1</i> ; <i>expr2</i> ; <i>expr3</i> )) ; <code>do</code><i>list</i> ; <code>done</code></dt>
<dd> <p> First, the arithmetic expression <i>expr1</i> is evaluated according to the rules described below under <font SIZE="-1"><code>ARITHMETIC</code>EVALUATION <code>.</code> </font> The arithmetic expression <i>expr2</i> is then evaluated repeatedly until it evaluates to zero. Each time <i>expr2</i> evaluates to a non-zero value, <i>list</i> is executed and the arithmetic expression <i>expr3</i> is evaluated. If any expression is omitted, it behaves as if it evaluates to 1. The return value is the exit status of the last command in <i>list</i> that is executed, or false if any of the expressions is invalid. </p>
 </dd>
<dt><code>select</code><i>name</i> [ <code>in</code><i>word</i> ] ; <code>do</code><i>list</i> ; <code>done</code></dt>
<dd> <p> The list of words following <code>in</code> is expanded, generating a list of items. The set of expanded words is printed on the standard error, each preceded by a number. If the <code>in</code> <i>word</i> is omitted, the positional parameters are printed (see <font SIZE="-1"><code>PARAMETERS</code> </font> below). The <font SIZE="-1"><code>PS3</code> </font> prompt is then displayed and a line read from the standard input. If the line consists of a number corresponding to one of the displayed words, then the value of <i>name</i> is set to that word. If the line is empty, the words and prompt are displayed again. If EOF is read, the command completes. Any other value read causes <i>name</i> to be set to null. The line read is saved in the variable <font SIZE="-1"><code>REPLY</code>. </font> The <i>list</i> is executed after each selection until a <code>break</code> command is executed. The exit status of <code>select</code> is the exit status of the last command executed in <i>list</i>, or zero if no commands were executed. </p>
 </dd>
<dt><code>case</code><i>word</i><code>in</code> [ [(] <i>pattern</i> [ <code>|</code><i>pattern</i> ] </dt>
<dd> <p> A <code>case</code> command first expands <i>word</i>, and tries to match it against each <i>pattern</i> in turn, using the matching rules described under <code>Pattern Matching</code> below. The <i>word</i> is expanded using tilde expansion, parameter and variable expansion, arithmetic expansion, command substitution, process substitution and quote removal. Each <i>pattern</i> examined is expanded using tilde expansion, parameter and variable expansion, arithmetic expansion, command substitution, and process substitution. If the <code>nocasematch</code> shell option is enabled, the match is performed without regard to the case of alphabetic characters. When a match is found, the corresponding <i>list</i> is executed. If the <code>;;</code> operator is used, no subsequent matches are attempted after the first pattern match. Using <code>;&amp;</code> in place of <code>;;</code> causes execution to continue with the <i>list</i> associated with the next set of patterns. Using <code>;;&amp;</code> in place of <code>;;</code> causes the shell to test the next pattern list in the statement, if any, and execute any associated <i>list</i> on a successful match, continuing the case statement execution as if the pattern list had not matched. The exit status is zero if no pattern matches. Otherwise, it is the exit status of the last command executed in <i>list</i>. </p>
 </dd>
<dt><code>if</code><i>list</i>; <code>then</code><i>list</i>; [ <code>elif</code><i>list</i>; <code>then</code><i>list</i>; ] ... [ <code>else</code><i>list</i>; ] <code>fi</code></dt>
<dd> <p> The <code>if</code> <i>list</i> is executed. If its exit status is zero, the <code>then</code> <i>list</i> is executed. Otherwise, each <code>elif</code> <i>list</i> is executed in turn, and if its exit status is zero, the corresponding <code>then</code> <i>list</i> is executed and the command completes. Otherwise, the <code>else</code> <i>list</i> is executed, if present. The exit status is the exit status of the last command executed, or zero if no condition tested true. </p>
 </dd>
<dt><code>while</code><i>list-1</i>; <code>do</code><i>list-2</i>; <code>done</code></dt>
<dd>  </dd>
<dt><code>until</code><i>list-1</i>; <code>do</code><i>list-2</i>; <code>done</code></dt>
<dd> <p> The <code>while</code> command continuously executes the list <i>list-2</i> as long as the last command in the list <i>list-1</i> returns an exit status of zero. The <code>until</code> command is identical to the <code>while</code> command, except that the test is negated: <i>list-2</i> is executed as long as the last command in <i>list-1</i> returns a non-zero exit status. The exit status of the <code>while</code> and <code>until</code> commands is the exit status of the last command executed in <i>list-2</i>, or zero if none was executed. </p>
 </dd></dl>
<h3>Coprocesses</h3>
<p> A <i>coprocess</i> is a shell command preceded by the <code>coproc</code> reserved word. A coprocess is executed asynchronously in a subshell, as if the command had been terminated with the <code>&amp;</code> control operator, with a two-way pipe established between the executing shell and the coprocess. </p>
<p> The format for a coprocess is: </p>
<dl>
<dd> <p> <code>coproc</code> [<i>NAME</i>] <i>command</i> [<i>redirections</i>] </p>
 </dd></dl>
<p> This creates a coprocess named <i>NAME</i>. If <i>NAME</i> is not supplied, the default name is <code>COPROC</code>. <i>NAME</i> must not be supplied if <i>command</i> is a <i>simple command</i> (see above); otherwise, it is interpreted as the first word of the simple command. When the coprocess is executed, the shell creates an array variable (see <code>Arrays</code> below) named <i>NAME</i> in the context of the executing shell. The standard output of <i>command</i> is connected via a pipe to a file descriptor in the executing shell, and that file descriptor is assigned to <i>NAME</i>[0]. The standard input of <i>command</i> is connected via a pipe to a file descriptor in the executing shell, and that file descriptor is assigned to <i>NAME</i>[1]. This pipe is established before any redirections specified by the command (see <font SIZE="-1"><code>REDIRECTION</code> </font> below). The file descriptors can be utilized as arguments to shell commands and redirections using standard word expansions. Other than those created to execute command and process substitutions, the file descriptors are not available in subshells. The process ID of the shell spawned to execute the coprocess is available as the value of the variable <i>NAME</i>_PID. The <code>wait</code> builtin command may be used to wait for the coprocess to terminate. </p>
<p> Since the coprocess is created as an asynchronous command, the <code>coproc</code> command always returns success. The return status of a coprocess is the exit status of <i>command</i>.  </p>
<h3>Shell Function Definitions</h3>
<p> A shell function is an object that is called like a simple command and executes a compound command with a new set of positional parameters. Shell functions are declared as follows: </p>
<dl>
<dt><i>fname</i> () <i>compound-command</i> [<i>redirection</i>]</dt>
<dd>  </dd>
<dt><code>function</code><i>fname</i> [()] <i>compound-command</i> [<i>redirection</i>]</dt>
<dd> <p> This defines a function named <i>fname</i>. The reserved word <code>function</code> is optional. If the <code>function</code> reserved word is supplied, the parentheses are optional. The <i>body</i> of the function is the compound command <i>compound-command</i> (see <code>Compound Commands</code> above). That command is usually a <i>list</i> of commands between { and }, but may be any command listed under <code>Compound Commands</code> above, with one exception: If the <code>function</code> reserved word is used, but the parentheses are not supplied, the braces are required. <i>compound-command</i> is executed whenever <i>fname</i> is specified as the name of a simple command. When in <i>posix mode</i>, <i>fname</i> must be a valid shell <i>name</i> and may not be the name of one of the POSIX <i>special builtins</i>. In default mode, a function name can be any unquoted shell word that does not contain <code>$</code>. Any redirections (see <font SIZE="-1"><code>REDIRECTION</code> </font> below) specified when a function is defined are performed when the function is executed. The exit status of a function definition is zero unless a syntax error occurs or a readonly function with the same name already exists. When executed, the exit status of a function is the exit status of the last command executed in the body. (See <font SIZE="-1"><code>FUNCTIONS</code> </font> below.) </p>
 </dd></dl>
<h2>COMMENTS</h2>
<p> In a non-interactive shell, or an interactive shell in which the <code>interactive_comments</code> option to the <code>shopt</code> builtin is enabled (see <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below), a word beginning with <code>#</code> causes that word and all remaining characters on that line to be ignored. An interactive shell without the <code>interactive_comments</code> option enabled does not allow comments. The <code>interactive_comments</code> option is on by default in interactive shells.  </p>
<h2>QUOTING</h2>
<p> <i>Quoting</i> is used to remove the special meaning of certain characters or words to the shell. Quoting can be used to disable special treatment for special characters, to prevent reserved words from being recognized as such, and to prevent parameter expansion. </p>
<p> Each of the <i>metacharacters</i> listed above under <font SIZE="-1"><code>DEFINITIONS</code> </font> has special meaning to the shell and must be quoted if it is to represent itself. </p>
<p> When the command history expansion facilities are being used (see <font SIZE="-1"><code>HISTORY EXPANSION</code> </font> below), the <i>history expansion</i> character, usually <code>!</code>, must be quoted to prevent history expansion. </p>
<p> There are three quoting mechanisms: the <i>escape character</i>, single quotes, and double quotes. </p>
<p> A non-quoted backslash (<code>\</code>) is the <i>escape character</i>. It preserves the literal value of the next character that follows, with the exception of &lt;newline&gt;. If a <code>\</code>&lt;newline&gt; pair appears, and the backslash is not itself quoted, the <code>\</code>&lt;newline&gt; is treated as a line continuation (that is, it is removed from the input stream and effectively ignored). </p>
<p> Enclosing characters in single quotes preserves the literal value of each character within the quotes. A single quote may not occur between single quotes, even when preceded by a backslash. </p>
<p> Enclosing characters in double quotes preserves the literal value of all characters within the quotes, with the exception of <code>$</code>, <code>`</code>, <code>\</code>, and, when history expansion is enabled, <code>!</code>. When the shell is in <i>posix mode</i>, the <code>!</code> has no special meaning within double quotes, even when history expansion is enabled. The characters <code>$</code> and <code>`</code> retain their special meaning within double quotes. The backslash retains its special meaning only when followed by one of the following characters: <code>$</code>, <code>`</code>, <code>&quot;</code>, <code>\</code>, or <code>&lt;newline&gt;</code>. A double quote may be quoted within double quotes by preceding it with a backslash. If enabled, history expansion will be performed unless an <code>!</code> appearing in double quotes is escaped using a backslash. The backslash preceding the <code>!</code> is not removed. </p>
<p> The special parameters <code>*</code> and <code>@</code> have special meaning when in double quotes (see <font SIZE="-1"><code>PARAMETERS</code> </font> below). </p>
<p> Words of the form <code>$</code>&#8216;<i>string</i>&#8216; are treated specially. The word expands to <i>string</i>, with backslash-escaped characters replaced as specified by the ANSI C standard. Backslash escape sequences, if present, are decoded as follows: </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>\a</code></dt>
<dd> <p> alert (bell) </p>
 </dd>
<dt><code>\b</code></dt>
<dd> <p> backspace </p>
 </dd>
<dt><code>\e</code></dt>
<dd>  </dd>
<dt><code>\E</code></dt>
<dd> <p> an escape character </p>
 </dd>
<dt><code>\f</code></dt>
<dd> <p> form feed </p>
 </dd>
<dt><code>\n</code></dt>
<dd> <p> new line </p>
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
<dt><code>\&#8216;</code></dt>
<dd> <p> single quote </p>
 </dd>
<dt><code>\&quot;</code></dt>
<dd> <p> double quote </p>
 </dd>
<dt><code>\?</code></dt>
<dd> <p> question mark </p>
 </dd>
<dt><code>\</code><i>nnn</i></dt>
<dd> <p> the eight-bit character whose value is the octal value <i>nnn</i> (one to three octal digits) </p>
 </dd>
<dt><code>\x</code><i>HH</i></dt>
<dd> <p> the eight-bit character whose value is the hexadecimal value <i>HH</i> (one or two hex digits) </p>
 </dd>
<dt><code>\u</code><i>HHHH</i></dt>
<dd> <p> the Unicode (ISO/IEC 10646) character whose value is the hexadecimal value <i>HHHH</i> (one to four hex digits) </p>
 </dd>
<dt><code>\U</code><i>HHHHHHHH</i></dt>
<dd> <p> the Unicode (ISO/IEC 10646) character whose value is the hexadecimal value <i>HHHHHHHH</i> (one to eight hex digits) </p>
 </dd>
<dt><code>\c</code><i>x</i></dt>
<dd> <p> a control-<i>x</i> character </p>
 </dd></dl>
</dl>
<p> The expanded result is single-quoted, as if the dollar sign had not been present. </p>
<p> A double-quoted string preceded by a dollar sign (<code>$</code>&quot;<i>string</i>&quot;) will cause the string to be translated according to the current locale. The <i>gettext</i> infrastructure performs the message catalog lookup and translation, using the <code>LC_MESSAGES</code> and <code>TEXTDOMAIN</code> shell variables. If the current locale is <code>C</code> or <code>POSIX</code>, or if there are no translations available, the dollar sign is ignored. If the string is translated and replaced, the replacement is double-quoted.  </p>
<h2>PARAMETERS</h2>
<p> A <i>parameter</i> is an entity that stores values. It can be a <i>name</i>, a number, or one of the special characters listed below under <code>Special Parameters</code>. A <i>variable</i> is a parameter denoted by a <i>name</i>. A variable has a <i>value</i> and zero or more <i>attributes</i>. Attributes are assigned using the <code>declare</code> builtin command (see <code>declare</code> below in <font SIZE="-1"><code>SHELL</code>BUILTIN <code>COMMANDS</code>). </font> </p>
<p> A parameter is set if it has been assigned a value. The null string is a valid value. Once a variable is set, it may be unset only by using the <code>unset</code> builtin command (see <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below). </p>
<p> A <i>variable</i> may be assigned to by a statement of the form </p>
<dl>
<dd> <p> <i>name</i>=[<i>value</i>] </p>
 </dd></dl>
<p> If <i>value</i> is not given, the variable is assigned the null string. All <i>values</i> undergo tilde expansion, parameter and variable expansion, command substitution, arithmetic expansion, and quote removal (see <font SIZE="-1"><code>EXPANSION</code> </font> below). If the variable has its <code>integer</code> attribute set, then <i>value</i> is evaluated as an arithmetic expression even if the $((...)) expansion is not used (see <code>Arithmetic Expansion</code> below). Word splitting is not performed, with the exception of <code>&quot;$@&quot;</code> as explained below under <code>Special Parameters</code>. Pathname expansion is not performed. Assignment statements may also appear as arguments to the <code>alias</code>, <code>declare</code>, <code>typeset</code>, <code>export</code>, <code>readonly</code>, and <code>local</code> builtin commands (<i>declaration</i> commands). When in <i>posix mode</i>, these builtins may appear in a command after one or more instances of the <code>command</code> builtin and retain these assignment statement properties. </p>
<p> In the context where an assignment statement is assigning a value to a shell variable or array index, the += operator can be used to append to or add to the variable&#8217;s previous value. This includes arguments to builtin commands such as <code>declare</code> that accept assignment statements (<i>declaration</i> commands). When += is applied to a variable for which the <i>integer</i> attribute has been set, <i>value</i> is evaluated as an arithmetic expression and added to the variable&#8217;s current value, which is also evaluated. When += is applied to an array variable using compound assignment (see <code>Arrays</code> below), the variable&#8217;s value is not unset (as it is when using =), and new values are appended to the array beginning at one greater than the array&#8217;s maximum index (for indexed arrays) or added as additional key-value pairs in an associative array. When applied to a string-valued variable, <i>value</i> is expanded and appended to the variable&#8217;s value. </p>
<p> A variable can be assigned the <i>nameref</i> attribute using the <code>-n</code> option to the <code>declare</code> or <code>local</code> builtin commands (see the descriptions of <code>declare</code> and <code>local</code> below) to create a <i>nameref</i>, or a reference to another variable. This allows variables to be manipulated indirectly. Whenever the nameref variable is referenced, assigned to, unset, or has its attributes modified (other than using or changing the <i>nameref</i> attribute itself), the operation is actually performed on the variable specified by the nameref variable&#8217;s value. A nameref is commonly used within shell functions to refer to a variable whose name is passed as an argument to the function. For instance, if a variable name is passed to a shell function as its first argument, running </p>
<dl>
<dd> <p> declare -n ref=$1 </p>
 </dd></dl>
<p> inside the function creates a nameref variable <code>ref</code> whose value is the variable name passed as the first argument. References and assignments to <code>ref</code>, and changes to its attributes, are treated as references, assignments, and attribute modifications to the variable whose name was passed as <code>$1</code>. If the control variable in a <code>for</code> loop has the nameref attribute, the list of words can be a list of shell variables, and a name reference will be established for each word in the list, in turn, when the loop is executed. Array variables cannot be given the <code>nameref</code> attribute. However, nameref variables can reference array variables and subscripted array variables. Namerefs can be unset using the <code>-n</code> option to the <code>unset</code> builtin. Otherwise, if <code>unset</code> is executed with the name of a nameref variable as an argument, the variable referenced by the nameref variable will be unset.  </p>
<h3>Positional Parameters</h3>
<p> A <i>positional parameter</i> is a parameter denoted by one or more digits, other than the single digit 0. Positional parameters are assigned from the shell&#8217;s arguments when it is invoked, and may be reassigned using the <code>set</code> builtin command. Positional parameters may not be assigned to with assignment statements. The positional parameters are temporarily replaced when a shell function is executed (see <font SIZE="-1"><code>FUNCTIONS</code> </font> below). </p>
<p> When a positional parameter consisting of more than a single digit is expanded, it must be enclosed in braces (see <font SIZE="-1"><code>EXPANSION</code> </font> below).  </p>
<h3>Special Parameters</h3>
<p> The shell treats several parameters specially. These parameters may only be referenced; assignment to them is not allowed. </p>
<dl>
<dt><code>*</code></dt>
<dd> <p> Expands to the positional parameters, starting from one. When the expansion is not within double quotes, each positional parameter expands to a separate word. In contexts where it is performed, those words are subject to further word splitting and pathname expansion. When the expansion occurs within double quotes, it expands to a single word with the value of each parameter separated by the first character of the <font SIZE="-1"><code>IFS</code> </font> special variable. That is, &quot;<code>$*</code>&quot; is equivalent to &quot;<code>$1</code><i>c</i><code>$2</code><i>c</i><code>...</code>&quot;, where <i>c</i> is the first character of the value of the <font SIZE="-1"><code>IFS</code> </font> variable. If <font SIZE="-1"><code>IFS</code> </font> is unset, the parameters are separated by spaces. If <font SIZE="-1"><code>IFS</code> </font> is null, the parameters are joined without intervening separators. </p>
 </dd>
<dt><code>@</code></dt>
<dd> <p> Expands to the positional parameters, starting from one. In contexts where word splitting is performed, this expands each positional parameter to a separate word; if not within double quotes, these words are subject to word splitting. In contexts where word splitting is not performed, this expands to a single word with each positional parameter separated by a space. When the expansion occurs within double quotes, each parameter expands to a separate word. That is, &quot;<code>$@</code>&quot; is equivalent to &quot;<code>$1</code>&quot; &quot;<code>$2</code>&quot; ... If the double-quoted expansion occurs within a word, the expansion of the first parameter is joined with the beginning part of the original word, and the expansion of the last parameter is joined with the last part of the original word. When there are no positional parameters, &quot;<code>$@</code>&quot; and <code>$@</code> expand to nothing (i.e., they are removed). </p>
 </dd>
<dt><code>#</code></dt>
<dd> <p> Expands to the number of positional parameters in decimal. </p>
 </dd>
<dt><code>?</code></dt>
<dd> <p> Expands to the exit status of the most recently executed foreground pipeline. </p>
 </dd>
<dt><code>-</code></dt>
<dd> <p> Expands to the current option flags as specified upon invocation, by the <code>set</code> builtin command, or those set by the shell itself (such as the <code>-i</code> option). </p>
 </dd>
<dt><code>$</code></dt>
<dd> <p> Expands to the process ID of the shell. In a () subshell, it expands to the process ID of the current shell, not the subshell. </p>
 </dd>
<dt><code>!</code></dt>
<dd> <p> Expands to the process ID of the job most recently placed into the background, whether executed as an asynchronous command or using the <code>bg</code> builtin (see <font SIZE="-1"><code>JOB CONTROL</code> </font> below). </p>
 </dd>
<dt><code>0</code></dt>
<dd> <p> Expands to the name of the shell or shell script. This is set at shell initialization. If <code>bash</code> is invoked with a file of commands, <code>$0</code> is set to the name of that file. If <code>bash</code> is started with the <code>-c</code> option, then <code>$0</code> is set to the first argument after the string to be executed, if one is present. Otherwise, it is set to the filename used to invoke <code>bash</code>, as given by argument zero. </p>
 </dd></dl>
<h3>Shell Variables</h3>
<p> The following variables are set by the shell: </p>
<dl>
<dt><code>_</code></dt>
<dd> <p> At shell startup, set to the pathname used to invoke the shell or shell script being executed as passed in the environment or argument list. Subsequently, expands to the last argument to the previous simple command executed in the foreground, after expansion. Also set to the full pathname used to invoke each command executed and placed in the environment exported to that command. When checking mail, this parameter holds the name of the mail file currently being checked. </p>
 </dd>
<dt><code>BASH</code></dt>
<dd> <p> Expands to the full filename used to invoke this instance of <code>bash</code>. </p>
 </dd>
<dt><code>BASHOPTS</code></dt>
<dd> <p> A colon-separated list of enabled shell options. Each word in the list is a valid argument for the <code>-s</code> option to the <code>shopt</code> builtin command (see <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below). The options appearing in <font SIZE="-1"><code>BASHOPTS</code> </font> are those reported as <i>on</i> by <code>shopt</code>. If this variable is in the environment when <code>bash</code> starts up, each shell option in the list will be enabled before reading any startup files. This variable is read-only. </p>
 </dd>
<dt><code>BASHPID</code></dt>
<dd> <p> Expands to the process ID of the current <code>bash</code> process. This differs from <code>$$</code> under certain circumstances, such as subshells that do not require <code>bash</code> to be re-initialized. Assignments to <font SIZE="-1"><code>BASHPID</code> </font> have no effect. If <code>BASHPID</code> is unset, it loses its special properties, even if it is subsequently reset. </p>
 </dd>
<dt><code>BASH_ALIASES</code></dt>
<dd> <p> An associative array variable whose members correspond to the internal list of aliases as maintained by the <code>alias</code> builtin. Elements added to this array appear in the alias list; however, unsetting array elements currently does not cause aliases to be removed from the alias list. If <code>BASH_ALIASES</code> is unset, it loses its special properties, even if it is subsequently reset. </p>
 </dd>
<dt><code>BASH_ARGC</code></dt>
<dd> <p> An array variable whose values are the number of parameters in each frame of the current <code>bash</code> execution call stack. The number of parameters to the current subroutine (shell function or script executed with <code>.</code> or <code>source</code>) is at the top of the stack. When a subroutine is executed, the number of parameters passed is pushed onto <font SIZE="-1"><code>BASH_ARGC</code>. </font> The shell sets <font SIZE="-1"><code>BASH_ARGC</code> </font> only when in extended debugging mode (see the description of the <code>extdebug</code> option to the <code>shopt</code> builtin below). Setting <code>extdebug</code> after the shell has started to execute a script, or referencing this variable when <code>extdebug</code> is not set, may result in inconsistent values. </p>
 </dd>
<dt><code>BASH_ARGV</code></dt>
<dd> <p> An array variable containing all of the parameters in the current <code>bash</code> execution call stack. The final parameter of the last subroutine call is at the top of the stack; the first parameter of the initial call is at the bottom. When a subroutine is executed, the parameters supplied are pushed onto <font SIZE="-1"><code>BASH_ARGV</code>. </font> The shell sets <font SIZE="-1"><code>BASH_ARGV</code> </font> only when in extended debugging mode (see the description of the <code>extdebug</code> option to the <code>shopt</code> builtin below). Setting <code>extdebug</code> after the shell has started to execute a script, or referencing this variable when <code>extdebug</code> is not set, may result in inconsistent values. </p>
 </dd>
<dt><code>BASH_ARGV0</code></dt>
<dd> <p> When referenced, this variable expands to the name of the shell or shell script (identical to <code>$0</code>; see the description of special parameter 0 above). Assignment to <code>BASH_ARGV0</code> causes the value assigned to also be assigned to <code>$0</code>. If <code>BASH_ARGV0</code> is unset, it loses its special properties, even if it is subsequently reset. </p>
 </dd>
<dt><code>BASH_CMDS</code></dt>
<dd> <p> An associative array variable whose members correspond to the internal hash table of commands as maintained by the <code>hash</code> builtin. Elements added to this array appear in the hash table; however, unsetting array elements currently does not cause command names to be removed from the hash table. If <code>BASH_CMDS</code> is unset, it loses its special properties, even if it is subsequently reset. </p>
 </dd>
<dt><code>BASH_COMMAND</code></dt>
<dd> <p> The command currently being executed or about to be executed, unless the shell is executing a command as the result of a trap, in which case it is the command executing at the time of the trap. If <code>BASH_COMMAND</code> is unset, it loses its special properties, even if it is subsequently reset. </p>
 </dd>
<dt><code>BASH_EXECUTION_STRING</code></dt>
<dd> <p> The command argument to the <code>-c</code> invocation option. </p>
 </dd>
<dt><code>BASH_LINENO</code></dt>
<dd> <p> An array variable whose members are the line numbers in source files where each corresponding member of <font SIZE="-1"><code>FUNCNAME</code> </font> was invoked. <code>${BASH_LINENO[</code><i>$i</i><code>]}</code> is the line number in the source file (<code>${BASH_SOURCE[</code><i>$i+1</i><code>]}</code>) where <code>${FUNCNAME[</code><i>$i</i><code>]}</code> was called (or <code>${BASH_LINENO[</code><i>$i-1</i><code>]}</code> if referenced within another shell function). Use <font SIZE="-1"><code>LINENO</code> </font> to obtain the current line number. </p>
 </dd>
<dt><code>BASH_LOADABLES_PATH</code></dt>
<dd> <p> A colon-separated list of directories in which the shell looks for dynamically loadable builtins specified by the <code>enable</code> command. </p>
 </dd>
<dt><code>BASH_REMATCH</code></dt>
<dd> <p> An array variable whose members are assigned by the <code>=~</code> binary operator to the <code>[[</code> conditional command. The element with index 0 is the portion of the string matching the entire regular expression. The element with index <i>n</i> is the portion of the string matching the <i>n</i>th parenthesized subexpression. </p>
 </dd>
<dt><code>BASH_SOURCE</code></dt>
<dd> <p> An array variable whose members are the source filenames where the corresponding shell function names in the <font SIZE="-1"><code>FUNCNAME</code> </font> array variable are defined. The shell function <code>${FUNCNAME[</code><i>$i</i><code>]}</code> is defined in the file <code>${BASH_SOURCE[</code><i>$i</i><code>]}</code> and called from <code>${BASH_SOURCE[</code><i>$i+1</i><code>]}</code>. </p>
 </dd>
<dt><code>BASH_SUBSHELL</code></dt>
<dd> <p> Incremented by one within each subshell or subshell environment when the shell begins executing in that environment. The initial value is 0. If <code>BASH_SUBSHELL</code> is unset, it loses its special properties, even if it is subsequently reset. </p>
 </dd>
<dt><code>BASH_VERSINFO</code></dt>
<dd> <p> A readonly array variable whose members hold version information for this instance of <code>bash</code>. The values assigned to the array members are as follows: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>BASH_VERSINFO[</code>0] </dt>
<dd> <p> The major version number (the <i>release</i>). </p>
 </dd>
<dt><code>BASH_VERSINFO[</code>1] </dt>
<dd> <p> The minor version number (the <i>version</i>). </p>
 </dd>
<dt><code>BASH_VERSINFO[</code>2] </dt>
<dd> <p> The patch level. </p>
 </dd>
<dt><code>BASH_VERSINFO[</code>3] </dt>
<dd> <p> The build version. </p>
 </dd>
<dt><code>BASH_VERSINFO[</code>4] </dt>
<dd> <p> The release status (e.g., <i>beta1</i>). </p>
 </dd>
<dt><code>BASH_VERSINFO[</code>5] </dt>
<dd> <p> The value of <font SIZE="-1"><code>MACHTYPE</code>. </font> </p>
 </dd></dl>
</dl>
<dt><code>BASH_VERSION</code></dt>
<dd> <p> Expands to a string describing the version of this instance of <code>bash</code>. </p>
 </dd>
<dt><code>COMP_CWORD</code></dt>
<dd> <p> An index into <code>${COMP_WORDS}</code> of the word containing the current cursor position. This variable is available only in shell functions invoked by the programmable completion facilities (see <code>Programmable Completion</code> below). </p>
 </dd>
<dt><code>COMP_KEY</code></dt>
<dd> <p> The key (or final key of a key sequence) used to invoke the current completion function. </p>
 </dd>
<dt><code>COMP_LINE</code></dt>
<dd> <p> The current command line. This variable is available only in shell functions and external commands invoked by the programmable completion facilities (see <code>Programmable Completion</code> below). </p>
 </dd>
<dt><code>COMP_POINT</code></dt>
<dd> <p> The index of the current cursor position relative to the beginning of the current command. If the current cursor position is at the end of the current command, the value of this variable is equal to <code>${#COMP_LINE}</code>. This variable is available only in shell functions and external commands invoked by the programmable completion facilities (see <code>Programmable Completion</code> below). </p>
 </dd>
<dt><code>COMP_TYPE</code></dt>
<dd> <p> Set to an integer value corresponding to the type of completion attempted that caused a completion function to be called: <i>TAB</i>, for normal completion, <i>?</i>, for listing completions after successive tabs, <i>!</i>, for listing alternatives on partial word completion, <i>@</i>, to list completions if the word is not unmodified, or <i>%</i>, for menu completion. This variable is available only in shell functions and external commands invoked by the programmable completion facilities (see <code>Programmable Completion</code> below). </p>
 </dd>
<dt><code>COMP_WORDBREAKS</code></dt>
<dd> <p> The set of characters that the <code>readline</code> library treats as word separators when performing word completion. If <font SIZE="-1"><code>COMP_WORDBREAKS</code> </font> is unset, it loses its special properties, even if it is subsequently reset. </p>
 </dd>
<dt><code>COMP_WORDS</code></dt>
<dd> <p> An array variable (see <code>Arrays</code> below) consisting of the individual words in the current command line. The line is split into words as <code>readline</code> would split it, using <font SIZE="-1"><code>COMP_WORDBREAKS</code> </font> as described above. This variable is available only in shell functions invoked by the programmable completion facilities (see <code>Programmable Completion</code> below). </p>
 </dd>
<dt><code>COPROC</code></dt>
<dd> <p> An array variable (see <code>Arrays</code> below) created to hold the file descriptors for output from and input to an unnamed coprocess (see <code>Coprocesses</code> above). </p>
 </dd>
<dt><code>DIRSTACK</code></dt>
<dd> <p> An array variable (see <code>Arrays</code> below) containing the current contents of the directory stack. Directories appear in the stack in the order they are displayed by the <code>dirs</code> builtin. Assigning to members of this array variable may be used to modify directories already in the stack, but the <code>pushd</code> and <code>popd</code> builtins must be used to add and remove directories. Assignment to this variable will not change the current directory. If <font SIZE="-1"><code>DIRSTACK</code> </font> is unset, it loses its special properties, even if it is subsequently reset. </p>
 </dd>
<dt><code>EPOCHREALTIME</code></dt>
<dd> <p> Each time this parameter is referenced, it expands to the number of seconds since the Unix Epoch (see <i><a href="/docs/linux/man/3-time/">time</a></i>(3)) as a floating point value with micro-second granularity. Assignments to <font SIZE="-1"><code>EPOCHREALTIME</code> </font> are ignored. If <font SIZE="-1"><code>EPOCHREALTIME</code> </font> is unset, it loses its special properties, even if it is subsequently reset. </p>
 </dd>
<dt><code>EPOCHSECONDS</code></dt>
<dd> <p> Each time this parameter is referenced, it expands to the number of seconds since the Unix Epoch (see <i><a href="/docs/linux/man/3-time/">time</a></i>(3)). Assignments to <font SIZE="-1"><code>EPOCHSECONDS</code> </font> are ignored. If <font SIZE="-1"><code>EPOCHSECONDS</code> </font> is unset, it loses its special properties, even if it is subsequently reset. </p>
 </dd>
<dt><code>EUID</code></dt>
<dd> <p> Expands to the effective user ID of the current user, initialized at shell startup. This variable is readonly. </p>
 </dd>
<dt><code>FUNCNAME</code></dt>
<dd> <p> An array variable containing the names of all shell functions currently in the execution call stack. The element with index 0 is the name of any currently-executing shell function. The bottom-most element (the one with the highest index) is &quot;main&quot;. This variable exists only when a shell function is executing. Assignments to <font SIZE="-1"><code>FUNCNAME</code> </font> have no effect. If <font SIZE="-1"><code>FUNCNAME</code> </font> is unset, it loses its special properties, even if it is subsequently reset. </p>
<p> This variable can be used with <code>BASH_LINENO</code> and <code>BASH_SOURCE</code>. Each element of <code>FUNCNAME</code> has corresponding elements in <code>BASH_LINENO</code> and <code>BASH_SOURCE</code> to describe the call stack. For instance, <code>${FUNCNAME[</code><i>$i</i><code>]}</code> was called from the file <code>${BASH_SOURCE[</code><i>$i+1</i><code>]}</code> at line number <code>${BASH_LINENO[</code><i>$i</i><code>]}</code>. The <code>caller</code> builtin displays the current call stack using this information. </p>
 </dd>
<dt><code>GROUPS</code></dt>
<dd> <p> An array variable containing the list of groups of which the current user is a member. Assignments to <font SIZE="-1"><code>GROUPS</code> </font> have no effect. If <font SIZE="-1"><code>GROUPS</code> </font> is unset, it loses its special properties, even if it is subsequently reset. </p>
 </dd>
<dt><code>HISTCMD</code></dt>
<dd> <p> The history number, or index in the history list, of the current command. Assignments to <font SIZE="-1"><code>HISTCMD</code> </font> are ignored. If <font SIZE="-1"><code>HISTCMD</code> </font> is unset, it loses its special properties, even if it is subsequently reset. </p>
 </dd>
<dt><code>HOSTNAME</code></dt>
<dd> <p> Automatically set to the name of the current host. </p>
 </dd>
<dt><code>HOSTTYPE</code></dt>
<dd> <p> Automatically set to a string that uniquely describes the type of machine on which <code>bash</code> is executing. The default is system-dependent. </p>
 </dd>
<dt><code>LINENO</code></dt>
<dd> <p> Each time this parameter is referenced, the shell substitutes a decimal number representing the current sequential line number (starting with 1) within a script or function. When not in a script or function, the value substituted is not guaranteed to be meaningful. If <font SIZE="-1"><code>LINENO</code> </font> is unset, it loses its special properties, even if it is subsequently reset. </p>
 </dd>
<dt><code>MACHTYPE</code></dt>
<dd> <p> Automatically set to a string that fully describes the system type on which <code>bash</code> is executing, in the standard GNU <i>cpu-company-system</i> format. The default is system-dependent. </p>
 </dd>
<dt><code>MAPFILE</code></dt>
<dd> <p> An array variable (see <code>Arrays</code> below) created to hold the text read by the <code>mapfile</code> builtin when no variable name is supplied. </p>
 </dd>
<dt><code>OLDPWD</code></dt>
<dd> <p> The previous working directory as set by the <code>cd</code> command. </p>
 </dd>
<dt><code>OPTARG</code></dt>
<dd> <p> The value of the last option argument processed by the <code>getopts</code> builtin command (see <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below). </p>
 </dd>
<dt><code>OPTIND</code></dt>
<dd> <p> The index of the next argument to be processed by the <code>getopts</code> builtin command (see <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below). </p>
 </dd>
<dt><code>OSTYPE</code></dt>
<dd> <p> Automatically set to a string that describes the operating system on which <code>bash</code> is executing. The default is system-dependent. </p>
 </dd>
<dt><code>PIPESTATUS</code></dt>
<dd> <p> An array variable (see <code>Arrays</code> below) containing a list of exit status values from the processes in the most-recently-executed foreground pipeline (which may contain only a single command). </p>
 </dd>
<dt><code>PPID</code></dt>
<dd> <p> The process ID of the shell&#8217;s parent. This variable is readonly. </p>
 </dd>
<dt><code>PWD</code></dt>
<dd> <p> The current working directory as set by the <code>cd</code> command. </p>
 </dd>
<dt><code>RANDOM</code></dt>
<dd> <p> Each time this parameter is referenced, it expands to a random integer between 0 and 32767. Assigning a value to <font SIZE="-1"><code>RANDOM</code> </font> initializes (seeds) the sequence of random numbers. If <font SIZE="-1"><code>RANDOM</code> </font> is unset, it loses its special properties, even if it is subsequently reset. </p>
 </dd>
<dt><code>READLINE_LINE</code></dt>
<dd> <p> The contents of the <code>readline</code> line buffer, for use with &quot;bind -x&quot; (see <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below). </p>
 </dd>
<dt><code>READLINE_MARK</code></dt>
<dd> <p> The position of the mark (saved insertion point) in the <code>readline</code> line buffer, for use with &quot;bind -x&quot; (see <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below). The characters between the insertion point and the mark are often called the <i>region</i>. </p>
 </dd>
<dt><code>READLINE_POINT</code></dt>
<dd> <p> The position of the insertion point in the <code>readline</code> line buffer, for use with &quot;bind -x&quot; (see <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below). </p>
 </dd>
<dt><code>REPLY</code></dt>
<dd> <p> Set to the line of input read by the <code>read</code> builtin command when no arguments are supplied. </p>
 </dd>
<dt><code>SECONDS</code></dt>
<dd> <p> Each time this parameter is referenced, the number of seconds since shell invocation is returned. If a value is assigned to <font SIZE="-1"><code>SECONDS</code>, </font> the value returned upon subsequent references is the number of seconds since the assignment plus the value assigned. The number of seconds at shell invocation and the current time is always determined by querying the system clock. If <font SIZE="-1"><code>SECONDS</code> </font> is unset, it loses its special properties, even if it is subsequently reset. </p>
 </dd>
<dt><code>SHELLOPTS</code></dt>
<dd> <p> A colon-separated list of enabled shell options. Each word in the list is a valid argument for the <code>-o</code> option to the <code>set</code> builtin command (see <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below). The options appearing in <font SIZE="-1"><code>SHELLOPTS</code> </font> are those reported as <i>on</i> by <code>set -o</code>. If this variable is in the environment when <code>bash</code> starts up, each shell option in the list will be enabled before reading any startup files. This variable is read-only. </p>
 </dd>
<dt><code>SHLVL</code></dt>
<dd> <p> Incremented by one each time an instance of <code>bash</code> is started. </p>
 </dd>
<dt><code>SRANDOM</code></dt>
<dd> <p> This variable expands to a 32-bit pseudo-random number each time it is referenced. The random number generator is not linear on systems that support <code>/dev/urandom</code> or <i>arc4random</i>, so each returned number has no relationship to the numbers preceding it. The random number generator cannot be seeded, so assignments to this variable have no effect. If <font SIZE="-1"><code>SRANDOM</code> </font> is unset, it loses its special properties, even if it is subsequently reset. </p>
 </dd>
<dt><code>UID</code></dt>
<dd> <p> Expands to the user ID of the current user, initialized at shell startup. This variable is readonly. </p>
 </dd></dl>
<p> The following variables are used by the shell. In some cases, <code>bash</code> assigns a default value to a variable; these cases are noted below. </p>
<dl>
<dt><code>BASH_COMPAT</code></dt>
<dd> <p> The value is used to set the shell&#8217;s compatibility level. See <font SIZE="-1"><code>SHELL COMPATIBILITY MODE</code> </font> below for a description of the various compatibility levels and their effects. The value may be a decimal number (e.g., 4.2) or an integer (e.g., 42) corresponding to the desired compatibility level. If <code>BASH_COMPAT</code> is unset or set to the empty string, the compatibility level is set to the default for the current version. If <code>BASH_COMPAT</code> is set to a value that is not one of the valid compatibility levels, the shell prints an error message and sets the compatibility level to the default for the current version. The valid values correspond to the compatibility levels described below under <font SIZE="-1"><code>BSHELL</code>COMPATIBILITY <code>MODE</code>. </font> For example, 4.2 and 42 are valid values that correspond to the <code>compat42</code> <code>shopt</code> option and set the compatibility level to 42. The current version is also a valid value. </p>
 </dd>
<dt><code>BASH_ENV</code></dt>
<dd> <p> If this parameter is set when <code>bash</code> is executing a shell script, its value is interpreted as a filename containing commands to initialize the shell, as in <i>~/.bashrc</i>. The value of <font SIZE="-1"><code>BASH_ENV</code> </font> is subjected to parameter expansion, command substitution, and arithmetic expansion before being interpreted as a filename. <font SIZE="-1"><code>PATH</code> </font> is not used to search for the resultant filename. </p>
 </dd>
<dt><code>BASH_XTRACEFD</code></dt>
<dd> <p> If set to an integer corresponding to a valid file descriptor, <code>bash</code> will write the trace output generated when <i>set -x</i> is enabled to that file descriptor. The file descriptor is closed when <font SIZE="-1"><code>BASH_XTRACEFD</code> </font> is unset or assigned a new value. Unsetting <font SIZE="-1"><code>BASH_XTRACEFD</code> </font> or assigning it the empty string causes the trace output to be sent to the standard error. Note that setting <font SIZE="-1"><code>BASH_XTRACEFD</code> </font> to 2 (the standard error file descriptor) and then unsetting it will result in the standard error being closed. </p>
 </dd>
<dt><code>CDPATH</code></dt>
<dd> <p> The search path for the <code>cd</code> command. This is a colon-separated list of directories in which the shell looks for destination directories specified by the <code>cd</code> command. A sample value is &quot;.:~:/usr&quot;. </p>
 </dd>
<dt><code>CHILD_MAX</code></dt>
<dd> <p> Set the number of exited child status values for the shell to remember. Bash will not allow this value to be decreased below a POSIX-mandated minimum, and there is a maximum value (currently 8192) that this may not exceed. The minimum value is system-dependent. </p>
 </dd>
<dt><code>COLUMNS</code></dt>
<dd> <p> Used by the <code>select</code> compound command to determine the terminal width when printing selection lists. Automatically set if the <code>checkwinsize</code> option is enabled or in an interactive shell upon receipt of a <font SIZE="-1"><code>SIGWINCH</code>. </font> </p>
 </dd>
<dt><code>COMPREPLY</code></dt>
<dd> <p> An array variable from which <code>bash</code> reads the possible completions generated by a shell function invoked by the programmable completion facility (see <code>Programmable Completion</code> below). Each array element contains one possible completion. </p>
 </dd>
<dt><code>EMACS</code></dt>
<dd> <p> If <code>bash</code> finds this variable in the environment when the shell starts with value &quot;t&quot;, it assumes that the shell is running in an Emacs shell buffer and disables line editing. </p>
 </dd>
<dt><code>ENV</code></dt>
<dd> <p> Expanded and executed similarly to <font SIZE="-1"><code>BASH_ENV</code> </font> (see <code>INVOCATION</code> above) when an interactive shell is invoked in <i>posix mode</i>. </p>
 </dd>
<dt><code>EXECIGNORE</code></dt>
<dd> <p> A colon-separated list of shell patterns (see <code>Pattern Matching</code>) defining the list of filenames to be ignored by command search using <code>PATH</code>. Files whose full pathnames match one of these patterns are not considered executable files for the purposes of completion and command execution via <code>PATH</code> lookup. This does not affect the behavior of the <code>[</code>, <code>test</code>, and <code>[[</code> commands. Full pathnames in the command hash table are not subject to <code>EXECIGNORE</code>. Use this variable to ignore shared library files that have the executable bit set, but are not executable files. The pattern matching honors the setting of the <code>extglob</code> shell option. </p>
 </dd>
<dt><code>FCEDIT</code></dt>
<dd> <p> The default editor for the <code>fc</code> builtin command. </p>
 </dd>
<dt><code>FIGNORE</code></dt>
<dd> <p> A colon-separated list of suffixes to ignore when performing filename completion (see <font SIZE="-1"><code>READLINE</code> </font> below). A filename whose suffix matches one of the entries in <font SIZE="-1"><code>FIGNORE</code> </font> is excluded from the list of matched filenames. A sample value is &quot;.o:~&quot; (Quoting is needed when assigning a value to this variable, which contains tildes). </p>
 </dd>
<dt><code>FUNCNEST</code></dt>
<dd> <p> If set to a numeric value greater than 0, defines a maximum function nesting level. Function invocations that exceed this nesting level will cause the current command to abort. </p>
 </dd>
<dt><code>GLOBIGNORE</code></dt>
<dd> <p> A colon-separated list of patterns defining the set of file names to be ignored by pathname expansion. If a file name matched by a pathname expansion pattern also matches one of the patterns in <font SIZE="-1"><code>GLOBIGNORE</code>, </font> it is removed from the list of matches. </p>
 </dd>
<dt><code>HISTCONTROL</code></dt>
<dd> <p> A colon-separated list of values controlling how commands are saved on the history list. If the list of values includes <i>ignorespace</i>, lines which begin with a <code>space</code> character are not saved in the history list. A value of <i>ignoredups</i> causes lines matching the previous history entry to not be saved. A value of <i>ignoreboth</i> is shorthand for <i>ignorespace</i> and <i>ignoredups</i>. A value of <i>erasedups</i> causes all previous lines matching the current line to be removed from the history list before that line is saved. Any value not in the above list is ignored. If <font SIZE="-1"><code>HISTCONTROL</code> </font> is unset, or does not include a valid value, all lines read by the shell parser are saved on the history list, subject to the value of <font SIZE="-1"><code>HISTIGNORE</code>. </font> The second and subsequent lines of a multi-line compound command are not tested, and are added to the history regardless of the value of <font SIZE="-1"><code>HISTCONTROL</code>. </font> </p>
 </dd>
<dt><code>HISTFILE</code></dt>
<dd> <p> The name of the file in which command history is saved (see <font SIZE="-1"><code>HISTORY</code> </font> below). The default value is <i>~/.bash_history</i>. If unset, the command history is not saved when a shell exits. </p>
 </dd>
<dt><code>HISTFILESIZE</code></dt>
<dd> <p> The maximum number of lines contained in the history file. When this variable is assigned a value, the history file is truncated, if necessary, to contain no more than that number of lines by removing the oldest entries. The history file is also truncated to this size after writing it when a shell exits. If the value is 0, the history file is truncated to zero size. Non-numeric values and numeric values less than zero inhibit truncation. The shell sets the default value to the value of <code>HISTSIZE</code> after reading any startup files. </p>
 </dd>
<dt><code>HISTIGNORE</code></dt>
<dd> <p> A colon-separated list of patterns used to decide which command lines should be saved on the history list. Each pattern is anchored at the beginning of the line and must match the complete line (no implicit `<code>*</code>&#8216; is appended). Each pattern is tested against the line after the checks specified by <font SIZE="-1"><code>HISTCONTROL</code> </font> are applied. In addition to the normal shell pattern matching characters, `<code>&amp;</code>&#8216; matches the previous history line. `<code>&amp;</code>&#8216; may be escaped using a backslash; the backslash is removed before attempting a match. The second and subsequent lines of a multi-line compound command are not tested, and are added to the history regardless of the value of <font SIZE="-1"><code>HISTIGNORE</code>. </font> The pattern matching honors the setting of the <code>extglob</code> shell option. </p>
 </dd>
<dt><code>HISTSIZE</code></dt>
<dd> <p> The number of commands to remember in the command history (see <font SIZE="-1"><code>HISTORY</code> </font> below). If the value is 0, commands are not saved in the history list. Numeric values less than zero result in every command being saved on the history list (there is no limit). The shell sets the default value to 500 after reading any startup files. </p>
 </dd>
<dt><code>HISTTIMEFORMAT</code></dt>
<dd> <p> If this variable is set and not null, its value is used as a format string for <i><a href="/docs/linux/man/3-strftime/">strftime</a></i>(3) to print the time stamp associated with each history entry displayed by the <code>history</code> builtin. If this variable is set, time stamps are written to the history file so they may be preserved across shell sessions. This uses the history comment character to distinguish timestamps from other history lines. </p>
 </dd>
<dt><code>HOME</code></dt>
<dd> <p> The home directory of the current user; the default argument for the <code>cd</code> builtin command. The value of this variable is also used when performing tilde expansion. </p>
 </dd>
<dt><code>HOSTFILE</code></dt>
<dd> <p> Contains the name of a file in the same format as <i>/etc/hosts</i> that should be read when the shell needs to complete a hostname. The list of possible hostname completions may be changed while the shell is running; the next time hostname completion is attempted after the value is changed, <code>bash</code> adds the contents of the new file to the existing list. If <font SIZE="-1"><code>HOSTFILE</code> </font> is set, but has no value, or does not name a readable file, <code>bash</code> attempts to read <i>/etc/hosts</i> to obtain the list of possible hostname completions. When <font SIZE="-1"><code>HOSTFILE</code> </font> is unset, the hostname list is cleared. </p>
 </dd>
<dt><code>IFS</code></dt>
<dd> <p> The <i>Internal Field Separator</i> that is used for word splitting after expansion and to split lines into words with the <code>read</code> builtin command. The default value is ``&lt;space&gt;&lt;tab&gt;&lt;newline&gt;&#8216;&#8216;. </p>
 </dd>
<dt><code>IGNOREEOF</code></dt>
<dd> <p> Controls the action of an interactive shell on receipt of an <font SIZE="-1"><code>EOF</code> </font> character as the sole input. If set, the value is the number of consecutive <font SIZE="-1"><code>EOF</code> </font> characters which must be typed as the first characters on an input line before <code>bash</code> exits. If the variable exists but does not have a numeric value, or has no value, the default value is 10. If it does not exist, <font SIZE="-1"><code>EOF</code> </font> signifies the end of input to the shell. </p>
 </dd>
<dt><code>INPUTRC</code></dt>
<dd> <p> The filename for the <code>readline</code> startup file, overriding the default of <i>~/.inputrc</i> (see <font SIZE="-1"><code>READLINE</code> </font> below). </p>
 </dd>
<dt><code>INSIDE_EMACS</code></dt>
<dd> <p> If this variable appears in the environment when the shell starts, <code>bash</code> assumes that it is running inside an Emacs shell buffer and may disable line editing, depending on the value of <code>TERM</code>. </p>
 </dd>
<dt><code>LANG</code></dt>
<dd> <p> Used to determine the locale category for any category not specifically selected with a variable starting with <code>LC_</code>. </p>
 </dd>
<dt><code>LC_ALL</code></dt>
<dd> <p> This variable overrides the value of <font SIZE="-1"><code>LANG</code> </font> and any other <code>LC_</code> variable specifying a locale category. </p>
 </dd>
<dt><code>LC_COLLATE</code></dt>
<dd> <p> This variable determines the collation order used when sorting the results of pathname expansion, and determines the behavior of range expressions, equivalence classes, and collating sequences within pathname expansion and pattern matching. </p>
 </dd>
<dt><code>LC_CTYPE</code></dt>
<dd> <p> This variable determines the interpretation of characters and the behavior of character classes within pathname expansion and pattern matching. </p>
 </dd>
<dt><code>LC_MESSAGES</code></dt>
<dd> <p> This variable determines the locale used to translate double-quoted strings preceded by a <code>$</code>. </p>
 </dd>
<dt><code>LC_NUMERIC</code></dt>
<dd> <p> This variable determines the locale category used for number formatting. </p>
 </dd>
<dt><code>LC_TIME</code></dt>
<dd> <p> This variable determines the locale category used for data and time formatting. </p>
 </dd>
<dt><code>LINES</code></dt>
<dd> <p> Used by the <code>select</code> compound command to determine the column length for printing selection lists. Automatically set if the <code>checkwinsize</code> option is enabled or in an interactive shell upon receipt of a <font SIZE="-1"><code>SIGWINCH</code>. </font> </p>
 </dd>
<dt><code>MAIL</code></dt>
<dd> <p> If this parameter is set to a file or directory name and the <font SIZE="-1"><code>MAILPATH</code> </font> variable is not set, <code>bash</code> informs the user of the arrival of mail in the specified file or Maildir-format directory. </p>
 </dd>
<dt><code>MAILCHECK</code></dt>
<dd> <p> Specifies how often (in seconds) <code>bash</code> checks for mail. The default is 60 seconds. When it is time to check for mail, the shell does so before displaying the primary prompt. If this variable is unset, or set to a value that is not a number greater than or equal to zero, the shell disables mail checking. </p>
 </dd>
<dt><code>MAILPATH</code></dt>
<dd> <p> A colon-separated list of filenames to be checked for mail. The message to be printed when mail arrives in a particular file may be specified by separating the filename from the message with a `?&#8216;. When used in the text of the message, <code>$_</code> expands to the name of the current mailfile. Example: </p>
 </dd>
<dl>
<dd> <p> <code>MAILPATH</code>=&#8216;/var/mail/bfox?&quot;You have mail&quot;:~/shell-mail?&quot;$_ has mail!&quot;&#8216; </p>
<p> <code>Bash</code> can be configured to supply a default value for this variable (there is no value by default), but the location of the user mail files that it uses is system dependent (e.g., /var/mail/<code>$USER</code>). </p>
 </dd></dl>
<dt><code>OPTERR</code></dt>
<dd> <p> If set to the value 1, <code>bash</code> displays error messages generated by the <code>getopts</code> builtin command (see <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below). <font SIZE="-1"><code>OPTERR</code> </font> is initialized to 1 each time the shell is invoked or a shell script is executed. </p>
 </dd>
<dt><code>PATH</code></dt>
<dd> <p> The search path for commands. It is a colon-separated list of directories in which the shell looks for commands (see <font SIZE="-1"><code>COMMAND EXECUTION</code> </font> below). A zero-length (null) directory name in the value of <font SIZE="-1"><code>PATH</code> </font> indicates the current directory. A null directory name may appear as two adjacent colons, or as an initial or trailing colon. The default path is system-dependent, and is set by the administrator who installs <code>bash</code>. A common value is ``/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin&#8217;&#8216;. </p>
 </dd>
<dt><code>POSIXLY_CORRECT</code></dt>
<dd> <p> If this variable is in the environment when <code>bash</code> starts, the shell enters <i>posix mode</i> before reading the startup files, as if the <code>--posix</code> invocation option had been supplied. If it is set while the shell is running, <code>bash</code> enables <i>posix mode</i>, as if the command <i>set -o posix</i> had been executed. When the shell enters <i>posix mode</i>, it sets this variable if it was not already set. </p>
 </dd>
<dt><code>PROMPT_COMMAND</code></dt>
<dd> <p> If this variable is set, and is an array, the value of each set element is executed as a command prior to issuing each primary prompt. If this is set but not an array variable, its value is used as a command to execute instead. </p>
 </dd>
<dt><code>PROMPT_DIRTRIM</code></dt>
<dd> <p> If set to a number greater than zero, the value is used as the number of trailing directory components to retain when expanding the <code>\w</code> and <code>\W</code> prompt string escapes (see <font SIZE="-1"><code>PROMPTING</code> </font> below). Characters removed are replaced with an ellipsis. </p>
 </dd>
<dt><code>PS0</code></dt>
<dd> <p> The value of this parameter is expanded (see <font SIZE="-1"><code>PROMPTING</code> </font> below) and displayed by interactive shells after reading a command and before the command is executed. </p>
 </dd>
<dt><code>PS1</code></dt>
<dd> <p> The value of this parameter is expanded (see <font SIZE="-1"><code>PROMPTING</code> </font> below) and used as the primary prompt string. The default value is ``<code>\s-\v\$ </code>&#8216;&#8216;. </p>
 </dd>
<dt><code>PS2</code></dt>
<dd> <p> The value of this parameter is expanded as with <font SIZE="-1"><code>PS1</code> </font> and used as the secondary prompt string. The default is ``<code>&gt; </code>&#8216;&#8216;. </p>
 </dd>
<dt><code>PS3</code></dt>
<dd> <p> The value of this parameter is used as the prompt for the <code>select</code> command (see <font SIZE="-1"><code>SHELL GRAMMAR</code> </font> above). </p>
 </dd>
<dt><code>PS4</code></dt>
<dd> <p> The value of this parameter is expanded as with <font SIZE="-1"><code>PS1</code> </font> and the value is printed before each command <code>bash</code> displays during an execution trace. The first character of the expanded value of <font SIZE="-1"><code>PS4</code> </font> is replicated multiple times, as necessary, to indicate multiple levels of indirection. The default is ``<code>+ </code>&#8216;&#8216;. </p>
 </dd>
<dt><code>SHELL</code></dt>
<dd> <p> This variable expands to the full pathname to the shell. If it is not set when the shell starts, <code>bash</code> assigns to it the full pathname of the current user&#8217;s login shell. </p>
 </dd>
<dt><code>TIMEFORMAT</code></dt>
<dd> <p> The value of this parameter is used as a format string specifying how the timing information for pipelines prefixed with the <code>time</code> reserved word should be displayed. The <code>%</code> character introduces an escape sequence that is expanded to a time value or other information. The escape sequences and their meanings are as follows; the braces denote optional portions. </p>
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
<dd> <p> The CPU percentage, computed as (%U + %S) / %R. </p>
 </dd></dl>
</dl>
<dd> <p> The optional <i>p</i> is a digit specifying the <i>precision</i>, the number of fractional digits after a decimal point. A value of 0 causes no decimal point or fraction to be output. At most three places after the decimal point may be specified; values of <i>p</i> greater than 3 are changed to 3. If <i>p</i> is not specified, the value 3 is used. </p>
 </dd>
<dd> <p> The optional <code>l</code> specifies a longer format, including minutes, of the form <i>MM</i>m <i>SS</i>.<i>FF</i>s. The value of <i>p</i> determines whether or not the fraction is included. </p>
 </dd>
<dd> <p> If this variable is not set, <code>bash</code> acts as if it had the value <code>$&#8216;\nreal\t%3lR\nuser\t%3lU\nsys\t%3lS&#8217;</code>. If the value is null, no timing information is displayed. A trailing newline is added when the format string is displayed. </p>
 </dd>
<dt><code>TMOUT</code></dt>
<dd> <p> If set to a value greater than zero, <font SIZE="-1"><code>TMOUT</code> </font> is treated as the default timeout for the <code>read</code> builtin. The <code>select</code> command terminates if input does not arrive after <font SIZE="-1"><code>TMOUT</code> </font> seconds when input is coming from a terminal. In an interactive shell, the value is interpreted as the number of seconds to wait for a line of input after issuing the primary prompt. <code>Bash</code> terminates after waiting for that number of seconds if a complete line of input does not arrive. </p>
 </dd>
<dt><code>TMPDIR</code></dt>
<dd> <p> If set, <code>bash</code> uses its value as the name of a directory in which <code>bash</code> creates temporary files for the shell&#8217;s use. </p>
 </dd>
<dt><code>auto_resume</code></dt>
<dd> <p> This variable controls how the shell interacts with the user and job control. If this variable is set, single word simple commands without redirections are treated as candidates for resumption of an existing stopped job. There is no ambiguity allowed; if there is more than one job beginning with the string typed, the job most recently accessed is selected. The <i>name</i> of a stopped job, in this context, is the command line used to start it. If set to the value <i>exact</i>, the string supplied must match the name of a stopped job exactly; if set to <i>substring</i>, the string supplied needs to match a substring of the name of a stopped job. The <i>substring</i> value provides functionality analogous to the <code>%?</code> job identifier (see <font SIZE="-1"><code>JOB CONTROL</code> </font> below). If set to any other value, the supplied string must be a prefix of a stopped job&#8217;s name; this provides functionality analogous to the <code>%</code><i>string</i> job identifier. </p>
 </dd>
<dt><code>histchars</code></dt>
<dd> <p> The two or three characters which control history expansion and tokenization (see <font SIZE="-1"><code>HISTORY EXPANSION</code> </font> below). The first character is the <i>history expansion</i> character, the character which signals the start of a history expansion, normally `<code>!</code>&#8216;. The second character is the <i>quick substitution</i> character, which is used as shorthand for re-running the previous command entered, substituting one string for another in the command. The default is `<code>^</code>&#8216;. The optional third character is the character which indicates that the remainder of the line is a comment when found as the first character of a word, normally `<code>#</code>&#8216;. The history comment character causes history substitution to be skipped for the remaining words on the line. It does not necessarily cause the shell parser to treat the rest of the line as a comment. </p>
 </dd></dl>
<h3>Arrays</h3>
<p> <code>Bash</code> provides one-dimensional indexed and associative array variables. Any variable may be used as an indexed array; the <code>declare</code> builtin will explicitly declare an array. There is no maximum limit on the size of an array, nor any requirement that members be indexed or assigned contiguously. Indexed arrays are referenced using integers (including arithmetic expressions) and are zero-based; associative arrays are referenced using arbitrary strings. Unless otherwise noted, indexed array indices must be non-negative integers. </p>
<p> An indexed array is created automatically if any variable is assigned to using the syntax <i>name</i>[<i>subscript</i>]=<i>value</i>. The <i>subscript</i> is treated as an arithmetic expression that must evaluate to a number. To explicitly declare an indexed array, use <code>declare -a </code><i>name</i> (see <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below). <code>declare -a </code><i>name</i>[<i>subscript</i>] is also accepted; the <i>subscript</i> is ignored. </p>
<p> Associative arrays are created using <code>declare -A </code><i>name</i>. </p>
<p> Attributes may be specified for an array variable using the <code>declare</code> and <code>readonly</code> builtins. Each attribute applies to all members of an array. </p>
<p> Arrays are assigned to using compound assignments of the form <i>name</i>=<code>(</code>value <i>1</i> ... value <i>n</i><code>)</code>, where each <i>value</i> may be of the form [<i>subscript</i>]=<i>string</i>. Indexed array assignments do not require anything but <i>string</i>. Each <i>value</i> in the list is expanded using all the shell expansions described below under <font SIZE="-1"><code>EXPANSION</code>. </font> When assigning to indexed arrays, if the optional brackets and subscript are supplied, that index is assigned to; otherwise the index of the element assigned is the last index assigned to by the statement plus one. Indexing starts at zero. </p>
<p> When assigning to an associative array, the words in a compound assignment may be either assignment statements, for which the subscript is required, or a list of words that is interpreted as a sequence of alternating keys and values: <i>name</i>=<code>( </code><i>key1 value1 key2 value2</i> ...<code>)</code>. These are treated identically to <i>name</i>=<code>(</code> [<i>key1</i>]=<i>value1</i> [<i>key2</i>]=<i>value2</i> ...<code>)</code>. The first word in the list determines how the remaining words are interpreted; all assignments in a list must be of the same type. When using key/value pairs, the keys may not be missing or empty; a final missing value is treated like the empty string. </p>
<p> This syntax is also accepted by the <code>declare</code> builtin. Individual array elements may be assigned to using the <i>name</i>[<i>subscript</i>]=<i>value</i> syntax introduced above. When assigning to an indexed array, if <i>name</i> is subscripted by a negative number, that number is interpreted as relative to one greater than the maximum index of <i>name</i>, so negative indices count back from the end of the array, and an index of -1 references the last element. </p>
<p> Any element of an array may be referenced using ${<i>name</i>[<i>subscript</i>]}. The braces are required to avoid conflicts with pathname expansion. If <i>subscript</i> is <code>@</code> or <code>*</code>, the word expands to all members of <i>name</i>. These subscripts differ only when the word appears within double quotes. If the word is double-quoted, ${<i>name</i>[*]} expands to a single word with the value of each array member separated by the first character of the <font SIZE="-1"><code>IFS</code> </font> special variable, and ${<i>name</i>[@]} expands each element of <i>name</i> to a separate word. When there are no array members, ${<i>name</i>[@]} expands to nothing. If the double-quoted expansion occurs within a word, the expansion of the first parameter is joined with the beginning part of the original word, and the expansion of the last parameter is joined with the last part of the original word. This is analogous to the expansion of the special parameters <code>*</code> and <code>@</code> (see <code>Special Parameters</code> above). ${#<i>name</i>[<i>subscript</i>]} expands to the length of ${<i>name</i>[<i>subscript</i>]}. If <i>subscript</i> is <code>*</code> or <code>@</code>, the expansion is the number of elements in the array. If the <i>subscript</i> used to reference an element of an indexed array evaluates to a number less than zero, it is interpreted as relative to one greater than the maximum index of the array, so negative indices count back from the end of the array, and an index of -1 references the last element. </p>
<p> Referencing an array variable without a subscript is equivalent to referencing the array with a subscript of 0. Any reference to a variable using a valid subscript is legal, and <code>bash</code> will create an array if necessary. </p>
<p> An array variable is considered set if a subscript has been assigned a value. The null string is a valid value. </p>
<p> It is possible to obtain the keys (indices) of an array as well as the values. ${<code>!</code><i>name</i>[<i>@</i>]} and ${<code>!</code><i>name</i>[<i>*</i>]} expand to the indices assigned in array variable <i>name</i>. The treatment when in double quotes is similar to the expansion of the special parameters <i>@</i> and <i>*</i> within double quotes. </p>
<p> The <code>unset</code> builtin is used to destroy arrays. <code>unset</code> <i>name</i>[<i>subscript</i>] destroys the array element at index <i>subscript</i>, for both indexed and associative arrays. Negative subscripts to indexed arrays are interpreted as described above. Unsetting the last element of an array variable does not unset the variable. <code>unset</code> <i>name</i>, where <i>name</i> is an array, or <code>unset</code> <i>name</i>[<i>subscript</i>], where <i>subscript</i> is <code>*</code> or <code>@</code>, removes the entire array. </p>
<p> When using a variable name with a subscript as an argument to a command, such as with <code>unset</code>, without using the word expansion syntax described above, the argument is subject to pathname expansion. If pathname expansion is not desired, the argument should be quoted. </p>
<p> The <code>declare</code>, <code>local</code>, and <code>readonly</code> builtins each accept a <code>-a</code> option to specify an indexed array and a <code>-A</code> option to specify an associative array. If both options are supplied, <code>-A</code> takes precedence. The <code>read</code> builtin accepts a <code>-a</code> option to assign a list of words read from the standard input to an array. The <code>set</code> and <code>declare</code> builtins display array values in a way that allows them to be reused as assignments.  </p>
<h2>EXPANSION</h2>
<p> Expansion is performed on the command line after it has been split into words. There are seven kinds of expansion performed: <i>brace expansion</i>, <i>tilde expansion</i>, <i>parameter and variable expansion</i>, <i>command substitution</i>, <i>arithmetic expansion</i>, <i>word splitting</i>, and <i>pathname expansion</i>. </p>
<p> The order of expansions is: brace expansion; tilde expansion, parameter and variable expansion, arithmetic expansion, and command substitution (done in a left-to-right fashion); word splitting; and pathname expansion. </p>
<p> On systems that can support it, there is an additional expansion available: <i>process substitution</i>. This is performed at the same time as tilde, parameter, variable, and arithmetic expansion and command substitution. </p>
<p> After these expansions are performed, quote characters present in the original word are removed unless they have been quoted themselves (<i>quote removal</i>). </p>
<p> Only brace expansion, word splitting, and pathname expansion can increase the number of words of the expansion; other expansions expand a single word to a single word. The only exceptions to this are the expansions of &quot;<code>$@</code>&quot; and &quot;<code>${</code><i>name</i><code>[@]}</code>&quot;, and, in most cases, <code>$*</code> and <code>${</code><i>name</i><code>[*]}</code> as explained above (see <font SIZE="-1"><code>PARAMETERS</code>). </font>  </p>
<h3>Brace Expansion</h3>
<p> <i>Brace expansion</i> is a mechanism by which arbitrary strings may be generated. This mechanism is similar to <i>pathname expansion</i>, but the filenames generated need not exist. Patterns to be brace expanded take the form of an optional <i>preamble</i>, followed by either a series of comma-separated strings or a sequence expression between a pair of braces, followed by an optional <i>postscript</i>. The preamble is prefixed to each string contained within the braces, and the postscript is then appended to each resulting string, expanding left to right. </p>
<p> Brace expansions may be nested. The results of each expanded string are not sorted; left to right order is preserved. For example, a <code>{</code>d,c,b <code>}</code>e expands into `ade ace abe&#8217;. </p>
<p> A sequence expression takes the form <code>{</code><i>x</i><code>..</code><i>y</i><code>[..</code><i>incr</i><code>]}</code>, where <i>x</i> and <i>y</i> are either integers or single characters, and <i>incr</i>, an optional increment, is an integer. When integers are supplied, the expression expands to each number between <i>x</i> and <i>y</i>, inclusive. Supplied integers may be prefixed with <i>0</i> to force each term to have the same width. When either <i>x</i> or y begins with a zero, the shell attempts to force all generated terms to contain the same number of digits, zero-padding where necessary. When characters are supplied, the expression expands to each character lexicographically between <i>x</i> and <i>y</i>, inclusive, using the default C locale. Note that both <i>x</i> and <i>y</i> must be of the same type. When the increment is supplied, it is used as the difference between each term. The default increment is 1 or -1 as appropriate. </p>
<p> Brace expansion is performed before any other expansions, and any characters special to other expansions are preserved in the result. It is strictly textual. <code>Bash</code> does not apply any syntactic interpretation to the context of the expansion or the text between the braces. </p>
<p> A correctly-formed brace expansion must contain unquoted opening and closing braces, and at least one unquoted comma or a valid sequence expression. Any incorrectly formed brace expansion is left unchanged. A <code>{</code> or <code>,</code> may be quoted with a backslash to prevent its being considered part of a brace expression. To avoid conflicts with parameter expansion, the string <code>${</code> is not considered eligible for brace expansion, and inhibits brace expansion until the closing <code>}</code>. </p>
<p> This construct is typically used as shorthand when the common prefix of the strings to be generated is longer than in the above example: </p>
<dl>
<dd> <p> mkdir /usr/local/src/bash/{old,new,dist,bugs} </p>
 </dd></dl>
<p> or </p>
<dl>
<dd> <p> chown root /usr/{ucb/{ex,edit},lib/{ex?.?*,how_ex}} </p>
 </dd></dl>
<p> Brace expansion introduces a slight incompatibility with historical versions of <code>sh</code>. <code>sh</code> does not treat opening or closing braces specially when they appear as part of a word, and preserves them in the output. <code>Bash</code> removes braces from words as a consequence of brace expansion. For example, a word entered to <code>sh</code> as <i>file{1,2}</i> appears identically in the output. The same word is output as <i>file1 file2</i> after expansion by <code>bash</code>. If strict compatibility with <code>sh</code> is desired, start <code>bash</code> with the <code>+B</code> option or disable brace expansion with the <code>+B</code> option to the <code>set</code> command (see <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below).  </p>
<h3>Tilde Expansion</h3>
<p> If a word begins with an unquoted tilde character (`<code>~</code>&#8216;), all of the characters preceding the first unquoted slash (or all characters, if there is no unquoted slash) are considered a <i>tilde-prefix</i>. If none of the characters in the tilde-prefix are quoted, the characters in the tilde-prefix following the tilde are treated as a possible <i>login name</i>. If this login name is the null string, the tilde is replaced with the value of the shell parameter <font SIZE="-1"><code>HOME</code>. </font> If <font SIZE="-1"><code>HOME</code> </font> is unset, the home directory of the user executing the shell is substituted instead. Otherwise, the tilde-prefix is replaced with the home directory associated with the specified login name. </p>
<p> If the tilde-prefix is a `~+&#8216;, the value of the shell variable <font SIZE="-1"><code>PWD</code> </font> replaces the tilde-prefix. If the tilde-prefix is a `~-&#8216;, the value of the shell variable <font SIZE="-1"><code>OLDPWD</code>, </font> if it is set, is substituted. If the characters following the tilde in the tilde-prefix consist of a number <i>N</i>, optionally prefixed by a `+&#8216; or a `-&#8216;, the tilde-prefix is replaced with the corresponding element from the directory stack, as it would be displayed by the <code>dirs</code> builtin invoked with the tilde-prefix as an argument. If the characters following the tilde in the tilde-prefix consist of a number without a leading `+&#8216; or `-&#8216;, `+&#8216; is assumed. </p>
<p> If the login name is invalid, or the tilde expansion fails, the word is unchanged. </p>
<p> Each variable assignment is checked for unquoted tilde-prefixes immediately following a <code>:</code> or the first <code>=</code>. In these cases, tilde expansion is also performed. Consequently, one may use filenames with tildes in assignments to <font SIZE="-1"><code>PATH</code>, </font> <font SIZE="-1"><code>MAILPATH</code>, </font> and <font SIZE="-1"><code>CDPATH</code>, </font> and the shell assigns the expanded value. </p>
<p> Bash also performs tilde expansion on words satisfying the conditions of variable assignments (as described above under <font SIZE="-1"><code>PARAMETERS</code>) </font> when they appear as arguments to simple commands. Bash does not do this, except for the <i>declaration</i> commands listed above, when in <i>posix mode</i>.  </p>
<h3>Parameter Expansion</h3>
<p> The `<code>$</code>&#8216; character introduces parameter expansion, command substitution, or arithmetic expansion. The parameter name or symbol to be expanded may be enclosed in braces, which are optional but serve to protect the variable to be expanded from characters immediately following it which could be interpreted as part of the name. </p>
<p> When braces are used, the matching ending brace is the first `<code>}</code>&#8216; not escaped by a backslash or within a quoted string, and not within an embedded arithmetic expansion, command substitution, or parameter expansion. </p>
<dl>
<dt>${<i>parameter</i>}</dt>
<dd> <p> The value of <i>parameter</i> is substituted. The braces are required when <i>parameter</i> is a positional parameter with more than one digit, or when <i>parameter</i> is followed by a character which is not to be interpreted as part of its name. The <i>parameter</i> is a shell parameter as described above <code>PARAMETERS</code>) or an array reference (<code>Arrays</code>). </p>
 </dd></dl>
<p> If the first character of <i>parameter</i> is an exclamation point (<code>!</code>), and <i>parameter</i> is not a <i>nameref</i>, it introduces a level of indirection. <code>Bash</code> uses the value formed by expanding the rest of <i>parameter</i> as the new <i>parameter</i>; this is then expanded and that value is used in the rest of the expansion, rather than the expansion of the original <i>parameter</i>. This is known as <i>indirect expansion</i>. The value is subject to tilde expansion, parameter expansion, command substitution, and arithmetic expansion. If <i>parameter</i> is a nameref, this expands to the name of the parameter referenced by <i>parameter</i> instead of performing the complete indirect expansion. The exceptions to this are the expansions of ${<code>!</code><i>prefix</i><code>*</code>} and ${<code>!</code><i>name</i>[<i>@</i>]} described below. The exclamation point must immediately follow the left brace in order to introduce indirection. </p>
<p> In each of the cases below, <i>word</i> is subject to tilde expansion, parameter expansion, command substitution, and arithmetic expansion. </p>
<p> When not performing substring expansion, using the forms documented below (e.g., <code>:-</code>), <code>bash</code> tests for a parameter that is unset or null. Omitting the colon results in a test only for a parameter that is unset. </p>
<dl>
<dt>${<i>parameter</i><code>:-</code><i>word</i>}</dt>
<dd> <p> <code>Use Default Values</code>. If <i>parameter</i> is unset or null, the expansion of <i>word</i> is substituted. Otherwise, the value of <i>parameter</i> is substituted. </p>
 </dd>
<dt>${<i>parameter</i><code>:=</code><i>word</i>}</dt>
<dd> <p> <code>Assign Default Values</code>. If <i>parameter</i> is unset or null, the expansion of <i>word</i> is assigned to <i>parameter</i>. The value of <i>parameter</i> is then substituted. Positional parameters and special parameters may not be assigned to in this way. </p>
 </dd>
<dt>${<i>parameter</i><code>:?</code><i>word</i>}</dt>
<dd> <p> <code>Display Error if Null or Unset</code>. If <i>parameter</i> is null or unset, the expansion of <i>word</i> (or a message to that effect if <i>word</i> is not present) is written to the standard error and the shell, if it is not interactive, exits. Otherwise, the value of <i>parameter</i> is substituted. </p>
 </dd>
<dt>${<i>parameter</i><code>:+</code><i>word</i>}</dt>
<dd> <p> <code>Use Alternate Value</code>. If <i>parameter</i> is null or unset, nothing is substituted, otherwise the expansion of <i>word</i> is substituted. </p>
 </dd>
<dt>${<i>parameter</i><code>:</code><i>offset</i>}</dt>
<dd>  </dd>
<dt>${<i>parameter</i><code>:</code><i>offset</i><code>:</code><i>length</i>}</dt>
<dd> <p> <code>Substring Expansion</code>. Expands to up to <i>length</i> characters of the value of <i>parameter</i> starting at the character specified by <i>offset</i>. If <i>parameter</i> is <code>@</code>, an indexed array subscripted by <code>@</code> or <code>*</code>, or an associative array name, the results differ as described below. If <i>length</i> is omitted, expands to the substring of the value of <i>parameter</i> starting at the character specified by <i>offset</i> and extending to the end of the value. <i>length</i> and <i>offset</i> are arithmetic expressions (see <font SIZE="-1"><code>ARITHMETIC EVALUATION</code> </font> below). </p>
<p> If <i>offset</i> evaluates to a number less than zero, the value is used as an offset in characters from the end of the value of <i>parameter</i>. If <i>length</i> evaluates to a number less than zero, it is interpreted as an offset in characters from the end of the value of <i>parameter</i> rather than a number of characters, and the expansion is the characters between <i>offset</i> and that result. Note that a negative offset must be separated from the colon by at least one space to avoid being confused with the <code>:-</code> expansion. </p>
<p> If <i>parameter</i> is <code>@</code>, the result is <i>length</i> positional parameters beginning at <i>offset</i>. A negative <i>offset</i> is taken relative to one greater than the greatest positional parameter, so an offset of -1 evaluates to the last positional parameter. It is an expansion error if <i>length</i> evaluates to a number less than zero. </p>
<p> If <i>parameter</i> is an indexed array name subscripted by @ or *, the result is the <i>length</i> members of the array beginning with ${<i>parameter</i>[<i>offset</i>]}. A negative <i>offset</i> is taken relative to one greater than the maximum index of the specified array. It is an expansion error if <i>length</i> evaluates to a number less than zero. </p>
<p> Substring expansion applied to an associative array produces undefined results. </p>
<p> Substring indexing is zero-based unless the positional parameters are used, in which case the indexing starts at 1 by default. If <i>offset</i> is 0, and the positional parameters are used, <code>$0</code> is prefixed to the list. </p>
 </dd>
<dt>${<code>!</code><i>prefix</i><code>*</code>}</dt>
<dd>  </dd>
<dt>${<code>!</code><i>prefix</i><code>@</code>}</dt>
<dd> <p> <code>Names matching prefix</code>. Expands to the names of variables whose names begin with <i>prefix</i>, separated by the first character of the <font SIZE="-1"><code>IFS</code> </font> special variable. When <i>@</i> is used and the expansion appears within double quotes, each variable name expands to a separate word. </p>
 </dd>
<dt>${<code>!</code><i>name</i>[<i>@</i>]}</dt>
<dd>  </dd>
<dt>${<code>!</code><i>name</i>[<i>*</i>]}</dt>
<dd> <p> <code>List of array keys</code>. If <i>name</i> is an array variable, expands to the list of array indices (keys) assigned in <i>name</i>. If <i>name</i> is not an array, expands to 0 if <i>name</i> is set and null otherwise. When <i>@</i> is used and the expansion appears within double quotes, each key expands to a separate word. </p>
 </dd>
<dt>${<code>#</code><i>parameter</i>}</dt>
<dd> <p> <code>Parameter length</code>. The length in characters of the value of <i>parameter</i> is substituted. If <i>parameter</i> is <code>*</code> or <code>@</code>, the value substituted is the number of positional parameters. If <i>parameter</i> is an array name subscripted by <code>*</code> or <code>@</code>, the value substituted is the number of elements in the array. If <i>parameter</i> is an indexed array name subscripted by a negative number, that number is interpreted as relative to one greater than the maximum index of <i>parameter</i>, so negative indices count back from the end of the array, and an index of -1 references the last element. </p>
 </dd>
<dt>${<i>parameter</i><code>#</code><i>word</i>}</dt>
<dd>  </dd>
<dt>${<i>parameter</i><code>##</code><i>word</i>}</dt>
<dd> <p> <code>Remove matching prefix pattern</code>. The <i>word</i> is expanded to produce a pattern just as in pathname expansion, and matched against the expanded value of <i>parameter</i> using the rules described under <code>Pattern Matching</code> below. If the pattern matches the beginning of the value of <i>parameter</i>, then the result of the expansion is the expanded value of <i>parameter</i> with the shortest matching pattern (the ``<code>#</code>&#8216;&#8216; case) or the longest matching pattern (the ``<code>##</code>&#8216;&#8216; case) deleted. If <i>parameter</i> is <code>@</code> or <code>*</code>, the pattern removal operation is applied to each positional parameter in turn, and the expansion is the resultant list. If <i>parameter</i> is an array variable subscripted with <code>@</code> or <code>*</code>, the pattern removal operation is applied to each member of the array in turn, and the expansion is the resultant list. </p>
 </dd>
<dt>${<i>parameter</i><code>%</code><i>word</i>}</dt>
<dd>  </dd>
<dt>${<i>parameter</i><code>%%</code><i>word</i>}</dt>
<dd> <p> <code>Remove matching suffix pattern</code>. The <i>word</i> is expanded to produce a pattern just as in pathname expansion, and matched against the expanded value of <i>parameter</i> using the rules described under <code>Pattern Matching</code> below. If the pattern matches a trailing portion of the expanded value of <i>parameter</i>, then the result of the expansion is the expanded value of <i>parameter</i> with the shortest matching pattern (the ``<code>%</code>&#8216;&#8216; case) or the longest matching pattern (the ``<code>%%</code>&#8216;&#8216; case) deleted. If <i>parameter</i> is <code>@</code> or <code>*</code>, the pattern removal operation is applied to each positional parameter in turn, and the expansion is the resultant list. If <i>parameter</i> is an array variable subscripted with <code>@</code> or <code>*</code>, the pattern removal operation is applied to each member of the array in turn, and the expansion is the resultant list. </p>
 </dd>
<dt>${<i>parameter</i><code>/</code><i>pattern</i><code>/</code><i>string</i>}</dt>
<dd> <p> <code>Pattern substitution</code>. The <i>pattern</i> is expanded to produce a pattern just as in pathname expansion, <i>Parameter</i> is expanded and the longest match of <i>pattern</i> against its value is replaced with <i>string</i>. The match is performed using the rules described under <code>Pattern Matching</code> below. If <i>pattern</i> begins with <code>/</code>, all matches of <i>pattern</i> are replaced with <i>string</i>. Normally only the first match is replaced. If <i>pattern</i> begins with <code>#</code>, it must match at the beginning of the expanded value of <i>parameter</i>. If <i>pattern</i> begins with <code>%</code>, it must match at the end of the expanded value of <i>parameter</i>. If <i>string</i> is null, matches of <i>pattern</i> are deleted and the <code>/</code> following <i>pattern</i> may be omitted. If the <code>nocasematch</code> shell option is enabled, the match is performed without regard to the case of alphabetic characters. If <i>parameter</i> is <code>@</code> or <code>*</code>, the substitution operation is applied to each positional parameter in turn, and the expansion is the resultant list. If <i>parameter</i> is an array variable subscripted with <code>@</code> or <code>*</code>, the substitution operation is applied to each member of the array in turn, and the expansion is the resultant list. </p>
 </dd>
<dt>${<i>parameter</i><code>^</code><i>pattern</i>}</dt>
<dd>  </dd>
<dt>${<i>parameter</i><code>^^</code><i>pattern</i>}</dt>
<dd>  </dd>
<dt>${<i>parameter</i><code>,</code><i>pattern</i>}</dt>
<dd>  </dd>
<dt>${<i>parameter</i><code>,,</code><i>pattern</i>}</dt>
<dd> <p> <code>Case modification</code>. This expansion modifies the case of alphabetic characters in <i>parameter</i>. The <i>pattern</i> is expanded to produce a pattern just as in pathname expansion. Each character in the expanded value of <i>parameter</i> is tested against <i>pattern</i>, and, if it matches the pattern, its case is converted. The pattern should not attempt to match more than one character. The <code>^</code> operator converts lowercase letters matching <i>pattern</i> to uppercase; the <code>,</code> operator converts matching uppercase letters to lowercase. The <code>^^</code> and <code>,,</code> expansions convert each matched character in the expanded value; the <code>^</code> and <code>,</code> expansions match and convert only the first character in the expanded value. If <i>pattern</i> is omitted, it is treated like a <code>?</code>, which matches every character. If <i>parameter</i> is <code>@</code> or <code>*</code>, the case modification operation is applied to each positional parameter in turn, and the expansion is the resultant list. If <i>parameter</i> is an array variable subscripted with <code>@</code> or <code>*</code>, the case modification operation is applied to each member of the array in turn, and the expansion is the resultant list. </p>
 </dd>
<dt>${<i>parameter</i><code>@</code><i>operator</i>}</dt>
<dd> <p> <code>Parameter transformation</code>. The expansion is either a transformation of the value of <i>parameter</i> or information about <i>parameter</i> itself, depending on the value of <i>operator</i>. Each <i>operator</i> is a single letter: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>U</code></dt>
<dd> <p> The expansion is a string that is the value of <i>parameter</i> with lowercase alphabetic characters converted to uppercase. </p>
 </dd>
<dt><code>u</code></dt>
<dd> <p> The expansion is a string that is the value of <i>parameter</i> with the first character converted to uppercase, if it is alphabetic. </p>
 </dd>
<dt><code>L</code></dt>
<dd> <p> The expansion is a string that is the value of <i>parameter</i> with uppercase alphabetic characters converted to lowercase. </p>
 </dd>
<dt><code>Q</code></dt>
<dd> <p> The expansion is a string that is the value of <i>parameter</i> quoted in a format that can be reused as input. </p>
 </dd>
<dt><code>E</code></dt>
<dd> <p> The expansion is a string that is the value of <i>parameter</i> with backslash escape sequences expanded as with the <code>$&#8216;...&#8216;</code> quoting mechanism. </p>
 </dd>
<dt><code>P</code></dt>
<dd> <p> The expansion is a string that is the result of expanding the value of <i>parameter</i> as if it were a prompt string (see <code>PROMPTING</code> below). </p>
 </dd>
<dt><code>A</code></dt>
<dd> <p> The expansion is a string in the form of an assignment statement or <code>declare</code> command that, if evaluated, will recreate <i>parameter</i> with its attributes and value. </p>
 </dd>
<dt><code>K</code></dt>
<dd> <p> Produces a possibly-quoted version of the value of <i>parameter</i>, except that it prints the values of indexed and associative arrays as a sequence of quoted key-value pairs (see <code>Arrays</code> above). </p>
 </dd>
<dt><code>a</code></dt>
<dd> <p> The expansion is a string consisting of flag values representing <i>parameter</i>&#8216;s attributes. </p>
 </dd></dl>
<p> If <i>parameter</i> is <code>@</code> or <code>*</code>, the operation is applied to each positional parameter in turn, and the expansion is the resultant list. If <i>parameter</i> is an array variable subscripted with <code>@</code> or <code>*</code>, the operation is applied to each member of the array in turn, and the expansion is the resultant list. </p>
<p> The result of the expansion is subject to word splitting and pathname expansion as described below. </dl>
 </dl>
  </p>
<h3>Command Substitution</h3>
<p> <i>Command substitution</i> allows the output of a command to replace the command name. There are two forms: </p>
<dl>
<dd> <p> <code>$(</code><i>command</i><code>)</code> </p>
 </dd></dl>
<p> or </p>
<dl>
<dd> <p> <code>`</code><i>command</i><code>`</code> </p>
 </dd></dl>
<p> <code>Bash</code> performs the expansion by executing <i>command</i> in a subshell environment and replacing the command substitution with the standard output of the command, with any trailing newlines deleted. Embedded newlines are not deleted, but they may be removed during word splitting. The command substitution <code>$(cat </code><i>file</i>) can be replaced by the equivalent but faster <code>$(&lt; </code><i>file</i>). </p>
<p> When the old-style backquote form of substitution is used, backslash retains its literal meaning except when followed by <code>$</code>, <code>`</code>, or <code>\</code>. The first backquote not preceded by a backslash terminates the command substitution. When using the $(<i>command</i>) form, all characters between the parentheses make up the command; none are treated specially. </p>
<p> Command substitutions may be nested. To nest when using the backquoted form, escape the inner backquotes with backslashes. </p>
<p> If the substitution appears within double quotes, word splitting and pathname expansion are not performed on the results.  </p>
<h3>Arithmetic Expansion</h3>
<p> Arithmetic expansion allows the evaluation of an arithmetic expression and the substitution of the result. The format for arithmetic expansion is: </p>
<dl>
<dd> <p> <code>$((</code><i>expression</i><code>))</code> </p>
 </dd></dl>
<p> The old format <code>$[</code><i>expression</i><code>]</code> is deprecated and will be removed in upcoming versions of bash. </p>
<p> The <i>expression</i> is treated as if it were within double quotes, but a double quote inside the parentheses is not treated specially. All tokens in the expression undergo parameter and variable expansion, command substitution, and quote removal. The result is treated as the arithmetic expression to be evaluated. Arithmetic expansions may be nested. </p>
<p> The evaluation is performed according to the rules listed below under <font SIZE="-1"><code>ARITHMETIC</code>EVALUATION <code>.</code> </font> If <i>expression</i> is invalid, <code>bash</code> prints a message indicating failure and no substitution occurs.  </p>
<h3>Process Substitution</h3>
<p> <i>Process substitution</i> allows a process&#8217;s input or output to be referred to using a filename. It takes the form of <code>&lt;(</code><i>list</i><code>)</code> or <code>&gt;(</code><i>list</i><code>)</code>. The process <i>list</i> is run asynchronously, and its input or output appears as a filename. This filename is passed as an argument to the current command as the result of the expansion. If the <code>&gt;(</code><i>list</i><code>)</code> form is used, writing to the file will provide input for <i>list</i>. If the <code>&lt;(</code><i>list</i><code>)</code> form is used, the file passed as an argument should be read to obtain the output of <i>list</i>. Process substitution is supported on systems that support named pipes (<i>FIFOs</i>) or the <code>/dev/fd</code> method of naming open files. </p>
<p> When available, process substitution is performed simultaneously with parameter and variable expansion, command substitution, and arithmetic expansion.  </p>
<h3>Word Splitting</h3>
<p> The shell scans the results of parameter expansion, command substitution, and arithmetic expansion that did not occur within double quotes for <i>word splitting</i>. </p>
<p> The shell treats each character of <font SIZE="-1"><code>IFS</code> </font> as a delimiter, and splits the results of the other expansions into words using these characters as field terminators. If <font SIZE="-1"><code>IFS</code> </font> is unset, or its value is exactly <code>&lt;space&gt;&lt;tab&gt;&lt;newline&gt;</code>, the default, then sequences of <code>&lt;space&gt;</code>, <code>&lt;tab&gt;</code>, and <code>&lt;newline&gt;</code> at the beginning and end of the results of the previous expansions are ignored, and any sequence of <font SIZE="-1"><code>IFS</code> </font> characters not at the beginning or end serves to delimit words. If <font SIZE="-1"><code>IFS</code> </font> has a value other than the default, then sequences of the whitespace characters <code>space</code>, <code>tab</code>, and <code>newline</code> are ignored at the beginning and end of the word, as long as the whitespace character is in the value of <font SIZE="-1"><code>IFS</code> </font> (an <font SIZE="-1"><code>IFS</code> </font> whitespace character). Any character in <font SIZE="-1"><code>IFS</code> </font> that is not <font SIZE="-1"><code>IFS</code> </font> whitespace, along with any adjacent <font SIZE="-1"><code>IFS</code> </font> whitespace characters, delimits a field. A sequence of <font SIZE="-1"><code>IFS</code> </font> whitespace characters is also treated as a delimiter. If the value of <font SIZE="-1"><code>IFS</code> </font> is null, no word splitting occurs. </p>
<p> Explicit null arguments (<code>&quot;&quot;</code> or <code>&#8216;&#8216;</code>) are retained and passed to commands as empty strings. Unquoted implicit null arguments, resulting from the expansion of parameters that have no values, are removed. If a parameter with no value is expanded within double quotes, a null argument results and is retained and passed to a command as an empty string. When a quoted null argument appears as part of a word whose expansion is non-null, the null argument is removed. That is, the word <code>-d&#8217;&#8216;</code> becomes <code>-d</code> after word splitting and null argument removal. </p>
<p> Note that if no expansion occurs, no splitting is performed.  </p>
<h3>Pathname Expansion</h3>
<p> After word splitting, unless the <code>-f</code> option has been set, <code>bash</code> scans each word for the characters <code>*</code>, <code>?</code>, and <code>[</code>. If one of these characters appears, and is not quoted, then the word is regarded as a <i>pattern</i>, and replaced with an alphabetically sorted list of filenames matching the pattern (see <font SIZE="-1"><code>Pattern Matching</code> </font> below). If no matching filenames are found, and the shell option <code>nullglob</code> is not enabled, the word is left unchanged. If the <code>nullglob</code> option is set, and no matches are found, the word is removed. If the <code>failglob</code> shell option is set, and no matches are found, an error message is printed and the command is not executed. If the shell option <code>nocaseglob</code> is enabled, the match is performed without regard to the case of alphabetic characters. Note that when using range expressions like [a-z] (see below), letters of the other case may be included, depending on the setting of <code>LC_COLLATE.</code> When a pattern is used for pathname expansion, the character <code>``.&#8216;&#8216;</code> at the start of a name or immediately following a slash must be matched explicitly, unless the shell option <code>dotglob</code> is set. The filenames <code>``.&#8216;&#8216;</code> and <code>``..&#8216;&#8216;</code> must always be matched explicitly, even if <code>dotglob</code> is set. In other cases, the <code>``.&#8216;&#8216;</code> character is not treated specially. When matching a pathname, the slash character must always be matched explicitly by a slash in the pattern, but in other matching contexts it can be matched by a special pattern character as described below under <font SIZE="-1"><code>Pattern</code>Matching <code>.</code> </font> See the description of <code>shopt</code> below under <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> for a description of the <code>nocaseglob</code>, <code>nullglob</code>, <code>failglob</code>, and <code>dotglob</code> shell options. </p>
<p> The <font SIZE="-1"><code>GLOBIGNORE</code> </font> shell variable may be used to restrict the set of file names matching a <i>pattern</i>. If <font SIZE="-1"><code>GLOBIGNORE</code> </font> is set, each matching file name that also matches one of the patterns in <font SIZE="-1"><code>GLOBIGNORE</code> </font> is removed from the list of matches. If the <code>nocaseglob</code> option is set, the matching against the patterns in <font SIZE="-1"><code>GLOBIGNORE</code> </font> is performed without regard to case. The filenames <code>``.&#8216;&#8216;</code> and <code>``..&#8216;&#8216;</code> are always ignored when <font SIZE="-1"><code>GLOBIGNORE</code> </font> is set and not null. However, setting <font SIZE="-1"><code>GLOBIGNORE</code> </font> to a non-null value has the effect of enabling the <code>dotglob</code> shell option, so all other filenames beginning with a <code>``.&#8216;&#8216;</code> will match. To get the old behavior of ignoring filenames beginning with a <code>``.&#8216;&#8216;</code>, make <code>``.*&#8216;&#8216;</code> one of the patterns in <font SIZE="-1"><code>GLOBIGNORE</code>. </font> The <code>dotglob</code> option is disabled when <font SIZE="-1"><code>GLOBIGNORE</code> </font> is unset. The pattern matching honors the setting of the <code>extglob</code> shell option. </p>
<p> <code>Pattern Matching</code> </p>
<p> Any character that appears in a pattern, other than the special pattern characters described below, matches itself. The NUL character may not occur in a pattern. A backslash escapes the following character; the escaping backslash is discarded when matching. The special pattern characters must be quoted if they are to be matched literally. </p>
<p> The special pattern characters have the following meanings: </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>*</code></dt>
<dd> <p> Matches any string, including the null string. When the <code>globstar</code> shell option is enabled, and <code>*</code> is used in a pathname expansion context, two adjacent <code>*</code>s used as a single pattern will match all files and zero or more directories and subdirectories. If followed by a <code>/</code>, two adjacent <code>*</code>s will match only directories and subdirectories. </p>
 </dd>
<dt><code>?</code></dt>
<dd> <p> Matches any single character. </p>
 </dd>
<dt><code>[...]</code></dt>
<dd> <p> Matches any one of the enclosed characters. A pair of characters separated by a hyphen denotes a <i>range expression</i>; any character that falls between those two characters, inclusive, using the current locale&#8217;s collating sequence and character set, is matched. If the first character following the <code>[</code> is a <code>!</code> or a <code>^</code> then any character not enclosed is matched. The sorting order of characters in range expressions is determined by the current locale and the values of the <font SIZE="-1"><code>LC_COLLATE</code> </font> or <font SIZE="-1"><code>LC_ALL</code> </font> shell variables, if set. To obtain the traditional interpretation of range expressions, where <code>[a-d]</code> is equivalent to <code>[abcd]</code>, set value of the <code>LC_ALL</code> shell variable to <code>C</code>, or enable the <code>globasciiranges</code> shell option. A <code>-</code> may be matched by including it as the first or last character in the set. A <code>]</code> may be matched by including it as the first character in the set. <br />
 </p>
<p> Within <code>[</code> and <code>]</code>, <i>character classes</i> can be specified using the syntax <code>[:</code><i>class</i><code>:]</code>, where <i>class</i> is one of the following classes defined in the POSIX standard: </p>
 </dd></dl>
<dl>
<dd> <p> <code>alnum alpha ascii blank cntrl digit graph lower print punct space upper word xdigit </code> <br />
 A character class matches any character belonging to that class. The <code>word</code> character class matches letters, digits, and the character _. <br />
 </p>
<p> Within <code>[</code> and <code>]</code>, an <i>equivalence class</i> can be specified using the syntax <code>[=</code><i>c</i><code>=]</code>, which matches all characters with the same collation weight (as defined by the current locale) as the character <i>c</i>. <br />
 </p>
<p> Within <code>[</code> and <code>]</code>, the syntax <code>[.</code><i>symbol</i><code>.]</code> matches the collating symbol <i>symbol</i>. </p>
 </dd></dl>
</dl>
<p> If the <code>extglob</code> shell option is enabled using the <code>shopt</code> builtin, several extended pattern matching operators are recognized. In the following description, a <i>pattern-list</i> is a list of one or more patterns separated by a <code>|</code>. Composite patterns may be formed using one or more of the following sub-patterns: </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>?(</code><i>pattern-list</i><code>)</code></dt>
<dd> <p> Matches zero or one occurrence of the given patterns </p>
 </dd>
<dt><code>*(</code><i>pattern-list</i><code>)</code></dt>
<dd> <p> Matches zero or more occurrences of the given patterns </p>
 </dd>
<dt><code>+(</code><i>pattern-list</i><code>)</code></dt>
<dd> <p> Matches one or more occurrences of the given patterns </p>
 </dd>
<dt><code>@(</code><i>pattern-list</i><code>)</code></dt>
<dd> <p> Matches one of the given patterns </p>
 </dd>
<dt><code>!(</code><i>pattern-list</i><code>)</code></dt>
<dd> <p> Matches anything except one of the given patterns </p>
 </dd></dl>
</dl>
<p> Complicated extended pattern matching against long strings is slow, especially when the patterns contain alternations and the strings contain multiple matches. Using separate matches against shorter strings, or using arrays of strings instead of a single long string, may be faster.  </p>
<h3>Quote Removal</h3>
<p> After the preceding expansions, all unquoted occurrences of the characters <code>\</code>, <code>&#8216;</code>, and <code>&quot;</code> that did not result from one of the above expansions are removed.  </p>
<h2>REDIRECTION</h2>
<p> Before a command is executed, its input and output may be <i>redirected</i> using a special notation interpreted by the shell. Redirection allows commands&#8217; file handles to be duplicated, opened, closed, made to refer to different files, and can change the files the command reads from and writes to. Redirection may also be used to modify file handles in the current shell execution environment. The following redirection operators may precede or appear anywhere within a <i>simple command</i> or may follow a <i>command</i>. Redirections are processed in the order they appear, from left to right. </p>
<p> Each redirection that may be preceded by a file descriptor number may instead be preceded by a word of the form {<i>varname</i>}. In this case, for each redirection operator except &gt;&amp;- and &lt;&amp;-, the shell will allocate a file descriptor greater than or equal to 10 and assign it to <i>varname</i>. If &gt;&amp;- or &lt;&amp;- is preceded by {<i>varname</i>}, the value of <i>varname</i> defines the file descriptor to close. If {<i>varname</i>} is supplied, the redirection persists beyond the scope of the command, allowing the shell programmer to manage the file descriptor himself. </p>
<p> In the following descriptions, if the file descriptor number is omitted, and the first character of the redirection operator is <code>&lt;</code>, the redirection refers to the standard input (file descriptor 0). If the first character of the redirection operator is <code>&gt;</code>, the redirection refers to the standard output (file descriptor 1). </p>
<p> The word following the redirection operator in the following descriptions, unless otherwise noted, is subjected to brace expansion, tilde expansion, parameter and variable expansion, command substitution, arithmetic expansion, quote removal, pathname expansion, and word splitting. If it expands to more than one word, <code>bash</code> reports an error. </p>
<p> Note that the order of redirections is significant. For example, the command </p>
<dl>
<dd> <p> ls <code>&gt;</code> dirlist 2 <code>&gt;&amp;</code>1 </p>
 </dd></dl>
<p> directs both standard output and standard error to the file <i>dirlist</i>, while the command </p>
<dl>
<dd> <p> ls 2 <code>&gt;&amp;</code>1 <code>&gt;</code> dirlist </p>
 </dd></dl>
<p> directs only the standard output to file <i>dirlist</i>, because the standard error was duplicated from the standard output before the standard output was redirected to <i>dirlist</i>. </p>
<p> <code>Bash</code> handles several filenames specially when they are used in redirections, as described in the following table. If the operating system on which <code>bash</code> is running provides these special files, bash will use them; otherwise it will emulate them internally with the behavior described below. </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>/dev/fd/</code><i>fd</i></dt>
<dd> <p> If <i>fd</i> is a valid integer, file descriptor <i>fd</i> is duplicated. </p>
 </dd>
<dt><code>/dev/stdin</code></dt>
<dd> <p> File descriptor 0 is duplicated. </p>
 </dd>
<dt><code>/dev/stdout</code></dt>
<dd> <p> File descriptor 1 is duplicated. </p>
 </dd>
<dt><code>/dev/stderr</code></dt>
<dd> <p> File descriptor 2 is duplicated. </p>
 </dd>
<dt><code>/dev/tcp/</code><i>host</i>/<i>port</i></dt>
<dd> <p> If <i>host</i> is a valid hostname or Internet address, and <i>port</i> is an integer port number or service name, <code>bash</code> attempts to open the corresponding TCP socket. </p>
 </dd>
<dt><code>/dev/udp/</code><i>host</i>/<i>port</i></dt>
<dd> <p> If <i>host</i> is a valid hostname or Internet address, and <i>port</i> is an integer port number or service name, <code>bash</code> attempts to open the corresponding UDP socket. </p>
 </dd></dl>
</dl>
<p> A failure to open or create a file causes the redirection to fail. </p>
<p> Redirections using file descriptors greater than 9 should be used with care, as they may conflict with file descriptors the shell uses internally. </p>
<p> Note that the <code>exec</code> builtin command can make redirections take effect in the current shell.  </p>
<h3>Redirecting Input</h3>
<p> Redirection of input causes the file whose name results from the expansion of <i>word</i> to be opened for reading on file descriptor <i>n</i>, or the standard input (file descriptor 0) if <i>n</i> is not specified. </p>
<p> The general format for redirecting input is: </p>
<dl>
<dd> <p> [<i>n</i>]<code>&lt;</code><i>word</i> </p>
 </dd></dl>
<h3>Redirecting Output</h3>
<p> Redirection of output causes the file whose name results from the expansion of <i>word</i> to be opened for writing on file descriptor <i>n</i>, or the standard output (file descriptor 1) if <i>n</i> is not specified. If the file does not exist it is created; if it does exist it is truncated to zero size. </p>
<p> The general format for redirecting output is: </p>
<dl>
<dd> <p> [<i>n</i>]<code>&gt;</code><i>word</i> </p>
 </dd></dl>
<p> If the redirection operator is <code>&gt;</code>, and the <code>noclobber</code> option to the <code>set</code> builtin has been enabled, the redirection will fail if the file whose name results from the expansion of <i>word</i> exists and is a regular file. If the redirection operator is <code>&gt;|</code>, or the redirection operator is <code>&gt;</code> and the <code>noclobber</code> option to the <code>set</code> builtin command is not enabled, the redirection is attempted even if the file named by <i>word</i> exists.  </p>
<h3>Appending Redirected Output</h3>
<p> Redirection of output in this fashion causes the file whose name results from the expansion of <i>word</i> to be opened for appending on file descriptor <i>n</i>, or the standard output (file descriptor 1) if <i>n</i> is not specified. If the file does not exist it is created. </p>
<p> The general format for appending output is: </p>
<dl>
<dd> <p> [<i>n</i>]<code>&gt;&gt;</code><i>word</i> </p>
 </dd></dl>
<h3>Redirecting Standard Output and Standard Error</h3>
<p> This construct allows both the standard output (file descriptor 1) and the standard error output (file descriptor 2) to be redirected to the file whose name is the expansion of <i>word</i>. </p>
<p> There are two formats for redirecting standard output and standard error: </p>
<dl>
<dd> <p> <code>&amp;&gt;</code><i>word</i> </p>
 </dd></dl>
<p> and </p>
<dl>
<dd> <p> <code>&gt;&amp;</code><i>word</i> </p>
 </dd></dl>
<p> Of the two forms, the first is preferred. This is semantically equivalent to </p>
<dl>
<dd> <p> <code>&gt;</code><i>word</i> 2 <code>&gt;&amp;</code>1 </p>
 </dd></dl>
<p> When using the second form, <i>word</i> may not expand to a number or <code>-</code>. If it does, other redirection operators apply (see <code>Duplicating File Descriptors</code> below) for compatibility reasons.  </p>
<h3>Appending Standard Output and Standard Error</h3>
<p> This construct allows both the standard output (file descriptor 1) and the standard error output (file descriptor 2) to be appended to the file whose name is the expansion of <i>word</i>. </p>
<p> The format for appending standard output and standard error is: </p>
<dl>
<dd> <p> <code>&amp;&gt;&gt;</code><i>word</i> </p>
 </dd></dl>
<p> This is semantically equivalent to </p>
<dl>
<dd> <p> <code>&gt;&gt;</code><i>word</i> 2 <code>&gt;&amp;</code>1 </p>
 </dd></dl>
<p> (see <code>Duplicating File Descriptors</code> below).  </p>
<h3>Here Documents</h3>
<p> This type of redirection instructs the shell to read input from the current source until a line containing only <i>delimiter</i> (with no trailing blanks) is seen. All of the lines read up to that point are then used as the standard input (or file descriptor <i>n</i> if <i>n</i> is specified) for a command. </p>
<p> The format of here-documents is: </p>
<dl>
<dd> <pre><code>[ n ] &lt;&lt; [ - ] word  here-document 
 delimiter 
</code></pre>
 </dd></dl>
<p> No parameter and variable expansion, command substitution, arithmetic expansion, or pathname expansion is performed on <i>word</i>. If any part of <i>word</i> is quoted, the <i>delimiter</i> is the result of quote removal on <i>word</i>, and the lines in the here-document are not expanded. If <i>word</i> is unquoted, all lines of the here-document are subjected to parameter expansion, command substitution, and arithmetic expansion, the character sequence <code>\&lt;newline&gt;</code> is ignored, and <code>\</code> must be used to quote the characters <code>\</code>, <code>$</code>, and <code>`</code>. </p>
<p> If the redirection operator is <code>&lt;&lt;-</code>, then all leading tab characters are stripped from input lines and the line containing <i>delimiter</i>. This allows here-documents within shell scripts to be indented in a natural fashion.  </p>
<h3>Here Strings</h3>
<p> A variant of here documents, the format is: </p>
<dl>
<dd> <pre><code>[ n ] &lt;&lt;&lt;  word 
</code></pre>
 </dd></dl>
<p> The <i>word</i> undergoes tilde expansion, parameter and variable expansion, command substitution, arithmetic expansion, and quote removal. Pathname expansion and word splitting are not performed. The result is supplied as a single string, with a newline appended, to the command on its standard input (or file descriptor <i>n</i> if <i>n</i> is specified).  </p>
<h3>Duplicating File Descriptors</h3>
<p> The redirection operator </p>
<dl>
<dd> <p> [<i>n</i>]<code>&lt;&amp;</code><i>word</i> </p>
 </dd></dl>
<p> is used to duplicate input file descriptors. If <i>word</i> expands to one or more digits, the file descriptor denoted by <i>n</i> is made to be a copy of that file descriptor. If the digits in <i>word</i> do not specify a file descriptor open for input, a redirection error occurs. If <i>word</i> evaluates to <code>-</code>, file descriptor <i>n</i> is closed. If <i>n</i> is not specified, the standard input (file descriptor 0) is used. </p>
<p> The operator </p>
<dl>
<dd> <p> [<i>n</i>]<code>&gt;&amp;</code><i>word</i> </p>
 </dd></dl>
<p> is used similarly to duplicate output file descriptors. If <i>n</i> is not specified, the standard output (file descriptor 1) is used. If the digits in <i>word</i> do not specify a file descriptor open for output, a redirection error occurs. If <i>word</i> evaluates to <code>-</code>, file descriptor <i>n</i> is closed. As a special case, if <i>n</i> is omitted, and <i>word</i> does not expand to one or more digits or <code>-</code>, the standard output and standard error are redirected as described previously.  </p>
<h3>Moving File Descriptors</h3>
<p> The redirection operator </p>
<dl>
<dd> <p> [<i>n</i>]<code>&lt;&amp;</code><i>digit</i><code>-</code> </p>
 </dd></dl>
<p> moves the file descriptor <i>digit</i> to file descriptor <i>n</i>, or the standard input (file descriptor 0) if <i>n</i> is not specified. <i>digit</i> is closed after being duplicated to <i>n</i>. </p>
<p> Similarly, the redirection operator </p>
<dl>
<dd> <p> [<i>n</i>]<code>&gt;&amp;</code><i>digit</i><code>-</code> </p>
 </dd></dl>
<p> moves the file descriptor <i>digit</i> to file descriptor <i>n</i>, or the standard output (file descriptor 1) if <i>n</i> is not specified.  </p>
<h3>Opening File Descriptors for Reading and Writing</h3>
<p> The redirection operator </p>
<dl>
<dd> <p> [<i>n</i>]<code>&lt;&gt;</code><i>word</i> </p>
 </dd></dl>
<p> causes the file whose name is the expansion of <i>word</i> to be opened for both reading and writing on file descriptor <i>n</i>, or on file descriptor 0 if <i>n</i> is not specified. If the file does not exist, it is created.  </p>
<h2>ALIASES</h2>
<p> <i>Aliases</i> allow a string to be substituted for a word when it is used as the first word of a simple command. The shell maintains a list of aliases that may be set and unset with the <code>alias</code> and <code>unalias</code> builtin commands (see <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below). The first word of each simple command, if unquoted, is checked to see if it has an alias. If so, that word is replaced by the text of the alias. The characters <code>/</code>, <code>$</code>, <code>`</code>, and <code>=</code> and any of the shell <i>metacharacters</i> or quoting characters listed above may not appear in an alias name. The replacement text may contain any valid shell input, including shell metacharacters. The first word of the replacement text is tested for aliases, but a word that is identical to an alias being expanded is not expanded a second time. This means that one may alias <code>ls</code> to <code>ls -F</code>, for instance, and <code>bash</code> does not try to recursively expand the replacement text. If the last character of the alias value is a <i>blank</i>, then the next command word following the alias is also checked for alias expansion. </p>
<p> Aliases are created and listed with the <code>alias</code> command, and removed with the <code>unalias</code> command. </p>
<p> There is no mechanism for using arguments in the replacement text. If arguments are needed, a shell function should be used (see <font SIZE="-1"><code>FUNCTIONS</code> </font> below). </p>
<p> Aliases are not expanded when the shell is not interactive, unless the <code>expand_aliases</code> shell option is set using <code>shopt</code> (see the description of <code>shopt</code> under <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code></font> below). </p>
<p> The rules concerning the definition and use of aliases are somewhat confusing. <code>Bash</code> always reads at least one complete line of input, and all lines that make up a compound command, before executing any of the commands on that line or the compound command. Aliases are expanded when a command is read, not when it is executed. Therefore, an alias definition appearing on the same line as another command does not take effect until the next line of input is read. The commands following the alias definition on that line are not affected by the new alias. This behavior is also an issue when functions are executed. Aliases are expanded when a function definition is read, not when the function is executed, because a function definition is itself a command. As a consequence, aliases defined in a function are not available until after that function is executed. To be safe, always put alias definitions on a separate line, and do not use <code>alias</code> in compound commands. </p>
<p> For almost every purpose, aliases are superseded by shell functions.  </p>
<h2>FUNCTIONS</h2>
<p> A shell function, defined as described above under <font SIZE="-1"><code>SHELL</code>GRAMMAR <code>,</code> </font> stores a series of commands for later execution. When the name of a shell function is used as a simple command name, the list of commands associated with that function name is executed. Functions are executed in the context of the current shell; no new process is created to interpret them (contrast this with the execution of a shell script). When a function is executed, the arguments to the function become the positional parameters during its execution. The special parameter <code>#</code> is updated to reflect the change. Special parameter <code>0</code> is unchanged. The first element of the <font SIZE="-1"><code>FUNCNAME</code> </font> variable is set to the name of the function while the function is executing. </p>
<p> All other aspects of the shell execution environment are identical between a function and its caller with these exceptions: the <font SIZE="-1"><code>DEBUG</code> </font> and <code>RETURN</code> traps (see the description of the <code>trap</code> builtin under <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below) are not inherited unless the function has been given the <code>trace</code> attribute (see the description of the <font SIZE="-1"><code>declare</code> </font> builtin below) or the <code>-o functrace</code> shell option has been enabled with the <code>set</code> builtin (in which case all functions inherit the <code>DEBUG</code> and <code>RETURN</code> traps), and the <font SIZE="-1"><code>ERR</code> </font> trap is not inherited unless the <code>-o errtrace</code> shell option has been enabled. </p>
<p> Variables local to the function may be declared with the <code>local</code> builtin command. Ordinarily, variables and their values are shared between the function and its caller. If a variable is declared <code>local</code>, the variable&#8217;s visible scope is restricted to that function and its children (including the functions it calls). Local variables &quot;shadow&quot; variables with the same name declared at previous scopes. For instance, a local variable declared in a function hides a global variable of the same name: references and assignments refer to the local variable, leaving the global variable unmodified. When the function returns, the global variable is once again visible. </p>
<p> The shell uses <i>dynamic scoping</i> to control a variable&#8217;s visibility within functions. With dynamic scoping, visible variables and their values are a result of the sequence of function calls that caused execution to reach the current function. The value of a variable that a function sees depends on its value within its caller, if any, whether that caller is the &quot;global&quot; scope or another shell function. This is also the value that a local variable declaration &quot;shadows&quot;, and the value that is restored when the function returns. </p>
<p> For example, if a variable <i>var</i> is declared as local in function <i>func1</i>, and <i>func1</i> calls another function <i>func2</i>, references to <i>var</i> made from within <i>func2</i> will resolve to the local variable <i>var</i> from <i>func1</i>, shadowing any global variable named <i>var</i>. </p>
<p> The <code>unset</code> builtin also acts using the same dynamic scope: if a variable is local to the current scope, <code>unset</code> will unset it; otherwise the unset will refer to the variable found in any calling scope as described above. If a variable at the current local scope is unset, it will remain so until it is reset in that scope or until the function returns. Once the function returns, any instance of the variable at a previous scope will become visible. If the unset acts on a variable at a previous scope, any instance of a variable with that name that had been shadowed will become visible. </p>
<p> The <code>FUNCNEST</code> variable, if set to a numeric value greater than 0, defines a maximum function nesting level. Function invocations that exceed the limit cause the entire command to abort. </p>
<p> If the builtin command <code>return</code> is executed in a function, the function completes and execution resumes with the next command after the function call. Any command associated with the <code>RETURN</code> trap is executed before execution resumes. When a function completes, the values of the positional parameters and the special parameter <code>#</code> are restored to the values they had prior to the function&#8217;s execution. </p>
<p> Function names and definitions may be listed with the <code>-f</code> option to the <code>declare</code> or <code>typeset</code> builtin commands. The <code>-F</code> option to <code>declare</code> or <code>typeset</code> will list the function names only (and optionally the source file and line number, if the <code>extdebug</code> shell option is enabled). Functions may be exported so that subshells automatically have them defined with the <code>-f</code> option to the <code>export</code> builtin. A function definition may be deleted using the <code>-f</code> option to the <code>unset</code> builtin. </p>
<p> Functions may be recursive. The <code>FUNCNEST</code> variable may be used to limit the depth of the function call stack and restrict the number of function invocations. By default, no limit is imposed on the number of recursive calls.  </p>
<h2>ARITHMETIC EVALUATION</h2>
<p> The shell allows arithmetic expressions to be evaluated, under certain circumstances (see the <code>let</code> and <code>declare</code> builtin commands, the <code>((</code> compound command, and <code>Arithmetic Expansion</code>). Evaluation is done in fixed-width integers with no check for overflow, though division by 0 is trapped and flagged as an error. The operators and their precedence, associativity, and values are the same as in the C language. The following list of operators is grouped into levels of equal-precedence operators. The levels are listed in order of decreasing precedence. </p>
<dl>
<dt><i>id</i>++ <i>id</i>-- </dt>
<dd> <p> variable post-increment and post-decrement </p>
 </dd>
<dt><code>- +</code></dt>
<dd> <p> unary minus and plus </p>
 </dd>
<dt><code>++</code><i>id</i> --<i>id</i></dt>
<dd> <p> variable pre-increment and pre-decrement </p>
 </dd>
<dt><code>! ~</code></dt>
<dd> <p> logical and bitwise negation </p>
 </dd>
<dt><code>**</code></dt>
<dd> <p> exponentiation </p>
 </dd>
<dt><code>* / %</code></dt>
<dd> <p> multiplication, division, remainder </p>
 </dd>
<dt><code>+ -</code></dt>
<dd> <p> addition, subtraction </p>
 </dd>
<dt><code>&lt;&lt; &gt;&gt;</code></dt>
<dd> <p> left and right bitwise shifts </p>
 </dd>
<dt><code>&lt;= &gt;= &lt; &gt;</code></dt>
<dd> <p> comparison </p>
 </dd>
<dt><code>== !=</code></dt>
<dd> <p> equality and inequality </p>
 </dd>
<dt><code>&amp;</code></dt>
<dd> <p> bitwise AND </p>
 </dd>
<dt><code>^</code></dt>
<dd> <p> bitwise exclusive OR </p>
 </dd>
<dt><code>|</code></dt>
<dd> <p> bitwise OR </p>
 </dd>
<dt><code>&amp;&amp;</code></dt>
<dd> <p> logical AND </p>
 </dd>
<dt><code>||</code></dt>
<dd> <p> logical OR </p>
 </dd>
<dt><i>expr</i>?<i>expr</i>:<i>expr</i></dt>
<dd> <p> conditional operator </p>
 </dd>
<dt><code>= *= /= %= += -= &lt;&lt;= &gt;&gt;= &amp;= ^= |=</code></dt>
<dd> <p> assignment </p>
 </dd>
<dt><i>expr1</i> , <i>expr2</i></dt>
<dd> <p> comma </p>
 </dd></dl>
<p> Shell variables are allowed as operands; parameter expansion is performed before the expression is evaluated. Within an expression, shell variables may also be referenced by name without using the parameter expansion syntax. A shell variable that is null or unset evaluates to 0 when referenced by name without using the parameter expansion syntax. The value of a variable is evaluated as an arithmetic expression when it is referenced, or when a variable which has been given the <i>integer</i> attribute using <code>declare -i</code> is assigned a value. A null value evaluates to 0. A shell variable need not have its <i>integer</i> attribute turned on to be used in an expression. </p>
<p> Integer constants follow the C language definition, without suffixes or character constants. Constants with a leading 0 are interpreted as octal numbers. A leading 0x or 0X denotes hexadecimal. Otherwise, numbers take the form [<i>base#</i>]n, where the optional <i>base</i> is a decimal number between 2 and 64 representing the arithmetic base, and <i>n</i> is a number in that base. If <i>base#</i> is omitted, then base 10 is used. When specifying <i>n</i>, if a non-digit is required, the digits greater than 9 are represented by the lowercase letters, the uppercase letters, @, and _, in that order. If <i>base</i> is less than or equal to 36, lowercase and uppercase letters may be used interchangeably to represent numbers between 10 and 35. </p>
<p> Operators are evaluated in order of precedence. Sub-expressions in parentheses are evaluated first and may override the precedence rules above.  </p>
<h2>CONDITIONAL EXPRESSIONS</h2>
<p> Conditional expressions are used by the <code>[[</code> compound command and the <code>test</code> and <code>[</code> builtin commands to test file attributes and perform string and arithmetic comparisons. The <code>test</code> and <code>[</code> commands determine their behavior based on the number of arguments; see the descriptions of those commands for any other command-specific actions. </p>
<p> Expressions are formed from the following unary or binary primaries. <code>Bash</code> handles several filenames specially when they are used in expressions. If the operating system on which <code>bash</code> is running provides these special files, bash will use them; otherwise it will emulate them internally with this behavior: If any <i>file</i> argument to one of the primaries is of the form <i>/dev/fd/n</i>, then file descriptor <i>n</i> is checked. If the <i>file</i> argument to one of the primaries is one of <i>/dev/stdin</i>, <i>/dev/stdout</i>, or <i>/dev/stderr</i>, file descriptor 0, 1, or 2, respectively, is checked. </p>
<p> Unless otherwise specified, primaries that operate on files follow symbolic links and operate on the target of the link, rather than the link itself. </p>
<p> When used with <code>[[</code>, the <code>&lt;</code> and <code>&gt;</code> operators sort lexicographically using the current locale. The <code>test</code> command sorts using ASCII ordering. </p>
<dl>
<dt><code>-a </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists. </p>
 </dd>
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
<dd> <p> True if <i>file</i> exists. </p>
 </dd>
<dt><code>-f </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and is a regular file. </p>
 </dd>
<dt><code>-g </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and is set-group-id. </p>
 </dd>
<dt><code>-h </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and is a symbolic link. </p>
 </dd>
<dt><code>-k </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and its ``sticky&#8217;&#8216; bit is set. </p>
 </dd>
<dt><code>-p </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and is a named pipe (FIFO). </p>
 </dd>
<dt><code>-r </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and is readable. </p>
 </dd>
<dt><code>-s </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and has a size greater than zero. </p>
 </dd>
<dt><code>-t </code><i>fd</i></dt>
<dd> <p> True if file descriptor <i>fd</i> is open and refers to a terminal. </p>
 </dd>
<dt><code>-u </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and its set-user-id bit is set. </p>
 </dd>
<dt><code>-w </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and is writable. </p>
 </dd>
<dt><code>-x </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and is executable. </p>
 </dd>
<dt><code>-G </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and is owned by the effective group id. </p>
 </dd>
<dt><code>-L </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and is a symbolic link. </p>
 </dd>
<dt><code>-N </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and has been modified since it was last read. </p>
 </dd>
<dt><code>-O </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and is owned by the effective user id. </p>
 </dd>
<dt><code>-S </code><i>file</i></dt>
<dd> <p> True if <i>file</i> exists and is a socket. </p>
 </dd>
<dt><i>file1</i><code>-ef</code><i>file2</i></dt>
<dd> <p> True if <i>file1</i> and <i>file2</i> refer to the same device and inode numbers. </p>
 </dd>
<dt><i>file1</i> -<code>nt</code><i>file2</i></dt>
<dd> <p> True if <i>file1</i> is newer (according to modification date) than <i>file2</i>, or if <i>file1</i> exists and file2 does not. </p>
 </dd>
<dt><i>file1</i> -<code>ot</code><i>file2</i></dt>
<dd> <p> True if <i>file1</i> is older than <i>file2</i>, or if <i>file2</i> exists and <i>file1</i> does not. </p>
 </dd>
<dt><code>-o </code><i>optname</i></dt>
<dd> <p> True if the shell option <i>optname</i> is enabled. See the list of options under the description of the <code>-o</code> option to the <code>set</code> builtin below. </p>
 </dd>
<dt><code>-v </code><i>varname</i></dt>
<dd> <p> True if the shell variable <i>varname</i> is set (has been assigned a value). </p>
 </dd>
<dt><code>-R </code><i>varname</i></dt>
<dd> <p> True if the shell variable <i>varname</i> is set and is a name reference. </p>
 </dd>
<dt><code>-z </code><i>string</i></dt>
<dd> <p> True if the length of <i>string</i> is zero. </p>
 </dd>
<dt><i>string</i></dt>
<dd>  </dd>
<dt><code>-n </code><i>string</i></dt>
<dd> <p> True if the length of <i>string</i> is non-zero. </p>
 </dd>
<dt><i>string1</i><code>==</code><i>string2</i></dt>
<dd>  </dd>
<dt><i>string1</i><code>=</code><i>string2</i></dt>
<dd> <p> True if the strings are equal. <code>=</code> should be used with the <code>test</code> command for POSIX conformance. When used with the <code>[[</code> command, this performs pattern matching as described above (<code>Compound Commands</code>). </p>
 </dd>
<dt><i>string1</i><code>!=</code><i>string2</i></dt>
<dd> <p> True if the strings are not equal. </p>
 </dd>
<dt><i>string1</i><code>&lt;</code><i>string2</i></dt>
<dd> <p> True if <i>string1</i> sorts before <i>string2</i> lexicographically. </p>
 </dd>
<dt><i>string1</i><code>&gt;</code><i>string2</i></dt>
<dd> <p> True if <i>string1</i> sorts after <i>string2</i> lexicographically. </p>
 </dd>
<dt><i>arg1</i><code>OP</code><i>arg2</i></dt>
<dd> <p> <font SIZE="-1"><code>OP</code> </font> is one of <code>-eq</code>, <code>-ne</code>, <code>-lt</code>, <code>-le</code>, <code>-gt</code>, or <code>-ge</code>. These arithmetic binary operators return true if <i>arg1</i> is equal to, not equal to, less than, less than or equal to, greater than, or greater than or equal to <i>arg2</i>, respectively. <i>Arg1</i> and <i>arg2</i> may be positive or negative integers. When used with the <code>[[</code> command, <i>Arg1</i> and <i>Arg2</i> are evaluated as arithmetic expressions (see <font SIZE="-1"><code>ARITHMETIC EVALUATION</code> </font> above). </p>
 </dd></dl>
<h2>SIMPLE COMMAND EXPANSION</h2>
<p> When a simple command is executed, the shell performs the following expansions, assignments, and redirections, from left to right, in the following order. </p>
<dl>
<dt>1.</dt>
<dd> <p> The words that the parser has marked as variable assignments (those preceding the command name) and redirections are saved for later processing. </p>
 </dd>
<dt>2.</dt>
<dd> <p> The words that are not variable assignments or redirections are expanded. If any words remain after expansion, the first word is taken to be the name of the command and the remaining words are the arguments. </p>
 </dd>
<dt>3.</dt>
<dd> <p> Redirections are performed as described above under <font SIZE="-1"><code>REDIRECTION</code>. </font> </p>
 </dd>
<dt>4.</dt>
<dd> <p> The text after the <code>=</code> in each variable assignment undergoes tilde expansion, parameter expansion, command substitution, arithmetic expansion, and quote removal before being assigned to the variable. </p>
 </dd></dl>
<p> If no command name results, the variable assignments affect the current shell environment. Otherwise, the variables are added to the environment of the executed command and do not affect the current shell environment. If any of the assignments attempts to assign a value to a readonly variable, an error occurs, and the command exits with a non-zero status. </p>
<p> If no command name results, redirections are performed, but do not affect the current shell environment. A redirection error causes the command to exit with a non-zero status. </p>
<p> If there is a command name left after expansion, execution proceeds as described below. Otherwise, the command exits. If one of the expansions contained a command substitution, the exit status of the command is the exit status of the last command substitution performed. If there were no command substitutions, the command exits with a status of zero.  </p>
<h2>COMMAND EXECUTION</h2>
<p> After a command has been split into words, if it results in a simple command and an optional list of arguments, the following actions are taken. </p>
<p> If the command name contains no slashes, the shell attempts to locate it. If there exists a shell function by that name, that function is invoked as described above in <font SIZE="-1"><code>FUNCTIONS</code>. </font> If the name does not match a function, the shell searches for it in the list of shell builtins. If a match is found, that builtin is invoked. </p>
<p> If the name is neither a shell function nor a builtin, and contains no slashes, <code>bash</code> searches each element of the <font SIZE="-1"><code>PATH</code> </font> for a directory containing an executable file by that name. <code>Bash</code> uses a hash table to remember the full pathnames of executable files (see <code>hash</code> under <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below). A full search of the directories in <font SIZE="-1"><code>PATH</code> </font> is performed only if the command is not found in the hash table. If the search is unsuccessful, the shell searches for a defined shell function named <code>command_not_found_handle</code>. If that function exists, it is invoked in a separate execution environment with the original command and the original command&#8217;s arguments as its arguments, and the function&#8217;s exit status becomes the exit status of that subshell. If that function is not defined, the shell prints an error message and returns an exit status of 127. </p>
<p> If the search is successful, or if the command name contains one or more slashes, the shell executes the named program in a separate execution environment. Argument 0 is set to the name given, and the remaining arguments to the command are set to the arguments given, if any. </p>
<p> If this execution fails because the file is not in executable format, and the file is not a directory, it is assumed to be a <i>shell script</i>, a file containing shell commands. A subshell is spawned to execute it. This subshell reinitializes itself, so that the effect is as if a new shell had been invoked to handle the script, with the exception that the locations of commands remembered by the parent (see <code>hash</code> below under <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code>)</font> are retained by the child. </p>
<p> If the program is a file beginning with <code>#!</code>, the remainder of the first line specifies an interpreter for the program. The shell executes the specified interpreter on operating systems that do not handle this executable format themselves. The arguments to the interpreter consist of a single optional argument following the interpreter name on the first line of the program, followed by the name of the program, followed by the command arguments, if any.  </p>
<h2>COMMAND EXECUTION ENVIRONMENT</h2>
<p> The shell has an <i>execution environment</i>, which consists of the following: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> open files inherited by the shell at invocation, as modified by redirections supplied to the <code>exec</code> builtin </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> the current working directory as set by <code>cd</code>, <code>pushd</code>, or <code>popd</code>, or inherited by the shell at invocation </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> the file creation mode mask as set by <code>umask</code> or inherited from the shell&#8217;s parent </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> current traps set by <code>trap</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> shell parameters that are set by variable assignment or with <code>set</code> or inherited from the shell&#8217;s parent in the environment </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> shell functions defined during execution or inherited from the shell&#8217;s parent in the environment </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> options enabled at invocation (either by default or with command-line arguments) or by <code>set</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> options enabled by <code>shopt</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> shell aliases defined with <code>alias</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> various process IDs, including those of background jobs, the value of <code>$$</code>, and the value of <font SIZE="-1"><code>PPID</code> </font> </p>
 </dd></dl>
<p> When a simple command other than a builtin or shell function is to be executed, it is invoked in a separate execution environment that consists of the following. Unless otherwise noted, the values are inherited from the shell. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> the shell&#8217;s open files, plus any modifications and additions specified by redirections to the command </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> the current working directory </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> the file creation mode mask </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> shell variables and functions marked for export, along with variables exported for the command, passed in the environment </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> traps caught by the shell are reset to the values inherited from the shell&#8217;s parent, and traps ignored by the shell are ignored </p>
 </dd></dl>
<p> A command invoked in this separate environment cannot affect the shell&#8217;s execution environment. </p>
<p> Command substitution, commands grouped with parentheses, and asynchronous commands are invoked in a subshell environment that is a duplicate of the shell environment, except that traps caught by the shell are reset to the values that the shell inherited from its parent at invocation. Builtin commands that are invoked as part of a pipeline are also executed in a subshell environment. Changes made to the subshell environment cannot affect the shell&#8217;s execution environment. </p>
<p> Subshells spawned to execute command substitutions inherit the value of the <code>-e</code> option from the parent shell. When not in <i>posix mode</i>, <code>bash</code> clears the <code>-e</code> option in such subshells. </p>
<p> If a command is followed by a <code>&amp;</code> and job control is not active, the default standard input for the command is the empty file <i>/dev/null</i>. Otherwise, the invoked command inherits the file descriptors of the calling shell as modified by redirections.  </p>
<h2>ENVIRONMENT</h2>
<p> When a program is invoked it is given an array of strings called the <i>environment</i>. This is a list of <i>name</i>-<i>value</i> pairs, of the form <i>name</i>=value. </p>
<p> The shell provides several ways to manipulate the environment. On invocation, the shell scans its own environment and creates a parameter for each name found, automatically marking it for <i>export</i> to child processes. Executed commands inherit the environment. The <code>export</code> and <code>declare -x</code> commands allow parameters and functions to be added to and deleted from the environment. If the value of a parameter in the environment is modified, the new value becomes part of the environment, replacing the old. The environment inherited by any executed command consists of the shell&#8217;s initial environment, whose values may be modified in the shell, less any pairs removed by the <code>unset</code> command, plus any additions via the <code>export</code> and <code>declare -x</code> commands. </p>
<p> The environment for any <i>simple command</i> or function may be augmented temporarily by prefixing it with parameter assignments, as described above in <font SIZE="-1"><code>PARAMETERS</code>. </font> These assignment statements affect only the environment seen by that command. </p>
<p> If the <code>-k</code> option is set (see the <code>set</code> builtin command below), then <i>all</i> parameter assignments are placed in the environment for a command, not just those that precede the command name. </p>
<p> When <code>bash</code> invokes an external command, the variable <code>_</code> is set to the full filename of the command and passed to that command in its environment.  </p>
<h2>EXIT STATUS</h2>
<p> The exit status of an executed command is the value returned by the <i>waitpid</i> system call or equivalent function. Exit statuses fall between 0 and 255, though, as explained below, the shell may use values above 125 specially. Exit statuses from shell builtins and compound commands are also limited to this range. Under certain circumstances, the shell will use special values to indicate specific failure modes. </p>
<p> For the shell&#8217;s purposes, a command which exits with a zero exit status has succeeded. An exit status of zero indicates success. A non-zero exit status indicates failure. When a command terminates on a fatal signal <i>N</i>, <code>bash</code> uses the value of 128+<i>N</i> as the exit status. </p>
<p> If a command is not found, the child process created to execute it returns a status of 127. If a command is found but is not executable, the return status is 126. </p>
<p> If a command fails because of an error during expansion or redirection, the exit status is greater than zero. </p>
<p> Shell builtin commands return a status of 0 (<i>true</i>) if successful, and non-zero (<i>false</i>) if an error occurs while they execute. All builtins return an exit status of 2 to indicate incorrect usage, generally invalid options or missing arguments. </p>
<p> <code>Bash</code> itself returns the exit status of the last command executed, unless a syntax error occurs, in which case it exits with a non-zero value. See also the <code>exit</code> builtin command below.  </p>
<h2>SIGNALS</h2>
<p> When <code>bash</code> is interactive, in the absence of any traps, it ignores <font SIZE="-1"><code>SIGTERM</code> </font> (so that <code>kill 0</code> does not kill an interactive shell), and <font SIZE="-1"><code>SIGINT</code> </font> is caught and handled (so that the <code>wait</code> builtin is interruptible). In all cases, <code>bash</code> ignores <font SIZE="-1"><code>SIGQUIT</code>. </font> If job control is in effect, <code>bash</code> ignores <font SIZE="-1"><code>SIGTTIN</code>, </font> <font SIZE="-1"><code>SIGTTOU</code>, </font> and <font SIZE="-1"><code>SIGTSTP</code>. </font> </p>
<p> Non-builtin commands run by <code>bash</code> have signal handlers set to the values inherited by the shell from its parent. When job control is not in effect, asynchronous commands ignore <font SIZE="-1"><code>SIGINT</code> </font> and <font SIZE="-1"><code>SIGQUIT</code> </font> in addition to these inherited handlers. Commands run as a result of command substitution ignore the keyboard-generated job control signals <font SIZE="-1"><code>SIGTTIN</code>, </font> <font SIZE="-1"><code>SIGTTOU</code>, </font> and <font SIZE="-1"><code>SIGTSTP</code>. </font> </p>
<p> The shell exits by default upon receipt of a <font SIZE="-1"><code>SIGHUP</code>. </font> Before exiting, an interactive shell resends the <font SIZE="-1"><code>SIGHUP</code> </font> to all jobs, running or stopped. Stopped jobs are sent <font SIZE="-1"><code>SIGCONT</code> </font> to ensure that they receive the <font SIZE="-1"><code>SIGHUP</code>. </font> To prevent the shell from sending the signal to a particular job, it should be removed from the jobs table with the <code>disown</code> builtin (see <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below) or marked to not receive <font SIZE="-1"><code>SIGHUP</code> </font> using <code>disown -h</code>. </p>
<p> If the <code>huponexit</code> shell option has been set with <code>shopt</code>, <code>bash</code> sends a <font SIZE="-1"><code>SIGHUP</code> </font> to all jobs when an interactive login shell exits. </p>
<p> If <code>bash</code> is waiting for a command to complete and receives a signal for which a trap has been set, the trap will not be executed until the command completes. When <code>bash</code> is waiting for an asynchronous command via the <code>wait</code> builtin, the reception of a signal for which a trap has been set will cause the <code>wait</code> builtin to return immediately with an exit status greater than 128, immediately after which the trap is executed.  </p>
<h2>JOB CONTROL</h2>
<p> <i>Job control</i> refers to the ability to selectively stop (<i>suspend</i>) the execution of processes and continue (<i>resume</i>) their execution at a later point. A user typically employs this facility via an interactive interface supplied jointly by the operating system kernel&#8217;s terminal driver and <code>bash</code>. </p>
<p> The shell associates a <i>job</i> with each pipeline. It keeps a table of currently executing jobs, which may be listed with the <code>jobs</code> command. When <code>bash</code> starts a job asynchronously (in the <i>background</i>), it prints a line that looks like: </p>
<dl>
<dd> <p> [1] 25647 </p>
 </dd></dl>
<p> indicating that this job is job number 1 and that the process ID of the last process in the pipeline associated with this job is 25647. All of the processes in a single pipeline are members of the same job. <code>Bash</code> uses the <i>job</i> abstraction as the basis for job control. </p>
<p> To facilitate the implementation of the user interface to job control, the operating system maintains the notion of a <i>current terminal process group ID</i>. Members of this process group (processes whose process group ID is equal to the current terminal process group ID) receive keyboard-generated signals such as <font SIZE="-1"><code>SIGINT</code>. </font> These processes are said to be in the <i>foreground</i>. <i>Background</i> processes are those whose process group ID differs from the terminal&#8217;s; such processes are immune to keyboard-generated signals. Only foreground processes are allowed to read from or, if the user so specifies with <code>stty tostop</code>, write to the terminal. Background processes which attempt to read from (write to when <code>stty tostop</code> is in effect) the terminal are sent a <font SIZE="-1"><code>SIGTTIN (SIGTTOU)</code> </font> signal by the kernel&#8217;s terminal driver, which, unless caught, suspends the process. </p>
<p> If the operating system on which <code>bash</code> is running supports job control, <code>bash</code> contains facilities to use it. Typing the <i>suspend</i> character (typically <code>^Z</code>, Control-Z) while a process is running causes that process to be stopped and returns control to <code>bash</code>. Typing the <i>delayed suspend</i> character (typically <code>^Y</code>, Control-Y) causes the process to be stopped when it attempts to read input from the terminal, and control to be returned to <code>bash</code>. The user may then manipulate the state of this job, using the <code>bg</code> command to continue it in the background, the <code>fg</code> command to continue it in the foreground, or the <code>kill</code> command to kill it. A <code>^Z</code> takes effect immediately, and has the additional side effect of causing pending output and typeahead to be discarded. </p>
<p> There are a number of ways to refer to a job in the shell. The character <code>%</code> introduces a job specification (<i>jobspec</i>). Job number <i>n</i> may be referred to as <code>%n</code>. A job may also be referred to using a prefix of the name used to start it, or using a substring that appears in its command line. For example, <code>%ce</code> refers to a stopped job whose command name begins with <code>ce</code>. If a prefix matches more than one job, <code>bash</code> reports an error. Using <code>%?ce</code>, on the other hand, refers to any job containing the string <code>ce</code> in its command line. If the substring matches more than one job, <code>bash</code> reports an error. The symbols <code>%%</code> and <code>%+</code> refer to the shell&#8217;s notion of the <i>current job</i>, which is the last job stopped while it was in the foreground or started in the background. The <i>previous job</i> may be referenced using <code>%-</code>. If there is only a single job, <code>%+</code> and <code>%-</code> can both be used to refer to that job. In output pertaining to jobs (e.g., the output of the <code>jobs</code> command), the current job is always flagged with a <code>+</code>, and the previous job with a <code>-</code>. A single % (with no accompanying job specification) also refers to the current job. </p>
<p> Simply naming a job can be used to bring it into the foreground: <code>%1</code> is a synonym for <code>``fg %1&#8217;&#8216;</code>, bringing job 1 from the background into the foreground. Similarly, <code>``%1 &amp;&#8216;&#8216;</code> resumes job 1 in the background, equivalent to <code>``bg %1&#8217;&#8216;</code>. </p>
<p> The shell learns immediately whenever a job changes state. Normally, <code>bash</code> waits until it is about to print a prompt before reporting changes in a job&#8217;s status so as to not interrupt any other output. If the <code>-b</code> option to the <code>set</code> builtin command is enabled, <code>bash</code> reports such changes immediately. Any trap on <font SIZE="-1"><code>SIGCHLD</code> </font> is executed for each child that exits. </p>
<p> If an attempt to exit <code>bash</code> is made while jobs are stopped (or, if the <code>checkjobs</code> shell option has been enabled using the <code>shopt</code> builtin, running), the shell prints a warning message, and, if the <code>checkjobs</code> option is enabled, lists the jobs and their statuses. The <code>jobs</code> command may then be used to inspect their status. If a second attempt to exit is made without an intervening command, the shell does not print another warning, and any stopped jobs are terminated. </p>
<p> When the shell is waiting for a job or process using the <code>wait</code> builtin, and job control is enabled, <code>wait</code> will return when the job changes state. The <code>-f</code> option causes <code>wait</code> to wait until the job or process terminates before returning.  </p>
<h2>PROMPTING</h2>
<p> When executing interactively, <code>bash</code> displays the primary prompt <font SIZE="-1"><code>PS1</code> </font> when it is ready to read a command, and the secondary prompt <font SIZE="-1"><code>PS2</code> </font> when it needs more input to complete a command. <code>Bash</code> displays <font SIZE="-1"><code>PS0</code> </font> after it reads a command but before executing it. <code>Bash</code> displays <font SIZE="-1"><code>PS4</code> </font> as described above before tracing each command when the <code>-x</code> option is enabled. <code>Bash</code> allows these prompt strings to be customized by inserting a number of backslash-escaped special characters that are decoded as follows: </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>\a</code></dt>
<dd> <p> an ASCII bell character (07) </p>
 </dd>
<dt><code>\d</code></dt>
<dd> <p> the date in &quot;Weekday Month Date&quot; format (e.g., &quot;Tue May 26&quot;) </p>
 </dd>
<dt><code>\D{</code><i>format</i>} </dt>
<dd> <p> the <i>format</i> is passed to <i><a href="/docs/linux/man/3-strftime/">strftime</a></i>(3) and the result is inserted into the prompt string; an empty <i>format</i> results in a locale-specific time representation. The braces are required </p>
 </dd>
<dt><code>\e</code></dt>
<dd> <p> an ASCII escape character (033) </p>
 </dd>
<dt><code>\h</code></dt>
<dd> <p> the hostname up to the first `.&#8216; </p>
 </dd>
<dt><code>\H</code></dt>
<dd> <p> the hostname </p>
 </dd>
<dt><code>\j</code></dt>
<dd> <p> the number of jobs currently managed by the shell </p>
 </dd>
<dt><code>\l</code></dt>
<dd> <p> the basename of the shell&#8217;s terminal device name </p>
 </dd>
<dt><code>\n</code></dt>
<dd> <p> newline </p>
 </dd>
<dt><code>\r</code></dt>
<dd> <p> carriage return </p>
 </dd>
<dt><code>\s</code></dt>
<dd> <p> the name of the shell, the basename of <code>$0</code> (the portion following the final slash) </p>
 </dd>
<dt><code>\t</code></dt>
<dd> <p> the current time in 24-hour HH:MM:SS format </p>
 </dd>
<dt><code>\T</code></dt>
<dd> <p> the current time in 12-hour HH:MM:SS format </p>
 </dd>
<dt><code>\@</code></dt>
<dd> <p> the current time in 12-hour am/pm format </p>
 </dd>
<dt><code>\A</code></dt>
<dd> <p> the current time in 24-hour HH:MM format </p>
 </dd>
<dt><code>\u</code></dt>
<dd> <p> the username of the current user </p>
 </dd>
<dt><code>\v</code></dt>
<dd> <p> the version of <code>bash</code> (e.g., 2.00) </p>
 </dd>
<dt><code>\V</code></dt>
<dd> <p> the release of <code>bash</code>, version + patch level (e.g., 2.00.0) </p>
 </dd>
<dt><code>\w</code></dt>
<dd> <p> the current working directory, with <font SIZE="-1"><code>$HOME</code> </font> abbreviated with a tilde (uses the value of the <font SIZE="-1"><code>PROMPT_DIRTRIM</code> </font> variable) </p>
 </dd>
<dt><code>\W</code></dt>
<dd> <p> the basename of the current working directory, with <font SIZE="-1"><code>$HOME</code> </font> abbreviated with a tilde </p>
 </dd>
<dt><code>\!</code></dt>
<dd> <p> the history number of this command </p>
 </dd>
<dt><code>\#</code></dt>
<dd> <p> the command number of this command </p>
 </dd>
<dt><code>\$</code></dt>
<dd> <p> if the effective UID is 0, a <code>#</code>, otherwise a <code>$</code> </p>
 </dd>
<dt><code>\</code><i>nnn</i></dt>
<dd> <p> the character corresponding to the octal number <i>nnn</i> </p>
 </dd>
<dt><code>\\</code></dt>
<dd> <p> a backslash </p>
 </dd>
<dt><code>\[</code></dt>
<dd> <p> begin a sequence of non-printing characters, which could be used to embed a terminal control sequence into the prompt </p>
 </dd>
<dt><code>\]</code></dt>
<dd> <p> end a sequence of non-printing characters </p>
 </dd></dl>
</dl>
<p> The command number and the history number are usually different: the history number of a command is its position in the history list, which may include commands restored from the history file (see <font SIZE="-1"><code>HISTORY</code> </font> below), while the command number is the position in the sequence of commands executed during the current shell session. After the string is decoded, it is expanded via parameter expansion, command substitution, arithmetic expansion, and quote removal, subject to the value of the <code>promptvars</code> shell option (see the description of the <code>shopt</code> command under <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below). This can have unwanted side effects if escaped portions of the string appear within command substitution or contain characters special to word expansion.  </p>
<h2>READLINE</h2>
<p> This is the library that handles reading input when using an interactive shell, unless the <code>--noediting</code> option is given at shell invocation. Line editing is also used when using the <code>-e</code> option to the <code>read</code> builtin. By default, the line editing commands are similar to those of Emacs. A vi-style line editing interface is also available. Line editing can be enabled at any time using the <code>-o emacs</code> or <code>-o vi</code> options to the <code>set</code> builtin (see <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below). To turn off line editing after the shell is running, use the <code>+o emacs</code> or <code>+o vi</code> options to the <code>set</code> builtin.  </p>
<h3>Readline Notation</h3>
<p> In this section, the Emacs-style notation is used to denote keystrokes. Control keys are denoted by C-<i>key</i>, e.g., C-n means Control-N. Similarly, <i>meta</i> keys are denoted by M-<i>key</i>, so M-x means Meta-X. (On keyboards without a <i>meta</i> key, M-<i>x</i> means ESC <i>x</i>, i.e., press the Escape key then the <i>x</i> key. This makes ESC the <i>meta prefix</i>. The combination M-C-<i>x</i> means ESC-Control-<i>x</i>, or press the Escape key then hold the Control key while pressing the <i>x</i> key.) </p>
<p> Readline commands may be given numeric <i>arguments</i>, which normally act as a repeat count. Sometimes, however, it is the sign of the argument that is significant. Passing a negative argument to a command that acts in the forward direction (e.g., <code>kill-line</code>) causes that command to act in a backward direction. Commands whose behavior with arguments deviates from this are noted below. </p>
<p> When a command is described as <i>killing</i> text, the text deleted is saved for possible future retrieval (<i>yanking</i>). The killed text is saved in a <i>kill ring</i>. Consecutive kills cause the text to be accumulated into one unit, which can be yanked all at once. Commands which do not kill text separate the chunks of text on the kill ring.  </p>
<h3>Readline Initialization</h3>
<p> Readline is customized by putting commands in an initialization file (the <i>inputrc</i> file). The name of this file is taken from the value of the <font SIZE="-1"><code>INPUTRC</code> </font> variable. If that variable is unset, the default is <i>~/.inputrc</i>. If that file does not exist or cannot be read, the ultimate default is <i>/etc/inputrc</i>. When a program which uses the readline library starts up, the initialization file is read, and the key bindings and variables are set. There are only a few basic constructs allowed in the readline initialization file. Blank lines are ignored. Lines beginning with a <code>#</code> are comments. Lines beginning with a <code>$</code> indicate conditional constructs. Other lines denote key bindings and variable settings. </p>
<p> The default key-bindings may be changed with an <i>inputrc</i> file. Other programs that use this library may add their own commands and bindings. </p>
<p> For example, placing </p>
<dl>
<dd> <p> M-Control-u: universal-argument </p>
 </dd></dl>
<p> or </p>
<dl>
<dd> <p> C-Meta-u: universal-argument </p>
 </dd></dl>
<p> into the <i>inputrc</i> would make M-C-u execute the readline command <i>universal-argument</i>. </p>
<p> The following symbolic character names are recognized: <i>RUBOUT</i>, <i>DEL</i>, <i>ESC</i>, <i>LFD</i>, <i>NEWLINE</i>, <i>RET</i>, <i>RETURN</i>, <i>SPC</i>, <i>SPACE</i>, and <i>TAB</i>. </p>
<p> In addition to command names, readline allows keys to be bound to a string that is inserted when the key is pressed (a <i>macro</i>).  </p>
<h3>Readline Key Bindings</h3>
<p> The syntax for controlling key bindings in the <i>inputrc</i> file is simple. All that is required is the name of the command or the text of a macro and a key sequence to which it should be bound. The name may be specified in one of two ways: as a symbolic key name, possibly with <i>Meta-</i> or <i>Control-</i> prefixes, or as a key sequence. </p>
<p> When using the form <code>keyname</code>:<i>function-name</i> or <i>macro</i>, <i>keyname</i> is the name of a key spelled out in English. For example: </p>
<dl>
<dd> <p> Control-u: universal-argument <br />
 Meta-Rubout: backward-kill-word <br />
 Control-o: &quot;&gt; output&quot; </p>
 </dd></dl>
<p> In the above example, <i>C-u</i> is bound to the function <code>universal-argument</code>, <i>M-DEL</i> is bound to the function <code>backward-kill-word</code>, and <i>C-o</i> is bound to run the macro expressed on the right hand side (that is, to insert the text ``&gt; output&#8217;&#8216; into the line). </p>
<p> In the second form, <code>&quot;keyseq&quot;</code>:<i>function-name</i> or <i>macro</i>, <code>keyseq</code> differs from <code>keyname</code> above in that strings denoting an entire key sequence may be specified by placing the sequence within double quotes. Some GNU Emacs style key escapes can be used, as in the following example, but the symbolic character names are not recognized. </p>
<dl>
<dd> <p> &quot;\C-u&quot;: universal-argument <br />
 &quot;\C-x\C-r&quot;: re-read-init-file <br />
 &quot;\e[11~&quot;: &quot;Function Key 1&quot; </p>
 </dd></dl>
<p> In this example, <i>C-u</i> is again bound to the function <code>universal-argument</code>. <i>C-x C-r</i> is bound to the function <code>re-read-init-file</code>, and <i>ESC [ 1 1 ~</i> is bound to insert the text ``Function Key 1&#8217;&#8216;. </p>
<p> The full set of GNU Emacs style escape sequences is </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>\C-</code></dt>
<dd> <p> control prefix </p>
 </dd>
<dt><code>\M-</code></dt>
<dd> <p> meta prefix </p>
 </dd>
<dt><code>\e</code></dt>
<dd> <p> an escape character </p>
 </dd>
<dt><code>\\</code></dt>
<dd> <p> backslash </p>
 </dd>
<dt><code>\</code></dt>
<dd> <p> literal &quot; </p>
 </dd>
<dt><code>\&#8216;</code></dt>
<dd> <p> literal &#8216; </p>
 </dd></dl>
</dl>
<p> In addition to the GNU Emacs style escape sequences, a second set of backslash escapes is available: </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>\a</code></dt>
<dd> <p> alert (bell) </p>
 </dd>
<dt><code>\b</code></dt>
<dd> <p> backspace </p>
 </dd>
<dt><code>\d</code></dt>
<dd> <p> delete </p>
 </dd>
<dt><code>\f</code></dt>
<dd> <p> form feed </p>
 </dd>
<dt><code>\n</code></dt>
<dd> <p> newline </p>
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
<dt><code>\</code><i>nnn</i></dt>
<dd> <p> the eight-bit character whose value is the octal value <i>nnn</i> (one to three digits) </p>
 </dd>
<dt><code>\x</code><i>HH</i></dt>
<dd> <p> the eight-bit character whose value is the hexadecimal value <i>HH</i> (one or two hex digits) </p>
 </dd></dl>
</dl>
<p> When entering the text of a macro, single or double quotes must be used to indicate a macro definition. Unquoted text is assumed to be a function name. In the macro body, the backslash escapes described above are expanded. Backslash will quote any other character in the macro text, including &quot; and &#8216;. </p>
<p> <code>Bash</code> allows the current readline key bindings to be displayed or modified with the <code>bind</code> builtin command. The editing mode may be switched during interactive use by using the <code>-o</code> option to the <code>set</code> builtin command (see <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below).  </p>
<h3>Readline Variables</h3>
<p> Readline has variables that can be used to further customize its behavior. A variable may be set in the <i>inputrc</i> file with a statement of the form </p>
<dl>
<dd> <p> <code>set</code> <i>variable-name</i> <i>value</i> </p>
 </dd></dl>
<p> or using the <code>bind</code> builtin command (see <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below). </p>
<p> Except where noted, readline variables can take the values <code>On</code> or <code>Off</code> (without regard to case). Unrecognized variable names are ignored. When a variable value is read, empty or null values, &quot;on&quot; (case-insensitive), and &quot;1&quot; are equivalent to <code>On</code>. All other values are equivalent to <code>Off</code>. The variables and their default values are: </p>
<dl>
<dt><code>bell-style (audible)</code></dt>
<dd> <p> Controls what happens when readline wants to ring the terminal bell. If set to <code>none</code>, readline never rings the bell. If set to <code>visible</code>, readline uses a visible bell if one is available. If set to <code>audible</code>, readline attempts to ring the terminal&#8217;s bell. </p>
 </dd>
<dt><code>bind-tty-special-chars (On)</code></dt>
<dd> <p> If set to <code>On</code>, readline attempts to bind the control characters treated specially by the kernel&#8217;s terminal driver to their readline equivalents. </p>
 </dd>
<dt><code>blink-matching-paren (Off)</code></dt>
<dd> <p> If set to <code>On</code>, readline attempts to briefly move the cursor to an opening parenthesis when a closing parenthesis is inserted. </p>
 </dd>
<dt><code>colored-completion-prefix (Off)</code></dt>
<dd> <p> If set to <code>On</code>, when listing completions, readline displays the common prefix of the set of possible completions using a different color. The color definitions are taken from the value of the <code>LS_COLORS</code> environment variable. </p>
 </dd>
<dt><code>colored-stats (Off)</code></dt>
<dd> <p> If set to <code>On</code>, readline displays possible completions using different colors to indicate their file type. The color definitions are taken from the value of the <code>LS_COLORS</code> environment variable. </p>
 </dd>
<dt><code>comment-begin (``#&#8216;&#8216;)</code></dt>
<dd> <p> The string that is inserted when the readline <code>insert-comment</code> command is executed. This command is bound to <code>M-#</code> in emacs mode and to <code>#</code> in vi command mode. </p>
 </dd>
<dt><code>completion-display-width (-1)</code></dt>
<dd> <p> The number of screen columns used to display possible matches when performing completion. The value is ignored if it is less than 0 or greater than the terminal screen width. A value of 0 will cause matches to be displayed one per line. The default value is -1. </p>
 </dd>
<dt><code>completion-ignore-case (Off)</code></dt>
<dd> <p> If set to <code>On</code>, readline performs filename matching and completion in a case-insensitive fashion. </p>
 </dd>
<dt><code>completion-map-case (Off)</code></dt>
<dd> <p> If set to <code>On</code>, and <code>completion-ignore-case</code> is enabled, readline treats hyphens (<i>-</i>) and underscores (<i>_</i>) as equivalent when performing case-insensitive filename matching and completion. </p>
 </dd>
<dt><code>completion-prefix-display-length (0)</code></dt>
<dd> <p> The length in characters of the common prefix of a list of possible completions that is displayed without modification. When set to a value greater than zero, common prefixes longer than this value are replaced with an ellipsis when displaying possible completions. </p>
 </dd>
<dt><code>completion-query-items (100)</code></dt>
<dd> <p> This determines when the user is queried about viewing the number of possible completions generated by the <code>possible-completions</code> command. It may be set to any integer value greater than or equal to zero. If the number of possible completions is greater than or equal to the value of this variable, readline will ask whether or not the user wishes to view them; otherwise they are simply listed on the terminal. </p>
 </dd>
<dt><code>convert-meta (On)</code></dt>
<dd> <p> If set to <code>On</code>, readline will convert characters with the eighth bit set to an ASCII key sequence by stripping the eighth bit and prefixing an escape character (in effect, using escape as the <i>meta prefix</i>). The default is <i>On</i>, but readline will set it to <i>Off</i> if the locale contains eight-bit characters. </p>
 </dd>
<dt><code>disable-completion (Off)</code></dt>
<dd> <p> If set to <code>On</code>, readline will inhibit word completion. Completion characters will be inserted into the line as if they had been mapped to <code>self-insert</code>. </p>
 </dd>
<dt><code>echo-control-characters (On)</code></dt>
<dd> <p> When set to <code>On</code>, on operating systems that indicate they support it, readline echoes a character corresponding to a signal generated from the keyboard. </p>
 </dd>
<dt><code>editing-mode (emacs)</code></dt>
<dd> <p> Controls whether readline begins with a set of key bindings similar to <i>Emacs</i> or <i>vi</i>. <code>editing-mode</code> can be set to either <code>emacs</code> or <code>vi</code>. </p>
 </dd>
<dt><code>emacs-mode-string (@)</code></dt>
<dd> <p> If the <i>show-mode-in-prompt</i> variable is enabled, this string is displayed immediately before the last line of the primary prompt when emacs editing mode is active. The value is expanded like a key binding, so the standard set of meta- and control prefixes and backslash escape sequences is available. Use the \1 and \2 escapes to begin and end sequences of non-printing characters, which can be used to embed a terminal control sequence into the mode string. </p>
 </dd>
<dt><code>enable-bracketed-paste (On)</code></dt>
<dd> <p> When set to <code>On</code>, readline will configure the terminal in a way that will enable it to insert each paste into the editing buffer as a single string of characters, instead of treating each character as if it had been read from the keyboard. This can prevent pasted characters from being interpreted as editing commands. </p>
 </dd>
<dt><code>enable-keypad (Off)</code></dt>
<dd> <p> When set to <code>On</code>, readline will try to enable the application keypad when it is called. Some systems need this to enable the arrow keys. </p>
 </dd>
<dt><code>enable-meta-key (On)</code></dt>
<dd> <p> When set to <code>On</code>, readline will try to enable any meta modifier key the terminal claims to support when it is called. On many terminals, the meta key is used to send eight-bit characters. </p>
 </dd>
<dt><code>expand-tilde (Off)</code></dt>
<dd> <p> If set to <code>On</code>, tilde expansion is performed when readline attempts word completion. </p>
 </dd>
<dt><code>history-preserve-point (Off)</code></dt>
<dd> <p> If set to <code>On</code>, the history code attempts to place point at the same location on each history line retrieved with <code>previous-history</code> or <code>next-history</code>. </p>
 </dd>
<dt><code>history-size (unset)</code></dt>
<dd> <p> Set the maximum number of history entries saved in the history list. If set to zero, any existing history entries are deleted and no new entries are saved. If set to a value less than zero, the number of history entries is not limited. By default, the number of history entries is set to the value of the <code>HISTSIZE</code> shell variable. If an attempt is made to set <i>history-size</i> to a non-numeric value, the maximum number of history entries will be set to 500. </p>
 </dd>
<dt><code>horizontal-scroll-mode (Off)</code></dt>
<dd> <p> When set to <code>On</code>, makes readline use a single line for display, scrolling the input horizontally on a single screen line when it becomes longer than the screen width rather than wrapping to a new line. This setting is automatically enabled for terminals of height 1. </p>
 </dd>
<dt><code>input-meta (Off)</code></dt>
<dd> <p> If set to <code>On</code>, readline will enable eight-bit input (that is, it will not strip the eighth bit from the characters it reads), regardless of what the terminal claims it can support. The name <code>meta-flag</code> is a synonym for this variable. The default is <i>Off</i>, but readline will set it to <i>On</i> if the locale contains eight-bit characters. </p>
 </dd>
<dt><code>isearch-terminators (``C-[C-J&#8217;&#8216;)</code></dt>
<dd> <p> The string of characters that should terminate an incremental search without subsequently executing the character as a command. If this variable has not been given a value, the characters <i>ESC</i> and <i>C-J</i> will terminate an incremental search. </p>
 </dd>
<dt><code>keymap (emacs)</code></dt>
<dd> <p> Set the current readline keymap. The set of valid keymap names is <i>emacs, emacs-standard, emacs-meta, emacs-ctlx, vi, vi-command</i>, and <i>vi-insert</i>. <i>vi</i> is equivalent to <i>vi-command</i>; <i>emacs</i> is equivalent to <i>emacs-standard</i>. The default value is <i>emacs</i>; the value of <code>editing-mode</code> also affects the default keymap. </p>
 </dd>
<dt><code>keyseq-timeout (500)</code></dt>
<dd> <p> Specifies the duration <i>readline</i> will wait for a character when reading an ambiguous key sequence (one that can form a complete key sequence using the input read so far, or can take additional input to complete a longer key sequence). If no input is received within the timeout, <i>readline</i> will use the shorter but complete key sequence. The value is specified in milliseconds, so a value of 1000 means that <i>readline</i> will wait one second for additional input. If this variable is set to a value less than or equal to zero, or to a non-numeric value, <i>readline</i> will wait until another key is pressed to decide which key sequence to complete. </p>
 </dd>
<dt><code>mark-directories (On)</code></dt>
<dd> <p> If set to <code>On</code>, completed directory names have a slash appended. </p>
 </dd>
<dt><code>mark-modified-lines (Off)</code></dt>
<dd> <p> If set to <code>On</code>, history lines that have been modified are displayed with a preceding asterisk (<code>*</code>). </p>
 </dd>
<dt><code>mark-symlinked-directories (Off)</code></dt>
<dd> <p> If set to <code>On</code>, completed names which are symbolic links to directories have a slash appended (subject to the value of <code>mark-directories</code>). </p>
 </dd>
<dt><code>match-hidden-files (On)</code></dt>
<dd> <p> This variable, when set to <code>On</code>, causes readline to match files whose names begin with a `.&#8216; (hidden files) when performing filename completion. If set to <code>Off</code>, the leading `.&#8216; must be supplied by the user in the filename to be completed. </p>
 </dd>
<dt><code>menu-complete-display-prefix (Off)</code></dt>
<dd> <p> If set to <code>On</code>, menu completion displays the common prefix of the list of possible completions (which may be empty) before cycling through the list. </p>
 </dd>
<dt><code>output-meta (Off)</code></dt>
<dd> <p> If set to <code>On</code>, readline will display characters with the eighth bit set directly rather than as a meta-prefixed escape sequence. The default is <i>Off</i>, but readline will set it to <i>On</i> if the locale contains eight-bit characters. </p>
 </dd>
<dt><code>page-completions (On)</code></dt>
<dd> <p> If set to <code>On</code>, readline uses an internal <i>more</i>-like pager to display a screenful of possible completions at a time. </p>
 </dd>
<dt><code>print-completions-horizontally (Off)</code></dt>
<dd> <p> If set to <code>On</code>, readline will display completions with matches sorted horizontally in alphabetical order, rather than down the screen. </p>
 </dd>
<dt><code>revert-all-at-newline (Off)</code></dt>
<dd> <p> If set to <code>On</code>, readline will undo all changes to history lines before returning when <code>accept-line</code> is executed. By default, history lines may be modified and retain individual undo lists across calls to <code>readline</code>. </p>
 </dd>
<dt><code>show-all-if-ambiguous (Off)</code></dt>
<dd> <p> This alters the default behavior of the completion functions. If set to <code>On</code>, words which have more than one possible completion cause the matches to be listed immediately instead of ringing the bell. </p>
 </dd>
<dt><code>show-all-if-unmodified (Off)</code></dt>
<dd> <p> This alters the default behavior of the completion functions in a fashion similar to <code>show-all-if-ambiguous</code>. If set to <code>On</code>, words which have more than one possible completion without any possible partial completion (the possible completions don&#8217;t share a common prefix) cause the matches to be listed immediately instead of ringing the bell. </p>
 </dd>
<dt><code>show-mode-in-prompt (Off)</code></dt>
<dd> <p> If set to <code>On</code>, add a string to the beginning of the prompt indicating the editing mode: emacs, vi command, or vi insertion. The mode strings are user-settable (e.g., <i>emacs-mode-string</i>). </p>
 </dd>
<dt><code>skip-completed-text (Off)</code></dt>
<dd> <p> If set to <code>On</code>, this alters the default completion behavior when inserting a single match into the line. It&#8217;s only active when performing completion in the middle of a word. If enabled, readline does not insert characters from the completion that match characters after point in the word being completed, so portions of the word following the cursor are not duplicated. </p>
 </dd>
<dt><code>vi-cmd-mode-string ((cmd))</code></dt>
<dd> <p> If the <i>show-mode-in-prompt</i> variable is enabled, this string is displayed immediately before the last line of the primary prompt when vi editing mode is active and in command mode. The value is expanded like a key binding, so the standard set of meta- and control prefixes and backslash escape sequences is available. Use the \1 and \2 escapes to begin and end sequences of non-printing characters, which can be used to embed a terminal control sequence into the mode string. </p>
 </dd>
<dt><code>vi-ins-mode-string ((ins))</code></dt>
<dd> <p> If the <i>show-mode-in-prompt</i> variable is enabled, this string is displayed immediately before the last line of the primary prompt when vi editing mode is active and in insertion mode. The value is expanded like a key binding, so the standard set of meta- and control prefixes and backslash escape sequences is available. Use the \1 and \2 escapes to begin and end sequences of non-printing characters, which can be used to embed a terminal control sequence into the mode string. </p>
 </dd>
<dt><code>visible-stats (Off)</code></dt>
<dd> <p> If set to <code>On</code>, a character denoting a file&#8217;s type as reported by <i><a href="/docs/linux/man/2-stat/">stat</a></i>(2) is appended to the filename when listing possible completions. </p>
 </dd></dl>
<h3>Readline Conditional Constructs</h3>
<p> Readline implements a facility similar in spirit to the conditional compilation features of the C preprocessor which allows key bindings and variable settings to be performed as the result of tests. There are four parser directives used. </p>
<dl>
<dt><code>$if</code></dt>
<dd> <p> The <code>$if</code> construct allows bindings to be made based on the editing mode, the terminal being used, or the application using readline. The text of the test, after any comparison operator, <br />
&nbsp;extends to the end of the line; unless otherwise noted, no characters are required to isolate it. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>mode</code></dt>
<dd> <p> The <code>mode=</code> form of the <code>$if</code> directive is used to test whether readline is in emacs or vi mode. This may be used in conjunction with the <code>set keymap</code> command, for instance, to set bindings in the <i>emacs-standard</i> and <i>emacs-ctlx</i> keymaps only if readline is starting out in emacs mode. </p>
 </dd>
<dt><code>term</code></dt>
<dd> <p> The <code>term=</code> form may be used to include terminal-specific key bindings, perhaps to bind the key sequences output by the terminal&#8217;s function keys. The word on the right side of the <code>=</code> is tested against both the full name of the terminal and the portion of the terminal name before the first <code>-</code>. This allows <i>sun</i> to match both <i>sun</i> and <i>sun-cmd</i>, for instance. </p>
 </dd>
<dt><code>version</code></dt>
<dd> <p> The <code>version</code> test may be used to perform comparisons against specific readline versions. The <code>version</code> expands to the current readline version. The set of comparison operators includes <code>=</code>, (and <code>==</code>), <code>!=</code>, <code>&lt;=</code>, <code>&gt;=</code>, <code>&lt;</code>, and <code>&gt;</code>. The version number supplied on the right side of the operator consists of a major version number, an optional decimal point, and an optional minor version (e.g., <code>7.1</code>). If the minor version is omitted, it is assumed to be <code>0</code>. The operator may be separated from the string <code>version</code> and from the version number argument by whitespace. </p>
 </dd>
<dt><code>application</code></dt>
<dd> <p> The <code>application</code> construct is used to include application-specific settings. Each program using the readline library sets the <i>application name</i>, and an initialization file can test for a particular value. This could be used to bind key sequences to functions useful for a specific program. For instance, the following command adds a key sequence that quotes the current or previous word in <code>bash</code>: </p>
 </dd>
<dl>
<dd> <pre><code>
 $if  Bash
# Quote the current or previous word
&quot;\C-xq&quot;: &quot;\eb\&quot;\ef\&quot;&quot;
 $endif 
</code></pre>
 </dd></dl>
<dt><i>variable</i></dt>
<dd> <p> The <i>variable</i> construct provides simple equality tests for readline variables and values. The permitted comparison operators are <i>=</i>, <i>==</i>, and <i>!=</i>. The variable name must be separated from the comparison operator by whitespace; the operator may be separated from the value on the right hand side by whitespace. Both string and boolean variables may be tested. Boolean variables must be tested against the values <i>on</i> and <i>off</i>. </p>
 </dd></dl>
</dl>
<dt><code>$endif</code></dt>
<dd> <p> This command, as seen in the previous example, terminates an <code>$if</code> command. </p>
 </dd>
<dt><code>$else</code></dt>
<dd> <p> Commands in this branch of the <code>$if</code> directive are executed if the test fails. </p>
 </dd>
<dt><code>$include</code></dt>
<dd> <p> This directive takes a single filename as an argument and reads commands and bindings from that file. For example, the following directive would read <i>/etc/inputrc</i>: </p>
 </dd>
<dl>
<dd> <pre><code>
 $include  /etc/inputrc 
</code></pre>
 </dd></dl>
</dl>
<h3>Searching</h3>
<p> Readline provides commands for searching through the command history (see <font SIZE="-1"><code>HISTORY</code> </font> below) for lines containing a specified string. There are two search modes: <i>incremental</i> and <i>non-incremental</i>. </p>
<p> Incremental searches begin before the user has finished typing the search string. As each character of the search string is typed, readline displays the next entry from the history matching the string typed so far. An incremental search requires only as many characters as needed to find the desired history entry. The characters present in the value of the <code>isearch-terminators</code> variable are used to terminate an incremental search. If that variable has not been assigned a value the Escape and Control-J characters will terminate an incremental search. Control-G will abort an incremental search and restore the original line. When the search is terminated, the history entry containing the search string becomes the current line. </p>
<p> To find other matching entries in the history list, type Control-S or Control-R as appropriate. This will search backward or forward in the history for the next entry matching the search string typed so far. Any other key sequence bound to a readline command will terminate the search and execute that command. For instance, a <i>newline</i> will terminate the search and accept the line, thereby executing the command from the history list. </p>
<p> Readline remembers the last incremental search string. If two Control-Rs are typed without any intervening characters defining a new search string, any remembered search string is used. </p>
<p> Non-incremental searches read the entire search string before starting to search for matching history lines. The search string may be typed by the user or be part of the contents of the current line.  </p>
<h3>Readline Command Names</h3>
<p> The following is a list of the names of the commands and the default key sequences to which they are bound. Command names without an accompanying key sequence are unbound by default. In the following descriptions, <i>point</i> refers to the current cursor position, and <i>mark</i> refers to a cursor position saved by the <code>set-mark</code> command. The text between the point and mark is referred to as the <i>region</i>.  </p>
<h3>Commands for Moving</h3>
<dl>
<dt><code>beginning-of-line (C-a)</code></dt>
<dd> <p> Move to the start of the current line. </p>
 </dd>
<dt><code>end-of-line (C-e)</code></dt>
<dd> <p> Move to the end of the line. </p>
 </dd>
<dt><code>forward-char (C-f)</code></dt>
<dd> <p> Move forward a character. </p>
 </dd>
<dt><code>backward-char (C-b)</code></dt>
<dd> <p> Move back a character. </p>
 </dd>
<dt><code>forward-word (M-f)</code></dt>
<dd> <p> Move forward to the end of the next word. Words are composed of alphanumeric characters (letters and digits). </p>
 </dd>
<dt><code>backward-word (M-b)</code></dt>
<dd> <p> Move back to the start of the current or previous word. Words are composed of alphanumeric characters (letters and digits). </p>
 </dd>
<dt><code>shell-forward-word</code></dt>
<dd> <p> Move forward to the end of the next word. Words are delimited by non-quoted shell metacharacters. </p>
 </dd>
<dt><code>shell-backward-word</code></dt>
<dd> <p> Move back to the start of the current or previous word. Words are delimited by non-quoted shell metacharacters. </p>
 </dd>
<dt><code>previous-screen-line</code></dt>
<dd> <p> Attempt to move point to the same physical screen column on the previous physical screen line. This will not have the desired effect if the current Readline line does not take up more than one physical line or if point is not greater than the length of the prompt plus the screen width. </p>
 </dd>
<dt><code>next-screen-line</code></dt>
<dd> <p> Attempt to move point to the same physical screen column on the next physical screen line. This will not have the desired effect if the current Readline line does not take up more than one physical line or if the length of the current Readline line is not greater than the length of the prompt plus the screen width. </p>
 </dd>
<dt><code>clear-display (M-C-l)</code></dt>
<dd> <p> Clear the screen and, if possible, the terminal&#8217;s scrollback buffer, then redraw the current line, leaving the current line at the top of the screen. </p>
 </dd>
<dt><code>clear-screen (C-l)</code></dt>
<dd> <p> Clear the screen, then redraw the current line, leaving the current line at the top of the screen. With an argument, refresh the current line without clearing the screen. </p>
 </dd>
<dt><code>redraw-current-line</code></dt>
<dd> <p> Refresh the current line. </p>
 </dd></dl>
<h3>Commands for Manipulating the History</h3>
<dl>
<dt><code>accept-line (Newline, Return)</code></dt>
<dd> <p> Accept the line regardless of where the cursor is. If this line is non-empty, add it to the history list according to the state of the <font SIZE="-1"><code>HISTCONTROL</code> </font> variable. If the line is a modified history line, then restore the history line to its original state. </p>
 </dd>
<dt><code>previous-history (C-p)</code></dt>
<dd> <p> Fetch the previous command from the history list, moving back in the list. </p>
 </dd>
<dt><code>next-history (C-n)</code></dt>
<dd> <p> Fetch the next command from the history list, moving forward in the list. </p>
 </dd>
<dt><code>beginning-of-history (M-&lt;)</code></dt>
<dd> <p> Move to the first line in the history. </p>
 </dd>
<dt><code>end-of-history (M-&gt;)</code></dt>
<dd> <p> Move to the end of the input history, i.e., the line currently being entered. </p>
 </dd>
<dt><code>reverse-search-history (C-r)</code></dt>
<dd> <p> Search backward starting at the current line and moving `up&#8217; through the history as necessary. This is an incremental search. </p>
 </dd>
<dt><code>forward-search-history (C-s)</code></dt>
<dd> <p> Search forward starting at the current line and moving `down&#8217; through the history as necessary. This is an incremental search. </p>
 </dd>
<dt><code>non-incremental-reverse-search-history (M-p)</code></dt>
<dd> <p> Search backward through the history starting at the current line using a non-incremental search for a string supplied by the user. </p>
 </dd>
<dt><code>non-incremental-forward-search-history (M-n)</code></dt>
<dd> <p> Search forward through the history using a non-incremental search for a string supplied by the user. </p>
 </dd>
<dt><code>history-search-forward</code></dt>
<dd> <p> Search forward through the history for the string of characters between the start of the current line and the point. This is a non-incremental search. </p>
 </dd>
<dt><code>history-search-backward</code></dt>
<dd> <p> Search backward through the history for the string of characters between the start of the current line and the point. This is a non-incremental search. </p>
 </dd>
<dt><code>history-substring-search-backward</code></dt>
<dd> <p> Search backward through the history for the string of characters between the start of the current line and the current cursor position (the <i>point</i>). The search string may match anywhere in a history line. This is a non-incremental search. </p>
 </dd>
<dt><code>history-substring-search-forward</code></dt>
<dd> <p> Search forward through the history for the string of characters between the start of the current line and the point. The search string may match anywhere in a history line. This is a non-incremental search. </p>
 </dd>
<dt><code>yank-nth-arg (M-C-y)</code></dt>
<dd> <p> Insert the first argument to the previous command (usually the second word on the previous line) at point. With an argument <i>n</i>, insert the <i>n</i>th word from the previous command (the words in the previous command begin with word 0). A negative argument inserts the <i>n</i>th word from the end of the previous command. Once the argument <i>n</i> is computed, the argument is extracted as if the &quot;!<i>n</i>&quot; history expansion had been specified. </p>
 </dd>
<dt><code>yank-last-arg (M-., M-_)</code></dt>
<dd> <p> Insert the last argument to the previous command (the last word of the previous history entry). With a numeric argument, behave exactly like <code>yank-nth-arg</code>. Successive calls to <code>yank-last-arg</code> move back through the history list, inserting the last word (or the word specified by the argument to the first call) of each line in turn. Any numeric argument supplied to these successive calls determines the direction to move through the history. A negative argument switches the direction through the history (back or forward). The history expansion facilities are used to extract the last word, as if the &quot;!$&quot; history expansion had been specified. </p>
 </dd>
<dt><code>shell-expand-line (M-C-e)</code></dt>
<dd> <p> Expand the line as the shell does. This performs alias and history expansion as well as all of the shell word expansions. See <font SIZE="-1"><code>HISTORY EXPANSION</code> </font> below for a description of history expansion. </p>
 </dd>
<dt><code>history-expand-line (M-^)</code></dt>
<dd> <p> Perform history expansion on the current line. See <font SIZE="-1"><code>HISTORY EXPANSION</code> </font> below for a description of history expansion. </p>
 </dd>
<dt><code>magic-space</code></dt>
<dd> <p> Perform history expansion on the current line and insert a space. See <font SIZE="-1"><code>HISTORY EXPANSION</code> </font> below for a description of history expansion. </p>
 </dd>
<dt><code>alias-expand-line</code></dt>
<dd> <p> Perform alias expansion on the current line. See <font SIZE="-1"><code>ALIASES</code> </font> above for a description of alias expansion. </p>
 </dd>
<dt><code>history-and-alias-expand-line</code></dt>
<dd> <p> Perform history and alias expansion on the current line. </p>
 </dd>
<dt><code>insert-last-argument (M-., M-_)</code></dt>
<dd> <p> A synonym for <code>yank-last-arg</code>. </p>
 </dd>
<dt><code>operate-and-get-next (C-o)</code></dt>
<dd> <p> Accept the current line for execution and fetch the next line relative to the current line from the history for editing. A numeric argument, if supplied, specifies the history entry to use instead of the current line. </p>
 </dd>
<dt><code>edit-and-execute-command (C-x C-e)</code></dt>
<dd> <p> Invoke an editor on the current command line, and execute the result as shell commands. <code>Bash</code> attempts to invoke <font SIZE="-1"><code>$VISUAL</code>, </font> <font SIZE="-1"><code>$EDITOR</code>, </font> and <i>emacs</i> as the editor, in that order. </p>
 </dd></dl>
<h3>Commands for Changing Text</h3>
<dl>
<dt><i>end-of-file</i> (usually C-d) </dt>
<dd> <p> The character indicating end-of-file as set, for example, by ``stty&#8217;&#8216;. If this character is read when there are no characters on the line, and point is at the beginning of the line, Readline interprets it as the end of input and returns <font SIZE="-1"><code>EOF</code>. </font> </p>
 </dd>
<dt><code>delete-char (C-d)</code></dt>
<dd> <p> Delete the character at point. If this function is bound to the same character as the tty <code>EOF</code> character, as <code>C-d</code> commonly is, see above for the effects. </p>
 </dd>
<dt><code>backward-delete-char (Rubout)</code></dt>
<dd> <p> Delete the character behind the cursor. When given a numeric argument, save the deleted text on the kill ring. </p>
 </dd>
<dt><code>forward-backward-delete-char</code></dt>
<dd> <p> Delete the character under the cursor, unless the cursor is at the end of the line, in which case the character behind the cursor is deleted. </p>
 </dd>
<dt><code>quoted-insert (C-q, C-v)</code></dt>
<dd> <p> Add the next character typed to the line verbatim. This is how to insert characters like <code>C-q</code>, for example. </p>
 </dd>
<dt><code>tab-insert (C-v TAB)</code></dt>
<dd> <p> Insert a tab character. </p>
 </dd>
<dt><code>self-insert (a, b, A, 1,&nbsp;!, ...)</code></dt>
<dd> <p> Insert the character typed. </p>
 </dd>
<dt><code>transpose-chars (C-t)</code></dt>
<dd> <p> Drag the character before point forward over the character at point, moving point forward as well. If point is at the end of the line, then this transposes the two characters before point. Negative arguments have no effect. </p>
 </dd>
<dt><code>transpose-words (M-t)</code></dt>
<dd> <p> Drag the word before point past the word after point, moving point over that word as well. If point is at the end of the line, this transposes the last two words on the line. </p>
 </dd>
<dt><code>upcase-word (M-u)</code></dt>
<dd> <p> Uppercase the current (or following) word. With a negative argument, uppercase the previous word, but do not move point. </p>
 </dd>
<dt><code>downcase-word (M-l)</code></dt>
<dd> <p> Lowercase the current (or following) word. With a negative argument, lowercase the previous word, but do not move point. </p>
 </dd>
<dt><code>capitalize-word (M-c)</code></dt>
<dd> <p> Capitalize the current (or following) word. With a negative argument, capitalize the previous word, but do not move point. </p>
 </dd>
<dt><code>overwrite-mode</code></dt>
<dd> <p> Toggle overwrite mode. With an explicit positive numeric argument, switches to overwrite mode. With an explicit non-positive numeric argument, switches to insert mode. This command affects only <code>emacs</code> mode; <code>vi</code> mode does overwrite differently. Each call to <i>readline()</i> starts in insert mode. In overwrite mode, characters bound to <code>self-insert</code> replace the text at point rather than pushing the text to the right. Characters bound to <code>backward-delete-char</code> replace the character before point with a space. By default, this command is unbound. </p>
 </dd></dl>
<h3>Killing and Yanking</h3>
<dl>
<dt><code>kill-line (C-k)</code></dt>
<dd> <p> Kill the text from point to the end of the line. </p>
 </dd>
<dt><code>backward-kill-line (C-x Rubout)</code></dt>
<dd> <p> Kill backward to the beginning of the line. </p>
 </dd>
<dt><code>unix-line-discard (C-u)</code></dt>
<dd> <p> Kill backward from point to the beginning of the line. The killed text is saved on the kill-ring. </p>
 </dd>
<dt><code>kill-whole-line</code></dt>
<dd> <p> Kill all characters on the current line, no matter where point is. </p>
 </dd>
<dt><code>kill-word (M-d)</code></dt>
<dd> <p> Kill from point to the end of the current word, or if between words, to the end of the next word. Word boundaries are the same as those used by <code>forward-word</code>. </p>
 </dd>
<dt><code>backward-kill-word (M-Rubout)</code></dt>
<dd> <p> Kill the word behind point. Word boundaries are the same as those used by <code>backward-word</code>. </p>
 </dd>
<dt><code>shell-kill-word</code></dt>
<dd> <p> Kill from point to the end of the current word, or if between words, to the end of the next word. Word boundaries are the same as those used by <code>shell-forward-word</code>. </p>
 </dd>
<dt><code>shell-backward-kill-word</code></dt>
<dd> <p> Kill the word behind point. Word boundaries are the same as those used by <code>shell-backward-word</code>. </p>
 </dd>
<dt><code>unix-word-rubout (C-w)</code></dt>
<dd> <p> Kill the word behind point, using white space as a word boundary. The killed text is saved on the kill-ring. </p>
 </dd>
<dt><code>unix-filename-rubout</code></dt>
<dd> <p> Kill the word behind point, using white space and the slash character as the word boundaries. The killed text is saved on the kill-ring. </p>
 </dd>
<dt><code>delete-horizontal-space (M-\)</code></dt>
<dd> <p> Delete all spaces and tabs around point. </p>
 </dd>
<dt><code>kill-region</code></dt>
<dd> <p> Kill the text in the current region. </p>
 </dd>
<dt><code>copy-region-as-kill</code></dt>
<dd> <p> Copy the text in the region to the kill buffer. </p>
 </dd>
<dt><code>copy-backward-word</code></dt>
<dd> <p> Copy the word before point to the kill buffer. The word boundaries are the same as <code>backward-word</code>. </p>
 </dd>
<dt><code>copy-forward-word</code></dt>
<dd> <p> Copy the word following point to the kill buffer. The word boundaries are the same as <code>forward-word</code>. </p>
 </dd>
<dt><code>yank (C-y)</code></dt>
<dd> <p> Yank the top of the kill ring into the buffer at point. </p>
 </dd>
<dt><code>yank-pop (M-y)</code></dt>
<dd> <p> Rotate the kill ring, and yank the new top. Only works following <code>yank</code> or <code>yank-pop</code>. </p>
 </dd></dl>
<h3>Numeric Arguments</h3>
<dl>
<dt><code>digit-argument (M-0, M-1, ..., M--)</code></dt>
<dd> <p> Add this digit to the argument already accumulating, or start a new argument. M-- starts a negative argument. </p>
 </dd>
<dt><code>universal-argument</code></dt>
<dd> <p> This is another way to specify an argument. If this command is followed by one or more digits, optionally with a leading minus sign, those digits define the argument. If the command is followed by digits, executing <code>universal-argument</code> again ends the numeric argument, but is otherwise ignored. As a special case, if this command is immediately followed by a character that is neither a digit nor minus sign, the argument count for the next command is multiplied by four. The argument count is initially one, so executing this function the first time makes the argument count four, a second time makes the argument count sixteen, and so on. </p>
 </dd></dl>
<h3>Completing</h3>
<dl>
<dt><code>complete (TAB)</code></dt>
<dd> <p> Attempt to perform completion on the text before point. <code>Bash</code> attempts completion treating the text as a variable (if the text begins with <code>$</code>), username (if the text begins with <code>~</code>), hostname (if the text begins with <code>@</code>), or command (including aliases and functions) in turn. If none of these produces a match, filename completion is attempted. </p>
 </dd>
<dt><code>possible-completions (M-?)</code></dt>
<dd> <p> List the possible completions of the text before point. </p>
 </dd>
<dt><code>insert-completions (M-*)</code></dt>
<dd> <p> Insert all completions of the text before point that would have been generated by <code>possible-completions</code>. </p>
 </dd>
<dt><code>menu-complete</code></dt>
<dd> <p> Similar to <code>complete</code>, but replaces the word to be completed with a single match from the list of possible completions. Repeated execution of <code>menu-complete</code> steps through the list of possible completions, inserting each match in turn. At the end of the list of completions, the bell is rung (subject to the setting of <code>bell-style</code>) and the original text is restored. An argument of <i>n</i> moves <i>n</i> positions forward in the list of matches; a negative argument may be used to move backward through the list. This command is intended to be bound to <code>TAB</code>, but is unbound by default. </p>
 </dd>
<dt><code>menu-complete-backward</code></dt>
<dd> <p> Identical to <code>menu-complete</code>, but moves backward through the list of possible completions, as if <code>menu-complete</code> had been given a negative argument. This command is unbound by default. </p>
 </dd>
<dt><code>delete-char-or-list</code></dt>
<dd> <p> Deletes the character under the cursor if not at the beginning or end of the line (like <code>delete-char</code>). If at the end of the line, behaves identically to <code>possible-completions</code>. This command is unbound by default. </p>
 </dd>
<dt><code>complete-filename (M-/)</code></dt>
<dd> <p> Attempt filename completion on the text before point. </p>
 </dd>
<dt><code>possible-filename-completions (C-x /)</code></dt>
<dd> <p> List the possible completions of the text before point, treating it as a filename. </p>
 </dd>
<dt><code>complete-username (M-~)</code></dt>
<dd> <p> Attempt completion on the text before point, treating it as a username. </p>
 </dd>
<dt><code>possible-username-completions (C-x ~)</code></dt>
<dd> <p> List the possible completions of the text before point, treating it as a username. </p>
 </dd>
<dt><code>complete-variable (M-$)</code></dt>
<dd> <p> Attempt completion on the text before point, treating it as a shell variable. </p>
 </dd>
<dt><code>possible-variable-completions (C-x $)</code></dt>
<dd> <p> List the possible completions of the text before point, treating it as a shell variable. </p>
 </dd>
<dt><code>complete-hostname (M-@)</code></dt>
<dd> <p> Attempt completion on the text before point, treating it as a hostname. </p>
 </dd>
<dt><code>possible-hostname-completions (C-x @)</code></dt>
<dd> <p> List the possible completions of the text before point, treating it as a hostname. </p>
 </dd>
<dt><code>complete-command (M-!)</code></dt>
<dd> <p> Attempt completion on the text before point, treating it as a command name. Command completion attempts to match the text against aliases, reserved words, shell functions, shell builtins, and finally executable filenames, in that order. </p>
 </dd>
<dt><code>possible-command-completions (C-x !)</code></dt>
<dd> <p> List the possible completions of the text before point, treating it as a command name. </p>
 </dd>
<dt><code>dynamic-complete-history (M-TAB)</code></dt>
<dd> <p> Attempt completion on the text before point, comparing the text against lines from the history list for possible completion matches. </p>
 </dd>
<dt><code>dabbrev-expand</code></dt>
<dd> <p> Attempt menu completion on the text before point, comparing the text against lines from the history list for possible completion matches. </p>
 </dd>
<dt><code>complete-into-braces (M-{)</code></dt>
<dd> <p> Perform filename completion and insert the list of possible completions enclosed within braces so the list is available to the shell (see <code>Brace Expansion</code> above). </p>
 </dd></dl>
<h3>Keyboard Macros</h3>
<dl>
<dt><code>start-kbd-macro (C-x ()</code></dt>
<dd> <p> Begin saving the characters typed into the current keyboard macro. </p>
 </dd>
<dt><code>end-kbd-macro (C-x ))</code></dt>
<dd> <p> Stop saving the characters typed into the current keyboard macro and store the definition. </p>
 </dd>
<dt><code>call-last-kbd-macro (C-x e)</code></dt>
<dd> <p> Re-execute the last keyboard macro defined, by making the characters in the macro appear as if typed at the keyboard. </p>
 </dd>
<dt><code>print-last-kbd-macro ()</code></dt>
<dd> <p> Print the last keyboard macro defined in a format suitable for the <i>inputrc</i> file. </p>
 </dd></dl>
<h3>Miscellaneous</h3>
<dl>
<dt><code>re-read-init-file (C-x C-r)</code></dt>
<dd> <p> Read in the contents of the <i>inputrc</i> file, and incorporate any bindings or variable assignments found there. </p>
 </dd>
<dt><code>abort (C-g)</code></dt>
<dd> <p> Abort the current editing command and ring the terminal&#8217;s bell (subject to the setting of <code>bell-style</code>). </p>
 </dd>
<dt><code>do-lowercase-version (M-A, M-B, M-</code><i>x</i>, ...) </dt>
<dd> <p> If the metafied character <i>x</i> is uppercase, run the command that is bound to the corresponding metafied lowercase character. The behavior is undefined if <i>x</i> is already lowercase. </p>
 </dd>
<dt><code>prefix-meta (ESC)</code></dt>
<dd> <p> Metafy the next character typed. <font SIZE="-1"><code>ESC</code> </font> <code>f</code> is equivalent to <code>Meta-f</code>. </p>
 </dd>
<dt><code>undo (C-_, C-x C-u)</code></dt>
<dd> <p> Incremental undo, separately remembered for each line. </p>
 </dd>
<dt><code>revert-line (M-r)</code></dt>
<dd> <p> Undo all changes made to this line. This is like executing the <code>undo</code> command enough times to return the line to its initial state. </p>
 </dd>
<dt><code>tilde-expand (M-&amp;)</code></dt>
<dd> <p> Perform tilde expansion on the current word. </p>
 </dd>
<dt><code>set-mark (C-@, M-&lt;space&gt;)</code></dt>
<dd> <p> Set the mark to the point. If a numeric argument is supplied, the mark is set to that position. </p>
 </dd>
<dt><code>exchange-point-and-mark (C-x C-x)</code></dt>
<dd> <p> Swap the point with the mark. The current cursor position is set to the saved position, and the old cursor position is saved as the mark. </p>
 </dd>
<dt><code>character-search (C-])</code></dt>
<dd> <p> A character is read and point is moved to the next occurrence of that character. A negative count searches for previous occurrences. </p>
 </dd>
<dt><code>character-search-backward (M-C-])</code></dt>
<dd> <p> A character is read and point is moved to the previous occurrence of that character. A negative count searches for subsequent occurrences. </p>
 </dd>
<dt><code>skip-csi-sequence</code></dt>
<dd> <p> Read enough characters to consume a multi-key sequence such as those defined for keys like Home and End. Such sequences begin with a Control Sequence Indicator (CSI), usually ESC-[. If this sequence is bound to &quot;\[&quot;, keys producing such sequences will have no effect unless explicitly bound to a readline command, instead of inserting stray characters into the editing buffer. This is unbound by default, but usually bound to ESC-[. </p>
 </dd>
<dt><code>insert-comment (M-#)</code></dt>
<dd> <p> Without a numeric argument, the value of the readline <code>comment-begin</code> variable is inserted at the beginning of the current line. If a numeric argument is supplied, this command acts as a toggle: if the characters at the beginning of the line do not match the value of <code>comment-begin</code>, the value is inserted, otherwise the characters in <code>comment-begin</code> are deleted from the beginning of the line. In either case, the line is accepted as if a newline had been typed. The default value of <code>comment-begin</code> causes this command to make the current line a shell comment. If a numeric argument causes the comment character to be removed, the line will be executed by the shell. </p>
 </dd>
<dt><code>glob-complete-word (M-g)</code></dt>
<dd> <p> The word before point is treated as a pattern for pathname expansion, with an asterisk implicitly appended. This pattern is used to generate a list of matching filenames for possible completions. </p>
 </dd>
<dt><code>glob-expand-word (C-x *)</code></dt>
<dd> <p> The word before point is treated as a pattern for pathname expansion, and the list of matching filenames is inserted, replacing the word. If a numeric argument is supplied, an asterisk is appended before pathname expansion. </p>
 </dd>
<dt><code>glob-list-expansions (C-x g)</code></dt>
<dd> <p> The list of expansions that would have been generated by <code>glob-expand-word</code> is displayed, and the line is redrawn. If a numeric argument is supplied, an asterisk is appended before pathname expansion. </p>
 </dd>
<dt><code>dump-functions</code></dt>
<dd> <p> Print all of the functions and their key bindings to the readline output stream. If a numeric argument is supplied, the output is formatted in such a way that it can be made part of an <i>inputrc</i> file. </p>
 </dd>
<dt><code>dump-variables</code></dt>
<dd> <p> Print all of the settable readline variables and their values to the readline output stream. If a numeric argument is supplied, the output is formatted in such a way that it can be made part of an <i>inputrc</i> file. </p>
 </dd>
<dt><code>dump-macros</code></dt>
<dd> <p> Print all of the readline key sequences bound to macros and the strings they output. If a numeric argument is supplied, the output is formatted in such a way that it can be made part of an <i>inputrc</i> file. </p>
 </dd>
<dt><code>display-shell-version (C-x C-v)</code></dt>
<dd> <p> Display version information about the current instance of <code>bash</code>. </p>
 </dd></dl>
<h3>Programmable Completion</h3>
<p> When word completion is attempted for an argument to a command for which a completion specification (a <i>compspec</i>) has been defined using the <code>complete</code> builtin (see <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below), the programmable completion facilities are invoked. </p>
<p> First, the command name is identified. If the command word is the empty string (completion attempted at the beginning of an empty line), any compspec defined with the <code>-E</code> option to <code>complete</code> is used. If a compspec has been defined for that command, the compspec is used to generate the list of possible completions for the word. If the command word is a full pathname, a compspec for the full pathname is searched for first. If no compspec is found for the full pathname, an attempt is made to find a compspec for the portion following the final slash. If those searches do not result in a compspec, any compspec defined with the <code>-D</code> option to <code>complete</code> is used as the default. If there is no default compspec, <code>bash</code> attempts alias expansion on the command word as a final resort, and attempts to find a compspec for the command word from any successful expansion. </p>
<p> Once a compspec has been found, it is used to generate the list of matching words. If a compspec is not found, the default <code>bash</code> completion as described above under <code>Completing</code> is performed. </p>
<p> First, the actions specified by the compspec are used. Only matches which are prefixed by the word being completed are returned. When the <code>-f</code> or <code>-d</code> option is used for filename or directory name completion, the shell variable <font SIZE="-1"><code>FIGNORE</code> </font> is used to filter the matches. </p>
<p> Any completions specified by a pathname expansion pattern to the <code>-G</code> option are generated next. The words generated by the pattern need not match the word being completed. The <font SIZE="-1"><code>GLOBIGNORE</code> </font> shell variable is not used to filter the matches, but the <font SIZE="-1"><code>FIGNORE</code> </font> variable is used. </p>
<p> Next, the string specified as the argument to the <code>-W</code> option is considered. The string is first split using the characters in the <font SIZE="-1"><code>IFS</code> </font> special variable as delimiters. Shell quoting is honored. Each word is then expanded using brace expansion, tilde expansion, parameter and variable expansion, command substitution, and arithmetic expansion, as described above under <font SIZE="-1"><code>EXPANSION</code>. </font> The results are split using the rules described above under <code>Word Splitting</code>. The results of the expansion are prefix-matched against the word being completed, and the matching words become the possible completions. </p>
<p> After these matches have been generated, any shell function or command specified with the <code>-F</code> and <code>-C</code> options is invoked. When the command or function is invoked, the <font SIZE="-1"><code>COMP_LINE</code>, </font> <font SIZE="-1"><code>COMP_POINT</code>, </font> <font SIZE="-1"><code>COMP_KEY</code>, </font> and <font SIZE="-1"><code>COMP_TYPE</code> </font> variables are assigned values as described above under <code>Shell Variables</code>. If a shell function is being invoked, the <font SIZE="-1"><code>COMP_WORDS</code> </font> and <font SIZE="-1"><code>COMP_CWORD</code> </font> variables are also set. When the function or command is invoked, the first argument (<code>$1</code>) is the name of the command whose arguments are being completed, the second argument (<code>$2</code>) is the word being completed, and the third argument (<code>$3</code>) is the word preceding the word being completed on the current command line. No filtering of the generated completions against the word being completed is performed; the function or command has complete freedom in generating the matches. </p>
<p> Any function specified with <code>-F</code> is invoked first. The function may use any of the shell facilities, including the <code>compgen</code> builtin described below, to generate the matches. It must put the possible completions in the <font SIZE="-1"><code>COMPREPLY</code> </font> array variable, one per array element. </p>
<p> Next, any command specified with the <code>-C</code> option is invoked in an environment equivalent to command substitution. It should print a list of completions, one per line, to the standard output. Backslash may be used to escape a newline, if necessary. </p>
<p> After all of the possible completions are generated, any filter specified with the <code>-X</code> option is applied to the list. The filter is a pattern as used for pathname expansion; a <code>&amp;</code> in the pattern is replaced with the text of the word being completed. A literal <code>&amp;</code> may be escaped with a backslash; the backslash is removed before attempting a match. Any completion that matches the pattern will be removed from the list. A leading <code>!</code> negates the pattern; in this case any completion not matching the pattern will be removed. If the <code>nocasematch</code> shell option is enabled, the match is performed without regard to the case of alphabetic characters. </p>
<p> Finally, any prefix and suffix specified with the <code>-P</code> and <code>-S</code> options are added to each member of the completion list, and the result is returned to the readline completion code as the list of possible completions. </p>
<p> If the previously-applied actions do not generate any matches, and the <code>-o dirnames</code> option was supplied to <code>complete</code> when the compspec was defined, directory name completion is attempted. </p>
<p> If the <code>-o plusdirs</code> option was supplied to <code>complete</code> when the compspec was defined, directory name completion is attempted and any matches are added to the results of the other actions. </p>
<p> By default, if a compspec is found, whatever it generates is returned to the completion code as the full set of possible completions. The default <code>bash</code> completions are not attempted, and the readline default of filename completion is disabled. If the <code>-o bashdefault</code> option was supplied to <code>complete</code> when the compspec was defined, the <code>bash</code> default completions are attempted if the compspec generates no matches. If the <code>-o default</code> option was supplied to <code>complete</code> when the compspec was defined, readline&#8217;s default completion will be performed if the compspec (and, if attempted, the default <code>bash</code> completions) generate no matches. </p>
<p> When a compspec indicates that directory name completion is desired, the programmable completion functions force readline to append a slash to completed names which are symbolic links to directories, subject to the value of the <code>mark-directories</code> readline variable, regardless of the setting of the <code>mark-symlinked-directories</code> readline variable. </p>
<p> There is some support for dynamically modifying completions. This is most useful when used in combination with a default completion specified with <code>complete -D</code>. It&#8217;s possible for shell functions executed as completion handlers to indicate that completion should be retried by returning an exit status of 124. If a shell function returns 124, and changes the compspec associated with the command on which completion is being attempted (supplied as the first argument when the function is executed), programmable completion restarts from the beginning, with an attempt to find a new compspec for that command. This allows a set of completions to be built dynamically as completion is attempted, rather than being loaded all at once. </p>
<p> For instance, assuming that there is a library of compspecs, each kept in a file corresponding to the name of the command, the following default completion function would load completions dynamically: </p>
<p> <code>_completion_loader() <br />
 { <br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>. &quot;/etc/bash_completion.d/$1.sh&quot; &gt;/dev/null 2&gt;&amp;1 &amp;&amp; return 124<br />
 <br />
 } <br />
 complete -D -F _completion_loader -o bashdefault -o default <br />
 </code>  </p>
<h2>HISTORY</h2>
<p> When the <code>-o history</code> option to the <code>set</code> builtin is enabled, the shell provides access to the <i>command history</i>, the list of commands previously typed. The value of the <font SIZE="-1"><code>HISTSIZE</code> </font> variable is used as the number of commands to save in a history list. The text of the last <font SIZE="-1"><code>HISTSIZE</code> </font> commands (default 500) is saved. The shell stores each command in the history list prior to parameter and variable expansion (see <font SIZE="-1"><code>EXPANSION</code> </font> above) but after history expansion is performed, subject to the values of the shell variables <font SIZE="-1"><code>HISTIGNORE</code> </font> and <font SIZE="-1"><code>HISTCONTROL</code>. </font> </p>
<p> On startup, the history is initialized from the file named by the variable <font SIZE="-1"><code>HISTFILE</code> </font> (default <i>~/.bash_history</i>). The file named by the value of <font SIZE="-1"><code>HISTFILE</code> </font> is truncated, if necessary, to contain no more than the number of lines specified by the value of <font SIZE="-1"><code>HISTFILESIZE</code>. </font> If <code>HISTFILESIZE</code> is unset, or set to null, a non-numeric value, or a numeric value less than zero, the history file is not truncated. When the history file is read, lines beginning with the history comment character followed immediately by a digit are interpreted as timestamps for the following history line. These timestamps are optionally displayed depending on the value of the <font SIZE="-1"><code>HISTTIMEFORMAT</code> </font> variable. When a shell with history enabled exits, the last <font SIZE="-1"><code>$HISTSIZE</code> </font> lines are copied from the history list to <font SIZE="-1"><code>$HISTFILE</code>. </font> If the <code>histappend</code> shell option is enabled (see the description of <code>shopt</code> under <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below), the lines are appended to the history file, otherwise the history file is overwritten. If <font SIZE="-1"><code>HISTFILE</code> </font> is unset, or if the history file is unwritable, the history is not saved. If the <font SIZE="-1"><code>HISTTIMEFORMAT</code> </font> variable is set, time stamps are written to the history file, marked with the history comment character, so they may be preserved across shell sessions. This uses the history comment character to distinguish timestamps from other history lines. After saving the history, the history file is truncated to contain no more than <font SIZE="-1"><code>HISTFILESIZE</code> </font> lines. If <font SIZE="-1"><code>HISTFILESIZE</code> </font> is unset, or set to null, a non-numeric value, or a numeric value less than zero, the history file is not truncated. </p>
<p> The builtin command <code>fc</code> (see <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below) may be used to list or edit and re-execute a portion of the history list. The <code>history</code> builtin may be used to display or modify the history list and manipulate the history file. When using command-line editing, search commands are available in each editing mode that provide access to the history list. </p>
<p> The shell allows control over which commands are saved on the history list. The <font SIZE="-1"><code>HISTCONTROL</code> </font> and <font SIZE="-1"><code>HISTIGNORE</code> </font> variables may be set to cause the shell to save only a subset of the commands entered. The <code>cmdhist</code> shell option, if enabled, causes the shell to attempt to save each line of a multi-line command in the same history entry, adding semicolons where necessary to preserve syntactic correctness. The <code>lithist</code> shell option causes the shell to save the command with embedded newlines instead of semicolons. See the description of the <code>shopt</code> builtin below under <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> for information on setting and unsetting shell options.  </p>
<h2>HISTORY EXPANSION</h2>
<p> The shell supports a history expansion feature that is similar to the history expansion in <code>csh</code>. This section describes what syntax features are available. This feature is enabled by default for interactive shells, and can be disabled using the <code>+H</code> option to the <code>set</code> builtin command (see <font SIZE="-1"><code>SHELL BUILTIN COMMANDS</code> </font> below). Non-interactive shells do not perform history expansion by default. </p>
<p> History expansions introduce words from the history list into the input stream, making it easy to repeat commands, insert the arguments to a previous command into the current input line, or fix errors in previous commands quickly. </p>
<p> History expansion is performed immediately after a complete line is read, before the shell breaks it into words, and is performed on each line individually without taking quoting on previous lines into account. It takes place in two parts. The first is to determine which line from the history list to use during substitution. The second is to select portions of that line for inclusion into the current one. The line selected from the history is the <i>event</i>, and the portions of that line that are acted upon are <i>words</i>. Various <i>modifiers</i> are available to manipulate the selected words. The line is broken into words in the same fashion as when reading input, so that several <i>metacharacter</i>-separated words surrounded by quotes are considered one word. History expansions are introduced by the appearance of the history expansion character, which is <code>!</code> by default. Only backslash (<code>\</code>) and single quotes can quote the history expansion character, but the history expansion character is also treated as quoted if it immediately precedes the closing double quote in a double-quoted string. </p>
<p> Several characters inhibit history expansion if found immediately following the history expansion character, even if it is unquoted: space, tab, newline, carriage return, and <code>=</code>. If the <code>extglob</code> shell option is enabled, <code>(</code> will also inhibit expansion. </p>
<p> Several shell options settable with the <code>shopt</code> builtin may be used to tailor the behavior of history expansion. If the <code>histverify</code> shell option is enabled (see the description of the <code>shopt</code> builtin below), and <code>readline</code> is being used, history substitutions are not immediately passed to the shell parser. Instead, the expanded line is reloaded into the <code>readline</code> editing buffer for further modification. If <code>readline</code> is being used, and the <code>histreedit</code> shell option is enabled, a failed history substitution will be reloaded into the <code>readline</code> editing buffer for correction. The <code>-p</code> option to the <code>history</code> builtin command may be used to see what a history expansion will do before using it. The <code>-s</code> option to the <code>history</code> builtin may be used to add commands to the end of the history list without actually executing them, so that they are available for subsequent recall. </p>
<p> The shell allows control of the various characters used by the history expansion mechanism (see the description of <code>histchars</code> above under <code>Shell Variables</code>). The shell uses the history comment character to mark history timestamps when writing the history file.  </p>
<h3>Event Designators</h3>
<p> An event designator is a reference to a command line entry in the history list. Unless the reference is absolute, events are relative to the current position in the history list. </p>
<dl>
<dt><code>!</code></dt>
<dd> <p> Start a history substitution, except when followed by a <code>blank</code>, newline, carriage return, = or ( (when the <code>extglob</code> shell option is enabled using the <code>shopt</code> builtin). </p>
 </dd>
<dt><code>!</code><i>n</i></dt>
<dd> <p> Refer to command line <i>n</i>. </p>
 </dd>
<dt><code>!-</code><i>n</i></dt>
<dd> <p> Refer to the current command minus <i>n</i>. </p>
 </dd>
<dt><code>!!</code></dt>
<dd> <p> Refer to the previous command. This is a synonym for `!-1&#8217;. </p>
 </dd>
<dt><code>!</code><i>string</i></dt>
<dd> <p> Refer to the most recent command preceding the current position in the history list starting with <i>string</i>. </p>
 </dd>
<dt><code>!?</code><i>string</i><code>[?]</code></dt>
<dd> <p> Refer to the most recent command preceding the current position in the history list containing <i>string</i>. The trailing <code>?</code> may be omitted if <i>string</i> is followed immediately by a newline. If <i>string</i> is missing, the string from the most recent search is used; it is an error if there is no previous search string. </p>
 </dd>
<dt><font SIZE="+2"><code>^</code></font><i>string1</i><font SIZE="+2">^</font><i>string2</i><font SIZE="+2">^</font></dt>
<dd> <p> Quick substitution. Repeat the previous command, replacing <i>string1</i> with <i>string2</i>. Equivalent to ``!!:s<font SIZE="+2">^</font><i>string1</i><font SIZE="+2">^</font><i>string2</i><font SIZE="+2">^</font>&#8216;&#8216; (see <code>Modifiers</code> below). </p>
 </dd>
<dt><code>!#</code></dt>
<dd> <p> The entire command line typed so far. </p>
 </dd></dl>
<h3>Word Designators</h3>
<p> Word designators are used to select desired words from the event. A <code>:</code> separates the event specification from the word designator. It may be omitted if the word designator begins with a <code>^</code>, <code>$</code>, <code>*</code>, <code>-</code>, or <code>%</code>. Words are numbered from the beginning of the line, with the first word being denoted by 0 (zero). Words are inserted into the current line separated by single spaces. </p>
<dl>
<dt><code>0 (zero)</code></dt>
<dd> <p> The zeroth word. For the shell, this is the command word. </p>
 </dd>
<dt><i>n</i></dt>
<dd> <p> The <i>n</i>th word. </p>
 </dd>
<dt><code>^</code></dt>
<dd> <p> The first argument. That is, word 1. </p>
 </dd>
<dt><code>$</code></dt>
<dd> <p> The last word. This is usually the last argument, but will expand to the zeroth word if there is only one word in the line. </p>
 </dd>
<dt><code>%</code></dt>
<dd> <p> The first word matched by the most recent `?<i>string</i>?&#8216; search, if the search string begins with a character that is part of a word. </p>
 </dd>
<dt><i>x</i><code>-</code>y </dt>
<dd> <p> A range of words; `-<i>y</i>&#8216; abbreviates `0-<i>y</i>&#8216;. </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> All of the words but the zeroth. This is a synonym for `<i>1-$</i>&#8216;. It is not an error to use <code>*</code> if there is just one word in the event; the empty string is returned in that case. </p>
 </dd>
<dt><code>x*</code></dt>
<dd> <p> Abbreviates <i>x-$</i>. </p>
 </dd>
<dt><code>x-</code></dt>
<dd> <p> Abbreviates <i>x-$</i> like <code>x*</code>, but omits the last word. If <code>x</code> is missing, it defaults to 0. </p>
 </dd></dl>
<p> If a word designator is supplied without an event specification, the previous command is used as the event.  </p>
<h3>Modifiers</h3>
<p> After the optional word designator, there may appear a sequence of one or more of the following modifiers, each preceded by a `:&#8216;. These modify, or edit, the word or words selected from the history event. </p>
<dl>
<dt><code>h</code></dt>
<dd> <p> Remove a trailing filename component, leaving only the head. </p>
 </dd>
<dt><code>t</code></dt>
<dd> <p> Remove all leading filename components, leaving the tail. </p>
 </dd>
<dt><code>r</code></dt>
<dd> <p> Remove a trailing suffix of the form <i>.xxx</i>, leaving the basename. </p>
 </dd>
<dt><code>e</code></dt>
<dd> <p> Remove all but the trailing suffix. </p>
 </dd>
<dt><code>p</code></dt>
<dd> <p> Print the new command but do not execute it. </p>
 </dd>
<dt><code>q</code></dt>
<dd> <p> Quote the substituted words, escaping further substitutions. </p>
 </dd>
<dt><code>x</code></dt>
<dd> <p> Quote the substituted words as with <code>q</code>, but break into words at <code>blanks</code> and newlines. The <code>q</code> and <code>x</code> modifiers are mutually exclusive; the last one supplied is used. </p>
 </dd>
<dt><code>s/</code><i>old</i>/<i>new</i>/ </dt>
<dd> <p> Substitute <i>new</i> for the first occurrence of <i>old</i> in the event line. Any character may be used as the delimiter in place of /. The final delimiter is optional if it is the last character of the event line. The delimiter may be quoted in <i>old</i> and <i>new</i> with a single backslash. If &amp; appears in <i>new</i>, it is replaced by <i>old</i>. A single backslash will quote the &amp;. If <i>old</i> is null, it is set to the last <i>old</i> substituted, or, if no previous history substitutions took place, the last <i>string</i> in a <code>!?</code><i>string</i><code>[?]</code> search. If <i>new</i> is null, each matching <i>old</i> is deleted. </p>
 </dd>
<dt><code>&amp;</code></dt>
<dd> <p> Repeat the previous substitution. </p>
 </dd>
<dt><code>g</code></dt>
<dd> <p> Cause changes to be applied over the entire event line. This is used in conjunction with `<code>:s</code>&#8216; (e.g., `<code>:gs/</code><i>old</i>/<i>new</i>/&#8216;) or `<code>:&amp;</code>&#8216;. If used with `<code>:s</code>&#8216;, any delimiter can be used in place of /, and the final delimiter is optional if it is the last character of the event line. An <code>a</code> may be used as a synonym for <code>g</code>. </p>
 </dd>
<dt><code>G</code></dt>
<dd> <p> Apply the following `<code>s</code>&#8216; or `<code>&amp;</code>&#8216; modifier once to each word in the event line. </p>
 </dd></dl>
<h2>SHELL BUILTIN COMMANDS</h2>
<p> Unless otherwise noted, each builtin command documented in this section as accepting options preceded by <code>-</code> accepts <code>--</code> to signify the end of the options. The <code>:</code>, <code>true</code>, <code>false</code>, and <code>test</code>/<code>[</code> builtins do not accept options and do not treat <code>--</code> specially. The <code>exit</code>, <code>logout</code>, <code>return</code>, <code>break</code>, <code>continue</code>, <code>let</code>, and <code>shift</code> builtins accept and process arguments beginning with <code>-</code> without requiring <code>--</code>. Other builtins that accept arguments but are not specified as accepting options interpret arguments beginning with <code>-</code> as invalid options and require <code>--</code> to prevent this interpretation. </p>
<dl>
<dt><code>:</code> [<i>arguments</i>]</dt>
<dd> <p> No effect; the command does nothing beyond expanding <i>arguments</i> and performing any specified redirections. The return status is zero. </p>
 </dd>
<dt><code> . </code><i>filename</i> [<i>arguments</i>]</dt>
<dd>  </dd>
<dt><code>source</code><i>filename</i> [<i>arguments</i>]</dt>
<dd> <p> Read and execute commands from <i>filename</i> in the current shell environment and return the exit status of the last command executed from <i>filename</i>. If <i>filename</i> does not contain a slash, filenames in <font SIZE="-1"><code>PATH</code> </font> are used to find the directory containing <i>filename</i>. The file searched for in <font SIZE="-1"><code>PATH</code> </font> need not be executable. When <code>bash</code> is not in <i>posix mode</i>, the current directory is searched if no file is found in <font SIZE="-1"><code>PATH</code>. </font> If the <code>sourcepath</code> option to the <code>shopt</code> builtin command is turned off, the <font SIZE="-1"><code>PATH</code> </font> is not searched. If any <i>arguments</i> are supplied, they become the positional parameters when <i>filename</i> is executed. Otherwise the positional parameters are unchanged. If the <code>-T</code> option is enabled, <code>source</code> inherits any trap on <code>DEBUG</code>; if it is not, any <code>DEBUG</code> trap string is saved and restored around the call to <code>source</code>, and <code>source</code> unsets the <code>DEBUG</code> trap while it executes. If <code>-T</code> is not set, and the sourced file changes the <code>DEBUG</code> trap, the new value is retained when <code>source</code> completes. The return status is the status of the last command exited within the script (0 if no commands are executed), and false if <i>filename</i> is not found or cannot be read. </p>
 </dd>
<dt><code>alias</code> [<code>-p</code>] [<i>name</i>[=<i>value</i>] ...]</dt>
<dd> <p> <code>Alias</code> with no arguments or with the <code>-p</code> option prints the list of aliases in the form <code>alias</code> <i>name</i>=<i>value</i> on standard output. When arguments are supplied, an alias is defined for each <i>name</i> whose <i>value</i> is given. A trailing space in <i>value</i> causes the next word to be checked for alias substitution when the alias is expanded. For each <i>name</i> in the argument list for which no <i>value</i> is supplied, the name and value of the alias is printed. <code>Alias</code> returns true unless a <i>name</i> is given for which no alias has been defined. </p>
 </dd>
<dt><code>bg</code> [<i>jobspec</i> ...]</dt>
<dd> <p> Resume each suspended job <i>jobspec</i> in the background, as if it had been started with <code>&amp;</code>. If <i>jobspec</i> is not present, the shell&#8217;s notion of the <i>current job</i> is used. <code>bg</code> <i>jobspec</i> returns 0 unless run when job control is disabled or, when run with job control enabled, any specified <i>jobspec</i> was not found or was started without job control. </p>
 </dd>
<dt><code>bind</code> [<code>-m</code><i>keymap</i>] [<code>-lpsvPSVX</code>]</dt>
<dd>  </dd>
<dt><code>bind</code> [<code>-m</code><i>keymap</i>] [<code>-q</code><i>function</i>] [<code>-u</code><i>function</i>] [<code>-r</code><i>keyseq</i>]</dt>
<dd>  </dd>
<dt><code>bind</code> [<code>-m</code><i>keymap</i>] <code>-f</code><i>filename</i></dt>
<dd>  </dd>
<dt><code>bind</code> [<code>-m</code><i>keymap</i>] <code>-x</code><i>keyseq</i>:<i>shell-command</i></dt>
<dd>  </dd>
<dt><code>bind</code> [<code>-m</code><i>keymap</i>] <i>keyseq</i>:<i>function-name</i></dt>
<dd>  </dd>
<dt><code>bind</code> [<code>-m</code><i>keymap</i>] <i>keyseq</i>:<i>readline-command</i></dt>
<dd> <p> Display current <code>readline</code> key and function bindings, bind a key sequence to a <code>readline</code> function or macro, or set a <code>readline</code> variable. Each non-option argument is a command as it would appear in <i>.inputrc</i>, but each binding or command must be passed as a separate argument; e.g., &#8216;&quot;\C-x\C-r&quot;: re-read-init-file&#8217;. Options, if supplied, have the following meanings: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>-m </code><i>keymap</i></dt>
<dd> <p> Use <i>keymap</i> as the keymap to be affected by the subsequent bindings. Acceptable <i>keymap</i> names are <i>emacs, emacs-standard, emacs-meta, emacs-ctlx, vi, vi-move, vi-command</i>, and <i>vi-insert</i>. <i>vi</i> is equivalent to <i>vi-command</i> (<i>vi-move</i> is also a synonym); <i>emacs</i> is equivalent to <i>emacs-standard</i>. </p>
 </dd>
<dt><code>-l</code></dt>
<dd> <p> List the names of all <code>readline</code> functions. </p>
 </dd>
<dt><code>-p</code></dt>
<dd> <p> Display <code>readline</code> function names and bindings in such a way that they can be re-read. </p>
 </dd>
<dt><code>-P</code></dt>
<dd> <p> List current <code>readline</code> function names and bindings. </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> Display <code>readline</code> key sequences bound to macros and the strings they output in such a way that they can be re-read. </p>
 </dd>
<dt><code>-S</code></dt>
<dd> <p> Display <code>readline</code> key sequences bound to macros and the strings they output. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Display <code>readline</code> variable names and values in such a way that they can be re-read. </p>
 </dd>
<dt><code>-V</code></dt>
<dd> <p> List current <code>readline</code> variable names and values. </p>
 </dd>
<dt><code>-f </code><i>filename</i></dt>
<dd> <p> Read key bindings from <i>filename</i>. </p>
 </dd>
<dt><code>-q </code><i>function</i></dt>
<dd> <p> Query about which keys invoke the named <i>function</i>. </p>
 </dd>
<dt><code>-u </code><i>function</i></dt>
<dd> <p> Unbind all keys bound to the named <i>function</i>. </p>
 </dd>
<dt><code>-r </code><i>keyseq</i></dt>
<dd> <p> Remove any current binding for <i>keyseq</i>. </p>
 </dd>
<dt><code>-x </code><i>keyseq</i>:<i>shell-command</i></dt>
<dd> <p> Cause <i>shell-command</i> to be executed whenever <i>keyseq</i> is entered. When <i>shell-command</i> is executed, the shell sets the <font SIZE="-1"><code>READLINE_LINE</code> </font> variable to the contents of the <code>readline</code> line buffer and the <font SIZE="-1"><code>READLINE_POINT</code> </font> and <font SIZE="-1"><code>READLINE_MARK</code> </font> variables to the current location of the insertion point and the saved insertion point (the mark), respectively. If the executed command changes the value of any of <font SIZE="-1"><code>READLINE_LINE</code>, </font> <font SIZE="-1"><code>READLINE_POINT</code>, </font> or <font SIZE="-1"><code>READLINE_MARK</code>, </font> those new values will be reflected in the editing state. </p>
 </dd>
<dt><code>-X</code></dt>
<dd> <p> List all key sequences bound to shell commands and the associated commands in a format that can be reused as input. </p>
 </dd></dl>
<p> The return value is 0 unless an unrecognized option is given or an error occurred. </dl>
 </p>
<dt><code>break</code> [<i>n</i>]</dt>
<dd> <p> Exit from within a <code>for</code>, <code>while</code>, <code>until</code>, or <code>select</code> loop. If <i>n</i> is specified, break <i>n</i> levels. <i>n</i> must be &ge; 1. If <i>n</i> is greater than the number of enclosing loops, all enclosing loops are exited. The return value is 0 unless <i>n</i> is not greater than or equal to 1. </p>
 </dd>
<dt><code>builtin</code><i>shell-builtin</i> [<i>arguments</i>]</dt>
<dd> <p> Execute the specified shell builtin, passing it <i>arguments</i>, and return its exit status. This is useful when defining a function whose name is the same as a shell builtin, retaining the functionality of the builtin within the function. The <code>cd</code> builtin is commonly redefined this way. The return status is false if <i>shell-builtin</i> is not a shell builtin command. </p>
 </dd>
<dt><code>caller</code> [<i>expr</i>]</dt>
<dd> <p> Returns the context of any active subroutine call (a shell function or a script executed with the <code>.</code> or <code>source</code> builtins). Without <i>expr</i>, <code>caller</code> displays the line number and source filename of the current subroutine call. If a non-negative integer is supplied as <i>expr</i>, <code>caller</code> displays the line number, subroutine name, and source file corresponding to that position in the current execution call stack. This extra information may be used, for example, to print a stack trace. The current frame is frame 0. The return value is 0 unless the shell is not executing a subroutine call or <i>expr</i> does not correspond to a valid position in the call stack. </p>
 </dd>
<dt><code>cd</code> [<code>-L</code>|[<code>-P</code> [<code>-e</code>]] [-@]] [<i>dir</i>]</dt>
<dd> <p> Change the current directory to <i>dir</i>. if <i>dir</i> is not supplied, the value of the <font SIZE="-1"><code>HOME</code> </font> shell variable is the default. Any additional arguments following <i>dir</i> are ignored. The variable <font SIZE="-1"><code>CDPATH</code> </font> defines the search path for the directory containing <i>dir</i>: each directory name in <font SIZE="-1"><code>CDPATH</code> </font> is searched for <i>dir</i>. Alternative directory names in <font SIZE="-1"><code>CDPATH</code> </font> are separated by a colon (:). A null directory name in <font SIZE="-1"><code>CDPATH</code> </font> is the same as the current directory, i.e., ``<code>.</code>&#8216;&#8216;. If <i>dir</i> begins with a slash (/), then <font SIZE="-1"><code>CDPATH</code> </font> is not used. The <code>-P</code> option causes <code>cd</code> to use the physical directory structure by resolving symbolic links while traversing <i>dir</i> and before processing instances of <i>..</i> in <i>dir</i> (see also the <code>-P</code> option to the <code>set</code> builtin command); the <code>-L</code> option forces symbolic links to be followed by resolving the link after processing instances of <i>..</i> in <i>dir</i>. If <i>..</i> appears in <i>dir</i>, it is processed by removing the immediately previous pathname component from <i>dir</i>, back to a slash or the beginning of <i>dir</i>. If the <code>-e</code> option is supplied with <code>-P</code>, and the current working directory cannot be successfully determined after a successful directory change, <code>cd</code> will return an unsuccessful status. On systems that support it, the <code>-@</code> option presents the extended attributes associated with a file as a directory. An argument of <code>-</code> is converted to <font SIZE="-1"><code>$OLDPWD</code> </font> before the directory change is attempted. If a non-empty directory name from <font SIZE="-1"><code>CDPATH</code> </font> is used, or if <code>-</code> is the first argument, and the directory change is successful, the absolute pathname of the new working directory is written to the standard output. The return value is true if the directory was successfully changed; false otherwise. </p>
 </dd>
<dt><code>command</code> [<code>-pVv</code>] <i>command</i> [<i>arg</i> ...]</dt>
<dd> <p> Run <i>command</i> with <i>args</i> suppressing the normal shell function lookup. Only builtin commands or commands found in the <font SIZE="-1"><code>PATH</code> </font> are executed. If the <code>-p</code> option is given, the search for <i>command</i> is performed using a default value for <font SIZE="-1"><code>PATH</code> </font> that is guaranteed to find all of the standard utilities. If either the <code>-V</code> or <code>-v</code> option is supplied, a description of <i>command</i> is printed. The <code>-v</code> option causes a single word indicating the command or filename used to invoke <i>command</i> to be displayed; the <code>-V</code> option produces a more verbose description. If the <code>-V</code> or <code>-v</code> option is supplied, the exit status is 0 if <i>command</i> was found, and 1 if not. If neither option is supplied and an error occurred or <i>command</i> cannot be found, the exit status is 127. Otherwise, the exit status of the <code>command</code> builtin is the exit status of <i>command</i>. </p>
 </dd>
<dt><code>compgen</code> [<i>option</i>] [<i>word</i>]</dt>
<dd> <p> Generate possible completion matches for <i>word</i> according to the <i>option</i>s, which may be any option accepted by the <code>complete</code> builtin with the exception of <code>-p</code> and <code>-r</code>, and write the matches to the standard output. When using the <code>-F</code> or <code>-C</code> options, the various shell variables set by the programmable completion facilities, while available, will not have useful values. </p>
<p> The matches will be generated in the same way as if the programmable completion code had generated them directly from a completion specification with the same flags. If <i>word</i> is specified, only those completions matching <i>word</i> will be displayed. </p>
<p> The return value is true unless an invalid option is supplied, or no matches were generated. </p>
 </dd>
<dt><code>complete</code> [<code>-abcdefgjksuv</code>] [<code>-o</code><i>comp-option</i>] [<code>-DEI</code>] [<code>-A</code><i>action</i>] [<code>-G</code><i>globpat</i>] [<code>-W</code><i>wordlist</i>]</dt>
<dd> <p> <br />
 [<code>-F</code> <i>function</i>] [<code>-C</code> <i>command</i>] [<code>-X</code> <i>filterpat</i>] [<code>-P</code> <i>prefix</i>] [<code>-S</code> <i>suffix</i>] <i>name</i> [<i>name ...</i>] </p>
 </dd>
<dt><code>complete</code><code>-pr</code> [<code>-DEI</code>] [<i>name</i> ...]</dt>
<dd> <p> Specify how arguments to each <i>name</i> should be completed. If the <code>-p</code> option is supplied, or if no options are supplied, existing completion specifications are printed in a way that allows them to be reused as input. The <code>-r</code> option removes a completion specification for each <i>name</i>, or, if no <i>name</i>s are supplied, all completion specifications. The <code>-D</code> option indicates that other supplied options and actions should apply to the ``default&#8217;&#8216; command completion; that is, completion attempted on a command for which no completion has previously been defined. The <code>-E</code> option indicates that other supplied options and actions should apply to ``empty&#8217;&#8216; command completion; that is, completion attempted on a blank line. The <code>-I</code> option indicates that other supplied options and actions should apply to completion on the initial non-assignment word on the line, or after a command delimiter such as <code>;</code> or <code>|</code>, which is usually command name completion. If multiple options are supplied, the <code>-D</code> option takes precedence over <code>-E</code>, and both take precedence over <code>-I</code>. If any of <code>-D</code>, <code>-E</code>, or <code>-I</code> are supplied, any other <i>name</i> arguments are ignored; these completions only apply to the case specified by the option. </p>
<p> The process of applying these completion specifications when word completion is attempted is described above under <code>Programmable Completion</code>. </p>
<p> Other options, if specified, have the following meanings. The arguments to the <code>-G</code>, <code>-W</code>, and <code>-X</code> options (and, if necessary, the <code>-P</code> and <code>-S</code> options) should be quoted to protect them from expansion before the <code>complete</code> builtin is invoked. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>-o</code><i>comp-option</i></dt>
<dd> <p> The <i>comp-option</i> controls several aspects of the compspec&#8217;s behavior beyond the simple generation of completions. <i>comp-option</i> may be one of: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>bashdefault</code></dt>
<dd> <p> Perform the rest of the default <code>bash</code> completions if the compspec generates no matches. </p>
 </dd>
<dt><code>default</code></dt>
<dd> <p> Use readline&#8217;s default filename completion if the compspec generates no matches. </p>
 </dd>
<dt><code>dirnames</code></dt>
<dd> <p> Perform directory name completion if the compspec generates no matches. </p>
 </dd>
<dt><code>filenames</code></dt>
<dd> <p> Tell readline that the compspec generates filenames, so it can perform any filename-specific processing (like adding a slash to directory names, quoting special characters, or suppressing trailing spaces). Intended to be used with shell functions. </p>
 </dd>
<dt><code>noquote</code></dt>
<dd> <p> Tell readline not to quote the completed words if they are filenames (quoting filenames is the default). </p>
 </dd>
<dt><code>nosort</code></dt>
<dd> <p> Tell readline not to sort the list of possible completions alphabetically. </p>
 </dd>
<dt><code>nospace</code></dt>
<dd> <p> Tell readline not to append a space (the default) to words completed at the end of the line. </p>
 </dd>
<dt><code>plusdirs</code></dt>
<dd> <p> After any matches defined by the compspec are generated, directory name completion is attempted and any matches are added to the results of the other actions. </p>
 </dd></dl>
</dl>
<dt><code>-A</code><i>action</i></dt>
<dd> <p> The <i>action</i> may be one of the following to generate a list of possible completions: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>alias</code></dt>
<dd> <p> Alias names. May also be specified as <code>-a</code>. </p>
 </dd>
<dt><code>arrayvar</code></dt>
<dd> <p> Array variable names. </p>
 </dd>
<dt><code>binding</code></dt>
<dd> <p> <code>Readline</code> key binding names. </p>
 </dd>
<dt><code>builtin</code></dt>
<dd> <p> Names of shell builtin commands. May also be specified as <code>-b</code>. </p>
 </dd>
<dt><code>command</code></dt>
<dd> <p> Command names. May also be specified as <code>-c</code>. </p>
 </dd>
<dt><code>directory</code></dt>
<dd> <p> Directory names. May also be specified as <code>-d</code>. </p>
 </dd>
<dt><code>disabled</code></dt>
<dd> <p> Names of disabled shell builtins. </p>
 </dd>
<dt><code>enabled</code></dt>
<dd> <p> Names of enabled shell builtins. </p>
 </dd>
<dt><code>export</code></dt>
<dd> <p> Names of exported shell variables. May also be specified as <code>-e</code>. </p>
 </dd>
<dt><code>file</code></dt>
<dd> <p> File names. May also be specified as <code>-f</code>. </p>
 </dd>
<dt><code>function</code></dt>
<dd> <p> Names of shell functions. </p>
 </dd>
<dt><code>group</code></dt>
<dd> <p> Group names. May also be specified as <code>-g</code>. </p>
 </dd>
<dt><code>helptopic</code></dt>
<dd> <p> Help topics as accepted by the <code>help</code> builtin. </p>
 </dd>
<dt><code>hostname</code></dt>
<dd> <p> Hostnames, as taken from the file specified by the <font SIZE="-1"><code>HOSTFILE</code> </font> shell variable. </p>
 </dd>
<dt><code>job</code></dt>
<dd> <p> Job names, if job control is active. May also be specified as <code>-j</code>. </p>
 </dd>
<dt><code>keyword</code></dt>
<dd> <p> Shell reserved words. May also be specified as <code>-k</code>. </p>
 </dd>
<dt><code>running</code></dt>
<dd> <p> Names of running jobs, if job control is active. </p>
 </dd>
<dt><code>service</code></dt>
<dd> <p> Service names. May also be specified as <code>-s</code>. </p>
 </dd>
<dt><code>setopt</code></dt>
<dd> <p> Valid arguments for the <code>-o</code> option to the <code>set</code> builtin. </p>
 </dd>
<dt><code>shopt</code></dt>
<dd> <p> Shell option names as accepted by the <code>shopt</code> builtin. </p>
 </dd>
<dt><code>signal</code></dt>
<dd> <p> Signal names. </p>
 </dd>
<dt><code>stopped</code></dt>
<dd> <p> Names of stopped jobs, if job control is active. </p>
 </dd>
<dt><code>user</code></dt>
<dd> <p> User names. May also be specified as <code>-u</code>. </p>
 </dd>
<dt><code>variable</code></dt>
<dd> <p> Names of all shell variables. May also be specified as <code>-v</code>. </p>
 </dd></dl>
</dl>
<dt><code>-C</code><i>command</i></dt>
<dd> <p> <i>command</i> is executed in a subshell environment, and its output is used as the possible completions. </p>
 </dd>
<dt><code>-F</code><i>function</i></dt>
<dd> <p> The shell function <i>function</i> is executed in the current shell environment. When the function is executed, the first argument (<code>$1</code>) is the name of the command whose arguments are being completed, the second argument (<code>$2</code>) is the word being completed, and the third argument (<code>$3</code>) is the word preceding the word being completed on the current command line. When it finishes, the possible completions are retrieved from the value of the <font SIZE="-1"><code>COMPREPLY</code> </font> array variable. </p>
 </dd>
<dt><code>-G</code><i>globpat</i></dt>
<dd> <p> The pathname expansion pattern <i>globpat</i> is expanded to generate the possible completions. </p>
 </dd>
<dt><code>-P</code><i>prefix</i></dt>
<dd> <p> <i>prefix</i> is added at the beginning of each possible completion after all other options have been applied. </p>
 </dd>
<dt><code>-S</code><i>suffix</i></dt>
<dd> <p> <i>suffix</i> is appended to each possible completion after all other options have been applied. </p>
 </dd>
<dt><code>-W</code><i>wordlist</i></dt>
<dd> <p> The <i>wordlist</i> is split using the characters in the <font SIZE="-1"><code>IFS</code> </font> special variable as delimiters, and each resultant word is expanded. Shell quoting is honored within <i>wordlist</i>, in order to provide a mechanism for the words to contain shell metacharacters or characters in the value of <font SIZE="-1"><code>IFS</code>. </font> The possible completions are the members of the resultant list which match the word being completed. </p>
 </dd>
<dt><code>-X</code><i>filterpat</i></dt>
<dd> <p> <i>filterpat</i> is a pattern as used for pathname expansion. It is applied to the list of possible completions generated by the preceding options and arguments, and each completion matching <i>filterpat</i> is removed from the list. A leading <code>!</code> in <i>filterpat</i> negates the pattern; in this case, any completion not matching <i>filterpat</i> is removed. </p>
 </dd></dl>
<p> The return value is true unless an invalid option is supplied, an option other than <code>-p</code> or <code>-r</code> is supplied without a <i>name</i> argument, an attempt is made to remove a completion specification for a <i>name</i> for which no specification exists, or an error occurs adding a completion specification. </dl>
 </p>
<dt><code>compopt</code> [<code>-o</code><i>option</i>] [<code>-DEI</code>] [<code>+o</code><i>option</i>] [<i>name</i>]</dt>
<dd> <p> Modify completion options for each <i>name</i> according to the <i>option</i>s, or for the currently-executing completion if no <i>name</i>s are supplied. If no <i>option</i>s are given, display the completion options for each <i>name</i> or the current completion. The possible values of <i>option</i> are those valid for the <code>complete</code> builtin described above. The <code>-D</code> option indicates that other supplied options should apply to the ``default&#8217;&#8216; command completion; that is, completion attempted on a command for which no completion has previously been defined. The <code>-E</code> option indicates that other supplied options should apply to ``empty&#8217;&#8216; command completion; that is, completion attempted on a blank line. The <code>-I</code> option indicates that other supplied options should apply to completion on the initial non-assignment word on the line, or after a command delimiter such as <code>;</code> or <code>|</code>, which is usually command name completion. </p>
<p> The return value is true unless an invalid option is supplied, an attempt is made to modify the options for a <i>name</i> for which no completion specification exists, or an output error occurs. </p>
 </dd>
<dt><code>continue</code> [<i>n</i>]</dt>
<dd> <p> Resume the next iteration of the enclosing <code>for</code>, <code>while</code>, <code>until</code>, or <code>select</code> loop. If <i>n</i> is specified, resume at the <i>n</i>th enclosing loop. <i>n</i> must be &ge; 1. If <i>n</i> is greater than the number of enclosing loops, the last enclosing loop (the ``top-level&#8217;&#8216; loop) is resumed. The return value is 0 unless <i>n</i> is not greater than or equal to 1. </p>
 </dd>
<dt><code>declare</code> [<code>-aAfFgiIlnrtux</code>] [<code>-p</code>] [<i>name</i>[=<i>value</i>] ...]</dt>
<dd>  </dd>
<dt><code>typeset</code> [<code>-aAfFgiIlnrtux</code>] [<code>-p</code>] [<i>name</i>[=<i>value</i>] ...]</dt>
<dd> <p> Declare variables and/or give them attributes. If no <i>name</i>s are given then display the values of variables. The <code>-p</code> option will display the attributes and values of each <i>name</i>. When <code>-p</code> is used with <i>name</i> arguments, additional options, other than <code>-f</code> and <code>-F</code>, are ignored. When <code>-p</code> is supplied without <i>name</i> arguments, it will display the attributes and values of all variables having the attributes specified by the additional options. If no other options are supplied with <code>-p</code>, <code>declare</code> will display the attributes and values of all shell variables. The <code>-f</code> option will restrict the display to shell functions. The <code>-F</code> option inhibits the display of function definitions; only the function name and attributes are printed. If the <code>extdebug</code> shell option is enabled using <code>shopt</code>, the source file name and line number where each <i>name</i> is defined are displayed as well. The <code>-F</code> option implies <code>-f</code>. The <code>-g</code> option forces variables to be created or modified at the global scope, even when <code>declare</code> is executed in a shell function. It is ignored in all other cases. The <code>-I</code> option causes local variables to inherit the attributes (except the <i>nameref</i> attribute) and value of any existing variable with the same <i>name</i> at a surrounding scope. If there is no existing variable, the local variable is initially unset. The following options can be used to restrict output to variables with the specified attribute or to give variables attributes: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>-a</code></dt>
<dd> <p> Each <i>name</i> is an indexed array variable (see <code>Arrays</code> above). </p>
 </dd>
<dt><code>-A</code></dt>
<dd> <p> Each <i>name</i> is an associative array variable (see <code>Arrays</code> above). </p>
 </dd>
<dt><code>-f</code></dt>
<dd> <p> Use function names only. </p>
 </dd>
<dt><code>-i</code></dt>
<dd> <p> The variable is treated as an integer; arithmetic evaluation (see <font SIZE="-1"><code>ARITHMETIC EVALUATION</code> </font> above) is performed when the variable is assigned a value. </p>
 </dd>
<dt><code>-l</code></dt>
<dd> <p> When the variable is assigned a value, all upper-case characters are converted to lower-case. The upper-case attribute is disabled. </p>
 </dd>
<dt><code>-n</code></dt>
<dd> <p> Give each <i>name</i> the <i>nameref</i> attribute, making it a name reference to another variable. That other variable is defined by the value of <i>name</i>. All references, assignments, and attribute modifications to <i>name</i>, except those using or changing the <code>-n</code> attribute itself, are performed on the variable referenced by <i>name</i>&#8216;s value. The nameref attribute cannot be applied to array variables. </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> Make <i>name</i>s readonly. These names cannot then be assigned values by subsequent assignment statements or unset. </p>
 </dd>
<dt><code>-t</code></dt>
<dd> <p> Give each <i>name</i> the <i>trace</i> attribute. Traced functions inherit the <code>DEBUG</code> and <code>RETURN</code> traps from the calling shell. The trace attribute has no special meaning for variables. </p>
 </dd>
<dt><code>-u</code></dt>
<dd> <p> When the variable is assigned a value, all lower-case characters are converted to upper-case. The lower-case attribute is disabled. </p>
 </dd>
<dt><code>-x</code></dt>
<dd> <p> Mark <i>name</i>s for export to subsequent commands via the environment. </p>
 </dd></dl>
<p> Using `+&#8216; instead of `-&#8216; turns off the attribute instead, with the exceptions that <code>+a</code> and <code>+A</code> may not be used to destroy array variables and <code>+r</code> will not remove the readonly attribute. When used in a function, <code>declare</code> and <code>typeset</code> make each <i>name</i> local, as with the <code>local</code> command, unless the <code>-g</code> option is supplied. If a variable name is followed by =<i>value</i>, the value of the variable is set to <i>value</i>. When using <code>-a</code> or <code>-A</code> and the compound assignment syntax to create array variables, additional attributes do not take effect until subsequent assignments. The return value is 0 unless an invalid option is encountered, an attempt is made to define a function using ``-f foo=bar&#8217;&#8216;, an attempt is made to assign a value to a readonly variable, an attempt is made to assign a value to an array variable without using the compound assignment syntax (see <code>Arrays</code> above), one of the <i>names</i> is not a valid shell variable name, an attempt is made to turn off readonly status for a readonly variable, an attempt is made to turn off array status for an array variable, or an attempt is made to display a non-existent function with <code>-f</code>. </dl>
 </p>
<dt><code>dirs [-clpv</code>] [+<i>n</i>] [-<i>n</i>] </dt>
<dd> <p> Without options, displays the list of currently remembered directories. The default display is on a single line with directory names separated by spaces. Directories are added to the list with the <code>pushd</code> command; the <code>popd</code> command removes entries from the list. The current directory is always the first directory in the stack. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>-c</code></dt>
<dd> <p> Clears the directory stack by deleting all of the entries. </p>
 </dd>
<dt><code>-l</code></dt>
<dd> <p> Produces a listing using full pathnames; the default listing format uses a tilde to denote the home directory. </p>
 </dd>
<dt><code>-p</code></dt>
<dd> <p> Print the directory stack with one entry per line. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Print the directory stack with one entry per line, prefixing each entry with its index in the stack. </p>
 </dd>
<dt><code>+</code><i>n</i></dt>
<dd> <p> Displays the <i>n</i>th entry counting from the left of the list shown by <code>dirs</code> when invoked without options, starting with zero. </p>
 </dd>
<dt><code>-</code><i>n</i></dt>
<dd> <p> Displays the <i>n</i>th entry counting from the right of the list shown by <code>dirs</code> when invoked without options, starting with zero. </p>
 </dd></dl>
<p> The return value is 0 unless an invalid option is supplied or <i>n</i> indexes beyond the end of the directory stack. </dl>
 </p>
<dt><code>disown</code> [<code>-ar</code>] [<code>-h</code>] [<i>jobspec</i> ... | <i>pid</i> ... ]</dt>
<dd> <p> Without options, remove each <i>jobspec</i> from the table of active jobs. If <i>jobspec</i> is not present, and neither the <code>-a</code> nor the <code>-r</code> option is supplied, the <i>current job</i> is used. If the <code>-h</code> option is given, each <i>jobspec</i> is not removed from the table, but is marked so that <font SIZE="-1"><code>SIGHUP</code> </font> is not sent to the job if the shell receives a <font SIZE="-1"><code>SIGHUP</code>. </font> If no <i>jobspec</i> is supplied, the <code>-a</code> option means to remove or mark all jobs; the <code>-r</code> option without a <i>jobspec</i> argument restricts operation to running jobs. The return value is 0 unless a <i>jobspec</i> does not specify a valid job. </p>
 </dd>
<dt><code>echo</code> [<code>-neE</code>] [<i>arg</i> ...]</dt>
<dd> <p> Output the <i>arg</i>s, separated by spaces, followed by a newline. The return status is 0 unless a write error occurs. If <code>-n</code> is specified, the trailing newline is suppressed. If the <code>-e</code> option is given, interpretation of the following backslash-escaped characters is enabled. The <code>-E</code> option disables the interpretation of these escape characters, even on systems where they are interpreted by default. The <code>xpg_echo</code> shell option may be used to dynamically determine whether or not <code>echo</code> expands these escape characters by default. <code>echo</code> does not interpret <code>--</code> to mean the end of options. <code>echo</code> interprets the following escape sequences: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>\a</code></dt>
<dd> <p> alert (bell) </p>
 </dd>
<dt><code>\b</code></dt>
<dd> <p> backspace </p>
 </dd>
<dt><code>\c</code></dt>
<dd> <p> suppress further output </p>
 </dd>
<dt><code>\e</code></dt>
<dd>  </dd>
<dt><code>\E</code></dt>
<dd> <p> an escape character </p>
 </dd>
<dt><code>\f</code></dt>
<dd> <p> form feed </p>
 </dd>
<dt><code>\n</code></dt>
<dd> <p> new line </p>
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
<dt><code>\0</code><i>nnn</i></dt>
<dd> <p> the eight-bit character whose value is the octal value <i>nnn</i> (zero to three octal digits) </p>
 </dd>
<dt><code>\x</code><i>HH</i></dt>
<dd> <p> the eight-bit character whose value is the hexadecimal value <i>HH</i> (one or two hex digits) </p>
 </dd>
<dt><code>\u</code><i>HHHH</i></dt>
<dd> <p> the Unicode (ISO/IEC 10646) character whose value is the hexadecimal value <i>HHHH</i> (one to four hex digits) </p>
 </dd>
<dt><code>\U</code><i>HHHHHHHH</i></dt>
<dd> <p> the Unicode (ISO/IEC 10646) character whose value is the hexadecimal value <i>HHHHHHHH</i> (one to eight hex digits) </p>
 </dd></dl>
</dl>
<dt><code>enable</code> [<code>-a</code>] [<code>-dnps</code>] [<code>-f</code><i>filename</i>] [<i>name</i> ...]</dt>
<dd> <p> Enable and disable builtin shell commands. Disabling a builtin allows a disk command which has the same name as a shell builtin to be executed without specifying a full pathname, even though the shell normally searches for builtins before disk commands. If <code>-n</code> is used, each <i>name</i> is disabled; otherwise, <i>names</i> are enabled. For example, to use the <code>test</code> binary found via the <font SIZE="-1"><code>PATH</code> </font> instead of the shell builtin version, run ``enable -n test&#8217;&#8216;. The <code>-f</code> option means to load the new builtin command <i>name</i> from shared object <i>filename</i>, on systems that support dynamic loading. The <code>-d</code> option will delete a builtin previously loaded with <code>-f</code>. If no <i>name</i> arguments are given, or if the <code>-p</code> option is supplied, a list of shell builtins is printed. With no other option arguments, the list consists of all enabled shell builtins. If <code>-n</code> is supplied, only disabled builtins are printed. If <code>-a</code> is supplied, the list printed includes all builtins, with an indication of whether or not each is enabled. If <code>-s</code> is supplied, the output is restricted to the POSIX <i>special</i> builtins. The return value is 0 unless a <i>name</i> is not a shell builtin or there is an error loading a new builtin from a shared object. </p>
 </dd>
<dt><code>eval</code> [<i>arg</i> ...]</dt>
<dd> <p> The <i>arg</i>s are read and concatenated together into a single command. This command is then read and executed by the shell, and its exit status is returned as the value of <code>eval</code>. If there are no <i>args</i>, or only null arguments, <code>eval</code> returns 0. </p>
 </dd>
<dt><code>exec</code> [<code>-cl</code>] [<code>-a</code><i>name</i>] [<i>command</i> [<i>arguments</i>]]</dt>
<dd> <p> If <i>command</i> is specified, it replaces the shell. No new process is created. The <i>arguments</i> become the arguments to <i>command</i>. If the <code>-l</code> option is supplied, the shell places a dash at the beginning of the zeroth argument passed to <i>command</i>. This is what <i><a href="/docs/linux/man/1-login/">login</a></i>(1) does. The <code>-c</code> option causes <i>command</i> to be executed with an empty environment. If <code>-a</code> is supplied, the shell passes <i>name</i> as the zeroth argument to the executed command. If <i>command</i> cannot be executed for some reason, a non-interactive shell exits, unless the <code>execfail</code> shell option is enabled. In that case, it returns failure. An interactive shell returns failure if the file cannot be executed. A subshell exits unconditionally if <code>exec</code> fails. If <i>command</i> is not specified, any redirections take effect in the current shell, and the return status is 0. If there is a redirection error, the return status is 1. </p>
 </dd>
<dt><code>exit</code> [<i>n</i>]</dt>
<dd> <p> Cause the shell to exit with a status of <i>n</i>. If <i>n</i> is omitted, the exit status is that of the last command executed. A trap on <font SIZE="-1"><code>EXIT</code> </font> is executed before the shell terminates. </p>
 </dd>
<dt><code>export</code> [<code>-fn</code>] [<i>name</i>[=<i>word</i>]] ...</dt>
<dd>  </dd>
<dt><code>export -p</code></dt>
<dd> <p> The supplied <i>names</i> are marked for automatic export to the environment of subsequently executed commands. If the <code>-f</code> option is given, the <i>names</i> refer to functions. If no <i>names</i> are given, or if the <code>-p</code> option is supplied, a list of names of all exported variables is printed. The <code>-n</code> option causes the export property to be removed from each <i>name</i>. If a variable name is followed by =<i>word</i>, the value of the variable is set to <i>word</i>. <code>export</code> returns an exit status of 0 unless an invalid option is encountered, one of the <i>names</i> is not a valid shell variable name, or <code>-f</code> is supplied with a <i>name</i> that is not a function. </p>
 </dd>
<dt><code>fc</code> [<code>-e</code><i>ename</i>] [<code>-lnr</code>] [<i>first</i>] [<i>last</i>]</dt>
<dd>  </dd>
<dt><code>fc</code><code>-s</code> [<i>pat</i>=<i>rep</i>] [<i>cmd</i>]</dt>
<dd> <p> The first form selects a range of commands from <i>first</i> to <i>last</i> from the history list and displays or edits and re-executes them. <i>First</i> and <i>last</i> may be specified as a string (to locate the last command beginning with that string) or as a number (an index into the history list, where a negative number is used as an offset from the current command number). When listing, a <i>first</i> or <i>last</i> of 0 is equivalent to -1 and -0 is equivalent to the current command (usually the <code>fc</code> command); otherwise 0 is equivalent to -1 and -0 is invalid. If <i>last</i> is not specified, it is set to the current command for listing (so that ``fc -l -10&#8217;&#8216; prints the last 10 commands) and to <i>first</i> otherwise. If <i>first</i> is not specified, it is set to the previous command for editing and -16 for listing. </p>
<p> The <code>-n</code> option suppresses the command numbers when listing. The <code>-r</code> option reverses the order of the commands. If the <code>-l</code> option is given, the commands are listed on standard output. Otherwise, the editor given by <i>ename</i> is invoked on a file containing those commands. If <i>ename</i> is not given, the value of the <font SIZE="-1"><code>FCEDIT</code> </font> variable is used, and the value of <font SIZE="-1"><code>EDITOR</code> </font> if <font SIZE="-1"><code>FCEDIT</code> </font> is not set. If neither variable is set, <i>vi</i> is used. When editing is complete, the edited commands are echoed and executed. </p>
<p> In the second form, <i>command</i> is re-executed after each instance of <i>pat</i> is replaced by <i>rep</i>. <i>Command</i> is interpreted the same as <i>first</i> above. A useful alias to use with this is ``r=&quot;fc -s&quot;&#8216;&#8216;, so that typing ``r cc&#8217;&#8216; runs the last command beginning with ``cc&#8217;&#8216; and typing ``r&#8217;&#8216; re-executes the last command. </p>
<p> If the first form is used, the return value is 0 unless an invalid option is encountered or <i>first</i> or <i>last</i> specify history lines out of range. If the <code>-e</code> option is supplied, the return value is the value of the last command executed or failure if an error occurs with the temporary file of commands. If the second form is used, the return status is that of the command re-executed, unless <i>cmd</i> does not specify a valid history line, in which case <code>fc</code> returns failure. </p>
 </dd>
<dt><code>fg</code> [<i>jobspec</i>]</dt>
<dd> <p> Resume <i>jobspec</i> in the foreground, and make it the current job. If <i>jobspec</i> is not present, the shell&#8217;s notion of the <i>current job</i> is used. The return value is that of the command placed into the foreground, or failure if run when job control is disabled or, when run with job control enabled, if <i>jobspec</i> does not specify a valid job or <i>jobspec</i> specifies a job that was started without job control. </p>
 </dd>
<dt><code>getopts</code><i>optstring</i><i>name</i> [<i>arg ...</i>]</dt>
<dd> <p> <code>getopts</code> is used by shell procedures to parse positional parameters. <i>optstring</i> contains the option characters to be recognized; if a character is followed by a colon, the option is expected to have an argument, which should be separated from it by white space. The colon and question mark characters may not be used as option characters. Each time it is invoked, <code>getopts</code> places the next option in the shell variable <i>name</i>, initializing <i>name</i> if it does not exist, and the index of the next argument to be processed into the variable <font SIZE="-1"><code>OPTIND</code>. </font> <font SIZE="-1"><code>OPTIND</code> </font> is initialized to 1 each time the shell or a shell script is invoked. When an option requires an argument, <code>getopts</code> places that argument into the variable <font SIZE="-1"><code>OPTARG</code>. </font> The shell does not reset <font SIZE="-1"><code>OPTIND</code> </font> automatically; it must be manually reset between multiple calls to <code>getopts</code> within the same shell invocation if a new set of parameters is to be used. </p>
<p> When the end of options is encountered, <code>getopts</code> exits with a return value greater than zero. <font SIZE="-1"><code>OPTIND</code> </font> is set to the index of the first non-option argument, and <i>name</i> is set to ?. </p>
<p> <code>getopts</code> normally parses the positional parameters, but if more arguments are supplied as <i>arg</i> values, <code>getopts</code> parses those instead. </p>
<p> <code>getopts</code> can report errors in two ways. If the first character of <i>optstring</i> is a colon, <i>silent</i> error reporting is used. In normal operation, diagnostic messages are printed when invalid options or missing option arguments are encountered. If the variable <font SIZE="-1"><code>OPTERR</code> </font> is set to 0, no error messages will be displayed, even if the first character of <i>optstring</i> is not a colon. </p>
<p> If an invalid option is seen, <code>getopts</code> places ? into <i>name</i> and, if not silent, prints an error message and unsets <font SIZE="-1"><code>OPTARG</code>. </font> If <code>getopts</code> is silent, the option character found is placed in <font SIZE="-1"><code>OPTARG</code> </font> and no diagnostic message is printed. </p>
<p> If a required argument is not found, and <code>getopts</code> is not silent, a question mark (<code>?</code>) is placed in <i>name</i>, <font SIZE="-1"><code>OPTARG</code> </font> is unset, and a diagnostic message is printed. If <code>getopts</code> is silent, then a colon (<code>:</code>) is placed in <i>name</i> and <font SIZE="-1"><code>OPTARG</code> </font> is set to the option character found. </p>
<p> <code>getopts</code> returns true if an option, specified or unspecified, is found. It returns false if the end of options is encountered or an error occurs. </p>
 </dd>
<dt><code>hash</code> [<code>-lr</code>] [<code>-p</code><i>filename</i>] [<code>-dt</code>] [<i>name</i>]</dt>
<dd> <p> Each time <code>hash</code> is invoked, the full pathname of the command <i>name</i> is determined by searching the directories in <code>$PATH</code> and remembered. Any previously-remembered pathname is discarded. If the <code>-p</code> option is supplied, no path search is performed, and <i>filename</i> is used as the full filename of the command. The <code>-r</code> option causes the shell to forget all remembered locations. The <code>-d</code> option causes the shell to forget the remembered location of each <i>name</i>. If the <code>-t</code> option is supplied, the full pathname to which each <i>name</i> corresponds is printed. If multiple <i>name</i> arguments are supplied with <code>-t</code>, the <i>name</i> is printed before the hashed full pathname. The <code>-l</code> option causes output to be displayed in a format that may be reused as input. If no arguments are given, or if only <code>-l</code> is supplied, information about remembered commands is printed. The return status is true unless a <i>name</i> is not found or an invalid option is supplied. </p>
 </dd>
<dt><code>help</code> [<code>-dms</code>] [<i>pattern</i>]</dt>
<dd> <p> Display helpful information about builtin commands. If <i>pattern</i> is specified, <code>help</code> gives detailed help on all commands matching <i>pattern</i>; otherwise help for all the builtins and shell control structures is printed. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>-d</code></dt>
<dd> <p> Display a short description of each <i>pattern</i> </p>
 </dd>
<dt><code>-m</code></dt>
<dd> <p> Display the description of each <i>pattern</i> in a manpage-like format </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> Display only a short usage synopsis for each <i>pattern</i> </p>
 </dd></dl>
<p> The return status is 0 unless no command matches <i>pattern</i>. </dl>
 </p>
<dt><code>history [</code><i>n</i>]</dt>
<dd>  </dd>
<dt><code>history</code><code>-c</code></dt>
<dd>  </dd>
<dt><code>history -d</code><i>offset</i></dt>
<dd>  </dd>
<dt><code>history -d</code><i>start</i>-<i>end</i></dt>
<dd>  </dd>
<dt><code>history</code><code>-anrw</code> [<i>filename</i>]</dt>
<dd>  </dd>
<dt><code>history</code><code>-p</code><i>arg</i> [<i>arg ...</i>]</dt>
<dd>  </dd>
<dt><code>history</code><code>-s</code><i>arg</i> [<i>arg ...</i>]</dt>
<dd> <p> With no options, display the command history list with line numbers. Lines listed with a <code>*</code> have been modified. An argument of <i>n</i> lists only the last <i>n</i> lines. If the shell variable <font SIZE="-1"><code>HISTTIMEFORMAT</code> </font> is set and not null, it is used as a format string for <i><a href="/docs/linux/man/3-strftime/">strftime</a></i>(3) to display the time stamp associated with each displayed history entry. No intervening blank is printed between the formatted time stamp and the history line. If <i>filename</i> is supplied, it is used as the name of the history file; if not, the value of <font SIZE="-1"><code>HISTFILE</code> </font> is used. Options, if supplied, have the following meanings: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>-c</code></dt>
<dd> <p> Clear the history list by deleting all the entries. </p>
 </dd>
<dt><code>-d</code><i>offset</i></dt>
<dd> <p> Delete the history entry at position <i>offset</i>. If <i>offset</i> is negative, it is interpreted as relative to one greater than the last history position, so negative indices count back from the end of the history, and an index of -1 refers to the current <code>history -d</code> command. </p>
 </dd>
<dt><code>-d</code><i>start</i>-<i>end</i></dt>
<dd> <p> Delete the history entries between positions <i>start</i> and <i>end</i>, inclusive. Positive and negative values for <i>start</i> and <i>end</i> are interpreted as described above. </p>
 </dd>
<dt><code>-a</code></dt>
<dd> <p> Append the ``new&#8217;&#8216; history lines to the history file. These are history lines entered since the beginning of the current <code>bash</code> session, but not already appended to the history file. </p>
 </dd>
<dt><code>-n</code></dt>
<dd> <p> Read the history lines not already read from the history file into the current history list. These are lines appended to the history file since the beginning of the current <code>bash</code> session. </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> Read the contents of the history file and append them to the current history list. </p>
 </dd>
<dt><code>-w</code></dt>
<dd> <p> Write the current history list to the history file, overwriting the history file&#8217;s contents. </p>
 </dd>
<dt><code>-p</code></dt>
<dd> <p> Perform history substitution on the following <i>args</i> and display the result on the standard output. Does not store the results in the history list. Each <i>arg</i> must be quoted to disable normal history expansion. </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> Store the <i>args</i> in the history list as a single entry. The last command in the history list is removed before the <i>args</i> are added. </p>
 </dd></dl>
<p> If the <font SIZE="-1"><code>HISTTIMEFORMAT</code> </font> variable is set, the time stamp information associated with each history entry is written to the history file, marked with the history comment character. When the history file is read, lines beginning with the history comment character followed immediately by a digit are interpreted as timestamps for the following history entry. The return value is 0 unless an invalid option is encountered, an error occurs while reading or writing the history file, an invalid <i>offset</i> is supplied as an argument to <code>-d</code>, or the history expansion supplied as an argument to <code>-p</code> fails. </dl>
 </p>
<dt><code>jobs</code> [<code>-lnprs</code>] [ <i>jobspec</i> ... ]</dt>
<dd>  </dd>
<dt><code>jobs</code><code>-x</code><i>command</i> [ <i>args</i> ... ]</dt>
<dd> <p> The first form lists the active jobs. The options have the following meanings: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>-l</code></dt>
<dd> <p> List process IDs in addition to the normal information. </p>
 </dd>
<dt><code>-n</code></dt>
<dd> <p> Display information only about jobs that have changed status since the user was last notified of their status. </p>
 </dd>
<dt><code>-p</code></dt>
<dd> <p> List only the process ID of the job&#8217;s process group leader. </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> Display only running jobs. </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> Display only stopped jobs. </p>
 </dd></dl>
<p> If <i>jobspec</i> is given, output is restricted to information about that job. The return status is 0 unless an invalid option is encountered or an invalid <i>jobspec</i> is supplied. </p>
<p> If the <code>-x</code> option is supplied, <code>jobs</code> replaces any <i>jobspec</i> found in <i>command</i> or <i>args</i> with the corresponding process group ID, and executes <i>command</i> passing it <i>args</i>, returning its exit status. </dl>
 </p>
<dt><code>kill</code> [<code>-s</code><i>sigspec</i> | <code>-n</code><i>signum</i> | <code>-</code><i>sigspec</i>] [<i>pid</i> | <i>jobspec</i>] ...</dt>
<dd>  </dd>
<dt><code>kill</code><code>-l</code>|<code>-L</code> [<i>sigspec</i> | <i>exit_status</i>]</dt>
<dd> <p> Send the signal named by <i>sigspec</i> or <i>signum</i> to the processes named by <i>pid</i> or <i>jobspec</i>. <i>sigspec</i> is either a case-insensitive signal name such as <font SIZE="-1"><code>SIGKILL</code> </font> (with or without the <font SIZE="-1"><code>SIG</code> </font> prefix) or a signal number; <i>signum</i> is a signal number. If <i>sigspec</i> is not present, then <font SIZE="-1"><code>SIGTERM</code> </font> is assumed. An argument of <code>-l</code> lists the signal names. If any arguments are supplied when <code>-l</code> is given, the names of the signals corresponding to the arguments are listed, and the return status is 0. The <i>exit_status</i> argument to <code>-l</code> is a number specifying either a signal number or the exit status of a process terminated by a signal. The <code>-L</code> option is equivalent to <code>-l</code>. <code>kill</code> returns true if at least one signal was successfully sent, or false if an error occurs or an invalid option is encountered. </p>
 </dd>
<dt><code>let</code><i>arg</i> [<i>arg</i> ...]</dt>
<dd> <p> Each <i>arg</i> is an arithmetic expression to be evaluated (see <font SIZE="-1"><code>ARITHMETIC EVALUATION</code> </font> above). If the last <i>arg</i> evaluates to 0, <code>let</code> returns 1; 0 is returned otherwise. </p>
 </dd>
<dt><code>local</code> [<i>option</i>] [<i>name</i>[=<i>value</i>] ... | - ]</dt>
<dd> <p> For each argument, a local variable named <i>name</i> is created, and assigned <i>value</i>. The <i>option</i> can be any of the options accepted by <code>declare</code>. When <code>local</code> is used within a function, it causes the variable <i>name</i> to have a visible scope restricted to that function and its children. If <i>name</i> is -, the set of shell options is made local to the function in which <code>local</code> is invoked: shell options changed using the <code>set</code> builtin inside the function are restored to their original values when the function returns. The restore is effected as if a series of <code>set</code> commands were executed to restore the values that were in place before the function. With no operands, <code>local</code> writes a list of local variables to the standard output. It is an error to use <code>local</code> when not within a function. The return status is 0 unless <code>local</code> is used outside a function, an invalid <i>name</i> is supplied, or <i>name</i> is a readonly variable. </p>
 </dd>
<dt><code>logout</code></dt>
<dd> <p> Exit a login shell. </p>
 </dd>
<dt><code>mapfile</code> [<code>-d</code><i>delim</i>] [<code>-n</code><i>count</i>] [<code>-O</code><i>origin</i>] [<code>-s</code><i>count</i>] [<code>-t</code>] [<code>-u</code><i>fd</i>] [<code>-C</code><i>callback</i>] [<code>-c</code><i>quantum</i>] [<i>array</i>]</dt>
<dd>  </dd>
<dt><code>readarray</code> [<code>-d</code><i>delim</i>] [<code>-n</code><i>count</i>] [<code>-O</code><i>origin</i>] [<code>-s</code><i>count</i>] [<code>-t</code>] [<code>-u</code><i>fd</i>] [<code>-C</code><i>callback</i>] [<code>-c</code><i>quantum</i>] [<i>array</i>]</dt>
<dd> <p> Read lines from the standard input into the indexed array variable <i>array</i>, or from file descriptor <i>fd</i> if the <code>-u</code> option is supplied. The variable <font SIZE="-1"><code>MAPFILE</code> </font> is the default <i>array</i>. Options, if supplied, have the following meanings: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>-d</code></dt>
<dd> <p> The first character of <i>delim</i> is used to terminate each input line, rather than newline. If <i>delim</i> is the empty string, <code>mapfile</code> will terminate a line when it reads a NUL character. </p>
 </dd>
<dt><code>-n</code></dt>
<dd> <p> Copy at most <i>count</i> lines. If <i>count</i> is 0, all lines are copied. </p>
 </dd>
<dt><code>-O</code></dt>
<dd> <p> Begin assigning to <i>array</i> at index <i>origin</i>. The default index is 0. </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> Discard the first <i>count</i> lines read. </p>
 </dd>
<dt><code>-t</code></dt>
<dd> <p> Remove a trailing <i>delim</i> (default newline) from each line read. </p>
 </dd>
<dt><code>-u</code></dt>
<dd> <p> Read lines from file descriptor <i>fd</i> instead of the standard input. </p>
 </dd>
<dt><code>-C</code></dt>
<dd> <p> Evaluate <i>callback</i> each time <i>quantum</i> lines are read. The <code>-c</code> option specifies <i>quantum</i>. </p>
 </dd>
<dt><code>-c</code></dt>
<dd> <p> Specify the number of lines read between each call to <i>callback</i>. </p>
 </dd></dl>
<p> If <code>-C</code> is specified without <code>-c</code>, the default quantum is 5000. When <i>callback</i> is evaluated, it is supplied the index of the next array element to be assigned and the line to be assigned to that element as additional arguments. <i>callback</i> is evaluated after the line is read but before the array element is assigned. </p>
<p> If not supplied with an explicit origin, <code>mapfile</code> will clear <i>array</i> before assigning to it. </p>
<p> <code>mapfile</code> returns successfully unless an invalid option or option argument is supplied, <i>array</i> is invalid or unassignable, or if <i>array</i> is not an indexed array. </dl>
 </p>
<dt><code>popd</code> [-<code>n</code>] [+<i>n</i>] [-<i>n</i>]</dt>
<dd> <p> Removes entries from the directory stack. With no arguments, removes the top directory from the stack, and performs a <code>cd</code> to the new top directory. Arguments, if supplied, have the following meanings: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>-n</code></dt>
<dd> <p> Suppresses the normal change of directory when removing directories from the stack, so that only the stack is manipulated. </p>
 </dd>
<dt><code>+</code><i>n</i></dt>
<dd> <p> Removes the <i>n</i>th entry counting from the left of the list shown by <code>dirs</code>, starting with zero. For example: ``popd +0&#8217;&#8216; removes the first directory, ``popd +1&#8217;&#8216; the second. </p>
 </dd>
<dt><code>-</code><i>n</i></dt>
<dd> <p> Removes the <i>n</i>th entry counting from the right of the list shown by <code>dirs</code>, starting with zero. For example: ``popd -0&#8217;&#8216; removes the last directory, ``popd -1&#8217;&#8216; the next to last. </p>
 </dd></dl>
<p> If the <code>popd</code> command is successful, a <code>dirs</code> is performed as well, and the return status is 0. <code>popd</code> returns false if an invalid option is encountered, the directory stack is empty, a non-existent directory stack entry is specified, or the directory change fails. </dl>
 </p>
<dt><code>printf</code> [<code>-v</code><i>var</i>] <i>format</i> [<i>arguments</i>]</dt>
<dd> <p> Write the formatted <i>arguments</i> to the standard output under the control of the <i>format</i>. The <code>-v</code> option causes the output to be assigned to the variable <i>var</i> rather than being printed to the standard output. </p>
<p> The <i>format</i> is a character string which contains three types of objects: plain characters, which are simply copied to standard output, character escape sequences, which are converted and copied to the standard output, and format specifications, each of which causes printing of the next successive <i>argument</i>. In addition to the standard <i><a href="/docs/linux/man/1-printf/">printf</a></i>(1) format specifications, <code>printf</code> interprets the following extensions: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>%b</code></dt>
<dd> <p> causes <code>printf</code> to expand backslash escape sequences in the corresponding <i>argument</i> in the same way as <code>echo -e</code>. </p>
 </dd>
<dt><code>%q</code></dt>
<dd> <p> causes <code>printf</code> to output the corresponding <i>argument</i> in a format that can be reused as shell input. </p>
 </dd>
<dt><code>%(</code><i>datefmt</i>)T </dt>
<dd> <p> causes <code>printf</code> to output the date-time string resulting from using <i>datefmt</i> as a format string for <i><a href="/docs/linux/man/3-strftime/">strftime</a></i>(3). The corresponding <i>argument</i> is an integer representing the number of seconds since the epoch. Two special argument values may be used: -1 represents the current time, and -2 represents the time the shell was invoked. If no argument is specified, conversion behaves as if -1 had been given. This is an exception to the usual <code>printf</code> behavior. </p>
 </dd></dl>
<p> The %b, %q, and %T directives all use the field width and precision arguments from the format specification and write that many bytes from (or use that wide a field for) the expanded argument, which usually contains more characters than the original. </p>
<p> Arguments to non-string format specifiers are treated as C constants, except that a leading plus or minus sign is allowed, and if the leading character is a single or double quote, the value is the ASCII value of the following character. </p>
<p> The <i>format</i> is reused as necessary to consume all of the <i>arguments</i>. If the <i>format</i> requires more <i>arguments</i> than are supplied, the extra format specifications behave as if a zero value or null string, as appropriate, had been supplied. The return value is zero on success, non-zero on failure. </dl>
 </p>
<dt><code>pushd</code> [<code>-n</code>] [+<i>n</i>] [-<i>n</i>]</dt>
<dd>  </dd>
<dt><code>pushd</code> [<code>-n</code>] [<i>dir</i>]</dt>
<dd> <p> Adds a directory to the top of the directory stack, or rotates the stack, making the new top of the stack the current working directory. With no arguments, <code>pushd</code> exchanges the top two directories and returns 0, unless the directory stack is empty. Arguments, if supplied, have the following meanings: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>-n</code></dt>
<dd> <p> Suppresses the normal change of directory when rotating or adding directories to the stack, so that only the stack is manipulated. </p>
 </dd>
<dt><code>+</code><i>n</i></dt>
<dd> <p> Rotates the stack so that the <i>n</i>th directory (counting from the left of the list shown by <code>dirs</code>, starting with zero) is at the top. </p>
 </dd>
<dt><code>-</code><i>n</i></dt>
<dd> <p> Rotates the stack so that the <i>n</i>th directory (counting from the right of the list shown by <code>dirs</code>, starting with zero) is at the top. </p>
 </dd>
<dt><i>dir</i></dt>
<dd> <p> Adds <i>dir</i> to the directory stack at the top, making it the new current working directory as if it had been supplied as the argument to the <code>cd</code> builtin. </p>
 </dd></dl>
<p> If the <code>pushd</code> command is successful, a <code>dirs</code> is performed as well. If the first form is used, <code>pushd</code> returns 0 unless the cd to <i>dir</i> fails. With the second form, <code>pushd</code> returns 0 unless the directory stack is empty, a non-existent directory stack element is specified, or the directory change to the specified new current directory fails. </dl>
 </p>
<dt><code>pwd</code> [<code>-LP</code>]</dt>
<dd> <p> Print the absolute pathname of the current working directory. The pathname printed contains no symbolic links if the <code>-P</code> option is supplied or the <code>-o physical</code> option to the <code>set</code> builtin command is enabled. If the <code>-L</code> option is used, the pathname printed may contain symbolic links. The return status is 0 unless an error occurs while reading the name of the current directory or an invalid option is supplied. </p>
 </dd>
<dt><code>read</code> [<code>-ers</code>] [<code>-a</code><i>aname</i>] [<code>-d</code><i>delim</i>] [<code>-i</code><i>text</i>] [<code>-n</code><i>nchars</i>] [<code>-N</code><i>nchars</i>] [<code>-p</code><i>prompt</i>] [<code>-t</code><i>timeout</i>] [<code>-u</code><i>fd</i>] [<i>name</i> ...]</dt>
<dd> <p> One line is read from the standard input, or from the file descriptor <i>fd</i> supplied as an argument to the <code>-u</code> option, split into words as described above under <code>Word Splitting</code>, and the first word is assigned to the first <i>name</i>, the second word to the second <i>name</i>, and so on. If there are more words than names, the remaining words and their intervening delimiters are assigned to the last <i>name</i>. If there are fewer words read from the input stream than names, the remaining names are assigned empty values. The characters in <font SIZE="-1"><code>IFS</code> </font> are used to split the line into words using the same rules the shell uses for expansion (described above under <code>Word Splitting</code>). The backslash character (<code>\</code>) may be used to remove any special meaning for the next character read and for line continuation. Options, if supplied, have the following meanings: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>-a </code><i>aname</i></dt>
<dd> <p> The words are assigned to sequential indices of the array variable <i>aname</i>, starting at 0. <i>aname</i> is unset before any new values are assigned. Other <i>name</i> arguments are ignored. </p>
 </dd>
<dt><code>-d </code><i>delim</i></dt>
<dd> <p> The first character of <i>delim</i> is used to terminate the input line, rather than newline. If <i>delim</i> is the empty string, <code>read</code> will terminate a line when it reads a NUL character. </p>
 </dd>
<dt><code>-e</code></dt>
<dd> <p> If the standard input is coming from a terminal, <code>readline</code> (see <font SIZE="-1"><code>READLINE</code> </font> above) is used to obtain the line. Readline uses the current (or default, if line editing was not previously active) editing settings, but uses Readline&#8217;s default filename completion. </p>
 </dd>
<dt><code>-i </code><i>text</i></dt>
<dd> <p> If <code>readline</code> is being used to read the line, <i>text</i> is placed into the editing buffer before editing begins. </p>
 </dd>
<dt><code>-n </code><i>nchars</i></dt>
<dd> <p> <code>read</code> returns after reading <i>nchars</i> characters rather than waiting for a complete line of input, but honors a delimiter if fewer than <i>nchars</i> characters are read before the delimiter. </p>
 </dd>
<dt><code>-N </code><i>nchars</i></dt>
<dd> <p> <code>read</code> returns after reading exactly <i>nchars</i> characters rather than waiting for a complete line of input, unless EOF is encountered or <code>read</code> times out. Delimiter characters encountered in the input are not treated specially and do not cause <code>read</code> to return until <i>nchars</i> characters are read. The result is not split on the characters in <code>IFS</code>; the intent is that the variable is assigned exactly the characters read (with the exception of backslash; see the <code>-r</code> option below). </p>
 </dd>
<dt><code>-p </code><i>prompt</i></dt>
<dd> <p> Display <i>prompt</i> on standard error, without a trailing newline, before attempting to read any input. The prompt is displayed only if input is coming from a terminal. </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> Backslash does not act as an escape character. The backslash is considered to be part of the line. In particular, a backslash-newline pair may not then be used as a line continuation. </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> Silent mode. If input is coming from a terminal, characters are not echoed. </p>
 </dd>
<dt><code>-t </code><i>timeout</i></dt>
<dd> <p> Cause <code>read</code> to time out and return failure if a complete line of input (or a specified number of characters) is not read within <i>timeout</i> seconds. <i>timeout</i> may be a decimal number with a fractional portion following the decimal point. This option is only effective if <code>read</code> is reading input from a terminal, pipe, or other special file; it has no effect when reading from regular files. If <code>read</code> times out, <code>read</code> saves any partial input read into the specified variable <i>name</i>. If <i>timeout</i> is 0, <code>read</code> returns immediately, without trying to read any data. The exit status is 0 if input is available on the specified file descriptor, non-zero otherwise. The exit status is greater than 128 if the timeout is exceeded. </p>
 </dd>
<dt><code>-u </code><i>fd</i></dt>
<dd> <p> Read input from file descriptor <i>fd</i>. </p>
 </dd></dl>
<p> If no <i>names</i> are supplied, the line read, without the ending delimiter but otherwise unmodified, is assigned to the variable <font SIZE="-1"><code>REPLY</code>. </font> The exit status is zero, unless end-of-file is encountered, <code>read</code> times out (in which case the status is greater than 128), a variable assignment error (such as assigning to a readonly variable) occurs, or an invalid file descriptor is supplied as the argument to <code>-u</code>. </dl>
 </p>
<dt><code>readonly</code> [<code>-aAf</code>] [<code>-p</code>] [<i>name</i>[=<i>word</i>] ...]</dt>
<dd> <p> The given <i>names</i> are marked readonly; the values of these <i>names</i> may not be changed by subsequent assignment. If the <code>-f</code> option is supplied, the functions corresponding to the <i>names</i> are so marked. The <code>-a</code> option restricts the variables to indexed arrays; the <code>-A</code> option restricts the variables to associative arrays. If both options are supplied, <code>-A</code> takes precedence. If no <i>name</i> arguments are given, or if the <code>-p</code> option is supplied, a list of all readonly names is printed. The other options may be used to restrict the output to a subset of the set of readonly names. The <code>-p</code> option causes output to be displayed in a format that may be reused as input. If a variable name is followed by =<i>word</i>, the value of the variable is set to <i>word</i>. The return status is 0 unless an invalid option is encountered, one of the <i>names</i> is not a valid shell variable name, or <code>-f</code> is supplied with a <i>name</i> that is not a function. </p>
 </dd>
<dt><code>return</code> [<i>n</i>]</dt>
<dd> <p> Causes a function to stop executing and return the value specified by <i>n</i> to its caller. If <i>n</i> is omitted, the return status is that of the last command executed in the function body. If <code>return</code> is executed by a trap handler, the last command used to determine the status is the last command executed before the trap handler. If <code>return</code> is executed during a <code>DEBUG</code> trap, the last command used to determine the status is the last command executed by the trap handler before <code>return</code> was invoked. If <code>return</code> is used outside a function, but during execution of a script by the <code>.</code> (<code>source</code>) command, it causes the shell to stop executing that script and return either <i>n</i> or the exit status of the last command executed within the script as the exit status of the script. If <i>n</i> is supplied, the return value is its least significant 8 bits. The return status is non-zero if <code>return</code> is supplied a non-numeric argument, or is used outside a function and not during execution of a script by <code>.</code> or <code>source</code>. Any command associated with the <code>RETURN</code> trap is executed before execution resumes after the function or script. </p>
 </dd>
<dt><code>set</code> [<code>--abefhkmnptuvxBCEHPT</code>] [<code>-o</code><i>option-name</i>] [<i>arg</i> ...]</dt>
<dd>  </dd>
<dt><code>set</code> [<code>+abefhkmnptuvxBCEHPT</code>] [<code>+o</code><i>option-name</i>] [<i>arg</i> ...]</dt>
<dd> <p> Without options, the name and value of each shell variable are displayed in a format that can be reused as input for setting or resetting the currently-set variables. Read-only variables cannot be reset. In <i>posix mode</i>, only shell variables are listed. The output is sorted according to the current locale. When options are specified, they set or unset shell attributes. Any arguments remaining after option processing are treated as values for the positional parameters and are assigned, in order, to <code>$1</code>, <code>$2</code>, <code>...</code> <code>$</code><i>n</i>. Options, if specified, have the following meanings: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>-a</code></dt>
<dd> <p> Each variable or function that is created or modified is given the export attribute and marked for export to the environment of subsequent commands. </p>
 </dd>
<dt><code>-b</code></dt>
<dd> <p> Report the status of terminated background jobs immediately, rather than before the next primary prompt. This is effective only when job control is enabled. </p>
 </dd>
<dt><code>-e</code></dt>
<dd> <p> Exit immediately if a <i>pipeline</i> (which may consist of a single <i>simple command</i>), a <i>list</i>, or a <i>compound command</i> (see <font SIZE="-1"><code>SHELL GRAMMAR</code> </font> above), exits with a non-zero status. The shell does not exit if the command that fails is part of the command list immediately following a <code>while</code> or <code>until</code> keyword, part of the test following the <code>if</code> or <code>elif</code> reserved words, part of any command executed in a <code>&amp;&amp;</code> or <code>||</code> list except the command following the final <code>&amp;&amp;</code> or <code>||</code>, any command in a pipeline but the last, or if the command&#8217;s return value is being inverted with <code>!</code>. If a compound command other than a subshell returns a non-zero status because a command failed while <code>-e</code> was being ignored, the shell does not exit. A trap on <code>ERR</code>, if set, is executed before the shell exits. This option applies to the shell environment and each subshell environment separately (see <font SIZE="-1"><code>COMMAND EXECUTION ENVIRONMENT</code> </font> above), and may cause subshells to exit before executing all the commands in the subshell. </p>
<p> If a compound command or shell function executes in a context where <code>-e</code> is being ignored, none of the commands executed within the compound command or function body will be affected by the <code>-e</code> setting, even if <code>-e</code> is set and a command returns a failure status. If a compound command or shell function sets <code>-e</code> while executing in a context where <code>-e</code> is ignored, that setting will not have any effect until the compound command or the command containing the function call completes. </p>
 </dd>
<dt><code>-f</code></dt>
<dd> <p> Disable pathname expansion. </p>
 </dd>
<dt><code>-h</code></dt>
<dd> <p> Remember the location of commands as they are looked up for execution. This is enabled by default. </p>
 </dd>
<dt><code>-k</code></dt>
<dd> <p> All arguments in the form of assignment statements are placed in the environment for a command, not just those that precede the command name. </p>
 </dd>
<dt><code>-m</code></dt>
<dd> <p> Monitor mode. Job control is enabled. This option is on by default for interactive shells on systems that support it (see <font SIZE="-1"><code>JOB CONTROL</code> </font> above). All processes run in a separate process group. When a background job completes, the shell prints a line containing its exit status. </p>
 </dd>
<dt><code>-n</code></dt>
<dd> <p> Read commands but do not execute them. This may be used to check a shell script for syntax errors. This is ignored by interactive shells. </p>
 </dd>
<dt><code>-o </code><i>option-name</i></dt>
<dd> <p> The <i>option-name</i> can be one of the following: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>allexport</code></dt>
<dd> <p> Same as <code>-a</code>. </p>
 </dd>
<dt><code>braceexpand</code></dt>
<dd> <p> Same as <code>-B</code>. </p>
 </dd>
<dt><code>emacs</code></dt>
<dd> <p> Use an emacs-style command line editing interface. This is enabled by default when the shell is interactive, unless the shell is started with the <code>--noediting</code> option. This also affects the editing interface used for <code>read -e</code>. </p>
 </dd>
<dt><code>errexit</code></dt>
<dd> <p> Same as <code>-e</code>. </p>
 </dd>
<dt><code>errtrace</code></dt>
<dd> <p> Same as <code>-E</code>. </p>
 </dd>
<dt><code>functrace</code></dt>
<dd> <p> Same as <code>-T</code>. </p>
 </dd>
<dt><code>hashall</code></dt>
<dd> <p> Same as <code>-h</code>. </p>
 </dd>
<dt><code>histexpand</code></dt>
<dd> <p> Same as <code>-H</code>. </p>
 </dd>
<dt><code>history</code></dt>
<dd> <p> Enable command history, as described above under <font SIZE="-1"><code>HISTORY</code>. </font> This option is on by default in interactive shells. </p>
 </dd>
<dt><code>ignoreeof</code></dt>
<dd> <p> The effect is as if the shell command ``IGNOREEOF=10&#8217;&#8216; had been executed (see <code>Shell Variables</code> above). </p>
 </dd>
<dt><code>keyword</code></dt>
<dd> <p> Same as <code>-k</code>. </p>
 </dd>
<dt><code>monitor</code></dt>
<dd> <p> Same as <code>-m</code>. </p>
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
<dd> <p> Currently ignored. </p>
 </dd>
<dt><code>notify</code></dt>
<dd> <p> Same as <code>-b</code>. </p>
 </dd>
<dt><code>nounset</code></dt>
<dd> <p> Same as <code>-u</code>. </p>
 </dd>
<dt><code>onecmd</code></dt>
<dd> <p> Same as <code>-t</code>. </p>
 </dd>
<dt><code>physical</code></dt>
<dd> <p> Same as <code>-P</code>. </p>
 </dd>
<dt><code>pipefail</code></dt>
<dd> <p> If set, the return value of a pipeline is the value of the last (rightmost) command to exit with a non-zero status, or zero if all commands in the pipeline exit successfully. This option is disabled by default. </p>
 </dd>
<dt><code>posix</code></dt>
<dd> <p> Change the behavior of <code>bash</code> where the default operation differs from the POSIX standard to match the standard (<i>posix mode</i>). See <font SIZE="-1"><code>SEE ALSO</code> </font> below for a reference to a document that details how posix mode affects bash&#8217;s behavior. </p>
 </dd>
<dt><code>privileged</code></dt>
<dd> <p> Same as <code>-p</code>. </p>
 </dd>
<dt><code>verbose</code></dt>
<dd> <p> Same as <code>-v</code>. </p>
 </dd>
<dt><code>vi</code></dt>
<dd> <p> Use a vi-style command line editing interface. This also affects the editing interface used for <code>read -e</code>. </p>
 </dd>
<dt><code>xtrace</code></dt>
<dd> <p> Same as <code>-x</code>. </p>
 </dd></dl>
<p> If <code>-o</code> is supplied with no <i>option-name</i>, the values of the current options are printed. If <code>+o</code> is supplied with no <i>option-name</i>, a series of <code>set</code> commands to recreate the current option settings is displayed on the standard output. </dl>
 </p>
<dt><code>-p</code></dt>
<dd> <p> Turn on <i>privileged</i> mode. In this mode, the <font SIZE="-1"><code>$ENV</code> </font> and <font SIZE="-1"><code>$BASH_ENV</code> </font> files are not processed, shell functions are not inherited from the environment, and the <font SIZE="-1"><code>SHELLOPTS</code>, </font> <font SIZE="-1"><code>BASHOPTS</code>, </font> <font SIZE="-1"><code>CDPATH</code>, </font> and <font SIZE="-1"><code>GLOBIGNORE</code> </font> variables, if they appear in the environment, are ignored. If the shell is started with the effective user (group) id not equal to the real user (group) id, and the <code>-p</code> option is not supplied, these actions are taken and the effective user id is set to the real user id. If the <code>-p</code> option is supplied at startup, the effective user id is not reset. Turning this option off causes the effective user and group ids to be set to the real user and group ids. </p>
 </dd>
<dt><code>-t</code></dt>
<dd> <p> Exit after reading and executing one command. </p>
 </dd>
<dt><code>-u</code></dt>
<dd> <p> Treat unset variables and parameters other than the special parameters &quot;@&quot; and &quot;*&quot; as an error when performing parameter expansion. If expansion is attempted on an unset variable or parameter, the shell prints an error message, and, if not interactive, exits with a non-zero status. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Print shell input lines as they are read. </p>
 </dd>
<dt><code>-x</code></dt>
<dd> <p> After expanding each <i>simple command</i>, <code>for</code> command, <code>case</code> command, <code>select</code> command, or arithmetic <code>for</code> command, display the expanded value of <font SIZE="-1"><code>PS4</code>, </font> followed by the command and its expanded arguments or associated word list. </p>
 </dd>
<dt><code>-B</code></dt>
<dd> <p> The shell performs brace expansion (see <code>Brace Expansion</code> above). This is on by default. </p>
 </dd>
<dt><code>-C</code></dt>
<dd> <p> If set, <code>bash</code> does not overwrite an existing file with the <code>&gt;</code>, <code>&gt;&amp;</code>, and <code>&lt;&gt;</code> redirection operators. This may be overridden when creating output files by using the redirection operator <code>&gt;|</code> instead of <code>&gt;</code>. </p>
 </dd>
<dt><code>-E</code></dt>
<dd> <p> If set, any trap on <code>ERR</code> is inherited by shell functions, command substitutions, and commands executed in a subshell environment. The <code>ERR</code> trap is normally not inherited in such cases. </p>
 </dd>
<dt><code>-H</code></dt>
<dd> <p> Enable <code>!</code> style history substitution. This option is on by default when the shell is interactive. </p>
 </dd>
<dt><code>-P</code></dt>
<dd> <p> If set, the shell does not resolve symbolic links when executing commands such as <code>cd</code> that change the current working directory. It uses the physical directory structure instead. By default, <code>bash</code> follows the logical chain of directories when performing commands which change the current directory. </p>
 </dd>
<dt><code>-T</code></dt>
<dd> <p> If set, any traps on <code>DEBUG</code> and <code>RETURN</code> are inherited by shell functions, command substitutions, and commands executed in a subshell environment. The <code>DEBUG</code> and <code>RETURN</code> traps are normally not inherited in such cases. </p>
 </dd>
<dt><code>--</code></dt>
<dd> <p> If no arguments follow this option, then the positional parameters are unset. Otherwise, the positional parameters are set to the <i>arg</i>s, even if some of them begin with a <code>-</code>. </p>
 </dd>
<dt><code>-</code></dt>
<dd> <p> Signal the end of options, cause all remaining <i>arg</i>s to be assigned to the positional parameters. The <code>-x</code> and <code>-v</code> options are turned off. If there are no <i>arg</i>s, the positional parameters remain unchanged. </p>
 </dd></dl>
<p> The options are off by default unless otherwise noted. Using + rather than - causes these options to be turned off. The options can also be specified as arguments to an invocation of the shell. The current set of options may be found in <code>$-</code>. The return status is always true unless an invalid option is encountered. </dl>
 </p>
<dt><code>shift</code> [<i>n</i>]</dt>
<dd> <p> The positional parameters from <i>n</i>+1 ... are renamed to <code>$1</code> <code>....</code> Parameters represented by the numbers <code>$#</code> down to <code>$#</code>-<i>n</i>+1 are unset. <i>n</i> must be a non-negative number less than or equal to <code>$#</code>. If <i>n</i> is 0, no parameters are changed. If <i>n</i> is not given, it is assumed to be 1. If <i>n</i> is greater than <code>$#</code>, the positional parameters are not changed. The return status is greater than zero if <i>n</i> is greater than <code>$#</code> or less than zero; otherwise 0. </p>
 </dd>
<dt><code>shopt</code> [<code>-pqsu</code>] [<code>-o</code>] [<i>optname</i> ...]</dt>
<dd> <p> Toggle the values of settings controlling optional shell behavior. The settings can be either those listed below, or, if the <code>-o</code> option is used, those available with the <code>-o</code> option to the <code>set</code> builtin command. With no options, or with the <code>-p</code> option, a list of all settable options is displayed, with an indication of whether or not each is set; if <i>optnames</i> are supplied, the output is restricted to those options. The <code>-p</code> option causes output to be displayed in a form that may be reused as input. Other options have the following meanings: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>-s</code></dt>
<dd> <p> Enable (set) each <i>optname</i>. </p>
 </dd>
<dt><code>-u</code></dt>
<dd> <p> Disable (unset) each <i>optname</i>. </p>
 </dd>
<dt><code>-q</code></dt>
<dd> <p> Suppresses normal output (quiet mode); the return status indicates whether the <i>optname</i> is set or unset. If multiple <i>optname</i> arguments are given with <code>-q</code>, the return status is zero if all <i>optnames</i> are enabled; non-zero otherwise. </p>
 </dd>
<dt><code>-o</code></dt>
<dd> <p> Restricts the values of <i>optname</i> to be those defined for the <code>-o</code> option to the <code>set</code> builtin. </p>
 </dd></dl>
<p> If either <code>-s</code> or <code>-u</code> is used with no <i>optname</i> arguments, <code>shopt</code> shows only those options which are set or unset, respectively. Unless otherwise noted, the <code>shopt</code> options are disabled (unset) by default. </p>
<p> The return status when listing options is zero if all <i>optnames</i> are enabled, non-zero otherwise. When setting or unsetting options, the return status is zero unless an <i>optname</i> is not a valid shell option. </p>
<p> The list of <code>shopt</code> options is: </p>
<dl>
<dt><code>assoc_expand_once</code></dt>
<dd> <p> If set, the shell suppresses multiple evaluation of associative array subscripts during arithmetic expression evaluation, while executing builtins that can perform variable assignments, and while executing builtins that perform array dereferencing. </p>
 </dd>
<dt><code>autocd</code></dt>
<dd> <p> If set, a command name that is the name of a directory is executed as if it were the argument to the <code>cd</code> command. This option is only used by interactive shells. </p>
 </dd>
<dt><code>cdable_vars</code></dt>
<dd> <p> If set, an argument to the <code>cd</code> builtin command that is not a directory is assumed to be the name of a variable whose value is the directory to change to. </p>
 </dd>
<dt><code>cdspell</code></dt>
<dd> <p> If set, minor errors in the spelling of a directory component in a <code>cd</code> command will be corrected. The errors checked for are transposed characters, a missing character, and one character too many. If a correction is found, the corrected filename is printed, and the command proceeds. This option is only used by interactive shells. </p>
 </dd>
<dt><code>checkhash</code></dt>
<dd> <p> If set, <code>bash</code> checks that a command found in the hash table exists before trying to execute it. If a hashed command no longer exists, a normal path search is performed. </p>
 </dd>
<dt><code>checkjobs</code></dt>
<dd> <p> If set, <code>bash</code> lists the status of any stopped and running jobs before exiting an interactive shell. If any jobs are running, this causes the exit to be deferred until a second exit is attempted without an intervening command (see <font SIZE="-1"><code>JOB CONTROL</code> </font> above). The shell always postpones exiting if any jobs are stopped. </p>
 </dd>
<dt><code>checkwinsize</code></dt>
<dd> <p> If set, <code>bash</code> checks the window size after each external (non-builtin) command and, if necessary, updates the values of <font SIZE="-1"><code>LINES</code> </font> and <font SIZE="-1"><code>COLUMNS</code>. </font> This option is enabled by default. </p>
 </dd>
<dt><code>cmdhist</code></dt>
<dd> <p> If set, <code>bash</code> attempts to save all lines of a multiple-line command in the same history entry. This allows easy re-editing of multi-line commands. This option is enabled by default, but only has an effect if command history is enabled, as described above under <font SIZE="-1"><code>HISTORY</code>. </font> </p>
 </dd>
<dt><code>compat31</code></dt>
<dd>  </dd>
<dt><code>compat32</code></dt>
<dd>  </dd>
<dt><code>compat40</code></dt>
<dd>  </dd>
<dt><code>compat41</code></dt>
<dd>  </dd>
<dt><code>compat42</code></dt>
<dd>  </dd>
<dt><code>compat43</code></dt>
<dd>  </dd>
<dt><code>compat44</code></dt>
<dd> <p> These control aspects of the shell&#8217;s compatibility mode (see <font SIZE="-1"><code>SHELL COMPATIBILITY MODE</code> </font> below). </p>
 </dd>
<dt><code>complete_fullquote</code></dt>
<dd> <p> If set, <code>bash</code> quotes all shell metacharacters in filenames and directory names when performing completion. If not set, <code>bash</code> removes metacharacters such as the dollar sign from the set of characters that will be quoted in completed filenames when these metacharacters appear in shell variable references in words to be completed. This means that dollar signs in variable names that expand to directories will not be quoted; however, any dollar signs appearing in filenames will not be quoted, either. This is active only when bash is using backslashes to quote completed filenames. This variable is set by default, which is the default bash behavior in versions through 4.2. </p>
 </dd>
<dt><code>direxpand</code></dt>
<dd> <p> If set, <code>bash</code> replaces directory names with the results of word expansion when performing filename completion. This changes the contents of the readline editing buffer. If not set, <code>bash</code> attempts to preserve what the user typed. </p>
 </dd>
<dt><code>dirspell</code></dt>
<dd> <p> If set, <code>bash</code> attempts spelling correction on directory names during word completion if the directory name initially supplied does not exist. </p>
 </dd>
<dt><code>dotglob</code></dt>
<dd> <p> If set, <code>bash</code> includes filenames beginning with a `.&#8216; in the results of pathname expansion. The filenames <code>``.&#8216;&#8216;</code> and <code>``..&#8216;&#8216;</code> must always be matched explicitly, even if <code>dotglob</code> is set. </p>
 </dd>
<dt><code>execfail</code></dt>
<dd> <p> If set, a non-interactive shell will not exit if it cannot execute the file specified as an argument to the <code>exec</code> builtin command. An interactive shell does not exit if <code>exec</code> fails. </p>
 </dd>
<dt><code>expand_aliases</code></dt>
<dd> <p> If set, aliases are expanded as described above under <font SIZE="-1"><code>ALIASES</code>. </font> This option is enabled by default for interactive shells. </p>
 </dd>
<dt><code>extdebug</code></dt>
<dd> <p> If set at shell invocation, or in a shell startup file, arrange to execute the debugger profile before the shell starts, identical to the <code>--debugger</code> option. If set after invocation, behavior intended for use by debuggers is enabled: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>1.</code></dt>
<dd> <p> The <code>-F</code> option to the <code>declare</code> builtin displays the source file name and line number corresponding to each function name supplied as an argument. </p>
 </dd>
<dt><code>2.</code></dt>
<dd> <p> If the command run by the <code>DEBUG</code> trap returns a non-zero value, the next command is skipped and not executed. </p>
 </dd>
<dt><code>3.</code></dt>
<dd> <p> If the command run by the <code>DEBUG</code> trap returns a value of 2, and the shell is executing in a subroutine (a shell function or a shell script executed by the <code>.</code> or <code>source</code> builtins), the shell simulates a call to <code>return</code>. </p>
 </dd>
<dt><code>4.</code></dt>
<dd> <p> <font SIZE="-1"><code>BASH_ARGC</code> </font> and <font SIZE="-1"><code>BASH_ARGV</code> </font> are updated as described in their descriptions above. </p>
 </dd>
<dt><code>5.</code></dt>
<dd> <p> Function tracing is enabled: command substitution, shell functions, and subshells invoked with <code>(</code> <i>command</i> <code>)</code> inherit the <code>DEBUG</code> and <code>RETURN</code> traps. </p>
 </dd>
<dt><code>6.</code></dt>
<dd> <p> Error tracing is enabled: command substitution, shell functions, and subshells invoked with <code>(</code> <i>command</i> <code>)</code> inherit the <code>ERR</code> trap. </p>
 </dd></dl>
</dl>
<dt><code>extglob</code></dt>
<dd> <p> If set, the extended pattern matching features described above under <code>Pathname Expansion</code> are enabled. </p>
 </dd>
<dt><code>extquote</code></dt>
<dd> <p> If set, <code>$</code>&#8216;<i>string</i>&#8216; and <code>$</code>&quot;<i>string</i>&quot; quoting is performed within <code>${</code><i>parameter</i><code>}</code> expansions enclosed in double quotes. This option is enabled by default. </p>
 </dd>
<dt><code>failglob</code></dt>
<dd> <p> If set, patterns which fail to match filenames during pathname expansion result in an expansion error. </p>
 </dd>
<dt><code>force_fignore</code></dt>
<dd> <p> If set, the suffixes specified by the <font SIZE="-1"><code>FIGNORE</code> </font> shell variable cause words to be ignored when performing word completion even if the ignored words are the only possible completions. See <font SIZE="-1"><code>SHELL VARIABLES</code></font> above for a description of <font SIZE="-1"><code>FIGNORE</code>. </font> This option is enabled by default. </p>
 </dd>
<dt><code>globasciiranges</code></dt>
<dd> <p> If set, range expressions used in pattern matching bracket expressions (see <font SIZE="-1"><code>Pattern Matching</code> </font> above) behave as if in the traditional C locale when performing comparisons. That is, the current locale&#8217;s collating sequence is not taken into account, so <code>b</code> will not collate between <code>A</code> and <code>B</code>, and upper-case and lower-case ASCII characters will collate together. </p>
 </dd>
<dt><code>globstar</code></dt>
<dd> <p> If set, the pattern <code>**</code> used in a pathname expansion context will match all files and zero or more directories and subdirectories. If the pattern is followed by a <code>/</code>, only directories and subdirectories match. </p>
 </dd>
<dt><code>gnu_errfmt</code></dt>
<dd> <p> If set, shell error messages are written in the standard GNU error message format. </p>
 </dd>
<dt><code>histappend</code></dt>
<dd> <p> If set, the history list is appended to the file named by the value of the <font SIZE="-1"><code>HISTFILE</code> </font> variable when the shell exits, rather than overwriting the file. </p>
 </dd>
<dt><code>histreedit</code></dt>
<dd> <p> If set, and <code>readline</code> is being used, a user is given the opportunity to re-edit a failed history substitution. </p>
 </dd>
<dt><code>histverify</code></dt>
<dd> <p> If set, and <code>readline</code> is being used, the results of history substitution are not immediately passed to the shell parser. Instead, the resulting line is loaded into the <code>readline</code> editing buffer, allowing further modification. </p>
 </dd>
<dt><code>hostcomplete</code></dt>
<dd> <p> If set, and <code>readline</code> is being used, <code>bash</code> will attempt to perform hostname completion when a word containing a <code>@</code> is being completed (see <code>Completing</code> under <font SIZE="-1"><code>READLINE</code> </font> above). This is enabled by default. </p>
 </dd>
<dt><code>huponexit</code></dt>
<dd> <p> If set, <code>bash</code> will send <font SIZE="-1"><code>SIGHUP</code> </font> to all jobs when an interactive login shell exits. </p>
 </dd>
<dt><code>inherit_errexit</code></dt>
<dd> <p> If set, command substitution inherits the value of the <code>errexit</code> option, instead of unsetting it in the subshell environment. This option is enabled when <i>posix mode</i> is enabled. </p>
 </dd>
<dt><code>interactive_comments</code></dt>
<dd> <p> If set, allow a word beginning with <code>#</code> to cause that word and all remaining characters on that line to be ignored in an interactive shell (see <font SIZE="-1"><code>COMMENTS</code> </font> above). This option is enabled by default. </p>
 </dd>
<dt><code>lastpipe</code></dt>
<dd> <p> If set, and job control is not active, the shell runs the last command of a pipeline not executed in the background in the current shell environment. </p>
 </dd>
<dt><code>lithist</code></dt>
<dd> <p> If set, and the <code>cmdhist</code> option is enabled, multi-line commands are saved to the history with embedded newlines rather than using semicolon separators where possible. </p>
 </dd>
<dt><code>localvar_inherit</code></dt>
<dd> <p> If set, local variables inherit the value and attributes of a variable of the same name that exists at a previous scope before any new value is assigned. The nameref attribute is not inherited. </p>
 </dd>
<dt><code>localvar_unset</code></dt>
<dd> <p> If set, calling <code>unset</code> on local variables in previous function scopes marks them so subsequent lookups find them unset until that function returns. This is identical to the behavior of unsetting local variables at the current function scope. </p>
 </dd>
<dt><code>login_shell</code></dt>
<dd> <p> The shell sets this option if it is started as a login shell (see <font SIZE="-1"><code>INVOCATION</code> </font> above). The value may not be changed. </p>
 </dd>
<dt><code>mailwarn</code></dt>
<dd> <p> If set, and a file that <code>bash</code> is checking for mail has been accessed since the last time it was checked, the message ``The mail in <i>mailfile</i> has been read&#8217;&#8216; is displayed. </p>
 </dd>
<dt><code>no_empty_cmd_completion</code></dt>
<dd> <p> If set, and <code>readline</code> is being used, <code>bash</code> will not attempt to search the <font SIZE="-1"><code>PATH</code> </font> for possible completions when completion is attempted on an empty line. </p>
 </dd>
<dt><code>nocaseglob</code></dt>
<dd> <p> If set, <code>bash</code> matches filenames in a case-insensitive fashion when performing pathname expansion (see <code>Pathname Expansion</code> above). </p>
 </dd>
<dt><code>nocasematch</code></dt>
<dd> <p> If set, <code>bash</code> matches patterns in a case-insensitive fashion when performing matching while executing <code>case</code> or <code>[[</code> conditional commands, when performing pattern substitution word expansions, or when filtering possible completions as part of programmable completion. </p>
 </dd>
<dt><code>nullglob</code></dt>
<dd> <p> If set, <code>bash</code> allows patterns which match no files (see <code>Pathname Expansion</code> above) to expand to a null string, rather than themselves. </p>
 </dd>
<dt><code>progcomp</code></dt>
<dd> <p> If set, the programmable completion facilities (see <code>Programmable Completion</code> above) are enabled. This option is enabled by default. </p>
 </dd>
<dt><code>progcomp_alias</code></dt>
<dd> <p> If set, and programmable completion is enabled, <code>bash</code> treats a command name that doesn&#8217;t have any completions as a possible alias and attempts alias expansion. If it has an alias, <code>bash</code> attempts programmable completion using the command word resulting from the expanded alias. </p>
 </dd>
<dt><code>promptvars</code></dt>
<dd> <p> If set, prompt strings undergo parameter expansion, command substitution, arithmetic expansion, and quote removal after being expanded as described in <font SIZE="-1"><code>PROMPTING</code> </font> above. This option is enabled by default. </p>
 </dd>
<dt><code>restricted_shell</code></dt>
<dd> <p> The shell sets this option if it is started in restricted mode (see <font SIZE="-1"><code>RESTRICTED SHELL</code> </font> below). The value may not be changed. This is not reset when the startup files are executed, allowing the startup files to discover whether or not a shell is restricted. </p>
 </dd>
<dt><code>shift_verbose</code></dt>
<dd> <p> If set, the <code>shift</code> builtin prints an error message when the shift count exceeds the number of positional parameters. </p>
 </dd>
<dt><code>sourcepath</code></dt>
<dd> <p> If set, the <code>source</code> (<code>.</code>) builtin uses the value of <font SIZE="-1"><code>PATH</code> </font> to find the directory containing the file supplied as an argument. This option is enabled by default. </p>
 </dd>
<dt><code>xpg_echo</code></dt>
<dd> <p> If set, the <code>echo</code> builtin expands backslash-escape sequences by default. </p>
 </dd></dl>
</dl>
<dt><code>suspend</code> [<code>-f</code>]</dt>
<dd> <p> Suspend the execution of this shell until it receives a <font SIZE="-1"><code>SIGCONT</code> </font> signal. A login shell cannot be suspended; the <code>-f</code> option can be used to override this and force the suspension. The return status is 0 unless the shell is a login shell and <code>-f</code> is not supplied, or if job control is not enabled. </p>
 </dd>
<dt><code>test</code><i>expr</i></dt>
<dd>  </dd>
<dt><code>[</code><i>expr</i><code>]</code></dt>
<dd> <p> Return a status of 0 (true) or 1 (false) depending on the evaluation of the conditional expression <i>expr</i>. Each operator and operand must be a separate argument. Expressions are composed of the primaries described above under <font SIZE="-1"><code>CONDITIONAL</code>EXPRESSIONS <code>.</code> </font> <code>test</code> does not accept any options, nor does it accept and ignore an argument of <code>--</code> as signifying the end of options. </p>
<p> Expressions may be combined using the following operators, listed in decreasing order of precedence. The evaluation depends on the number of arguments; see below. Operator precedence is used when there are five or more arguments. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>! </code><i>expr</i></dt>
<dd> <p> True if <i>expr</i> is false. </p>
 </dd>
<dt><code>( </code><i>expr</i> ) </dt>
<dd> <p> Returns the value of <i>expr</i>. This may be used to override the normal precedence of operators. </p>
 </dd>
<dt><i>expr1</i> -<code>a</code><i>expr2</i></dt>
<dd> <p> True if both <i>expr1</i> and <i>expr2</i> are true. </p>
 </dd>
<dt><i>expr1</i> -<code>o</code><i>expr2</i></dt>
<dd> <p> True if either <i>expr1</i> or <i>expr2</i> is true. </p>
 </dd></dl>
<p> <code>test</code> and <code>[</code> evaluate conditional expressions using a set of rules based on the number of arguments. </p>
<dl>
<dt>0 arguments</dt>
<dd> <p> The expression is false. </p>
 </dd>
<dt>1 argument</dt>
<dd> <p> The expression is true if and only if the argument is not null. </p>
 </dd>
<dt>2 arguments</dt>
<dd> <p> If the first argument is <code>!</code>, the expression is true if and only if the second argument is null. If the first argument is one of the unary conditional operators listed above under <font SIZE="-1"><code>CONDITIONAL</code>EXPRESSIONS <code>,</code> </font> the expression is true if the unary test is true. If the first argument is not a valid unary conditional operator, the expression is false. </p>
 </dd>
<dt>3 arguments</dt>
<dd> <p> The following conditions are applied in the order listed. If the second argument is one of the binary conditional operators listed above under <font SIZE="-1"><code>CONDITIONAL</code>EXPRESSIONS <code>,</code> </font> the result of the expression is the result of the binary test using the first and third arguments as operands. The <code>-a</code> and <code>-o</code> operators are considered binary operators when there are three arguments. If the first argument is <code>!</code>, the value is the negation of the two-argument test using the second and third arguments. If the first argument is exactly <code>(</code> and the third argument is exactly <code>)</code>, the result is the one-argument test of the second argument. Otherwise, the expression is false. </p>
 </dd>
<dt>4 arguments</dt>
<dd> <p> If the first argument is <code>!</code>, the result is the negation of the three-argument expression composed of the remaining arguments. Otherwise, the expression is parsed and evaluated according to precedence using the rules listed above. </p>
 </dd>
<dt>5 or more arguments</dt>
<dd> <p> The expression is parsed and evaluated according to precedence using the rules listed above. </p>
 </dd></dl>
<p> When used with <code>test</code> or <code>[</code>, the <code>&lt;</code> and <code>&gt;</code> operators sort lexicographically using ASCII ordering. </dl>
 </p>
<dt><code>times</code></dt>
<dd> <p> Print the accumulated user and system times for the shell and for processes run from the shell. The return status is 0. </p>
 </dd>
<dt><code>trap</code> [<code>-lp</code>] [[<i>arg</i>] <i>sigspec</i> ...]</dt>
<dd> <p> The command <i>arg</i> is to be read and executed when the shell receives signal(s) <i>sigspec</i>. If <i>arg</i> is absent (and there is a single <i>sigspec</i>) or <code>-</code>, each specified signal is reset to its original disposition (the value it had upon entrance to the shell). If <i>arg</i> is the null string the signal specified by each <i>sigspec</i> is ignored by the shell and by the commands it invokes. If <i>arg</i> is not present and <code>-p</code> has been supplied, then the trap commands associated with each <i>sigspec</i> are displayed. If no arguments are supplied or if only <code>-p</code> is given, <code>trap</code> prints the list of commands associated with each signal. The <code>-l</code> option causes the shell to print a list of signal names and their corresponding numbers. Each <i>sigspec</i> is either a signal name defined in &lt;<i>signal.h</i>&gt;, or a signal number. Signal names are case insensitive and the <font SIZE="-1"><code>SIG</code> </font> prefix is optional. </p>
<p> If a <i>sigspec</i> is <font SIZE="-1"><code>EXIT</code> </font> (0) the command <i>arg</i> is executed on exit from the shell. If a <i>sigspec</i> is <font SIZE="-1"><code>DEBUG</code>, </font> the command <i>arg</i> is executed before every <i>simple command</i>, <i>for</i> command, <i>case</i> command, <i>select</i> command, every arithmetic <i>for</i> command, and before the first command executes in a shell function (see <font SIZE="-1"><code>SHELL GRAMMAR</code> </font> above). Refer to the description of the <code>extdebug</code> option to the <code>shopt</code> builtin for details of its effect on the <code>DEBUG</code> trap. If a <i>sigspec</i> is <font SIZE="-1"><code>RETURN</code>, </font> the command <i>arg</i> is executed each time a shell function or a script executed with the <code>.</code> or <code>source</code> builtins finishes executing. </p>
<p> If a <i>sigspec</i> is <font SIZE="-1"><code>ERR</code>, </font> the command <i>arg</i> is executed whenever a pipeline (which may consist of a single simple command), a list, or a compound command returns a non-zero exit status, subject to the following conditions. The <font SIZE="-1"><code>ERR</code> </font> trap is not executed if the failed command is part of the command list immediately following a <code>while</code> or <code>until</code> keyword, part of the test in an <i>if</i> statement, part of a command executed in a <code>&amp;&amp;</code> or <code>||</code> list except the command following the final <code>&amp;&amp;</code> or <code>||</code>, any command in a pipeline but the last, or if the command&#8217;s return value is being inverted using <code>!</code>. These are the same conditions obeyed by the <code>errexit</code> (<code>-e</code>) option. </p>
<p> Signals ignored upon entry to the shell cannot be trapped or reset. Trapped signals that are not being ignored are reset to their original values in a subshell or subshell environment when one is created. The return status is false if any <i>sigspec</i> is invalid; otherwise <code>trap</code> returns true. </p>
 </dd>
<dt><code>type</code> [<code>-aftpP</code>] <i>name</i> [<i>name</i> ...]</dt>
<dd> <p> With no options, indicate how each <i>name</i> would be interpreted if used as a command name. If the <code>-t</code> option is used, <code>type</code> prints a string which is one of <i>alias</i>, <i>keyword</i>, <i>function</i>, <i>builtin</i>, or <i>file</i> if <i>name</i> is an alias, shell reserved word, function, builtin, or disk file, respectively. If the <i>name</i> is not found, then nothing is printed, and an exit status of false is returned. If the <code>-p</code> option is used, <code>type</code> either returns the name of the disk file that would be executed if <i>name</i> were specified as a command name, or nothing if ``type -t name&#8217;&#8216; would not return <i>file</i>. The <code>-P</code> option forces a <font SIZE="-1"><code>PATH</code> </font> search for each <i>name</i>, even if ``type -t name&#8217;&#8216; would not return <i>file</i>. If a command is hashed, <code>-p</code> and <code>-P</code> print the hashed value, which is not necessarily the file that appears first in <font SIZE="-1"><code>PATH</code>. </font> If the <code>-a</code> option is used, <code>type</code> prints all of the places that contain an executable named <i>name</i>. This includes aliases and functions, if and only if the <code>-p</code> option is not also used. The table of hashed commands is not consulted when using <code>-a</code>. The <code>-f</code> option suppresses shell function lookup, as with the <code>command</code> builtin. <code>type</code> returns true if all of the arguments are found, false if any are not found. </p>
 </dd>
<dt><code>ulimit</code> [<code>-HS</code>] <code>-a</code></dt>
<dd>  </dd>
<dt><code>ulimit</code> [<code>-HS</code>] [<code>-bcdefiklmnpqrstuvxPRT</code> [<i>limit</i>]]</dt>
<dd> <p> Provides control over the resources available to the shell and to processes started by it, on systems that allow such control. The <code>-H</code> and <code>-S</code> options specify that the hard or soft limit is set for the given resource. A hard limit cannot be increased by a non-root user once it is set; a soft limit may be increased up to the value of the hard limit. If neither <code>-H</code> nor <code>-S</code> is specified, both the soft and hard limits are set. The value of <i>limit</i> can be a number in the unit specified for the resource or one of the special values <code>hard</code>, <code>soft</code>, or <code>unlimited</code>, which stand for the current hard limit, the current soft limit, and no limit, respectively. If <i>limit</i> is omitted, the current value of the soft limit of the resource is printed, unless the <code>-H</code> option is given. When more than one resource is specified, the limit name and unit, if appropriate, are printed before the value. Other options are interpreted as follows: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>-a</code></dt>
<dd> <p> All current limits are reported; no limits are set </p>
 </dd>
<dt><code>-b</code></dt>
<dd> <p> The maximum socket buffer size </p>
 </dd>
<dt><code>-c</code></dt>
<dd> <p> The maximum size of core files created </p>
 </dd>
<dt><code>-d</code></dt>
<dd> <p> The maximum size of a process&#8217;s data segment </p>
 </dd>
<dt><code>-e</code></dt>
<dd> <p> The maximum scheduling priority (&quot;nice&quot;) </p>
 </dd>
<dt><code>-f</code></dt>
<dd> <p> The maximum size of files written by the shell and its children </p>
 </dd>
<dt><code>-i</code></dt>
<dd> <p> The maximum number of pending signals </p>
 </dd>
<dt><code>-k</code></dt>
<dd> <p> The maximum number of kqueues that may be allocated </p>
 </dd>
<dt><code>-l</code></dt>
<dd> <p> The maximum size that may be locked into memory </p>
 </dd>
<dt><code>-m</code></dt>
<dd> <p> The maximum resident set size (many systems do not honor this limit) </p>
 </dd>
<dt><code>-n</code></dt>
<dd> <p> The maximum number of open file descriptors (most systems do not allow this value to be set) </p>
 </dd>
<dt><code>-p</code></dt>
<dd> <p> The pipe size in 512-byte blocks (this may not be set) </p>
 </dd>
<dt><code>-q</code></dt>
<dd> <p> The maximum number of bytes in POSIX message queues </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> The maximum real-time scheduling priority </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> The maximum stack size </p>
 </dd>
<dt><code>-t</code></dt>
<dd> <p> The maximum amount of cpu time in seconds </p>
 </dd>
<dt><code>-u</code></dt>
<dd> <p> The maximum number of processes available to a single user </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> The maximum amount of virtual memory available to the shell and, on some systems, to its children </p>
 </dd>
<dt><code>-x</code></dt>
<dd> <p> The maximum number of file locks </p>
 </dd>
<dt><code>-P</code></dt>
<dd> <p> The maximum number of pseudoterminals </p>
 </dd>
<dt><code>-R</code></dt>
<dd> <p> The maximum time a real-time process can run before blocking, in microseconds </p>
 </dd>
<dt><code>-T</code></dt>
<dd> <p> The maximum number of threads </p>
 </dd></dl>
<p> If <i>limit</i> is given, and the <code>-a</code> option is not used, <i>limit</i> is the new value of the specified resource. If no option is given, then <code>-f</code> is assumed. Values are in 1024-byte increments, except for <code>-t</code>, which is in seconds; <code>-R</code>, which is in microseconds; <code>-p</code>, which is in units of 512-byte blocks; <code>-P</code>, <code>-T</code>, <code>-b</code>, <code>-k</code>, <code>-n</code>, and <code>-u</code>, which are unscaled values; and, when in posix mode, <code>-c</code> and <code>-f</code>, which are in 512-byte increments. The return status is 0 unless an invalid option or argument is supplied, or an error occurs while setting a new limit. </dl>
 </p>
<dt><code>umask</code> [<code>-p</code>] [<code>-S</code>] [<i>mode</i>]</dt>
<dd> <p> The user file-creation mask is set to <i>mode</i>. If <i>mode</i> begins with a digit, it is interpreted as an octal number; otherwise it is interpreted as a symbolic mode mask similar to that accepted by <i><a href="/docs/linux/man/1-chmod/">chmod</a></i>(1). If <i>mode</i> is omitted, the current value of the mask is printed. The <code>-S</code> option causes the mask to be printed in symbolic form; the default output is an octal number. If the <code>-p</code> option is supplied, and <i>mode</i> is omitted, the output is in a form that may be reused as input. The return status is 0 if the mode was successfully changed or if no <i>mode</i> argument was supplied, and false otherwise. </p>
 </dd>
<dt><code>unalias</code> [-<code>a</code>] [<i>name</i> ...]</dt>
<dd> <p> Remove each <i>name</i> from the list of defined aliases. If <code>-a</code> is supplied, all alias definitions are removed. The return value is true unless a supplied <i>name</i> is not a defined alias. </p>
 </dd>
<dt><code>unset</code> [-<code>fv</code>] [-<code>n</code>] [<i>name</i> ...]</dt>
<dd> <p> For each <i>name</i>, remove the corresponding variable or function. If the <code>-v</code> option is given, each <i>name</i> refers to a shell variable, and that variable is removed. Read-only variables may not be unset. If <code>-f</code> is specified, each <i>name</i> refers to a shell function, and the function definition is removed. If the <code>-n</code> option is supplied, and <i>name</i> is a variable with the <i>nameref</i> attribute, <i>name</i> will be unset rather than the variable it references. <code>-n</code> has no effect if the <code>-f</code> option is supplied. If no options are supplied, each <i>name</i> refers to a variable; if there is no variable by that name, a function with that name, if any, is unset. Each unset variable or function is removed from the environment passed to subsequent commands. If any of <font SIZE="-1"><code>BASH_ALIASES</code>, </font> <font SIZE="-1"><code>BASH_ARGV0</code>, </font> <font SIZE="-1"><code>BASH_CMDS</code>, </font> <font SIZE="-1"><code>BASH_COMMAND</code>, </font> <font SIZE="-1"><code>BASH_SUBSHELL</code>, </font> <font SIZE="-1"><code>BASHPID</code>, </font> <font SIZE="-1"><code>COMP_WORDBREAKS</code>, </font> <font SIZE="-1"><code>DIRSTACK</code>, </font> <font SIZE="-1"><code>EPOCHREALTIME</code>, </font> <font SIZE="-1"><code>EPOCHSECONDS</code>, </font> <font SIZE="-1"><code>FUNCNAME</code>, </font> <font SIZE="-1"><code>GROUPS</code>, </font> <font SIZE="-1"><code>HISTCMD</code>, </font> <font SIZE="-1"><code>LINENO</code>, </font> <font SIZE="-1"><code>RANDOM</code>, </font> <font SIZE="-1"><code>SECONDS</code>, </font> or <font SIZE="-1"><code>SRANDOM</code> </font> are unset, they lose their special properties, even if they are subsequently reset. The exit status is true unless a <i>name</i> is readonly. </p>
 </dd>
<dt><code>wait</code> [<code>-fn</code>] [-p <i>varname</i>] [<i>id ...</i>]</dt>
<dd> <p> Wait for each specified child process and return its termination status. Each <i>id</i> may be a process ID or a job specification; if a job spec is given, all processes in that job&#8217;s pipeline are waited for. If <i>id</i> is not given, <code>wait</code> waits for all running background jobs and the last-executed process substitution, if its process id is the same as <code>$!</code>, and the return status is zero. If the <code>-n</code> option is supplied, <code>wait</code> waits for a single job from the list of <i>id</i>s or, if no <i>id</i>s are supplied, any job, to complete and returns its exit status. If none of the supplied arguments is a child of the shell, or if no arguments are supplied and the shell has no unwaited-for children, the exit status is 127. If the <code>-p</code> option is supplied, the process or job identifier of the job for which the exit status is returned is assigned to the variable <i>varname</i> named by the option argument. The variable will be unset initially, before any assignment. This is useful only when the <code>-n</code> option is supplied. Supplying the <code>-f</code> option, when job control is enabled, forces <code>wait</code> to wait for <i>id</i> to terminate before returning its status, instead of returning when it changes status. If <i>id</i> specifies a non-existent process or job, the return status is 127. Otherwise, the return status is the exit status of the last process or job waited for. </p>
 </dd></dl>
<h2>SHELL COMPATIBILITY MODE</h2>
<p> Bash-4.0 introduced the concept of a `shell compatibility level&#8217;, specified as a set of options to the shopt builtin <code>compat31</code>, <code>compat32</code>, <code>compat40</code>, <code>compat41</code>, and so on). There is only one current compatibility level -- each option is mutually exclusive. The compatibility level is intended to allow users to select behavior from previous versions that is incompatible with newer versions while they migrate scripts to use current features and behavior. It&#8217;s intended to be a temporary solution. </p>
<p> This section does not mention behavior that is standard for a particular version (e.g., setting <code>compat32</code> means that quoting the rhs of the regexp matching operator quotes special regexp characters in the word, which is default behavior in bash-3.2 and above). </p>
<p> If a user enables, say, <code>compat32</code>, it may affect the behavior of other compatibility levels up to and including the current compatibility level. The idea is that each compatibility level controls behavior that changed in that version of <code>bash</code>, but that behavior may have been present in earlier versions. For instance, the change to use locale-based comparisons with the <code>[[</code> command came in bash-4.1, and earlier versions used ASCII-based comparisons, so enabling <code>compat32</code> will enable ASCII-based comparisons as well. That granularity may not be sufficient for all uses, and as a result users should employ compatibility levels carefully. Read the documentation for a particular feature to find out the current behavior. </p>
<p> Bash-4.3 introduced a new shell variable: <font SIZE="-1"><code>BASH_COMPAT</code>. </font> The value assigned to this variable (a decimal version number like 4.2, or an integer corresponding to the <code>compat</code><i>NN</i> option, like 42) determines the compatibility level. </p>
<p> Starting with bash-4.4, Bash has begun deprecating older compatibility levels. Eventually, the options will be removed in favor of <font SIZE="-1"><code>BASH_COMPAT</code>. </font> </p>
<p> Bash-5.0 is the final version for which there will be an individual shopt option for the previous version. Users should use <font SIZE="-1"><code>BASH_COMPAT</code> </font> on bash-5.0 and later versions. </p>
<p> The following table describes the behavior changes controlled by each compatibility level setting. The <code>compat</code><i>NN</i> tag is used as shorthand for setting the compatibility level to <i>NN</i> using one of the following mechanisms. For versions prior to bash-5.0, the compatibility level may be set using the corresponding <code>compat</code><i>NN</i> shopt option. For bash-4.3 and later versions, the <font SIZE="-1"><code>BASH_COMPAT</code> </font> variable is preferred, and it is required for bash-5.1 and later versions. </p>
<dl>
<dt><code>compat31</code></dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> quoting the rhs of the <code>[[</code> command&#8217;s regexp matching operator (=~) has no special effect </p>
 </dd></dl>
</dl>
<dt><code>compat32</code></dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> interrupting a command list such as &quot;a ; b ; c&quot; causes the execution of the next command in the list (in bash-4.0 and later versions, the shell acts as if it received the interrupt, so interrupting one command in a list aborts the execution of the entire list) </p>
 </dd></dl>
</dl>
<dt><code>compat40</code></dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> the <code>&lt;</code> and <code>&gt;</code> operators to the <code>[[</code> command do not consider the current locale when comparing strings; they use ASCII ordering. Bash versions prior to bash-4.1 use ASCII collation and <i><a href="/docs/linux/man/3-strcmp/">strcmp</a></i>(3); bash-4.1 and later use the current locale&#8217;s collation sequence and <i><a href="/docs/linux/man/3-strcoll/">strcoll</a></i>(3). </p>
 </dd></dl>
</dl>
<dt><code>compat41</code></dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> in <i>posix</i> mode, <code>time</code> may be followed by options and still be recognized as a reserved word (this is POSIX interpretation 267) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> in <i>posix</i> mode, the parser requires that an even number of single quotes occur in the <i>word</i> portion of a double-quoted parameter expansion and treats them specially, so that characters within the single quotes are considered quoted (this is POSIX interpretation 221) </p>
 </dd></dl>
</dl>
<dt><code>compat42</code></dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> the replacement string in double-quoted pattern substitution does not undergo quote removal, as it does in versions after bash-4.2 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> in posix mode, single quotes are considered special when expanding the <i>word</i> portion of a double-quoted parameter expansion and can be used to quote a closing brace or other special character (this is part of POSIX interpretation 221); in later versions, single quotes are not special within double-quoted word expansions </p>
 </dd></dl>
</dl>
<dt><code>compat43</code></dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> the shell does not print a warning message if an attempt is made to use a quoted compound assignment as an argument to declare (declare -a foo=&#8216;(1 2)&#8216;). Later versions warn that this usage is deprecated </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> word expansion errors are considered non-fatal errors that cause the current command to fail, even in posix mode (the default behavior is to make them fatal errors that cause the shell to exit) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> when executing a shell function, the loop state (while/until/etc.) is not reset, so <code>break</code> or <code>continue</code> in that function will break or continue loops in the calling context. Bash-4.4 and later reset the loop state to prevent this </p>
 </dd></dl>
</dl>
<dt><code>compat44</code></dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> the shell sets up the values used by <font SIZE="-1"><code>BASH_ARGV</code> </font> and <font SIZE="-1"><code>BASH_ARGC</code> </font> so they can expand to the shell&#8217;s positional parameters even if extended debugging mode is not enabled </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> a subshell inherits loops from its parent context, so <code>break</code> or <code>continue</code> will cause the subshell to exit. Bash-5.0 and later reset the loop state to prevent the exit </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> variable assignments preceding builtins like <code>export</code> and <code>readonly</code> that set attributes continue to affect variables with the same name in the calling environment even if the shell is not in posix mode </p>
 </dd></dl>
</dl>
<dt><code>compat50</code></dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Bash-5.1 changed the way <font SIZE="-1"><code>$RANDOM</code> </font> is generated to introduce slightly more randomness. If the shell compatibility level is set to 50 or lower, it reverts to the method from bash-5.0 and previous versions, so seeding the random number generator by assigning a value to <font SIZE="-1"><code>RANDOM</code> </font> will produce the same sequence as in bash-5.0 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If the command hash table is empty, bash versions prior to bash-5.1 printed an informational message to that effect, even when producing output that can be reused as input. Bash-5.1 suppresses that message when the <code>-l</code> option is supplied. </p>
 </dd></dl>
</dl>
</dl>
<h2>RESTRICTED SHELL</h2>
<p> If <code>bash</code> is started with the name <code>rbash</code>, or the <code>-r</code> option is supplied at invocation, the shell becomes restricted. A restricted shell is used to set up an environment more controlled than the standard shell. It behaves identically to <code>bash</code> with the exception that the following are disallowed or not performed: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> changing directories with <code>cd</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> setting or unsetting the values of <font SIZE="-1"><code>SHELL</code>, </font> <font SIZE="-1"><code>PATH</code>, </font> <font SIZE="-1"><code>HISTFILE</code>, </font> <font SIZE="-1"><code>ENV</code>, </font> or <font SIZE="-1"><code>BASH_ENV</code> </font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> specifying command names containing <code>/</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> specifying a filename containing a <code>/</code> as an argument to the <code>.</code> builtin command </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> specifying a filename containing a slash as an argument to the <code>history</code> builtin command </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> specifying a filename containing a slash as an argument to the <code>-p</code> option to the <code>hash</code> builtin command </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> importing function definitions from the shell environment at startup </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> parsing the value of <font SIZE="-1"><code>SHELLOPTS</code> </font> from the shell environment at startup </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> redirecting output using the &gt;, &gt;|, &lt;&gt;, &gt;&amp;, &amp;&gt;, and &gt;&gt; redirection operators </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> using the <code>exec</code> builtin command to replace the shell with another command </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> adding or deleting builtin commands with the <code>-f</code> and <code>-d</code> options to the <code>enable</code> builtin command </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> using the <code>enable</code> builtin command to enable disabled shell builtins </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> specifying the <code>-p</code> option to the <code>command</code> builtin command </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> turning off restricted mode with <code>set +r</code> or <code>set +o restricted</code>. </p>
 </dd></dl>
<p> These restrictions are enforced after any startup files are read. </p>
<p> When a command that is found to be a shell script is executed (see <font SIZE="-1"><code>COMMAND EXECUTION</code> </font> above), <code>rbash</code> turns off any restrictions in the shell spawned to execute the script.  </p>
<h2>SEE ALSO</h2>
<dl>
<dt><i>Bash Reference Manual</i>, Brian Fox and Chet Ramey</dt>
<dd>  </dd>
<dt><i>The Gnu Readline Library</i>, Brian Fox and Chet Ramey</dt>
<dd>  </dd>
<dt><i>The Gnu History Library</i>, Brian Fox and Chet Ramey</dt>
<dd>  </dd>
<dt><i>Portable Operating System Interface (POSIX) Part 2: Shell and Utilities</i>, IEEE --</dt>
<dd> <p> <a rel="nofollow" href="http://pubs.opengroup.org/onlinepubs/9699919799/">http://pubs.opengroup.org/onlinepubs/9699919799/</a> </p>
 </dd>
<dt><a rel="nofollow" href="http://tiswww.case.edu/~chet/bash/POSIX">http://tiswww.case.edu/~chet/bash/POSIX</a> -- a description of posix mode</dt>
<dd>  </dd>
<dt><i><a href="/docs/linux/man/1-sh/">sh</a></i>(1), <i>ksh</i>(1), <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1)</dt>
<dd>  </dd>
<dt><i><a href="/docs/linux/man/1-emacs/">emacs</a></i>(1), <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1)</dt>
<dd>  </dd>
<dt><i><a href="/docs/linux/man/3-readline/">readline</a></i>(3)</dt>
<dd>  </dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>/bin/bash</i></dt>
<dd> <p> The <code>bash</code> executable </p>
 </dd>
<dt><i>/etc/profile</i></dt>
<dd> <p> The systemwide initialization file, executed for login shells </p>
 </dd>
<dt><i>/etc/bash.bashrc</i></dt>
<dd> <p> The systemwide per-interactive-shell startup file </p>
 </dd>
<dt><i>/etc/bash.bash.logout</i></dt>
<dd> <p> The systemwide login shell cleanup file, executed when a login shell exits </p>
 </dd>
<dt><i>~/.bash_profile</i></dt>
<dd> <p> The personal initialization file, executed for login shells </p>
 </dd>
<dt><i>~/.bashrc</i></dt>
<dd> <p> The individual per-interactive-shell startup file </p>
 </dd>
<dt><i>~/.bash_logout</i></dt>
<dd> <p> The individual login shell cleanup file, executed when a login shell exits </p>
 </dd>
<dt><i>~/.inputrc</i></dt>
<dd> <p> Individual <i>readline</i> initialization file </p>
 </dd></dl>
<h2>AUTHORS</h2>
<p> Brian Fox, Free Software Foundation <br />
 bfox [at] gnu.org </p>
<p> Chet Ramey, Case Western Reserve University <br />
 chet.ramey [at] case.edu  </p>
<h2>BUG REPORTS</h2>
<p> If you find a bug in <code>bash,</code> you should report it. But first, you should make sure that it really is a bug, and that it appears in the latest version of <code>bash</code>. The latest version is always available from <i><a href="ftp://ftp.gnu.org/pub/gnu/bash/">ftp://ftp.gnu.org/pub/gnu/bash/</a></i>. </p>
<p> Once you have determined that a bug actually exists, use the <i>bashbug</i> command to submit a bug report. If you have a fix, you are encouraged to mail that as well! Suggestions and `philosophical&#8217; bug reports may be mailed to <i>bug-bash [at] gnu.org</i> or posted to the Usenet newsgroup <code>gnu.bash.bug</code>. </p>
<p> ALL bug reports should include: </p>
<dl>
<dt>The version number of <code>bash</code></dt>
<dd>  </dd>
<dt>The hardware and operating system</dt>
<dd>  </dd>
<dt>The compiler used to compile</dt>
<dd>  </dd>
<dt>A description of the bug behaviour</dt>
<dd>  </dd>
<dt>A short script or `recipe&#8217; which exercises the bug</dt>
<dd>  </dd></dl>
<p> <i>bashbug</i> inserts the first three items automatically into the template it provides for filing a bug report. </p>
<p> Comments and bug reports concerning this manual page should be directed to <i>chet.ramey [at] case.edu</i>.  </p>
<h2>BUGS</h2>
<p> It&#8217;s too big and too slow. </p>
<p> There are some subtle differences between <code>bash</code> and traditional versions of <code>sh</code>, mostly because of the <font SIZE="-1"><code>POSIX</code> </font> specification. </p>
<p> Aliases are confusing in some uses. </p>
<p> Shell builtin commands and functions are not stoppable/restartable. </p>
<p> Compound commands and command sequences of the form `a ; b ; c&#8217; are not handled gracefully when process suspension is attempted. When a process is stopped, the shell immediately executes the next command in the sequence. It suffices to place the sequence of commands between parentheses to force it into a subshell, which may be stopped as a unit. </p>
<p> Array variables may not (yet) be exported. </p>
<p> There may be only one active coprocess at a time. </p>
