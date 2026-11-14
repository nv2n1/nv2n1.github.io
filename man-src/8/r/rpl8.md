---
title: "rpl8(8)"
name: "rpl8"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rpl8/"
description: "rpl8 – Firmware loader for DVD drives"
---

<p>rpl8 &#8211; Firmware loader for DVD drives</p>
<h2>Synopsis</h2>
<p><code>rpl8</code> <i>/dev/cdrom</i> [-[<code>dump-only</code>]|<i>firmwarefile</i>]</p>
<h2>Description</h2>
<p><code>rpl8</code> is a program for Linux 2.4 and upwards that uploads firmware to DVD drives (mostly DVD+RW). </p>
<p> <code>rpl8</code> stands for RICOH Program Loader 8, though it also supports Program Loader 9. </p>
<p> The program never updates Program Loader code so that you should always be able to downgrade your firmware in case something goes wrong. </p>
<p> So far <code>rpl8</code> has been tested with the following:<br />
 * HP dvd100i<br />
 * Ricoh MP5120A<br />
 * Philips DVDRW208<br />
 * HP dvd200i </p>
<p> To run <code>rpl8</code> correctly, make sure you have no media in drive. Optionally go to single user mode and reboot after uploading the new firmware.</p>
<h2>Options</h2>
<dl>
<dt>-[<code>dump-only</code>]</p>
<dd>Only backs up the firmware. Note that you might have to reboot even after this.</dl>
<h2>Bugs</h2>
<p>Getting messages like this is &quot;normal&quot;</p>
<dl>
<dd>ide-scsi: Strange, packet command initiated yet DRQ isn&#8217;t asserted</dl>
<h2>Author</h2>
<p><code>rpl8</code> is in public domain. </p>
<p> This manual page was written by Elias Kunnas &lt;elias_kunnas [at] welho.com&gt;, for the Debian project (but may be used by others).</p>
