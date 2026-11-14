---
title: "nvme-resv-acquire(1)"
name: "nvme-resv-acquire"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-resv-acquire/"
---

<h2 class="name">NAME</h2>
 

 nvme-resv-acquire - Acquire an nvme reservation 

<h2>SYNOPSIS</h2>

 

 <pre>
<i>nvme resv-acquire</i> &lt;device&gt;
</pre>

<h2>DESCRIPTION</h2>

 

 The Reservation Acquire command is used to acquire a reservation on a namespace, preempt a reservation held on a namespace, and abort a reservation held on a namespace.

<h2>OPTIONS</h2>

 

 -n &lt;nsid&gt;, --namespace-id=&lt;nsid&gt;
<dl>
<dt>
<dd> Override the nsid field. If using the admin character device, this parameter is required.</dl>
 

 -c &lt;crkey&gt;, --crkey=&lt;crkey&gt;
<dl>
<dt>
<dd> Current Reservation Key: The field specifies the current reservation key associated with the host. If the IEKEY bit is set to '1' in the command, then the CRKEY check succeeds regardless of the value in this field.</dl>
 

 -p &lt;prkey&gt;, --prkey=&lt;prkey&gt;
<dl>
<dt>
<dd> Preempt Reservation Key: If the Reservation Acquire Action is set to 001b (i.e., Preempt) or 010b (i.e., Preempt and Abort), then this field specifies the reservation key to be unregistered from the namespace. For all other Reservation Acquire Action values, this field is reserved.</dl>
 

 -t &lt;rtype&gt;, --rtyep=&lt;rtype&gt;
<dl>
<dt>
<dd> Reservation Type: This field specifies the type of reservation to be created. <table BORDER> <tr VALIGN=top><td> Value </td><td> Definition 
</td></tr> <tr VALIGN=top><td> 0h </td><td> Reserved 
</td></tr> <tr VALIGN=top><td> 1h </td><td> Write Exclusive Reservation 
</td></tr> <tr VALIGN=top><td> 2h </td><td> Exclusive Access Reservation 
</td></tr> <tr VALIGN=top><td> 3h </td><td> Write Exclusive - Registrants Only Reservation 
</td></tr> <tr VALIGN=top><td> 4h </td><td> Exclusive Access - Registrants Only Reservation 
</td></tr> <tr VALIGN=top><td> 5h </td><td> Write Exclusive - All Registrants Reservation 
</td></tr> <tr VALIGN=top><td> 6h </td><td> Exclusive Access - All Registrants Reservation 
</td></tr> <tr VALIGN=top><td> 07h-FFh </td><td> Reserved 
</td></tr> </table> 

</dl>
 

 -a &lt;racqa&gt;, --racqa=&lt;racqa&gt;
<dl>
<dt>
<dd> Reservation Acquire Action: This field specifies the action that is performed by the command. <table BORDER> <tr VALIGN=top><td> Value </td><td> Definition 
</td></tr> <tr VALIGN=top><td> 0 </td><td> Acquire 
</td></tr> <tr VALIGN=top><td> 1 </td><td> Preempt 
</td></tr> <tr VALIGN=top><td> 2 </td><td> Preempt and Abort 
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


