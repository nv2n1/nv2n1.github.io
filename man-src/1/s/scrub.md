---

title: "scrub(1)"
name: "scrub"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scrub/"
description: "scrub – write patterns on disk/file"
---

<p> scrub - write patterns on disk/file </p>
<h2>SYNOPSIS</h2>
<p> <code>scrub</code> <i>[OPTIONS] special-file [special-file ...]</i> <br />
 <code>scrub</code> <i>[OPTIONS] file [file ...]</i> <br />
 <code>scrub</code> <i>-X [OPTIONS] directory</i>  </p>
<h2>DESCRIPTION</h2>
<p> <code>Scrub</code> iteratively writes patterns on files or disk devices to make retrieving the data more difficult. <code>Scrub </code> operates in one of three modes: </p>
<p> 1) The special file corresponding to an entire disk is scrubbed and all data on it is destroyed. This mode is selected if <i>file</i> is a character or block special file. This is the most effective method. </p>
<p> 2) A regular file is scrubbed and only the data in the file (and optionally its name in the directory entry) is destroyed. The file size is rounded up to fill out the last file system block. This mode is selected if <i>file</i> is a regular file. See CAVEATS below. </p>
<p> 3) <i>directory</i> is created and filled with files until the file system is full, then the files are scrubbed as in 2). This mode is selected with the <i>-X </i> option. See CAVEATS below.  </p>
<h2>OPTIONS</h2>
<p> <code>Scrub </code> accepts the following options: </p>
<dl>
<dt><i>-v</i>, <i>--version</i></dt>
<dd> <p> Print scrub version and exit. </p>
 </dd>
<dt><i>-r</i>, <i>--remove</i></dt>
<dd> <p> Remove the file after scrubbing. </p>
 </dd>
<dt><i>-p</i>, <i>--pattern</i><i>PATTERN</i></dt>
<dd> <p> Select the patterns to write. See SCRUB METHODS below. The default, <i>nnsa</i>, is reasonable for sanitizing modern PRML/EPRML encoded disk devices. </p>
 </dd>
<dt><i>-b</i>, <i>--blocksize</i><i>blocksize</i></dt>
<dd> <p> Perform <a href="/docs/linux/man/2-read/">read</a>(2) and <a href="/docs/linux/man/2-write/">write</a>(2) calls using the specified blocksize (in bytes). <i>K,</i> <i>M,</i> or <i>G</i> may be appended to the number to change the units to KiBytes, MiBytes, or GiBytes, respectively. Default: 4M. </p>
 </dd>
<dt><i>-f</i>, <i>--force</i></dt>
<dd> <p> Scrub even if target contains signature indicating it has already been scrubbed. </p>
 </dd>
<dt><i>-S</i>, <i>--no-signature</i></dt>
<dd> <p> Do not write scrub signature. Later, <code>scrub </code> will not be able to ascertain if the disk has already been scrubbed. </p>
 </dd>
<dt><i>-X</i>, <i>--freespace</i></dt>
<dd> <p> Create specified directory and fill it with files until write returns ENOSPC (file system full), then scrub the files as usual. The size of each file can be set with <i>-s</i>, otherwise it will be the maximum file size creatable given the user&#8217;s file size limit or 1g if unlimited. </p>
 </dd>
<dt><i>-D</i>, <i>--dirent</i><i>newname</i></dt>
<dd> <p> After scrubbing the file, scrub its name in the directory entry, then rename it to the new name. The scrub patterns used on the directory entry are constrained by the operating system and thus are not compliant with cited standards. This option only works with a single target. </p>
 </dd>
<dt><i>-s</i>, <i>--device-size</i><i>size</i></dt>
<dd> <p> Override the device size (in bytes). Without this option, <code>scrub</code> determines media capacity using OS-specific <a href="/docs/linux/man/2-ioctl/">ioctl</a>(2) calls. <i>K,</i> <i>M,</i> or <i>G</i> may be appended to the number to change the units to KiBytes, MiBytes, or GiBytes, respectively. </p>
 </dd>
<dt><i>-L</i>, <i>--no-link</i></dt>
<dd> <p> If <i>file</i> is a symbolic link, do not scrub the link target. Do remove it, however, if <i>--remove</i> is specified. </p>
 </dd>
<dt><i>-R</i>, <i>--no-hwrand</i></dt>
<dd> <p> Don&#8217;t use a hardware random number generator even if one is available. </p>
 </dd>
<dt><i>-t</i>, <i>--no-threads</i></dt>
<dd> <p> Don&#8217;t generate random data in parallel with I/O. </p>
 </dd>
<dt><i>-n</i>, <i>--dry-run</i></dt>
<dd> <p> Do everything but write to targets. </p>
 </dd>
<dt><i>-h</i>, <i>--help</i></dt>
<dd> <p> Print a summary of command line options on stderr. </p>
 </dd></dl>
<h2>SCRUB METHODS</h2>
<dl>
<dt><i>nnsa</i></dt>
<dd> <p> 4-pass NNSA Policy Letter NAP-14.1-C (XVI-8) for sanitizing removable and non-removable hard disks, which requires overwriting all locations with a pseudorandom pattern twice and then with a known pattern: <code>random(x2), 0x00, verify</code>. </p>
 </dd>
<dt><i>dod</i></dt>
<dd> <p> 4-pass DoD 5220.22-M section 8-306 procedure (d) for sanitizing removable and non-removable rigid disks which requires overwriting all addressable locations with a character, its complement, a random character, then verify. NOTE: <code>scrub</code> performs the random pass first to make verification easier: <code>random, 0x00, 0xff, verify</code>. </p>
 </dd>
<dt><i>bsi</i></dt>
<dd> <p> 9-pass method recommended by the German Center of Security in Information Technologies (<a rel="nofollow" href="http://www.bsi.bund.de">http://www.bsi.bund.de</a>): <code>0xff, 0xfe, 0xfd, 0xfb, 0xf7, 0xef, 0xdf, 0xbf, 0x7f</code>. </p>
 </dd>
<dt><i>gutmann</i></dt>
<dd> <p> The canonical 35-pass sequence described in Gutmann&#8217;s paper cited below. </p>
 </dd>
<dt><i>schneier</i></dt>
<dd> <p> 7-pass method described by Bruce Schneier in &quot;Applied Cryptography&quot; (1996): <code>0x00, 0xff, random(x5)</code> </p>
 </dd>
<dt><i>pfitzner7</i></dt>
<dd> <p> Roy Pfitzner&#8217;s 7-random-pass method: <code>random(x7)</code>. </p>
 </dd>
<dt><i>pfitzner33</i></dt>
<dd> <p> Roy Pfitzner&#8217;s 33-random-pass method: <code>random(x33)</code>. </p>
 </dd>
<dt><i>usarmy</i></dt>
<dd> <p> US Army AR380-19 method: <code>0x00, 0xff, random</code>. (Note: identical to DoD 522.22-M section 8-306 procedure (e) for sanitizing magnetic core memory). </p>
 </dd>
<dt><i>fillzero</i></dt>
<dd> <p> 1-pass pattern: <code>0x00</code>. </p>
 </dd>
<dt><i>fillff</i></dt>
<dd> <p> 1-pass pattern: <code>0xff</code>. </p>
 </dd>
<dt><i>random</i></dt>
<dd> <p> 1-pass pattern: <code>random(x1)</code>. </p>
 </dd>
<dt><i>random2</i></dt>
<dd> <p> 2-pass pattern: <code>random(x2)</code>. </p>
 </dd>
<dt><i>old</i></dt>
<dd> <p> 6-pass pre-version 1.7 scrub method: <code>0x00, 0xff, 0xaa, 0x00, 0x55, verify</code>. </p>
 </dd>
<dt><i>fastold</i></dt>
<dd> <p> 5-pass pattern: <code>0x00, 0xff, 0xaa, 0x55, verify</code>. </p>
 </dd>
<dt><i>custom=string</i></dt>
<dd> <p> 1-pass custom pattern. String may contain C-style numerical escapes: \nnn (octal) or \xnn (hex). </p>
 </dd></dl>
<h2>CAVEATS</h2>
<p> <code>Scrub </code> may be insufficient to thwart heroic efforts to recover data in an appropriately equipped lab. If you need this level of protection, physical destruction is your best bet. </p>
<p> The effectiveness of scrubbing regular files through a file system will be limited by the OS and file system. File systems that are known to be problematic are journaled, log structured, copy-on-write, versioned, and network file systems. If in doubt, scrub the raw disk device. </p>
<p> Scrubbing free blocks in a file system with the <i>-X</i> method is subject to the same caveats as scrubbing regular files, and in addition, is only useful to the extent the file system allows you to reallocate the target blocks as data blocks in a new file. If in doubt, scrub the raw disk device. </p>
<p> On MacOS X HFS file system, <code>scrub </code> attempts to overwrite a file&#8217;s resource fork if it exists. Although MacOS X claims it will support additional named forks in the future, <code>scrub </code> is only aware of the traditional data and resource forks. </p>
<p> <code>scrub</code> cannot access disk blocks that have been spared out by the disk controller. For SATA/PATA drives, the ATA &quot;security erase&quot; command built into the drive controller can do this. Similarly, the ATA &quot;enhanced security erase&quot; can erase data on track edges and between tracks. The DOS utility HDDERASE from the UCSD Center for Magnetic Recording Research can issue these commands, as can modern versions of Linux <code>hdparm</code>. Unfortunately, the analogous SCSI command is optional according to T-10, and not widely implemented.  </p>
<h2>EXAMPLES</h2>
<p> To scrub a raw device <i>/dev/sdf1</i> with default NNSA patterns: </p>
<dl>
<dd> <pre><code># scrub /dev/sdf1
scrub: using NNSA NAP-14.1-C patterns
scrub: please verify that device size below is correct!
scrub: scrubbing /dev/sdf1 1995650048 bytes (~1GB)
scrub: random |................................................|
scrub: random |................................................|
scrub: 0x00 |................................................|
scrub: verify |................................................|
</code></pre>
 </dd></dl>
<p> To scrub the file <i>/tmp/scrubme</i> with a sequence of 0xff 0xaa bytes: </p>
<dl>
<dd> <pre><code># scrub -p custom=&quot;\xff\xaa&quot; /tmp/scrubme
scrub: using Custom single-pass patterns
scrub: scrubbing /tmp/scrubme 78319616 bytes (~74MB)
scrub: 0xffaa |................................................|
</code></pre>
 </dd></dl>
<h2>AUTHOR</h2>
<p> Jim Garlick &lt;garlick [at] llnl.gov&gt; </p>
<p> This work was produced at the University of California, Lawrence Livermore National Laboratory under Contract No. W-7405-ENG-48 with the DOE. Designated UCRL-CODE-2003-006, scrub is licensed under terms of the GNU General Public License.  </p>
<h2>SEE ALSO</h2>
<p> DoD 5220.22-M, &quot;National Industrial Security Program Operating Manual&quot;, Chapter 8, 01/1995. </p>
<p> NNSA Policy Letter: NAP-14.1-C, &quot;Clearing, Sanitizing, and Destroying Information System Storage Media, Memory Devices, and other Related Hardware&quot;, 05-02-08, page XVI-8. </p>
<p> &quot;Secure Deletion of Data from Magnetic and Solid-State Memory&quot;, by Peter Gutmann, Sixth USENIX Security Symposium, San Jose, CA, July 22-25, 1996. </p>
<p> &quot;Gutmann Method&quot;, Wikipedia, <a rel="nofollow" href="http://en.wikipedia.org/wiki/Gutmann_method.">http://en.wikipedia.org/wiki/Gutmann_method.</a> </p>
<p> Darik&#8217;s boot and Nuke FAQ: <a rel="nofollow" href="http://dban.sourceforge.net/faq/index.html">http://dban.sourceforge.net/faq/index.html</a> </p>
<p> &quot;Tutorial on Disk Drive Data Sanitization&quot;, by Gordon Hugues and Tom Coughlin, <br />
 <a rel="nofollow" href="http://cmrr.ucsd.edu/people/Hughes/DataSanitizationTutorial.pdf.">http://cmrr.ucsd.edu/people/Hughes/DataSanitizationTutorial.pdf.</a> </p>
<p> &quot;Guidelines for Media Sanitization&quot;, NIST special publication 800-88, Kissel et al, September, 2006. </p>
<p> <a href="/docs/linux/man/1-shred/">shred</a>(1), <a href="/docs/linux/man/8-hdparm/">hdparm</a>(8) </p>
