---
title: "error-h(3)"
name: "error-h"
section: "3"
letter: "e"
url: "/docs/linux/man/3-error-h/"
description: "src/error.h –"
---

<p>src/error.h &#8211; </p>
<p> Rasing errors.</p>
<h2>Synopsis</h2>
<p>#include &lt;stddef.h&gt; </p>
<h3>Functions</h3>
<p>int <code>drmaa_get_errno_error</code> (char *error_diagnosis, size_t error_diag_len)<br />
 <i>Gets last system error message and returns its code. </i><br />
 int <code>drmaa_get_pbs_error</code> (char *error_diagnosis, size_t error_diag_len)<br />
 <i>Retrieves last PBS error message. </i><br />
 int <code>drmaa_map_pbs_error</code> (int pbs_errcode)<br />
 <i>Maps PBS error code into DMRAA code. </i></p>
<h2>Detailed Description</h2>
<p>Rasing errors. </p>
<h2>Function Documentation</h2>
<h3>int drmaa_get_errno_error (char *error_diagnosis, size_terror_diag_len)</h3>
<p>Gets last system error message and returns its code.</p>
<h3>int drmaa_get_pbs_error (char *error_diagnosis, size_terror_diag_len)</h3>
<p>Retrieves last PBS error message.</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>no longer viable in multi-threaded torque</dl>
<h3>int drmaa_map_pbs_error (intpbs_errcode)</h3>
<p>Maps PBS error code into DMRAA code.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for torque from the source code.</p>
