---
title: "ripright(1)"
name: "ripright"
section: "1"
letter: "r"
url: "/docs/linux/man/1-ripright/"
description: "ripright – CD ripper"
---

<h2>NAME</h2>
<p> ripright &#8211; CD ripper</p>
<h2>SYNOPSIS</h2>
<p> <code>ripright [-d] [-a] [-r] [-s] [-w] [-c </code><i>device</i>] [-o <i>format</i>] [<i>outpath</i>] </p>
<h2>DESCRIPTION</h2>
<p> RigRight is a minimal CD ripper with few options. It can run as a daemon and will automatically start ripping any CD found in the drive after which the disc will be ejected. Ripping is always to FLAC lossless audio format with tags taken from the MusicBrainz lookup service and cover art from Amazon where possible. If a disc is unknown to MusicBrainz, the CD will be ejected without ripping. </p>
<p> In case a disc is unknown, MusicBrainz Picard can be used to send the CD ToC to the MusicBrainz database. The MusicBrainz website can then be used to find or add details of a CD, after which the CD can be ripped using RipRight. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;daemon</code></p>
<dd> Run in daemon mode. Ripright will detach from the terminal and direct output to the syslog.</p>
<dt><code>-a</code>, <code>&#8211;rip-to-all</code></p>
<dd> Normally exactly 1 result is required from Musicbrainz, otherwise the CD will be refused and ejected. With this option, the CD will be ripped and tagged to multiple files, once as each result from Musicbrainz. Each rip is output under a directory named Ambiguous/&lt;mb-release-id&gt;/ where the the Musicbrainz release Id is used to identify each possible release.</p>
<dt><code>-w</code>, <code>&#8211;w32-filenames</code></p>
<dd> Covert characters that are illegal on Windows filesystems to UTF-8 alternatives. If accessing files over Samba, this prevents name mangling which can lose the file extension. Mapped characters are <code>*</code>, <code>?</code>, <code>&quot;</code> and <code>|</code> which are replaced by <code>ӿ</code>, <code>ʔ</code>, <code>¨</code> and <code>ǀ</code> respectively.</p>
<dt><code>-s</code>, <code>&#8211;allow-skips</code></p>
<dd> Normally ripping attempts to make a perfect copy of a CD by using all data verification and correction features of the cdparanoia library. With this option, each bad sectors will be skipped after 20 failed attempts to read the data. Without this option, ripping of scratched or damaged CDs may take a very long time and possibly may not complete.</p>
<dt><code>-r</code>, <code>&#8211;require-art</code></p>
<dd> Refuse to rip a CD if the cover art cannot be retrieved. The correct ASIN must be added to the MusicBrainz database for art to be fetched from Amazon.</p>
<dt><code>-f &lt;file&gt;</code>, <code>&#8211;folder-art &lt;file&gt;</p>
<dd> Save cover art (if available) to &lt;file&gt;, relative to the output directory. The art file will be converted to the format specified by the filename e.g. -f folder.jpg or -f folder.gif or -f folder.png</p>
<dt>-c</code>, <code>&#8211;cd-device</code></p>
<dd> Path to the CD-ROM device to use. This defaults to /dev/cdrom if not otherwise specified.</p>
<dt><code>-o</code>, <code>&#8211;output-file</code></p>
<dd> Set the format used to produce output filenames and paths. This should be a string containing the following special tokens: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>%N&nbsp;<wbr>=&nbsp;<wbr>Track number&nbsp;<wbr>(TRACKNUMBER)<br />
&nbsp;<wbr>&nbsp;<wbr>%A&nbsp;<wbr>=&nbsp;<wbr>Track artist&nbsp;<wbr>(ARTIST)<br />
&nbsp;<wbr>&nbsp;<wbr>%a&nbsp;<wbr>=&nbsp;<wbr>Track artist sort name&nbsp;<wbr>(ARTISTSORT)<br />
&nbsp;<wbr>&nbsp;<wbr>%B&nbsp;<wbr>=&nbsp;<wbr>Album artist&nbsp;<wbr>(ALBUMARTIST)<br />
&nbsp;<wbr>&nbsp;<wbr>%b&nbsp;<wbr>=&nbsp;<wbr>Album artist sort name&nbsp;<wbr>(ALBUMARTISTSORT)<br />
&nbsp;<wbr>&nbsp;<wbr>%C&nbsp;<wbr>=&nbsp;<wbr>Track artist if present, else album artist<br />
&nbsp;<wbr>&nbsp;<wbr>%c&nbsp;<wbr>=&nbsp;<wbr>Track artist sort name if present, else album artist sort name<br />
&nbsp;<wbr>&nbsp;<wbr>%D&nbsp;<wbr>=&nbsp;<wbr>Album/CD name&nbsp;<wbr>(ALBUM)<br />
&nbsp;<wbr>&nbsp;<wbr>%T&nbsp;<wbr>=&nbsp;<wbr>Track name&nbsp;<wbr>(TITLE)<br />
&nbsp;<wbr>&nbsp;<wbr>%Y&nbsp;<wbr>=&nbsp;<wbr>Release type&nbsp;<wbr>(MUSICBRAINZ_TYPE)<br />
&nbsp;<wbr>&nbsp;<wbr>%%&nbsp;<wbr>=&nbsp;<wbr>A single percent sign </p>
<p> The release type is one of Albums, Audiobooks, Compilations, EPs, Interviews, Live, Remixes, Singles, Soundtracks, Spokenword and Other. </p>
<p> Slashes and colons in the &#8216;%&#8217; output fields are converted to UTF-8 equivalents to avoid creating subdirectories or causing problems with Windows shares mounted via Samba. Slashes and colons given in the format string will be literally preserved. </p>
</dl>
<h2>COPYRIGHT</h2>
<p> RipRight, Copyright (C) 2013-2015 Michael C McTernan,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mike [at] mcternan.uk<br />
 Eject routines, Copyright (c) 1994-2005 Jeff Tranter<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>tranter [at] pobox.com </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-riparrange/">riparrange</a>(1) </p>
<p> <a rel="nofollow" href="http://www.mcternan.co.uk/ripright/">http://www.mcternan.co.uk/ripright/</a><br />
 <a rel="nofollow" href="http://www.musicbrainz.org/">http://www.musicbrainz.org/</a> </p>
<h2>Index</h2>
