---
title: "crm_ticket(8)"
name: "crm_ticket"
section: "8"
letter: "c"
url: "/docs/linux/man/8-crm_ticket/"
description: "Pacemaker – Part of the Pacemaker cluster resource manager"
---

<p>Pacemaker &#8211; Part of the Pacemaker cluster resource manager</p>
<h2>Synopsis</h2>
<p><code>crm_ticket</code> <i>(query|command) </i>[<i>options</i>]</p>
<h2>Description</h2>
<p>crm_ticket &#8211; Perform tasks related to cluster tickets. Allows ticket attributes to be queried, modified and deleted.</p>
<h2>Options</h2>
<dl>
<dt>-?, <code>&#8211;help</code></p>
<dd>This text</p>
<dt>-$, <code>&#8211;version</code></p>
<dd>Version information</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd>Increase debug output</p>
<dt><code>-Q</code>, <code>&#8211;quiet</code></p>
<dd>Print only the value on stdout</p>
<dt><code>-t</code>, <code>&#8211;ticket</code>=<i>value</i></p>
<dd>Ticket ID</dl>
<h3>Queries:</h3>
<dl>
<dt><code>-l</code>, <code>&#8211;info</code></p>
<dd>Display the information of ticket(s)</p>
<dt><code>-L</code>, <code>&#8211;details</code></p>
<dd>Display the details of ticket(s)</p>
<dt><code>-w</code>, <code>&#8211;raw</code></p>
<dd>Display the IDs of ticket(s)</p>
<dt><code>-q</code>, <code>&#8211;query-xml</code></p>
<dd>Query the XML of ticket(s)</p>
<dt><code>-c</code>, <code>&#8211;constraints</code></p>
<dd>Display the rsc_ticket constraints that apply to ticket(s)</dl>
<h3>Commands:</h3>
<dl>
<dt><code>-g</code>, <code>&#8211;grant</code></p>
<dd>Grant a ticket to this cluster site</p>
<dt><code>-r</code>, <code>&#8211;revoke</code></p>
<dd>Revoke a ticket from this cluster site</p>
<dt><code>-s</code>, <code>&#8211;standby</code></p>
<dd>Tell this cluster site this ticket is standby</p>
<dt><code>-a</code>, <code>&#8211;activate</code></p>
<dd>Tell this cluster site this ticket is active</dl>
<h3>Advanced Commands:</h3>
<dl>
<dt><code>-G</code>, <code>&#8211;get-attr</code>=<i>value</i></p>
<dd>Display the named attribute for a ticket</p>
<dt><code>-S</code>, <code>&#8211;set-attr</code>=<i>value</i></p>
<dd>Set the named attribtue for a ticket</p>
<dt><code>-D</code>, <code>&#8211;delete-attr</code>=<i>value</i></p>
<dd>Delete the named attribute for a ticket</p>
<dt><code>-C</code>, <code>&#8211;cleanup</code></p>
<dd>Delete all state of a ticket at this cluster site</dl>
<h3>Additional Options:</h3>
<dl>
<dt><code>-v</code>, <code>&#8211;attr-value</code>=<i>value</i></p>
<dd>Attribute value to use with <code>-S</code></p>
<dt><code>-d</code>, <code>&#8211;default</code>=<i>value</i></p>
<dd>(Advanced) The default attribute value to display if none is found. For use with <code>-G</code></p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>(Advanced) Force the action to be performed</p>
<dt><code>-n</code>, <code>&#8211;set-name</code>=<i>value</i></p>
<dd>(Advanced) ID of the instance_attributes object to change</p>
<dt><code>-i</code>, <code>&#8211;nvpair</code>=<i>value</i></p>
<dd>(Advanced) ID of the nvpair object to change/delete</dl>
<h2>Examples</h2>
<p>Display the info of tickets:</p>
<dl>
<dd># crm_ticket &#8211;info</dl>
<p> Display the detailed info of tickets:</p>
<dl>
<dd># crm_ticket &#8211;details</dl>
<p> Display the XML of &#8216;ticketA&#8217;:</p>
<dl>
<dd># crm_ticket &#8211;ticket ticketA &#8211;query-xml</dl>
<p> Display the rsc_ticket constraints that apply to &#8216;ticketA&#8217;:</p>
<dl>
<dd># crm_ticket &#8211;ticket ticketA &#8211;constraints</dl>
<p> Grant &#8216;ticketA&#8217; to this cluster site:</p>
<dl>
<dd># crm_ticket &#8211;ticket ticketA &#8211;grant</dl>
<p> Revoke &#8216;ticketA&#8217; from this cluster site:</p>
<dl>
<dd># crm_ticket &#8211;ticket ticketA &#8211;revoke</dl>
<p> Make &#8216;ticketA&#8217; standby: </p>
<p> The cluster site will treat a granted &#8216;ticketA&#8217; as &#8216;standby&#8217;. The dependent resources will be stopped or demoted gracefully without triggering loss-policies</p>
<dl>
<dd># crm_ticket &#8211;ticket ticketA &#8211;standby</dl>
<p> Activate &#8216;ticketA&#8217; from being standby:</p>
<dl>
<dd># crm_ticket &#8211;ticket ticketA &#8211;activate</dl>
<p> Get the value of the &#8216;granted&#8217; attribute for &#8216;ticketA&#8217;:</p>
<dl>
<dd># crm_ticket &#8211;ticket ticketA &#8211;get-attr granted</dl>
<p> Set the value of the &#8216;standby&#8217; attribute for &#8216;ticketA&#8217;:</p>
<dl>
<dd># crm_ticket &#8211;ticket ticketA &#8211;set-attr standby &#8211;attr-value true</dl>
<p> Delete the &#8216;granted&#8217; attribute for &#8216;ticketA&#8217;:</p>
<dl>
<dd># crm_ticket &#8211;ticket ticketA &#8211;delete-attr granted</dl>
<p> Erase the operation history of &#8216;ticketA&#8217; at this cluster site: </p>
<p> The cluster site will &#8216;forget&#8217; the existing ticket state.</p>
<dl>
<dd># crm_ticket &#8211;ticket ticketA &#8211;cleanup</dl>
<h2>Author</h2>
<p>Written by Andrew Beekhof</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to pacemaker [at] oss.clusterlabs.org</p>
