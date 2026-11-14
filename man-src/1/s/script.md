---
title: "script(1)"
name: "script"
section: "1"
letter: "s"
url: "/docs/linux/man/1-script/"
description: "script – make typescript of terminal session"
---

<h2 class="name">NAME</h2>
<p> script &#8211; make typescript of terminal session </p>
<h2>SYNOPSIS</h2>
<p> <code>script</code> [options] [<i>file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>script</code> makes a typescript of everything on your terminal session. The terminal data are stored in raw form to the log file and information about timing to another (optional) structured log file. The timing log file is necessary to replay the session later by <code><a href="/docs/linux/man/1-scriptreplay/">scriptreplay</a></code>(1) and to store additional information about the session. </p>
<p> Since version 2.35, <code>script</code> supports multiple streams and allows the logging of input and output to separate files or all the one file. This version also supports new timing file which records additional information. The command <code>scriptreplay &#8211;summary</code> then provides all the information. </p>
<p> If the argument <i>file</i> or option <code>&#8211;log-out</code> <i>file</i> is given, <code>script</code> saves the dialogue in this <i>file</i>. If no filename is given, the dialogue is saved in the file <i>typescript</i>. </p>
<p> Note that logging input using <code>&#8211;log-in</code> or <code>&#8211;log-io</code> may record security-sensitive information as the log file contains all terminal session input (e.g., passwords) independently of the terminal echo flag setting.</p>
<h2>OPTIONS</h2>
<p> Below, the <i>size</i> argument may be followed by the multiplicative suffixes KiB (=1024), MiB (=1024*1024), and so on for GiB, TiB, PiB, EiB, ZiB and YiB (the &quot;iB&quot; is optional, e.g., &quot;K&quot; has the same meaning as &quot;KiB&quot;), or the suffixes KB (=1000), MB (=1000*1000), and so on for GB, TB, PB, EB, ZB and YB. </p>
<p> <code>-a</code>, <code>&#8211;append</code></p>
<dl>
<dt>
<dd> Append the output to <i>file</i> or to <i>typescript</i>, retaining the prior contents.</dl>
<p> <code>-c</code>, <code>&#8211;command</code> <i>command</i></p>
<dl>
<dt>
<dd> Run the <i>command</i> rather than an interactive shell. This makes it easy for a script to capture the output of a program that behaves differently when its stdout is not a tty.</dl>
<p> <code>-E</code>, <code>&#8211;echo</code> <i>when</i></p>
<dl>
<dt>
<dd> This option controls the <code>ECHO</code> flag for the slave end of the session&#8217;s pseudoterminal. The supported modes are <i>always</i>, <i>never</i>, or <i>auto</i>. </p>
<p> The default is <i>auto</i> &#8212; in this case, <code>ECHO</code> enabled for the pseudoterminal slave; if the current standard input is a terminal, <code>ECHO</code> is disabled for it to prevent double echo; if the current standard input is not a terminal (for example pipe: <code>echo date | script</code>) then keeping <code>ECHO</code> enabled for the pseudoterminal slave enables the standard input data to be viewed on screen while being recorded to session log simultaneously. </p>
<p> Note that &#8216;never&#8217; mode affects content of the session output log, because users input is not repeated on output.</dl>
<p> <code>-e</code>, <code>&#8211;return</code></p>
<dl>
<dt>
<dd> Return the exit status of the child process. Uses the same format as bash termination on signal termination (i.e., exit status is 128 + the signal number). The exit status of the child process is always stored in the type script file too.</dl>
<p> <code>-f</code>, <code>&#8211;flush</code></p>
<dl>
<dt>
<dd> Flush output after each write. This is nice for telecooperation: one person does <code>mkfifo foo; script -f foo</code>, and another can supervise in real-time what is being done using <code>cat foo</code>. Note that flush has an impact on performance; it&#8217;s possible to use <code>SIGUSR1</code> to flush logs on demand.</dl>
<p> <code>&#8211;force</code></p>
<dl>
<dt>
<dd> Allow the default output file <i>typescript</i> to be a hard or symbolic link. The command will follow a symbolic link.</dl>
<p> <code>-B</code>, <code>&#8211;log-io</code> <i>file</i></p>
<dl>
<dt>
<dd> Log input and output to the same <i>file</i>. Note, this option makes sense only if <code>&#8211;log-timing</code> is also specified, otherwise it&#8217;s impossible to separate output and input streams from the log <i>file</i>.</dl>
<p> <code>-I</code>, <code>&#8211;log-in</code> <i>file</i></p>
<dl>
<dt>
<dd> Log input to the <i>file</i>. The log output is disabled if only <code>&#8211;log-in</code> specified. </p>
<p> Use this logging functionality carefully as it logs all input, including input when terminal has disabled echo flag (for example, password inputs).</dl>
<p> <code>-O</code>, <code>&#8211;log-out</code> <i>file</i></p>
<dl>
<dt>
<dd> Log output to the <i>file</i>. The default is to log output to the file with name <i>typescript</i> if the option <code>&#8211;log-out</code> or <code>&#8211;log-in</code> is not given. The log output is disabled if only <code>&#8211;log-in</code> specified.</dl>
<p> <code>-T</code>, <code>&#8211;log-timing</code> <i>file</i></p>
<dl>
<dt>
<dd> Log timing information to the <i>file</i>. Two timing file formats are supported now. The classic format is used when only one stream (input or output) logging is enabled. The multi-stream format is used on <code>&#8211;log-io</code> or when <code>&#8211;log-in</code> and <code>&#8211;log-out</code> are used together. See also <code>&#8211;logging-format</code>.</dl>
<p> <code>-m</code>, <code>&#8211;logging-format</code> <i>format</i></p>
<dl>
<dt>
<dd> Force use of <i>advanced</i> or <i>classic</i> format. The default is the classic format to log only output and the advanced format when input as well as output logging is requested. </p>
<p> <code>Classic format</code></p>
<dl>
<dt>
<dd> The log contains two fields, separated by a space. The first field indicates how much time elapsed since the previous output. The second field indicates how many characters were output this time.</dl>
<p> <code>Advanced (multi-stream) format</code></p>
<dl>
<dt>
<dd> The first field is an entry type identifier (&#8216;I&#8217;nput, &#8216;O&#8217;utput, &#8216;H&#8217;eader, &#8216;S&#8217;ignal). The socond field is how much time elapsed since the previous entry, and the rest of the entry is type-specific data.</dl>
</dl>
<p> <code>-o</code>, <code>&#8211;output-limit</code> <i>size</i></p>
<dl>
<dt>
<dd> Limit the size of the typescript and timing files to <i>size</i> and stop the child process after this size is exceeded. The calculated file size does not include the start and done messages that the <code>script</code> command prepends and appends to the child process output. Due to buffering, the resulting output file might be larger than the specified value.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Be quiet (do not write start and done messages to standard output).</dl>
<p> <code>-t</code>[<i>file</i>], <code>&#8211;timing</code>[=<i>file</i>]</p>
<dl>
<dt>
<dd> Output timing data to standard error, or to <i>file</i> when given. This option is deprecated in favour of <code>&#8211;log-timing</code> where the <i>file</i> argument is not optional.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>SIGNALS</h2>
<p> Upon receiving <code>SIGUSR1</code>, <code>script</code> immediately flushes the output files.</p>
<h2>ENVIRONMENT</h2>
<p> The following environment variable is utilized by <code>script</code>: </p>
<p> <code>SHELL</code></p>
<dl>
<dt>
<dd> If the variable <code>SHELL</code> exists, the shell forked by <code>script</code> will be that shell. If <code>SHELL</code> is not set, the Bourne shell is assumed. (Most shells set this variable automatically).</dl>
<h2>NOTES</h2>
<p> The script ends when the forked shell exits (a <i>control-D</i> for the Bourne shell (<code><a href="//www.systutorials.com/docs/linux/man/1p-sh/">sh</a></code>(1p)), and <i>exit</i>, <i>logout</i> or <i>control-d</i> (if <i>ignoreeof</i> is not set) for the C-shell, <code><a href="/docs/linux/man/1-csh/">csh</a></code>(1)). </p>
<p> Certain interactive commands, such as <code><a href="/docs/linux/man/1-vi/">vi</a></code>(1), create garbage in the typescript file. <code>script</code> works best with commands that do not manipulate the screen, the results are meant to emulate a hardcopy terminal. </p>
<p> It is not recommended to run <code>script</code> in non-interactive shells. The inner shell of <code>script</code> is always interactive, and this could lead to unexpected results. If you use <code>script</code> in the shell initialization file, you have to avoid entering an infinite loop. You can use for example the <code>.profile</code> file, which is read by login shells only: </p>
<dl>
<dt>
<dd>
<pre>
if test -t 0 ; then
    script
    exit
fi
</pre>
</dl>
<p> You should also avoid use of <code>script</code> in command pipes, as <code>script</code> can read more input than you would expect.</p>
<h2>HISTORY</h2>
<p> The <code>script</code> command appeared in 3.0BSD.</p>
<h2>BUGS</h2>
<p> <code>script</code> places <i>everything</i> in the log file, including linefeeds and backspaces. This is not what the naive user expects. </p>
<p> <code>script</code> is primarily designed for interactive terminal sessions. When stdin is not a terminal (for example: <code>echo foo | script</code>), then the session can hang, because the interactive shell within the script session misses EOF and <code>script</code> has no clue when to close the session. See the <code>NOTES</code> section for more information.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-csh/">csh</a></code>(1) (for the <i>history</i> mechanism), <code><a href="/docs/linux/man/1-scriptreplay/">scriptreplay</a></code>(1), <code><a href="/docs/linux/man/1-scriptlive/">scriptlive</a></code>(1)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>script</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
