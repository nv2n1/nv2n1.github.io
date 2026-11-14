---
title: "ngspice(1)"
name: "ngspice"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ngspice/"
description: "ngspice – circuit simulator derived from spice]3f5"
---

<h2 class="name">NAME</h2>
<p> ngspice &#8211; circuit simulator derived from spice]3f5 </p>
<h2>SYNOPSIS</h2>
<p> <code>ngspice</code> [<i>options</i>] [<i>file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> This man page is just a small overview. The primary documentation of ngspice is in the ngspice] User&#8217;s Manual, which is available as a pdf file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code> or <code>&#8211;no-spiceinit</code></p>
<dd> Don&#8217;t try to source the file &quot;.spiceinit&quot; upon startup. Normally ngspice] tries to find the file in the current directory, and if it is not found then in the user&#8217;s home directory.</p>
<dt><code>-q</code> or <code>&#8211;completion</code></p>
<dd> Enable command completion. (defect)</p>
<dt><code>-t</code> <i>term</i> or <code>&#8211;term=</code><i>term</i></p>
<dd> The program is being run on a terminal with <code>mfb</code> name <i>term</i>.</p>
<dt><code>-b</code> or <code>&#8211;batch</code></p>
<dd> Run in batch mode. ngspice] will read the standard input or the specified input file and do the simulation. Note that if the standard input is not a terminal, ngspice] will default to batch mode, unless the -i flag is given.</p>
<dt><code>-s</code> or <code>&#8211;server</code></p>
<dd> Run in server mode. This is like batch mode, except that a temporary rawfile is used and then written to the standard output, preceded by a line with a single &quot;@&quot;, after the simulation is done. This mode is used by the ngspice daemon.</p>
<dt><code>-i</code> or <code>&#8211;interactive</code></p>
<dd> Run in interactive mode. This is useful if the standard input is not a terminal but interactive mode is desired. Command completion is not available unless the standard input is a terminal, however.</p>
<dt><code>-r</code> <i>rawfile</i> or <code>&#8211;rawfile=</code><i>file</i></p>
<dd> Use <i>rawfile</i> as the default file into which the results of the simulation are saved.</p>
<dt><code>-c</code> <i>circuitfile</i> or <code>&#8211;circuitfile=</code><i>circuitfile</i></p>
<dd> Use <i>circuitfile</i> as the default input deck.</p>
<dt><code>-h</code> or <code>&#8211;help</code></p>
<dd> Display a verbose help on the arguments available to the program.</p>
<dt><code>-v</code> or <code>&#8211;version</code></p>
<dd> Display a version number and copyright information of the program.</p>
<dt><code>-a</code> or <code>&#8211;autorun</code></p>
<dd> FIXME</p>
<dt><code>-o</code> <i>outfile</i> or <code>&#8211;output=</code><i>outfile</i></p>
<dd> All logs generated during a batch run (<code>-b</code>) will be saved in <i>outfile</i>.</p>
<dt><code>-p</code> or <code>&#8211;pipe</code></p>
<dd> Allow a program (e.g., xcircuit) to act as a GUI frontend for ngspice through a pipe. Thus ngspice will assume that the pipe is a tty and allows to run in interactive mode.</dl>
<p> Further arguments are taken to be spice] input decks, which are read and saved. (If batch mode is requested then they are run immediately.)</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>SPICE_LIB_DIR</code></p>
<dd>
<dt><code>SPICE_EXEC_DIR</code></p>
<dd>
<dt><code>SPICE_HOST</code></p>
<dd>
<dt><code>SPICE_BUGADDR</code></p>
<dd>
<dt><code>SPICE_EDITOR</code></p>
<dd>
<dt><code>SPICE_ASCIIRAWFILE</code> default <i>0</i></p>
<dd> Format of the rawfile. <i>0</i> for binary, and <i>1</i> for ascii.</p>
<dt><code>SPICE_NEWS</code> default <i>$SPICE_LIB_DIR/news</i></p>
<dd> A file which is copied verbatim to stdout when ngspice starts in interactive mode.</p>
<dt><code>SPICE_MFBCAP</code> default <i>$SPICE_LIB_DIR/mfbcap</i></p>
<dd>
<dt><code>SPICE_HELP_DIR</code> default <i>$SPICE_LIB_DIR/helpdir</i></p>
<dd>
<dt><code>SPICE_SCRIPTS</code> default <i>$SPICE_LIB_DIR/scripts</i></p>
<dd> In this directory the <i>spinit</i> file will be searched.</p>
<dt><code>SPICE_PATH</code> default <i>$SPICE_EXEC_DIR/ngspice</i></p>
<dd></dl>
<p> various undocumented ngspice centric environment variables :</p>
<dl>
<dt><code>NGSPICE_MEAS_PRECISION</code></p>
<dd>
<dt><code>SPICE_NO_DATASEG_CHECK</code></p>
<dd></dl>
<p> Common environment variables :</p>
<dl>
<dt><code>TERM</code> <code>LINES</code> <code>COLS</code> <code>DISPLAY</code> <code>HOME</code> <code>PATH</code> <code>EDITOR</code> <code>SHELL</code></p>
<dd>
<dt><code>POSIXLY_CORRECT</code></p>
<dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>$SPICE_LIB_DIR/scripts/spinit</i></p>
<dd> The System&#8217;s Initialisation File.</p>
<dt><i>.spiceinit</i> or <i>$HOME/.spiceinit</i></p>
<dd> The User&#8217;s Initialisation File.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-sconvert/">sconvert</a>(1), <a href="/docs/linux/man/1-ngnutmeg/">ngnutmeg</a>(1), <a href="/docs/linux/man/3-mfb/">mfb</a>(3), <a href="/docs/linux/man/3-writedata/">writedata</a>(3), and<br />
 ngspice] User&#8217;s Manual at <code><a rel="nofollow" href="http://ngspice.sourceforge.net/docs.html">http://ngspice.sourceforge.net/docs.html</a></code></p>
<h2>BUGS</h2>
<p> Please report bugs to the ngspice project via<br />
 <code><a rel="nofollow" href="http://ngspice.sourceforge.net/bugrep.html">http://ngspice.sourceforge.net/bugrep.html</a></code></p>
<h2>AUTHORS</h2>
<p> <code>spice3</code>: Tom Quarles (quarles [at] cad.berkeley.edu)<br />
 <code>nutmeg</code>: User interface: Wayne Christopher (faustus [at] cad.berkeley.edu)<br />
 <code>ngspice</code>: various authors (see <code><a rel="nofollow" href="http://sourceforge.net/projects/ngspice/">http://sourceforge.net/projects/ngspice/</a></code>) </p>
<h2>Index</h2>
