---
title: "mtx(1)"
name: "mtx"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mtx/"
description: "mtx – control SCSI media changer devices"
---

<h2>NAME</h2>
<p> mtx &#8211; control SCSI media changer devices</p>
<h2>SYNOPSIS</h2>
<p> mtx [-f &lt;scsi-generic-device&gt;] [nobarcode] [invert] [noattach] command [ command &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>mtx</code> command controls single or multi-drive SCSI media changers such as tape changers, autoloaders, tape libraries, or optical media jukeboxes. It can also be used with media changers that use the &#8216;ATTACHED&#8217; API, presuming that they properly report the MChanger bit as required by the SCSI T-10 SMC specification.</p>
<h2>OPTIONS</h2>
<p> The first argument, given following <code>-f</code> , is the SCSI generic device corresponding to your media changer. Consult your operating system&#8217;s documentation for more information (for example, under Linux these are generally /dev/sg0 through /dev/sg15, under FreeBSD these are /dev/pass0 through /dev/passX, under SunOS it may be a file under /dev/rdsk). </p>
<p> The &#8216;invert&#8217; option will invert (flip) the media (for optical jukeboxes that allow such) before inserting it into the drive or returning it to the storage slot. </p>
<p> The &#8216;noattach&#8217; option forces the regular media changer API even if the media changer incorrectly reported that it uses the &#8216;ATTACHED&#8217; API. </p>
<p> The &#8216;nobarcode&#8217; option forces the loader to not request barcodes even if the loader is capable of reporting them. </p>
<p> Following these options there may follow one or more robotics control commands. Note that the &#8216;invert&#8217; and &#8216;noattach&#8217; options apply to ALL of robotics control commands. </p>
<h2>COMMANDS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Report the mtx version number (e.g. mtx 1.2.8) and exit. </p>
<dt><code>inquiry</code></p>
<dd> Report the product type (Medium Changer, Tape Drive, etc.), Vendor ID, Product ID, Revision, and whether this uses the Attached Changer API (some tape drives use this rather than reporting a Medium Changer on a separate LUN or SCSI address).</p>
<dt><code>noattach</code></p>
<dd> Make further commands use the regular media changer API rather than the _ATTACHED API, no matter what the &quot;Attached&quot; bit said in the Inquiry info. Needed with some brain-dead changers that report Attached bit but don&#8217;t respond to _ATTACHED API.</p>
<dt><code>inventory</code></p>
<dd> Makes the robot arm go and check what elements are in the slots. This is needed for a few libraries like the Breece Hill ones that do not automatically check the tape inventory at system startup.</p>
<dt><code>status</code></p>
<dd> Reports how many drives and storage elements are contained in the device. For each drive, reports whether it has media loaded in it, and if so, from which storage slot the media originated. For each storage slot, reports whether it is empty or full, and if the media changer has a bar code, MIC reader, or some other way of uniquely identifying media without loading it into a drive, this reports the volume tag and/or alternate volume tag for each piece of media. For historical reasons drives are numbered from 0 and storage slots are numbered from 1.</p>
<dt><code>load &lt;slotnum&gt; [ &lt;drivenum&gt; ]</code></p>
<dd> Load media from slot &lt;slotnum&gt; into drive &lt;drivenum&gt;. Drive 0 is assumed if the drive number is omitted.</p>
<dt><code>unload [&lt;slotnum&gt;] [ &lt;drivenum&gt; ]</code></p>
<dd> Unloads media from drive &lt;drivenum&gt; into slot &lt;slotnum&gt;. If &lt;drivenum&gt; is omitted, defaults to drive 0 (as do all commands). If &lt;slotnum&gt; is omitted, defaults to the slot that the drive was loaded from. Note that there&#8217;s currently no way to say &#8216;unload drive 1&#8217;s media to the slot it came from&#8217;, other than to explicitly use that slot number as the destination.</p>
<dt><code>[eepos &lt;operation&gt;] transfer &lt;slotnum&gt; &lt;slotnum&gt;</code></p>
<dd> Transfers media from one slot to another, assuming that your mechanism is capable of doing so. Usually used to move media to/from an import/export port. &#8216;eepos&#8217; is used to extend/retract the import/export tray on certain mid-range to high end tape libraries (if, e.g., the tray was slot 32, you might say say &#8216;eepos 1 transfer 32 32&#8217; to extend the tray). Valid values for eepos &lt;operation&gt; are 0 (do nothing to the import/export tray), 1, and 2 (what 1 and 2 do varies depending upon the library, consult your library&#8217;s SCSI-level documentation).</p>
<dt><code>[eepos &lt;operation&gt;] [invert] [invert2] exchange &lt;slotnum&gt; &lt;slotnum&gt; [&lt;slotnum&gt;]</code></p>
<dd> Move medium from the first slot to the second slot, placing the medium currently in the second slot either back into the first slot or into the optional third slot. </p>
<dt><code>first [&lt;drivenum&gt;]</code></p>
<dd> Loads drive &lt;drivenum&gt; from the first slot in the media changer. Unloads the drive if there is already media in it (note: you may need to eject the tape using your OS&#8217;s tape control commands first). Note that this command may not be what you want on large tape libraries &#8212; e.g. on Exabyte 220, the first slot is usually a cleaning tape. If &lt;drivenum&gt; is omitted, defaults to first drive.</p>
<dt><code>last [&lt;drivenum&gt;]</code></p>
<dd> Loads drive &lt;drivenum&gt; from the last slot in the media changer. Unloads the drive if there is already a tape in it. (Note: you may need to eject the tape using your OS&#8217;s tape control commands first).</p>
<dt><code>previous [&lt;drivenum&gt;]</code></p>
<dd> Unloads the drive and loads the previous tape in sequence. If the drive was empty, loads the first tape into the drive.</p>
<dt><code>next [&lt;drivenum&gt;]</code></p>
<dd> Unloads the drive and loads the next tape in sequence. If the drive was empty, loads the first tape into the drive.</p>
<dt><code>position &lt;slotnum&gt;</code></p>
<dd> Positions the robot at a specific slot. Needed by some changers to move to and open the import/export, or mailbox, slot.</p>
<dt><code>eject</code></p>
<dd> Eject the tape currently in the drive. </p>
</dl>
<h2>AUTHORS</h2>
<p> The original &#8216;mtx&#8217; program was written by Leonard Zubkoff and extensively revised for large multi-drive libraries with bar code readers by Eric Lee Green &lt;eric [at] badtux.org&gt;. See &#8216;mtx.c&#8217; for other contributors.</p>
<h2>BUGS AND LIMITATIONS</h2>
<p> You may need to do a &#8216;mt offline&#8217; on the tape drive to eject the tape before you can issue the &#8216;mtx unload&#8217; command. The Exabyte EZ-17 and 220 in particular will happily sit there snapping the robot arm&#8217;s claws around thin air trying to grab a tape that&#8217;s not there. </p>
<p> For some Linux distributions, you may need to re-compile the kernel to scan SCSI LUN&#8217;s in order to detect the media changer. Check /proc/scsi/scsi to see what&#8217;s going on. </p>
<p> If you try to unload a tape to its &#8216;source&#8217; slot, and said slot is full, it will instead put the tape into the first empty slot. Unfortunately the list of empty slots is not updated between commands on the command line, so if you try to unload another drive to a full &#8216;source&#8217; slot during the same invocation of &#8216;mtx&#8217;, it will try to unload to the same (no longer empty) slot and will urp with a SCSI error. </p>
<p> This program reads the Mode Sense Element Address Assignment Page (SCSI) and requests data on all available elements. For larger libraries (more than a couple dozen elements) this sets a big Allocation_Size in the SCSI command block for the REQUEST_ELEMENT_STATUS command in order to be able to read the entire result of a big tape library. Some operating systems may not be able to handle this. Versions of Linux earlier than 2.2.6, in particular, may fail this request due to inability to find contiguous pages of memory for the SCSI transfer (later versions of Linux &#8216;sg&#8217; device do scatter-gather so that this should no longer be a problem). </p>
<p> The <code>eepos</code> command remains in effect for all further commands on a command line. Thus you might want to follow <code>eepos 1 transfer 32 32</code> with <code>eepos 0</code> as the next command (which clears the <code>eepos</code> bits). </p>
<p> Need a better name for &#8216;eepos&#8217; command! (&#8216;eepos&#8217; is the name of the bit field in the actual low-level SCSI command, and has nothing to do with what it does). </p>
<p> This program has only been tested on Linux with a limited number of tape loaders (a dual-drive Exabyte 220 tape library, with bar-code reader and 21 slots, an Exabyte EZ-17 7-slot autoloader, and a Seagate DDS-4 autochanger with 6 slots). It may not work on other operating systems with larger libraries, due to the big SCSI request size. Please see the projecdt page <a rel="nofollow" href="http://sourceforge.net/projects/mtx">http://sourceforge.net/projects/mtx</a> for information on reporting bugs, requesting features and the mailing list for peer support.</p>
<h2>HINTS</h2>
<p> Under Linux, <code>cat /proc/scsi/scsi</code> will tell you what SCSI devices you have. You can then refer to them as <code>/dev/sga,</code> <code>/dev/sgb, </code> etc. by the order they are reported. </p>
<p> Under FreeBSD, <code>camcontrol devlist</code> will tell you what SCSI devices you have, along with which <code>pass</code> device controls them. </p>
<p> Under Solaris, set up your &#8216;sgen&#8217; driver so that it&#8217;ll look for tape changers (see /kernel/drv/sgen.conf and the sgen man page), type <code>touch /reconfigure</code> then reboot. You can find your changer in /devices by typing <code>/usr/sbin/devfsadm -C</code> to clean out no-longer-extant entries in your /devices directory, then <code>find /devices -name \*changer -print</code> to find the device name. Set the symbolic link <code>/dev/changer </code> to point to that device name (if it is not doing so already). </p>
<p> With BRU, set your mount and unmount commands as described on the BRU web site at <a rel="nofollow" href="http://www.bru.com">http://www.bru.com</a> to move to the next tape when backing up or restoring. With GNU <code>tar,</code> see <code>mtx.doc</code> for an example of how to use <code>tar</code> and <code>mtx</code> to make multi-tape backups. </p>
<h2>AVAILABILITY</h2>
<p> This version of <code>mtx</code> is currently being maintained by Robert Nelson &lt;robertnelson [at] users.sourceforge.net&gt; . The &#8216;mtx&#8217; home page is <a rel="nofollow" href="http://mtx.sourceforge.net">http://mtx.sourceforge.net</a> and the actual code is currently available there and via SVN from <a rel="nofollow" href="http://sourceforge.net/projects/mtx.">http://sourceforge.net/projects/mtx.</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mt/">mt</a></code>(1),<code><a href="/docs/linux/man/1-loaderinfo/">loaderinfo</a></code>(1),<code><a href="/docs/linux/man/1-tapeinfo/">tapeinfo</a></code>(1),<code><a href="/docs/linux/man/1-scsitape/">scsitape</a></code>(1),<code><a href="/docs/linux/man/1-scsieject/">scsieject</a></code>(1) </p>
<h2>Index</h2>
