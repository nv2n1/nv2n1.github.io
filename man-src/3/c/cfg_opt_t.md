---
title: "cfg_opt_t(3)"
name: "cfg_opt_t"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cfg_opt_t/"
description: "cfg_opt_t – Data structure holding information about an option."
---

<h2 class="name">NAME</h2>
<p> cfg_opt_t &#8211; Data structure holding information about an option. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;confuse.h&gt; </p>
<h3>Data Fields</h3>
<p> char * <code>name</code><br />
 <i>The name of the option. </i><br />
 <code>cfg_type_t</code> <code>type</code><br />
 <i>Type of option. </i><br />
 unsigned int <code>nvalues</code><br />
 <i>Number of values parsed. </i><br />
 <code>cfg_value_t</code> ** <code>values</code><br />
 <i>Array of found values. </i><br />
 cfg_flag_t <code>flags</code><br />
 <i>Flags. </i><br />
 <code>cfg_opt_t</code> * <code>subopts</code><br />
 <i>Suboptions (only applies to sections). </i><br />
 <code>cfg_defvalue_t</code> <code>def</code><br />
 <i>Default value. </i><br />
 <code>cfg_func_t</code> <code>func</code><br />
 <i>Function callback for CFGT_FUNC options. </i><br />
 void * <code>simple_value</code><br />
 <i>Pointer to user-specified variable to store simple values (created with the CFG_SIMPLE_* initializers). </i><br />
 <code>cfg_callback_t</code> <code>parsecb</code><br />
 <i>Value parsing callback function. </i><br />
 <code>cfg_validate_callback_t</code> <code>validcb</code><br />
 <i>Value validating callback function. </i><br />
 <code>cfg_print_func_t</code> <code>pf</code><br />
 <i>print callback function </i></p>
<h2>Detailed Description</h2>
<p> Data structure holding information about an option. </p>
<p> The value(s) are stored as an array of fundamental values (strings, numbers, etc). </p>
<p> <code>Examples: </code> </p>
<p> <code>ftpconf.c</code>, <code>reread.c</code>, and <code>simple.c</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for confuse from the source code. </p>
<h2>Index</h2>
