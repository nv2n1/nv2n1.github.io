---
title: "ncl_ngckop(3)"
name: "ncl_ngckop"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ngckop/"
---

<pre><code>NGCKOP - a function to check if a specified GKS workstation is open.</code></pre>
<h2>Synopsis</h2>INTEGER FUNCTION NGCKOP(WKID)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 int c_ngckop(int wkid)
<h2>Description</h2><dl COMPACT><dt>WKID
<dd>(an input variable of type INTEGER) specifying a GKS workstation identifier.</dl><h2>C-Binding Description</h2>The C binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>The function returns a &quot;1&quot; if the workstation identified by WKID is open, otherwise it returns a &quot;0&quot;.
<h2>Examples</h2><pre><code>IOPEN = NGCKOP(WKID)


sets IOPEN to &quot;1&quot; if WKID is open and sets IOPEN to &quot;0&quot; otherwise.</code></pre>
<h2>Access</h2>To use NGCKOP or c_ngckop, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online URL: <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/gks/gkshome.html">http://ngwww.ucar.edu/ngdoc/ng/gks/gkshome.html</a>
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
