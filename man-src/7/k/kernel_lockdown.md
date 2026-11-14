---
title: "kernel_lockdown(7)"
name: "kernel_lockdown"
section: "7"
letter: "k"
url: "/docs/linux/man/7-kernel_lockdown/"
---

kernel_lockdown - kernel image access prevention feature

<h2>Description</h2>

The Kernel Lockdown feature is designed to prevent both direct and indirect access to a running kernel image, attempting to protect against unauthorized modification of the kernel image and to prevent access to security and cryptographic data located in kernel memory, whilst still permitting driver modules to be loaded. 

 If a prohibited or restricted feature is accessed or used, the kernel will emit a message that looks like: 

<dl><dd>&nbsp;Lockdown: X: Y is restricted, see man kernel_lockdown.7</dl>
 

 where X indicates the process name and Y indicates what is restricted. 

 On an EFI-enabled x86 or arm64 machine, lockdown will be automatically enabled if the system boots in EFI Secure Boot mode.

<h3>Coverage</h3>

When lockdown is in effect, a number of features are disabled or have their use restricted. This includes special device files and kernel services that allow direct access of the kernel image: 

<dl><dd>/dev/mem 
 /dev/kmem 
 /dev/kcore 
 /dev/ioports 
 BPF 
 kprobes</dl>
 

 and the ability to directly configure and control devices, so as to prevent the use of a device to access or modify a kernel image:
<dl><dt>&bull;
<dd>The use of module parameters that directly specify hardware parameters to drivers through the kernel command line or when loading a module.
<dt>&bull;
<dd>The use of direct PCI BAR access.
<dt>&bull;
<dd>The use of the ioperm and iopl instructions on x86.
<dt>&bull;
<dd>The use of the KD*IO console ioctls.
<dt>&bull;
<dd>The use of the TIOCSSERIAL serial ioctl.
<dt>&bull;
<dd>The alteration of MSR registers on x86.
<dt>&bull;
<dd>The replacement of the PCMCIA CIS.
<dt>&bull;
<dd>The overriding of ACPI tables.
<dt>&bull;
<dd>The use of ACPI error injection.
<dt>&bull;
<dd>The specification of the ACPI RDSP address.
<dt>&bull;
<dd>The use of ACPI custom methods.</dl>
 

 Certain facilities are restricted:
<dl><dt>&bull;
<dd>Only validly signed modules may be loaded (waived if the module file being loaded is vouched for by IMA appraisal).
<dt>&bull;
<dd>Only validly signed binaries may be kexec'd (waived if the binary image file to be executed is vouched for by IMA appraisal).
<dt>&bull;
<dd>Unencrypted hibernation/suspend to swap are disallowed as the kernel image is saved to a medium that can then be accessed.
<dt>&bull;
<dd>Use of debugfs is not permitted as this allows a whole range of actions including direct configuration of, access to and driving of hardware.
<dt>&bull;
<dd>IMA requires the addition of the &quot;secure_boot&quot; rules to the policy, whether or not they are specified on the command line, for both the built-in and custom policies in secure boot lockdown mode.</dl>

<h2>Versions</h2>

The Kernel Lockdown feature was added in Linux 5.4.

<h2>Notes</h2>

The Kernel Lockdown feature is enabled by CONFIG_SECURITY_LOCKDOWN_LSM. The <i>lsm=lsm1,...,lsmN</i> command line parameter controls the sequence of the initialization of Linux Security Modules. It must contain the string <i>lockdown</i> to enable the Kernel Lockdown feature. If the command line parameter is not specified, the initialization falls back to the value of the deprecated <i>security=</i> command line parameter and further to the value of CONFIG_LSM.

<h2>Colophon</h2>

This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" HREF="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> 
