---
title: "hbf2gf(1)"
name: "hbf2gf"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hbf2gf/"
description: "hbf2gf – convert a CJK bitmap font into subfonts usable by TeX and Omega."
---

<h2 class="name">NAME</h2>
<p> hbf2gf &#8211; convert a CJK bitmap font into subfonts usable by TeX and Omega. </p>
<h2>SYNOPSIS</h2>
<p> <code>hbf2gf</code> [<code>-q</code>] <i>configuration-file</i>[<i>.cfg</i>]<br />
 <code>hbf2gf</code> [<code>-q</code>] [<code>-p</code>] [<code>-g</code>] [<code>-n</code>] <i>subfont-name x-resolution</i> [<i>y-scale</i>&nbsp;|<i>&nbsp;y-resolution</i>]<br />
 <code>hbf2gf</code> <code>-t</code> [<code>-q</code>] <i>subfont-name</i><br />
 <code>hbf2gf &#8211;version</code> | <code>&#8211;help</code></p>
<h2>DESCRIPTION</h2>
<p> CJK bitmap fonts can&#8217;t be directly used with TeX because the number of characters in such fonts exceeds 256, the limit of a TeX font. Thus it is necessary to split these fonts into subfonts, and this is exactly what <code>hbf2gf</code> does. </p>
<p> As the name says, <code>hbf2gf</code> uses CJK fonts in a certain format which is called <code>Hanzi Bitmap Font</code> (<code>HBF</code>) format. It simply consists of the CJK bitmap file(s) and a text file in a format very similar to the BDF format of the X Window System which describes the bitmap font files: the encoding, the size, etc. The produced files can then be converted with <code>gftopk</code> into standard files. </p>
<p> <code>hbf2gf</code> can be called in three modes: </p>
<p> <code>hbf2gf</code> [<code>-q</code>] <i>configuration-file</i>[<i>.cfg</i>] </p>
<p> This call normally creates a set of files, one file, and a batch file which must be executed after <code>hbf2gf</code> has finished. This script will then call <code>gftopk</code> to convert all files into files, and it will call <code>pltotf</code> to convert the file into a file. Finally it will copy the file so that each file has its file (which are all identical). </p>
<p> If <code>ofm_file</code> is set to &#8216;yes&#8217; in the configuration file, and files will be created too. </p>
<p> <code>-q</code> makes <code>hbf2gf</code> quiet. </p>
<p> <code>hbf2gf</code> [<code>-q</code>] [<code>-p</code>] [<code>-g</code>] [<code>-n</code>] <i>subfont-name x-resolution</i> [<i>y-scale</i>&nbsp;|<i>&nbsp;y-resolution</i>] </p>
<p> This mode is intended for use with <code>mktexpk</code> and its derivates. Only one file together with a file for the given subfont will be computed, taking the horizontal resolution and a vertical scaling factor (if the value is smaller than 10) resp. the vertical resolution (otherwise) from the command line, ignoring the <code>nmb_fonts</code> parameter of the configuration file. The last two characters (which are interpreted as the subfont number) are stripped to get the name for the configuration file (which must end with &#8216; No job file will be created. If option <code>-p</code> is set, no file is created. If <code>-g</code> is set, no file is created. The extension can be controlled with <code>-n</code>; if set, the extension is &#8216; otherwise &#8216; <i>resolution</i>&gt; <code>-q</code> makes <code>hbf2gf</code> quiet. </p>
<p> <code>hbf2gf</code> <code>-t</code> [<code>-q</code>] <i>subfont-name</i> </p>
<p> This mode is intended for use with scripts like <code>mktexpk</code>; it tests whether the specified subfont name leads to an <code>hbf2gf</code> configuration file. It returns 0 on success and prints out the name of that configuration file (provided the <code>-q</code> switch isn&#8217;t set). This test isn&#8217;t a thorough one; it only removes the last two characters and checks whether a configuration file with that name exists. </p>
<p> See the next section for more details about configuration files. </p>
<p> Specifying the option <code>&#8211;version</code> returns the current version of <code>hbf2gf</code> and the used file search library (e.g.&nbsp;<code>kpathsea</code>). Usage information is shown with the <code>&#8211;help</code> parameter.</p>
<h2>CONFIGURATION FILE</h2>
<p> Here a sample configuration file ( for a 56&#215;56 Chinese font in GB encoding; note that all information about the font is in the file. See the <code>FILE SEARCHING</code> section how HBF fonts and <code>hbf2gf</code> configuration files are found. See the <code>AVAILABILITY</code> section where to get CJK fonts together with its files: </p>
<pre>
  hbf_header     jfs56.hbf
  mag_x          1
  threshold      128
  comment        jianti fansongti 56x56 pixel font
  design_size    14.4
  y_offset       -13
  nmb_files      -1
  output_name    gsfs14
  checksum       123456789
  dpi_x          300
  pk_files       no
  tfm_files      yes
  coding         codingscheme GuoBiao encoded TeX text
  pk_directory   $HBF_TARGET/pk/modeless/gb2312/gsfs14/
  tfm_directory  $HBF_TARGET/tfm/gb2312/gsfs14/
</pre>
<p> A configuration file is a plain text file consisting of keywords and its arguments. A keyword must start a line, otherwise the whole line will be ignored. If the word starting a line is not a keyword, the line will be ignored too. Empty lines will also be skipped. The search for keywords is case insensitive; in contrast, the arguments will be taken exactly as given (except &#8216;yes&#8217; and &#8216;no&#8217; which can be written with uppercase or lowercase letters). Each keyword has one argument which must be separated by whitespace (blanks or tabs) from the keyword and must be on the same line. Each line must not be longer than 256 characters. </p>
<p> You can use environment variables in the configuration file. The escape character starting an environment variable in the configuration file is always &#8216; even for operating systems like DOS which has other conventions. <code>hbf2gf</code> recognizes only environment variable names which start with a letter or an underscore, followed by alphanumeric characters or underscores. You can surround the variable with braces to indicate where the variable name ends, for example To get a dollar sign you must write &#8216; The expansion of environment variables in hbf2gf itself (without the help of either kpathsea, emtexdir, or MiKTeX searching routines) is very limited; this feature has been carried over from previous versions. It can&#8217;t expand variables set in texmf.cnf; it also can&#8217;t handle more than one directory as the variable&#8217;s value. <code>Don&#8217;t use it except for the &#8216;pk_directory&#8217; and &#8216;tfm_directory&#8217;</code> <code>parameters!</code> </p>
<p> This is the list of all necessary keywords:</p>
<dl>
<dt><code>hbf_header</code></p>
<dd> The HBF header file name of the input font(s). <code>hbf2gf</code> uses the given searching mechanism (kpathsea, emtexdir, or MiKTeX) to locate this file.</p>
<dt><code>output_name</code></p>
<dd> The name stem of the output files. A running two digit decimal number starting with &#8216; will be appended. For Unicode fonts see the keyword <code>unicode</code> below. This value is in almost all cases identical to the name of the configuration file.</dl>
<p> And now all optional keywords:</p>
<dl>
<dt><code>x_offset</code></p>
<dd> Increases the character width. Will be applied on both sides; default for non-rotated glyphs is the value given in the HBF header (<code>HBF_BITMAP_BOUNDING_BOX</code>) scaled to <code>design_size</code> (in pixels).</p>
<dt><code>y_offset</code></p>
<dd> Shifts all characters up or down; default for non-rotated glyphs is the value given in the HBF header (<code>HBF_BITMAP_BOUNDING_BOX</code>) scaled to <code>design_size</code> (in pixels).</p>
<dt><code>design_size</code></p>
<dd> The design size (in points) of the font. <code>x_offset</code> and <code>y_offset</code> refer to this size. Default is 10.0.</p>
<dt><code>slant</code></p>
<dd> The slant of the font (given as Delta_x&nbsp;/&nbsp;Delta_y). Only values in the range 0&nbsp;&le;&nbsp;<code>slant</code>&nbsp;&le;&nbsp;1 are allowed. Default is 0.0.</p>
<dt><code>rotation</code></p>
<dd> If set to &#8216;yes&#8217;, all glyphs will be rotated 90 degrees counter-clockwise. The default offsets as given in the HBF header will be ignored (and set to 0). Default is &#8216;no&#8217;.</p>
<dt><code>mag_x</code></p>
<dd>
<dt> <code>mag_y</code></p>
<dd>Scaling values of the characters to reach design size. If only one magnification is given, x and y values are assumed to be equal. Default is <code>mag_x</code>&nbsp;=&nbsp;<code>mag_y</code>&nbsp;=&nbsp;1.0.</dl>
<dl>
<dt><code>threshold</code></p>
<dd> A value between 1 and 254 defining a threshold for converting the internal graymap into the output bitmap; lower values cut more pixels. Default value is 128.</dl>
<dl>
<dt><code>comment</code></p>
<dd> A comment describing the font; default is none.</dl>
<dl>
<dt><code>nmb_fonts</code></p>
<dd> The number of subfonts to create. Default value is -1 for creating all fonts.</p>
<dt><code>unicode</code></p>
<dd> If &#8216;yes&#8217;, a two digit hexadecimal number will be used as a running number, starting with the value of the first byte of the first code range. Default is &#8216;no&#8217;.</p>
<dt><code>min_char</code></p>
<dd> The minimum value of the encoding. You should set this value to get correct subfile offsets if it is not identical to the lowest character code in the HBF file.</dl>
<dl>
<dt><code>dpi_x</code></p>
<dd>
<dt> <code>dpi_y</code></p>
<dd>The horizontal and vertical resolution (in dpi) of the printer. If only one resolution is given, x and y values are assumed to be equal. Default is 300.</p>
<dt><code>checksum</code></p>
<dd> A checksum to identify the files with the appropriate files. The default value of this unsigned 32bit integer is 0.</p>
<dt><code>coding</code></p>
<dd> A comment describing the coding scheme; default is none.</dl>
<dl>
<dt><code>pk_directory</code></p>
<dd> The destination directory of the files; default: none. Attention! The batch file will not check whether this directory exists.</p>
<dt><code>tfm_directory</code></p>
<dd> The destination directory of the files; default: none. Attention! The batch file will not check whether this directory exists.</p>
<dt><code>pk_files</code></p>
<dd> Whether to create files or not; default is &#8216;yes&#8217;.</p>
<dt><code>tfm_files</code></p>
<dd> Whether to create files or not; default is &#8216;yes&#8217;.</p>
<dt><code>ofm_file</code></p>
<dd> Whether to create an file or not; default is &#8216;no&#8217;. The batch file will then use <code>ovp2ovf</code> of the Omega distribution to convert it into an and an file. The file simply maps all subfonts back to a single Omega font.</p>
<dt><code>long_extension</code></p>
<dd> If &#8216;yes&#8217;, files will include the resolution in the extension (e.g. This affects the batch file only (default is &#8216;yes&#8217;).</p>
<dt><code>rm_command</code></p>
<dd> The shell command to remove files; default: &#8216;rm&#8217;.</p>
<dt><code>cp_command</code></p>
<dd> The shell command to copy files; default: &#8216;cp&#8217;.</p>
<dt><code>job_extension</code></p>
<dd> The extension of the batch file which calls <code>gftopk</code> and <code>pltotf</code> to convert the and the files into and files respectively; default is none.</dl>
<h2>FILE SEARCHING</h2>
<p> <code>hbf2gf</code> uses either the <code>kpathsea</code>, <code>emtexdir</code>, or <code>MiKTeX</code> library for searching files (<code>emtexdir</code> will work only on operating systems which have an MS-DOSish background, i.e., MS-DOS, OS/2, Windows; <code>MiKTeX</code> is for Win32 systems).</p>
<h3>kpathsea</h3>
<p> The actual version of kpathsea is displayed on screen if you call <code>hbf2gf</code> <code>&#8211;version</code>. </p>
<p> Here is a table of the file type and the corresponding <code>kpathsea</code> variables. </p>
<p> Please consult the info files of <code>kpathsea</code> for details on these variables. The decision which naming scheme to use for variables will be done during compilation. </p>
<p> You should set the variable to the directory where your configuration file resides. </p>
<p> Here is the proper command to find out to which value a <code>kpathsea</code> variable is set (we use as an example). This is especially useful if a variable isn&#8217;t set in or in the environment, thus pointing to the default value which is hard-coded into the <code>kpathsea</code> library. </p>
<p> We select the program name also since it is possible to specify variables which are searched only for a certain program &#8211; in our example it would be </p>
<p> A similar but not identical method is to say </p>
<p> [A full list of format types can be obtained by saying &#8216; on the command line prompt.] This is exactly how <code>hbf2gf</code> searches for files; the disadvantage is that all variables are expanded which can cause very long strings.</p>
<h3>emtexdir</h3>
<p> Here the list of suffixes and its related environment variables to be set in (resp. in for OS/2): </p>
<p> If one of the variables isn&#8217;t set, a warning message is emitted. The current directory will always be searched. As usual, one exclamation mark appended to a directory path causes subdirectories one level deep to be searched, two exclamation marks causes all subdirectories to be searched. Example: </p>
<p> Constructions like &#8216; aren&#8217;t possible.</p>
<h3>MikTeX</h3>
<p> Please consult the documentation files of <code>MiKTeX</code> for more details.</p>
<h2>LIMITATIONS</h2>
<p> The x and y output size must not exceed <code>MAX_CHAR_SIZE</code>, which is defined at compile time; its default value is 1023&nbsp;(pixel).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ttf2pk/">ttf2pk</a></code>(1) </p>
<p> this is the source code written in <code>CWEB</code> which can be converted into a pretty-printed TeX document using <code>cweave</code>. The CJK package also contains a preformatted file. </p>
<p> the <code>CJK</code> documentation files ( </p>
<p> the <code>Hanzi Bitmap File</code> (<code>HBF</code>) standard version 1.3; available at </p>
<p> the Omega documentation available at and the CTAN hosts and mirrors.</p>
<h2>FILES</h2>
<dl>
<dt>
<dd> The <code>hbf2gf</code> configuration scripts.</p>
<dt>
<dd> HBF header files which describe fixed-width bitmap fonts. Note that the bitmap font name(s) themselves as specified in the header files are irrelevant for <code>hbf2gf</code>.</dl>
<h2>AVAILABILITY</h2>
<p> <code>hbf2gf</code> is part of the CJK macro package for LaTeX 2e available at the CTAN hosts and its mirrors. </p>
<p> CJK fonts together with HBF header files can be found at and its mirrors.</p>
<h2>AUTHORS</h2>
<p> Werner Lemberg<br />
 Ross Paterson (the HBF API) </p>
<h2>Index</h2>
