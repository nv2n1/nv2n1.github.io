---
title: "srm(1)"
name: "srm"
section: "1"
letter: "s"
url: "/docs/linux/man/1-srm/"
description: "srm – securely remove files or directories"
---

<h2>NAME</h2>
<p> srm &#8211; securely remove files or directories</p>
<h2>SYNOPSIS</h2>
<p> <code>srm</code> [<i>OPTION</i>]&#8230; <i>FILE</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>srm</code> removes each specified file by overwriting, renaming, and truncating it before unlinking. This prevents other people from undeleting or recovering any information about the file from the command line. By default srm uses the simple mode to overwrite the file&#8217;s contents. You can choose a different overwrite mode with <code>&#8211;dod</code>, <code>&#8211;doe</code>, <code>&#8211;openbsd</code>, <code>&#8211;rcmp</code>, <code>&#8211;gutmann</code>. If you specify more than one mode option, the last option is used. </p>
<p> You can use <code>srm</code> to overwrite block devices. The device node is not removed after overwriting. This feature is available on Linux. Files with multiple hard links will be unlinked but not overwritten. </p>
<p> <code>srm</code>, like every program that uses the getopt function to parse its arguments, lets you use the &#8212; option to indicate that all following arguments are non-options. To remove a file called `-f&#8217; in the current directory, you could type either</p>
<dl>
<dt>
<dd> rm &#8212; -f</dl>
<p> or</p>
<dl>
<dt>
<dd> rm ./-f</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;directory</code></p>
<dd> ignored (for compatibility with <code><a href="/docs/linux/man/1-rm/">rm</a>(1)</code>)</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> ignore nonexistent files, never prompt</p>
<dt><code>-i</code>, <code>&#8211;interactive</code></p>
<dd> prompt before any removal</p>
<dt><code>-r</code>, <code>-R</code>, <code>&#8211;recursive</code></p>
<dd> remove the contents of directories recursively</p>
<dt><code>-x</code>, <code>&#8211;one-file-system</code></p>
<dd> when removing a hierarchy recursively, skip any directory that is on a file system different from that of the corresponding command line argument. (Not supported on Windows)</p>
<dt><code>-s</code>, <code>&#8211;simple</code></p>
<dd> Overwrite the file with a single pass of 0x00 bytes. This is the default mode.</p>
<dt><code>-P</code>, <code>&#8211;openbsd</code></p>
<dd> OpenBSD compatible rm. Files are overwritten three times, first with the byte 0xFF, then 0x00, and then 0xFF again, before they are deleted.</p>
<dt><code>-D</code>, <code>&#8211;dod</code></p>
<dd> US Dod compliant 7-pass overwrite.</p>
<dt><code>-E</code>, <code>&#8211;doe</code></p>
<dd> US DoE compliant 3-pass overwrite. Twice with a random pattern, finally with the bytes &quot;DoE&quot;. See <a rel="nofollow" href="http://cio.energy.gov/CS-11_Clearing_and_Media_Sanitization_Guidance.pdf">http://cio.energy.gov/CS-11_Clearing_and_Media_Sanitization_Guidance.pdf</a> for details.</p>
<dt><code>-G</code>, <code>&#8211;gutmann</code></p>
<dd> Use the 35-pass Gutmann method. See <a rel="nofollow" href="http://en.wikipedia.org/wiki/Gutmann_method">http://en.wikipedia.org/wiki/Gutmann_method</a> for details.</p>
<dt><code>-C</code>, <code>&#8211;rcmp</code></p>
<dd> Royal Canadian Mounted Police compliant 3-pass overwrite. First pass writes 0x00 bytes. Second pass writes 0xFF bytes. Third pass writes &quot;RCMP&quot;. See <a rel="nofollow" href="https://www.cse-cst.gc.ca/en/node/270/html/10572">https://www.cse-cst.gc.ca/en/node/270/html/10572</a> for details.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> explain what is being done. Specify this option multiple times to increase verbosity.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display this help and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> output version information and exit.</dl>
<h2>SIGNALS</h2>
<dl>
<dt><code>SIGINFO, SIGUSR2</code></p>
<dd> show current write position and filename handled.</dl>
<h2>ENTIRE HARD DISKS</h2>
<p> <code>srm</code> can write to block devices on Linux. You can use srm to securely delete an entire hard disk, however you should only do this for classic magnetic drives. The modern solid state disks (SSD) have a faster and better way to erase all contents, <i>Secure Erase.</i> For a Linux operating system see <a rel="nofollow" href="https://ata.wiki.kernel.org/index.php/ATA_Secure_Erase">https://ata.wiki.kernel.org/index.php/ATA_Secure_Erase</a></p>
<h2>NOTES</h2>
<p> <code>srm</code> can not remove write protected files owned by another user, regardless of the permissions on the directory containing the file. </p>
<p> Development and discussion of srm is carried out at <a rel="nofollow" href="https://sourceforge.net/projects/srm/">https://sourceforge.net/projects/srm/</a> which is also accessible via <a rel="nofollow" href="http://srm.sourceforge.net/.">http://srm.sourceforge.net/.</a> See <a rel="nofollow" href="http://en.wikipedia.org/wiki/Data_remanence">http://en.wikipedia.org/wiki/Data_remanence</a> for a general discussion about overwriting data.</p>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/1-rm/">rm</a>(1)</code></p>
<dd> <a rel="nofollow" href="http://www.gnu.org/software/coreutils/manual/coreutils.html#rm-invocation">http://www.gnu.org/software/coreutils/manual/coreutils.html#rm-invocation</a></p>
<dt><code><a href="/docs/linux/man/1-shred/">shred</a>(1)</code></p>
<dd> <a rel="nofollow" href="http://www.gnu.org/software/coreutils/manual/coreutils.html#shred-invocation">http://www.gnu.org/software/coreutils/manual/coreutils.html#shred-invocation</a></p>
<dt><code><a href="/docs/linux/man/1-wipe/">wipe</a>(1)</code></p>
<dd> <a rel="nofollow" href="http://lambda-diode.com/software/wipe">http://lambda-diode.com/software/wipe</a></p>
<dt><code>secure-delete</code></p>
<dd> <a rel="nofollow" href="http://packages.debian.org/lenny/secure-delete">http://packages.debian.org/lenny/secure-delete</a></p>
<dt><code><a href="/docs/linux/man/1-scrub/">scrub</a>(1)</code></p>
<dd> <a rel="nofollow" href="http://code.google.com/p/diskscrub/">http://code.google.com/p/diskscrub/</a> </p>
</dl>
<h2>Index</h2>
