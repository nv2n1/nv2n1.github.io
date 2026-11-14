---
title: "vdr(5)"
name: "vdr"
section: "5"
letter: "v"
url: "/docs/linux/man/5-vdr/"
description: "vdr_files – the Video Disk Recorder Files"
---

<p>vdr_files &#8211; the Video Disk Recorder Files</p>
<h2>Description</h2>
<p>This page describes the formats of the various files <code>vdr</code> uses to store configuration data and recordings.</p>
<h2>Syntax</h2>
<h3>Channels</h3>
<p>The file <i>channels.conf</i> contains the channel configuration. Each line defines either a <code>group delimiter</code> or a <code>channel</code>. </p>
<p> A <code>group delimiter</code> is a line starting with a &#8216;:&#8217; as the very first character, followed by arbitrary text. Example: </p>
<p> <code>:First group</code> </p>
<p> Group delimiters may also be used to specify the number of the next channel. To do this, the character &#8216;@&#8217; and a number must immediately follow the &#8216;:&#8217;, as in </p>
<p> <code>:@201 First group</code> </p>
<p> The given number must be larger than the number of any previous channel (otherwise it is silently ignored). </p>
<p> A group delimiter can also be used to just set the next channel&#8217;s number, without an explicit delimiter text, as in </p>
<p> <code>:@201</code> </p>
<p> Such a delimiter will not appear in the Channels menu. </p>
<p> A <code>channel definition</code> is a line with channel data, where the fields are separated by &#8216;:&#8217; characters. Example: </p>
<table>
<tr VALIGN=top>
<td><code>RTL Television,RTL;RTL World:12187:hC34M2O0S0:S19.2E:27500:163=2:104=deu;106=deu:105:0:12003:1:1089:0</code>
</td>
</tr>
</table>
<p> The line number of a channel definition (not counting group separators, and based on a possible previous &#8216;@&#8230;&#8217; parameter) defines the channel&#8217;s number in OSD menus and the <i>timers.conf</i> file. </p>
<p> The fields in a channel definition have the following meaning (from left to right):</p>
<dl>
<dt><code>Name</code></p>
<dd>The channel&#8217;s name (if the name originally contains a &#8216;:&#8217; character it has to be replaced by &#8216;|&#8217;). Some TV stations provide a way of deriving a &quot;short name&quot; from the channel name, which can be used in situations where there is not much space for displaying a long name. If a short name is available for this channel, it follows the full name and is delimited by a comma, as in </p>
<p> <code>RTL Television,RTL:&#8230;</code> </p>
<p> If the short name itself would contain a comma, it is replaced with a &#8216;.&#8217;. Note that some long channel names may contain a comma, so the delimiting comma is always the rightmost one. </p>
<p> If present, the name of the service provider or &quot;bouquet&quot; is appended to the channel name, separated by a semicolon, as in </p>
<p> <code>RTL Television,RTL;RTL World:&#8230;</code></p>
<dt><code>Frequency</code></p>
<dd>The transponder frequency (as an integer). For DVB-S this value is in MHz. For DVB-C and DVB-T it can be given either in MHz, kHz or Hz (the actual value given will be multiplied by 1000 until it is larger than 1000000).</p>
<dt><code>Parameters</code></p>
<dd>Various parameters, depending on whether this is a DVB-S, DVB-C or DVB-T channel. Each parameter consist of a key character, followed by an integer number that represents the actual setting of that parameter. The valid key characters, their meaning (and allowed values) are </p>
<table>
<tr VALIGN=top>
<td><code>B</code></td>
<td>Bandwidth (1712, 5, 6, 7, 8, 10)
</td>
</tr>
<tr VALIGN=top>
<td><code>C</code></td>
<td>Code rate high priority (0, 12, 23, 34, 35, 45, 56, 67, 78, 89, 910)
</td>
</tr>
<tr VALIGN=top>
<td><code>D</code></td>
<td>coDe rate low priority (0, 12, 23, 34, 35, 45, 56, 67, 78, 89, 910)
</td>
</tr>
<tr VALIGN=top>
<td><code>G</code></td>
<td>Guard interval (4, 8, 16, 32, 128, 19128, 19256)
</td>
</tr>
<tr VALIGN=top>
<td><code>H</code></td>
<td>Horizontal polarization
</td>
</tr>
<tr VALIGN=top>
<td><code>I</code></td>
<td>Inversion (0, 1)
</td>
</tr>
<tr VALIGN=top>
<td><code>L</code></td>
<td>Left circular polarization
</td>
</tr>
<tr VALIGN=top>
<td><code>M</code></td>
<td>Modulation (2, 5, 6, 7, 10, 11, 12, 16, 32, 64, 128, 256, 999)
</td>
</tr>
<tr VALIGN=top>
<td><code>O</code></td>
<td>rollOff (0, 20, 25, 35)
</td>
</tr>
<tr VALIGN=top>
<td><code>P</code></td>
<td>stream id (0-255)
</td>
</tr>
<tr VALIGN=top>
<td><code>R</code></td>
<td>Right circular polarization
</td>
</tr>
<tr VALIGN=top>
<td><code>S</code></td>
<td>delivery System (0, 1)
</td>
</tr>
<tr VALIGN=top>
<td><code>T</code></td>
<td>Transmission mode (1, 2, 4, 8, 16, 32)
</td>
</tr>
<tr VALIGN=top>
<td><code>V</code></td>
<td>Vertical polarization
</td>
</tr>
<tr VALIGN=top>
<td><code>Y</code></td>
<td>hierarchY (0, 1, 2, 4)
</td>
</tr>
</table>
<p> <code>Bandwidth:</code> The bandwidth of the channel in MHz (1712 in kHz): (DVB-T/DVB-T2 only). </p>
<p> <code>Code rate high priority:</code> Forward Error Correction (FEC) of the high priority stream (DVB-T/DVB-T2). For DVB-S/DVB-S2 this parameter specifies the inner FEC scheme. 12 = 1/2, 23 = 2/3, 34 = 3/4, &#8230; </p>
<p> <code>Code rate low priority:</code> Forward Error Correction (FEC) of the low priority stream (DVB-T/DVB-T2 only). If no hierarchy is used, set to 0. </p>
<p> <code>Guard interval:</code> The guard interval value (DVB-T only): 4 = 1/4, 8 = 1/8, 16 = 1/16, 32 = 1/32, 128 = 1/128, 19128 = 19/128, 19256 = 19/256. </p>
<p> <code>Inversion:</code> Specifies whether the DVB frontend needs spectral inversion (DVB-T and DVB-C only). This is frontend specific, if in doubt, omit. </p>
<p> <code>Modulation:</code> Specifies the modulation/constellation of the channel as follows: </p>
<table>
<tr VALIGN=top>
<td><code>2</code></td>
<td>QPSK (DVB-S, DVB-S2, DVB-T, DVB-T2, ISDB-T)
</td>
</tr>
<tr VALIGN=top>
<td><code>5</code></td>
<td>8PSK (DVB-S, DVB-S2)
</td>
</tr>
<tr VALIGN=top>
<td><code>6</code></td>
<td>16APSK (DVB-S2)
</td>
</tr>
<tr VALIGN=top>
<td><code>7</code></td>
<td>32APSK (DVB-S2)
</td>
</tr>
<tr VALIGN=top>
<td><code>10</code></td>
<td>VSB8 (ATSC aerial)
</td>
</tr>
<tr VALIGN=top>
<td><code>11</code></td>
<td>VSB16 (ATSC aerial)
</td>
</tr>
<tr VALIGN=top>
<td><code>12</code></td>
<td>DQPSK (ISDB-T)
</td>
</tr>
<tr VALIGN=top>
<td><code>16</code></td>
<td>QAM16 (DVB-T, DVB-T2, ISDB-T)
</td>
</tr>
<tr VALIGN=top>
<td><code>32</code></td>
<td>QAM32
</td>
</tr>
<tr VALIGN=top>
<td><code>64</code></td>
<td>QAM64 (DVB-C, DVB-T, DVB-T2, ISDB-T)
</td>
</tr>
<tr VALIGN=top>
<td><code>128</code></td>
<td>QAM128 (DVB-C)
</td>
</tr>
<tr VALIGN=top>
<td><code>256</code></td>
<td>QAM256 (DVB-C, DVB-T2)
</td>
</tr>
</table>
<p> <code>Rolloff:</code> The Nyquist filter rolloff factor for DVB-S (<code>35</code>) and DVB-S2 (<code>35</code>, 25, 20), 35 = 0.35, 25 = 0.25, 20 = 0.20, DVB-S/DVB-S2 default value is 0.35 </p>
<p> <code>Stream id:</code> Input Stream Identifier (ISI) (<code>0</code>-255) for DVB-S2 multiplex or Physical Layer Pipe (PLP) id (<code>0</code>-255) for DVB-T2 multiplex (DVB-S2/DVB-T2 only, with devices that support &quot;multi streaming&quot;). </p>
<p> <code>Transmission mode:</code> Number of DVB-T OFDM carriers, 32 = 32k, 16 = 16k, 8 = 8k, 4 = 4k, 2 = 2k, 1 = 1k. If in doubt, try 8k. </p>
<p> <code>Hierarchy:</code> If set to 1, this transponder uses two streams, high priority and low priority. If in doubt, try 0 (off). (DVB-T/DVB-T2 only). </p>
<p> <code>Delivery System:</code> The delivery system (0 = &quot;first generation&quot; (DVB-S/DVB-T), 1 = &quot;second generation&quot; (DVB-S2/DVB-T2). </p>
<p> <code>Polarization:</code> Satellite antenna polarization. H = horizontal, V = vertical, R = circular right, L = circular left. </p>
<p> The polarization parameters have no integer numbers following them. This is for compatibility with files from older versions and also to keep the DVB-S entries as simple as possible. </p>
<p> The special value <code>999</code> is used for &quot;automatic&quot;, which means the driver will automatically determine the proper value (if possible). </p>
<p> An example of a parameter field for a DVB-T channel might look like this: <code>B8C23D12G8M16T8Y0S0</code> </p>
<p> An example of a parameter field for a DVB-T2 channel might look like this: <code>B8C23D12G8M16T8Y0P0S1</code> </p>
<p> An example of a parameter field for a DVB-C channel might look like this: <code>C0M64</code> </p>
<p> An example of a parameter field for a DVB-S channel might look like this: <code>HC56M2O35S0</code> </p>
<p> An example of a parameter field for a DVB-S2 channel might look like this: <code>HC910M2O35S1</code> </p>
<p> Plugins that implement devices that need their own set of parameters may store those in the parameters string in arbitrary format (not necessarily the &quot;character/number&quot; format listed above). The only condition is that the string may not contain colons (&#8216;:&#8217;) or newline characters.</p>
<dt><code>Source</code></p>
<dd>The signal source of this channel, as defined in the file <i>sources.conf</i>.</p>
<dt><code>Srate</code></p>
<dd>The symbol rate of this channel (DVB-S and DVB-C only).</p>
<dt><code>VPID</code></p>
<dd>The video PID (set to &#8216;0&#8217; for radio channels). If this channel uses a separate PCR PID, it follows the VPID, separated by a plus sign, as in </p>
<p> <code>&#8230;:164+17:&#8230;</code> </p>
<p> If this channel has a video mode other than 0, the mode follows the pids, separated by an &#8216;=&#8217; sign, as in </p>
<p> <code>&#8230;:164+17=27:&#8230;</code></p>
<dt><code>APID</code></p>
<dd>The audio PID (either one number, or several, separated by commas). If this channel also carries Dolby Digital sound, the Dolby PIDs follow the audio PIDs, separated by a semicolon, as in </p>
<p> <code>&#8230;:101,102;103,104:&#8230;</code> </p>
<p> If certain audio PIDs broadcast in specific languages, the language codes for these can be appended to the individual audio or Dolby PID, separated by an &#8216;=&#8217; sign, as in </p>
<p> <code>&#8230;:101=deu,102=eng;103=deu,104=eng:&#8230;</code> </p>
<p> Some channels broadcast two different languages in the two stereo channels, which can be indicated by adding a second language code, delimited by a &#8216;+&#8217; sign, as in </p>
<p> <code>&#8230;:101=deu,102=eng+spa;103=deu,104=eng:&#8230;</code> </p>
<p> The audio type is appended with a separating &#8216;@&#8217; character, as in </p>
<p> <code>&#8230;:101=deu@4,102=eng+spa@4,105=@4:&#8230;</code> </p>
<p> Note that if there is no language code, there still is the separating &#8216;=&#8217; if there is an audio type. </p>
<dt><code>TPID</code></p>
<dd>The teletext PID. If this channel also carries DVB subtitles, the DVB subtitling PIDs follow the teletext PID, separated by a semicolon, as in </p>
<p> <code>&#8230;:201;2001,2002:&#8230;</code> </p>
<p> If certain subtitling PIDs broadcast in specific languages, the language codes for these can be appended to the individual subtitling PID, separated by an &#8216;=&#8217; sign, as in </p>
<p> <code>&#8230;:201;2001=deu,2002=eng:&#8230;</code> </p>
<p> Manual teletext subtitling pages can be defined separated by a &#8216;+&#8217; sign. The pages (separated by commas) can contain language codes, delimited by a &#8216;=&#8217; sign, as in </p>
<p> <code>&#8230;:201+150=deu,151=fin;2001,2002:&#8230;</code> </p>
<dt><code>Conditional access</code></p>
<dd>A hexadecimal integer defining how this channel can be accessed: </p>
<table>
<tr VALIGN=top>
<td><code>0000</code></td>
<td>Free To Air
</td>
</tr>
<tr VALIGN=top>
<td><code>0001&#8230;000F</code></td>
<td>explicitly requires the device with the given number
</td>
</tr>
<tr VALIGN=top>
<td><code>0010&#8230;00FF</code></td>
<td>reserved for user defined assignments
</td>
</tr>
<tr VALIGN=top>
<td><code>0100&#8230;FFFF</code></td>
<td>specific decryption methods as broadcast in the data stream
</td>
</tr>
</table>
<p> Values in the range 0001&#8230;00FF will not be overwritten, all other values will be automatically replaced by the actual CA system identifiers received from the data stream. If there is more than one CA system id broadcast, they will be separated by commas, as in </p>
<p> <code>&#8230;:1702,1722,1801:&#8230;</code> </p>
<p> The values are in hex because that&#8217;s the way they are defined in the &quot;ETR 162&quot; document. Leading zeros may be omitted.</p>
<dt><code>SID</code></p>
<dd>The Service ID of this channel.</p>
<dt><code>NID</code></p>
<dd>The Network ID of this channel.</p>
<dt><code>TID</code></p>
<dd>The Transport stream ID of this channel.</p>
<dt><code>RID</code></p>
<dd>The Radio ID of this channel (typically 0, may be used to distinguish channels where NID, TID and SID are all equal).</dl>
<p> A particular channel can be uniquely identified by its <code>channel ID</code>, which is a string that looks like this: </p>
<p> <code>S19.2E-1-1089-12003-0</code> </p>
<p> The components of this string are the <code>Source</code> (S19.2E), <code>NID</code> (1), <code>TID</code> (1089), <code>SID</code> (12003) and <code>RID</code> (0) as defined above. The last part can be omitted if it is <code>0</code>, so the above example could also be written as S19.2E-1-1089-12003).<br />
 The <code>channel ID</code> is used in the <i>timers.conf</i> and <i>epg.data</i> files to properly identify the channels. </p>
<p> If a channel has both <code>NID</code> and <code>TID</code> set to 0, the <code>channel ID</code> will use the <code>Frequency</code> instead of the <code>TID</code>. For satellite channels an additional offset of 100000, 200000, 300000 or 400000 is added to that number, depending on the <code>Polarization</code> (<code>H</code>, <code>V</code>, <code>L</code> or <code>R</code>, respectively). This is necessary because on some satellites the same frequency is used for two different transponders, with opposite polarization.</p>
<h3>Timers</h3>
<p>The file <i>timers.conf</i> contains the timer setup. Each line contains one timer definition, with individual fields separated by &#8216;:&#8217; characters. Example: </p>
<p> <code>1:10:-T&#8212;&#8211;:2058:2150:50:5:Quarks &amp; Co:</code> </p>
<p> The fields in a timer definition have the following meaning (from left to right):</p>
<dl>
<dt><code>Flags</code></p>
<dd>The individual bits in this field have the following meaning: </p>
<table>
<tr VALIGN=top>
<td><code>1</code></td>
<td>the timer is active (and will record if it hits)
</td>
</tr>
<tr VALIGN=top>
<td><code>2</code></td>
<td>this is an instant recording timer
</td>
</tr>
<tr VALIGN=top>
<td><code>4</code></td>
<td>this timer uses VPS
</td>
</tr>
<tr VALIGN=top>
<td><code>8</code></td>
<td>this timer is currently recording (may only be up-to-date with SVDRP)
</td>
</tr>
</table>
<p> All other bits are reserved for future use.</p>
<dt><code>Channel</code></p>
<dd>The channel to record from. This is either the channel number as shown in the on-screen menus, or a complete channel ID. When reading <i>timers.conf</i> any channel numbers will be mapped to the respective channel ids and when the file is written again, there will only be channel ids. Channel numbers are accepted as input in order to allow easier creation of timers when manually editing <i>timers.conf</i>. Also, when timers are listed via SVDRP commands, the channels are given as numbers.</p>
<dt><code>Day</code></p>
<dd>The day when this timer shall record. </p>
<p> If this is a `single-shot&#8217; timer, this is the date on which this timer shall record, given in ISO notation (<code>YYYY-MM-DD</code>), as in: </p>
<p> <code>2005-03-19</code> </p>
<p> For compatibility with earlier versions of VDR this may also be just the day of month on which this timer shall record (must be in the range <code>1&#8230;31</code>). </p>
<p> In case of a `repeating&#8217; timer this is a string consisting of exactly seven characters, where each character position corresponds to one day of the week (with Monday being the first day). The character &#8216;-&#8216; at a certain position means that the timer shall not record on that day. Any other character will cause the timer to record on that day. Example: </p>
<p> <code>MTWTF&#8211;</code> </p>
<p> will define a timer that records on Monday through Friday and does not record on weekends. Note that only letters may be used here, no digits. For compatibility with timers created with earlier versions of VDR, the same result could be achieved with <code>ABCDE&#8211;</code> (which was used to allow setting the days with language specific characters). Since version 1.5.3 VDR can use UTF-8 characters to present data to the user, but the weekday encoding in the <i>timers.conf</i> file always uses single byte characters. </p>
<p> The day definition of a `repeating&#8217; timer may be followed by the date when that timer shall hit for the first time. The format for this is <code>@YYYY-MM-DD</code>, so a complete definition could look like this: </p>
<p> <code>MTWTF&#8211; [at] 2002-02-18</code> </p>
<p> which would implement a timer that records Monday through Friday, and will hit for the first time on or after February 18, 2002. This <code>first day</code> feature can be used to disable a repeating timer for a couple of days, or for instance to define a new Mon&#8230;Fri timer on Wednesday, which actually starts &quot;Monday next week&quot;. The <code>first day</code> date given need not be that of a day when the timer would actually hit.</p>
<dt><code>Start</code></p>
<dd>A four digit integer defining when this timer shall <code>start</code> recording. The format is <code>hhmm</code>, so <code>1430</code> would mean &quot;half past two&quot; in the afternoon.</p>
<dt><code>Stop</code></p>
<dd>A four digit integer defining when this timer shall <code>stop</code> recording. The format is the same as for the <code>start</code> time.</p>
<dt><code>Priority</code></p>
<dd>An integer in the range <code>0&#8230;99</code>, defining the <code>priority</code> of this timer and of recordings created by this timer. <code>0</code> represents the lowest value, <code>99</code> the highest. The priority is used to decide which timer shall be started in case there are two or more timers with the exact same <code>start</code> time. The first timer in the list with the highest priority will be used. </p>
<p> This value is also stored with the recording and is later used to decide which recording to remove from disk in order to free space for a new recording. If the disk runs full and a new recording needs more space, an existing recording with the lowest priority (and which has exceeded its guaranteed <code>lifetime</code>) will be removed. </p>
<p> If all available DVB cards are currently occupied, a timer with a higher priority will interrupt the timer with the lowest priority in order to start recording.</p>
<dt><code>Lifetime</code></p>
<dd>The <code>guaranteed lifetime</code> (in days) of a recording created by this timer. <code>0</code> means that this recording may be automatically deleted at any time by a new recording with higher priority. <code>99</code> means that this recording will never be automatically deleted. Any number in the range <code>1&#8230;98</code> means that this recording may not be automatically deleted in favour of a new recording, until the given number of days since the <code>start</code> time of the recording has passed by.</p>
<dt><code>File</code></p>
<dd>The <code>file name</code> this timer will give to a recording. If the name contains any &#8216;:&#8217; characters, these have to be replaced by &#8216;|&#8217;. If the name shall contain subdirectories, these have to be delimited by &#8216;~&#8217; (since the &#8216;/&#8217; character may be part of a regular programme name). </p>
<p> The special keywords <code>TITLE</code> and <code>EPISODE</code>, if present, will be replaced by the title and episode information from the EPG data at the time of recording (if that data is available). If at the time of recording either of these cannot be determined, <code>TITLE</code> will default to the channel name, and <code>EPISODE</code> will default to a blank.</p>
<dt><code>Auxiliary data</code></p>
<dd>An arbitrary string that can be used by external applications to store any kind of data related to this timer. The string must not contain any newline characters. If this field is not empty, its contents will be written into the <i>info</i> file of the recording with the &#8216;@&#8217; tag.</dl>
<h3>Sources</h3>
<p>The file <i>sources.conf</i> defines the codes to be used in the <code>Source</code> field of channels in <i>channels.conf</i> and assigns descriptive texts to them. Example: </p>
<p> <code>S19.2E Astra 1</code> </p>
<p> Anything after (and including) a &#8216;#&#8217; character is comment. </p>
<p> The first character of the <code>code</code> must be one of </p>
<table>
<tr VALIGN=top>
<td><code>A</code></td>
<td>ATSC
</td>
</tr>
<tr VALIGN=top>
<td><code>C</code></td>
<td>Cable
</td>
</tr>
<tr VALIGN=top>
<td><code>S</code></td>
<td>Satellite
</td>
</tr>
<tr VALIGN=top>
<td><code>T</code></td>
<td>Terrestrial
</td>
</tr>
</table>
<p> and is followed by further data pertaining to that particular source. In case of <code>S</code>atellite this is the orbital position in degrees, followed by <code>E</code> for east or <code>W</code> for west. Plugins may define additional sources, using other characters in the range &#8216;A&#8217;&#8230;&#8217;Z&#8217;.</p>
<h3>Diseqc</h3>
<p>The file <i>diseqc.conf</i> defines the <code>DiSEqC</code> control sequences to be sent to the DVB-S card in order to access a given satellite position and/or band. Example: </p>
<p> <code>S19.2E 11700 V 9750 t v W15 [E0 10 38 F0] W15 A W15 t</code> </p>
<p> Anything after (and including) a &#8216;#&#8217; character is comment. </p>
<p> The first word in a parameter line must be one of the codes defined in the file <i>sources.conf</i> and tells which satellite this line applies to. </p>
<p> Following is the &quot;switch frequency&quot; of the LNB (slof), which is the transponder frequency up to which this entry shall be used; the first entry with an slof greater than the actual transponder frequency will be used. Typically there is only one slof per LNB, but the syntax allows any number of frequency ranges to be defined. Note that there should be a last entry with the value <code>99999</code> for each satellite, which covers the upper frequency range. </p>
<p> The third parameter defines the polarization to which this entry applies. It can be either <code>H</code> for horizontal, <code>V</code> for vertical, <code>L</code> for circular left or <code>R</code> for circular right. </p>
<p> The fourth parameter specifies the &quot;local oscillator frequency&quot; (lof) of the LNB to use for the given frequency range. This number will be subtracted from the actual transponder frequency when tuning to the channel. </p>
<p> The rest of the line holds the actual sequence of DiSEqC actions to be taken. The code letters used here are </p>
<table>
<tr VALIGN=top>
<td><code>t</code></td>
<td>22kHz tone off
</td>
</tr>
<tr VALIGN=top>
<td><code>T</code></td>
<td>22kHz tone on
</td>
</tr>
<tr VALIGN=top>
<td><code>v</code></td>
<td>voltage low (13V)
</td>
</tr>
<tr VALIGN=top>
<td><code>V</code></td>
<td>voltage high (18V)
</td>
</tr>
<tr VALIGN=top>
<td><code>A</code></td>
<td>mini A
</td>
</tr>
<tr VALIGN=top>
<td><code>B</code></td>
<td>mini B
</td>
</tr>
<tr VALIGN=top>
<td><code>Sn</code></td>
<td>Satellite channel routing code sequence for bank n follows
</td>
</tr>
<tr VALIGN=top>
<td><code>Wnn</code></td>
<td>wait nn milliseconds (nn may be any positive integer number)
</td>
</tr>
<tr VALIGN=top>
<td><code>[xx &#8230;]</code></td>
<td>hex code sequence (max. 6)
</td>
</tr>
</table>
<p> There can be any number of actions in a line, including none at all &#8211; in which case the entry would be used only to set the LOF to use for the given frequency range and polarization. </p>
<p> By default it is assumed that every DVB-S device can receive every satellite. If this is not the case in a particular setup, lines of the form </p>
<p> <code>1 2 4:</code> </p>
<p> may be inserted in the <i>diseqc.conf</i> file, defining the devices that are able to receive the satellites following thereafter. In this case, only the devices 1, 2 and 4 would be able to receive any satellites following this line and up to the next such line, or the end of the file. Devices may be listed more than once.</p>
<h3>Satellite Channel Routing (Scr)</h3>
<p>The file <i>scr.conf</i> contains the channel definitions of the SCR device in use. The format is </p>
<p> channel frequency [pin] </p>
<p> where channel is the SCR device&#8217;s channel index (0-7), frequency is the user band frequency of the given channel, and pin is an optional pin number (0-255). The actual values are device specific and can be found in the SCR device&#8217;s manual. </p>
<p> Examples: </p>
<p> 0 1284<br />
 1 1400<br />
 2 1516<br />
 3 1632<br />
 4 1748<br />
 5 1864<br />
 6 1980<br />
 7 2096 </p>
<p> By default it is assumed that the SCR configurations apply to all devices, and each device will pick one. If you have several SCR sat cables connected to one VDR machine, or if you want to explicitly assign the SCR channels to your devices, lines of the form </p>
<p> <code>1 2 4:</code> </p>
<p> may be inserted in the <i>scr.conf</i> file, defining the devices that are allowed to use the SCR channels thereafter. In this case, only the devices 1, 2 and 4 would be allowed to use the SCR channels following this line and up to the next such line, or the end of the file. If a device is listed more than once, only its first appearance counts.</p>
<h3>Remote Control Keys</h3>
<p>The file <i>remote.conf</i> contains the key assignments for all remote control units. Each line consists of one key assignment in the following format: </p>
<p> <code>name.key code</code> </p>
<p> where <code>name</code> is the name of the remote control (for instance KBD for the PC keyboard, or LIRC for the &quot;Linux Infrared Remote Control&quot;), <code>key</code> is the name of the key that is defined (like Up, Down, Menu etc.), and <code>code</code> is a character string that this remote control delivers when the given key is pressed.</p>
<h3>Key Macros</h3>
<p>The file <i>keymacros.conf</i> contains user defined macros that will be executed whenever the given key is pressed. The format is </p>
<p> <code>macrokey [@plugin] key1 key2 key3&#8230;</code> </p>
<p> where <code>macrokey</code> is the key that shall initiate execution of this macro and can be one of <i>Up</i>, <i>Down</i>, <i>Ok</i>, <i>Back</i>, <i>Left</i>, <i>Right</i>, <i>Red</i>, <i>Green</i>, <i>Yellow</i>, <i>Blue</i>, <i>0</i>&#8230;<i>9</i> or <i>User1</i>&#8230;<i>User9</i>. The rest of the line consists of a set of keys, which will be executed just as if they had been pressed in the given sequence. The optional <code>@plugin</code> can be used to automatically select the given plugin. <code>plugin</code> is the name of the plugin, exactly as given in the -P option when starting VDR. There can be only one <code>@plugin</code> per key macro. For instance </p>
<p> <code>User1 @abc Down Down Ok</code> </p>
<p> would call the main menu function of the &quot;abc&quot; plugin and execute two &quot;Down&quot; key presses, followed by &quot;Ok&quot;.<br />
 Note that the color keys will only execute their macro function in &quot;normal viewing&quot; mode (i.e. when no other menu or player is active). The <i>User1</i>&#8230;<i>User9</i> keys will always execute their macro function. There may be up to 15 keys in such a key sequence.</p>
<h3>Folders</h3>
<p>The file <i>folders.conf</i> contains the definitions of folders that can be used in the &quot;Edit timer&quot; menu. Each line contains one folder definition. Leading whitespace and everything after and including a &#8216;#&#8217; is ignored. A line ending with &#8216;{&#8216; defines a sub folder (i.e. a folder that contains other folders), and a line consisting of only &#8216;}&#8217; ends the definition of a sub folder. </p>
<p> Example: </p>
<p> Daily { </p>
<p>&nbsp;<wbr>&nbsp;<wbr>News </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Soaps </p>
<p>&nbsp;<wbr>&nbsp;<wbr>}<br />
 Archive { </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Movies </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Sports </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Sci-Fi&nbsp;<wbr>{ </p>
<p>&nbsp;<wbr>Star Trek </p>
<p>&nbsp;<wbr>U.F.O. </p>
<p>&nbsp;<wbr>} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>}<br />
 Comedy<br />
 Science </p>
<p> Note that these folder definitions are only used to set the file name under which a timer will store its recording. Changing these definitions in any way has no effect on existing timers or recordings.</p>
<h3>Commands</h3>
<p>The file <i>commands.conf</i> contains the definitions of commands that can be executed from the <code>vdr</code> main menu&#8217;s &quot;Commands&quot; option. Each line contains one command definition in the following format: </p>
<p> <code>title : command</code> </p>
<p> where <code>title</code> is the string that will be displayed in the &quot;Commands&quot; menu, and <code>command</code> is the actual command string that will be executed when this option is selected. The delimiting &#8216;:&#8217; may be surrounded by any number of white space characters. If <code>title</code> ends with the character &#8216;?&#8217;, there will be a confirmation prompt before actually executing the command. This can be used for commands that might have serious results (like deleting files etc) to make sure they are not executed inadvertently. </p>
<p> Everything following (and including) a &#8216;#&#8217; character is considered to be comment. </p>
<p> You can have nested layers of command menus by surrounding a sequence of commands with &#8216;{&#8216;&#8230;&#8217;}&#8217; and giving it a title, as in </p>
<p> My Commands { </p>
<p>&nbsp;<wbr>&nbsp;<wbr>First list&nbsp;<wbr>{<br />
&nbsp;<wbr>Do something: some command<br />
&nbsp;<wbr>Do something else: another command<br />
&nbsp;<wbr>}<br />
&nbsp;<wbr>&nbsp;<wbr>Second list&nbsp;<wbr>{<br />
&nbsp;<wbr>Even more: yet another command<br />
&nbsp;<wbr>So much more: and yet another one<br />
&nbsp;<wbr>} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>} </p>
<p> Command lists can be nested to any depth. </p>
<p> By default the menu entries in the &quot;Commands&quot; menu will be numbered &#8216;1&#8217;&#8230;&#8217;9&#8242; to make them selectable by pressing the corresponding number key. If you want to use your own numbering scheme (maybe to skip certain numbers), just precede the <code>title</code>s with the numbers of your choice. <code>vdr</code> will suppress its automatic numbering if the first entry in <i>commands.conf</i> starts with a digit in the range &#8216;1&#8217;&#8230;&#8217;9&#8242;, followed by a blank. </p>
<p> In order to avoid error messages to the console, every command should have <i>stderr</i> redirected to <i>stdout</i>. Everything the command prints to <i>stdout</i> will be displayed in a result window, with <code>title</code> as its title. </p>
<p> Examples: </p>
<p> Check for new mail?: /usr/local/bin/checkmail 2&gt;&amp;1<br />
 CPU status: /usr/local/bin/cpustatus 2&gt;&amp;1<br />
 Disk space: df -h | grep &#8216;/video&#8217; | awk &#8216;{ print 100 &#8211; $5 &quot;% free&quot;; }&#8217;<br />
 Calendar: date;echo;cal </p>
<p> Note that the commands &#8216;checkmail&#8217; and &#8216;cpustatus&#8217; are only <code>examples</code>! Don&#8217;t send emails to the author asking where to find these ;-)<br />
 The &#8216;?&#8217; at the end of the &quot;Check for new mail?&quot; entry will prompt the user whether this command shall really be executed.</p>
<h3>Recording Commands</h3>
<p>The file <i>reccmds.conf</i> can be used to define commands that can be applied to the currently highlighted recording in the &quot;Recordings&quot; menu. The syntax is exactly the same as described for the file <i>commands.conf</i>. When executing a command, the directory name of the recording will be appended to the command string, separated by a blank and enclosed in single quotes.</p>
<h3>Svdrp Hosts</h3>
<p>The file <i>svdrphosts.conf</i> contains the IP numbers of all hosts that are allowed to access the SVDRP port. Each line contains one IP number in the format </p>
<p> <code>IP-Address[/Netmask]</code> </p>
<p> where <code>IP-Address</code> is the address of a host or a network in the usual dot separated notation (as in 192.168.100.1). If the optional <code>Netmask</code> is given only the given number of bits of <code>IP-Address</code> are taken into account. This allows you to grant SVDRP access to all hosts of an entire network. <code>Netmask</code> can be any integer from 1 to 32. The special value of 0 is only accepted if the <code>IP-Address</code> is 0.0.0.0, because this will give access to any host (<code>USE THIS WITH CARE!</code>). </p>
<p> Everything following (and including) a &#8216;#&#8217; character is considered to be comment. </p>
<p> Examples: </p>
<p> 127.0.0.1 # always accept localhost<br />
 192.168.100.0/24 # any host on the local net<br />
 204.152.189.113 # a specific host<br />
 0.0.0.0/0 # any host on any net (<code>USE WITH CARE!</code>)</p>
<h3>Setup</h3>
<p>The file <i>setup.conf</i> contains the basic configuration options for <code>vdr</code>. Each line contains one option in the format &quot;Name = Value&quot;. See the MANUAL file for a description of the available options.</p>
<h3>Themes</h3>
<p>The files <i>/var/lib/vdr/data/themes/&lt;skin&gt;-&lt;theme&gt;.theme</i> contain the color theme definitions for the various skins. In the actual file names <i>&lt;skin&gt;</i> will be replaced by the name if the skin this theme belongs to, and <i>&lt;theme&gt;</i> will be the name of this theme. Each line in a theme file contains one option in the format &quot;Name = Value&quot;. Anything after (and including) a &#8216;#&#8217; character is comment. </p>
<p> The definitions in a theme file are either <code>colors</code> or a <code>description</code>.<br />
 <code>Colors</code> are in the form </p>
<p> <code>clrTitle = FF123456</code> </p>
<p> where the name (clrTitle) is one of the names defined in the source code of the <code>skin</code> that uses this theme, through the <code>THEME_CLR()</code> macro. The value (FF123456) is an eight digit hex number that consist of four bytes, representing alpha (transparency), red, green and blue component of the color. An alpha value of 00 means the color will be completely transparent, while FF means it will be opaque. An RGB value of 000000 results in black, while FFFFFF is white. </p>
<p> A <code>description</code> can be given as </p>
<p> <code>Description = Shades of blue</code> </p>
<p> and will be used in the Setup/OSD menu to select a theme for a given skin. The description should give the user an idea what this theme will be like (for instance, in the given example it would use various shades of blue), and shouldn&#8217;t be too long to make sure it fits on the Setup screen. The default description always should be given in English. If you want, you can provide language specific descriptions as </p>
<p> <code>Description.eng = Shades of blue</code><br />
 <code>Description.ger = Blaut&ouml;ne</code> </p>
<p> where the language code is added to the keyword &quot;Description&quot;, separated by a dot. You can enter as many language specific descriptions as you like, but only those that have a corresponding locale messages file will be actually used. If a theme file doesn&#8217;t contain a Description, the name of the theme (as given in the theme&#8217;s file name) will be used.</p>
<h3>Audio/Video Data</h3>
<p>The files <i>00001.ts</i>&#8230;<i>65535.ts</i> are the actual recorded data files. In order to keep the size of an individual file below a given limit, a recording may be split into several files. The contents of these files is <code>Transport Stream</code> (TS) and contains data packets that are each 188 byte long and start with 0x47. Data is stored exactly as it is broadcast, with a generated PAT/PMT inserted right before every independent frame.</p>
<h3>Index</h3>
<p>The file <i>index</i> (if present in a recording directory) contains the (binary) index data into each of the the recording files <i>00001.ts</i>&#8230;<i>65535.ts</i>. It is used during replay to determine the current position within the recording, and to implement skipping and fast forward/back functions. See the definition of the <code>cIndexFile</code> class for details about the actual contents of this file.</p>
<h3>Info</h3>
<p>The file <i>info</i> (if present in a recording directory) contains a description of the recording, derived from the EPG data at recording time (if such data was available). The <code>Aux</code> field of the corresponding timer (if given) is copied into this file, using the &#8216;@&#8217; tag. This is a plain ASCII file and contains tagged lines like the <code>EPG DATA</code> file (see the description of the <i>epg.data</i> file). Note that the lowercase tags (&#8216;c&#8217; and &#8216;e&#8217;) will not appear in an <i>info</i> file. Lines tagged with &#8216;#&#8217; are ignored and can be used by external tools to store arbitrary information. </p>
<p> In addition to the tags used in the <i>epg.data</i> file, the following tag characters are defined: </p>
<table>
<tr VALIGN=top>
<td><code>F</code></td>
<td>&lt;frame rate&gt;
</td>
</tr>
<tr VALIGN=top>
<td><code>L</code></td>
<td>&lt;lifetime&gt;
</td>
</tr>
<tr VALIGN=top>
<td><code>P</code></td>
<td>&lt;priority&gt;
</td>
</tr>
<tr VALIGN=top>
<td><code>@</code></td>
<td>&lt;auxiliary data&gt;
</td>
</tr>
</table>
<h3>Resume</h3>
<p>The file <i>resume</i> (if present in a recording directory) contains the position within the recording where the last replay session left off. The file consists of tagged lines that describe the various parameters necessary to pick up replay where it left off. </p>
<p> The following tag characters are defined: </p>
<table>
<tr VALIGN=top>
<td><code>I</code></td>
<td>&lt;offset into the file <i>index</i>&gt;
</td>
</tr>
</table>
<h3>Marks</h3>
<p>The file <i>marks</i> (if present in a recording directory) contains the editing marks defined for this recording. Each line contains the definition of one mark in the following format: </p>
<p> <code>hh:mm:ss.ff comment</code> </p>
<p> where <code>hh:mm:ss.ff</code> is a frame position within the recording, given as &quot;hours, minutes, seconds and (optional) frame number&quot;. <code>comment</code> can be any string and may be used to describe this mark. If present, <code>comment</code> must be separated from the frame position by at least one blank. </p>
<p> The lines in this file need not necessarily appear in the correct temporal sequence, they will be automatically sorted by time index. </p>
<p> If a frame position doesn&#8217;t point to an I-frame of the corresponding recording, it will be shifted towards the next I-frame (either up or down, whichever is closer). </p>
<p> <code>CURRENT RESTRICTIONS:</code> </p>
<p> &#8211; the comment is currently not used by VDR</p>
<h3>Epg Data</h3>
<p>The file <i>epg.data</i> contains the EPG data in an easily parsable format. The first character of each line defines what kind of data this line contains. </p>
<p> The following tag characters are defined: </p>
<table>
<tr VALIGN=top>
<td><code>C</code></td>
<td>&lt;channel id&gt; &lt;channel name&gt;
</td>
</tr>
<tr VALIGN=top>
<td><code>E</code></td>
<td>&lt;event id&gt; &lt;start time&gt; &lt;duration&gt; &lt;table id&gt; &lt;version&gt;
</td>
</tr>
<tr VALIGN=top>
<td><code>T</code></td>
<td>&lt;title&gt;
</td>
</tr>
<tr VALIGN=top>
<td><code>S</code></td>
<td>&lt;short text&gt;
</td>
</tr>
<tr VALIGN=top>
<td><code>D</code></td>
<td>&lt;description&gt;
</td>
</tr>
<tr VALIGN=top>
<td><code>G</code></td>
<td>&lt;genre&gt; &lt;genre&gt;&#8230;
</td>
</tr>
<tr VALIGN=top>
<td><code>R</code></td>
<td>&lt;parental rating&gt;
</td>
</tr>
<tr VALIGN=top>
<td><code>X</code></td>
<td>&lt;stream&gt; &lt;type&gt; &lt;language&gt; &lt;descr&gt;
</td>
</tr>
<tr VALIGN=top>
<td><code>V</code></td>
<td>&lt;vps time&gt;
</td>
</tr>
<tr VALIGN=top>
<td><code>e</code></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>c</code></td>
<td>
</td>
</tr>
</table>
<p> Lowercase characters mark the end of a sequence that was started by the corresponding uppercase character. The outer frame consists of a sequence of one or more <code>C</code>&#8230;<code>c</code> (Channel) entries. Inside these any number of <code>E</code>&#8230;<code>e</code> (Event) entries are allowed. All other tags are optional (although every event should at least have a <code>T</code> entry). </p>
<p> There may be several <code>X</code> tags, depending on the number of tracks (video, audio etc.) the event provides. </p>
<table>
<tr VALIGN=top>
<td>&lt;channel id&gt; </td>
<td>is the &quot;channel ID&quot;, made up from the parameters defined in &#8216;channels.conf&#8217;
</td>
</tr>
<tr VALIGN=top>
<td>&lt;channel name&gt; </td>
<td>is the &quot;name&quot; as in &#8216;channels.conf&#8217; (for information only, may be left out)
</td>
</tr>
<tr VALIGN=top>
<td>&lt;event id&gt; </td>
<td>is a 32 bit unsigned int, uniquely identifying this event
</td>
</tr>
<tr VALIGN=top>
<td>&lt;start time&gt; </td>
<td>is the time (as a time_t integer) in UTC when this event starts
</td>
</tr>
<tr VALIGN=top>
<td>&lt;duration&gt; </td>
<td>is the time (in seconds) that this event will take
</td>
</tr>
<tr VALIGN=top>
<td>&lt;table id&gt; </td>
<td>is a hex number that indicates the table this event is contained in (if this is left empty it will be set to 0x00; and value less than 0x4E it will be treated as if it were 0x4E)
</td>
</tr>
<tr VALIGN=top>
<td>&lt;version&gt; </td>
<td>is a hex number that indicates the event&#8217;s version number inside its table (optional, ignored when reading EPG data)
</td>
</tr>
<tr VALIGN=top>
<td>&lt;title&gt; </td>
<td>is the title of the event
</td>
</tr>
<tr VALIGN=top>
<td>&lt;short text&gt; </td>
<td>is the short text of the event (typically the name of the episode etc.)
</td>
</tr>
<tr VALIGN=top>
<td>&lt;description&gt; </td>
<td>is the description of the event (any &#8216;|&#8217; characters will be interpreted as newlines)
</td>
</tr>
<tr VALIGN=top>
<td>&lt;genre&gt; </td>
<td>is a two digit hex code, as defined in ETSI EN 300 468, table 28 (up to 4 genre codes are supported)
</td>
</tr>
<tr VALIGN=top>
<td>&lt;parental rating&gt;</td>
<td>is the minimum age of the intended audience
</td>
</tr>
<tr VALIGN=top>
<td>&lt;stream&gt; </td>
<td>is the stream content (1 = MPEG2 video, 2 = MP2 audio, 3 = subtitles, 4 = AC3 audio, 5 = H.264 video, 6 = HEAAC audio)
</td>
</tr>
<tr VALIGN=top>
<td>&lt;type&gt; </td>
<td>is the stream type according to ETSI EN 300 468
</td>
</tr>
<tr VALIGN=top>
<td>&lt;language&gt; </td>
<td>is the three letter language code (optionally two codes, separated by &#8216;+&#8217;)
</td>
</tr>
<tr VALIGN=top>
<td>&lt;descr&gt; </td>
<td>is the description of this stream component
</td>
</tr>
<tr VALIGN=top>
<td>&lt;vps time&gt; </td>
<td>is the Video Programming Service time of this event
</td>
</tr>
</table>
<p> This file will be read at program startup in order to restore the results of previous EPG scans. </p>
<p> Note that the <code>event id</code> that comes from the DVB data stream is actually just 16 bit wide. The internal representation in VDR allows for 32 bit to be used, so that external tools can generate EPG data that is guaranteed not to collide with the ids of existing data.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-vdr/">vdr</a></code>(1)</p>
<h2>Author</h2>
<p>Written by Klaus Schmidinger.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;vdr-bugs [at] tvdr.de&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Klaus Schmidinger. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
