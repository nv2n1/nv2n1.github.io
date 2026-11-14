---
title: "sadf(1)"
name: "sadf"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sadf/"
description: "sadf – Display data collected by sar in multiple formats."
---

<h2 class="name">NAME</h2>
<p> sadf &#8211; Display data collected by sar in multiple formats.</p>
<h2>SYNOPSIS</h2>
<p> <code>sadf [ -C ] [ -c | -d | -g | -j | -l | -p | -r | -x ] [ -H ] [ -h ] [ -T | -t | -U ] [ -V ] [ -O</code> <i>opts </i><code>[,&#8230;] ] [ -P { </code><i>cpu_list </i><code>| ALL } ] [ -s [</code> <i>hh</i><code>:</code><i>mm</i><code>[:</code><i>ss</i><code>] ] ] [ -e [</code><i>hh</i><code>:</code><i>mm</i><code>[:</code><i>ss</i><code>] ] ]</code> <code>[ &#8211;dev=</code><i>dev_list </i><code>] [ &#8211;fs=</code><i>fs_list </i><code>] [ &#8211;iface=</code><i>iface_list</i><code>] [ &#8212;</code> <i>sar_options </i><code>] [ </code><i>interval </i><code>[ </code><i>count </i><code>] ] [ </code><i>datafile </i><code>| </code><i>-[0-9]+ </i><code>]</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>sadf</code> command is used for displaying the contents of data files created by the <code><a href="/docs/linux/man/1-sar/">sar</a></code>(1) command. But unlike <code>sar</code>, <code>sadf</code> can write its data in many different formats (CSV, XML, etc.) The default format is one that can easily be handled by pattern processing commands like <code>awk </code>(see option <code>-p</code>). The <code>sadf</code> command can also be used to draw graphs for the various activities collected by <code>sar</code> and display them as SVG (Scalable Vector Graphics) graphics in your web browser (see option <code>-g</code>). </p>
<p> The <code>sadf</code> command extracts and writes to standard output records saved in the <i>datafile</i> file. This file must have been created by a version of <code>sar </code>which is compatible with that of <code>sadf</code>. If <i>datafile</i> is omitted, <code>sadf</code> uses the standard system activity daily data file. It is also possible to enter <code>-1</code>, <code>-2 </code>etc. as an argument to <code>sadf</code> to display data of that days ago. For example, <code>-1</code> will point at the standard system activity file of yesterday. </p>
<p> The standard system activity daily data file is named <i>saDD </i>or <i>saYYYYMMDD</i>, where <i>YYYY </i>stands for the current year, <i>MM </i>for the current month and <i>DD</i> for the current day. <code>sadf</code> will look for the most recent of <i>saDD </i>and <i>saYYYYMMDD</i>, and use it. By default it is located in the <i>/var/log/sysstat</i> directory. Yet it is possible to specify an alternate location for it: If <i>datafile</i> is a directory (instead of a plain file) then it will be considered as the directory where the standard system activity daily data file is located. </p>
<p> The <i>interval </i>and <i>count </i>parameters are used to tell <code>sadf </code>to select <i>count </i>records at <i>interval </i>seconds apart. If the <i>count</i> parameter is not set, then all the records saved in the data file will be displayed. </p>
<p> All the activity flags of <code>sar</code> may be entered on the command line to indicate which activities are to be reported. Before specifying them, put a pair of dashes (<code>&#8212;</code>) on the command line in order not to confuse the flags with those of <code>sadf.</code> Not specifying any flags selects only CPU activity. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-C</code></p>
<dd> Tell <code>sadf </code>to display comments present in file.</p>
<dt><code>-c</code></p>
<dd> Convert an old system activity binary datafile (version 9.1.6 and later) to current up-to-date format. Use the following syntax: </p>
<p> <code>sadf -c </code><i>old_datafile </i><code>&gt; </code><i>new_datafile</i> </p>
<p> Conversion can be controlled using option <code>-O </code>(see below).</p>
<dt><code>-d</code></p>
<dd> Print the contents of the data file in a format that can easily be ingested by a relational database system. The output consists of fields separated by a semicolon. Each record contains the hostname of the host where the file was created, the interval value (or -1 if not applicable), the timestamp in a form easily acceptable by most databases, and additional semicolon separated data fields as specified by <i>sar_options </i>command line options. Note that timestamp output can be controlled by options <code>-T</code>, <code>-t </code>and <code>-U</code>.</p>
<dt><code>&#8211;dev=</code><i>dev_list</i></p>
<dd> Specify the block devices for which statistics are to be displayed by <code>sadf</code>. <i>dev_list</i> is a list of comma-separated device names. Useful with option <code>-d </code>from <code>sar</code>.</p>
<dt><code>-e [ </code><i>hh</i><code>:</code><i>mm</i><code>[:</code><i>ss</i><code>] ]</code></p>
<dd> Set the ending time of the report. The default ending time is 18:00:00. Hours must be given in 24-hour format.</p>
<dt><code>&#8211;fs=</code><i>fs_list</i></p>
<dd> Specify the filesystems for which statistics are to be displayed by <code>sadf</code>. <i>fs_list</i> is a list of comma-separated filesystem names or mountpoints. Useful with option <code>-F </code>from <code>sar</code>.</p>
<dt><code>-g</code></p>
<dd> Print the contents of the data file in SVG (Scalable Vector Graphics) format. This option enables you to display some fancy graphs in your web browser. Use the following syntax: </p>
<p> <code>sadf -g </code><i>your_datafile </i><code>[ &#8212; </code><i>sar_options </i><code>] &gt; </code><i>output.svg</i> </p>
<p> and open the resulting SVG file in your favorite web browser. Output can be controlled using option <code>-O </code>(see below).</p>
<dt><code>-H</code></p>
<dd> Display only the header of the report (when applicable). If no format has been specified, then the header data (metadata) of the data file are displayed.</p>
<dt><code>-h</code></p>
<dd> When used in conjunction with option <code>-d</code>, all activities will be displayed horizontally on a single line.</p>
<dt><code>&#8211;iface=</code><i>iface_list</i></p>
<dd> Specify the network interfaces for which statistics are to be displayed by <code>sadf</code>. <i>iface_list</i> is a list of comma-separated interface names. Useful with options <code>-n DEV </code>and <code>-n EDEV </code>from <code>sar</code>.</p>
<dt><code>-j</code></p>
<dd> Print the contents of the data file in JSON (JavaScript Object Notation) format. Timestamps can be controlled by options <code>-T </code>and <code>-t</code>.</p>
<dt><code>-l</code></p>
<dd> Export the contents of the data file to a PCP (Performance Co-Pilot) archive. The name of the archive can be specified using the keyword <code>pcparchive= </code>with option <code>-O</code>.</p>
<dt><code>-O </code><i>opts</i><code>[,&#8230;]</code></p>
<dd> Use the specified options to control the output of <code>sadf</code>. The following options are used to control SVG output displayed by <code>sadf -g</code>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>autoscale</p>
<dd> Draw all the graphs of a given view as large as possible based on current view&#8217;s scale. To do this, a factor (10, 100, 1000&#8230;) is used to enlarge the graph drawing. This option may be interesting when several graphs are drawn on the same view, some with only very small values, and others with high ones, the latter making the former hardly visible.</p>
<dt>bwcol</p>
<dd> Use a black and white palette to draw the graphs.</p>
<dt>customcol</p>
<dd> Use a customizable color palette instead of the default one to draw the graphs. See environment variable <code>S_COLORS_PALETTE</code> below to know how to customize that palette.</p>
<dt>height=<i>value</i></p>
<dd> Set SVG canvas height to <i>value</i>.</p>
<dt>oneday</p>
<dd> Display graphs data over a period of 24 hours. Note that hours are still printed in UTC by default: You should use option <code>-T </code>to print them in local time and get a time window starting from midnight.</p>
<dt>packed</p>
<dd> Group all views from the same activity (and for the same device) on the same row.</p>
<dt>showidle</p>
<dd> Also display %idle state in graphs for CPU statistics.</p>
<dt>showinfo</p>
<dd> Display additional information (such as the date and the host name) on each view.</p>
<dt>showtoc</p>
<dd> Add a table of contents at the beginning of the SVG output, consisting of links pointing at the first graph of each activity.</p>
<dt>skipempty</p>
<dd> Do not display views where all graphs have only zero values.</dl>
</dl>
<dt>
<dd> The following option may be used when converting an old system activity binary datafile to current up-to-date format:</p>
<dl>
<dt>
<dd>
<dl>
<dt>hz=<i>value</i></p>
<dd> Specify the number of ticks per second for the machine where the old datafile has been created.</dl>
</dl>
<dt>
<dd> The following option may be used when data are exported to a PCP archive:</p>
<dl>
<dt>
<dd>
<dl>
<dt>pcparchive=<i>name</i></p>
<dd> Specify the name of the PCP archive to create.</dl>
</dl>
<dt>
<dd> The following option is used to control raw output displayed by <code>sadf -r</code>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>debug</p>
<dd> Display additional information, mainly useful for debugging purpose.</dl>
</dl>
<dt><code>-P { </code><i>cpu_list </i><code>| ALL }</code></p>
<dd> Tell <code>sadf</code> that processor dependent statistics are to be reported only for the specified processor or processors. <i>cpu_list</i> is a list of comma-separated values or range of values (e.g., <code>0,2,4-7,12-</code>). Note that processor 0 is the first processor, and processor <code>all </code>is the global average among all processors. Specifying the <code>ALL</code> keyword reports statistics for each individual processor, and globally for all processors.</p>
<dt><code>-p</code></p>
<dd> Print the contents of the data file in a format that can easily be handled by pattern processing commands like <code>awk</code>. The output consists of fields separated by a tab. Each record contains the hostname of the host where the file was created, the interval value (or -1 if not applicable), the timestamp, the device name (or &#8211; if not applicable), the field name and its value. Note that timestamp output can be controlled by options <code>-T</code>, <code>-t </code>and <code>-U</code>.</p>
<dt><code>-r</code></p>
<dd> Print the raw contents of the data file. With this format, the values for all the counters are displayed as read from the kernel, which means e.g., that no average values are calculated over the elapsed time interval. Output can be controlled using option <code>-O </code>(see above).</p>
<dt><code>-s [ </code><i>hh</i><code>:</code><i>mm</i><code>[:</code><i>ss</i><code>] ]</code></p>
<dd> Set the starting time of the data, causing the <code>sadf</code> command to extract records time-tagged at, or following, the time specified. The default starting time is 08:00:00. Hours must be given in 24-hour format.</p>
<dt><code>-T</code></p>
<dd> Display timestamp in local time instead of UTC (Coordinated Universal Time).</p>
<dt><code>-t</code></p>
<dd> Display timestamp in the original local time of the data file creator instead of UTC (Coordinated Universal Time).</p>
<dt><code>-U</code></p>
<dd> Display timestamp (UTC &#8211; Coordinated Universal Time) in seconds from the epoch.</p>
<dt><code>-V</code></p>
<dd> Print version number then exit.</p>
<dt><code>-x</code></p>
<dd> Print the contents of the data file in XML format. Timestamps can be controlled by options <code>-T </code>and <code>-t</code>. The corresponding DTD (Document Type Definition) and XML Schema are included in the sysstat source package. They are also available at <i><a rel="nofollow" href="http://pagesperso-orange.fr/sebastien.godard/download.html">http://pagesperso-orange.fr/sebastien.godard/download.html</a></i>. </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> The <code>sadf</code> command takes into account the following environment variables:</p>
<dl>
<dt><code>S_COLORS_PALETTE</code></p>
<dd> Specify the colors used by <code>sadf -g</code> to render the SVG output. This environment variable is taken into account only when the custom color palette has been selected with the option <code>customcol </code>(see option <code>-O</code>). Its value is a colon-separated list of capabilities associated with six-digit, three-byte hexadecimal numbers (hex triplets) representing colors that defaults to </p>
<p> <code>0=000000:1=1a1aff:2=1affb2:3=b21aff:</code><br />
 <code>4=1ab2ff:5=ff1a1a:6=ffb31a:7=b2ff1a:</code><br />
 <code>8=efefef:9=000000:A=1a1aff:B=1affb2:</code><br />
 <code>C=b21aff:D=1ab2ff:E=ff1a1a:F=ffb31a:</code><br />
 <code>G=bebebe:H=000000:I=000000:K=ffffff:</code><br />
 <code>L=000000:T=000000:W=000000:X=000000</code> </p>
<p> Capabilities consisting of an hexadecimal digit (<code>0 </code>through <code>F</code>) are used to specify the first sixteen colors in the palette (these colors are used to draw the graphs), e.g., 3=ffffff would indicate that the third color in the palette is white (0xffffff).<br />
 Other capabilities are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>G=</code></p>
<dd> Specify the color used to draw the grid lines.</p>
<dt><code>H=</code></p>
<dd> Specify the color used to display the report header.</p>
<dt><code>I=</code></p>
<dd> Specify the color used to display additional information (e.g., date, hostname&#8230;)</p>
<dt><code>K=</code></p>
<dd> Specify the color used for the graphs background.</p>
<dt><code>L=</code></p>
<dd> Specify the default color (which is for example used to display the table of contents).</p>
<dt><code>T=</code></p>
<dd> Specify the color used to display the graphs title.</p>
<dt><code>W=</code></p>
<dd> Specify the color used to display warning and error messages.</p>
<dt><code>X=</code></p>
<dd> Specify the color used to draw the axes and display the graduations.</dl>
</dl>
<dt><code>S_TIME_DEF_TIME</code></p>
<dd> If this variable exists and its value is <code>UTC </code>then <code>sadf</code> will use UTC time instead of local time to determine the current daily data file located in the <i>/var/log/sysstat</i> directory. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>sadf -d /var/log/sysstat/sa21 &#8212; -r -n DEV</code></p>
<dd> Extract memory and network statistics from system activity file <i>sa21</i>, and display them in a format that can be ingested by a database.</p>
<dt><code>sadf -p -P 1</code></p>
<dd> Extract CPU statistics for processor 1 (the second processor) from current daily data file, and display them in a format that can easily be handled by a pattern processing command. </p>
</dl>
<h2>BUGS</h2>
<p> SVG output (as created by option <code>-g</code>) is fully compliant with SVG 1.1 standard. Graphics have been successfully displayed in various web browsers, including Firefox, Chrome and Opera. Yet SVG rendering is broken on Microsoft browsers (tested on Internet Explorer 11 and Edge 13.1): So please don&#8217;t use them. </p>
<h2>FILES</h2>
<p> <i>/var/log/sysstat/saDD</i><br />
 <i>/var/log/sysstat/saYYYYMMDD</i></p>
<dl>
<dt>
<dd> The standard system activity daily data files and their default location. <i>YYYY </i>stands for the current year, <i>MM </i>for the current month and <i>DD</i> for the current day.</dl>
<h2>AUTHOR</h2>
<p> Sebastien Godard (sysstat &lt;at&gt; orange.fr) </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sar/">sar</a></code>(1), <code><a href="/docs/linux/man/8-sadc/">sadc</a></code>(8), <code><a href="/docs/linux/man/8-sa1/">sa1</a></code>(8), <code><a href="/docs/linux/man/8-sa2/">sa2</a></code>(8), <code><a href="/docs/linux/man/5-sysstat/">sysstat</a></code>(5) </p>
<p> <i><a rel="nofollow" href="https://github.com/sysstat/sysstat">https://github.com/sysstat/sysstat</a></i><br />
 <i><a rel="nofollow" href="http://pagesperso-orange.fr/sebastien.godard/">http://pagesperso-orange.fr/sebastien.godard/</a></i> </p>
<h2>Index</h2>
