---
title: "ecore_main_loop_group(3)"
name: "ecore_main_loop_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_main_loop_group/"
description: "Main Loop Functions – These functions control the Ecore event handling loop."
---

<p>Main Loop Functions &#8211; These functions control the Ecore event handling loop. </p>
<h3>Functions</h3>
<p>EAPI void <code>ecore_main_loop_iterate</code> (void)<br />
 <i>Runs a single iteration of the main loop to process everything on the queue. </i><br />
 EAPI void <code>ecore_main_loop_begin</code> (void)<br />
 <i>Runs the application main loop. </i><br />
 EAPI void <code>ecore_main_loop_quit</code> (void)<br />
 <i>Quits the main loop once all the events currently on the queue have been processed. </i></p>
<h2>Detailed Description</h2>
<p>These functions control the Ecore event handling loop. </p>
<p> This loop is designed to work on embedded systems all the way to large and powerful mutli-cpu workstations. </p>
<p> It serialises all system signals and events into a single event queue, that can be easily processed without needing to worry about concurrency. A properly written, event-driven program using this kind of programming does not need threads. It makes the program very robust and easy to follow. </p>
<p> Here is an example of simple program and its basic event loop flow: </p>
<p> For examples of setting up and using a main loop, see <code>event_handler_example::c</code> and <code>timer_example::c</code>.</p>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_main_loop_begin (void)</h3>
<p>Runs the application main loop. </p>
<p> This function will not return until <code>ecore_main_loop_quit</code> is called.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
