---
title: "whichman(1)"
name: "whichman"
section: "1"
letter: "w"
url: "/docs/linux/man/1-whichman/"
description: "whichman – show the location of a man page using a fault tolerant approximate matching algorithm"
---

<h2 class="name">NAME</h2>
<p> whichman &#8211; show the location of a man page using a fault tolerant approximate matching algorithm </p>
<h2>SYNOPSIS</h2>
<p> <code>whichman</code> [-#ehIp][-t#] man-page-name</p>
<h2>DESCRIPTION</h2>
<p> <code>whichman </code> is a &quot;which&quot; alike search command for man pages. <code>whichman </code> searches the <code>MANPATH </code> environment variable. If this variable is not defined, then it uses <i>/usr/share/man:/usr/man:/usr/X11R6/man:</i> <i>/usr/local/share/man:/usr/local/man</i> by default. </p>
<p> Unlike &quot;which&quot; this program does not stop on the first match. The name should probably have been something like whereman as this is not a &quot;which&quot; at all. whichman shows all man-pages that match and allows you to identify the different sections to which the pages belong. </p>
<p> <code>whichman </code> can handle international manpage path names for different languages. Man pages in different languages may be stored in &#8230;/man/&lt;country_code&gt;/man[1-9]/&#8230; </p>
<p> By default, <code>whichman</code> does fault tolerant approximate string matching. With a default tolerance level of: (strlen(searchpattern) &#8211; number of wildcards)/6 + 1</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-h</i></p>
<dd> Prints a little help/usage information.</p>
<dt><i>-I</i></p>
<dd> Do case sensitive search (default is case in-sensitive)</p>
<dt><i>-e</i></p>
<dd> Use exact matching when searching for a given man-page and the wildcards * and ? are disabled.</p>
<dt><i>-p</i></p>
<dd> print the actual tolerance level in front of the man page name.</p>
<dt><i>-# or -t#</i></p>
<dd> Set the fault tolerance level to #. The fault tolerance level is a integer # in the range 0-255. It specifies the maximum number of errors permitted in finding the approximate match. A tolerance_level of zero allows exact matches only but does NOT disable the wildcards * and ?.</dl>
<p> The search key may contain the wildcards * and ? (but see -e option):</p>
<dl>
<dt><code>&#8216;*&#8217;</code></p>
<dd> any arbitrary number of character</p>
<dt><code>&#8216;?&#8217;</code></p>
<dd> one character</dl>
<p> The last argument to whichman is not parsed for options as the program needs at least one man-page-name argument. This means that <i>whichman -x</i> will not complain about a wrong option but search for the man-page named -x.</p>
<h2>EXAMPLE</h2>
<p> <i>whichman</i> print </p>
<p> This will e.g. find the man-pages:<br />
 /usr/share/man/man1/printf.1.gz<br />
 /usr/share/man/man3/printf.3.gz<br />
 /usr/share/man/man3/rint.3.gz</p>
<h2>BUGS</h2>
<p> The wildcards <code>&#8216;?&#8217;</code> and <code>&#8216;*&#8217;</code> can not be escaped. These characters function always as wildcards. This is however not a big problem since there is hardly any man-page that has these characters in its name.</p>
<h2>AUTHOR</h2>
<p> Guido Socher (guido [at] linuxfocus.org)</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ftff/">ftff</a></code>(1), <code><a href="/docs/linux/man/1-man/">man</a></code>(1) </p>
<h2>Index</h2>
