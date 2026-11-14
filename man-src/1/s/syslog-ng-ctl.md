---
title: "syslog-ng-ctl(1)"
name: "syslog-ng-ctl"
section: "1"
letter: "s"
url: "/docs/linux/man/1-syslog-ng-ctl/"
description: "syslog-ng-ctl – Display message statistics and enable verbose, debug and trace modes in syslog-ng Open Source Edition"
---

<h2 class="name">NAME</h2>
<p> syslog-ng-ctl &#8211; Display message statistics and enable verbose, debug and trace modes in syslog-ng Open Source Edition </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>syslog-ng-ctl</code> [command] [options]</dl>
<h2>DESCRIPTION</h2>
<dd>NOTE: The syslog-ng-ctl application is distributed with the syslog-ng Open Source Edition system logging application, and is usually part of the syslog-ng package. The latest version of the syslog-ng application is available at m[blue]<code>the official syslog-ng website</code>m[]<font SIZE="-2">[1]</font>. </p>
<p> This manual page is only an abstract; for the complete documentation of syslog-ng, see m[blue]<code>The syslog-ng Open Source Edition Administrator Guide</code>m[]<font SIZE="-2">[2]</font>. </p>
<p> The <code>syslog-ng-ctl</code> application is a utility that can be used to: </p>
<dl>
<dt>
<dd> &bull; enable/disable various syslog-ng messages for troubleshooting;</dl>
<dl>
<dt>
<dd> &bull; display statistics about the processed messages.</dl>
<h2>ENABLING TROUBLESHOOTING MESSAGES</h2>
<dl>
<dt> <code>command</code> [options]</dl>
<dd>Use the <code>syslog-ng-ctl &lt;command&gt; &#8211;set=on</code> command to display verbose, trace, or debug messages. If you are trying to solve configuration problems, the debug (and occassionally trace) messages are usually sufficient; debug messages are needed mostly for finding software errors. After solving the problem, do not forget to turn these messages off using the <code>syslog-ng-ctl &lt;command&gt; &#8211;set=off</code>. Note that enabling debug messages does not enable verbose and trace messages. </p>
<p> Use <code>syslog-ng-ctl &lt;command&gt;</code> without any parameters to display whether the particular type of messages are enabled or not. </p>
<p> If you need to use a non-standard control socket to access syslog-ng, use the <code>syslog-ng-ctl &lt;command&gt; &#8211;set=on &#8211;control=&lt;socket&gt;</code> command to specify the socket to use. </p>
<p> <code>verbose</code></p>
<dl>
<dt>
<dd> Print verbose messages. If syslog-ng was started with the <i>&#8211;stderr</i> or <i>-e</i> option, the messages will be sent to stderr. If not specified, syslog-ng will log such messages to its internal source.</dl>
<p> <code>trace</code></p>
<dl>
<dt>
<dd> Print trace messages of how messages are processed. If syslog-ng was started with the <i>&#8211;stderr</i> or <i>-e</i> option, the messages will be sent to stderr. If not specified, syslog-ng will log such messages to its internal source.</dl>
<p> <code>debug</code></p>
<dl>
<dt>
<dd> Print debug messages. If syslog-ng was started with the <i>&#8211;stderr</i> or <i>-e</i> option, the messages will be sent to stderr. If not specified, syslog-ng will log such messages to its internal source.</dl>
<p> Example: </p>
<dl>
<dt>
<dd>
<pre>
syslog-ng-ctl verbose --set=on
</pre>
</dl>
<h2>THE STATS COMMAND</h2>
<dl>
<dt> <code>stats</code> [options]</dl>
<dd>Use the <code>stats</code> command to display statistics about the processed messages. The <code>stats</code> command has the following options: </p>
<p> <code>&#8211;control=&lt;socket&gt;</code> or <code>-c</code></p>
<dl>
<dt>
<dd> Specify the socket to use to access syslog-ng. Only needed when using a non-standard socket.</dl>
<p> Example: </p>
<dl>
<dt>
<dd>
<pre>
syslog-ng-ctl stats
</pre>
</dl>
<p> An example output: </p>
<dl>
<dt>
<dd>
<pre><code>
src.internal;
s_all #0;
;
a;
processed;
6445 src.internal;
s_all #0;
;
a;
stamp;
1268989330 destination;
df_auth;
;
a;
processed;
404 destination;
df_news_dot_notice;
;
a;
processed;
0 destination;
df_news_dot_err;
;
a;
processed;
0 destination;
d_ssb;
;
a;
processed;
7128 destination;
df_uucp;
;
a;
processed;
0 source;
s_all;
;
a;
processed;
7128 destination;
df_mail;
;
a;
processed;
0 destination;
df_user;
;
a;
processed;
1 destination;
df_daemon;
;
a;
processed;
1 destination;
df_debug;
;
a;
processed;
15 destination;
df_messages;
;
a;
processed;
54 destination;
dp_xconsole;
;
a;
processed;
671 dst.tcp;
d_network #0;
10.50.0.111 : 514;
a;
dropped;
5080 dst.tcp;
d_network #0;
10.50.0.111 : 514;
a;
processed;
7128 dst.tcp;
d_network #0;
10.50.0.111 : 514;
a;
stored;
2048 destination;
df_syslog;
;
a;
processed;
6724 destination;
df_facility_dot_warn;
;
a;
processed;
0 destination;
df_news_dot_crit;
;
a;
processed;
0 destination;
df_lpr;
;
a;
processed;
0 destination;
du_all;
;
a;
processed;
0 destination;
df_facility_dot_info;
;
a;
processed;
0 center;
;
received;
a;
processed;
0 destination;
df_kern;
;
a;
processed;
70 center;
;
queued;
a;
processed;
0 destination;
df_facility_dot_err;
;
a;
processed;
0
</code></pre>
</dl>
<h2>FILES</h2>
<p> /home/algernon/install/syslog-ng/3.5/sbin/syslog-ng-ctl</p>
<h2>SEE ALSO</h2>
<p> m[blue]<code>The syslog-ng Administrator Guide</code>m[]<font SIZE="-2">[2]</font> </p>
<p> <code><a href="/docs/linux/man/5-syslog-ng-conf/">syslog-ng.conf</a></code>(5) </p>
<p> <code><a href="/docs/linux/man/8-syslog-ng/">syslog-ng</a></code>(8) </p>
<p> m[blue]<code>The syslog-ng OSE 3.3 Administrator Guide</code>m[]<font SIZE="-2">[2]</font> </p>
<p> If you experience any problems or need help with syslog-ng, visit m[blue]<code>visit the syslog-ng wiki</code>m[]<font SIZE="-2">[3]</font> or the m[blue]<code>syslog-ng mailing list</code>m[]<font SIZE="-2">[4]</font>. </p>
<p> For news and notifications about of syslog-ng, visit the m[blue]<code>syslog-ng Insider Blog</code>m[]<font SIZE="-2">[5]</font>.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by the BalaBit Documentation Team &lt;documentation [at] balabit.com&gt;.</p>
<h2>COPYRIGHT</h2>
<h3></h3>
<p> The authors grant permission to copy, distribute and/or modify this manual page under the terms of the GNU General Public License Version 2 or newer (GPL v2+).</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> the official syslog-ng website</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.balabit.com/network-security/syslog-ng/">http://www.balabit.com/network-security/syslog-ng/</a></dl>
<dt> 2.</p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>The syslog-ng Open Source Edition Administrator Guide</code><br />
&nbsp;<wbr>&nbsp;<wbr></p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.balabit.com/support/documentation/">http://www.balabit.com/support/documentation/</a></dl>
<dt> 3.</p>
<dd> visit the syslog-ng wiki</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.balabit.com/wiki/syslog-ng-faq">http://www.balabit.com/wiki/syslog-ng-faq</a></dl>
<dt> 4.</p>
<dd> <code>syslog-ng mailing list</code></p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://lists.balabit.hu/mailman/listinfo/syslog-ng">https://lists.balabit.hu/mailman/listinfo/syslog-ng</a></dl>
<dt> 5.</p>
<dd> <code>syslog-ng Insider Blog</code></p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://insider.blogs.balabit.com">http://insider.blogs.balabit.com</a></dl>
</dl>
<h2>Index</h2>
<dt><a href="#lbAL">NOTES</a></p>
<dd></dl>
