---
title: "mgd77convert(1)"
name: "mgd77convert"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mgd77convert/"
description: "mgd77convert – Convert MGD77 data to other file formats"
---

<h2>NAME</h2>
<p> mgd77convert &#8211; Convert MGD77 data to other file formats</p>
<h2>SYNOPSIS</h2>
<p> <code>mgd77convert</code> <i>NGDC-ids</i> <code>a</code>|<code>c</code>|<code>m</code> |<code>t</code> [<code>+</code>]<code>a</code>|<code>c</code>|<code>m</code>|<code>t</code> [ ] [ ] [ [<code>w</code>][<code>e</code>][<code>+</code>] ] [ [<i>level</i>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>mgd77convert</code> reads versions of MGD77 files and writes the same data in (probably) another format to a new file in the current directory. Both pre- and post-Y2K MGD77 formats can be processed.</p>
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
<p> (See mgd77info <code>-L</code> for agency and vessel codes). The &quot;.mgd77&quot; or &quot;.nc&quot; extensions will automatically be appended, if needed (use <code>-I</code> to ignore certain file types). Cruise files will be looked for first in the current directory and second in all directories listed in <code>$MGD77_HOME</code>/mgd77_paths.txt [If <code>$MGD77_HOME</code> is not set it will default to <code>$GMT_SHAREDIR</code>/mgd77].</p>
<dt><code>-Fa</code>|<code>c</code>|<code>m</code> |<code>t</code></p>
<dd> Specifies the format of the input (From) files. Choose from <code>a</code> for standard MGD77 ASCII table (with extension .mgd77), <code>c</code> for the new MGD77+ netCDF format (with extension .nc), <code>m</code> for the new MGD77 t format (extension .m77t) and <code>t</code> for a plain ASCII tab-separated table dump (with extension .dat). Use <code>-FC</code> to recover the original MGD77 setting from the MGD77+ file [Default will apply any E77 corrections encoded in the file].</p>
<dt><code>-T</code>[<code>+</code>]<code>a</code>|<code>c</code>|<code>m</code> |<code>t</code></p>
<dd> Specifies the format of the output (To) files. Choose from <code>a</code> for standard MGD77 ASCII table (with extension .mgd77), <code>c</code> for the new MGD77+ netCDF format (with extension .nc), <code>m</code> for the new MGD77 t format (extension .m77t) and <code>t</code> for a plain ASCII tab-separated table dump (with extension .dat). We will refuse to create the file(s) if they already exist in the current directory. Prepend <code>+</code> to override this policy.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-C</code></p>
<dd> Convert from NGDC two-file data sets *.h77, *.a77 to single file *.mgd77. No other options (except <code>-V</code>) are allowed. Give one or more names of *.h77 files, *.a77 files, or just the file prefixes.</p>
<dt><code>-D</code></p>
<dd> By default, the storage types used in a MGD77+ netCDF file greatly exceed the precision imposed by the ASCII MGD77 format. However, for the five items <code>faa</code>, <code>eot</code>, <code>mag</code>, <code>diur</code> and <code>msd</code> we use 2-byte integers with implied precisions of 0.1 mGal, 0.1 nTesla, and 1 m as in the MGD77 format. It is possible that at some point these items will need to be stored as 4-byte ints which would allow precisions of 10 fTesla, 1 nGal, and 0.01 mm, respectively. This option activates such storage [Default uses 2-byte integers].</p>
<dt><code>-L</code>[<code>w</code>][<code>e</code>][<code>+</code>]</p>
<dd> Set the level of verification reporting [none] and where to send such reports [stderr]. Append a combination of <code>w</code> for warnings, <code>e</code> for errors, and <code>+</code> to send such log information to stdout.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
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
<h2>EXAMPLES</h2>
<p> To convert a large set of a77,h77 pairs to proper mgd77 files, try </p>
<pre>
gmt mgd77convert -C *.h77
</pre>
<p> To convert 01010047.mgd77 and 01010008.mgd77 to new netCDF .nc files, and capture all verification messages, try </p>
<pre>
gmt mgd77convert 01010047 01010008 -Fa -Tc -V -Lew+ &gt; log.lis
</pre>
<p> To convert 01010047.nc back to MGD77 ASCII and make sure it is identical to the original file, try (Bourne shell syntax) </p>
<pre>
orig=`gmt mgd77path 01010047 -Ic`
gmt mgd77convert 01010047 -Fc -Ta -V
diff $orig 01010047.mgd77
</pre>
<p> To convert 01010047.nc to a plain ASCII table for manual editing, overwriting any existing table, try </p>
<pre>
gmt mgd77convert 01010047 -Fc -T+t -V
</pre>
<p> To recover the original NGDC MGD77 version of 01020051.nc and ignore any E77 corrections, use </p>
<pre>
gmt mgd77convert 01020051 -FC -Ta -V
</pre>
<h2>FILE FORMATS</h2>
<p> <code>mgd77convert</code> handles three different formats. (1) The MGD77 ASCII tables are the established standard for distribution of underway geophysical data to and from the NGDC data center. Normally, only the ship-operations people and the cruise PI might be involved in <i>making</i> an MGD77 ASCII file for transmission to NGDC; users are more interested in <i>reading</i> such files. (2) The MGD77+ netCDF format was developed to facilitate the use of MGD77 data by scientists. It contains all the information of the original MGD77 file and if you convert back and forth you end up with the original. However, file sizes are typically ~30% of the original ASCII format and is much faster to operate on. (3) The plain ASCII tab-separated dump is available for users who need to manually edit the content of a MGD77 file. This is usually easier to do when the columns are tab-separated than when they are all crunched together in the MGD77 punch-card format.</p>
<h2>OTHER TOOLS</h2>
<p> The MGD77+ netCDF files are CF-1.0 and COARDS compliant and can be examined with general-purpose tools such as ncBrowse and ncView.</p>
<h2>SEE ALSO</h2>
<p> <code>mgd77manage</code>, <code>mgd77list</code>, <code>mgd77info</code>, <code>mgd77track</code> <code>x2sys_init</code></p>
<h2>REFERENCES</h2>
<p> ncBrowse, see <i><a rel="nofollow" href="http://www.epic.noaa.gov/java/ncBrowse/">http://www.epic.noaa.gov/java/ncBrowse/</a></i> ncView, see <i><a rel="nofollow" href="http://meteora.ucsd.edu/~pierce/ncview_home_page/">http://meteora.ucsd.edu/~pierce/ncview_home_page/</a></i> The Marine Geophysical Data Exchange Format &#8211; &quot;MGD77&quot;, see <i><a rel="nofollow" href="http://www.ngdc.noaa.gov/mgg/dat/geodas/docs/mgd77.txt">http://www.ngdc.noaa.gov/mgg/dat/geodas/docs/mgd77.txt</a></i></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
