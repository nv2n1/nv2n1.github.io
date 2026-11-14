---
title: "readprofile(1)"
name: "readprofile"
section: "1"
letter: "r"
url: "/docs/linux/man/1-readprofile/"
description: "readprofile – read kernel profiling information"
---

<h2 class="name">NAME</h2>
<p> readprofile &#8211; read kernel profiling information </p>
<h2>SYNOPSIS</h2>
<p> <code>readprofile</code> [<i>options</i>] </p>
<h2>VERSION</h2>
<p> This manpage documents version 2.0 of the program. </p>
<h2>DESCRIPTION</h2>
<p> The <code>readprofile</code> command uses the <code>/proc/profile</code> information to print ascii data on standard output. The output is organized in three columns: the first is the number of clock ticks, the second is the name of the C function in the kernel where those many ticks occurred, and the third is the normalized `load&#8217; of the procedure, calculated as a ratio between the number of ticks and the length of the procedure. The output is filled with blanks to ease readability. </p>
<p> Available command line options are the following: </p>
<dl>
<dt><code>-m</code><i> mapfile</i></p>
<dd> Specify a mapfile, which by default is <code>/usr/src/linux/System.map.</code> You should specify the map file on cmdline if your current kernel isn&#8217;t the last one you compiled, or if you keep System.map elsewhere. If the name of the map file ends with `.gz&#8217; it is decompressed on the fly. </p>
<dt><code>-p</code><i> pro-file</i></p>
<dd> Specify a different profiling buffer, which by default is <code>/proc/profile.</code> Using a different pro-file is useful if you want to `freeze&#8217; the kernel profiling at some time and read it later. The <code>/proc/profile</code> file can be copied using `cat&#8217; or `cp&#8217;. There is no more support for compressed profile buffers, like in <code>readprofile-1.1,</code> because the program needs to know the size of the buffer in advance. </p>
<dt><code>-i</code></p>
<dd> Info. This makes <code>readprofile</code> only print the profiling step used by the kernel. The profiling step is the resolution of the profiling buffer, and is chosen during kernel configuration (through `make config&#8217;), or in the kernel&#8217;s command line. If the <code>-t</code> (terse) switch is used together with <code>-i</code> only the decimal number is printed. </p>
<dt><code>-a</code></p>
<dd> Print all symbols in the mapfile. By default the procedures with 0 reported ticks are not printed. </p>
<dt><code>-b</code></p>
<dd> Print individual histogram-bin counts. </p>
<dt><code>-r</code></p>
<dd> Reset the profiling buffer. This can only be invoked by root, because <code>/proc/profile</code> is readable by everybody but writable only by the superuser. However, you can make <code>readprofile</code> setuid 0, in order to reset the buffer without gaining privileges. </p>
<dt><code>-M</code><i> multiplier</i></p>
<dd> On some architectures it is possible to alter the frequency at which the kernel delivers profiling interrupts to each CPU. This option allows you to set the frequency, as a multiplier of the system clock frequency, HZ. This is supported on i386-SMP (2.2 and 2.4 kernel) and also on sparc-SMP and sparc64-SMP (2.4 kernel). This option also resets the profiling buffer, and requires superuser privileges. </p>
<dt><code>-v</code></p>
<dd> Verbose. The output is organized in four columns and filled with blanks. The first column is the RAM address of a kernel function, the second is the name of the function, the third is the number of clock ticks and the last is the normalized load. </p>
<dt><code>-V</code></p>
<dd> Version. This makes <code>readprofile</code> print its version number and exit. </p>
</dl>
<h2>EXAMPLES</h2>
<p> Browse the profiling buffer ordering by clock ticks: </p>
<pre>
   readprofile | sort -nr | less
</pre>
<p> Print the 20 most loaded procedures: </p>
<pre>
   readprofile | sort -nr +2 | head -20
</pre>
<p> Print only filesystem profile: </p>
<pre>
   readprofile | grep _ext2
</pre>
<p> Look at all the kernel information, with ram addresses&quot; </p>
<pre>
   readprofile -av | less
</pre>
<p> Browse a `freezed&#8217; profile buffer for a non current kernel: </p>
<pre>
   readprofile -p ~/profile.freeze -m /zImage.map.gz
</pre>
<p> Request profiling at 2kHz per CPU, and reset the profiling buffer </p>
<pre>
   sudo readprofile -M 20
</pre>
<h2>BUGS</h2>
<p> <code>readprofile</code> only works with an 1.3.x or newer kernel, because <code>/proc/profile</code> changed in the step from 1.2 to 1.3 </p>
<p> This program only works with ELF kernels. The change for a.out kernels is trivial, and left as an exercise to the a.out user. </p>
<p> To enable profiling, the kernel must be rebooted, because no profiling module is available, and it wouldn&#8217;t be easy to build. To enable profiling, you can specify &quot;profile=2&quot; (or another number) on the kernel commandline. The number you specify is the two-exponent used as profiling step. </p>
<p> Profiling is disabled when interrupts are inhibited. This means that many profiling ticks happen when interrupts are re-enabled. Watch out for misleading information. </p>
<h2>FILES</h2>
<pre>
/proc/profile              A binary snapshot of the profiling buffer.
/usr/src/linux/System.map  The symbol table for the kernel.
/usr/src/linux/*           The program being profiled :-)
</pre>
<h2>AVAILABILITY</h2>
<p> The readprofile command is part of the util-linux package and is available from <a href="ftp://ftp.kernel.org/pub/linux/utils/util-linux/.">ftp://ftp.kernel.org/pub/linux/utils/util-linux/.</a> </p>
<h2>Index</h2>
