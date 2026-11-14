---
title: "pbmpscale(1)"
name: "pbmpscale"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmpscale/"
---

<h2 class="name">NAME</h2>
 

 pbmpscale - enlarge a portable bitmap with edge smoothing 

<h2>SYNOPSIS</h2>

 pbmpscale N [ pbmfile ]

<h2>DESCRIPTION</h2>

 Reads a portable bitmap as input, and outputs a portable bitmap enlarged N times. Enlargement is done by pixel replication, with some additional smoothing of corners and edges.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-pnmenlarge/">pnmenlarge</a>(1), <a HREF="/docs/linux/man/1-ppmscale/">ppmscale</a>(1), <a HREF="/docs/linux/man/5-pbm/">pbm</a>(5)

<h2>AUTHOR</h2>

 Copyright (C) 1990 by Angus Duggan Copyright (C) 1989 by Jef Poskanzer. 

 Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. This software is provided &quot;as is&quot; without express or implied warranty.

<h2>NOTES</h2>

 pbmpscale works best for enlargements of 2. Enlargements greater than 2 should be done by as many enlargements of 2 as possible, followed by an enlargement by the remaining factor. 

<h2>Index</h2>


