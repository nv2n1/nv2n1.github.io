---
title: "fcaps(1)"
name: "fcaps"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fcaps/"
description: "fcaps – report available fontcaps"
---

<h2>NAME</h2>
<p> fcaps &#8211; report available fontcaps</p>
<h2>SYNOPSIS</h2>
<p> <code>fcaps</code> [ <code>-V</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>fcaps</code> is a simple script that reports all the available fontcaps for use in metafile translation by the metafile translator <code>ctrans(1NCARG)</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V</code></p>
<dd> Print the version number and then exit.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>NCARG_ROOT</code></p>
<dd> Path to root of NCAR Graphics installation.</p>
<dt><code>NCARG_LIB</code></p>
<dd> If set this variable contains the path to the installed NCAR Graphics libraries. <code>NCARG_LIB</code> overrides <code>NCARG_ROOT</code>.</dl>
<h2>FILES</h2>
<dl>
<dt>$NCARG_ROOT/lib/ncarg/fontcaps/*</p>
<dd> The fontcaps.</p>
<dt>$NCARG_LIB/ncarg/fontcaps/*</p>
<dd> The fontcaps.</dl>
<h2>SEE ALSO</h2>
<p> <code>gcaps(5NCARG),</code> <code>ctrans(1NCARG),</code> <code>ictrans(1NCARG),</code> <code>fontcap(5NCARG)</code> </p>
<p> Hardcopy: NCAR Graphics Fundamentals, UNIX Version</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research </p>
<p> The use of this Software is governed by a License Agreement. </p>
<h2>Index</h2>
