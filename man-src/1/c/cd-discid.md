---
title: "cd-discid(1)"
name: "cd-discid"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cd-discid/"
description: "cd-discid – read CD and get CDDB discid information"
---

<h2>SYNOPSIS</h2>
<p> <code>cd-discid</code> [<i>option</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> In order to do CDDB queries over the Internet, you must know the DiscID of the CD you are querying. <code>cd-discid</code> provides you with that information. It outputs the discid, the number of tracks, the frame offset of all of the tracks, and the total length of the CD in seconds, on one line in a space-delimited format. <code>cd-discid</code> was designed as a backend tool for cdgrab (now <code>abcde</code>) but will work independently of it.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;musicbrainz</code></dt>
<dd> Output a TOC that is suitable for calculating the MusicBrainz disc id.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Display a brief help message.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show the version.</dd>
<dt><code>devicename</code></dt>
<dd> CD-ROM block device name that contains the CD to be queried. If this option is omitted, the following device name is assumed:</dd>
<dl>
<dl>
<dt><i>/dev/cdrom</i></dt>
<dd> Linux and FreeBSD</dd>
<dt><i>/dev/cd0a</i></dt>
<dd> OpenBSD and NetBSD</dd>
<dt><i>/dev/vol/aliases/cdrom0</i></dt>
<dd> Solaris</dd>
<dt><i>/dev/disk1</i></dt>
<dd> MacOS X</dd>
<dt><i>/dev/cd0</i></dt>
<dd> Hurd</dd></dl>
</dl>
</dl>
<h2>AUTHOR</h2>
<p> Robert Woodcock &lt;rcw [at] debian.org&gt;. Updates by Timur Bish &lt;taem [at] linukz.org&gt;. </p>
