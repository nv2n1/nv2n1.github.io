---
title: "cyrfetchnews(8)"
name: "cyrfetchnews"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cyrfetchnews/"
description: "cyrfetchnews – retrieve new articles from peer and feed to Cyrus"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>cyrfetchnews &#8211; retrieve new articles from peer and feed to Cyrus</p>
<h2>Synopsis</h2>
<p><code>cyrfetchnews</code> [ <code>-C</code> <i>config-file</i> ] [ <code>-s</code> <i>servername[:port]</i> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[ <code>-n</code> ] [ <code>-y</code> ] [ <code>-w</code> <i>wildmat</i> ] [ <code>-f</code> <i>tstampfile</i> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[ <code>-a</code> <i>authname</i> [ <code>-p</code> <i>password</i> ] ] <i>peername</i></p>
<h2>Description</h2>
<p><i>Cyrfetchnews</i> retrieves news articles from a peer news server and feeds them to a Cyrus server. <i>Cyrfetchnews</i> connects to the peer specified by <i>peername</i>, requests new articles since the time stored in <i>tstampfile</i> and feeds them to <i>servername</i>. </p>
<p> <i>Cyrfetchnews</i> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> config-file</i></p>
<dd>Read configuration options from <i>config-file</i>.</p>
<dt><code>-s</code><i> servername</i></p>
<dd>Hostname of the Cyrus server (with optional port) to which articles should be fed. Defaults to &quot;localhost:nntp&quot;.</p>
<dt><code>-n</code></p>
<dd>Don&#8217;t use the NEWNEWS command. <i>Cyrfetchnews</i> will keep track of the high and low water marks for each group and use them to fetch new articles.</p>
<dt><code>-y</code></p>
<dd>Use 4 instead of 2 digits for year. 2-digits are rfc977- but not y2k-compliant.</p>
<dt><code>-w</code><i> wildmat</i></p>
<dd>Wildmat pattern specifying which newsgroups to search for new articles. Defaults to &quot;*&quot;.</p>
<dt><code>-f</code><i> tstampfile</i></p>
<dd>File in which to read/write the timestamp of when articles were last retrieved. Defaults to &quot;newsstamp&quot; located in <i>configdir</i> as specified by the configuration options.</p>
<dt><code>-a</code><i> authname</i></p>
<dd>Userid to use for authentication.</p>
<dt><code>-p</code><i> password</i></p>
<dd>Password to use for authentication.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></p>
<dd></dl>
