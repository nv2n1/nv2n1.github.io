---
title: "cd-discid(1)"
name: "cd-discid"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cd-discid/"
description: "cd-discid – read CD and get CDDB discid information"
---

<h2 class="name">NAME</h2>
<p> cd-discid &#8211; read CD and get CDDB discid information </p>
<h2>SYNOPSIS</h2>
<p> <code>cd-discid</code> [<i>option</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> In order to do CDDB queries over the Internet, you must know the DiscID of the CD you are querying. <code>cd-discid</code> provides you with that information. It outputs the discid, the number of tracks, the frame offset of all of the tracks, and the total length of the CD in seconds, on one line in a space-delimited format. <code>cd-discid</code> was designed as a backend tool for cdgrab (now <code>abcde</code>) but will work independently of it.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;musicbrainz</code></p>
<dd> Output a TOC that is suitable for calculating the MusicBrainz disc id.</p>
<dt><code>&#8211;help</code></p>
<dd> Display a brief help message.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version.</p>
<dt><code>devicename</code></p>
<dd> CD-ROM block device name that contains the CD to be queried. If this option is omitted, the following device name is assumed:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>/dev/cdrom</i></p>
<dd> Linux and FreeBSD</p>
<dt><i>/dev/cd0a</i></p>
<dd> OpenBSD and NetBSD</p>
<dt><i>/dev/vol/aliases/cdrom0</i></p>
<dd> Solaris</p>
<dt><i>/dev/disk1</i></p>
<dd> MacOS X</p>
<dt><i>/dev/cd0</i></p>
<dd> Hurd</dl>
</dl>
</dl>
<h2>AUTHOR</h2>
<p> Robert Woodcock &lt;rcw [at] debian.org&gt;. Updates by Timur Bish &lt;taem [at] linukz.org&gt;. </p>
<h2>Index</h2>
