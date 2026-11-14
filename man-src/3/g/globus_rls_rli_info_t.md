---
title: "globus_rls_rli_info_t(3)"
name: "globus_rls_rli_info_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_rls_rli_info_t/"
description: "globus_rls_rli_info_t –"
---

<h2 class="name">NAME</h2>
<p> globus_rls_rli_info_t &#8211; </p>
<p> Information about RLI server, returned by <code>globus_rls_client_lrc_rli_info()</code> and <code>globus_rls_client_lrc_rli_list()</code>.</p>
<h2>SYNOPSIS</h2>
<h3>Data Fields</h3>
<p> char <code>url</code> [256] </p>
<p> int <code>updateinterval</code> </p>
<p> int <code>flags</code> </p>
<p> time_t <code>lastupdate</code> </p>
<h2>Detailed Description</h2>
<p> Information about RLI server, returned by <code>globus_rls_client_lrc_rli_info()</code> and <code>globus_rls_client_lrc_rli_list()</code>.</p>
<h2>Field Documentation</h2>
<h3>char <code>globus_rls_rli_info_t::url</code>[256]</h3>
<p> URL of server.</p>
<h3>int <code>globus_rls_rli_info_t::updateinterval</code></h3>
<p> Interval between softstate updates.</p>
<h3>int <code>globus_rls_rli_info_t::flags</code></h3>
<p> RLI flags (see <code>FRLI_BLOOMFILTER</code>).</p>
<h3>time_t <code>globus_rls_rli_info_t::lastupdate</code></h3>
<p> Time of last softstate update. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus rls client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAK">Author</a></p>
<dd></dl>
