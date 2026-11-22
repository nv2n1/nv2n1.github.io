---
title: "opaledports(8)"
name: "opaledports"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opaledports/"
description: "opaledports"
---

<p>opaledports </p>
<p> Toggles the beaconing LED state of HFIs, switches, and switch ports. opaledports is a useful aid for finding specific physical nodes in a crowded data center. It supports the CSV link format provided by opaextractsellinks.</p>
<h2>Syntax</h2>
<p>opaledports [-h hfi] [-p port] [-C] [-s|-d] [on|off] #8217lt; portlist.csv</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</dt>
<dd>Produces full help text. </dd>
<dt>-h <i>hfi</i></dt>
<dd>HFI to send through/to. Default is first HFI. </dd>
<dt>-p <i>port</i></dt>
<dd>Port to send through/to. Default is first active port. </dd>
<dt>-C</dt>
<dd>Clears beaconing LED on all ports. </dd>
<dd></dd></dl>
<p> <code>NOTE:</code> If -C is entered, no other options are valid. </p>
<dl>
<dt>-s</dt>
<dd>Affects source side (first node) of link only. </dd>
<dt>-d</dt>
<dd>Affects destination side (second node) of link only. </dd>
<dt>on|off</dt>
<dd>Action to perform. Options include: </dd>
<dl>
<dd>
</dd><dl>
<dd>on Turns on beaconing LED. </dd>
</dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>off Turns off beaconing LED. </dd>
</dl>
</dl>
<dt>portlist.csv</dt>
<dd>File listing the links to process. The list is of the form: </dd>
<dd>NodeGUID;PortNum;NodeType;NodeDesc;NodeGUID;PortNum;NodeType; NodeDesc;Dontcare</dd></dl>
<h2>Examples</h2>
<p>echo &quot;0x001175010165ac1d;1;FI;phkpstl035 hfi1_0&quot;|opaledports on<br/>
 opaledports on #8217lt; portlist.csv<br/>
 opaextractsellinks -F led:on | opaledports off<br/>
 opaledports -C </p>
