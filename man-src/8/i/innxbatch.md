---
title: "innxbatch(8)"
name: "innxbatch"
section: "8"
letter: "i"
url: "/docs/linux/man/8-innxbatch/"
description: "innxbatch – send xbatched Usenet articles to a remote NNTP server"
---

<p>innxbatch &#8211; send xbatched Usenet articles to a remote NNTP server</p>
<h2>Synopsis</h2>
<p><i>innxbatch</i> [ <code>-D</code> ] [ <code>-t</code><i> timeout</i> ] [ <code>-T</code><i> timeout</i> ] [ <code>-v</code> ] <i>host</i> <i>file &#8230;</i></p>
<h2>Description</h2>
<p><i>Innxbatch</i> connects to the NNTP server at the specified <i>host</i> and sends it the specified xbatch files, using the XBATCH extension to the NNTP protocol. It is normally invoked by a script run out of <i><a href="/docs/linux/man/8-cron/">cron</a></i>(8) that uses <i><a href="/docs/linux/man/1-shlock/">shlock</a></i>(1) to lock the host name, followed by a <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8) command to flush the batchfile. Each file is removed after it has been successfully transferred. If a communication error such as a <i><a href="/docs/linux/man/2-write/">write</a></i>(2) failure, or an unexpected reply from the remote server occurs, <i>innxbatch</i> will stop sending and leave all remaining files untouched for later retry. </p>
<h2>Options</h2>
<dl>
<dt><code>-t seconds</code></p>
<dd><i>Innxbatch</i> normally blocks until the connection is made. To specify a timeout on how long to try to make the connection, use the &#8220;-t&#8221; flag.</p>
<dt><code>-T seconds</code></p>
<dd>To specify the total amount of time that should be allowed for article transfers, use the &#8220;-T&#8221; flag.<br />
 The default is to wait until an I/O error occurs, or all the articles have been transferred. If the &#8220;-T&#8221; flag is used, the time is checked just before each article is started; it will not abort a transfer that is in progress.</p>
<dt><code>-v</code></p>
<dd>Upon exit, <i>innxbatch</i> reports transfer and CPU usage statistics via <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3). If the &#8220;-v&#8221; flag is used, they will also be printed on the standard output.</p>
<dt><code>-D</code></p>
<dd>Use the &#8220;-D&#8221; flag to print debugging information on standard error. This will show the protocol transactions between <i>innxbatch</i> and the NNTP server on the remote host.</dl>
<h2>Examples</h2>
<p>A sample <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a>(5)</i> entry to produce appropriate xbatch files (thanks to Karsten Leipold &lt;poldi [at] dfn.de&gt;): </p>
<pre> nase\
 :*\
 :Tc,Wnb\
 :&lt;pathbin in inn.conf&gt;/batcher \
 -p &quot;(&lt;$ac_cv_path_COMPRESS in config.cache&gt; &gt;\
 &lt;pathoutgoing in inn.conf&gt;/nase.\$\$)&quot; \
 nase.do.main</pre>
<p>A sample script to invoke <i><a href="/docs/linux/man/8-innxbatch/">innxbatch</a>(8)</i> is: </p>
<pre> #!/bin/sh
 ## SH script to send xbatches for a site, wrapped around innxbatch
 ## Invocation:
 ## sendxbatches.sh &lt;sitename&gt; &lt;hostname&gt; &lt;xbatch file name&gt; ...
 if [ $# -le 3 ]
 then
 echo &quot;usage: $0 &lt;sitename&gt; &lt;hostname&gt; &lt;xbatch file name&gt;&quot;
 exit 1
 fi
 . &lt;pathbin in inn.conf&gt;/innshellvars
 site=&quot;$1&quot;; host=&quot;$2&quot;; shift; shift
 ctlinnd flush &quot;$site&quot; \
 &amp;&amp; sleep 5 \
 &amp;&amp; exec $NEWSBIN/innxbatch -v -D &quot;$host&quot; $*</pre>
<h2>History</h2>
<p>Written by Stefan Petri &lt;petri [at] ibr.cs.tu-bs.de&gt;, modelled after <i><a href="/docs/linux/man/8-innxmit/">innxmit</a></i>(8) and the XBATCH patch for the nntp reference implementation.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a>(8), <a href="/docs/linux/man/5-inn-conf/">inn.conf</a>(5), <a href="/docs/linux/man/8-innd/">innd</a>(8), <a href="/docs/linux/man/8-innxmit/">innxmit</a>(8), <a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a>(5), <a href="/docs/linux/man/8-nntpsend/">nntpsend</a>(8), <a href="/docs/linux/man/1-shlock/">shlock</a>(1). </p>
