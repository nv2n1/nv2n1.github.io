---
title: "cannakill(1)"
name: "cannakill"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cannakill/"
description: "cannakill – Terminate operation of the Kana-Kanji conversion server cannaserver"
---

<h2>NAME</h2>
<p> cannakill &#8211; Terminate operation of the Kana-Kanji conversion server cannaserver</p>
<h2>SYNOPSIS</h2>
<p> <code>cannakill</code></p>
<h2>DESCRIPTION</h2>
<p> cannakill terminates operation of Kana-Kanji conversion server <a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M). This causes the server to delete the socket and close all open dictionaries before terminating its processing. </p>
<p> The user who has started <a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M) or the super user can only use <a href="//www.systutorials.com/docs/linux/man/1M-cannakill/">cannakill</a>(1M) to terminate operation of canncannaer.</p>
<h2>FILES</h2>
<dl>
<dt>/var/run/.iroha_unix/IROHA[:num]</p>
<dd> Socket</dl>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M), <a href="/docs/linux/man/1-cannastat/">cannastat</a>(1), <a href="/docs/linux/man/1-cannacheck/">cannacheck</a>(1) </p>
<h2>Index</h2>
