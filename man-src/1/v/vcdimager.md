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
<p> <code>vcdimager</code> [<i>OPTION</i>&#8230;] <i>&lt;mpeg-tracks</i>&#8230;<i>&gt;</i></p>
<dl>
<dt><code>-t</code>, <code>&#8211;type</code>=<i>TYPE</i></dt>
<dd> select VideoCD type (&#8216;vcd11&#8217;, &#8216;vcd2&#8217;, &#8216;svcd&#8217; or &#8216;hqvcd&#8217;) (default: &#8216;vcd2&#8217;)</dd>
<dt><code>-c</code>, <code>&#8211;cue-file</code>=<i>FILE</i></dt>
<dd> specify cue file for output (default: &#8216;videocd.cue&#8217;)</dd>
<dt><code>-b</code>, <code>&#8211;bin-file</code>=<i>FILE</i></dt>
<dd> specify bin file for output (default: &#8216;videocd.bin&#8217;)</dd>
<dt><code>-l</code>, <code>&#8211;iso-volume-label</code>=<i>LABEL</i></dt>
<dd> specify ISO volume label for video cd (default: &#8216;VIDEOCD&#8217;)</dd>
<dt><code>&#8211;iso-application-id</code>=<i>LABEL</i></dt>
<dd> specify ISO application id for video cd (default: &#8221;)</dd>
<dt><code>&#8211;info-album-id</code>=<i>LABEL</i></dt>
<dd> specify album id for video cd set (default: &#8221;)</dd>
<dt><code>&#8211;volume-count</code>=<i>NUMBER</i></dt>
<dd> specify number of volumes in album set</dd>
<dt><code>&#8211;volume-number</code>=<i>NUMBER</i></dt>
<dd> specify album set sequence number (&lt; volume-count)</dd>
<dt><code>&#8211;broken-svcd-mode</code></dt>
<dd> enable non-compliant compatibility mode for broken devices</dd>
<dt><code>&#8211;update-scan-offsets</code></dt>
<dd> update scan data offsets in video mpeg2 stream</dd>
<dt><code>&#8211;sector-2336</code></dt>
<dd> use 2336 byte sectors for output</dd>
<dt><code>&#8211;add-dir</code>=<i>ISO_DIRNAME</i></dt>
<dd> add empty dir to ISO fs</dd>
<dt><code>&#8211;add-file</code>=<i>FILE</i>,ISO_FILENAME</dt>
<dd> add single file to ISO fs</dd>
<dt><code>&#8211;add-file-2336</code>=<i>FILE</i>,ISO_FILENAME</dt>
<dd> add file containing full 2336 byte sectors to ISO fs</dd>
<dt><code>-T</code>, <code>&#8211;create-time</code>=<i>STRING</i></dt>
<dd> specify creation date on files in CD image (default: current date)</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> be verbose</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> show only critical messages</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> display version and copyright information and exit</dd></dl>
<h3>Help options:</h3>
<dl>
<dt>-?, <code>&#8211;help</code></dt>
<dd> Show this help message</dd>
<dt><code>&#8211;usage</code></dt>
<dd> Display brief usage message</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Herbert Valerio Riedel and Rocky Bernstein. </p>
<p> <a rel="nofollow" href="http://www.gnu.org/software/vcdimager/">http://www.gnu.org/software/vcdimager/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2000-2003 Herbert Valerio Riedel &lt;hvr [at] gnu.org&gt;</p>
<dl>
<dt>
</dt><dd> 2003 Rocky Bernstein &lt;rocky [at] panix.com&gt;</dd></dl>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>vcdimager</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>vcdimager</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info vcdimager</code></dd></dl>
<p> should give you access to the complete manual. </p>
