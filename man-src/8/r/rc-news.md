---
title: "rc-news(8)"
name: "rc-news"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rc-news/"
description: "rc.news – Start or stop INN daemons"
---

<p>rc.news &#8211; Start or stop INN daemons</p>
<h2>Synopsis</h2>
<p><code>rc.news</code> [<tt>&quot;start&quot;</tt> | <tt>&quot;stop&quot;</tt>]</p>
<h2>Description</h2>
<p><code>rc.news</code> can be used to start or stop <code>innd</code> and supporting programs. It checks to make sure <font SIZE="-1">INN</font> is not already running, handles cases of unclean shutdown, finishes up tasks which might have been interrupted by the preceding shutdown, e-mails certain boot-time warnings to <i>newsmaster</i> (as set in <i>inn.conf</i>), and is generally safer and easier than starting and stopping everything directly. It needs to be run as the news user so that files in <i>pathrun</i> are created with the right ownership (though this is less important for <tt>&quot;rc.news stop&quot;</tt>). </p>
<p> Programs run and stopped by this script include:</p>
<dl>
<dt>&bull;</p>
<dd>Always: <code>innd</code> is started or stopped.</p>
<dt>&bull;</p>
<dd>If <i>doinnwatch</i> is true in <i>inn.conf</i>: <code>innwatch</code> is started and stopped.</p>
<dt>&bull;</p>
<dd>If <i>docnfsstat</i> is true in <i>inn.conf</i>: <code>cnfsstat</code> is started and stopped.</p>
<dt>&bull;</p>
<dd>If <i>ovmethod</i> is set to <tt>&quot;ovdb&quot;</tt> in <i>inn.conf</i>: <code>ovdb_init</code> is run; <code>ovdb_server</code> and <code>ovdb_monitor</code> are stopped.</p>
<dt>&bull;</p>
<dd>If <i>rc.news.local</i> exists in <i>pathbin</i>: <code>rc.news.local</code> is run with argument <tt>&quot;start&quot;</tt> or <tt>&quot;stop&quot;</tt> (to perform site-specific startup or shutdown tasks).</p>
<dt>&bull;</p>
<dd>When started, if <font SIZE="-1">INN</font> appears to have previously been shut down during its expiry process, run <code>expirerm</code> if there are articles to unlink.</p>
<dt>&bull;</p>
<dd>When started, if overview data appears to have just been rebuilt and <i>active</i> needs to be renumbered, then actually renumber it.</dl>
<h2>Options</h2>
<dl>
<dt>&quot;start&quot;</p>
<dd>If the first argument is <tt>&quot;start&quot;</tt>, or no first argument is given, <code>rc.news</code> initiates <font SIZE="-1">INN</font> startup.</p>
<dt>&quot;stop&quot;</p>
<dd>If the first argument is <tt>&quot;stop&quot;</tt>, <code>rc.news</code> initiates <font SIZE="-1">INN</font> shutdown.</dl>
<h2>Examples</h2>
<p>To start <font SIZE="-1">INN</font> and leave certain error messages going to the terminal: </p>
<pre> su news -s /bin/sh -c /etc/rc.news</pre>
<p>To run <font SIZE="-1">INN</font> at startup time from appropriate system boot scripts: </p>
<pre> su news -s /bin/sh -c /etc/rc.news &gt;&gt; &lt;pathlog&gt;/rc.news 2&gt;&amp;1</pre>
<p>To stop <font SIZE="-1">INN:</font> </p>
<pre> su news -s /bin/sh -c '/etc/rc.news stop'</pre>
<h2>Bugs</h2>
<p>Running <tt>&quot;rc.news start&quot;</tt> as root is never the right thing to do, so we should at minimum check for this and error, or perhaps change effective user <font SIZE="-1">ID</font>.</p>
<h2>History</h2>
<p>// <font SIZE="-1">FIXME:</font> any attribution for <i>rc.news</i> itself? </p>
<p> This manual page written by Jeffrey M. Vinocur &lt;jeff [at] litech.org&gt; for InterNetNews. </p>
<p> <tt>$Id:</tt> rc.news.pod 9727 2014-09-24 18:06:23Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8), <i><a href="/docs/linux/man/8-cnfsstat/">cnfsstat</a></i>(8), <i><a href="/docs/linux/man/8-expirerm/">expirerm</a></i>(8), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-innwatch/">innwatch</a></i>(8), <i><a href="/docs/linux/man/5-ovdb/">ovdb</a></i>(5). </p>
