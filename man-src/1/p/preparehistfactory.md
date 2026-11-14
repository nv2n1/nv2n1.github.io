---
title: "preparehistfactory(1)"
name: "preparehistfactory"
section: "1"
letter: "p"
url: "/docs/linux/man/1-preparehistfactory/"
description: "prepareHistFactory – create a working directory for the HistFactory tools"
---

<p>prepareHistFactory &#8211; create a working directory for the HistFactory tools </p>
<h2>Synopsis</h2>
<p><code>prepareHistFactory [dir_name]</code></p>
<h2>Description</h2>
<p><code>prepareHistFactory</code> is a simple script that prepares a working area (and creates the directory dir_name if specified). Within the directory dir_name, it creates a results/, data/, and config/ directory relative to the given path. It also copies the HistFactorySchema.dtd and example XML files into the config/ directory. Additionally, it copies a root file into the data/ directory for use with the examples.<br />
 Once this is done, one is ready to run the example <code>hist2workspace input.xml</code> or edit the XML files for a new project.</p>
<h2>Original Authors</h2>
<dl COMPACT>
<dd><code>Dominique Tardif</code><br />
&nbsp;<wbr>and <code>Kyle Cranmer</code></dl>
<h2>Copyright</h2>
<p>This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version. </p>
<p> This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details. </p>
<p> You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA</p>
