---
title: "calc(1)"
name: "calc"
section: "1"
letter: "c"
url: "/docs/linux/man/1-calc/"
description: "calc – arbitrary precision calculator"
---

<h2>NAME</h2>
<p> calc &#8211; arbitrary precision calculator</p>
<h2>SYNOPSIS</h2>
<p> <i>calc</i> [<code>-c</code>] [<code>-C</code>] [<code>-d</code>]<br />
 [<code>-D calc_debug[:resource_debug[:user_debug]]</code>]<br />
 [<code>-e</code>] [<code>-h</code>] [<code>-i</code>] [<code>-m mode</code>] [<code>-O</code>]<br />
 [<code>-p</code>] [<code>-q</code>] [<code>-s</code>] [<code>-u</code>] [<code>-v</code>] [<code>[&#8211;]&nbsp;<wbr>calc_cmd &#8230;</code>] </p>
<p> <i>#!/usr/bin/calc</i>&nbsp;<wbr>[other_flags &#8230;] <code>-f</code></p>
<h2>DESCRIPTION</h2>
<p> CALC OPTIONS </p>
<dl>
<dt><code>-c</code></p>
<dd> Continue reading command lines even after a scan/parse error has caused the abandonment of a line. Note that this option only deals with scanning and parsing of the calc language. It does not deal with execution or run-time errors. </p>
<p> For example: </p>
<pre>
calc read many_errors.cal
</pre>
<p> will cause <code>calc</code> to abort on the first syntax error, whereas: </p>
<pre>
calc -c read many_errors.cal
</pre>
<p> will cause <code>calc</code> to try to process each line being read despite the scan/parse errors that it encounters. </p>
<p> By default, calc startup resource files are silently ignored if not found. This flag will report missing startup resource files unless <code>-d</code> is also given. </p>
<dt><code>-C</code></p>
<dd> Permit the execution of custom builtin functions. Without this flag, calling the custom() builtin function will simply generate an error. </p>
<p> Use of this flag may cause <code>calc</code> to execute functions that are non-standard and that are not portable. Custom builtin functions are disabled by default for this reason. </p>
<dt><code>-d</code></p>
<dd> Disable the printing of the opening title. The printing of resource file debug and informational messages is also disabled as if <code>config(&quot;resource_debug&quot;, 0)</code> had been executed. </p>
<p> For example: </p>
<p> calc &quot;read qtime; <a href="/docs/linux/man/2-qtime/">qtime</a>(2)&quot; </p>
<p> will output something like: </p>
<pre>
qtime(utc_hr_offset) defined
It's nearly ten past six.
</pre>
<p> whereas: </p>
<pre>
calc -d &quot;read qtime; <a href="//www.systutorials.com/docs/linux/man/2-qtime/">qtime</a>(2)&quot;
</pre>
<p> will just say: </p>
<pre>
It's nearly ten past six.
</pre>
<p> This flag disables the reporting of missing calc startup resource files. </p>
<dt><code>-D</code> calc_debug[:resource_debug[:user_debug]]</p>
<dd> Force the initial value of config(&quot;calc_debug&quot;), config(&quot;resource_debug&quot;) and config(&quot;user_debug&quot;). </p>
<p> The : separated strings are interpreted as signed 32 bit integers. After an optional leading sign a leading zero indicates octal conversion, and a leading &#8220;0x&#8221; or &#8220;0X&#8221; hexadecimal conversion. Otherwise, decimal conversion is assumed. </p>
<p> By default, <i>calc_debug</i> is 0, <i>resource_debug</i> is 3 and <i>user_debug</i> is 0. </p>
<p> For more information use the following <code>calc</code> command: </p>
<pre>
help config
</pre>
<dt><code>-e</code></p>
<dd> Ignore any environment variables on startup. The getenv() builtin will still return values, however. </p>
<dt><code>-f</code></p>
<dd> This flag is required when using calc in <code>shell script mode</code>. It must be at the end of the initial <code>#!</code> line of the script. </p>
<p> This flag is normally only at the end of a calc shell script. If the first line of an executable file begins <code>#!</code> followed by the absolute pathname of the <code>calc</code> program and the flag <code>-f</code> as in: </p>
<pre>
<i>#!/usr/bin/calc</i>&nbsp;<wbr>[other_flags ...] <code>-f</code>
</pre>
<p> the rest of the file will be processed in <code>shell script mode</code>. See <code>SHELL SCRIPT MODE</code> section of this man page below for details. </p>
<p> The actual form of this flag is: </p>
<p> <code>-f</code> filename </p>
<p> On systems that treat an executable that begins with <code>#!</code> as a script, the path of the executable is appended by the kernel as the final argument to the exec() system call. This is why the <code>-f</code> flag at the very end of the <code>#!</code> line. </p>
<p> It is possible use <code>-f filename</code> on the command line: </p>
<pre>
<i>calc</i>&nbsp;<wbr>[other_flags ...] <code>-f</code> filename
</pre>
<p> This will cause calc to process lines in <code>filename</code> in <code>shell script mode</code>. </p>
<p> Use of <code>-f</code> implies <code>-s</code>. In addition, <code>-d</code> and <code>-p</code> are implied if <code>-i</code> is not given. </p>
<dt><code>-h</code></p>
<dd> Print a help message. This option implies <code>-q</code>. This is equivalent to the <code>calc</code> command help help. The help facility is disabled unless the mode is 5 or 7. See <code>-m</code>. </p>
<dt><code>-i</code></p>
<dd> Become interactive if possible. This flag will cause <code>calc</code> to drop into interactive mode after the <i>calc_cmd</i> arguments on the command line are evaluated. Without this flag, <code>calc</code> will exit after they are evaluated. </p>
<p> For example: </p>
<pre>
calc 2+5
</pre>
<p> will print the value 7 and exit whereas: </p>
<pre>
calc -i 2+5
</pre>
<p> will print the value 7 and prompt the user for more <code>calc</code> commands. </p>
<dt><code>-m</code> mode</p>
<dd> This flag sets the permission mode of <code>calc</code>. It controls the ability for <code>calc</code> to open files and execute programs. <i>Mode</i> may be a number from 0 to 7. </p>
<p> The mode value is interpreted in a way similar to that of the <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1) octal mode: </p>
<pre><code>
0  do not open any file, do not execute progs
1  do not open any file
2  do not open files for reading, do not execute progs
3  do not open files for reading
4  do not open files for writing, do not execute progs
5  do not open files for writing
6  do not execute any program
7  allow everything (default mode)
</code></pre>
<p> If one wished to run <code>calc</code> from a privileged user, one might want to use <code>-m</code> 0 in an effort to make <code>calc</code> somewhat more secure. </p>
<p> Mode bits for reading and writing apply only on an open. Files already open are not effected. Thus if one wanted to use the <code>-m</code> 0 in an effort to make <code>calc</code> somewhat more secure, but still wanted to read and write a specific file, one might want to do in <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/1-ksh/">ksh</a></code>(1), <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1)-like shells: </p>
<pre>
calc -m 0 3&lt;a.file
</pre>
<p> Files presented to <code>calc</code> in this way are opened in an unknown mode. <code>Calc</code> will attempt to read or write them if directed. </p>
<p> If the mode disables opening of files for reading, then the startup resource files are disabled as if <code>-q</code> was given. The reading of key bindings is also disabled when the mode disables opening of files for reading. </p>
<dt><code>-O</code></p>
<dd> Use the old classic defaults instead of the default configuration. This flag as the same effect as executing <code>config(&quot;all&quot;, &quot;oldcfg&quot;)</code> at startup time. </p>
<p> NOTE: Older versions of calc used <code>-n</code> to setup a modified form of the default calc configuration. The <code>-n</code> flag currently does nothing. Use of the <code>-n</code> flag is now deprecated and may be used for something else in the future. </p>
<dt><code>-p</code></p>
<dd> Pipe processing is enabled by use of <code>-p</code>. For example: </p>
<pre>
calc -p &quot;2^21701-1&quot; | fizzbin
</pre>
<p> In pipe mode, <code>calc</code> does not prompt, does not print leading tabs and does not print the initial header. The <code>-p</code> flag overrides <code>-i</code>. </p>
<dt><code>-q</code></p>
<dd> Disable the reading of the startup scripts. </p>
<dt><code>-s</code></p>
<dd> By default, all <i>calc_cmd</i> args are evaluated and executed. This flag will disable their evaluation and instead make them available as strings for the argv() builtin function. </p>
<dt><code>-u</code></p>
<dd> Disable buffering of stdin and stdout. </p>
<dt><code>-v</code></p>
<dd> Print the <code>calc</code> version number and exit. </p>
<dt><code>&#8212;</code></p>
<dd> The double dash indicates to calc that no more option follow. Thus calc will ignore a later argument on the command line even if it starts with a dash. This is useful when entering negative values on the command line as in: </p>
<pre>
calc -p -- -1 - -7
</pre>
</dl>
<p> CALC COMMAND LINE </p>
<p> With no <i>calc_cmd</i> arguments, <code>calc</code> operates interactively. If one or more arguments are given on the command line and <code>-s</code> is NOT given, then <code>calc</code> will read and execute them and either attempt to go interactive according as the <code>-i</code> flag was present or absent. </p>
<p> If <code>-s</code> is given, <code>calc</code> will not evaluate any <i>calc_cmd</i> arguments but instead make them available as strings to the argv() builtin function. </p>
<p> Sufficiently simple commands with no no characters like parentheses, brackets, semicolons, &#8216;*&#8217;, which have special interpretations in UNIX shells may be entered, possibly with spaces, until the terminating newline. For example: </p>
<pre>
calc 23 + 47
</pre>
<p> will print 70. However, command lines will have problems: </p>
<pre>
calc 23 * 47
calc -23 + 47
</pre>
<p> The first example above fails because the shell interprets the &#8216;*&#8217; as a file glob. The second example fails because &#8216;-23&#8217; is viewed as a calc option (which it is not) and do calc objects to that it thinks of as an unknown option. These cases can usually be made to work as expected by enclosing the command between quotes: </p>
<pre>
calc '23 * 47'
calc &quot;print <a href="//www.systutorials.com/docs/linux/man/2-sqrt/">sqrt</a>(2), <a href="//www.systutorials.com/docs/linux/man/1-exp/">exp</a>(1)&quot;
</pre>
<p> or in parentheses and quotes to avoid leading -&#8216;s as in: </p>
<pre>
calc '(-23 + 47)'
</pre>
<p> One may also use a double dash to denote that calc options have ended as in: </p>
<pre>
calc -- -23 + 47
calc -q -- -23 + 47
</pre>
<p> If &#8216;!&#8217; is to be used to indicate the factorial function, for shells like <code><a href="/docs/linux/man/1-csh/">csh</a></code><i>(1)</i> for which &#8216;!&#8217; followed by a non-space character is used for history substitution, it may be necessary to include a space or use a backslash to escape the special meaning of &#8216;!&#8217;. For example, the command: </p>
<pre>
print 27!^2
</pre>
<p> may have to be replaced by: </p>
<pre>
print 27! ^2    or      print 27^2
</pre>
<p> CALC STARTUP FILES </p>
<p> Normally on startup, if the environment variable <code>$CALCRC</code> is undefined and <code>calc</code> is invoked without the <code>-q</code> flag, or if <code>$CALCRC</code> is defined and calc is invoked with <code>-e</code>, <code>calc</code> looks for a file &quot;startup&quot; in the calc resource directory <code>.calcrc</code> in the user&#8217;s home directory, and <code>.calcinit in the current directory.</code> If one or more of these are found, they are read in succession as <code>calc</code> scripts and their commands executed. When defined, <code>$CALCRC</code> is to contain a &#8216;:&#8217; separated list of names of files, and if calc is then invoked without either the <code>-q</code> or <code>-e</code> flags, these files are read in succession and their commands executed. No error condition is produced if a listed file is not found. </p>
<p> If the mode specified by <code>-m</code> disables opening of files for reading, then the reading of startup files is also disabled as if <code>-q</code> was given. </p>
<p> CALC FILE SEARCH PATH </p>
<p> If the environment variable <code>$CALCPATH</code> is undefined, or if it is defined and <code>calc</code> is invoked with the <code>-e</code> flag, when a file name not beginning with <code>/</code>, <code>~</code> or <code>./</code>, is specified as in: </p>
<pre>
calc read myfile
</pre>
<p> <code>calc</code> searches in succession: </p>
<pre>
/usr/lib64/myfile
/usr/lib64/myfile.cal
/usr/share/calc/custom/myfile
/usr/share/calc/custom/myfile.cal
</pre>
<p> If the file is found, the search stops and the commands in the file are executed. It is an error if no readable file with the specified name is found. An alternative search path can be specified by defining <code>$CALCPATH</code> in the same way as PATH is defined, as a &#8216;:&#8217; separated list of directories, and then invoking <code>calc</code> without the <code>-e</code> flag. </p>
<p> <code>Calc</code> treats all open files, other than stdin, stdout and stderr as files available for reading and writing. One may present <code>calc</code> with an already open file using <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/1-ksh/">ksh</a></code>(1), <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1)-like shells is to: </p>
<p> calc 3&lt;open_file 4&lt;open_file2 </p>
<p> For more information use the following <code>calc</code> commands: </p>
<pre>
help help
help overview
help usage
help environment
help config
</pre>
<p> SHELL SCRIPT MODE </p>
<p> If the first line of an executable file begins <code>#!</code> followed by the absolute pathname of the <code>calc</code> program and the flag <code>-f</code> as in: </p>
<pre>
<i>#!/usr/bin/calc</i>&nbsp;<wbr>[other_flags ...] <code>-f</code>
</pre>
<p> the rest of the file will be processed in <code>shell script mode</code>. Note that <code>-f</code> must at the end of the initial &#8220;#!&#8221; line. Any other optional <code>other_flags</code> must come before the <code>-f</code>. </p>
<p> In <code>shell script mode</code> the contents of the file are read and executed as if they were in a file being processed by a read command, except that a &quot;command&quot; beginning with &#8216;#&#8217; followed by whitespace and ending at the next newline is treated as a comment. Any optional <code>other_flags</code> will be parsed first followed by the later lines within the script itself. </p>
<p> In <code>shell script mode</code>, <code>-s</code> is always assumed. In addition, <code>-d</code> and <code>-p</code> are automatically set if <code>-i</code> is not given. </p>
<p> For example, if the file <code>/tmp/mersenne</code>: </p>
<pre><code>
#!/ usr / bin / calc &amp; nbsp; - q - f
#
#mersenne - an example of a calc shell script file
/* parse args */
if (argv() != 1) {
    fprintf(files(2), "usage: %s exp
", config("program"));
    abort "must give one exponent arg";
}
/* print the mersenne number */
print "2^" : argv(0)
    : "-1 =", 2 ^ eval(argv(0)) - 1;
</code></pre>
<p> is made an executable file by: </p>
<pre>
chmod +x /tmp/mersenne
</pre>
<p> then the command line: </p>
<pre>
/tmp/mersenne 127
</pre>
<p> will print: </p>
<pre>
2^127-1 = 170141183460469231731687303715884105727
</pre>
<p> Note that because <code>-s</code> is assumed in <code>shell script mode</code> and non-dashed args are made available as strings via the <code>argv</code>() builtin function. Therefore: </p>
<pre>
2^eval(argv(0))-1
</pre>
<p> will print the decimal value of 2^n-1 but </p>
<pre>
2^argv(0)-1
</pre>
<p> will not. </p>
<p> DATA TYPES </p>
<p> Fundamental builtin data types include integers, real numbers, rational numbers, complex numbers and strings. </p>
<p> By use of an object, one may define an arbitrarily complex data types. One may define how such objects behave a wide range of operations such as addition, subtraction, multiplication, division, negation, squaring, modulus, rounding, exponentiation, equality, comparison, printing and so on. </p>
<p> For more information use the following <code>calc</code> commands: </p>
<p> help types<br />
 help obj<br />
 show objfuncs </p>
<p> VARIABLES </p>
<p> Variables in <i>calc</i> are typeless. In other words, the fundamental type of a variable is determined by its content. Before a variable is assigned a value it has the value of zero. </p>
<p> The scope of a variable may be global, local to a file, or local to a procedure. Values may be grouped together in a matrix, or into a a list that permits stack and queue style operations. </p>
<p> For more information use the following <code>calc</code> commands: </p>
<p> help variable<br />
 help mat<br />
 help list<br />
 show globals </p>
<p> INPUT/OUTPUT </p>
<p> A leading &#8220;0x&#8221; implies a hexadecimal value, a leading &#8220;0b&#8221; implies a binary value, and a &#8220;0&#8221; followed by a digit implies an octal value. Complex numbers are indicated by a trailing &#8220;i&#8221; such as in &#8220;3+4i&#8221;. Strings may be delimited by either a pair of single or double quotes. By default, <i>calc</i> prints values as if they were floating point numbers. One may change the default to print values in a number of modes including fractions, integers and exponentials. </p>
<p> A number of stdio-like file I/O operations are provided. One may open, read, write, seek and close files. Filenames are subject to &#8220;~&#8221; expansion to home directories in a way similar to that of the Korn or C-Shell. </p>
<p> For example: </p>
<p> ~/.calcrc<br />
 ~chongo/lib/fft_multiply.cal </p>
<p> For more information use the following <code>calc</code> command: </p>
<p> help file </p>
<p> CALC LANGUAGE </p>
<p> The <i>calc</i> language is a C-like language. The language includes commands such as variable declarations, expressions, tests, labels, loops, file operations, function calls. These commands are very similar to their counterparts in C. </p>
<p> The language also include a number of commands particular to <i>calc</i> itself. These include commands such as function definition, help, reading in resource files, dump files to a file, error notification, configuration control and status. </p>
<p> For more information use the following <code>calc</code> command: </p>
<p> help command<br />
 help statement<br />
 help expression<br />
 help operator<br />
 help config </p>
<h2>FILES</h2>
<dl>
<dt>/usr/bin/calc</p>
<dd> calc binary </p>
<dt>/usr/share/calc/cscript/*</p>
<dd> calc shell scripts </p>
<dt>/usr/lib64/*.cal</p>
<dd> calc standard resource files </p>
<dt>/usr/lib64/help/*</p>
<dd> help files </p>
<dt>/usr/lib64/bindings</p>
<dd> non-GNU-readline command line editor bindings </p>
<dt>/usr/include/calc/*.h</p>
<dd> include files for C interface use </p>
<dt>/usr/lib64/libcalc.a</p>
<dd> calc binary link library </p>
<dt>/usr/lib64/libcustcalc.a</p>
<dd> custom binary link library </p>
<dt>/usr/share/calc/custom/*.cal</p>
<dd> custom resource files </p>
<dt>/usr/share/calc/custhelp/*</p>
<dd> custom help files </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>CALCPATH</p>
<dd> A :-separated list of directories used to search for calc resource filenames that do not begin with /, ./ or ~. </p>
<p> Default value: .:./cal:~/.cal:/usr/share/calc </p>
<dt>CALCRC</p>
<dd> On startup (unless -h or -q was given on the command line), <code>calc</code> searches for files along this :-separated environment variable. </p>
<p> Default value: /usr/share/calc/startup:~/.calcrc:./.calcinit </p>
<dt>CALCBINDINGS</p>
<dd> On startup (unless <i>-h</i> or <i>-q</i> was given on the command line, or <i>-m</i> disallows opening files for reading), <code>calc</code> reads key bindings from the filename specified by this environment variable. The key binding file is searched for along the $CALCPATH list of directories. </p>
<p> Default value: binding </p>
<p> This variable is not used if calc was compiled with GNU-readline support. In that case, the standard readline mechanisms (see <a href="/docs/linux/man/3-readline/">readline</a>(3)) are used. </p>
</dl>
<h2>CREDIT</h2>
<p> The main chunk of <code>calc</code> was written by David I. Bell. </p>
<p> The <code>calc</code> primary mirror, calc mailing list and calc bug report processing is performed by Landon Curt Noll. </p>
<p> Landon Curt Noll maintains the master reference source, performs release control functions as well as other calc maintenance functions. </p>
<p> Thanks for suggestions and encouragement from Peter Miller, Neil Justusson, and Landon Noll. </p>
<p> Thanks to Stephen Rothwell for writing the original version of hist.c which is used to do the command line editing. </p>
<p> Thanks to Ernest W. Bowen for supplying many improvements in accuracy and generality for some numeric functions. Much of this was in terms of actual code which I gratefully accepted. Ernest also supplied the original text for many of the help files. </p>
<p> Portions of this program are derived from an earlier set of public domain arbitrarily precision routines which was posted to the net around 1984. By now, there is almost no recognizable code left from that original source. </p>
<h2>COPYING / CALC GNU LESSER GENERAL PUBLIC LICENSE</h2>
<p> Calc is open software, and is covered under version 2 of the GNU General Public License. You are welcome to change it and/or distribute copies of it under certain conditions. The calc commands: </p>
<pre>
help copyright
help copying
help copying-gpl
</pre>
<p> should display the contents of the COPYING and COPYING-GPL files. Those files contain information about the calc&#8217;s GNU General Public License, and in particular the conditions under which you are allowed to change it and/or distribute copies of it. </p>
<p> You should have received a copy of the version 2 of the GNU General Public License. If you do not have these files, write to: </p>
<pre>
Free Software Foundation, Inc.
51 Franklin Street
Fifth Floor
Boston, MA  02110-1301
USA
</pre>
<p> Calc is copyrighted in several different ways. These ways include: </p>
<pre>
Copyright (C) year  David I. Bell
Copyright (C) year  David I. Bell and Landon Curt Noll
Copyright (C) year  David I. Bell and Ernest Bowen
Copyright (C) year  David I. Bell, Landon Curt Noll and Ernest Bowen
Copyright (C) year  Landon Curt Noll
Copyright (C) year  Ernest Bowen and Landon Curt Noll
Copyright (C) year  Ernest Bowen
</pre>
<p> This man page is: </p>
<pre>
Copyright (C) 1999  Landon Curt Noll
</pre>
<p> and is covered under version 2 GNU General Public License. </p>
<h2>CALC MAILING LIST / CALC UPDATES / ENHANCEMENTS</h2>
<p> To contribute comments, suggestions, enhancements and interesting <code>calc</code> resource files, and shell scripts please join the calc-tester low volume moderated calc mailing list. </p>
<p> To the calc-tester mailing list, visit the following URL: </p>
<pre>
<a rel="nofollow" href="https://www.listbox.com/subscribe/?list_id=239342">https://www.listbox.com/subscribe/?list_id=239342</a>
</pre>
<p> To help determine you are a human and not just a spam bot, you will be required to provide the following additional information: </p>
<pre>
Your Name
Calc Version
   For example, the current version is: 2.12.5.0
Operating System
   If you don't know your operating system, enter: unknown
The date 7 days ago
   Consult a calendar :-)
</pre>
<p> If you need a human to help you with your mailing list subscription, or if you have problems with the above procedure, please send EMail to our special address: </p>
<pre>
calc-tester-maillist-help at asthe dot com
NOTE: Remove spaces and replace 'at' with @, 'dot' with .
NOTE: Yes, the EMail address uses 'asthe',
      while the web site uses 'isthe'.
</pre>
<p> To be sure we see your EMail asking for help with your mailing list subscription, please use the following phase in your EMail Subject line your subject must contain the words: </p>
<pre>
calc tester mailing list help
</pre>
<p> You may have additional words in your subject line. </p>
<h2>BUG REPORTS / BUG FIXES</h2>
<p> Send bug reports and bug fixes to: </p>
<pre>
calc-bug-report at asthe dot com
NOTE: Remove spaces and replace 'at' with @, 'dot' with .
NOTE: Yes, the EMail address uses 'asthe',
      while the web site uses 'isthe'.
</pre>
<p> Your subject must contain the words: </p>
<pre>
calc bug report
</pre>
<p> You may have additional words in your subject line. However, you may find it more helpful to simply subscribe to the calc-tester mailing list (see above) and then to send your report to that mailing list as a wider set calc testers may be able to help you. </p>
<p> See the <i>BUGS</i> source file or use the <i>calc</i> command: </p>
<pre>
help bugs
</pre>
<p> for more information about bug reporting. </p>
<h2>CALC WEB SITE</h2>
<p> Landon Noll maintains the <code>calc</code> web site is located at: </p>
<p> <a rel="nofollow" href="http://www.isthe.com">www.isthe.com</a>/chongo/tech/comp/calc/ </p>
<p> Share and Enjoy! :-) </p>
<h2>Index</h2>
