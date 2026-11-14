---
title: "sc_triangle(3)"
name: "sc_triangle"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_triangle/"
description: "sc::Triangle –"
---

<p>sc::Triangle &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::RefCount</code>.</p>
<h3>Public Types</h3>
<pre><code>enum { max_order = 10 }

Public Member Functions
Triangle(const Ref&lt;Edge&gt; &amp;v1, const Ref&lt;Edge&gt; &amp;v2, const Ref&lt;Edge&gt; &amp;v3, unsigned int orient0 = 0)

    Ref&lt;Edge&gt; edge(int i)

        int contains(const Ref&lt;Edge&gt; &amp;) const

    unsigned int orientation(int i) const

    unsigned int orientation(const Ref&lt;Edge&gt; &amp;) const

    void add_edges(std::set&lt;Ref&lt;Edge&gt;&gt; &amp;)

        void add_vertices(std::set&lt;Ref&lt;Vertex&gt;&gt; &amp;)

            void interpolate(const Ref&lt;TriInterpCoef&gt; &amp;, double r, double s, const Ref&lt;Vertex&gt; &amp;v, SCVector3 &amp;dA)

                void interpolate(double r, double s, const Ref&lt;Vertex&gt; &amp;v, SCVector3 &amp;dA)

                    void interpolate(double r, double s, const Ref&lt;Vertex&gt; &amp;v, SCVector3 &amp;dA, const Ref&lt;Volume&gt; &amp;vol, double isovalue)

                        Ref&lt;Vertex&gt; vertex(int i)

                            double flat_area()

                                void flip()

                                    unsigned int order() const

    void set_order(int order, const Ref&lt;Volume&gt; &amp;vol, double isovalue)

        Protected Attributes
    unsigned int _order

    unsigned int _orientation0

    unsigned int _orientation1

    unsigned int _orientation2

    Ref&lt;Edge&gt; _edges[3]

    Ref&lt;Vertex&gt; *_vertices
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
