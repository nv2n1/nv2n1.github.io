---
title: "innxmit(8)"
name: "innxmit"
section: "8"
letter: "i"
url: "/docs/linux/man/8-innxmit/"
description: "innxmit – Send Usenet articles to a remote NNTP server"
---

<p>innxmit &#8211; Send Usenet articles to a remote NNTP server</p>
<h2>Synopsis</h2>
<p><code>innxmit</code> [<code>-acdHlprsv</code>] [<code>-P</code> <i>portnum</i>] [<code>-T</code> <i>seconds</i>] [<code>-t</code> <i>seconds</i>] <i>host</i> <i>file</i></p>
<h2>Description</h2>
<p><code>innxmit</code> connects to the <font SIZE="-1">NNTP</font> server at the specified <i>host</i> (validating itself via <i>passwd.nntp</i> if possible) and sends it the articles specified in the batch file named <i>file</i>. It is normally invoked by a script run out of <i><a href="/docs/linux/man/8-cron/">cron</a></i>(8) that uses <code>shlock</code> to lock the host name, followed by a <code>ctlinnd</code> command to flush the batch file. If <i>file</i> is not an absolute path name, it is taken relative to the directory specified by the <i>pathoutgoing</i> parameter in <i>inn.conf</i>. It is normally written by specifying the <tt>&quot;Wnm&quot;</tt> flags in the <i>newsfeeds</i> file. Each line in the batch file should be in one of the following formats: </p>
<pre> article Message-ID
 article</pre>
<p>The first field is either the storage <font SIZE="-1">API</font> token of an article or the name of a file holding an article. If it is not an absolute pathname or a storage <font SIZE="-1">API</font> token, it is taken to be a file name relative to <i>patharticles</i> in <i>inn.conf</i>. If the second field is not specified, the message-ID will be obtained by scanning the article. The two fields, if present, are separated by a space. If a communication error such as a <i><a href="/docs/linux/man/2-write/">write</a></i>(2) failure occurs, <code>innxmit</code> will stop sending and rewrite the batch file to contain the current article and any other unsent articles. </p>
<p> An alternative to <code>innxmit</code> can be <code>innduct</code>, mentioned in the <i><a href="/docs/linux/man/8-innfeed/">innfeed</a></i>(8) man page.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>If all articles were sent successfully, <code>innxmit</code> will remove the batch file; otherwise it will rewrite it to contain the list of unsent articles. If no articles were sent or rejected, the file is left untouched. This can cause the batch file to grow excessively large if many articles have been expired and there are communication problems. To always rewrite the batch file, use the <code>-a</code> flag.</p>
<dt><code>-c</code></p>
<dd>In streaming mode, a check of each message-ID is still made to avoid sending articles already on the server. The <code>-c</code> flag will, if streaming mode is supported, result in sending articles without checking. This results in slightly greater throughput and may be appropriate when it is known that the site could not already have the articles such as in the case of a &#8220;leaf&#8221; site.</p>
<dt><code>-d</code></p>
<dd>Use the <code>-d</code> flag to print debugging information on standard error. This will show the protocol transactions between <code>innxmit</code> and the <font SIZE="-1">NNTP</font> server on the remote host.</p>
<dt><code>-H</code></p>
<dd>If the <code>-H</code> flag is given, then only headers are sent to <i>host</i> for all articles except control messages. And the Bytes: header is also included even if it does not exist in the original article. The <code>-H</code> flag is useful for Diablo reader.</p>
<dt><code>-l</code></p>
<dd>The <code>-l</code> flag is used to turn on logging of reasons the remote gives for rejecting an article.</p>
<dt><code>-P</code> <i>portnum</i></p>
<dd>To specify a port number other than the default, use the <code>-P</code> flag.</p>
<dt><code>-p</code></p>
<dd>If the <code>-p</code> flag is given, then no connection is made and the batch file is purged of entries that refer to files that no longer exist. This implies the <code>-a</code> flag.</p>
<dt><code>-r</code></p>
<dd>If the remote server sends an unexpected reply code, <code>innxmit</code> will requeue the article and proceed. Use the <code>-r</code> flag if the article should not be requeued.</p>
<dt><code>-s</code></p>
<dd><code>innxmit</code> will attempt to negotiate a streaming mode extension of the <font SIZE="-1">NNTP</font> protocol with the server at connect time. If successful, it will use a slightly different protocol that enhances throughput. If the server does not recognize the streaming mode negotiation, <code>innxmit</code> will revert to normal <font SIZE="-1">NNTP</font> transfer mode. Use the <code>-s</code> flag to disable the attempt to negotiate the streaming mode extension.</p>
<dt><code>-T</code> <i>seconds</i></p>
<dd>To specify the total amount of time that should be allowed for article transfers, use the <code>-T</code> flag. The default is to wait until an I/O error occurs, or all the articles have been transferred. If the <code>-T</code> flag is used, the time is checked just before each article is started; it will not abort a transfer that is in progress.</p>
<dt><code>-t</code> <i>seconds</i></p>
<dd><code>innxmit</code> normally blocks until the connection is made. To specify a timeout on how long to try to make the connection, use the <code>-t</code> flag.</p>
<dt><code>-v</code></p>
<dd>Upon exit, <code>innxmit</code> reports transfer and <font SIZE="-1">CPU</font> usage statistics via syslog. If the <code>-v</code> flag is used, they will also be printed on the standard output.</dl>
<h2>History</h2>
<p>Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. Converted to <font SIZE="-1">POD</font> by Julien Elie. </p>
<p> <tt>$Id:</tt> innxmit.pod 9590 2013-12-19 17:48:22Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8), <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5), <i><a href="/docs/linux/man/5-passwd-nntp/">passwd.nntp</a></i>(5), <i><a href="/docs/linux/man/1-shlock/">shlock</a></i>(1). </p>
