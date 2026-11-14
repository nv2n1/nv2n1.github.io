---
title: "forward(5)"
name: "forward"
section: "5"
letter: "f"
url: "/docs/linux/man/5-forward/"
description: "forward – email forwarding information file"
---

<p><code>forward</code> &#8211; email forwarding information file</p>
<h2>Description</h2>
<p>Users may put a <code>.forward</code> file in their home directory. If this file exists, <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8) forwards email to the destinations specified therein. </p>
<p> A <code>.forward</code> file contains a list of expansion values, as described in <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5). Each expansion value should be on a line by itself. However, the <code>.forward</code> mechanism differs from the aliases mechanism in that it disallows file inclusion (:include:) and it performs expansion under the user ID of the <code>.forward</code> file owner. </p>
<p> Permissions on the <code>.forward</code> file are very strict and expansion is rejected if the file is group or world-writable; if the home directory is group writeable; or if the file is not owned by the user. </p>
<p> Users should avoid editing directly the <code>.forward</code> file to prevent delivery failures from occurring if a message arrives while the file is not fully written. The best option is to use a temporary file and use the <code><a href="/docs/linux/man/1-mv/">mv</a></code>(1) command to atomically overwrite the former <code>.forward</code>. Alternatively, setting the <code><a href="/docs/linux/man/8-sticky/">sticky</a></code>(8) bit on the home directory will cause the <code>.forward</code> lookup to return a temporary failure, causing mails to be deferred.</p>
<h2>Files</h2>
<dl>
<dd>
<dl>
<dt><code>~/.forward</code></p>
<dd>Email forwarding information.</dl>
</dl>
<h2>Examples</h2>
<p>The following file forwards mail to &#8220;user [at] example.com&#8221;, and pipes the same mail to &#8220;examplemda&#8221;.</p>
<dl>
<dd>
<pre># empty lines are ignored
user [at] example.com # anything after # is ignored
&quot;|/path/to/examplemda&quot;
</dl></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5), <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8) </p>
