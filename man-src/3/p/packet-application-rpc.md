---
title: "packet-application-rpc(3)"
name: "packet-application-rpc"
section: "3"
letter: "p"
url: "/docs/linux/man/3-packet-application-rpc/"
description: "packet.application.rpc – RPC module"
---

<p>packet.application.rpc &#8211; RPC module</p>
<h2>Description</h2>
<p>Decode RPC layer.</p>
<h2>Classes</h2>
<h3>class Header(baseobj.BaseObj)</h3>
<pre>Header object
<code>Methods defined here:</code>
---------------------
<code>__init__(self, size, last_fragment)</code>
Constructor which takes the size and last fragment as inputs</pre>
<h3>class Prog(baseobj.BaseObj)</h3>
<pre>Prog object
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code>
Constructor which takes the Unpack object as input</pre>
<h3>class RPC(packet.application.gss.GSS)</h3>
<pre>RPC object
Usage:
 from packet.application.rpc import RPC
 # Decode the RPC header
 x = RPC(pktt_obj, proto=6)
 # Decode NFS layer
 nfs = x.decode_payload()
Object definition:
RPC(
 [
 # If TCP
 fragment_hdr = Header(
 last_fragment = int,
 size = int,
 ),
 ]
 xid = int,
 type = int,
 [
 # If type == 0 (RPC call)
 rpc_version = int,
 program = int,
 version = int,
 procedure = int,
 credential = Credential(
 data = string,
 flavor = int,
 size = int,
 ),
 verifier = Credential(
 data =string,
 flavor = int,
 size = int,
 ),
 ] | [
 # If type == 1 (RPC reply)
 reply_status = int,
 [
 # If reply_status == 0
 verifier = Credential(
 data = string,
 flavor = int,
 size = int,
 ),
 accepted_status = int,
 [
 # If accepted_status == 2
 prog_mismatch = Prog(
 low = int,
 high = int,
 )
 ]
 ] | [
 # If reply_status != 0
 rejected_status = int,
 [
 # If rejected_status == 0
 prog_mismatch = Prog(
 low = int,
 high = int,
 )
 ] | [
 # If rejected_status != 0
 auth_status = int,
 ]
 ]
 ]
 [data = string] # raw data of payload if unable to decode
)
<code>Methods defined here:</code>
---------------------
<code>__init__(self, pktt, proto, state=True)</code>
Constructor
Initialize object's private data.
<dl><dt><dd><dl><dt><code>pktt:</code>
<dd>Packet trace object (packet.pktt.Pktt) so this layer has
access to the parent layers.
<dt><code>proto:</code>
<dd>Transport layer protocol.
<dt><code>state:</code>
<dd>Save call state. [default: True]
</dl></dl>
<code>__nonzero__(self)</code>
Truth value testing for the built-in operation bool()
<code>__str__(self)</code>
String representation of object
The representation depends on the verbose level set by debug_repr().
If set to 0 the generic object representation is returned.
If set to 1 the representation of the object is:
 'RPC call program: 100003, version: 4, procedure: 0, xid: 0xe37d3d5 '
If set to 2 the representation of the object is as follows:
 'CALL(0), program: 100003, version: 4, procedure: 0, xid: 0xe37d3d5'
<code>decode_payload(self)</code>
Decode RPC load
For RPC calls it is easy to decide if the RPC payload is an NFS packet
since the RPC program is in the RPC header, which for NFS the
program number is 100003. On the other hand, for RPC replies the RPC
header does not have any information on what the payload is, so the
transaction ID (xid) is used to map the replies to their calls and
thus deciding if RPC payload is an NFS packet or not.
This is further complicated when trying to decode callbacks, since
the program number for callbacks could be any number in the transient
program range [0x40000000, 0x5FFFFFFF]. Therefore, any program number
in the transient range is considered a callback and if the decoding
succeeds then this is an NFS callback, otherwise it is not.
Since the RPC replies do not contain any information about what type
of payload, when they are decoded correctly as NFS replies this
information is inserted in the RPC (pkt.rpc) object.
This information includes program number, RPC version, procedure
number as well as the call_index which is the packet index of its
corresponding call for each reply.
x.pkt.nfs = &lt;NFSobject&gt;
where &lt;NFSobject&gt; is an object of type COMPOUND4args or COMPOUND4res
class COMPOUND4args(
 tag = string,
 minorversion = int,
 argarray = [],
)
The argarray is a list of nfs_argop4 objects:
class nfs_argop4(
 argop = int,
 [&lt;opobject&gt; = &lt;opargobject&gt;,]
)
where opobject could be opsequence, opgetattr, etc., and opargobject
is the object which has the arguments for the given opobject, e.g.,
SEQUENCE4args, GETATTR4args, etc.
class COMPOUND4res(
 tag = string,
 status = int,
 resarray = [],
)
The resarray is a list of nfs_resop4 objects:
class nfs_resop4(
 resop = int,
 [&lt;opobject&gt; = &lt;opresobject&gt;,]
)
where opobject could be opsequence, opgetattr, etc., and opresobject
is the object which has the results for the given opobject, e.g.,
SEQUENCE4res, GETATTR4res, etc.</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-baseobj/">baseobj</a>(3),</code> <code><a href="/docs/linux/man/3-packet-application-gss/">packet.application.gss</a>(3),</code> <code><a href="/docs/linux/man/3-packet-nfs-mount3/">packet.nfs.mount3</a>(3),</code> <code><a href="/docs/linux/man/3-packet-nfs-nfs/">packet.nfs.nfs</a>(3),</code> <code><a href="/docs/linux/man/3-packet-nfs-nlm4/">packet.nfs.nlm4</a>(3),</code> <code><a href="/docs/linux/man/3-packet-nfs-portmap2/">packet.nfs.portmap2</a>(3)</code> </p>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
