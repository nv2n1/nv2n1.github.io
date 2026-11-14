---
title: "vboxctrl(1)"
name: "vboxctrl"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vboxctrl/"
description: "vboxctrl – control vbox functions"
---

<h2 class="name">NAME</h2>
<p> vboxctrl &#8211; control vbox functions</p>
<h2>SYNOPSIS</h2>
<p> <code>vboxctrl</code> [{-c | -r}] {-a | -n | -p | -j} [-s spool]<br />
 <code>vboxctrl</code> -v </p>
<h2>DESCRIPTION</h2>
<p> <code>vboxctrl</code> controls a number of vbox functions. The user&#8217;s password is asked before performing the requested action.</p>
<h3>OPTIONS</h3>
<dl>
<dt><i>-c, &#8211;create</i></p>
<dd> Creates a control file.</p>
<dt><i>-r, &#8211;remove</i></p>
<dd> Removes a control file (default).</p>
<dt><i>-n, &#8211;answernow</i></p>
<dd> Control file &quot;vboxctrl-answernow&quot;.</p>
<dt><i>-a, &#8211;answerall</i></p>
<dd> Control file &quot;vboxctrl-answerall&quot;.</p>
<dt><i>-p, &#8211;stop</i></p>
<dd> Control file &quot;vboxctrl-stop&quot;.</p>
<dt><i>-j, &#8211;reject</i></p>
<dd> Control file &quot;vboxctrl-reject&quot;.</p>
<dt><i>-s, &#8211;spooldir</i></p>
<dd> Spooldirectory in which to create/remove control files.</p>
<dt><i>-v, &#8211;version</i></p>
<dd> Displays package version.</p>
<dt><i>-h, &#8211;help</i></p>
<dd> Displays a usage message.</dl>
<p> The spool directory is taken from one of the following:</p>
<dl>
<dt><i>1</i></p>
<dd> the default builtin value</p>
<dt><i>2</i></p>
<dd> The value of the environment variable VBOXSPOOL, if set.</p>
<dt><i>3</i></p>
<dd> The directory of the command line option &quot;&#8211;spooldir&quot;. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-vbox/">vbox</a>(1), <a href="/docs/linux/man/8-vboxd/">vboxd</a>(8)</code> </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Paul Slootman &lt;paul [at] debian.org&gt;, for Debian GNU/Linux and isdn4linux. </p>
<h2>Index</h2>
