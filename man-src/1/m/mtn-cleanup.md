---
title: "mtn-cleanup(1)"
name: "mtn-cleanup"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mtn-cleanup/"
description: "mtn-cleanup – generate shell variables from monotone workspace options"
---

<h2>NAME</h2>
<p> mtn-cleanup &#8211; generate shell variables from monotone workspace options</p>
<h2>SYNOPSIS</h2>
<p> <code>mtn-cleanup</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>mtn-cleanup</code> returns a workspace to its pristine state with the minimum of change; missing files are restored, changed files are reverted and new files are removed.</p>
<h2>BUGS</h2>
<p> <code>mtn-cleanup</code> doesn&#8217;t look to see if the database happens to be somewhere in the workspace, and might therefore remove it. Future version may take a look at <i>_MTN/options</i> to check for this possibility.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mtn/">mtn</a></code>(1),</p>
<h2>AUTHOR</h2>
<p> Written by Anthony Edward Cooper &lt;aecooper [at] coosoft.plus.com&gt;. </p>
<h2>Index</h2>
