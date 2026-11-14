---
title: "icedax(1)"
name: "icedax"
section: "1"
letter: "i"
url: "/docs/linux/man/1-icedax/"
description: "icedax – a sampling utility that dumps CD audio data into wav sound files"
---

<h2>NAME</h2>
<p> icedax &#8211; a sampling utility that dumps CD audio data into wav sound files</p>
<h2>SYNOPSIS</h2>
<p> <code>icedax</code> [<code>-c</code> <i>chans</i>] [<code>-s</code>] [<code>-m</code>] [<code>-b</code> <i>bits</i>] [<code>-r</code> <i>rate</i>] [<code>-a</code> <i>divider</i>] [<code>-t</code> <i>track</i>[<i>+endtrack</i>]] [<code>-i</code> <i>index</i>] [<code>-o</code> <i>offset</i>] [<code>-d</code> <i>duration</i>] [<code>-x</code>] [<code>-q</code>] [<code>-w</code>] [<code>-v</code> <i>optlist</i>] [<code>-V</code>] [<code>-Q</code>] [<code>-J</code>] [<code>-L</code> <i>cddbmode</i>] [<code>-R</code>] [<code>-P</code> <i>sectors</i>] [<code>-F</code>] [<code>-G</code>] [<code>-T</code>] [<code>-e</code>] [<code>-p</code> <i>percentage</i>] [<code>-n</code> <i>sectors</i>] [<code>-l</code> <i>buffers</i>] [<code>-N</code>] [<code>-J</code>] [<code>-H</code>] [<code>-g</code>] [<code>-B</code>] [<code>-D</code> <i>device</i>] [<code>-A</code> <i>auxdevice</i>] [<code>-I</code> <i>interface</i>] [<code>-O</code> <i>audiotype</i>] [<code>-C</code> <i>input-endianess</i>] [<code>-E</code> <i>output-endianess</i>] [<code>-M</code> <i>count</i>] [<code>-S</code> <i>speed</i>] [<code>-paranoia</code>] [<code>cddbp-server=servername</code>] [<code>cddbp-port=portnumber</code>] [<i>filename(s)</i> or <i>directories</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>icedax</code> stands for InCrEdible Digital Audio eXtractor. It can retrieve audio tracks (<code>CDDA</code>) from CDROM drives that are capable of reading audio data digitally to the host (see README for a list of drives). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>dev=</code><i>device</i></p>
<dd>
<dt><code>-D</code><i> device</i></p>
<dd>
<dt><code>-device</code><i> device</i></p>
<dd> uses <code>device</code> as the source for CDDA reading. For example <code>/dev/cdrom</code> or <code>Bus,ID,Lun.</code> The device specification can also have influence on the selection of the driver interface (eg. on Linux). See the <code>-I</code> option for details. </p>
<p> The setting of the environment variable <code>CDDA_DEVICE</code> is overridden by this option.</p>
<dt><code>-A</code><i> auxdevice</i></p>
<dd>
<dt><code>-auxdevice</code><i> auxdevice</i></p>
<dd> uses <code>auxdevice</code> as CDROM drive for ioctl usage.</p>
<dt><code>-I</code><i> interface</i></p>
<dd>
<dt><code>-interface</code><i> interface</i></p>
<dd> specifies the interface for CDROM access: <code>generic_scsi</code> or (on Linux, and FreeBSD systems) <code>cooked_ioctl</code>. </p>
<p> Using the <code>cooked_ioctl</code> is not recommended as this makes <code>icedax</code> mainly depend on the audio extraction quality of the operating system which is usually extremely bad.</p>
<dt><code>-c</code><i> channels &#8211;channels</i></p>
<dd> uses <code>1</code> for mono, or <code>2</code> for stereo recording, or <code>s</code> for stereo recording with both channels swapped.</p>
<dt><code>-s &#8211;stereo</code></p>
<dd> sets to stereo recording.</p>
<dt><code>-m &#8211;mono</code></p>
<dd> sets to mono recording.</p>
<dt><code>-x &#8211;max</code></p>
<dd> sets maximum (CD) quality.</p>
<dt><code>-b</code><i> bits &#8211;bits-per-sample</i></p>
<dd> sets bits per sample per channel: <code>8</code>, <code>12</code> or <code>16</code>.</p>
<dt><code>-r</code><i> rate &#8211;rate</i></p>
<dd> sets rate in samples per second. Possible values are listed with the <code>-R</code> option.</p>
<dt><code>-a</code><i> divider &#8211;divider</i></p>
<dd> sets rate to 44100Hz / divider. Possible values are listed with the <code>-R</code> option.</p>
<dt><code>-R &#8211;dump-rates</code></p>
<dd> shows a list of all sample rates and their dividers.</p>
<dt><code>-P sectors &#8211;set-overlap</code></p>
<dd> sets the initial number of overlap <i>sectors</i> for jitter correction.</p>
<dt><code>-n</code><i> sectors &#8211;sectors-per-request</i></p>
<dd> reads <i>sectors</i> per request.</p>
<dt><code>-l</code><i> buffers &#8211;buffers-in-ring</i></p>
<dd> uses a ring buffer with <i>buffers</i> total.</p>
<dt><code>-t</code><i> track+endtrack &#8211;track</i></p>
<dd> selects the start track and optionally the end track.</p>
<dt><code>-i</code><i> index &#8211;index</i></p>
<dd> selects the start index.</p>
<dt><code>-o</code><i> offset &#8211;offset</i></p>
<dd> starts <i>offset</i> sectors behind start track (one sector equivalents 1/75 seconds).</p>
<dt><code>-O audiotype &#8211;output-format</code></p>
<dd> can be <i>wav</i> (for wav files) or <i>aiff</i> (for apple/sgi aiff files) or <i>aifc</i> (for apple/sgi aifc files) or <i>au</i> or <i>sun</i> (for sun .au PCM files) or <i>cdr</i> or <i>raw</i> (for headerless files to be used for cd writers).</p>
<dt><code>-C</code><i> endianess &#8211;cdrom-endianess</i></p>
<dd> sets endianess of the input samples to &#8216;little&#8217;, &#8216;big&#8217; or &#8216;guess&#8217; to override defaults.</p>
<dt><code>-E</code><i> endianess &#8211;output-endianess</i></p>
<dd> sets endianess of the output samples to &#8216;little&#8217; or &#8216;big&#8217; to override defaults.</p>
<dt><code>-d</code><i> duration &#8211;duration</i></p>
<dd> sets recording time in seconds or frames. Frames (sectors) are indicated by a &#8216;f&#8217; suffix (like 75f for 75 sectors). <code>0</code> sets the time for whole track.</p>
<dt><code>-B &#8211;bulk &#8211;alltracks</code></p>
<dd> copies each track into a separate file.</p>
<dt><code>-w &#8211;wait</code></p>
<dd> waits for signal, then start recording.</p>
<dt><code>-F &#8211;find-extremes</code></p>
<dd> finds extreme amplitudes in samples.</p>
<dt><code>-G &#8211;find-mono</code></p>
<dd> finds if input samples are in mono.</p>
<dt><code>-T &#8211;deemphasize</code></p>
<dd> undo the effect of pre-emphasis in the input samples.</p>
<dt><code>-e &#8211;echo</code></p>
<dd> copies audio data to sound device e.g. <code>/dev/dsp</code>.</p>
<dt><code>-p percentage &#8211;set-pitch</code></p>
<dd> changes pitch of audio data copied to sound device.</p>
<dt><code>-v itemlist &#8211;verbose-level</code></p>
<dd> prints verbose information about the CD. <code>Level</code> is a list of comma separated suboptions. Each suboption controls the type of information to be reported. </p>
<table BORDER>
<tr VALIGN=top>
<td ALIGN=center>Suboption</td>
<td ALIGN=center>Description
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>disable</td>
<td>no information is given, warnings appear however
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>all</td>
<td>all information is given
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>toc</td>
<td>show table of contents
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>summary</td>
<td>show a summary of the recording parameters
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>indices</td>
<td>determine and display index offsets
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>catalog</td>
<td>retrieve and display the media catalog number MCN
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>trackid</td>
<td> retrieve and display all International Standard Recording Codes ISRC
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>sectors</td>
<td> show the table of contents in start sector notation
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>titles</td>
<td> show the table of contents with track titles (when available)
</td>
</tr>
</table>
<dt><code>-N &#8211;no-write</code></p>
<dd> does not write to a file, it just reads (for debugging purposes).</p>
<dt><code>-J &#8211;info-only</code></p>
<dd> does not write to a file, it just gives information about the disc.</p>
<dt><code>-L cddb mode &#8211;cddb</code></p>
<dd> does a cddbp album- and track title lookup based on the cddb id. The parameter cddb mode defines how multiple entries shall be handled. </p>
<table BORDER>
<tr VALIGN=top>
<td ALIGN=center>Parameter</td>
<td ALIGN=center>Description
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>0</td>
<td> interactive mode. The user selects the entry to use.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>1</td>
<td> first fit mode. The first entry is taken unconditionally.
</td>
</tr>
</table>
<dt><code> cddbp-server=servername</code></p>
<dd> sets the server to be contacted for title lookups.</p>
<dt><code> cddbp-port=portnumber</code></p>
<dd> sets the port number to be used for title lookups.</p>
<dt><code>-H &#8211;no-infofile</code></p>
<dd> does not write an info file and a cddb file.</p>
<dt><code>-g &#8211;gui</code></p>
<dd> formats the output to be better parsable by gui frontends.</p>
<dt><code>-M count &#8211;md5</code></p>
<dd> enables calculation of MD-5 checksum for &#8216;count&#8217; bytes from a beginning of a track.</p>
<dt><code>-S speed &#8211;speed</code></p>
<dd> sets the cdrom device to one of the selectable speeds for reading.</p>
<dt><code>-q &#8211;quiet</code></p>
<dd> quiet operation, no screen output.</p>
<dt><code>-V &#8211;verbose-SCSI</code></p>
<dd> enable SCSI command logging to the console. This is mainly used for debugging.</p>
<dt><code>-Q &#8211;silent-SCSI</code></p>
<dd> suppress SCSI command error reports to the console. This is mainly used for guis.</p>
<dt><code>-scanbus</code></p>
<dd> Scan all SCSI devices on all SCSI busses and print the inquiry strings. This option may be used to find SCSI address of the CD/DVD-Recorder on a system. The numbers printed out as labels are computed by: <code>bus * 100 + target</code></p>
<dt><code>&#8211;devices</code></p>
<dd> Like -scanbus but works in a more native way, respecting the device name specification on the current operating system. See <code><a href="/docs/linux/man/1-wodim/">wodim</a>(1)</code> for details.</p>
<dt><code>-paranoia</code></p>
<dd> use the paranoia library instead of icedax&#8217;s routines for reading.</p>
<dt><code>-h &#8211;help</code></p>
<dd> display version of icedax on standard output.</p>
<dt>Defaults depend on the</p>
<dd> <code>Makefile</code> and <code>environment variable</code> settings (currently <code>CDDA_DEVICE</code> ).</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <code>CDDA_DEVICE</code> is used to set the device name. The device naming is compatible with the one used by the wodim tool.</p>
<dl>
<dt><code>CDDBP_SERVER</code></p>
<dd> is used for cddbp title lookups when supplied.</p>
<dt><code>CDDBP_PORT</code></p>
<dd> is used for cddbp title lookups when supplied.</p>
<dt><code>RSH</code></p>
<dd> If the <code>RSH</code> environment variable is present, the remote connection will not be created via <code><a href="/docs/linux/man/3-rcmd/">rcmd</a></code>(3) but by calling the program pointed to by <code>RSH</code>. Use e.g. <code>RSH=</code>/usr/bin/ssh to create a secure shell connection. </p>
<p> Note that this forces <code>icedax</code> to create a pipe to the <code><a href="/docs/linux/man/1-rsh/">rsh</a>(1)</code> program and disallows <code>icedax</code> to directly access the network socket to the remote server. This makes it impossible to set up performance parameters and slows down the connection compared to a <code>root</code> initiated <code><a href="/docs/linux/man/3-rcmd/">rcmd</a>(3)</code> connection.</p>
<dt><code>RSCSI</code></p>
<dd> If the <code>RSCSI</code> environment variable is present, the remote SCSI server will not be the program <code>/opt/schily/sbin/rscsi</code> but the program pointed to by <code>RSCSI</code>. Note that the remote SCSI server program name will be ignored if you log in using an account that has been created with a remote SCSI server program as login shell.</dl>
<h2>RETURN VALUES</h2>
<p> <code>icedax</code> uses the following exit codes to indicate various degrees of success: </p>
<table BORDER>
<tr VALIGN=top>
<td ALIGN=center>Exitcode</td>
<td ALIGN=center>Description
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>0</td>
<td>no errors encountered, successful operation.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>1</td>
<td>usage or syntax error. icedax got inconsistent arguments.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>2</td>
<td>permission (un)set errors. permission changes failed.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>3</td>
<td>read errors on the cdrom/burner device encountered.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>4</td>
<td> write errors while writing one of the output files encountered.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>5</td>
<td>errors with soundcard handling (initialization/write).
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>6</td>
<td> errors with stat() system call on the read device (cooked ioctl).
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>7</td>
<td>pipe communication errors encountered (in forked mode).
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>8</td>
<td>signal handler installation errors encountered.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>9</td>
<td>allocation of shared memory failed (in forked mode).
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>10</td>
<td>dynamic heap memory allocation failed.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>11</td>
<td>errors on the audio cd medium encountered.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>12</td>
<td>device open error in ioctl handling detected.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>13</td>
<td>race condition in ioctl interface handling detected.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>14</td>
<td>error in ioctl() operation encountered.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>15</td>
<td>internal error encountered. Please report back!!!
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>16</td>
<td> error in semaphore operation encountered (install / request).
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>17</td>
<td>could not get the scsi transfer buffer.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>18</td>
<td> could not create pipes for process communication (in forked mode).
</td>
</tr>
</table>
<h2>DISCUSSION</h2>
<p> <code>icedax</code> is able to read parts of an <code>audio</code> CD or <code>multimedia</code> CDROM (containing audio parts) directly digitally. These parts can be written to a file, a pipe, or to a sound device. </p>
<p> <code>icedax</code> stands for <code>CDDA</code> to <code>WAV</code> (where <code>CDDA</code> stands for compact disc digital audio and <code>WAV</code> is a sound sample format introduced by MS Windows). It allows copying <code>CDDA</code> audio data from the CDROM drive into a file in <code>WAV</code> or other formats. </p>
<p> The latest versions try to get higher real-time scheduling priorities to ensure smooth (uninterrupted) operation. These priorities are available for super users and are higher than those of &#8216;normal&#8217; processes. Thus delays are minimized. </p>
<p> If your CDROM is on device <code>DEV</code> and it is loaded with an audio CD, you may simply invoke <code>icedax dev=DEV</code> and it will create the sound file <code>audio.wav</code> recording the whole track beginning with track 1 in stereo at 16 bit at 44100 Hz sample rate, if your file system has enough space free. Otherwise recording time will be limited. For details see files <code>README</code> and <code>README.INSTALL</code></p>
<h2>HINTS ON OPTIONS</h2>
<dl>
<dt>Options</p>
<dd> Most of the options are used to control the format of the WAV file. In the following text all of them are described.</p>
<dt>Select Device</p>
<dd> <code>-D</code><i> device</i> selects the CDROM drive device to be used. The specifier given should correspond to the selected interface (see below). <code>CHANGE!</code> For the cooked_ioctl interface this is the cdrom device descriptor as before. <code>The SCSI devices used with the generic SCSI interface however are now</code> <code>addressed with their SCSI-Bus, SCSI-Id, and SCSI-Lun instead of the generic</code> <code>SCSI device descriptor!!!</code> One example for a SCSI CDROM drive on bus 0 with SCSI ID 3 and lun 0 is -D0,3,0.</p>
<dt>Select Auxiliary device</p>
<dd> <code>-A</code><i> auxdevice</i> is necessary for CD-Extra handling. For Non-SCSI-CDROM drives this is the same device as given by -D (see above). For SCSI-CDROM drives it is the CDROM drive (SCSI) device (i.e. <code>/dev/sr0</code> ) corresponding to the SCSI device (i.e. <code>0,3,0</code> ). It has to match the device used for sampling.</p>
<dt>Select Interface</p>
<dd> <code>-I</code><i> interface</i> selects the CDROM drive interface. For SCSI drives use generic_scsi (cooked_ioctl may not yet be available for all devices): <code>generic_scsi</code> and <code>cooked_ioctl</code>. The first uses the generic SCSI interface, the latter uses the ioctl of the CDROM driver. The latter variant works only when the kernel driver supports <code>CDDA</code> reading. This entry has to match the selected CDROM device (see above).</p>
<dt>Enable echo to soundcard</p>
<dd> <code>-e</code> copies audio data to the sound card while recording, so you hear it nearly simultaneously. The soundcard gets the same data that is recorded. This is time critical, so it works best with the <code>-q</code> option. To use <code>icedax</code> as a pseudo CD player without recording in a file you could use <code>icedax -q -e -t2 -d0 -N</code> to play the whole second track. This feature reduces the recording speed to at most onefold speed. You cannot make better recordings than your sound card can play (since the same data is used).</p>
<dt>Change pitch of echoed audio</p>
<dd> <code>-p percentage</code> changes the pitch of all audio echoed to a sound card. Only the copy to the soundcard is affected, the recorded audio samples in a file remain the same. Normal pitch, which is the default, is given by 100%. Lower percentages correspond to lower pitches, i.e. -p 50 transposes the audio output one octave lower. See also the script <code>pitchplay</code> as an example. This option was contributed by Raul Sobon.</p>
<dt>Select mono or stereo recording</p>
<dd> <code>-m</code> or <code>-c 1</code> selects mono recording (both stereo channels are mixed), <code>-s</code> or <code>-c 2</code> or <code>-c s</code> selects stereo recording. Parameter s will swap both sound channels.</p>
<dt>Select maximum quality</p>
<dd> <code>-x</code> will set stereo, 16 bits per sample at 44.1 KHz (full CD quality). Note that other format options given later can change this setting.</p>
<dt>Select sample quality</p>
<dd> <code>-b 8</code> specifies 8 bit (1 Byte) for each sample in each channel; <code>-b 12</code> specifies 12 bit (2 Byte) for each sample in each channel; <code>-b 16</code> specifies 16 bit (2 Byte) for each sample in each channel (Ensure that your sample player or sound card is capable of playing 12-bit or 16-bit samples). Selecting 12 or 16 bits doubles file size. 12-bit samples are aligned to 16-bit samples, so they waste some disk space.</p>
<dt>Select sample rate</p>
<dd> <code>-r</code><i> samplerate</i> selects a sample rate. <i>samplerate</i> can be in a range between 44100 and 900. Option <code>-R</code> lists all available rates.</p>
<dt>Select sample rate divider</p>
<dd> <code>-a</code><i> divider</i> selects a sample rate divider. <i>divider</i> can be minimally 1 and maximally 50.5 and everything between in steps of 0.5. Option <code>-R</code> lists all available rates.</p>
<dt>
<dd> To make the sound smoother at lower sampling rates, <code>icedax</code> sums over <i>n</i> samples (where <i>n</i> is the specific dividend). So for 22050 Hertz output we have to sum over 2 samples, for 900 Hertz we have to sum over 49 samples. This cancels higher frequencies. Standard sector size of an audio CD (ignoring additional information) is 2352 Bytes. In order to finish summing for an output sample at sector boundaries the rates above have to be chosen. Arbitrary sampling rates in high quality would require some interpolation scheme, which needs much more sophisticated programming.</p>
<dt>List a table of all sampling rates</p>
<dd> <code>-R</code> shows a list of all sample rates and their dividers. Dividers can range from 1 to 50.5 in steps of 0.5.</p>
<dt>Select start track and optionally end track</p>
<dd> <code>-t</code><i> n+m</i> selects <code>n</code> as the start track and optionally <code>m</code> as the last track of a range to be recorded. These tracks must be from the table of contents. This sets the track where recording begins. Recording can advance through the following tracks as well (limited by the optional end track or otherwise depending on recording time). Whether one file or different files are then created depends on the <code>-B</code> option (see below).</p>
<dt>Select start index</p>
<dd> <code>-i</code><i> n</i> selects the index to start recording with. Indices other than 1 will invoke the index scanner, which will take some time to find the correct start position. An offset may be given additionally (see below).</p>
<dt>Set recording time</p>
<dd> <code>-d n</code> sets recording time to <i>n</i> seconds or set recording time for whole track if <i>n</i> is zero. In order to specify the duration in frames (sectors) also, the argument can have an appended &#8216;f&#8217;. Then the numerical argument is to be taken as frames (sectors) rather than seconds. Please note that if track ranges are being used they define the recording time as well thus overriding any <code>-d</code> option specified times.</p>
<dt>
<dd> Recording time is defined as the time the generated sample will play (at the defined sample rate). Since it&#8217;s related to the amount of generated samples, it&#8217;s not the time of the sampling process itself (which can be less or more). It&#8217;s neither strictly coupled with the time information on the audio CD (shown by your hifi CD player). Differences can occur by the usage of the <code>-o</code> option (see below). Notice that recording time will be shortened, unless enough disk space exists. Recording can be aborted at anytime by pressing the break character (signal SIGQUIT).<br />
.IP&nbsp;<wbr>&quot;Record all tracks of a complete audio CD in separate files&quot; <code>-B</code> copies each track into a separate file. A base name can be given. File names have an appended track number and an extension corresponding to the audio format. To record all audio tracks of a CD, use a sufficient high duration (i.e. -d99999).</p>
<dt>Set start sector offset</p>
<dd> <code>-o</code><i> sectors</i> increments start sector of the track by <i>sectors</i>. By this option you are able to skip a certain amount at the beginning of a track so you can pick exactly the part you want. Each sector runs for 1/75 seconds, so you have very fine control. If your offset is so high that it would not fit into the current track, a warning message is issued and the offset is ignored. Recording time is not reduced. (To skip introductory quiet passages automagically, use the <code>-w</code> option see below.)</p>
<dt>Wait for signal option</p>
<dd> <code>-w</code> Turning on this option will suppress all silent output at startup, reducing possibly file size. <code>icedax</code> will watch for any signal in the output signal and switches on writing to file.</p>
<dt>Find extreme samples</p>
<dd> <code>-F</code> Turning on this option will display the most negative and the most positive sample value found during recording for both channels. This can be useful for readjusting the volume. The values shown are not reset at track boundaries, they cover the complete sampling process. They are taken from the original samples and have the same format (i.e. they are independent of the selected output format).</p>
<dt>Find if input samples are in mono</p>
<dd> <code>-G</code> If this option is given, input samples for both channels will be compared. At the end of the program the result is printed. Differences in the channels indicate stereo, otherwise when both channels are equal it will indicate mono.</p>
<dt>Undo the pre-emphasis in the input samples</p>
<dd> <code>-T</code> Some older audio CDs are recorded with a modified frequency response called pre-emphasis. This is found mostly in classical recordings. The correction can be seen in the flags of the Table Of Contents often. But there are recordings, that show this setting only in the subchannels. If this option is given, the index scanner will be started, which reads the q-subchannel of each track. If pre-emphasis is indicated in the q-subchannel of a track, but not in the TOC, pre-emphasis will be assumed to be present, and subsequently a reverse filtering is done for this track before the samples are written into the audio file.</p>
<dt>Set audio format</p>
<dd> <code>-O audiotype</code> can be <i>wav</i> (for wav files) or <i>au</i> or <i>sun</i> (for sun PCM files) or <i>cdr</i> or <i>raw</i> (for headerless files to be used for cd writers). All file samples are coded in linear pulse code modulation (as done in the audio compact disc format). This holds for all audio formats. Wav files are compatible to Wind*ws sound files, they have lsb,msb byte order as being used on the audio cd. The default filename extension is &#8216;.wav&#8217;. Sun type files are not like the older common logarithmically coded .au files, but instead as mentioned above linear PCM is used. The byte order is msb,lsb to be compatible. The default filename extension is &#8216;.au&#8217;. The AIFF and the newer variant AIFC from the Apple/SGI world store their samples in bigendian format (msb,lsb). In AIFC no compression is used. Finally the easiest &#8216;format&#8217;, the cdr aka raw format. It is done per default in msb,lsb byte order to satisfy the order wanted by most cd writers. Since there is no header information in this format, the sample parameters can only be identified by playing the samples on a soundcard or similar. The default filename extension is &#8216;.cdr&#8217; or &#8216;.raw&#8217;.</p>
<dt>Select cdrom drive reading speed</p>
<dd> <code>-S speed</code> allows to switch the cdrom drive to a certain level of speed in order to reduce read errors. The argument is transfered verbatim to the drive. Details depend very much on the cdrom drives. An argument of 0 for example is often the default speed of the drive, a value of 1 often selects single speed.</p>
<dt>Enable MD5 checksums</p>
<dd> <code>-M count</code> enables calculation of MD-5 checksum for &#8216;count&#8217; bytes from the beginning of a track. This was introduced for quick comparisons of tracks.</p>
<dt>Use Monty&#8217;s libparanoia for reading of sectors</p>
<dd> <code>-paranoia</code> selects an alternate way of extracting audio sectors. Monty&#8217;s library is used with the following default options: </p>
<p> PARANOIA_MODE_FULL, but without PARANOIA_MODE_NEVERSKIP </p>
<p> for details see Monty&#8217;s libparanoia documentation. In this case the option <code>-P</code> has no effect.</p>
<dt>Do linear or overlapping reading of sectors</p>
<dd> (This applies unless option <code>-paranoia</code> is used.) <code>-P sectors</code> sets the given number of sectors for initial overlap sampling for jitter correction. Two cases are to be distinguished. For nonzero values, some sectors are read twice to enable icedax&#8217;s jitter correction. If an argument of zero is given, no overlap sampling will be used. For nonzero overlap sectors icedax dynamically adjusts the setting during sampling (like cdparanoia does). If no match can be found, icedax retries the read with an increased overlap. If the amount of jitter is lower than the current overlapped samples, icedax reduces the overlap setting, resulting in a higher reading speed. The argument given has to be lower than the total number of sectors per request (see option <i>-n</i> below). Icedax will check this setting and issues a error message otherwise. The case of zero sectors is nice on low load situations or errorfree (perfect) cdrom drives and perfect (not scratched) audio cds.</p>
<dt>Set the transfer size</p>
<dd> <code>-n sectors</code> will set the transfer size to the specified sectors per request.</p>
<dt>Set number of ring buffer elements</p>
<dd> <code>-l buffers</code> will allocate the specified number of ring buffer elements.</p>
<dt>Set endianess of input samples</p>
<dd> <code>-C endianess</code> will override the default settings of the input format. Endianess can be set explicitly to &quot;little&quot; or &quot;big&quot; or to the automatic endianess detection based on voting with &quot;guess&quot;.</p>
<dt>Set endianess of output samples</p>
<dd> <code>-E endianess</code> (endianess can be &quot;little&quot; or &quot;big&quot;) will override the default settings of the output format.</p>
<dt>Verbose option</p>
<dd> <code>-v itemlist</code> prints more information. A list allows selection of different information items. </p>
<p> <code>disable</code> keeps quiet </p>
<p> <code>toc</code> displays the table of contents </p>
<p> <code>summary</code> displays a summary of recording parameters </p>
<p> <code>indices</code> invokes the index scanner and displays start positions of indices </p>
<p> <code>catalog</code> retrieves and displays a media catalog number </p>
<p> <code>trackid</code> retrieves and displays international standard recording codes </p>
<p> <code>sectors</code> displays track start positions in absolute sector notation </p>
<p> To combine several requests just list the suboptions separated with commas.</p>
<dt>The table of contents</p>
<dd> The display will show the table of contents with number of tracks and total time (displayed in <i>mm</i>:<i>ss</i>.<i>hh</i> format, <i>mm</i>=minutes, <i>ss</i>=seconds, <i>hh</i>=rounded 1/100 seconds). The following list displays track number and track time for each entry. The summary gives a line per track describing the type of the track. </p>
<p> <center> <code>track preemphasis copypermitted tracktype chans</code><br />
 </center> </p>
<p> The <code>track</code> column holds the track number. <code>preemphasis</code> shows if that track has been given a non linear frequency response. NOTE: You can undo this effect with the <code>-T</code> option. <code>copy-permitted</code> indicates if this track is allowed to copy. <code>tracktype</code> can be data or audio. On multimedia CDs (except hidden track CDs) both of them should be present. <code>channels</code> is defined for audio tracks only. There can be two or four channels.</p>
<dt>No file output</p>
<dd> <code>-N</code> this debugging option switches off writing to a file.</p>
<dt>No infofile generation</p>
<dd> <code>-H</code> this option switches off creation of an info file and a cddb file.</p>
<dt>Generation of simple output for gui frontends</p>
<dd> <code>-g</code> this option switches on simple line formatting, which is needed to support gui frontends (like xcd-roast).</p>
<dt>Verbose SCSI logging</p>
<dd> <code>-V</code> this option switches on logging of SCSI commands. This will produce a lot of output (when SCSI devices are being used). This is needed for debugging purposes. The format is the same as being used with the cdrecord program from Joerg Schilling or the wodim tool. See there for details.</p>
<dt>Quiet option</p>
<dd> <code>-q</code> suppresses all screen output except error messages. That reduces cpu time resources.</p>
<dt>Just show information option</p>
<dd> <code>-J</code> does not write a file, it only prints information about the disc (depending on the <code>-v</code> option). This is just for information purposes.</dl>
<h2>CDDBP support</h2>
<dl>
<dt>Lookup album and track titles option</p>
<dd> <code>-L cddbp mode</code> Icedax tries to retrieve performer, album-, and track titles from a cddbp server. The default server right now is &#8216;freedb.freedb.org&#8217;. It is planned to have more control over the server handling later. The parameter defines how multiple entries are handled:</dl>
<p> 0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>interactive mode, the user chooses one of the entries.</p>
<p> 1<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>take the first entry without asking.</p>
<dl>
<dt>Set server for title lookups</p>
<dd> <code>cddbp-server servername</code> When using -L or &#8211;cddb, the server being contacted can be set with this option.</p>
<dt>Set portnumber for title lookups</p>
<dd> <code>cddbp-port portnumber</code> When using -L or &#8211;cddb, the server port being contacted can be set with this option.</dl>
<h2>HINTS ON USAGE</h2>
<p> Don&#8217;t create samples you cannot read. First check your sample player software and sound card hardware. I experienced problems with very low sample rates (stereo &lt;= 1575 Hz, mono &lt;= 3675 Hz) when trying to play them with standard WAV players for sound blaster (maybe they are not legal in <code>WAV</code> format). Most CD-Writers insist on audio samples in a bigendian format. Now icedax supports the <code>-E endianess</code> option to control the endianess of the written samples. </p>
<p> If your hardware is fast enough to run icedax uninterrupted and your CD drive is one of the &#8216;perfect&#8217; ones, you will gain speed when switching all overlap sampling off with the <code>-P 0</code> option. Further fine tuning can be done with the <code>-n sectors</code> option. You can specify how much sectors should be requested in one go. </p>
<p> Icedax supports <code>pipes</code> now. Use a filename of <code>&#8211;</code> to let icedax output its samples to standard output. </p>
<p> Conversion to other sound formats can be done using the <code>sox</code> program package (although the use of <code>sox -x</code> to change the byte order of samples should be no more necessary; see option <code>-E</code> to change the output byteorder). </p>
<p> If you want to sample more than one track into different files in one run, this is currently possible with the <code>-B</code> option. When recording time exceeds the track limit a new file will be opened for the next track.</p>
<h2>FILES</h2>
<p> Icedax can generate a lot of files for various purposes. </p>
<p> Audio files: </p>
<p> There are audio files containing samples with default extensions These files are not generated when option (-N) is given. Multiple files may be written when the bulk copy option (-B) is used. Individual file names can be given as arguments. If the number of file names given is sufficient to cover all included audio tracks, the file names will be used verbatim. Otherwise, if there are less file names than files needed to write the included tracks, the part of the file name before the extension is extended with &#8216;_dd&#8217; where dd represents the current track number. </p>
<p> Cddb and Cdindex files: </p>
<p> If icedax detects cd-extra or cd-text (album/track) title information, then .cddb and .cdindex files are generated unless suppressed by the option -H. They contain suitable formatted entries for submission to audio cd track title databases in the internet. The CDINDEX and CDDB(tm) systems are currently supported. For more information please visit <a rel="nofollow" href="http://www.musicbrainz.org">www.musicbrainz.org</a> and <a href="http://www.freedb.com">www.freedb.com</a>. </p>
<p> Inf files: </p>
<p> The inf files are describing the sample files and the part from the audio cd, it was taken from. They are a means to transfer information to a cd burning program like wodim. For example, if the original audio cd had pre-emphasis enabled, and icedax -T did remove the pre-emphasis, then the inf file has pre-emphasis not set (since the audio file does not have it anymore), while the .cddb and the .cdindex have pre-emphasis set as the original does.</p>
<h2>WARNING</h2>
<p> <code>IMPORTANT:</code> it is prohibited to sell copies of copyrighted material by noncopyright holders. This program may not be used to circumvent copyrights. The user acknowledges this constraint when using the software.</p>
<h2>BUGS</h2>
<p> Generation of md5 checksums is currently broken. </p>
<p> Performance may not be optimal on slower systems. </p>
<p> The index scanner may give timeouts. </p>
<p> The resampling (rate conversion code) uses polynomial interpolation, which is not optimal. </p>
<p> Icedax should use threads. </p>
<p> Icedax currently cannot sample hidden audio tracks (track 1 index 0).</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> Thanks goto Project MODE (<a rel="nofollow" href="http://www.mode.net/)">http://www.mode.net/)</a> and Fraunhofer Institut fuer integrierte Schaltungen (FhG-IIS) (<a rel="nofollow" href="http://www.iis.fhg.de/)">http://www.iis.fhg.de/)</a> for financial support. Plextor Europe and Ricoh Japan provided cdrom disk drives and cd burners which helped a lot to develop this software. Rammi has helped a lot with the debugging and showed a lot of stamina when hearing 100 times the first 16 seconds of the first track of the Krupps CD. Libparanoia contributed by Monty (Christopher Montgomery) xiphmont [at] mit.edu.</p>
<h2>AUTHOR</h2>
<p> Heiko Eissfeldt heiko [at] colossus.escape.de </p>
<p> This manpage describes the program implementation of <code>icedax</code> as shipped by the cdrkit distribution. See <code><a rel="nofollow" href="http://alioth.debian.org/projects/debburn/">http://alioth.debian.org/projects/debburn/</a></code> for details. It is a spinoff from the original program cdda2wav as distributed in the cdrtools package [1]. However, the cdrtools developers are not involved in the development of this spinoff and therefore shall not be made responsible for any problem caused by it. Do not try to get support for this program by contacting the original authors. </p>
<p> If you have support questions, send them to </p>
<p> <code>debburn-devel [at] lists.alioth.debian.org</code> </p>
<p> If you have definitely found a bug, send a mail to this list or to </p>
<p> <code>submit [at] bugs.debian.org</code> </p>
<p> writing at least a short description into the Subject and &quot;Package: cdrkit&quot; into the first line of the mail body. </p>
<h2>DATE</h2>
<p> 26 Sep 2006 </p>
<h2>SOURCES</h2>
<p> [1] Cdrtools 2.01.01a08 from May 2006, <a rel="nofollow" href="http://cdrecord.berlios.de">http://cdrecord.berlios.de</a> </p>
<h2>Index</h2>
