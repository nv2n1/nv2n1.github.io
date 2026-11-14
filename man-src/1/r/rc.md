---
title: "rc(1)"
name: "rc"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rc/"
description: "rc – shell"
---

<h2>NAME</h2>
<p> rc &#8211; shell</p>
<h2>SYNOPSIS</h2>
<p> <code>rc</code> [<code>-deiIlnopsvx</code>] [<code>-c</code> <i>command</i>] [<i>arguments</i>]</p>
<h2>DESCRIPTION</h2>
<p> <i>rc</i> is a command interpreter and programming language similar to <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1). It is based on the AT&amp;T Plan 9 shell of the same name. The shell offers a C-like syntax (much more so than the C shell), and a powerful mechanism for manipulating variables. It is reasonably small and reasonably fast, especially when compared to contemporary shells. Its use is intended to be interactive, but the language lends itself well to scripts.</p>
<h2>OPTIONS</h2>
<dl>
<dt> R-c</p>
<dd> If R-c is present, commands are executed from the immediately following argument. Any further arguments to <i>rc</i> are placed in R$*R. R$* Thus: </p>
<pre>
Rrc -c 'echo $*' 1 2 3
</pre>
<dt>
<dd> prints out </p>
<pre>
R1 2 3
</pre>
<dt> R-d</p>
<dd> This flag causes <i>rc</i> not to ignore RSIGQUIT or RSIGTERMR. RSIGTERM Thus <i>rc</i> can be made to dump core if sent RSIGQUITR. RSIGQUIT This flag is only useful for debugging <i>rc</i>.</p>
<dt> R-e</p>
<dd> If the R-e flag is present, then <i>rc</i> will exit if the exit status of a command is false (nonzero). <i>rc</i> will not exit, however, if a conditional fails, e.g., an Rif() command.</p>
<dt> R-i</p>
<dd> If the R-i flag is present or if the input to <i>rc</i> is from a terminal (as determined by <i><a href="/docs/linux/man/3-isatty/">isatty</a></i>(3)) then <i>rc</i> will be in <i>interactive</i> mode. That is, a prompt (from R$<a href="/docs/linux/man/1-prompt/">prompt</a>(1)R) R$<a href="/docs/linux/man/1-prompt/">prompt</a>(1) will be printed before an input line is taken, and <i>rc</i> will ignore RSIGINTR. RSIGINT</p>
<dt> R-I</p>
<dd> If the R-I flag is present, or if the input to <i>rc</i> is not from a terminal, then <i>rc</i> will not be in interactive mode. No prompts will be printed, and RSIGINT will cause <i>rc</i> to exit.</p>
<dt> R-l</p>
<dd> If the R-l flag is present, or if <i>rc</i>&#8216;s Rargv[0][0] is a dash R(R-R), R(R- R( then <i>rc</i> will behave as a login shell. That is, it will run commands from R$home/.rcrcR, R$home/.rcrc if this file exists, before reading any other input.</p>
<dt> R-n</p>
<dd> This flag causes <i>rc</i> to read its input and parse it, but not to execute any commands. This is useful for syntax checking on scripts. If used in combination with the R-x flag, <i>rc</i> will print each command as it is parsed in a form similar to the one used for exporting functions into the environment.</p>
<dt> R-o</p>
<dd> This flag prevents the usual practice of trying to open R/dev/null on file descriptors 0, 1, and 2, if any of those descriptors are inherited closed.</p>
<dt> R-p</p>
<dd> This flag prevents <i>rc</i> from initializing shell functions from the environment. This allows <i>rc</i> to run in a protected mode, whereby it becomes more difficult for an <i>rc</i> script to be subverted by placing false commands in the environment. (Note that the presence of this flag does <i>not</i> mean that it is safe to run setuid <i>rc</i> scripts; the usual caveats about the setuid bit still apply.)</p>
<dt> R-s</p>
<dd> This flag causes <i>rc</i> to read from standard input. Any arguments are placed in R$*R. R$*</p>
<dt> R-v</p>
<dd> This flag causes <i>rc</i> to echo its input to standard error as it is read.</p>
<dt> R-x</p>
<dd> This flag causes <i>rc</i> to print every command on standard error before it is executed. It can be useful for debugging <i>rc</i> scripts.</dl>
<h2>COMMANDS</h2>
<p> A simple command is a sequence of words, separated by white space (space and tab) characters that ends with a newline, semicolon R(R;R), R(R; R( or ampersand R(R&amp;R). R(R&amp; R( The first word of a command is the name of that command. If the name begins with R/R, R/ R./R, R./ or R../R, R../ then the name is used as an absolute path name referring to an executable file. Otherwise, the name of the command is looked up in a table of shell functions, builtin commands, or as a file in the directories named by R$pathR. R$path</p>
<h3>Background Tasks</h3>
<p> A command ending with R&amp; is run in the background; that is, the shell returns immediately rather than waiting for the command to complete. Background commands have R/dev/null connected to their standard input unless an explicit redirection for standard input is used.</p>
<h3>Subshells</h3>
<p> A command prefixed with an at-sign R(R@R) R(R@ R( is executed in a subshell. This insulates the parent shell from the effects of state changing operations such as a <code>cd</code> or a variable assignment. For example: </p>
<pre>
R@ {cd ..; make}
</pre>
<p> will run <i><a href="/docs/linux/man/1-make/">make</a></i>(1) in the parent directory R(R..R), R(R.. R( but leaves the shell running in the current directory.</p>
<h3>Line continuation</h3>
<p> A long logical line may be continued over several physical lines by terminating each line (except the last) with a backslash R(R\R). R(R\ R( The backslash-newline sequence is treated as a space. A backslash is not otherwise special to <i>rc</i>. (In addition, inside quotes a backslash loses its special meaning even when it is followed by a newline.)</p>
<h3>Quoting</h3>
<p> <i>rc</i> interprets several characters specially; special characters automatically terminate words. The following characters are special: </p>
<pre>
R# ; &amp; | ^ $ = ` ' { } ( ) &lt; &gt;
</pre>
<p> The single quote R(R&#8217;R) R(R&#8217; R( prevents special treatment of any character other than itself. All characters, including control characters, newlines, and backslashes between two quote characters are treated as an uninterpreted string. A quote character itself may be quoted by placing two quotes in a row. The minimal sequence needed to enter the quote character is R&#8221;&#8221;R. R&#8221;&#8221; The empty string is represented by R&#8221;R. R&#8221; Thus: </p>
<pre>
Recho 'What''s the plan, Stan?'
</pre>
<p> prints out </p>
<pre>
RWhat's the plan, Stan?
</pre>
<p> The number sign R(R#R) R(R# R( begins a comment in <i>rc</i>. All characters up to but not including the next newline are ignored. Note that backslash continuation does not work inside a comment, i.e., the backslash is ignored along with everything else.</p>
<h3>Grouping</h3>
<p> Zero or more commands may be grouped within braces R(&#8220;R{R&#8221; R(&#8220;R{ R(&#8220; and R&#8220;R}R&#8221;), R&#8220;R} R&#8220; and are then treated as one command. Braces do not otherwise define scope; they are used only for command grouping. In particular, be wary of the command: </p>
<pre>
Rfor (i) {
R    command
R} | command
</pre>
<p> Since pipe binds tighter than RforR, Rfor this command does not perform what the user expects it to. Instead, enclose the whole Rfor statement in braces: </p>
<pre>
R{for (i) command} | command
</pre>
<p> Fortunately, <i>rc</i>&#8216;s grammar is simple enough that a (confident) user can understand it by examining the skeletal <i><a href="/docs/linux/man/1-yacc/">yacc</a></i>(1) grammar at the end of this man page (see the section entitled <code>GRAMMAR</code>).</p>
<h3>Input and output</h3>
<p> The standard output may be redirected to a file with </p>
<pre>
Rcommand &gt; file
</pre>
<p> and the standard input may be taken from a file with </p>
<pre>
Rcommand &lt; file
</pre>
<p> Redirections can appear anywhere in the line: the word following the redirection symbol is the filename and must be quoted if it contains spaces or other special characters. These are all equivalent. </p>
<pre>
Recho 1 2 3 &gt; foo
R&gt; foo echo 1 2 3
Recho 1 2 &gt; foo 3
</pre>
<p> File descriptors other than 0 and 1 may be specified also. For example, to redirect standard error to a file, use: </p>
<pre>
Rcommand &gt;[2] file
</pre>
<p> In order to duplicate a file descriptor, use R&gt;[InR=ImR]. R&gt;[InR=Im R&gt;[InR= R&gt;[In R&gt;[ Thus to redirect both standard output and standard error to the same file, use </p>
<pre>
Rcommand &gt; file &gt;[2=1]
</pre>
<p> As in <i>sh</i>, redirections are processed from left to right. Thus this sequence </p>
<pre>
Rcommand &gt;[2=1] &gt; file
</pre>
<p> is usually a mistake. It first duplicates standard error to standard output; then redirects standard output to a file, leaving standard error wherever standard output originally was. </p>
<p> To close a file descriptor that may be open, use R&gt;[InR=]. R&gt;[In R&gt;[ For example, to close file descriptor 7: </p>
<pre>
Rcommand &gt;[7=]
</pre>
<p> Note that no spaces may appear in these constructs: </p>
<pre>
Rcommand &gt; [2] file
</pre>
<p> would send the output of the command to a file named R[2]R, R[2] with the intended filename appearing in the command&#8217;s argument list. </p>
<p> In order to place the output of a command at the end of an already existing file, use: </p>
<pre>
Rcommand &gt;&gt; file
</pre>
<p> If the file does not exist, then it is created. </p>
<p> &#8220;Here documents&#8221; are supported as in <i>sh</i> with the use of </p>
<pre>
Rcommand &lt;&lt; 'eof-marker'
</pre>
<p> Subsequent lines form the standard input of the command, till a line containing just the marker, in this case Reof-markerR, Reof-marker is encountered. </p>
<p> If the end-of-file marker is enclosed in quotes, then no variable substitution occurs inside the here document. Otherwise, every variable is substituted by its space-separated-list value (see <code>Flat Lists</code>, below), and if a R^ character follows a variable name, it is deleted. This allows the unambiguous use of variables adjacent to text, as in </p>
<pre>
R$variable^follow
</pre>
<p> To include a literal R$ in a here document when an unquoted end-of-file marker is being used, enter it as R$$R. R$$ </p>
<p> Additionally, <i>rc</i> supports &#8220;here strings&#8221;, which are like here documents, except that input is taken directly from a string on the command line. Their use is illustrated here: </p>
<pre>
Rcat &lt;&lt;&lt; 'this is a here string' | wc
</pre>
<p> (This feature enables <i>rc</i> to export functions using here documents into the environment; the author does not expect users to find this feature useful.)</p>
<h3>Pipes</h3>
<p> Two or more commands may be combined in a pipeline by placing the vertical bar R(R|R) R(R| R( between them. The standard output (file descriptor 1) of the command on the left is tied to the standard input (file descriptor 0) of the command on the right. The notation R|[InR=ImR] R|[InR=Im R|[InR= R|[In R|[ indicates that file descriptor <i>n</i> of the left process is connected to file descriptor <i>m</i> of the right process. R|[InR] R|[In R|[ is a shorthand for R|[InR=0]. R|[In R|[ As an example, to pipe the standard error of a command to <i><a href="/docs/linux/man/1-wc/">wc</a></i>(1), use: </p>
<pre>
Rcommand |[2] wc
</pre>
<p> As with file redirections, no spaces may occur in the construct specifying numbered file descriptors. </p>
<p> The exit status of a pipeline is considered true if and only if every command in the pipeline exits true.</p>
<h3>Commands as Arguments</h3>
<p> Some commands, like <i><a href="/docs/linux/man/1-cmp/">cmp</a></i>(1) or <i><a href="/docs/linux/man/1-diff/">diff</a></i>(1), take their arguments on the command line, and do not read input from standard input. It is convenient sometimes to build nonlinear pipelines so that a command like <i>cmp</i> can read the output of two other commands at once. <i>rc</i> does it like this: </p>
<pre><code>
Rcmp &lt; {command} &lt;
{
    command
}
</code></pre>
<p> compares the output of the two commands in braces. Note: since this form of redirection is implemented with some kind of pipe, and since one cannot <i><a href="/docs/linux/man/2-lseek/">lseek</a></i>(2) on a pipe, commands that use <i><a href="/docs/linux/man/2-lseek/">lseek</a></i>(2) will hang. For example, some versions of <i><a href="/docs/linux/man/1-diff/">diff</a></i>(1) use <i><a href="/docs/linux/man/2-lseek/">lseek</a></i>(2) on their inputs. </p>
<p> Data can be sent down a pipe to several commands using <i><a href="/docs/linux/man/1-tee/">tee</a></i>(1) and the output version of this notation: </p>
<p>Recho hi there | tee &gt; {sed &#8216;s/^/p1 /&#8217;} &gt;<br />
{<br />
    sed &#8216;s/^/p2 /&#8217;<br />
}</p>
<h2>CONTROL STRUCTURES</h2>
<p> The following may be used for control flow in <i>rc</i>:</p>
<h3>If-Else Statements</h3>
<p> Rif (ItestR) { Rif (Itest Rif (<br />
 <i> cmd</i> </p>
<dl>
<dt> R} else Icmd R} else</p>
<dd> The <i>test</i> is executed, and if its return status is zero, the first command is executed, otherwise the second is. Braces are not mandatory around the commands. However, an Relse statement is valid only if it follows a close-brace on the same line. Otherwise, the Rif is taken to be a simple-if: </p>
<pre>
Rif (test)
R    command
</pre>
</dl>
<h3>While and For Loops</h3>
<dl>
<dt> Rwhile (ItestR)I cmd Rwhile (ItestR) Rwhile (Itest Rwhile (</p>
<dd> <i>rc</i> executes the <i>test</i> and performs the command as long as the <i>test</i> is true.</p>
<dt> Rfor (IvarR in IlistR)I cmd Rfor (IvarR in IlistR) Rfor (IvarR in Ilist Rfor (IvarR in Rfor (Ivar Rfor (</p>
<dd> <i>rc</i> sets <i>var</i> to each element of <i>list</i> (which may contain variables and backquote substitutions) and runs <i>cmd</i>. If R&#8220;Rin R&#8220; <i>list</i>&#8221; is omitted, then <i>rc</i> will set <i>var</i> to each element of R$*R. R$* For example: </p>
<p>Rfor(i in `{ls &#8211; F | grep &#8216;\*$&#8217; | sed &#8216;s/\*$//&#8217;})<br />
{<br />
    commands<br />
}</p>
<dt>
<dd> will set R$i to the name of each file in the current directory that is executable.</dl>
<h3>Switch</h3>
<dl>
<dt> Rswitch (IlistR) { caseI &#8230;R } Rswitch (IlistR) { caseI &#8230; Rswitch (IlistR) { case Rswitch (Ilist Rswitch (</p>
<dd> <i>rc</i> looks inside the braces after a Rswitch for statements beginning with the word RcaseR. Rcase If any of the patterns following Rcase match the list supplied to RswitchR, Rswitch then the commands up until the next Rcase statement are executed. The metacharacters R*R, R* R[ or R? should not be quoted; matching is performed only against the strings in <i>list</i>, not against file names. (Matching for case statements is the same as for the R~ command.)</dl>
<h3>Logical Operators</h3>
<p> There are a number of operators in <i>rc</i> which depend on the exit status of a command. </p>
<pre>
Rcommand &amp;&amp; command
</pre>
<p> executes the first command and then executes the second command if and only if the first command exits with a zero exit status (&#8220;true&#8221; in Unix). </p>
<pre>
Rcommand || command
</pre>
<p> executes the first command and then executes the second command if and only if the first command exits with a nonzero exit status (&#8220;false&#8221; in Unix). </p>
<pre>
R! command
</pre>
<p> negates the exit status of a command.</p>
<h2>PATTERN MATCHING</h2>
<p> There are two forms of pattern matching in <i>rc</i>. One is traditional shell globbing. This occurs in matching for file names in argument lists: </p>
<pre>
Rcommand argument argument ...
</pre>
<p> When the characters R*R, R* R[ or R? occur in an argument or command, <i>rc</i> looks at the argument as a pattern for matching against files. (Contrary to the behavior other shells exhibit, <i>rc</i> will only perform pattern matching if a metacharacter occurs unquoted and literally in the input. Thus, </p>
<pre>
Rfoo='*'
Recho $foo
</pre>
<p> will always echo just a star. In order for non-literal metacharacters to be expanded, an Reval statement must be used in order to rescan the input.) Pattern matching occurs according to the following rules: a R* matches any number (including zero) of characters. A R? matches any single character, and a R[ followed by a number of characters followed by a R] matches a single character in that class. The rules for character class matching are the same as those for <i><a href="/docs/linux/man/1-ed/">ed</a></i>(1), with the exception that character class negation is achieved with the tilde R(R~R), R(R~ R( not the caret R(R^R), R(R^ R( since the caret already means something else in <i>rc</i>. </p>
<p> <i>rc</i> also matches patterns against strings with the R~ command: </p>
<pre>
R~ subject pattern pattern ...
</pre>
<p> R~ sets R$status to zero if and only if a supplied pattern matches any single element of the subject list. Thus </p>
<pre>
R~ foo f*
</pre>
<p> sets status to zero, while </p>
<pre>
R~ (bar baz) f*
</pre>
<p> sets status to one. The null list is matched by the null list, so </p>
<pre>
R~ $foo ()
</pre>
<p> checks to see whether R$foo is empty or not. This may also be achieved by the test </p>
<pre>
R~ $#foo 0
</pre>
<p> Note that inside a R~ command <i>rc</i> does not match patterns against file names, so it is not necessary to quote the characters R*R, R* R[ and R?R. R? However, <i>rc</i> does expand the subject against filenames if it contains metacharacters. Thus, the command </p>
<pre>
R~ * ?
</pre>
<p> returns true if any of the files in the current directory have a single-character name. If the R~ command is given a list as its first argument, then a successful match against any of the elements of that list will cause R~ to return true. For example: </p>
<pre>
R~ (foo goo zoo) z*
</pre>
<p> is true.</p>
<h2>LISTS AND VARIABLES</h2>
<p> The primary data structure in <i>rc</i> is the list, which is a sequence of words. Parentheses are used to group lists. The empty list is represented by R()R. R() Lists have no hierarchical structure; a list inside another list is expanded so the outer list contains all the elements of the inner list. Thus, the following are all equivalent </p>
<pre>
Rone two three
R(one two three)
R((one) () ((two three)))
</pre>
<p> Note that the null string, R&#8221;R, R&#8221; and the null list, R()R, R() are two very different things. Assigning the null string to a variable is a valid operation, but it does not remove its definition. </p>
<pre>
Rnull = '' empty = () echo $#null $#empty
</pre>
<p> produces the output </p>
<pre>
R1 0
</pre>
<h3>List Concatenation</h3>
<p> Two lists may be joined by the concatenation operator R(R^R). R(R^ R( Concatenation works according to the following rules: if the two lists have the same number of elements, then concatenation is pairwise: </p>
<pre>
Recho (a- b- c-)^(1 2 3)
</pre>
<p> produces the output </p>
<pre>
Ra-1 b-2 c-3
</pre>
<p> Otherwise, at least one of the lists must have a single element, and then the concatenation is distributive: </p>
<pre>
Rcc -^(O g c) (malloc alloca)^.c
</pre>
<p> has the effect of performing the command </p>
<pre>
Rcc -O -g -c malloc.c alloca.c
</pre>
<p> A single word is a list of length one, so </p>
<pre>
Recho foo^bar
</pre>
<p> produces the output </p>
<pre>
Rfoobar
</pre>
<h3>Free Carets</h3>
<p> <i>rc</i> inserts carets (concatenation operators) for free in certain situations, in order to save some typing on the user&#8217;s behalf. For example, the above example could also be typed in as: </p>
<pre>
Ropts=(O g c) files=(malloc alloca) cc -$opts $files.c
</pre>
<p> <i>rc</i> takes care to insert a free-caret between the R&#8220;R-R&#8221; R&#8220;R- R&#8220; and R$optsR, R$opts as well as between R$files and R.cR. R.c The rule for free carets is as follows: if a word or keyword is immediately followed by another word, keyword, dollar-sign or backquote, then <i>rc</i> inserts a caret between them.</p>
<h3>Variables</h3>
<p> A list may be assigned to a variable, using the notation: </p>
<pre>
IvarR = IlistIvarR = 
Ivar
</pre>
<p> The special variable R* may also be assigned to using this notation; <i>rc</i> has no <code>set</code> builtin. </p>
<p> Any non-empty sequence of characters, except a sequence including only digits, may be used as a variable name. Any character except R= may be used, but special characters must be quoted. All user-defined variables are exported into the environment. </p>
<p> The value of a variable is referenced with the dollar R(R$R) R(R$ R( operator: </p>
<pre>
R$IvarR$
</pre>
<p> Any variable which has not been assigned a value returns the null list, R()R, R() when referenced. Multiple references are allowed: </p>
<pre>
Ra = foo
Rb = a
Recho $ $ b
</pre>
<p> prints </p>
<pre>
Rfoo
</pre>
<p> A variable&#8217;s definition may also be removed by assigning the null list to a variable: </p>
<pre>
IvarR=()Ivar
</pre>
<p> For &#8220;free careting&#8221; to work correctly, <i>rc</i> must make certain assumptions about what characters may appear in a variable name. <i>rc</i> assumes that a variable name consists only of alphanumeric characters, underscore R(R_R) R(R_ R( and star R(R*R). R(R* R( To reference a variable with other characters in its name, quote the variable name. Thus: </p>
<pre>
Recho $'we$Ird:Variab!le'
</pre>
<h3>Local Variables</h3>
<p> Any number of variable assignments may be made local to a single command by typing: </p>
<pre>
Ra=foo b=bar ... command
</pre>
<p> The command may be a compound command, so for example: </p>
<pre>
Rpath=. ifs=() {
R    R...R    
R}
</pre>
<p> sets Rpath to R. and removes Rifs for the duration of one long compound command.</p>
<h3>Variable Subscripts</h3>
<p> Variables may be subscripted with the notation </p>
<pre>
R$var(InR)R$var(In
R$var(
</pre>
<p> where <i>n</i> is a list of integers (origin 1). The opening parenthesis must immediately follow the variable name. The list of subscripts need not be in order or even unique. Thus, </p>
<pre>
Ra=(one two three)
Recho $a(3 3 3)
</pre>
<p> prints </p>
<pre>
Rthree three three
</pre>
<p> If <i>n</i> references a nonexistent element, then R$var(InR) R$var(In R$var( returns the null list. The notation R$In, R$ where <i>n</i> is an integer, is a shorthand for R$*(InR). R$*(In R$*( Thus, <i>rc</i>&#8216;s arguments may be referred to as R$1R, R$1 R$2R, R$2 and so on. </p>
<p> Note also that the list of subscripts may be given by any of <i>rc</i>&#8216;s list operations: </p>
<p>R$var(`{awk &#8216;BEGIN{for(i=1;i&lt;=10;i++)print i;exit; }&#8217;})</p>
<p> returns the first 10 elements of R$varR. R$var </p>
<p> To count the number of elements in a variable, use </p>
<pre>
R$#var
</pre>
<p> This returns a single-element list, with the number of elements in R$varR. R$var</p>
<h3>Flat Lists</h3>
<p> In order to create a single-element list from a multi-element list, with the components space-separated, use the dollar-caret R(R$^R) R(R$^ R( operator: </p>
<pre>
R$^var
</pre>
<p> This is useful when the normal list concatenation rules need to be bypassed. For example, to append a single period at the end of R$pathR, R$path use: </p>
<pre>
Recho $^path.
</pre>
<p> For compability with the Plan 9 rc, </p>
<pre>
R$var
</pre>
<p> is accepted as a synonym for dollar-caret.</p>
<h3>Backquote Substitution</h3>
<p> A list may be formed from the output of a command by using backquote substitution: </p>
<pre>
R`{ command }
</pre>
<p> returns a list formed from the standard output of the command in braces. R$ifs is used to split the output into list elements. By default, R$ifs has the value space-tab-newline. The braces may be omitted if the command is a single word. Thus R`ls may be used instead of R`{ls}R. R`{ls} This last feature is useful when defining functions that expand to useful argument lists. A frequent use is: </p>
<p>Rfn src<br />
{<br />
    echo *.[chy]<br />
}</p>
<p> followed by </p>
<pre>
Rwc `src
</pre>
<p> (This will print out a word-count of all C source files in the current directory.) </p>
<p> In order to override the value of R$ifs for a single backquote substitution, use: </p>
<pre>
R`` (ifs-list) { command }
</pre>
<p> R$ifs will be temporarily ignored and the command&#8217;s output will be split as specified by the list following the double backquote. For example: </p>
<pre>
R`` ($nl :) {cat /etc/passwd}
</pre>
<p> splits up R/etc/passwd into fields, assuming that R$nl contains a newline as its value.</p>
<h2>SPECIAL VARIABLES</h2>
<p> Several variables are known to <i>rc</i> and are treated specially. In the following list, &#8220;default&#8221; indicates that <i>rc</i> gives the variable a default value on startup; &#8220;no-export&#8221; indicates that the variable is never exported; and &#8220;read-only&#8221; indicates that an attempt to set the variable will silently have no effect. </p>
<p> Also, &#8220;alias&#8221; means that the variable is aliased to the same name in capitals. For example, an assignment to R$cdpath causes an automatic assignment to R$CDPATHR, R$CDPATH and vice-versa. If R$CDPATH is set when <i>rc</i> is started, its value is imported into R$cdpathR. R$cdpath R$cdpath and R$path are <i>rc</i> lists; R$CDPATH and R$PATH are colon-separated lists. Only the names spelt in capitals are exported into the environment.</p>
<dl>
<dt> R*R (no-export) R*</p>
<dd> The argument list of <i>rc</i>. R$1, $2, etc. are the same as R$*(1)R, R$*(1) R$*(2)R, R$*(2) etc.</p>
<dt> R0R (default no-export) R0</p>
<dd> The variable R$0 holds the value of Rargv[0] with which <i>rc</i> was invoked. Additionally, R$0 is set to the name of a function for the duration of the execution of that function, and R$0 is also set to the name of the file being interpreted for the duration of a R. command. R$0 is not an element of R$*R, R$* and is never treated as one.</p>
<dt> RapidR (no-export) Rapid</p>
<dd> The process ID of the last process started in the background.</p>
<dt> RapidsR (no-export read-only) Rapids</p>
<dd> A list whose elements are the process IDs of all background processes which are still alive, or which have died and have not been waited for yet.</p>
<dt> RbqstatusR (no-export) Rbqstatus</p>
<dd> The exit status of the <i>rc</i> forked to execute the most recent backquote substitution. Note that, unlike R$statusR, R$status R$bqstatus is always a single element list (see <code>EXIT STATUS</code> below). For example: </p>
<pre>
Recho foo |grep bar; whatis status
</pre>
<dt>
<dd> prints </p>
<pre>
Rstatus=(0 1)
</pre>
<dt>
<dd> whereas </p>
<pre>
Rx=`{echo foo |grep bar}; whatis bqstatus
</pre>
<dt>
<dd> prints </p>
<pre>
Rbqstatus=1
</pre>
<dt> RcdpathR (alias) Rcdpath</p>
<dd> A list of directories to search for the target of a <code>cd</code> command. The empty string stands for the current directory. Note that if the R$cdpath variable does not contain the current directory, then the current directory will not be searched; this allows directory searching to begin in a directory other than the current directory.</p>
<dt> Rhistory</p>
<dd> R$history contains the name of a file to which commands are appended as <i>rc</i> reads them. This facilitates the use of a stand-alone history program (such as <i><a href="/docs/linux/man/1-history/">history</a></i>(1)) which parses the contents of the history file and presents them to <i>rc</i> for reinterpretation. If R$history is not set, then <i>rc</i> does not append commands to any file.</p>
<dt> RhomeR (alias) Rhome</p>
<dd> The default directory for the builtin <code>cd</code> command, and the directory in which <i>rc</i> looks to find its initialization file, R.rcrcR, R.rcrc if <i>rc</i> has been started up as a login shell.</p>
<dt> RifsR (default) Rifs</p>
<dd> The internal field separator, used for splitting up the output of backquote commands for digestion as a list. On startup, <i>rc</i> assigns the list containing the characters space, tab, and newline to R$ifsR. R$ifs</p>
<dt> RpathR (alias) Rpath</p>
<dd> This is a list of directories to search in for commands. The empty string stands for the current directory. If neither R$PATH nor R$path is set at startup time, R$path assumes a default value suitable for your system. This is typically R(/usr/local/bin /usr/bin /usr/ucb /bin .)</p>
<dt> RpidR (default no-export) Rpid</p>
<dd> On startup, R$pid is initialized to the numeric process ID of the currently running <i>rc</i>.</p>
<dt> RpromptR (default) Rprompt</p>
<dd> This variable holds the two prompts (in list form, of course) that <i>rc</i> prints. R$<a href="/docs/linux/man/1-prompt/">prompt</a>(1) is printed before each command is read, and R$<a href="/docs/linux/man/2-prompt/">prompt</a>(2) is printed when input is expected to continue on the next line. <i>rc</i> sets R$prompt to R(&#8216;; &#8216; &#8221;) by default. The reason for this is that it enables an <i>rc</i> user to grab commands from previous lines using a mouse, and to present them to <i>rc</i> for re-interpretation; the semicolon prompt is simply ignored by <i>rc</i>. The null R$<a href="/docs/linux/man/2-prompt/">prompt</a>(2) also has its justification: an <i>rc</i> script, when typed interactively, will not leave R$<a href="/docs/linux/man/2-prompt/">prompt</a>(2)R&#8217;s R$<a href="/docs/linux/man/2-prompt/">prompt</a>(2) on the screen, and can therefore be grabbed by a mouse and placed directly into a file for use as a shell script, without further editing being necessary.</p>
<dt> RpromptR (function) Rprompt</p>
<dd> If this function is defined, then it gets executed every time <i>rc</i> is about to print R$<a href="/docs/linux/man/1-prompt/">prompt</a>(1)R. R$<a href="/docs/linux/man/1-prompt/">prompt</a>(1)</p>
<dt> RstatusR (no-export read-only) Rstatus</p>
<dd> The exit status of the last command. If the command exited with a numeric value, that number is the status. If the command died with a signal, the status is the name of that signal; if a core file was created, the string R&#8220;R+coreR&#8221; R&#8220;R+core R&#8220; is appended. The value of R$status for a pipeline is a list, with one entry, as above, for each process in the pipeline. For example, the command </p>
<pre>
Rls | wc
</pre>
<dt>
<dd> usually sets R$status to R(0 0)R. R(0 0)</p>
<dt> RversionR (default) Rversion</p>
<dd> On startup, the first element of this list variable is initialized to a string which identifies this version of <i>rc</i>. The second element is initialized to a string which can be found by <i><a href="/docs/linux/man/1-ident/">ident</a></i>(1) and the <i>what</i> command of <i><a href="/docs/linux/man/1-sccs/">sccs</a></i>(1).</dl>
<h2>FUNCTIONS</h2>
<p> <i>rc</i> functions are identical to <i>rc</i> scripts, except that they are stored in memory and are automatically exported into the environment. A shell function is declared as: </p>
<pre>
Rfn name { commands }
</pre>
<p> <i>rc</i> scans the definition until the close-brace, so the function can span more than one line. The function definition may be removed by typing </p>
<pre>
Rfn name
</pre>
<p> (One or more names may be specified. With an accompanying definition, all names receive the same definition. This is sometimes useful for assigning the same signal handler to many signals. Without a definition, all named functions are deleted.) When a function is executed, R$* is set to the arguments to that function for the duration of the command. Thus a reasonable definition for RlR, Rl a shorthand for <i><a href="/docs/linux/man/1-ls/">ls</a></i>(1), could be: </p>
<pre>
Rfn l { ls -FC $* }
</pre>
<p> but not </p>
<pre>
Rfn l { ls -FC } # WRONG
</pre>
<h2>INTERRUPTS AND SIGNALS</h2>
<p> <i>rc</i> recognizes a number of signals, and allows the user to define shell functions which act as signal handlers. <i>rc</i> by default traps RSIGINT when it is in interactive mode. RSIGQUIT and RSIGTERM are ignored, unless <i>rc</i> has been invoked with the R-d flag. However, user-defined signal handlers may be written for these and all other signals. The way to define a signal handler is to write a function by the name of the signal in lower case. Thus: </p>
<p>Rfn sighup<br />
{<br />
    echo hangup;<br />
    rm / tmp / rc$pid.*;<br />
    exit<br />
}</p>
<p> In addition to Unix signals, <i>rc</i> recognizes the artificial signal RSIGEXIT which occurs as <i>rc</i> is about to exit. </p>
<p> In order to remove a signal handler&#8217;s definition, remove it as though it were a regular function. For example: </p>
<pre>
Rfn sigint
</pre>
<p> returns the handler of RSIGINT to the default value. In order to ignore a signal, set the signal handler&#8217;s value to R{}R. R{} Thus: </p>
<pre>
Rfn sigint {}
</pre>
<p> causes RSIGINT to be ignored by the shell. Only signals that are being ignored are passed on to programs run by <i>rc</i>; signal functions are not exported. </p>
<p> On System V-based Unix systems, <i>rc</i> will not allow you to trap RSIGCLDR. RSIGCLD</p>
<h2>BUILTIN COMMANDS</h2>
<p> Builtin commands execute in the context of the shell, but otherwise behave exactly like other commands. Although <code>!</code>, <code>~</code> and <code>@</code> are not strictly speaking builtin commands, they can usually be used as such.</p>
<dl>
<dt><code>.</code> [<code>-i</code>] <i>file </i>[<i>arg &#8230;</i>]</p>
<dd> Reads <i>file</i> as input to <i>rc</i> and executes its contents. With a R-i flag, input is interactive. Thus from within a shell script, </p>
<pre>
R. -i /dev/tty
</pre>
<dt>
<dd> does the &#8220;right thing&#8221;.</p>
<dt><code>break</code></p>
<dd> Breaks from the innermost Rfor or RwhileR, Rwhile as in C. It is an error to invoke <code>break</code> outside of a loop. (Note that there is no <code>break</code> keyword between commands in Rswitch statements, unlike C.)</p>
<dt><code>builtin </code><i>command </i>[<i>arg &#8230;</i>]</p>
<dd> Executes the command ignoring any function definition of the same name. This command is present to allow functions with the same names as builtins to use the underlying builtin or binary. For example: </p>
<pre>
Rfn ls { builtin ls -FC $* }
</pre>
<dt>
<dd> is a reasonable way to pass a default set of arguments to <a href="/docs/linux/man/1-rlsr/">RlsR</a>(1), Rls whereas </p>
<pre>
Rfn ls { ls -FC $* } # WRONG
</pre>
<dt>
<dd> is a non-terminating recursion, which will cause Rrc to exhaust its stack space and (eventually) terminate if it is executed.</p>
<dt><code>cd </code>[<i>directory</i>]</p>
<dd> Changes the current directory to <i>directory</i>. The variable R$cdpath is searched for possible locations of <i>directory</i>, analogous to the searching of R$path for executable files. With no argument, <code>cd</code> changes the current directory to R$homeR. R$home</p>
<dt><code>echo </code>[<code>-n</code>] [<code>&#8212;</code>] [<i>arg &#8230;</i>]</p>
<dd> Prints its arguments to standard output, terminated by a newline. Arguments are separated by spaces. If the first argument is R-n no final newline is printed. If the first argument is R&#8211;R, R&#8211; then all other arguments are echoed literally. This is used for echoing a literal R-nR. R-n</p>
<dt><code>eval </code>[<i>list</i>]</p>
<dd> Concatenates the elements of <i>list</i> with spaces and feeds the resulting string to <i>rc</i> for re-scanning. This is the only time input is rescanned in <i>rc</i>.</p>
<dt><code>exec </code>[<i>arg &#8230;</i>]</p>
<dd> Replaces <i>rc</i> with the given command. If the exec contains only redirections, then these redirections apply to the current shell and the shell does not exit. For example, </p>
<pre>
Rexec &gt;[2] err.out
</pre>
<dt>
<dd> places further output to standard error in the file <i>err.out</i>.</p>
<dt><code>exit </code>[<i>status</i>]</p>
<dd> Cause the current shell to exit with the given exit <i>status</i>. If no argument is given, the current value of R$status is used.</p>
<dt><code>limit </code>[<code>-h</code>] [<i>resource </i>[<i>value</i>]]</p>
<dd> Similar to the <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1) <code>limit</code> builtin, this command operates upon the BSD-style resource limits of a process. The R-h flag displays/alters the hard limits. The resources which can be shown or altered are <code>cputime</code>, <code>filesize</code>, <code>datasize</code>, <code>stacksize</code>, <code>coredumpsize</code>, <code>memoryuse</code>, and, where supported, <code>descriptors</code>, <code>memoryuse</code>, <code>memoryrss</code>, <code>maxproc</code>, <code>memorylocked</code>, and <code>filelocks</code>. For example: </p>
<pre>
Rlimit coredumpsize 0
</pre>
<dt>
<dd> disables core dumps. To set a soft limit equal to the hard limit: </p>
<pre>
Rlimit `{limit -h datasize}
</pre>
<dt><code>newpgrp</code></p>
<dd> Puts <i>rc</i> into a new process group. This builtin is useful for making <i>rc</i> behave like a job-control shell in a hostile environment. One example is the NeXT Terminal program, which implicitly assumes that each shell it forks will put itself into a new process group.</p>
<dt><code>return </code>[<i>n</i>]</p>
<dd> Returns from the current function, with status <i>n</i>, where <i>n</i> is a valid exit status, or a list of them. Thus it is legal to have </p>
<pre>
Rreturn (sigpipe 1 2 3)
</pre>
<dt>
<dd> (This is commonly used to allow a function to return with the exit status of a previously executed pipeline of commands.) If <i>n</i> is omitted, then R$status is left unchanged. It is an error to invoke <code>return</code> when not inside a function.</p>
<dt><code>shift </code>[<i>n</i>]</p>
<dd> Deletes <i>n</i> elements from the beginning of R$* and shifts the other elements down by <i>n</i>. <i>n</i> defaults to 1.</p>
<dt><code>umask </code>[<i>mask</i>]</p>
<dd> Sets the current umask (see <i><a href="/docs/linux/man/2-umask/">umask</a></i>(2)) to the octal <i>mask</i>. If no argument is present, the current mask value is printed.</p>
<dt><code>wait </code>[<i>pid</i>]</p>
<dd> Waits for process with the specified <i>pid</i>, which must have been started by <i>rc</i>, to exit. If no <i>pid</i> is specified, <i>rc</i> waits for all its child processes to exit.</p>
<dt><code>whatis </code>[<code>-b</code>] [<code>-f</code>] [<code>-p</code>] [<code>-s</code>] [<code>-v</code>] [<code>&#8212;</code>] [<i>name &#8230;</i>]</p>
<dd> Prints a definition of the named objects. For builtins, Rbuiltin <i>foo</i> is printed; for functions, including signal handlers, their definitions are printed; for executable files, path names are printed; and for variables, their values are printed. The flags restrict output to builtins, functions, executable programs, signal handlers, and variables, respectively. If no <i>name</i>s are specified, <i>rc</i> lists all objects of that type. (This is not permitted for R-pR.) R-p Without arguments, Rwhatis is equivalent to Rwhatis -fvR, Rwhatis -fv and prints the values of all shell variables and functions.</p>
<dt>
<dd> Note that <code>whatis</code> output is suitable for input to <i>rc</i>; by saving the output of <code>whatis</code> in a file, it should be possible to recreate the state of <i>rc</i> by sourcing this file with a R. command. Another note: Rwhatis -s &gt; file cannot be used to store the state of <i>rc</i>&#8216;s signal handlers in a file, because builtins with redirections are run in a subshell, and <i>rc</i> always restores signal handlers to their default value after a Rfork()R. Rfork()</p>
<dt>
<dd> Since <code>whatis</code> uses <i><a href="/docs/linux/man/3-getopt/">getopt</a></i>(3) to parse its arguments, you can use the special argument R&#8211; to terminate its flags. This allows you to use names beginning with a dash, such as the <i><a href="/docs/linux/man/1-history/">history</a></i>(1) commands. For example, </p>
<pre>
Rwhatis -- -p
</pre>
</dl>
<h2>EXAMPLES</h2>
<p> The <code>shift</code> builtin only shifts R$*R. R$* This function can shift any variable (except R$lshiftR). R$lshift </p>
<p>Rfn lshift<br />
{<br />
    lshift = $ *;<br />
    *= $$1;<br />
    shift $lshift(2);<br />
    $lshift(1) = $ *<br />
}</p>
<p> With this definition in place, </p>
<pre>
Rwalrus = (shoes ships sealing-wax cabbages kings)
Rlshift walrus 3
Rwhatis walrus
</pre>
<p> prints </p>
<pre>
Rwalrus=(cabbages kings)
</pre>
<p> The R$^var operator flattens a list by separating each element with a space. This function allows the separator to be an arbitrary string. </p>
<p>Rfn lflat<br />
{<br />
    R lflat = $ *;<br />
    *= $$1<br />
        R while ()<br />
    {<br />
        R echo &#8211; n $1;<br />
        shift<br />
                    R ~$ # *<br />
                0 &amp;&amp;<br />
            break R echo &#8211; n $lflat(2)<br />
                               R<br />
    }</p>
<p> With this definition in place, </p>
<pre>
Rhops=(uunet mcvax ukc tlg)
Rlflat hops !
</pre>
<p> prints (with no final newline) </p>
<pre>
Ruunet!mcvax!ukc!tlg
</pre>
<h2>EXIT STATUS</h2>
<p> The exit status of <i>rc</i> is normally the same as that of the last command executed. If the last command was a pipeline, <i>rc</i> exits R0 if every command in the pipeline did; otherwise it exits R1R. R1 </p>
<p> <i>rc</i> can be made to exit with a particular status using the <code>exit</code> builtin.</p>
<h2>GRAMMAR</h2>
<p> Here is <i>rc</i>&#8216;s grammar, edited to remove semantic actions. </p>
<p>R % term ANDAND BACKBACK BANG CASE COUNT DUP ELSE END FLAT FN FOR IF IN % term OROR PIPE REDIR SUB SUBSHELL SWITCH TWIDDLE WHILE WORD HUH % left WHILE &#8216;)&#8217; ELSE % left ANDAND OROR &#8216;
&#8217; % left BANG SUBSHELL % left PIPE % right &#8216;$&#8217; % left SUB % start rc % %<br />
        rc : line end |<br />
    error end<br />
        end : END /* EOF */<br />
              |<br />
              &#8216;
&#8217; cmdsa : cmd &#8216;;&#8217; | cmd &#8216;&amp;&#8217; line : cmd | cmdsa line body : cmd | cmdsan body cmdsan : cmdsa | cmd &#8216;
&#8217; brace : &#8216;{&#8216; body &#8216;}&#8217; paren : &#8216;(&#8216; body &#8216;)&#8217; assign : first &#8216;=&#8217; word epilog : /* empty */ | redir epilog redir : DUP | REDIR word case : CASE words &#8216;;&#8217; | CASE words &#8216;
&#8217; cbody : cmd | case cbody | cmdsan cbody iftail : cmd % prec ELSE | brace ELSE optnl cmd cmd : /* empty */ % prec WHILE | simple | brace epilog | IF paren optnl iftail | FOR &#8216;(&#8216; word IN words &#8216;)&#8217; optnl cmd | FOR &#8216;(&#8216; word &#8216;)&#8217; optnl cmd | WHILE paren optnl cmd | SWITCH &#8216;(&#8216; word &#8216;)&#8217; optnl &#8216;{&#8216; cbody &#8216;}&#8217; | TWIDDLE optcaret word words | cmd ANDAND optnl cmd | cmd OROR optnl cmd | cmd PIPE optnl cmd | redir cmd % prec BANG | assign cmd % prec BANG | BANG optcaret cmd | SUBSHELL optcaret cmd | FN words brace | FN words optcaret : /* empty */ | &#8216;^&#8217; simple : first | simple word | simple redir first : comword | first &#8216;^&#8217; sword sword : comword | keyword word : sword | word &#8216;^&#8217; sword comword : &#8216;$&#8217; sword | &#8216;$&#8217; sword SUB words &#8216;)&#8217; | COUNT sword | FLAT sword | &#8216;`&#8217; sword | &#8216;`&#8217; brace | BACKBACK word brace | BACKBACK word sword | &#8216;(&#8216; words &#8216;)&#8217; | REDIR brace | WORD keyword : FOR | IN | WHILE | IF | SWITCH | FN | ELSE | CASE | TWIDDLE | BANG | SUBSHELL words : /* empty */ | words word optnl : /* empty */ | optnl &#8216;
&#8217;</p>
<h2>FILES</h2>
<p> R$HOME/.rcrcR, R$HOME/.rcrc R/tmp/rc*R, R/tmp/rc* R/dev/null</p>
<h2>CREDITS</h2>
<p> <i>rc</i> was written by Byron Rakitzis, with valuable help from Paul Haahr, Hugh Redelmeier and David Sanderson. The design of this shell was copied from the <i>rc</i> that Tom Duff wrote at Bell Labs.</p>
<h2>BUGS</h2>
<p> There is a compile-time limit on the number of R; separated commands in a line: usually 500. This is sometimes a problem for automatically generated scripts: substituting the newline character for R; avoids the limit. </p>
<p> On modern systems that support R/dev/fd or R/proc/self/fdR, R/proc/self/fd R&lt;{foo} style redirection is implemented that way. However, on older systems it is implemented with named pipes. Allegedly, it is sometimes possible to foil <i>rc</i> into removing the FIFO it places in R/tmp prematurely, or it is even possible to cause <i>rc</i> to hang. (The current maintainer has never seen this, but then he doesn&#8217;t use systems which lack R/dev/fd any more. If anybody can reproduce this problem, please let the maintainer know.) </p>
<p> The <code>echo</code> command does not need to be a builtin. It is one for reasons of performance and portability (of <i>rc</i> scripts). </p>
<p> There should be a way to avoid exporting a variable. </p>
<p> Extra parentheses around a R~ expression or a R! expression are a syntax error. Thus, this code is illegal. </p>
<pre>
Rwhile ((~ $1 -*) &amp;&amp; (! ~ $1 --)) { ...
</pre>
<dl>
<dt>The redundant inner parentheses must be omitted.</p>
<dd></dl>
<p> Variable subscripting cannot be used in here documents. </p>
<p> The Rlimit builtin silently ignores extra arguments. </p>
<p> Backquote substitution never produces empty strings &#8211; multiple consecutive occurrences of the separator are treated the same as a single occurrence. </p>
<pre><code>
Rifs = !
{
    x = `{echo - n a !!b};
    whatis x
}
Rx = (a b) #NOT x = (a '' b)
                        Bug reports should be mailed to
                            R&lt;toby[at] paccrat.org&gt;
                                R.R&lt;toby[at] paccrat.org&gt;
</code></pre>
<h2>INCOMPATIBILITIES</h2>
<p> Here is a list of features which distinguish this incarnation of <i>rc</i> from the one described in the Bell Labs manual pages: </p>
<p> The Tenth Edition <i>rc</i> does not have the <code>else</code> keyword. Instead, <code>if</code> is optionally followed by an <code>if not</code> clause which is executed if the preceding <code>if</code> test does not succeed. </p>
<p> Backquotes are slightly different in Tenth Edition <i>rc</i>: a backquote must always be followed by a left-brace. This restriction is not present for single-word commands in this <i>rc</i>. </p>
<p> For R. <i>file</i>, the Tenth Edition <i>rc</i> searches R$path for <i>file</i>. This <i>rc</i> does not, since it is not considered useful. </p>
<p> The list flattening operator, R$^fooR, R$^foo is spelt R$&quot;foo in those versions of the Bell Labs <i>rc</i> which have it. </p>
<p> The following are all new with this version of <i>rc</i>: The R-n flag, here strings (they facilitate exporting of functions with here documents into the environment), the <code>return</code> and <code>break</code> keywords, the <code>echo</code> builtin, the Rbqstatus and Rversion variables, the support for the GNU <i><a href="/docs/linux/man/3-readline/">readline</a></i>(3) library, and the support for the Rprompt function. This <i>rc</i> also sets R$0 to the name of a function being executed/file being sourced.</p>
<h2>SEE ALSO</h2>
<p> &#8220;rc &#8212; A Shell for Plan 9 and UNIX Systems&#8221;, Unix Research System, Tenth Edition, Volume 2. (Saunders College Publishing) </p>
<p> R<a rel="nofollow" href="http://static.tobold.org/rc/rc-duff.htmlR,">http://static.tobold.org/rc/rc-duff.htmlR,</a> R<a rel="nofollow" href="http://static.tobold.org/rc/rc-duff.html">http://static.tobold.org/rc/rc-duff.html</a> an updated version of the above paper. </p>
<p> <i><a href="/docs/linux/man/1-history/">history</a></i>(1) </p>
<h2>Index</h2>
