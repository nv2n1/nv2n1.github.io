---
title: "admesh(1)"
name: "admesh"
section: "1"
letter: "a"
url: "/docs/linux/man/1-admesh/"
description: "ADMesh – a program for processing triangulated solid meshes"
---

<h2>NAME</h2>
<p> ADMesh &#8211; a program for processing triangulated solid meshes</p>
<h2>SYNOPSIS</h2>
<p> <code>admesh</code> [<i>OPTION</i>]&#8230; <i>file</i></p>
<h2>DESCRIPTION</h2>
<p> ADMesh is a program for processing triangulated solid meshes. Currently, ADMesh only reads the STL file format that is used for rapid prototyping applications, although it can write STL, VRML, OFF, and DXF files. </p>
<p> By default, ADMesh performs all of the mesh checking and repairing options on the input file. This means that is checks exact, nearby, remove-unconnected, fill-holes, normal-directions, and normal-values. The file type (ASCII or binary) is automatically detected. The input file is not modified unless it is specified by the <code>&#8211;write</code> option. If the following command line was input: </p>
<p> <code>admesh sphere.stl</code> </p>
<p> The file sphere.stl would be opened and read, it would be checked and fixed if necessary, and the results of processing would be printed out. The results would not be saved. </p>
<p> The default value for tolerance is the length of the shortest edge of the mesh. The default number of iterations is 2, and the default increment is 0.01% of the diameter of a sphere that encloses the entire mesh. </p>
<p> If any of the options <code>&#8211;exact</code>, <code>&#8211;nearby</code>, <code>&#8211;remove-unconnected</code>, <code>&#8211;fill-holes</code>, <code>&#8211;normal-directions</code>, <code>&#8211;reverse-all</code>, <code>&#8211;normal-values</code>, or <code>&#8211;no-check</code> are given, then no other checks besides that one will be done unless they are specified or unless they are required by ADMesh before the specified check can be done. For example the following command line: </p>
<p> <code>admesh &#8211;remove-unconnected sphere.stl</code> </p>
<p> would first do an exact check because it is required, and then the unconnected facets would be removed. The results would be printed and no other checks would be done.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;x-rotate</code>=<i>angle</i></p>
<dd> Rotate CCW about x-axis by angle degrees</p>
<dt><code>&#8211;y-rotate</code>=<i>angle</i></p>
<dd> Rotate CCW about y-axis by angle degrees</p>
<dt><code>&#8211;z-rotate</code>=<i>angle</i></p>
<dd> Rotate CCW about z-axis by angle degrees</p>
<dt><code>&#8211;xy-mirror</code></p>
<dd> Mirror about the xy plane</p>
<dt><code>&#8211;yz-mirror</code></p>
<dd> Mirror about the yz plane</p>
<dt><code>&#8211;xz-mirror</code></p>
<dd> Mirror about the xz plane</p>
<dt><code>&#8211;scale</code>=<i>factor</i></p>
<dd> Scale the file by factor (multiply by factor)</p>
<dt><code>&#8211;translate</code>=<i>x</i>,y,z</p>
<dd> Translate the file to x, y, and z</p>
<dt><code>&#8211;merge</code>=<i>name</i></p>
<dd> Merge file called name with input file</p>
<dt><code>-e</code>, <code>&#8211;exact</code></p>
<dd> Only check for perfectly matched edges</p>
<dt><code>-n</code>, <code>&#8211;nearby</code></p>
<dd> Find and connect nearby facets. Correct bad facets</p>
<dt><code>-t</code>, <code>&#8211;tolerance</code>=<i>tol</i></p>
<dd> Initial tolerance to use for nearby check = tol</p>
<dt><code>-i</code>, <code>&#8211;iterations</code>=<i>i</i></p>
<dd> Number of iterations for nearby check = i</p>
<dt><code>-m</code>, <code>&#8211;increment</code>=<i>inc</i></p>
<dd> Amount to increment tolerance after iteration=inc</p>
<dt> <code>-u</code>, <code>&#8211;remove-unconnected</code> Remove facets that have 0 neighbors</p>
<dt><code>-f</code>, <code>&#8211;fill-holes</code></p>
<dd>
<dd>Add facets to fill holes</p>
<dt><code>-d</code>, <code>&#8211;normal-directions</code></p>
<dd> Check and fix direction of normals(ie cw, ccw)</p>
<dt><code>&#8211;reverse-all</code></p>
<dd> Reverse the directions of all facets and normals</p>
<dt><code>-v</code>, <code>&#8211;normal-values</code></p>
<dd> Check and fix normal values</p>
<dt><code>-c</code>, <code>&#8211;no-check</code></p>
<dd> Don&#8217;t do any check on input file</p>
<dt><code>-b</code>, <code>&#8211;write-binary-stl</code>=<i>name</i></p>
<dd> Output a binary STL file called name</p>
<dt><code>-a</code>, <code>&#8211;write-ascii-stl</code>=<i>name</i></p>
<dd> Output an ascii STL file called name</p>
<dt><code>&#8211;write-off</code>=<i>name</i></p>
<dd> Output a Geomview OFF format file called name</p>
<dt><code>&#8211;write-dxf</code>=<i>name</i></p>
<dd> Output a DXF format file called name</p>
<dt><code>&#8211;write-vrml</code>=<i>name</i></p>
<dd> Output a VRML format file called name</p>
<dt><code>&#8211;help</code></p>
<dd> Display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> Output version information and exit</dl>
<p> The functions are executed in the same order as the options shown here. So check here to find what happens if, for example, <code>&#8211;translate</code> and <code>&#8211;merge</code> options are specified together. The order of the options specified on the command line is not important.</p>
<h2>EXAMPLES</h2>
<p> To perform all checks except for nearby, the following command line would be used: </p>
<p> <code>admesh &#8211;exact &#8211;remove-unconnected &#8211;fill-holes &#8211;normal-directions &#8211;normal-values sphere.stl</code> </p>
<p> Actually, since the <code>exact</code> check is required by ADMesh before <code>remove-unconnected</code>, and <code>remove-unconnected</code> is required before <code>&#8211;fill-holes</code>, the above command line could be shortened as follows with the same results: </p>
<p> <code>admesh &#8211;fill-holes &#8211;normal-directions &#8211;normal-values sphere.stl</code> </p>
<p> And again the same results could be achieved using the short options: </p>
<p> <code>admesh -fudev sphere.stl</code> </p>
<p> or </p>
<p> <code>admesh -fdv sphere.stl</code><br />
 The following command lines do the same thing: </p>
<p> <code>admesh sphere.stl</code> </p>
<p> <code>admesh -fundev sphere.stl</code> </p>
<p> <code>admesh -f -u -n -d -e -v sphere.stl</code> </p>
<p> since the <code>-fundev</code> options are implied by default. To eliminate one of the checks, just remove the letter of the check to eliminate from the &quot;word&quot; fundev.</p>
<h2>SEE ALSO</h2>
<p> For more information about the options and output read <code>admesh-doc.txt</code> &#8211; it is usually located in /usr/share/doc/admesh-x.xx dir.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1995, 1996 Anthony D. Martin &lt;amartin [at] engr.csulb.edu&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA. </p>
<h2>Index</h2>
