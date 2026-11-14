---
title: "collectl(1)"
name: "collectl"
section: "1"
letter: "c"
url: "/docs/linux/man/1-collectl/"
description: "collectl – Collects data that describes the current system status."
---

<h2>NAME</h2>
<p> collectl &#8211; Collects data that describes the current system status. </p>
<h2>SYNOPSIS</h2>
<p> Record Mode &#8211; read data from live system and write to file or display on terminal </p>
<p> <code>collectl [-f file] [options]</code> </p>
<p> Playback Mode &#8211; read data from one or more raw data files and display on terminal </p>
<p> <code>collectl -p file1 [file2 &#8230;] [options]</code> </p>
<h2>OPTIONS</h2>
<p> Record Mode </p>
<p> In this mode data is taken from a <code>live</code> system and either displayed on the terminal or written to one or more files or a socket. </p>
<p> <code>&#8211;align</code></p>
<dl>
<dt>
<dd> If the HiRes modules is present, <code>collectl</code> sample monitoring will be aligned such that a sample will always be taken at the top of a minute (this does NOT mean the first sample will occur then) so that all instances of collectl running on any systems which have their clocks synchronized will all take samples at the same time. Furthermore, if one is doing process monitoring, those samples will also be taken at the top of the minute and so can delay the start of sampling up to 2 full process monitoring intervals.</dl>
<p> <code>&#8211;all</code></p>
<dl>
<dt>
<dd> Collect summary data for ALL subsystems except slabs, since slab monitoring requires a different monitoring interval. This also means you won&#8217;t get any detail data which also includes processes and environmementals. You can use this switch anywhere -s can be used but not both together. If the system supports lustre and/or interconnect monitoring those statistics will be provided but the warnings produced when they are not available you try to select them with -s will not be displayed.</dl>
<p> <code>&#8211;ALL</code></p>
<dl>
<dt>
<dd> This is actually a superset of &#8211;all by adding detail statistics as well with the exception of TCP details when displaying to a terminal since those are only available with -P or -f.</dl>
<p> <code>-A, &#8211;address address[:port[:timeout]] | server[:port]</code></p>
<dl>
<dt>
<dd> In the first form, one specifies an address, optional port and timeout (the first colon is required to specify timeout for default port). All data is then written to that socket prefaced with the current host name at the named address and port until the socket is closed, at which time collectl will exit. </p>
<p> In the second form one enters the text &quot;server&quot; and optional port. In this form, collectl runs as a server, waiting for a connection and once established writes data on that socket. The key difference here is if the client exists collectl keeps running and will again look for a new connection, allowing it to survive client restarts or crashes. </p>
<p> The default port is set at 2655 but can be changed &#8211; see collectl.conf. </p>
<p> In both forms, one can additionally request local data logging by specifying a combination of -P and -f. See <code>man collectl-logging</code> for more details.</dl>
<p> <code>&#8211;comment string</code></p>
<dl>
<dt>
<dd> Add the specified string to the end of the headers in the data files. If any embedded spaces be sure to quote it. This can be very useful when doing characterizations or benchmarking and you&#8217;re frequently changing system/application parameters and restarting collectl between tests.</dl>
<p> <code>-C, &#8211;config filename</code></p>
<dl>
<dt>
<dd> Name/location of the collectl configuration file. If not specified, <code>collectl</code> searches for <code>collectl.conf</code> first in /etc (the default), then in the same directory the <code>collectl</code> executable is in, and finally the current working directory.</dl>
<p> <code>-c, &#8211;count Samples</code></p>
<dl>
<dt>
<dd> The number of samples to record. This is one way of 3 ways of describing how long collectl should run (see <code>-r</code> and <code>-R</code> ). Note that these 3 switches are mutually exclusive.</dl>
<p> <code>-D, &#8211;daemon</code></p>
<dl>
<dt>
<dd> Run <code>collectl</code> as a daemon, primarily used when starting as a service. One caveat about this mode is you can only run one copy.</dl>
<p> <code>&#8211;export file[,options]</code></p>
<dl>
<dt>
<dd> This requests that collectl does not print anything on the terminal (or send it to a socket) using the standard brief/verbose/plot formats. Instead it executes a perl &quot;require&quot; on the named file, using an extension of ph if not specified. It first looks in the current directory and if not there the directory the executable is in. It then calls the function &quot;file&quot;Init(options) towards the beginning of collectl and again as simply &quot;file&quot;(@options) to generate the exported formatted output. See the online documentation on Exporting Custom Output and Logging for more details.</dl>
<p> <code>-f, &#8211;filename Filename</code></p>
<dl>
<dt>
<dd> This is the name of a file to write the output to. For details on how the output files are named, see the <code>File</code> <code>Naming</code> section of the documentation on collectl.sourceforge.net OR /usr/share/doc/collectl/FileNaming.html </p>
</dl>
<p> <code>-F, &#8211;flush seconds</code></p>
<dl>
<dt>
<dd> Flush output buffers after this number of seconds. This is equivalent to issuing <code>kill -s USR1</code> at the same frequency (but a lot easier!). If 0, a flush will occur every data collection interval.</dl>
<p> <code>&#8211;grep pattern</code></p>
<dl>
<dt>
<dd> The main purpose of this switch is for those users who have discovered there is some data in the raw files that never appears in any display and have taken to displaying it themselves with grep. Unfortunately this method does not include timestamps and so makes it difficult to interpret the results. Even if you include the timestamp from the file it is in UTC and so needs to be translated to be of any real value. This switch does just that and then some. </p>
<p> Specifically, it allows you to playback a file and instead of processing it normally it simply searches for any entries that match the perl pattern and reports those lines prefaced with time stamps. You can optionally change the time format with the usual -o options and can even select the timeframe with &#8211;from and &#8211;thru.</dl>
<p> <code>&#8211;home</code></p>
<dl>
<dt>
<dd> Always start the display for the current interval at the top of the screen also known as the home position (non-plot format only). This generates a real-time, continously refreshing display when the data fits on a single screen.</dl>
<p> <code>&#8211;import file1[,options][:file2[,options]&#8230;]</code></p>
<dl>
<dt>
<dd> This loads the named files and executes callbacks to them, which is the API mechanism for importing additional metrics into collectl. See the webpage on the API for further detail. </p>
<p> Since these files also include instructions for how to report the output in all the various forms, you will also need to include &#8211;import during playback. Finally, since the default is to seamlessly include imported data with everything else collectl reports, if you ONLY want to display imported data you much explicitly deselect all other subsystems either by including -s- (note the trailing minus sign) followed by all the subsystems were recorded OR simply say -s-all.</dl>
<p> <code>-i, &#8211;interval interval[:interval2[:interval3]]</code></p>
<dl>
<dt>
<dd> This is the sampling interval in seconds. The default is 10 seconds when run as a daemon and 1 second otherwise. The process subsystem and slabs (-sY and -sZ) are sampled at the lower rate of <code>interval2.</code> Environmentals (-sE), which only apply to a subset of hardware, are sampled at <code>interval3.</code> Both <code>interval2</code> and <code>interval3,</code> if specified, must be an even multiple of <code>interval1.</code> The daemon default is -i10:60:300 and all other modes are -i1:60:300. To sample only processes once every 10 seconds use -i:10.</dl>
<p> <code>&#8211;nohup</code></p>
<dl>
<dt>
<dd> Whenever collectl finishes a data collection interval, it checks to see if the starting parent has exited. This is to prevent the case in which someone might start a copy of collectl and then the process dies and collectl keeps running. If that is the behavior someone actually intends, they should start collectl with &#8211;nohup. </p>
<p> NOTE &#8211; when running as a daemon, &#8211;nohup is implied.</dl>
<p> <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Whenever collectl wants to tell the user something, it assigns a category to it such as Informational, Warning, Error or Fatal. When run with -m, all messages are displayed for the user and if logging data to a file with -f, these messages are also sent to a log file which is in the data collection directory and has an extenion of &quot;log&quot;. However, if -m is not specified Informational messages (such as collectl starting or stopping) are not reported on the terminal but the other 3 are. Sometimes the warnings can be annoying and one can suppress these with &#8211;quiet though they will still be written to the message log in -f. You cannot suppress Error or Fatal errors.</dl>
<p> <code>-r, &#8211;rolllogs time[[,days[:months]][,minutes]]</code></p>
<dl>
<dt>
<dd> When selected, collectl runs indefinately (or at least until the system reboots). The maximum number of raw and/or plot files that will be retained (older ones are automatically deleted) is controlled by the <code>days</code> field, the default is 7. When -m is also specified to direct collectl to write messages to a log file in the logging directory, the number of months to retain those logs is controlled by the <code>months</code> field and its default is 12. The <code>increment</code> field which is also optional (but is position dependent) specifies the duration of an individual collection file in minutes the default of which is 1440 or 1 day.</dl>
<p> <code>&#8211;rawdskfilt</code></p>
<dl>
<dt>
<dd> This switch overrides the DiskFilter setting in collectl.conf and explicitly defines a perl regx expression against which records from /prod/diskstats are selected for processing. When there are a lot of disks to process, this can be a handy way to reduce the amount of data collected and actually improve performance since there are less patterns to match each input record against. Just remember that unlike &#8211;dskfilt which only filters during display, records filtered with this switch are never even recorded and so lost forever. </p>
<p> You can optionally specify your filter with a leading plus-sign which tells collectl to just add your filter to the default specification. Care should be taken here as longer filters will slightly increase overhead and with a lot of disks and/or shorter monitoring intervals can add up. </p>
<p> As a side benefit of this switch, if you really want to look at partition level stats you can do so by leaving off the trailing space in the default pattern. </p>
<p> One must be also be careful in selecting the correct pattern since it&#8217;s easy to get it wrong and you may end up collecting the WRONG data! To verify you are collecting what you think you are, make a test run using -d4 to see the raw data being recorded in real-time.</dl>
<p> <code>&#8211;rawdskignore</code></p>
<dl>
<dt>
<dd> This is the opposite of the rawdskfilt switch. When specified any disks listed are completely ignored and will not appear in the raw file. Typically this switch is useful when you&#8217;re only interested in recording a subset of disk statistics.</dl>
<p> <code>&#8211;rawnetfilt</code></p>
<dl>
<dt>
<dd> This works just like &#8211;rawdskfilt except it applies to networks. Unlike disk filtering which has an explicit default pattern, the default for network filtering is to simply record all network data from /proc/net/dev. </p>
<p> The -d4 switch also works here, as well as everywhere, to see the raw data as it is being collected.</dl>
<p> <code>&#8211;rawnetignore</code></p>
<dl>
<dt>
<dd> This is the opposite of the rawnetfilt switch and works just like the rawdskignore switch. When specified any networks listed are ignored and will not appear in the raw file. Typically this switch is useful when you&#8217;re only interested in recording a subset of network statistics.</dl>
<p> <code>&#8211;rawtoo</code></p>
<dl>
<dt>
<dd> Only available in conjunction with -P, this switch causes the creation/logging of raw data in addition to plottable data. While this may seem excessive, keep in mind that unlike plottable data, raw data can be played back with different switches potentially providing more details. The overhead to write out this additional data is minimal, the only real cost being that of extra disk space.</dl>
<p> <code>-R, &#8211;runas uid[:gid]</code></p>
<dl>
<dt>
<dd> This switch only works when running in daemon mode and so must be specified in the DaemonCommands line. Its presence will cause collectl to write the collectl.pid file into the same directory as its other output files as specified by -f, since /var/run does not normally grant non-privileged users write access. Furthermore, the ownership of that directory must match the specified ownership since collectl needs to write ALL it&#8217;s files to that directory and can no longer assume global permissions when run as root. </p>
<p> This WILL also require manually modifying /etc/init.d/collectl to change the PIDFILE variable to point to the same directory which the -f switch in the DaemonCommands line of collectl.conf points to. </p>
<p> As a final note of caution, since this mechanism changes where collectl reads/writes its pid file, once you start using &#8211;runas, all calls to run collectl as a daemon must use it or it may be confused and exhibit unpredictable behavior.</dl>
<p> <code>-R, &#8211;runtime duration</code></p>
<dl>
<dt>
<dd> Specify the duration of data collection where the duration is a number followed by one of <code>wdhms,</code> indicating how many weeks, days, hours, minutes or seconds the collection is to be taken for.</dl>
<p> <code>&#8211;sep separator</code></p>
<dl>
<dt>
<dd> Specify the plot format separator &#8211; default is a space. If this is a numeric field it is interpretted as the decimal value of the associated ASCII character code. Otherwise it is interpretted as the character itself. In other words, &quot;&#8211;sep :&quot; sets the separator character to a colon and &quot;&#8211;sep 9&quot; sets it to a horizontal tab. &quot;&#8211;sep 58&quot; would also set it to a colon.</dl>
<p> <code>&#8211;tworaw</code></p>
<dl>
<dt>
<dd> The switches -G and &#8211;group have been replaced by &#8211;rawtoo, which is more rescriptive of its function. When specified, it tells collectl to treat process and slab data as an entirely separate group of raw files, named with the extention &quot;rawp&quot;. These separate files can be played back and processed just like any other collectl raw files and in fact one can even play back both at the same time if that is what is desired. The only real purpose of this switch is that on some systems with many processes, it is possible to generate huge raw files (some have been observerd to be &gt;250MB!) and while collectl will happily play back/process these files it can take a long time. By using the &#8211;tworaw switch one still gets a huge rawp file, but the normal raw file is a much more manageable size and as a result will faster to process then when all data is combined into the same file.</dl>
<p> Playback Mode </p>
<p> In this mode, data is read from one or more data files that were generated in Record Mode </p>
<p> <code>&#8211;export Filename</code></p>
<dl>
<dt>
<dd> When playing back a file, use this switch to create an identical raw file differing only in the timeframe being convered, so naturally one must also include &#8211;from, &#8211;thru or both. Further, since the resultant file will contain the exact same raw data you cannot select a subset using -s. This switch is actually intended for a support function for situations where somone is having problems playing back a file and a subset of the original raw file that covers the problem time has been requested, hopefully allowing a significantly file to be posted or emailed.</dl>
<p> <code>&#8211;extract filename</code></p>
<dl>
<dt>
<dd> If specified, rather than actually play back the file specified with -p, ALL raw data between the date ranges is selected and a subset of that raw file created. The rules for how to interpret the filename are the same as used for -f.</dl>
<p> <code>-f, &#8211;filename filename</code></p>
<dl>
<dt>
<dd> If specified, this is the name of a file or directory to write the output to (rather than the terminal). See the description for details on the format of this field. This requires the -P flag as well.</dl>
<p> <code>&#8211;from time range</code></p>
<dl>
<dt>
<dd> Play back data starting with this time, which may optionally include the ending time as well, which is of the format of [date:]time[-[date:]time]. The leading 0 of the hour is optional and if the seconds field is not specified is assumed to be 0. If no dates specified the time(s) apply to each file specified by -P. Otherwise the time(s) only apply to the first/last dates and any files between those dates will have all their data reported.</dl>
<p> <code>&#8211;full</code></p>
<dl>
<dt>
<dd> Full mode is actually a superset of &#8211;verbose and if selected will force &#8211;verbose. It will also force the RECORD separator to be printed for every interval even if only a single subsystem was requested and to include the actual subsystems that follow following the utc timestamp as a parsing aid for those who may wish to parse the text output rather than the plot data.</dl>
<p> <code>&#8211;offsettime seconds</code></p>
<dl>
<dt>
<dd> This field originally was used before collectl reported the timezone in the file headers and allowed one to compensate. Since then it is rarely needed except in two possible cases, one in which data on two systems is to be compared and they weren&#8217;t synchonized with ntp. This allows all the times to be reported as shifted by some number of seconds. The other case (and this is very rare) is when a clock had changed in the middle of a sample and will not be converted correctly. When this happens one may have to play back the samples in pieces and manually set the time offset.</dl>
<p> <code>&#8211;passwd filename</code></p>
<dl>
<dt>
<dd> When reporting usernames associated with a UID, use this file for the mapping. This is particularly important on systems running NIS where this are no user names in /etc/passwd.</dl>
<p> <code>-p, &#8211;playback Filename</code></p>
<dl>
<dt>
<dd> Read data from the specified <code>playback</code> file(s), noting that one can use wildcards in the filename if quoted (if playing back multiple files to the terminal you probably want to include -m to see the filenames as they are processed). The filename must either end in <code>raw</code> or <code>raw.gz.</code> As an added feature, since people sometimes automate the running of this option and don&#8217;t want to hard code a date, you can specify the string YESTERDAY or TODAY and they will be replaced in the filename string by the appropriate date.</dl>
<p> <code>&#8211;pname name</code></p>
<dl>
<dt>
<dd> By default, collectl uses the file /var/run/collectl.pid to indicate the pid of the running instance of collectl and prevent multiple copies from being run. If you DO want to run a second copy, this switch will cause collectl to change its process name to collectl-name and use that name as the associated pid file as well.</dl>
<p> <code>&#8211;procanalyze</code></p>
<dl>
<dt>
<dd> When specified and there is process data in the raw file, a summary file will be generated with one entry unique process containing such things as the total cpu consumed for both user and system, min/max utilization of various memory types, total page faults and several others.</dl>
<p> <code>&#8211;slabanalyze</code></p>
<dl>
<dt>
<dd> When specified and there is slab data in the raw file, a summary file will be generated with one entry unique slab containing data on physical memory usage by that slab.</dl>
<p> <code>&#8211;thru time</code></p>
<dl>
<dt>
<dd> Time thru which to play back a raw file. See &#8211;from for more</dl>
<p> Common Switches &#8211; both record and playback modes </p>
<p> <code>-d, &#8211;debug debug</code></p>
<dl>
<dt>
<dd> Control the level of debugging information, not typically used. For details see the source code.</dl>
<p> <code>-h, &#8211;help, -x, &#8211;helpext, -X, &#8211;helpall</code></p>
<dl>
<dt>
<dd> Display standard, extended help message (which doesn&#8217;t include the optional displays such as &#8211;showoptions, &#8211;showsubsys, &#8211;showsubopts, &#8211;showtopopts) or everything.</dl>
<p> <code>&#8211;hr, &#8211;headerrepeat num</code></p>
<dl>
<dt>
<dd> Sets the number of intervals to display data for before repeating the header. A value -1 will prevent any headers from being displayed and a value of 0 will cause only a single header to be displayed and never repeated.</dl>
<p> <code>&#8211;iosize</code></p>
<dl>
<dt>
<dd> In brief mode, include iosize with disk, infiniband and network data.</dl>
<p> <code>-l, &#8211;limits limit</code></p>
<dl>
<dt>
<dd> Override one or more default exception limits. If more than one limit they must be separated by hyphens. Current values are: </p>
<p> <code>SVC:value</code></p>
<dl>
<dt>
<dd> Report partition activity with Service times &gt;= 30 msec</dl>
<p> <code>IOS:value</code></p>
<dl>
<dt>
<dd> Report device activity with 10 or more reads or writes per second</dl>
<p> <code>LusKBS:value</code></p>
<dl>
<dt>
<dd> Report client or OSS activity greater than limit. Only applies to Client Summary or OSS Detail reporting. [default=100000]</dl>
<p> <code>LusReints:value</code></p>
<dl>
<dt>
<dd> Report MDS activity with Reint greater than limit. Only applies to MDS Summary reporting. [default=1000]</dl>
<p> <code>AND</code></p>
<dl>
<dt>
<dd> Both the IOS and SCV limits must be reached before a device is reported. This is the default value and is only included for completeness.</dl>
<p> <code>OR</code></p>
<dl>
<dt>
<dd> Report device activity if either IOS or SVC thresholds are reached.</dl>
<p> <code>-L, &#8211;lustsvcs [c|m|o][:seconds]</code></p>
<dl>
<dt>
<dd> This switch limits which servics lustre checks for and the frequency of those checks. For more information see the man page collectl-lustre.</dl>
</dl>
<p> <code>-m, &#8211;messages</code></p>
<dl>
<dt>
<dd> Write status to a monthly log file in the same directory as the output file (requires -f to be specified as well). The name of the file will be <code>collectl-yyyymm.log</code> and will track various messages that may get generated during every run of <code>collectl.</code></dl>
<p> <code>-N, &#8211;nice</code></p>
<dl>
<dt>
<dd> Set priority to a <code>nicer</code> one of 10. </p>
</dl>
<p> <code>-o, &#8211;options Options</code></p>
<dl>
<dt>
<dd> These apply to the way output is displayed OR written to a plot file. They do not effect the way data is selected for recording. Most of these switches work in both record as well as playback mode. If you&#8217;re not sure, just try it. </p>
<p> <code>1</code></p>
<dl>
<dt>
<dd> Data in plotting format should use 1 decimal point of precision as appropriate.</dl>
<p> <code>2</code></p>
<dl>
<dt>
<dd> Data in plotting format should use 2 decimal points of precision as appropriate.</dl>
<p> <code>a</code></p>
<dl>
<dt>
<dd> Always append data to an existing plot file. By default if a plot file exists, the playback file will be skipped as a way of assuring it is associated with a single recorded file. This switch overrides that mechanism allowing muliple recorded files to be processed and written to a single plot file.</dl>
<p> <code>c</code></p>
<dl>
<dt>
<dd> Always open newly named plot fies in <code>create</code> mode, overwriting any old ones that may already exists. If one processes multiple files for the same day in <code>append</code> mode multiple times, the same data will be appended to the same file mulitple times. This assures a new file is created at the start of the processing.</dl>
<p> <code>d</code></p>
<dl>
<dt>
<dd> For use with terminal output and brief mode. Preceed each line with a date/time stamp, the date being in mm/dd format. This option can also be applied to plot formatit which will cause the date portion to also be displayed in this format as opposed to D format.</dl>
<p> <code>D</code></p>
<dl>
<dt>
<dd> For use with terminal output and brief mode. Preceed each line with a date/time stamp, the date being in yyyymmdd format.</dl>
<p> <code>g</code></p>
<dl>
<dt>
<dd> For use with terminal output and brief mode. When displaying values of 1G or greater there is limited precision for 1 digit values. This options provides a way to display additional digits for more granularity by substituting a &quot;g&quot; for the decimal point rather than the trailing &quot;G&quot;.</dl>
<p> <code>G</code></p>
<dl>
<dt>
<dd> For use with terminal output and brief mode. This is similar to &quot;g&quot; but preserves the trailing &quot;G&quot; by sacrificing a digit of granularity.</dl>
<p> <code>m</code></p>
<dl>
<dt>
<dd> Whenever times are reported in plot format, in the normal terminal reporting format at the bginning of each interval or when when one of the time reporting options (d, D, T or U is selected), append the milliseconds to the time.</dl>
<p> <code>n</code></p>
<dl>
<dt>
<dd> Where appropriate, data such as disk KBs or transfers are normalized to units per second by taking the change in a counter and dividing by the number of seconds in that interval. In the case of CPUs, utilization (calculated in jiffies) is normalized as a percentage of the interval. </p>
<p> Normalization can be disabled via this option, the result being the reported values are not divided by the duration of the interval. This can be particulary useful for reporting values that are &lt; 1/2 the sampling, which will be rounded to 0.</dl>
<p> <code>T</code></p>
<dl>
<dt>
<dd> For use with terminal output and brief mode, preceeds each line with a time stamp.</dl>
<p> <code>u</code></p>
<dl>
<dt>
<dd> Create plot files with unique names by include the starting time of a colletion in the name. This forces multiple collections taken the same day to be written to multiple files.</dl>
<p> <code>-U or &#8211;utc</code></p>
<dl>
<dt>
<dd> In plot format only, report timestamps in Coordinated Universal time which is more commonly know as UTC.</dl>
<p> <code>x</code></p>
<dl>
<dt>
<dd> Report only exception records for selected subsystems. Exception reporting also requires &#8211;verbose. Currently this only applies to disk detail and Lustre server information so one must select at least -s D, l or L for this to apply. If writing to a detail file, this data will go into a separate file with the extension <code>X</code> appended to the regular detail file name.</dl>
<p> <code>X</code></p>
<dl>
<dt>
<dd> Report both exceptions as well as all details for selected subsystems, for -s D, l or L only.</dl>
<p> <code>z</code></p>
<dl>
<dt>
<dd> If the compression library has been installed, all output files will be compressed by default. This switch tells collectl not to compress any plottable files. If collectl tries to compress but cannot because the library hasn&#8217;t been installed, it will generate a warning which can be suppressed with this switch.</dl>
</dl>
<p> <code>-P, &#8211;plot</code></p>
<dl>
<dt>
<dd> Generate output in plot format. This format is space separated data which consists of a header (prefaced with a # for easy identification by an analysis program as well as identifying it as a comment for programs, such as gnuplot, which honor that convention). When written to disk, which is the typical way this option is used, <code>summary</code> data elements are written to the <code>tab</code> file and the <code>detail</code> elements written to one or more files, one per detail subsystem. If -f is not specified, all output is sent to the terminal. Output is always one line per sampling interval.</dl>
<p> <code>&#8211;stats</code></p>
<dl>
<dt>
<dd> This switch will cause brief data to be reported as both totals and averages after processing one or more files for the same day or in playback mode.</dl>
<p> <code>&#8211;statopts option(s)</code></p>
<dl>
<dt>
<dd> This switch controls the way brief stats are reported, the default is to report the totals once, at the end of a day&#8217;s worth of raw files, if more than one. </p>
<p> a &#8211; include averages along with totals<br />
 i &#8211; include the interval data itself, which is the equivalent of -oA<br />
 s &#8211; print summary stats at the end of each file processed even if more than one per day</dl>
<p> <code>-s, &#8211;subsys subsystem</code></p>
<dl>
<dt>
<dd> This field controls which subsystem data is to be collected or played back. The default for collecting data is &quot;cdn&quot;, which stands for CPU, Disk and Network summary data and the default for playback is everthing that was collected. </p>
<p> The rules for displaying results vary depending on the type of data selected. If you write data for CPUs and DISKs to a raw file and play it back with -sc, you will only see CPU data. If you play it back with -scm you will still only see CPU data since memory data was not collected. However, when used with -P, collectl will always honor the subsystems specified with this switch so in the previous example you will see CPU data plus memory data of all 0s. To see the current set of default subsystems, which are a subset of this full list, use -h. </p>
<p> You can also use + or &#8211; to add or subtract subsystems to/from the default values. For example, &quot;-s-cdn+N&quot;&lt; will remove cpu, disk and network monitoring from the defaults while adding network detail. </p>
<p> Refer to data definitions on the sourceforge website OR in /usr/share/collectl/doc/collectl-xxx to see complete descriptions of the data returned. </p>
<p> SUMMARY SUBSYSTEMS </p>
<p> b &#8211; buddy info (memory fragmentation)<br />
 c &#8211; CPU<br />
 d &#8211; Disk<br />
 f &#8211; NFS V3 Data<br />
 i &#8211; Inode and File System<br />
 j &#8211; Interrupts<br />
 l &#8211; Lustre<br />
 m &#8211; Memory<br />
 n &#8211; Networks<br />
 s &#8211; Sockets<br />
 t &#8211; TCP<br />
 x &#8211; Interconnect<br />
 y &#8211; Slabs (system object caches) </p>
<p> DETAIL SUBSYSTEMS </p>
<p> This is the set of <code>detail</code> data from which in most cases the corresponding summary data is derived. There are currently 2 types that do not have corresponding summary data and those are &quot;Environmental&quot; and &quot;Process&quot;. So, if one has 3 disks and chooses <code>-sd,</code> one will only see a single total taken across all 3 disks. If one chooses <code>-sD,</code> individual disk totals will be reported but no totals. Choosing <code>-sdD</code> will get you both. </p>
<p> C &#8211; CPU<br />
 D &#8211; Disk<br />
 E &#8211; Environmental data (fan, power, temp), via ipmitool<br />
 F &#8211; NFS Data<br />
 J &#8211; Interrupts<br />
 L &#8211; Lustre OST detail OR client Filesystem detail<br />
 M &#8211; Memory node data, which is also known as numa data<br />
 N &#8211; Networks<br />
 T &#8211; 65 TCP counters only available in plot format<br />
 X &#8211; Interconnect<br />
 Y &#8211; Slabs (system object caches)<br />
 Z &#8211; Processes</dl>
<p> <code>&#8211;showheader</code></p>
<dl>
<dt>
<dd> In collectl mode this command will cause the header that is normally written to a data file to be displayed on the terminal and collectl then exists. This can be a handy way to get a brief overview of the system configuration.</dl>
<p> <code>&#8211;showoptions</code></p>
<dl>
<dt>
<dd> This command shows only the portion of the help text that desribes the -o and &#8211;options switches to save the time of wading through the entire help screen.</dl>
<p> <code>&#8211;showcolheaders</code></p>
<dl>
<dt>
<dd> This command shows the first set of headers that will be printed by collectl and exits. Doesn&#8217;t really make sense for multi-section output like several sets of verbose or detail data. Also note that since it requires one monitoring interval to build up some headers which may be dynamic, it also forces the interval to 0.</dl>
<p> <code>&#8211;showsubopts</code></p>
<dl>
<dt>
<dd> List all the subsystem specifice options</dl>
<p> <code>&#8211;showtopopts</code></p>
<dl>
<dt>
<dd> Show all the different values for the &#8211;top type field, which specify the field(s) by to sort the data</dl>
<p> <code>&#8211;showrootslabs</code></p>
<dl>
<dt>
<dd> This command only works on systems using the new slab allocator and will list the root name (these are those entries in /sys/slab which are not soft links) along with all its alias names. If a name doesn&#8217;t have an alias, it will not appear in this report.</dl>
<p> <code>&#8211;showslabaliases</code></p>
<dl>
<dt>
<dd> This command only works on systems using the new slab allocator. Like &#8211;showrootslabs, it will name a slab and all its aliases but rather than show the root slab name it will show one of the aliases to provide a more meaningful name. If there are any slabs that only have a single (or no) alias they will not be included in this report.</dl>
<p> <code>&#8211;showsubopts</code></p>
<dl>
<dt>
<dd> Similar to &#8211;showoptions, this command summaries just the paramaters associated with -O and &#8211;subopts.</dl>
<p> <code>&#8211;showsubsys</code></p>
<dl>
<dt>
<dd> Yet another way to summare a portion of the help text, this command only shows valid subsystems.</dl>
<p> <code>&#8211;top [type][,num[,v]]</code></p>
<dl>
<dt>
<dd> Include the top &quot;num&quot; consumers by resource for this interval. The default number is the height of the window if it can be determined otherwise 24, and the default resource is the total cpu time which is taken as the sum of SysT and UsrT. See &#8211;showtopopts for a list of other types of data you can sort on. </p>
<p> This switch can also be used with -s in which case a portion of the window is reserved at the top to fill in the subsystem data, which is currently in verbose mode though a brief format is contemplated for some time in the future. </p>
<p> In interactive mode and if not specified, the process monitoring interval will be set to that for other subsystems. The screen will be cleared for each interval resulting in a display similar to the &quot;top&quot; utility. In playback more the screen will NOT be cleared. You cannot use this switch in &quot;record&quot; mode. </p>
<p> Finally, if v is specified as the 3rd parameter, the output scrolls vertically (like playbak mode) rather than clearing the screen between intervals.</dl>
<p> <code>&#8211;umask mask</code></p>
<dl>
<dt>
<dd> Sets collectl&#8217;s umask to control output file permissions. Only root can set the umask. See &quot;man umask&quot; for details.</dl>
<p> <code>&#8211;utime mask</code></p>
<dl>
<dt>
<dd> Write periodic micro-timestamps into raw file at different points in time for fine grained measurements of operation times.<br />
 1 &#8211; write timestamps when entering major sections<br />
 2 &#8211; write timestamps for all /proc accesses except for process data<br />
 4 &#8211; write timestamps for /proc data for all processes including threads</dl>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> Show version and whether or not Compression and/or HiResTime modules have been installed and exit.</dl>
<p> <code>-V</code></p>
<dl>
<dt>
<dd> Show default parmeter and control settings, all of which can be changed in /etc/collectl.conf</dl>
<p> <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Display output in verbose mode. This often displays more data than in the default mode. When displaying detail data, verbose mode is forced. Furthermore, if summary data for a single subsystem is to be displayed in verbose mode, the headers are only repeated occasionally whereas if multiple subsystems are involved each needs their own header.</dl>
<p> <code>-w</code></p>
<dl>
<dt>
<dd> Disply data in <code>wide</code> mode. When displaying data on the terminal, some data is formatted followed by a K, M or G as appropriate. Selecting this switch will cause the full field to be displayed. Note that there is no attempt to align data with the column headings in this mode.</dl>
<h2>SUBSYSTEM OPTIONS</h2>
<p> The following options are subsystem specific and typically filter data for collection and/or display as well as affect the output format: </p>
<p> <code>&#8211;cpufilt[^]perl-regx[,perl-regx&#8230;] </code></p>
<dl>
<dt>
<dd>
 Works the same as dskfilt and netfilt, allows one to select a subset of CPUs. These filters are also honored by interrupt reporting as well.</dl>
<p> <code>&#8211;cpuopts</code></p>
<dl>
<dt>
<dd>
 z &#8211; only applies to cpu details, do not report any CPUs with no load. In other words all entries are zero except for IDLE.</dl>
<p> <code>&#8211;dskfilt [^]perl-regx[,perl-regx&#8230;]</code></p>
<dl>
<dt>
<dd> NOTE &#8211; this does NOT effect data collection and ALL disk data will always be collected, unless &#8211;rawdskfilt is specified too. However, only data for disk names that match the pattern(s) will be included in the summary totals and displayed when details are requested. Alternatively, if you preface the first expression with a caret, all names that match all strings will be excluded from the summary totals and detail displays rather then included. If you don&#8217;t know perl, a partial string will usually work too.</dl>
<p> <code>&#8211;dskopts</code></p>
<dl>
<dt>
<dd>
 f &#8211; report some columns as fractions for more precision on detail output<br />
 i &#8211; display the i/o sizes in brief mode just like with &#8211;iosize<br />
 o &#8211; exclude unused disks from new file headers and plot data<br />
 z &#8211; only applies to disk details, do not report any lines with values of all zeros.</dl>
<p> <code>&#8211;dskremap aaa:bbb,ccc:ddd&#8230;</code></p>
<dl>
<dt>
<dd> This will cause disk names matching the perl pattern aaa to be replaced with the string bbb. In some cases, you may simply want to remove the entire string in which case the second string should be left empty. If you want to remove a string container a /, be sure to escape it with a backslash.</dl>
<p> <code>&#8211;envopts Environmental Options</code></p>
<dl>
<dt>
<dd> The default is to display ALL data but the following will cause a subset to be displayed </p>
<p> f &#8211; display fan data<br />
 p &#8211; display current (power) data<br />
 t &#8211; display temperature data<br />
 C &#8211; convert temperature to Celcius if in Farenheit<br />
 F &#8211; convert temperature to Farenheit if in Celcius<br />
 M &#8211; display each type of data on separate line<br />
 T &#8211; display data truncated to whole integers (some implemenations displayed them with fractional components)<br />
 9 &#8211; any number, will tell ipmitool to read on this device number</dl>
<p> <code>&#8211;envfilt regx</code> If specified, this regx is evaluated against each line of data returned by ipmitool and only those that match are retained. All other data is lost.</p>
<dl>
<dt>
<dd></dl>
<p> <code>&#8211;envremap perl-regx,&#8230;</code></p>
<dl>
<dt>
<dd> If specified as a comma separated list of perl regular substitution expressions without the =~s portion, each expression is applied to each environmental field name, thereby allowing one to rename the column headers. This can be most useful when running on heterogeneuos systems and you want consistent column names.</dl>
<p> <code>&#8211;intfilt [^]perl-regx[,perl-regx&#8230;]</code></p>
<dl>
<dt>
<dd> NOTE &#8211; this does NOT effect data collection, ALL interrupt data will always be collected. However, only data for interrupts that match the pattern(s) will be included in the summary totals and displayed when details are requested. Alternatively, if you preface the first expression with a caret, all names that match all strings will be excluded from the summary totals and detail displays rather then included. If you don&#8217;t know perl, a partial string will usually work too. </p>
<p> NOTE &#8211; these expressions are applied to the entire line one sees in /proc/interrupts, including the interrupt number, name and even counters so if you do want to include an interrupt number in the pattern be sure to include the trailing colon as well.</dl>
<p> <code>&#8211;lustopts Lustre Options</code></p>
<dl>
<dt>
<dd>
 B &#8211; For clients and servers, show buffer stats<br />
 D &#8211; For MDSs and OSTs AND running earlier versions of HPSFS, collect disk block iostats<br />
 M &#8211; For clients, collect metadata<br />
 O &#8211; For OSTs, show detail level stats<br />
 R &#8211; For client, collect readahead stats</dl>
<p> <code>&#8211;memopts Memory Options</code></p>
<dl>
<dt>
<dd> R &#8211; show memory values (including swap space) as rates of change as opposed to absolute values. One can also show absolute changes between intervals by including -on.</dl>
<p> <code>&#8211;netfilt [^]perl-regx[,perl-regx&#8230;]</code></p>
<dl>
<dt>
<dd> NOTE &#8211; this does NOT effect data collection and ALL network data will always be collected, unless &#8211;rawnetfilt is specified too. Also note that by default only eth, ib, em and p1p networks when present are included in the summary. When this switch is specified, only data for network names that match the pattern(s) will be included in the summary and displayed when details are requested. This switch therefore also gives you the ability to add other, possibly new, network devices to the summary totals. </p>
<p> Alternatively, if you preface the first expression with a caret, all names that match all strings will be excluded from the summary totals and detail displays rather then included. If you don&#8217;t know perl, a partial string will usually work too.</dl>
<p> <code>&#8211;netopts</code></p>
<dl>
<dt>
<dd> e &#8211; include network error counts in brief and explicit error types elsewhere<br />
 E &#8211; only include lines with network errors in them<br />
 i &#8211; include i/o sizes in brief mode<br />
 o &#8211; exclude unused networks from new file headers and plot data<br />
 w &#8211; set width of network device name</dl>
<p> <code>&#8211;nfsfilt NFS Filters</code></p>
<dl>
<dt>
<dd> Specify one or more comma separated filters as a C/S followed by an nfs version number and only those will have data reported on. For example, C2 says to report data on V2 Clients. As a data collection performance optimization, if one or more client filters are specified, data will actually be collected for all clients as is also done for servers.</dl>
<p> <code>&#8211;nfsopts NFS Options</code> q.RS z &#8211; only display detail lines which have data </p>
<p> <code>&#8211;procfilt Process Filters</code></p>
<dl>
<dt>
<dd> These filters restrict which processes are selected for collection/display. Using this filter will significanly reduce the load on process data collection since collectl creates a blacklist of those existing processes that do not pass the filter and so are permanently excluded from any future processing. </p>
<p> The format of a filter is a one charter type followed by a match string. Multiple filters may be specified if separated by commas. </p>
<p> c &#8211; substring of the command being executed as explicitly read from /proc/pid/stat. Note that this can actually be a perl expression, so if you want a command that ends in a particular string all you need to is append a to the end of the string. Otherwise it would match any commands containing that string.<br />
 C &#8211; any command that starts with the specified string<br />
 f &#8211; full path of the command, including arguments, as read from /proc/pid/cmdline. Like the c modifier this too can be a perl expression.<br />
 p &#8211; pid<br />
 P &#8211; parent pid<br />
 u &#8211; any process ownerd by this user&#8217;s UID or in the range specifide by uxxx-yyy<br />
 U &#8211; any process owned by this username </p>
<p> <code>caution:</code> the process names collectl tries to match with c and C is the second field in /proc/pid/stat which may not necessarily be what you think! eg the name for X emacs is actually emacs-x</dl>
<p> <code>&#8211;procopts options</code></p>
<dl>
<dt>
<dd> These options control the way data is displayed and can also improve data collection performance </p>
<p> c &#8211; include CPU time of children who have exited (same as ps -S)<br />
 f &#8211; use cumulative totals for page faults in process data instead of rates<br />
 i &#8211; show process I/O counters in display instead of default format<br />
 I &#8211; disable collection of I/O counters, see note below<br />
 k &#8211; remove known shells from process names, making it possible to see actual command<br />
 m &#8211; show breakdown of memory utilization instead of default format<br />
 p &#8211; never look for new pids or threads during data collection<br />
 r &#8211; show root command name only (no directory) for narrower display. Note that this is applied AFTER &#8216;k&#8217; so if arg1 becomes the new command it will be truncated now, which is very handy when running in a virtual python environment<br />
 R &#8211; show ALL process priorities (&#8216;RT&#8217; currently displayed if realtime)<br />
 s &#8211; show process start time in hh:mm:ss format<br />
 S &#8211; show process start time in mmmdd-hh:mm:ss format<br />
 t &#8211; include ALL process threads (increases collection overhead)<br />
 u &#8211; report username as 12 chars instead of 8, noting uxx will cause column width to be xx but cannot be less than 8<br />
 w &#8211; widen display by including whole argument string, with optional max width<br />
 x &#8211; include extended process attributes (currently only for context switches)<br />
 z &#8211; exclude any processes with 0 in sort field (in &#8211;top mode) </p>
<p> Process data is the most expensive type of data collected, costing as much as 3 times the CPU load as all other types of data combined. Collecting thread data makes this even more expensive. One can significantly reduce this load by over 25 percent by disabling the collection of I/O stats. However, keep in mind that even if you don&#8217;t try to optimize process data collection, the overall system load by collectl can still be on the order of about 0.2% when running as a daemon with default collection rates. See the online documentation on measuring performance for more information. </p>
<p> A security hole was identified that allowed non-priviledged users to read /proc/pid/io and guess password lengths and noe many distros retrict access to the owner or root. As a result, non-priviledged users will see all 0 I/O counts for processes that are not theirs when specifying &#8211;procopt i.</dl>
<p> <code>&#8211;slabfilt Slab Filters</code></p>
<dl>
<dt>
<dd> One can specify a list of slab names separated by commas and only those slabs whose names start with those strings will be listed or summaried.</dl>
<p> <code>&#8211;slabopts Slab Options</code></p>
<dl>
<dt>
<dd> <code>s &#8211; exclude any slabs with an allocation of 0</code><br />
 <code>S &#8211; only show those slabs whose allocations changed since last display</code></dl>
<p> <code>&#8211;tcpfilt</code></p>
<dl>
<dt>
<dd> These filters actually control both what is collected as well as displayed. If one selects non-collected filters, 0s will be reported. There is one special case and that is if one includes T (tcp extended stats) in the filter string, there are no brief ones and therefore &#8211;verbose will be forced.<br />
 <code>i &#8211; ip stats</code><br />
 <code>t &#8211; tcp stats</code><br />
 <code>u &#8211; udp stats</code><br />
 <code>c &#8211; icmp stats</code><br />
 <code>I &#8211; ip extended stats</code><br />
 <code>T &#8211; tcp excented stats</code></dl>
<p> <code>&#8211;xopts</code></p>
<dl>
<dt>
<dd> i &#8211; include i/o sizes in brief mode</dl>
<h2>DESCRIPTION</h2>
<p> The <code>collectl</code> utility is a system monitoring tool that records or displays specific operating system data for one or more sets of subsystems. Any set of the subsystems, such as CPU, Disks, Memory or Sockets can be included in or excluded from data collection. Data can either be displayed back to the terminal, or stored in either a compressed or uncompressed data file. The data files themselves can either be in <code>raw</code> format (essentially a direct copy from the associated /proc structures) or in a space separated <code>plottable</code> format such that it can be easily plotted using tools such as gnuplot or excel. Data files can be read and manipulated from the command line, or through use of command scripts. </p>
<p> Upon startup, <code>collectl.conf</code> is read, which sets a number of default parameters and switch values. Collectl searches for this file first in /etc, then in the directory the collectl execuable lives in (typically /usr/sbin) and finally the current directory. These locations can be overriden with the <code>-C</code> switch. Unless you&#8217;re doing something really special, this file need never be touched, the only exception perhaps being when choosing to run collectl as a service and you wish to change it&#8217;s default behavior which is set by the DaemonCommand entry. </p>
<h2>RESTRICTIONS/PROBLEMS</h2>
<p> Thread reporting currently only works with 2.6 kernels. </p>
<p> The pagesize has been hardcoded for perl 5.6 systems to 4096 for IA32 and 16384 for all others. If you are running 5.6 on a system with a different pagesize you will see incorrect SLAB allocation sizes and will need to scale the numbers you&#8217;re seeing accordingly. </p>
<p> I have recently discovered there is a bug in /proc in that an extra line is occasionally read with the end of the previous buffer! When this occurs a message is written (if -m enabled) and always written to the terminal. Since this happens with a higher frequency with process data I silently ignore those as the output can get pretty noisey. If for any reason this is a problem, be sure to let me know. </p>
<p> Since collectl has no control over the frequency at which data gets written to /proc, one can get anomolous statistics as collectl is only reporting a snapshot of what is being recorded. For more information see <a rel="nofollow" href="http://collectl.sourceforge.net/TheMath.html.">http://collectl.sourceforge.net/TheMath.html.</a> </p>
<p> At least one network card occasionally generates erroneous network stats and to try to keep the data rational, collectl tries to detect this and when it does generates a message that bogus data has been detected. </p>
<h2>FILES, EXAMPLES AND MORE INFORMATION</h2>
<p> <a rel="nofollow" href="http://collectl.sourceforge.net">http://collectl.sourceforge.net</a> OR /opt/hp/collectl/docs </p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> I would like to thank Rob Urban for his creation of the Tru64 Unix collect tool, which collectl is based on. </p>
<h2>AUTHOR</h2>
<p> This program was written by Mark Seger (mjseger [at] gmail.com).<br />
 Copyright 2003-2015 Hewlett-Packard Development Company, LP<br />
 collectl may be copied only under the terms of either the Artistic License or the GNU General Public License, which may be found in the source kit </p>
<h2>Index</h2>
