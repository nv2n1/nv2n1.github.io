---
title: "expirerm(8)"
name: "expirerm"
section: "8"
letter: "e"
url: "/docs/linux/man/8-expirerm/"
description: "expirerm – Remove articles that have been expired"
---

<p>expirerm &#8211; Remove articles that have been expired</p>
<h2>Synopsis</h2>
<p><code>expirerm</code> <i>file</i></p>
<h2>Description</h2>
<p><code>expirerm</code> is a script that removes a list of files. The specified <i>file</i> lists the files to be removed. It is usually created by <code>expire -z</code>. This file is sorted, and then fed into a pipeline responsible for doing the removal, normally <code>fastrm</code>. (You may want to edit <code>expirerm</code> to change the flags passed to <code>fastrm</code>.) </p>
<p> If there seemed to be a problem removing the files, then a mail is sent to the news administrator. If there were no problems, then <i>file</i> is renamed to <i>pathlog</i>/expire.list where it is kept (for safety) until the next time expiration is done.</p>
<h2>History</h2>
<p>Written by Landon Curt Noll &lt;chongo [at] toad.com&gt; and Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt;. Converted to <font SIZE="-1">POD</font> by Julien Elie. </p>
<p> <tt>$Id:</tt> expirerm.pod 8577 2009-08-18 14:02:02Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-expire/">expire</a></i>(8), <i><a href="/docs/linux/man/8-fastrm/">fastrm</a></i>(8), <i><a href="/docs/linux/man/5-newslog/">newslog</a></i>(5). </p>
