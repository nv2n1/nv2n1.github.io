---
title: "newscacheclean(8)"
name: "newscacheclean"
section: "8"
letter: "n"
url: "/docs/linux/man/8-newscacheclean/"
description: "test – Purge the NewsCache to SpoolSize (newscache.conf parameter)."
---

<p>test &#8211; Purge the NewsCache to SpoolSize (newscache.conf parameter).</p>
<h2>Synopsis</h2>
<p><code>newscacheclean </code> [<i>-h</i>] [<i>-s</i>] [<i>-p</i>] [<i>&#8211;version</i>] [<i>-c config-file</i>]</p>
<h2>Description</h2>
<p>The <code>newscacheclean</code> command purges the Cache from NewsCache to the SpoolSize parameter specified in the newscache.conf file. The program newscacheclean walks through the directory tree of SpoolDirectory (newscache.conf parameter) and adds every newsgroup db and every articel file into the purge list. Every outdated external article is also inserted. Then the purge list is sorted by access time. The purge removes first all outdated external articles and then one article or newsgroup database after the other until SpoolSize (newscache.conf parameter) is reached. </p>
<h2>Options</h2>
<p>This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd>Show summary of options.</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd>Show version of program.</dd>
<dt><code>-c &#8211;configuration config-file</code></dt>
<dd>
</dd><dt><code>-s &#8211;statistic</code></dt>
<dd>Show statistic informations.</dd>
<dt><code>-p &#8211;print-purgetable</code></dt>
<dd>Print the sorted purge table.</dd>
<dt><code>-t &#8211;try</code></dt>
<dd>Try, not really removing files. </dd>
</dl>
<h2>Files</h2>
<p>/etc/newscache.conf<br/>
 /usr/sbin/newscache<br/>
 /usr/sbin/newscacheclean<br/>
 /usr/sbin/newscacheclean<br/>
 /usr/sbin/updatenews</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-newscache/">newscache</a></code>(8), <code><a href="/docs/linux/man/8-updatenews/">updatenews</a></code>(8), <code>newscache.conf</code>(5), </p>
<h2>Authors</h2>
<p>1997-2000 Thomas Gschwind &lt;tom [at] infosys.tuwien.ac.at&gt;<br/>
 2001-2004 Herbert Straub &lt;h.straub [at] aon.at&gt;</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;newscache [at] linuxhacker.org&gt;.</p>
<h2>Copyright</h2>
<p><code>NewsCache</code> is released under the <code>GNU General Public License (GPL).</code> There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
