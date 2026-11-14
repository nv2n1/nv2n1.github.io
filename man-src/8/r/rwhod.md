---
title: "rwhod(8)"
name: "rwhod"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rwhod/"
description: "rwhod – system status server"
---

<p><code>rwhod</code> &#8211; system status server</p>
<h2>Synopsis</h2>
<p><code>rwhod</code> [-<code>bpa</code> ] [-<code>u </code><i>user</i> ]</p>
<h2>Description</h2>
<p><code>Rwhod</code> is the server which maintains the database used by the <a href="/docs/linux/man/1-rwho/">rwho</a>(1) and <a href="/docs/linux/man/1-ruptime/">ruptime</a>(1) programs. Its operation is predicated on the ability to <i>broadcast</i> messages on a network. </p>
<p> <code>Rwhod</code> operates as both a producer and consumer of status information. As a producer of information it periodically queries the state of the system and constructs status messages which are broadcast on a network. As a consumer of information, it listens for other <code>rwhod</code> servers&#8217; status messages, validating them, then recording them in a collection of files located in the directory /var/spool/rwho </p>
<p> The server transmits and receives messages at the port indicated in the &#8220;rwho&#8221; service specification; see <a href="/docs/linux/man/5-services/">services</a>(5). </p>
<p> If the &#8211;<code>b</code> flag is supplied, only broadcast interfaces, such as ethernets, will be used. If the &#8211;<code>p</code> flag is supplied, only point-to-point interfaces will be used. If the &#8211;<code>a</code> flag is supplied, or no flags are supplied, all interfaces will be used. </p>
<p> If the &#8211;<code>u</code> flag is supplied, rwhod will run as the specified user instead of as root. </p>
<p> The messages sent and received, are of the form: </p>
<blockquote>
<pre>struct outmp {
 char out_line[8]; /* tty name */
 char out_name[8]; /* user id */
 long out_time; /* time on */
};
struct whod {
 char wd_vers;
 char wd_type;
 char wd_fill[2];
 int wd_sendtime;
 int wd_recvtime;
 char wd_hostname[32];
 int wd_loadav[3];
 int wd_boottime;
 struct whoent {
 struct outmp we_utmp;
 int we_idle;
 } wd_we[1024 / sizeof (struct whoent)];
};</pre>
</blockquote>
<p> All fields are converted to network byte order prior to transmission. The load averages are as calculated by the <a href="/docs/linux/man/1-w/">w</a>(1) program, and represent load averages over the 5, 10, and 15 minute intervals prior to a server&#8217;s transmission; they are multiplied by 100 for representation in an integer. The host name included is that returned by the <a href="/docs/linux/man/2-gethostname/">gethostname</a>(2) system call, with any trailing domain name omitted. The array at the end of the message contains information about the users logged in to the sending machine. This information includes the contents of the <a href="/docs/linux/man/5-utmp/">utmp</a>(5) entry for each non-idle terminal line and a value indicating the time in seconds since a character was last received on the terminal line. </p>
<p> Messages received by the rwho server are discarded unless they originated at an rwho server&#8217;s port. In addition, if the host&#8217;s name, as specified in the message, contains any unprintable <code>ASCII</code> characters, the message is discarded. Valid messages received by <code>rwhod</code> are placed in files named whod.hostname in the directory /var/spool/rwho These files contain only the most recent message, in the format described above. </p>
<p> Status messages are generated approximately once every 3 minutes. <code>Rwhod</code> recomputes the system boot time every 30 minutes because on some (non-Linux) systems it is not a totally reliable process.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-rwho/">rwho</a>(1), <a href="/docs/linux/man/1-ruptime/">ruptime</a>(1)</p>
<h2>Bugs</h2>
<p>There should be a way to relay status information between networks. People often interpret the server dying or network communtication failures as a machine going down.</p>
<h2>History</h2>
<p>The <code>rwhod</code> command appeared in BSD 4.2</p>
