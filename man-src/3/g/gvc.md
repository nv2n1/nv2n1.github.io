---
title: "gvc(3)"
name: "gvc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gvc/"
description: "libgvc – Graphviz context library"
---

<h2>NAME</h2>
<p> <code>libgvc</code> &#8211; Graphviz context library</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;graphviz/gvc.h&gt;
/* set up a graphviz context */
extern GVC_t *gvNEWcontext(char **info, char *user);
extern char *gvUsername(void);
/*  set up a graphviz context - alternative */
/*     (wraps the above two functions using info built into libgvc) */
extern GVC_t *gvContext(void);
/* parse command line args - minimally argv[0] sets layout engine */
extern int gvParseArgs(GVC_t *gvc, int argc, char **argv);
extern graph_t *gvNextInputGraph(GVC_t *gvc);
/* Compute a layout using a specified engine */
extern int gvLayout(GVC_t *gvc, graph_t *g, char *engine);
/* Compute a layout using layout engine from command line args */
extern int gvLayoutJobs(GVC_t *gvc, graph_t *g);
/* Render layout into string attributes of the graph */
extern void attach_attrs(graph_t *g);
/* Parse an html string */
extern char *agstrdup_html(char *s);
extern int aghtmlstr(char *s);
/* Render layout in a specified format to an open FILE */
extern int gvRender(GVC_t *gvc, graph_t *g, char *format, FILE *out);
/* Render layout in a specified format to an open FILE */
extern int gvRenderFilename(GVC_t *gvc, graph_t *g, char *format, char *filename);
/* Render layout according to -T and -o options found by gvParseArgs */
extern int gvRenderJobs(GVC_t *gvc, graph_t *g);
/* Clean up layout data structures - layouts are not nestable (yet) */
extern int gvFreeLayout(GVC_t *gvc, graph_t *g);
/* Clean up graphviz context */
extern int gvFreeContext(GVC_t *gvc);
/* Inquire about available plugins */
/* See comment in gvc.h            */
extern char **gvPluginList(GVC_t *gvc, char *kind, int *cnt, char *);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>libgvc</i> provides a context for applications wishing to manipulate and render graphs. It provides a command line parsing, common rendering code, and a plugin mechanism for renderers. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dot/">dot</a></code>(1), <code><a href="/docs/linux/man/1-neato/">neato</a></code>(1), <code><a href="/docs/linux/man/3-libcdt/">libcdt</a></code>(3) <code><a href="/docs/linux/man/3-libgraph/">libgraph</a></code>(3) </p>
<h2>AUTHOR</h2>
<p> John Ellson (ellson [at] research.att.com), AT&amp;T </p>
<h2>Index</h2>
