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
<dt>bin</dt>
<dd> Directory where NCAR Graphics binaries are installed.</dd>
<dt>config</dt>
<dd> Directory where NCAR Graphics configuration files are installed.</dd>
<dt>data</dt>
<dd> Directory where NCAR Graphics HLU and NCL example data files are installed.</dd>
<dt>database</dt>
<dd> Directory where NCAR Graphics databases (like the Ezmap database) are installed.</dd>
<dt>doc</dt>
<dd> Directory where NCAR Graphics PostScript documents are installed.</dd>
<dt>examples</dt>
<dd> Directory where NCAR Graphics LLU Fortran and C examples are installed.</dd>
<dt>fontcap</dt>
<dd> The default fontcap being used; only returns a valid fontcap if the environment variable FONTCAP is set.</dd>
<dt>fontcaps</dt>
<dd> Directory where NCAR Graphics fontcaps are installed.</dd>
<dt>gks_output</dt>
<dd> The default name of the metafile.</dd>
<dt>graphcap</dt>
<dd> The default graphcap being used; only returns a valid graphcap if the environment variable GRAPHCAP is set.</dd>
<dt>graphcaps</dt>
<dd> Directory where NCAR Graphics graphcaps are installed.</dd>
<dt>hluex</dt>
<dd> Directory where NCAR Graphics HLU Fortran and C examples are installed.</dd>
<dt>include</dt>
<dd> Directory where NCAR Graphics include files are installed.</dd>
<dt>lib</dt>
<dd> Directory where NCAR Graphics libraries are installed.</dd>
<dt>man</dt>
<dd> Directory where NCAR Graphics man pages are installed.</dd>
<dt>ncarg</dt>
<dd> Root directory where NCAR Graphics examples, databases, resource files, etc. are installed.</dd>
<dt>nclex</dt>
<dd> Directory where NCAR Graphics NCL examples are installed.</dd>
<dt>ngwww</dt>
<dd> Directory where NCAR Graphics HTML files are installed (if they were installed).</dd>
<dt>ngurl</dt>
<dd> URL for the NCAR Graphics documentation.</dd>
<dt>resfiles</dt>
<dd> Directory where resource files for the NCL and HLU examples are installed.</dd>
<dt>root</dt>
<dd> Parent directory where NCAR Graphics is installed.</dd>
<dt>sysappres</dt>
<dd> Directory where the NCAR Graphics systems application resource file is installed.</dd>
<dt>sysresfile</dt>
<dd> Directory where the NCAR Graphics system resource file is installed.</dd>
<dt>tests</dt>
<dd> Directory where NCAR Graphics LLU Fortran and C test examples are installed.</dd>
<dt>tmp</dt>
<dd> Directory where NCAR Graphics temporary files will be written.</dd>
<dt>tutorial</dt>
<dd> Directory where NCAR Graphics LLU tutorial C and Fortran examples are installed.</dd>
<dt>usrresfile</dt>
<dd> Directory where the NCAR Graphics user resource file is installed.</dd>
<dt>xapp</dt>
<dd> Directory where NCAR Graphics X application default files are installed.</dd></dl>
<h2>SEE ALSO</h2>
<p> Online: <code>ncarg_env(5NCARG),</code>ncarg_gks(3NCARG),<code>ncargintro(5NCARG)</code> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement. </p>
