---
title: "nvidia-xconfig(1)"
name: "nvidia-xconfig"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvidia-xconfig/"
description: "nvidia-xconfig – manipulate X configuration files for the NVIDIA driver"
---

<h2 class="name">NAME</h2>
<p> nvidia-xconfig &#8211; manipulate X configuration files for the NVIDIA driver </p>
<h2>SYNOPSIS</h2>
<p> <code>nvidia-xconfig</code> [ <i>options</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>nvidia-xconfig</code> is a tool intended to provide basic control over configuration options available in the NVIDIA X driver. </p>
<p> <code>nvidia-xconfig</code> performs its operations in several steps:</p>
<dl>
<dt>1)</p>
<dd> The system X configuration file is found and read into memory. If no configuration file can be found, <code>nvidia-xconfig</code> generates one from scratch using default settings; in this case, <code>nvidia-xconfig</code> will write the configuration to <i>/etc/X11/xorg.conf</i></p>
<dt>2)</p>
<dd> The configuration in memory is modified to support the NVIDIA driver. This consists of changing the display driver to &quot;nvidia&quot;, removing the commands to load the &quot;GLcore&quot; and &quot;dri&quot; modules, and adding the command to load the &quot;glx&quot; module.</p>
<dt>3)</p>
<dd> The configuration in memory is modified according to the options specified on the command line. Please see the NVIDIA README for a description of the NVIDIA X configuration file options. Note that <code>nvidia-xconfig </code> does not perform any validation of the X configuration file options requested on the command line; X configuration file option validation is left for the NVIDIA X driver.</p>
<dt>4)</p>
<dd> The configuration is written back to the file from which it was read. A backup of the original configuration is created with &quot;.backup&quot; appended. For example, if your X configuration is <i>/etc/X11/xorg.conf</i> then <code>nvidia-xconfig</code> will copy it to <i>/etc/X11/xorg.conf.backup</i> before writing the new configuration. The <code>&#8211;post-tree (-T)</code> option can be used to print the new configuration to standard out in tree form instead. This option is useful to see what <code>nvidia-xconfig</code> will do while leaving the original configuration intact.</dl>
<p> The source code to <code>nvidia-xconfig</code> is released under the GPL and available here: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; &lt; <a rel="nofollow" href="https://download.nvidia.com/XFree86/nvidia-xconfig/">https://download.nvidia.com/XFree86/nvidia-xconfig/</a> &gt; </p>
<p> Patches are welcome.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c </code><i>XCONFIG</i><code>, &#8211;xconfig=</code><i>XCONFIG</i></p>
<dd> Use <i>XCONFIG</i> as the input X config file; if this option is not specified, then the same search path used by the X server will be used to find the X configuration file.</p>
<dt><code>-o </code><i>OUTPUT-XCONFIG</i><code>, &#8211;output-xconfig=</code><i>OUTPUT-XCONFIG</i></p>
<dd> Use <i>OUTPUT-XCONFIG</i> as the output X configuration file; if this option is not specified, then the input X configuration filename will also be used as the output X configuration filename.</p>
<dt><code>-s, &#8211;silent</code></p>
<dd> Run silently; no messages will be printed to stdout, except for warning and error messages to stderr.</p>
<dt><code>-t, &#8211;tree</code></p>
<dd> Read the X configuration file, print to stdout the X configuration data in a tree format, and exit.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Print the nvidia-xconfig version and exit.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Print usage information for the common commandline options and exit.</p>
<dt><code>-A, &#8211;advanced-help</code></p>
<dd> Print usage information for the common commandline options as well as the advanced options, and then exit.</dl>
<h2>ADVANCED OPTIONS</h2>
<dl>
<dt><code>&#8211;acpid-socket-path=</code><i>ACPID-SOCKET-PATH</i><code>, &#8211;no-acpid-socket-path</code></p>
<dd> Set this option to specify an alternate path to the Linux ACPI daemon (acpid)&#8217;s socket, which the NVIDIA X driver will use to connect to acpid.</p>
<dt><code>&#8211;add-argb-glx-visuals, &#8211;no-add-argb-glx-visuals</code></p>
<dd> Enables or disables support for OpenGL rendering into 32-bit ARGB windows and pixmaps.</p>
<dt><code>&#8211;allow-glx-with-composite, &#8211;no-allow-glx-with-composite</code></p>
<dd> Enable or disable the &quot;AllowGLXWithComposite&quot; X configuration option.</p>
<dt><code>&#8211;busid=</code><i>BUSID</i><code>, &#8211;no-busid</code></p>
<dd> This option writes the specified BusID to the device section of the X configuration file. If there are multiple device sections, then it adds the BusID field to each of them. To add the BusID to only a specific device or screen section, use the &#8216;&#8211;device&#8217; or &#8216;&#8211;screen&#8217; options.</p>
<dt><code>&#8211;preserve-busid, &#8211;no-preserve-busid</code></p>
<dd> By default, nvidia-xconfig preserves the existing BusID in the X configuration file only if there are multiple X screens configured for the X server. Use &#8216;&#8211;preserve-busid&#8217; or &#8216;&#8211;no-preserve-busid&#8217; to force the BusID to be preserved or not preserved, overriding the default behavior.</p>
<dt><code>&#8211;cool-bits=</code><i>COOL-BITS</i><code>, &#8211;no-cool-bits</code></p>
<dd> Enable or disable the &quot;Coolbits&quot; X configuration option. Setting this option will enable support in the NV-CONTROL X extension for manipulating GPU clock and GPU fan control settings. Default value is 0. For fan control set it to 4. WARNING: this may cause system damage and void warranties.</p>
<dt><code>&#8211;composite, &#8211;no-composite</code></p>
<dd> Enable or disable the &quot;Composite&quot; X extension.</p>
<dt><code>&#8211;connected-monitor=</code><i>CONNECTED-MONITOR</i><code>, &#8211;no-connected-monitor</code></p>
<dd> Enable or disable the &quot;ConnectedMonitor&quot; X configuration option; setting this option forces the X driver to behave as if the specified display devices are connected to the GPU.</p>
<dt><code>&#8211;connect-to-acpid, &#8211;no-connect-to-acpid</code></p>
<dd> Enable or disable the &quot;ConnectToAcpid&quot; X configuration option. If this option is set, the NVIDIA X driver will attempt to connect to the Linux ACPI daemon (acpid). Set this option to off to prevent the X driver from attempting to connect to acpid.</p>
<dt><code>&#8211;constant-dpi, &#8211;no-constant-dpi</code></p>
<dd> Enable or disable the &quot;ConstantDPI&quot; X configuration option, which controls whether the NVIDIA X driver maintains a constant dots per inch (DPI) value by recomputing the reported size in millimeters of the X screen when XRandR changes the size in pixels of the X screen.</p>
<dt><code>&#8211;custom-edid=</code><i>CUSTOM-EDID</i><code>, &#8211;no-custom-edid</code></p>
<dd> Enable or disable the &quot;CustomEDID&quot; X configuration option; setting this option forces the X driver to use the EDID specified.This option is a semicolon-separated list of pairs of display device names and filename pairs; e.g &quot;CRT-0: mp\did.bin&quot;. Note that a display device name must always be specified even if only one EDID is specified.</p>
<dt><code>&#8211;dac-8bit, &#8211;no-dac-8bit</code></p>
<dd> Most Quadro parts by default use a 10 bit color look up table (LUT) by default; setting this option to TRUE forces these graphics chips to use an 8 bit (LUT).</p>
<dt><code>-d </code><i>DEPTH</i><code>, &#8211;depth=</code><i>DEPTH</i></p>
<dd> Set the default depth to <i>DEPTH</i> ; valid values for <i>DEPTH</i> are 8, 15, 16, 24, and 30.</p>
<dt><code>&#8211;device=</code><i>DEVICE</i></p>
<dd> The nvidia-xconfig utility operates on one or more devices in the X configuration file. If this option is specified, the device named <i>DEVICE</i> in the X configuration file will be used. If this option is not specified, all the devices within the X configuration file will be used.</p>
<dt><code>&#8211;disable-glx-root-clipping, &#8211;no-disable-glx-root-clipping</code></p>
<dd> Disable or enable clipping OpenGL rendering to the root window via the &quot;DisableGLXRootClipping&quot; X configuration option.</p>
<dt><code>&#8211;damage-events, &#8211;no-damage-events</code></p>
<dd> Use OS-level events to notify the X server when a direct-rendering client has performed rendering that needs to be composited to the screen. Improves performance when using GLX with the composite extension.</p>
<dt><code>&#8211;preserve-driver-name</code></p>
<dd> By default nvidia-xconfig changes the display driver to &quot;nvidia&quot; for all configured X screens; this option preserves the existing driver name of each X screen.</p>
<dt><code>&#8211;egpu, &#8211;no-egpu</code></p>
<dd> Enable or disable the &quot;AllowExternalGpus&quot; X configuration option.</p>
<dt><code>-a, &#8211;enable-all-gpus</code></p>
<dd> Delete all existing X screens in the current configuration, then configure an X screen on every GPU in your system.</p>
<dt><code>&#8211;exact-mode-timings-dvi, &#8211;no-exact-mode-timings-dvi</code></p>
<dd> Forces the initialization of the X server with the exact timings specified in the ModeLine.</p>
<dt><code>-E </code><i>FILE</i><code>, &#8211;extract-edids-from-file=</code><i>FILE</i></p>
<dd> Extract any raw EDID byte blocks contained in the specified X log file <i>LOG</i> ; raw EDID bytes are printed by the NVIDIA X driver to the X log as hexadecimal when verbose logging is enabled with the &quot;-logverbose 6&quot; X server commandline option. Any extracted EDIDs are then written as binary data to individual files. These files can later be used by the NVIDIA X driver through the &quot;CustomEDID&quot; X configuration option.</p>
<dt><code>&#8211;extract-edids-output-file=</code><i>FILENAME</i></p>
<dd> When the &#8216;&#8211;extract-edids-from-file&#8217; option is used, nvidia-xconfig writes any extracted EDID to a file, typically &quot;edid.bin&quot; in the current directory. Use this option to specify an alternate filename. Note that nvidia-xconfig, if necessary, will append a unique number to the EDID filename, to avoid overwriting existing files (e.g., &quot;edid.bin.1&quot; if &quot;edid.bin&quot; already exists).</p>
<dt><code>&#8211;flatpanel-properties=</code><i>FLATPANEL-PROPERTIES</i><code>, &#8211;no-flatpanel-properties</code></p>
<dd> Set the flat panel properties. The supported properties are &#8216;dithering&#8217; and &#8216;ditheringmode&#8217;. Please see the NVIDIA README &#8216;Appendix B. X Config Options&#8217; for more details on the possible values and syntax.</p>
<dt><code>&#8211;flip, &#8211;no-flip</code></p>
<dd> Enable or disable OpenGL flipping</p>
<dt><code>&#8211;force-generate</code></p>
<dd> Force generation of a new X config file, ignoring any existing system X config file. This is not typically recommended, as things like the mouse protocol, keyboard layout, font paths, etc, are setup by your Unix distribution. While nvidia-xconfig can attempt to infer these values, it is best to use your Unix distribution&#8217;s X config file for the basis of anything that nvidia-xconfig creates.</p>
<dt><code>&#8211;force-stereo-flipping, &#8211;no-force-stereo-flipping</code></p>
<dd> Normally, stereo flipping is only performed when a stereo drawable is visible. This option forces stereo flipping even when no stereo drawables are visible.</p>
<dt><code>&#8211;handle-special-keys=</code><i>WHEN</i><code>, &#8211;no-handle-special-keys</code></p>
<dd> Specify when the X server should use the builtin keyboard handler to process special key combinations (such as Ctrl+Alt+Backspace); see the X configuration man page for details. The value of <i>WHEN</i> can be &#8216;Always&#8217;, &#8216;Never&#8217;, or &#8216;WhenNeeded&#8217;.</p>
<dt><code>&#8211;include-implicit-metamodes, &#8211;no-include-implicit-metamodes</code></p>
<dd> Enable or disable the &quot;IncludeImplicitMetaModes&quot; X configuration option.</p>
<dt><code>&#8211;keyboard=</code><i>KEYBOARD</i></p>
<dd> When generating a new X configuration file (which happens when no system X configuration file can be found, or the &#8216;&#8211;force-generate&#8217; option is specified), use <i>KEYBOARD</i> as the keyboard type, rather than attempting to probe the system for the keyboard type. For a list of possible keyboard types, see the &#8216;&#8211;keyboard-list&#8217; option.</p>
<dt><code>&#8211;keyboard-driver=</code><i>DRIVER</i></p>
<dd> In most cases nvidia-xconfig can automatically determine the correct keyboard driver to use (either &#8216;kbd&#8217; or &#8216;keyboard&#8217;). Use this option to override what nvidia-xconfig detects. Typically, if you are using an X.Org X server, use &#8216;kdb&#8217;; if you are using an XFree86 X server, use &#8216;keyboard&#8217;.</p>
<dt><code>&#8211;keyboard-list</code></p>
<dd> Print to stdout the available keyboard types recognized by the &#8216;&#8211;keyboard&#8217; option, and then exit.</p>
<dt><code>&#8211;layout=</code><i>LAYOUT</i></p>
<dd> The nvidia-xconfig utility operates on a Server Layout within the X configuration file. If this option is specified, the layout named <i>LAYOUT</i> in the X configuration file will be used. If this option is not specified, the first Server Layout in the X configuration file is used.</p>
<dt><code>&#8211;mode=</code><i>MODE</i></p>
<dd> Add the specified mode to the mode list.</p>
<dt><code>&#8211;mode-debug, &#8211;no-mode-debug</code></p>
<dd> Enable or disable the &quot;ModeDebug&quot; X configuration option; when enabled, this option causes the X driver to print verbose details about mode validation to the X log file.</p>
<dt><code>&#8211;mode-list=</code><i>MODELIST</i></p>
<dd> Remove all existing modes from the X configuration&#8217;s modelist and add the one(s) specified in the <i>MODELIST</i> string.</p>
<dt><code>&#8211;remove-mode=</code><i>MODE</i></p>
<dd> Remove the specified mode from the mode list.</p>
<dt><code>&#8211;metamodes=</code><i>METAMODES</i></p>
<dd> Add the MetaMode X configuration option with the value <i>METAMODES</i> which will replace any existing MetaMode option already in the X configuration file.</p>
<dt><code>&#8211;mouse=</code><i>MOUSE</i></p>
<dd> When generating a new X configuration file (which happens when no system X configuration file can be found, or the &#8216;&#8211;force-generate&#8217; option is specified), use <i>MOUSE</i> as the mouse type, rather than attempting to probe the system for the mouse type. For a list of possible mouse types, see the &#8216;&#8211;mouse-list&#8217; option.</p>
<dt><code>&#8211;mouse-list</code></p>
<dd> Print to stdout the available mouse types recognized by the &#8216;&#8211;mouse&#8217; option, and then exit.</p>
<dt><code>&#8211;multigpu=</code><i>MULTIGPU</i><code>, &#8211;no-multigpu</code></p>
<dd> Enable or disable MultiGPU. Valid values for <i>MULTIGPU</i> are &#8216;Off&#8217; and &#8216;Mosaic&#8217;.</p>
<dt><code>&#8211;multisample-compatibility, &#8211;no-multisample-compatibility</code></p>
<dd> Enable or disable the use of separate front and back multisample buffers.</p>
<dt><code>&#8211;nvidia-cfg-path=</code><i>PATH</i></p>
<dd> The nvidia-cfg library is used to communicate with the NVIDIA kernel module to query basic properties of every GPU in the system. This library is typically only used by nvidia-xconfig when configuring multiple X screens. This option tells nvidia-xconfig where to look for this library (in case it cannot find it on its own). This option should normally not be needed.</p>
<dt><code>&#8211;only-one-x-screen</code></p>
<dd> Disable all but one X screen.</p>
<dt><code>&#8211;overlay, &#8211;no-overlay</code></p>
<dd> Enable or disable the &quot;Overlay&quot; X configuration option.</p>
<dt><code>&#8211;cioverlay, &#8211;no-cioverlay</code></p>
<dd> Enable or disable the color index overlay.</p>
<dt><code>&#8211;overlay-default-visual, &#8211;no-overlay-default-visual</code></p>
<dd> Enable or disable the &quot;OverlayDefaultVisual&quot; X configuration option.</p>
<dt><code>&#8211;transparent-index=</code><i>INDEX</i><code>, &#8211;no-transparent-index</code></p>
<dd> Pixel to use as transparent when using color index overlays. Valid values for <i>TRANSPARENT-INDEX</i> are 0-255.</p>
<dt><code>-T, &#8211;post-tree</code></p>
<dd> Like the &#8216;&#8211;tree&#8217; option, but goes through the full process of applying any user requested updates to the X configuration, before printing the final configuration to stdout in a tree format. Effectively, this option just causes the configuration to be printed to stdout as a tree instead of writing the results to file.</p>
<dt><code>&#8211;power-connector-check, &#8211;no-power-connector-check</code></p>
<dd> Disable or enable the &quot;NoPowerConnectorCheck&quot; X configuration option.</p>
<dt><code>&#8211;probe-all-gpus, &#8211;no-probe-all-gpus</code></p>
<dd> Disable or enable the &quot;ProbeAllGpus&quot; X configuration option.</p>
<dt><code>&#8211;query-gpu-info</code></p>
<dd> Print information about all recognized NVIDIA GPUs in the system.</p>
<dt><code>&#8211;registry-dwords=</code><i>REGISTRY-DWORDS</i><code>, &#8211;no-registry-dwords</code></p>
<dd> Enable or disable the &quot;RegistryDwords&quot; X configuration option.</p>
<dt><code>&#8211;render-accel, &#8211;no-render-accel</code></p>
<dd> Enable or disable the &quot;RenderAccel&quot; X configuration option.</p>
<dt><code>&#8211;render-extension, &#8211;no-render-extension</code></p>
<dd> Disable or enable the &quot;NoRenderExtension&quot; X configuration option.</p>
<dt><code>&#8211;screen=</code><i>SCREEN</i></p>
<dd> The nvidia-xconfig utility operates on one or more screens within a Server Layout in the X configuration file. If this option is specified, the screen named <i>SCREEN</i> in the X configuration file will be used. If this option is not specified, all screens within the selected Server Layout in the X configuration file will be used used.</p>
<dt><code>&#8211;separate-x-screens, &#8211;no-separate-x-screens</code></p>
<dd> A GPU that supports multiple simultaneous display devices can either drive these display devices in a single X screen, or as separate X screens. When the &#8216;&#8211;separate-x-screens&#8217; option is specified, each GPU on which an X screen is currently configured will be updated to have two or more (depending on the capabilities of that GPU) X screens configured. The &#8216;&#8211;no-separate-x-screens&#8217; option will remove any extra configured X screens on each GPU. Please see the NVIDIA README description of &quot;Separate X Screens on One GPU&quot; for further details.</p>
<dt><code>&#8211;x-screens-per-gpu=</code><i>X-SCREENS-PER-GPU</i></p>
<dd> A GPU that supports multiple simultaneous display devices can either drive these display devices in a single X screen, or as separate X screens. When the &#8216;&#8211;x-screens-per-gpu=&lt;quantity&gt;&#8217; option is specified, each GPU on which an X screen is currently configured will be updated to have &lt;quantity&gt; X screens. &lt;quantity&gt; has to be greater than 0. Setting &lt;quantity&gt; to 1 is equivalent to specifying the &#8216;&#8211;no-separate-x-screens&#8217; option. Please see the NVIDIA README description of &quot;Separate X Screens on One GPU&quot; for further details.</p>
<dt><code>&#8211;sli=</code><i>SLI</i><code>, &#8211;no-sli</code></p>
<dd> Enable or disable SLI. Valid values for <i>SLI</i> are &#8216;Off&#8217; and &#8216;Mosaic&#8217;.</p>
<dt><code>&#8211;stereo=</code><i>STEREO</i><code>, &#8211;no-stereo</code></p>
<dd> Enable or disable the stereo mode. Valid values for <i>STEREO</i> are: 0 (Disabled), 1 (DDC glasses), 2 (Blueline glasses), 3 (Onboard stereo), 4 (multi-display clone mode stereo), 5 (SeeReal digital flat panel), 6 (Sharp3D digital flat panel), 7 (Arisawa/Hyundai/Zalman/Pavione/Miracube), 8 (3D DLP), 9 (3D DLP INV), 10 (NVIDIA 3D VISION), 11 (NVIDIA 3D VISION PRO), 12 (HDMI 3D), 13 (Tridelity SL).</p>
<dt><code>&#8211;thermal-configuration-check, &#8211;no-thermal-configuration-check</code></p>
<dd> Disable or enable the &quot;ThermalConfigurationCheck&quot; X configuration option.</p>
<dt><code>&#8211;tv-standard=</code><i>TV-STANDARD</i><code>, &#8211;no-tv-standard</code></p>
<dd> Enable or disable the &quot;TVStandard&quot; X configuration option. Valid values for &quot;TVStandard&quot; are: &quot;PAL-B&quot;, &quot;PAL-D&quot;, &quot;PAL-G&quot;, &quot;PAL-H&quot;, &quot;PAL-I&quot;, &quot;PAL-K1&quot;, &quot;PAL-M&quot;, &quot;PAL-N&quot;, &quot;PAL-NC&quot;, &quot;NTSC-J&quot;, &quot;NTSC-M&quot;, &quot;HD480i&quot;, &quot;HD480p&quot;, &quot;HD720p&quot;, &quot;HD1080i&quot;, &quot;HD1080p&quot;, &quot;HD576i&quot;, &quot;HD576p&quot;.</p>
<dt><code>&#8211;tv-out-format=</code><i>TV-OUT-FORMAT</i><code>, &#8211;no-tv-out-format</code></p>
<dd> Enable or disable the &quot;TVOutFormat&quot; X configuration option. Valid values for &quot;TVOutFormat&quot; are: &quot;SVIDEO&quot; and &quot;COMPOSITE&quot;.</p>
<dt><code>&#8211;metamode-orientation=</code><i>ORIENTATION</i><code>, &#8211;no-metamode-orientation</code></p>
<dd> Specify the MetaModeOrientation. Valid values for <i>ORIENTATION</i> are: &quot;RightOf&quot; (the default), &quot;LeftOf&quot;, &quot;Above&quot;, &quot;Below&quot;, or &quot;Clone&quot;.</p>
<dt><code>&#8211;nvidia-xinerama-info, &#8211;no-nvidia-xinerama-info</code></p>
<dd> Enable or disable providing Xinerama information from the NVIDIA X driver.</p>
<dt><code>&#8211;nvidia-xinerama-info-order=</code><i>NVIDIA-XINERAMA-INFO-ORDER</i><code>, &#8211;no-nvidia-xinerama-info-order</code></p>
<dd> Enable or disable the &quot;nvidiaXineramaInfoOrder&quot; X configuration option. <i>NVIDIA-XINERAMA-INFO-ORDER</i> is a comma-separated list of display device names that describe the order in which nvidiaXineramaInfo should be reported. E.g., &quot;CRT, DFP, TV&quot;.</p>
<dt><code>&#8211;ubb, &#8211;no-ubb</code></p>
<dd> Enable or disable the &quot;UBB&quot; X configuration option.</p>
<dt><code>&#8211;use-edid, &#8211;no-use-edid</code></p>
<dd> Enable or disable use of the EDID (Extended Display Identification Data) from your display device(s). The EDID will be used for driver operations such as building lists of available modes, determining valid frequency ranges, and computing the DPI (Dots Per Inch). This option defaults to TRUE (the NVIDIA X driver will use the EDID, when available). It is NOT recommended that you use this option to globally disable use of the EDID; instead, use &#8216;&#8211;no-use-edid-freqs&#8217; or &#8216;&#8211;no-use-edid-dpi&#8217; to disable specific uses of the EDID.</p>
<dt><code>&#8211;use-edid-dpi, &#8211;no-use-edid-dpi</code></p>
<dd> Enable or disable use of the physical size information in the display device&#8217;s EDID, if any, to compute the DPI (Dots Per Inch) of the X screen. This option defaults to TRUE (the NVIDIA X driver uses the EDID&#8217;s physical size, when available, to compute the DPI).</p>
<dt><code>&#8211;use-edid-freqs, &#8211;no-use-edid-freqs</code></p>
<dd> Enable or disable use of the HorizSync and VertRefresh ranges given in a display device&#8217;s EDID, if any. EDID provided range information will override the HorizSync and VertRefresh ranges specified in the Monitor section. This option defaults to TRUE (the NVIDIA X driver will use frequency information from the EDID, when available).</p>
<dt><code>&#8211;use-display-device=</code><i>DISPLAY-DEVICE</i><code>, &#8211;no-use-display-device</code></p>
<dd> Force the X driver to use the display device specified.</p>
<dt><code>&#8211;use-events, &#8211;no-use-events</code></p>
<dd> Enable or disable &quot;UseEvents&quot; X configuration option. Setting this option will enable the X driver to use the system events in some cases when it is waiting for the hardware. With this option X driver sets an event handler and waits for the hardware through the poll() system call. This option defaults to FALSE.</p>
<dt><code>&#8211;virtual=</code><i>WIDTHxHEIGHT</i><code>, &#8211;no-virtual</code></p>
<dd> Specify the virtual screen resolution.</p>
<dt><code>&#8211;x-prefix=</code><i>X-PREFIX</i></p>
<dd> The X installation prefix; the default is /usr/X11R6/. Only under rare circumstances should this option be needed.</p>
<dt><code>&#8211;xinerama, &#8211;no-xinerama</code></p>
<dd> Enable or disable Xinerama.</p>
<dt><code>&#8211;color-space=</code><i>COLORSPACE</i><code>, &#8211;no-color-space</code></p>
<dd> Enable or disable the &quot;ColorSpace&quot; X configuration option. Valid values for &quot;COLORSPACE&quot; are: &quot;RGB&quot; and &quot;YCbCr444&quot;.</p>
<dt><code>&#8211;color-range=</code><i>COLORRANGE</i><code>, &#8211;no-color-range</code></p>
<dd> Sets the &quot;ColorRange&quot; X configuration option. Valid values for &quot;COLORRANGE&quot; are: &quot;Full&quot; and &quot;Limited&quot;.</p>
<dt><code>&#8211;3dvision-usb-path=</code><i>3DVISION-USB-PATH</i></p>
<dd> Set this option to specify the sysfs path of the connected USB dongle.</p>
<dt><code>&#8211;3dvisionpro-config-file=</code><i>3DVISIONPRO-CONFIG-FILE</i></p>
<dd> Set this option to specify the NVIDIA 3DVisionPro configuration file. Ensure X server has a read and write access permissions to this file. NVIDIA X driver stores the hub and the pairing configuration in this file to re-use across X restarts. If this option is not provided, 3D VisionPro configuration will not be stored.</p>
<dt><code>&#8211;3dvision-display-type=</code><i>3DVISION-DISPLAY-TYPE</i><code>, &#8211;no-3dvision-display-type</code></p>
<dd> When NVIDIA 3D Vision is enabled with a non 3D Vision ready display, use this option to specify the display type. Valid values are: 0 (Assume it is a CRT), 1 (Assume it is a DLP) and 2 (Assume it is a DLP TV and enable the checkerboard output).</p>
<dt><code>&#8211;base-mosaic, &#8211;no-base-mosaic</code></p>
<dd> Enable or disable the &quot;BaseMosaic&quot; X configuration option.</p>
<dt><code>&#8211;restore-original-backup</code></p>
<dd> Restore a backup of the X configuration that was made before any changes were made by nvidia-xconfig, if such a backup is available. This type of backup is made by nvidia-xconfig before it modifies an X configuration file that it has not previously touched; this is assumed to be an X configuration file that predates the involvement of the NVIDIA X driver. As an example, nvidia-xconfig will copy an X configuration file at /etc/X11/xorg.conf to /etc/X11/xorg.conf.nvidia-xconfig-original the first time it makes changes to that file.</p>
<dt><code>&#8211;allow-empty-initial-configuration, &#8211;no-allow-empty-initial-configuration</code></p>
<dd> Allow the X server to start even if no connected display devices could be detected.</p>
<dt><code>&#8211;inband-stereo-signaling, &#8211;no-inband-stereo-signaling</code></p>
<dd> Enable or disable the &quot;InbandStereoSignaling&quot; X configuration option.</p>
<dt><code>&#8211;force-yuv-420, &#8211;no-force-yuv-420</code></p>
<dd> Enable or disable the &quot;ForceYUV420&quot; X configuration option. If the current display and GPU both support uncompressed RGB 4:4:4 output and YUV 4:2:0 compressed output with the current mode, then RGB 4:4:4 output is selected by default. This option forces the use of YUV 4:2:0 output (where supported) instead.</p>
<dt><code>&#8211;force-composition-pipeline=</code><i>FORCE-COMPOSITION-PIPELINE</i><code>, &#8211;no-force-composition-pipeline</code></p>
<dd> Enable or disable the &quot;ForceCompositionPipeline&quot; X configuration option.</p>
<dt><code>&#8211;force-full-composition-pipeline=</code><i>FORCE-FULL-COMPOSITION-PIPELINE</i><code>, &#8211;no-force-full-composition-pipeline</code></p>
<dd> Enable or disable the &quot;ForceFullCompositionPipeline&quot; X configuration option.</p>
<dt><code>&#8211;allow-hmd=</code><i>ALLOW-HMD</i><code>, &#8211;no-allow-hmd</code></p>
<dd> Enable or disable the &quot;AllowHMD&quot; X configuration option.</p>
<dt><code>&#8211;prime, &#8211;no-prime</code></p>
<dd> Enable PRIME for the generated X config file. Cannot be run with &#8211;no-busid or &#8211;no-allow-empty-initial-configuration. On a system with more than 1 GPU, specify the GPU to use for PRIME with &#8211;busid or the first available will be chosen. Note that to enable PRIME it is necessary to run &quot;xrandr &#8211;setprovideroutputsource modesetting NVIDIA-0&quot; and &quot;xrandr &#8211;auto&quot; after completion.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>nvidia-xconfig</code></p>
<dd> Reads an existing X config file and adapts it to use the NVIDIA driver. If no X config file can be found, a new one is created at /etc/X11/xorg.conf with default settings.</p>
<dt><code>nvidia-xconfig &#8211;post-tree &#8211;metamode-orientation=clone</code></p>
<dd> Reads the existing X configuration file, adds the MetaModeOrientation option, and then prints the resulting config file to standard out in tree form. The configuration file is not modified.</p>
<dt><code>nvidia-xconfig &#8211;enable-all-gpus</code></p>
<dd> Examines the system and configures an X screen for each display device it finds.</p>
<dt><code>nvidia-xconfig &#8211;mode=</code><i>1600&#215;1200</i></p>
<dd> Adds a 1600&#215;1200 mode to an existing X configuration.</p>
<dt><code>nvidia-xconfig &#8211;mode-list=</code><i>1600&#215;1200 1280&#215;1024</i></p>
<dd> Removes any existing modes from the X configuration file, replacing them with &quot;1600&#215;1200&quot; and &quot;1280&#215;1024&quot;.</p>
<dt><code>nvidia-xconfig &#8211;metamodes=</code><i>1024&#215;768 +0+0, 1024&#215;768 +1024+0</i></p>
<dd> Adds the MetaMode &quot;1024&#215;768 +0+0, 1024&#215;768 +1024+0&quot; to the existing X configuration file, replacing any existing MetaModes X configuration option.</p>
<dt><code>nvidia-xconfig &#8211;only-one-x-screen &#8211;sli=Auto</code></p>
<dd> Configures the X server to have just one X screen that will use SLI when available.</dl>
<h2>AUTHOR</h2>
<p> Aaron Plattner<br />
 NVIDIA Corporation</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nvidia-settings/">nvidia-settings</a></code>(1), <i>/usr/share/doc/NVIDIA_GLX-1.0/README.txt</i></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005-2010 NVIDIA Corporation. </p>
<h2>Index</h2>
