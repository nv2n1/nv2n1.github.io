---
title: "globus_rls_sender_info_t(3)"
name: "globus_rls_sender_info_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_rls_sender_info_t/"
description: "globus_rls_sender_info_t –"
---

<h2 class="name">NAME</h2>
<p> globus_rls_sender_info_t &#8211; </p>
<p> Information about server sending updates to an rli, returned by <code>globus_rls_client_rli_sender_list()</code>.</p>
<h2>SYNOPSIS</h2>
<h3>Data Fields</h3>
<p> char <code>url</code> [256] </p>
<p> time_t <code>lastupdate</code> </p>
<h2>Detailed Description</h2>
<p> Information about server sending updates to an rli, returned by <code>globus_rls_client_rli_sender_list()</code>.</p>
<h2>Field Documentation</h2>
<h3>char <code>globus_rls_sender_info_t::url</code>[256]</h3>
<p> URL of server.</p>
<h3>time_t <code>globus_rls_sender_info_t::lastupdate</code></h3>
<p> Time of last softstate update. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus rls client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Author</a></p>
<dd></dl>
