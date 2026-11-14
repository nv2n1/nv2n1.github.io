---
title: "gmtswitch(1)"
name: "gmtswitch"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmtswitch/"
description: "gmtswitch – Switching between different GMT versions"
---

<h2>NAME</h2>
<p> gmtswitch &#8211; Switching between different GMT versions</p>
<h2>SYNOPSIS</h2>
<p> <code>gmtswitch</code> [ D | <i>version</i> ]</p>
<h2>INTRODUCTION</h2>
<p> <code>gmtswitch</code> helps you modify your environment to allow for the switching back and forth between several installed GMT versions, in particular GMT 5 and versions from the GMT 4 series. It works by maintaining a list of directories to GMT installations in a file in your home directory, then manipulates a symbolic link to point to the GMT directory whose executables we wish to use [The Windows version works a bit differently; see WINDOWS below].</p>
<h2>REQUIRED ARGUMENTS</h2>
<p> None. If no arguments are given you are presented with a menu of installed GMT versions from 1 to <i>n</i> and you specify which one you wish to switch to.</p>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>D</code></p>
<dd> Select the default GMT version. This is the first entry in the ~/.gmtversions file</p>
<dt><i>version</i></p>
<dd> Search for a unique match in the ~/.gmtversions file. If one match is found we switch to that entry; otherwise an error is generated. where module is the name of a GMT program and the options are those that pertain to that particular program.</dl>
<h2>SETUP</h2>
<p> If you have official versions installed then running gmtswitch the very first time will examine your hard disk starting at / and look for directories with GMT4 or GMT5 in the name. This will fail to find the subversion directories and possibly others you have placed elsewhere. The fastest way to get up and running is this:</p>
<dl>
<dt>1.</p>
<dd>
<dt><code>Edit/Create ~/.gmtversions and add the paths to all GMT installations</code></p>
<dd> you have or care to consider. Each path goes on separate lines and points to the top dir of each distribution, e.g., /Users/pwessel/UH/RESEARCH/PROJECTS/GMTdev/GMT4.5.7</p>
<dt>2.</p>
<dd>
<dt><code>In your .bashrc or .[t]csrh or wherever you are maintaining your PATH</code></p>
<dd> or path variable, remove any directories you have added that contain GMT, and add the new path $HOME/this_gmt/bin (might be $home for csh users). Make sure this path appears before any others that might contain a GMT installation, such as those used by package managers (e.g., /sw/bin for fink, /opt/local/bin for Macports, etc.).</p>
<dt>3.</p>
<dd> Make the new path take effect (quit/restart terminal, logout/login, etc).</p>
<dt>4.</p>
<dd>
<dt><code>cd to the most recent GMT directory where a gmtswitch version lives,</code></p>
<dd> and run gmtswitch with no argument. Select one of the version from the menu.</p>
<dt>5.</p>
<dd> If in csh you may have to say rehash afterwards.</p>
<dt>6.</p>
<dd>
<dt><code>Type psxy &#8211; and the synopsis should tell you that you got the</code></p>
<dd> correct version. You can now run gmtswitch from anywhere; try it out and make sure that you can switch between the versions.</dl>
<h2>EXAMPLES</h2>
<p> To switch to GMT version 4.5.7 (assuming it was installed as such and not via a package manager), try gmtswitch GMT4.5.7 </p>
<p> To switch to the default (your top choice), do gmtswitch D </p>
<p> Finally, to select from the menu, just run gmtswitch </p>
<p> and pick the one you want.</p>
<h2>BEWARE</h2>
<p> GMT remembers where it was installed the first time and uses that dir to find the default GMT share directory. If you move entire GMT installation after compilation then you may have to set GMT_SHAREDIR to point to the top dir in order for things to work. It is best not to move things after installation.</p>
<h2>WINDOWS</h2>
<p> Under Windows use gmtswitch.bat which is a batch script that changes the Windows PATH variable so that the BIN directory of the preferred version always comes first. To do that the batch works in two alternative modes: </p>
<p> 1 &#8211; Permanent mode </p>
<p> 2 &#8211; Temporary mode </p>
<p> The permanent mode makes use of the free executable program &quot;EditPath&quot; to change the user path in the registry. It&#8217;s called permanent because the changes remains until &#8230; next change. See </p>
<p> <i><a rel="nofollow" href="http://www.softpedia.com/get/Tweak/Registry-Tweak/EditPath.shtml">http://www.softpedia.com/get/Tweak/Registry-Tweak/EditPath.shtml</a></i> </p>
<p> Of course the editpath.exe binary must be in your system&#8217;s path as well. WARNING: The path change will not be visible on the shell cmd where it was executed. For the change to be active you will need to open a new cmd window. </p>
<p> The second mode is temporary because the path to the selected GMT binary dir is prepended to the previous path via a shell command line. This modification disappears when the shell cmd window where it was executes is deleted. </p>
<p> It is the user responsibility to set the contents of the G32_32 to G5_64 below to valid paths where the binaries of the different GMT versions are installed Note that it is not mandatory to have all four of them in you computer. For the ones you do not have just let them pointing to nothing e.g., </p>
<p> set G4_64= </p>
<p> The permanent mode is the default one (but this can be changed. See edit section) To run in the temporary mode just give a second argument (doesn&#8217;t matter what) </p>
<p> Example usage to set a GMT5 64 bits permanent </p>
<p> gmtswitch g5_64 </p>
<p> To temporary set a GMT4 32 bits do </p>
<p> gmtswitch g4_32 1 </p>
<p> Run without arguments to get a &quot;Usage&quot; (for permanent mode)</p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
