---
title: "signal-safety(7)"
name: "signal-safety"
section: "7"
letter: "s"
url: "/docs/linux/man/7-signal-safety/"
description: "signal-safety – async-signal-safe functions"
---

<p>signal-safety &#8211; async-signal-safe functions</p>
<h2>Description</h2>
<p>An <i>async-signal-safe</i> function is one that can be safely called from within a signal handler. Many functions are <i>not</i> async-signal-safe. In particular, nonreentrant functions are generally unsafe to call from a signal handler. </p>
<p> The kinds of issues that render a function unsafe can be quickly understood when one considers the implementation of the <i>stdio</i> library, all of whose functions are not async-signal-safe. </p>
<p> When performing buffered I/O on a file, the <i>stdio</i> functions must maintain a statically allocated data buffer along with associated counters and indexes (or pointers) that record the amount of data and the current position in the buffer. Suppose that the main program is in the middle of a call to a <i>stdio</i> function such as <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) where the buffer and associated variables have been partially updated. If, at that moment, the program is interrupted by a signal handler that also calls <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3), then the second call to <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) will operate on inconsistent data, with unpredictable results. </p>
<p> To avoid problems with unsafe functions, there are two possible choices:</p>
<dl>
<dt>1.</p>
<dd>Ensure that (a) the signal handler calls only async-signal-safe functions, and (b) the signal handler itself is reentrant with respect to global variables in the main program.</p>
<dt>2.</p>
<dd>Block signal delivery in the main program when calling functions that are unsafe or operating on global data that is also accessed by the signal handler.</dl>
<p> Generally, the second choice is difficult in programs of any complexity, so the first choice is taken. </p>
<p> POSIX.1 specifies a set of functions that an implementation must make async-signal-safe. (An implementation may provide safe implementations of additional functions, but this is not required by the standard and other implementations may not provide the same guarantees.) </p>
<p> In general, a function is async-signal-safe either because it is reentrant or because it is atomic with respect to signals (i.e., its execution can&#8217;t be interrupted by a signal handler). </p>
<p> The set of functions required to be async-signal-safe by POSIX.1 is shown in the following table. The functions not otherwise noted were required to be async-signal-safe in POSIX.1-2001; the table details changes in the subsequent standards. </p>
<table>
<tr VALIGN=top>
<td><code>Function</code></td>
<td><code>Notes</code>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-abort/">abort</a></code>(3)</td>
<td>Added in POSIX.1-2001 TC1
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-accept/">accept</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-access/">access</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-aio_error/">aio_error</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-aio_return/">aio_return</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-aio_suspend/">aio_suspend</a></code>(3)</td>
<td>See notes below
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-alarm/">alarm</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-bind/">bind</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-cfgetispeed/">cfgetispeed</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-cfgetospeed/">cfgetospeed</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-cfsetispeed/">cfsetispeed</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-cfsetospeed/">cfsetospeed</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-chdir/">chdir</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-chown/">chown</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-close/">close</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-connect/">connect</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-creat/">creat</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-dup/">dup</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-dup2/">dup2</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-execl/">execl</a></code>(3)</td>
<td>Added in POSIX.1-2008; see notes below
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-execle/">execle</a></code>(3)</td>
<td>See notes below
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-execv/">execv</a></code>(3)</td>
<td>Added in POSIX.1-2008
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-execve/">execve</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-_exit/">_Exit</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-faccessat/">faccessat</a></code>(2)</td>
<td>Added in POSIX.1-2008
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fchdir/">fchdir</a></code>(2)</td>
<td>Added in POSIX.1-2008 TC1
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fchmod/">fchmod</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fchmodat/">fchmodat</a></code>(2)</td>
<td>Added in POSIX.1-2008
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fchown/">fchown</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fchownat/">fchownat</a></code>(2)</td>
<td>Added in POSIX.1-2008
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fdatasync/">fdatasync</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-fexecve/">fexecve</a></code>(3)</td>
<td>Added in POSIX.1-2008
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-ffs/">ffs</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fork/">fork</a></code>(2)</td>
<td>See notes below
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fstat/">fstat</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fstatat/">fstatat</a></code>(2)</td>
<td>Added in POSIX.1-2008
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-ftruncate/">ftruncate</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-futimens/">futimens</a></code>(3)</td>
<td>Added in POSIX.1-2008
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getegid/">getegid</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-geteuid/">geteuid</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getgid/">getgid</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getgroups/">getgroups</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getpeername/">getpeername</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getpgrp/">getpgrp</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getppid/">getppid</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getsockname/">getsockname</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-getuid/">getuid</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-htonl/">htonl</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-htons/">htons</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-kill/">kill</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-link/">link</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-linkat/">linkat</a></code>(2)</td>
<td>Added in POSIX.1-2008
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-listen/">listen</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-longjmp/">longjmp</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2; see notes below
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-lstat/">lstat</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-memccpy/">memccpy</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-memchr/">memchr</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-memcmp/">memcmp</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-memcpy/">memcpy</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-memmove/">memmove</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-memset/">memset</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-mkdirat/">mkdirat</a></code>(2)</td>
<td>Added in POSIX.1-2008
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-mkfifo/">mkfifo</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-mkfifoat/">mkfifoat</a></code>(3)</td>
<td>Added in POSIX.1-2008
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-mknod/">mknod</a></code>(2)</td>
<td>Added in POSIX.1-2008
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-mknodat/">mknodat</a></code>(2)</td>
<td>Added in POSIX.1-2008
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-ntohl/">ntohl</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-ntohs/">ntohs</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-open/">open</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-openat/">openat</a></code>(2)</td>
<td>Added in POSIX.1-2008
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-pause/">pause</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-poll/">poll</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-posix_trace_event/">posix_trace_event</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-pselect/">pselect</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-pthread_kill/">pthread_kill</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC1
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-pthread_self/">pthread_self</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC1
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-pthread_sigmask/">pthread_sigmask</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC1
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-raise/">raise</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-read/">read</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-readlinkat/">readlinkat</a></code>(2)</td>
<td>Added in POSIX.1-2008
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-recv/">recv</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-recvfrom/">recvfrom</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-rename/">rename</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-renameat/">renameat</a></code>(2)</td>
<td>Added in POSIX.1-2008
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-rmdir/">rmdir</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-select/">select</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-sem_post/">sem_post</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-send/">send</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sendto/">sendto</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setgid/">setgid</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setpgid/">setpgid</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setsid/">setsid</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-setuid/">setuid</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-shutdown/">shutdown</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-sigaddset/">sigaddset</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-sigdelset/">sigdelset</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-sigemptyset/">sigemptyset</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-sigfillset/">sigfillset</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-sigismember/">sigismember</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-siglongjmp/">siglongjmp</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2; see notes below
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-signal/">signal</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-sigpause/">sigpause</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sigpending/">sigpending</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sigqueue/">sigqueue</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-sigset/">sigset</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sigsuspend/">sigsuspend</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-sleep/">sleep</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-sockatmark/">sockatmark</a></code>(3)</td>
<td>Added in POSIX.1-2001 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-socket/">socket</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-socketpair/">socketpair</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-stat/">stat</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-stpcpy/">stpcpy</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-stpncpy/">stpncpy</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-strcat/">strcat</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-strchr/">strchr</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-strcmp/">strcmp</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-strcpy/">strcpy</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-strcspn/">strcspn</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-strlen/">strlen</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-strncat/">strncat</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-strncmp/">strncmp</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-strncpy/">strncpy</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-strnlen/">strnlen</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-strpbrk/">strpbrk</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-strrchr/">strrchr</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-strspn/">strspn</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-strstr/">strstr</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-strtok_r/">strtok_r</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-symlink/">symlink</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-symlinkat/">symlinkat</a></code>(2)</td>
<td>Added in POSIX.1-2008
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-tcdrain/">tcdrain</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-tcflow/">tcflow</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-tcflush/">tcflush</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-tcgetattr/">tcgetattr</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-tcgetpgrp/">tcgetpgrp</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-tcsendbreak/">tcsendbreak</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-tcsetattr/">tcsetattr</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-tcsetpgrp/">tcsetpgrp</a></code>(3)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-time/">time</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-timer_getoverrun/">timer_getoverrun</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-timer_gettime/">timer_gettime</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-timer_settime/">timer_settime</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-times/">times</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-umask/">umask</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-uname/">uname</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-unlink/">unlink</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-unlinkat/">unlinkat</a></code>(2)</td>
<td>Added in POSIX.1-2008
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-utime/">utime</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-utimensat/">utimensat</a></code>(2)</td>
<td>Added in POSIX.1-2008
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-utimes/">utimes</a></code>(2)</td>
<td>Added in POSIX.1-2008
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-wait/">wait</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-wcpcpy/">wcpcpy</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-wcpncpy/">wcpncpy</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-wcscat/">wcscat</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-wcschr/">wcschr</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-wcscmp/">wcscmp</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-wcscpy/">wcscpy</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-wcscspn/">wcscspn</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-wcslen/">wcslen</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-wcsncat/">wcsncat</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-wcsncmp/">wcsncmp</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-wcsncpy/">wcsncpy</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-wcsnlen/">wcsnlen</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-wcspbrk/">wcspbrk</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-wcsrchr/">wcsrchr</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-wcsspn/">wcsspn</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-wcsstr/">wcsstr</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-wcstok/">wcstok</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-wmemchr/">wmemchr</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-wmemcmp/">wmemcmp</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-wmemcpy/">wmemcpy</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-wmemmove/">wmemmove</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/3-wmemset/">wmemset</a></code>(3)</td>
<td>Added in POSIX.1-2008 TC2
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-write/">write</a></code>(2)</td>
<td>
</td>
</tr>
</table>
<p> Notes:</p>
<dl>
<dt>*</p>
<dd>POSIX.1-2001 and POSIX.1-2001 TC2 required the functions <code><a href="/docs/linux/man/3-fpathconf/">fpathconf</a></code>(3), <code><a href="/docs/linux/man/3-pathconf/">pathconf</a></code>(3), and <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3) to be async-signal-safe, but this requirement was removed in POSIX.1-2008.</p>
<dt>*</p>
<dd>If a signal handler interrupts the execution of an unsafe function, and the handler terminates via a call to <code><a href="/docs/linux/man/3-longjmp/">longjmp</a></code>(3) or <code><a href="/docs/linux/man/3-siglongjmp/">siglongjmp</a></code>(3) and the program subsequently calls an unsafe function, then the behavior of the program is undefined.</p>
<dt>*</p>
<dd>POSIX.1-2001 TC1 clarified that if an application calls <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) from a signal handler and any of the fork handlers registered by <code><a href="/docs/linux/man/3-pthread_atfork/">pthread_atfork</a></code>(3) calls a function that is not async-signal-safe, the behavior is undefined. A future revision of the standard is likely to remove <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) from the list of async-signal-safe functions.</p>
<dt>*</p>
<dd>Asynchronous signal handlers that call functions which are cancellation points and nest over regions of deferred cancellation may trigger cancellation whose behavior is as if asynchronous cancellation had occurred and may cause application state to become inconsistent.</dl>
<h3>errno</h3>
<p>Fetching and setting the value of <i>errno</i> is async-signal-safe provided that the signal handler saves <i>errno</i> on entry and restores its value before returning.</p>
<h3>Deviations in the GNU C library</h3>
<p>The following known deviations from the standard occur in the GNU C library:</p>
<dl>
<dt>*</p>
<dd>Before glibc 2.24, <code><a href="/docs/linux/man/3-execl/">execl</a></code>(3) and <code><a href="/docs/linux/man/3-execle/">execle</a></code>(3) employed <code><a href="/docs/linux/man/3-realloc/">realloc</a></code>(3) internally and were consequently not async-signal-safe. This was fixed in glibc 2.24.</p>
<dt>*</p>
<dd>The glibc implementation of <code><a href="/docs/linux/man/3-aio_suspend/">aio_suspend</a></code>(3) is not async-signal-safe because it uses <code><a href="/docs/linux/man/3-pthread_mutex_lock/">pthread_mutex_lock</a></code>(3) internally.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7), <code><a href="/docs/linux/man/7-standards/">standards</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
