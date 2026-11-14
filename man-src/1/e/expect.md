---
title: "expect(1)"
name: "expect"
section: "1"
letter: "e"
url: "/docs/linux/man/1-expect/"
description: "expect – programmed dialogue with interactive programs, Version 5"
---

<h2 class="name">NAME</h2>
<p> expect &#8211; programmed dialogue with interactive programs, Version 5 </p>
<h2>SYNOPSIS</h2>
<p> <code>expect</code> [ <code>-dDinN</code> ] [ <code>-c</code> <i>cmds</i> ] [ [ <code>&#8211;</code>[<code>f</code>|<code>b</code>] ] <i>cmdfile</i> ] [ <i>args</i> ]</p>
<h2>INTRODUCTION</h2>
<p> <code>Expect</code> is a program that &quot;talks&quot; to other interactive programs according to a script. Following the script, <code>Expect</code> knows what can be expected from a program and what the correct response should be. An interpreted language provides branching and high-level control structures to direct the dialogue. In addition, the user can take control and interact directly when desired, afterward returning control to the script. </p>
<p> <code>Expectk</code> is a mixture of <code>Expect</code> and <code>Tk</code>. It behaves just like <code>Expect</code> and <code>Tk</code>&#8216;s <code>wish</code>. <code>Expect</code> can also be used directly in C or C++ (that is, without Tcl). See <a href="/docs/linux/man/3-libexpect/">libexpect</a>(3). </p>
<p> The name &quot;Expect&quot; comes from the idea of <i>send/expect</i> sequences popularized by uucp, kermit and other modem control programs. However unlike uucp, <code>Expect</code> is generalized so that it can be run as a user-level command with any program and task in mind. <code>Expect</code> can actually talk to several programs at the same time. </p>
<p> For example, here are some things <code>Expect</code> can do:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Cause your computer to dial you back, so that you can login without paying for the call.</p>
<dt>&bull;</p>
<dd> Start a game (e.g., rogue) and if the optimal configuration doesn&#8217;t appear, restart it (again and again) until it does, then hand over control to you.</p>
<dt>&bull;</p>
<dd> Run fsck, and in response to its questions, answer &quot;yes&quot;, &quot;no&quot; or give control back to you, based on predetermined criteria.</p>
<dt>&bull;</p>
<dd> Connect to another network or BBS (e.g., MCI Mail, CompuServe) and automatically retrieve your mail so that it appears as if it was originally sent to your local system.</p>
<dt>&bull;</p>
<dd> Carry environment variables, current directory, or any kind of information across rlogin, telnet, tip, su, chgrp, etc.</dl>
</dl>
<p> There are a variety of reasons why the shell cannot perform these tasks. (Try, you&#8217;ll see.) All are possible with <code>Expect</code>. </p>
<p> In general, <code>Expect</code> is useful for running any program which requires interaction between the program and the user. All that is necessary is that the interaction can be characterized programmatically. <code>Expect</code> can also give the user back control (without halting the program being controlled) if desired. Similarly, the user can return control to the script at any time.</p>
<h2>USAGE</h2>
<p> <code>Expect</code> reads <i>cmdfile</i> for a list of commands to execute. <code>Expect</code> may also be invoked implicitly on systems which support the #! notation by marking the script executable, and making the first line in your script: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#!/usr/bin/expect -f </p>
<p> Of course, the path must accurately describe where <code>Expect</code> lives. /usr/bin is just an example. </p>
<p> The <code>-c</code> flag prefaces a command to be executed before any in the script. The command should be quoted to prevent being broken up by the shell. This option may be used multiple times. Multiple commands may be executed with a single <code>-c</code> by separating them with semicolons. Commands are executed in the order they appear. (When using Expectk, this option is specified as <code>-command</code>.) </p>
<p> The <code>-d</code> flag enables some diagnostic output, which primarily reports internal activity of commands such as <code>expect</code> and <code>interact</code>. This flag has the same effect as &quot;exp_internal 1&quot; at the beginning of an Expect script, plus the version of <code>Expect</code> is printed. (The <code>strace</code> command is useful for tracing statements, and the <code>trace</code> command is useful for tracing variable assignments.) (When using Expectk, this option is specified as <code>-diag</code>.) </p>
<p> The <code>-D</code> flag enables an interactive debugger. An integer value should follow. The debugger will take control before the next Tcl procedure if the value is non-zero or if a ^C is pressed (or a breakpoint is hit, or other appropriate debugger command appears in the script). See the README file or SEE ALSO (below) for more information on the debugger. (When using Expectk, this option is specified as <code>-Debug</code>.) </p>
<p> The <code>-f</code> flag prefaces a file from which to read commands from. The flag itself is optional as it is only useful when using the #! notation (see above), so that other arguments may be supplied on the command line. (When using Expectk, this option is specified as <code>-file</code>.) </p>
<p> By default, the command file is read into memory and executed in its entirety. It is occasionally desirable to read files one line at a time. For example, stdin is read this way. In order to force arbitrary files to be handled this way, use the <code>-b</code> flag. (When using Expectk, this option is specified as <code>-buffer</code>.) Note that stdio-buffering may still take place however this shouldn&#8217;t cause problems when reading from a fifo or stdin. </p>
<p> If the string &quot;-&quot; is supplied as a filename, standard input is read instead. (Use &quot;./-&quot; to read from a file actually named &quot;-&quot;.) </p>
<p> The <code>-i</code> flag causes <code>Expect</code> to interactively prompt for commands instead of reading them from a file. Prompting is terminated via the <code>exit</code> command or upon EOF. See <code>interpreter</code> (below) for more information. <code>-i</code> is assumed if neither a command file nor <code>-c</code> is used. (When using Expectk, this option is specified as <code>-interactive</code>.) </p>
<p> <code>&#8212;</code> may be used to delimit the end of the options. This is useful if you want to pass an option-like argument to your script without it being interpreted by <code>Expect</code>. This can usefully be placed in the #! line to prevent any flag-like interpretation by Expect. For example, the following will leave the original arguments (including the script name) in the variable <i>argv</i>. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#!/usr/bin/expect &#8212; </p>
<p> Note that the usual <a href="/docs/linux/man/3-getopt/">getopt</a>(3) and <a href="/docs/linux/man/2-execve/">execve</a>(2) conventions must be observed when adding arguments to the #! line. </p>
<p> The file $exp_library/expect.rc is sourced automatically if present, unless the <code>-N</code> flag is used. (When using Expectk, this option is specified as <code>-NORC</code>.) Immediately after this, the file ~/.expect.rc is sourced automatically, unless the <code>-n</code> flag is used. If the environment variable DOTDIR is defined, it is treated as a directory and .expect.rc is read from there. (When using Expectk, this option is specified as <code>-norc</code>.) This sourcing occurs only after executing any <code>-c</code> flags. </p>
<p> <code>-v</code> causes Expect to print its version number and exit. (The corresponding flag in Expectk, which uses long flag names, is -version.) </p>
<p> Optional <i>args</i> are constructed into a list and stored in the variable named <i>argv</i>. <i>argc</i> is initialized to the length of argv. </p>
<p> <i>argv0</i> is defined to be the name of the script (or binary if no script is used). For example, the following prints out the name of the script and the first three arguments: </p>
<pre>
    send_user &quot;$argv0 [lrange $argv 0 2]
&quot;
</pre>
<h2>COMMANDS</h2>
<p> <code>Expect</code> uses <i>Tcl</i> (Tool Command Language). Tcl provides control flow (e.g., if, for, break), expression evaluation and several other features such as recursion, procedure definition, etc. Commands used here but not defined (e.g., <code>set</code>, <code>if</code>, <code>exec</code>) are Tcl commands (see <a href="/docs/linux/man/3-tcl/">tcl</a>(3)). <code>Expect</code> supports additional commands, described below. Unless otherwise specified, commands return the empty string. </p>
<p> Commands are listed alphabetically so that they can be quickly located. However, new users may find it easier to start by reading the descriptions of <code>spawn</code>, <code>send</code>, <code>expect</code>, and <code>interact</code>, in that order. </p>
<p> Note that the best introduction to the language (both Expect and Tcl) is provided in the book &quot;Exploring Expect&quot; (see SEE ALSO below). Examples are included in this man page but they are very limited since this man page is meant primarily as reference material. </p>
<p> Note that in the text of this man page, &quot;Expect&quot; with an uppercase &quot;E&quot; refers to the <code>Expect</code> program while &quot;expect&quot; with a lower-case &quot;e&quot; refers to the <code>expect</code> command within the <code>Expect</code> program.) <i></p>
<dl>
<dt></i><code>close</code><i> [-slave] [-onexec 0|1] [-i spawn_id]</i></p>
<dd> closes the connection to the current process. Most interactive programs will detect EOF on their stdin and exit; thus <code>close</code> usually suffices to kill the process as well. The <code>-i</code> flag declares the process to close corresponding to the named spawn_id. </p>
<p> Both <code>expect</code> and <code>interact</code> will detect when the current process exits and implicitly do a <code>close</code>. But if you kill the process by, say, &quot;exec kill $pid&quot;, you will need to explicitly call <code>close</code>. </p>
<p> The <code>-onexec</code> flag determines whether the spawn id will be closed in any new spawned processes or if the process is overlayed. To leave a spawn id open, use the value 0. A non-zero integer value will force the spawn closed (the default) in any new processes. </p>
<p> The <code>-slave</code> flag closes the slave associated with the spawn id. (See &quot;spawn -pty&quot;.) When the connection is closed, the slave is automatically closed as well if still open. </p>
<p> No matter whether the connection is closed implicitly or explicitly, you should call <code>wait</code> to clear up the corresponding kernel process slot. <code>close</code> does not call <code>wait</code> since there is no guarantee that closing a process connection will cause it to exit. See <code>wait</code> below for more info.</p>
<dt><code>debug</code><i> [[-now] 0|1]</i></p>
<dd> controls a Tcl debugger allowing you to step through statements, set breakpoints, etc. </p>
<p> With no arguments, a 1 is returned if the debugger is not running, otherwise a 0 is returned. </p>
<p> With a 1 argument, the debugger is started. With a 0 argument, the debugger is stopped. If a 1 argument is preceded by the <code>-now</code> flag, the debugger is started immediately (i.e., in the middle of the <code>debug</code> command itself). Otherwise, the debugger is started with the next Tcl statement. </p>
<p> The <code>debug</code> command does not change any traps. Compare this to starting Expect with the <code>-D</code> flag (see above). </p>
<p> See the README file or SEE ALSO (below) for more information on the debugger.</p>
<dt><code>disconnect</code></p>
<dd> disconnects a forked process from the terminal. It continues running in the background. The process is given its own process group (if possible). Standard I/O is redirected to /dev/null.</p>
<dt>
<dd> The following fragment uses <code>disconnect</code> to continue running the script in the background. </p>
<pre><code>
if {
    [fork] != 0
}
exit
    disconnect
        ...
</code></pre>
<p> The following script reads a password, and then runs a program every hour that demands a password each time it is run. The script supplies the password so that you only have to type it once. (See the <code>stty</code> command which demonstrates how to turn off password echoing.)<br />
    send_user &#8220;password?\ &#8221;<br />
    expect_user -re &#8220;(.*)
&#8221;<br />
    for<br />
    {<br />
    }<br />
    1 {}<br />
    {<br />
        if {<br />
            [fork] != 0<br />
        }<br />
        {<br />
            sleep 3600;<br />
            continue<br />
        }<br />
        disconnect<br />
            spawn priv_prog<br />
                expect Password : send &#8220;$expect_out(1,string)&#8221;<br />
                                      &#8230;exit<br />
    }<br />
 An advantage to using <code>disconnect</code> over the shell asynchronous process feature (&amp;) is that <code>Expect</code> can save the terminal parameters prior to disconnection, and then later apply them to new ptys. With &amp;, <code>Expect</code> does not have a chance to read the terminal&#8217;s parameters since the terminal is already disconnected by the time <code>Expect</code> receives control.</p>
<dt><code>exit</code><i> [-opts] [status]</i></p>
<dd> causes <code>Expect</code> to exit or otherwise prepare to do so. </p>
<p> The <code>-onexit</code> flag causes the next argument to be used as an exit handler. Without an argument, the current exit handler is returned. </p>
<p> The <code>-noexit</code> flag causes <code>Expect</code> to prepare to exit but stop short of actually returning control to the operating system. The user-defined exit handler is run as well as Expect&#8217;s own internal handlers. No further Expect commands should be executed. This is useful if you are running Expect with other Tcl extensions. The current interpreter (and main window if in the Tk environment) remain so that other Tcl extensions can clean up. If Expect&#8217;s <code>exit</code> is called again (however this might occur), the handlers are not rerun. </p>
<p> Upon exiting, all connections to spawned processes are closed. Closure will be detected as an EOF by spawned processes. <code>exit</code> takes no other actions beyond what the normal <a href="/docs/linux/man/2-_exit/">_exit</a>(2) procedure does. Thus, spawned processes that do not check for EOF may continue to run. (A variety of conditions are important to determining, for example, what signals a spawned process will be sent, but these are system-dependent, typically documented under <a href="/docs/linux/man/3-exit/">exit</a>(3).) Spawned processes that continue to run will be inherited by init. </p>
<p> <i>status</i> (or 0 if not specified) is returned as the exit status of <code>Expect</code>. <code>exit</code> is implicitly executed if the end of the script is reached.</p>
<dt><code>exp_continue</code> [-continue_timer]</p>
<dd> The command <code>exp_continue</code> allows <code>expect</code> itself to continue executing rather than returning as it normally would. By default <code>exp_continue</code> resets the timeout timer. The <i>-continue_timer</i> flag prevents timer from being restarted. (See <code>expect</code> for more information.)</p>
<dt><code>exp_internal</code><i> [-f file] value</i></p>
<dd> causes further commands to send diagnostic information internal to <code>Expect</code> to stderr if <i>value</i> is non-zero. This output is disabled if <i>value</i> is 0. The diagnostic information includes every character received, and every attempt made to match the current output against the patterns.</p>
<dt>
<dd> If the optional <i>file</i> is supplied, all normal and debugging output is written to that file (regardless of the value of <i>value</i>). Any previous diagnostic output file is closed. </p>
<p> The <code>-info</code> flag causes exp_internal to return a description of the most recent non-info arguments given.</p>
<dt><code>exp_open</code><i> [args] [-i spawn_id]</i></p>
<dd> returns a Tcl file identifier that corresponds to the original spawn id. The file identifier can then be used as if it were opened by Tcl&#8217;s <code>open</code> command. (The spawn id should no longer be used. A <code>wait</code> should not be executed. </p>
<p> The <code>-leaveopen</code> flag leaves the spawn id open for access through Expect commands. A <code>wait</code> must be executed on the spawn id.</p>
<dt><code>exp_pid</code><i> [-i spawn_id]</i></p>
<dd> returns the process id corresponding to the currently spawned process. If the <code>-i</code> flag is used, the pid returned corresponds to that of the given spawn id.</p>
<dt><code>exp_send</code></p>
<dd> is an alias for <code>send</code>.</p>
<dt><code>exp_send_error</code></p>
<dd> is an alias for <code>send_error</code>.</p>
<dt><code>exp_send_log</code></p>
<dd> is an alias for <code>send_log</code>.</p>
<dt><code>exp_send_tty</code></p>
<dd> is an alias for <code>send_tty</code>.</p>
<dt><code>exp_send_user</code></p>
<dd> is an alias for <code>send_user</code>.</p>
<dt><code>exp_version</code><i> [[-exit] version]</i></p>
<dd> is useful for assuring that the script is compatible with the current version of Expect.</p>
<dt>
<dd> With no arguments, the current version of <code>Expect</code> is returned. This version may then be encoded in your script. If you actually know that you are not using features of recent versions, you can specify an earlier version.</p>
<dt>
<dd> Versions consist of three numbers separated by dots. First is the major number. Scripts written for versions of <code>Expect</code> with a different major number will almost certainly not work. <code>exp_version </code> returns an error if the major numbers do not match.</p>
<dt>
<dd> Second is the minor number. Scripts written for a version with a greater minor number than the current version may depend upon some new feature and might not run. <code>exp_version</code> returns an error if the major numbers match, but the script minor number is greater than that of the running <code>Expect</code>.</p>
<dt>
<dd> Third is a number that plays no part in the version comparison. However, it is incremented when the <code>Expect</code> software distribution is changed in any way, such as by additional documentation or optimization. It is reset to 0 upon each new minor version.</p>
<dt>
<dd> With the <code>-exit</code> flag, <code>Expect</code> prints an error and exits if the version is out of date.</p>
<dt><code>expect</code><i> [[-opts] pat1 body1] &#8230; [-opts] patn [bodyn]</i></p>
<dd> waits until one of the patterns matches the output of a spawned process, a specified time period has passed, or an end-of-file is seen. If the final body is empty, it may be omitted.</p>
<dt>
<dd> Patterns from the most recent <code>expect_before</code> command are implicitly used before any other patterns. Patterns from the most recent <code>expect_after</code> command are implicitly used after any other patterns.</p>
<dt>
<dd> If the arguments to the entire <code>expect</code> statement require more than one line, all the arguments may be &quot;braced&quot; into one so as to avoid terminating each line with a backslash. In this one case, the usual Tcl substitutions will occur despite the braces.</p>
<dt>
<dd> If a pattern is the keyword <code>eof</code>, the corresponding body is executed upon end-of-file. If a pattern is the keyword <code>timeout</code>, the corresponding body is executed upon timeout. If no timeout keyword is used, an implicit null action is executed upon timeout. The default timeout period is 10 seconds but may be set, for example to 30, by the command &quot;set timeout 30&quot;. An infinite timeout may be designated by the value -1. If a pattern is the keyword <code>default</code>, the corresponding body is executed upon either timeout or end-of-file.</p>
<dt>
<dd> If a pattern matches, then the corresponding body is executed. <code>expect</code> returns the result of the body (or the empty string if no pattern matched). In the event that multiple patterns match, the one appearing first is used to select a body.</p>
<dt>
<dd> Each time new output arrives, it is compared to each pattern in the order they are listed. Thus, you may test for absence of a match by making the last pattern something guaranteed to appear, such as a prompt. In situations where there is no prompt, you must use <code>timeout</code> (just like you would if you were interacting manually).</p>
<dt>
<dd> Patterns are specified in three ways. By default, patterns are specified as with Tcl&#8217;s <code>string match</code> command. (Such patterns are also similar to C-shell regular expressions usually referred to as &quot;glob&quot; patterns). The <code>-gl</code> flag may may be used to protect patterns that might otherwise match <code>expect</code> flags from doing so. Any pattern beginning with a &quot;-&quot; should be protected this way. (All strings starting with &quot;-&quot; are reserved for future options.) </p>
<dt>
<dd> For example, the following fragment looks for a successful login. (Note that <code>abort</code> is presumed to be a procedure defined elsewhere in the script.)<br />
expect<br />
{<br />
    busy<br />
    {<br />
        puts busy
;<br />
        exp_continue<br />
    }<br />
    failed abort<br />
        &#8220;invalid password&#8221; abort<br />
            timeout abort<br />
                connected<br />
}<br />
 Quotes are necessary on the fourth pattern since it contains a space, which would otherwise separate the pattern from the action. Patterns with the same action (such as the 3rd and 4th) require listing the actions again. This can be avoid by using regexp-style patterns (see below). More information on forming glob-style patterns can be found in the Tcl manual.</p>
<dt>
<dd> Regexp-style patterns follow the syntax defined by Tcl&#8217;s <code>regexp</code> (short for &quot;regular expression&quot;) command. regexp patterns are introduced with the flag <code>-re</code>. The previous example can be rewritten using a regexp as:<br />
expect<br />
{<br />
    busy<br />
    {<br />
        puts busy
;<br />
        exp_continue<br />
    }<br />
    -re &#8220;failed|invalid password&#8221; abort<br />
        timeout abort<br />
            connected<br />
}<br />
 Both types of patterns are &quot;unanchored&quot;. This means that patterns do not have to match the entire string, but can begin and end the match anywhere in the string (as long as everything else matches). Use ^ to match the beginning of a string, and $ to match the end. Note that if you do not wait for the end of a string, your responses can easily end up in the middle of the string as they are echoed from the spawned process. While still producing correct results, the output can look unnatural. Thus, use of $ is encouraged if you can exactly describe the characters at the end of a string. </p>
<p> Note that in many editors, the ^ and $ match the beginning and end of lines respectively. However, because expect is not line oriented, these characters match the beginning and end of the data (as opposed to lines) currently in the expect matching buffer. (Also, see the note below on &quot;system indigestion.&quot;) </p>
<p> The <code>-ex</code> flag causes the pattern to be matched as an &quot;exact&quot; string. No interpretation of *, ^, etc is made (although the usual Tcl conventions must still be observed). Exact patterns are always unanchored. </p>
<dt>
<dd> The <code>-nocase</code> flag causes uppercase characters of the output to compare as if they were lowercase characters. The pattern is not affected.</p>
<dt>
<dd> While reading output, more than 2000 bytes can force earlier bytes to be &quot;forgotten&quot;. This may be changed with the function <code>match_max</code>. (Note that excessively large values can slow down the pattern matcher.) If <i>patlist</i> is <code>full_buffer</code>, the corresponding body is executed if <i>match_max</i> bytes have been received and no other patterns have matched. Whether or not the <code>full_buffer</code> keyword is used, the forgotten characters are written to expect_out(buffer). </p>
<p> If <i>patlist</i> is the keyword <code>null</code>, and nulls are allowed (via the <code>remove_nulls</code> command), the corresponding body is executed if a single ASCII 0 is matched. It is not possible to match 0 bytes via glob or regexp patterns. </p>
<p> Upon matching a pattern (or eof or full_buffer), any matching and previously unmatched output is saved in the variable <i>expect_out(buffer)</i>. Up to 9 regexp substring matches are saved in the variables <i>expect_out(1,string)</i> through <i>expect_out(9,string)</i>. If the <code>-indices</code> flag is used before a pattern, the starting and ending indices (in a form suitable for <code>lrange</code>) of the 10 strings are stored in the variables <i>expect_out(X,start)</i> and <i>expect_out(X,end)</i> where X is a digit, corresponds to the substring position in the buffer. 0 refers to strings which matched the entire pattern and is generated for glob patterns as well as regexp patterns. For example, if a process has produced output of &quot;abcdefgh
&quot;, the result of: </p>
<pre>
    expect &quot;cd&quot;
</pre>
<p> is as if the following statements had executed: </p>
<pre>
    set expect_out(0,string) cd
    set expect_out(buffer) abcd
</pre>
<p> and &quot;efgh
&quot; is left in the output buffer. If a process produced the output &quot;abbbcabkkkka
&quot;, the result of: </p>
<pre>
    expect -indices -re &quot;b(b*).*(k+)&quot;
</pre>
<p> is as if the following statements had executed: </p>
<pre>
    set expect_out(0,start) 1
    set expect_out(0,end) 10
    set expect_out(0,string) bbbcabkkkk
    set expect_out(1,start) 2
    set expect_out(1,end) 3
    set expect_out(1,string) bb
    set expect_out(2,start) 10
    set expect_out(2,end) 10
    set expect_out(2,string) k
    set expect_out(buffer) abbbcabkkkk
</pre>
<p> and &quot;a
&quot; is left in the output buffer. The pattern &quot;*&quot; (and -re &quot;.*&quot;) will flush the output buffer without reading any more output from the process.</p>
<dt>
<dd> Normally, the matched output is discarded from Expect&#8217;s internal buffers. This may be prevented by prefixing a pattern with the <code>-notransfer</code> flag. This flag is especially useful in experimenting (and can be abbreviated to &quot;-not&quot; for convenience while experimenting). </p>
<p> The spawn id associated with the matching output (or eof or full_buffer) is stored in <i>expect_out(spawn_id)</i>. </p>
<p> The <code>-timeout</code> flag causes the current expect command to use the following value as a timeout instead of using the value of the timeout variable. </p>
<p> By default, patterns are matched against output from the current process, however the <code>-i</code> flag declares the output from the named spawn_id list be matched against any following patterns (up to the next <code>-i</code>). The spawn_id list should either be a whitespace separated list of spawn_ids or a variable referring to such a list of spawn_ids. </p>
<p> For example, the following example waits for &quot;connected&quot; from the current process, or &quot;busy&quot;, &quot;failed&quot; or &quot;invalid password&quot; from the spawn_id named by $proc2.<br />
expect<br />
{<br />
    -i $proc2 busy<br />
    {<br />
        puts busy
;<br />
        exp_continue<br />
    }<br />
    -re &#8220;failed|invalid password&#8221; abort<br />
        timeout abort<br />
            connected<br />
}<br />
 The value of the global variable <i>any_spawn_id</i> may be used to match patterns to any spawn_ids that are named with all other <code>-i</code> flags in the current <code>expect</code> command. The spawn_id from a <code>-i</code> flag with no associated pattern (i.e., followed immediately by another <code>-i</code>) is made available to any other patterns in the same <code>expect</code> command associated with <i>any_spawn_id.</i> </p>
<p> The <code>-i</code> flag may also name a global variable in which case the variable is read for a list of spawn ids. The variable is reread whenever it changes. This provides a way of changing the I/O source while the command is in execution. Spawn ids provided this way are called &quot;indirect&quot; spawn ids. </p>
<p> Actions such as <code>break</code> and <code>continue</code> cause control structures (i.e., <code>for</code>, <code>proc</code>) to behave in the usual way. The command <code>exp_continue</code> allows <code>expect</code> itself to continue executing rather than returning as it normally would.</p>
<dt>
<dd> This is useful for avoiding explicit loops or repeated expect statements. The following example is part of a fragment to automate rlogin. The <code>exp_continue</code> avoids having to write a second <code>expect</code> statement (to look for the prompt again) if the rlogin prompts for a password.<br />
expect<br />
{<br />
Password : {<br />
    stty &#8211; echo send_user &#8220;password (for $user) on $host: &#8221; expect_user &#8211; re &#8220;(.*)
&#8221; send_user &#8220;
&#8221; send &#8220;$expect_out(1,string)&#8221; stty echo exp_continue<br />
}<br />
    incorrect{<br />
        send_user &#8220;invalid password or account
&#8221; exit} timeout{<br />
        send_user &#8220;connection to $host timed out
&#8221; exit} eof{<br />
        send_user<br />
        &#8220;connection to host failed: $expect_out(buffer)&#8221; exit} &#8211;<br />
        re $prompt<br />
}<br />
 For example, the following fragment might help a user guide an interaction that is already totally automated. In this case, the terminal is put into raw mode. If the user presses &quot;+&quot;, a variable is incremented. If &quot;p&quot; is pressed, several returns are sent to the process, perhaps to poke it in some way, and &quot;i&quot; lets the user interact with the process, effectively stealing away control from the script. In each case, the <code>exp_continue</code> allows the current <code>expect</code> to continue pattern matching after executing the current action.<br />
stty raw &#8211; echo<br />
               expect_after<br />
{<br />
    -i $user_spawn_id<br />
        &#8220;p&#8221;<br />
    {<br />
        send &#8220;&#8221;;<br />
        exp_continue<br />
    }<br />
    &#8220;+&#8221;<br />
    {<br />
        incr foo;<br />
        exp_continue<br />
    }<br />
    &#8220;i&#8221;<br />
    {<br />
        interact;<br />
        exp_continue<br />
    }<br />
    &#8220;quit&#8221; exit<br />
}</p>
<dt>
<dd> By default, <code>exp_continue</code> resets the timeout timer. The timer is not restarted, if <code>exp_continue</code> is called with the <code>-continue_timer</code> flag.</p>
<dt><code>expect_after</code><i> [expect_args]</i></p>
<dd> works identically to the <code>expect_before</code> except that if patterns from both <code>expect</code> and <code>expect_after</code> can match, the <code>expect</code> pattern is used. See the <code>expect_before</code> command for more information.</p>
<dt><code>expect_background</code><i> [expect_args]</i></p>
<dd> takes the same arguments as <code>expect</code>, however it returns immediately. Patterns are tested whenever new input arrives. The pattern <code>timeout</code> and <code>default</code> are meaningless to <code>expect_background</code> and are silently discarded. Otherwise, the <code>expect_background</code> command uses <code>expect_before</code> and <code>expect_after</code> patterns just like <code>expect</code> does. </p>
<p> When <code>expect_background</code> actions are being evaluated, background processing for the same spawn id is blocked. Background processing is unblocked when the action completes. While background processing is blocked, it is possible to do a (foreground) <code>expect</code> on the same spawn id. </p>
<p> It is not possible to execute an <code>expect</code> while an <code>expect_background</code> is unblocked. <code>expect_background</code> for a particular spawn id is deleted by declaring a new expect_background with the same spawn id. Declaring <code>expect_background</code> with no pattern removes the given spawn id from the ability to match patterns in the background.</p>
<dt><code>expect_before</code><i> [expect_args]</i></p>
<dd> takes the same arguments as <code>expect</code>, however it returns immediately. Pattern-action pairs from the most recent <code>expect_before</code> with the same spawn id are implicitly added to any following <code>expect</code> commands. If a pattern matches, it is treated as if it had been specified in the <code>expect</code> command itself, and the associated body is executed in the context of the <code>expect</code> command. If patterns from both <code>expect_before</code> and <code>expect</code> can match, the <code>expect_before</code> pattern is used. </p>
<p> If no pattern is specified, the spawn id is not checked for any patterns. </p>
<p> Unless overridden by a <code>-i</code> flag, <code>expect_before</code> patterns match against the spawn id defined at the time that the <code>expect_before</code> command was executed (not when its pattern is matched). </p>
<p> The -info flag causes <code>expect_before</code> to return the current specifications of what patterns it will match. By default, it reports on the current spawn id. An optional spawn id specification may be given for information on that spawn id. For example </p>
<pre>
    expect_before -info -i $proc
</pre>
<p> At most one spawn id specification may be given. The flag -indirect suppresses direct spawn ids that come only from indirect specifications. </p>
<p> Instead of a spawn id specification, the flag &quot;-all&quot; will cause &quot;-info&quot; to report on all spawn ids. </p>
<p> The output of the -info flag can be reused as the argument to expect_before.</p>
<dt><code>expect_tty</code><i> [expect_args]</i></p>
<dd> is like <code>expect</code> but it reads characters from /dev/tty (i.e. keystrokes from the user). By default, reading is performed in cooked mode. Thus, lines must end with a return in order for <code>expect</code> to see them. This may be changed via <code>stty</code> (see the <code>stty</code> command below).</p>
<dt><code>expect_user</code><i> [expect_args]</i></p>
<dd> is like <code>expect</code> but it reads characters from stdin (i.e. keystrokes from the user). By default, reading is performed in cooked mode. Thus, lines must end with a return in order for <code>expect</code> to see them. This may be changed via <code>stty</code> (see the <code>stty</code> command below).</p>
<dt><code>fork</code></p>
<dd> creates a new process. The new process is an exact copy of the current <code>Expect</code> process. On success, <code>fork</code> returns 0 to the new (child) process and returns the process ID of the child process to the parent process. On failure (invariably due to lack of resources, e.g., swap space, memory), <code>fork</code> returns -1 to the parent process, and no child process is created.</p>
<dt>
<dd> Forked processes exit via the <code>exit</code> command, just like the original process. Forked processes are allowed to write to the log files. If you do not disable debugging or logging in most of the processes, the result can be confusing.</p>
<dt>
<dd> Some pty implementations may be confused by multiple readers and writers, even momentarily. Thus, it is safest to <code>fork</code> before spawning processes.</p>
<dt><code>interact</code><i> [string1 body1] &#8230; [stringn [bodyn]]</i></p>
<dd> gives control of the current process to the user, so that keystrokes are sent to the current process, and the stdout and stderr of the current process are returned.</p>
<dt>
<dd> String-body pairs may be specified as arguments, in which case the body is executed when the corresponding string is entered. (By default, the string is not sent to the current process.) The <code>interpreter</code> command is assumed, if the final body is missing.</p>
<dt>
<dd> If the arguments to the entire <code>interact</code> statement require more than one line, all the arguments may be &quot;braced&quot; into one so as to avoid terminating each line with a backslash. In this one case, the usual Tcl substitutions will occur despite the braces.</p>
<dt>
<dd> For example, the following command runs interact with the following string-body pairs defined: When ^Z is pressed, <code>Expect</code> is suspended. (The <code>-reset</code> flag restores the terminal modes.) When ^A is pressed, the user sees &quot;you typed a control-A&quot; and the process is sent a ^A. When $ is pressed, the user sees the date. When ^C is pressed, <code>Expect</code> exits. If &quot;foo&quot; is entered, the user sees &quot;bar&quot;. When ~~ is pressed, the <code>Expect</code> interpreter runs interactively.<br />
set CTRLZ  interact<br />
{<br />
    -reset $CTRLZ<br />
    {<br />
        exec kill &#8211; STOP[pid]<br />
    }<br />
    <br />
    {<br />
        send_user &#8220;you typed a control-A
&#8221;;<br />
        send &#8220;&#8221;<br />
    }<br />
    $<br />
    {<br />
        send_user &#8220;The date is [clock format [clock seconds]].&#8221;<br />
    }<br />
     exit<br />
        foo<br />
    {<br />
        send_user &#8220;bar&#8221;<br />
    }<br />
    ~~<br />
}</p>
<dt>
<dd> In string-body pairs, strings are matched in the order they are listed as arguments. Strings that partially match are not sent to the current process in anticipation of the remainder coming. If characters are then entered such that there can no longer possibly be a match, only the part of the string will be sent to the process that cannot possibly begin another match. Thus, strings that are substrings of partial matches can match later, if the original strings that was attempting to be match ultimately fails.</p>
<dt>
<dd> By default, string matching is exact with no wild cards. (In contrast, the <code>expect</code> command uses glob-style patterns by default.) The <code>-ex</code> flag may be used to protect patterns that might otherwise match <code>interact</code> flags from doing so. Any pattern beginning with a &quot;-&quot; should be protected this way. (All strings starting with &quot;-&quot; are reserved for future options.) </p>
<p> The <code>-re</code> flag forces the string to be interpreted as a regexp-style pattern. In this case, matching substrings are stored in the variable <i>interact_out</i> similarly to the way <code>expect</code> stores its output in the variable <code>expect_out</code>. The <code>-indices</code> flag is similarly supported. </p>
<p> The pattern <code>eof</code> introduces an action that is executed upon end-of-file. A separate <code>eof</code> pattern may also follow the <code>-output</code> flag in which case it is matched if an eof is detected while writing output. The default <code>eof</code> action is &quot;return&quot;, so that <code>interact</code> simply returns upon any EOF. </p>
<p> The pattern <code>timeout</code> introduces a timeout (in seconds) and action that is executed after no characters have been read for a given time. The <code>timeout</code> pattern applies to the most recently specified process. There is no default timeout. The special variable &quot;timeout&quot; (used by the <code>expect</code> command) has no affect on this timeout. </p>
<p> For example, the following statement could be used to autologout users who have not typed anything for an hour but who still get frequent system messages: </p>
<pre>
    interact -input $user_spawn_id timeout 3600 return -output \
        $spawn_id 
</pre>
<p> If the pattern is the keyword <code>null</code>, and nulls are allowed (via the <code>remove_nulls</code> command), the corresponding body is executed if a single ASCII 0 is matched. It is not possible to match 0 bytes via glob or regexp patterns. </p>
<p> Prefacing a pattern with the flag <code>-iwrite</code> causes the variable <i>interact_out(spawn_id)</i> to be set to the spawn_id which matched the pattern (or eof). </p>
<p> Actions such as <code>break</code> and <code>continue</code> cause control structures (i.e., <code>for</code>, <code>proc</code>) to behave in the usual way. However <code>return</code> causes interact to return to its caller, while <code>inter_return</code> causes <code>interact</code> to cause a return in its caller. For example, if &quot;proc foo&quot; called <code>interact</code> which then executed the action <code>inter_return</code>, <code>proc foo</code> would return. (This means that if <code>interact</code> calls <code>interpreter</code> interactively typing <code>return</code> will cause the interact to continue, while <code>inter_return</code> will cause the interact to return to its caller.)</p>
<dt>
<dd> During <code>interact</code>, raw mode is used so that all characters may be passed to the current process. If the current process does not catch job control signals, it will stop if sent a stop signal (by default ^Z). To restart it, send a continue signal (such as by &quot;kill -CONT &lt;pid&gt;&quot;). If you really want to send a SIGSTOP to such a process (by ^Z), consider spawning csh first and then running your program. On the other hand, if you want to send a SIGSTOP to <code>Expect</code> itself, first call interpreter (perhaps by using an escape character), and then press ^Z.</p>
<dt>
<dd> String-body pairs can be used as a shorthand for avoiding having to enter the interpreter and execute commands interactively. The previous terminal mode is used while the body of a string-body pair is being executed.</p>
<dt>
<dd> For speed, actions execute in raw mode by default. The <code>-reset</code> flag resets the terminal to the mode it had before <code>interact</code> was executed (invariably, cooked mode). Note that characters entered when the mode is being switched may be lost (an unfortunate feature of the terminal driver on some systems). The only reason to use <code>-reset</code> is if your action depends on running in cooked mode.</p>
<dt>
<dd> The <code>-echo</code> flag sends characters that match the following pattern back to the process that generated them as each character is read. This may be useful when the user needs to see feedback from partially typed patterns.</p>
<dt>
<dd> If a pattern is being echoed but eventually fails to match, the characters are sent to the spawned process. If the spawned process then echoes them, the user will see the characters twice. <code>-echo</code> is probably only appropriate in situations where the user is unlikely to not complete the pattern. For example, the following excerpt is from rftp, the recursive-ftp script, where the user is prompted to enter ~g, ~p, or ~l, to get, put, or list the current directory recursively. These are so far away from the normal ftp commands, that the user is unlikely to type ~ followed by anything else, except mistakenly, in which case, they&#8217;ll probably just ignore the result anyway.<br />
interact<br />
{<br />
    -echo ~g{getcurdirectory 1} &#8211; echo ~l{getcurdirectory 0} &#8211; echo ~p<br />
    {<br />
        putcurdirectory<br />
    }<br />
}<br />
 The <code>-nobuffer</code> flag sends characters that match the following pattern on to the output process as characters are read. </p>
<p> This is useful when you wish to let a program echo back the pattern. For example, the following might be used to monitor where a person is dialing (a Hayes-style modem). Each time &quot;atd&quot; is seen the script logs the rest of the line.<br />
proc lognumber{} {<br />
    interact &#8211; nobuffer &#8211; re &#8220;(.*)&#8221; return puts $log &#8220;[clock format [clock seconds]]: dialed $interact_out(1,string)&#8221;} interact &#8211;<br />
    nobuffer &#8220;atd&#8221; lognumber</p>
<dt>
<dd> During <code>interact</code>, previous use of <code>log_user</code> is ignored. In particular, <code>interact</code> will force its output to be logged (sent to the standard output) since it is presumed the user doesn&#8217;t wish to interact blindly.</p>
<dt>
<dd> The <code>-o</code> flag causes any following key-body pairs to be applied to the output of the current process. This can be useful, for example, when dealing with hosts that send unwanted characters during a telnet session.</p>
<dt>
<dd> By default, <code>interact</code> expects the user to be writing stdin and reading stdout of the <code>Expect</code> process itself. The <code>-u</code> flag (for &quot;user&quot;) makes <code>interact</code> look for the user as the process named by its argument (which must be a spawned id).</p>
<dt>
<dd> This allows two unrelated processes to be joined together without using an explicit loop. To aid in debugging, Expect diagnostics always go to stderr (or stdout for certain logging and debugging information). For the same reason, the <code>interpreter</code> command will read interactively from stdin.</p>
<dt>
<dd> For example, the following fragment creates a login process. Then it dials the user (not shown), and finally connects the two together. Of course, any process may be substituted for login. A shell, for example, would allow the user to work without supplying an account and password. </p>
<pre>
    spawn login
    set login $spawn_id
    spawn tip modem
    # dial back out to user
    # connect user to login
    interact -u $login
</pre>
<p> To send output to multiple processes, list each spawn id list prefaced by a <code>-output</code> flag. Input for a group of output spawn ids may be determined by a spawn id list prefaced by a <code>-input</code> flag. (Both <code>-input</code> and <code>-output</code> may take lists in the same form as the <code>-i</code> flag in the <code>expect</code> command, except that any_spawn_id is not meaningful in <code>interact</code>.) All following flags and strings (or patterns) apply to this input until another -input flag appears. If no <code>-input</code> appears, <code>-output</code> implies &quot;-input $user_spawn_id -output&quot;. (Similarly, with patterns that do not have <code>-input</code>.) If one <code>-input</code> is specified, it overrides $user_spawn_id. If a second <code>-input</code> is specified, it overrides $spawn_id. Additional <code>-input</code> flags may be specified. </p>
<p> The two implied input processes default to having their outputs specified as $spawn_id and $user_spawn_id (in reverse). If a <code>-input</code> flag appears with no <code>-output</code> flag, characters from that process are discarded. </p>
<p> The <code>-i</code> flag introduces a replacement for the current spawn_id when no other <code>-input</code> or <code>-output</code> flags are used. A -i flag implies a -o flag. </p>
<p> It is possible to change the processes that are being interacted with by using indirect spawn ids. (Indirect spawn ids are described in the section on the expect command.) Indirect spawn ids may be specified with the -i, -u, -input, or -output flags.</p>
<dt><code>interpreter [args]</code></p>
<dd> causes the user to be interactively prompted for <code>Expect</code> and Tcl commands. The result of each command is printed.</p>
<dt>
<dd> Actions such as <code>break</code> and <code>continue</code> cause control structures (i.e., <code>for</code>, <code>proc</code>) to behave in the usual way. However <code>return</code> causes interpreter to return to its caller, while <code>inter_return</code> causes <code>interpreter</code> to cause a return in its caller. For example, if &quot;proc foo&quot; called <code>interpreter</code> which then executed the action <code>inter_return</code>, <code>proc foo</code> would return. Any other command causes <code>interpreter</code> to continue prompting for new commands.</p>
<dt>
<dd> By default, the prompt contains two integers. The first integer describes the depth of the evaluation stack (i.e., how many times Tcl_Eval has been called). The second integer is the Tcl history identifier. The prompt can be set by defining a procedure called &quot;prompt1&quot; whose return value becomes the next prompt. If a statement has open quotes, parens, braces, or brackets, a secondary prompt (by default &quot;+&gt; &quot;) is issued upon newline. The secondary prompt may be set by defining a procedure called &quot;prompt2&quot;.</p>
<dt>
<dd> During <code>interpreter</code>, cooked mode is used, even if the its caller was using raw mode.</p>
<dt>
<dd> If stdin is closed, <code>interpreter</code> will return unless the <code>-eof</code> flag is used, in which case the subsequent argument is invoked.</p>
<dt><code>log_file</code><i> [args] [[-a] file]</i></p>
<dd> If a filename is provided, <code>log_file</code> will record a transcript of the session (beginning at that point) in the file. <code>log_file</code> will stop recording if no argument is given. Any previous log file is closed. </p>
<p> Instead of a filename, a Tcl file identifier may be provided by using the <code>-open</code> or <code>-leaveopen</code> flags. This is similar to the <code>spawn</code> command. (See <code>spawn</code> for more info.) </p>
<p> The <code>-a</code> flag forces output to be logged that was suppressed by the <code>log_user</code> command. </p>
<p> By default, the <code>log_file</code> command <i>appends</i> to old files rather than truncating them, for the convenience of being able to turn logging off and on multiple times in one session. To truncate files, use the <code>-noappend</code> flag. </p>
<p> The <code>-info</code> flag causes log_file to return a description of the most recent non-info arguments given.</p>
<dt><code>log_user</code><i> -info|0|1</i></p>
<dd> By default, the send/expect dialogue is logged to stdout (and a logfile if open). The logging to stdout is disabled by the command &quot;log_user 0&quot; and reenabled by &quot;log_user 1&quot;. Logging to the logfile is unchanged. </p>
<p> The <code>-info</code> flag causes log_user to return a description of the most recent non-info arguments given.</p>
<dt><code>match_max</code><i> [-d] [-i spawn_id] [size]</i></p>
<dd> defines the size of the buffer (in bytes) used internally by <code>expect</code>. With no <i>size</i> argument, the current size is returned.</p>
<dt>
<dd> With the <code>-d</code> flag, the default size is set. (The initial default is 2000.) With the <code>-i</code> flag, the size is set for the named spawn id, otherwise it is set for the current process.</p>
<dt><code>overlay</code><i> [-# spawn_id] [-# spawn_id] [&#8230;] program [args]</i></p>
<dd> executes <i>program args</i> in place of the current <code>Expect</code> program, which terminates. A bare hyphen argument forces a hyphen in front of the command name as if it was a login shell. All spawn_ids are closed except for those named as arguments. These are mapped onto the named file identifiers.</p>
<dt>
<dd> Spawn_ids are mapped to file identifiers for the new program to inherit. For example, the following line runs chess and allows it to be controlled by the current process &#8211; say, a chess master. </p>
<pre>
    overlay -0 $spawn_id -1 $spawn_id -2 $spawn_id chess
</pre>
<p> This is more efficient than &quot;interact -u&quot;, however, it sacrifices the ability to do programmed interaction since the <code>Expect</code> process is no longer in control.</p>
<dt>
<dd> Note that no controlling terminal is provided. Thus, if you disconnect or remap standard input, programs that do job control (shells, login, etc) will not function properly.</p>
<dt><code>parity</code><i> [-d] [-i spawn_id] [value]</i></p>
<dd> defines whether parity should be retained or stripped from the output of spawned processes. If <i>value</i> is zero, parity is stripped, otherwise it is not stripped. With no <i>value</i> argument, the current value is returned.</p>
<dt>
<dd> With the <code>-d</code> flag, the default parity value is set. (The initial default is 1, i.e., parity is not stripped.) With the <code>-i</code> flag, the parity value is set for the named spawn id, otherwise it is set for the current process.</p>
<dt><code>remove_nulls</code><i> [-d] [-i spawn_id] [value]</i></p>
<dd> defines whether nulls are retained or removed from the output of spawned processes before pattern matching or storing in the variable <i>expect_out </i> or <i>interact_out</i>. If <i>value</i> is 1, nulls are removed. If <i>value</i> is 0, nulls are not removed. With no <i>value</i> argument, the current value is returned.</p>
<dt>
<dd> With the <code>-d</code> flag, the default value is set. (The initial default is 1, i.e., nulls are removed.) With the <code>-i</code> flag, the value is set for the named spawn id, otherwise it is set for the current process. </p>
<p> Whether or not nulls are removed, <code>Expect</code> will record null bytes to the log and stdout.</p>
<dt><code>send</code><i> [-flags] string</i></p>
<dd> Sends <i>string</i> to the current process. For example, the command </p>
<pre>
    send &quot;hello world&quot;
</pre>
<p> sends the characters, h e l l o &lt;blank&gt; w o r l d &lt;return&gt; to the current process. (Tcl includes a printf-like command (called <code>format</code>) which can build arbitrarily complex strings.)</p>
<dt>
<dd> Characters are sent immediately although programs with line-buffered input will not read the characters until a return character is sent. A return character is denoted &quot;&quot;. </p>
<p> The <code>&#8212;</code> flag forces the next argument to be interpreted as a string rather than a flag. Any string can be preceded by &quot;&#8211;&quot; whether or not it actually looks like a flag. This provides a reliable mechanism to specify variable strings without being tripped up by those that accidentally look like flags. (All strings starting with &quot;-&quot; are reserved for future options.) </p>
<p> The <code>-i</code> flag declares that the string be sent to the named spawn_id. If the spawn_id is <i>user_spawn_id</i>, and the terminal is in raw mode, newlines in the string are translated to return-newline sequences so that they appear as if the terminal was in cooked mode. The <code>-raw</code> flag disables this translation. </p>
<p> The <code>-null</code> flag sends null characters (0 bytes). By default, one null is sent. An integer may follow the <code>-null</code> to indicate how many nulls to send. </p>
<p> The <code>-break</code> flag generates a break condition. This only makes sense if the spawn id refers to a tty device opened via &quot;spawn -open&quot;. If you have spawned a process such as tip, you should use tip&#8217;s convention for generating a break. </p>
<p> The <code>-s</code> flag forces output to be sent &quot;slowly&quot;, thus avoid the common situation where a computer outtypes an input buffer that was designed for a human who would never outtype the same buffer. This output is controlled by the value of the variable &quot;send_slow&quot; which takes a two element list. The first element is an integer that describes the number of bytes to send atomically. The second element is a real number that describes the number of seconds by which the atomic sends must be separated. For example, &quot;set send_slow {10 .001}&quot; would force &quot;send -s&quot; to send strings with 1 millisecond in between each 10 characters sent. </p>
<p> The <code>-h</code> flag forces output to be sent (somewhat) like a human actually typing. Human-like delays appear between the characters. (The algorithm is based upon a Weibull distribution, with modifications to suit this particular application.) This output is controlled by the value of the variable &quot;send_human&quot; which takes a five element list. The first two elements are average interarrival time of characters in seconds. The first is used by default. The second is used at word endings, to simulate the subtle pauses that occasionally occur at such transitions. The third parameter is a measure of variability where .1 is quite variable, 1 is reasonably variable, and 10 is quite invariable. The extremes are 0 to infinity. The last two parameters are, respectively, a minimum and maximum interarrival time. The minimum and maximum are used last and &quot;clip&quot; the final time. The ultimate average can be quite different from the given average if the minimum and maximum clip enough values. </p>
<p> As an example, the following command emulates a fast and consistent typist: </p>
<pre>
    set send_human {.1 .3 1 .05 2}
    send -h &quot;I'm hungry.  Let's do lunch.&quot;
</pre>
<p> while the following might be more suitable after a hangover: </p>
<pre>
    set send_human {.4 .4 .2 .5 100}
    send -h &quot;Goodd party lash night!&quot;
</pre>
<p> Note that errors are not simulated, although you can set up error correction situations yourself by embedding mistakes and corrections in a send argument. </p>
<p> The flags for sending null characters, for sending breaks, for forcing slow output and for human-style output are mutually exclusive. Only the one specified last will be used. Furthermore, no <i>string</i> argument can be specified with the flags for sending null characters or breaks. </p>
<p> It is a good idea to precede the first <code>send</code> to a process by an <code>expect</code>. <code>expect</code> will wait for the process to start, while <code>send</code> cannot. In particular, if the first <code>send</code> completes before the process starts running, you run the risk of having your data ignored. In situations where interactive programs offer no initial prompt, you can precede <code>send</code> by a delay as in: </p>
<pre>
    # To avoid giving hackers hints on how to break in,
    # this system does not prompt for an external password.
    # Wait for 5 seconds for exec to complete
    spawn telnet very.secure.gov
    sleep 5
    send password
</pre>
<p> <code>exp_send</code> is an alias for <code>send</code><i>.</i> If you are using Expectk or some other variant of Expect in the Tk environment, <code>send</code> is defined by Tk for an entirely different purpose. <code>exp_send</code> is provided for compatibility between environments. Similar aliases are provided for other Expect&#8217;s other send commands.</p>
<dt><code>send_error</code><i> [-flags] string</i></p>
<dd> is like <code>send</code>, except that the output is sent to stderr rather than the current process.</p>
<dt><code>send_log</code><i> [&#8211;] string</i></p>
<dd> is like <code>send</code>, except that the string is only sent to the log file (see <code>log_file</code>.) The arguments are ignored if no log file is open.</p>
<dt><code>send_tty</code><i> [-flags] string</i></p>
<dd> is like <code>send</code>, except that the output is sent to /dev/tty rather than the current process.</p>
<dt><code>send_user</code><i> [-flags] string</i></p>
<dd> is like <code>send</code>, except that the output is sent to stdout rather than the current process.</p>
<dt><code>sleep</code><i> seconds</i></p>
<dd> causes the script to sleep for the given number of seconds. Seconds may be a decimal number. Interrupts (and Tk events if you are using Expectk) are processed while Expect sleeps.</p>
<dt><code>spawn</code><i> [args] program [args]</i></p>
<dd> creates a new process running <i>program args</i>. Its stdin, stdout and stderr are connected to Expect, so that they may be read and written by other <code>Expect</code> commands. The connection is broken by <code>close</code> or if the process itself closes any of the file identifiers.</p>
<dt>
<dd> When a process is started by <code>spawn</code>, the variable <i>spawn_id</i> is set to a descriptor referring to that process. The process described by <i>spawn_id</i> is considered the <i>current process</i>. <i>spawn_id</i> may be read or written, in effect providing job control.</p>
<dt>
<dd> <i>user_spawn_id</i> is a global variable containing a descriptor which refers to the user. For example, when <i>spawn_id</i> is set to this value, <code>expect</code> behaves like <code>expect_user</code>. </p>
<p> <i>error_spawn_id</i> is a global variable containing a descriptor which refers to the standard error. For example, when <i>spawn_id</i> is set to this value, <code>send</code> behaves like <code>send_error</code>.</p>
<dt>
<dd> <i>tty_spawn_id</i> is a global variable containing a descriptor which refers to /dev/tty. If /dev/tty does not exist (such as in a cron, at, or batch script), then <i>tty_spawn_id</i> is not defined. This may be tested as:<br />
if {<br />
    [info vars tty_spawn_id]<br />
}<br />
{<br />
#/ dev / tty exists<br />
}<br />
else<br />
{<br />
#/ dev / tty doesn&#8217;t exist<br />
#probably in cron, batch, or at script<br />
}</p>
<dt>
<dd> <code>spawn</code> returns the UNIX process id. If no process is spawned, 0 is returned. The variable <i>spawn_out(slave,name)</i> is set to the name of the pty slave device.</p>
<dt>
<dd> By default, <code>spawn</code> echoes the command name and arguments. The <code>-noecho</code> flag stops <code>spawn</code> from doing this.</p>
<dt>
<dd> The <code>-console</code> flag causes console output to be redirected to the spawned process. This is not supported on all systems. </p>
<p> Internally, <code>spawn</code> uses a pty, initialized the same way as the user&#8217;s tty. This is further initialized so that all settings are &quot;sane&quot; (according to <a href="/docs/linux/man/1-stty/">stty</a>(1)). If the variable <i>stty_init</i> is defined, it is interpreted in the style of stty arguments as further configuration. For example, &quot;set stty_init raw&quot; will cause further spawned processes&#8217;s terminals to start in raw mode. <code>-nottycopy</code> skips the initialization based on the user&#8217;s tty. <code>-nottyinit</code> skips the &quot;sane&quot; initialization.</p>
<dt>
<dd> Normally, <code>spawn</code> takes little time to execute. If you notice spawn taking a significant amount of time, it is probably encountering ptys that are wedged. A number of tests are run on ptys to avoid entanglements with errant processes. (These take 10 seconds per wedged pty.) Running Expect with the <code>-d</code> option will show if <code>Expect</code> is encountering many ptys in odd states. If you cannot kill the processes to which these ptys are attached, your only recourse may be to reboot. </p>
<p> If <i>program</i> cannot be spawned successfully because <a href="/docs/linux/man/2-exec/">exec</a>(2) fails (e.g. when <i>program</i> doesn&#8217;t exist), an error message will be returned by the next <code>interact</code> or <code>expect</code> command as if <i>program</i> had run and produced the error message as output. This behavior is a natural consequence of the implementation of <code>spawn</code>. Internally, spawn forks, after which the spawned process has no way to communicate with the original <code>Expect</code> process except by communication via the spawn_id. </p>
<p> The <code>-open</code> flag causes the next argument to be interpreted as a Tcl file identifier (i.e., returned by <code>open</code>.) The spawn id can then be used as if it were a spawned process. (The file identifier should no longer be used.) This lets you treat raw devices, files, and pipelines as spawned processes without using a pty. 0 is returned to indicate there is no associated process. When the connection to the spawned process is closed, so is the Tcl file identifier. The <code>-leaveopen</code> flag is similar to <code>-open</code> except that <code>-leaveopen</code> causes the file identifier to be left open even after the spawn id is closed. </p>
<p> The <code>-pty</code> flag causes a pty to be opened but no process spawned. 0 is returned to indicate there is no associated process. Spawn_id is set as usual. </p>
<p> The variable <i>spawn_out(slave,fd)</i> is set to a file identifier corresponding to the pty slave. It can be closed using &quot;close -slave&quot;. </p>
<p> The <code>-ignore</code> flag names a signal to be ignored in the spawned process. Otherwise, signals get the default behavior. Signals are named as in the <code>trap</code> command, except that each signal requires a separate flag.</p>
<dt><code>strace</code><i> level</i></p>
<dd> causes following statements to be printed before being executed. (Tcl&#8217;s trace command traces variables.) <i>level</i> indicates how far down in the call stack to trace. For example, the following command runs <code>Expect</code> while tracing the first 4 levels of calls, but none below that. </p>
<pre>
    expect -c &quot;strace 4&quot; script.exp
</pre>
<p> The <code>-info</code> flag causes strace to return a description of the most recent non-info arguments given.</p>
<dt><code>stty</code><i> args</i></p>
<dd> changes terminal modes similarly to the external stty command. </p>
<p> By default, the controlling terminal is accessed. Other terminals can be accessed by appending &quot;&lt; /dev/tty&#8230;&quot; to the command. (Note that the arguments should not be grouped into a single argument.) </p>
<p> Requests for status return it as the result of the command. If no status is requested and the controlling terminal is accessed, the previous status of the raw and echo attributes are returned in a form which can later be used by the command. </p>
<p> For example, the arguments <code>raw</code> or <code>-cooked</code> put the terminal into raw mode. The arguments <code>-raw</code> or <code>cooked</code> put the terminal into cooked mode. The arguments <code>echo</code> and <code>-echo</code> put the terminal into echo and noecho mode respectively.</p>
<dt>
<dd> The following example illustrates how to temporarily disable echoing. This could be used in otherwise-automatic scripts to avoid embedding passwords in them. (See more discussion on this under EXPECT HINTS below.) </p>
<pre>
    stty -echo
    send_user &quot;Password: &quot;
    expect_user -re &quot;(.*)
&quot;
    set password $expect_out(1,string)
    stty echo
</pre>
<dt><code>system</code><i> args</i></p>
<dd> gives <i>args</i> to <a href="/docs/linux/man/1-sh/">sh</a>(1) as input, just as if it had been typed as a command from a terminal. <code>Expect</code> waits until the shell terminates. The return status from sh is handled the same way that <code>exec</code> handles its return status.</p>
<dt>
<dd> In contrast to <code>exec</code> which redirects stdin and stdout to the script, <code>system</code> performs no redirection (other than that indicated by the string itself). Thus, it is possible to use programs which must talk directly to /dev/tty. For the same reason, the results of <code>system</code> are not recorded in the log.</p>
<dt><code>timestamp</code><i> [args]</i></p>
<dd> returns a timestamp. With no arguments, the number of seconds since the epoch is returned. </p>
<p> The <code>-format</code> flag introduces a string which is returned but with substitutions made according to the POSIX rules for strftime. For example %a is replaced by an abbreviated weekday name (i.e., Sat). Others are: </p>
<pre>
    %a      abbreviated weekday name
    %A      full weekday name
    %b      abbreviated month name
    %B      full month name
    %c      date-time as in: Wed Oct  6 11:45:56 1993
    %d      day of the month (01-31)
    %H      hour (00-23)
    %I      hour (01-12)
    %j      day (001-366)
    %m      month (01-12)
    %M      minute (00-59)
    %p      am or pm
    %S      second (00-61)
    %u      day (1-7, Monday is first day of week)
    %U      week (00-53, first Sunday is first day of week one)
    %V      week (01-53, ISO 8601 style)
    %w      day (0-6)
    %W      week (00-53, first Monday is first day of week one)
    %x      date-time as in: Wed Oct  6 1993
    %X      time as in: 23:59:59
    %y      year (00-99)
    %Y      year as in: 1993
    %Z      timezone (or nothing if not determinable)
    %%      a bare percent sign
</pre>
<p> Other % specifications are undefined. Other characters will be passed through untouched. Only the C locale is supported. </p>
<p> The <code>-seconds</code> flag introduces a number of seconds since the epoch to be used as a source from which to format. Otherwise, the current time is used. </p>
<p> The <code>-gmt</code> flag forces timestamp output to use the GMT timezone. With no flag, the local timezone is used.</p>
<dt><code>trap</code><i> [[command] signals]</i></p>
<dd> causes the given <i>command</i> to be executed upon future receipt of any of the given signals. The command is executed in the global scope. If <i>command</i> is absent, the signal action is returned. If <i>command </i> is the string SIG_IGN, the signals are ignored. If <i>command</i> is the string SIG_DFL, the signals are result to the system default. <i>signals</i> is either a single signal or a list of signals. Signals may be specified numerically or symbolically as per <a href="/docs/linux/man/3-signal/">signal</a>(3). The &quot;SIG&quot; prefix may be omitted. </p>
<p> With no arguments (or the argument -number), <code>trap</code> returns the signal number of the trap command currently being executed. </p>
<p> The <code>-code</code> flag uses the return code of the command in place of whatever code Tcl was about to return when the command originally started running. </p>
<p> The <code>-interp</code> flag causes the command to be evaluated using the interpreter active at the time the command started running rather than when the trap was declared. </p>
<p> The <code>-name</code> flag causes the <code>trap</code> command to return the signal name of the trap command currently being executed. </p>
<p> The <code>-max</code> flag causes the <code>trap</code> command to return the largest signal number that can be set. </p>
<p> For example, the command &quot;trap {send_user &quot;Ouch!&quot;} SIGINT&quot; will print &quot;Ouch!&quot; each time the user presses ^C. </p>
<p> By default, SIGINT (which can usually be generated by pressing ^C) and SIGTERM cause Expect to exit. This is due to the following trap, created by default when Expect starts. </p>
<pre>
    trap exit {SIGINT SIGTERM}
</pre>
<p> If you use the -D flag to start the debugger, SIGINT is redefined to start the interactive debugger. This is due to the following trap: </p>
<pre>
    trap {exp_debug 1} SIGINT
</pre>
<p> The debugger trap can be changed by setting the environment variable EXPECT_DEBUG_INIT to a new trap command. </p>
<p> You can, of course, override both of these just by adding trap commands to your script. In particular, if you have your own &quot;trap exit SIGINT&quot;, this will override the debugger trap. This is useful if you want to prevent users from getting to the debugger at all. </p>
<p> If you want to define your own trap on SIGINT but still trap to the debugger when it is running, use:<br />
if {<br />
    ![exp_debug]<br />
}<br />
{<br />
    trap mystuff SIGINT<br />
}<br />
 Alternatively, you can trap to the debugger using some other signal. </p>
<p> <code>trap</code> will not let you override the action for SIGALRM as this is used internally to <code>Expect</code>. The disconnect command sets SIGALRM to SIG_IGN (ignore). You can reenable this as long as you disable it during subsequent spawn commands. </p>
<p> See <a href="/docs/linux/man/3-signal/">signal</a>(3) for more info.</p>
<dt><code>wait</code><i> [args]</i></p>
<dd> delays until a spawned process (or the current process if none is named) terminates.</p>
<dt>
<dd> <code>wait</code> normally returns a list of four integers. The first integer is the pid of the process that was waited upon. The second integer is the corresponding spawn id. The third integer is -1 if an operating system error occurred, or 0 otherwise. If the third integer was 0, the fourth integer is the status returned by the spawned process. If the third integer was -1, the fourth integer is the value of errno set by the operating system. The global variable errorCode is also set. </p>
<p> Additional elements may appear at the end of the return value from <code>wait</code>. An optional fifth element identifies a class of information. Currently, the only possible value for this element is CHILDKILLED in which case the next two values are the C-style signal name and a short textual description.</p>
<dt>
<dd> The <code>-i</code> flag declares the process to wait corresponding to the named spawn_id (NOT the process id). Inside a SIGCHLD handler, it is possible to wait for any spawned process by using the spawn id -1. </p>
<p> The <code>-nowait</code> flag causes the wait to return immediately with the indication of a successful wait. When the process exits (later), it will automatically disappear without the need for an explicit wait. </p>
<p> The <code>wait</code> command may also be used wait for a forked process using the arguments &quot;-i -1&quot;. Unlike its use with spawned processes, this command can be executed at any time. There is no control over which process is reaped. However, the return value can be checked for the process id. </p>
</dl>
<h2>LIBRARIES</h2>
<p> Expect automatically knows about two built-in libraries for Expect scripts. These are defined by the directories named in the variables exp_library and exp_exec_library. Both are meant to contain utility files that can be used by other scripts. </p>
<p> exp_library contains architecture-independent files. exp_exec_library contains architecture-dependent files. Depending on your system, both directories may be totally empty. The existence of the file $exp_exec_library/cat-buffers describes whether your /bin/cat buffers by default.</p>
<h2>PRETTY-PRINTING</h2>
<p> A vgrind definition is available for pretty-printing <code>Expect</code> scripts. Assuming the vgrind definition supplied with the <code>Expect</code> distribution is correctly installed, you can use it as: </p>
<pre>
    vgrind -lexpect file
</pre>
<h2>EXAMPLES</h2>
<p> It many not be apparent how to put everything together that the man page describes. I encourage you to read and try out the examples in the example directory of the <code>Expect</code> distribution. Some of them are real programs. Others are simply illustrative of certain techniques, and of course, a couple are just quick hacks. The INSTALL file has a quick overview of these programs. </p>
<p> The <code>Expect</code> papers (see SEE ALSO) are also useful. While some papers use syntax corresponding to earlier versions of Expect, the accompanying rationales are still valid and go into a lot more detail than this man page.</p>
<h2>CAVEATS</h2>
<p> Extensions may collide with Expect&#8217;s command names. For example, <code>send</code> is defined by Tk for an entirely different purpose. For this reason, most of the <code>Expect</code> commands are also available as &quot;exp_XXXX&quot;. Commands and variables beginning with &quot;exp&quot;, &quot;inter&quot;, &quot;spawn&quot;, and &quot;timeout&quot; do not have aliases. Use the extended command names if you need this compatibility between environments. </p>
<p> <code>Expect</code> takes a rather liberal view of scoping. In particular, variables read by commands specific to the <code>Expect</code> program will be sought first from the local scope, and if not found, in the global scope. For example, this obviates the need to place &quot;global timeout&quot; in every procedure you write that uses <code>expect</code>. On the other hand, variables written are always in the local scope (unless a &quot;global&quot; command has been issued). The most common problem this causes is when spawn is executed in a procedure. Outside the procedure, <i>spawn_id</i> no longer exists, so the spawned process is no longer accessible simply because of scoping. Add a &quot;global spawn_id&quot; to such a procedure. </p>
<p> If you cannot enable the multispawning capability (i.e., your system supports neither select (BSD *.*), poll (SVR&gt;2), nor something equivalent), <code>Expect</code> will only be able to control a single process at a time. In this case, do not attempt to set <i>spawn_id</i>, nor should you execute processes via exec while a spawned process is running. Furthermore, you will not be able to <code>expect</code> from multiple processes (including the user as one) at the same time. </p>
<p> Terminal parameters can have a big effect on scripts. For example, if a script is written to look for echoing, it will misbehave if echoing is turned off. For this reason, Expect forces sane terminal parameters by default. Unfortunately, this can make things unpleasant for other programs. As an example, the emacs shell wants to change the &quot;usual&quot; mappings: newlines get mapped to newlines instead of carriage-return newlines, and echoing is disabled. This allows one to use emacs to edit the input line. Unfortunately, Expect cannot possibly guess this. </p>
<p> You can request that Expect not override its default setting of terminal parameters, but you must then be very careful when writing scripts for such environments. In the case of emacs, avoid depending upon things like echoing and end-of-line mappings. </p>
<p> The commands that accepted arguments braced into a single list (the <code>expect</code> variants and <code>interact</code>) use a heuristic to decide if the list is actually one argument or many. The heuristic can fail only in the case when the list actually does represent a single argument which has multiple embedded 
&#8217;s with non-whitespace characters between them. This seems sufficiently improbable, however the argument &quot;-nobrace&quot; can be used to force a single argument to be handled as a single argument. This could conceivably be used with machine-generated Expect code. Similarly, -brace forces a single argument to be handle as multiple patterns/actions. </p>
<h2>BUGS</h2>
<p> It was really tempting to name the program &quot;sex&quot; (for either &quot;Smart EXec&quot; or &quot;Send-EXpect&quot;), but good sense (or perhaps just Puritanism) prevailed. </p>
<p> On some systems, when a shell is spawned, it complains about not being able to access the tty but runs anyway. This means your system has a mechanism for gaining the controlling tty that <code>Expect</code> doesn&#8217;t know about. Please find out what it is, and send this information back to me. </p>
<p> Ultrix 4.1 (at least the latest versions around here) considers timeouts of above 1000000 to be equivalent to 0. </p>
<p> Digital UNIX 4.0A (and probably other versions) refuses to allocate ptys if you define a SIGCHLD handler. See grantpt page for more info. </p>
<p> IRIX 6.0 does not handle pty permissions correctly so that if Expect attempts to allocate a pty previously used by someone else, it fails. Upgrade to IRIX 6.1. </p>
<p> Telnet (verified only under SunOS 4.1.2) hangs if TERM is not set. This is a problem under cron, at and in cgi scripts, which do not define TERM. Thus, you must set it explicitly &#8211; to what type is usually irrelevant. It just has to be set to something! The following probably suffices for most cases. </p>
<pre>
    set env(TERM) vt100
</pre>
<p> Tip (verified only under BSDI BSD/OS 3.1 i386) hangs if SHELL and HOME are not set. This is a problem under cron, at and in cgi scripts, which do not define these environment variables. Thus, you must set them explicitly &#8211; to what type is usually irrelevant. It just has to be set to something! The following probably suffices for most cases. </p>
<pre>
    set env(SHELL) /bin/sh
    set env(HOME) /usr/bin
</pre>
<p> Some implementations of ptys are designed so that the kernel throws away any unread output after 10 to 15 seconds (actual number is implementation-dependent) after the process has closed the file descriptor. Thus <code>Expect</code> programs such as </p>
<pre>
    spawn date
    sleep 20
    expect
</pre>
<p> will fail. To avoid this, invoke non-interactive programs with <code>exec</code> rather than <code>spawn</code>. While such situations are conceivable, in practice I have never encountered a situation in which the final output of a truly interactive program would be lost due to this behavior. </p>
<p> On the other hand, Cray UNICOS ptys throw away any unread output immediately after the process has closed the file descriptor. I have reported this to Cray and they are working on a fix. </p>
<p> Sometimes a delay is required between a prompt and a response, such as when a tty interface is changing UART settings or matching baud rates by looking for start/stop bits. Usually, all this is require is to sleep for a second or two. A more robust technique is to retry until the hardware is ready to receive input. The following example uses both strategies:<br />
send &#8220;speed 9600&#8221;;<br />
sleep 1 expect<br />
{<br />
    timeout<br />
    {<br />
        send &#8220;&#8221;;<br />
        exp_continue<br />
    }<br />
    $prompt<br />
}</p>
<p> trap -code will not work with any command that sits in Tcl&#8217;s event loop, such as sleep. The problem is that in the event loop, Tcl discards the return codes from async event handlers. A workaround is to set a flag in the trap code. Then check the flag immediately after the command (i.e., sleep). </p>
<p> The expect_background command ignores -timeout arguments and has no concept of timeouts in general. </p>
<h2>EXPECT HINTS</h2>
<p> There are a couple of things about <code>Expect</code> that may be non-intuitive. This section attempts to address some of these things with a couple of suggestions. </p>
<p> A common expect problem is how to recognize shell prompts. Since these are customized differently by differently people and different shells, portably automating rlogin can be difficult without knowing the prompt. A reasonable convention is to have users store a regular expression describing their prompt (in particular, the end of it) in the environment variable EXPECT_PROMPT. Code like the following can be used. If EXPECT_PROMPT doesn&#8217;t exist, the code still has a good chance of functioning correctly. </p>
<pre><code>
set prompt "(%|#|\$) $";
#default prompt catch {set prompt $env(EXPECT_PROMPT) } expect - re $prompt
</code></pre>
<p> I encourage you to write <code>expect</code> patterns that include the end of whatever you expect to see. This avoids the possibility of answering a question before seeing the entire thing. In addition, while you may well be able to answer questions before seeing them entirely, if you answer early, your answer may appear echoed back in the middle of the question. In other words, the resulting dialogue will be correct but look scrambled. </p>
<p> Most prompts include a space character at the end. For example, the prompt from ftp is &#8216;f&#8217;, &#8216;t&#8217;, &#8216;p&#8217;, &#8216;&gt;&#8217; and &lt;blank&gt;. To match this prompt, you must account for each of these characters. It is a common mistake not to include the blank. Put the blank in explicitly. </p>
<p> If you use a pattern of the form X*, the * will match all the output received from the end of X to the last thing received. This sounds intuitive but can be somewhat confusing because the phrase &quot;last thing received&quot; can vary depending upon the speed of the computer and the processing of I/O both by the kernel and the device driver. </p>
<p> In particular, humans tend to see program output arriving in huge chunks (atomically) when in reality most programs produce output one line at a time. Assuming this is the case, the * in the pattern of the previous paragraph may only match the end of the current line even though there seems to be more, because at the time of the match that was all the output that had been received. </p>
<p> <code>expect</code> has no way of knowing that further output is coming unless your pattern specifically accounts for it. </p>
<p> Even depending on line-oriented buffering is unwise. Not only do programs rarely make promises about the type of buffering they do, but system indigestion can break output lines up so that lines break at seemingly random places. Thus, if you can express the last few characters of a prompt when writing patterns, it is wise to do so. </p>
<p> If you are waiting for a pattern in the last output of a program and the program emits something else instead, you will not be able to detect that with the <code>timeout</code> keyword. The reason is that <code>expect</code> will not timeout &#8211; instead it will get an <code>eof</code> indication. Use that instead. Even better, use both. That way if that line is ever moved around, you won&#8217;t have to edit the line itself. </p>
<p> Newlines are usually converted to carriage return, linefeed sequences when output by the terminal driver. Thus, if you want a pattern that explicitly matches the two lines, from, say, printf(&quot;foo
bar&quot;), you should use the pattern &quot;foo
bar&quot;. </p>
<p> A similar translation occurs when reading from the user, via <code>expect_user</code>. In this case, when you press return, it will be translated to a newline. If <code>Expect</code> then passes that to a program which sets its terminal to raw mode (like telnet), there is going to be a problem, as the program expects a true return. (Some programs are actually forgiving in that they will automatically translate newlines to returns, but most don&#8217;t.) Unfortunately, there is no way to find out that a program put its terminal into raw mode. </p>
<p> Rather than manually replacing newlines with returns, the solution is to use the command &quot;stty raw&quot;, which will stop the translation. Note, however, that this means that you will no longer get the cooked line-editing features. </p>
<p> <code>interact</code> implicitly sets your terminal to raw mode so this problem will not arise then. </p>
<p> It is often useful to store passwords (or other private information) in <code>Expect</code> scripts. This is not recommended since anything that is stored on a computer is susceptible to being accessed by anyone. Thus, interactively prompting for passwords from a script is a smarter idea than embedding them literally. Nonetheless, sometimes such embedding is the only possibility. </p>
<p> Unfortunately, the UNIX file system has no direct way of creating scripts which are executable but unreadable. Systems which support setgid shell scripts may indirectly simulate this as follows: </p>
<p> Create the <code>Expect</code> script (that contains the secret data) as usual. Make its permissions be 750 (-rwxr-x&#8212;) and owned by a trusted group, i.e., a group which is allowed to read it. If necessary, create a new group for this purpose. Next, create a /bin/sh script with permissions 2751 (-rwxr-s&#8211;x) owned by the same group as before. </p>
<p> The result is a script which may be executed (and read) by anyone. When invoked, it runs the <code>Expect</code> script.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-tcl/">Tcl</a></code>(3), <code><a href="/docs/linux/man/3-libexpect/">libexpect</a></code>(3)<br />
 <i>&quot;Exploring Expect: A Tcl-Based Toolkit for Automating Interactive Programs&quot;</i> by Don Libes, pp. 602, ISBN 1-56592-090-2, O&#8217;Reilly and Associates, 1995.<br />
 <i>&quot;expect: Curing Those Uncontrollable Fits of Interactivity&quot; </i>by Don Libes, Proceedings of the Summer 1990 USENIX Conference, Anaheim, California, June 11-15, 1990.<br />
 <i>&quot;Using</i> <code>expect</code> to Automate System Administration Tasks&quot; by Don Libes, Proceedings of the 1990 USENIX Large Installation Systems Administration Conference, Colorado Springs, Colorado, October 17-19, 1990.<br />
 <i>&quot;Tcl: An Embeddable Command Language&quot; </i>by John Ousterhout, Proceedings of the Winter 1990 USENIX Conference, Washington, D.C., January 22-26, 1990.<br />
 <i>&quot;expect: Scripts for Controlling Interactive Programs&quot; </i>by Don Libes, Computing Systems, Vol. 4, No. 2, University of California Press Journals, November 1991.<br />
 <i>&quot;Regression Testing and Conformance Testing Interactive Programs&quot;, </i>by Don Libes, Proceedings of the Summer 1992 USENIX Conference, pp. 135-144, San Antonio, TX, June 12-15, 1992.<br />
 <i>&quot;Kibitz &#8211; Connecting Multiple Interactive Programs Together&quot;, </i>by Don Libes, Software &#8211; Practice &amp; Experience, John Wiley &amp; Sons, West Sussex, England, Vol. 23, No. 5, May, 1993.<br />
 <i>&quot;A Debugger for Tcl Applications&quot;, </i>by Don Libes, Proceedings of the 1993 Tcl/Tk Workshop, Berkeley, CA, June 10-11, 1993.</p>
<h2>AUTHOR</h2>
<p> Don Libes, National Institute of Standards and Technology</p>
<h2>ACKNOWLEDGMENTS</h2>
<p> Thanks to John Ousterhout for Tcl, and Scott Paisley for inspiration. Thanks to Rob Savoye for Expect&#8217;s autoconfiguration code. </p>
<p> The HISTORY file documents much of the evolution of <code>expect</code>. It makes interesting reading and might give you further insight to this software. Thanks to the people mentioned in it who sent me bug fixes and gave other assistance. </p>
<p> Design and implementation of <code>Expect</code> was paid for in part by the U.S. government and is therefore in the public domain. However the author and NIST would like credit if this program and documentation or portions of them are used. </p>
<h2>Index</h2>
