---
title: "tcl_channelcloseproc(3)"
name: "tcl_channelcloseproc"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_channelcloseproc/"
description: "Tcl_CreateChannel, Tcl_GetChannelInstanceData, Tcl_GetChannelType, Tcl_GetChannelName, Tcl_GetChannelHandle, Tcl_GetChannelMode, Tcl_GetChannelBufferSize, Tcl_SetChannelBufferSize, Tcl_NotifyChanne..."
---

<p>Tcl_CreateChannel, Tcl_GetChannelInstanceData, Tcl_GetChannelType, Tcl_GetChannelName, Tcl_GetChannelHandle, Tcl_GetChannelMode, Tcl_GetChannelBufferSize, Tcl_SetChannelBufferSize, Tcl_NotifyChannel, Tcl_BadChannelOption, Tcl_ChannelName, Tcl_ChannelVersion, Tcl_ChannelBlockModeProc, Tcl_ChannelCloseProc, Tcl_ChannelClose2Proc, Tcl_ChannelInputProc, Tcl_ChannelOutputProc, Tcl_ChannelSeekProc, Tcl_ChannelWideSeekProc, Tcl_ChannelTruncateProc, Tcl_ChannelSetOptionProc, Tcl_ChannelGetOptionProc, Tcl_ChannelWatchProc, Tcl_ChannelGetHandleProc, Tcl_ChannelFlushProc, Tcl_ChannelHandlerProc, Tcl_ChannelThreadActionProc, Tcl_IsChannelShared, Tcl_IsChannelRegistered, Tcl_CutChannel, Tcl_SpliceChannel, Tcl_IsChannelExisting, Tcl_ClearChannelHandlers, Tcl_GetChannelThread, Tcl_ChannelBuffered &#8211; procedures for creating and manipulating channels </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
Tcl_Channel
<code>Tcl_CreateChannel</code>(<i>typePtr, channelName, instanceData, mask</i>)
ClientData
<code>Tcl_GetChannelInstanceData</code>(<i>channel</i>)
Tcl_ChannelType *
<code>Tcl_GetChannelType</code>(<i>channel</i>)
const char *
<code>Tcl_GetChannelName</code>(<i>channel</i>)
int
<code>Tcl_GetChannelHandle</code>(<i>channel, direction, handlePtr</i>)
Tcl_ThreadId
<code>Tcl_GetChannelThread</code>(<i>channel</i>)
int
<code>Tcl_GetChannelMode</code>(<i>channel</i>)
int
<code>Tcl_GetChannelBufferSize</code>(<i>channel</i>)
<code>Tcl_SetChannelBufferSize</code>(<i>channel, size</i>)
<code>Tcl_NotifyChannel</code>(<i>channel, mask</i>)
int
<code>Tcl_BadChannelOption</code>(<i>interp, optionName, optionList</i>)
int
<code>Tcl_IsChannelShared</code>(<i>channel</i>)
int
<code>Tcl_IsChannelRegistered</code>(<i>interp, channel</i>)
int
<code>Tcl_IsChannelExisting</code>(<i>channelName</i>)
void
<code>Tcl_CutChannel</code>(<i>channel</i>)
void
<code>Tcl_SpliceChannel</code>(<i>channel</i>)
void
<code>Tcl_ClearChannelHandlers</code>(<i>channel</i>)
int
<code>Tcl_ChannelBuffered</code>(<i>channel</i>)
const char *
<code>Tcl_ChannelName</code>(<i>typePtr</i>)
Tcl_ChannelTypeVersion
<code>Tcl_ChannelVersion</code>(<i>typePtr</i>)
Tcl_DriverBlockModeProc *
<code>Tcl_ChannelBlockModeProc</code>(<i>typePtr</i>)
Tcl_DriverCloseProc *
<code>Tcl_ChannelCloseProc</code>(<i>typePtr</i>)
Tcl_DriverClose2Proc *
<code>Tcl_ChannelClose2Proc</code>(<i>typePtr</i>)
Tcl_DriverInputProc *
<code>Tcl_ChannelInputProc</code>(<i>typePtr</i>)
Tcl_DriverOutputProc *
<code>Tcl_ChannelOutputProc</code>(<i>typePtr</i>)
Tcl_DriverSeekProc *
<code>Tcl_ChannelSeekProc</code>(<i>typePtr</i>)
Tcl_DriverWideSeekProc *
<code>Tcl_ChannelWideSeekProc</code>(<i>typePtr</i>)
Tcl_DriverThreadActionProc *
<code>Tcl_ChannelThreadActionProc</code>(<i>typePtr</i>)
Tcl_DriverTruncateProc *
<code>Tcl_ChannelTruncateProc</code>(<i>typePtr</i>)
Tcl_DriverSetOptionProc *
<code>Tcl_ChannelSetOptionProc</code>(<i>typePtr</i>)
Tcl_DriverGetOptionProc *
<code>Tcl_ChannelGetOptionProc</code>(<i>typePtr</i>)
Tcl_DriverWatchProc *
<code>Tcl_ChannelWatchProc</code>(<i>typePtr</i>)
Tcl_DriverGetHandleProc *
<code>Tcl_ChannelGetHandleProc</code>(<i>typePtr</i>)
Tcl_DriverFlushProc *
<code>Tcl_ChannelFlushProc</code>(<i>typePtr</i>)
Tcl_DriverHandlerProc *
<code>Tcl_ChannelHandlerProc</code>(<i>typePtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>const Tcl_ChannelType <i>*typePtr</i> (in) Points to a structure containing the addresses of procedures that can be called to perform I/O and other functions on the channel.</p>
<dd>const char <i>*channelName</i> (in) The name of this channel, such as <code>file3</code>; must not be in use by any other channel. Can be NULL, in which case the channel is created without a name.</p>
<dd>ClientData <i>instanceData</i> (in) Arbitrary one-word value to be associated with this channel. This value is passed to procedures in <i>typePtr</i> when they are invoked.</p>
<dd>int <i>mask</i> (in) OR-ed combination of <code>TCL_READABLE</code> and <code>TCL_WRITABLE</code> to indicate whether a channel is readable and writable.</p>
<dd>Tcl_Channel <i>channel</i> (in) The channel to operate on.</p>
<dd>int <i>direction</i> (in) <code>TCL_READABLE</code> means the input handle is wanted; <code>TCL_WRITABLE</code> means the output handle is wanted.</p>
<dd>ClientData <i>*handlePtr</i> (out) Points to the location where the desired OS-specific handle should be stored.</p>
<dd>int <i>size</i> (in) The size, in bytes, of buffers to allocate in this channel.</p>
<dd>int <i>mask</i> (in) An OR-ed combination of <code>TCL_READABLE</code>, <code>TCL_WRITABLE</code> and <code>TCL_EXCEPTION</code> that indicates events that have occurred on this channel.</p>
<dd>Tcl_Interp <i>*interp</i> (in) Current interpreter. (can be NULL)</p>
<dd>const char <i>*optionName</i> (in) Name of the invalid option.</p>
<dd>const char <i>*optionList</i> (in) Specific options list (space separated words, without &#8220;-&#8221;) to append to the standard generic options list. Can be NULL for generic options error message only. </p>
</dl>
<h2>Description</h2>
<p>Tcl uses a two-layered channel architecture. It provides a generic upper layer to enable C and Tcl programs to perform input and output using the same APIs for a variety of files, devices, sockets etc. The generic C APIs are described in the manual entry for <code>Tcl_OpenFileChannel</code>. </p>
<p> The lower layer provides type-specific channel drivers for each type of device supported on each platform. This manual entry describes the C APIs used to communicate between the generic layer and the type-specific channel drivers. It also explains how new types of channels can be added by providing new channel drivers. </p>
<p> Channel drivers consist of a number of components: First, each channel driver provides a <code>Tcl_ChannelType</code> structure containing pointers to functions implementing the various operations used by the generic layer to communicate with the channel driver. The <code>Tcl_ChannelType</code> structure and the functions referenced by it are described in the section <code>TCL_CHANNELTYPE</code>, below. </p>
<p> Second, channel drivers usually provide a Tcl command to create instances of that type of channel. For example, the Tcl <code>open</code> command creates channels that use the file and command channel drivers, and the Tcl <code>socket</code> command creates channels that use TCP sockets for network communication. </p>
<p> Third, a channel driver optionally provides a C function to open channel instances of that type. For example, <code>Tcl_OpenFileChannel</code> opens a channel that uses the file channel driver, and <code>Tcl_OpenTcpClient</code> opens a channel that uses the TCP network protocol. These creation functions typically use <code>Tcl_CreateChannel</code> internally to open the channel. </p>
<p> To add a new type of channel you must implement a C API or a Tcl command that opens a channel by invoking <code>Tcl_CreateChannel</code>. When your driver calls <code>Tcl_CreateChannel</code> it passes in a <code>Tcl_ChannelType</code> structure describing the driver&#8217;s I/O procedures. The generic layer will then invoke the functions referenced in that structure to perform operations on the channel. </p>
<p> <code>Tcl_CreateChannel</code> opens a new channel and associates the supplied <i>typePtr</i> and <i>instanceData</i> with it. The channel is opened in the mode indicated by <i>mask</i>. For a discussion of channel drivers, their operations and the <code>Tcl_ChannelType</code> structure, see the section <code>TCL_CHANNELTYPE</code>, below. </p>
<p> <code>Tcl_CreateChannel</code> interacts with the code managing the standard channels. Once a standard channel was initialized either through a call to <code>Tcl_GetStdChannel</code> or a call to <code>Tcl_SetStdChannel</code> closing this standard channel will cause the next call to <code>Tcl_CreateChannel</code> to make the new channel the new standard channel too. See <code>Tcl_StandardChannels</code> for a general treatise about standard channels and the behaviour of the Tcl library with regard to them. </p>
<p> <code>Tcl_GetChannelInstanceData</code> returns the instance data associated with the channel in <i>channel</i>. This is the same as the <i>instanceData</i> argument in the call to <code>Tcl_CreateChannel</code> that created this channel. </p>
<p> <code>Tcl_GetChannelType</code> returns a pointer to the <code>Tcl_ChannelType</code> structure used by the channel in the <i>channel</i> argument. This is the same as the <i>typePtr</i> argument in the call to <code>Tcl_CreateChannel</code> that created this channel. </p>
<p> <code>Tcl_GetChannelName</code> returns a string containing the name associated with the channel, or NULL if the <i>channelName</i> argument to <code>Tcl_CreateChannel</code> was NULL. </p>
<p> <code>Tcl_GetChannelHandle</code> places the OS-specific device handle associated with <i>channel</i> for the given <i>direction</i> in the location specified by <i>handlePtr</i> and returns <code>TCL_OK</code>. If the channel does not have a device handle for the specified direction, then <code>TCL_ERROR</code> is returned instead. Different channel drivers will return different types of handle. Refer to the manual entries for each driver to determine what type of handle is returned. </p>
<p> <code>Tcl_GetChannelThread</code> returns the id of the thread currently managing the specified <i>channel</i>. This allows channel drivers to send their file events to the correct event queue even for a multi-threaded core. </p>
<p> <code>Tcl_GetChannelMode</code> returns an OR-ed combination of <code>TCL_READABLE</code> and <code>TCL_WRITABLE</code>, indicating whether the channel is open for input and output. </p>
<p> <code>Tcl_GetChannelBufferSize</code> returns the size, in bytes, of buffers allocated to store input or output in <i>channel</i>. If the value was not set by a previous call to <code>Tcl_SetChannelBufferSize</code>, described below, then the default value of 4096 is returned. </p>
<p> <code>Tcl_SetChannelBufferSize</code> sets the size, in bytes, of buffers that will be allocated in subsequent operations on the channel to store input or output. The <i>size</i> argument should be between ten and one million, allowing buffers of ten bytes to one million bytes. If <i>size</i> is outside this range, <code>Tcl_SetChannelBufferSize</code> sets the buffer size to 4096. </p>
<p> <code>Tcl_NotifyChannel</code> is called by a channel driver to indicate to the generic layer that the events specified by <i>mask</i> have occurred on the channel. Channel drivers are responsible for invoking this function whenever the channel handlers need to be called for the channel. See <code>WATCHPROC</code> below for more details. </p>
<p> <code>Tcl_BadChannelOption</code> is called from driver specific <i>setOptionProc</i> or <i>getOptionProc</i> to generate a complete error message. </p>
<p> <code>Tcl_ChannelBuffered</code> returns the number of bytes of input currently buffered in the internal buffer (push back area) of the channel itself. It does not report about the data in the overall buffers for the stack of channels the supplied channel is part of. </p>
<p> <code>Tcl_IsChannelShared</code> checks the refcount of the specified <i>channel</i> and returns whether the <i>channel</i> was shared among multiple interpreters (result == 1) or not (result == 0). </p>
<p> <code>Tcl_IsChannelRegistered</code> checks whether the specified <i>channel</i> is registered in the given <i>interp</i>reter (result == 1) or not (result == 0). </p>
<p> <code>Tcl_IsChannelExisting</code> checks whether a channel with the specified name is registered in the (thread)-global list of all channels (result == 1) or not (result == 0). </p>
<p> <code>Tcl_CutChannel</code> removes the specified <i>channel</i> from the (thread)global list of all channels (of the current thread). Application to a channel still registered in some interpreter is not allowed. Also notifies the driver if the <code>Tcl_ChannelType</code> version is <code>TCL_CHANNEL_VERSION_4</code> (or higher), and <code>Tcl_DriverThreadActionProc</code> is defined for it. </p>
<p> <code>Tcl_SpliceChannel</code> adds the specified <i>channel</i> to the (thread)global list of all channels (of the current thread). Application to a channel registered in some interpreter is not allowed. Also notifies the driver if the <code>Tcl_ChannelType</code> version is <code>TCL_CHANNEL_VERSION_4</code> (or higher), and <code>Tcl_DriverThreadActionProc</code> is defined for it. </p>
<p> <code>Tcl_ClearChannelHandlers</code> removes all channel handlers and event scripts associated with the specified <i>channel</i>, thus shutting down all event processing for this channel.</p>
<h2>Tcl_Channeltype</h2>
<p>A channel driver provides a <code>Tcl_ChannelType</code> structure that contains pointers to functions that implement the various operations on a channel; these operations are invoked as needed by the generic layer. The structure was versioned starting in Tcl 8.3.2/8.4 to correct a problem with stacked channel drivers. See the <code>OLD CHANNEL TYPES</code> section below for details about the old structure. </p>
<p> The <code>Tcl_ChannelType</code> structure contains the following fields:</p>
<dl COMPACT>
<dd>
<pre>typedef struct Tcl_ChannelType {
 char *<i>typeName</i>;
 Tcl_ChannelTypeVersion <i>version</i>;
 Tcl_DriverCloseProc *<i>closeProc</i>;
 Tcl_DriverInputProc *<i>inputProc</i>;
 Tcl_DriverOutputProc *<i>outputProc</i>;
 Tcl_DriverSeekProc *<i>seekProc</i>;
 Tcl_DriverSetOptionProc *<i>setOptionProc</i>;
 Tcl_DriverGetOptionProc *<i>getOptionProc</i>;
 Tcl_DriverWatchProc *<i>watchProc</i>;
 Tcl_DriverGetHandleProc *<i>getHandleProc</i>;
 Tcl_DriverClose2Proc *<i>close2Proc</i>;
 Tcl_DriverBlockModeProc *<i>blockModeProc</i>;
 Tcl_DriverFlushProc *<i>flushProc</i>;
 Tcl_DriverHandlerProc *<i>handlerProc</i>;
 Tcl_DriverWideSeekProc *<i>wideSeekProc</i>;
 Tcl_DriverThreadActionProc *<i>threadActionProc</i>;
 Tcl_DriverTruncateProc *<i>truncateProc</i>;
} Tcl_ChannelType;</pre>
</dl>
<p> It is not necessary to provide implementations for all channel operations. Those which are not necessary may be set to NULL in the struct: <i>blockModeProc</i>, <i>seekProc</i>, <i>setOptionProc</i>, <i>getOptionProc</i>, and <i>close2Proc</i>, in addition to <i>flushProc</i>, <i>handlerProc</i>, <i>threadActionProc</i>, and <i>truncateProc</i>. Other functions that cannot be implemented in a meaningful way should return <code>EINVAL</code> when called, to indicate that the operations they represent are not available. Also note that <i>wideSeekProc</i> can be NULL if <i>seekProc</i> is. </p>
<p> The user should only use the above structure for <code>Tcl_ChannelType</code> instantiation. When referencing fields in a <code>Tcl_ChannelType</code> structure, the following functions should be used to obtain the values: <code>Tcl_ChannelName</code>, <code>Tcl_ChannelVersion</code>, <code>Tcl_ChannelBlockModeProc</code>, <code>Tcl_ChannelCloseProc</code>, <code>Tcl_ChannelClose2Proc</code>, <code>Tcl_ChannelInputProc</code>, <code>Tcl_ChannelOutputProc</code>, <code>Tcl_ChannelSeekProc</code>, <code>Tcl_ChannelWideSeekProc</code>, <code>Tcl_ChannelThreadActionProc</code>, <code>Tcl_ChannelTruncateProc</code>, <code>Tcl_ChannelSetOptionProc</code>, <code>Tcl_ChannelGetOptionProc</code>, <code>Tcl_ChannelWatchProc</code>, <code>Tcl_ChannelGetHandleProc</code>, <code>Tcl_ChannelFlushProc</code>, or <code>Tcl_ChannelHandlerProc</code>. </p>
<p> The change to the structures was made in such a way that standard channel types are binary compatible. However, channel types that use stacked channels (i.e. TLS, Trf) have new versions to correspond to the above change since the previous code for stacked channels had problems.</p>
<h3>Typename</h3>
<p>The <i>typeName</i> field contains a null-terminated string that identifies the type of the device implemented by this driver, e.g. <code>file</code> or <code>socket</code>. </p>
<p> This value can be retrieved with <code>Tcl_ChannelName</code>, which returns a pointer to the string.</p>
<h3>Version</h3>
<p>The <i>version</i> field should be set to the version of the structure that you require. <code>TCL_CHANNEL_VERSION_2</code> is the minimum recommended. <code>TCL_CHANNEL_VERSION_3</code> must be set to specify the <i>wideSeekProc</i> member. <code>TCL_CHANNEL_VERSION_4</code> must be set to specify the <i>threadActionProc</i> member (includes <i>wideSeekProc</i>). <code>TCL_CHANNEL_VERSION_5</code> must be set to specify the <i>truncateProc</i> members (includes <i>wideSeekProc</i> and <i>threadActionProc</i>). If it is not set to any of these, then this <code>Tcl_ChannelType</code> is assumed to have the original structure. See <code>OLD CHANNEL TYPES</code> for more details. While Tcl will recognize and function with either structures, stacked channels must be of at least <code>TCL_CHANNEL_VERSION_2</code> to function correctly. </p>
<p> This value can be retrieved with <code>Tcl_ChannelVersion</code>, which returns one of <code>TCL_CHANNEL_VERSION_5</code>, <code>TCL_CHANNEL_VERSION_4</code>, <code>TCL_CHANNEL_VERSION_3</code>, <code>TCL_CHANNEL_VERSION_2</code> or <code>TCL_CHANNEL_VERSION_1</code>.</p>
<h3>Blockmodeproc</h3>
<p>The <i>blockModeProc</i> field contains the address of a function called by the generic layer to set blocking and nonblocking mode on the device. <i>BlockModeProc</i> should match the following prototype: </p>
<dl COMPACT>
<dd>
<pre>typedef int Tcl_DriverBlockModeProc(
 ClientData <i>instanceData</i>,
 int <i>mode</i>);</pre>
</dl>
<p> The <i>instanceData</i> is the same as the value passed to <code>Tcl_CreateChannel</code> when this channel was created. The <i>mode</i> argument is either <code>TCL_MODE_BLOCKING</code> or <code>TCL_MODE_NONBLOCKING</code> to set the device into blocking or nonblocking mode. The function should return zero if the operation was successful, or a nonzero POSIX error code if the operation failed. </p>
<p> If the operation is successful, the function can modify the supplied <i>instanceData</i> to record that the channel entered blocking or nonblocking mode and to implement the blocking or nonblocking behavior. For some device types, the blocking and nonblocking behavior can be implemented by the underlying operating system; for other device types, the behavior must be emulated in the channel driver. </p>
<p> This value can be retrieved with <code>Tcl_ChannelBlockModeProc</code>, which returns a pointer to the function. </p>
<p> A channel driver <code>not</code> supplying a <i>blockModeProc</i> has to be very, very careful. It has to tell the generic layer exactly which blocking mode is acceptable to it, and should this also document for the user so that the blocking mode of the channel is not changed to an unacceptable value. Any confusion here may lead the interpreter into a (spurious and difficult to find) deadlock.</p>
<h3>Closeproc And Close2Proc</h3>
<p>The <i>closeProc</i> field contains the address of a function called by the generic layer to clean up driver-related information when the channel is closed. <i>CloseProc</i> must match the following prototype: </p>
<dl COMPACT>
<dd>
<pre>typedef int Tcl_DriverCloseProc(
 ClientData <i>instanceData</i>,
 Tcl_Interp *<i>interp</i>);</pre>
</dl>
<p> The <i>instanceData</i> argument is the same as the value provided to <code>Tcl_CreateChannel</code> when the channel was created. The function should release any storage maintained by the channel driver for this channel, and close the input and output devices encapsulated by this channel. All queued output will have been flushed to the device before this function is called, and no further driver operations will be invoked on this instance after calling the <i>closeProc</i>. If the close operation is successful, the procedure should return zero; otherwise it should return a nonzero POSIX error code. In addition, if an error occurs and <i>interp</i> is not NULL, the procedure should store an error message in the interpreter&#8217;s result. </p>
<p> Alternatively, channels that support closing the read and write sides independently may set <i>closeProc</i> to <code>TCL_CLOSE2PROC</code> and set <i>close2Proc</i> to the address of a function that matches the following prototype: </p>
<dl COMPACT>
<dd>
<pre>typedef int Tcl_DriverClose2Proc(
 ClientData <i>instanceData</i>,
 Tcl_Interp *<i>interp</i>,
 int <i>flags</i>);</pre>
</dl>
<p> The <i>close2Proc</i> will be called with <i>flags</i> set to an OR&#8217;ed combination of <code>TCL_CLOSE_READ</code> or <code>TCL_CLOSE_WRITE</code> to indicate that the driver should close the read and/or write side of the channel. The channel driver may be invoked to perform additional operations on the channel after <i>close2Proc</i> is called to close one or both sides of the channel. If <i>flags</i> is <code>0</code> (zero), the driver should close the channel in the manner described above for <i>closeProc</i>. No further operations will be invoked on this instance after <i>close2Proc</i> is called with all flags cleared. In all cases, the <i>close2Proc</i> function should return zero if the close operation was successful; otherwise it should return a nonzero POSIX error code. In addition, if an error occurs and <i>interp</i> is not NULL, the procedure should store an error message in the interpreter&#8217;s result. </p>
<p> The <i>closeProc</i> and <i>close2Proc</i> values can be retrieved with <code>Tcl_ChannelCloseProc</code> or <code>Tcl_ChannelClose2Proc</code>, which return a pointer to the respective function.</p>
<h3>Inputproc</h3>
<p>The <i>inputProc</i> field contains the address of a function called by the generic layer to read data from the file or device and store it in an internal buffer. <i>InputProc</i> must match the following prototype: </p>
<dl COMPACT>
<dd>
<pre>typedef int Tcl_DriverInputProc(
 ClientData <i>instanceData</i>,
 char *<i>buf</i>,
 int <i>bufSize</i>,
 int *<i>errorCodePtr</i>);</pre>
</dl>
<p> <i>InstanceData</i> is the same as the value passed to <code>Tcl_CreateChannel</code> when the channel was created. The <i>buf</i> argument points to an array of bytes in which to store input from the device, and the <i>bufSize</i> argument indicates how many bytes are available at <i>buf</i>. </p>
<p> The <i>errorCodePtr</i> argument points to an integer variable provided by the generic layer. If an error occurs, the function should set the variable to a POSIX error code that identifies the error that occurred. </p>
<p> The function should read data from the input device encapsulated by the channel and store it at <i>buf</i>. On success, the function should return a nonnegative integer indicating how many bytes were read from the input device and stored at <i>buf</i>. On error, the function should return -1. If an error occurs after some data has been read from the device, that data is lost. </p>
<p> If <i>inputProc</i> can determine that the input device has some data available but less than requested by the <i>bufSize</i> argument, the function should only attempt to read as much data as is available and return without blocking. If the input device has no data available whatsoever and the channel is in nonblocking mode, the function should return an <code>EAGAIN</code> error. If the input device has no data available whatsoever and the channel is in blocking mode, the function should block for the shortest possible time until at least one byte of data can be read from the device; then, it should return as much data as it can read without blocking. </p>
<p> This value can be retrieved with <code>Tcl_ChannelInputProc</code>, which returns a pointer to the function.</p>
<h3>Outputproc</h3>
<p>The <i>outputProc</i> field contains the address of a function called by the generic layer to transfer data from an internal buffer to the output device. <i>OutputProc</i> must match the following prototype: </p>
<dl COMPACT>
<dd>
<pre>typedef int Tcl_DriverOutputProc(
 ClientData <i>instanceData</i>,
 const char *<i>buf</i>,
 int <i>toWrite</i>,
 int *<i>errorCodePtr</i>);</pre>
</dl>
<p> <i>InstanceData</i> is the same as the value passed to <code>Tcl_CreateChannel</code> when the channel was created. The <i>buf</i> argument contains an array of bytes to be written to the device, and the <i>toWrite</i> argument indicates how many bytes are to be written from the <i>buf</i> argument. </p>
<p> The <i>errorCodePtr</i> argument points to an integer variable provided by the generic layer. If an error occurs, the function should set this variable to a POSIX error code that identifies the error. </p>
<p> The function should write the data at <i>buf</i> to the output device encapsulated by the channel. On success, the function should return a nonnegative integer indicating how many bytes were written to the output device. The return value is normally the same as <i>toWrite</i>, but may be less in some cases such as if the output operation is interrupted by a signal. If an error occurs the function should return -1. In case of error, some data may have been written to the device. </p>
<p> If the channel is nonblocking and the output device is unable to absorb any data whatsoever, the function should return -1 with an <code>EAGAIN</code> error without writing any data. </p>
<p> This value can be retrieved with <code>Tcl_ChannelOutputProc</code>, which returns a pointer to the function.</p>
<h3>Seekproc And Wideseekproc</h3>
<p>The <i>seekProc</i> field contains the address of a function called by the generic layer to move the access point at which subsequent input or output operations will be applied. <i>SeekProc</i> must match the following prototype: </p>
<dl COMPACT>
<dd>
<pre>typedef int Tcl_DriverSeekProc(
 ClientData <i>instanceData</i>,
 long <i>offset</i>,
 int <i>seekMode</i>,
 int *<i>errorCodePtr</i>);</pre>
</dl>
<p> The <i>instanceData</i> argument is the same as the value given to <code>Tcl_CreateChannel</code> when this channel was created. <i>Offset</i> and <i>seekMode</i> have the same meaning as for the <code>Tcl_Seek</code> procedure (described in the manual entry for <code>Tcl_OpenFileChannel</code>). </p>
<p> The <i>errorCodePtr</i> argument points to an integer variable provided by the generic layer for returning <code>errno</code> values from the function. The function should set this variable to a POSIX error code if an error occurs. The function should store an <code>EINVAL</code> error code if the channel type does not implement seeking. </p>
<p> The return value is the new access point or -1 in case of error. If an error occurred, the function should not move the access point. </p>
<p> If there is a non-NULL <i>seekProc</i> field, the <i>wideSeekProc</i> field may contain the address of an alternative function to use which handles wide (i.e. larger than 32-bit) offsets, so allowing seeks within files larger than 2GB. The <i>wideSeekProc</i> will be called in preference to the <i>seekProc</i>, but both must be defined if the <i>wideSeekProc</i> is defined. <i>WideSeekProc</i> must match the following prototype: </p>
<dl COMPACT>
<dd>
<pre>typedef Tcl_WideInt Tcl_DriverWideSeekProc(
 ClientData <i>instanceData</i>,
 Tcl_WideInt <i>offset</i>,
 int <i>seekMode</i>,
 int *<i>errorCodePtr</i>);</pre>
</dl>
<p> The arguments and return values mean the same thing as with <i>seekProc</i> above, except that the type of offsets and the return type are different. </p>
<p> The <i>seekProc</i> value can be retrieved with <code>Tcl_ChannelSeekProc</code>, which returns a pointer to the function, and similarly the <i>wideSeekProc</i> can be retrieved with <code>Tcl_ChannelWideSeekProc</code>.</p>
<h3>Setoptionproc</h3>
<p>The <i>setOptionProc</i> field contains the address of a function called by the generic layer to set a channel type specific option on a channel. <i>setOptionProc</i> must match the following prototype: </p>
<dl COMPACT>
<dd>
<pre>typedef int Tcl_DriverSetOptionProc(
 ClientData <i>instanceData</i>,
 Tcl_Interp *<i>interp</i>,
 const char *<i>optionName</i>,
 const char *<i>newValue</i>);</pre>
</dl>
<p> <i>optionName</i> is the name of an option to set, and <i>newValue</i> is the new value for that option, as a string. The <i>instanceData</i> is the same as the value given to <code>Tcl_CreateChannel</code> when this channel was created. The function should do whatever channel type specific action is required to implement the new value of the option. </p>
<p> Some options are handled by the generic code and this function is never called to set them, e.g. <code>-blockmode</code>. Other options are specific to each channel type and the <i>setOptionProc</i> procedure of the channel driver will get called to implement them. The <i>setOptionProc</i> field can be NULL, which indicates that this channel type supports no type specific options. </p>
<p> If the option value is successfully modified to the new value, the function returns <code>TCL_OK</code>. It should call <code>Tcl_BadChannelOption</code> which itself returns <code>TCL_ERROR</code> if the <i>optionName</i> is unrecognized. If <i>newValue</i> specifies a value for the option that is not supported or if a system call error occurs, the function should leave an error message in the <i>result</i> field of <i>interp</i> if <i>interp</i> is not NULL. The function should also call <code>Tcl_SetErrno</code> to store an appropriate POSIX error code. </p>
<p> This value can be retrieved with <code>Tcl_ChannelSetOptionProc</code>, which returns a pointer to the function.</p>
<h3>Getoptionproc</h3>
<p>The <i>getOptionProc</i> field contains the address of a function called by the generic layer to get the value of a channel type specific option on a channel. <i>getOptionProc</i> must match the following prototype: </p>
<dl COMPACT>
<dd>
<pre>typedef int Tcl_DriverGetOptionProc(
 ClientData <i>instanceData</i>,
 Tcl_Interp *<i>interp</i>,
 const char *<i>optionName</i>,
 Tcl_DString *<i>optionValue</i>);</pre>
</dl>
<p> <i>OptionName</i> is the name of an option supported by this type of channel. If the option name is not NULL, the function stores its current value, as a string, in the Tcl dynamic string <i>optionValue</i>. If <i>optionName</i> is NULL, the function stores in <i>optionValue</i> an alternating list of all supported options and their current values. On success, the function returns <code>TCL_OK</code>. It should call <code>Tcl_BadChannelOption</code> which itself returns <code>TCL_ERROR</code> if the <i>optionName</i> is unrecognized. If a system call error occurs, the function should leave an error message in the result of <i>interp</i> if <i>interp</i> is not NULL. The function should also call <code>Tcl_SetErrno</code> to store an appropriate POSIX error code. </p>
<p> Some options are handled by the generic code and this function is never called to retrieve their value, e.g. <code>-blockmode</code>. Other options are specific to each channel type and the <i>getOptionProc</i> procedure of the channel driver will get called to implement them. The <i>getOptionProc</i> field can be NULL, which indicates that this channel type supports no type specific options. </p>
<p> This value can be retrieved with <code>Tcl_ChannelGetOptionProc</code>, which returns a pointer to the function.</p>
<h3>Watchproc</h3>
<p>The <i>watchProc</i> field contains the address of a function called by the generic layer to initialize the event notification mechanism to notice events of interest on this channel. <i>WatchProc</i> should match the following prototype: </p>
<dl COMPACT>
<dd>
<pre>typedef void Tcl_DriverWatchProc(
 ClientData <i>instanceData</i>,
 int <i>mask</i>);</pre>
</dl>
<p> The <i>instanceData</i> is the same as the value passed to <code>Tcl_CreateChannel</code> when this channel was created. The <i>mask</i> argument is an OR-ed combination of <code>TCL_READABLE</code>, <code>TCL_WRITABLE</code> and <code>TCL_EXCEPTION</code>; it indicates events the caller is interested in noticing on this channel. </p>
<p> The function should initialize device type specific mechanisms to notice when an event of interest is present on the channel. When one or more of the designated events occurs on the channel, the channel driver is responsible for calling <code>Tcl_NotifyChannel</code> to inform the generic channel module. The driver should take care not to starve other channel drivers or sources of callbacks by invoking Tcl_NotifyChannel too frequently. Fairness can be insured by using the Tcl event queue to allow the channel event to be scheduled in sequence with other events. See the description of <code>Tcl_QueueEvent</code> for details on how to queue an event. </p>
<p> This value can be retrieved with <code>Tcl_ChannelWatchProc</code>, which returns a pointer to the function.</p>
<h3>Gethandleproc</h3>
<p>The <i>getHandleProc</i> field contains the address of a function called by the generic layer to retrieve a device-specific handle from the channel. <i>GetHandleProc</i> should match the following prototype: </p>
<dl COMPACT>
<dd>
<pre>typedef int Tcl_DriverGetHandleProc(
 ClientData <i>instanceData</i>,
 int <i>direction</i>,
 ClientData *<i>handlePtr</i>);</pre>
</dl>
<p> <i>InstanceData</i> is the same as the value passed to <code>Tcl_CreateChannel</code> when this channel was created. The <i>direction</i> argument is either <code>TCL_READABLE</code> to retrieve the handle used for input, or <code>TCL_WRITABLE</code> to retrieve the handle used for output. </p>
<p> If the channel implementation has device-specific handles, the function should retrieve the appropriate handle associated with the channel, according the <i>direction</i> argument. The handle should be stored in the location referred to by <i>handlePtr</i>, and <code>TCL_OK</code> should be returned. If the channel is not open for the specified direction, or if the channel implementation does not use device handles, the function should return <code>TCL_ERROR</code>. </p>
<p> This value can be retrieved with <code>Tcl_ChannelGetHandleProc</code>, which returns a pointer to the function.</p>
<h3>Flushproc</h3>
<p>The <i>flushProc</i> field is currently reserved for future use. It should be set to NULL. <i>FlushProc</i> should match the following prototype: </p>
<dl COMPACT>
<dd>
<pre>typedef int Tcl_DriverFlushProc(
 ClientData <i>instanceData</i>);</pre>
</dl>
<p> This value can be retrieved with <code>Tcl_ChannelFlushProc</code>, which returns a pointer to the function.</p>
<h3>Handlerproc</h3>
<p>The <i>handlerProc</i> field contains the address of a function called by the generic layer to notify the channel that an event occurred. It should be defined for stacked channel drivers that wish to be notified of events that occur on the underlying (stacked) channel. <i>HandlerProc</i> should match the following prototype: </p>
<dl COMPACT>
<dd>
<pre>typedef int Tcl_DriverHandlerProc(
 ClientData <i>instanceData</i>,
 int <i>interestMask</i>);</pre>
</dl>
<p> <i>InstanceData</i> is the same as the value passed to <code>Tcl_CreateChannel</code> when this channel was created. The <i>interestMask</i> is an OR-ed combination of <code>TCL_READABLE</code> or <code>TCL_WRITABLE</code>; it indicates what type of event occurred on this channel. </p>
<p> This value can be retrieved with <code>Tcl_ChannelHandlerProc</code>, which returns a pointer to the function. </p>
<h3>Threadactionproc</h3>
<p>The <i>threadActionProc</i> field contains the address of the function called by the generic layer when a channel is created, closed, or going to move to a different thread, i.e. whenever thread-specific driver state might have to initialized or updated. It can be NULL. The action <i>TCL_CHANNEL_THREAD_REMOVE</i> is used to notify the driver that it should update or remove any thread-specific data it might be maintaining for the channel. </p>
<p> The action <i>TCL_CHANNEL_THREAD_INSERT</i> is used to notify the driver that it should update or initialize any thread-specific data it might be maintaining using the calling thread as the associate. See <code>Tcl_CutChannel</code> and <code>Tcl_SpliceChannel</code> for more detail. </p>
<dl COMPACT>
<dd>
<pre>typedef void Tcl_DriverThreadActionProc(
 ClientData <i>instanceData</i>,
 int <i>action</i>);</pre>
</dl>
<p> <i>InstanceData</i> is the same as the value passed to <code>Tcl_CreateChannel</code> when this channel was created. </p>
<p> These values can be retrieved with <code>Tcl_ChannelThreadActionProc</code>, which returns a pointer to the function.</p>
<h3>Truncateproc</h3>
<p>The <i>truncateProc</i> field contains the address of the function called by the generic layer when a channel is truncated to some length. It can be NULL. </p>
<dl COMPACT>
<dd>
<pre>typedef int Tcl_DriverTruncateProc(
 ClientData <i>instanceData</i>,
 Tcl_WideInt <i>length</i>);</pre>
</dl>
<p> <i>InstanceData</i> is the same as the value passed to <code>Tcl_CreateChannel</code> when this channel was created, and <i>length</i> is the new length of the underlying file, which should not be negative. The result should be 0 on success or an errno code (suitable for use with <code>Tcl_SetErrno</code>) on failure. </p>
<p> These values can be retrieved with <code>Tcl_ChannelTruncateProc</code>, which returns a pointer to the function.</p>
<h2>Tcl_Badchanneloption</h2>
<p>This procedure generates a &#8220;bad option&#8221; error message in an (optional) interpreter. It is used by channel drivers when an invalid Set/Get option is requested. Its purpose is to concatenate the generic options list to the specific ones and factorize the generic options error message string. </p>
<p> It always returns <code>TCL_ERROR</code> </p>
<p> An error message is generated in <i>interp</i>&#8216;s result object to indicate that a command was invoked with a bad option. The message has the form</p>
<dl COMPACT>
<dd>
<pre> bad option &quot;blah&quot;: should be one of 
 &lt;...generic options...&gt;+&lt;...specific options...&gt;</pre>
</dl>
<p> so you get for instance:</p>
<dl COMPACT>
<dd>
<pre> bad option &quot;-blah&quot;: should be one of -blocking,
 -buffering, -buffersize, -eofchar, -translation,
 -peername, or -sockname</pre>
</dl>
<p> when called with <i>optionList</i> equal to &#8220;peername sockname&#8221; </p>
<p> &#8220;blah&#8221; is the <i>optionName</i> argument and &#8220;&lt;specific options&gt;&#8221; is a space separated list of specific option words. The function takes good care of inserting minus signs before each option, commas after, and an &#8220;or&#8221; before the last option.</p>
<h2>Old Channel Types</h2>
<p>The original (8.3.1 and below) <code>Tcl_ChannelType</code> structure contains the following fields: </p>
<dl COMPACT>
<dd>
<pre>typedef struct Tcl_ChannelType {
 char *<i>typeName</i>;
 Tcl_DriverBlockModeProc *<i>blockModeProc</i>;
 Tcl_DriverCloseProc *<i>closeProc</i>;
 Tcl_DriverInputProc *<i>inputProc</i>;
 Tcl_DriverOutputProc *<i>outputProc</i>;
 Tcl_DriverSeekProc *<i>seekProc</i>;
 Tcl_DriverSetOptionProc *<i>setOptionProc</i>;
 Tcl_DriverGetOptionProc *<i>getOptionProc</i>;
 Tcl_DriverWatchProc *<i>watchProc</i>;
 Tcl_DriverGetHandleProc *<i>getHandleProc</i>;
 Tcl_DriverClose2Proc *<i>close2Proc</i>;
} Tcl_ChannelType;</pre>
</dl>
<p> It is still possible to create channel with the above structure. The internal channel code will determine the version. It is imperative to use the new <code>Tcl_ChannelType</code> structure if you are creating a stacked channel driver, due to problems with the earlier stacked channel implementation (in 8.2.0 to 8.3.1). </p>
<p> Prior to 8.4.0 (i.e. during the later releases of 8.3 and early part of the 8.4 development cycle) the <code>Tcl_ChannelType</code> structure contained the following fields: </p>
<dl COMPACT>
<dd>
<pre>typedef struct Tcl_ChannelType {
 char *<i>typeName</i>;
 Tcl_ChannelTypeVersion <i>version</i>;
 Tcl_DriverCloseProc *<i>closeProc</i>;
 Tcl_DriverInputProc *<i>inputProc</i>;
 Tcl_DriverOutputProc *<i>outputProc</i>;
 Tcl_DriverSeekProc *<i>seekProc</i>;
 Tcl_DriverSetOptionProc *<i>setOptionProc</i>;
 Tcl_DriverGetOptionProc *<i>getOptionProc</i>;
 Tcl_DriverWatchProc *<i>watchProc</i>;
 Tcl_DriverGetHandleProc *<i>getHandleProc</i>;
 Tcl_DriverClose2Proc *<i>close2Proc</i>;
 Tcl_DriverBlockModeProc *<i>blockModeProc</i>;
 Tcl_DriverFlushProc *<i>flushProc</i>;
 Tcl_DriverHandlerProc *<i>handlerProc</i>;
 Tcl_DriverTruncateProc *<i>truncateProc</i>;
} Tcl_ChannelType;</pre>
</dl>
<p> When the above structure is registered as a channel type, the <i>version</i> field should always be <code>TCL_CHANNEL_VERSION_2</code>. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-tcl_close/">Tcl_Close</a>(3), <a href="/docs/linux/man/3-tcl_openfilechannel/">Tcl_OpenFileChannel</a>(3), <a href="/docs/linux/man/3-tcl_seterrno/">Tcl_SetErrno</a>(3), <a href="/docs/linux/man/3-tcl_queueevent/">Tcl_QueueEvent</a>(3), <a href="/docs/linux/man/3-tcl_stackchannel/">Tcl_StackChannel</a>(3), <a href="/docs/linux/man/3-tcl_getstdchannel/">Tcl_GetStdChannel</a>(3) </p>
<h2>Keywords</h2>
<p>blocking, channel driver, channel registration, channel type, nonblocking</p>
