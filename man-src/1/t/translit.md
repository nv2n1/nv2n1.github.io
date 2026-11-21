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
<dt><code>&#8211;trans</code>, <code>-t</code> <i>name</i></dt>
<dd> Use the transliteration standard named <i>name</i>.</dd>
<dt><code>&#8211;reverse</code>, <code>-r</code></dt>
<dd> Transliterate in reverse direction. </dd>
<p> <font SIZE="-1"><code>NOTE</code></font>: Not every transliteration is capable of being reversed. If unsure, have a look at the list of supported transliterations using the <code>&#8211;list</code> switch.</p>
<dt><code>&#8211;infile</code>, <code>-i</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></dt>
<dd> Read text from <i></i><font SIZE="-1"><i>FILE</i></font><i></i>. Defaults to <font SIZE="-1">STDIN.</font></dd>
<dt><code>&#8211;outfile</code>, <code>-o</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></dt>
<dd> Write the transliterated text to <i></i><font SIZE="-1"><i>FILE</i></font><i></i>. Defaults to <font SIZE="-1">STDOUT.</font></dd>
<dt><code>&#8211;list</code>, <code>-l</code></dt>
<dd> Print a list of supported transliterations showing their</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> name</dd>
<dt>&bull;</dt>
<dd> reversibility</dd>
<dt>&bull;</dt>
<dd> description</dd></dl>
</dl>
<dl>
</dl>
<dt><code>&#8211;verbose</code>, <code>-v</code></dt>
<dd> Print verbose status messages to <font SIZE="-1">STDERR.</font></dd>
<dt><code>&#8211;help</code>, <code>-h</code></dt>
<dd> Show a short help text introducing command line switches only.</dd></dl>
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
