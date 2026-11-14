---
title: "inndcomm(3)"
name: "inndcomm"
section: "3"
letter: "i"
url: "/docs/linux/man/3-inndcomm/"
---

<h2>NAME</h2>

 inndcomm - INND communication part of InterNetNews library

<h2>SYNOPSIS</h2>

 <pre><code>
#include "inn/inndcomm.h"
int ICCopen() int ICCclose() void ICCsettimeout(i) int i;
int ICCcommand(cmd, argv, replyp)
char cmd;
char *argv[];
char **replyp;
int ICCcancel(mesgid)
char *mesgid;
int ICCreserve(why)
char *why;
int ICCpause(why)
char *why;
int ICCgo(why)
char *why;
extern char *ICCfailure;
</code></pre>

<h2>DESCRIPTION</h2>

 The routines described in this manual page are part of the InterNetNews library, <i><a HREF="/docs/linux/man/3-libinn/">libinn</a></i>(3). They are used to send commands to a running <i><a HREF="/docs/linux/man/8-innd/">innd</a></i>(8) daemon on the local host. The letters ``ICC'' stand for <i>I</i>nnd <i>C</i>ontrol <i>C</i>ommand. 

 <i>ICCopen</i> creates a Unix-domain datagram socket and binds it to the server's control socket, if <i>&lt;HAVE_UNIX_DOMAIN_SOCKETS in include/config.h&gt;</i> is defined. Otherwise it creates a named pipe for communicating with the server. It returns -1 on failure or zero on success. This routine must be called before any other routine. 

 <i>ICCclose</i> closes any descriptors that have been created by <i>ICCopen</i>. It returns -1 on failure or zero on success. 

 <i>ICCsettimeout</i> can be called before any of the following routines to determine how long the library should wait before giving up on getting the server's reply. This is done by setting and catching a SIGALRM <i><a HREF="/docs/linux/man/2-signal/">signal</a></i>(2). If the timeout is less then zero then no reply will be waited for. The SC_SHUTDOWN, SC_XABORT, and SC_XEXEC commands do not get a reply either. The default, which can be obtained by setting the timeout to zero, is to wait until the server replies. 

 <i>ICCcommand</i> sends the command <i>cmd</i> with parameters <i>argv</i> to the server. It returns -1 on error. If the server replies, and <i>replyp</i> is not NULL, it will be filled in with an allocated buffer that contains the full text of the server's reply. This buffer is a string in the form of ``&lt;digits&gt;&lt;space&gt;&lt;text&gt;'' where ``digits'' is the text value of the recommended exit code; zero indicates success. Replies longer then 4000 bytes will be truncated. The possible values of <i>cmd</i> are defined in the ``inn/inndcomm.h'' header file. The parameters for each command are described in <i><a HREF="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8). This routine returns -1 on communication failure, or the exit status sent by the server which will never be negative. 

 <i>ICCcancel</i> sends a ``cancel'' message to the server. <i>Mesgid</i> is the Message-ID of the article that should be cancelled. The return value is the same as for <i>ICCcommand</i>. 

 <i>ICCpause</i>, <i>ICCreserve</i>, and <i>ICCgo</i> send a ``pause,'' ``reserve,'' or ``go'' command to the server, respectively. If <i>ICCreserve</i> is used, then the <i>why</i> value used in the <i>ICCpause</i> invocation must match; the value used in the <i>ICCgo</i> invocation must always match that the one used in the <i>ICCpause</i> invocation. The return value for all three routines is the same as for <i>ICCcommand</i>. 

 If any routine described above fails, the <i>ICCfailure</i> variable will identify the system call that failed.

<h2>HISTORY</h2>

 Written by Rich $alz &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. This is revision 7901, dated 2008-06-22.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/8-ctlinnd/">ctlinnd</a>(8), <a HREF="/docs/linux/man/8-innd/">innd</a>(8), <a HREF="/docs/linux/man/3-libinn/">libinn</a>(3). 

<h2>Index</h2>


