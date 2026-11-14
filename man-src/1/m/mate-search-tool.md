---
title: "mate-search-tool(1)"
name: "mate-search-tool"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mate-search-tool/"
description: "mate-search-tool – the MATE Search Tool"
---

<h2>NAME</h2>
<p> mate-search-tool &#8211; the MATE Search Tool</p>
<h2>SYNOPSIS</h2>
<p> <code>mate-search-tool</code> [<i>options</i>] </p>
<p> or select <code>Search for Files&#8230;</code> from a <code>Main Menu</code> or from the <code>Places</code> menu in a <code>Menu Bar</code></p>
<h2>DESCRIPTION</h2>
<p> <code>MATE Search Tool</code> is a utility for finding files on your system. To perform a basic search, you can type a filename or a partial filename, with or without wildcards. To refine your search, you can apply additional search options. </p>
<p> <code>MATE Search Tool</code> uses the find, grep, and locate UNIX commands. The case sensitivity of the search depends on your operating system. For example, on Linux, the find, grep, and locate commands support the -i option, so all searches are case-insensitive. </p>
<p> For full documentation see the <code>MATE Search Tool</code> online help. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Show help message</p>
<dt><code>&#8211;named=</code><i>STRING</i></p>
<dd> Set the text of &quot;Name contains&quot; search option</p>
<dt><code>&#8211;path=</code><i>PATH</i></p>
<dd> Set the text of &quot;Look in folder&quot; search option</p>
<dt><code>&#8211;sortby=</code><i>VALUE</i></p>
<dd> Sort files by one of the following: name, folder, size, type, or date</p>
<dt><code>&#8211;descending</code></p>
<dd> Set sort order to descending, the default is ascending</p>
<dt><code>&#8211;start</code></p>
<dd> Automatically start a search</p>
<dt><code>&#8211;contains=</code><i>STRING</i></p>
<dd> Select and set the &quot;Contains the text&quot; search option</p>
<dt><code>&#8211;mtimeless=</code><i>DAYS</i></p>
<dd> Select and set the &quot;Date modified less than&quot; search option</p>
<dt><code>&#8211;mtimemore=</code><i>DAYS</i></p>
<dd> Select and set the &quot;Date modified more than&quot; search option</p>
<dt><code>&#8211;sizemore=</code><i>KILOBYTES</i></p>
<dd> Select and set the &quot;Size at least&quot; search option</p>
<dt><code>&#8211;sizeless=</code><i>KILOBYTES</i></p>
<dd> Select and set the &quot;Size at most&quot; search option</p>
<dt><code>&#8211;empty</code></p>
<dd> Select the &quot;File is empty&quot; search option</p>
<dt><code>&#8211;user=</code><i>USER</i></p>
<dd> Select and set the &quot;Owned by user&quot; search option</p>
<dt><code>&#8211;group=</code><i>GROUP</i></p>
<dd> Select and set the &quot;Owned by group&quot; search option</p>
<dt><code>&#8211;nouser</code></p>
<dd> Select the &quot;Owner is unrecognized&quot; search option</p>
<dt><code>&#8211;notnamed=</code><i>STRING</i></p>
<dd> Select and set the &quot;Name does not contain&quot; search option</p>
<dt><code>&#8211;regex=</code><i>PATTERN</i></p>
<dd> Select and set the &quot;Name matches regular expression&quot; search option</p>
<dt><code>&#8211;hidden</code></p>
<dd> Select the &quot;Show hidden and backup files&quot; search option</p>
<dt><code>&#8211;follow</code></p>
<dd> Select the &quot;Follow symbolic links&quot; search option</p>
<dt><code>&#8211;mounts</code></p>
<dd> Select the &quot;Exclude other filesystems&quot; search option</dl>
<h2>AUTHOR</h2>
<p> <code>MATE Search Tool</code> was originally written by George Lebl (&lt;jirka [at] 5z.com&gt;). Version 2 was written by Dennis M. Cranston (&lt;dennis_cranston [at] yahoo.com&gt;). </p>
<p> This manual page was originally written by Jochen Voss &lt;voss [at] mathematik.uni-kl.de&gt;. Version 2 was written by Dennis M. Cranston (&lt;dennis_cranston [at] yahoo.com&gt;). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-find/">find</a></code>(1), <code><a href="/docs/linux/man/1-locate/">locate</a></code>(1), <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1) </p>
<h2>Index</h2>
