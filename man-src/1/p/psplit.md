---
title: "psplit(1)"
name: "psplit"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psplit/"
---

<h2 class="name">NAME</h2>
 

 psplit - a tool for splitting PostScript files with multiple frames into individual PostScript files, or simply determining the number of pages in a file. 

<h2>SYNOPSIS</h2>

 usage: psplit [-c] input_file [output_file_root]

<h2>DESCRIPTION</h2>

 &quot;psplit&quot; takes a PostScript file as input (that may have multiple pictures) and splits it into individual PostScript files having a single frame each. If the original file has a %%BoundingBox comment in it, then that comment will be inserted into each output file and the output files will be EPS (encapsulated PostScript) conforming. If the original file does not have a %%BoundingBox comment, then the output files will not have one either. In that case, if you want the output files to be EPS files, use the &quot;ps2epsi&quot; utility that is based on GhostScript. If the -c option is present, then only the number of pages in input_file is reported. 

 &quot;psplit&quot; is primarily intended to be used with PostScript files that have been produced directly by NCAR Graphics, or produced from NCAR Graphics by running &quot;ctrans&quot; with a PostScript graphcap. However, &quot;psplit&quot; will also work on most PostScript files adhering to PostScript Document Structuring Conventions (DSC). 

 By default the output files are named in sequence as &quot;pict0001.ps&quot;, &quot;pict0002.ps&quot;, and so forth. If you want to specify a different root name for the output files (i.e. a name different from &quot;pict&quot;), you can specify that by entering the optional second argument.

<h2>COPYRIGHT</h2>

 Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement. 

<h2>Index</h2>


