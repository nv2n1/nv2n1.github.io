---
title: "antlr3-tostring(3)"
name: "antlr3-tostring"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-tostring/"
description: "src/antlr3commontoken.c –"
---

<p>src/antlr3commontoken.c &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3.h">antlr3.h</a>&gt; </p>
<h3>Functions</h3>
<p>ANTLR3_API <code>pANTLR3_COMMON_TOKEN</code> <code>antlr3CommonTokenNew</code> (<code>ANTLR3_UINT32</code> ttype) </p>
<p> ANTLR3_API void <code>antlr3SetTokenAPI</code> (<code>pANTLR3_COMMON_TOKEN</code> token) </p>
<p> ANTLR3_API <code>pANTLR3_TOKEN_FACTORY</code> <code>antlr3TokenFactoryNew</code> (<code>pANTLR3_INPUT_STREAM</code> input) </p>
<p> static void <code>factoryClose</code> (<code>pANTLR3_TOKEN_FACTORY</code> factory) </p>
<p> static <code>ANTLR3_UINT32</code> <code>getChannel</code> (<code>pANTLR3_COMMON_TOKEN</code> token) </p>
<p> static <code>ANTLR3_INT32</code> <code>getCharPositionInLine</code> (<code>pANTLR3_COMMON_TOKEN</code> token) </p>
<p> static <code>ANTLR3_UINT32</code> <code>getLine</code> (<code>pANTLR3_COMMON_TOKEN</code> token) </p>
<p> static <code>ANTLR3_MARKER</code> <code>getStartIndex</code> (<code>pANTLR3_COMMON_TOKEN</code> token) </p>
<p> static <code>ANTLR3_MARKER</code> <code>getStopIndex</code> (<code>pANTLR3_COMMON_TOKEN</code> token) </p>
<p> static <code>pANTLR3_STRING</code> <code>getText</code> (<code>pANTLR3_COMMON_TOKEN</code> token)<br />
 <i>Contains the default implementation of the common token used within java. </i><br />
 static <code>ANTLR3_MARKER</code> <code>getTokenIndex</code> (<code>pANTLR3_COMMON_TOKEN</code> token) </p>
<p> static <code>ANTLR3_UINT32</code> <code>getType</code> (<code>pANTLR3_COMMON_TOKEN</code> token) </p>
<p> static void <code>newPool</code> (<code>pANTLR3_TOKEN_FACTORY</code> factory) </p>
<p> static <code>pANTLR3_COMMON_TOKEN</code> <code>newPoolToken</code> (<code>pANTLR3_TOKEN_FACTORY</code> factory) </p>
<p> static <code>pANTLR3_COMMON_TOKEN</code> <code>newToken</code> (void) </p>
<p> static void <code>setChannel</code> (<code>pANTLR3_COMMON_TOKEN</code> token, <code>ANTLR3_UINT32</code> channel) </p>
<p> static void <code>setCharPositionInLine</code> (<code>pANTLR3_COMMON_TOKEN</code> token, <code>ANTLR3_INT32</code> pos) </p>
<p> static void <code>setInputStream</code> (<code>pANTLR3_TOKEN_FACTORY</code> factory, <code>pANTLR3_INPUT_STREAM</code> input) </p>
<p> static void <code>setLine</code> (<code>pANTLR3_COMMON_TOKEN</code> token, <code>ANTLR3_UINT32</code> line) </p>
<p> static void <code>setStartIndex</code> (<code>pANTLR3_COMMON_TOKEN</code> token, <code>ANTLR3_MARKER</code> index) </p>
<p> static void <code>setStopIndex</code> (<code>pANTLR3_COMMON_TOKEN</code> token, <code>ANTLR3_MARKER</code> index) </p>
<p> static void <code>setText</code> (<code>pANTLR3_COMMON_TOKEN</code> token, <code>pANTLR3_STRING</code> text)<br />
 <i>Install the supplied text string as teh text for the token. </i><br />
 static void <code>setText8</code> (<code>pANTLR3_COMMON_TOKEN</code> token, <code>pANTLR3_UINT8</code> text) </p>
<p> static void <code>setTokenIndex</code> (<code>pANTLR3_COMMON_TOKEN</code> token, <code>ANTLR3_MARKER</code>) </p>
<p> static void <code>setType</code> (<code>pANTLR3_COMMON_TOKEN</code> token, <code>ANTLR3_UINT32</code> type) </p>
<p> static <code>pANTLR3_STRING</code> <code>toString</code> (<code>pANTLR3_COMMON_TOKEN</code> token) </p>
<h2>Function Documentation</h2>
<h3>ANTLR3_API <code>pANTLR3_COMMON_TOKEN</code> antlr3CommonTokenNew (<code>ANTLR3_UINT32</code> ttype)</h3>
<p>References newToken(), and ANTLR3_COMMON_TOKEN_struct::setType. </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew().</p>
<h3>ANTLR3_API void antlr3SetTokenAPI (<code>pANTLR3_COMMON_TOKEN</code> token)</h3>
<p>References ANTLR3_TEXT_NONE, ANTLR3_TOKEN_DEFAULT_CHANNEL, ANTLR3_TOKEN_INVALID, ANTLR3_COMMON_TOKEN_struct::channel, ANTLR3_COMMON_TOKEN_struct::custom, ANTLR3_COMMON_TOKEN_struct::freeCustom, getChannel(), ANTLR3_COMMON_TOKEN_struct::getChannel, getCharPositionInLine(), ANTLR3_COMMON_TOKEN_struct::getCharPositionInLine, getLine(), ANTLR3_COMMON_TOKEN_struct::getLine, getStartIndex(), ANTLR3_COMMON_TOKEN_struct::getStartIndex, getStopIndex(), ANTLR3_COMMON_TOKEN_struct::getStopIndex, getText(), ANTLR3_COMMON_TOKEN_struct::getText, getTokenIndex(), ANTLR3_COMMON_TOKEN_struct::getTokenIndex, getType(), ANTLR3_COMMON_TOKEN_struct::getType, ANTLR3_COMMON_TOKEN_struct::index, ANTLR3_COMMON_TOKEN_struct::input, ANTLR3_COMMON_TOKEN_struct::line, setChannel(), ANTLR3_COMMON_TOKEN_struct::setChannel, setCharPositionInLine(), ANTLR3_COMMON_TOKEN_struct::setCharPositionInLine, setLine(), ANTLR3_COMMON_TOKEN_struct::setLine, setStartIndex(), ANTLR3_COMMON_TOKEN_struct::setStartIndex, setStopIndex(), ANTLR3_COMMON_TOKEN_struct::setStopIndex, setText(), ANTLR3_COMMON_TOKEN_struct::setText, setText8(), ANTLR3_COMMON_TOKEN_struct::setText8, setTokenIndex(), ANTLR3_COMMON_TOKEN_struct::setTokenIndex, setType(), ANTLR3_COMMON_TOKEN_struct::setType, ANTLR3_COMMON_TOKEN_struct::start, ANTLR3_COMMON_TOKEN_struct::stop, ANTLR3_COMMON_TOKEN_struct::textState, toString(), ANTLR3_COMMON_TOKEN_struct::toString, ANTLR3_COMMON_TOKEN_struct::type, ANTLR3_COMMON_TOKEN_struct::user1, ANTLR3_COMMON_TOKEN_struct::user2, and ANTLR3_COMMON_TOKEN_struct::user3. </p>
<p> Referenced by antlr3LexerNew(), antlr3TokenFactoryNew(), newPoolToken(), and newToken().</p>
<h3>ANTLR3_API <code>pANTLR3_TOKEN_FACTORY</code> antlr3TokenFactoryNew (<code>pANTLR3_INPUT_STREAM</code> input)</h3>
<p>References ANTLR3_MALLOC, ANTLR3_TRUE, antlr3SetTokenAPI(), ANTLR3_TOKEN_FACTORY_struct::close, factoryClose(), ANTLR3_COMMON_TOKEN_struct::factoryMade, newPool(), newPoolToken(), ANTLR3_TOKEN_FACTORY_struct::newToken, ANTLR3_TOKEN_FACTORY_struct::pools, setInputStream(), ANTLR3_TOKEN_FACTORY_struct::setInputStream, ANTLR3_TOKEN_FACTORY_struct::thisPool, and ANTLR3_TOKEN_FACTORY_struct::unTruc. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew(), getMissingSymbol(), and setCharStream().</p>
<h3>static void factoryClose (<code>pANTLR3_TOKEN_FACTORY</code> factory) [static]</h3>
<p>References ANTLR3_FACTORY_POOL_SIZE, ANTLR3_FREE, ANTLR3_COMMON_TOKEN_struct::custom, ANTLR3_COMMON_TOKEN_struct::freeCustom, ANTLR3_TOKEN_FACTORY_struct::nextToken, ANTLR3_TOKEN_FACTORY_struct::pools, and ANTLR3_TOKEN_FACTORY_struct::thisPool. </p>
<p> Referenced by antlr3TokenFactoryNew().</p>
<h3>static <code>ANTLR3_UINT32</code> getChannel (<code>pANTLR3_COMMON_TOKEN</code> token) [static]</h3>
<p>References ANTLR3_COMMON_TOKEN_struct::channel. </p>
<p> Referenced by antlr3SetTokenAPI().</p>
<h3>static <code>ANTLR3_INT32</code> getCharPositionInLine (<code>pANTLR3_COMMON_TOKEN</code> token) [static]</h3>
<p>References ANTLR3_COMMON_TOKEN_struct::charPosition. </p>
<p> Referenced by antlr3SetTokenAPI().</p>
<h3>static <code>ANTLR3_UINT32</code> getLine (<code>pANTLR3_COMMON_TOKEN</code> token) [static]</h3>
<p>References ANTLR3_COMMON_TOKEN_struct::line. </p>
<p> Referenced by antlr3SetTokenAPI().</p>
<h3>static <code>ANTLR3_MARKER</code> getStartIndex (<code>pANTLR3_COMMON_TOKEN</code> token) [static]</h3>
<p>References ANTLR3_INPUT_STREAM_struct::data, ANTLR3_COMMON_TOKEN_struct::input, and ANTLR3_COMMON_TOKEN_struct::start. </p>
<p> Referenced by antlr3SetTokenAPI().</p>
<h3>static <code>ANTLR3_MARKER</code> getStopIndex (<code>pANTLR3_COMMON_TOKEN</code> token) [static]</h3>
<p>References ANTLR3_COMMON_TOKEN_struct::stop. </p>
<p> Referenced by antlr3SetTokenAPI().</p>
<h3>static <code>pANTLR3_STRING</code> getText (<code>pANTLR3_COMMON_TOKEN</code> token) [static]</h3>
<p>Contains the default implementation of the common token used within java. Custom tokens should create this structure and then append to it using the custom pointer to install their own structure and API. </p>
<p> References ANTLR3_TEXT_CHARP, ANTLR3_TEXT_STRING, ANTLR3_TOKEN_EOF, ANTLR3_COMMON_TOKEN_struct::chars, ANTLR3_COMMON_TOKEN_struct::getStartIndex, ANTLR3_COMMON_TOKEN_struct::getStopIndex, ANTLR3_COMMON_TOKEN_struct::input, ANTLR3_STRING_FACTORY_struct::newStr8, ANTLR3_COMMON_TOKEN_struct::strFactory, ANTLR3_INPUT_STREAM_struct::substr, ANTLR3_COMMON_TOKEN_struct::text, ANTLR3_COMMON_TOKEN_struct::textState, ANTLR3_COMMON_TOKEN_struct::tokText, and ANTLR3_COMMON_TOKEN_struct::type. </p>
<p> Referenced by antlr3SetTokenAPI().</p>
<h3>static <code>ANTLR3_MARKER</code> getTokenIndex (<code>pANTLR3_COMMON_TOKEN</code> token) [static]</h3>
<p>References ANTLR3_COMMON_TOKEN_struct::index. </p>
<p> Referenced by antlr3SetTokenAPI().</p>
<h3>static <code>ANTLR3_UINT32</code> getType (<code>pANTLR3_COMMON_TOKEN</code> token) [static]</h3>
<p>References ANTLR3_COMMON_TOKEN_struct::type. </p>
<p> Referenced by antlr3SetTokenAPI().</p>
<h3>static void newPool (<code>pANTLR3_TOKEN_FACTORY</code> factory) [static]</h3>
<p>References ANTLR3_FACTORY_POOL_SIZE, ANTLR3_MALLOC, ANTLR3_REALLOC, ANTLR3_TOKEN_FACTORY_struct::nextToken, ANTLR3_TOKEN_FACTORY_struct::pools, and ANTLR3_TOKEN_FACTORY_struct::thisPool. </p>
<p> Referenced by antlr3TokenFactoryNew(), and newPoolToken().</p>
<h3>static <code>pANTLR3_COMMON_TOKEN</code> newPoolToken (<code>pANTLR3_TOKEN_FACTORY</code> factory) [static]</h3>
<p>References ANTLR3_FACTORY_POOL_SIZE, ANTLR3_TRUE, antlr3SetTokenAPI(), ANTLR3_COMMON_TOKEN_struct::factoryMade, ANTLR3_COMMON_TOKEN_struct::input, ANTLR3_TOKEN_FACTORY_struct::input, newPool(), ANTLR3_TOKEN_FACTORY_struct::nextToken, ANTLR3_TOKEN_FACTORY_struct::pools, ANTLR3_INPUT_STREAM_struct::strFactory, ANTLR3_COMMON_TOKEN_struct::strFactory, and ANTLR3_TOKEN_FACTORY_struct::thisPool. </p>
<p> Referenced by antlr3TokenFactoryNew().</p>
<h3>static <code>pANTLR3_COMMON_TOKEN</code> newToken (void) [static]</h3>
<p>References ANTLR3_FALSE, ANTLR3_MALLOC, antlr3SetTokenAPI(), and ANTLR3_COMMON_TOKEN_struct::factoryMade. </p>
<p> Referenced by antlr3CommonTokenNew(), createToken(), and createTokenFromToken().</p>
<h3>static void setChannel (<code>pANTLR3_COMMON_TOKEN</code> token, <code>ANTLR3_UINT32</code> channel) [static]</h3>
<p>References ANTLR3_COMMON_TOKEN_struct::channel. </p>
<p> Referenced by antlr3SetTokenAPI().</p>
<h3>static void setCharPositionInLine (<code>pANTLR3_COMMON_TOKEN</code> token, <code>ANTLR3_INT32</code> pos) [static]</h3>
<p>References ANTLR3_COMMON_TOKEN_struct::charPosition. </p>
<p> Referenced by antlr3SetTokenAPI().</p>
<h3>static void setInputStream (<code>pANTLR3_TOKEN_FACTORY</code> factory, <code>pANTLR3_INPUT_STREAM</code> input) [static]</h3>
<p>References ANTLR3_COMMON_TOKEN_struct::input, ANTLR3_TOKEN_FACTORY_struct::input, ANTLR3_INPUT_STREAM_struct::strFactory, ANTLR3_COMMON_TOKEN_struct::strFactory, and ANTLR3_TOKEN_FACTORY_struct::unTruc. </p>
<p> Referenced by antlr3TokenFactoryNew().</p>
<h3>static void setLine (<code>pANTLR3_COMMON_TOKEN</code> token, <code>ANTLR3_UINT32</code> line) [static]</h3>
<p>References ANTLR3_COMMON_TOKEN_struct::line. </p>
<p> Referenced by antlr3SetTokenAPI().</p>
<h3>static void setStartIndex (<code>pANTLR3_COMMON_TOKEN</code> token, <code>ANTLR3_MARKER</code> index) [static]</h3>
<p>References ANTLR3_COMMON_TOKEN_struct::start. </p>
<p> Referenced by antlr3SetTokenAPI().</p>
<h3>static void setStopIndex (<code>pANTLR3_COMMON_TOKEN</code> token, <code>ANTLR3_MARKER</code> index) [static]</h3>
<p>References ANTLR3_COMMON_TOKEN_struct::stop. </p>
<p> Referenced by antlr3SetTokenAPI().</p>
<h3>static void setText (<code>pANTLR3_COMMON_TOKEN</code> token, <code>pANTLR3_STRING</code> text) [static]</h3>
<p>Install the supplied text string as teh text for the token. The method assumes that the existing text (if any) was created by a factory and so does not attempt to release any memory it is using.Text not created by a string fctory (not advised) should be released prior to this call. </p>
<p> References ANTLR3_TEXT_STRING, ANTLR3_COMMON_TOKEN_struct::text, ANTLR3_COMMON_TOKEN_struct::textState, and ANTLR3_COMMON_TOKEN_struct::tokText. </p>
<p> Referenced by antlr3SetTokenAPI().</p>
<h3>static void setText8 (<code>pANTLR3_COMMON_TOKEN</code> token, <code>pANTLR3_UINT8</code> text) [static]</h3>
<p>References ANTLR3_TEXT_CHARP, ANTLR3_TEXT_NONE, ANTLR3_COMMON_TOKEN_struct::chars, ANTLR3_STRING_struct::set8, ANTLR3_COMMON_TOKEN_struct::text, ANTLR3_COMMON_TOKEN_struct::textState, and ANTLR3_COMMON_TOKEN_struct::tokText. </p>
<p> Referenced by antlr3SetTokenAPI().</p>
<h3>static void setTokenIndex (<code>pANTLR3_COMMON_TOKEN</code> token, <code>ANTLR3_MARKER</code> index) [static]</h3>
<p>References ANTLR3_COMMON_TOKEN_struct::index. </p>
<p> Referenced by antlr3SetTokenAPI().</p>
<h3>static void setType (<code>pANTLR3_COMMON_TOKEN</code> token, <code>ANTLR3_UINT32</code> type) [static]</h3>
<p>References ANTLR3_COMMON_TOKEN_struct::type. </p>
<p> Referenced by antlr3SetTokenAPI().</p>
<h3>static <code>pANTLR3_STRING</code> toString (<code>pANTLR3_COMMON_TOKEN</code> token) [static]</h3>
<p>References ANTLR3_STRING_struct::addc, ANTLR3_STRING_struct::addi, ANTLR3_TOKEN_DEFAULT_CHANNEL, ANTLR3_STRING_struct::append8, ANTLR3_STRING_struct::appendS, ANTLR3_STRING_struct::factory, ANTLR3_COMMON_TOKEN_struct::getChannel, ANTLR3_COMMON_TOKEN_struct::getCharPositionInLine, ANTLR3_COMMON_TOKEN_struct::getLine, ANTLR3_COMMON_TOKEN_struct::getStartIndex, ANTLR3_COMMON_TOKEN_struct::getStopIndex, ANTLR3_COMMON_TOKEN_struct::getText, ANTLR3_COMMON_TOKEN_struct::getTokenIndex, ANTLR3_STRING_FACTORY_struct::newRaw, and ANTLR3_COMMON_TOKEN_struct::type. </p>
<p> Referenced by antlr3SetTokenAPI().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
