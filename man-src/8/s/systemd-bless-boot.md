---
title: "systemd-bless-boot(8)"
name: "systemd-bless-boot"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-bless-boot/"
description: "systemd-bless-boot.service, systemd-bless-boot – Mark current boot process as successful"
---

<p>systemd-bless-boot.service, systemd-bless-boot &#8211; Mark current boot process as successful</p>
<h2>Synopsis</h2>
<p>systemd-bless-boot.service </p>
<p> /lib/systemd/system-bless-boot</p>
<h2>Description</h2>
<p>systemd-bless-boot.service is a system service that marks the current boot process as successful. It&#8217;s automatically pulled into the initial transaction when <code><a href="/docs/linux/man/8-systemd-bless-boot-generator/">systemd-bless-boot-generator</a></code>(8) detects that <code><a href="/docs/linux/man/7-systemd-boot/">systemd-boot</a></code>(7) style boot counting is used. </p>
<p> Internally, the service operates based on the <i>LoaderBootCountPath</i> EFI variable (of the vendor UUID <code>4a67b082-0a4c-41cf-b6c7-440b29bb8c4</code>), which is passed from the boot loader to the OS. It contains a file system path (relative to the EFI system partition) of the m[blue]<code>Boot Loader Specification</code>m[]<font SIZE="-2">[1]</font> compliant boot loader entry file or unified kernel image file that was used to boot up the system. <code>systemd-bless-boot.service</code> removes the two &#8216;tries done&#8217; and &#8216;tries left&#8217; numeric boot counters from the filename, which indicates to future invocations of the boot loader that the entry has completed booting successfully at least once. (This service will hence rename the boot loader entry file or unified kernel image file on the first successful boot.)</p>
<h2>Options</h2>
<p>The /lib/systemd/system-bless-boot executable may also be invoked from the command line, taking one of the following command arguments: </p>
<p> <code>status</code></p>
<dl>
<dd>The current status of the boot loader entry file or unified kernel image file is shown. This outputs one of &quot;good&quot;, &quot;bad&quot;, &quot;indeterminate&quot;, &quot;clean&quot;, depending on the state and previous invocations of the command. The string &quot;indeterminate&quot; is shown initially after boot, before it has been marked as &quot;good&quot; or &quot;bad&quot;. The string &quot;good&quot; is shown after the boot was marked as &quot;good&quot; with the <code>good</code> command below, and &quot;bad&quot; conversely after the <code>bad</code> command was invoked. The string &quot;clean&quot; is returned when boot counting is currently not in effect. </p>
<p> This command is implied if no command argument is specified.</dl>
<p> <code>good</code></p>
<dl>
<dd>When invoked, the current boot loader entry file or unified kernel image file will be marked as &quot;good&quot;, executing the file rename operation described above. This command is intended to be invoked at the end of a successful boot. The systemd-bless-boot.service unit invokes this command.</dl>
<p> <code>bad</code></p>
<dl>
<dd>When called the &#8216;tries left&#8217; counter in the boot loader entry file name or unified kernel image file name is set to zero, marking the boot loader entry or kernel image as &quot;bad&quot;, so that the boot loader won&#8217;t consider it anymore on future boots (at least as long as there are other entries available that are not marked &quot;bad&quot; yet). This command is normally not executed, but can be used to instantly put an end to the boot counting logic if a problem is detected and persistently mark the boot entry as bad.</dl>
<p> <code>indeterminate</code></p>
<dl>
<dd>This command undoes any marking of the current boot loader entry file or unified kernel image file as good or bad. This is implemented by renaming the boot loader entry file or unified kernel image file back to the path encoded in the <i>LoaderBootCountPath</i> EFI variable.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Print a short version string and exit.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/7-systemd-boot/">systemd-boot</a></code>(7), <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Boot Loader Specification</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/BOOT_LOADER_SPECIFICATION">https://systemd.io/BOOT_LOADER_SPECIFICATION</a></dl>
