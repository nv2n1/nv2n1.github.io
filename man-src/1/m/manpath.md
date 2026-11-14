---
title: "manpath(1)"
name: "manpath"
section: "1"
letter: "m"
url: "/docs/linux/man/1-manpath/"
description: "manpath – determine search path for manual pages"
---

<h2 class="name">NAME</h2>
<p> manpath &#8211; determine search path for manual pages </p>
<h2>SYNOPSIS</h2>
<p> <code>manpath</code> [<code>-qgdc?V</code>] [<code>-m</code> <i>system</i>[,&#8230;]] [<code>-C</code> <i>file</i>]</p>
<h2>DESCRIPTION</h2>
<p> If $<code>MANPATH</code> is set, <code>manpath</code> will simply display its contents and issue a warning. If not, <code>manpath</code> will determine a suitable manual page hierarchy search path and display the results. </p>
<p> The colon-delimited path is determined using information gained from the man-db configuration file &#8211; (<i>/etc/manpath.config</i>) and the user&#8217;s environment.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Do not issue warnings.</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Print debugging information.</p>
<dt><code>-c</code>, <code>&#8211;catpath</code></p>
<dd> Produce a catpath as opposed to a manpath. Once the manpath is determined, each path element is converted to its relative catpath.</p>
<dt><code>-g</code>, <code>&#8211;global</code></p>
<dd> Produce a manpath consisting of all paths named as &quot;global&quot; within the man-db configuration file.</p>
<dt><code>-m</code> <i>system</i>[,&#8230;], <code>&#8211;systems=</code><i>system</i>[,&#8230;]</p>
<dd> If this system has access to other operating systems&#8217; manual hierarchies, this option can be used to include them in the output of <code>manpath</code>. To include NewOS&#8217;s manual page hierarchies use the option <code>-m</code> <code>NewOS</code>. </p>
<p> The <i>system</i> specified can be a combination of comma delimited operating system names. To include the native operating system&#8217;s manual page hierarchies, the system name <code>man</code> must be included in the argument string. This option will override the $<code>SYSTEM</code> environment variable.</p>
<dt><code>-C&nbsp;</code><i>file</i>,&nbsp;<code>&#8211;config-file=</code><i>file</i></p>
<dd> Use this user configuration file rather than the default of <i>~/.manpath</i>.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Print a help message and exit.</p>
<dt><code>&#8211;usage</code></p>
<dd> Print a short usage message and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display version information.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>MANPATH</code></p>
<dd> If $<code>MANPATH</code> is set, <code>manpath</code> displays its value rather than determining it on the fly. </p>
<p> See the <code>SEARCH PATH</code> section of <code><a href="/docs/linux/man/5-manpath/">manpath</a></code>(5) for the default behaviour and details of how this environment variable is handled.</p>
<dt><code>SYSTEM</code></p>
<dd> If $<code>SYSTEM</code> is set, it will have the same effect as if it had been specified as the argument to the <code>-m</code> option.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/manpath.config</i></p>
<dd> man-db configuration file.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-apropos/">apropos</a></code>(1), <code><a href="/docs/linux/man/1-man/">man</a></code>(1), <code><a href="/docs/linux/man/1-whatis/">whatis</a></code>(1)</p>
<h2>AUTHOR</h2>
<pre><code>
Wilf.(G.Wilford[at] ee.surrey.ac.uk).Fabrizio Polacco(fpolacco[at] debian.org).Colin Watson(cjwatson[at] debian.org).
</code></pre>
<h2>BUGS</h2>
<p> <a rel="nofollow" href="https://gitlab.com/cjwatson/man-db/-/issues">https://gitlab.com/cjwatson/man-db/-/issues</a><br />
 <a rel="nofollow" href="https://savannah.nongnu.org/bugs/?group=man-db">https://savannah.nongnu.org/bugs/?group=man-db</a> </p>
<h2>Index</h2>
