---
title: "odfimgimport(1)"
name: "odfimgimport"
section: "1"
letter: "o"
url: "/docs/linux/man/1-odfimgimport/"
description: "odfimgimport – Import external images"
---

<p>odfimgimport &#8211; Import external images</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>odfimgimport</code> [-q] [-o&nbsp;<wbr><i>outputfile</i>] [<i>inputfile</i>]</dl>
<h2>Description</h2>
<dd>If you copy and paste html from your webbrowser to your word processor, the pictures in the pasted text will still load the images from the Internet. This script will import all images into the OpenDocument file. </p>
<p> If you don&#8217;t provide an input file, the program will read from stdin. If the program reads from stdin, it might not know how to resolve relative filenames. If you don&#8217;t provide an output file, the program will import the pictures into the input file.</p>
<h2>Options</h2>
<p> -q</p>
<dl>
<dt>
<dd> If there are images that can&#8217;t be imported, odfimgimport will write how many has failed. The -q flag will prevent that.</dl>
<p> -v</p>
<dl>
<dt>
<dd> Verbose: Prints the URL of every image it tries to import and the result.</dl>
<p> -o <i>outputfile</i></p>
<dl>
<dt>
<dd> The file to save the output to. &quot;-&quot; is stdout. Defaults to the input file.</dl>
<h2>Example</h2>
<dl>
<dt>
<dd> <font SIZE="-1"> </font></p>
<pre>
odfimgimport -v -o newfile.odt oldfile.odt
</pre>
<p> <font SIZE="+1"></dl>
<p> </font></p>
<h2>Author</h2>
<p> <code>S&oslash;ren Roug</code></p>
<dl>
<dt>
<dd> Original author</dl>
<h2>Index</h2>
