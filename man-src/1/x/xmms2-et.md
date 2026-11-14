---
title: "xmms2-et(1)"
name: "xmms2-et"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmms2-et/"
description: "xmms2-et – transmits an anonymous informative packet to the XMMS2 team on each song change"
---

<h2>NAME</h2>
<p> xmms2-et &#8211; transmits an anonymous informative packet to the XMMS2 team on each song change</p>
<h2>SYNOPSIS</h2>
<p> <i>xmms2-et</i></p>
<h2>DESCRIPTION</h2>
<p> <code>XMMS2 </code> is a redesign of the XMMS (<a rel="nofollow" href="http://www.xmms.org)">http://www.xmms.org)</a> music player. It features a client-server model, allowing multiple (even simultaneous!) user interfaces, both textual and graphical. All common audio formats are supported using plugins. On top of this, there is a flexible media library to organize your music. </p>
<p> <i>xmms2-et</i> is the ET Phone Home Client for <code>XMMS2.</code> <i>xmms2-et </i> is designed to transmit a packet of information to the <code>XMMS2</code> team whenever a new song is played. The packet is anonymous and does not contain metadata about the song being played. The specifics of what data is transmitted to the <code>XMMS2</code> team can be found in the <code>ET PACKET</code> section of this manual page. <i>xmms2-et</i> is used for release engineering by the <code>XMMS2</code> team. During a release cycle, the usage of various plugins, operating systems, and XMMS2 components is collected from data transmitted by the <i>xmms2-et</i> client. A release is made when sufficient testing has occured as determined by the number of related <i>xmms2-et</i> packets that the <code>XMMS2</code> team has received.</p>
<h2>ET PACKET</h2>
<p> The following data is transmitted with every packet transmitted by <i>xmms2-et:</i></p>
<dl>
<dt><i>XMMS2-ET status</i></p>
<dd> Begins XMMS2-ET packets; <i>status</i> gives a descriptive message denoting what this packet is about. (e.g. Clean shutdown, Unclean shutdown, New media)</p>
<dt><i>version=version</i></p>
<dd> contains the version of the <code>XMMS2</code> daemon</p>
<dt><i>system=os</i></p>
<dd> contains the name and release of the operating system on which <i>xmms2d</i> is running</p>
<dt><i>output=output_plugin </i></p>
<dd> contains the output plugin being used to playback audio by <i>xmms2d</i></p>
<dt><i>starttime=start_time</i></p>
<dd> contains the time at which the <i>xmms2-et</i> client was started</p>
<dt><i>uptime=xmms2d_uptime</i></p>
<dd> contains the uptime of the <i>xmms2-et</i> client</p>
<dt><i>playlistloads=times</i></p>
<dd> contains the number of times a playlist has been loaded from the Media Library</p>
<dt><i>mlibresolves=times</i></p>
<dd> contains the number of times that metadata has been resolved for media in the Media Library</dl>
<p> The following data is different for each song being played:</p>
<dl>
<dt><i>decoder=plugin</i></p>
<dd> contains the decoder plugin used to playback the last played song</p>
<dt><i>transport=plugin</i></p>
<dd> contains the transport plugin used to read the last played song</p>
<dt><i>samplefmt:in=in_fmt</i></p>
<dd> contains the sample format of the original audio file of the last played song</p>
<dt><i>samplefmt:out=out_fmt</i></p>
<dd> contains the sample format that was sent to the output plugin for the last played song</p>
<dt><i>samplerate:in=in_rate</i></p>
<dd> contains the sample rate of the original audio file of the last played song</p>
<dt><i>samplerate:out=out_rate</i></p>
<dd> contains the sample rate that was sent to the output plugin for the last played song</p>
<dt><i>channels:in=number_in</i></p>
<dd> contains the number of channels of the original audio file of the last played song</p>
<dt><i>channels:out=number_out</i></p>
<dd> contains the number of channels that were sent to the output plugin for the last played song</dl>
<h2>ENVIRONMENTAL VARIABLES</h2>
<dl>
<dt><i>XMMS_PATH</i></p>
<dd> The URL path to <i>xmms2d.</i> See <code>IPC SOCKET</code> in <i><a href="/docs/linux/man/8-xmms2d/">xmms2d</a>(8)</i> for details of possible values for this variable </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xmms2/">xmms2</a>(1), <a href="/docs/linux/man/8-xmms2d/">xmms2d</a>(8), <a rel="nofollow" href="http://xmms2.xmms.org">http://xmms2.xmms.org</a></p>
<h2>HISTORY</h2>
<p> The <code>XMMS2</code> Project was started by Tobias Rundström and Anders Gustafsson. It is developed with their lead by a small group of contributers from all over the world.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Alexander Botero-Lowry &lt;alex [at] foxybanana.com&gt; </p>
<h2>Index</h2>
