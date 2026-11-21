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
<p> <code>xmltex</code> <i>xml file</i><br />
 <code>pdfxmltex</code> <i>xml file</i></p>
<p> This manual page documents briefly the <code>xmltex</code>, and <code>pdfxmltex</code> commands. This manual page was written for the Debian GNU/Linux distribution because the original program does not have a manual page. Instead, it has documentation in HTML and PS format in the /usr/share/doc/xmltex directory. </p>
<p> <code>xmltex</code> and <code>pdfxmltex</code> is a TeX XML parser able to transform XML documents into .dvi files. xmltex knows nothing about your XML files. It needs to load some special macros files, usually with the .xmt extension. A configuration file, either named xmltex.cfg or \jobname.cfg, is parsed. An especially useful configuration command is <i></i> <i>\xmltraceoff</i> which disables XML elements tracing. </p>
<p> <code>xmltex</code> already knows about many XML schemata, such as TEI, TEI.2, MathML, SEC, HTML and XSL-FO, the support for the latest being provided by the passivetex package.  </p>
<h2>SEE ALSO</h2>
<p> The programs are documented fully in their own manual in the /usr/share/doc/xmltex directory. <br />
 <code><a href="/docs/linux/man/1-latex/">latex</a></code>(1), <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1)  </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Fabien Ni&ntilde;oles &lt;fabien [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
