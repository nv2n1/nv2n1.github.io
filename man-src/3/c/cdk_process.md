---
title: "cdk_process(3)"
name: "cdk_process"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_process/"
description: "cdk_process – curses widget pre/post-processing"
---

<h2>NAME</h2>
<p> cdk_process &#8211; curses widget pre/post-processing</p>
<h2>SYNOPSIS</h2>
<p> Perform pre- and post-processing of data which is injected into a widget.</p>
<h2>DESCRIPTION</h2>
<p> Character input is handled by each widget by its injection function. That is typically a large case-statement consisting of the actions to be taken for editing and scrolling keys. The calling application can modify the behavior of the injection function by defining either or both preprocess and postprocess functions. </p>
<p> Preprocessing is performed before doing anything with the injected keystroke. If the preprocess function returns zero, no further action is taken in the injection function. Note that the preprocess function may do more than filter out characters; it can fill in logic to coordinate different widgets. </p>
<p> Postprocessing is performed after all other actions have been done in the injection function. Like the other actions, it is performed only if the preprocess function returns a nonzero value. Unlike the preprocess function, its return value is ignored.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3). </p>
<h2>Index</h2>
