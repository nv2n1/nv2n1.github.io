---
title: "mlmmj-unsub(1)"
name: "mlmmj-unsub"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mlmmj-unsub/"
description: "mlmmj-unsub – unsubscribe address from a mailinglist run by mlmmj"
---

<h2>NAME</h2>
<p> mlmmj-unsub &#8211; unsubscribe address from a mailinglist run by mlmmj</p>
<h2>SYNOPSIS</h2>
<p> <code>mlmmj-unsub</code> <i>-L /path/to/list -a john [at] doe.org</i> [<i>-b</i>] [<i>-c</i> | <i>-C</i>] [<i>-d</i> | <i>-n</i> | <i>-N</i>] [<i>-h</i>] [<i>-q</i>] [<i>-r</i> | <i>-R</i>] [<i>-s</i>] [<i>-U</i>] [<i>-V</i>]</p>
<dl>
<dt> <code>-a</code>: Email address to unsubscribe</p>
<dt> <code>-b</code>: Behave as if unsubscription is due to bouncing (internal use)</p>
<dt> <code>-c</code>: Send goodbye mail</p>
<dt> <code>-C</code>: Request mail confirmation</p>
<dt> <code>-d</code>: Unsubscribe from the digest version of the list</p>
<dt> <code>-h</code>: This help</p>
<dt> <code>-L</code>: Full path to list directory</p>
<dt> <code>-n</code>: Unsubscribe from the nomail version of the list</p>
<dt> <code>-N</code>: Unsubscribe from the normal version of the list</p>
<dt> <code>-q</code>: Be quiet (don&#8217;t notify owner about the unsubscribe)</p>
<dt> <code>-r</code>: Behave as if request arrived via email (internal use)</p>
<dt> <code>-R</code>: Behave as if confirmation arrived via email (internal use)</p>
<dt> <code>-s</code>: Don&#8217;t send a mail to the address if not subscribed</p>
<dt> <code>-U</code>: Don&#8217;t switch to the user id of the listdir owner</p>
<dt> <code>-V</code>: Print version</dl>
<h2>DESCRIPTION</h2>
<dd>This utility is used to unsubscribe people from the specified mailinglist. It will remove the specified email address from every file in the &lt;listdir&gt;/subscribers.d/, &lt;listdir&gt;/digesters.d/ and &lt;listdir&gt;/nomailsubs.d/ directories (or if the -d, -n or -N switch is given, only the one relevant directory). </p>
<p> Unless the <code>-U</code> switch is used it will switch its user id to the user id owning the list directory. This is done to make sure that new files created are having correct permissions. </p>
<p> Normally a mail is sent to the person being unsubscribed if the address is not subscribed to the list. If the <code>-s</code> switch is used such a mail will not be sent. </p>
<p> When neither <code>-c</code> nor <code>-C</code> is specified, unsubscription happens silently from the point of view of the subscriber. When <code>-q</code> is specified, unsubscription happens silently from the point of view of the list owner. Use of <code>-s</code> is recommended to ensure you don&#8217;t spam unsubscribed addresses by accident.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mlmmj-sub/">mlmmj-sub</a>(1)</p>
<h2>AUTHORS</h2>
<p> This manual page was written by the following persons:</p>
<dl>
<dt>
<dd>S&oslash;ren Boll Overgaard &lt;boll [at] debian.org&gt; (based on html2man output)</p>
<dt>
<dd>Mads Martin J&oslash;rgensen &lt;mmj [at] mmj.dk&gt; </p>
</dl>
<h2>Index</h2>
