---
title: "g_kinetics(1)"
name: "g_kinetics"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_kinetics/"
description: "g_kinetics – derives information about kinetic processes from you trajectories"
---

<h2>NAME</h2>
<p> g_kinetics &#8211; derives information about kinetic processes from you trajectories </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_kinetics</code> <code>-f</code><i> temp.xvg </i> <code>-d</code><i> data.xvg </i> <code>-d2</code><i> data2.xvg </i> <code>-o</code><i> ft_all.xvg </i> <code>-o2</code><i> it_all.xvg </i> <code>-o3</code><i> ft_repl.xvg </i> <code>-ee</code><i> err_est.xvg </i> <code>-g</code><i> remd.log </i> <code>-m</code><i> melt.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-tu</code><i> enum </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-[no]time</code><i></i> <code>-b</code><i> real </i> <code>-e</code><i> real </i> <code>-bfit</code><i> real </i> <code>-efit</code><i> real </i> <code>-T</code><i> real </i> <code>-n</code><i> int </i> <code>-cut</code><i> real </i> <code>-ucut</code><i> real </i> <code>-euf</code><i> real </i> <code>-efu</code><i> real </i> <code>-ei</code><i> real </i> <code>-maxiter</code><i> int </i> <code>-[no]back</code><i></i> <code>-tol</code><i> real </i> <code>-skip</code><i> int </i> <code>-[no]split</code><i></i> <code>-[no]sum</code><i></i> <code>-[no]discrete</code><i></i> <code>-mult</code><i> int </i></p>
<h2>DESCRIPTION</h2>
<p> g_kinetics reads two xvg files, each one containing data for N replicas. The first file contains the temperature of each replica at each timestep,and the second contains real values that can be interpreted as an indicator for folding. If the value in the file is larger than the cutoff it is taken to be unfolded and the other way around. </p>
<p> From these data an estimate of the forward and backward rate constants for folding is made at a reference temperature. In addition,a theoretical melting curve and free energy as a function of temperatureare printed in an xvg file. </p>
<p> The user can give a max value to be regarded as intermediate (<code> -ucut</code>), which, when given will trigger the use of an intermediate state in the algorithm to be defined as those structures that have cutoff DATA ucut. Structures with DATA values larger than ucut will not be regarded as potential folders. In this case 8 parameters are optimized. </p>
<p> The average fraction foled is printed in an xvg file together with the fit to it. If an intermediate is used a further file will show the build of the intermediate and the fit to that process. </p>
<p> The program can also be used with continuous variables (by setting <code> -nodiscrete</code>). In this case kinetics of other processes can be studied. This is very much a work in progress and hence the manual (this information) is lagging behind somewhat. </p>
<p> In order to compile this program you need access to the GNU scientific library.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> temp.xvg</i> <code>Input</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-d</code><i> data.xvg</i> <code>Input</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-d2</code><i> data2.xvg</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-o</code><i> ft_all.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-o2</code><i> it_all.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-o3</code><i> ft_repl.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-ee</code><i> err_est.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-g</code><i> remd.log</i> <code>Output</code><br />
&nbsp;<wbr>Log file&nbsp;<wbr> </p>
<p> <code>-m</code><i> melt.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 19</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-tu</code><i> enum</i><code> ps</code><br />
&nbsp;<wbr>Time unit:&nbsp;<wbr><code>&nbsp;<wbr>ps</code>,&nbsp;<wbr><code>&nbsp;<wbr>fs</code>,&nbsp;<wbr><code>&nbsp;<wbr>ns</code>,&nbsp;<wbr><code>&nbsp;<wbr>us</code>,&nbsp;<wbr><code>&nbsp;<wbr>ms</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>s</code> </p>
<p> <code>-[no]w</code><i>no </i><br />
&nbsp;<wbr>View output xvg, xpm, eps and pdb files </p>
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-[no]time</code><i>yes </i><br />
&nbsp;<wbr>Expect a time in the input </p>
<p> <code>-b</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>First time to read from set </p>
<p> <code>-e</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Last time to read from set </p>
<p> <code>-bfit</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>Time to start the fit from </p>
<p> <code>-efit</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>Time to end the fit </p>
<p> <code>-T</code><i> real</i><code> 298.15</code><br />
&nbsp;<wbr>Reference temperature for computing rate constants </p>
<p> <code>-n</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Read data for&nbsp;<wbr>&nbsp;<wbr>replicas. Only necessary when files are written in xmgrace format using&nbsp;<wbr>@type and&nbsp;<wbr>&amp;&nbsp;<wbr>as delimiters. </p>
<p> <code>-cut</code><i> real</i><code> 0.2 </code><br />
&nbsp;<wbr>Cut-off&nbsp;<wbr>(max)&nbsp;<wbr>value for regarding a structure as folded </p>
<p> <code>-ucut</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Cut-off&nbsp;<wbr>(max)&nbsp;<wbr>value for regarding a structure as intermediate&nbsp;<wbr>(if not folded) </p>
<p> <code>-euf</code><i> real</i><code> 10 </code><br />
&nbsp;<wbr>Initial guess for energy of activation for folding&nbsp;<wbr>(kJ/mole) </p>
<p> <code>-efu</code><i> real</i><code> 30 </code><br />
&nbsp;<wbr>Initial guess for energy of activation for unfolding&nbsp;<wbr>(kJ/mole) </p>
<p> <code>-ei</code><i> real</i><code> 10 </code><br />
&nbsp;<wbr>Initial guess for energy of activation for intermediates&nbsp;<wbr>(kJ/mole) </p>
<p> <code>-maxiter</code><i> int</i><code> 100</code><br />
&nbsp;<wbr>Max number of iterations </p>
<p> <code>-[no]back</code><i>yes </i><br />
&nbsp;<wbr>Take the back reaction into account </p>
<p> <code>-tol</code><i> real</i><code> 0.001 </code><br />
&nbsp;<wbr>Absolute tolerance for convergence of the Nelder and Mead simplex algorithm </p>
<p> <code>-skip</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Skip points in the output xvg file </p>
<p> <code>-[no]split</code><i>yes </i><br />
&nbsp;<wbr>Estimate error by splitting the number of replicas in two and refitting </p>
<p> <code>-[no]sum</code><i>yes </i><br />
&nbsp;<wbr>Average folding before computing chi2 </p>
<p> <code>-[no]discrete</code><i>yes </i><br />
&nbsp;<wbr>Use a discrete folding criterium&nbsp;<wbr>(F &#8211; U)&nbsp;<wbr>or a continuous one </p>
<p> <code>-mult</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Factor to multiply the data with before discretization </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
