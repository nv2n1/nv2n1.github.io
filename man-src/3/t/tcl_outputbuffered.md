---
title: "tcl_outputbuffered(3)"
name: "tcl_outputbuffered"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_outputbuffered/"
description: "Tcl_OpenFileChannel, Tcl_OpenCommandChannel, Tcl_MakeFileChannel, Tcl_GetChannel, Tcl_GetChannelNames, Tcl_GetChannelNamesEx, Tcl_RegisterChannel, Tcl_UnregisterChannel, Tcl_DetachChannel, Tcl_IsSt..."
---

<p>Tcl_OpenFileChannel, Tcl_OpenCommandChannel, Tcl_MakeFileChannel, Tcl_GetChannel, Tcl_GetChannelNames, Tcl_GetChannelNamesEx, Tcl_RegisterChannel, Tcl_UnregisterChannel, Tcl_DetachChannel, Tcl_IsStandardChannel, Tcl_Close, Tcl_ReadChars, Tcl_Read, Tcl_GetsObj, Tcl_Gets, Tcl_WriteObj, Tcl_WriteChars, Tcl_Write, Tcl_Flush, Tcl_Seek, Tcl_Tell, Tcl_TruncateChannel, Tcl_GetChannelOption, Tcl_SetChannelOption, Tcl_Eof, Tcl_InputBlocked, Tcl_InputBuffered, Tcl_OutputBuffered, Tcl_Ungets, Tcl_ReadRaw, Tcl_WriteRaw &#8211; buffered I/O facilities using channels </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
Tcl_Channel
<code>Tcl_OpenFileChannel</code>(<i>interp, fileName, mode, permissions</i>)
Tcl_Channel
<code>Tcl_OpenCommandChannel</code>(<i>interp, argc, argv, flags</i>)
Tcl_Channel
<code>Tcl_MakeFileChannel</code>(<i>handle, readOrWrite</i>)
Tcl_Channel
<code>Tcl_GetChannel</code>(<i>interp, channelName, modePtr</i>)
int
<code>Tcl_GetChannelNames</code>(<i>interp</i>)
int
<code>Tcl_GetChannelNamesEx</code>(<i>interp, pattern</i>)
void
<code>Tcl_RegisterChannel</code>(<i>interp, channel</i>)
int
<code>Tcl_UnregisterChannel</code>(<i>interp, channel</i>)
int
<code>Tcl_DetachChannel</code>(<i>interp, channel</i>)
int
<code>Tcl_IsStandardChannel</code>(<i>channel</i>)
int
<code>Tcl_Close</code>(<i>interp, channel</i>)
int
<code>Tcl_ReadChars</code>(<i>channel, readObjPtr, charsToRead, appendFlag</i>)
int
<code>Tcl_Read</code>(<i>channel, readBuf, bytesToRead</i>)
int
<code>Tcl_GetsObj</code>(<i>channel, lineObjPtr</i>)
int
<code>Tcl_Gets</code>(<i>channel, lineRead</i>)
int
<code>Tcl_Ungets</code>(<i>channel, input, inputLen, addAtEnd</i>)
int
<code>Tcl_WriteObj</code>(<i>channel, writeObjPtr</i>)
int
<code>Tcl_WriteChars</code>(<i>channel, charBuf, bytesToWrite</i>)
int
<code>Tcl_Write</code>(<i>channel, byteBuf, bytesToWrite</i>)
int
<code>Tcl_ReadRaw</code>(<i>channel, readBuf, bytesToRead</i>)
int
<code>Tcl_WriteRaw</code>(<i>channel, byteBuf, bytesToWrite</i>)
int
<code>Tcl_Eof</code>(<i>channel</i>)
int
<code>Tcl_Flush</code>(<i>channel</i>)
int
<code>Tcl_InputBlocked</code>(<i>channel</i>)
int
<code>Tcl_InputBuffered</code>(<i>channel</i>)
int
<code>Tcl_OutputBuffered</code>(<i>channel</i>)
Tcl_WideInt
<code>Tcl_Seek</code>(<i>channel, offset, seekMode</i>)
Tcl_WideInt
<code>Tcl_Tell</code>(<i>channel</i>)
int
<code>Tcl_TruncateChannel</code>(<i>channel, length</i>)
int
<code>Tcl_GetChannelOption</code>(<i>interp, channel, optionName, optionValue</i>)
int
<code>Tcl_SetChannelOption</code>(<i>interp, channel, optionName, newValue</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Used for error reporting and to look up a channel registered in it.</p>
<dd>const char <i>*fileName</i> (in) The name of a local or network file.</p>
<dd>const char <i>*mode</i> (in) Specifies how the file is to be accessed. May have any of the values allowed for the <i>mode</i> argument to the Tcl <code>open</code> command.</p>
<dd>int <i>permissions</i> (in) POSIX-style permission flags such as 0644. If a new file is created, these permissions will be set on the created file.</p>
<dd>int <i>argc</i> (in) The number of elements in <i>argv</i>.</p>
<dd>const char <i>**argv</i> (in) Arguments for constructing a command pipeline. These values have the same meaning as the non-switch arguments to the Tcl <code>exec</code> command.</p>
<dd>int <i>flags</i> (in) Specifies the disposition of the stdio handles in pipeline: OR-ed combination of <code>TCL_STDIN</code>, <code>TCL_STDOUT</code>, <code>TCL_STDERR</code>, and <code>TCL_ENFORCE_MODE</code>. If <code>TCL_STDIN</code> is set, stdin for the first child in the pipe is the pipe channel, otherwise it is the same as the standard input of the invoking process; likewise for <code>TCL_STDOUT</code> and <code>TCL_STDERR</code>. If <code>TCL_ENFORCE_MODE</code> is not set, then the pipe can redirect stdio handles to override the stdio handles for which <code>TCL_STDIN</code>, <code>TCL_STDOUT</code> and <code>TCL_STDERR</code> have been set. If it is set, then such redirections cause an error.</p>
<dd>ClientData <i>handle</i> (in) Operating system specific handle for I/O to a file. For Unix this is a file descriptor, for Windows it is a HANDLE.</p>
<dd>int <i>readOrWrite</i> (in) OR-ed combination of <code>TCL_READABLE</code> and <code>TCL_WRITABLE</code> to indicate what operations are valid on <i>handle</i>.</p>
<dd>const char <i>*channelName</i> (in) The name of the channel.</p>
<dd>int <i>*modePtr</i> (out) Points at an integer variable that will receive an OR-ed combination of <code>TCL_READABLE</code> and <code>TCL_WRITABLE</code> denoting whether the channel is open for reading and writing.</p>
<dd>const char <i>*pattern</i> (in) The pattern to match on, passed to Tcl_StringMatch, or NULL.</p>
<dd>Tcl_Channel <i>channel</i> (in) A Tcl channel for input or output. Must have been the return value from a procedure such as <code>Tcl_OpenFileChannel</code>.</p>
<dd>Tcl_Obj <i>*readObjPtr</i> (in/out) A pointer to a Tcl Object in which to store the characters read from the channel.</p>
<dd>int <i>charsToRead</i> (in) The number of characters to read from the channel. If the channel&#8217;s encoding is <code>binary</code>, this is equivalent to the number of bytes to read from the channel.</p>
<dd>int <i>appendFlag</i> (in) If non-zero, data read from the channel will be appended to the object. Otherwise, the data will replace the existing contents of the object.</p>
<dd>char <i>*readBuf</i> (out) A buffer in which to store the bytes read from the channel.</p>
<dd>int <i>bytesToRead</i> (in) The number of bytes to read from the channel. The buffer <i>readBuf</i> must be large enough to hold this many bytes.</p>
<dd>Tcl_Obj <i>*lineObjPtr</i> (in/out) A pointer to a Tcl object in which to store the line read from the channel. The line read will be appended to the current value of the object.</p>
<dd>Tcl_DString <i>*lineRead</i> (in/out) A pointer to a Tcl dynamic string in which to store the line read from the channel. Must have been initialized by the caller. The line read will be appended to any data already in the dynamic string.</p>
<dd>const char <i>*input</i> (in) The input to add to a channel buffer.</p>
<dd>int <i>inputLen</i> (in) Length of the input</p>
<dd>int <i>addAtEnd</i> (in) Flag indicating whether the input should be added to the end or beginning of the channel buffer.</p>
<dd>Tcl_Obj <i>*writeObjPtr</i> (in) A pointer to a Tcl Object whose contents will be output to the channel.</p>
<dd>const char <i>*charBuf</i> (in) A buffer containing the characters to output to the channel.</p>
<dd>const char <i>*byteBuf</i> (in) A buffer containing the bytes to output to the channel.</p>
<dd>int <i>bytesToWrite</i> (in) The number of bytes to consume from <i>charBuf</i> or <i>byteBuf</i> and output to the channel.</p>
<dd>Tcl_WideInt <i>offset</i> (in) How far to move the access point in the channel at which the next input or output operation will be applied, measured in bytes from the position given by <i>seekMode</i>. May be either positive or negative.</p>
<dd>int <i>seekMode</i> (in) Relative to which point to seek; used with <i>offset</i> to calculate the new access point for the channel. Legal values are <code>SEEK_SET</code>, <code>SEEK_CUR</code>, and <code>SEEK_END</code>.</p>
<dd>Tcl_WideInt <i>length</i> (in) The (non-negative) length to truncate the channel the channel to.</p>
<dd>const char <i>*optionName</i> (in) The name of an option applicable to this channel, such as <code>-blocking</code>. May have any of the values accepted by the <code>fconfigure</code> command.</p>
<dd>Tcl_DString <i>*optionValue</i> (in) Where to store the value of an option or a list of all options and their values. Must have been initialized by the caller.</p>
<dd>const char <i>*newValue</i> (in) New value for the option given by <i>optionName</i>. </p>
</dl>
<h2>Description</h2>
<p>The Tcl channel mechanism provides a device-independent and platform-independent mechanism for performing buffered input and output operations on a variety of file, socket, and device types. The channel mechanism is extensible to new channel types, by providing a low-level channel driver for the new type; the channel driver interface is described in the manual entry for <code>Tcl_CreateChannel</code>. The channel mechanism provides a buffering scheme modeled after Unix&#8217;s standard I/O, and it also allows for nonblocking I/O on channels. </p>
<p> The procedures described in this manual entry comprise the C APIs of the generic layer of the channel architecture. For a description of the channel driver architecture and how to implement channel drivers for new types of channels, see the manual entry for <code>Tcl_CreateChannel</code>. </p>
<h2>Tcl_Openfilechannel</h2>
<p><code>Tcl_OpenFileChannel</code> opens a file specified by <i>fileName</i> and returns a channel handle that can be used to perform input and output on the file. This API is modeled after the <code>fopen</code> procedure of the Unix standard I/O library. The syntax and meaning of all arguments is similar to those given in the Tcl <code>open</code> command when opening a file. If an error occurs while opening the channel, <code>Tcl_OpenFileChannel</code> returns NULL and records a POSIX error code that can be retrieved with <code>Tcl_GetErrno</code>. In addition, if <i>interp</i> is non-NULL, <code>Tcl_OpenFileChannel</code> leaves an error message in <i>interp</i>&#8216;s result after any error. As of Tcl 8.4, the object-based API <code>Tcl_FSOpenFileChannel</code> should be used in preference to <code>Tcl_OpenFileChannel</code> wherever possible. </p>
<p> The newly created channel is not registered in the supplied interpreter; to register it, use <code>Tcl_RegisterChannel</code>, described below. If one of the standard channels, <code>stdin, stdout</code> or <code>stderr</code> was previously closed, the act of creating the new channel also assigns it as a replacement for the standard channel. </p>
<h2>Tcl_Opencommandchannel</h2>
<p><code>Tcl_OpenCommandChannel</code> provides a C-level interface to the functions of the <code>exec</code> and <code>open</code> commands. It creates a sequence of subprocesses specified by the <i>argv</i> and <i>argc</i> arguments and returns a channel that can be used to communicate with these subprocesses. The <i>flags</i> argument indicates what sort of communication will exist with the command pipeline. </p>
<p> If the <code>TCL_STDIN</code> flag is set then the standard input for the first subprocess will be tied to the channel: writing to the channel will provide input to the subprocess. If <code>TCL_STDIN</code> is not set, then standard input for the first subprocess will be the same as this application&#8217;s standard input. If <code>TCL_STDOUT</code> is set then standard output from the last subprocess can be read from the channel; otherwise it goes to this application&#8217;s standard output. If <code>TCL_STDERR</code> is set, standard error output for all subprocesses is returned to the channel and results in an error when the channel is closed; otherwise it goes to this application&#8217;s standard error. If <code>TCL_ENFORCE_MODE</code> is not set, then <i>argc</i> and <i>argv</i> can redirect the stdio handles to override <code>TCL_STDIN</code>, <code>TCL_STDOUT</code>, and <code>TCL_STDERR</code>; if it is set, then it is an error for argc and argv to override stdio channels for which <code>TCL_STDIN</code>, <code>TCL_STDOUT</code>, and <code>TCL_STDERR</code> have been set. </p>
<p> If an error occurs while opening the channel, <code>Tcl_OpenCommandChannel</code> returns NULL and records a POSIX error code that can be retrieved with <code>Tcl_GetErrno</code>. In addition, <code>Tcl_OpenCommandChannel</code> leaves an error message in the interpreter&#8217;s result if <i>interp</i> is not NULL. </p>
<p> The newly created channel is not registered in the supplied interpreter; to register it, use <code>Tcl_RegisterChannel</code>, described below. If one of the standard channels, <code>stdin, stdout</code> or <code>stderr</code> was previously closed, the act of creating the new channel also assigns it as a replacement for the standard channel. </p>
<h2>Tcl_Makefilechannel</h2>
<p><code>Tcl_MakeFileChannel</code> makes a <code>Tcl_Channel</code> from an existing, platform-specific, file handle. The newly created channel is not registered in the supplied interpreter; to register it, use <code>Tcl_RegisterChannel</code>, described below. If one of the standard channels, <code>stdin, stdout</code> or <code>stderr</code> was previously closed, the act of creating the new channel also assigns it as a replacement for the standard channel. </p>
<h2>Tcl_Getchannel</h2>
<p><code>Tcl_GetChannel</code> returns a channel given the <i>channelName</i> used to create it with <code>Tcl_CreateChannel</code> and a pointer to a Tcl interpreter in <i>interp</i>. If a channel by that name is not registered in that interpreter, the procedure returns NULL. If the <i>modePtr</i> argument is not NULL, it points at an integer variable that will receive an OR-ed combination of <code>TCL_READABLE</code> and <code>TCL_WRITABLE</code> describing whether the channel is open for reading and writing. </p>
<p> <code>Tcl_GetChannelNames</code> and <code>Tcl_GetChannelNamesEx</code> write the names of the registered channels to the interpreter&#8217;s result as a list object. <code>Tcl_GetChannelNamesEx</code> will filter these names according to the <i>pattern</i>. If <i>pattern</i> is NULL, then it will not do any filtering. The return value is <code>TCL_OK</code> if no errors occurred writing to the result, otherwise it is <code>TCL_ERROR</code>, and the error message is left in the interpreter&#8217;s result. </p>
<h2>Tcl_Registerchannel</h2>
<p><code>Tcl_RegisterChannel</code> adds a channel to the set of channels accessible in <i>interp</i>. After this call, Tcl programs executing in that interpreter can refer to the channel in input or output operations using the name given in the call to <code>Tcl_CreateChannel</code>. After this call, the channel becomes the property of the interpreter, and the caller should not call <code>Tcl_Close</code> for the channel; the channel will be closed automatically when it is unregistered from the interpreter. </p>
<p> Code executing outside of any Tcl interpreter can call <code>Tcl_RegisterChannel</code> with <i>interp</i> as NULL, to indicate that it wishes to hold a reference to this channel. Subsequently, the channel can be registered in a Tcl interpreter and it will only be closed when the matching number of calls to <code>Tcl_UnregisterChannel</code> have been made. This allows code executing outside of any interpreter to safely hold a reference to a channel that is also registered in a Tcl interpreter. </p>
<p> This procedure interacts with the code managing the standard channels. If no standard channels were initialized before the first call to <code>Tcl_RegisterChannel</code>, they will get initialized by that call. See <code>Tcl_StandardChannels</code> for a general treatise about standard channels and the behaviour of the Tcl library with regard to them. </p>
<h2>Tcl_Unregisterchannel</h2>
<p><code>Tcl_UnregisterChannel</code> removes a channel from the set of channels accessible in <i>interp</i>. After this call, Tcl programs will no longer be able to use the channel&#8217;s name to refer to the channel in that interpreter. If this operation removed the last registration of the channel in any interpreter, the channel is also closed and destroyed. </p>
<p> Code not associated with a Tcl interpreter can call <code>Tcl_UnregisterChannel</code> with <i>interp</i> as NULL, to indicate to Tcl that it no longer holds a reference to that channel. If this is the last reference to the channel, it will now be closed. <code>Tcl_UnregisterChannel</code> is very similar to <code>Tcl_DetachChannel</code> except that it will also close the channel if no further references to it exist. </p>
<h2>Tcl_Detachchannel</h2>
<p><code>Tcl_DetachChannel</code> removes a channel from the set of channels accessible in <i>interp</i>. After this call, Tcl programs will no longer be able to use the channel&#8217;s name to refer to the channel in that interpreter. Beyond that, this command has no further effect. It cannot be used on the standard channels (stdout, stderr, stdin), and will return <code>TCL_ERROR</code> if passed one of those channels. </p>
<p> Code not associated with a Tcl interpreter can call <code>Tcl_DetachChannel</code> with <i>interp</i> as NULL, to indicate to Tcl that it no longer holds a reference to that channel. If this is the last reference to the channel, unlike <code>Tcl_UnregisterChannel</code>, it will not be closed. </p>
<h2>Tcl_Isstandardchannel</h2>
<p><code>Tcl_IsStandardChannel</code> tests whether a channel is one of the three standard channels, stdin, stdout or stderr. If so, it returns 1, otherwise 0. </p>
<p> No attempt is made to check whether the given channel or the standard channels are initialized or otherwise valid. </p>
<h2>Tcl_Close</h2>
<p><code>Tcl_Close</code> destroys the channel <i>channel</i>, which must denote a currently open channel. The channel should not be registered in any interpreter when <code>Tcl_Close</code> is called. Buffered output is flushed to the channel&#8217;s output device prior to destroying the channel, and any buffered input is discarded. If this is a blocking channel, the call does not return until all buffered data is successfully sent to the channel&#8217;s output device. If this is a nonblocking channel and there is buffered output that cannot be written without blocking, the call returns immediately; output is flushed in the background and the channel will be closed once all of the buffered data has been output. In this case errors during flushing are not reported. </p>
<p> If the channel was closed successfully, <code>Tcl_Close</code> returns <code>TCL_OK</code>. If an error occurs, <code>Tcl_Close</code> returns <code>TCL_ERROR</code> and records a POSIX error code that can be retrieved with <code>Tcl_GetErrno</code>. If the channel is being closed synchronously and an error occurs during closing of the channel and <i>interp</i> is not NULL, an error message is left in the interpreter&#8217;s result. </p>
<p> Note: it is not safe to call <code>Tcl_Close</code> on a channel that has been registered using <code>Tcl_RegisterChannel</code>; see the documentation for <code>Tcl_RegisterChannel</code>, above, for details. If the channel has ever been given as the <code>chan</code> argument in a call to <code>Tcl_RegisterChannel</code>, you should instead use <code>Tcl_UnregisterChannel</code>, which will internally call <code>Tcl_Close</code> when all calls to <code>Tcl_RegisterChannel</code> have been matched by corresponding calls to <code>Tcl_UnregisterChannel</code>. </p>
<h2>Tcl_Readchars And Tcl_Read</h2>
<p><code>Tcl_ReadChars</code> consumes bytes from <i>channel</i>, converting the bytes to UTF-8 based on the channel&#8217;s encoding and storing the produced data in <i>readObjPtr</i>&#8216;s string representation. The return value of <code>Tcl_ReadChars</code> is the number of characters, up to <i>charsToRead</i>, that were stored in <i>readObjPtr</i>. If an error occurs while reading, the return value is -1 and <code>Tcl_ReadChars</code> records a POSIX error code that can be retrieved with <code>Tcl_GetErrno</code>. </p>
<p> Setting <i>charsToRead</i> to <code>-1</code> will cause the command to read all characters currently available (non-blocking) or everything until eof (blocking mode). </p>
<p> The return value may be smaller than the value to read, indicating that less data than requested was available. This is called a <i>short read</i>. In blocking mode, this can only happen on an end-of-file. In nonblocking mode, a short read can also occur if there is not enough input currently available: <code>Tcl_ReadChars</code> returns a short count rather than waiting for more data. </p>
<p> If the channel is in blocking mode, a return value of zero indicates an end-of-file condition. If the channel is in nonblocking mode, a return value of zero indicates either that no input is currently available or an end-of-file condition. Use <code>Tcl_Eof</code> and <code>Tcl_InputBlocked</code> to tell which of these conditions actually occurred. </p>
<p> <code>Tcl_ReadChars</code> translates the various end-of-line representations into the canonical <code>
</code> internal representation according to the current end-of-line recognition mode. End-of-line recognition and the various platform-specific modes are described in the manual entry for the Tcl <code>fconfigure</code> command. </p>
<p> As a performance optimization, when reading from a channel with the encoding <code>binary</code>, the bytes are not converted to UTF-8 as they are read. Instead, they are stored in <i>readObjPtr</i>&#8216;s internal representation as a byte-array object. The string representation of this object will only be constructed if it is needed (e.g., because of a call to <code>Tcl_GetStringFromObj</code>). In this way, byte-oriented data can be read from a channel, manipulated by calling <code>Tcl_GetByteArrayFromObj</code> and related functions, and then written to a channel without the expense of ever converting to or from UTF-8. </p>
<p> <code>Tcl_Read</code> is similar to <code>Tcl_ReadChars</code>, except that it does not do encoding conversions, regardless of the channel&#8217;s encoding. It is deprecated and exists for backwards compatibility with non-internationalized Tcl extensions. It consumes bytes from <i>channel</i> and stores them in <i>readBuf</i>, performing end-of-line translations on the way. The return value of <code>Tcl_Read</code> is the number of bytes, up to <i>bytesToRead</i>, written in <i>readBuf</i>. The buffer produced by <code>Tcl_Read</code> is not null-terminated. Its contents are valid from the zeroth position up to and excluding the position indicated by the return value. </p>
<p> <code>Tcl_ReadRaw</code> is the same as <code>Tcl_Read</code> but does not compensate for stacking. While <code>Tcl_Read</code> (and the other functions in the API) always get their data from the topmost channel in the stack the supplied channel is part of, <code>Tcl_ReadRaw</code> does not. Thus this function is <code>only</code> usable for transformational channel drivers, i.e. drivers used in the middle of a stack of channels, to move data from the channel below into the transformation. </p>
<h2>Tcl_Getsobj And Tcl_Gets</h2>
<p><code>Tcl_GetsObj</code> consumes bytes from <i>channel</i>, converting the bytes to UTF-8 based on the channel&#8217;s encoding, until a full line of input has been seen. If the channel&#8217;s encoding is <code>binary</code>, each byte read from the channel is treated as an individual Unicode character. All of the characters of the line except for the terminating end-of-line character(s) are appended to <i>lineObjPtr</i>&#8216;s string representation. The end-of-line character(s) are read and discarded. </p>
<p> If a line was successfully read, the return value is greater than or equal to zero and indicates the number of bytes stored in <i>lineObjPtr</i>. If an error occurs, <code>Tcl_GetsObj</code> returns -1 and records a POSIX error code that can be retrieved with <code>Tcl_GetErrno</code>. <code>Tcl_GetsObj</code> also returns -1 if the end of the file is reached; the <code>Tcl_Eof</code> procedure can be used to distinguish an error from an end-of-file condition. </p>
<p> If the channel is in nonblocking mode, the return value can also be -1 if no data was available or the data that was available did not contain an end-of-line character. When -1 is returned, the <code>Tcl_InputBlocked</code> procedure may be invoked to determine if the channel is blocked because of input unavailability. </p>
<p> <code>Tcl_Gets</code> is the same as <code>Tcl_GetsObj</code> except the resulting characters are appended to the dynamic string given by <i>lineRead</i> rather than a Tcl object. </p>
<h2>Tcl_Ungets</h2>
<p><code>Tcl_Ungets</code> is used to add data to the input queue of a channel, at either the head or tail of the queue. The pointer <i>input</i> points to the data that is to be added. The length of the input to add is given by <i>inputLen</i>. A non-zero value of <i>addAtEnd</i> indicates that the data is to be added at the end of queue; otherwise it will be added at the head of the queue. If <i>channel</i> has a &#8220;sticky&#8221; EOF set, no data will be added to the input queue. <code>Tcl_Ungets</code> returns <i>inputLen</i> or -1 if an error occurs. </p>
<h2>Tcl_Writechars, Tcl_Writeobj, And Tcl_Write</h2>
<p><code>Tcl_WriteChars</code> accepts <i>bytesToWrite</i> bytes of character data at <i>charBuf</i>. The UTF-8 characters in the buffer are converted to the channel&#8217;s encoding and queued for output to <i>channel</i>. If <i>bytesToWrite</i> is negative, <code>Tcl_WriteChars</code> expects <i>charBuf</i> to be null-terminated and it outputs everything up to the null. </p>
<p> Data queued for output may not appear on the output device immediately, due to internal buffering. If the data should appear immediately, call <code>Tcl_Flush</code> after the call to <code>Tcl_WriteChars</code>, or set the <code>-buffering</code> option on the channel to <code>none</code>. If you wish the data to appear as soon as a complete line is accepted for output, set the <code>-buffering</code> option on the channel to <code>line</code> mode. </p>
<p> The return value of <code>Tcl_WriteChars</code> is a count of how many bytes were accepted for output to the channel. This is either greater than zero to indicate success or -1 to indicate that an error occurred. If an error occurs, <code>Tcl_WriteChars</code> records a POSIX error code that may be retrieved with <code>Tcl_GetErrno</code>. </p>
<p> Newline characters in the output data are translated to platform-specific end-of-line sequences according to the <code>-translation</code> option for the channel. This is done even if the channel has no encoding. </p>
<p> <code>Tcl_WriteObj</code> is similar to <code>Tcl_WriteChars</code> except it accepts a Tcl object whose contents will be output to the channel. The UTF-8 characters in <i>writeObjPtr</i>&#8216;s string representation are converted to the channel&#8217;s encoding and queued for output to <i>channel</i>. As a performance optimization, when writing to a channel with the encoding <code>binary</code>, UTF-8 characters are not converted as they are written. Instead, the bytes in <i>writeObjPtr</i>&#8216;s internal representation as a byte-array object are written to the channel. The byte-array representation of the object will be constructed if it is needed. In this way, byte-oriented data can be read from a channel, manipulated by calling <code>Tcl_GetByteArrayFromObj</code> and related functions, and then written to a channel without the expense of ever converting to or from UTF-8. </p>
<p> <code>Tcl_Write</code> is similar to <code>Tcl_WriteChars</code> except that it does not do encoding conversions, regardless of the channel&#8217;s encoding. It is deprecated and exists for backwards compatibility with non-internationalized Tcl extensions. It accepts <i>bytesToWrite</i> bytes of data at <i>byteBuf</i> and queues them for output to <i>channel</i>. If <i>bytesToWrite</i> is negative, <code>Tcl_Write</code> expects <i>byteBuf</i> to be null-terminated and it outputs everything up to the null. </p>
<p> <code>Tcl_WriteRaw</code> is the same as <code>Tcl_Write</code> but does not compensate for stacking. While <code>Tcl_Write</code> (and the other functions in the API) always feed their input to the topmost channel in the stack the supplied channel is part of, <code>Tcl_WriteRaw</code> does not. Thus this function is <code>only</code> usable for transformational channel drivers, i.e. drivers used in the middle of a stack of channels, to move data from the transformation into the channel below it. </p>
<h2>Tcl_Flush</h2>
<p><code>Tcl_Flush</code> causes all of the buffered output data for <i>channel</i> to be written to its underlying file or device as soon as possible. If the channel is in blocking mode, the call does not return until all the buffered data has been sent to the channel or some error occurred. The call returns immediately if the channel is nonblocking; it starts a background flush that will write the buffered data to the channel eventually, as fast as the channel is able to absorb it. </p>
<p> The return value is normally <code>TCL_OK</code>. If an error occurs, <code>Tcl_Flush</code> returns <code>TCL_ERROR</code> and records a POSIX error code that can be retrieved with <code>Tcl_GetErrno</code>. </p>
<h2>Tcl_Seek</h2>
<p><code>Tcl_Seek</code> moves the access point in <i>channel</i> where subsequent data will be read or written. Buffered output is flushed to the channel and buffered input is discarded, prior to the seek operation. </p>
<p> <code>Tcl_Seek</code> normally returns the new access point. If an error occurs, <code>Tcl_Seek</code> returns -1 and records a POSIX error code that can be retrieved with <code>Tcl_GetErrno</code>. After an error, the access point may or may not have been moved. </p>
<h2>Tcl_Tell</h2>
<p><code>Tcl_Tell</code> returns the current access point for a channel. The returned value is -1 if the channel does not support seeking. </p>
<h2>Tcl_Truncatechannel</h2>
<p><code>Tcl_TruncateChannel</code> truncates the file underlying <i>channel</i> to a given <i>length</i> of bytes. It returns <code>TCL_OK</code> if the operation succeeded, and <code>TCL_ERROR</code> otherwise. </p>
<h2>Tcl_Getchanneloption</h2>
<p><code>Tcl_GetChannelOption</code> retrieves, in <i>optionValue</i>, the value of one of the options currently in effect for a channel, or a list of all options and their values. The <i>channel</i> argument identifies the channel for which to query an option or retrieve all options and their values. If <i>optionName</i> is not NULL, it is the name of the option to query; the option&#8217;s value is copied to the Tcl dynamic string denoted by <i>optionValue</i>. If <i>optionName</i> is NULL, the function stores an alternating list of option names and their values in <i>optionValue</i>, using a series of calls to <code>Tcl_DStringAppendElement</code>. The various preexisting options and their possible values are described in the manual entry for the Tcl <code>fconfigure</code> command. Other options can be added by each channel type. These channel type specific options are described in the manual entry for the Tcl command that creates a channel of that type; for example, the additional options for TCP based channels are described in the manual entry for the Tcl <code>socket</code> command. The procedure normally returns <code>TCL_OK</code>. If an error occurs, it returns <code>TCL_ERROR</code> and calls <code>Tcl_SetErrno</code> to store an appropriate POSIX error code. </p>
<h2>Tcl_Setchanneloption</h2>
<p><code>Tcl_SetChannelOption</code> sets a new value <i>newValue</i> for an option <i>optionName</i> on <i>channel</i>. The procedure normally returns <code>TCL_OK</code>. If an error occurs, it returns <code>TCL_ERROR</code>; in addition, if <i>interp</i> is non-NULL, <code>Tcl_SetChannelOption</code> leaves an error message in the interpreter&#8217;s result. </p>
<h2>Tcl_Eof</h2>
<p><code>Tcl_Eof</code> returns a nonzero value if <i>channel</i> encountered an end of file during the last input operation. </p>
<h2>Tcl_Inputblocked</h2>
<p><code>Tcl_InputBlocked</code> returns a nonzero value if <i>channel</i> is in nonblocking mode and the last input operation returned less data than requested because there was insufficient data available. The call always returns zero if the channel is in blocking mode. </p>
<h2>Tcl_Inputbuffered</h2>
<p><code>Tcl_InputBuffered</code> returns the number of bytes of input currently buffered in the internal buffers for a channel. If the channel is not open for reading, this function always returns zero. </p>
<h2>Tcl_Outputbuffered</h2>
<p><code>Tcl_OutputBuffered</code> returns the number of bytes of output currently buffered in the internal buffers for a channel. If the channel is not open for writing, this function always returns zero. </p>
<h2>Platform Issues</h2>
<p>The handles returned from <code>Tcl_GetChannelHandle</code> depend on the platform and the channel type. On Unix platforms, the handle is always a Unix file descriptor as returned from the <code>open</code> system call. On Windows platforms, the handle is a file <code>HANDLE</code> when the channel was created with <code>Tcl_OpenFileChannel</code>, <code>Tcl_OpenCommandChannel</code>, or <code>Tcl_MakeFileChannel</code>. Other channel types may return a different type of handle on Windows platforms. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-dstring/">DString</a>(3), <a href="/docs/linux/man/n-fconfigure/">fconfigure</a>(n), <a href="/docs/linux/man/n-filename/">filename</a>(n), <a href="/docs/linux/man/3-fopen/">fopen</a>(3), <a href="/docs/linux/man/3-tcl_createchannel/">Tcl_CreateChannel</a>(3) </p>
<h2>Keywords</h2>
<p>access point, blocking, buffered I/O, channel, channel driver, end of file, flush, input, nonblocking, output, read, seek, write</p>
