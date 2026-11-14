---
title: "mksimnodedir(1)"
name: "mksimnodedir"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mksimnodedir/"
description: "mkSimNodeDir – Create a /proc like files for a simulated node"
---

<p><code>mkSimNodeDir</code> &#8211; Create a /proc like files for a simulated node</p>
<h2>Synopsys</h2>
<p>mkSimNodeDir -n node-name [-g sim-guids-file]</p>
<h2>Description</h2>
<p>This utility build the /proc like file tree for the given node based on the guids dump file produced by the simulator.</p>
<h2>Arguments</h2>
<dl COMPACT>
<dt>-n node-name</p>
<dd>The node name to create the files for.</p>
<dt>-g sim-guids-file</p>
<dd>Dump file to use. default is ./ibmgtsim.guids.txt</dl>
<h2>Limitations</h2>
<p>Only HCAs are supported. </p>
<p> Single <font SIZE="-1">HCA</font> per guid.</p>
<h2>Author</h2>
<p>Eitan Zahavi, Mellanox Technologies <font SIZE="-1">LTD</font>, eitan [at] mellanox.co.il</p>
