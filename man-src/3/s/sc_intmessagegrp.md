---
title: "sc_intmessagegrp(3)"
name: "sc_intmessagegrp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_intmessagegrp/"
description: "sc::intMessageGrp –"
---

<p>sc::intMessageGrp &#8211; </p>
<p> Uses integer message types to send and receive messages.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;message.h&gt;</code></pre>
<p> Inherits <code>sc::MessageGrp</code>. Inherited by <code>sc::ShmMessageGrp</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>void raw_send (int target, const void *data, int nbyte)



void raw_recv (int sender, void *data, int nbyte)



void raw_sendt (int target, int type, const void *data, int nbyte)



void raw_recvt (int type, void *data, int nbyte)



int probet (int)


Ask if a given typed message has been received.


int leftover_ctl_bits ()



Protected Member Functions
int msgtype_typ (int msgtype)



int typ_msgtype (int usrtype)



int seq_msgtype (int source, int seq)



virtual void basic_send (int target, int type, const void *data, int nbyte)=0


Must be implemented by specializations.


virtual void basic_recv (int type, void *data, int nbyte)=0


Must be implemented by specializations.


virtual int basic_probe (int type)=0


Must be implemented by specializations.


intMessageGrp (const Ref&lt; KeyVal &gt; &amp;)



void initialize (int me, int n, int nbits)



Protected Attributes
int msgtype_nbit



int ctl_nbit



int seq_nbit



int typ_nbit



int src_nbit



int ctl_mask



int seq_mask



int typ_mask



int src_mask



int ctl_shift



int seq_shift



int typ_shift



int src_shift



int * source_seq



int * target_seq</code></pre>
<h2>Detailed Description</h2>
<p>Uses integer message types to send and receive messages. </p>
<p> Message group specializations that use the MPI library and the Paragon NX can be conveniently implemented in terms of this.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
