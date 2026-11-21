---

title: "doxygen(1)"
name: "doxygen"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doxygen/"
description: "doxygen – documentation system for various programming languages"
---

<p> Doxygen is a documentation system for C++, C, Java, Objective-C, IDL (Corba and Microsoft flavors), Fortran, Python, VHDL and to some extent PHP, C#, and D. </p>
<p> You can use doxygen in a number of ways:</p>
<dl>
<dt>1) Use doxygen to generate a template configuration file:</dt>
<dd>
</dd><dt>
</dt><dd> doxygen [-s] <code>-g</code> [configName]</dd>
<dt>2) Use doxygen to update an old configuration file:</dt>
<dd>
</dd><dt>
</dt><dd> doxygen [-s] <code>-u</code> [configName]</dd>
<dt>3) Use doxygen to generate documentation using an existing configuration file:</dt>
<dd>
</dd><dt>
</dt><dd> doxygen [configName]</dd>
<dt>4) Use doxygen to generate a template file controlling the layout of the generated documentation:</dt>
<dd>
</dd><dt>
</dt><dd> doxygen -l [layoutFileName]</dd>
<dt>
</dt><dd> In case layoutFileName is omitted layoutFileName.xml will be used as filename. If &#8211; is used for layoutFileName doxygen will write to standard output.</dd>
<dt>5) Use doxygen to generate a template style sheet file for RTF, HTML or Latex.</dt>
<dd>
</dd><dt>
</dt><dd> RTF: doxygen <code>-w</code> rtf styleSheetFile</dd>
<dt>
</dt><dd> HTML: doxygen <code>-w</code> html headerFile footerFile styleSheetFile [configFile]</dd>
<dt>
</dt><dd> LaTeX: doxygen <code>-w</code> latex headerFile footerFile styleSheetFile [configFile]</dd>
<dt>6) Use doxygen to generate an rtf extensions file</dt>
<dd>
</dd><dt>
</dt><dd> RTF: doxygen <code>-e</code> rtf extensionsFile</dd>
<dt>
</dt><dd> If &#8211; is used for extensionsFile doxygen will write to standard output.</dd>
<dt>7) Use doxygen to compare the used configuration file with the template configuration file</dt>
<dd>
</dd><dt>
</dt><dd> doxygen <code>-x</code> [configFile]</dd>
<dt>8) Use doxygen to show a list of built-in emojis.</dt>
<dd>
</dd><dt>
</dt><dd> doxygen <code>-f</code> emoji outputFileName</dd>
<dt>
</dt><dd> If &#8211; is used for outputFileName doxygen will write to standard output.</dd></dl>
<p> If <code>-s</code> is specified the comments in the config file will be omitted. If configName is omitted `Doxyfile&#8217; will be used as a default. If &#8211; is used for configFile doxygen will write / read the configuration to /from standard output / input.</p>
<h2>AUTHOR</h2>
<p> Doxygen version 1.9.1, Copyright Dimitri van Heesch 1997-2019</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-doxywizard/">doxywizard</a>(1). </p>
<p> Please consider installing the doxygen-doc package as it contains additional documentation on how to use doxygen. </p>
