---
title: "cpuid(4)"
name: "cpuid"
section: "4"
letter: "c"
url: "/docs/linux/man/4-cpuid/"
description: "cpuid – x86 CPUID access device"
---

<p>cpuid &#8211; x86 CPUID access device</p>
<h2>Description</h2>
<p>CPUID provides an interface for querying information about the x86 CPU. </p>
<p> This device is accessed by <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2) or <code><a href="/docs/linux/man/2-pread/">pread</a></code>(2) to the appropriate CPUID level and reading in chunks of 16 bytes. A larger read size means multiple reads of consecutive levels. </p>
<p> The lower 32 bits of the file position is used as the incoming <i>%eax</i>, and the upper 32 bits of the file position as the incoming <i>%ecx</i>, the latter is intended for &quot;counting&quot; <i>eax</i> levels like <i>eax=4</i>. </p>
<p> This driver uses <i>/dev/cpu/CPUNUM/cpuid</i>, where <i>CPUNUM</i> is the minor number, and on an SMP box will direct the access to CPU <i>CPUNUM</i> as listed in <i>/proc/cpuinfo</i>. </p>
<p> This file is protected so that it can be read only by the user <i>root</i>, or members of the group <i>root</i>.</p>
<h2>Notes</h2>
<p>The CPUID instruction can be directly executed by a program using inline assembler. However this device allows convenient access to all CPUs without changing process affinity. </p>
<p> Most of the information in <i>cpuid</i> is reported by the kernel in cooked form either in <i>/proc/cpuinfo</i> or through subdirectories in <i>/sys/devices/system/cpu</i>. Direct CPUID access through this device should only be used in exceptional cases. </p>
<p> The <i>cpuid</i> driver is not auto-loaded. On modular kernels you might need to use the following command to load it explicitly before use: </p>
<p> $ modprobe cpuid </p>
<p> There is no support for CPUID functions that require additional input registers. </p>
<p> Very old x86 CPUs don&#8217;t support CPUID.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-cpuid/">cpuid</a></code>(1) </p>
<p> Intel Corporation, Intel 64 and IA-32 Architectures Software Developer&#8217;s Manual Volume 2A: Instruction Set Reference, A-M, 3-180 CPUID reference. </p>
<p> Intel Corporation, Intel Processor Identification and the CPUID Instruction, Application note 485.</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
