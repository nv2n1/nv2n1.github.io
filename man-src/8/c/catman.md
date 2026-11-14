---
title: "catman(8)"
name: "catman"
section: "8"
letter: "c"
url: "/docs/linux/man/8-catman/"
description: "catman – create or update the pre-formatted manual pages"
---

<p>catman &#8211; create or update the pre-formatted manual pages</p>
<h2>Synopsis</h2>
<p><code>catman</code> [<code>-d?V</code>] [<code>-M</code> <i>path</i>] [<code>-C</code> <i>file</i>] [<i>section</i>] &#8230;</p>
<h2>Description</h2>
<p><code>catman</code> is used to create an up to date set of pre-formatted manual pages known as cat pages. Cat pages are generally much faster to display than the original manual pages, but require extra storage space. The decision to support cat pages is that of the local administrator, who must provide suitable directories to contain them. </p>
<p> The options available to <code>catman</code> are the manual page hierarchies and sections to pre-format. The default hierarchies are those specified as system hierarchies in the man-db configuration file, and the default sections are either the colon-delimited contents of the environment variable $<code>MANSECT</code> or the standard set compiled into <code>man</code> if $<code>MANSECT</code> is undefined. Supplying <code>catman</code> with a set of whitespace-delimited section names will override both of the above. </p>
<p> <code>catman</code> makes use of the <code>index</code> database cache associated with each hierarchy to determine which files need to be formatted.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd>Print debugging information.</p>
<dt><code>-M&nbsp;</code><i>path</i>,&nbsp;<code>&#8211;manpath=</code><i>path</i></p>
<dd>Specify an alternate colon-delimited manual page hierarchy search path. By default, this is all paths indicated as system hierarchies in the man-db configuration file.</p>
<dt><code>-C&nbsp;</code><i>file</i>,&nbsp;<code>&#8211;config-file=</code><i>file</i></p>
<dd>Use this user configuration file rather than the default of <i>~/.manpath</i>.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd>Print a help message and exit.</p>
<dt><code>&#8211;usage</code></p>
<dd>Print a short usage message and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Display version information.</dl>
<h2>Environment</h2>
<dl>
<dt><code>MANSECT</code></p>
<dd>If $<code>MANSECT</code> is set, its value is a colon-delimited list of sections and it is used to determine which manual sections to search and in what order. The default is &quot;1 n l 8 3 0 2 3posix 3pm 3perl 3am 5 4 9 6 7&quot;, unless overridden by the <code>SECTION</code> directive in <i>/etc/manpath.config</i>.</p>
<dt><code>MANPATH</code></p>
<dd>If $<code>MANPATH</code> is set, its value is interpreted as the colon-delimited manual page hierarchy search path to use. </p>
<p> See the <code>SEARCH PATH</code> section of <code><a href="/docs/linux/man/5-manpath/">manpath</a></code>(5) for the default behaviour and details of how this environment variable is handled.</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/manpath.config</i></p>
<dd>man-db configuration file.</p>
<dt><i>/usr/man/index.(bt|db|dir|pag)</i></p>
<dd>A traditional global <i>index</i> database cache.</p>
<dt><i>/var/catman/index.(bt|db|dir|pag)</i></p>
<dd>An alternate or FSSTND compliant global <i>index</i> database cache.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-man/">man</a></code>(1), <code><a href="/docs/linux/man/5-manpath/">manpath</a></code>(5), <code><a href="/docs/linux/man/8-mandb/">mandb</a></code>(8)</p>
<h2>Author</h2>
<pre>Wilf. (G.Wilford [at] ee.surrey.ac.uk).
Fabrizio Polacco (fpolacco [at] debian.org).
Colin Watson (cjwatson [at] debian.org).</pre>
<h2>Bugs</h2>
<p><a rel="nofollow" href="https://gitlab.com/cjwatson/man-db/-/issues">https://gitlab.com/cjwatson/man-db/-/issues</a><br />
 <a rel="nofollow" href="https://savannah.nongnu.org/bugs/?group=man-db">https://savannah.nongnu.org/bugs/?group=man-db</a> </p>
