---
title: "ncra(1)"
name: "ncra"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncra/"
description: "ncra – netCDF Record Averager"
---

<h2>NAME</h2>
<p> ncra &#8211; netCDF Record Averager</p>
<h2>SYNTAX</h2>
<p> ncra [-3] [-4] [-6] [-7] [-A] [&#8211;bfr <i>sz</i>]<i>[-C]</i>[-c]<i>[&#8211;cnk_byt</i> <i>sz</i>]<i>[&#8211;cnk_dmn</i> <i>nm,sz</i>] [&#8211;cnk_map <i>map</i>] [&#8211;cnk_plc <i>plc</i>] [&#8211;cnk_scl <i>sz</i>]<i>[-D</i> <i>dbg_lvl</i>] [-d <i>dim</i>,[ <i>min</i>][,[ <i>max</i>]][, <i>stride</i>[[,[ <i>subcycle</i>]]]]] [&#8211;dbl|flt] [-F] [-G <i>gpe_dsc</i>] [-g <i>grp</i>[,&#8230;]] [-h] [&#8211;hdf] [&#8211;hdr_pad <i>sz</i>] [-L <i>dfl_lvl</i>] [-l <i>path</i>] [&#8211;mro] [&#8211;msa] [-n <i>loop</i>] [&#8211;no_cll_mth] [&#8211;no_tmp_fl] [-O] [-p <i>path</i>] [-R] [-r] [&#8211;ram_all] [&#8211;rec_apn] [-t <i>thr_nbr</i>] [&#8211;unn] [-v <i>var</i>[,&#8230;]] [-X <i>box</i>] [-x] [-y <i>op_typ</i>] <i>input-files</i> <i>output-file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ncra</code> averages record variables across an arbitrary number of input files. The record dimension is retained as a degenerate (size 1) dimension in the output variables. </p>
<p> Input files may vary in size, but each must have a record dimension. The record coordinate, if any, should be monotonic for (or else non-fatal warnings may be generated). Hyperslabs of the record dimension which include more than one file are handled correctly. <code>ncra</code> supports the <i>stride</i> argument to the <code>-d</code> hyperslab option for the record dimension only, <i>stride</i> is not supported for non-record dimensions. </p>
<p> <code>ncra</code> weights each record (e.g., time slice) in the <i>input-files</i> equally. <code>ncra</code> does not attempt to see if, say, the <code>time</code> coordinate is irregularly spaced and thus would require a weighted average in order to be a true time average.</p>
<h2>EXAMPLES</h2>
<p> Average files <code>85.nc</code>, <code>86.nc</code>, &nbsp;<wbr>&#8230;&nbsp;<wbr> <code>89.nc</code> along the record dimension, and store the results in <code>8589.nc</code>:</p>
<dl>
<dt>
<dd> ncra 85.nc 86.nc 87.nc 88.nc 89.nc 8589.nc<br />
 ncra 8[56789].nc 8589.nc<br />
 ncra -n 5,2,1 85.nc 8589.nc</dl>
<p> These three methods produce identical answers. </p>
<p> Assume the files <code>85.nc</code>, <code>86.nc</code>, &nbsp;<wbr>&#8230;&nbsp;<wbr> <code>89.nc</code> each contain a record coordinate <i>time</i> of length 12 defined such that the third record in <code>86.nc</code> contains data from March 1986, etc. NCO knows how to hyperslab the record dimension across files. Thus, to average data from December, 1985 through February, 1986:</p>
<dl>
<dt>
<dd> ncra -d time,11,13 85.nc 86.nc 87.nc 8512_8602.nc<br />
 ncra -F -d time,12,14 85.nc 86.nc 87.nc 8512_8602.nc</dl>
<p> The file <code>87.nc</code> is superfluous, but does not cause an error. The <code>-F</code> turns on the Fortran (1-based) indexing convention. The following uses the <i>stride</i> option to average all the March temperature data from multiple input files into a single output file</p>
<dl>
<dt>
<dd> ncra -F -d time,3,,12 -v temperature 85.nc 86.nc 87.nc 858687_03.nc</dl>
<p> Assume the <i>time</i> coordinate is incrementally numbered such that January, 1985 = 1 and December, 1989 = 60. Assuming <code>??</code> only expands to the five desired files, the following averages June, 1985&#8211;June, 1989:</p>
<dl>
<dt>
<dd> ncra -d time,6.,54. ??.nc 8506_8906.nc</dl>
<h2>AUTHOR</h2>
<p> <code>NCO</code> manual pages written by Charlie Zender and originally formatted by Brian Mays. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;<a rel="nofollow" href="http://sf.net/bugs/?group_id=3331">http://sf.net/bugs/?group_id=3331</a>&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1995-2014 Charlie Zender<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>NCO</code> is maintained as a Texinfo manual called the <code>NCO User&#8217;s Guide.</code> Because <code>NCO</code> is mathematical in nature, the documentation includes TeX-intensive portions not viewable on character-based displays. Hence the only complete and authoritative versions of the <code>NCO User&#8217;s Guide </code> are the PDF (recommended), DVI, and Postscript versions at &lt;<a rel="nofollow" href="http://nco.sf.net/nco.pdf">http://nco.sf.net/nco.pdf</a>&gt;, &lt;<a href="http://nco.sf.net/nco.dvi">http://nco.sf.net/nco.dvi</a>&gt;, and &lt;<a rel="nofollow" href="http://nco.sf.net/nco.ps">http://nco.sf.net/nco.ps</a>&gt;, respectively. HTML and XML versions are available at &lt;<a rel="nofollow" href="http://nco.sf.net/nco.html">http://nco.sf.net/nco.html</a>&gt; and &lt;<a rel="nofollow" href="http://nco.sf.net/nco.xml">http://nco.sf.net/nco.xml</a>&gt;, respectively. </p>
<p> If the <code>info</code> and <code>NCO</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info nco</code></dl>
<p> should give you access to the complete manual, except for the TeX-intensive portions. </p>
<p> <code><a href="/docs/linux/man/1-ncap/">ncap</a></code>(1), <code><a href="/docs/linux/man/1-ncap2/">ncap2</a></code>(1), <code><a href="/docs/linux/man/1-ncatted/">ncatted</a></code>(1), <code><a href="/docs/linux/man/1-ncbo/">ncbo</a></code>(1), <code><a href="/docs/linux/man/1-ncdiff/">ncdiff</a></code>(1), <code><a href="/docs/linux/man/1-nces/">nces</a></code>(1), <code><a href="/docs/linux/man/1-ncecat/">ncecat</a></code>(1), <code><a href="/docs/linux/man/1-ncflint/">ncflint</a></code>(1), <code><a href="/docs/linux/man/1-ncks/">ncks</a></code>(1), <code><a href="/docs/linux/man/1-nco/">nco</a></code>(1), <code><a href="/docs/linux/man/1-ncpdq/">ncpdq</a></code>(1), <code><a href="/docs/linux/man/1-ncra/">ncra</a></code>(1), <code><a href="/docs/linux/man/1-ncrcat/">ncrcat</a></code>(1), <code><a href="/docs/linux/man/1-ncrename/">ncrename</a></code>(1), <code><a href="/docs/linux/man/1-ncwa/">ncwa</a></code>(1) </p>
<h2>HOMEPAGE</h2>
<p> The <code>NCO</code> homepage at &lt;<a rel="nofollow" href="http://nco.sf.net">http://nco.sf.net</a>&gt; contains more information. </p>
<h2>Index</h2>
