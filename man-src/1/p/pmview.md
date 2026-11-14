---
title: "pmview(1)"
name: "pmview"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmview/"
description: "pmview – performance metrics 3D visualization back-end"
---

<h2>NAME</h2>
<p> <code>pmview</code> &#8211; performance metrics 3D visualization back-end</p>
<h2>SYNOPSIS</h2>
<p> <code>pmview</code> [<code>-Cz</code>] [<code>-A</code> <i>align</i>] [<code>-a</code> <i>archive</i>[<code>,</code><i>archive</i><code>,</code>&#8230;]] [<code>-c</code> <i>configfile</i>] [<code>-h</code> <i>host</i>] [<code>-n</code> <i>pmnsfile</i>] [<code>-O</code> <i>origin</i>] [<code>-p</code> <i>port</i>] [<code>-R</code> <i>logconfig</i>] [<code>-r</code> <i>addconfig</i>] [<code>-S</code> <i>starttime</i>] [<code>-t</code> <i>interval</i>] [<code>-T</code> <i>endtime</i>] [<code>-x</code> <i>version</i>] [<code>-Z</code> <i>timezone</i>] [<code>-geometry</code> <i>geometry</i>] [<code>-display</code> <i>display</i>] [<code>-name</code> <i>name</i>] [<code>-title</code> <i>title</i>] [<code>-xrm &quot;</code><i>resourceName</i><code>:</code><i> value</i><code>&quot;</code> &#8230;] [<i>other X11-args</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmview </code> is a generalized 3D performance metrics visualization tool for the Performance Co-Pilot (<code><a href="/docs/linux/man/1-pcp/">PCP</a></code>(1)). </p>
<p> <code>pmview</code> is the base utility behind performance metrics visualization tools such as <code><a href="/docs/linux/man/1-dkvis/">dkvis</a></code>(1), <code><a href="/docs/linux/man/1-mpvis/">mpvis</a></code>(1), <code><a href="/docs/linux/man/1-osvis/">osvis</a></code>(1) and <code><a href="/docs/linux/man/1-nfsvis/">nfsvis</a></code>(1), It is also used by a range of related tools that are specific to optional Performance Domain Agents (PMDA) and/or PCP add-on products. <code>pmview</code> may also be used to construct customized 3D performance displays. </p>
<p> <code>pmview</code> displays performance metrics as colored blocks and cylinders arranged on monochrome base planes. Each object may represent a single performance metric, or a stack of several performance metrics. Since the objects are modulated by the value of the metric they represent, only numerical metrics may be visualized. Objects representing a single metric may be modulated in terms of height, color, or height and color. Objects in a stack may only be height modulated, but the stack can be normalized to the maximum height. Labels may be added to the scene to help identify groups of metrics. </p>
<p> A configuration file (as specified by the <code>-c</code> option, or read from standard input) is used to specify the position, color, maximum value and labels of metrics and metric instances in the scene. The maximum value acts as a normalization factor and is used to scale the object height and/or color in proportion to the metric values. Metric values which exceed the associated maximum value are displayed as solid white objects. If a metric is unavailable, the object will have minimum height and will be colored grey. </p>
<p> Normally, the tool operates in &#8220;live&#8221; mode where performance metrics are fetched in real-time. The user can view metrics from any host running <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1). <code>pmview</code> can also replay archives of performance metrics (see <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1)) and allow the user to interactively control the current replay time and rate using the VCR paradigm. This is particularly useful for retrospective comparisons and for post-mortem analysis of performance problems where a remote system is not accessible or a performance analyst is not available on-site. </p>
<p> All metrics in the Performance Metrics Name Space (PMNS) with numeric value semantics from any number of hosts or archives may be visualized. <code>pmview</code> examines the semantics of the metrics and where sensible, converts metric values to a rate before scaling.</p>
<h2>COMMAND LINE OPTIONS</h2>
<p> The <code>-S</code>, <code>-T</code>, <code>-O</code> and <code>-A</code> options may be used to define a time window to restrict the samples retrieved, set an initial origin within the time window, or specify a &#8220;natural&#8221; alignment of the sample times; refer to <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a>(1)</code> for a complete description of these options. </p>
<p> The other available options are:</p>
<dl>
<dt><code>-a</code> <i>archive</i>[<code>,</code><i>archive</i><code>,</code>&#8230;]]</p>
<dd> Specify an <i>archive</i> from which metrics can be obtained for a particular host. <i>archive</i> is the basename of an archive, or the name of a directory conytaining archives, previously created by <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1). Multiple sets of archives (separated by commas or in different <code>-a</code> options) from different hosts may be given, but an error will occur if there is more than one set of archives from the same host. Any metrics that are not associated with a specific host or archive in the configuration file will use the first set of archives as their source.</p>
<dt><code>-C</code></p>
<dd> Parse the configuration file and exit before displaying the <code>pmview</code> window. Any errors in the configuration file are displayed.</p>
<dt><code>-c</code> <i>configfile</i></p>
<dd> Load the configuration from <i>configfile</i> rather than standard input.</p>
<dt><code>-h</code> <i>host</i></p>
<dd> Fetch performance metrics from <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) on <i>host</i>, rather than the default localhost. Implies that <code>pmview</code> will run in live mode, so no archives can be specified on the command line or in the configuration file. Only one <code>-h</code> option may be given.</p>
<dt><code>-n</code> <i>pmnsfile</i></p>
<dd> Normally <code>pmview</code> operates on the distributed Performance Metrics Name Space (PMNS), however if the <code>-n</code> option is specified an alternative local PMNS is loaded from the file <i>pmnsfile</i>.</p>
<dt><code>-p</code> <i>port</i></p>
<dd> Connect to the time controls (see <code><a href="/docs/linux/man/1-pmtime/">pmtime</a></code>(1)) on this <code>port</code>. Used when a tool launches another tool so that they can connect to the same time controls.</p>
<dt><code>-R</code> <i>logconfig</i></p>
<dd> Use <i>logconfig</i> as the <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) config when recording.</p>
<dt><code>-r</code> <i>addconfig</i></p>
<dd> Append <i>addconfig</i> onto the <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) config generated by <code>pmview</code> when recording.</p>
<dt><code>-t</code> <i>interval</i></p>
<dd> The update <i>interval</i> used to fetch metrics from the live or archive sources. The <i>interval</i> argument follows the syntax described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), and in the simplest form may be an unsigned integer (the implied units in this case are seconds). The default is 2.0 seconds.</p>
<dt><code>-x</code> <i>version</i></p>
<dd> Use the specified <i>version</i> of the <code><a href="/docs/linux/man/5-pmlaunch/">pmlaunch</a></code>(5) specification. The versions currently supported are &#8220;1.0&#8221; and the default version &#8220;2.0&#8221;.</p>
<dt><code>-Z</code> <i>timezone</i></p>
<dd> By default, <code>pmview</code> reports the time of day according to the local timezone on the system where <code>pmview</code> is run. The <code>-Z</code> option changes the default timezone to <i>timezone</i> which should be in the format of the environment variable <code>TZ</code> as described in <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7).</p>
<dt><code>-z</code></p>
<dd> Change the reporting timezone to the local timezone at the host that is the source of the performance metrics, as identified via either the <code>-h</code> option, or the first <code>-a</code> option.</dl>
<p> <code>-geometry</code> <i>geometry</i><br />
 <code>-display</code> <i>display</i><br />
 <code>-name</code> <i>name</i><br />
 <code>-title</code> <i>title</i><br />
 <code>-xrm</code> <code>&quot;</code><i>resourceName: value</i><code>&quot;</code></p>
<dl>
<dt>
<dd> Most standard <code><a href="/docs/linux/man/1-x/">X</a></code>(1) command line arguments may be used.</dl>
<h2>WINDOW</h2>
<p> The <code>pmview </code> window is comprised of a menu bar, time and scale controls, metric and time values, and an &#8220;examiner&#8221; viewer (see <code><a href="/docs/linux/man/1-ivview/">ivview</a></code>(1)), which displays the 3D scene.</p>
<h2>EXAMINER VIEWER</h2>
<p> The left, right and bottom edges of the examiner viewer contain a variety of thumb wheels and buttons that can be used to adjust the visualization of the 3D scene. The <i>Rotx</i> and <i>Roty</i> thumb wheels allow the user to rotate the scene about the x and y axes, respectively. The <i>dolly</i> thumb wheel moves the virtual camera closer and further from the scene allowing the user to examine specific parts in detail or view the entire scene. On the right edge of the viewer are eight buttons which affect the way the user can interact with the scene.</p>
<dl>
<dt><i>Pointer</i></p>
<dd> Changes the cursor to a pointer which allows blocks to be selected in the scene. See the Metric Selection section below.</p>
<dt><i>Hand</i></p>
<dd> Changes the cursor to a hand which allows the scene to be rotated, translated and dollied using a combination of mouse buttons. The left mouse button can be used to rotate the scene in the direction of the mouse. Releasing the left mouse button before the mouse has stopped moving will cause the scene to continue to rotate, which can be stopped by pressing the left mouse button again. The middle mouse button will &#8220;pan&#8221; the scene, and both mouse buttons act as a dolly for the virtual camera.</p>
<dt><i>Question Mark</i></p>
<dd> Displays the SGI Help information for the examiner viewer.</p>
<dt><i>Home</i></p>
<dd> Changes the scene back to its original position, unless the home position has been changed by the home pointer button.</p>
<dt><i>Home Pointer</i></p>
<dd> Changes the home position of the scene to be the scene currently in view.</p>
<dt><i>Eye</i></p>
<dd> Resizes the scene so that it completely fits into the 3D viewing area.</p>
<dt><i>Cross-hairs</i></p>
<dd> Moves the object under the cursor to the center of the viewing area, if the hand cursor has been selected. Pressing the &#8220;s&#8221; key while the cursor is over an object has the same effect.</p>
<dt><i>Perspective Box</i></p>
<dd> Switches the display between perspective and orthogonal projections.</dl>
<p> Pressing the right mouse button within the scene window will bring up a menu of options which affect how the 3D scene is drawn. The options include drawing the blocks as wire frames, and turning on stereo viewing.</p>
<h2>METRIC SELECTION</h2>
<p> When the pointer cursor is active, more information about the 3D scene can be obtained. Text describing the metric represented by the block under the cursor will be displayed in the top text box of the <code>pmview</code> window. The text contains the source and name of the metric, current value and units, and the percentage of the expected maximum (or normalization) value. The text box is updated whenever the scene is updated with the latest metric values or when the cursor is moved over another block in the scene. Moving the cursor over a base plane block, text or the surrounding space will clear the text box. </p>
<p> Clicking the left mouse button on a block will bind the text box on that metric instance so that the metric can be monitored while performing other actions with the mouse. The block will be highlighted with a red wire frame. Clicking the left mouse button on text or the space surrounding the scene will unselect the object, causing the text box to revert to the original behavior of showing the metric underneath the cursor. </p>
<p> Selecting a base plane instead of a modulated block will cause all the blocks on that base plane to be selected. When more than one object is selected, the text box behaves as if nothing is selected, so the metric displayed is the metric currently under the cursor. Multiple selections are also possible by pressing the SHIFT key while selecting an object with the left mouse button.</p>
<h2>MENUS</h2>
<p> There are four menus in <code>pmview</code>&#8216;s user interface which allow scenes to be recorded, saved and printed (<code>File</code>), access to the time controls (<code>Options</code>), launching other tools (<code>Launch</code>) and online help (<code>Help</code>).</p>
<dl>
<dt><code>File/Record</code></p>
<dd> When in &#8220;live&#8221; mode, this option will launch <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) processes to record the current scene into an archive folio (see <code><a href="/docs/linux/man/1-pmafm/">pmafm</a>(1))</code> so that it may be replayed at a later time. This option is not available in &#8220;replay&#8221; mode. </p>
<p> When <code>File/Record</code> is selected, a file chooser dialog will prompt for the name of the new archive folio. If the directory to the folio does not exist, <code>pmview</code> will attempt to create it. It is usually convenient to keep each folio within its own directory as there will be several other files associated with the folio, including the generated archives. </p>
<p> Once a valid folio has been created, <code>pmview</code> will launch a <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) process for each host to collect the metrics required from that host in the current scene. The current selections do not affect the set of metrics that are recorded. </p>
<p> While recording is in progress, a red dot will appear in the time controls button in the top left-hand corner of the <code>pmview</code> window. The <code>File/Record</code> option will also change to <code>File/Stop Recording</code> as only one recording session is possible at any one time. Selecting blocks or launching other tools will have no affect on the recording session. </p>
<p> The record session may be terminated by selecting <code>File/Stop Recording</code>. This will display dialogs for each <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) instance describing the size and location of the archive files before terminating each process. When all <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) processes have been terminated, the red dot is removed from the time controls button, and the menu reverts back to <code>File/Record</code> to allow another recording session to take place. </p>
<p> If the application exists while recording, a dialog will appear allowing you to terminate each <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) process, or leave it running unattached. </p>
<p> An archive folio may be replayed using the command: &#8220;<code>pmafm</code> <i>folio</i> <code>replay</code>&#8221;. See <code><a href="/docs/linux/man/1-pmafm/">pmafm</a></code>(1) for more details. </p>
<p> It is not uncommon for a front-end script which generates a <code>pmview</code> scene to use metrics that are not contained in the scene. For example, <code><a href="/docs/linux/man/1-osvis/">osvis</a></code>(1) uses several <i>hinv</i> metrics to determine the size and layout of some objects. As these metrics are also needed when replaying the generated archive with the front-end script, a complete <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) config can be specified (<code>-R</code>) that overrides the <code>pmview</code> generated config, or an additional config can be appended (<code>-r</code>) to the <code>pmview</code> generated config.</p>
<dt><code>File/Save</code></p>
<dd> Saves the current scene to a human-readable Open Inventor file (see <code><a href="/docs/linux/man/1-inventor/">inventor</a></code>(1)). A file dialog will prompt for the location of the file. The default file extension is &#8220;.iv&#8221; which is recognized by <code><a href="/docs/linux/man/1-ivview/">ivview</a></code>(1) and some Web browsers.</p>
<dt><code>File/Print</code></p>
<dd> Outputs the current scene to a printer. A print dialog will be displayed allowing a specific printer to be selected.</p>
<dt><code>File/Quit</code></p>
<dd> <code>pmview</code> immediately exits. If recording was active, dialogs will be displayed for each <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) process so that they may be terminated.</p>
<dt><code>Options/Show Time Control</code></p>
<dd> Displays the time controls (see <code><a href="/docs/linux/man/1-pmtime/">pmtime</a></code>(1)) that are driving this instance of <code>pmview</code>. The time controls may be shared by other tools, including <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1), that have been launched by other instances of <code>pmview</code> and <code><a href="/docs/linux/man/1-oview/">oview</a></code>(1). Therefore, this menu item may appear to have no affect if the time controls are already visible.</p>
<dt><code>Options/New Time Control</code></p>
<dd> Disconnect with the current time controls (which may be shared by other tools, see <code><a href="/docs/linux/man/1-pmtime/">pmtime</a></code>(1)) and use a new time control that is not connected to any other tools. The new time control will be immediately displayed.</p>
<dt><code>Launch</code></p>
<dd> The launch menu is generated from a menu specification file (see <code><a href="/docs/linux/man/5-pmlaunch/">pmlaunch</a></code>(5)). The menu contains tools that may be launched based on the sources and names of the selected metrics in the scene. For example, if the selected metrics are from three different hosts, then three copies of a tool may be launched, one for each host. The behavior of a launch depends on the selected metrics and the tools being launched. </p>
<p> On selection of a <code>Launch</code> menu item <code>pmview</code> generates state information in the <code><a href="/docs/linux/man/5-pmlaunch/">pmlaunch</a></code>(5) metrics specification format. This provides a description of the selected metrics (or if there are no selections, all the metrics) in the scene without any geometry information. </p>
<p> Tools which can monitor multiple hosts and user specified metrics may be launched only once for those metrics (eg <code><a href="/docs/linux/man/1-pmdumptext/">pmdumptext</a></code>(1)). Other tools which have a fixed view for one host (eg <code><a href="/docs/linux/man/1-mpvis/">mpvis</a></code>(1)), may be launched multiple times, once for each host in the selected metric list. If the launched tools have time controls, they will share the time controls with the launching <code>pmview</code>. </p>
<p> The set of launched tools is configurable, and may include IRIX and user applications. See <code><a href="/docs/linux/man/5-pmlaunch/">pmlaunch</a></code>(5) for more details.</p>
<dt><code>Help/&#8230;</code></p>
<dd> If <i>pcp.books.help</i> has been installed, then the <code><a href="/docs/linux/man/1-insight/">insight</a></code>(1) books for <code>pmview</code> are displayed.</dl>
<h2>TIME CONTROLS</h2>
<p> In addition to the menu options for time controls, the current direction of the time controls (see <code><a href="/docs/linux/man/1-pmtime/">pmtime</a></code>(1)) is shown in a button in the top-left corner of the <code>pmview</code> window. Pressing this button will display the time control and is identical in behavior to <code>Options/Show Time Control</code>.</p>
<h2>SCALE CONTROLS</h2>
<p> Above the examiner window is a thumb wheel and an editable text box which allow the user to apply a multiplier to all values represented in the scene. Spinning the wheel to the right and/or increasing the text value for the scale will increase the height of the bars. Spinning the wheel to the left and/or lowering the text value will decrease the height of the bars. The button to the right of the thumb wheel will reset the scale so that the bars appear at the original height for their current value.</p>
<h2>TIME INFORMATION</h2>
<p> Beside the scale controls is another text box which displays the time of the fetched metrics. The time will change with the time controller (see <code><a href="/docs/linux/man/1-pmtime/">pmtime</a></code>(1)).</p>
<h2>ENVIRONMENT</h2>
<p> The default face of the 3D font in the <code>pmview </code> window can be altered via <i>PMVIEW_FONT</i> environment variable which can be set to the base name of a Type1 font file in the default Inventor fonts directory.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_VAR_DIR/pmns/*</code></p>
<dd> default PMNS specification files</p>
<dt><code>$PCP_VAR_DIR/config/pmlaunch/pmlaunchrc</code></p>
<dd> menu specification file &#8211; provides a mapping between menu item and launched program</p>
<dt><code>$HOME/.pcp/pmlaunch/pmlaunchrc</code></p>
<dd> individual users menu specification</p>
<dt><code>/usr/lib/X11/app-defaults/PmView</code></p>
<dd> application resources</p>
<dt><code>/usr/lib/images/PmView.icon</code></p>
<dd> icon for <code>pmview</code></p>
<dt><code>$PCP_SHARE_DIR/lib/pmview-args</code></p>
<dd> shell procedures for parsing <code>pmview</code> command line options in front end scripts</p>
<dt><code>/usr/lib/DPS/outline/base/</code></p>
<dd> directory where Inventor normally looks for the outlines of Type1 fonts.</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dkvis/">dkvis</a></code>(1), <code><a href="/docs/linux/man/1-insight/">insight</a></code>(1), <code><a href="/docs/linux/man/1-inventor/">inventor</a></code>(1), <code><a href="/docs/linux/man/1-ivview/">ivview</a></code>(1), <code><a href="/docs/linux/man/1-mpvis/">mpvis</a></code>(1), <code><a href="/docs/linux/man/1-nfsvis/">nfsvis</a></code>(1), <code><a href="/docs/linux/man/1-osvis/">osvis</a></code>(1), <code><a href="/docs/linux/man/1-oview/">oview</a></code>(1), <code><a href="/docs/linux/man/1-pcp/">pcp</a></code>(1), <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmafm/">pmafm</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1), <code><a href="/docs/linux/man/1-pmdumptext/">pmdumptext</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/1-pmtime/">pmtime</a></code>(1), <code><a href="/docs/linux/man/1-pmview/">pmview</a></code>(1), <code><a href="/docs/linux/man/1-x/">X</a></code>(1), <code><a href="/docs/linux/man/1-xconfirm/">xconfirm</a></code>(1), <code><a href="/docs/linux/man/1-xlv_vis/">xlv_vis</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pmview/">pmview</a></code>(5), <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7) and <code><a href="/docs/linux/man/5-pmlaunch/">pmlaunch</a></code>(5). </p>
<p> Relevant information is also available from the on-line PCP Tutorial. Provided the <code>pcp.man.tutorial</code> subsystem from the PCP images has been installed, access the URL <code>file:$PCP_DOC_DIR/Tutorial/pmview.html </code> from your web browser. </p>
<h2>DIAGNOSTICS</h2>
<p> Are intended to be self-explanatory. The environment variable <code>PCP_STDERR</code> can be set to force most startup warnings and errors to be sent to the standard error stream rather than posted in a dialog. </p>
<h2>Index</h2>
