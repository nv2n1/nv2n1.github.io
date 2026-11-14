---
title: "zshmisc(1)"
name: "zshmisc"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zshmisc/"
description: "zshmisc – everything and then some"
---

<h2 class="name">NAME</h2>
<p> zshmisc &#8211; everything and then some </p>
<h2>SIMPLE COMMANDS &amp; PIPELINES</h2>
<p> A <i>simple command</i> is a sequence of optional parameter assignments followed by blank-separated words, with optional redirections interspersed. For a description of assignment, see the beginning of <i><a href="/docs/linux/man/1-zshparam/">zshparam</a></i>(1). </p>
<p> The first word is the command to be executed, and the remaining words, if any, are arguments to the command. If a command name is given, the parameter assignments modify the environment of the command when it is executed. The value of a simple command is its exit status, or 128 plus the signal number if terminated by a signal. For example, </p>
<dl>
<dt>
<dd>
<pre>
<code>echo foo</code>
</pre>
</dl>
<p> is a simple command with arguments. </p>
<p> A <i>pipeline</i> is either a simple command, or a sequence of two or more simple commands where each command is separated from the next by `<code>|</code>&#8216; or `<code>|&amp;</code>&#8216;. Where commands are separated by `<code>|</code>&#8216;, the standard output of the first command is connected to the standard input of the next. `<code>|&amp;</code>&#8216; is shorthand for `<code>2&gt;&amp;1 |</code>&#8216;, which connects both the standard output and the standard error of the command to the standard input of the next. The value of a pipeline is the value of the last command, unless the pipeline is preceded by `<code>!</code>&#8216; in which case the value is the logical inverse of the value of the last command. For example, </p>
<dl>
<dt>
<dd>
<pre>
<code>echo foo | sed 's/foo/bar/'</code>
</pre>
</dl>
<p> is a pipeline, where the output (`<code>foo</code>&#8216; plus a newline) of the first command will be passed to the input of the second. </p>
<p> If a pipeline is preceded by `<code>coproc</code>&#8216;, it is executed as a coprocess; a two-way pipe is established between it and the parent shell. The shell can read from or write to the coprocess by means of the `<code>&gt;&amp;p</code>&#8216; and `<code>&lt;&amp;p</code>&#8216; redirection operators or with `<code>print -p</code>&#8216; and `<code>read -p</code>&#8216;. A pipeline cannot be preceded by both `<code>coproc</code>&#8216; and `<code>!</code>&#8216;. If job control is active, the coprocess can be treated in other than input and output as an ordinary background job. </p>
<p> A <i>sublist</i> is either a single pipeline, or a sequence of two or more pipelines separated by `<code>&amp;&amp;</code>&#8216; or `<code>||</code>&#8216;. If two pipelines are separated by `<code>&amp;&amp;</code>&#8216;, the second pipeline is executed only if the first succeeds (returns a zero status). If two pipelines are separated by `<code>||</code>&#8216;, the second is executed only if the first fails (returns a nonzero status). Both operators have equal precedence and are left associative. The value of the sublist is the value of the last pipeline executed. For example, </p>
<dl>
<dt>
<dd>
<pre>
<code>dmesg | grep panic &amp;&amp; print yes</code>
</pre>
</dl>
<p> is a sublist consisting of two pipelines, the second just a simple command which will be executed if and only if the <code>grep</code> command returns a zero status. If it does not, the value of the sublist is that return status, else it is the status returned by the <code>print</code> (almost certainly zero). </p>
<p> A <i>list</i> is a sequence of zero or more sublists, in which each sublist is terminated by `<code>;</code>&#8216;, `<code>&amp;</code>&#8216;, `<code>&amp;|</code>&#8216;, `<code>&amp;!</code>&#8216;, or a newline. This terminator may optionally be omitted from the last sublist in the list when the list appears as a complex command inside `<code>(</code>&#8230;<code>)</code>&#8216; or `<code>{</code>&#8230;<code>}</code>&#8216;. When a sublist is terminated by `<code>;</code>&#8216; or newline, the shell waits for it to finish before executing the next sublist. If a sublist is terminated by a `<code>&amp;</code>&#8216;, `<code>&amp;|</code>&#8216;, or `<code>&amp;!</code>&#8216;, the shell executes the last pipeline in it in the background, and does not wait for it to finish (note the difference from other shells which execute the whole sublist in the background). A backgrounded pipeline returns a status of zero. </p>
<p> More generally, a list can be seen as a set of any shell commands whatsoever, including the complex commands below; this is implied wherever the word `list&#8217; appears in later descriptions. For example, the commands in a shell function form a special sort of list.</p>
<h2>PRECOMMAND MODIFIERS</h2>
<p> A simple command may be preceded by a <i>precommand modifier</i>, which will alter how the command is interpreted. These modifiers are shell builtin commands with the exception of <code>nocorrect</code> which is a reserved word. </p>
<dl>
<dt>
<dd> <code>&#8211;</code> The command is executed with a `<code>&#8211;</code>&#8216; prepended to its <code>argv[0]</code> string.</p>
<dt><code>builtin</code></p>
<dd> The command word is taken to be the name of a builtin command, rather than a shell function or external command.</p>
<dt><code>command</code> [ <code>-pvV</code> ]</p>
<dd> The command word is taken to be the name of an external command, rather than a shell function or builtin. If the <code>POSIX_BUILTINS</code> option is set, builtins will also be executed but certain special properties of them are suppressed. The <code>-p</code> flag causes a default path to be searched instead of that in <code>$path</code>. With the <code>-v</code> flag, <code>command</code> is similar to <code>whence</code> and with <code>-V</code>, it is equivalent to <code>whence -v</code>.</p>
<dt><code>exec</code> [ <code>-cl</code> ] [ <code>-a</code> <i>argv0</i> ]</p>
<dd> The following command together with any arguments is run in place of the current process, rather than as a sub-process. The shell does not fork and is replaced. The shell does not invoke <code>TRAPEXIT</code>, nor does it source <code>zlogout</code> files. The options are provided for compatibility with other shells.</p>
<dl>
<dt>
<dd>
<p> The <code>-c</code> option clears the environment. </p>
<p> The <code>-l</code> option is equivalent to the <code>&#8211;</code> precommand modifier, to treat the replacement command as a login shell; the command is executed with a <code>&#8211;</code> prepended to its <code>argv[0]</code> string. This flag has no effect if used together with the <code>-a</code> option. </p>
<p> The <code>-a</code> option is used to specify explicitly the <code>argv[0]</code> string (the name of the command as seen by the process itself) to be used by the replacement command and is directly equivalent to setting a value for the <code>ARGV0</code> environment variable.</dl>
<dt><code>nocorrect</code></p>
<dd> Spelling correction is not done on any of the words. This must appear before any other precommand modifier, as it is interpreted immediately, before any parsing is done. It has no effect in non-interactive shells.</p>
<dt><code>noglob</code></p>
<dd> Filename generation (globbing) is not performed on any of the words.</dl>
<h2>COMPLEX COMMANDS</h2>
<p> A <i>complex command</i> in zsh is one of the following: </p>
<dl>
<dt>
<dd> <code>if</code> <i>list</i> <code>then</code> <i>list</i> [ <code>elif</code> <i>list</i> <code>then</code> <i>list</i> ] &#8230; [ <code>else</code> <i>list</i> ] <code>fi</code> The <code>if</code> <i>list</i> is executed, and if it returns a zero exit status, the <code>then</code> <i>list</i> is executed. Otherwise, the <code>elif</code> <i>list</i> is executed and if its status is zero, the <code>then</code> <i>list</i> is executed. If each <code>elif</code> <i>list</i> returns nonzero status, the <code>else</code> <i>list</i> is executed.</p>
<dt><code>for</code> <i>name</i> &#8230; [ <code>in</code> <i>word</i> &#8230; ] <i>term</i> <code>do</code> <i>list</i> <code>done</code></p>
<dd> Expand the list of <i>word</i>s, and set the parameter <i>name</i> to each of them in turn, executing <i>list</i> each time. If the `<code>in</code> <i>word</i>&#8216; is omitted, use the positional parameters instead of the <i>word</i>s.</p>
<dl>
<dt>
<dd>
<p> The <i>term</i> consists of one or more newline or <code>;</code> which terminate the <i>word</i>s, and are optional when the `<code>in</code> <i>word</i>&#8216; is omitted. </p>
<p> More than one parameter <i>name</i> can appear before the list of <i>word</i>s. If <i>N</i> <i>name</i>s are given, then on each execution of the loop the next <i>N</i> <i>word</i>s are assigned to the corresponding parameters. If there are more <i>name</i>s than remaining <i>word</i>s, the remaining parameters are each set to the empty string. Execution of the loop ends when there is no remaining <i>word</i> to assign to the first <i>name</i>. It is only possible for <code>in</code> to appear as the first <i>name</i> in the list, else it will be treated as marking the end of the list.</dl>
<dt><code>for ((</code> [<i>expr1</i>] <code>;</code> [<i>expr2</i>] <code>;</code> [<i>expr3</i>] <code>)) do</code> <i>list</i> <code>done</code></p>
<dd> The arithmetic expression <i>expr1</i> is evaluated first (see the section `Arithmetic Evaluation&#8217;). The arithmetic expression <i>expr2</i> is repeatedly evaluated until it evaluates to zero and when non-zero, <i>list</i> is executed and the arithmetic expression <i>expr3</i> evaluated. If any expression is omitted, then it behaves as if it evaluated to 1.</p>
<dt><code>while</code> <i>list</i> <code>do</code> <i>list</i> <code>done</code></p>
<dd> Execute the <code>do</code> <i>list</i> as long as the <code>while</code> <i>list</i> returns a zero exit status.</p>
<dt><code>until</code> <i>list</i> <code>do</code> <i>list</i> <code>done</code></p>
<dd> Execute the <code>do</code> <i>list</i> as long as <code>until</code> <i>list</i> returns a nonzero exit status.</p>
<dt><code>repeat</code> <i>word</i> <code>do</code> <i>list</i> <code>done</code></p>
<dd> <i>word</i> is expanded and treated as an arithmetic expression, which must evaluate to a number <i>n</i>. <i>list</i> is then executed <i>n</i> times.</p>
<dl>
<dt>
<dd>
<p> The <code>repeat</code> syntax is disabled by default when the shell starts in a mode emulating another shell. It can be enabled with the command `<code>enable -r repeat</code>&#8216;</dl>
<dt><code>case</code> <i>word</i> <code>in</code> [ [<code>(</code>] <i>pattern</i> [ <code>|</code> <i>pattern</i> ] &#8230; <code>)</code> <i>list</i> (<code>;;</code>|<code>;&amp;</code>|<code>;|</code>) ] &#8230; <code>esac</code></p>
<dd> Execute the <i>list</i> associated with the first <i>pattern</i> that matches <i>word</i>, if any. The form of the patterns is the same as that used for filename generation. See the section `Filename Generation&#8217;.</p>
<dl>
<dt>
<dd>
<p> Note further that, unless the <code>SH_GLOB</code> option is set, the whole pattern with alternatives is treated by the shell as equivalent to a group of patterns within parentheses, although white space may appear about the parentheses and the vertical bar and will be stripped from the pattern at those points. White space may appear elsewhere in the pattern; this is not stripped. If the <code>SH_GLOB</code> option is set, so that an opening parenthesis can be unambiguously treated as part of the case syntax, the expression is parsed into separate words and these are treated as strict alternatives (as in other shells). </p>
<p> If the <i>list</i> that is executed is terminated with <code>;&amp;</code> rather than <code>;;</code>, the following list is also executed. The rule for the terminator of the following list <code>;;</code>, <code>;&amp;</code> or <code>;|</code> is applied unless the <code>esac</code> is reached. </p>
<p> If the <i>list</i> that is executed is terminated with <code>;|</code> the shell continues to scan the <i>pattern</i>s looking for the next match, executing the corresponding <i>list</i>, and applying the rule for the corresponding terminator <code>;;</code>, <code>;&amp;</code> or <code>;|</code>. Note that <i>word</i> is not re-expanded; all applicable <i>pattern</i>s are tested with the same <i>word</i>.</dl>
<dt><code>select</code> <i>name</i> [ <code>in</code> <i>word</i> &#8230; <i>term</i> ] <code>do</code> <i>list</i> <code>done</code></p>
<dd> where <i>term</i> is one or more newline or <code>;</code> to terminate the <i>word</i>s. Print the set of <i>word</i>s, each preceded by a number. If the <code>in</code> <i>word</i> is omitted, use the positional parameters. The <code>PROMPT3</code> prompt is printed and a line is read from the line editor if the shell is interactive and that is active, or else standard input. If this line consists of the number of one of the listed <i>word</i>s, then the parameter <i>name</i> is set to the <i>word</i> corresponding to this number. If this line is empty, the selection list is printed again. Otherwise, the value of the parameter <i>name</i> is set to null. The contents of the line read from standard input is saved in the parameter <code>REPLY</code>. <i>list</i> is executed for each selection until a break or end-of-file is encountered.</p>
<dt><code>(</code> <i>list</i> <code>)</code></p>
<dd> Execute <i>list</i> in a subshell. Traps set by the <code>trap</code> builtin are reset to their default values while executing <i>list</i>.</p>
<dt><code>{</code> <i>list</i> <code>}</code></p>
<dd> Execute <i>list</i>.</p>
<dt><code>{</code> <i>try-list</i> <code>} always {</code> <i>always-list</i> <code>}</code></p>
<dd> First execute <i>try-list</i>. Regardless of errors, or <code>break</code> or <code>continue</code> commands encountered within <i>try-list</i>, execute <i>always-list</i>. Execution then continues from the result of the execution of <i>try-list</i>; in other words, any error, or <code>break</code> or <code>continue</code> command is treated in the normal way, as if <i>always-list</i> were not present. The two chunks of code are referred to as the `try block&#8217; and the `always block&#8217;.</p>
<dl>
<dt>
<dd>
<p> Optional newlines or semicolons may appear after the <code>always</code>; note, however, that they may <i>not</i> appear between the preceding closing brace and the <code>always</code>. </p>
<p> An `error&#8217; in this context is a condition such as a syntax error which causes the shell to abort execution of the current function, script, or list. Syntax errors encountered while the shell is parsing the code do not cause the <i>always-list</i> to be executed. For example, an erroneously constructed <code>if</code> block in <i>try-list</i> would cause the shell to abort during parsing, so that <i>always-list</i> would not be executed, while an erroneous substitution such as <code>${*foo*}</code> would cause a run-time error, after which <i>always-list</i> would be executed. </p>
<p> An error condition can be tested and reset with the special integer variable <code>TRY_BLOCK_ERROR</code>. Outside an <i>always-list</i> the value is irrelevant, but it is initialised to <code>-1</code>. Inside <i>always-list</i>, the value is 1 if an error occurred in the <i>try-list</i>, else 0. If <code>TRY_BLOCK_ERROR</code> is set to 0 during the <i>always-list</i>, the error condition caused by the <i>try-list</i> is reset, and shell execution continues normally after the end of <i>always-list</i>. Altering the value during the <i>try-list</i> is not useful (unless this forms part of an enclosing <code>always</code> block). </p>
<p> Regardless of <code>TRY_BLOCK_ERROR</code>, after the end of <i>always-list</i> the normal shell status <code>$?</code> is the value returned from <i>try-list</i>. This will be non-zero if there was an error, even if <code>TRY_BLOCK_ERROR</code> was set to zero. </p>
<p> The following executes the given code, ignoring any errors it causes. This is an alternative to the usual convention of protecting code by executing it in a subshell. </p>
<dl>
<dt>
<dd>
<pre><code>
{
#code which may cause an error
} always
{
#This code is executed regardless of the error.
    ((TRY_BLOCK_ERROR = 0))
}
#The error condition has been reset.
</code></pre>
</dl>
<p> When a <code>try</code> block occurs outside of any function, a <code>return</code> or a <code>exit</code> encountered in <i>try-list</i> does <i>not</i> cause the execution of <i>always-list</i>. Instead, the shell exits immediately after any <code>EXIT</code> trap has been executed. Otherwise, a <code>return</code> command encountered in <i>try-list</i> will cause the execution of <i>always-list</i>, just like <code>break</code> and <code>continue</code>. </p>
</dl>
<dt>
<dd> <code>function</code> <i>word</i> &#8230; [ <code>()</code> ] [ <i>term</i> ] <code>{</code> <i>list</i> <code>}</code></p>
<dt>
<dd> <i>word</i> &#8230; <code>()</code> [ <i>term</i> ] <code>{</code> <i>list</i> <code>}</code></p>
<dt>
<dd> <i>word</i> &#8230; <code>()</code> [ <i>term</i> ] <i>command</i> where <i>term</i> is one or more newline or <code>;</code>. Define a function which is referenced by any one of <i>word</i>. Normally, only one <i>word</i> is provided; multiple <i>word</i>s are usually only useful for setting traps. The body of the function is the <i>list</i> between the <code>{</code> and <code>}</code>. See the section `Functions&#8217;.</p>
<dl>
<dt>
<dd>
<p> If the option <code>SH_GLOB</code> is set for compatibility with other shells, then whitespace may appear between the left and right parentheses when there is a single <i>word</i>; otherwise, the parentheses will be treated as forming a globbing pattern in that case. </p>
<p> In any of the forms above, a redirection may appear outside the function body, for example </p>
<dl>
<dt>
<dd>
<pre>
<code>func() { ... } 2&gt;&amp;1</code>
</pre>
</dl>
<p> The redirection is stored with the function and applied whenever the function is executed. Any variables in the redirection are expanded at the point the function is executed, but outside the function scope.</dl>
<dt><code>time</code> [ <i>pipeline</i> ]</p>
<dd> The <i>pipeline</i> is executed, and timing statistics are reported on the standard error in the form specified by the <code>TIMEFMT</code> parameter. If <i>pipeline</i> is omitted, print statistics about the shell process and its children.</p>
<dt><code>[[</code> <i>exp</i> <code>]]</code></p>
<dd> Evaluates the conditional expression <i>exp</i> and return a zero exit status if it is true. See the section `Conditional Expressions&#8217; for a description of <i>exp</i>.</dl>
<h2>ALTERNATE FORMS FOR COMPLEX COMMANDS</h2>
<p> Many of zsh&#8217;s complex commands have alternate forms. These are non-standard and are likely not to be obvious even to seasoned shell programmers; they should not be used anywhere that portability of shell code is a concern. </p>
<p> The short versions below only work if <i>sublist</i> is of the form `<code>{</code> <i>list</i> <code>}</code>&#8216; or if the <code>SHORT_LOOPS</code> option is set. For the <code>if</code>, <code>while</code> and <code>until</code> commands, in both these cases the test part of the loop must also be suitably delimited, such as by `<code>[[</code> <i>&#8230;</i> <code>]]</code>&#8216; or `<code>((</code> <i>&#8230;</i> <code>))</code>&#8216;, else the end of the test will not be recognized. For the <code>for</code>, <code>repeat</code>, <code>case</code> and <code>select</code> commands no such special form for the arguments is necessary, but the other condition (the special form of <i>sublist</i> or use of the <code>SHORT_LOOPS</code> option) still applies. </p>
<dl>
<dt>
<dd> <code>if</code> <i>list</i> <code>{</code> <i>list</i> <code>}</code> [ <code>elif</code> <i>list</i> <code>{</code> <i>list</i> <code>}</code> ] &#8230; [ <code>else {</code> <i>list</i> <code>}</code> ] An alternate form of <code>if</code>. The rules mean that</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
if[[-o ignorebraces]] {<br />
    print yes<br />
}
</dl>
<p> works, but </p>
<dl>
<dt>
<dd>
<pre>
<code>if true {  # Does not work!
  print yes
}</code>
</pre>
</dl>
<p> does <i>not</i>, since the test is not suitably delimited.</dl>
<dt><code>if</code> <i>list</i> <i>sublist</i></p>
<dd> A short form of the alternate <code>if</code>. The same limitations on the form of <i>list</i> apply as for the previous form.</p>
<dt><code>for</code> <i>name</i> &#8230; <code>(</code> <i>word</i> &#8230; <code>)</code> <i>sublist</i></p>
<dd> A short form of <code>for</code>.</p>
<dt><code>for</code> <i>name</i> &#8230; [ <code>in</code> <i>word</i> &#8230; ] <i>term</i> <i>sublist</i></p>
<dd> where <i>term</i> is at least one newline or <code>;</code>. Another short form of <code>for</code>.</p>
<dt><code>for ((</code> [<i>expr1</i>] <code>;</code> [<i>expr2</i>] <code>;</code> [<i>expr3</i>] <code>))</code> <i>sublist</i></p>
<dd> A short form of the arithmetic <code>for</code> command.</p>
<dt><code>foreach</code> <i>name</i> &#8230; <code>(</code> <i>word</i> &#8230; <code>)</code> <i>list</i> <code>end</code></p>
<dd> Another form of <code>for</code>.</p>
<dt><code>while</code> <i>list</i> <code>{</code> <i>list</i> <code>}</code></p>
<dd> An alternative form of <code>while</code>. Note the limitations on the form of <i>list</i> mentioned above.</p>
<dt><code>until</code> <i>list</i> <code>{</code> <i>list</i> <code>}</code></p>
<dd> An alternative form of <code>until</code>. Note the limitations on the form of <i>list</i> mentioned above.</p>
<dt><code>repeat</code> <i>word</i> <i>sublist</i></p>
<dd> This is a short form of <code>repeat</code>.</p>
<dt><code>case</code> <i>word</i> <code>{</code> [ [<code>(</code>] <i>pattern</i> [ <code>|</code> <i>pattern</i> ] &#8230; <code>)</code> <i>list</i> (<code>;;</code>|<code>;&amp;</code>|<code>;|</code>) ] &#8230; <code>}</code></p>
<dd> An alternative form of <code>case</code>.</p>
<dt><code>select</code> <i>name</i> [ <code>in</code> <i>word</i> &#8230; <i>term</i> ] <i>sublist</i></p>
<dd> where <i>term</i> is at least one newline or <code>;</code>. A short form of <code>select</code>.</p>
<dt><code>function</code> <i>word</i> &#8230; [ <code>()</code> ] [ <i>term</i> ] <i>sublist</i></p>
<dd> This is a short form of <code>function</code>.</dl>
<h2>RESERVED WORDS</h2>
<p> The following words are recognized as reserved words when used as the first word of a command unless quoted or disabled using <code>disable -r</code>: </p>
<p> <code>do done esac then elif else fi for case if while function repeat time until select coproc nocorrect foreach end ! [[ { } declare export float integer local readonly typeset</code> </p>
<p> Additionally, `<code>}</code>&#8216; is recognized in any position if neither the <code>IGNORE_BRACES</code> option nor the <code>IGNORE_CLOSE_BRACES</code> option is set.</p>
<h2>ERRORS</h2>
<p> Certain errors are treated as fatal by the shell: in an interactive shell, they cause control to return to the command line, and in a non-interactive shell they cause the shell to be aborted. In older versions of zsh, a non-interactive shell running a script would not abort completely, but would resume execution at the next command to be read from the script, skipping the remainder of any functions or shell constructs such as loops or conditions; this somewhat illogical behaviour can be recovered by setting the option <code>CONTINUE_ON_ERROR</code>. </p>
<p> Fatal errors found in non-interactive shells include: </p>
<dl>
<dt>
<dd> &bull; Failure to parse shell options passed when invoking the shell</p>
<dt>&bull;</p>
<dd> Failure to change options with the <code>set</code> builtin</p>
<dt>&bull;</p>
<dd> Parse errors of all sorts, including failures to parse mathematical expressions</p>
<dt>&bull;</p>
<dd> Failures to set or modify variable behaviour with <code>typeset</code>, <code>local</code>, <code>declare</code>, <code>export</code>, <code>integer</code>, <code>float</code></p>
<dt>&bull;</p>
<dd> Execution of incorrectly positioned loop control structures (<code>continue</code>, <code>break</code>)</p>
<dt>&bull;</p>
<dd> Attempts to use regular expression with no regular expression module available</p>
<dt>&bull;</p>
<dd> Disallowed operations when the <code>RESTRICTED</code> options is set</p>
<dt>&bull;</p>
<dd> Failure to create a pipe needed for a pipeline</p>
<dt>&bull;</p>
<dd> Failure to create a multio</p>
<dt>&bull;</p>
<dd> Failure to autoload a module needed for a declared shell feature</p>
<dt>&bull;</p>
<dd> Errors creating command or process substitutions</p>
<dt>&bull;</p>
<dd> Syntax errors in glob qualifiers</p>
<dt>&bull;</p>
<dd> File generation errors where not caught by the option <code>BAD_PATTERN</code></p>
<dt>&bull;</p>
<dd> All bad patterns used for matching within case statements</p>
<dt>&bull;</p>
<dd> File generation failures where not caused by <code>NO_MATCH</code> or similar options</p>
<dt>&bull;</p>
<dd> All file generation errors where the pattern was used to create a multio</p>
<dt>&bull;</p>
<dd> Memory errors where detected by the shell</p>
<dt>&bull;</p>
<dd> Invalid subscripts to shell variables</p>
<dt>&bull;</p>
<dd> Attempts to assign read-only variables</p>
<dt>&bull;</p>
<dd> Logical errors with variables such as assignment to the wrong type</p>
<dt>&bull;</p>
<dd> Use of invalid variable names</p>
<dt>&bull;</p>
<dd> Errors in variable substitution syntax</p>
<dt>&bull;</p>
<dd> Failure to convert characters in <code>$&#8217;</code>&#8230;<code>&#8216;</code> expressions</dl>
<p> If the <code>POSIX_BUILTINS</code> option is set, more errors associated with shell builtin commands are treated as fatal, as specified by the POSIX standard. </p>
<h2>COMMENTS</h2>
<p> In non-interactive shells, or in interactive shells with the <code>INTERACTIVE_COMMENTS</code> option set, a word beginning with the third character of the <code>histchars</code> parameter (`<code>#</code>&#8216; by default) causes that word and all the following characters up to a newline to be ignored.</p>
<h2>ALIASING</h2>
<p> Every eligible <i>word</i> in the shell input is checked to see if there is an alias defined for it. If so, it is replaced by the text of the alias if it is in command position (if it could be the first word of a simple command), or if the alias is global. If the replacement text ends with a space, the next word in the shell input is always eligible for purposes of alias expansion. An alias is defined using the <code>alias</code> builtin; global aliases may be defined using the <code>-g</code> option to that builtin. </p>
<p> A <i>word</i> is defined as: </p>
<dl>
<dt>
<dd> &bull; Any plain string or glob pattern</p>
<dt>&bull;</p>
<dd> Any quoted string, using any quoting method (note that the quotes must be part of the alias definition for this to be eligible)</p>
<dt>&bull;</p>
<dd> Any parameter reference or command substitution</p>
<dt>&bull;</p>
<dd> Any series of the foregoing, concatenated without whitespace or other tokens between them</p>
<dt>&bull;</p>
<dd> Any reserved word (<code>case</code>, <code>do</code>, <code>else</code>, etc.)</p>
<dt>&bull;</p>
<dd> With global aliasing, any command separator, any redirection operator, and `<code>(</code>&#8216; or `<code>)</code>&#8216; when not part of a glob pattern</dl>
<p> Alias expansion is done on the shell input before any other expansion except history expansion. Therefore, if an alias is defined for the word <code>foo</code>, alias expansion may be avoided by quoting part of the word, e.g. <code>oo</code>. Any form of quoting works, although there is nothing to prevent an alias being defined for the quoted form such as <code>oo</code> as well. </p>
<p> When <code>POSIX_ALIASES</code> is set, only plain unquoted strings are eligible for aliasing. The <code>alias</code> builtin does not reject ineligible aliases, but they are not expanded. </p>
<p> For use with completion, which would remove an initial backslash followed by a character that isn&#8217;t special, it may be more convenient to quote the word by starting with a single quote, i.e. <code>&#8216;foo</code>; completion will automatically add the trailing single quote. </p>
<h3>Alias difficulties</h3>
<p> Although aliases can be used in ways that bend normal shell syntax, not every string of non-white-space characters can be used as an alias. </p>
<p> Any set of characters not listed as a word above is not a word, hence no attempt is made to expand it as an alias, no matter how it is defined (i.e. via the builtin or the special parameter <code>aliases</code> described in the section THE ZSH/PARAMETER MODULE in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1)). However, as noted in the case of <code>POSIX_ALIASES</code> above, the shell does not attempt to deduce whether the string corresponds to a word at the time the alias is created. </p>
<p> For example, an expression containing an <code>=</code> at the start of a command line is an assignment and cannot be expanded as an alias; a lone <code>=</code> is not an assignment but can only be set as an alias using the parameter, as otherwise the <code>=</code> is taken part of the syntax of the builtin command. </p>
<p> It is not presently possible to alias the `<code>((</code>&#8216; token that introduces arithmetic expressions, because until a full statement has been parsed, it cannot be distinguished from two consecutive `<code>(</code>&#8216; tokens introducing nested subshells. Also, if a separator such as <code>&amp;&amp;</code> is aliased, <code>\&amp;&amp;</code> turns into the two tokens <code>\&amp;</code> and <code>&amp;</code>, each of which may have been aliased separately. Similarly for <code>\&lt;&lt;</code>, <code>\&gt;|</code>, etc. </p>
<p> There is a commonly encountered problem with aliases illustrated by the following code: </p>
<dl>
<dt>
<dd>
<pre>
<code>alias echobar='echo bar'; echobar</code>
</pre>
</dl>
<p> This prints a message that the command <code>echobar</code> could not be found. This happens because aliases are expanded when the code is read in; the entire line is read in one go, so that when <code>echobar</code> is executed it is too late to expand the newly defined alias. This is often a problem in shell scripts, functions, and code executed with `<code>source</code>&#8216; or `<code>.</code>&#8216;. Consequently, use of functions rather than aliases is recommended in non-interactive code. </p>
<p> Note also the unhelpful interaction of aliases and function definitions: </p>
<dl>
<dt>
<dd>
<pre>
<code>alias func='noglob func'
func() {
    echo Do something with $*
}</code>
</pre>
</dl>
<p> Because aliases are expanded in function definitions, this causes the following command to be executed: </p>
<dl>
<dt>
<dd>
<pre>
<code>noglob func() {
    echo Do something with $*
}</code>
</pre>
</dl>
<p> which defines <code>noglob</code> as well as <code>func</code> as functions with the body given. To avoid this, either quote the name <code>func</code> or use the alternative function definition form `<code>function func</code>&#8216;. Ensuring the alias is defined after the function works but is problematic if the code fragment might be re-executed. </p>
<h2>QUOTING</h2>
<p> A character may be <i>quoted</i> (that is, made to stand for itself) by preceding it with a `<code>\</code>&#8216;. `<code>\</code>&#8216; followed by a newline is ignored. </p>
<p> A string enclosed between `<code>$&#8217;</code>&#8216; and `<code>&#8216;</code>&#8216; is processed the same way as the string arguments of the <code>print</code> builtin, and the resulting string is considered to be entirely quoted. A literal `<code>&#8216;</code>&#8216; character can be included in the string by using the `<code>\&#8217;</code>&#8216; escape. </p>
<p> All characters enclosed between a pair of single quotes (<code>&#8221;</code>) that is not preceded by a `<code>$</code>&#8216; are quoted. A single quote cannot appear within single quotes unless the option <code>RC_QUOTES</code> is set, in which case a pair of single quotes are turned into a single quote. For example, </p>
<dl>
<dt>
<dd>
<pre>
<code>print ''''</code>
</pre>
</dl>
<p> outputs nothing apart from a newline if <code>RC_QUOTES</code> is not set, but one single quote if it is set. </p>
<p> Inside double quotes (<code>&quot;&quot;</code>), parameter and command substitution occur, and `<code>\</code>&#8216; quotes the characters `<code>\</code>&#8216;, `<code>`</code>&#8216;, `<code>&quot;</code>&#8216;, `<code>$</code>&#8216;, and the first character of <code>$histchars</code> (default `<code>!</code>&#8216;).</p>
<h2>REDIRECTION</h2>
<p> If a command is followed by <code>&amp;</code> and job control is not active, then the default standard input for the command is the empty file <code>/dev/null</code>. Otherwise, the environment for the execution of a command contains the file descriptors of the invoking shell as modified by input/output specifications. </p>
<p> The following may appear anywhere in a simple command or may precede or follow a complex command. Expansion occurs before <i>word</i> or <i>digit</i> is used except as noted below. If the result of substitution on <i>word</i> produces more than one filename, redirection occurs for each separate filename in turn. </p>
<dl>
<dt>
<dd> <code>&lt;</code> <i>word</i> Open file <i>word</i> for reading as standard input. It is an error to open a file in this fashion if it does not exist.</p>
<dt><code>&lt;&gt;</code> <i>word</i></p>
<dd> Open file <i>word</i> for reading and writing as standard input. If the file does not exist then it is created.</p>
<dt><code>&gt;</code> <i>word</i></p>
<dd> Open file <i>word</i> for writing as standard output. If the file does not exist then it is created. If the file exists, and the <code>CLOBBER</code> option is unset, this causes an error; otherwise, it is truncated to zero length.</p>
<dt>
<dd> <code>&gt;|</code> <i>word</i></p>
<dt>
<dd> <code>&gt;!</code> <i>word</i> Same as <code>&gt;</code>, except that the file is truncated to zero length if it exists, regardless of <code>CLOBBER</code>.</p>
<dt><code>&gt;&gt;</code> <i>word</i></p>
<dd> Open file <i>word</i> for writing in append mode as standard output. If the file does not exist, and the <code>CLOBBER</code> and <code>APPEND_CREATE</code> options are both unset, this causes an error; otherwise, the file is created.</p>
<dt>
<dd> <code>&gt;&gt;|</code> <i>word</i></p>
<dt>
<dd> <code>&gt;&gt;!</code> <i>word</i> Same as <code>&gt;&gt;</code>, except that the file is created if it does not exist, regardless of <code>CLOBBER</code> and <code>APPEND_CREATE</code>.</p>
<dt><code>&lt;&lt;</code>[<code>&#8211;</code>] <i>word</i></p>
<dd> The shell input is read up to a line that is the same as <i>word</i>, or to an end-of-file. No parameter expansion, command substitution or filename generation is performed on <i>word</i>. The resulting document, called a <i>here-document</i>, becomes the standard input.</p>
<dl>
<dt>
<dd>
<p> If any character of <i>word</i> is quoted with single or double quotes or a `<code>\</code>&#8216;, no interpretation is placed upon the characters of the document. Otherwise, parameter and command substitution occurs, `<code>\</code>&#8216; followed by a newline is removed, and `<code>\</code>&#8216; must be used to quote the characters `<code>\</code>&#8216;, `<code>$</code>&#8216;, `<code>`</code>&#8216; and the first character of <i>word</i>. </p>
<p> Note that <i>word</i> itself does not undergo shell expansion. Backquotes in <i>word</i> do not have their usual effect; instead they behave similarly to double quotes, except that the backquotes themselves are passed through unchanged. (This information is given for completeness and it is not recommended that backquotes be used.) Quotes in the form <code>$&#8217;</code><i>&#8230;</i><code>&#8216;</code> have their standard effect of expanding backslashed references to special characters. </p>
<p> If <code>&lt;&lt;-</code> is used, then all leading tabs are stripped from <i>word</i> and from the document.</dl>
<dt><code>&lt;&lt;&lt;</code> <i>word</i></p>
<dd> Perform shell expansion on <i>word</i> and pass the result to standard input. This is known as a <i>here-string</i>. Compare the use of <i>word</i> in here-documents above, where <i>word</i> does not undergo shell expansion.</p>
<dt>
<dd> <code>&lt;&amp;</code> <i>number</i></p>
<dt>
<dd> <code>&gt;&amp;</code> <i>number</i> The standard input/output is duplicated from file descriptor <i>number</i> (see <i><a href="/docs/linux/man/2-dup2/">dup2</a></i>(2)).</p>
<dt>
<dd> <code>&lt;&amp; &#8211;</code></p>
<dt>
<dd> <code>&gt;&amp; &#8211;</code> Close the standard input/output.</p>
<dt>
<dd> <code>&lt;&amp; p</code></p>
<dt>
<dd> <code>&gt;&amp; p</code> The input/output from/to the coprocess is moved to the standard input/output.</p>
<dt>
<dd> <code>&gt;&amp;</code> <i>word</i></p>
<dt>
<dd> <code>&amp;&gt;</code> <i>word</i> (Except where `<code>&gt;&amp;</code> <i>word</i>&#8216; matches one of the above syntaxes; `<code>&amp;&gt;</code>&#8216; can always be used to avoid this ambiguity.) Redirects both standard output and standard error (file descriptor 2) in the manner of `<code>&gt;</code> <i>word</i>&#8216;. Note that this does <i>not</i> have the same effect as `<code>&gt;</code> <i>word</i> <code>2&gt;&amp;1</code>&#8216; in the presence of multios (see the section below).</p>
<dt>
<dd> <code>&gt;&amp;|</code> <i>word</i></p>
<dt>
<dd> <code>&gt;&amp;!</code> <i>word</i></p>
<dt>
<dd> <code>&amp;&gt;|</code> <i>word</i></p>
<dt>
<dd> <code>&amp;&gt;!</code> <i>word</i> Redirects both standard output and standard error (file descriptor 2) in the manner of `<code>&gt;|</code> <i>word</i>&#8216;.</p>
<dt>
<dd> <code>&gt;&gt;&amp;</code> <i>word</i></p>
<dt>
<dd> <code>&amp;&gt;&gt;</code> <i>word</i> Redirects both standard output and standard error (file descriptor 2) in the manner of `<code>&gt;&gt;</code> <i>word</i>&#8216;.</p>
<dt>
<dd> <code>&gt;&gt;&amp;|</code> <i>word</i></p>
<dt>
<dd> <code>&gt;&gt;&amp;!</code> <i>word</i></p>
<dt>
<dd> <code>&amp;&gt;&gt;|</code> <i>word</i></p>
<dt>
<dd> <code>&amp;&gt;&gt;!</code> <i>word</i> Redirects both standard output and standard error (file descriptor 2) in the manner of `<code>&gt;&gt;|</code> <i>word</i>&#8216;.</dl>
<p> If one of the above is preceded by a digit, then the file descriptor referred to is that specified by the digit instead of the default 0 or 1. The order in which redirections are specified is significant. The shell evaluates each redirection in terms of the (<i>file descriptor</i>, <i>file</i>) association at the time of evaluation. For example: </p>
<dl>
<dt>
<dd>
<pre>
... <code>1&gt;</code><i>fname</i> <code>2&gt;&amp;1</code>
</pre>
</dl>
<p> first associates file descriptor 1 with file <i>fname</i>. It then associates file descriptor 2 with the file associated with file descriptor 1 (that is, <i>fname</i>). If the order of redirections were reversed, file descriptor 2 would be associated with the terminal (assuming file descriptor 1 had been) and then file descriptor 1 would be associated with file <i>fname</i>. </p>
<p> The `<code>|&amp;</code>&#8216; command separator described in <i>Simple Commands &amp; Pipelines</i> in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1) is a shorthand for `<code>2&gt;&amp;1 |</code>&#8216;. </p>
<p> The various forms of process substitution, `<code>&lt;(</code><i>list</i><code>)</code>&#8216;, and `<code>=(</code><i>list</i><code>)</code>&#8216; for input and `<code>&gt;(</code><i>list</i><code>)</code>&#8216; for output, are often used together with redirection. For example, if <i>word</i> in an output redirection is of the form `<code>&gt;(</code><i>list</i><code>)</code>&#8216; then the output is piped to the command represented by <i>list</i>. See <i>Process Substitution</i> in <i><a href="/docs/linux/man/1-zshexpn/">zshexpn</a></i>(1).</p>
<h2>OPENING FILE DESCRIPTORS USING PARAMETERS</h2>
<p> When the shell is parsing arguments to a command, and the shell option <code>IGNORE_BRACES</code> is not set, a different form of redirection is allowed: instead of a digit before the operator there is a valid shell identifier enclosed in braces. The shell will open a new file descriptor that is guaranteed to be at least 10 and set the parameter named by the identifier to the file descriptor opened. No whitespace is allowed between the closing brace and the redirection character. For example: </p>
<dl>
<dt>
<dd>
<pre>
... <code>{myfd}&gt;&amp;1</code>
</pre>
</dl>
<p> This opens a new file descriptor that is a duplicate of file descriptor 1 and sets the parameter <code>myfd</code> to the number of the file descriptor, which will be at least 10. The new file descriptor can be written to using the syntax <code>&gt;&amp;$myfd</code>. The file descriptor remains open in subshells and forked external executables. </p>
<p> The syntax <code>{</code><i>varid</i><code>}&gt;&amp;-</code>, for example <code>{myfd}&gt;&amp;-</code>, may be used to close a file descriptor opened in this fashion. Note that the parameter given by <i>varid</i> must previously be set to a file descriptor in this case. </p>
<p> It is an error to open or close a file descriptor in this fashion when the parameter is readonly. However, it is not an error to read or write a file descriptor using <code>&lt;&amp;$</code><i>param</i> or <code>&gt;&amp;$</code><i>param</i> if <i>param</i> is readonly. </p>
<p> If the option <code>CLOBBER</code> is unset, it is an error to open a file descriptor using a parameter that is already set to an open file descriptor previously allocated by this mechanism. Unsetting the parameter before using it for allocating a file descriptor avoids the error. </p>
<p> Note that this mechanism merely allocates or closes a file descriptor; it does not perform any redirections from or to it. It is usually convenient to allocate a file descriptor prior to use as an argument to <code>exec</code>. The syntax does not in any case work when used around complex commands such as parenthesised subshells or loops, where the opening brace is interpreted as part of a command list to be executed in the current shell. </p>
<p> The following shows a typical sequence of allocation, use, and closing of a file descriptor: </p>
<dl>
<dt>
<dd>
integer myfd<br />
        exec{myfd} &gt; ~ / logs / mylogfile.txt print This is a log message.&gt;<br />
    &amp;$myfd<br />
        exec{myfd} &gt; &amp;-
</dl>
<p> Note that the expansion of the variable in the expression <code>&gt;&amp;$myfd</code> occurs at the point the redirection is opened. This is after the expansion of command arguments and after any redirections to the left on the command line have been processed.</p>
<h2>MULTIOS</h2>
<p> If the user tries to open a file descriptor for writing more than once, the shell opens the file descriptor as a pipe to a process that copies its input to all the specified outputs, similar to <code>tee</code>, provided the <code>MULTIOS</code> option is set, as it is by default. Thus: </p>
<dl>
<dt>
<dd>
<pre>
<code>date &gt;foo &gt;bar</code>
</pre>
</dl>
<p> writes the date to two files, named `<code>foo</code>&#8216; and `<code>bar</code>&#8216;. Note that a pipe is an implicit redirection; thus </p>
<dl>
<dt>
<dd>
<pre>
<code>date &gt;foo | cat</code>
</pre>
</dl>
<p> writes the date to the file `<code>foo</code>&#8216;, and also pipes it to cat. </p>
<p> Note that the shell opens all the files to be used in the multio process immediately, not at the point they are about to be written. </p>
<p> Note also that redirections are always expanded in order. This happens regardless of the setting of the <code>MULTIOS</code> option, but with the option in effect there are additional consequences. For example, the meaning of the expression <code>&gt;&amp;1</code> will change after a previous redirection: </p>
<dl>
<dt>
<dd>
<pre>
<code>date &gt;&amp;1 &gt;output</code>
</pre>
</dl>
<p> In the case above, the <code>&gt;&amp;1</code> refers to the standard output at the start of the line; the result is similar to the <code>tee</code> command. However, consider: </p>
<dl>
<dt>
<dd>
<pre>
<code>date &gt;output &gt;&amp;1</code>
</pre>
</dl>
<p> As redirections are evaluated in order, when the <code>&gt;&amp;1</code> is encountered the standard output is set to the file <code>output</code> and another copy of the output is therefore sent to that file. This is unlikely to be what is intended. </p>
<p> If the <code>MULTIOS</code> option is set, the word after a redirection operator is also subjected to filename generation (globbing). Thus </p>
<dl>
<dt>
<dd>
<pre>
<code>: &gt; *</code>
</pre>
</dl>
<p> will truncate all files in the current directory, assuming there&#8217;s at least one. (Without the <code>MULTIOS</code> option, it would create an empty file called `<code>*</code>&#8216;.) Similarly, you can do </p>
<dl>
<dt>
<dd>
<pre>
<code>echo exit 0 &gt;&gt; *.sh</code>
</pre>
</dl>
<p> If the user tries to open a file descriptor for reading more than once, the shell opens the file descriptor as a pipe to a process that copies all the specified inputs to its output in the order specified, provided the <code>MULTIOS</code> option is set. It should be noted that each file is opened immediately, not at the point where it is about to be read: this behaviour differs from <code>cat</code>, so if strictly standard behaviour is needed, <code>cat</code> should be used instead. </p>
<p> Thus </p>
<dl>
<dt>
<dd>
<pre>
<code>sort &lt;foo &lt;fubar</code>
</pre>
</dl>
<p> or even </p>
<dl>
<dt>
<dd>
<pre>
<code>sort &lt;f{oo,ubar}</code>
</pre>
</dl>
<p> is equivalent to `<code>cat foo fubar | sort</code>&#8216;. </p>
<p> Expansion of the redirection argument occurs at the point the redirection is opened, at the point described above for the expansion of the variable in <code>&gt;&amp;$myfd</code>. </p>
<p> Note that a pipe is an implicit redirection; thus </p>
<dl>
<dt>
<dd>
<pre>
<code>cat bar | sort &lt;foo</code>
</pre>
</dl>
<p> is equivalent to `<code>cat bar foo | sort</code>&#8216; (note the order of the inputs). </p>
<p> If the <code>MULTIOS</code> option is <i>un</i>set, each redirection replaces the previous redirection for that file descriptor. However, all files redirected to are actually opened, so </p>
<dl>
<dt>
<dd>
<pre>
<code>echo Hello &gt; bar &gt; baz</code>
</pre>
</dl>
<p> when <code>MULTIOS</code> is unset will truncate `<code>bar</code>&#8216;, and write `<code>Hello</code>&#8216; into `<code>baz</code>&#8216;. </p>
<p> There is a problem when an output multio is attached to an external program. A simple example shows this: </p>
<dl>
<dt>
<dd>
<pre>
<code>cat file &gt;file1 &gt;file2
cat file1 file2</code>
</pre>
</dl>
<p> Here, it is possible that the second `<code>cat</code>&#8216; will not display the full contents of <code>file1</code> and <code>file2</code> (i.e. the original contents of <code>file</code> repeated twice). </p>
<p> The reason for this is that the multios are spawned after the <code>cat</code> process is forked from the parent shell, so the parent shell does not wait for the multios to finish writing data. This means the command as shown can exit before <code>file1</code> and <code>file2</code> are completely written. As a workaround, it is possible to run the <code>cat</code> process as part of a job in the current shell: </p>
<dl>
<dt>
<dd>
<pre>
<code>{ cat file } &gt;file &gt;file2</code>
</pre>
</dl>
<p> Here, the <code>{</code><i>&#8230;</i><code>}</code> job will pause to wait for both files to be written. </p>
<h2>REDIRECTIONS WITH NO COMMAND</h2>
<p> When a simple command consists of one or more redirection operators and zero or more parameter assignments, but no command name, zsh can behave in several ways. </p>
<p> If the parameter <code>NULLCMD</code> is not set or the option <code>CSH_NULLCMD</code> is set, an error is caused. This is the <code>csh</code> behavior and <code>CSH_NULLCMD</code> is set by default when emulating <code>csh</code>. </p>
<p> If the option <code>SH_NULLCMD</code> is set, the builtin `<code>:</code>&#8216; is inserted as a command with the given redirections. This is the default when emulating <code>sh</code> or <code>ksh</code>. </p>
<p> Otherwise, if the parameter <code>NULLCMD</code> is set, its value will be used as a command with the given redirections. If both <code>NULLCMD</code> and <code>READNULLCMD</code> are set, then the value of the latter will be used instead of that of the former when the redirection is an input. The default for <code>NULLCMD</code> is `<code>cat</code>&#8216; and for <code>READNULLCMD</code> is `<code>more</code>&#8216;. Thus </p>
<dl>
<dt>
<dd>
<pre>
<code>&lt; file</code>
</pre>
</dl>
<p> shows the contents of <code>file</code> on standard output, with paging if that is a terminal. <code>NULLCMD</code> and <code>READNULLCMD</code> may refer to shell functions. </p>
<h2>COMMAND EXECUTION</h2>
<p> If a command name contains no slashes, the shell attempts to locate it. If there exists a shell function by that name, the function is invoked as described in the section `Functions&#8217;. If there exists a shell builtin by that name, the builtin is invoked. </p>
<p> Otherwise, the shell searches each element of <code>$path</code> for a directory containing an executable file by that name. If the search is unsuccessful, the shell prints an error message and returns a nonzero exit status. </p>
<p> If execution fails because the file is not in executable format, and the file is not a directory, it is assumed to be a shell script. <code>/bin/sh</code> is spawned to execute it. If the program is a file beginning with `<code>#!</code>&#8216;, the remainder of the first line specifies an interpreter for the program. The shell will execute the specified interpreter on operating systems that do not handle this executable format in the kernel. </p>
<p> If no external command is found but a function <code>command_not_found_handler</code> exists the shell executes this function with all command line arguments. The return status of the function becomes the status of the command. If the function wishes to mimic the behaviour of the shell when the command is not found, it should print the message `<code>command not found:</code> <i>cmd</i>&#8216; to standard error and return status 127. Note that the handler is executed in a subshell forked to execute an external command, hence changes to directories, shell parameters, etc. have no effect on the main shell. </p>
<h2>FUNCTIONS</h2>
<p> Shell functions are defined with the <code>function</code> reserved word or the special syntax `<i>funcname</i> <code>()</code>&#8216;. Shell functions are read in and stored internally. Alias names are resolved when the function is read. Functions are executed like commands with the arguments passed as positional parameters. (See the section `Command Execution&#8217;.) </p>
<p> Functions execute in the same process as the caller and share all files and present working directory with the caller. A trap on <code>EXIT</code> set inside a function is executed after the function completes in the environment of the caller. </p>
<p> The <code>return</code> builtin is used to return from function calls. </p>
<p> Function identifiers can be listed with the <code>functions</code> builtin. Functions can be undefined with the <code>unfunction</code> builtin.</p>
<h2>AUTOLOADING FUNCTIONS</h2>
<p> A function can be marked as <i>undefined</i> using the <code>autoload</code> builtin (or `<code>functions -u</code>&#8216; or `<code>typeset -fu</code>&#8216;). Such a function has no body. When the function is first executed, the shell searches for its definition using the elements of the <code>fpath</code> variable. Thus to define functions for autoloading, a typical sequence is: </p>
<dl>
<dt>
<dd>
<pre>
<code>fpath=(~/myfuncs $fpath)
autoload myfunc1 myfunc2 ...</code>
</pre>
</dl>
<p> The usual alias expansion during reading will be suppressed if the <code>autoload</code> builtin or its equivalent is given the option <code>-U</code>. This is recommended for the use of functions supplied with the zsh distribution. Note that for functions precompiled with the <code>zcompile</code> builtin command the flag <code>-U</code> must be provided when the <code>.zwc</code> file is created, as the corresponding information is compiled into the latter. </p>
<p> For each <i>element</i> in <code>fpath</code>, the shell looks for three possible files, the newest of which is used to load the definition for the function: </p>
<dl>
<dt>
<dd> <i>element</i><code>.zwc</code> A file created with the <code>zcompile</code> builtin command, which is expected to contain the definitions for all functions in the directory named <i>element</i>. The file is treated in the same manner as a directory containing files for functions and is searched for the definition of the function. If the definition is not found, the search for a definition proceeds with the other two possibilities described below.</p>
<dl>
<dt>
<dd>
<p> If <i>element</i> already includes a <code>.zwc</code> extension (i.e. the extension was explicitly given by the user), <i>element</i> is searched for the definition of the function without comparing its age to that of other files; in fact, there does not need to be any directory named <i>element</i> without the suffix. Thus including an element such as `<code>/usr/local/funcs.zwc</code>&#8216; in <code>fpath</code> will speed up the search for functions, with the disadvantage that functions included must be explicitly recompiled by hand before the shell notices any changes.</dl>
<dt><i>element</i><code>/</code><i>function</i><code>.zwc</code></p>
<dd> A file created with <code>zcompile</code>, which is expected to contain the definition for <i>function</i>. It may include other function definitions as well, but those are neither loaded nor executed; a file found in this way is searched <i>only</i> for the definition of <i>function</i>.</p>
<dt><i>element</i><code>/</code><i>function</i></p>
<dd> A file of zsh command text, taken to be the definition for <i>function</i>.</dl>
<p> In summary, the order of searching is, first, in the <i>parents of</i> directories in <code>fpath</code> for the newer of either a compiled directory or a directory in <code>fpath</code>; second, if more than one of these contains a definition for the function that is sought, the leftmost in the <code>fpath</code> is chosen; and third, within a directory, the newer of either a compiled function or an ordinary function definition is used. </p>
<p> If the <code>KSH_AUTOLOAD</code> option is set, or the file contains only a simple definition of the function, the file&#8217;s contents will be executed. This will normally define the function in question, but may also perform initialization, which is executed in the context of the function execution, and may therefore define local parameters. It is an error if the function is not defined by loading the file. </p>
<p> Otherwise, the function body (with no surrounding `<i>funcname</i><code>() {</code><i>&#8230;</i><code>}</code>&#8216;) is taken to be the complete contents of the file. This form allows the file to be used directly as an executable shell script. If processing of the file results in the function being re-defined, the function itself is not re-executed. To force the shell to perform initialization and then call the function defined, the file should contain initialization code (which will be executed then discarded) in addition to a complete function definition (which will be retained for subsequent calls to the function), and a call to the shell function, including any arguments, at the end. </p>
<p> For example, suppose the autoload file <code>func</code> contains </p>
<dl>
<dt>
<dd>
<pre>
<code>func() { print This is func; }
print func is initialized</code>
</pre>
</dl>
<p> then `<code>func; func</code>&#8216; with <code>KSH_AUTOLOAD</code> set will produce both messages on the first call, but only the message `<code>This is func</code>&#8216; on the second and subsequent calls. Without <code>KSH_AUTOLOAD</code> set, it will produce the initialization message on the first call, and the other message on the second and subsequent calls. </p>
<p> It is also possible to create a function that is not marked as autoloaded, but which loads its own definition by searching <code>fpath</code>, by using `<code>autoload -X</code>&#8216; within a shell function. For example, the following are equivalent: </p>
<dl>
<dt>
<dd>
<pre>
<code>myfunc() {
  autoload -X
}
myfunc args...</code>
</pre>
</dl>
<p> and </p>
<dl>
<dt>
<dd>
unfunction myfunc #if myfunc was defined<br />
    autoload myfunc<br />
        myfunc args&#8230;
</dl>
<p> In fact, the <code>functions</code> command outputs `<code>builtin autoload -X</code>&#8216; as the body of an autoloaded function. This is done so that </p>
<dl>
<dt>
<dd>
<pre>
<code>eval &quot;$(functions)&quot;</code>
</pre>
</dl>
<p> produces a reasonable result. A true autoloaded function can be identified by the presence of the comment `<code># undefined</code>&#8216; in the body, because all comments are discarded from defined functions. </p>
<p> To load the definition of an autoloaded function <code>myfunc</code> without executing <code>myfunc</code>, use: </p>
<dl>
<dt>
<dd>
<pre>
<code>autoload +X myfunc</code>
</pre>
</dl>
<h2>ANONYMOUS FUNCTIONS</h2>
<p> If no name is given for a function, it is `anonymous&#8217; and is handled specially. Either form of function definition may be used: a `<code>()</code>&#8216; with no preceding name, or a `<code>function</code>&#8216; with an immediately following open brace. The function is executed immediately at the point of definition and is not stored for future use. The function name is set to `<code>(anon)</code>&#8216;. </p>
<p> Arguments to the function may be specified as words following the closing brace defining the function, hence if there are none no arguments (other than <code>$0</code>) are set. This is a difference from the way other functions are parsed: normal function definitions may be followed by certain keywords such as `<code>else</code>&#8216; or `<code>fi</code>&#8216;, which will be treated as arguments to anonymous functions, so that a newline or semicolon is needed to force keyword interpretation. </p>
<p> Note also that the argument list of any enclosing script or function is hidden (as would be the case for any other function called at this point). </p>
<p> Redirections may be applied to the anonymous function in the same manner as to a current-shell structure enclosed in braces. The main use of anonymous functions is to provide a scope for local variables. This is particularly convenient in start-up files as these do not provide their own local variable scope. </p>
<p> For example, </p>
<dl>
<dt>
<dd>
<pre>
<code>variable=outside
function {
  local variable=inside
  print &quot;I am $variable with arguments $*&quot;
} this and that
print &quot;I am $variable&quot;</code>
</pre>
</dl>
<p> outputs the following: </p>
<dl>
<dt>
<dd>
<pre>
<code>I am inside with arguments this and that
I am outside</code>
</pre>
</dl>
<p> Note that function definitions with arguments that expand to nothing, for example `<code>name=; function $name { </code><i>&#8230;</i><code> }</code>&#8216;, are not treated as anonymous functions. Instead, they are treated as normal function definitions where the definition is silently discarded. </p>
<h2>SPECIAL FUNCTIONS</h2>
<p> Certain functions, if defined, have special meaning to the shell. </p>
<h3>Hook Functions</h3>
<p> For the functions below, it is possible to define an array that has the same name as the function with `<code>_functions</code>&#8216; appended. Any element in such an array is taken as the name of a function to execute; it is executed in the same context and with the same arguments as the basic function. For example, if <code>$chpwd_functions</code> is an array containing the values `<code>mychpwd</code>&#8216;, `<code>chpwd_save_dirstack</code>&#8216;, then the shell attempts to execute the functions `<code>chpwd</code>&#8216;, `<code>mychpwd</code>&#8216; and `<code>chpwd_save_dirstack</code>&#8216;, in that order. Any function that does not exist is silently ignored. A function found by this mechanism is referred to elsewhere as a `hook function&#8217;. An error in any function causes subsequent functions not to be run. Note further that an error in a <code>precmd</code> hook causes an immediately following <code>periodic</code> function not to run (though it may run at the next opportunity). </p>
<dl>
<dt>
<dd> <code>chpwd</code> Executed whenever the current working directory is changed.</p>
<dt><code>periodic</code></p>
<dd> If the parameter <code>PERIOD</code> is set, this function is executed every <code>$PERIOD</code> seconds, just before a prompt. Note that if multiple functions are defined using the array <code>periodic_functions</code> only one period is applied to the complete set of functions, and the scheduled time is not reset if the list of functions is altered. Hence the set of functions is always called together.</p>
<dt><code>precmd</code></p>
<dd> Executed before each prompt. Note that precommand functions are not re-executed simply because the command line is redrawn, as happens, for example, when a notification about an exiting job is displayed.</p>
<dt><code>preexec</code></p>
<dd> Executed just after a command has been read and is about to be executed. If the history mechanism is active (regardless of whether the line was discarded from the history buffer), the string that the user typed is passed as the first argument, otherwise it is an empty string. The actual command that will be executed (including expanded aliases) is passed in two different forms: the second argument is a single-line, size-limited version of the command (with things like function bodies elided); the third argument contains the full text that is being executed.</p>
<dt><code>zshaddhistory</code></p>
<dd> Executed when a history line has been read interactively, but before it is executed. The sole argument is the complete history line (so that any terminating newline will still be present).</p>
<dl>
<dt>
<dd>
<p> If any of the hook functions returns status 1 (or any non-zero value other than 2, though this is not guaranteed for future versions of the shell) the history line will not be saved, although it lingers in the history until the next line is executed, allowing you to reuse or edit it immediately. </p>
<p> If any of the hook functions returns status 2 the history line will be saved on the internal history list, but not written to the history file. In case of a conflict, the first non-zero status value is taken. </p>
<p> A hook function may call `<code>fc -p</code> <i>&#8230;</i>&#8216; to switch the history context so that the history is saved in a different file from the that in the global <code>HISTFILE</code> parameter. This is handled specially: the history context is automatically restored after the processing of the history line is finished. </p>
<p> The following example function works with one of the options <code>INC_APPEND_HISTORY</code> or <code>SHARE_HISTORY</code> set, in order that the line is written out immediately after the history entry is added. It first adds the history line to the normal history with the newline stripped, which is usually the correct behaviour. Then it switches the history context so that the line will be written to a history file in the current directory. </p>
<dl>
<dt>
<dd>
zshaddhistory()<br />
{<br />
    print &#8211; sr&#8211; ${1 % % $ &#8216;
&#8217;} fc &#8211; p.zsh_local_history<br />
}
</dl>
</dl>
<dt><code>zshexit</code></p>
<dd> Executed at the point where the main shell is about to exit normally. This is not called by exiting subshells, nor when the <code>exec</code> precommand modifier is used before an external command. Also, unlike <code>TRAPEXIT</code>, it is not called when functions exit.</dl>
<h3>Trap Functions</h3>
<p> The functions below are treated specially but do not have corresponding hook arrays. </p>
<dl>
<dt>
<dd> <code>TRAP</code><i>NAL</i> If defined and non-null, this function will be executed whenever the shell catches a signal <code>SIG</code><i>NAL</i>, where <i>NAL</i> is a signal name as specified for the <code>kill</code> builtin. The signal number will be passed as the first parameter to the function.</p>
<dl>
<dt>
<dd>
<p> If a function of this form is defined and null, the shell and processes spawned by it will ignore <code>SIG</code><i>NAL</i>. </p>
<p> The return status from the function is handled specially. If it is zero, the signal is assumed to have been handled, and execution continues normally. Otherwise, the shell will behave as interrupted except that the return status of the trap is retained. </p>
<p> Programs terminated by uncaught signals typically return the status 128 plus the signal number. Hence the following causes the handler for <code>SIGINT</code> to print a message, then mimic the usual effect of the signal. </p>
<dl>
<dt>
<dd>
<pre>
<code>TRAPINT() {
  print &quot;Caught SIGINT, aborting.&quot;
  return $(( 128 + $1 ))
}</code>
</pre>
</dl>
<p> The functions <code>TRAPZERR</code>, <code>TRAPDEBUG</code> and <code>TRAPEXIT</code> are never executed inside other traps.</dl>
<dt><code>TRAPDEBUG</code></p>
<dd> If the option <code>DEBUG_BEFORE_CMD</code> is set (as it is by default), executed before each command; otherwise executed after each command. See the description of the <code>trap</code> builtin in <i><a href="/docs/linux/man/1-zshbuiltins/">zshbuiltins</a></i>(1) for details of additional features provided in debug traps.</p>
<dt><code>TRAPEXIT</code></p>
<dd> Executed when the shell exits, or when the current function exits if defined inside a function. The value of <code>$?</code> at the start of execution is the exit status of the shell or the return status of the function exiting.</p>
<dt><code>TRAPZERR</code></p>
<dd> Executed whenever a command has a non-zero exit status. However, the function is not executed if the command occurred in a sublist followed by `<code>&amp;&amp;</code>&#8216; or `<code>||</code>&#8216;; only the final command in a sublist of this type causes the trap to be executed. The function <code>TRAPERR</code> acts the same as <code>TRAPZERR</code> on systems where there is no <code>SIGERR</code> (this is the usual case).</dl>
<p> The functions beginning `<code>TRAP</code>&#8216; may alternatively be defined with the <code>trap</code> builtin: this may be preferable for some uses. Setting a trap with one form removes any trap of the other form for the same signal; removing a trap in either form removes all traps for the same signal. The forms </p>
<dl>
<dt>
<dd>
<pre>
<code>TRAPNAL() { 
 # code
}</code>
</pre>
</dl>
<p> (&#8216;function traps&#8217;) and </p>
<dl>
<dt>
<dd>
<pre>
<code>trap '
 # code
' NAL</code>
</pre>
</dl>
<p> (&#8216;list traps&#8217;) are equivalent in most ways, the exceptions being the following: </p>
<dl>
<dt>
<dd> &bull; Function traps have all the properties of normal functions, appearing in the list of functions and being called with their own function context rather than the context where the trap was triggered.</p>
<dt>&bull;</p>
<dd> The return status from function traps is special, whereas a return from a list trap causes the surrounding context to return with the given status.</p>
<dt>&bull;</p>
<dd> Function traps are not reset within subshells, in accordance with zsh behaviour; list traps are reset, in accordance with POSIX behaviour.</dl>
<h2>JOBS</h2>
<p> If the <code>MONITOR</code> option is set, an interactive shell associates a <i>job</i> with each pipeline. It keeps a table of current jobs, printed by the <code>jobs</code> command, and assigns them small integer numbers. When a job is started asynchronously with `<code>&amp;</code>&#8216;, the shell prints a line to standard error which looks like: </p>
<dl>
<dt>
<dd>
<pre>
<code>[1] 1234</code>
</pre>
</dl>
<p> indicating that the job which was started asynchronously was job number 1 and had one (top-level) process, whose process ID was 1234. </p>
<p> If a job is started with `<code>&amp;|</code>&#8216; or `<code>&amp;!</code>&#8216;, then that job is immediately disowned. After startup, it does not have a place in the job table, and is not subject to the job control features described here. </p>
<p> If you are running a job and wish to do something else you may hit the key ^Z (control-Z) which sends a <code>TSTP</code> signal to the current job: this key may be redefined by the <code>susp</code> option of the external <code>stty</code> command. The shell will then normally indicate that the job has been `suspended&#8217;, and print another prompt. You can then manipulate the state of this job, putting it in the background with the <code>bg</code> command, or run some other commands and then eventually bring the job back into the foreground with the foreground command <code>fg</code>. A ^Z takes effect immediately and is like an interrupt in that pending output and unread input are discarded when it is typed. </p>
<p> A job being run in the background will suspend if it tries to read from the terminal. </p>
<p> Note that if the job running in the foreground is a shell function, then suspending it will have the effect of causing the shell to fork. This is necessary to separate the function&#8217;s state from that of the parent shell performing the job control, so that the latter can return to the command line prompt. As a result, even if <code>fg</code> is used to continue the job the function will no longer be part of the parent shell, and any variables set by the function will not be visible in the parent shell. Thus the behaviour is different from the case where the function was never suspended. Zsh is different from many other shells in this regard. </p>
<p> One additional side effect is that use of <code>disown</code> with a job created by suspending shell code in this fashion is delayed: the job can only be disowned once any process started from the parent shell has terminated. At that point, the disowned job disappears silently from the job list. </p>
<p> The same behaviour is found when the shell is executing code as the right hand side of a pipeline or any complex shell construct such as <code>if</code>, <code>for</code>, etc., in order that the entire block of code can be managed as a single job. Background jobs are normally allowed to produce output, but this can be disabled by giving the command `<code>stty tostop</code>&#8216;. If you set this tty option, then background jobs will suspend when they try to produce output like they do when they try to read input. </p>
<p> When a command is suspended and continued later with the <code>fg</code> or <code>wait</code> builtins, zsh restores tty modes that were in effect when it was suspended. This (intentionally) does not apply if the command is continued via `<code>kill -CONT</code>&#8216;, nor when it is continued with <code>bg</code>. </p>
<p> There are several ways to refer to jobs in the shell. A job can be referred to by the process ID of any process of the job or by one of the following: </p>
<dl>
<dt><code>%</code><i>number</i></p>
<dd> The job with the given number.</p>
<dt><code>%</code><i>string</i></p>
<dd> The last job whose command line begins with <i>string</i>.</p>
<dt><code>%?</code><i>string</i></p>
<dd> The last job whose command line contains <i>string</i>.</p>
<dt><code>%%</code></p>
<dd> Current job.</p>
<dt><code>%+</code></p>
<dd> Equivalent to `<code>%%</code>&#8216;.</p>
<dt><code>%-</code></p>
<dd> Previous job.</dl>
<p> The shell learns immediately whenever a process changes state. It normally informs you whenever a job becomes blocked so that no further progress is possible. If the <code>NOTIFY</code> option is not set, it waits until just before it prints a prompt before it informs you. All such notifications are sent directly to the terminal, not to the standard output or standard error. </p>
<p> When the monitor mode is on, each background job that completes triggers any trap set for <code>CHLD</code>. </p>
<p> When you try to leave the shell while jobs are running or suspended, you will be warned that `You have suspended (running) jobs&#8217;. You may use the <code>jobs</code> command to see what they are. If you do this or immediately try to exit again, the shell will not warn you a second time; the suspended jobs will be terminated, and the running jobs will be sent a <code>SIGHUP</code> signal, if the <code>HUP</code> option is set. </p>
<p> To avoid having the shell terminate the running jobs, either use the <code>nohup</code> command (see <i><a href="/docs/linux/man/1-nohup/">nohup</a></i>(1)) or the <code>disown</code> builtin.</p>
<h2>SIGNALS</h2>
<p> The <code>INT</code> and <code>QUIT</code> signals for an invoked command are ignored if the command is followed by `<code>&amp;</code>&#8216; and the <code>MONITOR</code> option is not active. The shell itself always ignores the <code>QUIT</code> signal. Otherwise, signals have the values inherited by the shell from its parent (but see the <code>TRAP</code><i>NAL</i> special functions in the section `Functions&#8217;). </p>
<p> Certain jobs are run asynchronously by the shell other than those explicitly put into the background; even in cases where the shell would usually wait for such jobs, an explicit <code>exit</code> command or exit due to the option <code>ERR_EXIT</code> will cause the shell to exit without waiting. Examples of such asynchronous jobs are process substitution, see the section PROCESS SUBSTITUTION in the <i><a href="/docs/linux/man/1-zshexpn/">zshexpn</a></i>(1) manual page, and the handler processes for multios, see the section MULTIOS in the <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1) manual page.</p>
<h2>ARITHMETIC EVALUATION</h2>
<p> The shell can perform integer and floating point arithmetic, either using the builtin <code>let</code>, or via a substitution of the form <code>$((</code><i>&#8230;</i><code>))</code>. For integers, the shell is usually compiled to use 8-byte precision where this is available, otherwise precision is 4 bytes. This can be tested, for example, by giving the command `<code>print &#8211; $(( 12345678901 ))</code>&#8216;; if the number appears unchanged, the precision is at least 8 bytes. Floating point arithmetic always uses the `double&#8217; type with whatever corresponding precision is provided by the compiler and the library. </p>
<p> The <code>let</code> builtin command takes arithmetic expressions as arguments; each is evaluated separately. Since many of the arithmetic operators, as well as spaces, require quoting, an alternative form is provided: for any command which begins with a `<code>((</code>&#8216;, all the characters until a matching `<code>))</code>&#8216; are treated as a quoted expression and arithmetic expansion performed as for an argument of <code>let</code>. More precisely, `<code>((</code><i>&#8230;</i><code>))</code>&#8216; is equivalent to `<code>let &quot;</code><i>&#8230;</i><code>&quot;</code>&#8216;. The return status is 0 if the arithmetic value of the expression is non-zero, 1 if it is zero, and 2 if an error occurred. </p>
<p> For example, the following statement </p>
<dl>
<dt>
<dd>
<pre>
<code>(( val = 2 + 1 ))</code>
</pre>
</dl>
<p> is equivalent to </p>
<dl>
<dt>
<dd>
<pre>
<code>let &quot;val = 2 + 1&quot;</code>
</pre>
</dl>
<p> both assigning the value 3 to the shell variable <code>val</code> and returning a zero status. </p>
<p> Integers can be in bases other than 10. A leading `<code>0x</code>&#8216; or `<code>0X</code>&#8216; denotes hexadecimal and a leading `<code>0b</code>&#8216; or `<code>0B</code>&#8216; binary. Integers may also be of the form `<i>base</i><code>#</code><i>n</i>&#8216;, where <i>base</i> is a decimal number between two and thirty-six representing the arithmetic base and <i>n</i> is a number in that base (for example, `<code>16#ff</code>&#8216; is 255 in hexadecimal). The <i>base</i><code>#</code> may also be omitted, in which case base 10 is used. For backwards compatibility the form `<code>[</code><i>base</i><code>]</code><i>n</i>&#8216; is also accepted. </p>
<p> An integer expression or a base given in the form `<i>base</i><code>#</code><i>n</i>&#8216; may contain underscores (`<code>_</code>&#8216;) after the leading digit for visual guidance; these are ignored in computation. Examples are <code>1_000_000</code> or <code>0xffff_ffff</code> which are equivalent to <code>1000000</code> and <code>0xffffffff</code> respectively. </p>
<p> It is also possible to specify a base to be used for output in the form `<code>[#</code><i>base</i><code>]</code>&#8216;, for example `<code>[#16]</code>&#8216;. This is used when outputting arithmetical substitutions or when assigning to scalar parameters, but an explicitly defined integer or floating point parameter will not be affected. If an integer variable is implicitly defined by an arithmetic expression, any base specified in this way will be set as the variable&#8217;s output arithmetic base as if the option `<code>-i</code> <i>base</i>&#8216; to the <code>typeset</code> builtin had been used. The expression has no precedence and if it occurs more than once in a mathematical expression, the last encountered is used. For clarity it is recommended that it appear at the beginning of an expression. As an example: </p>
<dl>
<dt>
<dd>
<pre>
<code>typeset -i 16 y
print $(( [#8] x = 32, y = 32 ))
print $x $y</code>
</pre>
</dl>
<p> outputs first `<code>8#40</code>&#8216;, the rightmost value in the given output base, and then `<code>8#40 16#20</code>&#8216;, because <code>y</code> has been explicitly declared to have output base 16, while <code>x</code> (assuming it does not already exist) is implicitly typed by the arithmetic evaluation, where it acquires the output base 8. </p>
<p> The <i>base</i> may be replaced or followed by an underscore, which may itself be followed by a positive integer (if it is missing the value 3 is used). This indicates that underscores should be inserted into the output string, grouping the number for visual clarity. The following integer specifies the number of digits to group together. For example: </p>
<dl>
<dt>
<dd>
<pre>
<code>setopt cbases
print $(( [#16_4] 65536 ** 2 ))</code>
</pre>
</dl>
<p> outputs `<code>0x1_0000_0000</code>&#8216;. </p>
<p> The feature can be used with floating point numbers, in which case the base must be omitted; grouping is away from the decimal point. For example, </p>
<dl>
<dt>
<dd>
<pre>
<code>zmodload zsh/mathfunc
print $(( [#_] sqrt(1e7) ))</code>
</pre>
</dl>
<p> outputs `<code>3_162.277_660_168_379_5</code>&#8216; (the number of decimal places shown may vary). </p>
<p> If the <code>C_BASES</code> option is set, hexadecimal numbers are output in the standard C format, for example `<code>0xFF</code>&#8216; instead of the usual `<code>16#FF</code>&#8216;. If the option <code>OCTAL_ZEROES</code> is also set (it is not by default), octal numbers will be treated similarly and hence appear as `<code>077</code>&#8216; instead of `<code>8#77</code>&#8216;. This option has no effect on the output of bases other than hexadecimal and octal, and these formats are always understood on input. </p>
<p> When an output base is specified using the `<code>[#</code><i>base</i><code>]</code>&#8216; syntax, an appropriate base prefix will be output if necessary, so that the value output is valid syntax for input. If the <code>#</code> is doubled, for example `<code>[##16]</code>&#8216;, then no base prefix is output. </p>
<p> Floating point constants are recognized by the presence of a decimal point or an exponent. The decimal point may be the first character of the constant, but the exponent character <code>e</code> or <code>E</code> may not, as it will be taken for a parameter name. All numeric parts (before and after the decimal point and in the exponent) may contain underscores after the leading digit for visual guidance; these are ignored in computation. </p>
<p> An arithmetic expression uses nearly the same syntax and associativity of expressions as in C. </p>
<p> In the native mode of operation, the following operators are supported (listed in decreasing order of precedence): </p>
<dl>
<dt><code>+ &#8211; ! ~ ++ &#8212;</code></p>
<dd> unary plus/minus, logical NOT, complement, {pre,post}{in,de}crement</p>
<dt><code>&lt;&lt; &gt;&gt;</code></p>
<dd> bitwise shift left, right</p>
<dt><code>&amp;</code></p>
<dd> bitwise AND</p>
<dt><code>^</code></p>
<dd> bitwise XOR</p>
<dt><code>|</code></p>
<dd> bitwise OR</p>
<dt><code>**</code></p>
<dd> exponentiation</p>
<dt><code>* / %</code></p>
<dd> multiplication, division, modulus (remainder)</p>
<dt><code>+ &#8211;</code></p>
<dd> addition, subtraction</p>
<dt><code>&lt; &gt; &lt;= &gt;=</code></p>
<dd> comparison</p>
<dt><code>== !=</code></p>
<dd> equality and inequality</p>
<dt><code>&amp;&amp;</code></p>
<dd> logical AND</p>
<dt><code>|| ^^</code></p>
<dd> logical OR, XOR</p>
<dt><code>? :</code></p>
<dd> ternary operator</p>
<dt><code>= += -= *= /= %= &amp;= ^= |= &lt;&lt;= &gt;&gt;= &amp;&amp;= ||= ^^= **=</code></p>
<dd> assignment</p>
<dt><code>,</code></p>
<dd> comma operator</dl>
<p> The operators `<code>&amp;&amp;</code>&#8216;, `<code>||</code>&#8216;, `<code>&amp;&amp;=</code>&#8216;, and `<code>||=</code>&#8216; are short-circuiting, and only one of the latter two expressions in a ternary operator is evaluated. Note the precedence of the bitwise AND, OR, and XOR operators. </p>
<p> With the option <code>C_PRECEDENCES</code> the precedences (but no other properties) of the operators are altered to be the same as those in most other languages that support the relevant operators: </p>
<dl>
<dt><code>+ &#8211; ! ~ ++ &#8212;</code></p>
<dd> unary plus/minus, logical NOT, complement, {pre,post}{in,de}crement</p>
<dt><code>**</code></p>
<dd> exponentiation</p>
<dt><code>* / %</code></p>
<dd> multiplication, division, modulus (remainder)</p>
<dt><code>+ &#8211;</code></p>
<dd> addition, subtraction</p>
<dt><code>&lt;&lt; &gt;&gt;</code></p>
<dd> bitwise shift left, right</p>
<dt><code>&lt; &gt; &lt;= &gt;=</code></p>
<dd> comparison</p>
<dt><code>== !=</code></p>
<dd> equality and inequality</p>
<dt><code>&amp;</code></p>
<dd> bitwise AND</p>
<dt><code>^</code></p>
<dd> bitwise XOR</p>
<dt><code>|</code></p>
<dd> bitwise OR</p>
<dt><code>&amp;&amp;</code></p>
<dd> logical AND</p>
<dt><code>^^</code></p>
<dd> logical XOR</p>
<dt><code>||</code></p>
<dd> logical OR</p>
<dt><code>? :</code></p>
<dd> ternary operator</p>
<dt><code>= += -= *= /= %= &amp;= ^= |= &lt;&lt;= &gt;&gt;= &amp;&amp;= ||= ^^= **=</code></p>
<dd> assignment</p>
<dt><code>,</code></p>
<dd> comma operator</dl>
<p> Note the precedence of exponentiation in both cases is below that of unary operators, hence `<code>-3**2</code>&#8216; evaluates as `<code>9</code>&#8216;, not `<code>-9</code>&#8216;. Use parentheses where necessary: `<code>-(3**2)</code>&#8216;. This is for compatibility with other shells. </p>
<p> Mathematical functions can be called with the syntax `<i>func</i><code>(</code><i>args</i><code>)</code>&#8216;, where the function decides if the <i>args</i> is used as a string or a comma-separated list of arithmetic expressions. The shell currently defines no mathematical functions by default, but the module <code>zsh/mathfunc</code> may be loaded with the <code>zmodload</code> builtin to provide standard floating point mathematical functions. </p>
<p> An expression of the form `<code>##</code><i>x</i>&#8216; where <i>x</i> is any character sequence such as `<code>a</code>&#8216;, `<code>^A</code>&#8216;, or `<code>\M-\C-x</code>&#8216; gives the value of this character and an expression of the form `<code>#</code><i>name</i>&#8216; gives the value of the first character of the contents of the parameter <i>name</i>. Character values are according to the character set used in the current locale; for multibyte character handling the option <code>MULTIBYTE</code> must be set. Note that this form is different from `<code>$#</code><i>name</i>&#8216;, a standard parameter substitution which gives the length of the parameter <i>name</i>. `<code>#\</code>&#8216; is accepted instead of `<code>##</code>&#8216;, but its use is deprecated. </p>
<p> Named parameters and subscripted arrays can be referenced by name within an arithmetic expression without using the parameter expansion syntax. For example, </p>
<dl>
<dt>
<dd>
<pre>
<code>((val2 = val1 * 2))</code>
</pre>
</dl>
<p> assigns twice the value of <code>$val1</code> to the parameter named <code>val2</code>. </p>
<p> An internal integer representation of a named parameter can be specified with the <code>integer</code> builtin. Arithmetic evaluation is performed on the value of each assignment to a named parameter declared integer in this manner. Assigning a floating point number to an integer results in rounding towards zero. </p>
<p> Likewise, floating point numbers can be declared with the <code>float</code> builtin; there are two types, differing only in their output format, as described for the <code>typeset</code> builtin. The output format can be bypassed by using arithmetic substitution instead of the parameter substitution, i.e. `<code>${</code><i>float</i><code>}</code>&#8216; uses the defined format, but `<code>$((</code><i>float</i><code>))</code>&#8216; uses a generic floating point format. </p>
<p> Promotion of integer to floating point values is performed where necessary. In addition, if any operator which requires an integer (`<code>&amp;</code>&#8216;, `<code>|</code>&#8216;, `<code>^</code>&#8216;, `<code>&lt;&lt;</code>&#8216;, `<code>&gt;&gt;</code>&#8216; and their equivalents with assignment) is given a floating point argument, it will be silently rounded towards zero except for `<code>~</code>&#8216; which rounds down. </p>
<p> Users should beware that, in common with many other programming languages but not software designed for calculation, the evaluation of an expression in zsh is taken a term at a time and promotion of integers to floating point does not occur in terms only containing integers. A typical result of this is that a division such as <code>6/8</code> is truncated, in this being rounded towards 0. The <code>FORCE_FLOAT</code> shell option can be used in scripts or functions where floating point evaluation is required throughout. </p>
<p> Scalar variables can hold integer or floating point values at different times; there is no memory of the numeric type in this case. </p>
<p> If a variable is first assigned in a numeric context without previously being declared, it will be implicitly typed as <code>integer</code> or <code>float</code> and retain that type either until the type is explicitly changed or until the end of the scope. This can have unforeseen consequences. For example, in the loop </p>
<dl>
<dt>
<dd>
for ((f = 0; f &lt; 1; f += 0.1))<br />
    ;<br />
do<br />
#use $f<br />
done
</dl>
<p> if <code>f</code> has not already been declared, the first assignment will cause it to be created as an integer, and consequently the operation `<code>f += 0.1</code>&#8216; will always cause the result to be truncated to zero, so that the loop will fail. A simple fix would be to turn the initialization into `<code>f = 0.0</code>&#8216;. It is therefore best to declare numeric variables with explicit types.</p>
<h2>CONDITIONAL EXPRESSIONS</h2>
<p> A <i>conditional expression</i> is used with the <code>[[</code> compound command to test attributes of files and to compare strings. Each expression can be constructed from one or more of the following unary or binary expressions: </p>
<dl>
<dt>
<dd> <code>-a</code> <i>file</i> true if <i>file</i> exists.</p>
<dt><code>-b</code> <i>file</i></p>
<dd> true if <i>file</i> exists and is a block special file.</p>
<dt><code>-c</code> <i>file</i></p>
<dd> true if <i>file</i> exists and is a character special file.</p>
<dt><code>-d</code> <i>file</i></p>
<dd> true if <i>file</i> exists and is a directory.</p>
<dt><code>-e</code> <i>file</i></p>
<dd> true if <i>file</i> exists.</p>
<dt><code>-f</code> <i>file</i></p>
<dd> true if <i>file</i> exists and is a regular file.</p>
<dt><code>-g</code> <i>file</i></p>
<dd> true if <i>file</i> exists and has its setgid bit set.</p>
<dt><code>-h</code> <i>file</i></p>
<dd> true if <i>file</i> exists and is a symbolic link.</p>
<dt><code>-k</code> <i>file</i></p>
<dd> true if <i>file</i> exists and has its sticky bit set.</p>
<dt><code>-n</code> <i>string</i></p>
<dd> true if length of <i>string</i> is non-zero.</p>
<dt><code>-o</code> <i>option</i></p>
<dd> true if option named <i>option</i> is on. <i>option</i> may be a single character, in which case it is a single letter option name. (See the section `Specifying Options&#8217;.)</p>
<dl>
<dt>
<dd>
<p> When no option named <i>option</i> exists, and the <code>POSIX_BUILTINS</code> option hasn&#8217;t been set, return 3 with a warning. If that option is set, return 1 with no warning.</dl>
<dt><code>-p</code> <i>file</i></p>
<dd> true if <i>file</i> exists and is a FIFO special file (named pipe).</p>
<dt><code>-r</code> <i>file</i></p>
<dd> true if <i>file</i> exists and is readable by current process.</p>
<dt><code>-s</code> <i>file</i></p>
<dd> true if <i>file</i> exists and has size greater than zero.</p>
<dt><code>-t</code> <i>fd</i></p>
<dd> true if file descriptor number <i>fd</i> is open and associated with a terminal device. (note: <i>fd</i> is not optional)</p>
<dt><code>-u</code> <i>file</i></p>
<dd> true if <i>file</i> exists and has its setuid bit set.</p>
<dt><code>-v</code> <i>varname</i></p>
<dd> true if shell variable <i>varname</i> is set.</p>
<dt><code>-w</code> <i>file</i></p>
<dd> true if <i>file</i> exists and is writable by current process.</p>
<dt><code>-x</code> <i>file</i></p>
<dd> true if <i>file</i> exists and is executable by current process. If <i>file</i> exists and is a directory, then the current process has permission to search in the directory.</p>
<dt><code>-z</code> <i>string</i></p>
<dd> true if length of <i>string</i> is zero.</p>
<dt><code>-L</code> <i>file</i></p>
<dd> true if <i>file</i> exists and is a symbolic link.</p>
<dt><code>-O</code> <i>file</i></p>
<dd> true if <i>file</i> exists and is owned by the effective user ID of this process.</p>
<dt><code>-G</code> <i>file</i></p>
<dd> true if <i>file</i> exists and its group matches the effective group ID of this process.</p>
<dt><code>-S</code> <i>file</i></p>
<dd> true if <i>file</i> exists and is a socket.</p>
<dt><code>-N</code> <i>file</i></p>
<dd> true if <i>file</i> exists and its access time is not newer than its modification time.</p>
<dt><i>file1</i> <code>-nt</code> <i>file2</i></p>
<dd> true if <i>file1</i> exists and is newer than <i>file2</i>.</p>
<dt><i>file1</i> <code>-ot</code> <i>file2</i></p>
<dd> true if <i>file1</i> exists and is older than <i>file2</i>.</p>
<dt><i>file1</i> <code>-ef</code> <i>file2</i></p>
<dd> true if <i>file1</i> and <i>file2</i> exist and refer to the same file.</p>
<dt>
<dd> <i>string</i> <code>=</code> <i>pattern</i></p>
<dt>
<dd> <i>string</i> <code>==</code> <i>pattern</i> true if <i>string</i> matches <i>pattern</i>. The two forms are exactly equivalent. The `<code>=</code>&#8216; form is the traditional shell syntax (and hence the only one generally used with the <code>test</code> and <code>[</code> builtins); the `<code>==</code>&#8216; form provides compatibility with other sorts of computer language.</p>
<dt><i>string</i> <code>!=</code> <i>pattern</i></p>
<dd> true if <i>string</i> does not match <i>pattern</i>.</p>
<dt><i>string</i> <code>=~</code> <i>regexp</i></p>
<dd> true if <i>string</i> matches the regular expression <i>regexp</i>. If the option <code>RE_MATCH_PCRE</code> is set <i>regexp</i> is tested as a PCRE regular expression using the <code>zsh/pcre</code> module, else it is tested as a POSIX extended regular expression using the <code>zsh/regex</code> module. Upon successful match, some variables will be updated; no variables are changed if the matching fails.</p>
<dl>
<dt>
<dd>
<p> If the option <code>BASH_REMATCH</code> is not set the scalar parameter <code>MATCH</code> is set to the substring that matched the pattern and the integer parameters <code>MBEGIN</code> and <code>MEND</code> to the index of the start and end, respectively, of the match in <i>string</i>, such that if <i>string</i> is contained in variable <code>var</code> the expression `<code>${var[$MBEGIN,$MEND]}</code>&#8216; is identical to `<code>$MATCH</code>&#8216;. The setting of the option <code>KSH_ARRAYS</code> is respected. Likewise, the array <code>match</code> is set to the substrings that matched parenthesised subexpressions and the arrays <code>mbegin</code> and <code>mend</code> to the indices of the start and end positions, respectively, of the substrings within <i>string</i>. The arrays are not set if there were no parenthesised subexpressions. For example, if the string `<code>a short string</code>&#8216; is matched against the regular expression `<code>s(&#8230;)t</code>&#8216;, then (assuming the option <code>KSH_ARRAYS</code> is not set) <code>MATCH</code>, <code>MBEGIN</code> and <code>MEND</code> are `<code>short</code>&#8216;, <code>3</code> and <code>7</code>, respectively, while <code>match</code>, <code>mbegin</code> and <code>mend</code> are single entry arrays containing the strings `<code>hor</code>&#8216;, `<code>4</code>&#8216; and `<code>6</code>&#8216;, respectively. </p>
<p> If the option <code>BASH_REMATCH</code> is set the array <code>BASH_REMATCH</code> is set to the substring that matched the pattern followed by the substrings that matched parenthesised subexpressions within the pattern.</dl>
<dt><i>string1</i> <code>&lt;</code> <i>string2</i></p>
<dd> true if <i>string1</i> comes before <i>string2</i> based on ASCII value of their characters.</p>
<dt><i>string1</i> <code>&gt;</code> <i>string2</i></p>
<dd> true if <i>string1</i> comes after <i>string2</i> based on ASCII value of their characters.</p>
<dt><i>exp1</i> <code>-eq</code> <i>exp2</i></p>
<dd> true if <i>exp1</i> is numerically equal to <i>exp2</i>. Note that for purely numeric comparisons use of the <code>((</code><i>&#8230;</i><code>))</code> builtin described in the section `ARITHMETIC EVALUATION&#8217; is more convenient than conditional expressions.</p>
<dt><i>exp1</i> <code>-ne</code> <i>exp2</i></p>
<dd> true if <i>exp1</i> is numerically not equal to <i>exp2</i>.</p>
<dt><i>exp1</i> <code>-lt</code> <i>exp2</i></p>
<dd> true if <i>exp1</i> is numerically less than <i>exp2</i>.</p>
<dt><i>exp1</i> <code>-gt</code> <i>exp2</i></p>
<dd> true if <i>exp1</i> is numerically greater than <i>exp2</i>.</p>
<dt><i>exp1</i> <code>-le</code> <i>exp2</i></p>
<dd> true if <i>exp1</i> is numerically less than or equal to <i>exp2</i>.</p>
<dt><i>exp1</i> <code>-ge</code> <i>exp2</i></p>
<dd> true if <i>exp1</i> is numerically greater than or equal to <i>exp2</i>.</p>
<dt><code>(</code> <i>exp</i> <code>)</code></p>
<dd> true if <i>exp</i> is true.</p>
<dt><code>!</code> <i>exp</i></p>
<dd> true if <i>exp</i> is false.</p>
<dt><i>exp1</i> <code>&amp;&amp;</code> <i>exp2</i></p>
<dd> true if <i>exp1</i> and <i>exp2</i> are both true.</p>
<dt><i>exp1</i> <code>||</code> <i>exp2</i></p>
<dd> true if either <i>exp1</i> or <i>exp2</i> is true.</dl>
<p> For compatibility, if there is a single argument that is not syntactically significant, typically a variable, the condition is treated as a test for whether the expression expands as a string of non-zero length. In other words, <code>[[ $var ]]</code> is the same as <code>[[ -n $var ]]</code>. It is recommended that the second, explicit, form be used where possible. </p>
<p> Normal shell expansion is performed on the <i>file</i>, <i>string</i> and <i>pattern</i> arguments, but the result of each expansion is constrained to be a single word, similar to the effect of double quotes. </p>
<p> Filename generation is not performed on any form of argument to conditions. However, it can be forced in any case where normal shell expansion is valid and when the option <code>EXTENDED_GLOB</code> is in effect by using an explicit glob qualifier of the form <code>(#q)</code> at the end of the string. A normal glob qualifier expression may appear between the `<code>q</code>&#8216; and the closing parenthesis; if none appears the expression has no effect beyond causing filename generation. The results of filename generation are joined together to form a single word, as with the results of other forms of expansion. </p>
<p> This special use of filename generation is only available with the <code>[[</code> syntax. If the condition occurs within the <code>[</code> or <code>test</code> builtin commands then globbing occurs instead as part of normal command line expansion before the condition is evaluated. In this case it may generate multiple words which are likely to confuse the syntax of the test command. </p>
<p> For example, </p>
<dl>
<dt>
<dd>
[[-n file * (#qN)]]
</dl>
<p> produces status zero if and only if there is at least one file in the current directory beginning with the string `<code>file</code>&#8216;. The globbing qualifier <code>N</code> ensures that the expression is empty if there is no matching file. </p>
<p> Pattern metacharacters are active for the <i>pattern</i> arguments; the patterns are the same as those used for filename generation, see <i><a href="/docs/linux/man/1-zshexpn/">zshexpn</a></i>(1), but there is no special behaviour of `<code>/</code>&#8216; nor initial dots, and no glob qualifiers are allowed. </p>
<p> In each of the above expressions, if <i>file</i> is of the form `<code>/dev/fd/</code><i>n</i>&#8216;, where <i>n</i> is an integer, then the test applied to the open file whose descriptor number is <i>n</i>, even if the underlying system does not support the <code>/dev/fd</code> directory. </p>
<p> In the forms which do numeric comparison, the expressions <i>exp</i> undergo arithmetic expansion as if they were enclosed in <code>$((</code><i>&#8230;</i><code>))</code>. </p>
<p> For example, the following: </p>
<dl>
<dt>
<dd>
<pre><code>
[[(-f foo || -f bar) &amp;&amp;$report = y * ]] &amp;&amp; print File exists.
</code></pre>
</dl>
<p> tests if either file <code>foo</code> or file <code>bar</code> exists, and if so, if the value of the parameter <code>report</code> begins with `<code>y</code>&#8216;; if the complete condition is true, the message `<code>File exists.</code>&#8216; is printed.</p>
<h2>EXPANSION OF PROMPT SEQUENCES</h2>
<p> Prompt sequences undergo a special form of expansion. This type of expansion is also available using the <code>-P</code> option to the <code>print</code> builtin. </p>
<p> If the <code>PROMPT_SUBST</code> option is set, the prompt string is first subjected to <i>parameter expansion</i>, <i>command substitution</i> and <i>arithmetic expansion</i>. See <i><a href="/docs/linux/man/1-zshexpn/">zshexpn</a></i>(1). </p>
<p> Certain escape sequences may be recognised in the prompt string. </p>
<p> If the <code>PROMPT_BANG</code> option is set, a `<code>!</code>&#8216; in the prompt is replaced by the current history event number. A literal `<code>!</code>&#8216; may then be represented as `<code>!!</code>&#8216;. </p>
<p> If the <code>PROMPT_PERCENT</code> option is set, certain escape sequences that start with `<code>%</code>&#8216; are expanded. Many escapes are followed by a single character, although some of these take an optional integer argument that should appear between the `<code>%</code>&#8216; and the next character of the sequence. More complicated escape sequences are available to provide conditional expansion. </p>
<h2>SIMPLE PROMPT ESCAPES</h2>
<h3>Special characters</h3>
<dl>
<dt>
<dd> <code>%%</code> A `<code>%</code>&#8216;.</p>
<dt><code>%)</code></p>
<dd> A `<code>)</code>&#8216;.</dl>
<h3>Login information</h3>
<dl>
<dt>
<dd> <code>%l</code> The line (tty) the user is logged in on, without `<code>/dev/</code>&#8216; prefix. If the name starts with `<code>/dev/tty</code>&#8216;, that prefix is stripped.</p>
<dt><code>%M</code></p>
<dd> The full machine hostname.</p>
<dt><code>%m</code></p>
<dd> The hostname up to the first `<code>.</code>&#8216;. An integer may follow the `<code>%</code>&#8216; to specify how many components of the hostname are desired. With a negative integer, trailing components of the hostname are shown.</p>
<dt><code>%n</code></p>
<dd> <code>$USERNAME</code>.</p>
<dt><code>%y</code></p>
<dd> The line (tty) the user is logged in on, without `<code>/dev/</code>&#8216; prefix. This does not treat `<code>/dev/tty</code>&#8216; names specially.</dl>
<h3>Shell state</h3>
<dl>
<dt>
<dd> <code>%#</code> A `<code>#</code>&#8216; if the shell is running with privileges, a `<code>%</code>&#8216; if not. Equivalent to `<code>%(!.#.%%)</code>&#8216;. The definition of `privileged&#8217;, for these purposes, is that either the effective user ID is zero, or, if POSIX.1e capabilities are supported, that at least one capability is raised in either the Effective or Inheritable capability vectors.</p>
<dt><code>%?</code></p>
<dd> The return status of the last command executed just before the prompt.</p>
<dt><code>%_</code></p>
<dd> The status of the parser, i.e. the shell constructs (like `<code>if</code>&#8216; and `<code>for</code>&#8216;) that have been started on the command line. If given an integer number that many strings will be printed; zero or negative or no integer means print as many as there are. This is most useful in prompts <code>PS2</code> for continuation lines and <code>PS4</code> for debugging with the <code>XTRACE</code> option; in the latter case it will also work non-interactively.</p>
<dt><code>%^</code></p>
<dd> The status of the parser in reverse. This is the same as `<code>%_</code>&#8216; other than the order of strings. It is often used in <code>RPS2</code>.</p>
<dt>
<dd> <code>%d</code></p>
<dt>
<dd> <code>%/</code> Current working directory. If an integer follows the `<code>%</code>&#8216;, it specifies a number of trailing components of the current working directory to show; zero means the whole path. A negative integer specifies leading components, i.e. <code>%-1d</code> specifies the first component.</p>
<dt><code>%~</code></p>
<dd> As <code>%d</code> and <code>%/</code>, but if the current working directory starts with <code>$HOME</code>, that part is replaced by a `<code>~</code>&#8216;. Furthermore, if it has a named directory as its prefix, that part is replaced by a `<code>~</code>&#8216; followed by the name of the directory, but only if the result is shorter than the full path; see <i>Dynamic</i> and <i>Static named directories</i> in <i><a href="/docs/linux/man/1-zshexpn/">zshexpn</a></i>(1).</p>
<dt><code>%e</code></p>
<dd> Evaluation depth of the current sourced file, shell function, or <code>eval</code>. This is incremented or decremented every time the value of <code>%N</code> is set or reverted to a previous value, respectively. This is most useful for debugging as part of <code>$PS4</code>.</p>
<dt>
<dd> <code>%h</code></p>
<dt>
<dd> <code>%!</code> Current history event number.</p>
<dt><code>%i</code></p>
<dd> The line number currently being executed in the script, sourced file, or shell function given by <code>%N</code>. This is most useful for debugging as part of <code>$PS4</code>.</p>
<dt><code>%I</code></p>
<dd> The line number currently being executed in the file <code>%x</code>. This is similar to <code>%i</code>, but the line number is always a line number in the file where the code was defined, even if the code is a shell function.</p>
<dt><code>%j</code></p>
<dd> The number of jobs.</p>
<dt><code>%L</code></p>
<dd> The current value of <code>$SHLVL</code>.</p>
<dt><code>%N</code></p>
<dd> The name of the script, sourced file, or shell function that zsh is currently executing, whichever was started most recently. If there is none, this is equivalent to the parameter <code>$0</code>. An integer may follow the `<code>%</code>&#8216; to specify a number of trailing path components to show; zero means the full path. A negative integer specifies leading components.</p>
<dt><code>%x</code></p>
<dd> The name of the file containing the source code currently being executed. This behaves as <code>%N</code> except that function and eval command names are not shown, instead the file where they were defined.</p>
<dt>
<dd> <code>%c</code></p>
<dt>
<dd> <code>%.</code></p>
<dt>
<dd> <code>%C</code> Trailing component of the current working directory. An integer may follow the `<code>%</code>&#8216; to get more than one component. Unless `<code>%C</code>&#8216; is used, tilde contraction is performed first. These are deprecated as <code>%c</code> and <code>%C</code> are equivalent to <code>%1~</code> and <code>%1/</code>, respectively, while explicit positive integers have the same effect as for the latter two sequences.</dl>
<h3>Date and time</h3>
<dl>
<dt>
<dd> <code>%D</code> The date in <i>yy</i><code>&#8211;</code><i>mm</i><code>&#8211;</code><i>dd</i> format.</p>
<dt><code>%T</code></p>
<dd> Current time of day, in 24-hour format.</p>
<dt>
<dd> <code>%t</code></p>
<dt>
<dd> <code>%@</code> Current time of day, in 12-hour, am/pm format.</p>
<dt><code>%*</code></p>
<dd> Current time of day in 24-hour format, with seconds.</p>
<dt><code>%w</code></p>
<dd> The date in <i>day</i><code>&#8211;</code><i>dd</i> format.</p>
<dt><code>%W</code></p>
<dd> The date in <i>mm</i><code>/</code><i>dd</i><code>/</code><i>yy</i> format.</p>
<dt><code>%D{</code><i>string</i><code>}</code></p>
<dd> <i>string</i> is formatted using the <code>strftime</code> function. See <i><a href="/docs/linux/man/3-strftime/">strftime</a></i>(3) for more details. Various zsh extensions provide numbers with no leading zero or space if the number is a single digit:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>%f</code></p>
<dd> a day of the month</p>
<dt><code>%K</code></p>
<dd> the hour of the day on the 24-hour clock</p>
<dt><code>%L</code></p>
<dd> the hour of the day on the 12-hour clock</dl>
<p> In addition, if the system supports the POSIX <code>gettimeofday</code> system call, <code>%.</code> provides decimal fractions of a second since the epoch with leading zeroes. By default three decimal places are provided, but a number of digits up to 9 may be given following the <code>%</code>; hence <code>%6.</code> outputs microseconds, and <code>%9.</code> outputs nanoseconds. (The latter requires a nanosecond-precision <code>clock_gettime</code>; systems lacking this will return a value multiplied by the appropriate power of 10.) A typical example of this is the format `<code>%D{%H:%M:%S.%.}</code>&#8216;. </p>
<p> The GNU extension <code>%N</code> is handled as a synonym for <code>%9.</code>. </p>
<p> Additionally, the GNU extension that a `<code>&#8211;</code>&#8216; between the <code>%</code> and the format character causes a leading zero or space to be stripped is handled directly by the shell for the format characters <code>d</code>, <code>f</code>, <code>H</code>, <code>k</code>, <code>l</code>, <code>m</code>, <code>M</code>, <code>S</code> and <code>y</code>; any other format characters are provided to the system&#8217;s <a href="/docs/linux/man/3-strftime/">strftime</a>(3) with any leading `<code>&#8211;</code>&#8216; present, so the handling is system dependent. Further GNU (or other) extensions are also passed to <a href="/docs/linux/man/3-strftime/">strftime</a>(3) and may work if the system supports them.</dl>
</dl>
<h3>Visual effects</h3>
<dl>
<dt>
<dd> <code>%B</code> (<code>%b</code>) Start (stop) boldface mode.</p>
<dt><code>%E</code></p>
<dd> Clear to end of line.</p>
<dt><code>%U</code> (<code>%u</code>)</p>
<dd> Start (stop) underline mode.</p>
<dt><code>%S</code> (<code>%s</code>)</p>
<dd> Start (stop) standout mode.</p>
<dt><code>%F</code> (<code>%f</code>)</p>
<dd> Start (stop) using a different foreground colour, if supported by the terminal. The colour may be specified two ways: either as a numeric argument, as normal, or by a sequence in braces following the <code>%F</code>, for example <code>%F{red}</code>. In the latter case the values allowed are as described for the <code>fg</code> <code>zle_highlight</code> attribute; see <i>Character Highlighting</i> in <i><a href="/docs/linux/man/1-zshzle/">zshzle</a></i>(1). This means that numeric colours are allowed in the second format also.</p>
<dt><code>%K</code> (<code>%k</code>)</p>
<dd> Start (stop) using a different bacKground colour. The syntax is identical to that for <code>%F</code> and <code>%f</code>.</p>
<dt><code>%{</code>&#8230;<code>%}</code></p>
<dd> Include a string as a literal escape sequence. The string within the braces should not change the cursor position. Brace pairs can nest.</p>
<dl>
<dt>
<dd>
<p> A positive numeric argument between the <code>%</code> and the <code>{</code> is treated as described for <code>%G</code> below.</dl>
<dt><code>%G</code></p>
<dd> Within a <code>%{</code>&#8230;<code>%}</code> sequence, include a `glitch&#8217;: that is, assume that a single character width will be output. This is useful when outputting characters that otherwise cannot be correctly handled by the shell, such as the alternate character set on some terminals. The characters in question can be included within a <code>%{</code>&#8230;<code>%}</code> sequence together with the appropriate number of <code>%G</code> sequences to indicate the correct width. An integer between the `<code>%</code>&#8216; and `<code>G</code>&#8216; indicates a character width other than one. Hence <code>%{</code><i>seq</i><code>%2G%}</code> outputs <i>seq</i> and assumes it takes up the width of two standard characters.</p>
<dl>
<dt>
<dd>
<p> Multiple uses of <code>%G</code> accumulate in the obvious fashion; the position of the <code>%G</code> is unimportant. Negative integers are not handled. </p>
<p> Note that when prompt truncation is in use it is advisable to divide up output into single characters within each <code>%{</code>&#8230;<code>%}</code> group so that the correct truncation point can be found.</dl>
</dl>
<h2>CONDITIONAL SUBSTRINGS IN PROMPTS</h2>
<dl>
<dt>
<dd> <code>%v</code> The value of the first element of the <code>psvar</code> array parameter. Following the `<code>%</code>&#8216; with an integer gives that element of the array. Negative integers count from the end of the array.</p>
<dt><code>%(</code><i>x</i><code>.</code><i>true-text</i><code>.</code><i>false-text</i><code>)</code></p>
<dd> Specifies a ternary expression. The character following the <i>x</i> is arbitrary; the same character is used to separate the text for the `true&#8217; result from that for the `false&#8217; result. This separator may not appear in the <i>true-text</i>, except as part of a %-escape sequence. A `<code>)</code>&#8216; may appear in the <i>false-text</i> as `<code>%)</code>&#8216;. <i>true-text</i> and <i>false-text</i> may both contain arbitrarily-nested escape sequences, including further ternary expressions.</p>
<dl>
<dt>
<dd>
<p> The left parenthesis may be preceded or followed by a positive integer <i>n</i>, which defaults to zero. A negative integer will be multiplied by -1, except as noted below for `<code>l</code>&#8216;. The test character <i>x</i> may be any of the following: </p>
<dl>
<dt><code>!</code></p>
<dd> True if the shell is running with privileges.</p>
<dt><code>#</code></p>
<dd> True if the effective uid of the current process is <i>n</i>.</p>
<dt><code>?</code></p>
<dd> True if the exit status of the last command was <i>n</i>.</p>
<dt><code>_</code></p>
<dd> True if at least <i>n</i> shell constructs were started.</p>
<dt><code>C</code></p>
<dd>
<dt><code>/</code></p>
<dd> True if the current absolute path has at least <i>n</i> elements relative to the root directory, hence <code>/</code> is counted as 0 elements.</p>
<dt><code>c</code></p>
<dd>
<dt><code>.</code></p>
<dd>
<dt><code>~</code></p>
<dd> True if the current path, with prefix replacement, has at least <i>n</i> elements relative to the root directory, hence <code>/</code> is counted as 0 elements.</p>
<dt><code>D</code></p>
<dd> True if the month is equal to <i>n</i> (January = 0).</p>
<dt><code>d</code></p>
<dd> True if the day of the month is equal to <i>n</i>.</p>
<dt><code>e</code></p>
<dd> True if the evaluation depth is at least <i>n</i>.</p>
<dt><code>g</code></p>
<dd> True if the effective gid of the current process is <i>n</i>.</p>
<dt><code>j</code></p>
<dd> True if the number of jobs is at least <i>n</i>.</p>
<dt><code>L</code></p>
<dd> True if the <code>SHLVL</code> parameter is at least <i>n</i>.</p>
<dt><code>l</code></p>
<dd> True if at least <i>n</i> characters have already been printed on the current line. When <i>n</i> is negative, true if at least <code>abs</code><code>(</code><i>n</i><code>)</code> characters remain before the opposite margin (thus the left margin for <code>RPROMPT</code>).</p>
<dt><code>S</code></p>
<dd> True if the <code>SECONDS</code> parameter is at least <i>n</i>.</p>
<dt><code>T</code></p>
<dd> True if the time in hours is equal to <i>n</i>.</p>
<dt><code>t</code></p>
<dd> True if the time in minutes is equal to <i>n</i>.</p>
<dt><code>v</code></p>
<dd> True if the array <code>psvar</code> has at least <i>n</i> elements.</p>
<dt><code>V</code></p>
<dd> True if element <i>n</i> of the array <code>psvar</code> is set and non-empty.</p>
<dt><code>w</code></p>
<dd> True if the day of the week is equal to <i>n</i> (Sunday = 0).</dl>
</dl>
<dt>
<dd> <code>%&lt;</code><i>string</i><code>&lt;</code></p>
<dt>
<dd> <code>%&gt;</code><i>string</i><code>&gt;</code></p>
<dt>
<dd> <code>%[</code><i>xstring</i><code>]</code> Specifies truncation behaviour for the remainder of the prompt string. The third, deprecated, form is equivalent to `<code>%</code><i>xstringx</i>&#8216;, i.e. <i>x</i> may be `<code>&lt;</code>&#8216; or `<code>&gt;</code>&#8216;. The <i>string</i> will be displayed in place of the truncated portion of any string; note this does not undergo prompt expansion.</p>
<dl>
<dt>
<dd>
<p> The numeric argument, which in the third form may appear immediately after the `<code>[</code>&#8216;, specifies the maximum permitted length of the various strings that can be displayed in the prompt. In the first two forms, this numeric argument may be negative, in which case the truncation length is determined by subtracting the absolute value of the numeric argument from the number of character positions remaining on the current prompt line. If this results in a zero or negative length, a length of 1 is used. In other words, a negative argument arranges that after truncation at least <i>n</i> characters remain before the right margin (left margin for <code>RPROMPT</code>). </p>
<p> The forms with `<code>&lt;</code>&#8216; truncate at the left of the string, and the forms with `<code>&gt;</code>&#8216; truncate at the right of the string. For example, if the current directory is `<code>/home/pike</code>&#8216;, the prompt `<code>%8&lt;..&lt;%/</code>&#8216; will expand to `<code>..e/pike</code>&#8216;. In this string, the terminating character (`<code>&lt;</code>&#8216;, `<code>&gt;</code>&#8216; or `<code>]</code>&#8216;), or in fact any character, may be quoted by a preceding `<code>\</code>&#8216;; note when using <code>print -P</code>, however, that this must be doubled as the string is also subject to standard <code>print</code> processing, in addition to any backslashes removed by a double quoted string: the worst case is therefore `<code>print -P &quot;%&lt;\\&lt;&lt;&#8230;&quot;</code>&#8216;. </p>
<p> If the <i>string</i> is longer than the specified truncation length, it will appear in full, completely replacing the truncated string. </p>
<p> The part of the prompt string to be truncated runs to the end of the string, or to the end of the next enclosing group of the `<code>%(</code>&#8216; construct, or to the next truncation encountered at the same grouping level (i.e. truncations inside a `<code>%(</code>&#8216; are separate), which ever comes first. In particular, a truncation with argument zero (e.g., `<code>%&lt;&lt;</code>&#8216;) marks the end of the range of the string to be truncated while turning off truncation from there on. For example, the prompt `<code>%10&lt;&#8230;&lt;%~%&lt;&lt;%# </code>&#8216; will print a truncated representation of the current directory, followed by a `<code>%</code>&#8216; or `<code>#</code>&#8216;, followed by a space. Without the `<code>%&lt;&lt;</code>&#8216;, those two characters would be included in the string to be truncated. Note that `<code>%-0&lt;&lt;</code>&#8216; is not equivalent to `<code>%&lt;&lt;</code>&#8216; but specifies that the prompt is truncated at the right margin. </p>
<p> Truncation applies only within each individual line of the prompt, as delimited by embedded newlines (if any). If the total length of any line of the prompt after truncation is greater than the terminal width, or if the part to be truncated contains embedded newlines, truncation behavior is undefined and may change in a future version of the shell. Use `<code>%-</code><i>n</i><code>(l.</code><i>true-text</i><code>.</code><i>false-text</i><code>)</code>&#8216; to remove parts of the prompt when the available space is less than <i>n</i>.</dl>
</dl>
<h2>Index</h2>
