---
title: "rtpr(8)"
name: "rtpr"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rtpr/"
description: "rtpr – replace backslashes with newlines."
---

<p>rtpr &#8211; replace backslashes with newlines.</p>
<h2>Description</h2>
<p><code>rtpr</code> is a trivial shell script which converts backslashes in standard input to newlines. It&#8217;s sole purpose is to be fed with input from <code>ip</code> when executed with it&#8217;s <code>&#8211;oneline</code> flag. </p>
<h2>Examples</h2>
<dl>
<dt>ip &#8211;oneline address show | rtpr</p>
<dd>Undo oneline converted <code>ip-address</code> output. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8) </p>
<h2>Authors</h2>
<p>Stephen Hemminger &lt;shemming [at] brocade.com&gt;</p>
