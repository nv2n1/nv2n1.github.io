---
title: "hdparm(5)"
name: "hdparm"
section: "5"
letter: "h"
url: "/docs/linux/man/5-hdparm/"
description: "hdparm.conf – Debian configuration file for hdparm"
---

<p>hdparm.conf &#8211; Debian configuration file for hdparm</p>
<h2>Description</h2>
<p>This is the default configuration for hdparm for Debian. It is a rather simple script, so please follow the following guidelines :) Any line that begins with a comment is ignored &#8211; add as many as you like. </p>
<p> Note that an in-line comment is not supported. If a line consists of whitespace only (tabs, spaces, carriage return), it will be ignored, so you can space control fields as you like. ANYTHING ELSE IS PARSED!! </p>
<p> This means that lines with stray characters or lines that use non # comment characters will be interpreted by the initscript. This has probably minor, but potentially serious, side effects for your hard drives, so please follow the guidelines. Patches to improve flexibilty welcome. </p>
<p> Please read /usr/share/doc/hdparm/README.Debian for notes about known issues, especially if you have an MD array. </p>
<p> Note that if the init script causes boot problems, you can pass &#8216;nohdparm&#8217; on the kernel command line, and the script will not be run. </p>
<p> Setting an option outside of one of the stanzas enables it for all drives. </p>
<p> If an option is listed twice, the second instance replaces the first. </p>
<p> /sbin/hdparm is not run unless a block of the form: </p>
<p> <code>DEV {</code></p>
<dl>
<dt>option</dt>
<dd>
</dd><dt>option</dt>
<dd>
</dd><dt>}</dt>
<dd></dd></dl>
<p> exists. This blocks will cause /sbin/hdparm OPTIONS DEV to be run. Where OPTIONS is the concatenation of all options previously defined outside of a block and all options defined with in the block.</p>
<h2>Options</h2>
<dl>
<dt><code>-q</code> be quiet</dt>
<dd>quiet</dd>
<dt><code>-a</code> sector count for filesystem read-ahead</dt>
<dd>read_ahead_sect = 12</dd>
<dt><code>-A</code> disable/enable the IDE drive&#8217;s read-lookahead feature</dt>
<dd>lookahead = on</dd>
<dt><code>-b</code> bus state</dt>
<dd>bus = on</dd>
<dt><code>-B</code> apm setting</dt>
<dd>apm = 255</dd>
<dt><code>-B</code> apm setting when on battery</dt>
<dd>apm_battery = 127</dd>
<dt><code>-c</code> enable (E)IDE 32-bit I/O support &#8211; can be any of 0,1,3</dt>
<dd>io32_support = 1</dd>
<dt><code>-d</code> disable/enable the &quot;using_dma&quot; flag for this drive</dt>
<dd>dma = off</dd>
<dt><code>-D</code> enable/disable the on-drive defect management</dt>
<dd>defect_mana = off</dd>
<dt><code>-E</code> cdrom speed</dt>
<dd>cd_speed = 16</dd>
<dt><code>-k</code> disable/enable the &quot;keep_settings_over_reset&quot; flag for this drive</dt>
<dd>keep_settings_over_reset = off</dd>
<dt><code>-K</code> disable/enable the drive&#8217;s &quot;keep_features_over_reset&quot; flag</dt>
<dd>keep_features_over_reset = on</dd>
<dt><code>-m</code> sector count for multiple sector I/O</dt>
<dd>mult_sect_io = 32</dd>
<dt><code>-P</code> maximum sector count for the drive&#8217;s internal prefetch mechanism</dt>
<dd>prefetch_sect = 12</dd>
<dt><code>-r</code> read-only flag for device</dt>
<dd>read_only = off</dd>
<dt><code>-s</code> Enable/disable the power-on in standby feature</dt>
<dd>poweron_standby = off</dd>
<dt><code>-S</code> standby (spindown) timeout for the drive</dt>
<dd>spindown_time = 24</dd>
<dt><code>-u</code> interrupt-unmask flag for the drive</dt>
<dd>interrupt_unmask = on</dd>
<dt><code>-W</code> Disable/enable the IDE drive&#8217;s write-caching feature</dt>
<dd>write_cache = off</dd>
<dt><code>-X</code> IDE transfer mode for newer (E)IDE/ATA2 drives</dt>
<dd>transfer_mode = 34</dd>
<dt><code>-y</code> force to immediately enter the standby mode</dt>
<dd>standby</dd>
<dt><code>-Y</code> force to immediately enter the sleep mode</dt>
<dd>sleep</dd>
<dt><code>-Z</code> Disable the power-saving function of certain Seagate drives</dt>
<dd>disable_seagate</dd>
<dt><code>-M</code> Set the acoustic management properties of a drive</dt>
<dd>acoustic_management</dd>
<dt><code>-p</code> Set the chipset PIO mode</dt>
<dd>&nbsp;<wbr>chipset_pio_mode</dd>
<dt><code>&#8211;security-freeze</code> Freeze the drive&#8217;s security status</dt>
<dd>security_freeze</dd>
<dt><code>&#8211;security-unlock</code> Unlock the drive&#8217;s security</dt>
<dd>security_unlock = PWD</dd>
<dt><code>&#8211;security-set-pass</code> Set security password</dt>
<dd>security_pass = password</dd>
<dt><code>&#8211;security-disable</code> Disable drive locking</dt>
<dd>security_disable</dd>
<dt><code>&#8211;user-master</code> Specifies which password to select</dt>
<dd>security_mode = u</dd>
<dt><code>&#8211;security-mode</code> Set the security mode</dt>
<dd>security_mode = h</dd>
<dt>Root file systems.</dt>
<dd>Please see README.Debian for details. ROOTFS = /dev/hda</dd></dl>
<p> Blocks beginning with the keyword &#8216;command_line&#8217; instead of a device identifier are no longer supported for backwards compatibility by this version of hdparm. Options must be introduced by a correct device identifier instead so that they will be applied when the device becomes available.</p>
<h2>Author</h2>
<p>hdparm was written by Mark Lord &lt;mlord [at] pobox.com&gt; The init script and configuration file are currently maintained by Stephen Gran &lt;sgran [at] debian.org&gt;, but are the result of the work of many people. </p>
<p> This manual page was created by Stephen Gran &lt;sgran [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others).</p>
