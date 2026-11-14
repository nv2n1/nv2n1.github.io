---
title: "kbdrate(8)"
name: "kbdrate"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kbdrate/"
description: "kbdrate – reset the keyboard repeat rate and delay time"
---

<p>kbdrate &#8211; reset the keyboard repeat rate and delay time</p>
<h2>Synopsis</h2>
<p><code>kbdrate</code> [<i>,options/</i>&#8230;]</p>
<h2>Description</h2>
<p><code>kbdrate</code> is used to change the keyboard repeat rate and delay time. The delay is the amount of time that a key must be depressed before it will start to repeat. Using <code>kbdrate</code> without any options will reset the repeat rate to 10.9 characters per second (cps) and the delay to 250 milliseconds (ms) for Intel- and M68K-based systems. These are the IBM defaults. On SPARC-based systems it will reset the repeat rate to 5 cps and the delay to 200 ms. </p>
<h2>Options</h2>
<dl>
<dt><code>-r</code>, <code>&#8211;rate</code>=<i>,NUMBER/</i></p>
<dd>Change the keyboard repeat rate to <i>NUMBER</i> cps. For Intel-based systems, the allowable range is from 2.0 to 30.0 cps. Only certain, specific values are possible, and the program will select the nearest possible value to the one specified. The possible values are given, in characters per second, as follows: 2.0, 2.1, 2.3, 2.5, 2.7, 3.0, 3.3, 3.7, 4.0, 4.3, 4.6, 5.0, 5.5, 6.0, 6.7, 7.5, 8.0, 8.6, 9.2, 10.0, 10.9, 12.0, 13.3, 15.0, 16.0, 17.1, 18.5, 20.0, 21.8, 24.0, 26.7, 30.0. For SPARC-based systems, the allowable range is from 0 (no repeat) to 50 cps.</p>
<dt><code>-d</code>, <code>&#8211;delay</code>=<i>,NUMBER/</i></p>
<dd>Change the delay to <i>NUMBER</i> milliseconds. For Intel-based systems, the allowable range is from 250 to 1000 ms, in 250 ms steps. For SPARC systems, possible values are between 10 ms and 1440 ms, in 10 ms steps.</p>
<dt><code>-s</code>, <code>&#8211;silent</code></p>
<dd>Silent. No messages are printed.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display a help text.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Display a version number and exit.</dl>
<h2>Bugs</h2>
<p>Not all keyboards support all rates. </p>
<p> Not all keyboards have the rates mapped in the same way. </p>
<p> Setting the repeat rate on the Gateway AnyKey keyboard does not work. If someone with a Gateway figures out how to program the keyboard, please send mail to util-linux [at] math.uio.no. </p>
<p> All this is very architecture dependent. Nowadays <code>kbdrate</code> first tries the KDKBDREP and KIOCSRATE ioctls. (The former usually works on an m68k/i386 machine, the latter for SPARC.) When these ioctls fail an ioport interface.</p>
<h2>Files</h2>
<p><i>/etc/rc.local</i><br />
 <i>/dev/port</i></p>
