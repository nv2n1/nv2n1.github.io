---
title: "brlapi_describedkeycode_t(3)"
name: "brlapi_describedkeycode_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-brlapi_describedkeycode_t/"
description: "brlapi_describedKeyCode_t –"
---

<p>brlapi_describedKeyCode_t &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;brlapi.h&gt;</p>
<h3>Data Fields</h3>
<p>const char * <code>type</code> </p>
<p> const char * <code>command</code> </p>
<p> unsigned int <code>argument</code> </p>
<p> unsigned int <code>flags</code> </p>
<p> const char * <code>flag</code> [64-<code>BRLAPI_KEY_FLAGS_SHIFT</code>] </p>
<p> <code>brlapi_expandedKeyCode_t</code> <code>values</code> </p>
<h2>Detailed Description</h2>
<p>Structure holding the components of a key code as returned by <code>brlapi_describeKeyCode()</code></p>
<h2>Field Documentation</h2>
<h3>unsigned int brlapi_describedKeyCode_t::argument</h3>
<p>the argument value</p>
<h3>const char* brlapi_describedKeyCode_t::command</h3>
<p>the command name</p>
<h3>const char* brlapi_describedKeyCode_t::flag[64-<code>BRLAPI_KEY_FLAGS_SHIFT</code>]</h3>
<p>the flag names</p>
<h3>unsigned int brlapi_describedKeyCode_t::flags</h3>
<p>the flag count</p>
<h3>const char* brlapi_describedKeyCode_t::type</h3>
<p>the type name</p>
<h3><code>brlapi_expandedKeyCode_t</code> brlapi_describedKeyCode_t::values</h3>
<p>the actual values of the components </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for BrlAPI from the source code.</p>
