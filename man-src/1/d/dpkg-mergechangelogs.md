---
title: "dpkg-mergechangelogs(1)"
name: "dpkg-mergechangelogs"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg-mergechangelogs/"
description: "dpkg-mergechangelogs – 3-way merge of debian/changelog files"
---

<h2 class="name">NAME</h2>
<p> dpkg-mergechangelogs &#8211; 3-way merge of debian/changelog files </p>
<h2>SYNOPSIS</h2>
<p> <code>dpkg-mergechangelogs</code> [<i>option</i>&#8230;] <i>old</i> <i>new-a</i> <i>new-b</i> [<i>out</i>]</p>
<h2>DESCRIPTION</h2>
<p> This program will use the 3 provided versions of the Debian changelog to generate a merged changelog file. The resulting changelog is stored in the file <i>out</i> or output to the standard output if that parameter is not given. </p>
<p> Each entry is identified by its version number and they are assumed to be not conflicting, they are simply merged in the right order (by decreasing version number). When <code>&#8211;merge-prereleases</code> is used, the part of the version number after the last tilde is dropped so that 1.0-1~exp1 and 1.0-1~exp5 are considered to be the same entry. When the same version is available in both <i>new-a</i> and <i>new-b</i>, a standard line-based 3-way merge is attempted (provided that the module Algorithm::Merge is available &#8212; it&#8217;s part of the package libalgorithm-merge-perl &#8212; otherwise you get a global conflict on the content of the entry).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;merge-unreleased</code></p>
<dd> Ignore the version number when the entries are marked as <font SIZE="-1"><code>UNRELEASED</code></font> (since dpkg 1.21.0). </p>
<p> This is useful when you have diverging development for versions that have not yet been released. For instance 2.1-1 is released, then development happens for the new 2.2-1 and then for 2.3-1, where it makes sense to just end with a coalesced entry for 2.3-1 including all the development done in 2.2-1.</p>
<dt><code>-m</code>, <code>&#8211;merge-prereleases</code></p>
<dd> Drop the part after the last tilde in the version number when doing version comparison to identify if two entries are supposed to be the same or not. </p>
<p> This is useful when you keep using the same changelog entry but you increase its version number regularly. For instance, you might have 2.3-1~exp1, 2.3-1~exp2, &#8230; until the official release 2.3-1 and they are all the same changelog entry that has evolved over time.</p>
<dt><code>&#8211;help</code></p>
<dd> Show the usage message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version and exit.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>DPKG_COLORS</code></font></p>
<dd> Sets the color mode (since dpkg 1.18.5). The currently accepted values are: <code>auto</code> (default), <code>always</code> and <code>never</code>.</p>
<dt><font SIZE="-1"><code>DPKG_NLS</code></font></p>
<dd> If set, it will be used to decide whether to activate Native Language Support, also known as internationalization (or i18n) support (since dpkg 1.19.0). The accepted values are: <code>0</code> and <code>1</code> (default).</dl>
<h2>LIMITATIONS</h2>
<p> Anything that is not parsed by Dpkg::Changelog is lost during the merge. This might include stuff like comments which were not supposed to be there, etc.</p>
<h2>INTEGRATION WITH GIT</h2>
<p> If you want to use this program to merge Debian changelog files in a git repository, you have first to register a new merge driver in <code>.git/config</code> or <code>~/.gitconfig</code>: </p>
<pre>
 [merge &quot;dpkg-mergechangelogs&quot;]
    name = debian/changelog merge driver
    driver = dpkg-mergechangelogs -m %O %A %B %A
</pre>
<p> Then you have to setup the merge attribute for the debian/changelog file either in <code>.gitattributes</code> in the repository itself, or in <code>.git/info/attributes</code>: </p>
<pre>
 debian/changelog merge=dpkg-mergechangelogs
</pre>
<h2>Index</h2>
