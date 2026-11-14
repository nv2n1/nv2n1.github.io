---
title: "dviselect(1)"
name: "dviselect"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dviselect/"
description: "dviselect – extract pages from DVI files"
---

<h2 class="name">NAME</h2>
<p> dviselect &#8211; extract pages from DVI files </p>
<h2>SYNOPSIS</h2>
<p> <code>dviselect</code> [ <code>-s</code> ] [ <code>-i</code> <i>infile</i> ] [ <code>-o</code> <i>outfile</i> ] <i>list of pages</i> [ <i>infile</i> [ <i>outfile</i> ] ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Dviselect</i> selects pages from a DVI file produced by TeX, creating a new DVI file usable by any of the TeX conversion programs, or even by <i>dviselect</i> itself. </p>
<p> A <i>range</i> is a string of the form <i>even</i>, <i>odd</i>, or <i>first:last</i> where both <i>first</i> and <i>last</i> are optional numeric strings, with negative numbers indicated by a leading underscore character &#8220;_&#8221;. If both <i>first</i> and <i>last</i> are omitted, the colon may also be omitted, or may be replaced with an asterisk &#8220;*&#8221;. A <i>page range</i> is a list of ranges separated by periods. A <i>list of pages</i> is described by a set of page ranges separated by commas and/or white space. </p>
<p> <i>Dviselect</i> actually looks at the ten <i>count</i> variables that TeX writes; the first of these (
