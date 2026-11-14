---
title: "voms(3)"
name: "voms"
section: "3"
letter: "v"
url: "/docs/linux/man/3-voms/"
description: "voms –"
---

<p>voms &#8211;</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;voms_api.h&gt;

Public Member Functions
voms (const voms &amp;)



voms ()



voms &amp; operator= (const voms &amp;)



~voms ()



AC * GetAC ()



std::vector&lt; attributelist &gt; &amp; GetAttributes ()



std::vector&lt; std::string &gt; GetTargets ()



Data Fields
int version



int siglen



std::string signature



std::string user



std::string userca



std::string server



std::string serverca



std::string voname



std::string uri



std::string date1



std::string date2



data_type type



std::vector&lt; data &gt; std



std::string custom



std::vector&lt; std::string &gt; fqan



std::string serial



Friends</code></pre>
<p> class <code>vomsdata</code> </p>
<p> int <code>TranslateVOMS</code> (struct vomsdatar *vd, std::vector&lt; <code>voms</code> &gt; &amp;v, int *error)</p>
<h2>Detailed Description</h2>
<p>Definition at line 98 of file voms_api.h.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>voms::voms (const <code>voms</code> &amp;)</h3>
<h3>voms::voms ()</h3>
<h3>voms::~voms ()</h3>
<h2>Member Function Documentation</h2>
<h3>AC* voms::GetAC ()</h3>
<h3>std::vector&lt;<code>attributelist</code>&gt;&amp; voms::GetAttributes ()</h3>
<p>Generic attributes</p>
<h3>std::vector&lt;std::string&gt; voms::GetTargets ()</h3>
<h3><code>voms</code>&amp; voms::operator= (const <code>voms</code> &amp;)</h3>
<h2>Friends And Related Function Documentation</h2>
<h3>int TranslateVOMS (struct vomsdatar *vd, std::vector&lt; <code>voms</code> &gt; &amp;v, int *error) [friend]</h3>
<h3>friend class <code>vomsdata</code> [friend]</h3>
<p>Definition at line 99 of file voms_api.h.</p>
<h2>Field Documentation</h2>
<h3>std::string voms::custom</h3>
<p>The data returned by an S command </p>
<p> Definition at line 113 of file voms_api.h.</p>
<h3>std::string voms::date1</h3>
<p>Beginning of validity of the user info </p>
<p> Definition at line 109 of file voms_api.h.</p>
<h3>std::string voms::date2</h3>
<p>End of validity of the user info </p>
<p> Definition at line 110 of file voms_api.h.</p>
<h3>std::vector&lt;std::string&gt; voms::fqan</h3>
<p>Keeps the data in the compact format </p>
<p> Definition at line 115 of file voms_api.h.</p>
<h3>std::string voms::serial</h3>
<p>Serial number. &#8216;0&#8217; if coming from non-ac </p>
<p> Definition at line 116 of file voms_api.h.</p>
<h3>std::string voms::server</h3>
<p>The VOMS server DN, as from its certificate </p>
<p> Definition at line 105 of file voms_api.h.</p>
<h3>std::string voms::serverca</h3>
<p>The CA which signed the VOMS certificate </p>
<p> Definition at line 106 of file voms_api.h.</p>
<h3>int voms::siglen</h3>
<p>The length of the VOMS server signature </p>
<p> Definition at line 101 of file voms_api.h.</p>
<h3>std::string voms::signature</h3>
<p>The VOMS server signature </p>
<p> Definition at line 102 of file voms_api.h.</p>
<h3>std::vector&lt;<code>data</code>&gt; voms::std</h3>
<p>User&#8217;s characteristics </p>
<p> Definition at line 112 of file voms_api.h.</p>
<h3><code>data_type</code> voms::type</h3>
<p>The type of data returned </p>
<p> Definition at line 111 of file voms_api.h.</p>
<h3>std::string voms::uri</h3>
<p>The URI of the VOMS server </p>
<p> Definition at line 108 of file voms_api.h.</p>
<h3>std::string voms::user</h3>
<p>The user&#8217;s DN, as from his certificate </p>
<p> Definition at line 103 of file voms_api.h.</p>
<h3>std::string voms::userca</h3>
<p>The CA which signed the user&#8217;s certificate </p>
<p> Definition at line 104 of file voms_api.h.</p>
<h3>int voms::version</h3>
<p>0 means data didn&#8217;t originate from an AC </p>
<p> Definition at line 100 of file voms_api.h.</p>
<h3>std::string voms::voname</h3>
<p>The name of the VO to which the VOMS belongs </p>
<p> Definition at line 107 of file voms_api.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for VOMS CC API from the source code.</p>
