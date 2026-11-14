---
title: "update-grub-gfxpayload(8)"
name: "update-grub-gfxpayload"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-grub-gfxpayload/"
description: "update-grub-gfxpayload – update /boot/grub/gfxblacklist.txt"
---

<p><code>update-grub-gfxpayload</code> &#8211; update /boot/grub/gfxblacklist.txt</p>
<h2>Synopsis</h2>
<p><code>update\-grub\-gfxpayload</code></p>
<h2>Description</h2>
<p><code>update\-grub\-gfxpayload</code> updates /boot/grub/gfxblacklist.txt from source files in /usr/share/grub-gfxpayload-lists/blacklist/ which disables GRUB&#8217;s <code>gfxpayload=keep</code> facility with certain graphics cards. It should normally only need to be called internally by packages. If you need to disable <code>gfxpayload=keep</code> locally (perhaps because your system starts up with a black or corrupt screen), then you do not need this program. Instead, add this line to /etc/default/grub </p>
<h2>Author</h2>
<p>An Colin Watson Aq cjwatson [at] ubuntu.com</p>
