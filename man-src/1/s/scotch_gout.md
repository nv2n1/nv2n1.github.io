---
title: "scotch_gout(1)"
name: "scotch_gout"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scotch_gout/"
description: "gout – output graphics from matrices and graphs"
---

<h2>NAME</h2>
<p> <code>gout </code>&#8211; output graphics from matrices and graphs</p>
<h2>SYNOPSIS</h2>
<pre><code>
gout[options][gfile][xfile][mfile][vfile]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>gout</code> program creates graphics files of various types, representing the Scotch graph and mapping data which is passed to it. </p>
<p> Source graph file <i>gfile</i> can only be a centralized graph file. File <i>xfile</i> stores its associated geometry, whenever necessary. File <i>mfile</i> represents label information attached to each of the graph vertices, for instance the index of the part to which each vertex belongs in the case of a mapping file. File <i>vfile</i> is the output graphics file, the type of which may differ according to the input parameters. When file names are not specified, data is read from standard input and written to standard output. Standard streams can also be explicitly represented by a dash &#8216;-&#8216;. </p>
<p> When the proper libraries have been included at compile time, gtst can directly handle compressed graphs, both as input and output. A stream is treated as compressed whenever its name is postfixed with a compressed file extension, such as in &#8216;brol.grf.bz2&#8217; or &#8216;-.gz&#8217;. The compression formats which can be supported are the bzip2 format (&#8216;.bz2&#8217;), the gzip format (&#8216;.gz&#8217;), and the lzma format (&#8216;.lzma&#8217;, on input only).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Display some help.</p>
<dt><code>-g</code><i>geop</i></p>
<dd> Geometry parameters, which can be an arbitrary combination of any of the following code letters:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>n</code></p>
<dd> Do not read geometry data, when it is not available or not required, such as when using the <code>-om</code> option.</p>
<dt><code>p</code></p>
<dd> Permute Y and Z geometry dimensions.</p>
<dt><code>r</code></p>
<dd> Rotate geometry by 90 degrees in the (X,Y) plane.</dl>
</dl>
<dt><code>-h</code></p>
<dd> Display some help.</p>
<dt><code>-mn</code></p>
<dd> Do not read mapping data, when it is not available or not required.</p>
<dt><code>-o</code><i>outp</i></p>
<dd> Select the output file type and allows to provide additional parameters between braces and separated by commas:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>i</code></p>
<dd> OpenInventor 3D mesh file, to be viewed by means of programs such as <code>ivview</code>. Additional parameters for this output file type are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>c</code></p>
<dd> Color output.</p>
<dt><code>g</code></p>
<dd> Gray level output.</p>
<dt><code>r</code></p>
<dd> Remove cut edges.</p>
<dt><code>v</code></p>
<dd> View cut edges.</dl>
</dl>
<dt><code>m</code></p>
<dd> PostScript matrix pattern file. Additional parameters for this output file type are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>e</code></p>
<dd> EPSF-type output.</p>
<dt><code>f</code></p>
<dd> Full-page output.</dl>
</dl>
<dt><code>p</code></p>
<dd> PostScript 2D mesh file. This output module was intended for 2D meshes; as a fallback, the Z coordinate is projected according to isometric perspective rules, but drawings of full 3D objects are most likely to be unreadable. Additional parameters for this output file type are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>c</code></p>
<dd> Color output.</p>
<dt><code>g</code></p>
<dd> Gray level output.</p>
<dt><code>e</code></p>
<dd> EPSF-type output.</p>
<dt><code>f</code></p>
<dd> Full-page output.</p>
<dt><code>s</code></p>
<dd> Short clipping (disks excluded).</p>
<dt><code>l</code></p>
<dd> Large clipping (disks included).</p>
<dt><code>a</code></p>
<dd> Avoid displaying disks.</p>
<dt><code>d</code></p>
<dd> Display disks.</p>
<dt><code>r</code></p>
<dd> Remove cut edges.</p>
<dt><code>v</code></p>
<dd> View cut edges.</p>
<dt><code>X=</code><i>rat</i></p>
<dd> Maximum x clipping ratio (in [0.0;1.0]).</p>
<dt><code>x=</code><i>rat</i></p>
<dd> Minimum x clipping ratio.</p>
<dt><code>Y=</code><i>rat</i></p>
<dd> Maximum y clipping ratio.</p>
<dt><code>y=</code><i>rat</i></p>
<dd> Minimum y clipping ratio.</dl>
</dl>
<dt><code>t</code></p>
<dd> Tulip 3D mesh file. Additional parameters for this output file type are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>b</code></p>
<dd> Black and white output.</p>
<dt><code>c</code></p>
<dd> Color output.</p>
<dt><code>a</code></p>
<dd> Avoid displaying disks.</p>
<dt><code>d</code></p>
<dd> Display disks.</p>
<dt><code>r</code></p>
<dd> Remove cut edges.</p>
<dt><code>v</code></p>
<dd> View cut edges.</dl>
</dl>
</dl>
</dl>
<dt><code>-V</code></p>
<dd> Display program version and copyright.</dl>
<h2>EXAMPLES</h2>
<p> Build an OpenInventor file of the mapping of graph brol.grf contained in file brol.map. Vertices with no mapping information attached to them will be rendered in white, while distinct colors will be used to represent the different parts. Cut edges will be removed: </p>
<pre>
    $ gout '-oi{r}' brol.grf brol.xyz brol.map brol.iv
    $ ivview brol.iv
</pre>
<p> Build an OpenInventor file of graph brol.grf without any vertex information associated to it. Mapping data are not required and will not be read, but a file name has to be provided, hence the </p>
<pre>
    $ gout -oi -mn brol.grf brol.xyz - brol.iv
</pre>
<p> Output the pattern of matrix brol.grf on the form of a PostScript flat drawing. Geometry and mapping data are not required and will not be read, but file names have to be provided, hence the two &#8216;-&#8216;s: </p>
<pre>
    $ gout -om -gn -mn brol.grf - - brol.ps
</pre>
<p> Output a PostScript 2D drawing of a rectangular portion graph brol.grf, with disks representing mapping data: </p>
<pre>
    $ gout '-op{c,e,d,x=0.3,X=0.6,y=0.2,Y=0.5}' brol.grf brol.xyz brol.map brol.ps
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gmap/">gmap</a></code>(1), <code><a href="/docs/linux/man/1-gout/">gout</a></code>(1), <code><a href="/docs/linux/man/1-gtst/">gtst</a></code>(1). </p>
<p> Scotch user&#8217;s manual.</p>
<h2>AUTHOR</h2>
<p> Francois Pellegrini &lt;francois.pellegrini [at] labri.fr&gt; </p>
<h2>Index</h2>
