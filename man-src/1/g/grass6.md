---
title: "grass6(1)"
name: "grass6"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grass6/"
description: "grass63 – The GRASS startup program"
---

<h2>NAME</h2>
<p> <i></i><code>grass63</code> &#8211; The GRASS startup program </p>
<h2>SYNOPSIS</h2>
<p> <code>grass63</code> [<code>&#8211;</code>] [<code>-v</code>] [<code>-h | -help | &#8211;help</code>] [<code>-text | -gui | -oldgui]</code>] [[[<code>/</code>]<code>/</code>] ] </p>
<h2>DESCRIPTION</h2>
<p> This program is used to start GRASS. It will parse the command line arguments and then initialize GRASS for the user. Since GRASS programs require a specific environment, this program must be called before any other GRASS program can run. The command line arguments are optional and provide the user with a method to indicate the desired user interface, as well as the desired mapset to work on.</p>
<h2>FEATURES</h2>
<p> The GRASS program will save both the desired user interface and mapset. Thus, the next time the user runs GRASS, typing <i>grass63</i> (without any options) will start grass with the previous settings for the user interface and mapset. </p>
<p> If you specify a graphical user interface (eg Tcl/Tk) the <i>grass63</i> program will try to verify that the system you specified exists and that you can access it successfully. If any of these checks fail, then <i>grass63</i> will automatically switch back to the text user interface mode.</p>
<h2>OPTIONS</h2>
<p> All command line options are optional.</p>
<h3>Flags:</h3>
<dl>
<dt><code>&#8211;</code></p>
<dd>
<p>&nbsp;<wbr>Tries to start GRASS using location environment variables&nbsp;<wbr>(see below)</p>
<dt><code>-h -help &#8211;help</code></p>
<dd>
<p>&nbsp;<wbr>Prints a brief usage message</p>
<dt><code>-text</code></p>
<dd>
<p>&nbsp;<wbr>Indicates that the text based user interface should be used</p>
<dt><code>-gui</code> (or <code>-tcltk</code>)</p>
<dd>
<p>&nbsp;<wbr>Indicates that the Tcl/Tk based graphical user interface should be used</p>
<dt><code>-oldgui</code></p>
<dd>
<p>&nbsp;<wbr>Indicates that the old graphical user interface should be used&nbsp;<wbr>(d.m)</p>
<dt><code>-v &#8211;version</code></p>
<dd>
<p>&nbsp;<wbr>Prints the version for GRASS</dl>
<h3>Parameters:</h3>
<dl>
<dt><code>GISDBASE</code></p>
<dd>
<p>&nbsp;<wbr>Initial database directory which should be a fully qualified path (eg /usr/local/share/grassdata)</p>
<dt><code>LOCATION_NAME</code></p>
<dd>
<p>&nbsp;<wbr>Initial location directory which is a subdirectory of GISDBASE</p>
<dt><code>MAPSET</code></p>
<dd>
<p>&nbsp;<wbr>Initial mapset directory which is a subdirectory of LOCATION_NAME</p>
<dt><code>Note</code></p>
<dd>
<p>&nbsp;<wbr>You must specify one of the following<br />
 MAPSET<br />
 LOCATION_NAME/MAPSET<br />
 GISDBASE/LOCATION_NAME/MAPSET
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<h3>User Interface Environment Variable</h3>
<p> The <i>grass63</i> program will check for the existence of an environment variable called GRASS_GUI which indicates the type of user interface for GRASS to use. If this variable is not set when <i>grass63</i> is run, then it will be created and then saved in the $HOME/.grassrc6 file for the next time GRASS is run. In addition to &quot;text&quot; or &quot;tcltk&quot;, the GRASS_GUI variable can be set to the name of the GUI to use, for example &quot;gis.m&quot; or &quot;d.m&quot;. </p>
<p> There is an order of precedence in the way <i>grass63</i> determines the user interface to use. The following is the hierarchy from highest precedence to lowest. </p>
<p> The user may add own environment variable settings to $HOME/.grassrc6 file which are used during next startup of GRASS (list of implemented environment variables).</p>
<dl>
<dt><code>Interface precedence</code></p>
<dd>
 Command line argument<br />
 Environment variable GRASS_GUI<br />
 Value set in $HOME/.grassrc6<br />
 Default value &#8211; currently gis.m</dl>
<h3>Tcl/Tk Environment Variables</h3>
<p> If you choose to use the Tcl/Tk graphical user interface, then the following environment variables can be used to override your system default tclsh and wish commands. See the section immediately following the variable descriptions for an example.</p>
<dl>
<dt><code>GRASS_TCLSH</code></p>
<dd>
<p>&nbsp;<wbr>Command to use to override tclsh</p>
<dt><code>GRASS_WISH</code></p>
<dd>
<p>&nbsp;<wbr>Command to use to override wish</dl>
<h3>Example Use of GRASS Tcl/Tk Environment Variables</h3>
<p> Suppose your system has Tcl/Tk 8.0 installed and you install your personal version of Tcl/Tk 8.3 binaries installed under $HOME/bin. You can use the above variables to have GRASS use the Tcl/Tk 8.3 binaries instead. </p>
<p> GRASS_TCLSH = $HOME/bin/tclsh8.3<br />
 GRASS_WISH = $HOME/bin/wish8.3</p>
<h3>Addon path to extra local GRASS modules</h3>
<p> This environment variables allows to extend the GRASS paths to locally developed/installed modules which are not distributes through the standard release of GRASS. </p>
<p> GRASS_ADDON_PATH=/usr/mytools<br />
 GRASS_ADDON_PATH=/usr/mytools:/usr/local/othertools </p>
<p> In this example above path(s) would be added to the standard GRASS path environment.</p>
<h3>Location Environment Variables</h3>
<p> The Synopsis and Options sections above describe options that can be used to set the location and mapset that GRASS will use. These values can also be set with environment variables. However, specifying the location and mapset variables on the command line will override these environment variables. The available variables are as follows:</p>
<dl>
<dt><code>LOCATION</code></p>
<dd>
<p>&nbsp;<wbr>A fully qualified path to a mapset&nbsp;<wbr> (eg /usr/local/share/grassdata/spearfish60/PERMANENT). This environment variable overrides the GISDBASE, LOCATION_NAME, and MAPSET variables.</p>
<dt><code>GISDBASE</code></p>
<dd>
<p>&nbsp;<wbr>Initial database directory which should be a fully qualified path (eg /usr/local/share/grassdata)</p>
<dt><code>LOCATION_NAME</code></p>
<dd>
<p>&nbsp;<wbr>Initial location directory which is a subdirectory of GISDBASE</p>
<dt><code>MAPSET</code></p>
<dd>
<p>&nbsp;<wbr>Initial mapset directory which is a subdirectory of LOCATION_NAME</dl>
<p> There are a variety of ways in which these variables can be used to specify the mapset to use. The following are some possible examples.</p>
<dl>
<dt><code>Example 1</code></p>
<dd>
<p>&nbsp;<wbr>The environment variables are defined as follows:<br />
 LOCATION = /usr/local/share/grassdata/spearfish60/PERMANENT<br />
 GISDBASE = /usr/local/share/grassdata<br />
 LOCATION_NAME = spearfish60<br />
 MAPSET = PERMANENT<br />
 Start GRASS with the following command:<br />
 grass63 &#8211;<br />
 GRASS will start with the mapset defined by LOCATION since the LOCATION variable overrides the other variables. </p>
<dt><code>Example 2</code></p>
<dd>
<p>&nbsp;<wbr>The environment variables are defined as follows:<br />
 GISDBASE = /usr/local/share/grassdata<br />
 LOCATION_NAME = spearfish60<br />
 MAPSET = PERMANENT<br />
 Start GRASS with the following command:<br />
 grass63 &#8211;<br />
 GRASS will start with the mapset defined by GISDBASE/LOCATION_NAME/MAPSET. </p>
<dt><code>Example 3</code></p>
<dd>
<p>&nbsp;<wbr>The environment variables are defined as follows:<br />
 LOCATION = /usr/local/share/grassdata/spearfish60/PERMANENT<br />
 GISDBASE = /usr/local/share/grassdata<br />
 LOCATION_NAME = spearfish60<br />
 MAPSET = PERMANENT<br />
 Start GRASS with the following command:<br />
 grass63 /usr/home/grass/data/thailand/forests<br />
 GRASS will start with the mapset /home/grass/data/thailand/forests which overrides the environment variables. </p>
<dt><code>Example 4</code></p>
<dd>
<p>&nbsp;<wbr>The environment variables are defined as follows:<br />
 LOCATION = /usr/local/share/grassdata/spearfish60/PERMANENT<br />
 GISDBASE = /usr/local/share/grassdata<br />
 LOCATION_NAME = spearfish60<br />
 MAPSET = PERMANENT<br />
 Start GRASS with the following command:<br />
 grass63 swamps<br />
 GRASS will start with the mapset defined by GISDBASE/LOCATION_NAME/swamps since the command line argument for the mapset overrides the environment variable MAPSET. </p>
<dt><code>Example 5</code></p>
<dd>
<p>&nbsp;<wbr>The environment variables are defined as follows:<br />
 LOCATION = /usr/local/share/grassdata/spearfish60/PERMANENT<br />
 GISDBASE = /usr/local/share/grassdata<br />
 LOCATION_NAME = spearfish60<br />
 MAPSET = PERMANENT<br />
 Start GRASS with the following command:<br />
 grass63 thailand/forests<br />
 GRASS will start with the mapset defined by GISDBASE/thailand/forests since the command line arguments for the location and mapset overrides the environment variables LOCATION_NAME and MAPSET.
</dl>
<h3>Note</h3>
<p> Note that you will need to set these variables using the appropriate method required for the UNIX shell that you use.</p>
<h2>EXAMPLES</h2>
<p> The following are some examples of how you could start GRASS</p>
<dl>
<dt><code>grass63</code></p>
<dd>
<p>&nbsp;<wbr>Start GRASS using the default user interface. The user will be prompted to choose the appropriate location and mapset.</p>
<dt><code>grass63 -gui</code></p>
<dd>
<p>&nbsp;<wbr>Start GRASS using the Tcl/Tk based user interface. The user will be prompted to choose the appropriate location and mapset.</p>
<dt><code>grass63 -text</code></p>
<dd>
<p>&nbsp;<wbr>Start GRASS using the text based user interface. The user will be prompted to choose the appropriate location and mapset.</p>
<dt><code>grass63 -gui &#8211;</code></p>
<dd>
<p>&nbsp;<wbr>Start GRASS using the Tcl/Tk based user interface and try to obtain the location and mapset from environment variables.</p>
<dt><code>Other examples</code></p>
<dd>
<p>&nbsp;<wbr>See the&nbsp;<wbr><code>Location Environment Variables</code>&nbsp;<wbr>section for further examples.</dl>
<h2>BUGS AND CAVEAT</h2>
<p> If you start GRASS using the Tcl/Tk interface you must have a <i>wish</i> command in your $PATH variable. That is, the command must be named <i>wish</i> and not something like <i>wish8.3</i>. By default, a Tcl/Tk installation does not create a <i>wish</i> command. Thus, the system administrator must create an appropriate link to the actual wish program. </p>
<p> For example, suppose Tcl/Tk 8.3 programs are installed in /usr/local/bin. Then the system administrator should go to the /usr/local/bin directory and run the commands <i>ln -s wish8.3 wish</i> and <i>ln -s tclsh8.3 tclsh</i> to properly install Tcl/Tk for use with GRASS. </p>
<p> Furthermore, if you have more than one version of Tcl/Tk installed, make sure that the version you want to use with GRASS is the first version found in your $PATH variable. GRASS searches your $PATH variable until it finds the first version of <i>wish</i>.</p>
<h2>FILES</h2>
<p> <i>$UNIX_BIN/grass63</i> &#8211; GRASS startup program<br />
 <i>$GISBASE/etc/Init.sh</i> &#8211; GRASS initialization script called by <i>grass63</i><br />
 <i>$GISBASE/etc/gis_set.tcl</i> &#8211; Tcl/Tk script to set the location and mapset to use. Called by <i>Init.sh</i> </p>
<h2>SEE ALSO</h2>
<p> List of implemented GRASS environment variables. </p>
<p> GRASS Web site</p>
<h2>AUTHORS (of this page)</h2>
<p> Justin Hickey<br />
 Markus Neteler </p>
<p> <i>Last changed: $Date: 2006-11-02 07:48:36 +0100 (Thu, 02 Nov 2006) $</i> </p>
<p> Help Index </p>
<h2>Index</h2>
