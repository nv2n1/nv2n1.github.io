---
title: "dar_xform(1)"
name: "dar_xform"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dar_xform/"
description: "dar_xform – disk archive \"re-slicer\""
---

<h2 class="name">NAME</h2>
<p> dar_xform &#8211; disk archive &quot;re-slicer&quot; </p>
<h2>SYNOPSIS</h2>
<p> dar_xform [options] [&lt;path&gt;/]source [&lt;path&gt;/]destination </p>
<p> dar_xform -h </p>
<p> dar_xform -V</p>
<h2>DESCRIPTION</h2>
<p> <code>dar_xform</code> changes the size of slices of an existing archive. </p>
<p> Source is the basename of the existing archive, destination is the basename of the archive to be created. If source basename is &quot;-&quot;, the archive is read from standard input. If the destination basename is &quot;-&quot;, the archive is written to standard output and -s option is not available. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-h</p>
<dd> displays help usage.</p>
<dt>-V</p>
<dd> displays version information.</p>
<dt>-b</p>
<dd> make the terminal ring when user interaction is required (like for example the creation of a new slice when using the -p option)</p>
<dt>-s &lt;number&gt;</p>
<dd> Size of the slices in bytes. If the number is followed by k (or K), M, G, T or P the size is in kilobytes, megabytes, gigabytes, terabytes or petabytes respectively. Example: by default &quot;20M&quot; means 20 megabytes it is the same as giving 20971520 as argument (see also -aSI and -abinary options). If -s is not present the backup will be written to a single slice whatever the size of the backup may be (there is probably some filesystem limitation, thus you might expect problems with file size over 2 gigabytes, depending on your filesystem).</p>
<dt>-S &lt;number&gt;</p>
<dd> -S gives the size of the first slice which may be chosen independently of the size of following slices. This option needs -s and by default, the size of the first slice is the same as the one of the following slices.</p>
<dt>-p [&lt;integer&gt;]</p>
<dd> pauses before writing to a new slice (this requires -s). By default there is no pause, all slices are output in the same directory, up to the end of the backup or until the filesystem is full. In this later case, the user is informed of the lack of disk space and dar stops for user interaction. As soon as some disk space is available, the user can continue the backup. The optional integer that this option can receive tells dar to only pause very &#8216;n&#8217; slice. Giving 3 for &#8216;n&#8217; will make dar pause only after slices 3, 6, 9 and so on. If this integer is not specified, the behavior is as if &#8216;1&#8217; was given as argument which makes dar pause after each slice.</p>
<dt>-n</p>
<dd> Do not allow overwriting of any slice.</p>
<dt>-w</p>
<dd> Do not warn before overwriting slice. By default (no -n and no -w) overwriting is allowed but a warning is issued before proceeding.</p>
<dt>-E &lt;string&gt;</p>
<dd> the string is a command-line to be launched between the slices of the destination archive. See <a href="/docs/linux/man/1-dar/">dar</a>(1) man page (same option) for more information.</p>
<dt>-F &lt;string&gt;</p>
<dd> the string is a command-line to be launched between the slices of the source archive. See <a href="/docs/linux/man/1-dar/">dar</a>(1) man page (same option) for more information.</p>
<dt>-aSI[-unit[s]]</p>
<dd> when using k M G T E Z Y prefixes to define a size, use the SI meaning: multiple of 10^3 (a Mega is 1,000,000).</p>
<dt>-abinary[-unit[s]]</p>
<dd> when using k M G T E Z Y prefixes to define a size, use the historical computer science meaning: multiple of 2^10 (a Mega is 1,048,576).</dl>
<p> -aSI and -abinary can be used several times, they affect all prefix which follow even those found in file included by -B option up to the next -a&#8230; occurrence. Note that if in a file included by -B option an -abinary or -aSI is met, it affects all the following prefix even those outside the included files (for example in the following &quot;-B some.dcf -s 1K&quot; 1K may be equal to 1000 or 1024 depending on the presence of an -aSI or -abinary in the file some.dcf. By default (before any -aSI/binary argument has been reached), binary interpretation of suffix is done (for compatibility with older versions).</p>
<dl>
<dt>-Q</p>
<dd> Do not display any message on stderr when not launched from a terminal (for example when launched from an at job or crontab). Remains that any question to the user will be assumed a &#8216;no&#8217; answer, which most of the time will abort the program.</p>
<dt>-^ perm[:user[:group]]</p>
<dd> defines the permission and ownership to use for created slices.</p>
<dt>-3 &lt;algo&gt;</p>
<dd> Beside each created slice is generated an on-fly hash file using the specified algorithm. Available algorithm are &quot;md5&quot; and &quot;sha1&quot;, by default no hash file is generated. This option description is more detailed in dar man page (where it has the same designation as here).</p>
<dt>-9 &lt;src_num&gt;[,&lt;dst_num&gt;]</p>
<dd> Defines the minimum number of digit to use for the source archive and for the destination archive. If you the source has not been defined with a minimum number of digit and you want to define a value for the destination archive, use zero (or one) as value for src. See the same option in dar man page for more details.</dl>
<h2>NOTES</h2>
<p> Dar_xform is not concerned by encryption or compression. It does not need to be aware of it to be able to change the slice scheme. Thus, it is not able to uncompress or uncipher an archive. </p>
<h2>EXIT CODES</h2>
<p> <code>dar_xform</code> uses the same exit status as dar does, see <a href="/docs/linux/man/1-dar/">dar</a>(1) man page. </p>
<h2>SIGNALS</h2>
<p> Any signal sent to dar_xform will abort the program immediately, there is no way to have a proper termination before the end of the process </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-dar/">dar</a>(1), <a href="/docs/linux/man/1-dar_slave/">dar_slave</a>(1), <a href="/docs/linux/man/1-dar_manager/">dar_manager</a>(1), <a href="/docs/linux/man/1-dar_cp/">dar_cp</a>(1), <a href="/docs/linux/man/1-dar_split/">dar_split</a>(1) </p>
<h2>KNOWN BUGS</h2>
<p> <a rel="nofollow" href="http://sourceforge.net/p/dar/bugs/">http://sourceforge.net/p/dar/bugs/</a> </p>
<h2>AUTHOR</h2>
<pre>
<a rel="nofollow" href="http://dar.linux.free.fr/">http://dar.linux.free.fr/</a>
Denis Corbin
France
Europe
</pre>
<h2>Index</h2>
