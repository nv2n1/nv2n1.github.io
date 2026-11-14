---
title: "xdmxconfig(1)"
name: "xdmxconfig"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xdmxconfig/"
description: "xdmxconfig – a graphical configuration tool for Xdmx configuration files"
---

<h2>NAME</h2>
<p> xdmxconfig &#8211; a graphical configuration tool for Xdmx configuration files</p>
<h2>SYNOPSIS</h2>
<p> <code>xdmxconfig</code> [filename]</p>
<h2>DESCRIPTION</h2>
<p> <i>xdmxconfig</i> reads, edits, and writes configuration files for the Xdmx server. The grammar for the configuration file is specified in the <a href="/docs/linux/man/1-xdmx/">Xdmx</a>(1) manual page. </p>
<p> To start from scratch, create a &quot;New Global&quot; and specify the name and overall dimensions for the configuration. Then use &quot;New Display&quot; to enter more displays. </p>
<p> If there is more than one configuration, the configuration name button will bring up a selection menu. </p>
<p> In the right-hand pannel, the left mouse button will move the highlighted display at &quot;tool resolution&quot;; the middle mouse button will move the highlighted display by a single pixel (at &quot;wall resolution&quot;); and the right mouse button will bring up a menu allowing the highlighted display to be edited or deleted. The arrow keys will also move the highlighted display by a single pixel.</p>
<h2>BUGS</h2>
<p> Currently, entries with the <code>wall</code> keyword are not editable, but will be preserved in the new output file. The tool will quit when requested by the user, even if a configuration file has not been written out (i.e., without warning). The menu interaction should be improved (menu entries that don&#8217;t currently work should be greyed-out, for example). The Help button does not work.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xdmx/">Xdmx</a>(1), <a href="/docs/linux/man/1-vdltodmx/">vdltodmx</a>(1) </p>
<h2>Index</h2>
