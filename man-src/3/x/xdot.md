---
title: "xdot(3)"
name: "xdot"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xdot/"
description: "libxdot – parsing and deparsing of xdot operations"
---

<p><code>libxdot</code> &#8211; parsing and deparsing of xdot operations</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;graphviz/xdot.h&gt;

typedef enum {
    xd_left,
    xd_center,
    xd_right
} xdot_align;

typedef struct {
    double x, y, z;
} xdot_point;

typedef struct {
    double x, y, w, h;
} xdot_rect;

typedef struct {
    int cnt;
    xdot_point *pts;
} xdot_polyline;

typedef struct {
    double x, y;
    xdot_align align;
    double width;
    char *text;
} xdot_text;

typedef struct {
    xdot_rect pos;
    char *name;
} xdot_image;

typedef struct {
    double size;
    char *name;
} xdot_font;

typedef enum {
    xd_filled_ellipse,
    xd_unfilled_ellipse,
    xd_filled_polygon,
    xd_unfilled_polygon,
    xd_filled_bezier,
    xd_unfilled_bezier,
    xd_polyline,
    xd_text,
    xd_fill_color,
    xd_pen_color,
    xd_font,
    xd_style,
    xd_image
} xdot_kind;

typedef enum {
    xop_ellipse,
    xop_polygon,
    xop_bezier,
    xop_polyline,
    xop_text,
    xop_fill_color,
    xop_pen_color,
    xop_font,
    xop_style,
    xop_image
} xop_kind;

typedef struct _xdot_op xdot_op;
typedef void (*drawfunc_t)(xdot_op *, int);
typedef void (*freefunc_t)(xdot_op *);

struct _xdot_op {
    xdot_kind kind;
    union {
        xdot_rect ellipse;      /* xd_filled_ellipse, xd_unfilled_ellipse */
        xdot_polyline polygon;  /* xd_filled_polygon, xd_unfilled_polygon */
        xdot_polyline polyline; /* xd_polyline */
        xdot_polyline bezier;   /* xd_filled_bezier,  xd_unfilled_bezier */
        xdot_text text;         /* xd_text */
        xdot_image image;       /* xd_image */
        char *color;            /* xd_fill_color, xd_pen_color */
        xdot_font font;         /* xd_font */
        char *style;            /* xd_style */
    } u;
    drawfunc_t drawfunc;
};

#define XDOT_PARSE_ERROR 1

typedef struct {
    int cnt;
    int sz;
    xdot_op *ops;
    freefunc_t freefunc;
    int flags;
} xdot;

xdot *parseXDotF(char *, drawfunc_t opfns[], int sz);
xdot *parseXDot(char *);
char *sprintXDot(xdot *);
void fprintXDot(FILE *, xdot *);
void freeXDot(xdot *);</code></pre>
<h2>Description</h2>
<p><i>libxdot</i> provides support for parsing and deparsing graphical operations specificed by the <i>xdot</i> language.</p>
<h3>Types</h3>
<h3> xdot</h3>
<p>This encapsulates a series of <i>cnt</i> xdot operations, stored in the array pointed to by <i>ops</i>. The <i>sz</i> indicates the size of each item stored in <i>ops</i>. If the user sets the <i>freefunc</i> field, this function will be called on each item in <i>ops</i> during <i>freeXDot</i> before the library does its own clean up of the item. This allows the user to free any resources stored in the item by using an expansion of the <i>xdot_op</i> structure.</p>
<h3> xdot_op</h3>
<p>A value of this type represents one xdot operation. The operation is specified by the <i>kind</i> field. The corresponding data is stored in the union <i>u</i>, with the subfield associated with a given <i>kind</i> indicated by the comments. The <i>drawfunc</i> field allows the user to attach a drawing-specific function to the operation, providing an object-based interface. These functions can be automatically attached during parsing by providing a non-NULL second argument to <i>parseXDotF</i>.</p>
<h3> xop_kind</h3>
<p>This type provides an enumeration of the allowed xdot operations. See </p>
<p>&nbsp;<wbr><a rel="nofollow" href="http://www.graphviz.org/doc/info/output.html#d:xdot">http://www.graphviz.org/doc/info/output.html#d:xdot</a>&nbsp;<wbr><br />
 for the specific semantics associated with each operation.</p>
<h3> xdot_rect</h3>
<p>This represents a rectangle. For ellipses, the <i>x</i> and <i>x</i> fields represent the center of the rectangle, and <i>w</i> and <i>h</i> give the half-width and half-height, respectively. For images, (<i>x</i>,<i>y</i>) gives the lower left corner of the rectangle, and <i>w</i> and <i>h</i> give the width and height, respectively.</p>
<h3> xdot_polyline</h3>
<p>This type encapsulates a series of <i>cnt</i> points.</p>
<h3> xdot_text</h3>
<p>A value of this type corresponds to printing the string <i>text</i> using the baseline point (<i>x</i>,<i>y</i>). The <i>width</i> field gives an approximation of how wide the printed string will be using the current font and font size. The <i>align</i> field indicates how the text should be horizontally aligned with the point (<i>x</i>,<i>y</i>).</p>
<h3> xdot_image</h3>
<p>This denotes the insertion of an image. The image source is given by <i>name</i>. The images is to be placed into the rectangle <i>pos</i>.</p>
<h3> xdot_font</h3>
<p>The fields give the name and size, in points, of a font.</p>
<h3> xdot_align</h3>
<p>This enumeration type corresponds to the xdot alignment values -1, 0 and 1 used with the text operator, or &#8216;\l&#8217;, &#8216;
&#8217; and &#8216;&#8217; used in dot text.</p>
<h3>Functions</h3>
<h3> xdot* parseXDotF (char *str, drawfunc_t* opfns, int sz)</h3>
<p>Parses the string <i>str</i> as a sequence of xdot operations and returns a pointer to the resulting <i>xdot</i> structure. The function parses as many xdot operations as it can. If some unknown or incorrect input was encountered in <i>str</i>, the <i>ops</i> and <i>cnt</i> fields will reflect the operations parsed before the error, and the <i>XDOT_PARSE_ERROR</i> bit will be set in the <i>flags</i> field. The function returns NULL if it cannot parse anything. If <i>sz</i> is non-zero, it is assumed to be the size of some structure type containing <i>xdot_op</i> as a prefix. In this case, the elements in the array pointed to by <i>ops</i> will each have size <i>sz</i>. If <i>opfns</i> is non-zero, it is taken to be any array of functions indexed by <i>xop_kind</i>. During parsing, the <i>drawfunc</i> member of <i>xop_op</i> will be set to the corresponding function in <i>opfns</i>.</p>
<h3> xdot* parseXDot (char *str)</h3>
<p>This is equivalent to <i>parseXDotF(str, 0, 0)</i> .</p>
<h3> void freeXDot (xdot* xp)</h3>
<p>This frees the resources associated with the argument. If <i>xp</i> is NULL, nothing happens.</p>
<h3> extern char* sprintXDot (xdot* xp)</h3>
<h3> extern void fprintXDot (FILE* fp, xdot* xp)</h3>
<p>These two functions deparse the argument xdot structure, producing a string representation. <i>fprintXDot</i> writes the output onto the open stream <i>fp</i>; <i>sprintXDot</i> returns a heap-allocated string. </p>
<h2>Bugs</h2>
<p>Although some small checking is done on the <i>sz</i> argument to <i>parseXDotF</i>, it is assumed it is a valid value from <i>sizeof</i> applied to some structure type containing <i>xdot_op</i> as its first field. There can be no validation of the <i>opfns</i> argument.</p>
<h2>Authors</h2>
<p>Emden R. Gansner (erg [at] research.att.com).</p>
