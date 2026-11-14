---
title: "vlc-wrapper(1)"
name: "vlc-wrapper"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vlc-wrapper/"
description: "vlc-wrapper – a wrapper to drop privileges with VLC"
---

<h2 class="name">NAME</h2>
<p> vlc-wrapper &#8211; a wrapper to drop privileges with VLC </p>
<h2>SYNOPSIS</h2>
<p> <code>vlc-wrapper</code> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>VLC</code> wrapper to open privileged network ports. The ports it can open are 80, 443 and 554. </p>
<h2>OPTIONS</h2>
<p> They will be passed to <code>VLC</code> with no modification. </p>
<h2>USAGE</h2>
<p> The preferred way is to use <code>sudo</code> : </p>
<p> $ sudo vlc-wrapper &#8211;option1 &#8211;option2 </p>
<p> You can also set the SUDO_UID environment variable: </p>
<p> # SUDO_UID=1000 vlc-wrapper &#8211;option1 &#8211;option2 </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-vlc/">vlc</a></code>(1), <code><a href="/docs/linux/man/8-sudo/">sudo</a></code>(8) </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Christophe Mutricy. </p>
<h2>Index</h2>
