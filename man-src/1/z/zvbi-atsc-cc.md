---
title: "zvbi-atsc-cc(1)"
name: "zvbi-atsc-cc"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zvbi-atsc-cc/"
description: "zvbi-atsc-cc – ATSC Closed Caption decoder"
---

<h2>NAME</h2>
<p> zvbi-atsc-cc &#8211; ATSC Closed Caption decoder</p>
<h2>SYNOPSIS</h2>
<p> <code>zvbi-atsc-cc [ options ] [-n] station name</code></p>
<h2>DESCRIPTION</h2>
<p> <code>zvbi-atsc-cc</code> captures ATSC TV transmissions using a Linux DVB device and decodes the enclosed Closed Caption data. It can record both NTSC caption (EIA 608-B) and DTVCC caption (CEA 708-C).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?</code> <code>-h</code> <code>&#8211;help</code> <code>&#8211;usage</code></p>
<dd> Print a short usage message.</p>
<dt><code>-q</code> <code>&#8211;quiet</code></p>
<dd> Suppress all progress and error messages.</p>
<dt><code>-v</code> <code>&#8211;verbose</code></p>
<dd> Increase verbosity.</dl>
<h3>Device options</h3>
<dl>
<dt><code>-a</code> number</p>
<dd>
<dt><code>&#8211;adapter-num</code> number</p>
<dd> Select a different DVB device to capture the signal (/dev/dvb/adapterN). The default is adapter 0.</p>
<dt><code>-i</code> number</p>
<dd>
<dt><code>&#8211;frontend-id</code> number</p>
<dd> Select a different frontend on the DVB device (/dev/dvb/adapterN/frontendM). Most devices have only one frontend. The default is frontend 0.</p>
<dt><code>-d</code> number</p>
<dd>
<dt><code>&#8211;demux-id</code> number</p>
<dd> Select a different demultiplexer on the DVB device (/dev/dvb/adapterN/demuxM). Most devices have only one demultiplexer. The default is demultiplexer 0.</p>
<dt><code>-r</code> number</p>
<dd>
<dt><code>&#8211;dvr-id</code> number</p>
<dd> Select a different DVR interface on the DVB device (/dev/dvb/adapterN/dvrM). Most devices have only one DVR interface. The default is DVR interface 0.</p>
<dt><code>-T</code></p>
<dd>
<dt><code>&#8211;ts</code></p>
<dd> Decode an MPEG-2 Transport Stream on standard input instead of opening a DVB device. This option is mainly intended for debugging.</p>
<dt>
<dd> Since Transport Streams can contain multiple programs you must still specify one or more station names, which <code>zvbi-atsc-cc</code> will look up in a channel configuration file to determine the Program ID of the video elementary stream or streams it should extract. You should also add the <code>&#8211;atsc</code> option to clarify that this is an ATSC TS and the program should expect an <code>azap</code> channel configuration file, which is otherwise inferred from the DVB device capabilities.</dl>
<h3>Tuning options</h3>
<dl>
<dt><code>-e</code> file name</p>
<dd>
<dt><code>&#8211;channel-conf</code> file name</p>
<dd> To tune in a TV station <code>zvbi-atsc-cc</code> needs a channel configuration file. We use the config file of the <code>azap</code> tuning tool from the linuxtv-dvb-apps package. You can create it with the <code>scan</code> tool from the same package.</p>
<dt>
<dd> The azap channel configuration file is a text file which lists one station per line. Each line contains six fields separated by a colon: The station name, the transponder frequency in Hz, the modulation used (8VSB, 16VSB, QAM_64, QAM_256), the video stream PID, the audio stream PID, and the service ID. Empty lines and lines starting with a number sign will be ignored.</p>
<dt>
<dd> This option selects a different channel configuration file. The default is </p>
<pre>
<i>$HOME/.azap/channels.conf</i>
</pre>
<dt><code>-L</code> <code>&#8211;list</code></p>
<dd> List all stations in the channel configuration file and their transponder frequency.</p>
<dt><code>-n</code> station name</p>
<dd>
<dt><code>&#8211;station</code> station name</p>
<dd> The station to tune in. Usually the <code>-n</code> can be omitted.</p>
<dt>
<dd> <code>zvbi-atsc-cc</code> can record caption from multiple stations at once if they share a transponder frequency. Just specify multiple station names on the command line to enable this.</dl>
<h3>Caption options</h3>
<p> With the caption and XDS options you specify which data <code>zvbi-atsc-cc</code> should extract. If multiple station names are given these options apply to the succeeding station name. You must specify at least one of these options for each station.</p>
<dl>
<dt><code>-c</code> <code>&#8211;cc</code></p>
<dd> Print any received caption on standard output.</p>
<dt><code>-C</code> file name</p>
<dd>
<dt><code>&#8211;cc-file</code> file name</p>
<dd> Append any received caption to the specified file.</p>
<dt><code>-l</code> number</p>
<dd>
<dt><code>&#8211;channel</code> number</p>
<dd> Print NTSC Closed Caption channel 1, 2, 3 or 4 on standard output.</p>
<dt><code>-1</code> &#8230; <code>-4</code> file name</p>
<dd>
<dt><code>&#8211;cc1-file</code> &#8230; <code>&#8211;cc4-file</code> file name</p>
<dd> Filter out NTSC Closed Caption channel CC1 &#8230; CC4 and append the text to the specified file. CC1 is the primary, CC3 the secondary caption service. If both services are transmitted CC1 usually carries English, CC3 Spanish caption.</p>
<dt><code>-5</code> &#8230; <code>-8</code> file name</p>
<dd>
<dt><code>&#8211;t1-file</code> &#8230; <code>&#8211;t4-file</code> file name</p>
<dd> Filter out NTSC Text service T1 &#8230; T4 and append the text to the specified file.</p>
<dt><code>-9</code> &#8230; <code>-0</code> file name</p>
<dd>
<dt><code>&#8211;s1-file</code> &#8230; <code>&#8211;s2-file</code> file name</p>
<dd> Filter out DTVCC service 1 or 2 and append the text to the specified file. Service 1 is the primary, service 2 the secondary caption service. If both services are transmitted service 1 usually carries English, service 2 Spanish caption.</p>
<dt>
<dd> Digital TV stations are supposed to transmit language codes and other information about the available caption services but these are not presently evaluated. <code>zvbi-atsc-cc</code> filters out text which does not appear to be caption, such as tickers or vertically printed text.</p>
<dt><code>-b</code> <code>&#8211;no-webtv</code></p>
<dd> Do not print WebTV links.</p>
<dt><code>-m</code> <code>&#8211;timestamps</code></p>
<dd> Prepend timestamps (YYYYMMDDHHMMSS) to caption lines.</p>
<dt><code>-s</code> <code>&#8211;sentences</code></p>
<dd> Print caption one sentence at a time.</p>
<dt><code>-j</code> type</p>
<dd>
<dt><code>&#8211;format</code> type</p>
<dd> When type is &quot;plain&quot; <code>zvbi-atsc-cc</code> prints caption and XDS text without any markup. When type is &quot;vt100&quot; it faithfully reproduces the caption foreground and background color, italic and underline attributes by inserting VT.100 terminal control codes. With type &quot;ntsc-cc&quot; it mimics the output of the <code>ntsc-cc</code> and <code>zvbi-ntsc-cc</code> tool. The default is &quot;ntsc-cc&quot;.</p>
<dt>
<dd> <code>zvbi-atsc-cc supports all Closed Caption character sets and</code> converts to the encoding of the current locale, usually UTF-8.</p>
<dt><code>-p</code> <code>&#8211;plain</code></p>
<dd> Same as <code>-j plain</code></dl>
<h3>XDS options</h3>
<dl>
<dt><code>-x</code> <code>&#8211;xds</code></p>
<dd> Print all received XDS data on standard output.</p>
<dt><code>-X</code> file name</p>
<dd>
<dt><code>&#8211;xds-file</code> file name</p>
<dd> Filter out eXtended Data Service data (station name, program name, program rating etc.) and append it as text to the specified file.</p>
<dt><code>-f</code> type[,type]*</p>
<dd>
<dt><code>&#8211;filter</code> type[,type]*</p>
<dd> Filter out specific XDS information: all, call (station call sign), desc (program synopsis), length, network, rating, time, timecode, timezone, title. Multiple <code>-f</code> options accumulate. The default is &quot;all&quot;.</dl>
<h2>EXAMPLES</h2>
<pre>
zvbi-atsc-cc -c NJN-HD
zvbi-atsc-cc --cc1-file wnyw.txt WNYW-DT --cc1-file wwor.txt WWOR-DT
(NJN-HD, WNYW-DT and WWOR-DT are TV stations in New York. WNYW-DT
and WWOR-DT can be captured simultaneously because they share a
transponder frequency.)
</pre>
<h2>FILES</h2>
<p> <i>$HOME/.azap/channels.conf</i></p>
<h2>SEE ALSO</h2>
<p> zvbi-ntsc-cc, azap </p>
<p> <a rel="nofollow" href="http://zapping.sourceforge.net">http://zapping.sourceforge.net</a></p>
<h2>AUTHORS</h2>
<p> Michael H. Schimek (mschimek AT users.sourceforge.net)<br />
 timecop [at] japan.co.jp<br />
 Mike Baker<br />
 Mark K. Kim</p>
<h2>COPYRIGHT</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA. </p>
<h2>Index</h2>
