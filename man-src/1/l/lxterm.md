---
title: "lxterm(1)"
name: "lxterm"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxterm/"
description: "lxterm – locale-sensitive wrapper for xterm"
---

<h2 class="name">NAME</h2>
<p> lxterm &#8211; locale-sensitive wrapper for xterm </p>
<h2>SYNOPSIS</h2>
<p> <code>lxterm</code> [ <i>xterm-options</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>lxterm</code> is a wrapper around the <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1) program that invokes <code>xterm</code>, <code><a href="/docs/linux/man/1-koi8rxterm/">koi8rxterm</a></code>(1), or <code><a href="/docs/linux/man/1-uxterm/">uxterm</a></code>(1) as appropriate, based on the user&#8217;s locale setting. All arguments to <code>lxterm</code> are passed to <code>xterm</code> without processing; the <code>-class</code>, <code>-k8</code>, and <code>-u8</code> options should not be specified because they are used by <code>koi8rxterm</code> and <code>uxterm</code>. See the <code>xterm</code> manual page for more information on <i>xterm-options</i>. </p>
<p> The <code><a href="/docs/linux/man/1-locale/">locale</a></code>(1) utility is used to determine the character set used by the current locale. If the character set is UTF-8, <code>uxterm</code> is invoked; if the character set is KOI8-R, <code>koi8rxtem</code> is invoked; otherwise, &#8216;plain&#8217; <code>xterm</code> is invoked.</p>
<h2>AUTHOR</h2>
<p> Branden Robinson</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-locale/">locale</a></code>(1), <code><a href="/docs/linux/man/1-koi8rxterm/">koi8rxterm</a></code>(1), <code><a href="/docs/linux/man/1-uxterm/">uxterm</a></code>(1), <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1) </p>
<h2>Index</h2>
