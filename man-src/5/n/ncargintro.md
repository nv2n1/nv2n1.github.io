---
title: "ncargintro(5)"
name: "ncargintro"
section: "5"
letter: "n"
url: "/docs/linux/man/5-ncargintro/"
description: "ncargintro – NCAR Graphics Overview"
---

<p>ncargintro &#8211; NCAR Graphics Overview</p>
<h2>Synopsis</h2>
<p><code>ncargintro</code></p>
<h2>Description</h2>
<p>NCAR Graphics is a collection of graphics libraries that supports the display of scientific data. The low-level utilities (LLUs) are the traditional C and Fortran interfaces for contouring, mapping, drawing field flows, drawing surfaces, drawing histograms, drawing X/Y plots, labeling, and more. </p>
<p> Output from these interfaces can be directed in a combination of three ways: an NCGM (NCAR Graphics Computer Graphics Metafile), an X11 window, or one of many PostScript outputs (regular, Encapsulated, or Interchange PostScript format). Other formats are available through NCGM translators and accompanying device drivers.</p>
<h2>Math Library</h2>
<p>As of March, 1998 the Ngmath library contains a collection of interpolators for one-dimensional, two-dimensional, and three-dimensional data. The packages are: dsgrid &#8212; a three-dimensional random data interpolator based on a simple inverse distance weighting algorithm. </p>
<p> csagrid &#8212; an approximation package for one-dimensional, two-dimensional, and three-dimensional random data based on David Fulker&#8217;s package Splpack. Csagrid uses cubic splines to calculate its approximation function. </p>
<p> cssgrid &#8212; an interpolation package for random data on the surface of a sphere. Cssgrid uses cubic splines to calculate its interpolation function. Cssgrid is based on the work of Robert Renka. </p>
<p> fitgrid &#8212; an interpolation package for one-dimensional and two-dimensional gridded data based on Alan Cline&#8217;s package Fitpack, an early version of which is available from netlib. Fitpack uses splines under tension to interpolate in one and two dimensions. </p>
<p> natgrid &#8212; a two-dimensional random data interpolation package based on Dave Watson&#8217;s package nngridr. </p>
<p> shgrid &#8212; an interpolation package for random data in 3-space. Shgrid uses a modified Shepard&#8217;s algorithm to calculate its interpolation function. Shgrid is based on the work of Robert Renka.</p>
<h2>Environment Variables</h2>
<p>Every user of NCAR Graphics will either need to set the environment variable NCARG_ROOT or the environment variables NCARG_BIN, NCARG_LIB, and NCARG_INCLUDE depending on how NCAR Graphics was installed on your system. </p>
<p> If the NCAR Graphics binaries, libraries, and include files were installed under one root directory, say for example /usr/local/bin, /usr/local/lib, and /usr/local/include respectively, then you&#8217;ll need to do the following: </p>
<p> setenv NCARG_ROOT /usr/local </p>
<p> If the binaries, libraries, and include files were NOT installed under one root directory, say for example /usr/local/ncarg/bin, /usr/local/ncarg/lib, and /usr/local/include, then you&#8217;ll need to do the following: </p>
<p> setenv NCARG_BIN /usr/local/ncarg/bin </p>
<p> setenv NCARG_LIB /usr/local/ncarg/lib </p>
<p> setenv NCARG_INCLUDE /usr/local/include </p>
<p> The environment variable NCARG_GKS_OUTPUT may be used to direct the metafile output from the NCAR Graphics GKS package to a file (use just the file name) or to pipe it to a translator (give the name of the translator, preceded by a &quot;|&quot;). </p>
<p> The environment variable NCARG_GKS_PSOUTPUT may be used to direct the PostScript output from the NCAR Graphics GKS package to a file (stdout is allowed). </p>
<p> The environment variable NCARG_GKS_PDFOUTPUT may be used to direct the PDF output from the NCAR Graphics GKS package to a file (stdout is allowed). </p>
<p> The environment variables GRAPHCAP and FONTCAP may be used to tell the NCGM translators &quot;ctrans&quot;, &quot;ictrans&quot; and &quot;idt&quot; what default &quot;graphcap&quot; and &quot;fontcap&quot; to use. See the man pages for ctrans(1NCARG), ictrans(1NCARG), and idt(1NCARG) for more information. </p>
<p> The environment variable DISPLAY is not actually used by the translators; if you are using X Windows, it determines where the translator output is to be displayed.</p>
<h2>See Also</h2>
<p>Online: </p>
<p> Commands which facilitate compiling and running with NCAR Graphics: </p>
<p> <code>nhlf77(1NCARG),</code> <code>nhlcc(1NCARG),</code> <code>ncargf77(1NCARG),</code> <code>ncargcc(1NCARG),</code> <code>ncargpath(1NCARG),</code> <code>ncargrun(1NCARG)</code> </p>
<p> NCAR Command Language: </p>
<p> <code>ncl</code> </p>
<p> Fortran utilities in NCAR Graphics: </p>
<p> <code>areas(3NCARG),</code> <code>autograph(3NCARG),</code> <code>bivar(3NCARG),</code> <code>colconv(3NCARG),</code> <code>conpack(3NCARG),</code> <code>dashline(3NCARG),</code> <code>dashpack(3NCARG),</code> <code>ezmap(3NCARG),</code> <code>gflash(3NCARG),</code> <code>gks(3NCARG),</code> <code>gridall(3NCARG),</code> <code>histogram(3NCARG),</code> <code>isosurface(3NCARG),</code> <code>labelbar(3NCARG),</code> <code>ngmisc(3NCARG),</code> <code>plotchar(3NCARG),</code> <code>softfill(3NCARG),</code> <code>surface(3NCARG),</code> <code>scrolled_title(3NCARG),</code> <code>streamlines(3NCARG),</code> <code>tdpack(3NCARG),</code> <code>vectors(3NCARG),</code> <code>wmap(3NCARG)</code> </p>
<p> NCGM translators: </p>
<p> <code>ctrans(1NCARG),</code> <code>ictrans(1NCARG),</code> <code>idt(1NCARG),</code> <code>med(1NCARG)</code> </p>
<p> Raster formats and applications: </p>
<p> <code>ras_formats(1NCARG),</code> <code>ras_palette(1NCARG),</code> <code>rascat(1NCARG),</code> <code>rasview(1NCARG),</code> <code>rasls(1NCARG),</code> <code>rasgetpal(1NCARG)</code> </p>
<p> LLU NCAR Graphics C-binding: </p>
<p> <code>ncarg_cbind(3NCARG)</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Descriptions of environment variables: </p>
<p> <code>ncarg_env(5NCARG),</code> </p>
<p> Descriptions of fontcaps and graphcaps: </p>
<p> <code>fcaps(1NCARG),</code> <code>fontcap(5NCARG),</code> <code>gcaps(1NCARG),</code> <code>graphcap(5NCARG)</code> </p>
<p> Metafile filters: </p>
<p> <code>cgm2ncgm(1NCARG)</code> <code>ncgm2cgm(1NCARG),</code> <code>pre2ncgm(1NCARG),</code> <code>psblack(1NCARG),</code> <code>pswhite(1NCARG),</code> </p>
<p> A command which tells you what version of NCAR Graphics you are using: </p>
<p> <code>ncargversion(1NCARG)</code> </p>
<p> Utility for generating NCAR Graphics Fortran and C examples: </p>
<p> <code>ncargex(1NCARG),</code> </p>
<p> Utilities for giving you access to special NCAR Graphics files and/or tables. </p>
<p> <code>ncargfile(1NCARG)</code> </p>
<p> Programs for generating sample NCGMs: <code>ncargworld,</code>tgks0a </p>
<p> Online documentation: </p>
<p> <a rel="nofollow" href="http://ngwww.ucar.edu/ngdoc/ng/">http://ngwww.ucar.edu/ngdoc/ng/</a></p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2002<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
