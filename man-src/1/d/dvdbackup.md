---
title: "dvdbackup(1)"
name: "dvdbackup"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvdbackup/"
description: "dvdbackup – Tool to backup DVDs"
---

<h2 class="name">NAME</h2>
<p> dvdbackup &#8211; Tool to backup DVDs </p>
<h2>SYNOPSIS</h2>
<p> <code>dvdbackup</code> [<i>OPTION</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>dvdbackup</code> command. This manual page was written for the Debian distribution because the original program does not have a manual page. <code>dvdbackup</code> is a tool to extract data from video DVDs. It has the advantages of being small, fast, and easy to use.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> print a brief usage message</p>
<dt><code>-V, &#8211;version</code></p>
<dd> print version information</p>
<dt><code>-I, &#8211;info</code></p>
<dd> for information about the DVD</p>
<dt><code>-M, &#8211;mirror</code></p>
<dd> backup the whole DVD</p>
<dt><code>-F, &#8211;feature</code></p>
<dd> backup the main feature of the DVD</p>
<dt><code>-T X, &#8211;titleset=X</code></p>
<dd> backup title set X</p>
<dt><code>-t X, &#8211;title=X</code></p>
<dd> backup title X</p>
<dt><code>-s X, &#8211;start=X</code></p>
<dd> backup from chapter X</p>
<dt><code>-e X, &#8211;end=X</code></p>
<dd> backup to chapter X</p>
<dt><code>-i DEVICE, &#8211;input=DEVICE</code></p>
<dd> where DEVICE is your DVD device. This switch only needs to be used if your DVD device node is not /dev/dvd</p>
<dt><code>-o DIRECTORY, &#8211;output=DIRECTORY</code></p>
<dd> where DIRECTORY is your backup target. If not given, the current working directory will be used.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> print more information about progress</p>
<dt><code>-n NAME, &#8211;name=NAME</code></p>
<dd> (optional) set the title &#8211; useful if autodetection fails</p>
<dt><code>-a 0, &#8211;aspect=0</code></p>
<dd> to get aspect ratio 4:3 instead of 16:9 if both are present</p>
<dt><code>-r {a,b,m}, &#8211;error={a,b,m}</code></p>
<dd> select read error handling: a=abort, b=skip block, m=skip multiple blocks (default)</p>
<dt><code>-p, &#8211;progress</code></p>
<dd> print progress information while copying VOBs</dl>
<h2>Option notes</h2>
<p> <code>-a</code> is option to the <code>-F</code> switch and has no effect on other options<br />
 <code>-s</code> and <code>-e</code> should preferably be used together with <code>-t</code></p>
<h2>General backup information</h2>
<p> If your backup directory is /my/dvd/backup/dir/ specified with the <code>-o</code> flag, then dvdbackup will create a DVD-Video structure under /my/dvd/backup/dir/TITLE_NAME/VIDEO_TS. If the <code>-o</code> flag is omitted, the current directory is used. </p>
<p> Since the title is &quot;unique&quot; you can use the same directory for all your DVD backups. If it happens to have a generic title dvdbackup will exit with a return value of 2, and you will need to specify a title name with the <code>-n</code> switch. </p>
<p> dvdbackup will always mimic the original DVD-Video structure. Hence if you e.g. use the <code>-M</code> (mirror) you will get an exact duplicate of the original. This means that every file will have the same size as the original one. Likewise also for the <code>-F</code> and the <code>-T</code> switch. </p>
<p> However the <code>-t</code> and (<code>-t -s</code>/<code>-e</code>) switch is a bit different the titles sectors will be written to the original file but not at the same offset as the original one since there may be gaps in the cell structure that we do not fill.</p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>dvdbackup -I</code></p>
<dd> gathers information about the DVD. /dev/dvd is the default device tried &#8211; you need to use <code>-i</code> if your device name is different.</p>
<dt><code>dvdbackup -M</code></p>
<dd> backups the whole DVD. This action creates a valid DVD-Video structure that can be burned to a DVD-/+R(W) with help of genisoimage.</p>
<dt><code>dvdbackup -F</code></p>
<dd> backups the main feature of the DVD. This action creates a valid DVD-Video structure of the feature title set. Note that this will not result in an image immediately watchable &#8211; you will need another program like dvdauthor to help construct the IFO files. </p>
<p> dvdbackup defaults to get the 16:9 version of the main feature if a 4:3 is also present on the DVD. To get the 4:3 version use <code>-a</code> 0. </p>
<p> dvdbackup makes it best to make a intelligent guess what is the main feature of the DVD &#8211; in case it fails please send a bug report.</p>
<dt><code>dvdbackup -T</code><i>&nbsp;<wbr>2</i></p>
<dd> backups the title set <i>2</i> i.e. all VTS_02_X.XXX files. This action creates a valid DVD-Video structure of the specified title set. Note that this will not result in an image immediately watchable &#8211; you will need another program like dvdauthor to help construct the IFO files.</p>
<dt><code>dvdbackup -t</code><i>&nbsp;<wbr>1</i></p>
<dd> backups the title 1. This action backups all cells that forms the specified title. Note that there can be sector gaps in between one cell and another. dvdbackup will backup all sectors that belongs to the title but will skip sectors that are not a part of the title.</p>
<dt><code>dvdbackup -t </code><i>1</i><code> -s </code><i>20</i><code> -e </code><i>25</p>
<dd> This action will backup chapter 20 to 25 in title 1, as with the backup of a title there can be sector gaps between one chapter (cell) and on other. dvdbackup will backup all sectors that belongs to the title 1 chapter 20 to 25 but will skip sectors that are not a part of the title 1 chapter 20 to 25. </p>
<p> To backup a single chapter e.g. chapter 20 do </i><code>-s</code> 20 <code>-e</code> 20.<br />
 To backup from chapter 20 to the end chapter use only <code>-s</code> 20.<br />
 To backup to chapter 20 from the first chapter use only <code>-e</code> 20. </p>
<p> You can skip the <code>-t</code> switch and let the program guess the title although it is not recommended. </p>
<p> If you specify a chapter that is higher than the last chapter of the title dvdbackup will truncate to the highest chapter of the title.</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> on success</p>
<dt><code>1</code></p>
<dd> on usage error</p>
<dt><code>2</code></p>
<dd> on title name error</p>
<dt><code>-1</code></p>
<dd> on failure</dl>
<h2>AUTHORS</h2>
<p> dvdbackup was written by Olaf Beck &lt;olaf_sc [at] yahoo.com&gt;, but is now maintained by Benjamin Drung &lt;benjamin.drung [at] gmail.com&gt; and Stephen Gran &lt;sgran [at] debian.org&gt;. This manual page was written by Stephen Gran &lt;sgran [at] debian.org&gt;. </p>
<h2>Index</h2>
