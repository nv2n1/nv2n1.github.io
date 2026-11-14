---
title: "sty2dtx(1)"
name: "sty2dtx"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sty2dtx/"
description: "sty2dtx — Converts a LaTeX .sty file to a documented .dtx file"
---

<h2 class="name">NAME</h2>
<p> sty2dtx &#8212; Converts a LaTeX .sty file to a documented .dtx file </p>
<h2>VERSION</h2>
<p> Version: v2.3</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2010-2012 Martin Scharrer &lt;martin [at] scharrer-online.de&gt; </p>
<p> This program is free software: you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program. If not, see &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/">http://www.gnu.org/licenses/</a>&gt;.</p>
<h2>DESCRIPTION</h2>
<p> Converts a .sty file (LaTeX package) to .dtx format (documented LaTeX source), by surrounding macro definitions with &#8216;macro&#8217; and &#8216;macrocode&#8217; environments. The macro name is automatically inserted as an argument to the &#8216;macro&#8217; environemnt. Code lines outside macro definitions are wrapped only in &#8216;macrocode&#8217; environments. Empty lines are removed. The script is not thought to be fool proof and 100% accurate but rather as a good start to convert undocumented style files to .dtx files.</p>
<h3>Basic Usage</h3>
<pre>
     perl sty2dtx.pl infile [infile ...] outfile
</pre>
<p> or </p>
<pre>
     perl sty2dtx.pl &lt; file.sty &gt; file.dtx
</pre>
<h3>Supported Definitions</h3>
<p> The following macro definitions are detected when they are at the start of a line (can be prefixed by \global, \long, \protected and/or \outer): </p>
<pre><code>
\def   def   \gdef   �f
    
ewcommand
{
    
ame
}

ewcommand *
{
    
ame
}

ewcommand
ame       
ewcommand *
ame
    enewcommand
{
    
ame
}
enewcommand *
{
    
ame
}
enewcommand
ame     enewcommand *
ame
    \providecommand
{
    
ame
}
\providecommand *
{
    
ame
}
\providecommand
ame   \providecommand *
ame
    \@namedef
{
    
ame
}
\@namedef
ame
</code></pre>
<p> The following environment definitions are detected when they are at the start of a line: </p>
<p>
ewenvironment<br />
{<br />
    name<br />
}<br />
enewenvironemnt<br />
{<br />
    name<br />
}<br />
\provideenvironment<br />
{<br />
    name<br />
}</p>
<p> The macro and environment definition must either end at the same line or with a &#8216;<tt>&quot;}&quot;</tt>&#8216; on its own on a line.</p>
<h2>USAGE</h2>
<p>sty2dtx[&lt;options&gt;][&#8211; &lt; VAR &gt;= &lt;VALUE&gt;&#8230;][&#8211;][&lt;infile(s)&gt;][&lt;outfile&gt;]</p>
<h3>Files</h3>
<dl>
<dt>&bull;</p>
<dd> can be &#8216;<tt>&quot;-&quot;</tt>&#8216; for <font SIZE="-1">STDIN</font> or <font SIZE="-1">STDOUT</font>, which is the default if no files are given</p>
<dt>&bull;</p>
<dd> multiple input files are merged to one output file</dl>
<h3>Variables</h3>
<p> Variables can be defined using </p>
<pre>
  --&lt;VAR&gt;=&lt;VALUE&gt;
</pre>
<p> or </p>
<pre>
  --&lt;VAR&gt; &lt;VALUE&gt;
</pre>
<p> and will be used for substitutions in the template file. </p>
<p> <i>Common variables:</i> </p>
<pre>
      author, email, maintainer, year (for copyright),
      version, date, description (of package/class),
      type (either 'package' default or 'class'),
      filebase (automatically set from output or input file name),
</pre>
<h3>Options</h3>
<dl>
<dt><code>-h</code> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Print this help text</p>
<dd>
<dt><code>-H</code> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Print extended help</p>
<dd>
<dt><code>-V</code> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Print version and copyright</p>
<dd>
<dt><code>-v</code> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Be verbose</p>
<dd>
<dt><code>-o</code> <i>output</i> &nbsp;<wbr>&nbsp;<wbr>&nbsp;Use given file as output</p>
<dd>
<dt><code>-O</code> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Overwrite already existing output file(s)</p>
<dd>
<dt><code>-B</code> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Use basename of single input file for output file</p>
<dd>
<dt><code>-I</code> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Also create .ins (install) file</p>
<dd>
<dt><code>-c</code> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Only use code section (like v1.0)</p>
<dd>
<dt><code>-r</code> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Remove existing &#8216;macro&#8217;, &#8216;macrocode&#8217;, etc. environments.</p>
<dd>
<dt><code>-R</code> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Do not remove existing &#8216;macro&#8217;, &#8216;macrocode&#8217;, etc. environments.</p>
<dd>
<dt><code>-i</code> <i>ins-file</i> &nbsp;Create .ins file with given name</p>
<dd>
<dt><code>-t</code> <i>template</i> &nbsp;Use this file as template instead of the default one</p>
<dd>
<dt><code>-T</code> <i>template</i> &nbsp;Use this file as template for the .ins file</p>
<dd>
<dt><code>-e</code> <i>file</i> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Export default .dtx template to file and exit</p>
<dd>
<dt><code>-E</code> <i>file</i> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Export default .ins template to file and exit</p>
<dd>
<dt><code>-D</code> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Use current date as file date</p>
<dd>
<dt><code>-F</code> <i>file</i> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Read more options and variables from file.</p>
<dd>
<dt><code>-N</code> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Do not read default config file; must be the first option</p>
<dd></dl>
<h3>Config files</h3>
<p> A default config file either named &#8216;sty2dtx.cfg&#8217; or &#8216;.sty2dtx.cfg&#8217; is searched in the current directory, the users home directory and the directory of this script, in this order. The first one found is loaded. If none is found the &#8216;texmf&#8217; tree is searched for a &#8216;sty2dtx.cfg&#8217; config file. As with -F files the config file should contain one option or variable per line. Lines starting with &#8216;<tt>&quot;%&quot;</tt>&#8216; or &#8216;<tt>&quot;#&quot;</tt>&#8216; are ignored.</p>
<h2>Examples</h2>
<p> Produce &#8216;file.dtx&#8217; from &#8216;file.sty&#8217;: </p>
<pre>
    sty2dtx.pl &lt; file.sty &gt; file.dtx
</pre>
<p> or </p>
<pre>
    sty2dtx.pl file.sty file.dtx
</pre>
<p> or </p>
<pre>
    sty2dtx.pl -B file.sty
</pre>
<p> Produce &#8216;file.dtx&#8217; and &#8216;file.ins&#8217; from &#8216;file.sty&#8217;: </p>
<pre>
    sty2dtx.pl -I file.sty file.dtx
</pre>
<p> or </p>
<pre>
    sty2dtx.pl file.sty -i file.sty file.dtx
</pre>
<p> or </p>
<pre>
    sty2dtx.pl -IB file.sty
</pre>
<p> Set custom variable values: </p>
<pre><code>
sty2dtx.pl-- author Me-- email me[at] there.com mypkg.sty mypkg.dtx
</code></pre>
<p> Produce <font SIZE="-1">DTX</font> file for a class: </p>
<pre>
    sty2dtx.pl --type class mycls.sty mycls.dtx
</pre>
<h2>AUTHOR</h2>
<p> Martin Scharrer </p>
<p> E-mail: martin [at] scharrer-online.de </p>
<p> <font SIZE="-1">WWW:</font> <a rel="nofollow" href="http://www.scharrer-online.de">http://www.scharrer-online.de</a> &lt;<a rel="nofollow" href="http://www.scharrer-online.de">http://www.scharrer-online.de</a>&gt; </p>
<h2>Index</h2>
