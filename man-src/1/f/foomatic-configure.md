---
title: "foomatic-configure(1)"
name: "foomatic-configure"
section: "1"
letter: "f"
url: "/docs/linux/man/1-foomatic-configure/"
description: "foomatic-configure – the main configuration program of the foomatic printing system."
---

<h2>NAME</h2>
<p> foomatic-configure &#8211; the main configuration program of the foomatic printing system.</p>
<h2>SYNOPSIS</h2>
<p> <code>foomatic-configure</code> [<i>OPTION</i>]&#8230; </p>
<p> <code>foomatic-configure -n</code><i>&nbsp;<wbr>queuename</i><code>&nbsp;<wbr>[&nbsp;<wbr>-N</code><i>&nbsp;<wbr>description</i><code>&nbsp;<wbr>]</code><i>&nbsp;<wbr>[&nbsp;<wbr>-L</i><code>&nbsp;<wbr>location</code><i>&nbsp;<wbr>]</i><code>&nbsp;<wbr>[&nbsp;<wbr>-c</code><i>&nbsp;<wbr>connect</i><code>&nbsp;<wbr>]</code><i>&nbsp;<wbr>[&nbsp;<wbr>-d</i><code>&nbsp;<wbr>driver</code><i>&nbsp;<wbr>]</i><code>&nbsp;<wbr>[&nbsp;<wbr>-p</code><i>&nbsp;<wbr>printer</i><code>&nbsp;<wbr>]</code><i>&nbsp;<wbr>[&nbsp;<wbr>&#8211;ppd</i><code>&nbsp;<wbr>ppdfile</code><i>&nbsp;<wbr>]</i><code>&nbsp;<wbr>[&nbsp;<wbr>-s</code><i>&nbsp;<wbr>spooler</i><code>&nbsp;<wbr>]</code><i>&nbsp;<wbr></i><code>[&nbsp;<wbr>-C&nbsp;<wbr>[&nbsp;<wbr></code><i>sourcespooler</i><code>&nbsp;<wbr>]&nbsp;<wbr></code><i>sourcequeue</i><i>&nbsp;<wbr></i><code>]&nbsp;<wbr>[&nbsp;<wbr>-o</code><i>&nbsp;<wbr>option1</i><code>=</code><i>value1</i><code>&nbsp;<wbr>-o</code><i>&nbsp;<wbr></i><code>&#8230;&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr>-q&nbsp;<wbr>]</code> <code>foomatic-configure -D -n</code><i>&nbsp;<wbr>queuename</i><code>&nbsp;<wbr>[&nbsp;<wbr>-s</code><i>&nbsp;<wbr>spooler</i><code>&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr>-q&nbsp;<wbr>]</code> </p>
<p> <code>foomatic-configure -R -n</code><i>&nbsp;<wbr>queuename</i><code>&nbsp;<wbr>[&nbsp;<wbr>-s</code><i>&nbsp;<wbr>spooler</i><code>&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr>-q&nbsp;<wbr>]</code> </p>
<p> <code>foomatic-configure -Q&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>-s</code><i>&nbsp;<wbr>spooler</i><code>&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr>-n</code><i>&nbsp;<wbr>queuename</i><code>&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr>-r&nbsp;<wbr>]</code> </p>
<p> <code>foomatic-configure -P&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>-s</code><i>&nbsp;<wbr>spooler</i><code>&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr>-n</code><i>&nbsp;<wbr>queuename</i><code>&nbsp;<wbr>]</code><i>&nbsp;<wbr></i><code>[&nbsp;<wbr>-d&nbsp;<wbr></code><i>driver&nbsp;<wbr></i><code>]&nbsp;<wbr>[&nbsp;<wbr>-p</code><i>&nbsp;<wbr>printer</i><code>&nbsp;<wbr>]</code><i>&nbsp;<wbr></i><code>[&nbsp;<wbr>&#8211;ppd&nbsp;<wbr></code><i>ppdfile&nbsp;<wbr></i><code>]&nbsp;<wbr>[&nbsp;<wbr></code><i>index&nbsp;<wbr></i><code>]</code> </p>
<p> <code>foomatic-configure -X -p</code><i>&nbsp;<wbr>printer</i><code>&nbsp;<wbr>| -d</code><i>&nbsp;<wbr>driver</i><code>&nbsp;<wbr>|</code> <code>-p</code><i>&nbsp;<wbr>printer</i><code>&nbsp;<wbr>-d</code><i>&nbsp;<wbr>driver</i> </p>
<p> <code>foomatic-configure -O</code> </p>
<p> <code>foomatic-configure -h</code> </p>
<p> <code>foomatic-configure &#8211;help</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>foomatic-configure </code> is a program to set up and configure print queues for every known spooler (CUPS, LPRng, LPD, GNUlpr, PPR, PDQ. CPS, no spooler) and every valid printer/driver combo in the Foomatic database or every PPD file coming with PostScript printers. As RIP filter (Raster Image Processor, translation from PostScript to the native language of the printer) always <code><a href="/docs/linux/man/1-foomatic-rip/">foomatic-rip</a>(1)</code> will be used, except for PPD files of PostScript printers under CUPS or PPR, they will be used without RIP filter. </p>
<p> It also comprises half of a programatic API for user tools: you can learn and control everything about the static properties of print queues here. With the sister program <code><a href="/docs/linux/man/1-foomatic-printjob/">foomatic-printjob</a>(1)</code>, you can do everything related to the print queue&#8217;s dynamic state: submit jobs, and query, cancel, reorder, and redirect them. </p>
<h3>Options</h3>
<dl>
<dt><code>-n</code><i>&nbsp;<wbr>queuename</i></p>
<dd> Configure this print queue</p>
<dt><code>-N</code><i>&nbsp;<wbr>Name/Description</i></p>
<dd> Use this proper human-readable name/description</p>
<dt><code>-L</code><i>&nbsp;<wbr>Location</i></p>
<dd> Short phrase describing this printer&#8217;s location</p>
<dt><code>-c</code><i>&nbsp;<wbr>connection</i></p>
<dd> Printer is connected thusly (ex file:/dev/lp0)</p>
<dt><code>-d</code><i>&nbsp;<wbr>driver</i></p>
<dd> Foomatic database name for desired printer driver</p>
<dt><code>-p</code><i>&nbsp;<wbr>printer</i></p>
<dd> Foomatic id for printer</p>
<dt><code>&#8211;ppd</code><i>&nbsp;<wbr>ppdfile</i></p>
<dd> PPD file, for example the one supplied by the manufacturer of a PostScript printer</p>
<dt><code>-s</code><i>&nbsp;<wbr>spooler</i></p>
<dd> Explicit spooler type (cups, lpd, lprng, pdq, ppr, direct)</p>
<dt><code>-o</code><i>&nbsp;<wbr>option=value</i></p>
<dd> Set the default of option to value</p>
<dt><code>-o</code><i>&nbsp;<wbr>option</i></p>
<dd> Turn on option by default</p>
<dt><code>-D</code></p>
<dd> Set this queue as the default queue (just give <code>-n</code> <i>queuename</i>)</p>
<dt><code>-R</code></p>
<dd> Remove this whole queue entirely (just give <code>-n</code> <i>queuename</i>)</p>
<dt><code>-C</code><i>&nbsp;<wbr>[</i><code>&nbsp;<wbr>sourcespooler</code><i>&nbsp;<wbr>]</i><code>&nbsp;<wbr>sourcequeue</code></p>
<dd> Copy sourcequeue from sourcespooler (or the current one if sourcespooler is not given) into the queue given by <code>-n</code> <i>queuename</i> (of the current spooler).</p>
<dt><code>-Q</code></p>
<dd> Query existing configuration (gives XML summary)</p>
<dt><code>-r</code></p>
<dd> List also remotely defined queues (CUPS only)</p>
<dt><code>-P</code><i>&nbsp;<wbr>[</i><code>&nbsp;<wbr>index</code><i>&nbsp;<wbr>]</i></p>
<dd> Get Perl dump of current configuration (as a Perl array named QUEUES, the first index is index, or zero if index is not given)</p>
<dt><code>-O</code></p>
<dd> Print XML Overview of all known printer/drivers (this shows also the Foomatic IDs of the printers)</p>
<dt><code>-X</code></p>
<dd> Print XML data for <code>-p</code> <i>printer</i> and/or <code>-d</code> <i>driver</i> object</p>
<dt><code>-q</code></p>
<dd> Run quietly </p>
</dl>
<h3>Commands</h3>
<p> No commands, just options </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-foomatic-printjob/">foomatic-printjob</a></i>(1),<i>&nbsp;<wbr><a href="/docs/linux/man/1-foomatic-rip/">foomatic-rip</a></i>(1) </p>
<h2>EXIT STATUS</h2>
<p> <code>foomatic-configure</code> returns 0 if no errors occurred. </p>
<h2>AUTHOR</h2>
<p> Manfred Wassmann &lt;<i>manolo [at] NCC-1701.B.Shuttle.de</i>&gt; for the foomatic project using comments from the source. </p>
<h2>BUGS</h2>
<p> <code>foomatic-configure</code> currently cannot handle printcap files in the <code>lprng</code> style. As <code>lprng</code> can use BSD style printcaps this is not much of a problem, as long as the GUI based print manager <code>lprngtool</code> is not used. The difference between those formats is, that BSD style requires continuation lines in printer definitions to be ended with a colon and the newline character to be escaped with a backslash. <code>Lprng</code> has no such restriction. </p>
<p> To use a printcap file generated or edited with <code>lprngtool</code> with <code>foomatic-configure</code> it is necessary to add <code>:\</code> to the end of all but the last line of every printer definition, just as shown below: </p>
<pre>
#comment
# primary printer name
lp
#alternate names
 |lp2|lp3
 |Example of a printer
 :sd=/usr/spool/LPD/lp
 :rw:lp=/dev/lp:mx#100
 :
</pre>
<p> must be converted to: </p>
<pre>
#comment
# primary printer name
lp\
 |lp2|lp3\
 |Example of a printer\
 :sd=/usr/spool/LPD/lp:\
 :rw:lp=/dev/lp:mx#100:
</pre>
<p> This manpage may be out of date. </p>
<h2>Index</h2>
