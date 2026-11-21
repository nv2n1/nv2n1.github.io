---

title: "robodoc(1)"
name: "robodoc"
section: "1"
letter: "r"
url: "/docs/linux/man/1-robodoc/"
description: "ROBODoc – Extract documentation from source code."
---

<p> ROBODoc &#8211; Extract documentation from source code.</p>
<h2>SYNOPSIS</h2>
<p> <code>robodoc</code> <i>&#8211;src</i> &lt;source&gt; <i>&#8211;doc</i> &lt;destination&gt; <code>[options]</code> </p>
<h2>DESCRIPTION</h2>
<p> ROBODoc extracts specially formated documentation from the source code. It allows you to maintain a program and its documentation in a single file. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-c</dt>
<dd> Show the copyright message. </dd>
<dt>&#8211;version</dt>
<dd> Print version information and exit. </dd>
<dt>&#8211;doc</dt>
<dd> Define the documentation directory or documentation file. A directory should start with a &#8216;/&#8217; or a &#8216;./&#8217; and should not include any &#8216;..&#8217;. </dd>
<dt>&#8211;src</dt>
<dd> Define the source directory or source file. A directory should start with a &#8216;/&#8217; or a &#8216;./&#8217; and should not include any &#8216;..&#8217;. </dd>
<dt>&#8211;ascii</dt>
<dd> Generate documentation in ASCII format. </dd>
<dt>&#8211;html</dt>
<dd> Generate documentation in HTML format. </dd>
<dt>&#8211;dbxml</dt>
<dd> Generate documentation in XML DocBook format. </dd>
<dt>&#8211;latex</dt>
<dd> Generate documentation in LaTeX format. </dd>
<dt>&#8211;rtf</dt>
<dd> Generate documentation in RTF format. </dd>
<dt>&#8211;index</dt>
<dd> Create an additional master index file. </dd>
<dt>&#8211;multidoc</dt>
<dd> Store all documentation in seperate files. </dd>
<dt>&#8211;singledoc</dt>
<dd> Store all documentation in a single file. </dd>
<dt>&#8211;singlefile</dt>
<dd> Generate a single document from a single file </dd>
<p> The complete list of options can be found in the HTML documentation. (Reference at the end of this page.) </p>
</dl>
<h2>EXAMPLES</h2>
<pre><code>
robodoc-- src./ --doc myproject-- singledoc-- html
</code></pre>
<p> Creates a document called myproject.html from all source files in the current directory. </p>
<pre><code>
robodoc-- src./ myproject /
    --doc./ myprojectdoc-- multidoc-- html-- index
</code></pre>
<p> Creates seperate documents for all the source files found in the directory ./myproject they are stored in the directory ./myprojectdoc. A master index file called ./myprojectdoc/masterindex.html is also created. This provides links to all the individual files. </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1994-2008 Frans Slothouber, Petteri Kettunen, Gergely Budai and Jacco van Weert. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>AUTHORS</h2>
<p> Frans Slothouber, Jacco van Weert, Petteri Kettunen, Bernd Koesling, Thomas Aglassinger, Anthon Pang, Stefan Kost, David Druffner, Sasha Vasko, Nathan Prewitt, Gergely Budai and Dennis Stampfer. </p>
<h2>SEE ALSO</h2>
<p> The documentation in HTML format that comes with ROBODoc. Latest version can be found from <a rel="nofollow" href="http://www.xs4all.nl/~rfsber/Robo/">http://www.xs4all.nl/~rfsber/Robo/</a> or from <a rel="nofollow" href="http://sourceforge.net/projects/robodoc/.">http://sourceforge.net/projects/robodoc/.</a> </p>
<p> <code><a href="/docs/linux/man/1-robohdrs/">robohdrs</a>(1)</code> </p>
