---
title: "netsnmp_utilities(3)"
name: "netsnmp_utilities"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_utilities/"
description: "utility_handlers – Simplify request processing A group of handlers intended to simplify certain aspects of processing a request for a MIB object."
---

<p>utility_handlers &#8211; Simplify request processing A group of handlers intended to simplify certain aspects of processing a request for a MIB object.</p>
<h3>Modules</h3>
<p><code>bulk_to_next</code><br />
 <i>Convert GETBULK requests into GETNEXT requests for the handler. </i><br />
 <code>cache_handler</code><br />
 <i>Maintains a cache of data for use by lower level handlers. </i><br />
 <code>debug</code><br />
 <i>Print out debugging information about the handler chain being called. </i><br />
 <code>mode_end_call</code><br />
 <i>At the end of a series of requests, call another handler hook. </i><br />
 <code>multiplexer</code><br />
 <i>Splits mode requests into calls to different handlers. </i><br />
 <code>read_only</code><br />
 <i>Make your handler read_only automatically The only purpose of this handler is to return an appropriate error for any requests passed to it in a SET mode. </i><br />
 <code>row_merge</code><br />
 <i>Calls sub handlers with request for one row at a time. </i><br />
 <code>serialize</code><br />
 <i>Calls sub handlers one request at a time. </i><br />
 <code>stash_to_next</code><br />
 <i>Convert GET_STASH requests into GETNEXT requests for the handler. </i> </p>
<h2>Detailed Description</h2>
<p>Simplify request processing A group of handlers intended to simplify certain aspects of processing a request for a MIB object. </p>
<p> These helpers do not implement any MIB objects themselves. Rather they handle specific generic situations, either returning an error, or passing a (possibly simpler) request down to lower level handlers.</p>
