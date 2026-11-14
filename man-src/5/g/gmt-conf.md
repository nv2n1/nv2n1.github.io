---
title: "gmt-conf(5)"
name: "gmt-conf"
section: "5"
letter: "g"
url: "/docs/linux/man/5-gmt-conf/"
description: "gmt.conf – Configuration for GMT"
---

<p>gmt.conf &#8211; Configuration for GMT</p>
<h2>Description</h2>
<p>The following is a list of the parameters that are user-definable in GMT. The parameter names are always given in UPPER CASE. The parameter values are case-insensitive unless otherwise noted. The system defaults are given in brackets [ for SI (and US) ]. Those marked <code>*</code> can be set on the command line as well (the corresponding option is given in parentheses). Note that default distances and lengths below are given in both cm or inch; the chosen default depends on your choice of default unit (see <i>PROJ_LENGTH_UNIT</i>). You can explicitly specify the unit used for distances and lengths by appending <code>c</code> (cm), <code>i</code> (inch), or <code>p</code> (points). When no unit is indicated the value will be assumed to be in the unit set by <i>PROJ_LENGTH_UNIT</i>. Several parameters take only <code>true</code> or <code>false</code>. Finally, most of these parameters can be changed on-the-fly via the <code>&#8211;</code><code>-PARAMETER</code>=<i>VALUE</i> option to any GMT program. However, a few are static and are only read via the <code>gmt.conf</code> file; these are labeled (static).</p>
<h2>Common Specifications</h2>
<p>The full explanation for how to specify pens, pattern fills, colors, and fonts can be found in the <code>gmt</code> man page. <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> THEMATIC SUB-SECTIONS </td>
<td> <i>prefix</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>COLOR Parameters</i> </td>
<td> <code>COLOR_</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>DIR Parameters</i> </td>
<td> <code>DIR_</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>FONT Parameters</i> </td>
<td> <code>FONT_</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>FORMAT Parameters</i> </td>
<td> <code>FORMAT_</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>GMT Miscellaneous Parameters</i> </td>
<td> <code>GMT_</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>I/O Parameters</i> </td>
<td> <code>IO_</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>MAP Parameters</i> </td>
<td> <code>MAP_</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>Projection Parameters</i> </td>
<td> <code>PROJ_</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>PostScript Parameters</i> </td>
<td> <code>PS_</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>Calendar/Time Parameters</i> </td>
<td> <code>TIME_</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dl>
<dt><code>COLOR_BACKGROUND</code></p>
<dd>Color used for the background of images (i.e., when z &lt; lowest color table entry) [black].</p>
<dt><code>COLOR_FOREGROUND</code></p>
<dd>Color used for the foreground of images (i.e., when z &gt; highest color table entry) [white].</p>
<dt><code>COLOR_HSV_MAX_S</code></p>
<dd>Maximum saturation (0-1) assigned for most positive intensity value [0.1].</p>
<dt><code>COLOR_HSV_MIN_S</code></p>
<dd>Minimum saturation (0-1) assigned for most negative intensity value [1.0].</p>
<dt><code>COLOR_HSV_MAX_V</code></p>
<dd>Maximum value (0-1) assigned for most positive intensity value [1.0].</p>
<dt><code>COLOR_HSV_MIN_V</code></p>
<dd>Minimum value (0-1) assigned for most negative intensity value [0.3].</p>
<dt><code>COLOR_MODEL</code></p>
<dd>Selects in which color space a CPT should be interpolated. By default, color interpolation takes place directly on the RGB values which can produce some unexpected hues, whereas interpolation directly on the HSV values better preserves those hues. The choices are: <code>none</code> (default: use whatever the COLOR_MODEL setting in the CPT file demands), <code>rgb</code> (force interpolation in RGB), <code>hsv</code> (force interpolation in HSV), <code>cmyk</code> (assumes colors are in CMYK but interpolates in RGB).</p>
<dt><code>COLOR_NAN</code></p>
<dd>Color used for the non-defined areas of images (i.e., where z == NaN) [127.5].</p>
<dt><code>DIR_DATA</code></p>
<dd>Session data dir. Overrides the value of the environment variable <code>$GMT_DATADIR</code> (see <i>Directory parameters</i> in the CookBook).</p>
<dt><code>DIR_DCW</code></p>
<dd>Path to optional Digital Chart of the World polygon files.</p>
<dt><code>DIR_GSHHG</code></p>
<dd>Path to GSHHG files. Defaults to <code>$GMT_SHAREDIR</code>/coast if empty.</p>
<dt><code>FONT</code></p>
<dd>Sets the default for all fonts, except FONT_LOGO. This setting is not included in the <code>gmt.conf</code> file.</p>
<dt><code>FONT_ANNOT_PRIMARY</code></p>
<dd>Font used for primary annotations, etc. [12p,Helvetica,black]. When <code>+</code> is prepended, scale fonts, offsets and tick-lengths relative to <code>FONT_ANNOT_PRIMARY</code>.</p>
<dt><code>FONT_ANNOT_SECONDARY</code></p>
<dd>Font to use for time axis secondary annotations [14p,Helvetica,black].</p>
<dt><code>FONT_LABEL</code></p>
<dd>Font to use when plotting labels below axes [16p,Helvetica,black].</p>
<dt><code>FONT_LOGO</code></p>
<dd>Font to use for text plotted as part of the GMT time logo [8p,Helvetica,black].</p>
<dt><code>FONT_TITLE</code></p>
<dd>Font to use when plotting titles over graphs [24p,Helvetica,black].</p>
<dt><code>FORMAT_CLOCK_IN</code></p>
<dd>Formatting template that indicates how an input clock string is formatted. This template is then used to guide the reading of clock strings in data fields. To properly decode 12-hour clocks, append am or pm (or upper case) to match your data records. As examples, try hh:mm, hh:mm:ssAM, etc. [hh:mm:ss].</p>
<dt><code>FORMAT_CLOCK_MAP</code></p>
<dd>Formatting template that indicates how an output clock string is to be plotted. This template is then used to guide the formatting of clock strings in plot annotations. See <code>FORMAT_CLOCK_OUT</code> for details. [hh:mm:ss].</p>
<dt><code>FORMAT_CLOCK_OUT</code></p>
<dd>Formatting template that indicates how an output clock string is to be formatted. This template is then used to guide the writing of clock strings in data fields. To use a floating point format for the smallest unit (e.g., seconds), append .xxx, where the number of x indicates the desired precision. If no floating point is indicated then the smallest specified unit will be rounded off to nearest integer. For 12-hour clocks, append am, AM, a.m., or A.M. (GMT will replace a|A with p|P for pm). If your template starts with a leading hyphen (-) then each integer item (y,m,d) will be printed without leading zeros (default uses fixed width formats). As examples, try hh:mm, hh.mm.ss, hh:mm:ss.xxxx, hha.m., etc. [hh:mm:ss]. If the format is simply &#8211; then no clock is output and the ISO T divider between date and clock is omitted.</p>
<dt><code>FORMAT_DATE_IN</code></p>
<dd>Formatting template that indicates how an input date string is formatted. This template is then used to guide the reading of date strings in data fields. You may specify either Gregorian calendar format or ISO week calendar format. Gregorian calendar: Use any combination of yyyy (or yy for 2-digit years; if so see <code>TIME_Y2K_OFFSET_YEAR</code>), mm (or o for abbreviated month name in the current time language), and dd, with or without delimiters. For day-of-year data, use jjj instead of mm and/or dd. Examples can be ddmmyyyy, yy-mm-dd, dd-o-yyyy, yyyy/dd/mm, yyyy-jjj, etc. ISO Calendar: Expected template is yyyy[-]W[-]ww[-]d, where ww is ISO week and d is ISO week day. Either template must be consistent, e.g., you cannot specify months if you do not specify years. Examples are yyyyWwwd, yyyy-Www, etc. [yyyy-mm-dd].</p>
<dt><code>FORMAT_DATE_MAP</code></p>
<dd>Formatting template that indicates how an output date string is to be plotted. This template is then used to guide the plotting of date strings in data fields. See <code>FORMAT_DATE_OUT</code> for details. In addition, you may use a single o instead of mm (to plot month name) and u instead of W[-]ww to plot &quot;Week ##&quot;. Both of these text strings will be affected by the <code>GMT_LANGUAGE</code>, <code>FORMAT_TIME_PRIMARY_MAP</code> and <code>FORMAT_TIME_SECONDARY_MAP</code> setting. [yyyy-mm-dd].</p>
<dt><code>FORMAT_DATE_OUT</code></p>
<dd>Formatting template that indicates how an output date string is to be formatted. This template is then used to guide the writing of date strings in data fields. You may specify either Gregorian calendar format or ISO week calendar format. Gregorian calendar: Use any combination of yyyy (or yy for 2-digit years; if so see <code>TIME_Y2K_OFFSET_YEAR</code>), mm (or o for abbreviated month name in the current time language), and dd, with or without delimiters. For day-of-year data, use jjj instead of mm and/or dd. As examples, try yy/mm/dd, yyyy=jjj, dd-o-yyyy, dd-mm-yy, yy-mm, etc. ISO Calendar: Expected template is yyyy[-]W[-]ww[-]d, where ww is ISO week and d is ISO week day. Either template must be consistent, e.g., you cannot specify months if you do not specify years. As examples, try yyyyWww, yy-W-ww-d, etc. If your template starts with a leading hyphen (-) then each integer item (y,m,d) will be printed without leading zeros (default uses fixed width formats) [yyyy-mm-dd]. If the format is simply &#8211; then no date is output and the ISO T divider between date and clock is omitted.</p>
<dt><code>FORMAT_GEO_MAP</code></p>
<dd>Formatting template that indicates how an output geographical coordinate is to be plotted. This template is then used to guide the plotting of geographical coordinates in data fields. See <code>FORMAT_GEO_OUT</code> for details. In addition, you can append A which plots the absolute value of the coordinate. The default is ddd:mm:ss. Not all items may be plotted as this depends on the annotation interval.</p>
<dt><code>FORMAT_GEO_OUT</code></p>
<dd>Formatting template that indicates how an output geographical coordinate is to be formatted. This template is then used to guide the writing of geographical coordinates in data fields. The template is in general of the form [+|-]D or [+|-]ddd[:mm[:ss]][.xxx][F]. By default, longitudes will be reported in the range [-180,180]. The various terms have the following purpose: </p>
<p> +D Output longitude in the range [0,360] </p>
<p> -D Output longitude in the range [-360,0] </p>
<p> D Use <code>FORMAT_FLOAT_OUT</code> for floating point degrees. </p>
<p> ddd Fixed format integer degrees </p>
<p> : delimiter used </p>
<p> mm Fixed format integer arc minutes </p>
<p> ss Fixed format integer arc seconds </p>
<p> .xxx Floating fraction of previous integer field, fixed width. </p>
<p> F Encode sign using WESN suffix </p>
<p> G Same as F but with a leading space before suffix </p>
<p> The default is D.</p>
<dt><code>FORMAT_FLOAT_MAP</code></p>
<dd>Format (C language printf syntax) to be used when plotting double precision floating point numbers along plot frames and contours. For geographic coordinates, see <code>FORMAT_GEO_MAP</code>. [%.12lg].</p>
<dt><code>FORMAT_FLOAT_OUT</code></p>
<dd>Format (C language printf syntax) to be used when printing double precision floating point numbers to output files. For geographic coordinates, see <code>FORMAT_GEO_OUT</code>. [%.12lg]. To give some columns a separate format, supply one or more comma-separated <i>cols</i>:<i>format</i> specifications, where <i>cols</i> can be specific columns (e.g., 5 for 6th since 0 is the first) or a range of columns (e.g., 3-7). The last specification without column information will override the format for all other columns. Alternatively, you can list N space-separated formats and these apply to the first N columns.</p>
<dt><code>FORMAT_TIME_PRIMARY_MAP</code></p>
<dd>Controls how primary month-, week-, and weekday-names are formatted. Choose among <code>full</code>, <code>abbreviated</code>, and <code>character</code>. If the leading <code>f</code>, <code>a</code>, or <code>c</code> are replaced with <code>F</code>, <code>A</code>, and <code>C</code> the entire annotation will be in upper case [full].</p>
<dt><code>FORMAT_TIME_SECONDARY_MAP</code></p>
<dd>Controls how secondary month-, week-, and weekday-names are formatted. Choose among <code>full</code>, <code>abbreviated</code>, and <code>character</code>. If the leading <code>f</code>, <code>a</code>, or <code>c</code> are replaced with <code>F</code>, <code>A</code>, and <code>C</code> the entire annotation will be in upper case [full].</p>
<dt><code>FORMAT_TIME_STAMP</code></p>
<dd>Defines the format of the time information in the UNIX time stamp. This format is parsed by the C function <code>strftime</code>, so that virtually any text can be used (even not containing any time information) [%Y %b %d %H:%M:%S].</p>
<dt><code>GMT_COMPATIBILITY</code></p>
<dd>Determines if this GMT version should be able to parse command-line options for a prior major release. Specify either 4 or 5. If 4 is set we will parse obsolete GMT 4 options and issue warnings; if 5 is set then parsing GMT 4 only syntax will result in errors [4].</p>
<dt><code>GMT_EXPORT_TYPE</code></p>
<dd>This setting is only used by external interfaces and controls the data type used for table entries. Choose from double, single, [u]long, [u]int, [u]short, and [u]char [double].</p>
<dt><code>GMT_EXTRAPOLATE_VAL</code></p>
<dd>Determines what to do if extrapolating beyond the data domain. Choose among &#8216;NaN&#8217;, &#8216;extrap&#8217; or &#8216;extrapval,val&#8217; (without quotes). In the first case return NaN for any element of x that is outside range [Default]. Second case lets the selected algorithm compute the extrapolation values. Third case sets the extrapolation values to the constant value passed in &#8216;val&#8217; (this value must off course be numeric).</p>
<dt><code>GMT_CUSTOM_LIBS</code></p>
<dd>Comma-separated list of GMT-compliant shared libraries that extend the capability of GMT with additional custom modules [none]. Alternatively, provide a directory name, that MUST end with a slash (or back slash), to use all shared libraries in that directory. On Windows, if the dir name is made up only of a single slash (&#8216;/&#8217;) search inside a subdirectory called &#8216;gmt_plugins&#8217; of the directory that contains the &#8216;gmt&#8217; executable. See the API documentation for how to build your own shared modules.</p>
<dt><code>GMT_FFT</code></p>
<dd>Determines which Fast Fourier Transform (FFT) should be used among those that have been configured during installation. Choose from <code>auto</code> (pick the most suitable for the task among available algorithms), <code>fftw</code>[,<i>planner_flag</i>] (The Fastest Fourier Transform in the West), <code>accelerate</code> (Use the Accelerate Framework under OS X; Note, that the number of samples to be processed must be a base 2 exponent), <code>kiss</code>, (Kiss FFT), <code>brenner</code> Brenner Legacy FFT [auto]. FFTW can &quot;learn&quot; how to optimally compute Fourier transforms on the current hardware and OS by computing several FFTs and measuring their execution time. This so gained &quot;Wisdom&quot; will be stored in and reloaded from the file fftw_wisdom_&lt;hostname&gt; in $GMT_USERDIR or, if $GMT_USERDIR is not writable, in the current directory. To use this feature append <i>planner_flag</i>, which can be one of <i>measure</i>, <i>patient</i>, and <i>exhaustive</i>; see FFTW reference for details. The default FFTW planner flag is <i>estimate</i>, i.e., pick a (probably sub-optimal) plan quickly. Note: if you need a single transform of a given size only, the one-time cost of the smart planner becomes significant. In that case, stick to the default planner, <i>estimate</i>, based on heuristics.</p>
<dt><code>GMT_HISTORY</code></p>
<dd>Passes the history of past common command options via the gmt.history file. The different values for this setting are: <code>true</code>, <code>readonly</code>, <code>false</code>, to either read and write to the gmt.history file, only read, or not use the file at all [true].</p>
<dt><code>GMT_INTERPOLANT</code></p>
<dd>Determines if linear (linear), Akima&#8217;s spline (akima), natural cubic spline (cubic) or no interpolation (none) should be used for 1-D interpolations in various programs [akima].</p>
<dt><code>GMT_LANGUAGE</code></p>
<dd>Language to use when plotting calendar and map items such as months and days, map annotations and cardinal points. Select from:</p>
<dt>&bull;</p>
<dd>CN1 Simplified Chinese</p>
<dt>&bull;</p>
<dd>CN2 Traditional Chinese</p>
<dt>&bull;</p>
<dd>DE German</p>
<dt>&bull;</p>
<dd>DK Danish</p>
<dt>&bull;</p>
<dd>EH Basque</p>
<dt>&bull;</p>
<dd>ES Spanish</p>
<dt>&bull;</p>
<dd>FI Finnish</p>
<dt>&bull;</p>
<dd>FR French</p>
<dt>&bull;</p>
<dd>GR Greek</p>
<dt>&bull;</p>
<dd>HI Hawaiian</p>
<dt>&bull;</p>
<dd>HU Hungarian</p>
<dt>&bull;</p>
<dd>IE Irish</p>
<dt>&bull;</p>
<dd>IL Hebrew</p>
<dt>&bull;</p>
<dd>IS Icelandic</p>
<dt>&bull;</p>
<dd>IT Italian</p>
<dt>&bull;</p>
<dd>JP Japanese</p>
<dt>&bull;</p>
<dd>KR Korean</p>
<dt>&bull;</p>
<dd>NL Dutch</p>
<dt>&bull;</p>
<dd>NO Norwegian</p>
<dt>&bull;</p>
<dd>PL Polish</p>
<dt>&bull;</p>
<dd>PT Portuguese</p>
<dt>&bull;</p>
<dd>RU Russian</p>
<dt>&bull;</p>
<dd>SE Swedish</p>
<dt>&bull;</p>
<dd>SG Scottish Gaelic</p>
<dt>&bull;</p>
<dd>TO Tongan</p>
<dt>&bull;</p>
<dd>TR Turkish</p>
<dt>&bull;</p>
<dd>UK British English</p>
<dt>&bull;</p>
<dd>US US English </p>
<p> If your language is not supported, please examine the <code>$GMT_SHAREDIR</code>/localization/gmt_us.locale file and make a similar file. Please submit it to the GMT Developers for official inclusion. Custom language files can be placed in directories <code>$GMT_SHAREDIR</code>/localization or ~/.gmt. Note: Some of these languages may require you to also change the <code>PS_CHAR_ENCODING</code> setting.</p>
<dt><code>GMT_TRIANGULATE</code></p>
<dd>Determines if we use the <code>Watson</code> [Default] or <code>Shewchuk</code> algorithm (if configured during installation) for triangulation. Note that Shewchuk is required for operations involving Voronoi constructions.</p>
<dt><code>GMT_VERBOSE</code></p>
<dd>(<code>-V</code>) Determines the level of verbosity used by GMT programs. Choose among 6 levels; each level adds to the verbosity of the lower levels: <code>q</code>uiet, <code>n</code>normal (errors and warnings), <code>c</code>ompatibility warnings, <code>v</code>erbose progress reports, <code>l</code>ong verbose progress reports, <code>d</code>ebugging messages [c].</p>
<dt><code>IO_COL_SEPARATOR</code></p>
<dd>This setting determines what character will separate ASCII output data columns written by GMT. Choose from tab, space, comma, and none [tab].</p>
<dt><code>IO_GRIDFILE_FORMAT</code></p>
<dd>Default file format for grids, with optional scale, offset and invalid value, written as <i>ff</i>/<i>scale</i>/<i>offset</i>/<i>invalid</i>. The 2-letter format indicator can be one of [<code>abcegnrs</code>][<code>bsifd</code>]. See <code>grdconvert</code> and Section <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information. The <i>scale</i> and <i>offset</i> modifiers may be left empty to select default values (scale = 1, offset = 0), or you may specify <i>a</i> for auto-adjusting the scale and/or offset of packed integer grids (=<i>id/a</i> is a shorthand for =<i>id/a/a</i>). When <i>invalid</i> is omitted the appropriate value for the given format is used (NaN or largest negative). [nf].</p>
<dt><code>IO_GRIDFILE_SHORTHAND</code></p>
<dd>If true, all grid file names are examined to see if they use the file extension shorthand discussed in Section <i>grid-file-format</i> of the GMT Technical Reference and Cookbook. If false, no filename expansion is done [false].</p>
<dt><code>IO_HEADER</code></p>
<dd>(<code>-h</code>) Specifies whether input/output ASCII files have header record(s) or not [false].</p>
<dt><code>IO_LONLAT_TOGGLE</code></p>
<dd>(<code>-:</code>) Set if the first two columns of input and output files contain (latitude,longitude) or (y,x) rather than the expected (longitude,latitude) or (x,y). false means we have (x,y) both on input and output. true means both input and output should be (y,x). IN means only input has (y,x), while OUT means only output should be (y,x). [false].</p>
<dt><code>IO_N_HEADER_RECS</code></p>
<dd>Specifies how many header records to expect if <code>-h</code> is used [0]. Note: This will skip the specified number of records regardless of what they are. Since any records starting with # is automatically considered a header you will only specify a non-zero number in order to skip headers that do not conform to that convention.</p>
<dt><code>IO_NAN_RECORDS</code></p>
<dd>Determines what happens when input records containing NaNs for <i>x</i> or <i>y</i> (and in some cases <i>z</i>) are read. Choose between <code>skip</code>, which will simply report how many bad records were skipped, and <code>pass</code> [Default], which will pass these records on to the calling programs. For most programs this will result in output records with NaNs as well, but some will interpret these NaN records to indicate gaps in a series; programs may then use that information to detect segmentation (if applicable).</p>
<dt><code>IO_NC4_CHUNK_SIZE</code></p>
<dd>Sets the default chunk size for the <code>lat</code> and <code>lon</code> dimension of the <code>z</code> variable. Very large chunk sizes and sizes smaller than 128 should be avoided because they can lead to unexpectedly bad performance. Note that a chunk of a single precision floating point variable of size 2896&#215;2896 completely fills the chunk cache of 32MiB. Specify the chunk size for each dimension separated by a comma, or <code>a</code>uto for optimally chosen chunk sizes in the range [128,256). Setting IO_NC4_CHUNK_SIZE will produce netCDF version 4 files, which can only be read with the netCDF 4 library, unless all dimensions are less than 128 or <code>c</code>lassic is specified for classic netCDF. [auto]</p>
<dt><code>IO_NC4_DEFLATION_LEVEL</code></p>
<dd>Sets the compression level for netCDF4 files upon output. Values allowed are integers from 0 (no compression) to 9 (maximum compression). Enabling a low compression level can dramatically improve performance and reduce the size of certain data. While higher compression levels further reduce the data size, they do so at the cost of extra processing time. This parameter does not apply to classic netCDF files. [3]</p>
<dt><code>IO_SEGMENT_BINARY</code></p>
<dd>Determines how binary data records with all values set to NaN are interpreted. Such records are considered to be encoded segment headers in binary files provided the number of columns equals or exceeds the current setting of IO_SEGMENT_BINARY [2]. Specify 0 or &quot;off&quot; to deactivate the segment header determination.</p>
<dt><code>IO_SEGMENT_MARKER</code></p>
<dd>This holds the character we expect to indicate a segment header in an incoming ASCII data or text table [&gt;]. If this marker should be different for output then append another character for the output segment marker. The two characters must be separated by a comma. Two marker characters have special meaning: B means &quot;blank line&quot; and will treat blank lines as initiating a new segment, whereas N means &quot;NaN record&quot; and will treat records with all NaNs as initiating a new segment. If you choose B or N for the output marker then the normal GMT segment header is replaced by a blank or NaN record, respectively, and no segment header information is written. To use B or N as regular segment markers you must escape them with a leading backslash.</p>
<dt><code>MAP_ANNOT_MIN_ANGLE</code></p>
<dd>If the angle between the map boundary and the annotation baseline is less than this minimum value (in degrees), the annotation is not plotted (this may occur for certain oblique projections.) Give a value in the range [0,90]. [20]</p>
<dt><code>MAP_ANNOT_MIN_SPACING</code></p>
<dd>If an annotation would be plotted less than this minimum distance from its closest neighbor, the annotation is not plotted (this may occur for certain oblique projections.) [0p]</p>
<dt><code>MAP_ANNOT_OBLIQUE</code></p>
<dd>This integer is a sum of 6 bit flags (most of which only are relevant for oblique projections): If bit 1 is set (1), annotations will occur wherever a gridline crosses the map boundaries, else longitudes will be annotated on the lower and upper boundaries only, and latitudes will be annotated on the left and right boundaries only. If bit 2 is set (2), then longitude annotations will be plotted horizontally. If bit 3 is set (4), then latitude annotations will be plotted horizontally. If bit 4 is set (8), then oblique tick-marks are extended to give a projection equal to the specified tick length. If bit 5 is set (16), tick-marks will be drawn normal to the border regardless of gridline angle. If bit 6 is set (32), then latitude annotations will be plotted parallel to the border. To set a combination of these, add up the values in parentheses. [1].</p>
<dt><code>MAP_ANNOT_OFFSET_PRIMARY</code></p>
<dd>Distance from end of tick-mark to start of annotation [5p].</p>
<dt><code>MAP_ANNOT_OFFSET_SECONDARY</code></p>
<dd>Distance from base of primary annotation to the top of the secondary annotation [5p] (Only applies to time axes with both primary and secondary annotations).</p>
<dt><code>MAP_ANNOT_ORTHO</code></p>
<dd>Determines which axes will get their annotations (for linear projections) plotted orthogonally to the axes. Combine any <code>w</code>, <code>e</code>, <code>s</code>, <code>n</code>, <code>z</code> (uppercase allowed as well). [we].</p>
<dt><code>MAP_DEFAULT_PEN</code></p>
<dd>Sets the default of all pens related to <code>-W</code> options. Prepend <code>+</code> to overrule the color of the parameters <code>MAP_GRID_PEN_PRIMARY</code>, <code>MAP_GRID_PEN_SECONDARY</code>, <code>MAP_FRAME_PEN</code>, <code>MAP_TICK_PEN_PRIMARY</code>, and <code>MAP_TICK_PEN_SECONDARY</code> by the color of <code>MAP_DEFAULT_PEN</code> [default,black].</p>
<dt><code>MAP_DEGREE_SYMBOL</code></p>
<dd>Determines what symbol is used to plot the degree symbol on geographic map annotations. Choose between ring, degree, colon, or none [ring].</p>
<dt><code>MAP_FRAME_AXES</code></p>
<dd>Sets which axes to draw and annotate. Combine any uppercase <code>W</code>, <code>E</code>, <code>S</code>, <code>N</code>, <code>Z</code> to draw and annotate west, east, south, north and/or vertical (perspective view only) axis. Use lower case to draw the axis only, but not annotate. Add an optional <code>+</code> to draw a cube of axes in perspective view. [WESN].</p>
<dt><code>MAP_FRAME_PEN</code></p>
<dd>Pen attributes used to draw plain map frame [thicker,black].</p>
<dt><code>MAP_FRAME_TYPE</code></p>
<dd>Choose between <code>inside</code>, <code>plain</code> and <code>fancy</code> (thick boundary, alternating black/white frame; append <code>+</code> for rounded corners) [fancy]. For some map projections (e.g., Oblique Mercator), plain is the only option even if fancy is set as default. In general, fancy only applies to situations where the projected x and y directions parallel the longitude and latitude directions (e.g., rectangular projections, polar projections). For situations where all boundary ticks and annotations must be inside the maps (e.g., for preparing geotiffs), chose <code>inside</code>.</p>
<dt><code>MAP_FRAME_WIDTH</code></p>
<dd>Width (&gt; 0) of map borders for fancy map frame [5p].</p>
<dt><code>MAP_GRID_CROSS_SIZE_PRIMARY</code></p>
<dd>Size (&gt;= 0) of grid cross at lon-lat intersections. 0 means draw continuous gridlines instead [0p].</p>
<dt><code>MAP_GRID_CROSS_SIZE_SECONDARY</code></p>
<dd>Size (&gt;= 0) of grid cross at secondary lon-lat intersections. 0 means draw continuous gridlines instead [0p].</p>
<dt><code>MAP_GRID_PEN_PRIMARY</code></p>
<dd>Pen attributes used to draw primary grid lines in dpi units or points (append p) [default,black].</p>
<dt><code>MAP_GRID_PEN_SECONDARY</code></p>
<dd>Pen attributes used to draw secondary grid lines in dpi units or points (append p) [thinner,black].</p>
<dt><code>MAP_LABEL_OFFSET</code></p>
<dd>Distance from base of axis annotations to the top of the axis label [8p].</p>
<dt><code>MAP_LINE_STEP</code></p>
<dd>Determines the maximum length (&gt; 0) of individual straight line-segments when drawing arcuate lines [0.75p]</p>
<dt><code>MAP_LOGO</code></p>
<dd>(<code>-U</code>) Specifies if a GMT logo with system timestamp should be plotted at the lower left corner of the plot [false].</p>
<dt><code>MAP_LOGO_POS</code></p>
<dd>(<code>-U</code>) Sets the justification and the position of the logo/timestamp box relative to the current plots lower left corner of the plot [BL/-54p/-54p].</p>
<dt><code>MAP_ORIGIN_X</code></p>
<dd>(<code>-X</code>) Sets the x-coordinate of the origin on the paper for a new plot [1i]. For an overlay, the default offset is 0.</p>
<dt><code>MAP_ORIGIN_Y</code></p>
<dd>(<code>-Y</code>) Sets the y-coordinate of the origin on the paper for a new plot [1i]. For an overlay, the default offset is 0.</p>
<dt><code>MAP_POLAR_CAP</code></p>
<dd>Controls the appearance of gridlines near the poles for all azimuthal projections and a few others in which the geographic poles are plotted as points (Lambert Conic, Hammer, Mollweide, Sinusoidal, and van der Grinten). Specify either none (in which case there is no special handling) or <i>pc_lat</i>/<i>pc_dlon</i>. In that case, normal gridlines are only drawn between the latitudes &#8211;<i>pc_lat</i>/+*pc_lat*, and above those latitudes the gridlines are spaced at the (presumably coarser) <i>pc_dlon</i> interval; the two domains are separated by a small circle drawn at the <i>pc_lat</i> latitude [85/90]. Note for r-theta (polar) projection where r = 0 is at the center of the plot the meaning of the cap is reversed, i.e., the default 85/90 will draw a r = 5 radius circle at the center of the map with less frequent radial lines there.</p>
<dt><code>MAP_SCALE_HEIGHT</code></p>
<dd>Sets the height (&gt; 0) on the map of the map scale bars drawn by various programs [5p].</p>
<dt><code>MAP_TICK_LENGTH_PRIMARY</code></p>
<dd>The length of a primary major/minor tick-marks [5p/2.5p]. If only the first value is set, the second is assumed to be 50% of the first.</p>
<dt><code>MAP_TICK_LENGTH_SECONDARY</code></p>
<dd>The length of a secondary major/minor tick-marks [15p/3.75p]. If only the first value is set, the second is assumed to be 25% of the first.</p>
<dt><code>MAP_TICK_PEN_PRIMARY</code></p>
<dd>Pen attributes to be used for primary tick-marks in dpi units or points (append p) [thinner,black].</p>
<dt><code>MAP_TICK_PEN_SECONDARY</code></p>
<dd>Pen attributes to be used for secondary tick-marks in dpi units or points (append p) [thinner,black].</p>
<dt><code>MAP_TITLE_OFFSET</code></p>
<dd>Distance from top of axis annotations (or axis label, if present) to base of plot title [14p].</p>
<dt><code>MAP_VECTOR_SHAPE</code></p>
<dd>Determines the shape of the head of a vector. Normally (i.e., for vector_shape = 0), the head will be triangular, but can be changed to an arrow (1) or an open V (2). Intermediate settings give something in between. Negative values (up to -2) are allowed as well [0].</p>
<dt><code>PROJ_AUX_LATITUDE</code></p>
<dd>Only applies when geodesics are approximated by great circle distances on an equivalent sphere. Select from authalic, geocentric, conformal, meridional, parametric, or none [authalic]. When not none we convert any latitude used in the great circle calculation to the chosen auxiliary latitude before doing the distance calculation. See also <code>PROJ_MEAN_RADIUS</code>.</p>
<dt><code>PROJ_ELLIPSOID</code></p>
<dd>The (case sensitive) name of the ellipsoid used for the map projections [WGS-84]. Choose among: </p>
<pre><i>Airy</i>: Applies to Great Britain (1830)
<i>Airy-Ireland</i>: Applies to Ireland in 1965 (1830)
<i>Andrae</i>: Applies to Denmark and Iceland (1876)
<i>APL4.9</i>: Appl. Physics (1965)
<i>ATS77</i>: Average Terrestrial System, Canada Maritime provinces (1977)
<i>Australian</i>: Applies to Australia (1965)
<i>Bessel</i>: Applies to Central Europe, Chile, Indonesia (1841)
<i>Bessel-Namibia</i>: Same as Bessel-Schwazeck (1841)
<i>Bessel-NGO1948</i>: Modified Bessel for NGO 1948 (1841)
<i>Bessel-Schwazeck</i>: Applies to Namibia (1841)
<i>Clarke-1858</i>: Clarke's early ellipsoid (1858)
<i>Clarke-1866</i>: Applies to North America, the Philippines (1866)
<i>Clarke-1866-Michigan</i>: Modified Clarke-1866 for Michigan (1866)
<i>Clarke-1880</i>: Applies to most of Africa, France (1880)
<i>Clarke-1880-Arc1950</i>: Modified Clarke-1880 for Arc 1950 (1880)
<i>Clarke-1880-IGN</i>: Modified Clarke-1880 for IGN (1880)
<i>Clarke-1880-Jamaica</i>: Modified Clarke-1880 for Jamaica (1880)
<i>Clarke-1880-Merchich</i>: Modified Clarke-1880 for Merchich (1880)
<i>Clarke-1880-Palestine</i>: Modified Clarke-1880 for Palestine (1880)
<i>CPM</i>: Comm. des Poids et Mesures, France (1799)
<i>Delambre</i>: Applies to Belgium (1810)
<i>Engelis</i>: Goddard Earth Models (1985)
<i>Everest-1830</i>: India, Burma, Pakistan, Afghanistan, Thailand (1830)
<i>Everest-1830-Kalianpur</i>: Modified Everest for Kalianpur (1956) (1830)
<i>Everest-1830-Kertau</i>: Modified Everest for Kertau, Malaysia &amp; Singapore (1830)
<i>Everest-1830-Pakistan</i>: Modified Everest for Pakistan (1830)
<i>Everest-1830-Timbalai</i>: Modified Everest for Timbalai, Sabah Sarawak (1830)
<i>Fischer-1960</i>: Used by NASA for Mercury program (1960)
<i>Fischer-1960-SouthAsia</i>: Same as Modified-Fischer-1960 (1960)
<i>Fischer-1968</i>: Used by NASA for Mercury program (1968)
<i>FlatEarth</i>: As Sphere, but implies fast &quot;Flat Earth&quot; distance calculations (1984)
<i>GRS-67</i>: International Geodetic Reference System (1967)
<i>GRS-80</i>: International Geodetic Reference System (1980)
<i>Hayford-1909</i>: Same as the International 1924 (1909)
<i>Helmert-1906</i>: Applies to Egypt (1906)
<i>Hough</i>: Applies to the Marshall Islands (1960)
<i>Hughes-1980</i>: Hughes Aircraft Company for DMSP SSM/I grid products (1980)
<i>IAG-75</i>: International Association of Geodesy (1975)
<i>Indonesian</i>: Applies to Indonesia (1974)
<i>International-1924</i>: Worldwide use (1924)
<i>International-1967</i>: Worldwide use (1967)
<i>Kaula</i>: From satellite tracking (1961)
<i>Krassovsky</i>: Used in the (now former) Soviet Union (1940)
<i>Lerch</i>: For geoid modeling (1979)
<i>Maupertius</i>: Really old ellipsoid used in France (1738)
<i>Mercury-1960</i>: Same as Fischer-1960 (1960)
<i>MERIT-83</i>: United States Naval Observatory (1983)
<i>Modified-Airy</i>: Same as Airy-Ireland (1830)
<i>Modified-Fischer-1960</i>: Applies to Singapore (1960)
<i>Modified-Mercury-1968</i>: Same as Fischer-1968 (1968)
<i>NWL-10D</i>: Naval Weapons Lab (Same as WGS-72) (1972)
<i>NWL-9D</i>: Naval Weapons Lab (Same as WGS-66) (1966)
<i>OSU86F</i>: Ohio State University (1986)
<i>OSU91A</i>: Ohio State University (1991)
<i>Plessis</i>: Old ellipsoid used in France (1817)
<i>SGS-85</i>: Soviet Geodetic System (1985)
<i>South-American</i>: Applies to South America (1969)
<i>Sphere</i>: The mean radius in WGS-84 (for spherical/plate tectonics applications) (1984)
<i>Struve</i>: Friedrich Georg Wilhelm Struve (1860)
<i>TOPEX</i>: Used commonly for altimetry (1990)
<i>Walbeck</i>: First least squares solution by Finnish astronomer (1819)
<i>War-Office</i>: Developed by G. T. McCaw (1926)
<i>WGS-60</i>: World Geodetic System (1960)
<i>WGS-66</i>: World Geodetic System (1966)
<i>WGS-72</i>: World Geodetic System (1972)
<i>WGS-84</i>: World Geodetic System [Default] (1984)
<i>Moon</i>: Moon (IAU2000) (2000)
<i>Mercury</i>: Mercury (IAU2000) (2000)
<i>Venus</i>: Venus (IAU2000) (2000)
<i>Mars</i>: Mars (IAU2000) (2000)
<i>Jupiter</i>: Jupiter (IAU2000) (2000)
<i>Saturn</i>: Saturn (IAU2000) (2000)
<i>Uranus</i>: Uranus (IAU2000) (2000)
<i>Neptune</i>: Neptune (IAU2000) (2000)
<i>Pluto</i>: Pluto (IAU2000) (2000)</pre>
<p>Note that for some global projections, GMT may use a spherical approximation of the ellipsoid chosen, setting the flattening to zero, and using a mean radius. A warning will be given when this happens. If a different ellipsoid name than those mentioned here is given, GMT will attempt to parse the name to extract the semi-major axis (<i>a</i> in m) and the flattening. Formats allowed are: </p>
<p> <i>a</i> implies a zero flattening </p>
<p> <i>a</i>,<i>inv_f</i> where <i>inv_f</i> is the inverse flattening </p>
<p> <i>a</i>,<code>b=</code><i>b</i> where <i>b</i> is the semi-minor axis (in m) </p>
<p> <i>a</i>,<code>f=</code><i>f</i> where <i>f</i> is the flattening </p>
<p> This way a custom ellipsoid (e.g., those used for other planets) may be used. Further note that coordinate transformations in <code>mapproject</code> can also specify specific datums; see the <code>mapproject</code> man page for further details and how to view ellipsoid and datum parameters.</p>
<dt><code>PROJ_GEODESIC</code></p>
<dd>Selects the algorithm to use for geodesic calculations. Choose between <code>Vincenty</code> [Default], <code>Rudoe</code>, or <code>Andoyer</code>. The <code>Andoyer</code> algorithm is only approximate (to within a few tens of meters) but is up to 5 times faster. The <code>Rudoe</code> is given for legacy purposes. The default <code>Vincenty</code> is accurate to about 0.5 mm.</p>
<dt><code>PROJ_LENGTH_UNIT</code></p>
<dd>Sets the unit length. Choose between <code>c</code>m, <code>i</code>nch, or <code>p</code>oint [c (or i)]. Note that, in GMT, one point is defined as 1/72 inch (the PostScript definition), while it is often defined as 1/72.27 inch in the typesetting industry. There is no universal definition.</p>
<dt><code>PROJ_MEAN_RADIUS</code></p>
<dd>Applies when geodesics are approximated by great circle distances on an equivalent sphere or when surface areas are computed. Select from mean (R_1), authalic (R_2), volumetric (R_3), meridional, or quadratic [authalic]. See also PROJ_MEAN_RADIUS.</p>
<dt><code>PROJ_SCALE_FACTOR</code></p>
<dd>Changes the default map scale factor used for the Polar Stereographic [0.9996], UTM [0.9996], and Transverse Mercator [1] projections in order to minimize areal distortion. Provide a new scale-factor or leave as default.</p>
<dt><code>PS_CHAR_ENCODING</code></p>
<dd>(static) Names the eight bit character set being used for text in files and in command line parameters. This allows GMT to ensure that the PostScript output generates the correct characters on the plot.. Choose from Standard, Standard+, ISOLatin1, ISOLatin1+, and ISO-8859-x (where x is in the ranges [1,10] or [13,15]). See Appendix F for details [ISOLatin1+ (or Standard+)].</p>
<dt><code>PS_COLOR_MODEL</code></p>
<dd>Determines whether PostScript output should use RGB, HSV, CMYK, or GRAY when specifying color [rgb]. Note if HSV is selected it does not apply to images which in that case uses RGB. When selecting GRAY, all colors will be converted to gray scale using YIQ (television) conversion.</p>
<dt><code>PS_COMMENTS</code></p>
<dd>(static) If true we will issue comments in the PostScript file that explain the logic of operations. These are useful if you need to edit the file and make changes; otherwise you can set it to false which yields a somewhat slimmer PostScript file [false].</p>
<dt><code>PS_IMAGE_COMPRESS</code></p>
<dd>Determines if PostScript images are compressed using the Run-Length Encoding scheme (rle), Lempel-Ziv-Welch compression (lzw), DEFLATE compression (deflate[,level]), or not at all (none) [deflate,5]. When specifying deflate, the compression level (1&#8211;9) may optionally be appended.</p>
<dt><code>PS_LINE_CAP</code></p>
<dd>Determines how the ends of a line segment will be drawn. Choose among a <i>butt</i> cap (default) where there is no projection beyond the end of the path, a <i>round</i> cap where a semicircular arc with diameter equal to the line-width is drawn around the end points, and <i>square</i> cap where a half square of size equal to the line-width extends beyond the end of the path [butt].</p>
<dt><code>PS_LINE_JOIN</code></p>
<dd>Determines what happens at kinks in line segments. Choose among a <i>miter</i> join where the outer edges of the strokes for the two segments are extended until they meet at an angle (as in a picture frame; if the angle is too acute, a bevel join is used instead, with threshold set by <code>PS_MITER_LIMIT</code>), <i>round</i> join where a circular arc is used to fill in the cracks at the kinks, and <i>bevel</i> join which is a miter join that is cut off so kinks are triangular in shape [miter].</p>
<dt><code>PS_MEDIA</code></p>
<dd>Sets the physical format of the current plot paper [a4 (or letter)]. The following formats (and their widths and heights in points) are recognized (Additional site-specific formats may be specified in the gmt_custom_media.conf file in <code>$GMT_SHAREDIR</code>/conf or ~/.gmt; see that file for details): </p>
<p> Media width height</p>
<dt>&bull;</p>
<dd>A0 2380 3368</p>
<dt>&bull;</p>
<dd>A1 1684 2380</p>
<dt>&bull;</p>
<dd>A2 1190 1684</p>
<dt>&bull;</p>
<dd>A3 842 1190</p>
<dt>&bull;</p>
<dd>A4 595 842</p>
<dt>&bull;</p>
<dd>A5 421 595</p>
<dt>&bull;</p>
<dd>A6 297 421</p>
<dt>&bull;</p>
<dd>A7 210 297</p>
<dt>&bull;</p>
<dd>A8 148 210</p>
<dt>&bull;</p>
<dd>A9 105 148</p>
<dt>&bull;</p>
<dd>A10 74 105</p>
<dt>&bull;</p>
<dd>B0 2836 4008</p>
<dt>&bull;</p>
<dd>B1 2004 2836</p>
<dt>&bull;</p>
<dd>B2 1418 2004</p>
<dt>&bull;</p>
<dd>B3 1002 1418</p>
<dt>&bull;</p>
<dd>B4 709 1002</p>
<dt>&bull;</p>
<dd>B5 501 709</p>
<dt>&bull;</p>
<dd>archA 648 864</p>
<dt>&bull;</p>
<dd>archB 864 1296</p>
<dt>&bull;</p>
<dd>archC 1296 1728</p>
<dt>&bull;</p>
<dd>archD 1728 2592</p>
<dt>&bull;</p>
<dd>archE 2592 3456</p>
<dt>&bull;</p>
<dd>flsa 612 936</p>
<dt>&bull;</p>
<dd>halfletter 396 612</p>
<dt>&bull;</p>
<dd>statement 396 612</p>
<dt>&bull;</p>
<dd>note 540 720</p>
<dt>&bull;</p>
<dd>letter 612 792</p>
<dt>&bull;</p>
<dd>legal 612 1008</p>
<dt>&bull;</p>
<dd>11&#215;17 792 1224</p>
<dt>&bull;</p>
<dd>tabloid 792 1224</p>
<dt>&bull;</p>
<dd>ledger 1224 792 </p>
<p> For a completely custom format (e.g., for large format plotters) you may also specify WxH, where W and H are in points unless you append a unit to each dimension (<code>c</code>, <code>i</code>, <code>m</code> or <code>p</code> [Default]).</p>
<dt><code>PS_MITER_LIMIT</code></p>
<dd>Sets the threshold angle in degrees (integer in range [0,180]) used for mitered joins only. When the angle between joining line segments is smaller than the threshold the corner will be bevelled instead of mitered. The default threshold is 35 degrees. Setting the threshold angle to 0 implies the PostScript default of about 11 degrees. Setting the threshold angle to 180 causes all joins to be beveled.</p>
<dt><code>PS_PAGE_COLOR</code></p>
<dd>Sets the color of the imaging background, i.e., the paper [white].</p>
<dt><code>PS_PAGE_ORIENTATION</code></p>
<dd>(<code>* -P</code>) Sets the orientation of the page. Choose portrait or landscape [landscape].</p>
<dt><code>PS_SCALE_X</code></p>
<dd>Global x-scale (&gt; 0) to apply to plot-coordinates before plotting. Normally used to shrink the entire output down to fit a specific height/width [1.0].</p>
<dt><code>PS_SCALE_Y</code></p>
<dd>Global y-scale (&gt; 0) to apply to plot-coordinates before plotting. Normally used to shrink the entire output down to fit a specific height/width [1.0].</p>
<dt><code>PS_TRANSPARENCY</code></p>
<dd>Sets the transparency mode to use when preparing PS for rendering to PDF. Choose from Color, ColorBurn, ColorDodge, Darken, Difference, Exclusion, HardLight, Hue, Lighten, Luminosity, Multiply, Normal, Overlay, Saturation, SoftLight, and Screen [Normal].</p>
<dt><code>TIME_EPOCH</code></p>
<dd>Specifies the value of the calendar and clock at the origin (zero point) of relative time units (see <code>TIME_UNIT</code>). It is a string of the form yyyy-mm-ddT[hh:mm:ss] (Gregorian) or yyyy-Www-ddT[hh:mm:ss] (ISO) Default is 1970-01-01T00:00:00, the origin of the UNIX time epoch.</p>
<dt><code>TIME_INTERVAL_FRACTION</code></p>
<dd>Determines if partial intervals at the start and end of an axis should be annotated. If the range of the partial interval exceeds the specified fraction of the normal interval stride we will place the annotation centered on the partial interval [0.5].</p>
<dt><code>TIME_IS_INTERVAL</code></p>
<dd>Used when input calendar data should be truncated and adjusted to the middle of the relevant interval. In the following discussion, the unit <code>u</code> can be one of these time units: (<code>y</code> year, <code>o</code> month, <code>u</code> ISO week, <code>d</code> day, <code>h</code> hour, <code>m</code> minute, and <code>s</code> second). <code>TIME_IS_INTERVAL</code> can have any of the following three values: (1) OFF [Default]. No adjustment, time is decoded as given. (2) +<i>n</i><code>u</code>. Activate interval adjustment for input by truncate to previous whole number of <i>n</i> units and then center time on the following interval. (3) &#8211;<i>n</i><code>u</code>. Same, but center time on the previous interval. For example, with <code>TIME_IS_INTERVAL</code> = +1o, an input data string like 1999-12 will be interpreted to mean 1999-12-15T12:00:00.0 (exactly middle of December), while if <code>TIME_IS_INTERVAL</code> = off then that date is interpreted to mean 1999-12-01T00:00:00.0 (start of December) [off].</p>
<dt><code>TIME_REPORT</code></p>
<dd>Controls if a time-stamp should be issued at start of all progress reports. Choose among <code>TIMER_CLOCK</code> (absolute time stamp), <code>TIMER_ELAPSED</code> (time since start of session), or <code>TIMER_NONE</code> [Default].</p>
<dt><code>TIME_SYSTEM</code></p>
<dd>Shorthand for a combination of <code>TIME_EPOCH</code> and <code>TIME_UNIT</code>, specifying which time epoch the relative time refers to and what the units are. Choose from one of the preset systems below (epoch and units are indicated): </p>
<p> JD -4713-11-25T12:00:00 d (Julian Date) </p>
<p> MJD 1858-11-17T00:00:00 d (Modified Julian Date) </p>
<p> J2000 2000-01-01T12:00:00 d (Astronomical time) </p>
<p> S1985 1985-01-01T00:00:00 s (Altimetric time) </p>
<p> UNIX 1970-01-01T00:00:00 s (UNIX time) </p>
<p> RD0001 0001-01-01T00:00:00 s </p>
<p> RATA 0000-12-31T00:00:00 d </p>
<p> This parameter is not stored in the <code>gmt.conf</code> file but is translated to the respective values of <code>TIME_EPOCH</code> and <code>TIME_UNIT</code>.</p>
<dt><code>TIME_UNIT</code></p>
<dd>Specifies the units of relative time data since epoch (see <code>TIME_EPOCH</code>). Choose y (year &#8211; assumes all years are 365.2425 days), o (month &#8211; assumes all months are of equal length y/12), d (day), h (hour), m (minute), or s (second) [s].</p>
<dt><code>TIME_WEEK_START</code></p>
<dd>When weeks are indicated on time axes, this parameter determines the first day of the week for Gregorian calendars. (The ISO weekly calendar always begins weeks with Monday.) [Monday (or Sunday)].</p>
<dt><code>TIME_Y2K_OFFSET_YEAR</code></p>
<dd>When 2-digit years are used to represent 4-digit years (see various <code>FORMAT_DATE</code>s), <code>TIME_Y2K_OFFSET_YEAR</code> gives the first year in a 100-year sequence. For example, if <code>TIME_Y2K_OFFSET_YEAR</code> is 1729, then numbers 29 through 99 correspond to 1729 through 1799, while numbers 00 through 28 correspond to 1800 through 1828. [1950].</dl>
<h2>See Also</h2>
<p><code>gmt</code> , <code>gmtdefaults</code> , <code>gmtcolors</code> , <code>gmtget</code> , <code>gmtset</code></p>
<h2>Copyright</h2>
<p>2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe</p>
