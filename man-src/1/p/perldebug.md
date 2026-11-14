---
title: "perldebug(1)"
name: "perldebug"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perldebug/"
description: "perldebug – Perl debugging"
---

<h2 class="name">NAME</h2>
<p> perldebug &#8211; Perl debugging </p>
<h2>DESCRIPTION</h2>
<p> First of all, have you tried using <tt>&quot;use strict;&quot;</tt> and <tt>&quot;use warnings;&quot;</tt>? </p>
<p> If you&#8217;re new to the Perl debugger, you may prefer to read perldebtut, which is a tutorial introduction to the debugger. </p>
<p> If you&#8217;re looking for the nitty gritty details of how the debugger is <i>implemented</i>, you may prefer to read perldebguts.</p>
<h2>The Perl Debugger</h2>
<p> If you invoke Perl with the <code>-d</code> switch, your script runs under the Perl source debugger. This works like an interactive Perl environment, prompting for debugger commands that let you examine source code, set breakpoints, get stack backtraces, change the values of variables, etc. This is so convenient that you often fire up the debugger all by itself just to test out Perl constructs interactively to see what they do. For example: </p>
<pre>
    $ perl -d -e 42
</pre>
<p> In Perl, the debugger is not a separate program the way it usually is in the typical compiled environment. Instead, the <code>-d</code> flag tells the compiler to insert source information into the parse trees it&#8217;s about to hand off to the interpreter. That means your code must first compile correctly for the debugger to work on it. Then when the interpreter starts up, it preloads a special Perl library file containing the debugger. </p>
<p> The program will halt <i>right before</i> the first run-time executable statement (but see below regarding compile-time statements) and ask you to enter a debugger command. Contrary to popular expectations, whenever the debugger halts and shows you a line of code, it always displays the line it&#8217;s <i>about</i> to execute, rather than the one it has just executed. </p>
<p> Any command not recognized by the debugger is directly executed (<tt>&quot;eval&quot;</tt>&#8216;d) as Perl code in the current package. (The debugger uses the <font SIZE="-1">DB</font> package for keeping its own state information.) </p>
<p> Note that the said <tt>&quot;eval&quot;</tt> is bound by an implicit scope. As a result any newly introduced lexical variable or any modified capture buffer content is lost after the eval. The debugger is a nice environment to learn Perl, but if you interactively experiment using material which should be in the same scope, stuff it in one line. </p>
<p> For any text entered at the debugger prompt, leading and trailing whitespace is first stripped before further processing. If a debugger command coincides with some function in your own program, merely precede the function with something that doesn&#8217;t look like a debugger command, such as a leading <tt>&quot;;&quot;</tt> or perhaps a <tt>&quot;+&quot;</tt>, or by wrapping it with parentheses or braces.</p>
<h3>Calling the Debugger</h3>
<p> There are several ways to call the debugger:</p>
<dl>
<dt>perl -d program_name</p>
<dd> On the given program identified by <tt>&quot;program_name&quot;</tt>.</p>
<dt>perl -d -e 0</p>
<dd> Interactively supply an arbitrary <tt>&quot;expression&quot;</tt> using <tt>&quot;-e&quot;</tt>.</p>
<dt>perl -d:ptkdb program_name</p>
<dd> Debug a given program via the <tt>&quot;Devel::ptkdb&quot;</tt> <font SIZE="-1">GUI.</font></p>
<dt>perl -dt threaded_program_name</p>
<dd> Debug a given program using threads (experimental).</dl>
<h3>Debugger Commands</h3>
<p> The interactive debugger understands the following commands:</p>
<dl>
<dt>h</p>
<dd> Prints out a summary help message</p>
<dt>h [command]</p>
<dd> Prints out a help message for the given debugger command.</p>
<dt>h h</p>
<dd> The special argument of <tt>&quot;h h&quot;</tt> produces the entire help page, which is quite long. </p>
<p> If the output of the <tt>&quot;h h&quot;</tt> command (or any command, for that matter) scrolls past your screen, precede the command with a leading pipe symbol so that it&#8217;s run through your pager, as in </p>
<pre>
    DB&gt; |h h
</pre>
<p> You may change the pager which is used via <tt>&quot;o pager=...&quot;</tt> command.</p>
<dt>p expr</p>
<dd> Same as <tt>&quot;print {$DB::OUT} expr&quot;</tt> in the current package. In particular, because this is just Perl&#8217;s own <tt>&quot;print&quot;</tt> function, this means that nested data structures and objects are not dumped, unlike with the <tt>&quot;x&quot;</tt> command. </p>
<p> The <tt>&quot;DB::OUT&quot;</tt> filehandle is opened to <i>/dev/tty</i>, regardless of where <font SIZE="-1">STDOUT</font> may be redirected to.</p>
<dt>x [maxdepth] expr</p>
<dd> Evaluates its expression in list context and dumps out the result in a pretty-printed fashion. Nested data structures are printed out recursively, unlike the real <tt>&quot;print&quot;</tt> function in Perl. When dumping hashes, you&#8217;ll probably prefer &#8216;x \%h&#8217; rather than &#8216;x <tt>%h</tt>&#8216;. See Dumpvalue if you&#8217;d like to do this yourself. </p>
<p> The output format is governed by multiple options described under &#8220;Configurable Options&#8221;. </p>
<p> If the <tt>&quot;maxdepth&quot;</tt> is included, it must be a numeral <i>N</i>; the value is dumped only <i>N</i> levels deep, as if the <tt>&quot;dumpDepth&quot;</tt> option had been temporarily set to <i>N</i>.</p>
<dt>V [pkg [vars]]</p>
<dd> Display all (or some) variables in package (defaulting to <tt>&quot;main&quot;</tt>) using a data pretty-printer (hashes show their keys and values so you see what&#8217;s what, control characters are made printable, etc.). Make sure you don&#8217;t put the type specifier (like <tt>&quot;$&quot;</tt>) there, just the symbol names, like this: </p>
<pre>
    V DB filename line
</pre>
<p> Use <tt>&quot;~pattern&quot;</tt> and <tt>&quot;!pattern&quot;</tt> for positive and negative regexes. </p>
<p> This is similar to calling the <tt>&quot;x&quot;</tt> command on each applicable var.</p>
<dt>X [vars]</p>
<dd> Same as <tt>&quot;V currentpackage [vars]&quot;</tt>.</p>
<dt>y [level [vars]]</p>
<dd> Display all (or some) lexical variables (mnemonic: <tt>&quot;mY&quot;</tt> variables) in the current scope or <i>level</i> scopes higher. You can limit the variables that you see with <i>vars</i> which works exactly as it does for the <tt>&quot;V&quot;</tt> and <tt>&quot;X&quot;</tt> commands. Requires the <tt>&quot;PadWalker&quot;</tt> module version 0.08 or higher; will warn if this isn&#8217;t installed. Output is pretty-printed in the same style as for <tt>&quot;V&quot;</tt> and the format is controlled by the same options.</p>
<dt>T</p>
<dd> Produce a stack backtrace. See below for details on its output.</p>
<dt>s [expr]</p>
<dd> Single step. Executes until the beginning of another statement, descending into subroutine calls. If an expression is supplied that includes function calls, it too will be single-stepped.</p>
<dt>n [expr]</p>
<dd> Next. Executes over subroutine calls, until the beginning of the next statement. If an expression is supplied that includes function calls, those functions will be executed with stops before each statement.</p>
<dt>r</p>
<dd> Continue until the return from the current subroutine. Dump the return value if the <tt>&quot;PrintRet&quot;</tt> option is set (default).</p>
<dt>&lt;<font SIZE="-1">CR</font>&gt;</p>
<dd> Repeat last <tt>&quot;n&quot;</tt> or <tt>&quot;s&quot;</tt> command.</p>
<dt>c [line|sub]</p>
<dd> Continue, optionally inserting a one-time-only breakpoint at the specified line or subroutine.</p>
<dt>l</p>
<dd> List next window of lines.</p>
<dt>l min+incr</p>
<dd> List <tt>&quot;incr+1&quot;</tt> lines starting at <tt>&quot;min&quot;</tt>.</p>
<dt>l min-max</p>
<dd> List lines <tt>&quot;min&quot;</tt> through <tt>&quot;max&quot;</tt>. <tt>&quot;l -&quot;</tt> is synonymous to <tt>&quot;-&quot;</tt>.</p>
<dt>l line</p>
<dd> List a single line.</p>
<dt>l subname</p>
<dd> List first window of lines from subroutine. <i>subname</i> may be a variable that contains a code reference.</p>
<dt>&#8211;</p>
<dd> List previous window of lines.</p>
<dt>v [line]</p>
<dd> View a few lines of code around the current line.</p>
<dt>.</p>
<dd> Return the internal debugger pointer to the line last executed, and print out that line.</p>
<dt>f filename</p>
<dd> Switch to viewing a different file or <tt>&quot;eval&quot;</tt> statement. If <i>filename</i> is not a full pathname found in the values of <tt>%INC</tt>, it is considered a regex. </p>
<p> <tt>&quot;eval&quot;</tt>ed strings (when accessible) are considered to be filenames: <tt>&quot;f (eval 7)&quot;</tt> and <tt>&quot;f eval 7&quot;</tt> access the body of the 7th <tt>&quot;eval&quot;</tt>ed string (in the order of execution). The bodies of the currently executed <tt>&quot;eval&quot;</tt> and of <tt>&quot;eval&quot;</tt>ed strings that define subroutines are saved and thus accessible.</p>
<dt>/pattern/</p>
<dd> Search forwards for pattern (a Perl regex); final / is optional. The search is case-insensitive by default.</p>
<dt>?pattern?</p>
<dd> Search backwards for pattern; final ? is optional. The search is case-insensitive by default.</p>
<dt>L [abw]</p>
<dd> List (default all) actions, breakpoints and watch expressions</p>
<dt>S [[!]regex]</p>
<dd> List subroutine names [not] matching the regex.</p>
<dt>t [n]</p>
<dd> Toggle trace mode (see also the <tt>&quot;AutoTrace&quot;</tt> option). Optional argument is the maximum number of levels to trace below the current one; anything deeper than that will be silent.</p>
<dt>t [n] expr</p>
<dd> Trace through execution of <tt>&quot;expr&quot;</tt>. Optional first argument is the maximum number of levels to trace below the current one; anything deeper than that will be silent. See &#8220;Frame Listing Output Examples&#8221; in perldebguts for examples.</p>
<dt>b</p>
<dd> Sets breakpoint on current line</p>
<dt>b [line] [condition]</p>
<dd> Set a breakpoint before the given line. If a condition is specified, it&#8217;s evaluated each time the statement is reached: a breakpoint is taken only if the condition is true. Breakpoints may only be set on lines that begin an executable statement. Conditions don&#8217;t use <tt>&quot;if&quot;</tt>: </p>
<pre>
    b 237 $x &gt; 30
    b 237 ++$count237 &lt; 11
    b 33 /pattern/i
</pre>
<p> If the line number is <tt>&quot;.&quot;</tt>, sets a breakpoint on the current line: </p>
<pre>
    b . $n &gt; 100
</pre>
<dt>b [file]:[line] [condition]</p>
<dd> Set a breakpoint before the given line in a (possibly different) file. If a condition is specified, it&#8217;s evaluated each time the statement is reached: a breakpoint is taken only if the condition is true. Breakpoints may only be set on lines that begin an executable statement. Conditions don&#8217;t use <tt>&quot;if&quot;</tt>: </p>
<pre>
    b lib/MyModule.pm:237 $x &gt; 30
    b /usr/lib/perl5/site_perl/CGI.pm:100 ++$count100 &lt; 11
</pre>
<dt>b subname [condition]</p>
<dd> Set a breakpoint before the first line of the named subroutine. <i>subname</i> may be a variable containing a code reference (in this case <i>condition</i> is not supported).</p>
<dt>b postpone subname [condition]</p>
<dd> Set a breakpoint at first line of subroutine after it is compiled.</p>
<dt>b load filename</p>
<dd> Set a breakpoint before the first executed line of the <i>filename</i>, which should be a full pathname found amongst the <tt>%INC</tt> values.</p>
<dt>b compile subname</p>
<dd> Sets a breakpoint before the first statement executed after the specified subroutine is compiled.</p>
<dt>B line</p>
<dd> Delete a breakpoint from the specified <i>line</i>.</p>
<dt>B *</p>
<dd> Delete all installed breakpoints.</p>
<dt>disable [file]:[line]</p>
<dd> Disable the breakpoint so it won&#8217;t stop the execution of the program. Breakpoints are enabled by default and can be re-enabled using the <tt>&quot;enable&quot;</tt> command.</p>
<dt>disable [line]</p>
<dd> Disable the breakpoint so it won&#8217;t stop the execution of the program. Breakpoints are enabled by default and can be re-enabled using the <tt>&quot;enable&quot;</tt> command. </p>
<p> This is done for a breakpoint in the current file.</p>
<dt>enable [file]:[line]</p>
<dd> Enable the breakpoint so it will stop the execution of the program.</p>
<dt>enable [line]</p>
<dd> Enable the breakpoint so it will stop the execution of the program. </p>
<p> This is done for a breakpoint in the current file.</p>
<dt>a [line] command</p>
<dd> Set an action to be done before the line is executed. If <i>line</i> is omitted, set an action on the line about to be executed. The sequence of steps taken by the debugger is </p>
<pre>
  1. check for a breakpoint at this line
  2. print the line if necessary (tracing)
  3. do any actions associated with that line
  4. prompt user if at a breakpoint or in single-step
  5. evaluate line
</pre>
<p> For example, this will print out <tt>$foo</tt> every time line 53 is passed: </p>
<pre>
    a 53 print &quot;DB FOUND $foo
&quot;
</pre>
<dt>A line</p>
<dd> Delete an action from the specified line.</p>
<dt>A *</p>
<dd> Delete all installed actions.</p>
<dt>w expr</p>
<dd> Add a global watch-expression. Whenever a watched global changes the debugger will stop and display the old and new values.</p>
<dt>W expr</p>
<dd> Delete watch-expression</p>
<dt>W *</p>
<dd> Delete all watch-expressions.</p>
<dt>o</p>
<dd> Display all options.</p>
<dt>o booloption &#8230;</p>
<dd> Set each listed Boolean option to the value <tt>1</tt>.</p>
<dt>o anyoption? &#8230;</p>
<dd> Print out the value of one or more options.</p>
<dt>o option=value &#8230;</p>
<dd> Set the value of one or more options. If the value has internal whitespace, it should be quoted. For example, you could set <tt>&quot;o pager=&quot;less -MQeicsNfr&quot;&quot;</tt> to call <code>less</code> with those specific options. You may use either single or double quotes, but if you do, you must escape any embedded instances of same sort of quote you began with, as well as any escaping any escapes that immediately precede that quote but which are not meant to escape the quote itself. In other words, you follow single-quoting rules irrespective of the quote; eg: <tt>&quot;o option='this isn\'t bad'&quot;</tt> or <tt>&quot;o option=&quot;She said, \&quot;Isn't it?\&quot;&quot;&quot;</tt>. </p>
<p> For historical reasons, the <tt>&quot;=value&quot;</tt> is optional, but defaults to 1 only where it is safe to do so&#8212;that is, mostly for Boolean options. It is always better to assign a specific value using <tt>&quot;=&quot;</tt>. The <tt>&quot;option&quot;</tt> can be abbreviated, but for clarity probably should not be. Several options can be set together. See &#8220;Configurable Options&#8221; for a list of these.</p>
<dt>&lt; ?</p>
<dd> List out all pre-prompt Perl command actions.</p>
<dt>&lt; [ command ]</p>
<dd> Set an action (Perl command) to happen before every debugger prompt. A multi-line command may be entered by backslashing the newlines.</p>
<dt>&lt; *</p>
<dd> Delete all pre-prompt Perl command actions.</p>
<dt>&lt;&lt; command</p>
<dd> Add an action (Perl command) to happen before every debugger prompt. A multi-line command may be entered by backwhacking the newlines.</p>
<dt>&gt; ?</p>
<dd> List out post-prompt Perl command actions.</p>
<dt>&gt; command</p>
<dd> Set an action (Perl command) to happen after the prompt when you&#8217;ve just given a command to return to executing the script. A multi-line command may be entered by backslashing the newlines (we bet you couldn&#8217;t have guessed this by now).</p>
<dt>&gt; *</p>
<dd> Delete all post-prompt Perl command actions.</p>
<dt>&gt;&gt; command</p>
<dd> Adds an action (Perl command) to happen after the prompt when you&#8217;ve just given a command to return to executing the script. A multi-line command may be entered by backslashing the newlines.</p>
<dt>{ ?</p>
<dd> List out pre-prompt debugger commands.</p>
<dt>{ [ command ]</p>
<dd> Set an action (debugger command) to happen before every debugger prompt. A multi-line command may be entered in the customary fashion. </p>
<p> Because this command is in some senses new, a warning is issued if you appear to have accidentally entered a block instead. If that&#8217;s what you mean to do, write it as with <tt>&quot;;{ ... }&quot;</tt> or even <tt>&quot;do { ... }&quot;</tt>.</p>
<dt>{ *</p>
<dd> Delete all pre-prompt debugger commands.</p>
<dt>&#123;&#123; command</p>
<dd> Add an action (debugger command) to happen before every debugger prompt. A multi-line command may be entered, if you can guess how: see above.</p>
<dt>! number</p>
<dd> Redo a previous command (defaults to the previous command).</p>
<dt>! -number</p>
<dd> Redo number&#8217;th previous command.</p>
<dt>! pattern</p>
<dd> Redo last command that started with pattern. See <tt>&quot;o recallCommand&quot;</tt>, too.</p>
<dt>!! cmd</p>
<dd> Run cmd in a subprocess (reads from <font SIZE="-1">DB::IN,</font> writes to <font SIZE="-1">DB::OUT</font>) See <tt>&quot;o shellBang&quot;</tt>, also. Note that the user&#8217;s current shell (well, their <tt>$ENV{SHELL}</tt> variable) will be used, which can interfere with proper interpretation of exit status or signal and coredump information.</p>
<dt>source file</p>
<dd> Read and execute debugger commands from <i>file</i>. <i>file</i> may itself contain <tt>&quot;source&quot;</tt> commands.</p>
<dt>H -number</p>
<dd> Display last n commands. Only commands longer than one character are listed. If <i>number</i> is omitted, list them all.</p>
<dt>q or ^D</p>
<dd> Quit. (&#8220;quit&#8221; doesn&#8217;t work for this, unless you&#8217;ve made an alias) This is the only supported way to exit the debugger, though typing <tt>&quot;exit&quot;</tt> twice might work. </p>
<p> Set the <tt>&quot;inhibit_exit&quot;</tt> option to 0 if you want to be able to step off the end the script. You may also need to set <tt>$finished</tt> to 0 if you want to step through global destruction.</p>
<dt>R</p>
<dd> Restart the debugger by <tt>&quot;exec()&quot;</tt>ing a new session. We try to maintain your history across this, but internal settings and command-line options may be lost. </p>
<p> The following setting are currently preserved: history, breakpoints, actions, debugger options, and the Perl command-line options <code>-w</code>, <code>-I</code>, and <code>-e</code>.</p>
<dt>|dbcmd</p>
<dd> Run the debugger command, piping <font SIZE="-1">DB::OUT</font> into your current pager.</p>
<dt>||dbcmd</p>
<dd> Same as <tt>&quot;|dbcmd&quot;</tt> but <font SIZE="-1">DB::OUT</font> is temporarily <tt>&quot;select&quot;</tt>ed as well.</p>
<dt>= [alias value]</p>
<dd> Define a command alias, like </p>
<pre>
    = quit q
</pre>
<p> or list current aliases.</p>
<dt>command</p>
<dd> Execute command as a Perl statement. A trailing semicolon will be supplied. If the Perl statement would otherwise be confused for a Perl debugger, use a leading semicolon, too.</p>
<dt>m expr</p>
<dd> List which methods may be called on the result of the evaluated expression. The expression may evaluated to a reference to a blessed object, or to a package name.</p>
<dt>M</p>
<dd> Display all loaded modules and their versions.</p>
<dt>man [manpage]</p>
<dd> Despite its name, this calls your system&#8217;s default documentation viewer on the given page, or on the viewer itself if <i>manpage</i> is omitted. If that viewer is <code>man</code>, the current <tt>&quot;Config&quot;</tt> information is used to invoke <code>man</code> using the proper <font SIZE="-1">MANPATH</font> or <code>-M</code> <i>manpath</i> option. Failed lookups of the form <tt>&quot;XXX&quot;</tt> that match known manpages of the form <i>perlXXX</i> will be retried. This lets you type <tt>&quot;man debug&quot;</tt> or <tt>&quot;man op&quot;</tt> from the debugger. </p>
<p> On systems traditionally bereft of a usable <code>man</code> command, the debugger invokes <code>perldoc</code>. Occasionally this determination is incorrect due to recalcitrant vendors or rather more felicitously, to enterprising users. If you fall into either category, just manually set the <tt>$DB::doccmd</tt> variable to whatever viewer to view the Perl documentation on your system. This may be set in an rc file, or through direct assignment. We&#8217;re still waiting for a working example of something along the lines of: </p>
<pre>
    $DB::doccmd = 'netscape -remote <a rel="nofollow" href="http://something.here/';">http://something.here/';</a>
</pre>
</dl>
<h3>Configurable Options</h3>
<p> The debugger has numerous options settable using the <tt>&quot;o&quot;</tt> command, either interactively or from the environment or an rc file. (./.perldb or ~/.perldb under Unix.)</p>
<dl>
<dt>&quot;recallCommand&quot;, &quot;ShellBang&quot;</p>
<dd> The characters used to recall a command or spawn a shell. By default, both are set to <tt>&quot;!&quot;</tt>, which is unfortunate.</p>
<dt>&quot;pager&quot;</p>
<dd> Program to use for output of pager-piped commands (those beginning with a <tt>&quot;|&quot;</tt> character.) By default, <tt>$ENV{PAGER}</tt> will be used. Because the debugger uses your current terminal characteristics for bold and underlining, if the chosen pager does not pass escape sequences through unchanged, the output of some debugger commands will not be readable when sent through the pager.</p>
<dt>&quot;tkRunning&quot;</p>
<dd> Run Tk while prompting (with ReadLine).</p>
<dt>&quot;signalLevel&quot;, &quot;warnLevel&quot;, &quot;dieLevel&quot;</p>
<dd> Level of verbosity. By default, the debugger leaves your exceptions and warnings alone, because altering them can break correctly running programs. It will attempt to print a message when uncaught <font SIZE="-1">INT, BUS,</font> or <font SIZE="-1">SEGV</font> signals arrive. (But see the mention of signals in &#8220;<font SIZE="-1">BUGS&#8221;</font> below.) </p>
<p> To disable this default safe mode, set these values to something higher than 0. At a level of 1, you get backtraces upon receiving any kind of warning (this is often annoying) or exception (this is often valuable). Unfortunately, the debugger cannot discern fatal exceptions from non-fatal ones. If <tt>&quot;dieLevel&quot;</tt> is even 1, then your non-fatal exceptions are also traced and unceremoniously altered if they came from <tt>&quot;eval'ed&quot;</tt> strings or from any kind of <tt>&quot;eval&quot;</tt> within modules you&#8217;re attempting to load. If <tt>&quot;dieLevel&quot;</tt> is 2, the debugger doesn&#8217;t care where they came from: It usurps your exception handler and prints out a trace, then modifies all exceptions with its own embellishments. This may perhaps be useful for some tracing purposes, but tends to hopelessly destroy any program that takes its exception handling seriously.</p>
<dt>&quot;AutoTrace&quot;</p>
<dd> Trace mode (similar to <tt>&quot;t&quot;</tt> command, but can be put into <tt>&quot;PERLDB_OPTS&quot;</tt>).</p>
<dt>&quot;LineInfo&quot;</p>
<dd> File or pipe to print line number info to. If it is a pipe (say, <tt>&quot;|visual_perl_db&quot;</tt>), then a short message is used. This is the mechanism used to interact with a slave editor or visual debugger, such as the special <tt>&quot;vi&quot;</tt> or <tt>&quot;emacs&quot;</tt> hooks, or the <tt>&quot;ddd&quot;</tt> graphical debugger.</p>
<dt>&quot;inhibit_exit&quot;</p>
<dd> If 0, allows <i>stepping off</i> the end of the script.</p>
<dt>&quot;PrintRet&quot;</p>
<dd> Print return value after <tt>&quot;r&quot;</tt> command if set (default).</p>
<dt>&quot;ornaments&quot;</p>
<dd> Affects screen appearance of the command line (see Term::ReadLine). There is currently no way to disable these, which can render some output illegible on some displays, or with some pagers. This is considered a bug.</p>
<dt>&quot;frame&quot;</p>
<dd> Affects the printing of messages upon entry and exit from subroutines. If <tt>&quot;frame &amp; 2&quot;</tt> is false, messages are printed on entry only. (Printing on exit might be useful if interspersed with other messages.) </p>
<p> If <tt>&quot;frame &amp; 4&quot;</tt>, arguments to functions are printed, plus context and caller info. If <tt>&quot;frame &amp; 8&quot;</tt>, overloaded <tt>&quot;stringify&quot;</tt> and <tt>&quot;tie&quot;</tt>d <tt>&quot;FETCH&quot;</tt> is enabled on the printed arguments. If <tt>&quot;frame &amp; 16&quot;</tt>, the return value from the subroutine is printed. </p>
<p> The length at which the argument list is truncated is governed by the next option:</p>
<dt>&quot;maxTraceLen&quot;</p>
<dd> Length to truncate the argument list when the <tt>&quot;frame&quot;</tt> option&#8217;s bit 4 is set.</p>
<dt>&quot;windowSize&quot;</p>
<dd> Change the size of code list window (default is 10 lines).</dl>
<p> The following options affect what happens with <tt>&quot;V&quot;</tt>, <tt>&quot;X&quot;</tt>, and <tt>&quot;x&quot;</tt> commands:</p>
<dl>
<dt>&quot;arrayDepth&quot;, &quot;hashDepth&quot;</p>
<dd> Print only first N elements (&#8221; for all).</p>
<dt>&quot;dumpDepth&quot;</p>
<dd> Limit recursion depth to N levels when dumping structures. Negative values are interpreted as infinity. Default: infinity.</p>
<dt>&quot;compactDump&quot;, &quot;veryCompact&quot;</p>
<dd> Change the style of array and hash output. If <tt>&quot;compactDump&quot;</tt>, short array may be printed on one line.</p>
<dt>&quot;globPrint&quot;</p>
<dd> Whether to print contents of globs.</p>
<dt>&quot;DumpDBFiles&quot;</p>
<dd> Dump arrays holding debugged files.</p>
<dt>&quot;DumpPackages&quot;</p>
<dd> Dump symbol tables of packages.</p>
<dt>&quot;DumpReused&quot;</p>
<dd> Dump contents of &#8220;reused&#8221; addresses.</p>
<dt>&quot;quote&quot;, &quot;HighBit&quot;, &quot;undefPrint&quot;</p>
<dd> Change the style of string dump. The default value for <tt>&quot;quote&quot;</tt> is <tt>&quot;auto&quot;</tt>; one can enable double-quotish or single-quotish format by setting it to <tt>&quot;&quot;&quot;</tt> or <tt>&quot;'&quot;</tt>, respectively. By default, characters with their high bit set are printed verbatim.</p>
<dt>&quot;UsageOnly&quot;</p>
<dd> Rudimentary per-package memory usage dump. Calculates total size of strings found in variables in the package. This does not include lexicals in a module&#8217;s file scope, or lost in closures.</p>
<dt>&quot;HistFile&quot;</p>
<dd> The path of the file from which the history (assuming a usable Term::ReadLine backend) will be read on the debugger&#8217;s startup, and to which it will be saved on shutdown (for persistence across sessions). Similar in concept to Bash&#8217;s <tt>&quot;.bash_history&quot;</tt> file.</p>
<dt>&quot;HistSize&quot;</p>
<dd> The count of the saved lines in the history (assuming <tt>&quot;HistFile&quot;</tt> above).</dl>
<p> After the rc file is read, the debugger reads the <tt>$ENV{PERLDB_OPTS}</tt> environment variable and parses this as the remainder of a &#8220;O &#8230;&#8221; line as one might enter at the debugger prompt. You may place the initialization options <tt>&quot;TTY&quot;</tt>, <tt>&quot;noTTY&quot;</tt>, <tt>&quot;ReadLine&quot;</tt>, and <tt>&quot;NonStop&quot;</tt> there. </p>
<p> If your rc file contains: </p>
<pre>
  parse_options(&quot;NonStop=1 LineInfo=db.out AutoTrace&quot;);
</pre>
<p> then your script will run without human intervention, putting trace information into the file <i>db.out</i>. (If you interrupt it, you&#8217;d better reset <tt>&quot;LineInfo&quot;</tt> to <i>/dev/tty</i> if you expect to see anything.)</p>
<dl>
<dt>&quot;TTY&quot;</p>
<dd> The <font SIZE="-1">TTY</font> to use for debugging I/O.</p>
<dt>&quot;noTTY&quot;</p>
<dd> If set, the debugger goes into <tt>&quot;NonStop&quot;</tt> mode and will not connect to a <font SIZE="-1">TTY.</font> If interrupted (or if control goes to the debugger via explicit setting of <tt>$DB::signal</tt> or <tt>$DB::single</tt> from the Perl script), it connects to a <font SIZE="-1">TTY</font> specified in the <tt>&quot;TTY&quot;</tt> option at startup, or to a tty found at runtime using the <tt>&quot;Term::Rendezvous&quot;</tt> module of your choice. </p>
<p> This module should implement a method named <tt>&quot;new&quot;</tt> that returns an object with two methods: <tt>&quot;IN&quot;</tt> and <tt>&quot;OUT&quot;</tt>. These should return filehandles to use for debugging input and output correspondingly. The <tt>&quot;new&quot;</tt> method should inspect an argument containing the value of <tt>$ENV{PERLDB_NOTTY}</tt> at startup, or <tt>&quot;$ENV{HOME}/.perldbtty$$&quot;</tt> otherwise. This file is not inspected for proper ownership, so security hazards are theoretically possible.</p>
<dt>&quot;ReadLine&quot;</p>
<dd> If false, readline support in the debugger is disabled in order to debug applications that themselves use ReadLine.</p>
<dt>&quot;NonStop&quot;</p>
<dd> If set, the debugger goes into non-interactive mode until interrupted, or programmatically by setting <tt>$DB::signal</tt> or <tt>$DB::single</tt>.</dl>
<p> Here&#8217;s an example of using the <tt>$ENV{PERLDB_OPTS}</tt> variable: </p>
<pre>
    $ PERLDB_OPTS=&quot;NonStop frame=2&quot; perl -d myprogram
</pre>
<p> That will run the script <code>myprogram</code> without human intervention, printing out the call tree with entry and exit points. Note that <tt>&quot;NonStop=1 frame=2&quot;</tt> is equivalent to <tt>&quot;N f=2&quot;</tt>, and that originally, options could be uniquely abbreviated by the first letter (modulo the <tt>&quot;Dump*&quot;</tt> options). It is nevertheless recommended that you always spell them out in full for legibility and future compatibility. </p>
<p> Other examples include </p>
<pre>
    $ PERLDB_OPTS=&quot;NonStop LineInfo=listing frame=2&quot; perl -d myprogram
</pre>
<p> which runs script non-interactively, printing info on each entry into a subroutine and each executed line into the file named <i>listing</i>. (If you interrupt it, you would better reset <tt>&quot;LineInfo&quot;</tt> to something &#8220;interactive&#8221;!) </p>
<p> Other examples include (using standard shell syntax to show environment variable settings): </p>
<pre>
  $ ( PERLDB_OPTS=&quot;NonStop frame=1 AutoTrace LineInfo=tperl.out&quot;
      perl -d myprogram )
</pre>
<p> which may be useful for debugging a program that uses <tt>&quot;Term::ReadLine&quot;</tt> itself. Do not forget to detach your shell from the <font SIZE="-1">TTY</font> in the window that corresponds to <i>/dev/ttyXX</i>, say, by issuing a command like </p>
<pre>
  $ sleep 1000000
</pre>
<p> See &#8220;Debugger Internals&#8221; in perldebguts for details.</p>
<h3>Debugger Input/Output</h3>
<dl>
<dt>Prompt</p>
<dd> The debugger prompt is something like </p>
<pre>
    DB&lt;8&gt;
</pre>
<p> or even </p>
<pre>
    DB&lt;&lt;17&gt;&gt;
</pre>
<p> where that number is the command number, and which you&#8217;d use to access with the built-in <code>csh</code>-like history mechanism. For example, <tt>&quot;!17&quot;</tt> would repeat command number 17. The depth of the angle brackets indicates the nesting depth of the debugger. You could get more than one set of brackets, for example, if you&#8217;d already at a breakpoint and then printed the result of a function call that itself has a breakpoint, or you step into an expression via <tt>&quot;s/n/t expression&quot;</tt> command.</p>
<dt>Multiline commands</p>
<dd> If you want to enter a multi-line command, such as a subroutine definition with several statements or a format, escape the newline that would normally end the debugger command with a backslash. Here&#8217;s an example: </p>
<pre><code>
DB&lt;1&gt; for (1..4)
{
cont:
    print "ok
";
cont:
}
ok
    ok
        ok
            ok
</code></pre>
<p> Note that this business of escaping a newline is specific to interactive commands typed into the debugger.</p>
<dt>Stack backtrace</p>
<dd> Here&#8217;s an example of what a stack backtrace via <tt>&quot;T&quot;</tt> command might look like: </p>
<pre>
 $ = main::infested called from file 'Ambulation.pm' line 10
 @ = Ambulation::legs(1, 2, 3, 4) called from file 'camel_flea'
                                                          line 7
 $ = main::pests('bactrian', 4) called from file 'camel_flea'
                                                          line 4
</pre>
<p> The left-hand character up there indicates the context in which the function was called, with <tt>&quot;$&quot;</tt> and <tt>&quot;@&quot;</tt> meaning scalar or list contexts respectively, and <tt>&quot;.&quot;</tt> meaning void context (which is actually a sort of scalar context). The display above says that you were in the function <tt>&quot;main::infested&quot;</tt> when you ran the stack dump, and that it was called in scalar context from line 10 of the file <i>Ambulation.pm</i>, but without any arguments at all, meaning it was called as <tt>&amp;infested</tt>. The next stack frame shows that the function <tt>&quot;Ambulation::legs&quot;</tt> was called in list context from the <i>camel_flea</i> file with four arguments. The last stack frame shows that <tt>&quot;main::pests&quot;</tt> was called in scalar context, also from <i>camel_flea</i>, but from line 4. </p>
<p> If you execute the <tt>&quot;T&quot;</tt> command from inside an active <tt>&quot;use&quot;</tt> statement, the backtrace will contain both a <tt>&quot;require&quot;</tt> frame and an <tt>&quot;eval&quot;</tt> frame.</p>
<dt>Line Listing Format</p>
<dd> This shows the sorts of output the <tt>&quot;l&quot;</tt> command can produce: </p>
<p>DB &lt;&lt; 13 &gt;&gt; l 101 : @i<br />
{<br />
    @i<br />
}<br />
= ();<br />
102 : b @isa<br />
{<br />
    @i, $pack<br />
}<br />
= () 103 if (exists $i{$prevpack} || exists $isa{$pack});<br />
104<br />
}<br />
105 106 next 107 == &gt; if (exists $isa{$pack});<br />
108 109 : a if ($extra&#8211; &gt; 0)<br />
{<br />
    110 : % isa = ($pack, 1);</p>
<p> Breakable lines are marked with <tt>&quot;:&quot;</tt>. Lines with breakpoints are marked by <tt>&quot;b&quot;</tt> and those with actions by <tt>&quot;a&quot;</tt>. The line that&#8217;s about to be executed is marked by <tt>&quot;==&gt;&quot;</tt>. </p>
<p> Please be aware that code in debugger listings may not look the same as your original source code. Line directives and external source filters can alter the code before Perl sees it, causing code to move from its original positions or take on entirely different forms.</p>
<dt>Frame listing</p>
<dd> When the <tt>&quot;frame&quot;</tt> option is set, the debugger would print entered (and optionally exited) subroutines in different styles. See perldebguts for incredibly long examples of these.</dl>
<h3>Debugging Compile-Time Statements</h3>
<p> If you have compile-time executable statements (such as code within <font SIZE="-1">BEGIN, UNITCHECK</font> and <font SIZE="-1">CHECK</font> blocks or <tt>&quot;use&quot;</tt> statements), these will <i>not</i> be stopped by debugger, although <tt>&quot;require&quot;</tt>s and <font SIZE="-1">INIT</font> blocks will, and compile-time statements can be traced with the <tt>&quot;AutoTrace&quot;</tt> option set in <tt>&quot;PERLDB_OPTS&quot;</tt>). From your own Perl code, however, you can transfer control back to the debugger using the following statement, which is harmless if the debugger is not running: </p>
<pre>
    $DB::single = 1;
</pre>
<p> If you set <tt>$DB::single</tt> to 2, it&#8217;s equivalent to having just typed the <tt>&quot;n&quot;</tt> command, whereas a value of 1 means the <tt>&quot;s&quot;</tt> command. The <tt>$DB::trace</tt> variable should be set to 1 to simulate having typed the <tt>&quot;t&quot;</tt> command. </p>
<p> Another way to debug compile-time code is to start the debugger, set a breakpoint on the <i>load</i> of some module: </p>
<pre>
    DB&lt;7&gt; b load f:/perllib/lib/Carp.pm
  Will stop on load of 'f:/perllib/lib/Carp.pm'.
</pre>
<p> and then restart the debugger using the <tt>&quot;R&quot;</tt> command (if possible). One can use <tt>&quot;b compile subname&quot;</tt> for the same purpose.</p>
<h3>Debugger Customization</h3>
<p> The debugger probably contains enough configuration hooks that you won&#8217;t ever have to modify it yourself. You may change the behaviour of the debugger from within the debugger using its <tt>&quot;o&quot;</tt> command, from the command line via the <tt>&quot;PERLDB_OPTS&quot;</tt> environment variable, and from customization files. </p>
<p> You can do some customization by setting up a <i>.perldb</i> file, which contains initialization code. For instance, you could make aliases like these (the last one is one people expect to be there): </p>
<pre><code>
$DB::alias{'len'} = 's/^len(.*)/p length($1)/';
$DB::alias{'stop'} = 's/^stop (at|in)/b/';
$DB::alias{'ps'} = 's/^ps/p scalar /';
$DB::alias{'quit'} = 's/^quit(\s*)/exit/';
</code></pre>
<p> You can change options from <i>.perldb</i> by using calls like this one; </p>
<pre>
    parse_options(&quot;NonStop=1 LineInfo=db.out AutoTrace=1 frame=2&quot;);
</pre>
<p> The code is executed in the package <tt>&quot;DB&quot;</tt>. Note that <i>.perldb</i> is processed before processing <tt>&quot;PERLDB_OPTS&quot;</tt>. If <i>.perldb</i> defines the subroutine <tt>&quot;afterinit&quot;</tt>, that function is called after debugger initialization ends. <i>.perldb</i> may be contained in the current directory, or in the home directory. Because this file is sourced in by Perl and may contain arbitrary commands, for security reasons, it must be owned by the superuser or the current user, and writable by no one but its owner. </p>
<p> You can mock <font SIZE="-1">TTY</font> input to debugger by adding arbitrary commands to <tt>@DB::typeahead</tt>. For example, your <i>.perldb</i> file might contain: </p>
<pre>
    sub afterinit { push @DB::typeahead, &quot;b 4&quot;, &quot;b 6&quot;; }
</pre>
<p> Which would attempt to set breakpoints on lines 4 and 6 immediately after debugger initialization. Note that <tt>@DB::typeahead</tt> is not a supported interface and is subject to change in future releases. </p>
<p> If you want to modify the debugger, copy <i>perl5db.pl</i> from the Perl library to another name and hack it to your heart&#8217;s content. You&#8217;ll then want to set your <tt>&quot;PERL5DB&quot;</tt> environment variable to say something like this: </p>
<pre>
    BEGIN { require &quot;myperl5db.pl&quot; }
</pre>
<p> As a last resort, you could also use <tt>&quot;PERL5DB&quot;</tt> to customize the debugger by directly setting internal variables or calling debugger functions. </p>
<p> Note that any variables and functions that are not documented in this document (or in perldebguts) are considered for internal use only, and as such are subject to change without notice.</p>
<h3>Readline Support / History in the Debugger</h3>
<p> As shipped, the only command-line history supplied is a simplistic one that checks for leading exclamation points. However, if you install the Term::ReadKey and Term::ReadLine modules from <font SIZE="-1">CPAN</font> (such as Term::ReadLine::Gnu, Term::ReadLine::Perl, &#8230;) you will have full editing capabilities much like those <font SIZE="-1">GNU</font> <i><a href="/docs/linux/man/3-readline/">readline</a></i>(3) provides. Look for these in the <i>modules/by-module/Term</i> directory on <font SIZE="-1">CPAN.</font> These do not support normal <code>vi</code> command-line editing, however. </p>
<p> A rudimentary command-line completion is also available, including lexical variables in the current scope if the <tt>&quot;PadWalker&quot;</tt> module is installed. </p>
<p> Without Readline support you may see the symbols &#8220;^[[A&#8221;, &#8220;^[[C&#8221;, &#8220;^[[B&#8221;, &#8220;^[[D&#8221;&#8220;, &#8221;^H&quot;, &#8230; when using the arrow keys and/or the backspace key.</p>
<h3>Editor Support for Debugging</h3>
<p> If you have the <font SIZE="-1">GNU</font>&#8216;s version of <code>emacs</code> installed on your system, it can interact with the Perl debugger to provide an integrated software development environment reminiscent of its interactions with C debuggers. </p>
<p> Recent versions of Emacs come with a start file for making <code>emacs</code> act like a syntax-directed editor that understands (some of) Perl&#8217;s syntax. See perlfaq3. </p>
<p> Users of <code>vi</code> should also look into <code>vim</code> and <code>gvim</code>, the mousey and windy version, for coloring of Perl keywords. </p>
<p> Note that only perl can truly parse Perl, so all such <font SIZE="-1">CASE</font> tools fall somewhat short of the mark, especially if you don&#8217;t program your Perl as a C programmer might.</p>
<h3>The Perl Profiler</h3>
<p> If you wish to supply an alternative debugger for Perl to run, invoke your script with a colon and a package argument given to the <code>-d</code> flag. Perl&#8217;s alternative debuggers include a Perl profiler, Devel::NYTProf, which is available separately as a <font SIZE="-1">CPAN</font> distribution. To profile your Perl program in the file <i>mycode.pl</i>, just type: </p>
<pre>
    $ perl -d:NYTProf mycode.pl
</pre>
<p> When the script terminates the profiler will create a database of the profile information that you can turn into reports using the profiler&#8217;s tools. See &lt;perlperf&gt; for details.</p>
<h2>Debugging Regular Expressions</h2>
<p> <tt>&quot;use re 'debug'&quot;</tt> enables you to see the gory details of how the Perl regular expression engine works. In order to understand this typically voluminous output, one must not only have some idea about how regular expression matching works in general, but also know how Perl&#8217;s regular expressions are internally compiled into an automaton. These matters are explored in some detail in &#8220;Debugging Regular Expressions&#8221; in perldebguts.</p>
<h2>Debugging Memory Usage</h2>
<p> Perl contains internal support for reporting its own memory usage, but this is a fairly advanced concept that requires some understanding of how memory allocation works. See &#8220;Debugging Perl Memory Usage&#8221; in perldebguts for the details.</p>
<h2>SEE ALSO</h2>
<p> You do have <tt>&quot;use strict&quot;</tt> and <tt>&quot;use warnings&quot;</tt> enabled, don&#8217;t you? </p>
<p> perldebtut, perldebguts, re, <font SIZE="-1">DB</font>, Devel::NYTProf, Dumpvalue, and perlrun. </p>
<p> When debugging a script that uses #! and is thus normally found in <tt>$PATH</tt>, the -S option causes perl to search <tt>$PATH</tt> for it, so you don&#8217;t have to type the path or <tt>&quot;which $scriptname&quot;</tt>. </p>
<pre>
  $ perl -Sd foo.pl
</pre>
<h2>BUGS</h2>
<p> You cannot get stack frame information or in any fashion debug functions that were not compiled by Perl, such as those from C or C<font SIZE="-2">++</font> extensions. </p>
<p> If you alter your <tt>@_</tt> arguments in a subroutine (such as with <tt>&quot;shift&quot;</tt> or <tt>&quot;pop&quot;</tt>), the stack backtrace will not show the original values. </p>
<p> The debugger does not currently work in conjunction with the <code>-W</code> command-line switch, because it itself is not free of warnings. </p>
<p> If you&#8217;re in a slow syscall (like <tt>&quot;wait&quot;</tt>ing, <tt>&quot;accept&quot;</tt>ing, or <tt>&quot;read&quot;</tt>ing from your keyboard or a socket) and haven&#8217;t set up your own <tt>$SIG{INT}</tt> handler, then you won&#8217;t be able to CTRL-C your way back to the debugger, because the debugger&#8217;s own <tt>$SIG{INT}</tt> handler doesn&#8217;t understand that it needs to raise an exception to <code><a href="/docs/linux/man/3-longjmp/">longjmp</a></code>(3) out of slow syscalls. </p>
<h2>Index</h2>
