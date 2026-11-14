---
title: "hwloc-annotate(1)"
name: "hwloc-annotate"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hwloc-annotate/"
description: "hwloc-annotate – Add info attributes to a XML topology"
---

<h2>NAME</h2>
<p> hwloc-annotate &#8211; Add info attributes to a XML topology</p>
<h2>SYNOPSIS</h2>
<p> <code>hwloc-annotate</code> [<i>options</i>] <i>&lt;input.xml&gt;</i> <i>&lt;output.xml&gt;</i> <i>&lt;location&gt;</i> <i>&lt;mode&gt;</i> <i>&lt;annotation&gt;</i></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;ri</code></p>
<dd> Remove all info attributes that exist with the same name before adding the new one. This option is only accepted in &quot;info&quot; mode. If the info value is omitted, existing infos are replaced with nothing.</p>
<dt><code>&#8211;ci</code></p>
<dd> Clear the existing info attributes in the target objects before annotating. If no new annotation has to be added after clearing, <i>mode</i> should be set to <i>none</i>.</dl>
<h2>DESCRIPTION</h2>
<p> hwloc-annotate loads a topology from a XML file, adds some annotations, and export the resulting topology to another XML file. The input and output files may be the same. </p>
<p> The annotation may be string info attributes. This is specified by the <i>mode</i>:</p>
<dl>
<dt><code>info &lt;name&gt; &lt;value&gt;</code></p>
<dd> Specifies a new string info attribute whose name is <i>name</i> and value is <i>value</i>.</p>
<dt><code>misc &lt;name&gt;</code></p>
<dd> Specifies a new Misc object name.</p>
<dt><code>none</code></p>
<dd> No new annotation is added. This is useful when clearing existing attributes.</dl>
<p> Annotations may be added to one specific object in the topology, all of them, or all of a given type. This is specified by the <i>location</i>:</p>
<dl>
<dt><code>all</code></p>
<dd> annotates all objects in the topology.</p>
<dt><code>root</code></p>
<dd> annotates the root object of the topology.</p>
<dt><code>&lt;type&gt;:all</code></p>
<dd> annotates all objects of the given type.</p>
<dt><code>&lt;type&gt;:&lt;index&gt;</code></p>
<dd> annotates the object of the given type and index. The index is logical.</dl>
<p> <code>NOTE:</code> The existing annotations may be listed with hwloc-info. </p>
<p> <code>NOTE:</code> It is highly recommended that you read the <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7) overview page before reading this man page. Most of the concepts described in <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7) directly apply to the hwloc-annotate utility.</p>
<h2>EXAMPLES</h2>
<p> hwloc-annotate&#8217;s operation is best described through several examples. </p>
<p> Add an info attribute to all Core objects: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-annotate input.xml output.xml Core:all info infoname infovalue </p>
<p> Add a Misc object named &quot;foobar&quot; under the root object of the topology and modify the input XML directly: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-annotate file.xml file.xml root misc foobar </p>
<p> Add an info attribute to OS device #2 and #3: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-annotate input.xml output.xml os:2-3 info infoname infovalue </p>
<p> Change package objects to green with red text in the lstopo graphical output: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-annotate topo.xml topo.xml package:all info lstopoStyle&nbsp;<wbr>&quot;Background=#00ff00;Text=#ff0000&quot;<br />
&nbsp;<wbr>$&nbsp;<wbr>lstopo -i topo.xml</p>
<h2>RETURN VALUE</h2>
<p> Upon successful execution, hwloc-annotate generates the output topology. The return value is 0. </p>
<p> hwloc-annotate will return nonzero if any kind of error occurs, such as (but not limited to) failure to parse the command line.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7), <a href="/docs/linux/man/1-lstopo/">lstopo</a>(1), <a href="/docs/linux/man/1-hwloc-info/">hwloc-info</a>(1) </p>
<h2>Index</h2>
