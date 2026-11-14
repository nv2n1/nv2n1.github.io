---
title: "ncecat(1)"
name: "ncecat"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncecat/"
description: "ncecat – netCDF Ensemble Concatenator"
---

<h2>NAME</h2>
<p> ncecat &#8211; netCDF Ensemble Concatenator</p>
<h2>SYNTAX</h2>
<p> ncecat [-3] [-4] [-6] [-7] [-A] [&#8211;bfr <i>sz</i>]<i>[-C]</i>[-c]<i>[&#8211;cnk_byt</i> <i>sz</i>]<i>[&#8211;cnk_dmn</i> <i>nm,sz</i>] [&#8211;cnk_map <i>map</i>] [&#8211;cnk_plc <i>plc</i>] [&#8211;cnk_scl <i>sz</i>]<i>[-D</i> <i>dbg_lvl</i>] [-d <i>dim</i>,[ <i>min</i>][,[ <i>max</i>]]] [-F] [-G <i>gpe_dsc</i>] [-g <i>grp</i>[,&#8230;]] [&#8211;gag] [-h] [&#8211;hdr_pad <i>sz</i>] [-L <i>dfl_lvl</i>] [-l <i>path</i>] [-M] [&#8211;mrd] [&#8211;msa] [-n <i>loop</i>] [&#8211;no_tmp_fl] [-O] [-p <i>path</i>] [-R] [-r] [&#8211;ram_all] [-t <i>thr_nbr</i>] [-u <i>ulm_nm</i>] [&#8211;unn] [-v <i>var</i>[,&#8230;]] [-X <i>box</i>] [-x] <i>input-files</i> <i>output-file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ncecat</code> concatenates an arbitrary number of input files into a single output file. Input files are glued together by creating a record dimension in the output file. Input files must be the same size. Each input file is stored consecutively as a single record in the output file. Each variable (except coordinate variables) in each input file becomes one record in the same variable in the output file. Coordinate variables are not concatenated, they are instead simply copied from the first input file to the output-file. Thus, the size of the output file is the sum of the sizes of the input files. </p>
<p> Consider five realizations, <code>85a.nc</code>, <code>85b.nc</code>,<code>&#8230;</code> <code>85e.nc</code> of 1985 predictions from the same climate model. Then <code>ncecat 85?.nc 85_ens.nc</code> glues the individual realizations together into the single file, <code>85_ens.nc</code>. If an input variable was dimensioned [ <code>lat</code>, <code>lon</code>], it will have dimensions [ <code>record</code>, <code>lat</code>, <code>lon</code>] in the output file. A restriction of <code>ncecat</code> is that the hyperslabs of the processed variables must be the same from file to file. Normally this means all the input files are the same size, and contain data on different realizations of the same variables.</p>
<h2>EXAMPLES</h2>
<p> Consider a model experiment which generated five realizations of one year of data, say 1985. You can imagine that the experimenter slightly perturbs the initial conditions of the problem before generating each new solution. Assume each file contains all twelve months (a seasonal cycle) of data and we want to produce a single file containing all the seasonal cycles. Here the numeric filename suffix denotes the experiment number (<i>not</i> the month):</p>
<dl>
<dt>
<dd> ncecat 85_01.nc 85_02.nc 85_03.nc 85_04.nc 85_05.nc 85.nc<br />
 ncecat 85_0[1-5].nc 85.nc<br />
 ncecat -n 5,2,1 85_01.nc 85.nc</dl>
<p> These three commands produce identical answers. The output file, <code>85.nc</code>, is five times the size as a single <i>input-file</i>. It contains 60 months of data (which might or might not be stored in the record dimension, depending on the input files). </p>
<h2>AUTHOR</h2>
<p> <code>NCO</code> manual pages written by Charlie Zender and originally formatted by Brian Mays. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;<a rel="nofollow" href="http://sf.net/bugs/?group_id=3331">http://sf.net/bugs/?group_id=3331</a>&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1995-2012 Charlie Zender<br />
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
