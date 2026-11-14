---
title: "mlmmj-sub(1)"
name: "mlmmj-sub"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mlmmj-sub/"
description: "mlmmj-sub – subscribe address to a mailinglist run by mlmmj"
---

<h2>NAME</h2>
<p> mlmmj-sub &#8211; subscribe address to a mailinglist run by mlmmj</p>
<h2>SYNOPSIS</h2>
<p> <code>mlmmj-sub</code> <i>-L /path/to/list</i> [<i>-a john [at] doe.org</i> | <i>-m str</i>] [<i>-c</i>] [<i>-C</i>] [<i>-d</i> | <i>-n</i>] [<i>-f</i>] [<i>-h</i>] [<i>-q</i>] [<i>-r</i> | <i>-R</i>] [<i>-s</i>] [<i>-U</i>] [<i>-V</i>]</p>
<dl>
<dt> <code>-a</code>: Email address to subscribe</p>
<dt> <code>-c</code>: Send welcome mail (unless requesting confirmation)</p>
<dt> <code>-C</code>: Request mail confirmation (unless switching versions)</p>
<dt> <code>-d</code>: Subscribe to digest version of the list</p>
<dt> <code>-f</code>: Force subscription (do not moderate)</p>
<dt> <code>-h</code>: This help</p>
<dt> <code>-L</code>: Full path to list directory</p>
<dt> <code>-m</code>: Moderation string</p>
<dt> <code>-n</code>: Subscribe to nomail version of the list</p>
<dt> <code>-q</code>: Be quiet (don&#8217;t notify owner about the subscription)</p>
<dt> <code>-r</code>: Behave as if request arrived via email (internal use)</p>
<dt> <code>-R</code>: Behave as if confirmation arrived via email (internal use)</p>
<dt> <code>-s</code>: Don&#8217;t send a mail to the subscriber if already subscribed</p>
<dt> <code>-U</code>: Don&#8217;t switch to the user id of the listdir owner</p>
<dt> <code>-V</code>: Print version</dl>
<h2>DESCRIPTION</h2>
<dd>This utility is used to subscribe people to the specified mailinglist. It will write the email address in a file with the name of the beginning letter of the email address getting subscribed in the &lt;listdir&gt;/subscribers.d/ directory. </p>
<p> The digest version of the list is a list version where people receive postings to the list periodically (e.g. once a day) or when a large number of posts have accumulated. Digest subscribers are in the &lt;listdir&gt;/digesters.d/ directory. </p>
<p> The nomail version of the list is a list version where people are subscribed like usual, but they won&#8217;t receive any postings to the list. This is useful for people who read the mailinglist through a news gateway, but want to be able to post to the list. Nomail subscribers are in the &lt;listdir&gt;/nomailsubs.d/ directory. </p>
<p> Unless the <code>-U</code> switch is used it will switch its user id to the user id owning the list directory. This is done to make sure that new files created are having correct permissions. </p>
<p> If the given address is already subscribed to the list, but to a different version, the subscription is switched to that version, and confirmation and moderation are bypassed. If the address is already subscribed to the version requested, a mail is sent to the subscriber, unless the <code>-s</code> switch is used. </p>
<p> Subscription may be moderated (if &lt;listdir&gt;/control/submod exists) unless the <code>-f</code> switch is given. When a subscription is permitted by a gatekeeper, welcome messages are sent to the subscriber as usual, regardless of options given now. </p>
<p> To ensure subscription is silent from the point of view of the subscriber, use <code>-f</code>, but neither <code>-c</code> nor <code>-C</code>. To inhibit notification of the owner, use <code>-q</code>. Use of <code>-s</code> is recommended to ensure you don&#8217;t spam already-subscribed addresses by accident.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mlmmj-unsub/">mlmmj-unsub</a>(1), <a href="/docs/linux/man/2-setuid/">setuid</a>(2)</p>
<h2>AUTHORS</h2>
<p> This manual page was written by the following persons:</p>
<dl>
<dt>
<dd>S&oslash;ren Boll Overgaard &lt;boll [at] debian.org&gt; (based on html2man output)</p>
<dt>
<dd>Mads Martin J&oslash;rgensen &lt;mmj [at] mmj.dk&gt; </p>
</dl>
<h2>Index</h2>
