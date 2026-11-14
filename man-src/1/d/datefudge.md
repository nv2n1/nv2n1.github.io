---
title: "datefudge(1)"
name: "datefudge"
section: "1"
letter: "d"
url: "/docs/linux/man/1-datefudge/"
description: "datefudge – pretend the system time is different"
---

<h2>NAME</h2>
<p> datefudge &#8211; pretend the system time is different</p>
<h2>SYNOPSIS</h2>
<p> <code>datefudge</code> [<i>-s</i>|<i>&#8211;static</i>] <i>at_date program</i> [<i>arguments</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>datefudge</code> is a small utility that pretends that the system time is different by pre-loading a small library which modifies the <code><a href="/docs/linux/man/2-time/">time</a></code>(2), <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2) and <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2) system calls.</p>
<h2>DATE FORMAT</h2>
<p> The <i>at_date</i> argument can be given in any format accepted by the <code><a href="/docs/linux/man/1-date/">date</a></code>(1) program, for example &quot;2007-04-01 12:21&quot; or &quot;yesterday&quot;, or &quot;next Friday&quot;.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;static</code>, <code>-s</code></p>
<dd> Mark the date as a `static&#8217; one. The above mentioned system calls will always return the date given in the <i>at_date</i> argument, regardless of time passing. See EXAMPLES<br />
&nbsp;<wbr>below.</p>
<dt><code>&#8211;help</code>, <code>-h</code></p>
<dd> Print short usage information and exit.</p>
<dt><code>&#8211;version</code>, <code>-v</code></p>
<dd> Print version information and exit.</dl>
<h2>EXAMPLES</h2>
<h3>Basic examples:</h3>
<pre>
<i>$ datefudge &quot;2007-04-01 10:23&quot; date -R</i>
Sun, 01 Apr 2007 10:23:00 +0200
<i>$ datefudge &quot;1 May 2007&quot; date -R</i>
Tue, 01 May 2007 00:00:00 +0200
<i>$ datefudge &quot;2 weeks ago&quot; date -R</i>
Wed, 16 Jan 2008 13:32:12 +0100
</pre>
<h3>Non-static vs. static example:</h3>
<pre><code>
$ datefudge "2007-04-01 10:23" sh - c "sleep 3; date -R" Sun, 01 Apr 2007 10 : 23 : 03 + 0200 $ datefudge-- static "2007-04-01 10:23" sh - c "sleep 3; date -R" Sun, 01 Apr 2007 10 : 23 : 00 + 0200
</code></pre>
<h2>AUTHOR</h2>
<p> Written by Matthias Urlichs &lt;smurf [at] noris.de&gt;. Modified by Robert Luberda &lt;robert [at] debian.org&gt;.</p>
<h2>BUGS</h2>
<p> There is no attempt to make this change undetectable by the program. In particular, file modification times are <code>not</code> modified.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2003 by Matthias Urlichs.<br />
 Copyright &#169; 2008-2016 by Robert Luberda. </p>
<p> There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. You may redistribute copies of datefudge under the terms of the GNU General Public License.<br />
 For more information about these matters, see the file named COPYING.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-date/">date</a></code>(1), <code><a href="/docs/linux/man/1-ld-so/">ld.so</a></code>(1), <code><a href="/docs/linux/man/2-time/">time</a></code>(2), <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2), <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2) </p>
<h2>Index</h2>
