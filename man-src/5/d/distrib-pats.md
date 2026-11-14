---
title: "distrib-pats(5)"
name: "distrib-pats"
section: "5"
letter: "d"
url: "/docs/linux/man/5-distrib-pats/"
description: "distrib.pats – Default values for the Distribution: header"
---

<p>distrib.pats &#8211; Default values for the Distribution: header</p>
<h2>Description</h2>
<p>The file <i>pathetc</i>/distrib.pats is used by <code>nnrpd</code> to determine the default value of the Distribution: header. Blank lines and lines beginning with a number sign (<tt>&quot;#&quot;</tt>) are ignored. All other lines consist of three fields separated by a colon: </p>
<pre> &lt;weight&gt;:&lt;pattern&gt;:&lt;value&gt;</pre>
<p>The first field is the weight to assign to this match. If a newsgroup matches multiple lines, the line with the highest weight is used. This should be an arbitrary integer greater than zero. The order of lines in the file is only important if groups have equal weight (in which case, the first matching line will be used). </p>
<p> The second field is either the name of a newsgroup or a <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3)-style pattern to specify a set of newsgroups. </p>
<p> The third field is the value that should be used for the Distribution: header of a posted article, if this line was picked as the best match and no Distribution: header was supplied by the user. It can be an empty string, specifying that no Distribution: header should be added. If it is not empty, it is better to only use US-ASCII characters for that field; otherwise, make sure it is encoded in <font SIZE="-1">UTF-8</font>. </p>
<p> When a post is received by <code>nnrpd</code> that does not already contain a Distribution: header, each newsgroup to which an article is posted will be checked against this file in turn, and the matching line with the highest weight will be used as the value of the Distribution: header. If no lines match, or if the matching line has an empty string for its third field, no header will be added. In case a distribution is added by <code>nnrpd</code>, make sure it is not rejected by the <i>newsfeeds</i> <tt>&quot;ME&quot;</tt> entry. </p>
<p> A list of recommended distributions can be specified and described in <i><a href="/docs/linux/man/5-distributions/">distributions</a></i>(5).</p>
<h2>History</h2>
<p>Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. Converted to <font SIZE="-1">POD</font> by Russ Allbery &lt;eagle [at] eyrie.org&gt;. </p>
<p> <tt>$Id:</tt> distrib.pats.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-distributions/">distributions</a></i>(5), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5), <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8), <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3). </p>
