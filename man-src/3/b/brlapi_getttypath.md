---
title: "brlapi_getttypath(3)"
name: "brlapi_getttypath"
section: "3"
letter: "b"
url: "/docs/linux/man/3-brlapi_getttypath/"
description: "Deprecated names –"
---

<p>Deprecated names &#8211; </p>
<h3>Data Structures</h3>
<p>struct <code>brlapi_writeStruct</code> </p>
<h3>Macros</h3>
<p>#define <code>brlapi_settings_t</code> <code>brlapi_connectionSettings_t</code> </p>
<p> #define <code>BRLAPI_WRITESTRUCT_INITIALIZER</code> <code>BRLAPI_WRITEARGUMENTS_INITIALIZER</code> </p>
<p> #define <code>brl_keycode_t</code> <code>brlapi_keyCode_t</code> </p>
<p> #define <code>brl_type_t</code> <code>brlapi_packetType_t</code> </p>
<p> #define <code>BRLCOMMANDS</code> NULL </p>
<p> #define <code>BRL_KEYCODE_MAX</code> <code>BRLAPI_KEY_MAX</code> </p>
<p> #define <code>brlapi_initializeConnection</code> <code>brlapi_openConnection</code> </p>
<p> #define <code>brlapi_getTty</code> <code>brlapi_enterTtyMode</code> </p>
<p> #define <code>brlapi_getTtyPath</code> <code>brlapi_enterTtyModeWithPath</code> </p>
<p> #define <code>brlapi_leaveTty</code> <code>brlapi_leaveTtyMode</code> </p>
<p> #define <code>brlapi_unignoreKeyRange</code> brlapi_acceptKeyRange </p>
<p> #define <code>brlapi_unignoreKeySet</code> brlapi_acceptKeySet </p>
<p> #define <code>brlapi_getRaw</code> <code>brlapi_enterRawMode</code> </p>
<p> #define <code>brlapi_leaveRaw</code> <code>brlapi_leaveRawMode</code> </p>
<p> #define <code>brlapi_suspend</code> <code>brlapi_suspendDriver</code> </p>
<p> #define <code>brlapi_resume</code> <code>brlapi_resumeDriver</code> </p>
<p> #define <code>BRLERR_SUCCESS</code> <code>BRLAPI_ERROR_SUCCESS</code> </p>
<p> #define <code>BRLERR_NOMEM</code> <code>BRLAPI_ERROR_NOMEM</code> </p>
<p> #define <code>BRLERR_TTYBUSY</code> <code>BRLAPI_ERROR_TTYBUSY</code> </p>
<p> #define <code>BRLERR_DEVICEBUSY</code> <code>BRLAPI_ERROR_DEVICEBUSY</code> </p>
<p> #define <code>BRLERR_UNKNOWN_INSTRUCTION</code> <code>BRLAPI_ERROR_UNKNOWN_INSTRUCTION</code> </p>
<p> #define <code>BRLERR_ILLEGAL_INSTRUCTION</code> <code>BRLAPI_ERROR_ILLEGAL_INSTRUCTION</code> </p>
<p> #define <code>BRLERR_INVALID_PARAMETER</code> <code>BRLAPI_ERROR_INVALID_PARAMETER</code> </p>
<p> #define <code>BRLERR_INVALID_PACKET</code> <code>BRLAPI_ERROR_INVALID_PACKET</code> </p>
<p> #define <code>BRLERR_CONNREFUSED</code> <code>BRLAPI_ERROR_CONNREFUSED</code> </p>
<p> #define <code>BRLERR_OPNOTSUPP</code> <code>BRLAPI_ERROR_OPNOTSUPP</code> </p>
<p> #define <code>BRLERR_GAIERR</code> <code>BRLAPI_ERROR_GAIERR</code> </p>
<p> #define <code>BRLERR_LIBCERR</code> <code>BRLAPI_ERROR_LIBCERR</code> </p>
<p> #define <code>BRLERR_UNKNOWNTTY</code> <code>BRLAPI_ERROR_UNKNOWNTTY</code> </p>
<p> #define <code>BRLERR_PROTOCOL_VERSION</code> <code>BRLAPI_ERROR_PROTOCOL_VERSION</code> </p>
<p> #define <code>BRLERR_EOF</code> <code>BRLAPI_ERROR_EOF</code> </p>
<p> #define <code>BRLERR_EMPTYKEY</code> <code>BRLAPI_ERROR_EMPTYKEY</code> </p>
<p> #define <code>BRLERR_DRIVERERROR</code> <code>BRLAPI_ERROR_DRIVERERROR</code> </p>
<h2>Detailed Description</h2>
<p>With version 0.5.0, BrlAPI is now provided through including &lt;<code>brlapi.h</code>&gt; and got a big renaming pass. Old names are still available through macros, but they are deprecated since they will get dropped in the next release. This documentation is for you to know the new names. </p>
<p> For checking that you have completely switched to new names, just define BRLAPI_NO_DEPRECATED: that will disable compatibility macros.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define BRL_KEYCODE_MAX <code>BRLAPI_KEY_MAX</code></h3>
<h3>#define brl_keycode_t <code>brlapi_keyCode_t</code></h3>
<h3>#define brl_type_t <code>brlapi_packetType_t</code></h3>
<h3>#define brlapi_getRaw <code>brlapi_enterRawMode</code></h3>
<h3>#define brlapi_getTty <code>brlapi_enterTtyMode</code></h3>
<h3>#define brlapi_getTtyPath <code>brlapi_enterTtyModeWithPath</code></h3>
<h3>#define brlapi_initializeConnection <code>brlapi_openConnection</code></h3>
<h3>#define brlapi_leaveRaw <code>brlapi_leaveRawMode</code></h3>
<h3>#define brlapi_leaveTty <code>brlapi_leaveTtyMode</code></h3>
<h3>#define brlapi_resume <code>brlapi_resumeDriver</code></h3>
<h3>#define brlapi_settings_t <code>brlapi_connectionSettings_t</code></h3>
<h3>#define brlapi_suspend <code>brlapi_suspendDriver</code></h3>
<h3>#define brlapi_unignoreKeyRange brlapi_acceptKeyRange</h3>
<h3>#define brlapi_unignoreKeySet brlapi_acceptKeySet</h3>
<h3>#define BRLAPI_WRITESTRUCT_INITIALIZER <code>BRLAPI_WRITEARGUMENTS_INITIALIZER</code></h3>
<h3>#define BRLCOMMANDS NULL</h3>
<h3>#define BRLERR_CONNREFUSED <code>BRLAPI_ERROR_CONNREFUSED</code></h3>
<h3>#define BRLERR_DEVICEBUSY <code>BRLAPI_ERROR_DEVICEBUSY</code></h3>
<h3>#define BRLERR_DRIVERERROR <code>BRLAPI_ERROR_DRIVERERROR</code></h3>
<h3>#define BRLERR_EMPTYKEY <code>BRLAPI_ERROR_EMPTYKEY</code></h3>
<h3>#define BRLERR_EOF <code>BRLAPI_ERROR_EOF</code></h3>
<h3>#define BRLERR_GAIERR <code>BRLAPI_ERROR_GAIERR</code></h3>
<h3>#define BRLERR_ILLEGAL_INSTRUCTION <code>BRLAPI_ERROR_ILLEGAL_INSTRUCTION</code></h3>
<h3>#define BRLERR_INVALID_PACKET <code>BRLAPI_ERROR_INVALID_PACKET</code></h3>
<h3>#define BRLERR_INVALID_PARAMETER <code>BRLAPI_ERROR_INVALID_PARAMETER</code></h3>
<h3>#define BRLERR_LIBCERR <code>BRLAPI_ERROR_LIBCERR</code></h3>
<h3>#define BRLERR_NOMEM <code>BRLAPI_ERROR_NOMEM</code></h3>
<h3>#define BRLERR_OPNOTSUPP <code>BRLAPI_ERROR_OPNOTSUPP</code></h3>
<h3>#define BRLERR_PROTOCOL_VERSION <code>BRLAPI_ERROR_PROTOCOL_VERSION</code></h3>
<h3>#define BRLERR_SUCCESS <code>BRLAPI_ERROR_SUCCESS</code></h3>
<h3>#define BRLERR_TTYBUSY <code>BRLAPI_ERROR_TTYBUSY</code></h3>
<h3>#define BRLERR_UNKNOWN_INSTRUCTION <code>BRLAPI_ERROR_UNKNOWN_INSTRUCTION</code></h3>
<h3>#define BRLERR_UNKNOWNTTY <code>BRLAPI_ERROR_UNKNOWNTTY</code></h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for BrlAPI from the source code.</p>
