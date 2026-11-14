---
title: "acct(5)"
name: "acct"
section: "5"
letter: "a"
url: "/docs/linux/man/5-acct/"
description: "acct – process accounting file"
---

<p>acct &#8211; process accounting file</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/acct.h&gt;</code></pre>
<h2>Description</h2>
<p>If the kernel is built with the process accounting option enabled (<code>CONFIG_BSD_PROCESS_ACCT</code>), then calling <code><a href="/docs/linux/man/2-acct/">acct</a></code>(2) starts process accounting, for example: acct(&quot;/var/log/pacct&quot;); When process accounting is enabled, the kernel writes a record to the accounting file as each process on the system terminates. This record contains information about the terminated process, and is defined in <i>&lt;sys/acct.h&gt;</i> as follows: struct acct_v3 {<br />
    char ac_flag;            /* Flags */<br />
    char ac_version;         /* Always set to ACCT_VERSION (3) */<br />
    u_int16_t ac_tty;        /* Controlling terminal */<br />
    u_int32_t ac_exitcode;   /* Process termination status */<br />
    u_int32_t ac_uid;        /* Real user ID */<br />
    u_int32_t ac_gid;        /* Real group ID */<br />
    u_int32_t ac_pid;        /* Process ID */<br />
    u_int32_t ac_ppid;       /* Parent process ID */<br />
    u_int32_t ac_btime;      /* Process creation time */<br />
    float ac_etime;          /* Elapsed time */<br />
    comp_t ac_utime;         /* User CPU time */<br />
    comp_t ac_stime;         /* System time */<br />
    comp_t ac_mem;           /* Average memory usage (kB) */<br />
    comp_t ac_io;            /* Characters transferred (unused) */<br />
    comp_t ac_rw;            /* Blocks read or written<br />
                                (unused) */<br />
    comp_t ac_minflt;        /* Minor page faults */<br />
    comp_t ac_majflt;        /* Major page faults */<br />
    comp_t ac_swaps;         /* Number of swaps (unused) */<br />
    char ac_comm[ACCT_COMM]; /* Command name */<br />
}; typedef u_int16_t comp_t; struct acct_v3 {<br />
    char ac_flag;            /* Flags */<br />
    char ac_version;         /* Always set to ACCT_VERSION (3) */<br />
    u_int16_t ac_tty;        /* Controlling terminal */<br />
    u_int32_t ac_exitcode;   /* Process termination status */<br />
    u_int32_t ac_uid;        /* Real user ID */<br />
    u_int32_t ac_gid;        /* Real group ID */<br />
    u_int32_t ac_pid;        /* Process ID */<br />
    u_int32_t ac_ppid;       /* Parent process ID */<br />
    u_int32_t ac_btime;      /* Process creation time */<br />
    float ac_etime;          /* Elapsed time */<br />
    comp_t ac_utime;         /* User CPU time */<br />
    comp_t ac_stime;         /* System time */<br />
    comp_t ac_mem;           /* Average memory usage (kB) */<br />
    comp_t ac_io;            /* Characters transferred (unused) */<br />
    comp_t ac_rw;            /* Blocks read or written<br />
                                (unused) */<br />
    comp_t ac_minflt;        /* Minor page faults */<br />
    comp_t ac_majflt;        /* Major page faults */<br />
    comp_t ac_swaps;         /* Number of swaps (unused) */<br />
    char ac_comm[ACCT_COMM]; /* Command name */<br />
}; The <i>comp_t</i> data type is a floating-point value consisting of a 3-bit, base-8 exponent, and a 13-bit mantissa. A value, <i>c</i>, of this type can be converted to a (long) integer as follows: struct acct_v3 {<br />
    char ac_flag;            /* Flags */<br />
    char ac_version;         /* Always set to ACCT_VERSION (3) */<br />
    u_int16_t ac_tty;        /* Controlling terminal */<br />
    u_int32_t ac_exitcode;   /* Process termination status */<br />
    u_int32_t ac_uid;        /* Real user ID */<br />
    u_int32_t ac_gid;        /* Real group ID */<br />
    u_int32_t ac_pid;        /* Process ID */<br />
    u_int32_t ac_ppid;       /* Parent process ID */<br />
    u_int32_t ac_btime;      /* Process creation time */<br />
    float ac_etime;          /* Elapsed time */<br />
    comp_t ac_utime;         /* User CPU time */<br />
    comp_t ac_stime;         /* System time */<br />
    comp_t ac_mem;           /* Average memory usage (kB) */<br />
    comp_t ac_io;            /* Characters transferred (unused) */<br />
    comp_t ac_rw;            /* Blocks read or written<br />
                                (unused) */<br />
    comp_t ac_minflt;        /* Minor page faults */<br />
    comp_t ac_majflt;        /* Major page faults */<br />
    comp_t ac_swaps;         /* Number of swaps (unused) */<br />
    char ac_comm[ACCT_COMM]; /* Command name */<br />
}; The <i>ac_utime</i>, <i>ac_stime</i>, and <i>ac_etime</i> fields measure time in &quot;clock ticks&quot;; divide these values by <i>sysconf(_SC_CLK_TCK)</i> to convert them to seconds.</p>
<h3>Version 3 accounting file format</h3>
<p>Since kernel 2.6.8, an optional alternative version of the accounting file can be produced if the <code>CONFIG_BSD_PROCESS_ACCT_V3</code> option is set when building the kernel. With this option is set, the records written to the accounting file contain additional fields, and the width of <i>c_uid</i> and <i>ac_gid</i> fields is widened from 16 to 32 bits (in line with the increased size of UID and GIDs in Linux 2.4 and later). The records are defined as follows: </p>
<pre><code>struct acct_v3 {
    char ac_flag;            /* Flags */
    char ac_version;         /* Always set to ACCT_VERSION (3) */
    u_int16_t ac_tty;        /* Controlling terminal */
    u_int32_t ac_exitcode;   /* Process termination status */
    u_int32_t ac_uid;        /* Real user ID */
    u_int32_t ac_gid;        /* Real group ID */
    u_int32_t ac_pid;        /* Process ID */
    u_int32_t ac_ppid;       /* Parent process ID */
    u_int32_t ac_btime;      /* Process creation time */
    float ac_etime;          /* Elapsed time */
    comp_t ac_utime;         /* User CPU time */
    comp_t ac_stime;         /* System time */
    comp_t ac_mem;           /* Average memory usage (kB) */
    comp_t ac_io;            /* Characters transferred (unused) */
    comp_t ac_rw;            /* Blocks read or written
                                (unused) */
    comp_t ac_minflt;        /* Minor page faults */
    comp_t ac_majflt;        /* Major page faults */
    comp_t ac_swaps;         /* Number of swaps (unused) */
    char ac_comm[ACCT_COMM]; /* Command name */
};</code></pre>
<h2>Versions</h2>
<p>The <i>acct_v3</i> structure is defined in glibc since version 2.6.</p>
<h2>Conforming To</h2>
<p>Process accounting originated on BSD. Although it is present on most systems, it is not standardized, and the details vary somewhat between systems.</p>
<h2>Notes</h2>
<p>Records in the accounting file are ordered by termination time of the process. </p>
<p> In kernels up to and including 2.6.9, a separate accounting record is written for each thread created using the NPTL threading library; since Linux 2.6.10, a single accounting record is written for the entire process on termination of the last thread in the process. </p>
<p> The <i>/proc/sys/kernel/acct</i> file, described in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), defines settings that control the behavior of process accounting when disk space runs low.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lastcomm/">lastcomm</a></code>(1), <code><a href="/docs/linux/man/2-acct/">acct</a></code>(2), <code><a href="/docs/linux/man/8-accton/">accton</a></code>(8), <code><a href="/docs/linux/man/8-sa/">sa</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
