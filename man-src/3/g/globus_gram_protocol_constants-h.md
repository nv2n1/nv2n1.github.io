---
title: "globus_gram_protocol_constants-h(3)"
name: "globus_gram_protocol_constants-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gram_protocol_constants-h/"
description: "globus_gram_protocol_constants.h –"
---

<p>globus_gram_protocol_constants.h &#8211; </p>
<p> Protocol Constants.</p>
<h2>Synopsis</h2>
<h3>Enumerations</h3>
<p>enum <code>globus_gram_protocol_error_t</code> </p>
<p> enum <code>globus_gram_protocol_job_signal_t</code> { <code>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_CANCEL</code> =1, <code>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_SUSPEND</code> =2, <code>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_RESUME</code> =3, <code>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_PRIORITY</code> =4, <code>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_COMMIT_REQUEST</code> =5, <code>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_COMMIT_EXTEND</code> =6, <code>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_STDIO_UPDATE</code> =7, <code>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_STDIO_SIZE</code> =8, <code>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_STOP_MANAGER</code> =9, <code>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_COMMIT_END</code> =10 } </p>
<p> enum <code>globus_gram_protocol_job_state_t</code> { <code>GLOBUS_GRAM_PROTOCOL_JOB_STATE_PENDING</code> =1, <code>GLOBUS_GRAM_PROTOCOL_JOB_STATE_ACTIVE</code> =2, <code>GLOBUS_GRAM_PROTOCOL_JOB_STATE_FAILED</code> =4, <code>GLOBUS_GRAM_PROTOCOL_JOB_STATE_DONE</code> =8, <code>GLOBUS_GRAM_PROTOCOL_JOB_STATE_SUSPENDED</code> =16, <code>GLOBUS_GRAM_PROTOCOL_JOB_STATE_UNSUBMITTED</code> =32, <code>GLOBUS_GRAM_PROTOCOL_JOB_STATE_STAGE_IN</code> =64, <code>GLOBUS_GRAM_PROTOCOL_JOB_STATE_STAGE_OUT</code> =128, <code>GLOBUS_GRAM_PROTOCOL_JOB_STATE_ALL</code> =0xFFFFF } </p>
<h2>Detailed Description</h2>
<p>Protocol Constants. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_gram_protocol from the source code.</p>
