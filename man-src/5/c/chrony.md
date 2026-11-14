---
title: "chrony(5)"
name: "chrony"
section: "5"
letter: "c"
url: "/docs/linux/man/5-chrony/"
description: "chrony.conf – chronyd configuration file"
---

<p>chrony.conf &#8211; chronyd configuration file </p>
<h2>Synopsis</h2>
<p><code>/etc/chrony.conf</code> </p>
<h2>Description</h2>
<p><i>chrony</i> is a pair of programs for maintaining the accuracy of computer clocks. <i>chronyd</i> is a background daemon program that can be started at boot time. Assuming that you have found some servers, you need to set up a configuration file to run <i>chrony</i>. The (compiled-in) default location for this file is <code>/etc/chrony.conf</code>. Assuming that your ntp servers are called `a.b.c&#8217; and `d.e.f&#8217;, your <code>chrony.conf</code> file could contain as a minimum<br />
&nbsp;<wbr>&nbsp;<wbr>server a.b.c<br />
&nbsp;<wbr>&nbsp;<wbr>server d.e.f<br />
&nbsp;<wbr>&nbsp;<wbr>server g.h.i However, you will probably want to include some of the other directives described in detail in the documentation supplied with the distribution (<i>chrony.txt</i> and <i>chrony.texi</i>). The following directives may be particularly useful : `driftfile&#8217;, `generatecommandkey&#8217;, `keyfile&#8217;, `makestep&#8217;. Also, the `iburst&#8217; server option is useful to speed up the initial synchronization. The smallest useful configuration file would look something like<br />
&nbsp;<wbr>&nbsp;<wbr>server a.b.c iburst<br />
&nbsp;<wbr>&nbsp;<wbr>server d.e.f iburst<br />
&nbsp;<wbr>&nbsp;<wbr>server g.h.i iburst<br />
&nbsp;<wbr>&nbsp;<wbr>keyfile&nbsp;<wbr>/etc/chrony.keys<br />
&nbsp;<wbr>&nbsp;<wbr>generatecommandkey<br />
&nbsp;<wbr>&nbsp;<wbr>driftfile&nbsp;<wbr>/var/lib/chrony/drift<br />
&nbsp;<wbr>&nbsp;<wbr>makestep 10 3 </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chrony/">chrony</a>(1),</code> <code><a href="/docs/linux/man/1-chronyc/">chronyc</a>(1),</code> <code><a href="/docs/linux/man/8-chronyd/">chronyd</a>(8)</code> <i><a rel="nofollow" href="http://chrony.tuxfamily.org/">http://chrony.tuxfamily.org/</a></i> </p>
<h2>Author</h2>
<p>Richard Curnow &lt;rc [at] rc0.org.uk&gt; </p>
<p> This man-page was written by Jan Schaumann &lt;jschauma [at] netmeister.org&gt; as part of &quot;The Missing Man Pages Project&quot;. Please see <i><a rel="nofollow" href="http://www.netmeister.org/misc/m2p2/index.html">http://www.netmeister.org/misc/m2p2/index.html</a></i> for details. </p>
<p> The complete chrony documentation is supplied in texinfo format.</p>
