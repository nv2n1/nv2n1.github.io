---
title: "i3lock(1)"
name: "i3lock"
section: "1"
letter: "i"
url: "/docs/linux/man/1-i3lock/"
description: "i3lock – slightly improved version of slock"
---

<h2 class="name">NAME</h2>
<p> i3lock &#8211; slightly improved version of slock</p>
<h2>SYNOPSIS</h2>
<p> <code>i3lock</code> [-v] [-n] [-b] [-d] </p>
<h2>DESCRIPTION</h2>
<p> <code>i3lock</code> locks your screen by making it white. To quit <code>i3lock</code> just enter your password. </p>
<h2>DIFFERENCES TO SLOCK</h2>
<p> <code>i3lock</code> improves slock by making it fork() and therefore combinable with commands to suspend your computer. Additionally, instead of turning off your screen via DPMS and/or displaying a black screen, <code>i3lock</code> displays a white screen so you can see if your computer failed to resume from suspend or if your screen is just locked. Also, when entering a wrong password, <code>i3lock</code> does not call XBell(). This is important because <code>i3lock/slock</code> think you&#8217;ve entered a password when resuming from suspend, at least sometimes. </p>
<p> Since version 1.0, i3lock supports PAM. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v, &#8211;version</code></p>
<dd> Display the version of your <code>i3lock</code> </p>
<dt><code>-n, &#8211;nofork</code></p>
<dd> Don&#8217;t fork after starting. </p>
<dt><code>-b, &#8211;beep</code></p>
<dd> Enable beeping. Be sure to not do this when you are about to annoy other people, like when opening your laptop in a boring lecture. </p>
<dt><code>-d, &#8211;dpms</code></p>
<dd> Enable turning off your screen using DPMS. Note that, when you do not specify this option, DPMS will turn off your screen after 15 minutes of inactivity anyways (if you did not disable this in your X server). </p>
</dl>
<h2>AUTHOR</h2>
<p> Michael Stapelberg &lt;michael+i3lock at stapelberg dot de&gt; </p>
<p> forked from slock-0.9 by Anselm R Garbe &lt;garbeam at gmail dot com&gt; </p>
<h2>Index</h2>
