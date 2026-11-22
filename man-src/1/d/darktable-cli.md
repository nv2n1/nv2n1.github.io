---

title: "darktable-cli(1)"
name: "darktable-cli"
section: "1"
letter: "d"
url: "/docs/linux/man/1-darktable-cli/"
description: "darktable-cli – a command line darktable variant"
---

<p> darktable-cli &#8211; a command line darktable variant </p>
<h2>SYNOPSIS</h2>
<pre><code>
darktable - cli IMG_1234.{RAW, ...}[&lt;xmp file&gt;]&lt;output file&gt;[options][--core&lt;darktable options&gt;]
</code></pre>
<p> Options: </p>
<pre><code>
--width&lt;max width&gt; --height&lt;max height&gt; --bpp&lt;bpp&gt; --hq&lt;0 | 1 | true | false&gt; --upscale&lt;0 | 1 | true | false&gt; --verbose
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>darktable</code> is a digital photography workflow application for <code>Linux</code>, <code>Mac </code><code>OS X</code> and several other <code>Unices</code>. It&#8217;s described further in <i><a href="/docs/linux/man/1-darktable/">darktable</a></i>(1). </p>
<p> <code>darktable-cli</code> is a command line variant to be used to export images given the raw file and the accompanying xmp file.</p>
<h2>OPTIONS</h2>
<p> The user needs to supply an input filename and an output filename. All other parameters are optional.</p>
<dl>
<dt><code>&lt;input file&gt;</code></dt>
<dd> The name of the input file to export.</dd>
<dt><code>&lt;xmp file&gt;</code></dt>
<dd> The optional name of an XMP sidecar file containing the history stack data to be applied during export. If this option is not given darktable will search for an XMP file that belongs to the given input file.</dd>
<dt><code>&lt;output file&gt;</code></dt>
<dd> The name of the output file. darktable derives the export file format from the file extension. You can also use all the variables available in <code>darktable</code>&#8216;s export module in the output filename.</dd>
<dt><code>&#8211;width &lt;max width&gt;</code></dt>
<dd> This optional parameter allows one to limit the width of the exported image to that number of pixels.</dd>
<dt><code>&#8211;height &lt;max height&gt;</code></dt>
<dd> This optional parameter allows one to limit the height of the exported image to that number of pixels.</dd>
<dt><code>&#8211;bpp &lt;bpp&gt;</code></dt>
<dd> An optional parameter to define the bit depth of the exported image; allowed values depend on the file format. Currently this option is not yet functional. If you need to define the bit depth you need to use the following workaround: </dd>
<pre>
    --core --conf plugins/imageio/format/&lt;FORMAT&gt;/bpp=&lt;VALUE&gt;
</pre>
<p> where <code>FORMAT</code> is the name of the selected output format, for example <code>png</code>.</p>
<dt><code>&#8211;hq &lt;0|1|true|false&gt;</code></dt>
<dd> A flag that defines whether to use high quality resampling during export. Defaults to true.</dd>
<dt><code>&#8211;upscale &lt;0|1|true|false&gt;</code></dt>
<dd> A flag that defines whether to allow upscaling during export. Defaults to false.</dd>
<dt><code>&#8211;verbose</code></dt>
<dd> Enables verbose output.</dd>
<dt><code>&#8211;core &lt;darktable options&gt;</code></dt>
<dd> All command line parameters following <code>&#8211;core</code> are passed to the darktable core and handled as standard parameters. See <i><a href="/docs/linux/man/1-darktable/">darktable</a></i>(1) for a detailed description of the options.</dd></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-darktable/">darktable</a></i>(1)</p>
<h2>AUTHORS</h2>
<p> The principal developer of darktable is Johannes Hanika. The (hopefully) complete list of contributors to the project is: </p>
<p> * developers: Henrik Andersson, Johannes Hanika, Tobias Ellinghaus, Ulrich Pegelow. </p>
<p> * ubuntu packaging, color management, video tutorials: Pascal de Bruijn. </p>
<p> * opencl pipeline, usermanual: Ulrich Pegelow. </p>
<p> * networking, battle testing, translation expert: Alexandre Prokoudine. </p>
<p> * translation: a3novy, Alexandre Prokoudine, Anocha Yimsiriwattana, Artur de Sousa Rocha, Daniele Giorgis, Dimitrios Psychogios, Ger Siemerink, Guilherme Brondani Torri, Henrik Andersson, José Carlos Casimiro, Josep Puigdemont, María Leandro, Mauro Bartoccelli, Michał Prędotka, Mikko Ruohola, Milan Knížek, Olivier Tribout, Pascal Obry, Richard Levitte, Roberto Quintero, Sebastien Delcoigne, Thomas Costis, Thomas Pryds, Tobias Ellinghaus, Victor Lamoine. </p>
<p> * contributors: Aldric Renaudin, Alexandre Prokoudine, Alexey Dokuchaev, Ammon Riley, Anton Keks, Antony Dovgal, Ari Makela, Benjamin Cahill, Brian Teague, Bruce Guenter, Cherrot Luo, Chris Mason, Christian Tellefsen, David Morel, Denis Cheremisov, Dennis Gnad, Diego Segura, Dimitrios Psychogios, Eckhart Pedersen, Edouard Gomez, Edward Herr, František Šidák, Gaspard Jankowiak, Ger Siemerink, Gianluigi Calcaterra, Guilherme Brondani Torri, Ivan Tarozzi, James C. McPherson, Jan Kundrát, Jean-Sébastien Pédron, Jérémy Rosen, Jesper Pedersen, Joao Trindade, Jon Leighton, Jose Carlos Garcia Sogo, Josef Wells, Julian J. M, Mattias Eriksson, Michal Babej, Michał Prędotka, Moritz Lipp, Olivier Tribout, Pascal de Bruijn, Pascal Obry, parafin, Petr Styblo, Pierre Le Magourou, Richard Levitte, Richard Tollerton, Robert Bieber, Roland Riegel, Roman Lebedev, Rostyslav Pidgornyi, Sergey Pavlov, Simon Harhues, Simon Spannagel, Stuart Henderson, Terry Jeffress, Tim Harder, Togan Muftuoglu, Tom Vanderpoel, Ulrich Pegelow, Wolfgang Goetz, Wolfgang Kuehnel, Yari Adan, hal, jan, maigl, tuxuser. And all those of you that made previous releases possible. </p>
<p> This man page was written by Richard Levitte &lt;richard [at] levittr.org&gt;. Additions were made by Tobias Ellinghaus &lt;me [at] houz.org&gt;.</p>
<h2>COPYRIGHT AND LICENSE</h2>
<p> <code>Copyright (C)</code> 2009-2015 by Authors. </p>
<p> <code>darktable</code> is free software; you can redistribute it and/or modify it under the terms of the GPL v3 or (at your option) any later version. </p>
