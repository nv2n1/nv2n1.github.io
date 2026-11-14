---
title: "alsaloop(1)"
name: "alsaloop"
section: "1"
letter: "a"
url: "/docs/linux/man/1-alsaloop/"
description: "alsaloop – command-line PCM loopback"
---

<h2 class="name">NAME</h2>
<p> alsaloop &#8211; command-line PCM loopback </p>
<h2>SYNOPSIS</h2>
<p> <code>alsaloop</code> [<i>-option</i>] [<i>cmd</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>alsaloop</code> allows create a PCM loopback between a PCM capture device and a PCM playback device. </p>
<p> <code>alsaloop</code> supports multiple soundcards, adaptive clock synchronization, adaptive rate resampling using the samplerate library (if available in the system). Also, mixer controls can be redirected from one card to another (for example Master and PCM). </p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-h</i> | <i>&#8211;help</i></p>
<dd>
<p> Prints the help information. </p>
<dt><i>-g &lt;file&gt;</i> | <i>&#8211;config=&lt;file&gt;</i></p>
<dd>
<p> Use given configuration file. The syntax of this file is simple: one line contains the command line options for one job. The &#8216;#&#8217; means comment and rest of line is ignored. Example: </p>
<p>&nbsp;<wbr>&nbsp;#&nbsp;First line &#8211; comment, second line &#8211; first job<br />
&nbsp;<wbr>&nbsp;-C hw:1,0 -P hw:0,0 -t 50000 -T 1<br />
&nbsp;<wbr>&nbsp;#&nbsp;Third line &#8211; comment, fourth line &#8211; second job<br />
&nbsp;<wbr>&nbsp;-C hw:1,1 -P hw:0,1 -t 40000 -T 2 </p>
<dt><i>-d</i> | <i>&#8211;daemonize</i></p>
<dd>
<p> Daemonize the main process and use syslog for messages. </p>
<dt><i>-P &lt;device&gt;</i> | <i>&#8211;pdevice=&lt;device&gt;</i></p>
<dd>
<p> Use given playback device. </p>
<dt><i>-C &lt;device&gt;</i> | <i>&#8211;cdevice=&lt;device&gt;</i></p>
<dd>
<p> Use given capture device. </p>
<dt><i>-X &lt;device&gt;</i> | <i>&#8211;pctl=&lt;device&gt;</i></p>
<dd>
<p> Use given CTL device for playback. </p>
<dt><i>-Y &lt;device&gt;</i> | <i>&#8211;cctl=&lt;device&gt;</i></p>
<dd>
<p> Use given CTL device for capture. </p>
<dt><i>-x &lt;ctl_ascii_name&gt;</i> | <i>&#8211;prateshift=&lt;ctl_ascii_name&gt;</i></p>
<dd>
<p> Specify ctl ascii name for playshift sync mode (see the Examples section). </p>
<dt><i>-l &lt;latency&gt;</i> | <i>&#8211;latency=&lt;frames&gt;</i></p>
<dd>
<p> Requested latency in frames. </p>
<dt><i>-t &lt;usec&gt;</i> | <i>&#8211;tlatency=&lt;usec&gt;</i></p>
<dd>
<p> Requested latency in usec (1/1000000sec). </p>
<dt><i>-f &lt;format&gt;</i> | <i>&#8211;format=&lt;format&gt;</i></p>
<dd>
<p> Format specification (usually S16_LE S32_LE). Use -h to list all formats. Default format is S16_LE. </p>
<dt><i>-c &lt;channels&gt;</i> | <i>&#8211;channels=&lt;channels&gt;</i></p>
<dd>
<p> Channel count specification. Default value is 2. </p>
<dt><i>-r &lt;rate&gt;</i> | <i>&#8211;rate=&lt;rate&gt;</i></p>
<dd>
<p> Rate specification. Default value is 48000 (Hz). </p>
<dt><i>-n</i> | <i>&#8211;resample</i></p>
<dd>
<p> Allow rate resampling using alsa-lib. </p>
<dt><i>-A &lt;converter&gt;</i> | <i>&#8211;samplerate=&lt;converter&gt;</i></p>
<dd>
<p> Use libsamplerate and choose a converter: </p>
<p>&nbsp;<wbr>&nbsp;0 or sincbest&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; best quality<br />
&nbsp;<wbr>&nbsp;1 or sincmedium&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; medium quality<br />
&nbsp;<wbr>&nbsp;2 or sincfastest&nbsp;<wbr>&nbsp;&#8211; lowest quality<br />
&nbsp;<wbr>&nbsp;3 or zerohold&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; hold zero samples<br />
&nbsp;<wbr>&nbsp;4 or linear&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; worst quality &#8211; linear resampling<br />
&nbsp;<wbr>&nbsp;5 or auto&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; choose best method </p>
<dt><i>-B &lt;size&gt;</i> | <i>&#8211;buffer=&lt;size&gt;</i></p>
<dd>
<p> Buffer size in frames. </p>
<dt><i>-E &lt;size&gt;</i> | <i>&#8211;period=&lt;size&gt;</i></p>
<dd>
<p> Period size in frames. </p>
<dt><i>-s &lt;secs&gt;</i> | <i>&#8211;seconds=&lt;secs&gt;</i></p>
<dd>
<p> Duration of loop in seconds. </p>
<dt><i>-b</i> | <i>&#8211;nblock</i></p>
<dd>
<p> Non-block mode (very early process wakeup). Eats more CPU. </p>
<dt><i>-S &lt;mode&gt;</i> | <i>&#8211;sync=&lt;mode&gt;</i></p>
<dd>
<p> Sync mode specification for capture to playback stream:<br />
&nbsp;<wbr>&nbsp;0 or none&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; do not touch the stream<br />
&nbsp;<wbr>&nbsp;1 or simple&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; add or remove samples to keep<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;both streams synchronized<br />
&nbsp;<wbr>&nbsp;2 or captshift&nbsp;<wbr>&nbsp;&#8211; use driver for the capture device<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(if supported)&nbsp;to compensate<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the rate shift<br />
&nbsp;<wbr>&nbsp;3 or playshift&nbsp;<wbr>&nbsp;&#8211; use driver for the playback device<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(if supported)&nbsp;to compensate<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the rate shift<br />
&nbsp;<wbr>&nbsp;4 or samplerate &#8211; use samplerate library to do rate resampling<br />
&nbsp;<wbr>&nbsp;5 or auto&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; automatically selects the best method<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in this order: captshift, playshift,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;samplerate, simple </p>
<dt><i>-T &lt;num&gt;</i> | <i>&#8211;thread=&lt;num&gt;</i></p>
<dd>
<p> Thread number (-1 means create a unique thread). All jobs with same thread numbers are run within one thread. </p>
<dt><i>-m &lt;mixid&gt;</i> | <i>&#8211;mixer=&lt;midid&gt;</i></p>
<dd>
<p> Redirect mixer control from the playback card to the capture card. Format of <i>mixid</i> is SRCID(PLAYBACK)[@DSTID(PLAYBACK)]: </p>
<p>&nbsp;<wbr>&nbsp;&quot;name=&#8217;Master Playback Switch&#8217;@name=&#8217;Another Switch&#8217;&quot;<br />
&nbsp;<wbr>&nbsp;&quot;name=&#8217;PCM Playback Volume&#8217;&quot; </p>
<p> Known attributes: </p>
<p>&nbsp;<wbr>&nbsp;name&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; control ID name<br />
&nbsp;<wbr>&nbsp;index&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; control ID index<br />
&nbsp;<wbr>&nbsp;device&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; control ID device<br />
&nbsp;<wbr>&nbsp;subdevice &#8211; control ID subdevice<br />
&nbsp;<wbr>&nbsp;iface&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; control ID interface<br />
&nbsp;<wbr>&nbsp;numid&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; control ID numid </p>
<dt><i>-O &lt;ossmixid&gt;</i> | <i>&#8211;ossmixer=&lt;midid&gt;</i></p>
<dd>
<p> Redirect mixer control from the OSS Mixer emulation layer (capture card) to the ALSA layer (capture card). Format of <i>ossmixid</i> is ALSAID[,INDEX]@OSSID: </p>
<p>&nbsp;<wbr>&nbsp;&quot;Master [at] VOLUME&quot;<br />
&nbsp;<wbr>&nbsp;&quot;PCM,1@ALTPCM&quot; </p>
<p> Known OSS attributes: </p>
<p>&nbsp;<wbr>&nbsp;VOLUME, BASS, TREBLE, SYNTH, PCM, SPEAKER, LINE, MIC, CD, IMIX, ALTPCM,<br />
&nbsp;<wbr>&nbsp;RECLEV, IGAIN, OGAIN, LINE1, LINE2, LINE3, DIGITAL1, DIGITAL2, DIGITAL3,<br />
&nbsp;<wbr>&nbsp;PHONEIN, PHONEOUT, VIDEO, RADIO, MONITOR </p>
<dt><i>-v</i> | <i>&#8211;verbose</i></p>
<dd>
<p> Verbose mode. Use multiple times to increase verbosity. </p>
<dt><i>-U</i> | <i>&#8211;xrun</i></p>
<dd>
<p> Verbose xrun profiling. </p>
<dt><i>-W &lt;timeout&gt;</i> | <i>&#8211;wake=&lt;timeout&gt;</i></p>
<dd>
<p> Set process wake timeout. </p>
</dl>
<h2>EXAMPLES</h2>
<pre>
<code>alsaloop -C hw:0,0 -P hw:1,0 -t 50000</code>
<code>alsaloop -C hw:soundcard,0 -P hw:Loopback,0 -t 50000 -S playshift \
-x iface=PCM,name='PCM Rate Shift 100000',device=1</code>
</pre>
<h2>BUGS</h2>
<p> None known.</p>
<h2>AUTHOR</h2>
<p> <code>alsaloop</code> is by Jaroslav Kysela &lt;perex [at] perex.cz&gt;. This document is by Jaroslav Kysela &lt;perex [at] perex.cz&gt;. </p>
<h2>Index</h2>
