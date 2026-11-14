---
title: "mikmod(1)"
name: "mikmod"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mikmod/"
description: "mikmod – play soundtracker etc. modules on a Unix machine."
---

<h2>NAME</h2>
<p> mikmod &#8211; play soundtracker etc. modules on a Unix machine. </p>
<h2>SYNOPSIS</h2>
<p> <code>mikmod [-options</code>]&#8230; [<code>module</code>|<code>playlist</code>]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <i>MikMod</i> is a <i>very</i> portable module player based on libmikmod, written originally by Jean-Paul Mikkers (MikMak). It will play the IT, XM, MOD, MTM, S3M, STM, ULT, FAR, MED, DSM, AMF, IMF and 669 module formats. It works under AIX, FreeBSD, HP-UX, IRIX, Linux, NetBSD, OpenBSD, OSF/1, SunOS, Solaris, OS/2, DOS, and Windows. It is controllable via an easy-to-use curses interface and will extract and play modules from a variety of different archive formats. </p>
<h2>OPTIONS</h2>
<p> Options can be given in any order, and are case-sensitive. For the options which have both a short and a long form, the long form can be prefixed by one or two dashes. Note that the settings in your $HOME/.mikmodrc will override the defaults shown in this man page. </p>
<h2>OUTPUT OPTIONS</h2>
<dl>
<dt><code>-d </code><i>n</i></p>
<dd>
<dt><code>&#8211;driver </code><i>n</i></p>
<dd> Use the specified device driver for output, 0 is autodetect. The default is 0. If your installed libmikmod engine is recent enough (&gt;=3.1.7), you can also specify the driver with an alias, as well as driver options separated by commas. The list and driver aliases and recognized options can be found in libmikmod&#8217;s documentation.</p>
<dt><code>-o[utput] </code><i>8m</i>|<i>8s</i>|<i>16m</i>|<i>16s</i></p>
<dd> Output settings, 8 or 16 bit in stereo or mono. The default is &quot;16s&quot;.</p>
<dt><code>-f </code><i>freq</i></p>
<dd>
<dt><code>&#8211;frequency </code><i>freq</i></p>
<dd> Set mixing frequency in hertz. The default is 44100.</p>
<dt><code>-i</code></p>
<dd>
<dt><code>&#8211;interpolate</code></p>
<dd> Use interpolated mixing. This will generally improve audio quality, at the expense of a bit more CPU usage. Note that this option alters the behaviour of software drivers only ; hardware drivers are not affected (default).</p>
<dt><code>&#8211;nointerpolate</code></p>
<dd> Do not use interpolated mixing.</p>
<dt><code>-hq</code></p>
<dd>
<dt><code>&#8211;hqmixer</code></p>
<dd> Use high quality software mixer. This improves audio quality, but requires a lot more CPU power. Note that this option alters the behaviour of software drivers only ; hardware drivers are not affected.</p>
<dt><code>&#8211;nohqmixer</p>
<dd> Do not use high quality software mixer (default).</p>
<dt>-s</code></p>
<dd>
<dt><code>&#8211;surround</code></p>
<dd> Use surround mixing.</p>
<dt><code>&#8211;nosurround</code></p>
<dd> Do not use surround mixing (default).</p>
<dt><code>-r </code><i>n</i></p>
<dd>
<dt><code>&#8211;reverb </code><i>n</i></p>
<dd> Sets reverb amount from 0 (no reverb) to 15 (max reverb). The default is 0 (no reverb). </p>
</dl>
<h2>PLAYBACK OPTIONS</h2>
<dl>
<dt><code>-v </code><i>volume</i></p>
<dd>
<dt><code>&#8211;volume </code><i>volume</i></p>
<dd> Set volume from 0% (silence) to 100%. The default is 100%.</p>
<dt><code>-F</code></p>
<dd>
<dt><code>&#8211;fadeout</code></p>
<dd> Fade out the volume during the last pattern of each module.</p>
<dt><code>&#8211;nofadeout</code></p>
<dd> Do not fade out the volume during the last pattern of each module (default).</p>
<dt><code>-l</code></p>
<dd>
<dt><code>&#8211;loops</code></p>
<dd> Enable in-module backwards loops.</p>
<dt><code>&#8211;noloops</code></p>
<dd> Disable in-module backwards loops (default).</p>
<dt><code>-a</code></p>
<dd>
<dt><code>&#8211;panning</code></p>
<dd> Process panning effects (default). This should be disabled (using &#8211;nopanning) for very old demo modules which use the panning effects for synchronization purposes.</p>
<dt><code>&#8211;nopanning</code></p>
<dd> Do not process panning effects.</p>
<dt><code>-x</code></p>
<dd>
<dt><code>&#8211;protracker</code></p>
<dd> Enable protracker extended speed effect (default). This should be disabled (using &#8211;noprotracker) for very old demo modules which use the extended speed effect for synchronization purposes.</p>
<dt><code>&#8211;noprotracker</code></p>
<dd> Disable protracker extended speed effect. </p>
</dl>
<h2>LOADING OPTIONS</h2>
<dl>
<dt><code>-y </code><i>dir</i></p>
<dd>
<dt><code>&#8211;directory </code><i>dir</i></p>
<dd> Scan directory recursively for modules.</p>
<dt><code>-c</code></p>
<dd>
<dt><code>&#8211;curious</code></p>
<dd> Look for hidden patterns in module. Most modules don&#8217;t have hidden patterns, but you can find &quot;bonus&quot; patterns (or just silence) in some modules.</p>
<dt><code>&#8211;nocurious</code></p>
<dd> Do not look for hidden patterns in module (default).</p>
<dt><code>-p </code><i>n</i></p>
<dd>
<dt><code>&#8211;playmode </code><i>n</i></p>
<dd> Playlist mode. The allowed values here are 1, to loop the current module; 2, to play the whole playlist repeatedly; 4, to shuffle the list before playing, and 8, to play the whole list randomly. The default is 2.</p>
<dt><code>-t</code></p>
<dd>
<dt><code>&#8211;tolerant</code></p>
<dd> Don&#8217;t halt MikMod if a module cannot be read or is an unknown format (default).</p>
<dt><code>&#8211;notolerant</code></p>
<dd> Halt MikMod if a module cannot be read or is an unknown format. </p>
</dl>
<h2>SCHEDULING OPTIONS</h2>
<p> The following options need root privileges (or a setuid root binary), and don&#8217;t work under all systems.</p>
<dl>
<dt><code>-s</code></p>
<dd>
<dt><code>&#8211;renice</code></p>
<dd> Renice to -20 if possible to gain more CPU priority. This option is only available under FreeBSD, Linux, NetBSD, OpenBSD and OS/2.</p>
<dt><code>&#8211;norenice</code></p>
<dd> Do not renice to -20 (default).</p>
<dt><code>-S</code></p>
<dd>
<dt><code>&#8211;realtime</code></p>
<dd> Reschedule mikmod to gain real-time priority (and thus more CPU time). <code>DANGEROUS! USE WITH CAUTION!</code> This option is only available under FreeBSD, Linux and OS/2.</p>
<dt><code>&#8211;norealtime</code></p>
<dd> Do not reschedule MikMod to gain real-time priority (default). </p>
</dl>
<h2>DISPLAY OPTIONS</h2>
<dl>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd> Quiet mode. Disables interactive commands and displays only errors. </p>
</dl>
<h2>INFORMATION OPTIONS</h2>
<dl>
<dt><code>-n</code></p>
<dd>
<dt><code>&#8211;information</code></p>
<dd> Display the list of the known drivers and module loaders.</p>
<dt><code>-N </code><i>n</i></p>
<dd>
<dt><code>&#8211;drvinfo </code><i>n</i></p>
<dd> Display information about a specific driver.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display MikMod version.</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd> Display a summary of the options. </p>
</dl>
<h2>CONFIGURATION OPTION</h2>
<dl>
<dt><code>&#8211;norc</code></p>
<dd> Do not parse the $HOME/.mikmodrc configuration file. This file contains your default settings, so that you don&#8217;t have to specify them each time you run MikMod. The file is read when you run MikMod and updated on exit. Using this option prevents MikMod from accessing this file. </p>
</dl>
<h2>RUNTIME COMMANDS</h2>
<p> At play time, the following keystrokes offer control over MikMod:</p>
<dl>
<dt><code>H</code>, <code>function key F1</code></p>
<dd> Display help panel.</p>
<dt><code>S</code>, <code>function key F2</code></p>
<dd> Display samples panel.</p>
<dt><code>I</code>, <code>function key F3</code></p>
<dd> Display instruments panel (if present in the module).</p>
<dt><code>M</code>, <code>function key F4</code></p>
<dd> Display song message panel (if present in the module).</p>
<dt><code>L</code>, <code>function key F5</code></p>
<dd> Display the playlist panel.</p>
<dt><code>C</code>, <code>function key F6</code></p>
<dd> Display the configuration panel.</p>
<dt><code>V</code>, <code>function key F7</code></p>
<dd> Display the volume panel.</p>
<dt><code>digits</code></p>
<dd> Set volume from 10% (digit 1) to 100% (digit 0).</p>
<dt><code>&lt;</code></p>
<dd> Decrease volume.</p>
<dt><code>&gt;</code></p>
<dd> Increase volume.</p>
<dt><code>&#8211;</code>, <code>Left</code></p>
<dd> Restart current pattern / skip to previous pattern.</p>
<dt><code>+</code>, <code>Right</code></p>
<dd> Skip to next pattern in current module.</p>
<dt><code>Up</code>, <code>Down</code></p>
<dd> Scroll panel.</p>
<dt><code>PgUp</code>, <code>PgDown</code></p>
<dd> Scroll panel (faster).</p>
<dt><code>Home</code></p>
<dd> Go on top of the panel.</p>
<dt><code>End</code></p>
<dd> Go to the end of the panel.</p>
<dt><code>(</code></p>
<dd> Decrease speed variable (module plays faster).</p>
<dt><code>)</code></p>
<dd> Increase speed variable (module plays slower).</p>
<dt><code>{</code></p>
<dd> Decrease tempo variable (module plays slower).</p>
<dt><code>}</code></p>
<dd> Increase tempo variable (module plays faster).</p>
<dt><code>:</code> or <code>;</code></p>
<dd> Toggle interpolation mixing.</p>
<dt><code>U</code></p>
<dd> Toggle surround mixing.</p>
<dt><code>Q</code></p>
<dd> Exit MikMod.</p>
<dt><code>P</code></p>
<dd> Switch to previous module in playlist.</p>
<dt><code>N</code></p>
<dd> Switch to next module in playlist.</p>
<dt><code>R</code></p>
<dd> Restart current module.</p>
<dt><code>F</code></p>
<dd> Toggle fake/real volume bars in volume panel.</p>
<dt><code>space</code></p>
<dd> Toggle pause.</p>
<dt><code>Control-L</code></p>
<dd> Refresh the screen. </p>
</dl>
<h2>MENU BASICS</h2>
<p> Some functions of MikMod are available through menus, in the playlist and configuration panels. </p>
<p> You can select commands in the menus either by moving the selection with the arrow keys and pressing enter, or entering the highlighted letter corresponding ot the command you want to select. </p>
<p> Menu entries ending with a <code>&gt;</code> character open a submenu, whereas entries ending in <code>&#8230;</code> open a dialog box. You can dismiss a submenu either by choosing a command in this menu, or using the left arrow key to go back, or switching panels. </p>
<p> In dialog boxes, you can move the focus from the input line to the <code>Ok</code> and <code>Cancel</code> buttons either with the &quot;tab&quot; key, or the up and down arrow keys. </p>
<p> Also, if the statusbar is active (which is the default behaviour), it will contain a short help text describing the menu option currently highlighted. </p>
<h2>PLAYLIST MENU</h2>
<p> When the playlist panel is displayed, pressing the <i>return</i> key will popup a menu. The menu commands are: </p>
<dl>
<dt><code>Play</code></p>
<dd> Continue list playback from the currently highlighted module.</p>
<dt><code>Remove</code></p>
<dd> Remove module from the playlist.</p>
<dt><code>Delete&#8230;</code></p>
<dd> Remove module from the playlist, and delete module file on disk, or whole archive if the module is stored in an archive file. This function asks you to confirm your choice.</p>
<dt><code>File &gt;</code></p>
<dd> This entry opens a submenu with four commands, &quot;<code>Load</code>&quot;, &quot;<code>Insert</code>&quot;, &quot;<code>Save</code>&quot; and &quot;<code>Save as</code>&quot;. The <code>Load</code> and <code>Insert</code> commands ask you for a filename, and replace the playlist with it (load) or merge it with the playlist (insert). No wildcards are allowed. The <code>Save</code> and <code>Save as</code> commands save the current playlist in a file, by default &#8220;playlist.mpl&#8221;, in the current directory. Note that playlist filenames should end in <code>.mpl</code>, or they won&#8217;t be recognized immediately as a playlist by MikMod.</p>
<dt><code>Shuffle</code></p>
<dd> Randomize the playlist.</p>
<dt><code>Sort &gt;</code></p>
<dd> This entry opens a submenu with sort commands. You can select a normal or <code>reverse</code> order, and then sort the playlist with one of the four criteria: <code>by name</code>, <code>by extension</code>, <code>by path</code> or <code>by time</code>.</p>
<dt><code>Back</code></p>
<dd> Discards the menu. </p>
</dl>
<h2>CONFIGURATION PANEL</h2>
<p> The configuration panel lets you customize your MikMod settings, and save them. You can also try some particular settings without losing your previous configuration. </p>
<dl>
<dt><code>Output options</code></p>
<dd> This section lets you choose various vital playback settings, such as the output driver, the stereo/mono and 16/8 bit output settings, the playback frequency, and the software mixer settings.</p>
<dt><code>Playback options</code></p>
<dd> This section lets you choose various module playback settings, such as the output volume, the processing of panning effects and bacwards loops, etc.</p>
<dt><code>Other options</code></p>
<dd> This section lets you choose the remaining settings, such as the playlist mode, and various program settings. </p>
<dt><code>Use config</code></p>
<dd> This command activates the current configuration settings, but does not save them.</p>
<dt><code>Save config</code></p>
<dd> This command saves and activates the current configuration settings.</p>
<dt><code>Revert config</code></p>
<dd> This command reverts to the on-disk configuration file settings. </p>
</dl>
<h2>MODULE FORMATS</h2>
<p> MikMod will currently play the following common and not so common formats:</p>
<dl>
<dt><code>669</code></p>
<dd> Composer 669 and Extended 669 modules.</p>
<dt><code>AMF</code></p>
<dd> DSMI internal module format (Advanced Module Format, converted with M2AMF).</p>
<dt><code>AMF</code></p>
<dd> ASYLUM Music format (From crusader games)</p>
<dt><code>DSM</code></p>
<dd> DSIK&#8217;s internal module format.</p>
<dt><code>FAR</code></p>
<dd> Farandole composer modules.</p>
<dt><code>GDM</code></p>
<dd> General Digital Munsic internal module format (converted with 2GDM).</p>
<dt><code>IMF</code></p>
<dd> Imago Orpheus modules.</p>
<dt><code>IT</code></p>
<dd> Impulse Tracker modules.</p>
<dt><code>MED</code></p>
<dd> Amiga MED modules, but synthsounds are not supported.</p>
<dt><code>MOD</code></p>
<dd> Protracker, Startracker, Fasttracker, Oktalyzer, and Taketracker modules.</p>
<dt><code>MTM</code></p>
<dd> Multitracker module editor modules.</p>
<dt><code>S3M</code></p>
<dd> Screamtracker version 3 modules.</p>
<dt><code>STM</code></p>
<dd> Screamtracker version 2 modules.</p>
<dt><code>STX</code></p>
<dd> STMIK converted modules.</p>
<dt><code>ULT</code></p>
<dd> Ultratracker modules.</p>
<dt><code>UNI</code>, <code>APUN</code></p>
<dd> Old MikMod (UNI) and APlayer (APUN) internal module format.</p>
<dt><code>XM</code></p>
<dd> Fasttracker 2 modules. </p>
</dl>
<h2>ARCHIVE FORMATS</h2>
<p> MikMod should recognize and extract the following common archive formats. However, to use each of these you will need to find the appropriate program(s) for MikMod to use to extract them. These are commonly available and you will most likely find them with this distribution of MikMod. Other archive formats can be configured by editing the configuration file (see <code>FILES</code> below). </p>
<dl>
<dt><code>zip</code></p>
<dd> Info-zip or PkZip archives, commonly used on DOS/Windows platforms.</p>
<dt><code>lha</code>, <code>lzh</code></p>
<dd> Lharc archives, commonly used on the Amiga.</p>
<dt><code>zoo</code></p>
<dd> Zoo archives, quite rare those days&#8230;</p>
<dt><code>rar</code></p>
<dd> Rar archives.</p>
<dt><code>gz</code></p>
<dd> Gzip compressed files.</p>
<dt><code>bz2</code></p>
<dd> Bzip2 compressed files.</p>
<dt><code>tar</code>, <code>tar.gz</code> and <code>tar.bz2</code></p>
<dd> Tar archives, even compressed with gzip or bzip2. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt>$HOME/.mikmodrc (or mikmod.cfg under OS/2 / Windows)</p>
<dd> User configuration settings.</p>
<dt>$HOME/.mikmod_playlist (mikmodpl.cfg/mikmod_playlist.mpl under OS/2 / Windows)</p>
<dd> The default playlist, loaded if no other files are specified on the command line.</p>
<dt>playlist.mpl</p>
<dd> Default playlist filename. </p>
</dl>
<h2>AUTHORS</h2>
<p> <i>MikMod</i> is the result of the work of many people, including: Jean-Paul Mikkers, Jake Stine, Miodrag Vallat, Frank Loemker, Andrew Zabolotny, Raphael Assenat, Steve McIntyre, Peter Amstutz, &quot;MenTaLguY&quot;, Dimitri Boldyrev, Shlomi Fish, Stefan Tibus, Tinic Urou. A full list of people having worked on libmikmod and MikMod is displayed when MikMod starts. </p>
<h2>LOCATING NEWER VERSIONS&#8230;</h2>
<p> The official MikMod and libmikmod home page is located on<br />
&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://mikmod.raphnet.net">http://mikmod.raphnet.net</a> </p>
<h2>Index</h2>
