---
title: "rtime(3)"
name: "rtime"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rtime/"
description: "rtime – get time from a remote machine"
---

<p>rtime &#8211; get time from a remote machine</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;rpc/auth_des.h&gt;

int rtime(struct sockaddr_in *addrp, struct rpc_timeval *timep,
          struct rpc_timeval *timeout);</code></pre>
<h2>Description</h2>
<p>This function uses the Time Server Protocol as described in RFC 868 to obtain the time from a remote machine. </p>
<p> The Time Server Protocol gives the time in seconds since 00:00:00 UTC, 1 Jan 1900, and this function subtracts the appropriate constant in order to convert the result to seconds since the Epoch, 1970-01-01 00:00:00 +0000 (UTC). </p>
<p> When <i>timeout</i> is non-NULL, the udp/time socket (port 37) is used. Otherwise, the tcp/time socket (port 37) is used.</p>
<h2>Return Value</h2>
<p>On success, 0 is returned, and the obtained 32-bit time value is stored in <i>timep-&gt;tv_sec</i>. In case of error -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>Errors</h2>
<p>All errors for underlying functions (<code><a href="/docs/linux/man/2-sendto/">sendto</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="/docs/linux/man/2-recvfrom/">recvfrom</a></code>(2), <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2)) can occur. Moreover:</p>
<dl>
<dt><code>EIO</code></p>
<dd>The number of returned bytes is not 4.</p>
<dt><code>ETIMEDOUT</code></p>
<dd>The waiting time as defined in timeout has expired.</dl>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>rtime</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Notes</h2>
<p>Only IPv4 is supported. </p>
<p> Some <i>in.timed</i> versions support only TCP. Try the example program with <i>use_tcp</i> set to 1.</p>
<h2>Bugs</h2>
<p><code>rtime</code>() in glibc 2.2.5 and earlier does not work properly on 64-bit machines.</p>
<h2>Examples</h2>
<p>This example requires that port 37 is up and open. You may check that the time entry within <i>/etc/inetd.conf</i> is not commented out. The program connects to a computer called &quot;linux&quot;. Using &quot;localhost&quot; does not work. The result is the localtime of the computer &quot;linux&quot;. </p>
<pre><code>#include &lt;errno.h&gt;
#include &lt;netdb.h&gt;
#include &lt;rpc/auth_des.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;time.h&gt;
static int use_tcp = 0;
static char *servername = &quot;linux&quot;;
int main(void)
{
    struct sockaddr_in name;
    struct rpc_timeval time1 = {0, 0};
    struct rpc_timeval timeout = {1, 0};
    struct hostent *hent;
    int ret;
    memset(&amp;name, 0, sizeof(name));
    sethostent(1);
    hent = gethostbyname(servername);
    memcpy(&amp;name.sin_addr, hent-&gt;h_addr, hent-&gt;h_length);
    ret = rtime(&amp;name, &amp;time1, use_tcp ? NULL : &amp;timeout);
    if (ret &lt; 0)
        perror(&quot;rtime error&quot;);
    else {
        time_t t = time1.tv_sec;
        printf(&quot;%s
&quot;, ctime(&amp;t));
    }
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ntpdate/">ntpdate</a></code>(1), <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
