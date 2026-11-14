---
title: "nvidia-settings(1)"
name: "nvidia-settings"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvidia-settings/"
description: "nvidia-settings – configure the NVIDIA graphics driver"
---

<h2 class="name">NAME</h2>
<p> nvidia-settings &#8211; configure the NVIDIA graphics driver </p>
<h2>SYNOPSIS</h2>
<p> <code>nvidia-settings [</code><i>options</i><code>]</code><br />
 <code>nvidia-settings [</code><i>options</i><code>] &#8211;no-config</code><br />
 <code>nvidia-settings [</code><i>options</i><code>] &#8211;load-config-only</code><br />
 <code>nvidia-settings [</code><i>options</i><code>] {&#8211;query=</code><i>attr</i><code> | &#8211;assign=</code><i>attr</i><code>=</code><i>value</i><code>} &#8230;</code><br />
 <code>nvidia-settings [</code><i>options</i><code>] &#8211;glxinfo</code> </p>
<p> Options: <code>[-vh] [&#8211;config=</code><i>configfile</i><code>] [-c </code><i>ctrl-display</i><code>]</code><br />
 <i> </i><code>[&#8211;verbose=</code>{<i>none </i>|<i> errors </i>|<i> deprecations </i>|<i> warnings </i>|<i> all</i>}<code>]</code><br />
 <i> </i><code>[&#8211;describe=</code>{<i>all </i>|<i> list </i>|<i> attribute_name</i>}<code>]</code> </p>
<p> <i>attr</i> has the form:<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; <i>DISPLAY</i><code>/</code><i>attribute_name</i><code>[</code><i>display_devices</i><code>]</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>nvidia-settings</code> utility is a tool for configuring the NVIDIA graphics driver. It operates by communicating with the NVIDIA X driver, querying and updating state as appropriate. This communication is done via the NV-CONTROL, GLX, XVideo, and RandR X extensions. </p>
<p> Values such as brightness and gamma, XVideo attributes, temperature, and OpenGL settings can be queried and configured via <code>nvidia-settings.</code> </p>
<p> When <code>nvidia-settings</code> starts, it reads the current settings from its configuration file and sends those settings to the X server. Then, it displays a graphical user interface (GUI) for configuring the current settings. When <code>nvidia-settings</code> exits, it queries the current settings from the X server and saves them to the configuration file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v, &#8211;version</code></p>
<dd> Print the <code>nvidia-settings</code> version and exit.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Print usage information and exit.</p>
<dt><code>&#8211;config=</code><i>CONFIG</i></p>
<dd> Use the configuration file <i>CONFIG</i> rather than the default <i>~/.nvidia-settings-rc</i> </p>
<dt><code>-c </code><i>CTRL-DISPLAY</i><code>, &#8211;ctrl-display=</code><i>CTRL-DISPLAY</i></p>
<dd> Control the specified X display. If this option is not given, then <code>nvidia-settings</code> will control the display specified by <code>&#8216;&#8211;display&#8217;</code> ; if that is not given, then the <i>$DISPLAY</i> environment variable is used.</p>
<dt><code>-l, &#8211;load-config-only</code></p>
<dd> Load the configuration file, send the values specified therein to the X server, and exit. This mode of operation is useful to place in your xinitrc file, for example.</p>
<dt><code>-n, &#8211;no-config</code></p>
<dd> Do not load the configuration file. This mode of operation is useful if <code>nvidia-settings</code> has difficulties starting due to problems with applying settings in the configuration file.</p>
<dt><code>-r, &#8211;rewrite-config-file</code></p>
<dd> Write the X server configuration to the configuration file, and exit, without starting the graphical user interface. See EXAMPLES section.</p>
<dt><code>-V </code><i>VERBOSE</i><code>, &#8211;verbose=</code><i>VERBOSE</i></p>
<dd> Controls how much information is printed. Valid values are <code>&#8216;none&#8217;</code> (do not print status messages), <code>&#8216;errors&#8217;</code> (print error messages), <code>&#8216;deprecations&#8217;</code> (print error and deprecation messages), <code>&#8216;warnings&#8217;</code> (print error, deprecation, and warning messages), and <code>&#8216;all&#8217;</code> (print error, deprecation, warning and other informational messages). By default, <code>&#8216;deprecations&#8217;</code> is set.</p>
<dt><code>-a </code><i>ASSIGN</i><code>, &#8211;assign=</code><i>ASSIGN</i></p>
<dd> The <i>ASSIGN</i> argument to the <code>&#8216;&#8211;assign&#8217;</code> command line option is of the form: </p>
<p>&nbsp;<wbr>&nbsp;{DISPLAY}/{attribute name}[{display devices}]={value} </p>
<p> This assigns the attribute {attribute name} to the value {value} on the X Display {DISPLAY}. {DISPLAY} follows the usual {host}:{display}.{screen} syntax of the DISPLAY environment variable and is optional; when it is not specified, then it is implied following the same rule as the <code>&#8211;ctrl-display</code> option. If the X screen is not specified, then the assignment is made to all X screens. Note that the &#8216;/&#8217; is only required when {DISPLAY} is present. </p>
<p> {DISPLAY} can additionally include a target specification to direct an assignment to something other than an X screen. A target specification is contained within brackets and consists of a target type name, a colon, and the target id. The target type name can be one of <code>screen, gpu, framelock, fan, thermalsensor, svp,</code> or <code>dpy;</code> the target id is the index into the list of targets (for that target type). The target specification can be used in {DISPLAY} wherever an X screen can be used, following the syntax {host}:{display}[{target_type}:{target_id}]. See the output of </p>
<p>&nbsp;<wbr>&nbsp;nvidia-settings -q all&nbsp; </p>
<p> for information on which target types can be used with which attributes. See the output of </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nvidia-settings -q screens -q gpus -q framelocks -q fans -q thermalsensors -q svps -q dpys&nbsp; </p>
<p> for lists of targets for each target type. </p>
<p> The [{display devices}] portion is also optional; if it is not specified, then the attribute is assigned to all display devices. </p>
<p> Some examples: </p>
<p>&nbsp;<wbr>&nbsp;-a FSAA=5<br />
&nbsp;<wbr>&nbsp;-a localhost:0.0/DigitalVibrance[CRT-0]=0<br />
&nbsp;<wbr>&nbsp;&#8211;assign=&quot;SyncToVBlank=1&quot;<br />
&nbsp;<wbr>&nbsp;-a&nbsp;[gpu:0]/DigitalVibrance[DFP-1]=63 </p>
<dt><code>-q </code><i>QUERY</i><code>, &#8211;query=</code><i>QUERY</i></p>
<dd> The <i>QUERY</i> argument to the <code>&#8216;&#8211;query&#8217;</code> command line option is of the form: </p>
<p>&nbsp;<wbr>&nbsp;{DISPLAY}/{attribute name}[{display devices}] </p>
<p> This queries the current value of the attribute {attribute name} on the X Display {DISPLAY}. The syntax is the same as that for the <code>&#8216;&#8211;assign&#8217;</code> option, without &#8216;= <code>{value}&#8217;</code> ; specify <code>&#8216;-q screens&#8217;, &#8216;-q gpus&#8217;, &#8216;-q framelocks&#8217;, &#8216;-q fans&#8217;</code> , &#8216;-q thermalsensors&#8217;, &#8216;-q svps&#8217;, or &#8216;-q dpys&#8217; to query a list of X screens, GPUs, Frame Lock devices, Visual Computing Systems, Devices, Fans, Thermal Sensors, 3D Vision Pro Transceivers, or Display Devices, respectively, that are present on the X Display {DISPLAY}. Specify <code>&#8216;-q all&#8217;</code> to query all attributes.</p>
<dt><code>-t, &#8211;terse</code></p>
<dd> When querying attribute values with the &#8216;&#8211;query&#8217; command line option, only print the current value, rather than the more verbose description of the attribute, its valid values, and its current value.</p>
<dt><code>-d, &#8211;display-device-string</code></p>
<dd> When printing attribute values in response to the &#8216;&#8211;query&#8217; option, if the attribute value is a display device mask, print the value as a list of display devices (e.g., &quot;CRT-0, DFP-0&quot;), rather than a hexadecimal bit mask (e.g., 0x00010001).</p>
<dt><code>-g, &#8211;glxinfo</code></p>
<dd> Print GLX Information for the X display and exit.</p>
<dt><code>-E, &#8211;eglinfo</code></p>
<dd> Print EGL Information for the X display and exit.</p>
<dt><code>-e </code><i>DESCRIBE</i><code>, &#8211;describe=</code><i>DESCRIBE</i></p>
<dd> Prints information about a particular attribute. Specify &#8216;all&#8217; to list the descriptions of all attributes. Specify &#8216;list&#8217; to list the attribute names without a descriptions.</p>
<dt><code>-p </code><i>PAGE</i><code>, &#8211;page=</code><i>PAGE</i></p>
<dd> The <i>PAGE</i> argument to the <code>&#8216;&#8211;page&#8217;</code> commandline option selects a particular page in the nvidia-settings user interface to display upon starting nvidia-settings. Valid values are the page names in the tree view on the left side of the nvidia-settings user interface; e.g., </p>
<p>&nbsp;<wbr>&nbsp;&#8211;page=&quot;X Screen 0&quot; </p>
<p> Because some page names are not unique (e.g., a &quot;PowerMizer&quot; page is present under each GPU), the page name can optionally be prepended with the name of the parent X Screen or GPU page, followed by a comma. E.g., </p>
<p>&nbsp;<wbr>&nbsp;&#8211;page=&quot;GPU 0 &#8211;&nbsp;(Quadro 6000), PowerMizer&quot; </p>
<p> The first page with a name matching the <i>PAGE</i> argument will be used. By default, the &quot;System Information&quot; page is displayed.</p>
<dt><code>-L, &#8211;list-targets-only</code></p>
<dd> When performing an attribute query (from the &#8216;&#8211;query&#8217; command line option) or an attribute assignment (from the &#8216;&#8211;assign&#8217; command line option or when loading an ~/.nvidia-settings-rc file), nvidia-settings identifies one or more targets on which to query/assign the attribute. </p>
<p> The &#8216;&#8211;list-targets-only&#8217; option will cause nvidia-settings to list the targets on which the query/assign operation would have been performed, without actually performing the operation(s), and exit.</p>
<dt><code>-w, &#8211;write-config, &#8211;no-write-config</code></p>
<dd> Save the configuration file on exit (enabled by default).</p>
<dt><code>-i, &#8211;use-gtk2</code></p>
<dd> Force nvidia-settings to use the GTK+ 2 library for the graphical user interface if a user interface is required. This option is only available on systems where nvidia-settings supports both the GTK+ 2 and GTK+ 3 user interfaces. </p>
<dt><code>-I </code><i>GTK-LIBRARY</i><code>, &#8211;gtk-library=</code><i>GTK-LIBRARY</i></p>
<dd> Specify the graphical user interface library to use if a nvidia-settings user interface is required. This value may be the exact location of the library or it may be the directory containing the appropriately named library. If this is the exact location, the &#8216;use-gtk2&#8217; option is ignored. </p>
</dl>
<h2>USER GUIDE</h2>
<h3>Contents</h3>
<p> 1.<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Layout of the nvidia-settings GUI</p>
<p> 2.<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>How OpenGL Interacts with nvidia-settings</p>
<p> 3.<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Loading Settings Automatically</p>
<p> 4.<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Command Line Interface</p>
<p> 5.<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>X Display Names in the Config File</p>
<p> 6.<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Connecting to Remote X Servers</p>
<p> 7.<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Licensing</p>
<p> 8.<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>TODO</p>
<h3>1. Layout of the nvidia-settings GUI</h3>
<p> The <code>nvidia-settings</code> GUI is organized with a list of different categories on the left side. Only one entry in the list can be selected at once, and the selected category controls which &quot;page&quot; is displayed on the right side of the <code>nvidia-settings</code> GUI. </p>
<p> The category list is organized in a tree: each X screen contains the relevant subcategories beneath it. Similarly, the Display Devices category for a screen contains all the enabled display devices beneath it. Besides each X screen, the other top level category is &quot;nvidia-settings Configuration&quot;, which configures behavior of the <code>nvidia-settings</code> application itself. </p>
<p> Along the bottom of the <code>nvidia-settings</code> GUI, from left to right, is:</p>
<dl>
<dt>1)</p>
<dd> a status bar which indicates the most recently altered option;</p>
<dt>2)</p>
<dd> a Help button that toggles the display of a help window which provides a detailed explanation of the available options in the current page; and</p>
<dt>3)</p>
<dd> a Quit button to exit <code>nvidia-settings.</code></dl>
<p> Most options throughout <code>nvidia-settings</code> are applied immediately. Notable exceptions are OpenGL options which are only read by OpenGL when an OpenGL application starts. </p>
<p> Details about the options on each page of <code>nvidia-settings</code> are available in the help window.</p>
<h3>2. How OpenGL Interacts with nvidia-settings</h3>
<p> When an OpenGL application starts, it downloads the current values from the X driver, and then reads the environment (see <i>APPENDIX E: OPENGL ENVIRONMENT VARIABLE SETTINGS</i> in the README). Settings from the X server override OpenGL&#8217;s default values, and settings from the environment override values from the X server. </p>
<p> For example, by default OpenGL uses the FSAA setting requested by the application (normally, applications do not request any FSAA). An FSAA setting specified in <code>nvidia-settings</code> would override the OpenGL application&#8217;s request. Similarly, the <code>__GL_FSAA_MODE</code> environment variable will override the application&#8217;s FSAA setting, as well as any FSAA setting specified in <code>nvidia-settings.</code> </p>
<p> Note that an OpenGL application only retrieves settings from the X server when it starts, so if you make a change to an OpenGL value in <code>nvidia-settings,</code> it will only apply to OpenGL applications which are started after that point in time.</p>
<h3>3. Loading Settings Automatically</h3>
<p> The NVIDIA X driver does not preserve values set with <code>nvidia-settings</code> between runs of the X server (or even between logging in and logging out of X, with <code><a href="/docs/linux/man/1-xdm/">xdm</a></code>(1), <code>gdm,</code> or <code>kdm</code> ). This is intentional, because different users may have different preferences, thus these settings are stored on a per-user basis in a configuration file stored in the user&#8217;s home directory. </p>
<p> The configuration file is named <i>~/.nvidia-settings-rc</i>. You can specify a different configuration file name with the <code>&#8211;config</code> command line option. </p>
<p> After you have run <code>nvidia-settings</code> once and have generated a configuration file, you can then run: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; nvidia-settings &#8211;load-config-only </p>
<p> at any time in the future to upload these settings to the X server again. For example, you might place the above command in your <i>~/.xinitrc</i> file so that your settings are applied automatically when you log in to X. </p>
<p> Your <i>.xinitrc</i> file, which controls what X applications should be started when you log into X (or startx), might look something like this: </p>
<pre>
     nvidia-settings --load-config-only &amp;
     xterm &amp;
     evilwm
</pre>
<p> or: </p>
<pre>
     nvidia-settings --load-config-only &amp;
     gnome-session
</pre>
<p> If you do not already have an <i>~/.xinitrc</i> file, then chances are that <code><a href="/docs/linux/man/1-xinit/">xinit</a></code>(1) is using a system-wide xinitrc file. This system wide file is typically here: </p>
<pre>
     /etc/X11/xinit/xinitrc
</pre>
<p> To use it, but also have <code>nvidia-settings</code> upload your settings, you could create an <i>~/.xinitrc</i> with the contents: </p>
<pre>
     nvidia-settings --load-config-only &amp;
     . /etc/X11/xinit/xinitrc
</pre>
<p> System administrators may choose to place the <code>nvidia-settings</code> load command directly in the system xinitrc script. </p>
<p> Please see the <code><a href="/docs/linux/man/1-xinit/">xinit</a></code>(1) man page for further details of configuring your <i>~/.xinitrc</i> file.</p>
<h3>4. Command Line Interface</h3>
<p> <code>nvidia-settings</code> has a rich command line interface: all attributes that can be manipulated with the GUI can also be queried and set from the command line. The command line syntax for querying and assigning attributes matches that of the <i>.nvidia-settings-rc</i> configuration file. </p>
<p> The <code>&#8211;query</code> option can be used to query the current value of attributes. This will also report the valid values for the attribute. You can run <code>nvidia-settings &#8211;query all</code> for a complete list of available attributes, what the current value is, what values are valid for the attribute, and through which target types (e.g., X screens, GPUs) the attributes can be addressed. Additionally, individual attributes may be specified like this: </p>
<pre>
        nvidia-settings --query Overlay
</pre>
<p> An attribute name may be prepended with an X Display name and a forward slash to indicate a different X Display; e.g.: </p>
<pre>
        nvidia-settings --query localhost:0.0/Overlay
</pre>
<p> An attribute name may also just be prepended with the screen number and a forward slash: </p>
<pre>
        nvidia-settings --query 0/Overlay
</pre>
<p> in which case the default X Display will be used, but you can indicate to which X screen to direct the query (if your X server has multiple X screens). If no X screen is specified, then the attribute value will be queried for all valid targets of the attribute (eg GPUs, Displays X screens, etc). </p>
<p> Attributes can be addressed through &quot;target types&quot;. A target type indicates the object that is queried when you query an attribute. The default target type is an X screen, but other possible target types are GPUs, Frame Lock devices, Visual Computing Systems, fans, thermal sensors, 3D Vision Pro Transceivers and display devices. </p>
<p> Target types give you different granularities with which to perform queries and assignments. Since X screens can span multiple GPUs (in the case of Xinerama, or SLI), and multiple X screens can exist on the same GPU, it is sometimes useful to address attributes by GPU rather than X screen. </p>
<p> A target specification is contained within brackets and may consist of a target type name, a colon, and the target id. The target type name can be one of <code>screen,</code> <code>gpu,</code> <code>framelock,</code> <code>fan,</code> <code>thermalsensor,</code> <code>svp,</code> or <code>dpy;</code> the target id is the index into the list of targets (for that target type). Target specifications can be used wherever an X screen is used in query and assignment commands; the target specification can be used either by itself on the left side of the forward slash, or as part of an X Display name. </p>
<p> For example, the following queries address X screen 0 on the localhost: </p>
<pre><code>
nvidia - settings-- query 0 / VideoRam nvidia - settings-- query localhost : 0.0 / VideoRam nvidia - settings-- query [screen:0] / VideoRam nvidia - settings-- query localhost : 0 [screen:0] / VideoRam
</code></pre>
<p> To address GPU 0 instead, you can use either of:<br />
nvidia &#8211; settings&#8211; query [gpu:0] / VideoRam nvidia &#8211; settings&#8211; query localhost : 0 [gpu:0] / VideoRam<br />
 Note that if a target specification is present, it will override any X screen specified in the display name as the target to process. For example, the following query would address GPU 0, and not X screen 1: </p>
<pre>
        nvidia-settings --query localhost:0.1[gpu:0]/VideoRam
</pre>
<p> A target name may be used instead of a target id, in which case all targets with matching names are processed. </p>
<p> For example, querying the DigitalVibrance of display device DVI-I-1 may be done like so: </p>
<pre>
        nvidia-settings --query [dpy:DVI-I-1]/DigitalVibrance
</pre>
<p> When a target name is specified, the target type name may be omitted, though this should be used with caution since the name will be matched across all target types. The above example could be written as: </p>
<pre>
        nvidia-settings --query [DVI-I-1]/DigitalVibrance
</pre>
<p> The target name may also simply be a target type name, in which case all targets of that type will be queried. </p>
<p> For example, querying the BusRate of all GPUs may be done like so: </p>
<pre>
        nvidia-settings --query [gpu]/BusRate
</pre>
<p> The target specification may also include a target qualifier. This is useful to limit processing to a subset of targets, based on an existing relationship(s) to other targets. The target qualifier is specified by prepending a target type name, a colon, the target id, and a period to the existing specification. Only one qualitfer may be specified. </p>
<p> For example, querying the RefreshRate of all DFP devices on GPU 1 may be done like so: </p>
<pre>
        nvidia-settings --query [GPU:1.DPY:DFP]/RefreshRate
</pre>
<p> Likewise, a simple target name (or target type name) may be used as the qualifier. For example, to query the BusType of all GPUs that have DFPs can be done like so: </p>
<pre>
        nvidia-settings --query [DFP.GPU]/BusType
</pre>
<p> See the output of </p>
<pre>
        nvidia-settings --query all
</pre>
<p> for what targets types can be used with each attribute. See the output of<br />
nvidia &#8211; settings&#8211; query screens&#8211; query gpus&#8211; query framelocks&#8211; query fans&#8211; query thermalsensors&#8211; query svps&#8211; query dpys<br />
 for lists of targets for each target type. </p>
<p> To enable support for the &quot;GPUGraphicsClockOffset&quot; and &quot;GPUMemoryTransferRateOffset&quot; attributes, ensure that the &quot;Coolbits&quot; X configuration option includes the value &quot;8&quot; in the bitmask. For more details, refer to the documentation of the &quot;Coolbits&quot; option in the NVIDIA driver README. Query the &quot;GPUPerfModes&quot; string attribute to see a list of the available performance modes: </p>
<pre>
        nvidia-settings --query GPUPerfModes 
</pre>
<p> Each performance mode is presented as a comma-separated list of &quot;token=value&quot; pairs. Each set of performance mode tokens is separated by a &quot;;&quot;. The &quot;perf&quot; token indicates the performance level. The &quot;*editable&quot; tokens indicate which domains within the performance level can have an offset applied. The &quot;GPUGraphicsClockOffset&quot; and &quot;GPUMemoryTransferRateOffset&quot; attributes map respectively to the &quot;nvclock&quot; and &quot;memtransferrate&quot; tokens of performance levels in the &quot;GPUPerfModes&quot; string. </p>
<p> Note that the clock manipulation attributes &quot;GPUGraphicsClockOffset&quot; and &quot;GPUMemoryTransferRateOffset&quot; apply to the offsets of specific performance levels. The performance level is specified in square brackets after the attribute name. For example, to query the &quot;GPUGraphicsClockOffset&quot; for performance level 2: </p>
<pre>
        nvidia-settings --query GPUGraphicsClockOffset[2]
</pre>
<p> The <code>&#8211;assign</code> option can be used to assign a new value to an attribute. The valid values for an attribute are reported when the attribute is queried. The syntax for <code>&#8211;assign</code> is the same as <code>&#8211;query,</code> with the additional requirement that assignments also have an equal sign and the new value. For example: </p>
<pre><code>
nvidia - settings-- assign FSAA = 2 nvidia - settings-- assign[CRT - 1] / DigitalVibrance = 9 nvidia - settings-- assign [gpu:0] / DigitalVibrance = 0 nvidia - settings-- assign [gpu:0] / GPUGraphicsClockOffset[2] = 10
</code></pre>
<p> Multiple queries and assignments may be specified on the command line for a single invocation of <code>nvidia-settings.</code> Assignments are processed in the order they are entered on the command line. If multiple assignments are made to the same attribute or to multiple attributes with dependencies, then the later assignments will have priority. </p>
<p> If either the <code>&#8211;query</code> or <code>&#8211;assign</code> options are passed to <code>nvidia-settings,</code> the GUI will not be presented, and <code>nvidia-settings</code> will exit after processing the assignments and/or queries. In this case, settings contained within the <i>~/.nvidia-settings-rc</i> configuration file will not be automatically uploaded to the X server, nor will the <i>~/.nvidia-settings-rc</i> configuration file be automatically updated to reflect attribute assignments made via the <code>&#8211;assign</code> option.</p>
<h3>5. X Display Names in the Config File</h3>
<p> In the Command Line Interface section above, it was noted that you can specify an attribute without any X Display qualifiers, with only an X screen qualifier, or with a full X Display name. For example: </p>
<pre>
        nvidia-settings --query FSAA
        nvidia-settings --query 0/FSAA
        nvidia-settings --query stravinsky.nvidia.com:0/FSAA
</pre>
<p> In the first two cases, the default X Display will be used, in the second case, the screen from the default X Display can be overridden, and in the third case, the entire default X Display can be overridden. </p>
<p> The same possibilities are available in the <i>~/.nvidia-settings-rc</i> configuration file. </p>
<p> For example, in a computer lab environment, you might log into any of multiple workstations, and your home directory is NFS mounted to each workstation. In such a situation, you might want your <i>~/.nvidia-settings-rc</i> file to be applicable to all the workstations. Therefore, you would not want your config file to qualify each attribute with an X Display Name. Leave the &quot;Include X Display Names in the Config File&quot; option unchecked on the <code>nvidia-settings</code> Configuration page (this is the default). </p>
<p> There may be cases when you do want attributes in the config file to be qualified with the X Display name. If you know what you are doing and want config file attributes to be qualified with an X Display, check the &quot;Include X Display Names in the Config File&quot; option on the <code>nvidia-settings</code> Configuration page. </p>
<p> In the typical home user environment where your home directory is local to one computer and you are only configuring one X Display, then it does not matter whether each attribute setting is qualified with an X Display Name.</p>
<h3>6. Connecting to Remote X Servers</h3>
<p> <code>nvidia-settings</code> is an X client, but uses two separate X connections: one to display the GUI, and another to communicate the NV-CONTROL requests. These two X connections do not need to be to the same X server. For example, you might run <code>nvidia-settings</code> on the computer stravinsky.nvidia.com, export the display to the computer bartok.nvidia.com, but be configuring the X server on the computer schoenberg.nvidia.com: </p>
<pre>
        nvidia-settings --display=bartok.nvidia.com:0 \
            --ctrl-display=schoenberg.nvidia.com:0
</pre>
<p> If <code>&#8211;ctrl-display</code> is not specified, then the X Display to control is what <code>&#8211;display</code> indicates. If <code>&#8211;display</code> is also not specified, then the <i>$DISPLAY</i> environment variable is used. </p>
<p> Note, however, that you will need to have X permissions configured such that you can establish an X connection from the computer on which you are running <code>nvidia-settings</code> (stravinsky.nvidia.com) to the computer where you are displaying the GUI (bartok.nvidia.com) and the computer whose X Display you are configuring (schoenberg.nvidia.com). </p>
<p> The simplest, most common, and least secure mechanism to do this is to use &#8216;xhost&#8217; to allow access from the computer on which you are running <code>nvidia-settings.</code> </p>
<pre>
        (issued from bartok.nvidia.com)
        xhost +stravinsky.nvidia.com
        (issued from schoenberg.nvidia.com)
        xhost +stravinsky.nvidia.com
</pre>
<p> This will allow all X clients run on stravinsky.nvidia.com to connect and display on bartok.nvidia.com&#8217;s X server and configure schoenberg.nvidia.com&#8217;s X server. </p>
<p> Please see the <code><a href="/docs/linux/man/1-xauth/">xauth</a></code>(1) and <code><a href="/docs/linux/man/1-xhost/">xhost</a></code>(1) man pages, or refer to your system documentation on remote X applications and security. You might also Google for terms such as &quot;remote X security&quot; or &quot;remote X Windows&quot;, and see documents such as the Remote X Apps mini-HOWTO: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; &lt; <a rel="nofollow" href="http://www.tldp.org/HOWTO/Remote-X-Apps.html">http://www.tldp.org/HOWTO/Remote-X-Apps.html</a> &gt; </p>
<p> Please also note that the remote X server to be controlled must be using the NVIDIA X driver.</p>
<h3>7. Licensing</h3>
<p> The source code to <code>nvidia-settings</code> is released as GPL. The most recent official version of the source code is available here: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; &lt; <a rel="nofollow" href="https://download.nvidia.com/XFree86/nvidia-settings/">https://download.nvidia.com/XFree86/nvidia-settings/</a> &gt; </p>
<p> Note that <code>nvidia-settings</code> is simply an NV-CONTROL client. It uses the NV-CONTROL X extension to communicate with the NVIDIA X server to query current settings and make changes to settings. </p>
<p> You can make additions directly to <code>nvidia-settings,</code> or write your own NV-CONTROL client, using <code>nvidia-settings</code> as an example. </p>
<p> Documentation on the NV-CONTROL extension and additional sample clients are available in the <code>nvidia-settings</code> source tarball. Patches can be submitted to linux-bugs [at] nvidia.com.</p>
<h3>8. TODO</h3>
<p> There are many things still to be added to <code>nvidia-settings,</code> some of which include:</p>
<dl>
<dt>&#8211;</p>
<dd> different toolkits? The GUI for <code>nvidia-settings</code> is cleanly abstracted from the back-end of <code>nvidia-settings</code> that parses the configuration file and command line, communicates with the X server, etc. If someone were so inclined, a different front-end GUI could be implemented.</p>
<dt>&#8211;</p>
<dd> write a design document explaining how <code>nvidia-settings</code> is designed; presumably this would make it easier for people to become familiar with the code base.</dl>
<p> If there are other things you would like to see added (or better yet, would like to add yourself), please contact linux-bugs [at] nvidia.com.</p>
<h2>FILES</h2>
<dl>
<dt><i>~/.nvidia-settings-rc</i></p>
<dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>nvidia-settings</code></p>
<dd> Starts the <code>nvidia-settings</code> graphical interface.</p>
<dt><code>nvidia-settings &#8211;load-config-only</code></p>
<dd> Loads the settings stored in <i>~/.nvidia-settings-rc</i> and exits.</p>
<dt><code>nvidia-settings &#8211;rewrite-config-file</code></p>
<dd> Writes the current X server configuration to <i>~/.nvidia-settings-rc</i> file and exits.</p>
<dt><code>nvidia-settings &#8211;query FSAA</code></p>
<dd> Query the value of the full-screen antialiasing setting.</p>
<dt><code>nvidia-settings &#8211;assign RedGamma=2.0 &#8211;assign BlueGamma=2.0 &#8211;assign GreenGamma=2.0</code></p>
<dd> Set the gamma of the screen to 2.0.</dl>
<h2>AUTHOR</h2>
<p> Aaron Plattner<br />
 NVIDIA Corporation</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nvidia-xconfig/">nvidia-xconfig</a></code>(1), <code><a href="/docs/linux/man/1-nvidia-installer/">nvidia-installer</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2010 NVIDIA Corporation. </p>
<h2>Index</h2>
