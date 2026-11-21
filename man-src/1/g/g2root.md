---
title: "g2root(1)"
name: "g2root"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g2root/"
description: "g2root – convert GEANT geometry files to ROOT files"
---

<h2>SYNOPSIS</h2>
<p> <code>g2rootd</code> <i>[-f map_name] geant_name macro_name</i></p>
<h2>DESCRIPTION</h2>
<p> You can convert a <code>GEANT</code> (see <i><a rel="nofollow" href="http://geant.cern.ch/">http://geant.cern.ch/</a></i> fore more on <code>GEANT</code>) geometry to <code>ROOT</code> geometry with the following steps</p>
<dl>
<dt>1</dt>
<dd> Run the interactive version of <code>GEANT</code> and produce a Zebra RZ file <i>detector.geom</i>, by typing the command: </dd>
<dl>
<dt>
</dt><dd> Geant &gt; rz/file 21 <i>detector.geom</i> on</dd></dl>
<dt>2</dt>
<dd> Run the <code>g2root</code> program to convert the Zebra RZ file into a <code>ROOT</code> macro <i>detector.C:</i> </dd>
<dl>
<dt>
</dt><dd> g2root <i>detector.geom</i> <i>detector.C</i></dd></dl>
<dt>3</dt>
<dd> Run the following <code>ROOT</code> session; </dd>
<dl>
<dt>
</dt><dd>
<pre><code>
root[1].x detector.C
    root[2] detector.Draw()
        root[3] c1.x3d()                    // (this invokes the 3-d Root viewer)
    root[4] TFile f("detector.root", "NEW") // open a new root file
    root[5] detector.Write()                // Write the geometry structure
    root[6] f.Write()
</code></pre>
</dd></dl>
<p> Note that the <i>TNode</i> structure currently in <code>ROOT</code> was not designed as a replacement for a true geometry package. The idea was mainly to draw simple geometries in event display programs. We are currently investigating several alternatives for a true &amp; efficient geometry package supporting;</p>
<dt>&#8211;</dt>
<dd> a disk data base with storage of multiple geometry versions</dd>
<dt>&#8211;</dt>
<dd> an interactive editor and viewer</dd>
<dt>&#8211;</dt>
<dd> with 3-d views</dd>
<dt>&#8211;</dt>
<dd> but also 2-d cut views</dd>
<dt>&#8211;</dt>
<dd> with interfaces to existing or future MC such as <code>GEANT3</code> or <code>GEANT4</code></dd></dl>
<p> A second program called <code>gh2root</code> (see <i><a rel="nofollow" href="http://root.cern.ch/root/gh2root.html">http://root.cern.ch/root/gh2root.html</a></i>) generates automatically C++ code corresponding to the <code>GEANT3 Zebra</code> structures <i>JSET</i>, <i>JVERTX</i>, <i>JKINE</i>, <i>JHITS</i> and <i>JDIGI.</i></p>
<h2>SEE ALSO</h2>
<dl>
<dt>
</dt><dd> <i><a href="/docs/linux/man/1-root/">root</a>(1)</i>, <i><a href="/docs/linux/man/1-h2root/">h2root</a>(1)</i>,</dd></dl>
<p> and</p>
<dl>
<dt>
</dt><dd> <i>The ROOT Users Guide</i></dd></dl>
<p> available from the main <code>ROOT</code> website:</p>
<dl>
<dt>
</dt><dd> <i><a rel="nofollow" href="http://root.cern.ch">http://root.cern.ch</a></i></dd></dl>
<h2>ORIGINAL AUTHORS</h2>
<p> The ROOT team (see web page above):</p>
<dl>
<dt>
</dt><dd> <code>Rene Brun</code> and <code>Fons Rademakers</code></dd></dl>
<h2>COPYRIGHT</h2>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version. </p>
<p> This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details. </p>
<p> You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Christian Holm Christensen &lt;cholm [at] nbi.dk&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
