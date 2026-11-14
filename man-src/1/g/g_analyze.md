---
title: "g_analyze(1)"
name: "g_analyze"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_analyze/"
description: "g_analyze – analyzes data sets"
---

<h2>NAME</h2>
<p> g_analyze &#8211; analyzes data sets </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_analyze</code> <code>-f</code><i> graph.xvg </i> <code>-ac</code><i> autocorr.xvg </i> <code>-msd</code><i> msd.xvg </i> <code>-cc</code><i> coscont.xvg </i> <code>-dist</code><i> distr.xvg </i> <code>-av</code><i> average.xvg </i> <code>-ee</code><i> errest.xvg </i> <code>-g</code><i> fitlog.log </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-[no]time</code><i></i> <code>-b</code><i> real </i> <code>-e</code><i> real </i> <code>-n</code><i> int </i> <code>-[no]d</code><i></i> <code>-bw</code><i> real </i> <code>-errbar</code><i> enum </i> <code>-[no]integrate</code><i></i> <code>-aver_start</code><i> real </i> <code>-[no]xydy</code><i></i> <code>-[no]regression</code><i></i> <code>-[no]luzar</code><i></i> <code>-temp</code><i> real </i> <code>-fitstart</code><i> real </i> <code>-smooth</code><i> real </i> <code>-filter</code><i> real </i> <code>-[no]power</code><i></i> <code>-[no]subav</code><i></i> <code>-[no]oneacf</code><i></i> <code>-acflen</code><i> int </i> <code>-[no]normalize</code><i></i> <code>-P</code><i> enum </i> <code>-fitfn</code><i> enum </i> <code>-ncskip</code><i> int </i> <code>-beginfit</code><i> real </i> <code>-endfit</code><i> real </i></p>
<h2>DESCRIPTION</h2>
<p> g_analyze reads an ascii file and analyzes data sets. A line in the input file may start with a time (see option <code> -time</code>) and any number of y values may follow. Multiple sets can also be read when they are seperated by &amp; (option <code> -n</code>), in this case only one y value is read from each line. All lines starting with and @ are skipped. All analyses can also be done for the derivative of a set (option <code> -d</code>). </p>
<p> All options, except for <code> -av</code> and <code> -power</code> assume that the points are equidistant in time. </p>
<p> g_analyze always shows the average and standard deviation of each set. For each set it also shows the relative deviation of the third and forth cumulant from those of a Gaussian distribution with the same standard deviation. </p>
<p> Option <code> -ac</code> produces the autocorrelation function(s). </p>
<p> Option <code> -cc</code> plots the resemblance of set i with a cosine of i/2 periods. The formula is: 2 (int0-T y(t) cos(i pi t) dt)2 / int0-T y(t) y(t) dt </p>
<p> This is useful for principal components obtained from covariance analysis, since the principal components of random diffusion are pure cosines. </p>
<p> Option <code> -msd</code> produces the mean square displacement(s). </p>
<p> Option <code> -dist</code> produces distribution plot(s). </p>
<p> Option <code> -av</code> produces the average over the sets. Error bars can be added with the option <code> -errbar</code>. The errorbars can represent the standard deviation, the error (assuming the points are independent) or the interval containing 90% of the points, by discarding 5% of the points at the top and the bottom. </p>
<p> Option <code> -ee</code> produces error estimates using block averaging. A set is divided in a number of blocks and averages are calculated for each block. The error for the total average is calculated from the variance between averages of the m blocks B_i as follows: error2 = Sum (B_i &#8211; B)2 / (m*(m-1)). These errors are plotted as a function of the block size. Also an analytical block average curve is plotted, assuming that the autocorrelation is a sum of two exponentials. The analytical curve for the block average is: </p>
<p> f(t) = sigma sqrt(2/T ( a (tau1 ((exp(-t/tau1) &#8211; 1) tau1/t + 1)) + </p>
<p> (1-a) (tau2 ((exp(-t/tau2) &#8211; 1) tau2/t + 1)))), where T is the total time. a, tau1 and tau2 are obtained by fitting f2(t) to error2. When the actual block average is very close to the analytical curve, the error is sigma*sqrt(2/T (a tau1 + (1-a) tau2)). The complete derivation is given in B. Hess, J. Chem. Phys. 116:209-217, 2002. </p>
<p> Option <code> -filter</code> prints the RMS high-frequency fluctuation of each set and over all sets with respect to a filtered average. The filter is proportional to cos(pi t/len) where t goes from -len/2 to len/2. len is supplied with the option <code> -filter</code>. This filter reduces oscillations with period len/2 and len by a factor of 0.79 and 0.33 respectively. </p>
<p> Option <code> -g</code> fits the data to the function given with option <code> -fitfn</code>. </p>
<p> Option <code> -power</code> fits the data to b ta, which is accomplished by fitting to a t + b on log-log scale. All points after the first zero or negative value are ignored. </p>
<p> Option <code> -luzar</code> performs a Luzar &amp; Chandler kinetics analysis on output from <code> g_hbond</code>. The input file can be taken directly from <code> g_hbond -ac</code>, and then the same result should be produced.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> graph.xvg</i> <code>Input</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-ac</code><i> autocorr.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-msd</code><i> msd.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-cc</code><i> coscont.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-dist</code><i> distr.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-av</code><i> average.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-ee</code><i> errest.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-g</code><i> fitlog.log</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Log file&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 0</code><br />
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
<p> <code>-n</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Read&nbsp;<wbr>&nbsp;<wbr>sets seperated by&nbsp;<wbr>&amp; </p>
<p> <code>-[no]d</code><i>no </i><br />
&nbsp;<wbr>Use the derivative </p>
<p> <code>-bw</code><i> real</i><code> 0.1 </code><br />
&nbsp;<wbr>Binwidth for the distribution </p>
<p> <code>-errbar</code><i> enum</i><code> none</code><br />
&nbsp;<wbr>Error bars for -av:&nbsp;<wbr><code>&nbsp;<wbr>none</code>,&nbsp;<wbr><code>&nbsp;<wbr>stddev</code>,&nbsp;<wbr><code>&nbsp;<wbr>error</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>90</code> </p>
<p> <code>-[no]integrate</code><i>no </i><br />
&nbsp;<wbr>Integrate data function(s)&nbsp;<wbr>numerically using trapezium rule </p>
<p> <code>-aver_start</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Start averaging the integral from here </p>
<p> <code>-[no]xydy</code><i>no </i><br />
&nbsp;<wbr>Interpret second data set as error in the y values for integrating </p>
<p> <code>-[no]regression</code><i>no </i><br />
&nbsp;<wbr>Perform a linear regression analysis on the data </p>
<p> <code>-[no]luzar</code><i>no </i><br />
&nbsp;<wbr>Do a Luzar and Chandler analysis on a correlation function and related as produced by g_hbond. When in addition the -xydy flag is given the second and fourth column will be interpreted as errors in c(t)&nbsp;<wbr>and n(t). </p>
<p> <code>-temp</code><i> real</i><code> 298.15</code><br />
&nbsp;<wbr>Temperature for the Luzar hydrogen bonding kinetics analysis </p>
<p> <code>-fitstart</code><i> real</i><code> 1 </code><br />
&nbsp;<wbr>Time&nbsp;<wbr>(ps)&nbsp;<wbr>from which to start fitting the correlation functions in order to obtain the forward and backward rate constants for HB breaking and formation </p>
<p> <code>-smooth</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>If&nbsp;<wbr>=&nbsp;<wbr>0, the tail of the ACF will be smoothed by fitting it to an exponential function: y&nbsp;<wbr>=&nbsp;<wbr>A exp(-x/tau) </p>
<p> <code>-filter</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Print the high-frequency fluctuation after filtering with a cosine filter of length&nbsp;<wbr> </p>
<p> <code>-[no]power</code><i>no </i><br />
&nbsp;<wbr>Fit data to: b ta </p>
<p> <code>-[no]subav</code><i>yes </i><br />
&nbsp;<wbr>Subtract the average before autocorrelating </p>
<p> <code>-[no]oneacf</code><i>no </i><br />
&nbsp;<wbr>Calculate one ACF over all sets </p>
<p> <code>-acflen</code><i> int</i><code> -1</code><br />
&nbsp;<wbr>Length of the ACF, default is half the number of frames </p>
<p> <code>-[no]normalize</code><i>yes </i><br />
&nbsp;<wbr>Normalize ACF </p>
<p> <code>-P</code><i> enum</i><code> 0</code><br />
&nbsp;<wbr>Order of Legendre polynomial for ACF&nbsp;<wbr>(0 indicates none):&nbsp;<wbr><code>&nbsp;<wbr>0</code>,&nbsp;<wbr><code>&nbsp;<wbr>1</code>,&nbsp;<wbr><code>&nbsp;<wbr>2</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>3</code> </p>
<p> <code>-fitfn</code><i> enum</i><code> none</code><br />
&nbsp;<wbr>Fit function:&nbsp;<wbr><code>&nbsp;<wbr>none</code>,&nbsp;<wbr><code>&nbsp;<wbr>exp</code>,&nbsp;<wbr><code>&nbsp;<wbr>aexp</code>,&nbsp;<wbr><code>&nbsp;<wbr>exp_exp</code>,&nbsp;<wbr><code>&nbsp;<wbr>vac</code>,&nbsp;<wbr><code>&nbsp;<wbr>exp5</code>,&nbsp;<wbr><code>&nbsp;<wbr>exp7</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>exp9</code> </p>
<p> <code>-ncskip</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Skip N points in the output file of correlation functions </p>
<p> <code>-beginfit</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Time where to begin the exponential fit of the correlation function </p>
<p> <code>-endfit</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>Time where to end the exponential fit of the correlation function, -1 is till the end </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
