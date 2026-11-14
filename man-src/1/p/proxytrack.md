---
title: "proxytrack(1)"
name: "proxytrack"
section: "1"
letter: "p"
url: "/docs/linux/man/1-proxytrack/"
description: "proxytrack – proxy to serve content archived by httrack website copier"
---

<h2>NAME</h2>
<p> proxytrack &#8211; proxy to serve content archived by httrack website copier</p>
<h2>SYNOPSIS</h2>
<p> <code>proxytrack proxy_address:proxy_port icp_address:icp_port [ httrack_cache_filename_1 [ httrack_cache_filename_2 .. ] ]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>proxytrack</code> this program allows you to create a proxy to deliver content already archived by <code><a href="/docs/linux/man/1-httrack/">httrack</a></code>(1) , a website copier.</p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>proxytrack proxy:8080 localhost:3130 /home/archives/example.com/hts-cache/new.zip</code></p>
<dd>
&nbsp;<wbr>will launch the proxytrack proxy, listening to :8080, to deliver content archived in the&nbsp;<wbr>/home/archives/example.com/hts-cache/new.zip cache</dl>
<h2>ENVIRONMENT</h2>
<h2>DIAGNOSTICS</h2>
<p> Errors/Warnings are reported the console and standard error </p>
<h2>BUGS</h2>
<p> Please reports bugs to <code>&lt;bugs [at] httrack.com&gt;.</code> Include a complete, self-contained example that will allow the bug to be reproduced, and say which version of (web)httrack you are using. Do not forget to detail options used, OS version, and any other information you deem necessary.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1998-2013 Xavier Roche and other contributors </p>
<p> This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program. If not, see &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/">http://www.gnu.org/licenses/</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The most recent released version of (web)httrack can be found at: <code><a rel="nofollow" href="http://www.httrack.com">http://www.httrack.com</a></code></p>
<h2>AUTHOR</h2>
<p> Xavier Roche &lt;roche [at] httrack.com&gt;</p>
<h2>SEE ALSO</h2>
<p> The <code>HTML </code> documentation (available online at <code><a rel="nofollow" href="http://www.httrack.com/html/">http://www.httrack.com/html/</a></code> ) contains more detailed information. Please also refer to the <code>httrack FAQ</code> (available online at <code><a rel="nofollow" href="http://www.httrack.com/html/faq.html">http://www.httrack.com/html/faq.html</a></code> ) </p>
<h2>Index</h2>
