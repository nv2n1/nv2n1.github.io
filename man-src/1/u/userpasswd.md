---
title: "userpasswd(1)"
name: "userpasswd"
section: "1"
letter: "u"
url: "/docs/linux/man/1-userpasswd/"
description: "userpasswd – A graphical tool to allow users to change their passwords."
---

<h2>NAME</h2>
<p> userpasswd &#8211; A graphical tool to allow users to change their passwords.</p>
<h2>SYNOPSIS</h2>
<p> <code>userpasswd</code> [ <i>options</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>userpasswd</code> is a graphical tool to allow users to easily change their passwords. Aside from being a nice GUI frontend, this program does the right thing when the pam configuration has changed.</p>
<h2>OPTIONS</h2>
<p> This program has no command line options of its own, but it does take the standard X program options like <code>-display</code> and such. See the <i><a href="/docs/linux/man/1-x/">X</a></i>(1) man page for some of the common options.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-userhelper/">userhelper</a></i>(8)</p>
<h2>BUGS</h2>
<p> No known bugs, but compatibility with bizarre changes in the pam configuration have not been tested aggressively. If you have a non-standard pam configuration, I&#8217;d be interested to hear whether it worked and what kind of configuration you have.</p>
<h2>AUTHOR</h2>
<p> Otto Hammersmith &lt;otto [at] redhat.com&gt; </p>
<h2>Index</h2>
