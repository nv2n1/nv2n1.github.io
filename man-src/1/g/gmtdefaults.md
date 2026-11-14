---
title: "gmtdefaults(1)"
name: "gmtdefaults"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmtdefaults/"
description: "gmtdefaults – List current GMT default parameters"
---

<h2>NAME</h2>
<p> gmtdefaults &#8211; List current GMT default parameters</p>
<h2>SYNOPSIS</h2>
<p> <code>gmtdefaults</code> [ [<code>u</code>|<code>s</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>gmtdefaults</code> lists the GMT parameter defaults if the option <code>-D</code> is used. There are three ways to change some of the settings: (1) Use the command <code>gmtset</code>, (2) use any text editor to edit the file <code>gmt.conf</code> in your home, ~/.gmt or current directory (if you do not have this file, run <code>gmtset</code> <code>-D</code> to get one with the system default settings), or (3) override any parameter by specifying one or more <code>&#8211;</code><code>-PARAMETER</code>=<i>VALUE</i> statements on the command line of any GMT command (<code>PARAMETER</code> and <i>VALUE</i> are any combination listed below). The first two options are permanent changes until explicitly changed back, while the last option is ephemeral and only applies to the single GMT command that received the override. GMT can provide default values in US or SI units. This choice is determined at compile time.</p>
<h2>REQUIRED ARGUMENTS</h2>
<p> None.</p>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-D</code></p>
<dd> Print the system GMT defaults to standard output. Append <code>u</code> for US defaults or <code>s</code> for SI defaults. [<code>-D</code> alone gives the version selected at compile time; If <code>-D</code> is omitted, the user&#8217;s currently active defaults are printed.]</p>
<dt><code>-^</code> or just <code>&#8211;</code></p>
<dd> Print a short message about the syntax of the command, then exits (NOTE: on Windows use just <code>&#8211;</code>).</p>
<dt><code>-+</code> or just <code>+</code></p>
<dd> Print an extensive usage (help) message, including the explanation of any module-specific option (but not the GMT common options), then exits.</p>
<dt><code>-?</code> or no arguments</p>
<dd> Print a complete usage (help) message, including the explanation of options, then exits.</p>
<dt><code>&#8211;</code><code>-version</code></p>
<dd> Print GMT version and exit.</p>
<dt><code>&#8211;</code><code>-show-datadir</code></p>
<dd> Print full path to GMT share directory and exit. </p>
<p> Your currently active defaults come from the <code>gmt.conf</code> file in the current working directory, if present; else from the <code>gmt.conf</code> file in your home directory, if present; else from the file <code>~/.gmt/gmt.conf</code> if present; else from the system defaults set at the time GMT was compiled.</dl>
<h2>GMT PARAMETERS</h2>
<p> Read the <code>gmt.conf</code> man page for a full list of the parameters that are user-definable in GMT.</p>
<h2>EXAMPLES</h2>
<p> To get a copy of the GMT parameter defaults in your home directory, run </p>
<pre>
gmt defaults -D &gt; ~/gmt.conf
</pre>
<p> You may now change the settings by editing this file using a text editor of your choice, or use <code>gmtset</code> to change specified parameters on the command line.</p>
<h2>BUGS</h2>
<p> If you have typographical errors in your <code>gmt.conf</code> file(s), a warning message will be issued, and the GMT defaults for the affected parameters will be used.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmt.conf</code>, <code>gmtcolors</code>, <code>gmtget</code>, <code>gmtset</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
