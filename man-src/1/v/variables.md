---
title: "variables(1)"
name: "variables"
section: "1"
letter: "v"
url: "/docs/linux/man/1-variables/"
---

<h2>GRASS variables and environment variables</h2>
<p> There are two types of variables:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> shell environment variables,</p>
<dt>
<dd> GRASS gisenv variables.</dl>
</dl>
<p> There are a number of shell environment variable groups:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> PNG driver</p>
<dt>
<dd> PS driver (PostScript)</p>
<dt>
<dd> variables for direct rendering</p>
<dt>
<dd> variables for internal use</dl>
</dl>
<p> Any setting which needs to be modifiable by a GRASS program (e.g. MONITOR) has to be a GRASS <i>gisenv</i> variable.</p>
<h2>GRASS-related Files</h2>
<p> GRASS maintains some settings in a number of files on the system. They are detailed below.</p>
<h2>Setting environment variables</h2>
<p> Setting environment variables depends on the shell being used: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Bash:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>export VARIABLE=value </p>
<p>or </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Csh:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>setenv VARIABLE value </p>
<p>or </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Cmd.exe&nbsp;<wbr>(Windows): set VARIABLE=value</p>
<h2>Setting environment variables permanently</h2>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> To get personal BASH shell definitions (aliases, color listing option, &#8230;) into GRASS, store them in:<br />
 $HOME/.grass.bashrc</p>
<dt>
<dd> To get personal CSH shell definitions (aliases, color listing option, &#8230;) into GRASS, store them in:<br />
 $HOME/.grass.cshrc</dl>
</dl>
<h2>Setting GRASS variables</h2>
<p> Use &quot;g.gisenv&quot; within GRASS. This permanently predefines GRASS variables in the .grassrc6 file. </p>
<p> Usage: </p>
<p> g.gisenv set=&quot;VARIABLE=VALUE&quot; </p>
<p> It looks unusual with two equals signs, but g.gisenv serves dual duty for getting and setting GRASS variables. </p>
<p> If the user just specifies a variable name, it defaults to &quot;get&quot; mode. For example: </p>
<p> GRASS ~&gt; g.gisenv GRASS_GUI<br />
 text </p>
<h2>List of selected (GRASS related) environment variables</h2>
<p> [ To be set from the terminal shell or startup scripts ] </p>
<p> GISBASE </p>
<p>&nbsp;<wbr>&nbsp;<wbr>directory where GRASS lives. This is set automatically by the startup script. </p>
<p> GISRC </p>
<p>&nbsp;<wbr>&nbsp;<wbr>name of .grassrc6 file. GISRCRC defines the system wide value while in a GRASS session. </p>
<p> GRASS_ADDON_PATH<br />
 [grass startup script] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>allows to specify additional paths to local GRASS modules extra to standard distribution. </p>
<p> GRASS_ADDON_ETC<br />
 [libgis, g.findetc] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>specify paths where support files&nbsp;<wbr>(etc/)&nbsp;<wbr>may be found external to standard distribution. </p>
<p> GRASS_BATCH_JOB </p>
<p>&nbsp;<wbr>&nbsp;<wbr>defines the name&nbsp;<wbr>(path)&nbsp;<wbr>of a shell script to be processed as batch job. </p>
<p> GRASS_ERROR_MAIL </p>
<p>&nbsp;<wbr>&nbsp;<wbr>set to any value to send user mail on an error or warning that&nbsp;<wbr> happens while stderr is being redirected. </p>
<p> GRASS_GNUPLOT<br />
 [i.spectral] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>program to use for plotting&nbsp;<wbr>&quot;gnuplot&quot;&nbsp;<wbr>data </p>
<p> GRASS_GUI </p>
<p>&nbsp;<wbr>&nbsp;<wbr>either&nbsp;<wbr>&quot;text&quot;&nbsp;<wbr>or&nbsp;<wbr>&quot;tcltk&quot;&nbsp;<wbr>to define non-/graphical startup. Can also specify the name of the GUI to use, e.g. &quot;gis.m&quot;, &quot;d.m&quot; or dqwxpython&quot; (<i>wx name subject to change</i>). Also exists as a GRASS gisenv variable (see below). If this shell variable exists at GRASS startup, it will determine the GUI used. If it is not defined startup will default to the last GUI used. </p>
<p> GRASS_FONT_CAP<br />
 [g.mkfontcap, d.font, display drivers] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Specifies an alternative location&nbsp;<wbr>(to&nbsp;<wbr>$GISBASE/etc/fontcap)&nbsp;<wbr>for&nbsp;<wbr> the font configuration file. </p>
<p> GRASS_HEIGHT<br />
 [d.mon] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>defines the height of GRASS monitor, see also GRASS_WIDTH </p>
<p> GRASS_HTML_BROWSER<br />
 [init.sh, d.m, gis.m] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>defines name of HTML browser.&nbsp;<wbr>&nbsp;<wbr>For most platforms this should be an executable in your PATH, or the full path to an executable.<br />
 Mac OS X runs applications differently from the CLI. Therefore, GRASS_HTML_BROWSER should be the application&#8217;s signature, which is a domain-like name, just reversed. ie: com.apple.Safari. To find an application&#8217;s signature, type the following in a Terminal (fill in the path to the application you are interested in, for example: /Applications/Safari.app):<br />
 <i>grep -A 1 &quot;CFBundleIdentifier&quot;</i> <i>/path/to/application.app</i><i>/Contents/Info.plist</i><br />
 The signature is the following the , without the bracketing tags. </p>
<p> GRASS_INT_ZLIB<br />
 [libgis] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>If the environment variable GRASS_INT_ZLIB exists, new compressed rasters will be compressed using zlib instead of RLE compression. Such rasters will have a &quot;compressed&quot; value of 2 in the cellhd file.<br />
 Obviously, decompression is controlled by the raster&#8217;s &quot;compressed&quot; value, not the environment variable. </p>
<p> GRASS_MESSAGE_FORMAT<br />
 [various modules]<br />
 Maybe set to either &quot;standard&quot; or &quot;gui&quot; (normally GRASS takes care) </p>
<p> GRASS_MOUSE_BUTTON<br />
 [various modules] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>swaps mouse buttons for two-button or left-handed mice. Its value has three digits 1, 2, and 3, which represent default left, middle, and right buttons respectively. Setting to &quot;132&quot; will swap middle and right buttons. Note that this variable should be set before a display driver is initialized (e.g., d.mon x0). </p>
<p> GRASS_PAGER<br />
 [various modules]<br />
 Maybe set to either &quot;less&quot; or &quot;more&quot; </p>
<p> GRASS_PERL<br />
 [Used during install process for generating man pages] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>set perl with path </p>
<p> GRASS_RND_SEED </p>
<p>&nbsp;<wbr>&nbsp;<wbr>set random seed for r.mapcalc rand()&nbsp;<wbr>function </p>
<p> GRASS_SH<br />
 [shell scripts on Windows]<br />
 Path to bourne shell interpreter used to run shell scripts </p>
<p> GRASS_TCLSH<br />
 [nviz] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>set tclsh shell name to override&nbsp;<wbr>&#8216;tclsh&#8217; </p>
<p> GRASS_XTERM<br />
 lib/init/grass-xterm-wrapper<br />
 lib/init/grass-xterm-mac </p>
<p>&nbsp;<wbr>&nbsp;<wbr>set to any value&nbsp;<wbr>(e.g. rxvt, aterm, gnome-terminal, konsole)&nbsp;<wbr>to substitute &#8216;x-terminal-emulator&#8217; or &#8216;xterm&#8217;. The Mac OS X app startup defaults to an internal &#8216;$GISBASE/etc/grass-xterm-mac&#8217;, which emulates the necessary xterm functionality in Terminal.app. </p>
<p> GRASS_UI_TERM </p>
<p>&nbsp;<wbr>&nbsp;<wbr>set to any value to use the terminal based parser </p>
<p> GRASS_VERSION </p>
<p>&nbsp;<wbr>&nbsp;<wbr>reports the current version number&nbsp;<wbr>(used by R-stats interface etc); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>should not be changed by user </p>
<p> GRASS_WIDTH<br />
 [d.mon] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>defines the width of GRASS monitor, see also GRASS_HEIGHT </p>
<p> GRASS_WISH<br />
 [d.m, nviz] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>set wish shell name to override&nbsp;<wbr>&#8216;wish&#8217; </p>
<p> GRASS_NO_GLX_PBUFFERS<br />
 [nviz] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>set to any value to disable the use of Pbuffers </p>
<p> GRASS_NO_GLX_PIXMAPS<br />
 [nviz] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>set to any value to disable the use of GLX Pixmaps</p>
<h3>List of selected GRASS PNG driver environment variables</h3>
<p> [ These variables control the function of the PNG Driver. ] </p>
<p> GRASS_PNGFILE </p>
<p>&nbsp;<wbr>&nbsp;<wbr>name of PNG output file. If it ends with&nbsp;<wbr>&quot;.ppm&quot;&nbsp;<wbr>a PPM file will be created. </p>
<p> GRASS_WIDTH </p>
<p>&nbsp;<wbr>&nbsp;<wbr>defines the width of GRASS monitor, see also GRASS_HEIGHT </p>
<p> GRASS_HEIGHT </p>
<p>&nbsp;<wbr>&nbsp;<wbr>defines the height of GRASS monitor, see also GRASS_WIDTH </p>
<p> GRASS_BACKGROUNDCOLOR </p>
<p>&nbsp;<wbr>&nbsp;<wbr>defines the background color of the image created by the PNG driver </p>
<p> GRASS_TRANSPARENT </p>
<p>&nbsp;<wbr>&nbsp;<wbr>if&nbsp;<wbr>&quot;TRUE&quot;, the image created by the PNG driver will have a transparent background </p>
<p> GRASS_PNG_COMPRESSION </p>
<p>&nbsp;<wbr>&nbsp;<wbr>compression level of PNG files&nbsp;<wbr>(0&nbsp;<wbr>=&nbsp;<wbr>none, 1&nbsp;<wbr>=&nbsp;<wbr>fastest, 9&nbsp;<wbr>=&nbsp;<wbr>best) </p>
<p> GRASS_TRUECOLOR </p>
<p>&nbsp;<wbr>&nbsp;<wbr>if&nbsp;<wbr>&quot;TRUE&quot;, the PNG driver generates a true-color image </p>
<p> GRASS_PNG_AUTO_WRITE </p>
<p>&nbsp;<wbr>&nbsp;<wbr>tells the PNG driver to write the image to a file whenever a client disconnects, rather than waiting until you stop the monitor </p>
<p> GRASS_PNG_READ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>if&nbsp;<wbr>&quot;TRUE&quot;, the PNG driver will initialize the image from the contents of $GRASS_PNGFILE </p>
<p> GRASS_PNG_MAPPED </p>
<p>&nbsp;<wbr>&nbsp;<wbr>if&nbsp;<wbr>&quot;TRUE&quot;, the PNG driver will map&nbsp;<wbr>$GRASS_PNGFILE as its framebuffer, rather than using memory; this only works with BMP files</p>
<h3>List of selected GRASS PS driver environment variables</h3>
<p> [ These variables control the function of the PS Driver. ] </p>
<p> GRASS_PSFILE </p>
<p>&nbsp;<wbr>&nbsp;<wbr>name of output file. If it ends with&nbsp;<wbr>&quot;.eps&quot;&nbsp;<wbr>an EPS file will be created. </p>
<p> GRASS_PAPER </p>
<p>&nbsp;<wbr>&nbsp;<wbr>sets the screen dimensions and margins to fit a standard paper size, see also GRASS_WIDTH, GRASS_HEIGHT. </p>
<p> GRASS_WIDTH </p>
<p>&nbsp;<wbr>&nbsp;<wbr>defines the width of the screen, see also GRASS_HEIGHT </p>
<p> GRASS_HEIGHT </p>
<p>&nbsp;<wbr>&nbsp;<wbr>defines the height of the screen, see also GRASS_WIDTH </p>
<p> GRASS_TRUECOLOR </p>
<p>&nbsp;<wbr>&nbsp;<wbr>if&nbsp;<wbr>&quot;TRUE&quot;, the PS driver generates color output, otherwise monochrome. </p>
<p> GRASS_LANDSCAPE </p>
<p>&nbsp;<wbr>&nbsp;<wbr>if&nbsp;<wbr>&quot;TRUE&quot;, the screen is rotated 90 degrees counter-clockwise so that a &quot;landscape&quot; screen fits better on dqportrait&quot; paper. </p>
<p> GRASS_PS_HEADER </p>
<p>&nbsp;<wbr>&nbsp;<wbr>if&nbsp;<wbr>&quot;FALSE&quot;, the output is appended to any existing file, and no prolog or setup sections are generated. </p>
<p> GRASS_PS_TRAILER </p>
<p>&nbsp;<wbr>&nbsp;<wbr>if&nbsp;<wbr>&quot;FALSE&quot;, no trailer section is generated.</p>
<h3>List of selected GRASS environment variables for direct rendering</h3>
<p> [ In addition to those which are understood by the PNG Driver, the following variables affect direct rendering. ] </p>
<p> GRASS_RENDER_IMMEDIATE </p>
<p>&nbsp;<wbr>&nbsp;<wbr>tells the raster library to use its built-in PNG/PS driver rather than connecting to an external monitor process using sockets. If GRASS_RENDER_IMMEDIATE=TRUE is set, there is no need to run dqd.mon start=PNG&quot; </p>
<p> GRASS_FONT </p>
<p>&nbsp;<wbr>&nbsp;<wbr>specifies the font as either the name of a font from $GISBASE/etc/fontcap (or alternative fontcap file specifed by GRASS_FONT_CAP), or alternatively the full path to a FreeType font file. </p>
<p> GRASS_ENCODING </p>
<p>&nbsp;<wbr>&nbsp;<wbr>the encoding to be assumed for text which is drawn using a freetype font; may be any encoding know to &quot;iconv&quot;.</p>
<h3>List of selected internal GRASS environment variables</h3>
<p> [ These variables are intended <code>for internal use only</code> by the GRASS software to facilitate communiction between the GIS engine, GRASS scripts, and the GUI. The user should not set these in a GRASS session. They are meant to be set locally for specific commands. ] </p>
<p> GRASS_OVERWRITE<br />
 [all modules] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>toggles map overwrite.</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
&nbsp;<wbr>0 &#8211; maps are protected&nbsp;<wbr>(default),</p>
<dt>
<dd>
&nbsp;<wbr>1 &#8211; maps with identical names will be overwritten.</dl>
</dl>
<p> This variable is automatically created by g.parser so that the dq&#8211;overwrite&quot; option will be inherited by dependant modules as the script runs. Setting either the GRASS_OVERWRITE environment variable or the OVERWRITE gisenv variable detailed below will cause maps with identical names to be overwritten. </p>
<p> GRASS_VERBOSE<br />
 [all modules] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>toggles verbosity level</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
&nbsp;<wbr>0 &#8211; only errors and warnings are printed</p>
<dt>
<dd>
&nbsp;<wbr>1 &#8211; progress messages are printed&nbsp;<wbr>(percent complete)</p>
<dt>
<dd>
&nbsp;<wbr>2 &#8211; all module messages are printed</p>
<dt>
<dd>
&nbsp;<wbr>3 &#8211; additional verbose messages are printed</dl>
</dl>
<p> This variable is automatically created by <i>g.parser</i> so that the &quot;&#8211;verbose&quot; or &quot;&#8211;quiet&quot; flags will be inherited by dependant modules as the script runs. </p>
<p> GRASS_REGION<br />
 [libgis] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Override region settings, separate parameters with a&nbsp;<wbr>&quot;;&quot;. Format is the same as in the WIND region settings file. Otherwise use is the same as WIND_OVERRIDE. </p>
<p> WIND_OVERRIDE<br />
 [libgis] </p>
<p>&nbsp;<wbr>&nbsp;<wbr> It causes programs to use the specified named region (created with e.g. &quot;g.region save=&#8230;&quot;) to be used as the current region, instead of the region from the WIND file.<br />
 This allows programs such as gis.m to run external commands on an alternate region without having to modify the WIND file then change it back afterwards. </p>
<h2>List of selected GRASS gisenv variables</h2>
<p> [ Use g.gisenv to get/set/unset/change them ] </p>
<p> DEBUG<br />
 [entire GRASS] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>sets level of debug message output&nbsp;<wbr>(0: no debug messages)<br />
 g.gisenv set=DEBUG=0 </p>
<p> DM_FORM_MODE<br />
 [d.m] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>sets default form mode&nbsp;<wbr>(txt or gui)<br />
 g.gisenv set=DM_FORM_MODE=txt </p>
<p> GISDBASE </p>
<p>&nbsp;<wbr>&nbsp;<wbr>initial database </p>
<p> GIS_LOCK </p>
<p>&nbsp;<wbr>&nbsp;<wbr>lock ID to prevent parallel GRASS use, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>process id of the start-up shell script </p>
<p> GRASS_DB_ENCODING<br />
 [d.what.vect/forms library] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>encoding of query form&nbsp;<wbr>(utf-8, ascii, iso8859-1, koi8-r) </p>
<p> GRASS_GUI </p>
<p>&nbsp;<wbr>&nbsp;<wbr>either&nbsp;<wbr>&quot;text&quot;&nbsp;<wbr>or&nbsp;<wbr>&quot;tcltk&quot;&nbsp;<wbr>to define non-/graphical startup. Can also specify the name of the GUI to use, e.g. &quot;gis.m&quot;, &quot;d.m&quot; or dqwxpython&quot; (<i>wx name subject to change</i>). Can also exist as a GRASS startup shell variable. The gisenv setting defines what GUI GRASS will use the next time it starts. </p>
<p> LOCATION </p>
<p>&nbsp;<wbr>full path to location directory </p>
<p> LOCATION_NAME </p>
<p>&nbsp;<wbr>initial location name </p>
<p> MAPSET </p>
<p>&nbsp;<wbr>&nbsp;<wbr>initial mapset </p>
<p> OVERWRITE<br />
 [all modules] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>toggles map overwrite. </p>
<p>&nbsp;<wbr>With 0 maps are protected&nbsp;<wbr>(default),&nbsp;<wbr> </p>
<p>&nbsp;<wbr>With 1 maps with identical names will be overwritten. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Example: g.gisenv set=&quot;OVERWRITE=0&quot; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>You can force an overwrite for an individual command by adding&nbsp;<wbr>&quot;&#8211;o&quot;&nbsp;<wbr>to the command:&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>r.in.gdal &#8211;o output=existing_map &#8230; </p>
<h2>GRASS-related Files</h2>
<p> $HOME/.grassrc6 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>stores the GRASS variables&nbsp;<wbr>(but not environment variables) </p>
<p> $HOME/.grasslogin6 </p>
<p>stores the DBMI passwords in this hidden file Only the file owner can access this file. </p>
<p> $HOME/GIS_ERROR_LOG </p>
<p>&nbsp;<wbr>&nbsp;<wbr>If this file exists then all GRASS error and warning messages are&nbsp;<wbr> logged here. Applies to current user. To generate the file, use: </p>
<p>touch&nbsp;<wbr>$HOME/GIS_ERROR_LOG </p>
<p> $GISBASE/GIS_ERROR_LOG </p>
<p>&nbsp;<wbr>&nbsp;<wbr>If this file exists then all GRASS error and warning messages are&nbsp;<wbr> logged here. Applies to all users. (proper write permissions must be in place) </p>
<p> <i>Note:</i> Error and warning messages encountered while using the GUI menus are not logged.</p>
<h3>SEE ALSO</h3>
<p> <i> g.gisenv, g.parser </i> </p>
<p> <i>Last changed: $Date: 2008-04-15 19:10:05 +0200 (Tue, 15 Apr 2008) $</i> </p>
<p> Help Index </p>
<h2>Index</h2>
