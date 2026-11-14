---
title: "ibv_port_state_str(3)"
name: "ibv_port_state_str"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_port_state_str/"
---

<h2 class="name">NAME</h2>
 

 

 ibv_event_type_str - Return string describing event_type enum value 

 ibv_node_type_str - Return string describing node_type enum value 

 ibv_port_state_str - Return string describing port_state enum value 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/verbs.h&gt;
const char *ibv_event_type_str(enum ibv_event_type event_type);
const char *ibv_node_type_str(enum ibv_node_type node_type);
const char *ibv_port_state_str(enum ibv_port_state port_state);
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 ibv_node_type_str() returns a string describing the node type enum value node_type. 

 ibv_port_state_str() returns a string describing the port state enum value port_state. 

 ibv_event_type_str() returns a string describing the event type enum value event_type.

<h2>RETURN VALUE</h2>

 

 These functions return a constant string that describes the enum value passed as their argument.

<h2>AUTHOR</h2>

 

 Roland Dreier &lt;rolandd [at] cisco.com&gt; 

<h2>Index</h2>


