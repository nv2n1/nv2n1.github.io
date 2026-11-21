---
title: "gource(1)"
name: "gource"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gource/"
description: "Gource – a software version control visualization"
---

<h2>NAME</h2>
<p> Gource &#8211; a software version control visualization</p>
<h2>SYNOPSIS</h2>
<p> <i>gource</i> &lt;options&gt; &lt;path&gt;</p>
<h2>DESCRIPTION</h2>
<p> <i>gource</i> is an OpenGL-based 3D visualisation tool for source control repositories. </p>
<p> The repository is displayed as a tree where the root of the repository is the centre, directories are branches and files are leaves. Contributors to the source code appear and disappear as they contribute to specific files and directories.</p>
<h2>REQUIREMENTS</h2>
<p> <i>gource</i> requires a OpenGL capable video card to run.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code></dt>
<dd> Fullscreen</dd>
<dt><code>-WIDTHxHEIGHT</code></dt>
<dd> Set the window size. If -f is also supplied, will attempt to set the video mode to this also.</dd>
<dt><code>-p, &#8211;start-position POSITION</code></dt>
<dd> Begin at some position in the log (between 0.0 and 1.0).</dd>
<dt><code> &#8211;stop-position POSITION</code></dt>
<dd> Stop (exit) at some position in the log (does not work with STDIN).</dd>
<dt><code> &#8211;stop-on-idle</code></dt>
<dd> Stop on break in activity. May be combined with &#8211;stop-position.</dd>
<dt><code> &#8211;stop-at-end</code></dt>
<dd> Stop (exit) at the end of the log / stream.</dd>
<dt><code> &#8211;loop</code></dt>
<dd> Loop back to the start of the log when the end is reached.</dd>
<dt><code>-a, &#8211;auto-skip-seconds SECONDS</code></dt>
<dd> Automatically skip to next entry if nothing happens for a specified number of seconds.</dd>
<dt><code>-s, &#8211;seconds-per-day SECONDS</code></dt>
<dd> Speed of simulation in seconds per day.</dd>
<dt><code>&nbsp;<wbr> &#8211;realtime</code></dt>
<dd> Realtime playback speed.</dd>
<dt><code>-i, &#8211;file-idle-time SECONDS</code></dt>
<dd> Time in seconds files remain idle before they are removed.</dd>
<dt><code>-e, &#8211;elasticity FLOAT</code></dt>
<dd> Elasticity of nodes.</dd>
<dt><code>-b, &#8211;background FFFFFF</code></dt>
<dd> Background colour in hex.</dd>
<dt><code>&#8211;date-format FORMAT</code></dt>
<dd> Specify display date string (strftime format).</dd>
<dt><code>&#8211;log-format FORMAT</code></dt>
<dd> Specify format of the log being read (git,cvs,custom). Required when reading STDIN.</dd>
<dt><code>&#8211;git-branch</code></dt>
<dd> Get the git log of a branch other than the current one.</dd>
<dt><code>&#8211;git-log-command</code></dt>
<dd> Print the git log command used by <i>gource</i>.</dd>
<dt><code>&#8211;hg-log-command</code></dt>
<dd> Print the hg log command (Mercurial) used by <i>gource</i>.</dd>
<dt><code>&#8211;cvs-exp-command</code></dt>
<dd> Print the cvs-exp.pl log command used by <i>gource</i>.</dd>
<dt><code>&#8211;follow-user USER</code></dt>
<dd> Have the camera automatically follow a particular user.</dd>
<dt><code>&#8211;highlight-user USER</code></dt>
<dd> Highlight the names of a particular user.</dd>
<dt><code>&#8211;highlight-all-users</code></dt>
<dd> Highlight the names of all users.</dd>
<dt><code>&#8211;file-filter REGEX</code></dt>
<dd> Filter out any files matching a specified regular expression.</dd>
<dt><code>&#8211;user-image-dir DIRECTORY</code></dt>
<dd> Directory containing .jpg or .png images of users (eg &#8216;Full Name.png&#8217;) to use as avatars.</dd>
<dt><code>&#8211;default-user-image IMAGE</code></dt>
<dd> Path of .jpg to use as the default user image.</dd>
<dt><code>&#8211;colour-images</code></dt>
<dd> Colourize user images.</dd>
<dt><code>&#8211;crop AXIS</code></dt>
<dd> Crop view on an axis (vertical,horizontal).</dd>
<dt><code>&#8211;multi-sampling</code></dt>
<dd> Enable multi-sampling.</dd>
<dt><code>&#8211;bloom-multiplier FLOAT</code></dt>
<dd> Adjust the amount of bloom.</dd>
<dt><code>&#8211;bloom-intensity FLOAT</code></dt>
<dd> Adjust the intensity of the bloom.</dd>
<dt><code>&#8211;disable-progress</code></dt>
<dd> Disable progress bar.</dd>
<dt><code>&#8211;disable-bloom</code></dt>
<dd> Disable bloom effect.</dd>
<dt><code>&#8211;max-files</code></dt>
<dd> Set the maximum number of files. Excess files will be discarded.</dd>
<dt><code>&#8211;max-file-lag SECONDS</code></dt>
<dd> Max time files of a commit can take to appear.</dd>
<dt><code>&#8211;max-user-speed UNITS</code></dt>
<dd> Max speed users can travel per second.</dd>
<dt><code>&#8211;user-friction SECONDS</code></dt>
<dd> Time users come to a complete hault.</dd>
<dt><code>&#8211;user-scale SCALE</code></dt>
<dd> Change scale of users.</dd>
<dt><code>&#8211;hide-users</code></dt>
<dd> Hide users.</dd>
<dt><code>&#8211;hide-tree</code></dt>
<dd> Hide tree.</dd>
<dt><code>&#8211;hide-files</code></dt>
<dd> Hide files.</dd>
<dt><code>&#8211;hide-usernames</code></dt>
<dd> Hide usernames.</dd>
<dt><code>&#8211;hide-filenames</code></dt>
<dd> Hide filenames.</dd>
<dt><code>&#8211;hide-dirnames</code></dt>
<dd> Hide directory names.</dd>
<dt><code>&#8211;hide-date</code></dt>
<dd> Hide the date.</dd>
<dt><code>&#8211;output-ppm-stream FILE</code></dt>
<dd> Write frames as PPM to a file (&#8216;-&#8216; for STDOUT).</dd>
<dt><code>&#8211;output-framerate FPS</code></dt>
<dd> Framerate of output (used with &#8211;output-ppm-stream).</dd>
<dt><code>path</code></dt>
<dd> Either a Git or Mercurial directory, a pre-generated log file (see &#8211;git-log-command, &#8211;hg-log-command or the custom log format) or &#8216;-&#8216; to read STDIN. If path is ommited <i>gource</i> will attempt to read a log from the current directory.</dd></dl>
<h2>GIT AND MERCURIAL EXAMPLES</h2>
<p> View the log of the respository in the current path: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <i>gource</i> </p>
<p> View the log of a project in the specified directory: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <i>gource</i> my-project-dir </p>
<p> Save a copy of the log using in a special log format and play it back (example is for Git, Mercurial users see &#8211;hg-log-command): </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> cd my-git-project<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> `<i>gource</i> &#8211;git-log-command` &gt; my-git-project.log<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <i>gource</i> my-git-project.log </p>
<p> NOTE: &#8211;git-log-command assumes you have a recent version of git that supports all the options. You may need to modify the command line to work with an older version (changing %aN to %an for instance). </p>
<h2>OTHER VERSION CONTROL SYSTEMS</h2>
<p> The Gource homepage has guides and examples for using Gource with other version control systems: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> CVS &#8211; <a rel="nofollow" href="http://code.google.com/p/gource/wiki/CVS">http://code.google.com/p/gource/wiki/CVS</a><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> SVN &#8211; <a rel="nofollow" href="http://code.google.com/p/gource/wiki/SVN">http://code.google.com/p/gource/wiki/SVN</a> </p>
<h2>CUSTOM LOG FORMAT</h2>
<p> If you want to use Gource with something other than the supported systems, there is a pipe (&#8216;|&#8217;) delimited custom log format: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> timestamp &#8211; A unix timestamp of when the update occured.<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> username &#8211; The name of the user who made the update.<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> type &#8211; Single character for the update type &#8211; (A)dded, (M)odified or (D)eleted.<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> file &#8211; Path of the file updated.<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> colour &#8211; A colour for the file in hex (FFFFFF) format. Optional. </p>
<h2>RECORDING VIDEOS</h2>
<p> See the guide on the homepage for examples of recording videos with Gource: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <a rel="nofollow" href="http://code.google.com/p/gource/wiki/Videos">http://code.google.com/p/gource/wiki/Videos</a> </p>
<h2>INTERFACE</h2>
<p> The time shown in the top left of the screen is set initially from the first log entry read and is incremented according to the simulation speed (&#8211;seconds-per-day). </p>
<p> Pressing SPACE at any time will pause/unpause the simulation. While paused you may use the mouse to inspect the detail of individual files and users. </p>
<p> TAB cycles through selecting the current visible users. </p>
<p> The camera mode, either tracking activity, or showing the entire code tree, can be toggled using the V key. </p>
<p> Interactive keyboard commands: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> (V) Toggle camera mode<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> (C) Displays Gource logo<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> (N) Jump forward in time to next log entry.<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> (+-) Adjust simulation speed.<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> (&lt;&gt;) Adjust time scale.<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> (TAB) Cycle through visible users<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> (ESC) Quit</p>
<h2>AUTHOR</h2>
<pre>
 Written by Andrew Caudwell
 Project Homepage: <a rel="nofollow" href="http://gource.googlecode.com/">http://gource.googlecode.com/</a>
</pre>
<h2>COPYRIGHT</h2>
<pre><code>
Copyright(C) 2009 Andrew Caudwell(acaudwell[at] gmail.com)
    This program is free software;
you can redistribute it and / or
    modify it under the terms of the GNU General Public License
        as published by the Free Software Foundation;
either version 3 of the License, or (at your option) any later version.This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 You should have received a copy of the GNU General Public License
 along with this program.  If not, see &lt;http://www.gnu.org/licenses/&gt;.
</code></pre>
<h2>ACKNOWLEDGEMENTS</h2>
<pre>
 Catalyst IT (catalyst.net.nz)
 For supporting the development of Gource!
</pre>
