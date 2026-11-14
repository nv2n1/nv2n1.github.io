---
title: "tinyleaf(8)"
name: "tinyleaf"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tinyleaf/"
description: "tinyleaf – Very simple IHAVE-only NNTP server"
---

<p>tinyleaf &#8211; Very simple IHAVE-only NNTP server</p>
<h2>Synopsis</h2>
<p><code>tinyleaf</code> <i>spool</i> [<i>processor</i>]</p>
<h2>Description</h2>
<p><code>tinyleaf</code> is intended to be the simplest possible transit news server that still does something useful. It must be run under <i><a href="/docs/linux/man/8-inetd/">inetd</a></i>(8) or some equivalent, and only implements three commands (<font SIZE="-1">HELP</font>, <font SIZE="-1">IHAVE</font>, and <font SIZE="-1">QUIT</font>). When it receives an article, it saves it into the directory <i>spool</i> and, if <i>processor</i> is given, passes information about the article to <i>processor</i> via a pipe. The file name of the article will be the <font SIZE="-1">MD5</font> hash of its message-ID, and if a file by that name already exists, <code>tinyleaf</code> will refuse the article, reporting it as a duplicate. </p>
<p> If <i>processor</i> is given, it should specify the path to a program. That program is started when <code>tinyleaf</code> starts, and its current working directory will be <i>spool</i>. For each article received by <code>tinyleaf</code>, a single line will be sent to standard input of <i>processor</i>. That line will consist of the file name of the received article (relative to <i>spool</i>), a single space, and the message-ID of the received article. Note that the message-ID will be taken from the argument to the <font SIZE="-1">IHAVE</font> command and may not match the Message-ID: header in the article. When <code>tinyleaf</code> shuts down, standard input to <i>processor</i> will be closed. </p>
<p> <code>tinyleaf</code> does no syntax verification of received articles whatsoever; it just stores them and optionally passes them off to <i>processor</i>. It also never deletes articles; normally, <i>processor</i> should do that when it&#8217;s finished doing whatever it needs to with the article. </p>
<p> <code>tinyleaf</code> expects <font SIZE="-1">NNTP</font> commands on standard input and replies on standard output. Status information and any error messages are sent to standard error. It does no authentication; any authentication must be done by <i><a href="/docs/linux/man/8-inetd/">inetd</a></i>(8) or by a wrapper program. (One simple authentication mechanism is to invoke <code>tinyleaf</code> via <i><a href="/docs/linux/man/8-tcpd/">tcpd</a></i>(8) from <font SIZE="-1">TCP</font> wrappers and use <i>/etc/hosts.allow</i> and <i>/etc/hosts.deny</i> to restrict who can talk to the server.) </p>
<p> <code>tinyleaf</code> has a (currently hard-coded) maximum message size of 1&nbsp;<wbr><font SIZE="-1">MB</font> and a (similarly hard-coded) timeout of ten minutes for each command or chunk of article data.</p>
<h2>Example</h2>
<p>Suppose that you want to archive news articles on a particular host (like the <font SIZE="-1">FTP</font> server for a newsgroup archive) where you don&#8217;t want the overhead of running a full-blown news server. Write a program that reads one line at a time from standard input and treats everything before the first space as the filename of a news article to archive. Each time the program reads a line, it should archive that file and then delete it, and it should exit when it gets end of file on standard input. </p>
<p> Then, add a line like: </p>
<pre> nntp stream tcp nowait archive /usr/sbin/tcpd \
 &lt;pathbin&gt;/tinyleaf &lt;pathspool&gt;/tinyleaf &lt;pathbin&gt;/archive</pre>
<p>(all on one line &#8212; the backslash and split in this line is just for readability) where <tt>&quot;archive&quot;</tt> is the user that owns the archive, <i>/usr/sbin/tcpd</i> is the path to <i><a href="/docs/linux/man/8-tcpd/">tcpd</a></i>(8), <i>pathbin</i>/tinyleaf is the path to this program, <i>pathspool</i>/tinyleaf is some scratch directory that the user <tt>&quot;archive&quot;</tt> has write access to, and <i>pathbin</i>/archive is the path to your <code>archive</code> script. </p>
<p> You can now restrict access to <code>tinyleaf</code> to just your local news server with <tt>&quot;/etc/hosts.allow&quot;</tt> and <tt>&quot;/etc/hosts.deny&quot;</tt> and set up an ordinary feed from the server to the archive host, just like you would to any other news server, of only the newsgroup that you want to archive. </p>
<p> Note that the archiving script should probably perform basic syntax and validity checks on the input, since <code>tinyleaf</code> doesn&#8217;t. </p>
<p> This is the application that motivated the original development of this program.</p>
<h2>Bugs</h2>
<p>The timeout and maximum message size should really be configurable. <code>tinyleaf</code> should also probably not just respond 500 to every command other than <font SIZE="-1">HELP</font>, <font SIZE="-1">IHAVE</font>, and <font SIZE="-1">QUIT</font>; there are more useful (and more expected) error codes that could be returned. </p>
<p> An option to scan the spool directory for any left-over files and pass them to the processor when starting up would be useful.</p>
<h2>History</h2>
<p>Written by Russ Allbery &lt;eagle [at] eyrie.org&gt; for InterNetNews. </p>
<p> <tt>$Id:</tt> tinyleaf.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-hosts_access/">hosts_access</a></i>(5), <i><a href="/docs/linux/man/8-inetd/">inetd</a></i>(8), <i><a href="/docs/linux/man/8-tcpd/">tcpd</a></i>(8). </p>
