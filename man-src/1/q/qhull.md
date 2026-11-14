---
title: "qhull(1)"
name: "qhull"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qhull/"
---

<h2>NAME</h2>

 qhull - convex hull, Delaunay triangulation, Voronoi diagram, halfspace intersection about a point, hull volume, facet area

<h2>SYNOPSIS</h2>

 <pre><code>
qhull- compute convex hulls and related structures
    input (stdin): dimension, #points, point coordinates
    first comment (non-numeric) is listed in the summary
    halfspace: use dim plus one with offsets after coefficients
    
options (qh-quick.htm):
    d      - Delaunay triangulation by lifting points to a paraboloid
    v      - Voronoi diagram via the Delaunay triangulation
    H1,1   - Halfspace intersection about [1,1,0,...]
    d Qu   - Furthest-site Delaunay triangulation (upper convex hull)
    v Qu   - Furthest-site Voronoi diagram
    Qt     - triangulated output
    QJ     - Joggle the input to avoid precision problems
    .      - concise list of all options
    -      - one-line description of all options
    
Output options (subset):
    FA     - compute total area and volume
    Fx     - extreme points (convex hull vertices)
    G      - Geomview output (2-d, 3-d and 4-d)
    Fp     - halfspace intersection coordinates
    m      - Mathematica output (2-d and 3-d)
    n      - normals with offsets
    o      - OFF file format (if Voronoi, outputs regions)
    TO file- output results to file, may be enclosed in single quotes
    f      - print all fields of all facets
    s      - summary of results (default)
    Tv     - verify result: structure, convexity, and point inclusion
    p      - vertex coordinates (centers for Voronoi)
    i      - vertices incident to each facet
    
example:
    rbox 1000 s | qhull Tv s FA
</code></pre> 

 
&nbsp;<wbr>- html manual:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>index.htm 
&nbsp;<wbr>- installation:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>README.txt 
&nbsp;<wbr>- see also:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>COPYING.txt, REGISTER.txt, Changes.txt 
&nbsp;<wbr>- WWW:&nbsp;<wbr>&nbsp;<wbr>&lt;<a rel="nofollow" HREF="http://www.qhull.org">http://www.qhull.org</a>&gt; 
&nbsp;<wbr>- CVS:&nbsp;<wbr>&nbsp;<wbr>&lt;<a rel="nofollow" HREF="http://savannah.nongnu.org/projects/qhull/">http://savannah.nongnu.org/projects/qhull/</a>&gt; 
&nbsp;<wbr>- mirror:&nbsp;<wbr>&lt;<a rel="nofollow" HREF="http://www6.uniovi.es/ftp/pub/mirrors/geom.umn.edu/software/ghindex.html">http://www6.uniovi.es/ftp/pub/mirrors/geom.umn.edu/software/ghindex.html</a>&gt; 
&nbsp;<wbr>- news:&nbsp;<wbr>&lt;<a rel="nofollow" HREF="http://www.qhull.org/news">http://www.qhull.org/news</a>&gt; 
&nbsp;<wbr>- Geomview:&nbsp;<wbr>&nbsp;<wbr>&lt;<a rel="nofollow" HREF="http://www.geomview.org">http://www.geomview.org</a>&gt; 
&nbsp;<wbr>- news group:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;news:comp.graphics.algorithms&gt; 
&nbsp;<wbr>- FAQ:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;<a rel="nofollow" HREF="http://exaflop.org/docs/cgafaq/cga6.html">http://exaflop.org/docs/cgafaq/cga6.html</a>&gt; 
&nbsp;<wbr>- email:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>qhull [at] qhull.org 
&nbsp;<wbr>- bug reports:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>qhull_bug [at] qhull.org 
&nbsp;<wbr> The sections are: 
&nbsp;<wbr>- INTRODUCTION 
&nbsp;<wbr>- DESCRIPTION, a description of Qhull 
&nbsp;<wbr>- IMPRECISION, how Qhull handles imprecision 
&nbsp;<wbr>- OPTIONS 
&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Input and output options 
&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Additional input/output formats 
&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Precision options 
&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Geomview options 
&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Print options 
&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Qhull options 
&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Trace options 
&nbsp;<wbr>- BUGS 
&nbsp;<wbr>- E-MAIL 
&nbsp;<wbr>- SEE ALSO 
&nbsp;<wbr>- AUTHORS 
&nbsp;<wbr>- ACKNOWLEGEMENTS 

 This man page briefly describes all Qhull options. Please report any mismatches with Qhull's html manual (index.htm). 

 

<h2>INTRODUCTION</h2>

 Qhull is a general dimension code for computing convex hulls, Delaunay triangulations, Voronoi diagram, furthest-site Voronoi diagram, furthest-site Delaunay triangulations, and halfspace intersections about a point. It implements the Quickhull algorithm for computing the convex hull. Qhull handles round-off errors from floating point arithmetic. It can approximate a convex hull. 

 The program includes options for hull volume, facet area, partial hulls, input transformations, randomization, tracing, multiple output formats, and execution statistics. The program can be called from within your application. You can view the results in 2-d, 3-d and 4-d with Geomview. 

<h2>DESCRIPTION</h2>

 

 The format of input is the following: first line contains the dimension, second line contains the number of input points, and point coordinates follow. The dimension and number of points can be reversed. Comments and line breaks are ignored. A comment starts with a non-numeric character and continues to the end of line. The first comment is reported in summaries and statistics. Error reporting is better if there is one point per line. 

 The default printout option is a short summary. There are many other output formats. 

 Qhull implements the Quickhull algorithm for convex hull. This algorithm combines the 2-d Quickhull algorithm with the n-d beneath-beyond algorithm [c.f., Preparata &amp; Shamos '85]. It is similar to the randomized algorithms of Clarkson and others [Clarkson et al. '93]. The main advantages of Quickhull are output sensitive performance, reduced space requirements, and automatic handling of precision problems. 

 The data structure produced by Qhull consists of vertices, ridges, and facets. A vertex is a point of the input set. A ridge is a set of d vertices and two neighboring facets. For example in 3-d, a ridge is an edge of the polyhedron. A facet is a set of ridges, a set of neighboring facets, a set of incident vertices, and a hyperplane equation. For simplicial facets, the ridges are defined by the vertices and neighboring facets. When Qhull merges two facets, it produces a non-simplicial facet. A non-simplicial facet has more than d neighbors and may share more than one ridge with a neighbor. 

<h2>IMPRECISION</h2>

 

 Since Qhull uses floating point arithmetic, roundoff error may occur for each calculation. This causes problems for most geometric algorithms. 

 Qhull automatically sets option 'C-0' in 2-d, 3-d, and 4-d, or option 'Qx' in 5-d and higher. These options handle precision problems by merging facets. Alternatively, use option 'QJ' to joggle the input. 

 With 'C-0', Qhull merges non-convex facets while constructing the hull. The remaining facets are clearly convex. With 'Qx', Qhull merges coplanar horizon facets, flipped facets, concave facets and duplicated ridges. It merges coplanar facets after constructing the hull. With 'Qx', coplanar points may be missed, but it appears to be unlikely. 

 To guarantee triangular output, joggle the input with option 'QJ'. Facet merging will not occur.

<h2>OPTIONS</h2>

 

 To get a list of the most important options, execute 'qhull' by itself. To get a complete list of options, execute 'qhull -'. To get a complete, concise list of options, execute 'qhull .'. 

 Options can be in any order. Capitalized options take an argument (except 'PG' and 'F' options). Single letters are used for output formats and precision constants. The other options are grouped into menus for other output formats ('F'), Geomview output ('G'), printing ('P'), Qhull control ('Q'), and tracing ('T').
<dl>
<dt>Main options:
<dd>
<dt>default
<dd> Compute the convex hull of the input points. Report a summary of the result.
<dt>d
<dd> Compute the Delaunay triangulation by lifting the input points to a paraboloid. The 'o' option prints the input points and facets. The 'QJ' option guarantees triangular output. The 'Ft' option prints a triangulation. It adds points (the centrums) to non-simplicial facets.
<dt>v
<dd> Compute the Voronoi diagram from the Delaunay triangulation. The 'p' option prints the Voronoi vertices. The 'o' option prints the Voronoi vertices and the vertices in each Voronoi region. It lists regions in site ID order. The 'Fv' option prints each ridge of the Voronoi diagram. The first or zero'th vertex indicates the infinity vertex. Its coordinates are qh_INFINITE (-10.101). It indicates unbounded Voronoi regions or degenerate Delaunay triangles.
<dt>Hn,n,...
<dd> Compute halfspace intersection about [n,n,0,...]. The input is a set of halfspaces defined in the same format as 'n', 'Fo', and 'Fi'. Use 'Fp' to print the intersection points. Use 'Fv' to list the intersection points for each halfspace. The other output formats display the dual convex hull. 

 The point [n,n,n,...] is a feasible point for the halfspaces, i.e., a point that is inside all of the halfspaces (Hx+b &lt;= 0). The default coordinate value is 0. 

 The input may start with a feasible point. If so, use 'H' by itself. The input starts with a feasible point when the first number is the dimension, the second number is &quot;1&quot;, and the coordinates complete a line. The 'FV' option produces a feasible point for a convex hull.
<dt>d Qu
<dd> Compute the furthest-site Delaunay triangulation from the upper convex hull. The 'o' option prints the input points and facets. The 'QJ' option guarantees triangular otuput. You can also use facets.
<dt>v Qu
<dd> Compute the furthest-site Voronoi diagram. The 'p' option prints the Voronoi vertices. The 'o' option prints the Voronoi vertices and the vertices in each Voronoi region. The 'Fv' option prints each ridge of the Voronoi diagram. The first or zero'th vertex indicates the infinity vertex at infinity. Its coordinates are qh_INFINITE (-10.101). It indicates unbounded Voronoi regions and degenerate Delaunay triangles.</dl>
 

<dl>
<dt>Input/Output options:
<dd>
<dt>f
<dd> Print out all facets and all fields of each facet.
<dt>G
<dd> Output the hull in Geomview format. For imprecise hulls, Geomview displays the inner and outer hull. Geomview can also display points, ridges, vertices, coplanar points, and facet intersections. See below for a list of options. 

 For Delaunay triangulations, 'G' displays the corresponding paraboloid. For halfspace intersection, 'G' displays the dual polytope.
<dt>i
<dd> Output the incident vertices for each facet. Qhull prints the number of facets followed by the vertices of each facet. One facet is printed per line. The numbers are the 0-relative indices of the corresponding input points. The facets are oriented. 

 In 4-d and higher, Qhull triangulates non-simplicial facets. Each apex (the first vertex) is a created point that corresponds to the facet's centrum. Its index is greater than the indices of the input points. Each base corresponds to a simplicial ridge between two facets. To print the vertices without triangulation, use option 'Fv'.
<dt>m
<dd> Output the hull in Mathematica format. Qhull writes a Mathematica file for 2-d and 3-d convex hulls and for 2-d Delaunay triangulations. Qhull produces a list of objects that you can assign to a variable in Mathematica, for example: &quot;list= &lt;&lt; &lt;outputfilename&gt; &quot;. If the object is 2-d, it can be visualized by &quot;Show[Graphics[list]] &quot;. For 3-d objects the command is &quot;Show[Graphics3D[list]]&quot;.
<dt>n
<dd> Output the normal equation for each facet. Qhull prints the dimension (plus one), the number of facets, and the normals for each facet. The facet's offset follows its normal coefficients.
<dt>o
<dd> Output the facets in OFF file format. Qhull prints the dimension, number of points, number of facets, and number of ridges. Then it prints the coordinates of the input points and the vertices for each facet. Each facet is on a separate line. The first number is the number of vertices. The remainder are the indices of the corresponding points. The vertices are oriented in 2-d, 3-d, and in simplicial facets. 

 For 2-d Voronoi diagrams, the vertices are sorted by adjacency, but not oriented. In 3-d and higher, the Voronoi vertices are sorted by index. See the 'v' option for more information.
<dt>p
<dd> Output the coordinates of each vertex point. Qhull prints the dimension, the number of points, and the coordinates for each vertex. With the 'Gc' and 'Gi' options, it also prints coplanar and interior points. For Voronoi diagrams, it prints the coordinates of each Voronoi vertex.
<dt>s
<dd> Print a summary to stderr. If no output options are specified at all, a summary goes to stdout. The summary lists the number of input points, the dimension, the number of vertices in the convex hull, the number of facets in the convex hull, the number of good facets (if 'Pg'), and statistics. 

 The last two statistics (if needed) measure the maximum distance from a point or vertex to a facet. The number in parenthesis (e.g., 2.1x) is the ratio between the maximum distance and the worst-case distance due to merging two simplicial facets.</dl>
 

<dl>
<dt>Precision options
<dd>
<dt>An
<dd> Maximum angle given as a cosine. If the angle between a pair of facet normals is greater than n, Qhull merges one of the facets into a neighbor. If 'n' is negative, Qhull tests angles after adding each point to the hull (pre-merging). If 'n' is positive, Qhull tests angles after constructing the hull (post-merging). Both pre- and post-merging can be defined. 

 Option 'C0' or 'C-0' is set if the corresponding 'Cn' or 'C-n' is not set. If 'Qx' is set, then 'A-n' and 'C-n' are checked after the hull is constructed and before 'An' and 'Cn' are checked.
<dt>Cn
<dd> Centrum radius. If a centrum is less than n below a neighboring facet, Qhull merges one of the facets. If 'n' is negative or '-0', Qhull tests and merges facets after adding each point to the hull. This is called &quot;pre-merging&quot;. If 'n' is positive, Qhull tests for convexity after constructing the hull (&quot;post-merging&quot;). Both pre- and post-merging can be defined. 

 For 5-d and higher, 'Qx' should be used instead of 'C-n'. Otherwise, most or all facets may be merged together.
<dt>En
<dd> Maximum roundoff error for distance computations.
<dt>Rn
<dd> Randomly perturb distance computations up to +/- n * max_coord. This option perturbs every distance, hyperplane, and angle computation. To use time as the random number seed, use option 'QR-1'.
<dt>Vn
<dd> Minimum distance for a facet to be visible. A facet is visible if the distance from the point to the facet is greater than 'Vn'. 

 Without merging, the default value for 'Vn' is the round-off error ('En'). With merging, the default value is the pre-merge centrum ('C-n') in 2-d or 3--d, or three times that in other dimensions. If the outside width is specified ('Wn'), the maximum, default value for 'Vn' is 'Wn'.
<dt>Un
<dd> Maximum distance below a facet for a point to be coplanar to the facet. The default value is 'Vn'.
<dt>Wn
<dd> Minimum outside width of the hull. Points are added to the convex hull only if they are clearly outside of a facet. A point is outside of a facet if its distance to the facet is greater than 'Wn'. The normal value for 'Wn' is 'En'. If the user specifies pre-merging and does not set 'Wn', than 'Wn' is set to the premerge 'Cn' and maxcoord*(1-An).</dl>
 

<dl>
<dt>Additional input/output formats
<dd>
<dt>Fa
<dd> Print area for each facet. For Delaunay triangulations, the area is the area of the triangle. For Voronoi diagrams, the area is the area of the dual facet. Use 'PAn' for printing the n largest facets, and option 'PFn' for printing facets larger than 'n'. 

 The area for non-simplicial facets is the sum of the areas for each ridge to the centrum. Vertices far below the facet's hyperplane are ignored. The reported area may be significantly less than the actual area.
<dt>FA
<dd> Compute the total area and volume for option 's'. It is an approximation for non-simplicial facets (see 'Fa').
<dt>Fc
<dd> Print coplanar points for each facet. The output starts with the number of facets. Then each facet is printed one per line. Each line is the number of coplanar points followed by the point ids. Option 'Qi' includes the interior points. Each coplanar point (interior point) is assigned to the facet it is furthest above (resp., least below).
<dt>FC
<dd> Print centrums for each facet. The output starts with the dimension followed by the number of facets. Then each facet centrum is printed, one per line.
<dt>Fd
<dd> Read input in cdd format with homogeneous points. The input starts with comments. The first comment is reported in the summary. Data starts after a &quot;begin&quot; line. The next line is the number of points followed by the dimension+1 and &quot;real&quot; or &quot;integer&quot;. Then the points are listed with a leading &quot;1&quot; or &quot;1.0&quot;. The data ends with an &quot;end&quot; line. 

 For halfspaces ('Fd Hn,n,...'), the input format is the same. Each halfspace starts with its offset. The sign of the offset is the opposite of Qhull's convention.
<dt>FD
<dd> Print normals ('n', 'Fo', 'Fi') or points ('p') in cdd format. The first line is the command line that invoked Qhull. Data starts with a &quot;begin&quot; line. The next line is the number of normals or points followed by the dimension+1 and &quot;real&quot;. Then the normals or points are listed with the offset before the coefficients. The offset for points is 1.0. The offset for normals has the opposite sign. The data ends with an &quot;end&quot; line.
<dt>FF
<dd> Print facets (as in 'f') without printing the ridges.
<dt>Fi
<dd> Print inner planes for each facet. The inner plane is below all vertices.
<dt>Fi
<dd> Print separating hyperplanes for bounded, inner regions of the Voronoi diagram. The first line is the number of ridges. Then each hyperplane is printed, one per line. A line starts with the number of indices and floats. The first pair lists adjacent input sites, the next d floats are the normalized coefficients for the hyperplane, and the last float is the offset. The hyperplane is oriented toward verify that the hyperplanes are perpendicular bisectors. Use 'Fo' for unbounded regions, and 'Fv' for the corresponding Voronoi vertices.
<dt>FI
<dd> Print facet identifiers.
<dt>Fm
<dd> Print number of merges for each facet. At most 511 merges are reported for a facet. See 'PMn' for printing the facets with the most merges.
<dt>FM
<dd> Output the hull in Maple format. Qhull writes a Maple file for 2-d and 3-d convex hulls and for 2-d Delaunay triangulations. Qhull produces a '.mpl' file for displaying with display3d().
<dt>Fn
<dd> Print neighbors for each facet. The output starts with the number of facets. Then each facet is printed one per line. Each line is the number of neighbors followed by an index for each neighbor. The indices match the other facet output formats. 

 A negative index indicates an unprinted facet due to printing only good facets ('Pg'). It is the negation of the facet's ID (option 'FI'). For example, negative indices are used for facets &quot;at infinity&quot; in the Delaunay triangulation.
<dt>FN
<dd> Print vertex neighbors or coplanar facet for each point. The first line is the number of points. Then each point is printed, one per line. If the point is coplanar, the line is &quot;1&quot; followed by the facet's ID. If the point is not a selected vertex, the line is &quot;0&quot;. Otherwise, each line is the number of neighbors followed by the corresponding facet indices (see 'Fn').
<dt>Fo
<dd> Print outer planes for each facet in the same format as 'n'. The outer plane is above all points.
<dt>Fo
<dd> Print separating hyperplanes for unbounded, outer regions of the Voronoi diagram. The first line is the number of ridges. Then each hyperplane is printed, one per line. A line starts with the number of indices and floats. The first pair lists adjacent input sites, the next d floats are the normalized coefficients for the hyperplane, and the last float is the offset. The hyperplane is oriented toward verify that the hyperplanes are perpendicular bisectors. Use 'Fi' for bounded regions, and 'Fv' for the corresponding Voronoi vertices.
<dt>FO
<dd> List all options to stderr, including the default values. Additional 'FO's are printed to stdout.
<dt>Fp
<dd> Print points for halfspace intersections (option 'Hn,n,...'). Each intersection corresponds to a facet of the dual polytope. The &quot;infinity&quot; point [-10.101,-10.101,...] indicates an unbounded intersection.
<dt>FP
<dd> For each coplanar point ('Qc') print the point ID of the nearest vertex, the point ID, the facet ID, and the distance.
<dt>FQ
<dd> Print command used for qhull and input.
<dt>Fs
<dd> Print a summary. The first line consists of the number of integers (&quot;8&quot;), followed by the dimension, the number of points, the number of vertices, the number of facets, the number of vertices selected for output, the number of facets selected for output, the number of coplanar points selected for output, number of simplicial, unmerged facets in output 

 The second line consists of the number of reals (&quot;2&quot;), followed by the maxmimum offset to an outer plane and and minimum offset to an inner plane. Roundoff is included. Later versions of Qhull may produce additional integers or reals.
<dt>FS
<dd> Print the size of the hull. The first line consists of the number of integers (&quot;0&quot;). The second line consists of the number of reals (&quot;2&quot;), followed by the total facet area, and the total volume. Later versions of Qhull may produce additional integers or reals. 

 The total volume measures the volume of the intersection of the halfspaces defined by each facet. Both area and volume are approximations for non-simplicial facets. See option 'Fa'.
<dt>Ft
<dd> Print a triangulation with added points for non-simplicial facets. The first line is the dimension and the second line is the number of points and the number of facets. The points follow, one per line, then the facets follow as a list of point indices. With option points include the point-at-infinity.
<dt>Fv
<dd> Print vertices for each facet. The first line is the number of facets. Then each facet is printed, one per line. Each line is the number of vertices followed by the corresponding point ids. Vertices are listed in the order they were added to the hull (the last one is first).
<dt>Fv
<dd> Print all ridges of a Voronoi diagram. The first line is the number of ridges. Then each ridge is printed, one per line. A line starts with the number of indices. The first pair lists adjacent input sites, the remaining indices list Voronoi vertices. Vertex '0' indicates the vertex-at-infinity (i.e., an unbounded ray). In 3-d, the vertices are listed in order. See 'Fi' and 'Fo' for separating hyperplanes.
<dt>FV
<dd> Print average vertex. The average vertex is a feasible point for halfspace intersection.
<dt>Fx
<dd> List extreme points (vertices) of the convex hull. The first line is the number of points. The other lines give the indices of the corresponding points. The first point is '0'. In 2-d, the points occur in counter-clockwise order; otherwise they occur in input order. For Delaunay triangulations, 'Fx' lists the extreme points of the input sites. The points are unordered.</dl>
 

<dl>
<dt>Geomview options
<dd>
<dt>G
<dd> Produce a file for viewing with Geomview. Without other options, Qhull displays edges in 2-d, outer planes in 3-d, and ridges in 4-d. A ridge can be explicit or implicit. An explicit ridge is a dim-1 dimensional simplex between two facets. In 4-d, the explicit ridges are triangles. When displaying a ridge in 4-d, Qhull projects the ridge's vertices to one of its facets' hyperplanes. Use 'Gh' to project ridges to the intersection of both hyperplanes.
<dt>Ga
<dd> Display all input points as dots.
<dt>Gc
<dd> Display the centrum for each facet in 3-d. The centrum is defined by a green radius sitting on a blue plane. The plane corresponds to the facet's hyperplane. The radius is defined by 'C-n' or 'Cn'.
<dt>GDn
<dd> Drop dimension n in 3-d or 4-d. The result is a 2-d or 3-d object.
<dt>Gh
<dd> Display hyperplane intersections in 3-d and 4-d. In 3-d, the intersection is a black line. It lies on two neighboring hyperplanes (c.f., the blue squares associated with centrums ('Gc')). In 4-d, the ridges are projected to the intersection of both hyperplanes.
<dt>Gi
<dd> Display inner planes in 2-d and 3-d. The inner plane of a facet is below all of its vertices. It is parallel to the facet's hyperplane. The inner plane's color is the opposite (1-r,1-g,1-b) of the outer plane. Its edges are determined by the vertices.
<dt>Gn
<dd> Do not display inner or outer planes. By default, Geomview displays the precise plane (no merging) or both inner and output planes (merging). Under merging, Geomview does not display the inner plane if the the difference between inner and outer is too small.
<dt>Go
<dd> Display outer planes in 2-d and 3-d. The outer plane of a facet is above all input points. It is parallel to the facet's hyperplane. Its color is determined by the facet's normal, and its edges are determined by the vertices.
<dt>Gp
<dd> Display coplanar points and vertices as radii. A radius defines a ball which corresponds to the imprecision of the point. The imprecision is the maximum of the roundoff error, the centrum radius, and maxcoord * (1-An). It is at least 1/20'th of the maximum coordinate, and ignores post-merging if pre-merging is done.
<dt>Gr
<dd> Display ridges in 3-d. A ridge connects the two vertices that are shared by neighboring facets. Ridges are always displayed in 4-d.
<dt>Gt
<dd> A 3-d Delaunay triangulation looks like a convex hull with interior facets. Option 'Gt' removes the outside ridges to reveal the outermost facets. It automatically sets options 'Gr' and 'GDn'.
<dt>Gv
<dd> Display vertices as spheres. The radius of the sphere corresponds to the imprecision of the data. See 'Gp' for determining the radius.</dl>
 

<dl>
<dt>Print options
<dd>
<dt>PAn
<dd> Only the n largest facets are marked good for printing. Unless 'PG' is set, 'Pg' is automatically set.
<dt>Pdk:n
<dd> Drop facet from output if normal[k] &lt;= n. The option 'Pdk' uses the default value of 0 for n.
<dt>PDk:n
<dd> Drop facet from output if normal[k] &gt;= n. The option 'PDk' uses the default value of 0 for n.
<dt>PFn
<dd> Only facets with area at least 'n' are marked good for printing. Unless 'PG' is set, 'Pg' is automatically set.
<dt>Pg
<dd> Print only good facets. A good facet is either visible from a point (the 'QGn' option) or includes a point (the 'QVn' option). It also meets the requirements of 'Pdk' and 'PDk' options. Option 'Pg' is automatically set for options 'PAn' and 'PFn'.
<dt>PG
<dd> Print neighbors of good facets.
<dt>PMn
<dd> Only the n facets with the most merges are marked good for printing. Unless 'PG' is set, 'Pg' is automatically set.
<dt>Po
<dd> Force output despite precision problems. Verify ('Tv') does not check coplanar points. Flipped facets are reported and concave facets are counted. If 'Po' is used, points are not partitioned into flipped facets and a flipped facet is always visible to a point. Also, if an error occurs before the completion of Qhull and tracing is not active, 'Po' outputs a neighborhood of the erroneous facets (if any).
<dt>Pp
<dd> Do not report precision problems.</dl>
 

<dl>
<dt>Qhull control options
<dd>
<dt>Qbk:0Bk:0
<dd> Drop dimension k from the input points. This allows the user to take convex hulls of sub-dimensional objects. It happens before the Delaunay and Voronoi transformation.
<dt>QbB
<dd> Scale the input points to fit the unit cube. After scaling, the lower bound will be -0.5 and the upper bound +0.5 in all dimensions. For Delaunay and Voronoi diagrams, scaling happens after projection to the paraboloid. Under precise arithmetic, scaling does not change the topology of the convex hull.
<dt>Qbb
<dd> Scale the last coordinate to [0, m] where m is the maximum absolute value of the other coordinates. For Delaunay and Voronoi diagrams, scaling happens after projection to the paraboloid. It reduces roundoff error for inputs with integer coordinates. Under precise arithmetic, scaling does not change the topology of the convex hull.
<dt>Qbk:n
<dd> Scale the k'th coordinate of the input points. After scaling, the lower bound of the input points will be n. 'Qbk' scales to -0.5.
<dt>QBk:n
<dd> Scale the k'th coordinate of the input points. After scaling, the upper bound will be n. 'QBk' scales to +0.5.
<dt>Qc
<dd> Keep coplanar points with the nearest facet. Output formats 'p', 'f', 'Gp', 'Fc', 'FN', and 'FP' will print the points.
<dt>Qf
<dd> Partition points to the furthest outside facet.
<dt>Qg
<dd> Only build good facets. With the 'Qg' option, Qhull will only build those facets that it needs to determine the good facets in the output. See 'QGn', 'QVn', and 'PdD' for defining good facets, and 'Pg' and 'PG' for printing good facets and their neighbors.
<dt>QGn
<dd> A facet is good (see 'Qg' and 'Pg') if it is visible from point n. If n &lt; 0, a facet is good if it is not visible from point n. Point n is not added to the hull (unless 'TCn' or 'TPn'). With rbox, use the 'Pn,m,r' option to define your point; it will be point 0 (QG0).
<dt>Qi
<dd> Keep interior points with the nearest facet. Output formats 'p', 'f', 'Gp', 'FN', 'FP', and 'Fc' will print the points.
<dt>QJn
<dd> Joggle each input coordinate by adding a random number in [-n,n]. If a precision error occurs, then qhull increases n and tries again. It does not increase n beyond a certain value, and it stops after a certain number of attempts [see user.h]. Option 'QJ' selects a default value for n. The output will be simplicial. For Delaunay triangulations, 'QJn' sets 'Qbb' to scale the last coordinate (not if 'Qbk:n' or 'QBk:n' is set). See also 'Qt'.
<dt>Qm
<dd> Only process points that would otherwise increase max_outside. Other points are treated as coplanar or interior points.
<dt>Qr
<dd> Process random outside points instead of furthest ones. This makes Qhull equivalent to the randomized incremental algorithms. CPU time is not reported since the randomization is inefficient.
<dt>QRn
<dd> Randomly rotate the input points. If n=0, use time as the random number seed. If n&gt;0, use n as the random number seed. If n=-1, don't rotate but use time as the random number seed. For Delaunay triangulations ('d' and 'v'), rotate about the last axis.
<dt>Qs
<dd> Search all points for the initial simplex.
<dt>Qt
<dd> Triangulated output. Triangulate all non-simplicial facets. See also 'QJ'.
<dt>Qv
<dd> Test vertex neighbors for convexity after post-merging. To use the 'Qv' option, you also need to set a merge option (e.g., 'Qx' or 'C-0').
<dt>QVn
<dd> A good facet (see 'Qg' and 'Pg') includes point n. If n&lt;0, then a good facet does not include point n. The point is either in the initial simplex or it is the first point added to the hull. Option 'QVn' may not be used with merging.
<dt>Qx
<dd> Perform exact merges while building the hull. The &quot;exact&quot; merges are merging a point into a coplanar facet (defined by 'Vn', 'Un', and 'C-n'), merging concave facets, merging duplicate ridges, and merging flipped facets. Coplanar merges and angle coplanar merges ('A-n') are not performed. Concavity testing is delayed until a merge occurs. 

 After the hull is built, all coplanar merges are performed (defined by 'C-n' and 'A-n'), then post-merges are performed (defined by 'Cn' and 'An').
<dt>Qz
<dd> Add a point &quot;at infinity&quot; that is above the paraboloid for Delaunay triangulations and Voronoi diagrams. This reduces precision problems and allows the triangulation of cospherical points.</dl>
 

<dl>
<dt>Qhull experiments and speedups
<dd>
<dt>Q0
<dd> Turn off pre-merging as a default option. With 'Q0'/'Qx' and without explicit pre-merge options, Qhull ignores precision issues while constructing the convex hull. This may lead to precision errors. If so, a descriptive warning is generated.
<dt>Q1
<dd> With 'Q1', Qhull sorts merges by type (coplanar, angle coplanar, concave) instead of by angle.
<dt>Q2
<dd> With 'Q2', Qhull merges all facets at once instead of using independent sets of merges and then retesting.
<dt>Q3
<dd> With 'Q3', Qhull does not remove redundant vertices.
<dt>Q4
<dd> With 'Q4', Qhull avoids merges of an old facet into a new facet.
<dt>Q5
<dd> With 'Q5', Qhull does not correct outer planes at the end. The maximum outer plane is used instead.
<dt>Q6
<dd> With 'Q6', Qhull does not pre-merge concave or coplanar facets.
<dt>Q7
<dd> With 'Q7', Qhull processes facets in depth-first order instead of breadth-first order.
<dt>Q8
<dd> With 'Q8' and merging, Qhull does not retain near-interior points for adjusting outer planes. 'Qc' will probably retain all points that adjust outer planes.
<dt>Q9
<dd> With 'Q9', Qhull processes the furthest of all outside sets at each iteration.
<dt>Q10
<dd> With 'Q10', Qhull does not use special processing for narrow distributions.
<dt>Q11
<dd> With 'Q11', Qhull copies normals and recompute centrums for tricoplanar facets.</dl>
 

<dl>
<dt>Trace options
<dd>
<dt>Tn
<dd> Trace at level n. Qhull includes full execution tracing. 'T-1' traces events. 'T1' traces the overall execution of the program. 'T2' and 'T3' trace overall execution and geometric and topological events. 'T4' traces the algorithm. 'T5' includes information about memory allocation and Gaussian elimination.
<dt>Tc
<dd> Check frequently during execution. This will catch most inconsistency errors.
<dt>TCn
<dd> Stop Qhull after building the cone of new facets for point n. The output for 'f' includes the cone and the old hull. See also 'TVn'.
<dt>TFn
<dd> Report progress whenever more than n facets are created During post-merging, 'TFn' reports progress after more than n/2 merges.
<dt>TI file
<dd> Input data from 'file'. The filename may not include spaces or quotes.
<dt>TO file
<dd> Output results to 'file'. The name may be enclosed in single quotes.
<dt>TPn
<dd> Turn on tracing when point n is added to the hull. Trace partitions of point n. If used with TWn, turn off tracing after adding point n to the hull.
<dt>TRn
<dd> Rerun qhull n times. Usually used with 'QJn' to determine the probability that a given joggle will fail.
<dt>Ts
<dd> Collect statistics and print to stderr at the end of execution.
<dt>Tv
<dd> Verify the convex hull. This checks the topological structure, facet convexity, and point inclusion. If precision problems occurred, facet convexity is tested whether or not 'Tv' is selected. Option 'Tv' does not check point inclusion if forcing output with 'Po', or if 'Q5' is set. 

 For point inclusion testing, Qhull verifies that all points are below all outer planes (facet-&gt;maxoutside). Point inclusion is exhaustive if merging or if the facet-point product is small enough; otherwise Qhull verifies each point with a directed search (qh_findbest). 

 Point inclusion testing occurs after producing output. It prints a message to stderr unless option 'Pp' is used. This allows the user to interrupt Qhull without changing the output.
<dt>TVn
<dd> Stop Qhull after adding point n. If n &lt; 0, stop Qhull before adding point n. Output shows the hull at this time. See also 'TCn'
<dt>TMn
<dd> Turn on tracing at n'th merge.
<dt>TWn
<dd> Trace merge facets when the width is greater than n.
<dt>Tz
<dd> Redirect stderr to stdout.</dl>
 

<h2>BUGS</h2>

 Please report bugs to Brad Barber at qhull_bug [at] qhull.org. 

 If Qhull does not compile, it is due to an incompatibility between your system and ours. The first thing to check is that your compiler is ANSI standard. If it is, check the man page for the best options, or find someone to help you. If you locate the cause of your problem, please send email since it might help others. 

 If Qhull compiles but crashes on the test case (rbox D4), there's still incompatibility between your system and ours. Typically it's been due to mem.c and memory alignment. You can use qh_NOmem in mem.h to turn off memory management. Please let us know if you figure out how to fix these problems. 

 If you do find a problem, try to simplify it before reporting the error. Try different size inputs to locate the smallest one that causes an error. You're welcome to hunt through the code using the execution trace as a guide. This is especially true if you're incorporating Qhull into your own program. 

 When you do report an error, please attach a data set to the end of your message. This allows us to see the error for ourselves. Qhull is maintained part-time. 

<h2>E-MAIL</h2>

 Please send correspondence to qhull [at] qhull.org and report bugs to qhull_bug [at] qhull.org. Let us know how you use Qhull. If you mention it in a paper, please send the reference and an abstract. 

 If you would like to get Qhull announcements (e.g., a new version) and news (any bugs that get fixed, etc.), let us know and we will add you to our mailing list. If you would like to communicate with other Qhull users, we will add you to the qhull_users alias. For Internet news about geometric algorithms and convex hulls, look at comp.graphics.algorithms and sci.math.num-analysis 

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-rbox/">rbox</a>(1) 

 Barber, C. B., D.P. Dobkin, and H.T. Huhdanpaa, &quot;The Quickhull Algorithm for Convex Hulls,&quot; ACM Trans. on Mathematical Software, <a HREF="/docs/linux/man/4-22/">22</a>(4):469-483, Dec. 1996. <a rel="nofollow" HREF="http://www.acm.org/pubs/citations/journals/toms/1996-22-4/p469-barber/">http://www.acm.org/pubs/citations/journals/toms/1996-22-4/p469-barber/</a> <a rel="nofollow" HREF="http://citeseer.nj.nec.com/83502.html">http://citeseer.nj.nec.com/83502.html</a> 

 Clarkson, K.L., K. Mehlhorn, and R. Seidel, &quot;Four results on randomized incremental construction,&quot; Computational Geometry: Theory and Applications, vol. 3, p. 185-211, 1993. 

 Preparata, F. and M. Shamos, Computational Geometry, Springer-Verlag, New York, 1985. 

 

<h2>AUTHORS</h2>

 <pre><code>
C.Bradford Barber Hannu Huhdanpaa
        bradb[at] qhull.org hannu[at] qhull.org

            c /
    o The Geometry Center
        University of Minnesota 400 Lind Hall 207 Church Street S.E.Minneapolis,
    MN 55455
</code></pre> 

<h2>ACKNOWLEDGEMENTS</h2>

 

 A special thanks to Albert Marden, Victor Milenkovic, the Geometry Center, Harvard University, and Endocardial Solutions, Inc. for supporting this work. 

 Qhull 1.0 and 2.0 were developed under National Science Foundation grants NSF/DMS-8920161 and NSF-CCR-91-15793 750-7504. David Dobkin guided the original work at Princeton University. If you find it useful, please let us know. 

 The Geometry Center is supported by grant DMS-8920161 from the National Science Foundation, by grant DOE/DE-FG02-92ER25137 from the Department of Energy, by the University of Minnesota, and by Minnesota Technology, Inc. 

 Qhull is available from <a rel="nofollow" HREF="http://www.qhull.org">http://www.qhull.org</a> 

<h2>Index</h2>


