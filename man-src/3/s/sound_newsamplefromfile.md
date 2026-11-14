---
title: "sound_newsamplefromfile(3)"
name: "sound_newsamplefromfile"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sound_newsamplefromfile/"
description: "SDL_sound.h –"
---

<p>SDL_sound.h &#8211; </p>
<h2>Synopsis</h2>
<p>#include &#8216;SDL.h&#8217;<br />
 #include &#8216;SDL_endian.h&#8217; </p>
<h3>Data Structures</h3>
<p>struct <code>Sound_AudioInfo</code><br />
 <i>Information about an existing sample&#8217;s format. </i><br />
 struct <code>Sound_DecoderInfo</code><br />
 <i>Information about available soudn decoders. </i><br />
 struct <code>Sound_Sample</code><br />
 <i>Represents sound data in the process of being decoded. </i><br />
 struct <code>Sound_Version</code><br />
 <i>Information the version of SDL_sound in use. </i></p>
<h3>Defines</h3>
<p>#define <code>SOUND_VERSION</code>(x)<br />
 <i>Macro to determine SDL_sound version program was compiled against. </i></p>
<h3>Enumerations</h3>
<p>enum <code>Sound_SampleFlags</code> { <code>SOUND_SAMPLEFLAG_NONE</code> = 0, <code>SOUND_SAMPLEFLAG_CANSEEK</code> = 1, <code>SOUND_SAMPLEFLAG_EOF</code> = 1 &lt;&lt; 29, <code>SOUND_SAMPLEFLAG_ERROR</code> = 1 &lt;&lt; 30, <code>SOUND_SAMPLEFLAG_EAGAIN</code> = 1 &lt;&lt; 31 }<br />
 <i>Flags that are used in a </i><code>Sound_Sample</code> to show various states.</p>
<h3>Functions</h3>
<p>void <code>Sound_GetLinkedVersion</code> (<code>Sound_Version</code> *ver)<br />
 <i>Get the version of SDL_sound that is linked against your program. </i><br />
 int <code>Sound_Init</code> (void)<br />
 <i>Initialize SDL_sound. </i><br />
 int <code>Sound_Quit</code> (void)<br />
 <i>Shutdown SDL_sound. </i><br />
 const <code>Sound_DecoderInfo</code> ** <code>Sound_AvailableDecoders</code> (void)<br />
 <i>Get a list of sound formats supported by this version of SDL_sound. </i><br />
 const char * <code>Sound_GetError</code> (void)<br />
 <i>Get the last SDL_sound error message as a null-terminated string. </i><br />
 void <code>Sound_ClearError</code> (void)<br />
 <i>Clear the current error message. </i><br />
 <code>Sound_Sample</code> * <code>Sound_NewSample</code> (SDL_RWops *rw, const char *ext, <code>Sound_AudioInfo</code> *desired, Uint32 bufferSize)<br />
 <i>Start decoding a new sound sample. </i><br />
 <code>Sound_Sample</code> * <code>Sound_NewSampleFromFile</code> (const char *fname, <code>Sound_AudioInfo</code> *desired, Uint32 bufferSize)<br />
 <i>Start decoding a new sound sample from a file on disk. </i><br />
 void <code>Sound_FreeSample</code> (<code>Sound_Sample</code> *sample)<br />
 <i>Dispose of a </i><code>Sound_Sample</code>.<br />
 int <code>Sound_SetBufferSize</code> (<code>Sound_Sample</code> *sample, Uint32 new_size)<br />
 <i>Change the current buffer size for a sample. </i><br />
 Uint32 <code>Sound_Decode</code> (<code>Sound_Sample</code> *sample)<br />
 <i>Decode more of the sound data in a </i><code>Sound_Sample</code>.<br />
 Uint32 <code>Sound_DecodeAll</code> (<code>Sound_Sample</code> *sample)<br />
 <i>Decode the remainder of the sound data in a </i><code>Sound_Sample</code>.<br />
 int <code>Sound_Rewind</code> (<code>Sound_Sample</code> *sample)<br />
 <i>Rewind a sample to the start. </i><br />
 int <code>Sound_Seek</code> (<code>Sound_Sample</code> *sample, Uint32 ms)<br />
 <i>Seek to a different point in a sample. </i></p>
<h2>Detailed Description</h2>
<h2>Define Documentation</h2>
<h3>#define SOUND_VERSION(x)</h3>
<p><code>Value:</code> </p>
<pre>{ (x)-&gt;major = SOUND_VER_MAJOR; (x)-&gt;minor = SOUND_VER_MINOR; (x)-&gt;patch = SOUND_VER_PATCH; }</pre>
<p>Macro to determine SDL_sound version program was compiled against. </p>
<p> This macro fills in a <code>Sound_Version</code> structure with the version of the library you compiled against. This is determined by what header the compiler uses. Note that if you dynamically linked the library, you might have a slightly newer or older version at runtime. That version can be determined with <code>Sound_GetLinkedVersion()</code>, which, unlike SOUND_VERSION, is not a macro. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>x</i> A pointer to a <code>Sound_Version</code> struct to initialize.</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Sound_Version</code> </p>
<p> <code>Sound_GetLinkedVersion</code></dl>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>Sound_SampleFlags</code></h3>
<p>Flags that are used in a <code>Sound_Sample</code> to show various states. </p>
<p> To use: </p>
<pre> if (sample-&gt;flags &amp; SOUND_SAMPLEFLAG_ERROR) { dosomething(); }</pre>
<p><code>See also:</code></p>
<dl COMPACT>
<dd>Sound_SampleNew </p>
<p> Sound_SampleNewFromFile </p>
<p> Sound_SampleDecode </p>
<p> Sound_SampleDecodeAll </p>
<p> Sound_SampleSeek</dl>
<p> <code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>SOUND_SAMPLEFLAG_NONE </i></p>
<dd>No special attributes.</p>
<dt><i>SOUND_SAMPLEFLAG_CANSEEK </i></p>
<dd>Sample can seek to arbitrary points.</p>
<dt><i>SOUND_SAMPLEFLAG_EOF </i></p>
<dd>End of input stream.</p>
<dt><i>SOUND_SAMPLEFLAG_ERROR </i></p>
<dd>Unrecoverable error.</p>
<dt><i>SOUND_SAMPLEFLAG_EAGAIN </i></p>
<dd>Function would block, or temp error.</dl>
<h2>Function Documentation</h2>
<h3>const <code>Sound_DecoderInfo</code> ** Sound_AvailableDecoders (void)</h3>
<p>Get a list of sound formats supported by this version of SDL_sound. </p>
<p> This is for informational purposes only. Note that the extension listed is merely convention: if we list &#8216;MP3&#8217;, you can open an MPEG-1 Layer 3 audio file with an extension of &#8216;XYZ&#8217;, if you like. The file extensions are informational, and only required as a hint to choosing the correct decoder, since the sound data may not be coming from a file at all, thanks to the abstraction that an SDL_RWops provides. </p>
<p> The returned value is an array of pointers to <code>Sound_DecoderInfo</code> structures, with a NULL entry to signify the end of the list: </p>
<pre> Sound_DecoderInfo **i;
 for (i = Sound_AvailableDecoders(); *i != NULL; i++)
 {
 printf('Supported sound format: [%s], which is [%s].,
 i-&gt;extension, i-&gt;description);
 // ...and other fields...
 }</pre>
<p>The return values are pointers to static internal memory, and should be considered READ ONLY, and never freed. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>READ ONLY Null-terminated array of READ ONLY structures.</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Sound_DecoderInfo</code></dl>
<h3>void Sound_ClearError (void)</h3>
<p>Clear the current error message. </p>
<p> The next call to <code>Sound_GetError()</code> after <code>Sound_ClearError()</code> will return NULL. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Sound_GetError</code></dl>
<h3>Uint32 Sound_Decode (<code>Sound_Sample</code> * sample)</h3>
<p>Decode more of the sound data in a <code>Sound_Sample</code>. </p>
<p> It will decode at most sample-&gt;buffer_size bytes into sample-&gt;buffer in the desired format, and return the number of decoded bytes. If sample-&gt;buffer_size bytes could not be decoded, then please refer to sample-&gt;flags to determine if this was an end-of-stream or error condition. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>sample</i> Do more decoding to this <code>Sound_Sample</code>.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>number of bytes decoded into sample-&gt;buffer. If it is less than sample-&gt;buffer_size, then you should check sample-&gt;flags to see what the current state of the sample is (EOF, error, read again).</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Sound_DecodeAll</code> </p>
<p> <code>Sound_SetBufferSize</code> </p>
<p> <code>Sound_Seek</code> </p>
<p> <code>Sound_Rewind</code></dl>
<h3>Uint32 Sound_DecodeAll (<code>Sound_Sample</code> * sample)</h3>
<p>Decode the remainder of the sound data in a <code>Sound_Sample</code>. </p>
<p> This will dynamically allocate memory for the ENTIRE remaining sample. sample-&gt;buffer_size and sample-&gt;buffer will be updated to reflect the new buffer. Please refer to sample-&gt;flags to determine if the decoding finished due to an End-of-stream or error condition. </p>
<p> Be aware that sound data can take a large amount of memory, and that this function may block for quite awhile while processing. Also note that a streaming source (for example, from a SDL_RWops that is getting fed from an Internet radio feed that doesn&#8217;t end) may fill all available memory before giving up&#8230;be sure to use this on finite sound sources only! </p>
<p> When decoding the sample in its entirety, the work is done one buffer at a time. That is, sound is decoded in sample-&gt;buffer_size blocks, and appended to a continually-growing buffer until the decoding completes. That means that this function will need enough RAM to hold approximately sample-&gt;buffer_size bytes plus the complete decoded sample at most. The larger your buffer size, the less overhead this function needs, but beware the possibility of paging to disk. Best to make this user-configurable if the sample isn&#8217;t specific and small. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>sample</i> Do all decoding for this <code>Sound_Sample</code>.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>number of bytes decoded into sample-&gt;buffer. You should check sample-&gt;flags to see what the current state of the sample is (EOF, error, read again).</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Sound_Decode</code> </p>
<p> <code>Sound_SetBufferSize</code></dl>
<h3>void Sound_FreeSample (<code>Sound_Sample</code> * sample)</h3>
<p>Dispose of a <code>Sound_Sample</code>. </p>
<p> This will also close/dispose of the SDL_RWops that was used at creation time, so there&#8217;s no need to keep a reference to that around. The <code>Sound_Sample</code> pointer is invalid after this call, and will almost certainly result in a crash if you attempt to keep using it. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>sample</i> The <code>Sound_Sample</code> to delete.</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Sound_NewSample</code> </p>
<p> <code>Sound_NewSampleFromFile</code></dl>
<h3>const char * Sound_GetError (void)</h3>
<p>Get the last SDL_sound error message as a null-terminated string. </p>
<p> This will be NULL if there&#8217;s been no error since the last call to this function. The pointer returned by this call points to an internal buffer, and should not be deallocated. Each thread has a unique error state associated with it, but each time a new error message is set, it will overwrite the previous one associated with that thread. It is safe to call this function at anytime, even before <code>Sound_Init()</code>. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>READ ONLY string of last error message.</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Sound_ClearError</code></dl>
<h3>void Sound_GetLinkedVersion (<code>Sound_Version</code> * ver)</h3>
<p>Get the version of SDL_sound that is linked against your program. </p>
<p> If you are using a shared library (DLL) version of SDL_sound, then it is possible that it will be different than the version you compiled against. </p>
<p> This is a real function; the macro SOUND_VERSION tells you what version of SDL_sound you compiled against: </p>
<pre> Sound_Version compiled;
 Sound_Version linked;
 SOUND_VERSION(&amp;compiled);
 Sound_GetLinkedVersion(&amp;linked);
 printf('We compiled against SDL_sound version %d.%d.%d ...,
 compiled.major, compiled.minor, compiled.patch);
 printf('But we linked against SDL_sound version %d.%d.%d.,
 linked.major, linked.minor, linked.patch);</pre>
<p>This function may be called safely at any time, even before <code>Sound_Init()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ver</i> <code>Sound_Version</code> structure to fill with shared library&#8217;s version.</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Sound_Version</code> </p>
<p> <code>SOUND_VERSION</code></dl>
<h3>Sound_Init (void)</h3>
<p>Initialize SDL_sound. </p>
<p> This must be called before any other SDL_sound function (except perhaps <code>Sound_GetLinkedVersion()</code>). You should call SDL_Init() before calling this. <code>Sound_Init()</code> will attempt to call SDL_Init(SDL_INIT_AUDIO), just in case. This is a safe behaviour, but it may not configure SDL to your liking by itself. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>nonzero on success, zero on error. Specifics of the error can be gleaned from <code>Sound_GetError()</code>.</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Sound_Quit</code></dl>
<h3><code>Sound_Sample</code> * Sound_NewSample (SDL_RWops * rw, const char * ext, <code>Sound_AudioInfo</code> * desired, Uint32 bufferSize)</h3>
<p>Start decoding a new sound sample. </p>
<p> The data is read via an SDL_RWops structure (see SDL_rwops.h in the SDL include directory), so it may be coming from memory, disk, network stream, etc. The (ext) parameter is merely a hint to determining the correct decoder; if you specify, for example, &#8216;mp3&#8217; for an extension, and one of the decoders lists that as a handled extension, then that decoder is given first shot at trying to claim the data for decoding. If none of the extensions match (or the extension is NULL), then every decoder examines the data to determine if it can handle it, until one accepts it. In such a case your SDL_RWops will need to be capable of rewinding to the start of the stream. </p>
<p> If no decoders can handle the data, a NULL value is returned, and a human readable error message can be fetched from <code>Sound_GetError()</code>. </p>
<p> Optionally, a desired audio format can be specified. If the incoming data is in a different format, SDL_sound will convert it to the desired format on the fly. Note that this can be an expensive operation, so it may be wise to convert data before you need to play it back, if possible, or make sure your data is initially in the format that you need it in. If you don&#8217;t want to convert the data, you can specify NULL for a desired format. The incoming format of the data, preconversion, can be found in the <code>Sound_Sample</code> structure. </p>
<p> Note that the raw sound data &#8216;decoder&#8217; needs you to specify both the extension &#8216;RAW&#8217; and a &#8216;desired&#8217; format, or it will refuse to handle the data. This is to prevent it from catching all formats unsupported by the other decoders. </p>
<p> Finally, specify an initial buffer size; this is the number of bytes that will be allocated to store each read from the sound buffer. The more you can safely allocate, the more decoding can be done in one block, but the more resources you have to use up, and the longer each decoding call will take. Note that different data formats require more or less space to store. This buffer can be resized via <code>Sound_SetBufferSize()</code> &#8230; </p>
<p> The buffer size specified must be a multiple of the size of a single sample point. So, if you want 16-bit, stereo samples, then your sample point size is (2 channels * 16 bits), or 32 bits per sample, which is four bytes. In such a case, you could specify 128 or 132 bytes for a buffer, but not 129, 130, or 131 (although in reality, you&#8217;ll want to specify a MUCH larger buffer). </p>
<p> When you are done with this <code>Sound_Sample</code> pointer, you can dispose of it via <code>Sound_FreeSample()</code>. </p>
<p> You do not have to keep a reference to (rw) around. If this function suceeds, it stores (rw) internally (and disposes of it during the call to <code>Sound_FreeSample()</code>). If this function fails, it will dispose of the SDL_RWops for you. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rw</i> SDL_RWops with sound data.<br />
 <i>ext</i> File extension normally associated with a data format. Can usually be NULL.<br />
 <i>desired</i> Format to convert sound data into. Can usually be NULL, if you don&#8217;t need conversion.<br />
 <i>bufferSize</i> Size, in bytes, to allocate for the decoding buffer.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd><code>Sound_Sample</code> pointer, which is used as a handle to several other SDL_sound APIs. NULL on error. If error, use <code>Sound_GetError()</code> to see what went wrong.</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Sound_NewSampleFromFile</code> </p>
<p> <code>Sound_SetBufferSize</code> </p>
<p> <code>Sound_Decode</code> </p>
<p> <code>Sound_DecodeAll</code> </p>
<p> <code>Sound_Seek</code> </p>
<p> <code>Sound_Rewind</code> </p>
<p> <code>Sound_FreeSample</code></dl>
<h3><code>Sound_Sample</code> * Sound_NewSampleFromFile (const char * filename, <code>Sound_AudioInfo</code> * desired, Uint32 bufferSize)</h3>
<p>Start decoding a new sound sample from a file on disk. </p>
<p> This is identical to <code>Sound_NewSample()</code>, but it creates an SDL_RWops for you from the file located in (filename). Note that (filename) is specified in platform-dependent notation. (&#8216;C:\music\mysong.mp3&#8217; on windows, and &#8216;/home/icculus/music/mysong.mp3&#8217; or whatever on Unix, etc.) <code>Sound_NewSample()</code>&#8216;s &#8216;ext&#8217; parameter is gleaned from the contents of (filename). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>filename</i> file containing sound data.<br />
 <i>desired</i> Format to convert sound data into. Can usually be NULL, if you don&#8217;t need conversion.<br />
 <i>bufferSize</i> size, in bytes, of initial read buffer.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd><code>Sound_Sample</code> pointer, which is used as a handle to several other SDL_sound APIs. NULL on error. If error, use <code>Sound_GetError()</code> to see what went wrong.</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Sound_NewSample</code> </p>
<p> <code>Sound_SetBufferSize</code> </p>
<p> <code>Sound_Decode</code> </p>
<p> <code>Sound_DecodeAll</code> </p>
<p> <code>Sound_Seek</code> </p>
<p> <code>Sound_Rewind</code> </p>
<p> <code>Sound_FreeSample</code></dl>
<h3>Sound_Quit (void)</h3>
<p>Shutdown SDL_sound. </p>
<p> This closes any SDL_RWops that were being used as sound sources, and frees any resources in use by SDL_sound. </p>
<p> All <code>Sound_Sample</code> pointers you had prior to this call are INVALIDATED. </p>
<p> Once successfully deinitialized, <code>Sound_Init()</code> can be called again to restart the subsystem. All default API states are restored at this point. </p>
<p> You should call this BEFORE SDL_Quit(). This will NOT call SDL_Quit() for you! </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>nonzero on success, zero on error. Specifics of the error can be gleaned from <code>Sound_GetError()</code>. If failure, state of SDL_sound is undefined, and probably badly screwed up.</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Sound_Init</code></dl>
<h3>int Sound_Rewind (<code>Sound_Sample</code> * sample)</h3>
<p>Rewind a sample to the start. </p>
<p> Restart a sample at the start of its waveform data, as if newly created with <code>Sound_NewSample()</code>. If successful, the next call to Sound_Decode[All]() will give audio data from the earliest point in the stream. </p>
<p> Beware that this function will fail if the SDL_RWops that feeds the decoder can not be rewound via it&#8217;s seek method, but this can theoretically be avoided by wrapping it in some sort of buffering SDL_RWops. </p>
<p> This function should ONLY fail if the RWops is not seekable, or SDL_sound is not initialized. Both can be controlled by the application, and thus, it is up to the developer&#8217;s paranoia to dictate whether this function&#8217;s return value need be checked at all. </p>
<p> If this function fails, the state of the sample is undefined, but it is still safe to call <code>Sound_FreeSample()</code> to dispose of it. </p>
<p> On success, ERROR, EOF, and EAGAIN are cleared from sample-&gt;flags. The ERROR flag is set on error. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>sample</i> The <code>Sound_Sample</code> to rewind.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>nonzero on success, zero on error. Specifics of the error can be gleaned from <code>Sound_GetError()</code>.</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Sound_Seek</code></dl>
<h3>int Sound_Seek (<code>Sound_Sample</code> * sample, Uint32 ms)</h3>
<p>Seek to a different point in a sample. </p>
<p> Reposition a sample&#8217;s stream. If successful, the next call to Sound_Decode[All]() will give audio data from the offset you specified. </p>
<p> The offset is specified in milliseconds from the start of the sample. </p>
<p> Beware that this function can fail for several reasons. If the SDL_RWops that feeds the decoder can not seek, this call will almost certainly fail, but this can theoretically be avoided by wrapping it in some sort of buffering SDL_RWops. Some decoders can never seek, others can only seek with certain files. The decoders will set a flag in the sample at creation time to help you determine this. </p>
<p> You should check sample-&gt;flags &amp; SOUND_SAMPLEFLAG_CANSEEK before attempting. <code>Sound_Seek()</code> reports failure immediately if this flag isn&#8217;t set. This function can still fail for other reasons if the flag is set. </p>
<p> This function can be emulated in the application with <code>Sound_Rewind()</code> and predecoding a specific amount of the sample, but this can be extremely inefficient. <code>Sound_Seek()</code> accelerates the seek on a with decoder-specific code. </p>
<p> If this function fails, the sample should continue to function as if this call was never made. If there was an unrecoverable error, sample-&gt;flags &amp; SOUND_SAMPLEFLAG_ERROR will be set, which you regular decoding loop can pick up. </p>
<p> On success, ERROR, EOF, and EAGAIN are cleared from sample-&gt;flags. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>sample</i> The <code>Sound_Sample</code> to seek.<br />
 <i>ms</i> The new position, in milliseconds from start of sample.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>nonzero on success, zero on error. Specifics of the error can be gleaned from <code>Sound_GetError()</code>.</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Sound_Rewind</code></dl>
<h3>int Sound_SetBufferSize (<code>Sound_Sample</code> * sample, Uint32 new_size)</h3>
<p>Change the current buffer size for a sample. </p>
<p> If the buffer size could be changed, then the sample-&gt;buffer and sample-&gt;buffer_size fields will reflect that. If they could not be changed, then your original sample state is preserved. If the buffer is shrinking, the data at the end of buffer is truncated. If the buffer is growing, the contents of the new space at the end is undefined until you decode more into it or initialize it yourself. </p>
<p> The buffer size specified must be a multiple of the size of a single sample point. So, if you want 16-bit, stereo samples, then your sample point size is (2 channels * 16 bits), or 32 bits per sample, which is four bytes. In such a case, you could specify 128 or 132 bytes for a buffer, but not 129, 130, or 131 (although in reality, you&#8217;ll want to specify a MUCH larger buffer). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>sample</i> The <code>Sound_Sample</code> whose buffer to modify.<br />
 <i>new_size</i> The desired size, in bytes, of the new buffer.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>non-zero if buffer size changed, zero on failure.</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Sound_Decode</code> </p>
<p> <code>Sound_DecodeAll</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for SDL_sound from the source code.</p>
