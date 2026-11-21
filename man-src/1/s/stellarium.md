---

title: "stellarium(1)"
name: "stellarium"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stellarium/"
description: "stellarium – A real-time realistic planetarium"
---

<p> stellarium [<font SIZE="-1"><code>OPTIONS</code></font>]</p>
<p> Stellarium is a free <font SIZE="-1">GPL</font> software which renders realistic skies in real time with OpenGL. It is available for Linux/Unix, Windows and MacOSX. With Stellarium, you really see what you can see with your eyes, binoculars or a small telescope.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v, &#8211;version</code></dt>
<dd> Print program name and version and exit.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Print a brief synopsis of program options and exit.</dd>
<dt><code>&#8211;safe-mode</code></dt>
<dd> Do not use OpenGL2 features (such as shaders). Useful on systems that report support for OpenGL 2, but its implementation is buggy. Used as a work-around for the &#8220;broken fonts&#8221; bug.</dd>
<dt><code>-c, &#8211;config-file</code> <i>file</i></dt>
<dd> Use <i>file</i> for the config filename instead of the default <i>config.ini</i>.</dd>
<dt><code>-u, &#8211;user-dir</code> <i>dir</i></dt>
<dd> Use <i>dir</i> instead of the default user data directory (<i></i>$HOME<i>/.stellarium/</i> on *nix operating systems).</dd>
<dt><code>-f, &#8211;full-screen</code> <i>yes|no</i></dt>
<dd> With argument <i>yes</i> or <i>no</i> over-rides the full screen setting in the config file. The setting is saved in the config-file and as such will be the default for subsequent invocations of Stellarium.</dd>
<dt><code>&#8211;screenshot-dir</code> <i>dir</i></dt>
<dd> Set the directory into which screenshots will be saved to <i>dir</i>, instead of the default (which is <tt>$HOME</tt> on *nix operating systems).</dd>
<dt><code>&#8211;home-planet</code> <i>planet-name</i></dt>
<dd> Specify observer planet. <i>planet-name</i> is an English name, and should refer to an object defined in the <i>ssystem.ini</i> file.</dd>
<dt><code>&#8211;altitude</code> <i>alt</i></dt>
<dd> Specify the initial observer altitude, where <i>alt</i> is the altitude in meters.</dd>
<dt><code>&#8211;longitude</code> <i>lon</i></dt>
<dd> Specify the initial observer longitude, where <i>lon</i> is the longitude. The format is illustrated by this example: +4d16&#8217;12&quot; which refers to 4 degrees, 16 minutes and 12 arc seconds East. Westerly longitudes should be prefixed with <tt>&quot;-&quot;</tt>.</dd>
<dt><code>&#8211;latitude</code> <i>lat</i></dt>
<dd> Specify the initial observer latitude, where <i>lat</i> is the latitude. The format is illustrated by this example: +53d58&#8217;16.65&quot; which refers to 53 degrees, 58 minutes and 16.65 arc seconds North. Southerly latitudes should be prefixed with <tt>&quot;-&quot;</tt>.</dd>
<dt><code>&#8211;list-landscapes</code></dt>
<dd> Print a list of landscape names and exit.</dd>
<dt><code>&#8211;landscape</code> <i>name</i></dt>
<dd> Start Stellarium using landscape <i>name</i>. Refer to <code>&#8211;list-landscapes</code> for possible names.</dd>
<dt><code>&#8211;sky-date</code> <i>date</i></dt>
<dd> Specify sky date in format yyyymmdd.</dd>
<dt><code>&#8211;sky-time</code> <i>time</i></dt>
<dd> Specify sky time in format hh:mm:ss.</dd>
<dt><code>&#8211;fov</code> <i>fov</i></dt>
<dd> Specify the field of view (<i>fov</i> degrees).</dd>
<dt><code>&#8211;projection-type</code> <i>p</i></dt>
<dd> Specify projection type, <i>p</i>. Permitted values of <i>p</i> are: equalarea, stereographic, fisheye, cylinder, mercator, perspective, and orthographic.</dd></dl>
<h2>RETURN VALUE</h2>
<dl>
<dt>0</dt>
<dd> Completed successfully.</dd>
<dt>not 0</dt>
<dd> Some sort of error.</dd></dl>
<h2>FILES</h2>
<p> Note: file locations on non-*nix operating systems (include <font SIZE="-1">OSX</font>) may vary. Please refer to the Stellarium User Guide for more details, as well as information on how to customise the Stellarium data files.</p>
<dl>
<dt><i>/usr/share/stellarium/</i></dt>
<dd> This is the Installation Data Directory set at compile-time.</dd>
<dt><i>$HOME/.stellarium/</i></dt>
<dd> This is the User Data Directory, which may be over-ridden using command line option <code>-u</code>. It contains the user&#8217;s settings, extra landscapes, scripts, and can also be used to over-ride data files which are provided with the default install.</dd>
<dt><i>$HOME/.stellarium/config.ini</i></dt>
<dd> The default main configuration file is <i>config.ini</i>. Refer to <code>-c</code> above to use a different filename and to <code>-u</code> to use a different User Data Directory.</dd>
<dt><i>$HOME/</i></dt>
<dd> The default screenshot directory. Refer to <code>&#8211;screenshot-dir</code> to use a different path.</dd></dl>
<h2>SEE ALSO</h2>
<p> <i>celestia</i>(1).</p>
<h2>NOTES</h2>
<p> Sources of more information:</p>
<dl>
<dt>Websites</dt>
<dd> Main website: &lt;<a rel="nofollow" href="http://stellarium.org/">http://stellarium.org/</a>&gt; </dd>
<p> Wiki: &lt;<a rel="nofollow" href="http://stellarium.org/wiki/">http://stellarium.org/wiki/</a>&gt; </p>
<p> Forums: &lt;<a rel="nofollow" href="http://sourceforge.net/projects/stellarium/forums">http://sourceforge.net/projects/stellarium/forums</a>&gt; </p>
<p> Downloads: &lt;<a rel="nofollow" href="http://sourceforge.net/projects/stellarium/files/">http://sourceforge.net/projects/stellarium/files/</a>&gt; </p>
<p> Support Requests: &lt;<a rel="nofollow" href="https://answers.launchpad.net/stellarium">https://answers.launchpad.net/stellarium</a>&gt; </p>
<p> Bug Tracker: &lt;<a rel="nofollow" href="https://bugs.launchpad.net/stellarium">https://bugs.launchpad.net/stellarium</a>&gt;</p>
<dt>The Stellarium User Guide</dt>
<dd> Visit the downloads page to get a <font SIZE="-1">PDF</font> copy of the Stellarium User Guide.</dd></dl>
<h2>BUGS</h2>
<p> Please report bugs using the bug tracker link in the <font SIZE="-1">NOTES</font> section of this page.</p>
<h2>AUTHOR</h2>
<p> Fabien Chereau, Rob Spearman, Johan Meuris, Matthew Gates, Johannes Gajdosik, Nigel Kerr, Andras Mohari, Bogdan Marinov, Timothy Reaves, Mike Storm, Diego Marcos, Guillaume Chereau, Alexander Wolf, Georg Zotti </p>
<p> x14817 </p>
