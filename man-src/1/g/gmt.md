---
title: "gmt(1)"
name: "gmt"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmt/"
description: "gmt – The Generic Mapping Tools data processing and display software package"
---

<h2>NAME</h2>
<p> gmt &#8211; The Generic Mapping Tools data processing and display software package</p>
<h2>INTRODUCTION</h2>
<p> GMT is a collection of public-domain Unix tools that allows you to manipulate x,y and x,y,z data sets (filtering, trend fitting, gridding, projecting, etc.) and produce PostScript illustrations ranging from simple x-y plots, via contour maps, to artificially illuminated surfaces and 3-D perspective views in black/white or full color. Linear, log10, and power scaling is supported in addition to over 30 common map projections. The processing and display routines within GMT are completely general and will handle any (x,y) or (x,y,z) data as input.</p>
<h2>SYNOPSIS</h2>
<p> <code>gmt</code> is the main program that can start any of the modules: </p>
<p> <code>gmt</code> module module-options </p>
<p> where module is the name of a GMT module and the options are those that pertain to that particular module. If no module is given then several other options are available:</p>
<dl>
<dt><code>&#8211;</code><code>-help</code></p>
<dd> List and description of GMT modules.</p>
<dt><code>&#8211;</code><code>-show-cores</code></p>
<dd> Show number of available cores.</p>
<dt><code>&#8211;</code><code>-show-bindir</code></p>
<dd> Show directory of executables and exit.</p>
<dt><code>&#8211;</code><code>-show-datadir</code></p>
<dd> Show data directory/ies and exit.</p>
<dt><code>&#8211;</code><code>-show-modules</code></p>
<dd> List module names on stdout and exit.</p>
<dt><code>&#8211;</code><code>-show-plugindir</code></p>
<dd> Show plugin directory and exit.</p>
<dt><code>&#8211;</code><code>-show-sharedir</code></p>
<dd> Show share directory and exit.</p>
<dt><code>&#8211;</code><code>-version</code></p>
<dd> Print version and exit.</p>
<dt><code>=</code></p>
<dd> Check if that module exist and if so the program will exit with status of 0; otherwise the status of exit will be non-zero.</dl>
<h2>COMMAND-LINE COMPLETION</h2>
<p> GMT provides basic command-line completion (tab completion) for bash. The completion rules are either installed in <code>/etc/bash_completion.d/gmt</code> or <code>&lt;prefix&gt;/share/tools/gmt_completion.bash</code>. Depending on the distribution, you may still need to source the gmt completion file from <code>~/.bash_completion</code> or <code>~/.bashrc</code>. For more information see Section <i>command-line-completion</i> in the CookBook.</p>
<h2>GMT OVERVIEW</h2>
<p> The following is a summary of all the programs supplied with GMT and a very short description of their purpose. Detailed information about each program can be found in the separate manual pages. <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>blockmean</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>blockmedian</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>blockmode</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>filter1d</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>fitcircle</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>gmt2kml</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>gmtconnect</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>gmtconvert</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>gmtdefaults</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>gmtget</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>gmtinfo</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>gmtmath</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>gmtselect</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>gmtset</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>gmtspatial</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>gmtsimplify</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>gmtvector</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>gmtwhich</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grd2cpt</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grd2rgb</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grd2xyz</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdblend</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdclip</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdcontour</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdconvert</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdcut</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdedit</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdfft</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdfilter</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdgradient</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdhisteq</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdimage</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdinfo</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdlandmask</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdmask</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdmath</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdpaste</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdproject</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdraster</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdsample</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdtrack</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdtrend</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdvector</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdview</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdvolume</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>greenspline</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>kml2gmt</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>makecpt</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>mapproject</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>nearneighbor</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>project</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>psbasemap</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>psclip</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>pscoast</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>pscontour</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>psconvert</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>pshistogram</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>psimage</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>pslegend</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>psmask</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>psrose</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>psscale</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>pstext</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>pswiggle</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>psxy</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>psxyz</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>sample1d</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>spectrum1d</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>splitxyz</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>surface</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>trend1d</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>trend2d</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>triangulate</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>xyz2grd</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td> Supplement <i>gshhg</i>:
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>gshhg</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td> Supplement <i>img</i>:
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>img2grd</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td> Supplement <i>meca</i>:
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>pscoupe</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>psmeca</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>pspolar</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>psvelo</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td> Supplement <i>mgd77</i>:
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>mgd77convert</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>mgd77info</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>mgd77list</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>mgd77magref</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>mgd77manage</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>mgd77path</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>mgd77sniffer</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>mgd77track</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td> Supplement <i>potential</i>:
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>gmtgravmag3d</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>gmtflexure</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>gravfft</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdflexure</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdgravmag3d</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdredpol</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdseamount</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>talwani2d</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>talwani3d</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td> Supplement <i>segy</i>:
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>pssegy</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>pssegyz</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>segy2grd</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td> Supplement <i>sph</i>:
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>sphdistance</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>sphinterpolate</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>sphtriangulate</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td> Supplement <i>spotter</i>:
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>backtracker</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdpmodeler</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdrotater</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>grdspotter</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>hotspotter</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>originator</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>rotconverter</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td> Supplement <i>x2sys</i>:
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>x2sys_binlist</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>x2sys_cross</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>x2sys_datalist</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>x2sys_get</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>x2sys_init</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>x2sys_list</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>x2sys_merge</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>x2sys_put</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>x2sys_report</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>x2sys_solve</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<h2>CUSTOM MODULES</h2>
<p> The <code>gmt</code> program can also load custom modules from shared libraries built as specified in the GMT API documentation. This way your modules can benefit form the GMT infrastructure and extend GMT in specific ways.</p>
<h2>THE COMMON GMT OPTIONS</h2>
<p> [<code>p</code>|<code>s</code>]<i>parameters</i> <code>-J</code><i>parameters</i> <code>-Jz</code>|<code>Z</code><i>parameters</i> <code>-K</code> <code>-O</code> <code>-P</code> <i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>] [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] [<i>level</i>] <i>x_offset</i> <i>y_offset</i> <code>-a</code><i>&lt;flags&gt;</i> <code>-b</code><i>&lt;binary&gt;</i> <code>-d</code><i>&lt;nodata&gt;</i> <code>-f</code><i>&lt;flags&gt;</i> <code>-g</code><i>&lt;gaps&gt;</i> <code>-h</code><i>&lt;headers&gt;</i> <code>-i</code><i>&lt;flags&gt;</i> <code>-n</code><i>&lt;flags&gt;</i> <code>-o</code><i>&lt;flags&gt;</i> <code>-p</code><i>&lt;flags&gt;</i> <code>-r</code> <code>-s</code><i>&lt;flags&gt;</i> <code>-t</code><i>&lt;transp&gt;</i> <code>-x</code>[[-]<i>n</i>] <code>-:</code>[<code>i</code>|<code>o</code>]</p>
<h2>DESCRIPTION</h2>
<p> These are all the common GMT options that remain the same for all GMT programs. No space between the option flag and the associated arguments.</p>
<dl>
<dt><code>-B</code>[<code>p</code>|<code>s</code>]<i>parameters</i></p>
<dd> Set map Frame and Axes parameters. The Frame parameters are specified by </p>
<p> <code>-B</code>[<i>axes</i>][<code>+b</code>][<code>+g</code><i>fill</i>][<code>+n</code>][<code>+o</code><i>lon/lat</i>][<code>+t</code><i>title</i>] </p>
<p> where <i>axes</i> selects which axes to plot. By default, all 4 map boundaries (or plot axes) are plotted (named <code>W</code>, <code>E</code>, <code>S</code>, <code>N</code>). To customize, append the codes for those you want (e.g., <code>WSn</code>). Upper case means plot and annotate while lower case just plots the specified axes. If a 3-D basemap is selected with <code>-p</code> and <code>-Jz</code>, append <code>Z</code> or <code>z</code> to control the appearance of the vertical axis. By default a single vertical axes will be plotted at the most suitable map corner. Override the default by appending any combination of corner ids <code>1234</code>, where <code>1</code> represents the lower left corner and the order goes counter-clockwise. Append <code>+b</code> to draw the outline of the 3-D cube defined by <code>-R</code>; this modifier is also needed to display gridlines in the x-z, y-z planes. Note that for 3-D views the title, if given, will be suppressed. You can paint the interior of the canvas with <code>+g</code><i>fill</i>. Append <code>+n</code> to have no frame and annotations at all [Default is controlled by the codes]. Optionally append <code>+o</code><i>plon/plat</i> to draw oblique gridlines about specified pole [regular gridlines]. Ignored if gridlines are not requested (below) and disallowed for the oblique Mercator projection. To add a plot title (<code>+t</code><i>title</i>). The Frame setting is optional but can be invoked once to override the above defaults. </p>
<p> The Axes parameters are specified by </p>
<p> <code>-B</code>[<code>p</code>|<code>s</code>][<code>x</code>|<code>y</code>|<code>z</code>]<i>intervals</i>[<code>+l</code>|<code>L</code><i>label</i>][<code>+p</code><i>prefix</i>][<code>+u</code><i>unit</i>] </p>
<p> but you may also split this into two separate invocations for clarity, i.e.,</p>
<dt>&bull;</p>
<dd> <code>-B</code>[<code>p</code>|<code>s</code>][<code>x</code>|<code>y</code>|<code>z</code>][<code>+l</code><i>label</i>][<code>+p</code><i>prefix</i>][<code>+u</code><i>unit</i>]</p>
<dt>&bull;</p>
<dd> <code>-B</code>[<code>p</code>|<code>s</code>][<code>x</code>|<code>y</code>|<code>z</code>]<i>intervals</i> </p>
<p> The first optional flag following <code>-B</code> selects <code>p</code> (rimary) [Default] or <code>s</code> (econdary) axes information (mostly used for time axes annotations). The [<code>x</code>|<code>y</code>|<code>z</code>] flags specify which axes you are providing information for. If none are given then we default to <code>xy</code>. If you wish to give different annotation intervals or labels for the various axes then you must repeat the <code>B</code> option for each axis (If a 3-D basemap is selected with <code>-p</code> and <code>-Jz</code>, use <code>-Bz</code> to give settings for the vertical axis.). To add a label to an axis, just append <code>+l</code><i>label</i> (Cartesian projections only). Use <code>+L</code> to force a horizontal label for <i>y</i>-axes (useful for very short labels). If the axis annotation should have a leading text prefix (e.g., dollar sign for those plots of your net worth) you can append <code>+p</code><i>prefix</i>. For geographic maps the addition of degree symbols, etc. is automatic (and controlled by the GMT default setting <i>FORMAT_GEO_MAP</i>). However, for other plots you can add specific units by adding <code>+u</code><i>unit</i>. If any of these text strings contain spaces or special UNIX characters you will need to enclose them in quotes. The <i>intervals</i> specification is a concatenated string made up of substrings of the form </p>
<p> [<code>a</code>|<code>f</code>|<code>g</code>]<i>stride</i>[<i>+-phase</i>][<code>u</code>]. </p>
<p> The leading <code>a</code> is used to specify the annotation and major tick spacing [Default], <code>f</code> for minor tick spacing, and <code>g</code> for gridline spacing. <i>stride</i> is the desired stride interval. The optional <i>phase</i> shifts the annotation interval by that amount (positive or negative). The optional <i>unit</i> indicates the unit of the <i>stride</i> and can be any of</p>
<dt>&bull;</p>
<dd> <code>Y</code> (year, plot with 4 digits)</p>
<dt>&bull;</p>
<dd> <code>y</code> (year, plot with 2 digits)</p>
<dt>&bull;</p>
<dd> <code>O</code> (month, plot using <i>FORMAT_DATE_MAP</i>)</p>
<dt>&bull;</p>
<dd> <code>o</code> (month, plot with 2 digits)</p>
<dt>&bull;</p>
<dd> <code>U</code> (ISO week, plot using <i>FORMAT_DATE_MAP</i>)</p>
<dt>&bull;</p>
<dd> <code>u</code> (ISO week, plot using 2 digits)</p>
<dt>&bull;</p>
<dd> <code>r</code> (Gregorian week, 7-day stride from start of week <i>TIME_WEEK_START</i>)</p>
<dt>&bull;</p>
<dd> <code>K</code> (ISO weekday, plot name of day)</p>
<dt>&bull;</p>
<dd> <code>D</code> (date, plot using <i>FORMAT_DATE_MAP</i>)</p>
<dt>&bull;</p>
<dd> <code>d</code> (day, plot day of month 0-31 or year 1-366, via <i>FORMAT_DATE_MAP</i>)</p>
<dt>&bull;</p>
<dd> <code>R</code> (day, same as <code>d</code>, aligned with <i>TIME_WEEK_START</i>)</p>
<dt>&bull;</p>
<dd> <code>H</code> (hour, plot using <i>FORMAT_CLOCK_MAP</i>)</p>
<dt>&bull;</p>
<dd> <code>h</code> (hour, plot with 2 digits)</p>
<dt>&bull;</p>
<dd> <code>M</code> (minute, plot using <i>FORMAT_CLOCK_MAP</i>)</p>
<dt>&bull;</p>
<dd> <code>m</code> (minute, plot with 2 digits)</p>
<dt>&bull;</p>
<dd> <code>S</code> (second, plot using <i>FORMAT_CLOCK_MAP</i>)</p>
<dt>&bull;</p>
<dd> <code>s</code> (second, plot with 2 digits). </p>
<p> Note for geographic axes <code>m</code> and <code>s</code> instead mean arc minutes and arc seconds. All entities that are language-specific are under control by <i>GMT_LANGUAGE</i>. Alternatively, for linear maps, we can omit <i>stride</i>, thus setting <i>xinfo</i>, <i>yinfo</i>, or <i>zinfo</i> to <code>a</code> plots annotations at automatically determined intervals,</p>
<dt>&bull;</p>
<dd> <code>ag</code> plots both annotations and grid lines with the same spacing,</p>
<dt>&bull;</p>
<dd> <code>afg</code> adds suitable minor tick intervals,</p>
<dt>&bull;</p>
<dd> <code>g</code> plots grid lines with the same interval as if <code>-Bf</code> was used. </p>
<p> For custom annotations and intervals, let <i>intervals</i> be given as <code>c</code><i>intfile</i>, where <i>intfile</i> contains any number of records with <i>coord</i> <i>type</i> [<i>label</i>]. Here, <i>type</i> is one or more letters from <code>a</code>|<code>i</code>, <code>f</code>, and <code>g</code>. For <code>a</code>|<code>i</code> you must supply a <i>label</i> that will be plotted at the <i>coord</i> location. For non-geographical projections: Give negative scale (in <code>-Jx</code>) or axis length (in <code>-JX</code>) to change the direction of increasing coordinates (i.e., to make the y-axis positive down). For log10 axes: Annotations can be specified in one of three ways:</p>
<dt>1.</p>
<dd> <i>stride</i> can be 1, 2, 3, or &#8211;<i>n</i>. Annotations will then occur at 1, 1-2-5, or 1-2-3-4-&#8230;-9, respectively; for &#8211;<i>n</i> we annotate every <i>n</i>&#8216;t magnitude. This option can also be used for the frame and grid intervals.</p>
<dt>2.</p>
<dd> An <code>l</code> is appended to the <i>tickinfo</i> string. Then, log10 of the tick value is plotted at every integer log10 value.</p>
<dt>3.</p>
<dd> A <code>p</code> is appended to the <i>tickinfo</i> string. Then, annotations appear as 10 raised to log10 of the tick value. </p>
<p> For power axes: Annotations can be specified in one of two ways:</p>
<dt>1.</p>
<dd> <i>stride</i> sets the regular annotation interval.</p>
<dt>2.</p>
<dd> A <code>p</code> is appended to the <i>tickinfo</i> string. Then, the annotation interval is expected to be in transformed units, but the annotation value will be plotted as untransformed units. E.g., if <i>stride</i> = 1 and <i>power</i> = 0.5 (i.e., sqrt), then equidistant annotations labeled 1-4-9&#8230; will appear. </p>
<p> These GMT parameters can affect the appearance of the map boundary: <i>MAP_ANNOT_MIN_ANGLE</i>, <i>MAP_ANNOT_MIN_SPACING</i>, <i>FONT_ANNOT_PRIMARY</i>, <i>FONT_ANNOT_SECONDARY</i>, <i>MAP_ANNOT_OFFSET_PRIMARY</i>, <i>MAP_ANNOT_OFFSET_SECONDARY</i>, <i>MAP_ANNOT_ORTHO</i>, <i>MAP_FRAME_AXES</i>, <i>MAP_DEFAULT_PEN</i>, <i>MAP_FRAME_TYPE</i>, <i>FORMAT_GEO_MAP</i>, <i>MAP_FRAME_PEN</i>, <i>MAP_FRAME_WIDTH</i>, <i>MAP_GRID_CROSS_SIZE_PRIMARY</i>, <i>MAP_GRID_PEN_PRIMARY</i>, <i>MAP_GRID_CROSS_SIZE_SECONDARY</i>, <i>MAP_GRID_PEN_SECONDARY</i>, <i>FONT_TITLE</i>, <i>FONT_LABEL</i>, <i>MAP_LINE_STEP</i>, <i>MAP_ANNOT_OBLIQUE</i>, <i>FORMAT_CLOCK_MAP</i>, <i>FORMAT_DATE_MAP</i>, <i>FORMAT_TIME_PRIMARY_MAP</i>, <i>FORMAT_TIME_SECONDARY_MAP</i>, <i>GMT_LANGUAGE</i>, <i>TIME_WEEK_START</i>, <i>MAP_TICK_LENGTH_PRIMARY</i>, and <i>MAP_TICK_PEN_PRIMARY</i>; see the <code>gmt.conf</code> man page for details. </p>
<p> <code>-J</code><i>parameters</i> </p>
<p> Select map projection. The following character determines the projection. If the character is upper case then the argument(s) supplied as scale(s) is interpreted to be the map width (or axis lengths), else the scale argument(s) is the map scale (see its definition for each projection). UNIT is cm, inch, or point, depending on the <i>PROJ_LENGTH_UNIT</i> setting in <code>gmt.conf</code>, but this can be overridden on the command line by appending <code>c</code>, <code>i</code>, or <code>p</code> to the <i>scale</i> or <i>width</i> values. Append <code>h</code>, <code>+</code>, or <code>&#8211;</code> to the given <i>width</i> if you instead want to set map height, the maximum dimension, or the minimum dimension, respectively [Default is <code>w</code> for width]. In case the central meridian is an optional parameter and it is being omitted, then the center of the longitude range given by the <code>-R</code> option is used. The default standard parallel is the equator. The ellipsoid used in the map projections is user-definable by editing the <code>gmt.conf</code> file in your home directory. 73 commonly used ellipsoids and spheroids are currently supported, and users may also specify their own custom ellipsoid parameters [Default is WGS-84]. Several GMT parameters can affect the projection: <i>PROJ_ELLIPSOID</i>, <i>GMT_INTERPOLANT</i>, <i>PROJ_SCALE_FACTOR</i>, and <i>PROJ_LENGTH_UNIT</i>; see the <code>gmt.conf</code> man page for details. Choose one of the following projections (The <code>E</code> or <code>C</code> after projection names stands for Equal-Area and Conformal, respectively): <code>CYLINDRICAL PROJECTIONS:</code> <code>-Jc</code><i>lon0/lat0/scale</i> or <code>-JC</code><i>lon0/lat0/width</i> (Cassini). Give projection center <i>lon0/lat0</i> and <i>scale</i> (<code>1:</code><i>xxxx</i> or UNIT/degree). <code>-Jcyl_stere</code>/[<i>lon0/</i>[<i>lat0/</i>]]<i>scale</i> or <code>-JCyl_stere</code>/[<i>lon0/</i>[<i>lat0/</i>]]<i>width</i> (Cylindrical Stereographic). Give central meridian <i>lon0</i> (optional), standard parallel <i>lat0</i> (optional), and <i>scale</i> along parallel (<code>1:</code><i>xxxx</i> or UNIT/degree). The standard parallel is typically one of these (but can be any value):</p>
<dt>&bull;</p>
<dd> 66.159467 &#8211; Miller&#8217;s modified Gall</p>
<dt>&bull;</p>
<dd> 55 &#8211; Kamenetskiy&#8217;s First</p>
<dt>&bull;</p>
<dd> 45 &#8211; Gall&#8217;s Stereographic</p>
<dt>&bull;</p>
<dd> 30 &#8211; Bolshoi Sovietskii Atlas Mira or Kamenetskiy&#8217;s Second</p>
<dt>&bull;</p>
<dd> 0 &#8211; Braun&#8217;s Cylindrical <code>-Jj</code>[<i>lon0/</i>]<i>scale</i> or <code>-JJ</code>[<i>lon0/</i>]<i>width</i> (Miller Cylindrical Projection). Give the central meridian <i>lon0</i> (optional) and <i>scale</i> (<code>1:</code><i>xxxx</i> or UNIT/degree). <code>-Jm</code>[<i>lon0/</i>[<i>lat0/</i>]]<i>scale</i> or <code>-JM</code>[<i>lon0/</i>[<i>lat0/</i>]]<i>width</i> (Mercator <code>[C]</code>) Give central meridian <i>lon0</i> (optional), standard parallel <i>lat0</i> (optional), and <i>scale</i> along parallel (<code>1:</code><i>xxxx</i> or UNIT/degree). <code>-Jo</code><i>parameters</i> (Oblique Mercator <code>[C]</code>). Typically used with <code>-R</code><i>LLx/LLy/URx/URy</i><code>r</code> or with projected coordinates. Specify one of:</p>
<dt><code>-Jo</code>[<code>a</code>|<code>A</code>]<i>lon0/lat0/azimuth/scale</i> or <code>-JO</code>[<code>a</code>|<code>A</code>]<i>lon0/lat0/azimuth/width</i></p>
<dd> Set projection center <i>lon0/lat0</i>, <i>azimuth</i> of oblique equator, and <i>scale</i>.</p>
<dt><code>-Jo</code>[<code>b</code>|<code>B</code>]<i>lon0/lat0/lon1/lat1/scale</i> or <code>-JO</code>[<code>b</code>|<code>B</code>]<i>lon0/lat0/lon1/lat1/scale</i></p>
<dd> Set projection center <i>lon0/lat0</i>, another point on the oblique equator <i>lon1/lat1</i>, and <i>scale</i>.</p>
<dt><code>-Joc</code>|<code>C</code><i>lon0/lat0/lonp/latp/scale</i> or <code>-JOc</code>|<code>C</code><i>lon0/lat0/lonp/latp/scale</i></p>
<dd> Set projection center <i>lon0/lat0</i>, pole of oblique projection <i>lonp/latp</i>, and <i>scale</i>. Give <i>scale</i> along oblique equator (<code>1:</code><i>xxxx</i> or UNIT/degree). The upper-case <code>A</code>|<code>B</code>|<code>C</code> to removes enforcement of a northern hemisphere pole. <code>-Jq</code>[<i>lon0/</i>[<i>lat0/</i>]]<i>scale</i> or <code>-JQ</code>[<i>lon0/</i>[<i>lat0/</i>]]<i>width</i> (Cylindrical Equidistant). Give the central meridian <i>lon0</i> (optional), standard parallel <i>lat0</i> (optional), and <i>scale</i> (<code>1:</code><i>xxxx</i> or UNIT/degree). The standard parallel is typically one of these (but can be any value):</p>
<dt>&bull;</p>
<dd> 61.7 &#8211; Grafarend and Niermann, minimum linear distortion</p>
<dt>&bull;</p>
<dd> 50.5 &#8211; Ronald Miller Equirectangular</p>
<dt>&bull;</p>
<dd> 43.5 &#8211; Ronald Miller, minimum continental distortion</p>
<dt>&bull;</p>
<dd> 42 &#8211; Grafarend and Niermann</p>
<dt>&bull;</p>
<dd> 37.5 &#8211; Ronald Miller, minimum overall distortion</p>
<dt>&bull;</p>
<dd> 0 &#8211; Plate Carree, Simple Cylindrical, Plain/Plane Chart <code>-Jt</code><i>lon0/</i>[<i>lat0/</i>]<i>scale</i> or <code>-JT</code><i>lon0/</i>[<i>lat0/</i>]<i>width</i> (Transverse Mercator <code>[C]</code>) Give the central meridian <i>lon0</i>, central parallel <i>lat0</i> (optional), and <i>scale</i> (<code>1:</code><i>xxxx</i> or UNIT/degree). <code>-Ju</code><i>zone/scale</i> or <code>-JU</code><i>zone/width</i> (UTM &#8211; Universal Transverse Mercator <code>[C]</code>). Give the UTM zone (A,B,1-60[C-X],Y,Z)) and <i>scale</i> (<code>1:</code><i>xxxx</i> or UNIT/degree). Zones: If C-X not given, prepend &#8211; or + to enforce southern or northern hemisphere conventions [northern if south &gt; 0]. <code>-Jy</code>[<i>lon0/</i>[<i>lat0/</i>]]<i>scale</i> or <code>-JY</code>[<i>lon0/</i>[<i>lat0/</i>]]<i>width</i> (Cylindrical Equal-Area <code>[E]</code>). Give the central meridian <i>lon0</i> (optional), standard parallel <i>lat0</i> (optional), and <i>scale</i> (<code>1:</code><i>xxxx</i> or UNIT/degree). The standard parallel is typically one of these (but can be any value):</p>
<dt>&bull;</p>
<dd> 50 &#8211; Balthasart</p>
<dt>&bull;</p>
<dd> 45 &#8211; Gall-Peters</p>
<dt>&bull;</p>
<dd> 37.0666 &#8211; Caster</p>
<dt>&bull;</p>
<dd> 37.4 &#8211; Trystan Edwards</p>
<dt>&bull;</p>
<dd> 37.5 &#8211; Hobo-Dyer</p>
<dt>&bull;</p>
<dd> 30 &#8211; Behrman</p>
<dt>&bull;</p>
<dd> 0 &#8211; Lambert (default) </p>
<p> <code>CONIC PROJECTIONS:</code></p>
<dt><code>-Jb</code><i>lon0/lat0/lat1/lat2/scale</i> or <code>-JB</code><i>lon0/lat0/lat1/lat2/width</i> (Albers <code>[E]</code>).</p>
<dd> Give projection center <i>lon0/lat0</i>, two standard parallels <i>lat1/lat2</i>, and <i>scale</i> (<code>1:</code><i>xxxx</i> or UNIT/degree).</p>
<dt><code>-Jd</code><i>lon0/lat0/lat1/lat2/scale</i> or <code>-JD</code><i>lon0/lat0/lat1/lat2/width</i> (Conic Equidistant)</p>
<dd> Give projection center <i>lon0/lat0</i>, two standard parallels <i>lat1/lat2</i>, and <i>scale</i> (<code>1:</code><i>xxxx</i> or UNIT/degree).</p>
<dt><code>-Jl</code><i>lon0/lat0/lat1/lat2/scale</i> or <code>-JL</code><i>lon0/lat0/lat1/lat2/width</i> (Lambert <code>[C]</code>)</p>
<dd> Give origin <i>lon0/lat0</i>, two standard parallels <i>lat1/lat2</i>, and <i>scale</i> along these (<code>1:</code><i>xxxx</i> or UNIT/degree).</p>
<dt><code>-Jpoly</code>/[<i>lon0/</i>[<i>lat0/</i>]]<i>scale</i> or <code>-JPoly</code>/[<i>lon0/</i>[<i>lat0/</i>]]<i>width</i> ((American) Polyconic).</p>
<dd> Give the central meridian <i>lon0</i> (optional), reference parallel <i>lat0</i> (optional, default = equator), and <i>scale</i> along central meridian (<code>1:</code><i>xxxx</i> or UNIT/degree). </p>
<p> <code>AZIMUTHAL PROJECTIONS:</code> </p>
<p> Except for polar aspects, <code>-R</code>w/e/s/n will be reset to <code>-Rg</code>. Use <code>-R</code>&lt;&#8230;&gt;<code>r</code> for smaller regions.</p>
<dt><code>-Ja</code><i>lon0/lat0</i>[<i>/horizon</i>]<i>/scale</i> or <code>-JA</code><i>lon0/lat0</i>[<i>/horizon</i>]<i>/width</i> (Lambert <code>[E]</code>).</p>
<dd> <i>lon0/lat0</i> specifies the projection center. <i>horizon</i> specifies the max distance from projection center (in degrees, &lt;= 180, default 90). Give <i>scale</i> as <code>1:</code><i>xxxx</i> or <i>radius/lat</i>, where <i>radius</i> is distance in UNIT from origin to the oblique latitude <i>lat</i>.</p>
<dt><code>-Je</code><i>lon0/lat0</i>[<i>/horizon</i>]<i>/scale</i> or <code>-JE</code><i>lon0/lat0</i>[<i>/horizon</i>]<i>/width</i> (Azimuthal Equidistant).</p>
<dd> <i>lon0/lat0</i> specifies the projection center. <i>horizon</i> specifies the max distance from projection center (in degrees, &lt;= 180, default 180). Give <i>scale</i> as <code>1:</code><i>xxxx</i> or <i>radius/lat</i>, where <i>radius</i> is distance in UNIT from origin to the oblique latitude <i>lat</i>.</p>
<dt><code>-Jf</code><i>lon0/lat0</i>[<i>/horizon</i>]<i>/scale</i> or <code>-JF</code><i>lon0/lat0</i>[<i>/horizon</i>]<i>/width</i> (Gnomonic).</p>
<dd> <i>lon0/lat0</i> specifies the projection center. <i>horizon</i> specifies the max distance from projection center (in degrees, &lt; 90, default 60). Give <i>scale</i> as <code>1:</code><i>xxxx</i> or <i>radius/lat</i>, where <i>radius</i> is distance in UNIT from origin to the oblique latitude <i>lat</i>.</p>
<dt><code>-Jg</code><i>lon0/lat0</i>[<i>/horizon</i>]<i>/scale</i> or <code>-JG</code><i>lon0/lat0</i>[<i>/horizon</i>]<i>/width</i> (Orthographic).</p>
<dd> <i>lon0/lat0</i> specifies the projection center. <i>horizon</i> specifies the max distance from projection center (in degrees, &lt;= 90, default 90). Give <i>scale</i> as <code>1:</code><i>xxxx</i> or <i>radius/lat</i>, where <i>radius</i> is distance in UNIT from origin to the oblique latitude <i>lat</i>.</p>
<dt><code>-Jg</code><i>lon0/lat0/altitude/azimuth/tilt/twist/Width/Height/scale</i> or <code>-JG</code><i>lon0/lat0/altitude/azimuth/tilt/twist/Width/Height/width</i> (General Perspective).</p>
<dd> <i>lon0/lat0</i> specifies the projection center. <i>altitude</i> is the height (in km) of the viewpoint above local sea level. If <i>altitude</i> is less than 10, then it is the distance from the center of the earth to the viewpoint in earth radii. If <i>altitude</i> has a suffix <code>r</code> then it is the radius from the center of the earth in kilometers. <i>azimuth</i> is measured to the east of north of view. <i>tilt</i> is the upward tilt of the plane of projection. If <i>tilt</i> is negative, then the viewpoint is centered on the horizon. Further, specify the clockwise <i>twist</i>, <i>Width</i>, and <i>Height</i> of the viewpoint in degrees. Give <i>scale</i> as <code>1:</code><i>xxxx</i> or <i>radius/lat</i>, where <i>radius</i> is distance in UNIT from origin to the oblique latitude <i>lat</i>.</p>
<dt><code>-Js</code><i>lon0/lat0</i>[<i>/horizon</i>]<i>/scale</i> or <code>-JS</code><i>lon0/lat0</i>[<i>/horizon</i>]<i>/width</i> (General Stereographic <code>[C]</code>).</p>
<dd> <i>lon0/lat0</i> specifies the projection center. <i>horizon</i> specifies the max distance from projection center (in degrees, &lt; 180, default 90). Give <i>scale</i> as <code>1:</code><i>xxxx</i> (true at pole) or <i>lat0</i>/<code>1:</code><i>xxxx</i> (true at standard parallel <i>lat</i>) or <i>radius/lat</i> (<i>radius</i> in UNIT from origin to the oblique latitude <i>lat</i>). Note if <code>1:</code><i>xxxx</i> is used then to specify <i>horizon</i> you must also specify the <i>lat</i> as +-90 to avoid ambiguity. </p>
<p> <code>MISCELLANEOUS PROJECTIONS:</code></p>
<dt><code>-Jh</code>[<i>lon0/</i>]<i>scale</i> or <code>-JH</code>[<i>lon0/</i>]<i>width</i> (Hammer <code>[E]</code>).</p>
<dd> Give the central meridian <i>lon0</i> (optional) and <i>scale</i> along equator (<code>1:</code><i>xxxx</i> or UNIT/degree).</p>
<dt><code>-Ji</code>[<i>lon0/</i>]<i>scale</i> or <code>-JI</code>[<i>lon0/</i>]<i>width</i> (Sinusoidal <code>[E]</code>).</p>
<dd> Give the central meridian <i>lon0</i> (optional) and <i>scale</i> along equator (<code>1:</code><i>xxxx</i> or UNIT/degree).</p>
<dt><code>-Jkf</code>[<i>lon0/</i>]<i>scale</i> or <code>-JKf</code>[<i>lon0/</i>]<i>width</i> (Eckert IV) <code>[E]</code>).</p>
<dd> Give the central meridian <i>lon0</i> (optional) and <i>scale</i> along equator (<code>1:</code><i>xxxx</i> or UNIT/degree).</p>
<dt><code>-Jk</code>[<code>s</code>][<i>lon0/</i>]<i>scale</i> or <code>-JK</code>[<code>s</code>][<i>lon0/</i>]<i>width</i> (Eckert VI) <code>[E]</code>).</p>
<dd> Give the central meridian <i>lon0</i> (optional) and <i>scale</i> along equator (<code>1:</code><i>xxxx</i> or UNIT/degree).</p>
<dt><code>-Jn</code>[<i>lon0/</i>]<i>scale</i> or <code>-JN</code>[<i>lon0/</i>]<i>width</i> (Robinson).</p>
<dd> Give the central meridian <i>lon0</i> (optional) and <i>scale</i> along equator (<code>1:</code><i>xxxx</i> or UNIT/degree).</p>
<dt><code>-Jr</code>[<i>lon0/</i>]<i>scale</i> <code>-JR</code>[<i>lon0/</i>]<i>width</i> (Winkel Tripel).</p>
<dd> Give the central meridian <i>lon0</i> (optional) and <i>scale</i> along equator (<code>1:</code><i>xxxx</i> or UNIT/degree).</p>
<dt><code>-Jv</code>[<i>lon0/</i>]<i>scale</i> or <code>-JV</code>[<i>lon0/</i>]<i>width</i> (Van der Grinten).</p>
<dd> Give the central meridian <i>lon0</i> (optional) and <i>scale</i> along equator (<code>1:</code><i>xxxx</i> or UNIT/degree).</p>
<dt><code>-Jw</code>[<i>lon0/</i>]<i>scale</i> or <code>-JW</code>[<i>lon0/</i>]<i>width</i> (Mollweide <code>[E]</code>).</p>
<dd> Give the central meridian <i>lon0</i> (optional) and <i>scale</i> along equator (<code>1:</code><i>xxxx</i> or UNIT/degree). </p>
<p> <code>NON-GEOGRAPHICAL PROJECTIONS:</code> <code>-Jp</code>[<code>a</code>]<i>scale</i>[<i>/origin</i>][<code>r</code>|<code>z</code>] or <code>-JP</code>[<code>a</code>]<i>width</i>[<i>/origin</i>][<code>r</code>|<code>z</code>] (Polar coordinates (theta,r)) </p>
<p> Optionally insert <code>a</code> after <code>-Jp</code> [ or <code>-JP</code>] for azimuths CW from North instead of directions CCW from East [Default]. Optionally append /<i>origin</i> in degrees to indicate an angular offset [0]). Finally, append <code>r</code> if r is elevations in degrees (requires s &gt;= 0 and n &lt;= 90) or <code>z</code> if you want to annotate depth rather than radius [Default]. Give <i>scale</i> in UNIT/r-unit. <code>-Jx</code><i>x-scale</i>[<i>/y-scale</i>] or <code>-JX</code><i>width</i>[<i>/height</i>] (Linear, log, and power scaling) </p>
<p> Give <i>x-scale</i> (<code>1:</code><i>xxxx</i> or UNIT/x-unit) and/or <i>y-scale</i> (<code>1:</code><i>xxxx</i> or UNIT/y-unit); or specify <i>width</i> and/or <i>height</i> in UNIT. <i>y-scale</i>=<i>x-scale</i> if not specified separately and using <code>1:</code><i>xxxx</i> implies that x-unit and y-unit are in meters. Use negative scale(s) to reverse the direction of an axis (e.g., to have y be positive down). Set <i>height</i> or <i>width</i> to 0 to have it recomputed based on the implied scale of the other axis. Optionally, append to <i>x-scale</i>, <i>y-scale</i>, <i>width</i> or <i>height</i> one of the following:</p>
<dt><code>d</code></p>
<dd> Data are geographical coordinates (in degrees).</p>
<dt><code>l</code></p>
<dd> Take log10 of values before scaling.</p>
<dt><code>p</code><i>power</i></p>
<dd> Raise values to <i>power</i> before scaling.</p>
<dt><code>t</code></p>
<dd> Input coordinates are time relative to <i>TIME_EPOCH</i>.</p>
<dt><code>T</code></p>
<dd> Input coordinates are absolute time. </p>
<p> Default axis lengths (see <code>gmt.conf</code>) can be invoked using <code>-JXh</code> (for landscape); <code>-JXv</code> (for portrait) will swap the x- and y-axis lengths. The default unit for this installation is either cm or inch, as defined in the file <code>share/gmt.conf</code>. However, you may change this by editing your <code>gmt.conf</code> file(s). </p>
<p> When <code>-J</code> is used without any further arguments, or just with the projection type, the arguments of the last used <code>-J</code>, or the last used <code>-J</code> with that projection type, will be used.</p>
<dt><code>-Jz</code>|<code>Z</code><i>parameters</i></p>
<dd> Set z-axis scaling; same syntax as <code>-Jx</code>.</p>
<dt><code>-K</code></p>
<dd> More PostScript code will be appended later [Default terminates the plot system]. Required for all but the last plot command when building multi-layer plots.</p>
<dt><code>-O</code></p>
<dd> Selects Overlay plot mode [Default initializes a new plot system]. Required for all but the first plot command when building multi-layer plots.</p>
<dt><code>-P</code></p>
<dd> Select &quot;Portrait&quot; plot orientation [Default is &quot;Landscape&quot;; see <code>gmt.conf</code> or <code>gmtset</code> to change the <code>PS_PAGE_ORIENTATION</code> parameter, or supply <code>&#8211;</code><code>-PS_PAGE_ORIENTATION=</code><i>orientation</i> on the command line].</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>]</p>
<dd> <i>xmin</i>, <i>xmax</i>, <i>ymin</i>, and <i>ymax</i> specify the region of interest. For geographic regions, these limits correspond to <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> and you may specify them in decimal degrees or in [<code>+-</code>]<i>dd</i><code>:</code><i>mm</i>[<code>:</code><i>ss.xxx</i>][<code>W</code>|<code>E</code>|<code>S</code>|<code>N</code>] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of <i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>-R</code><i>code</i><i>x0</i>/<i>y0</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of <code>L</code>, <code>C</code>, <code>R</code> (for left, center, or right) and <code>T</code>, <code>M</code>, <code>B</code> for top, middle, or bottom. e.g., <code>BL</code> for lower left. This indicates which point on a rectangular region the <i>x0</i>/<i>y0</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. When <code>-R</code> is used without any further arguments, the values from the last use of <code>-R</code> in a previous GMT command will be used. For calendar time coordinates you may either give (a) relative time (relative to the selected <i>TIME_EPOCH</i> and in the selected <i>TIME_UNIT</i>; append <code>t</code> to <code>-JX</code>|<code>x</code>), or (b) absolute time of the form [<i>date</i>]<code>T</code>[<i>clock</i>] (append <code>T</code> to <code>-JX</code>|<code>x</code>). At least one of <i>date</i> and <i>clock</i> must be present; the <code>T</code> is always required. The <i>date</i> string must be of the form [<code>&#8211;</code>]<i>yyyy</i>[<code>&#8211;</code><i>mm</i>[<code>&#8211;</code><i>dd</i>]] (Gregorian calendar) or <i>yyyy</i>[<code>-W</code><i>ww</i>[<code>&#8211;</code><i>d</i>]] (ISO week calendar), while the <i>clock</i> string must be of the form <i>hh</i><code>:</code><i>mm</i><code>:</code><i>ss</i>[<i>.xxx</i>]. The use of delimiters and their type and positions must be exactly as indicated (however, input, output and plot formats are customizable; see <code>gmt.conf</code>). You can also use Cartesian projected coordinates compatible with the chosen projection. Give them with a leading length <i>unit</i>, (e.g., <code>-Rk</code>-200/200/-300/300 for a 400 by 600 km rectangular area centered on the projection center (0, 0). These coordinates are internally converted to the corresponding geographic (longitude, latitude) coordinates for the lower left and upper right corners. This form is convenient when you want to specify a region directly in the projected units (e.g., UTM meters). </p>
<p> In case of perspective view <code>p</code>, a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>Jz</code> option, not when using only the <code>p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension.</p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>]</p>
<dd> Draw Unix System time stamp on plot. By adding <i>just/dx/dy/</i>, the user may specify the justification of the stamp and where the stamp should fall on the page relative to lower left corner of the plot. For example, BL/0/0 will align the lower left corner of the time stamp with the lower left corner of the plot. Optionally, append a <i>label</i>, or <code>c</code> (which will plot the command string.). The GMT parameters <i>MAP_LOGO</i>, <i>MAP_LOGO_POS</i>, and <i>FORMAT_TIME_STAMP</i> can affect the appearance; see the <code>gmt.conf</code> man page for details. The time string will be in the locale set by the environment variable <code>TZ</code> (generally local time).</p>
<dt><code>-V</code>[<i>level</i>]</p>
<dd> Select verbose mode, which will send progress reports to <i>stderr</i>. Choose among 6 levels of verbosity; each level adds mode messages: <code>q</code> &#8211; Complete silence, not even fatal error messages are produced. <code>n</code> &#8211; Normal verbosity: produce only fatal error messages. <code>c</code> &#8211; Produce also compatibility warnings (same as when <code>-V</code> is omitted). <code>v</code> &#8211; Produce also warnings and progress messages (same as <code>-V</code> only). <code>l</code> &#8211; Produce also detailed progress messages. <code>d</code> &#8211; Produce also debugging messages. </p>
<p> <code>-X</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>x-shift</i>[<code>u</code>]]</p>
<dt><code>-Y</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>y-shift</i>[<code>u</code>]]</p>
<dd> Shift plot origin relative to the current origin by (<i>x-shift</i>,<i>y-shift</i>) and optionally append the length unit (<code>c</code>, <code>i</code>, or <code>p</code>). You can prepend <code>a</code> to shift the origin back to the original position after plotting, prepend <code>c</code> to center the plot on the center of the paper (optionally add shift), prepend <code>f</code> to shift the origin relative to the fixed lower left corner of the page, or prepend <code>r</code> [Default] to move the origin relative to its current location. If <code>-O</code> is used then the default (<i>x-shift</i>,<i>y-shift</i>) is (r0), otherwise it is (r1i). When <code>-X</code> or <code>-Y</code> are used without any further arguments, the values from the last use of that option in a previous GMT command will be used.</p>
<dt><code>-a</code>[<i>col</i>=]<i>name</i>[<i>&#8230;</i>]</p>
<dd> Control how aspatial data are handled in GMT during input and output. <i>Reading OGR/GMT-formatted files</i>: To assign certain aspatial data items to GMT data columns, give one or more comma-separated associations <i>col</i>=<i>name</i>, where <i>name</i> is the name of an aspatial attribute field in a OGR/GMT file and whose value we wish to as data input for column <i>col</i>. In addition, to assign an aspatial value to non-column data, you may specify <i>col</i> as <code>D</code> for <i>distance</i>, <code>G</code> for <i>fill</i>, <code>I</code> for <i>ID</i>, <code>L</code> for <i>label</i>, <code>T</code> for <i>text</i>, <code>W</code> for <i>pen</i>, and <code>Z</code> for <i>value</i> [e.g., used to look-up color via a CPT]. If you skip the leading &quot;<i>col</i>=&quot; in the argument then we supply (and automatically increment) a column value starting at 2. <i>Writing OGR/GMT-formatted files</i>: Give one or more comma-separated associations <i>col</i>=<i>name</i>[:<i>type</i>], To write OGR/GMT-formatted files, give one or more comma-separated associations <i>col</i>=<i>name</i>[:<i>type</i>], with an optional data type from DOUBLE, FLOAT, INTEGER, CHAR, STRING, DATETIME, or LOGICAL [DOUBLE]. To extract information from GMT multisegment headers encoded in the <code>-D</code><i>distance</i>, <code>-G</code><i>fill</i>, <code>-I</code><i>ID</i>, <code>-L</code><i>label</i>, <code>-T</code><i>text</i>, <code>-W</code><i>pen</i>, or <code>-Z</code><i>value</i> settings, specify <i>COL</i> as <code>D</code>, <code>G</code>, <code>I</code>, <code>L</code>, <code>T</code>, <code>W</code> or <code>Z</code>, respectively; type will be set automatically. Finally, you <i>must</i> append <code>+g</code><i>geometry</i>, where <i>geometry</i> is either POINT, LINE, or POLY. Optionally, prepend <code>M</code> for multi-versions of these geometries. To force the clipping of features crossing the Dateline, use upper-case <code>+G</code> instead. See GMT Appendix Q for details of the OGR/GMT file format.</p>
<dt><code>-bi</code>[<i>ncols</i>][<i>type</i>][w][<code>+L</code>|<code>+B</code>]</p>
<dd> Select native binary input. Here, <i>ncols</i> is the number of data columns of given type and <code>t</code> must be one of <code>c</code> (int8_t, aka char), <code>u</code> (uint8_t, aka unsigned char), <code>h</code> (int16_t, 2-byte signed int), <code>H</code> (uint16_t, 2-byte unsigned int), <code>i</code> (int32_t, 4-byte signed int), <code>I</code> ((capital i) uint32_t, 4-byte unsigned int), <code>l</code> ((lower case el) int64_t, 8-byte signed int), <code>L</code> (uint64_t, 8-byte unsigned int), <code>f</code> (4-byte single-precision float), and <code>d</code> (8-byte double-precision float). In addition, use <code>x</code> to skip <i>ncols</i> bytes anywhere in the record. For records with mixed types, simply append additional comma-separated combinations of <i>ncols</i><code>t</code>. Append <code>w</code> to any item to force byte-swapping. Alternatively, append <code>+L</code>|<code>B</code> to indicate that the entire data file should be read as little- or big-endian, respectively. The cumulative number of <i>ncols</i> may exceed the columns actually needed by the program. If <i>ncols</i> is not specified we assume that <code>t</code> applies to all columns and that <i>ncols</i> is implied by the expectation of the program. If the input file is netCDF, no <code>-b</code> is needed; simply append <code>?</code><i>var1</i><code>/</code><i>var2</i><code>/</code><i>&#8230;</i> to the filename to specify the variables to be read.</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>][w][<code>+L</code>|<code>+B</code>]</p>
<dd> Select native binary output. Here, <i>ncols</i> is the actual number of data columns of type <code>t</code>, which must be one of <code>c</code>, <code>u</code>, <code>h</code>, <code>H</code>, <code>i</code>, <code>I</code> (capital i), <code>l</code> (lower case elle), <code>L</code>, <code>f</code>, and <code>d</code> (see <code>-bi</code>). For a mixed-type output record, append additional comma-separated combinations of <i>ncols</i>/<code>t</code>. Append <code>w</code> to any item to force byte-swapping or <code>+L</code>|<code>B</code> for byte-swapping of the entire record. If <i>ncols</i> is not specified we assume that <code>t</code> applies to all columns and that <i>ncols</i> is implied by the default output of the program. Note: NetCDF file output is not supported.</p>
<dt><code>-c</code><i>copies</i></p>
<dd> Specify number of plot copies. [Default is 1]. When used without argument, use the same number of copies and specified in the last <code>-c</code> in a previous GMT command.</p>
<dt><code>-d</code>[<code>i</code>|<code>o</code>]<i>nodata</i></p>
<dd> Control how user-coded missing z data values are translated to official NaN values in GMT. For input data we replace any value that equals <i>nodata</i> with NaN. For output data we replace any NaN with the chosen <i>nodata</i> value. Use <code>-di</code> or <code>-do</code> to only affect input or output.</p>
<dt><code>-di</code><i>nodata</i></p>
<dd> Examine all input columns and if any item equals <i>nodata</i> we interpret this value as a missing data item and substitute the value NaN.</p>
<dt><code>-do</code><i>nodata</i></p>
<dd> Examine all output columns and if any item equals NAN we substitute it with the chosen missing data value <i>nodata</i>.</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i></p>
<dd> Specify the data types of input and/or output columns (time or geographical data). Specify <code>i</code> or <code>o</code> to make this apply only to input or output [Default applies to both]. Give one or more columns (or column ranges) separated by commas, or use <code>-f</code> multiple times (column ranges must be given in the format <i>start</i>[:<i>inc</i> ]:<i>stop</i>, where <i>inc</i> defaults to 1 if not specified). Append <code>T</code> (absolute calendar time), <code>t</code> (relative time in chosen <i>TIME_UNIT</i> since <i>TIME_EPOCH</i>), <code>x</code> (longitude), <code>y</code> (latitude), <code>p</code>[<i>unit</i>] (projected x,y map coordinates in given unit [meter]) or <code>f</code> (floating point) to each column or column range item. Shorthand <code>-f</code>[<code>i</code>|<code>o</code>]<code>g</code> means <code>-f</code>[<code>i</code>|<code>o</code>]0<code>x</code>,1<code>y</code> (geographic coordinates).</p>
<dt><code>-g</code>[<code>a</code>]<code>x</code>|<code>y</code>|<code>d</code>|<code>X</code>|<code>Y</code>|<code>D</code>|[<i>col</i>]<code>z</code>[+|-]<i>gap</i>[<code>u</code>]</p>
<dd> Examine the spacing between consecutive data points in order to impose breaks in the line. Append <code>x</code>|<code>X</code> or <code>y</code>|<code>Y</code> to define a gap when there is a large enough change in the x or y coordinates, respectively, or <code>d</code>|<code>D</code> for distance gaps; use upper case to calculate gaps from projected coordinates. For gap-testing on other columns use [<i>col</i>]<code>z</code>; if <i>col</i> is not prepended the it defaults to 2 (i.e., 3rd column). Append [+|-]<i>gap</i> and optionally a unit <code>u</code>. Regarding optional signs: -ve means previous minus current column value must exceed <i>gap</i> to be a gap, +ve means current minus previous column value must exceed <i>gap</i>, and no sign means the absolute value of the difference must exceed <i>gap</i>. For geographic data (<code>x</code>|<code>y</code>|<code>d</code>), the unit <code>u</code> may be arc <code>d</code>egree, <code>m</code>inute, or <code>s</code>econd, or m<code>e</code>ter [Default], <code>f</code>oot, <code>k</code>ilometer, <code>M</code>ile, <code>n</code>autical mile, or s<code>u</code>rvey foot. For projected data (<code>X</code>|<code>Y</code>|<code>D</code>), choose from <code>i</code>nch, <code>c</code>entimeter, or <code>p</code>oint [Default unit set by <i>PROJ_LENGTH_UNIT</i>]. Note: For <code>x</code>|<code>y</code>|<code>z</code> with time data the unit is instead controlled by <i>TIME_UNIT</i>. Repeat the option to specify multiple criteria, of which any can be met to produce a line break. Issue an additional <code>-ga</code> to indicate that all criteria must be met instead.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+t</code><i>title</i>]</p>
<dd> Input file(s) has header record(s). If used, the default number of header records is <i>IO_N_HEADER_RECS</i> [1]. Use <code>-hi</code> if only input data should have header records [Default will write out header records if the input data have them]. Blank lines and lines starting with # are always skipped. For output you may request additional headers to be written via the option modifiers, and use <code>+d</code> to remove existing header records. Append <code>+c</code> to issue a header comment with column names to the output [none]. Append <code>+r</code> to add a <i>remark</i> comment to the output [none]. Append <code>+t</code> to add a <i>title</i> comment to the output [none]. These optional strings may contain n to indicate line-breaks). If used with native binary data we interpret <i>n</i> to instead mean the number of bytes to skip on input or pad on output.</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>]</p>
<dd> Select specific data columns for input, in arbitrary order. Columns not listed will be skipped. Give individual columns (or column ranges in the format <i>start</i>[:<i>inc</i> ]:<i>stop</i>, where <i>inc</i> defaults to 1 if not specified) separated by commas [Default reads all columns in order, starting with the first column (0)]. Columns may not be repeated. To each column, optionally add any of the following, in this order: <code>l</code> takes the <code>log10</code> of the input values first; <code>s</code><i>scale</i>, subsequently multiplies by a given scale factor; <code>o</code><i>offset</i>, finally adds a given offset.</p>
<dt><code>-n</code>[<code>b</code>|<code>c</code>|<code>l</code>|<code>n</code>][<code>+a</code>][<code>+b</code><i>BC</i>][<code>+c</code>][<code>+t</code><i>threshold</i>]</p>
<dd> Select grid interpolation mode by adding <code>b</code> for B-spline smoothing, <code>c</code> for bicubic interpolation, <code>l</code> for bilinear interpolation, or <code>n</code> for nearest-neighbor value (for example to plot categorical data). Optionally, append <code>+a</code> to switch off antialiasing (where supported). Append <code>+b</code><i>BC</i> to override the boundary conditions used, adding <code>g</code> for geographic, <code>p</code> for periodic, or <code>n</code> for natural boundary conditions. For the latter two you may append <code>x</code> or <code>y</code> to specify just one direction, otherwise both are assumed. Append <code>+c</code> to clip the interpolated grid to input z-min/max [Default may exceed limits]. Add append <code>+t</code><i>threshold</i> to control how close to nodes with NaNs the interpolation will go. A <i>threshold</i> of 1.0 requires all (4 or 16) nodes involved in interpolation to be non-NaN. 0.5 will interpolate about half way from a non-NaN value; 0.1 will go about 90% of the way, etc. [Default is bicubic interpolation with antialiasing and a threshold of 0.5, using geographic (if grid is known to be geographic) or natural boundary conditions].</p>
<dt><code>-o</code><i>cols</i>[,&#8230;]</p>
<dd> Select specific data columns for output, in arbitrary order. Columns not listed will be skipped. Give columns (or column ranges in the format <i>start</i>[:<i>inc</i> ]:<i>stop</i>, where <i>inc</i> defaults to 1 if not specified) separated by commas. Columns may be repeated. [Default writes all columns in order].</p>
<dt><code>-p</code>[<code>x</code>|<code>y</code>|<code>z</code>]<i>azim</i>/<i>elev</i>[/<i>zlevel</i>][<code>+w</code><i>lon0</i>/<i>lat0</i>[/<i>z0</i>]][<code>+v</code><i>x0</i>/<i>y0</i>]</p>
<dd> Selects perspective view and sets the azimuth and elevation of the viewpoint [180/90]. When <code>-p</code> is used in consort with <code>-Jz</code> or <code>-JZ</code>, a third value can be appended which indicates at which z-level all 2D material, like the plot frame, is plotted (in perspective). [Default is at the bottom of the z-axis]. Use <code>-px</code> or <code>-py</code> to plot against the &quot;wall&quot; x = level or y = level (default is on the horizontal plane, which is the same as using <code>-pz</code>). For frames used for animation, you may want to append <code>+</code> to fix the center of your data domain (or specify a particular world coordinate point with <code>+w</code><i>lon0</i>/<i>lat</i>[/<i>z</i>]) which will project to the center of your page size (or specify the coordinates of the projected view point with <code>+v</code><i>x0</i>/<i>y0</i>. When <code>-p</code> is used without any further arguments, the values from the last use of <code>-p</code> in a previous GMT command will be used.</p>
<dt><code>-r</code></p>
<dd> Force pixel node registration [Default is gridline registration]. (Node registrations are defined in Section <i>grid-registration</i> of the GMT Technical Reference and Cookbook.)</p>
<dt><code>-s</code>[<i>cols</i>][<code>a</code>|<code>r</code>]</p>
<dd> Suppress output for records whose <i>z</i>-value equals NaN [Default outputs all records]. Append <code>a</code> to skip records where at least one field equal NaN. Append <code>r</code> to reverse the suppression, i.e., only output the records whose <i>z</i>-value equals NaN. Alternatively, indicate a comma-separated list of all columns or column ranges to consider for this NaN test (Column ranges must be given in the format <i>start</i>[:<i>inc</i> ]:<i>stop</i>, where <i>inc</i> defaults to 1 if not specified).</p>
<dt><code>-t</code>[<i>transp</i>]</p>
<dd> Set PDF transparency level for an overlay, in 0-100 percent range. [Default is 0, i.e., opaque].</p>
<dt><code>-x</code>[[-]<i>n</i>]</p>
<dd> Limit the number of cores to be used in any OpenMP-enabled multi-threaded algorithms. By default we try to use all available cores. Append <i>n</i> to only use <i>n</i> cores (if too large it will be truncated to the maximum cores available). Finally, give a negative <i>n</i> to select (all &#8211; <i>n</i>) cores (or at least 1 if <i>n equals or exceeds all). The *</i>-x** option is only available to GMT modules compiled with OpenMP support.</p>
<dt><code>-:</code>[<code>i</code>|<code>o</code>]</p>
<dd> Swap 1st and 2nd column on input and/or output [Default is no swapping]. Append <code>i</code> to select input only or <code>o</code> to select output only. [Default affects both]. This option is typically used to handle (latitude, longitude) files; see also <code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>].</p>
<dt><code>-^</code> or just <code>&#8211;</code></p>
<dd> Print a short message about the syntax of the command, then exits (NOTE: on Windows use just <code>&#8211;</code>).</p>
<dt><code>-+</code> or just <code>+</code></p>
<dd> Print an extensive usage (help) message, including the explanation of any module-specific option (but not the GMT common options), then exits.</p>
<dt><code>-?</code> or no arguments</p>
<dd> Print a complete usage (help) message, including the explanation of options, then exits.</p>
<dt><code>&#8211;</code><code>-version</code></p>
<dd> Print GMT version and exit.</p>
<dt><code>&#8211;</code><code>-show-datadir</code></p>
<dd> Print full path to GMT share directory and exit.</dl>
<h3><i>Specifying Color</i></h3>
<dl>
<dt><i>color</i></p>
<dd> The <i>color</i> of lines, areas and patterns can be specified by a valid color name; by a gray shade (in the range 0-255); by a decimal color code (r/g/b, each in range 0-255; h-s-v, ranges 0-360, 0-1, 0-1; or c/m/y/k, each in range 0-1); or by a hexadecimal color code (#rrggbb, as used in HTML). For PDF transparency, append @<i>transparency</i> in the 0-100 percent range [0 or opaque]. See the <code>gmtcolors</code> for more information and a full list of color names. See GMT Cookbook &amp; Technical Reference Chapter 4 for more information.</dl>
<h3><i>Specifying Fill</i></h3>
<dl>
<dt><i>fill</i></p>
<dd> The attribute <i>fill</i> specifies the solid shade or solid <i>color</i> (see <i>Specifying Color</i> above) or the pattern used for filling polygons. Patterns are specified as <code>p</code><i>dpi/pattern</i>, where <i>pattern</i> gives the number of the built-in pattern (1-90) <i>or</i> the name of a Sun 1-, 8-, or 24-bit raster file. The <i>dpi</i> sets the resolution of the image. For 1-bit rasters: use <code>P</code><i>dpi/pattern</i> for inverse video, or append <code>:F</code><i>color</i>[<code>B</code>[<i>color</i>]] to specify fore- and background colors (use <i>color</i> = &#8211; for transparency). See GMT Cookbook &amp; Technical Reference Appendix E for information on individual patterns.</dl>
<h3><i>Specifying Fonts</i></h3>
<dl>
<dt><i>font</i></p>
<dd> The attributes of text fonts as defined by <i>font</i> is a comma delimited list of <i>size</i>, <i>fonttype</i> and <i>fill</i>, each of which is optional. <i>size</i> is the font size (usually in points) but <code>c</code> or <code>i</code> can be added to indicate other units. <i>fonttype</i> is the name (case sensitive!) of the font or its equivalent numerical ID (e.g., Helvetica-Bold or 1). <i>fill</i> specifies the gray shade, color or pattern of the text (see <i>Specifying Fill</i> above). Optionally, you may append <code>=</code><i>pen</i> to the <i>fill</i> value in order to draw a text outline. If you want to avoid that the outline partially obscures the text, append append <code>=~</code><i>pen</i> instead; in that case only half the linewidth is plotted on the outside of the font only. If an outline is requested, you may optionally skip the text <i>fill</i> by setting it to <code>&#8211;</code>, in which case the full pen width is always used. If any of the font attributes is omitted their default or previous setting will be retained. </p>
<p> The 35 available fonts are:</p>
<dt>0.</p>
<dd> Helvetica</p>
<dt>1.</p>
<dd> Helvetica-Bold</p>
<dt>2.</p>
<dd> Helvetica-Oblique</p>
<dt>3.</p>
<dd> Helvetica-BoldOblique</p>
<dt>4.</p>
<dd> Times-Roman</p>
<dt>5.</p>
<dd> Times-Bold</p>
<dt>6.</p>
<dd> Times-Italic</p>
<dt>7.</p>
<dd> Times-BoldItalic</p>
<dt>8.</p>
<dd> Courier</p>
<dt>9.</p>
<dd> Courier-Bold</p>
<dt>10.</p>
<dd> Courier-Oblique</p>
<dt>11.</p>
<dd> Courier-BoldOblique</p>
<dt>12.</p>
<dd> Symbol</p>
<dt>13.</p>
<dd> AvantGarde-Book</p>
<dt>14.</p>
<dd> AvantGarde-BookOblique</p>
<dt>15.</p>
<dd> AvantGarde-Demi</p>
<dt>16.</p>
<dd> AvantGarde-DemiOblique</p>
<dt>17.</p>
<dd> Bookman-Demi</p>
<dt>18.</p>
<dd> Bookman-DemiItalic</p>
<dt>19.</p>
<dd> Bookman-Light</p>
<dt>20.</p>
<dd> Bookman-LightItalic</p>
<dt>21.</p>
<dd> Helvetica-Narrow</p>
<dt>22.</p>
<dd> Helvetica-Narrow-Bold</p>
<dt>23.</p>
<dd> Helvetica-Narrow-Oblique</p>
<dt>24.</p>
<dd> Helvetica-Narrow-BoldOblique</p>
<dt>25.</p>
<dd> NewCenturySchlbk-Roman</p>
<dt>26.</p>
<dd> NewCenturySchlbk-Italic</p>
<dt>27.</p>
<dd> NewCenturySchlbk-Bold</p>
<dt>28.</p>
<dd> NewCenturySchlbk-BoldItalic</p>
<dt>29.</p>
<dd> Palatino-Roman</p>
<dt>30.</p>
<dd> Palatino-Italic</p>
<dt>31.</p>
<dd> Palatino-Bold</p>
<dt>32.</p>
<dd> Palatino-BoldItalic</p>
<dt>33.</p>
<dd> ZapfChancery-MediumItalic</p>
<dt>34.</p>
<dd> ZapfDingbats</dl>
<h3>Specifying Pens</h3>
<dl>
<dt><i>pen</i></p>
<dd> The attributes of lines and symbol outlines as defined by <i>pen</i> is a comma-delimited list of <i>width</i>, <i>color</i> and <i>style</i>, each of which is optional. <i>width</i> can be indicated as a measure (in <code>p</code>oints (this is the default), <code>c</code>entimeters, or <code>i</code>nches) or as <code>faint</code>, <code>default</code>, <code>thin</code>[<code>ner</code>|<code>nest</code>], <code>thick</code>[<code>er</code>|<code>est</code>], <code>fat</code>[<code>ter</code>|<code>test</code>], or <code>obese</code>. <i>color</i> specifies a gray shade or color (see <i>Specifying Color</i> above). <i>style</i> is a combination of dashes &#8216;-&#8216; and dots &#8216;.&#8217;. If any of the attributes is omitted their default or previous setting will be retained. See GMT Cookbook &amp; Technical Reference Chapter 4 for more information.</dl>
<h2>ASCII FORMAT PRECISION</h2>
<p> The ASCII output formats of numerical data are controlled by parameters in your <code>gmt.conf</code> file. Longitude and latitude are formatted according to <i>FORMAT_GEO_OUT</i>, whereas other values are formatted according to <i>FORMAT_FLOAT_OUT</i>. Be aware that the format in effect can lead to loss of precision in the output, which can lead to various problems downstream. If you find the output is not written with enough precision, consider switching to binary output (<code>-bo</code> if available) or specify more decimals using the <i>FORMAT_FLOAT_OUT</i> setting.</p>
<h2>GRID FILE FORMATS</h2>
<p> By default GMT writes out grid as single precision floats in a COARDS-complaint netCDF file format. However, GMT is able to produce grid files in many other commonly used grid file formats and also facilitates so called &quot;packing&quot; of grids, writing out floating point data as 1- or 2-byte integers. To specify the precision, scale and offset, the user should add the suffix <code>=</code><i>id</i>[<code>/</code><i>scale</i><code>/</code><i>offset</i>[<code>/</code><i>nan</i>]], where <i>id</i> is a two-letter identifier of the grid type and precision, and <i>scale</i> and <i>offset</i> are optional scale factor and offset to be applied to all grid values, and <i>nan</i> is the value used to indicate missing data. In case the two characters <i>id</i> is not provided, as in <code>=/</code><i>scale</i> than a <i>id</i><code>=</code><i>nf</i> is assumed. When reading grids, the format is generally automatically recognized. If not, the same suffix can be added to input grid file names. See <code>grdconvert</code> and Section <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information. </p>
<p> When reading a netCDF file that contains multiple grids, GMT will read, by default, the first 2-dimensional grid that can find in that file. To coax GMT into reading another multi-dimensional variable in the grid file, append <code>?</code><i>varname</i> to the file name, where <i>varname</i> is the name of the variable. Note that you may need to escape the special meaning of <code>?</code> in your shell program by putting a backslash in front of it, or by placing the filename and suffix between quotes or double quotes. The <code>?</code><i>varname</i> suffix can also be used for output grids to specify a variable name different from the default: &quot;z&quot;. See <code>grdconvert</code> and Sections <i>modifiers-for-CF</i> and <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information, particularly on how to read splices of 3-, 4-, or 5-dimensional grids.</p>
<h2>SEE ALSO</h2>
<p> Look up the individual man pages for more details and full syntax. Run <code>gmt &#8211;help</code> to list all GMT programs and to show all installation directories. For an explanation of the various GMT settings in this man page (like <i>FORMAT_FLOAT_OUT</i>), see the man page of the GMT configuration file <code>gmt.conf</code>. Information is also available on the GMT home page <i><a rel="nofollow" href="http://gmt.soest.hawaii.edu/">http://gmt.soest.hawaii.edu/</a></i></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
<dt><a href="#lbAN">ASCII FORMAT PRECISION</a></p>
<dd>
<dt><a href="#lbAO">GRID FILE FORMATS</a></p>
<dd>
<dt><a href="#lbAP">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAQ">COPYRIGHT</a></p>
<dd></dl>
