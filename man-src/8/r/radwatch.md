---
title: "radwatch(8)"
name: "radwatch"
section: "8"
letter: "r"
url: "/docs/linux/man/8-radwatch/"
description: "radwatch – wrapper for radiusd"
---

<p>radwatch &#8211; wrapper for radiusd</p>
<h2>Synopsis</h2>
<p><code>radwatch</code> <i>[</i>options<i>]</i></p>
<h2>Description</h2>
<p>This is a wrapper for <i>radiusd</i>. It starts the radius server, then waits for it to terminate, which should never happen. If it does happen, <code>radwatch</code> sends a notification email to <i>root</i> about the event, waits 10 seconds, then restarts the server. </p>
<p> This script <code>SHOULD NOT BE USED</code>! It&#8217;s only here for historical purposes, and WILL be deleted in a future version of the the server. </p>
<p> Please see &#8216;<i>doc/supervise-radiusd.txt</i>&#8216; for info on methods of supervising your radius installation.</p>
<h2>Options</h2>
<p>Passed directly to the radius server &#8211; see the manpage of <code>radiusd</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-radiusd/">radiusd</a>(8).</p>
<h2>Author</h2>
<p>Miquel van Smoorenburg, miquels [at] cistron.nl.</p>
