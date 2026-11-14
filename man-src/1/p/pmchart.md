---
title: "pmchart(1)"
name: "pmchart"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmchart/"
description: "pmchart – strip chart tool for Performance Co-Pilot"
---

<h2>NAME</h2>
<p> <code>pmchart</code> &#8211; strip chart tool for Performance Co-Pilot</p>
<h2>SYNOPSIS</h2>
<p> <code>pmchart</code> [<code>-CVWz</code>] [<code>-A</code> <i>align</i>] [<code>-a</code> <i>archive</i>] [<code>-c</code> <i>configfile</i>] [<code>-f</code> <i>fontfamily</i>] [<code>-F</code> <i>fontsize</i>] [<code>-g</code> <i>geometry</i>] [<code>-h</code> <i>host</i>] [<code>-o</code> <i>outfile</i>] [<code>-O</code> <i>offset</i>] [<code>-p</code> <i>port</i>] [<code>-s</code> <i>samples</i>] [<code>-S</code> <i>starttime</i>] [<code>-T</code> <i>endtime</i>] [<code>-t</code> <i>interval</i>] [<code>-v</code> <i>visible</i>] [<code>-Z</code> <i>timezone</i>] [<code>-geometry</code> <i>geometry</i>] [<i>sources</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmchart</code> is a graphical utility that plots performance metrics values available through the facilities of the Performance Co-Pilot (PCP). Multiple charts can be displayed simultaneously, either aligned on the unified time axis (X-axis), and through the use of multiple interface Tabs. </p>
<p> Metric values can be sourced from one or more live hosts (simultaneously). Alternatively, one or more sets of PCP archives can be used as a source of historical data. See <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) for an in-depth discussion of the capabilities of the PCP framework, many of which are used by <code>pmchart.</code> </p>
<p> Many aspects of the behaviour of <code>pmchart</code> can be customised through the interface. In particular, the use of &quot;views&quot; (refer to the section describing VIEWS later in this document) allows predefined sets of metrics and charting parameters like colors, scaling, titles, legends, and so on to be stored for later use, or use with different hosts and sets of archives. In addition, the Preferences dialog allows customisations to the rest of the <code>pmchart</code> user interface to be saved and restored between different invocations of the tool. This allows the default background color, highlight color, contents and location of the toolbar, and many other aspects to be configured. </p>
<p> <code>pmchart</code> makes extensive use of the <code><a href="/docs/linux/man/1-pmtime/">pmtime</a></code>(1) utility for time control, refer to the <code>pmtime</code> manual page for further details of its operation. </p>
<p> Options which control the default source, timing and layout of the <code>pmchart</code> window are as follows:</p>
<dl>
<dt><code>-a</code></p>
<dd> Performance metric values are retrieved from the set of Performance Co-Pilot (PCP) archive logs identified by this option, by default. The argument is a comma-separated list of names, each of which may be the base name of an archive or the name of a directory containing one or more archives. The resulting set of archives will be the source of the performance metrics. The initial Tab created will be an archive mode Tab. Multiple <code>-a</code> options can be presented, and the resulting list of sets of archives is used for sourcing metric values. Any <i>sources</i> listed on the command line are assumed to be sets of archives if this option is used.</p>
<dt><code>-c</code></p>
<dd> <i>configfile</i> specifies an initial view to load, using the default source of metrics. Multiple <code>-c</code> views can be specified, and they will all be opened in the default Tab with the default source of metrics.</p>
<dt><code>-C</code></p>
<dd> Used with <code>-c</code>, the view(s) are parsed, any errors are reported, and the tool exits. This is primarily intended for testing purposes. If a second <code>-C</code> option is presented, <code>pmchart </code> also connects to <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) to check the semantics of metrics.</p>
<dt><code>-f</code></p>
<dd> Specify the default font <i>family</i> to be used in several chart components, such as the chart title, legend, and Y-axis label. The default value is &quot;Sans Serif&quot;. This setting does not affect the rest of the user interface, where the value is inherited from the environment in which <code>pmchart</code> operates, and differs according to the look-and-feel of each platform.</p>
<dt><code>-F</code></p>
<dd> Specify the default font <i>point</i> size to be used in several chart components, such as the chart title, legend, and Y-axis label. The default is platform dependent, but is either 7, 8 or 9. This setting does not affect the rest of the user interface.</p>
<dt><code>-g</code></p>
<dd> Generate image with the specified <i>geometry</i> (width and height). This option is only useful when used in conjunction with the <code>-o</code> option for generating an output image. The <i>geometry</i> argument takes the form &quot;WxH&quot; (e.g. 240&#215;120). When NOT using the <code>-o</code> flag, to specify the display window geometry, use <code>-geometry</code> <i>geometry</i> where <i>geometry</i> specifies the desired window width, height and optional placement.</p>
<dt><code>-h</code></p>
<dd> Current performance metric values are retrieved from the nominated <i>host</i> machine by default. Multiple <code>-h</code> options can be presented, and the list of hosts is used for sourcing metric values. Any <i>sources</i> listed on the command line are assumed to be hosts if this option is used.</p>
<dt><code>-o</code></p>
<dd> Generate an image file named <i>outfile</i>, and then exit. This is most useful when run with a set of archives and one or more views. The generated image will be in the format specified as the file extension (automatically determined from <i>outfile</i>). If no extension can be determined, then the GIF format is used and the generated file is named with this extension. The supported image file formats include: bmp, jpeg, jpg, png, ppm, tif, tiff, xbm, and xpm.</p>
<dt><code>-p</code></p>
<dd> <i>port</i> number for connection to an existing <code>pmtime</code> time control process.</p>
<dt><code>-s</code></p>
<dd> Specifies the number of <i>samples</i> that will be retained before discarding old data (replaced by new values at the current time position). This value can subsequently be modified through the Edit Tab dialog.</p>
<dt><code>-t</code></p>
<dd> Sets the inital update <i>interval</i> to something other than the default 1 second. The <i>interval</i> argument follows the syntax described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), and in the simplest form may be an unsigned integer (the implied units in this case are seconds).</p>
<dt><code>-v</code></p>
<dd> Sets the inital visible <i>samples</i> that will be displayed in all charts in the default Tab. This value must be less than or equal to the total number of samples retained (the <code>-s</code> value).</p>
<dt><code>-V</code></p>
<dd> Display pmchart version number and exit</p>
<dt><code>-W</code></p>
<dd> Export images using an opaque(white) background</p>
<dt><code>-Z</code></p>
<dd> By default, <code>pmtime</code> reports the time of day according to the local timezone on the system where <code>pmchart is run.</code> The <code>-Z</code> option changes the timezone to <i>timezone</i> in the format of the environment variable TZ as described in <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7).</p>
<dt><code>-z</code></p>
<dd> Change the reporting timezone to the local timezone at the host that is the source of the performance metrics, as identified via either the <code>-h</code> or <code>-a</code> options.</dl>
<p> The <code>-S</code>, <code>-T</code>, <code>-O</code> and <code>-A</code> options may be used to define a time window to restrict the samples retrieved, set an initial origin within the time window, or specify a &quot;natural&quot; alignment of the sample times; refer to <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) for a complete description of these options.</p>
<h2>VIEWS</h2>
<p> The primary <code>pmchart</code> configuration file is the &quot;view&quot;, which allows the metadata associated with one or more charts to be saved in the filesystem. This metadata describes all aspects of the charts, including which PCP metrics and instances are to be used, which hosts, which colors, the chart titles, use of chart legends, and much more. </p>
<p> From a conceptual point of view, there are two classes of view. These views share the same configuration file format &#8211; refer to a later section for a complete description of this format. The differences lie in where they are installed and how they are manipulated. </p>
<p> The first class, the &quot;system&quot; view, is simply any view that is installed as part of the <code>pmchart</code> package. These are stored in <i>$PCP_VAR_DIR/config/pmchart.</i> When the <i>File&rarr;Open View</i> dialog is displayed, it is these views that are initially listed. The system views cannot be modified by a normal user, and should not be modified even by a user with suitable privileges, as they will be overwritten during an upgrade. </p>
<p> The second class of view is the &quot;user&quot; view. These views are created on-the-fly using the <i>File&rarr;Save View</i> dialog. This is a mechanism for individual users to save their commonly used views. Access to these views is achieved through the <i>File&rarr;Open View</i> dialog, as with the system views. Once the dialog is opened, the list of views can be toggled between user and system views by clicking on the two toggle buttons in the top right corner. User views are stored in <i>$HOME/.pcp/pmchart.</i></p>
<h2>TABS</h2>
<p> <code>pmchart</code> provides the common user interface concept of the Tab, which is most prevalent in modern web browsers. Tabs allow <code>pmchart</code> to update many more charts than the available screen real estate allows, by providing a user interface mechanism to stack (and switch between) different vertical sets of charts. Switching between Tabs is achieved by clicking on the Tab labels, which are located along the top of the display beneath the Menu and Tool bars). </p>
<p> Each Tab has a mode of operation (either live or archive &#8211; <code>pmchart</code> can support both modes simultaneously), the total number of samples and currently visible points, and a label describing the Tab which is displayed at the top of the <code>pmchart</code> window. New Tabs can be created using the <i>File&rarr;Add Tab</i> dialog. </p>
<p> In order to save on vertical screen real estate, note that the user interface element for changing between different Tabs (and its label) are only displayed when more than one Tab exists. A Tab can be dismissed using the <i>File&rarr;Close Tab</i> menu, which removes the current Tab and any charts it contained.</p>
<h2>IMAGES and PRINTING</h2>
<p> A static copy of the currently displayed vertical series of charts can be captured in two ways. </p>
<p> When the intended display device is the screen, the <i>File&rarr;Export</i> menu option should be used. This allows exporting the charts in a variety of image formats, including PNG, JPEG, GIF, and BMP. The image size can be scaled up or down in any dimension. </p>
<p> Alternatively, when the intended display device is paper, the <i>File&rarr;Print</i> menu option can be used. This supports the usual set of printing options (choice of printer, grayscale/color, landscape/portrait, scaling to different paper sizes, etc), and in addition allows printing to the intermediate printer formats of PostScript and Portable Document Format (PDF).</p>
<h2>RECORDING</h2>
<p> It is possible to make a recording of a set of displayed charts, for later playback through <code>pmchart</code> or any of the other Performance Co-Pilot tools. The <i>Record&rarr;Start</i> functionality is simple to configure through the user interface, and allows fine-tuning of the recording process (including record frequencies that differ to the <code>pmchart</code> update interval, alternate file locations, etc). </p>
<p> <code>pmchart</code> produces recordings that are compatible with the PCP <code><a href="/docs/linux/man/1-pmafm/">pmafm</a></code>(1) replay mechanism, for later playback via a new instance of <code>pmchart</code>. In addition, when recording through <code>pmchart</code> one can also replay the recording immediately, as on termination of the recording (through the <i>Record&rarr;Stop</i> menu item), an archive mode Tab will be created with the captured view. </p>
<p> Once recording is active in a Live Tab, the Time Control status button in the bottom left corner of the <code>pmchart</code> window is displayed with a distinctive red dot. At any time during a <code>pmchart</code> recording session, the amount of space used in the filesystem by that recording can be displayed using the <i>Record&rarr;Query</i> menu item. </p>
<p> Finally, the <i>Record&rarr;Detach</i> menu option provides a mechanism whereby the recording process can be completely divorced from the running <code>pmchart</code> process, and allowed to continue on when <code>pmchart</code> exits. A dialog displaying the current size and estimated rate of growth for the recording is presented. On the other hand, if <code>pmchart</code> is terminated while recording is in process, then the recording process will prompt the user to choose immediate cessation of recording or for it to continue on independently. </p>
<p> All of the record mode services available from <code>pmchart</code> are implemented with the assistance of the base Performance Co-Pilot logging services &#8211; refer to <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) and <code><a href="/docs/linux/man/1-pmafm/">pmafm</a></code>(1) for an extensive description of the capabilities of these tools.</p>
<h2>CONFIGURATION FILE SYNTAX</h2>
<p> <code>pmchart</code> loads predefined chart configurations (or &quot;views&quot;) from external files that conform to the following rules. In the descriptions below keywords (shown in bold) may appear in upper, lower or mixed case, elements shown in <tt>[stuff]</tt> are optional, and user-supplied elements are shown as <tt>&lt;other stuff&gt;</tt>. A vertical bar (|) is used where syntactic elements are alternatives. Quotes (&quot;) may be used to enclose lexical elements that may contain white space, such as titles, labels and instance names.</p>
<dl>
<dt>1.</p>
<dd> The first line defines the configuration file type and should be </p>
<pre>
#kmchart
<br>
</pre>
<p> although <code>pmchart</code> provides backwards compatibility for the older <code>pmchart</code> view formats with an initial line of </p>
<pre>
#pmchart
<br>
</pre>
<dt>2.</p>
<dd> After the first line, lines beginning with &quot;#&quot; as the first non-white space character are treated as comments and skipped. Similarly blank lines are skipped.</p>
<dt>3.</p>
<dd> The next line should be </p>
<pre>
version &lt;n&gt; &lt;host-clause&gt;
<br>
</pre>
<p> where <tt>&lt;n&gt;</tt> depends on the configuration file type, and is 1 for pmchart else 1.1, 1.2 or 2.0 for pmchart.</p>
<dl>
<dt>
<dd> The <tt>&lt;host-clause&gt;</tt> part is optional (and ignored) for <code>pmchart</code> configuration files, but required for the <code>pmchart</code> configuration files, and is of the form </p>
<pre>
host literal
<br>
</pre>
<p> or </p>
<pre>
host dynamic
<br>
</pre>
</dl>
<dt>4.</p>
<dd> A configuration contains one or more charts defined as follows: </p>
<pre>
chart [title &lt;title&gt;] style &lt;style&gt; &lt;options&gt;
<br>
</pre>
<p> If specified, the title will appear centred and above the graph area of the chart. The <tt>&lt;title&gt;</tt> is usually enclosed in quotes (&quot;) and if it contains the sequence &quot;%h&quot; this will be replaced by the short form of the hostname for the default source of metrics at the time this chart was loaded. Alternatively, &quot;%H&quot; can be used to insert the full host name. If the hostname appears to be an inet or IPv6 address, no shortening will be attempted; it will be used as-is in both replacement cases. After the view is loaded, the title visibility and setting can be manipulated using the <i>Chart Title</i> text box in the <i>Edit&rarr;Chart</i> dialog.</p>
<dl>
<dt>
<dd>
<p> The <tt>&lt;style&gt;</tt> controls the initial plotting style of the chart, and should be one of the keywords plot (line graph), bar, stacking (stacked bar), area or utilization. After the view is loaded, the plotting style can be changed using the <i>Edit&rarr;Chart</i> Style dropdown list. </p>
<p> The <tt>&lt;options&gt;</tt> are zero or more of the optional elements: </p>
<pre><code>
[scale[from]&lt;ymin&gt;[to]&lt;ymax&gt;][legend&lt;onoff&gt;]
</code></pre>
<p> If scale is specified, the vertical scaling is set for all plots in the chart to a y-range defined by <tt>&lt;ymin&gt;</tt> and <tt>&lt;ymax&gt;</tt>. Otherwise the vertical axis will be autoscaled based on the values currently being plotted. </p>
<p> <tt>&lt;onoff&gt;</tt> is one of the keywords on or off and the legend clause controls the presence or absence of the plot legend below the graph area. The default is for the legend to be shown. After the view is loaded, the legend visibility can be toggled using the <i>Show Legend</i> button in the <i>Edit&rarr;Chart</i> dialog.</dl>
<dt>5.</p>
<dd> <code>pmchart</code> supports a global clause to specify the dimensions of the top-level window (using the width and height keywords), the number of visible points (points keyword) and the starting X and Y axis positions on the screen (xpos and ypos keywords). Each of these global attributes takes an integer value as the sole qualifier.</p>
<dt>6.</p>
<dd> Each chart has one or more plots associated with it, as defined by one of the following specifications:<br />
plot<br />
    [legend&lt;title&gt;][color&lt;colorspec&gt;][host&lt;hostspec&gt;] metric&lt;metricname&gt;[instance&lt;inst&gt; | matching&lt;pat&gt; | not -matching&lt;pat&gt;]</p>
<dl>
<dt>
<dd>
<p> The keyword plot may be replaced with the keyword optional-plot, in which case if the source of performance data does not include the specified performance metric and/or instance, then this plot is silently dropped from the chart. </p>
<p> If specified, the title will appear in the chart legend. The <tt>&lt;title&gt;</tt> is usually enclosed in quotes (&quot;) and it may contain one or more wildcard characters which will be expanded using metric name, instance name, and host name for the plot. The wildcards are &quot;%i&quot; (short unique instance name, up to the first whitespace), &quot;%I&quot; (full instance name), &quot;%h&quot; (short host name, up to the first dot), %H (full host name), &quot;%m&quot; (metric name shortened to the final two PMNS components), and &quot;%M&quot; (full metric name). </p>
<p> For older <code>pmchart</code> configuration files, the keyword title must be used instead of legend. Nowadays <code>pmchart</code> supports either keyword. </p>
<p> The color clause is optional for newer <code>pmchart</code> configuration files, but it was mandatory in the original <code>pmchart</code> configuration file format. <tt>&lt;colorspec&gt;</tt> may be one of the following: </p>
<pre>
#-cycle
rgbi:rr:gg:bb
#rgb
#rrggbb
#rrrgggbbb
#rrrrggggbbbb
&lt;Xcolor&gt;
<br>
</pre>
<p> where each of <tt>r</tt>, <tt>g</tt> and <tt>b</tt> are hexadecimal digits (0-9 and A-F) representing respectively the red, green and blue color components. <tt>&lt;Xcolor&gt;</tt> is one of the color names from the X color database, e.g. red or steelblue, see also the output from <code><a href="/docs/linux/man/1-showrgb/">showrgb</a></code>(1). </p>
<p> The &quot;color&quot; #-cycle specifies that <code>pmchart</code> should use the next in a pallet of colors that it uses cyclically for each chart. This is the default if the color clause is omitted. </p>
<p> The <tt>&lt;hostspec&gt;</tt> in the host clause may be a hostname, an IP address or an asterisk (*); the latter is used to mean the default source of performance metrics. For older <code>pmchart</code> configuration files, the host clause must be present, for new <code>pmchart</code> configuration files it is optional, and if missing the default source of performance metrics will be used. </p>
<p> The optional instance specification,</p>
<dl>
<dt>(a)</p>
<dd> is omitted in which case one plot will be created for every instance of the <tt>&lt;metricname&gt;</tt> metric</p>
<dt>(b)</p>
<dd> starts with instance, in which case only the instance named <tt>&lt;inst&gt;</tt> will be plotted</p>
<dt>(c)</p>
<dd> starts with matching, in which case all instances whose names match the pattern <tt>&lt;pat&gt;</tt> will be plotted; the pattern uses extended regular expression notation in the style of <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1) (refer to the PMCD view for an example)</p>
<dt>(d)</p>
<dd> starts with not-matching, in which case all instances whose names <code>do not</code> match the pattern <tt>&lt;pat&gt;</tt> will be plotted; the pattern uses extended regular expression notation in the style of <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1) (refer to the Netbytes view for an example)</dl>
<p> <code>pmchart</code> uses a bizarre syntactic notation where <tt>&lt;inst&gt;</tt> and <tt>&lt;pat&gt;</tt> extend from the first non-white space character to the end of the input line. For <code>pmchart</code> configuration files these elements are either delimited by white space, or enclosed in quotes (&quot;).</dl>
<dt>7.</p>
<dd> The optional tab directive can be used to create views with multiple charts which span multiple Tabs. The syntax is as follows: </p>
<pre><code>
tab&lt;label&gt;[host&lt;host&gt;][points&lt;points&gt;[samples&lt;samples&gt;]]
</code></pre>
<dl>
<dt>
<dd>
<pre>
All chart specifications following this keyword will be created
on the new Tab, until the end of the configuration file or until
another tab keyword is encountered.
</dl>
</dl>
</pre>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5). </p>
<p> Of particular note, the <code>$PCP_XCONFIRM_PROG</code> setting is explicitly and unconditionally overridden by <code>pmchart.</code> This is set to the <code><a href="/docs/linux/man/1-pmconfirm/">pmconfirm</a></code>(1), utility, in order that some popup dialogs (particularly in the area of Recording) maintain a consistent look-and-feel with the rest of the <code>pmchart</code> application.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmtime/">pmtime</a></code>(1), <code><a href="/docs/linux/man/1-pmconfirm/">pmconfirm</a></code>(1), <code><a href="/docs/linux/man/1-pmdumptext/">pmdumptext</a></code>(1), <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmafm/">pmafm</a></code>(1), <code><a href="/docs/linux/man/1-pmrep/">pmrep</a></code>(1), <code><a href="/docs/linux/man/1-pmval/">pmval</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pminfo/">pminfo</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5) and <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5). </p>
<h2>Index</h2>
