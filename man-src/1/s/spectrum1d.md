---
title: "spectrum1d(1)"
name: "spectrum1d"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spectrum1d/"
description: "spectrum1d – Compute auto- [and cross- ] spectra from one [or two] time-series"
---

<h2>NAME</h2>
<p> spectrum1d &#8211; Compute auto- [and cross- ] spectra from one [or two] time-series</p>
<h2>SYNOPSIS</h2>
<p> <code>spectrum1d</code> [ <i>table</i> ] <i>segment_size</i>] [ [<code>xycnpago</code>] ] [ <i>dt</i> ] [ [<code>h</code>|<code>m</code>] ] [ [<i>name_stem</i> ] ] [ ] [ ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-d</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-g</code><i>&lt;gaps&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>spectrum1d</code> reads X [and Y] values from the first [and second] columns on standard input [or <i>x[y]file</i>]. These values are treated as timeseries X(t) [Y(t)] sampled at equal intervals spaced <i>dt</i> units apart. There may be any number of lines of input. <code>spectrum1d</code> will create file[s] containing auto- [and cross- ] spectral density estimates by Welch&#8217;s method of ensemble averaging of multiple overlapped windows, using standard error estimates from Bendat and Piersol. </p>
<p> The output files have 3 columns: f or w, p, and e. f or w is the frequency or wavelength, p is the spectral density estimate, and e is the one standard deviation error bar size. These files are named based on <i>name_stem</i>. If the <code>-C</code> option is used, up to eight files are created; otherwise only one (xpower) is written. The files (which are ASCII unless <code>-bo</code> is set) are as follows:</p>
<dl>
<dt><i>name_stem</i>.xpower</p>
<dd> Power spectral density of X(t). Units of X * X * <i>dt</i>.</p>
<dt><i>name_stem</i>.ypower</p>
<dd> Power spectral density of Y(t). Units of Y * Y * <i>dt</i>.</p>
<dt><i>name_stem</i>.cpower</p>
<dd> Power spectral density of the coherent output. Units same as ypower.</p>
<dt><i>name_stem</i>.npower</p>
<dd> Power spectral density of the noise output. Units same as ypower.</p>
<dt><i>name_stem</i>.gain</p>
<dd> Gain spectrum, or modulus of the transfer function. Units of (Y / X).</p>
<dt><i>name_stem</i>.phase</p>
<dd> Phase spectrum, or phase of the transfer function. Units are radians.</p>
<dt><i>name_stem</i>.admit</p>
<dd> Admittance spectrum, or real part of the transfer function. Units of (Y / X).</p>
<dt><i>name_stem</i>.coh</p>
<dd> (Squared) coherency spectrum, or linear correlation coefficient as a function of frequency. Dimensionless number in [0, 1]. The Signal-to-Noise-Ratio (SNR) is coh / (1 &#8211; coh). SNR = 1 when coh = 0.5. </p>
<p> In addition, a single file with all of the above as individual columns will be written to <i>stdout</i> (unless disabled via <code>-T</code>).</dl>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-S</code><i>segment_size</i>]</p>
<dd> <i>segment_size</i> is a radix-2 number of samples per window for ensemble averaging. The smallest frequency estimated is 1.0/(<i>segment_size</i> * <i>dt</i>), while the largest is 1.0/(2 * <i>dt</i>). One standard error in power spectral density is approximately 1.0 / sqrt(<i>n_data</i> / <i>segment_size</i>), so if <i>segment_size</i> = 256, you need 25,600 data to get a one standard error bar of 10%. Cross-spectral error bars are larger and more complicated, being a function also of the coherency.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>) files holding X(t) [Y(t)] samples in the first 1 [or 2] columns. If no files are specified, <code>spectrum1d</code> will read from standard input.</p>
<dt><code>-C</code>[<code>xycnpago</code>]</p>
<dd> Read the first two columns of input as samples of two time-series, X(t) and Y(t). Consider Y(t) to be the output and X(t) the input in a linear system with noise. Estimate the optimum frequency response function by least squares, such that the noise output is minimized and the coherent output and the noise output are uncorrelated. Optionally specify up to 8 letters from the set { <code>x y c n p a g o</code> } in any order to create only those output files instead of the default [all]. <code>x</code> = xpower, <code>y</code> = ypower, <code>c</code> = cpower, <code>n</code> = npower, <code>p</code> = phase, <code>a</code> = admit, <code>g</code> = gain, <code>o</code> = coh.</p>
<dt><code>-D</code><i>dt</i></p>
<dd> <i>dt</i> Set the spacing between samples in the time-series [Default = 1].</p>
<dt><code>-L</code></p>
<dd> Leave trend alone. By default, a linear trend will be removed prior to the transform. Alternatively, append <code>m</code> to just remove the mean value or <code>h</code> to remove the mid-value.</p>
<dt><code>-N</code>[<i>name_stem</i>]</p>
<dd> Supply an alternate name stem to be used for output files [Default = &quot;spectrum&quot;]. Giving no argument will disable the writing of individual output files.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-T</code></p>
<dd> Disable the writing of a single composite results file to stdout.</p>
<dt><code>-W</code></p>
<dd> Write Wavelength rather than frequency in column 1 of the output file[s] [Default = frequency, (cycles / <i>dt</i>)].</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 2 input columns].</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output. [Default is 2 output columns].</p>
<dt><code>-d</code>[<code>i</code>|<code>o</code>]<i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN and do the reverse on output.</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
<dt><code>-g</code>[<code>a</code>]<code>x</code>|<code>y</code>|<code>d</code>|<code>X</code>|<code>Y</code>|<code>D</code>|[<i>col</i>]<code>z</code>[+|-]<i>gap</i>[<code>u</code>] <i>(more &#8230;)</i></p>
<dd> Determine data gaps and line breaks.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
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
<h2>ASCII FORMAT PRECISION</h2>
<p> The ASCII output formats of numerical data are controlled by parameters in your <code>gmt.conf</code> file. Longitude and latitude are formatted according to <i>FORMAT_GEO_OUT</i>, whereas other values are formatted according to <i>FORMAT_FLOAT_OUT</i>. Be aware that the format in effect can lead to loss of precision in the output, which can lead to various problems downstream. If you find the output is not written with enough precision, consider switching to binary output (<code>-bo</code> if available) or specify more decimals using the <i>FORMAT_FLOAT_OUT</i> setting.</p>
<h2>EXAMPLES</h2>
<p> Suppose data.g is gravity data in mGal, sampled every 1.5 km. To write its power spectrum, in mGal**2-km, to the file data.xpower, use </p>
<pre>
gmt spectrum1d data.g -S256 -D1.5 -Ndata
</pre>
<p> Suppose in addition to data.g you have data.t, which is topography in meters sampled at the same points as data.g. To estimate various features of the transfer function, considering data.t as input and data.g as output, use </p>
<pre>
paste data.t data.g | gmt spectrum1d -S256 -D1.5 -Ndata -C &gt; results.txt
</pre>
<h2>TUTORIAL</h2>
<p> The output of spectrum1d is in units of power spectral density, and so to get units of data-squared you must divide by delta_t, where delta_t is the sample spacing. (There may be a factor of 2 pi somewhere, also. If you want to be sure of the normalization, you can determine a scale factor from Parseval&#8217;s theorem: the sum of the squares of your input data should equal the sum of the squares of the outputs from spectrum1d, if you are simply trying to get a periodogram. [See below.]) </p>
<p> Suppose we simply take a data set, x(t), and compute the discrete Fourier transform (DFT) of the entire data set in one go. Call this X(f). Then suppose we form X(f) times the complex conjugate of X(f). </p>
<p> P_raw(f) = X(f) * X'(f), where the &#8216; indicates complex conjugation. </p>
<p> P_raw is called the periodogram. The sum of the samples of the periodogram equals the sum of the samples of the squares of x(t), by Parseval&#8217;s theorem. (If you use a DFT subroutine on a computer, usually the sum of P_raw equals the sum of x-squared, times M, where M is the number of samples in x(t).) </p>
<p> Each estimate of X(f) is now formed by a weighted linear combination of all of the x(t) values. (The weights are sometimes called &quot;twiddle factors&quot; in the DFT literature.) So, no matter what the probability distribution for the x(t) values is, the probability distribution for the X(f) values approaches [complex] Gaussian, by the Central Limit Theorem. This means that the probability distribution for P_raw(f) approaches chi-squared with two degrees of freedom. That reduces to an exponential distribution, and the variance of the estimate of P_raw is proportional to the square of the mean, that is, the expected value of P_raw. </p>
<p> In practice if we form P_raw, the estimates are hopelessly noisy. Thus P_raw is not useful, and we need to do some kind of smoothing or averaging to get a useful estimate, P_useful(f). </p>
<p> There are several different ways to do this in the literature. One is to form P_raw and then smooth it. Another is to form the auto-covariance function of x(t), smooth, taper and shape it, and then take the Fourier transform of the smoothed, tapered and shaped auto-covariance. Another is to form a parametric model for the auto-correlation structure in x(t), then compute the spectrum of that model. This last approach is what is done in what is called the &quot;maximum entropy&quot; or &quot;Berg&quot; or &quot;Box-Jenkins&quot; or &quot;ARMA&quot; or &quot;ARIMA&quot; methods. </p>
<p> Welch&#8217;s method is a tried-and-true method. In his method, you choose a segment length, <code>-S</code><i>N</i>, so that estimates will be made from segments of length <i>N</i>. The frequency samples (in cycles per delta_t unit) of your P_useful will then be at <i>k</i> /(<i>N</i> * <i>delta_t</i>), where <i>k</i> is an integer, and you will get <i>N</i> samples (since the spectrum is an even function of <i>f</i>, only <i>N</i>/2 of them are really useful). If the length of your entire data set, x(t), is <i>M</i> samples long, then the variance in your P_useful will decrease in proportion to <i>N/M</i>. Thus you need to choose <i>N</i> &lt;&lt; <i>M</i> to get very low noise and high confidence in P_useful. There is a trade-off here; see below. </p>
<p> There is an additional reduction in variance in that Welch&#8217;s method uses a Von Hann spectral window on each sample of length <i>N</i>. This reduces side lobe leakage and has the effect of smoothing the (<i>N</i> segment) periodogram as if the X(f) had been convolved with [1/4, 1/2, 1/4] prior to forming P_useful. But this slightly widens the spectral bandwidth of each estimate, because the estimate at frequency sample <i>k</i> is now a little correlated with the estimate at frequency sample k+1. (Of course this would also happen if you simply formed P_raw and then smoothed it.) </p>
<p> Finally, Welch&#8217;s method also uses overlapped processing. Since the Von Hann window is large in the middle and tapers to near zero at the ends, only the middle of the segment of length <i>N</i> contributes much to its estimate. Therefore in taking the next segment of data, we move ahead in the x(t) sequence only <i>N</i>/2 points. In this way, the next segment gets large weight where the segments on either side of it will get little weight, and vice versa. This doubles the smoothing effect and ensures that (if <i>N</i> &lt;&lt; <i>M</i>) nearly every point in x(t) contributes with nearly equal weight in the final answer. </p>
<p> Welch&#8217;s method of spectral estimation has been widely used and widely studied. It is very reliable and its statistical properties are well understood. It is highly recommended in such textbooks as &quot;Random Data: Analysis and Measurement Procedures&quot; by Bendat and Piersol. </p>
<p> In all problems of estimating parameters from data, there is a classic trade-off between resolution and variance. If you want to try to squeeze more resolution out of your data set, then you have to be willing to accept more noise in the estimates. The same trade-off is evident here in Welch&#8217;s method. If you want to have very low noise in the spectral estimates, then you have to choose <i>N</i> &lt;&lt; <i>M</i>, and this means that you get only <i>N</i> samples of the spectrum, and the longest period that you can resolve is only <i>N</i> * <i>delta_t</i>. So you see that reducing the noise lowers the number of spectral samples and lowers the longest period. Conversely, if you choose <i>N</i> approaching <i>M</i>, then you approach the periodogram with its very bad statistical properties, but you get lots of samples and a large fundamental period. </p>
<p> The other spectral estimation methods also can do a good job. Welch&#8217;s method was selected because the way it works, how one can code it, and its effects on statistical distributions, resolution, side-lobe leakage, bias, variance, etc. are all easily understood. Some of the other methods (e.g. Maximum Entropy) tend to hide where some of these trade-offs are happening inside a &quot;black box&quot;.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grdfft</code></p>
<h2>REFERENCES</h2>
<p> Bendat, J. S., and A. G. Piersol, 1986, Random Data, 2nd revised ed., John Wiley &amp; Sons. </p>
<p> Welch, P. D., 1967, The use of Fast Fourier Transform for the estimation of power spectra: a method based on time averaging over short, modified periodograms, IEEE Transactions on Audio and Electroacoustics, Vol AU-15, No 2.</p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
