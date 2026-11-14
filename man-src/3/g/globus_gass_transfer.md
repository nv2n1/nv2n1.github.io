---
title: "globus_gass_transfer(3)"
name: "globus_gass_transfer"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gass_transfer/"
description: "GASS Transfer API –"
---

<h2 class="name">NAME</h2>
<p> GASS Transfer API &#8211; </p>
<p> GASS Transfer API.</p>
<h3>Modules</h3>
<p> <code>Activation</code> </p>
<p> <code>Client-Initiated Operations</code><br />
 <i>GASS Transfer Client Operations. </i><br />
 <code>Implementing Servers</code><br />
 <i>GASS Server Implementation. </i><br />
 <code>Referrals</code><br />
 <i>GASS Referrals. </i><br />
 <code>Request Handles</code><br />
 <i>Request Handles. </i><br />
 <code>Request Attributes</code> </p>
<p> <code>Listener attributes</code> </p>
<p> <code>Implementing Request Attributes</code> </p>
<p> <code>Protocol Modules</code><br />
 <i>Protocol Implementation API. </i></p>
<h2>Detailed Description</h2>
<p> GASS Transfer API. </p>
<p> The GASS Transfer API is the core part of the GASS (Global Access to Secondary Storage) component of the Globus Toolkit. The purpose of GASS is to provide a simple way to enable grid applications to securely stage and access data to and from remote file servers using a simple protocol-independent API. </p>
<p> The GASS Transfer API provides a way to implement both <code>client</code> and <code>server</code> components. These share common data block and request management functionality. Client-specific functions are provided to implement file &#8216;get&#8217;, &#8216;put&#8217;, and &#8216;append&#8217; operations. Server-specific functions are provided to implement servers which service such requests. Client and server functionality can be included in a single application, so one could implement proxies or cross-protocol bridges. </p>
<p> The GASS Transfer API is easily extensible to support different remote data access protocols. The standard Globus distribution includes client-side support for the http, and https protocols, as well as server-side support for the http and https protocols. An application which requires additional protocol support may add this through the <code>protocol module interface</code>. </p>
<p> The GASS Transfer API is defined in the header file &#8216;globus_gass_transfer.h&#8217; </p>
<p> The <code>GLOBUS_GASS_TRANSFER_MODULE</code> must be activated before calling any functions in this API.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gass_transfer from the source code. </p>
<h2>Index</h2>
