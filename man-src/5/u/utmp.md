---
title: "utmp(5)"
name: "utmp"
section: "5"
letter: "u"
url: "/docs/linux/man/5-utmp/"
description: "utmp, wtmp – login records"
---

<p>utmp, wtmp &#8211; login records</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;utmp.h&gt;</code></pre>
<h2>Description</h2>
<p>The <i>utmp</i> file allows one to discover information about who is currently using the system. There may be more users currently using the system, because not all programs use utmp logging. <code>Warning:</code> <i>utmp</i> must not be writable by the user class &quot;other&quot;, because many system programs (foolishly) depend on its integrity. You risk faked system logfiles and modifications of system files if you leave <i>utmp</i> writable to any user other than the owner and group owner of the file. The file is a sequence of <i>utmp</i> structures, declared as follows in <i>&lt;utmp.h&gt;</i> (note that this is only one of several definitions around; details depend on the version of libc): /* Values for ut_type field, below */<br />
#define EMPTY 0         /* Record does not contain valid info \<br />
                           (formerly known as UT_UNKNOWN on Linux) */<br />
#define RUN_LVL 1       /* Change in system run-level (see \<br />
                           init(1)) */<br />
#define BOOT_TIME 2     /* Time of system boot (in ut_tv) */<br />
#define NEW_TIME 3      /* Time after system clock change \<br />
                           (in ut_tv) */<br />
#define OLD_TIME 4      /* Time before system clock change \<br />
                           (in ut_tv) */<br />
#define INIT_PROCESS 5  /* Process spawned by init(1) */<br />
#define LOGIN_PROCESS 6 /* Session leader process for user login */<br />
#define USER_PROCESS 7  /* Normal process */<br />
#define DEAD_PROCESS 8  /* Terminated process */<br />
#define ACCOUNTING 9    /* Not implemented */<br />
#define UT_LINESIZE 32<br />
#define UT_NAMESIZE 32<br />
#define UT_HOSTSIZE 256<br />
struct exit_status {     /* Type for ut_exit, below */<br />
    short e_termination; /* Process termination status */<br />
    short e_exit;        /* Process exit status */<br />
};<br />
struct utmp {<br />
    short ut_type;              /* Type of record */<br />
    pid_t ut_pid;               /* PID of login process */<br />
    char ut_line[UT_LINESIZE];  /* Device name of tty &#8211; &quot;/dev/&quot; */<br />
    char ut_id[4];              /* Terminal name suffix,<br />
                                   or inittab(5) ID */<br />
    char ut_user[UT_NAMESIZE];  /* Username */<br />
    char ut_host[UT_HOSTSIZE];  /* Hostname for remote login, or<br />
                                   kernel version for run-level<br />
                                   messages */<br />
    struct exit_status ut_exit; /* Exit status of a process<br />
                                   marked as DEAD_PROCESS; not<br />
                                   used by Linux init(1) */<br />
    /* The ut_session and ut_tv fields must be the same size when<br />
       compiled 32- and 64-bit.  This allows data files and shared<br />
       memory to be shared between 32- and 64-bit applications. */<br />
#if __WORDSIZE == 64 &amp;&amp; defined __WORDSIZE_COMPAT32<br />
    int32_t ut_session; /* Session ID (getsid(2)),<br />
                           used for windowing */<br />
    struct {<br />
        int32_t tv_sec;  /* Seconds */<br />
        int32_t tv_usec; /* Microseconds */<br />
    } ut_tv;             /* Time entry was made */<br />
#else<br />
    long ut_session;      /* Session ID */<br />
    struct timeval ut_tv; /* Time entry was made */<br />
#endif<br />
    int32_t ut_addr_v6[4]; /* Internet address of remote<br />
                                  host; IPv4 address uses<br />
                                  just ut_addr_v6[0] */<br />
    char __unused[20];     /* Reserved for future use */<br />
};<br />
/* Backward compatibility hacks */<br />
#define ut_name ut_user<br />
#ifndef _NO_UT_TIME<br />
#define ut_time ut_tv.tv_sec<br />
#endif<br />
#define ut_xtime ut_tv.tv_sec<br />
#define ut_addr ut_addr_v6[0] This structure gives the name of the special file associated with the user&#8217;s terminal, the user&#8217;s login name, and the time of login in the form of <code><a href="/docs/linux/man/2-time/">time</a></code>(2). String fields are terminated by a null byte (&#8216;
