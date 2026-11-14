---
title: "rc(8)"
name: "rc"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rc/"
description: "rc.news – Start or stop INN daemons"
---

<p>rc.news &#8211; Start or stop INN daemons</p>
<h2>Synopsis</h2>
<p><code>rc.news</code> [start | stop]</p>
<h2>Description</h2>
<p><code>rc.news</code> can be used to start or stop <code>innd</code> and supporting programs. It checks to make sure <font SIZE="-1">INN</font> is not already running, handles cases of unclean shutdown, finishes up tasks which might have been interrupted by the preceeding shutdown, e-mails certain boot-time warnings to <i>newsmaster</i> (as set in <i>inn.conf</i>), and is generally safer and easier than starting and stopping everything directly. It needs to be run as the news user so that files in <i>pathrun</i> are created with the right ownership (though this is less important for <tt>&quot;rc.news stop&quot;</tt>). </p>
<p> Programs run and stopped by this script include:</p>
<dl>
<dt>*</p>
<dd>Always: <code>innd</code> is started or stopped.</p>
<dt>*</p>
<dd>If <i>doinnwatch</i> is true in <i>inn.conf</i>: <code>innwatch</code> is started and stopped.</p>
<dt>*</p>
<dd>If <i>docnfsstat</i> is true in <i>inn.conf</i>: <code>ovdb_init</code> is run; <code>ovdb_server</code> and <code>ovdb_monitor</code> are stopped.</p>
<dt>*</p>
<dd>If <i>rc.news.local</i> exists in <i>pathbin</i>: <code>rc.news.local</code> is run with argument <tt>&quot;start&quot;</tt> or <tt>&quot;stop&quot;</tt> (to perform site-specific startup or shutdown tasks).</dl>
<h2>Options</h2>
<dl>
<dt>start</p>
<dd>If the first argument is <tt>&quot;start&quot;</tt>, or no first argument is given, <code>rc.news</code> initiates <font SIZE="-1">INN</font> startup.</p>
<dt>stop</p>
<dd>If the first argument is <tt>&quot;stop&quot;</tt>, <code>rc.news</code> initiates <font SIZE="-1">INN</font> shutdown. It is recommended to throttle the server first as described in <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8).</dl>
<h2>Examples</h2>
<p>To start <font SIZE="-1">INN</font> and leave certain error messages going to the terminal: </p>
<pre> su -m news -c /etc/rc.news</pre>
<p>To run <font SIZE="-1">INN</font> at startup time from appropriate system boot scripts: </p>
<pre> su -m news -c /etc/rc.news &gt;/dev/console</pre>
<p>To stop <font SIZE="-1">INN</font> (throttling first): </p>
<pre> &lt;pathbin&gt;/ctlinnd throttle reason
 su -m news -c '/etc/rc.news stop'</pre>
<h2>Bugs</h2>
<p>Running <tt>&quot;rc.news start&quot;</tt> as root is never the right thing to do, so we should at minimum check for this and error, or perhaps change effective user <font SIZE="-1">ID</font>.</p>
<h2>History</h2>
<p>// <font SIZE="-1">FIXME:</font> any attribution for <i>rc.news</i> itself? </p>
<p> This manual page written by Jeffrey M. Vinocur &lt;jeff [at] litech.org&gt; for InterNetNews. </p>
<p> $Id: rc.news.pod 8200 2008-11-30 13:31:30Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8), <i><a href="/docs/linux/man/8-cnfsstat/">cnfsstat</a></i>(8), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-innwatch/">innwatch</a></i>(8), <i><a href="/docs/linux/man/5-ovdb/">ovdb</a></i>(5). </p>
