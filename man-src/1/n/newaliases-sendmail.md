---
title: "newaliases-sendmail(1)"
name: "newaliases-sendmail"
section: "1"
letter: "n"
url: "/docs/linux/man/1-newaliases-sendmail/"
description: "newaliases – rebuild the data base for the mail aliases file"
---

<p>newaliases &#8211; rebuild the data base for the mail aliases file</p>
<h2>Synopsis</h2>
<p><code>newaliases</code></p>
<h2>Description</h2>
<p><code>Newaliases</code> rebuilds the random access data base for the mail aliases file /etc/aliases. It must be run each time this file is changed in order for the change to take effect. </p>
<p> <code>Newaliases</code> is identical to &#8220;sendmail -bi&#8221;. </p>
<p> The <code>newaliases</code> utility exits 0 on success, and &gt;0 if an error occurs. </p>
<p> Notice: do <code>not</code> use <code>makemap</code> to create the aliases data base, because <code>newaliases</code> puts a special token into the data base that is required by <code>sendmail.</code></p>
<h2>Files</h2>
<dl COMPACT>
<dt>/etc/aliases</p>
<dd>The mail aliases file</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-aliases/">aliases</a>(5), <a href="/docs/linux/man/8-sendmail/">sendmail</a>(8)</p>
<h2>History</h2>
<p>The <code>newaliases</code> command appeared in 4.0BSD.</p>
