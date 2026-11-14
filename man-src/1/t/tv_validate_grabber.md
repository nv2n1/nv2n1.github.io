---
title: "tv_validate_grabber(1)"
name: "tv_validate_grabber"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_validate_grabber/"
description: "tv_validate_grabber – Validate that an xmltv grabber works correctly"
---

<h2 class="name">NAME</h2>
<p> tv_validate_grabber &#8211; Validate that an xmltv grabber works correctly </p>
<h2>SYNOPSIS</h2>
<p> tv_validate_grabber &#8211;help </p>
<p> tv_validate_grabber [&#8211;config-file &lt;configfile&gt;] [&#8211;keep-files] &lt;cmd&gt;</p>
<h2>DESCRIPTION</h2>
<p> tv_validate_grabber runs a grabber through a series of test to determine if it follows the recommendations described at &lt;<a rel="nofollow" href="http://wiki.xmltv.org/index.php/XmltvCapabilities">http://wiki.xmltv.org/index.php/XmltvCapabilities</a>&gt; </p>
<p> tv_validate_grabber does not assume that the grabber is written in perl. The command does not have to be a single executable, it can also be a complete command-line: </p>
<p> tv_validate_grabber &#8220;perl -I lib grab/new/tv_grab_new&#8221;</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;config-file &lt;configfile</code>&gt; Use the specified file as configuration file for the grabber. If the file does not exist, the grabber is run with &#8211;configure to create it. Default is to always run the grabber with &#8211;configure first and store the configuration in a temporary file. </p>
<p> <code>&#8211;keep-files</code> Do not delete the output-files generated during the validation.</p>
<h2>AUTHOR</h2>
<p> Mattias Holmlund, mattias -at- holmlund -dot- se.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005 Mattias Holmlund. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301, USA.</font> </p>
<h2>Index</h2>
