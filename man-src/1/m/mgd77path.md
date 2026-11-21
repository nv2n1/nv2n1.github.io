---

title: "mgd77path(1)"
name: "mgd77path"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mgd77path/"
description: "mgd77path – Return paths to MGD77 cruises and directories"
---

<h2>NAME</h2>
<p> mgd77path &#8211; Return paths to MGD77 cruises and directories</p>
<p> <code>mgd77path</code> <i>NGDC-ids</i> [ [<code>&#8211;</code>] ] [ ] [ <i>ignore</i> ] [ [<i>level</i>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<p> <code>mgd77path</code> returns the full pathname to one or more MGD77 files. The pathname returned for a given cruise may change with time due to reshuffling of disks/subdirectories.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>NGDC-ids</i></dt>
<dd> Can be one or more of five kinds of specifiers:</dd>
<dt>1.</dt>
<dd> 8-character NGDC IDs, e.g., 01010083, JA010010etc., etc.</dd>
<dt>2.</dt>
<dd> 2-character &lt;agency&gt; codes which will return all cruises from each agency.</dd>
<dt>3.</dt>
<dd> 4-character &lt;agency&gt;&lt;vessel&gt; codes, which will return all cruises from those vessels.</dd>
<dt>4.</dt>
<dd> =&lt;list&gt;, where &lt;list&gt; is a table with NGDC IDs, one per line.</dd>
<dt>5.</dt>
<dd> If nothing is specified we return all cruises in the data base. </dd>
<p> (See mgd77info <code>-L</code> for agency and vessel codes). The &quot;.mgd77&quot; or &quot;.nc&quot; extensions will automatically be appended, if needed (use <code>-I</code> to ignore certain file types). Cruise files will be looked for first in the current directory and second in all directories listed in <code>$MGD77_HOME</code>/mgd77_paths.txt [If <code>$MGD77_HOME</code> is not set it will default to <code>$GMT_SHAREDIR</code>/mgd77].</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code>[<code>&#8211;</code>]</dt>
<dd> Display the full path to each cruise [Default]. Optionally, append <code>&#8211;</code> which will list just the cruise IDs instead.</dd>
<dt><code>-D</code></dt>
<dd> Instead of cruise listings, just show the directory paths currently used in the search.</dd>
<dt><code>-I</code><i>ignore</i></dt>
<dd> Ignore certain data file formats from consideration. Append <code>a|c|t</code> to ignore MGD77 ASCII, MGD77+ netCDF, or plain tab-separated ASCII table files, respectively. The option may be repeated to ignore more than one format. [Default ignores none].</dd>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></dt>
<dd> Select verbosity level [c]. Reports the total number of cruises found.</dd>
<dt><code>-^</code> or just <code>&#8211;</code></dt>
<dd> Print a short message about the syntax of the command, then exits (NOTE: on Windows use just <code>&#8211;</code>).</dd>
<dt><code>-+</code> or just <code>+</code></dt>
<dd> Print an extensive usage (help) message, including the explanation of any module-specific option (but not the GMT common options), then exits.</dd>
<dt><code>-?</code> or no arguments</dt>
<dd> Print a complete usage (help) message, including the explanation of options, then exits.</dd>
<dt><code>&#8211;</code><code>-version</code></dt>
<dd> Print GMT version and exit.</dd>
<dt><code>&#8211;</code><code>-show-datadir</code></dt>
<dd> Print full path to GMT share directory and exit.</dd></dl>
<h2>EXAMPLES</h2>
<p> To obtain pathnames for cruises 01010008 and 01010007, run </p>
<pre>
gmt mgd77path 01010008 01010007
</pre>
<p> To obtain pathnames for cruises 01010008 and 01010007, but only if there are MGD77+ version in netCDF, run </p>
<pre>
gmt mgd77path 01010008 01010007 -Ia -It
</pre>
<p> To see the list of active directories where MGD77 files might be stored, run </p>
<pre>
gmt mgd77path -D
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code> <code>mgd77info</code> <code>mgd77list</code> <code>mgd77manage</code> <code>mgd77track</code></p>
<h2>REFERENCES</h2>
<p> The Marine Geophysical Data Exchange Format &#8211; MGD77, see <i>*<a rel="nofollow" href="http://www.ngdc.noaa.gov/mgg/dat/geodas/docs/mgd77.txt*.">http://www.ngdc.noaa.gov/mgg/dat/geodas/docs/mgd77.txt*.</a></i></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
