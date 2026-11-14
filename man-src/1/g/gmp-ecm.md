---
title: "gmp-ecm(1)"
name: "gmp-ecm"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmp-ecm/"
description: "ecm – integer factorization using ECM, P-1 or P+1"
---

<h2 class="name">NAME</h2>
<p> ecm &#8211; integer factorization using ECM, P-1 or P+1 </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ecm</code> [<code>options</code>] <i>B1</i> [<i>B2min</i>&#8211;<i>B2max</i> | <i>B2</i>]</p>
<dd>
</dl>
<h2>DESCRIPTION</h2>
<dd>ecm is an integer factoring program using the Elliptic Curve Method (ECM), the P-1 method, or the P+1 method. The following sections describe parameters relevant to these algorithms.</p>
<h2>STEP 1 AND STEP 2 BOUND PARAMETERS</h2>
<p> <i>B1</i></p>
<dl>
<dt>
<dd> <i>B1</i> is the step 1 bound. It is a mandatory parameter. It can be given either in integer format (for example 3000000) or in floating-point format (3000000.0 or 3e6). The largest possible <i>B1</i> value is 9007199254740996 for P-1, and ULONG_MAX or 9007199254740996 (whichever is smaller) for ECM and P+1. All primes 2 &lt;= p &lt;= <i>B1</i> are processed in step 1.</dl>
<p> <i>B2</i></p>
<dl>
<dt>
<dd> <i>B2</i> is the step 2 bound. It is optional: if omitted, a default value is computed from <i>B1</i>, which should be close to optimal. Like <i>B1</i>, it can be given either in integer or in floating-point format. The largest possible value of <i>B2</i> is approximately 9e23, but depends on the number of blocks <i>k</i> if you specify the <code>-k</code> option. All primes <i>B1</i> &lt;= p &lt;= <i>B2</i> are processed in step 2. If <i>B2</i> &lt; <i>B1</i>, no step 2 is performed.</dl>
<p> <i>B2min</i><code>&#8211;</code><i>B2max</i></p>
<dl>
<dt>
<dd> alternatively one may use the <i>B2min</i>&#8211;<i>B2max</i> form, which means that all primes <i>B2min</i> &lt;= p &lt;= <i>B2max</i> should be processed. Thus specifying <i>B2</i> only corresponds to <i>B1</i>&#8211;<i>B2</i>. The values of <i>B2min</i> and <i>B2max</i> may be arbitrarily large, but their difference must not exceed approximately 9e23, subject to the number of blocks <i>k</i>.</dl>
<h2>FACTORING METHOD</h2>
<p> <code>-pm1</code></p>
<dl>
<dt>
<dd> Perform P-1 instead of the default method (ECM).</dl>
<p> <code>-pp1</code></p>
<dl>
<dt>
<dd> Perform P+1 instead of the default method (ECM).</dl>
<p> <code>-t </code><i>n</i></p>
<dl>
<dt>
<dd> Perform trial division up to <i>n</i>, before P-1, P+1 or ECM. In loop mode (see option <code>-c</code>), trial division is only performed in the first run.</dl>
<h2>GROUP AND INITIAL POINT PARAMETERS</h2>
<p> <code>-x0 </code><i>x</i></p>
<dl>
<dt>
<dd> [ECM, P-1, P+1] Use <i>x</i> (arbitrary-precision integer or rational) as initial point. For example, <code>-x0 1/3</code> is valid. If not given, <i>x</i> is generated from the sigma value for ECM, or at random for P-1 and P+1.</dl>
<p> <code>-sigma </code><i>s</i></p>
<dl>
<dt>
<dd> [ECM] Use <i>s</i> (arbitrary-precision integer) as curve generator. If omitted, <i>s</i> is generated at random.</dl>
<p> <code>-A </code><i>a</i></p>
<dl>
<dt>
<dd> [ECM] Use <i>a</i> (arbitrary-precision integer) as curve parameter. If omitted, is it generated from the sigma value.</dl>
<p> <code>-go </code><i>val</i></p>
<dl>
<dt>
<dd> [ECM, P-1, P+1] Multiply the initial point by <i>val</i>, which can any valid expression, possibly containing the special character N as place holder for the current input number. Example: </p>
<dl>
<dt>
<dd>
<pre>
ecm -pp1 -go &quot;N^2-1&quot; 1e6 &lt; composite2000
</pre>
</dl>
</dl>
<h2>STEP 2 PARAMETERS</h2>
<p> <code>-k </code><i>k</i></p>
<dl>
<dt>
<dd> [ECM, P-1, P+1] Perform <i>k</i> blocks in step 2. For a given <i>B2</i> value, increasing <i>k</i> decreases the memory usage of step 2, at the expense of more cpu time.</dl>
<p> <code>-treefile </code><i>file</i></p>
<dl>
<dt>
<dd> Stores some tables of data in disk files to reduce the amount of memory occupied in step 2, at the expense of disk I/O. Data will be written to files <i>file</i>.1, <i>file</i>.2 etc. Does not work with fast stage 2 for P+1 and P-1.</dl>
<p> <code>-power </code><i>n</i></p>
<dl>
<dt>
<dd> [ECM, P-1] Use x^<i>n</i> for Brent-Suyama&#8217;s extension (<code>-power 1</code> disables Brent-Suyama&#8217;s extension). The default polynomial is chosen depending on the method and B2. For P-1 and P+1, disables the fast stage 2. For P-1, <i>n</i> must be even.</dl>
<p> <code>-dickson </code><i>n</i></p>
<dl>
<dt>
<dd> [ECM, P-1] Use degree-<i>n</i> Dickson&#8217;s polynomial for Brent-Suyama&#8217;s extension. For P-1 and P+1, disables the fast stage 2. Like for <code>-power</code>, <i>n</i> must be even for P-1.</dl>
<p> <code>-maxmem </code><i>n</i></p>
<dl>
<dt>
<dd> Use at most <i>n</i> megabytes of memory in stage 2.</dl>
<p> <code>-ntt</code>, <code>-no-ntt</code></p>
<dl>
<dt>
<dd> Enable or disable the Number-Theoretic Transform code for polynomial arithmetic in stage 2. With NTT, dF is chosen to be a power of 2, and is limited by the number suitable primes that fit in a machine word (which is a limitation only on 32 bit systems). The -no-ntt variant uses more memory, but is faster than NTT with large input numbers. By default, NTT is used for P-1, P+1 and for ECM on numbers of size at most 30 machine words.</dl>
<h2>OUTPUT</h2>
<p> <code>-q</code></p>
<dl>
<dt>
<dd> Quiet mode. Found factorizations are printed on standard output, with factors separated by white spaces, one line per input number (if no factor was found, the input number is simply copied).</dl>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> Verbose mode. More information is printed, more <code>-v</code> options increase verbosity. With one <code>-v</code>, the kind of modular multiplication used, initial x0 value, step 2 parameters and progress, and expected curves and time to find factors of different sizes for ECM are printed. With <code>-v -v</code>, the A value for ECM and residues at the end of step 1 and step 2 are printed. More <code>-v</code> print internal data for debugging.</dl>
<p> <code>-timestamp</code></p>
<dl>
<dt>
<dd> Print a time stamp whenever a new ECM curve or P+1 or P-1 run is processed.</dl>
<h2>MODULAR ARITHMETIC OPTIONS</h2>
<p> Several algorithms are available for modular multiplication. The program tries to find the best one for each input; one can force a given method with the following options. </p>
<p> <code>-mpzmod</code></p>
<dl>
<dt>
<dd> Use GMP&#8217;s mpz_mod function (sub-quadratic for large inputs, but induces some overhead for small ones).</dl>
<p> <code>-modmuln</code></p>
<dl>
<dt>
<dd> Use Montgomery&#8217;s multiplication (quadratic version). Usually best method for small input.</dl>
<p> <code>-redc</code></p>
<dl>
<dt>
<dd> Use Montgomery&#8217;s multiplication (sub-quadratic version). Theoretically optimal for large input.</dl>
<p> <code>-nobase2</code></p>
<dl>
<dt>
<dd> Disable special base-2 code (which is used when the input number is a large factor of 2^n+1 or 2^n-1, see <code>-v</code>).</dl>
<p> <code>-base2</code> <i>n</i></p>
<dl>
<dt>
<dd> Force use of special base-2 code, input number must divide 2^<i>n</i>+1 if <i>n</i> &gt; 0, or 2^|<i>n</i>|-1 if <i>n</i> &lt; 0.</dl>
<h2>FILE I/O</h2>
<p> The following options enable one to perform step 1 and step 2 separately, either on different machines, at different times, or using different software (in particular, George Woltman&#8217;s Prime95/mprime program can produce step 1 output suitable for resuming with GMP-ECM). It can also be useful to split step 2 into several runs, using the <i>B2min-B2max</i> option. </p>
<p> <code>-inp </code><i>file</i></p>
<dl>
<dt>
<dd> Take input from file <i>file</i> instead of from standard input.</dl>
<p> <code>-save </code><i>file</i></p>
<dl>
<dt>
<dd> Save result of step 1 in <i>file</i>. If <i>file</i> exists, an error is raised. Example: to perform only step 1 with <i>B1</i>=1000000 on the composite number in the file &quot;c155&quot; and save its result in file &quot;foo&quot;, use </p>
<dl>
<dt>
<dd>
<pre>
ecm -save foo 1e6 1 &lt; c155
</pre>
</dl>
</dl>
<p> <code>-savea </code><i>file</i></p>
<dl>
<dt>
<dd> Like <code>-save</code>, but appends to existing files.</dl>
<p> <code>-resume </code><i>file</i></p>
<dl>
<dt>
<dd> Resume residues from <i>file</i>, reads from standard input if <i>file</i> is &quot;-&quot;. Example: to perform step 2 following the above step 1 computation, use </p>
<dl>
<dt>
<dd>
<pre>
ecm -resume foo 1e6
</pre>
</dl>
</dl>
<p> <code>-chkpoint </code><i>file</i></p>
<dl>
<dt>
<dd> Periodically write the current residue in stage 1 to <i>file</i>. In case of a power failure, etc., the computation can be continued with the <code>-resume</code> option. </p>
<dl>
<dt>
<dd>
<pre>
ecm -chkpnt foo -pm1 1e10 &lt; largenumber.txt 
</pre>
</dl>
</dl>
<h2>LOOP MODE</h2>
<p> The lqloop moderq (option <code>-c </code><i>n</i>) enables one to run several curves on each input number. The following options control its behavior. </p>
<p> <code>-c </code><i>n</i></p>
<dl>
<dt>
<dd> Perform <i>n</i> runs on each input number (default is one). This option is mainly useful for P+1 (for example with <i>n</i>=3) or for ECM, where <i>n</i> could be set to the expected number of curves to find a d-digit factor with a given step 1 bound. This option is incompatible with <code>-resume, -sigma, -x0</code>. Giving <code>-c 0</code> produces an infinite loop until a factor is found.</dl>
<p> <code>-one</code></p>
<dl>
<dt>
<dd> In loop mode, stop when a factor is found; the default is to continue until the cofactor is prime or the specified number of runs are done.</dl>
<p> <code>-b</code></p>
<dl>
<dt>
<dd> Breadth-first processing: in loop mode, run one curve for each input number, then a second curve for each one, and so on. This is the default mode with <code>-inp</code>.</dl>
<p> <code>-d</code></p>
<dl>
<dt>
<dd> Depth-first processing: in loop mode, run <i>n</i> curves for the first number, then <i>n</i> curves for the second one and so on. This is the default mode with standard input.</dl>
<p> <code>-ve </code><i>n</i></p>
<dl>
<dt>
<dd> In loop mode, in the second and following runs, output only expressions that have at most <i>n</i> characters. Default is <code>-ve 0</code>.</dl>
<p> <code>-i </code><i>n</i></p>
<dl>
<dt>
<dd> In loop mode, increment <i>B1</i> by <i>n</i> after each curve.</dl>
<p> <code>-I </code><i>n</i></p>
<dl>
<dt>
<dd> In loop mode, multiply <i>B1</i> by a factor depending on <i>n</i> after each curve. Default is one which should be optimal on one machine, while <code>-I 10</code> could be used when trying to factor the same number simultaneously on 10 identical machines.</dl>
<h2>SHELL COMMAND EXECUTION</h2>
<p> These optins allow for executing shell commands to supplement functionality to GMP-ECM. </p>
<p> <code>-prpcmd </code><i>cmd</i></p>
<dl>
<dt>
<dd> Execute command <i>cmd</i> to test primality if factors and cofactors instead of GMP-ECM&#8217;s own functions. The number to test is passed via stdin. An exit code of 0 is interpreted as lqprobably primerq, a non-zero exit code as lqcompositerq.</dl>
<p> <code>-faccmd </code><i>cmd</i></p>
<dl>
<dt>
<dd> Executes command <i>cmd</i> whenever a factor is found by P-1, P+1 or ECM. The input number, factor and cofactor are passed via stdin, each on a line. This could be used i.e. to mail new factors automatically: </p>
<dl>
<dt>
<dd>
<pre>
ecm -faccmd 'mail -s lq$HOSTNAME found a factorrq
                me [at] myaddress.com' 11e6 &lt; cunningham.in
</pre>
</dl>
</dl>
<p> <code>-idlecmd </code><i>cmd</i></p>
<dl>
<dt>
<dd> Executes command <i>cmd</i> before each ECM curve, P-1 or P+1 attempt on a number is started. If the exit status of <i>cmd</i> is non-zero, GMP-ECM terminates immediately, otherwise it continues normally. GMP-ECM is stopped while <i>cmd</i> runs, offering a way for letting GMP-ECM sleep for example while the system is otherwise busy.</dl>
<h2>MISCELLANEOUS</h2>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> Run the program in lqnicerq mode (below normal priority).</dl>
<p> <code>-nn</code></p>
<dl>
<dt>
<dd> Run the program in lqvery nicerq mode (idle priority).</dl>
<p> <code>-B2scale </code><i>f</i></p>
<dl>
<dt>
<dd> Multiply the default step 2 bound <i>B2</i> by the floating-point value <i>f</i>. Example: <code>-B2scale 0.5</code> divides the default <i>B2</i> by 2.</dl>
<p> <code>-stage1time </code><i>n</i></p>
<dl>
<dt>
<dd> Add <i>n</i> seconds to stage 1 time. This is useful to get correct expected time with <i>-v</i> if part of stage 1 was done in another run.</dl>
<p> <code>-cofdec</code></p>
<dl>
<dt>
<dd> Force cofactor output in decimal (even if expressions are used).</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display a short description of ecm usage, parameters and command line options.</dl>
<h2>INPUT SYNTAX</h2>
<p> The input numbers can have several forms: </p>
<p> Raw decimal numbers like 123456789. </p>
<p> Comments can be placed in the file: everything after lq//rq is ignored, up to the end of line. </p>
<p> Line continuation. If a line ends with a backslash character lqq, it is considered to continue on the next line. </p>
<p> Common arithmetic expressions can be used. Example: <i>3*5+2^10</i>. </p>
<p> Factorial: example <i>53!</i>. </p>
<p> Multi-factorial: example <i>15!3</i> means 15*12*9*6*3. </p>
<p> Primorial: example <i>11#</i> means 2*3*5*7*11. </p>
<p> Reduced primorial: example <i>17#5</i> means 5*7*11*13*17. </p>
<p> Functions: currently, the only available function is <i>Phi(x,n)</i>.</p>
<h2>EXIT STATUS</h2>
<p> The exit status reflects the result of the last ECM curve or P-1/P+1 attempt the program performed. Individual bits signify particular events, specifically: </p>
<p> Bit 0</p>
<dl>
<dt>
<dd> 0 if normal program termination, 1 if error occured</dl>
<p> Bit 1</p>
<dl>
<dt>
<dd> 0 if no proper factor was found, 1 otherwise</dl>
<p> Bit 2</p>
<dl>
<dt>
<dd> 0 if factor is composite, 1 if factor is a probable prime</dl>
<p> Bit 3</p>
<dl>
<dt>
<dd> 0 if cofactor is composite, 1 if cofactor is a probable prime</dl>
<p> Thus, the following exit status values may occur: </p>
<p> 0</p>
<dl>
<dt>
<dd> Normal program termination, no factor found</dl>
<p> 1</p>
<dl>
<dt>
<dd> Error</dl>
<p> 2</p>
<dl>
<dt>
<dd> Composite factor found, cofactor is composite</dl>
<p> 6</p>
<dl>
<dt>
<dd> Probable prime factor found, cofactor is composite</dl>
<p> 8</p>
<dl>
<dt>
<dd> Input number found</dl>
<p> 10</p>
<dl>
<dt>
<dd> Composite factor found, cofactor is a probable prime</dl>
<p> 14</p>
<dl>
<dt>
<dd> Probable prime factor found, cofactor is a probable prime</dl>
<h2>BUGS</h2>
<p> Report bugs to &lt;ecm-discuss [at] lists.gforge.inria.fr&gt;, after checking &lt;<a rel="nofollow" href="http://www.loria.fr/~zimmerma/records/ecmnet.html">http://www.loria.fr/~zimmerma/records/ecmnet.html</a>&gt; for bug fixes or new versions.</p>
<h2>AUTHORS</h2>
<p> Pierrick Gaudry &lt;gaudry at lix dot polytechnique dot fr&gt; contributed efficient assembly code for combined mul/redc; </p>
<p> Jim Fougeron &lt;jfoug at cox dot net&gt; contributed the expression parser and several command-line options; </p>
<p> Laurent Fousse &lt;laurent at komite dot net&gt; contributed the middle product code, the autoconf/automake tools, and is the maintainer of the Debian package; </p>
<p> Alexander Kruppa &lt;(lastname)al [at] loria.fr&gt; contributed estimates for probability of success for ECM, the new P+1 and P-1 stage 2 (with P.-L. Montgomery), new AMD64 asm mulredc code, and some other things; </p>
<p> Dave Newman &lt;david.(lastname)@jesus.ox.ac.uk&gt; contributed the Kronecker-Schoenhage and NTT multiplication code; </p>
<p> Jason S. Papadopoulos contributed a speedup of the NTT code </p>
<p> Paul Zimmermann &lt;zimmerma at loria dot fr&gt; is the author of the first version of the program and chief maintainer of GMP-ECM. </p>
<p> Note: email addresses have been obscured, the required substitutions should be obvious. </p>
<h2>Index</h2>
