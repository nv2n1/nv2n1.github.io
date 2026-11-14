---
title: "undocumented(7)"
name: "undocumented"
section: "7"
letter: "u"
url: "/docs/linux/man/7-undocumented/"
description: "undocumented – No manpage for this program, utility or function."
---

<p>undocumented &#8211; No manpage for this program, utility or function.</p>
<h2>Description</h2>
<p>This <code>program</code>, <code>utility</code> or <code>function </code> does not have a useful manpage. Before opening a bug to report this, please check with the Debian Bug Tracking System (BTS) at &lt;<i><a rel="nofollow" href="http://bugs.debian.org/">http://bugs.debian.org/</a></i>&gt; if a bug has already been reported. If not, you can submit a wishlist bug if you want. If you are a competent and accurate writer and are willing to spend the time reading the source code and writing good manpages please write a better man page than this one. Please <code>contact </code> the <code>package maintainer </code> and copy <i>man-pages [at] qa.debian.org</i> in order to avoid several people working on the same manpage. Even if you are not an accurate writer, your input may be helpful. Writing manual pages is quite easy, the format is described in <code><a href="/docs/linux/man/7-man/">man</a></code>(7). The most important and time-consuming task is to collect the information to be put in the new manpage. </p>
<h2>Diagnostics</h2>
<p>It is possible that the man page for the command you specified is installed and that your manual page index caches are out of sync. You should try running <code><a href="/docs/linux/man/8-mandb/">mandb</a></code>(8). </p>
<p> Try the following options if you want more information: </p>
<p> <i>foo</i> <code>&#8211;help</code>, <i>foo</i> <code>-h</code>, <i>foo</i><code> -?</code> </p>
<p> <code>info</code><i> foo</i> </p>
<p> <code>whatis</code> <code>foo</code>, <code>apropos</code><i> foo</i> </p>
<p> <code>dpkg &#8211;listfiles</code> <i>foo</i>, <code>dpkg &#8211;search </code><i>foo</i> </p>
<p> <code>locate &#8216;*</code><i>foo</i><code>*&#8217;</code> </p>
<p> <code>find / -name &#8216;*</code><i>foo</i><code>*&#8217;</code> </p>
<p> Additionally, check the directories <i>/usr/share/doc/foo</i>, <i>/usr/lib/foo</i>. </p>
<p> The documentation might be in a package starting with the same name as the package the software belongs to, but ending with -doc or -docs. </p>
<p> If you still didn&#8217;t find the information you are looking for you might consider posting a call for help to <i>debian-user [at] lists.debian.org</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-info/">info</a></code>(1), <code><a href="/docs/linux/man/1-whatis/">whatis</a></code>(1), <code><a href="/docs/linux/man/1-apropos/">apropos</a></code>(1), <code><a href="/docs/linux/man/8-dpkg/">dpkg</a></code>(8), <code><a href="/docs/linux/man/1-locate/">locate</a></code>(1), <code><a href="/docs/linux/man/1-find/">find</a></code>(1), <code><a href="/docs/linux/man/1-updatedb/">updatedb</a></code>(1), <code><a href="/docs/linux/man/3-undocumented/">undocumented</a></code>(3), <code><a href="/docs/linux/man/7-man/">man</a></code>(7), <code><a href="/docs/linux/man/8-mandb/">mandb</a></code>(8), <code><a href="/docs/linux/man/7-missing/">missing</a></code>(7). </p>
