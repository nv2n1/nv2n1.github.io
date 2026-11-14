---
title: "smokeping_cgi(1)"
name: "smokeping_cgi"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smokeping_cgi/"
description: "smokeping_cgi – SmokePing webfrontend"
---

<h2 class="name">NAME</h2>
<p> smokeping_cgi &#8211; SmokePing webfrontend </p>
<h2>OVERVIEW</h2>
<p> This script acts as a &#8216;website&#8217; for your SmokePing monitoring operation. It presents the targets you are looking at in a tree structure and draws graphs as they are required by people looking at the pages.</p>
<h2>DESCRIPTION</h2>
<p> To get <code>smokeping_cgi</code> going, you need a webserver which allows you to run <font SIZE="-1">CGI</font> or better FastCGI scripts. The system must be setup so that the cgi process is allowed to write to the image caching area as defined in the config file. </p>
<p> This script runs fine as a normal <font SIZE="-1">CGI, </font><font SIZE="-1"><code>BUT</code></font> it will appear to be very slow, because it does a lot of things when starting up. So if the script has to be started a fresh on every click, this is both slow and a tough thing for your webserver. I therefore strongly recommend using FastCGI. </p>
<p> Please refer to the installation document for detailed setup instructions.</p>
<h2>SETUP</h2>
<p> There is a sample <i>htdocs</i> directory in your smokeping installation root. Copy its content to the place where your webserver expects its files. There are also two sample cgi scripts showing how to launch the smokeping cgi in your website. The only difference is the file extension. Adjust the paths in the script and you should be ready to go.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2011 by Tobias Oetiker. All right reserved.</p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font></p>
<h2>AUTHOR</h2>
<p> Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; </p>
<h2>Index</h2>
