---
title: "ppmtompeg(1)"
name: "ppmtompeg"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtompeg/"
description: "ppmtompeg – encodes MPEG-1 bitstreams"
---

<h2 class="name">NAME</h2>
<p> ppmtompeg &#8211; encodes MPEG-1 bitstreams </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtompeg</code> [ <i>options</i> ] <i>parameter-file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ppmtompeg</code> produces an MPEG-1 video stream. param_file is a parameter file which includes a list of input files and other parameters. The file is described in detail below. The -gop, -combine_gops, -frames, and -combine_frames options are all exclusive. This man page is probably incomplete. For complete usage, see the User&#8217;s Guide.</p>
<h2>OPTIONS</h2>
<dl>
<dt> <code>-stat stat_file</code> : causes the encoder to append the statistics to the file <i>stat_file</i>.</p>
<dd>In any case, the statistics are output to stdout. The statistics use the following abbreviations: bits per block (bpb), bits per frame (bpf), seconds per frame (spf), and bits per second (bps).</p>
<dt> <code>-quiet num_seconds</code> : causes the program to not report remaining time for at least num_seconds</p>
<dd>seconds. A negative values tells the program not to report at all. 0 is the default (reports once after each frame). Note that the time remaining is an estimate and does not take into account time to read in frames.</p>
<dt> <code>-realquiet</code> : causes the encoder to run silently, with the only screen output being errors.</p>
<dd>Particularly useful when reading input from stdin.</p>
<dt> <code>-no_frame_summary</code> : prevents the program from printing a summary line for each frame</p>
<dt> <code>-float_dct</code> : forces the encoder to use a more accurate, yet more computationally expensive</p>
<dd>version of the DCT.</p>
<dt> <code>-gop gop_num</code> : causes the encoder to only encode the numbered GOP (first GOP is 0). The</p>
<dd>parameter file is the same as for normal usage. The output file will be the normal output file with the suffix &quot;.gop.&lt;gop_num&gt;&quot; No sequence info is output.</p>
<dt> <code>-combine_gops</code> : causes the encoder to simply combine some GOP files into a single MPEG</p>
<dd>stream. A sequence header/ender are inserted. In this case, the parameter file need only contain the YUV_SIZE value, an output file, and perhaps a list of input GOP files (see below).</p>
<dt> <code>-frames first_frame last_frame</code> : causes the encoder to only encode the frames from first_frame to</p>
<dd>last_frame, inclusive. The parameter file is the same as for normal usage. The output will be placed in separate files, one per frame, with the file names being the normal output file with the suffix &quot;.frame.&lt;frame num&gt;&quot; No GOP header information is output. (Thus, the parameter file need not include the GOP_SIZE value)</p>
<dt> <code>-combine_frames</code> : causes the encoder to simply combine some frames into a single MPEG stream.</p>
<dd>Sequence and GOP headers are inserted appropriately. In this case, the parameter file need only contain the YUV_SIZE value, the GOP_SIZE value, an output file, and perhaps a list of frame files (see below).</p>
<dt> <code>-nice</code> : causes the program to run any remote processes &#8216;nicely.&#8217; This is only</p>
<dd>relevant if the program is using parallel encoding. (see &#8216;man nice.&#8217;)</p>
<dt> <code>-max_machines num_machines</code> : causes the program to use no more than num_machines machines as slaves for</p>
<dd>use in parallel encoding.</p>
<dt> <code>-snr</code> : print the signal-to-noise ratio. Prints SNR (Y U V) and peak SNR (Y U V)</p>
<dd>for each frame. In summary, prints averages of luminance only (Y). SNR is defined as 10*log(variance of original/variance of error). Peak SNR is defined as 20*log(255/RMSE). Note that the encoder will run a little slower if you want it to print the SNR.</p>
<dt> <code>-mse</code> : computes the mean squared error per block. Also automatically computes</p>
<dd>the quality of the images when set, so there is no need to specify -snr then.</p>
<dt> <code>-bit_rate_info rate_file</code> : prints bit rate information into the file rate_file. Bit rate info is bits</p>
<dd>per frame, and also bits per I-frame-to-I-frame.</p>
<dt> <code>-mv-histogram</code> : prints histogram of motion vectors as part of statistics. There are three</p>
<dd>histograms &#8212; one for P, forward B, and backward B vectors. Each histogram is a 2-dimensional array, and there is one entry for each vector in the search window.</p>
<dt></dl>
<h2>PARAMETER FILE</h2>
<dd>The parameter file MUST contain the following lines (except when using the -combine_gops or -combine_frames options):</p>
<dl>
<dt>
<dl>
<dt>
<dd>
<dd>PATTERN &lt;pattern&gt;</p>
<dl>
<dt>
<dd>OUTPUT &lt;output file&gt;</p>
<dt>
<dd>INPUT_DIR &lt;directory&gt;</p>
<dl>
<dt>
<dd> all input files must reside in this directory. If you want to refer to the current directory, use &#8216;.&#8217; (an empty INPUT_DIR value would refer to the root directory). If input files will be coming in from standard input, use &#8216;stdin&#8217;.</dl>
<dt>
<dd>INPUT</p>
<dl>
<dt>
<dd> This line must be followed by a list of the input files (in display order) and then the line</p>
<dl>
<dt>
<dd> END_INPUT</dl>
<p> There are three types of lines between INPUT and END_INPUT. First, a line may simply be the name of an input file. Secondly, the line may be of the form</p>
<dl>
<dt>
<dd> &lt;single_star_expr&gt; [x-y]</dl>
<p> single_star_expr can have a single &#8216;*&#8217; in it. It is replaced by all the numbers between x and y inclusive. So, for example, the line</p>
<dl>
<dt>
<dd> tennis*.ppm [12-15]</dl>
<p> is replaced by tennis12.ppm, tennis13.ppm, tennis14.ppm, tennis15.ppm. Uniform zero-padding occurs, as well. For example, the line</p>
<dl>
<dt>
<dd> football.*.ppm [001-130]</dl>
<p> is replaced by football.001.ppm, football.002.ppm, &#8230;, football.009.ppm, football.010.ppm, &#8230;, football.130.ppm. The third type of line is:</p>
<dl>
<dt>
<dd> &lt;single_star_expr&gt; [x-y+s]</dl>
<p> Where the line is treated exactly as above, except that we skip by s. Thus, the line</p>
<dl>
<dt>
<dd> football.*.ppm [001-130+4]</dl>
<p> is replaced by football.001.ppm, football.005.ppm, football.009.ppm, football.013.ppm, etc.</dl>
<dt>
<dd>BASE_FILE_FORMAT &lt;YUV or PPM or PNM or JPEG or JMOVIE&gt;</p>
<dl>
<dt>
<dd> All the input files must be converted to YUV, JPEG(v4), JMOVIE, PNM, or PPM format. This line specifies which of the three formats (actually PPM is a subset of PNM). The reason for having a separate PPM option is for simplicity. If your files are RAWBITS ppm files, then use the PPM option rather than the PNM. Also, depending on the system, file reads will go much faster with the PPM option (as opposed to PNM).</dl>
<dt>
<dd>INPUT_CONVERT &lt;conversion command&gt;</p>
<dl>
<dt>
<dd> You must specify how to convert a file to the base file format. In the conversion command, each &#8216;*&#8217; is replaced by the filename (the items listed between INPUT and END_INPUT). If no conversion is necessary, then you would just say:</p>
<dl>
<dt>
<dd> INPUT_CONVERT *</dl>
<p> If you had a bunch of gif files, you might say:</p>
<dl>
<dt>
<dd> INPUT_CONVERT giftoppm *</dl>
<p> If you have a bunch of separate a.Y, a.U, and a.V files, then you might say:</p>
<dl>
<dt>
<dd> INPUT_CONVERT cat *.Y *.U *.V</dl>
<dl>
<dt>
<dd> Input conversion is not allowed with input from stdin.</dl>
<dl>
<dt>
<dd>GOP_SIZE &lt;n&gt;</p>
<dl>
<dt>
<dd> n is roughly the number of frames in a Group of Pictures (roughly because a GOP must begin with an I-frame)</dl>
<dt>
<dd>SLICES_PER_FRAME &lt;n&gt;</p>
<dl>
<dt>
<dd> n is roughly the number of slices per frame. Note, at least one MPEG player may complain if slices do not start at the left side of an image. To ensure this does not happen, make sure the number of rows is divisible by SLICES_PER_FRAME.</dl>
<dt>
<dd>PIXEL &lt;FULL or HALF&gt;</p>
<dl>
<dt>
<dd> use half-pixel motion vectors, or only full-pixel ones</dl>
<dt>
<dd>RANGE &lt;n&gt;</p>
<dl>
<dt>
<dd> use a search range of +/- n pixels</dl>
<dt>
<dd>PSEARCH_ALG &lt;algorithm&gt;</p>
<dl>
<dt>
<dd> algorithm must be one of {EXHAUSTIVE, TWOLEVEL, SUBSAMPLE, LOGARITHMIC}. Tells what kind of search procedure should be used for P-frames. Exhaustive gives the best compression, but logarithmic is the fastest. You select the desired combination of speed and compression. TWOLEVEL is an exhaustive full-pixel search, followed by a local half- pixel search around the best full-pixel vector (the PIXEL option is ignored for this search algorithm).</dl>
<dt>
<dd>BSEARCH_ALG &lt;algorithm&gt;</p>
<dl>
<dt>
<dd> algorithm must be one of {SIMPLE, CROSS2, EXHAUSTIVE}. Tells what kind of search procedure should be used for B-frames. Simple means find best forward and backward vectors, then interpolate. Cross2 means find those two vectors, then see what backward vector best matches the best forward vector, and vice versa. Exhaustive does an n-squared search and is EXTREMELY slow in relation to the others (Cross2 is about twice as slow as Simple).</dl>
<dt>
<dd>IQSCALE &lt;n&gt;</p>
<dl>
<dt>
<dd> use n as the qscale for I-frames</dl>
<dt>
<dd>PQSCALE &lt;n&gt;</p>
<dl>
<dt>
<dd> use n as the qscale for P-frames</dl>
<dt>
<dd>BQSCALE &lt;n&gt;</p>
<dl>
<dt>
<dd> use n as the qscale for B-frames</dl>
<dt>
<dd>REFERENCE_FRAME &lt;ORIGINAL or DECODED&gt;</p>
<dl>
<dt>
<dd> If ORIGINAL is specified, then the original images are used when computing motion vectors. To be more accurate, use DECODED, in which the decoded images are used. This should increase the quality of the image, but will take a bit longer to encode.</dl>
<p> The following lines are optional:</p>
<dt>
<dl>
<dt>
<dd>
<dd>FORCE_I_ALIGN</p>
<dl>
<dt>
<dd> This option is only relevant for parallel execution (see below). It forces each processor to encode a block of N frames, where N must be a multiple of the pattern length. Since the first frame in any pattern is an I-frame, this forces each block encoded by a processor to begin with an I-frame.</dl>
<p> foo</dl>
<dt></dl>
</dl>
</dl>
</dl>
</dl>
<h2>NOTES</h2>
<dd>If the BASE_FILE_FORMAT is YUV, then the parameter file must contain:</p>
<dl>
<dt>
<dd> YUV_SIZE &lt;w&gt;x&lt;h&gt;</dl>
<p> where w = width, h = height (in pixels) of image, and</p>
<dl>
<dt>
<dd> YUV_FORMAT &lt;ABEKAS or PHILLIPS or UCB or EYUV or pattern&gt;.</dl>
<p> See the file doc/INPUT.FORMAT for more information. </p>
<p> If the -combine-gops option is used, then only the YUV_SIZE and OUTPUT values need be specified in the parameter file. In addition, the parameter file may specify input GOP files in the same manner as normal input files &#8212; except instead of using INPUT_DIR, INPUT, and END_INPUT, use GOP_INPUT_DIR, GOP_INPUT, and GOP_END_INPUT. If no input GOP files are specified, then the default is to use the output file name with suffix &quot;.gop.&lt;gop_num&gt;&quot; starting from 0 as the input files. </p>
<p> If the -combine-frames option is used, then only the YUV_SIZE, GOP_SIZE, and OUTPUT values need be specified in the parameter file. In addition, the parameter file may specify input frame files in the same manner as normal input files &#8212; except instead of using INPUT_DIR, INPUT, and END_INPUT, use FRAME_INPUT_DIR, FRAME_INPUT, and FRAME_END_INPUT. If no input frame files are specified, then the default is to use the output file name with suffix &quot;.frame.&lt;frame_num&gt;&quot; starting from 0 as the input files. </p>
<p> Any number of spaces and tabs may come between each option and value. Lines beginning with &#8216;#&#8217; are ignored. Any other lines are ignored except for those between INPUT and END_INPUT. This allows you to use the same parameter file for normal usage and for -combine_gops and -combine_frames. </p>
<p> The encoder is case-sensitive so, except for file names and directories, everything should be in upper case. </p>
<p> The lines may appear in any order, except the following exceptions. INPUT must appear before END_INPUT (also, GOP_INPUT before GOP_END_INPUT and FRAME_INPUT before FRAME_END_INPUT). All lines between INPUT and END_INPUT must be the frames in play order. </p>
<p> The encoder is prepared to handle up to 16 B frames between reference frames when encoding with input from stdin. To increase this amount, change the constant B_FRAME_RUN in frame.c and recompile. </p>
<dl>
<dt></dl>
<h2>PARALLEL OPERATION</h2>
<dd>The encoder may be run on multiple machines at once. To do so, add a line &quot;PARALLEL&quot; in the parameter file, followed by a listing, one machine per line, then &quot;END_PARALLEL&quot;. Each of the lines should be in one of two forms. If the machine has access to the file server, then the line should be: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&lt;machine&gt; &lt;user&gt; &lt;executable&gt;</p>
<p> The executable is normally ppmtompeg (you may need to give the complete path if you&#8217;ve built for different architectures). If the machine is a remote machine, then the line should be: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>REMOTE &lt;machine&gt; &lt;user&gt; &lt;executable&gt; &lt;parameter file&gt;</p>
<p> Full paths should generally be used when describing executables and parameter files. This INCLUDES the parameter file given as an argument to the original call to ppmtompeg. Also, .rhosts files on the appropriate machines should have the appropriate information. </p>
<p> The encoder will use the original machine for the master and I/O server processes, and uses the listed machines as slaves to do the computation. </p>
<p> Optional lines are</p>
<dl>
<dt>
<dd>RSH &lt;remote shell command&gt;</p>
<dl>
<dt>
<dd> The encoder uses the remote shell command to start processes on other machines. The default command is &#8216;rsh.&#8217; If your machine supports a different command, specify it here.</dl>
<dt>
<dd>PARALLEL_TEST_FRAMES &lt;n&gt;</p>
<dl>
<dt>
<dd> n is the number of frames to encode initially on each processor</dl>
<dt>
<dd>PARALLEL_TIME_CHUNKS &lt;t&gt;</p>
<dl>
<dt>
<dd> subsequently, each slave processor will be asked to encode for approximately t seconds. Smaller values of &lt;t&gt; increase communication, but improve load balancing.</p>
<dl>
<dt>
<dd>The default values for these two options are n = 3 frames and t = 30 seconds.</dl>
</dl>
<dt>
<dd>PARALLEL_PERFECT</p>
<dl>
<dt>
<dd> If this line is present, then scheduling is done on the assumption that work distribution will be perfectly even &#8212; meaning that each machine is about the same speed. The frames will simply be divided up evenly between the processors. This has the advantage of very minimal scheduling overhead, but is obviously wrong if machines have varying speeds, or if the network load makes performance uneven.</dl>
</dl>
<h2>VERSION</h2>
<p> This is version 1.5 it contins new features and bug fixes from version 1.3.</p>
<h2>BUGS</h2>
<p> Not really a bug, but at least a limitation: If writing to an output file, ppmtompeg sometimes uses &lt;filename&gt;.* as temporary files. </p>
<p> No known bugs, but if you find any, report them to mpeg-bugs [at] plateau.cs.berkeley.edu.</p>
<dl>
<dt></dl>
<h2>AUTHORS</h2>
<dl>
<dt>
<dd>Kevin Gong &#8211; University of California, Berkeley, keving [at] cs.berkeley.edu</p>
<dt>
<dd>Ketan Patel &#8211; University of California, Berkeley, kpatel [at] cs.berkeley.edu</p>
<dt>
<dd>Dan Wallach &#8211; University of California, Berkeley, dwallach [at] cs.berkeley.edu</p>
<dt>
<dd>Darryl Brown &#8211; University of California, Berkeley, darryl [at] cs.berkeley.edu</p>
<dt>
<dd>Eugene Hung &#8211; University of California, Berkeley, eyhung [at] cs.berkeley.edu</p>
<dt>
<dd>Steve Smoot &#8211; University of California, Berkeley, smoot [at] cs.berkeley.edu</p>
<dt>
</dl>
<h2>Index</h2>
