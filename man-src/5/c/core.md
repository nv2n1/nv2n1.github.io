---
title: "core(5)"
name: "core"
section: "5"
letter: "c"
url: "/docs/linux/man/5-core/"
description: "core – core dump file"
---

<p>core &#8211; core dump file</p>
<h2>Description</h2>
<p>The default action of certain signals is to cause a process to terminate and produce a <i>core dump file</i>, a file containing an image of the process&#8217;s memory at the time of termination. This image can be used in a debugger (e.g., <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1)) to inspect the state of the program at the time that it terminated. A list of the signals which cause a process to dump core can be found in <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7). A process can set its soft <code>RLIMIT_CORE</code> resource limit to place an upper limit on the size of the core dump file that will be produced if it receives a &quot;core dump&quot; signal; see <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2) for details. There are various circumstances in which a core dump file is not produced:</p>
<dl>
<dt>*</p>
<dd>The process does not have permission to write the core file. (By default, the core file is called <i>core</i> or <i>core.pid</i>, where <i>pid</i> is the ID of the process that dumped core, and is created in the current working directory. See below for details on naming.) Writing the core file fails if the directory in which it is to be created is not writable, or if a file with the same name exists and is not writable or is not a regular file (e.g., it is a directory or a symbolic link).</p>
<dt>*</p>
<dd>A (writable, regular) file with the same name as would be used for the core dump already exists, but there is more than one hard link to that file.</p>
<dt>*</p>
<dd>The filesystem where the core dump file would be created is full; or has run out of inodes; or is mounted read-only; or the user has reached their quota for the filesystem.</p>
<dt>*</p>
<dd>The directory in which the core dump file is to be created does not exist.</p>
<dt>*</p>
<dd>The <code>RLIMIT_CORE</code> (core file size) or <code>RLIMIT_FSIZE</code> (file size) resource limits for the process are set to zero; see <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2) and the documentation of the shell&#8217;s <i>ulimit</i> command (<i>limit</i> in <code><a href="/docs/linux/man/1-csh/">csh</a></code>(1)).</p>
<dt>*</p>
<dd>The binary being executed by the process does not have read permission enabled. (This is a security measure to ensure that an executable whose contents are not readable does not produce a&#8212;possibly readable&#8212;core dump containing an image of the executable.)</p>
<dt>*</p>
<dd>The process is executing a set-user-ID (set-group-ID) program that is owned by a user (group) other than the real user (group) ID of the process, or the process is executing a program that has file capabilities (see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)). (However, see the description of the <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_SET_DUMPABLE</code> operation, and the description of the <i>/proc/sys/fs/suid_dumpable</i> file in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5).)</p>
<dt>*</p>
<dd><i>/proc/sys/kernel/core_pattern</i> is empty and <i>/proc/sys/kernel/core_uses_pid</i> contains the value 0. (These files are described below.) Note that if <i>/proc/sys/kernel/core_pattern</i> is empty and <i>/proc/sys/kernel/core_uses_pid</i> contains the value 1, core dump files will have names of the form <i>.pid</i>, and such files are hidden unless one uses the <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1) <i>-a</i> option.</p>
<dt>*</p>
<dd>(Since Linux 3.7) The kernel was configured without the <code>CONFIG_COREDUMP</code> option.</dl>
<p> In addition, a core dump may exclude part of the address space of the process if the <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2) <code>MADV_DONTDUMP</code> flag was employed. On systems that employ <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) as the <i>init</i> framework, core dumps may instead be placed in a location determined by <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1). See below for further details.</p>
<h3>Naming of core dump files</h3>
<p>By default, a core dump file is named <i>core</i>, but the <i>/proc/sys/kernel/core_pattern</i> file (since Linux 2.6 and 2.4.21) can be set to define a template that is used to name core dump files. The template can contain % specifiers which are substituted by the following values when a core file is created:</p>
<dl>
<dd>
<dl>
<dt>%%</p>
<dd>A single % character.</p>
<dt>%c</p>
<dd>Core file size soft resource limit of crashing process (since Linux 2.6.24).</p>
<dt>%d</p>
<dd>Dump mode&#8212;same as value returned by <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_GET_DUMPABLE</code> (since Linux 3.7).</p>
<dt>%e</p>
<dd>The process or thread&#8217;s <i>comm</i> value, which typically is the same as the executable filename (without path prefix, and truncated to a maximum of 15 characters), but may have been modified to be something different; see the discussion of <i>/proc/[pid]/comm</i> and <i>/proc/[pid]/task/[tid]/comm</i> in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5).</p>
<dt>%E</p>
<dd>Pathname of executable, with slashes (&#8216;/&#8217;) replaced by exclamation marks (&#8216;!&#8217;) (since Linux 3.0).</p>
<dt>%g</p>
<dd>Numeric real GID of dumped process.</p>
<dt>%h</p>
<dd>Hostname (same as <i>nodename</i> returned by <code><a href="/docs/linux/man/2-uname/">uname</a></code>(2)).</p>
<dt>%i</p>
<dd>TID of thread that triggered core dump, as seen in the PID namespace in which the thread resides (since Linux 3.18).</p>
<dt>%I</p>
<dd>TID of thread that triggered core dump, as seen in the initial PID namespace (since Linux 3.18).</p>
<dt>%p</p>
<dd>PID of dumped process, as seen in the PID namespace in which the process resides.</p>
<dt>%P</p>
<dd>PID of dumped process, as seen in the initial PID namespace (since Linux 3.12).</p>
<dt>%s</p>
<dd>Number of signal causing dump.</p>
<dt>%t</p>
<dd>Time of dump, expressed as seconds since the Epoch, 1970-01-01 00:00:00 +0000 (UTC).</p>
<dt>%u</p>
<dd>Numeric real UID of dumped process.</dl>
</dl>
<p> A single % at the end of the template is dropped from the core filename, as is the combination of a % followed by any character other than those listed above. All other characters in the template become a literal part of the core filename. The template may include &#8216;/&#8217; characters, which are interpreted as delimiters for directory names. The maximum size of the resulting core filename is 128 bytes (64 bytes in kernels before 2.6.19). The default value in this file is &quot;core&quot;. For backward compatibility, if <i>/proc/sys/kernel/core_pattern</i> does not include <i>%p</i> and <i>/proc/sys/kernel/core_uses_pid</i> (see below) is nonzero, then .PID will be appended to the core filename. Paths are interpreted according to the settings that are active for the crashing process. That means the crashing process&#8217;s mount namespace (see <code><a href="/docs/linux/man/7-mount_namespaces/">mount_namespaces</a></code>(7)), its current working directory (found via <code><a href="/docs/linux/man/2-getcwd/">getcwd</a></code>(2)), and its root directory (see <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2)). Since version 2.4, Linux has also provided a more primitive method of controlling the name of the core dump file. If the <i>/proc/sys/kernel/core_uses_pid</i> file contains the value 0, then a core dump file is simply named <i>core</i>. If this file contains a nonzero value, then the core dump file includes the process ID in a name of the form <i>core.PID</i>. Since Linux 3.6, if <i>/proc/sys/fs/suid_dumpable</i> is set to 2 (&quot;suidsafe&quot;), the pattern must be either an absolute pathname (starting with a leading &#8216;/&#8217; character) or a pipe, as defined below.</p>
<h3>Piping core dumps to a program</h3>
<p>Since kernel 2.6.19, Linux supports an alternate syntax for the <i>/proc/sys/kernel/core_pattern</i> file. If the first character of this file is a pipe symbol (<code>|</code>), then the remainder of the line is interpreted as the command-line for a user-space program (or script) that is to be executed. Since kernel 5.3.0, the pipe template is split on spaces into an argument list <i>before</i> the template parameters are expanded. In earlier kernels, the template parameters are expanded first and the resulting string is split on spaces into an argument list. This means that in earlier kernels executable names added by the <i>%e</i> and <i>%E</i> template parameters could get split into multiple arguments. So the core dump handler needs to put the executable names as the last argument and ensure it joins all parts of the executable name using spaces. Executable names with multiple spaces in them are not correctly represented in earlier kernels, meaning that the core dump handler needs to use mechanisms to find the executable name. Instead of being written to a file, the core dump is given as standard input to the program. Note the following points:</p>
<dl>
<dt>*</p>
<dd>The program must be specified using an absolute pathname (or a pathname relative to the root directory, <i>/</i>), and must immediately follow the &#8216;|&#8217; character.</p>
<dt>*</p>
<dd>The command-line arguments can include any of the % specifiers listed above. For example, to pass the PID of the process that is being dumped, specify <i>%p</i> in an argument.</p>
<dt>*</p>
<dd>The process created to run the program runs as user and group <i>root</i>.</p>
<dt>*</p>
<dd>Running as <i>root</i> does not confer any exceptional security bypasses. Namely, LSMs (e.g., SELinux) are still active and may prevent the handler from accessing details about the crashed process via <i>/proc/[pid]</i>.</p>
<dt>*</p>
<dd>The program pathname is interpreted with respect to the initial mount namespace as it is always executed there. It is not affected by the settings (e.g., root directory, mount namespace, current working directory) of the crashing process.</p>
<dt>*</p>
<dd>The process runs in the initial namespaces (PID, mount, user, and so on) and not in the namespaces of the crashing process. One can utilize specifiers such as <i>%P</i> to find the right <i>/proc/[pid]</i> directory and probe/enter the crashing process&#8217;s namespaces if needed.</p>
<dt>*</p>
<dd>The process starts with its current working directory as the root directory. If desired, it is possible change to the working directory of the dumping process by employing the value provided by the <i>%P</i> specifier to change to the location of the dumping process via <i>/proc/[pid]/cwd</i>.</p>
<dt>*</p>
<dd>Command-line arguments can be supplied to the program (since Linux 2.6.24), delimited by white space (up to a total line length of 128 bytes).</p>
<dt>*</p>
<dd>The <code>RLIMIT_CORE</code> limit is not enforced for core dumps that are piped to a program via this mechanism.</dl>
<h3>/proc/sys/kernel/core_pipe_limit</h3>
<p>When collecting core dumps via a pipe to a user-space program, it can be useful for the collecting program to gather data about the crashing process from that process&#8217;s <i>/proc/[pid]</i> directory. In order to do this safely, the kernel must wait for the program collecting the core dump to exit, so as not to remove the crashing process&#8217;s <i>/proc/[pid]</i> files prematurely. This in turn creates the possibility that a misbehaving collecting program can block the reaping of a crashed process by simply never exiting. Since Linux 2.6.32, the <i>/proc/sys/kernel/core_pipe_limit</i> can be used to defend against this possibility. The value in this file defines how many concurrent crashing processes may be piped to user-space programs in parallel. If this value is exceeded, then those crashing processes above this value are noted in the kernel log and their core dumps are skipped. A value of 0 in this file is special. It indicates that unlimited processes may be captured in parallel, but that no waiting will take place (i.e., the collecting program is not guaranteed access to <i>/proc/&lt;crashing-PID&gt;</i>). The default value for this file is 0.</p>
<h3>Controlling which mappings are written to the core dump</h3>
<p>Since kernel 2.6.23, the Linux-specific <i>/proc/[pid]/coredump_filter</i> file can be used to control which memory segments are written to the core dump file in the event that a core dump is performed for the process with the corresponding process ID. The value in the file is a bit mask of memory mapping types (see <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2)). If a bit is set in the mask, then memory mappings of the corresponding type are dumped; otherwise they are not dumped. The bits in this file have the following meanings:</p>
<dl>
<dd>
<dl>
<dt>bit 0</p>
<dd>Dump anonymous private mappings.</p>
<dt>bit 1</p>
<dd>Dump anonymous shared mappings.</p>
<dt>bit 2</p>
<dd>Dump file-backed private mappings.</p>
<dt>bit 3</p>
<dd>Dump file-backed shared mappings.</p>
<dt>bit 4 (since Linux 2.6.24)</p>
<dd>Dump ELF headers.</p>
<dt>bit 5 (since Linux 2.6.28)</p>
<dd>Dump private huge pages.</p>
<dt>bit 6 (since Linux 2.6.28)</p>
<dd>Dump shared huge pages.</p>
<dt>bit 7 (since Linux 4.4)</p>
<dd>Dump private DAX pages.</p>
<dt>bit 8 (since Linux 4.4)</p>
<dd>Dump shared DAX pages.</dl>
</dl>
<p> By default, the following bits are set: 0, 1, 4 (if the <code>CONFIG_CORE_DUMP_DEFAULT_ELF_HEADERS</code> kernel configuration option is enabled), and 5. This default can be modified at boot time using the <i>coredump_filter</i> boot option. The value of this file is displayed in hexadecimal. (The default value is thus displayed as 33.) Memory-mapped I/O pages such as frame buffer are never dumped, and virtual DSO (<code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7)) pages are always dumped, regardless of the <i>coredump_filter</i> value. A child process created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) inherits its parent&#8217;s <i>coredump_filter</i> value; the <i>coredump_filter</i> value is preserved across an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). It can be useful to set <i>coredump_filter</i> in the parent shell before running a program, for example: $<code> echo 0x7 &gt; /proc/self/coredump_filter</code> $<code> ./some_program</code> This file is provided only if the kernel was built with the <code>CONFIG_ELF_CORE</code> configuration option.</p>
<h3>Core dumps and systemd</h3>
<p>On systems using the <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) <i>init</i> framework, core dumps may be placed in a location determined by <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1). To do this, <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) employs the <i>core_pattern</i> feature that allows piping core dumps to a program. One can verify this by checking whether core dumps are being piped to the <code><a href="/docs/linux/man/8-systemd-coredump/">systemd-coredump</a></code>(8) program: $ <code>cat /proc/sys/kernel/core_pattern</code> |/usr/lib/systemd/systemd-coredump %P %u %g %s %t %c %e In this case, core dumps will be placed in the location configured for <code><a href="/docs/linux/man/8-systemd-coredump/">systemd-coredump</a></code>(8), typically as <code><a href="/docs/linux/man/1-lz4/">lz4</a></code>(1) compressed files in the directory <i>/var/lib/systemd/coredump/</i>. One can list the core dumps that have been recorded by <code><a href="/docs/linux/man/8-systemd-coredump/">systemd-coredump</a></code>(8) using <code><a href="/docs/linux/man/1-coredumpctl/">coredumpctl</a></code>(1): $ <code>coredumpctl list | tail -5</code> Wed 2017-10-11 22:25:30 CEST 2748 1000 1000 3 present /usr/bin/sleep Thu 2017-10-12 06:29:10 CEST 2716 1000 1000 3 present /usr/bin/sleep Thu 2017-10-12 06:30:50 CEST 2767 1000 1000 3 present /usr/bin/sleep Thu 2017-10-12 06:37:40 CEST 2918 1000 1000 3 present /usr/bin/cat Thu 2017-10-12 08:13:07 CEST 2955 1000 1000 3 present /usr/bin/cat The information shown for each core dump includes the date and time of the dump, the PID, UID, and GID of the dumping process, the signal number that caused the core dump, and the pathname of the executable that was being run by the dumped process. Various options to <code><a href="/docs/linux/man/1-coredumpctl/">coredumpctl</a></code>(1) allow a specified coredump file to be pulled from the <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) location into a specified file. For example, to extract the core dump for PID 2955 shown above to a file named <i>core</i> in the current directory, one could use: $ <code>coredumpctl dump 2955 -o core</code> For more extensive details, see the <code><a href="/docs/linux/man/1-coredumpctl/">coredumpctl</a></code>(1) manual page. To (persistently) disable the <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) mechanism that archives core dumps, restoring to something more like traditional Linux behavior, one can set an override for the <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) mechanism, using something like: # <code>echo &quot;kernel.core_pattern=core.%p&quot; &gt; \</code> <code> /etc/sysctl.d/50-coredump.conf</code> # <code>/lib/systemd/systemd-sysctl</code> It is also possible to temporarily (i.e., until the next reboot) change the <i>core_pattern</i> setting using a command such as the following (which causes the names of core dump files to include the executable name as well as the number of the signal which triggered the core dump): </p>
<pre><code># sysctl -w kernel.core_pattern=&quot;%e-%s.core&quot;</code></pre>
<h2>Notes</h2>
<p>The <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1) <i>gcore</i> command can be used to obtain a core dump of a running process. </p>
<p> In Linux versions up to and including 2.6.27, if a multithreaded process (or, more precisely, a process that shares its memory with another process by being created with the <code>CLONE_VM</code> flag of <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2)) dumps core, then the process ID is always appended to the core filename, unless the process ID was already included elsewhere in the filename via a <i>%p</i> specification in <i>/proc/sys/kernel/core_pattern</i>. (This is primarily useful when employing the obsolete LinuxThreads implementation, where each thread of a process has a different PID.)</p>
<h2>Examples</h2>
<p>The program below can be used to demonstrate the use of the pipe syntax in the <i>/proc/sys/kernel/core_pattern</i> file. The following shell session demonstrates the use of this program (compiled to create an executable named <i>core_pattern_pipe_test</i>): $<code> cc -o core_pattern_pipe_test core_pattern_pipe_test.c</code> $<code> su</code> Password: #<code> echo &quot;|$PWD/core_pattern_pipe_test %p UID=%u GID=%g sig=%s&quot; &gt; \</code> <code> /proc/sys/kernel/core_pattern</code> #<code> exit</code> $<code> sleep 100</code> <code>ha\</code> # type control-backslash Quit (core dumped) $<code> cat core.info</code> argc=5 argc[0]=&lt;/home/mtk/core_pattern_pipe_test&gt; argc[1]=&lt;20575&gt; argc[2]=&lt;UID=1000&gt; argc[3]=&lt;GID=100&gt; argc[4]=&lt;sig=3&gt; Total bytes in core dump: 282624</p>
<h3>Program source</h3>
<p>/* core_pattern_pipe_test.c */ </p>
<pre><code>#define _GNU_SOURCE
#include &lt;fcntl.h&gt;
#include &lt;limits.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;sys/stat.h&gt;
#include &lt;unistd.h&gt;
#define BUF_SIZE 1024
int main(int argc, char *argv[])
{
    ssize_t nread, tot;
    char buf[BUF_SIZE];
    FILE *fp;
    char cwd[PATH_MAX];
    /* Change our current working directory to that of the
           crashing process */
    snprintf(cwd, PATH_MAX, &quot;/proc/%s/cwd&quot;, argv[1]);
    chdir(cwd);
    /* Write output to file &quot;core.info&quot; in that directory */
    fp = fopen(&quot;core.info&quot;, &quot;w+&quot;);
    if (fp == NULL)
        exit(EXIT_FAILURE);
    /* Display command-line arguments given to core_pattern
           pipe program */
    fprintf(fp, &quot;argc=%d
&quot;, argc);
    for (int j = 0; j &lt; argc; j++)
        fprintf(fp, &quot;argc[%d]=&lt;%s&gt;
&quot;, j, argv[j]);
    /* Count bytes in standard input (the core dump) */
    tot = 0;
    while ((nread = read(STDIN_FILENO, buf, BUF_SIZE)) &gt; 0)
        tot += nread;
    fprintf(fp, &quot;Total bytes in core dump: %zd
&quot;, tot);
    fclose(fp);
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-bash/">bash</a></code>(1), <code><a href="/docs/linux/man/1-coredumpctl/">coredumpctl</a></code>(1), <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1), <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/5-elf/">elf</a></code>(5), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7), <code><a href="/docs/linux/man/8-systemd-coredump/">systemd-coredump</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
