---
title: "obspectrophore(1)"
name: "obspectrophore"
section: "1"
letter: "o"
url: "/docs/linux/man/1-obspectrophore/"
description: "obspectrophore – SPECTROPHORE calculator"
---

<h2>NAME</h2>
<p> <code>obspectrophore</code> &#8211; SPECTROPHORE calculator</p>
<h2>SYNOPSIS</h2>
<p> [<i>options</i> ] &#8211;<code>i </code><i>input_file</i> </p>
<p> [-<code>u | h</code> ]</p>
<h2>DESCRIPTION</h2>
<p> can be used to generate Spectrophores, which are one-dimensional descriptors generated from the property fields surrounding the molecules. This technology allows the accurate description of molecules in terms of their surface properties or fields. Comparison of molecules property fields provides a robust structure-independent method of aligning actives from different chemical classes. When applied to molecules such as ligands and drugs, Spectrophores can be used as powerful molecular descriptors in the fields of chemoinformatics, virtual screening, and QSAR modeling.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i </code><i>file</i></p>
<dd> Specifies the molecular input file from which Spectrophores are to be calculated. The filetype is automatically detected from the file extension.</p>
<dt><code>-n </code><i>value</i></p>
<dd> Specifies the kind of normalization that should be performed. Valid values are (without quotes): <i>No</i> (default), <i>ZeroMean</i>, <i>UnitStd</i> and <i>ZeroMeanAndUnitStd</i>.</p>
<dt><code>-a </code><i>value</i></p>
<dd> Specifies the required accuracy expressed as the angular stepsize. Only the following discrete values are allowed: <i>1 | 2 | 5 | 10 | 15 | 20 </i><code>(default) | </code><i>30 | 36 | 45 | 60</i></p>
<dt><code>-s </code><i>value</i></p>
<dd> Specifies the kind of cages that should be used in terms of the underlying pointgroup: P1 or P-1. Valid values are (without quotes): <i>No</i> (default), <i>Unique</i>, <i>Mirror</i> and <i>All</i>.</p>
<dt><code>-r </code><i>value</i></p>
<dd> Specifies the required resolution expressed as a real positive number. The default value is <i>3.0</i> Angstrom. Negative values or a value equal to 0 generate an error message.</p>
<dt><code>-u</code></p>
<dd> Display implementation details.</p>
<dt><code>-h</code></p>
<dd> Display help message.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-babel/">babel</a>(1). </p>
<p> The web pages for Open Babel can be found at: &lt;<code><a rel="nofollow" href="http://openbabel.org/">http://openbabel.org/</a></code>&gt;</p>
<h2>AUTHORS</h2>
<p> An -nosplit Open Babel is developed by a cast of many, including currrent maintainers An Geoff Hutchison , An Chris Morley , An Michael Banck , and innumerable others who have contributed fixes and additions. For more contributors to Open Babel, see &lt;<code><a rel="nofollow" href="http://openbabel.org/wiki/THANKS">http://openbabel.org/wiki/THANKS</a></code>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005-2010 by Silicos NV </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation version 2 of the License. </p>
<p> The algorithm in this software has been covered by patent WO2009146735. However, Silicos NV and the inventors of the above mentioned patent assure that no patent infringment claims will be issued against individuals or institutions that use this software under the GNU General Public License. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<h2>Index</h2>
