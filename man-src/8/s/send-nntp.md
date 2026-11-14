---
title: "send-nntp(8)"
name: "send-nntp"
section: "8"
letter: "s"
url: "/docs/linux/man/8-send-nntp/"
description: "send-nntp, send-ihave – send Usenet articles to remote site"
---

<p>send-nntp, send-ihave &#8211; send Usenet articles to remote site</p>
<h2>Synopsis</h2>
<p><code>send-nntp</code> [ <code>-d</code> ] <code>sitename:hostname | sitename</code> [ <code>sitename:hostname | sitename ..</code> ] </p>
<p> <code>send-ihave</code> [ <code>-d</code> ] <code>sitename:hostname | sitename</code> [ <code>sitename:hostname | sitename ..</code> ]</p>
<h2>Description</h2>
<p>The send-* utilities are scripts that process the batch files written by <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8) to send Usenet articles to a remote NNTP site. </p>
<p> The sites to be fed may be specified by giving <i>sitename</i> <i>hostname</i> pairs on the command line. </p>
<p> The <i>sitename</i> is the label the site has in the <i>newsfeeds</i> file, the <i>hostname</i> is the real hostname of the remote site, a FQDN (Fully Qualified Domain Name). Normally, the <i>sitename</i> and the <i>hostname</i> are the same, and as such don&#8217;t have to be specified as sitename:hostname pairs but just as a sitename. </p>
<p> <i>send-nntp</i> starts an innxmit to send the articles to the remote site. </p>
<p> <i>send-ihave</i> encapsulates the articles in an <i>ihave</i> control message and uses <i>inews</i> to send the articles to a <i>to.sitename</i> pseudo-group. Using <i>send-ihave</i> is discouraged, nobody uses it anymore and even the author of this manpage is unsure as to how it actually works or used to work. </p>
<p> <i>send-*</i> expect that the batchfile for a site is named <i>&lt;pathoutgoing in inn.conf&gt;/sitename</i>. To prevent batchfile corruption, <i><a href="/docs/linux/man/1-shlock/">shlock</a></i>(1) is used to &#8220;lock&#8221; these files.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code></p>
<dd>The &#8220;-d&#8221; flag causes <i>nntpsend</i> to send output to stdout rather than the log file <i>&lt;pathlog in inn.conf&gt;/&lt;program-name&gt;.log</i>.</dl>
<h2>Notes</h2>
<p>You should probably not use send-nntp, but <i>innfeed</i>, or if that is not possible, <i>nntpsend</i>. </p>
<p> The usual flags for a batch file for send-nntp are &#8220;<code>Tf,Wfm</code>&#8221;.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a>(5), <a href="/docs/linux/man/8-nntpsend/">nntpsend</a>(8) </p>
