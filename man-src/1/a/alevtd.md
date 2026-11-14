---
title: "alevtd(1)"
name: "alevtd"
section: "1"
letter: "a"
url: "/docs/linux/man/1-alevtd/"
description: "alevtd – webserver for videotext pages"
---

<h2>NAME</h2>
<p> alevtd &#8211; webserver for videotext pages</p>
<h2>SYNOPSIS</h2>
<p> <code>alevtd [ options ]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>alevtd</code> is http daemon which serves videotext pages as HTML. Tune in some station with a utility like v4lctl or some TV application. Then start it and point your browser to <a rel="nofollow" href="http://localhost:5654/">http://localhost:5654/</a> </p>
<p> Pages may be requested either in HTML format (<a rel="nofollow" href="http://localhost:5654/">http://localhost:5654/</a>&lt;page&gt;/ or <a rel="nofollow" href="http://localhost:5654/">http://localhost:5654/</a>&lt;page&gt;/&lt;subpage&gt;.html) or in ASCII text format (<a rel="nofollow" href="http://localhost:5654/">http://localhost:5654/</a>&lt;page&gt;/&lt;subpage&gt;.txt). Subpage &quot;00&quot; can be used for pages without subpages.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> print a short <code>h</code>elp text and the default values for all options.</p>
<dt><code>-v dev</code></p>
<dd> set <code>v</code>bi device (default: /dev/vbi0).</p>
<dt><code>-d</code></p>
<dd> enable <code>d</code>ebug output.</p>
<dt><code>-s</code></p>
<dd> Write a start/stop notice and serious errors to the <code>s</code>yslog. Specify this option twice to get a verbose log (additional log events like dropped connections).</p>
<dt><code>-t sec</code></p>
<dd> set network <code>t</code>imeout to &gt;sec&lt; seconds.</p>
<dt><code>-c n</code></p>
<dd> set the number of allowed parallel <code>c</code>onnections to &gt;n&lt;. This is a per-thread limit.</p>
<dt><code>-p port</code></p>
<dd> listen on <code>p</code>ort &gt;port&lt; for incoming connections. Default 5654.</p>
<dt><code>-n hostname</code></p>
<dd> set the host<code>n</code>ame which the server should use (required for redirects).</p>
<dt><code>-i ip</code></p>
<dd> bind to <code>I</code>P-address &gt;ip&lt;.</p>
<dt><code>-l log</code></p>
<dd> <code>l</code>og all requests to the logfile &gt;log&lt; (common log format). Using &quot;-&quot; as filename makes alevtd print the access log to stdout, which is only useful together with the -F switch (see below).</p>
<dt><code>-L log</code></p>
<dd> same as above, but additional flush every line. Useful if you want monitor the logfile with tail -f.</p>
<dt><code>-u user</code></p>
<dd> set <code>u</code>id to &gt;user&lt; (after binding to the tcp port). This option is allowed for root only.</p>
<dt><code>-g group</code></p>
<dd> set <code>g</code>id to &gt;group&lt; (after binding to the tcp port). This option is allowed for root only.</p>
<dt><code>-F</code></p>
<dd> don&#8217;t run as daemon. alevtd will not fork into background, not detach from terminal and report errors to stderr.</p>
<dt><code>-r</code></p>
<dd> poll tv frequency, clear vtx page cache if a frequency change was detected.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-alevt/">alevt</a>(1), <a href="/docs/linux/man/1-xawtv/">xawtv</a>(1), <a href="/docs/linux/man/1-v4lctl/">v4lctl</a>(1)</p>
<h2>AUTHOR</h2>
<p> Gerd Knorr &lt;kraxel [at] goldbach.in-berlin.de&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2000 Gerd Knorr &lt;kraxel [at] goldbach.in-berlin.de&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA. </p>
<h2>Index</h2>
