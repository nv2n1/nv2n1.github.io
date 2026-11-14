---
title: "webhttrack(1)"
name: "webhttrack"
section: "1"
letter: "w"
url: "/docs/linux/man/1-webhttrack/"
description: "webhttrack – offline browser : copy websites to a local directory"
---

<h2>NAME</h2>
<p> webhttrack &#8211; offline browser : copy websites to a local directory</p>
<h2>SYNOPSIS</h2>
<p> <code>webhttrack [ keyword value [ keyword value .. ] ]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>webhttrack</code> this program is a script frontend to <code><a href="/docs/linux/man/1-httrack/">httrack</a></code>(1) and <code><a href="/docs/linux/man/1-htsserver/">htsserver</a></code>(1) , a website copier.</p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>webhttrack lang 1</code></p>
<dd>
&nbsp;<wbr>will launch the webhttrack server frontend, and the default system browser, with&nbsp;<wbr>&quot;lang&quot;&nbsp;<wbr>set to&nbsp;<wbr>&quot;english&quot;&nbsp;<wbr>(language&nbsp;<wbr>#1)</dl>
<h2>FILES</h2>
<p> <i>/etc/httrack.conf</i></p>
<dl>
<dt>
<dd> The system wide configuration file.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>HOME</p>
<dd> Is being used if you defined in /etc/httrack.conf the line <i>path ~/websites/# </i></dl>
<h2>DIAGNOSTICS</h2>
<p> Errors/Warnings are reported to <i>hts-log.txt</i> located in the destination directory. </p>
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
