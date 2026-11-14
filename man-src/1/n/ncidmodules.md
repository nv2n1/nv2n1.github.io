---
title: "ncidmodules(1)"
name: "ncidmodules"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncidmodules/"
description: "ncid-kpopup – Popup Caller ID using KDE"
---

<h2>NAME</h2>
<p> <code>ncid-kpopup</code> &#8211; Popup Caller ID using KDE </p>
<p> <code>ncid-page</code> &#8211; send Caller ID to a pager or cell phone </p>
<p> <code>ncid-samba</code> &#8211; send Caller ID to samba to create a popup </p>
<p> <code>ncid-speak</code> &#8211; send Caller ID to a text-to-speach program </p>
<p> <code>ncid-mythtv</code> &#8211; display Caller ID on MythTV using mythtvosd </p>
<p> <code>ncid-skel</code> &#8211; display Caller ID on stdout in a terminal window </p>
<p> <code>ncid-tivo</code> &#8211; display Caller ID on TiVo using text2osd </p>
<p> <code>ncid-yac</code> &#8211; Send Caller ID to YAC listeners</p>
<h2>SYNOPSIS</h2>
<p> ncid &#8211;no-gui [&#8211;ring #] [&#8211;message] &#8211;call-prog &#8211;program <code>ncid-page</code> </p>
<p> ncid &#8211;no-gui [&#8211;message] &#8211;call-prog &#8211;program <code>ncid-kpopup</code> </p>
<p> ncid &#8211;no-gui [&#8211;message] &#8211;call-prog &#8211;program <code>ncid-samba</code> </p>
<p> ncid &#8211;no-gui [&#8211;message] &#8211;call-prog &#8211;program <code>ncid-speak</code> </p>
<p> ncid &#8211;no-gui [&#8211;message] &#8211;call-prog &#8211;program <code>ncid-mythtv</code> </p>
<p> ncid &#8211;no-gui [&#8211;message] &#8211;call-prog &#8211;program <code>ncid-skel</code> </p>
<p> ncid &#8211;no-gui [&#8211;message] &#8211;call-prog &#8211;program <code>ncid-tivo</code> </p>
<p> ncid &#8211;no-gui [&#8211;message] &#8211;call-prog &#8211;program <code>ncid-yac</code></p>
<h2>DESCRIPTION</h2>
<p> These are ncid output modules and are normally located in the <code>/usr/share/ncid</code> directory. </p>
<p> The client, <code>ncid</code>, can be configured to call any one module. It cannot call multiple modules, but multiple <code>ncid</code> clients can be used each calling a different output module. </p>
<p> The ncid-skel output module is used as a template for writing a shell script output module. All it does is send the Caller ID data to standard output. This makes it useful for troubleshooting. </p>
<p> Each output module can be independently configured using <i>/etc/ncid/ncidmodules.conf</i></p>
<h2>FILES</h2>
<p> /etc/ncid/ncidmodules.conf</p>
<h2>SEE ALSO</h2>
<p> ncid.1, ncidmodules.conf.5, ncidd.8 </p>
<h2>Index</h2>
