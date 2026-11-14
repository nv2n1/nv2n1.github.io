---
title: "expireover(8)"
name: "expireover"
section: "8"
letter: "e"
url: "/docs/linux/man/8-expireover/"
description: "expireover – Expire entries from the news overview database"
---

<p>expireover &#8211; Expire entries from the news overview database</p>
<h2>Synopsis</h2>
<p><code>expireover</code> [<code>-ekNpqs</code>] [<code>-f</code> <i>file</i>] [<code>-w</code> <i>offset</i>] [<code>-z</code> <i>rmfile</i>] [<code>-Z</code> <i>lowmarkfile</i>]</p>
<h2>Description</h2>
<p><code>expireover</code> expires old entries from the news overview database. It reads in a list of newsgroups (by default from <i>pathdb</i>/active, but a different file can be specified with the <code>-f</code> option) and then removes from the overview database mentions of any articles that no longer exist in the news spool. </p>
<p> If <i>groupbaseexpiry</i> in <i>inn.conf</i> is true, <code>expireover</code> also removes old articles from the news spool according to the expiration rules in <i>expire.ctl</i>. Otherwise it only removes overview entries for articles that have already been removed by some other process, and <code>-e</code>, <code>-k</code>, <code>-N</code>, <code>-p</code>, <code>-q</code>, <code>-w</code>, and <code>-z</code> are all ignored. </p>
<p> When <i>groupbaseexpiry</i> is set, the default behavior of <code>expireover</code> is to remove the article from the spool once it expires out of all of the newsgroups to which it was crossposted. The article is, however, removed from the overview database of each newsgroup as soon as it expires out of that individual newsgroup. The effect is that an article crossposted to several groups will be removed from the overview database from each group one-by-one as its age passes the expiration threshold for that group as set in <i>expire.ctl</i>, and then when it expires out of the last newsgroup, it will be deleted from the news spool. </p>
<p> Articles that are stored in self-expiring storage backends such as <font SIZE="-1">CNFS</font> are normally treated differently and not expired until they expire out of the backend regardless of <i>expire.ctl</i>. See <code>-N</code>, however. </p>
<p> By default, <code>expireover</code> purges all overview information for newsgroups that have been removed from the server; this behavior is suppressed if <code>-f</code> is given.</p>
<h2>Options</h2>
<dl>
<dt><code>-e</code></p>
<dd>Remove articles from the news spool and all overview databases as soon as they expire out of any newsgroup to which they are posted, rather than retain them until they expire out of all newsgroups. <code>-e</code> and <code>-k</code> cannot be used at the same time. This flag is ignored if <i>groupbaseexpiry</i> is false.</p>
<dt><code>-f</code> <i>file</i></p>
<dd>Use <i>file</i> as the newsgroup list instead of <i>pathdb</i>/active. <i>file</i> can be <tt>&quot;-&quot;</tt> to indicate standard input. Using this flag suppresses the normal purge of all overview information from newsgroups that have been removed from the server.</p>
<dt><code>-k</code></p>
<dd>Retain all overview information for an article, as well as the article itself, until it expires out of all newsgroups to which it was posted. This can cause articles to stick around in a newsgroup for longer than the <i>expire.ctl</i> rules indicate, when they&#8217;re crossposted. <code>-e</code> and <code>-k</code> cannot be used at the same time. This flag is ignored if <i>groupbaseexpiry</i> is false.</p>
<dt><code>-N</code></p>
<dd>Apply <i>expire.ctl</i> rules to expire articles even from storage methods that have self-expire functionality. This may remove articles from self-expiring storage methods before the articles &#8220;naturally&#8221; expire. This flag is ignored if <i>groupbaseexpiry</i> is false.</p>
<dt><code>-p</code></p>
<dd>By default, <code>expireover</code> bases decisions on whether to remove an article on the arrival time on the server. This means that articles may be kept a little longer than if the decision were based on the article&#8217;s posting date. If this option is given, expiration decisions are based on the article posting date instead. This flag is ignored if <i>groupbaseexpiry</i> is false.</p>
<dt><code>-q</code></p>
<dd><code>expireover</code> normally prints statistics at the end of the expiration process. <code>-q</code> suppresses this report. This flag is ignored if <i>groupbaseexpiry</i> is false.</p>
<dt><code>-s</code></p>
<dd><code>expireover</code> normally only checks the existence of articles in the news spool if querying the storage method for that article to see if it still exists is considered &#8220;inexpensive&#8221;. To always check the existence of all articles regardless of how resource-intensive this may be, use the <code>-s</code> flag. See <i><a href="/docs/linux/man/5-storage-conf/">storage.conf</a></i>(5) for more information about this metric.</p>
<dt><code>-w</code> <i>offset</i></p>
<dd>&#8220;Warps&#8221; time so that <code>expireover</code> thinks that it&#8217;s running at some time other than the current time. This is occasionally useful to force groups to be expired or not expired without changing <i>expire.ctl</i> for the expire run. <i>offset</i> should be a signed floating point number specifying the number of days difference from the current time to use as &#8220;now&#8221;. This flag is ignored if <i>groupbaseexpiry</i> is false.</p>
<dt><code>-z</code> <i>rmfile</i></p>
<dd>Don&#8217;t remove articles immediately but instead write the path to the article or the token of the article to <i>rmfile</i>, which is suitable input for <i><a href="/docs/linux/man/1-fastrm/">fastrm</a></i>(1). This can substantially speed up deletion of expired articles for those storage methods where each article is a single file (such as tradspool and timehash). See the description of the <i>delayrm</i> keyword in <i><a href="/docs/linux/man/8-news-daily/">news.daily</a></i>(8) for more details. This flag is ignored if <i>groupbaseexpiry</i> is false.</p>
<dt><code>-Z</code> <i>lowmarkfile</i></p>
<dd>Write the lowest article numbers for each newsgroup as it&#8217;s expired to the specified file. This file is then suitable for <tt>&quot;ctlinnd lowmark&quot;</tt>. See <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8) for more information.</dl>
<h2>Examples</h2>
<p>Normally <code>expireover</code> is invoked from <i><a href="/docs/linux/man/8-news-daily/">news.daily</a></i>(8), which handles such things as processing the <i>rmfile</i> and <i>lowmarkfile</i> if necessary. Sometimes it&#8217;s convenient to manually expire a particular newsgroup, however. This can be done with a command like: </p>
<pre> echo example.test | expireover -f - -Z &lt;pathtmp in inn.conf&gt;/lowmark
 ctlinnd lowmark &lt;pathtmp&gt;/lowmark</pre>
<p>This can be particularly useful if a lot of articles in a particular group have expired but the overview information is still present, causing some clients to see a lot of &#8220;this article may have been cancelled&#8221; messages when they first enter the newsgroup.</p>
<h2>History</h2>
<p>Written by Rob Robertson &lt;rob [at] violet.berkeley.edu&gt; and Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; (with help from Dave Lawrence &lt;tale [at] uunet.uu.net&gt;) for InterNetNews. </p>
<p> <tt>$Id:</tt> expireover.pod 8575 2009-08-18 13:53:54Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-active/">active</a></i>(5), <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8), <i><a href="/docs/linux/man/8-expire/">expire</a></i>(8), <i><a href="/docs/linux/man/5-expire-ctl/">expire.ctl</a></i>(5), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-news-daily/">news.daily</a></i>(8). </p>
