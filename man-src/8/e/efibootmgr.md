---
title: "efibootmgr(8)"
name: "efibootmgr"
section: "8"
letter: "e"
url: "/docs/linux/man/8-efibootmgr/"
description: "efibootmgr – manipulate the UEFI Boot Manager"
---

<p>efibootmgr &#8211; manipulate the UEFI Boot Manager</p>
<h2>Synopsis</h2>
<p><code>efibootmgr</code> [ <code>-a</code> ] [ <code>-A</code> ] [ <code>-b </code><i>XXXX</i> ] [ <code>-r</code> | <code>-y</code> ] [ <code>-B</code> ] [ <code>-c</code> ] [ <code>-d </code><i>DISK</i> ] [ <code>-D</code> ] [ <code>-e </code><i>1|3|-1</i> ] [ <code>-E </code><i>NUM</i> ] [ <code>-g</code> ] [ <code>-i </code><i>NAME</i> ] [ <code>-l </code><i>NAME</i> ] [ <code>-L </code><i>LABEL</i> ] [ <code>-m </code><i>t|f</i> ] [ <code>-M </code><i>X</i> ] [ <code>-n </code><i>XXXX</i> ] [ <code>-N</code> ] [ <code>-o </code><i>XXXX</i><code>,</code><i>YYYY</i><code>,</code><i>ZZZZ</i><i> &#8230;</i> ] [ <code>-O</code> ] [ <code>-p </code><i>PART</i> ] [ <code>-q</code> ] [ <code>-t </code><i>seconds</i> ] [ <code>-T</code> ] [ <code>-u</code> ] [ <code>-v</code> ] [ <code>-V</code> ] [ <code>-w</code> ] [ <code>-@ </code><i>file</i> ] </p>
<h2>Description</h2>
<p><code>efibootmgr</code> is a userspace application used to modify the UEFI Boot Manager. This application can create and destroy boot entries, change the boot order, change the next running boot option, and more. </p>
<p> Details on the UEFI Boot Manager are available from the UEFI Specification, v1.02 or later, available from: <a rel="nofollow" href="http://www.uefi.org">http://www.uefi.org</a> </p>
<dl>
<dd><code>Note:</code> efibootmgr requires that the kernel support access to EFI non-volatile variables through <i>/sys/firmware/efi/vars</i> or <i>/sys/firmware/efi/efivars/</i>.</dl>
<h2>Options</h2>
<p>The following is a list of options accepted by efibootmgr:</p>
<dl>
<dt><code>-a | &#8211;active</code></p>
<dd>Sets bootnum active</p>
<dt><code>-A | &#8211;inactive</code></p>
<dd>Sets bootnum inactive</p>
<dt><code>-b | &#8211;bootnum </code><i>XXXX</i></p>
<dd>Modify Boot<i>XXXX</i> (hex)</p>
<dt><code>-B | &#8211;delete-bootnum</code></p>
<dd>Delete bootnum</p>
<dt><code>-c | &#8211;create</code></p>
<dd>Create new variable bootnum and add to bootorder</p>
<dt><code>-d | &#8211;disk </code><i>DISK</i></p>
<dd>The disk containing the loader (defaults to <i>/dev/sda</i>)</p>
<dt><code>-D | &#8211;remove-dups</code></p>
<dd>Remove duplicated entries from BootOrder</p>
<dt><code>-e | &#8211;edd30 </code><i>1|3|-1</i></p>
<dd>Force EDD 1.0 or 3.0 creation variables, or guess.</p>
<dt><code>-E | &#8211;edd-device </code><i>NUM</i></p>
<dd>EDD 1.0 device number (defaults to 0x80)</p>
<dt><code>-g | &#8211;gpt</code></p>
<dd>Force disk with invalid PMBR to be treated as GPT</p>
<dt><code>-i | &#8211;iface </code><i>NAME</i></p>
<dd>create a netboot entry for the named interface</p>
<dt><code>-l | &#8211;loader </code><i>NAME</i></p>
<dd>Specify a loader (defaults to <i>\elilo.efi</i>)</p>
<dt><code>-L | &#8211;label </code><i>LABEL</i></p>
<dd>Boot manager display label (defaults to &quot;Linux&quot;)</p>
<dt><code>-m | &#8211;mirror-below-4G </code><i>t|f</i></p>
<dd>Set t if you want to mirror memory below 4GB</p>
<dt><code>-M | &#8211;mirror-above-4G </code><i>X</i></p>
<dd>X percentage memory to mirror above 4GB. Floating-point value with up to 2 decimal places is accepted.</p>
<dt><code>-n | &#8211;bootnext </code><i>XXXX</i></p>
<dd>Set BootNext to XXXX (hex)</p>
<dt><code>-N | &#8211;delete-bootnext</code></p>
<dd>Delete BootNext</p>
<dt><code>-o | &#8211;bootorder </code><i>XXXX</i><code>,</code><i>YYYY</i><code>,</code><i>ZZZZ</i></p>
<dd>Explicitly set BootOrder (hex). Any value from 0 to FFFF is accepted so long as it corresponds to an existing Boot#### variable, and zero padding is not required.</p>
<dt><code>-O | &#8211;delete-bootorder</code></p>
<dd>Delete BootOrder</p>
<dt><code>-p | &#8211;part </code><i>PART</i></p>
<dd>Partition number containing the bootloader (defaults to 1)</p>
<dt><code>-q | &#8211;quiet</code></p>
<dd>Quiet mode &#8211; supresses output.</p>
<dt><code>-r | &#8211;driver</code></p>
<dd>Operate on Driver#### variables instead of Boot#### variables.</p>
<dt><code>-t | &#8211;timeout </code><i>seconds</i></p>
<dd>Boot Manager timeout, in <i>seconds</i>.</p>
<dt><code>-T | &#8211;delete-timeout</code></p>
<dd>Delete Timeout variable.</p>
<dt><code>-u | &#8211;unicode | &#8211;UCS-2 </code></p>
<dd>Handle extra command line arguments as UCS-2 (default is ASCII)</p>
<dt><code>-v | &#8211;verbose</code></p>
<dd>Verbose mode &#8211; prints additional information</p>
<dt><code>-V | &#8211;version</code></p>
<dd>Just print version string and exit.</p>
<dt><code>-w | &#8211;write-signature</code></p>
<dd>write unique signature to the MBR if needed</p>
<dt><code>-y | &#8211;sysprep</code></p>
<dd>Operate on SysPrep#### variables instead of Boot#### variables.</p>
<dt><code>-@ | &#8211;append-binary-args </code></p>
<dd>append extra variable args from file (use &#8211; to read from stdin). Data in file is appended as command line arguments to the boot loader command, with no modification to the data, so you can pass any binary or text data necessary.</dl>
<h2>Examples</h2>
<h3>Displaying the current settings (must be root):</h3>
<pre><code>[root [at] localhost ~]# efibootmgr</code>
BootCurrent: 0004
BootNext: 0003
BootOrder: 0004,0000,0001,0002,0003
Timeout: 30 seconds
Boot0000* Diskette Drive(device:0)
Boot0001* CD-ROM Drive(device:FF)
Boot0002* Hard Drive(Device:80)/HD(Part1,Sig00112233)
Boot0003* PXE Boot: MAC(00D0B7C15D91)
Boot0004* Linux</pre>
<p>Each of the above are boot variables, which are defined as follows:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>BootCurrent &#8211; the boot entry used to start the currently running system</p>
<dt>&bull;</p>
<dd>BootOrder &#8211; the boot order as would appear in the boot manager. The boot manager tries to boot the first active entry in this list. If unsuccessful, it tries the next entry, and so on.</p>
<dt>&bull;</p>
<dd>BootNext &#8211; the boot entry which is scheduled to be run on next boot. This supercedes BootOrder for one boot only, and is deleted by the boot manager after first use. This allows you to change the next boot behavior without changing BootOrder.</p>
<dt>&bull;</p>
<dd>Timeout &#8211; the time in seconds between when the boot manager appears on the screen until when it automatically chooses the startup value from BootNext or BootOrder.</p>
<dt>&bull;</p>
<dd>Five boot entries (0000 &#8211; 0004), along with the active/inactive flag (* means active) and the name displayed on the screen.</dl>
</dl>
<h3>Creating a new boot option</h3>
<p>An OS installer would call <code>efibootmgr -c</code>. This assumes that <i>/boot/efi</i> is your EFI System Partition, and is mounted at <i>/dev/sda1</i>. This creates a new boot option, called &quot;Linux&quot;, and puts it at the top of the boot order list. Options may be passed to modify the default behavior. The default OS Loader is <i>elilo.efi</i>.</p>
<h3>Changing the boot order</h3>
<p>Assuming the configuration in the first example, <code>efibootmgr -o 3,4</code> could be called to specify PXE boot first, then Linux boot.</p>
<h3>Changing the boot order for the next boot only</h3>
<p>Assuming the configuration in the first example, <code>efibootmgr -n 4</code> could be called to specify that the Linux entry be taken on next boot.</p>
<h3>Deleting a boot option</h3>
<p>Assuming the configuration in the first example, <code>efibootmgr -b 4 -B</code> could be called to delete entry 4 and remove it from the BootOrder.</p>
<h3>Creating network boot entries</h3>
<p>A system administrator wants to create a boot option to network boot. You create the boot entry with: <code>efibootmgr -c -i eth0 -L netboot [ -l &#8216;ilename.efi&#8217; ]</code></p>
<h2>Bugs</h2>
<p>Please direct any bugs, features, patches, etc. to the Red Hat bootloader team at <a rel="nofollow" href="https://github.com/rhboot/efibootmgr">https://github.com/rhboot/efibootmgr</a> .</p>
<h2>Author</h2>
<p>This man page was generated by dann frazier &lt;dannf [at] debian.org&gt; for the Debian GNU/Linux operating system and updated by Robert Bisewski &lt;contact [at] ibiscybernetics.com&gt;, but may be used by others.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-elilo/">elilo</a>(1) </p>
