---
title: "dh_numpy(1)"
name: "dh_numpy"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_numpy/"
description: "dh_numpy – adds Numpy depends to python:Depends substvar"
---

<h2 class="name">NAME</h2>
<p> dh_numpy &#8211; adds Numpy depends to python:Depends substvar </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_numpy</code> [<i>debhelper options</i>]</p>
<h2>DESCRIPTION</h2>
<p> dh_numpy adds information about the correct versioned depends on python-numpy to python:Depends substvar. </p>
<p> This is needed because some Python extensions require strict versioned depends on python-numpy, and using this helper script is the easiest and most consistent way to get them. </p>
<p> The helper script uses the information stored in /usr/share/numpy/versions, and the architecture type of the package, to generate the Depends information; for a detailed description of how the dependencies are generate, please refer to /usr/share/doc/python-numpy/README.DebianMaints .</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is not a part of debhelper (and it&#8217;s provided by python-numpy). </p>
<h2>Index</h2>
