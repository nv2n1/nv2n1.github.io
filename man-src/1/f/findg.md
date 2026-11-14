---
title: "findg(1)"
name: "findg"
section: "1"
letter: "f"
url: "/docs/linux/man/1-findg/"
description: "findg – locates calls to all entries in pre-GKS NCAR Graphics"
---

<h2>NAME</h2>
<p> findg &#8211; locates calls to all entries in pre-GKS NCAR Graphics</p>
<h2>SYNOPSIS</h2>
<p> <code>findg &lt;fortran-file</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>findg</code> reads an input FORTRAN file, <i>fortran-file</i>, from the standard input and prints out those lines (along with line numbers) which contain calls to old plotting entries from the pre-GKS NCAR plot package. In conversions to GKS, the user should examine these calls for possible changes. Many entries will require no change. For details on needed changes, see the &quot;Conversion Guide&quot; section of the Version 2.00 User&#8217;s Guide. </p>
<p> If the single character $ is read in column 1 of any input line, then a complete list of the entry points being searched for is printed, and execution is terminated.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1987-2002<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement. </p>
<h2>Index</h2>
