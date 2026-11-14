---
title: "antlr3_int_stream_struct(3)"
name: "antlr3_int_stream_struct"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3_int_stream_struct/"
description: "ANTLR3_INT_STREAM_struct –"
---

<p>ANTLR3_INT_STREAM_struct &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3intstream.h">antlr3intstream.h</a>&gt;</p>
<h3>Data Fields</h3>
<p><code>ANTLR3_UINT32</code>(* <code>_LA</code> )(struct <code>ANTLR3_INT_STREAM_struct</code> *intStream, <code>ANTLR3_INT32</code> i)<br />
 <i>Get ANTLR3_UINT32 at current input pointer + i ahead where i=1 is next ANTLR3_UINT32. </i><br />
 <code>ANTLR3_UINT32</code> <code>cachedSize</code><br />
 <i>Because the indirect call, though small in individual cases can mount up if there are thousands of tokens (very large input streams), callers of size can optionally use this cached size field. </i><br />
 void(* <code>consume</code> )(struct <code>ANTLR3_INT_STREAM_struct</code> *intStream)<br />
 <i>Consume the next &#8216;ANTR3_UINT32&#8217; in the stream. </i><br />
 void(* <code>free</code> )(struct <code>ANTLR3_INT_STREAM_struct</code> *stream)<br />
 <i>Frees any resources that were allocated for the implementation of this interface. </i><br />
 <code>pANTLR3_STRING</code>(* <code>getSourceName</code> )(struct <code>ANTLR3_INT_STREAM_struct</code> *intStream) </p>
<p> <code>ANTLR3_MARKER</code>(* <code>index</code> )(struct <code>ANTLR3_INT_STREAM_struct</code> *intStream)<br />
 <i>Return the current input symbol index 0..n where n indicates the last symbol has been read. </i><br />
 <code>ANTLR3_MARKER</code> <code>lastMarker</code><br />
 <i>Last marker position allocated. </i><br />
 <code>ANTLR3_MARKER</code>(* <code>mark</code> )(struct <code>ANTLR3_INT_STREAM_struct</code> *intStream)<br />
 <i>Tell the stream to start buffering if it hasn&#8217;t already. </i><br />
 void(* <code>release</code> )(struct <code>ANTLR3_INT_STREAM_struct</code> *intStream, <code>ANTLR3_MARKER</code> <code>mark</code>)<br />
 <i>You may want to commit to a backtrack but don&#8217;t want to force the stream to keep bookkeeping objects around for a marker that is no longer necessary. </i><br />
 void(* <code>rewind</code> )(struct <code>ANTLR3_INT_STREAM_struct</code> *intStream, <code>ANTLR3_MARKER</code> marker)<br />
 <i>Reset the stream so that next call to index would return marker. </i><br />
 void(* <code>rewindLast</code> )(struct <code>ANTLR3_INT_STREAM_struct</code> *intStream)<br />
 <i>Reset the stream to the last marker position, witouh destryoing the last marker position. </i><br />
 void(* <code>seek</code> )(struct <code>ANTLR3_INT_STREAM_struct</code> *intStream, <code>ANTLR3_MARKER</code> <code>index</code>)<br />
 <i>Set the input cursor to the position indicated by index. </i><br />
 <code>ANTLR3_UINT32</code>(* <code>size</code> )(struct <code>ANTLR3_INT_STREAM_struct</code> *intStream)<br />
 <i>Only makes sense for streams that buffer everything up probably, but might be useful to display the entire stream or for testing. </i><br />
 <code>pANTLR3_STRING</code> <code>streamName</code><br />
 <i>Potentially useful in error reporting and so on, this string is an identification of the input source. </i><br />
 void * <code>super</code><br />
 <i>Pointer to the super structure that contains this interface. </i><br />
 <code>ANTLR3_UINT32</code> <code>type</code><br />
 <i>Input stream type indicator. </i></p>
<h2>Field Documentation</h2>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_INT_STREAM_struct::_LA</code>)(struct <code>ANTLR3_INT_STREAM_struct</code> *intStream, <code>ANTLR3_INT32</code> i)</h3>
<p>Get ANTLR3_UINT32 at current input pointer + i ahead where i=1 is next ANTLR3_UINT32. </p>
<p> Referenced by antlr3AsciiLT(), antlr3AsciiSetUcaseLA(), antlr3CommonTokenDebugStreamSourceNew(), antlr3CommonTokenStreamNew(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), antlr3dfapredict(), antlr3GenericSetupStream(), antlr3RecognitionExceptionNew(), antlr3UCS2SetupStream(), consumeUntil(), consumeUntilSet(), match(), matchc(), matchRange(), matchs(), mismatchIsMissingToken(), mismatchIsUnwantedToken(), nextTokenStr(), recoverFromMismatchedElement(), and setDebugListener().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_INT_STREAM_struct::cachedSize</code></h3>
<p>Because the indirect call, though small in individual cases can mount up if there are thousands of tokens (very large input streams), callers of size can optionally use this cached size field. </p>
<p> Referenced by tokLT().</p>
<h3>void(* <code>ANTLR3_INT_STREAM_struct::consume</code>)(struct <code>ANTLR3_INT_STREAM_struct</code> *intStream)</h3>
<p>Consume the next &#8216;ANTR3_UINT32&#8217; in the stream. </p>
<p> Referenced by antlr3AsciiSeek(), antlr3CommonTokenDebugStreamSourceNew(), antlr3CommonTokenStreamNew(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), antlr3dfapredict(), antlr3GenericSetupStream(), antlr3UCS2Seek(), antlr3UCS2SetupStream(), consumeUntil(), consumeUntilSet(), match(), matchAny(), matchc(), matchRange(), matchs(), recover(), recoverFromMismatchedToken(), and setDebugListener().</p>
<h3>void(* <code>ANTLR3_INT_STREAM_struct::free</code>)(struct <code>ANTLR3_INT_STREAM_struct</code> *stream)</h3>
<p>Frees any resources that were allocated for the implementation of this interface. Usually this is just releasing the memory allocated for the structure itself, but it may of course do anything it need to so long as it does not stamp on anything else. </p>
<p> Referenced by antlr3CommonTreeNodeStreamFree(), antlr3CTSFree(), antlr3InputClose(), and antlr3IntStreamNew().</p>
<h3><code>pANTLR3_STRING</code>(* <code>ANTLR3_INT_STREAM_struct::getSourceName</code>)(struct <code>ANTLR3_INT_STREAM_struct</code> *intStream)</h3>
<p>Referenced by antlr3CommonTokenStreamNew(), and antlr3GenericSetupStream().</p>
<h3><code>ANTLR3_MARKER</code>(* <code>ANTLR3_INT_STREAM_struct::index</code>)(struct <code>ANTLR3_INT_STREAM_struct</code> *intStream)</h3>
<p>Return the current input symbol index 0..n where n indicates the last symbol has been read. </p>
<p> Referenced by alreadyParsedRule(), antlr3CommonTokenStreamNew(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), antlr3GenericSetupStream(), antlr3RecognitionExceptionNew(), antlr3UCS2SetupStream(), consumeInitialHiddenTokens(), dbgConsume(), getCharIndex(), memoize(), nextTokenStr(), recover(), and tokLT().</p>
<h3><code>ANTLR3_MARKER</code> <code>ANTLR3_INT_STREAM_struct::lastMarker</code></h3>
<p>Last marker position allocated. </p>
<p> Referenced by antlr3AsciiMark(), antlr3AsciiRewindLast(), and reset().</p>
<h3><code>ANTLR3_MARKER</code>(* <code>ANTLR3_INT_STREAM_struct::mark</code>)(struct <code>ANTLR3_INT_STREAM_struct</code> *intStream)</h3>
<p>Tell the stream to start buffering if it hasn&#8217;t already. Return current input position, <code>index()</code>, or some other marker so that when passed to <code>rewind()</code> you get back to the same spot. rewind(<code>mark()</code>) should not affect the input cursor. </p>
<p> Referenced by antlr3CommonTokenDebugStreamSourceNew(), antlr3CommonTokenStreamNew(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), antlr3dfapredict(), antlr3GenericSetupStream(), pushCharStream(), setDebugListener(), and synpred().</p>
<h3>void(* <code>ANTLR3_INT_STREAM_struct::release</code>)(struct <code>ANTLR3_INT_STREAM_struct</code> *intStream, <code>ANTLR3_MARKER</code> <code>mark</code>)</h3>
<p>You may want to commit to a backtrack but don&#8217;t want to force the stream to keep bookkeeping objects around for a marker that is no longer necessary. This will have the same behavior as <code>rewind()</code> except it releases resources without the backward seek. </p>
<p> Referenced by antlr3AsciiRewind(), antlr3CommonTokenStreamNew(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), and antlr3GenericSetupStream().</p>
<h3>void(* <code>ANTLR3_INT_STREAM_struct::rewind</code>)(struct <code>ANTLR3_INT_STREAM_struct</code> *intStream, <code>ANTLR3_MARKER</code> marker)</h3>
<p>Reset the stream so that next call to index would return marker. The marker will usually be <code>index()</code> but it doesn&#8217;t have to be. It&#8217;s just a marker to indicate what state the stream was in. This is essentially calling <code>release()</code> and <code>seek()</code>. If there are markers created after this marker argument, this routine must unroll them like a stack. Assume the state the stream was in when this marker was created. </p>
<p> Referenced by antlr3AsciiRewindLast(), antlr3CommonTokenDebugStreamSourceNew(), antlr3CommonTokenStreamNew(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), antlr3dfapredict(), antlr3GenericSetupStream(), setDebugListener(), and synpred().</p>
<h3>void(* <code>ANTLR3_INT_STREAM_struct::rewindLast</code>)(struct <code>ANTLR3_INT_STREAM_struct</code> *intStream)</h3>
<p>Reset the stream to the last marker position, witouh destryoing the last marker position. </p>
<p> Referenced by antlr3CommonTokenDebugStreamSourceNew(), antlr3CommonTokenStreamNew(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), antlr3GenericSetupStream(), popCharStream(), and setDebugListener().</p>
<h3>void(* <code>ANTLR3_INT_STREAM_struct::seek</code>)(struct <code>ANTLR3_INT_STREAM_struct</code> *intStream, <code>ANTLR3_MARKER</code> <code>index</code>)</h3>
<p>Set the input cursor to the position indicated by index. This is normally used to seek ahead in the input stream. No buffering is required to do this unless you know your stream will use seek to move backwards such as when backtracking. </p>
<p> This is different from rewind in its multi-directional requirement and in that its argument is strictly an input cursor (index). </p>
<p> For char streams, seeking forward must update the stream state such as line number. For seeking backwards, you will be presumably backtracking using the mark/rewind mechanism that restores state and so this method does not need to update state when seeking backwards. </p>
<p> Currently, this method is only used for efficient backtracking, but in the future it may be used for incremental parsing. </p>
<p> Referenced by alreadyParsedRule(), antlr3CommonTokenDebugStreamSourceNew(), antlr3CommonTokenStreamNew(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), antlr3GenericSetupStream(), antlr3UCS2SetupStream(), reset(), and setDebugListener().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_INT_STREAM_struct::size</code>)(struct <code>ANTLR3_INT_STREAM_struct</code> *intStream)</h3>
<p>Only makes sense for streams that buffer everything up probably, but might be useful to display the entire stream or for testing. </p>
<p> Referenced by antlr3CommonTokenStreamNew(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), getTokensSet(), toString(), and toStringSS().</p>
<h3><code>pANTLR3_STRING</code> <code>ANTLR3_INT_STREAM_struct::streamName</code></h3>
<p>Potentially useful in error reporting and so on, this string is an identification of the input source. It may be NULL, so anything attempting to access it needs to check this and substitute a sensible default. </p>
<p> Referenced by antlr3AsciiFileStreamNew(), antlr3AsciiGetSourceName(), antlr3NewAsciiStringCopyStream(), antlr3NewAsciiStringInPlaceStream(), and antlr3NewUCS2StringInPlaceStream().</p>
<h3>void* <code>ANTLR3_INT_STREAM_struct::super</code></h3>
<p>Pointer to the super structure that contains this interface. This will usually be a token stream or a tree stream. </p>
<p> Referenced by antlr3AsciiConsume(), antlr3AsciiIndex(), antlr3AsciiLA(), antlr3AsciiLA_ucase(), antlr3AsciiMark(), antlr3AsciiRelease(), antlr3AsciiRewind(), antlr3AsciiSeek(), antlr3CommonTokenStreamNew(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), antlr3CTSFree(), antlr3GenericSetupStream(), antlr3UCS2Consume(), antlr3UCS2Index(), antlr3UCS2LA(), antlr3UCS2Seek(), consume(), consumeInitialHiddenTokens(), dbgConsume(), getCurrentInputSymbol(), and getMissingSymbol().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_INT_STREAM_struct::type</code></h3>
<p>Input stream type indicator. Sometimes useful for error reporting etc. </p>
<p> Referenced by antlr3CommonTokenStreamNew(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), antlr3GenericSetupStream(), and antlr3RecognitionExceptionNew(). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
