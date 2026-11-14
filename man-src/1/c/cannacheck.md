---
title: "cannacheck(1)"
name: "cannacheck"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cannacheck/"
description: "cannacheck – Display information about Japanese input system Canna"
---

<h2>NAME</h2>
<p> cannacheck &#8211; Display information about Japanese input system Canna</p>
<h2>SYNOPSIS</h2>
<p> <code>cannacheck [-v]</code></p>
<h2>DESCRIPTION</h2>
<p> cannacheck displays the problems concerning use of Canna and the related information. It examines the following items:</p>
<dl>
<dt>&#8211;</p>
<dd> Customize file to be used</p>
<dt>&#8211;</p>
<dd> Romaji-to-Kana conversion dictionary to be used</p>
<dt>&#8211;</p>
<dd> Destination to which the server is to be connected. Is it connectable?</p>
<dt>&#8211;</p>
<dd> Dictionaries to be mounted. Are they mountable?</p>
<dt>&#8211;</p>
<dd> Errors in the customize file</dl>
<p> The problem(s) are displayed on the standard output if found.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-v</p>
<dd> Displays all the above information including items that contain no problem.</dl>
<h2>FILES</h2>
<dl>
<dt>/etc/canna/cannahost</p>
<dd> Name of the host under which <i><a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M)</i> is in operation.</dl>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M), <a href="//www.systutorials.com/docs/linux/man/1M-cannakill/">cannakill</a>(1M), <a href="/docs/linux/man/1-cannastat/">cannastat</a>(1)</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt>CANNAHOST</p>
<dd> Specifies the name of the host under which <i><a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M)</i> is in operation.</p>
<dt>CANNAFILE</p>
<dd> Specifies the initialize file (.canna). </p>
</dl>
<h2>Index</h2>
