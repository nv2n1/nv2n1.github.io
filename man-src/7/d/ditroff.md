---
title: "ditroff(7)"
name: "ditroff"
section: "7"
letter: "d"
url: "/docs/linux/man/7-ditroff/"
---

ditroff - classical device-independent roff

<h2>Description</h2>

The name <i>ditroff</i> refers to a historical development stage of the <i><a HREF="/docs/linux/man/7-roff/">roff</a></i>(7) text processing system. In <i>roff</i> systems extant today, the name <i>troff</i> is a synonym for <i>ditroff</i>. 

 Early versions of <i>roff</i> by Joe Ossanna generated two programs from the same sources, using conditional compilation to distinguish them. <i>nroff</i> produced text-oriented TTY output, while <i>troff</i> generated graphical output for exactly one output device, the Wang Graphic Systems CAT phototypesetter. 

 In 1979, Brian Kernighan rewrote <i>troff</i> to support more devices by creating an intermediate output format for <i>troff</i> that could be fed into postprocessor programs which actually do the printout on the device. Kernighan's version marks what is known as "classical troff" today. In order to distinguish it from Ossanna's original version, it was called <i>ditroff</i> (<i>d</i>evice <i>i</i>ndependent <i>t</i>roff) on some systems, though this naming isn't mentioned in the classical documentation. 

 Today, all existing <i>roff</i> systems are based on Kernighan's multi-device <i>troff</i>. The distinction between <i>troff</i> and <i>ditroff</i> is no longer necessary; each modern <i>troff</i> provides the complete functionality of <i>ditroff</i>. 

 The easiest way to use <i>ditroff</i> is via the GNU <i>roff</i> system, <i>groff</i>. The <i><a HREF="/docs/linux/man/1-groff/">groff</a></i>(1) program is a wrapper around <i>(di)troff</i> that automatically handles device postprocessing.

<h2>Authors</h2>

This document was written by Bernd Warken

<h2>See Also</h2>

<dl><dt>CSTR~#54
<dd>refers to the 1992 revision of the <i>Nroff/Troff User's Manual</i> by J. F. Ossanna and Brian Kernighan.
<dt>CSTR~#97
<dd>refers to <i>A Typesetter-independent TROFF</i>, by Brian Kernighan and is the original documentation of the first multi-device <i>troff</i> (<i>ditroff</i>).
<dt><i><a HREF="/docs/linux/man/7-roff/">roff</a></i>(7)
<dd>provides a history and conceptual overview of <i>roff</i> systems.
<dt><i><a HREF="/docs/linux/man/1-troff/">troff</a></i>(1)
<dd>describes the GNU implementation of <i>(di)troff</i>.
<dt><i><a HREF="/docs/linux/man/1-groff/">groff</a></i>(1)
<dd>documents the GNU <i>roff</i> program and includes pointers to further documentation about <i>groff</i>.
<dt><i><a HREF="/docs/linux/man/5-groff_out/">groff_out</a></i>(5)
<dd>describes the <i>groff</i> version of the intermediate output language, the basis for multi-device output. 
