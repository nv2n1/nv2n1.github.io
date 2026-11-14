---
title: "tzselect(1)"
name: "tzselect"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tzselect/"
description: "tzselect – view timezones"
---

<h2 class="name">NAME</h2>
<p> tzselect &#8211; view timezones </p>
<h2>SYNOPSIS</h2>
<p> <code>tzselect</code></p>
<h2>DESCRIPTION</h2>
<p> This manual page explains how you can use the <code>tzselect</code> utility to view the installed timezone. It comes handy when you want to know what time it is in other countries, or if you just wonder what timezones exist. </p>
<p> <code>tzselect</code> is called without any parameters from the shell. It shows a list of about one dozen geographic areas one can roughly recognize as continents. After choosing a geographic area by number, a list of countries and cities in this area will be shown. </p>
<p> You can press the <code>Enter</code> key to reprint the list. To choose a timezone, just press the number left to it. If your input is invalid, the list will be reprinted. </p>
<p> You may press <code>Ctrl-C</code> to interrupt the script at any time. </p>
<p> Note that <code>tzselect</code> will not actually change the timezone for you. Use &#8216;dpkg-reconfigure tzdata&#8217; to achieve this.</p>
<h2>FILES</h2>
<p> <i>/usr/share/zoneinfo/</i></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8)</p>
<h2>AUTHOR</h2>
<p> Copyright 1998 Marcus Brinkmann &lt;brinkmd [at] debian.org&gt; </p>
<p> Please see nroff source for legal notice. </p>
<h2>Index</h2>
