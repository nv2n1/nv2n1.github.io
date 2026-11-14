---
title: "lwres_getrrsetbyname(3)"
name: "lwres_getrrsetbyname"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lwres_getrrsetbyname/"
description: "lwres_getrrsetbyname, lwres_freerrset – retrieve DNS records"
---

<h2 class="name">NAME</h2>
<p> lwres_getrrsetbyname, lwres_freerrset &#8211; retrieve DNS records </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;lwres/netdb.h&gt;
</code></pre>
<dl>
<dt> <code>int lwres_getrrsetbyname(const char&nbsp;<wbr>*</code><i>hostname</i><code>, unsigned int&nbsp;<wbr></code><i>rdclass</i><code>, unsigned int&nbsp;<wbr></code><i>rdtype</i><code>, unsigned int&nbsp;<wbr></code><i>flags</i><code>, struct rrsetinfo&nbsp;<wbr>**</code><i>res</i><code>);</code></p>
<dt> <code>void lwres_freerrset(struct rrsetinfo&nbsp;<wbr>*</code><i>rrset</i><code>);</code></dl>
<dd>The following structures are used: </p>
<dl>
<dt>
<dd>
struct rdatainfo {<br />
    unsigned int rdi_length; /* length of data */<br />
    unsigned char *rdi_data; /* record data */<br />
};
</dl>
<dl>
<dt>
<dd>
<pre><code>
struct rrsetinfo {
    unsigned int rri_flags;       /* RRSET_VALIDATED... */
    unsigned int rri_rdclass;     /* class number */
    unsigned int rri_rdtype;      /* RR type number */
    unsigned int rri_ttl;         /* time to live */
    unsigned int rri_nrdatas;     /* size of rdatas array */
    unsigned int rri_nsigs;       /* size of sigs array */
    char *rri_name;               /* canonical name */
    struct rdatainfo *rri_rdatas; /* individual records */
    struct rdatainfo *rri_sigs;   /* individual signatures */
};
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>lwres_getrrsetbyname()</code> gets a set of resource records associated with a <i>hostname</i>, <i>class</i>, and <i>type</i>. <i>hostname</i> is a pointer a to null-terminated string. The <i>flags</i> field is currently unused and must be zero. </p>
<p> After a successful call to <code>lwres_getrrsetbyname()</code>, <i>*res</i> is a pointer to an <code>rrsetinfo</code> structure, containing a list of one or more <code>rdatainfo</code> structures containing resource records and potentially another list of <code>rdatainfo</code> structures containing SIG resource records associated with those records. The members <code>rri_rdclass</code> and <code>rri_rdtype</code> are copied from the parameters. <code>rri_ttl</code> and <code>rri_name</code> are properties of the obtained rrset. The resource records contained in <code>rri_rdatas</code> and <code>rri_sigs</code> are in uncompressed DNS wire format. Properties of the rdataset are represented in the <code>rri_flags</code> bitfield. If the RRSET_VALIDATED bit is set, the data has been DNSSEC validated and the signatures verified. </p>
<p> All of the information returned by <code>lwres_getrrsetbyname()</code> is dynamically allocated: the <code>rrsetinfo</code> and <code>rdatainfo</code> structures, and the canonical host name strings pointed to by the <code>rrsetinfo</code>structure. Memory allocated for the dynamically allocated structures created by a successful call to <code>lwres_getrrsetbyname()</code> is released by <code>lwres_freerrset()</code>. <i>rrset</i> is a pointer to a <code>struct rrset</code> created by a call to <code>lwres_getrrsetbyname()</code>. </p>
<h2>RETURN VALUES</h2>
<p> <code>lwres_getrrsetbyname()</code> returns zero on success, and one of the following error codes if an error occurred: </p>
<p> <code>ERRSET_NONAME</code></p>
<dl>
<dt>
<dd> the name does not exist</dl>
<p> <code>ERRSET_NODATA</code></p>
<dl>
<dt>
<dd> the name exists, but does not have data of the desired type</dl>
<p> <code>ERRSET_NOMEMORY</code></p>
<dl>
<dt>
<dd> memory could not be allocated</dl>
<p> <code>ERRSET_INVAL</code></p>
<dl>
<dt>
<dd> a parameter is invalid</dl>
<p> <code>ERRSET_FAIL</code></p>
<dl>
<dt>
<dd> other failure</dl>
<dl>
<dt>
<dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-lwres/">lwres</a></code>(3).</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004, 2005, 2007 Internet Systems Consortium, Inc. (&quot;ISC&quot;)<br />
 Copyright &#169; 2000, 2001 Internet Software Consortium. </p>
<h2>Index</h2>
