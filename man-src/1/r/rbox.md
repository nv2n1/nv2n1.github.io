---
title: "rbox(1)"
name: "rbox"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rbox/"
---

<h2>NAME</h2>

 rbox - generate point distributions for qhull

<h2>SYNOPSIS</h2>

 Command &quot;rbox&quot; (w/o arguments) lists the options.

<h2>DESCRIPTION</h2>

 

 rbox generates random or regular points according to the options given, and outputs the points to stdout. The points are generated in a cube, unless 's' or given. The format of the output is the following: first line contains the dimension and a comment, second line contains the number of points, and the following lines contain the points, one point per line. Points are represented by their coordinate values.

<h2>EXAMPLES</h2>

<dl>
<dt>rbox 10
<dd> 10 random points in the unit cube centered at the origin.
<dt>rbox 10 s D2
<dd> 10 random points on a 2-d circle.
<dt>rbox 100 W0
<dd> 100 random points on the surface of a cube.
<dt>rbox 1000 s D4
<dd> 1000 random points on a 4-d sphere.
<dt>rbox c D5 O0.5
<dd> a 5-d hypercube with one corner at the origin.
<dt>rbox d D10
<dd> a 10-d diamond.
<dt>rbox x 1000 r W0
<dd> 100 random points on the surface of a fixed simplex
<dt>rbox y D12
<dd> a 12-d simplex.
<dt>rbox l 10
<dd> 10 random points along a spiral
<dt>rbox l 10 r
<dd> 10 regular points along a spiral plus two end points
<dt>rbox 1000 L10000 D4 s
<dd> 1000 random points on the surface of a narrow lens.
<dt>rbox c G2 d G3
<dd> a cube with coordinates +2/-2 and a diamond with coordinates +3/-3.
<dt>rbox 64 M3,4 z
<dd> a rotated, {0,1,2,3} x {0,1,2,3} x {0,1,2,3} lattice (Mesh) of integer points.
<dt>rbox P0 P0 P0 P0 P0
<dd> 5 copies of the origin in 3-d. Try 'rbox P0 P0 P0 P0 P0 | qhull QJ'.
<dt>r 100 s Z1 G0.1
<dd> two cospherical 100-gons plus another cospherical point.
<dt>100 s Z1
<dd> a cone of points.
<dt>100 s Z1e-7
<dd> a narrow cone of points with many precision errors.</dl>

<h2>OPTIONS</h2>

<dl>
<dt>n
<dd> number of points
<dt>Dn
<dd> dimension n-d (default 3-d)
<dt>Bn
<dd> bounding box coordinates (default 0.5)
<dt>l
<dd> spiral distribution, available only in 3-d
<dt>Ln
<dd> lens distribution of radius n. May be used with 's', 'r', 'G', and 'W'.
<dt>Mn,m,r
<dd> lattice (Mesh) rotated by {[n,-m,0], [m,n,0], [0,0,r], ...}. Use 'Mm,n' for a rigid rotation with r = sqrt(n^2+m^2). 'M1,0' is an orthogonal lattice. For example, '27 M1,0' is {0,1,2} x {0,1,2} x {0,1,2}.
<dt>s
<dd> cospherical points randomly generated in a cube and projected to the unit sphere
<dt>x
<dd> simplicial distribution. It is fixed for option 'r'. May be used with 'W'.
<dt>y
<dd> simplicial distribution plus a simplex. Both 'x' and 'y' generate the same points.
<dt>Wn
<dd> restrict points to distance n of the surface of a sphere or a cube
<dt>c
<dd> add a unit cube to the output
<dt>c Gm
<dd> add a cube with all combinations of +m and -m to the output
<dt>d
<dd> add a unit diamond to the output.
<dt>d Gm
<dd> add a diamond made of 0, +m and -m to the output
<dt>Pn,m,r
<dd> add point [n,m,r] to the output first. Pad coordinates with 0.0.
<dt>n
<dd> Remove the command line from the first line of output.
<dt>On
<dd> offset the data by adding n to each coordinate.
<dt>t
<dd> use time in seconds as the random number seed (default is command line).
<dt>tn
<dd> set the random number seed to n.
<dt>z
<dd> generate integer coordinates. Use 'Bn' to change the range. The default is 'B1e6' for six-digit coordinates. In R^4, seven-digit coordinates will overflow hyperplane normalization.
<dt>Zn s
<dd> restrict points to a disk about the z+ axis and the sphere (default Z1.0). Includes the opposite pole. 'Z1e-6' generates degenerate points under single precision.
<dt>Zn Gm s
<dd> same as Zn with an empty center (default G0.5).
<dt>r s D2
<dd> generate a regular polygon
<dt>r s Z1 G0.1
<dd> generate a regular cone</dl>

<h2>BUGS</h2>

 Some combinations of arguments generate odd results. 

 Report bugs to qhull_bug [at] qhull.org, other correspondence to qhull [at] qhull.org

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-qhull/">qhull</a>(1)

<h2>AUTHOR</h2>

 <pre>
C. Bradford Barber
c/o The Geometry Center
400 Lind Hall
207 Church Street S.E.
Minneapolis, MN 55455
</pre> 

 

<h2>Index</h2>


