---
title: "perlmine-pl(1)"
name: "perlmine-pl"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlmine-pl/"
---

perlmine - A game to clear hidden mines from a minefield 

<h2>Synopsis</h2>perl perlmine.pl
<h2>Description</h2>An example of config file: 

 <pre> # -*- perl -*-
 # ~/.perlmine
 use utf8;
 %Config = (
 %Config,
 rows =&gt; 10,
 cols =&gt; 10,
 mines =&gt; 10,
 image_directory =&gt; '/usr/share/pixmaps/gnomine',
 name =&gt; 'XXX',
 );</pre><h2>Pod Errors</h2>Hey! <b>The above document had some coding errors, which are explained below:</b>
<dl COMPACT><dt>Around line 941:
<dd>Non-ASCII character seen before =encoding in ''<font SIZE="-1">XXX</font>','. Assuming <font SIZE="-1">UTF-8</font> 

</dl>
