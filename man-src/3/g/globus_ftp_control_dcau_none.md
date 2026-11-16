---
title: "globus_ftp_control_dcau_none(3)"
name: "globus_ftp_control_dcau_none"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_control_dcau_none/"
description: "GridFTP Constants –"
---

<p>GridFTP Constants &#8211; </p>
<p> Constants.</p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_FTP_CONTROL_MODULE</code> (&amp;globus_i_ftp_control_module)<br />
 <i>Module descriptor. </i></p>
<h3>Typedefs</h3>
<p>typedef enum<br />
 <code>globus_ftp_control_type_e</code> <code>globus_ftp_control_type_t</code>&quot;<br />
 <i>GridFTP TYPE values. </i><br />
 typedef enum<br />
 <code>globus_ftp_control_mode_e</code> <code>globus_ftp_control_mode_t</code>&quot;<br />
 <i>GridFTP MODE values. </i><br />
 typedef enum<br />
 <code>globus_ftp_control_dcau_mode_e</code> <code>globus_ftp_control_dcau_mode_t</code>&quot;<br />
 <i>GridFTP DCAU values. </i><br />
 typedef enum<br />
 <code>globus_ftp_control_striping_mode_e</code> <code>globus_ftp_control_striping_mode_t</code>&quot;<br />
 <i>GridFTP Striping Types. </i></p>
<h3>Enumerations</h3>
<p>enum <code>globus_ftp_control_type_e</code> { <code>GLOBUS_FTP_CONTROL_TYPE_NONE</code>, <code>GLOBUS_FTP_CONTROL_TYPE_ASCII</code> = &#8216;A&#8217;, <code>GLOBUS_FTP_CONTROL_TYPE_EBCDIC</code> = &#8216;E&#8217;, <code>GLOBUS_FTP_CONTROL_TYPE_IMAGE</code> = &#8216;I&#8217;, <code>GLOBUS_FTP_CONTROL_TYPE_LOCAL</code> = &#8216;L&#8217; }<br />
 <i>GridFTP TYPE values. </i><br />
 enum <code>globus_ftp_control_mode_e</code> { <code>GLOBUS_FTP_CONTROL_MODE_NONE</code>, <code>GLOBUS_FTP_CONTROL_MODE_STREAM</code> = &#8216;S&#8217;, <code>GLOBUS_FTP_CONTROL_MODE_BLOCK</code> = &#8216;B&#8217;, <code>GLOBUS_FTP_CONTROL_MODE_EXTENDED_BLOCK</code> = &#8216;E&#8217;, <code>GLOBUS_FTP_CONTROL_MODE_COMPRESSED</code> = &#8216;C&#8217; }<br />
 <i>GridFTP MODE values. </i><br />
 enum <code>globus_ftp_control_dcau_mode_e</code> { <code>GLOBUS_FTP_CONTROL_DCAU_NONE</code> = &#8216;N&#8217;, <code>GLOBUS_FTP_CONTROL_DCAU_SELF</code> = &#8216;A&#8217;, <code>GLOBUS_FTP_CONTROL_DCAU_SUBJECT</code> = &#8216;S&#8217;, <code>GLOBUS_FTP_CONTROL_DCAU_DEFAULT</code> }<br />
 <i>GridFTP DCAU values. </i><br />
 enum <code>globus_ftp_control_striping_mode_e</code><br />
 <i>GridFTP Striping Types. </i><br />
 enum <code>globus_ftp_control_protection_t</code> { <code>GLOBUS_FTP_CONTROL_PROTECTION_CLEAR</code> = &#8216;C&#8217;, <code>GLOBUS_FTP_CONTROL_PROTECTION_SAFE</code> = &#8216;S&#8217;, <code>GLOBUS_FTP_CONTROL_PROTECTION_CONFIDENTIAL</code> = &#8216;E&#8217;, <code>GLOBUS_FTP_CONTROL_PROTECTION_PRIVATE</code> = &#8216;P&#8217; }<br />
 <i>GridFTP Protection Types. </i></p>
<h2>Detailed Description</h2>
<p>Constants. </p>
<h2>Typedef Documentation</h2>
<h3>typedef enum <code>globus_ftp_control_dcau_mode_e</code> <code>globus_ftp_control_dcau_mode_t</code></h3>
<p>GridFTP DCAU values. The enumeration values match the character value of the argument to DCAU.</p>
<h3>typedef enum <code>globus_ftp_control_mode_e</code> <code>globus_ftp_control_mode_t</code></h3>
<p>GridFTP MODE values. The enumeration values match the character value of the argument to MODE.</p>
<h3>typedef enum <code>globus_ftp_control_striping_mode_e</code> <code>globus_ftp_control_striping_mode_t</code></h3>
<p>GridFTP Striping Types. The enumeration values match the types of striping handled by the GridFTP server.</p>
<h3>typedef enum <code>globus_ftp_control_type_e</code> <code>globus_ftp_control_type_t</code></h3>
<p>GridFTP TYPE values. The enumeration values match the character value of the argument to TYPE.</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_ftp_control_dcau_mode_e</code></h3>
<p>GridFTP DCAU values. The enumeration values match the character value of the argument to DCAU. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_FTP_CONTROL_DCAU_NONE </i></dt>
<dd>No Authorization</dd>
<dt><i>GLOBUS_FTP_CONTROL_DCAU_SELF </i></dt>
<dd>Self Authorization</dd>
<dt><i>GLOBUS_FTP_CONTROL_DCAU_SUBJECT </i></dt>
<dd>Subject Authorization</dd>
<dt><i>GLOBUS_FTP_CONTROL_DCAU_DEFAULT </i></dt>
<dd>Default Authorization</dd></dl>
<h3>enum <code>globus_ftp_control_mode_e</code></h3>
<p>GridFTP MODE values. The enumeration values match the character value of the argument to MODE. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_FTP_CONTROL_MODE_NONE </i></dt>
<dd>Undefined MODE</dd>
<dt><i>GLOBUS_FTP_CONTROL_MODE_STREAM </i></dt>
<dd>Stream Mode</dd>
<dt><i>GLOBUS_FTP_CONTROL_MODE_BLOCK </i></dt>
<dd>Block Mode</dd>
<dt><i>GLOBUS_FTP_CONTROL_MODE_EXTENDED_BLOCK </i></dt>
<dd>Extended Block Mode</dd>
<dt><i>GLOBUS_FTP_CONTROL_MODE_COMPRESSED </i></dt>
<dd>Compressed Mode</dd></dl>
<h3>enum <code>globus_ftp_control_protection_t</code></h3>
<p>GridFTP Protection Types. The enumeration values match the types of protection handled by the GridFTP server. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_FTP_CONTROL_PROTECTION_CLEAR </i></dt>
<dd>Clear protection</dd>
<dt><i>GLOBUS_FTP_CONTROL_PROTECTION_SAFE </i></dt>
<dd>Safe (integrity) protection</dd>
<dt><i>GLOBUS_FTP_CONTROL_PROTECTION_CONFIDENTIAL </i></dt>
<dd>Confidential (encrypted) protection</dd>
<dt><i>GLOBUS_FTP_CONTROL_PROTECTION_PRIVATE </i></dt>
<dd>Private (integrity and encrypted) protection</dd></dl>
<h3>enum <code>globus_ftp_control_striping_mode_e</code></h3>
<p>GridFTP Striping Types. The enumeration values match the types of striping handled by the GridFTP server.</p>
<h3>enum <code>globus_ftp_control_type_e</code></h3>
<p>GridFTP TYPE values. The enumeration values match the character value of the argument to TYPE. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_FTP_CONTROL_TYPE_NONE </i></dt>
<dd>Undefined TYPE</dd>
<dt><i>GLOBUS_FTP_CONTROL_TYPE_ASCII </i></dt>
<dd>ASCII TYPE</dd>
<dt><i>GLOBUS_FTP_CONTROL_TYPE_EBCDIC </i></dt>
<dd>EBCDIC TYPE</dd>
<dt><i>GLOBUS_FTP_CONTROL_TYPE_IMAGE </i></dt>
<dd>Image TYPE</dd>
<dt><i>GLOBUS_FTP_CONTROL_TYPE_LOCAL </i></dt>
<dd>Local TYPE</dd></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_ftp_control from the source code.</p>
