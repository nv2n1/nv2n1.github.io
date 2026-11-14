---
title: "ncargpath(1)"
name: "ncargpath"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncargpath/"
description: "ncargpath – Return the full pathname to a given NCAR Graphics directory or the default of a particular NCAR Graphics attribute."
---

<h2>NAME</h2>
<p> ncargpath &#8211; Return the full pathname to a given NCAR Graphics directory or the default of a particular NCAR Graphics attribute.</p>
<h2>SYNOPSIS</h2>
<p> <code>ncargpath name</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>ncargpath</code> has one argument which is the shortened name of the directory whose full pathname you want returned or the name of the attribute whose default value you want. It is used by several NCAR Graphics scripts to find the pathname to certain installables. For example, the script <code>ncargex</code> uses <code>ncargpath</code> to determine where the directory that contains all the examples is installed. The following arguments are recognized: </p>
<dl>
<dt>bin</p>
<dd> Directory where NCAR Graphics binaries are installed.</p>
<dt>config</p>
<dd> Directory where NCAR Graphics configuration files are installed.</p>
<dt>data</p>
<dd> Directory where NCAR Graphics HLU and NCL example data files are installed.</p>
<dt>database</p>
<dd> Directory where NCAR Graphics databases (like the Ezmap database) are installed.</p>
<dt>doc</p>
<dd> Directory where NCAR Graphics PostScript documents are installed.</p>
<dt>examples</p>
<dd> Directory where NCAR Graphics LLU Fortran and C examples are installed.</p>
<dt>fontcap</p>
<dd> The default fontcap being used; only returns a valid fontcap if the environment variable FONTCAP is set.</p>
<dt>fontcaps</p>
<dd> Directory where NCAR Graphics fontcaps are installed.</p>
<dt>gks_output</p>
<dd> The default name of the metafile.</p>
<dt>graphcap</p>
<dd> The default graphcap being used; only returns a valid graphcap if the environment variable GRAPHCAP is set.</p>
<dt>graphcaps</p>
<dd> Directory where NCAR Graphics graphcaps are installed.</p>
<dt>hluex</p>
<dd> Directory where NCAR Graphics HLU Fortran and C examples are installed.</p>
<dt>include</p>
<dd> Directory where NCAR Graphics include files are installed.</p>
<dt>lib</p>
<dd> Directory where NCAR Graphics libraries are installed.</p>
<dt>man</p>
<dd> Directory where NCAR Graphics man pages are installed.</p>
<dt>ncarg</p>
<dd> Root directory where NCAR Graphics examples, databases, resource files, etc. are installed.</p>
<dt>nclex</p>
<dd> Directory where NCAR Graphics NCL examples are installed.</p>
<dt>ngwww</p>
<dd> Directory where NCAR Graphics HTML files are installed (if they were installed).</p>
<dt>ngurl</p>
<dd> URL for the NCAR Graphics documentation.</p>
<dt>resfiles</p>
<dd> Directory where resource files for the NCL and HLU examples are installed.</p>
<dt>root</p>
<dd> Parent directory where NCAR Graphics is installed.</p>
<dt>sysappres</p>
<dd> Directory where the NCAR Graphics systems application resource file is installed.</p>
<dt>sysresfile</p>
<dd> Directory where the NCAR Graphics system resource file is installed.</p>
<dt>tests</p>
<dd> Directory where NCAR Graphics LLU Fortran and C test examples are installed.</p>
<dt>tmp</p>
<dd> Directory where NCAR Graphics temporary files will be written.</p>
<dt>tutorial</p>
<dd> Directory where NCAR Graphics LLU tutorial C and Fortran examples are installed.</p>
<dt>usrresfile</p>
<dd> Directory where the NCAR Graphics user resource file is installed.</p>
<dt>xapp</p>
<dd> Directory where NCAR Graphics X application default files are installed.</dl>
<h2>SEE ALSO</h2>
<p> Online: <code>ncarg_env(5NCARG),</code>ncarg_gks(3NCARG),<code>ncargintro(5NCARG)</code> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement. </p>
<h2>Index</h2>
