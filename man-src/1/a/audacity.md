---
title: "audacity(1)"
name: "audacity"
section: "1"
letter: "a"
url: "/docs/linux/man/1-audacity/"
description: "audacity – Graphical cross-platform audio editor"
---

<h2>NAME</h2>
<p> audacity &#8211; Graphical cross-platform audio editor</p>
<h2>SYNOPSIS</h2>
<p> <code>audacity</code> -help<br />
 <code>audacity</code> -version </p>
<p> <code>audacity</code> [-blocksize nnn] -test<br />
 <code>audacity</code> [-blocksize nnn] [ <i>AUDIO-FILE</i> ] <code>&#8230;</code></p>
<h2>DESCRIPTION</h2>
<p> <code>Audacity</code> is a graphical audio editor. This man page does not describe all of the features of Audacity or how to use it; for this, see the html documentation that came with the program, which should be accessible from the Help menu. This man page describes the Unix-specific features, including special files and environment variables. </p>
<p> Audacity currently uses <code>libsndfile</code> to open many uncompressed audio formats such as WAV, AIFF, and AU, and it can also be linked to <code>libmad,</code> <code>libvorbis,</code> and <code>libflac,</code> to provide support for opening MP2/3, Ogg Vorbis, and FLAC files, respectively. <code>LAME, libvorbis, libflac</code> and <code>libtwolame</code> provide facilities to export files to all these formats as well. </p>
<p> Audacity is primarily an interactive, graphical editor, not a batch-processing tool. Whilst there is a basic batch processing tool it is experimental and incomplete. If you need to batch-process audio or do simple edits from the command line, using <code>sox</code> or <code>ecasound</code> driven by a bash script will be much more powerful than audacity. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-help</code></p>
<dd> display a brief list of command line options</p>
<dt><code>-version</code></p>
<dd> display the audacity version number</p>
<dt><code>-test</code></p>
<dd> run self diagnostics tests (only present in development builds)</p>
<dt><code>-blocksize nnn</code></p>
<dd> set the audacity block size for writing files to disk to nnn bytes </p>
</dl>
<h2>FILES</h2>
<p> <i>~/.audacity-data/audacity.cfg</i></p>
<dl>
<dt>
<dd> Per user configuration file.</dl>
<p> <i>/var/tmp/audacity-&lt;user&gt;/</i></p>
<dl>
<dt>
<dd> Default location of Audacity&#8217;s temp directory, where &lt;user&gt; is your username. If this location is not suitable (not enough space in /var/tmp, for example), you should change the temp directory in the Preferences and restart Audacity. Audacity is a disk-based editor, so the temp directory is very important: it should always be on a fast (local) disk with lots of free space. </p>
<p> Note that older versions of Audacity put the temp directory inside of the user&#8217;s home directory. This is undesirable on many systems, and using some directory in /tmp is recommended. </p>
<p> On many modern Linux systems all files in /tmp/ will be deleted each time the system boots up, which makes recovering a recording that was going on when the system crashed much harder. This is why the default is to use a directory in /var/tmp/ which will not normally be deleted by the system. Open the Preferences to check.</dl>
<h2>SEARCH PATH</h2>
<p> When looking for plug-ins, help files, localization files, or other configuration files, Audacity searches the following locations, in this order: </p>
<p> <i>AUDACITY_PATH</i></p>
<dl>
<dt>
<dd> Any directories in the <i>AUDACITY_PATH </i> environment variable will be searched before anywhere else.</dl>
<p> <i>.</i></p>
<dl>
<dt>
<dd> The current working directory when Audacity is started.</dl>
<p> <i>~/.audacity-data/Plug-Ins</i> </p>
<p> <i>&lt;prefix&gt;/share/audacity</i></p>
<dl>
<dt>
<dd> The system-wide Audacity directory, where &lt;prefix&gt; is usually /usr or /usr/local, depending on where the program was installed.</dl>
<p> <i>&lt;prefix&gt;/share/doc/audacity</i></p>
<dl>
<dt>
<dd> The system-wide Audacity documentation directory, where &lt;prefix&gt; is usually /usr or /usr/local, depending on where the program was installed.</dl>
<p> For localization files in particular (i.e. translations of Audacity into other languages), Audacity also searches <i>&lt;prefix&gt;/share/locale</i> </p>
<h2>PLUG-INS</h2>
<p> Audacity supports two types of plug-ins on Unix: LADSPA and Nyquist plug-ins. These are generally placed in a directory called <i>plug-ins </i> somewhere on the search path (see above). </p>
<p> LADSPA plug-ins can either be in the plug-ins directory, or alternatively in a <i>ladspa </i> directory on the search path if you choose to create one. Audacity will also search the directories in the <i>LADSPA_PATH </i> environment variable for additional LADSPA plug-ins. </p>
<p> Nyquist plug-ins can either be in the plug-ins directory, or alternatively in a <i>nyquist</i> directory on the search path if you choose to create one. </p>
<h2>VERSION</h2>
<p> This man page documents audacity version 1.3.5 </p>
<h2>LICENSE</h2>
<p> Audacity is distributed under the GPL, however some of the libraries it links to are distributed under other free licenses, including the LGPL and BSD licenses. </p>
<h2>BUGS</h2>
<p> For details of known problems, see the release notes and the audacity wiki:<br />
 <a rel="nofollow" href="http://www.audacityteam.org/wiki/index.php?title=Known_Issues">http://www.audacityteam.org/wiki/index.php?title=Known_Issues</a> </p>
<p> To report a bug, see the instructions at<br />
 <a rel="nofollow" href="http://www.audacityteam.org/wiki/index.php?title=Reporting_Bugs">http://www.audacityteam.org/wiki/index.php?title=Reporting_Bugs</a> </p>
<h2>AUTHORS</h2>
<p> Project leaders include Dominic Mazzoni, Matt Brubeck, James Crook, Vaughan Johnson, Leland Lucius, and Markus Meyer, but dozens of others have contributed, and Audacity would not be possible without wxWindows, libsndfile, and many of the other libraries it is built upon. For the most recent list of contributors and current email addresses, see our website: </p>
<p> <a rel="nofollow" href="http://audacity.sourceforge.net/about/credits/">http://audacity.sourceforge.net/about/credits/</a> </p>
<h2>Index</h2>
