---
title: "libgenders(3)"
name: "libgenders"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libgenders/"
description: "libgenders – a library of functions to parse and retrieve genders data"
---

<h2>NAME</h2>
<p> libgenders &#8211; a library of functions to parse and retrieve genders data</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;genders.h&gt;</code> </p>
<p> <code>genders_t genders_handle_create(void);</code> </p>
<p> <code>int genders_handle_destroy(genders_t handle);</code> </p>
<p> <code>int genders_load_data(genders_t handle, const char *filename);</code> </p>
<p> <code>int genders_errnum(genders_t handle);</code> </p>
<p> <code>char *genders_strerror(int errnum);</code> </p>
<p> <code>char *genders_errormsg(genders_t handle);</code> </p>
<p> <code>void genders_perror(genders_t handle, const char *msg);</code> </p>
<p> <code>int genders_getnumnodes(genders_t handle);</code> </p>
<p> <code>int genders_getnumattrs(genders_t handle);</code> </p>
<p> <code>int genders_getmaxattrs(genders_t handle);</code> </p>
<p> <code>int genders_getmaxnodelen(genders_t handle);</code> </p>
<p> <code>int genders_getmaxattrlen(genders_t handle);</code> </p>
<p> <code>int genders_getmaxvallen(genders_t handle);</code> </p>
<p> <code>int genders_nodelist_create(genders_t handle, char ***nodelist);</code> </p>
<p> <code>int genders_nodelist_clear(genders_t handle, char **nodelist);</code> </p>
<p> <code>int genders_nodelist_destroy(genders_t handle, char **nodelist);</code> </p>
<p> <code>int genders_attrlist_create(genders_t handle, char ***attrlist);</code> </p>
<p> <code>int genders_attrlist_clear(genders_t handle, char **attrlist);</code> </p>
<p> <code>int genders_attrlist_destroy(genders_t handle, char **attrlist);</code> </p>
<p> <code>int genders_vallist_create(genders_t handle, char ***vallist);</code> </p>
<p> <code>int genders_vallist_clear(genders_t handle, char **vallist);</code> </p>
<p> <code>int genders_vallist_destroy(genders_t handle, char **vallist);</code> </p>
<p> <code>int genders_getnodename(genders_t handle, char *node, int len);</code> </p>
<p> <code>int genders_getnodes(genders_t handle, char *nodes[], int len, const char *attr, const char *val);</code> </p>
<p> <code>int genders_getattr(genders_t handle, char *attrs[], char *vals[], int len, const char *node);</code> </p>
<p> <code>int genders_getattr_all(genders_t handle, char *attrs[], int len);</code> </p>
<p> <code>int genders_testattr(genders_t handle, const char *node, const char *attr, char *val, int len);</code> </p>
<p> <code>int genders_testattrval(genders_t handle, const char *node, const char *attr, const char *val);</code> </p>
<p> <code>int genders_isnode(genders_t handle, const char *node);</code> </p>
<p> <code>int genders_isattr(genders_t handle, const char *attr);</code> </p>
<p> <code>int genders_isattrval(genders_t handle, const char *attr, const char *val);</code> </p>
<p> <code>int genders_index_attrvals(genders_t handle, const char *attr);</code> </p>
<p> <code>int genders_query(genders_t handle, char *nodes[], int len, const char *query);</code> </p>
<p> <code>int genders_testquery(genders_t handle, const char *node, const char *query);</code> </p>
<p> <code>int genders_parse(genders_t handle, const char *filename, FILE *stream);</code> </p>
<h2>DESCRIPTION</h2>
<p> The genders library functions are a set of functions used to parse and retrieve data from a genders file. For API details, please see the individual manpages for each of the functions above, or read the comments written in /usr/include/genders.h. </p>
<h2>GENDERS FILE FORMAT</h2>
<p> Each line of the genders file has one of the following formats. See the section HOST RANGES below for information on host range formatting. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>nodename&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>attr[=value],attr[=value],&#8230;<br />
&nbsp;<wbr>&nbsp;<wbr>nodename1,nodename2,&#8230; attr[=value],attr[=value],&#8230;<br />
&nbsp;<wbr>&nbsp;<wbr>nodenames[A-B]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>attr[=value],attr[=value],&#8230; </p>
<p> The nodename(s) are the shortened hostnames of a node. This is followed by any number of spaces or tabs, and then the comma-separated list of attributes, each of which can optionally have a value. The substitution string &quot;%n&quot; can be used in an attribute value to represent the nodename. Nodenames can be listed on multiple lines, so a node&#8217;s attributes can be specified on multiple lines. However, no single node may have duplicate attributes. </p>
<p> There must be no spaces embedded in the attribute list and there is no provision for continuation lines. Commas and equal characters are special and cannot appear in attribute names or their values. Comments are prefixed with the hash chracter (#) and can appear anywhere in the file. The active genders file is typically found at /etc/genders or /admin/etc/genders. </p>
<p> Here is an example genders file from a small 16-node linux cluster: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>slc cluster genders file<br />
&nbsp;<wbr>&nbsp;<wbr>slci,slcj,slc[0-15]&nbsp;<wbr>&nbsp;<wbr>eth2=e%n,cluster=slc,all<br />
&nbsp;<wbr>&nbsp;<wbr>slci&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>passwdhost&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>slci,slcj&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>management<br />
&nbsp;<wbr>&nbsp;<wbr>slc[1-15]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>compute </p>
<h2>HOST RANGES</h2>
<p> As noted in sections above, the genders database accepts ranges of nodenames in the general form: prefix[n-m,l-k,&#8230;], where n &lt; m and l &lt; k, etc., as an alternative to explicit lists of nodenames. </p>
<p> This range syntax is meant only as a convenience on clusters with a prefixNN naming convention and specification of ranges should not be considered necessary &#8212; the list foo1,foo9 could be specified as such, or by the range foo[1,9]. </p>
<p> Some examples of range usage follow: </p>
<p> foo01,foo02,foo03,foo04,foo05: foo[01-05] </p>
<p> foo3,foo7,foo9,foo11: foo[3,7,9-11] </p>
<p> fooi,fooj,foo0,foo1,foo2: fooi,fooj,foo[0-2] </p>
<h2>FILES</h2>
<p> /usr/include/genders.h </p>
<p> /etc/genders</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-libgenders/">Libgenders</a>(3), <a href="/docs/linux/man/3-genders/">Genders</a>(3), <a href="/docs/linux/man/3-genders_handle_create/">genders_handle_create</a>(3), <a href="/docs/linux/man/3-genders_handle_destroy/">genders_handle_destroy</a>(3), <a href="/docs/linux/man/3-genders_load_data/">genders_load_data</a>(3), <a href="/docs/linux/man/3-genders_errnum/">genders_errnum</a>(3), <a href="/docs/linux/man/3-genders_strerror/">genders_strerror</a>(3), <a href="/docs/linux/man/3-genders_errormsg/">genders_errormsg</a>(3), <a href="/docs/linux/man/3-genders_perror/">genders_perror</a>(3), <a href="/docs/linux/man/3-genders_getnumnodes/">genders_getnumnodes</a>(3), <a href="/docs/linux/man/3-genders_getnumattrs/">genders_getnumattrs</a>(3), <a href="/docs/linux/man/3-genders_getmaxattrs/">genders_getmaxattrs</a>(3), <a href="/docs/linux/man/3-genders_getmaxnodelen/">genders_getmaxnodelen</a>(3), <a href="/docs/linux/man/3-genders_getmaxattrlen/">genders_getmaxattrlen</a>(3), <a href="/docs/linux/man/3-genders_getmaxvallen/">genders_getmaxvallen</a>(3), <a href="/docs/linux/man/3-genders_nodelist_create/">genders_nodelist_create</a>(3), <a href="/docs/linux/man/3-genders_nodelist_clear/">genders_nodelist_clear</a>(3), <a href="/docs/linux/man/3-genders_nodelist_destroy/">genders_nodelist_destroy</a>(3), <a href="/docs/linux/man/3-genders_attrlist_create/">genders_attrlist_create</a>(3), <a href="/docs/linux/man/3-genders_attrlist_clear/">genders_attrlist_clear</a>(3), <a href="/docs/linux/man/3-genders_attrlist_destroy/">genders_attrlist_destroy</a>(3), <a href="/docs/linux/man/3-genders_vallist_create/">genders_vallist_create</a>(3), <a href="/docs/linux/man/3-genders_vallist_clear/">genders_vallist_clear</a>(3), <a href="/docs/linux/man/3-genders_vallist_destroy/">genders_vallist_destroy</a>(3), <a href="/docs/linux/man/3-genders_getnodename/">genders_getnodename</a>(3), <a href="/docs/linux/man/3-genders_getnodes/">genders_getnodes</a>(3), <a href="/docs/linux/man/3-genders_getattr/">genders_getattr</a>(3), <a href="/docs/linux/man/3-genders_getattr_all/">genders_getattr_all</a>(3), <a href="/docs/linux/man/3-genders_testattr/">genders_testattr</a>(3), <a href="/docs/linux/man/3-genders_testattrval/">genders_testattrval</a>(3), <a href="/docs/linux/man/3-genders_testnode/">genders_testnode</a>(3), <a href="/docs/linux/man/3-genders_index_nodes/">genders_index_nodes</a>(3), <a href="/docs/linux/man/3-genders_index_attrs/">genders_index_attrs</a>(3), <a href="/docs/linux/man/3-genders_index_attrvals/">genders_index_attrvals</a>(3), <a href="/docs/linux/man/3-genders_query/">genders_query</a>(3), <a href="/docs/linux/man/3-genders_testquery/">genders_testquery</a>(3), <a href="/docs/linux/man/3-genders_parse/">genders_parse</a>(3) </p>
<h2>Index</h2>
