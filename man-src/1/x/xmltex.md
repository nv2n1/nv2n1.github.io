---
title: "xmltex(1)"
name: "xmltex"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmltex/"
description: "xmltex, pdfxmltex – xml non-validating parser in TeX"
---

<h2>NAME</h2>
<p> xmltex, pdfxmltex &#8211; xml non-validating parser in TeX</p>
<h2>SYNOPSIS</h2>
<p> <code>xmltex</code> <i>xml file</i><br />
 <code>pdfxmltex</code> <i>xml file</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>xmltex</code>, and <code>pdfxmltex</code> commands. This manual page was written for the Debian GNU/Linux distribution because the original program does not have a manual page. Instead, it has documentation in HTML and PS format in the /usr/share/doc/xmltex directory. </p>
<p> <code>xmltex</code> and <code>pdfxmltex</code> is a TeX XML parser able to transform XML documents into .dvi files. xmltex knows nothing about your XML files. It needs to load some special macros files, usually with the .xmt extension. A configuration file, either named xmltex.cfg or \jobname.cfg, is parsed. An especially useful configuration command is <i>
