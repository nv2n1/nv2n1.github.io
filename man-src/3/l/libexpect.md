---
title: "libexpect(3)"
name: "libexpect"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libexpect/"
description: "libexpect – programmed dialogue library with interactive programs"
---

<h2>NAME</h2>
<p> libexpect &#8211; programmed dialogue library with interactive programs</p>
<h2>DESCRIPTION</h2>
<p> This library contains functions that allow Expect to be used as a Tcl extension or to be used directly from C or C++ (without Tcl). Adding Expect as a Tcl extension is very short and simple, so that will be covered first.</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include expect_tcl.h
Expect_Init(interp);
cc files... - lexpect5 .20 - ltcl7 .5 - lm
</code></pre>
<p> Note: library versions may differ in the actual release. </p>
<p> The Expect_Init function adds expect commands to the named interpreter. It avoids overwriting commands that already exist, however aliases beginning with &quot;exp_&quot; are always created for expect commands. So for example, &quot;send&quot; can be used as &quot;exp_send&quot;. </p>
<p> Generally, you should only call Expect commands via Tcl_Eval. Certain auxiliary functions may be called directly. They are summarized below. They may be useful in constructing your own main. Look at the file exp_main_exp.c in the Expect distribution as a prototype main. Another prototype is tclAppInit.c in the Tcl source distribution. A prototype for working with Tk is in exp_main_tk.c in the Expect distribution.<br />
int exp_cmdlinecmds;<br />
int exp_interactive;<br />
FILE *exp_cmdfile;<br />
char *exp_cmdfilename;<br />
int exp_tcl_debugger_available;<br />
void exp_parse_argv(Tcl_Interp *, int argc, char **argv);<br />
int exp_interpreter(Tcl_Interp *);<br />
void exp_interpret_cmdfile(Tcl_Interp *, FILE *);<br />
void exp_interpret_cmdfilename(Tcl_Interp *, char *);<br />
void exp_interpret_rcfiles(Tcl_Interp *, int my_rc, int sys_rc);<br />
char *exp_cook(char *s, int *len);<br />
void    (*exp_app_exit)EXP_PROTO((Tcl_Interp *);<br />
void    exp_exit(Tcl_Interp *,int status);<br />
void    exp_exit_handlers(Tcl_Interp *);<br />
void    exp_error(Tcl_Interp,char *,&#8230;);<br />
 <code>exp_cmdlinecmds</code> is 1 if Expect has been invoked with commands on the program command-line (using &quot;-c&quot; for example). <code>exp_interactive</code> is 1 if Expect has been invoked with the -i flag or if no commands or script is being invoked. <code>exp_cmdfile</code> is a stream from which Expect will read commands. <code>exp_cmdfilename</code> is the name of a file which Expect will open and read commands from. <code>exp_tcl_debugger_available</code> is 1 if the debugger has been armed. </p>
<p> <code>exp_parse_argv</code> reads the representation of the command line. Based on what is found, any of the other variables listed here are initialized appropriately. <code>exp_interpreter</code> interactively prompts the user for commands and evaluates them. <code>exp_interpret_cmdfile</code> reads the given stream and evaluates any commands found. <code>exp_interpret_cmdfilename</code> opens the named file and evaluates any commands found. <code>exp_interpret_rcfiles</code> reads and evalutes the .rc files. If my_rc is zero, then ~/.expectrc is skipped. If sys_rc is zero, then the system-wide expectrc file is skipped. <code>exp_cook</code> returns a static buffer containing the argument reproduced with newlines replaced by carriage-return linefeed sequences. The primary purpose of this is to allow messages to be produced without worrying about whether the terminal is in raw mode or cooked mode. If length is zero, it is computed via strlen. <code>exp_error is a printf-like function that writes the result</code> to interp-&gt;result.</p>
<h2>SYNOPSIS</h2>
<p>#include &lt;expect.h&gt;<br />
int exp_spawnl(file, arg0[, arg1, &#8230;, argn](char *) 0);<br />
char *file;<br />
char *arg0, *arg1, &#8230; *argn;<br />
int<br />
    exp_spawnv(file, argv);<br />
char *file, *argv[];<br />
int<br />
    exp_spawnfd(fd);<br />
int fd;<br />
FILE *<br />
    exp_popen(command);<br />
char *command;<br />
extern int exp_pid;<br />
extern int exp_ttyinit;<br />
extern int exp_ttycopy;<br />
extern int exp_console;<br />
extern char *exp_stty_init;<br />
extern void (*exp_close_in_child)();<br />
extern void (*exp_child_exec_prelude)();<br />
extern void exp_close_tcl_files();<br />
cc files&#8230; &#8211; lexpect &#8211; ltcl &#8211; lm</p>
<h2>DESCRIPTION</h2>
<p> <code>exp_spawnl</code> and <code>exp_spawnv</code> fork a new process so that its stdin, stdout, and stderr can be written and read by the current process. <i>file</i> is the name of a file to be executed. The <i>arg</i> pointers are null-terminated strings. Following the style of execve(), <i>arg0</i> (or <i>argv[0]</i>) is customarily a duplicate of the name of the file. </p>
<p> Four interfaces are available, <code>exp_spawnl</code> is useful when the number of arguments is known at compile time. <code>exp_spawnv</code> is useful when the number of arguments is not known at compile time. <code>exp_spawnfd</code> is useful when an open file descriptor is already available as a source. <code>exp_popen</code> is explained later on. </p>
<p> If the process is successfully created, a file descriptor is returned which corresponds to the process&#8217;s stdin, stdout and stderr. A stream may be associated with the file descriptor by using fdopen(). (This should almost certainly be followed by setbuf() to unbuffer the I/O.) </p>
<p> Closing the file descriptor will typically be detected by the process as an EOF. Once such a process exits, it should be waited upon (via wait) in order to free up the kernel process slot. (Some systems allow you to avoid this if you ignore the SIGCHLD signal). </p>
<p> <code>exp_popen</code> is yet another interface, styled after popen(). It takes a Bourne shell command line, and returns a stream that corresponds to the process&#8217;s stdin, stdout and stderr. The actual implementation of <code>exp_popen</code> below demonstrates <code>exp_spawnl</code>.<br />
FILE *<br />
exp_popen(program)<br />
char *program;<br />
{<br />
    FILE *fp;<br />
    int ec;<br />
    if (0 &gt; (ec = exp_spawnl(&#8220;sh&#8221;, &#8220;sh&#8221;, &#8220;-c&#8221;, program, (char *)0)))<br />
        return (0);<br />
        if (NULL == (fp = fdopen(ec,&#8221;r+&#8221;)) return(0);<br />
        setbuf(fp,(char *)0);<br />
        return(fp);<br />
}</p>
<p> After a process is started, the variable <code>exp_pid</code> is set to the process-id of the new process. The variable <code>exp_pty_slave_name</code> is set to the name of the slave side of the pty. </p>
<p> The spawn functions uses a pty to communicate with the process. By default, the pty is initialized the same way as the user&#8217;s tty (if possible, i.e., if the environment has a controlling terminal.) This initialization can be skipped by setting exp_ttycopy to 0. </p>
<p> The pty is further initialized to some system wide defaults if exp_ttyinit is non-zero. The default is generally comparable to &quot;stty sane&quot;. </p>
<p> The tty setting can be further modified by setting the variable <code>exp_stty_init</code>. This variable is interpreted in the style of stty arguments. For example, exp_stty_init = &quot;sane&quot;; repeats the default initialization. </p>
<p> On some systems, it is possible to redirect console output to ptys. If this is supported, you can force the next spawn to obtain the console output by setting the variable <code>exp_console</code> to 1. </p>
<p> Between the time a process is started and the new program is given control, the spawn functions can clean up the environment by closing file descriptors. By default, the only file descriptors closed are ones internal to Expect and any marked &quot;close-on-exec&quot;. </p>
<p> If needed, you can close additional file descriptors by creating an appropriate function and assigning it to exp_close_in_child. The function will be called after the fork and before the exec. (This also modifies the behavior of the spawn command in Expect.) </p>
<p> If you are also using Tcl, it may be convenient to use the function exp_close_tcl_files which closes all files between the default standard file descriptors and the highest descriptor known to Tcl. (Expect does this.) </p>
<p> The function exp_child_exec_prelude is the last function called prior to the actual exec in the child. You can redefine this for effects such as manipulating the uid or the signals. </p>
<h2>IF YOU WANT TO ALLOCATE YOUR OWN PTY</h2>
<p>extern int exp_autoallocpty;<br />
extern int exp_pty[2];</p>
<p> The spawn functions use a pty to communicate with the process. By default, a pty is automatically allocated each time a process is spawned. If you want to allocate ptys yourself, before calling one of the spawn functions, set <code>exp_autoallocpty</code> to 0, <code>exp_pty[0]</code> to the master pty file descriptor and <code>exp_pty[1]</code> to the slave pty file descriptor. The expect library will not do any pty initializations (e.g., exp_stty_init will not be used). The slave pty file descriptor will be automatically closed when the process is spawned. After the process is started, all further communication takes place with the master pty file descriptor. </p>
<p> <code>exp_spawnl</code> and <code>exp_spawnv</code> duplicate the shell&#8217;s actions in searching for an executable file in a list of directories. The directory list is obtained from the environment.</p>
<h2>EXPECT PROCESSING</h2>
<p> While it is possible to use read() to read information from a process spawned by <code>exp_spawnl</code> or <code>exp_spawnv</code>, more convenient functions are provided. They are as follows:<br />
int<br />
    exp_expectl(fd, type1, pattern1, [<br />
        re1,<br />
    ],<br />
                value1, type2, &#8230;, exp_end);<br />
int fd;<br />
enum exp_type type;<br />
char *pattern1, *pattern2, &#8230;;<br />
regexp *re1, *re2, &#8230;;<br />
int value1, value2, &#8230;;<br />
int<br />
    exp_fexpectl(fp, type1, pattern1, [<br />
        re1,<br />
    ] value1,<br />
                 type2, &#8230;, exp_end);<br />
FILE *fp;<br />
enum exp_type type;<br />
char *pattern1, *pattern2, &#8230;;<br />
regexp *re1, *re2, &#8230;;<br />
int value1, value2, &#8230;;<br />
enum exp_type {<br />
};<br />
struct exp_case {<br />
};<br />
int<br />
    exp_expectv(fd, cases);<br />
int fd;<br />
struct exp_case *cases;<br />
int<br />
    exp_fexpectv(fp, cases);<br />
FILE *fp;<br />
struct exp_case *cases;<br />
extern int exp_timeout;<br />
extern char *exp_match;<br />
extern char *exp_match_end;<br />
extern char *exp_buffer;<br />
extern char *exp_buffer_end;<br />
extern int exp_match_max;<br />
extern int exp_full_buffer;<br />
extern int exp_remove_nulls;</p>
<p> The functions wait until the output from a process matches one of the patterns, a specified time period has passed, or an EOF is seen. </p>
<p> The first argument to each function is either a file descriptor or a stream. Successive sets of arguments describe patterns and associated integer values to return when the pattern matches. </p>
<p> The type argument is one of four values. exp_end indicates that no more patterns appear. exp_glob indicates that the pattern is a glob-style string pattern. exp_exact indicates that the pattern is an exact string. exp_regexp indicates that the pattern is a regexp-style string pattern. exp_compiled indicates that the pattern is a regexp-style string pattern, and that its compiled form is also provided. exp_null indicates that the pattern is a null (for debugging purposes, a string pattern must also follow). </p>
<p> If the compiled form is not provided with the functions <code>exp_expectl</code> and <code>exp_fexpectl</code>, any pattern compilation done internally is thrown away after the function returns. The functions <code>exp_expectv</code> and <code>exp_fexpectv</code> will automatically compile patterns and will not throw them away. Instead, they must be discarded by the user, by calling free on each pattern. It is only necessary to discard them, the last time the cases are used. </p>
<p> Regexp subpatterns matched are stored in the compiled regexp. Assuming &quot;re&quot; contains a compiled regexp, the matched string can be found in re-&gt;startp[0]. The match substrings (according to the parentheses) in the original pattern can be found in re-&gt;startp[1], re-&gt;startp[2], and so on, up to re-&gt;startp[9]. The corresponding strings ends are re-&gt;endp[x] where x is that same index as for the string start. </p>
<p> The type exp_null matches if a null appears in the input. The variable exp_remove_nulls must be set to 0 to prevent nulls from being automatically stripped. By default, exp_remove_nulls is set to 1 and nulls are automatically stripped. </p>
<p> <code>exp_expectv</code> and <code>exp_fexpectv</code> are useful when the number of patterns is not known in advance. In this case, the sets are provided in an array. The end of the array is denoted by a struct exp_case with type exp_end. For the rest of this discussion, these functions will be referred to generically as <i>expect.</i> </p>
<p> If a pattern matches, then the corresponding integer value is returned. Values need not be unique, however they should be positive to avoid being mistaken for EXP_EOF, EXP_TIMEOUT, or EXP_FULLBUFFER. Upon EOF or timeout, the value <code>EXP_EOF</code> or <code>EXP_TIMEOUT</code> is returned. The default timeout period is 10 seconds but may be changed by setting the variable <code>exp_timeout</code>. A value of -1 disables a timeout from occurring. A value of 0 causes the expect function to return immediately (i.e., poll) after one read(). However it must be preceded by a function such as select, poll, or an event manager callback to guarantee that there is data to be read. </p>
<p> If the variable exp_full_buffer is 1, then EXP_FULLBUFFER is returned if exp_buffer fills with no pattern having matched. </p>
<p> When the expect function returns, <code>exp_buffer</code> points to the buffer of characters that was being considered for matching. <code>exp_buffer_end</code> points to one past the last character in exp_buffer. If a match occurred, <code>exp_match</code> points into <code>exp_buffer</code> where the match began. <code>exp_match_end</code> points to one character past where the match ended. </p>
<p> Each time new input arrives, it is compared to each pattern in the order they are listed. Thus, you may test for absence of a match by making the last pattern something guaranteed to appear, such as a prompt. In situations where there is no prompt, you must check for <code>EXP_TIMEOUT</code> (just like you would if you were interacting manually). More philosophy and strategies on specifying <code>expect</code> patterns can be found in the documentation on the <code>expect</code> program itself. See SEE ALSO below. </p>
<p> Patterns are the usual C-shell-style regular expressions. For example, the following fragment looks for a successful login, such as from a telnet dialogue.<br />
switch (exp_expectl(<br />
    exp_glob, &#8220;connected&#8221;, CONN,<br />
    exp_glob, &#8220;busy&#8221;, BUSY,<br />
    exp_glob, &#8220;failed&#8221;, ABORT,<br />
    exp_glob, &#8220;invalid password&#8221;, ABORT,<br />
    exp_end)) {<br />
case CONN: /* logged in successfully */<br />
    break;<br />
case BUSY: /* couldn&#8217;t log in at the moment */<br />
    break;<br />
case EXP_TIMEOUT:<br />
case ABORT: /* can&#8217;t log in at any moment! */<br />
    break;<br />
default: /* problem with expect */<br />
}</p>
<p> Asterisks (as in the example above) are a useful shorthand for omitting line-termination characters and other detail. Patterns must match the entire output of the current process (since the previous read on the descriptor or stream). More than 2000 bytes of output can force earlier bytes to be &quot;forgotten&quot;. This may be changed by setting the variable <code>exp_match_max</code>. Note that excessively large values can slow down the pattern matcher.</p>
<h2>RUNNING IN THE BACKGROUND</h2>
<p>extern int exp_disconnected;<br />
int exp_disconnect();<br />
 It is possible to move a process into the background after it has begun running. A typical use for this is to read passwords and then go into the background to sleep before using the passwords to do real work. </p>
<p> To move a process into the background, fork, call exp_disconnect() in the child process and exit() in the parent process. This disassociates your process from the controlling terminal. If you wish to move a process into the background in a different way, you must set the variable exp_disconnected to 1. This allows processes spawned after this point to be started correctly.</p>
<h2>MULTIPLEXING</h2>
<p> By default, the expect functions block inside of a read on a single file descriptor. If you want to wait on patterns from multiple file descriptors, use select, poll, or an event manager. They will tell you what file descriptor is ready to read. </p>
<p> When a file descriptor is ready to read, you can use the expect functions to do one and only read by setting timeout to 0.</p>
<h2>SLAVE CONTROL</h2>
<p>void<br />
    exp_slave_control(fd, enable) int fd;<br />
int enable;</p>
<p> Pty trapping is normally done automatically by the expect functions. However, if you want to issue an ioctl, for example, directly on the slave device, you should temporary disable trapping. </p>
<p> Pty trapping can be controlled with exp_slave_control. The first argument is the file descriptor corresponding to the spawned process. The second argument is a 0 if trapping is to be disabled and 1 if it is to be enabled. </p>
<h2>ERRORS</h2>
<p> All functions indicate errors by returning -1 and setting errno. </p>
<p> Errors that occur after the spawn functions fork (e.g., attempting to spawn a non-existent program) are written to the process&#8217;s stderr, and will be read by the first <code>expect</code>.</p>
<h2>SIGNALS</h2>
<pre>
<code>extern int exp_reading;</code>
<code>extern jmp_buf exp_readenv;</code>
</pre>
<p> <code>expect</code> uses alarm() to timeout, thus if you generate alarms during <code>expect</code>, it will timeout prematurely. </p>
<p> Internally, <code>expect</code> calls read() which can be interrupted by signals. If you define signal handlers, you can choose to restart or abort <code>expect</code>&#8216;s internal read. The variable, <code>exp_reading</code>, is true if (and only if) <code>expect</code>&#8216;s read has been interrupted. longjmp(exp_readenv,EXP_ABORT) will abort the read. longjmp(exp_readenv,EXP_RESTART) will restart the read.</p>
<h2>LOGGING</h2>
<pre><code>
extern int exp_loguser;
extern int exp_logfile_all extern FILE *exp_logfile;
</code></pre>
<p> If <code>exp_loguser</code> is nonzero, <code>expect</code> sends any output from the spawned process to stdout. Since interactive programs typically echo their input, this usually suffices to show both sides of the conversation. If <code>exp_logfile</code> is also nonzero, this same output is written to the stream defined by <code>exp_logfile</code>. If <code>exp_logfile_all</code> is non-zero, <code>exp_logfile</code> is written regardless of the value of <code>exp_loguser</code>. </p>
<h2>DEBUGGING</h2>
<p> While I consider the library to be easy to use, I think that the standalone expect program is much, much, easier to use than working with the C compiler and its usual edit, compile, debug cycle. Unlike typical C programs, most of the debugging isn&#8217;t getting the C compiler to accept your programs &#8211; rather, it is getting the dialogue correct. Also, translating scripts from expect to C is usually not necessary. For example, the speed of interactive dialogues is virtually never an issue. So please try the standalone &#8216;expect&#8217; program first. I suspect it is a more appropriate solution for most people than the library. </p>
<p> Nonetheless, if you feel compelled to debug in C, here are some tools to help you. </p>
<pre>
<code>extern int exp_is_debugging;</code>
<code>extern FILE *exp_debugfile;</code>
</pre>
<p> While expect dialogues seem very intuitive, trying to codify them in a program can reveal many surprises in a program&#8217;s interface. Therefore a variety of debugging aids are available. They are controlled by the above variables, all 0 by default. </p>
<p> Debugging information internal to <code>expect</code> is sent to stderr when <code>exp_is_debugging</code> is non-zero. The debugging information includes every character received, and every attempt made to match the current input against the patterns. In addition, non-printable characters are translated to a printable form. For example, a control-C appears as a caret followed by a C. If <code>exp_logfile</code> is non-zero, this information is also written to that stream. </p>
<p> If <code>exp_debugfile</code> is non-zero, all normal and debugging information is written to that stream, regardless of the value of <code>exp_is_debugging</code>.</p>
<h2>CAVEATS</h2>
<p> The stream versions of the <code>expect</code> functions are much slower than the file descriptor versions because there is no way to portably read an unknown number of bytes without the potential of timing out. Thus, characters are read one at a time. You are therefore strongly encouraged to use the file descriptor versions of <code>expect</code> (although, automated versions of interactive programs don&#8217;t usually demand high speed anyway). </p>
<p> You can actually get the best of both worlds, writing with the usual stream functions and reading with the file descriptor versions of <code>expect</code> as long as you don&#8217;t attempt to intermix other stream input functions (e.g., fgetc). To do this, pass fileno(stream) as the file descriptor each time. Fortunately, there is little reason to use anything but the <code>expect</code> functions when reading from interactive programs. </p>
<p> There is no matching exp_pclose to exp_popen (unlike popen and pclose). It only takes two functions to close down a connection (fclose() followed by waiting on the pid), but it is not uncommon to separate these two actions by large time intervals, so the function seems of little value. </p>
<p> If you are running on a Cray running Unicos (all I know for sure from experience), you must run your compiled program as root or setuid. The problem is that the Cray only allows root processes to open ptys. You should observe as much precautions as possible: If you don&#8217;t need permissions, setuid(0) only immediately before calling one of the spawn functions and immediately set it back afterwards. </p>
<p> Normally, <code>spawn</code> takes little time to execute. If you notice spawn taking a significant amount of time, it is probably encountering ptys that are wedged. A number of tests are run on ptys to avoid entanglements with errant processes. (These take 10 seconds per wedged pty.) Running expect with the -d option will show if <code>expect</code> is encountering many ptys in odd states. If you cannot kill the processes to which these ptys are attached, your only recourse may be to reboot.</p>
<h2>BUGS</h2>
<p> The <code>exp_fexpect</code> functions don&#8217;t work at all under HP-UX &#8211; it appears to be a bug in getc. Follow the advice (above) about using the <code>exp_expect</code> functions (which doesn&#8217;t need to call getc). If you fix the problem (before I do &#8211; please check the latest release) let me know.</p>
<h2>SEE ALSO</h2>
<p> An alternative to this library is the <code>expect</code> program. <code>expect</code> interprets scripts written in a high-level language which direct the dialogue. In addition, the user can take control and interact directly when desired. If it is not absolutely necessary to write your own C program, it is much easier to use <code>expect</code> to perform the entire interaction. It is described further in the following references: </p>
<p> <i>&quot;expect: Curing Those Uncontrollable Fits of Interactivity&quot; </i>by Don Libes, Proceedings of the Summer 1990 USENIX Conference, Anaheim, California, June 11-15, 1990. </p>
<p> <i>&quot;Using expect to Automate System Administration Tasks&quot; </i>by Don Libes, Proceedings of the 1990 USENIX Large Installation Systems Administration Conference, Colorado Springs, Colorado, October 17-19, 1990. </p>
<p> <a href="/docs/linux/man/1-expect/">expect</a>(1), <a href="/docs/linux/man/3-alarm/">alarm</a>(3), <a href="/docs/linux/man/2-read/">read</a>(2), <a href="/docs/linux/man/2-write/">write</a>(2), <a href="/docs/linux/man/3-fdopen/">fdopen</a>(3), <a href="/docs/linux/man/2-execve/">execve</a>(2), <a href="/docs/linux/man/3-execvp/">execvp</a>(3), <a href="/docs/linux/man/3-longjmp/">longjmp</a>(3), <a href="/docs/linux/man/4-pty/">pty</a>(4). </p>
<p> There are several examples C programs in the test directory of <code>expect</code>&#8216;s source distribution which use the expect library. </p>
<h2>AUTHOR</h2>
<p> Don Libes, libes [at] nist.gov, National Institute of Standards and Technology</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> Thanks to John Ousterhout (UCBerkeley) for supplying the pattern matcher. </p>
<p> Design and implementation of the <code>expect</code> library was paid for by the U.S. government and is therefore in the public domain. However the author and NIST would like credit if this program and documentation or portions of them are used. </p>
<h2>Index</h2>
