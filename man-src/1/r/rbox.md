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
</dt><dd> 10 random points in the unit cube centered at the origin.
</dd><dt>rbox 10 s D2
</dt><dd> 10 random points on a 2-d circle.
</dd><dt>rbox 100 W0
</dt><dd> 100 random points on the surface of a cube.
</dd><dt>rbox 1000 s D4
</dt><dd> 1000 random points on a 4-d sphere.
</dd><dt>rbox c D5 O0.5
</dt><dd> a 5-d hypercube with one corner at the origin.
</dd><dt>rbox d D10
</dt><dd> a 10-d diamond.
</dd><dt>rbox x 1000 r W0
</dt><dd> 100 random points on the surface of a fixed simplex
</dd><dt>rbox y D12
</dt><dd> a 12-d simplex.
</dd><dt>rbox l 10
</dt><dd> 10 random points along a spiral
</dd><dt>rbox l 10 r
</dt><dd> 10 regular points along a spiral plus two end points
</dd><dt>rbox 1000 L10000 D4 s
</dt><dd> 1000 random points on the surface of a narrow lens.
</dd><dt>rbox c G2 d G3
</dt><dd> a cube with coordinates +2/-2 and a diamond with coordinates +3/-3.
</dd><dt>rbox 64 M3,4 z
</dt><dd> a rotated, {0,1,2,3} x {0,1,2,3} x {0,1,2,3} lattice (Mesh) of integer points.
</dd><dt>rbox P0 P0 P0 P0 P0
</dt><dd> 5 copies of the origin in 3-d. Try 'rbox P0 P0 P0 P0 P0 | qhull QJ'.
</dd><dt>r 100 s Z1 G0.1
</dt><dd> two cospherical 100-gons plus another cospherical point.
</dd><dt>100 s Z1
</dt><dd> a cone of points.
</dd><dt>100 s Z1e-7
</dt><dd> a narrow cone of points with many precision errors.</dd></dl>

<h2>OPTIONS</h2>

<dl>
<dt>n
</dt><dd> number of points
</dd><dt>Dn
</dt><dd> dimension n-d (default 3-d)
</dd><dt>Bn
</dt><dd> bounding box coordinates (default 0.5)
</dd><dt>l
</dt><dd> spiral distribution, available only in 3-d
</dd><dt>Ln
</dt><dd> lens distribution of radius n. May be used with 's', 'r', 'G', and 'W'.
</dd><dt>Mn,m,r
</dt><dd> lattice (Mesh) rotated by {[n,-m,0], [m,n,0], [0,0,r], ...}. Use 'Mm,n' for a rigid rotation with r = sqrt(n^2+m^2). 'M1,0' is an orthogonal lattice. For example, '27 M1,0' is {0,1,2} x {0,1,2} x {0,1,2}.
</dd><dt>s
</dt><dd> cospherical points randomly generated in a cube and projected to the unit sphere
</dd><dt>x
</dt><dd> simplicial distribution. It is fixed for option 'r'. May be used with 'W'.
</dd><dt>y
</dt><dd> simplicial distribution plus a simplex. Both 'x' and 'y' generate the same points.
</dd><dt>Wn
</dt><dd> restrict points to distance n of the surface of a sphere or a cube
</dd><dt>c
</dt><dd> add a unit cube to the output
</dd><dt>c Gm
</dt><dd> add a cube with all combinations of +m and -m to the output
</dd><dt>d
</dt><dd> add a unit diamond to the output.
</dd><dt>d Gm
</dt><dd> add a diamond made of 0, +m and -m to the output
</dd><dt>Pn,m,r
</dt><dd> add point [n,m,r] to the output first. Pad coordinates with 0.0.
</dd><dt>n
</dt><dd> Remove the command line from the first line of output.
</dd><dt>On
</dt><dd> offset the data by adding n to each coordinate.
</dd><dt>t
</dt><dd> use time in seconds as the random number seed (default is command line).
</dd><dt>tn
</dt><dd> set the random number seed to n.
</dd><dt>z
</dt><dd> generate integer coordinates. Use 'Bn' to change the range. The default is 'B1e6' for six-digit coordinates. In R^4, seven-digit coordinates will overflow hyperplane normalization.
</dd><dt>Zn s
</dt><dd> restrict points to a disk about the z+ axis and the sphere (default Z1.0). Includes the opposite pole. 'Z1e-6' generates degenerate points under single precision.
</dd><dt>Zn Gm s
</dt><dd> same as Zn with an empty center (default G0.5).
</dd><dt>r s D2
</dt><dd> generate a regular polygon
</dd><dt>r s Z1 G0.1
</dt><dd> generate a regular cone</dd></dl>

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


