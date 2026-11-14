---
title: "amanda(5)"
name: "amanda"
section: "5"
letter: "a"
url: "/docs/linux/man/5-amanda/"
description: "amanda.conf – Main configuration file for Amanda, the Advanced Maryland Automatic Network Disk Archiver"
---

<p>amanda.conf &#8211; Main configuration file for Amanda, the Advanced Maryland Automatic Network Disk Archiver</p>
<h2>Description</h2>
<p><i>amanda.conf</i> is the main configuration file for <i>Amanda</i>. This manpage lists the relevant sections and parameters of this file for quick reference. </p>
<p> The file <code>&lt;CONFIG_DIR&gt;/&lt;config&gt;/amanda.conf</code> is loaded.</p>
<h2>Parameters</h2>
<p>There are a number of configuration parameters that control the behavior of the <i>Amanda</i> programs. All have default values, so you need not specify the parameter in <code>amanda.conf</code> if the default is suitable. </p>
<p> Lines starting with # are ignored, as are blank lines. Comments may be placed on a line with a directive by starting the comment with a #. The remainder of the line is ignored. </p>
<p> Keywords are case insensitive, i.e. <code>mailto</code> and <code>MailTo</code> are treated the same. </p>
<p> Integer arguments may have one of the following (case insensitive) suffixes, some of which have a multiplier effect:</p>
<h3>Possible Suffixes</h3>
<p><code>b byte bytes</code></p>
<dl>
<dd>Some number of bytes.</dl>
<p> <code>bps</code></p>
<dl>
<dd>Some number of bytes per second.</dl>
<p> <code>k kb kbyte kbytes kilobyte kilobytes</code></p>
<dl>
<dd>Some number of kilobytes (bytes*1024).</dl>
<p> <code>kps kbps</code></p>
<dl>
<dd>Some number of kilobytes per second (bytes*1024).</dl>
<p> <code>m mb meg mbyte mbytes megabyte megabytes</code></p>
<dl>
<dd>Some number of megabytes (bytes*1024*1024).</dl>
<p> <code>mps mbps</code></p>
<dl>
<dd>Some number of megabytes per second (bytes*1024*1024).</dl>
<p> <code>g gb gbyte gbytes gigabyte gigabytes</code></p>
<dl>
<dd>Some number of gigabytes (bytes*1024*1024*1024).</dl>
<p> <code>tape tapes</code></p>
<dl>
<dd>Some number of tapes.</dl>
<p> <code>day days</code></p>
<dl>
<dd>Some number of days.</dl>
<p> <code>week weeks</code></p>
<dl>
<dd>Some number of weeks (days*7). </p>
<p> Note The value <code>inf</code> may be used in most places where an integer is expected to mean an infinite amount. </p>
<p> Boolean arguments may have any of the values <code>y</code>, <code>yes</code>, <code>t</code>, <code>true</code> or <code>on</code> to indicate a true state, or <code>n</code>, <code>no</code>, <code>f</code>, <code>false</code> or <code>off</code> to indicate a false state. If no argument is given, <code>true</code> is assumed.</dl>
<h3>Parameters</h3>
<p><code>org</code> <i> string</i></p>
<dl>
<dd>Default: <i>daily</i>. A descriptive name for the configuration. This string appears in the Subject line of mail reports. Each <i>Amanda</i> configuration should have a different string to keep mail reports distinct.</dl>
<p> <code>mailto</code> <i> string</i></p>
<dl>
<dd>Default: <i>operators</i>. A space separated list of recipients for mail reports.</dl>
<p> <code>dumpcycle</code> <i> int</i></p>
<dl>
<dd>Default: <i>10 days</i>. The number of days in the backup cycle. Each disk will get a full backup at least this often. Setting this to zero tries to do a full backup each run. </p>
<p> Note This parameter may also be set in a specific <code>dumptype</code> (see below). This value sets the default for all <code>dumptype</code>s so must appear in <code>amanda.conf</code> before any <code>dumptype</code>s are defined.</dl>
<p> <code>runspercycle</code> <i> int</i></p>
<dl>
<dd>Default: <i>same as dumpcycle</i>. The number of amdump runs in <code>dumpcycle</code> days. A value of 0 means the same value as <code>dumpcycle</code>. A value of -1 means guess the number of runs from the <i>tapelist</i> file, which is the number of tapes used in the last <code>dumpcycle</code> days / <code>runtapes</code>.</dl>
<p> <code>tapecycle</code> <i> int</i></p>
<dl>
<dd>Default: <i>15 tapes</i>. Typically tapes are used by <i>Amanda</i> in an ordered rotation. The <code>tapecycle</code> parameter defines the size of that rotation. The number of tapes in rotation must be larger than the number of tapes required for a complete dump cycle (see the <code>dumpcycle</code> parameter). </p>
<p> This is calculated by multiplying the number of <code>amdump</code> runs per dump cycle (<code>runspercycle</code> parameter) times the number of tapes used per run (<code>runtapes</code> parameter). Typically two to four times this calculated number of tapes are in rotation. While <i>Amanda</i> is always willing to use a new tape in its rotation, it refuses to reuse a tape until at least &#8216;<code>tapecycle</code> -1&#8242; number of other tapes have been used. </p>
<p> It is considered good administrative practice to set the <code>tapecycle</code> parameter slightly lower than the actual number of tapes in rotation. This allows the administrator to more easily cope with damaged or misplaced tapes or schedule adjustments that call for slight adjustments in the rotation order.</dl>
<p> <code>usetimestamps</code> <i> bool</i></p>
<dl>
<dd>Default: <code>Yes</code>. This option allows Amanda to track multiple runs per calendar day. The only reason one might disable it is that Amanda versions before 2.5.1 can&#8217;t read logfiles written when this option was enabled.</dl>
<p> <code>label_new_tapes</code> <i> string</i></p>
<dl>
<dd>Default: not set. When set, this directive will cause <i>Amanda</i> to automatically write an <i>Amanda</i> tape label to any blank tape she encounters. This option is DANGEROUS because when set, <i>Amanda</i> will ERASE any non-<i>Amanda</i> tapes you may have, and may also ERASE any near-failing tapes. Use with caution. </p>
<p> When using this directive, specify the template for new tape labels. The template should contain some number of contiguous &#8216;%&#8217; characters, which will be replaced with a generated number. Be sure to specify enough &#8216;%&#8217; characters that you do not run out of tape labels. Example: <code>label_new_tapes &quot;DailySet1-%%%&quot;</code></dl>
<p> <code>dumpuser</code> <i> string</i></p>
<dl>
<dd>Default: <i>amanda</i>. The login name <i>Amanda</i> uses to run the backups. The backup client hosts must allow access from the tape server host as this user via <code>.rhosts</code> or <code>.amandahosts</code>, depending on how the <i>Amanda</i> software was built.</dl>
<p> <code>printer</code> string</p>
<dl>
<dd>Printer to use when doing tape labels. See the <code>lbl-templ</code> <code>tapetype</code> option.</dl>
<p> <code>tapedev</code> string</p>
<dl>
<dd>Default: <i>null:</i>. The path name of the non-rewinding tape device. Non-rewinding tape device names often have an &#8216;n&#8217; in the name, e.g. <i>/dev/rmt/0mn</i>, however this is operating system specific and you should consult that documentation for detailed naming information. </p>
<p> If a tape changer is configured (see the <code>tpchanger</code> option), this option might not be used. </p>
<p> If the <code>null</code> output driver is selected (see the section OUTPUT DRIVERS in the <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) manpage for more information), programs such as <code>amdump</code> will run normally but all images will be thrown away. This should only be used for debugging and testing, and probably only with the <code>record</code> option set to <i>no</i>.</dl>
<p> <code>device_property</code> string string</p>
<dl>
<dd>These options can set various device properties, including block size, maximum volume usage, authentication information, hardware feature support, and more.Specifics of how properties are used are device-dependent, though some common properties are supported across multiple device drivers. </p>
<p> Both strings are quoted; the first string contains the name of the property to set, and the second contains its value. For example, to set a fixed block size of 128k, do: </p>
<pre>device_property &quot;BLOCK_SIZE&quot; &quot;131072&quot;.fi
The order in which device properties are set is as follows:
<dl><dt><dd>1.Tapetype parameters, including length, blocksize, readblocksize, file-pad, are translated into device properties and set accordingly.
</dl><dl><dt><dd>2.Device properties from any device_property configuration directives are set, in the order they appear in the configuration file.
</dl></dl>
<code>tpchanger</code> string
<dl><dt><dd>Default:
<i>none</i>. The name of the tape changer. If a tape changer is not configured, this option is not used and should be commented out of the configuration file.
If a tape changer is configured, choose one of the changer scripts (e.g.
<code>chg-scsi</code>) and enter that here.
</dl>
<code>changerdev</code> string
<dl><dt><dd>Default:
<i>/dev/null</i>. A tape changer configuration parameter. Usage depends on the particular changer defined with the
<code>tpchanger</code>
option.
</dl>
<code>changerfile</code> string
<dl><dt><dd>Default:
<i>/usr/adm/amanda/log/changer-status</i>. A tape changer configuration parameter. Usage depends on the particular changer defined with the
<code>tpchanger</code>
option.
</dl>
<code>runtapes</code> int
<dl><dt><dd>Default:
1. The maximum number of tapes used in a single run. If a tape changer is not configured, this option is not used and should be commented out of the configuration file.
If a tape changer is configured, this may be set larger than one to let
<i>Amanda</i>
write to more than one tape.
Note that this is an upper bound on the number of tapes, and
<i>Amanda</i>
may use less.
Also note that as of this release,
<i>Amanda</i>
does not support true tape overflow. When it reaches the end of one tape, the backup image
<i>Amanda</i>
was processing starts over again on the next tape.
</dl>
<code>maxdumpsize</code> int
<dl><dt><dd>Default:
<i>runtapes</i>*<i>tape_length</i>. Maximum number of bytes the planner will schedule for a run.
</dl>
<code>taperalgo</code> [first|firstfit|largest|largestfit|smallest|last]
<dl><dt><dd>Default:
<i>first</i>. The algorithm used to choose which dump image to send to the taper.
<code>first</code>
<dl><dt><dd>First in, first out.
</dl>
<code>firstfit</code>
<dl><dt><dd>The first dump image that will fit on the current tape.
</dl>
<code>largest</code>
<dl><dt><dd>The largest dump image.
</dl>
<code>largestfit</code>
<dl><dt><dd>The largest dump image that will fit on the current tape.
</dl>
<code>smallest</code>
<dl><dt><dd>The smallest dump image.
</dl>
<code>last</code>
<dl><dt><dd>Last in, first out.
</dl></dl>
<code>labelstr</code> <i> string</i>
<dl><dt><dd>Default:
<i>.*</i>. The tape label constraint regular expression. All tape labels generated (see
<code><a href="//www.systutorials.com/docs/linux/man/8-amlabel/">amlabel</a></code>(8)) and used by this configuration must match the regular expression. If multiple configurations are run from the same tape server host, it is helpful to set their labels to different strings (for example, &quot;DAILY[0-9][0-9]*&quot; vs. &quot;ARCHIVE[0-9][0-9]*&quot;) to avoid overwriting each other's tapes.
</dl>
<code>tapetype</code> <i> string</i>
<dl><dt><dd>Default:
<i>EXABYTE</i>. The type of tape drive associated with
<code>tapedev</code>
or
<code>tpchanger</code>. This refers to one of the defined
<code>tapetype</code>s in the config file (see below), which specify various tape parameters, like the
<code>length</code>,
<code>filemark</code>
size, and
<code>speed</code>
of the tape media and device.
First character of a
<code>tapetype</code>
string must be an alphabetic character
</dl>
<code>ctimeout</code> int
<dl><dt><dd>Default:
<i>30 seconds</i>. Maximum amount of time that
<code>amcheck</code>
will wait for each client host.
</dl>
<code>dtimeout</code> int
<dl><dt><dd>Default:
<i>1800 seconds</i>. Amount of idle time per disk on a given client that a
<code>dumper</code>
running from within
<code>amdump</code>
will wait before it fails with a data timeout error.
</dl>
<code>etimeout</code> int
<dl><dt><dd>Default:
<i>300 seconds</i>. Amount of time per estimate on a given client that the
<code>planner</code>
step of
<code>amdump</code>
will wait to get the dump size estimates (note: Amanda runs up to 3 estimates for each DLE). For instance, with the default of 300 seconds and four DLE's, each estimating level 0 and level 1 on client A,
<code>planner</code>
will wait up to 40 minutes for that machine. A negative value will be interpreted as a total amount of time to wait per client instead of per disk.
</dl>
<code>connect_tries</code> int
<dl><dt><dd>Default:
<i>3</i>. How many times the server will try a connection.
</dl>
<code>req_tries</code> int
<dl><dt><dd>Default:
<i>3</i>. How many times the server will resend a REQ packet if it doesn't get the ACK packet.
</dl>
<code>netusage</code> int
<dl><dt><dd>Default:
<i>8000 Kbps</i>. The maximum network bandwidth allocated to
<i>Amanda</i>, in Kbytes per second. See also the
<code>interface</code>
section.
</dl>
<code>inparallel</code> int
<dl><dt><dd>Default:
10. The maximum number of backups that
<i>Amanda</i>
will attempt to run in parallel.
<i>Amanda</i>
will stay within the constraints of network bandwidth and holding disk space available, so it doesn't hurt to set this number a bit high. Some contention can occur with larger numbers of backups, but this effect is relatively small on most systems.
</dl>
<code>displayunit</code> &quot;k|m|g|t&quot;
<dl><dt><dd>Default:
&quot;k&quot;. The unit used to print many numbers, k=kilo, m=mega, g=giga, t=tera.
</dl>
<code>dumporder</code> string
<dl><dt><dd>Default:
<i>tttTTTTTTT</i>. The priority order of each dumper:
s: smallest size
S: largest size
t: smallest time
T: largest time
b: smallest bandwidth
B: largest bandwidth</pre>
</dl>
<p> <code>maxdumps</code> int</p>
<dl>
<dd>Default: 1. The maximum number of backups from a single host that <i>Amanda</i> will attempt to run in parallel. See also the <code>inparallel</code> option. </p>
<p> Note that this parameter may also be set in a specific <code>dumptype</code> (see below). This value sets the default for all <code>dumptype</code>s so must appear in <code>amanda.conf</code> before any <code>dumptype</code>s are defined.</dl>
<p> <code>bumpsize</code> int</p>
<dl>
<dd>Default: <i>10 Mbytes</i>. The minimum savings required to trigger an automatic bump from one incremental level to the next, expressed as size. If <i>Amanda</i> determines that the next higher backup level will be this much smaller than the current level, it will do the next level. The value of this parameter is used only if the parameter <i>bumppercent</i> is set to 0. </p>
<p> The global setting of this parameter can be overwritten inside of a dumptype-definition. </p>
<p> See also the options <code>bumppercent</code>, <code>bumpmult</code> and <code>bumpdays</code>.</dl>
<p> <code>bumppercent</code> int</p>
<dl>
<dd>Default: <i>0 percent</i>. The minimum savings required to trigger an automatic bump from one incremental level to the next, expressed as percentage of the current size of the DLE (size of current level 0). If <i>Amanda</i> determines that the next higher backup level will be this much smaller than the current level, it will do the next level. </p>
<p> If this parameter is set to 0, the value of the parameter <i>bumpsize</i> is used to trigger bumping. </p>
<p> The global setting of this parameter can be overwritten inside of a dumptype-definition. </p>
<p> See also the options <code>bumpsize</code>, <code>bumpmult</code> and <code>bumpdays</code>.</dl>
<p> <code>bumpmult</code> <i> float</i></p>
<dl>
<dd>Default: 1.5. The bump size multiplier. <i>Amanda</i> multiplies <code>bumpsize</code> by this factor for each level. This prevents active filesystems from bumping too much by making it harder to bump to the next level. For example, with the default <code>bumpsize</code> and <code>bumpmult</code> set to 2.0, the bump threshold will be 10 Mbytes for level one, 20 Mbytes for level two, 40 Mbytes for level three, and so on. </p>
<p> The global setting of this parameter can be overwritten inside of a dumptype-definition.</dl>
<p> <code>bumpdays</code> <i> int</i></p>
<dl>
<dd>Default: <i>2 days</i>. To insure redundancy in the dumps, <i>Amanda</i> keeps filesystems at the same incremental level for at least <code>bumpdays</code> days, even if the other bump threshold criteria are met. </p>
<p> The global setting of this parameter can be overwritten inside of a dumptype-definition.</dl>
<p> <code>diskfile</code> <i> string</i></p>
<dl>
<dd>Default: <i>disklist</i>. The file name for the <i>disklist</i> file holding client hosts, disks and other client dumping information.</dl>
<p> <code>infofile</code> <i> string</i></p>
<dl>
<dd>Default: <i>/usr/adm/amanda/curinfo</i>. The file or directory name for the historical information database. If <i>Amanda</i> was configured to use DBM databases, this is the base file name for them. If it was configured to use text formated databases (the default), this is the base directory and within here will be a directory per client, then a directory per disk, then a text file of data.</dl>
<p> <code>logdir</code> <i> string</i></p>
<dl>
<dd>Default: <i>/usr/adm/amanda</i>. The directory for the <code>amdump</code> and <code>log</code> files.</dl>
<p> <code>indexdir</code> <i> string</i></p>
<dl>
<dd>Default <i>/usr/adm/amanda/index</i>. The directory where index files (backup image catalogues) are stored. Index files are only generated for filesystems whose <code>dumptype</code> has the <code>index</code> option enabled.</dl>
<p> <code>tapelist</code> <i> string</i></p>
<dl>
<dd>Default: <i>tapelist</i>. The file name for the active <i>tapelist</i> file. <i>Amanda</i> maintains this file with information about the active set of tapes.</dl>
<p> <code>device_output_buffer_size</code> <i> int</i></p>
<dl>
<dd>Default: 640k. Controls the amount of memory used by <i>Amanda</i> to hold data as it is read from the network or disk before it is written to the output device. Higher values may be useful on fast tape drives and optical media.</dl>
<p> <code>tapebufs</code> <i> int</i></p>
<dl>
<dd>Default: 20. This option is deprecated; use the <code>device_output_buffer_size</code> directive instead. <code>tapebufs</code> works the same way, but the number specified is multiplied by the device blocksize prior to use.</dl>
<p> <code>reserve</code> <i> number</i></p>
<dl>
<dd>Default: 100. The part of holding-disk space that should be reserved for incremental backups if no tape is available, expressed as a percentage of the available holding-disk space (0-100). By default, when there is no tape to write to, degraded mode (incremental) backups will be performed to the holding disk. If full backups should also be allowed in this case, the amount of holding disk space reserved for incrementals should be lowered.</dl>
<p> <code>autoflush</code> <i> bool</i></p>
<dl>
<dd>Default: <i>off</i>. Whether an amdump run will flush the dumps from holding disk to tape.</dl>
<p> <code>amrecover_do_fsf</code> <i> bool</i></p>
<dl>
<dd>Default: <i>on</i>. Amrecover will call amrestore with the -f flag for faster positioning of the tape.</dl>
<p> <code>amrecover_check_label</code> <i> bool</i></p>
<dl>
<dd>Default: <i>on</i>. Amrecover will call amrestore with the -l flag to check the label.</dl>
<p> <code>amrecover_changer</code> <i> string</i></p>
<dl>
<dd>Default: &#8221;. Amrecover will use the changer if you use &#8216;settape &lt;string&gt;&#8217; and that string is the same as the amrecover_changer setting.</dl>
<p> <code>columnspec</code> <i> string</i></p>
<dl>
<dd>Defines the width of columns <code>amreport</code> should use. <i>String</i> is a comma (&#8216;,&#8217;) separated list of triples. Each triple consists of three parts which are separated by a equal sign (&#8216;=&#8217;) and a colon (&#8216;:&#8217;) (see the example). These three parts specify: </p>
<dl>
<dd>1.the name of the column, which may be: </p>
<pre> Compress (compression ratio)
 Disk (client disk name)
 DumpRate (dump rate in KBytes/sec)
 DumpTime (total dump time in hours:minutes)
 HostName (client host name)
 Level (dump level)
 OrigKB (original image size in KBytes)
 OutKB (output image size in KBytes)
 TapeRate (tape writing rate in KBytes/sec)
 TapeTime (total tape time in hours:minutes)
 .fi
</dl><dl><dt><dd>2.the amount of space to display before the column (used to get whitespace between columns).
</dl><dl><dt><dd>3.the width of the column itself. If set to a negative value, the width will be calculated on demand to fit the largest entry in this column.
</dl><dl><dt><dd>Here is an example:
columnspec &quot;Disk=1:18,HostName=0:10,OutKB=1:7&quot;</pre>
<p>The above will display the disk information in 18 characters and put one space before it. The hostname column will be 10 characters wide with no space to the left. The output KBytes column is seven characters wide with one space before it.</dl>
</dl>
<p> <code>includefile</code> <i> string</i></p>
<dl>
<dd>Default: <i>none</i>. The name of an <i>Amanda</i> configuration file to include within the current file. Useful for sharing dumptypes, tapetypes and interface definitions among several configurations. Relative pathnames are relative to the configuration directory.</dl>
<p> <code>debug_auth</code> int</p>
<dl>
<dd>Default: <i>0</i>. Debug level of the auth module</dl>
<p> <code>debug_event</code> int</p>
<dl>
<dd>Default: <i>0</i>. Debug level of the event module</dl>
<p> <code>debug_holding</code> int</p>
<dl>
<dd>Default: <i>0</i>. Debug level of the holdingdisk module</dl>
<p> <code>debug_protocol</code> int</p>
<dl>
<dd>Default: <i>0</i>. Debug level of the protocol module</dl>
<p> <code>debug_planner</code> int</p>
<dl>
<dd>Default: <i>0</i>. Debug level of the planner process</dl>
<p> <code>debug_driver</code> int</p>
<dl>
<dd>Default: <i>0</i>. Debug level of the driver process</dl>
<p> <code>debug_dumper</code> int</p>
<dl>
<dd>Default: <i>0</i>. Debug level of the dumper process</dl>
<p> <code>debug_chunker</code> int</p>
<dl>
<dd>Default: <i>0</i>. Debug level of the chunker process</dl>
<p> <code>debug_taper</code> int</p>
<dl>
<dd>Default: <i>0</i>. Debug level of the taper process</dl>
<p> <code>flush-threshold-dumped</code> int</p>
<dl>
<dd>Default: <i>0</i>. <i>Amanda</i> will not begin writing data to a new volume until the amount of data on the holding disk is at least this percentage of the volume size. In other words, <i>Amanda</i> will not begin until the inequality h &lt; t &#215; d is satisfied, where h is the amount of data on the holding disk, t is the capacity of a volume, and d is this parameter, expressed as a percentage. </p>
<p> Needless to say, your holding disk must be big enough that this criterion could be satisfied. If the holding disk cannot be used for a particular dump (because, for example, there is no remaining holding space) then <i>Amanda</i> will disregard the constraint specified by this setting and start a new volume anyway. Once writing to a volume has begun, this constraint is not applied unless and until a new volume is needed. </p>
<p> The value of this parameter may not exceed than that of the <code>flush-threshold-scheduled</code> parameter.</dl>
<p> <code>flush-threshold-scheduled</code> int</p>
<dl>
<dd>Default: <i>0</i>. <i>Amanda</i> will not begin writing data to a new volume until the sum of the amount of data on the holding disk and the estimated amount of data remaining to be dumped during this run is at least this percentage of the volume size. In other words, <i>Amanda</i> will not begin until the inequality h + s &lt; t &#215; d is satisfied, where h is the amount of data on the holding disk, s is the total amount of data scheduled for this run but not dumped yet, t is the capacity of a volume, and d is this parameter, expressed as a percentage. </p>
<p> Needless to say, your holding disk must be big enough that this criterion could be satisfied. If the holding disk cannot be used for a particular dump (because, for example, there is no remaining holding space) then <i>Amanda</i> will disregard the constraint specified by this setting and start a new volume anyway. Once writing to a volume has begun, this constraint is not applied unless and until a new volume is needed. </p>
<p> The value of this parameter may not be less than that of the <code>flush-threshold-dumped</code> or <code>taperflush</code> parameters.</dl>
<p> <code>taperflush</code> int</p>
<dl>
<dd>Default: <i>0</i>. At the end of a run, <i>Amanda</i> will start a new tape to flush remaining data if there is more data on the holding disk at the end of a run than this setting allows; the amount is specified as a percentage of the capacity of a single volume. In other words, at the end of a run, <i>Amanda</i> will begin a new tape if the inequality h &lt; t &#215; f is satisfied, where h is the amount of data remaining on the holding disk from this or previous runs, t is the capacity of a volume, and f is this parameter, expressed as a percentage. </p>
<p> The value of this parameter may not exceed that of the <code>flush-threshold-scheduled</code> parameter.; <code>autoflush</code> must be set to &#8216;yes&#8217; if <code>taperflush</code> is greater than 0.</dl>
<p> <code>reserved-udp-port</code> int,int</p>
<dl>
<dd>Default: &#8211;with-udpportrange or <i>512,1023</i>. Reserved udp port that will be used (bsd, bsdudp). Range is inclusive.</dl>
<p> <code>reserved-tcp-port</code> int,int</p>
<dl>
<dd>Default: &#8211;with-low-tcpportrange or <i>512,1023</i>. Reserved tcp port that will be used (bsdtcp). Range is inclusive.</dl>
<p> <code>unreserved-tcp-port</code> int,int</p>
<dl>
<dd>Default: &#8211;with-tcpportrange or <i>1024,65535</i>. Unreserved tcp port that will be used (bsd, bsdudp). Range is inclusive.</dl>
<h2>Holdingdisk Section</h2>
<p>The <code>amanda.conf</code> file may define one or more holding disks used as buffers to hold backup images before they are written to tape. The syntax is: </p>
<pre>holdingdisk <i>name</i> {
 <i>holdingdisk-option</i> <i>holdingdisk-value</i>
 ...
}</pre>
<p><i>Name</i> is a logical name for this holding disk. </p>
<p> The options and values are: </p>
<p> <code>comment</code> <i> string</i></p>
<dl>
<dd>Default: <i>none</i>. A comment string describing this holding disk.</dl>
<p> <code>directory</code> <i> disk</i></p>
<dl>
<dd>Default: <i>/dumps/amanda</i>. The path to this holding area.</dl>
<p> <code>use</code> <i> int</i></p>
<dl>
<dd>Default: <i>0 Gb</i>. Amount of space that can be used in this holding disk area. If the value is zero, all available space on the file system is used. If the value is negative, <i>Amanda</i> will use all available space minus that value.</dl>
<p> <code>chunksize</code> <i> int</i></p>
<dl>
<dd>Default: <i>1 Gb</i>. Holding disk chunk size. Dumps larger than the specified size will be stored in multiple holding disk files. The size of each chunk will not exceed the specified value. However, even though dump images are split in the holding disk, they are concatenated as they are written to tape, so each dump image still corresponds to a single continuous tape section. </p>
<p> If 0 is specified, <i>Amanda</i> will create holding disk chunks as large as ((INT_MAX/1024)-64) Kbytes. </p>
<p> Each holding disk chunk includes a 32 Kbyte header, so the minimum chunk size is 64 Kbytes (but that would be really silly). </p>
<p> Operating systems that are limited to a maximum file size of 2 Gbytes actually cannot handle files that large. They must be at least one byte less than 2 Gbytes. Since <i>Amanda</i> works with 32 Kbyte blocks, and to handle the final read at the end of the chunk, the chunk size should be at least 64 Kbytes (2 * 32 Kbytes) smaller than the maximum file size, e.g. 2047 Mbytes.</dl>
<h2>Dumptype Section</h2>
<p>The <i>amanda.conf</i> file may define multiple sets of backup options and refer to them by name from the <i>disklist</i> file. For instance, one set of options might be defined for file systems that can benefit from high compression, another set that does not compress well, another set for file systems that should always get a full backup and so on. </p>
<p> A set of backup options are entered in a <code>dumptype</code> section, which looks like this: </p>
<pre>define dumptype <i>name</i> {
 <i>dumptype-option</i> <i>dumptype-value</i>
 ...
}</pre>
<p><i>Name</i> is the name of this set of backup options. It is referenced from the <i>disklist</i> file. </p>
<p> Some of the options in a <code>dumptype</code> section are the same as those in the main part of <i>amanda.conf</i>. The main option value is used to set the default for all <code>dumptype</code> sections. For instance, setting <code>dumpcycle</code> to 50 in the main part of the config file causes all following <code>dumptype</code> sections to start with that value, but the value may be changed on a section by section basis. Changes to variables in the main part of the config file must be done before (earlier in the file) any <code>dumptype</code>s are defined. </p>
<p> The dumptype options and values are: </p>
<p> <code>auth</code> <i> string</i></p>
<dl>
<dd>Default: <i>bsd</i>. Type of authorization to perform between tape server and backup client hosts. </p>
<p> <code>bsd</code>, bsd authorization with udp initial connection and one tcp connection by data stream. </p>
<p> <code>bsdtcp</code>, bsd authorization but use only one tcp connection. </p>
<p> <code>bsdudp</code>, like bsd, but will use only one tcp connection for all data stream. </p>
<p> <code>krb4</code> to use Kerberos-IV authorization. </p>
<p> <code>krb5</code> to use Kerberos-V authorization. </p>
<p> <code>local</code>, if the client is the server, it doesn&#8217;t require authencation setup. </p>
<p> <code>rsh</code> to use rsh authorization. </p>
<p> <code>ssh</code> to use OpenSSH authorization.</dl>
<p> <code>amandad_path</code> <i> string</i></p>
<dl>
<dd>Default: <i>$libexec/amandad</i>. Specify the amandad path of the client, only use with rsh/ssh authentification.</dl>
<p> <code>client_username</code> <i> string</i></p>
<dl>
<dd>Default: <i>CLIENT_LOGIN</i>. Specify the username to connect on the client, only use with rsh/ssh authentification.</dl>
<p> <code>bumpsize</code> int</p>
<dl>
<dd>Default: <i>10 Mbytes</i>. The minimum savings required to trigger an automatic bump from one incremental level to the next, expressed as size. If <i>Amanda</i> determines that the next higher backup level will be this much smaller than the current level, it will do the next level. The value of this parameter is used only if the parameter <i>bumppercent</i> is set to 0. </p>
<p> See also the options <code>bumppercent</code>, <code>bumpmult</code> and <code>bumpdays</code>.</dl>
<p> <code>bumppercent</code> int</p>
<dl>
<dd>Default: <i>0 percent</i>. The minimum savings required to trigger an automatic bump from one incremental level to the next, expressed as percentage of the current size of the DLE (size of current level 0). If <i>Amanda</i> determines that the next higher backup level will be this much smaller than the current level, it will do the next level. </p>
<p> If this parameter is set to 0, the value of the parameter <i>bumpsize</i> is used to trigger bumping. </p>
<p> See also the options <code>bumpsize</code>, <code>bumpmult</code> and <code>bumpdays</code>.</dl>
<p> <code>bumpmult</code> <i> float</i></p>
<dl>
<dd>Default: 1.5. The bump size multiplier. <i>Amanda</i> multiplies <code>bumpsize</code> by this factor for each level. This prevents active filesystems from bumping too much by making it harder to bump to the next level. For example, with the default <code>bumpsize</code> and <code>bumpmult</code> set to 2.0, the bump threshold will be 10 Mbytes for level one, 20 Mbytes for level two, 40 Mbytes for level three, and so on.</dl>
<p> <code>bumpdays</code> <i> int</i></p>
<dl>
<dd>Default: <i>2 days</i>. To insure redundancy in the dumps, <i>Amanda</i> keeps filesystems at the same incremental level for at least <code>bumpdays</code> days, even if the other bump threshold criteria are met.</dl>
<p> <code>comment</code> <i> string</i></p>
<dl>
<dd>Default: <i>none</i>. A comment string describing this set of backup options.</dl>
<p> <code>comprate</code> <i>float</i> [, <i>float</i> ]</p>
<dl>
<dd>Default: 0.50, 0.50. The expected full and incremental compression factor for dumps. It is only used if <i>Amanda</i> does not have any history information on compression rates for a filesystem, so should not usually need to be set. However, it may be useful for the first time a very large filesystem that compresses very little is backed up.</dl>
<p> <code>compress [client|server]</code> <i> string</i></p>
<dl>
<dd>Default: <i>client fast</i>. If <i>Amanda</i> does compression of the backup images, it can do so either on the backup client host before it crosses the network or on the tape server host as it goes from the network into the holding disk or to tape. Which place to do compression (if at all) depends on how well the dump image usually compresses, the speed and load on the client or server, network capacity, holding disk capacity, availability of tape hardware compression, etc. </p>
<p> For either type of compression, <i>Amanda</i> also allows the selection of three styles of compression. <code>Best</code> is the best compression available, often at the expense of CPU overhead. <code>Fast</code> is often not as good a compression as <code>best</code>, but usually less CPU overhead. Or to specify <code>Custom</code> to use your own compression method. (See dumptype custom-compress in example/amanda.conf for reference) </p>
<p> So the <code>compress</code> options line may be one of: </p>
<p> compress none</p>
<dl>
<dd></dl>
<p> compress client fast</p>
<dl>
<dd></dl>
<p> compress client best</p>
<dl>
<dd></dl>
<p> compress client custom</p>
<dl>
<dd>Specify <i>client_custom_compress</i> &quot;PROG&quot; </p>
<p> PROG must not contain white space and it must accept -d for uncompress.</dl>
<p> compress server fast</p>
<dl>
<dd></dl>
<p> compress server best</p>
<dl>
<dd></dl>
<p> compress server custom</p>
<dl>
<dd>Specify <i>server_custom_compress</i> &quot;PROG&quot; </p>
<p> PROG must not contain white space and it must accept -d for uncompress.</dl>
<p> Note that some tape devices do compression and this option has nothing to do with whether that is used. If hardware compression is used (usually via a particular tape device name or <code>mt</code> option), <i>Amanda</i> (software) compression should be disabled.</dl>
<p> <code>dumpcycle</code> <i> int</i></p>
<dl>
<dd>Default: <i>10 days</i>. The number of days in the backup cycle. Each disk using this set of options will get a full backup at least this of ten. Setting this to zero tries to do a full backup each run.</dl>
<p> <code>encrypt [none|client|server]</code></p>
<dl>
<dd>Default: <i>none</i>. To encrypt backup images, it can do so either on the backup client host before it crosses the network or on the tape server host as it goes from the network into the holding disk or to tape. </p>
<p> So the <code>encrypt</code> options line may be one of: </p>
<p> encrypt none</p>
<dl>
<dd></dl>
<p> encrypt client</p>
<dl>
<dd>Specify client_encrypt &quot;PROG&quot; </p>
<p> PROG must not contain white space. </p>
<p> Specify client_decrypt_option &quot;decryption-parameter&quot; Default: &quot;-d&quot; </p>
<p> decryption-parameter must not contain white space. </p>
<p> (See dumptype server-encrypt-fast in example/amanda.conf for reference)</dl>
<p> encrypt server</p>
<dl>
<dd>Specify server_encrypt &quot;PROG&quot; </p>
<p> PROG must not contain white space. </p>
<p> Specify server_decrypt_option &quot;decryption-parameter&quot; Default: &quot;-d&quot; </p>
<p> decryption-parameter must not contain white space. </p>
<p> (See dumptype client-encrypt-nocomp in example/amanda.conf for reference)</dl>
<p> Note that current logic assumes compression then encryption during backup(thus decrypt then uncompress during restore). So specifying client-encryption AND server-compression is not supported. <i>amcrypt</i> which is a wrapper of <i>aespipe</i> is provided as a reference symmetric encryption program.</dl>
<p> <code>estimate</code> <i>client|calcsize|server</i></p>
<dl>
<dd>Default: <i>client</i>. Determine the way <i>Amanda</i> does it&#8217;s estimate. </p>
<p> client</p>
<dl>
<dd>Use the same program as the dumping program, this is the most accurate way to do estimates, but it can take a long time.</dl>
<p> calcsize</p>
<dl>
<dd>Use a faster program to do estimates, but the result is less accurate.</dl>
<p> server</p>
<dl>
<dd>Use only statistics from the previous run to give an estimate, it takes only a few seconds but the result is not accurate if your disk usage changes from day to day.</dl>
</dl>
<p> <code>exclude</code> [ list|file ][[optional][ append ][ <i>string</i> ]+]</p>
<dl>
<dd>Default: <i>file</i>. There are two exclude lists, <code>exclude file</code> and <code>exclude list.</code> With <code>exclude file</code> , the <i>string</i> is a <code>GNU-tar</code> exclude expression. With <code>exclude list</code> , the <i>string</i> is a file name on the client containing <code>GNU-tar</code> exclude expressions. The path to the specified exclude list file, if present (see description of &#8216;optional&#8217; below), must be readable by the <i>Amanda</i> user. </p>
<p> All exclude expressions are concatenated in one file and passed to <code>GNU-tar</code> as an <code>&#8211;exclude-from</code> argument. </p>
<p> Exclude expressions must always be specified as relative to the head directory of the DLE. </p>
<p> With the <code>append</code> keyword, the <i>string</i> is appended to the current list, without it, the <i>string</i> overwrites the list. </p>
<p> If <code>optional</code> is specified for <code>exclude list</code>, then amcheck will not complain if the file doesn&#8217;t exist or is not readable. </p>
<p> For <code>exclude list</code>, if the file name is relative, the disk name being backed up is prepended. So if this is entered: </p>
<pre> exclude list &quot;.amanda.excludes&quot;</pre>
<p>the actual file used would be <i>/var/.amanda.excludes</i> for a backup of <i>/var</i>, <i>/usr/local/.amanda.excludes</i> for a backup of <i>/usr/local</i>, and so on.</dl>
<p> <code>holdingdisk</code> [ never|auto|required ]</p>
<dl>
<dd>Default: <i>auto</i>. Whether a holding disk should be used for these backups or whether they should go directly to tape. If the holding disk is a portion of another file system that <i>Amanda</i> is backing up, that file system should refer to a dumptype with <code>holdingdisk</code> set to <i>never</i> to avoid backing up the holding disk into itself. </p>
<p> <code>never</code>|no|false|off</p>
<dl>
<dd>Never use a holdingdisk, the dump will always go directly to tape. There will be no dump if you have a tape error.</dl>
<p> <code>auto</code>|yes|true|on</p>
<dl>
<dd>Use the holding disk, unless there is a problem with the holding disk, the dump won&#8217;t fit there or the medium doesn&#8217;t require spooling (e.g., VFS device)</dl>
<p> <code>required</code></p>
<dl>
<dd>Always dump to holdingdisk, never directly to tape. There will be no dump if it doesn&#8217;t fit on holdingdisk</dl>
</dl>
<p> <code>ignore</code> <i> boolean</i></p>
<dl>
<dd>Default: <i>no</i>. Whether disks associated with this backup type should be backed up or not. This option is useful when the <i>disklist</i> file is shared among several configurations, some of which should not back up all the listed file systems.</dl>
<p> <code>include</code> [ list|file ][[optional][ append ][ <i>string</i> ]+]</p>
<dl>
<dd>Default: <i>file</i> &quot;.&quot;. There are two include lists, <code>include file</code> and <code>include list.</code> With <code>include file</code> , the <i>string</i> is a glob expression. With <code>include list</code> , the <i>string</i> is a file name on the client containing glob expressions. </p>
<p> All include expressions are expanded by <i>Amanda</i>, concatenated in one file and passed to <code>GNU-tar</code> as a <code>&#8211;files-from</code> argument. They must start with &quot;./&quot; and contain no other &quot;/&quot;. </p>
<p> Include expressions must always be specified as relative to the head directory of the DLE. </p>
<p> Note For globbing to work at all, even the limited single level, the top level directory of the DLE must be readable by the <i>Amanda</i> user. </p>
<p> With the <code>append</code> keyword, the <i>string</i> is appended to the current list, without it, the <i>string</i> overwrites the list. </p>
<p> If <code>optional</code> is specified for <code>include list,</code> then amcheck will not complain if the file doesn&#8217;t exist or is not readable. </p>
<p> For <code>include list</code>, If the file name is relative, the disk name being backed up is prepended.</dl>
<p> <code>index</code> <i> boolean</i></p>
<dl>
<dd>Default: <i>no</i>. Whether an index (catalogue) of the backup should be generated and saved in <code>indexdir</code>. These catalogues are used by the <code>amrecover</code> utility.</dl>
<p> <code>kencrypt</code> <i> boolean</i></p>
<dl>
<dd>Default: <i>no</i>. Whether the backup image should be encrypted by Kerberos as it is sent across the network from the backup client host to the tape server host.</dl>
<p> <code>maxdumps</code> <i> int</i></p>
<dl>
<dd>Default: 1. The maximum number of backups from a single host that <i>Amanda</i> will attempt to run in parallel. See also the main section parameter <code>inparallel</code>.</dl>
<p> <code>maxpromoteday</code> <i> int</i></p>
<dl>
<dd>Default: 10000. The maximum number of day for a promotion, set it 0 if you don&#8217;t want promotion, set it to 1 or 2 if your disks get overpromoted.</dl>
<p> <code>priority</code> <i> string</i></p>
<dl>
<dd>Default: <i>medium</i>. When there is no tape to write to, <i>Amanda</i> will do incremental backups in priority order to the holding disk. The priority may be high (2), medium (1), low (0) or a number of your choice.</dl>
<p> <code>program</code> <i> string</i></p>
<dl>
<dd>Default: <i>DUMP</i>. The type of backup to perform. Valid values are <code>DUMP</code> for the native operating system backup program, and <code>GNUTAR</code> to use <code>GNU-tar</code> or to do PC backups using Samba.</dl>
<p> <code>record</code> <i> boolean</i></p>
<dl>
<dd>Default: <i>yes</i>. Whether to ask the backup program to update its database (e.g. <i>/etc/dumpdates</i> for DUMP or <i>/usr/local/var/amanda/gnutar-lists</i> for GNUTAR) of time stamps. This is normally enabled for daily backups and turned off for periodic archival runs.</dl>
<p> <code>skip-full</code> <i> boolean</i></p>
<dl>
<dd>Default: <i>no</i>. If <i>true</i> and <code>planner</code> has scheduled a full backup, these disks will be skipped, and full backups should be run off-line on these days. It was reported that <i>Amanda</i> only schedules level 1 incrementals in this configuration; this is probably a bug.</dl>
<p> <code>skip-incr</code> <i> boolean</i></p>
<dl>
<dd>Default: <i>no</i>. If <i>true</i> and <code>planner</code> has scheduled an incremental backup, these disks will be skipped.</dl>
<p> <code>starttime</code> <i> int</i></p>
<dl>
<dd>Default: <i>none</i>. Backups will not start until after this time of day. The value should be hh*100+mm, e.g. 6:30PM (18:30) would be entered as 1830.</dl>
<p> <code>strategy</code> <i> string</i></p>
<dl>
<dd>Default: <i>standard</i>. Strategy to use when planning what level of backup to run next. Values are: </p>
<p> <code>standard</code></p>
<dl>
<dd>The standard <i>Amanda</i> schedule.</dl>
<p> <code>nofull</code></p>
<dl>
<dd>Never do full backups, only level 1 incrementals.</dl>
<p> <code>noinc</code></p>
<dl>
<dd>Never do incremental backups, only full dumps.</dl>
<p> <code>skip</code></p>
<dl>
<dd>Never do backups (useful when sharing the <i>disklist</i> file).</dl>
<p> <code>incronly</code></p>
<dl>
<dd>Only do incremental dumps. <code>amadmin force</code> should be used to tell <i>Amanda</i> that a full dump has been performed off-line, so that it resets to level 1.</dl>
</dl>
<p> <code>tape_splitsize</code> <i> int</i></p>
<dl>
<dd>Default: <i>none</i>. Split dump file on tape into pieces of a specified size. This allows dumps to be spread across multiple tapes, and can potentially make more efficient use of tape space. Note that if this value is too large (more than half the size of the average dump being split), substantial tape space can be wasted. If too small, large dumps will be split into innumerable tiny dumpfiles, adding to restoration complexity. A good rule of thumb, usually, is 1/10 of the size of your tape.</dl>
<p> <code>split_diskbuffer</code> <i> string</i></p>
<dl>
<dd>Default: <i>none</i>. When dumping a split dump in PORT-WRITE mode (usually meaning &quot;no holding disk&quot;), buffer the split chunks to a file in the directory specified by this option.</dl>
<p> <code>fallback_splitsize</code> <i> int</i></p>
<dl>
<dd>Default: <i>10M</i>. When dumping a split dump in PORT-WRITE mode, if no split_diskbuffer is specified (or if we somehow fail to use our split_diskbuffer), we must buffer split chunks in memory. This specifies the maximum size split chunks can be in this scenario, and thus the maximum amount of memory consumed for in-memory splitting. The size of this buffer can be changed from its (very conservative) default to a value reflecting the amount of memory that each taper process on the dump server may reasonably consume.</dl>
<p> The following <code>dumptype</code> entries are predefined by <i>Amanda</i>: </p>
<pre>define dumptype no-compress {
 compress none
}
define dumptype compress-fast {
 compress client fast
}
define dumptype compress-best {
 compress client best
}
define dumptype srvcompress {
 compress server fast
}
define dumptype bsd-auth {
 auth bsd
}
define dumptype krb4-auth {
 auth krb4
}
define dumptype no-record {
 record no
}
define dumptype no-hold {
 holdingdisk no
}
define dumptype no-full {
 skip-full yes
} </pre>
<p>In addition to options in a <code>dumptype</code> section, one or more other <code>dumptype</code> names may be entered, which make this <code>dumptype</code> inherit options from other previously defined <code>dumptype</code>s. For instance, two sections might be the same except for the <code>record</code> option: </p>
<pre>define dumptype normal {
 comment &quot;Normal backup, no compression, do indexing&quot;
 no-compress
 index yes
 maxdumps 2
}
define dumptype testing {
 comment &quot;Test backup, no compression, do indexing, no recording&quot;
 normal
 record no
}</pre>
<p><i>Amanda</i> provides a <code>dumptype</code> named <i>global</i> in the sample <code>amanda.conf</code> file that all <code>dumptype</code>s should reference. This provides an easy place to make changes that will affect every <code>dumptype</code>.</p>
<h2>Tapetype Section</h2>
<p>The <code>amanda.conf</code> file may define multiple types of tape media and devices. The information is entered in a <code>tapetype</code> section, which looks like this in the config file: </p>
<pre>define tapetype <i>name</i> {
 <i>tapetype-option</i> <i>tapetype-value</i>
 ...
}</pre>
<p><i>Name</i> is the name of this type of tape medium/device. It is referenced from the <code>tapetype</code> option in the main part of the config file. </p>
<p> The tapetype options and values are: </p>
<p> <code>comment</code> <i> string</i></p>
<dl>
<dd>Default: <i>none</i>. A comment string describing this set of tape information.</dl>
<p> <code>filemark</code> <i> int</i></p>
<dl>
<dd>Default: <i>1 kbytes</i>. How large a file mark (tape mark) is, measured in kbytes. If the size is only known in some linear measurement (e.g. inches), convert it to kbytes using the device density.</dl>
<p> <code>length</code> <i> int</i></p>
<dl>
<dd>Default: <i>2000 kbytes</i>. How much data will fit on a tape. </p>
<p> Note that this value is only used by <i>Amanda</i> to schedule which backups will be run. Once the backups start, <i>Amanda</i> will continue to write to a tape until it gets an error, regardless of what value is entered for <code>length</code> (but see the section OUTPUT DRIVERS in the <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) manpage for exceptions).</dl>
<p> <code>blocksize</code> <i> int</i></p>
<dl>
<dd>Default: <i>32 kbytes</i>. How much data will be written in each tape record expressed in KiloBytes. The tape record size (= blocksize) can not be reduced below the default 32 KBytes. The parameter blocksize can only be raised if <i>Amanda</i> was compiled with the configure option &#8211;with-maxtapeblocksize=N set with &quot;N&quot; greater than 32 during <code>configure</code>.</dl>
<p> <code>readblocksize</code> <i> int</i></p>
<dl>
<dd>Default: (<i>from configure &#8211;with-maxtapeblocksize</i>). How much data will be read in each tape record expressed in KiloBytes. Some hardware require a value not too large, and some require it to be equal to the blocksize. It is useful if you configured amanda with a big &#8211;with-maxtapeblocksize and your hardware don&#8217;t work with a value that big.</dl>
<p> <code>file-pad</code> <i> boolean</i></p>
<dl>
<dd>Default: <i>true</i>. If true, every record, including the last one in the file, will have the same length. This matches the way <i>Amanda</i> wrote tapes prior to the availability of this parameter. It may also be useful on devices that only support a fixed blocksize. </p>
<p> Note that the last record on the tape probably includes trailing null byte padding, which will be passed back to <code>gzip</code>, <code>compress</code> or the restore program. Most programs just ignore this (although possibly with a warning). </p>
<p> If this parameter is false, the last record in a file may be shorter than the block size. The file will contain the same amount of data the dump program generated, without trailing null byte padding. When read, the same amount of data that was written will be returned.</dl>
<p> <code>speed</code> <i> int</i></p>
<dl>
<dd>Default: <i>200 bps</i>. How fast the drive will accept data, in bytes per second. This parameter is NOT currently used by <i>Amanda</i>.</dl>
<p> <code>lbl-templ</code> <i> string</i></p>
<dl>
<dd>A PostScript template file used by <code>amreport</code> to generate labels. Several sample files are provided with the <i>Amanda</i> sources in the <i>example</i> directory. See the <code><a href="/docs/linux/man/8-amreport/">amreport</a></code>(8) man page for more information.</dl>
<p> In addition to options, another <code>tapetype</code> name may be entered, which makes this <code>tapetype</code> inherit options from another <code>tapetype</code>. For instance, the only difference between a DLT4000 tape drive using Compact-III tapes and one using Compact-IV tapes is the length of the tape. So they could be entered as: </p>
<pre>define tapetype DLT4000-III {
 comment &quot;DLT4000 tape drives with Compact-III tapes&quot;
 length 12500 mbytes # 10 Gig tapes with some compression
 filemark 2000 kbytes
 speed 1536 kps
}
define tapetype DLT4000-IV {
 DLT4000-III
 comment &quot;DLT4000 tape drives with Compact-IV tapes&quot;
 length 25000 mbytes # 20 Gig tapes with some compression
}</pre>
<h2>Interface Section</h2>
<p>The <code>amanda.conf</code> file may define multiple types of network interfaces. The information is entered in an <code>interface</code> section, which looks like this: </p>
<pre>define interface <i>name</i> {
 <i>interface-option</i> <i>interface-value</i>
 ...
}</pre>
<p><i>name</i> is the name of this type of network interface. It is referenced from the <i>disklist</i> file. </p>
<p> Note that these sections define network interface characteristics, not the actual interface that will be used. Nor do they impose limits on the bandwidth that will actually be taken up by <i>Amanda</i>. <i>Amanda</i> computes the estimated bandwidth each file system backup will take based on the estimated size and time, then compares that plus any other running backups with the limit as another of the criteria when deciding whether to start the backup. Once a backup starts, <i>Amanda</i> will use as much of the network as it can leaving throttling up to the operating system and network hardware. </p>
<p> The interface options and values are: </p>
<p> <code>comment</code> <i> string</i></p>
<dl>
<dd>Default: <i>none</i>. A comment string describing this set of network information.</dl>
<p> <code>use</code> <i> int</i></p>
<dl>
<dd>Default: <i>8000 Kbps</i>. The speed of the interface in Kbytes per second.</dl>
<p> In addition to options, another <code>interface</code> name may be entered, which makes this <code>interface</code> inherit options from another <code>interface</code>. At the moment, this is of little use.</p>
<h2>Author</h2>
<p>James da Silva, &lt;jds [at] amanda.org&gt;: Original text </p>
<p> Stefan G. Weichinger, &lt;sgw [at] amanda.org&gt;, maintainer of the <i>Amanda</i>-documentation: XML-conversion, major update, splitting</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-client-conf/">amanda-client.conf</a></code>(5), <code><a href="/docs/linux/man/8-amcrypt/">amcrypt</a></code>(8), <code><a href="/docs/linux/man/1-aespipe/">aespipe</a></code>(1), : <a rel="nofollow" href="http://wiki.zmanda.com">http://wiki.zmanda.com</a> </p>
