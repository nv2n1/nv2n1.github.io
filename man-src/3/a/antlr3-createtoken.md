---
title: "antlr3-createtoken(3)"
name: "antlr3-createtoken"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-createtoken/"
description: "src/antlr3commontreeadaptor.c –"
---

<p>src/antlr3commontreeadaptor.c &#8211; </p>
<p> This is the standard tree adaptor used by the C runtime unless the grammar source file says to use anything different.</p>
<h2>Synopsis</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3commontreeadaptor.h">antlr3commontreeadaptor.h</a>&gt; </p>
<h3>Functions</h3>
<p> ANTLR3_API <code>pANTLR3_BASE_TREE_ADAPTOR</code> <code>ANTLR3_TREE_ADAPTORDebugNew</code> (<code>pANTLR3_STRING_FACTORY</code> strFactory, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> debugger)<br />
 <i>Debugging version of the tree adaptor (not normally called as generated code calls setDebugEventListener instead which changes a normal token stream to a debugging stream and means that a user&#8217;s instantiation code does not need to be changed just to debug with AW. </i><br />
 ANTLR3_API <code>pANTLR3_BASE_TREE_ADAPTOR</code> <code>ANTLR3_TREE_ADAPTORNew</code> (<code>pANTLR3_STRING_FACTORY</code> strFactory)<br />
 <i>Create a new tree adaptor. </i><br />
 static <code>pANTLR3_BASE_TREE</code> <code>create</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adpator, <code>pANTLR3_COMMON_TOKEN</code> payload) </p>
<p> static <code>pANTLR3_COMMON_TOKEN</code> <code>createToken</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>ANTLR3_UINT32</code> tokenType, <code>pANTLR3_UINT8</code> text)<br />
 <i>Tell me how to create a token for use with imaginary token nodes. </i><br />
 static <code>pANTLR3_COMMON_TOKEN</code> <code>createTokenFromToken</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_COMMON_TOKEN</code> fromToken)<br />
 <i>Tell me how to create a token for use with imaginary token nodes. </i><br />
 static void <code>ctaFree</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>dbgCreate</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_COMMON_TOKEN</code> payload) </p>
<p> static void <code>dbgSetTokenBoundaries</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>pANTLR3_COMMON_TOKEN</code> startToken, <code>pANTLR3_COMMON_TOKEN</code> stopToken) </p>
<p> static void <code>deleteChild</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>ANTLR3_UINT32</code> i) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>dupNode</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> treeNode)<br />
 <i>Duplicate the supplied node. </i><br />
 static <code>pANTLR3_BASE_TREE</code> <code>errorNode</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_TOKEN_STREAM</code> ctnstream, <code>pANTLR3_COMMON_TOKEN</code> startToken, <code>pANTLR3_COMMON_TOKEN</code> stopToken, <code>pANTLR3_EXCEPTION</code> e) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>getChild</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>ANTLR3_UINT32</code> i) </p>
<p> static <code>ANTLR3_UINT32</code> <code>getChildCount</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t) </p>
<p> static <code>ANTLR3_INT32</code> <code>getChildIndex</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t) </p>
<p> static <code>pANTLR3_BASE_TREE</code> <code>getParent</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> child) </p>
<p> static <code>pANTLR3_STRING</code> <code>getText</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t) </p>
<p> static <code>pANTLR3_COMMON_TOKEN</code> <code>getToken</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t) </p>
<p> static <code>ANTLR3_MARKER</code> <code>getTokenStartIndex</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t) </p>
<p> static <code>ANTLR3_MARKER</code> <code>getTokenStopIndex</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t) </p>
<p> static <code>ANTLR3_UINT32</code> <code>getType</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t) </p>
<p> static void <code>replaceChildren</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> parent, <code>ANTLR3_INT32</code> startChildIndex, <code>ANTLR3_INT32</code> stopChildIndex, <code>pANTLR3_BASE_TREE</code> t) </p>
<p> static void <code>setChild</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>ANTLR3_UINT32</code> i, <code>pANTLR3_BASE_TREE</code> child) </p>
<p> static void <code>setChildIndex</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>ANTLR3_INT32</code> i) </p>
<p> static void <code>setDebugEventListener</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> debugger)<br />
 <i>Causes an existing common tree adaptor to become a debug version. </i><br />
 static void <code>setParent</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> child, <code>pANTLR3_BASE_TREE</code> parent) </p>
<p> static void <code>setTokenBoundaries</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>pANTLR3_COMMON_TOKEN</code> startToken, <code>pANTLR3_COMMON_TOKEN</code> stopToken)<br />
 <i>Track start/stop token for subtree root created for a rule. </i></p>
<h2>Detailed Description</h2>
<p> This is the standard tree adaptor used by the C runtime unless the grammar source file says to use anything different. </p>
<p> It embeds a BASE_TREE to which it adds its own implementation of anything that the base tree is not good for, plus a number of methods that any other adaptor type needs to implement too.</p>
<h2>Function Documentation</h2>
<h3>ANTLR3_API <code>pANTLR3_BASE_TREE_ADAPTOR</code> ANTLR3_TREE_ADAPTORDebugNew (<code>pANTLR3_STRING_FACTORY</code> strFactory, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> debugger)</h3>
<p> Debugging version of the tree adaptor (not normally called as generated code calls setDebugEventListener instead which changes a normal token stream to a debugging stream and means that a user&#8217;s instantiation code does not need to be changed just to debug with AW. </p>
<p> References ANTLR3_TREE_ADAPTORNew(), antlr3BaseTreeAdaptorInit(), ANTLR3_BASE_TREE_ADAPTOR_struct::create, dbgCreate(), dbgSetTokenBoundaries(), and ANTLR3_BASE_TREE_ADAPTOR_struct::setTokenBoundaries.</p>
<h3>ANTLR3_API <code>pANTLR3_BASE_TREE_ADAPTOR</code> ANTLR3_TREE_ADAPTORNew (<code>pANTLR3_STRING_FACTORY</code> strFactory)</h3>
<p> Create a new tree adaptor. Note that despite the fact that this is creating a new COMMON_TREE adaptor, we return the address of the BASE_TREE interface, as should any other adaptor that wishes to be used as the tree element of a tree parse/build. It needs to be given the address of a valid string factory as we do not know what the originating input stream encoding type was. This way we can rely on just using the original input stream&#8217;s string factory or one of the correct type which the user supplies us. </p>
<p> References ANTLR3_MALLOC, antlr3ArboretumNew(), antlr3BaseTreeAdaptorInit(), antlr3TokenFactoryNew(), ANTLR3_COMMON_TREE_ADAPTOR_struct::arboretum, ANTLR3_COMMON_TREE_ADAPTOR_struct::baseAdaptor, create(), ANTLR3_BASE_TREE_ADAPTOR_struct::create, createToken(), ANTLR3_BASE_TREE_ADAPTOR_struct::createToken, createTokenFromToken(), ANTLR3_BASE_TREE_ADAPTOR_struct::createTokenFromToken, ctaFree(), deleteChild(), ANTLR3_BASE_TREE_ADAPTOR_struct::deleteChild, dupNode(), ANTLR3_BASE_TREE_ADAPTOR_struct::dupNode, errorNode(), ANTLR3_BASE_TREE_ADAPTOR_struct::errorNode, ANTLR3_BASE_TREE_ADAPTOR_struct::free, getChild(), ANTLR3_BASE_TREE_ADAPTOR_struct::getChild, getChildCount(), ANTLR3_BASE_TREE_ADAPTOR_struct::getChildCount, getChildIndex(), ANTLR3_BASE_TREE_ADAPTOR_struct::getChildIndex, getParent(), ANTLR3_BASE_TREE_ADAPTOR_struct::getParent, getText(), ANTLR3_BASE_TREE_ADAPTOR_struct::getText, getTokenStartIndex(), ANTLR3_BASE_TREE_ADAPTOR_struct::getTokenStartIndex, getTokenStopIndex(), ANTLR3_BASE_TREE_ADAPTOR_struct::getTokenStopIndex, getType(), ANTLR3_BASE_TREE_ADAPTOR_struct::getType, replaceChildren(), ANTLR3_BASE_TREE_ADAPTOR_struct::replaceChildren, setChild(), ANTLR3_BASE_TREE_ADAPTOR_struct::setChild, setChildIndex(), ANTLR3_BASE_TREE_ADAPTOR_struct::setChildIndex, setDebugEventListener(), ANTLR3_BASE_TREE_ADAPTOR_struct::setDebugEventListener, setParent(), ANTLR3_BASE_TREE_ADAPTOR_struct::setParent, setTokenBoundaries(), ANTLR3_BASE_TREE_ADAPTOR_struct::setTokenBoundaries, ANTLR3_BASE_TREE_ADAPTOR_struct::strFactory, ANTLR3_COMMON_TOKEN_struct::strFactory, ANTLR3_BASE_TREE_ADAPTOR_struct::super, ANTLR3_BASE_TREE_ADAPTOR_struct::tokenFactory, and ANTLR3_TOKEN_FACTORY_struct::unTruc. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORDebugNew(), and antlr3CommonTreeNodeStreamNew().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> create (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adpator, <code>pANTLR3_COMMON_TOKEN</code> payload) [static]</h3>
<p> References ANTLR3_BASE_TREE_ADAPTOR_struct::super. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew(), and dbgCreate().</p>
<h3>static <code>pANTLR3_COMMON_TOKEN</code> createToken (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>ANTLR3_UINT32</code> tokenType, <code>pANTLR3_UINT8</code> text) [static]</h3>
<p> Tell me how to create a token for use with imaginary token nodes. For example, there is probably no input symbol associated with imaginary token DECL, but you need to create it as a payload or whatever for the DECL node as in ^(DECL type ID). </p>
<p> If you care what the token payload objects&#8217; type is, you should override this method and any other createToken variant. </p>
<p> References ANTLR3_TEXT_CHARP, ANTLR3_COMMON_TOKEN_struct::chars, ANTLR3_TOKEN_FACTORY_struct::input, ANTLR3_COMMON_TOKEN_struct::input, ANTLR3_TOKEN_FACTORY_struct::newToken, newToken(), ANTLR3_COMMON_TOKEN_struct::setType, ANTLR3_BASE_TREE_ADAPTOR_struct::strFactory, ANTLR3_COMMON_TOKEN_struct::strFactory, ANTLR3_COMMON_TOKEN_struct::textState, ANTLR3_BASE_TREE_ADAPTOR_struct::tokenFactory, and ANTLR3_COMMON_TOKEN_struct::tokText. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>static <code>pANTLR3_COMMON_TOKEN</code> createTokenFromToken (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_COMMON_TOKEN</code> fromToken) [static]</h3>
<p> Tell me how to create a token for use with imaginary token nodes. For example, there is probably no input symbol associated with imaginary token DECL, but you need to create it as a payload or whatever for the DECL node as in ^(DECL type ID). </p>
<p> This is a variant of createToken where the new token is derived from an actual real input token. Typically this is for converting &#8216;{&#8216; tokens to BLOCK etc&#8230; You&#8217;ll see </p>
<p> r : lc='{&#8216; ID+ &#8216;}&#8217; -&gt; ^(BLOCK[$lc] ID+) ; </p>
<p> If you care what the token payload objects&#8217; type is, you should override this method and any other createToken variant. </p>
<p> NB: this being C it is not so easy to extend the types of creaeteToken. We will have to see if anyone needs to do this and add any variants to this interface. </p>
<p> References ANTLR3_TEXT_CHARP, ANTLR3_TEXT_STRING, ANTLR3_STRING_struct::chars, ANTLR3_COMMON_TOKEN_struct::chars, ANTLR3_COMMON_TOKEN_struct::getChannel, ANTLR3_COMMON_TOKEN_struct::getCharPositionInLine, ANTLR3_COMMON_TOKEN_struct::getLine, ANTLR3_COMMON_TOKEN_struct::getText, ANTLR3_COMMON_TOKEN_struct::getTokenIndex, ANTLR3_COMMON_TOKEN_struct::getType, ANTLR3_STRING_struct::len, ANTLR3_STRING_FACTORY_struct::newPtr, ANTLR3_TOKEN_FACTORY_struct::newToken, newToken(), ANTLR3_COMMON_TOKEN_struct::setChannel, ANTLR3_COMMON_TOKEN_struct::setCharPositionInLine, ANTLR3_COMMON_TOKEN_struct::setLine, ANTLR3_COMMON_TOKEN_struct::setTokenIndex, ANTLR3_COMMON_TOKEN_struct::setType, ANTLR3_BASE_TREE_ADAPTOR_struct::strFactory, ANTLR3_COMMON_TOKEN_struct::text, ANTLR3_COMMON_TOKEN_struct::textState, ANTLR3_BASE_TREE_ADAPTOR_struct::tokenFactory, ANTLR3_COMMON_TOKEN_struct::tokText, and ANTLR3_COMMON_TOKEN_struct::toString. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>static void ctaFree (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor) [static]</h3>
<p> References ANTLR3_FREE, ANTLR3_COMMON_TREE_ADAPTOR_struct::arboretum, ANTLR3_TOKEN_FACTORY_struct::close, ANTLR3_ARBORETUM_struct::close, ANTLR3_BASE_TREE_ADAPTOR_struct::super, and ANTLR3_BASE_TREE_ADAPTOR_struct::tokenFactory. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> dbgCreate (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_COMMON_TOKEN</code> payload) [static]</h3>
<p> References create(), ANTLR3_DEBUG_EVENT_LISTENER_struct::createNode, and ANTLR3_BASE_TREE_ADAPTOR_struct::debugger. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORDebugNew(), and setDebugEventListener().</p>
<h3>static void dbgSetTokenBoundaries (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>pANTLR3_COMMON_TOKEN</code> startToken, <code>pANTLR3_COMMON_TOKEN</code> stopToken) [static]</h3>
<p> References ANTLR3_BASE_TREE_ADAPTOR_struct::debugger, ANTLR3_COMMON_TOKEN_struct::getTokenIndex, ANTLR3_DEBUG_EVENT_LISTENER_struct::setTokenBoundaries, and setTokenBoundaries(). </p>
<p> Referenced by ANTLR3_TREE_ADAPTORDebugNew(), and setDebugEventListener().</p>
<h3>static void deleteChild (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>ANTLR3_UINT32</code> i) [static]</h3>
<p> References ANTLR3_BASE_TREE_struct::deleteChild. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> dupNode (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> treeNode) [static]</h3>
<p> Duplicate the supplied node. </p>
<p> References ANTLR3_BASE_TREE_struct::dupNode. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> errorNode (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_TOKEN_STREAM</code> ctnstream, <code>pANTLR3_COMMON_TOKEN</code> startToken, <code>pANTLR3_COMMON_TOKEN</code> stopToken, <code>pANTLR3_EXCEPTION</code> e) [static]</h3>
<p> References ANTLR3_TOKEN_INVALID, and ANTLR3_BASE_TREE_ADAPTOR_struct::createTypeText. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> getChild (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>ANTLR3_UINT32</code> i) [static]</h3>
<p> References ANTLR3_BASE_TREE_struct::getChild. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>static <code>ANTLR3_UINT32</code> getChildCount (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t) [static]</h3>
<p> References ANTLR3_BASE_TREE_struct::getChildCount. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>static <code>ANTLR3_INT32</code> getChildIndex (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t) [static]</h3>
<p> References ANTLR3_BASE_TREE_struct::getChildIndex. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>static <code>pANTLR3_BASE_TREE</code> getParent (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> child) [static]</h3>
<p> References ANTLR3_BASE_TREE_struct::getParent. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>static <code>pANTLR3_STRING</code> getText (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t) [static]</h3>
<p> References ANTLR3_BASE_TREE_struct::getText. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>static <code>pANTLR3_COMMON_TOKEN</code> getToken (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t) [static]</h3>
<h3>static <code>ANTLR3_MARKER</code> getTokenStartIndex (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t) [static]</h3>
<p> References ANTLR3_BASE_TREE_struct::super. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>static <code>ANTLR3_MARKER</code> getTokenStopIndex (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t) [static]</h3>
<p> References ANTLR3_BASE_TREE_struct::super. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>static <code>ANTLR3_UINT32</code> getType (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t) [static]</h3>
<p> References ANTLR3_BASE_TREE_struct::getType. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>static void replaceChildren (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> parent, <code>ANTLR3_INT32</code> startChildIndex, <code>ANTLR3_INT32</code> stopChildIndex, <code>pANTLR3_BASE_TREE</code> t) [static]</h3>
<p> References ANTLR3_BASE_TREE_struct::replaceChildren. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>static void setChild (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>ANTLR3_UINT32</code> i, <code>pANTLR3_BASE_TREE</code> child) [static]</h3>
<p> References ANTLR3_BASE_TREE_struct::setChild. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>static void setChildIndex (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>ANTLR3_INT32</code> i) [static]</h3>
<p> References ANTLR3_BASE_TREE_struct::setChildIndex. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>static void setDebugEventListener (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> debugger) [static]</h3>
<p> Causes an existing common tree adaptor to become a debug version. </p>
<p> References antlr3BaseTreeAdaptorInit(), ANTLR3_BASE_TREE_ADAPTOR_struct::create, dbgCreate(), dbgSetTokenBoundaries(), and ANTLR3_BASE_TREE_ADAPTOR_struct::setTokenBoundaries. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>static void setParent (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> child, <code>pANTLR3_BASE_TREE</code> parent) [static]</h3>
<p> References ANTLR3_BASE_TREE_struct::setParent. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>static void setTokenBoundaries (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_TREE</code> t, <code>pANTLR3_COMMON_TOKEN</code> startToken, <code>pANTLR3_COMMON_TOKEN</code> stopToken) [static]</h3>
<p> Track start/stop token for subtree root created for a rule. Only works with CommonTree nodes. For rules that match nothing, seems like this will yield start=i and stop=i-1 in a nil node. Might be useful info so I&#8217;ll not force to be i..i. </p>
<p> References ANTLR3_COMMON_TOKEN_struct::getTokenIndex, ANTLR3_COMMON_TREE_struct::startIndex, ANTLR3_COMMON_TREE_struct::stopIndex, and ANTLR3_BASE_TREE_struct::super. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew(), and dbgSetTokenBoundaries().</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code.</p>
