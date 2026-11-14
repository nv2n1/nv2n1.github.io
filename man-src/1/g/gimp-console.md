---
title: "gimp-console(1)"
name: "gimp-console"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gimp-console/"
description: "gimp – an image manipulation and paint program."
---

<h2 class="name">NAME</h2>
<p> gimp &#8211; an image manipulation and paint program. </p>
<h2>SYNOPSIS</h2>
<p> <code>gimp</code> [-h] [&#8211;help] [&#8211;help-all] [&#8211;help-gtk] [-v] [&#8211;version] [&#8211;license] [&#8211;verbose] [-n] [&#8211;new-instance] [-a] [&#8211;as-new] [-i] [&#8211;no-interface] [-d] [&#8211;no-data] [-f] [&#8211;no-fonts] [-s] [&#8211;no-splash] [&#8211;no-shm] [&#8211;no-cpu-accel] [&#8211;display <i>display</i>] [&#8211;session <i>&lt;name&gt;</i>] [-g] [&#8211;gimprc <i>&lt;gimprc&gt;</i>] [&#8211;system-gimprc <i>&lt;gimprc&gt;</i>] [&#8211;dump-gimprc] [&#8211;console-messages] [&#8211;debug-handlers] [&#8211;stack-trace-mode <i>&lt;mode&gt;</i>] [&#8211;pdb-compat-mode <i>&lt;mode&gt;</i>] [&#8211;batch-interpreter <i>&lt;procedure&gt;</i>] [-b] [&#8211;batch <i>&lt;command&gt;</i>] [<i>filename</i>] &#8230; </p>
<h2>DESCRIPTION</h2>
<p> GIMP is the <i>GNU Image Manipulation Program</i>. It is used to edit and manipulate images. It can load and save a variety of image formats and can be used to convert between formats. </p>
<p> GIMP can also be used as a paint program. It features a set of drawing and painting tools such as airbrush, clone, pencil, and paint brush. Painting and drawing tools can be applied to an image with a variety of paint modes. It also offers an extensive array of selection tools like rectangle, ellipse, fuzzy select, bezier select, intelligent scissors, and select by color. </p>
<p> GIMP offers a variety of plug-ins that perform a variety of image manipulations. Examples include bumpmap, edge detect, gaussian blur, and many others. In addition, GIMP has several scripting extension which allow for advanced non-interactive processing and creation of images. </p>
<p> GIMP ships with a second binary called <i>gimp-console</i>. This binary is a console-only version and behaves as if <i>gimp</i> was called with the &#8211;no-interface command-line option. </p>
<p> On platforms with the D-Bus message bus system, GIMP will by default check if an instance is already running in this user session. If it detects that, it will pass all filenames given on the command-line to the already running GIMP instance and quit. </p>
<h2>OPTIONS</h2>
<p> GIMP accepts the following options:</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show GIMP command-line options.</p>
<dt><code>&#8211;help-all</code></p>
<dd> Show all command-line options.</p>
<dt><code>&#8211;help-gtk</code></p>
<dd> Show GTK+ command-line options.</p>
<dt><code>&#8211;help-gegl</code></p>
<dd> Show GEGL command-line options.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Output version information and exit. When combined with the &#8211;verbose option, version information about libraries used by GIMP is shown as well.</p>
<dt><code>&#8211;license</code></p>
<dd> Output license information and exit.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Be verbose and create information on standard output.</p>
<dt><code>-n, &#8211;new-instance</code></p>
<dd> Do not attempt to reuse an already running GIMP instance. Always start a new one.</p>
<dt><code>-a, &#8211;as-new</code></p>
<dd> Open filenames passed on the command-line as new images, don&#8217;t set the filename on them.</p>
<dt><code>-i, &#8211;no-interface</code></p>
<dd> Run without a user interface.</p>
<dt><code>-d, &#8211;no-data</code></p>
<dd> Do not load patterns, gradients, palettes, or brushes. Often useful in non-interactive situations where startup time is to be minimized.</p>
<dt><code>-f, &#8211;no-fonts</code></p>
<dd> Do not load any fonts. No text functionality will be available if this option is used.</p>
<dt><code>&#8211;display </code><i>display</i></p>
<dd> Use the designated X display.</p>
<dt><code>-s, &#8211;no-splash</code></p>
<dd> Do not show the splash screen.</p>
<dt><code>&#8211;no-shm</code></p>
<dd> Do not use shared memory between GIMP and its plug-ins. Instead of using shared memory, GIMP will send the data via pipe. This will result in slower performance than using shared memory.</p>
<dt><code>&#8211;no-cpu-accel</code></p>
<dd> Do not use CPU accelerations such as MMX or SSE even if GIMP detects that your CPU provides this functionality.</p>
<dt><code>&#8211;session </code><i>&lt;name&gt;</i></p>
<dd> Use a different sessionrc for this GIMP session. The given session name is appended to the default sessionrc filename.</p>
<dt><code>-g, &#8211;gimprc </code><i>&lt;gimprc&gt;</i></p>
<dd> Use an alternative gimprc instead of the default one. Useful in cases where plug-in paths or machine specs may be different.</p>
<dt><code>&#8211;system-gimprc </code><i>&lt;gimprc&gt;</i></p>
<dd> Use an alternate system gimprc file.</p>
<dt><code>&#8211;dump-gimprc</code></p>
<dd> Output a gimprc file with default settings.</p>
<dt><code>&#8211;debug-handlers</code></p>
<dd> Enable debugging signal handlers.</p>
<dt><code>-c, &#8211;console-messages</code></p>
<dd> Do not popup dialog boxes on errors or warnings. Print the messages on the console instead.</p>
<dt><code>&#8211;stack-trace-mode </code><i>{never|query|always}</i></p>
<dd> If a stack-trace should be generated in case of fatal signals.</p>
<dt><code>&#8211;pdb-compat-mode </code><i>{off|on|warn}</i></p>
<dd> If the PDB should provide aliases for deprecated functions.</p>
<dt><code>&#8211;batch-interpreter </code><i>&lt;procedure&gt;</i></p>
<dd> Specifies the procedure to use to process batch events. The default is to let Script-Fu evaluate the commands.</p>
<dt><code>-b, &#8211;batch </code><i>&lt;command&gt;</i></p>
<dd> Execute <i>&lt;command&gt;</i> non-interactively. This option may appear multiple times. The <i>&lt;command&gt;</i> is passed to the batch interpreter. When <i>&lt;command&gt;</i> is <code>&#8211;</code> the commands are read from standard input. </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> GIMP respects a number of environment variables. </p>
<dl>
<dt><code>DISPLAY</code></p>
<dd> to get the default host and display number.</p>
<dt><code>GIMP2_DIRECTORY</code></p>
<dd> to get the name of the personal GIMP directory. If unset .gimp-2.8 is used. If this is an absolute path, it is used as is. If it is a relative path, it is taken to be a subdirectory of the home directory.</p>
<dt><code>GIMP2_DATADIR</code></p>
<dd> to get the base location for data files such as brushes and patterns. If unset ${datarootdir}/gimp/2.0 is used.</p>
<dt><code>GIMP2_LOCALEDIR</code></p>
<dd> to get the base location for translations. If unset ${datarootdir}/locale is used.</p>
<dt><code>GIMP2_PLUGINDIR</code></p>
<dd> to get the base location for plug-ins and modules. If unset /usr/lib/gimp/2.0 is used.</p>
<dt><code>GIMP2_SYSCONFDIR</code></p>
<dd> to get the location of configuration files. If unset /etc/gimp/2.0 is used. </p>
<p> On Linux GIMP can be compiled with support for binary relocatibility. This will cause data, plug-ins and configuration files to be searched relative to the location of the gimp executable file unless overridden by the environment variables mentioned above. </p>
</dl>
<h2>FILES</h2>
<p> GIMP&#8217;s data files are stored in ${datarootdir}/gimp/2.0, where ${datarootdir} is set on install, but is typically /usr/share. GIMP&#8217;s system-wide configuration files are stored in /etc/gimp/2.0, where ${prefix} is typically /usr. </p>
<p> Most GIMP configuration is read in from the user&#8217;s init file, <code>$HOME</code>/.gimp-2.8/gimprc. The system wide equivalent is in /etc/gimp/2.0/gimprc. The system wide file is parsed first and the user gimprc can override the system settings. /etc/gimp/2.0/gimprc_user is the default gimprc placed in users&#8217; home directories the first time GIMP is run. </p>
<p> <code>$HOME</code>/.gimp-2.8/devicerc &#8211; holds settings for input devices together with the tool, colors, brush, pattern and gradient associated to that device. </p>
<p> <code>$HOME</code>/.gimp-2.8/gtkrc &#8211; users set of GIMP-specific GTK+ config settings. Options such as widget color and fonts sizes can be set here. </p>
<p> /etc/gimp/2.0/gtkrc &#8211; system wide default set of GIMP-specific GTK+ config settings. </p>
<p> <code>$HOME</code>/.gimp-2.8/menurc &#8211; user&#8217;s set of keybindings. </p>
<p> <code>$HOME</code>/.gimp-2.8/parasiterc &#8211; Stores all persistent GIMP parasites. This file will be rewritten every time you quit GIMP. </p>
<p> <code>$HOME</code>/.gimp-2.8/sessionrc &#8211; This file takes session-specific info (that is info, you want to keep between two GIMP sessions). You are not supposed to edit it manually, but of course you can do. This file will be entirely rewritten every time you quit GIMP. If this file isn&#8217;t found, defaults are used. </p>
<p> <code>$HOME</code>/.gimp-2.8/templaterc &#8211; Image templates are kept in this file. New images can conveniently created from these templates. If this file isn&#8217;t found, defaults are used. </p>
<p> /etc/gimp/2.0/unitrc &#8211; default user unit database. It contains the unit definitions for centimeters, meters, feet, yards, typographic points and typographic picas and is placed in users home directories the first time GIMP is ran. If this file isn&#8217;t found, defaults are used. </p>
<p> <code>$HOME</code>/.gimp-2.8/unitrc &#8211; This file contains your user unit database. You can modify this list with the unit editor. You are not supposed to edit it manually, but of course you can do. This file will be entirely rewritten every time you quit GIMP. </p>
<p> <code>$HOME</code>/.gimp-2.8/plug-ins &#8211; location of user installed plug-ins. </p>
<p> <code>$HOME</code>/.gimp-2.8/pluginrc &#8211; plug-in initialization values are stored here. This file is parsed on startup and regenerated if need be. </p>
<p> <code>$HOME</code>/.gimp-2.8/modules &#8211; location of user installed modules. </p>
<p> <code>$HOME</code>/.gimp-2.8/tmp &#8211; default location that GIMP uses as temporary space. </p>
<p> ${datarootdir}/gimp/2.0/brushes &#8211; system wide brush files. </p>
<p> <code>$HOME</code>/.gimp-2.8/brushes &#8211; user created and installed brush files. These files are in the .gbr, .gih or .vbr file formats. </p>
<p> <code>$HOME</code>/.gimp-2.8/curves &#8211; Curve profiles and presets as saved from the Curves tool. </p>
<p> <code>$HOME</code>/.gimp-2.8/gimpressionist &#8211; Presets and user created brushes and papers are stored here. </p>
<p> <code>$HOME</code>/.gimp-2.8/levels &#8211; Level profiles and presets as saved from the Levels tool. </p>
<p> ${datarootdir}/gimp/2.0/palettes &#8211; the system wide palette files. </p>
<p> <code>$HOME</code>/.gimp-2.8/palettes &#8211; user created and modified palette files. This files are in the .gpl format. </p>
<p> ${datarootdir}/gimp/2.0/patterns &#8211; basic set of patterns for use in GIMP. </p>
<p> <code>$HOME</code>/.gimp-2.8/patterns &#8211; user created and installed gimp pattern files. This files are in the .pat format. </p>
<p> ${datarootdir}/gimp/2.0/gradients &#8211; standard system wide set of gradient files. </p>
<p> <code>$HOME</code>/.gimp-2.8/gradients &#8211; user created and installed gradient files. </p>
<p> ${datarootdir}/gimp/2.0/scripts &#8211; system wide directory of scripts used in Script-Fu and other scripting extensions. </p>
<p> <code>$HOME</code>/.gimp-2.8/scripts &#8211; user created and installed scripts. </p>
<p> ${datarootdir}/gimp/2.0/gflares &#8211; system wide directory used by the gflare plug-in. </p>
<p> <code>$HOME</code>/.gimp-2.8/gflares &#8211; user created and installed gflare files. </p>
<p> ${datarootdir}/gimp/2.0/gfig &#8211; system wide directory used by the gfig plug-in. </p>
<p> <code>$HOME</code>/.gimp-2.8/gfig &#8211; user created and installed gfig files. </p>
<p> ${datarootdir}/gimp/2.0/images/gimp-splash.png &#8211; the default image used for the GIMP splash screen. </p>
<p> ${datarootdir}/gimp/2.0/images/gimp-logo.png &#8211; image used in the GIMP about dialog. </p>
<p> ${datarootdir}/gimp/2.0/tips/gimp-tips.xml &#8211; tips as displayed in the &quot;Tip of the Day&quot; dialog box. </p>
<h2>SPLASH IMAGES</h2>
<p> GIMP comes with a default image for the splash screen but it allows system administrators and users to customize the splash screen by providing other images. The image to be used with the splash screen is chosen as follows: </p>
<dl>
<dt>1.</p>
<dd> GIMP tries to load a random splash screen from the directory <code>$HOME</code>/.gimp-2.8/splashes.</p>
<dt>2.</p>
<dd> It then falls back to using <code>$HOME</code>/.gimp-2.8/gimp-splash.png.</p>
<dt>3.</p>
<dd> If the user didn&#8217;t install any custom splash images, a random image is picked from ${datarootdir}/gimp/2.0/splashes.</p>
<dt>4.</p>
<dd> As a last resort, GIMP uses the default splash image located at ${datarootdir}/gimp/2.0/images/gimp-splash.png. </p>
</dl>
<h2>SUGGESTIONS AND BUG REPORTS</h2>
<p> Any bugs found should be reported to the online bug-tracking system available on the web at <a rel="nofollow" href="http://bugzilla.gnome.org/.">http://bugzilla.gnome.org/.</a> Before reporting bugs, please check to see if the bug has already been reported. </p>
<p> When reporting GIMP bugs, it is important to include a reliable way to reproduce the bug, version number of GIMP (and probably GTK+), OS name and version, and any relevant hardware specs. If a bug is causing a crash, it is very useful if a stack trace can be provided. And of course, patches to rectify the bug are even better. </p>
<h2>OTHER INFO</h2>
<p> The canonical place to find GIMP info is at <a rel="nofollow" href="http://www.gimp.org/.">http://www.gimp.org/.</a> Here you can find links to just about many other GIMP sites, tutorials, data sets, mailing list archives, and more. </p>
<p> There is also a GIMP User Manual available at <a rel="nofollow" href="http://docs.gimp.org/">http://docs.gimp.org/</a> that goes into much more detail about the interactive use of GIMP. </p>
<p> The latest versions of GIMP and the GTK+ libs are always available at <a href="ftp://ftp.gimp.org/.">ftp://ftp.gimp.org/.</a> </p>
<h2>AUTHORS</h2>
<p> Spencer Kimball, Peter Mattis and the GIMP Development Team. </p>
<p> With patches, fixes, plug-ins, extensions, scripts, translations, documentation and more from lots and lots of people all over the world. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-gimprc/">gimprc</a></code>(5), <code><a href="/docs/linux/man/1-gimptool/">gimptool</a></code>(1), </p>
<h2>Index</h2>
