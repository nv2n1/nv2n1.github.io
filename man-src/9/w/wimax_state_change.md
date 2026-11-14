---
title: "wimax_state_change(9)"
name: "wimax_state_change"
section: "9"
letter: "w"
url: "/docs/linux/man/9-wimax_state_change/"
---

wimax_state_change - Set the current state of a WiMAX device

<h2>Synopsis</h2>

<pre><code>void wimax_state_change(struct wimax_dev *wimax_dev, enum wimax_st new_state);</code></pre>

<h2>Arguments</h2>

<i>wimax_dev</i>
<dl><dd><dd>WiMAX device descriptor (properly referenced)</dl>
 

 <i>new_state</i>
<dl><dd>New state to switch to</dl>

<h2>Description</h2>

This implements the state changes for the wimax devices. It will 

 - verify that the state transition is legal (for now it'll just print a warning if not) according to the table in linux/wimax.h's documentation for 'enum wimax_st'. 

 - perform the actions needed for leaving the current state and whichever are needed for entering the new state. 

 - issue a report to user space indicating the new state (and an optional payload with information about the new state).

<h2>Note</h2>

<i>wimax_dev</i> must be locked

<h2>Copyright</h2>


