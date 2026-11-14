---
title: "pkaction(1)"
name: "pkaction"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pkaction/"
description: "pkaction – Get details about a registered action"
---

<h2 class="name">NAME</h2>
<p> pkaction &#8211; Get details about a registered action </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pkaction</code> [<code>&#8211;version</code>] [<code>&#8211;help</code>]</p>
<dt> <code>pkaction</code> [<code>&#8211;verbose</code>]</p>
<dt> <code>pkaction</code> <code>&#8211;action-id</code>&nbsp;<i>action</i> [<code>&#8211;verbose</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>pkaction</code></p>
<dd>is used to obtain information about registered PolicyKit actions. If called with <code>&#8211;action-id</code> then all actions are displayed. Otherwise the action <i>action</i>. If called without the <code>&#8211;verbose</code> option only the name of the action is shown. Otherwise details about the actions are shown.</p>
<h2>RETURN VALUE</h2>
<p> On success <code>pkaction</code> returns 0. Otherwise a non-zero value is returned and a diagnostic message is printed on standard error.</p>
<h2>AUTHOR</h2>
<p> Written by David Zeuthen &lt;davidz [at] redhat.com&gt; with a lot of help from many others.</p>
<h2>BUGS</h2>
<p> Please send bug reports to either the distribution or the polkit-devel mailing list, see the link m[blue]<code><a rel="nofollow" href="http://lists.freedesktop.org/mailman/listinfo/polkit-devel">http://lists.freedesktop.org/mailman/listinfo/polkit-devel</a></code>m[] on how to subscribe.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-polkit/">polkit</a></code>(8), <code><a href="/docs/linux/man/1-pkcheck/">pkcheck</a></code>(1), <code><a href="/docs/linux/man/1-pkexec/">pkexec</a></code>(1), <code><a href="/docs/linux/man/1-pkttyagent/">pkttyagent</a></code>(1) </p>
<h2>Index</h2>
