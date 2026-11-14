---
title: "libpm(3)"
name: "libpm"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libpm/"
description: "Table Of Contents"
---

<p>Table Of Contents </p>
<p> These library functions are part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> This page documents functions in the Netpbm subroutine library that are not directly related to image data. </p>
<p> For introductory and general information using <code>libnetpbm</code>, see <code>Libnetpbm</code>User&#8217;s<code><a href="/docs/linux/man/1-guide/">Guide</a></code>(1) </p>
<p> The most commonly used <code>libnetpbm</code> functions are those that read and write and process Netpbm images. Those are documented in <code>Libnetpbm</code>Netpbm<code>Image</code>Processing Manual (1) </p>
<p> To use these services, #include <code>pam.h</code>. </p>
<h2>Functions</h2>
<h3>Initialization</h3>
<p> <code>Overview</code> </p>
<p> <code>void pm_init(</code> <code>const char * </code><i>progname</i><code>,</code> <code>unsigned int </code><i>flags</i> <code>);</code> </p>
<p> <code>void pm_proginit(</code> <code>int * </code><i>argcP</i><code>,</code> <code>char * </code><i>argv</i><code>[]</code> <code>);</code> </p>
<p> <code>Description</code> </p>
<p> All Netpbm programs must call <code>pm_proginit()</code> just after startup, before they process their arguments. <code>pm_proginit()</code>, among other things, processes Netpbm universal arguments and removes them from the argument list. </p>
<p> A program that isn&#8217;t a Netpbm program, but just uses <code>libnetpbm</code> services, need not invoke <code>pm_proginit</code>. But such a program must invoke <code>pm_init()</code>. </p>
<p> By &#8216;Netpbm program,&#8217; we mean a program that is part of the Netpbm package or is intended to act like one. <code>pm_proginit()</code> does things that all Netpbm programs do by convention. For example, it scans the argument list for<br />
&nbsp;<wbr>common options , handles them, and removes them from the argument list. Ergo, if you want your program to have the same common options as those in the Netpbm package, you might use <code>pm_proginit()</code>, and if you don&#8217;t, you must not. </p>
<p> <code>pm_proginit()</code> is primarily intended for Netpbm developers, so you should not expect it to have stable function across releases, and you must go to the comments in the source code to see exactly what it does. </p>
<p> Any program that uses <code>libnetpbm</code> but does not call <code>pm_proginit</code> (i.e. is not a Netpbm program) must call <code>pm_init()</code>. The conventional place to do this is at the very beginning of the program. This sets up some program-global variables for use by the <code>libnetpbm</code> functions. </p>
<p> The <i>progname</i> argument is the program name for <code>libnetpbm</code> functions to use in messages they issue. Normally, you would use argv[0] for this. </p>
<p> <i>flags</i> is meaningless, but for forward compatibility, you must set it to zero. </p>
<p> <code>pm_init()</code> and <code>pm_proginit()</code> have been around at least since Netpbm 9.25 (March 2002). Another function named <code>pm_init()</code> exists in older Netpbm, but was for internal use. Netpbm programs of that era use <code>pbm_init()</code>, etc to do what <code>pm_proginit()</code> does today. Today, <code>pbm_init()</code>, etc. exist for backward compatibility and are identical the <code>pm_proginit()</code>. </p>
<h3>File Or Image Stream Access</h3>
<p> <code>Overview</code> </p>
<p> <code>FILE *pm_openr(</code> <code>char *</code> <i>name</i> <code>);</code> </p>
<p> <code>FILE *pm_openw(</code> <code>char *</code> <i>name</i> <code>);</code> </p>
<p> <code>FILE *pm_openr_seekable(</code> <code>const char *</code> <i>name</i> <code>);</code> </p>
<p> <code>FILE *pm_close(</code> <code>FILE *</code> <i>fp</i> <code>);</code> </p>
<p> <code>void pm_tell2(</code> <code>FILE * </code> <i>fileP</i><code>,</code> <code>pm_filepos *</code> <i>fileposP</i><code>,</code> <code>unsigned int</code> <i>fileposSize</i> <code>);</code> </p>
<p> <code>unsigned int pm_tell(</code> <code>FILE *</code> <i>fileP</i> <code>);</code> </p>
<p> <code>void pm_seek2(</code> <code>FILE * </code> <i>fileP</i><code>,</code> <code>const pm_filepos *</code> <i>fileposP</i><code>,</code> <code>unsigned int</code> <i>fileposSize</i> <code>);</code> </p>
<p> <code>void pm_seek(</code> <code>FILE * </code> <i>fileP</i><code>,</code> <code>unsigned long</code> <i>filepos</i> <code>);</code> </p>
<p> <code>char *pm_read_unknown_size(</code> <code>FILE *</code> <i>fp</i><code>,</code> <code>long *</code> <i>nread</i> <code>);</code> </p>
<p> <code>Description</code> </p>
<p> An image stream is just a file stream (represented in the standard C library as type <code>FILE *</code>). </p>
<p> These routines work on files &gt; 2 GiB if the underlying system does, using the standard large file interface. Before Netpbm 10.15 (April 2003), though, they would fail to open any file that large or process any offset in a file that could not be represented in 32 bits. </p>
<p> <code>pm_openr()</code> opens the given file for reading, with appropriate error checking. A filename of <code>&#8211;</code> is taken to mean Standard Input. <code>pm_openw()</code> opens the given file for writing, with appropriate error checking. <code>pm_close()</code> closes the file descriptor, with appropriate error checking. </p>
<p> <code>pm_openr_seekable()</code> appears to open the file just like <code>pm_openr()</code>, but the file thus opened is guaranteed to be seekable (you can use ftell() and fseek() on it). <code>pm_openr_seekable()</code> pulls this off by copying the entire file to a temporary file and giving you the handle of the temporary file, if it has to. If the file you name is a regular file, it&#8217;s already seekable so <code>pm_openr_seekable()</code> just does the same thing as <code>pm_openr()</code>. </p>
<p> But if it is, say, a pipe, it isn&#8217;t seekable. So <code>pm_openr_seekable()</code> reads the pipe until EOF into a temporary file, then opens that temporary file and returns the handle of the temporary file. The temporary file is seekable. </p>
<p>&nbsp;<wbr>The file <code>pm_openr_seekable()</code> creates is one that the operating system recognizes as temporary, so when you close the file, by any means, it gets deleted. </p>
<p> You need a seekable file if you intend to make multiple passes through the file. The only alternative is to read the entire image into memory and work from that copy. That may use too much memory. Note that the image takes less space in the file cache than in a buffer in memory. As much as 96 times less space! Each sample is an integer in the buffer, which is usually 96 bits. In the file, a sample may be as small as 1 bit and rarely more than 8 bits. </p>
<p> <code>pm_tell2()</code> returns a handle for the current position of the image stream (file), whether it be the header or a row of the raster. Use the handle as an argument to <code>pm_seek2()</code> to reposition the file there later. The file must be seekable (which you can ensure by opening it with <code>pm_openr_seekable()</code>) or this may fail. </p>
<p> The file position handle is of type <code>pm_filepos</code>, which is intended to be opaque, i.e. used only with these two functions. In practice, it is a file offset and is 32 bits or 64 bits depending upon the capability of the underlying system. For maximum backward and forward compatibility, the functions that take or return a <code>pm_filepos</code> have a <i>fileposSize</i> argument for the size of the data structure. In C, simply code <code>sizeof(pm_filepos)</code> for that. </p>
<p> <code>pm_seek()</code> and <code>pm_tell</code> are for backward compatibility only. Do not use them in new code. These functions are not capable of handle positions in files whose byte offset cannot be represented in 32 bits. </p>
<p> <code>pm_tell2()</code> and <code>pm_seek2()</code> replaced <code>pm_tell()</code> and <code>pm_seek()</code> in Netpbm 10.15 (April 2003). </p>
<p> <code>pm_read_unknown_size()</code> reads an entire file or input stream of unknown size to a buffer. It allocates more memory as needed. The calling routine has to free the allocated buffer with <code>free()</code>. </p>
<p> <code>pm_read_unknown_size()</code> returns a pointer to the allocated buffer. The <code>nread</code> argument returns the number of bytes read. </p>
<h3>Endian I/O</h3>
<p> <code>Entry Points</code> </p>
<p> <code>void pm_readchar(</code> <code>FILE *</code> <i>in</i><code>,</code> <code>char *</code> <i>sP</i> <code>);</code> </p>
<p> <code>void pm_writechar(</code> <code>FILE *</code> <i>out</i><code>,</code> <code>char</code> <i>s</i> <code>);</code> </p>
<p> <code>int pm_readbigshort(</code> <code>FILE *</code> <i>in</i><code>,</code> <code>short *</code> <i>sP</i> <code>);</code> </p>
<p> <code>int pm_writebigshort(</code> <code>FILE *</code> <i>out</i><code>,</code> <code>short</code> <i>s</i> <code>);</code> </p>
<p> <code>int pm_readbiglong(</code> <code>FILE *</code> <i>in</i><code>,</code> <code>long *</code> <i>lP</i> <code>);</code> </p>
<p> <code>int pm_writebiglong(</code> <code>FILE *</code> <i>out</i><code>,</code> <code>long</code> <i>l</i> <code>);</code> </p>
<p> <code>int pm_readlittleshort(</code> <code>FILE *</code> <i>in</i><code>,</code> <code>short *</code> <i>sP</i> <code>);</code> </p>
<p> <code>int pm_writelittleshort(</code> <code>FILE *</code> <i>out</i><code>,</code> <code>short</code> <i>s</i> <code>);</code> </p>
<p> <code>int pm_readlittlelong(</code> <code>FILE *</code> <i>in</i><code>,</code> <code>long *</code> <i>lP</i> <code>);</code> </p>
<p> <code>int pm_writelittlelong(</code> <code>FILE *</code> <i>out</i><code>,</code> <code>long</code> <i>l</i> <code>);</code> </p>
<p> <code>void pm_readcharu(</code> <code>FILE *</code> <i>in</i><code>,</code> <code>char *</code> <i>sP</i> <code>);</code> </p>
<p> <code>void pm_writecharu(</code> <code>FILE *</code> <i>out</i><code>,</code> <code>char</code> <i>s</i> <code>);</code> </p>
<p> <code>int pm_readbigshortu(</code> <code>FILE *</code> <i>in</i><code>,</code> <code>short *</code> <i>sP</i> <code>);</code> </p>
<p> <code>int pm_writebigshortu(</code> <code>FILE *</code> <i>out</i><code>,</code> <code>short</code> <i>s</i> <code>);</code> </p>
<p> <code>int pm_readbiglongu(</code> <code>FILE *</code> <i>in</i><code>,</code> <code>long *</code> <i>lP</i> <code>);</code> </p>
<p> <code>int pm_writebiglongu(</code> <code>FILE *</code> <i>out</i><code>,</code> <code>long</code> <i>l</i> <code>);</code> </p>
<p> <code>int pm_readlittleshortu(</code> <code>FILE *</code> <i>in</i><code>,</code> <code>short *</code> <i>sP</i> <code>);</code> </p>
<p> <code>int pm_writelittleshortu(</code> <code>FILE *</code> <i>out</i><code>,</code> <code>short</code> <i>s</i> <code>);</code> </p>
<p> <code>int pm_readlittlelongu(</code> <code>FILE *</code> <i>in</i><code>,</code> <code>long *</code> <i>lP</i> <code>);</code> </p>
<p> <code>int pm_writelittlelongu(</code> <code>FILE *</code> <i>out</i><code>,</code> <code>long</code> <i>l</i> <code>);</code> </p>
<p> <code>Description</code> </p>
<p> <code>pm_readchar()</code>, <code>pm_writechar()</code>, <code>pm_readbigshort()</code>, <code>pm_writebigshort()</code>, <code>pm_readbiglong()</code>, <code>pm_writebiglong()</code>, <code>pm_readlittleshort()</code>, <code>pm_writelittleshort()</code>, <code>pm_readlittlelong()</code>, and <code>pm_writelittlelong()</code> are routines to read and write 1-byte, 2-byte, and 4-byte pure binary integers in either big- or little-endian byte order. Note that a &#8216;long int&#8217; C type might be wider than 4 bytes, but the &#8216;long&#8217; routines still read and write 4 bytes. </p>
<p> <code>pm_readbiglongu()</code>, etc. (names ending in <code>u</code>) are the same except they work on unsigned versions of the type. </p>
<p> The routines with declared return values always return 0. Before Netpbm 10.27 (March 2005), they returned -1 on failure, including EOF. Now, they issue an error message to Standard Error and abort the program if the I/O fails or encounters EOF. </p>
<p> The 1-byte routines were new in Netpbm 10.27 (March 2005). The unsigned versions were new somewhere around Netpbm 10.21 (2004). </p>
<h3>Maxval Arithmetic</h3>
<p> <code>Entry Points</code> </p>
<p> <code>int pm_maxvaltobits(</code> <code>int</code> <i>maxval</i> <code>);</code> </p>
<p> <code>int pm_bitstomaxval(</code> <code>int</code> <i>bits</i> <code>);</code> </p>
<p> <code>unsigned int pm_lcm(</code> <code>unsigned int</code> <i>x</i><code>,</code> <code>unsigned int</code> <i>y</i><code>,</code> <code>unsigned int</code> <i>z</i><code>,</code> <code>unsigned int</code> <i>limit</i> <code>);</code> </p>
<p> <code>Description</code> </p>
<p> <code>pm_maxvaltobits()</code> and <code>pm_bitstomaxval()</code> convert between a maxval and the minimum number of bits required to hold it. </p>
<p> <code>pm_lcm()</code> computes the least common multiple of 3 integers. You also specify a limit and if the LCM would be higher than that limit, <code>pm_lcm()</code> just returns that limit. </p>
<h3>Gamma Arithmetic</h3>
<p> <code>Entry Points</code> </p>
<p> <code>float pm_gamma709(</code> <code>float</code> <i>intensity</i> <code>);</code> </p>
<p> <code>float pm_ungamma709(</code> <code>float</code> <i>brightness</i> <code>);</code> </p>
<p> <code>Description</code> </p>
<p> In graphics processing, there are two common ways of representing numerically the intensity of a pixel, or a component of a pixel. </p>
<p> The obvious way is with a number that is directly proportional to the light intensity (e.g. 10 means twice as many milliwatts per square centimeter as 5). There are two problems with this: </p>
<dl>
<dt>&bull;</p>
<dd> To the human eye, a 1 milliwatt per square centimeter difference<br />
&nbsp;<wbr>in a bright image is much less apparent than a 1 milliwatt per<br />
&nbsp;<wbr>square centimeter difference in a dark image.&nbsp;<wbr>&nbsp;<wbr>So if you have<br />
&nbsp;<wbr>a fixed number of bits in which to store the intensity value,<br />
&nbsp;<wbr>you&#8217;re wasting resolution at the bright end and skimping on it at<br />
&nbsp;<wbr>the dark end.</p>
<dt>&bull;</p>
<dd> Monitor inputs and camera outputs aren&#8217;t directly proportional to<br />
&nbsp;<wbr>the light intensity they project or detect. </p>
</dl>
<p> For these reasons, light intensities are often represented in graphics processing by an exponential scale. The transfer function is called a gamma function and the resulting numbers are called gamma-corrected or gamma-adjusted. There are various gamma functions. The Netpbm formats specify that intensities are represented by gamma-adjusted numbers of a particular gamma transfer function. </p>
<p> These functions let you convert back and forth between these two scales, using the same gamma transfer function that is specified in the Netpbm format specifications. </p>
<p> <code>pm_gamma709</code> converts from an intensity-proportional intensity value to a gamma-adjusted intensity value (roughly proportional to brightness, which is the human subjective perception of intensity), using the ITU-R Recommendation BT.709 gamma transfer function. </p>
<p> <code>pm_ungamma709</code> is the inverse of <code>pm_gamma709</code>. </p>
<h3>Messages</h3>
<p> <code>Overview</code> </p>
<p> <code>void pm_message(</code> <code>char *</code> <i>fmt</i><code>,</code> <code>&#8230; );</code> </p>
<p> <code>void pm_setusermessagefn(pm_usermessagefn *</code> <i>function</i><code>);</code> </p>
<p> <code>Description</code> </p>
<p> <code>pm_message()</code> is a <code>printf()</code> style routine to write an informational message to the Standard Error file stream. <code>pm_message()</code> suppresses the message, however, if the user specified the <code>-quiet</code> common option on the command line. Note that Netpbm programs are often used interactively, but also often used by programs. In the interactive case, it is nice to issue messages about what the program is doing, but in the program case, such messages are usually undesirable. By using <code>pm_message()</code> for all your messages, you make your program usable in both cases. Without any effort on your part, program users of your program can avoid the messages by specifying the <code>-quiet</code> option. </p>
<p> Netpbm distinguishes between error messages and information messages; <code>pm_message()</code> is just for informational messages. To issue an error message, see <code>pm_errormsg()</code> . </p>
<p> <code>pm_setusermessagefn</code> registers a handler for informational messages, called a user message routine. Any library function (including <code>pm_message()</code>) that wants to issue an informational message in the future will call that function with the message as an argument instead of writing the message to Standard Error. </p>
<p> The argument the user message routine gets is English text designed for human reading. It is just the text of the message; there is no attempt at formatting in it (so you won&#8217;t see any newline or tab characters). </p>
<p> To capture error messages in addition to informational messages, see <code>pm_setusererrormsgfn()</code> . </p>
<p> You can remove the user message routine, so that the library issues future informational messages in its default way (write to Standard Error) by specifying a null pointer for <i>function</i>. </p>
<p> Example: </p>
<pre><code>

static pm_usermessagefn logfilewrite;
static void
logfilewrite(const char *const msg)
{
    fprintf(mymsglog, 'Netpbm message: %s', msg);
}
pm_setusermessagefn(&amp;logfilewrite);

pm_message('Message for the message log');
</code></pre>
<h3>System Utilities</h3>
<dl>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-pm_system/">pm_system</a></code>(1) </p>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-pm_tmpfile/">pm_tmpfile</a></code>(1) </p>
</dl>
<h3>Keyword Matching</h3>
<p> <code>Entry Points</code> </p>
<p> <code>void pm_keymatch();</code> </p>
<p> <code>Description</code> </p>
<p> This subroutine is obsolete. It used to be used for command line option processing. Today, you can do better option processing more easily with the shhopt facility. See any recent program in the Netpbm package for an example. </p>
<p> <code>pm_keymatch()</code> does a case-insensitive match of <code>str</code> against <code>keyword</code>. <code>str</code> can be a leading substring of <code>keyword</code>, but at least <code>minchars</code> must be present. </p>
<h2>Index</h2>
