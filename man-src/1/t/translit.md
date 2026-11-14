---
title: "translit(1)"
name: "translit"
section: "1"
letter: "t"
url: "/docs/linux/man/1-translit/"
description: "translit – transliterate text between various writing systems"
---

<h2 class="name">NAME</h2>
<p> translit &#8211; transliterate text between various writing systems </p>
<h2>SYNOPSIS</h2>
<p> translit <code>-t</code> <i>name</i> <code>-r</code> <code>-i</code> <i>file</i> <code>-o</code> <i>file</i> -l -v -h</p>
<h2>DESCRIPTION</h2>
<p> <code>translit</code> transliterates <font SIZE="-1"><code>UTF-8</code></font> encoded natural language text from one writing system to another. </p>
<p> It utilizes the Perl module Lingua::Translit to accomplish this task and follows the provided transliteration standards as strict as possible. </p>
<p> <code>translit</code> regards the following commandline switches:</p>
<dl>
<dt><code>&#8211;trans</code>, <code>-t</code> <i>name</i></p>
<dd> Use the transliteration standard named <i>name</i>.</p>
<dt><code>&#8211;reverse</code>, <code>-r</code></p>
<dd> Transliterate in reverse direction. </p>
<p> <font SIZE="-1"><code>NOTE</code></font>: Not every transliteration is capable of being reversed. If unsure, have a look at the list of supported transliterations using the <code>&#8211;list</code> switch.</p>
<dt><code>&#8211;infile</code>, <code>-i</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> Read text from <i></i><font SIZE="-1"><i>FILE</i></font><i></i>. Defaults to <font SIZE="-1">STDIN.</font></p>
<dt><code>&#8211;outfile</code>, <code>-o</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> Write the transliterated text to <i></i><font SIZE="-1"><i>FILE</i></font><i></i>. Defaults to <font SIZE="-1">STDOUT.</font></p>
<dt><code>&#8211;list</code>, <code>-l</code></p>
<dd> Print a list of supported transliterations showing their</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> name</p>
<dt>&bull;</p>
<dd> reversibility</p>
<dt>&bull;</p>
<dd> description</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;verbose</code>, <code>-v</code></p>
<dd> Print verbose status messages to <font SIZE="-1">STDERR.</font></p>
<dt><code>&#8211;help</code>, <code>-h</code></p>
<dd> Show a short help text introducing command line switches only.</dl>
<h2>RESTRICTIONS</h2>
<p> The input has to be <font SIZE="-1">UTF-8</font> encoded.</p>
<h2>BUGS</h2>
<p> None known. </p>
<p> Please report bugs using <font SIZE="-1">CPAN</font>&#8216;s request tracker at &lt;<a rel="nofollow" href="https://rt.cpan.org/Public/Dist/Display.html?Name=Lingua-Translit">https://rt.cpan.org/Public/Dist/Display.html?Name=Lingua-Translit</a>&gt;.</p>
<h2>SEE ALSO</h2>
<p> Lingua::Translit, Lingua::Translit::Tables</p>
<h2>AUTHORS</h2>
<p> Alex Linke &lt;alinke [at] netzum-sorglos.de&gt; </p>
<p> Rona Linke &lt;rlinke [at] netzum-sorglos.de&gt;</p>
<h2>LICENSE AND COPYRIGHT</h2>
<p> Copyright (C) 2007-2008 Alex Linke and Rona Linke </p>
<p> Copyright (C) 2009-2016 Lingua-Systems Software GmbH </p>
<p> Copyright (C) 2016 Netzum Sorglos, Lingua-Systems Software GmbH </p>
<p> This module is free software; you can redistribute it and/or modify it under the same terms as Perl itself. </p>
<h2>Index</h2>
