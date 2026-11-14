---
title: "dvipost(1)"
name: "dvipost"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvipost/"
description: "dvipost, pptex, pplatex – post processing of dvi files"
---

<h2>NAME</h2>
<p> dvipost, pptex, pplatex &#8211; post processing of dvi files </p>
<h2>SYNOPSIS</h2>
<p> <code>dvipost</code> [<code>-debug</code>] [<code>-version</code>] [<code>-help</code>] <i>in</i> <i>out</i> </p>
<p> <code>pplatex</code> [<code>-debug</code>] [<code>-version</code>] [<code>-help</code>] [LaTeX-Arguments] </p>
<p> <code>pptex</code> [<code>-debug</code>] [<code>-version</code>] [<code>-help</code>] [TeX-Arguments] </p>
<h2>DESCRIPTION</h2>
<p> The command <code>dvipost</code> is a post procesor for dvi files, created by <code>latex</code> or <code>tex</code>. It is used for special modes, which normally needs the support of dvi drivers (such as <code>dvips</code>). With <code>dvipost</code>, this features could be implemented independent of the prefered driver. Currently, the post processor supports layout raster, change bars and overstrike mode. </p>
<p> This version of <code>dvipost</code> does not seek the dvi file, so it could be used as a filter. If <code>&#8211;</code> is given as file name, the command uses standard input or standard output respective. The command does not substitute a missing <code>.dvi</code> extension to the filename. </p>
<p> Because the command works with a temporary file and creates the ouput file only after successfull processing the input file, it is possible to use the same name for input and output. </p>
<p> If the command is renamed or linked to <code>pplatex</code>/<code>pptex</code>, it runs <code>latex</code>/<code>tex</code> and post processes the createt output. If the name of the dvi file could not be determined by the arguments to <code>latex</code>/<code>tex</code> (e.g. on an interactive run), the command processes all dvi files in the current directory with a modification time later than the run of <code>latex</code>/<code>tex</code>. </p>
<h3>Basics</h3>
<p> If the filter is used in context of LaTeX, the style file <code>dvipost.sty</code> should be included in the LaTeX source. </p>
<p> The filter interpretes dvi extensions in the form of</p>
<dl>
<dt>
<dd> <code>dvipost:</code> <i>name</i> [<i>arg</i>]</dl>
<p> where <i>arg</i> depends on the command <i>name</i> and may be separated from <i>name</i> by <code>=</code> or space. All other extensions are not interpreted by <code>dvipost</code> and remain in the dvi file. </p>
<p> Such a dvipost command could be placed with the TeX primitive</p>
<dl>
<dt>
<dd> <code>\special{dvipost:</code> <i>cmd</i><code>}</code></dl>
<p> or the LaTeX macro (provided by <code>dvipost.sty</code>)</p>
<dl>
<dt>
<dd> <code>\dvipost{</code><i>cmd</i><code>}</code></dl>
<p> in the dvi file. </p>
<p> Depending on the type of <code>dvipost</code> commands, the following kinds of arguments may be used:</p>
<dl>
<dt><i>length</i></p>
<dd> is a floating point number followed by a unit specification. The following units are supportet by <code>divipost</code>: <code>pt</code>, <code>in</code>, <code>cm</code> and <code>mm</code>. If no argument is given or the unit specification is missing, the corresponding <i>length</i> is set to 0.</p>
<dt><i>string</i></p>
<dd> is an arbitrary string argument.</p>
<dt><i>flag</i></p>
<dd> is an integer argument, where a value different from 0 (usually 1) means true and a missing value or 0 means false.</p>
<dt><i>depth</i></p>
<dd> is an integer argument, where a value different from 0 (usually 1) increments a depth counter and a missing value or 0 decrements it.</dl>
<h3>Change bars</h3>
<p> All text printed with change mode level higher than 0 is marked with a change bar. </p>
<p> The following LaTeX macros modifies the change mode level: </p>
<dl>
<dt><code>
