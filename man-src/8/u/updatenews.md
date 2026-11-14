---
title: "updatenews(8)"
name: "updatenews"
section: "8"
letter: "u"
url: "/docs/linux/man/8-updatenews/"
description: "updatenews – post articles from outgoing spool directory and prefetch newsgroups"
---

<p>updatenews &#8211; post articles from outgoing spool directory and prefetch newsgroups</p>
<h2>Synopsis</h2>
<p><code>updatenews [ -h ] [ -v ] [ -a ] [ -g ] [ -o ] [ -l ] [ -w # ]</code></p>
<h2>Description</h2>
<p>Updatenews submits all those articles that have been stored within NewsCache&#8217;s outgoing-queue. If necessary the ActiveDB will be updated (see the -a option to force the update). Afterwards retrieves all the articles from the newsgroups listed in the PrefetchFile (This can be configured in newscache.conf). </p>
<h2>Options</h2>
<p>These programs follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Show summary of options.</p>
<dt><code>-v, &#8211;version</code></p>
<dd>Show version of program.</p>
<dt><code>-a, &#8211;active</code></p>
<dd>Force the prefetch the active data base. Updatenews first invalidate the ActiveDB to force the update.</p>
<dt><code>-g, &#8211;group</code></p>
<dd>Prefetch whole newsgroups.</p>
<dt><code>-o, &#8211;over</code></p>
<dd>Only prefetch the overview database.</p>
<dt><code>-l, &#8211;lock-group</code></p>
<dd>Always lock the newsgroup while prefetching it. This improves the performance of update- news slightly, but nobody else can read this newsgroup while prefetching.</p>
<dt><code>-w, &#8211;workers #</code></p>
<dd>Use # workers for prefetching. Each worker is assigned its own newsgroup to prefetch. </p>
</dl>
<h2>Files</h2>
<p>/etc/newscache.conf<br />
 /usr/sbin/newscache<br />
 /usr/sbin/newscacheclean<br />
 /usr/sbin/newscacheclean<br />
 /usr/sbin/updatenews</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-newscache-conf/">newscache.conf</a></code>(5), <code><a href="/docs/linux/man/8-newscacheclean/">newscacheclean</a></code>(8), <code><a href="/docs/linux/man/8-updatenews/">updatenews</a></code>(8).</p>
<h2>Authors</h2>
<p>1997-2000 Thomas Gschwind &lt;tom [at] infosys.tuwien.ac.at&gt;<br />
 2001-2004 Herbert Straub &lt;h.straub [at] aon.at&gt;</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;newscache [at] linuxhacker.org&gt;.</p>
<h2>Copyright</h2>
<p><code>NewsCache</code> is released under the <code>GNU General Public License (GPL).</code> There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
