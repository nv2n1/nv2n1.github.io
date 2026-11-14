---
title: "g_sham(1)"
name: "g_sham"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_sham/"
description: "g_sham – read/write xmgr and xvgr data sets"
---

<h2>NAME</h2>
<p> g_sham &#8211; read/write xmgr and xvgr data sets </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_sham</code> <code>-f</code><i> graph.xvg </i> <code>-ge</code><i> gibbs.xvg </i> <code>-ene</code><i> esham.xvg </i> <code>-dist</code><i> ener.xvg </i> <code>-histo</code><i> edist.xvg </i> <code>-bin</code><i> bindex.ndx </i> <code>-lp</code><i> prob.xpm </i> <code>-ls</code><i> gibbs.xpm </i> <code>-lsh</code><i> enthalpy.xpm </i> <code>-lss</code><i> entropy.xpm </i> <code>-map</code><i> map.xpm </i> <code>-ls3</code><i> gibbs3.pdb </i> <code>-mdata</code><i> mapdata.xvg </i> <code>-g</code><i> shamlog.log </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-[no]time</code><i></i> <code>-b</code><i> real </i> <code>-e</code><i> real </i> <code>-ttol</code><i> real </i> <code>-n</code><i> int </i> <code>-[no]d</code><i></i> <code>-bw</code><i> real </i> <code>-[no]sham</code><i></i> <code>-tsham</code><i> real </i> <code>-pmin</code><i> real </i> <code>-dim</code><i> vector </i> <code>-ngrid</code><i> vector </i> <code>-xmin</code><i> vector </i> <code>-xmax</code><i> vector </i> <code>-pmax</code><i> real </i> <code>-gmax</code><i> real </i> <code>-emin</code><i> real </i> <code>-emax</code><i> real </i> <code>-nlevels</code><i> int </i> <code>-mname</code><i> string </i></p>
<h2>DESCRIPTION</h2>
<p> g_sham makes multi-dimensional free-energy, enthalpy and entropy plots. g_sham reads one or more xvg files and analyzes data sets. g_sham basic purpose is plotting Gibbs free energy landscapes (option <code> -ls</code>) by Bolzmann inverting multi-dimensional histograms (option <code> -lp</code>) but it can also make enthalpy (option <code> -lsh</code>) and entropy (option <code> -lss</code>) plots. The histograms can be made for any quantities the user supplies. A line in the input file may start with a time (see option <code> -time</code>) and any number of y values may follow. Multiple sets can also be read when they are seperated by &amp; (option <code> -n</code>), in this case only one y value is read from each line. All lines starting with and @ are skipped. </p>
<p> Option <code> -ge</code> can be used to supply a file with free energies when the ensemble is not a Boltzmann ensemble, but needs to be biased by this free energy. One free energy value is required for each (multi-dimensional) data point in the <code> -f</code> input. </p>
<p> Option <code> -ene</code> can be used to supply a file with energies. These energies are used as a weighting function in the single histogram analysis method due to Kumar et. al. When also temperatures are supplied (as a second column in the file) an experimental weighting scheme is applied. In addition the vales are used for making enthalpy and entropy plots. </p>
<p> With option <code> -dim</code> dimensions can be gives for distances. When a distance is 2- or 3-dimensional, the circumference or surface sampled by two particles increases with increasing distance. Depending on what one would like to show, one can choose to correct the histogram and free-energy for this volume effect. The probability is normalized by r and r2 for a dimension of 2 and 3 respectively. A value of -1 is used to indicate an angle in degrees between two vectors: a sin(angle) normalization will be applied. Note that for angles between vectors the inner-product or cosine is the natural quantity to use, as it will produce bins of the same volume.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> graph.xvg</i> <code>Input</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-ge</code><i> gibbs.xvg</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-ene</code><i> esham.xvg</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-dist</code><i> ener.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-histo</code><i> edist.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-bin</code><i> bindex.ndx</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-lp</code><i> prob.xpm</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
<p> <code>-ls</code><i> gibbs.xpm</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
<p> <code>-lsh</code><i> enthalpy.xpm</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
<p> <code>-lss</code><i> entropy.xpm</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
<p> <code>-map</code><i> map.xpm</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
<p> <code>-ls3</code><i> gibbs3.pdb</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Protein data bank file&nbsp;<wbr> </p>
<p> <code>-mdata</code><i> mapdata.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-g</code><i> shamlog.log</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Log file&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 19</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-[no]w</code><i>no </i><br />
&nbsp;<wbr>View output xvg, xpm, eps and pdb files </p>
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-[no]time</code><i>yes </i><br />
&nbsp;<wbr>Expect a time in the input </p>
<p> <code>-b</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>First time to read from set </p>
<p> <code>-e</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>Last time to read from set </p>
<p> <code>-ttol</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Tolerance on time in appropriate units&nbsp;<wbr>(usually ps) </p>
<p> <code>-n</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Read&nbsp;<wbr>&nbsp;<wbr>sets seperated by&nbsp;<wbr>&amp; </p>
<p> <code>-[no]d</code><i>no </i><br />
&nbsp;<wbr>Use the derivative </p>
<p> <code>-bw</code><i> real</i><code> 0.1 </code><br />
&nbsp;<wbr>Binwidth for the distribution </p>
<p> <code>-[no]sham</code><i>yes </i><br />
&nbsp;<wbr>Turn off energy weighting even if energies are given </p>
<p> <code>-tsham</code><i> real</i><code> 298.15</code><br />
&nbsp;<wbr>Temperature for single histogram analysis </p>
<p> <code>-pmin</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Minimum probability. Anything lower than this will be set to zero </p>
<p> <code>-dim</code><i> vector</i><code> 1 1 1</code><br />
&nbsp;<wbr>Dimensions for distances, used for volume correction&nbsp;<wbr>(max 3 values, dimensions&nbsp;<wbr>&nbsp;<wbr>3 will get the same value as the last) </p>
<p> <code>-ngrid</code><i> vector</i><code> 32 32 32</code><br />
&nbsp;<wbr>Number of bins for energy landscapes&nbsp;<wbr>(max 3 values, dimensions&nbsp;<wbr>&nbsp;<wbr>3 will get the same value as the last) </p>
<p> <code>-xmin</code><i> vector</i><code> 0 0 0</code><br />
&nbsp;<wbr>Minimum for the axes in energy landscape&nbsp;<wbr>(see above for&nbsp;<wbr>&nbsp;<wbr>3 dimensions) </p>
<p> <code>-xmax</code><i> vector</i><code> 1 1 1</code><br />
&nbsp;<wbr>Maximum for the axes in energy landscape&nbsp;<wbr>(see above for&nbsp;<wbr>&nbsp;<wbr>3 dimensions) </p>
<p> <code>-pmax</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Maximum probability in output, default is calculate </p>
<p> <code>-gmax</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Maximum free energy in output, default is calculate </p>
<p> <code>-emin</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Minimum enthalpy in output, default is calculate </p>
<p> <code>-emax</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Maximum enthalpy in output, default is calculate </p>
<p> <code>-nlevels</code><i> int</i><code> 25</code><br />
&nbsp;<wbr>Number of levels for energy landscape </p>
<p> <code>-mname</code><i> string</i><br />
&nbsp;<wbr>Legend label for the custom landscape </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
