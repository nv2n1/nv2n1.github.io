---
title: "grubby(8)"
name: "grubby"
section: "8"
letter: "g"
url: "/docs/linux/man/8-grubby/"
description: "grubby – command line tool used to configure bootloader menu entries across multiple architectures"
---

<p>grubby &#8211; command line tool used to configure bootloader menu entries across multiple architectures</p>
<h2>Synopsis</h2>
<p><code>grubby</code> [<i>OPTIONS</i>] </p>
<h2>Description</h2>
<h3>General Information</h3>
<p><code>grubby</code> is a command line tool for updating and displaying information about the configuration files for various architecture specific bootloaders. It is primarily designed to be used from scripts which install new kernels and need to find information about the current boot environment.</p>
<h3>Architecture Support</h3>
<p>The <code>grubby</code> executable has full support for the <code>grub2</code> bootloader on <code>x86_64</code> systems using legacy BIOS or modern UEFI firmware and <code>ppc64</code> and <code>ppc64le</code> hardware using OPAL or SLOF as firmware. Legacy <code>s390</code> and the current <code>s390x</code> architectures and their <code>zipl</code> bootloader are fully supported. Support for <code>yaboot</code> has been deprecated as all ppc architecture hardware since the Power8 uses <code>grub2</code> or petitboot which both use the grub2 configuration file format. Legacy bootloaders <code>LILO</code>, <code>SILO</code>, and <code>ELILO</code> are deprecated and no longer receiving active support in favor of previously mentioned bootloaders.</p>
<h3>Default Behavior</h3>
<p>The default bootloader target is primarily determined by the architecture for which grubby has been built. Each architecture has a preferred bootloader, and each bootloader has its own configuration file. If no bootloader is selected on the command line, grubby will use these default settings to search for an existing configuration. If no bootloader configuration file is found, grubby will use the default value for that architecture. These defaults are listed in the table below. </p>
<table BORDER>
<tr VALIGN=top>
<td><code><br />
&nbsp;<wbr>Arch</code></td>
<td><code>Bootloader</code></td>
<td><code>Configuration File</code>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>x86_64&nbsp;<wbr>[BIOS]</td>
<td>grub2</td>
<td>/boot/grub2/grub.cfg
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>x86_64&nbsp;<wbr>[UEFI]</td>
<td>grub2</td>
<td>/boot/efi/EFI/redhat/grub.cfg
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>i386</td>
<td>grub2</td>
<td>/boot/grub2/grub.cfg
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>ia64</td>
<td>elilo</td>
<td>/boot/efi/EFI/redhat/elilo.conf
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>ppc&nbsp;<wbr>[&gt;=Power8]</td>
<td>grub2</td>
<td>/boot/grub2/grub.cfg
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>ppc&nbsp;<wbr>[&lt;=Power7]</td>
<td>yaboot</td>
<td>/etc/yaboot.conf
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>s390</td>
<td>zipl</td>
<td>/etc/zipl.conf
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>s390x</td>
<td>zipl</td>
<td>/etc/zipl.conf
</td>
</tr>
</table>
<h3>Special Arguments</h3>
<p>There are a number of ways to specify the kernel used for <code>&#8211;info</code>, <code>&#8211;remove-kernel</code>, and <code>&#8211;update-kernel</code>. Specifying <code>DEFAULT</code> or <code>ALL</code> selects the default entry and all of the entries, respectively. If a comma separated list of numbers is given, the boot entries indexed by those numbers are selected. Finally, the title of a boot entry may be specified by using <code>TITLE=</code><i>title</i> as the argument; all entries with that title are used. </p>
<h2>Options</h2>
<h3>Basic Options</h3>
<dl>
<dt><code>&#8211;add-kernel</code>=<i>kernel-path</i></p>
<dd>Add a new boot entry for the kernel located at <i>kernel-path</i>. A title for the boot entry must be set using <code>&#8211;title</code>. Most invocations should also include <code>&#8211;initrd</code> with memtest86 as a notable exception. </p>
<p> The <code>&#8211;update-kernel</code> option may not be used in the same invocation. </p>
<dt><code>&#8211;remove-kernel</code>=<i>kernel-path</i></p>
<dd>Remove all boot entries which match <i>kernel-path</i>. This may be used along with <code>&#8211;add-kernel</code>, in which case the new entry being added will not be removed. </p>
<dt><code>&#8211;update-kernel</code>=<i>kernel-path</i></p>
<dd>Update the entries for kernels matching kernel-path. Currently the only item that can be updated is the kernel argument list, which is modified via the <code>&#8211;args</code> and <code>&#8211;remove-args</code> options. </p>
<dt><code>&#8211;args</code>=<i>kernel-args</i></p>
<dd>When a new kernel is added, this specifies the command line arguments which should be passed to the kernel by default (note they are merged with the arguments from the template if <code>&#8211;copy-default</code> is used). When <code>&#8211;update-kernel</code> is used, this specifies new arguments to add to the argument list. Multiple, space separated arguments may be used. If an argument already exists the new value replaces the old values. The <code>root=</code> kernel argument gets special handling if the configuration file has special handling for specifying the root filesystem (like lilo.conf does). </p>
<dt><code>&#8211;remove-args</code>=<i>kernel-args</i></p>
<dd>The arguments specified by <i>kernel-args</i> are removed from the kernels specified by <code>&#8211;update-kernel</code>. The <code>root</code> argument gets special handling for configuration files that support separate root filesystem configuration. </p>
<dt><code>&#8211;copy-default</code></p>
<dd><code>grubby</code> will copy as much information (such as kernel arguments and root device) as possible from the current default kernel. The kernel path and initrd path will never be copied. </p>
<dt><code>&#8211;title</code>=<i>entry-title</i></p>
<dd>When a new kernel entry is added <i>entry-title</i> is used as the title (<code>lilo</code> label) for the entry. If <i>entry-title</i> is longer then maximum length allowed by the bootloader (15 for lilo, unlimited for grub and elilo) the title is shortened to a (unique) entry. </p>
<dt><code>&#8211;initrd</code>=<i>initrd-path</i></p>
<dd>Use <i>initrd-path</i> as the path to an initial ram disk for a new kernel being added. </p>
<dt><code>&#8211;efi</code></p>
<dd>Use appropriate bootloader commands for EFI on this architecture. </p>
<dt><code>&#8211;set-default</code>=<i>kernel-path</i></p>
<dd>The first entry which boots the specified kernel is made the default boot entry. This may not be invoked with <code>&#8211;set-default-index</code>. </p>
<dt><code>&#8211;set-default-index</code>=<i>entry-index</i></p>
<dd>Makes the given entry number the default boot entry. This may not be invoked with <code>&#8211;set-default</code>. The given value represents the index in the post-modification boot entry list. </p>
<dt><code>&#8211;make-default</code></p>
<dd>Make the new kernel entry being added the default entry. </p>
<dt><code>&#8211;set-index</code>=<i>entry-index</i></p>
<dd>Set the position at which to add a new entry created with <code>&#8211;add-kernel</code>. </p>
<dt><code>&#8211;debug</code></p>
<dd>Display extra debugging information for failures. </p>
<dt><code>-i</code>, <code>&#8211;extra-initrd</code>=<i>initrd-path</i></p>
<dd>Use <i>initrd-path</i> as the path for an auxiliary initrd image. </p>
</dl>
<h3>Display Options</h3>
<p>Passing the display option to grubby will cause it to print out the requested information about the current bootloader configuration and then immediately exit. These options should not be used in any script intended to update the bootloader configuration. </p>
<dl>
<dt><code>&#8211;default-kernel</code></p>
<dd>Display the full path to the current default kernel and exit. </p>
<dt><code>&#8211;default-index</code></p>
<dd>Display the numeric index of the current default boot entry and exit. </p>
<dt><code>&#8211;default-title</code></p>
<dd>Display the title of the current default boot entry and exit. </p>
<dt><code>&#8211;info</code>=<i>kernel-path</i></p>
<dd>Display information on all boot entries which match <i>kernel-path</i>. I </p>
<dt><code>&#8211;bootloader-probe</code></p>
<dd>Attempt to probe for installed bootloaders. If this option is specified, <code>grubby</code> tries to determine if <code>grub</code> or <code>lilo</code> is currently installed. When one of those bootloaders is found the name of that bootloader is displayed on stdout. Both could be installed (on different devices), and grubby will print out the names of both bootloaders, one per line. The probe for <code>grub</code> requires a commented out boot directive <code>grub.conf</code> identical to the standard directive in the lilo configuration file. If this is not present <code>grubby</code> will assume grub is not installed (note that <code>anaconda</code> places this directive in <code>grub.conf</code> files it creates). </p>
<p> <i>This option is only available on x86 BIOS platforms.</i> </p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>Display the version of <code>grubby</code> being run and then exit immediately. </p>
</dl>
<h3>Output Format Options</h3>
<p>Sane default options for the current platform are compiled into grubby on a per platform basis. These defaults determine the format and layout of the generated bootloader configuration file. A different configuration file format may be specified on the command line if the system uses a supported alternative bootloader. </p>
<dl>
<dt><code>&#8211;elilo</code></p>
<dd>Use an <code>elilo</code> style configuration file. This is the default on ia64 platforms. This format is deprecated. </p>
<dt><code>&#8211;extlinux</code></p>
<dd>Use an <code>extlinux</code> style configuration file. This format is deprecated. </p>
<dt><code>&#8211;grub</code></p>
<dd>Use a <code>grub</code> style configuration file. This is the default on the i386 architecture. </p>
<dt><code>&#8211;grub2</code></p>
<dd>Use a <code>grub2</code> style configuration file. This is the default on <code>x86_64</code> architecture as well as the <code>ppc64</code> and <code>ppc64le</code> architectures running on Power8 or later hardware. </p>
<dt><code>&#8211;lilo</code></p>
<dd>Use a <code>lilo</code> style configuration file. </p>
<dt><code>&#8211;silo</code></p>
<dd>Use a <code>silo</code> style configuration file. This is the default on SPARC systems. This format is legacy, deprecated, and unsupported. </p>
<dt><code>&#8211;yaboot</code></p>
<dd>Use a <code>yaboot</code> style configuration file. This is the default for the <code>ppc</code> architecture on on Power7 and earlier hardware. </p>
<dt><code>&#8211;zipl</code></p>
<dd>Use a <code>zipl</code> style configuration file. This is the default on the legacy s390 and current s390x architectures. </p>
</dl>
<h3>Override Options</h3>
<dl>
<dt><code>&#8211;bad-image-okay</code></p>
<dd>When <code>grubby</code> is looking for a entry to use for something (such as a template or a default boot entry) it uses sanity checks, such as ensuring that the kernel exists in the filesystem, to make sure entries that obviously won&#8217;t work aren&#8217;t selected. This option overrides that behavior, and is designed primarily for testing. </p>
<dt><code>&#8211;boot-filesystem</code>=<i>bootfs</i></p>
<dd>The <code>grub</code> boot loader expects file paths listed in its configuration path to be relative to the top of the filesystem they are on, rather then relative to the current root filesystem. By default <code>grubby</code> searches the list of currently mounted filesystems to determine this. If this option is given <code>grubby</code> acts as if the specified filesystem was the filesystem containing the kernel (this option is designed primarily for testing). </p>
<dt><code>&#8211;env</code>=<i>path</i></p>
<dd>Path for the file where grub environment data is stored. </p>
<dt><code>-c</code>, <code>&#8211;config-file</code>=<i>path</i></p>
<dd>Use <i>path</i> as the configuration file rather then the default. </p>
<dt><code>-o</code>, <code>&#8211;output-file</code>=<i>file_path</i></p>
<dd>The destination path for the updated configuration file. Use &quot;-&quot; to send it to stdout. </p>
</dl>
<h3>Multiboot Options</h3>
<p>The Multiboot Specification provides a generic interface for boot loaders and operating systems. It is supported by the GRUB bootloader. </p>
<dl>
<dt><code>&#8211;add-multiboot</code>=<i>multiboot-path</i></p>
<dd>Add a new boot entry for the multiboot kernel located at <i>multiboot-path</i>. Note that this is generally accompanied with a <code>&#8211;add-kernel</code> option. </p>
<dt><code>&#8211;remove-multiboot</code>=<i>multiboot-path</i></p>
<dd>Removes all boot entries which match <i>multiboot-path</i>. </p>
<dt><code>&#8211;mbargs</code>=<i>multiboot-args</i></p>
<dd>When a new multiboot kernel is added, this specifies the command line arguments which should be passed to that kernel by default When <code>&#8211;update-kernel</code> is used, this specifies new arguments to add to the argument list. Multiple, space separated arguments may be used. If an argument already exists the new value replaces the old values. </p>
<dt><code>&#8211;remove-mbargs</code>=<i>multiboot-args</i></p>
<dd>The arguments specified by <i>multiboot-args</i> are removed from the kernels specified by <code>&#8211;update-kernel</code>. </p>
</dl>
<h2>Bugs</h2>
<p>The command line syntax is more than a little baroque. This probably won&#8217;t be fixed as <code>grubby</code> is only intended to be called from shell scripts which can get it right. </p>
<h2>Example</h2>
<p>The following examples assume the following: </p>
<table BORDER>
<tr VALIGN=top>
<td ALIGN=right><code>cfg_file</code></td>
<td>Full path to bootloader config file
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>new_kernel</code></td>
<td>Full path to kernel image to be installed
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>old_kernel</code></td>
<td>Full path to old kernel image to be removed
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>current_kernel</code></td>
<td>Full path to a currently installed kernel
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>entry_title</code></td>
<td>Title that appears on bootloader menu
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>new_initrd</code></td>
<td>Full path to initrd for a new kernel
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>kernel_args</code></td>
<td>Set of arguments for the kernel
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>menu_index</code></td>
<td>Index number of a menu entry
</td>
</tr>
</table>
<p> The examples below quote strings that may have spaces or other whitespace in them. It is also perfectly valid to backslash escape these strings if that is more convenient. Add a new kernel entry and copy all options from the current default kernel. This is the behavior that most users will want.</p>
<dl>
<dd><code>grubby</code> &#8211;add-kernel=<i>new_kernel</i> &#8211;title=&quot;<i>entry_title</i>&quot; &#8211;initrd=&quot;<i>new_initrd</i>&quot; &#8211;copy-default</dl>
<p> Add a new kernel entry with custom arguments</p>
<dl>
<dd><code>grubby</code> &#8211;add-kernel=<i>new_kernel</i> &#8211;title=&quot;<i>entry_title</i>&quot; &#8211;initrd=&quot;<i>new_initrd</i>&quot; &#8211;args=<i>kernel_args</i></dl>
<p> Remove <code>all menu entries</code> for a specified kernel.</p>
<dl>
<dd><code>grubby</code> &#8211;remove-kernel=<i>old_kernel</i></dl>
<p> Target a single menu entry to remove without targetting other entries with the same kernel.</p>
<dl>
<dd><code>grubby</code> &#8211;info=<i>old_kernel</i> <code>grubby</code> &#8211;remove-kernel=<i>menu_index</i></dl>
<pre><code>Update the arguments for all entries of a specific kernel. New arguments get
added while existing arguments get updated values.


grubby --update-kernel=current_kernel --args=&quot;kernel_args&quot;</code></pre>
<p> Remove the arguments for a single entry of a specific kernel.</p>
<dl>
<dd><code>grubby</code> &#8211;info=<i>current_kernel</i> </p>
<pre><code>grubby --remove-args=menu_index --args=&quot;kernel_args&quot;
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-grub/">grub</a></code>(8), <code><a href="/docs/linux/man/8-lilo/">lilo</a></code>(8), <code><a href="/docs/linux/man/8-yaboot/">yaboot</a></code>(8), <code><a href="/docs/linux/man/8-zipl/">zipl</a></code>(8), <code><a href="/docs/linux/man/8-dracut/">dracut</a></code>(8), <code><a href="/docs/linux/man/8-mkinitrd/">mkinitrd</a></code>(8) </p>
<h2>Authors</h2>
<pre>Erik Troan
Jeremy Katz
Peter Jones
Robert Marshall</pre>
