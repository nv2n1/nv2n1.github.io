---
title: "kexec(8)"
name: "kexec"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kexec/"
description: "kexec – directly boot into a new kernel"
---

<p>kexec &#8211; directly boot into a new kernel</p>
<h2>Synopsis</h2>
<p><code>/sbin/kexec</code> <code>[-v (&#8211;version)] [-f (&#8211;force)] [-x (&#8211;no-ifdown)] [-y (&#8211;no-sync)] [-l (&#8211;load)] [-p (&#8211;load-panic)] [-u (&#8211;unload)] [-e (&#8211;exec)] [-t (&#8211;type)]</code> <code>[&#8211;mem-min=</code><i>addr</i><code>]</code> <code>[&#8211;mem-max=</code><i>addr</i><code>]</code> </p>
<h2>Description</h2>
<p><code>kexec</code> is a system call that enables you to load and boot into another kernel from the currently running kernel. <code>kexec</code> performs the function of the boot loader from within the kernel. The primary difference between a standard system boot and a <code>kexec</code> boot is that the hardware initialization normally performed by the BIOS or firmware (depending on architecture) is not performed during a <code>kexec</code> boot. This has the effect of reducing the time required for a reboot. </p>
<p> Make sure you have selected <code>CONFIG_KEXEC=y</code> when configuring the kernel. The <code>CONFIG_KEXEC</code> option enables the <code>kexec</code> system call.</p>
<h2>Usage</h2>
<p>Using <code>kexec</code> consists of </p>
<dl>
<dd>(1) loading the kernel to be rebooted to into memory, and</dl>
<dl>
<dd>(2) actually rebooting to the pre-loaded kernel.</dl>
<p> To load a kernel, the syntax is as follows: </p>
<dl>
<dd><code>kexec</code> -l&nbsp;<wbr><i>kernel-image</i> &#8211;append=<i>command-line-options</i> &#8211;initrd=<i>initrd-image</i></dl>
<p> where <i>kernel-image</i> is the kernel file that you intend to reboot to. </p>
<p> Insert the command-line parameters that must be passed to the new kernel into <i>command-line-options</i>. Passing the exact contents of /proc/cmdline into <i>command-line-options</i> is the safest way to ensure that correct values are passed to the rebooting kernel. </p>
<p> The optional <i>initrd-image</i> is the initrd image to be used during boot. </p>
<p> It&#8217;s also possible to invoke <code>kexec</code> without an option parameter. In that case, kexec loads the specified kernel and then invokes <code><a href="/docs/linux/man/8-shutdown/">shutdown</a></code>(8). If the shutdown scripts of your Linux distribution support kexec-based rebooting, they then call <code>kexec</code> <i>-e</i> just before actually rebooting the machine. That way, the machine does a clean shutdown including all shutdown scripts.</p>
<h2>Example</h2>
<p>For example, if the kernel image you want to reboot to is <code>/boot/vmlinux</code>, the contents of /proc/cmdline is <code>root=/dev/hda1</code>, and the path to the initrd is <code>/boot/initrd</code>, then you would use the following command to load the kernel:</p>
<dl>
<dd><code>kexec</code> -l&nbsp;<wbr><code>/boot/vmlinux</code> &#8211;append=<code>root=/dev/hda1</code>&nbsp;<wbr>&#8211;initrd=<code>/boot/initrd</code></dl>
<p> After this kernel is loaded, it can be booted to at any time using the command:</p>
<dl>
<dd><code>kexec</code>&nbsp;<wbr>-e</dl>
<h2>Options</h2>
<dl>
<dt><code>-d&nbsp;<wbr>(&#8211;debug)</code></p>
<dd>Enable debugging messages.</p>
<dt><code>-e&nbsp;<wbr>(&#8211;exec)</code></p>
<dd>Run the currently loaded kernel. Note that it will reboot into the loaded kernel without calling <a href="/docs/linux/man/8-shutdown/">shutdown</a>(8).</p>
<dt><code>-f&nbsp;<wbr>(&#8211;force)</code></p>
<dd>Force an immediate <code>kexec</code> call, do not call <code><a href="/docs/linux/man/8-shutdown/">shutdown</a></code>(8) (contrary to the default action without any option parameter). This option performs the same actions like executing <i>-l</i> and <i>-e</i> in one call.</p>
<dt><code>-h&nbsp;<wbr>(&#8211;help)</code></p>
<dd>Open a help file for <code>kexec</code>.</p>
<dt><code>-l&nbsp;<wbr>(&#8211;load)</code><i>&nbsp;<wbr>kernel</i></p>
<dd>Load the specified <i>kernel</i> into the current kernel.</p>
<dt><code>-p&nbsp;<wbr>(&#8211;load-panic)</code></p>
<dd>Load the new kernel for use on panic.</p>
<dt><code>-t&nbsp;<wbr>(&#8211;type=</code><i>type</i><code>)</code></p>
<dd>Specify that the new kernel is of this <i>type.</i></p>
<dt><code>-u&nbsp;<wbr>(&#8211;unload)</code></p>
<dd>Unload the current <code>kexec</code> target kernel. If a capture kernel is being unloaded then specify -p with -u.</p>
<dt><code>-v&nbsp;<wbr>(&#8211;version)</code></p>
<dd>Return the version number of the installed utility.</p>
<dt><code>-x&nbsp;<wbr>(&#8211;no-ifdown)</code></p>
<dd>Shut down the running kernel, but restore the interface on reload.</p>
<dt><code>-y&nbsp;<wbr>(&#8211;no-sync)</code></p>
<dd>Shut down the running kernel, but skip syncing the filesystems.</p>
<dt><code>&#8211;mem-min=</code><i>addr</i></p>
<dd>Specify the lowest memory address <i>addr</i> to load code into.</p>
<dt><code>&#8211;mem-max=</code><i>addr</i></p>
<dd>Specify the highest memory address <i>addr</i> to load code into.</p>
<dt><code>&#8211;entry=</code><i>addr</i></p>
<dd>Specify the jump back address. (0 means it&#8217;s not jump back or preserve context)</p>
<dt><code>&#8211;load-preserve-context</code></p>
<dd>Load the new kernel and preserve context of current kernel during kexec.</p>
<dt><code>&#8211;load-jump-back-helper</code></p>
<dd>Load a helper image to jump back to original kernel.</p>
<dt><code>&#8211;reuseinitrd</code></p>
<dd>Reuse initrd from first boot. </p>
</dl>
<h2>Supported Kernel File Types And Options</h2>
<p><code>Beoboot-x86</code></p>
<dl>
<dd>
<dl>
<dt><code>&#8211;args-elf</code></p>
<dd>Pass ELF boot notes.</p>
<dt><code>&#8211;args-linux</code></p>
<dd>Pass Linux kernel style options.</p>
<dt><code>&#8211;real-mode</code></p>
<dd>Use the kernel&#8217;s real mode entry point.</dl>
</dl>
<p> <code>elf-x86</code></p>
<dl>
<dd>
<dl>
<dt><code>&#8211;append=</code><i>string</i></p>
<dd>Append <i>string</i> to the kernel command line.</p>
<dt><code>&#8211;command-line=</code><i>string</i></p>
<dd>Set the kernel command line to <i>string</i>.</p>
<dt><code>&#8211;reuse-cmdline</code></p>
<dd>Use the command line from the running system. When a panic kernel is loaded, it strips the <i>crashkernel</i> parameter automatically. The <i>BOOT_IMAGE</i> parameter is also stripped.</p>
<dt><code>&#8211;initrd=</code><i>file</i></p>
<dd>Use <i>file</i> as the kernel&#8217;s initial ramdisk.</p>
<dt><code>&#8211;ramdisk=</code><i>file</i></p>
<dd>Use <i>file</i> as the kernel&#8217;s initial ramdisk.</dl>
</dl>
<p> <code>bzImage-x86</code></p>
<dl>
<dd>
<dl>
<dt><code>&#8211;append=</code><i>string</i></p>
<dd>Append <i>string</i> to the kernel command line.</p>
<dt><code>&#8211;command-line=</code><i>string</i></p>
<dd>Set the kernel command line to <i>string</i>.</p>
<dt><code>&#8211;reuse-cmdline</code></p>
<dd>Use the command line from the running system. When a panic kernel is loaded, it strips the <i>crashkernel</i> parameter automatically. The <i>BOOT_IMAGE</i> parameter is also stripped.</p>
<dt><code>&#8211;initrd=</code><i>file</i></p>
<dd>Use <i>file</i> as the kernel&#8217;s initial ramdisk.</p>
<dt><code>&#8211;ramdisk=</code><i>file</i></p>
<dd>Use <i>file</i> as the kernel&#8217;s initial ramdisk.</p>
<dt><code>&#8211;real-mode</code></p>
<dd>Use real-mode entry point.</dl>
</dl>
<p> <code>multiboot-x86</code></p>
<dl>
<dd>
<dl>
<dt><code>&#8211;command-line=</code><i>string</i></p>
<dd>Set the kernel command line to <i>string</i>.</p>
<dt><code>&#8211;reuse-cmdline</code></p>
<dd>Use the command line from the running system. When a panic kernel is loaded, it strips the <i>crashkernel</i> parameter automatically. The <i>BOOT_IMAGE</i> parameter is also stripped.</p>
<dt><code>&#8211;module=</code><i>mod arg1 arg2 &#8230;</i></p>
<dd>Load module <i>mod</i> with command-line arguments <i>arg1 arg2 &#8230;</i> This parameter can be specified multiple times.</dl>
</dl>
<h2>Architecture Options</h2>
<dl>
<dt><code>&#8211;console-serial</code></p>
<dd>Enable the serial console.</p>
<dt><code>&#8211;console-vga</code></p>
<dd>Enable the VGA console.</p>
<dt><code>&#8211;elf32-core-headers</code></p>
<dd>Prepare core headers in ELF32 format.</p>
<dt><code>&#8211;elf64-core-headers</code></p>
<dd>Prepare core headers in ELF64 format.</p>
<dt><code>&#8211;reset-vga</code></p>
<dd>Attempt to reset a standard VGA device.</p>
<dt><code>&#8211;serial=</code><i>port</i></p>
<dd>Specify the serial <i>port</i> for debug output.</p>
<dt><code>&#8211;serial-baud=</code><i>baud_rate</i></p>
<dd>Specify the <i>baud rate</i> of the serial port. </p>
</dl>
