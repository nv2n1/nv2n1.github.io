---
title: "globus_rls_client_status(3)"
name: "globus_rls_client_status"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_rls_client_status/"
description: "Status Codes –"
---

<h2 class="name">NAME</h2>
<p> Status Codes &#8211; </p>
<p> All of the functions in the API that return status return it in a globus_result_t structure.</p>
<h3>Defines</h3>
<p> #define <code>GLOBUS_RLS_SUCCESS</code> 0 </p>
<p> #define <code>GLOBUS_RLS_GLOBUSERR</code> 1 </p>
<p> #define <code>GLOBUS_RLS_INVHANDLE</code> 2 </p>
<p> #define <code>GLOBUS_RLS_BADURL</code> 3 </p>
<p> #define <code>GLOBUS_RLS_NOMEMORY</code> 4 </p>
<p> #define <code>GLOBUS_RLS_OVERFLOW</code> 5 </p>
<p> #define <code>GLOBUS_RLS_BADARG</code> 6 </p>
<p> #define <code>GLOBUS_RLS_PERM</code> 7 </p>
<p> #define <code>GLOBUS_RLS_BADMETHOD</code> 8 </p>
<p> #define <code>GLOBUS_RLS_INVSERVER</code> 9 </p>
<p> #define <code>GLOBUS_RLS_MAPPING_NEXIST</code> 10 </p>
<p> #define <code>GLOBUS_RLS_LFN_EXIST</code> 11 </p>
<p> #define <code>GLOBUS_RLS_LFN_NEXIST</code> 12 </p>
<p> #define <code>GLOBUS_RLS_PFN_EXIST</code> 13 </p>
<p> #define <code>GLOBUS_RLS_PFN_NEXIST</code> 14 </p>
<p> #define <code>GLOBUS_RLS_LRC_EXIST</code> 15 </p>
<p> #define <code>GLOBUS_RLS_LRC_NEXIST</code> 16 </p>
<p> #define <code>GLOBUS_RLS_DBERROR</code> 17 </p>
<p> #define <code>GLOBUS_RLS_RLI_EXIST</code> 18 </p>
<p> #define <code>GLOBUS_RLS_RLI_NEXIST</code> 19 </p>
<p> #define <code>GLOBUS_RLS_MAPPING_EXIST</code> 20 </p>
<p> #define <code>GLOBUS_RLS_INV_ATTR_TYPE</code> 21 </p>
<p> #define <code>GLOBUS_RLS_ATTR_EXIST</code> 22 </p>
<p> #define <code>GLOBUS_RLS_ATTR_NEXIST</code> 23 </p>
<p> #define <code>GLOBUS_RLS_INV_OBJ_TYPE</code> 24 </p>
<p> #define <code>GLOBUS_RLS_INV_ATTR_OP</code> 25 </p>
<p> #define <code>GLOBUS_RLS_UNSUPPORTED</code> 26 </p>
<p> #define <code>GLOBUS_RLS_TIMEOUT</code> 27 </p>
<p> #define <code>GLOBUS_RLS_TOO_MANY_CONNECTIONS</code> 28 </p>
<p> #define <code>GLOBUS_RLS_ATTR_VALUE_NEXIST</code> 29 </p>
<p> #define <code>GLOBUS_RLS_ATTR_INUSE</code> 30 </p>
<h2>Detailed Description</h2>
<p> All of the functions in the API that return status return it in a globus_result_t structure. </p>
<p> Prior to version 2.0.0 an integer status was returned. The globus_result_t structure includes an integer &#8216;type&#8217; which is set to one of the status codes defined below (the same values that were returned by earlier versions of the API). The function <code>globus_rls_client_error_info()</code> may be used to extract the status code and/or error message from a globus_result_t. GLOBUS_SUCCESS is returned when the operation was successful.</p>
<h2>Define Documentation</h2>
<h3>#define GLOBUS_RLS_SUCCESS 0</h3>
<p> Operation succeeded.</p>
<h3>#define GLOBUS_RLS_GLOBUSERR 1</h3>
<p> An error was returned by the Globus I/O module.</p>
<h3>#define GLOBUS_RLS_INVHANDLE 2</h3>
<p> The <code>globus_rls_handle_t</code> handle is invalid.</p>
<h3>#define GLOBUS_RLS_BADURL 3</h3>
<p> The URL could not be parsed.</p>
<h3>#define GLOBUS_RLS_NOMEMORY 4</h3>
<p> Out of memory.</p>
<h3>#define GLOBUS_RLS_OVERFLOW 5</h3>
<p> A result was too large to fit in buffer.</p>
<h3>#define GLOBUS_RLS_BADARG 6</h3>
<p> Bad argument (eg NULL where string pointer expected).</p>
<h3>#define GLOBUS_RLS_PERM 7</h3>
<p> Client does not have permission for requested action.</p>
<h3>#define GLOBUS_RLS_BADMETHOD 8</h3>
<p> RPC error, invalid method name sent to server.</p>
<h3>#define GLOBUS_RLS_INVSERVER 9</h3>
<p> LRC request made to RLI server or vice versa.</p>
<h3>#define GLOBUS_RLS_MAPPING_NEXIST 10</h3>
<p> LFN,PFN (LRC) or LFN,LRC (RLI) mapping doesn&#8217;t exist.</p>
<h3>#define GLOBUS_RLS_LFN_EXIST 11</h3>
<p> LFN already exists in LRC or RLI database.</p>
<h3>#define GLOBUS_RLS_LFN_NEXIST 12</h3>
<p> LFN doesn&#8217;t exist in LRC or RLI database.</p>
<h3>#define GLOBUS_RLS_PFN_EXIST 13</h3>
<p> PFN already exists in LRC database.</p>
<h3>#define GLOBUS_RLS_PFN_NEXIST 14</h3>
<p> PFN doesn&#8217;t exist in LRC database.</p>
<h3>#define GLOBUS_RLS_LRC_EXIST 15</h3>
<p> LRC already exists in LRC or RLI database.</p>
<h3>#define GLOBUS_RLS_LRC_NEXIST 16</h3>
<p> LRC doesn&#8217;t exist in RLI database.</p>
<h3>#define GLOBUS_RLS_DBERROR 17</h3>
<p> Database error.</p>
<h3>#define GLOBUS_RLS_RLI_EXIST 18</h3>
<p> RLI already exists in LRC database.</p>
<h3>#define GLOBUS_RLS_RLI_NEXIST 19</h3>
<p> RLI doesn&#8217;t exist in LRC.</p>
<h3>#define GLOBUS_RLS_MAPPING_EXIST 20</h3>
<p> LFN,PFN (LRC) or LFN,LRC (RLI) mapping already exists.</p>
<h3>#define GLOBUS_RLS_INV_ATTR_TYPE 21</h3>
<p> Invalid attribute type, see globus_rls_attr_type_t.</p>
<h3>#define GLOBUS_RLS_ATTR_EXIST 22</h3>
<p> Attribute already exists.</p>
<h3>#define GLOBUS_RLS_ATTR_NEXIST 23</h3>
<p> Attribute doesn&#8217;t exist.</p>
<h3>#define GLOBUS_RLS_INV_OBJ_TYPE 24</h3>
<p> Invalid object type, see globus_rls_obj_type_t.</p>
<h3>#define GLOBUS_RLS_INV_ATTR_OP 25</h3>
<p> Invalid attribute search operator, see globus_rls_attr_op_t.</p>
<h3>#define GLOBUS_RLS_UNSUPPORTED 26</h3>
<p> Operation is unsupported.</p>
<h3>#define GLOBUS_RLS_TIMEOUT 27</h3>
<p> IO timeout.</p>
<h3>#define GLOBUS_RLS_TOO_MANY_CONNECTIONS 28</h3>
<p> Too many connections.</p>
<h3>#define GLOBUS_RLS_ATTR_VALUE_NEXIST 29</h3>
<p> Attribute with specified value not found.</p>
<h3>#define GLOBUS_RLS_ATTR_INUSE 30</h3>
<p> Attribute in use by some object, can&#8217;t be deleted.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus rls client from the source code. </p>
<h2>Index</h2>
