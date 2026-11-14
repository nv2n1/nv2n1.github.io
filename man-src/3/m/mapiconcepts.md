---
title: "mapiconcepts(3)"
name: "mapiconcepts"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mapiconcepts/"
description: "mapiconcepts – MAPI Concepts"
---

<h2 class="name">NAME</h2>
<p> mapiconcepts &#8211; MAPI Concepts </p>
<h3>MAPI objects</h3>
<p> Almost any MAPI data you access, read or edit is associated with an object. No matter whether you intend to browse mailbox hierarchy, open folders, create tables or access items (messages, appointments, contacts, tasks, notes), you will have to initialize and use MAPI objects: <i>object understanding and manipulation is fundamental</i>. </p>
<dl>
<dt>*</p>
<dd> When developing MAPI clients with Microsoft framework, instantiated objects inherit from parent classes. As a matter of fact, developers know which methods they can apply to objects and we suppose it makes their life easier.</p>
<dt>*</p>
<dd> In OpenChange, objects are opaque. They are generic data structures which content is set and accessed through MAPI public functions. Therefore, Linux MAPI developers must know what they are doing.</dl>
<p> An example of MAPI object manipulation is shown below: </p>
<pre><code>
mapi_object obj_store;
[...] mapi_object_init(&amp;obj_store);
retval = OpenMsgStore(&amp;obj_store);
if (retval != MAPI_E_SUCCESS) {
    mapi_errstr('OpenMsgStore', GetLastError());
    exit(1);
}
mapi_object_release(&amp;obj_store);
</code></pre>
<h3>MAPI Handles</h3>
<p> Beyond memory management considerations, understanding MAPI handles role in object manipulation provides a better understanding why <code>mapi_object_release()</code> matters. </p>
<p> Handles are temporary identifiers returned by Exchange when you access or create objects on the server. They are used to make reference to a particular object all along its session lifetime. They are stored in unsigned integers, are unique for each object but temporary along MAPI session. Handles are the only links between objects accessed on the client side and efficiently stored on the server side. </p>
<p> Although OpenChange MAPI makes handles manipulation transparent for developers, <code>mapi_object_release()</code> frees both the allocated memory for the object on client side, but also releases the object on the server. </p>
<h2>Index</h2>
