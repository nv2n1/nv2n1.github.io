---
title: "ncl_gescape(3)"
name: "ncl_gescape"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gescape/"
description: "gescape (Escape) – provides a standard way of implementing nonstandard GKS features. NCAR GKS has only two user-accessible escape functions defined: one for changing the name of a metafile and anot..."
---

<p>gescape (Escape) &#8211; provides a standard way of implementing nonstandard GKS features. NCAR GKS has only two user-accessible escape functions defined: one for changing the name of a metafile and another for pausing in an X window.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gescape(Gint func_id, const Gescape_in_data *in_data, Gstore *store_data,Gescape_out_data **out_data);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>func_id</p>
<dd>(Input) &#8211; A function identifier specifying the requested activity. The legal values for func_id are &quot;-1391&quot; for changing a metafile name and &quot;-1396&quot; for effecting a pause in an X window.</p>
<dt>in_data.escape_r1.size</p>
<dd>(size_t, Input) &#8211; Size of the input data record array (for input data record, see below).</p>
<dt>in_data.escape_r1.data</p>
<dd>(void *, Input) &#8211; Input data record. For calls to gescape with func_id equal to -1391 the input data record should be a character string containing the desired metafile name left justified and blank filled; for calls to gescape with func_id equal to -1396 the input data record should be a character string containing the workstation identifier encoded as a five character number.</p>
<dt>store_data</p>
<dd>(void *, Input) &#8211; Storage for output data. Not currently in use for NCAR GKS.</p>
<dt>out_data.escape_r1.size</p>
<dd>(size_t, Output) &#8211; Size of the output data record array. Not currently in use for NCAR GKS.</p>
<dt>out_data.escape_r1.data</p>
<dd>(void *, Output) &#8211; Output data record. Not currently in use for NCAR GKS.</dl>
<h2>Usage</h2>
<p>The sizes of the data records must always be at least &quot;1&quot; in value.</p>
<h2>Examples</h2>
<p>gescape can be used to dynamically change the name of an output metafile and to do so one should use the calls gopen_gks and gopen_ws instead of c_opngks. If you are using c_opngks, see the man page for setusv(3NCARG) for changing the name of the metafile. </p>
<p> To change the name of the output metafile inside your program, you should make a call similar to the following: </p>
<pre> int str_len = 12;
 Gescape_in_data in_data;
 gopen_gks(&quot;stdout&quot;,0);
 in_data.escape_r1.data = (Gdata *)malloc(str_len*sizeof(char));
 strcpy(in_data.escape_r1.data, &quot;new.cgm.name&quot; );
 in_data.escape_r1.size = str_len;
 gescape(-1391,&amp;in_data,NULL,NULL);</pre>
<p>The call to gescape to change the metafile name must always occur just before the call to gopen_ws that opens a CGM workstation. Setting the environment variable NCARG_GKS_OUTPUT overrides any attempt to change the name of an output metafile via a gescape call. </p>
<p> See the &quot;User&#8217;s Guide for NCAR GKS-0A Graphics&quot; for a more complete example of changing metafile names from within a code. </p>
<p> Here is an example of a piece of code that will create an X window, draw a line, and then pause waiting for a mouse click or a key click. </p>
<pre> Gescape_in_data in_data;
 int str_len = 5;
 gopen_gks(&quot;stdout&quot;,0);
 gopen_ws(3,NULL,8);
 <a href="//www.systutorials.com/docs/linux/man/3-gactivate_ws/">gactivate_ws</a>(3);
 c_line(0.,0.,1.,1.);
 c_sflush();
 in_data.escape_r1.data = (Gdata *)malloc(str_len*sizeof(char));
 strcpy(in_data.escape_r1.data, &quot; 3&quot; );
 in_data.escape_r1.size = str_len;
 gescape(-1396,&amp;in_data,NULL,NULL);
 <a href="//www.systutorials.com/docs/linux/man/3-gdeactivate_ws/">gdeactivate_ws</a>(3);
 <a href="//www.systutorials.com/docs/linux/man/3-gclose_ws/">gclose_ws</a>(3);
 gclose_gks();</pre>
<p>The functions c_frame and c_ngpict are in general much easier to use and more flexible than the direct ESCAPE call for pausing in an X window. It is suggested that those functions be used.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>setusv(3NCARG),</code> <code>frame(3NCARG),</code> <code>ngpict(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG)</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
