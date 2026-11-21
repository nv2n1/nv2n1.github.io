---
title: "dvipost(1)"
name: "dvipost"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvipost/"
description: "dvipost, pptex, pplatex – post processing of dvi files"
---
<h2>NAME</h2>
<p> dvipost, pptex, pplatex - post processing of dvi files </p>
<h2>SYNOPSIS</h2>
<p> <code>dvipost</code> [<code>-debug</code>] [<code>-version</code>] [<code>-help</code>] <i>in</i> <i>out</i> </p>
<p> <code>pplatex</code> [<code>-debug</code>] [<code>-version</code>] [<code>-help</code>] [LaTeX-Arguments] </p>
<p> <code>pptex</code> [<code>-debug</code>] [<code>-version</code>] [<code>-help</code>] [TeX-Arguments] </p>
<h2>DESCRIPTION</h2>
<p> The command <code>dvipost</code> is a post procesor for dvi files, created by <code>latex</code> or <code>tex</code>. It is used for special modes, which normally needs the support of dvi drivers (such as <code>dvips</code>). With <code>dvipost</code>, this features could be implemented independent of the prefered driver. Currently, the post processor supports layout raster, change bars and overstrike mode. </p>
<p> This version of <code>dvipost</code> does not seek the dvi file, so it could be used as a filter. If <code>-</code> is given as file name, the command uses standard input or standard output respective. The command does not substitute a missing <code>.dvi</code> extension to the filename. </p>
<p> Because the command works with a temporary file and creates the ouput file only after successfull processing the input file, it is possible to use the same name for input and output. </p>
<p> If the command is renamed or linked to <code>pplatex</code>/<code>pptex</code>, it runs <code>latex</code>/<code>tex</code> and post processes the createt output. If the name of the dvi file could not be determined by the arguments to <code>latex</code>/<code>tex</code> (e.g. on an interactive run), the command processes all dvi files in the current directory with a modification time later than the run of <code>latex</code>/<code>tex</code>. </p>
<h3>Basics</h3>
<p> If the filter is used in context of LaTeX, the style file <code>dvipost.sty</code> should be included in the LaTeX source. </p>
<p> The filter interpretes dvi extensions in the form of </p>
<dl>
<dd> <p> <code>dvipost:</code> <i>name</i> [<i>arg</i>] </p>
 </dd></dl>
<p> where <i>arg</i> depends on the command <i>name</i> and may be separated from <i>name</i> by <code>=</code> or space. All other extensions are not interpreted by <code>dvipost</code> and remain in the dvi file. </p>
<p> Such a dvipost command could be placed with the TeX primitive </p>
<dl>
<dd> <p> <code>\special{dvipost:</code> <i>cmd</i><code>}</code> </p>
 </dd></dl>
<p> or the LaTeX macro (provided by <code>dvipost.sty</code>) </p>
<dl>
<dd> <p> <code>\dvipost{</code><i>cmd</i><code>}</code> </p>
 </dd></dl>
<p> in the dvi file. </p>
<p> Depending on the type of <code>dvipost</code> commands, the following kinds of arguments may be used: </p>
<dl>
<dt><i>length</i></dt>
<dd> <p> is a floating point number followed by a unit specification. The following units are supportet by <code>divipost</code>: <code>pt</code>, <code>in</code>, <code>cm</code> and <code>mm</code>. If no argument is given or the unit specification is missing, the corresponding <i>length</i> is set to 0. </p>
 </dd>
<dt><i>string</i></dt>
<dd> <p> is an arbitrary string argument. </p>
 </dd>
<dt><i>flag</i></dt>
<dd> <p> is an integer argument, where a value different from 0 (usually 1) means true and a missing value or 0 means false. </p>
 </dd>
<dt><i>depth</i></dt>
<dd> <p> is an integer argument, where a value different from 0 (usually 1) increments a depth counter and a missing value or 0 decrements it. </p>
 </dd></dl>
<h3>Change bars</h3>
<p> All text printed with change mode level higher than 0 is marked with a change bar. </p>
<p> The following LaTeX macros modifies the change mode level: </p>
<dl>
<dt><code>\changestart</code></dt>
<dd> <p> increments the change mode level. </p>
 </dd>
<dt><code>\changeend</code></dt>
<dd> <p> decrements the change mode level. </p>
 </dd>
<dt><code>\textchanged{</code><i>text</i><code>}</code></dt>
<dd> <p> increments the change mode level for <i>text</i> only. </p>
 </dd></dl>
<p> The following <code>dvipost</code> commands are used in context of change bars: </p>
<dl>
<dt><code>cbmode </code><i>depth</i></dt>
<dd> <p> increments/decrements the change mode level. This command is used by the LaTeX macros. </p>
 </dd>
<dt><code>cbrule </code><i>length</i></dt>
<dd> <p> determines the thickness of the change bar. The default value is 2pt. </p>
 </dd>
<dt><code>cbsep </code><i>length</i></dt>
<dd> <p> sets the distance beetween page margin and change bar. The default value is 2pt. </p>
 </dd>
<dt><code>cbexp </code><i>length</i></dt>
<dd> <p> sets the additional height and depth of a character in calculating the change bar positions. The default value is 6pt. </p>
 </dd>
<dt><code>cbstart </code><i>string</i></dt>
<dd> <p> places the dvi extension <i>string</i> before printing characters in change mode. </p>
 </dd>
<dt><code>cbend </code><i>string</i></dt>
<dd> <p> places the dvi extension <i>string</i> after printing characters in change mode. </p>
 </dd></dl>
<p> The use of <code>cbstart</code> and <code>cbend</code> allows to set additional attributes to the marked text, depending on the dvi driver. </p>
<p> If <code>dvips</code> is used as dvi driver and the preamble of the LaTeX source contains </p>
<dl>
<dd> <p> <code>\usepackage{dvipost}</code> <br />
 <code>\dvipost{cbstart color push Blue}</code> <br />
 <code>\dvipost{cbend color pop}</code> </p>
 </dd></dl>
<p> the marked text is colored blue. </p>
<h3>Overstrike mode</h3>
<p> All text printed with overstrike level higher than 0 is overstriked with a horizontal line. </p>
<p> The overstrike line is positioned at the mean height of every block of text not broken by vertical movements and font changes. </p>
<p> The following LaTeX macros modifies the overstrike level: </p>
<dl>
<dt><code>\overstrikeon</code></dt>
<dd> <p> increments the overstrike level. </p>
 </dd>
<dt><code>\overstrikeoff</code></dt>
<dd> <p> decrements the overstrike level. </p>
 </dd>
<dt><code>\overstrike{</code><i>text</i><code>}</code></dt>
<dd> <p> increments the overstrike level for <i>text</i> only. </p>
 </dd></dl>
<p> The following <code>dvipost</code> commands are used in context of overstrike mode: </p>
<dl>
<dt><code>osmode </code><i>depth</i></dt>
<dd> <p> increments/decrements the overstrike level. This command is used by the LaTeX macros. </p>
 </dd>
<dt><code>osrule </code><i>length</i></dt>
<dd> <p> sets the thickness of the overstrike line to <i>length</i>. The default value is <code>\fboxrule</code>. </p>
 </dd>
<dt><code>osstart </code><i>string</i></dt>
<dd> <p> places the dvi extension <i>string</i> before change of overstrike mode. </p>
 </dd>
<dt><code>osend </code><i>string</i></dt>
<dd> <p> places the dvi extension <i>string</i> after change of overstrike mode. </p>
 </dd></dl>
<p> The use of <code>osstart</code> and <code>osend</code> is similar to <code>cbstart</code> and <code>cbend</code>. </p>
<h3>Layout parameters</h3>
<p> Layout parameters are transfered to the dvi file on loading the style file. If any changes are made to layout parameters, like <code>\evensidemargin</code>, the macro <code>\dvipostlayout</code> must be called to get the correct placement of change bars. Additional calls to <code>\dvipostlayout</code> are harmeless. </p>
<p> The following layout parameters are transfered to the dvi file: <code>\hoffset</code>, <code>\voffset</code>, <code>\textwidth</code>, <code>\textheight</code>, <code>\oddsidemargin</code>, <code>\evensidemargin</code>, <code>\topmargin</code>, <code>\headheight</code>, <code>\headsep</code>, <code>\footskip</code>, <code>\marginparsep</code> and <code>\marginparwidth</code>. Additional the flag <code>twoside</code> is set to 0 or 1, depending on the document style option <code>twoside</code>. </p>
<p> Instead of calling <code>\dvipostlayout</code>, partciucular values could be set. The command </p>
<dl>
<dd> <p> <code>\dvipost{evensidemargin=\the\evensidemargin}</code> </p>
 </dd></dl>
<p> transfers the actual setting of <code>\evensidemargin</code> to the dvi file. </p>
<p> The <code>dvipost</code> command allows the printing of the layout raster by setting <code>layout</code> to a length different to 0. The value of <code>layout</code> is used as the thickness of the raster lines. </p>
<p> For example: The command </p>
<dl>
<dd> <p> <code>\dvipost{layout=\the\fboxrule}</code> </p>
 </dd></dl>
<p> activates the layout raster and uses the same line thicknes as frame boxes. </p>
<h2>NOTES</h2>
<p> The filter is primarly written for LaTeX. It could be used for plain TeX, but currently there is no assistance style file included in the distribution. Maybe somone would write one, I am not a plain TeX user. </p>
<p> The current state of change bar mode and overstrike mode must be committed do environments, which are placed on different locations than the current text. This is done in <code>dvipost.sty</code> by redefining <code>\color [at] begingroup</code> and <code>\color [at] endgroup</code>. This may conflict with other packages. </p>
<p> If the macro <code>\footnoterule</code> is redefined, it should start with the command <code>\dvipost{footnote}</code> for a correct handling of overstrike mode and change bars. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2002 Erich Fruehstueck </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAE">Basics</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">Change bars</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">Overstrike mode</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">Layout parameters</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAI">NOTES</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">COPYRIGHT</a></dt>
<dd>  </dd></dl>
