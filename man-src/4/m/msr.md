---
title: "msr(4)"
name: "msr"
section: "4"
letter: "m"
url: "/docs/linux/man/4-msr/"
---

msr - x86 CPU MSR access device

<h2>Description</h2>

<i>/dev/cpu/CPUNUM/msr</i> provides an interface to read and write the model-specific registers (MSRs) of an x86 CPU. <i>CPUNUM</i> is the number of the CPU to access as listed in <i>/proc/cpuinfo</i>. 

 The register access is done by opening the file and seeking to the MSR number as offset in the file, and then reading or writing in chunks of 8 bytes. An I/O transfer of more than 8 bytes means multiple reads or writes of the same register. 

 This file is protected so that it can be read and written only by the user <i>root</i>, or members of the group <i>root</i>.

<h2>Notes</h2>

The <i>msr</i> driver is not auto-loaded. On modular kernels you might need to use the following command to load it explicitly before use: $ modprobe msr 

<h2>See Also</h2>

Intel Corporation Intel 64 and IA-32 Architectures Software Developer's Manual Volume 3B Appendix B, for an overview of the Intel CPU MSRs.

<h2>Colophon</h2>

This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" HREF="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> 
