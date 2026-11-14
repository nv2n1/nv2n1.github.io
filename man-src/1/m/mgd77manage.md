---
title: "mgd77manage(1)"
name: "mgd77manage"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mgd77manage/"
description: "mgd77manage – Manage the content of MGD77+ files"
---

<h2>NAME</h2>
<p> mgd77manage &#8211; Manage the content of MGD77+ files</p>
<h2>SYNOPSIS</h2>
<p> <code>mgd77manage</code> <i>NGDC-ids</i> [ [<code>+</code>]<code>a</code>|<code>c</code>|<code>d</code>|<code>D</code>|<code>e</code>|<code>E</code>|<code>g</code>|<code>i</code>|<code>n</code>|<code>t</code>|<code>T</code><i>fileinfo</i> ] [ <code>f</code>|<code>g</code>|<code>e</code> ] [ <i>abbrev1</i>,<i>abbrev2</i>,&#8230;) ] [ <i>empty</i> ] [ ] [ <i>abbrev</i>/<i>name</i>/<i>unit</i>/<code>t</code>/<i>scale</i>/<i>offset</i>/<i>comment</i> ] [ <i>unit</i> ] [ <i>region</i> ] [ [<i>level</i>] ] [ <code>-bi</code><i>&lt;binary&gt;</i> ] [ <code>-di</code><i>&lt;nodata&gt;</i> ] [ <code>-n</code><i>&lt;flags&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>mgd77manage</code> deals with maintaining extra custom columns in MGD77+ netCDF files. You can either delete one or more columns, add a new column, update an existing column with new data, or supply error correction information (*.e77 files). New data may come from a table (ASCII unless <code>-bi</code> is used), be based on existing columns and certain theoretical expressions, or they may be obtained by sampling a grid (choose between GMT grid or a Sandwell/Smith Mercator *.img grid) along track. The new data will be appended to the MGD77+ file in the form of an extra data column of specified type. The data file will be modified; no new file will be created. For the big issues, see the DISCUSSION section below.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>NGDC-ids</i></p>
<dd> Can be one or more of five kinds of specifiers:</p>
<dt>1.</p>
<dd> 8-character NGDC IDs, e.g., 01010083, JA010010etc., etc.</p>
<dt>2.</p>
<dd> 2-character &lt;agency&gt; codes which will return all cruises from each agency.</p>
<dt>3.</p>
<dd> 4-character &lt;agency&gt;&lt;vessel&gt; codes, which will return all cruises from those vessels.</p>
<dt>4.</p>
<dd> =&lt;list&gt;, where &lt;list&gt; is a table with NGDC IDs, one per line.</p>
<dt>5.</p>
<dd> If nothing is specified we return all cruises in the data base. </p>
<p> (See mgd77info <code>-L</code> for agency and vessel codes). The &quot;.mgd77&quot; or &quot;.nc&quot; extensions will automatically be appended, if needed (use <code>-I</code> to ignore certain file types). Cruise files will be looked for first in the current directory and second in all directories listed in <code>$MGD77_HOME</code>/mgd77_paths.txt [If <code>$MGD77_HOME</code> is not set it will default to <code>$GMT_SHAREDIR</code>/mgd77].</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code>[<code>+</code>]<code>a</code>|<code>c</code>|<code>d</code>|<code>D</code>|<code>e</code>|<code>E</code>|<code>g</code>|<code>i</code>|<code>n</code>|<code>t</code>|<code>T</code><i>fileinfo</i></p>
<dd> Add a new data column. If an existing column with the same abbreviation already exists in the file we will cowardly refuse to update the file. Specifying <code>-A+</code> overcomes this reluctance (However, sometimes an existing column cannot be upgraded without first deleting it; if so you will be warned). Select a column source code among <code>a</code>, <code>c</code>, <code>d</code>, <code>D</code>, <code>e</code>, <code>g</code>, <code>i</code>, <code>n</code>, <code>t</code>, or <code>T</code>; detailed descriptions for each choice follow: </p>
<p> <code>a</code> Append filename of a single column table to add. File must have the same number of rows as the MGD77+ file. If no file is given we read from stdin instead. </p>
<p> <code>c</code> Create a new column that derives from existing data or formulas for corrections and reference fields. Append <code>c</code> for the Carter corrections subtracted from uncorrected depths, <code>g</code> for the IGF gravity reference field (a.k.a &quot;normal gravity&quot;), <code>m</code> for the IGRF total field magnetic reference field, and <code>r</code> for recomputed magnetic anomaly (append 1 or 2 to specify which total field column to use [1]). For gravity we choose the reference field based on the parameter Gravity Theoretical Formula Code in the cruise&#8217;s MGD77 header. If this is not set or is invalid we default to the IGF 1980. You can override this behavior by appending the desired code: 1 = Heiskanen 1924, 2 = International 1930, 3 = IGF1967, or 4 = IGF1980. </p>
<p> <code>d</code> Append filename of a two-column table with the first column holding distances along track and the second column holding data values. If no file is given we read from stdin instead. Records with matching distances in the MGD77+ file will be assigned the new values; at other distances we set them to NaN. Alternatively, give upper case <code>D</code> instead and we will interpolate the column at all record distances. See <code>-N</code> for choosing distance units and <code>-C</code> for choosing how distances are calculated. </p>
<p> <code>e</code> Expects to find an e77 error/correction log from <code>mgd77sniffer</code> with the name <i>NGDC_ID</i>.e77 in the current directory or in $MGD77_HOME/E77; this file will examined and used to make modifications to the header values, specify a systematic correction for certain columns (such as scale and offset), specify that a certain anomaly should be recalculated from the observations (e.g., recalculate mag from mtf1 and the latest IGRF), and add or update the special column <code>flag</code> which may hold bitflags (0 = GOOD, 1 = BAD) for each data field in the standard MGD77 data set. Any fixed correction terms found (such as needing to scale a field by 0.1 or 10 because the source agency used incorrect units) will be written as attributes to the netCDF MGD77+ file and applied when the data are read by <code>mgd77list</code>. Ephemeral corrections such as those determined by crossover analysis are not kept in the data files but reside in correction tables (see <code>mgd77list</code> for details). By default, the first character of each header line in the e77 file (which is ?, Y or N) will be consulted to see if the corresponding adjustment should be applied. If any undecided settings are found (i.i, ?) we will abort and make no changes. Only records marked Y will be processed. You can override this behavior by appending one or more modifiers to the <code>-Ae</code> command: <code>h</code> will ignore all header corrections, <code>f</code> will ignore all fixed systematic trend corrections, <code>n</code>, <code>v</code>, and <code>s</code> will ignore bitflags pertaining to navigation, data values, and data slopes, respectively. Use <code>-A+e</code> to replace any existing E77 corrections in the file with the new values. Finally, e77 corrections will not be applied if the E77 file has not been verified. Use <code>-AE</code> to ignore the verification status. </p>
<p> <code>g</code> Sample a GMT geographic (lon, lat) grid along the track given by the MGD77+ file using bicubic interpolation (however, see <code>-n</code>). Append name of a GMT grid file. </p>
<p> <code>i</code> Sample a Sandwell/Smith Mercator *.img grid along the track given by the MGD77+ file using bicubic interpolation (however, see <code>-n</code>). Append the img grid filename, followed by the comma-separated data scale (typically 1 or 0.1), the IMG file mode (0-3), and optionally the img grid max latitude [80.738]. The modes stand for the following: (0) Img files with no constraint code, returns data at all points, (1) Img file with constraints coded, return data at all points, (2) Img file with constraints coded, return data only at constrained points and NaN elsewhere, and (3) Img file with constraints coded, return 1 at constraints and 0 elsewhere. </p>
<p> <code>n</code> Append filename of a two-column table with the first column holding the record number (0 to nrows &#8211; 1) and the second column holding data values. If no file is given we read from stdin instead. Records with matching record numbers in the MGD77+ file will be assigned the new values; at other records we set them to NaN. </p>
<p> <code>t</code> Append filename of a two-column table with the first column holding absolute times along track and the second column holding data values. If no file is given we read from stdin instead. Records with matching times in the MGD77+ file will be assigned the new values; at other times we set them to NaN. Alternatively, give upper case <code>T</code> instead and we will interpolate the column at all record times.</p>
<dt><code>-C</code><code>f</code>|<code>g</code>|<code>e</code></p>
<dd> Append a one-letter code to select the procedure for along-track distance calculation when using <code>-Ad</code>|<code>D</code> (see <code>-N</code> for selecting distance units): </p>
<p> <code>f</code> Flat Earth distances. </p>
<p> <code>g</code> Great circle distances [Default]. </p>
<p> <code>e</code> Geodesic distances on current GMT ellipsoid.</p>
<dt><code>-D</code><i>abbrev1</i>,<i>abbrev2</i>,&#8230;)</p>
<dd> Give a comma-separated list of column abbreviations that you want to delete from the MGD77+ files. Do NOT use this option to remove columns that you are replacing with new data (use <code>-A+</code> instead). Because we cannot remove variables from netCDF files we must create a new file without the columns to be deleted. Once the file is successfully created we temporarily rename the old file, change the new filename to the old filename, and finally remove the old, renamed file.</p>
<dt><code>-E</code><i>empty</i></p>
<dd> Give a single character that will be repeated to fill empty string values, e.g., &quot;9&quot; will yield a string like &quot;99999&#8230;&quot; [9].</p>
<dt><code>-F</code></p>
<dd> Force mode. When this mode is active you are empowered to delete or replace even the standard MGD77 set of columns. You better know what you are doing!</p>
<dt><code>-I</code><i>abbrev</i>/<i>name</i>/<i>unit</i>/<code>t</code>/<i>scale</i>/<i>offset</i>/<i>comment</i></p>
<dd> In addition to file information we must specify additional information about the extra column. Specify a short (16 char or less, using lower case letters, digits, or underscores only) abbreviation for the selected data, its more descriptive name, the data unit, the data type 1-character code (<code>b</code>yte, <code>s</code>hort, <code>f</code>loat, <code>i</code>nt, <code>d</code>ouble, or <code>t</code>ext) you want used for storage in the netCDF file, any scale and offset we should apply to the data to make them fit inside the range implied by the chosen storage type, and a general comment (&lt; 128 characters) regarding what these data represent. Note: If text data type is selected then the terms &quot;values&quot; in the <code>-A</code> discussion refer to your text data. Furthermore, the discussion on interpolation does not apply and the NaN value becomes a &quot;no string&quot; value (see <code>-E</code> for what this is). Place quotes around terms with more than one word (e.g., &quot;Corrected Depth&quot;).</p>
<dt><code>-N</code><i>unit</i></p>
<dd> Append the distance unit (see UNITS). [Default is <code>-Nk</code> (km)]. Only relevant when <code>-Ag</code>|<code>i</code> is selected.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. Only relevant when <code>-Ag</code>|<code>i</code> is selected.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. This applies to the input 1- or 2-column data files specified under some of the <code>-A</code> options. The binary input option is only available for numerical data columns.</p>
<dt><code>-di</code><i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN.</p>
<dt><code>-n</code>[<code>b</code>|<code>c</code>|<code>l</code>|<code>n</code>][<code>+a</code>][<code>+b</code><i>BC</i>][<code>+c</code>][<code>+t</code><i>threshold</i>] <i>(more &#8230;)</i></p>
<dd> Select interpolation mode for grids.</p>
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
<h2>UNITS</h2>
<p> For map distance unit, append <i>unit</i> <code>d</code> for arc degree, <code>m</code> for arc minute, and <code>s</code> for arc second, or <code>e</code> for meter [Default], <code>f</code> for foot, <code>k</code> for km, <code>M</code> for statute mile, <code>n</code> for nautical mile, and <code>u</code> for US survey foot. By default we compute such distances using a spherical approximation with great circles. Prepend <code>&#8211;</code> to a distance (or the unit is no distance is given) to perform &quot;Flat Earth&quot; calculations (quicker but less accurate) or prepend <code>+</code> to perform exact geodesic calculations (slower but more accurate).</p>
<h2>CONSEQUENCES OF GRID RESAMPLING</h2>
<p> Resample or sampling of grids will use various algorithms (see <code>-n</code>) that may lead to possible distortions or unexpected results in the resampled values. One expected effect of resampling with splines is the tendency for the new resampled values to slightly exceed the global min/max limits of the original grid. If this is unacceptable, you can impose clipping of the resampled values values so they do not exceed the input min/max values by adding <code>+c</code> to your <code>-n</code> option.</p>
<h2>EXAMPLES</h2>
<p> To append Geosat/ERS-1 gravity version 11.2 as an extra data column in the cruises 01010047.nc and 01010008.nc, storing the values as mGal*10 in a 2-byte short integer, try </p>
<pre>
gmt mgd77manage 01010047 01010008 -Ai10/1/grav.11.2.img \
    -Isatgrav/&quot;Geosat/ERS-1 gravity&quot;/&quot;mGal&quot;/s/10/0/&quot;Sandwell/Smith version 11.2&quot; -V
</pre>
<p> To append a filtered version of magnetics as an extra data column of type float for the cruise 01010047.nc, and interpolate the filtered data at the times given in the MGD77+ file, try </p>
<pre>
gmt mgd77manage 01010047 -ATmymag.tm -Ifiltmag/&quot;Intermediate-wavelength \
    magnetic residuals&quot;/&quot;nTesla&quot;/f/1/0/&quot;Useful for looking for isochrons&quot; -V
</pre>
<p> To delete the existing extra columns satfaa, coastdist, and satvgg from all MGD77+ files, try </p>
<pre>
gmt mgd77manage =allmgd77.lis -Dsatfaa,coastdist,satvgg -V
</pre>
<p> To create a 4-byte float column with the correct IGRF reference field in all MGD77+ files, try </p>
<pre>
gmt mgd77manage =allmgd77.lis -Acm -Iigrf/&quot;IGRF reference \
    field&quot;/&quot;nTesla&quot;/f/1/0/&quot;IGRF version 10 for 1990-2010&quot; -V
</pre>
<h2>DISCUSSION</h2>
<p> <code>1. Preamble</code> </p>
<p> The mgd77 supplement is an attempt to (1) improve on the limited functionality of the existing mgg supplement, (2) incorporate some of the ideas from Scripps&#8217; gmt+ supplement by allowing extra data columns, and (3) add new capabilities for managing marine geophysical trackline data stored in an architecture-independent CF-1.0- and COARDS-compliant netCDF file format. Here are some of the underlying ideas and steps you need to take to maintain your files. </p>
<p> <code>2. Introduction</code> </p>
<p> Our starting point is the MGD77 ASCII data files distributed from NGDC on CD-ROMS, DVD-ROMS, and via FTP. Using Geodas to install the files locally we choose the &quot;Carter corrected depth&quot; option which will fill in the depth column using the two-way travel-times and the Carter tables if twt is present. This step yields ~5000 individual cruise files. Place these in one or more sub-directories of your choice, list these sub-directories (one per line) in the file mgd77_paths.txt, and place that file in the directory pointed to by <code>$MGD77_HOME</code>; if not set this variable defaults to <code>$GMT_SHAREDIR</code>/mgd77. </p>
<p> <code>3. Conversion</code> </p>
<p> Convert the ASCII MGD77 files to the new netCDF MGD77+ format using <code>mgd77convert</code>. Typically, you will make a list of all the cruises to be converted (with or without extension), and you then run mgd77convert =cruises.lis -Fa -Tc -V -Lwe+ &gt; log.txt </p>
<p> The verbose settings will ensure that all problems found during conversion will be reported. The new *.nc files may also be placed in one or more separate sub-directories and these should also be listed in the mgd77_paths.txt file. We suggest you place the directories with *.nc files ahead of the *.mgd77 directories. When you later want to limit a search to files of a certain extension you should use the <code>-I</code> option. </p>
<p> <code>4. Adding new columns</code> </p>
<p> <code>mgd77manage</code> will allow you to add additional data columns to your *.nc files. These can be anything, including text strings, but most likely are numerical values sampled along the track from a supplied grid or an existing column that have been filtered or manipulated for a particular purpose. The format supports up to 32 such extra columns. See this man page for how to add columns. You may later decide to remove some of these columns or update the data associated with a certain column. Data extraction tools such as <code>mgd77list</code> can be used to extract a mix of standard MGD77 columns (navigation, time, and the usual geophysical observations) and your custom columns. </p>
<p> <code>5. Error sources</code> </p>
<p> Before we discuss how to correct errors we will first list the different classes of errors associated with MGD77 data: (1) Header record errors occur when some of the information fields in the header do not comply with the MGD77 specification or required information is missing. <code>mgd77convert</code> will list these errors when the extended verbose setting is selected. These errors typically do not affect the data and are instead errors in the <i>meta-data</i> (2). Fixed systematic errors occur when a particular data column, despite the MGD77 specification, has been encoded incorrectly. This usually means the data will be off by a constant factor such as 10 or 0.1, or in some cases even 1.8288 which converts fathoms to meters. (3) Unknown systematic errors occur when the instrument that recorded the data or the processing that followed introduced signals that appear to be systematic functions of time along track, latitude, heading, or some other combination of terms that have a physical or logical explanation. These terms may sometimes be resolved by data analysis techniques such as along-track and across-track investigations, and will result in correction terms that when applied to the data will remove these unwanted signals in an optimal way. Because these correction terms may change when new data are considered in their determination, such corrections are considered to be ephemeral. (4) Individual data points or sequences of data may violate rules such as being outside of possible ranges or in other ways violate sanity. Furthermore, sequences of points that may be within valid ranges may give rise to data gradients that are unreasonable. The status of every point can therefore be determined and this gives rise to bitflags GOOD or BAD. Our policy is that error sources 1, 2, and 4 will be corrected by supplying the information as meta-data in the relevant *.nc files, whereas the corrections for error source 3 (because they will constantly be improved) will be maintained in a separate list of corrections. </p>
<p> <code>6. Finding errors</code> </p>
<p> The <code>mgd77sniffer</code> is a tool that does a thorough along-track sanity check of the original MGD77 ASCII files and produces a corresponding *.e77 error log. All problems found are encoded in the error log, and recommended fixed correction terms are given, if needed. An analyst may verify that the suggested corrections are indeed valid (we only want to correct truly obvious unit errors), edit these error logs and modify such correction terms and activate them by changing the relevant code key (see <code>mgd77sniffer</code> for more details). <code>mgd77manage</code> can ingest these error logs and (1) correct bad header records given the suggestions in the log, (2) insert scale/offset correction terms to be used when reading certain columns, and (3) insert any bit-flags found. Rerun this step if you later find other problems as all E77 settings or flags will be recreated based on the latest E77 log. </p>
<p> <code>7. Error corrections</code> </p>
<p> The extraction program <code>mgd77list</code> allows for corrections to be applied on-the-fly when data are requested. First, data with BAD bitflags are suppressed. Second, data with fixed systematic correction terms are corrected accordingly. Third, data with ephemeral correction terms will have those corrections applied (if a correction table is supplied). All of these steps require the presence of the relevant meta-data and all can be overruled by the user. In addition, users may add their own bitflags as separate data columns and use <code>mgd77list</code>&#8216;s logical tests to further dictate which data are suppressed from output.</p>
<h2>CREDITS</h2>
<p> The IGRF calculations are based on a Fortran program written by Susan Macmillan, British Geological Survey, translated to C via f2c by Joaquim Luis, and adapted to GMT style by Paul Wessel.</p>
<h2>SEE ALSO</h2>
<p> <code>mgd77convert</code>, <code>mgd77list</code>, <code>mgd77info</code>, <code>mgd77sniffer</code> <code>mgd77track</code> <code>x2sys_init</code></p>
<h2>REFERENCES</h2>
<p> The Marine Geophysical Data Exchange Format &#8211; MGD77, see <i><a rel="nofollow" href="http://www.ngdc.noaa.gov/mgg/dat/geodas/docs/mgd77.txt">http://www.ngdc.noaa.gov/mgg/dat/geodas/docs/mgd77.txt</a></i> </p>
<p> IGRF, see <i><a rel="nofollow" href="http://www.ngdc.noaa.gov/IAGA/vmod/igrf.html">http://www.ngdc.noaa.gov/IAGA/vmod/igrf.html</a></i></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
