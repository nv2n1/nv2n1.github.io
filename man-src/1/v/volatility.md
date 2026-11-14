---
title: "volatility(1)"
name: "volatility"
section: "1"
letter: "v"
url: "/docs/linux/man/1-volatility/"
description: "volatility – advanced memory forensics framework"
---

<h2 class="name">NAME</h2>
<p> <code>volatility </code>&#8211; advanced memory forensics framework </p>
<h2>SYNOPSIS</h2>
<pre><code>
vol[option] vol - f[image]-- profile = [profile][plugin]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The Volatility Framework is a completely open collection of tools for the extraction of digital artifacts from volatile memory (RAM) samples. It is useful in forensics analysis. The extraction techniques are performed completely independent of the system being investigated but offer unprecedented visibility into the runtime state of the system. </p>
<p> Volatility supports several versions of the MS Windows, Linux and MAC OSX: </p>
<p> MS Windows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> 32-bit Windows XP Service Pack 2 and 3</p>
<dt>&bull;</p>
<dd> 32-bit Windows 2003 Server Service Pack 0, 1, 2</p>
<dt>&bull;</p>
<dd> 32-bit Windows Vista Service Pack 0, 1, 2</p>
<dt>&bull;</p>
<dd> 32-bit Windows 2008 Server Service Pack 1, 2 (there is no SP0)</p>
<dt>&bull;</p>
<dd> 32-bit Windows 7 Service Pack 0, 1</p>
<dt>&bull;</p>
<dd> 32-bit Windows 8, 8.1, and 8.1 Update 1</p>
<dt>&bull;</p>
<dd> 32-bit Windows 10 (initial support)</p>
<dt>&bull;</p>
<dd> 64-bit Windows XP Service Pack 1 and 2 (there is no SP0)</p>
<dt>&bull;</p>
<dd> 64-bit Windows 2003 Server Service Pack 1 and 2 (there is no SP0)</p>
<dt>&bull;</p>
<dd> 64-bit Windows Vista Service Pack 0, 1, 2</p>
<dt>&bull;</p>
<dd> 64-bit Windows 2008 Server Service Pack 1 and 2 (there is no SP0)</p>
<dt>&bull;</p>
<dd> 64-bit Windows 2008 R2 Server Service Pack 0 and 1</p>
<dt>&bull;</p>
<dd> 64-bit Windows 7 Service Pack 0 and 1</p>
<dt>&bull;</p>
<dd> 64-bit Windows 8, 8.1, and 8.1 Update 1</p>
<dt>&bull;</p>
<dd> 64-bit Windows Server 2012 and 2012 R2</p>
<dt>&bull;</p>
<dd> 64-bit Windows 10 (initial support)</dl>
</dl>
<p> Linux:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> 32-bit Linux kernels 2.6.11 to 4.2.3</p>
<dt>&bull;</p>
<dd> 64-bit Linux kernels 2.6.11 to 4.2.3</p>
<dt>&bull;</p>
<dd> OpenSuSE, Ubuntu, Debian, CentOS, Fedora, Mandriva, etc</dl>
</dl>
<p> Mac OSX:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> 32-bit 10.5.x Leopard (the only 64-bit 10.5 is Server, which isn&#8217;t supported)</p>
<dt>&bull;</p>
<dd> 32-bit 10.6.x Snow Leopard</p>
<dt>&bull;</p>
<dd> 64-bit 10.6.x Snow Leopard</p>
<dt>&bull;</p>
<dd> 32-bit 10.7.x Lion</p>
<dt>&bull;</p>
<dd> 64-bit 10.7.x Lion</p>
<dt>&bull;</p>
<dd> 64-bit 10.8.x Mountain Lion (there is no 32-bit version)</p>
<dt>&bull;</p>
<dd> 64-bit 10.9.x Mavericks (there is no 32-bit version)</p>
<dt>&bull;</p>
<dd> 64-bit 10.10.x Yosemite (there is no 32-bit version)</p>
<dt>&bull;</p>
<dd> 64-bit 10.11.x El Capitan (there is no 32-bit version)</dl>
</dl>
<p> The memory formats supported are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Raw linear sample (dd)</p>
<dt>&bull;</p>
<dd> Hibernation file</p>
<dt>&bull;</p>
<dd> Crash dump file</p>
<dt>&bull;</p>
<dd> VirtualBox ELF64 core dump</p>
<dt>&bull;</p>
<dd> VMware saved state and snapshot files</p>
<dt>&bull;</p>
<dd> EWF format (E01)</p>
<dt>&bull;</p>
<dd> LiME (Linux Memory Extractor) format</p>
<dt>&bull;</p>
<dd> Mach-o file format</p>
<dt>&bull;</p>
<dd> QEMU virtual machine dumps</p>
<dt>&bull;</p>
<dd> Firewire</p>
<dt>&bull;</p>
<dd> HPAK (FDPro)</dl>
</dl>
<p> The supported address spaces (RAM types) are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> AMD64PagedMemory &#8211; Standard AMD 64-bit address space</p>
<dt>&bull;</p>
<dd> ArmAddressSpace &#8211; Address space for ARM processors</p>
<dt>&bull;</p>
<dd> FileAddressSpace &#8211; This is a direct file AS</p>
<dt>&bull;</p>
<dd> HPAKAddressSpace &#8211; This AS supports the HPAK format</p>
<dt>&bull;</p>
<dd> IA32PagedMemoryPae &#8211; This class implements the IA-32 PAE paging address space. It is responsible</p>
<dt>&bull;</p>
<dd> IA32PagedMemory &#8211; Standard IA-32 paging address space</p>
<dt>&bull;</p>
<dd> LimeAddressSpace &#8211; Address space for Lime</p>
<dt>&bull;</p>
<dd> MachOAddressSpace &#8211; Address space for mach-o files to support atc-ny memory reader</p>
<dt>&bull;</p>
<dd> OSXPmemELF &#8211; This AS supports VirtualBox ELF64 coredump format</p>
<dt>&bull;</p>
<dd> QemuCoreDumpElf &#8211; This AS supports Qemu ELF32 and ELF64 coredump format</p>
<dt>&bull;</p>
<dd> VirtualBoxCoreDumpElf64 &#8211; This AS supports VirtualBox ELF64 coredump format</p>
<dt>&bull;</p>
<dd> VMWareAddressSpace &#8211; This AS supports VMware snapshot (VMSS) and saved state (VMSS) files</p>
<dt>&bull;</p>
<dd> VMWareMetaAddressSpace &#8211; This AS supports the VMEM format with VMSN/VMSS metadata</p>
<dt>&bull;</p>
<dd> WindowsCrashDumpSpace32 &#8211; This AS supports windows Crash Dump format</p>
<dt>&bull;</p>
<dd> WindowsCrashDumpSpace64BitMap &#8211; This AS supports Windows BitMap Crash Dump format</p>
<dt>&bull;</p>
<dd> WindowsCrashDumpSpace64 &#8211; This AS supports windows Crash Dump format</p>
<dt>&bull;</p>
<dd> WindowsHiberFileSpace32 &#8211; This is a hibernate address space for windows hibernation files</dl>
</dl>
<p> There are exemplar memory images for tests at <a rel="nofollow" href="https://github.com/volatilityfoundation/volatility/wiki/Memory-Samples.">https://github.com/volatilityfoundation/volatility/wiki/Memory-Samples.</a></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> List all available options and their default values. Default values may be set in the configuration file (/etc/volatilityrc).</p>
<dt><code>&#8211;conf-file</code>=/root/.volatilityrc</p>
<dd> User based configuration file.</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Debug Volatility.</p>
<dt><code>&#8211;plugins</code>=PLUGINS</p>
<dd> Additional <i>plugin</i> directories to use (colon separated).</p>
<dt><code>&#8211;info</code></p>
<dd> Print information about all registered objects.</p>
<dt><code>&#8211;cache-directory</code>=/root/.cache/volatility</p>
<dd> Directory where cache files are stored.</p>
<dt><code>&#8211;cache</code></p>
<dd> Use caching.</p>
<dt><code>&#8211;tz</code>=TZ</p>
<dd> Set the timezone for displaying timestamps using pytz (if installed) or tzset</p>
<dt><code>-f</code> FILENAME, <code>&#8211;filename</code>=FILENAME</p>
<dd> Filename to use when opening an <i>image</i>.</p>
<dt><code>&#8211;profile</code>=WinXPSP2x86</p>
<dd> Name of the profile to load (use <code>&#8211;info</code> to see a list of supported profiles).</p>
<dt><code>-l</code> LOCATION, <code>&#8211;location</code>=LOCATION</p>
<dd> A URN location from which to load an address space.</p>
<dt><code>-w</code>, <code>&#8211;write</code></p>
<dd> Enable write support.</p>
<dt><code>&#8211;dtb</code>=DTB</p>
<dd> DTB Address.</p>
<dt><code>&#8211;shift</code>=SHIFT</p>
<dd> Mac KASLR shift address.</p>
<dt><code>&#8211;output</code>=text</p>
<dd> Output in this format.</p>
<dt><code>&#8211;output-file</code>=OUTPUT_FILE</p>
<dd> Write output in this file.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Verbose information.</p>
<dt><code>-g</code> KDBG, <code>&#8211;kdbg</code>=KDBG</p>
<dd> Specify a specific KDBG virtual address. For 64-bit Windows 8 and above this is the address of KdCopyDataBlock.</p>
<dt><code>&#8211;force</code></p>
<dd> Force utilization of suspect profile.</p>
<dt><code>-k</code> KPCR, <code>&#8211;kpcr</code>=KPCR</p>
<dd> Specify a specific KPCR address.</p>
<dt><code>&#8211;cookie</code>=COOKIE</p>
<dd> Specify the address of nt!ObHeaderCookie (valid for Windows 10 only).</dl>
<h2>PLUGINS AND PROFILES</h2>
<p> The supported <i>plugin</i> commands and profiles can be viewed if using the command &#8216;$ volatility <code>&#8211;info</code>&#8216;. Note that Linux and MAC OSX allowed plugins will have the &#8216;linux_&#8217; and &#8216;mac_&#8217; prefixes. Plugins without these prefixes were designed for MS Windows. </p>
<p> Profiles are maps used by Volatility to understand the operational systems. The allowed MS Windows profiles are provided by the Volatility. </p>
<p> You must create your own profiles for Linux and MAC OSX. For this, you can use the tools from the directory /usr/share/python-volatility/tools. On Fedora with python-volatility package installed you can use script vol_genprofile to generate profile for the currently running kernel. </p>
<p> For MS Windows images, to determine the OS type, you can use: </p>
<pre>
    $ vol -f &lt;image&gt; imageinfo
    or
    $ vol -f &lt;image&gt; kdbgscan
</pre>
<h2>ENVIRONMENT VARIABLES</h2>
<p> On a GNU/Linux or OS X system, these variables can be set:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> VOLATILITY_PROFILE &#8211; Specifies a profile to be used as default, making unnecessary a &#8216;<code>&#8211;profile</code>&#8216; <i>option</i>.</p>
<dt>&bull;</p>
<dd> VOLATILITY_LOCATION &#8211; Specifies the path of an <i>image</i>. So, the Volatility command will not need a file name via &#8216;<code>-f</code>&#8216; <i>option</i>.</p>
<dt>&bull;</p>
<dd> VOLATILITY_KDBG &#8211; Specifies a KDBG address. See EXTRA PROCEDURES to more details.</dl>
</dl>
<p> Other <i>plugin</i> flags may be utilized in this way, for example KPCR, DTB or PLUGINS. When exporting variables, simply prefix VOLATILITY_ before the flag name (e.g. VOLATILITY_KPCR). Otherwise, the flag name remains the same when adding it to the configuration file. </p>
<p> If you have a path with a space or more in the name, spaces should be replaced with %20 instead (e.g. LOCATION=file:///tmp/my%20image.img). </p>
<p> Example: </p>
<pre>
    $ export VOLATILITY_PROFILE=Win7SP0x86
    $ export VOLATILITY_LOCATION=file:///tmp/myimage.img
    $ export VOLATILITY_KDBG=0x82944c28
</pre>
<h2>CONFIGURATION FILES</h2>
<p> Configuration files are typically &#8216;volatilityrc&#8217; in the current directory or &#8216;~/.volatilityrc&#8217; in user&#8217;s home directory, or at user specified path, using the <code>&#8211;conf-file</code> <i>option</i>. An example of the file contents is shown below: </p>
<pre>
    [DEFAULT]
    PROFILE=Win7SP0x86
    LOCATION=file:///tmp/myimage.img
    KDBG=0x82944c28
</pre>
<p> Other <i>plugin</i> flags may be utilized in this way, for example KPCR, DTB or PLUGINS. When exporting variables, simply prefix VOLATILITY_ before the flag name (e.g. VOLATILITY_KPCR). Otherwise, the flag name remains the same when adding it to the configuration file. </p>
<p> If you have a path with a space or more in the name, spaces should be replaced with %20 instead (e.g. LOCATION=file:///tmp/my%20image.img).</p>
<h2>EXTRA PROCEDURES</h2>
<p> Setting a timezone </p>
<pre>
  Timestamps extracted from memory can either be in system-local time, or in Universal Time
  Coordinates (UTC). If they're in UTC, Volatility can be instructed to display them in a time
  zone of the analyst's choosing. To choose a timezone, use one of the standard timezone
  names (such as America/Sao_Paulo, Europe/London, US/Eastern or most Olson timezones) with
  the --tz=TIMEZONE flag.
  Volatility attempts to use pytz if installed, otherwise it uses tzset.
  Please note that specifying a timezone will not affect how system-local times are displayed. If
  you identify a time that you know is UTC-based, please file it as an issue in the issue tracker.
  By default the _EPROCESS CreateTime and ExitTime timestamps are in UTC.
</pre>
<p> Setting the DTB </p>
<pre>
  The DTB (Directory Table Base) is what Volatility uses to translate virtual addresses to physical
  addresses. By default, a kernel DTB is used (from the Idle/System process). If you want to use a
  different process's DTB when accessing data, supply the address to --dtb=ADDRESS.
</pre>
<p> Setting the KDBG address (this is a Windows-only <i>option</i>) </p>
<p>  Volatility scans for the &#8216;_KDDEBUGGER_DATA64&#8217; structure using hard-coded signatures &#8220;KDBG&#8221; and<br />
  a series of sanity checks. These signatures are not critical for the operating system to function<br />
  properly, thus malware can overwrite them in attempt to throw off tools that do rely on the<br />
  signature. Additionally, in some cases there may be more than one &#8216;_KDDEBUGGER_DATA64&#8217; (for<br />
  example if you apply a major OS update and don&#8217;t reboot), which can cause confusion and lead to<br />
  incorrect process and module listings, among other problems. If you know the address<br />
  add &#8216;_KDDEBUGGER_DATA64&#8217;, you can specify it with &#8211;kdbg=ADDRESS and this override the automated<br />
  scans. For more information, see the kdbgscan plugin.<br />
 Setting the KPCR address (this is a Windows-only <i>option</i>) </p>
<p>  There is one KPCR (Kernel Processor Control Region) for each CPU on a system. Some Volatility<br />
  plugins display per-processor information. Thus if you want to display data for a specific CPU, for<br />
  example CPU 3 instead of CPU 1, you can pass the address of that CPU&#8217;s KPCR with &#8211;kpcr=ADDRESS.<br />
  To locate the KPCRs for all CPUs, see the kpcrscan plugin. Also note that starting in Volatility 2.2,<br />
  many of the plugins such as idt and gdt automatically iterate through the list of KPCRs.<br />
 Enabling write support </p>
<pre>
  Write support in Volatility should be used with caution. Therefore, to actually enable it, you must
  not only type --write on command-line but you must type a 'password' in response to a question that
  you'll be prompted with.  In most cases you will not want to use write support since it can lead to
  corruption or modification of data in your memory dump. However, special cases exist that make this
  feature really interesting. For example, you could cleanse a live system of certain malware by
  writing to RAM over firewire, or you could break into a locked workstation by patching bytes in the
  winlogon DLLs.
</pre>
<p> Specifying additional <i>plugin</i> directories </p>
<pre><code>
  Volatility's plugin architecture can load plugin files from multiple directories at once. In the
  Volatility source code, most plugins are located in volatility/plugins. However, there is another
  directory (volatility/contrib) which is reserved for contributions from third party developers, or
  weakly supported plugins that simply are not enabled by default. To access these plugins you just
  type --plugins=contrib/plugins on command-line. It also enables you to create a separate directory
  of your own plugins that you can manage without having to add/remove/modify files in the core
  Volatility directories.
  Notes:
  * On Fedora systems, the contrib/plugins directory is at:
    /usr/lib/python2.7/site-packages/volatility/contrib
  * Subdirectories will also be traversed as long as there is an __init__.py file (which can be empty)
    within them.
  * The parameter to --plugins can also be a zip file containing the plugins such
    as --plugins=myplugins.zip. Due to the way plugins are loaded, the external plugins directory
    or zip file must be specified before any plugin-specific arguments (including the name of the
    plugin). Example:
    $ vol --plugins=contrib -f XPSP3x86.vmem example
</code></pre>
<p> Choosing an output format </p>
<pre>
  By default, plugins use text renderers to standard output. If you want to redirect to a file, you
  can of course use the console's redirection (i.e. &gt; out.txt) or you could use --output-file=out.txt.
  The reason you can also choose --output=FORMAT is for allowing plugins to also render output as HTML,
  JSON, SQL, or whatever you choose. However, there are no plugins with those alternate output formats
  pre-configured for use, so you'll need to add a function named render_html, render_json, render_sql,
  respectively to each plugin before using --output=HTML.
</pre>
<p> Plugin specific options </p>
<pre>
  Many plugins accept arguments of their own, which are independent of the global options. To see the
  list of available options, type both the plugin name and -h/--help on command-line.
    $ vol dlllist -h
</pre>
<p> Debug mode </p>
<pre>
  If something isn't happening in Volatility the expected way, try to run the command with -d/--debug.
  This will enable the printing of debug messages to standard error. To more debug levels, as in using
  pdb debugger), add -d -d -d to command.
</pre>
<p> Using Volatility as a library </p>
<pre>
  Although its possible to use Volatility as a library, (there are plans to support it better in the
  future). Currently, to import Volatility from a python script, the following example code can be used:
    $ python
    &gt;&gt;&gt; import volatility.conf as conf
    &gt;&gt;&gt; import volatility.registry as registry
    &gt;&gt;&gt; registry.PluginImporter()
    &lt;volatility.registry.PluginImporter object at 0x7f9608f3ac10&gt;
    &gt;&gt;&gt; config = conf.ConfObject()
    &gt;&gt;&gt; import volatility.commands as commands
    &gt;&gt;&gt; import volatility.addrspace as addrspace
    &gt;&gt;&gt; registry.register_global_options(config, commands.Command)
    &gt;&gt;&gt; registry.register_global_options(config, addrspace.BaseAddressSpace)
    &gt;&gt;&gt; config.parse_options()
    &gt;&gt;&gt; config.PROFILE=&quot;WinXPSP2x86&quot;
    &gt;&gt;&gt; config.LOCATION = &quot;file:///media/memory/private/image.dmp&quot;
    &gt;&gt;&gt; import volatility.plugins.taskmods as taskmods
    &gt;&gt;&gt; p = taskmods.PSList(config)
    &gt;&gt;&gt; for process in p.calculate():
    ...   print process
</pre>
<h2>EXAMPLES</h2>
<p> To see all available plugins, profiles, scanner checks and address spaces: </p>
<pre>
    $ vol --info
</pre>
<p> To list all active processes found in a MS Windows 8 SP0 <i>image</i>: </p>
<pre>
    $ vol -f win8.raw --profile=Win8SP0x86 pslist
</pre>
<p> To list all active processes found in a MS Windows 8 SP0 <i>image</i>, using a timezone: </p>
<pre>
    $ vol -f win8.raw --profile=Win8SP0x86 pslist --tz=America/Sao_Paulo
</pre>
<p> To show the kernel bnuffer from a Linux 3.2.63 <i>image</i>: </p>
<pre>
    $ vol -f mem.dd --profile=Linux_3_2_63_x64 linux_dmesg
</pre>
<h2>NOTES</h2>
<p> This manpage was based in some tests and several official documents about Volatility. For other information and tutorials, see:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <a rel="nofollow" href="http://www.volatilityfoundation.org">http://www.volatilityfoundation.org</a></p>
<dt>&bull;</p>
<dd> <a rel="nofollow" href="https://github.com/volatilityfoundation/volatility/wiki">https://github.com/volatilityfoundation/volatility/wiki</a></dl>
</dl>
<h2>AUTHOR</h2>
<p> Volatility was written by Volatility Foundation and several contributors. For contact, use the email &lt;info [at] volatilityfoundation.org&gt;. </p>
<p> This manual page was written by Joao Eriberto Mota Filho &lt;eriberto [at] debian.org&gt; for the Debian project (but may be used by others). </p>
<h2>Index</h2>
