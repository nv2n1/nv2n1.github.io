---
title: "xorg-conf-d(5)"
name: "xorg-conf-d"
section: "5"
letter: "x"
url: "/docs/linux/man/5-xorg-conf-d/"
description: "xorg.conf, xorg.conf.d – configuration files for Xorg X server"
---

<p>xorg.conf, xorg.conf.d &#8211; configuration files for Xorg X server</p>
<h2>Introduction</h2>
<p><code>Xorg</code> supports several mechanisms for supplying/obtaining configuration and run-time parameters: command line options, environment variables, the xorg.conf and xorg.conf.d configuration files, auto-detection, and fallback defaults. When the same information is supplied in more than one way, the highest precedence mechanism is used. The list of mechanisms is ordered from highest precedence to lowest. Note that not all parameters can be supplied via all methods. The available command line options and environment variables (and some defaults) are described in the <a href="/docs/linux/man/1-xserver/">Xserver</a>(1) and <a href="/docs/linux/man/1-xorg/">Xorg</a>(1) manual pages. Most configuration file parameters, with their defaults, are described below. Driver and module specific configuration parameters are described in the relevant driver or module manual page.</p>
<h2>Description</h2>
<p><code>Xorg</code> uses a configuration file called <i>xorg.conf</i> and files ending in the suffix <i>.conf</i> from the directory <i>xorg.conf.d</i> for its initial setup. The <i>xorg.conf</i> configuration file is searched for in the following places when the server is started as a normal user: </p>
<dl>
<dd>
<pre><i>/etc/X11/</i>&lt;cmdline&gt;
<i>/usr/etc/X11/</i>&lt;cmdline&gt;
<i>/etc/X11/</i><code>$XORGCONFIG</code>
<i>/usr/etc/X11/</i><code>$XORGCONFIG</code>
<i>/etc/X11/xorg.conf</i>
<i>/etc/xorg.conf</i>
<i>/usr/etc/X11/xorg.conf.</i>&lt;hostname&gt;
<i>/usr/etc/X11/xorg.conf</i>
<i>/usr/lib/X11/xorg.conf.</i>&lt;hostname&gt;
<i>/usr/lib/X11/xorg.conf</i></pre>
</dl>
<p> where <i>&lt;cmdline&gt;</i> is a relative path (with no &#8220;..&#8221; components) specified with the <code>-config</code> command line option, <code>$XORGCONFIG</code> is the relative path (with no &#8220;..&#8221; components) specified by that environment variable, and <i>&lt;hostname&gt;</i> is the machine&#8217;s hostname as reported by <code><a href="/docs/linux/man/3-gethostname/">gethostname</a></code>(3). </p>
<p> When the Xorg server is started by the &#8220;root&#8221; user, the config file search locations are as follows: </p>
<dl>
<dd>
<pre>&lt;cmdline&gt;
<i>/etc/X11/</i>&lt;cmdline&gt;
<i>/usr/etc/X11/</i>&lt;cmdline&gt;
<code>$XORGCONFIG</code>
<i>/etc/X11/</i><code>$XORGCONFIG</code>
<i>/usr/etc/X11/</i><code>$XORGCONFIG</code>
<i>/etc/X11/xorg.conf</i>
<i>/etc/xorg.conf</i>
<i>/usr/etc/X11/xorg.conf.</i>&lt;hostname&gt;
<i>/usr/etc/X11/xorg.conf</i>
<i>/usr/lib/X11/xorg.conf.</i>&lt;hostname&gt;
<i>/usr/lib/X11/xorg.conf</i></pre>
</dl>
<p> where <i>&lt;cmdline&gt;</i> is the path specified with the <code>-config</code> command line option (which may be absolute or relative), <code>$XORGCONFIG</code> is the path specified by that environment variable (absolute or relative), <code>$HOME</code> is the path specified by that environment variable (usually the home directory), and <i>&lt;hostname&gt;</i> is the machine&#8217;s hostname as reported by <code><a href="/docs/linux/man/3-gethostname/">gethostname</a></code>(3). </p>
<p> Additional configuration files are searched for in the following directories when the server is started as a normal user: </p>
<dl>
<dd>
<pre><i>/etc/X11/</i>&lt;cmdline&gt;
<i>/etc/X11/</i>&lt;cmdline&gt;
<i>/etc/X11/xorg.conf.d</i>
<i>/etc/X11/xorg.conf.d</i></pre>
</dl>
<p> where <i>&lt;cmdline&gt;</i> is a relative path (with no &#8220;..&#8221; components) specified with the <code>-configdir</code> command line option. </p>
<p> When the Xorg server is started by the &#8220;root&#8221; user, the config directory search locations are as follows: </p>
<dl>
<dd>
<pre>&lt;cmdline&gt;
<i>/etc/X11/</i>&lt;cmdline&gt;
<i>/etc/X11/</i>&lt;cmdline&gt;
<i>/etc/X11/xorg.conf.d</i>
<i>/etc/X11/xorg.conf.d</i></pre>
</dl>
<p> where <i>&lt;cmdline&gt;</i> is the path specified with the <code>-configdir</code> command line option (which may be absolute or relative). </p>
<p> Finally, configuration files will also be searched for in a directory reserved for system use. This is to separate configuration files from the vendor or 3rd party packages from those of local administration. These files are found in the following directory: </p>
<dl>
<dd>
<pre><i>/usr/share/X11/xorg.conf.d</i></pre>
</dl>
<p> The <i>xorg.conf</i> and <i>xorg.conf.d</i> files are composed of a number of sections which may be present in any order, or omitted to use default configuration values. Each section has the form: </p>
<dl>
<dd>
<pre><code>Section &#34;</code><i>SectionName</i><code>&#34;</code>
 <i>SectionEntry</i>
 ...
<code>EndSection</code></pre>
</dl>
<p> The section names are: </p>
<dl>
<dd>
<pre><code>Files </code>File pathnames
<code>ServerFlags </code>Server flags
<code>Module </code>Dynamic module loading
<code>Extensions </code>Extension enabling
<code>InputDevice </code>Input device description
<code>InputClass </code>Input class description
<code>OutputClass </code>Output class description
<code>Device </code>Graphics device description
<code>VideoAdaptor </code>Xv video adaptor description
<code>Monitor </code>Monitor description
<code>Modes </code>Video modes descriptions
<code>Screen </code>Screen configuration
<code>ServerLayout </code>Overall layout
<code>DRI </code>DRI-specific configuration
<code>Vendor </code>Vendor-specific configuration</pre>
</dl>
<p> The following obsolete section names are still recognised for compatibility purposes. In new config files, the <code>InputDevice</code> section should be used instead. </p>
<dl>
<dd>
<pre><code>Keyboard </code>Keyboard configuration
<code>Pointer </code>Pointer/mouse configuration</pre>
</dl>
<p> The old <code>XInput</code> section is no longer recognised. </p>
<p> The <code>ServerLayout</code> sections are at the highest level. They bind together the input and output devices that will be used in a session. The input devices are described in the <code>InputDevice</code> sections. Output devices usually consist of multiple independent components (e.g., a graphics board and a monitor). These multiple components are bound together in the <code>Screen</code> sections, and it is these that are referenced by the <code>ServerLayout</code> section. Each <code>Screen</code> section binds together a graphics board and a monitor. The graphics boards are described in the <code>Device</code> sections, and the monitors are described in the <code>Monitor</code> sections. </p>
<p> Config file keywords are case-insensitive, and &#8220;_&#8221; characters are ignored. Most strings (including <code>Option</code> names) are also case-insensitive, and insensitive to white space and &#8220;_&#8221; characters. </p>
<p> Each config file entry usually takes up a single line in the file. They consist of a keyword, which is possibly followed by one or more arguments, with the number and types of the arguments depending on the keyword. The argument types are: </p>
<dl>
<dd>
<pre><code>Integer </code>an integer number in decimal, hex or octal
<code>Real </code>a floating point number
<code>String </code>a string enclosed in double quote marks (&#34;)</pre>
</dl>
<p> Note: hex integer values must be prefixed with &#8220;0x&#8221;, and octal values with &#8220;0&#8221;. </p>
<p> A special keyword called <code>Option</code> may be used to provide free-form data to various components of the server. The <code>Option</code> keyword takes either one or two string arguments. The first is the option name, and the optional second argument is the option value. Some commonly used option value types include: </p>
<dl>
<dd>
<pre><code>Integer </code>an integer number in decimal, hex or octal
<code>Real </code>a floating point number
<code>String </code>a sequence of characters
<code>Boolean </code>a boolean value (see below)
<code>Frequency </code>a frequency value (see below)</pre>
</dl>
<p> Note that <i>all</i> <code>Option</code> values, not just strings, must be enclosed in quotes. </p>
<p> Boolean options may optionally have a value specified. When no value is specified, the option&#8217;s value is <code>TRUE</code>. The following boolean option values are recognised as <code>TRUE</code>: </p>
<dl>
<dd><code>1</code>, <code>on</code>, <code>true</code>, <code>yes</code></dl>
<p> and the following boolean option values are recognised as <code>FALSE</code>: </p>
<dl>
<dd><code>0</code>, <code>off</code>, <code>false</code>, <code>no</code></dl>
<p> If an option name is prefixed with &#34;<code>No</code>&#34;, then the option value is negated. </p>
<p> Example: the following option entries are equivalent: </p>
<dl>
<dd>
<pre><code>Option &#34;Accel&#34; &#34;Off&#34;</code>
<code>Option &#34;NoAccel&#34;</code>
<code>Option &#34;NoAccel&#34; &#34;On&#34;</code>
<code>Option &#34;Accel&#34; &#34;false&#34;</code>
<code>Option &#34;Accel&#34; &#34;no&#34;</code></pre>
</dl>
<p> Frequency option values consist of a real number that is optionally followed by one of the following frequency units: </p>
<dl>
<dd><code>Hz</code>, <code>k</code>, <code>kHz</code>, <code>M</code>, <code>MHz</code></dl>
<p> When the unit name is omitted, the correct units will be determined from the value and the expectations of the appropriate range of the value. It is recommended that the units always be specified when using frequency option values to avoid any errors in determining the value.</p>
<h2>Files Section</h2>
<p>The <code>Files</code> section is used to specify some path names required by the server. Some of these paths can also be set from the command line (see <code><a href="/docs/linux/man/1-xserver/">Xserver</a></code>(1) and <code><a href="/docs/linux/man/1-xorg/">Xorg</a></code>(1)). The command line settings override the values specified in the config file. The <code>Files</code> section is optional, as are all of the entries that may appear in it. </p>
<p> The entries that can appear in this section are:</p>
<dl>
<dt><code>FontPath &#34;</code><i>path</i><code>&#34;</code></p>
<dd>sets the search path for fonts. This path is a comma separated list of font path elements which the Xorg server searches for font databases. Multiple <code>FontPath</code> entries may be specified, and they will be concatenated to build up the fontpath used by the server. Font path elements can be absolute directory paths, catalogue directories or a font server identifier. The formats of the later two are explained below:</dl>
<dl>
<dd>Catalogue directories: </p>
<dl>
<dd>Catalogue directories can be specified using the prefix <code>catalogue:</code> before the directory name. The directory can then be populated with symlinks pointing to the real font directories, using the following syntax in the symlink name: </p>
<dl>
<dd><i>&lt;identifier&gt;</i>:<i>[attribute]:</i>pri=<i>&lt;priority&gt;</i></dl>
<p> where <i>&lt;identifier&gt;</i> is an alphanumeric identifier, <i>[attribute]</i> is an attribute which will be passed to the underlying FPE and <i>&lt;priority&gt;</i> is a number used to order the fontfile FPEs. Examples: </p>
<dl>
<dd>
<pre><i>75dpi:unscaled:pri=20 -&gt; /usr/share/X11/fonts/75dpi</i>
<i>gscript:pri=60 -&gt; /usr/share/fonts/default/ghostscript</i>
<i>misc:unscaled:pri=10 -&gt; /usr/share/X11/fonts/misc</i></pre>
</dl>
</dl>
</dl>
<dl>
<dd>Font server identifiers: </p>
<dl>
<dd>Font server identifiers have the form:</p>
<dl>
<dd><i>&lt;trans&gt;</i>/<i>&lt;hostname&gt;</i>:<i>&lt;port-number&gt;</i></dl>
<p> where <i>&lt;trans&gt;</i> is the transport type to use to connect to the font server (e.g., <code>unix</code> for UNIX-domain sockets or <code>tcp</code> for a TCP/IP connection), <i>&lt;hostname&gt;</i> is the hostname of the machine running the font server, and <i>&lt;port-number&gt;</i> is the port number that the font server is listening on (usually 7100).</dl>
<p> When this entry is not specified in the config file, the server falls back to the compiled-in default font path, which contains the following font path elements (which can be set inside a catalogue directory): </p>
<dl>
<dd>
<pre><i>/usr/share/fonts/X11/misc/</i>
<i>/usr/share/fonts/X11/TTF/</i>
<i>/usr/share/fonts/X11/OTF/</i>
<i>/usr/share/fonts/X11/Type1/</i>
<i>/usr/share/fonts/X11/100dpi/</i>
<i>/usr/share/fonts/X11/75dpi/</i></pre>
</dl>
<p> Font path elements that are found to be invalid are removed from the font path when the server starts up.</dl>
<dl>
<dt><code>ModulePath &#34;</code><i>path</i><code>&#34;</code></p>
<dd>sets the search path for loadable Xorg server modules. This path is a comma separated list of directories which the Xorg server searches for loadable modules loading in the order specified. Multiple <code>ModulePath</code> entries may be specified, and they will be concatenated to build the module search path used by the server. The default module path is</dl>
<dl>
<dd>/usr/lib/xorg/modules</dl>
<dl>
<dt><code>XkbDir &#34;</code><i>path</i><code>&#34;</code></p>
<dd>sets the base directory for keyboard layout files. The <code>-xkbdir</code> command line option can be used to override this. The default directory is</dl>
<dl>
<dd>/usr/share/X11/xkb</dl>
<h2>Serverflags Section</h2>
<p>In addition to options specific to this section (described below), the <code>ServerFlags</code> section is used to specify some global Xorg server options. All of the entries in this section are <code>Options</code>, although for compatibility purposes some of the old style entries are still recognised. Those old style entries are not documented here, and using them is discouraged. The <code>ServerFlags</code> section is optional, as are the entries that may be specified in it. </p>
<p> <code>Options</code> specified in this section (with the exception of the <code>&#34;DefaultServerLayout&#34;</code> <code>Option</code>) may be overridden by <code>Options</code> specified in the active <code>ServerLayout</code> section. Options with command line equivalents are overridden when their command line equivalent is used. The options recognised by this section are:</p>
<dl>
<dt><code>Option &#34;Debug&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>This comma-separated list provides a way to control various debugging switches from the config file. At the moment the only defined value is <code>dmabuf_capable</code> which instructs glamor to enable some unstable buffer management code.</p>
<dt><code>Option &#34;DefaultServerLayout&#34; &#34;</code><i>layout-id</i><code>&#34;</code></p>
<dd>This specifies the default <code>ServerLayout</code> section to use in the absence of the <code>-layout</code> command line option.</p>
<dt><code>Option &#34;DontVTSwitch&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This disallows the use of the <code>Ctrl+Alt+F</code><i>n</i> sequence (where F<i>n</i> refers to one of the numbered function keys). That sequence is normally used to switch to another &#34;virtual terminal&#34; on operating systems that have this feature. When this option is enabled, that key sequence has no special meaning and is passed to clients. Default: off.</p>
<dt><code>Option &#34;DontZap&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This disallows the use of the <code>Terminate_Server</code> XKB action (usually on Ctrl+Alt+Backspace, depending on XKB options). This action is normally used to terminate the Xorg server. When this option is enabled, the action has no effect. Default: off.</p>
<dt><code>Option &#34;DontZoom&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This disallows the use of the <code>Ctrl+Alt+Keypad-Plus</code> and <code>Ctrl+Alt+Keypad-Minus</code> sequences. These sequences allows you to switch between video modes. When this option is enabled, those key sequences have no special meaning and are passed to clients. Default: off.</p>
<dt><code>Option &#34;DisableVidModeExtension&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This disables the parts of the VidMode extension used by the xvidtune client that can be used to change the video modes. Default: the VidMode extension is enabled.</p>
<dt><code>Option &#34;AllowNonLocalXvidtune&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This allows the xvidtune client (and other clients that use the VidMode extension) to connect from another host. Default: off.</p>
<dt><code>Option &#34;AllowMouseOpenFail&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This tells the <a href="/docs/linux/man/4-mousedrv/">mousedrv</a>(4) and <a href="/docs/linux/man/4-vmmouse/">vmmouse</a>(4) drivers to not report failure if the mouse device can&#8217;t be opened/initialised. It has no effect on the <a href="/docs/linux/man/4-evdev/">evdev</a>(4) or other drivers. Default: false.</p>
<dt><code>Option &#34;BlankTime&#34; &#34;</code><i>time</i><code>&#34;</code></p>
<dd>sets the inactivity timeout for the <code>blank</code> phase of the screensaver. <i>time</i> is in minutes. This is equivalent to the Xorg server&#8217;s <code>-s</code> flag, and the value can be changed at run-time with <code><a href="/docs/linux/man/1-xset/">xset</a>(1).</code> Default: 10 minutes.</p>
<dt><code>Option &#34;StandbyTime&#34; &#34;</code><i>time</i><code>&#34;</code></p>
<dd>sets the inactivity timeout for the <code>standby</code> phase of DPMS mode. <i>time</i> is in minutes, and the value can be changed at run-time with <code><a href="/docs/linux/man/1-xset/">xset</a>(1).</code> Default: 10 minutes. This is only suitable for VESA DPMS compatible monitors, and may not be supported by all video drivers. It is only enabled for screens that have the <code>&#34;DPMS&#34;</code> option set (see the MONITOR section below).</p>
<dt><code>Option &#34;SuspendTime&#34; &#34;</code><i>time</i><code>&#34;</code></p>
<dd>sets the inactivity timeout for the <code>suspend</code> phase of DPMS mode. <i>time</i> is in minutes, and the value can be changed at run-time with <code><a href="/docs/linux/man/1-xset/">xset</a>(1).</code> Default: 10 minutes. This is only suitable for VESA DPMS compatible monitors, and may not be supported by all video drivers. It is only enabled for screens that have the <code>&#34;DPMS&#34;</code> option set (see the MONITOR section below).</p>
<dt><code>Option &#34;OffTime&#34; &#34;</code><i>time</i><code>&#34;</code></p>
<dd>sets the inactivity timeout for the <code>off</code> phase of DPMS mode. <i>time</i> is in minutes, and the value can be changed at run-time with <code><a href="/docs/linux/man/1-xset/">xset</a>(1).</code> Default: 10 minutes. This is only suitable for VESA DPMS compatible monitors, and may not be supported by all video drivers. It is only enabled for screens that have the <code>&#34;DPMS&#34;</code> option set (see the MONITOR section below).</p>
<dt><code>Option &#34;MaxClients&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Set the maximum number of clients allowed to connect to the X server. Acceptable values are 64, 128, 256 or 512.</p>
<dt><code>Option &#34;NoPM&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disables something to do with power management events. Default: PM enabled on platforms that support it.</p>
<dt><code>Option &#34;Xinerama&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>enable or disable XINERAMA extension. Default is disabled.</p>
<dt><code>Option &#34;IndirectGLX&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>enable or disable indirect GLX contexts. Indirect GLX contexts are disabled by default.</p>
<dt><code>Option &#34;DRI2&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>enable or disable DRI2. DRI2 is disabled by default.</p>
<dt><code>Option &#34;GlxVisuals&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>This option controls how many GLX visuals the GLX modules sets up. The default value is <code>typical</code>, which will setup up a typical subset of the GLXFBConfigs provided by the driver as GLX visuals. Other options are <code>minimal</code>, which will set up the minimal set allowed by the GLX specification and <code>all</code> which will setup GLX visuals for all GLXFBConfigs.</p>
<dt><code>Option &#34;UseDefaultFontPath&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Include the default font path even if other paths are specified in xorg.conf. If enabled, other font paths are included as well. Enabled by default.</p>
<dt><code>Option &#34;IgnoreABI&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Allow modules built for a different, potentially incompatible version of the X server to load. Disabled by default.</p>
<dt><code>Option &#34;AutoAddDevices&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>If this option is disabled, then no devices will be added from the HAL or udev backends. Enabled by default.</p>
<dt><code>Option &#34;AutoEnableDevices&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>If this option is disabled, then the devices will be added (and the DevicePresenceNotify event sent), but not enabled, thus leaving policy up to the client. Enabled by default.</p>
<dt><code>Option &#34;AutoAddGPU&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>If this option is disabled, then no GPU devices will be added from the udev backend. Enabled by default. (May need to be disabled to setup Xinerama).</p>
<dt><code>Option &#34;AutoBindGPU&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>If enabled then secondary GPUs will be automatically set up as output-sinks and offload-sources. Making e.g. laptop outputs connected only to the secondary GPU directly available for use without needing to run &quot;xrandr &#8211;setprovideroutputsource&quot;. Enabled by default.</p>
<dt><code>Option &#34;Log&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>This option controls whether the log is flushed and/or synced to disk after each message. Possible values are <code>flush</code> or <code>sync</code>. Unset by default.</dl>
<h2>Module Section</h2>
<p>The <code>Module</code> section is used to specify which Xorg server modules should be loaded. This section is ignored when the Xorg server is built in static form. The type of modules normally loaded in this section are Xorg server extension modules. Most other module types are loaded automatically when they are needed via other mechanisms. The <code>Module</code> section is optional, as are all of the entries that may be specified in it. </p>
<p> Entries in this section may be in two forms. The first and most commonly used form is an entry that uses the <code>Load</code> keyword, as described here:</p>
<dl>
<dt><code>Load &#34;</code><i>modulename</i><code>&#34;</code></p>
<dd>This instructs the server to load the module called <i>modulename</i>. The module name given should be the module&#8217;s standard name, not the module file name. The standard name is case-sensitive, and does not include the &#8220;lib&#8221; or &#8220;cyg&#8221; prefixes, or the &#8220;.so&#8221; or &#8220;.dll&#8221; suffixes.</dl>
<dl>
<dd>Example: the DRI extension module can be loaded with the following entry: </p>
<dl>
<dd><code>Load &#34;dri&#34;</code></dl>
</dl>
<dl>
<dt><code>Disable &#34;</code><i>modulename</i><code>&#34;</code></p>
<dd>This instructs the server to not load the module called <i>modulename</i>. Some modules are loaded by default in the server, and this overrides that default. If a <code>Load</code> instruction is given for the same module, it overrides the <code>Disable</code> instruction and the module is loaded. The module name given should be the module&#8217;s standard name, not the module file name. As with the <code>Load</code> instruction, the standard name is case-sensitive, and does not include the &quot;lib&quot; prefix, or the &quot;.a&quot;, &quot;.o&quot;, or &quot;.so&quot; suffixes.</dl>
<p> The second form of entry is a <code>SubSection,</code> with the subsection name being the module name, and the contents of the <code>SubSection</code> being <code>Options</code> that are passed to the module when it is loaded. </p>
<p> Example: the extmod module (which contains a miscellaneous group of server extensions) can be loaded, with the XFree86-DGA extension disabled by using the following entry: </p>
<dl>
<dd>
<pre><code>SubSection &#34;extmod&#34;</code>
<code> Option &#34;omit XFree86-DGA&#34;</code>
<code>EndSubSection</code></pre>
</dl>
<p> Modules are searched for in each directory specified in the <code>ModulePath</code> search path, and in the drivers, extensions, input, internal, and multimedia subdirectories of each of those directories. In addition to this, operating system specific subdirectories of all the above are searched first if they exist. </p>
<p> To see what extension modules are available, check the extensions subdirectory under: </p>
<dl>
<dd>
<pre>/usr/lib/xorg/modules</pre>
</dl>
<p> The &#8220;extmod&#8221;, &#8220;dbe&#8221;, &#8220;dri&#8221;, &#8220;dri2&#8221;, &#8220;glx&#8221;, and &#8220;record&#8221; extension modules are loaded automatically, if they are present, unless disabled with &#34;Disable&#34; entries. It is recommended that at very least the &#8220;extmod&#8221; extension module be loaded. If it isn&#8217;t, some commonly used server extensions (like the SHAPE extension) will not be available.</p>
<h2>Extensions Section</h2>
<p>The <code>Extensions</code> section is used to specify which X11 protocol extensions should be enabled or disabled. The <code>Extensions</code> section is optional, as are all of the entries that may be specified in it. </p>
<p> Entries in this section are listed as Option statements with the name of the extension as the first argument, and a boolean value as the second. The extension name is case-sensitive, and matches the form shown in the output of &#34;Xorg -extension ?&#34;. </p>
<dl>
<dd>Example: the MIT-SHM extension can be disabled with the following entry: </p>
<dl>
<dd>
<pre><code>Section &#34;Extensions&#34;</code>
<code> Option &#34;MIT-SHM&#34; &#34;Disable&#34;</code>
<code>EndSection</code></pre>
</dl>
</dl>
<h2>Inputdevice Section</h2>
<p>The config file may have multiple <code>InputDevice</code> sections. Recent X servers employ HAL or udev backends for input device enumeration and input hotplugging. It is usually not necessary to provide <code>InputDevice</code> sections in the xorg.conf if hotplugging is in use (i.e. AutoAddDevices is enabled). If hotplugging is enabled, <code>InputDevice</code> sections using the <code>mouse, kbd</code> and <code>vmmouse</code> driver will be ignored. </p>
<p> If hotplugging is disabled, there will normally be at least two: one for the core (primary) keyboard and one for the core pointer. If either of these two is missing, a default configuration for the missing ones will be used. In the absence of an explicitly specified core input device, the first <code>InputDevice</code> marked as <code>CorePointer</code> (or <code>CoreKeyboard</code>) is used. If there is no match there, the first <code>InputDevice</code> that uses the &#8220;mouse&#8221; (or &#8220;kbd&#8221;) driver is used. The final fallback is to use built-in default configurations. Currently the default configuration may not work as expected on all platforms. </p>
<p> <code>InputDevice</code> sections have the following format: </p>
<dl>
<dd>
<pre><code>Section &#34;InputDevice&#34;</code>
<code> Identifier &#34;</code><i>name</i><code>&#34;</code>
<code> Driver &#34;</code><i>inputdriver</i><code>&#34;</code>
<i> options</i>
<i> ...</i>
<code>EndSection</code></pre>
</dl>
<p> The <code>Identifier</code> and <code>Driver</code> entries are required in all <code>InputDevice</code> sections. All other entries are optional. </p>
<p> The <code>Identifier</code> entry specifies the unique name for this input device. The <code>Driver</code> entry specifies the name of the driver to use for this input device. When using the loadable server, the input driver module &#34;<i>inputdriver</i>&#34; will be loaded for each active <code>InputDevice</code> section. An <code>InputDevice</code> section is considered active if it is referenced by an active <code>ServerLayout</code> section, if it is referenced by the <code>-keyboard</code> or <code>-pointer</code> command line options, or if it is selected implicitly as the core pointer or keyboard device in the absence of such explicit references. The most commonly used input drivers are <code><a href="/docs/linux/man/4-evdev/">evdev</a></code>(4) on Linux systems, and <code><a href="/docs/linux/man/4-kbd/">kbd</a></code>(4) and <code><a href="/docs/linux/man/4-mousedrv/">mousedrv</a></code>(4) on other platforms. </p>
<p> <code>InputDevice</code> sections recognise some driver-independent <code>Options</code>, which are described here. See the individual input driver manual pages for a description of the device-specific options.</p>
<dl>
<dt><code>Option &#34;AutoServerLayout&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Always add the device to the ServerLayout section used by this instance of the server. This affects implied layouts as well as explicit layouts specified in the configuration and/or on the command line.</p>
<dt><code>Option &#34;CorePointer&#34;</code></p>
<dd>Deprecated, see <code>Floating</code></p>
<dt><code>Option &#34;CoreKeyboard&#34;</code></p>
<dd>Deprecated, see <code>Floating</code></p>
<dt><code>Option &#34;AlwaysCore&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Deprecated, see <code>Floating</code></p>
<dt><code>Option &#34;SendCoreEvents&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Deprecated, see <code>Floating</code> </p>
<dt><code>Option &#34;Floating&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>When enabled, the input device is set up floating and does not report events through any master device or control a cursor. The device is only available to clients using the X Input Extension API. This option is disabled by default. The options <code>CorePointer,</code> <code>CoreKeyboard,</code> <code>AlwaysCore,</code> and <code>SendCoreEvents,</code> are the inverse of option <code>Floating</code> (i.e. <code>SendCoreEvents &#34;on&#34;</code> is equivalent to <code>Floating &#34;off&#34;</code> ). </p>
<p> This option controls the startup behavior only, a device may be reattached or set floating at runtime.</p>
<dt><code>Option &#34;TransformationMatrix&#34; &#34;</code><i>a</i><i>b</i><i>c</i><i>d</i><i>e</i><i>f</i><i>g</i><i>h</i><i>i</i><code>&#34;</code></p>
<dd>Specifies the 3&#215;3 transformation matrix for absolute input devices. The input device will be bound to the area given in the matrix. In most configurations, &quot;a&quot; and &quot;e&quot; specify the width and height of the area the device is bound to, and &quot;c&quot; and &quot;f&quot; specify the x and y offset of the area. The value range is 0 to 1, where 1 represents the width or height of all root windows together, 0.5 represents half the area, etc. The values represent a 3&#215;3 matrix, with the first, second and third group of three values representing the first, second and third row of the matrix, respectively. The identity matrix is &quot;1 0 0 0 1 0 0 0 1&quot;.</dl>
<h3>Pointer Acceleration</h3>
<p>For pointing devices, the following options control how the pointer is accelerated or decelerated with respect to physical device motion. Most of these can be adjusted at runtime, see the <a href="/docs/linux/man/1-xinput/">xinput</a>(1) man page for details. Only the most important acceleration options are discussed here.</p>
<dl>
<dt><code>Option &#34;AccelerationProfile&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Select the profile. In layman&#8217;s terms, the profile constitutes the &quot;feeling&quot; of the acceleration. More formally, it defines how the transfer function (actual acceleration as a function of current device velocity and acceleration controls) is constructed. This is mainly a matter of personal preference.</dl>
<dl>
<dd>
<pre><code> 0 classic (mostly compatible)</code>
<code>-1 none (only constant deceleration is applied)</code>
<code> 1 device-dependent</code>
<code> 2 polynomial (polynomial function)</code>
<code> 3 smooth linear (soft knee, then linear)</code>
<code> 4 simple (normal when slow, otherwise accelerated)</code>
<code> 5 power (power function)</code>
<code> 6 linear (more speed, more acceleration)</code>
<code> 7 limited (like linear, but maxes out at threshold)</code></pre>
</dl>
<dl>
<dt><code>Option &#34;ConstantDeceleration&#34; &#34;</code><i>real</i><code>&#34;</code></p>
<dd>Makes the pointer go <code>deceleration</code> times slower than normal. Most useful for high-resolution devices. A value between 0 and 1 will speed up the pointer.</p>
<dt><code>Option &#34;AdaptiveDeceleration&#34; &#34;</code><i>real</i><code>&#34;</code></p>
<dd>Allows to actually decelerate the pointer when going slow. At most, it will be <code>adaptive deceleration</code> times slower. Enables precise pointer placement without sacrificing speed.</p>
<dt><code>Option &#34;AccelerationScheme&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Selects the scheme, which is the underlying algorithm.</dl>
<dl>
<dd>
<pre><code>predictable default algorithm (behaving more predictable)</code>
<code>lightweight old acceleration code (as specified in the X protocol spec)</code>
<code>none no acceleration or deceleration</code></pre>
</dl>
<dl>
<dt><code>Option &#34;AccelerationNumerator&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>
<dt><code>Option &#34;AccelerationDenominator&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Set numerator and denominator of the acceleration factor. The acceleration factor is a rational which, together with threshold, can be used to tweak profiles to suit the users needs. The <code>simple</code> and <code>limited</code> profiles use it directly (i.e. they accelerate by the factor), for other profiles it should hold that a higher acceleration factor leads to a faster pointer. Typically, 1 is unaccelerated and values up to 5 are sensible.</p>
<dt><code>Option &#34;AccelerationThreshold&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Set the threshold, which is roughly the velocity (usually device units per 10 ms) required for acceleration to become effective. The precise effect varies with the profile however. </p>
</dl>
<h2>Inputclass Section</h2>
<p>The config file may have multiple <code>InputClass</code> sections. These sections are optional and are used to provide configuration for a class of input devices as they are automatically added. An input device can match more than one <code>InputClass</code> section. Each class can override settings from a previous class, so it is best to arrange the sections with the most generic matches first. </p>
<p> <code>InputClass</code> sections have the following format: </p>
<dl>
<dd>
<pre><code>Section &#34;InputClass&#34;</code>
<code> Identifier &#34;</code><i>name</i><code>&#34;</code>
<i> entries</i>
<i> ...</i>
<i> options</i>
<i> ...</i>
<code>EndSection</code></pre>
</dl>
<p> The <code>Identifier</code> entry is required in all <code>InputClass</code> sections. All other entries are optional. </p>
<p> The <code>Identifier</code> entry specifies the unique name for this input class. The <code>Driver</code> entry specifies the name of the driver to use for this input device. After all classes have been examined, the &#34;<i>inputdriver</i>&#34; module from the first <code>Driver</code> entry will be enabled when using the loadable server. </p>
<p> When an input device is automatically added, its characteristics are checked against all <code>InputClass</code> sections. Each section can contain optional entries to narrow the match of the class. If none of the optional entries appear, the <code>InputClass</code> section is generic and will match any input device. If more than one of these entries appear, they all must match for the configuration to apply. </p>
<p> There are two types of match entries used in <code>InputClass</code> sections. The first allows various tokens to be matched against attributes of the device. An entry can be constructed to match attributes from different devices by separating arguments with a &#8216;|&#8217; character. Multiple entries of the same type may be supplied to add multiple matching conditions on the same attribute. For example: </p>
<dl>
<dd>
<pre><code>Section &#34;InputClass&#34;</code>
<code> Identifier &#34;My Class&#34;</code>
<code> # product string must contain example and</code>
<code> # either gizmo or gadget</code>
<code> MatchProduct &#34;example&#34;</code>
<code> MatchProduct &#34;gizmo|gadget&#34;</code>
<code> NoMatchDriver &#34;drivername&#34;</code>
<i> ...</i>
<code>EndSection</code></pre>
</dl>
<dl>
<dt><code>MatchProduct &#34;</code><i>matchproduct</i><code>&#34;</code></p>
<dd>This entry can be used to check if the substring &#34;<i>matchproduct</i>&#34; occurs in the device&#8217;s product name.</p>
<dt><code>MatchVendor &#34;</code><i>matchvendor</i><code>&#34;</code></p>
<dd>This entry can be used to check if the substring &#34;<i>matchvendor</i>&#34; occurs in the device&#8217;s vendor name.</p>
<dt><code>MatchDevicePath &#34;</code><i>matchdevice</i><code>&#34;</code></p>
<dd>This entry can be used to check if the device file matches the &#34;<i>matchdevice</i>&#34; pathname pattern.</p>
<dt><code>MatchOS &#34;</code><i>matchos</i><code>&#34;</code></p>
<dd>This entry can be used to check if the operating system matches the case-insensitive &#34;<i>matchos</i>&#34; string. This entry is only supported on platforms providing the <code><a href="/docs/linux/man/2-uname/">uname</a></code>(2) system call.</p>
<dt><code>MatchPnPID &#34;</code><i>matchpnp</i><code>&#34;</code></p>
<dd>The device&#8217;s Plug and Play (PnP) ID can be checked against the &#34;<i>matchpnp</i>&#34; shell wildcard pattern.</p>
<dt><code>MatchUSBID &#34;</code><i>matchusb</i><code>&#34;</code></p>
<dd>The device&#8217;s USB ID can be checked against the &#34;<i>matchusb</i>&#34; shell wildcard pattern. The ID is constructed as lowercase hexadecimal numbers separated by a &#8216;:&#8217;. This is the same format as the <code><a href="/docs/linux/man/8-lsusb/">lsusb</a></code>(8) program.</p>
<dt><code>MatchDriver &#34;</code><i>matchdriver</i><code>&#34;</code></p>
<dd>Check the case-sensitive string &#34;<i>matchdriver</i>&#34; against the currently configured driver of the device. Ordering of sections using this entry is important since it will not match unless the driver has been set by the config backend or a previous <code>InputClass</code> section.</p>
<dt><code>MatchTag &#34;</code><i>matchtag</i><code>&#34;</code></p>
<dd>This entry can be used to check if tags assigned by the config backend matches the &#34;<i>matchtag</i>&#34; pattern. A match is found if at least one of the tags given in &#34;<i>matchtag</i>&#34; matches at least one of the tags assigned by the backend.</p>
<dt><code>MatchLayout &#34;</code><i>matchlayout</i><code>&#34;</code></p>
<dd>Check the case-sensitive string &#34;<i>matchlayout</i>&#34; against the currently active <code>ServerLayout</code> section. The empty string &quot;&quot; matches an implicit layout which appears if no named <code>ServerLayout</code> sections have been found.</dl>
<p> The above directives have equivalents for negative matching with the <code>NoMatchProduct,</code> <code>NoMatchVendor,</code> <code>NoMatchDevicePath,</code> <code>NoMatchOS,</code> <code>NoMatchPnPID,</code> <code>NoMatchUSBID,</code> <code>NoMatchDriver,</code> <code>NoMatchTag,</code> and <code>NoMatchLayout</code> directives. These NoMatch directives match if the subsequent match is not met by the device. </p>
<p> The second type of entry is used to match device types. These entries take a boolean argument similar to <code>Option</code> entries.</p>
<dl>
<dt><code>MatchIsKeyboard &#34;</code><i>bool</i><code>&#34;</code></p>
<dd>
<dt><code>MatchIsPointer &#34;</code><i>bool</i><code>&#34;</code></p>
<dd>
<dt><code>MatchIsJoystick &#34;</code><i>bool</i><code>&#34;</code></p>
<dd>
<dt><code>MatchIsTablet &#34;</code><i>bool</i><code>&#34;</code></p>
<dd>
<dt><code>MatchIsTabletPad &#34;</code><i>bool</i><code>&#34;</code></p>
<dd>
<dt><code>MatchIsTouchpad &#34;</code><i>bool</i><code>&#34;</code></p>
<dd>
<dt><code>MatchIsTouchscreen &#34;</code><i>bool</i><code>&#34;</code></p>
<dd></dl>
<p> When an input device has been matched to the <code>InputClass</code> section, any <code>Option</code> entries are applied to the device. One <code>InputClass</code> specific <code>Option</code> is recognized. See the <code>InputDevice</code> section above for a description of the remaining <code>Option</code> entries.</p>
<dl>
<dt><code>Option &#34;Ignore&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This optional entry specifies that the device should be ignored entirely, and not added to the server. This can be useful when the device is handled by another program and no X events should be generated.</dl>
<h2>Outputclass Section</h2>
<p>The config file may have multiple <code>OutputClass</code> sections. These sections are optional and are used to provide configuration for a class of output devices as they are automatically added. An output device can match more than one <code>OutputClass</code> section. Each class can override settings from a previous class, so it is best to arrange the sections with the most generic matches first. </p>
<p> <code>OutputClass</code> sections have the following format: </p>
<dl>
<dd>
<pre><code>Section &#34;OutputClass&#34;</code>
<code> Identifier &#34;</code><i>name</i><code>&#34;</code>
<i> entries</i>
<i> ...</i>
<code>EndSection</code></pre>
</dl>
<p> The <code>Identifier</code> entry is required in all <code>OutputClass</code> sections. All other entries are optional. </p>
<p> The <code>Identifier</code> entry specifies the unique name for this output class. The <code>Driver</code> entry specifies the name of the driver to use for this output device. After all classes have been examined, the &#34;<i>outputdriver</i>&#34; module from the first <code>Driver</code> entry will be enabled when using the loadable server. </p>
<p> When an output device is automatically added, its characteristics are checked against all <code>OutputClass</code> sections. Each section can contain optional entries to narrow the match of the class. If none of the optional entries appear, the <code>OutputClass</code> section is generic and will match any output device. If more than one of these entries appear, they all must match for the configuration to apply. </p>
<p> The following list of tokens can be matched against attributes of the device. An entry can be constructed to match attributes from different devices by separating arguments with a &#8216;|&#8217; character. </p>
<p> For example: </p>
<dl>
<dd>
<pre><code>Section &#34;OutputClass&#34;</code>
<code> Identifier &#34;My Class&#34;</code>
<code> # kernel driver must be either foo or bar</code>
<code> MatchDriver &#34;foo|bar&#34;</code>
<i> ...</i>
<code>EndSection</code></pre>
</dl>
<dl>
<dt><code>MatchDriver &#34;</code><i>matchdriver</i><code>&#34;</code></p>
<dd>Check the case-sensitive string &#34;<i>matchdriver</i>&#34; against the kernel driver of the device.</dl>
<p> When an output device has been matched to the <code>OutputClass</code> section, any <code>Option</code> entries are applied to the device. One <code>OutputClass</code> specific <code>Option</code> is recognized. See the <code>Device</code> section below for a description of the remaining <code>Option</code> entries.</p>
<dl>
<dt><code>Option &#34;PrimaryGPU&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>This option specifies that the matched device should be treated as the primary GPU, replacing the selection of the GPU used as output by the firmware. If multiple output devices match an OutputClass section with the PrimaryGPU option set, the first one enumerated becomes the primary GPU.</dl>
<p> A <code>OutputClass</code> Section may contain <code>ModulePath</code> entries. When an output device matches an <code>OutputClass</code> section, any <code>ModulePath</code> entries in that <code>OutputClass</code> are pre-pended to the search path for loadable Xorg server modules. See <code>ModulePath</code> in the <code>Files</code> section for more info.</p>
<h2>Device Section</h2>
<p>The config file may have multiple <code>Device</code> sections. There must be at least one, for the video card being used. </p>
<p> <code>Device</code> sections have the following format: </p>
<dl>
<dd>
<pre><code>Section &#34;Device&#34;</code>
<code> Identifier &#34;</code><i>name</i><code>&#34;</code>
<code> Driver &#34;</code><i>driver</i><code>&#34;</code>
<i> entries</i>
<i> ...</i>
<code>EndSection</code></pre>
</dl>
<p> The <code>Identifier</code> and <code>Driver</code> entries are required in all <code>Device</code> sections. All other entries are optional. </p>
<p> The <code>Identifier</code> entry specifies the unique name for this graphics device. The <code>Driver</code> entry specifies the name of the driver to use for this graphics device. When using the loadable server, the driver module &#34;<i>driver</i>&#34; will be loaded for each active <code>Device</code> section. A <code>Device</code> section is considered active if it is referenced by an active <code>Screen</code> section. </p>
<p> <code>Device</code> sections recognise some driver-independent entries and <code>Options</code>, which are described here. Not all drivers make use of these driver-independent entries, and many of those that do don&#8217;t require them to be specified because the information is auto-detected. See the individual graphics driver manual pages for further information about this, and for a description of the device-specific options. Note that most of the <code>Options</code> listed here (but not the other entries) may be specified in the <code>Screen</code> section instead of here in the <code>Device</code> section.</p>
<dl>
<dt><code>BusID &#34;</code><i>bus-id</i><code>&#34;</code></p>
<dd>This specifies the bus location of the graphics card. For PCI/AGP cards, the <i>bus-id</i> string has the form <code>PCI:</code><i>bus</i><code>@</code><i>domain</i><code>:</code><i>device</i><code>:</code><i>function</i> (e.g., &#8220;PCI:1@0:0:0&#8221; might be appropriate for an AGP card). The &quot;@domain&quot; part can be left out for PCI domain 0. This field is usually optional in single-head configurations when using the primary graphics card. In multi-head configurations, or when using a secondary graphics card in a single-head configuration, this entry is mandatory. Its main purpose is to make an unambiguous connection between the device section and the hardware it is representing. This information can usually be found by running the pciaccess tool scanpci.</p>
<dt><code>Screen </code><i>number</i></p>
<dd>This option is mandatory for cards where a single PCI entity can drive more than one display (i.e., multiple CRTCs sharing a single graphics accelerator and video memory). One <code>Device</code> section is required for each head, and this parameter determines which head each of the <code>Device</code> sections applies to. The legal values of <i>number</i> range from 0 to one less than the total number of heads per entity. Most drivers require that the primary screen (0) be present.</p>
<dt><code>Chipset &#34;</code><i>chipset</i><code>&#34;</code></p>
<dd>This usually optional entry specifies the chipset used on the graphics board. In most cases this entry is not required because the drivers will probe the hardware to determine the chipset type. Don&#8217;t specify it unless the driver-specific documentation recommends that you do.</p>
<dt><code>Ramdac &#34;</code><i>ramdac-type</i><code>&#34;</code></p>
<dd>This optional entry specifies the type of RAMDAC used on the graphics board. This is only used by a few of the drivers, and in most cases it is not required because the drivers will probe the hardware to determine the RAMDAC type where possible. Don&#8217;t specify it unless the driver-specific documentation recommends that you do.</p>
<dt><code>DacSpeed </code><i>speed</i></p>
<dd>
<dt><code>DacSpeed </code><i>speed-8 speed-16 speed-24 speed-32</i></p>
<dd>This optional entry specifies the RAMDAC speed rating (which is usually printed on the RAMDAC chip). The speed is in MHz. When one value is given, it applies to all framebuffer pixel sizes. When multiple values are given, they apply to the framebuffer pixel sizes 8, 16, 24 and 32 respectively. This is not used by many drivers, and only needs to be specified when the speed rating of the RAMDAC is different from the defaults built in to driver, or when the driver can&#8217;t auto-detect the correct defaults. Don&#8217;t specify it unless the driver-specific documentation recommends that you do.</p>
<dt><code>Clocks </code><i>clock &#8230;</i></p>
<dd>specifies the pixel that are on your graphics board. The clocks are in MHz, and may be specified as a floating point number. The value is stored internally to the nearest kHz. The ordering of the clocks is important. It must match the order in which they are selected on the graphics board. Multiple <code>Clocks</code> lines may be specified, and each is concatenated to form the list. Most drivers do not use this entry, and it is only required for some older boards with non-programmable clocks. Don&#8217;t specify this entry unless the driver-specific documentation explicitly recommends that you do.</p>
<dt><code>ClockChip &#34;</code><i>clockchip-type</i><code>&#34;</code></p>
<dd>This optional entry is used to specify the clock chip type on graphics boards which have a programmable clock generator. Only a few Xorg drivers support programmable clock chips. For details, see the appropriate driver manual page.</p>
<dt><code>VideoRam </code><i>mem</i></p>
<dd>This optional entry specifies the amount of video ram that is installed on the graphics board. This is measured in kBytes. In most cases this is not required because the Xorg server probes the graphics board to determine this quantity. The driver-specific documentation should indicate when it might be needed.</p>
<dt><code>MemBase </code><i>baseaddress</i></p>
<dd>This optional entry specifies the memory base address of a graphics board&#8217;s linear frame buffer. This entry is not used by many drivers, and it should only be specified if the driver-specific documentation recommends it.</p>
<dt><code>IOBase </code><i>baseaddress</i></p>
<dd>This optional entry specifies the IO base address. This entry is not used by many drivers, and it should only be specified if the driver-specific documentation recommends it.</p>
<dt><code>ChipID </code><i>id</i></p>
<dd>This optional entry specifies a numerical ID representing the chip type. For PCI cards, it is usually the device ID. This can be used to override the auto-detection, but that should only be done when the driver-specific documentation recommends it.</p>
<dt><code>ChipRev </code><i>rev</i></p>
<dd>This optional entry specifies the chip revision number. This can be used to override the auto-detection, but that should only be done when the driver-specific documentation recommends it.</p>
<dt><code>MatchSeat </code><i>seat-id</i></p>
<dd>Only apply this <code>Device</code> section if X server was started with <code>-seat</code> <i>seat-id</i> option.</p>
<dt><code>Option &#34;ModeDebug&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable printing of additional debugging information about modesetting to the server log.</p>
<dt><code>Option &#34;NoOutputInitialSize&#34; &#34;</code><i>width</i><i>height</i><code>&#34;</code></p>
<dd>Normally, the X server infers the initial screen size based on any connected outputs. However, if no outputs are connected, the X server picks a default screen size of 1024 x 768. This option overrides the default screen size to use when no outputs are connected. In contrast to the &#34;Virtual&#34; Display SubSection entry, which applies unconditionally, &#34;NoOutputInitialSize&#34; is only used if no outputs are detected when the X server starts.</p>
<dt><code>Option &#34;PreferCloneMode&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>If enabled, bring up monitors of a screen in clone mode instead of horizontal extended layout by default. (Defaults to off; the video driver can change the default value, but this option can always override it)</p>
<dt><code>Options</code></p>
<dd>Option flags may be specified in the <code>Device</code> sections. These include driver-specific options and driver-independent options. The former are described in the driver-specific documentation. Some of the latter are described below in the section about the <code>Screen</code> section, and they may also be included here. </p>
</dl>
<h2>Videoadaptor Section</h2>
<p>Nobody wants to say how this works. Maybe nobody knows &#8230;</p>
<h2>Monitor Section</h2>
<p>The config file may have multiple <code>Monitor</code> sections. There should normally be at least one, for the monitor being used, but a default configuration will be created when one isn&#8217;t specified. </p>
<p> <code>Monitor</code> sections have the following format: </p>
<dl>
<dd>
<pre><code>Section &#34;Monitor&#34;</code>
<code> Identifier &#34;</code><i>name</i><code>&#34;</code>
<i> entries</i>
<i> ...</i>
<code>EndSection</code></pre>
</dl>
<p> The only mandatory entry in a <code>Monitor</code> section is the <code>Identifier</code> entry. </p>
<p> The <code>Identifier</code> entry specifies the unique name for this monitor. The <code>Monitor</code> section may be used to provide information about the specifications of the monitor, monitor-specific <code>Options</code>, and information about the video modes to use with the monitor. </p>
<p> With RandR 1.2-enabled drivers, monitor sections may be tied to specific outputs of the video card. Using the name of the output defined by the video driver plus the identifier of a monitor section, one associates a monitor section with an output by adding an option to the Device section in the following format: </p>
<p> <code>Option &#34;Monitor-</code><i>outputname</i><code>&#34; &#34;</code><i>monitorsection</i><code>&#34;</code> </p>
<p> (for example, <code>Option &#34;Monitor-VGA&#34; &#34;VGA monitor&#34;</code> for a VGA output) </p>
<p> In the absence of specific association of monitor sections to outputs, if a monitor section is present the server will associate it with an output to preserve compatibility for previous single-head configurations. </p>
<p> Specifying video modes is optional because the server will use the DDC or other information provided by the monitor to automatically configure the list of modes available. When modes are specified explicitly in the <code>Monitor</code> section (with the <code>Mode</code>, <code>ModeLine</code>, or <code>UseModes</code> keywords), built-in modes with the same names are not included. Built-in modes with different names are, however, still implicitly included, when they meet the requirements of the monitor. </p>
<p> The entries that may be used in <code>Monitor</code> sections are described below.</p>
<dl>
<dt><code>VendorName &#34;</code><i>vendor</i><code>&#34;</code></p>
<dd>This optional entry specifies the monitor&#8217;s manufacturer.</p>
<dt><code>ModelName &#34;</code><i>model</i><code>&#34;</code></p>
<dd>This optional entry specifies the monitor&#8217;s model.</p>
<dt><code>HorizSync </code><i>horizsync-range</i></p>
<dd>gives the range(s) of horizontal sync frequencies supported by the monitor. <i>horizsync-range</i> may be a comma separated list of either discrete values or ranges of values. A range of values is two values separated by a dash. By default the values are in units of kHz. They may be specified in MHz or Hz if <code>MHz</code> or <code>Hz</code> is added to the end of the line. The data given here is used by the Xorg server to determine if video modes are within the specifications of the monitor. This information should be available in the monitor&#8217;s handbook. If this entry is omitted, a default range of 28-33kHz is used.</p>
<dt><code>VertRefresh </code><i>vertrefresh-range</i></p>
<dd>gives the range(s) of vertical refresh frequencies supported by the monitor. <i>vertrefresh-range</i> may be a comma separated list of either discrete values or ranges of values. A range of values is two values separated by a dash. By default the values are in units of Hz. They may be specified in MHz or kHz if <code>MHz</code> or <code>kHz</code> is added to the end of the line. The data given here is used by the Xorg server to determine if video modes are within the specifications of the monitor. This information should be available in the monitor&#8217;s handbook. If this entry is omitted, a default range of 43-72Hz is used.</p>
<dt><code>DisplaySize </code><i>width height</i></p>
<dd>This optional entry gives the width and height, in millimetres, of the picture area of the monitor. If given this is used to calculate the horizontal and vertical pitch (DPI) of the screen.</p>
<dt><code>Gamma </code><i>gamma-value</i></p>
<dd>
<dt><code>Gamma </code><i>red-gamma green-gamma blue-gamma</i></p>
<dd>This is an optional entry that can be used to specify the gamma correction for the monitor. It may be specified as either a single value or as three separate RGB values. The values should be in the range 0.1 to 10.0, and the default is 1.0. Not all drivers are capable of using this information.</p>
<dt><code>UseModes &#34;</code><i>modesection-id</i><code>&#34;</code></p>
<dd>Include the set of modes listed in the <code>Modes</code> section called <i>modesection-id.</i> This makes all of the modes defined in that section available for use by this monitor.</p>
<dt><code>Mode &#34;</code><i>name</i><code>&#34;</code></p>
<dd>This is an optional multi-line entry that can be used to provide definitions for video modes for the monitor. In most cases this isn&#8217;t necessary because the built-in set of VESA standard modes will be sufficient. The <code>Mode</code> keyword indicates the start of a multi-line video mode description. The mode description is terminated with the <code>EndMode</code> keyword. The mode description consists of the following entries:</p>
<dl>
<dd>
<dl>
<dt><code>DotClock </code><i>clock</i></p>
<dd>is the dot (pixel) clock rate to be used for the mode.</p>
<dt><code>HTimings </code><i>hdisp hsyncstart hsyncend htotal</i></p>
<dd>specifies the horizontal timings for the mode.</p>
<dt><code>VTimings </code><i>vdisp vsyncstart vsyncend vtotal</i></p>
<dd>specifies the vertical timings for the mode.</p>
<dt><code>Flags &#34;</code><i>flag</i><code>&#34;</code><i> &#8230;</i></p>
<dd>specifies an optional set of mode flags, each of which is a separate string in double quotes. <code>&#34;Interlace&#34;</code> indicates that the mode is interlaced. <code>&#34;DoubleScan&#34;</code> indicates a mode where each scanline is doubled. <code>&#34;+HSync&#34;</code> and <code>&#34;-HSync&#34;</code> can be used to select the polarity of the HSync signal. <code>&#34;+VSync&#34;</code> and <code>&#34;-VSync&#34;</code> can be used to select the polarity of the VSync signal. <code>&#34;Composite&#34;</code> can be used to specify composite sync on hardware where this is supported. Additionally, on some hardware, <code>&#34;+CSync&#34;</code> and <code>&#34;-CSync&#34;</code> may be used to select the composite sync polarity.</p>
<dt><code>HSkew </code><i>hskew</i></p>
<dd>specifies the number of pixels (towards the right edge of the screen) by which the display enable signal is to be skewed. Not all drivers use this information. This option might become necessary to override the default value supplied by the server (if any). &#8220;Roving&#8221; horizontal lines indicate this value needs to be increased. If the last few pixels on a scan line appear on the left of the screen, this value should be decreased.</p>
<dt><code>VScan </code><i>vscan</i></p>
<dd>specifies the number of times each scanline is painted on the screen. Not all drivers use this information. Values less than 1 are treated as 1, which is the default. Generally, the <code>&#34;DoubleScan&#34;</code> <code>Flag</code> mentioned above doubles this value.</dl>
</dl>
<dt><code>ModeLine &#34;</code><i>name</i><code>&#34;</code><i> mode-description</i></p>
<dd>This entry is a more compact version of the <code>Mode</code> entry, and it also can be used to specify video modes for the monitor. This is a single line format for specifying video modes. In most cases this isn&#8217;t necessary because the built-in set of VESA standard modes will be sufficient.</dl>
<dl>
<dd>The <i>mode-description</i> is in four sections, the first three of which are mandatory. The first is the dot (pixel) clock. This is a single number specifying the pixel clock rate for the mode in MHz. The second section is a list of four numbers specifying the horizontal timings. These numbers are the <i>hdisp</i>, <i>hsyncstart</i>, <i>hsyncend</i>, and <i>htotal</i> values. The third section is a list of four numbers specifying the vertical timings. These numbers are the <i>vdisp</i>, <i>vsyncstart</i>, <i>vsyncend</i>, and <i>vtotal</i> values. The final section is a list of flags specifying other characteristics of the mode. <code>Interlace</code> indicates that the mode is interlaced. <code>DoubleScan</code> indicates a mode where each scanline is doubled. <code>+HSync</code> and <code>-HSync</code> can be used to select the polarity of the HSync signal. <code>+VSync</code> and <code>-VSync</code> can be used to select the polarity of the VSync signal. <code>Composite</code> can be used to specify composite sync on hardware where this is supported. Additionally, on some hardware, <code>+CSync</code> and <code>-CSync</code> may be used to select the composite sync polarity. The <code>HSkew</code> and <code>VScan</code> options mentioned above in the <code>Mode</code> entry description can also be used here.</dl>
<dl>
<dt><code>Option &#34;DPMS&#34; &#34;</code><i>bool</i><code>&#34;</code></p>
<dd>This option controls whether the server should enable the DPMS extension for power management for this screen. The default is to enable the extension.</p>
<dt><code>Option &#34;SyncOnGreen&#34; &#34;</code><i>bool</i><code>&#34;</code></p>
<dd>This option controls whether the video card should drive the sync signal on the green color pin. Not all cards support this option, and most monitors do not require it. The default is off.</p>
<dt><code>Option &#34;Primary&#34; &#34;</code><i>bool</i><code>&#34;</code></p>
<dd>This optional entry specifies that the monitor should be treated as the primary monitor. (RandR 1.2-supporting drivers only)</p>
<dt><code>Option &#34;PreferredMode&#34; &#34;</code><i>name</i><code>&#34;</code></p>
<dd>This optional entry specifies a mode to be marked as the preferred initial mode of the monitor. (RandR 1.2-supporting drivers only)</p>
<dt><code>Option &#34;ZoomModes&#34; &#34;</code><i>name</i><i>name</i><i>&#8230;</i><code>&#34;</code></p>
<dd>This optional entry specifies modes to be marked as zoom modes. It is possible to switch to the next and previous mode via <code>Ctrl+Alt+Keypad-Plus</code> and <code>Ctrl+Alt+Keypad-Minus</code>. All these keypad available modes are selected from the screen mode list. This list is a copy of the compatibility output monitor mode list. Since this output is the output connected to the lowest dot-area monitor, as determined from its largest size mode, that monitor defines the available zoom modes. (RandR 1.2-supporting drivers only)</p>
<dt><code>Option &#34;Position&#34; &#34;</code><i>x</i><i>y</i><code>&#34;</code></p>
<dd>This optional entry specifies the position of the monitor within the X screen. (RandR 1.2-supporting drivers only)</p>
<dt><code>Option &#34;LeftOf&#34; &#34;</code><i>output</i><code>&#34;</code></p>
<dd>This optional entry specifies that the monitor should be positioned to the left of the output (not monitor) of the given name. (RandR 1.2-supporting drivers only)</p>
<dt><code>Option &#34;RightOf&#34; &#34;</code><i>output</i><code>&#34;</code></p>
<dd>This optional entry specifies that the monitor should be positioned to the right of the output (not monitor) of the given name. (RandR 1.2-supporting drivers only)</p>
<dt><code>Option &#34;Above&#34; &#34;</code><i>output</i><code>&#34;</code></p>
<dd>This optional entry specifies that the monitor should be positioned above the output (not monitor) of the given name. (RandR 1.2-supporting drivers only)</p>
<dt><code>Option &#34;Below&#34; &#34;</code><i>output</i><code>&#34;</code></p>
<dd>This optional entry specifies that the monitor should be positioned below the output (not monitor) of the given name. (RandR 1.2-supporting drivers only)</p>
<dt><code>Option &#34;Enable&#34; &#34;</code><i>bool</i><code>&#34;</code></p>
<dd>This optional entry specifies whether the monitor should be turned on at startup. By default, the server will attempt to enable all connected monitors. (RandR 1.2-supporting drivers only)</p>
<dt><code>Option &#34;DefaultModes&#34; &#34;</code><i>bool</i><code>&#34;</code></p>
<dd>This optional entry specifies whether the server should add supported default modes to the list of modes offered on this monitor. By default, the server will add default modes; you should only disable this if you can guarantee that EDID will be available at all times, or if you have added custom modelines which the server can use. (RandR 1.2-supporting drivers only)</p>
<dt><code>Option &#34;MinClock&#34; &#34;</code><i>frequency</i><code>&#34;</code></p>
<dd>This optional entry specifies the minimum dot clock, in kHz, that is supported by the monitor.</p>
<dt><code>Option &#34;MaxClock&#34; &#34;</code><i>frequency</i><code>&#34;</code></p>
<dd>This optional entry specifies the maximum dot clock, in kHz, that is supported by the monitor.</p>
<dt><code>Option &#34;Ignore&#34; &#34;</code><i>bool</i><code>&#34;</code></p>
<dd>This optional entry specifies that the monitor should be ignored entirely, and not reported through RandR. This is useful if the hardware reports the presence of outputs that don&#8217;t exist. (RandR 1.2-supporting drivers only)</p>
<dt><code>Option &#34;Rotate&#34; &#34;</code><i>rotation</i><code>&#34;</code></p>
<dd>This optional entry specifies the initial rotation of the given monitor. Valid values for rotation are &#34;normal&#34;, &#34;left&#34;, &#34;right&#34;, and &#34;inverted&#34;. (RandR 1.2-supporting drivers only) </p>
</dl>
<h2>Modes Section</h2>
<p>The config file may have multiple <code>Modes</code> sections, or none. These sections provide a way of defining sets of video modes independently of the <code>Monitor</code> sections. <code>Monitor</code> sections may include the definitions provided in these sections by using the <code>UseModes</code> keyword. In most cases the <code>Modes</code> sections are not necessary because the built-in set of VESA standard modes will be sufficient. </p>
<p> <code>Modes</code> sections have the following format: </p>
<dl>
<dd>
<pre><code>Section &#34;Modes&#34;</code>
<code> Identifier &#34;</code><i>name</i><code>&#34;</code>
<i> entries</i>
<i> ...</i>
<code>EndSection</code></pre>
</dl>
<p> The <code>Identifier</code> entry specifies the unique name for this set of mode descriptions. The other entries permitted in <code>Modes</code> sections are the <code>Mode</code> and <code>ModeLine</code> entries that are described above in the <code>Monitor</code> section.</p>
<h2>Screen Section</h2>
<p>The config file may have multiple <code>Screen</code> sections. There must be at least one, for the &#8220;screen&#8221; being used. A &#8220;screen&#8221; represents the binding of a graphics device (<code>Device</code> section) and a monitor (<code>Monitor</code> section). A <code>Screen</code> section is considered &#8220;active&#8221; if it is referenced by an active <code>ServerLayout</code> section or by the <code>-screen</code> command line option. If neither of those is present, the first <code>Screen</code> section found in the config file is considered the active one. </p>
<p> <code>Screen</code> sections have the following format: </p>
<dl>
<dd>
<pre><code>Section &#34;Screen&#34;</code>
<code> Identifier &#34;</code><i>name</i><code>&#34;</code>
<code> Device &#34;</code><i>devid</i><code>&#34;</code>
<code> GPUDevice &#34;</code><i>devid</i><code>&#34;</code>
<code> Monitor &#34;</code><i>monid</i><code>&#34;</code>
<i> entries</i>
<i> ...</i>
<code> SubSection &#34;Display&#34;</code>
<i> entries</i>
<i> ...</i>
<code> EndSubSection</code>
<i> ...</i>
<code>EndSection</code></pre>
</dl>
<p> The <code>Identifier</code> entry is mandatory. All others are optional. </p>
<p> The <code>Identifier</code> entry specifies the unique name for this screen. The <code>Screen</code> section provides information specific to the whole screen, including screen-specific <code>Options</code>. In multi-head configurations, there will be multiple active <code>Screen</code> sections, one for each head. The entries available for this section are:</p>
<dl>
<dt><code>Device &#34;</code><i>device-id</i><code>&#34;</code></p>
<dd>This entry specifies the <code>Device</code> section to be used for this screen. When multiple graphics cards are present, this is what ties a specific card to a screen. The <i>device-id</i> must match the <code>Identifier</code> of a <code>Device</code> section in the config file.</p>
<dt><code>GPUDevice &#34;</code><i>device-id</i><code>&#34;</code></p>
<dd>This entry specifies the <code>Device</code> section to be used as a secondary GPU device for this screen. When multiple graphics cards are present, this is what ties a specific secondary card to a screen. The <i>device-id</i> must match the <code>Identifier</code> of a <code>Device</code> section in the config file. This can be specified up to 4 times for a single screen.</p>
<dt><code>Monitor &#34;</code><i>monitor-id</i><code>&#34;</code></p>
<dd>specifies which monitor description is to be used for this screen. If a <code>Monitor</code> name is not specified, a default configuration is used. Currently the default configuration may not function as expected on all platforms.</p>
<dt><code>VideoAdaptor &#34;</code><i>xv-id</i><code>&#34;</code></p>
<dd>specifies an optional Xv video adaptor description to be used with this screen.</p>
<dt><code>DefaultDepth </code><i>depth</i></p>
<dd>specifies which color depth the server should use by default. The <code>-depth</code> command line option can be used to override this. If neither is specified, the default depth is driver-specific, but in most cases is 8.</p>
<dt><code>DefaultFbBpp </code><i>bpp</i></p>
<dd>specifies which framebuffer layout to use by default. The <code>-fbbpp</code> command line option can be used to override this. In most cases the driver will chose the best default value for this. The only case where there is even a choice in this value is for depth 24, where some hardware supports both a packed 24 bit framebuffer layout and a sparse 32 bit framebuffer layout.</p>
<dt><code>MatchSeat </code><i>seat-id</i></p>
<dd>Only apply this <code>Screen</code> section if X server was started with <code>-seat</code> <i>seat-id</i> option.</p>
<dt><code>Options</code></p>
<dd>Various <code>Option</code> flags may be specified in the <code>Screen</code> section. Some are driver-specific and are described in the driver documentation. Others are driver-independent, and will eventually be described here.</p>
<dt><code>Option &#34;Accel&#34;</code></p>
<dd>Enables 2D hardware acceleration. This option is on by default, but it may be necessary to turn it off if there are bugs in the driver. There are many options to disable specific accelerated operations, listed below. Note that disabling an operation will have no effect if the operation is not accelerated (whether due to lack of support in the hardware or in the driver).</p>
<dt><code>Option &#34;GlxVendorLibrary&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>This option specifies a space-separated list of OpenGL vendor libraries to use for the screen. This may be used to select an alternate implementation for development, debugging, or alternate feature sets. Default: mesa.</p>
<dt><code>Option &#34;InitPrimary&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Use the Int10 module to initialize the primary graphics card. Normally, only secondary cards are soft-booted using the Int10 module, as the primary card has already been initialized by the BIOS at boot time. Default: false.</p>
<dt><code>Option &#34;NoInt10&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Disables the Int10 module, a module that uses the int10 call to the BIOS of the graphics card to initialize it. Default: false.</dl>
<p> Each <code>Screen</code> section may optionally contain one or more <code>Display</code> subsections. Those subsections provide depth/fbbpp specific configuration information, and the one chosen depends on the depth and/or fbbpp that is being used for the screen. The <code>Display</code> subsection format is described in the section below.</p>
<h2>Display Subsection</h2>
<p>Each <code>Screen</code> section may have multiple <code>Display</code> subsections. The &#8220;active&#8221; <code>Display</code> subsection is the first that matches the depth and/or fbbpp values being used, or failing that, the first that has neither a depth or fbbpp value specified. The <code>Display</code> subsections are optional. When there isn&#8217;t one that matches the depth and/or fbbpp values being used, all the parameters that can be specified here fall back to their defaults. </p>
<p> <code>Display</code> subsections have the following format: </p>
<dl>
<dd>
<pre><code> SubSection &#34;Display&#34;</code>
<code> Depth </code><i>depth</i>
<i> entries</i>
<i> ...</i>
<code> EndSubSection</code></pre>
</dl>
<dl>
<dt><code>Depth </code><i>depth</i></p>
<dd>This entry specifies what colour depth the <code>Display</code> subsection is to be used for. This entry is usually specified, but it may be omitted to create a match-all <code>Display</code> subsection or when wishing to match only against the <code>FbBpp</code> parameter. The range of <i>depth</i> values that are allowed depends on the driver. Most drivers support 8, 15, 16 and 24. Some also support 1 and/or 4, and some may support other values (like 30). Note: <i>depth</i> means the number of bits in a pixel that are actually used to determine the pixel colour. 32 is not a valid <i>depth</i> value. Most hardware that uses 32 bits per pixel only uses 24 of them to hold the colour information, which means that the colour depth is 24, not 32.</p>
<dt><code>FbBpp </code><i>bpp</i></p>
<dd>This entry specifies the framebuffer format this <code>Display</code> subsection is to be used for. This entry is only needed when providing depth 24 configurations that allow a choice between a 24 bpp packed framebuffer format and a 32bpp sparse framebuffer format. In most cases this entry should not be used.</p>
<dt><code>Weight </code><i>red-weight green-weight blue-weight</i></p>
<dd>This optional entry specifies the relative RGB weighting to be used for a screen is being used at depth 16 for drivers that allow multiple formats. This may also be specified from the command line with the <code>-weight</code> option (see <code><a href="/docs/linux/man/1-xorg/">Xorg</a>(1)).</code></p>
<dt><code>Virtual </code><i>xdim ydim</i></p>
<dd>This optional entry specifies the virtual screen resolution to be used. <i>xdim</i> must be a multiple of either 8 or 16 for most drivers, and a multiple of 32 when running in monochrome mode. The given value will be rounded down if this is not the case. Video modes which are too large for the specified virtual size will be rejected. If this entry is not present, the virtual screen resolution will be set to accommodate all the valid video modes given in the <code>Modes</code> entry. Some drivers/hardware combinations do not support virtual screens. Refer to the appropriate driver-specific documentation for details.</p>
<dt><code>ViewPort </code><i>x0 y0</i></p>
<dd>This optional entry sets the upper left corner of the initial display. This is only relevant when the virtual screen resolution is different from the resolution of the initial video mode. If this entry is not given, then the initial display will be centered in the virtual display area.</p>
<dt><code>Modes &#34;</code><i>mode-name</i><code>&#34;</code><i> &#8230;</i></p>
<dd>This optional entry specifies the list of video modes to use. Each <i>mode-name</i> specified must be in double quotes. They must correspond to those specified or referenced in the appropriate <code>Monitor</code> section (including implicitly referenced built-in VESA standard modes). The server will delete modes from this list which don&#8217;t satisfy various requirements. The first valid mode in this list will be the default display mode for startup. The list of valid modes is converted internally into a circular list. It is possible to switch to the next mode with <code>Ctrl+Alt+Keypad-Plus</code> and to the previous mode with <code>Ctrl+Alt+Keypad-Minus</code>. When this entry is omitted, the valid modes referenced by the appropriate <code>Monitor</code> section will be used. If the <code>Monitor</code> section contains no modes, then the selection will be taken from the built-in VESA standard modes.</p>
<dt><code>Visual &#34;</code><i>visual-name</i><code>&#34;</code></p>
<dd>This optional entry sets the default root visual type. This may also be specified from the command line (see the <code><a href="/docs/linux/man/1-xserver/">Xserver</a>(1)</code> man page). The visual types available for depth 8 are (default is <code>PseudoColor</code>):</dl>
<dl>
<dd>
<pre><code>StaticGray</code>
<code>GrayScale</code>
<code>StaticColor</code>
<code>PseudoColor</code>
<code>TrueColor</code>
<code>DirectColor</code></pre>
</dl>
<dl>
<dd>The visual type available for the depths 15, 16 and 24 are (default is <code>TrueColor</code>): </p>
<dl>
<dd>
<pre><code>TrueColor</code>
<code>DirectColor</code></pre>
</dl>
<p> Not all drivers support <code>DirectColor</code> at these depths. </p>
<p> The visual types available for the depth 4 are (default is <code>StaticColor</code>): </p>
<dl>
<dd>
<pre><code>StaticGray</code>
<code>GrayScale</code>
<code>StaticColor</code>
<code>PseudoColor</code></pre>
</dl>
<p> The visual type available for the depth 1 (monochrome) is <code>StaticGray</code>.</dl>
<dl>
<dt><code>Black </code><i>red green blue</i></p>
<dd>This optional entry allows the &#8220;black&#8221; colour to be specified. This is only supported at depth 1. The default is black.</p>
<dt><code>White </code><i>red green blue</i></p>
<dd>This optional entry allows the &#8220;white&#8221; colour to be specified. This is only supported at depth 1. The default is white.</p>
<dt><code>Options</code></p>
<dd>Option flags may be specified in the <code>Display</code> subsections. These may include driver-specific options and driver-independent options. The former are described in the driver-specific documentation. Some of the latter are described above in the section about the <code>Screen</code> section, and they may also be included here.</dl>
<h2>Serverlayout Section</h2>
<p>The config file may have multiple <code>ServerLayout</code> sections. A &#8220;server layout&#8221; represents the binding of one or more screens (<code>Screen</code> sections) and one or more input devices (<code>InputDevice</code> sections) to form a complete configuration. In multi-head configurations, it also specifies the relative layout of the heads. A <code>ServerLayout</code> section is considered &#8220;active&#8221; if it is referenced by the <code>-layout</code> command line option or by an <code>Option &#34;DefaultServerLayout&#34;</code> entry in the <code>ServerFlags</code> section (the former takes precedence over the latter). If those options are not used, the first <code>ServerLayout</code> section found in the config file is considered the active one. If no <code>ServerLayout</code> sections are present, the single active screen and two active (core) input devices are selected as described in the relevant sections above. </p>
<p> <code>ServerLayout</code> sections have the following format: </p>
<dl>
<dd>
<pre><code>Section &#34;ServerLayout&#34;</code>
<code> Identifier &#34;</code><i>name</i><code>&#34;</code>
<code> Screen &#34;</code><i>screen-id</i><code>&#34;</code>
<i> ...</i>
<code> InputDevice &#34;</code><i>idev-id</i><code>&#34;</code>
<i> ...</i>
<i> options</i>
<i> ...</i>
<code>EndSection</code></pre>
</dl>
<p> Each <code>ServerLayout</code> section must have an <code>Identifier</code> entry and at least one <code>Screen</code> entry. </p>
<p> The <code>Identifier</code> entry specifies the unique name for this server layout. The <code>ServerLayout</code> section provides information specific to the whole session, including session-specific <code>Options</code>. The <code>ServerFlags</code> options (described above) may be specified here, and ones given here override those given in the <code>ServerFlags</code> section. </p>
<p> The entries that may be used in this section are described here.</p>
<dl>
<dt><code>Screen </code><i>screen-num</i><code> &#34;screen-id&#34; </code><i>position-information</i></p>
<dd>One of these entries must be given for each screen being used in a session. The <i>screen-id</i> field is mandatory, and specifies the <code>Screen</code> section being referenced. The <i>screen-num</i> field is optional, and may be used to specify the screen number in multi-head configurations. When this field is omitted, the screens will be numbered in the order that they are listed in. The numbering starts from 0, and must be consecutive. The <i>position-information</i> field describes the way multiple screens are positioned. There are a number of different ways that this information can be provided:</p>
<dl>
<dd>
<dl>
<dt><i>x y</i></p>
<dd>
<dt><code>Absolute </code><i>x y</i></p>
<dd>These both specify that the upper left corner&#8217;s coordinates are (<i>x</i>,<i>y</i>). The <code>Absolute</code> keyword is optional. Some older versions of XFree86 (4.2 and earlier) don&#8217;t recognise the <code>Absolute</code> keyword, so it&#8217;s safest to just specify the coordinates without it.</p>
<dt><code>RightOf &#34;</code><i>screen-id</i><code>&#34;</code></p>
<dd>
<dt><code>LeftOf &#34;</code><i>screen-id</i><code>&#34;</code></p>
<dd>
<dt><code>Above &#34;</code><i>screen-id</i><code>&#34;</code></p>
<dd>
<dt><code>Below &#34;</code><i>screen-id</i><code>&#34;</code></p>
<dd>
<dt><code>Relative &#34;</code><i>screen-id</i><code>&#34;</code><i> x y</i></p>
<dd>These give the screen&#8217;s location relative to another screen. The first four position the screen immediately to the right, left, above or below the other screen. When positioning to the right or left, the top edges are aligned. When positioning above or below, the left edges are aligned. The <code>Relative</code> form specifies the offset of the screen&#8217;s origin (upper left corner) relative to the origin of another screen.</dl>
</dl>
<dt><code>InputDevice &#34;</code><i>idev-id</i><code>&#34; &#34;</code><i>option</i><code>&#34;</code><i> &#8230;</i></p>
<dd>One of these entries should be given for each input device being used in a session. Normally at least two are required, one each for the core pointer and keyboard devices. If either of those is missing, suitable <code>InputDevice</code> entries are searched for using the method described above in the <code>INPUTDEVICE</code> section. The <i>idev-id</i> field is mandatory, and specifies the name of the <code>InputDevice</code> section being referenced. Multiple <i>option</i> fields may be specified, each in double quotes. The options permitted here are any that may also be given in the <code>InputDevice</code> sections. Normally only session-specific input device options would be used here. The most commonly used options are:</dl>
<dl>
<dd>
<pre><code>&#34;CorePointer&#34;</code>
<code>&#34;CoreKeyboard&#34;</code>
<code>&#34;SendCoreEvents&#34;</code></pre>
</dl>
<dl>
<dd>and the first two should normally be used to indicate the core pointer and core keyboard devices respectively.</dl>
<dl>
<dt><code>MatchSeat </code><i>seat-id</i></p>
<dd>Only apply this <code>ServerLayout</code> section if X server was started with <code>-seat</code> <i>seat-id</i> option.</p>
<dt><code>Options</code></p>
<dd>In addition to the following, any option permitted in the <code>ServerFlags</code> section may also be specified here. When the same option appears in both places, the value given here overrides the one given in the <code>ServerFlags</code> section.</p>
<dt><code>Option &#34;IsolateDevice&#34; &#34;</code><i>bus-id</i><code>&#34;</code></p>
<dd>Restrict device resets to the specified <i>bus-id</i>. See the <code>BusID</code> option (described in <code>DEVICE SECTION</code>, above) for the format of the <i>bus-id</i> parameter. This option overrides <code>SingleCard</code>, if specified. At present, only PCI devices can be isolated in this manner.</p>
<dt><code>Option &#34;SingleCard&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>As <code>IsolateDevice</code>, except that the bus ID of the first device in the layout is used.</dl>
<p> Here is an example of a <code>ServerLayout</code> section for a dual headed configuration with two mice: </p>
<dl>
<dd>
<pre><code>Section &#34;ServerLayout&#34;</code>
<code> Identifier &#34;Layout 1&#34;</code>
<code> Screen &#34;MGA 1&#34;</code>
<code> Screen &#34;MGA 2&#34; RightOf &#34;MGA 1&#34;</code>
<code> InputDevice &#34;Keyboard 1&#34; &#34;CoreKeyboard&#34;</code>
<code> InputDevice &#34;Mouse 1&#34; &#34;CorePointer&#34;</code>
<code> InputDevice &#34;Mouse 2&#34; &#34;SendCoreEvents&#34;</code>
<code> Option &#34;BlankTime&#34; &#34;5&#34;</code>
<code>EndSection</code></pre>
</dl>
<h2>Dri Section</h2>
<p>This optional section is used to provide some information for the Direct Rendering Infrastructure. Details about the format of this section can be found on-line at <i>&lt;<a rel="nofollow" href="https://dri.freedesktop.org/">https://dri.freedesktop.org/</a>&gt;</i>.</p>
<h2>Vendor Section</h2>
<p>The optional <code>Vendor</code> section may be used to provide vendor-specific configuration information. Multiple <code>Vendor</code> sections may be present, and they may contain an <code>Identifier</code> entry and multiple <code>Option</code> flags. The data therein is not used in this release.</p>
<h2>See Also</h2>
<p>General: <code><a href="/docs/linux/man/7-x/">X</a></code>(7), <code><a href="/docs/linux/man/1-xserver/">Xserver</a></code>(1), <code><a href="/docs/linux/man/1-xorg/">Xorg</a></code>(1), <code><a href="/docs/linux/man/1-cvt/">cvt</a></code>(1), <code><a href="/docs/linux/man/1-gtf/">gtf</a></code>(1). </p>
<p> <code>Not all modules or interfaces are available on all platforms.</code> </p>
<p> Display drivers: <code><a href="/docs/linux/man/4-apm/">apm</a></code>(4), <code><a href="/docs/linux/man/4-ati/">ati</a></code>(4), <code><a href="/docs/linux/man/4-chips/">chips</a></code>(4), <code><a href="/docs/linux/man/4-cirrus/">cirrus</a></code>(4), <code><a href="/docs/linux/man/4-cyrix/">cyrix</a></code>(4), <code><a href="/docs/linux/man/4-fbdev/">fbdev</a></code>(4), <code><a href="/docs/linux/man/4-glide/">glide</a></code>(4), <code><a href="/docs/linux/man/4-glint/">glint</a></code>(4), <code><a href="/docs/linux/man/4-i128/">i128</a></code>(4), <code><a href="/docs/linux/man/4-i740/">i740</a></code>(4), <code><a href="/docs/linux/man/4-imstt/">imstt</a></code>(4), <code><a href="/docs/linux/man/4-intel/">intel</a></code>(4), <code><a href="/docs/linux/man/4-mga/">mga</a></code>(4), <code><a href="/docs/linux/man/4-neomagic/">neomagic</a></code>(4), <code><a href="/docs/linux/man/4-nv/">nv</a></code>(4), <code><a href="/docs/linux/man/4-openchrome/">openchrome</a></code>(4), <code><a href="/docs/linux/man/4-r128/">r128</a></code>(4), <code><a href="/docs/linux/man/4-radeon/">radeon</a></code>(4), <code><a href="/docs/linux/man/4-rendition/">rendition</a></code>(4), <code><a href="/docs/linux/man/4-savage/">savage</a></code>(4), <code><a href="/docs/linux/man/4-s3virge/">s3virge</a></code>(4), <code><a href="/docs/linux/man/4-siliconmotion/">siliconmotion</a></code>(4), <code><a href="/docs/linux/man/4-sis/">sis</a></code>(4), <code><a href="/docs/linux/man/4-sisusb/">sisusb</a></code>(4), <code><a href="/docs/linux/man/4-sunbw2/">sunbw2</a></code>(4), <code><a href="/docs/linux/man/4-suncg14/">suncg14</a></code>(4), <code><a href="/docs/linux/man/4-suncg3/">suncg3</a></code>(4), <code><a href="/docs/linux/man/4-suncg6/">suncg6</a></code>(4), <code><a href="/docs/linux/man/4-sunffb/">sunffb</a></code>(4), <code><a href="/docs/linux/man/4-sunleo/">sunleo</a></code>(4), <code><a href="/docs/linux/man/4-suntcx/">suntcx</a></code>(4), <code><a href="/docs/linux/man/4-tdfx/">tdfx</a></code>(4), <code><a href="/docs/linux/man/4-trident/">trident</a></code>(4), <code><a href="/docs/linux/man/4-tseng/">tseng</a></code>(4), <code><a href="/docs/linux/man/4-vesa/">vesa</a></code>(4), <code><a href="/docs/linux/man/4-vmware/">vmware</a></code>(4), <code><a href="/docs/linux/man/4-voodoo/">voodoo</a></code>(4), <code><a href="/docs/linux/man/4-wsfb/">wsfb</a></code>(4), <code><a href="/docs/linux/man/4-xgi/">xgi</a></code>(4), <code><a href="/docs/linux/man/4-xgixp/">xgixp</a></code>(4). </p>
<p> Input drivers: <code><a href="/docs/linux/man/4-acecad/">acecad</a></code>(4), <code><a href="/docs/linux/man/4-citron/">citron</a></code>(4), <code><a href="/docs/linux/man/4-elographics/">elographics</a></code>(4), <code><a href="/docs/linux/man/4-evdev/">evdev</a></code>(4), <code><a href="/docs/linux/man/4-fpit/">fpit</a></code>(4), <code><a href="/docs/linux/man/4-joystick/">joystick</a></code>(4), <code><a href="/docs/linux/man/4-kbd/">kbd</a></code>(4), <code><a href="/docs/linux/man/4-libinput/">libinput</a></code>(4), <code><a href="/docs/linux/man/4-mousedrv/">mousedrv</a></code>(4), <code><a href="/docs/linux/man/4-mutouch/">mutouch</a></code>(4), <code><a href="/docs/linux/man/4-penmount/">penmount</a></code>(4), <code><a href="/docs/linux/man/4-synaptics/">synaptics</a></code>(4), <code><a href="/docs/linux/man/4-vmmouse/">vmmouse</a></code>(4), <code><a href="/docs/linux/man/4-void/">void</a></code>(4), <code><a href="/docs/linux/man/4-wacom/">wacom</a></code>(4). </p>
<p> Other modules and interfaces: <code><a href="/docs/linux/man/4-exa/">exa</a></code>(4), <code><a href="/docs/linux/man/4-fbdevhw/">fbdevhw</a></code>(4), <code><a href="/docs/linux/man/4-v4l/">v4l</a></code>(4).</p>
<h2>Authors</h2>
<p>This manual page was largely rewritten by David Dawes <i>&lt;dawes [at] xfree86.org&gt;</i>.</p>
