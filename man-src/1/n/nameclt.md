---
title: "nameclt(1)"
name: "nameclt"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nameclt/"
description: "nameclt – Naming Service client"
---

<h2 class="name">NAME</h2>
<p> nameclt &#8211; Naming Service client</p>
<h2>SYNOPSIS</h2>
<p> <code>nameclt</code> [-ior &lt;object-reference&gt;] [-advanced] &lt;operation&gt; </p>
<h2>DESCRIPTION</h2>
<p> The nameclt command invokes operations on the Naming Service. The allowed operations are:</p>
<dl>
<dl>
<dt>list&nbsp;<wbr>&lt;context-name&gt;</dt>
<dd> lists contexts and objects bound in the context with the specified name.</dd>
<dt>bind_new_context&nbsp;<wbr>&lt;context-name&gt;</dt>
<dd> binds name to a new context, and returns the stringified context IOR.</dd>
<dt>remove_context&nbsp;<wbr>&lt;context-name&gt;</dt>
<dd> unbinds and destroys the named context, as long as it is empty.</dd>
<dt>bind&nbsp;<wbr>&lt;object-name&gt;&nbsp;<wbr>&lt;stringified-IOR&gt;</dt>
<dd> binds name to object.</dd>
<dt>unbind&nbsp;<wbr>&lt;object-name&gt;</dt>
<dd> unbinds name and object.</dd>
<dt>resolve&nbsp;<wbr>&lt;object-name&gt;</dt>
<dd> returns stringified IOR bound to specified name.</dd></dl>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-ior NameService-object-reference</code></dt>
<dd> Use the given stringified IOR as the &quot;root&quot; context of the naming service. By default, nameclt uses the object reference returned by calling CORBA::ORB::resolve_initial_references(&quot;NameService&quot;).</dd>
<dt><code>-advanced</code></dt>
<dd> Allow advanced operations. These are operations which should not normally need to be used. They may however be useful for testing the naming service and also for cleaning up in the event of a client messing up the namespace. The operations are:</dd>
<dl>
<dl>
<dt>bind_context&nbsp;<wbr>&lt;context-name&gt;&nbsp;<wbr>&lt;stringified-IOR&gt;</dt>
<dd> binds name to context.</dd>
<dt>rebind&nbsp;<wbr>&lt;object-name&gt;&nbsp;<wbr>&lt;stringified-IOR&gt;</dt>
<dd> binds name to object even if binding already exists.</dd>
<dt>rebind_context&nbsp;<wbr>&lt;context-name&gt;&nbsp;<wbr>&lt;stringified-IOR&gt;</dt>
<dd> binds name to context even if binding already exists.</dd>
<dt>new_context</dt>
<dd> returns stringified IOR for a new context.</dd>
<dt>destroy</dt>
<dd> destroys the naming context given with -ior flag.</dd></dl>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> omniNames(1) </p>
<h2>AUTHOR</h2>
<p> Tristan Richardson, ORL (Olivetti &amp; Oracle Research Laboratory) </p>
