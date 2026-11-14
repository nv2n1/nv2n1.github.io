---
title: "blender(1)"
name: "blender"
section: "1"
letter: "b"
url: "/docs/linux/man/1-blender/"
description: "blender – a 3D modelling and rendering package"
---

<h2 class="name">NAME</h2>
<p> blender &#8211; a 3D modelling and rendering package </p>
<h2>SYNOPSIS</h2>
<p> <code>blender [args &#8230;] [file] [args &#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>blender</code> is a 3D modelling and rendering package. It is the in-house software of a high quality animation studio, Blender has proven to be an extremely fast and versatile design instrument. The software has a personal touch, offering a unique approach to the world of Three Dimensions. </p>
<p> Use Blender to create TV commercials, to make technical visualizations, business graphics, to do some morphing, or design user interfaces. You can easy build and manage complex environments. The renderer is versatile and extremely fast. All basic animation principles (curves &amp; keys) are well implemented. </p>
<p> <a rel="nofollow" href="http://www.blender.org">http://www.blender.org</a></p>
<h2>OPTIONS</h2>
<p> Blender 2.66 Usage: blender [args &#8230;] [file] [args &#8230;] </p>
<h3>Render Options:</h3>
<dl>
<dt><code>-b or &#8211;background &lt;file&gt;</code></p>
<dd>
 Load &lt;file&gt; in background (often used for UI-less rendering) </p>
<dt><code>-a or &#8211;render-anim</code></p>
<dd>
 Render frames from start to end (inclusive) </p>
<dt><code>-S or &#8211;scene &lt;name&gt;</code></p>
<dd>
 Set the active scene &lt;name&gt; for rendering </p>
<dt><code>-f or &#8211;render-frame &lt;frame&gt;</code></p>
<dd>
 Render frame &lt;frame&gt; and save it.<br />
 +&lt;frame&gt; start frame relative, -&lt;frame&gt; end frame relative. </p>
<dt><code>-s or &#8211;frame-start &lt;frame&gt;</code></p>
<dd>
 Set start to frame &lt;frame&gt; (use before the -a argument) </p>
<dt><code>-e or &#8211;frame-end &lt;frame&gt;</code></p>
<dd>
 Set end to frame &lt;frame&gt; (use before the -a argument) </p>
<dt><code>-j or &#8211;frame-jump &lt;frames&gt;</code></p>
<dd>
 Set number of frames to step forward after each rendered frame </p>
<dt><code>-o or &#8211;render-output &lt;path&gt;</code></p>
<dd>
 Set the render path and file name.<br />
 Use // at the start of the path to </p>
<p>&nbsp;<wbr>render relative to the blend file.<br />
 The # characters are replaced by the frame number, and used to define zero padding. </p>
<p>&nbsp;<wbr>ani_##_test.png becomes ani_01_test.png </p>
<p>&nbsp;<wbr>test-######.png becomes test-000001.png </p>
<p>&nbsp;<wbr>When the filename does not contain&nbsp;<wbr>#, The suffix&nbsp;<wbr>####&nbsp;<wbr>is added to the filename<br />
 The frame number will be added at the end of the filename. </p>
<p>&nbsp;<wbr>eg: blender -b foobar.blend -o&nbsp;<wbr>//render_&nbsp;<wbr>-F PNG -x 1 -a </p>
<p>&nbsp;<wbr>//render_&nbsp;<wbr>becomes&nbsp;<wbr>//render_####, writing frames as&nbsp;<wbr>//render_0001.png// </p>
<dt><code>-E or &#8211;engine &lt;engine&gt;</code></p>
<dd>
 Specify the render engine<br />
 use -E help to list available engines </p>
<dt>
<dd>
</dl>
<h3>Format Options:</h3>
<dl>
<dt><code>-F or &#8211;render-format &lt;format&gt;</code></p>
<dd>
 Set the render format, Valid options are&#8230; </p>
<p>&nbsp;<wbr>TGA IRIS JPEG MOVIE IRIZ RAWTGA </p>
<p>&nbsp;<wbr>AVIRAW AVIJPEG PNG BMP FRAMESERVER<br />
 (formats that can be compiled into blender, not available on all systems) </p>
<p>&nbsp;<wbr>HDR TIFF EXR MULTILAYER MPEG AVICODEC QUICKTIME CINEON DPX DDS </p>
<dt><code>-x or &#8211;use-extension &lt;bool&gt;</code></p>
<dd>
 Set option to add the file extension to the end of the file </p>
<dt><code>-t or &#8211;threads &lt;threads&gt;</code></p>
<dd>
 Use amount of &lt;threads&gt; for rendering in background<br />
 [1-64], 0 for systems processor count. </p>
<dt>
<dd>
</dl>
<h3>Animation Playback Options:</h3>
<dl>
<dt><code>-a &lt;options&gt; &lt;file(s)&gt;</code></p>
<dd>
 Playback &lt;file(s)&gt;, only operates this way when not running in background. </p>
<p>&nbsp;<wbr>-p&nbsp;<wbr>&lt;sx&gt;&nbsp;<wbr>&lt;sy&gt;&nbsp;<wbr>Open with lower left corner at&nbsp;<wbr>&lt;sx&gt;,&nbsp;<wbr>&lt;sy&gt; </p>
<p>&nbsp;<wbr>-m Read from disk&nbsp;<wbr>(Don&#8217;t buffer) </p>
<p>&nbsp;<wbr>-f&nbsp;<wbr>&lt;fps&gt;&nbsp;<wbr>&lt;fps-base&gt;&nbsp;<wbr>Specify FPS to start with </p>
<p>&nbsp;<wbr>-j&nbsp;<wbr>&lt;frame&gt;&nbsp;<wbr>Set frame step to&nbsp;<wbr>&lt;frame&gt; </p>
<p>&nbsp;<wbr>-s&nbsp;<wbr>&lt;frame&gt;&nbsp;<wbr>Play from&nbsp;<wbr>&lt;frame&gt; </p>
<p>&nbsp;<wbr>-e&nbsp;<wbr>&lt;frame&gt;&nbsp;<wbr>Play until&nbsp;<wbr>&lt;frame&gt; </p>
<dt>
<dd>
</dl>
<h3>Window Options:</h3>
<dl>
<dt><code>-w or &#8211;window-border</code></p>
<dd>
 Force opening with borders (default) </p>
<dt><code>-W or &#8211;window-borderless</code></p>
<dd>
 Force opening without borders </p>
<dt><code>-p or &#8211;window-geometry &lt;sx&gt; &lt;sy&gt; &lt;w&gt; &lt;h&gt;</code></p>
<dd>
 Open with lower left corner at &lt;sx&gt;, &lt;sy&gt; and width and height as &lt;w&gt;, &lt;h&gt; </p>
<dt><code>-con or &#8211;start-console</code></p>
<dd>
 Start with the console window open (ignored if -b is set) </p>
<dt>
<dd>
</dl>
<h3>Game Engine Specific Options:</h3>
<dl>
<dt><code>-g Game Engine specific options</code></p>
<dd>
 -g fixedtime Run on 50 hertz without dropping frames<br />
 -g vertexarrays Use Vertex Arrays for rendering (usually faster)<br />
 -g nomipmap No Texture Mipmapping<br />
 -g linearmipmap Linear Texture Mipmapping instead of Nearest (default) </p>
<dt>
<dd>
</dl>
<h3>Misc Options:</h3>
<dl>
<dt><code>-d or &#8211;debug</code></p>
<dd>
 Turn debugging on </p>
<dt>
<dd> * Prints every operator call and their arguments<br />
 * Disables mouse grab (to interact with a debugger in some cases)<br />
 * Keeps python sys.stdin rather than setting it to None </p>
<dt><code>&#8211;debug-fpe</code></p>
<dd>
 Enable floating point exceptions </p>
<dt><code>&#8211;disable-crash-handler</code></p>
<dd>
 Disable the crash handler </p>
<dt>
<dd>
<dt><code>&#8211;factory-startup</code></p>
<dd>
 Skip reading the &quot;startup.blend&quot; in the users home directory </p>
<dt>
<dd>
<dt><code>&#8211;env-system-datafiles</code></p>
<dd>
 Set the BLENDER_SYSTEM_DATAFILES environment variable </p>
<dt><code>&#8211;env-system-scripts</code></p>
<dd>
 Set the BLENDER_SYSTEM_SCRIPTS environment variable </p>
<dt><code>&#8211;env-system-python</code></p>
<dd>
 Set the BLENDER_SYSTEM_PYTHON environment variable </p>
<dt>
<dd>
<dt><code>-nojoystick</code></p>
<dd>
 Disable joystick support </p>
<dt><code>-noglsl</code></p>
<dd>
 Disable GLSL shading </p>
<dt><code>-noaudio</code></p>
<dd>
 Force sound system to None </p>
<dt><code>-setaudio</code></p>
<dd>
 Force sound system to a specific device<br />
 NULL SDL OPENAL JACK </p>
<dt>
<dd>
<dt><code>-h or &#8211;help</code></p>
<dd>
 Print this help text and exit </p>
<dt>
<dd>
<dt><code>-y or &#8211;enable-autoexec</code></p>
<dd>
 Enable automatic python script execution, (default) </p>
<dt><code>-Y or &#8211;disable-autoexec</code></p>
<dd>
 Disable automatic python script execution (pydrivers &amp; startup scripts) </p>
<dt>
<dd>
<dt><code>-P or &#8211;python &lt;filename&gt;</code></p>
<dd>
 Run the given Python script file </p>
<dt><code>&#8211;python-text &lt;name&gt;</code></p>
<dd>
 Run the given Python script text block </p>
<dt><code>&#8211;python-console</code></p>
<dd>
 Run blender with an interactive console </p>
<dt><code>&#8211;addons</code></p>
<dd>
 Comma separated list of addons (no spaces) </p>
<dt><code>-v or &#8211;version</code></p>
<dd>
 Print Blender version and exit </p>
<dt><code>&#8212;</code></p>
<dd>
 Ends option processing, following arguments passed unchanged. Access via python&#8217;s sys.argv </p>
</dl>
<h3>Other Options:</h3>
<dl>
<dt><code>/?</code></p>
<dd>
 Print this help text and exit (windows only) </p>
<dt><code>&#8211;debug-python</code></p>
<dd>
 Enable debug messages for python </p>
<dt><code>&#8211;debug-events</code></p>
<dd>
 Enable debug messages for the event system </p>
<dt><code>&#8211;debug-handlers</code></p>
<dd>
 Enable debug messages for event handling </p>
<dt><code>&#8211;debug-wm</code></p>
<dd>
 Enable debug messages for the window manager </p>
<dt><code>&#8211;debug-all</code></p>
<dd>
 Enable all debug messages (excludes libmv) </p>
<dt><code>&#8211;debug-value &lt;value&gt;</code></p>
<dd>
 Set debug value of &lt;value&gt; on startup </p>
<dt>
<dd>
<dt><code>&#8211;debug-jobs</code></p>
<dd>
 Enable time profiling for background jobs. </p>
<dt><code>&#8211;verbose &lt;verbose&gt;</code></p>
<dd>
 Set logging verbosity level. </p>
<dt><code>-R</code></p>
<dd>
 Register .blend extension, then exit (Windows only) </p>
<dt><code>-r</code></p>
<dd>
 Silently register .blend extension, then exit (Windows only) </p>
<dt><code>&#8211;no-native-pixels</code></p>
<dd>
 Do not use native pixel size, for high resolution displays (MacBook &#8216;Retina&#8217;) </p>
</dl>
<h3>Argument Parsing:</h3>
<p>&nbsp;<wbr>arguments must be separated by white space. eg<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;blender -ba test.blend&quot;<br />
&nbsp;<wbr>&#8230;will ignore the&nbsp;<wbr>&#8216;a&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;blender -b test.blend -f8&quot;<br />
&nbsp;<wbr>&#8230;will ignore 8 because there is no space between the -f and the frame value </p>
<h3>Argument Order:</h3>
<p> Arguments are executed in the order they are given. eg<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;blender &#8211;background test.blend &#8211;render-frame 1 &#8211;render-output&nbsp;<wbr>/tmp&quot;<br />
&nbsp;<wbr>&#8230;will not render to&nbsp;<wbr>/tmp because&nbsp;<wbr>&#8216;&#8211;render-frame 1&#8217;&nbsp;<wbr>renders before the output path is set<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;blender &#8211;background &#8211;render-output&nbsp;<wbr>/tmp test.blend &#8211;render-frame 1&quot;<br />
&nbsp;<wbr>&#8230;will not render to&nbsp;<wbr>/tmp because loading the blend file overwrites the render output that was set<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;blender &#8211;background test.blend &#8211;render-output&nbsp;<wbr>/tmp &#8211;render-frame 1&quot;&nbsp;<wbr>works as expected. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<p>&nbsp;<wbr>&nbsp;<wbr><i>BLENDER_USER_CONFIG</i>&nbsp;<wbr>Directory for user configuration files.<br />
&nbsp;<wbr>&nbsp;<wbr><i>BLENDER_USER_SCRIPTS</i>&nbsp;<wbr>Directory for user scripts.<br />
&nbsp;<wbr>&nbsp;<wbr><i>BLENDER_SYSTEM_SCRIPTS</i>&nbsp;<wbr>Directory for system wide scripts.<br />
&nbsp;<wbr>&nbsp;<wbr><i>Directory</i>&nbsp;<wbr>for user data files&nbsp;<wbr>(icons, translations, ..).<br />
&nbsp;<wbr>&nbsp;<wbr><i>BLENDER_SYSTEM_DATAFILES</i>&nbsp;<wbr>Directory for system wide data files.<br />
&nbsp;<wbr>&nbsp;<wbr><i>BLENDER_SYSTEM_PYTHON</i>&nbsp;<wbr>Directory for system python libraries.<br />
&nbsp;<wbr>&nbsp;<wbr><i>TMP</i>&nbsp;<wbr>or&nbsp;<wbr><i>TMPDIR</i>&nbsp;<wbr>Store temporary files here.<br />
&nbsp;<wbr>&nbsp;<wbr><i>PYTHONHOME</i>&nbsp;<wbr>Path to the python directory, eg.&nbsp;<wbr>/usr/lib/python. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-yafaray/">yafaray</a>(1)</code> </p>
<h2>AUTHORS</h2>
<p> This manpage was written for a Debian GNU/Linux system by Daniel Mester &lt;mester [at] uni-bremen.de&gt; and updated by Cyril Brulebois &lt;cyril.brulebois [at] enst-bretagne.fr&gt; and Dan Eicher &lt;dan [at] trollwerks.org&gt;. </p>
<h2>Index</h2>
