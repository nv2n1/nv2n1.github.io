---
title: "cxpm(1)"
name: "cxpm"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cxpm/"
description: "cxpm – Check an XPM (X PixMap) file, versions XPM 1, 2, or 3."
---

<h2 class="name">NAME</h2>
<p> cxpm &#8211; Check an XPM (X PixMap) file, versions XPM 1, 2, or 3. </p>
<h2>SYNOPSIS</h2>
<p> <code>cxpm</code> [<i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>cxpm</code> program can be used to check the format of any XPM (version 1, 2, or 3) file. On error, unlike <code>sxpm</code>, <code>cxpm</code> prints out an error message indicating where the parser choked. This should help finding out what&#8217;s wrong with an XPM file but do not expect too much from it though. This is not even close from being some kind of lint program for XPM. First, it stops at the first error it encounters &#8211; so several fix and retry cycles may be necessary to get your file to parse successfully. Second, <code>cxpm</code> only cares about the format. If, for instance, your pixmap uses too many colors for your system you still may experience difficulties displaying it. Be warned. </p>
<p> When no <i>filename</i> is given <code>cxpm</code> reads from the standard input.</p>
<h2>AUTHOR</h2>
<p> Arnaud Le Hors (lehors [at] sophia.inria.fr)<br />
 Copyright (C) 1998 by Arnaud LE HORS. </p>
<h2>Index</h2>
