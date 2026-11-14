---
title: "gpt_build_config(8)"
name: "gpt_build_config"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gpt_build_config/"
description: "gpt_build_config – Returns a minimized list of ldflags from a list of globus packages and external libraries."
---

<p><code>gpt_build_config</code> &#8211; Returns a minimized list of ldflags from a list of globus packages and external libraries.</p>
<h2>Synopsis</h2>
<p>gpt_build_config -src &lt;source metadata file&gt; -f &lt;globus_flavor_name&gt; -link [static|shared]</p>
<h2>Description</h2>
<p><code>gpt_build_config</code> creates a file in it&#8217;s current directory named gpt_build_temp.sh that contains a list of necessary flags assembled from the build environment metadata of the packages on which the source metadata depends. This scanning is done recursively to cover the entire dependency tree. This script was initially inspired by the shell script gnome_config.</p>
<h2>Link Order</h2>
<p>The flag list returned by <code>gpt_build_config</code> is assembled in dependent order. A dependency between two libraries occurs when one library needs the symbols of another library in order to link correctly. For most linkers the library providing the symbols has to be linked after the library that needs the symbols. For example, from the line: </p>
<pre> -L/opt/Xpm/lib -lXpm -L/usr/lib/X11 -lXm -lX</pre>
<p><code>gpt_build_config</code> assumes that the library Xpm is dependent on Xm which in turn is dependent on X. In addition, <code>gpt_build_config</code> assumes that Xpm is located in /opt/Xpm/lib and Xm and X are both located in /usr/lib/X11.</p>
<h2>Bugs</h2>
<p>Circular dependencies between libraries are not supported.</p>
<h2>Author</h2>
<p>Michael Bletzinger &lt;mbletzin.ncsa.uiuc.edu&gt; and Eric Blau &lt;eblau.ncsa.uiuc.edu&gt;</p>
