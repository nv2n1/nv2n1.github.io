---
title: "pptemplate(1)"
name: "pptemplate"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pptemplate/"
description: "pptemplate – script to generate Makefile.PL and PP file skeleton"
---

<h2 class="name">NAME</h2>
<p> pptemplate &#8211; script to generate Makefile.PL and PP file skeleton </p>
<h2>SYNOPSIS</h2>
<pre>
        # generate Makefile.PL and mymodule.pd in CWD
        pptemplate PDL::MyModule;
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>pptemplate</code> script is the easiest way to start a new module for <font SIZE="-1">PDL</font> that contains <font SIZE="-1">PP</font> code (see also <font SIZE="-1">PDL::PP</font>). The usage is simply </p>
<pre>
  pptemplate modulename;
</pre>
<p> As a result pptemplate will generate a perl Makefile for the new module (<i>Makefile.PL</i>) that contains the minimal structure to generate a module from <font SIZE="-1">PP</font> code and also a skeleton file for your new module. </p>
<p> The file will be called <i>mymod.pd</i> if you called <tt>&quot;pptemplate&quot;</tt> as </p>
<pre>
  pptemplate PDL::CleverAlgs::Mymod;
</pre>
<p> I suppose you can work out the naming rule <tt>&quot;;)&quot;</tt>. If not resort to experimentation or the source code. </p>
<p> <tt>&quot;pptemplate&quot;</tt> will refuse to overwrite existing files of the same name to avoid accidents. Move them out of the way if you really want to scrap them.</p>
<h3>Options</h3>
<p> Currently there is only the <tt>&quot;-i&quot;</tt> option which switches <tt>&quot;pptemplate&quot;</tt> into the so called <i>internal mode</i>. It should only be used when you are starting a new module within the main <font SIZE="-1">PDL</font> tree that is supposed to be part of the <font SIZE="-1">PDL</font> distribution and the normal <font SIZE="-1">PDL</font> build process, e.g. </p>
<pre><code>
cd PDL / IO;
mkdir Mpthree;
cd Mpthree;
pptemplate - i PDL::IO::Mpthree;
</code></pre>
<h2>BUGS</h2>
<p> Maybe <tt>&quot;;)&quot;</tt>. Feedback and bug reports are welcome.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2001, Christian Soeller. All Rights Reserved. This module is free software. It may be used, redistributed and/or modified under the same terms as <font SIZE="-1">PDL</font> itself (see &lt;<a rel="nofollow" href="http://pdl.perl.org">http://pdl.perl.org</a>&gt;). </p>
<h2>Index</h2>
