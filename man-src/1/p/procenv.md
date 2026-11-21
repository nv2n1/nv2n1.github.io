---
title: "procenv(1)"
name: "procenv"
section: "1"
letter: "p"
url: "/docs/linux/man/1-procenv/"
description: "procenv – display process environment details"
---

<h2 class="name">NAME</h2>
<p> procenv &#8211; display process environment details </p>
<h2>SYNOPSIS</h2>
<p> <code>procenv</code> [<i>OPTION</i>]</p>
<h2>DESCRIPTION</h2>
<p> Display details of the process environment in a parseable format.</p>
<h2>OPTIONS</h2>
<p> Options shown with a bracketed asterisk &#8216;(*)&#8217; are non-display options and must preceed any other (display) options. </p>
<dl>
<dt><code>-a</code>, <code>&#8211;meta</code></dt>
<dd> Display meta details.</dd>
<dt><code>-A</code>, <code>&#8211;arguments</code></dt>
<dd> Display program arguments.</dd>
<dt><code>-b</code>, <code>&#8211;libs</code></dt>
<dd> Display details of linked libraries. See <code><a href="/docs/linux/man/3-dl_iterate_phdr/">dl_iterate_phdr</a></code>(3).</dd>
<dt><code>-B</code>, <code>&#8211;libc</code></dt>
<dd> Display standard library details. See <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7) (Linux).</dd>
<dt><code>-c</code>, <code>&#8211;cgroups</code></dt>
<dd> Display cgroup details (Linux only). See <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5).</dd>
<dt><code>-C</code>, <code>&#8211;cpu</code></dt>
<dd> Display CPU and scheduler details. See <code>kvm_getprocs</code>(3) (BSD), <code><a href="/docs/linux/man/3-pthread_getaffinity_np/">pthread_getaffinity_np</a></code>(3)<code>, </code> <code><a href="/docs/linux/man/3-sched_getcpu/">sched_getcpu</a></code>(3) (Linux).</dd>
<dt><code>&#8211;crumb-separator=</code><i>str</i> (*)</dt>
<dd> Specify string <i>str</i> as alternate delimiter for crumb format output (default=&#8217;:&#8217;).</dd>
<dt><code>-d</code>, <code>&#8211;compiler</code></dt>
<dd> Display compiler details. See <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1), <code><a href="/docs/linux/man/1-cc/">cc</a></code>(1) and <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7) (Linux).</dd>
<dt><code>-e</code>, <code>&#8211;environment</code></dt>
<dd> Display environment variables. See <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7).</dd>
<dt><code>-E</code>, <code>&#8211;semaphores</code></dt>
<dd> Display semaphore details (not queryable on BSD). See <code><a href="/docs/linux/man/2-semctl/">semctl</a></code>(2).</dd>
<dt><code>&#8211;exec</code> (*)</dt>
<dd> Treat non-option arguments as program to execute after running <code>procenv</code>. See <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3).</dd>
<dt><code>-f</code>, <code>&#8211;fds</code></dt>
<dd> Display file descriptor details. Under FreeBSD, file descriptor capabilities will also be displayed assuming the kernel has Capsicum support. See <code>cap_getmode</code>(2) (BSD), <code>cap_rights_get</code>(2) (BSD), <code>cap_rights_is_set</code>(3) (BSD), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code>isatty</code>(5).</dd>
<dt><code>-F</code>, <code>&#8211;namespaces</code></dt>
<dd> Display namespace details (Linux only). See <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5).</dd>
<dt><code>&#8211;file=</code><i>FILE</i> (*)</dt>
<dd> Send output to file <i>FILE</i> (implies <code>&#8211;output=file</code>).</dd></dl>
<dl>
<dt><code>&#8211;format=</code><i>FORMAT</i> (*)</dt>
<dd> Specify output format. <i>FORMAT</i> may be one of:</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> <i>crumb</i> (&quot;breadcrumbs&quot;).</dd>
<dt>&bull;</dt>
<dd> <i>json</i> (JavaScript Object Notation).</dd>
<dt>&bull;</dt>
<dd> <i>text</i> (plain ASCII text) [default].</dd>
<dt>&bull;</dt>
<dd> <i>xml</i> (Extensible Markup Language).</dd></dl>
</dl>
</dl>
<dl>
<dt><code>-g</code>, <code>&#8211;sizeof</code></dt>
<dd> Display sizes of data types.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> This help text.</dd>
<dt><code>-i</code>, <code>&#8211;misc</code></dt>
<dd> Display miscellaneous details. See <code>umask</code>(P), <code><a href="/docs/linux/man/3-getcwd/">getcwd</a></code>(3), <code><a href="/docs/linux/man/2-personality/">personality</a></code>(2) (Linux), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2), <code>aa_getcon</code>(2) (Linux), <code><a href="/docs/linux/man/3-getpidcon/">getpidcon</a></code>(3) (Linux), <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3), <code>kvm_getprocs</code>(3) (BSD), <code><a href="/docs/linux/man/2-getpriority/">getpriority</a></code>(2).</dd>
<dt><code>&#8211;indent</code> (*)</dt>
<dd> Number of indent characters to use for each indent (default=2).</dd>
<dt><code>&#8211;indent-char=</code><i>c</i> (*)</dt>
<dd> Use character <i>c</i> for indenting (default=&#8217; &#8216; (space)).</dd>
<dt><code>-j</code>, <code>&#8211;uname</code></dt>
<dd> Display uname details. See <code><a href="/docs/linux/man/2-uname/">uname</a></code>(2).</dd>
<dt><code>-k</code>, <code>&#8211;clocks</code></dt>
<dd> Display clock details. See <code><a href="/docs/linux/man/2-clock_getres/">clock_getres</a></code>(2).</dd>
<dt><code>-l</code>, <code>&#8211;limits</code></dt>
<dd> Display limits. See <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2).</dd>
<dt><code>-L</code>, <code>&#8211;locale</code></dt>
<dd> Display locale details. See <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3) and <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7).</dd>
<dt><code>-m</code>, <code>&#8211;mounts</code></dt>
<dd> Display mount details. See <code><a href="/docs/linux/man/3-getmntent/">getmntent</a></code>(3) and <code><a href="/docs/linux/man/2-statfs/">statfs</a></code>(2) (Linux), and <code>getmntinfo</code>(3) (BSD).</dd></dl>
<dl>
<dt><code>-M</code>, <code>&#8211;message-queues</code></dt>
<dd> Display message queue details (not queryable on BSD). See <code><a href="/docs/linux/man/2-msgctl/">msgctl</a></code>(2).</dd>
<dt><code>-n</code>, <code>&#8211;confstr</code></dt>
<dd> Display confstr details. See <code>confstr</code>(5).</dd></dl>
<dl>
<dt><code>-N</code>, <code>&#8211;network</code></dt>
<dd> Display network details. See <code><a href="/docs/linux/man/3-getifaddrs/">getifaddrs</a></code>(3), <code><a href="/docs/linux/man/3-getnameinfo/">getnameinfo</a></code>(3), and <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2)<code> (Linux)</code>.</dd></dl>
<dl>
<dt><code>-o</code>, <code>&#8211;oom</code></dt>
<dd> Display out-of-memory manager details (Linux only). See <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5).</dd></dl>
<dl>
<dt><code>&#8211;output=</code><i>TYPE</i> (*)</dt>
<dd> Send output to alternative location. <i>TYPE</i> can be one of:</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> <i>file</i> (send output to a file).</dd>
<dt>&bull;</dt>
<dd> <i>stderr</i> (write to standard error).</dd>
<dt>&bull;</dt>
<dd> <i>stdout</i> (write to standard output (default)).</dd>
<dt>&bull;</dt>
<dd> <i>syslog</i> (write to the system log file).</dd>
<dt>&bull;</dt>
<dd> <i>terminal</i> (write to terminal).</dd></dl>
</dl>
</dl>
<dl>
<dt><code>-p</code>, <code>&#8211;process</code></dt>
<dd> Display process details. See <code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2), <code><a href="/docs/linux/man/2-getppid/">getppid</a></code>(2), <code><a href="/docs/linux/man/2-getresuid/">getresuid</a></code>(2), <code><a href="/docs/linux/man/2-getresgid/">getresgid</a></code>(2), <code><a href="/docs/linux/man/2-getuid/">getuid</a></code>(2), <code><a href="/docs/linux/man/2-geteuid/">geteuid</a></code>(2), <code><a href="/docs/linux/man/2-getgid/">getgid</a></code>(2), <code><a href="/docs/linux/man/2-getegid/">getegid</a></code>(2), <code><a href="/docs/linux/man/2-getsid/">getsid</a></code>(2), <code><a href="/docs/linux/man/3-getlogin/">getlogin</a></code>(3), <code><a href="/docs/linux/man/2-getpgrp/">getpgrp</a></code>(2), <code><a href="/docs/linux/man/3-ctermid/">ctermid</a></code>(3), <code><a href="/docs/linux/man/3-tcgetpgrp/">tcgetpgrp</a></code>(3), <code><a href="/docs/linux/man/3-tcgetsid/">tcgetsid</a></code>(3), <code><a href="/docs/linux/man/3-getpwuid/">getpwuid</a></code>(3) and <code><a href="/docs/linux/man/2-getgroups/">getgroups</a></code>(2).</dd></dl>
<dl>
<dt><code>-P</code>, <code>&#8211;platform</code></dt>
<dd> Display platform details.</dd>
<dt><code>-q</code>, <code>&#8211;time</code></dt>
<dd> Display time details. See <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2), <code><a href="/docs/linux/man/3-localtime/">localtime</a></code>(3) and <code><a href="/docs/linux/man/3-asctime/">asctime</a></code>(3).</dd></dl>
<dl>
<dt><code>-r</code>, <code>&#8211;ranges</code></dt>
<dd> Display range of data types. See <code>limits.h</code>(P).</dd></dl>
<dl>
<dt><code>-s</code>, <code>&#8211;signals</code></dt>
<dd> Display signal details. See <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2).</dd></dl>
<dl>
<dt><code>-S</code>, <code>&#8211;shared-memory</code></dt>
<dd> Display shared memory details (not queryable on BSD). See <code><a href="/docs/linux/man/2-shmctl/">shmctl</a></code>(2).</dd></dl>
<dl>
<dt><code>&#8211;separator=</code><i>str</i> (*)</dt>
<dd> Specify string <i>str</i> as alternate delimiter for text format output (default=&#8217;: &#8216;).</dd>
<dt><code>-t</code>, <code>&#8211;tty</code></dt>
<dd> Display terminal details. On Linux, will also show if any attributes are locked when running as <i>root</i>. See <code><a href="/docs/linux/man/3-tcgetattr/">tcgetattr</a></code>(3) and <code><a href="/docs/linux/man/4-tty_ioctl/">tty_ioctl</a></code>(4) (Linux).</dd></dl>
<dl>
<dt><code>-T</code>, <code>&#8211;threads</code></dt>
<dd> Display thread details. See <code><a href="/docs/linux/man/3-pthread_attr_getstacksize/">pthread_attr_getstacksize</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_getstacksize/">pthread_attr_getstacksize</a></code>(3) and <code><a href="/docs/linux/man/3-pthread_attr_getguardsize/">pthread_attr_getguardsize</a></code>(3).</dd></dl>
<dl>
<dt><code>-u</code>, <code>&#8211;stat</code></dt>
<dd> Display stat details. See <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2).</dd></dl>
<dl>
<dt><code>-U</code>, <code>&#8211;rusage</code></dt>
<dd> Display rusage details. See <code><a href="/docs/linux/man/2-getrusage/">getrusage</a></code>(2).</dd></dl>
<dl>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Display version details.</dd></dl>
<dl>
<dt><code>-w</code>, <code>&#8211;capabilities</code></dt>
<dd> Display Linux capability details. For FreeBSD file descriptor capabilities, see <code>&#8211;file-descriptors</code>. See <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) (Linux), <code><a href="/docs/linux/man/3-libcap/">libcap</a></code>(3) (Linux).</dd></dl>
<dl>
<dt><code>-x</code>, <code>&#8211;pathconf</code></dt>
<dd> Display pathconf details. See <code><a href="/docs/linux/man/3-pathconf/">pathconf</a></code>(3).</dd></dl>
<dl>
<dt><code>-y</code>, <code>&#8211;sysconf</code></dt>
<dd> Display sysconf details. See <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3) and <code><a href="/docs/linux/man/7-posixoptions/">posixoptions</a></code>(7) (Linux).</dd></dl>
<dl>
<dt><code>-Y</code>, <code>&#8211;memory</code></dt>
<dd> Display memory details. See <code><a href="/docs/linux/man/2-getpagesize/">getpagesize</a></code>(2), <code><a href="/docs/linux/man/3-numa/">numa</a></code>(3) (Linux) and <code><a href="/docs/linux/man/7-numa/">numa</a></code>(7) (Linux).</dd></dl>
<dl>
<dt><code>-z</code>, <code>&#8211;timezone</code></dt>
<dd> Display timezone details. See <code><a href="/docs/linux/man/3-tzset/">tzset</a></code>(3).</dd></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The following environment variables may be used as aliases to their command-line counterparts:</p>
<dl>
<dt><code>PROCENV_CRUMB_SEPARATOR</code></dt>
<dd> Alternative to <code>&#8211;crumb-separator</code>.</dd></dl>
<dl>
<dt><code>PROCENV_EXEC</code></dt>
<dd> Alternative to <code>&#8211;exec</code>.</dd></dl>
<dl>
<dt><code>PROCENV_FILE</code></dt>
<dd> Alternative to <code>&#8211;file</code>.</dd></dl>
<dl>
<dt><code>PROCENV_FORMAT</code></dt>
<dd> Alternative to <code>&#8211;format</code>.</dd></dl>
<dl>
<dt><code>PROCENV_INDENT</code></dt>
<dd> Alternative to <code>&#8211;indent</code>.</dd></dl>
<dl>
<dt><code>PROCENV_INDENT_CHAR</code></dt>
<dd> Alternative to <code>&#8211;indent-char</code>.</dd></dl>
<dl>
<dt><code>PROCENV_SEPARATOR</code></dt>
<dd> Alternative to <code>&#8211;separator</code>.</dd></dl>
<dl>
<dt><code>PROCENV_OUTPUT</code></dt>
<dd> Alternative to <code>&#8211;output</code>.</dd></dl>
<h2>NOTES</h2>
<dl>
<dt>&bull;</dt>
<dd> Options are considered in order, so <code>&#8211;output</code> should precede any other option.</dd>
<dt>&bull;</dt>
<dd> If no display option is specified, all details are displayed.</dd>
<dt>&bull;</dt>
<dd> Only one display option may be specified.</dd>
<dt>&bull;</dt>
<dd> Command-line options take priority over environment variables.</dd>
<dt>&bull;</dt>
<dd> All values for <code>&#8211;indent-char</code> are literal except &#8216;	&#8217; which can be used to specify a tab character. The same is true for <code>&#8211;separator-char</code> and <code>&#8211;crumb-separator</code> but only if it is the first character specified.</dd>
<dt>&bull;</dt>
<dd> Specifying a visible indent-char is only (vaguely) meaningful for text output.</dd>
<dt>&bull;</dt>
<dd> If <code>&#8211;exec</code> is specified, atleast one non-option argument must also be specified.</dd>
<dt>&bull;</dt>
<dd> Any long option name may be shortened as long as it remains unique.</dd>
<dt>&bull;</dt>
<dd> The <i>crumb</i> output format is designed for easy parsing: it displays the data in a flattened format with each value on a separate line preceded by all appropriate headings which are separated by the current separator.</dd>
<dt>&bull;</dt>
<dd> The <code>&#8211;message-queues</code>, <code>&#8211;semaphores</code> and <code>&#8211;shared-memory</code> options are not available on BSD since although the values are queryable, there is no documented method to do so. </dd>
</dl>
<h2>EXAMPLES</h2>
<pre><code>
#Show limits
procenv - l
#Send compiler information to syslog(note the order of the options).
              procenv-- output = syslog-- compiler
#Write compiler details direct to the terminal
    procenv-- output = terminal-- compiler
#Run a command('mycmd --arg1 --foo=bar') without creating a new
#process, but have procenv run first and log its output to a
#regular file.
        exec procenv-- file = / tmp / procenv.log-- exec-- mycmd-- arg1-- foo = bar
#The following kernel command - line snippet will cause procenv to
#write output to first serial tty device and then execute init(8)
#in debug mode to allow early boot environment to be examined.
                                  init = / usr / bin / procenv PROCENV_FILE = / dev / ttyS0 PROCENV_EXEC = "/sbin/init --debug"
#Display all data in JSON format using an indent of 4 spaces
    procenv-- format = json-- indent = 4
#Display all data in XML format using tabs for indents
    procenv-- format = xml-- indent - char = "	"
#Display signal details in XML format
    procenv-- format = xml-- signals
#Display resource limits in easily - parseable format
        procenv-- format = crumb-- limits
#Produce output suitable for importing into a spreadsheet
            procenv-- format = crumb-- crumb - separator = ',' --separator = ',' --limits
#Produce stylised output
                                   procenv-- format = crumb-- crumb - separator = ' 92 ' --separator = '='
</code></pre>
<h2>LIMITATIONS</h2>
<dl>
<dt>&bull;</dt>
<dd> Spaces within the value of <code>PROCENV_EXEC</code> are treated as delimiters meaning that any spaces within a string argument for example will result in incorrect behaviour.</dd>
<dt>&bull;</dt>
<dd> The separator character must be chosen carefully since no check is performed on the data to see if <i>it itself</i> contains instances of the separator character.</dd></dl>
<h2>AUTHORS</h2>
<p> Written by James Hunt &lt;<code>jamesodhunt [at] ubuntu.com</code>&gt; and Kees Cook &lt;<code>kees [at] ubuntu.com</code>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2012-2014 James Hunt &lt;<code>jamesodhunt [at] ubuntu.com</code>&gt; and Kees Cook &lt;<code>kees [at] ubuntu.com</code>&gt;.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>LICENSE</h2>
<p> GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7) (Linux), <code>capsicum</code>(4) (BSD), <code><a href="/docs/linux/man/1-cc/">cc</a></code>(1), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), <code><a href="/docs/linux/man/1-date/">date</a></code>(1), <code><a href="/docs/linux/man/1-env/">env</a></code>(1), <code>exec</code>(P), <code><a href="/docs/linux/man/1-getconf/">getconf</a></code>(1), <code><a href="/docs/linux/man/1-groups/">groups</a></code>(1), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8), <code>ip</code>(9), <code><a href="/docs/linux/man/1-ipcs/">ipcs</a></code>(1), <code><a href="/docs/linux/man/1-kill/">kill</a></code>(1), <code><a href="/docs/linux/man/1-ldd/">ldd</a></code>(1), <code><a href="/docs/linux/man/1-locale/">locale</a></code>(1), <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1), <code><a href="/docs/linux/man/1-mount/">mount</a></code>(1), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1), <code>rights</code>(4)(BSD), <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/1-stat/">stat</a></code>(1), <code><a href="/docs/linux/man/1-stty/">stty</a></code>(1), <code>umask</code>(P), <code><a href="/docs/linux/man/1-uname/">uname</a></code>(1) </p>
