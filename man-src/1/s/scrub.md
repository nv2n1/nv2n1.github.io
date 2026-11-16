---
title: "scrub(1)"
name: "scrub"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scrub/"
description: "scrub – write patterns on disk/file"
---

<h2 class="name">NAME</h2>
<p> scrub &#8211; write patterns on disk/file </p>
<h2>SYNOPSIS</h2>
<p> <code>scrub</code> <i>[OPTIONS] special-file [special-file &#8230;]</i><br />
 <code>scrub</code> <i>[OPTIONS] file [file &#8230;]</i><br />
 <code>scrub</code> <i>-X [OPTIONS] directory</i></p>
<h2>DESCRIPTION</h2>
<p> <code>Scrub</code> iteratively writes patterns on files or disk devices to make retrieving the data more difficult. <code>Scrub </code> operates in one of three modes: </p>
<p> 1) The special file corresponding to an entire disk is scrubbed and all data on it is destroyed. This mode is selected if <i>file</i> is a character or block special file. This is the most effective method. </p>
<p> 2) A regular file is scrubbed and only the data in the file (and optionally its name in the directory entry) is destroyed. The file size is rounded up to fill out the last file system block. This mode is selected if <i>file</i> is a regular file. See CAVEATS below. </p>
<p> 3) <i>directory</i> is created and filled with files until the file system is full, then the files are scrubbed as in 2). This mode is selected with the <i>-X </i> option. See CAVEATS below.</p>
<h2>OPTIONS</h2>
<p> <code>Scrub </code> accepts the following options:</p>
<dl>
<dt><i>-v</i>, <i>&#8211;version</i></dt>
<dd> Print scrub version and exit.</dd>
<dt><i>-r</i>, <i>&#8211;remove</i></dt>
<dd> Remove the file after scrubbing.</dd>
<dt><i>-p</i>, <i>&#8211;pattern</i> <i>PATTERN</i></dt>
<dd> Select the patterns to write. See SCRUB METHODS below. The default, <i>nnsa</i>, is reasonable for sanitizing modern PRML/EPRML encoded disk devices.</dd>
<dt><i>-b</i>, <i>&#8211;blocksize</i> <i>blocksize</i></dt>
<dd> Perform <a href="/docs/linux/man/2-read/">read</a>(2) and <a href="/docs/linux/man/2-write/">write</a>(2) calls using the specified blocksize (in bytes). <i>K,</i> <i>M,</i> or <i>G</i> may be appended to the number to change the units to KiBytes, MiBytes, or GiBytes, respectively. Default: 4M.</dd>
<dt><i>-f</i>, <i>&#8211;force</i></dt>
<dd> Scrub even if target contains signature indicating it has already been scrubbed.</dd>
<dt><i>-S</i>, <i>&#8211;no-signature</i></dt>
<dd> Do not write scrub signature. Later, <code>scrub </code> will not be able to ascertain if the disk has already been scrubbed.</dd>
<dt><i>-X</i>, <i>&#8211;freespace</i></dt>
<dd> Create specified directory and fill it with files until write returns ENOSPC (file system full), then scrub the files as usual. The size of each file can be set with <i>-s</i>, otherwise it will be the maximum file size creatable given the user&#8217;s file size limit or 1g if unlimited.</dd>
<dt><i>-D</i>, <i>&#8211;dirent</i> <i>newname</i></dt>
<dd> After scrubbing the file, scrub its name in the directory entry, then rename it to the new name. The scrub patterns used on the directory entry are constrained by the operating system and thus are not compliant with cited standards. This option only works with a single target.</dd>
<dt><i>-s</i>, <i>&#8211;device-size</i> <i>size</i></dt>
<dd> Override the device size (in bytes). Without this option, <code>scrub</code> determines media capacity using OS-specific <a href="/docs/linux/man/2-ioctl/">ioctl</a>(2) calls. <i>K,</i> <i>M,</i> or <i>G</i> may be appended to the number to change the units to KiBytes, MiBytes, or GiBytes, respectively.</dd>
<dt><i>-L</i>, <i>&#8211;no-link</i></dt>
<dd> If <i>file</i> is a symbolic link, do not scrub the link target. Do remove it, however, if <i>&#8211;remove</i> is specified.</dd>
<dt><i>-R</i>, <i>&#8211;no-hwrand</i></dt>
<dd> Don&#8217;t use a hardware random number generator even if one is available.</dd>
<dt><i>-t</i>, <i>&#8211;no-threads</i></dt>
<dd> Don&#8217;t generate random data in parallel with I/O.</dd>
<dt><i>-n</i>, <i>&#8211;dry-run</i></dt>
<dd> Do everything but write to targets.</dd>
<dt><i>-h</i>, <i>&#8211;help</i></dt>
<dd> Print a summary of command line options on stderr.</dd></dl>
<h2>SCRUB METHODS</h2>
<dl>
<dt><i>nnsa</i></dt>
<dd> 4-pass NNSA Policy Letter NAP-14.1-C (XVI-8) for sanitizing removable and non-removable hard disks, which requires overwriting all locations with a pseudorandom pattern twice and then with a known pattern: <code>random(x2), 0x00, verify</code>.</dd>
<dt><i>dod</i></dt>
<dd> 4-pass DoD 5220.22-M section 8-306 procedure (d) for sanitizing removable and non-removable rigid disks which requires overwriting all addressable locations with a character, its complement, a random character, then verify. NOTE: <code>scrub</code> performs the random pass first to make verification easier: <code>random, 0x00, 0xff, verify</code>.</dd>
<dt><i>bsi</i></dt>
<dd> 9-pass method recommended by the German Center of Security in Information Technologies (<a rel="nofollow" href="http://www.bsi.bund.de">http://www.bsi.bund.de</a>): <code>0xff, 0xfe, 0xfd, 0xfb, 0xf7, 0xef, 0xdf, 0xbf, 0x7f</code>.</dd>
<dt><i>gutmann</i></dt>
<dd> The canonical 35-pass sequence described in Gutmann&#8217;s paper cited below.</dd>
<dt><i>schneier</i></dt>
<dd> 7-pass method described by Bruce Schneier in &quot;Applied Cryptography&quot; (1996): <code>0x00, 0xff, random(x5)</code></dd>
<dt><i>pfitzner7</i></dt>
<dd> Roy Pfitzner&#8217;s 7-random-pass method: <code>random(x7)</code>.</dd>
<dt><i>pfitzner33</i></dt>
<dd> Roy Pfitzner&#8217;s 33-random-pass method: <code>random(x33)</code>.</dd>
<dt><i>usarmy</i></dt>
<dd> US Army AR380-19 method: <code>0x00, 0xff, random</code>. (Note: identical to DoD 522.22-M section 8-306 procedure (e) for sanitizing magnetic core memory).</dd>
<dt><i>fillzero</i></dt>
<dd> 1-pass pattern: <code>0x00</code>.</dd>
<dt><i>fillff</i></dt>
<dd> 1-pass pattern: <code>0xff</code>.</dd>
<dt><i>random</i></dt>
<dd> 1-pass pattern: <code>random(x1)</code>.</dd>
<dt><i>random2</i></dt>
<dd> 2-pass pattern: <code>random(x2)</code>.</dd>
<dt><i>old</i></dt>
<dd> 6-pass pre-version 1.7 scrub method: <code>0x00, 0xff, 0xaa, 0x00, 0x55, verify</code>.</dd>
<dt><i>fastold</i></dt>
<dd> 5-pass pattern: <code>0x00, 0xff, 0xaa, 0x55, verify</code>.</dd>
<dt><i>custom=string</i></dt>
<dd> 1-pass custom pattern. String may contain C-style numerical escapes: 
nn (octal) or 
</dd></dl>