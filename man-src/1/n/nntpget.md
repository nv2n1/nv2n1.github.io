---
title: "nntpget(1)"
name: "nntpget"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nntpget/"
description: "nntpget – get Usenet articles from a remote NNTP server"
---

<h2>NAME</h2>
<p> nntpget &#8211; get Usenet articles from a remote NNTP server</p>
<h2>SYNOPSIS</h2>
<p> <i>nntpget</i> [ <code>-d</code><i> dist</i> ] [ <code>-f</code><i> file</i> ] [ <code>-n</code><i> newsgroups</i> ] [ <code>-t</code><i> timestring</i> ] [ <code>-o</code> ] [ <code>-u</code><i> file</i> ] [ <code>-v</code> ] <i>host</i></p>
<h2>DESCRIPTION</h2>
<p> <i>Nntpget</i> connects to the NNTP server at the specified <i>host</i> and retrieves articles from it. The Message-ID&#8217;s of the desired articles are read from standard input. The articles are sent to standard output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code></p>
<dd> The &#8220;-o&#8221; option may be used only if the command is executed on the host where the <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8) server is running. If this option is used, <i>nntpget</i> connects to the specified remote <i>host</i> to retrieve articles. Any article not present in the local <i>history</i> database is then fetched from the remote site and offered to the local server.</p>
<dt><code>-v</code></p>
<dd> If the &#8220;<code>-v</code>&#8221; option is used with the &#8220;<code>-o</code>&#8221; option then the Message-ID of each article will be sent to standard output as it is processed.</p>
<dt><code>-f</code></p>
<dd> The list of article Message-ID&#8217;s is normally read from standard input. If the &#8220;<code>-f</code>&#8221; option is used, then a &#8220;newnews&#8221; command is used to retrieve all articles newer then the modification date of the specified <i>file</i>.</p>
<dt><code>-u</code></p>
<dd> The &#8220;<code>-u</code>&#8221; option is like &#8220;<code>-f</code>&#8221; except that if the transfer succeedes, the file will be updated with a statistics line, modifying its timestamp so that it can be used in later invocations.</p>
<dt><code>-t</code></p>
<dd> If the &#8220;-t&#8221; option is used, then the specified <i>timestring</i> is used as the time and date parameter to the &#8220;newnews&#8221; command.</p>
<dt><code>-n</code></p>
<dd> If either the &#8220;<code>-u</code>&#8221; or &#8220;<code>-f</code>&#8221; options are used, then the &#8220;<code>-n</code>&#8221; option may be used to specify a newsgroup list. The default is &#8220;*&#8221;.</p>
<dt><code>-d</code></p>
<dd> The &#8220;<code>-d</code>&#8221; option may be used to specify a distribution list when using the &#8220;<code>-u</code>&#8221; or &#8220;<code>-f</code>&#8221; options. The default is no distribution list.</dl>
<h2>HISTORY</h2>
<p> Written by Rich $alz &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. This is revision 5909, dated 2002-12-03.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-innd/">innd</a>(8). </p>
<h2>Index</h2>
