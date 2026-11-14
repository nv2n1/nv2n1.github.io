---
title: "vcdimager(1)"
name: "vcdimager"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vcdimager/"
description: "vcdimager – manual page for vcdimager 0.7.24"
---

<h2>NAME</h2>
<p> vcdimager &#8211; manual page for vcdimager 0.7.24</p>
<h2>SYNOPSIS</h2>
<p> <code>vcdimager</code> [<i>OPTION</i>&#8230;] <i>&lt;mpeg-tracks</i>&#8230;<i>&gt;</i></p>
<h2>DESCRIPTION</h2>
<dl>
<dt><code>-t</code>, <code>&#8211;type</code>=<i>TYPE</i></p>
<dd> select VideoCD type (&#8216;vcd11&#8217;, &#8216;vcd2&#8217;, &#8216;svcd&#8217; or &#8216;hqvcd&#8217;) (default: &#8216;vcd2&#8217;)</p>
<dt><code>-c</code>, <code>&#8211;cue-file</code>=<i>FILE</i></p>
<dd> specify cue file for output (default: &#8216;videocd.cue&#8217;)</p>
<dt><code>-b</code>, <code>&#8211;bin-file</code>=<i>FILE</i></p>
<dd> specify bin file for output (default: &#8216;videocd.bin&#8217;)</p>
<dt><code>-l</code>, <code>&#8211;iso-volume-label</code>=<i>LABEL</i></p>
<dd> specify ISO volume label for video cd (default: &#8216;VIDEOCD&#8217;)</p>
<dt><code>&#8211;iso-application-id</code>=<i>LABEL</i></p>
<dd> specify ISO application id for video cd (default: &#8221;)</p>
<dt><code>&#8211;info-album-id</code>=<i>LABEL</i></p>
<dd> specify album id for video cd set (default: &#8221;)</p>
<dt><code>&#8211;volume-count</code>=<i>NUMBER</i></p>
<dd> specify number of volumes in album set</p>
<dt><code>&#8211;volume-number</code>=<i>NUMBER</i></p>
<dd> specify album set sequence number (&lt; volume-count)</p>
<dt><code>&#8211;broken-svcd-mode</code></p>
<dd> enable non-compliant compatibility mode for broken devices</p>
<dt><code>&#8211;update-scan-offsets</code></p>
<dd> update scan data offsets in video mpeg2 stream</p>
<dt><code>&#8211;sector-2336</code></p>
<dd> use 2336 byte sectors for output</p>
<dt><code>&#8211;add-dir</code>=<i>ISO_DIRNAME</i></p>
<dd> add empty dir to ISO fs</p>
<dt><code>&#8211;add-file</code>=<i>FILE</i>,ISO_FILENAME</p>
<dd> add single file to ISO fs</p>
<dt><code>&#8211;add-file-2336</code>=<i>FILE</i>,ISO_FILENAME</p>
<dd> add file containing full 2336 byte sectors to ISO fs</p>
<dt><code>-T</code>, <code>&#8211;create-time</code>=<i>STRING</i></p>
<dd> specify creation date on files in CD image (default: current date)</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> be verbose</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> show only critical messages</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> display version and copyright information and exit</dl>
<h3>Help options:</h3>
<dl>
<dt>-?, <code>&#8211;help</code></p>
<dd> Show this help message</p>
<dt><code>&#8211;usage</code></p>
<dd> Display brief usage message</dl>
<h2>AUTHOR</h2>
<p> Written by Herbert Valerio Riedel and Rocky Bernstein. </p>
<p> <a rel="nofollow" href="http://www.gnu.org/software/vcdimager/">http://www.gnu.org/software/vcdimager/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2000-2003 Herbert Valerio Riedel &lt;hvr [at] gnu.org&gt;</p>
<dl>
<dt>
<dd> 2003 Rocky Bernstein &lt;rocky [at] panix.com&gt;</dl>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>vcdimager</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>vcdimager</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info vcdimager</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
