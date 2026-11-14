---
title: "microcode_ctl(8)"
name: "microcode_ctl"
section: "8"
letter: "m"
url: "/docs/linux/man/8-microcode_ctl/"
description: "microcode_ctl – microcode utility for Intel IA32 processors"
---

<p>microcode_ctl &#8211; microcode utility for Intel IA32 processors</p>
<h2>Synopsis</h2>
<p><code>microcode_ctl</code> [<i>-h</i>] [<i>-u</i> [<i>-q</i>]] [<i>-Q</i>] [<i>-f microcode</i>]</p>
<h2>Description</h2>
<p>The microcode_ctl utility is a companion to the IA32 microcode driver written by Tigran Aivazian &lt;tigran [at] aivazian.fsnet.co.uk&gt;. The utility has two uses: </p>
<p> <code>a)</code> it decodes and sends new microcode to the kernel driver to be uploaded to Intel IA32 processors. (Pentium Pro, PII, Celeron, PIII, Xeon, Pentium 4 etc) </p>
<p> <code>b)</code> it signals the kernel driver to release the buffers containing the copy of microcode data actually applied to given CPU, linear array of 2048 bytes per CPU, see struct microcode in include/asm/processor.h for information on the layout of chunks buffers may hold </p>
<p> The microcode update is volatile and needs to be uploaded on each system boot i.e. it doesn&#8217;t reflash your cpu permanently, reboot and it reverts back to the old microcode. </p>
<dl>
<dt><code>-h</code></p>
<dd>display usage and exit</p>
<dt><code>-u</code></p>
<dd>upload microcode (from default filename)</p>
<dt><code>-f</code></p>
<dd>upload microcode from named Intel formatted file</p>
<dt><code>-q</code></p>
<dd>run silently when successful</p>
<dt><code>-Q</code></p>
<dd>run silently even on failure</dl>
<h2>Example</h2>
<dl>
<dt>microcode_ctl -u</p>
<dd>Upload microcode using defaults</dl>
<h2>Files</h2>
<dl>
<dt>/etc/microcode.dat</p>
<dd>The default microcode location</dl>
<h2>Author</h2>
<p>Microcode utility written by Simon Trimmer<br />
 Linux Kernel driver written by Tigran Aivazian.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to either Simon Trimmer &lt;simon [at] urbanmyth.org&gt; or Tigran Aivazian &lt;tigran [at] aivazian.fsnet.co.uk&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2000 VERITAS Software<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>Special Thanks</h2>
<p>Thanks to the Intel Corporation, for supplying microcode update data and publishing the specifications that enabled us to write microcode driver for Linux.</p>
<h2>See Also</h2>
<p>The brave are recommended to view the driver source code located in the Linux Kernel source tree in arch/i386/kernel/microcode.c Visit <a rel="nofollow" href="http://www.urbanmyth.org/microcode/">http://www.urbanmyth.org/microcode/</a> for more information and microcode updates. </p>
