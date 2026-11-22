---
title: "wtmp(5)"
name: "wtmp"
section: "5"
letter: "w"
url: "/docs/linux/man/5-wtmp/"
description: "utmp, wtmp – login records"
---

<p>utmp, wtmp &#8211; login records</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;utmp.h&gt;</code></pre>
<h2>Description</h2>
<p>The <i>utmp</i> file allows one to discover information about who is currently using the system. There may be more users currently using the system, because not all programs use utmp logging. <code>Warning:</code> <i>utmp</i> must not be writable by the user class &quot;other&quot;, because many system programs (foolishly) depend on its integrity. You risk faked system logfiles and modifications of system files if you leave <i>utmp</i> writable to any user other than the owner and group owner of the file. The file is a sequence of <i>utmp</i> structures, declared as follows in <i>&lt;utmp.h&gt;</i> (note that this is only one of several definitions around; details depend on the version of libc): /* Values for ut_type field, below */<br/>
#define EMPTY 0         /* Record does not contain valid info \<br/>
                           (formerly known as UT_UNKNOWN on Linux) */<br/>
#define RUN_LVL 1       /* Change in system run-level (see \<br/>
                           init(1)) */<br/>
#define BOOT_TIME 2     /* Time of system boot (in ut_tv) */<br/>
#define NEW_TIME 3      /* Time after system clock change \<br/>
                           (in ut_tv) */<br/>
#define OLD_TIME 4      /* Time before system clock change \<br/>
                           (in ut_tv) */<br/>
#define INIT_PROCESS 5  /* Process spawned by init(1) */<br/>
#define LOGIN_PROCESS 6 /* Session leader process for user login */<br/>
#define USER_PROCESS 7  /* Normal process */<br/>
#define DEAD_PROCESS 8  /* Terminated process */<br/>
#define ACCOUNTING 9    /* Not implemented */<br/>
#define UT_LINESIZE 32<br/>
#define UT_NAMESIZE 32<br/>
#define UT_HOSTSIZE 256<br/>
struct exit_status {     /* Type for ut_exit, below */<br/>
    short e_termination; /* Process termination status */<br/>
    short e_exit;        /* Process exit status */<br/>
};<br/>
struct utmp {<br/>
    short ut_type;              /* Type of record */<br/>
    pid_t ut_pid;               /* PID of login process */<br/>
    char ut_line[UT_LINESIZE];  /* Device name of tty &#8211; &quot;/dev/&quot; */<br/>
    char ut_id[4];              /* Terminal name suffix,<br/>
                                   or inittab(5) ID */<br/>
    char ut_user[UT_NAMESIZE];  /* Username */<br/>
    char ut_host[UT_HOSTSIZE];  /* Hostname for remote login, or<br/>
                                   kernel version for run-level<br/>
                                   messages */<br/>
    struct exit_status ut_exit; /* Exit status of a process<br/>
                                   marked as DEAD_PROCESS; not<br/>
                                   used by Linux init(1) */<br/>
    /* The ut_session and ut_tv fields must be the same size when<br/>
       compiled 32- and 64-bit.  This allows data files and shared<br/>
       memory to be shared between 32- and 64-bit applications. */<br/>
#if __WORDSIZE == 64 &amp;&amp; defined __WORDSIZE_COMPAT32<br/>
    int32_t ut_session; /* Session ID (getsid(2)),<br/>
                           used for windowing */<br/>
    struct {<br/>
        int32_t tv_sec;  /* Seconds */<br/>
        int32_t tv_usec; /* Microseconds */<br/>
    } ut_tv;             /* Time entry was made */<br/>
#else<br/>
    long ut_session;      /* Session ID */<br/>
    struct timeval ut_tv; /* Time entry was made */<br/>
#endif<br/>
    int32_t ut_addr_v6[4]; /* Internet address of remote<br/>
                                  host; IPv4 address uses<br/>
                                  just ut_addr_v6[0] */<br/>
    char __unused[20];     /* Reserved for future use */<br/>
};<br/>
/* Backward compatibility hacks */<br/>
#define ut_name ut_user<br/>
#ifndef _NO_UT_TIME<br/>
#define ut_time ut_tv.tv_sec<br/>
#endif<br/>
#define ut_xtime ut_tv.tv_sec<br/>
#define ut_addr ut_addr_v6[0] This structure gives the name of the special file associated with the user&#8217;s terminal, the user&#8217;s login name, and the time of login in the form of <code><a href="/docs/linux/man/2-time/">time</a></code>(2). String fields are terminated by a null byte (&#8216;\0&#8217;) if they are shorter than the size of the field. </p>
<p> The first entries ever created result from <code><a href="/docs/linux/man/1-init/">init</a></code>(1) processing <code><a href="/docs/linux/man/5-inittab/">inittab</a></code>(5). Before an entry is processed, though, <code><a href="/docs/linux/man/1-init/">init</a></code>(1) cleans up utmp by setting <i>ut_type</i> to <code>DEAD_PROCESS</code>, clearing <i>ut_user</i>, <i>ut_host</i>, and <i>ut_time</i> with null bytes for each record which <i>ut_type</i> is not <code>DEAD_PROCESS</code> or <code>RUN_LVL</code> and where no process with PID <i>ut_pid</i> exists. If no empty record with the needed <i>ut_id</i> can be found, <code><a href="/docs/linux/man/1-init/">init</a></code>(1) creates a new one. It sets <i>ut_id</i> from the inittab, <i>ut_pid</i> and <i>ut_time</i> to the current values, and <i>ut_type</i> to <code>INIT_PROCESS</code>. </p>
<p> <code><a href="/docs/linux/man/8-mingetty/">mingetty</a></code>(8) (or <code><a href="/docs/linux/man/8-agetty/">agetty</a></code>(8)) locates the entry by the PID, changes <i>ut_type</i> to <code>LOGIN_PROCESS</code>, changes <i>ut_time</i>, sets <i>ut_line</i>, and waits for connection to be established. <code><a href="/docs/linux/man/1-login/">login</a></code>(1), after a user has been authenticated, changes <i>ut_type</i> to <code>USER_PROCESS</code>, changes <i>ut_time</i>, and sets <i>ut_host</i> and <i>ut_addr</i>. Depending on <code><a href="/docs/linux/man/8-mingetty/">mingetty</a></code>(8) (or <code><a href="/docs/linux/man/8-agetty/">agetty</a></code>(8)) and <code><a href="/docs/linux/man/1-login/">login</a></code>(1), records may be located by <i>ut_line</i> instead of the preferable <i>ut_pid</i>. </p>
<p> When <code><a href="/docs/linux/man/1-init/">init</a></code>(1) finds that a process has exited, it locates its utmp entry by <i>ut_pid</i>, sets <i>ut_type</i> to <code>DEAD_PROCESS</code>, and clears <i>ut_user</i>, <i>ut_host</i>, and <i>ut_time</i> with null bytes. </p>
<p> <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1) and other terminal emulators directly create a <code>USER_PROCESS</code> record and generate the <i>ut_id</i> by using the string that suffix part of the terminal name (the characters following <i>/dev/[pt]ty</i>). If they find a <code>DEAD_PROCESS</code> for this ID, they recycle it, otherwise they create a new entry. If they can, they will mark it as <code>DEAD_PROCESS</code> on exiting and it is advised that they null <i>ut_line</i>, <i>ut_time</i>, <i>ut_user</i>, and <i>ut_host</i> as well. </p>
<p> <code><a href="/docs/linux/man/8-telnetd/">telnetd</a></code>(8) sets up a <code>LOGIN_PROCESS</code> entry and leaves the rest to <code><a href="/docs/linux/man/1-login/">login</a></code>(1) as usual. After the telnet session ends, <code><a href="/docs/linux/man/8-telnetd/">telnetd</a></code>(8) cleans up utmp in the described way. </p>
<p> The <i>wtmp</i> file records all logins and logouts. Its format is exactly like <i>utmp</i> except that a null username indicates a logout on the associated terminal. Furthermore, the terminal name <code>~</code> with username <code>shutdown</code> or <code>reboot</code> indicates a system shutdown or reboot and the pair of terminal names <code>|</code>/<code>}</code> logs the old/new system time when <code><a href="/docs/linux/man/1-date/">date</a></code>(1) changes it. <i>wtmp</i> is maintained by <code><a href="/docs/linux/man/1-login/">login</a></code>(1), <code><a href="/docs/linux/man/1-init/">init</a></code>(1), and some versions of <code><a href="/docs/linux/man/8-getty/">getty</a></code>(8) (e.g., <code><a href="/docs/linux/man/8-mingetty/">mingetty</a></code>(8) or <code><a href="/docs/linux/man/8-agetty/">agetty</a></code>(8)). None of these programs creates the file, so if it is removed, record-keeping is turned off.  </p>
<h2>FILES</h2>
<p> <i>/var/run/utmp</i> <br/>
 <i>/var/log/wtmp</i>  </p>
<h2>CONFORMING TO</h2>
<p> POSIX.1 does not specify a <i>utmp</i> structure, but rather one named <i>utmpx</i>, with specifications for the fields <i>ut_type</i>, <i>ut_pid</i>, <i>ut_line</i>, <i>ut_id</i>, <i>ut_user</i>, and <i>ut_tv</i>. POSIX.1 does not specify the lengths of the <i>ut_line</i> and <i>ut_user</i> fields. </p>
<p> Linux defines the <i>utmpx</i> structure to be the same as the <i>utmp</i> structure.  </p>
<h3>Comparison with historical systems</h3>
<p> Linux utmp entries conform neither to v7/BSD nor to System V; they are a mix of the two. </p>
<p> v7/BSD has fewer fields; most importantly it lacks <i>ut_type</i>, which causes native v7/BSD-like programs to display (for example) dead or login entries. Further, there is no configuration file which allocates slots to sessions. BSD does so because it lacks <i>ut_id</i> fields. </p>
<p> In Linux (as in System V), the <i>ut_id</i> field of a record will never change once it has been set, which reserves that slot without needing a configuration file. Clearing <i>ut_id</i> may result in race conditions leading to corrupted utmp entries and potential security holes. Clearing the abovementioned fields by filling them with null bytes is not required by System V semantics, but makes it possible to run many programs which assume BSD semantics and which do not modify utmp. Linux uses the BSD conventions for line contents, as documented above. </p>
<p> System V has no <i>ut_host</i> or <i>ut_addr_v6</i> fields.  </p>
<h2>NOTES</h2>
<p> Unlike various other systems, where utmp logging can be disabled by removing the file, utmp must always exist on Linux. If you want to disable <code><a href="/docs/linux/man/1-who/">who</a></code>(1), then do not make utmp world readable. </p>
<p> The file format is machine-dependent, so it is recommended that it be processed only on the machine architecture where it was created. </p>
<p> Note that on <i>biarch</i> platforms, that is, systems which can run both 32-bit and 64-bit applications (x86-64, ppc64, s390x, etc.), <i>ut_tv</i> is the same size in 32-bit mode as in 64-bit mode. The same goes for <i>ut_session</i> and <i>ut_time</i> if they are present. This allows data files and shared memory to be shared between 32-bit and 64-bit applications. This is achieved by changing the type of <i>ut_session</i> to <i>int32_t</i>, and that of <i>ut_tv</i> to a struct with two <i>int32_t</i> fields <i>tv_sec</i> and <i>tv_usec</i>. Since <i>ut_tv</i> may not be the same as <i>struct timeval</i>, then instead of the call: </p>
<p> gettimeofday((struct timeval *) &amp;ut.ut_tv, NULL); </p>
<p> the following method of setting this field is recommended: </p>
<p> struct utmp ut; struct timeval tv; </p>
<p> gettimeofday(&amp;tv, NULL); ut.ut_tv.tv_sec = tv.tv_sec; ut.ut_tv.tv_usec = tv.tv_usec;  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ac/">ac</a></code>(1), <code><a href="/docs/linux/man/1-date/">date</a></code>(1), <code><a href="/docs/linux/man/1-init/">init</a></code>(1), <code><a href="/docs/linux/man/1-last/">last</a></code>(1), <code><a href="/docs/linux/man/1-login/">login</a></code>(1), <code><a href="/docs/linux/man/1-logname/">logname</a></code>(1), <code><a href="/docs/linux/man/1-lslogins/">lslogins</a></code>(1), <code><a href="/docs/linux/man/1-users/">users</a></code>(1), <code><a href="/docs/linux/man/1-utmpdump/">utmpdump</a></code>(1), <code><a href="/docs/linux/man/1-who/">who</a></code>(1), <code><a href="/docs/linux/man/3-getutent/">getutent</a></code>(3), <code><a href="/docs/linux/man/3-getutmp/">getutmp</a></code>(3), <code><a href="/docs/linux/man/3-login/">login</a></code>(3), <code><a href="/docs/linux/man/3-logout/">logout</a></code>(3), <code><a href="/docs/linux/man/3-logwtmp/">logwtmp</a></code>(3), <code><a href="/docs/linux/man/3-updwtmp/">updwtmp</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
