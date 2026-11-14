---
title: "arcplugin(1)"
name: "arcplugin"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arcplugin/"
description: "arcplugin – ARC plugin management utility"
---

<h2 class="name">NAME</h2>
<p> arcplugin &#8211; ARC plugin management utility</p>
<h2>DESCRIPTION</h2>
<p> The <code>arcplugin</code> command prints description of ARC plugin or creates ARC Plugin Descriptor (APD) file. </p>
<h2>SYNOPSIS</h2>
<p> <code>arcplugin [-c] [-r] [-p priority,regex] [-h] plugin_path [plugin_path [&#8230;]]</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&nbsp;<wbr>-h </code></p>
<dd> Prints help message and exits.</p>
<dt><code>&nbsp;<wbr>-c </code></p>
<dd> If specified then APD file is created using same name as ARC plugin with suffix. replaced with .apd.</p>
<dt><code>&nbsp;<wbr>-r </code></p>
<dd> If specified operation is fully recursive.</p>
<dt><code>&nbsp;<wbr>-p </code></p>
<dd> Defines which priority to be assigned for each plugin. Each plugin&#8217;s kind and name attributes are matched specified regex. One which matches gets specified This option can be specified multiple times. Priority is 32 bit positive integer. Default value is 128.</p>
<dt><code>&nbsp;<wbr>plugin_path </code></p>
<dd> full path to ARC plugin loadable module file or directory containing such modules. In last case operation will recurse once into that directory. For fully recursive operation use -r.</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="http://bugzilla.nordugrid.org">http://bugzilla.nordugrid.org</a> </p>
<h2>COPYRIGHT</h2>
<p> APACHE LICENSE Version 2.0 </p>
<h2>AUTHOR</h2>
<p> ARC software is developed by the NorduGrid Collaboration (<a rel="nofollow" href="http://www.nordugrid.org">http://www.nordugrid.org</a>), please consult the AUTHORS file distributed with ARC. Please report bugs and feature requests to <a rel="nofollow" href="http://bugzilla.nordugrid.org">http://bugzilla.nordugrid.org</a> </p>
<h2>Index</h2>
