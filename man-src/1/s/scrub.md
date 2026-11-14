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
<dt><i>-v</i>, <i>&#8211;version</i></p>
<dd> Print scrub version and exit.</p>
<dt><i>-r</i>, <i>&#8211;remove</i></p>
<dd> Remove the file after scrubbing.</p>
<dt><i>-p</i>, <i>&#8211;pattern</i> <i>PATTERN</i></p>
<dd> Select the patterns to write. See SCRUB METHODS below. The default, <i>nnsa</i>, is reasonable for sanitizing modern PRML/EPRML encoded disk devices.</p>
<dt><i>-b</i>, <i>&#8211;blocksize</i> <i>blocksize</i></p>
<dd> Perform <a href="/docs/linux/man/2-read/">read</a>(2) and <a href="/docs/linux/man/2-write/">write</a>(2) calls using the specified blocksize (in bytes). <i>K,</i> <i>M,</i> or <i>G</i> may be appended to the number to change the units to KiBytes, MiBytes, or GiBytes, respectively. Default: 4M.</p>
<dt><i>-f</i>, <i>&#8211;force</i></p>
<dd> Scrub even if target contains signature indicating it has already been scrubbed.</p>
<dt><i>-S</i>, <i>&#8211;no-signature</i></p>
<dd> Do not write scrub signature. Later, <code>scrub </code> will not be able to ascertain if the disk has already been scrubbed.</p>
<dt><i>-X</i>, <i>&#8211;freespace</i></p>
<dd> Create specified directory and fill it with files until write returns ENOSPC (file system full), then scrub the files as usual. The size of each file can be set with <i>-s</i>, otherwise it will be the maximum file size creatable given the user&#8217;s file size limit or 1g if unlimited.</p>
<dt><i>-D</i>, <i>&#8211;dirent</i> <i>newname</i></p>
<dd> After scrubbing the file, scrub its name in the directory entry, then rename it to the new name. The scrub patterns used on the directory entry are constrained by the operating system and thus are not compliant with cited standards. This option only works with a single target.</p>
<dt><i>-s</i>, <i>&#8211;device-size</i> <i>size</i></p>
<dd> Override the device size (in bytes). Without this option, <code>scrub</code> determines media capacity using OS-specific <a href="/docs/linux/man/2-ioctl/">ioctl</a>(2) calls. <i>K,</i> <i>M,</i> or <i>G</i> may be appended to the number to change the units to KiBytes, MiBytes, or GiBytes, respectively.</p>
<dt><i>-L</i>, <i>&#8211;no-link</i></p>
<dd> If <i>file</i> is a symbolic link, do not scrub the link target. Do remove it, however, if <i>&#8211;remove</i> is specified.</p>
<dt><i>-R</i>, <i>&#8211;no-hwrand</i></p>
<dd> Don&#8217;t use a hardware random number generator even if one is available.</p>
<dt><i>-t</i>, <i>&#8211;no-threads</i></p>
<dd> Don&#8217;t generate random data in parallel with I/O.</p>
<dt><i>-n</i>, <i>&#8211;dry-run</i></p>
<dd> Do everything but write to targets.</p>
<dt><i>-h</i>, <i>&#8211;help</i></p>
<dd> Print a summary of command line options on stderr.</dl>
<h2>SCRUB METHODS</h2>
<dl>
<dt><i>nnsa</i></p>
<dd> 4-pass NNSA Policy Letter NAP-14.1-C (XVI-8) for sanitizing removable and non-removable hard disks, which requires overwriting all locations with a pseudorandom pattern twice and then with a known pattern: <code>random(x2), 0x00, verify</code>.</p>
<dt><i>dod</i></p>
<dd> 4-pass DoD 5220.22-M section 8-306 procedure (d) for sanitizing removable and non-removable rigid disks which requires overwriting all addressable locations with a character, its complement, a random character, then verify. NOTE: <code>scrub</code> performs the random pass first to make verification easier: <code>random, 0x00, 0xff, verify</code>.</p>
<dt><i>bsi</i></p>
<dd> 9-pass method recommended by the German Center of Security in Information Technologies (<a rel="nofollow" href="http://www.bsi.bund.de">http://www.bsi.bund.de</a>): <code>0xff, 0xfe, 0xfd, 0xfb, 0xf7, 0xef, 0xdf, 0xbf, 0x7f</code>.</p>
<dt><i>gutmann</i></p>
<dd> The canonical 35-pass sequence described in Gutmann&#8217;s paper cited below.</p>
<dt><i>schneier</i></p>
<dd> 7-pass method described by Bruce Schneier in &quot;Applied Cryptography&quot; (1996): <code>0x00, 0xff, random(x5)</code></p>
<dt><i>pfitzner7</i></p>
<dd> Roy Pfitzner&#8217;s 7-random-pass method: <code>random(x7)</code>.</p>
<dt><i>pfitzner33</i></p>
<dd> Roy Pfitzner&#8217;s 33-random-pass method: <code>random(x33)</code>.</p>
<dt><i>usarmy</i></p>
<dd> US Army AR380-19 method: <code>0x00, 0xff, random</code>. (Note: identical to DoD 522.22-M section 8-306 procedure (e) for sanitizing magnetic core memory).</p>
<dt><i>fillzero</i></p>
<dd> 1-pass pattern: <code>0x00</code>.</p>
<dt><i>fillff</i></p>
<dd> 1-pass pattern: <code>0xff</code>.</p>
<dt><i>random</i></p>
<dd> 1-pass pattern: <code>random(x1)</code>.</p>
<dt><i>random2</i></p>
<dd> 2-pass pattern: <code>random(x2)</code>.</p>
<dt><i>old</i></p>
<dd> 6-pass pre-version 1.7 scrub method: <code>0x00, 0xff, 0xaa, 0x00, 0x55, verify</code>.</p>
<dt><i>fastold</i></p>
<dd> 5-pass pattern: <code>0x00, 0xff, 0xaa, 0x55, verify</code>.</p>
<dt><i>custom=string</i></p>
<dd> 1-pass custom pattern. String may contain C-style numerical escapes: 
nn (octal) or 
