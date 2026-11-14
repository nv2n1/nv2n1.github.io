---
title: "fityk(1)"
name: "fityk"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fityk/"
description: "fityk – non-linear curve fitting and data analysis"
---

<h2 class="name">NAME</h2>
<p> fityk &#8211; non-linear curve fitting and data analysis </p>
<h2>SYNOPSIS</h2>
<p> <code>fityk</code> [<i>OPTION</i>]&#8230; [<i>FILE</i>]&#8230;<br />
 <code>cfityk</code> [<i>OPTION</i>]&#8230; [<i>FILE</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This manpage documents briefly the <code>fityk</code> and <code>cfityk</code> programs for nonlinear fitting of analytical functions (especially peak-shaped) to data (usually experimental data). In other words, for nonlinear peak separation and analysis.<br />
 It was developed for analyzing diffraction patterns, but can be also used in other fields, since concepts and operations specific for crystallography are separated from the rest of the program.<br />
 Fityk offers various nonlinear fitting methods, subtracting background, calibrating data, easy placement of peaks and changing peak parameters, automation of common tasks with scripts, and much more. The main advantage of the program is a flexibility &#8211; parameters of peaks can be arbitrarily binded with each other, eg. width of peak can be an independent variable, can be the same as width of other peak or can be given by complicated &#8211; common for all peaks &#8211; formula.<br />
 The program comes in two versions: <code>fityk</code> , the GUI version and <code>cfityk</code> , the command line version.<br />
 A user manual for <code>fityk</code> and <code>cfityk</code> can be found in /usr/share/doc/fityk/fitykhelp.html. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-h, &#8211;help</p>
<dd> Print the usage and exit.</p>
<dt>-V, &#8211;version</p>
<dd> Print the version number and exit.</dl>
<p> Use &#8211;help to see the full list of options.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Carlo Segre &lt;segre [at] iit.edu&gt; and updated by Marcin Wojdyr. </p>
<h2>Index</h2>
