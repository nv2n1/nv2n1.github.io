---
title: "mknetid(8)"
name: "mknetid"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mknetid/"
description: "mknetid – generate data for netid map"
---

<p>mknetid &#8211; generate data for netid map</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/usr/lib/yp/mknetid</code> [-q] [-h&nbsp;<wbr><i>hosts</i>] [-p&nbsp;<wbr><i>passwd</i>] [-g&nbsp;<wbr><i>group</i>] [-d&nbsp;<wbr><i>domain</i>] [-n&nbsp;<wbr><i>netid</i>]</p>
<dt> <code>/usr/lib/yp/mknetid</code> &#8211;version</dl>
<h2>Description</h2>
<p><code>mknetid</code></p>
<dd>generates the <i>netid.byname</i> NIS map from the contents of the <a href="/docs/linux/man/5-group/">group</a>(5), <a href="/docs/linux/man/5-passwd/">passwd</a>(5), <a href="/docs/linux/man/5-hosts/">hosts</a>(5) and netid files. It checks for multiple entrys of netids and warn for them or filters them out. It is only called by <i>/var/yp/Makefile</i> when rebuilding the NIS map.</p>
<h2>Options</h2>
<p><code>-q</code></p>
<dl>
<dd>This flag turns on &#8216;quiet&#8217; mode, don&#8217;t print a warning message when finding an duplicate netid entry.</dl>
<p> <code>-h</code><i> hosts</i></p>
<dl>
<dd>The <code>-h</code> flag can be used to specify the use of another hosts file than the default <i>/etc/hosts</i>.</dl>
<p> <code>-p</code><i> passwd</i></p>
<dl>
<dd>The <code>-p</code> flag can be used to specify the use of another passwd file than the default <i>/etc/passwd</i>.</dl>
<p> <code>-g</code><i> group</i></p>
<dl>
<dd>The <code>-g</code> flag can be used to specify the use of another group file than the default <i>/etc/group</i>.</dl>
<p> <code>-n</code><i> netid</i></p>
<dl>
<dd>The <code>-n</code> flag can be used to specify the use of another netid file than the default <i>/etc/netid</i>.</dl>
<p> <code>-d</code><i> domain</i></p>
<dl>
<dd>The <code>mknetid</code> command uses the system domainname by default. If it is not set or you whish to override it, you must use the <code>-d</code> parameter.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Prints the version number</dl>
<h2>Files</h2>
<p><i>/etc/group</i></p>
<dl>
<dd>groups file</dl>
<p> <i>/etc/hosts</i></p>
<dl>
<dd>hosts database</dl>
<p> <i>/etc/netid</i></p>
<dl>
<dd>netname database</dl>
<p> <i>/etc/passwd</i></p>
<dl>
<dd>password file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-passwd/">passwd</a></code>(8), <code><a href="/docs/linux/man/5-group/">group</a></code>(5), <code><a href="/docs/linux/man/5-hosts/">hosts</a></code>(5), <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5)</p>
<h2>Author</h2>
<p><code>mknetid</code> was written by Thorsten Kukuk &lt;kukuk [at] linux-nis.org&gt;.</p>
