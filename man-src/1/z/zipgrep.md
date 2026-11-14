---
title: "zipgrep(1)"
name: "zipgrep"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zipgrep/"
description: "zipgrep – search files in a ZIP archive for lines matching a pattern"
---

<h2 class="name">NAME</h2>
<p> zipgrep &#8211; search files in a ZIP archive for lines matching a pattern </p>
<h2>SYNOPSIS</h2>
<p> <code>zipgrep</code> [<code>egrep_options</code>] <i>pattern</i> <i>file</i>[<i>.zip</i>] [<i>file(s)</i>&nbsp;&#8230;] [<code>-x</code>&nbsp;<i>xfile(s)</i>&nbsp;&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <i>zipgrep</i> will search files within a ZIP archive for lines matching the given string or pattern. <i>zipgrep</i> is a shell script and requires <i><a href="/docs/linux/man/1-egrep/">egrep</a></i>(1) and <i><a href="/docs/linux/man/1-unzip/">unzip</a></i>(1) to function. Its output is identical to that of <i><a href="/docs/linux/man/1-egrep/">egrep</a></i>(1).</p>
<h2>ARGUMENTS</h2>
<dl>
<dt>
<dt><i>pattern</i></p>
<dd>
<dd> The pattern to be located within a ZIP archive. Any string or regular expression accepted by <i><a href="/docs/linux/man/1-egrep/">egrep</a></i>(1) may be used. <i>file</i>[<i>.zip</i>] Path of the ZIP archive. (Wildcard expressions for the ZIP archive name are not supported.) If the literal filename is not found, the suffix .zip is appended. Note that self-extracting ZIP files are supported, as with any other ZIP archive; just specify the .exe suffix (if any) explicitly.</p>
<dt>[<i>file(s)</i>]</p>
<dd> An optional list of archive members to be processed, separated by spaces. If no member files are specified, all members of the ZIP archive are searched. Regular expressions (wildcards) may be used to match multiple members:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> matches a sequence of 0 or more characters</p>
<dt>?</p>
<dd> matches exactly 1 character</p>
<dt>[&#8230;]</p>
<dd> matches any single character found inside the brackets; ranges are specified by a beginning character, a hyphen, and an ending character. If an exclamation point or a caret (`!&#8217; or `^&#8217;) follows the left bracket, then the range of characters within the brackets is complemented (that is, anything <i>except</i> the characters inside the brackets is considered a match).</dl>
</dl>
<dt>
<dd> (Be sure to quote any character that might otherwise be interpreted or modified by the operating system.)</p>
<dt>[<code>-x</code>&nbsp;<i>xfile(s)</i>]</p>
<dd> An optional list of archive members to be excluded from processing. Since wildcard characters match directory separators (`/&#8217;), this option may be used to exclude any files that are in subdirectories. For example, &#8220;zipgrep grumpy foo *.[ch] -x */*&#8221; would search for the string &#8220;grumpy&#8221; in all C source files in the main directory of the &#8220;foo&#8221; archive, but none in any subdirectories. Without the <code>-x</code> option, all C source files in all directories within the zipfile would be searched.</dl>
<h2>OPTIONS</h2>
<p> All options prior to the ZIP archive filename are passed to <i><a href="/docs/linux/man/1-egrep/">egrep</a></i>(1).</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-egrep/">egrep</a></i>(1), <i><a href="/docs/linux/man/1-unzip/">unzip</a></i>(1), <i><a href="/docs/linux/man/1-zip/">zip</a></i>(1), <i><a href="/docs/linux/man/1-funzip/">funzip</a></i>(1), <i><a href="/docs/linux/man/1-zipcloak/">zipcloak</a></i>(1), <i><a href="/docs/linux/man/1-zipinfo/">zipinfo</a></i>(1), <i><a href="/docs/linux/man/1-zipnote/">zipnote</a></i>(1), <i><a href="/docs/linux/man/1-zipsplit/">zipsplit</a></i>(1)</p>
<h2>URL</h2>
<p> The Info-ZIP home page is currently at <a rel="nofollow" href="http://www.info-zip.org/pub/infozip/">http://www.info-zip.org/pub/infozip/</a> or <a href="ftp://ftp.info-zip.org/pub/infozip/">ftp://ftp.info-zip.org/pub/infozip/</a> .</p>
<h2>AUTHORS</h2>
<p> <i>zipgrep</i> was written by Jean-loup Gailly. </p>
<h2>Index</h2>
