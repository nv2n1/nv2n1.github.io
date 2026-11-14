---
title: "brlapi_keycodes-h(3)"
name: "brlapi_keycodes-h"
section: "3"
letter: "b"
url: "/docs/linux/man/3-brlapi_keycodes-h/"
description: "brlapi_keycodes.h –"
---

<p>brlapi_keycodes.h &#8211; </p>
<h2>Synopsis</h2>
<p>#include &#8216;brlapi_constants.h&#8217; </p>
<h3>Macros</h3>
<p>#define <code>BRLAPI_PRIxKEYCODE</code> PRIx64 </p>
<p> #define <code>BRLAPI_PRIuKEYCODE</code> PRIu64 </p>
<p> #define <code>BRLAPI_KEY_MAX</code> UINT64_C(0XFFFFFFFFFFFFFFFF) </p>
<p> #define <code>BRLAPI_KEY_FLAGS_MASK</code> UINT64_C(0XFFFFFFFF00000000) </p>
<p> #define <code>BRLAPI_KEY_FLAGS_SHIFT</code> 32 </p>
<p> #define <code>BRLAPI_KEY_FLG</code>(v) ((<code>brlapi_keyCode_t</code>)(v) &lt;&lt; <code>BRLAPI_KEY_FLAGS_SHIFT</code>) </p>
<p> #define <code>BRLAPI_KEY_FLG_MOD1</code> <code>BRLAPI_KEY_FLG</code>(0x00000008) </p>
<p> #define <code>BRLAPI_KEY_FLG_MOD2</code> <code>BRLAPI_KEY_FLG</code>(0x00000010) </p>
<p> #define <code>BRLAPI_KEY_FLG_MOD3</code> <code>BRLAPI_KEY_FLG</code>(0x00000020) </p>
<p> #define <code>BRLAPI_KEY_FLG_MOD4</code> <code>BRLAPI_KEY_FLG</code>(0x00000040) </p>
<p> #define <code>BRLAPI_KEY_FLG_MOD5</code> <code>BRLAPI_KEY_FLG</code>(0x00000080) </p>
<p> #define <code>BRLAPI_KEY_TYPE_MASK</code> UINT64_C(0X00000000E0000000) </p>
<p> #define <code>BRLAPI_KEY_TYPE_SHIFT</code> 29 </p>
<p> #define <code>BRLAPI_KEY_TYPE_CMD</code> UINT64_C(0X0000000020000000) </p>
<p> #define <code>BRLAPI_KEY_TYPE_SYM</code> UINT64_C(0X0000000000000000) </p>
<p> #define <code>BRLAPI_KEY_CODE_MASK</code> UINT64_C(0X000000001FFFFFFF) </p>
<p> #define <code>BRLAPI_KEY_CODE_SHIFT</code> 0 </p>
<p> #define <code>BRLAPI_KEY_CMD_BLK_MASK</code> UINT64_C(0X1FFF0000) </p>
<p> #define <code>BRLAPI_KEY_CMD_BLK_SHIFT</code> 16 </p>
<p> #define <code>BRLAPI_KEY_CMD_ARG_MASK</code> UINT64_C(0X0000FFFF) </p>
<p> #define <code>BRLAPI_KEY_CMD_ARG_SHIFT</code> 0 </p>
<p> #define <code>BRLAPI_KEY_CMD</code>(v) ((v) &lt;&lt; <code>BRLAPI_KEY_CMD_BLK_SHIFT</code>) </p>
<p> #define <code>BRLAPI_KEY_SYM_BACKSPACE</code> UINT64_C(0X0000FF08) </p>
<p> #define <code>BRLAPI_KEY_SYM_TAB</code> UINT64_C(0X0000FF09) </p>
<p> #define <code>BRLAPI_KEY_SYM_LINEFEED</code> UINT64_C(0X0000FF0D) </p>
<p> #define <code>BRLAPI_KEY_SYM_ESCAPE</code> UINT64_C(0X0000FF1B) </p>
<p> #define <code>BRLAPI_KEY_SYM_HOME</code> UINT64_C(0X0000FF50) </p>
<p> #define <code>BRLAPI_KEY_SYM_LEFT</code> UINT64_C(0X0000FF51) </p>
<p> #define <code>BRLAPI_KEY_SYM_UP</code> UINT64_C(0X0000FF52) </p>
<p> #define <code>BRLAPI_KEY_SYM_RIGHT</code> UINT64_C(0X0000FF53) </p>
<p> #define <code>BRLAPI_KEY_SYM_DOWN</code> UINT64_C(0X0000FF54) </p>
<p> #define <code>BRLAPI_KEY_SYM_PAGE_UP</code> UINT64_C(0X0000FF55) </p>
<p> #define <code>BRLAPI_KEY_SYM_PAGE_DOWN</code> UINT64_C(0X0000FF56) </p>
<p> #define <code>BRLAPI_KEY_SYM_END</code> UINT64_C(0X0000FF57) </p>
<p> #define <code>BRLAPI_KEY_SYM_INSERT</code> UINT64_C(0X0000FF63) </p>
<p> #define <code>BRLAPI_KEY_SYM_FUNCTION</code> UINT64_C(0X0000FFBE) </p>
<p> #define <code>BRLAPI_KEY_SYM_DELETE</code> UINT64_C(0X0000FFFF) </p>
<p> #define <code>BRLAPI_KEY_SYM_UNICODE</code> UINT64_C(0X01000000) </p>
<h3>Typedefs</h3>
<p>typedef uint64_t <code>brlapi_keyCode_t</code> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for BrlAPI from the source code.</p>
