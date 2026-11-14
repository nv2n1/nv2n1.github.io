---
title: "mpath_persistent_reserve_out(3)"
name: "mpath_persistent_reserve_out"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mpath_persistent_reserve_out/"
description: "mpath_persistent_reserve_out"
---

<p>mpath_persistent_reserve_out</p>
<h2>Synopsis</h2>
<p><code>#include &lt;mpath_persist.h&gt;</code> </p>
<p> <code>int mpath_persistent_reserve_out (int fd, int rq_servact, struct prin_resp *resp, int noisy, int verbose)</code> </p>
<h2>Description</h2>
<p>The function in the <code>mpath_persistent_reserve_out</code>() sends PR OUT command to the DM device and gets the response.<br />
 <code>Parameters:</code><br />
 <i>fd </i> <code>The file descriptor of a multipath device. Input argument.</code><br />
 <i>rq_servact</i> <code>PROUT command service action. Input argument</code><br />
 <i>rq_scope</i> <code>Persistent reservation scope. The value should be always LU_SCOPE (0h).</code><br />
 <i>rq_type</i> <code>Persistent reservation type. The valid values of persistent reservation types are</code><br />
5h&nbsp;<wbr>(Write exclusive &#8211; registrants only)<br />
6h&nbsp;<wbr>(Exclusive access &#8211; registrants only)<br />
7h&nbsp;<wbr>(Write exclusive &#8211; All registrants)<br />
8h&nbsp;<wbr>(Exclusive access &#8211; All registrants).<br />
 <i>paramp</i> <code>PROUT command parameter data. The paramp is a struct which describes PROUT parameter list. Caller should manage the memory allocation of this structure.</code><br />
 <i>noisy</i> <code>Turn on debugging trace: Input argument. 0-&gt;Disable, 1-&gt;Enable.</code><br />
 <i>verbose</i> <code>Set verbosity level. Input argument. value: 0 to 3. 0-&gt;Crits and Errors, 1-&gt;Warnings, 2-&gt;Info, 3-&gt;Debug</code> </p>
<h2>Returns</h2>
<p><i>MPATH_PR_SUCCESS</i> <code>if PR command successful else returns any one of the status mentioned below</code><br />
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
 <i>MPATH_PR_RESERV_CONFLICT</i> <code>if command fails with reservation conflict</code><br />
 <i>MPATH_PR_FILE_ERROR</i> <code>if command fails while accessing file (device node) problems(e.g. not found)</code><br />
 <i>MPATH_PR_DMMP_ERROR</i> <code>if Device Mapper related error.(e.g Error in getting dm info) </code><br />
 <i>MPATH_PR_OTHER</i> <code>if other error/warning has occurred(e.g transport or driver error)</code> </p>
<h2>See Also</h2>
<p><i>mpath_persistent_reserve_in<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>mpathpersist /usr/share/doc/mpathpersist/README</i></p>
