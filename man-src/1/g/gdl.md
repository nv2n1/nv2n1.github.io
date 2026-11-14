---
title: "gdl(1)"
name: "gdl"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdl/"
description: "gdl – GNU Data Language incremental compiler"
---

<h2>NAME</h2>
<p> gdl &#8211; GNU Data Language incremental compiler</p>
<h2>SYNOPSIS</h2>
<p> <code>gdl</code> [&#8211;help] [-h] [&#8211;version] [-v] [-V] [[-]-quiet] [-q] [ -arg value ] [ -args &#8230; ] [ -e statement ] [ -pref=/path/to/preferenceFile ] [ batch_file &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <code>gdl</code> is an incremental compiler for the GNU Data Language (GDL). GDL is being developed with the aim of providing an open-source drop-in replacement for ITTVIS Interactive Data Language (IDL). It is also partially compatible with Visual Numerics (VN) PV-WAVE. IDL and PV-WAVE are registered trademarks of ITTVIS and VN, respectively. GDL and its library routines are designed as a tool for numerical data analysis and visualisation. GDL is dynamically typed, vectorized and has object-oriented programming capabilities. The library routines handle numerical calculations, data visualisation, signal/image processing, file input/output (incl. graphical and scientific data formats such as TIFF, PNG, netCDF, HDF etc) and interaction with host OS. </p>
<p> Information on GDL/IDL/PV-WAVE syntax and library routines can be found in e.g.: </p>
<p> &#8211; GDL documentation draft at: <a rel="nofollow" href="http://gnudatalanguage.sf.net/gdl.pdf">http://gnudatalanguage.sf.net/gdl.pdf</a> </p>
<p> &#8211; IDL manual on-line @ NASA.gov: <a rel="nofollow" href="http://idlastro.gsfc.nasa.gov/idl_html_help/home.html">http://idlastro.gsfc.nasa.gov/idl_html_help/home.html</a> </p>
<p> &#8211; ITTVIS (ittvis.com) and Visual Numerics (vni.com) websites </p>
<p> &#8211; comp.lang.idl-pvwave newsgroup </p>
<p> &#8211; newsletter at: <a rel="nofollow" href="https://sympa.obspm.fr/wws/info/gdl-announces">https://sympa.obspm.fr/wws/info/gdl-announces</a> </p>
<p> A vast part of GDL library routines is implemented using open-source libraries including GSL, plPlot, and optionally: readline, FFTW, Eigen3, ImageMagick, netCDF, HDF4, HDF5, libproj4, UDUNITS-2, libps and others.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help (or -h)</code></p>
<dd> Show summary of options</p>
<dt><code>&#8211;version (or -v, -V)</code></p>
<dd> Show version of program</p>
<dt><code>&#8211;quiet (or -quiet, -q)</code></p>
<dd> Suppress welcome messages</p>
<dt><code>-arg value</code></p>
<dd> Tells COMMAND_LINE_ARGS() to report the following argument (may be specified more than once)</p>
<dt><code>-args &#8230;</code></p>
<dd> Tells COMMAND_LINE_ARGS() to report all following arguments</p>
<dt><code>-e statement</code></p>
<dd> Execute given statement and exit (last occurance taken into account only, executed after startup file, may not be specified together with batch files)</p>
<dt><code>-pref=/path/to/PreferenceFile</code></p>
<dd> (only partially working now) setting using external text file few variables including default preferences (e.g. X11 Windows Size)</p>
<dt><code>&#8211;fakerelease version</code></p>
<dd> setting !VERSION.RELASE to that value. !VERSION.RELASE is often tested by procedures to decide whether some function or option should be used. It is sometimes possible to use this option to fool a procedure that request a specific value of !VERSION.RELEASE</p>
<dt>The -demo, -em, -novm, -queue, -rt, -ulicense and -vm options</p>
<dd> are ignored for compatibility with IDL.</p>
<dt>A list of batch files to be executed before entering the interactive</p>
<dd> mode (but after executing a startup file, if specified) may be given when not using the -e option.</dl>
<h2>FILES</h2>
<dl>
<dt><code>$DATADIR/gnudatalanguage/lib/*.pro</code></p>
<dd> Library routines implemented in GDL. $DATADIR is specified during compilation and usually translates to /usr/share, /usr/local/share or alike. GDL includes this directory in its search path unless GDL_PATH or IDL_PATH env. variables are set (see below).</p>
<dt><code>$HOME/.gdl/history</code></p>
<dd> A file used for storing the history of commands issued in the interactive mode</dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variables have special meaning to <code>gdl</code>. The <code>GDL_*</code> variant, if defined, takes precedence over any corresponding <code>IDL_*</code> variant.</p>
<dl>
<dt><code>GDL_PATH, IDL_PATH</code></p>
<dd> The GDL command (script) search path.</p>
<dt><code>GDL_STARTUP, IDL_STARTUP</code></p>
<dd> A file of commands to be executed on startup.</p>
<dt><code>GDL_TMPDIR, IDL_TMPDIR</code></p>
<dd> A directory in which temporary files may be created.</p>
<dt><code>HOME, SHELL</code></p>
<dd> Variables influencing shell invocations from within GDL (SPAWN procedure and the $ interpreter command). Value of HOME determines as well the location of the GDL history-file.</p>
<dt><code>PATH</code></p>
<dd> Determines search path when spawning child processes using the SPAWN procedure with the /NOSHELL keyword set.</p>
<dt><code>PYTHONPATH</code></p>
<dd> Influences behaviour of PYTHON procedure and PYTHON() function (available if GDL is compiled with support for calling Python code)</p>
<dt><code>GDL_MPI</code></p>
<dd> A message to be sent out using MPI_Send before initialization of the interpreter (available if GDL is compiled with support for MPI)</p>
<dt><code>DISPLAY, XENVIRONMENT</code></p>
<dd> Tell GDL how to connect to the X server</p>
<dt><code>PLPLOT_DRV_DIR</code></p>
<dd> Override the default location of PLplot dynamic drivers.</p>
<dt><code>LC_*</code></p>
<dd> The locale-related settings accessible via LOCALE_GET() (GDL always uses the C locale internally)</p>
<dt><code>GDL_GR_WIN_HEIGHT</code></p>
<dd> Sets the preference for the default height of a Windows(tm) graphic window</p>
<dt><code>GDL_GR_WIN_QSCREEN</code></p>
<dd> if set to true (1) this will prevent the use of the GDL_GR_WIN_HEIGHT and GDL_GR_WIN_WIDTH preferences and the default dimensions of graphic windows will be 1/4 of the screen dimensions</p>
<dt><code>GDL_GR_WIN_WIDTH</code></p>
<dd> Sets the preference for the default width of a Windows(tm) graphic window</p>
<dt><code>GDL_GR_X_HEIGHT</code></p>
<dd> Sets the preference for the default height of an X11 graphic window</p>
<dt><code>GDL_GR_X_QSCREEN</code></p>
<dd> if set to true (1) this will prevent the use of the GDL_GR_X_HEIGHT and GDL_GR_X_WIDTH preferences and the default dimensions of graphic windows will be 1/4 of the screen dimensions</p>
<dt><code>GDL_GR_X_WIDTH</code></p>
<dd> Sets the preference for the default width of an X11 graphic window</p>
<dt><code>GDL_WX_BACKEND</code></p>
<dd> can be set to [0,1,2] which will select, respectively, the backends 0,1 or 2 of plplot&#8217;s old wxWidgets driver (plplot versions &lt; 5.10). Backend 2 has antialiasing enabled.</p>
<dt><code>GSHHS_DATA_DIR</code></p>
<dd> If not automatically found, tells GDL where the gshhs files (coasts rivers, etc) are located.</dl>
<h2>BUGS</h2>
<p> Please report bugs, comments, patches or feature requests at <a rel="nofollow" href="http://sf.net/projects/gnudatalanguage/">http://sf.net/projects/gnudatalanguage/</a></p>
<h2>AUTHOR</h2>
<p> The primary author of GDL is Marc Schellens &lt;m_schellens [at] users.sourceforge.net&gt;. A list of contributors is available in the AUTHORS file shipped with GDL, and on the project website (see above). </p>
<p> The original version of this manual page was written by Sergio Gelato &lt;Sergio.Gelato [at] astro.su.se&gt;. It is currently a part of the GDL package, and is maintained by the GDL Team.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-netcdf/">netcdf</a>(3), <a href="/docs/linux/man/1-hdf/">hdf</a>(1), <a href="/docs/linux/man/3-gsl/">gsl</a>(3) </p>
<h2>Index</h2>
