---
title: "mupprnt(1)"
name: "mupprnt"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mupprnt/"
---

<h2>NAME</h2>

 

 mupprnt - print output from Mup music publisher

<h2>SYNOPSIS</h2>

 

 mupprnt <i>[mup_options] file</i>

<h2>DESCRIPTION</h2>

 

 mupprnt provides a way to print Mup output on your printer. The <i>file</i> is Mup input. Any other Mup options can be given, except -C, -E, -f, -F, -l, -m, -M, or -v, which don't produce print output. 

 Under UNIX, if the environment variable COPIES is set to a number, that number of copies will be printed. Otherwise only 1 copy will be printed. 

 

 The GS_DEVICE shell variable must be set to the proper value for your printer type. Mupprnt is a shell script (under UNIX) or batch script (under MS-DOS), so you can customize it if you wish.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/1-gs/">gs</a>(1), <a HREF="/docs/linux/man/1-mup/">mup</a>(1), <a HREF="/docs/linux/man/1-mupdisp/">mupdisp</a>(1). 
 Mup --- Music Publisher User's Guide

<h2>CAVEATS</h2>

 

 You must have mup in your PATH. You must have ghostscript (gs or gs386.exe) in your PATH. 

<h2>Index</h2>


