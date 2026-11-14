---
title: "sdl_sound(3)"
name: "sdl_sound"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_sound/"
---

SDL_sound.h - 

<h2>Synopsis</h2>#include 'SDL.h' 
 #include 'SDL_endian.h' 
 

<h3>Data Structures</h3>struct <b>Sound_AudioInfo</b> 
 <i>Information about an existing sample's format. </i> 
 struct <b>Sound_DecoderInfo</b> 
 <i>Information about available soudn decoders. </i> 
 struct <b>Sound_Sample</b> 
 <i>Represents sound data in the process of being decoded. </i> 
 struct <b>Sound_Version</b> 
 <i>Information the version of SDL_sound in use. </i>
<h3>Defines</h3>#define <b>SOUND_VERSION</b>(x) 
 <i>Macro to determine SDL_sound version program was compiled against. </i>
<h3>Enumerations</h3>enum <b>Sound_SampleFlags</b> { <b>SOUND_SAMPLEFLAG_NONE</b> = 0, <b>SOUND_SAMPLEFLAG_CANSEEK</b> = 1, <b>SOUND_SAMPLEFLAG_EOF</b> = 1 &lt;&lt; 29, <b>SOUND_SAMPLEFLAG_ERROR</b> = 1 &lt;&lt; 30, <b>SOUND_SAMPLEFLAG_EAGAIN</b> = 1 &lt;&lt; 31 } 
 <i>Flags that are used in a </i><b>Sound_Sample</b> to show various states.
<h3>Functions</h3>void <b>Sound_GetLinkedVersion</b> (<b>Sound_Version</b> *ver) 
 <i>Get the version of SDL_sound that is linked against your program. </i> 
 int <b>Sound_Init</b> (void) 
 <i>Initialize SDL_sound. </i> 
 int <b>Sound_Quit</b> (void) 
 <i>Shutdown SDL_sound. </i> 
 const <b>Sound_DecoderInfo</b> ** <b>Sound_AvailableDecoders</b> (void) 
 <i>Get a list of sound formats supported by this version of SDL_sound. </i> 
 const char * <b>Sound_GetError</b> (void) 
 <i>Get the last SDL_sound error message as a null-terminated string. </i> 
 void <b>Sound_ClearError</b> (void) 
 <i>Clear the current error message. </i> 
 <b>Sound_Sample</b> * <b>Sound_NewSample</b> (SDL_RWops *rw, const char *ext, <b>Sound_AudioInfo</b> *desired, Uint32 bufferSize) 
 <i>Start decoding a new sound sample. </i> 
 <b>Sound_Sample</b> * <b>Sound_NewSampleFromFile</b> (const char *fname, <b>Sound_AudioInfo</b> *desired, Uint32 bufferSize) 
 <i>Start decoding a new sound sample from a file on disk. </i> 
 void <b>Sound_FreeSample</b> (<b>Sound_Sample</b> *sample) 
 <i>Dispose of a </i><b>Sound_Sample</b>. 
 int <b>Sound_SetBufferSize</b> (<b>Sound_Sample</b> *sample, Uint32 new_size) 
 <i>Change the current buffer size for a sample. </i> 
 Uint32 <b>Sound_Decode</b> (<b>Sound_Sample</b> *sample) 
 <i>Decode more of the sound data in a </i><b>Sound_Sample</b>. 
 Uint32 <b>Sound_DecodeAll</b> (<b>Sound_Sample</b> *sample) 
 <i>Decode the remainder of the sound data in a </i><b>Sound_Sample</b>. 
 int <b>Sound_Rewind</b> (<b>Sound_Sample</b> *sample) 
 <i>Rewind a sample to the start. </i> 
 int <b>Sound_Seek</b> (<b>Sound_Sample</b> *sample, Uint32 ms) 
 <i>Seek to a different point in a sample. </i>
<h2>Detailed Description</h2><h2>Define Documentation</h2><h3>#define SOUND_VERSION(x)</h3><b>Value:</b> 

 <pre>{ (x)-&gt;major = SOUND_VER_MAJOR; (x)-&gt;minor = SOUND_VER_MINOR; (x)-&gt;patch = SOUND_VER_PATCH; }</pre>Macro to determine SDL_sound version program was compiled against. 

 This macro fills in a <b>Sound_Version</b> structure with the version of the library you compiled against. This is determined by what header the compiler uses. Note that if you dynamically linked the library, you might have a slightly newer or older version at runtime. That version can be determined with <b>Sound_GetLinkedVersion()</b>, which, unlike SOUND_VERSION, is not a macro. 

 <b>Parameters:</b>
<dl COMPACT><dd><i>x</i> A pointer to a <b>Sound_Version</b> struct to initialize.</dl>
 

 <b>See also:</b>
<dl COMPACT><dd><b>Sound_Version</b> 

 <b>Sound_GetLinkedVersion</b></dl><h2>Enumeration Type Documentation</h2><h3>enum <b>Sound_SampleFlags</b></h3>Flags that are used in a <b>Sound_Sample</b> to show various states. 

 To use: 

 <pre> if (sample-&gt;flags &amp; SOUND_SAMPLEFLAG_ERROR) { dosomething(); }</pre><b>See also:</b>
<dl COMPACT><dd>Sound_SampleNew 

 Sound_SampleNewFromFile 

 Sound_SampleDecode 

 Sound_SampleDecodeAll 

 Sound_SampleSeek</dl>
 

 

 

 <b>Enumerator: </b>
<dl COMPACT><dt><i>SOUND_SAMPLEFLAG_NONE </i>
<dd>No special attributes.
<dt><i>SOUND_SAMPLEFLAG_CANSEEK </i>
<dd>Sample can seek to arbitrary points.
<dt><i>SOUND_SAMPLEFLAG_EOF </i>
<dd>End of input stream.
<dt><i>SOUND_SAMPLEFLAG_ERROR </i>
<dd>Unrecoverable error.
<dt><i>SOUND_SAMPLEFLAG_EAGAIN </i>
<dd>Function would block, or temp error.</dl><h2>Function Documentation</h2><h3>const <b>Sound_DecoderInfo</b> ** Sound_AvailableDecoders (void)</h3>Get a list of sound formats supported by this version of SDL_sound. 

 This is for informational purposes only. Note that the extension listed is merely convention: if we list 'MP3', you can open an MPEG-1 Layer 3 audio file with an extension of 'XYZ', if you like. The file extensions are informational, and only required as a hint to choosing the correct decoder, since the sound data may not be coming from a file at all, thanks to the abstraction that an SDL_RWops provides. 

 The returned value is an array of pointers to <b>Sound_DecoderInfo</b> structures, with a NULL entry to signify the end of the list: 

 

 <pre> Sound_DecoderInfo **i;
 for (i = Sound_AvailableDecoders(); *i != NULL; i++)
 {
 printf('Supported sound format: [%s], which is [%s].,
 i-&gt;extension, i-&gt;description);
 // ...and other fields...
 }</pre>The return values are pointers to static internal memory, and should be considered READ ONLY, and never freed. 

 <b>Returns:</b>
<dl COMPACT><dd>READ ONLY Null-terminated array of READ ONLY structures.</dl>
 

 <b>See also:</b>
<dl COMPACT><dd><b>Sound_DecoderInfo</b></dl><h3>void Sound_ClearError (void)</h3>Clear the current error message. 

 The next call to <b>Sound_GetError()</b> after <b>Sound_ClearError()</b> will return NULL. 

 <b>See also:</b>
<dl COMPACT><dd><b>Sound_GetError</b></dl><h3>Uint32 Sound_Decode (<b>Sound_Sample</b> * sample)</h3>Decode more of the sound data in a <b>Sound_Sample</b>. 

 It will decode at most sample-&gt;buffer_size bytes into sample-&gt;buffer in the desired format, and return the number of decoded bytes. If sample-&gt;buffer_size bytes could not be decoded, then please refer to sample-&gt;flags to determine if this was an end-of-stream or error condition. 

 <b>Parameters:</b>
<dl COMPACT><dd><i>sample</i> Do more decoding to this <b>Sound_Sample</b>.</dl>
 

 <b>Returns:</b>
<dl COMPACT><dd>number of bytes decoded into sample-&gt;buffer. If it is less than sample-&gt;buffer_size, then you should check sample-&gt;flags to see what the current state of the sample is (EOF, error, read again).</dl>
 

 <b>See also:</b>
<dl COMPACT><dd><b>Sound_DecodeAll</b> 

 <b>Sound_SetBufferSize</b> 

 <b>Sound_Seek</b> 

 <b>Sound_Rewind</b></dl><h3>Uint32 Sound_DecodeAll (<b>Sound_Sample</b> * sample)</h3>Decode the remainder of the sound data in a <b>Sound_Sample</b>. 

 This will dynamically allocate memory for the ENTIRE remaining sample. sample-&gt;buffer_size and sample-&gt;buffer will be updated to reflect the new buffer. Please refer to sample-&gt;flags to determine if the decoding finished due to an End-of-stream or error condition. 

 Be aware that sound data can take a large amount of memory, and that this function may block for quite awhile while processing. Also note that a streaming source (for example, from a SDL_RWops that is getting fed from an Internet radio feed that doesn't end) may fill all available memory before giving up...be sure to use this on finite sound sources only! 

 When decoding the sample in its entirety, the work is done one buffer at a time. That is, sound is decoded in sample-&gt;buffer_size blocks, and appended to a continually-growing buffer until the decoding completes. That means that this function will need enough RAM to hold approximately sample-&gt;buffer_size bytes plus the complete decoded sample at most. The larger your buffer size, the less overhead this function needs, but beware the possibility of paging to disk. Best to make this user-configurable if the sample isn't specific and small. 

 <b>Parameters:</b>
<dl COMPACT><dd><i>sample</i> Do all decoding for this <b>Sound_Sample</b>.</dl>
 

 <b>Returns:</b>
<dl COMPACT><dd>number of bytes decoded into sample-&gt;buffer. You should check sample-&gt;flags to see what the current state of the sample is (EOF, error, read again).</dl>
 

 <b>See also:</b>
<dl COMPACT><dd><b>Sound_Decode</b> 

 <b>Sound_SetBufferSize</b></dl><h3>void Sound_FreeSample (<b>Sound_Sample</b> * sample)</h3>Dispose of a <b>Sound_Sample</b>. 

 This will also close/dispose of the SDL_RWops that was used at creation time, so there's no need to keep a reference to that around. The <b>Sound_Sample</b> pointer is invalid after this call, and will almost certainly result in a crash if you attempt to keep using it. 

 <b>Parameters:</b>
<dl COMPACT><dd><i>sample</i> The <b>Sound_Sample</b> to delete.</dl>
 

 <b>See also:</b>
<dl COMPACT><dd><b>Sound_NewSample</b> 

 <b>Sound_NewSampleFromFile</b></dl><h3>const char * Sound_GetError (void)</h3>Get the last SDL_sound error message as a null-terminated string. 

 This will be NULL if there's been no error since the last call to this function. The pointer returned by this call points to an internal buffer, and should not be deallocated. Each thread has a unique error state associated with it, but each time a new error message is set, it will overwrite the previous one associated with that thread. It is safe to call this function at anytime, even before <b>Sound_Init()</b>. 

 <b>Returns:</b>
<dl COMPACT><dd>READ ONLY string of last error message.</dl>
 

 <b>See also:</b>
<dl COMPACT><dd><b>Sound_ClearError</b></dl><h3>void Sound_GetLinkedVersion (<b>Sound_Version</b> * ver)</h3>Get the version of SDL_sound that is linked against your program. 

 If you are using a shared library (DLL) version of SDL_sound, then it is possible that it will be different than the version you compiled against. 

 This is a real function; the macro SOUND_VERSION tells you what version of SDL_sound you compiled against: 

 

 <pre> Sound_Version compiled;
 Sound_Version linked;
 SOUND_VERSION(&amp;compiled);
 Sound_GetLinkedVersion(&amp;linked);
 printf('We compiled against SDL_sound version %d.%d.%d ...,
 compiled.major, compiled.minor, compiled.patch);
 printf('But we linked against SDL_sound version %d.%d.%d.,
 linked.major, linked.minor, linked.patch);</pre>This function may be called safely at any time, even before <b>Sound_Init()</b>. 

 <b>Parameters:</b>
<dl COMPACT><dd><i>ver</i> <b>Sound_Version</b> structure to fill with shared library's version.</dl>
 

 <b>See also:</b>
<dl COMPACT><dd><b>Sound_Version</b> 

 <b>SOUND_VERSION</b></dl><h3>Sound_Init (void)</h3>Initialize SDL_sound. 

 This must be called before any other SDL_sound function (except perhaps <b>Sound_GetLinkedVersion()</b>). You should call SDL_Init() before calling this. <b>Sound_Init()</b> will attempt to call SDL_Init(SDL_INIT_AUDIO), just in case. This is a safe behaviour, but it may not configure SDL to your liking by itself. 

 <b>Returns:</b>
<dl COMPACT><dd>nonzero on success, zero on error. Specifics of the error can be gleaned from <b>Sound_GetError()</b>.</dl>
 

 <b>See also:</b>
<dl COMPACT><dd><b>Sound_Quit</b></dl><h3><b>Sound_Sample</b> * Sound_NewSample (SDL_RWops * rw, const char * ext, <b>Sound_AudioInfo</b> * desired, Uint32 bufferSize)</h3>Start decoding a new sound sample. 

 The data is read via an SDL_RWops structure (see SDL_rwops.h in the SDL include directory), so it may be coming from memory, disk, network stream, etc. The (ext) parameter is merely a hint to determining the correct decoder; if you specify, for example, 'mp3' for an extension, and one of the decoders lists that as a handled extension, then that decoder is given first shot at trying to claim the data for decoding. If none of the extensions match (or the extension is NULL), then every decoder examines the data to determine if it can handle it, until one accepts it. In such a case your SDL_RWops will need to be capable of rewinding to the start of the stream. 

 If no decoders can handle the data, a NULL value is returned, and a human readable error message can be fetched from <b>Sound_GetError()</b>. 

 Optionally, a desired audio format can be specified. If the incoming data is in a different format, SDL_sound will convert it to the desired format on the fly. Note that this can be an expensive operation, so it may be wise to convert data before you need to play it back, if possible, or make sure your data is initially in the format that you need it in. If you don't want to convert the data, you can specify NULL for a desired format. The incoming format of the data, preconversion, can be found in the <b>Sound_Sample</b> structure. 

 Note that the raw sound data 'decoder' needs you to specify both the extension 'RAW' and a 'desired' format, or it will refuse to handle the data. This is to prevent it from catching all formats unsupported by the other decoders. 

 Finally, specify an initial buffer size; this is the number of bytes that will be allocated to store each read from the sound buffer. The more you can safely allocate, the more decoding can be done in one block, but the more resources you have to use up, and the longer each decoding call will take. Note that different data formats require more or less space to store. This buffer can be resized via <b>Sound_SetBufferSize()</b> ... 

 The buffer size specified must be a multiple of the size of a single sample point. So, if you want 16-bit, stereo samples, then your sample point size is (2 channels * 16 bits), or 32 bits per sample, which is four bytes. In such a case, you could specify 128 or 132 bytes for a buffer, but not 129, 130, or 131 (although in reality, you'll want to specify a MUCH larger buffer). 

 When you are done with this <b>Sound_Sample</b> pointer, you can dispose of it via <b>Sound_FreeSample()</b>. 

 You do not have to keep a reference to (rw) around. If this function suceeds, it stores (rw) internally (and disposes of it during the call to <b>Sound_FreeSample()</b>). If this function fails, it will dispose of the SDL_RWops for you. 

 <b>Parameters:</b>
<dl COMPACT><dd><i>rw</i> SDL_RWops with sound data. 
 <i>ext</i> File extension normally associated with a data format. Can usually be NULL. 
 <i>desired</i> Format to convert sound data into. Can usually be NULL, if you don't need conversion. 
 <i>bufferSize</i> Size, in bytes, to allocate for the decoding buffer.</dl>
 

 <b>Returns:</b>
<dl COMPACT><dd><b>Sound_Sample</b> pointer, which is used as a handle to several other SDL_sound APIs. NULL on error. If error, use <b>Sound_GetError()</b> to see what went wrong.</dl>
 

 <b>See also:</b>
<dl COMPACT><dd><b>Sound_NewSampleFromFile</b> 

 <b>Sound_SetBufferSize</b> 

 <b>Sound_Decode</b> 

 <b>Sound_DecodeAll</b> 

 <b>Sound_Seek</b> 

 <b>Sound_Rewind</b> 

 <b>Sound_FreeSample</b></dl><h3><b>Sound_Sample</b> * Sound_NewSampleFromFile (const char * filename, <b>Sound_AudioInfo</b> * desired, Uint32 bufferSize)</h3>Start decoding a new sound sample from a file on disk. 

 This is identical to <b>Sound_NewSample()</b>, but it creates an SDL_RWops for you from the file located in (filename). Note that (filename) is specified in platform-dependent notation. ('C:\\music\\mysong.mp3' on windows, and '/home/icculus/music/mysong.mp3' or whatever on Unix, etc.) <b>Sound_NewSample()</b>'s 'ext' parameter is gleaned from the contents of (filename). 

 <b>Parameters:</b>
<dl COMPACT><dd><i>filename</i> file containing sound data. 
 <i>desired</i> Format to convert sound data into. Can usually be NULL, if you don't need conversion. 
 <i>bufferSize</i> size, in bytes, of initial read buffer.</dl>
 

 <b>Returns:</b>
<dl COMPACT><dd><b>Sound_Sample</b> pointer, which is used as a handle to several other SDL_sound APIs. NULL on error. If error, use <b>Sound_GetError()</b> to see what went wrong.</dl>
 

 <b>See also:</b>
<dl COMPACT><dd><b>Sound_NewSample</b> 

 <b>Sound_SetBufferSize</b> 

 <b>Sound_Decode</b> 

 <b>Sound_DecodeAll</b> 

 <b>Sound_Seek</b> 

 <b>Sound_Rewind</b> 

 <b>Sound_FreeSample</b></dl><h3>Sound_Quit (void)</h3>Shutdown SDL_sound. 

 This closes any SDL_RWops that were being used as sound sources, and frees any resources in use by SDL_sound. 

 All <b>Sound_Sample</b> pointers you had prior to this call are INVALIDATED. 

 Once successfully deinitialized, <b>Sound_Init()</b> can be called again to restart the subsystem. All default API states are restored at this point. 

 You should call this BEFORE SDL_Quit(). This will NOT call SDL_Quit() for you! 

 <b>Returns:</b>
<dl COMPACT><dd>nonzero on success, zero on error. Specifics of the error can be gleaned from <b>Sound_GetError()</b>. If failure, state of SDL_sound is undefined, and probably badly screwed up.</dl>
 

 <b>See also:</b>
<dl COMPACT><dd><b>Sound_Init</b></dl><h3>int Sound_Rewind (<b>Sound_Sample</b> * sample)</h3>Rewind a sample to the start. 

 Restart a sample at the start of its waveform data, as if newly created with <b>Sound_NewSample()</b>. If successful, the next call to Sound_Decode[All]() will give audio data from the earliest point in the stream. 

 Beware that this function will fail if the SDL_RWops that feeds the decoder can not be rewound via it's seek method, but this can theoretically be avoided by wrapping it in some sort of buffering SDL_RWops. 

 This function should ONLY fail if the RWops is not seekable, or SDL_sound is not initialized. Both can be controlled by the application, and thus, it is up to the developer's paranoia to dictate whether this function's return value need be checked at all. 

 If this function fails, the state of the sample is undefined, but it is still safe to call <b>Sound_FreeSample()</b> to dispose of it. 

 On success, ERROR, EOF, and EAGAIN are cleared from sample-&gt;flags. The ERROR flag is set on error. 

 <b>Parameters:</b>
<dl COMPACT><dd><i>sample</i> The <b>Sound_Sample</b> to rewind.</dl>
 

 <b>Returns:</b>
<dl COMPACT><dd>nonzero on success, zero on error. Specifics of the error can be gleaned from <b>Sound_GetError()</b>.</dl>
 

 <b>See also:</b>
<dl COMPACT><dd><b>Sound_Seek</b></dl><h3>int Sound_Seek (<b>Sound_Sample</b> * sample, Uint32 ms)</h3>Seek to a different point in a sample. 

 Reposition a sample's stream. If successful, the next call to Sound_Decode[All]() will give audio data from the offset you specified. 

 The offset is specified in milliseconds from the start of the sample. 

 Beware that this function can fail for several reasons. If the SDL_RWops that feeds the decoder can not seek, this call will almost certainly fail, but this can theoretically be avoided by wrapping it in some sort of buffering SDL_RWops. Some decoders can never seek, others can only seek with certain files. The decoders will set a flag in the sample at creation time to help you determine this. 

 You should check sample-&gt;flags &amp; SOUND_SAMPLEFLAG_CANSEEK before attempting. <b>Sound_Seek()</b> reports failure immediately if this flag isn't set. This function can still fail for other reasons if the flag is set. 

 This function can be emulated in the application with <b>Sound_Rewind()</b> and predecoding a specific amount of the sample, but this can be extremely inefficient. <b>Sound_Seek()</b> accelerates the seek on a with decoder-specific code. 

 If this function fails, the sample should continue to function as if this call was never made. If there was an unrecoverable error, sample-&gt;flags &amp; SOUND_SAMPLEFLAG_ERROR will be set, which you regular decoding loop can pick up. 

 On success, ERROR, EOF, and EAGAIN are cleared from sample-&gt;flags. 

 <b>Parameters:</b>
<dl COMPACT><dd><i>sample</i> The <b>Sound_Sample</b> to seek. 
 <i>ms</i> The new position, in milliseconds from start of sample.</dl>
 

 <b>Returns:</b>
<dl COMPACT><dd>nonzero on success, zero on error. Specifics of the error can be gleaned from <b>Sound_GetError()</b>.</dl>
 

 <b>See also:</b>
<dl COMPACT><dd><b>Sound_Rewind</b></dl><h3>int Sound_SetBufferSize (<b>Sound_Sample</b> * sample, Uint32 new_size)</h3>Change the current buffer size for a sample. 

 If the buffer size could be changed, then the sample-&gt;buffer and sample-&gt;buffer_size fields will reflect that. If they could not be changed, then your original sample state is preserved. If the buffer is shrinking, the data at the end of buffer is truncated. If the buffer is growing, the contents of the new space at the end is undefined until you decode more into it or initialize it yourself. 

 The buffer size specified must be a multiple of the size of a single sample point. So, if you want 16-bit, stereo samples, then your sample point size is (2 channels * 16 bits), or 32 bits per sample, which is four bytes. In such a case, you could specify 128 or 132 bytes for a buffer, but not 129, 130, or 131 (although in reality, you'll want to specify a MUCH larger buffer). 

 <b>Parameters:</b>
<dl COMPACT><dd><i>sample</i> The <b>Sound_Sample</b> whose buffer to modify. 
 <i>new_size</i> The desired size, in bytes, of the new buffer.</dl>
 

 <b>Returns:</b>
<dl COMPACT><dd>non-zero if buffer size changed, zero on failure.</dl>
 

 <b>See also:</b>
<dl COMPACT><dd><b>Sound_Decode</b> 

 <b>Sound_DecodeAll</b></dl><h2>Author</h2>Generated automatically by Doxygen for SDL_sound from the source code.
