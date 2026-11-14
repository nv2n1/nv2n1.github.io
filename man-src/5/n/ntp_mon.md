---
title: "ntp_mon(5)"
name: "ntp_mon"
section: "5"
letter: "n"
url: "/docs/linux/man/5-ntp_mon/"
description: "ntp_mon – Monitoring Options"
---

<p>ntp_mon &#8211; Monitoring Options</p>
<h2>&nbsp;<wbr></h2>
<h2>Introduction</h2>
<p>The <code>ntpd</code> includes a comprehensive monitoring facility which collects statistical data of various types and writes the data to files associated with each type at defined events or intervals. The files associated with a particular type are collectively called the generation file set for that type. The files in the file set are the members of that set. </p>
<p> File sets have names specific to the type and generation epoch. The names are constructed from three concatenated elements <i></i><code>prefix</code><i></i>, <i></i><code>filename</code><i></i> and <i></i><code>suffix</code><i></i>: </p>
<dl>
<dd>
<dl>
<dt><i></i><code>prefix</code><i></i></p>
<dd>The directory path specified in the <code>statsdir</code> command.</p>
<dt><i></i><code>name</code><i></i></p>
<dd>The name specified by the <code>file</code> option of the <code>filegen</code> command.</p>
<dt><i></i><code>suffix</code><i></i></p>
<dd>A string of elements bdginning with . (dot) followed by a number of elements depending on the file set type.</dl>
</dl>
<p> Statistics files can be managed using scripts, examples of which are in the <code>46/scripts</code> directory. Using these or similar scripts and Unix <code>cron</code> jobs, the files can be automatically summarized and archived for retrospective analysis.</p>
<h2>Monitoring Commands</h2>
<dl>
<dd>
<dl>
<dt><code>filegen </code><i>name</i><code> file </code><i>filename</i><code> [type </code><i>type</i><code>] [link | nolink] [enable | disable]</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><i></i><code>name</code><i></i></p>
<dd>Specifies the file set type from the list in the next section.</p>
<dt><code>file </code><i>filename</i></p>
<dd>Specfies the file set name.</p>
<dt><code>type </code><i>typename</i></p>
<dd>Specifies the file set interval. The following intervals are supported with default <code>day</code>: </p>
<dl>
<dd>
<dl>
<dt><code>none</code></p>
<dd>The file set is actually a single plain file.</p>
<dt><code>pid</code></p>
<dd>One file set member is created for every incarnation of <code>ntpd</code>46 The file name suffix is the string .<code>n</code>, where <code>n</code> is the process ID of the <code>ntpd</code> server process.</p>
<dt><code>day</code></p>
<dd>One file set member is created per day. A day is defined as the period between 00:00 and 23:59 UTC. The file name suffix is the string .<code>yyyymmdd</code>, where <code>yyyy</code> is the year, <code>mm</code> the month of the year and <code>dd</code> the day of the month. Thus, member created on 10 December 1992 would have suffix <code>4619921210</code>46</p>
<dt><code>week</code></p>
<dd>One file set member is created per week. The week is defined as the day of year modulo 7. The file name suffix is the string .<code>yyyyWww</code>, where <code>yyyy</code> is the year, <code>W</code> stands for itself and <code>ww</code> the week number starting from 0. For example, The member created on 10 January 1992 would have suffix <code>461992W1</code>46</p>
<dt><code>month</code></p>
<dd>One file set member is created per month. The file name suffix is the string .<code>yyyymm</code>, where <code>yyyy</code> is the year and <code>mm</code> the month of the year starting from 1. For example, The member created on 10 January 1992 would have suffix <code>46199201</code>46</p>
<dt><code>year</code></p>
<dd>One file set member is generated per year. The file name suffix is the string .<code>yyyy</code>, where <code>yyyy</code> is the year. For example, The member created on 1 January 1992 would have suffix <code>461992</code>46</p>
<dt><code>age</code></p>
<dd>One file set member is generated every 24 hours of <code>ntpd</code> operation. The filename suffix is the string <code>46adddddddd</code>, where <code>a</code> stands for itself and <code>dddddddd</code> is the <code>ntpd</code> running time in seconds at the start of the corresponding 24-hour period.</dl>
</dl>
<dt><code>link | nolink</code></p>
<dd>It is convenient to be able to access the current file set members by file name, but without the suffix. This feature is enabled by <code>link</code> and disabled by <code>nolink</code>46 If enabled, which is the default, a hard link from the current file set member to a file without suffix is created. When there is already a file with this name and the number of links to this file is one, it is renamed by appending a dot, the letter <code>C</code>, and the pid of the <code>ntpd</code> server process. When the number of links is greater than one, the file is unlinked. This allows the current file to be accessed by a constant name.</p>
<dt><code>enable | disable</code></p>
<dd>Enable or disable the recording function, with default <code>enable</code>46 These options are intended for remote configutation commands.</dl>
</dl>
<dt><code>statsdir </code><i>directory_path</i></p>
<dd>Specify the directory path prefix for statistics file names.</dl>
</dl>
<h2>File Set Types</h2>
<dl>
<dd>
<dl>
<dt><code>clockstats</code></p>
<dd>Record reference clock statistics. Each update received from a reference clock driver appends one line to the <code>clockstats</code> file set: <code>49213 525.624 127.127.4.1 93 226 00:08:29.606 D</code> </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>Item </td>
<td> Units </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td><code>49213</code> </td>
<td> MJD </td>
<td> date
</td>
</tr>
<tr VALIGN=top>
<td><code>525.624</code> </td>
<td> s </td>
<td> time past midnight
</td>
</tr>
<tr VALIGN=top>
<td><code>127.127.4.1</code> </td>
<td> IP </td>
<td> reference clock address
</td>
</tr>
<tr VALIGN=top>
<td><i>message</i> </td>
<td> text </td>
<td> log message
</td>
</tr>
</table>
<p> The <i>message</i> field includes the last timecode received in decoded ASCII format, where meaningful. In some cases a good deal of additional information is displayed. See information specific to each reference clock for further details.</p>
<dt><code>cryptostats</code></p>
<dd>Record significant events in the Autokey protocol. This option requires the OpenSSL cryptographic software library. Each event appends one line to the <code>cryptostats</code> file set: <code>49213 525.624 128.4.1.1 </code><i>message</i> </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>Item </td>
<td> Units </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td><code>49213</code> </td>
<td> MJD </td>
<td> date
</td>
</tr>
<tr VALIGN=top>
<td><code>525.624</code> </td>
<td> s </td>
<td> time past midnight
</td>
</tr>
<tr VALIGN=top>
<td><code>128.4.1.1</code> </td>
<td> IP </td>
<td> source address (<code>0.0.0.0</code> for system)
</td>
</tr>
<tr VALIGN=top>
<td><i>message</i> </td>
<td> text </td>
<td> log message
</td>
</tr>
</table>
<p> The <i>message</i> field includes the message type and certain ancillary information. See the Authentication Options page for further information.</p>
<dt><code>loopstats</code></p>
<dd>Record clock discipline loop statistics. Each system clock update appends one line to the <code>loopstats</code> file set: <code>50935 75440.031 0.000006019 13.778 0.000351733 0.013380 6</code> </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>Item </td>
<td> Units </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td><code>50935</code> </td>
<td> MJD </td>
<td> date
</td>
</tr>
<tr VALIGN=top>
<td><code>75440.031</code> </td>
<td> s </td>
<td> time past midnight
</td>
</tr>
<tr VALIGN=top>
<td><code>0.000006019</code> </td>
<td> s </td>
<td> clock offset
</td>
</tr>
<tr VALIGN=top>
<td><code>13.778</code> </td>
<td> PPM </td>
<td> frequency offset
</td>
</tr>
<tr VALIGN=top>
<td><code>0.000351733</code> </td>
<td> s </td>
<td> RMS jitter
</td>
</tr>
<tr VALIGN=top>
<td><code>0.013380</code> </td>
<td> PPM </td>
<td> RMS frequency jitter (aka wander)
</td>
</tr>
<tr VALIGN=top>
<td><code>6 </code> </td>
<td> log2 s </td>
<td> clock discipline loop time constant
</td>
</tr>
</table>
<dt><code>peerstats</code></p>
<dd>Record peer statistics. Each NTP packet or reference clock update received appends one line to the <code>peerstats</code> file set: <code>48773 10847.650 127.127.4.1 9714 -0.001605376 0.000000000 0.001424877 0.000958674</code> </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>Item </td>
<td> Units </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td><code>48773</code> </td>
<td> MJD </td>
<td> date
</td>
</tr>
<tr VALIGN=top>
<td><code>10847.650</code> </td>
<td> s </td>
<td> time past midnight
</td>
</tr>
<tr VALIGN=top>
<td><code>127.127.4.1</code> </td>
<td> IP </td>
<td> source address
</td>
</tr>
<tr VALIGN=top>
<td><code>9714</code> </td>
<td> hex </td>
<td> status word
</td>
</tr>
<tr VALIGN=top>
<td><code>-0.001605376</code> </td>
<td> s </td>
<td> clock offset
</td>
</tr>
<tr VALIGN=top>
<td><code>0.000000000 </code> </td>
<td> s </td>
<td> roundtrip delay
</td>
</tr>
<tr VALIGN=top>
<td><code>0.001424877</code> </td>
<td> s </td>
<td> dispersion
</td>
</tr>
<tr VALIGN=top>
<td><code>0.000958674</code> </td>
<td> s </td>
<td> RMS jitter
</td>
</tr>
</table>
<p> The status field is encoded in hex format as described in Appendix B of the NTP specification RFC 1305.</p>
<dt><code>protostats</code></p>
<dd>Record significant peer, system and [rptpcp; events. Each significant event appends one line to the <code>protostats</code> file set: <code>49213 525.624 128.4.1.1 963a 8a </code><i>message</i> </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>Item </td>
<td> Units </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td><code>49213</code> </td>
<td> MJD </td>
<td> date
</td>
</tr>
<tr VALIGN=top>
<td><code>525.624</code> </td>
<td> s </td>
<td> time past midnight
</td>
</tr>
<tr VALIGN=top>
<td><code>128.4.1.1</code> </td>
<td> IP </td>
<td> source address (<code>0.0.0.0</code> for system)
</td>
</tr>
<tr VALIGN=top>
<td><code>963a</code> </td>
<td> code </td>
<td> status word
</td>
</tr>
<tr VALIGN=top>
<td><code>8a</code> </td>
<td> code </td>
<td> event message code
</td>
</tr>
<tr VALIGN=top>
<td><i>message</i> </td>
<td> text </td>
<td> event message
</td>
</tr>
</table>
<p> The event message code and <i>message</i> field are described on the Event Messages and Status Words page.</p>
<dt><code>rawstats</code></p>
<dd>Record timestamp statistics. Each NTP packet received appends one line to the <code>rawstats</code> file set: <code>50928 2132.543 128.4.1.1 128.4.1.20 3102453281.584327000 3102453281.58622800031 02453332.540806000 3102453332.541458000</code> </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>Item </td>
<td> Units </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td><code>50928</code> </td>
<td> MJD </td>
<td> date
</td>
</tr>
<tr VALIGN=top>
<td><code>2132.543</code> </td>
<td> s </td>
<td> time past midnight
</td>
</tr>
<tr VALIGN=top>
<td><code>128.4.1.1</code> </td>
<td> IP </td>
<td> source address
</td>
</tr>
<tr VALIGN=top>
<td><code>128.4.1.20</code> </td>
<td> IP </td>
<td> destination address
</td>
</tr>
<tr VALIGN=top>
<td><code>3102453281.584327000</code> </td>
<td> NTP s </td>
<td> origin timestamp
</td>
</tr>
<tr VALIGN=top>
<td><code>3102453281.586228000</code> </td>
<td> NTP s </td>
<td> receive timestamp
</td>
</tr>
<tr VALIGN=top>
<td><code>3102453332.540806000 </code> </td>
<td> NTP s </td>
<td> transmit timestamp
</td>
</tr>
<tr VALIGN=top>
<td><code>3102453332.541458000</code> </td>
<td> NTP s </td>
<td> destination timestamp
</td>
</tr>
</table>
<dt><code>sysstats</code></p>
<dd>Record system statistics. Each hour one line is appended to the <code>sysstats</code> file set in the following format: <code>50928 2132.543 3600 81965 0 9546 56 512 540 10 4 147 1</code> </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>Item </td>
<td> Units </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td><code>50928</code> </td>
<td> MJD </td>
<td> date
</td>
</tr>
<tr VALIGN=top>
<td><code>2132.543</code> </td>
<td> s </td>
<td> time past midnight
</td>
</tr>
<tr VALIGN=top>
<td><code>3600</code> </td>
<td> s </td>
<td> time since reset
</td>
</tr>
<tr VALIGN=top>
<td><code>81965</code> </td>
<td> # </td>
<td> packets received
</td>
</tr>
<tr VALIGN=top>
<td><code>0</code> </td>
<td> # </td>
<td> packets for this host
</td>
</tr>
<tr VALIGN=top>
<td><code>9546</code> </td>
<td> # </td>
<td> current versions
</td>
</tr>
<tr VALIGN=top>
<td><code>56</code> </td>
<td> # </td>
<td> old version
</td>
</tr>
<tr VALIGN=top>
<td><code>512</code> </td>
<td> # </td>
<td> access denied
</td>
</tr>
<tr VALIGN=top>
<td><code>540</code> </td>
<td> # </td>
<td> bad length or format
</td>
</tr>
<tr VALIGN=top>
<td><code>10</code> </td>
<td> # </td>
<td> bad authentication
</td>
</tr>
<tr VALIGN=top>
<td><code>4</code> </td>
<td> # </td>
<td> declined
</td>
</tr>
<tr VALIGN=top>
<td><code>147</code> </td>
<td> # </td>
<td> rate exceeded
</td>
</tr>
<tr VALIGN=top>
<td><code>1</code> </td>
<td> # </td>
<td> kiss-o&#8217;-death packets sent
</td>
</tr>
</table>
<dt><code>timingstats</code></p>
<dd>(Only available when the deamon is compiled with process time debugging support (&#8211;enable-debug-timing &#8211; costs performance). Record processing time statistics for various selected code paths. <code>53876 36.920 10.0.3.5 1 0.000014592 input processing delay</code> </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>Item </td>
<td> Units </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td><code>53876</code> </td>
<td> MJD </td>
<td> date
</td>
</tr>
<tr VALIGN=top>
<td><code>36.920</code> </td>
<td> s </td>
<td> time past midnight
</td>
</tr>
<tr VALIGN=top>
<td><code>10.0.3.5</code> </td>
<td> IP </td>
<td> server address
</td>
</tr>
<tr VALIGN=top>
<td><code>1</code> </td>
<td> # </td>
<td> event count
</td>
</tr>
<tr VALIGN=top>
<td><code>0.000014592</code> </td>
<td> s </td>
<td> total time
</td>
</tr>
<tr VALIGN=top>
<td><i>message</i> </td>
<td> text </td>
<td> code path description (see source)
</td>
</tr>
</table>
</dl>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-ntp-conf/">ntp.conf</a>(5), <a href="/docs/linux/man/5-ntp_decode/">ntp_decode</a>(5) The official HTML documentation. This file was automatically generated from HTML source. </p>
