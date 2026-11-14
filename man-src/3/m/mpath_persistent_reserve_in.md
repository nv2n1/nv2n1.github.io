---
title: "mpath_persistent_reserve_in(3)"
name: "mpath_persistent_reserve_in"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mpath_persistent_reserve_in/"
description: "mpath_persistent_reserve_in"
---

<p>mpath_persistent_reserve_in</p>
<h2>Synopsis</h2>
<p><code>#include &lt;mpath_persist.h&gt;</code> </p>
<p> <code>int mpath_persistent_reserve_in (int fd, int rq_servact, struct prin_resp *resp, int noisy, int verbose)</code> </p>
<h2>Description</h2>
<p>The function in the <code>mpath_persistent_reserve_in</code>() sends PRIN command to the DM device and gets the response.<br />
 <code>Parameters:</code><br />
 <i>fd</i> <code>The file descriptor of a multipath device. Input argument.</code><br />
 <i>rq_servact</i> <code>PRIN command service action. Input argument</code><br />
 <i>resp</i> <code>The response from PRIN service action. The caller should manage the memory allocation of this structure</code><br />
 <i>noisy</i> <code>Turn on debugging trace: Input argument. 0-&gt;Disable, 1-&gt;Enable</code><br />
 <i>verbose</i> <code>Set verbosity level. Input argument. value:[0-3]. 0-&gt;Crits and Errors, 1-&gt;Warnings, 2-&gt;Info, 3-&gt;Debug</code> </p>
<h2>Returns</h2>
<p><i>MPATH_PR_SUCCESS</i> <code>if PR command successful</code><br />
 <i>MPATH_PR_SYNTAX_ERROR </i> <code>if syntax error or invalid parameter</code><br />
 <i>MPATH_PR_SENSE_NOT_READY </i> <code>if command fails with [sk,asc,ascq: 0x2,*,*]</code><br />
 <i>MPATH_PR_SENSE_MEDIUM_ERROR</i> <code>if command fails with [sk,asc,ascq: 0x3,*,*]</code><br />
 <i>MPATH_PR_SENSE_HARDWARE_ERROR</i> <code>if command fails with [sk,asc,ascq: 0x4,*,*]</code><br />
 <i>MPATH_PR_SENSE_INVALID_OP</i> <code>if command fails with [sk,asc,ascq: 0x5,0x20,0x0]</code><br />
 <i>MPATH_PR_ILLEGAL_REQ</i> <code>if command fails with [sk,asc,ascq: 0x5,*,*]</code><br />
 <i>MPATH_PR_SENSE_UNIT_ATTENTION</i> <code>if command fails with [sk,asc,ascq: 0x6,*,*]</code><br />
 <i>MPATH_PR_SENSE_ABORTED_COMMAND</i> <code>if command fails with [sk,asc,ascq: 0xb,*,*]</code><br />
 <i>MPATH_PR_NO_SENSE</i> <code>if command fails with [sk,asc,ascq: 0x0,*,*]</code><br />
 <i>MPATH_PR_SENSE_MALFORMED </i> <code>if command fails with SCSI command malformed</code><br />
 <i>MPATH_PR_FILE_ERROR</i> <code>if command fails while accessing file (device node) problems(e.g. not found)</code><br />
 <i>MPATH_PR_DMMP_ERROR</i> <code>if Device Mapper related error.(e.g Error in getting dm info) </code><br />
 <i>MPATH_PR_OTHER</i> <code>if other error/warning has occurred(e.g transport or driver error)</code> </p>
<h2>See Also</h2>
<p><i>mpath_persistent_reserve_out mpathpersist /usr/share/doc/mpathpersist/README</i></p>
