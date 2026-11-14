---
title: "expectk(1)"
name: "expectk"
section: "1"
letter: "e"
url: "/docs/linux/man/1-expectk/"
description: "expectk – Expect with Tk support"
---

<h2>NAME</h2>
<p> expectk &#8211; Expect with Tk support</p>
<h2>SYNOPSIS</h2>
<p> <code>expectk</code> [ <i>args</i> ]</p>
<h2>INTRODUCTION</h2>
<p> <code>Expectk</code> is a combination of Expect with Tk. (See their respective man pages for a more comprehensive explanation of either.) <code>Expectk</code> should run any <code>wish</code> or <code>Expect</code> script (with minor changes &#8211; see below). </p>
<p> The differences between the Expectk and Expect environment follows. </p>
<p> The <code>send</code> command is Tk&#8217;s. Expect&#8217;s <code>send</code> command can be invoked by the name <code>exp_send</code>. (For compatibility, Expect allows either <code>send</code> or <code>exp_send</code> to be used.) </p>
<p> Scripts may be invoked implicitly on systems which support the #! notation by marking the script executable, and making the first line in your script: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>#!/usr/local/bin/expectk -f</p>
<p> Of course, the path must accurately describe where <code>Expectk</code> lives. /usr/local/bin is just an example. </p>
<h2>Index</h2>
