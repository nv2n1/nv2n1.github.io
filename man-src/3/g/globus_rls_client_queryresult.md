---
title: "globus_rls_client_queryresult(3)"
name: "globus_rls_client_queryresult"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_rls_client_queryresult/"
description: "Query Results –"
---

<h2 class="name">NAME</h2>
<p> Query Results &#8211; </p>
<p> List results are returned as globus_list_t&#8217;s, list datums depend on the type of query (eg <code>globus_rls_string2_t</code>, <code>globus_rls_attribute_t</code>, etc).</p>
<h3>Data Structures</h3>
<p> struct <code>globus_rls_attribute_object_t</code><br />
 <i></i><code>globus_rls_client_lrc_attr_search()</code> returns a list of these structures which include the object name (LFN or PFN) and attribute value found by the query.<br />
 struct <code>globus_rls_string2_t</code><br />
 <i>String pair result. </i><br />
 struct <code>globus_rls_string2_bulk_t</code><br />
 <i>String pair result with return code, returned by bulk query operations. </i></p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_rls_client_free_list</code> (globus_list_t *list) </p>
<h2>Detailed Description</h2>
<p> List results are returned as globus_list_t&#8217;s, list datums depend on the type of query (eg <code>globus_rls_string2_t</code>, <code>globus_rls_attribute_t</code>, etc). </p>
<p> A list result should be freed with <code>globus_rls_client_free_list()</code> when it&#8217;s no longer needed. RLS supports limiting the number of results returned by a single query using an offset and reslimit. The offset specifies which result to begin with, reslimit specifies how many results to return. Offset should begin at 0 to retrieve all records. If reslimit is 0 then all results are returned at once, unless the server has a limit on results configured. If NULL is passed as the offset argument then the API will repeatedly call the query function until are results are retrieved. The following are equivalent examples of how to print the lfn,pfn pairs returned by <code>globus_rls_client_lrc_get_lfn()</code>: </p>
<pre><code>
globus_list_t *str2_list;
globus_list_t *p;
globus_rls_string2_t *str2;
// Retrieve all results, API will handle looping through partial results
// if the server has a limit configured.  Error handling has been omitted.
globus_rls_client_lrc_get_lfn(h, "somepfn", NULL, 0, &amp;str2_list);
for (p = str2_list; p; p = globus_list_rest(p)) {
    str2 = (globus_rls_string2_t *)globus_list_first(p);
     printf("lfn: %s pfn:%s, str2-&gt;s1, str2-&gt;s2);
}
globus_rls_client_free_list(str2_list);
// This code fragment retrieves results 5 at a time.  Note offset is set
// to -1 when the server has no more results to return.
int offset = 0;
while (globus_rls_client_lrc_get_lfn(h, "somepfn", &amp;offset, 5, &amp;str2_list) == GLOBUS_SUCCESS) {
    for (p = str2_list; p; p = globus_list_rest(p)) {
        str2 = (globus_rls_string2_t *)globus_list_first(p);
       printf("lfn: %s pfn:%s, str2-&gt;s1, str2-&gt;s2);
    }
    globus_rls_client_free_list(str2_list);
    if (offset == -1)
        break;
}
.fi
</code></pre>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_rls_client_free_list (globus_list_t * list)</h3>
<p> Free result list returned by one of the query functions. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>list</i> List returned by one of the query functions.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> List and contents successfully freed.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus rls client from the source code. </p>
<h2>Index</h2>
