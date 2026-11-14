---
title: "pdfjam(1)"
name: "pdfjam"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdfjam/"
---

<h2>NAME</h2>

 pdfjam - A shell script for manipulating PDF files

<h2>SYNOPSIS</h2>

 

 pdfjam [OPTION [OPTION] ...] [SRC [PAGESPEC] [SRC [PAGESPEC]] ...] 

<h2>DESCRIPTION</h2>

 

 pdfjam provides a front end to most capabilities of the &quot;pdfpages&quot; package (by Andreas Matthias) of pdflatex. Detailed information can be found via &quot;pdfjam --help&quot;, and also in the web page mentioned below . 

 A working installation of pdflatex, with the pdfpages package, is required. 

 The pdfjam script is distributed as (the main) part of the pdfjam package. The homepage of pdfjam is at <a rel="nofollow" HREF="https://github.com/DavidFirth/pdfjam">https://github.com/DavidFirth/pdfjam</a> . 

<h2>SETUP</h2>

 

 See <a rel="nofollow" HREF="https://github.com/DavidFirth/pdfjam">https://github.com/DavidFirth/pdfjam</a> 

<h2>CONFIGURATION FILES</h2>

 

 Configuration of the PDFjam utilities involves specifying the location of pdflatex, the location of temporary files, specification of default page size, etc. This is done in a block of lines near the top of the pdfjam script; settings made there are over-ridden by any that are found at a site-wide configuration file (at /etc/pdfjam.conf, /usr/share/etc/pdfjam.conf, /usr/local/share/pdfjam.conf, or /usr/local/etc/pdfjam.conf), which in turn are over-ridden by any that are found in a user-defaults file at ~/.pdfjam.conf. 

<h2>LIMITATIONS AND BUGS</h2>

 

 pdfjam does not work with encrypted PDF files, and does not preserve hyperlinks. 

 Please report bugs! --- either at GitHub or by email, see <a rel="nofollow" HREF="https://github.com/DavidFirth/pdfjam">https://github.com/DavidFirth/pdfjam</a> . 

<h2>LICENSE</h2>

 

 pdfjam is distributed under the GNU public license. 

<h2>AUTHOR</h2>

 

 The pdfjam package is written and maintained by David Firth. 

 

<h2>Index</h2>


