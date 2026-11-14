---
title: "pidfile(3)"
name: "pidfile"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pidfile/"
description: "pidfile_open pidfile_write pidfile_close pidfile_remove – library for PID files handling"
---

<p><code>pidfile_open</code> <code>pidfile_write</code> <code>pidfile_close</code> <code>pidfile_remove</code> &#8211; library for PID files handling</p>
<h2>Library</h2>
<p>Lb libbsd</p>
<h2>Synopsis</h2>
<p>In bsd/libutil.h Ft struct pidfh * Fn pidfile_open const char *path mode_t mode pid_t *pidptr Ft int Fn pidfile_write struct pidfh *pfh Ft int Fn pidfile_close struct pidfh *pfh Ft int Fn pidfile_remove struct pidfh *pfh</p>
<h2>Description</h2>
<p>The <code>pidfile</code> family of functions allows daemons to handle PID files. It uses <a href="/docs/linux/man/3-flopen/">flopen</a>(3) to lock a pidfile and detect already running daemons. </p>
<p> The Fn pidfile_open function opens (or creates) a file specified by the Fa path argument and locks it. If a file can not be locked, a PID of an already running daemon is returned in the Fa pidptr argument (if it is not <code>NULL )</code> The function does not write process&#8217; PID into the file here, so it can be used before Fn fork Ns ing and exit with a proper error message when needed. If the Fa path argument is <code>NULL</code> /var/run/ <code>Ao </code><i>progname Ac </i><code>.pid </code> file will be used. </p>
<p> The Fn pidfile_write function writes process&#8217; PID into a previously opened file. </p>
<p> The Fn pidfile_close function closes a pidfile. It should be used after daemon Fn fork Ns s to start a child process. </p>
<p> The Fn pidfile_remove function closes and removes a pidfile.</p>
<h2>Return Values</h2>
<p>The Fn pidfile_open function returns a valid pointer to a Vt pidfh structure on success, or <code>NULL</code> if an error occurs. If an error occurs, <i>errno</i> will be set. </p>
<p> Rv -std pidfile_write pidfile_close pidfile_remove</p>
<h2>Examples</h2>
<p>The following example shows in which order these functions should be used. Note that it is safe to pass <code>NULL</code> to Fn pidfile_write , Fn pidfile_remove and Fn pidfile_close functions. </p>
<pre>struct pidfh *pfh;
pid_t otherpid, childpid;
pfh = pidfile_open(&quot;/var/run/daemon.pid&quot;, 0600, &amp;otherpid);
if (pfh == NULL) {
 if (errno == EEXIST) {
 errx(EXIT_FAILURE, &quot;Daemon already running, pid: %jd.&quot;,
 (intmax_t)otherpid);
 }
 /* If we cannot create pidfile from other reasons, only warn. */
 warn(&quot;Cannot open or create pidfile&quot;);
}
if (daemon(0, 0) == -1) {
 warn(&quot;Cannot daemonize&quot;);
 pidfile_remove(pfh);
 exit(EXIT_FAILURE);
}
pidfile_write(pfh);
for (;;) {
 /* Do work. */
 childpid = fork();
 switch (childpid) {
 case -1:
 syslog(LOG_ERR, &quot;Cannot fork(): %s.&quot;, strerror(errno));
 break;
 case 0:
 pidfile_close(pfh);
 /* Do child work. */
 break;
 default:
 syslog(LOG_INFO, &quot;Child %jd started.&quot;, (intmax_t)childpid);
 break;
 }
}
pidfile_remove(pfh);
exit(EXIT_SUCCESS);</pre>
<h2>Errors</h2>
<p>The Fn pidfile_open function will fail if:</p>
<dl>
<dt><code>Bq </code>Er EEXIST</p>
<dd>Some process already holds the lock on the given pidfile, meaning that a daemon is already running.</p>
<dt><code>Bq </code>Er ENAMETOOLONG</p>
<dd>Specified pidfile&#8217;s name is too long.</p>
<dt><code>Bq </code>Er EINVAL</p>
<dd>Some process already holds the lock on the given pidfile, but PID read from there is invalid.</p>
<dt><code>Bq </code>Er EAGAIN</p>
<dd>Some process already holds the lock on the given pidfile, but the file is truncated. Most likely, the existing daemon is writing new PID into the file.</dl>
<p> The Fn pidfile_open function may also fail and set <i>errno</i> for any errors specified for the <a href="/docs/linux/man/2-fstat/">fstat</a>(2), <a href="/docs/linux/man/2-open/">open</a>(2), and <a href="/docs/linux/man/2-read/">read</a>(2) calls. </p>
<p> The Fn pidfile_write function will fail if:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd>Improper function use. Probably called before Fn pidfile_open .</dl>
<p> The Fn pidfile_write function may also fail and set <i>errno</i> for any errors specified for the <a href="/docs/linux/man/2-fstat/">fstat</a>(2), <a href="/docs/linux/man/2-ftruncate/">ftruncate</a>(2), and <a href="/docs/linux/man/2-write/">write</a>(2) calls. </p>
<p> The Fn pidfile_close function may fail and set <i>errno</i> for any errors specified for the <a href="/docs/linux/man/2-close/">close</a>(2) and <a href="/docs/linux/man/2-fstat/">fstat</a>(2) calls. </p>
<p> The Fn pidfile_remove function will fail if:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd>Improper function use. Probably called not from the process which made Fn pidfile_write .</dl>
<p> The Fn pidfile_remove function may also fail and set <i>errno</i> for any errors specified for the <a href="/docs/linux/man/2-close/">close</a>(2), <a href="/docs/linux/man/2-fstat/">fstat</a>(2), <a href="/docs/linux/man/2-write/">write</a>(2), and <a href="/docs/linux/man/2-unlink/">unlink</a>(2) system calls and the <a href="/docs/linux/man/3-flopen/">flopen</a>(3) library function.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/2-open/">open</a>(2), <a href="/docs/linux/man/3-daemon/">daemon</a>(3), <a href="/docs/linux/man/3-flopen/">flopen</a>(3)</p>
<h2>Authors</h2>
<p>An -nosplit The <code>pidfile</code> functionality is based on ideas from An John-Mark Gurney Aq jmg [at] FreeBSD.org . </p>
<p> The code and manual page was written by An Pawel Jakub Dawidek Aq pjd [at] FreeBSD.org .</p>
