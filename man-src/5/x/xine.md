---
title: "xine(5)"
name: "xine"
section: "5"
letter: "x"
url: "/docs/linux/man/5-xine/"
description: "xine – a free video player"
---

<p>xine &#8211; a free video player</p>
<h2>MRL (media resource locator)</h2>
<p>MRLs are similar to URLs in your web browser. They describe the media to read from. Valid MRLs may be plain file names or one of the following (see also the notes below):</p>
<dl>
<dt>&bull; Filesystem:</dt>
<dd><code>file:</code><i>&lt;path&gt;</i><br />
 <code>fifo:</code><i>&lt;path&gt;</i><br />
 <code>stdin:/</code></dd></dl>
<dl>
<dt>&bull; CD and DVD:</dt>
<dd><code>dvd:/[</code><i>device_name</i><code>][/</code><i>title</i><code>[.</code><i>part</i><code>]]</code><br />
 <code>dvd:/</code><i>DVD_image_file</i><code>[/</code><i>title</i><code>[.</code><i>part</i><code>]]</code><br />
 <code>dvd:/</code><i>DVD_directory</i><code>[/</code><i>title</i><code>[.</code><i>part</i><code>]]</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>(use the path of the directory which contains VIDEO_TS)</dd>
<p> <code><a href="vcd://[">vcd://[</a></code><i>CD_image_or_device_name</i><code>][@[</code><i>letter</i><code>]</code><i>number</i><code>]</code><br />
 <code>vcdo://</code><i>track_number</i><br />
 <code>cdda:/[</code><i>device</i><code>][/</code><i>track_number</i><code>]</code></dl>
<dl>
<dt>&bull; Video devices:</dt>
<dd><code>v4l://[</code><i>tuner_device</i><code>/</code><i>frequency</i><code>]</code><br />
 <code>v4l2://</code><i>tuner_device</i><br />
 <code>dvb://</code><i>channel_number</i><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>(nth channel in your channels.conf)</dd>
<p> <code>dvb://</code><i>channel_name</i><br />
 <code>dvbc://</code><i>channel_name</i><code>:</code><i>tuning_parameters</i><br />
 <code>dvbs://</code><i>channel_name</i><code>:</code><i>tuning_parameters</i><br />
 <code>dvbt://</code><i>channel_name</i><code>:</code><i>tuning_parameters</i><br />
 <code>dvba://</code><i>channel_name</i><code>:</code><i>tuning_parameters</i><br />
 <code>pvr:/</code><i>tmp_files_path</i><code>!</code><i>saved_files_path</i><code>!</code><i>max_page_age</i><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>(for WinTV PVR 250 and 350)
</dl>
<dl>
<dt>&bull; Network:</dt>
<dd><code>http://</code><i>host&#8230;</i><br />
 <code>tcp://</code><i>host</i><code>[:</code><i>port</i><code>]</code><br />
 <code>udp://</code><i>host</i><code>[:</code><i>port</i><code>[?iface=</code><i>interface</i><code>]]</code><br />
 <code>rtp://</code><i>host</i><code>[:</code><i>port</i><code>[?iface=</code><i>interface</i><code>]]</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>(default port for tcp, udp and rtp is 7658)</dd>
<p> <code><a href="smb://...">smb://&#8230;</a></code><br />
 <code>mms://</code><i>host&#8230;</i><br />
 <code>pnm://</code><i>host&#8230;</i><br />
 <code>rtsp://</code><i>host&#8230;</i> (requires Real codecs)
</dl>
<p> Additional input plugins will provide additional MRL types. The ones listed above are available with stock libxine. </p>
<p> <code>NOTE:</code> where a file name is required, the <i>full path must be provided</i> &#8211; from a shell, you can normally use <code>&quot;$PWD/file&quot;</code> or <code>&quot;$(pwd)/file&quot;</code> or <code>&quot;`pwd`/file&quot;</code> if the file is in the current directory. (Which one depends on your shell; all three work in bash. Also, normal URL encoding rules apply; `%&#8217;, in particular, must be encoded as `%25&#8242;.) </p>
<p> As of xine-lib 1.1.3, the DVD title number may be 0 (select navigation) and the chapter number may be 0 (full title).</p>
<h3>VCD MRL Syntax</h3>
<p>A simple <code>vcd:/</code> runs the default item (e.g. perhaps track 1 or entry 0) using the default VCD device (perhaps /dev/cdrom). Both the default item and default device are user-configurable. </p>
<p> It is however also possible to specify both Video CD device/filename and item explicitly in the MRL. </p>
<p> For example <code>vcd:/dev/dvd</code> specifies the default entry using device /dev/dvd which might useful if this is your DVD which is different than your CD-ROM device and your DVD drive can play CD&#8217;s. And <code><a href="vcd://test_svcd_ntsc.cue">vcd://test_svcd_ntsc.cue</a></code> specifies the cue file for CD image on disk. (test_svcd_ntsc.bin is the corresponding bin file, but using that won&#8217;t work.) </p>
<p> After the optional device name or file name, you can name the kind of unit, preceded by a colon. An MRL which ends in a colon is like not adding it at all: the default entry type and number is used. Items come in 4 flavours: &quot;<code>Track</code>&quot;, &quot;<code>Entry</code>&quot;, &quot;<code>Playback</code>&quot; and &quot;<code>Segment</code>&quot;. These units are indicated with the capital first letter of each type: <code>T</code>, <code>E</code>, <code>P</code>, <code>S</code>, <code>s</code>. An uppercase <code>S</code> in the MRL display indicates a NTSC segment while a lowercase <code>s</code> indicates a PAL segment. However, when you enter an MRL, the case of these letters is insignificant. </p>
<p> Depending on the Video CD, you might not have any playable segments (<code>S</code>,<code>s</code>) or playback control (<code>P</code>). If you give a MRL that refers to a playback control entry but there is no playback control, your playback number will silently be converted into the corresponding entry number. </p>
<p> You can configure various things that affect MRLs are selected when there is some ambiguity in the MRL name. <i>media.vcd.autoplay</i> sets what kind of unit to to use in a MRL is none is given. Another configuration setting, <i>vcd.device</i>, determines what device to use if that part is not given. When you hit the VCD button, that is equivalent to entering <code>vcd:/</code> and thus these two configuration settings are used to expand the MRL. </p>
<p> Some examples of MRLs are given below. In the examples, we assume the following configuration settings: </p>
<dl>
<dt><code>vcd://</code></dt>
<dd>Play (navigate) default item (in this case Entry ID 0) from the default device (in this case set to /dev/cdrom)</dd>
<dt><code><a href="vcd://@">vcd://@</a></code></dt>
<dd>Same as above</dd>
<dt><code><a href="vcd:///dev/cdrom@">vcd:///dev/cdrom@</a></code></dt>
<dd>Same effect as above since the default device is set to /dev/cdrom.</dd>
<dt><code><a href="vcd:///dev/cdrom@E0">vcd:///dev/cdrom@E0</a></code></dt>
<dd>Same as above. But note that this is because we have autoplay:entry which is no longer the default value.</dd>
<dt><code><a href="vcd:///dev/cdrom2@">vcd:///dev/cdrom2@</a></code></dt>
<dd>Play (navigate) the default item of /dev/cdrom2</dd>
<dt><code><a href="vcd:///dev/cdrom2">vcd:///dev/cdrom2</a></code></dt>
<dd>should be same as above but is currently broken?</dd>
<dt><code><a href="vcd:///dev/cdrom2@T1">vcd:///dev/cdrom2@T1</a></code></dt>
<dd>Play Track 1 from /dev/cdrom2</dd>
<dt><code><a href="vcd:///dev/cdrom@S1">vcd:///dev/cdrom@S1</a></code></dt>
<dd>Play segment 1 from /dev/cdrom. This assumes that there *is* a segment 1. Check the MRL list to see if that is the case.</dd>
<dt><code><a href="vcd://@P1">vcd://@P1</a></code></dt>
<dd>Play playlist item 1 from default device. If there is no playback control, the MRL will be converted into vcd:/@E0. Again check the MRL list to see if there is a P1.</dd>
<dt><code><a href="vcd://@P1*">vcd://@P1*</a></code></dt>
<dd>Probably same as above.</dd>
<dt><code><a href="vcd:///dev/cdrom@E1">vcd:///dev/cdrom@E1</a></code></dt>
<dd>Play Entry id 1 from default device.</dd>
<dt><code><a href="vcd://@S0">vcd://@S0</a></code></dt>
<dd>Play segment 0 from default device.</dd>
<dt><code><a href="vcd://@3">vcd://@3</a></code></dt>
<dd>Play track 3 from default device.</dd>
<dt><code><a href="vcd:///dev/cdrom2:1">vcd:///dev/cdrom2:1</a></code></dt>
<dd>Play track 1 from /dev/cdrom2.</dd>
<dt><code><a href="vcd:///tmp/ntsc.cue@">vcd:///tmp/ntsc.cue@</a></code></dt>
<dd>Play default item (E0) of /tmp/ntsc.bin. Note trailing <code>@</code>.</dd>
<dt><code><a href="vcd://ntsc.cue/@E0">vcd://ntsc.cue/@E0</a></code></dt>
<dd>Play entry 0 of ntsc.bin.</dd>
<dt><code><a href="vcd:///tmp/ntsc.nrg/@E0">vcd:///tmp/ntsc.nrg/@E0</a></code></dt>
<dd>Play entry 0 of /tmp/ntsc.nrg (Nero file). Works for some simple Nero images.
</dd></dl>
<h3>Dvb</h3>
<p>DVB MRLs require that xine-lib/channels.conf exists in $XDG_CONFIG_HOME/ or ~/.config/ and contains valid data. This can be obtained by generating a tuning file using the LinuxTV DVB apps utility &quot;scan&quot; (or &quot;dvbscan&quot; if you&#8217;re using a version newer than 1.1.0): </p>
<p> <code>scan -o zap /usr/share/doc/dvb-utils/examples/scan/dvb-t/uk-PontopPike &gt;~/.config/xine-lib/channels.conf</code> </p>
<p> (This example is for the writer&#8217;s local transmitter, using a file from the Debian dvb-utils package.) </p>
<p> For the dvbc, dvbs and dvbt MRLs, tuning parameters are expected, taking one of the following forms:</p>
<dl>
<dt><code>DVB-S</code></dt>
<dd>&lt;frequency&gt;:&lt;polarisation&gt;:&lt;sat-no&gt;:&lt;sym-rate&gt;:&lt;vpid&gt;:&lt;apid&gt;:&lt;service-id&gt;</dd>
<dt><code>DVB-C</code></dt>
<dd>&lt;frequency&gt;:&lt;inversion&gt;:&lt;sym-rate&gt;:&lt;fec&gt;:&lt;qam&gt;:&lt;vpid&gt;:&lt;apid&gt;:&lt;service-id&gt;</dd>
<dt><code>DVB-T</code></dt>
<dd>&lt;frequency&gt;:&lt;inversion&gt;:&lt;bw&gt;:&lt;fec-hp&gt;:&lt;fec-lp&gt;:&lt;qam&gt;:&lt;transmission-mode&gt;:&lt;guardlist&gt;:&lt;hierarchy-info&gt;:&lt;vpid&gt;:&lt;apid&gt;:&lt;service-id&gt;</dd>
<dt><code>DVB-A</code></dt>
<dd>&lt;frequency&gt;:&lt;qam&gt;:&lt;vpid&gt;:&lt;apid&gt;:&lt;service-id&gt;</dd></dl>
<p> The individual parameters are:</p>
<dl>
<dt><code>frequency</code></dt>
<dd>number, usually in kHz</dd>
<dt><code>polarisation</code></dt>
<dd>`v&#8217; or `h&#8217;</dd>
<dt><code>sat-no</code></dt>
<dd>unsigned long, usually 0</dd>
<dt><code>sym-rate</code></dt>
<dd>symbol rate in MSyms/sec</dd>
<dt><code>inversion</code></dt>
<dd>INVERSION_ON, INVERSION_OFF, INVERSION_AUTO</dd>
<dt><code>fec, fec-hp, fec-lp</code></dt>
<dd>FEC_1_2, FEC_2_3, FEC_3_4 &#8230; FEC_8_9, FEC_AUTO, FEC_NONE</dd>
<dt><code>qam</code></dt>
<dd>QPSK, QAM_128, QAM_16 &#8230;</dd>
<dt><code>bw</code></dt>
<dd>BANDWIDTH_6_MHZ, BANDWIDTH_7_MHZ, BANDWIDTH_8_MHZ</dd>
<dt><code>transmission-mode</code></dt>
<dd>TRANSMISSION_MODE_2K, TRANSMISSION_MODE_8K</dd>
<dt><code>guardlist</code></dt>
<dd>GUARD_INTERVAL_1_4, GUARD_INTERVAL_1_8, GUARD_INTERVAL_1_16, GUARD_INTERVAL_1_32,</dd>
<dt><code>hierarchy-info</code></dt>
<dd>HIERARCHY_1, HIERARCHY_2, HIERARCHY_4, HIERARCHY_NONE</dd>
<dt><code>vpid</code></dt>
<dd>video program ID</dd>
<dt><code>apid</code></dt>
<dd>audio program ID</dd>
<dt><code>service-id</code></dt>
<dd>service ID (needed for now/next information etc.)</dd></dl>
<p> The following keyboard &amp; mouse inputs may be accepted:</p>
<dl>
<dt><code>Menu 2</code></dt>
<dd>Start/stop recording</dd>
<dt><code>Menu 3</code></dt>
<dd>Toggle zoom</dd>
<dt><code>Menu 7</code></dt>
<dd>Toggle now/next display</dd>
<dt><code>Previous/Next Chapter</code></dt>
<dd>Previous/next channel</dd>
<dt><code>Mouse wheel &amp; button 1</code></dt>
<dd>Scroll through channel list &amp; select the highlighted channel</dd></dl>
<h2>Subtitle</h2>
<p><code>external subtitle files (any mrl)</code><br />
 Text subtitle files may be appended to the MRL:.</p>
<dl>
<dt><code>&lt;mrl&gt;#subtitle:&lt;subtitlefile&gt;</code></dt>
<dd>This is the normal way to define the subtitle file to use. The frontend will not take any notice of the subtitle file. For example:<br />
 <i>file://home/user/wibble.mpg#subtitle:/home/user/wibble.sub</i><br />
 (Note that some front ends can detect subtitles files where the name differs as shown in the example.)
</dd></dl>
<h2>Stream Options</h2>
<p>After a delimiting <code>#</code> you can add several stream parameters:</p>
<dl>
<dt><code>novideo</code></dt>
<dd>Video will be ignored.</dd>
<dt><code>noaudio</code></dt>
<dd>Audio will be ignored.</dd>
<dt><code>nospu</code></dt>
<dd>Subpictures will be ignored.</dd>
<dt><code>demux:</code><i>&lt;demux name&gt;</i></dt>
<dd>Specify the demux plugin to use.</dd>
<dt><code>volume:</code><i>&lt;level&gt;</i></dt>
<dd>Set audio volume.</dd>
<dt><code>compression:</code><i>&lt;level&gt;</i></dt>
<dd>Set audio dynamic range compression.</dd>
<dt><code>&lt;config entry&gt;</code><i>:</i><code>&lt;config value&gt;</code></dt>
<dd>Assign a new value to any config entry.</dd>
<dt><code>save:</code><i>&lt;file&gt;</i></dt>
<dd>Save the stream (if allowed) to the named file, relative to the directory given by the option &quot;media.capture.save_dir&quot;.</dd>
<dt><code>change configuration option &#8216;on the fly&#8217;:</code></dt>
<dd>You can change a configuration option at any time, using the special <code>cfg:/</code> MRL style. The syntax is:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cfg:/&lt;config entry&gt; : &lt;config value&gt;</dd>
<p> Unlike stream config option, you can change anything <i>before</i> playing the stream. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-xine/">xine</a></code>(1), <code><a href="/docs/linux/man/1-aaxine/">aaxine</a></code>(1), <code><a href="/docs/linux/man/1-gxine/">gxine</a></code>(1), <code>toxine</code>(1), <code><a href="/docs/linux/man/1-totem/">totem</a></code>(1), <code>kaffeine</code>(1) &#8230; </p>
<p> The programs are documented fully on the xine home page: <i><a rel="nofollow" href="http://www.xine-project.org/">http://www.xine-project.org/</a></i></p>
<h2>Author</h2>
<p>This text was extracted from the xine man page by Darren Salt &lt;dsalt [at] users.sourceforge.net&gt;. The xine man page was written by Siggi Langauf &lt;siggi [at] debian.org&gt; for the xine project. Lots of additions by Guenter Bartsch &lt;guenter [at] users.sourceforge.net&gt;, Daniel Caujolle-Bert &lt;f1rmb [at] users.sourceforge.net&gt;, Rocky Bernstein &lt;rocky [at] panix.com&gt;, and Philipp Hahn &lt;pmhahn [at] users.sourceforge.net&gt;.</p>
