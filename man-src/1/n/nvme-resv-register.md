---
title: "nvme-resv-register(1)"
name: "nvme-resv-register"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-resv-register/"
---

<h2 class="name">NAME</h2>
 

 nvme-resv-register - Register an nvme reservation 

<h2>SYNOPSIS</h2>

 

 <pre>
<i>nvme resv-register</i> &lt;device&gt;
</pre>

<h2>DESCRIPTION</h2>

 

 The Reservation Register command is used to register, unregister, or replace a reservation key.

<h2>OPTIONS</h2>

 

 -n &lt;nsid&gt;, --namespace-id=&lt;nsid&gt;
<dl>
<dt>
<dd> Override the nsid field. If using the admin character device, this parameter is required.</dl>
 

 -c &lt;crkey&gt;, --crkey=&lt;crkey&gt;
<dl>
<dt>
<dd> Current Reservation Key: If the Reservation Register Action is 001b (i.e., Unregister Reservation Key) or 010b (i.e., Replace Reservation Key), then this field contains the current reservation key associated with the host. For all other Reservation Register Action values, this field is reserved. The controller ignores the value of this field when the Ignore Existing Key (IEKEY) bit is set to '1'.</dl>
 

 -k &lt;nrkey&gt;, --nrkey=&lt;nrkey&gt;
<dl>
<dt>
<dd> New Reservation Key: If the Reservation Register Action is 000b (i.e., Register Reservation Key) or 010b (i.e., Replace Reservation Key), then this field contains the new reservation key associated with the host. For all other Reservation Register Action values, this field is reserved.</dl>
 

 -p &lt;cptpl&gt;, --cptpl=&lt;cptpl&gt;
<dl>
<dt>
<dd> Change Persist Through Power Loss State: This field allows the Persist Through Power Loss state associated with the namespace to be modified as a side effect of processing this command. <table BORDER> <tr VALIGN=top><td> Value </td><td> Definition 
</td></tr> <tr VALIGN=top><td> 0 </td><td> No change to PTPL state 
</td></tr> <tr VALIGN=top><td> 1 </td><td> Reserved 
</td></tr> <tr VALIGN=top><td> 2 </td><td> Set PTPL state to '0'. Reservations are released and registrants are cleared on a power on. 
</td></tr> <tr VALIGN=top><td> 3 </td><td> Set PTPL state to '1'. Reservations and registrants persist across a power loss. 
</td></tr> </table> 

</dl>
 

 -a &lt;rrega&gt;, --rrega=&lt;rrega&gt;
<dl>
<dt>
<dd> Reservation Register Action: This field specifies the registration action that is performed by the command. <table BORDER> <tr VALIGN=top><td> Value </td><td> Definition 
</td></tr> <tr VALIGN=top><td> 0 </td><td> Register Reservation Key 
</td></tr> <tr VALIGN=top><td> 1 </td><td> Unregister Reservation Key 
</td></tr> <tr VALIGN=top><td> 2 </td><td> Replace Reservation Key 
</td></tr> <tr VALIGN=top><td> 3-7 </td><td> Reserved 
</td></tr> </table> 

</dl>
 

 -i, --iekey
<dl>
<dt>
<dd> Ignore Existing Key: If this bit is set to a <i>1</i>, then the Current Reservation Key (CRKEY) check is disabled and the command shall succeed regardless of the CRKEY field value. 

 Indicator option, defaults to <i>0</i>.</dl>

<h2>EXAMPLES</h2>

 

 No examples yet

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


