---
title: "distributions(5)"
name: "distributions"
section: "5"
letter: "d"
url: "/docs/linux/man/5-distributions/"
description: "distributions – Recommended values for the Distribution: header"
---

<p>distributions &#8211; Recommended values for the Distribution: header</p>
<h2>Description</h2>
<p>The file <i>pathetc</i>/distributions contains a list of relevant distributions and their descriptions. It provides local information for posters who wish to add a Distribution: header to their articles so as to restrict their propagation, although it does not guarantee that such articles will not leak elsewhere because of a misconfiguration of a news server to which they are fed. See <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5) for more information about how a news server handles the Distribution: header. </p>
<p> Each line of this file consists of a distribution area followed by its description (encoded in <font SIZE="-1">UTF-8</font>) after at least a whitespace. For instance: </p>
<pre> fr Local to France.
 local Local to this news server.
 nj Local to New Jersey.
 usa Local to the United States of America.</pre>
<p>Blank lines and lines beginning with a number sign (<tt>&quot;#&quot;</tt>) are ignored. </p>
<p> Any client that issues the <font SIZE="-1">LIST</font> <font SIZE="-1">DISTRIBUTIONS</font> command obtain these recommended values, if available. However, be aware that use of the <font SIZE="-1">LIST</font> <font SIZE="-1">DISTRIBUTIONS</font> command is not widespread (though documented in <font SIZE="-1">RFC</font>&nbsp;<wbr>6048) and most news clients will never ask for this file. </p>
<p> If this file is empty, it is not an error. The server will just send the client an empty response. And if the file is missing, the server will also send the client an appropriate response to indicate that the distributions list is not maintained on the server. </p>
<p> The Distribution: header can also be automatically set by <code>nnrpd</code> if <i><a href="/docs/linux/man/5-distrib-pats/">distrib.pats</a></i>(5) is correctly configured.</p>
<h2>History</h2>
<p>Written by Julien Elie for InterNetNews. </p>
<p> <tt>$Id:</tt> distributions.pod 9138 2010-10-29 18:09:50Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-distrib-pats/">distrib.pats</a></i>(5), <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5), <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8). </p>
