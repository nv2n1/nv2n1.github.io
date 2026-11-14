---
title: "growisofs(1)"
name: "growisofs"
section: "1"
letter: "g"
url: "/docs/linux/man/1-growisofs/"
description: "growisofs – combined genisoimage frontend/DVD recording program."
---

<h2 class="name">NAME</h2>
<p> growisofs &#8211; combined genisoimage frontend/DVD recording program. </p>
<h2>SYNOPSIS</h2>
<p> <code>growisofs</code> [<code>-dry-run</code>] [<code>-dvd-compat</code>] [<code>-overburn</code>] [<code>-speed=1</code>] -[<code>Z|M</code>] <i>/dev/dvd</i> <i>&lt;genisoimage-options&gt;</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>growisofs</code> was originally designed as a frontend to <code>genisoimage</code> to facilitate appending of data to ISO9660 volumes residing on random-access media such as DVD+RW, DVD-RAM, plain files, hard disk partitions. In the course of development general purpose DVD recording support was implemented, and as of now <code>growisofs</code> supports not only random-access media, but even mastering of multisession DVD media such as DVD+R and DVD-R/-RW, as well as Blu-ray Disc. In addition <code>growisofs</code> supports first-/single-session recording of <i>arbitrary pre-mastered image</i> (formatted as UDF, ISO9660 or any other file system, if formatted at all) to all supported DVD media types. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-Z&nbsp;/dev/dvd</code></p>
<dd> Burn an initial session to the selected device. A special form of this option is recognized to support burning of pre-mastered images. See EXAMPLES section for further details.</p>
<dt><code>-M&nbsp;/dev/dvd</code></p>
<dd> Merge a new session to an existing one.</p>
<dt><code>-version</code></p>
<dd> Print version information and invoke <code>genisoimage</code>, also with -version option.</p>
<dt><code>-dvd-compat</code></p>
<dd> Provide maximum media compatibility with DVD-ROM/-Video. In write-once DVD+R or DVD-R context this results in unappendable recording (closed disk). In DVD+RW context it instructs the logical unit to explicitly burn [otherwise optional] lead-out.</p>
<dt><code>-dry-run</code></p>
<dd> At dry-run <code>growisofs</code> performs all the steps till, but not including the first write operation. Most notably check for &quot;overburn&quot; condition is performed, which implies that genisoimage is invoked and terminated prematurely.</p>
<dt><code>-overburn</code></p>
<dd> Normally single layer DVD media can accommodate up to approximately 4.700.000.000 bytes (in marketing speech 4.7GB). In other words a DVD can contain about 4.377 GiB or 4482 MiB. Same kind of arithmetics applies to Blu-ray Disc capacity of 25.000.000.000 bytes. Anyway, growisofs won&#8217;t start without this option, if &quot;overburn&quot; condition appears to be unavoidable.</p>
<dt><code>-speed=N</code></p>
<dd> An option to control recording velocity. Most commonly you&#8217;ll use <code>-speed=1</code> with &quot;no-name&quot; media, if default speed setting messes up the media. Keep in mind that <code>N</code> essentially denotes speed <i>closest</i> to N*1385KBps in DVD or N*4496KBps in Blu-ray Disc case among those offered by unit for currently mounted media. The list can be found in <code>dvd+rw-mediainfo</code> output. Note that Blu-ray Disc recordings are commonly performed at ~1/2 of advertised speed, because of defect management being in effect.</p>
<dt><code>&lt;genisoimage-options&gt;</code></p>
<dd> More options can be found in the manpage for <code>genisoimage</code>. </p>
</dl>
<p> There are several undocumented options commonly denoted with <code>-use-the-force-luke</code> prefix. Some of them serve debugging purposes. Some require certain knowledge about recording process or even OS kernel internals and as being such can induce confusing behaviour. Some are to be used in very specific situations better recognized by front-ends or automated scripts. Rationale behind leaving these options undocumented is that those few users who would actually need to use them directly can as well consult the source code or obtain specific instructions elsewhere. </p>
<h2>DIFFERENCES WITH RUNNING GENISOIMAGE DIRECTLY</h2>
<p> When using growisofs you may not use the <code>-o </code> option for an output file. <code>growisofs</code> dumps the image directly to the media; </p>
<p> You don&#8217;t have to specify the <code>-C</code> option to create a higher level session on a multisession disk, <code>growisofs </code> will construct one for you; </p>
<p> Otherwise everything that applies to <i>[multisession] </i> mastering with <code>genisoimage</code> applies to <code>growisofs </code> as well. <code>growisofs</code> needs at least <code>mkisofs</code> version 1.14, version 2.0 is required for multisession write-once recordings or <code>genisoimage.</code> </p>
<h2>EXAMPLES</h2>
<p> Actual device names vary from one operating system to another. We use <i>/dev/dvd</i> as a collective name or as symbolic link to the actual device if you wish. Under Linux it will most likely be an ide-scsi device such as &quot;/dev/scd0.&quot; Under NetBSD/OpenBSD it has to be a <i>character</i> SCSI CD-ROM device such as &quot;/dev/rcd0c.&quot; Under Solaris it also has to be a <i>character</i> SCSI/ATAPI CD-ROM device, e.g. &quot;/dev/rdsk/c0t1d0s2&quot; or &quot;/vol/dev/aliases/cdrom0.&quot; And likewise in HP-UX, IRIX and Mac OS X&#8230; </p>
<p> To master and burn an ISO9660 volume with Joliet and Rock-Ridge extensions on a DVD or Blu-ray Disc: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>growisofs <code>-Z</code> /dev/dvd <code>-R -J</code> /some/files</p>
<p> To append more data to same media: </p>
<p>&nbsp;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>growisofs&nbsp;<code>-M</code>&nbsp;/dev/dvd&nbsp;<code>-R -J</code>&nbsp;/more/files</p>
<p> Make sure to use <i>the same options</i> for both initial burning and when appending data. </p>
<p> To finalize the multisession DVD maintaining maximum compatibility: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>growisofs <code>-M</code> /dev/dvd<code>=</code>/dev/zero</p>
<p> To use <code>growisofs</code> to write a pre-mastered ISO-image to a DVD: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>growisofs -dvd-compat -Z /dev/dvd<code>=</code>image.iso</p>
<p> where image.iso represents an arbitrary object in the filesystem, such as file, named pipe or device entry. Nothing is growing here and command name is not intuitive in this context. </p>
<h2>NOTES</h2>
<p> If executed under <a href="/docs/linux/man/8-sudo/">sudo</a>(8) growisofs refuses to start. This is done for the following reason. Naturally growisofs has to access the data set to be recorded to optical media, either indirectly by letting genisoimage generate ISO9660 layout on-the-fly or directly if a pre-mastered image is to be recorded. Being executed under <a href="/docs/linux/man/8-sudo/">sudo</a>(8), growisofs effectively grants sudoers read access to <i>any</i> file in the file system. The situation is intensified by the fact that growisofs parses GENISOIMAGE environment variable in order to determine alternative path to genisoimage executable image. This means that being executed under <a href="/docs/linux/man/8-sudo/">sudo</a>(8), growisofs effectively grants sudoers right to execute program of their choice with elevated privileges. If you for any reason still find the above acceptable and are willing to take the consequences, then consider running following wrapper script under <a href="/docs/linux/man/8-sudo/">sudo</a>(8) in place for real growisofs binary. </p>
<pre>
        #!/bin/ksh
        unset SUDO_COMMAND
        export GENISOIMAGE=/path/to/trusted/genisoimage
        exec growisofs &quot;$@&quot;
</pre>
<p> But note that the recommended alternative to the above &quot;workaround&quot; is actually to install growisofs set-root-uid, in which case it will drop privileges prior accessing data or executing genisoimage in order to preclude unauthorized access to the data. </p>
<p> If the media already carries isofs and <code>growisofs</code> is invoked with <code>-Z</code> option non-interactively, e.g. through cron, it shall fail with &quot;FATAL: /dev/dvd already carries isofs!&quot; Note that only ISO9660 is recognized, you can perfectly zap e.g. an UDF filesystem non-interactively. Recommendation is to prepare media for unattended usage by re-formatting or nullifying first 64KB in advance. </p>
<p> &quot;Overburn&quot; protection in pre-mastered image context works only with plain files and ISO9660 formatted volumes. E.g. [given that /dev/root is an ext2 formatted file system larger than 4.7GB] /dev/dvd=/dev/root is bound to produce corrupted recording. </p>
<p> Note that DVD+RW re-formatting procedure does not substitute for blanking. If you want to nullify the media, e.g. for privacy reasons, do it explicitly with &#8216;growisofs -Z /dev/dvd<code>=/dev/zero</code>&#8216;. </p>
<p> Playback of re-writable DVD media, both DVD+RW and DVD-RW, might be limited in legacy DVD-ROM/-Video units. In most cases this is due to lower reflectivity of such media. </p>
<p> Even though growisofs supports it, playback of multisession write-once DVD might be limited to the first session for two reasons: </p>
<dl>
<dt>&bull;</p>
<dd> not all DVD-ROM players are capable of multi-border DVD-R playback, even less are aware of DVD+R multisessioning, burner unit therefore might be the only one in your vicinity capable of accessing files written at different occasions;</p>
<dt>&bull;</p>
<dd> OS might fail to mount multisession DVD for various reasons;</dl>
<p> The above is not applicable to DVD+RW, DVD-RW Restricted Overwrite, DVD-RAM or Blu-ray Disc, as volumes are grown within a single session. </p>
<p> When growisofs &quot;runs into&quot; blank Blu-ray Disc media, BD-RE or BD-R, it gets pre-formatted with minimal spare area size of 256MB. </p>
<h2>SEE ALSO</h2>
<p> Most up-to-date information on dvd+rw-tools is available at <a rel="nofollow" href="http://fy.chalmers.se/~appro/linux/DVD+RW/.">http://fy.chalmers.se/~appro/linux/DVD+RW/.</a> </p>
<p> The manpage for <code>genisoimage</code>. </p>
<h2>AUTHORS</h2>
<p> Andy Polyakov &lt;appro [at] fy.chalmers.se&gt; stands for programming and on-line information. </p>
<p> This manpage is currently maintained by Huub Reuver &lt;h_reuver [at] mantell.xs4all.nl&gt;. </p>
<h2>LICENSE</h2>
<p> <code>growisofs</code> is distributed under GNU GPL. </p>
<h2>Index</h2>
