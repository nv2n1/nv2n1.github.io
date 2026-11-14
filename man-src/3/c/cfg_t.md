---
title: "cfg_t(3)"
name: "cfg_t"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cfg_t/"
description: "cfg_t – Data structure holding information about a ‘section’."
---

<h2 class="name">NAME</h2>
<p> cfg_t &#8211; Data structure holding information about a &#8216;section&#8217;. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;confuse.h&gt; </p>
<h3>Data Fields</h3>
<p> cfg_flag_t <code>flags</code><br />
 <i>Any flags passed to </i><code>cfg_init()</code>.<br />
 char * <code>name</code><br />
 <i>The name of this section, the root section returned from </i><code>cfg_init()</code> is always named &#8216;root&#8217;.<br />
 <code>cfg_opt_t</code> * <code>opts</code><br />
 <i>Array of options. </i><br />
 char * <code>title</code><br />
 <i>Optional title for this section, only set if CFGF_TITLE flag is set. </i><br />
 char * <code>filename</code><br />
 <i>Name of the file being parsed. </i><br />
 int <code>line</code><br />
 <i>Line number in the config file. </i><br />
 <code>cfg_errfunc_t</code> <code>errfunc</code><br />
 <i>This function (if set with cfg_set_error_function) is called for any error message. </i></p>
<h2>Detailed Description</h2>
<p> Data structure holding information about a &#8216;section&#8217;. </p>
<p> Sections can be nested. A section has a list of options (strings, numbers, booleans or other sections) grouped together. </p>
<p> <code>Examples: </code> </p>
<p> <code>ftpconf.c</code>, <code>reread.c</code>, and <code>simple.c</code>.</p>
<h2>Field Documentation</h2>
<h3><code>cfg_errfunc_t</code> <code>cfg_t::errfunc</code></h3>
<p> This function (if set with cfg_set_error_function) is called for any error message. </p>
<p> Referenced by cfg_error(), cfg_init(), cfg_set_error_function(), and cfg_setopt(). </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for confuse from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Author</a></p>
<dd></dl>
