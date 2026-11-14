---
title: "validatefile(3)"
name: "validatefile"
section: "3"
letter: "v"
url: "/docs/linux/man/3-validatefile/"
---

XMLTV::ValidateFile - Validates an XMLTV file 

<h2>Description</h2>Utility library that validates that a file is correct according to <a rel="nofollow" HREF="http://wiki.xmltv.org/index.php/XMLTVFormat.">http://wiki.xmltv.org/index.php/XMLTVFormat.</a>
<h2>Exported Functions</h2>All these functions are exported on demand.
<dl COMPACT><dt>LoadDtd
<dd>Load the xmltv dtd. Takes a single parameter which is the name of the xmltv dtd file. 

 LoadDtd must be called before ValidateFile can be called.
<dt>ValidateFile
<dd>Validate that a file is valid according to the <font SIZE="-1">XMLTV</font> dtd and try to check that it contains valid information. ValidateFile takes a filename as parameter and optionally also a day and an offset and prints error messages to <font SIZE="-1">STDERR.</font> 

 ValidateFile returns a list of errors that it found with the file. Each error takes the form of a keyword: 

 ValidateFile checks the following:
<dl COMPACT><dd><dl COMPACT><dt>notwell
<dd>The file is not well-formed <font SIZE="-1">XML.</font>
<dt>notdtd
<dd>The file does not follow the <font SIZE="-1">XMLTV DTD.</font>
<dt>unknownid
<dd>No channel-entry found for a channelid that is used in a programme-entry.
<dt>duplicatechannel
<dd>More than one channel-entry found for a channelid.
<dt>noprogrammes
<dd>No programme entries were found in the file.
<dt>channelnoprogramme
<dd>There are no programme entries for one of the channels listed with a channel-entry.
<dt>invalidid
<dd>An xmltvid does not look like a proper id, i.e. it does not match /^[-a-zA-Z0-9]+(\.[-a-zA-Z0-9]+)+$/.
<dt>noid
<dd>A programme-entry without an id was found.
<dt>emptytitle
<dd>A programme entry with an empty or missing title was found.
<dt>emptydescription
<dd>A programme entry with an empty desc-element was found. The desc-element shall be omitted if there is no description.
<dt>badstart
<dd>A programme entry with an invalid start-time was found.
<dt>badstop
<dd>A programme entry with an invalid stop-time was found.
<dt>badepisode
<dd>A programme entry with an invalid episode number was found.
<dt>badiso8859
<dd>The file is encoded in iso-8859 but contains characters that have no meaning in iso-8859 (or are control characters). If it's iso-8859-1 aka Latin 1 it might be some characters in windows-1252 encoding.
<dt>badutf8
<dd>The file is encoded in utf-8 but contains characters that look strange. 1) Mis-encoded single characters represented with [<font SIZE="-1">EF</font>][<font SIZE="-1">BF</font>][<font SIZE="-1">BD</font>] bytes 2) Mis-encoded single characters represented with [C3][<font SIZE="-1">AF</font>][C2][<font SIZE="-1">BF</font>][C2][<font SIZE="-1">BD</font>] bytes 3) Mis-encoded single characters in range [C2][80-9F]</dl></dl><dl COMPACT><dd>If no errors are found, an empty list is returned.</dl></dl><h2>Bugs</h2>It is currently necessary to specify the path to the xmltv dtd-file. This should not be necessary.
<h2>Copyright</h2>Copyright (C) 2006 Mattias Holmlund. 

 This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. 

 You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301, USA.</font>
