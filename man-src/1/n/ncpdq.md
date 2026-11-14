---
title: "ncpdq(1)"
name: "ncpdq"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncpdq/"
description: "ncpdq – netCDF Permute Dimensions Quickly, Pack Data Quietly…"
---

<h2>NAME</h2>
<p> ncpdq &#8211; netCDF Permute Dimensions Quickly, Pack Data Quietly&#8230;</p>
<h2>SYNTAX</h2>
<p> ncpdq [-3] [-4] [-6] [-7] [-A] [-a <i>dim</i>[,&#8230;]] [&#8211;bfr <i>sz</i>]<i>[-C]</i>[-c]<i>[&#8211;cnk_byt</i> <i>sz</i>]<i>[&#8211;cnk_dmn</i> <i>nm,sz</i>] [&#8211;cnk_map <i>map</i>] [&#8211;cnk_plc <i>plc</i>] [&#8211;cnk_scl <i>sz</i>]<i>[-D</i> <i>dbg_lvl</i>] [-d <i>dim</i>,[ <i>min</i>][,[ <i>max</i>]]] [-F] [-G <i>gpe_dsc</i>] [-g <i>grp</i>[,&#8230;]] [-h] [&#8211;hdf] [&#8211;hdr_pad <i>sz</i>] [-L <i>dfl_lvl</i>] [-l <i>path</i>] [-M <i>pck_map</i>] [&#8211;mrd] [&#8211;msa] [&#8211;no_tmp_fl] [-O] [-o <i>output-file</i>] [-P <i>pck_plc</i>] [-p <i>path</i>] [-R] [-r] [&#8211;ram_all] [-t <i>thr_nbr</i>] [&#8211;unn] [-v <i>var</i>[,&#8230;]] [-X <i>box</i>] [-x] <i>input-file</i> [ <i>output-file</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>ncpdq</code> packs or re-shapes variables in <i>input-file</i> and stores them in <i>output-file.</i> Which variables to pack/unpack are determined by the packing policy encoded in the <i>pck_plc</i> argument to the <code>-P</code> switch. Valid <i>pck_plc</i> options are <i>all_new,</i> <i>all_xst,</i> <i>xst_new,</i> and <i>upk.</i> The numeric type of variable to pack or re-pack a variable to is determined by the packing map encoded in the <i>pck_map</i> argument to the <code>-M</code> switch. Valid <i>pck_map</i> options are <i>flt_byt,</i> <i>flt_sht,</i> <i>hgh_byt,</i> <i>hgh_sht,</i> and <i>nxt_lsr.</i> </p>
<p> <code>ncpdq </code> re-shapes variables in <i>input-file</i> by re-ordering and/or reversing dimensions specified in the dimension list. The dimension list is a comma separated list of dimension names, optionally prefixed by negative signs, that follow the <code>-a</code> switch. To re-order variables by a subset of their dimensions, specify these dimensions in a comma-separated list following <code>-a</code>, e.g., <code>-a lon,lat.</code> To reverse a dimension, prefix its name with a negative sign in the dimension list, e.g., <code>-a -lat.</code> Re-ordering and reversal may be performed simultaneously, e.g., <code>-a lon,-lat,time,-lev.</code> </p>
<p> Users may specify any permutation of dimensions, including permutations which change the record dimension identity. The record dimension is re-ordered like any other dimension. The record dimension is always the most slowly varying dimension in a record variable. The specified re-ordering will fail if it requires creating more than one record dimension amongst all the output variables. </p>
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
