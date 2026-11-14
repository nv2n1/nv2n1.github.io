---
title: "drmaa_viter(3)"
name: "drmaa_viter"
section: "3"
letter: "d"
url: "/docs/linux/man/3-drmaa_viter/"
description: "Vector iteration functions. –"
---

<h2 class="name">NAME</h2>
<p> Vector iteration functions. &#8211; </p>
<p> The drmaa_get_next_<i>X</i>() functions SHALL store up to <i>value_len</i> bytes of the next attribute name / attribute value / job identifier from the <i>values</i> opaque string vector in the <i>value</i> buffer. The drmaa_get_next_<i>X</i>() functions SHALL store up to <i>value_len</i> bytes of the next attribute name / attribute value / job identifier from the <i>values</i> opaque string vector in the <i>value</i> buffer. </p>
<p> The opaque string vector&#8217;s internal iterator SHALL then be moved forward to the next entry. If there are no more values those functions return <code>DRMAA_ERRNO_INVALID_ARGUMENT</code> (but this is outside DRMAA specification). </p>
<p> The drmaa_get_num_<i>X</i>() functions SHALL store the number of elements in the space provided by <i>size</i>. </p>
<p> The drmaa_release_<i>X</i>() functions free the memory used by the <i>values</i> opaque string vector. All memory used by strings contained therein is also freed. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for torque from the source code. </p>
<h2>Index</h2>
