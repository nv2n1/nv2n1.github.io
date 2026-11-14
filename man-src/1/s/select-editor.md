---
title: "select-editor(1)"
name: "select-editor"
section: "1"
letter: "s"
url: "/docs/linux/man/1-select-editor/"
description: "select-editor – select your default sensible-editor from all installed editors"
---

<h2 class="name">NAME</h2>
<p> select-editor &#8211; select your default sensible-editor from all installed editors </p>
<h2>SYNOPSIS</h2>
<p> <code>select-editor</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>select-editor</code> provides a coherent mechanism for selecting and storing a preferred sensible-editor on a per-user basis. It lists the available editors on a system and interactively prompts the user to select one. The results are stored as SELECTED_EDITOR variable in ~/.selected_editor, which is sourced and used by <code>sensible-editor</code> command. SELECTED_EDITOR variable is overridden by the VISUAL and EDITOR environment variables.</p>
<h2>AUTHOR</h2>
<p> <code>select-editor</code> was written by Dustin Kirkland &lt;kirkland [at] canonical.com&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sensible-editor/">sensible-editor</a></code>(1) </p>
<h2>Index</h2>
