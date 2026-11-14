---
title: "libmng(3)"
name: "libmng"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libmng/"
description: "libmng – Multiple-image Network Graphics (MNG) Reference Library 1.0.9"
---

<h2>NAME</h2>
<p> libmng &#8211; Multiple-image Network Graphics (MNG) Reference Library 1.0.9</p>
<h2>SYNOPSIS</h2>
<p> <i></i><code> </p>
<p> #include &lt;libmng.h&gt;</code> </p>
<h2>DESCRIPTION</h2>
<p> The <i>libmng</i> library supports decoding, displaying, encoding, and various other manipulations of the Multiple-image Network Graphics (MNG) format image files. It uses the <i><a href="/docs/linux/man/3-zlib/">zlib</a>(3)</i> compression library, and optionally the JPEG library by the Independant JPEG Group (IJG) and/or lcms (little cms), a color-management library by Marti Maria Saguer. </p>
<h2>I. Introduction</h2>
<p> This file describes how to use and modify the MNG reference library (known as libmng) for your own use. There are seven sections to this file: introduction, callbacks, housekeeping, reading, displaying, writing, and modification and configuration notes for various special platforms. We assume that libmng is already installed; see the INSTALL.README file for instructions on how to install libmng. </p>
<p> Libmng was written to support and promote the MNG specification. </p>
<p> The MNG-1.0 specification is available at &lt;<a rel="nofollow" href="http://www.libpng.org/pub/mng/spec/">http://www.libpng.org/pub/mng/spec/</a>&gt;. </p>
<p> Other information about MNG can be found at the MNG home page, &lt;<a rel="nofollow" href="http://www.libpng.org/pub/mng/">http://www.libpng.org/pub/mng/</a>&gt;. The latest version of libmng can be found at its own homepage at &lt;<a rel="nofollow" href="http://www.libmng.com/">http://www.libmng.com/</a>&gt;. </p>
<p> In most cases the library will not need to be changed. For standardization purposes the library contains both a Windows DLL and a makefile for building a shared library (SO). The library is written in C, but an interface for Borland Delphi is also available. </p>
<p> Libmng has been designed to handle multiple sessions at one time, to be easily modifiable, to be portable to the vast majority of machines (ANSI, K&amp;R, 32-, and 64-bit) available, and to be easy to use. </p>
<p> Libmng uses zlib for its compression and decompression of MNG files. Further information about zlib, and the latest version of zlib, can be found at the zlib home page, &lt;<a rel="nofollow" href="http://www.zlib.org/">http://www.zlib.org/</a>&gt;. The zlib compression utility is a general purpose utility that is useful for more than MNG/PNG files, and can be used without libmng. See the documentation delivered with zlib for more details. </p>
<p> Libmng optionally uses the JPEG library by the Independant JPEG Group (IJG). This library is used for the JNG sub-format, which is part of the MNG specification, and allows for inclusion of JPEG decoded and thus highly compressed (photographic) images. Further information about the IJG JPEG library and the latest sources can be found at &lt;<a rel="nofollow" href="http://www.ijg.org/">http://www.ijg.org/</a>&gt;. </p>
<p> Libmng can also optionally use the lcms (little CMS) library by Marti Maria Saguer. This library provides an excellent color-management system (CMS), which gives libmng the ability to provide full color-correction for images with the proper color-information encoded. Further information and the latest sources can be found at &lt;<a rel="nofollow" href="http://www.littlecms.com/">http://www.littlecms.com/</a>&gt;. </p>
<p> Libmng is thread safe, provided the threads are using different handles as returned by the initialization call. Each thread should have its own handle and thus its own image. Libmng does not protect itself against two threads using the same instance of a handle. </p>
<p> The libmng.h header file is the single reference needed for programming with libmng: </p>
<p> #include &lt;libmng.h&gt; </p>
<h2>II. Callbacks</h2>
<p> Libmng makes extensive use of callback functions. This is meant to keep the library as platform-independant and flexible as possible. Actually, the first call you will make to the library, already contains three parameters you can use to provide callback entry-points. </p>
<p> Most functions must return a mng_bool (boolean). Returning MNG_FALSE indicates the library the callback failed in some way and the library will immediately return from whatever it was doing back to the application. Returning MNG_TRUE indicates there were no problems and processing can continue. </p>
<p> Let&#8217;s step through each of the possible callbacks. The sections on reading, displaying and writing will also explain which callbacks are needed when and where. </p>
<p> &#8211; mng_ptr mng_memalloc (mng_size_t iLen) </p>
<p> A very basic function which the library uses to allocate a memory-block with the given size. A typical implementation would be: </p>
<p>&nbsp;<wbr>mng_ptr my_alloc&nbsp;<wbr>(mng_size_t iLen)&nbsp;<wbr>{<br />
return calloc&nbsp;<wbr>(1, iLen);<br />
&nbsp;<wbr>} </p>
<p> Note that the library requires you to zero-out the memory-block!!! </p>
<p> &#8211; void mng_memfree (mng_ptr pPtr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_size_t iLen) </p>
<p> Counterpart of the previous function. Typically: </p>
<p>&nbsp;<wbr>void my_free&nbsp;<wbr>(mng_ptr pPtr, mng_size_t iLen)&nbsp;<wbr>{<br />
free&nbsp;<wbr>(pPtr);<br />
&nbsp;<wbr>} </p>
<p> &#8211; mng_bool mng_openstream (mng_handle hHandle) </p>
<p> &#8211; mng_bool mng_closestream (mng_handle hHandle) </p>
<p> These are called by the library just before it starts to process (either read or write) a file and just after the processing stops. This is the recommended place to do I/O initialization &amp; finalization. Whether you do or not, is up to you. The library does not put any meaning into the calls. They are simply provided for your convenience. </p>
<p> &#8211; mng_bool mng_readdata (mng_handle hHandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_ptr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pBuf,&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32&nbsp;<wbr>&nbsp;<wbr>iBuflen,&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32p pRead)<br />
&nbsp;<wbr> This function is called when the library needs some more input while reading an image. The reading process supports two modes: Suspension-mode (SMOD) and non-suspension-mode (NSMOD). See mng_set_suspensionmode() for a more detailed description. </p>
<p> In NSMOD, the library requires you to return exactly the amount of bytes requested (= iBuflen). Any lesser amount indicates the input file is exhausted and the library will return a MNG_UNEXPECTEDEOF errorcode. </p>
<p> In SMOD, you may return a smaller amount of bytes than requested. This tells the library it should temporarily wait for more input to arrive. The lib will return with MNG_NEEDMOREDATA, and will expect a call to mng_read_resume() or mng_display_resume() next, as soon as more input-data has arrived. </p>
<p> For NSMOD this function could be as simple as: </p>
<p>&nbsp;<wbr>mng_bool my_read&nbsp;<wbr>(mng_handle&nbsp;<wbr>&nbsp;<wbr>hHandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_ptr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pBuf,&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32&nbsp;<wbr>&nbsp;<wbr>iBuflen,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32p pRead)&nbsp;<wbr>{<br />
*pRead&nbsp;<wbr>=&nbsp;<wbr>fread&nbsp;<wbr>(pBuf, 1, iBuflen, myfile);<br />
return MNG_TRUE;<br />
&nbsp;<wbr>} </p>
<p> &#8211; mng_bool mng_writedata (mng_handle hHandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_ptr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pBuf,&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32&nbsp;<wbr>&nbsp;<wbr>iBuflen,&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32p pWritten) </p>
<p> This function is called during the mng_write() function to actually output data to the file. There is no suspension-mode during write, so the application must return the exact number of bytes the library requests to be written. </p>
<p> A typical implementation could be: </p>
<p>&nbsp;<wbr>mng_bool my_write&nbsp;<wbr>(mng_handle&nbsp;<wbr>&nbsp;<wbr>hHandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_ptr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pBuf,&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32&nbsp;<wbr>&nbsp;<wbr>iBuflen,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32p pWritten)&nbsp;<wbr>{<br />
*pWritten&nbsp;<wbr>=&nbsp;<wbr>fwrite&nbsp;<wbr>(pBuf, 1, iBuflen, myfile);<br />
return MNG_TRUE;<br />
&nbsp;<wbr>} </p>
<p> &#8211; mng_bool mng_errorproc (mng_handle hHandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_int32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>iErrorcode,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_int8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>iSeverity,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_chunkid iChunkname,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32&nbsp;<wbr>&nbsp;<wbr>iChunkseq,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_int32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>iExtra1,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_int32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>iExtra2,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_pchar&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>zErrortext) </p>
<p> This function is called whenever an error is detected inside the library. This may be caused by invalid input, callbacks indicating failure, or wrongfully calling functions out of place. </p>
<p> If you do not provide this callback the library will still return an errorcode from the called function, and the mng_getlasterror() function can be used to retrieve the other parameters. </p>
<p> This function is currently only provided for convenience, but may at some point be used to indicate certain errors may be acceptable, and processing should continue. </p>
<p> &#8211; mng_bool mng_traceproc (mng_handle hHandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_int32&nbsp;<wbr>&nbsp;<wbr>iFuncnr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_int32&nbsp;<wbr>&nbsp;<wbr>iFuncseq,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_pchar&nbsp;<wbr>&nbsp;<wbr>zFuncname) </p>
<p> This function is provided to allow a functional analysis of the library. This may be useful if you encounter certain errors and cannot determine what the problem is. </p>
<p> Almost all functions inside the library will activate this callback with an appropriate function-name at the start and end of the function. Please note that large images may generate an enormous amount of calls. </p>
<p> &#8211; mng_bool mng_processheader (mng_handle hHandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32 iWidth,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32 iHeight) </p>
<p> This function is called once the header information of an input- image has been processed. At this point the image dimensions are available and also some other properties depending on the type of the image. Eg. for a MNG the frame-/layercount, playtime &amp; simplicity fields are known. </p>
<p> The primary purpose of this callback is to inform the application of the size of the image, and for the application to initialize the drawing canvas to be used by the library. This is also a good point to set the canvas-style. Eg. mng_set_canvasstyle(). </p>
<p> &#8211; mng_bool mng_processtext (mng_handle hHandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint8&nbsp;<wbr>&nbsp;<wbr>iType,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_pchar&nbsp;<wbr>&nbsp;<wbr>zKeyword,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_pchar&nbsp;<wbr>&nbsp;<wbr>zText,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_pchar&nbsp;<wbr>&nbsp;<wbr>zLanguage,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_pchar&nbsp;<wbr>&nbsp;<wbr>zTranslation) </p>
<p> This callback is activated for each textual chunk in the input- image. These are tEXt, zTXt &amp; iTXt. It may be used to retain specific comments for presentation to the user. </p>
<p> &#8211; mng_bool mng_processsave (mng_handle hHandle) </p>
<p> &#8211; mng_bool mng_processseek (mng_handle hHandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_pchar&nbsp;<wbr>&nbsp;<wbr>zName) </p>
<p> The purpose of these callbacks is to signal the processing of the SAVE &amp; SEEK chunks in a MNG input-file. This may be used in the future to specify some special processing. At the moment these functions are only provided as a signal. </p>
<p> &#8211; mng_ptr mng_getcanvasline (mng_handle hHandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32 iLinenr) </p>
<p> &#8211; mng_ptr mng_getbkgdline (mng_handle hHandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32 iLinenr) </p>
<p> &#8211; mng_ptr mng_getalphaline (mng_handle hHandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32 iLinenr) </p>
<p> These callbacks are used to access the drawing canvas, background canvas and an optional separate alpha-channel canvas. The latter is used only with the MNG_CANVAS_RGB8_A8 canvas-style. </p>
<p> If the getbkgdline() callback is not supplied the library will composite fully or partially transparent pixels in the image against a specified background color. See mng_set_bgcolor() for more details. If a chosen canvas-style includes an alpha-channel, this callback is very likely not needed. </p>
<p> The application is responsible for returning a pointer to a line of pixels, which should be in the exact format as defined by the call to mng_set_canvasstyle() and mng_set_bkgdstyle(), without gaps between the representation of each pixel, unless specified by the canvas-style. </p>
<p> &#8211; mng_bool mng_refresh (mng_handle hHandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32 iX,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32 iY,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32 iWidth,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32 iHeight) </p>
<p> This callback is called when the library has drawn a complete frame onto the drawing canvas, and it is ready to be displayed. The application is responsible for transferring the drawing canvas from memory onto the actual output device. </p>
<p> &#8211; mng_uint32 mng_gettickcount (mng_handle hHandle) </p>
<p> This function should return the number of milliseconds on some internal clock. The entire animation timing depends heavily on this function, and the number returned should be as accurate as possible. </p>
<p> &#8211; mng_bool mng_settimer (mng_handle hHandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32 iMsecs) </p>
<p> This callback is activated every time the library requires a &quot;pause&quot;. Note that the function itself should NOT execute the wait. It should simply store the time-field and allow the library to return. Libmng will return with the MNG_NEEDTIMERWAIT code, indicating the callback was called and it is now time to execute the pause. </p>
<p> After the indicated number of milliseconds have elapsed, the application should call mng_display_resume(), to resume the animation as planned. </p>
<p> This method allows for both a real timer or a simple wait command in the application. Whichever method you select, both the gettickcount() and settimer() callbacks are crucial for proper animation timing. </p>
<p> &#8211; mng_bool mng_processgamma (mng_handle hHandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32 iGamma) </p>
<p> &#8211; mng_bool mng_processchroma (mng_handle hHandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32 iWhitepointx,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32 iWhitepointy,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32 iRedx,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32 iRedy,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32 iGreenx,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32 iGreeny,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32 iBluex,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32 iBluey) </p>
<p> &#8211; mng_bool mng_processsrgb (mng_handle hHandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint8&nbsp;<wbr>&nbsp;<wbr>iRenderingintent) </p>
<p> &#8211; mng_bool mng_processiccp (mng_handle hHandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32 iProfilesize,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_ptr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pProfile) </p>
<p> &#8211; mng_bool mng_processarow (mng_handle hHandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32 iRowsamples,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_bool&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>bIsRGBA16,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_ptr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pRow) </p>
<p> These callbacks are only required when you selected the MNG_APP_CMS directive during compilation of the library. See the configuration section for more details. </p>
<p> &#8211; mng_bool mng_iteratechunk (mng_handle hHandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_handle&nbsp;<wbr>&nbsp;<wbr>hChunk,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_chunkid iChunkid,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32&nbsp;<wbr>&nbsp;<wbr>iChunkseq) </p>
<p> This callback is only used for the mng_iterate_chunks() function. It is called exactly once for each chunk stored. </p>
<h2>III. Housekeeping</h2>
<h3>Memory management</h3>
<p> The library can use internal memory allocation/deallocation or use provided callbacks for its memory management. The choice is made at compilation time. See the section on customization for details. </p>
<p> If internal management has been selected, the memory callback functions need not be supplied. Even if you do supply them they will not be used. The actual code used is similar to the code discussed in the callback section: </p>
<p>pPtr&nbsp;<wbr>=&nbsp;<wbr>calloc&nbsp;<wbr>(1, iLen); </p>
<p>free&nbsp;<wbr>(pPtr); </p>
<p> If your compiler does not support these functions, or you wish to monitor the library&#8217;s use of memory for certain reasons, you can choose to compile the library with external memory management. In this case the memory callback functions MUST be supplied, and should function as if the above code was used. </p>
<h3>Initialization</h3>
<p> The basic initialization of the library is short and swift: </p>
<p>&nbsp;<wbr>myhandle&nbsp;<wbr>=&nbsp;<wbr>mng_initialize&nbsp;<wbr>(myuserdata, my_alloc,&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>my_free, MNG_NULL);<br />
&nbsp;<wbr>if&nbsp;<wbr>(myhandle&nbsp;<wbr>==&nbsp;<wbr>MNG_NULL)<br />
/*&nbsp;<wbr>process error&nbsp;<wbr>*/; </p>
<p> The first field is an application-only parameter. It is saved in libmng&#8217;s internal structures and available at all times through the mng_get_userdata() function. This is especially handy in callback functions if your program may be handling multiple files at the same time. </p>
<p> The second and third field supply the library with the memory callback function entry-points. These are described in more detail in the callback section and the previous paragraph. </p>
<p> The fourth and last field may be used to supply the library with the entry-point of a trace callback function. For regular use you will not need this! </p>
<p> The function returns a handle which will be your ticket to MNG-heaven. All other functions rely on this handle. It is the single fixed unique reference-point between your application and the library. </p>
<p> You should call the initialization function for each image you wish to process simultaneously. If you are processing images consecutively, you can reset the internal status of the library with the mng_reset() function. This function will clear all internal state variables, free any stored chunks and/or objects, etc, etc. Your callbacks and other external parameters will be retained. </p>
<p> After you successfully received the handle it is time to set the required callbacks. The sections on reading, displaying &amp; writing indicate which callbacks are required and which are optional. To set the callbacks simply do: </p>
<p>&nbsp;<wbr>myretcode&nbsp;<wbr>=&nbsp;<wbr>mng_setcb_xxxxxx&nbsp;<wbr>(myhandle, my_xxxxxx);<br />
&nbsp;<wbr>if&nbsp;<wbr>(myretcode&nbsp;<wbr>!=&nbsp;<wbr>MNG_NOERROR)<br />
/*&nbsp;<wbr>process error&nbsp;<wbr>*/; </p>
<p> Naturally you&#8217;d replace the x&#8217;s with the name of the callback. </p>
<h3>Cleanup</h3>
<p> Once you&#8217;ve gotten hold of that precious mng_handle, you should always, and I mean always, call the cleanup function when you&#8217;re done. Just do: </p>
<p>&nbsp;<wbr>mng_cleanup&nbsp;<wbr>(myhandle); </p>
<p> And you&#8217;re done. There shouldn&#8217;t be an ounce of memory spilled after that call. </p>
<p> Note that if you would like to process multiple files consecutively you do not need to do mng_cleanup() / mng_initialize() between each file but simply </p>
<p>&nbsp;<wbr>myretcode&nbsp;<wbr>=&nbsp;<wbr>mng_reset&nbsp;<wbr>(myhandle);<br />
&nbsp;<wbr>if&nbsp;<wbr>(myretcode&nbsp;<wbr>!=&nbsp;<wbr>MNG_NOERROR)<br />
/*&nbsp;<wbr>process error&nbsp;<wbr>*/; </p>
<p> will suffice. Saves some time and effort, that. </p>
<h3>Error handling</h3>
<p> From the examples in the previous paragraphs you may have noticed a meticulous scheme for error handling. And yes, that&#8217;s exactly what it is. Practically each call simply returns an errorcode, indicating success, eg. MNG_NOERROR or failure, anything else but MNG_NEEDMOREDATA and MNG_NEEDTIMERWAIT. These latter two will be discussed in more detail in their respective fields of interest: the reading section and displaying section respectively. </p>
<p> It is the application&#8217;s responsibility to check the returncode after each call. You can call mng_getlasterror() to receive the details of the last detected error. This even includes a discriptive error-message if you enabled that option during compilation of the library. </p>
<p> Note that after receiving an error it is still possible to call the library, but it&#8217;s also very likely that any following call will fail. The only functions deemed to work will be mng_reset() and mng_cleanup(). Yes, if you abort your program after an error, you should still call mng_cleanup(). </p>
<h2>IV. Reading</h2>
<p> Reading a MNG, JNG or PNG is fairly easy. It depends slightly on your ultimate goal how certain specifics are to be handled, but the basics are similar in all cases. </p>
<p> For the read functioins to work you must have compiled the library with the MNG_READ_SUPPRT directive. The standard DLL and Shared Library have this on by default! </p>
<h3>Setup</h3>
<p> Naturally you must have initialized the library and be the owner of a mng_handle. The following callbacks are essential: </p>
<p>&nbsp;<wbr>mng_openstream, mng_readdata, mng_closestream </p>
<p> You may optionally define: </p>
<p>&nbsp;<wbr>mng_errorproc, mng_traceproc<br />
&nbsp;<wbr>mng_processheader, mng_processtext<br />
&nbsp;<wbr>mng_processsave, mng_processseek </p>
<p> The reading bit will also fail if you are already creating or displaying a file. Seems a bit obvious, but I thought I&#8217;d mention it, just in case. </p>
<h3>To suspend or not to suspend</h3>
<p> There is one choice you need to make before calling the read function. Are you in need of suspension-mode or not? </p>
<p> If you&#8217;re reading from a disk you most certainly do not need suspension-mode. Even the oldest and slowest of disks will be fast enough for straight reading. </p>
<p> However, if your input comes from a really slow device, such as a dialup-line or the likes, you may opt for suspension-mode. This is done by calling </p>
<p>&nbsp;<wbr>myretcode&nbsp;<wbr>=&nbsp;<wbr>mng_set_suspensionmode&nbsp;<wbr>(myhandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>MNG_TRUE);<br />
&nbsp;<wbr>if&nbsp;<wbr>(myretcode&nbsp;<wbr>!=&nbsp;<wbr>MNG_NOERROR)<br />
/*&nbsp;<wbr>process error&nbsp;<wbr>*/; </p>
<p> Suspension-mode will force the library to use special buffering on the input. This allows your application to receive data of arbitrarily length and return this in the mng_readdata() callback, without disturbing the chunk processing routines of the library. </p>
<p> Suspension-mode does require a little extra care in the main logic of the application. The read function may return with MNG_NEEDMOREDATA when the mng_readdata() callback returns less data then it needs to process the next chunk. This indicates the application to wait for more data to arrive and then resume processing by calling mng_read_resume(). </p>
<h3>The read HLAPI</h3>
<p> The actual reading is just plain simple. Since all I/O is done outside the library through the callbacks, the library can focus on its real task. Understanding, checking and labelling the input data! </p>
<p> All you really need to do is this: </p>
<p>&nbsp;<wbr>myretcode&nbsp;<wbr>=&nbsp;<wbr>mng_read&nbsp;<wbr>(myhandle);<br />
&nbsp;<wbr>if&nbsp;<wbr>(myretcode&nbsp;<wbr>!=&nbsp;<wbr>MNG_NOERROR)<br />
/*&nbsp;<wbr>process error&nbsp;<wbr>*/; </p>
<p> Of course, if you&#8217;re on suspension-mode the code is a little more complicated: </p>
<p>&nbsp;<wbr>myretcode&nbsp;<wbr>=&nbsp;<wbr>mng_read&nbsp;<wbr>(myhandle); </p>
<p>&nbsp;<wbr>while&nbsp;<wbr>(myretcode&nbsp;<wbr>==&nbsp;<wbr>MNG_NEEDMOREDATA)&nbsp;<wbr>{<br />
/*&nbsp;<wbr>wait for input-data to arrive&nbsp;<wbr>*/<br />
myretcode&nbsp;<wbr>=&nbsp;<wbr>mng_read_resume&nbsp;<wbr>(myhandle);<br />
&nbsp;<wbr>}&nbsp;<wbr> </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(myretcode&nbsp;<wbr>!=&nbsp;<wbr>MNG_NOERROR)<br />
/*&nbsp;<wbr>process error&nbsp;<wbr>*/; </p>
<p> This is rather crude and more sophisticated programming methods may dictate another approach. Whatever method you decide on, it should act as if the above code was in its place. </p>
<p> There is also the mng_readdisplay() function, but this is discussed in the displaying section. It functions pretty much as the mng_read() function, but also immediately starts displaying the image. mng_read_resume() should be replaced by mng_display_resume() in that case! </p>
<h3>What happens inside</h3>
<p> What actually happens inside the library depends on the configuration options set during the compilation of the library. </p>
<p> Basically the library will first read the 8-byte file header, to determine its validity and the type of image it is about to process. Then it will repeatedly read a 4-byte chunk-length and then the remainder of the chunk until it either reaches EOF (indicated by the mng_readdata() callback) or implicitly decides EOF as it processed the logically last chunk of the image. </p>
<p> Applications that require strict conformity and do not allow superfluous data after the ending chunk, will need to perform this check in their mng_closestream() callback. </p>
<p> Each chunk is then checked on CRC, after which it is handed over to the appropriate chunk processing routine. These routines will disect the chunk, check the validity of its contents, check its position with respect to other chunks, etc, etc. </p>
<p> If everything checks out, the chunk is further processed as follows: </p>
<p> If display support has been selected during compilation, certain pre-display initialization will take place. </p>
<p> If chunk-storage support has been selected during compilation, the chunks data may be stored in a special internal structure and held for future reference. </p>
<h3>Storing and accessing chunks</h3>
<p> One of the compilation options activates support for chunk storage. This option may be useful if you want to examine an image. The directive is MNG_STORE_CHUNKS. You must also turn on the MNG_ACCESS_CHUNKS directive. </p>
<p> The actual storage facility can be turned on or off with the mng_set_storechunks() function. If set to MNG_TRUE, chunks will be stored as they are read. </p>
<p> At any point you can then call the mng_iterate_chunks() function to iterate through the current list of chunks. This function requires a callback which is called for each chunk and receives a specific chunk-handle. This chunk-handle can be used to call the appropriate mng_getchunk_xxxx() function, to access the chunks properties. </p>
<p> A typical implementation may look like this: </p>
<p>&nbsp;<wbr>mng_bool my_iteratechunk&nbsp;<wbr>(mng_handle&nbsp;<wbr>&nbsp;<wbr>hHandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_handle&nbsp;<wbr>&nbsp;<wbr>hChunk,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_chunkid iChunkid,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32&nbsp;<wbr>&nbsp;<wbr>iChunkseq)&nbsp;<wbr>{<br />
switch&nbsp;<wbr>(iChunkid)&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>case MNG_UINT_MHDR :&nbsp;<wbr>{&nbsp;<wbr>/*&nbsp;<wbr>process MHDR&nbsp;<wbr>*/;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>break;&nbsp;<wbr>}<br />
&nbsp;<wbr>&nbsp;<wbr>case MNG_UINT_FRAM :&nbsp;<wbr>{&nbsp;<wbr>/*&nbsp;<wbr>process FRAM&nbsp;<wbr>*/;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>break;&nbsp;<wbr>} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8230;etc&#8230; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>case MNG_UINT_HUH&nbsp;<wbr>&nbsp;<wbr>:&nbsp;<wbr>{&nbsp;<wbr>/*&nbsp;<wbr>unknown chunk&nbsp;<wbr>*/;&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>break;&nbsp;<wbr>}<br />
&nbsp;<wbr>&nbsp;<wbr>default :&nbsp;<wbr>{&nbsp;<wbr>/*&nbsp;<wbr>duh;&nbsp;<wbr>forgot one&nbsp;<wbr>*/;&nbsp;<wbr>}<br />
} </p>
<p>return MNG_TRUE;&nbsp;<wbr>/*&nbsp;<wbr>keep&#8217;m coming&nbsp;<wbr>*/<br />
&nbsp;<wbr>} </p>
<p> To get to the actual chunk fields of lets say a SHOW chunk you would do: </p>
<p>&nbsp;<wbr>mng_bool isempty;<br />
&nbsp;<wbr>mng_uint16 firstid, lastid;<br />
&nbsp;<wbr>mng_uint8 showmode; </p>
<p>&nbsp;<wbr>myretcode mng_getchunk_show&nbsp;<wbr>(hHandle, hChunk,&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>isempty, firstid,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>lastid, showmode);<br />
&nbsp;<wbr>if&nbsp;<wbr>(myretcode&nbsp;<wbr>!=&nbsp;<wbr>MNG_NOERROR)<br />
/*&nbsp;<wbr>process error&nbsp;<wbr>*/; </p>
<h2>V. Displaying</h2>
<h3>Setup</h3>
<p> Assuming you have initialized the library and are the owner of a mng_handle. The following callbacks are essential: </p>
<p>&nbsp;<wbr>mng_getcanvasline, mng_refresh<br />
&nbsp;<wbr>mng_gettickcount, mng_settimer </p>
<p> If you wish to use an application supplied background you must supply: </p>
<p>&nbsp;<wbr>mng_getbkgdline </p>
<p> If you wish to use the MNG_CANVAS_RGB8_A8 canvas style you must supply: </p>
<p>&nbsp;<wbr>mng_getalphaline </p>
<p> You may optionally define: </p>
<p>&nbsp;<wbr>mng_errorproc, mng_traceproc<br />
&nbsp;<wbr>mng_processheader, mng_processtext<br />
&nbsp;<wbr>mng_processsave, mng_processseek </p>
<p> Note that the mng_processheader() callback is optional but will be quite significant for proper operation! </p>
<p> Displaying an image will fail if you are creating a file or already displaying one. Yes, you can&#8217;t display it twice! </p>
<h3>A word on canvas styles</h3>
<p> The canvas style describes how your drawing canvas is made up. You must set this before the library actually starts drawing, so the mng_processheader() callback is a pretty good place for it. </p>
<p> Currently only 8-bit RGB canvas styles are supported, either with or without an alpha channel. </p>
<p> If you like to do alpha composition yourself you can select one of the canvas styles that include an alpha channel. You can even have a separate alpha canvas by selecting the MNG_CANVAS_RGB8_A8 style. </p>
<p> All styles require a compact model. Eg. MNG_CANVAS_BGR8 requires your canvas lines in bgrbgrbgr&#8230; storage, where each letter represents an 8-bit value of the corresponding color, and each threesome makes up the values of <a href="/docs/linux/man/1-one/">one</a>(1) pixel. </p>
<p> The library processes a line at a time, so the canvas lines do not actually need to be consecutive in memory. </p>
<h3>Alpha composition and application backgrounds</h3>
<p> All Network Graphics can be partially transparent. This requires special processing if you need to display an image against some background. Note that the MNG header (MHDR chunk) contains a simplicity field indicating whether transparency information in the file is critical or not. This only applies to embedded images, which means the full image-frame of the MNG may still contain fully transparent pixels! </p>
<p> Depending on your needs you can supply a single background color, a background canvas or tell the library to return the alpha-channel and do alpha composition yourself. </p>
<p> This is different from the BACK chunk in a MNG, or the bKGD chunk in an (embedded) PNG or JNG. The BACK chunk indicates an optional or mandatory background color and/or image. The bKGD chunk only indicates an optional background color. These chunks indicate the Authors preferences. They may be absent in which case you need to supply some sort of background yourself. </p>
<h3>Composing against a background color</h3>
<p> This is the easiest method. Call the mng_set_bgcolor() function to set the values of the red, green and blue component of your preferred background color. </p>
<p> Use one of the canvas styles that do not have an alpha-channel, and which matches your output requirements. </p>
<h3>Composing against a background canvas</h3>
<p> This is somewhat more complicated. You will need to set the mng_getbkgdline() callback. This will be called whenever the library needs to compose a partially transparent line. </p>
<p> This canvas must hold the background against which the image should be composed. Its size must match exactly with the image dimensions and thus the drawing canvas! </p>
<p> Use one of the canvas styles that do not have an alpha-channel, and which matches your output requirements. The canvas style of the background canvas may even differ from the drawing canvas. The library&#8217;s composing will still function properly. </p>
<h3>Composing within the application</h3>
<p> If you have the option in your application to draw a (partially) transparent canvas to the output device, this option is preferred. </p>
<p> Select one of the canvas styles that do have an alpha-channel. The library will now supply the appropriate alpha information, allowing the application to compose the image as it sees fit. </p>
<h3>Color information and CMS</h3>
<p> Network Graphics may, and usually will, contain color-correction information. This information is intended to compensate for the difference in recording and display devices used. </p>
<p> This document does not address the specifics of color-management. See the PNG specification for a more detailed description. </p>
<h3>Using little cms by Marti Maria Saguer</h3>
<p> This is the easiest method, providing you can compile the lcms package. Select the MNG_FULL_CMS directive during compilation, and sit back and relax. The library will take care of all color-correction for you. </p>
<h3>Using an OS- or application-supplied CMS</h3>
<p> If you are so lucky to have access to CMS functionality from within your application, you may instruct the library to leave color-correction to you. </p>
<p> Select the MNG_APP_CMS directive during compilation of the library. You MUST also set the following callbacks: </p>
<p>&nbsp;<wbr>mng_processgamma, mng_processchroma,<br />
&nbsp;<wbr>mng_processsrgb, mng_processiccp and<br />
&nbsp;<wbr>mng_processarow </p>
<p> The last callback is called when the library needs you to correct an arbitrary line of pixels. The other callbacks are called when the corresponding color-information is encountered in the file. You must store this information somewhere for use in the mng_processarow() callback. </p>
<h3>Using gamma-only correction</h3>
<p> This isn&#8217;t a preferred method, but it&#8217;s better than no correction at all. Gamma-only correction will at least compensate for gamma-differences between the original recorder and your output device. </p>
<p> Select the MNG_GAMMA_ONLY directive during compilation of the library. Your compiler MUST support fp operations. </p>
<h3>No color correction</h3>
<p> Ouch. This is really bad. This is the least preferred method, but may be necessary if your system cannot use lcms, doesn&#8217;t have its own CMS, and does not allow fp operations, ruling out the gamma-only option. </p>
<p> Select the MNG_NO_CMS directive during compilation. Images will definitely not be displayed as seen by the Author!!! </p>
<h3>Animations and timing</h3>
<p> Animations require some form of timing support. The library relies on two callbacks for this purpose. The mng_gettickcount() and mng_settimer() callbacks. mng_gettickcount() is used to determine the passing of time in milliseconds since the beginning of the animation. This is also used to compensate during suspension-mode if you are using the mng_readdisplay() function to read &amp; display the file simultaneously. </p>
<p> The callback may return an arbitrary number of milliseconds, but this number must increase proportionaly between calls. Most modern systems will have some tickcount() function which derives its input from an internal clock. The value returned from this function is more than adequate for libmng. </p>
<p> The mng_settimer() callback is called when the library determines a little &quot;pause&quot; is required before rendering another frame of the animation. The pause interval is also expressed in milliseconds. Your application should store this value and return immediately. The library will then make appropriate arrangements to store its internal state and returns to your application with the MNG_NEEDTIMERWAIT code. </p>
<p> At that point you should suspend processing and wait the given interval. Please use your OS features for this. Do not engage some sort of loop. That is real bad programming practice. Most modern systems will have some timing functions. A simple wait() function may suffice, but this may prevent your applications main-task from running, and possibly prevent the actual update of your output device. </p>
<h3>The mng_refresh() callback</h3>
<p> The mng_refresh() callback is called whenever the library has &quot;finished&quot; drawing a new frame onto your canvas, and just before it will call the mng_settimer() callback. </p>
<p> This allows you to perform some actions necessary to &quot;refresh&quot; the canvas onto your output device. Please do NOT suspend processing inside this callback. This must be handled after the mng_settimer() callback! </p>
<h3>Displaying while reading</h3>
<p> This method is preferred if you are reading from a slow input device (such as a dialup-line) and you wish to start displaying something as quickly as possible. This functionality is provided mainly for browser-type applications but may be appropriate for other applications as well. </p>
<p> The method is usually used in unison with the suspension-mode of the read module. A typical implementation would look like this: </p>
<p>&nbsp;<wbr>/*&nbsp;<wbr>initiale library and set required callbacks&nbsp;<wbr>*/ </p>
<p>&nbsp;<wbr>/*&nbsp;<wbr>activate suspension-mode&nbsp;<wbr>*/<br />
&nbsp;<wbr>myretcode&nbsp;<wbr>=&nbsp;<wbr>mng_set_suspensionmode&nbsp;<wbr>(myhandle,&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>MNG_TRUE);<br />
&nbsp;<wbr>if&nbsp;<wbr>(myretcode&nbsp;<wbr>!=&nbsp;<wbr>MNG_NOERROR)<br />
/*&nbsp;<wbr>process error&nbsp;<wbr>*/; </p>
<p>&nbsp;<wbr>myretcode&nbsp;<wbr>=&nbsp;<wbr>mng_readdisplay&nbsp;<wbr>(myhandle); </p>
<p>&nbsp;<wbr>while&nbsp;<wbr>((myretcode&nbsp;<wbr>==&nbsp;<wbr>MNG_NEEDMOREDATA)&nbsp;<wbr>||<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(myretcode&nbsp;<wbr>==&nbsp;<wbr>MNG_NEEDTIMERWAIT))&nbsp;<wbr>{<br />
if&nbsp;<wbr>(myretcode&nbsp;<wbr>==&nbsp;<wbr>MNG_NEEDMOREDATA)<br />
&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>wait for more input-data&nbsp;<wbr>*/;<br />
else<br />
&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>wait for timer interval&nbsp;<wbr>*/; </p>
<p>myretcode&nbsp;<wbr>=&nbsp;<wbr>mng_display_resume&nbsp;<wbr>(myhandle);<br />
&nbsp;<wbr>} </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(myretcode&nbsp;<wbr>!=&nbsp;<wbr>MNG_NOERROR)<br />
/*&nbsp;<wbr>process error&nbsp;<wbr>*/; </p>
<p> More advanced programming methods may require a different approach, but the final result should function as in the code above. </p>
<h3>Displaying after reading</h3>
<p> This method is used to display a file that was previously read. It is primarily meant for viewers with direct file access, such as 1a local harddisk. </p>
<p> Once you have successfully read the file, all you need to do is: </p>
<p>&nbsp;<wbr>myretcode&nbsp;<wbr>=&nbsp;<wbr>mng_display&nbsp;<wbr>(myhandle); </p>
<p>&nbsp;<wbr>while&nbsp;<wbr>(myretcode&nbsp;<wbr>==&nbsp;<wbr>MNG_NEEDTIMERWAIT)&nbsp;<wbr>{<br />
/*&nbsp;<wbr>wait for timer interval&nbsp;<wbr>*/;<br />
myretcode&nbsp;<wbr>=&nbsp;<wbr>mng_display_resume&nbsp;<wbr>(myhandle);<br />
&nbsp;<wbr>} </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(myretcode&nbsp;<wbr>!=&nbsp;<wbr>MNG_NOERROR)<br />
/*&nbsp;<wbr>process error&nbsp;<wbr>*/; </p>
<p> Again, more advanced programming methods may require a different approach, but the final result should function as in the code above. </p>
<h3>Display manipulation</h3>
<p> Several HLAPI functions are provided to allow a user to manipulate the normal flow of an animation. </p>
<p> &#8211; mng_display_freeze (mng_handle hHandle) </p>
<p> This will &quot;freeze&quot; the animation in place. </p>
<p> &#8211; mng_display_resume (mng_handle hHandle) </p>
<p> This function can be used to resume a frozen animation, or to force the library to advance the animation to the next frame. </p>
<p> &#8211; mng_display_reset (mng_handle hHandle) </p>
<p> This function will &quot;reset&quot; the animation into its pristine state. Calling mng_display() afterwards will re-display the animation from the first frame. </p>
<p> &#8211; mng_display_golayer (mng_handle hHandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32 iLayer) </p>
<p> &#8211; mng_display_goframe (mng_handle hHandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32 iFrame) </p>
<p> &#8211; mng_display_gotime (mng_handle hHandle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mng_uint32 iPlaytime) </p>
<p> These three functions can be used to &quot;jump&quot; to a specific layer, frame or timeslot in the animation. You must &quot;freeze&quot; the animation before using any of these functions. </p>
<p> All above functions may only be called during a timer interval! It is the applications responsibility to cleanup any resources with respect to the timer wait. </p>
<h2>VI. Writing</h2>
<p> The main focus of the library lies in its displaying capabilites. But it does offer writing support as well. You can create and write a file, or you can write a file you have previously read, providing the storage of chunks was enabled and active. </p>
<p> For this to work you must have compiled the library with the MNG_WRITE_SUPPO1RT and MNG_ACCESS_CHUNKS directives. The standard DLL and Shared Library have this on by default! </p>
<h3>Setup</h3>
<p> As always you must have initialized the library and be the owner of a mng_handle. The following callbacks are essential: </p>
<p>&nbsp;<wbr>mng_openstream, mng_writedata, mng_closestream </p>
<p> You can optionally define: </p>
<p>&nbsp;<wbr>mng_errorproc, mng_traceproc </p>
<p> The creation and writing functions will fail if you are in the middle of reading, creating or writing a file. </p>
<h3>Creating a new file</h3>
<p> To start a new file the library must be in its initial state. First you need to tell the library your intentions: </p>
<p>&nbsp;<wbr>myretcode&nbsp;<wbr>=&nbsp;<wbr>mng_create&nbsp;<wbr>(myhandle);<br />
&nbsp;<wbr>if&nbsp;<wbr>(myretcode&nbsp;<wbr>!=&nbsp;<wbr>MNG_NOERROR)<br />
/*&nbsp;<wbr>process error&nbsp;<wbr>*/; </p>
<p> After that you start adding the appropriate chunks: </p>
<p>&nbsp;<wbr>myretcode&nbsp;<wbr>=&nbsp;<wbr>mng_put1chunk_mhdr&nbsp;<wbr>(myhandle, &#8230;);<br />
&nbsp;<wbr>if&nbsp;<wbr>(myretcode&nbsp;<wbr>!=&nbsp;<wbr>MNG_NOERROR)<br />
/*&nbsp;<wbr>process error&nbsp;<wbr>*/; </p>
<p> And so on, and so forth. Note that the library will automatically signal the logical end of the file by the ending chunk. Also the first chunk will indicate the library the filetype (eg. PNG, JNG or MNG) and force the proper signature when writing the file. </p>
<p> The code above can be simplified, as you can always get the last errorcode by using the mng_getlasterror() function: </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(&nbsp;<wbr>(mng_putchunk_xxxx&nbsp;<wbr>(myhandle, &#8230;))&nbsp;<wbr>or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(mng_putchunk_xxxx&nbsp;<wbr>(myhandle, &#8230;))&nbsp;<wbr>or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8230;etc&#8230;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>)<br />
/*&nbsp;<wbr>process error&nbsp;<wbr>*/; </p>
<p> Please note that you must have a pretty good understanding of the chunk specification. Unlike the read functions, there are virtually no checks, so it is quite possible to write completely wrong files. It is a good practice to read back your file into the library to verify its integrity. </p>
<p> Once you&#8217;ve got all the chunks added, all you do is: </p>
<p>&nbsp;<wbr>myretcode mng_write&nbsp;<wbr>(myhandle);<br />
&nbsp;<wbr>if&nbsp;<wbr>(myretcode&nbsp;<wbr>!=&nbsp;<wbr>MNG_NOERROR)<br />
/*&nbsp;<wbr>process error&nbsp;<wbr>*/; </p>
<p> And presto. You&#8217;re done. The real work is of course carried out in your callbacks. Note that this is a single operation as opposed to the read &amp; display functions that may return with MNG_NEEDMOREDATA and/or MNG_NEEDTIMERWAIT. The write function just does the job, and only returns after it&#8217;s finished or if it encounters some unrecoverable error. </p>
<h3>Writing a previously read file</h3>
<p> If you have already successfully read a file, you can use the library to write it out as a copy or something. You MUST have compiled the library with the MNG_STORE_CHUNKS directive, and you must have done mng_set_storechunks (myhandle, MNG_TRUE). </p>
<p> This doesn&#8217;t require the MNG_ACCESS_CHUNKS directive, unless you want to fiddle with the chunks as well. </p>
<p> Again all you need to do is: </p>
<p>&nbsp;<wbr>myretcode mng_write&nbsp;<wbr>(myhandle);<br />
&nbsp;<wbr>if&nbsp;<wbr>(myretcode&nbsp;<wbr>!=&nbsp;<wbr>MNG_NOERROR)<br />
/*&nbsp;<wbr>process error&nbsp;<wbr>*/; </p>
<h2>VII. Modifying/Customizing libmng:</h2>
<p> not finished yet </p>
<h3>Compilation directives</h3>
<p> not finished yet </p>
<h3>Platform dependant modification</h3>
<p> not finished yet </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-mng/">mng</a>(5),</i><a href="/docs/linux/man/5-jng/">jng</a>(5),<i><a href="/docs/linux/man/5-png/">png</a>(5),</i><a href="/docs/linux/man/3-libpng/">libpng</a>(3) </p>
<p> libmng :</p>
<dl>
<dt>
<dd>
 <a rel="nofollow" href="http://www.libmng.com">http://www.libmng.com</a> </p>
</dl>
<p> zlib :</p>
<dl>
<dt>
<dd>
 <a rel="nofollow" href="http://www.info-zip.org/pub/infozip/zlib/">http://www.info-zip.org/pub/infozip/zlib/</a> </p>
</dl>
<p> IJG JPEG library :</p>
<dl>
<dt>
<dd>
 <a rel="nofollow" href="http://www.ijg.org">http://www.ijg.org</a> </p>
</dl>
<p> lcms (little CMS) by Marti Maria Saguer :</p>
<dl>
<dt>
<dd>
 <a rel="nofollow" href="http://www.littlecms.com/">http://www.littlecms.com/</a> </p>
</dl>
<p> MNG specification:</p>
<dl>
<dt>
<dd>
 <a rel="nofollow" href="http://www.libpng.org/pub/mng">http://www.libpng.org/pub/mng</a> </p>
</dl>
<p> In the case of any inconsistency between the MNG specification and this library, the specification takes precedence. </p>
<h2>AUTHORS</h2>
<p> This man page: Gerard Juyn &lt;gerard at libmng.com&gt; </p>
<p> The contributing authors would like to thank all those who helped with testing, bug fixes, and patience. This wouldn&#8217;t have been possible without all of you!!! </p>
<h2>COPYRIGHT NOTICE:</h2>
<p> Copyright (c) 2000-2002 Gerard Juyn </p>
<p> For the purposes of this copyright and license, &quot;Contributing Authors&quot; is defined as the following set of individuals: </p>
<p>Gerard Juyn </p>
<p> The MNG Library is supplied &quot;AS IS&quot;. The Contributing Authors disclaim all warranties, expressed or implied, including, without limitation, the warranties of merchantability and of fitness for any purpose. The Contributing Authors assume no liability for direct, indirect, incidental, special, exemplary, or consequential damages, which may result from the use of the MNG Library, even if advised of the possibility of such damage. </p>
<p> Permission is hereby granted to use, copy, modify, and distribute this source code, or portions hereof, for any purpose, without fee, subject to the following restrictions: </p>
<p> 1. The origin of this source code must not be misrepresented; you must not claim that you wrote the original software. </p>
<p> 2. Altered versions must be plainly marked as such and must not be misrepresented as being the original source. </p>
<p> 3. This Copyright notice may not be removed or altered from any source or altered source distribution. </p>
<p> The Contributing Authors specifically permit, without fee, and encourage the use of this source code as a component to supporting the MNG and JNG file format in commercial products. If you use this source code in a product, acknowledgment would be highly appreciated. </p>
<h2>Remarks</h2>
<p> Parts of this software have been adapted from the libpng library. Although this library supports all features from the PNG specification (as MNG descends from it) it does not require the libpng library. It does require the zlib library and optionally the IJG JPEG library, and/or the &quot;little-cms&quot; library by Marti Maria Saguer (depending on the inclusion of support for JNG and Full-Color-Management respectively. </p>
<p> This library&#8217;s function is primarily to read and display MNG animations. It is not meant as a full-featured image-editing component! It does however offer creation and editing functionality at the chunk level. (future modifications may include some more support for creation and or editing) </p>
<h2>Index</h2>
