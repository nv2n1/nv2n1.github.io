---
title: "readprofile(8)"
name: "readprofile"
section: "8"
letter: "r"
url: "/docs/linux/man/8-readprofile/"
description: "readprofile – read kernel profiling information"
---

<p>readprofile &#8211; read kernel profiling information</p>
<h2>Synopsis</h2>
<p><code>readprofile</code> [options]</p>
<h2>Version</h2>
<p>This manpage documents version 2.0 of the program.</p>
<h2>Description</h2>
<p>The <code>readprofile</code> command uses the <i>/proc/profile</i> information to print ascii data on standard output. The output is organized in three columns: the first is the number of clock ticks, the second is the name of the C function in the kernel where those many ticks occurred, and the third is the normalized `load&#8217; of the procedure, calculated as a ratio between the number of ticks and the length of the procedure. The output is filled with blanks to ease readability.</p>
<h2>Options</h2>
<p><code>-a</code>, <code>&#8211;all</code></p>
<dl>
<dd>Print all symbols in the mapfile. By default the procedures with reported ticks are not printed.</dl>
<p> <code>-b</code>, <code>&#8211;histbin</code></p>
<dl>
<dd>Print individual histogram-bin counts.</dl>
<p> <code>-i</code>, <code>&#8211;info</code></p>
<dl>
<dd>Info. This makes <code>readprofile</code> only print the profiling step used by the kernel. The profiling step is the resolution of the profiling buffer, and is chosen during kernel configuration (through <code>make config</code>), or in the kernel&#8217;s command line. If the <code>-t</code> (terse) switch is used together with <code>-i</code> only the decimal number is printed.</dl>
<p> <code>-m</code>, <code>&#8211;mapfile</code> <i>mapfile</i></p>
<dl>
<dd>Specify a mapfile, which by default is <i>/usr/src/linux/System.map</i>. You should specify the map file on cmdline if your current kernel isn&#8217;t the last one you compiled, or if you keep System.map elsewhere. If the name of the map file ends with <i>.gz</i> it is decompressed on the fly.</dl>
<p> <code>-M</code>, <code>&#8211;multiplier</code> <i>multiplier</i></p>
<dl>
<dd>On some architectures it is possible to alter the frequency at which the kernel delivers profiling interrupts to each CPU. This option allows you to set the frequency, as a multiplier of the system clock frequency, HZ. Linux 2.6.16 dropped multiplier support for most systems. This option also resets the profiling buffer, and requires superuser privileges.</dl>
<p> <code>-p</code>, <code>&#8211;profile</code> <i>pro-file</i></p>
<dl>
<dd>Specify a different profiling buffer, which by default is <i>/proc/profile</i>. Using a different pro-file is useful if you want to `freeze&#8217; the kernel profiling at some time and read it later. The <i>/proc/profile</i> file can be copied using <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1) or <code><a href="/docs/linux/man/1-cp/">cp</a></code>(1). There is no more support for compressed profile buffers, like in <code>readprofile-1.1</code>, because the program needs to know the size of the buffer in advance.</dl>
<p> <code>-r</code>, <code>&#8211;reset</code></p>
<dl>
<dd>Reset the profiling buffer. This can only be invoked by root, because <i>/proc/profile</i> is readable by everybody but writable only by the superuser. However, you can make <code>readprofile</code> set-user-ID 0, in order to reset the buffer without gaining privileges.</dl>
<p> <code>-s, &#8211;counters</code></p>
<dl>
<dd>Print individual counters within functions.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dd>Verbose. The output is organized in four columns and filled with blanks. The first column is the RAM address of a kernel function, the second is the name of the function, the third is the number of clock ticks and the last is the normalized load.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<h2>Files</h2>
<p><i>/proc/profile</i></p>
<dl>
<dd>A binary snapshot of the profiling buffer.</dl>
<p> <i>/usr/src/linux/System.map</i></p>
<dl>
<dd>The symbol table for the kernel.</dl>
<p> <i>/usr/src/linux/*</i></p>
<dl>
<dd>The program being profiled :-)</dl>
<h2>Bugs</h2>
<p><code>readprofile</code> only works with a 1.3.x or newer kernel, because <i>/proc/profile</i> changed in the step from 1.2 to 1.3. </p>
<p> This program only works with ELF kernels. The change for a.out kernels is trivial, and left as an exercise to the a.out user. </p>
<p> To enable profiling, the kernel must be rebooted, because no profiling module is available, and it wouldn&#8217;t be easy to build. To enable profiling, you can specify <code>profile</code>=<i>2</i> (or another number) on the kernel commandline. The number you specify is the two-exponent used as profiling step. </p>
<p> Profiling is disabled when interrupts are inhibited. This means that many profiling ticks happen when interrupts are re-enabled. Watch out for misleading information.</p>
<h2>Example</h2>
<p>Browse the profiling buffer ordering by clock ticks: </p>
<dl>
<dd>
<pre> readprofile | sort -nr | less</pre>
</dl>
<p> Print the 20 most loaded procedures: </p>
<dl>
<dd>
<pre> readprofile | sort -nr +2 | head -20</pre>
</dl>
<p> Print only filesystem profile: </p>
<dl>
<dd>
<pre> readprofile | grep _ext2</pre>
</dl>
<p> Look at all the kernel information, with ram addresses: </p>
<dl>
<dd>
<pre> readprofile -av | less</pre>
</dl>
<p> Browse a &#8216;frozen&#8217; profile buffer for a non current kernel: </p>
<dl>
<dd>
<pre> readprofile -p ~/profile.freeze -m /zImage.map.gz</pre>
</dl>
<p> Request profiling at 2kHz per CPU, and reset the profiling buffer: </p>
<dl>
<dd>
<pre> sudo readprofile -M 20</pre>
</dl>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>readprofile</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
