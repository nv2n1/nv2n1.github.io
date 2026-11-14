---
title: "antlr3_token_factory_struct(3)"
name: "antlr3_token_factory_struct"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3_token_factory_struct/"
description: "ANTLR3_TOKEN_FACTORY_struct –"
---

<p>ANTLR3_TOKEN_FACTORY_struct &#8211; </p>
<p> ANTLR3 Token factory interface to create lots of tokens efficiently rather than creating and freeing lots of little bits of memory.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3commontoken.h">antlr3commontoken.h</a>&gt;</p>
<h3>Data Fields</h3>
<p>void(* <code>close</code> )(struct <code>ANTLR3_TOKEN_FACTORY_struct</code> *factory)<br />
 <i>Pointer to a function the destroys the factory. </i><br />
 <code>pANTLR3_INPUT_STREAM</code> <code>input</code><br />
 <i>Pointer to an input stream that is using this token factory (may be NULL) which will be assigned to the tokens automatically. </i><br />
 <code>pANTLR3_COMMON_TOKEN</code>(* <code>newToken</code> )(struct <code>ANTLR3_TOKEN_FACTORY_struct</code> *factory)<br />
 <i>Pointer to a function that returns a new token. </i><br />
 <code>ANTLR3_UINT32</code> <code>nextToken</code><br />
 <i>The next token to throw out from the pool, will cause a new pool allocation if this exceeds the available tokenCount. </i><br />
 <code>pANTLR3_COMMON_TOKEN</code> * <code>pools</code><br />
 <i>Pointers to the array of tokens that this factory has produced so far. </i><br />
 void(* <code>setInputStream</code> )(struct <code>ANTLR3_TOKEN_FACTORY_struct</code> *factory, <code>pANTLR3_INPUT_STREAM</code> <code>input</code>)<br />
 <i>Pointer to a function that changes teh curent inptu stream so that new tokens are created with reference to their originating text. </i><br />
 <code>ANTLR3_INT32</code> <code>thisPool</code><br />
 <i>Current pool tokens we are allocating from. </i><br />
 <code>ANTLR3_COMMON_TOKEN</code> <code>unTruc</code><br />
 <i>Trick to initialize tokens and their API quickly, we set up this token when the factory is created, then just copy the memory it uses into the new token. </i></p>
<h2>Detailed Description</h2>
<p>ANTLR3 Token factory interface to create lots of tokens efficiently rather than creating and freeing lots of little bits of memory.</p>
<h2>Field Documentation</h2>
<h3>void(* <code>ANTLR3_TOKEN_FACTORY_struct::close</code>)(struct <code>ANTLR3_TOKEN_FACTORY_struct</code> *factory)</h3>
<p>Pointer to a function the destroys the factory. </p>
<p> Referenced by antlr3TokenFactoryNew(), ctaFree(), freeBR(), and freeLexer().</p>
<h3><code>pANTLR3_INPUT_STREAM</code> <code>ANTLR3_TOKEN_FACTORY_struct::input</code></h3>
<p>Pointer to an input stream that is using this token factory (may be NULL) which will be assigned to the tokens automatically. </p>
<p> Referenced by createToken(), newPoolToken(), and setInputStream().</p>
<h3><code>pANTLR3_COMMON_TOKEN</code>(* <code>ANTLR3_TOKEN_FACTORY_struct::newToken</code>)(struct <code>ANTLR3_TOKEN_FACTORY_struct</code> *factory)</h3>
<p>Pointer to a function that returns a new token. </p>
<p> Referenced by antlr3TokenFactoryNew(), createToken(), createTokenFromToken(), emit(), and getMissingSymbol().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_TOKEN_FACTORY_struct::nextToken</code></h3>
<p>The next token to throw out from the pool, will cause a new pool allocation if this exceeds the available tokenCount. </p>
<p> Referenced by factoryClose(), newPool(), and newPoolToken().</p>
<h3><code>pANTLR3_COMMON_TOKEN</code>* <code>ANTLR3_TOKEN_FACTORY_struct::pools</code></h3>
<p>Pointers to the array of tokens that this factory has produced so far. </p>
<p> Referenced by antlr3TokenFactoryNew(), factoryClose(), newPool(), and newPoolToken().</p>
<h3>void(* <code>ANTLR3_TOKEN_FACTORY_struct::setInputStream</code>)(struct <code>ANTLR3_TOKEN_FACTORY_struct</code> *factory, <code>pANTLR3_INPUT_STREAM</code> <code>input</code>)</h3>
<p>Pointer to a function that changes teh curent inptu stream so that new tokens are created with reference to their originating text. </p>
<p> Referenced by antlr3TokenFactoryNew(), and setCharStream().</p>
<h3><code>ANTLR3_INT32</code> <code>ANTLR3_TOKEN_FACTORY_struct::thisPool</code></h3>
<p>Current pool tokens we are allocating from. </p>
<p> Referenced by antlr3TokenFactoryNew(), factoryClose(), newPool(), and newPoolToken().</p>
<h3><code>ANTLR3_COMMON_TOKEN</code> <code>ANTLR3_TOKEN_FACTORY_struct::unTruc</code></h3>
<p>Trick to initialize tokens and their API quickly, we set up this token when the factory is created, then just copy the memory it uses into the new token. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew(), antlr3TokenFactoryNew(), and setInputStream(). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
