---
title: "riparrange(1)"
name: "riparrange"
section: "1"
letter: "r"
url: "/docs/linux/man/1-riparrange/"
description: "riparrange – FLAC file organiser"
---

<h2>NAME</h2>
<p> riparrange &#8211; FLAC file organiser</p>
<h2>SYNOPSIS</h2>
<p> <code>riparrange [-m|-c|-h] [-f] [-v] [-w] [-o format] &lt;file.flac&gt;</code> </p>
<h2>DESCRIPTION</h2>
<p> RipArrange is a tool for automatically moving flac files to a directory structure based upon Vorbis Comment tags. A format string is used to define how the comment tags are mapped into a filename and path. </p>
<p> The default operation is to just print what would be changed if the tool were to be ran with -m, -c or -h specified. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-m</code></p>
<dd> Move/rename files to new location. This only works within a mount.</p>
<dt><code>-c</code></p>
<dd> Copy files to new location.</p>
<dt><code>-h</code></p>
<dd> Hard link files to new location. This only works within a filesystem.</p>
<dt><code>-f</code></p>
<dd> Remove existing destination files before operation.</p>
<dt><code>-w</code>, <code>&#8211;w32-filenames</code></p>
<dd> Covert characters that are illegal on Windows filesystems to UTF-8 alternatives. If accessing files over Samba, this prevents name mangling which can lose the file extension. Mapped characters are <code>*</code>, <code>?</code>, <code>&quot;</code> and <code>|</code> which are replaced by <code>ӿ</code>, <code>ʔ</code>, <code>¨</code> and <code>ǀ</code> respectively.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Output information about files which will not be moved because they are already in the correct location. Normally only things that would be changed are reported.</p>
<dt><code>-o</code>, <code>&#8211;output-file</code> <i>format</i></p>
<dd> Set the format used to produce output filenames and paths. This should be a string containing the following special tokens: </p>
<p>&nbsp;<wbr>%N&nbsp;<wbr>=&nbsp;<wbr>Track number&nbsp;<wbr>(TRACKNUMBER)<br />
&nbsp;<wbr>%A&nbsp;<wbr>=&nbsp;<wbr>Track artist&nbsp;<wbr>(ARTIST)<br />
&nbsp;<wbr>%a&nbsp;<wbr>=&nbsp;<wbr>Track artist sort name&nbsp;<wbr>(ARTISTSORT)<br />
&nbsp;<wbr>%B&nbsp;<wbr>=&nbsp;<wbr>Album artist&nbsp;<wbr>(ALBUMARTIST)<br />
&nbsp;<wbr>%b&nbsp;<wbr>=&nbsp;<wbr>Album artist sort name&nbsp;<wbr>(ALBUMARTISTSORT)<br />
&nbsp;<wbr>%C&nbsp;<wbr>=&nbsp;<wbr>Track artist if present, else album artist<br />
&nbsp;<wbr>%c&nbsp;<wbr>=&nbsp;<wbr>Track artist sort name if present, else album artist sort name<br />
&nbsp;<wbr>%D&nbsp;<wbr>=&nbsp;<wbr>Album/CD name&nbsp;<wbr>(ALBUM)<br />
&nbsp;<wbr>%T&nbsp;<wbr>=&nbsp;<wbr>Track name&nbsp;<wbr>(TITLE)<br />
&nbsp;<wbr>%Y&nbsp;<wbr>=&nbsp;<wbr>Release type&nbsp;<wbr>(MUSICBRAINZ_TYPE)<br />
&nbsp;<wbr>%%&nbsp;<wbr>=&nbsp;<wbr>A single percent sign </p>
<p> The release type is one of Albums, Audiobooks, Compilations, EPs, Interviews, Live, Remixes, Singles, Soundtracks, Spokenword and Other. </p>
<p> Slashes and colons in the &#8216;%&#8217; output fields are converted to UTF-8 equivalents to avoid creating subdirectories or causing problems with Windows shares mounted via Samba. Slashes and colons given in the format string will be literally preserved. </p>
</dl>
<h2>EXAMPLE</h2>
<p> The following command will re-arrange FLAC files found in the current directory, making a new directory structure under <i>/media/newmusic</i> containing hard links to the current files: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>riparrange -h -f&nbsp;<wbr>&quot;/media/newmusic/%Y/%B &#8211;&nbsp;<wbr>%D/%N-%T.flac&quot;&nbsp;<wbr>*.flac </p>
<p> <code>Find</code> and <code>xargs</code> can be used to call riparrange for files in different directories: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>find&nbsp;<wbr>/media/music/&nbsp;<wbr>-name&nbsp;<wbr>&quot;*.flac&quot;&nbsp;<wbr>-print0 |<br />
&nbsp;<wbr>xargs -0 riparrange -h -f&nbsp;<wbr>&quot;/media/newmusic/%Y/%B &#8211;&nbsp;<wbr>%D/%N-%T.flac&quot;&nbsp;<wbr>*.flac </p>
<h2>COPYRIGHT</h2>
<p> RipArrange, Copyright (C) 2013-2015 Michael C McTernan,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mike [at] mcternan.uk </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ripright/">ripright</a>(1) </p>
<p> <a rel="nofollow" href="http://www.mcternan.co.uk/ripright/">http://www.mcternan.co.uk/ripright/</a><br />
 <a rel="nofollow" href="http://wiki.musicbrainz.org/MusicBrainz_Tag">http://wiki.musicbrainz.org/MusicBrainz_Tag</a> </p>
<h2>Index</h2>
