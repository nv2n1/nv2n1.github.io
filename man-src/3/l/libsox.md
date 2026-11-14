---
title: "libsox(3)"
name: "libsox"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libsox/"
description: "libsox – SoX, an audio file-format and effect library"
---

<h2>NAME</h2>
<p> libsox &#8211; SoX, an audio file-format and effect library</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sox.h&gt;
int sox_format_init(void);
void sox_format_quit(void);
sox_format_t sox_open_read(const char *path, const sox_signalinfo_t *info, const char *filetype);
sox_format_t sox_open_write(sox_bool (*overwrite_permitted)(const char *filename), const char *path, const sox_signalinfo_t *info, const char *filetype, const char *comment, sox_size_t length, const sox_instrinfo_t *instr, const sox_loopinfo_t *loops);
sox_size_t sox_read(sox_format_t ft, sox_ssample_t *buf, sox_size_t len);
sox_size_t sox_write(sox_format_t ft, sox_ssample_t *buf, sox_size_t len);
int sox_close(sox_format_t ft);
int sox_seek(sox_format_t ft, sox_size_t offset, int whence);
sox_effect_handler_t const *sox_find_effect(char const *name);
sox_effect_t *sox_create_effect(sox_effect_handler_t const *eh);
int sox_effect_options(sox_effect_t *effp, int argc, char *const argv[]);
sox_effects_chain_t *sox_create_effects_chain(sox_encodinginfo_t const *in_enc, sox_encodinginfo_t const *out_enc);
void sox_delete_effects_chain(sox_effects_chain_t *ecp);
int sox_add_effect(sox_effects_chaint_t *chain, sox_effect_t *effp, sox_signalinfo_t *in, sox_signalinfo_t const *out);
cc file.c - o file - lsox
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>libsox</i> is a library of sound sample file format readers/writers and sound effects processors. It is mainly developed for use by SoX but is useful for any sound application. </p>
<p> <code>sox_format_init</code> function performs some required initialization related to all file format handlers. If compiled with dynamic library support then this will detect and initialize all external libraries. This should be called before any other file operations are performed. </p>
<p> <code>sox_format_quit</code> function performs some required cleanup related to all file format handlers. </p>
<p> <code>sox_open_input</code> function opens the file for reading whose name is the string pointed to by <i>path</i> and associates an sox_format_t with it. If <i>info</i> is non-NULL then it will be used to specify the data format of the input file. This is normally only needed for headerless audio files since the information is not stored in the file. If <i>filetype</i> is non-NULL then it will be used to specify the file type. If this is not specified then the file type is attempted to be derived by looking at the file header and/or the filename extension. A special name of &quot;-&quot; can be used to read data from stdin. </p>
<p> <code>sox_open_output</code> function opens the file for writing whose name is the string pointed to by <i>path</i> and associates an sox_format_t with it. If <i>info</i> is non-NULL then it will be used to specify the data format of the output file. Since most file formats can write data in different data formats, this generally has to be specified. The info structure from the input format handler can be specified to copy data over in the same format. If <i>comment</i> is non-NULL, it will be written in the file header for formats that support comments. If <i>filetype</i> is non-NULL then it will be used to specify the file type. If this is not specified then the file type is attempted to be derived by looking at the filename extension. A special name of &quot;-&quot; can be used to write data to stdout. </p>
<p> The function <code>sox_read</code> reads <i>len</i> samples in to <i>buf</i> using the format handler specified by <i>ft</i>. All data read is converted to 32-bit signed samples before being placed in to <i>buf</i>. The value of <i>len</i> is specified in total samples. If its value is not evenly divisable by the number of channels, undefined behavior will occur. </p>
<p> The function <code>sox_write</code> writes <i>len</i> samples from <i>buf</i> using the format handler specified by <i>ft</i>. Data in <i>buf</i> must be 32-bit signed samples and will be converted during the write process. The value of <i>len</i> is specified in total samples. If its value is not evenly divisable by the number of channels, undefined behavior will occur. </p>
<p> The <code>sox_close</code> function dissociates the named <i>sox_format_t</i> from its underlying file or set of functions. If the format handler was being used for output, any buffered data is written first. </p>
<p> The function <code>sox_find_effect</code> finds effect <i>name</i>, returning a pointer to its <i>sox_effect_handler_t</i> if it exists, and NULL otherwise. </p>
<p> The function <code>sox_create_effect</code> instantiates an effect into a <i>sox_effect_t</i> given a <i>sox_effect_handler_t *</i>. Any missing methods are automatically set to the corresponding <code>nothing</code> method. </p>
<p> The function <code>sox_effect_options</code> allows passing options into the effect to control its behavior. It will return SOX_EOF if there were any invalid options passed in. On success, the <i>effp-&gt;in_signal</i> will optional contain the rate and channel count it requires input data from and <i>effp-&gt;out_signal</i> will optionally contain the rate and channel count it outputs in. When present, this information should be used to make sure appropriate effects are placed in the effects chain to handle any needed conversions. </p>
<p> Passing in options is currently only supported when they are passed in before the effect is ever started. The behavior is undefined if its called once the effect is started. </p>
<p> <code>sox_create_effects_chain</code> will instantiate an effects chain that effects can be added to. <i>in_enc</i> and <i>out_enc</i> are the signal encoding of the input and output of the chain respectively. The pointers to <i>in_enc</i> and <i>out_enc</i> are stored internally and so their memory should not be freed. Also, it is OK if their values change over time to reflect new input or output encodings as they are referenced only as effects start up or are restarted. </p>
<p> <code>sox_delete_effects_chain</code> will release any resources reserved during the creation of the chain. This will also call <code>sox_delete_effects</code> if any effects are still in the chain. </p>
<p> <code>sox_add_effect</code> adds an effect to the chain. <i>in</i> specifies the input signal info for this effect. <i>out</i> is a suggestion as to what the output signal should be but depending on the effects given options and on <i>in</i> the effect can choose to do differently. Whatever output rate and channels the effect does produce are written back to <i>in</i>. It is meant that <i>in</i> be stored and passed to each new call to <code>sox_add_effect</code> so that changes will be propagated to each new effect. </p>
<p> SoX includes skeleton C files to assist you in writing new formats (skelform.c) and effects (skeleff.c). Note that new formats can often just deal with the header and then use raw.c&#8217;s routines for reading and writing. </p>
<p> example0.c and example1.c are a good starting point to see how to write applications using libsox. sox.c itself is also a good reference. </p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion <code>sox_open_input</code> and <code>sox_open_output</code> return an <i>sox_format_t</i> (which is a pointer). Otherwise, NULL is returned. TODO: Need a way to return reason for failures. Currently, relies on <code>sox_warn</code> to print information. </p>
<p> <code>sox_read</code> and <code>sox_write</code> return the number of samples successfully read or written. If an error occurs, or the end-of-file is reached, the return value is a short item count or SOX_EOF. TODO: <code>sox_read</code> does not distiguish between end-of-file and error. Need an feof() and ferror() concept to determine which occured. </p>
<p> Upon successful completion <code>sox_close</code> returns 0. Otherwise, SOX_EOF is returned. In either case, any further access (including another call to <code>sox_close</code>()) to the handler results in undefined behavior. TODO: Need a way to return reason for failures. Currently, relies on sox_warn to print information. </p>
<p> Upon successful completion <code>sox_seek</code> returns 0. Otherwise, SOX_EOF is returned. TODO Need to set a global error and implement sox_tell.</p>
<h2>ERRORS</h2>
<p> TODO</p>
<h2>INTERNALS</h2>
<p> SoX&#8217;s formats and effects operate with an internal sample format of signed 32-bit integer. The data processing routines are called with buffers of these samples, and buffer sizes which refer to the number of samples processed, not the number of bytes. File readers translate the input samples to signed 32-bit integers and return the number of samples read. For example, data in linear signed byte format is left-shifted 24 bits. </p>
<p> Representing samples as integers can cause problems when processing the audio. For example, if an effect to mix down left and right channels into one monophonic channel were to use the line </p>
<pre>
   *obuf++ = (*ibuf++ + *ibuf++)/2;
</pre>
<p> distortion might occur since the intermediate addition can overflow 32 bits. The line </p>
<pre><code>
*obuf++ = *ibuf++ / 2 + *ibuf++ / 2;
</code></pre>
<p> would get round the overflow problem (at the expense of the least significant bit). </p>
<p> Stereo data is stored with the left and right speaker data in successive samples. Quadraphonic data is stored in this order: left front, right front, left rear, right rear.</p>
<h2>FORMATS</h2>
<p> A <i>format </i> is responsible for translating between sound sample files and an internal buffer. The internal buffer is store in signed longs with a fixed sampling rate. The <i>format</i> operates from two data structures: a format structure, and a private structure. </p>
<p> The format structure contains a list of control parameters for the sample: sampling rate, data size (8, 16, or 32 bits), encoding (unsigned, signed, floating point, etc.), number of sound channels. It also contains other state information: whether the sample file needs to be byte-swapped, whether sox_seek() will work, its suffix, its file stream pointer, its <i>format</i> pointer, and the <i>private</i> structure for the <i>format .</i> </p>
<p> The <i>private </i> area is just a preallocated data array for the <i>format</i> to use however it wishes. It should have a defined data structure and cast the array to that structure. See voc.c for the use of a private data area. Voc.c has to track the number of samples it writes and when finishing, seek back to the beginning of the file and write it out. The private area is not very large. The &#8220;echo&#8221; effect has to malloc() a much larger area for its delay line buffers. </p>
<p> A <i>format</i> has 6 routines:</p>
<dl>
<dt>startread</p>
<dd> Set up the format parameters, or read in a data header, or do what needs to be done.</p>
<dt>read</p>
<dd> Given a buffer and a length: read up to that many samples, transform them into signed long integers, and copy them into the buffer. Return the number of samples actually read.</p>
<dt>stopread</p>
<dd> Do what needs to be done.</p>
<dt>startwrite</p>
<dd> Set up the format parameters, or write out a data header, or do what needs to be done.</p>
<dt>write</p>
<dd> Given a buffer and a length: copy that many samples out of the buffer, convert them from signed longs to the appropriate data, and write them to the file. If it can&#8217;t write out all the samples, fail.</p>
<dt>stopwrite</p>
<dd> Fix up any file header, or do what needs to be done.</dl>
<h2>EFFECTS</h2>
<p> Each effect runs with one input and one output stream. An effect&#8217;s implementation comprises six functions that may be called to the follow flow diagram: </p>
<pre>
LOOP (invocations with different parameters)
  getopts
  LOOP (invocations with the same parameters)
    LOOP (channels)
      start
    LOOP (whilst there is input audio to process)
      LOOP (channels)
        flow
    LOOP (whilst there is output audio to generate)
      LOOP (channels)
        drain
    LOOP (channels)
      stop
  kill
</pre>
<p> Notes: For some effects, some of the functions may not be needed and can be NULL. An effect that is marked `MCHAN&#8217; does not use the LOOP (channels) lines and must therefore perform multiple channel processing inside the affected functions. Multiple effect instances may be processed (according to the above flow diagram) in parallel.</p>
<dl>
<dt>getopts</p>
<dd> is called with a character string argument list for the effect.</p>
<dt>start</p>
<dd> is called with the signal parameters for the input and output streams.</p>
<dt>flow</p>
<dd> is called with input and output data buffers, and (by reference) the input and output data buffer sizes. It processes the input buffer into the output buffer, and sets the size variables to the numbers of samples actually processed. It is under no obligation to read from the input buffer or write to the output buffer during the same call. If the call returns SOX_EOF then this should be used as an indication that this effect will no longer read any data and can be used to switch to drain mode sooner.</p>
<dt>drain</p>
<dd> is called after there are no more input data samples. If the effect wishes to generate more data samples it copies the generated data into a given buffer and returns the number of samples generated. If it fills the buffer, it will be called again, etc. The echo effect uses this to fade away.</p>
<dt>stop</p>
<dd> is called when there are no more input samples and no more output samples to process. It is typically used to release or close resources (e.g. allocated memory or temporary files) that were set-up in <i>start</i>. See echo.c for an example.</p>
<dt>kill</p>
<dd> is called to allow resources allocated by <i>getopts</i> to be released. See pad.c for an example.</dl>
<h2>LINKING</h2>
<p> The method of linking against libsox depends on how SoX was built on your system. For a static build, just link against the libraries as normal. For a dynamic build, you should use libtool to link with the correct linker flags. See the libtool manual for details; basically, you use it as: </p>
<pre>
   libtool --mode=link gcc -o prog /path/to/libsox.la
</pre>
<h2>BUGS</h2>
<p> This manual page is both incomplete and out of date.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sox/">sox</a></code>(1), <code><a href="/docs/linux/man/7-soxformat/">soxformat</a></code>(7) </p>
<p> example*.c in the SoX source distribution.</p>
<h2>LICENSE</h2>
<p> Copyright 1998-2011 by Chris Bagwell and SoX Contributors.<br />
 Copyright 1991 Lance Norskog and Sundry Contributors. </p>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1, or (at your option) any later version. </p>
<p> This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.</p>
<h2>AUTHORS</h2>
<p> Chris Bagwell (cbagwell [at] users.sourceforge.net). Other authors and contributors are listed in the ChangeLog file that is distributed with the source code. </p>
<h2>Index</h2>
