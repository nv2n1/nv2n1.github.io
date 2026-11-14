---
title: "xargs(1)"
name: "xargs"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xargs/"
description: "xargs – build and execute command lines from standard input"
---

<h2 class="name">NAME</h2>
<p> xargs &#8211; build and execute command lines from standard input </p>
<h2>SYNOPSIS</h2>
<p> <code>xargs</code> [<i>options</i>] [<i>command</i> [<i>initial-arguments</i>]]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents the GNU version of <code>xargs</code>. <code>xargs</code> reads items from the standard input, delimited by blanks (which can be protected with double or single quotes or a backslash) or newlines, and executes the <i>command</i> (default is <i>/bin/echo</i>) one or more times with any <i>initial-arguments</i> followed by items read from standard input. Blank lines on the standard input are ignored. </p>
<p> The command line for <i>command</i> is built up until it reaches a system-defined limit (unless the <code>-n</code> and <code>-L</code> options are used). The specified <i>command</i> will be invoked as many times as necessary to use up the list of input items. In general, there will be many fewer invocations of <i>command</i> than there were items in the input. This will normally have significant performance benefits. Some commands can usefully be executed in parallel too; see the <code>-P</code> option. </p>
<p> Because Unix filenames can contain blanks and newlines, this default behaviour is often problematic; filenames containing blanks and/or newlines are incorrectly processed by <code>xargs</code>. In these situations it is better to use the <code>-0</code> option, which prevents such problems. When using this option you will need to ensure that the program which produces the input for <code>xargs</code> also uses a null character as a separator. If that program is GNU <code>find</code> for example, the <code>-print0</code> option does this for you. </p>
<p> If any invocation of the command exits with a status of 255, <code>xargs</code> will stop immediately without reading any further input. An error message is issued on stderr when this happens.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-0, &#8211;null</code></p>
<dd> Input items are terminated by a null character instead of by whitespace, and the quotes and backslash are not special (every character is taken literally). Disables the end of file string, which is treated like any other argument. Useful when input items might contain white space, quote marks, or backslashes. The GNU find -print0 option produces input suitable for this mode. </p>
<dt><code>-a </code><i>file</i><code>, &#8211;arg-file=</code><i>file</i></p>
<dd> Read items from <i>file</i> instead of standard input. If you use this option, stdin remains unchanged when commands are run. Otherwise, stdin is redirected from <i>/dev/null</i>. </p>
<dt><code>&#8211;delimiter=</code><i>delim</i><code>, -d</code><i> delim</i></p>
<dd> Input items are terminated by the specified character. The specified delimiter may be a single character, a C-style character escape such as <code>
</code>, or an octal or hexadecimal escape code. Octal and hexadecimal escape codes are understood as for the <code>printf</code> command. Multibyte characters are not supported. When processing the input, quotes and backslash are not special; every character in the input is taken literally. The <code>-d</code> option disables any end-of-file string, which is treated like any other argument. You can use this option when the input consists of simply newline-separated items, although it is almost always better to design your program to use <code>&#8211;null</code> where this is possible. </p>
<dt><code>-E</code><i> eof-str</i></p>
<dd> Set the end of file string to <i>eof-str</i>. If the end of file string occurs as a line of input, the rest of the input is ignored. If neither <code>-E</code> nor <code>-e</code> is used, no end of file string is used.</p>
<dt><code>-e</code>[<i>eof-str</i>], <code>&#8211;eof</code>[<i>=eof-str</i>]</p>
<dd> This option is a synonym for the <code>-E</code> option. Use <code>-E</code> instead, because it is POSIX compliant while this option is not. If <i>eof-str</i> is omitted, there is no end of file string. If neither <code>-E</code> nor <code>-e</code> is used, no end of file string is used.</p>
<dt><code>-I</code><i> replace-str</i></p>
<dd> Replace occurrences of <i>replace-str</i> in the initial-arguments with names read from standard input. Also, unquoted blanks do not terminate input items; instead the separator is the newline character. Implies <code>-x</code> and <code>-L</code> 1.</p>
<dt><code>-i</code>[<i>replace-str</i>], <code>&#8211;replace</code>[<i>=replace-str</i>]</p>
<dd> This option is a synonym for <code>-I</code><i>replace-str</i> if <i>replace-str</i> is specified. If the <i>replace-str</i> argument is missing, the effect is the same as <code>-I</code>{}. This option is deprecated; use <code>-I</code> instead.</p>
<dt><code>-L</code><i> max-lines</i></p>
<dd> Use at most <i>max-lines</i> nonblank input lines per command line. Trailing blanks cause an input line to be logically continued on the next input line. Implies <code>-x</code>.</p>
<dt><code>-l</code>[<i>max-lines</i>], <code>&#8211;max-lines</code>[=<i>max-lines</i>]</p>
<dd> Synonym for the <code>-L</code> option. Unlike <code>-L</code>, the <i>max-lines</i> argument is optional. If <i>max-lines</i> is not specified, it defaults to one. The <code>-l</code> option is deprecated since the POSIX standard specifies <code>-L</code> instead.</p>
<dt><code>-n</code><i> max-args</i><code>, </code><i></i><code>&#8211;max-args</code><i></i>=<i>max-args</i></p>
<dd> Use at most <i>max-args</i> arguments per command line. Fewer than <i>max-args</i> arguments will be used if the size (see the <code>-s</code> option) is exceeded, unless the <code>-x</code> option is given, in which case <code>xargs will exit.</code></p>
<dt><code>-P</code><i> max-procs</i>, <i></i><code>&#8211;max-procs</code><i></i>=<i>max-procs</i></p>
<dd> Run up to <i>max-procs</i> processes at a time; the default is 1. If <i>max-procs</i> is 0, <code>xargs</code> will run as many processes as possible at a time. Use the <code>-n</code> option or the <code>-L</code> option with <code>-P</code>; otherwise chances are that only one exec will be done. While <code>xargs</code> is running, you can send its process a SIGUSR1 signal to increase the number of commands to run simultaneously, or a SIGUSR2 to decrease the number. You cannot increase it above an implementation-defined limit (which is shown with &#8211;show-limits). You cannot decrease it below 1. <code>xargs</code> never terminates its commands; when asked to decrease, it merely waits for more than one existing command to terminate before starting another. </p>
<p> <code>Please note</code> that it is up to the called processes to properly manage parallel access to shared resources. For example, if more than one of them tries to print to stdout, the output will be produced in an indeterminate order (and very likely mixed up) unless the processes collaborate in some way to prevent this. Using some kind of locking scheme is one way to prevent such problems. In general, using a locking scheme will help ensure correct output but reduce performance. If you don&#8217;t want to tolerate the performance difference, simply arrange for each process to produce a separate output file (or otherwise use separate resources).</p>
<dt><code>-o, &#8211;open-tty</code></p>
<dd> Reopen stdin as <i>/dev/tty</i> in the child process before executing the command. This is useful if you want <code>xargs</code> to run an interactive application.</p>
<dt><code>-p, &#8211;interactive</code></p>
<dd> Prompt the user about whether to run each command line and read a line from the terminal. Only run the command line if the response starts with `y&#8217; or `Y&#8217;. Implies <code>-t</code>.</p>
<dt><code>&#8211;process-slot-var</code>=<i>name</i></p>
<dd> Set the environment variable <i>name</i> to a unique value in each running child process. Values are reused once child processes exit. This can be used in a rudimentary load distribution scheme, for example.</p>
<dt><code>-r, &#8211;no-run-if-empty</code></p>
<dd> If the standard input does not contain any nonblanks, do not run the command. Normally, the command is run once even if there is no input. This option is a GNU extension.</p>
<dt><code>-s</code><i> max-chars</i>, <i></i><code>&#8211;max-chars</code><i>=max-chars</i></p>
<dd> Use at most <i>max-chars</i> characters per command line, including the command and initial-arguments and the terminating nulls at the ends of the argument strings. The largest allowed value is system-dependent, and is calculated as the argument length limit for exec, less the size of your environment, less 2048 bytes of headroom. If this value is more than 128KiB, 128Kib is used as the default value; otherwise, the default value is the maximum. 1KiB is 1024 bytes. <code>xargs</code> automatically adapts to tighter constraints.</p>
<dt><code>&#8211;show\-limits</code></p>
<dd> Display the limits on the command-line length which are imposed by the operating system, <code>xargs</code>&#8216; choice of buffer size and the <code>-s</code> option. Pipe the input from <i>/dev/null</i> (and perhaps specify <code>&#8211;no-run-if-empty</code>) if you don&#8217;t want <code>xargs</code> to do anything.</p>
<dt><code>-t, &#8211;verbose</code></p>
<dd> Print the command line on the standard error output before executing it.</p>
<dt><code>-x, &#8211;exit</code></p>
<dd> Exit if the size (see the <code>-s</code> option) is exceeded.</p>
<dt><code>&#8211;help</code></p>
<dd> Print a summary of the options to <code>xargs</code> and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Print the version number of <code>xargs</code> and exit.</dl>
<p> The options <code>&#8211;max-lines</code> (<code>-L</code>, <code>-l</code>), <code>&#8211;replace</code> (<code>-I</code>, <code>-i</code>) and <code>&#8211;max-args</code> (<code>-n</code>) are mutually exclusive. If some of them are specified at the same time, then <code>xargs</code> will generally use the option specified last on the command line, i.e., it will reset the value of the offending option (given before) to its default value. Additionally, <code>xargs</code> will issue a warning diagnostic on <i>stderr</i>. The exception to this rule is that the special <i>max-args</i> value <i>1</i> (&#8216;<code>-n</code><i>1</i>&#8216;) is ignored after the <code>&#8211;replace</code> option and its aliases <code>-I</code> and <code>-i</code>, because it would not actually conflict. </p>
<h2>EXAMPLES</h2>
<pre>
<code>find /tmp -name core -type f -print | xargs /bin/rm -f</code>
</pre>
<p> Find files named <code>core</code> in or below the directory <code>/tmp</code> and delete them. Note that this will work incorrectly if there are any filenames containing newlines or spaces. </p>
<p> <code>find /tmp -name core -type f -print0 | xargs -0 /bin/rm -f</code> </p>
<p> Find files named <code>core</code> in or below the directory <code>/tmp</code> and delete them, processing filenames in such a way that file or directory names containing spaces or newlines are correctly handled. </p>
<p> <code>find /tmp -depth -name core -type f -delete</code> </p>
<p> Find files named <code>core</code> in or below the directory <code>/tmp</code> and delete them, but more efficiently than in the previous example (because we avoid the need to use <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and <code><a href="/docs/linux/man/2-exec/">exec</a></code>(2) to launch <code>rm</code> and we don&#8217;t need the extra <code>xargs</code> process). </p>
<pre>
<code>cut -d: -f1 &lt; /etc/passwd | sort | xargs echo</code>
</pre>
<p> Generates a compact listing of all the users on the system.</p>
<h2>EXIT STATUS</h2>
<p> <code>xargs</code> exits with the following status:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> if it succeeds</p>
<dt>123</p>
<dd> if any invocation of the command exited with status 1-125</p>
<dt>124</p>
<dd> if the command exited with status 255</p>
<dt>125</p>
<dd> if the command is killed by a signal</p>
<dt>126</p>
<dd> if the command cannot be run</p>
<dt>127</p>
<dd> if the command is not found</p>
<dt>1</p>
<dd> if some other error occurred.</dl>
</dl>
<p> Exit codes greater than 128 are used by the shell to indicate that a program died due to a fatal signal.</p>
<h2>STANDARDS CONFORMANCE</h2>
<p> As of GNU xargs version 4.2.9, the default behaviour of <code>xargs</code> is not to have a logical end-of-file marker. POSIX (IEEE Std 1003.1, 2004 Edition) allows this. </p>
<p> The -l and -i options appear in the 1997 version of the POSIX standard, but do not appear in the 2004 version of the standard. Therefore you should use -L and -I instead, respectively. </p>
<p> The -o option is an extension to the POSIX standard for better compatibility with BSD. </p>
<p> The POSIX standard allows implementations to have a limit on the size of arguments to the <code>exec</code> functions. This limit could be as low as 4096 bytes including the size of the environment. For scripts to be portable, they must not rely on a larger value. However, I know of no implementation whose actual limit is that small. The <code>&#8211;show-limits</code> option can be used to discover the actual limits in force on the current system.</p>
<h2>BUGS</h2>
<p> It is not possible for <code>xargs</code> to be used securely, since there will always be a time gap between the production of the list of input files and their use in the commands that <code>xargs</code> issues. If other users have access to the system, they can manipulate the filesystem during this time window to force the action of the commands <code>xargs</code> runs to apply to files that you didn&#8217;t intend. For a more detailed discussion of this and related problems, please refer to the &#8220;Security Considerations&#8221; chapter in the findutils Texinfo documentation. The <code>-execdir</code> option of <code>find</code> can often be used as a more secure alternative. </p>
<p> When you use the <code>-I</code> option, each line read from the input is buffered internally. This means that there is an upper limit on the length of input line that <code>xargs</code> will accept when used with the <code>-I</code> option. To work around this limitation, you can use the <code>-s</code> option to increase the amount of buffer space that <code>xargs</code> uses, and you can also use an extra invocation of <code>xargs</code> to ensure that very long lines do not occur. For example: </p>
<p> <code>somecommand | xargs -s 50000 echo | xargs -I &#8216;{}&#8217; -s 100000 rm &#8216;{}&#8217;</code> </p>
<p> Here, the first invocation of <code>xargs</code> has no input line length limit because it doesn&#8217;t use the <code>-i</code> option. The second invocation of <code>xargs</code> does have such a limit, but we have ensured that it never encounters a line which is longer than it can handle. This is not an ideal solution. Instead, the <code>-i</code> option should not impose a line length limit, which is why this discussion appears in the BUGS section. The problem doesn&#8217;t occur with the output of <code><a href="/docs/linux/man/1-find/">find</a></code>(1) because it emits just one filename per line.</p>
<h2>REPORTING BUGS</h2>
<p> GNU findutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/findutils/#get-help">https://www.gnu.org/software/findutils/#get-help</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt; </p>
<p> Report any other issue via the form at the GNU Savannah bug tracker:</p>
<dl>
<dt>
<dd> &lt;<a rel="nofollow" href="https://savannah.gnu.org/bugs/?group=findutils">https://savannah.gnu.org/bugs/?group=findutils</a>&gt;</dl>
<p> General topics about the GNU findutils package are discussed at the <i>bug-findutils</i> mailing list:</p>
<dl>
<dt>
<dd> &lt;<a rel="nofollow" href="https://lists.gnu.org/mailman/listinfo/bug-findutils">https://lists.gnu.org/mailman/listinfo/bug-findutils</a>&gt;</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1990-2021 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-find/">find</a></code>(1), <code><a href="/docs/linux/man/1-kill/">kill</a></code>(1), <code><a href="/docs/linux/man/1-locate/">locate</a></code>(1), <code><a href="/docs/linux/man/1-updatedb/">updatedb</a></code>(1), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/3-execvp/">execvp</a></code>(3), <code><a href="/docs/linux/man/5-locatedb/">locatedb</a></code>(5), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/findutils/xargs">https://www.gnu.org/software/findutils/xargs</a>&gt;<br />
 or available locally via: <code>info xargs</code> </p>
<h2>Index</h2>
