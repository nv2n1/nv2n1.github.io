---
title: "ncea(1)"
name: "ncea"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncea/"
description: "ncea – netCDF Ensemble Averager"
---

<h2>NAME</h2>
<p> ncea &#8211; netCDF Ensemble Averager</p>
<h2>SYNTAX</h2>
<p> ncea [-3] [-4] [-6] [-7] [-A] [&#8211;bfr <i>sz</i>]<i>[-C]</i>[-c]<i>[&#8211;cnk_byt</i> <i>sz</i>]<i>[&#8211;cnk_dmn</i> <i>nm,sz</i>] [&#8211;cnk_map <i>map</i>] [&#8211;cnk_plc <i>plc</i>] [&#8211;cnk_scl <i>sz</i>]<i>[-D</i> <i>dbg_lvl</i>] [-d <i>dim</i>,[ <i>min</i>][,[ <i>max</i>]]] [&#8211;dbl|flt] [-F] [-G <i>gpe_dsc</i>] [-g <i>grp</i>[,&#8230;]] [-h] [&#8211;hdf] [&#8211;hdr_pad <i>sz</i>] [-L <i>dfl_lvl</i>] [-l <i>path</i>] [&#8211;msa] [-n <i>loop</i>] [&#8211;no_tmp_fl] [&#8211;nsm_sfx <i>grp_sfx</i>] [-O] [-p <i>path</i>] [-R] [-r] [&#8211;ram_all] [-t <i>thr_nbr</i>] [&#8211;unn] [-v <i>var</i>[,&#8230;]] [-X <i>box</i>] [-x] [-y <i>op_typ</i>] <i>input-files</i> <i>output-file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ncea</code> performs gridpoint averages of variables across an arbitrary number (an <i>ensemble</i>) of input files, with each file receiving an equal weight in the average. Each variable in the <i>output-file</i> will be the same size as the same variable in any one of the in the <i>input-files</i>, and all <i>input-files</i> must be the same size. Whereas <code>ncra</code> only performs averages over the record dimension (e.g., time), and weights each record in the record dimension evenly, <code>ncea</code> averages entire files, and weights each file evenly. All dimensions, including the record dimension, are treated identically and preserved in the <i>output-file</i>. </p>
<p> The file is the logical unit of organization for the results of many scientific studies. Often one wishes to generate a file which is the gridpoint average of many separate files. This may be to reduce statistical noise by combining the results of a large number of experiments, or it may simply be a step in a procedure whose goal is to compute anomalies from a mean state. In any case, when one desires to generate a file whose properties are the mean of all the input files, then <code>ncea</code> is the operator to use. <code>ncea</code> assumes coordinate variable are properties common to all of the experiments and so does not average them across files. Instead, <code>ncea</code> copies the values of the coordinate variables from the first input file to the output file.</p>
<h2>EXAMPLES</h2>
<p> Consider a model experiment which generated five realizations of one year of data, say 1985. You can imagine that the experimenter slightly perturbs the initial conditions of the problem before generating each new solution. Assume each file contains all twelve months (a seasonal cycle) of data and we want to produce a single file containing the ensemble average (mean) seasonal cycle. Here the numeric filename suffix denotes the experiment number (<i>not</i> the month):</p>
<dl>
<dt>
<dd> ncea 85_01.nc 85_02.nc 85_03.nc 85_04.nc 85_05.nc 85.nc<br />
 ncea 85_0[1-5].nc 85.nc<br />
 ncea -n 5,2,1 85_01.nc 85.nc</dl>
<p> These three commands produce identical answers. The output file, <code>85.nc</code>, is the same size as the inputs files. It contains 12 months of data (which might or might not be stored in the record dimension, depending on the input files), but each value in the output file is the average of the five values in the input files. </p>
<p> In the previous example, the user could have obtained the ensemble average values in a particular spatio-temporal region by adding a hyperslab argument to the command, e.g.,</p>
<dl>
<dt>
<dd> ncea -d time,0,2 -d lat,-23.5,23.5 85_??.nc 85.nc</dl>
<p> In this case the output file would contain only three slices of data in the <i>time</i> dimension. These three slices are the average of the first three slices from the input files. Additionally, only data inside the tropics is included. </p>
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
<h2>HOMEPAGE</h2>
<p> The <code>NCO</code> homepage at &lt;<a rel="nofollow" href="http://nco.sf.net">http://nco.sf.net</a>&gt; contains more information. </p>
<h2>Index</h2>
