---
title: "cdrwtool(1)"
name: "cdrwtool"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cdrwtool/"
description: "cdrwtool – perform various actions on a CD-R, CD-RW, and DVD-R"
---

<h2 class="name">NAME</h2>
<p> cdrwtool &#8211; perform various actions on a CD-R, CD-RW, and DVD-R</p>
<h2>SYNOPSIS</h2>
<p> <code>cdrwtool -d </code><i>device</i><code> -i | -g</code> </p>
<p> <code>cdrwtool -d </code><i>device</i><code> -s [ </code><i>write-parameters</i><code> ]</code> </p>
<p> <code>cdrwtool -d </code><i>device</i><code> -q [ </code><i>write-parameters</i><code> ]</code> </p>
<p> <code>cdrwtool -d </code><i>device</i><code> -m </code><i>offset</i><code> [ </code><i>write-parameters</i><code> ]</code> </p>
<p> <code>cdwrtool -d </code><i>device</i><code> -u </code><i>blocks</i><code> [ </code><i>write-parameters</i><code> ]</code> </p>
<p> <code>cdrwtool -d </code><i>device</i><code> -b </code><i>b_mode</i><code> [ </code><i>write-parameters</i><code> ]</code> </p>
<p> <code>cdrwtool -d </code><i>device</i><code> -c </code><i>blocks</i><code> [ </code><i>write-parameters</i><code> ]</code> </p>
<p> <code>cdwrtool -d </code><i>device</i><code> -f </code><i>filename</i><code> [ </code><i>write-parameters</i><code> ]</code> </p>
<p> <code>cdwrtool -d </code><i>device</i><code> -r </code><i>track</i><code> [ </code><i>write-parameters</i><code> ]</code> </p>
<p> <code>cdrwtool -h</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>cdwrtool</code> command can perform certain actions on a CD-R, CD-RW, or DVD-R device. Mainly these are blanking the media, formating it for use with the packet-cd device, and applying an UDF filesystem. </p>
<p> The most common usage is probably the `quick setup&#8217; option:</p>
<dl>
<dt>
</dt><dd> <code>cdrwtool -d </code><i>device</i><code> -q</code></dd></dl>
<p> which will blank the disc, format it as one large track, and write the UDF filesystem structures. </p>
<p> Other options get and set various parameters of how the device is set up, and provide for different offsets, modes and settings from the defaults. </p>
<p> The usefulness of most of the options is not explained. </p>
<h2>OPTIONS</h2>
<p> Main directives:</p>
<dl>
<dt><code>-d </code><i>device</i></dt>
<dd> Specify the device to use. eg. <i>/dev/sr0</i> </dd>
<dt><code>-i</code></dt>
<dd> Print disc track info. </dd>
<dt><code>-g</code></dt>
<dd> Print write parameters. </dd>
<dt><code>-u </code><i>length</i></dt>
<dd> Make a UDF filesystem using <i>length</i> number of blocks. </dd>
<dt><code>-m </code><i>offset</i></dt>
<dd> Format the disc at <i>offset</i> number of blocks. </dd>
<dt><code>-b </code><i>mode</i></dt>
<dd> Blank the disk using a <i>mode</i> of `full&#8217; or `fast&#8217;. </dd>
<dt><code>-f </code><i>filename</i></dt>
<dd> Write file. </dd>
<dt><code>-c </code><i>track</i></dt>
<dd> Close track.</dd>
<dt><code>-r </code><i>track</i></dt>
<dd> Reserve track. </dd>
<dt><code>-z </code><i>length</i></dt>
<dd> Fixed packet length. </dd>
<dt><code>-s</code></dt>
<dd> Set write parameters determined by <code>-l</code>,<code> -w</code>, and<code> -p</code> options for the disc. </dd>
<dt><code>-v </code><i>version</i></dt>
<dd> Specify the udf revision to use. Valid revisions are 0x0201, 0x0200, 0x0150, and 0x0102. If omitted, <code>mkudffs</code> udf-version is 0x0150. </dd>
<dt><code>-h</code></dt>
<dd> Prints a sparse help message.</dd></dl>
<p> Write parameters:</p>
<dl>
<dt><code>-t </code><i>speed</i></dt>
<dd> Set write speed. (Defaults to 12x ?)</dd>
<dt><code>-l </code><i>type</i></dt>
<dd> Set multi-session field. Either `0&#8242;, `1&#8242;, or `3&#8242;, corresponding to `No B0 pointer. Next Session not allowed&#8217;, `B0 pointer = FF:FF:FF. Next session not allowed&#8217;, and `Next session allowed. B0 pointer = next possible program area&#8217; respectively.</dd>
<dt><code>-w </code><i>mode</i></dt>
<dd> Set write mode. Either `mode1&#8242; or `mode2&#8242;.</dd>
<dt><code>-p </code><i>type</i></dt>
<dd> Set packet type. Either `0&#8242; or `1&#8242;, corresponding to variable and fixed packet sizes respectively.</dd>
<dt><code>-o </code><i>offset</i></dt>
<dd> Set write offset. </dd>
</dl>
<h2>AUTHORS</h2>
<pre><code>
Jens Axboe&lt;axboe[at] suse.de&gt;
    Ben Fennema&lt;bfennema[at] falcon.csc.calpoly.edu&gt;
</code></pre>
<h2>AVAILABILITY</h2>
<p> <code>cdrwtool</code> is part of the udftools package and is available from <a rel="nofollow" href="http://linux-udf.sourceforge.net.">http://linux-udf.sourceforge.net.</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-pktsetup/">pktsetup</a></code>(8) </p>
<h2>Index</h2>
