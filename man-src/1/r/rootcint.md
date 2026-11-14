---
title: "rootcint(1)"
name: "rootcint"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rootcint/"
description: "rootcint – ROOT Dictionary generator"
---

<h2 class="name">NAME</h2>
<p> rootcint &#8211; ROOT Dictionary generator </p>
<h2>SYNOPSIS</h2>
<pre><code>
rootcint header_file[+][-][!]...[LinkDef.h] &gt; dict_file
                                                  rootcint[-f] dict_file[-c] header_file[+][-][!]...[LinkDef.h]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>rootcint </code> program generates the <i>Streamer()</i>, <i>TBuffer &amp;operator&gt;&gt;() </i> and <i>ShowMembers() </i> methods for <code>ROOT </code> classes, i.e. classes using the <i>ClassDef </i> and <i>ClassImp </i> macros. In addition <code>rootcint </code> can also generate the <code>CINT </code> dictionaries needed in order to get access to ones classes via the interpreter. </p>
<p> <code>rootcint </code> can be used like: </p>
<dl>
<dt>
<dd>
rootcint TAttAxis.h[-][!]&#8230;[LinkDef.h] &gt; AxisGen.C
</dl>
<p> or</p>
<dl>
<dt>
<dd>
rootcint[-f][AxDict.C][-c] TAttAxis.h[-][!]&#8230;[LinkDef.h]
</dl>
<p> The difference between the two is that in the first case only the <i>Streamer() </i> and <i>ShowMembers() </i> methods are generated while in the latter case a complete compileable file is generated (including the include statements). The first method also allows the output to be appended to an already existing file (using <code>&gt;&gt;</code> ). The optional minus behind the include file name tells <code>rootcint </code> to not generate the <code>Streamer() </code> method. A custom method must be provided by the user in that case. When using option <code>-c </code> also the interpreter method interface stubs will be written to the output file ( <code>AxDict.C </code> in the above case). By default the output file will not be overwritten if it exists. Use the <code>-f (force) </code> option to overwite the output file. </p>
<p> Before specifying the first header file one can also add include file directories to be searched and preprocessor defines, like: </p>
<dl>
<dt>
<dd>
<pre>
<code>-I$../include -DDebug</code>
</pre>
</dl>
<p> The (optional) file <code>LinkDef.h </code> looks like: </p>
<dl>
<dt>
<dd>
<pre><code>
#ifdef __CINT__
#pragma link off all globals;
#pragma link off all classes;
#pragma link off all functions;
#pragma link C++ class TAxis;
#pragma link C++ class TAttAxis - ;
#pragma link C++ class TArrayC - !;
#pragma link C++ function StrDup;
#pragma link C++ function operator+ (const TString &amp;, const TString &amp;);
#pragma link C++ global gROOT;
#pragma link C++ global gEnv;
#pragma link C++ enum EMessageTypes;
#endif
</code></pre>
</dl>
<p> This file tells <code>rootcint </code> for which classes the method interface stubs should be generated. A trailing `-&#8216; in the class name tells <code>rootcint </code> to not generate the <code>Streamer() </code> method. This is necessary for those classes that need a customized <code>Streamer() </code> method. A trailing `!&#8217; in the class name tells <code>rootcint</code> to not generate the <code>operator&gt;&gt;(TBuffer &amp;b, MyClass *&amp;obj) </code> method. This is necessary to be able to write pointers to objects of classes not inheriting from <i>TObject. </i> When this file is not specified a default version exporting the classes with the names equal to the include files minus the <code>.h </code> is generated. </p>
<p> <code>IMPORTANT: </code></p>
<dl>
<dt>1</p>
<dd> <code>LinkDef.h </code> must be the last argument on the <code>rootcint command line. </code></p>
<dt>2</p>
<dd> Note that the <code>LinkDef </code> file name MUST contain the string: <code>LinkDef.h </code> or <code>linkdef.h</code>, i.e. <code>NA49_LinkDef.h </code> is fine just like, <code>mylinkdef.h</code>.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-root/">root</a></i>(1), <i><a href="/docs/linux/man/1-cint/">cint</a></i>(1) </p>
<p> <code>rootcint </code> is documented fully on <i>ROOT web-site</i></p>
<h2>ORIGINAL AUTHORS</h2>
<p> The ROOT team (see web page above):</p>
<dl>
<dt>
<dd> <code>Rene Brun </code> and <code>Fons Rademakers</code></dl>
<h2>COPYRIGHT</h2>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version. This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details. You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Christian Holm Christensen &lt;cholm [at] nbi.dk&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
