---
title: "voms_api-h(3)"
name: "voms_api-h"
section: "3"
letter: "v"
url: "/docs/linux/man/3-voms_api-h/"
description: "voms_api.h –"
---

<p>voms_api.h &#8211;</p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;fstream&gt;

#include &lt;string&gt;

#include &lt;vector&gt;

#include &lt;openssl/x509.h&gt;

#include &lt;openssl/bio.h&gt;

#include &lt;sys/types.h&gt;

#include 'newformat.h'</code></pre>
<h3>Data Structures</h3>
<p>struct data</p>
<p>User&#8217;s characteristics: can be repeated. Generic name-value attribute : can be repeated.</p>
<p>struct attribute</p>
<p>struct attributelist</p>
<p>struct contactdata</p>
<p>struct voms</p>
<p>struct vomsdata</p>
<p>Macros<br />
#define NOGLOBUS</p>
<p>Typedefs<br />
 typedef void * <code>gss_cred_id_t</code> </p>
<p> typedef void * <code>gss_ctx_id_t</code> </p>
<p> typedef bool(* <code>check_sig</code> )(X509 *, void *, <code>verror_type</code> &amp;)</p>
<h3>Enumerations</h3>
<pre><code>enum data_type { TYPE_NODATA,
                 TYPE_STD,
                 TYPE_CUSTOM }

The type of data returned.

    enum recurse_type { RECURSE_CHAIN,
                        RECURSE_NONE,
                        RECURSE_DEEP }

enum verify_type { VERIFY_FULL = 0xffffffff,
                   VERIFY_NONE = 0x00000000,
                   VERIFY_DATE = 0x00000001,
                   VERIFY_TARGET = 0x00000002,
                   VERIFY_KEY = 0x00000004,
                   VERIFY_SIGN = 0x00000008,
                   VERIFY_ORDER = 0x00000010,
                   VERIFY_ID = 0x00000020,
                   VERIFY_CERTLIST = 0x00000040 }

enum verror_type { VERR_NONE,
                   VERR_NOSOCKET,
                   VERR_NOIDENT,
                   VERR_COMM,
                   VERR_PARAM,
                   VERR_NOEXT,
                   VERR_NOINIT,
                   VERR_TIME,
                   VERR_IDCHECK,
                   VERR_EXTRAINFO,
                   VERR_FORMAT,
                   VERR_NODATA,
                   VERR_PARSE,
                   VERR_DIR,
                   VERR_SIGN,
                   VERR_SERVER,
                   VERR_MEM,
                   VERR_VERIFY,
                   VERR_TYPE,
                   VERR_ORDER,
                   VERR_SERVERCODE,
                   VERR_NOTAVAIL,
                   VERR_FILE }

Error codes.

    Functions int
    getVOMSMajorVersionNumber(void)

        int getVOMSMinorVersionNumber(void)

            int getVOMSPatchVersionNumber(void)</code></pre>
<h2>Macro Definition Documentation</h2>
<h3>#define NOGLOBUS</h3>
<p>Definition at line 33 of file voms_api.h.</p>
<h2>Typedef Documentation</h2>
<h3>typedef bool(* check_sig)(X509 *, void *, <code>verror_type</code> &amp;)</h3>
<p>Definition at line 190 of file voms_api.h.</p>
<h3>typedef void* <code>gss_cred_id_t</code></h3>
<p>Definition at line 42 of file voms_api.h.</p>
<h3>typedef void* <code>gss_ctx_id_t</code></h3>
<p>Definition at line 43 of file voms_api.h.</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>data_type</code></h3>
<p>The type of data returned. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>TYPE_NODATA </i></p>
<dd>no data</p>
<dt><i>TYPE_STD </i></p>
<dd>group, role, capability triplet</p>
<dt><i>TYPE_CUSTOM </i></p>
<dd>result of an S command</dl>
<p> Definition at line 77 of file voms_api.h.</p>
<h3>enum <code>recurse_type</code></h3>
<p><code>Enumerator</code></p>
<dl>
<dt><i>RECURSE_CHAIN </i></p>
<dd>
<dt><i>RECURSE_NONE </i></p>
<dd>
<dt><i>RECURSE_DEEP </i></p>
<dd></dl>
<p> Definition at line 143 of file voms_api.h.</p>
<h3>enum <code>verify_type</code></h3>
<p><code>Enumerator</code></p>
<dl>
<dt><i>VERIFY_FULL </i></p>
<dd>
<dt><i>VERIFY_NONE </i></p>
<dd>
<dt><i>VERIFY_DATE </i></p>
<dd>
<dt><i>VERIFY_TARGET </i></p>
<dd>
<dt><i>VERIFY_KEY </i></p>
<dd>
<dt><i>VERIFY_SIGN </i></p>
<dd>
<dt><i>VERIFY_ORDER </i></p>
<dd>
<dt><i>VERIFY_ID </i></p>
<dd>
<dt><i>VERIFY_CERTLIST </i></p>
<dd></dl>
<p> Definition at line 149 of file voms_api.h.</p>
<h3>enum <code>verror_type</code></h3>
<p>Error codes. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>VERR_NONE </i></p>
<dd>
<dt><i>VERR_NOSOCKET </i></p>
<dd>Socket problem</p>
<dt><i>VERR_NOIDENT </i></p>
<dd>Cannot identify itself (certificate problem)</p>
<dt><i>VERR_COMM </i></p>
<dd>Server problem</p>
<dt><i>VERR_PARAM </i></p>
<dd>Wrong parameters</p>
<dt><i>VERR_NOEXT </i></p>
<dd>VOMS extension missing</p>
<dt><i>VERR_NOINIT </i></p>
<dd>Initialization error</p>
<dt><i>VERR_TIME </i></p>
<dd>Error in time checking</p>
<dt><i>VERR_IDCHECK </i></p>
<dd>User data in extension different from the real ones</p>
<dt><i>VERR_EXTRAINFO </i></p>
<dd>VO name and URI missing</p>
<dt><i>VERR_FORMAT </i></p>
<dd>Wrong data format</p>
<dt><i>VERR_NODATA </i></p>
<dd>Empty extension</p>
<dt><i>VERR_PARSE </i></p>
<dd>Parse error</p>
<dt><i>VERR_DIR </i></p>
<dd>Directory error</p>
<dt><i>VERR_SIGN </i></p>
<dd>Signature error</p>
<dt><i>VERR_SERVER </i></p>
<dd>Unidentifiable VOMS server</p>
<dt><i>VERR_MEM </i></p>
<dd>Memory problems</p>
<dt><i>VERR_VERIFY </i></p>
<dd>Generic verification error</p>
<dt><i>VERR_TYPE </i></p>
<dd>Returned data of unknown type</p>
<dt><i>VERR_ORDER </i></p>
<dd>Ordering different than required</p>
<dt><i>VERR_SERVERCODE </i></p>
<dd>Error message from the server</p>
<dt><i>VERR_NOTAVAIL </i></p>
<dd>Method not available</p>
<dt><i>VERR_FILE </i></p>
<dd>Error reading data from file</dl>
<p> Definition at line 163 of file voms_api.h.</p>
<h2>Function Documentation</h2>
<h3>int getVOMSMajorVersionNumber (void)</h3>
<h3>int getVOMSMinorVersionNumber (void)</h3>
<h3>int getVOMSPatchVersionNumber (void)</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for VOMS CC API from the source code.</p>
